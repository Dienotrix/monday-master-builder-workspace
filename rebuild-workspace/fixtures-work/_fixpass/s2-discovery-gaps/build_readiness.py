#!/usr/bin/env python3
"""Fix-pass edit script for fixtures/s2-discovery-gaps/answer-key.json (2026-10-13).

Loads the key, applies the field corrections of the sweep and the standing lines,
adds the readiness block as the 26th and last field, proves every quote the block
carries verbatim at its cited transcript line, and dumps the key with the file's own
indentation. Refuses to write if any proof fails or if the untouched round trip is not
byte-identical. Standard library only.
"""
import json
import re
import sys

FIX = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s2-discovery-gaps"
KEY = FIX + "/answer-key.json"
TX = FIX + "/transcript.txt"

raw = open(KEY, "rb").read()
key = json.load(open(KEY, encoding="utf-8"))
assert (json.dumps(key, indent=2, ensure_ascii=False) + "\n").encode() == raw, "round trip differs"
assert "readiness" not in key, "already has readiness"
assert list(key.keys())[-1] == "expected_leak_blocklist"

lines = open(TX, encoding="utf-8").read().split("\n")


def unit(loc):
    m = re.match(r"L(\d+), (\w+)$", loc)
    assert m, loc
    n, name = int(m.group(1)), m.group(2)
    text = lines[n - 1]
    assert text.startswith(name + ": "), (loc, text[:40])
    return text


PROOFS = []


def q(quote, loc):
    """Return quote after proving it verbatim at loc."""
    text = unit(loc)
    assert quote in text, ("MISS", quote, loc)
    PROOFS.append((quote, loc))
    return quote


# ---------------------------------------------------------------------------
# 1. Field corrections (sweep hits that a builder reading the field alone would build)
# ---------------------------------------------------------------------------
voc = {v["their_term"]: v for v in key["vocabulary"]}

assert voc["routes"]["likely_monday_object"] == "group"
voc["routes"]["likely_monday_object"] = (
    "undecided: a group per technician only if daily routes are mirrored from the system; "
    "if monday tracks exceptions only, a route is not a monday object (readiness leaning 2; "
    "the group-per-tech shape was the consultant's pitch, not the client's ask)"
)

assert voc["route sheets"]["likely_monday_object"] == "view"
voc["route sheets"]["likely_monday_object"] = (
    "not a monday object while the system prints them; a view only if routes are mirrored "
    "(readiness leaning 2; Travis asked whether they would still print from the system and got no answer)"
)

assert voc["the system"]["likely_monday_object"] == "integration (external system of record)"
voc["the system"]["likely_monday_object"] = (
    "external system of record; writeback and integration direction unresolved; v0.1 does not "
    "depend on either; staying clear of the system is our safe default, labelled as ours"
)

assert voc["rounds"]["likely_monday_object"] == "column"
voc["rounds"]["likely_monday_object"] = (
    "child rows under the plan, one per round with its window and status, with the rounds behind "
    "rolled up on the plan (readiness leaning 1); not one column carrying one value for six or seven rounds"
)

assert voc["the board"]["likely_monday_object"] == "not a monday object (maps to a dispatch board or view)"
voc["the board"]["likely_monday_object"] = (
    "not a monday object; whether an exceptions board or a full routes board stands beside it is open "
    "(readiness leaning 2)"
)

assert voc["application record"]["likely_monday_object"] == "column (or kept only in the system)"
voc["application record"]["likely_monday_object"] = (
    "kept in the system (Travis: 'it has to be in the system, though'); no monday column holds the record "
    "itself in v0.1; at most a checkbox that Rhonda has keyed it, which is a person's claim, not the record"
)

old = "lawn plans and rounds with a timeline view and dependencies for the rain pushes"
new = (
    "lawn plans with their rounds as child rows so a rain push shows which rounds are behind (the "
    "timeline view and dependencies at L237 were the consultant's suggestion, answered with 'Oh. Okay. Huh.'; "
    "see readiness leaning 1)"
)
w = key["expected_monday_products"][0]["why"]
assert w.count(old) == 1
key["expected_monday_products"][0]["why"] = w.replace(old, new)
q("Oh. Okay. Huh.", "L239, Travis")
q("it has to be in the system, though", "L193, Travis")

# ---------------------------------------------------------------------------
# 2. The readiness block
# ---------------------------------------------------------------------------
CSL = "customer service lead, main branch (client; influencer)"
DSP = "dispatcher, main branch (client; end user)"

OUT_R = q("I just want to be able to look it up. Like, where's that re-treat at. Without walking back to Travis every time.", "L309, Renata")
OUT_T = q("if a guy calls out, I just want to push it to the guys and be done. Not chase everybody down.", "L317, Travis")
OUT_L = q("that's supposed to come to us as a lead, so we can call them.", "L205, Renata")

