#!/usr/bin/env python3
"""Validate the lossless consolidated registries without claiming historical truth."""
import json, pathlib, collections, hashlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
out=root/"data/integration/generated"
kinds=("documents","claims","events","politicians","organizations","roles")
report=json.loads((out/"report.json").read_text())
sources=json.loads((out/"sources.json").read_text())["sources"]
issues=[]
paths=[s["path"] for s in sources]
if len(paths)!=len(set(paths)):issues.append({"code":"DUPLICATE_SOURCE_PATH"})
if report["sourceFiles"]!=len(sources):issues.append({"code":"SOURCE_COUNT_MISMATCH"})
# Verify every inventoried byte stream against the actual repository checkout.
# A recorded path alone is not evidence that its original contents survived.
root_managed_paths = {"data/events.json", "data/politicians.json"}
for src in sources:
    original=root/src["path"]
    if not original.is_file():
        issues.append({"code":"MISSING_ORIGINAL_FILE","path":src["path"]})
        continue
    # The source inventory records the pre-reconciliation root snapshot.
    # The reconciler writes these two operational roots later in the same workflow.
    if src["path"] in root_managed_paths:
        continue
    digest=hashlib.sha256(original.read_bytes()).hexdigest()
    if digest!=src["sha256"]:
        issues.append({"code":"SOURCE_HASH_MISMATCH","path":src["path"]})

root_sync_path=out/"root-sync-report.json"
root_sync={}
if root_sync_path.is_file():
    root_sync=json.loads(root_sync_path.read_text())
    for path,digest in root_sync.get("rootFileHashes",{}).items():
        current=root/path
        if not current.is_file() or hashlib.sha256(current.read_bytes()).hexdigest()!=digest:
            issues.append({"code":"ROOT_REGISTRY_HASH_MISMATCH","path":path})
else:
    issues.append({"code":"ROOT_SYNC_REPORT_MISSING"})
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

