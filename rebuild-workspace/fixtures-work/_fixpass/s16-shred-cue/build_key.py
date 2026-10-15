#!/usr/bin/env python3
"""Fix-pass edit of fixtures/s16-shred-cue/answer-key.json. Load, change, dump (keyfmt reproduces the
file's own style). Every quote introduced here is proved verbatim at its cue before anything is written."""
import json, re, sys
sys.path.insert(0, "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_fixpass/s16-shred-cue")
import keyfmt

FIX = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s16-shred-cue"
KEY = FIX + "/answer-key.json"
raw = open(KEY, encoding="utf-8").read()
k = json.loads(raw)
assert keyfmt.dumps(k) == raw, "round trip is not byte-identical; stop"

# ---- transcript cues, for proofs -------------------------------------------------------------
cues = {}
for b in open(FIX + "/transcript.txt", encoding="utf-8").read().split("\n\n"):
    if not b.strip() or b.startswith("WEBVTT"):
        continue
    n, timing, line = b.strip().split("\n")
    label, text = line.split(": ", 1)
    cues[int(n)] = (timing.split(" --> ")[0], label, text)

def loc(a, b=None):
    start, label, _ = cues[a]
    if b is None:
        return f"cue {a}, {start}, {label}"
    for i in range(a, b + 1):
        assert cues[i][1] == label, f"run {a}-{b} crosses a label at {i}"
    return f"cues {a}-{b}, {start}, {label}"

def run_text(a, b=None):
    b = b or a
    return " ".join(cues[i][2] for i in range(a, b + 1))

proofs = []
def q(text, a, b=None):
    """Return (text, location) after proving text is verbatim in cue a (or run a-b)."""
    assert text in run_text(a, b), f"NOT VERBATIM at {a}{'-'+str(b) if b else ''}: {text!r}"
    proofs.append((text, a, b))
    return text, loc(a, b)

def prove(text, a, b=None):
    assert text in run_text(a, b), f"NOT VERBATIM at {a}{'-'+str(b) if b else ''}: {text!r}"
    proofs.append((text, a, b))
    return text

log = []
def change(where, why):
    log.append((where, why))

# ---- 1. FEEDBACK s16, change 1: the item grain is open, with a leaning ------------------------
grain = ("The item grain is open, with a leaning: the job as the parent row; signs or sign packages as child rows "
         "that each move through the six stations, the job showing a roll-up; permits as their own rows linked to the "
         "job or the building, each with its expiry and the install date it guards; a small job (one set of channel "
         "letters) stays a single row. A monday constraint to carry: all subitems of a board share one column set, so "
         "signs (stations) and permits (expiry) cannot both be subitems cleanly, and one of them likely needs its own "
         "connected board. To settle with the client: how independently signs move through the shop, and how permits "
         "map to signs, buildings and install dates.")
e210 = prove("Two hundred and some signs across four four buildings, kicks off after the first of the year, and it's forty-one permits.", 210, 211)
e109 = prove("Forty-one permits with the same install crew and the same crane,", 109)
k["expected_monday_products"][0]["why"] = (
    "Work Management for the two pieces the client ranked first: the production flow through the six stations as a "
    "status flow so the wall has a screen version in the shop, and permits with an expiry warning that moves when the "
    "install date moves. " + grain + " The evidence is the hospital contract ('" + e210 + "', cues 210-211; '" + e109 +
    "', cue 109): one job status cannot show signs of the same project in router, paint, wiring and install at once. "
    "A change request on the job is part of the build for P2 (see expected_structures.notes). Install scheduling "
    "against the one crane sits on the same boards. The estimator's spreadsheet stays where it is. So does the "
    "accounting system. Tier is never stated and there is no account, so no portfolio is assumed.")
change("expected_monday_products[0].why", "FEEDBACK s16 item 1: the grain stated as open with the leaning and its evidence; item 2: the change request named")

k["expected_questions_before_building"][9] = (
    "Is the hospital job one job with forty-one permits, four jobs by building, or two hundred sign items? The answer "
    "changes the model. Open structural question with a leaning: job as parent, signs or sign packages as child rows "
    "through the six stations with a roll-up on the job, permits as their own rows linked to the job or building with "
    "the install date each guards, small jobs a single row; subitems of one board share one column set, so signs and "
    "permits cannot both be subitems cleanly. To settle: how independently signs move through the shop, and how permits "
    "map to signs, buildings and install dates.")
change("expected_questions_before_building[9]", "FEEDBACK s16 item 1: the key's own open question gains the leaning")

v = {e["their_term"]: e for e in k["vocabulary"]}
v["permit / re-permit"]["likely_monday_object"] = (
    "own rows (a connected Permits board, or subitems if the signs are not) linked to the job or the building: office, "
    "submitted, approved, expiry, and the install date each guards; expiry against that install date drives the warning; "
    "a one-permit job may carry the columns on the job row. Shape open, see the item-grain leaning")
change("vocabulary['permit / re-permit'].likely_monday_object", "FEEDBACK item 1 and sweep pattern 1: 'columns on the job' builds one permit per job; the hospital job has forty-one")
v["the board / the wall"]["likely_monday_object"] = (
    "the station status flow shown as a full-screen view in the shop; which row carries the station status (the job, or "
    "a sign or sign package under it) is the open item-grain question with its leaning")
