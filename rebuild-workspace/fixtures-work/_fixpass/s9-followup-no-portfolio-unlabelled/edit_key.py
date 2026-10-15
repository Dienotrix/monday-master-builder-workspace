#!/usr/bin/env python3
"""Fix-pass edit for s9-followup-no-portfolio-unlabelled: field corrections and the readiness block.
Every quote the block introduces is proven verbatim at its paragraph before the file is written."""
import json, re, sys, collections
FIX = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s9-followup-no-portfolio-unlabelled'
KEY = FIX + '/answer-key.json'
raw = open(KEY, 'rb').read()
d = json.loads(raw.decode('utf-8'), object_pairs_hook=collections.OrderedDict)
assert (json.dumps(d, ensure_ascii=False, indent=2) + '\n').encode('utf-8') == raw, 'round trip differs'
assert list(d.keys())[-1] == 'expected_leak_blocklist' and 'readiness' not in d and len(d) == 25

paras = re.split(r'\n\s*\n', open(FIX + '/transcript.txt', encoding='utf-8').read().strip())
assert len(paras) == 119
STAMPS = {1:'00:00:06',4:'00:00:31',11:'00:01:52',19:'00:04:10',33:'00:07:55',54:'00:11:20',72:'00:15:30',79:'00:17:45',86:'00:19:05',98:'00:22:40',112:'00:24:20'}
M, W, I = 'Marisol Bettencourt', 'Warren Tibbetts', 'Ines Kovalenko'
proofs = []
def loc(n, who):
    stamp = f", [{STAMPS[n]}]" if n in STAMPS else ''
    return f"paragraph {n}{stamp}, inferred {who} (speaker unclear)"
def q(n, text):
    assert text in paras[n-1], f'NOT IN paragraph {n}: {text!r}'
    proofs.append((n, text)); return text

# ---------- field corrections (each asserts the old text so a drift fails loudly) ----------
def swap(path, old, new):
    o = d
    for p in path[:-1]: o = o[p]
    k = path[-1]
    assert old in o[k], f'old text missing at {path}: {old!r}'
    o[k] = o[k].replace(old, new)
# never-written rule, weaker form
swap(['integrations_mentioned', 0],
     "Sage stays the book of record and must not be rebuilt in monday.",
     "The call fixes only the read direction, a monthly upload of the controller's report (paragraph 75); writeback and integration direction beyond that upload are unresolved; v0.1 does not depend on either; keeping job cost in Sage and not rebuilding it in monday is our safe default, labelled as ours.")
# pattern 4, our framing labelled as the client's (permission wording)
swap(['compliance_or_security_signals', 4],
     "This is a permission, not a preference, and was recorded as such on the call.",
     "The client's words are 'I want to be the one who does it' (paragraph 62) and, for the substitute, 'her and not a PM' (paragraph 63); 'a permission rather than a preference' is the Consultant's framing (paragraph 65), which the client did not object to and which the Consultant committed to write down.")
swap(['requested_changes', 8, 'description'],
     "Recorded as a permission, not a preference.",
     "The Consultant framed it on the call as a permission rather than a preference (paragraph 65); the client's own words are 'I want to be the one who does it' (paragraph 62).")
swap(['entities_and_workflows', 1],
     "Revisit conditions, which double as success criteria:",
     "Revisit conditions, given by the client as the test for revisiting the portfolio layer (paragraph 19) and proposed by our side as success criteria:")
# s21 standing line: committed, not in progress
swap(['requested_changes', 10, 'description'],
     "The master checklist and the senior PM's own version are being sent so the differences can be built in.",
     "The PMO director committed on the call to send the master checklist and the senior PM's own version (paragraph 71); neither has been received.")
swap(['entities_and_workflows', 7],
     "the master checklist and the senior PM's private version are being sent for comparison;",
     "the PMO director committed on the call to send the master checklist and the senior PM's private version for comparison (not yet received);")
swap(['integrations_mentioned', 4],
     "Excel: the master startup checklist and the senior PM's own version are being sent as inputs;",
     "Excel: the master startup checklist and the senior PM's own version are committed to be sent as inputs (not yet received);")

