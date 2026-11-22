#!/usr/bin/env python3
"""Merge unambiguous, provenance-backed records into operational root registries."""
import collections, copy, datetime, hashlib, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = DATA / "integration" / "generated"
TODAY = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).date().isoformat()
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
def _name_values(person):
    values = []
    for key in ("name", "name_ko", "nameKo", "displayName", "display_name",
                "english", "name_en", "nameEn", "romanization", "romanized", "hanja"):
        value = person.get(key)
        if isinstance(value, dict):
            values.extend(v for v in value.values() if isinstance(v, str) and v.strip())
        elif isinstance(value, str) and value.strip():
            values.append(value)
    aliases = person.get("aliases", [])
    if isinstance(aliases, list):
        values.extend(v for v in aliases if isinstance(v, str) and v.strip())
    elif isinstance(aliases, str) and aliases.strip():
        values.append(aliases)
    return values

def names(person):
    return {norm(value) for value in _name_values(person) if norm(value)}

def display_name(person):
    candidates = []
    for key in ("name_ko", "nameKo", "displayName", "display_name", "name", "english", "name_en"):
        value = person.get(key)
        if isinstance(value, dict):
            for subkey in ("ko", "name_ko", "nameKo", "en", "english", "name_en"):
                item = value.get(subkey)
                if isinstance(item, str) and item.strip():
                    candidates.append(item.strip())
        elif isinstance(value, str) and value.strip():
            candidates.append(value.strip())
    if not candidates:
        return None
    candidates.sort(key=lambda value: (
        0 if re.search(r"[가-힣]", value) else 1,
        -len(value), value.lower()
    ))
    return candidates[0]

def is_foreign_person(person):
    values = []
    for key in ("type", "personType", "person_type", "actorType", "actor_type",
                "category", "scope", "nationality", "citizenship",
                "nationalityCode", "citizenshipCountry"):
        value = person.get(key)
        if isinstance(value, list):
            values.extend(str(item) for item in value)
        elif isinstance(value, dict):
            values.extend(str(item) for item in value.values())
        elif value:
            values.append(str(value))
    for key in ("roles", "actionTypes", "action_types", "affiliations", "organizations"):
        value = person.get(key)
        if isinstance(value, list):
            values.extend(str(item) for item in value)
        elif value:
            values.append(str(value))
    text = " ".join(values).lower()
    if re.search(r"foreign[-_ ](official|diplomat|military|actor|person|head|counterpart)", text):
        return True
    if re.search(r"external[-_ ](actor|official|person)", text):
        return True
    markers = (
        "u.s. army", "united states army", "u.s. navy", "united states navy",
        "usn", "u.s. department of state", "department of state", "state department",
        "united nations command", "cincunc", "unc representative",
        "u.s. ambassador to korea", "united states ambassador to korea",
        "미국 대통령", "주한 미국대사", "미국대사관", "미국 국무부",
        "미 국무부", "미8군", "미군", "special representative for korean economic affairs",
        "office of northeast asian affairs"
    )
    if any(marker in text for marker in markers):
        return True
    nationality = " ".join(str(person.get(key, "")) for key in ("nationality", "citizenship", "nationalityCode", "citizenshipCountry")).lower()
    if nationality and not any(token in nationality for token in ("korean", "korea", "대한민국", "한국")):
        return True
    return False

def is_collective_label(person):
    name = display_name(person)
    if not name:
        return True
    value = norm(name)
    tokens = (
        "성명미확정", "본명미확정", "성명미상", "본명미상", "미확인", "미상", "불명",
        "네트워크", "그룹", "집단", "명단", "후보군", "관계자", "담당자", "기초관료",
        "unknown", "unnamed", "unidentified", "collective", "network", "roster", "slot"
    )
    return any(norm(token) in value for token in tokens)

def is_root_politician(person):
    ident = rid(person) or ""
    allowed = bool(re.match(r"^(?:pol-|cand-|candidate-|cand[0-9]+[a-z]? -)".replace(" ", ""), ident))
    return bool(allowed and display_name(person) and not is_foreign_person(person) and not is_collective_label(person))