# Operational roots contain valid legacy/base IDs that may be referenced by overlays.
reference_ids={kind:set(values) for kind,values in ids.items()}
root_events=json.loads((root/"data/events.json").read_text(encoding="utf-8-sig")).get("events",[])
root_people=json.loads((root/"data/politicians.json").read_text(encoding="utf-8-sig")).get("politicians",[])
reference_ids["events"].update(r.get("id") or r.get("eventId") or r.get("actionId") for r in root_events if isinstance(r,dict))
reference_ids["politicians"].update(r.get("id") for r in root_people if isinstance(r,dict) and r.get("id"))
reference_ids["events"].discard(None)
reference_ids["politicians"].discard(None)
# The chronological president overlay is a valid legacy person-ID namespace.
presidents = json.loads((root/"data/presidents.json").read_text(encoding="utf-8-sig"))
if isinstance(presidents, list):
    reference_ids["politicians"].update(
        row.get("id") for row in presidents
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    )
reference_ids["politicians"].discard(None)
# Validate materialized canonical registries against the lossless alternatives.
# A generated index alone cannot establish that the queryable central layer exists.
canonical_root=root/"data/integration/canonical"
for kind in kinds:
    canonical_file=canonical_root/(kind+".json")
    if not canonical_file.is_file():
        issues.append({"code":"CANONICAL_REGISTRY_MISSING","kind":kind})
        continue
    try:
        canonical=json.loads(canonical_file.read_text(encoding="utf-8"))
        rows=canonical["records"]
        if not isinstance(rows,list):
            raise ValueError("records must be a list")
        if kind == "documents":
            for row in rows:
                if isinstance(row, dict) and isinstance(row.get("legacyIds"), list):
                    reference_ids["documents"].update(
                        alias for alias in row["legacyIds"] if isinstance(alias, str)
                    )
    except (ValueError,KeyError,TypeError,UnicodeError) as exc:
        issues.append({"code":"CANONICAL_REGISTRY_UNREADABLE","kind":kind,"detail":str(exc)[:160]})
        continue
    generated=json.loads((out/(kind+".json")).read_text())["records"]
    expected={}
    for record in generated:
        if record["integrationStatus"] == "INTEGRATED" and len(record["alternatives"]) == 1:
            expected[record["id"]] = record["alternatives"][0]
        elif record["integrationStatus"] == "SAFE_FIELDWISE_MERGE" and record.get("safeMerge"):
            safe = record["safeMerge"]
            expected[record["id"]] = {"data": safe["data"], "digest": safe["digest"],
                "provenance": safe["provenance"], "safeMerge": True,
                "mergePolicy": safe["mergePolicy"], "fieldVariantHistory": safe["fieldVariants"]}
    actual={}
    for row in rows:
        if not isinstance(row,dict) or not isinstance(row.get("_integration"),dict):
            issues.append({"code":"CANONICAL_PROVENANCE_MISSING","kind":kind})
            continue
        meta=row["_integration"]
        ident=meta.get("id")
        if not isinstance(ident,str) or ident in actual:
            issues.append({"code":"CANONICAL_ID_INVALID_OR_DUPLICATE","kind":kind,"id":ident})
            continue
        actual[ident]=row
    for ident in sorted(set(expected)-set(actual)):
        issues.append({"code":"CANONICAL_RECORD_MISSING","kind":kind,"id":ident})
    for ident in sorted(set(actual)-set(expected)):
        issues.append({"code":"UNSAFE_CANONICAL_RECORD","kind":kind,"id":ident})
    for ident in sorted(set(expected)&set(actual)):
        alt=expected[ident]
        row=actual[ident]
        payload={k:v for k,v in row.items() if k!="_integration"}
        # integrate_all adds a normalized "id" to canonical rows even when the
        # source used documentId/event_id/candidate_id/etc. Compare source payloads
        # without treating that generated compatibility field as source mutation.
        if "id" not in alt["data"] and not alt.get("safeMerge"):
            payload.pop("id", None)
        digest=hashlib.sha256(json.dumps(payload,ensure_ascii=False,sort_keys=True,
                              separators=(",",":")).encode()).hexdigest()
        if digest!=alt["digest"] or row["_integration"].get("digest")!=alt["digest"]:
            issues.append({"code":"CANONICAL_PAYLOAD_MISMATCH","kind":kind,"id":ident})
        if row["_integration"].get("provenance")!=alt["provenance"]:
            issues.append({"code":"CANONICAL_PROVENANCE_MISMATCH","kind":kind,"id":ident})
        if alt.get("safeMerge"):
            meta = row["_integration"]
            if meta.get("mergePolicy") != alt["mergePolicy"]:
                issues.append({"code":"CANONICAL_MERGE_POLICY_MISMATCH","kind":kind,"id":ident})
            if meta.get("fieldVariantHistory") != alt["fieldVariantHistory"]:
                issues.append({"code":"CANONICAL_FIELD_VARIANT_HISTORY_MISMATCH","kind":kind,"id":ident})

aux=json.loads((out/"auxiliary.json").read_text())["records"]
aux_paths={a["source"] for a in aux}
missing_aux=[s["path"] for s in sources if s["status"]=="AUXILIARY_JSON_INDEXED" and s["path"] not in aux_paths]
for p in missing_aux:issues.append({"code":"AUXILIARY_SOURCE_MISSING","path":p})
# Verify operational sidecar links across all preserved research layers.
link_file=out/"operational-links.json"
if not link_file.is_file():
    issues.append({"code":"OPERATIONAL_LINKS_MISSING"})