# ---------- pains: the key's 15 entries, same quotes and locations ----------
ids = ['P1.1','P1.2','P1.3','P1.4','P1.5','P2.1','P2.2','P2.3','P3.1','P3.2','P3.3','P4.1','P4.2','P4.3','P1.6']
roles = {M:'PMO Director', W:'Senior Project Manager', I:'Resource Manager'}
outcomes = {
 'P1.1': q(17, "Standardized, the same for everybody, actually used by the fourteen."),
 'P1.2': q(19, "I want one full month where I haven't had to email anybody for a status."),
 'P1.3': q(48, "I want to know who did that and when."),
 'P1.4': q(48, "I want to know who did that and when."),
 'P1.5': q(50, "Then surface it."),
 'P2.1': q(62, "I want to be the one who does it"),
 'P2.2': q(57, "I want to look at just those four."),
 'P2.3': q(63, "somebody has to be able to confirm in my place, and I'd want that to be her and not a PM"),
 'P3.1': q(77, "The actuals are history. My forecast is the job."),
 'P3.2': q(75, "there's a version of this where the number is a month old and everybody knows it's a month old"),
 'P3.3': q(40, "You've got a percent complete field on there and I'd take it off."),
 'P4.1': q(17, "Standardized, the same for everybody, actually used by the fourteen."),
 'P4.2': q(66, "it would be very useful to run that one properly from day one rather than retrofitting it afterwards"),
 'P4.3': q(83, "Send it to both of them and copy her."),
 'P1.6': q(45, "when did it move and what moved it"),
}
pains = []
for pid, p in zip(ids, d['pains']):
    n = int(re.match(r'paragraph (\d+)', p['location']).group(1))
    who = re.search(r'inferred (.+?) \(', p['location']).group(1)
    assert p['quote'] in paras[n-1]
    pains.append(collections.OrderedDict([
        ('id', pid), ('quote', p['quote']), ('location', p['location']),
        ('speaker_role', roles[who] + ' (inferred, speaker unclear)'),
        ('stated_or_excavated', 'stated'), ('outcome', outcomes[pid])]))

def sig(n, who, text, pain, nc):
    return collections.OrderedDict([('quote', q(n, text)), ('location', loc(n, who)), ('pain', pain), ('not_confirmed', nc)])
signals = [
 sig(15, M, "He said, I don't want a dashboard I have to learn to distrust.", 'P1.1',
     "the VP of Operations' objection is relayed by the PMO director; nobody on our side has heard him, and the revisit test is hers, not his"),
 sig(29, M, "He's a milestones man more than a totals man. But he might.", 'P1.1',
     "what Cumberland's VP will ask for on January fifteenth; our side raised the risk of a program total and the client took it, nothing was checked with Cumberland"),
 sig(54, I, "He could answer his own question with that.", 'P2.1',
     "that the workload view answers the senior PM's collision question; our side moved on to 'what would you change' without asking"),
 sig(55, W, "I went in on the Friday and looked Junie up for October without asking her, and it took me about eleven seconds, and it was right.", 'P2.1',
     "the senior PM's own tie of the workload view to his pain, in a paragraph that runs two speakers together; our side never asked whether it solves the collision"),
 sig(75, M, "Roland will talk to you.", 'P3.2',
     "the controller's position (no live connection; a monthly report he does not mind being uploaded) is relayed; what the report contains, its format and who uploads it were never confirmed with him"),
 sig(79, M, "he asked me on Monday whether this sits in our tenant and how many of the two hundred and twenty enterprise seats it eats", 'none (where the build lives)',
     "the IT director's two questions are relayed; the Consultant committed to answer them this week; nothing is sent"),
 sig(103, M, "He said if you're building this, can it show the pipeline as well, the work we're chasing.", 'none (out of scope)',
     "the VP of Operations' interest in a pipeline view is relayed and explicitly not requested by the client; nothing was checked with him or with preconstruction"),
]

def ent(name, parent, moves, shared, stale, source, ev):
    return collections.OrderedDict([('name', name), ('parent', parent), ('moves_independently', moves), ('shared_resource', shared), ('goes_stale', stale), ('source', source), ('evidence', ev)])
def E(n, who, text):
    q(n, text); return loc(n, who)