# pains: the key's 15 entries in array order, theme number first, running number after the dot
ids = ["P1.1", "P1.2", "P1.3", "P1.4", "P2.1", "P2.2", "P3.1", "P3.2", "P3.3", "P3.4", "P4.1", "P4.2", "P5.1", "P6.1", "P7.1"]
outcomes = {
    "P1.1": OUT_R, "P1.2": OUT_R, "P1.3": OUT_R, "P1.4": OUT_R,
    "P2.1": OUT_T, "P2.2": OUT_T,
    "P3.1": None, "P3.2": None, "P3.3": OUT_R, "P3.4": None,
    "P4.1": None, "P4.2": None,
    "P5.1": OUT_L, "P6.1": None, "P7.1": None,
}
pains = []
for pid, p in zip(ids, key["pains"]):
    assert p["theme"].startswith(pid.split(".")[0] + " "), (pid, p["theme"])
    q(p["quote"], p["location"])
    pains.append({
        "id": pid,
        "quote": p["quote"],
        "location": p["location"],
        "speaker_role": CSL if p["location"].endswith("Renata") else DSP,
        "stated_or_excavated": "stated",
        "outcome": outcomes[pid],
    })

signals = [
    {"quote": q("It's more that, um --", "L123, Renata"), "location": "L123, Renata", "pain": "P1.1",
     "not_confirmed": "why the callback sheet falls short in her own words; she was cut off by the consultant's 'a spreadsheet can only take you so far' and answered only 'Yeah, I mean, sure.'"},
    {"quote": q("Yeah. That'd be nice.", "L119, Renata"), "location": "L119, Renata", "pain": "P1.1",
     "not_confirmed": "which part of the pitched shape (a status, a ping to dispatch after a day, a dashboard) she was agreeing to; nobody asked"},
    {"quote": q("It's just, if I'm --", "L159, Travis"), "location": "L159, Travis", "pain": "P2.1",
     "not_confirmed": "what the whiteboard fails at when he is the one missing; cut off by the consultant and never picked up"},
    {"quote": q("Would we still be printing the route sheets from the system, or...?", "L291, Travis"), "location": "L291, Travis", "pain": "P2.2",
     "not_confirmed": "whether he wants the printed route sheets to stay; the consultant answered 'We can figure that part out' and moved on"},
    {"quote": q("The system will show you who's overdue, but it's not great.", "L235, Travis"), "location": "L235, Travis", "pain": "P3.2",
     "not_confirmed": "what the system's overdue view lacks; a rounds board that copies it badly would be the same tool again"},
    {"quote": q("Oh. Okay. Huh.", "L239, Travis"), "location": "L239, Travis", "pain": "P3.1",
     "not_confirmed": "whether a timeline with dependencies matches how rounds move after rain; a noncommittal sound after the consultant's pitch, not a yes"},
    {"quote": q("My leads are better about it. They'll actually text me.", "L215, Travis"), "location": "L215, Travis", "pain": "P5.1",
     "not_confirmed": "that lead technicians already relay add-on requests by text, which may be the capture point; never explored"},
    {"quote": q("everything's in five places, and it's kind of gotten worse, I don't know.", "L277, Renata"), "location": "L277, Renata", "pain": "P7.1",
     "not_confirmed": "what got worse and since when; the consultant accepted 'more organized' and did not ask"},
]


def ent(name, parent, moves, shared, stale, source, evidence):
    if evidence:
        unit(evidence)
    return {"name": name, "parent": parent, "moves_independently": moves, "shared_resource": shared,
            "goes_stale": stale, "source": source, "evidence": evidence}


