import json,os,re,shutil
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
BK="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_critic/backup"
os.makedirs(BK,exist_ok=True)
# (fixture, old, new) - rename the LESS entrenched side of each cross-scenario collision
RENAMES=[
 ("s2-discovery-gaps","Marisol","Renata"),        # vs s8/s9 attendee Marisol Bettencourt
 ("s6-discovery-crm-sales","Marcus","Emmett"),    # vs s1/s3/s10 offstage IT provider Marcus
 ("s6-discovery-crm-sales","Ravi","Anil"),        # vs s1/s3 structural engineer Ravi
 ("s7-discovery-service-desk","Junie","Miriam"),  # vs s8/s9 superintendent Junie Rasco
 ("s7-discovery-service-desk","Delia","Odette"),  # vs s6 attendee Delia Ostrowski
 ("s7-discovery-service-desk","Corinne","Imani"), # vs s8 CFO Corinne
 ("s10-support-checkin","Kestrel","Fenwick"),     # vs s6 customer Kestrel Fabrication
]
touched=set()
for fx,old,new in RENAMES:
    d=os.path.join(F,fx)
    for fn in os.listdir(d):
        if not (fn.endswith(".txt") or fn.endswith(".json") or fn.endswith(".md")): continue
        p=os.path.join(d,fn)
        src=open(p).read()
        n=len(re.findall(r"\b"+old+r"\b",src))
        if not n: continue
        if p not in touched:
            shutil.copy(p,os.path.join(BK,fx+"__"+fn)); touched.add(p)
        open(p,"w").write(re.sub(r"\b"+old+r"\b",new,src))
        print(f"  {fx}/{fn}: {old} -> {new}  ({n} occurrences)")
# s7 objection types: 'Spec name: nuance' -> 'Spec name (nuance)', matching the other nine keys
SPEC=["Price feels high","Needs to think it over","Must check with someone","Wrong time, next quarter","We'll build it ourselves","Talking to other partners","Just send a proposal or pricing","monday itself is the problem","Team won't adopt it"]
p=os.path.join(F,"s7-discovery-service-desk","answer-key.json")
if p not in touched: shutil.copy(p,os.path.join(BK,"s7-discovery-service-desk__answer-key.json.obj"))
k=json.load(open(p))
fixed=0
for o in k["objections"]:
    t=o["type"]
    for s in SPEC:
        if t.startswith(s+": "):
            o["type"]=s+" ("+t[len(s)+2:]+")"; fixed+=1; break
json.dump(k,open(p,"w"),indent=2,ensure_ascii=False)
open(p,"a").write("\n")
print(f"\n  s7 objection types normalised to the set's 'Spec name (nuance)' form: {fixed}")