entities = [
 ent('project (one per job; forty-one active, twelve of them Cumberland)', None, 'yes', False, False, 'spoken', E(17, M, "I want to start with the project boards.")),
 ent('portfolio layer (company-wide roll-up over the projects; deferred)', None, 'no', False, True, 'spoken', E(13, M, "a roll-up is only as good as the forty things underneath it")),
 ent('program (Cumberland: twelve projects under one owner; served by a filtered view, not a roll-up)', None, 'unknown', False, False, 'spoken', E(25, M, "Cumberland is twelve jobs, not forty.")),
 ent('project template (occupied renovation built; equipment next; ground-up after April)', None, 'yes', False, True, 'spoken', E(66, M, "But I need the equipment one sooner than I thought.")),
 ent('phase', 'project', 'yes', False, False, 'spoken', E(40, W, "The phases are right.")),
 ent('milestone (owner-facing contractual date)', 'project', 'yes', False, True, 'spoken', E(45, W, "First patient day has moved twice on the tower.")),
 ent('milestone date change (new date, date of the change, typed reason)', 'milestone', 'yes', False, False, 'spoken', E(45, W, "They want the history.")),
 ent('health status (red, amber, green; set by the PM)', 'project', 'yes', False, True, 'spoken', E(50, M, "a green row turned out not to be green")),
 ent('health status change (who, when)', 'health status', 'yes', False, False, 'spoken', E(48, M, "I want to know who did that and when.")),
 ent('percent complete (removed from the project)', 'project', 'no', False, True, 'spoken', E(42, W, "Because it's a number I make up.")),
 ent('startup checklist item', 'project', 'yes', False, False, 'spoken', E(70, W, "eighteen is about right for a renovation")),
 ent('startup checklist (the master and the senior PM\'s version, Excel)', None, 'unknown', False, True, 'spoken', E(71, M, "I'll send you my master version and Warren's version")),
 ent('ICRA permit (per work area; expires)', 'project', 'yes', False, True, 'spoken', E(83, W, "But the PM isn't the one who walks it to their nurse.")),
 ent('OAC meeting (weekly owner-architect-contractor meeting; where milestone history is asked for)', 'project', 'yes', False, False, 'spoken', E(45, W, "the question in the OAC is always when did it move and what moved it")),
 ent('person (project manager, superintendent, project engineer)', None, 'yes', True, False, 'spoken', E(57, I, "the answer is four names, and then it's a scheduling problem")),
 ent('occupied-work qualification', 'person', 'no', False, False, 'spoken', E(57, I, "Not scroll sixty people and spot the ticks.")),
 ent('allocation (one person on one project for a timeline at a percent)', 'person', 'yes', False, False, 'spoken', E(59, I, "Everything in there is a commitment.")),
 ent('allocation state (requested, confirmed)', 'allocation', 'yes', False, False, 'spoken', E(59, I, "There's no difference between I've asked for Junie and I've got Junie.")),
 ent("workload view (Who's over; per person per week)", 'allocation', 'no', False, True, 'spoken', E(54, I, "that's the grid basically, except everybody can see it")),
 ent('cost actuals (budget and spent to date, from Sage)', 'phase', 'no', False, True, 'spoken', E(75, M, "He will not give anybody a live connection into Sage this year and I'd stop pushing on it.")),
 ent('PM forecast (cost to complete, forward-looking)', 'project', 'yes', False, True, 'spoken', E(77, W, "The actuals are history. My forecast is the job.")),
 ent('Sage monthly job cost report (the eleventh or twelfth)', None, 'unknown', False, True, 'spoken', E(75, M, "he already produces a job cost report on the eleventh or twelfth and he doesn't much care if somebody uploads it somewhere")),
 ent("PMO director's view (the PMO overview dashboard re-sourced from the projects)", 'project', 'no', False, True, 'spoken', E(33, M, "No, I still want my own screen.")),
 ent('Cumberland January view (filtered list: colour, next milestone, date)', 'program', 'no', False, True, 'spoken', E(25, M, "If those twelve are on decent project boards and I can filter to them and show a list with a color and a next milestone and a date, that's enough for the fifteenth.")),
 ent('the grid (Excel allocation workbook)', None, 'unknown', False, True, 'spoken', E(54, I, "He could answer his own question with that.")),
 ent('fourteen private PM forecast files', None, 'unknown', False, True, 'spoken', E(13, M, "the forty things underneath it are fourteen people's spreadsheets")),
 ent('Monday status email (weekly; retired at go-live)', None, 'unknown', False, True, 'spoken', E(109, M, "The Monday status email is retired at go-live.")),
 ent("preconstruction pipeline (another group's; out of scope)", None, 'unknown', False, False, 'spoken', E(103, M, "Which I'm not asking you for.")),
 ent('project engineer on a project (the ICRA reminder\'s recipient; no field in v0.1)', 'project', 'unknown', False, False, 'assumed', None),
]

def lean(question, option, qs, cond, pattern):
    return collections.OrderedDict([('question', question), ('option', option),
        ('quotes', [q(n, t) for n, w, t in qs]), ('locations', [loc(n, w) for n, w, t in qs]),
        ('condition', cond), ('pattern', pattern)])
P1, P2, P4, P5, P6, P7 = ('one row where the call describes many', 'a pain with no element that fixes it', "our framing labelled as the client's",
    'a shared resource with no reservation tracking', 'an artefact that can go stale with nothing to flag it', 'an expected output the input cannot support')
