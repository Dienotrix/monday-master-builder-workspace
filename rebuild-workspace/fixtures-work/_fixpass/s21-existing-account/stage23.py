import json, re, sys
sys.path.insert(0, '.')
from render import dump
F = '/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s21-existing-account/'
P = F + 'answer-key.json'
k = json.load(open(P, encoding='utf-8'))
units = {}
for line in open(F + 'transcript.txt', encoding='utf-8'):
    m = re.match(r'\[(\d\d:\d\d:\d\d)\] ([^:]+): (.*)$', line.rstrip('\n'))
    if m: units[(m.group(1), m.group(2))] = m.group(3)
def at(loc):
    m = re.match(r'(\d\d:\d\d:\d\d) (.+?)(?: \(.*\))?$', loc); return units[(m.group(1), m.group(2))]
def q(quote, loc):
    assert quote in at(loc), (quote[:60], loc); return quote
def rep(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:80]); return s.replace(old, new)

# ---------- stage 2: sweep corrections to existing fields
lt = k['expected_structures']['lookalike_traps']
lt[1] = rep(lt[1], "the view is a view over studies, keyed by the agency value already on Studies.",
    "the view is a view over studies, keyed by an agency value: the costing form carries agency today (00:15:14), and whether the Studies board has such a column is read live, never assumed.")
voc = {v['their_term']: v for v in k['vocabulary']}
voc['client / agency / brand']['likely_monday_object'] = "dropdown or text: the agency field on the costing form today; on Studies only if a column exists there (read live); the per-agency view groups by it; not a CRM Accounts board"
voc['session']['likely_monday_object'] = "its own row (child rows under the study, or a sessions board connected to Studies) with date, centre, room, recruiter and headcount; the recruiter week view is a view over these rows, never one row per study"
am = k['intake']['alias_map']
assert am['Farraday'] == ["an agency and its study; not a person"]
am['Farraday'] = ["an agency (an organisation), not a person; 'the Farraday one' (00:09:16) is its study and 'the Farraday invoice' (00:37:30) its invoice, both belonging to the one agency, not second entities"]

# ---------- stage 3: the readiness block
H = 'Henrietta Weyland (Director of Operations)'; B = 'Bethan Tull (Fieldwork Manager)'; I = 'Idris Machado (Recruitment Team Lead)'
OUT1 = q("A brief comes in, Bethan costs it once, in one place, and the number that goes to the agency is the number Philippa sees. That's it. That's the whole thing.", '00:28:25 ' + H)
OUT2 = q("Meaning I don't care where, as long as there's one of it. If the number's on Beth's board and the Studies board shows it and Philippa reads it off the same thing, that's one place. If it's three files that agree, that's not.", '00:28:41 ' + H)
OUT3 = q("And I get my Fridays back.", '00:28:59 ' + B)
OUT4 = q("And the recruiters can see their week without Leonie retyping it.", '00:29:03 ' + I)
OUT5 = q("But if it was on the screen in the recruitment room, the big one, and it was right, they'd use it.", '00:26:01 ' + I)
OUT6 = q("This time I want someone here who can change things.", '00:05:55 ' + H)
kp = k['pains']
ids = ['P1.1', 'P1.2', 'P1.3', 'P1.4', 'P1.5', 'P1.6', 'P2.1', 'P2.2', 'P3.1']
roles = ['Fieldwork Manager'] * 6 + ['Recruitment Team Lead'] * 2 + ['Director of Operations']
se = ['excavated', 'excavated', 'stated', 'stated', 'stated', 'stated', 'excavated', 'excavated', 'excavated']
outs = [OUT1, OUT1, OUT2, OUT3, OUT2, None, OUT4, OUT5, OUT6]
pains = []
for pid, p, role, s, o in zip(ids, kp, roles, se, outs):
    q(p['quote'], p['location'])
    pains.append({"id": pid, "quote": p['quote'], "location": p['location'], "speaker_role": role, "stated_or_excavated": s, "outcome": o})

