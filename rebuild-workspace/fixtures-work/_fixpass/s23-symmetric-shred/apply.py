"""Fix pass for s23-symmetric-shred: FEEDBACK items, direction rename, sweep corrections,
the never-written rule, standing lines, and the readiness block. Run from anywhere."""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from keyfmt import dumps

FX = '/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s23-symmetric-shred'
KEY = os.path.join(FX, 'answer-key.json')
TR = os.path.join(FX, 'transcript.txt')

raw = open(KEY, encoding='utf-8').read()
key = json.loads(raw)
assert dumps(key) == raw, 'round trip must be byte-identical before any change'
lines = open(TR, encoding='utf-8').read().split('\n')
assert lines[-1] == '' and len(lines) == 265
units = {i: l for i, l in enumerate(lines[:264], 1)}

LOC = re.compile(r'^L(\d+), (\d\d:\d\d:\d\d) (.+)$')

def prove(quote, location):
    m = LOC.match(location)
    assert m, location
    n, ts, lab = int(m.group(1)), m.group(2), m.group(3)
    u = units[n]
    assert u.startswith(f'{ts} {lab}: '), (location, u[:40])
    assert quote in u, (quote, location)
    return True

def replace_once(s, old, new):
    assert s.count(old) == 1, (old[:60], s.count(old))
    return s.replace(old, new)

log = []

# ---------------------------------------------------------------- 1. FEEDBACK items
# Item 1: true talk share is fixture ground truth; line 162 trap reworded.
old = key['traps'][1]
assert old.startswith("The quietest speaker's figure is wrong by 2.7 points")
key['traps'][1] = ("The quietest speaker's figure by label is a label count, not a measurement: Thandiwe is 6.4 percent "
    "by label, and the heads and tails of her duet units are credited to the Consultant. Report the by-label figure "
    "with a warning that shredding likely understates it, never a corrected figure; the true share is fixture ground "
    "truth from the generation plan, which no grader expects as output (FEEDBACK 2026-10-13). Do not rank speakers "
    "by label counts as if they were measurements.")
log.append(('traps[1]', 'FEEDBACK s23 item 1', 'reworded: by-label figure with a warning; no corrected figure'))

sh = key['intake']['shred']
new_sh = {}
for k, v in sh.items():
    new_sh[k] = v
    if k == 'talk_share_true_by_words':
        new_sh['talk_share_true_note'] = ("fixture ground truth from the generation plan, kept for the fixture's own "
            "record; a plugin given only this transcript cannot establish it and no grader expects it as output; the "
            "graded output is the by-label figure with a warning that shredding likely understates it")
new_sh['quietest_speaker'] = ("Thandiwe Rourke by label (6.4 percent, 433 words); reported as a label count with a "
    "warning that shredding likely understates it, because inside the two duets the first and last clause of most of "
    "her units carry the Consultant's label; the same-side movement is invisible to the side-level share. The "
    "generation plan's figure (9.1 percent, 618 words) is fixture ground truth that no grader expects as output")
key['intake']['shred'] = new_sh
log.append(('intake.shred', 'FEEDBACK s23 item 1', 'talk_share_true_note added; quietest_speaker reworded'))

key['purpose_of_this_fixture'] = replace_once(key['purpose_of_this_fixture'],
    "the quietest speaker's figure is reported with its error,",
    "the quietest speaker's by-label figure is reported with a warning that shredding likely understates it (the true "
    "share is fixture ground truth no grader expects),")
key['purpose_of_this_fixture'] = replace_once(key['purpose_of_this_fixture'],
    "is understated by 2.7 points (9.1 true, 6.4 by label)",
    "is understated by 2.7 points (9.1 in the generation plan, 6.4 by label)")
key['transcript_format'] = replace_once(key['transcript_format'],
    "in truth Thandiwe 9.1 and Consultant 27.8, the other three within a tenth.",
    "in truth (the generation plan's figures, fixture ground truth that no grader expects as output) Thandiwe 9.1 and "
    "Consultant 27.8, the other three within a tenth.")
a4 = key['attendees'][4]
a4['role'] = replace_once(a4['role'], "The quietest speaker in truth (9.1 percent) and by label (6.4 percent).",
    "The quietest speaker by label (6.4 percent, a label count that shredding likely understates; the true figure is "
    "fixture ground truth no grader expects).")
ab = key['accepted_behaviours']
ab[3] = replace_once(ab[3], "provided the report says it is a label count with the shred's error and does not call her",
    "provided the report says it is a label count that shredding likely understates, gives no corrected figure, and "
    "does not call her")
conf = key['intake']['confidence']
conf['propagation'] = replace_once(conf['propagation'], "Thandiwe's share is reported with its error",
    "Thandiwe's share is reported as a label count with a warning that shredding likely understates it")
log.append(('purpose_of_this_fixture, transcript_format, attendees[4].role, accepted_behaviours[3], intake.confidence.propagation',
            'FEEDBACK s23 item 1', 'every "with its error" or "in truth" reading marked as ground truth or reworded to the warning'))

# Item 2: pack documents carry state; the checklist verifies the version.
why = key['expected_monday_products'][0]['why']
why = replace_once(why, "The pack is a checklist on the job that changes when the object list changes.",
    "The pack is the job's documents as child rows, each carrying its state (draft, issued, signed, approved); the "
    "checklist verifies that the current issued or approved version is in the pack, not that a document exists, and a "
    "pack built before a document's final version arrived shows as outdated, as does one built before the object list "
    "changed.")
