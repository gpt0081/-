#!/usr/bin/env python3
"""Build explicit cross-layer links without filename- or name-based identity guesses."""
import collections, hashlib, json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[1]
data=root/"data"
out=data/"integration"/"generated"
source_index=json.loads((out/"sources.json").read_text(encoding="utf-8-sig"))["sources"]

def read_rows(path, key):
    obj=json.loads(path.read_text(encoding="utf-8-sig"))
    return obj.get(key,[]) if isinstance(obj,dict) else []

root_people=read_rows(data/"politicians.json","politicians")
root_events=read_rows(data/"events.json","events")
president_rows=json.loads((data/"presidents.json").read_text(encoding="utf-8-sig"))
generated={kind:read_rows(out/(kind+".json"),"records")
           for kind in ("documents","claims","events","politicians","organizations","roles")}
known={kind:{r.get("id") for r in rows if isinstance(r,dict) and r.get("id")}
       for kind,rows in generated.items()}
known["politicians"].update(p.get("id") for p in root_people if isinstance(p,dict) and p.get("id"))
known["events"].update(r.get("id") or r.get("eventId") or r.get("actionId")
                       for r in root_events if isinstance(r,dict))
if isinstance(president_rows, list):
    known["politicians"].update(
        row.get("id") for row in president_rows
        if isinstance(row, dict) and isinstance(row.get("id"), str)
    )
for values in known.values():
    values.discard(None)

people_by_id={p["id"]:p for p in generated["politicians"] if isinstance(p,dict) and p.get("id")}
people_by_id.update({p["id"]:p for p in root_people if isinstance(p,dict) and p.get("id")})
by_legacy=collections.defaultdict(set)
for person in people_by_id.values():
    for alias in person.get("legacyIds",[]) if isinstance(person.get("legacyIds"),list) else []:
        if isinstance(alias,str):
            by_legacy[alias].add(person["id"])

patterns={
    "politicians":re.compile(r"\b(?:pol|cand|candidate|president|foreign|ext|actor)-[A-Za-z0-9][A-Za-z0-9-]*\b"),
    "events":re.compile(r"\b(?:evt|ACT|act)-[A-Za-z0-9][A-Za-z0-9-]*\b"),
    "documents":re.compile(r"\b(?:d[0-9]+-[A-Za-z0-9][A-Za-z0-9-]*|(?:doc|DOC)-[A-Za-z0-9][A-Za-z0-9-]*)\b|\burn:source:[0-9a-f]{24}\b"),
    "claims":re.compile(r"\b(?:claim|clm)-[A-Za-z0-9][A-Za-z0-9-]*\b"),
    "organizations":re.compile(r"\borg-[A-Za-z0-9][A-Za-z0-9-]*\b"),
    "roles":re.compile(r"\brole-[A-Za-z0-9][A-Za-z0-9-]*\b"),
}
file_fields={
    "evidence":("evidenceFile","evidenceFiles"),
    "annals":("annalsFile","annalsFiles"),
    "coverage":("coverageFile","coverageFiles"),
    "open_leads":("openLeadsFile","openLeadsFiles"),
}
linked=[];unlinked=[];layer_counts=collections.Counter();relation_counts=collections.Counter()
for source in source_index:
    path=source["path"]
    if path.startswith("data/evidence/"):
        layer="evidence"
    elif path.startswith("data/annals/"):
        layer="annals"
    elif path.startswith("data/research/coverage/") or path.endswith("-coverage.json"):
        layer="coverage"
    elif path.startswith("data/research/leads/") or path.startswith("data/research/lead-queues/") or path.endswith("-open-leads.json"):
        layer="lead_queue"
    elif path.startswith("data/research/debt/") or path.startswith("data/research/history-debt/") or path.endswith("HISTORY_DEBT.md"):
        layer="history_debt"
    else:
        continue
    layer_counts[layer]+=1
    file=root/path
    try:
        content=file.read_text(encoding="utf-8-sig",errors="replace")
    except OSError:
        content=""
    found={}
    for kind,pattern in patterns.items():
        found[kind]=set(pattern.findall(content)) & known[kind]

    # Exact registry path references are also explicit relations.
    for pid,person in people_by_id.items():
        fields=file_fields.get(layer,())
        referenced=False
        for field in fields:
            value=person.get(field)
            if isinstance(value,str) and value==path:
                referenced=True
            elif isinstance(value,list) and path in value:
                referenced=True
        research_refs=person.get("researchRefs",[])
        if isinstance(research_refs,list) and path in research_refs:
            referenced=True
        if referenced:
            found["politicians"].add(pid)
        for legacy in person.get("legacyIds",[]) if isinstance(person.get("legacyIds"),list) else []:
            if legacy in found["politicians"]:
                found["politicians"].add(pid)

    item={
        "source":path,
        "sha256":source["sha256"],
        "layer":layer,
        "candidatePoliticianIds":sorted(found["politicians"]),
        "relatedEventIds":sorted(found["events"]),
        "relatedDocumentIds":sorted(found["documents"]),
        "relatedClaimIds":sorted(found["claims"]),
        "relatedOrganizationIds":sorted(found["organizations"]),
        "relatedRoleIds":sorted(found["roles"]),
        "status":"NO_EXPLICIT_IDENTITY"
    }
    total=sum(len(item[field]) for field in (
        "candidatePoliticianIds","relatedEventIds","relatedDocumentIds",
        "relatedClaimIds","relatedOrganizationIds","relatedRoleIds"))
    for field in ("candidatePoliticianIds","relatedEventIds","relatedDocumentIds",
                  "relatedClaimIds","relatedOrganizationIds","relatedRoleIds"):
        relation_counts[field]+=len(item[field])
    if total==1:
        item["status"]="EXPLICITLY_LINKED"
        linked.append(item)
    elif total>1:
        item["status"]="EXPLICITLY_MULTI_LINKED"
        linked.append(item)
    else:
        unlinked.append(item)