def sig(quote, loc, pain, nc): return {"quote": q(quote, loc), "location": loc, "pain": pain, "not_confirmed": nc}
signals = [
    sig("If the number's on Beth's board and the Studies board shows it and Philippa reads it off the same thing, that's one place.", '00:28:41 ' + H, 'P1.3',
        "that Philippa will read the costed total off the board; she keeps her own copy of the sheet today (00:11:23) and was not on the call; our side wrote the actual question down for later (00:22:31) and never asked whether she would read the board"),
    sig("It's the number that doesn't follow.", '00:18:33 ' + B, 'P1.4',
        "whether a late cell added by an account lead should also tell Bethan it was added; our side asked who adds cells and moved to n, so the roll-up is confirmed as the fix and the notice is not"),
    sig("The two things don't know about each other.", '00:23:33 ' + I, 'P2.2',
        "that a week view reading the Studies board's field dates is the fix Idris wants; our side built it into the scope playback without reading it back to him, and Henrietta wants to see the approach before she says yes"),
    sig("If it was hers and not something done to her, maybe. Maybe. She'd need to be in the room when it's built, not shown it after.", '00:26:30 ' + I, 'P2.1',
        "whether Leonie would own a board; Idris's guess about an absent person; our side asked for her columns and not how she comes into the room"),
    sig("If we keep doing it in the sheet we will lose one of them. Not might. Will. They've said so.", '00:13:30 ' + H, 'P1.1',
        "the forty-eight-hour requirement as the agency stated it; relayed from a review; our side repeated 'They've said so.' and moved on"),
    sig("I think you're still an admin on it. You and Hamish, and that's it. I'm a member, I think, I've never checked.", '00:05:34 ' + B, 'P3.1',
        "who is admin on the account; hedged twice; our side said it would check rather than guess (00:05:44) and has not read it yet"),
]

def ent(name, parent, mv, shared, stale, source, ev):
    if ev: at(ev)
    return {"name": name, "parent": parent, "moves_independently": mv, "shared_resource": shared, "goes_stale": stale, "source": source, "evidence": ev}
entities = [
    ent("agency (the commissioning research agency, the client's 'client')", None, "yes", False, False, "spoken", '00:07:39 ' + B),
    ent("brand (a direct commissioner, sometimes)", None, "yes", False, False, "spoken", '00:12:52 ' + B),
    ent("brief / study (one thing at two stages; one row on Studies and one on the costing board today)", "agency", "yes", False, False, "spoken", '00:07:39 ' + B),
    ent("study code (the identifier on every board; typed twice today)", "brief / study", "no", False, True, "spoken", '00:16:13 ' + B),
    ent("cell (an audience group; agencies also say quota)", "brief / study", "yes", False, False, "spoken", '00:08:12 ' + B),
    ent("n (sample size of a cell; changes when the screener is signed off)", "cell", "yes", False, False, "spoken", '00:15:44 ' + B),
    ent("incentive per head, recruit cost per head, moderation hours (cost lines of a cell)", "cell", "no", False, False, "spoken", '00:08:12 ' + B),
    ent("qual / quant (the study type that decides which cost lines apply)", "brief / study", "no", False, False, "spoken", '00:08:51 ' + B),
    ent("cell total (formula on the subitem; works)", "cell", "no", False, False, "observed", '00:15:27 ' + B),
    ent("costed total on the parent (the subitem summary no parent formula or connection reads)", "brief / study", "no", False, True, "observed", '00:18:20 ' + B),
    ent("costed brief as sent to the agency (a snapshot of the total at sending)", "brief / study", "no", False, True, "spoken", '00:11:16 ' + B),
    ent("the costing sheet (one copy per fieldwork manager, copied per brief)", None, "no", False, True, "spoken", '00:07:55 ' + B),
    ent("finance's copy of the costing sheet", "the costing sheet", "no", False, True, "spoken", '00:11:23 ' + H),
    ent("invoice and actual study cost (in the accounting system)", "brief / study", "yes", False, False, "spoken", '00:22:25 ' + B),
    ent("field dates (on Studies; moved by the account lead)", "brief / study", "yes", False, False, "spoken", '00:23:33 ' + I),
    ent("Studies status label (about seven; two mean the same thing)", "brief / study", "yes", False, False, "spoken", '00:03:44 ' + H),
    ent("the Friday digest (an email automation off Studies)", "the Studies board", "no", False, False, "spoken", '00:03:20 ' + H),
    ent("Incentives board row (who is owed what and whether paid; finance's)", None, "yes", False, False, "spoken", '00:32:11 ' + H),
    ent("screener (signed off after the brief; changes n)", "brief / study", "yes", False, False, "spoken", '00:15:44 ' + B),
    ent("wave (a fielding period; nothing new in its last two weeks)", None, "yes", False, False, "spoken", '00:28:00 ' + I),
    ent("session (a fielding slot, such as a Saturday session)", "brief / study", "yes", False, False, "spoken", '00:23:13 ' + I),
    ent("recruiter (28 across two centres; booked on sessions)", "centre", "yes", True, False, "spoken", '00:23:13 ' + I),
    ent("room (the recruitment rooms; a session needs one)", "centre", "yes", True, False, "spoken", '00:27:38 ' + I),
    ent("centre (the main office and Thornbury)", None, "yes", False, False, "spoken", '00:01:28 ' + H),
    ent("Leonie's rota sheet (colour-coded)", None, "no", False, True, "spoken", '00:24:11 ' + I),
    ent("the photo of the rota sheet in the group chat", "Leonie's rota sheet", "no", False, True, "spoken", '00:23:33 ' + I),
    ent("the dead Recruiter rota board", None, "no", False, True, "spoken", '00:04:25 ' + I),
    ent("respondent (names, numbers and history; panel software only, never on a board)", None, "unknown", False, False, "spoken", '00:27:14 ' + I),
    ent("account lead (five; puts the brief on Studies, fills the form, sends the number)", None, "yes", False, False, "spoken", '00:07:39 ' + B),
    ent("fieldwork manager (three; costs briefs)", None, "yes", False, False, "spoken", '00:07:39 ' + B),
]