# Item 3: crates carry state, location and holdings.
why = replace_once(why, "The crate schedule is a three-week view with Margit's crate numbers on the objects.",
    "The crate schedule is a three-week view over a Crates board keyed on Margit's numbers, where each crate carries "
    "its state, its location and which job holds it for which dates, so a crate is never promised twice and an "
    "available one is not rebuilt.")
key['expected_monday_products'][0]['why'] = why
log.append(('expected_monday_products[0].why', 'FEEDBACK s23 items 2 and 3', 'pack and crate sentences corrected'))

voc = {v['their_term']: v for v in key['vocabulary']}
voc['pack, job pack']['likely_monday_object'] = ("the job's documents as child rows from the job's type, each with its "
    "state (draft, issued, signed, approved) and the date its current version arrived; the pack reads complete only on "
    "final versions and outdated when a final version or an object-list change arrived after it was built")
voc['crate, travel frame']['likely_monday_object'] = ("an item on a Crates board keyed on Margit's number, with state "
    "(in use, available, scrapped), location and holdings (which job, from when to when) as child rows; connected from objects")
log.append(('vocabulary["pack, job pack"], vocabulary["crate, travel frame"]', 'FEEDBACK s23 items 2 and 3', 'likely_monday_object corrected'))

es = key['expected_structures']
es['notes'] = replace_once(es['notes'],
    "The pack is a checklist on the job derived from the job's type and object list, and the crate schedule is a "
    "three-week view keyed on Margit's crate numbers.",
    "The pack is the job's documents as child rows from the job's type, each with its state, verified at the current "
    "issued or approved version and shown as outdated when a final version or an object-list change arrived after the "
    "pack was built; the crate schedule is a three-week view over crates that carry state, location and which job holds "
    "them for which dates.")
lt = es['lookalike_traps']
lt[4] = replace_once(lt[4], "instead of crates as records keyed on Margit's number with a three-week view.",
    "instead of crates as records keyed on Margit's number with state, location and holdings, and a three-week view.")
lt[6] = replace_once(lt[6], "when the pack is a checklist on the job derived from the job's type and object list and the handlers do not type.",
    "when the pack is the job's documents as rows with their states, derived from the job's type and object list, and the handlers do not type.")
log.append(('expected_structures.notes, lookalike_traps[4], lookalike_traps[6]', 'FEEDBACK s23 items 2 and 3', 'pack and crate wording corrected'))

# ---------------------------------------------------------------- 2. direction rename
th = key['intake']['type_header']
assert 'direction_of_show' in th
key['intake']['type_header'] = {('direction' if k == 'direction_of_show' else k): v for k, v in th.items()}
log.append(('intake.type_header.direction_of_show', 'brief section 4, rename', 'now direction; position kept'))

# ---------------------------------------------------------------- 3. sweep corrections in existing fields
key['company']['name'] = replace_once(key['company']['name'], "Aldergate Fine Art Services (called 'Aldergate')",
    "Aldergate (the only name spoken, L15; no longer trading name is said)")
log.append(('company.name', 'sweep 7: an expected output the input cannot support', '"Fine Art Services" is never spoken'))
key['transcript_format'] = replace_once(key['transcript_format'], "Currency is pounds, said once.",
    "Currency is pounds, said twice (L129, L151).")
log.append(('transcript_format', 'factual correction found while checking the file', 'pounds is said twice, not once'))
a2 = key['attendees'][2]
a2['decision_role'] = replace_once(a2['decision_role'],
    "(and the likely owner of the crate records; she will enter the book once and will not renumber)",
    "(and the likely owner of the crate records; she will not renumber (L238); entering the book once at a desk is our "
    "proposal (L232, L234), not her commitment)")
voc['the book']['likely_monday_object'] = ("the seed of the Crates board; our proposal is that Margit enters it once at "
    "a desk (L232, L234), which she has not confirmed; not a spreadsheet grid")
log.append(('attendees[2].decision_role, vocabulary["the book"]', "sweep 4: our framing labelled as the client's",
            'the one-time book entry is Thandiwe\'s proposal, never Margit\'s words'))

# ---------------------------------------------------------------- 4. the never-written rule
UNRES = ("writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of it is our "
         "safe default, labelled as ours")
key['purpose_of_this_fixture'] = replace_once(key['purpose_of_this_fixture'],
    "with the client's inventory system left as the book of record and read only.",
    f"with the client's inventory system left as the book of record ({UNRES}).")
why = key['expected_monday_products'][0]['why']
why = replace_once(why, "The inventory system stays the book of record, read only, with invoicing untouched.",
    "The inventory system stays the book of record and invoicing keeps running from it (the client's requirement, L96, "
    f"L97, L207); {UNRES}.")
key['expected_monday_products'][0]['why'] = why
im = key['integrations_mentioned']
im[0] = replace_once(im[0], "The inventory system: the feed source and the book of record, read only, never written to; jobs and objects",
    f"The inventory system: the feed source and the book of record; {UNRES} (the client's own requirements are that it is "
    "not replaced, L207; values never leave it, L211; invoicing keeps running from it, L96 and L97; nothing is typed "
    "twice, L170); jobs and objects")
es['notes'] = replace_once(es['notes'], "the inventory system is never written to and invoicing is untouched;",
    "invoicing is untouched and the inventory system is not replaced (the client's words, L96, L97, L207); writeback and "
    "integration direction unresolved, v0.1 depends on neither, and staying clear of the inventory system is our safe "
    "default, labelled as ours;")
log.append(('purpose_of_this_fixture, expected_monday_products[0].why, integrations_mentioned[0], expected_structures.notes',
            'never-written rule (FEEDBACK s14 item 2; brief section 4)', 'four occurrences reworded; the client-backed parts kept with their lines'))

