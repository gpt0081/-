#!/usr/bin/env python3
"""Produce source-preserving operational sidecar links; no speculative identity merges."""
import collections, hashlib, json, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
data=root/"data"
out=data/"integration"/"generated"
source_index=json.loads((out/"sources.json").read_text())["sources"]
politicians=json.loads((data/"politicians.json").read_text())["politicians"]
by_id={p["id"]:p for p in politicians if isinstance(p,dict) and p.get("id")}
by_legacy=collections.defaultdict(set)
for p in politicians:
    if not isinstance(p,dict) or not p.get("id"):continue
    for alias in p.get("legacyIds",[]):
        if isinstance(alias,str):by_legacy[alias].add(p["id"])
linked=[];unlinked=[];counts=collections.Counter()
for s in source_index:
    path=s["path"]
    if path.startswith("data/evidence/"):layer="evidence"
    elif path.startswith("data/annals/"):layer="annals"
    elif path.endswith("-coverage.json"):layer="coverage"
    elif path.endswith("-open-leads.json"):layer="open_leads"
    else:continue
    counts[layer]+=1
    p=root/path
    obj=None
    if p.suffix==".json":
        try:obj=json.loads(p.read_text(encoding="utf-8-sig"))
        except (ValueError,UnicodeError):pass
    ids=[]
    if isinstance(obj,dict):
        for k in ("politicianId","politician_id","personId","actorId"):
            v=obj.get(k)
            if isinstance(v,str):ids.append(v)
    for pid,person in by_id.items():
        key={"evidence":"evidenceFile","annals":"annalsFile","coverage":"coverageFile","open_leads":"openLeadsFile"}[layer]
        if person.get(key)==path:ids.append(pid)
    candidates=set()
    for pid in ids:
        if pid in by_id:candidates.add(pid)
        candidates.update(by_legacy.get(pid,()))
    item={"source":path,"sha256":s["sha256"],"layer":layer,"declaredIds":sorted(set(ids)),
          "candidatePoliticianIds":sorted(candidates)}
    if len(candidates)==1:
        item["status"]="EXPLICITLY_LINKED"
        linked.append(item)
    else:
        item["status"]="AMBIGUOUS_IDENTITY" if len(candidates)>1 else "NO_EXPLICIT_IDENTITY"
        unlinked.append(item)
result={"schemaVersion":1,"scope":"Evidence, annals, coverage and open leads sidecar",
        "policy":"Only explicit IDs or exact registry file references count; no filename-based identity assumptions",
        "layerCounts":dict(counts),"linked":linked,"unlinked":unlinked}
(out/"operational-links.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"layerCounts":dict(counts),"linked":len(linked),"unlinked":len(unlinked)}))