entities = [
    ent("customer", None, "yes", False, False, "spoken", "L75, Renata"),
    ent("service address with access notes (gate code, dog notes, lockbox code)", "customer", "no", False, False, "spoken", "L189, Travis"),
    ent("plan (quarterly pest plan or lawn plan)", "customer", "yes", False, False, "spoken", "L63, Renata"),
    ent("round (one lawn application, six or seven per plan, each due in a window)", "plan (quarterly pest plan or lawn plan)", "yes", False, True, "spoken", "L231, Travis"),
    ent("skip (a service the customer asks to skip; may become a cancel)", "plan (quarterly pest plan or lawn plan)", "yes", False, True, "spoken", "L249, Renata"),
    ent("cancellation", "plan (quarterly pest plan or lawn plan)", "yes", False, False, "spoken", "L249, Renata"),
    ent("one-time service with a thirty-day re-treat window", "customer", "yes", False, False, "spoken", "L103, Renata"),
    ent("service ticket (one scheduled visit, created in the system)", "plan (quarterly pest plan or lawn plan)", "yes", False, False, "spoken", "L67, Renata"),
    ent("application record (product, amount, target pest, signature; state-audited, in the system)", "service ticket (one scheduled visit, created in the system)", "no", False, False, "spoken", "L189, Travis"),
    ent("call-in or callback (re-treat, billing question, wants a call)", "customer", "yes", False, True, "spoken", "L99, Renata"),
    ent("re-treat visit (a truck going back out, free under a plan or within thirty days)", "call-in or callback (re-treat, billing question, wants a call)", "yes", False, False, "spoken", "L101, Travis"),
    ent("callback sheet (Google Sheet)", None, "yes", False, True, "spoken", "L83, Renata"),
    ent("dispatch whiteboard (a row per technician, a magnet per stop; wiped on a rain day)", None, "yes", False, True, "spoken", "L89, Travis"),
    ent("route (one technician's stops for one day, generated nightly by the system)", "technician (about sixty, more in summer; some on paper)", "yes", False, True, "spoken", "L147, Travis"),
    ent("printed route sheet", "route (one technician's stops for one day, generated nightly by the system)", "no", False, True, "spoken", "L147, Travis"),
    ent("stop (one visit on one route; moves between technicians by hand)", "route (one technician's stops for one day, generated nightly by the system)", "yes", False, False, "spoken", "L151, Travis"),
    ent("technician (about sixty, more in summer; some on paper)", "branch (main branch on Tolliver Road; North)", "yes", True, False, "spoken", "L329, Travis"),
    ent("lead technician ('My leads')", "branch (main branch on Tolliver Road; North)", "unknown", False, False, "assumed", None),
    ent("truck", "branch (main branch on Tolliver Road; North)", "yes", True, False, "spoken", "L151, Travis"),
    ent("rain day", None, "yes", False, False, "spoken", "L111, Renata"),
    ent("notify-list obligation (call before spraying, and again after every push)", "customer", "yes", False, True, "spoken", "L245, Renata"),
    ent("complaint (phones, office inbox, website, reviews, the owner's cell)", "customer", "yes", False, False, "spoken", "L253, Renata"),
    ent("complaint folder in the customer service lead's email", None, "no", False, True, "spoken", "L261, Renata"),
    ent("add-on request written on a paper ticket (mosquito, termite inspection)", "service ticket (one scheduled visit, created in the system)", "yes", False, True, "spoken", "L205, Renata"),
    ent("invoice (QuickBooks; hand-off from the system unclear)", "customer", "yes", False, False, "spoken", "L295, Renata"),
    ent("branch (main branch on Tolliver Road; North)", None, "yes", False, False, "spoken", "L43, Travis"),
    ent("North branch spreadsheet (contents unknown)", "branch (main branch on Tolliver Road; North)", "unknown", False, True, "spoken", "L141, Renata"),
    ent("CSR team (four, one part-time; North has its own)", "branch (main branch on Tolliver Road; North)", "no", False, False, "spoken", "L41, Renata"),
]

L = []  # leanings


def lean(question, option, quotes, locations, condition, pattern):
    for qq, ll in zip(quotes, locations):
        q(qq, ll)
    L.append({"question": question, "option": option, "quotes": quotes, "locations": locations,
              "condition": condition, "pattern": pattern})