def lean(question, option, qs, cond, pattern):
    return {"question": question, "option": option, "quotes": [q(a, b) for a, b in qs], "locations": [b for a, b in qs], "condition": cond, "pattern": pattern}
leanings = [
    lean("Is a recruiter week one row per study with its field dates, or one row per session?",
         "One row per session (date, centre, room, recruiter or recruiters, headcount needed) under the study it belongs to, bounded by the study's field dates read from the Studies board; the recruiter week view on the wall screen is a view over session rows. One row per study carrying its field dates would copy the dead rota board, which never had the sessions on it. Sessions are typed by Leonie, not by the account leads, so Studies stays read, not typed for them; whether sessions sit as child rows on Studies or on their own board connected to it is settled by the condition. The link to the Studies field dates is our design, drawn from Idris's account of the Saturday session; he did not ask for it in those words.",
         [("And the recruiters look at the photo. Not the board. The board's never had the sessions on it.", '00:23:55 ' + I),
          ("Sessions, rooms, which recruiter, how many needed. Never who the respondents are. That's the line.", '00:27:38 ' + I),
          ("The field dates moved on the Wednesday. The Studies board had the new dates, because the account lead changed them, which is right. Leonie's sheet had the old ones, because nobody told her.", '00:23:33 ' + I)],
         "Idris's photo of Leonie's columns (committed for the day of the call); Henrietta seeing the approach before she says yes (00:27:45, 00:34:33); Leonie in the room when it is built; and Henrietta's condition that the account leads type nothing new on Studies, which decides between child rows on Studies and a connected sessions board.",
         "one row where the call describes many"),
    lean("Who holds which recruiter and which room, when?",
         "Each session row names its recruiter or recruiters, its room and its centre, with a per-recruiter and a per-room view of the week, so a recruiter booked on two sessions or a room booked twice shows before the Saturday. Today Leonie's colour-coded sheet is the only reservation record, and nobody but Leonie can read it. A status on a session row set by Leonie is her claim that the recruiter knows, never evidence that they do; what the recruiters read is the wall screen.",
         [("Three weeks ago we had a Saturday session with two recruiters booked on it and neither of them knew. Twelve respondents turned up to an empty room and the account lead had to ring round apologising.", '00:23:13 ' + I),
          ("When she was off for a week in the summer nobody could read the colours and we lost two sessions.", '00:24:24 ' + I)],
         "Leonie's columns show whether a recruiter is booked per session or per day and whether rooms are on her sheet; Thornbury's own recruiters and room come with the second centre (00:25:17); the view is built only after Henrietta has seen the approach.",
         "a shared resource with no reservation tracking"),
    lean("When a cell is added or n changes after the brief was costed, what shows that the costed number is out of date?",
         "The parent total follows the cells once the roll-up works, which is the point of approach one, and the parent also keeps the total as sent and the date it was sent, so a difference between the live total and the sent total is visible and reaches Bethan rather than being found by Philippa. Without the sent total, a working roll-up still leaves the agency's number silently behind the board's.",
         [("Someone adds a cell after it's costed. Then the summary moves and the parent doesn't, and nobody -- nobody notices until Philippa does.", '00:18:20 ' + B),
          ("Same thing. Anything that changes after I've looked at it, I have to go back and look at it again, and I don't always know it's changed.", '00:18:49 ' + B)],
         "The working session on a copy shows whether the roll-up follows a late cell and an n change (00:20:59); Bethan says whether the costed brief goes to the agency from the board or by email, which decides where the sent total is set.",
         "an artefact that can go stale with nothing to flag it"),
    lean("Is the study code typed once, and on which board?",
         "Typed once on the Studies board, where the account lead already puts it first, and read by the costing board through the connection; the form stops asking for it or shows it read-only. The other direction, or typing it twice, leaves codes that do not match and a connection that fails silently, as the one with a space did.",
         [("Typed twice. I type it on the form, well, the account lead types it on the form, and they've already typed it on Studies. If they don't match, they don't match. I've had one with a space in it that never lined up.", '00:16:13 ' + B),
          ("The code. Same as the Studies board. We never put the brand on a board.", '00:15:58 ' + B)],
         "Whether a form on the costing board can take the code from a connected Studies item, tried on the copy; what happens to the existing items whose codes do not match; Henrietta's rule that account leads type nothing new on Studies holds either way, since the code is already theirs to type there.",
         "an artefact that can go stale with nothing to flag it"),
    lean("What does the per-agency monthly costed-versus-actual view show in v0.1, with 'actual' living in the accounting system?",
         "The costed half only: the parent totals grouped by agency and month, from the agency value on the form. The actual half waits for Philippa: whether she allows a read, a monthly upload, or keys actual onto the study herself. Until then a figure typed into an actual column is a claim about the accounting system, never its number, and the view says so. Building the view as if both halves existed would show a number nobody trusts, which is what stopped Bethan's dashboard.",
         [("Add up the study totals per agency, per month. Which is the other thing I want, so I'll come back to it. It showed me a number I didn't trust, so I stopped.", '00:17:34 ' + B),
          ("In Philippa's system. The accounting one. It doesn't live anywhere I can see.", '00:22:25 ' + B)],
         "Philippa's answer on where actual lives and how it may be read, after Henrietta puts the Consultant in touch (00:36:32); whether the agency value exists on Studies or only on the costing form.",
         "a pain with no element that fixes it"),
    lean("Where does the agency value that the per-agency view groups by live today?",
         "On the costing form, which the account lead fills in with brief name, agency, field dates and how many cells; the key had placed it on Studies, which the call does not say. Agency stays one dropdown or text value on the study row, spelled one way per agency; Farraday is one such agency and 'the Farraday one' is its study, not a second thing. It never becomes a board of agencies, which would be a CRM look-alike in a build with no CRM.",
         [("Form on the front. So the account lead fills it in, brief name, agency, field dates, how many cells, um, that makes the item. Then I go in and add the cells.", '00:15:14 ' + B),
          ("The Farraday one. The incentive line was in there twice, once per cell and once at the bottom, and I didn't catch it, and the number went to the agency doubled up on the incentives and light everywhere else, and we ate it.", '00:09:16 ' + B)],
         "The Studies board's columns read live at preflight; if agency is not on Studies, the view sits on the costing board, or the value reaches Studies through the same connection as the total, read, not typed.",
         "our framing labelled as the client's"),
]

