"""s25-client-documents fix pass: load, change, dump. Run from anywhere with python3 -I.
Writes the key only after every new call quote is proven verbatim at its unit and the readiness
block is scanned for sales vocabulary. The renderer keeps the file's own layout."""
import json
import re
import sys
from collections import OrderedDict

sys.path.insert(0, '/Users/caramelm4/DelOps/rebuild-workspace/fixtures-work/_fixpass/s25-client-documents')
import render  # noqa: E402

FIX = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s25-client-documents/'
KEY = FIX + 'answer-key.json'

raw = open(KEY, encoding='utf-8').read()
expanded = render.layout(raw)
d = json.loads(raw, object_pairs_hook=OrderedDict)
assert render.dumps(d, expanded) == raw, 'round trip failed before any change'
assert list(d.keys())[-1] == 'intake' and len(d) == 26

# ---------------------------------------------------------------- transcript, for proofs
units = {}
for line in open(FIX + 'transcript.txt', encoding='utf-8').read().splitlines():
    m = re.match(r'\[(\d\d:\d\d:\d\d)\] ([^:]+): (.*)$', line)
    units[m.group(1)] = (m.group(2), m.group(3))
ROS = 'Rosalind Okonjo (Sample Reception Coordinator)'


def at(ts, who=ROS):
    return '%s %s' % (ts, who)


def prove(quote, loc):
    ts = loc[:8]
    if ts in units:
        sp, tx = units[ts]
        assert quote in tx, 'NOT VERBATIM at %s: %r' % (loc, quote)
        label = 'Consultant' if sp == 'Consultant' else ROS
        assert loc == at(ts, label), 'label mismatch %s' % loc
    return quote


proofs = []


def Q(quote, loc):
    proofs.append((quote, loc))
    return prove(quote, loc)


# ---------------------------------------------------------------- 1. direction rename
th = d['intake']['type_header']
new_th = OrderedDict()
for k, v in th.items():
    new_th['direction' if k == 'direction_of_show' else k] = v
d['intake']['type_header'] = new_th
assert 'direction_of_show' not in json.dumps(d)

# ---------------------------------------------------------------- 2. sweep corrections
voc = {e['their_term']: e for e in d['vocabulary']}
assert voc['multi-test']['likely_monday_object'] == 'the tests-requested column holding several values; no separate object'
voc['multi-test']['likely_monday_object'] = (
    "one child row per test under the sample (readiness, leaning 1), each with its bench, its status and its due "
    "date; the sample's status rolls up from them; the fallback, if nearly every sample carries one test, is a "
    "bench per test column on the one row")
assert voc['bench']['likely_monday_object'] == 'a status or dropdown column for the allocated bench, and a view per bench; never a People column'
voc['bench']['likely_monday_object'] = (
    "a status or dropdown column on each test row for its bench (readiness, leaning 1), and a view per bench of the "
    "tests allocated to it in priority order; never a People column")
assert voc['re-test (QF-12)']['likely_monday_object'].startswith('a re-test status with the authorisation number as a column (W-7)')
voc['re-test (QF-12)']['likely_monday_object'] = (
    "a re-test status on the test row with the authorisation number as a column (W-7); the paper form stays until "
    "the Laboratory Manager says otherwise")

es = d['expected_structures']
old_notes_start = ("One product, one board of samples with the register's fields as columns, a status from receipt to "
                   "certificate, a bench column with a view per bench in priority order, a priority flag with a notification "
                   "(on the approval list), a re-test status with the authorisation number, dates for results entered, "
                   "checked, prepared and signed, and turnaround measured against section 6.5. ")
assert es['notes'].startswith(old_notes_start)
es['notes'] = (
    "One product, one board of samples with the register's fields as columns and one child row per test requested "
    "(purity, germination, moisture, vigour), each child with its bench, its status and its due date under section 6.5, "
    "the sample's status and its latest due date rolling up (readiness, leaning 1); a view per bench of its tests in "
    "priority order; a priority flag on the sample with a notification (on the approval list), shown on every child; "
    "a re-test status with the authorisation number on the test row; dates for results entered, checked, prepared and "
    "signed, each a person's claim about the bench sheet, the database or the paper certificate and never evidence "
    "from them; and turnaround measured against section 6.5 per test. "
) + es['notes'][len(old_notes_start):]

# never-written rule
im = d['integrations_mentioned']
assert im[0].endswith('never a write, and never a copy of the results into the platform as the record.')
im[0] = ("The results database: the validated system of record for results; results are entered there by the analysts "
         "and must stay there ('cannot be replaced or altered', write-up p.2 section 3; 'it can't be the place results "
         "live', 00:12:03); the certificate draft needs a read from it in a form to be agreed (an export, a report or "
         "read access), and never a copy of the results into the platform as the record. No client line addresses a "
         "write from the platform into the database: writeback and integration direction unresolved; v0.1 does not "
         "depend on either; staying clear of the results database is our safe default, labelled as ours.")