# ---------------------------------------------------------------- 5. standing lines (s21)
c = key['commitments_and_next_steps']
c[0]['what'] = replace_once(c[0]['what'], "with Constance, Eamon, Margit and the managing director; Margit taps",
    "with Constance, Eamon and Margit, and the managing director if Constance asks him ('If I ask him he'll come', L209; "
    "she has not said she will); Margit taps")
c[0]['owner'] = replace_once(c[0]['owner'], "Consultant (hosts); Constance to confirm; Eamon, Margit and the managing director attend",
    "Consultant (hosts); Constance to confirm the slot and to decide whether she asks the managing director; Eamon and Margit attend")
c[6]['owner'] = replace_once(c[6]['owner'], "Constance (to invite); Consultant (to plan the segment)",
    "unassigned on the call: Margit asked and the Consultant noted it (L258); who invites the crew chief is not said; "
    "Consultant (to plan the segment)")
log.append(('commitments_and_next_steps[0].what, [0].owner, [6].owner', 'standing line s21',
            "the managing director's attendance and the crew chief's invitation were owners the call never gave"))

# ---------------------------------------------------------------- 6. the readiness block
def Q(quote, location):
    prove(quote, location); return quote

P = key['pains']
assert len(P) == 6
EK, MS, CA = 'registrar (client; influencer and end user; the person who does the work on P1 and P2)', \
    'warehouse and crate shop lead (client; end user; owner of the crate numbers, the whiteboard and the book)', \
    'operations lead (client; approver up to twenty-five thousand)'
out1 = Q("I want to answer a museum's question about their object from my desk, with the photograph, in under a minute, without walking to a filing cabinet or asking Eamon. And I want to get to next May with no claim.", "L200, 00:35:06 Constance Ayodele")
out2 = Q("I want the pack to know the job changed. That's it. If the museum drops an object, the packing list and the forms should drop it before I do.", "L202, 00:35:44 Eamon Kilbride")
out3 = Q("I want to see next week's crates on a screen on a Monday morning, not on a whiteboard I wrote on a Friday. And no typing in the shop.", "L201, 00:35:29 Margit Sowande")
pains = []
for i, (role, se, outc) in enumerate([(EK, 'excavated', out1), (EK, 'excavated', out2), (MS, 'excavated', out3),
                                      (EK, 'stated', None), (CA, 'stated', None), (EK, 'stated', None)]):
    e = P[i]; prove(e['quote'], e['location'])
    pains.append({"id": f"P{i+1}", "quote": e['quote'], "location": e['location'], "speaker_role": role,
                  "stated_or_excavated": se, "outcome": outc})

signals = [
    {"quote": Q("Condition reports first, though. If I get one thing out of this before February, it's that one.", "L247, 00:44:55 Eamon Kilbride"),
     "location": "L247, 00:44:55 Eamon Kilbride", "pain": "P1",
     "not_confirmed": "the five-piece first cut as a set: the assent at the end of L246 sits inside our own unit and is non-evidence; the three client reactions that follow each accept one piece, never the set"},
    {"quote": Q("If it's a phone in a pocket and one tap, maybe. Maybe. I've seen a nephew's app die in a month here.", "L220, 00:38:36 Margit Sowande"),
     "location": "L220, 00:38:36 Margit Sowande", "pain": "P1",
     "not_confirmed": "that handlers in gloves will use a one-tap phone capture; conditional in her mouth, and the glove test in the yard is the only thing that settles it"},
    {"quote": Q("That's the win, and it's Lionel's win too, he's said it at every management meeting since June.", "L200, 00:35:06 Constance Ayodele"),
     "location": "L200, 00:35:06 Constance Ayodele", "pain": "P1",
     "not_confirmed": "the managing director's own agreement to the outcome; relayed by Constance, never heard from him; he was not on the call"},
    {"quote": Q("Handlers not typing. And that the values never leave the inventory system. He's said both to me, he'll say both to you, and if either one isn't true he's out and honestly so am I.", "L211, 00:37:12 Constance Ayodele"),
     "location": "L211, 00:37:12 Constance Ayodele", "pain": "P1",
     "not_confirmed": "the managing director's two conditions in his own words, relayed and adopted by Constance; our side never asked whether a phone tap counts as typing to him"},
    {"quote": Q("me the invite, I don't hold dates in my head. And I want Marek in the room for the photo part, because they're his handlers and he'll say what they'll actually do.", "L257, 00:46:56 Margit Sowande"),
     "location": "L257, 00:46:56 Margit Sowande", "pain": "P1",
     "not_confirmed": "the walkthrough slot (the assent at L252 sits inside our own unit) and who invites the crew chief; nobody on the call took it"},
    {"quote": Q("And Ravensdale. If it isn't in the system it isn't in your feed, so half my crates aren't in your feed, and that's before you ask about the bay numbers.", "L226, 00:40:00 Margit Sowande"),
     "location": "L226, 00:40:00 Margit Sowande", "pain": "P4",
     "not_confirmed": "that Margit will enter the book once at a desk and keep her bay numbers as locations: our proposal at L232 and L234, never answered by her; her own words are no typing in the shop (L201) and no renumbering (L238)"},
]

def ent(name, parent, mi, shared, stale, source, evidence):
    if evidence: prove('', evidence)
    return {"name": name, "parent": parent, "moves_independently": mi, "shared_resource": shared, "goes_stale": stale, "source": source, "evidence": evidence}

