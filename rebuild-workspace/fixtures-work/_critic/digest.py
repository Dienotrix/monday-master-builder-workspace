import json,os
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
out=[]
for s in SC:
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    out.append("="*100)
    out.append(f"### {s}  call_type={k['call_type']}")
    c=k["company"]; out.append(f"COMPANY: {c}")
    out.append(f"ATTENDEES: "+ " | ".join(f"{a.get('name')} :: {a.get('role')} :: {a.get('side')} :: {a.get('decision_role')}" for a in k["attendees"]))
    out.append(f"TRANSCRIPT_FORMAT: {k['transcript_format']}")
    out.append("PURPOSE: "+json.dumps(k["purpose_of_this_fixture"])[:2500])
    out.append("PRODUCTS: "+ " || ".join(f"{p.get('kind')}: {p.get('why')[:300]}" for p in k["expected_monday_products"]))
    out.append("RUBRIC R: "+ "; ".join(f"{r['criterion'].split(' ')[0]}={r['status']}" for r in k["rubric"] if r["criterion"].startswith("R")))
    out.append("RUBRIC P: "+ "; ".join(f"{r['criterion']}={r['status']}" for r in k["rubric"] if not r["criterion"].startswith("R")))
    n=k["numbers"]
    out.append(f"BLEED: {n['bleed'].get('status')} | {str(n['bleed'].get('value'))[:400]}")
    out.append(f"UPSIDE: {n['upside'].get('status')} | {str(n['upside'].get('value'))[:400]}")
    v=k["expected_verdict"]
    out.append(f"VERDICT: {v['verdict']}")
    out.append("GATES_MET: "+json.dumps(v.get("gates_met")))
    out.append("GATES_NOT: "+json.dumps(v.get("gates_not_met")))
    out.append("VERDICT_NOTE: "+str(v.get("note"))[:900])
    ac=k["account_context"]
    out.append(f"TIER: {ac.get('tier')}")
    out.append("PRODUCTS_ENABLED: "+json.dumps(ac.get("products_enabled"))[:600])
    out.append("EXISTING_SETUP: "+str(ac.get("existing_monday_setup"))[:700])
    out.append("TIER_EVIDENCE: "+str(ac.get("evidence_quote_or_null")))
    es=k["expected_structures"]
    out.append("NATIVE_BOARDS: "+ " || ".join(f"{b.get('product')}/{b.get('entity')}: {str(b.get('why'))[:150]}" for b in es.get("native_boards_required",[])) or "NONE")
    out.append(f"PORTFOLIO_EXPECTED: {es.get('portfolio_expected')!r} REASON: {str(es.get('portfolio_reason'))[:500]}")
    out.append(f"LOOKALIKE_TRAPS: n={len(es.get('lookalike_traps',[]))}")
    out.append("STRUCT_NOTES: "+str(es.get("notes"))[:600])
    out.append("INTEGRATIONS: "+json.dumps(k["integrations_mentioned"])[:800])
    out.append("COMPLIANCE: "+json.dumps(k["compliance_or_security_signals"])[:800])
    out.append("REQUESTED_CHANGES: "+ " || ".join(f"[{r.get('type')}] {str(r.get('description'))[:110]}" for r in k["requested_changes"]))
    out.append("COMMITMENTS: "+ " || ".join(f"{str(cm.get('what'))[:90]} ~{cm.get('owner')} ~{cm.get('date')}" for cm in k["commitments_and_next_steps"]))
    out.append("OBJ_TYPES: "+ " || ".join(o["type"].split(" (")[0].split(":")[0] for o in k["objections"]))
open("/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_critic/digest.txt","w").write("\n".join(out))
print("\n".join(out))