change("vocabulary['the board / the wall'].likely_monday_object", "FEEDBACK item 1: 'the Jobs board's status flow' builds one status per job")
v["magnet"]["likely_monday_object"] = (
    "station status on the row that moves through the shop: a sign or sign package under the job in the leaning, the "
    "job itself for a small job")
change("vocabulary['magnet'].likely_monday_object", "FEEDBACK item 1: 'status on the Jobs board' builds one status per job")

lt = k["expected_structures"]["lookalike_traps"]
lt[4] = ("Modelling the whiteboard as a plain list instead of the station status flow shown full-screen (on the job row, "
         "or on the sign rows under it, per the item-grain leaning), or building a separate 'Wall' board that duplicates the jobs.")
change("expected_structures.lookalike_traps[4]", "FEEDBACK item 1: the status flow no longer pinned to the job row")
k["expected_structures"]["portfolio_reason"] = k["expected_structures"]["portfolio_reason"].replace(
    "is the modelling question to settle first, and the answer decides whether a project layer is even wanted.",
    "is the modelling question to settle first (open, with the leaning in the readiness block: job as parent, signs or "
    "sign packages as child rows, permits as their own rows), and the answer decides whether a project layer is even wanted.")
change("expected_structures.portfolio_reason", "FEEDBACK item 1: points at the leaning")

# ---- 1b. FEEDBACK s16, change 2: the change-request element -----------------------------------
e236 = prove("She'd want to know it doesn't touch the accounting system.", 236)
e237 = prove("Which it won't, I assume.", 237)
k["expected_structures"]["notes"] = (
    "Two products, two rules. Work Management carries the production flow through the six stations, permits (office, "
    "submitted, approved, expiry) with a warning keyed to both expiry and install date, a change request on the job, "
    "install and crane scheduling, and a full-screen shop view; it is built structure, not governed by the native-board "
    "rule. " + grain + " The change request carries its source (who heard it, through which channel), what changed, the "
    "sign or signs it affects, the current approved version, and a required shop acknowledgment before the affected "
    "signs move on, with a notification to the shop when one is raised; one capture point that the three people who "
    "hear of changes can all use (a form is the natural fit), since the estimator's spreadsheet stays where it is and is "
    "where the last change got stuck; who may raise one and who approves it is open. CRM carries quotes and accounts on "
    "the native boards, detected live once an account exists and recorded per entity before the blueprint maps anything. "
    "Service and Dev are not part of this build. Constraints that survive into any shape: the floor reads and does not "
    "type. The estimator's spreadsheet is untouched on day one. The accounting system is not written to in v0.1, which "
    "rests on the client's relayed expectation of the accountant ('" + e236 + "', cue 236; '" + e237 + "', cue 237) and on "
    "nothing stronger; writeback and integration direction beyond that are unresolved and v0.1 does not depend on "
    "either; staying clear of the system is our safe default, labelled as ours. The owner sees permits and the wall first.")
change("expected_structures.notes", "FEEDBACK items 1 and 2 (grain open; change request added); 'never written to' rule applied to the accounting line")

k["expected_questions_before_building"][6] = (
    "Change orders: who may raise one, who approves it, and who must be notified in the shop and the office when one "
    "lands on a job? The build carries a change request on the job with a required shop acknowledgment; the capture "
    "point (a form the estimator, Rosamund and the lead installer can all use) is to be confirmed.")
change("expected_questions_before_building[6]", "FEEDBACK item 2: who approves added; the element named")
v["change order"]["likely_monday_object"] = (
    "change request linked to the job: source, what changed, the signs affected, the current approved version, and a "
    "shop acknowledgment status; captured by a form, with a notification to the shop; its shape (subitem or connected "
    "board) follows the item-grain decision, since subitems of one board share one column set")
change("vocabulary['change order'].likely_monday_object", "FEEDBACK item 2 and sweep pattern 2: 'subitem or update' would let a change sit in a post")

# ---- 2. direction rename ----------------------------------------------------------------------
th = k["intake"]["type_header"]
k["intake"]["type_header"] = {("direction" if kk == "direction_of_show" else kk): vv for kk, vv in th.items()}
assert "direction_of_show" not in json.dumps(k)
change("intake.type_header.direction_of_show", "renamed to direction, same position")

# ---- 3. sweep corrections not covered above ---------------------------------------------------
lt[3] = ("Treating permits as a ticket queue on a Service board because they have clocks and expiries; permits belong in "
         "Work Management beside the jobs they guard, and Service extras are out of v1. 'Permits on the job' was the "
         "Consultant's play-back (cue 271); the client agreed the order and added the install-date requirement (cues 274, "
         "276), not the shape, which stays open with its leaning.")
change("expected_structures.lookalike_traps[3]", "sweep pattern 4: 'the client asked for permits on the job' was our play-back labelled as the client's")

# ---- 4. the 'never written to' rule -------------------------------------------------------------
im = k["integrations_mentioned"]
im[0] = ("The accounting system: job number, customer and amount. The client expects it untouched ('" + e236 + "', cue 236, "
         "Rosamund relaying the accountant's condition, with '" + e237 + "' at cue 237; the accountant was not on the call); "
         "a job number is copied into monday by hand or import and nothing is written back in v0.1; writeback and "
         "integration direction beyond that are unresolved, v0.1 does not depend on either, and staying clear of the "
         "system is our safe default, labelled as ours")
