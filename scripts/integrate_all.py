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
sources, parse_errors, unstructured, auxiliary = [], [], [], []
id_fields = ("id", "documentId", "claimId", "eventId", "politicianId", "organizationId")
for path in sorted(DATA.rglob("*")):
    if not path.is_file() or path.is_relative_to(DATA / "integration"):
        continue
    rel = path.relative_to(ROOT).as_posix()
    raw = path.read_bytes()
    source = {"path": rel, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
              "status": "INVENTORIED", "recordCounts": {k: 0 for k in KINDS}}
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
    found = 0
    for typ in KINDS:
        items = (obj.get(typ, obj.get("actors") if typ == "politicians" and kind == "politicians" else None)) if isinstance(obj, dict) else (
            obj if isinstance(obj, list) and kind == typ else None)
        if not isinstance(items, list):
            continue
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                continue
            ident = next((item[key] for key in id_fields
                          if isinstance(item.get(key), str) and item[key]), None)
            if not ident:
                ident = "urn:source:" + hashlib.sha256((rel + ":" + typ + ":" + str(idx)).encode()).hexdigest()[:24]
            payload = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            records[typ][ident].append({
                "data": item, "digest": hashlib.sha256(payload.encode()).hexdigest(),
                "source": {"path": rel, "pointer": "/" + typ + "/" + str(idx)}})
            source["recordCounts"][typ] += 1
            found += 1
    if found == 0 and kind in KINDS and isinstance(obj, dict) and isinstance(obj.get("id"), str):
        typ = kind
        item = obj
        payload = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        records[typ][item["id"]].append({
            "data": item, "digest": hashlib.sha256(payload.encode()).hexdigest(),
            "source": {"path": rel, "pointer": "/"}})
        source["recordCounts"][typ] += 1
        found += 1
    source["status"] = "RECORDS_INDEXED" if found else "AUXILIARY_JSON_INDEXED"
    if not found:
        unstructured.append(rel)
        auxiliary.append({"source": rel, "payload": obj, "provenance": source["sha256"]})

(OUT / "auxiliary.json").write_text(
    json.dumps({"schemaVersion": 2, "records": auxiliary}, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
conflicts, exact_duplicates, totals = [], [], {}
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
    canonical_rows = [dict(row["alternatives"][0]["data"],
                           _integration={"id": row["id"],
                                         "digest": row["canonicalSelection"],
                                         "provenance": row["alternatives"][0]["provenance"]})
                      for row in central if row["integrationStatus"] == "INTEGRATED"]
    (CANONICAL / (typ + ".json")).write_text(
        json.dumps({"schemaVersion": 1, "registryType": typ,
                    "selectionPolicy": "UNAMBIGUOUS_ONLY",
                    "records": canonical_rows}, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
    (OUT / (typ + ".json")).write_text(
        json.dumps({"schemaVersion": 2, "registryType": typ, "records": central},
                   ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
(OUT / "sources.json").write_text(
    json.dumps({"schemaVersion": 2, "sources": sources}, ensure_ascii=False, indent=2) + chr(10),
    encoding="utf-8")
report = {"canonicalMaterialized": {k: v["uniqueIds"] - v["conflictedIds"] for k, v in totals.items()},
          "canonicalDirectory": "data/integration/canonical",
          "sourceFiles": len(sources), "totals": totals,
          "parseErrors": parse_errors, "conflictingIds": conflicts,
          "exactDuplicateIds": exact_duplicates, "auxiliaryIndexedSources": unstructured,
          "status": "FULL_INTEGRATION_INCOMPLETE" if parse_errors or conflicts or unstructured else "CENTRAL_SYNC_PASS",
          "unintegratedSources": [{"path": p, "reason": "AUXILIARY_ONLY_NOT_CANONICAL"} for p in unstructured],
          "policy": "Every ID retained; contradictory versions are explicit alternatives, not silently overwritten. Unstructured source files remain in source tree."}
(OUT / "report.json").write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + chr(10), encoding="utf-8")
print(json.dumps({"status": report["status"], "files": len(sources), "totals": totals,
                  "conflicts": len(conflicts), "parseErrors": len(parse_errors),
                  "auxiliaryIndexedSources": len(unstructured)}, ensure_ascii=False))
if parse_errors or conflicts or unstructured:
    sys.exit(1)
