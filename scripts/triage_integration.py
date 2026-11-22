#!/usr/bin/env python3
"""Per-file source triage, grouped inventory, and central-sync index refresh."""
import collections
import datetime
import hashlib
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/integration/generated"
INV = ROOT / "data/integration/inventory"
INV.mkdir(parents=True, exist_ok=True)
report = json.loads((OUT / "report.json").read_text(encoding="utf-8"))
sources = json.loads((OUT / "sources.json").read_text(encoding="utf-8"))["sources"]
conflicts = collections.defaultdict(list)
for item in report.get("conflictingIds", []):
    for path in item.get("sources", []):
        conflicts[path].append({
            "kind": item["type"], "id": item["id"],
            "variantCount": item.get("variantCount"),
            "mergeReview": item.get("mergeReview", {})
        })
unintegrated = {row["path"]: row.get("reason") for row in report.get("unintegratedSources", [])}

def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def write_json(path, value):
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return git_blob_sha(raw)

def group_name(path):
    roots = {
        "data/events.json": "data-events.json.json",
        "data/politicians.json": "data-politicians.json.json",
        "data/presidents.json": "data-presidents.json.json",
    }
    if path in roots:
        return roots[path]
    parts = path.split("/")
    return "data-" + (parts[1] if len(parts) > 1 else "misc") + ".json"

rows = []
groups = collections.defaultdict(list)
status_counts = collections.Counter()
for src in sources:
    path = src["path"]
    problems = conflicts.get(path, [])
    source_status = src.get("status", "")
    if source_status == "OPERATIONAL_ROOT_PRESERVED":
        status = "OPERATIONAL_ROOT_PRESERVED"
    elif source_status == "PRESIDENTIAL_BACKBONE_PRESERVED":
        status = "PRESIDENTIAL_BACKBONE_PRESERVED"
    elif source_status == "NON_JSON_SOURCE_PRESERVED":
        status = "NON_JSON_SOURCE_PRESERVED"
    elif source_status == "PARSE_ERROR":
        status = "BLOCKED_PARSE"
    elif problems or source_status == "CONFLICT_REVIEW_REQUIRED":
        status = "BLOCKED_ID_CONFLICT"
    elif source_status == "PARTIAL_CANONICAL_MATERIALIZED":
        status = "PARTIAL_CANONICAL_MATERIALIZED"
    elif source_status == "CANONICAL_MATERIALIZED":
        status = "CANONICAL_MATERIALIZED"
    elif path in unintegrated or source_status == "AUXILIARY_JSON_INDEXED":
        status = "UNMAPPED_AUXILIARY_OR_PARTIAL"
    elif source_status:
        status = "PRESERVED_SPECIALIZED_LAYER"
    else:
        status = "UNCLASSIFIED_REVIEW"
    raw = (ROOT / path).read_bytes()
    row = {
        "path": path,
        "gitBlobSha": git_blob_sha(raw),
        "sha256": src.get("sha256"),
        "bytes": src.get("bytes", len(raw)),
        "recordCounts": src.get("recordCounts", {}),
        "targetLayer": src.get("targetLayer", "unknown"),
        "targetRegistries": src.get("targetRegistries", []),
        "sourceStatus": source_status,
        "status": status,
        "conflicts": sorted(problems, key=lambda x: (x["kind"], x["id"])),
        "unintegratedReason": unintegrated.get(path),
    }
    rows.append(row)
    groups[group_name(path)].append(row)
    status_counts[status] += 1

assert len(rows) == report["sourceFiles"]
assert len({row["path"] for row in rows}) == len(rows)
assert sum(len(group) for group in groups.values()) == len(rows)

root_sync = json.loads((OUT / "root-sync-report.json").read_text(encoding="utf-8"))
integrity = json.loads((OUT / "integrity-audit.json").read_text(encoding="utf-8"))
politician_audit_path = OUT / "politician-reference-audit.json"
politician_audit = json.loads(politician_audit_path.read_text(encoding="utf-8")) if politician_audit_path.exists() else {}
root_status = root_sync.get("centralSync", "BLOCKED")
reference_issues = integrity.get("referenceIssueCount", len(integrity.get("integrityIssues", [])))
structural_issues = len(integrity.get("integrityIssues", integrity.get("issues", [])))
if root_status == "PASS" and structural_issues == 0 and reference_issues == 0 and politician_audit.get("canonicalSyncVerified"):
    central_status = "CENTRAL_SYNC_PASS"
elif root_status in ("PASS", "PARTIAL"):
    central_status = "CENTRAL_SYNC_PARTIAL"
else:
    central_status = "CENTRAL_SYNC_BLOCKED"