rc = d['requested_changes'][0]
assert rc['description'].endswith('is read, never replaced or written to.')
rc['description'] = ("Pre-build requirement from the write-up (no build exists yet): the results database stays the system "
                     "of record for results and is never replaced or altered (the client's words). Writeback and "
                     "integration direction unresolved; v0.1 does not depend on either; staying clear of the database "
                     "is our safe default, labelled as ours.")
tr = d['traps']
assert tr[26].startswith('The results database stays: never rebuild results inside the platform, never write to it,')
tr[26] = ("The results database stays and cannot be replaced or altered (the client's document): never rebuild results "
          "inside the platform. Writeback and integration direction unresolved; v0.1 does not depend on either; staying "
          "clear of the database is our safe default, labelled as ours. The certificate is a draft for signature under "
          "section 6.4, never issued automatically.")
assert tr[19].endswith('the alias map lists them as benches.')
tr[19] = tr[19][:-len('the alias map lists them as benches.')] + 'the alias map lists each as a bench, one entry per bench.'

# alias map: one entry per entity
am = d['intake']['alias_map']
assert am[9]['canonical'] == 'purity / germination / moisture and vigour'
assert am[10]['canonical'] == 'the assessor'
assert am[2]['canonical'] == 'Marguerite (Laboratory Manager)'
am[2]['note'] = ("mentioned only, absent; surname never given anywhere; the SOP names the role and the call the name, "
                 "and the two are bound by us: by elimination from the signatory rule of section 6.4 (the Laboratory "
                 "Manager or the Quality Manager signs; the Quality Manager is the SOP's author; 'Marguerite, mostly. "
                 "Annelise if Marguerite's off.', 00:08:50), never stated on the call; confirmed on the 9th or not at "
                 "all; also does the allocation the SOP gives the Laboratory Supervisor")


def alias(canonical, forms, side, note):
    return OrderedDict([('canonical', canonical), ('forms', forms), ('side', side), ('note', note)])


benches = [
    alias('the purity bench', ['purity', "whoever's on purity"], 'bench, not a person',
          "an ordinary word in a name slot ('told purity', 'whoever's on purity'); never coerced into a name; "
          "one entry per bench (fix pass sweep, alias pattern)"),
    alias('the germination bench', ['germination', 'the germinator'], 'bench, not a person',
          "an ordinary word in a name slot ('nobody on germination knew'); 'the germinator' is the apparatus at this "
          "bench, where a sample sits during the seven-day test; never coerced into a name"),
    alias('the moisture and vigour bench', ['the moisture and vigour bench', 'the moisture ones'], 'bench, not a person',
          "named only in QP-07 section 2.1; on the call only its samples ('the moisture ones go in the sealed bit "
          "at the back', 00:02:42); never a person"),
]
third = [
    alias('the assessor', ['the assessor'], 'third party', "role only; the person who asked to see where a sample "
          "was at the surveillance visit in May; never named"),
    alias('the accreditation body', ['the accreditation'], 'third party',
          "the organisation behind the surveillance visits; named only through 'the accreditation' (write-up p.2 "
          "section 3) and 'the audit' (00:07:53); the visit and the finding are events, not forms of its name"),
]
d['intake']['alias_map'] = am[:9] + benches + third
assert len(d['intake']['alias_map']) == 14

# ---------------------------------------------------------------- 3. the readiness block
pains_src = d['pains']
ids = ['P1.1', 'P1.2', 'P1.3', 'P1.4', 'P1.5', 'P2.1', 'P2.2', 'P2.3', 'P3.1', 'P4.1']
roles = {'write-up': "the client's document (the write-up, author unknown)", 'call': 'Sample Reception Coordinator (the operator)'}
stated = {'P1.1': 'stated', 'P1.2': 'excavated', 'P1.3': 'excavated', 'P1.4': 'excavated', 'P1.5': 'excavated',
          'P2.1': 'stated', 'P2.2': 'stated', 'P2.3': 'excavated', 'P3.1': 'stated', 'P4.1': 'stated'}
OUT_WALK = Q("I don't walk. [laughs] I look at a screen and I can tell Marlowe's where their sample is without getting up.", at('00:10:46'))
OUT_PRI = Q("And the priority thing is visible, so when I say it's urgent, germination knows it's urgent, not just purity.", at('00:10:46'))
OUT_CERT = Q("And I don't type the certificate.", at('00:10:46'))
OUT_W6 = "with a sample shown before it is late rather than after"
outcomes = {'P1.1': OUT_WALK, 'P1.2': OUT_WALK, 'P1.3': OUT_PRI, 'P1.4': OUT_PRI, 'P1.5': OUT_W6,
            'P2.1': OUT_CERT, 'P2.2': OUT_CERT, 'P2.3': OUT_CERT, 'P3.1': None, 'P4.1': OUT_WALK}