leanings = [
 lean("Is an owner milestone one row with a baseline and a current date, or a row with its moves as children?",
      "Milestone items stay under the project; every move of the current date becomes a child entry under the milestone (the new date, the date of the change, a typed free-text reason), and the milestone shows the current date, the count of moves and the latest reason. The baseline is the first entry. Whether the entry is a subitem or a dated update written by an automation is the open mechanism; either way the history is on the item.",
      [(45, W, "They want the history."), (45, W, "First patient day has moved twice on the tower."), (47, W, "I'd rather type the reason myself than pick it off a list")],
      "the senior PM says whether a dated list under the milestone answers the OAC question, and the PMs accept typing the reason at the moment the date moves rather than later", P1),
 lean("Is the health audit the column's own activity log surfaced on the item, a last-changed-by and last-changed-at pair written on the item, or both?",
      "Both: a last-changed-by and last-changed-at pair on the item, set by an automation when Health changes, for the glance; the column's change history for the chain. The colour stays the PM's claim about the job; the audit shows who claimed it and when, never that the job is green.",
      [(48, M, "If a PM moves his job from yellow to green, I want to know who did that and when."), (51, W, "And put it on the item, not in a log somewhere."), (50, M, "Then surface it.")],
      "the PMO director confirms that who-and-when of the last change on the item is enough at a glance, with the full chain one click away", P6),
 lean("Which allocation rows count as booked in the workload view, and who may move a row to confirmed?",
      "A state column on the allocation row (requested, confirmed) that only the resource manager may change, with the PMO director as the named substitute; requested rows show in Who's over as tentative and do not count toward a person being over until confirmed. Whether tentative rows should show at all, and what a refused request becomes, is open.",
      [(59, I, "Everything in there is a commitment."), (62, I, "I want to be the one who does it"), (63, I, "somebody has to be able to confirm in my place, and I'd want that to be her and not a PM")],
      "the resource manager decides whether a requested booking appears in the workload at all; and preflight shows whether the build account's tier supports a column permission limited to two named people, otherwise the rule is a documented convention with a notification", P5),
 lean("How does a burn figure show that its actual is a month old, and whose number it is?",
      "Two columns, not one: actuals from the uploaded Sage report with an actuals-as-of report month and the uploader on the project, and the PM's forecast entered on the board and owned by the PM. Burn is computed from the two and labelled with the actuals' month. Until the first upload every actual is a sample value and the board says so.",
      [(75, M, "there's a version of this where the number is a month old and everybody knows it's a month old"), (77, W, "The actuals are history. My forecast is the job."), (73, W, "It's a good-looking screen with made-up money on it.")],
      "the controller's report arrives in a form that maps to phases, or only to projects, and someone is named to upload it on the eleventh or twelfth; the controller's position is relayed and unconfirmed", P6),
 lean("Is Cumberland's January program review a roll-up or a filtered view across the twelve Cumberland projects?",
      "A filtered view across the projects whose Program is Cumberland, showing health, the next owner milestone and its date, with no program total, by the client's decision; the risk that the owner's VP asks for a total stays recorded and owned by her.",
      [(25, M, "If those twelve are on decent project boards and I can filter to them and show a list with a color and a next milestone and a date, that's enough for the fifteenth."), (29, M, "He's a milestones man more than a totals man. But he might.")],
      "the PMO director comes back if Cumberland's VP asks for a program total; until then no total is built and nothing shaped like Cumberland's template is attempted", P7),
 lean("One project template, or one per project type with its own startup list?",
      "One template per project type: occupied renovation (built), equipment (next, before the first week of December), ground-up (after April). Each carries its own startup list; the renovation list gains the preconstruction handover meeting. The lists come from the two checklists the PMO director committed to send.",
      [(70, W, "The equipment one is shorter and it's a completely different list."), (70, W, "You're missing the preconstruction handover meeting"), (66, M, "But I need the equipment one sooner than I thought.")],
      "the master checklist and the senior PM's version arrive (committed on the call, paragraph 71, not received) and the equipment list and milestone set are confirmed before the Waverly MRI starts", P1),
 lean("Who is the project engineer the ICRA reminder goes to, and where does the board hold that name?",
      "A Project engineer people column on the project, so the reminder can notify the project engineer and the superintendent and copy the PMO director; if the engineer differs per work area, the person goes on the ICRA item instead. v0.1 names a PM and a superintendent on the project and no project engineer, so the corrected recipient list cannot be built from the fields that exist.",
      [(83, W, "That's the project engineer, and the super needs to know because he's the one getting shut down."), (83, W, "Send it to both of them and copy her.")],
      "the senior PM says whether one project engineer per project is the rule or whether work areas within a job have different engineers", P7),
 lean("When the startup list changes in a template, how do projects already created from it learn of the change?",
      "Changes are made in the template and applied to live projects by hand as a listed step, with the template version noted on the project; nothing automatic. The list is still changing, since a missing step surfaced on this call, so this is a build mechanic for the user to know, not a client ask.",
      [(70, W, "You're missing the preconstruction handover meeting")],
      "how often the list changes; asked of the PMO director when the two checklists arrive", P6),
 lean("Does the next version carry a company-wide roll-up?",
      "No portfolio layer in this version, by the client's decision, recorded as hers with the two revisit conditions and no date. The projects stay real monday projects so the roll-up is later a connection rather than a rebuild. The PMO director keeps her own view over the project boards: the PMO overview dashboard re-sourced from the three projects, pointed at her and not at a wall. Nothing is aimed at leadership until she says so.",
      [(13, M, "a roll-up is only as good as the forty things underneath it"), (17, M, "I'm asking you not to build it yet."), (19, M, "The fourteen have to be putting their forecast in the thing rather than in their own file"), (19, M, "I want one full month where I haven't had to email anybody for a status."), (33, M, "No, I still want my own screen."), (21, M, "And write down that it was my decision and not yours")],
      "both revisit conditions true, which the client places after January fifteenth and refuses to date; then she takes the roll-up to the VP of Operations herself", P6),
]

def epp(pain, element, verdict):
    return collections.OrderedDict([('pain', pain), ('element', element), ('verdict', verdict)])
