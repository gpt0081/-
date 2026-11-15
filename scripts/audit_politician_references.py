#!/usr/bin/env python3
"""Read-only central politician registry integrity audit. Never changes source data."""
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
for p in people:
    for field in ("evidenceFile", "annalsFile", "openLeadsFile", "coverageFile"):
        target = p.get(field)
        if not target:
            continue
        if not isinstance(target, str) or not target.startswith("data/"):
            missing.append({"politicianId": p.get("id"), "field": field, "path": target, "reason": "invalid_path"})
            continue
        file = (ROOT / target).resolve()
        if not file.is_relative_to(DATA.resolve()) or not file.is_file():
            missing.append({"politicianId": p.get("id"), "field": field, "path": target, "reason": "missing"})
            continue
        if field == "evidenceFile" and file.suffix == ".json":
            try:
                evidence = json.loads(file.read_text(encoding="utf-8"))
                declared = evidence.get("politicianId") if isinstance(evidence, dict) else None
                if declared and declared != p.get("id"):
                    evidence_refs.append({"politicianId": p.get("id"), "declaredId": declared, "path": target})
            except (ValueError, UnicodeError) as exc:
                bad_json.append({"path": target, "error": str(exc)[:180]})
result = {
    "schemaVersion": 1,
    "scope": "canonical data/politicians.json file references only",
    "canonicalSyncVerified": False,
    "politiciansChecked": len(people),
    "duplicatePoliticianIds": duplicates,
    "missingOrInvalidFiles": missing,
    "evidenceOwnerMismatches": evidence_refs,
    "invalidEvidenceJson": bad_json,
    "limitations": [
        "Does not resolve conflicting source variants",
        "Does not validate event/document/claim cross-registry references",
        "Does not establish historical truth or provenance independence"
    ]
}
out = DATA / "integration" / "generated" / "politician-reference-audit.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: len(v) if isinstance(v, list) else v for k, v in result.items() if k not in ("limitations",)}, ensure_ascii=False))
if duplicates or missing or evidence_refs or bad_json:
    raise SystemExit(1)