else:
    links=json.loads(link_file.read_text())
    seen=set()
    link_fields={
        "candidatePoliticianIds":"politicians",
        "relatedEventIds":"events",
        "relatedDocumentIds":"documents",
        "relatedClaimIds":"claims",
        "relatedOrganizationIds":"organizations",
        "relatedRoleIds":"roles",
    }
    for row in links.get("linked",[])+links.get("unlinked",[]):
        path=row["source"]
        if path in seen:issues.append({"code":"DUPLICATE_OPERATIONAL_SOURCE","path":path})
        seen.add(path)
        if path not in paths:issues.append({"code":"UNKNOWN_OPERATIONAL_SOURCE","path":path})
        relation_total=0
        for field,target in link_fields.items():
            refs=row.get(field,[])
            if not isinstance(refs,list):
                issues.append({"code":"INVALID_OPERATIONAL_REFERENCE_LIST","path":path,"field":field})
                continue
            relation_total+=len(refs)
            for ref in refs:
                if not isinstance(ref,str) or ref not in reference_ids[target]:
                    issues.append({"code":"UNKNOWN_OPERATIONAL_REFERENCE","path":path,
                                   "field":field,"targetKind":target,"targetId":ref})
        status=row.get("status")
        if relation_total==0 and status!="NO_EXPLICIT_IDENTITY":
            issues.append({"code":"OPERATIONAL_LINK_STATUS_MISMATCH","path":path,"status":status})
        elif relation_total==1 and status!="EXPLICITLY_LINKED":
            issues.append({"code":"OPERATIONAL_LINK_STATUS_MISMATCH","path":path,"status":status})
        elif relation_total>1 and status!="EXPLICITLY_MULTI_LINKED":
            issues.append({"code":"OPERATIONAL_LINK_STATUS_MISMATCH","path":path,"status":status})
    if sum(links.get("layerCounts",{}).values())!=len(seen):
        issues.append({"code":"OPERATIONAL_LAYER_COUNT_MISMATCH"})
    # The sidecar link file is an audit view; the canonical registry is the
    # queryable central layer. Verify one stable record for every preserved file.
    sidecar_file=canonical_root/"operational_layers.json"
    if not sidecar_file.is_file():
        issues.append({"code":"CANONICAL_OPERATIONAL_LAYER_REGISTRY_MISSING"})
    else:
        try:
            sidecar=json.loads(sidecar_file.read_text(encoding="utf-8"))
            sidecar_rows=sidecar.get("records",[])
            link_by_source={r["source"]:r for r in links.get("linked",[])+links.get("unlinked",[])}
            source_by_path={r["path"]:r for r in sources}
            sidecar_seen=set()
            sidecar_ids=set()
            if not isinstance(sidecar_rows,list):
                raise ValueError("records must be a list")
            for row in sidecar_rows:
                path=row.get("sourcePath")
                ident=row.get("id")
                if not isinstance(path,str) or path in sidecar_seen:
                    issues.append({"code":"CANONICAL_OPERATIONAL_SOURCE_DUPLICATE_OR_INVALID","path":path})
                    continue
                sidecar_seen.add(path)
                expected_id="sidecar-"+hashlib.sha256(path.encode("utf-8")).hexdigest()[:24]
                if ident!=expected_id or ident in sidecar_ids:
                    issues.append({"code":"CANONICAL_OPERATIONAL_ID_INVALID_OR_DUPLICATE","id":ident,"path":path})
                sidecar_ids.add(ident)
                source=source_by_path.get(path)
                link=link_by_source.get(path)
                if source is None or link is None:
                    issues.append({"code":"CANONICAL_OPERATIONAL_SOURCE_UNKNOWN","path":path})
                    continue
                if row.get("sourceSha256")!=source.get("sha256") or row.get("sourceSha256")!=link.get("sha256"):
                    issues.append({"code":"CANONICAL_OPERATIONAL_SOURCE_HASH_MISMATCH","path":path})
                for field in ("layer","linkStatus","candidatePoliticianIds","relatedEventIds",
                              "relatedDocumentIds","relatedClaimIds","relatedOrganizationIds","relatedRoleIds"):
                    source_field={"linkStatus":"status"}.get(field,field)
                    if row.get(field)!=link.get(source_field):
                        issues.append({"code":"CANONICAL_OPERATIONAL_LINK_MISMATCH","path":path,"field":field})
            if sidecar_seen!=set(link_by_source):
                issues.append({"code":"CANONICAL_OPERATIONAL_SOURCE_SET_MISMATCH",
                               "missing":sorted(set(link_by_source)-sidecar_seen)[:20],
                               "extra":sorted(sidecar_seen-set(link_by_source))[:20]})
            if sidecar.get("sourceCount")!=len(sidecar_rows) or sidecar.get("sourceCount")!=len(link_by_source):
                issues.append({"code":"CANONICAL_OPERATIONAL_SOURCE_COUNT_MISMATCH"})
        except (ValueError,KeyError,TypeError,UnicodeError) as exc:
            issues.append({"code":"CANONICAL_OPERATIONAL_LAYER_REGISTRY_UNREADABLE","detail":str(exc)[:160]})
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
    for kind in ("documents","claims","events","politicians","organizations","roles"):
        for row in staged.get(kind,[]):
            if not isinstance(row,dict) or not isinstance(row.get("id"),str):
                continue
            if row["id"] not in reference_ids[kind]:
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
    "evidenceDocumentIds":"documents", "linkedDocumentIds":"documents",
    "supportingDocumentIds":"documents", "contradictingDocumentIds":"documents",
    "relatedEventIds":"events", "eventIds":"events", "linkedEventIds":"events",
    "relatedClaimIds":"claims", "claimIds":"claims",
    "relatedPoliticianIds":"politicians", "politicianIds":"politicians",
    "linkedPoliticianIds":"politicians",
    "relatedOrganizationIds":"organizations", "organizationIds":"organizations",
    "relatedRoleIds":"roles", "roleIds":"roles",
    "related_document_ids":"documents", "document_ids":"documents",
    "evidence_document_ids":"documents", "linked_document_ids":"documents",
    "supporting_document_ids":"documents", "contradicting_document_ids":"documents",
    "related_event_ids":"events", "event_ids":"events", "linked_event_ids":"events",
    "related_claim_ids":"claims", "claim_ids":"claims",
    "related_politician_ids":"politicians", "politician_ids":"politicians",
    "linked_politician_ids":"politicians",
    "related_organization_ids":"organizations", "organization_ids":"organizations",
    "related_role_ids":"roles", "role_ids":"roles",
}
reference_issues=[]
for kind in kinds:
    registry=json.loads((out/(kind+".json")).read_text())
    for record in registry["records"]:
        for alternative in record["alternatives"]:
            payload=alternative["data"]
            fields_to_check = dict(reference_fields)
            if kind == "roles":
                fields_to_check["eventLinks"] = "events"
            for field,target in fields_to_check.items():
                if field not in payload:
                    continue
                refs=payload[field]
                if not isinstance(refs,list):
                    reference_issues.append({"code":"INVALID_REFERENCE_LIST",
                        "kind":kind,"id":record["id"],"field":field})
                    continue
                for ref in refs:
                    if not isinstance(ref,str) or ref not in reference_ids[target]:
                        reference_issues.append({"code":"DANGLING_REFERENCE",
                            "kind":kind,"id":record["id"],"field":field,
                            "targetKind":target,"targetId":ref})
