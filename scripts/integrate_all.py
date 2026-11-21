#!/usr/bin/env python3
"""Lossless, deterministic central registry migration; never overwrite source evidence."""
import collections
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "integration" / "generated"
OUT.mkdir(parents=True, exist_ok=True)
CANONICAL = DATA / "integration" / "canonical"
CANONICAL.mkdir(parents=True, exist_ok=True)
KINDS = ("documents", "claims", "events", "politicians", "organizations")
records = {k: collections.defaultdict(list) for k in KINDS}
sources, parse_errors, unstructured, auxiliary, partial_sources = [], [], [], [], []
id_fields = ("id", "documentId", "claimId", "eventId", "politicianId", "candidateId", "organizationId")
for path in sorted(DATA.rglob("*")):
    if not path.is_file() or path.is_relative_to(DATA / "integration"):
        continue
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    source = {"path": rel, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
              "status": "INVENTORIED", "recordCounts": {k: 0 for k in KINDS}, "unmappedRecordCount": 0}
    sources.append(source)
    if path.suffix.lower() != ".json":
        source["status"] = "NON_JSON_SOURCE_PRESERVED"
        continue
    try:
        obj = json.loads(raw.decode("utf-8-sig"))
    except Exception as exc:
        source["status"] = "PARSE_ERROR"
        parse_errors.append({"path": rel, "error": str(exc)[:250]})
        continue
    kind = path.relative_to(DATA).parts[0]
    found = unmapped = 0
    collections_to_read = []
    processed_fields = set()
    if isinstance(obj, dict):
        for typ in KINDS:
            items = obj.get(typ)
            if isinstance(items, list):
                collections_to_read.append((typ, typ, items))
                processed_fields.add(typ)
        for field in ("actors", "nodes", "people", "candidates", "newCandidates",
                      "newPoliticians", "deepenedExisting", "existingDeepened",
                      "existing_deepened", "promoted", "deepened"):
            items = obj.get(field)
            if field not in processed_fields and isinstance(items, list):
                collections_to_read.append(("politicians", field, items))
                processed_fields.add(field)
    elif isinstance(obj, list) and kind in KINDS:
        collections_to_read.append((kind, kind, obj))

    for typ, field, items in collections_to_read:
        for idx, item in enumerate(items):
            pointer = f"/{field}/{idx}"
            if not isinstance(item, dict):
                auxiliary.append({"source": rel, "pointer": pointer, "payload": item,
                                  "reason": "NON_OBJECT_REGISTRY_ITEM", "provenance": source["sha256"]})
                unmapped += 1
                continue
            ident = next((item[key] for key in id_fields
                          if isinstance(item.get(key), str) and item[key]), None)
            target_type = "organizations" if typ == "politicians" and ident and ident.startswith("org-") else typ
            if not ident and typ == "politicians":
                auxiliary.append({"source": rel, "pointer": pointer, "payload": item,
                                  "reason": "POLITICIAN_ITEM_WITHOUT_STABLE_ID", "provenance": source["sha256"]})
                unmapped += 1
                continue
            if not ident:
                ident = "urn:source:" + hashlib.sha256((rel + ":" + target_type + ":" + pointer).encode()).hexdigest()[:24]
            payload = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            records[target_type][ident].append({
                "data": item, "digest": hashlib.sha256(payload.encode()).hexdigest(),
                "source": {"path": rel, "pointer": pointer}
            })
            source["recordCounts"][target_type] += 1
            found += 1

    if found == 0 and kind in KINDS and isinstance(obj, dict) and isinstance(obj.get("id") or obj.get({"documents": "documentId", "claims": "claimId", "events": "eventId", "politicians": "politicianId", "organizations": "organizationId"}[kind]), str):
        typ = kind
        item = obj
        ident = item.get("id") or item[{"documents": "documentId", "claims": "claimId", "events": "eventId", "politicians": "politicianId", "organizations": "organizationId"}[kind]]
        payload = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        records[typ][ident].append({
            "data": item, "digest": hashlib.sha256(payload.encode()).hexdigest(),
            "source": {"path": rel, "pointer": "/"}})
        source["recordCounts"][typ] += 1
        found += 1
    source["unmappedRecordCount"] = unmapped
    if found and unmapped:
        source["status"] = "PARTIAL_RECORDS_INDEXED"
        partial_sources.append(rel)
    elif found:
        source["status"] = "RECORDS_INDEXED"
    else:
        source["status"] = "AUXILIARY_JSON_INDEXED"
    if not found:
        unstructured.append(rel)
        if not unmapped:
            auxiliary.append({"source": rel, "payload": obj, "provenance": source["sha256"],
                              "reason": "NO_RECOGNIZED_REGISTRY_RECORDS"})
            source["unmappedRecordCount"] = 1