pains = []
for pid, p in zip(ids, pains_src):
    src = 'write-up' if p['location'].startswith('write-up') else 'call'
    if src == 'call':
        prove(p['quote'], p['location'])
    pains.append(OrderedDict([('id', pid), ('quote', p['quote']), ('location', p['location']), ('speaker_role', roles[src]),
                              ('stated_or_excavated', stated[pid]), ('outcome', outcomes[pid])]))

signals = [
    OrderedDict([('quote', Q("Can it tell Marguerite when I flag something? Because that's the whole thing, really, for me.", at('00:13:45'))),
                 ('location', at('00:13:45')), ('pain', 'P1.3'),
                 ('not_confirmed', "our side answered with a platform claim (00:13:51) and never confirmed that a notification to the Laboratory Manager is the mechanism she needs, or whether an approval sits behind the flag")]),
    OrderedDict([('quote', Q("If it just did the register and the where-is-it, that'd be most of it for me.", at('00:13:23'))),
                 ('location', at('00:13:23')), ('pain', 'P1.1'),
                 ('not_confirmed', "our side said 'Noted' and moved to turnaround; the register-first scope was never confirmed back to her, and never with the owner")]),
    OrderedDict([('quote', Q("The certificate thing would be lovely.", at('00:13:23'))),
                 ('location', at('00:13:23')), ('pain', 'P2.2'),
                 ('not_confirmed', "what 'the certificate thing' needs (a read from the results database) was never said to her; she may expect the typing to go in the first version")]),
    OrderedDict([('quote', Q("Annelise will want the turnaround numbers, she's asked for them twice.", at('00:13:23'))),
                 ('location', at('00:13:23')), ('pain', 'P1.5'),
                 ('not_confirmed', "relayed; the Quality Manager has not said it, and what numbers she wants (per test, per bench, per month) was never asked")]),
    OrderedDict([('quote', Q("Turnaround, probably. He gets the complaints. And the audit finding closed, Annelise would say that.", at('00:11:11'))),
                 ('location', at('00:11:11')), ('pain', 'P4.1'),
                 ('not_confirmed', "the operator's guess at the Director's and the Quality Manager's win; neither has spoken, and our side did not ask her what the finding says")]),
    OrderedDict([('quote', Q("Realistically Annelise said before the visit. But that's her saying it, not me. Ask her.", at('00:11:46'))),
                 ('location', at('00:11:46')), ('pain', 'P4.1'),
                 ('not_confirmed', "the clock is relayed and hedged; the date of the visit and whether closing the finding is the deadline were never confirmed")]),
]


def ent(name, parent, moves, shared, stale, source, evidence):
    return OrderedDict([('name', name), ('parent', parent), ('moves_independently', moves), ('shared_resource', shared),
                        ('goes_stale', stale), ('source', source), ('evidence', evidence)])


entities = [
    ent('Sample (one quantity of seed, identified by its sample number)', None, 'yes', False, False, 'documented', 'QP-07 section 2.1'),
    ent('Test (one per test requested on a sample: germination, purity, moisture or vigour)', 'Sample', 'yes', False, False, 'spoken', at('00:06:03')),
    ent('Re-test (a repeat of one test, authorised on QF-12)', 'Test', 'yes', False, False, 'documented', 'QP-07 section 4.3'),
    ent('Priority request (a flag on the sample that must show on every test)', 'Sample', 'no', False, False, 'documented', 'QP-07 section 4.2'),
    ent('Test request (QF-03, the paper form that comes with the sample)', 'Sample', 'no', False, False, 'documented', 'QP-07 section 2.1'),
    ent('Submitter (merchant, co-operative, breeder or private grower)', None, 'yes', False, False, 'documented', 'QP-07 section 2.1'),
    ent("The Harrowfield growers' co-operative (a submitter)", 'Submitter', 'yes', False, False, 'spoken', at('00:07:17')),
    ent("Marlowe's (a seed merchant, a submitter)", 'Submitter', 'yes', False, False, 'spoken', at('00:04:01')),
    ent('Bench (three: purity; germination; moisture and vigour), each with its own analysts and its own queue', None, 'yes', True, False, 'documented', 'QP-07 section 2.1'),
    ent('The germinator (the apparatus at the germination bench where a sample sits for the seven-day test)', 'Bench', 'unknown', True, False, 'spoken', at('00:03:03')),
    ent('Bench sheet (the paper record of one test)', 'Test', 'no', False, False, 'documented', 'QP-07 section 2.1'),
    ent('Result (entered from the bench sheet into the results database; never on the platform)', 'Test', 'yes', False, False, 'documented', 'QP-07 section 5.3'),
    ent('Results database (the validated system of record; an incumbent)', None, 'yes', False, False, 'documented', 'write-up p.2 section 3'),
    ent('Certificate (prepared by reception, signed by an authorised signatory, sent to the submitter)', 'Sample', 'yes', False, True, 'documented', 'QP-07 section 6.3'),
    ent('Due date per test (21 or 10 days from receipt by test, 7 once a priority is approved)', 'Test', 'yes', False, True, 'documented', 'QP-07 section 6.5'),
    ent('Sample register (the spreadsheet on the shared drive; replaced by the board)', None, 'no', False, True, 'spoken', at('00:01:43')),
    ent('Day book (the paper book written first; not in the procedure)', None, 'no', False, False, 'spoken', at('00:01:43')),
    ent("Bench allocation sheet (the previous day's register printed, the bench written on in biro)", None, 'no', False, True, 'spoken', at('00:02:14')),
    ent('Receipt store (the locked cupboard, with a sealed section for moisture samples)', None, 'no', True, False, 'spoken', at('00:02:42')),
    ent('Surveillance visit and the finding about the register (the why-now trigger)', None, 'unknown', False, False, 'spoken', at('00:07:53')),
    ent('Laboratory Supervisor (a title in QP-07; nobody named on the call; the Laboratory Manager allocates in practice)', None, 'unknown', False, False, 'documented', 'QP-07 section 4.1'),
]


