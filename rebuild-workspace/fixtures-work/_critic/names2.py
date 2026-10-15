import json,os,re,collections
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
CHAIN={"s1-discovery-strong":"A","s3-followup-demo-feedback":"A","s10-support-checkin":"A","s8-discovery-enterprise-pmo":"B","s9-followup-no-portfolio-unlabelled":"B"}
words=set(w.strip().lower() for w in open("/usr/share/dict/words"))
allt=collections.defaultdict(set); ctx=collections.defaultdict(list)
for s in SC:
    t=open(os.path.join(F,s,"transcript.txt")).read()
    for m in re.finditer(r"\b[A-Z][a-z]{2,}\b",t):
        w=m.group(0)
        if w.lower() in words: continue
        allt[w].add(s)
        if len(ctx[(w,s)])<2: ctx[(w,s)].append(t[max(0,m.start()-45):m.start()+45].replace("\n"," "))
print("=== NON-DICTIONARY PROPER NOUNS SHARED ACROSS UNRELATED FIXTURES ===")
for w,ss in sorted(allt.items()):
    ch={CHAIN.get(x,x) for x in ss}
    if len(ch)>1:
        print(f"\n## {w}  -> {sorted(ss)}")
        for s in sorted(ss):
            for c in ctx[(w,s)]: print(f"   [{s[:6]}] ...{c}...")