epp = [
    {"pain": "P1.1", "element": "Bethan's costing board as the one place: form, one item per brief, cells as subitems, the parent total read by the Studies board; the three copies of the sheet retire", "verdict": "fixes"},
    {"pain": "P1.2", "element": "the cell-total formula per cell and the parent total summed by the board, with the qual/quant type deciding which cost lines apply, so an incentive line cannot be counted twice by hand", "verdict": "fixes"},
    {"pain": "P1.3", "element": "one parent total read by Studies and by Philippa (assumption: she reads the board rather than her own copy; her re-key into the accounting system for the invoice is untouched in v0.1 and is an unmet need)", "verdict": "fixes"},
    {"pain": "P1.4", "element": "a late cell is a new subitem and the parent total follows; the sent total and sent date show the difference (leaning 3); unverified until the roll-up is tried on a copy", "verdict": "fixes"},
    {"pain": "P1.5", "element": "the roll-up itself: approach one, the cell total onto the parent and the Studies board reading it through a connection, in Bethan's own board and workspace; unverified until tried on a copy", "verdict": "fixes"},
    {"pain": "P1.6", "element": "the per-agency monthly view over parent totals; its actual half waits for a source in the accounting system (leaning 5), so until then the view answers half of the question that today gets a shrug", "verdict": "copies-today's-tool"},
    {"pain": "P2.1", "element": "session rows bounded by the Studies field dates, shown on the recruitment room's wall screen; Leonie types a session once and no photo is taken; conditional on Henrietta seeing the approach and Leonie in the room", "verdict": "fixes"},
    {"pain": "P2.2", "element": "the session rows read the study's field dates from the Studies board, so a moved date shows on the week view instead of in a stale photo (leaning 1)", "verdict": "fixes"},
    {"pain": "P3.1", "element": "label editing on the Studies board handed to Bethan with Henrietta's yes, after the admin and member roles are read live", "verdict": "fixes"},
]

