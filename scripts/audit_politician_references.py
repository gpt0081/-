#!/usr/bin/env python3
"""Read-only central politician registry integrity audit, including plural file references."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
registry = json.loads((DATA / "politicians.json").read_text(encoding="utf-8"))
people = registry["politicians"]
ids = [p.get("id") for p in people]
duplicates = sorted(k for k, n in Counter(ids).items() if n > 1)
missing = []
bad_json = []
evidence_refs = []
legacy_owner_refs = []
research_ref_missing = []
checked = Counter()

file_fields = {
    "evidenceFile": "evidenceFiles",
    "annalsFile": "annalsFiles",
    "openLeadsFile": "openLeadsFiles",
    "coverageFile": "coverageFiles",
}

for person in people:
    person_id = person.get("id")
    for singular, plural in file_fields.items():
        targets = []
        value = person.get(singular)
        if isinstance(value, str):
            targets.append(value)
        elif value:
            missing.append({"politicianId": person_id, "field": singular, "path": value, "reason": "invalid_singular_reference"})
        plural_values = person.get(plural, [])
        if isinstance(plural_values, list):
            targets.extend(v for v in plural_values if isinstance(v, str))
            if any(not isinstance(v, str) for v in plural_values):
                missing.append({"politicianId": person_id, "field": plural, "reason": "non_string_reference"})
        elif plural_values:
            missing.append({"politicianId": person_id, "field": plural, "reason": "invalid_plural_reference"})

        for target in sorted(set(targets)):
            checked[singular] += 1
            if not target.startswith("data/"):
                missing.append({"politicianId": person_id, "field": singular, "path": target, "reason": "invalid_path"})
                continue
            file = (ROOT / target).resolve()
            if not file.is_relative_to(DATA.resolve()) or not file.is_file():
                missing.append({"politicianId": person_id, "field": singular, "path": target, "reason": "missing"})
                continue
            if singular == "evidenceFile" and file.suffix == ".json":
                try:
                    evidence = json.loads(file.read_text(encoding="utf-8-sig"))
                    if isinstance(evidence, dict):
                        declared = evidence.get("politicianId") or evidence.get("politician_id") or evidence.get("personId")
                        declared_many = evidence.get("relatedPoliticianIds") or evidence.get("politicianIds") or []
                        if isinstance(declared_many, list) and person_id in declared_many:
                            declared = person_id
                        if declared and declared != person_id:
                            record = {"politicianId": person_id, "declaredId": declared, "path": target}
                            if declared in person.get("legacyIds", []):
                                legacy_owner_refs.append(record)
                            else:
                                evidence_refs.append(record)
                except (ValueError, UnicodeError) as exc:
                    bad_json.append({"path": target, "error": str(exc)[:180]})

    research_refs = person.get("researchRefs", [])
    if isinstance(research_refs, list):
        for target in sorted(set(v for v in research_refs if isinstance(v, str) and v.startswith("data/"))):
            checked["researchRefs"] += 1
            file = (ROOT / target).resolve()
            if not file.is_relative_to(DATA.resolve()) or not file.is_file():
                research_ref_missing.append({"politicianId": person_id, "path": target})
    elif research_refs:
        research_ref_missing.append({"politicianId": person_id, "path": research_refs, "reason": "invalid_researchRefs"})

snapshot_path = DATA / "research" / "branch-snapshots" / "pr74-data-politicians.json"
pr74_comparison = None
if snapshot_path.is_file():
    branch_registry = json.loads(snapshot_path.read_text(encoding="utf-8"))
    branch_people = branch_registry.get("politicians", [])
    branch_by_id = {p.get("id"): p for p in branch_people if isinstance(p.get("id"), str)}
    main_by_id = {p.get("id"): p for p in people if isinstance(p.get("id"), str)}
    branch_ids = set(branch_by_id)
    main_ids = set(main_by_id)
    branch_only = sorted(branch_ids - main_ids)
    main_only = sorted(main_ids - branch_ids)
    changed_records = []
    changed_fields = Counter()
    for person_id in sorted(branch_ids & main_ids):
        before = branch_by_id[person_id]
        after = main_by_id[person_id]
        fields = sorted(
            key for key in set(before) | set(after)
            if json.dumps(before.get(key), ensure_ascii=False, sort_keys=True)
            != json.dumps(after.get(key), ensure_ascii=False, sort_keys=True)
        )
        if fields:
            changed_records.append({"politicianId": person_id, "changedFields": fields})
            changed_fields.update(fields)
    snapshot_meta = branch_registry.get("snapshotMetadata", {})
    pr74_comparison = {
        "sourceBranch": snapshot_meta.get("sourceBranch"),
        "sourceCommit": snapshot_meta.get("sourceCommit"),
        "sourceBlobSha": snapshot_meta.get("sourceBlobSha"),
        "branchPoliticians": len(branch_people),
        "mainPoliticians": len(people),
        "sharedIds": len(branch_ids & main_ids),
        "branchOnlyCount": len(branch_only),
        "branchOnlyIds": branch_only,
        "mainOnlyCount": len(main_only),
        "mainOnlyIds": main_only,
        "changedRecordCount": len(changed_records),
        "changedFieldCounts": dict(sorted(changed_fields.items())),
        "sampleChangedRecords": changed_records[:40],
        "fullDiffPath": "data/integration/generated/pr74-politician-root-diff.json",
        "mergePolicy": "No branch record is copied over main automatically. Import only branch-only stable IDs after identity and provenance review; preserve shared-field differences as variants."
    }
    diff_path = DATA / "integration" / "generated" / "pr74-politician-root-diff.json"
    diff_path.parent.mkdir(parents=True, exist_ok=True)
    diff_path.write_text(json.dumps({
        "schemaVersion": 1,
        "comparison": pr74_comparison,
        "changedRecords": changed_records
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

result = {
    "schemaVersion": 2,
    "scope": "Central politician root singular/plural evidence, annals, coverage, open-lead and researchRefs paths",
    "canonicalSyncVerified": False,
    "politiciansChecked": len(people),
    "duplicatePoliticianIds": duplicates,
    "missingOrInvalidFiles": missing,
    "evidenceOwnerMismatches": evidence_refs,
    "acceptedLegacyEvidenceOwners": legacy_owner_refs,
    "invalidEvidenceJson": bad_json,
    "missingResearchRefs": research_ref_missing,
    "referenceCountsChecked": dict(sorted(checked.items())),
    "pr74BranchSnapshotComparison": pr74_comparison,
    "limitations": [
        "Does not resolve conflicting source variants",
        "PR #74 snapshot differences are audited only; no branch values are silently imported",
        "Does not validate event/document/claim graph truth",
        "Does not establish historical truth or provenance independence"
    ]
}
out = DATA / "integration" / "generated" / "politician-reference-audit.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({
    "politiciansChecked": len(people),
    "duplicatePoliticianIds": len(duplicates),
    "missingOrInvalidFiles": len(missing),
    "evidenceOwnerMismatches": len(evidence_refs),
    "acceptedLegacyEvidenceOwners": len(legacy_owner_refs),
    "invalidEvidenceJson": len(bad_json),
    "missingResearchRefs": len(research_ref_missing),
    "referenceCountsChecked": dict(sorted(checked.items())),
    "pr74BranchOnlyPoliticians": (pr74_comparison or {}).get("branchOnlyCount")
}, ensure_ascii=False))
if duplicates or missing or evidence_refs or bad_json or research_ref_missing or (pr74_comparison and pr74_comparison["branchOnlyCount"]):
    raise SystemExit(1)
