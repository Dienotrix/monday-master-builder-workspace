"""Fix pass for s15-shred-dense (2026-10-13). Loads the key, applies the FEEDBACK items, the
direction rename, the sweep corrections, the never-written rule, the standing lines and the
readiness block, proves every new quote at its cited transcript unit, and dumps the key in its
own style. Run from this folder: python3 -I apply.py"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import keystyle

FIX = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s15-shred-dense'
KEY = FIX + '/answer-key.json'
TR = FIX + '/transcript.txt'

# ---- transcript -------------------------------------------------------------------------
units = {}
for i, line in enumerate(open(TR, encoding='utf-8').read().split('\n'), 1):
    if not line:
        continue
    m = re.match(r'^(\d+:\d\d) (.+?): (.*)$', line)
    assert m, (i, line)
    units[i] = (m.group(1), m.group(2), m.group(3))

PERSON = {}
for lab in ['Tamsin Greaves', 'Greaves, Tamsin', 'TAMSIN GREAVES', 'Tamsin']: PERSON[lab] = 'Tamsin Greaves'
for lab in ['Oisin Farrelly', 'Farrelly, Oisin', 'OISIN FARRELLY', 'Oisin']: PERSON[lab] = 'Oisin Farrelly'
for lab in ['Dara Vasseur', 'Vasseur, Dara', 'DARA VASSEUR', 'Dara']: PERSON[lab] = 'Dara Vasseur'
for lab in ['Joost Teunissen', 'Teunissen, Joost', 'JOOST TEUNISSEN', 'Joost']: PERSON[lab] = 'Joost Teunissen'
for lab in ['Consultant', 'CONSULTANT']: PERSON[lab] = 'Consultant'

proofs = 0
def Q(n, text):
    """A quote at one unit: proves the text verbatim and returns (text, location)."""
    global proofs
    stamp, label, body = units[n]
    assert text in body, ('quote not at line', n, text, body)
    proofs += 1
    return text, f'L{n}, {stamp}, {label}'

def L(n):
    stamp, label, _ = units[n]
    return f'L{n}, {stamp}, {label}'

ROLE = {
    'Tamsin Greaves': 'operations director (client; approver for the operations budget)',
    'Oisin Farrelly': 'client services lead (client; end user)',
    'Dara Vasseur': 'lab manager (client; influencer, can stop anything that touches the lab)',
    'Joost Teunissen': 'systems (client; admin/owner of the lab system)',
}
def role_of_location(loc):
    label = loc.split(', ', 2)[2].replace(' (merged run)', '')
    return ROLE[PERSON.get(label, label)]

# ---- key ----------------------------------------------------------------------------------
raw = open(KEY, 'rb').read()
k = json.loads(raw)
assert keystyle.dumps(k).encode('utf-8') == raw, 'round trip broke before editing'
assert list(k.keys())[-1] == 'intake' and len(k) == 26

def sub(s, old, new):
    assert s.count(old) == 1, ('expected one occurrence', old[:60], s.count(old))
    return s.replace(old, new)

UNRESOLVED = ('writeback and integration direction unresolved; v0.1 does not depend on either; '
              'staying clear of the lab system is our safe default, labelled as ours')

# FEEDBACK item 1 and the never-written rule, purpose and products ------------------------------
k['purpose_of_this_fixture'] = sub(k['purpose_of_this_fixture'],
    "and a Work Management build that reads from the lab system's export and never writes to it.",
    "and a Work Management build that reads from the lab system's export; writeback and integration direction are unresolved and the first version depends on neither.")

why = k['expected_monday_products'][0]['why']
why = sub(why,
    "Nothing customer-facing in the first version, nothing the analysts touch in November, nothing written to the lab system.",
    "Nothing customer-facing in the first version, by the client's choice; nothing the analysts touch in November; " + UNRESOLVED + ".")
why = sub(why,
    "the vendor's customer portal is 'a slide', and customer-facing extras are out of the first version and deferred beyond v1 in any case.",
    "the vendor's customer portal is 'a slide', and customer visibility is out of the first version by the client's choice; it is what closes the audit finding, so a later customer-facing requirement stays open, with the February renewal as its clock; how it is met is open.")
k['expected_monday_products'][0]['why'] = why

# never-written rule: integrations, traps, lookalike trap, requested change, notes -----------------
k['integrations_mentioned'][0] = sub(k['integrations_mentioned'][0],
    "The lab system: the system of record, never written to ('What goes into the lab system stays in the lab system, and anything else reads from it.'); the vendor",
    "The lab system: the system of record. 'What goes into the lab system stays in the lab system, and anything else reads from it.' is the Consultant's sentence (L415), accepted by Dara with 'Then we're fine.' (L416); the client's own constraint is no double entry (L413); " + UNRESOLVED + ". The vendor")

k['traps'][23] = sub(k['traps'][23],
    "The lab system is never written to; the nightly export",
    "No client line says the lab system is never written to; the client's constraint is no double entry (L413) and the no-write sentence is the Consultant's (L415). Writeback and integration direction are unresolved, v0.1 depends on neither, and staying clear of the lab system is our safe default, labelled as ours. The nightly export")

k['expected_structures']['lookalike_traps'][2] = (
    "Rebuilding the lab system's job record field for field. The board mirrors the export; writeback and integration direction are unresolved, v0.1 depends on neither, and staying clear of the lab system is our safe default, labelled as ours.")

k['requested_changes'][3]['description'] = (
    "Pre-build constraint: no double entry, in the client's words; the build reads from the export. 'Whatever goes into the lab system stays there' is the Consultant's sentence at L415, accepted at L416; writeback and integration direction unresolved; v0.1 does not depend on either.")

# FEEDBACK item 1 elsewhere ----------------------------------------------------------------------
k['traps'][21] = sub(k['traps'][21],
    "the vendor's portal is 'a slide', nothing customer-facing is in the first version, and Service extras are deferred beyond v1 in any case.",
    "the vendor's portal is 'a slide', and nothing customer-facing is in the first version by the client's choice ('Customers don't see anything in the first version.', L457). Customer visibility is what closes the audit finding, so the need stays open with the February renewal as its clock and how it is met open; a product limit never deletes it from the record.")

k['requested_changes'][2]['description'] = (
    "Pre-build requirement: nothing customer-facing in the first version, by the client's choice; customers see nothing until the MD has seen it. Customer visibility is what closes the audit finding, so the need stays open with the February renewal as its clock; how it is met is open.")

k['expected_structures']['lookalike_traps'][1] = sub(k['expected_structures']['lookalike_traps'][1],
    "the client said nothing customer-facing until the MD has seen it.",
    "the client said nothing customer-facing until the MD has seen it. The need itself stays open: customer visibility is what closes the audit finding, with the February renewal as its clock; how it is met is open.")

k['commitments_and_next_steps'][9]['what'] = sub(k['commitments_and_next_steps'][9]['what'],
    "nothing customer-facing",
    "nothing customer-facing in the first version (the client's choice; the customer-visibility need stays open)")

# FEEDBACK items 2 and 3 and the rule: the blueprint notes ---------------------------------------
k['expected_structures']['notes'] = (
    "One product, built structure, no native-board rule in play: a Jobs board fed from the export (job number, customer, status mapped from the code, dates in and done, as the client listed the export; site and discipline stay wanted, with their source open until the export is inspected, and may have to be typed or derived; due typed by Dara), an urgents view visible from Carlisle, an on-hold list with an owner and a rung step (the name against each hold is the client's ask; the rung step is our addition in the play-back), and a turnaround view for the retail account. Automations are candidates to confirm with the client, not expected v0.1 logic: a reminder when a hold passes a day, a warning keyed to a date, a notification when an urgent changes. None was agreed on the call; 'day five' is when customers ring (L206), not an internal deadline, and chemistry takes five to ten days, so a flat day-five warning would fire on chem jobs that are on time. Constraints that survive into any shape: nothing typed twice, nothing derived for due, nothing the analysts touch in November, nothing customer-facing in the first version by the client's choice (the customer-visibility need stays open); writeback and integration direction for the lab system unresolved, v0.1 depending on neither.")

k['vocabulary'][14]['likely_monday_object'] = (
    "dropdown column (site) on the job, its source open until the export is inspected (typed or derived if the export does not carry it); the same board filtered, not a second board")
k['vocabulary'][16]['likely_monday_object'] = (
    "dropdown column (discipline) on the job, its source open until the export is inspected (typed or derived if the export does not carry it)")

k['expected_questions_before_building'][1] = sub(k['expected_questions_before_building'][1],
    "and whether the vendor's acceptance of reading the export is in writing.",
    "whether site and discipline are in it or must be typed or derived, whether a customer code survives the scrubbing so the retail account's rows can be picked out, and whether the vendor's acceptance of reading the export is in writing.")

k['expected_questions_before_building'][9] = (
    "Notifications, as candidates to confirm with the client rather than agreed logic: whether any reminder is wanted when a hold passes a day, whether a warning should key on Dara's typed due rather than a flat day five (day five is when customers ring, and chem takes five to ten days), who is told when an urgent changes, and by what channel; presented as one approval list.")

k['accepted_behaviours'][14] = (
    "Presenting the automations (an on-hold reminder, a date-keyed warning, urgents notifications) as candidates to confirm with the client in one approval list with trigger, conditions, action and recipients per row, none of them expected v0.1 logic, noting that API-created automations cannot be switched off through the API.")

# FEEDBACK item 4: the date ----------------------------------------------------------------------
k['rubric'][9]['note'] = sub(k['rubric'][9]['note'],
    "The weekday and date fit Thursday 17 September 2026 with the call earlier that month; no timezone is stated.",
    "The date stays relative, Thursday the 17th, 14:00, month unstated, because the input carries no call date and a weekday with a day of the month does not fix a month; no timezone is stated.")
k['traps'][17] = sub(k['traps'][17],
    "Thursday the seventeenth fits 17 September 2026 (1 September 2026 is a Tuesday) with the call earlier that month;",
    "Thursday the seventeenth stays relative (Thursday the 17th, 14:00, month unstated): the input carries no call date and a weekday with a day of the month does not fix a month;")
c = k['commitments_and_next_steps']
c[0]['date'] = "Thursday the 17th, 14:00, month unstated (the input carries no call date; timezone unstated)"
c[7]['date'] = "Before Thursday the 17th (month unstated)"
c[9]['date'] = "Before Thursday the 17th (month unstated)"

# s21 standing line: the walkthrough is committed, the MD not yet invited -------------------------
c[0]['what'] = ("Walkthrough of a first version built from the export, forty-five minutes; the MD to be invited (Tamsin forwards the invite and chases him this week; his attendance is unconfirmed). Committed on the call; the invite is not yet sent.")

# direction rename ---------------------------------------------------------------------------
th = k['intake']['type_header']
new_th = {}
for kk, v in th.items():
    new_th[{'direction_of_show': 'direction', 'direction_of_show_note': 'direction_note'}.get(kk, kk)] = v
k['intake']['type_header'] = new_th
k['intake']['type_segments'] = [{('direction' if kk == 'direction_of_show' else kk): v for kk, v in seg.items()} for seg in k['intake']['type_segments']]
assert 'direction_of_show' not in json.dumps(k)

# ---- readiness --------------------------------------------------------------------------------
# pains: the key's own 13 entries, numbered by theme in array order
ids = ['P1.1', 'P1.2', 'P1.3', 'P1.4', 'P1.5', 'P2.1', 'P2.2', 'P2.3', 'P2.4', 'P2.5', 'P3.1', 'P3.2', 'P1.6']
one_screen = Q(342, "Phone goes, I open one screen, I see the job, I see it says out Thursday, I say Thursday, I hang up.")[0]
no_walk = Q(345, "Nobody walks into my lab to ask where something is.")[0]
list_with_name = Q(364, "If there's a list of on hold with a name on it, someone rings.")[0]
bakery = Q(362, "If that existed the bakery thing doesn't happen.")[0]
monday_view = Q(347, "And I open something on a Monday morning that shows me the retail account's turnaround for last week without a spreadsheet and without me.")[0]
see_status = Q(294, "If I could see status I could see turnaround.")[0]
outcomes = {'P1.1': one_screen, 'P1.2': one_screen, 'P1.3': no_walk, 'P1.4': one_screen, 'P1.5': None,
            'P2.1': list_with_name, 'P2.2': list_with_name, 'P2.3': bakery, 'P2.4': list_with_name, 'P2.5': None,
            'P3.1': monday_view, 'P3.2': see_status, 'P1.6': None}
pains = []
for pid, p in zip(ids, k['pains']):
    # prove the key's own quote once more at its location
    m = re.match(r'^L(\d+)', p['location']); n = int(m.group(1))
    assert p['quote'] in units[n][2], (pid, p['location'])
    pains.append({
        'id': pid, 'quote': p['quote'], 'location': p['location'],
        'speaker_role': role_of_location(p['location']),
        'stated_or_excavated': 'excavated' if '(excavated)' in p['theme'] else 'stated',
        'outcome': outcomes[pid],
    })

def sig(n, text, pain, nc):
    q, loc = Q(n, text)
    return {'quote': q, 'location': loc, 'pain': pain, 'not_confirmed': nc}
signals = [
    sig(362, "If that existed the bakery thing doesn't happen.", 'P2.3',
        "said inside our sketch frame about a sketch row; whether the on-hold list as built is what she means, and what it must show, was never confirmed outside the frame; nothing has been shown yet"),
    sig(459, "That's the one I'd build first.", 'P2.1',
        "what the list must show for him, who sets the name at Normanton and at Carlisle, and whether 'first' means before the Jobs board; never asked"),
    sig(433, "Ideally I've got something to show the retail people in January, because their technical team wants to see it before they sign.", 'P1.1',
        "what the retail account's technical team needs to see, a walkthrough of the client's own board or a view of their own jobs; relayed from the account, never heard from it"),
    sig(353, "That's my read. It's a good read.", 'P1.4',
        "that the MD counts renewal with the finding closed as the win; Tamsin's read, nothing heard from him"),
    sig(229, "And Carlisle. Renske can't see the whiteboard from Carlisle either.", 'P1.5',
        "that the hub person would use an urgents view and what she needs on it; nobody from the hub or reception was on the call"),
]

def ent(name, parent, moves, shared, stale, source, n=None, note=None):
    e = {'name': name if not note else f'{name} ({note})', 'parent': parent, 'moves_independently': moves,
         'shared_resource': shared, 'goes_stale': stale, 'source': source, 'evidence': L(n) if n else None}
    return e
entities = [
    ent('job', None, 'yes', False, False, 'spoken', 97, 'the lab system record for one sample plus its tests'),
    ent('sample', 'job', 'no', False, True, 'spoken', 249, 'one sample is one job; a micro sample has a shelf life'),
    ent('test', 'job', 'yes', False, False, 'spoken', 99, 'scheduled off the job; micro starts the same day, chem can wait; results arrive as they come'),
    ent('report', 'job', 'yes', False, False, 'spoken', 123, 'generated after authorisation; a job can have two'),
    ent('chain of custody form', 'sample', 'no', False, True, 'spoken', 269, "paper, filled in by the customer; a bakery copied last month's form"),
    ent('status code (INC, AUTH)', 'job', 'no', False, True, 'spoken', 166, "the lab system's own value; the board's copy is as of the nightly export, not live"),
    ent('due', 'job', 'yes', False, True, 'spoken', 139, "Dara's judgement, not in the lab system; a promised Thursday became Friday"),
    ent('on-hold state', 'job', 'yes', False, True, 'spoken', 105, 'set at reception when the form is incomplete, cleared when the customer answers; the sample waits in the fridge and expires'),
    ent('on-hold owner', 'on-hold state', 'yes', False, False, 'assumed', 156, "who rings the customer; nobody's today"),
    ent('urgent flag', 'job', 'yes', False, True, 'spoken', 218, 'a customer says urgent; on the whiteboard and the spreadsheet, two lists that mostly agree'),
    ent('customer', None, 'yes', False, False, 'spoken', 30),
    ent('the retail account', 'customer', 'no', False, False, 'spoken', 32, 'one customer, a fifth of revenue, unnamed on the call'),
    ent('site (Normanton, Carlisle)', 'job', 'no', False, False, 'spoken', 25, 'two sites; whether the export carries it is open'),
    ent('discipline (micro, chem)', 'test', 'no', False, False, 'spoken', 100, 'different clocks; whether the export carries it is open'),
    ent('status call', 'job', 'yes', False, False, 'spoken', 193, 'about 420 a month logged for the retail account'),
    ent('void or re-test', 'job', 'yes', False, False, 'spoken', 256, "the outcome of a late hold; re-tests counted on Dara's budget"),
    ent('analyst', None, 'yes', True, False, 'spoken', 197, 'stops work to answer status questions; scheduled by the lab system; out of the first version'),
    ent('signatory', None, 'yes', True, False, 'spoken', 122, 'Dara, the quality manager or two seniors; the act stays in the lab system'),
    ent('the whiteboard', None, 'no', False, True, 'spoken', 142, 'urgents list in the lab office, wiped on Fridays; an artefact'),
    ent("Oisin's urgents spreadsheet", None, 'no', False, True, 'spoken', 143, 'the same list on his laptop; an artefact'),
    ent('the nightly export', None, 'no', False, True, 'spoken', 165, "the lab system's flat file, nightly, not live; an artefact"),
    ent("Tamsin's turnaround workbook", None, 'no', False, True, 'spoken', 160, 'rebuilt from the export every week; an artefact'),
    ent('the accreditation visit', None, 'yes', False, False, 'spoken', 81, 'second week of November, about three weeks notice; nothing changes in the lab that month'),
]

def lean(question, option, qs, condition, pattern):
    quotes, locs = [], []
    for n, t in qs:
        q, loc = Q(n, t); quotes.append(q); locs.append(loc)
    return {'question': question, 'option': option, 'quotes': quotes, 'locations': locs, 'condition': condition, 'pattern': pattern}
leanings = [
    lean("Is a job one row with one status and one due, or a parent with its tests as child rows?",
         "one row per job in v0.1, the client's unit of work and what the export lists; tests as child rows (parent-row-with-roll-up, the latest due and the count of tests not yet authorised on the parent) only if the export is per test or Dara wants a due per test",
         [(94, "So one sample, one job, but a job can have six tests."), (99, "And the tests are scheduled off the job."), (116, "Results go into the lab system as they come.")],
         "the export inspected (one row per job or per test) and Dara's answer on whether due is per job or per test",
         "one row where the call describes many"),
    lean("Where do site and discipline come from?",
         "both stay wanted (two sites; micro and chem run on different clocks); the export the client listed carries neither, so their source is open until the export is inspected, and they may have to be typed or derived",
         [(165, "The export's a flat file. Job number, customer, status code, dates in, dates done."), (25, "since the spring we've had a sample hub up in Carlisle, which is reception only"), (119, "Chem is five to ten.")],
         "the scrubbed export night, due Friday, inspected for the fields it carries",
         "an expected output the input cannot support"),
    lean("Are the on-hold reminder, the day-five warning and the urgents notifications agreed logic?",
         "no: candidates to confirm with the client, not expected v0.1 logic; 'day five' is when customers ring, not an internal deadline, and any warning that is wanted should key on Dara's typed due or the discipline's turnaround, since chemistry takes five to ten days and a flat day five would fire on chem jobs that are on time",
         [(206, "If a result's not out by day five, that customer rings us, every time, and if it's the retail account they ring Tamsin."), (119, "Chem is five to ten.")],
         "the client confirms each candidate on the 17th, with who is told and by what channel; until then none is built",
         "our framing labelled as the client's"),
    lean("How does the board show that a status is the export's last value and not the lab system's current one?",
         "an as-of date (the export's night) on the board and beside the status on every row; in v0.1 the board is one night's sample and says so; a status on the board is the export's copy, never evidence of the lab system's current state; until a scheduled import exists the turnaround view copies the spreadsheet the export lands in today",
         [(166, "It's not bad. It's just not live, right."), (372, "As long as nobody thinks it's true because it's on a screen.")],
         "Joost's answer on a scheduled import and its frequency, with the vendor's acceptance of reading the export in writing",
         "an artefact that can go stale with nothing to flag it"),
    lean("What flags a typed due that has passed while the job is not authorised?",
         "due carries who typed it and when; a view of jobs past their typed due and not yet authorised; nothing derives or moves the due",
         [(212, "They held a tanker on our result for a day and a half because we told them Thursday and it was Friday."), (367, "Due is a judgement."), (461, "Don't derive it.")],
         "Dara confirms she wants the view and says who may type due besides her; until then due is typed by her or blank, and the workaround still rests on one person",
         "an artefact that can go stale with nothing to flag it"),
    lean("What does the on-hold list show about how old a hold is, and who owns it?",
         "date in from the export and the age in days, oldest first, with the micro shelf life made visible once discipline has a source; a name against each hold, which is the client's ask; a rung step, which is ours from the play-back and records a person's act",
         [(249, "And by Friday a micro sample from Tuesday is out of date."), (364, "If there's a list of on hold with a name on it, someone rings."), (282, "Carlisle logs it as on hold and the fridge is two hours up the road.")],
         "discipline's source (leaning 2), and Oisin's confirmation of the rung step and of who sets the name at Normanton and at Carlisle",
         "an artefact that can go stale with nothing to flag it"),
    lean("How are the retail account's rows found in an export whose customer names are scrubbed?",
         "ask Joost to replace each customer name with a stable code or pseudonym before sending, so the retail account's jobs can be filtered without naming it; otherwise the turnaround view in v0.1 runs over all jobs and says so",
         [(34, "A supermarket group, yeah. I'd rather not name them on a recording, if that's all right."), (347, "And I open something on a Monday morning that shows me the retail account's turnaround for last week without a spreadsheet and without me.")],
         "what the scrubbed export carries in its customer field",
         "an expected output the input cannot support"),
    lean("How is the audit finding, no visibility of sample status for the customer, met?",
         "not in the first version, by the client's choice; the need stays open with the February renewal as its clock and a January showing to the retail technical team before it; how it is met is open (a customer-facing status later, a report, or something else); the roadmap defers the portal, not every way of showing a customer a status; flagged to the user, never dropped",
         [(64, "And one of the findings, in writing, was that we. have no visibility of sample status for the customer. That's a quote. No visibility."), (350, "The retail account renews in February with that audit finding closed. That's the win."), (457, "Customers don't see anything in the first version.")],
         "the MD has seen the first version, and the retail technical team says what it needs to see in January (question 4)",
         "a pain with no element that fixes it"),
    lean("Does anything in the first version reach form quality at intake?",
         "no element; the hold reason ('form incomplete') on the job lets the hold rate by cause be counted later; the paper form and the customer stay as they are",
         [(90, "Test code, sample type, a date. And a quarter are, honestly, handwriting."), (269, "Sent twelve samples up through the hub, four of them had the wrong test code because they'd copied last month's form.")],
         "the client asks for it; nothing on the call did",
         "a pain with no element that fixes it"),
    lean("Is anything in the first version aimed at the client-services retention risk?",
         "no element; the two-minute call from one screen (P1.2) is the only bearing; the remark is internal by the client's marking and never leaves the record",
         [(238, "And I lose one of my two."), (239, "Because nobody wants to answer that phone for a living.")],
         "none; revisited only if the client raises it outside an internal remark",
         "a pain with no element that fixes it"),
]

epp = [
    ('P1.1', "Jobs board: status column with readable labels mapped from the export codes and the due column typed by Dara, with the as-of date beside the status (leaning 4)", 'fixes'),
    ('P1.2', "one screen for client services: the job's row with its status and typed due", 'fixes'),
    ('P1.3', "the same row answers the question, so fewer walks into the lab; the analysts never touch the board", 'fixes'),
    ('P1.4', "the same board visible to Tamsin, so an escalation reads the row instead of ringing Dara", 'fixes'),
    ('P1.5', "urgents view visible from Carlisle in place of the whiteboard; due is still typed by Dara alone in v0.1, so when she is out nothing is typed (leaning 5)", "copies-today's-tool"),
    ('P2.1', "on-hold list with a name against each hold", 'fixes'),
    ('P2.2', "on-hold list ordered by date in with the age in days; a reminder is a candidate, not built (leaning 3)", 'fixes'),
    ('P2.3', "on-hold list showing age and, once discipline has a source, the micro shelf life (leaning 6)", 'fixes'),
    ('P2.4', "rung step on the on-hold list, the record of a person's act; the customer is still told by phone", 'fixes'),
    ('P2.5', "none; the hold reason on the job counts the cause (leaning 9)", 'none'),
    ('P3.1', "turnaround view off the Jobs board rows; in v0.1 built on one hand-loaded night, so it copies the spreadsheet the export lands in until a scheduled import exists (leaning 4)", "copies-today's-tool"),
    ('P3.2', "status readable on the Jobs board, which is the client's own condition for seeing turnaround", 'fixes'),
    ('P1.6', "none aimed at it; the load reduction of P1.2 is the only bearing (leaning 10)", 'none'),
]
element_per_pain = [{'pain': a, 'element': b, 'verdict': v} for a, b, v in epp]

structure = {
    'products': ['Work Management'],
    'build_target': 'own-account',
    'build_target_reason': "prospect, so the user's own account by default (A21)",
    'workspaces': ['Marrowbeck – Ops'],
    'native_reuse': 'none: no CRM or Service entity (customers are a value on the job; status calls are answered from the Jobs board, not a ticket queue)',
    'leanings': leanings,
    'patterns': ["parent-row-with-roll-up: not applied in v0.1 (one row per job, the client's unit and the export's); held ready as job with tests as child rows, the latest due and the count of tests not yet authorised on the parent, if leaning 1 settles that way"],
    'element_per_pain': element_per_pain,
}

def inc(system, authority, n):
    return {'system': system, 'authority': authority, 'evidence': L(n)}
existing = {
    'account': "unknown, no account bound. The client side: one free trial board for the laptop list last year, lapsed with nothing in it (L169); whether that account still exists is not said; tier never stated; no products. Under A21 the build target is the user's own account, read at preflight; which account the client adopts, and who administers it, moves to handover.",
    'incumbents': [
        inc('the lab system', "stays system of record for: the job, its tests, status codes, dates in and done, authorisation and the report PDF; follower for: nothing. Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the lab system is our safe default, labelled as ours (the client's own constraint is no double entry, L413).", 97),
        inc('the nightly export', "stays system of record for: nothing (it is the lab system's copy as of last night); follower for: the Jobs board's feed, one scrubbed night by hand in v0.1", 165),
        inc('the whiteboard', "stays system of record for: urgents and due today; follower for: nothing; replaced by the urgents view, if anything is replaced", 142),
        inc("Oisin's urgents spreadsheet", "stays system of record for: the urgents he was told about; follower for: nothing; replaced by the urgents view", 143),
        inc("Tamsin's turnaround workbook", "stays system of record for: the retail account's weekly turnaround until a scheduled import exists; follower for: nothing", 160),
        inc('the shared inbox', "stays system of record for: reports sent; follower for: nothing; the send step is a question for the first version", 124),
        inc('the phone system log', "stays system of record for: status-call counts; follower for: nothing; one week pulled by Oisin as a one-off", 473),
        inc('chain of custody forms (paper)', "stays system of record for: what the customer asked for; follower for: nothing; not modelled", 85),
    ],
}

assumptions = [
    ("The export is one row per job.", "Is the nightly export one row per job or one per test?"),
    ("Site and discipline are typed or derived until the export shows them.", "Does the export carry site and discipline, or a test code they can be read from?"),
    ("The status codes map to a handful of labels client services can read.", "Which codes exist, and what should each read as on the board?"),
    ("Due is typed by Dara alone in v0.1 and shown blank otherwise.", "May the two seniors type due as well, and does Dara want a view of past-due jobs not yet authorised?"),
    ("The on-hold owner is a person column set at reception; at Carlisle, the hub person.", "Who rings the customer at Normanton and at Carlisle, and who owns a hub sample on hold?"),
    ("A rung step is wanted on the on-hold list.", "Does client services want 'rung' recorded, and what counts as rung?"),
    ("A customer code or pseudonym survives the scrubbing, so the retail account's rows can be picked out.", "Can the export replace names with stable codes before it is sent?"),
    ("The first version is loaded by hand from one night and its status is as of that night.", "Will Joost own a scheduled import, and at what frequency, given the export is nightly and the calls are hourly?"),
    ("The turnaround measure is date in to authorised, by week.", "Which measure does the retail account want, to authorised or to report sent, and for which lines?"),
    ("Reception, client services and Tamsin look at the first version; nobody in the lab does.", "Does anyone in the lab need to see it before December, and does the quality manager need to know what it is?"),
    ("The urgent flag is set by client services when a customer says urgent.", "Who marks a job urgent today, and can Dara mark one from the lab office without typing twice?"),
    ("The Carlisle hub person uses the same board filtered to hub jobs.", "Does the hub person want the same board filtered, and what does she need on it?"),
    ("Sample data is the scrubbed export night or invented jobs with invented customers; no participant's name as a fact.", "May the scrubbed night seed the first version, or only invented jobs?"),
    ("No automation is built in v0.1; the candidates are shown as a list.", "Which of the three candidates, if any, does the client want, and who is told?"),
]
assumptions = [{'statement': s, 'question': q} for s, q in assumptions]

unmet_needs = [
    {'need': "Customer visibility of sample status: the audit finding ('no visibility of sample status for the customer', L64), the client's central need",
     'clock': "the February renewal, with something to show the retail account's technical team in January (L433)",
     'why_not_met': "out of the first version by the client's choice ('Customers don't see anything in the first version.', L457); how it is met is open; the roadmap defers the portal, not every way of showing a customer a status; flagged to the user, never dropped"},
    {'need': "A board that is current: Oisin's calls are hourly and the export is nightly ('It's just not live, right.', L166)",
     'clock': None,
     'why_not_met': "v0.1 is one night of the export loaded by hand; a scheduled import is a question for Joost, and anything beyond the export is a question for the vendor; the as-of date says what the board is (leaning 4)"},
    {'need': "Fewer incomplete chain of custody forms at intake (P2.5)",
     'clock': None,
     'why_not_met': "nothing in the first version reaches the paper form or the customer; the on-hold list catches the hold rather than preventing it, and the client did not ask for more (leaning 9)"},
    {'need': "The client-services retention risk (P1.6, internal by the client's marking)",
     'clock': None,
     'why_not_met': "no element is aimed at it; the load reduction of the two-minute call is the only bearing; never in a recap or any client-facing output (leaning 10)"},
]

ai_opportunities = [
    {'pain_or_need': 'P2.2', 'kind': 'workflow', 'round': 2, 'probe_basis': 'P-21',
     'idea': "A workflow that tells the on-hold owner when a hold passes a day with no rung step recorded, once the client confirms the reminder as a candidate (leaning 3)."},
    {'pain_or_need': 'P1.1', 'kind': 'ai_column', 'round': 2, 'probe_basis': 'unprobed',
     'idea': "An AI column that turns the status label, the dates and the typed due into one plain sentence client services can read down the phone, without deriving due."},
    {'pain_or_need': 'P3.1', 'kind': 'agent', 'round': 2, 'probe_basis': 'P-19',
     'idea': "An agent that drafts the retail account's weekly turnaround summary from the board's rows for Tamsin to check on a Monday morning, internal only."},
    {'pain_or_need': 'unmet need: customer visibility (P1.1)', 'kind': 'vibe_app', 'round': 2, 'probe_basis': 'P-20',
     'idea': "Later, a customer-facing status page for the retail account's jobs, one way the audit finding could be met without the vendor's portal; not in the first version, by the client's choice."},
]

verdict = {
    'cleared_for': 'build',
    'conditions': [
        "approval stop",
        "no A11 decision bites: own-account target, so sample data needs no decision (A21); the three A11 decisions stay open",
        "workspace name confirmed at approval; creating a workspace is irreversible-class",
        "sample rows come from the scrubbed export night or are invented; no customer name and no participant's name as a fact (the sketch names are seed data only)",
        "the walkthrough is committed, not booked: the invite is to be sent on the day of the call and the MD's attendance is unconfirmed until Tamsin has chased him",
        "the candidate automations are shown as a list and none is created",
        "the board says it is one night's sample with its as-of date; no status on it is presented as the lab system's current state",
        "the customer-visibility need is shown to the user as open, with the February clock",
    ],
    'reason': "Two excavated pains with named entities (the job, the hold, the due) and wanted outcomes in the client's words, one product, a stated structure with its leanings and the user's own account as the target clear a first version; the lab stays out of it and the customer-facing need stays open.",
}

questions = [
    {'text': "You pointed at the on-hold list: 'If there's a list of on hold with a name on it, someone rings' and 'That's the one I'd build first.' Whose name goes on a hold at Normanton and at Carlisle, what counts as rung, and what must the list show for it to be the one you build first?",
     'kind': 'read-back', 'role': 'operations director and client services lead (the reception supervisor was not on the call)',
     'known': "reception in theory, whoever notices in practice (L108); the Friday check is a Normanton check (L283); the hub has one person with a login (L112-113); the name is the client's ask and the rung step is ours (L454)"},
    {'text': "The export: one row per job or per test; which status codes exist and what each should read as; whether site and discipline are in it or must be typed or derived; whether a customer code can replace the names so the retail account's rows can be picked out; and whether the vendor's acceptance of reading it is in writing.",
     'kind': 'discovery', 'role': 'systems',
     'known': "the fields as listed (L165); not live (L166); the export is the client's own and the vendor's position is spoken (L393-394); one scrubbed night due Friday (L379)"},
    {'text': "Due: typed by you only, or by the two seniors as well; shown blank until typed; do you want a view of jobs past their typed due and not yet authorised; and is the customer's day-five clock a separate column from your due?",
     'kind': 'discovery', 'role': 'lab manager',
     'known': "due is a judgement in her head and on the whiteboard (L139, L367-368); typed by her or not shown, never derived (L460-461); day five is when customers ring (L206)"},
    {'text': "You said the retail account's technical team wants to see it before they sign, in January. What do they need to see: a walkthrough of your board, or a view of their own jobs? Nothing customer-facing is in the first version by your choice; what closes the finding is still open.",
     'kind': 'read-back', 'role': "operations director; the MD, since the retail account is his relationship",
     'known': "the finding in writing (L64); renewal in February (L66); January showing (L433); customers see nothing in the first version (L457); the vendor's portal is a slide (L429-430); the retail account refused a spreadsheet as visibility (L423-425)"},
    {'text': "Notifications, as candidates: do you want any reminder when a hold passes a day; should a warning key on Dara's typed due rather than a flat day five, given chem takes five to ten days; who is told when an urgent changes, and by what channel?",
     'kind': 'discovery', 'role': 'client services lead and lab manager',
     'known': "none was agreed on the call; day five is when customers ring (L206); chem is five to ten days (L119); micro three to five (L117)"},
]

readiness = {
    'schema': 'readiness/1',
    'note': "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top).",
    'pains': pains,
    'signals': signals,
    'entities': entities,
    'structure': structure,
    'existing': existing,
    'assumptions': assumptions,
    'unmet_needs': unmet_needs,
    'ai_opportunities': ai_opportunities,
    'verdict': verdict,
    'questions': questions,
}
k['readiness'] = readiness

# sales vocabulary check on the block
blob = json.dumps(readiness, ensure_ascii=False)
for w in [r'\bR\d{1,2}\b', r'\bgate', r'Discovery complete', r'Nearly ready', r'Not ready', r'\bgrade', r'\bmet-with-residual', r'\bnot-obtainable', r'\bpartial\b', r'\bmissing\b', r'\bverdict:']:
    hits = re.findall(w, blob)
    assert not hits, (w, hits)

# write
out = keystyle.dumps(k, deep=('readiness',))
json.loads(out)  # valid
open(KEY, 'w', encoding='utf-8', newline='\n').write(out)
print('written; new quote proofs', proofs, '; lines', out.count('\n'), '; fields', len(k), list(k)[-2:])
print('counts: pains', len(pains), 'signals', len(signals), 'entities', len(entities), 'leanings', len(leanings),
      'epp', len(element_per_pain), 'incumbents', len(existing['incumbents']), 'assumptions', len(assumptions),
      'unmet', len(unmet_needs), 'ai', len(ai_opportunities), 'questions', len(questions))