lean(
    "Is a lawn plan one row with a current-round column, or a parent with its rounds as child rows?",
    "parent-row-with-roll-up: the plan as parent, one child row per round with its window, its status and the date it was pushed to, the count of rounds behind rolled up on the plan; a skip is a status on the round it skips, so two skips in a row are visible before billing",
    ["So a lawn plan is, like, six rounds a year? Seven if they've got the grub control.",
     "And then if it rains, like, three, four days, everybody's pushed.",
     "sometimes the skip turns into a cancel and nobody really catches it until, like, billing."],
    ["L231, Travis", "L231, Travis", "L249, Renata"],
    "the plan structure is confirmed (how many rounds, what each window is) and it is known whether the system can export plans and overdue rounds or every round row is typed by hand",
    "one row where the call describes many",
)
lean(
    "Does monday mirror the system's daily routes, or track only the exceptions dispatch makes to them?",
    "exceptions only in v0.1: a board of today's changes (call-out, truck down, re-treat slotted in, same-day urgent job, rain push) with the stop, the technician it moves to and the date, so a technician's changed stops reach his phone without a text; the system keeps generating and printing routes; the group-per-technician routes board was the consultant's pitch, and Travis's answer was that the board works",
    ["honestly the board works. It works. Everybody gets their stops.",
     "Would we still be printing the route sheets from the system, or...?",
     "And half of them don't read the texts, so then I'm calling them."],
    ["L159, Travis", "L291, Travis", "L151, Travis"],
    "what the system can export and whether Travis wants the printed sheets to stay; a nightly route import would turn this into a mirror, which v0.1 does not have",
    "our framing labelled as the client's",
)
lean(
    "Is a repeat call about the same problem one ticket or three?",
    "one Tickets item per problem, with each call logged on it and the count of calls and the age shown, so the third call about the same spiders lands on the row the first one made",
    ["Last week I had a lady over on Pheasant Run call three times.",
     "And I go look, and it's on the sheet from the first call. It just never went anywhere."],
    ["L111, Renata", "L111, Renata"],
    "how CSRs handle a repeat call on the sheet today, a new row or the old one; the committed copy of the callback sheet will show it",
    "one row where the call describes many",
)
lean(
    "Which fields must a call-in carry before dispatch can act, and where does the plan come from?",
    "the callback sheet's own columns on the native Tickets item (customer, address, what is going on, plan or one-time, last technician) plus the last service date, with plan and last service date required at intake; days since last service is a formula on the item for the thirty-day decision; the plan and the date are typed by the CSR from the system and carry an as-of date, because they change when a visit happens and nothing refreshes them",
    ["sometimes a CSR puts it on the sheet but she doesn't put the plan, so Travis doesn't know if it's a re-treat or if we're charging for it, so it sits.",
     "If it was a one-time, you get thirty days. So if it's, like, day thirty-four, that's a whole conversation."],
    ["L111, Renata", "L103, Renata"],
    "whether the system can export the plan and the last service date, or the CSR keeps typing them; until then the days-since figure is as current as the typed date",
    "an artefact that can go stale with nothing to flag it",
)
lean(
    "What flags a re-treat that was on the whiteboard before a rain day wiped it?",
    "the Tickets item keeps its own status (new, scheduled, done) apart from the whiteboard; a view of scheduled-not-done re-treats older than a day is what dispatch rebuilds the board from after rain; a scheduled or done status set by dispatch or a technician is a claim about a visit the system records, never evidence from the system",
    ["there's a rain day and the whole board gets wiped and redone, and that one just doesn't make it back up."],
    ["L111, Renata"],
    "dispatch marks the ticket scheduled when the magnet goes up; if that step is skipped the view is as blind as the sheet",
    "an artefact that can go stale with nothing to flag it",
)
lean(
    "Which element shortens the two-hour morning rebuild (P2.1)?",
    "none: the causes (a call-out, a truck down, re-treats to slot in, a same-day urgent job) are outside any board, and the system's routes are rebuilt by hand either way; the exceptions board of leaning 2 changes how the result reaches technicians (P2.2), not the rebuild itself, and a routes board in monday would be the whiteboard on a screen",
    ["I'm in at six. I'm usually still redoing routes at eight, eight-fifteen? So call it two hours. Every morning. Saturdays too, in the season.",
     "It's just, if I'm --"],
    ["L155, Travis", "L159, Travis"],
    "Travis finishes his sentence: what the rebuild fails at, and what happens on a morning he is out",
    "a pain with no element that fixes it",
)
lean(
    "How does a reassigned stop show who holds it, so nothing is promised to two technicians?",
    "every exception row names the stop, the technician it leaves, the technician it goes to and the date; a per-technician view of today's changes is the reservation; the whiteboard is that reservation today (a row per technician, a magnet per stop) and only the people in the room can see it",
    ["Big whiteboard. Every tech's got a row, every stop's a magnet.",
     "So I'm moving magnets around on the board, and then I'm texting the guys their changes."],
    ["L89, Travis", "L151, Travis"],
    "whether a stop can be moved in monday without also being moved in the system (which prints the sheets); if not, the row records a move made elsewhere",
    "a shared resource with no reservation tracking",
)
lean(
    "Is the rounds board a shared backlog or the system's overdue view typed again by hand?",
    "the rounds board (leaning 1) is the shared view CSRs read for where a customer's round is, which the system's view does not give them; while round dates are typed by Travis after each push it copies the system's overdue list with his knowledge added, and is as current as he keeps it",
    ["And I kind of know who's behind, but it's -- it's in my head. The system will show you who's overdue, but it's not great.",
     "And then customers call going, where's my guy, and I don't know where their guy is."],
    ["L235, Travis", "L241, Renata"],
    "what the system's overdue view lacks, and whether overdue rounds can be exported from it; with a feed the board is a fix, without one it is a copy that Travis maintains",
    "a pain with no element that fixes it",
)
lean(
    "Which element reaches complaints that arrive by email, website, reviews and the owner's cell (P4.1)?",
    "none in v0.1: email-to-ticket is a deferred Service extra, a review site and a personal phone are not channels, and the owner was not on the call; each complaint is keyed onto Tickets by the customer service lead with its channel as a label, which replaces her email folder (P4.2) and leaves the arrival as it is",
    ["Everywhere. The phones, the office inbox, the website.",
     "So now he forwards me everything, screenshots, voicemails, and I've got a folder in my email, and I try to keep track, like, did we call them back, did we send somebody."],
    ["L253, Renata", "L261, Renata"],
    "how the owner wants what reaches his cell to reach the team, asked of him; and whether the office inbox could later be a Service channel",
    "a pain with no element that fixes it",
)
lean(
    "Does North get a copy of the same setup, a branch column in one build, or nothing yet (P7.1)?",
    "nothing for North in v0.1 and a branch column on every board so nothing has to be rebuilt if it joins; the copy-to-North idea was the consultant's and Renata said it is a Gary question; nothing in this build changes how North works",
    ["It's a different everything up there. Which, I mean, Lorna's great. It's just, when I cover for them, I don't know where anything is.",
     "If it's going to North. I don't know if it's going to North. That's kind of a Gary question."],
    ["L143, Travis", "L305, Renata"],
    "the owner says whether North is in scope; if it is, the North CSR's spreadsheet is read before any board is copied",
    "a pain with no element that fixes it",
)