change("integrations_mentioned[0]", "'never written to' rule: 'never written back' traced to cue 236 and 237 (relayed, 'I assume') and labelled; the unresolved wording added")
e256 = prove("If this needs her to stop using it on day one, she won't.", 256)
im[1] = ("The estimator's quoting spreadsheet: the day-one constraint is that Ottilie keeps using it ('" + e256 + "', cue 256); "
         "never a replacement in the first version; a one-way import is our safe default, labelled as ours, and is the key's own question")
change("integrations_mentioned[1]", "'never written to' rule: 'read-only import' labelled as our default; the client line cited")
cs = k["compliance_or_security_signals"]
cs[2] = ("The accounting system holds the job number, customer and amount; the client expects it untouched (cue 236, relayed "
         "from the accountant, with 'I assume' at cue 237); v0.1 writes nothing to it and does not depend on writing to it; "
         "'book of record' was our phrase, not the client's")
change("compliance_or_security_signals[2]", "'never written to' rule: 'book of record ... must not be written to' reworded to the client trace")

# ---- 5. s21 standing line: commitments are committed, done only on evidence ---------------------
cm = k["commitments_and_next_steps"]
cm[0]["what"] = ("Committed on the call: walkthrough of a first version (permits, the wall on a screen, quotes) with Rosamund, "
                 "Ruairi and Nkechi before the shop starts; the owner is to be brought by Rosamund and his attendance is not confirmed by him")
cm[1]["what"] = "Committed on the call: send the invite for the eighth to the three attendees; nothing is sent yet"
cm[2]["what"] = "Committed, conditional on the invite arriving: forward it to Gerrit Achterberg and frame the session for him"
cm[3]["what"] = "Committed on the call: send the permit spreadsheet with job numbers and amounts removed; not yet received"
cm[4]["what"] = "Committed on the call: send a short recap to Rosamund and Nkechi for correction; not yet sent"
change("commitments_and_next_steps[0..4].what", "s21 line: each is committed with owner, purpose and when; none recorded as done; the owner's attendance is Rosamund's intention")

# ---- 6. measured counts after the mess pass ------------------------------------------------------
tf = k["transcript_format"]
assert "about 3,173 spoken words" in tf
k["transcript_format"] = tf.replace("about 3,173 spoken words", "about 3,195 spoken words")
ef = k["intake"]["export_family"]
assert ef["words"] == 3173
ef["words"] = 3195
ef["note"] = ef["note"].replace("counting them gives 3,180 words", "counting them gives 3,202 words")
assert "3,202" in ef["note"]
ts = k["intake"]["silence"]["talk_share"]
assert ts["client_by_words"] == 0.754
ts["client_by_words"] = 0.749
change("transcript_format, intake.export_family.words and note, intake.silence.talk_share.client_by_words",
       "mess pass on five Consultant cues (52, 182, 207, 266, 280): 3,195 words, 3,202 with bracketed tokens, client share by words 0.749")

# ---- 7. the readiness block ----------------------------------------------------------------------
P = k["pains"]
ids = ["P1.1", "P1.2", "P1.3", "P2.1", "P2.2", "P2.3", "P2.4", "P3.1", "P4.1", "P5.1"]
roles = {"Rosamund Achterberg": "general manager in practice, the founder's daughter",
         "Nkechi Brandvold": "office and permits coordinator",
         "R": "shop floor lead (Ruairi, labelled R)"}
o225 = prove("For me it's the permit tells me before it expires. Not me telling myself. And the install date moving moves the permit warning with it.", 225)
o225s = prove("For me it's the permit tells me before it expires. Not me telling myself.", 225)
o222 = prove("I open something on Monday morning and I see every job, where it is on the floor, when it installs, and whether the permit's good.", 222, 223)
o227 = prove("I want the magnets to move when a change comes in without me hearing about it in the parking lot.", 227)
o224 = prove("And I don't have to walk out to the shop to find out.", 224)
outcomes = [o225, o225s, o222, o227, o227, o224, o222, None, o222, None]
sx = ["excavated"] * 7 + ["stated", "stated", "stated"]
pains = []
for pid, p, oc, s in zip(ids, P, outcomes, sx):
    prove(p["quote"], *[int(x) for x in re.match(r"cues? (\d+)(?:-(\d+))?", p["location"]).groups() if x])
    label = p["location"].split(", ")[-1]
    pains.append({"id": pid, "quote": p["quote"], "location": p["location"], "speaker_role": roles[label],
                  "stated_or_excavated": s, "outcome": oc})

def sig(text, a, pain, nc, b=None):
    t, l = q(text, a, b)
    return {"quote": t, "location": l, "pain": pain, "not_confirmed": nc}