entities = [
    ent("job", None, "yes", False, True, "spoken", "L54, 00:08:42 Eamon Kilbride"),
    ent("job state in the inventory system (booked, out, returned)", "job", "no", False, False, "spoken", "L64, 00:10:53 Eamon Kilbride"),
    ent("object (as the inventory system lists it: one line per object per job)", "job", "yes", False, True, "spoken", "L223, 00:39:20 Eamon Kilbride"),
    ent("object reference and accession number (today one field, sometimes both with a slash)", "object (as the inventory system lists it: one line per object per job)", "no", False, True, "spoken", "L223, 00:39:20 Eamon Kilbride"),
    ent("insurance value (never enters the build)", "object (as the inventory system lists it: one line per object per job)", "no", False, False, "spoken", "L56, 00:09:04 Eamon Kilbride"),
    ent("job pack", "job", "no", False, True, "spoken", "L58, 00:09:30 Eamon Kilbride"),
    ent("loan agreement (from the museum by email; unsigned, signed)", "job pack", "yes", False, True, "spoken", "L131, 00:22:19 Eamon Kilbride"),
    ent("insurance certificate (from the insurer by email)", "job pack", "yes", False, True, "spoken", "L60, 00:09:57 Eamon Kilbride"),
    ent("export licence and customs paperwork (from the broker, a person; draft, issued; only when the object leaves the country)", "job pack", "yes", False, True, "spoken", "L126, 00:21:14 Eamon Kilbride"),
    ent("packing list (made in a spreadsheet from the object list)", "job pack", "yes", False, True, "spoken", "L135, 00:22:57 Eamon Kilbride"),
    ent("blank condition report forms (printed, one per object)", "job pack", "yes", False, True, "spoken", "L135, 00:22:57 Eamon Kilbride"),
    ent("crew brief (where, who, what the building is like)", "job pack", "yes", False, True, "spoken", "L58, 00:09:30 Eamon Kilbride"),
    ent("condition report (outgoing at collection, incoming at return)", "object on a job", "yes", False, False, "spoken", "L76, 00:12:59 Eamon Kilbride"),
    ent("condition photograph", "condition report (outgoing at collection, incoming at return)", "no", False, False, "spoken", "L78, 00:13:18 Eamon Kilbride"),
    ent("condition-report request from a museum", "object on a job", "yes", False, False, "spoken", "L103, 00:17:04 Eamon Kilbride"),
    ent("claim", "object on a job", "yes", False, False, "spoken", "L42, 00:06:26 Constance Ayodele"),
    ent("crate (and travel frame): a number for life, built, reused across jobs, scrapped", None, "yes", True, True, "spoken", "L70, 00:12:05 Margit Sowande"),
    ent("crate holding (which job holds a crate from when to when)", "crate (and travel frame): a number for life, built, reused across jobs, scrapped", "yes", True, True, "assumed", None),
    ent("the book (every crate ever built, by number, dimensions and purpose)", None, "no", False, True, "spoken", "L68, 00:11:36 Margit Sowande"),
    ent("the whiteboard (crates by the week needed, in Margit's shorthand)", None, "no", False, True, "spoken", "L72, 00:12:19 Margit Sowande"),
    ent("store location (main store, Ravensdale, Margit's bay numbers)", None, "no", False, True, "spoken", "L162, 00:26:57 Margit Sowande"),
    ent("nightly file from the inventory system (as of two in the morning)", None, "no", False, True, "spoken", "L253, 00:46:18 Eamon Kilbride"),
    ent("crew and van grid (shared calendar for the vans, printed grid for the people; redone Monday)", None, "yes", True, True, "spoken", "L74, 00:12:35 Constance Ayodele"),
    ent("handler (art handler on the crew; gloves; will not type)", None, "yes", True, False, "spoken", "L220, 00:38:36 Margit Sowande"),
    ent("museum (the client's customer; owns its objects and its own photographs)", None, "yes", False, False, "spoken", "L243, 00:43:27 Eamon Kilbride"),
    ent("museum's registrar (the contact on a loan)", "museum (the client's customer; owns its objects and its own photographs)", "yes", False, False, "spoken", "L32, 00:04:59 Constance Ayodele"),
    ent("courier (a member of the museum's staff travelling with the object)", "museum (the client's customer; owns its objects and its own photographs)", "yes", False, False, "spoken", "L111, 00:18:43 Eamon Kilbride"),
    ent("the framework and the consortium (seven museums; a job source and a clause)", None, "yes", False, False, "spoken", "L36, 00:05:31 Constance Ayodele"),
    ent("loans in (private collectors' storage with a report at every touch; turned away today)", "job", "yes", False, False, "spoken", "L196, 00:34:13 Constance Ayodele"),
    ent("enquiry and quote (before the job exists; out of scope, no CRM)", "job", "yes", False, False, "spoken", "L52, 00:08:22 Eamon Kilbride"),
]

def lean(question, option, qls, condition, pattern):
    quotes = [q for q, l in qls]; locs = [l for q, l in qls]
    for q, l in qls: prove(q, l)
    return {"question": question, "option": option, "quotes": quotes, "locations": locs, "condition": condition, "pattern": pattern}