def policy_exclusion(person):
    ident = rid(person) or ""
    if ident.startswith("org-"): return "ORGANIZATION_NODE"
    if ident.startswith("actor-"): return "NON_POLITICIAN_POLICY_ACTOR"
    if ident.startswith(("foreign-", "ext-")) or is_foreign_person(person): return "EXTERNAL_PERSON_OUTSIDE_DOMESTIC_ROOT"
    if ident.startswith("class-") or is_collective_label(person): return "COLLECTIVE_OR_UNRESOLVED_LABEL_NOT_PERSON"
    if ident.startswith("slot-"): return "UNRESOLVED_NAME_SLOT"
    if ident.startswith("president-"): return "LEGACY_PRESIDENT_ID_REQUIRES_CROSSWALK"
    if not display_name(person): return "MISSING_PERSON_NAME_NOT_PROMOTED"
    if not re.match(r"^(?:pol-|cand-|candidate-|cand[0-9]+[a-z]? -)".replace(" ", ""), ident):
        return "NON_DOMESTIC_OR_UNSUPPORTED_ID_PREFIX"
    return "NOT_ELIGIBLE_FOR_DOMESTIC_POLITICIAN_ROOT"
def merge_list(left, right):
    result = list(left) if isinstance(left, list) else []
    seen = {json.dumps(v, ensure_ascii=False, sort_keys=True) for v in result}
    for value in right if isinstance(right, list) else []:
        key = json.dumps(value, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            result.append(copy.deepcopy(value)); seen.add(key)
    return result
reconciled_field_variants = []

def normalize_research_status(value):
    text = str(value or "").upper()
    for status in ("MATURE", "ANNALS_ACTIVE", "VERIFIED", "IDENTIFIED", "DISCOVERED"):
        if status in text:
            return status
    return "DISCOVERED"

def is_unverified_note(value):
    text = str(value or "").lower()
    return any(token in text for token in (
        "미확인", "not verified", "not checked", "not found",
        "unverified", "no original", "open"
    ))

def same_party_note(left, right):
    a, b = str(left or ""), str(right or "")
    if "미확인" in a and "미확인" in b:
        return True
    if "자유당" in a and "자유당" in b:
        return any(token in a for token in ("보도", "신문")) and any(token in b for token in ("보도", "신문"))
    return False

def add_note(target, field, value, incoming):
    note = {"value": copy.deepcopy(value), "provenance": provenance(incoming), "recordedAt": TODAY}
    notes = target.setdefault(field, [])
    if note not in notes:
        notes.append(note)

def record_field_variant(target, kind, ident, key, root_value, incoming_value, incoming,
                         decision, status="RECONCILED_VARIANT"):
    item = {
        "kind": kind, "id": ident, "field": key,
        "rootValue": copy.deepcopy(root_value),
        "incomingValue": copy.deepcopy(incoming_value),
        "incomingProvenance": provenance(incoming),
        "decision": decision, "status": status, "recordedAt": TODAY
    }
    meta = target.setdefault("_integration", {})
    history = meta.setdefault("fieldVariantHistory", [])
    signature = json.dumps({k: item.get(k) for k in
        ("field", "rootValue", "incomingValue", "incomingProvenance", "decision", "status")},
        ensure_ascii=False, sort_keys=True)
    if not any(json.dumps({k: old.get(k) for k in
        ("field", "rootValue", "incomingValue", "incomingProvenance", "decision", "status")},
        ensure_ascii=False, sort_keys=True) == signature for old in history if isinstance(old, dict)):
        history.append(item)
    if status == "RECONCILED_VARIANT":
        reconciled_field_variants.append(item)
        for old in meta.get("fieldConflicts", []):
            if isinstance(old, dict) and old.get("field") == key and old.get("incomingValue") == incoming_value:
                old["resolutionStatus"] = "RECONCILED_VARIANT"
                old["resolutionDate"] = TODAY
                old["resolution"] = decision
    return item

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
        elif kind == "politicians" and key == "researchStatus" and isinstance(target[key], str) and isinstance(value, str) and normalize_research_status(target[key]) == normalize_research_status(value):
            add_note(target, "researchStatusDetails", {"rawValue": value, "standardStatus": normalize_research_status(value)}, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "NORMALIZED_TO_STANDARD_RESEARCH_STATUS")
        elif kind == "politicians" and key == "evidenceCoverage" and isinstance(target[key], list) and isinstance(value, str):
            add_note(target, "evidenceCoverageNotes", value, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "MOVED_NARRATIVE_TO_EVIDENCE_COVERAGE_NOTES")
        elif kind == "politicians" and key == "verification" and isinstance(target[key], str) and isinstance(value, str) and is_unverified_note(target[key]) and is_unverified_note(value):
            add_note(target, "verificationNotes", value, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "PRESERVED_EQUIVALENT_UNVERIFIED_NOTE")
        elif kind == "politicians" and key == "partyAffiliation" and isinstance(target[key], str) and isinstance(value, str) and same_party_note(target[key], value):
            add_note(target, "partyAffiliationNotes", value, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "PRESERVED_EQUIVALENT_PARTY_AFFILIATION_NOTE")
        elif kind == "politicians" and key in ("identityCaution", "promotionReason") and isinstance(target[key], str) and isinstance(value, str):
            add_note(target, key + "History", value, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "PRESERVED_ADDITIVE_CAUTION_OR_REASON")
        elif kind == "events" and key == "name" and isinstance(target[key], str) and isinstance(value, str):
            add_note(target, "nameVariants", value, incoming)
            record_field_variant(target, kind, ident, key, target[key], value, incoming, "PRESERVED_EVENT_NAME_VARIANT")
        elif kind == "events" and key == "uncertainty" and isinstance(target[key], str) and isinstance(value, str):
            root_text, incoming_text = target[key].strip(), value.strip()
            if root_text and incoming_text and (root_text in incoming_text or incoming_text in root_text):
                add_note(target, "uncertaintyHistory", value, incoming)
                if len(incoming_text) > len(root_text):
                    target[key] = value
                record_field_variant(target, kind, ident, key, root_text, incoming_text, incoming, "MERGED_CONTAINMENT_UNCERTAINTY_NOTE")
            else:
                item = record_field_variant(target, kind, ident, key, target[key], value, incoming,
                                            "UNRESOLVED_UNCERTAINTY_VARIANT", "UNRESOLVED_CONFLICT")
                conflicts.append(item)
                fields = target.setdefault("_integration", {}).setdefault("fieldConflicts", [])
                if item not in fields: fields.append(item)
        else:
            item = record_field_variant(target, kind, ident, key, target[key], value, incoming,
                                        "UNRESOLVED_SCALAR_CONFLICT", "UNRESOLVED_CONFLICT")
            conflicts.append(item)
            fields = target.setdefault("_integration", {}).setdefault("fieldConflicts", [])
            if item not in fields: fields.append(item)

def attach_provenance(target, incoming):
    meta = target.setdefault("_integration", {})
    incoming_meta = incoming.get("_integration", {}) if isinstance(incoming, dict) else {}
    meta["id"] = target.get("id")
    meta["provenance"] = merge_list(meta.get("provenance", []), provenance(incoming))
    meta["fieldVariantHistory"] = merge_list(meta.get("fieldVariantHistory", []), incoming_meta.get("fieldVariantHistory", []))
    meta["mergePolicyHistory"] = merge_list(meta.get("mergePolicyHistory", []),
                                            [incoming_meta.get("mergePolicy")] if incoming_meta.get("mergePolicy") else [])
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
                                    "provenance": meta.get("provenance", []), "syncDate": TODAY,
                                    "mergePolicy": meta.get("mergePolicy"),
                                    "fieldVariantHistory": meta.get("fieldVariantHistory", []),
                                    "sourceVariantCount": meta.get("sourceVariantCount", 1),
                                    "identityBasis": meta.get("identityBasis")}
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
    if is_foreign_person(raw):
        crosswalk.append({"id": ident, "name": display_name(raw),
            "status": "EXTERNAL_PERSON_OUTSIDE_DOMESTIC_POLITICIAN_ROOT",
            "policyReason": policy_exclusion(raw), "sourcePaths": source_paths})
        continue
    if is_collective_label(raw):
        crosswalk.append({"id": ident, "name": display_name(raw),
            "status": "COLLECTIVE_OR_UNRESOLVED_LABEL_NOT_PROMOTED",
            "policyReason": policy_exclusion(raw), "sourcePaths": source_paths})
        continue
    if ident in people_by_id:
        target = people_by_id[ident]
        merge_record(target, raw, "politicians", ident, person_conflicts)
        attach_provenance(target, raw)
        target["researchRefs"] = merge_list(target.get("researchRefs", []), source_paths)
        person_merged += 1
        crosswalk.append({"id": ident, "name": raw.get("name"), "status": "ALREADY_REGISTERED_MERGED_ADDITIVELY", "targetIds": [ident], "sourcePaths": source_paths})
        continue
    if not is_root_politician(raw):
        crosswalk.append({"id": ident, "name": display_name(raw), "status": "NON_PERSON_OR_MISSING_NAME_NOT_PROMOTED",
                          "policyReason": policy_exclusion(raw), "sourcePaths": source_paths}); continue
    person = copy.deepcopy(raw)
    person["id"] = ident
    person["name"] = display_name(raw)
    integration_meta = copy.deepcopy(raw.get("_integration", {}))
    person["_integration"] = {
        "id": ident, "digest": integration_meta.get("digest"),
        "provenance": integration_meta.get("provenance", []),
        "mergePolicy": integration_meta.get("mergePolicy"),
        "fieldVariantHistory": integration_meta.get("fieldVariantHistory", []),
        "sourceVariantCount": integration_meta.get("sourceVariantCount", 1),
        "identityBasis": integration_meta.get("identityBasis"), "syncDate": TODAY
    }
    person["researchStatus"] = normalize_status(raw.get("researchStatus") or raw.get("status"))
    person["researchRefs"] = merge_list(person.get("researchRefs", []), source_paths)
    person["identityReviewStatus"] = ("SAFE_FIELDWISE_MERGED_SOURCE_CANDIDATE"
        if integration_meta.get("mergePolicy") else "UNRESOLVED_SOURCE_REGISTRY_CANDIDATE")
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