signals = [
    sig("I want the board on a screen in the shop, big, and I want the magnets to move when a change comes in without me hearing about it in the parking lot.", 227, "P2.1",
        "our side's play-back (cues 269 to 273) carried no change element, so his tie between a change arriving and the magnets moving was never answered on the call"),
    sig("He cares that we stop paying for the same sign twice.", 230, "P2.2",
        "the owner's win is relayed by his daughter; he was not on the call and has not said it"),
    sig("Dad needs to see the crane not go out empty. That's it. He doesn't care about software.", 229, "P1.1",
        "relayed; whether the permit piece on the eighth shows him exactly that was not asked"),
    sig("It had a shop floor screen. That part was good.", 260, "P2.4",
        "whether a full-screen board view is the thing he liked in the industry package's screen; nobody asked what that screen showed"),
    sig("Which it won't, I assume. And Ottilie, because if it touches her spreadsheet she'll have opinions.", 237, "P3.1",
        "the accountant's condition is relayed with 'I assume' and the estimator's reaction is predicted; neither has been asked"),
    sig("Ask Nkechi. She'll be the one in it.", 267, "P1.2",
        "Nkechi as the account's administrator was Rosamund's answer, not Nkechi's, and nothing about seats was said"),
    sig("If the permit piece works, Dad'll sign it in a week.", 292, "P1.1",
        "a prediction about the owner; nothing from him, and 'works' was not defined"),
]

def ent(name, parent, mv, shared, stale, source, a=None, b=None):
    return {"name": name, "parent": parent, "moves_independently": mv, "shared_resource": shared, "goes_stale": stale,
            "source": source, "evidence": (loc(a, b) if a else None)}
entities = [
    ent("quote", "customer account (landlord, general contractor, tenant)", "yes", False, False, "spoken", 47),
    ent("job", "quote (a won quote)", "yes", False, False, "spoken", 53),
    ent("job number (accounting system)", "job", "no", False, False, "spoken", 57),
    ent("job folder (shared drive)", "job", "no", False, False, "spoken", 54),
    ent("drawing (shop and permit, one drawing with different stamps)", "job", "unknown", False, True, "spoken", 58),
    ent("sign or sign package", "job", "unknown", False, False, "spoken", 210, 211),
    ent("building (the hospital's four)", "job (the hospital contract)", "yes", False, False, "spoken", 212, 214),
    ent("permit", "job or building (open)", "yes", False, True, "spoken", 78),
    ent("permit office (the city, the county, two suburbs)", None, "yes", False, False, "spoken", 67),
    ent("station (router, paint, letters, wiring, crating, install)", None, "no", True, False, "spoken", 115),
    ent("the whiteboard", None, "no", False, True, "spoken", 163),
    ent("magnet (one job's marker)", "job", "yes", False, True, "spoken", 116),
    ent("Friday photo of the whiteboard", "the whiteboard", "no", False, True, "spoken", 122, 123),
    ent("install (date, crew, crane)", "job or building (open)", "yes", False, True, "spoken", 84),
    ent("install crew (three; Lyle leads)", None, "yes", True, False, "spoken", 32),
    ent("the crane (rented from one outfit)", None, "yes", True, False, "spoken", 19),
    ent("crane booking", "install", "yes", True, True, "spoken", 88),
    ent("change order (change request in the build)", "job, and the signs it affects", "yes", False, False, "spoken", 130, 131),
    ent("re-quote", "quote", "yes", False, False, "spoken", 142),
    ent("remake", "job", "yes", False, False, "spoken", 146),
    ent("backcharge", "job", "yes", False, False, "spoken", 94),
    ent("customer account (landlord, general contractor, tenant, hospital system)", None, "yes", False, False, "spoken", 39),
    ent("the permit spreadsheet", None, "no", False, True, "spoken", 75),
    ent("the quoting spreadsheet", None, "no", False, True, "spoken", 41, 43),
    ent("calendar reminders for expiry", "permit", "no", False, True, "spoken", 76, 77),
    ent("the owner (a person and an approver; no board is made from him)", None, "no", False, False, "spoken", 29),
]

def lean(question, option, pairs, condition, pattern):
    qs, ls = [], []
    for text, a, *b in pairs:
        t, l = q(text, a, b[0] if b else None)
        qs.append(t); ls.append(l)
    return {"question": question, "option": option, "quotes": qs, "locations": ls, "condition": condition, "pattern": pattern}
