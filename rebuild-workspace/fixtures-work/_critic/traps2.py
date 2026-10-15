import json,os
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
for s in SC:
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    print(f"\n##### {s} TRAPS n={len(k['traps'])}")
    for i,t in enumerate(k["traps"]):
        print(f" {i+1:2}. {(t if isinstance(t,str) else json.dumps(t))[:115]}")