element_per_pain = [
 epp('P1.1', "none in this version: the leadership roll-up is deferred by the client; the PMO overview dashboard re-sourced from the three projects is her own view, not a portfolio; the trust the pain names is addressed at the inputs (P1.2 to P1.6) and the roll-up waits on the two revisit conditions (leaning 9)", 'none'),
 epp('P1.2', "the PM's forecast entered on the project (a forecast column per phase, PM-owned), health with its audit, and the Monday status email retired at go-live by the client's commitment; in v0.2 the figures are samples, so the element shows the shape until the fourteen enter their own (leanings 4 and 9)", 'fixes'),
 epp('P1.3', "last-changed-by and last-changed-at on the item when Health changes, with the column's change history behind it (leaning 2); the colour stays the PM's claim and the audit shows who claimed it", 'fixes'),
 epp('P1.4', "the same audit pair on the item, set by an automation when Health changes (leaning 2)", 'fixes'),
 epp('P1.5', "the same audit pair, surfaced on the item rather than left in the activity log where v0.1 had it", 'fixes'),
 epp('P1.6', "milestone date changes as child entries with the date of the change and a typed reason under each milestone (leaning 1)", 'fixes'),
 epp('P2.1', "requested and confirmed states on the allocation row; only the resource manager advances it (leaning 3)", 'fixes'),
 epp('P2.2', "a saved view on the allocation board filtered to occupied-work qualified superintendents", 'fixes'),
 epp('P2.3', "the PMO director as the second named person allowed to confirm during the resource manager's absence; a column permission if the tier allows it, otherwise a documented convention (leaning 3)", 'fixes'),
 epp('P3.1', "actuals from the uploaded monthly Sage report with their report month shown, beside the PM's forecast (leaning 4); until the first report is uploaded the burn column holds sample money, which is the complaint, and the upload is a monthly manual feed v0.1 does not have", "copies-today's-tool"),
 epp('P3.2', "the monthly upload shown as a month old, in place of a live connection (leaning 4); the report is today's report placed on the board with its age, and the pain itself (no live connection) is accepted, not fixed", "copies-today's-tool"),
 epp('P3.3', "percent complete deleted from the project; nothing replaces it", 'fixes'),
 epp('P4.1', "the preconstruction handover meeting added to the renovation startup list, and the two checklists compared when they arrive (leaning 6)", 'fixes'),
 epp('P4.2', "an equipment project template with its own startup list and milestone set (leaning 6)", 'fixes'),
 epp('P4.3', "the ICRA reminder's recipients changed to the project engineer and the superintendent with the PMO director copied, which needs a project engineer field on the project (leaning 7)", 'fixes'),
]
assert [e['pain'] for e in element_per_pain] == sorted(ids, key=lambda s: tuple(map(int, s[1:].split('.'))))
assert set(e['pain'] for e in element_per_pain) == set(ids)

structure = collections.OrderedDict([
 ('products', ['Work Management']),
 ('build_target', 'own-account'),
 ('build_target_reason', "prospect, so the user's own account by default (A21); v0.1 already lives there, and the client's own Enterprise account is closed to anything real until the IT director's security review clears (paragraphs 79 to 81)"),
 ('workspaces', ["Bellamy Ridge PMO (v0.1): the workspace v0.1 was built in (context-v0.1.md), continued under A21's continuation clause because the next version is a change to v0.1 after the client's feedback on the demo; one product, so no second workspace, and no new workspace"]),
 ('native_reuse', "none: no CRM or Service entity in this build. The projects use monday's project tool and project templates, not native CRM or Service boards. The preconstruction pipeline and the parked warranty inbox stay out; if either ever comes in it goes on the native CRM Accounts and Deals boards or the native Service Tickets board, detected first."),
 ('leanings', leanings),
 ('patterns', [
   "parent-row-with-roll-up: project with milestones as child items and each milestone's date changes as child entries (new date, date of the change, typed reason); current date, count of moves and the next owner milestone rolled up",
   "parent-row-with-roll-up: project with phases as child rows; phase budget, uploaded actuals (with their report month) and the PM's forecast rolled up to the project as burn",
   "parent-row-with-roll-up: person with allocation rows (project, timeline, percent, state) as children; the workload rolled up per person per week from confirmed rows",
   "parent-row-with-roll-up: project with startup checklist items as child rows; open items rolled up to the project",
 ]),
 ('element_per_pain', element_per_pain),
])