def lean(question, option, quotes, locations, condition, pattern):
    for q, l in zip(quotes, locations):
        if re.match(r'\d\d:\d\d:\d\d', l):
            prove(q, l)
    proofs.extend(zip(quotes, locations))
    return OrderedDict([('question', question), ('option', option), ('quotes', quotes), ('locations', locations),
                        ('condition', condition), ('pattern', pattern)])


leanings = [
    lean("Is a sample one row with one bench and one status, or a parent with one child row per test?",
         "A child row per test requested, each with its bench, its status and its due date under section 6.5 (7 days once a priority is approved); the sample's status and its latest due date roll up; the priority flag sits on the sample and shows on every child. One row with one bench column is the register's own flaw: a multi-test sample is on two benches at once, and in September purity finished the day it arrived while germination queued for a week.",
         ["Fifteen if it's a multi-test.",
          "And purity was fine, purity did it that day. But germination's a seven-day test and nobody on germination knew it was urgent, so it went in the normal queue, and it came out the Thursday after.",
          "Certificates are normally issued within 21 days of receipt for germination and vigour tests and within 10 days of receipt for purity and moisture tests."],
         [at('00:09:31'), at('00:06:03'), 'QP-07 section 6.5'],
         "The Laboratory Manager confirms on the 9th that a multi-test sample is worked by more than one bench at the same time and says how many samples a day carry more than one test; if nearly every sample is single-test, one row with a bench per test column is the fallback.",
         "one row where the call describes many"),
    lean("Who sets a test's status at the bench, when the analysts will not touch a screen?",
         "The Laboratory Manager's morning allocation sets each test's bench and 'allocated' on the board; 'started' and 'results entered' are set by the one analyst who will touch a screen or on a shared screen at the bench; reception never keys a bench status she learned by walking, because that would be today's walk with a board in front of it. Any status a person sets is that person's claim; the bench sheet and the results database stay the evidence.",
         ["The analysts have got seed dust on their hands all day, they're not going to touch a screen. Tobiah will, the others won't.",
          "Analysts must not need a keyboard at the bench while they are handling seed."],
         [at('00:12:03'), 'write-up p.2 section 3'],
         "The Laboratory Manager's answer on the 9th: a scan, a shared screen at the bench, the morning sheet, or herself alone; until then no bench view is shown as live.",
         "a pain with no element that fixes it"),
    lean("Does an approval step sit behind the priority flag, and whose is it?",
         "The priority flag on the sample with a notification to the Laboratory Manager is built; the approval step is built neither way. If the 9th settles on the procedure, the approval becomes a status the Laboratory Manager sets on the sample (W-3) and the 7-day target starts from it; if it settles on reception's route, the flag alone, with the notification as the Laboratory Manager's sight of it.",
         ["A priority request is approved by the Laboratory Manager before the sample is allocated.",
          "That box on the form? Nobody uses it.",
          "It doesn't happen. I mean, it's in the procedure, and Annelise wrote the procedure, so it's not that nobody knows it's there.",
          "Priority requests approved by the Laboratory Manager on screen, not on the form, and visible to every bench the same day."],
         ['QP-07 section 4.2', at('00:04:01'), at('00:04:25'), 'write-up p.1 section 2, W-3'],
         "The Quality Manager and the Laboratory Manager together on the 9th, asked as the procedure against reception, never as the operator's report.",
         "fork"),
    lean("Can the certificate be prepared from recorded results in the first version?",
         "Not yet. The certificate stage is a status with prepared, signed and sent dates; no result is held on the platform; the draft from recorded results waits for a read from the results database (an export, a report or read access) that nobody has described or granted. Until then the template is typed as today, and the structure copies today's tool for the three P2 pains.",
         ["And the certificate is me, typing, from the database into the template.",
          "The certificate prepared from recorded results without re-typing, ready to sign.",
          "Results entered once. The results database stays the system of record for results."],
         [at('00:08:36'), 'write-up p.1 section 2, W-5', 'write-up p.1 section 2, W-4'],
         "What can be read from the results database, how, and who grants it (the Quality Manager); whether a draft for signature is acceptable under section 6.4 and to the accreditation body.",
         "a pain with no element that fixes it"),
    lean("What happens to a prepared certificate draft when a result changes after it?",
         "The draft carries the date of the results it was prepared from; a later results-entered or re-test date on any of the sample's tests resets 'prepared' and shows a reissue. By the procedure a re-test precedes any certificate, but the June reissue shows a certificate can be wrong after it is signed.",
         ["Where a result falls outside the tolerance for the test, a re-test is authorised under section 4.3 before any certificate is prepared.",
          "The merchant rang, we reissued."],
         ['QP-07 section 6.2', at('00:09:00')],
         "Whether a correction or a re-test can follow a prepared draft in practice, and how a reissue is recorded today (the Laboratory Manager).",
         "an artefact that can go stale with nothing to flag it"),
    lean("Does the bench's daily list go stale the way the printed allocation sheet does?",
         "The daily list per bench is a live view of its tests in priority order (W-8), and the priority notification goes to a named person per bench, so a priority that arrives after the morning allocation reaches the bench without a reprint. If a bench works from paper, the print carries its time and the notification is the only flag that it is out of date.",
         ["She prints it. Prints the previous day. That's the allocation sheet, basically, she writes the bench on the printout.",
          "Marguerite finds out when she sees it on the list. If she looks.",
          "A daily list for each bench of the samples allocated to it, in priority order."],
         [at('00:02:14'), at('00:04:01'), 'write-up p.1 section 2, W-8'],
         "Whether each bench has a screen it will look at during the day (leaning 2), and who at each bench is named on the notification.",
         "an artefact that can go stale with nothing to flag it"),
    lean("Who owns the allocation view and the approvals: the Laboratory Supervisor of the procedure or the Laboratory Manager of the call?",
         "Marguerite is taken to be the Laboratory Manager, by our elimination from the signatory rule of section 6.4, never by anyone's statement, and she does the allocation the procedure gives the Supervisor; the owner of the allocation view and the approver are left unnamed in the structure until confirmed.",
         ["Each morning the Laboratory Supervisor takes the samples received on the previous working day from the receipt store and allocates them to the benches in order of receipt.",
          "Marguerite, mostly. Annelise if Marguerite's off.",
          "Marguerite does allocation in the morning so afternoons are better."],
         ['QP-07 section 4.1', at('00:08:50'), at('00:14:24')],
         "The Quality Manager and the Laboratory Manager on the 9th: whether the two titles are one person or the Supervisor role is vacant.",
         "our framing labelled as the client's"),
]