(OUT / "auxiliary.json").write_text(
    json.dumps({"schemaVersion": 2, "records": auxiliary}, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
conflicts, exact_duplicates, totals = [], [], {}
source_outcomes = collections.defaultdict(lambda: {"integrated": 0, "conflicted": 0, "records": []})
for typ, groups in records.items():
    central = []
    for ident in sorted(groups):
        versions = groups[ident]
        unique = {}
        for version in versions:
            unique.setdefault(version["digest"], []).append(version)
        alternatives = [
            {"digest": digest, "data": variants[0]["data"],
             "provenance": [v["source"] for v in variants]}
            for digest, variants in sorted(unique.items())]
        status = "CONFLICTED" if len(alternatives) > 1 else "INTEGRATED"
        central.append({"id": ident, "integrationStatus": status,
                        "alternatives": alternatives,
                        "canonicalSelection": alternatives[0]["digest"] if len(alternatives) == 1 else None})
        for version in versions:
            outcome = source_outcomes[version["source"]["path"]]
            outcome["conflicted" if status == "CONFLICTED" else "integrated"] += 1
            outcome["records"].append({"kind": typ, "id": ident,
                                       "pointer": version["source"]["pointer"],
                                       "status": status})
        if len(alternatives) > 1:
            conflicts.append({"type": typ, "id": ident,
                              "variantCount": len(alternatives),
                              "sources": sorted(set(v["source"]["path"] for v in versions))})
        if len(versions) > len(alternatives):
            exact_duplicates.append({"type": typ, "id": ident, "copies": len(versions),
                                     "uniqueVersions": len(alternatives)})
    totals[typ] = {"sourceRecords": sum(map(len, groups.values())),
                   "uniqueIds": len(groups),
                   "conflictedIds": sum(1 for c in central if c["integrationStatus"] == "CONFLICTED")}
    # Materialize only unambiguous records into a separate, queryable central layer.
    # Conflicted identities stay in the generated alternatives registry for review.
    canonical_rows = []
    for row in central:
        if row["integrationStatus"] != "INTEGRATED":
            continue
        payload = dict(row["alternatives"][0]["data"])
        payload["id"] = row["id"]
        payload["_integration"] = {
            "id": row["id"],
            "digest": row["canonicalSelection"],
            "provenance": row["alternatives"][0]["provenance"],
        }
        canonical_rows.append(payload)
    (CANONICAL / (typ + ".json")).write_text(
        json.dumps({"schemaVersion": 1, "registryType": typ,
                    "selectionPolicy": "UNAMBIGUOUS_ONLY",
                    "records": canonical_rows}, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
    (OUT / (typ + ".json")).write_text(
        json.dumps({"schemaVersion": 2, "registryType": typ, "records": central},
                   ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
for source in sources:
    outcome = source_outcomes.get(source["path"])
    if outcome:
        source["centralMapping"] = {"integrated": outcome["integrated"],
                                    "conflicted": outcome["conflicted"]}
        source["status"] = ("PARTIAL_CANONICAL_MATERIALIZED" if source.get("unmappedRecordCount") else
                            "CONFLICT_REVIEW_REQUIRED" if outcome["conflicted"] else "CANONICAL_MATERIALIZED")
    elif source["status"] == "AUXILIARY_JSON_INDEXED":
        source["centralMapping"] = {"integrated": 0, "conflicted": 0,
                                    "reason": "NO_RECOGNIZED_REGISTRY_RECORDS"}
(OUT / "source-record-mapping.json").write_text(
    json.dumps({"schemaVersion": 1, "mapping": dict(sorted(source_outcomes.items()))},
               ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
(OUT / "sources.json").write_text(
    json.dumps({"schemaVersion": 3, "sources": sources}, ensure_ascii=False, indent=2) + chr(10),
    encoding="utf-8")
report = {"canonicalMaterialized": {k: v["uniqueIds"] - v["conflictedIds"] for k, v in totals.items()},
          "canonicalDirectory": "data/integration/canonical",
          "sourceFiles": len(sources), "totals": totals,
          "parseErrors": parse_errors, "conflictingIds": conflicts,
          "exactDuplicateIds": exact_duplicates, "auxiliaryIndexedSources": sorted(set(unstructured + partial_sources)),
          "auxiliaryRecords": len(auxiliary), "partialSources": sorted(partial_sources),
          "status": "FULL_INTEGRATION_INCOMPLETE" if parse_errors or conflicts or unstructured or partial_sources or auxiliary else "CENTRAL_SYNC_PASS",
          "unintegratedSources": [{"path": p, "reason": "AUXILIARY_OR_PARTIAL_RECORDS"} for p in sorted(set(unstructured + partial_sources))],
          "policy": "Every ID retained; contradictory versions are explicit alternatives, not silently overwritten. Unstructured source files remain in source tree."}
(OUT / "report.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
print(json.dumps({"status": report["status"], "files": len(sources), "totals": totals,
                  "conflicts": len(conflicts), "parseErrors": len(parse_errors),
                  "auxiliaryIndexedSources": len(unstructured)}, ensure_ascii=False))
if parse_errors or conflicts or unstructured or partial_sources or auxiliary:
    sys.exit(1)