structure = {
    "products": ["Work Management"],
    "build_target": "client-account",
    "build_target_reason": "existing customer with a live account of their own (A21)",
    "workspaces": ["existing: the workspace that holds the Studies board, the Friday digest, the Incentives board and the dead rota board (its name is not spoken on the call; read live at preflight)", "existing: Bethan's own workspace that holds the costing board (no access yet; the client's IT people decide how the Consultant comes in)"],
    "native_reuse": "none: no CRM or Service entity. The per-agency view is a view over studies, never an Accounts board; no new workspace is planned, because the build continues the client's own existing workspaces (A21).",
    "leanings": leanings,
    "patterns": ["parent-row-with-roll-up: brief (study) with cells as child rows, the costed total on the parent (client-built; the roll-up to the parent is the missing piece)", "parent-row-with-roll-up: study with sessions as child rows or a connected sessions board, the recruiter week view over the sessions (conditional on Henrietta's yes)"],
    "element_per_pain": epp,
}

existing = {
    "account": "Bound: the client's own account (Pro per the client, 'thirty-something seats', hedged; read live at preflight). Live and ours from the earlier rollout: the Studies board (one line per study, a status column with about seven labels, field dates) with its Friday digest automation, do-not-change; the Incentives board, finance's own, do-not-change; the dead Recruiter rota board, to be archived once Henrietta approves. Client-built: Bethan's costing board (form, one item per brief, cells as subitems, a working cell formula, a subitem summary no parent formula or connection reads) in her own workspace, no access yet. Admin membership hedged ('I think you're still an admin on it'), read live. No CRM or Service. The record already exists; this is a second strand in it.",
    "incumbents": [
        {"system": "the accounting system (finance)", "authority": "stays system of record for: invoices, actual study cost, bank and payment details, the loaded rates ; follower for: nothing in v0.1; the per-agency view's actual half waits on it; writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours", "evidence": '00:22:25 ' + B},
        {"system": "the panel software", "authority": "stays system of record for: respondent names, numbers and history ; follower for: nothing, by the client's own rule agreed with the agencies' compliance people; no board, view or seed row names a respondent", "evidence": '00:27:14 ' + I},
        {"system": "the costing sheet (one per fieldwork manager, plus finance's copy)", "authority": "stays system of record for: briefs costed before the switch, until Bethan says otherwise ; follower for: nothing after it; replaced, not mirrored", "evidence": '00:07:55 ' + B},
        {"system": "Leonie's rota sheet and its photo in the group chat", "authority": "stays system of record for: the recruiters' week, until a week view exists that Leonie owns ; follower for: nothing; replaced only after Henrietta has seen the approach and Leonie was in the room", "evidence": '00:24:11 ' + I},
        {"system": "email (briefs in, the Friday digest out)", "authority": "stays system of record for: the brief as the agency sent it, and the digest's delivery ; follower for: nothing", "evidence": '00:07:39 ' + B},
    ],
}
for inc in existing['incumbents']: at(inc['evidence'])