leanings = [
    lean("What is the item: the job, the building, the sign, or the permit? One job status cannot show signs of one project in router, paint, wiring and install at once, and one permit field cannot hold forty-one permits.",
         "Job as the parent row; signs or sign packages as child rows that each move through the six stations, with a roll-up on the job; permits as their own rows linked to the job or the building, each with its expiry and the install date it guards; a small job (one set of channel letters) stays a single row. Subitems of one board share one column set, so signs and permits cannot both be subitems cleanly; one of them, most likely permits, gets its own connected board. 'Permits on the job' was our play-back (cue 271), not the client's ask; the client agreed the order and the install-date requirement.",
         [("Two hundred and some signs across four four buildings, kicks off after the first of the year, and it's forty-one permits.", 210, 211),
          ("Forty-one permits with the same install crew and the same crane,", 109),
          ("And the hospital job is going to be two hundred signs on, what, forty permits?", 107)],
         "how independently signs move through the shop (does one job move as a block, or do its signs spread across stations), and how permits map to signs, buildings and install dates; settled with Ruairi and Nkechi before the structure is written, and reopened after the owner has seen a real build",
         "one row where the call describes many"),
    lean("Where does a change land so that the shop sees it before the router cuts?",
         "A change request linked to the job: source (who heard it, through which channel), what changed, the sign or signs affected, the current approved version, a required shop acknowledgment before the affected signs move on, and a notification to the shop when one is raised; one capture point (a form) that the estimator, Rosamund and the lead installer can all use, since the estimator's spreadsheet stays where it is and is where the last change got stuck; its shape (subitem or connected board) follows the grain decision.",
         [("Everywhere. That's the problem.", 130), ("Usually I hear about it after the router's already cut it.", 138),
          ("Ottilie knew. She'd re-quoted it. The re-quote was in her spreadsheet.", 142),
          ("I want the magnets to move when a change comes in without me hearing about it in the parking lot.", 227)],
         "who may raise a change request and who approves it, and whether the estimator will raise one from her desk when a landlord calls her; settled with Rosamund and Ottilie",
         "a pain with no element that fixes it"),
    lean("Who holds the crane, and which crew, on which day?",
         "Crane booking and crew assignment as fields on the install row (a connected bookings board only if installs are many per day): the date, the job or sign package, the crew, and whether the rental outfit has confirmed; a booked status set by us is a claim about the outfit's calendar and the outfit's confirmation is the evidence; a view of the coming weeks' bookings beside their permits shows a booking about to go out empty.",
         [("and when they're booked, we're booked.", 19), ("And the crane was booked for the Monday.", 88),
          ("We have never run a job with forty-one permits and one crane.", 215)],
         "who books the crane today (Ruairi, Lyle or Nkechi) and whether the outfit confirms in writing; and whether install scheduling is wanted in the first version at all, since the client ranked permits and the wall first",
         "a shared resource with no reservation tracking"),
    lean("Does a station need to show its queue, not only which job is in it?",
         "A per-station view of the rows sitting in it, sorted by install date, so three jobs due the same day in the paint booth are visible before the day; no capacity number is built in, because none was given.",
         [("the paint booth had three jobs queued that were all due the same day. Go on, Nkechi.", 166)],
         "whether Ruairi reads capacity per station in hours or only by eye; a capacity figure, if one exists, is a later addition",
         "a shared resource with no reservation tracking"),
    lean("Which install date does the permit warning trust, and who owns it?",
         "One install date per job (or per building) with a named owner and a last-changed stamp; the permit warning is computed from that date and the expiry and re-raises when either moves; the date on the board is a claim about what Lyle and the customer have agreed, so the field's owner is the person who hears the landlord's call.",
         [("On the board, in the install column.", 125), ("And in Lyle's head.", 126),
          ("And Nkechi has it in the permit spreadsheet, if somebody told her.", 127),
          ("And it has to know about the install date. Not just the permit date.", 276)],
         "who owns the install date (Ruairi, Lyle or Nkechi) and how far ahead of expiry the warning fires, per office",
         "an artefact that can go stale with nothing to flag it"),
    lean("What does the first version show when a row was copied from a spreadsheet that is still being kept?",
         "Every row seeded from Nkechi's permit spreadsheet or imported from the quoting spreadsheet carries its source and import date, so a copy that drifted from the sheet is visible as a copy; Nkechi's sheet retires when she enters permits in monday, at the November cut-over at latest; the quoting spreadsheet does not retire in the first version.",
         [("I can send you the permit spreadsheet. With the job numbers. I can take the amounts off.", 288),
          ("And Ottilie's spreadsheet. If this needs her to stop using it on day one, she won't.", 256)],
         "the date Nkechi stops keeping her spreadsheet, and whether a one-way import of quotes is acceptable or quotes are keyed twice",
         "an artefact that can go stale with nothing to flag it"),
    lean("Does a Quotes board fix unchased quotes, or is it a second list of them?",
         "Quotes on the native Deals/Opportunities board relabelled Quotes, with an owner, a last-contact date and a next-chase date, which is what the spreadsheet lacks; until quotes reach it by a feed or Ottilie keys them, it is a second list, so the element is honest only once the import question is answered; third in the client's order and not on the eighth.",
         [("And then it sits. Nobody chases it unless the customer calls back.", 47),
          ("Ottilie's got, I don't know, sixty open quotes at any one time, and she's out doing surveys three days a week.", 48)],
         "a one-way import from the quoting spreadsheet accepted by Ottilie, or a decision that she keys quotes once they go out, and which fields",
         "a pain with no element that fixes it"),
    lean("Who moves the station status when the person who walks the floor is out?",
         "The station status stays set by a person after the six-thirty walk, as the magnet is today, which the floor-does-not-type constraint forces; a named deputy for the walk, and a view of rows whose status has not changed in a working day, so a board nobody walked is visible as such; a crew lead moving one row from a phone is a tap, not typing, and is a question rather than a plan.",
         [("And when Ruairi's out, nobody walks the board.", 163), ("They'll look at a phone. They won't type into one.", 253)],
         "whether a station lead will tap a status on the shop tablet or a phone, and who walks the floor when Ruairi is out",
         "a pain with no element that fixes it"),
]