leanings = [
    lean("Is the pack one checklist row per job with a tick per document, or the job as parent with each document as a child row carrying its state?",
         "parent-row-with-roll-up: the job holds its pack documents as child rows (loan agreement, insurance certificate, packing list, condition forms, customs paperwork and export licence where the object leaves the country, crew brief), each with a state (draft, issued, signed, approved) and the date its current version arrived. The pack status on the job reads complete only when every required document is at its final state, and outdated when a document's final version arrived after the pack was built or the object list changed after the packing list and the forms were made. One tick per document copies the spreadsheet that failed at the port.",
         [("The licence was issued, I had the email, and the copy in the pack was the draft, not the issued one, because the issued one came in at six the night before and I'd already built the pack. The port wouldn't accept the draft.", "L126, 00:21:14 Eamon Kilbride"),
          ("two where the crew got to a museum and the loan agreement in the pack was the unsigned version and the registrar wouldn't release the object", "L131, 00:22:19 Eamon Kilbride"),
          ("It works until the museum changes the object list, which they do, and then the packing list is wrong and the condition forms are wrong and the tick is still there.", "L135, 00:22:57 Eamon Kilbride")],
         "Eamon names the states each of the six documents passes through and which one is final for each, and who records a state when a document lands by email; a state set by a person is a claim, and the email is the evidence",
         "an artefact that can go stale with nothing to flag it"),
    lean("Is a crate a number written on an object, or a record with a state, a location and a holding?",
         "a Crates board keyed on Margit's number, one row per crate with its dimensions, state (in use, available, scrapped), location (main store, Ravensdale, her bay number) and holdings as child rows (job, from date, to date); an object on a job points at a crate; the three-week view shows crates needed, held and free, so a crate is never promised to two jobs and an available one is not built again",
         [("Never. A number is a crate for life. If it's scrapped, the number is scrapped with it, and I write scrapped in the book.", "L70, 00:12:05 Margit Sowande"),
          ("Some things reuse a crate we already have, or a travel frame, which is a crate without a lid, more or less.", "L66, 00:11:06 Margit Sowande"),
          ("If Eamon puts a Ravensdale crate on a job, he's guessing it exists.", "L162, 00:26:57 Margit Sowande"),
          ("Four or five times a year I build a crate and then find one in the book that would have done.", "L151, 00:25:20 Margit Sowande")],
         "Margit says from when to when a job holds a crate today and who says it is free again; nothing on the call describes a holding, so the holding rows are assumed until she does",
         "a shared resource with no reservation tracking"),
    lean("Is the condition report a pointer to photographs on the shared drive, or an item per object per direction with the photographs captured straight into it?",
         "an item per object per direction, with the photographs uploaded from the phone into the item at the museum and the object reference on each, so the report exists the moment it is taken; a view of outgoing reports with no photograph replaces Eamon's Friday chase list; the shared drive stops being the store; the museum's own photographs are never stored",
         [("The phone. Then the drive, if we're lucky. Nothing in the inventory system, it doesn't take pictures, it takes money.", "L88, 00:14:26 Eamon Kilbride"),
          ("I've got a list of jobs where I haven't seen photos, and on a Friday I go round.", "L120, 00:20:16 Eamon Kilbride"),
          ("Condition reports with photographs within twenty-four hours of collection, and available on request to any of the seven.", "L38, 00:05:53 Constance Ayodele")],
         "the glove test in the yard before Christmas and the photo size test before the walkthrough; if a handler in gloves will not tap, the capture is someone else's step and the structure says whose",
         "an artefact that can go stale with nothing to flag it"),
    lean("Is an object one row per job, as the inventory system lists it, or one record that appears on many jobs?",
         "for the first version, one object row per job line as the feed gives it, with the reference and the accession number as two columns, so a museum's question is answered by reference across jobs; a persistent object record with its job appearances as child rows waits until the reference field is clean, because until then the same object is two strings on two jobs and no record can be keyed",
         [("Job number, the client, the dates, and then I add the objects. Each object gets a line.", "L54, 00:08:42 Eamon Kilbride"),
          ("So if a museum asks about one object, I have to know which job it was on, which I usually do, and then find the form", "L84, 00:13:50 Eamon Kilbride"),
          ("So the same object can be two different strings on two different jobs.", "L223, 00:39:20 Eamon Kilbride")],
         "the ten-object sample and Eamon's answer on whether the normalised reference is consistent across jobs; if it is, the object becomes the parent and the job lines its children",
         "one row where the call describes many"),
    lean("Does a row read from the inventory system show when it was last read?",
         "every job and object row read from the feed carries an as-of time and its source (interface, nightly file, or keyed by Eamon); in v0.1 every row is a sample value and the board says so; a job confirmed after the nightly file ran is not on the board until the next read, and the as-of time is what tells Margit that",
         [("There's a nightly file, it lands on the shared drive at two in the morning.", "L253, 00:46:18 Eamon Kilbride"),
          ("If the vendor takes six weeks to answer Thandiwe, build it with Eamon typing ten jobs in by hand and we'll live with that for a month.", "L250, 00:45:22 Constance Ayodele")],
         "which of the three mechanisms the first version runs on, from the vendor's answers to the five questions",
         "an artefact that can go stale with nothing to flag it"),
    lean("Who enters the book into the Crates board, and are the invented bay numbers kept?",
         "our proposal is that Margit enters the four hundred and something crates once, at a desk, and that her bay numbers become the Ravensdale location values; it is labelled as ours until she says so, because her own words are no typing in the shop and no renumbering",
         [("And no typing in the shop. If it needs typing it dies.", "L201, 00:35:29 Margit Sowande"),
          ("Whatever you key on, the crate number is mine, and I'm not renumbering four hundred crates for a computer.", "L238, 00:42:47 Margit Sowande"),
          ("The other half is in the book, with my location, which is a bay number I made up.", "L162, 00:26:57 Margit Sowande")],
         "Margit's answer to the read-back; if she will not key it, who does, from her book, and how the bay numbers are kept",
         "our framing labelled as the client's"),
    lean("Is there an element for the crew and van grid?",
         "none in the first version: nobody asked for it, the look-alike list warns against a crew grid board, and a late crate reaching the crew chief is the only tie; recorded as a need the build does not meet, and the shared calendar and the printed grid stay his",
         [("and then he does it again on the Monday because something moved.", "L74, 00:12:35 Constance Ayodele"),
          ("Marek, who has to find them another day.", "L139, 00:23:39 Eamon Kilbride")],
         "the crew chief or Constance asks for it; the crew chief is in the room for the photo part on the fifth and can be asked",
         "a pain with no element that fixes it"),
]