epp = [
    ("P1.1", "a call-in is one native Tickets item with a status (new, scheduled, done) and an age, in place of a row on the sheet that nothing watches; a view of items sitting in new past a day", "fixes"),
    ("P1.2", "one ticket per problem with each call logged on it (leaning 3), so a third call lands on the first call's row", "fixes"),
    ("P1.3", "plan or one-time, last technician and last service date required at intake, with days since last service as a formula (leaning 4)", "fixes"),
    ("P1.4", "the ticket's own status survives a rain-day wipe; a view of scheduled-not-done re-treats is what the board is rebuilt from (leaning 5)", "fixes"),
    ("P2.1", "no element shortens the rebuild; the exceptions board moves the result, not the work (leaning 6)", "none"),
    ("P2.2", "an exceptions board with the stop, the technician and the date, and a mobile notification to the technician it goes to; a printed sheet stays for those who want paper (leaning 2)", "fixes"),
    ("P3.1", "the plan as parent with rounds as child rows and a rounds-behind view (leaning 1); typed by hand after each push until the system can feed it, so in v0.1 it is the system's overdue list again with Travis's knowledge added (leaning 8)", "copies-today's-tool"),
    ("P3.2", "the same rounds board as the written form of what is in his head; it is only as current as he keeps it, and the system already shows who is overdue (leaning 8)", "copies-today's-tool"),
    ("P3.3", "the rounds board is readable by CSRs, so where a customer's round stands is looked up, not walked back for; depends on the board being maintained (leaning 8)", "fixes"),
    ("P3.4", "a notify-list flag on the customer row and a call-before-spray task created whenever a round's date changes, with its own done status; that status is a CSR's claim that the call was made", "fixes"),
    ("P4.1", "no element: the channels (email, website, reviews, the owner's cell) stay as they are; email-to-ticket is a deferred extra and a personal phone is not connected (leaning 9)", "none"),
    ("P4.2", "each complaint as a Tickets item with a complaint label, a channel, and a follow-up status (called back, visit sent), replacing the email folder (leaning 9)", "fixes"),
    ("P5.1", "an add-on request item on a Work Management board, created by the technician from his phone or by Rhonda while re-keying the paper ticket, with a CSR owner and a called status; a simple board, not a CRM pipeline", "fixes"),
    ("P6.1", "a skip as a status on the round it skips (leaning 1), with a view of plans carrying two skips in a row so the cancel is seen before billing; works only if the CSR keys the skip in monday when the customer calls", "fixes"),
    ("P7.1", "no element: a branch column keeps the door open; nothing is built for North until the owner decides (leaning 10)", "none"),
]
assert [e[0] for e in epp] == ids

structure = {
    "products": ["Work Management", "Service"],
    "build_target": "own-account",
    "build_target_reason": "prospect, so the user's own account by default (A21)",
    "workspaces": ["Quillmoor – Ops", "Quillmoor – Service"],
    "native_reuse": "Service: the native Tickets board for call-ins (re-treats, callbacks, billing questions, complaints) distinguished by a request-type label, found by detection in the user's own account and recorded by id; the Service companions (Contacts, CSAT, the IT boards) are not used; no CRM entity: customers stay in the system and the CRM pitch was deflected ('That's more Gary's side.')",
    "leanings": L,
    "patterns": [
        "parent-row-with-roll-up: lawn plan with rounds as child rows, rounds behind and consecutive skips on the parent",
        "parent-row-with-roll-up: call-in ticket with each call about the same problem logged on it, call count and age on the parent",
    ],
    "element_per_pain": [{"pain": a, "element": b, "verdict": c} for a, b, c in epp],
}
q("That's more Gary's side.", "L213, Renata")

