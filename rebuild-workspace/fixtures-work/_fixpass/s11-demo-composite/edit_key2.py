import sys, re; sys.path.insert(0,'.')
import keyfmt
K='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s11-demo-composite/answer-key.json'
k=keyfmt.load(K)
tr=k['traps']
i=[n for n,t in enumerate(tr) if t.startswith("Talk share by label (client 18.4%)")][0]
tr[i]=tr[i].replace("(client 18.4%)","(client 18.3%)").replace("10.0% of the words","9.7% of the words")

HS="Hattie Szabo (Sales Manager)"; AV="Anjali Venkataraman (General Manager)"; DF="Desmond Farrow (Warehouse and Dispatch Manager)"
def seg(n): return "28:05 block, segment %d, a participant on the client side (speaker not resolvable)"%n
SR="a participant on the client side (speaker not resolvable)"
P=k['pains']
Q=lambda n:P[n]['quote']; L=lambda n:P[n]['location']
out_white="Yes. Yes, that's the thing. The whiteboard goes."
out_p2="So Hattie would see the chairs are gone before she quotes them."
out_p4="So the shortage goes to Hattie the same day. Not three weeks later when Bram does the invoices."
out_p3phone="The truck one. If it's on the phone. I keep saying that."
pains=[
 {"id":"P1","quote":Q(0),"location":L(0),"speaker_role":"Sales Manager","stated_or_excavated":"stated","outcome":None},
 {"id":"P2","quote":Q(1),"location":L(1),"speaker_role":"Sales Manager","stated_or_excavated":"stated","outcome":out_p2},
 {"id":"P3.1","quote":Q(2),"location":L(2),"speaker_role":SR,"stated_or_excavated":"stated","outcome":out_white},
 {"id":"P3.2","quote":Q(3),"location":L(3),"speaker_role":SR,"stated_or_excavated":"stated","outcome":out_white},
 {"id":"P3.3","quote":Q(4),"location":L(4),"speaker_role":SR,"stated_or_excavated":"stated","outcome":out_white},
 {"id":"P3.4","quote":Q(5),"location":L(5),"speaker_role":"Warehouse and Dispatch Manager","stated_or_excavated":"stated","outcome":out_p3phone},
 {"id":"P4.1","quote":Q(6),"location":L(6),"speaker_role":"Sales Manager","stated_or_excavated":"excavated","outcome":out_p4},
 {"id":"P4.2","quote":Q(7),"location":L(7),"speaker_role":"Warehouse and Dispatch Manager","stated_or_excavated":"excavated","outcome":out_p4},
 {"id":"P5","quote":Q(8),"location":L(8),"speaker_role":"Sales Manager","stated_or_excavated":"stated","outcome":None},
]
signals=[
 {"quote":"So Hattie would see the chairs are gone before she quotes them.","location":"22:46 "+AV,"pain":"P2","not_confirmed":"that the committed column solves the double-quoting; the next sentence from our side was 'It can also show you the trucks the same way'"},
 {"quote":"I don't want a warning. I want to know which wedding the tent's already on. The tent and the floor. Not the chairs.","location":"25:55 "+HS,"pain":"P2","not_confirmed":"whether a count on the date answers 'which wedding'; our reply at 26:03 restated the item list and did not answer the question"},
 {"quote":"That view, though. The red. That's the Saturday.","location":seg(5),"pain":"P3.3","not_confirmed":"whose words these are; our side said 'that's the Saturday in June' at 34:24, but the tie sits inside the composite block and the speaker is not resolvable"},
 {"quote":"If it's on my phone and it's on Ferenc's phone, yes.","location":seg(8),"pain":"P3.4","not_confirmed":"the speaker, and the condition itself: no phone has been put in anyone's hand"},
 {"quote":"The truck one. If it's on the phone. I keep saying that.","location":"47:24 "+DF,"pain":"P3.4","not_confirmed":"that the crew board on a phone is what he would use on a Saturday; the phone test is promised for the yard and has not happened"},
 {"quote":"That's the chairs that come back with cigarette burns and nobody bills for them.","location":"41:57 "+HS,"pain":"P4.1","not_confirmed":"that the same-day notification gets those chairs billed; the next sentence from our side was 'And it can also hold the photo'"},
 {"quote":"So the shortage goes to Hattie the same day. Not three weeks later when Bram does the invoices.","location":"44:26 "+DF,"pain":"P4.2","not_confirmed":"that same-day to the sales manager is the outcome both of them want; the next sentence from our side was 'It can also go to Bram at the same time'"},
 {"quote":"Gerald walked past it in August and said it's the reason we can't take the Larchmere contract, and he's not wrong, we can't run fourteen weekends of a convention venue off a whiteboard and a spreadsheet that Tanvi updates on her phone in the car park.","location":seg(7),"pain":"P3.1","not_confirmed":"the speaker, the owner's own view and the size of the contract; the only attributed clock is 'Before March.' at 51:23"},
]
def ent(name,parent,mi,sh,st,src,ev): return {"name":name,"parent":parent,"moves_independently":mi,"shared_resource":sh,"goes_stale":st,"source":src,"evidence":ev}
entities=[
 ent("Quote","Client","yes",False,False,"spoken","16:50 "+HS),
 ent("Quote line (item, quantity, unit price, line total)","Quote","no",False,False,"spoken","16:30 "+HS),
 ent("Client (a private client, a company or a venue)",None,"yes",False,False,"spoken","54:24 "+HS),
 ent("Venue (a type of client that sends work without paying)","Client","yes",False,False,"spoken","54:24 "+HS),
 ent("Venue coordinator","Venue","yes",False,True,"spoken","56:00 "+HS),
 ent("Event (date, venue, windows, status)","Quote","yes",False,False,"spoken","00:52 "+AV),
 ent("Movement (a delivery or a pickup; the client's word is open)","Event","yes",False,False,"spoken",seg(3)),
 ent("Delivery or pickup window","Movement","yes",False,False,"spoken",seg(3)),
 ent("Truck (one to four; a fifth hired on a June Saturday, side-only)",None,"yes",True,False,"spoken","37:02 "+DF),
 ent("Crew lead",None,"yes",True,False,"spoken","17:33 "+HS),
 ent("Crew lead's unavailable day","Crew lead","yes",False,False,"spoken",seg(3)),
 ent("Person-and-truck constraint (a crew lead who does not drive one truck)","Crew lead","unknown",False,False,"spoken",seg(3)),
 ent("Item type (chairs, tables, the ten-by-twenty, dance floor sections, lighting)",None,"yes",True,False,"spoken","25:23 "+HS),
 ent("Physical unit of a scarce item (each of the two ten-by-twenty tents; each dance floor section)","Item type","yes",True,False,"spoken","25:55 "+HS),
 ent("Owned quantity per item type","Item type","no",False,True,"assumed",None),
 ent("Committed count per item type per date (derived)","Item type","no",False,True,"assumed",None),
 ent("Pick list print (paper on the truck)","Event","no",False,True,"spoken",seg(5)),
 ent("Count-in (per returned event)","Event","yes",False,False,"spoken","41:57 "+HS),
 ent("Count-in line (out, back, outcome, note, photo)","Count-in","yes",False,False,"spoken","41:57 "+HS),
 ent("Shortage or damage charge","Count-in line","yes",False,True,"spoken","44:26 "+DF),
 ent("Invoice (in the accounting system, the bookkeeper's)","Client","yes",False,False,"spoken","44:26 "+DF),
 ent("The whiteboard (the Thursday board; today's dispatch plan)",None,"no",False,True,"spoken","51:23 "+AV),
 ent("Photo of the whiteboard texted to crew leads","The whiteboard (the Thursday board; today's dispatch plan)","no",False,True,"spoken",seg(3)),
 ent("Events spreadsheet (the sales administrator's)",None,"no",False,True,"spoken",seg(3)),
 ent("Paper count sheet","Count-in","no",False,True,"spoken","41:57 "+HS),
 ent("Weekend view (a page read from the boards for the Thursday meeting)",None,"no",False,False,"assumed",None),
]
def lean(q,o,qs,ls,c,p): return {"question":q,"option":o,"quotes":qs,"locations":ls,"condition":c,"pattern":p}
P1="one row where the call describes many"; P2="a pain with no element that fixes it"; P4="our framing labelled as the client's"; P5="a shared resource with no reservation tracking"; P6="an artefact that can go stale with nothing to flag it"
leanings=[
 lean("Is the ten-by-twenty one Items row with an owned quantity of two, or two rows, one per physical tent?",
      "One parent row per scarce item type with one child row per physical unit (tent one, tent two; each dance floor section), the committed count rolling up to the type and each unit showing the event it is on; chairs stay a quantity on one row.",
      ["It's not the chairs, mostly. We have chairs. It's the ten-by-twenty tent. There are two of them.","I want to know which wedding the tent's already on. The tent and the floor. Not the chairs."],
      ["25:23 "+HS,"25:55 "+HS],
      "Whether the client tells the two tents apart in practice (a number, a name, the patched panel) and whether the dance floor is hired by the section; Hattie and Desmond by name on the 8th, before the committed column is finished.",P1),
 lean("Does the committed count look at the event date, or at each line's out-and-back window?",
      "Each event line on a scarce item carries an out date and a back date, defaulting to the delivery and pickup windows with the tent's turnaround added; the committed count per date reads those windows, not the event date. Chairs stay on the event date.",
      ["check the tent's not on two of them, because there's two tents and everyone wants the big one"],[seg(3)],
      "Desmond by name: whether a tent really goes up the day before and comes down the day after, which decides whether the window is a rule per item or an entry per event; until then the turnaround stays half built, as the Consultant said.",P5),
 lean("Is the event's status one hand-set value, or does it roll up from the movements and the count-in?",
      "Movements carry their own status (planned, on the road, done, flipped by the crew lead) and the count-in its own; the event's status is derived from them, so one event row never carries one value for two trucks on two days. The Consultant's six labels are read back and the derived ones replace Picked, Delivered and Collected. A movement status flipped by a crew lead is a claim about where the truck is, never evidence from the truck.",
      ["Group it by truck. Not by crew lead. The truck is the thing that can't be in two places. Ferenc can drive two trucks in one day. Truck three can't be at two weddings."],["37:02 "+DF],
      "The client's own words for an event's states (the key's eleventh pre-build question); until then the labels are ours.",P1),
 lean("Are trucks a fixed set of four groups, or rows that can be added when a fifth is hired?",
      "A short Trucks list (truck one to four, plus a hired truck for a date range) as the group source of the Crew schedule, so a hired truck can be booked for a Saturday in June and a person-and-truck constraint can live on the truck; the look-alike trap against a Trucks board of work stands, because a list of four rows is not a board of work.",
      ["There are four trucks and on a Saturday in June I need five.","Ade doesn't drive truck three because of the clutch."],[seg(5),seg(3)],
      "Desmond by name: how often a fifth truck is hired and whether the clutch rule is permanent; both are side-only today. If neither matters, four groups suffice and the list is not built.",P5),
 lean("When the event changes after a pick list or the board has been printed, what tells the truck its paper is stale?",
      "A printed-at stamp on every print and a 'changed since print' flag on the event and the movement, set by any dated change after the stamp; the crew lead's phone notification is the primary channel and paper is a backup the client chooses.",
      ["because I'd moved him on the Thursday and the printout in truck three still had him on both, and nobody caught it until the golf club rang at half eleven asking where their tent was.","Can it text the crew leads when a quote's accepted? Because Ferenc doesn't read email. None of them read email."],
      [seg(5),"17:33 "+HS],
      "Whether paper stays at all ('that's your call, not mine'): Hattie and Desmond on the 8th with a phone in hand; and whether a text can be sent on this plan, which is an unverified claim.",P6),
 lean("Who keeps the owned quantity honest, and what flags it when nobody has?",
      "The owned number carries a kept-by and an as-of date; a Damaged line marked written off at count-in proposes a decrement for the warehouse manager to accept; a committed count whose owned number is older than the last count-in shows as unverified. The staleness itself is the Consultant's own admission at 19:11 ('if nobody changes it the committed column is quietly wrong'), not a client statement.",
      ["We had eight from one wedding in August and I found the count sheet in the door pocket of truck two a fortnight later, after the client had paid."],["41:57 "+HS],
      "Desmond by name: whether he will own the number after each count-in, which the Consultant proposed and the client has not agreed; if not, the committed column is advisory and says so on the board.",P6),
 lean("Which status words are the client's?",
      "Quote stages are the client's (draft, sent, sent back, accepted, dead; dead is not lost). 'Shortage' is the client's. 'Short', 'damaged', 'count-in', 'movement' and the six event labels are the Consultant's and are read back with their slots before v0.2. 'The Thursday board' is heard only inside the composite block and is confirmed by name before it names a board; 'the whiteboard' is attributed.",
      ["The statuses. We don't say negotiation. A quote is draft, sent, sent back if they want changes, accepted, or dead. And dead is not the same as lost, sometimes the event just doesn't happen.","So the shortage goes to Hattie the same day. Not three weeks later when Bram does the invoices."],
      ["16:50 "+HS,"44:26 "+DF],
      "The read-back on the 8th; the vocabulary entries and the leak list's caution line were corrected in this pass so a builder reading them alone does not take the Consultant's labels for the client's.",P4),
 lean("What, if anything, is built for venue coordinators (P5)?",
      "Nothing in v0.2; a question. If built later: contacts on the native Contacts board attached to the venue account, shown on the event with the phone number for the crew lead; the first job is getting them out of two phones and a notebook.",
      ["Can it do the venue's contact? The coordinator at the venue? Because half my week is finding out who the coordinator is this time.","Tanvi's phone. And mine. And a notebook."],
      ["54:24 "+HS,"56:00 "+HS],
      "Hattie by name: how many venues, how the coordinators are kept today, and whether the crew lead needs the number on the truck.",P2),
 lean("Does the Events board replace the sales administrator's spreadsheet, or does the spreadsheet hold events that never come through a quote?",
      "The Events board is fed by accepted quotes only; an event that does not start as a quote (a repeat booking, a venue's standing order) has no row until the spreadsheet has been read. Leaning: ask before assuming the spreadsheet is empty of them; the key's earlier 'replaced by the Events board' was our framing and now says so.",
      ["Um. Okay. So Thursday, I get in at six, and the first thing I do is print the week's events off Hattie's spreadsheet, the one Tanvi keeps, because the spreadsheet is the only place the events are."],[seg(3)],
      "The sales administrator, who was not in the room, through Hattie: what the spreadsheet holds that a quote does not; and the speaker of the block line, who is not resolvable.",P4),
]
patterns=[
 "parent-row-with-roll-up: quote with quote lines as child rows, the value on the parent; the same lines carried to the event as its pick list",
 "parent-row-with-roll-up: event with movements as child rows, the event status derived on the parent (leaning 3)",
 "parent-row-with-roll-up: scarce item type with one child row per physical unit, the committed count on the parent (leaning 1)",
 "parent-row-with-roll-up: count-in with one line per item, the event's Counted in state on the parent",
]
def epp(p,e,v): return {"pain":p,"element":e,"verdict":v}
element_per_pain=[
 epp("P1","Quote lines as child rows of the quote, carried to the event as the pick list without re-typing; changes after acceptance dated and visible to the warehouse","fixes"),
 epp("P2","Items with an owned quantity and the committed column on the two tents and the dance floor sections first, shown on the quote line as it is typed, amber rather than blocked; which tent is on which event waits on leaning 1","fixes"),
 epp("P3.1","Crew schedule board of movements grouped by truck (the v0.2 regroup), the workload view by truck going red on a double booking, the venue change made once on the event and carried to every movement, crew leads notified on their phone","fixes"),
 epp("P3.2","The same board: movements appear from the accepted quote with date and venue filled, Unassigned until the Thursday planning, so the plan is filled in rather than redrawn; the four hours are side-only and are re-asked before any saving is claimed","fixes"),
 epp("P3.3","The workload view by truck and the overlapping-window rule, red before the crew leads arrive; a movement status set by a crew lead is a claim about the truck, not evidence from it","fixes"),
 epp("P3.4","Regroup by truck with the crew lead as a column, trucks the default workload axis, people the second view; committed for v0.2, not yet done","fixes"),
 epp("P4.1","Count-in lines with an outcome per line, a photo and a note, a same-day notification to the sales manager by name, an open-charges view oldest first; the charge still reaches the invoice by hand, and a tick on it is a person's claim that the bookkeeper billed it","fixes"),
 epp("P4.2","The same notification, to the sales manager only at first; the bookkeeper reads a list rather than a second notification","fixes"),
 epp("P5","Nothing in v0.2; a question for the 8th (leaning 8). A pain with no element, kept visible","none"),
]
existing={"account":"unknown, no account bound: the client has none ('you don't have an account yet', 03:12); v0.1 lives in the Consultant's demo account as the workspace 'Quillhaven v0.1' with six boards, two automatic notifications and one dashboard, to be rebuilt rather than copied; under A21 the proof of concept goes into the user's own account, whose native CRM boards are read at preflight, and the key's question about which account the build lives in moves to handover",
 "incumbents":[
  {"system":"The accounting system (the bookkeeper's invoices)","authority":"stays system of record for: invoices, payments and a charge once billed; follower for: nothing in v0.1. Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours. A tick on an open charge is a person's claim that the bookkeeper billed it, never evidence from the accounting system.","evidence":"44:26 "+DF},
  {"system":"The sales administrator's events spreadsheet","authority":"stays system of record for: every event, until the Events board is live and the spreadsheet has been read for events that never start as a quote (leaning 9); follower for: nothing","evidence":seg(3)},
  {"system":"The whiteboard by the dispatch door","authority":"stays system of record for: the Thursday plan until the crew board is adopted on a phone; the client's stated outcome is that it goes","evidence":"51:23 "+AV},
  {"system":"Paper count sheets on the trucks","authority":"stays the record of what came back until the count-in is done at the dock; whether it stays as a backup is the client's call","evidence":"41:57 "+HS},
  {"system":"Two phones and a notebook (venue coordinators)","authority":"stays system of record for: venue coordinators; nothing in v0.2 reads or replaces it","evidence":"56:00 "+HS},
  {"system":"The old rental software's handheld scanner","authority":"unknown: what it talks to is answered by Friday; until then the count-in is a person typing","evidence":"37:56 "+DF},
  {"system":"Phones and text messages to crew leads","authority":"stays the channel for the board photo today (side-only); the mobile notification is the planned channel; a text on acceptance is an unverified claim","evidence":"17:33 "+HS},
 ]}