snapshot = os.environ.get("GITHUB_SHA") or subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
tree_sha = subprocess.check_output(
    ["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip()
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
triage_doc = {
    "schemaVersion": 2,
    "scope": "Every tracked data source file outside data/integration; exactly one row per source file",
    "updatedAt": now,
    "sourceSnapshotCommit": snapshot,
    "sourceTreeSha": tree_sha,
    "sourceFiles": len(rows),
    "statusCounts": dict(sorted(status_counts.items())),
    "centralSyncStatus": central_status,
    "canonicalSyncVerified": central_status == "CENTRAL_SYNC_PASS",
    "sources": rows,
    "nextAction": "Continue unresolved identity conflicts and auxiliary schema mapping. Preserve all source alternatives and provenance; do not infer identity from name similarity alone."
}
triage_sha = write_json(OUT / "source-triage.json", triage_doc)

inventory_groups = []
for filename, files in sorted(groups.items()):
    group_counts = collections.Counter(row["status"] for row in files)
    group_doc = {
        "schemaVersion": 2,
        "group": filename,
        "sourceSnapshotCommit": snapshot,
        "sourceTreeSha": tree_sha,
        "fileCount": len(files),
        "statusCounts": dict(sorted(group_counts.items())),
        "files": sorted(files, key=lambda row: row["path"])
    }
    group_sha = write_json(INV / filename, group_doc)
    inventory_groups.append({
        "path": f"data/integration/inventory/{filename}",
        "sha": group_sha,
        "fileCount": len(files),
        "statusCounts": dict(sorted(group_counts.items()))
    })

tracked = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
non_data = [path for path in tracked if not path.startswith("data/")]
conflict_summary = collections.Counter(item["type"] for item in report.get("conflictingIds", []))
master = {
    "schemaVersion": 3,
    "createdAt": "2026-11-22",
    "updatedAt": now,
    "sourceSnapshotCommit": snapshot,
    "sourceTreeSha": tree_sha,
    "sourceFilesTotal": len(rows) + len(non_data),
    "sourceDataFiles": len(rows),
    "nonDataFiles": len(non_data),
    "inventoryGroups": inventory_groups,
    "currentPerFileInventory": {
        "path": "data/integration/generated/source-triage.json",
        "blobSha": triage_sha,
        "sourceFiles": len(rows),
        "status": central_status
    },
    "semanticIntegrationStatus": report.get("status"),
    "centralSync": central_status,
    "canonicalMaterialized": report.get("canonicalMaterialized", {}),
    "safeMergeCount": report.get("safeMergeCount", 0),
    "conflictedIdCount": len(report.get("conflictingIds", [])),
    "conflictsByRegistry": dict(sorted(conflict_summary.items())),
    "auxiliaryRecords": report.get("auxiliaryRecords", 0),
    "unintegratedSources": len(report.get("unintegratedSources", [])),
    "partialSources": len(report.get("partialSources", [])),
    "rootSync": {
        "status": root_status,
        "eventRootAfter": root_sync.get("eventSync", {}).get("rootAfter"),
        "politicianRootAfter": root_sync.get("politicianSync", {}).get("rootAfter"),
        "missingEvents": len(root_sync.get("eventSync", {}).get("missingCanonicalIdsAfterSync", [])),
        "missingPoliticians": len(root_sync.get("politicianSync", {}).get("missingCanonicalIdsAfterSync", [])),
        "eventFieldConflicts": len(root_sync.get("eventSync", {}).get("fieldConflicts", [])),
        "politicianFieldConflicts": len(root_sync.get("politicianSync", {}).get("fieldConflicts", []))
    },
    "integrityAudit": {
        "structuralIssues": structural_issues,
        "referenceIssues": reference_issues
    },
    "politicianReferenceAudit": {
        "canonicalSyncVerified": politician_audit.get("canonicalSyncVerified"),
        "politiciansChecked": politician_audit.get("politiciansChecked"),
        "duplicateIds": len(politician_audit.get("duplicatePoliticianIds", [])),
        "missingFiles": len(politician_audit.get("missingOrInvalidFiles", [])),
        "missingResearchRefs": len(politician_audit.get("missingResearchRefs", []))
    },
    "priority": [
        "Resolve the remaining 30 identity-critical source conflicts with original document provenance; do not auto-select a variant.",
        "Map 2,232 auxiliary records across 1,604 source files into typed central registries or record precise non-registry reasons.",
        "Resolve 135 dangling cross-registry references by checking target IDs and original source pointers.",
        "Resolve operational root field variants and sidecar links after the canonical ID layer is stable.",
        "Review all 453 shared PR #74 politician records without importing branch variants by name-only matching."
    ],
    "migrationRule": "Unambiguous records and conservative field-wise merges are materialized; ambiguous scalar values remain field variants with provenance. Original source alternatives are retained.",
    "lastAudit": {
        "date": "2026-11-22",
        "sourceSnapshotCommit": snapshot,
        "sourceDataFiles": len(rows),
        "safeMergeCount": report.get("safeMergeCount", 0),
        "conflictedIds": len(report.get("conflictingIds", [])),
        "auxiliaryRecords": report.get("auxiliaryRecords", 0),
        "unintegratedSources": len(report.get("unintegratedSources", [])),
        "referenceIssueCount": reference_issues,
        "centralSync": central_status
    },
    "note": "Registry presence is not proof of historical truth. Source identity, claim truth, provenance independence and historical responsibility remain separate review questions."
}
write_json(ROOT / "data/integration/MASTER_INDEX.json", master)
assert sum(item["fileCount"] for item in inventory_groups) == len(rows)
print(json.dumps({
    "sourceFiles": len(rows),
    "statusCounts": triage_doc["statusCounts"],
    "centralSync": central_status,
    "inventoryGroups": len(inventory_groups),
    "safeMergeCount": report.get("safeMergeCount", 0)
}, ensure_ascii=False))