existing = {
    "account": "unknown, no account bound. The client has no monday account, workspace or board ('No. I've seen the ads.', L55, Renata), so there is nothing to audit or extend on their side and no tier is known. Under A21 the build target is the user's own account, whose tier and native Service boards are read at preflight; the client's own account, and whether the owner's daughter used monday somewhere, are handover questions, not build questions.",
    "incumbents": [
        {"system": "the system (legacy pest and lawn software, name unknown)",
         "authority": "stays system of record for: customers, plans, service tickets (visits), nightly routes, state application records; follower for: nothing in v0.1; writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the system is our safe default, labelled as ours",
         "evidence": "L75, Renata"},
        {"system": "QuickBooks",
         "authority": "stays system of record for: invoices; how it is fed from the system is unknown ('I think the system sends it over?'); follower for: nothing",
         "evidence": "L295, Renata"},
        {"system": "the callback sheet (Google Sheet)",
         "authority": "stays system of record for: nothing once call-ins are on Tickets; its columns are the Tickets columns; follower for: nothing; the committed copy is read before the columns are final",
         "evidence": "L83, Renata"},
        {"system": "the dispatch whiteboard",
         "authority": "stays system of record for: who goes where today, in the room; follower for: the exceptions board records the moves made on it, and does not replace it in v0.1",
         "evidence": "L89, Travis"},
        {"system": "printed route sheets and paper service tickets",
         "authority": "stays system of record for: the technician's day and the application record until Rhonda keys it; follower for: nothing; the paper stays for those who want it",
         "evidence": "L189, Travis"},
        {"system": "the customer service lead's email folder and the owner's cell",
         "authority": "stays system of record for: nothing once complaints are keyed onto Tickets; the owner's cell stays a channel until he says how it should reach the team",
         "evidence": "L261, Renata"},
        {"system": "the North branch spreadsheet",
         "authority": "stays system of record for: North's call-ins; follower for: nothing; untouched until the owner puts North in scope",
         "evidence": "L141, Renata"},
        {"system": "texts and calls to technicians",
         "authority": "stays system of record for: nothing; the exceptions board's notifications replace them for technicians on the app, and texts remain for the rest",
         "evidence": "L151, Travis"},
    ],
}
q("No. I've seen the ads.", "L55, Renata")
q("I think the system sends it over?", "L295, Renata")

assumptions = [
    {"statement": "A lawn plan has six rounds, seven with grub control, each with a named window; the sample plans are built that way.",
     "question": "How many rounds does each lawn plan type have, and what is each round's window?"},
    {"statement": "The system cannot feed monday in v0.1: plans, rounds, last service dates and routes are typed or imported once as sample data, each with an as-of date.",
     "question": "What can the system export, how often, and who can run the export?"},
    {"statement": "Monday tracks dispatch exceptions only; the system keeps generating and printing the daily routes.",
     "question": "Do you want the printed route sheets to stay, and should monday ever hold a full day's routes?"},
    {"statement": "A repeat call about the same problem goes on the ticket the first call made.",
     "question": "On the callback sheet today, is a repeat call a new row or a note on the old one?"},
    {"statement": "The CSR keys a skip in monday when the customer calls, as well as wherever it is recorded for the system.",
     "question": "Where is a skip recorded today, and who removes the skipped service from the route?"},
    {"statement": "Rhonda's re-keying of paper tickets is where an add-on request is captured, until technicians use the app.",
     "question": "Would Rhonda enter the add-on note while keying the ticket, or do lead technicians already pass them on by text?"},
    {"statement": "Technicians on the app get their changed stops as notifications; technicians on paper keep getting a text, and a 'texted' status on the exception row records it.",
     "question": "Who would use monday day to day: office staff only, lead technicians, or all technicians?"},
    {"statement": "One truck per technician; a truck down is recorded as an exception on that technician's stops.",
     "question": "Is a truck tied to one technician, and what happens to his stops when it is down?"},
    {"statement": "North is out of the first version; a branch column exists on every board so nothing is rebuilt if it joins.",
     "question": "Is the North branch in scope for this, and who decides?"},
    {"statement": "Re-treat volume for sample data is fifteen to twenty a week at the main branch, about double in summer.",
     "question": "How many re-treat calls come in a week, in season and out, and how many of them stall?"},
    {"statement": "The plan and the last service date on a ticket are typed by the CSR from the system at intake.",
     "question": "Can a CSR see the plan and the last service date in the system while on the call?"},
    {"statement": "Complaints are keyed onto Tickets by the customer service lead from what the owner forwards; the channels stay as they are.",
     "question": "How should what reaches the owner's cell and the office inbox reach the team?"},
    {"statement": "The notify-list flag lives on the customer row and a call-before-spray task is created on every date change; the medical reason is not stored.",
     "question": "What must be recorded about a notify-list customer, and who may see it?"},
    {"statement": "Access notes (gate code, lockbox code, dog notes) stay on the paper ticket and in the system; the sample data holds none.",
     "question": "Should access notes ever appear in monday, and for whom?"},
    {"statement": "The user's own account has the tier it has; the portfolio default (A6) is not applied, because the work is recurring plans and routes, not projects.",
     "question": "None for the client; read at preflight."},
]

