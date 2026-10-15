import json,os,re
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
PAIRS=[("s1-discovery-strong","Ravi"),("s3-followup-demo-feedback","Ravi"),("s6-discovery-crm-sales","Ravi"),
("s7-discovery-service-desk","Junie"),("s7-discovery-service-desk","Delia"),("s7-discovery-service-desk","Corinne"),
("s8-discovery-enterprise-pmo","Corinne"),("s6-discovery-crm-sales","Kestrel"),("s10-support-checkin","Kestrel"),
("s2-discovery-gaps","Marisol"),("s6-discovery-crm-sales","Marcus"),("s1-discovery-strong","Marcus"),("s10-support-checkin","Marcus"),
("s3-followup-demo-feedback","Marcus"),("s7-discovery-service-desk","Rosalie"),("s8-discovery-enterprise-pmo","Junie")]
def quotes(o):
    out=[]
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ("quote","evidence_quote_or_null") and isinstance(v,str): out.append(v)
            else: out+=quotes(v)
    elif isinstance(o,list):
        for v in o: out+=quotes(v)
    return out
for s,n in PAIRS:
    t=open(os.path.join(F,s,"transcript.txt")).read()
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    qs=[q for q in quotes(k) if re.search(r"\b"+n+r"\b",q)]
    print(f"\n### {s} :: {n}   transcript={len(re.findall(chr(92)+'b'+n+chr(92)+'b',t))} quotes_containing={len(qs)}")
    for m in list(re.finditer(r"\b"+n+r"\b",t))[:6]:
        print("   T: ..."+t[max(0,m.start()-90):m.start()+90].replace("\n"," | ")+"...")
    for q in qs[:4]: print("   Q: "+q[:160])
