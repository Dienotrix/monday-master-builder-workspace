# s7-discovery-service-desk — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s7-discovery-service-desk/answer-key.json` only. `transcript.txt` is unchanged (267 cues; the mess pass applies to s12 to s25 and no FEEDBACK entry asks for an edit here). There is no README and no `intake` field, so the direction rename does not apply. FEEDBACK.md has no entry for s7, so the pass here is the sweep, the "never written to" rule, the standing lines and the readiness block.

Method: the key was loaded, changed and dumped by script (`indent=2`, `ensure_ascii=False`, trailing newline) after a round trip without changes had reproduced the file byte for byte. The script changes four existing strings, each after asserting the old value, and appends `readiness` as the 26th and last field; nothing else is touched, by construction. Every quote the block introduces was proven verbatim in its cited cue before the file was written (55 proofs in the script, including the five `outcome` strings, which carry no location in the brief's shape and so are not seen by the shared verifier). The build target is own-account, as the task set: the client is a prospect, and under A21 their own live monday account is the handover target, not the proof-of-concept target.

A note for the planner: the session scratchpad is shared between the agents of this pass, and a scratch copy of the untouched key under a generic filename was overwritten by a sibling agent (an s3 key) between my copy and my diff. The fixture files were never at risk (each agent writes only its own fixture folder), but editors should keep scratch files under a per-fixture name.

## 1. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit becomes a `structure.leanings` entry; where a builder reading an existing field alone would build the flaw, that field was corrected too. Eleven leanings in all.

1. **One row where the call describes many.** One hit, in the later phase.
   - Preventive maintenance. "Every contract has a schedule in it. So many filter changes, so many inspections, quarterly this, annual that." (cue 41, Yvette Carnahan): one contract carries many visits that come due and complete independently, and the monthly report needs their completion rolled up. Leaning 5: contract as parent, visits as child rows, completion rolling up; later phase, in its own Work Management workspace. No field corrected: the vocabulary entry for PM already says "a separate recurring-schedule structure" and never proposes one row per contract.
   - Considered, not a hit: client and building. The key already says a client has many buildings and a work order belongs to a building (traps, vocabulary, `expected_structures.notes`). Leaning 4 adds the roll-up and the label, which is pattern 4 below. Escalation was also considered: "getting texted about the same job by three different people" is many texts for one job, which is the opposite flaw, and nothing says one work order is escalated more than once; the entity carries `moves_independently: unknown`.
2. **A pain with no element that fixes it.** Six pains carry `none` in `element_per_pain`, all kept visible, and four leanings carry them.
   - P4.1 and P4.2 (the client portals): the first build leaves the re-keying as it is; the board replaces the spreadsheet copy, so the work order is still keyed into the portal and once into monday. Leaning 7 says the board can record that the portal was updated, as a person's claim.
   - P5.1 and P5.2 (knowledge in the help desk lead and the binder): the client said "Not first." Leaning 8 names the cheap start (per-building fields on the building record the build already needs) and leaves articles for later.
   - P6 (Roanoke): nothing in the key's structure names a branch. Leaning 9.
   - P8 (after-hours email): "an emergency at seven at night is an email nobody's looking at" (cue 53) and the first cut as played back has no element for it. Leaning 6 names an answering-service form and a named owner of the inbox after six, labelled as our idea. Both land in `unmet_needs` as well (s15 line, section 3).
3. **An alias-map entry that names more than one entity.** No hit. s7 has no alias map. The nearest candidates in `vocabulary`: "portal", which names two different things but says so and separates them, so it is a disambiguation rather than a collapse; "the binder / the folder on the SharePoint", two artefacts under one term, neither a person, place or organisation; "building / property", one thing with two names. Nothing split.
4. **Our framing labelled as the client's.** Two soft hits, both corrected, and the four-part first cut checked and left (the traps already call it the Consultant's play-back, agreed in draft).
   - "Site" is our modelling word; the client says building or property, and the vocabulary already says so. `entities_and_workflows[11]` nevertheless read "Client, site and contact knowledge". **Corrected** to "Client, building and contact knowledge ('building' is their word; 'site' is ours, see vocabulary)". Leaning 4 fixes the label and the shape: client, then building, then work order, response-time results rolling up per building and per client, which is what the county RFP asks for (cue 182). Condition: that "building" covers what they also call a property ("Marley at the Ridgeline property", cue 16).
   - `expected_monday_products[0].why` said v1 carries priority and target date, "which is what the client said she needs for December". The shape is the Consultant's (cue 224); what she said she needs is to see what is late ("As long as I can see what's late. That's what I need in December.", cue 225). **Corrected** to say whose proposal it is and what her condition was.