assumptions = [
    {"statement": "Philippa will read the costed total off the board rather than from her own copy of the sheet.", "question": "Philippa, will you read the costed total from the board, and what do you still need in your own file?"},
    {"statement": "The agency value lives on the costing form and not on the Studies board.", "question": "Which columns does Studies carry today: code, status, field dates, and is agency among them?"},
    {"statement": "The Pro plan allows a connection from Bethan's workspace to the Studies board and a roll-up from subitems to the parent.", "question": "Read at preflight: the tier, the seat count and the limits that touch the connection and the roll-up."},
    {"statement": "The account lead puts the brief on Studies before the form is filled, so Studies is the source side for the code.", "question": "Does every brief reach Studies before the form, every time, or do some start on the form?"},
    {"statement": "A recruiter is booked per session, not per day.", "question": "On Leonie's sheet, is a recruiter against a session or against a day?"},
    {"statement": "Thornbury's sessions go on the same week view with a centre value, not on a second view.", "question": "Idris, one view across both centres, or one per centre on each room's screen?"},
    {"statement": "The Friday digest reads only the status column, so a read-only column added to Studies does not change it.", "question": "Read the digest automation live before anything lands on Studies: which columns does it send?"},
    {"statement": "The qual or quant type decides which cost lines apply to a cell, and no study is both.", "question": "Bethan, is a study ever both qual and quant, with cells of each kind?"},
    {"statement": "The number of cells on the form is informational; the subitems are the count.", "question": "Should the form stop asking how many cells, now that the cells are rows?"},
    {"statement": "The costed brief goes to the agency by email from Bethan today.", "question": "How does the number reach the agency: an email from you, from the account lead, or a document?"},
    {"statement": "The two Studies labels that mean the same thing are merged by Bethan after the handover, not by us.", "question": "Which two labels, and does the Friday digest or any view filter on either?"},
    {"statement": "The admins on the account are the Consultant and Hamish, and Bethan is a member.", "question": "Read live before anything is changed: who is admin and who is a member today?"},
    {"statement": "The wave's last two weeks fall after the working session, so the costing work is not blocked by the blackout; only work landing on the recruiters is.", "question": "Idris, when does the wave start and end, so nothing new reaches the recruiters in its last two weeks?"},
]

unmet = [
    {"need": "Actual study cost beside costed, per agency per month", "clock": None, "why_not_met": "actual lives in the accounting system; no read or upload exists in v0.1; waits on Philippa's answer"},
    {"need": "The third keying: Philippa re-keys the costed brief into the accounting system for the invoice", "clock": None, "why_not_met": "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours"},
    {"need": "A costed brief back to the agency inside forty-eight hours", "clock": "the two new agency clients want it inside forty-eight hours; no date given; one will be lost if costing stays in the sheet", "why_not_met": "the costing piece shortens Bethan's step; the brief's arrival by email and the account lead's send are untouched, and no board measures the turnaround in v0.1"},
    {"need": "Recruiters at both centres seeing their week without Leonie retyping it", "clock": "a wave starts the week after next; nothing new reaches the recruiters in a wave's last two weeks", "why_not_met": "conditional: Henrietta says yes only after she has seen the approach, and Leonie must be in the room; no element exists until then"},
    {"need": "n updated when the screener is signed off", "clock": None, "why_not_met": "no screener system was named; n stays typed by Bethan, and the sent-total flag (leaning 3) shows when it moved after costing"},
]

ai = [
    {"pain_or_need": "P1.4", "kind": "workflow", "round": 2, "probe_basis": "P-21", "idea": "When a cell is added or n changes on a brief whose total has been sent, mark the brief as changed since sending and notify Bethan and the account lead."},
    {"pain_or_need": "P1.1", "kind": "ai_column", "round": 2, "probe_basis": "unprobed", "idea": "An AI column on the brief that reads the agency's emailed brief, pasted or attached, and drafts the cells with n, incentive and recruit cost as a proposal for Bethan to accept or correct, since the agencies all send it differently."},
    {"pain_or_need": "P1.2", "kind": "ai_column", "round": 2, "probe_basis": "unprobed", "idea": "An AI column that reads a costed brief for the Farraday shape, moderation hours on a quant study or an incentive counted at both cell and study level, and writes one line of warnings before the number goes out."},
    {"pain_or_need": "P2.2", "kind": "workflow", "round": 2, "probe_basis": "P-21", "idea": "When a study's field dates move on the Studies board, flag every session under it and notify Leonie and Idris."},
]

