import json,os,re,collections
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
CHAIN={"s1-discovery-strong":"A","s3-followup-demo-feedback":"A","s10-support-checkin":"A","s8-discovery-enterprise-pmo":"B","s9-followup-no-portfolio-unlabelled":"B"}
STOP=set("""I I'm We The And But So That This They You He She It A An In On At For To Of If No Yes Okay OK Right Well Yeah Yep Nope Not Now Then There Here What When Where Which Who Why How All Any Some One Two Three Four Five Six Seven Eight Nine Ten My Our Your His Her Their Its Just Like Because Consultant Monday Speaker Sorry Thanks Thank Actually Honestly Maybe Probably Every Each Both Either Neither Also Still Even Only Really Very Much More Most Less Least First Second Third Last Next Previous North South East West New Old Big Small Good Bad Great Fine Sure Anyway Meanwhile However Although Though While Since Until Before After During About Above Below Under Over Through Between Among Against Toward Within Without Around Across Behind Beyond Down Up Out Off Away Back Again Once Twice Never Always Sometimes Often Rarely Usually Generally Specifically Particularly Especially Exactly Precisely Roughly Approximately Nearly Almost Quite Rather Pretty Fairly Somewhat Slightly Barely Hardly Scarcely Enough Too Such Same Different Other Another Certain Various Several Many Few Little Lot Lots Plenty Bunch Couple Dozen Hundred Thousand Million Billion Percent Dollars Hours Days Weeks Months Years Times Ways Things Stuff People Person Team Teams Group Groups Board Boards Item Items Column Columns Row Rows View Views Form Forms Dashboard Dashboards Automation Automations Workflow Workflows Project Projects Job Jobs Task Tasks Phase Phases Stage Stages Status Statuses Type Types Kind Kinds Sort Sorts Part Parts Piece Pieces Bit Bits Side Sides End Ends Start Starts Beginning Middle Center Centre Top Bottom Front Rear Left Right""".split())
per={}
allnames=collections.defaultdict(set)
for s in SC:
    t=open(os.path.join(F,s,"transcript.txt")).read()
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    blob=t+"\n"+json.dumps(k)
    caps=set(re.findall(r"\b[A-Z][a-z]{2,}\b",t))
    names=set()
    # attendee names
    for a in k["attendees"]:
        for w in re.findall(r"\b[A-Z][a-z]+\b",a.get("name","")): names.add(w)
    # heuristic offstage: capitalized word preceded by typical name context OR appearing as speaker label
    for w in caps:
        if w in STOP: continue
        names.add(w)
    per[s]=names
    for w in names: allnames[w].add(s)
print("=== ATTENDEE-LEVEL NAME TOKENS PER FIXTURE ===")
for s in SC:
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    print(f"{s:42}", [a.get("name") for a in k["attendees"]])
print("\n=== TOKENS SHARED ACROSS DIFFERENT CHAINS (candidate collisions) ===")
def chain(s): return CHAIN.get(s,s)
for w,ss in sorted(allnames.items()):
    ch={chain(x) for x in ss}
    if len(ch)>1:
        print(f"  {w:16} -> {sorted(ss)}")