def asm(s,q): return {"statement":s,"question":q}
assumptions=[
 asm("The Thursday walk-through inside the 28:05 block is the warehouse manager's.","Desmond, by name: is it yours, and are four hours a Thursday, three redos this week, four trucks and sixteen magnets right?"),
 asm("The two ten-by-twenty tents are told apart in practice.","How do you tell them apart, and is one always 'the big one'?"),
 asm("A tent goes up the day before the event and comes down the day after.","What is the real turnaround per scarce item?"),
 asm("The events spreadsheet holds nothing that does not start as a quote.","Tanvi, through Hattie: what is in the spreadsheet that a quote does not carry?"),
 asm("Crew leads do the count-in at the dock on a phone, not on the truck.","Dock or truck, and whose phone?"),
 asm("The six event labels and the count-in labels can stand until read back.","Which of these words are yours, and which slots are wrong?"),
 asm("The warehouse manager keeps the owned quantity after each count-in.","Will you own that number, and after which event does it change?"),
 asm("A fifth truck in June is hired, not owned, and is rare.","How often, and does it need a row of its own?"),
 asm("Each crew lead gets a login, rather than one phone per truck.","Anjali's decision: how many people, each needing what?"),
 asm("The bookkeeper reads a list of charges and the accounting system is untouched by v0.1.","Does Bram want a view or a list, and what does the accounting system talk to?"),
 asm("The Larchmere Hall contract is fourteen weekends of a convention venue from March.","Anjali, by name: what is the contract, and what did Gerald say about the whiteboard?"),
 asm("Sample data in the user's own account carries invented names and no name from this call.","For the user: which sample values, and may the real crew lead's name stay out of them?"),
 asm("A venue sits on the event as a type of client and never pays, so no Venues board.","Does a venue ever pay you directly?"),
 asm("A crew lead needs one truck for one day and nothing else on the phone.","Does a crew lead ever need another truck's plan or the whole weekend?"),
]
def need(n,c,w): return {"need":n,"clock":c,"why_not_met":w}
unmet_needs=[
 need("Text messages to crew leads when a quote is accepted","before the 8th, to answer; crew leads do not read email (17:33)","plan-dependent and unverified; v0.2 has the mobile notification; the claim is checked before it is promised"),
 need("The count-in reading the old rental software's handheld scanner","Friday of the call's week","unknown what the scanner talks to; until answered the count-in is a person typing a number"),
 need("The crew board usable on a Saturday on phones with cracked screens and no weekend data","crew learn it in January; nothing live in October; before March","the mobile app needs data; the client will pay for phones if it works; offline use is unprobed and the phone test at the yard has not happened"),
 need("The red workload grid for the dispatch manager on his phone in the car park","a Thursday","the grid is a desktop view; the phone gets a list of movements; a tablet or the office screen is the honest answer today"),
 need("A person-and-truck rule (a crew lead who does not drive one truck) as a rule rather than a note","none given","side-only inside the block; the Consultant declined to fake it with a note; leaning 4 decides where it would live once confirmed"),
 need("Venue coordinators (P5)","none given; 'half my week' (54:24)","a question, not a build, by agreement on the call; the data lives in two phones and a notebook"),
]
def ai(p,kind,r,b,idea): return {"pain_or_need":p,"kind":kind,"round":r,"probe_basis":b,"idea":idea}
ai_opportunities=[
 ai("P4.1","ai_column",2,"unprobed","An AI column on the count-in line drafts the charge note (item, count, suggested amount from the replacement cost, the photo's date) for the sales manager to accept or change before she raises it."),
 ai("P3.3","workflow",2,"P-21","A workflow that, when a movement goes red, notifies the crew lead on that movement and proposes the free truck for the window, with the dispatch manager's yes before anything moves."),
 ai("P3.2","agent",2,"P-19","An agent that reads the Crew schedule and the Events board on a Thursday morning and sends the dispatch manager a short read-out of unassigned movements, conflicts and tight windows for Friday to Monday, reading and writing only this client's workspaces."),
]
verdict={"cleared_for":"build","conditions":[
 "approval stop",
 "no A11 question first matters for an own-account build (A21: sample data in the user's own account needs no decision); the three A11 decisions stay open",
 "the v0.2 change list goes in first: by truck, the five quote stages, the committed column on the two tents and the dance floor sections, the money widget off, revenue hidden from every crew-lead view",
 "leanings 1 to 9 stay open structural questions and none is settled by the build; leaning 1 decides the Items shape before the committed column is finished",
 "the two notifications are approved as one automation list, with the caveat that automations created through the API cannot be switched off through it",
 "nothing tier-dependent is built, because the tier is unknown; the structure assertions stay provisional until the user has seen a real build (FEEDBACK, top)",
 "the next showing at the yard on the 8th with the owner present is committed, not held; the invite is committed, not evidenced as received"],
 "reason":"Four pains with named entities and wanted outcomes in the client's words, two products chosen, the structure stated with nine leanings and the build target named; the thin spots are the block's unresolved speaker and the open shape of the scarce items, and both travel as questions and assumptions rather than as evidence."}