existing = collections.OrderedDict([
 ('account', "The user's own account holds the v0.1 workspace 'Bellamy Ridge PMO (v0.1)' (context-v0.1.md): the portfolio 'Bellamy Ridge Portfolio' with three connected projects made from the 'Occupied renovation' template (Cumberland bed tower, Waverly cath lab, Pellham fit-out), the 'Resource allocation' board with about sixty seeded people and the 'Who's over' workload view, the 'PMO overview' dashboard reading from the portfolio, and one automation notifying the project manager thirty days before an ICRA expires. All data is sample data; no loaded rates, no patient information. The three client attendees have read-only access to it. The client's own Enterprise account (about 220 seats, preconstruction's bid board, safety's incident board) is bound to nothing and stays untouched until the security review clears; the migration into it, with its seat impact, is a handover question, not a build question."),
 ('incumbents', [
  collections.OrderedDict([('system', 'Sage 300'), ('authority', "stays system of record for: job cost actuals and budgets, invoicing ; follower for: the monthly job cost report uploaded to the project boards and shown with its report month; the PM's forward forecast lives on the board, not in Sage. Writeback and integration direction beyond that upload are unresolved; v0.1 does not depend on either; staying clear of Sage is our safe default, labelled as ours"), ('evidence', loc(75, M))]),
  collections.OrderedDict([('system', 'Procore'), ('authority', "stays system of record for: drawings, RFIs, submittals, daily reports ; follower for: nothing; not requested as an integration and not rebuilt"), ('evidence', E(40, W, "I didn't look at the submittal part because that's Procore's job."))]),
  collections.OrderedDict([('system', 'the grid (Excel allocation workbook)'), ('authority', "stays system of record for: allocations until confirmed bookings live on the allocation board (assumed cutover, not discussed) ; follower for: nothing; replaced, not mirrored"), ('evidence', loc(54, I))]),
  collections.OrderedDict([('system', 'fourteen private PM forecast files (Excel)'), ('authority', "stays system of record for: each PM's cost-to-complete until that PM enters the forecast on the board (the first revisit condition) ; follower for: nothing; replaced at adoption"), ('evidence', loc(19, M))]),
  collections.OrderedDict([('system', "startup checklists (the PMO master and the senior PM's version, Excel)"), ('authority', "stays system of record for: nothing once the per-type templates hold the lists ; follower for: nothing; inputs to the templates, committed to be sent"), ('evidence', loc(71, M))]),
  collections.OrderedDict([('system', 'the Monday status email'), ('authority', "stays system of record for: weekly status until go-live ; follower for: nothing; retired at go-live by the client's commitment, which is done only when the email stops"), ('evidence', loc(109, M))]),
  collections.OrderedDict([('system', 'Microsoft 365, Teams and the client tenant'), ('authority', "stays system of record for: identity and single sign-on, pending the IT director's questionnaire ; follower for: nothing; nothing of the build touches the tenant"), ('evidence', loc(79, M))]),
  collections.OrderedDict([('system', "the client's own monday Enterprise account"), ('authority', "stays system of record for: preconstruction's bid board and safety's incident board ; follower for: nothing; untouched until the security review clears, by agreement on the call"), ('evidence', E(81, M, "That's how it has to be. He'd find out."))]),
  collections.OrderedDict([('system', 'Smartsheet (abandoned 2023 pilot)'), ('authority', "stays system of record for: nothing ; follower for: nothing; adoption history, not an integration"), ('evidence', None)]),
 ]),
])

def A(s, qq): return collections.OrderedDict([('statement', s), ('question', qq)])
assumptions = [
 A("Milestone history is kept as child entries under the milestone (subitems or dated updates written by an automation) and the milestone shows the current date and the latest reason.", "Is a dated list under the milestone, with the typed reason, what the OAC needs; subitem or update entry?"),
 A("The health audit is a last-changed-by and last-changed-at pair on the item written by an automation, with the column's change history behind it.", "Is who-and-when of the last change on the item enough, or must the whole chain be visible on the item?"),
 A("The Sage report month is shown per project as actuals-as-of, and the PMO uploads the report on or after the eleventh or twelfth; with the PMO analyst on leave from November, the uploader is unnamed.", "What does the report contain, by job or by phase, in what format, who uploads it and on which day?"),
 A("Requested allocation rows show in Who's over as tentative and do not count toward over-capacity until confirmed.", "Should a requested booking appear in the workload at all, and what does a refused request become?"),
 A("The build account's tier supports a column permission limiting the state column to two named people.", "Preflight: does the user's own account plan allow column permissions; if not, the rule is a convention with a notification."),
 A("One project engineer per project is enough for the ICRA reminder, held in a people column on the project.", "Is there one project engineer per project, or do work areas within a job have different engineers?"),
 A("The equipment template's startup list and milestone set come from the two checklists the PMO director committed to send.", "Which items and milestones make the equipment template, and is eighteen plus the preconstruction handover meeting the renovation list?"),
 A("The ground-up template waits until April.", "Confirm nothing ground-up starts before April."),
 A("The PMO director's view is the PMO overview dashboard with its six widgets re-sourced from the three project boards, and it scales to six pilot projects and then forty-one.", "Which project-level fields should her view show, and is a dashboard over the project boards enough as the count grows?"),
 A("Cumberland projects are identified by the Program value on the project (context-v0.1.md) and the January view is a filter on it, with no total and nothing shaped like Cumberland's template.", "Is a filtered list of the twelve Cumberland projects enough for the owner's VP, and should anything be exportable in Cumberland's own template?"),
 A("Changes to a startup list are made in the template and applied to live projects by hand as a listed step.", "How often does the list change, and who applies a change to projects already running?"),
 A("v0.2 keeps v0.1's sample data, the three real job names and no loaded rates; the three Chattanooga pilot projects stay unbuilt.", "Are the Chattanooga pilots wanted in v0.2, or at six projects later?"),
 A("Go-live is the date the fourteen start entering their forecast on the board and the Monday status email stops; no date is set.", "What date is go-live, what replaces the email operationally, and who tells the fourteen PMs?"),
 A("The speakers are as inferred from direct address and content; every attribution is speaker-unclear until confirmed.", "To the user: confirm which paragraphs are the PMO director's, the senior PM's and the resource manager's before any tie is treated as that person's."),
 A("The next version stays in the user's own account (A21) in the existing v0.1 workspace; the client's tenant enters only after the security review.", "To the user, for handover: what is the migration path into the client's Enterprise account once the IT director signs off, and the seat impact he asked about?"),
 A("The preconstruction pipeline and the warranty inbox stay out of this build.", "Settled separately, not at the next session: does preconstruction want a pipeline view, and when does the warranty inbox come off the shelf?"),
 A("The revisit of the portfolio layer is a diarised conversation after January fifteenth tied to the two conditions, not a build commitment.", "Is that the user's understanding too, and should the two conditions be written into the scope as the revisit test?"),
]