def epp(pain, element, verdict):
    return OrderedDict([('pain', pain), ('element', element), ('verdict', verdict)])


element_per_pain = [
    epp('P1.1', "the Samples board with a child row per test, each with its bench and status, read on screen by reception, the benches and the Laboratory Manager (W-1); fixes once the bench marks its own progress (leaning 2); if reception keys what she learned by walking, it copies the walk", 'fixes'),
    epp('P1.2', "the same board and status per test, answered from the screen instead of the walk; the same condition on the bench's mechanism (leaning 2)", 'fixes'),
    epp('P1.3', "a priority flag on the sample with a notification to the Laboratory Manager, on the approval list; the approval step behind it built neither way before the 9th (leaning 3)", 'fixes'),
    epp('P1.4', "the sample's priority flag shown on every test row and in every bench's daily list, so the second bench sees what the first was told (leaning 1, leaning 6)", 'fixes'),
    epp('P1.5', "a due date per test from the receipt date and section 6.5, 7 days once a priority is approved, with the test shown before it is late (W-6) rather than counted at month end", 'fixes'),
    epp('P2.1', "nothing in v0.1 reduces the three writes: the bench sheet and the results database stay as they are, and the third write, the certificate, goes only once a read from the database exists (leaning 4)", "copies-today's-tool"),
    epp('P2.2', "the certificate stage as a status with prepared, signed and sent dates; the draft from recorded results waits for the read (leaning 4); until then the template is typed as today", "copies-today's-tool"),
    epp('P2.3', "the double check against the database goes only with the re-typing; the same dependency on the read (leaning 4)", "copies-today's-tool"),
    epp('P3.1', "the board replaces the spreadsheet file on the shared drive, so there is no file to corrupt; the paper day book stops only when the operator trusts the board, which is hers to say", 'fixes'),
    epp('P4.1', "the sample's status on screen answers 'where is it' in front of the assessor without a walk; whether that closes the finding depends on its wording, which nobody on the call had", 'fixes'),
]