def q(t,kind,role,known): return {"text":t,"kind":kind,"role":role,"known":known}
questions=[
 q("Desmond, the transcript has a Thursday under Anjali's name: in at six, the spreadsheet, sixteen magnets, the crew leads at seven, four hours, three redos this week, and the June Saturday with the golf club. Is that yours, word for word? And with the board grouped by truck, is this the Thursday board, and does that June Saturday go red on it?","read-back","Warehouse and Dispatch Manager","All of it sits inside the 28:05 block and cannot be attributed; 'by truck' (37:02) and 'if it's on the phone' (47:24) are his and attributed; the regroup is a committed v0.2 change; the phone test is promised for the yard."),
 q("Hattie, you said it is the ten-by-twenty, there are two of them, and the dance floor sections, and that you want to know which wedding the tent is already on, not a warning. Does a count on the date answer that, or do you need the two tents as two rows, each showing the event it is on?","read-back","Sales Manager","25:23 and 25:55 are attributed; our reply at 26:03 restated the item list and did not answer 'which wedding'; Anjali's tie at 22:46 was answered with 'It can also'; leaning 1 and assumption 2."),
 q("Hattie, you said the cigarette-burn chairs never get billed because the sheet turns up in a door pocket after the client has paid, and Desmond said the shortage should reach Hattie the same day. Does a line that notifies Hattie by name the same day, with the photo, get those chairs billed? And are 'short' and 'damaged' your words, or is it 'shortage' and something else?","read-back","Sales Manager; Warehouse and Dispatch Manager","41:57 and 44:26 are attributed and both were answered with 'it can also'; 'shortage' is the client's word, 'short' and 'damaged' the Consultant's; the bookkeeper still invoices in the accounting system, which v0.1 does not touch."),
 q("Anjali, with Desmond: how many crew leads are there, does each need a login or does one phone live in each truck, and on a Saturday with no data what must already be on the phone before the truck leaves the yard? And Desmond: how often is a fifth truck hired in June, and is 'Ade doesn't drive truck three' permanent?","discovery","General Manager (decision); Warehouse and Dispatch Manager","'We'll pay for phones if it works' (19:05); the seat shape is the Consultant's to bring as people and needs, not money; half the crew's phones have cracked screens and no weekend data (18:06); the fifth truck and the clutch rule are side-only inside the block."),
 q("Anjali, you said before March, Larchmere Hall starts in March and Gerald has said the whiteboard has to be gone. The transcript also carries, under your name, fourteen weekends of a convention venue and Gerald walking past the board in August. Is that right, and what did Gerald actually say?","read-back","General Manager","51:23 is attributed and is the clock; the scale and the August remark are side-only inside the block and relayed from the absent owner; the owner has seen nothing and will only meet at the yard (52:38, 53:20)."),
]
k['readiness']={
 "schema":"readiness/1",
 "note":"Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top).",
 "pains":pains,"signals":signals,"entities":entities,
 "structure":{"products":["CRM","Work Management"],"build_target":"own-account","build_target_reason":"prospect, so the user's own account by default (A21)",
   "workspaces":["Quillhaven – CRM","Quillhaven – Ops"],
   "native_reuse":"Deals/Opportunities relabelled Quotes with the five client stages; Accounts relabelled Clients with a type column for venues; Contacts for venue coordinators only once Hattie's question is answered. Events, Crew schedule, Items, Count-in and the Weekend view are Work Management boards built new in the Ops workspace; nothing is copied from the v0.1 demo account.",
   "leanings":leanings,"patterns":patterns,"element_per_pain":element_per_pain},
 "existing":existing,"assumptions":assumptions,"unmet_needs":unmet_needs,"ai_opportunities":ai_opportunities,"verdict":verdict,"questions":questions}
keyfmt.save(k,K)

# ---- self-checks
import json
blob=json.dumps(k['readiness'],ensure_ascii=False)
bad=re.findall(r"\b(R\d{1,2}|met-with-residual|Nearly ready|Not ready|partial|Partial|missing|Missing|gate|gates|grade|graded|Met)\b",blob)
print("sales words in block:",sorted(set(bad)))
ids=[p['id'] for p in pains]; print("pain ids",ids,"element rows",[e['pain'] for e in element_per_pain]==ids)
print("entities with parent all carry moves_independently:",all(e['moves_independently'] in ('yes','no','unknown') for e in entities if e['parent']))
print("questions",len(questions),"leanings",len(leanings),"entities",len(entities),"signals",len(signals),"assumptions",len(assumptions),"unmet",len(unmet_needs),"ai",len(ai_opportunities),"incumbents",len(existing['incumbents']))
# outcome strings verbatim at a transcript unit
import re as _re
T=open('/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s11-demo-composite/transcript.txt').read()
for p in pains:
    if p['outcome']: assert p['outcome'] in T, p['outcome']
print("outcomes verbatim: ok; field order:",list(k.keys())[-3:])
