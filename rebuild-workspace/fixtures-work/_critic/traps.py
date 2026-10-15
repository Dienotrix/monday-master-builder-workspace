import json,os
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
o=[]
for s in SC:
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    o.append(f"\n########## {s} TRAPS ({len(k['traps'])})")
    for i,t in enumerate(k["traps"]):
        t=t if isinstance(t,str) else json.dumps(t)
        o.append(f"  {i+1:2}. {t[:150]}")
    o.append(f"\n---------- {s} LEAK BLOCKLIST ({len(k['expected_leak_blocklist'])})")
    for i,t in enumerate(k["expected_leak_blocklist"]):
        t=t if isinstance(t,str) else json.dumps(t)
        o.append(f"  {i+1:2}. {t[:130]}")
    o.append(f"\n---------- {s} ACCEPTED_BEHAVIOURS ({len(k['accepted_behaviours'])})")
    for i,t in enumerate(k["accepted_behaviours"]):
        t=t if isinstance(t,str) else json.dumps(t)
        o.append(f"  {i+1:2}. {t[:120]}")
open("/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_critic/traps.txt","w").write("\n".join(o))
print("written", len("\n".join(o)))