branch_snapshot_path = DATA / "research" / "branch-snapshots" / "pr74-data-politicians.json"
branch_snapshot = read_json(branch_snapshot_path, {})
branch_snapshot_meta = branch_snapshot.get("snapshotMetadata", {}) if isinstance(branch_snapshot, dict) else {}
branch_snapshot_people = branch_snapshot.get("politicians", []) if isinstance(branch_snapshot, dict) else []
branch_snapshot_added, branch_snapshot_variant_refs, branch_snapshot_skipped = [], [], []
for index, raw in enumerate(branch_snapshot_people):
    if not isinstance(raw, dict):
        branch_snapshot_skipped.append({"pointer": f"/politicians/{index}", "reason": "NON_OBJECT_RECORD"})
        continue
    ident = rid(raw)
    if not ident or not ident.startswith(("pol-", "cand-", "candidate-", "cand172-")) or not display_name(raw):
        branch_snapshot_skipped.append({"id": ident, "pointer": f"/politicians/{index}", "reason": "POLICY_EXCLUDED_OR_MISSING_NAME"})
        continue
    ref = {
        "sourcePath": branch_snapshot_path.relative_to(ROOT).as_posix(),
        "sourcePointer": f"/politicians/{index}",
        "sourceBranch": branch_snapshot_meta.get("sourceBranch"),
        "sourceCommit": branch_snapshot_meta.get("sourceCommit"),
        "sourceBlobSha": branch_snapshot_meta.get("sourceBlobSha"),
        "recordedAt": TODAY
    }
    if ident in people_by_id:
        target = people_by_id[ident]
        refs = target.setdefault("_integration", {}).setdefault("branchSnapshotVariantRefs", [])
        if ref not in refs:
            refs.append(ref)
        branch_snapshot_variant_refs.append(ident)
        continue
    person = copy.deepcopy(raw)
    import_status = "IMPORTED_PENDING_ADJUDICATION"
    if ident.startswith("cand172-"):
        unresolved = {}
        for field in ("evidenceDocumentIds", "eventIds"):
            value = person.pop(field, None)
            if isinstance(value, list) and value:
                unresolved[field] = value
        role_document_refs = {}
        roles = person.get("roles", [])
        for role_index, role in enumerate(roles if isinstance(roles, list) else []):
            if not isinstance(role, dict):
                continue
            role_refs = role.pop("evidenceDocumentIds", None)
            if isinstance(role_refs, list) and role_refs:
                role_document_refs[str(role_index)] = role_refs
            role["verificationStatus"] = "UNVERIFIED_PENDING_PRIMARY_SOURCE"
        if role_document_refs:
            unresolved["roleEvidenceDocumentIds"] = role_document_refs
        missing_file_refs = {}
        for field in ("evidenceFile", "annalsFile", "coverageFile", "openLeadsFile"):
            value = person.get(field)
            if isinstance(value, str) and not (ROOT / value).is_file():
                missing_file_refs[field] = value
                person.pop(field, None)
        if missing_file_refs:
            unresolved["missingFileReferences"] = missing_file_refs
        if unresolved:
            person["unresolvedSourceLinks"] = unresolved
        person["researchStatus"] = "DISCOVERED"
        person["researchMaturity"] = "DISCOVERED"
        person["identityReviewStatus"] = "SOURCE_DOCUMENT_NOT_MATERIALIZED"
        person["sourceEvidenceState"] = "BRANCH_SNAPSHOT_ONLY"
        person["researchRefs"] = merge_list(person.get("researchRefs", []), [ref["sourcePath"]])
        notes = person.setdefault("researchNotes", [])
        if isinstance(notes, list):
            notes.append({
                "date": TODAY,
                "note": "PR #74 snapshot only. Referenced UNTS/FRUS document and event IDs are not present in current central registries; role text remains unverified and no event attribution is promoted."
            })
        import_status = "IMPORTED_AS_DISCOVERED_CANDIDATE_PENDING_SOURCE_VALIDATION"
    person.setdefault("_integration", {})["branchSnapshotImport"] = {
        **ref,
        "status": import_status,
        "identityPolicy": "NO_NAME_BASED_MERGE_OR_PROMOTION"
    }
    people.append(person)
    people_by_id[ident] = person
    branch_snapshot_added.append(ident)
    crosswalk.append({"id": ident, "name": display_name(person),
        "status": import_status,
        "sourcePaths": [ref["sourcePath"]], "sourcePointer": ref["sourcePointer"]})