structure = {
    "products": ["Work Management"],
    "build_target": "own-account",
    "build_target_reason": "prospect, so the user's own account by default (A21)",
    "workspaces": ["Aldergate – Ops"],
    "native_reuse": "none: no CRM or Service entity. Work Management is built structure: Jobs, Objects, Condition Reports, Pack Documents and Crates as connected boards, with a three-week crate view and a view of outgoing reports with no photograph.",
    "leanings": leanings,
    "patterns": [
        "parent-row-with-roll-up: job with pack documents as child rows, pack status (complete or outdated) on the job",
        "parent-row-with-roll-up: crate with holdings (job, from, to) as child rows, current state and location on the crate",
        "parent-row-with-roll-up: job with objects as child rows, outgoing-report and photograph completeness on the job",
    ],
    "element_per_pain": [
        {"pain": "P1", "element": "Condition Reports board: one item per object per direction, photographs uploaded from the phone into the item at the museum with the object reference on each; a view of outgoing reports with no photograph; Constance opens the item from her desk", "verdict": "fixes"},
        {"pain": "P2", "element": "pack documents as child rows of the job with state and arrival date; pack status complete or outdated on the job, re-derived when a final version lands or the object list changes", "verdict": "fixes"},
        {"pain": "P3", "element": "Crates board keyed on Margit's number with state, location and holdings; the three-week view of confirmed jobs with crates needed, held and free, from the feed or from Eamon's keyed jobs", "verdict": "fixes"},
        {"pain": "P4", "element": "two identifier columns on objects with an exceptions view of inconsistent references for Eamon to resolve; Ravensdale as a location value on crates once the book is entered. Until the feed's normalising step and the one-time entry exist, v0.1 shows sample identifiers and holds only the crates someone keyed, so the fix is proven only when both are real", "verdict": "copies-today's-tool"},
        {"pain": "P5", "element": "none: the crew and van grid is outside the first version and nobody asked for it", "verdict": "none"},
        {"pain": "P6", "element": "the monday job's own stages between booked and out (pack complete, crated, outgoing report done), set by people or by the report capture; the inventory system's three states are untouched and nothing here is evidence that it changed", "verdict": "fixes"},
    ],
}

for loc in ["L207, 00:36:25 Constance Ayodele", "L96, 00:15:34 Eamon Kilbride", "L78, 00:13:18 Eamon Kilbride", "L60, 00:09:57 Eamon Kilbride",
            "L68, 00:11:36 Margit Sowande", "L74, 00:12:35 Constance Ayodele", "L82, 00:13:40 Eamon Kilbride", "L204, 00:36:05 Constance Ayodele"]:
    prove('', loc)
existing = {
    "account": "unknown, no account bound. The key's account_context: no monday account at all ('No. Nothing.', L204); one museum registrar runs her exhibition schedule on the platform and that is all the client knows of it; the vendor's tracking module is an alternative in play with a quote on the managing director's desk, not an installed system. Under A21 the proof of concept goes into the user's own account in the workspace named above, so which account the client buys moves from pre-build to handover.",
    "incumbents": [
        {"system": "the inventory system", "authority": "stays system of record for: job numbers, clients, dates, the object lines with title, artist, dimensions, both identifiers and the insurance value, the three job states, invoicing on close ; follower for: nothing. Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of it is our safe default, labelled as ours. The client's own requirements: it is not replaced (L207), the values never leave it (L211), invoicing keeps running from it (L96, L97), nothing is typed twice (L170).", "evidence": "L207, 00:36:25 Constance Ayodele"},
        {"system": "the accounting system", "authority": "stays system of record for: invoices, received overnight from the inventory system the day a job closes ; follower for: nothing; the build does not reach it", "evidence": "L96, 00:15:34 Eamon Kilbride"},
        {"system": "the shared drive", "authority": "stays system of record for: the nightly file and the pack copies today ; follower for: condition photographs, which move into the report item", "evidence": "L78, 00:13:18 Eamon Kilbride"},
        {"system": "email (museums, the insurer, the broker)", "authority": "stays the channel for: loan agreements, certificates, the broker's paperwork and museums' requests ; follower for: nothing; a document's state is recorded on the job when the email lands, and the email is the evidence", "evidence": "L60, 00:09:57 Eamon Kilbride"},
        {"system": "the book and the whiteboard", "authority": "stays system of record for: crates, until the Crates board holds them and Margit says so ; follower for: the three-week view, which replaces the whiteboard only then", "evidence": "L68, 00:11:36 Margit Sowande"},
        {"system": "handlers' phones", "authority": "stays the capture device for: condition photographs ; follower for: nothing; the photograph leaves the phone into the report item", "evidence": "L78, 00:13:18 Eamon Kilbride"},
        {"system": "the crew chief's shared calendar and printed grid", "authority": "stays system of record for: vans and people ; follower for: nothing; outside the first version", "evidence": "L74, 00:12:35 Constance Ayodele"},
        {"system": "paper condition forms and the filing cabinet", "authority": "stays system of record for: every report made before the build ; follower for: new reports, once captured on the phone", "evidence": "L82, 00:13:40 Eamon Kilbride"},
    ],
}