structure = OrderedDict([
    ('products', ['Work Management']),
    ('build_target', 'own-account'),
    ('build_target_reason', "prospect, so the user's own account by default (A21)"),
    ('workspaces', ['Wexcombe \u2013 Ops']),
    ('native_reuse', "none: no CRM or Service entity; submitters are a name on the sample, and if the laboratory wants them tracked as accounts the native CRM Accounts and Contacts boards are used, never a Submitters look-alike"),
    ('leanings', leanings),
    ('patterns', ["parent-row-with-roll-up: sample with tests as child rows, the sample's status and its latest due date rolling up to the parent, the priority flag on the parent shown on every child"]),
    ('element_per_pain', element_per_pain),
])


def inc(system, authority, evidence):
    return OrderedDict([('system', system), ('authority', authority), ('evidence', evidence)])


existing = OrderedDict([
    ('account', "unknown, no account bound: nothing in the documents or the call names a monday account ('a login to something from her last place' is hearsay about a login); under A21 the first version goes into the user's own account, read at preflight, and the laboratory's own account is a handover question"),
    ('incumbents', [
        inc('Results database', "stays system of record for: every result and every certificate number; follower for: nothing. Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the database is our safe default, labelled as ours.", 'write-up p.2 section 3'),
        inc('Sample register (spreadsheet)', "stays system of record for: nothing once the board starts; follower for: history, if it is migrated, from a date to be agreed; until then the only record of receipts before the board.", at('00:01:26')),
        inc('Day book (paper)', "stays system of record for: the receipt as written at the door, by the operator's own rule; follower for: nothing; stops only when she trusts the board.", at('00:01:43')),
        inc('Certificate template (word-processing document)', "stays system of record for: the signed certificate that goes to the submitter; follower for: the draft's values, once a read exists; until then typed as today.", at('00:08:36')),
        inc('Paper forms QF-03 and QF-12 and the bench sheet', "stay system of record for: the test request, the re-test authorisation and the observations; follower for: nothing; the board carries their numbers and dates as a person's claim.", 'QP-07 section 4.3'),
        inc('Bench allocation sheet (printout)', "stays system of record for: nothing; replaced by the daily view per bench; a print of the view, if a bench needs paper, carries its time.", at('00:02:14')),
    ]),
])


def asm(statement, question):
    return OrderedDict([('statement', statement), ('question', question)])


assumptions = [
    asm("A sample with several tests is worked by more than one bench at the same time, so tests are child rows of the sample.", "Is a multi-test sample split across benches at the same time, and how many samples a day carry more than one test? (Laboratory Manager)"),
    asm("The one analyst who will touch a screen, or a shared screen at each bench, marks a test started and its results entered; reception never keys a bench status she learned by walking.", "How does each bench mark a test started, results entered and re-tested without a keyboard in hand? (Laboratory Manager)"),
    asm("The priority flag lives on the sample, notifies the Laboratory Manager and carries no approval step until the 9th settles one.", "Does an approval step exist, who owns it, and should the register carry the procedure's route or reception's? (Quality Manager and Laboratory Manager together)"),
    asm("The due date is the receipt date plus 21 days for germination and vigour, 10 for purity and moisture, and 7 once a priority is approved, as section 6.5 reads.", "Are the targets in section 6.5 the ones to measure against, and does the clock start at receipt or at allocation? (Quality Manager)"),
    asm("The certificate stage is a status with prepared, signed and sent dates; no result is held on the platform; the draft from recorded results waits for a read.", "What can be read from the results database, how, and who grants it? (Quality Manager)"),
    asm("A date or status a person sets on the board (allocated, results entered, checked, signed) is that person's claim; the bench sheet, the database and the paper certificate stay the evidence.", "Is a claim on the board enough for the Laboratory Manager's month-end check against the forms, or does the check stay on paper? (Laboratory Manager)"),
    asm("v0.1 carries invented sample data: no submitter name, no result, no lot reference and no certificate number from a real submitter.", "Which real-looking values, if any, may a demo show? (Quality Manager)"),
    asm("The spreadsheet's history is not migrated in v0.1; the board starts with new receipts.", "Is the register's history migrated, and from which date? (the operator, Quality Manager)"),
    asm("Submitters are a text or dropdown column on the sample; no CRM board exists in v0.1.", "Are merchants, co-operatives and breeders to be tracked as accounts with contacts? (Quality Manager)"),
    asm("The Laboratory Manager owns the allocation view and the approvals; the Supervisor title is hers or vacant.", "Is the Laboratory Supervisor of sections 4.1 and 5.4 the same person as the Laboratory Manager, or a vacant role? (Quality Manager, Laboratory Manager)"),
    asm("One workspace under Work Management in the user's own account; the laboratory's tier is unknown and nothing tier-dependent is designed.", "Once an account exists, which tier and how many seats, so anything tier-dependent is designed then? (Quality Manager)"),
    asm("The monthly summary (W-9) and the Director's whole picture (W-10) are a dashboard on the Samples board in a later version, agreed with him.", "What does the Laboratory Director want to see, how often, and does he want to be on the 9th? (Quality Manager, then the Director)"),
    asm("The paper test request (QF-03) and re-test request (QF-12) stay; the board carries their numbers and dates.", "Does the paper re-test form stay once the authorisation is raised on screen (W-7)? (Laboratory Manager)"),
    asm("The day book stops when the operator trusts the board; nothing removes it before then.", "What would make the operator trust the board enough to stop the book? (the operator)"),
]