epp = [
    ("P1.1", "permit rows with expiry and the install date each guards; a warning keyed to both", "fixes"),
    ("P1.2", "permit rows visible to Rosamund and Ruairi, and the warning sent to more than one person (recipients open)", "fixes"),
    ("P1.3", "permit rows per office linked to the building and its install date; a view of the forty-one against one crane", "fixes"),
    ("P2.1", "change request with a shop notification and a required acknowledgment before the affected signs move on", "fixes"),
    ("P2.2", "the same change request, raised by the estimator from a form while her spreadsheet stays; depends on her raising it (assumption)", "fixes"),
    ("P2.3", "the station status on a screen and in the office; still set by one person after a walk, so a screen version of the wall with the same single-person dependency; the deputy and the stale-status view are a leaning", "copies-today's-tool"),
    ("P2.4", "the live board view in the office replaces the Friday photo", "fixes"),
    ("P3.1", "Quotes on the native Deals/Opportunities board with a next-chase date; a second list of quotes until the import question is answered", "copies-today's-tool"),
    ("P4.1", "one install date field with an owner, read by the permit warning and the crane booking; Lyle's head is outside any board until he owns the field", "fixes"),
    ("P5.1", "none: no board changes whom the landlord calls; the owner's two wins are served through P1 and P2, and the escalation habit stays in the record as internal", "none"),
]
assert [e[0] for e in epp] == ids

structure = {
    "products": ["Work Management", "CRM"],
    "build_target": "own-account",
    "build_target_reason": "prospect, so the user's own account by default (A21)",
    "workspaces": ["Tallgrass – Ops", "Tallgrass – CRM"],
    "native_reuse": "CRM Deals/Opportunities relabelled Quotes; Accounts for landlords, general contractors, tenants and the hospital system; Contacts only if named people are to be tracked; detected in the user's own account before quotes are mapped. The Work Management boards (jobs, signs, permits, installs, change requests) are built structure.",
    "leanings": leanings,
    "patterns": ["parent-row-with-roll-up: job with signs or sign packages as child rows through the six stations, the furthest-back station and the install date rolled up on the job; permits as their own rows linked to the job or building, the nearest expiry against its install date rolled up on the job"],
    "element_per_pain": [{"pain": a, "element": b, "verdict": c} for a, b, c in epp],
}

def inc(system, authority, a=None, b=None):
    return {"system": system, "authority": authority, "evidence": loc(a, b) if a else None}
existing = {
    "account": "unknown, no account bound: the client has no monday account ('Any monday in the building today?' 'No.', cues 262-263; 'That's the extent of it.', cue 265) and the tier is never stated; under A21 the proof of concept goes into the user's own account, read at preflight, and the client's eventual account, its administrator (Nkechi is the client's own answer) and its seats are a handover question",
    "incumbents": [
        inc("the accounting system", "stays system of record for: job number, customer, amount; follower for: nothing (a job number is copied into monday by hand or import); writeback and integration direction unresolved beyond the client's relayed expectation that it is not touched; v0.1 does not depend on either; staying clear of it is our safe default, labelled as ours", 236),
        inc("the estimator's quoting spreadsheet", "stays system of record for: quotes and re-quotes in the first version; follower for: nothing until a one-way import is agreed; the Quotes board follows it, never the reverse", 256),
        inc("the permit spreadsheet", "system of record for: permits today, and the seed for the first version with amounts removed; follower for: everything once Nkechi enters permits in monday, at the November cut-over at latest, and retired then", 288),
        inc("the city and county permit portals", "stay system of record for: a permit's submitted, approved and expiry dates; the board's dates are keyed by Nkechi from them and are her claim, the portal is the evidence; no integration asked for or promised", 103),
        inc("the shared drive job folders", "stay system of record for: drawings, documents and the Friday photo; follower for: nothing; a link from the job row at most", 57),
        inc("the whiteboard", "stays the production record in the shop until the owner trusts the screen; the board on the screen runs beside it through the transition, not instead of it", 254),
        inc("calendar reminders", "today's expiry mechanism; replaced by the permit warning once Nkechi trusts it; not an integration", 76, 77),
        inc("the crane rental outfit's calendar", "system of record for: crane availability; follower for: nothing; a booked status in monday is a claim about it until the outfit confirms", 19),
    ],
}
prove("Any monday in the building today?", 262); prove("No.", 263); prove("That's the extent of it.", 265)

