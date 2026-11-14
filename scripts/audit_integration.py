#!/usr/bin/env python3
"""Validate the lossless consolidated registries without claiming historical truth."""
import json, pathlib, collections, hashlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
out=root/"data/integration/generated"
kinds=("documents","claims","events","politicians","organizations")
report=json.loads((out/"report.json").read_text())
sources=json.loads((out/"sources.json").read_text())["sources"]
issues=[]
paths=[s["path"] for s in sources]
if len(paths)!=len(set(paths)):issues.append({"code":"DUPLICATE_SOURCE_PATH"})
if report["sourceFiles"]!=len(sources):issues.append({"code":"SOURCE_COUNT_MISMATCH"})
# Verify every inventoried byte stream against the actual repository checkout.
# A recorded path alone is not evidence that its original contents survived.
for src in sources:
    original=root/src["path"]
    if not original.is_file():
        issues.append({"code":"MISSING_ORIGINAL_FILE","path":src["path"]})
        continue
    digest=hashlib.sha256(original.read_bytes()).hexdigest()
    if digest!=src["sha256"]:
        issues.append({"code":"SOURCE_HASH_MISMATCH","path":src["path"]})
# Confirm all currently present source files are represented in the inventory.
actual={p.relative_to(root).as_posix() for p in (root/"data").rglob("*")
        if p.is_file() and not p.is_relative_to(out.parent)}
for missing in sorted(actual-set(paths)):
    issues.append({"code":"UNINVENTORIED_SOURCE_FILE","path":missing})

ids={}
for kind in kinds:
    obj=json.loads((out/(kind+".json")).read_text())
    rows=obj["records"]
    ids[kind]={r["id"] for r in rows}
    if len(ids[kind])!=len(rows):issues.append({"code":"DUPLICATE_CENTRAL_ID","kind":kind})
    if len(rows)!=report["totals"][kind]["uniqueIds"]:issues.append({"code":"REGISTRY_COUNT_MISMATCH","kind":kind})
    for r in rows:
        if r["integrationStatus"]=="CONFLICTED" and r.get("canonicalSelection") is not None:
            issues.append({"code":"UNSAFE_CONFLICT_SELECTION","kind":kind,"id":r["id"]})
        if not r.get("alternatives"):issues.append({"code":"NO_ALTERNATIVES","kind":kind,"id":r["id"]})
        for alt in r["alternatives"]:
            if not alt.get("provenance"):issues.append({"code":"MISSING_PROVENANCE","kind":kind,"id":r["id"]})
            for p in alt.get("provenance",[]):
                if p["path"] not in paths:issues.append({"code":"UNKNOWN_SOURCE","kind":kind,"id":r["id"],"path":p["path"]})
aux=json.loads((out/"auxiliary.json").read_text())["records"]
aux_paths={a["source"] for a in aux}
missing_aux=[s["path"] for s in sources if s["status"]=="AUXILIARY_JSON_INDEXED" and s["path"] not in aux_paths]
for p in missing_aux:issues.append({"code":"AUXILIARY_SOURCE_MISSING","path":p})
# Verify the operational crosswalk is explicit, source-backed and unambiguous.
link_file=out/"operational-links.json"
if not link_file.is_file():
    issues.append({"code":"OPERATIONAL_LINKS_MISSING"})
else:
    links=json.loads(link_file.read_text())
    seen=set()
    for row in links.get("linked",[])+links.get("unlinked",[]):
        path=row["source"]
        if path in seen:issues.append({"code":"DUPLICATE_OPERATIONAL_SOURCE","path":path})
        seen.add(path)
        if path not in paths:issues.append({"code":"UNKNOWN_OPERATIONAL_SOURCE","path":path})
        candidates=row.get("candidatePoliticianIds",[])
        if row["status"]=="EXPLICITLY_LINKED":
            if len(candidates)!=1:issues.append({"code":"UNSAFE_OPERATIONAL_IDENTITY","path":path})
            elif candidates[0] not in ids["politicians"]:
                issues.append({"code":"UNKNOWN_OPERATIONAL_POLITICIAN","path":path,"id":candidates[0]})
        elif row["status"] not in ("AMBIGUOUS_IDENTITY","NO_EXPLICIT_IDENTITY"):
            issues.append({"code":"UNKNOWN_LINK_STATUS","path":path})
    if sum(links.get("layerCounts",{}).values())!=len(seen):
        issues.append({"code":"OPERATIONAL_LAYER_COUNT_MISMATCH"})
