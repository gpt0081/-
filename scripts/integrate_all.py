#!/usr/bin/env python3
"""Build a provenance-preserving consolidated index from all data sources."""
import json, pathlib, hashlib, collections
root=pathlib.Path(__file__).resolve().parents[1]
data=root/"data"
out=data/"integration"/"generated"
out.mkdir(parents=True,exist_ok=True)
types=("documents","claims","events","politicians","organizations")
records={k:[] for k in types}
sources=[]
errors=[]
for p in sorted(data.rglob("*")):
    if not p.is_file() or p.is_relative_to(data/"integration"): continue
    raw=p.read_bytes()
    rel=p.relative_to(root).as_posix()
    sources.append({"path":rel,"sha256":hashlib.sha256(raw).hexdigest(),"bytes":len(raw)})
    if p.suffix.lower()!=".json": continue
    try: obj=json.loads(raw.decode("utf-8-sig"))
    except Exception as e:
        errors.append({"path":rel,"error":str(e)[:200]})
        continue
    kind=p.relative_to(data).parts[0]
    for t in types:
        items=obj.get(t) if isinstance(obj,dict) else (obj if isinstance(obj,list) and kind==t else None)
        if not isinstance(items,list):continue
        for i,item in enumerate(items):
            if not isinstance(item,dict):continue
            ident=next((item[k] for k in ("id","documentId","claimId","eventId","politicianId","organizationId") if isinstance(item.get(k),str) and item[k]),None)
            if ident is None:ident="urn:source:"+hashlib.sha256((rel+":"+str(i)).encode()).hexdigest()[:24]
            records[t].append({"id":ident,"data":item,"source":{"path":rel,"pointer":"/"+t+"/"+str(i)}})
    if kind in types and isinstance(obj,dict) and not any(isinstance(obj.get(t),list) for t in types):
        ident=obj.get("id")
        if isinstance(ident,str) and ident:
            records[kind].append({"id":ident,"data":obj,"source":{"path":rel,"pointer":"/"}})
conflicts=[]
for t,items in records.items():
    grouped=collections.defaultdict(list)
    for item in items:grouped[item["id"]].append(item)
    for ident,versions in grouped.items():
        if len({json.dumps(v["data"],sort_keys=True,ensure_ascii=False) for v in versions})>1:
            conflicts.append({"type":t,"id":ident,"sources":[v["source"]["path"] for v in versions]})
    (out/(t+".json")).write_text(json.dumps({"schemaVersion":1,"records":items},ensure_ascii=False,indent=2)+"\\n")
(out/"sources.json").write_text(json.dumps({"sources":sources},ensure_ascii=False,indent=2)+"\\n")
report={"sourceFiles":len(sources),"recordsByType":{k:len(v) for k,v in records.items()},"parseErrors":errors,"conflictingIds":conflicts,"status":"REVIEW_REQUIRED" if errors or conflicts else "INDEX_BUILT","warning":"Non-destructive integrated index, not a verified historical database."}
(out/"report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\\n")
print(json.dumps({k:v for k,v in report.items() if k not in ("parseErrors","conflictingIds")},ensure_ascii=False))
