import json,os,re
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
def walk(o,kind="quote"):
    out=[]
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ("quote","evidence_quote_or_null") and isinstance(v,str): out.append(v)
            else: out+=walk(v,kind)
    elif isinstance(o,list):
        for v in o: out+=walk(v,kind)
    return out
def locs(o):
    out=[]
    if isinstance(o,dict):
        for k,v in o.items():
            if k=="location" and isinstance(v,str): out.append(v)
            else: out+=locs(v)
    elif isinstance(o,list):
        for v in o: out+=locs(v)
    return out
data={}
for s in SC:
    t=open(os.path.join(F,s,"transcript.txt")).read()
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    data[s]=(t,k,walk(k),locs(k))
print("=== COLLISION DETAIL ===")
for name in ["Marisol","Marcus","Junie","Ravi","Kelsey","Gary","Stefan","Travis","Wes","Delia","Tansy","Curtis","Yvette"]:
    hits=[]
    for s in SC:
        t,k,qs,ls=data[s]
        tc=len(re.findall(r"\b"+name+r"\b",t))
        qc=sum(1 for q in qs if re.search(r"\b"+name+r"\b",q))
        lc=sum(1 for l in ls if re.search(r"\b"+name+r"\b",l))
        kc=len(re.findall(r"\b"+name+r"\b",json.dumps(k)))
        if tc or kc: hits.append(f"{s.split('-')[0]}(T{tc},inQuote{qc},inLoc{lc},K{kc})")
    if hits: print(f"  {name:10} "+"  ".join(hits))
print("\n=== SAMPLE LOCATIONS ===")
for s in SC:
    ls=data[s][3]
    print(f"  {s:42} n={len(ls):4} e.g. {ls[0] if ls else '-'!r} | {ls[5] if len(ls)>5 else ''!r}")
print("\n=== GATE NAME CONVENTION ===")
STAGES=["Solution blueprint","Build","First demo (v0.1)","Pricing or proposal prep","v1.0 sign-off"]
for s in SC:
    v=data[s][1]["expected_verdict"]; all_g=(v.get("gates_met") or [])+(v.get("gates_not_met") or [])
    found={st:sum(1 for g in all_g if g.startswith(st)) for st in STAGES}
    ok=all(c==1 for c in found.values())
    print(f"  {s:42} total={len(all_g)} ok={ok} {'' if ok else found}")
print("\n=== RUBRIC CRITERION NAMES ===")
import collections
rn=collections.Counter()
for s in SC:
    for r in data[s][1]["rubric"]: rn[r["criterion"]]+=1
R=[c for c in rn if c.startswith("R")]
P=[c for c in rn if not c.startswith("R")]
print("  R names:",sorted(set(R)))
print("  P suffixes:",sorted({c.split(" ",1)[1] for c in P}))
print("  P prefixes:",sorted({c.split(" ",1)[0] for c in P}))
sts=collections.Counter()
for s in SC:
    for r in data[s][1]["rubric"]: sts[r["status"]]+=1
print("  statuses:",dict(sts))
print("\n=== PER-PAIN GRID ===")
for s in SC:
    rows=[r for r in data[s][1]["rubric"] if not r["criterion"].startswith("R")]
    byp=collections.OrderedDict()
    for r in rows:
        p,chk=r["criterion"].split(" ",1)
        byp.setdefault(p,{})[chk]=r["status"][0].upper()
    print(f"  {s}")
    for p,d in byp.items():
        seq=[d.get(c,"-") for c in ["Stated","Concrete","Workaround","Reach","Cost inputs","Trajectory"]]
        exc = all(d.get(c)=="met" for c in ["Stated","Concrete","Workaround"]) if all(c in d for c in ["Stated","Concrete","Workaround"]) else None
        print(f"     {p:4} S{seq[0]} C{seq[1]} W{seq[2]} R{seq[3]} ${seq[4]} T{seq[5]}   excavated={'yes' if seq[0]=='M' and seq[1]=='M' and seq[2]=='M' else 'no'}")
