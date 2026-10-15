import json,os,re,sys
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
ORDER=["scenario_id","call_type","purpose_of_this_fixture","transcript_format","company","attendees","expected_monday_products","rubric","pains","numbers","vocabulary","entities_and_workflows","integrations_mentioned","compliance_or_security_signals","objections","commitments_and_next_steps","traps","requested_changes","should_plugin_propose_a_build","expected_questions_before_building","expected_verdict","account_context","expected_structures","accepted_behaviours","expected_leak_blocklist"]
keys={};txt={}
for s in SC:
    p=os.path.join(F,s,"answer-key.json")
    keys[s]=json.load(open(p))
    txt[s]=open(os.path.join(F,s,"transcript.txt")).read()
print("=== FIELD ORDER ===")
for s in SC:
    k=list(keys[s].keys())
    print(f"{s:42} n={len(k)} order_ok={k==ORDER}")
    if k!=ORDER:
        print("   missing:",[f for f in ORDER if f not in k])
        print("   extra  :",[f for f in k if f not in ORDER])
        print("   actual :",k)
print("\n=== OBJECTION TYPES ===")
SPEC={"Price feels high","Needs to think it over","Must check with someone","Wrong time, next quarter","We'll build it ourselves","Talking to other partners","Just send a proposal or pricing","monday itself is the problem","Team won't adopt it"}
alltypes={}
for s in SC:
    for o in keys[s].get("objections",[]):
        t=o.get("type","")
        alltypes.setdefault(t,[]).append(s)
for t in sorted(alltypes):
    base=t.split(" (")[0].strip()
    ok = base in SPEC or t.startswith("Outside the map")
    print(f"  {'OK ' if ok else 'BAD'} {t!r}  -> {sorted(set(alltypes[t]))}")
print("\n=== DECISION ROLES ===")
roles={}
for s in SC:
    for a in keys[s].get("attendees",[]):
        roles.setdefault(a.get("decision_role",""),[]).append((s,a.get("name")))
for r in sorted(roles):
    print(f"  {r!r}: {[x[0] for x in roles[r]]}")
print("\n=== NAMES (people + company) ===")
for s in SC:
    c=keys[s]["company"]
    print(f"{s:42} {c.get('name')} | {[a.get('name') for a in keys[s].get('attendees',[])]}")
print("\n=== QUOTES ===")
def walkq(o,path=""):
    out=[]
    if isinstance(o,dict):
        for k,v in o.items():
            if k=="quote" and isinstance(v,str): out.append((path+"/"+k,v))
            elif k=="evidence_quote_or_null" and isinstance(v,str): out.append((path+"/"+k,v))
            else: out+=walkq(v,path+"/"+str(k))
    elif isinstance(o,list):
        for i,v in enumerate(o): out+=walkq(v,path+f"[{i}]")
    return out
tot=0
for s in SC:
    qs=walkq(keys[s]); bad=[]
    body=txt[s]
    lines=body.split("\n")
    for p,q in qs:
        if q not in body: bad.append((p,q[:60]))
        elif not any(q in ln for ln in lines): bad.append((p,"MULTILINE: "+q[:50]))
    tot+=len(qs)
    print(f"{s:42} quotes={len(qs):4} bad={len(bad)}")
    for b in bad[:6]: print("     ",b)
print("TOTAL QUOTES:",tot)
print("\n=== COUNTS ===")
for s in SC:
    k=keys[s]
    print(f"{s:42} traps={len(k.get('traps',[])):3} pains={len(k.get('pains',[])):3} rubric={len(k.get('rubric',[])):3} obj={len(k.get('objections',[])):3} vocab={len(k.get('vocabulary',[])):3} rc={len(k.get('requested_changes',[])):3} ab={len(k.get('accepted_behaviours',[])):3} leak={len(k.get('expected_leak_blocklist',[])):3} q={len(k.get('expected_questions_before_building',[])):3} build={k.get('should_plugin_propose_a_build')}")
