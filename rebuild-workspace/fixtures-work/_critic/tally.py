import json,os,collections
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
SPEC=["Price feels high","Needs to think it over","Must check with someone","Wrong time, next quarter","We'll build it ourselves","Talking to other partners","Just send a proposal or pricing","monday itself is the problem","Team won't adopt it"]
K={s:json.load(open(os.path.join(F,s,"answer-key.json"))) for s in SC}
print("=== OBJECTION TALLY (spec name x scenario) ===")
print(f"{'objection':34}"+"".join(f"{s.split('-')[0]:>5}" for s in SC))
for name in SPEC+["Outside the map"]:
    row=[]
    for s in SC:
        n=sum(1 for o in K[s]["objections"] if o["type"].split(" (")[0].split(":")[0].strip()==name or (name=="Outside the map" and o["type"].startswith("Outside the map")))
        row.append(n)
    print(f"{name:34}"+"".join(f"{v if v else '-':>5}" for v in row))
print(f"{'TOTAL':34}"+"".join(f"{len(K[s]['objections']):>5}" for s in SC))
print("\n=== REQUESTED CHANGES ===")
for s in SC:
    c=collections.Counter(r.get("type") for r in K[s]["requested_changes"])
    print(f"  {s:42} n={len(K[s]['requested_changes']):3} {dict(c)}")
print("\n=== NATIVE BOARDS REQUIRED ===")
for s in SC:
    es=K[s]["expected_structures"]
    nb=es.get("native_boards_required",[])
    print(f"  {s:42} portfolio={str(es.get('portfolio_expected')):6} lookalikes={len(es.get('lookalike_traps',[])):2} boards={[f\"{b.get('product')}:{b.get('entity')}\" for b in nb]}")
print("\n=== ACCOUNT TIER (first 90 chars) ===")
for s in SC:
    ac=K[s]["account_context"]
    print(f"  {s:42} {str(ac.get('tier'))[:90]}")
print("\n=== DEFERRED MENTIONS ===")
import re
for s in SC:
    j=json.dumps(K[s])
    hits=set()
    for m in re.finditer(r"[^\"]{0,90}defer[a-z]*[^\"]{0,90}",j):
        hits.add(m.group(0)[:150])
    print(f"  {s}: {len(hits)} mentions")
    for h in list(hits)[:3]: print("      ...",h[:140])