def need(need_, clock, why):
    return OrderedDict([('need', need_), ('clock', clock), ('why_not_met', why)])


unmet_needs = [
    need("Results entered once (W-4; 'Bench analysts must not enter a result twice', write-up p.2 section 3)", None,
         "v0.1 touches neither the bench sheet nor the results database, so the two bench writes stay as today; only the certificate's write can go, and only with a read from the database."),
    need("A bench that needs no keyboard ('Analysts must not need a keyboard at the bench while they are handling seed', write-up p.2 section 3)", None,
         "a board needs a hand on a screen; a scan, a shared screen or the morning sheet is a mechanism outside the board and unprobed; the constraint stays the client's and is not deleted by the limit."),
    need("The certificate prepared from recorded results, ready to sign (W-5)", None,
         "needs a read from the results database that nobody has described or granted; the signature stays on paper by the client's rule (section 6.4)."),
    need("The audit finding about the register closed before the next surveillance visit", "before the next visit: 'March, I think. Annelise would know.' (00:08:18), hedged, the Quality Manager's to confirm",
         "the finding's wording is unknown; the board shows where a sample is, and whether that closes the finding is the assessor's call, not ours."),
    need("The authorisation number carried to the bench sheet (W-7)", None,
         "the number is on the test row; getting it onto the paper sheet needs the bench mechanism above, since the analyst will not read it from a screen."),
]


def ai(pain, kind, rnd, basis, idea):
    return OrderedDict([('pain_or_need', pain), ('kind', kind), ('round', rnd), ('probe_basis', basis), ('idea', idea)])


ai_opportunities = [
    ai('P1.3', 'workflow', 2, 'P-21', "When the priority flag is set, notify the Laboratory Manager and the named person at each bench that holds one of the sample's tests; on the approval list with the recipients shown."),
    ai('P1.5', 'agent', 2, 'unprobed', "Each morning list, per bench, the tests due within two working days against section 6.5, so lateness is seen before the submitter rings."),
    ai('P1.2', 'ai_column', 2, 'unprobed', "Draft the one-line answer to a submitter's enquiry from the sample's test statuses, for reception to read out; no submitter data leaves the board."),
    ai('P2.3', 'ai_column', 2, 'unprobed', "Once a read from the results database exists, compare the certificate draft's values with the read-in results and flag a difference before signature; nothing until the read exists."),
]

verdict = OrderedDict([
    ('cleared_for', 'build'),
    ('conditions', [
        "approval stop",
        "no A11 question first matters for an own-account build with invented data (A21); the three A11 decisions stay open",
        "the priority approval is built neither way before the 9th; if the 9th does not settle it, it is carried as a listed open decision",
        "the meeting of Friday the 9th is committed, not held: the invite is the Consultant's to send today, the Quality Manager's and the Laboratory Manager's attendance is the operator's to secure, and the Director is not promised",
        "the bench's status mechanism is agreed with the Laboratory Manager before any bench view is shown as live",
        "no result and no submitter data on the platform; the certificate stage is shown as status and dates only until a read from the results database exists",
    ]),
    ('reason', "Pains with named entities and the operator's own outcome words, one product, a stated structure with its leanings and a named build target clear a build; what stays open is carried as leanings, assumptions and the five questions."),
])


def qst(text, kind, role, known):
    return OrderedDict([('text', text), ('kind', kind), ('role', role), ('known', known)])