unmet = [
    {"need": "complaints that arrive by email, the website and reviews landing in one place by themselves", "clock": None,
     "why_not_met": "email-to-ticket is a deferred Service extra (A7); in v0.1 each complaint is keyed by hand; the need stays the client's"},
    {"need": "complaints and texts that reach the owner's personal cell reaching the team", "clock": None,
     "why_not_met": "a personal phone is not a channel the build connects; how these should reach the team is a question for the owner, who was not on the call"},
    {"need": "the application record reaching the system from the technician's phone instead of through Rhonda's re-keying", "clock": None,
     "why_not_met": "the record must stay in the system (Travis, L193) and the integration direction is unresolved; v0.1 does not touch the system"},
    {"need": "a shorter morning rebuild of the routes (P2.1)", "clock": "every morning in season, Saturdays too",
     "why_not_met": "no element shortens it; the exceptions board changes how changes reach technicians, not the rebuild"},
    {"need": "printed route sheets for the technicians who want paper", "clock": None,
     "why_not_met": "not a product limit: the system keeps printing them, and the build does not take them away; recorded so the app is never made the only channel"},
    {"need": "both branches working the same way, so covering North is possible", "clock": None,
     "why_not_met": "North's scope is the owner's decision; nothing is built for North in v0.1"},
    {"need": "an answer to whether the system stays or is replaced", "clock": None,
     "why_not_met": "a decision for the owner ('I don't think Gary's getting rid of the system. I mean -- I don't know.'); the build assumes it stays"},
]
q("I don't think Gary's getting rid of the system. I mean -- I don't know.", "L295, Renata")

ai = [
    {"pain_or_need": "P1.1", "kind": "workflow", "round": 2, "probe_basis": "P-21",
     "idea": "a workflow that notifies dispatch and the customer service lead when a re-treat ticket has sat in new for a day (the consultant pitched this; Renata's 'That'd be nice' is a signal, not a request)"},
    {"pain_or_need": "P3.4", "kind": "workflow", "round": 2, "probe_basis": "P-21",
     "idea": "a workflow that creates a call-before-spray task for a notify-list customer whenever the round's date changes"},
    {"pain_or_need": "P6.1", "kind": "workflow", "round": 2, "probe_basis": "P-21",
     "idea": "a workflow that flags a plan when a second skip in a row is recorded, so the cancel is caught before billing"},
    {"pain_or_need": "P4.2", "kind": "ai_column", "round": 2, "probe_basis": "unprobed",
     "idea": "an AI column that reads the pasted complaint text and suggests the request type and what was promised, for the customer service lead to confirm"},
    {"pain_or_need": "P5.1", "kind": "ai_column", "round": 2, "probe_basis": "unprobed",
     "idea": "an AI column that turns a technician's note ('customer asked about mosquito') into an add-on request type"},
]
q("That'd be nice.", "L119, Renata")

verdict = {
    "cleared_for": "build-generic",
    "conditions": [
        "approval stop still to pass",
        "no A11 question first matters: own-account target, sample data in the user's own account needs no decision (A21); the three A11 decisions stay open",
        "the copy of the callback sheet and the photo of the whiteboard are committed by the client, not received; the Tickets columns are built from the spoken list at L83 until they arrive",
        "the North branch is out of the first version until the owner decides",
        "the native Service Tickets board is found by detection in the user's own account at preflight and recorded by id",
        "no figure on any sample row is the system's; every plan, round date and last service date is a sample value keyed by us, and the demo says so",
    ],
    "reason": "Two pains have an entity and a wanted outcome in the client's words (the call-in that stalls, with 'where's that re-treat at'; the route change that does not reach the technician, with 'push it to the guys and be done'), the products are chosen and the build target is named, but the Work Management half of the structure (rounds under plans, exceptions versus routes, skips, add-on capture) rests mostly on assumptions, so the build goes ahead as a generic version with the assumptions as the agenda for the next contact.",
}