5. **A shared resource with no reservation tracking.** Two hits.
   - Technicians across work orders. The whiteboard is today's reservation ("techs down the side, days across the top, and whoever's dispatching moves magnets around", cue 30; "The whiteboard is the truth.", cue 32), and the key's first cut has no element for who holds which technician on which day. Leaning 1: technician and day on the work order, a per-technician per-day view as the whiteboard's shape in monday; until the dispatcher works from it, the whiteboard stays the schedule and the fields on the work order are what the desk keyed. The vocabulary entry for the whiteboard ("the scheduling view that has to be replaced or respected") is incomplete rather than wrong, so it stands.
   - Field supervisors across escalations. Leaning 10: one escalation per work order, the supervisor's own acknowledgement on his phone as the state, a per-supervisor view in place of the legal pad. The escalation vocabulary entry ("status plus owner change on the ticket") stands for the same reason.
   - Declined: outside vendors (mentioned once, never said to be booked across jobs; carried in `unmet_needs` as an unprobed need), and Fairlane's badges and escorts (an access requirement, not a booking).
6. **An artefact that can go stale with nothing to flag it.** Three hits, the central ones for this fixture.
   - The closure date. "Except the date it was closed is the date I typed it in, which might be two days after he actually did it." (cue 103). A report built on a board's closed status inherits the flaw, which the key already calls a design constraint. Leaning 2: two dates on the work order, the field completion as reported and the desk closure, with the report on the first; until technicians close from a phone, every closed date is the desk's claim and says so. No field corrected: `entities_and_workflows[4]` and the trap already state the fact.
   - The target date. In v0.1 the window behind each target date is keyed by a person from memory of the contract; a target date set from the wrong or an old window shows nothing. Leaning 3: the window per client and priority as a lookup on the client record, the work order showing the window it was set from, SLA policy setup still deferred. The vocabulary entry for "the clock" is incomplete rather than wrong and stands.
   - The board beside the spreadsheet. "they were already typing it into the spreadsheet, so now it's two places. So they did the spreadsheet" (cue 60) is the client's own account of how a second copy drifts and dies. Leaning 11: the board replaces the spreadsheet on day one or it is the old tracker again. Odette's PM spreadsheet, the binder's folder and the dead work order tracker carry `goes_stale: true` in `entities` without a leaning of their own; each is out of the first version.