questions = [
    qst("Your procedure (section 4.2) has the Laboratory Manager approving a priority request before allocation, and the notes want that approval on screen (W-3). Reception described the request going to the top of the pile and to one bench by word of mouth, and asked whether the register can tell the Laboratory Manager when something is flagged. Which route should the register carry, and does an approval step exist at all?",
        'read-back', 'Quality Manager and Laboratory Manager together',
        "both statements with their sources (QP-07 section 4.2; 00:04:01 and 00:04:25); W-3 as the requirement that depends on the answer; the operator's own words for the outcome (00:10:46, 00:13:45); the flag with a notification is built either way and the approval step neither way until answered."),
    qst("How does an analyst mark a test started, its results entered and a re-test raised without a keyboard in hand: a scan, a shared screen at the bench, the morning sheet, or the Laboratory Manager alone? And is a sample with more than one test on two benches at the same time?",
        'discovery', 'Laboratory Manager',
        "'they're not going to touch a screen. Tobiah will, the others won't.' (00:12:03); the write-up's no-keyboard constraint (p.2 section 3); in September purity finished the day the lot arrived while germination queued (00:06:03); 'Fifteen if it's a multi-test.' (00:09:31); the bench's own time on results entry is hers to give (00:09:48)."),
    qst("What can be read from the results database, and how (an export, a report, read access), so a certificate draft can be prepared from recorded results without re-typing and without touching the validated system? Who grants it, and is a draft for the signatory's signature acceptable under section 6.4?",
        'discovery', 'Quality Manager, with the Laboratory Manager',
        "the database stays and 'cannot be replaced or altered' (write-up p.2 section 3; 00:12:03); the certificate is typed from it today and checked twice (00:08:36, 00:09:17); two transpositions this year (00:09:17); nothing on writeback was said by anyone."),
    qst("Reception says the finding from the May visit has to be closed before the next visit, 'March, I think', and that you said before the visit. What does the finding say, when is the next visit, and is closing the finding the deadline?",
        'read-back', 'Quality Manager',
        "the finding and the May visit first-hand from the operator (00:07:53); the date hedged (00:08:18); the timing relayed and hedged ('Realistically Annelise said before the visit', 00:11:46); the contract from October and the first lorry next week (00:07:17)."),
    qst("Reception says Marguerite does the morning allocation and signs most certificates; the procedure gives the allocation to a Laboratory Supervisor (4.1, 5.4) and the approvals and signature to the Laboratory Manager (4.2, 4.3, 6.4). Is Marguerite the Laboratory Manager, is the Supervisor role filled, and who should own the allocation view and the approvals?",
        'discovery', 'Quality Manager and Laboratory Manager',
        "the two titles and their sections; 'Marguerite, mostly. Annelise if Marguerite's off.' (00:08:50); 'Marguerite does allocation in the morning' (00:14:24); the binding of the name to the title is ours, by elimination from the signatory rule."),
]

readiness = OrderedDict([
    ('schema', 'readiness/1'),
    ('note', "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top)."),
    ('pains', pains),
    ('signals', signals),
    ('entities', entities),
    ('structure', structure),
    ('existing', existing),
    ('assumptions', assumptions),
    ('unmet_needs', unmet_needs),
    ('ai_opportunities', ai_opportunities),
    ('verdict', verdict),
    ('questions', questions),
])
d['readiness'] = readiness

# ---------------------------------------------------------------- 4. checks before writing
assert list(d.keys())[-2:] == ['intake', 'readiness'] and len(d) == 27
def strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)
    elif isinstance(o, str):
        yield o


blob = ' | '.join(strings(readiness))
bad = re.findall(r"\bR\d{1,2}\b|\bMet\b|\bPartial\b|\bMissing\b|met-with-residual|not-obtainable|\bgates?\b|Nearly ready|Not ready|\bverdicts?\b|\bgraded?\b|\brubric\b|\bcriteri", blob)
assert not bad, 'sales vocabulary in the block: %r' % bad
epp_ids = [e['pain'] for e in element_per_pain]
assert epp_ids == ids == [p['id'] for p in pains]
assert len(questions) <= 5
for e in entities:
    if e['parent']:
        assert e['moves_independently'] in ('yes', 'no', 'unknown')
print('new call-quote proofs:', sum(1 for q, l in proofs if re.match(r'\d\d:\d\d:\d\d', l)))
print('counts: pains %d signals %d entities %d leanings %d element_per_pain %d incumbents %d assumptions %d unmet %d ai %d questions %d' % (
    len(pains), len(signals), len(entities), len(leanings), len(element_per_pain), len(existing['incumbents']),
    len(assumptions), len(unmet_needs), len(ai_opportunities), len(questions)))

out = render.dumps(d, expanded)
json.loads(out)
open(KEY, 'w', encoding='utf-8').write(out)
print('written:', len(out.splitlines()), 'lines; non-ascii:', sorted({c for c in out if ord(c) > 127}))