# Crosswalk staging is not proof of canonical registration. Check every staged ID
# and its declared source document before reporting central synchronization.
crosswalk_gaps=[]
for crosswalk in sorted((root/"data/research/registry").glob("*index.json")):
    try:
        staged=json.loads(crosswalk.read_text(encoding="utf-8-sig"))
    except (ValueError,UnicodeError) as exc:
        crosswalk_gaps.append({"source":crosswalk.relative_to(root).as_posix(),
                               "reason":"UNREADABLE_CROSSWALK","detail":str(exc)[:160]})
        continue
    if not isinstance(staged,dict):
        continue
    for kind in ("documents","claims","events","politicians","organizations"):
        for row in staged.get(kind,[]):
            if not isinstance(row,dict) or not isinstance(row.get("id"),str):
                continue
            if row["id"] not in ids[kind]:
                crosswalk_gaps.append({"source":crosswalk.relative_to(root).as_posix(),
                                       "kind":kind,"id":row["id"],
                                       "reason":"NOT_IN_GENERATED_REGISTRY"})
# Cross-kind identity and explicit relationship integrity: audit every preserved
# alternative, not only the selected canonical variant. These are structural
# checks and do not adjudicate historical truth.
for left in kinds:
    for right in kinds:
        if left >= right:
            continue
        overlap=ids[left] & ids[right]
        for ident in sorted(overlap):
            issues.append({"code":"CROSS_KIND_ID_COLLISION","id":ident,
                           "kinds":[left,right]})
reference_fields={
    "relatedDocumentIds":"documents", "documentIds":"documents",
    "supportingDocumentIds":"documents", "contradictingDocumentIds":"documents",
    "relatedEventIds":"events", "eventIds":"events",
    "relatedClaimIds":"claims", "claimIds":"claims",
    "relatedPoliticianIds":"politicians", "politicianIds":"politicians",
    "relatedOrganizationIds":"organizations", "organizationIds":"organizations",
}
reference_issues=[]
for kind in kinds:
    registry=json.loads((out/(kind+".json")).read_text())
    for record in registry["records"]:
        for alternative in record["alternatives"]:
            payload=alternative["data"]
            for field,target in reference_fields.items():
                if field not in payload:
                    continue
                refs=payload[field]
                if not isinstance(refs,list):
                    reference_issues.append({"code":"INVALID_REFERENCE_LIST",
                        "kind":kind,"id":record["id"],"field":field})
                    continue
                for ref in refs:
                    if not isinstance(ref,str) or ref not in ids[target]:
                        reference_issues.append({"code":"DANGLING_REFERENCE",
                            "kind":kind,"id":record["id"],"field":field,
                            "targetKind":target,"targetId":ref})
issues.extend(reference_issues)
summary={"sourceFiles":len(sources),"uniqueCentralIds":{k:len(v) for k,v in ids.items()},
"conflictedIds":len(report["conflictingIds"]),"auxiliaryRecords":len(aux),
"unresolvedSources":[s["path"] for s in sources if s["status"] in ("PARSE_ERROR","AUXILIARY_JSON_INDEXED")],
"integrityIssues":issues,"referenceIssueCount":len(reference_issues),
"crosswalkGaps":crosswalk_gaps,
"centralSync":"PARTIAL" if report["conflictingIds"] or report["parseErrors"] or aux or crosswalk_gaps else "PASS",
"note":"Registry presence and provenance checks only. Referential and historical adjudication still required."}
(out/"integrity-audit.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in summary.items() if k not in ("unresolvedSources","integrityIssues")},ensure_ascii=False))
# A partial audit must never return success to CI or an hourly worker.
# The integrator intentionally preserves conflicting alternatives and auxiliary
# sources; those remain unresolved until separately adjudicated or mapped.
if summary["centralSync"] != "PASS" or issues:
    sys.exit(1)