result={
    "schemaVersion":2,
    "scope":"Evidence, annals, coverage, open leads, lead queues and history-debt sidecar links",
    "policy":"Only stable IDs present in file content or exact registry file references count; no filename or person-name inference.",
    "layerCounts":dict(sorted(layer_counts.items())),
    "relationCounts":dict(sorted(relation_counts.items())),
    "linked":linked,
    "unlinked":unlinked
}
# Materialize every evidence/annals/coverage/lead/debt sidecar as a central
# first-class source-pointer record. Unlinked items remain present with an explicit
# NO_EXPLICIT_IDENTITY status; they are not dropped or assigned by filename.
source_by_path = {row["path"]: row for row in source_index}
canonical_records = []
for row in linked + unlinked:
    source_meta = source_by_path[row["source"]]
    stable = "sidecar-" + hashlib.sha256(row["source"].encode("utf-8")).hexdigest()[:24]
    canonical_records.append({
        "id": stable,
        "layer": row["layer"],
        "sourcePath": row["source"],
        "sourceSha256": row["sha256"],
        "sourceBytes": source_meta.get("bytes"),
        "sourceStatus": source_meta.get("status"),
        "targetRegistries": source_meta.get("targetRegistries", []),
        "linkStatus": row["status"],
        "candidatePoliticianIds": row["candidatePoliticianIds"],
        "relatedEventIds": row["relatedEventIds"],
        "relatedDocumentIds": row["relatedDocumentIds"],
        "relatedClaimIds": row["relatedClaimIds"],
        "relatedOrganizationIds": row["relatedOrganizationIds"],
        "relatedRoleIds": row["relatedRoleIds"],
        "provenance": [{"path": row["source"], "sha256": row["sha256"]}]
    })
canonical_dir = out.parent / "canonical"
canonical_dir.mkdir(parents=True, exist_ok=True)
canonical_registry = {
    "schemaVersion": 1,
    "registryType": "operational_layers",
    "selectionPolicy": "ALL_SIDECAR_FILES_PRESERVED; EXPLICIT_ID_LINKS_ONLY; UNLINKED_FILES_RETAINED",
    "sourceCount": len(canonical_records),
    "linkedCount": len(linked),
    "unlinkedCount": len(unlinked),
    "layerCounts": dict(sorted(layer_counts.items())),
    "relationCounts": dict(sorted(relation_counts.items())),
    "records": sorted(canonical_records, key=lambda item: item["id"])
}
(canonical_dir / "operational_layers.json").write_text(
    json.dumps(canonical_registry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(out/"operational-links.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"layerCounts":dict(layer_counts),"linked":len(linked),"unlinked":len(unlinked),
                  "centralSidecarRecords":len(canonical_records),
                  "relationCounts":dict(relation_counts)},ensure_ascii=False))