assumptions = [
    ("Signs of one job spread across stations, so a sign or sign package is the row that moves; a small job is one row.", "Ruairi: when the hospital runs, will one building's signs be in router, paint and wiring at the same time, or does a job move as a block?"),
    ("A sign package (one building's set, or one sign type) is the workable child row for the hospital; two hundred rows per job is too many to move by hand.", "Ruairi: what do you move as a unit on the wall, a sign or a batch?"),
    ("Permits get their own connected board and signs are subitems of the job, because subitems of one board share one column set.", "Nkechi and Ruairi: does a permit belong to a building, a sign set or the whole job?"),
    ("The six stations are the complete, ordered list and every product passes through all of them.", "Ruairi: is router, paint, letters, wiring, crating, install complete and in order, and does vinyl or vehicle work skip stations?"),
    ("The permit warning fires a fixed number of days before expiry, measured against the install date, and goes to Nkechi and Rosamund.", "Nkechi: how far ahead, per office, and who should see it?"),
    ("The permit offices are the city, the county and two suburbs, each with one clock and one expiry period.", "Nkechi: which offices, with what clock and expiry period each?"),
    ("Ruairi owns the install date in the first version and Lyle tells him when it moves.", "Ruairi and Lyle: who owns the install date, and who hears first when the landlord moves it?"),
    ("A change request may be raised by Ottilie, Rosamund or Lyle through one form, and Rosamund approves it.", "Rosamund: who may raise a change request and who approves it?"),
    ("The three people who hear of changes will use the form; the estimator raising one from her desk is the weak link.", "Ottilie: when a landlord calls you with a change, will you file it before you re-quote?"),
    ("Crane bookings are a date and a confirmed flag on the install; the rental outfit is not in monday.", "Ruairi or Lyle: who books the crane, and how does the outfit confirm?"),
    ("Quotes reach the Quotes board by a one-way import of customer, amount, date sent and last contact; Ottilie keys nothing twice.", "Ottilie: is a one-way import of those fields acceptable, and which fields does it leave out?"),
    ("Landlords, general contractors, tenants and the hospital system are tracked as accounts with a type column; named contacts are not tracked in the first version.", "Rosamund: are the named people at landlords and general contractors to be tracked?"),
    ("The first version seeds permits from Nkechi's spreadsheet (job numbers and dates, amounts removed) and invents sample data for everything else.", "Nkechi: what may the spreadsheet seed, and what must stay out?"),
    ("Rosamund reads the board from the office; the shop reads a full-screen view; nobody on the floor types.", "Ruairi: what must be readable from the floor, and is a read-only full-screen view enough?"),
    ("The owner attends the eighth at seven-thirty.", "Rosamund: has he said yes?"),
    ("The user's own account is the build target; the client's eventual account, tier and seats are a handover question (A21).", "At handover: which account, who administers it, which products and seats?"),
]
unmet = [
    ("A number for what chased quotes would win (the win rate and the value)", None, "it sits with the estimator, who was not on the call and wants a week with her spreadsheet; the build does not produce it"),
    ("The actual remake and backcharge figures", "before the eighth, if Nkechi pulls them", "they live in the accounting system and in the owner's arguments with landlords; nothing in the build reads them"),
    ("Quotes visible without anyone keying them twice", None, "v0.1 has no feed from the quoting spreadsheet; a one-way import is a question, and until it is answered the Quotes board is a second list"),
    ("A permit's status from the portal without Nkechi checking it by hand", "November, when the first building's permits go in", "no portal integration was asked for or exists; the board's dates are her claim and the portal is the evidence"),
    ("Crane availability from the rental outfit's own calendar", "the hospital installs, after the first of the year", "the outfit is outside; a booking in monday is a claim about their calendar until they confirm"),
    ("The wall staying up until the owner trusts the screen", "spring, when he wants to be out of the day-to-day", "a transition need, not a board element: the screen and the wall run side by side, and the build cannot make him trust it; the walkthrough on the eighth is where it starts"),
    ("Shop-floor status moves without typing", "January, the shop side", "the floor will look at a phone and not type; a tap on a status is unprobed, so in the first version one person's walk sets every status"),
    ("What remakes look like once the hospital job runs or the founder steps back", "after the first of the year", "nobody asked and nobody said; a question for the eighth, not a build element"),
]
ai = [
    ("P2.1", "workflow", 2, "P-21", "When a change request is raised, notify the shop and hold the affected sign rows until a shop acknowledgment is recorded."),
    ("P1.1", "workflow", 2, "P-21", "When an install date or a permit expiry changes, recompute the permit warning and notify the permit owner and the general manager."),
    ("P2.2", "ai_column", 2, "unprobed", "Summarise the pasted note or email on a change request into what changed and which signs it touches, for the shop to confirm."),
    ("P1.3", "agent", 2, "unprobed", "Each morning, list the permits whose install date now sits within a set number of days of expiry across the hospital's four buildings, with the office and the crane booking beside each."),
    ("P3.1", "sequence", 2, "unprobed", "A chase sequence on open quotes by days since sent, once quotes are on the Quotes board; nothing is sent until the estimator agrees."),
]
verdict = {
    "cleared_for": "build",
    "conditions": [
        "approval stop",
        "no A11 question first matters for an own-account build (A21: sample data in the user's own account); the three A11 decisions stay open",
        "the item grain confirmed with Ruairi and Nkechi before the structure is written, or built on the leaning with the assumption shown on the approval card",
        "the owner's attendance on the eighth is Rosamund's intention, not his confirmation",
        "the invite and the recap are committed, not sent; the permit spreadsheet is committed, not received",
        "native CRM boards detected in the user's own account before quotes are mapped; quotes trail the eighth",
        "nothing is written to the accounting system, the quoting spreadsheet or the permit portals",
    ],
    "reason": "Two pains drawn out on the call with named entities and wanted outcomes in the client's words, two products chosen, the structure stated with its leanings and the build target named; the open grain is a leaning with its condition, not a gap.",
}
prove("Dad needs to see the crane not go out empty.", 229)
questions = [
    {"text": "The hospital job: two hundred and some signs, four buildings, forty-one permits. When it runs, will one building's signs be in router, paint and wiring at the same time, and does each permit belong to a building, a sign set or the whole job? The first version leans to the job as the parent row, signs or sign packages as rows under it through the six stations, and permits as their own rows linked to the job or building with the install date each guards; small jobs stay one row.",
     "kind": "discovery", "role": "Ruairi and Nkechi, with Rosamund",
     "known": "the counts (cues 107 to 110, 210 to 215); the six stations in order (cue 115); two city and two county buildings with engineering on every exterior sign (cues 212 to 214); permits in November for the first building (cue 242)"},
    {"text": "Ruairi said: 'I want the magnets to move when a change comes in without me hearing about it in the parking lot.' Nothing in our play-back answered that. The first version carries a change request on the job that notifies the shop and holds the affected signs until the shop acknowledges it, raised through one form. Is that what moves the magnets, and who may raise one and who approves it?",
     "kind": "read-back", "role": "Ruairi, then Rosamund and Ottilie",
     "known": "changes arrive through Ottilie, a note to Rosamund or Lyle on site (cues 131 to 133); today's catch is Ruairi at Ottilie's desk on Fridays (cue 158); the last miss was a re-quote in her spreadsheet (cue 142); the spreadsheet stays on day one (cue 256)"},
    {"text": "Rosamund said: 'Dad needs to see the crane not go out empty.' and 'He cares that we stop paying for the same sign twice.' On the eighth the permit piece shows a permit expiring against a moved install date before the crane is booked, and the change request shows a change reaching the shop before the router cuts. Is that his test, and has he said he will be there at seven-thirty?",
     "kind": "read-back", "role": "Rosamund, and the owner on the eighth",
     "known": "both wins are relayed by his daughter (cues 229 to 230); he signs anything over ten thousand or any new system after seeing it work (cues 233 to 235); seven-thirty on Thursday the eighth is Rosamund's proposal (cues 283 to 284) and the invite is committed, not sent (cue 285)"},
    {"text": "Who owns the install date, and who books the crane? The permit warning and the crane booking both read from one install date; today it lives on the board, in Lyle's head and in the permit spreadsheet if somebody told Nkechi.",
     "kind": "discovery", "role": "Ruairi and Lyle, with Nkechi",
     "known": "the three places (cues 125 to 128); the crane is rented from one outfit and when they are booked the company is booked (cues 17 to 19); the landlord moved the medical office install (cue 84)"},
    {"text": "Which permit offices, with what clock and expiry period each; how far ahead of expiry should the warning fire, measured against the install date; and who should get it?",
     "kind": "discovery", "role": "Nkechi",
     "known": "city three to six weeks with no notice of completion (cue 71); county ten days (cue 66); two suburbs need a hearing over forty square feet (cue 67); expiry ninety or a hundred and eighty days by city (cue 78); Nkechi's own outcome words (cue 225); the install-date requirement confirmed by our side (cues 276 to 277)"},
]
assert len(questions) <= 5