people.sort(key=lambda row: str(row.get("id", "")))
person_root["updatedAt"] = TODAY
write_json(person_file, person_root)
root_event_ids = {rid(row) for row in root_events if rid(row)}
root_person_ids = {p.get("id") for p in people if p.get("id")}
canonical_event_ids = {rid(row) for row in event_rows if rid(row)}
canonical_person_ids = {rid(row) for row in canonical_people if is_root_politician(row)}
policy_excluded = [{"id": rid(row), "name": display_name(row), "reason": policy_exclusion(row),
                    "sourcePaths": [p.get("path") for p in provenance(row) if p.get("path")]}
                   for row in canonical_people if rid(row) and not is_root_politician(row)]
missing_events = sorted(canonical_event_ids - root_event_ids)
missing_people = sorted(canonical_person_ids - root_person_ids)
source_report = read_json(OUT / "report.json", {})
root_file_hashes = {
    "data/events.json": hashlib.sha256(event_file.read_bytes()).hexdigest(),
    "data/politicians.json": hashlib.sha256(person_file.read_bytes()).hexdigest(),
}
branch_snapshot_ids = {rid(row) for row in branch_snapshot_people if isinstance(row, dict) and rid(row)}
branch_snapshot_missing = sorted(branch_snapshot_ids - root_person_ids)
branch_snapshot_unresolved = sorted(
    p["id"] for p in people
    if p.get("_integration", {}).get("branchSnapshotImport", {}).get("status")
    == "IMPORTED_AS_DISCOVERED_CANDIDATE_PENDING_SOURCE_VALIDATION"
)
status = "PASS" if not (event_conflicts or person_conflicts or missing_events or missing_people or root_duplicates or branch_snapshot_missing or branch_snapshot_skipped or branch_snapshot_unresolved) else "PARTIAL"
write_json(OUT / "root-sync-report.json", {
    "schemaVersion": 1, "generatedAt": TODAY, "centralSync": status,
    "eventSync": {"rootBefore": event_before, "canonicalMaterialized": len(canonical_event_ids), "added": event_added,
        "merged": event_merged, "rootAfter": len(root_events), "missingCanonicalIdsAfterSync": missing_events,
        "duplicateRootIds": sorted(set(root_duplicates)), "fieldConflicts": event_conflicts,
        "fieldVariantsReconciled": [x for x in reconciled_field_variants if x["kind"] == "events"], "skipped": event_skipped},
    "politicianSync": {"rootBefore": person_before, "canonicalMaterialized": len(canonical_person_ids),
        "added": person_added, "manualAdded": manual_added, "merged": person_merged, "rootAfter": len(people),
        "missingCanonicalIdsAfterSync": missing_people, "fieldConflicts": person_conflicts,
        "fieldVariantsReconciled": [x for x in reconciled_field_variants if x["kind"] == "politicians"],
        "policyExcludedCanonicalIds": policy_excluded, "policyExcludedCount": len(policy_excluded)},
    "branchSnapshotSync": {"sourcePath": branch_snapshot_path.relative_to(ROOT).as_posix(),
        "sourceBranch": branch_snapshot_meta.get("sourceBranch"), "sourceCommit": branch_snapshot_meta.get("sourceCommit"),
        "sourceBlobSha": branch_snapshot_meta.get("sourceBlobSha"), "branchRecordCount": len(branch_snapshot_people),
        "addedToRoot": len(branch_snapshot_added), "addedIds": sorted(branch_snapshot_added),
        "variantRefsAdded": len(branch_snapshot_variant_refs), "variantRefIds": sorted(set(branch_snapshot_variant_refs)),
        "skipped": branch_snapshot_skipped, "missingAfterSync": branch_snapshot_missing,
        "unresolvedSourceLinkIds": branch_snapshot_unresolved,
        "unresolvedSourceLinkCount": len(branch_snapshot_unresolved),
        "status": "PASS" if not branch_snapshot_missing and not branch_snapshot_skipped and not branch_snapshot_unresolved else "PARTIAL"},
    "rootFileHashes": root_file_hashes,
    "rootFileCounts": {"events": len(root_events), "politicians": len(people)},
    "sourceIntegrationStatus": source_report.get("status"), "sourceConflictedIds": len(source_report.get("conflictingIds", [])),
    "sourceAuxiliaryRecords": source_report.get("auxiliaryRecords", 0),
    "policy": "Only named domestic person nodes enter the operational politician root. Foreign officials and collective/unresolved labels remain outside the domestic root. Stable candidate prefixes pol-, cand-, candidate- and candNNN- are supported. Safe field-wise merges retain source alternatives and field-variant history; no name-only identity merge. The six cand172- legacy snapshot IDs remain DISCOVERED pending source validation."
})
write_json(OUT / "politician-root-crosswalk.json", {"schemaVersion": 1, "generatedAt": TODAY,
    "policy": "Possible-same-as links are hypotheses, not identity merges.",
    "entries": sorted(crosswalk, key=lambda row: str(row.get("id") or ""))})
print(json.dumps({"centralSync": status, "eventsAdded": event_added, "eventsMerged": event_merged,
    "rootEvents": len(root_events), "politiciansAdded": person_added, "politiciansMerged": person_merged,
    "manualPoliticiansAdded": manual_added, "rootPoliticians": len(people),
    "missingEvents": len(missing_events), "missingPoliticians": len(missing_people),
    "eventFieldConflicts": len(event_conflicts), "politicianFieldConflicts": len(person_conflicts),
    "fieldVariantsReconciled": len(reconciled_field_variants), "branchSnapshotAdded": len(branch_snapshot_added),
    "branchSnapshotMissing": len(branch_snapshot_missing)}, ensure_ascii=False))