def U(need, clock, why): return collections.OrderedDict([('need', need), ('clock', clock), ('why_not_met', why)])
unmet_needs = [
 U("A trustworthy company-wide roll-up for leadership (P1.1)", "next quarter, after January fifteenth; the client refuses to pin a date", "deferred by the client's decision until the fourteen enter their forecast on the board and she has one month without chasing a status; nothing in this version is aimed at leadership"),
 U("A program-level total for Cumberland's January review", "January fifteenth", "the client chose a filtered list of the twelve Cumberland projects with no total and carries the risk that the owner's VP asks for one"),
 U("Live burn actuals from Sage (P3.2)", "none this year, by the controller's decision", "no live connection this year; a monthly upload, knowingly a month old, is the agreed shape"),
 U("Burn figures the senior PM can say yes to (P3.1)", "the next showing, Thursday the fifteenth", "every figure is a sample until the first Sage report is uploaded; the report's content, format and uploader are unconfirmed"),
 U("Answers for the IT director: where the build sits and how many enterprise seats it consumes", "this week (the Consultant's commitment)", "not a build element; a prerequisite for anything entering the client's tenant; committed, not sent"),
 U("Microsoft single sign-on, restricted columns and permissions inside the client's tenant (carried from s8)", None, "cannot be shown in the user's own account; the client's tenant is closed until the security review clears; the need stays recorded"),
 U("A pipeline view for preconstruction (relayed from the VP of Operations)", "January, when he is expected to ask again", "not requested by the client; another group's; CRM-shaped and out of this build; a backlog seed"),
 U("Post-turnover warranty calls (parked in s8)", None, "parked by the client for this year and not mentioned on this call; stays recorded, not revived"),
]

def AI(p, kind, basis, idea): return collections.OrderedDict([('pain_or_need', p), ('kind', kind), ('round', 2), ('probe_basis', basis), ('idea', idea)])
ai_opportunities = [
 AI('P1.6', 'workflow', 'P-21', "When a milestone's current date changes, a workflow writes a dated history entry under the milestone and asks the PM for the typed reason, so no move is recorded without one."),
 AI('P1.4', 'workflow', 'P-21', "When Health changes, a workflow stamps last-changed-by and last-changed-at on the item and posts the change as an update, so the audit sits on the item."),
 AI('P2.1', 'workflow', 'P-21', "When an allocation is set to requested, a workflow notifies the resource manager (or the PMO director during her absence) with the person, project and dates, so confirmation is a deliberate act."),
 AI('P1.2', 'ai_column', 'unprobed', "An AI column on the project that summarises the week's updates into a one-line status for the PMO director's view, replacing the narrative half of the retired Monday status email; the colour and the forecast stay typed by the PM."),
 AI('P3.1', 'agent', 'P-19', "An agent that reads the uploaded monthly job cost report, maps its lines to phases and proposes spent-to-date values with the report month, writing nothing until the uploader approves each mapping; sample values until the first real report."),
]

verdict = collections.OrderedDict([
 ('cleared_for', 'build'),
 ('conditions', [
   "approval stop",
   "no A11 question first matters here: the target is the user's own account, where sample data needs no decision (A21); the three A11 decisions stay open",
   "the build continues in the existing v0.1 workspace in the user's own account (A21's continuation clause: a change to v0.1 after demo feedback); no new workspace, and the plugin writes into no other workspace",
   "the client's own Enterprise account stays untouched until the IT director's security review clears (paragraphs 79 to 81); the answers he needs are committed by the Consultant for this week, not sent",
   "every burn figure stays a sample until the first Sage report is uploaded; the controller's position is relayed and unconfirmed (paragraph 75)",
   "the two startup checklists are committed by the PMO director (paragraph 71), not received; the equipment template cannot be finished without them",
   "committed, not done: the invite for Thursday the fifteenth at 11:30 Eastern (Consultant, paragraph 115); the two further PMs' hours (PMO director, before the fifteenth, paragraph 117); the retirement of the Monday status email at go-live (PMO director, paragraph 109); each becomes done only on evidence",
   "every attribution is inferred, since the transcript has no speaker labels; the user confirms who said what before any client tie is treated as that person's",
   "the portfolio layer is not built; the two revisit conditions are recorded as the client's and no date is set",
 ]),
 ('reason', "Five pain themes have entities and outcomes in the client's own words, the one product is chosen, the structure is a change to v0.1 stated with nine leanings, and the target is the user's own account in the existing v0.1 workspace."),
])