questions = [
    {"text": "Renata, you said the sheet's fine, and then 'It's more that, um --'. What were you going to say? In the first version a call-in is one row with a status and an age that dispatch marks scheduled; what would it have to show for you to look it up instead of walking back to Travis?",
     "kind": "read-back", "role": "customer service lead",
     "known": "the sheet's columns (customer, address, what's going on, plan, last technician; L83), the two failure modes (plan left off; rain-day wipe; L111), the Pheasant Run instance, fifteen to twenty re-treat calls a week at the main branch (L131), her wanted outcome (L309)"},
    {"text": "Travis, you said the board works, then 'It's just, if I'm --'. If you're out, what happens? And you asked whether the route sheets would still print from the system: do you want them to, and should monday only carry the changes you make each morning?",
     "kind": "read-back", "role": "dispatcher",
     "known": "two hours every morning, Saturdays in season (L155); the causes (call-out, truck down, re-treats, same-day urgent; L151); half the technicians miss texts (L151); some want paper (L167); his wanted outcome (L317)"},
    {"text": "What can the system export (plans, rounds due, last service date, the day's routes), who can run it, and does anything need to be written into it?",
     "kind": "discovery", "role": "owner, or whoever administers the system",
     "known": "the system holds customers, plans, visits, nightly routes and the application records (L75, L147, L189); its name is unknown (L73); the QuickBooks hand-off is unclear (L295); Renata thinks it stays (L295)"},
    {"text": "How many rounds does a lawn plan have and what is each round's window, and where is a skip recorded today, and who takes the skipped service off the route?",
     "kind": "discovery", "role": "dispatcher and customer service lead",
     "known": "six rounds, seven with grub control, round one early spring (L231); rain pushes everybody (L231); the system shows who is overdue but not well (L235); skips become cancels caught at billing (L249)"},
    {"text": "Is North in the first version, and who would use monday day to day: office staff only, lead technicians, or every technician?",
     "kind": "discovery", "role": "owner",
     "known": "North has its own CSR, spreadsheet and routes (L141, L43); whether North is in scope is a Gary question (L305); about sixty technicians, more in summer, mixed company and personal phones, some on paper (L329, L167); lead technicians text Travis (L215)"},
]
for loc in ["L83, Renata", "L111, Renata", "L131, Renata", "L309, Renata", "L155, Travis", "L151, Travis", "L167, Travis",
            "L317, Travis", "L75, Renata", "L147, Travis", "L189, Travis", "L73, Travis", "L295, Renata", "L231, Travis",
            "L235, Travis", "L249, Renata", "L141, Renata", "L43, Travis", "L305, Renata", "L329, Travis", "L215, Travis"]:
    unit(loc)

note = (
    "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. "
    "Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top). "
    "The key's `should_plugin_propose_a_build: false` and its verdict answer the v2 sales question; under A19 and the user's "
    "decision of 2026-10-13, thin input clears a generic build with its assumptions listed."
)

key["readiness"] = {
    "schema": "readiness/1",
    "note": note,
    "pains": pains,
    "signals": signals,
    "entities": entities,
    "structure": structure,
    "existing": existing,
    "assumptions": assumptions,
    "unmet_needs": unmet,
    "ai_opportunities": ai,
    "verdict": verdict,
    "questions": questions,
}

# sales-vocabulary guard over the block
blob = json.dumps(key["readiness"], ensure_ascii=False)
for bad in [r"\bR\d{1,2}\b", r"\bNearly ready\b", r"\bNot ready\b", r"\bDiscovery complete\b", r"\bgate\b", r"\bgates\b",
            r"\bverdict\b(?!\")", r"\bMet\b", r"\bPartial\b", r"\bMissing\b", r"\bbleed\b", r"\bupside\b", r"\bexcavated\b(?!\")",
            r"\bgrade", r"\brubric\b"]:
    hits = [m.group(0) for m in re.finditer(bad, blob)]
    # the field names "verdict" and "stated_or_excavated" are the shape, not vocabulary; everything else must be clean
    hits = [h for h in hits if h not in ("verdict", "excavated")]
    if bad == r"\bgate\b":  # "gate code" is the client's access note, not the method's gate
        hits = [m.group(0) for m in re.finditer(r"\bgate\b(?! code)", blob)]
    assert not hits, (bad, hits)

# field order and shape checks
assert list(key.keys())[-1] == "readiness" and len(key) == 26
assert {p["id"] for p in pains} == {e["pain"] for e in structure["element_per_pain"]}
assert len(questions) <= 5
for e in entities:
    assert e["moves_independently"] in ("yes", "no", "unknown")
    assert e["source"] in ("spoken", "observed", "documented", "assumed")
    if e["parent"]:
        assert e["parent"] in {x["name"] for x in entities}, e["parent"]

out = json.dumps(key, indent=2, ensure_ascii=False) + "\n"
open(KEY, "w", encoding="utf-8").write(out)
print("written;", len(PROOFS), "quote proofs;", len(pains), "pains;", len(signals), "signals;", len(entities), "entities;",
      len(L), "leanings;", len(assumptions), "assumptions;", len(unmet), "unmet;", len(ai), "ai;", len(questions), "questions;",
      out.count("\n"), "lines")