assumptions = [
    {"statement": "The pack documents and their states are the same for every loan job; the customs paperwork and the export licence apply only when the object leaves the country.", "question": "Which documents does each job type need, and which states does each pass through before it is final?"},
    {"statement": "A pack document's state is recorded on the job by Eamon when the email lands.", "question": "Who records a document's state, and can the arrival email be attached as the evidence?"},
    {"statement": "A crate is held by a job from the day it is packed to the day the object is unpacked at return, and is free between jobs.", "question": "From when to when does a job hold a crate today, and who says it is free again?"},
    {"statement": "Margit enters the book once at a desk and her bay numbers become the Ravensdale location values.", "question": "Will she, and if not, who enters it from her book, and are the bay numbers kept?"},
    {"statement": "The feed gives one object line per job with the reference as one field; if the vendor is slow, the first version runs on ten jobs Eamon keys by hand.", "question": "Which of the three mechanisms does the first version run on, and does the nightly file carry both identifiers and the job close?"},
    {"statement": "Every row in the first version is sample data: fictional jobs, objects, museums and crates; no client object, museum name or value.", "question": "Which realistic shapes may appear in sample rows (job types, document names, crate sizes) so the walkthrough reads true to the room?"},
    {"statement": "The consortium's on-request clause is met in the first version by Constance opening the report and sending it; no museum reaches into the build.", "question": "Who may see a condition report outside the company, and does on request mean sent or self-served?"},
    {"statement": "A condition report is done on the phone in the loading bay with one tap per photograph and the object reference on it; the handler types nothing.", "question": "Does a phone tap count as typing to the handlers and to the managing director, and does it pass the glove test?"},
    {"statement": "The incoming report is compared with the outgoing one by a person, not by the build.", "question": "When an incoming report does not match the outgoing one, who looks, and what do they want in front of them?"},
    {"statement": "Loans in, the enquiry and quote step and the crew chief's grid are outside the first version.", "question": "Does any of these need a place in the first version before the managing director will say yes?"},
    {"statement": "The managing director sees the first version on the fifth, if Constance asks him, rather than afterwards through her.", "question": "Will Constance ask him, and does he see it on the fifth or afterwards?"},
    {"statement": "The insurance value is the only confidential field on the object line; title, artist, dimensions and both identifiers may appear.", "question": "Beyond the value, does the policy keep anything else on the object line off a screen?"},
    {"statement": "The shop first sees anything after the fifteenth of December and the first version exists before then.", "question": "Which days after the fifteenth, and who is on site for the glove test?"},
]

unmet_needs = [
    {"need": "Condition reports available on request to any of the seven consortium museums, within twenty-four hours of collection", "clock": "February: the framework starts then and its first move is in the second week; the clause says within twenty-four hours and on request", "why_not_met": "the first version answers a request from Constance's desk by sending the report; no museum sees into the build and no sharing mechanism exists yet; later work, kept in the record as the client's need"},
    {"need": "The crew chief's crew and van grid, redone every Monday because something moved (P5)", "clock": None, "why_not_met": "out of the first cut: nobody asked for it on the call; the shared calendar and the printed grid stay his; the look-alike list warns against building a crew grid board nobody asked for"},
    {"need": "Loans in: private collectors' storage with a report at every touch, turned away today", "clock": None, "why_not_met": "named as the thing they would go after once reports are real, with no figure; the report capture serves it later, and nothing in the first version is aimed at it"},
    {"need": "The vendor's answers to the five feed questions, so the first version can run on the interface rather than on keyed jobs", "clock": "the questions go to Eamon today; the vendor's timing after that", "why_not_met": "not ours to meet: Thandiwe sends the questions, Eamon forwards what he cannot answer, the vendor answers or does not; the client has said the feed is a question, not a condition (L250)"},
]

ai_opportunities = [
    {"pain_or_need": "P2", "kind": "workflow", "round": 2, "probe_basis": "P-21", "idea": "When a pack document's state moves to issued or signed after the pack was marked built, set the pack to outdated and notify Eamon with the document named."},
    {"pain_or_need": "P3", "kind": "workflow", "round": 2, "probe_basis": "P-21", "idea": "When a confirmed job's dates move or an object is added to it, re-check the crates held for it and tell Margit which crate is now needed earlier, so she hears on the Monday and not the Tuesday."},
    {"pain_or_need": "P1", "kind": "workflow", "round": 2, "probe_basis": "P-21", "idea": "When an outgoing report still has no photograph twenty-four hours after collection, notify Eamon and the crew chief; the photo notification to Constance stays a designed output, as the key already says."},
    {"pain_or_need": "P4", "kind": "agent", "round": 2, "probe_basis": "P-19", "idea": "An agent that reads this client's Ops workspace only and drafts the list of object references that look like the same object under two strings, in pairs, for Eamon to confirm or reject one by one; it changes nothing itself."},
    {"pain_or_need": "P1", "kind": "ai_column", "round": 2, "probe_basis": "unprobed", "idea": "An AI column that checks whether each outgoing photograph shows the object reference card and flags the ones that do not, so Eamon chases a photograph and not a whole job."},
]