def Q(text, kind, role, known): return collections.OrderedDict([('text', text), ('kind', kind), ('role', role), ('known', known)])
questions = [
 Q("On allocation, what sits between requested and confirmed, what happens to a request you refuse, and should a requested booking show in Who's over as tentative or not at all until you confirm it?", 'discovery', 'Resource Manager',
   "every row today is a commitment (paragraph 59); only she confirms (paragraph 62); the PMO director covers Thanksgiving week (paragraphs 63 and 64); the saved view of the four qualified superintendents is agreed (paragraph 57); v0.1 has no state and no permission model (context-v0.1.md)."),
 Q("You said 'the question in the OAC is always when did it move and what moved it'. If every move sits under the milestone as a dated entry with your typed reason, and the milestone shows the current date and the latest reason, does that answer the OAC? And for health, is who-and-when of the last change on the item enough, with the full chain behind it?", 'read-back', 'Senior Project Manager, with the PMO Director for health',
   "first patient day moved twice on the tower (paragraph 45); the reason is free text (paragraph 47); the audit goes on the item, not in a log (paragraph 51); v0.1 holds baseline versus current only and no audit on the item (context-v0.1.md)."),
 Q("You said Roland 'already produces a job cost report on the eleventh or twelfth and he doesn't much care if somebody uploads it somewhere'. What does the report contain, by job or by phase, in what format, who uploads it and on which day, so the board can show actuals as of that month beside the PM's forecast?", 'read-back', 'PMO Director, then the controller',
   "no live connection this year (paragraph 75); the forecast lives on the board (paragraph 77); every v0.1 figure is a sample (paragraph 73; context-v0.1.md); the PMO analyst is on leave from November."),
 Q("You said 'the PM isn't the one who walks it to their nurse. That's the project engineer'. Is there one project engineer per project, or do work areas within a job have different engineers, so the board knows who the ICRA reminder goes to?", 'read-back', 'Senior Project Manager',
   "thirty days is right (paragraph 83); recipients are the project engineer and the superintendent with the PMO director copied (paragraph 83); v0.1 names a PM and a superintendent on the project and no project engineer (context-v0.1.md)."),
 Q("You said 'The equipment one is shorter and it's a completely different list.' When the master checklist and Warren's version arrive, which items and which milestones make the equipment template, and is eighteen plus the preconstruction handover meeting the renovation list?", 'read-back', 'PMO Director and Senior Project Manager',
   "occupied renovation is built (context-v0.1.md); the equipment template is needed before the Waverly MRI in the first week of December (paragraph 66); ground-up waits until April (paragraph 68); the two checklists are committed, not received (paragraph 71)."),
]
# read-back quotes inside question text are also proven at their paragraphs
q(45, "the question in the OAC is always when did it move and what moved it")
q(75, "already produces a job cost report on the eleventh or twelfth and he doesn't much care if somebody uploads it somewhere")
q(83, "the PM isn't the one who walks it to their nurse. That's the project engineer")
q(70, "The equipment one is shorter and it's a completely different list.")

readiness = collections.OrderedDict([
 ('schema', 'readiness/1'),
 ('note', "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top)."),
 ('pains', pains), ('signals', signals), ('entities', entities), ('structure', structure), ('existing', existing),
 ('assumptions', assumptions), ('unmet_needs', unmet_needs), ('ai_opportunities', ai_opportunities), ('verdict', verdict), ('questions', questions),
])
# no sales vocabulary in the block
blob = json.dumps(readiness, ensure_ascii=False)
for bad in [r'\bR\d{1,2}\b', r'\bMet\b', r'\bPartial\b', r'\bMissing\b', r'\bgate\b', r'\bverdict\b(?!")', r'Nearly ready', r'Discovery complete', r'\bgrade', r'\bbleed\b', r'\bupside\b', r'rubric']:
    hits = [m.group(0) for m in re.finditer(bad, blob)]
    hits = [h for h in hits if not (bad == r'\bverdict\b(?!")')]
    assert not hits, (bad, hits)
assert '"verdict"' in blob and blob.count('verdict') == 1 + len(element_per_pain)  # the field names only
d['readiness'] = readiness
assert list(d.keys())[-1] == 'readiness' and len(d) == 26
open(KEY, 'wb').write((json.dumps(d, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))
print('written; proofs', len(proofs), 'distinct', len(set(proofs)))
print('pains', len(pains), 'signals', len(signals), 'entities', len(entities), 'with parent', sum(1 for e in entities if e['parent']),
      'leanings', len(leanings), 'epp', len(element_per_pain), 'incumbents', len(existing['incumbents']), 'assumptions', len(assumptions),
      'unmet', len(unmet_needs), 'ai', len(ai_opportunities), 'questions', len(questions), 'conditions', len(verdict['conditions']))