7. **An expected output the input cannot support.** One hit, corrected. `transcript_format` said "Three long turns continue into a second or third cue" and then listed two (174 into 175; 241 into 242 and 243). A recount of consecutive same-speaker cues finds exactly those two turns, plus the duplicated pair 13 and 14 and the mis-attributed cue 33 that the key already explains. **Corrected** to "Two long turns continue into a second or third cue". The other statistics were recounted and hold: 267 cues from 00:00:03,000 to 00:41:28,290; 5,401 alphanumeric tokens (apostrophe suffixes attached) excluding labels and timings; client talk share 62 percent (61.8 if cue 33 is counted as the Consultant's); the longest Consultant cue 89 words at cue 217. The arithmetic in `numbers` (65 x 35 = 2,275; x 52 = 118,300; the reporting components summing to 24 against her "Call it twenty") is correct and already labelled as the Consultant's on an unconfirmed rate. Every absolute date is held open as the key says.

## 2. The "never written to" rule

s7 is not among the eleven keys FEEDBACK lists. A search of the key for "never written", "written to", "written back", "write back", "writeback", "never touch", "not written", "read-only", "one way", "untouched" and "stays the source" found no no-write claim. Checked and left:
- `expected_structures.notes`: "Sage 300 remains the system of record for money and PM schedules." A book-of-record statement, not a no-write rule, and it traces to the client ("Invoicing comes out of there, and the contract values sit in there.", cue 45; "They live in Sage.", cue 43).
- `expected_questions_before_building[10]`: "does anything need to reach Sage 300 in v1 or does Sage stay untouched?" is a question, which is the right shape.
- "The two client-owned portals stay manual in v1" (`expected_structures.notes`, `vocabulary["portal"]`) traces to the client: closing in the portal is a payment condition (cue 145) and the API sits in Brightmoor's tenant behind an unanswered email (cue 140).
- `accepted_behaviours[10]`: "leaving the safety and estimating boards untouched" is about the client's own monday boards, which under A21 the proof of concept never writes into; a workspace rule, not an integration claim.

The block's `existing.incumbents` entries for Sage 300, ServiceChannel and Fairlane's system use the rule's wording from the start: writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the system is our safe default, labelled as ours.

## 3. Standing lines, where they bite

- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Bites once. `commitments_and_next_steps[0].what` read "a one-hour scoping session with Yvette and the CFO, with Tansy for the first half", as if the CFO were attending. On the call the CFO's attendance is Yvette's prediction ("If I tell him it's about the January renewal, he'll come.", cue 200), the time waits on his month-end (cue 249), and Tansy comes "for the first half of it if she can" (cue 246). **Corrected** to "Committed on the call: ... the CFO to be asked by Yvette (his attendance is not confirmed ...), and Tansy for the first half if she can; send three candidate times. Nothing is sent or confirmed yet." The field's existing tail about the missing time is kept as it is. The same state is a verdict condition. The other nine commitments already carry owner, purpose and a date or "no date stated", and none is recorded as done. No `status` field was added, since that would change the shared s1 to s10 shape.
- **s22 (a board status set by a person is a claim, never evidence that the source system changed).** Bites in four places, all in the block: the closed date keyed by the desk is a claim about the field until the technician closes from his own phone (leaning 2, P2.3, P7); "closed in client portal" on a work order is a claim and the portal is the evidence, with payment depending on the portal (leaning 7, assumption 12); the technician and day on a work order are what the desk keyed while the whiteboard stays the schedule (leaning 1); and an escalation state set by the sender is a claim, where the supervisor's own acknowledgement on his phone is the event (leaning 10, P3.2).
- **s11 (inference targets questions; it never fills evidence).** Six unconfirmed client ties are in `signals`, each naming what was never confirmed, and two of them drive the two `read-back` questions. The return visit, whose shape is inferred, carries `source: assumed` and `evidence: null`.
- **s15 (a product limit never deletes a client need).** Eleven entries in `unmet_needs`: the three deferred Service extras with their clocks (the December quarterly and the January renewal; "the one that bit us in July"), Microsoft sign-in and technician access, which cannot be shown in the user's own account against the client's tenant, the preventive maintenance side and the knowledge base ("not first"), less re-keying into the portals, vendor coordination, after-hours cover and Roanoke.

## 4. The readiness block, field by field

- `pains`: the key's eighteen `pains` entries in array order, same quotes and locations. The key groups them under five themes with three unnumbered at the end, so the ids are P1.1 to P1.5, P2.1 to P2.3, P3.1 to P3.3, P4.1 and P4.2, P5.1 and P5.2, and the three unnumbered pains take the next free numbers as P6 (Roanoke), P7 (paper tickets on Friday) and P8 (after-hours email), each being a different theme. P1 to P3 are `excavated` and the rest `stated`, as the key's own themes say. `outcome` is verbatim from cue 186 (P1.x: "Every work order is in one place, with a clock on it and a name on it..."; P2.x: "...the numbers on my slide came out of the system, and I can click into any line of it while they're watching."), cue 180 (P3.x: "And I'd stop being the escalation path."; P4.x: "Rosalie and Miriam would be doing account work..."), and cue 187 (P5.x: "I'd like to go on vacation and have it still work."); P6, P7 and P8 carry null, because no outcome words aim at them (her "what stops the Friday afternoon chiller happening again?" at cue 220 is a question, not an outcome).
- `signals`: six. Tansy's "if it just stopped being an inbox I'd take that today"; Yvette's "I can live with that"; the adoption test "Not typing the client and the building and the contact"; the IT admin's "fairly sure" API; "He'll look at it on a phone in a parking lot, or he won't look at it at all"; and the CFO prediction.
- `entities`: thirty-one, answering "what moves independently of what?"; twenty-seven have a parent and all carry `moves_independently`. Technicians and field supervisors are the shared resources. Thirteen entities carry `goes_stale: true`: the service-level window (a keyed target date is wrong once the contract changes), the service inbox, the target date, the dispatch assignment, the spreadsheet, the legal pad, the completion report, the closure timestamp, the portal closure, Odette's spreadsheet, the monthly report, the knowledge item and the client's old boards. The return visit is `assumed` with no evidence.
- `structure`: product Service only, with Work Management for the preventive maintenance side and possibly the knowledge base named as a later product that gets its own workspace then (A21); `own-account` with the brief's reason string; one workspace, "Ainsworth – Service", with the en dash, which makes the formerly ASCII key UTF-8; native reuse is the Tickets board relabelled "Work Orders" in the user's own account, client, building and contact records on whichever native board the account already holds, and no companion added unasked; eleven leanings; two parent-row-with-roll-up patterns (building with work orders, rolled up again to the client; contract with PM visits, later phase); eighteen `element_per_pain` rows, eight `fixes`, four `copies-today's-tool` (P1.4 the Friday-afternoon email, P2.2 and P2.3 the report on a typed closed date, P7 the paper ticket) and six `none` (P4.1, P4.2, P5.1, P5.2, P6, P8).
- `existing`: "unknown, no account bound" for the user's own account, read at preflight; the client's own live account described and placed at handover under A21; eleven incumbents with what each stays the record for.
- `assumptions`: fifteen, each with the question that would replace it. Two are routed to the user or to preflight (which sample values may appear; whether Service is provisioned on the bound account).
- `unmet_needs`: eleven, as in section 3.
- `ai_opportunities`: five, all round 2 because the client never asked for AI or workflows (the IT admin was asked whether the portal could be automated and answered about an API). The two workflows cite P-21 and the agent P-19; the two AI columns are `unprobed`. None states a credit figure or price.
- `verdict`: `build`. The reason names the three pains with entities and outcomes in the client's words, the product, the eleven leanings and the target. Eight conditions, starting with the approval stop and the A11 point (none bites for an own-account target; the three decisions stay open), then preflight on the user's own account, the new workspace, neutral sample data, the supervisor conversation before escalation is designed, leaning 11 before the demo claims the inbox pains, and the scoping session as committed rather than booked.
- `questions`: five, the ceiling, in build terms. Q1 and Q4 are read-backs because signals exist (the inbox tie and the day-one acceptance; the whiteboard line and the old tracker's death); Q2, Q3 and Q5 are discovery. Reused from the key's pool of fifteen: item 7 in Q2, item 8 in Q3, items 6 and 9 in Q5; Q1 and Q4 are new, built from the signals. Dropped from the pool for this block: items 1, 2 and 4 (the account, plan, native boards, old tracker and workspace questions move to preflight on the user's own account and to handover for the client's account under A21), item 3 (the CFO's rate; sales material, v2), item 5 (volumes; assumption 14), item 10 (access and seats; `unmet_needs` and assumption 14), item 11 (integrations; leaning 7, v0.1 does not depend on it), item 12 (Roanoke; assumption 8 and leaning 9), items 13 and 14 (PM and the knowledge base; assumptions 15 and 7, leanings 5 and 8), item 15 (scope and decision; v2). Everything dropped stays in the record as an assumption with its question.

## 5. Left as it is, and flagged

- `should_plugin_propose_a_build: true` and the key's verdict agree with `build`, so the `note` carries only the brief's standard sentence.
- The key's `expected_questions_before_building` still opens with two "blocking" account questions about the client's own account. They are right for the handover and wrong for the proof of concept under A21, where the user's own account is read at preflight. The list is left as it is, as in s1; `existing.account` says where each question now lives. For the planner: whether the s1 to s10 keys' account questions should be relabelled handover questions in one pass.
- Two cells in the vocabulary (the whiteboard, escalation) and one in the first cut (the queue) are incomplete rather than wrong and stand; leanings 1, 10 and 11 carry what they lack.

## 6. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 18 (11 excavated, 7 stated) |
| signals | 6 |
| entities | 31 (27 with a parent, all with `moves_independently`; 2 shared resources; 13 that go stale; 1 assumed) |
| leanings | 11 |
| element_per_pain | 18 (8 fixes, 4 copies-today's-tool, 6 none) |
| incumbents | 11 |
| assumptions | 15 |
| unmet needs | 11 |
| AI opportunities | 5 (all round 2) |
| existing fields corrected | 4 (`transcript_format`, `entities_and_workflows[11]`, `expected_monday_products[0].why`, `commitments_and_next_steps[0].what`) |
| transcript edits | 0 |
| key size | 2,271 lines, from 1,273; 26 top-level fields |
| quote-location pairs | 193, from 145 (18 pains, 6 signals, 24 leaning quotes added) |

Counts COVERAGE tracks for s7 that did not move: traps 35, pains 18, vocabulary 16, expected questions 15, entities_and_workflows 16, commitments 10, requested changes 2/4/0, look-alike traps 12, native boards 5, transcript 267 cues. The `quote` fields count in COVERAGE's second table moves from 144 to 192.

## 7. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s7-discovery-service-desk`, run after the single edit that touched quotes (the build script), exit code 0:

```
Fixture: s7-discovery-service-desk
Sources: transcript.txt (transcript/srt, 267 units)

pairs found      193
verified         193  (of which presence only, no location cited: 29)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes: the transcript was not edited, so no unit was renumbered. The build script's own walk proved 55 quote strings verbatim in their cues before writing, including the five `outcome` strings the shared verifier does not see.