verdict = {
    "cleared_for": "build",
    "conditions": [
        "approval stop",
        "no A11 question first matters here: the target is the user's own account, where sample data needs no decision (A21); the three A11 decisions stay open",
        "workspace to create: Aldergate – Ops, brand new, in the user's own account; the plugin writes into no other workspace",
        "sample rows only: fictional jobs, objects, museums and crates, no client object, no museum name, no value anywhere; every job and object row labelled sample with an as-of time, nothing presented as a live feed",
        "the first cut is not provably agreed: the five pieces go to Constance as five lines for a written yes (question 1) before the walkthrough treats them as scope",
        "the walkthrough on Thursday the fifth at ten is proposed, not confirmed; the recap asks Constance to confirm it; the managing director attends only if she asks him",
        "the feed mechanism is a question, not a condition, in the client's words (L250); the first version runs on keyed sample jobs",
        "nothing in front of the shop before the fifteenth of December (L214); the glove test in the yard before Christmas is the client's own test of the mobile capture",
    ],
    "reason": "Three pains have their entities and a wanted outcome in the client's own words (a museum's question answered from a desk with the photograph, a pack that knows the job changed, next week's crates on a screen on Monday), Work Management is chosen, the structure is stated with its leanings, and the target is the user's own account with its workspace named.",
}

questions = [
    {"text": "You heard the first cut as five pieces: jobs read from the inventory system, objects on the job without the value, a condition report per object done on a phone, the pack as a checklist that changes with the job, and the crate schedule three weeks out. Eamon said condition reports first, Margit asked to see the photo done with gloves on, and you said the feed must not hold anything up. Is that set, in that order, what the first version should be?",
     "kind": "read-back", "role": "Constance (approver); Eamon and Margit asked the same at the walkthrough",
     "known": "the playback at L246 is ours and its assent sits inside our own unit; the three client reactions (L247, L248, L250) each accept one piece; the order reports, packs, crates is the client's (L216, L217, L218); no client unit agrees the set"},
    {"text": "For each document in a pack, which states does it pass through and which one is final: the export licence from draft to issued, the loan agreement from unsigned to signed, the certificate, the customs paperwork, the packing list and the forms? And when the final version lands by email after the pack is built, who records it?",
     "kind": "discovery", "role": "Eamon (registrar)",
     "known": "the port (L126) and the two unsigned agreements (L131) were version failures, not missing documents; the museum changing the object list makes the packing list and the forms wrong (L135); the pack today is a spreadsheet with a tick per document (L137)"},
    {"text": "You said no typing in the shop and that you are not renumbering four hundred crates. Thandiwe proposed that the book is entered once, at a desk, by you, with your bay numbers kept as the Ravensdale locations. Is that right, and if not you, who? And when a crate goes on a job, from when to when is it held, and who says it is free again?",
     "kind": "read-back", "role": "Margit (warehouse and crate shop lead)",
     "known": "the crate number is hers and stays (L238, L239); a number is for life and scrapped stays scrapped (L70); about half of Ravensdale is in the book with invented bay numbers (L162); entering the book once is our proposal (L232, L234), never answered by her; nothing on the call says how long a job holds a crate"},
    {"text": "From the ten-object sample: which half of the reference field is yours and which is the museum's accession number, is your own reference the consistent one across jobs, and does the crate number ever sit in that field? Every term we key on is read back to you as your own string before anything is built.",
     "kind": "read-back", "role": "Eamon (registrar), with Thandiwe reading the sample",
     "known": "one reference field with their reference, the accession number or both with a slash (L223); about four thousand live objects (L225); the sample of ten objects with no values is committed by Eamon (L261, L262); the crate number is Margit's (L238)"},
    {"text": "Which of the three mechanisms does the first version run on: the vendor's interface read on a schedule, the nightly file, or Eamon keying ten jobs by hand? From the vendor: is there an interface at all, does the nightly file carry both identifiers, and does the job close come through?",
     "kind": "discovery", "role": "Eamon, and the vendor through him; Thandiwe owns the questions",
     "known": "a nightly file lands on the shared drive at two in the morning with one line per object, values probably excluded (L253, L255); the interface is unknown; Constance has said the feed is a question, not a condition (L250); Thandiwe writes the other four questions up today (L256)"},
]

readiness = {
    "schema": "readiness/1",
    "note": "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top).",
    "pains": pains, "signals": signals, "entities": entities, "structure": structure, "existing": existing,
    "assumptions": assumptions, "unmet_needs": unmet_needs, "ai_opportunities": ai_opportunities,
    "verdict": verdict, "questions": questions,
}

# checks on the block
assert len(questions) <= 5
pain_ids = {p['id'] for p in pains}
assert pain_ids == {e['pain'] for e in structure['element_per_pain']}
for e in entities:
    if e['parent']: assert e['moves_independently'] in ('yes', 'no', 'unknown')
for l in leanings: assert len(l['quotes']) == len(l['locations'])
blob = json.dumps({k: v for k, v in readiness.items()}, ensure_ascii=False)
blob_scan = re.sub(r'"stated_or_excavated": "(stated|excavated)"', '', blob)
bad = re.findall(r"\bR\d{1,2}\b|\bMet\b|\bPartial\b|\bMissing\b|advisory|met-with-residual|not-obtainable|\bgate\b|Nearly ready|Discovery complete|Not ready|\bbleed\b|\bupside\b|rubric|excavat", blob_scan)
assert not bad, bad

assert 'readiness' not in key
key['readiness'] = readiness
assert list(key.keys())[-2:] == ['intake', 'readiness']

out = dumps(key)
json.loads(out)
open(KEY, 'w', encoding='utf-8').write(out)
print('written', len(out.split('\n')) - 1, 'lines')
print('counts: pains', len(pains), 'signals', len(signals), 'entities', len(entities), 'with parent',
      sum(1 for e in entities if e['parent']), 'leanings', len(leanings), 'epp', len(structure['element_per_pain']),
      'incumbents', len(existing['incumbents']), 'assumptions', len(assumptions), 'unmet', len(unmet_needs),
      'ai', len(ai_opportunities), 'questions', len(questions))
for f, why, what in log:
    print('-', f, '|', why, '|', what)