verdict = {
    "cleared_for": "build",
    "conditions": [
        "approval stop",
        "A11-2 asked first (client-account target): sample data inside a live client account is asked before the first such build; Bethan's test rows are hers and are never presented as figures",
        "access to Bethan's workspace and the costing board by whatever route the client's IT people set; nothing is read or built there before it",
        "approach one tried on a copy of her board before any claim that it works; no completion, effort or duration figure until the board has been read",
        "Henrietta's yes before anything touches the Studies board or the Friday digest, and nothing new typed on Studies by the account leads",
        "the rota archive: proposed by the Consultant, accepted by Idris, Henrietta's approval still required before anything changes; archive, never delete",
        "the recruiter week view only after Henrietta has seen the approach and with Leonie in the room; nothing new reaches the recruiters in the last two weeks of the wave starting the week after next",
        "the Incentives board and respondent data untouched: nothing near Philippa's board without her, nothing from the panel software on any board, view or seed row",
        "the booking link, the recap, Idris's photo and Bethan's access request are committed, not done; each becomes done only on evidence",
    ],
    "reason": "Two pains with named entities and the outcome in Henrietta's words ('Bethan costs it once, in one place'), one product, a structure stated as a delta against the client-built board with its leanings, and the build target named: the client's own account, continuing its existing workspaces.",
}

questions = [
    {"text": "What did the IT people say about how the Consultant comes into your workspace and the costing board, and at what seat level?", "kind": "discovery", "role": "Bethan Tull, once the IT people answer", "known": "Bethan will ask them; a few days; the Consultant does it whichever way they want; nothing is read or built before the answer."},
    {"text": "On a copy of your board, does approach one hold: cells stay subitems, the total reaches the parent, the Studies board reads it through the connection, and what happens when a cell is added after costing or n changes at screener sign-off?", "kind": "discovery", "role": "Bethan Tull, in the booked working session", "known": "the subitem summary offers sum and average and is not in the formula list; four attempts failed (parent formula, mirror, typed number column, dashboard); the Consultant has built approach one before but not against a form like hers; the form stays."},
    {"text": "Henrietta said the number is in one place if it is on Beth's board, the Studies board shows it and you read it off the same thing. Will you read the costed total from the board, where does actual live in the accounting system, and may it be read or uploaded monthly?", "kind": "read-back", "role": "Philippa (finance controller), introduced by Henrietta", "known": "Philippa keeps her own copy of the costing sheet and re-keys the costed brief into the accounting system for the invoice; actual lives there and nowhere Bethan can see; she can stop anything near the Incentives board; the loaded rate is a separate conversation outside this check."},
    {"text": "You said the code is typed twice and one with a space never lined up. Should the code be typed once on Studies and read by the costing board, and which columns does Studies carry today: code, status, field dates, and is agency among them?", "kind": "read-back", "role": "Bethan Tull and one account lead", "known": "the account lead types the code on Studies and again on the form; the costing form carries agency; the Studies status column has about seven labels, two meaning the same thing; nothing new may be typed on Studies by the account leads."},
    {"text": "Idris said that if a board was yours and not something done to you, maybe you would own it. What is on your sheet, column by column, which sessions and rooms exist across both centres, is a recruiter booked per session or per day, and when do the wave's last two weeks fall?", "kind": "read-back", "role": "Leonie (recruitment coordinator) with Idris, in the room", "known": "a photo of the columns is committed by Idris for the day of the call; the sheet is colour-coded and photographed into the group chat; the dead board never had the sessions on it; Henrietta wants to see the approach before she says yes; nothing new in the last two weeks of a wave."},
]

k['readiness'] = {
    "schema": "readiness/1",
    "note": "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top). The build target is the client's own account (A21), so A11-2 is asked before the first such build; the key's pains are numbered P1.1 to P1.6, P2.1 and P2.2 after their themes, and the unnumbered incumbent-friction entry is P3.1.",
    "pains": pains, "signals": signals, "entities": entities, "structure": structure, "existing": existing,
    "assumptions": assumptions, "unmet_needs": unmet, "ai_opportunities": ai, "verdict": verdict, "questions": questions,
}
assert list(k)[-2:] == ['intake', 'readiness'] and len(k) == 27
blob = json.dumps(k['readiness'], ensure_ascii=False)
bad = re.findall(r"\bR\d{1,2}\b|\bgate\b|Nearly ready|Not ready|\bbleed\b|\bupside\b|mechanism-confirmed|expansion mode|\bPartial\b|\bMissing\b|met-with-residual|not-obtainable", blob)
assert not bad, bad
dump(k, P)
print('stage 2+3 written: pains', len(pains), 'signals', len(signals), 'entities', len(entities), 'leanings', len(leanings), 'epp', len(epp), 'assumptions', len(assumptions), 'unmet', len(unmet), 'ai', len(ai), 'questions', len(questions), 'conditions', len(verdict['conditions']))
