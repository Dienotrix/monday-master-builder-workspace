import json,os,re,collections
F="/Users/caramelm4/DelOps/rebuild-workspace/fixtures"
SC=["s1-discovery-strong","s2-discovery-gaps","s3-followup-demo-feedback","s4-discovery-software","s5-intro-thin","s6-discovery-crm-sales","s7-discovery-service-desk","s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled","s10-support-checkin"]
CHAIN={"s1-discovery-strong":"A","s3-followup-demo-feedback":"A","s10-support-checkin":"A","s8-discovery-enterprise-pmo":"B","s9-followup-no-portfolio-unlabelled":"B"}
STOP=set("""January February March April May June July August September October November December Monday Tuesday Wednesday Thursday Friday Saturday Sunday Mondays Tuesdays Wednesdays Thursdays Fridays Consultant Speaker WEBVTT Ajera Bluebeam Procore Redmine Zendesk GitHub Slack Microsoft Google Teams Outlook SharePoint Excel QuickBooks Eventbrite Trello Smartsheet Sage Epicor Prophet GoldMine ServiceChannel Dropbox Zoom Madison Milwaukee Rockford Moines Iowa Wisconsin Illinois Toledo Wayne Knoxville Chattanooga Huntsville Roanoke Raleigh Asheville Nashville Tennessee Eastern Central Pacific Mountain Kraków Krakow America North South East West Street Road Avenue Brackenholt Quillmoor Tollgrove Orrin Calderwood Ainsworth Bellamy Ridge Larkspur Harwood Cumberland Waverly Pellham Granite Fairlane Tolliver Lorna Christmas Thanksgiving Labor SOC CSAT ICRA ILSM RFP RFQ RFI PIC PM MEP HVAC CRM API SSO PII DPA WIP CDs SD DD CA IT HR VP COO CFO CEO PDF CSV URL SLA AI QA SRE PR GC GCs Pro Standard Enterprise Basic Leads Contacts Accounts Deals Opportunities Activities Tickets Incidents Workload Wall""".split())
COMMON=set("""The And But So That This They You He She It A An In On At For To Of If No Yes Okay Right Well Yeah Yep Nope Not Now Then There Here What When Where Which Who Why How All Any Some One Two Three Four Five Six Seven Eight Nine Ten Twelve Twenty Thirty Forty Fifty Sixty Ninety Hundred Thousand My Our Your His Her Their Its Just Like Because Sorry Thanks Thank Actually Honestly Maybe Probably Every Each Both Also Still Even Only Really Very Much More Most Less First Second Third Last Next New Old Big Small Good Bad Great Fine Sure Anyway However Although While Since Until Before After During About Above Below Under Over Through Between Within Without Around Across Behind Beyond Down Up Out Off Away Back Again Once Never Always Sometimes Often Usually Generally Especially Exactly Roughly Nearly Almost Quite Rather Pretty Fairly Somewhat Barely Enough Too Such Same Different Other Another Certain Various Several Many Few Little Lot Lots Plenty Couple Dozen Percent Dollars Hours Days Weeks Months Years Times Ways Things Stuff People Person Team Teams Group Groups Board Boards Item Items Column Columns Row Rows View Views Form Forms Dashboard Automation Project Projects Job Jobs Task Tasks Phase Phases Stage Stages Status Type Kind Sort Part Piece Bit Side End Start Beginning Middle Center Top Bottom Front Left Right Depends Email Engineers Makes Nobody None Noted Nothing Oof Open Perfect Please Put Safety Say Somebody Someone Sounds Take Talk Tell Theirs Those Understood Walk Was Whatever Whether With Working Works Worse Would Has Have Had Hang Morning Afternoon Evening Night Today Tomorrow Yesterday Week Month Year Quarter Spring Summer Autumn Fall Winter Cool Nice Wow Huh Hmm Uh Um Ah Oh Hi Hey Hello Bye Yep Mhm Mm Ha Haha Laughs Sighs Crosstalk Inaudible Muffled Chatter Sixty Seventy Eighty Fifteen Sixteen Eighteen Nineteen Eleven Thirteen Fourteen Seventeen Half Full Total Real Live Free Paid Light Heavy Hard Easy Simple Quick Slow Fast Late Early Long Short High Low Hot Cold Warm Cool Dry Wet Clean Dirty Safe Risk Issue Problem Question Answer Note Notes Call Calls Meeting Meetings Demo Demos Build Builds Scope Price Cost Rate Fee Fees Hour Hourly Yearly Weekly Daily Monthly Native Portfolio Service Sales Support Field Office Branch Site Building Property Client Clients Customer Customers Owner Owners User Users Staff Admin Manager Director Lead Leads Head Chief Senior Junior Principal Partner Partners Vendor Vendors Contractor Contractors Engineer Engineers Designer Designers Technician Technicians Dispatcher Dispatchers Analyst Coordinator Controller Superintendent Superintendents Estimator Foreman Crew Crews""".split())
per={}
for s in SC:
    t=open(os.path.join(F,s,"transcript.txt")).read()
    k=json.load(open(os.path.join(F,s,"answer-key.json")))
    kj=json.dumps(k)
    cand=collections.Counter()
    for m in re.finditer(r"\b[A-Z][a-z]{2,}\b",t):
        w=m.group(0)
        if w in STOP or w in COMMON: continue
        cand[w]+=1
    # keep tokens that also appear in the key (so they are entities the key tracks) OR appear 2+ times
    keep={w:c for w,c in cand.items() if (w in kj or c>=2)}
    per[s]=keep
print("=== CANDIDATE PERSON/ENTITY NAMES PER FIXTURE ===")
for s in SC:
    print(f"\n{s}:")
    print("   "+", ".join(f"{w}({c})" for w,c in sorted(per[s].items(), key=lambda x:-x[1])))
print("\n\n=== CROSS-CHAIN COLLISIONS ===")
inv=collections.defaultdict(set)
for s,d in per.items():
    for w in d: inv[w].add(s)
for w,ss in sorted(inv.items()):
    if len({CHAIN.get(x,x) for x in ss})>1:
        print(f"  {w:14} "+ "  ".join(f"{x.split('-')[0]}({per[x][w]})" for x in sorted(ss)))