k["readiness"] = {
    "schema": "readiness/1",
    "note": "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top).",
    "pains": pains,
    "signals": signals,
    "entities": entities,
    "structure": structure,
    "existing": existing,
    "assumptions": [{"statement": s, "question": qq} for s, qq in assumptions],
    "unmet_needs": [{"need": n, "clock": c, "why_not_met": w} for n, c, w in unmet],
    "ai_opportunities": [{"pain_or_need": p, "kind": kd, "round": r, "probe_basis": pb, "idea": i} for p, kd, r, pb, i in ai],
    "verdict": verdict,
    "questions": questions,
}
change("readiness", "added as the last top-level field in the brief's shape")

# ---- checks ---------------------------------------------------------------------------------------
keys = list(k.keys())
assert keys[-2:] == ["intake", "readiness"] and len(keys) == 27, keys
assert [p["id"] for p in k["readiness"]["pains"]] == ids
assert all(e["moves_independently"] in ("yes", "no", "unknown") for e in entities)
assert all(x["verdict"] in ("fixes", "copies-today's-tool", "none") for x in structure["element_per_pain"])
block = json.dumps(k["readiness"], ensure_ascii=False)
bad = []
for pat in [r"\bR\d{1,2}\b", r"Discovery complete", r"Nearly ready", r"Not ready", r"\bgates?\b", r"met-with-residual",
            r"not-obtainable", r"\bpartial\b", r"\bbleed\b", r"\bupside\b", r"\btrajectory\b", r"\bgrade", r"\bmissing\b",
            r"\brubric\b", r"\bgap question"]:
    for m in re.finditer(pat, block, flags=re.I):
        bad.append((pat, block[max(0, m.start()-40):m.end()+40]))
if bad:
    for b_ in bad: print("SALES WORD:", b_)
    sys.exit("sales vocabulary in the block")

out = keyfmt.dumps(k)
assert json.loads(out) == k
open(KEY, "w", encoding="utf-8").write(out)
print("written:", len(out.splitlines()), "lines; proofs:", len(proofs))
print("counts: pains", len(pains), "signals", len(signals), "entities", len(entities), "with parent",
      sum(1 for e in entities if e["parent"]), "leanings", len(leanings), "epp", len(epp), "incumbents",
      len(existing["incumbents"]), "assumptions", len(assumptions), "unmet", len(unmet), "ai", len(ai), "questions", len(questions))
print("\nCHANGE LOG")
for w, y in log:
    print("-", w, "::", y)
