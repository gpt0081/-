#!/usr/bin/env python3
"""Merge unambiguous, provenance-backed records into operational root registries."""
import collections, copy, datetime, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "integration" / "generated"
TODAY = datetime.date.today().isoformat()
def read_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8-sig")) if path.is_file() else default
def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def rid(row):
    return row.get("id") or row.get("eventId") or row.get("actionId") or row.get("_integration", {}).get("id")
def provenance(row):
    return row.get("_integration", {}).get("provenance", [])
def norm(value):
    return "".join(ch.lower() for ch in str(value or "") if ch.isalnum())
def names(person):
    values = [person.get("name")]
    if isinstance(person.get("aliases"), list):
        values.extend(person["aliases"])
    return {norm(v) for v in values if v}
def merge_list(left, right):
    result = list(left) if isinstance(left, list) else []
    seen = {json.dumps(v, ensure_ascii=False, sort_keys=True) for v in result}
    for value in right if isinstance(right, list) else []:
        key = json.dumps(value, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            result.append(copy.deepcopy(value)); seen.add(key)
    return result
def merge_record(target, incoming, kind, ident, conflicts):
    for key, value in incoming.items():
        if key in ("id", "_integration") or value is None:
            continue
        if key not in target or target[key] in (None, "", [], {}):
            target[key] = copy.deepcopy(value)
        elif target[key] == value:
            continue
        elif isinstance(target[key], list) and isinstance(value, list):
            target[key] = merge_list(target[key], value)
        elif isinstance(target[key], dict) and isinstance(value, dict):
            merge_record(target[key], value, kind, ident, conflicts)
        elif key in ("evidenceFile", "annalsFile", "coverageFile", "openLeadsFile") and isinstance(value, str):
            plural = key[:-4] + "Files"; vals = target.setdefault(plural, [])
            if isinstance(target.get(key), str) and target[key] not in vals: vals.append(target[key])
            if value not in vals: vals.append(value)
        else:
            item = {"kind": kind, "id": ident, "field": key, "rootValue": target[key],
                    "incomingValue": value, "incomingProvenance": provenance(incoming)}
            conflicts.append(item)
            fields = target.setdefault("_integration", {}).setdefault("fieldConflicts", [])
            if item not in fields: fields.append(item)
def attach_provenance(target, incoming):
    meta = target.setdefault("_integration", {})
    meta["id"] = target.get("id")
    meta["provenance"] = merge_list(meta.get("provenance", []), provenance(incoming))
    meta["syncDate"] = TODAY

# Event/action registry
event_file = DATA / "events.json"
event_root = read_json(event_file, {"schemaVersion": 1, "events": []})
event_rows = read_json(DATA / "integration" / "canonical" / "events.json", {"records": []}).get("records", [])
root_events = event_root.setdefault("events", [])
event_by_id, root_duplicates = {}, []
for row in root_events:
    ident = rid(row)
    if ident and ident in event_by_id: root_duplicates.append(ident)
    elif ident: event_by_id[ident] = row
event_before = len(event_by_id)
event_added = event_merged = 0
event_conflicts, event_skipped = [], []
for raw in event_rows:
    ident = rid(raw)
    if not ident:
        event_skipped.append({"reason": "MISSING_ID", "name": raw.get("name")}); continue
    incoming = copy.deepcopy(raw); incoming["id"] = ident
    incoming.setdefault("recordKind", "ACTION" if ident.startswith("ACT-") else "EVENT")
    if ident in event_by_id:
        merge_record(event_by_id[ident], incoming, "events", ident, event_conflicts)
        attach_provenance(event_by_id[ident], incoming); event_merged += 1
    else:
        meta = incoming.get("_integration", {})
        incoming["_integration"] = {"id": ident, "digest": meta.get("digest"),
                                    "provenance": meta.get("provenance", []), "syncDate": TODAY}
        root_events.append(incoming); event_by_id[ident] = incoming; event_added += 1
root_events.sort(key=lambda row: (str(row.get("date") or row.get("startDate") or row.get("dateRange") or "9999"), str(rid(row) or "")))
event_root["updatedAt"] = TODAY
write_json(event_file, event_root)

# Politician registry
person_file = DATA / "politicians.json"
person_root = read_json(person_file, {"schemaVersion": 1, "politicians": []})
people = person_root.setdefault("politicians", [])
people_by_id = {p["id"]: p for p in people if isinstance(p, dict) and p.get("id")}
canonical_people = read_json(DATA / "integration" / "canonical" / "politicians.json", {"records": []}).get("records", [])
manual = read_json(DATA / "integration" / "manual-politician-nodes.json", {"politicians": []}).get("politicians", [])
person_before = len(people_by_id)
person_added = person_merged = manual_added = 0
person_conflicts, crosswalk = [], []
def normalize_status(value):
    text = str(value or "").upper()
    for status in ("MATURE", "ANNALS_ACTIVE", "VERIFIED", "IDENTIFIED", "DISCOVERED"):
        if status in text: return status
    return "DISCOVERED"

for raw in canonical_people:
    ident = rid(raw)
    source_paths = [p.get("path") for p in provenance(raw) if p.get("path")]
    if not ident:
        crosswalk.append({"id": None, "name": raw.get("name"), "status": "MISSING_STABLE_ID"}); continue
    if ident.startswith("org-"):
        crosswalk.append({"id": ident, "name": raw.get("name"), "status": "ORGANIZATION_ROUTED", "sourcePaths": source_paths}); continue
    if ident.startswith("actor-"):
        crosswalk.append({"id": ident, "name": raw.get("name"), "status": "POLICY_ACTOR_OUTSIDE_POLITICIAN_ROOT", "sourcePaths": source_paths}); continue
    if ident in people_by_id:
        target = people_by_id[ident]
        merge_record(target, raw, "politicians", ident, person_conflicts)
        attach_provenance(target, raw)
        target["researchRefs"] = merge_list(target.get("researchRefs", []), source_paths)
        person_merged += 1
        crosswalk.append({"id": ident, "name": raw.get("name"), "status": "ALREADY_REGISTERED_MERGED_ADDITIVELY", "targetIds": [ident], "sourcePaths": source_paths})
        continue
    if not ident.startswith(("pol-", "cand-", "candidate-")) or not raw.get("name"):
        crosswalk.append({"id": ident, "name": raw.get("name"), "status": "NON_PERSON_OR_MISSING_NAME_NOT_PROMOTED", "sourcePaths": source_paths}); continue
    person = copy.deepcopy(raw); person["id"] = ident; person.pop("_integration", None)
    person["researchStatus"] = normalize_status(raw.get("researchStatus") or raw.get("status"))
    person["researchRefs"] = merge_list(person.get("researchRefs", []), source_paths)
    person["identityReviewStatus"] = "UNRESOLVED_SOURCE_REGISTRY_CANDIDATE"
    source_names = names(person)
    matches = [existing for existing in people if names(existing) & source_names]
    targets = sorted({existing["id"] for existing in matches})
    if targets:
        person["possibleSameAs"] = [{"id": target, "status": "UNRESOLVED_NOT_MERGED",
            "basis": "exact normalized name/alias overlap only; verify Hanja, lifespan and dated roles"} for target in targets]
        state = "ADDED_CANDIDATE_WITH_POSSIBLE_SAME_AS" if len(targets) == 1 else "ADDED_CANDIDATE_WITH_AMBIGUOUS_SAME_NAME"
    else:
        state = "ADDED_AS_CANDIDATE"
    if any(token in str(person.get("name", "")) for token in ("성명 미확정", "본명 미확정", "치안국장", "부산시장")):
        person["identityIncomplete"] = True; person["researchStatus"] = "DISCOVERED"
    people.append(person); people_by_id[ident] = person; person_added += 1
    crosswalk.append({"id": ident, "name": person.get("name"), "status": state, "targetIds": targets, "sourcePaths": source_paths})

for raw in manual:
    ident = raw.get("id")
    if not ident or ident in people_by_id: continue
    person = copy.deepcopy(raw); person["researchStatus"] = normalize_status(person.get("researchStatus"))
    people.append(person); people_by_id[ident] = person; manual_added += 1
    crosswalk.append({"id": ident, "name": person.get("name"), "status": "MANUAL_SOURCE_BACKED_NODE_ADDED", "sourcePaths": person.get("researchRefs", [])})

people.sort(key=lambda row: str(row.get("id", "")))
person_root["updatedAt"] = TODAY
write_json(person_file, person_root)
root_event_ids = {rid(row) for row in root_events if rid(row)}
root_person_ids = {p.get("id") for p in people if p.get("id")}
canonical_event_ids = {rid(row) for row in event_rows if rid(row)}
canonical_person_ids = {rid(row) for row in canonical_people if rid(row) and not rid(row).startswith(("actor-", "org-"))}
missing_events = sorted(canonical_event_ids - root_event_ids)
missing_people = sorted(canonical_person_ids - root_person_ids)
source_report = read_json(OUT / "report.json", {})
status = "PASS" if not (event_conflicts or person_conflicts or missing_events or missing_people or root_duplicates) else "PARTIAL"
write_json(OUT / "root-sync-report.json", {
    "schemaVersion": 1, "generatedAt": TODAY, "centralSync": status,
    "eventSync": {"rootBefore": event_before, "canonicalMaterialized": len(canonical_event_ids), "added": event_added,
        "merged": event_merged, "rootAfter": len(root_events), "missingCanonicalIdsAfterSync": missing_events,
        "duplicateRootIds": sorted(set(root_duplicates)), "fieldConflicts": event_conflicts, "skipped": event_skipped},
    "politicianSync": {"rootBefore": person_before, "canonicalMaterialized": len(canonical_person_ids),
        "added": person_added, "manualAdded": manual_added, "merged": person_merged, "rootAfter": len(people),
        "missingCanonicalIdsAfterSync": missing_people, "fieldConflicts": person_conflicts},
    "sourceIntegrationStatus": source_report.get("status"), "sourceConflictedIds": len(source_report.get("conflictingIds", [])),
    "sourceAuxiliaryRecords": source_report.get("auxiliaryRecords", 0),
    "policy": "Only unambiguous source variants are synchronized. Scalar conflicts are preserved; arrays merge additively; possible same-person candidates are not merged."
})
write_json(OUT / "politician-root-crosswalk.json", {"schemaVersion": 1, "generatedAt": TODAY,
    "policy": "Possible-same-as links are hypotheses, not identity merges.",
    "entries": sorted(crosswalk, key=lambda row: str(row.get("id") or ""))})
print(json.dumps({"centralSync": status, "eventsAdded": event_added, "eventsMerged": event_merged,
    "rootEvents": len(root_events), "politiciansAdded": person_added, "politiciansMerged": person_merged,
    "manualPoliticiansAdded": manual_added, "rootPoliticians": len(people),
    "missingEvents": len(missing_events), "missingPoliticians": len(missing_people),
    "eventFieldConflicts": len(event_conflicts), "politicianFieldConflicts": len(person_conflicts)}, ensure_ascii=False))