issues.extend(reference_issues)
summary={"sourceFiles":len(sources),"uniqueCentralIds":{k:len(v) for k,v in ids.items()},
"conflictedIds":len(report["conflictingIds"]),"auxiliaryRecords":len(aux),
"unresolvedSources":[s["path"] for s in sources if s["status"] in ("PARSE_ERROR","AUXILIARY_JSON_INDEXED","PARTIAL_RECORDS_INDEXED","PARTIAL_CANONICAL_MATERIALIZED")],
"integrityIssues":issues,"referenceIssueCount":len(reference_issues),
"crosswalkGaps":crosswalk_gaps,
"rootSyncStatus":root_sync.get("centralSync","MISSING"),
"centralSync":"PARTIAL" if report["conflictingIds"] or report["parseErrors"] or aux or crosswalk_gaps or issues or root_sync.get("centralSync")!="PASS" else "PASS",
"note":"PARTIAL includes structural integrity failures as well as unresolved historical conflicts and auxiliary sources. Registry presence is not proof of historical adjudication."}
(out/"integrity-audit.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({k:v for k,v in summary.items() if k not in ("unresolvedSources","integrityIssues")},ensure_ascii=False))
# A partial audit must never return success to CI or an hourly worker.
# The integrator intentionally preserves conflicting alternatives and auxiliary
# sources; those remain unresolved until separately adjudicated or mapped.
if summary["centralSync"] != "PASS" or issues:
    sys.exit(1)

