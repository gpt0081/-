#!/usr/bin/env python3
"""Per-source integration triage. This does NOT claim canonical synchronization."""
import collections
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/integration/generated"
report = json.loads((OUT / "report.json").read_text(encoding="utf-8"))
sources = json.loads((OUT / "sources.json").read_text(encoding="utf-8"))["sources"]
conflicts = collections.defaultdict(list)
for item in report["conflictingIds"]:
    for path in item["sources"]:
        conflicts[path].append({"kind": item["type"], "id": item["id"], "variantCount": item["variantCount"]})
unintegrated = {x["path"]: x["reason"] for x in report["unintegratedSources"]}
rows = []
counts = collections.Counter()
for src in sources:
    path = src["path"]
    kinds = [kind for kind, n in src["recordCounts"].items() if n]
    problems = conflicts.get(path, [])
    if src["status"] == "PARSE_ERROR":
        status = "BLOCKED_PARSE"
    elif problems:
        status = "BLOCKED_ID_CONFLICT"
    elif path in unintegrated:
        status = "UNMAPPED_AUXILIARY"
    elif kinds:
        status = "INDEXED_NOT_CANONICAL_VERIFIED"
    else:
        status = "NON_JSON_PRESERVED"
    counts[status] += 1
    rows.append({
        "path": path, "sha256": src["sha256"], "bytes": src["bytes"],
        "recordCounts": src["recordCounts"], "targetRegistries": kinds,
        "status": status, "conflicts": sorted(problems, key=lambda x: (x["kind"], x["id"])),
        "unintegratedReason": unintegrated.get(path),
    })
assert len(rows) == report["sourceFiles"]
assert len({r["path"] for r in rows}) == len(rows)
result = {
    "schemaVersion": 1,
    "scope": "Every inventoried source file; structural triage only",
    "canonicalSyncVerified": False,
    "sourceFiles": len(rows),
    "statusCounts": dict(sorted(counts.items())),
    "sources": rows,
    "nextAction": "Resolve conflicts and map auxiliary payloads; then verify canonical registries, operational layers and references.",
}
(OUT / "source-triage.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"sourceFiles": len(rows), "statusCounts": result["statusCounts"]}, ensure_ascii=False))
