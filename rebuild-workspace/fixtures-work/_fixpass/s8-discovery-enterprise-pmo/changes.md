# s8-discovery-enterprise-pmo — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s8-discovery-enterprise-pmo/answer-key.json` only. `transcript.txt` is unchanged (417 cues, 57,171 bytes, still ASCII; no FEEDBACK entry asks for an edit and the mess pass of the s11 rule applies to s12 to s25, not here). There is no README for s1 to s10, so there is none to bring in line. The key was loaded, changed and dumped by script with its existing two-space indentation and trailing newline, after a round trip without changes had reproduced the file byte for byte. The 25 fields keep their order; `readiness` is the 26th and last; there is no `intake` field, so the `direction` rename has nothing to touch and `direction_of_show` is absent. The key was ASCII before and is UTF-8 now, because the workspace name carries the brief's en dash; the `transcript_format` field's "ASCII only" describes the transcript, which is still ASCII.

FEEDBACK.md has no entry for s8, so the fixture-specific items are none. What was applied: the seven-pattern sweep, the "never written to" rule, the four standing lines where they bite, the readiness block in the brief's shape, and the build target the task set: own-account, a prospect, with the portfolio default of A6 applied to the structure.

## 1. The seven-pattern sweep

Each hit became a `readiness.structure.leanings` entry. A field was corrected only where a builder reading it alone would build the flaw; where a field was merely incomplete, the leaning carries the addition and the field stands (exemplar rule, brief section 8).

**One row where the call describes many.** Three hits, one field corrected.
- ICRA permits. `vocabulary["ICRA"].likely_monday_object` read "a dated, expiring item or date column inside the occupied-renovation project template, with a reminder automation". The permit is per work area ("And it's per work area, and it expires.", cue 65) and a job carries several work areas, so one date column on the project would hold one expiry for many permits, which is the PDF-in-a-folder failure in a new shape. **Corrected** to child items under the project, one per work area, the earliest expiry rolled up, a reminder before it, never a single date column. Leaning 2.
- Owner milestones. The key already has this right (the trap "Milestones are not one date", the vocabulary entry "milestone items under the project, not a single date column"). Leaning 1 states the parent-row shape: milestone rows under the project, several per phase, a contractual flag, the previous date kept when one moves, the portfolio showing the next incomplete milestone and whether it moved (cue 304). No field corrected; the condition is the real milestone list per type and what "next" means.
- The program. "their vice president of facilities wants to see it as one thing, not as twelve rows inside my forty" (cue 41): a program is many rows the owner wants to see as one thing, and a flat portfolio has nothing that is the program. Leaning 4 leans to one portfolio with a program attribute and a per-program view rather than a portfolio per program, and says both shapes stay acceptable and the choice is asked (the key's `accepted_behaviours` already says so). No field corrected.
- Considered and not counted: the grid. `vocabulary["the grid"]` says "a resource or allocation board with a workload view", which is incomplete rather than wrong (a workload view works from one item per assignment). The shape lands in leaning 3 under the shared-resource pattern instead.

**A pain with no element that fixes it.** Three pains carry `none` in `element_per_pain` and stay visible; two of them share a leaning.
- P5.1 and P5.2, the warranty inbox. Nothing in this build touches it, by the client's own parking ("It's not this year's mess.", cue 222). Leaning 10, and an entry in `unmet_needs`.
- P3.1, Sage actuals arriving on the twelfth for August. No element changes when Sage closes the month. The forecast element of leaning 5 gives earlier sight of committed cost, which is P3.2's fix, not this one's, and the row says so.
- Leaning 9 (the field path) also sits under this pattern: nothing in v0.1 reaches the superintendents who are "told on a Friday that Monday changed" (cue 164); the allocation view reaches the PMs. The PM stays the entry point and a two-field update is shown as an option.
- One `copies-today's-tool`: P2.6, the Speaker 2 line about a reshuffle in a meeting the resource manager is not in. A board shows only the bookings people key, and preconstruction, which does the reshuffling, "is not my group" (cue 56). The leaning and question 3 carry the condition.

**An alias-map entry that names more than one entity.** No hit. s8 has no alias map. The nearest candidate is "Cumberland", which the call uses for a health system (Cumberland Health), a program, and two jobs (the bed tower, Cumberland West). The key never collapses them, and the `entities` list keeps them apart (health system, program, project). Checked and left: "job / project" (one thing, two words, the client's own interchange), "turnover, punch list, closeout" (three stages of one sequence), "the owner" (one thing, the health system).

**Our framing labelled as the client's.** One soft hit, one field corrected.
- `expected_structures.notes` listed "a request-and-confirm step" among "Structures the call demands". The client said "I had him confirmed. Verbally." (cue 155) and "Verbally, in the hall, which is the problem." (cue 156); nobody said request-and-confirm. The key's question 10 already phrases it as a question, which is right; the notes did not. **Corrected** so the notes say the qualification is the client's and the request-and-confirm step is ours and is asked. Leaning 3 labels it the same way.
- Checked and left: the five-item scope (the Consultant's playback, agreed out loud with "Yes. Those five.", cue 380, then amended by two client speakers, so it is the client's by agreement); "three templates" (the client's correction, cue 212); the automation candidates in the traps (already labelled "obvious candidates", ours); "Teams is a realistic notification target" (labelled as an estimate).

**A shared resource with no reservation tracking.** One hit, the central one for P2. People across jobs and offices: the grid holds a percentage per person per week and no reservation with a state, which is how one superintendent was "penciled" by one PM and "promised" by preconstruction for the same week. Leaning 3: allocation rows (person, job, week range, percent, state) under the person, the weekly load rolled up so a double booking shows before the start week, the occupied-work qualification on the person. Nothing else on the call is booked or reused across jobs; owner inspection windows are the owner's, not theirs.

**An artefact that can go stale with nothing to flag it.** Four hits, one field corrected.
- The health colour and the summary page. "by the time it's in front of Curt it's a snapshot of a thing that already moved" (cue 102). `vocabulary["health"].likely_monday_object` read "status column on the project, rolled up to the portfolio"; a builder reading that alone builds today's summary page cell with no date and no author, which is the flaw. **Corrected** to a status set by the PM with the last-changed date and who changed it visible beside it and every change logged (the client's own requirement, cue 373), with the colour named as the PM's claim. Leaning 6.
- Burn: the PM's forecast and the Sage actual age differently. Leaning 5 gives each figure an as-of date and a source, and says every v0.1 figure is a sample keyed by us.
- Cumberland's report, rekeyed by hand into their template (cue 131). Leaning 7: a per-program view with its generated-on date plus a basic export shaped by the template once it arrives.
- The startup checklist's private variants ("Mine's got things on it the master doesn't", cue 71): the master goes stale as PMs add lines privately. Leaning 8: three templates with steps as child rows and a PM's extra line proposed to the template's owner.
- ICRA permits expiring unseen are covered by leaning 2.

**An expected output the input cannot support.** No hit in the pattern's sense. Checked by recount: 417 cues; 6,402 spoken words against "about 6,400"; talk shares 47.8, 12.3, 7.8 and 0.6 percent against the key's 48, 12, 8 and under 1; the longest unbroken Consultant stretch is 110 words from 00:54:10.284 to 00:55:04.305, 54 seconds, as stated; the bleed arithmetic ($276,640 + $37,440 + $18,000 + $100,000 = $432,080) on client inputs confirmed by the client; Wednesday the 23rd is a Wednesday in September 2026; every location in the key resolved by the verifier. One field in this family was corrected for a different reason, under section 4 below.

## 2. The "never written to" rule

s8 is not among the eleven keys FEEDBACK names. A search of the key for "written to", "write back", "writeback", "written back", "never touch", "read-only", "one way", "stays the source" and "not written" found nothing, so no existing claim needed rewording. The client lines that do exist are about the boundary, not about writes: "Procore is the job." (cue 361, about not moving the job out of Procore), "Sage is the book of record for anything with a dollar sign in this company." and "Nothing touches Sage without Roland" (cue 321). The new `existing.incumbents` entries for Procore and Sage use the rule's wording from the start: writeback and integration direction unresolved; v0.1 does not depend on either; staying clear is our safe default, labelled as ours. Leaning 5 says the same for Sage. `expected_structures.notes` still says "burn sourced from Sage rather than re-entered"; that is a statement of where actuals originate, backed by the client, not a feed claim, and the key's trap on Sage says the feed is unknown, so it was left.

## 3. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites in four places and is written into each: the health colour is the PM's claim (leaning 6 and the corrected vocabulary entry); an ICRA row's status is the PM's or project engineer's claim and the nurse's signed permit is the evidence (leaning 2); a confirmed allocation row is a claim until the person is on the job (leaning 3); every hours, cost, forecast and actuals figure in v0.1 is a sample keyed by us and no figure is Sage's (leaning 5, assumption 3, verdict condition 5).
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked against the nine `commitments_and_next_steps` entries: each carries its owner, purpose and date or "not dated", and none is recorded as done, so no field moved. The block carries the state in verdict condition 8: the invite for the 23rd, the template and August's summary page, the two grid tabs, the forecast sheet, the email starting the security review and the security documentation are all committed and none has arrived or been sent. The word "booked" in `expected_verdict.gates_met` and in `purpose_of_this_fixture` describes a time all three client attendees agreed on the call (cues 398 to 400), which is what happened; the invite itself is a commitment, and that is how the block states it. `expected_verdict` is v2 material and untouched in any case. No `status` field was added to the commitments array, because that would change the shared s1 to s10 shape.
- **s11 (inference targets questions; it never fills evidence).** Eight unconfirmed client ties are in `signals`, one of them from a cue the transcript does not label, and they drive four of the five questions as read-backs. None appears as evidence or as an element. The two things the Consultant said would change the proposal and never said how (build rights for Kyle and Bridget, cue 348) are signals routed to handover.
- **s15 (a product limit never deletes a client need).** Seven `unmet_needs` keep what this build does not meet: warranty calls (the client's own parking), Sage actuals without a second entry, single sign-on and the security questionnaire (the client's account, not the user's), a superintendent's update from a phone with no signal (no offline capture), Cumberland's format for January fifteenth, the written scope and number before the November lock (the user's own commitment, not the plugin's), and permission boundaries proven on their own people.

## 4. A21 and the existing account

The task sets the build target to own-account, a prospect. The key was written before A21, when the build was expected to go into the client's existing Enterprise account, and two fields said so in a way a builder would act on:

- `expected_structures.lookalike_traps[8]` read "A second workspace or a new account that ignores the existing Enterprise account, its 220 seats, preconstruction's bid board and safety's incident board." As written it would fail a proof of concept built where A21 puts it and would push a builder into a live client account without the A11-2 decision. **Corrected** to say the trap governs the later build in the client's account, which audits and extends what is there, and that the proof of concept is built in the user's own account in a new workspace for this client.
- `traps[5]` ("The account already has monday, so this is not a greenfield build...") gained one sentence saying the same: under A21 the proof of concept is built in the user's own account; the trap governs any later build inside the client's account.

Left as they are: `expected_questions_before_building[0]` ("Where should this live in the existing account?") is a question and the right shape; `existing.account` in the block says it moves to handover. `account_context.existing_monday_setup` describes the client's account truthfully and stands. Under A21 the "which account" question is not one of the five for a prospect.

One consequence the block states rather than hides: the A6 portfolio default fires on the client's tier, and the proof of concept is built in the user's own account, so the user's own account must offer monday's portfolio and project tools. Verdict condition 4 makes preflight confirm it and says the portfolio is not faked with plain boards if it does not.

## 5. The readiness block, field by field

- `pains`: the key's 24 entries in array order, same quotes and locations, numbered by theme as the exemplar rule asks: P1.1 to P1.9, P2.1 to P2.6, P3.1 to P3.4, P4.1 to P4.3, P5.1 and P5.2. Every key entry already carried its theme number, so none needed a new number. P1 and P2 are `excavated` (the key grades all six checks met for both) and P3 to P5 `stated`. `speaker_role` is the title (PMO Director, Senior Project Manager, Resource Manager); P2.6 carries "speaker unclear (tagged Speaker 2; the resource manager by context)". `outcome` is verbatim from cues 301, 302, 304, 306, 311, 312 and 195 where the client's words aim at the pain; six are null (P2.5, P4.1 to P4.3, P5.1, P5.2), because the only words aimed at them are the Consultant's playback, which the client agreed to but did not say.
- `signals`: eight, each naming what our side never confirmed: equipment jobs counted "mostly"; Waverly as a second program; Cumberland's spreadsheet template; Warren's forecast filling the summary page; the superintendent's two things a week; where the PMO's work sits and who builds, both routed to handover under A21; and the Speaker 2 line about preconstruction's promises.
- `entities`: 36, answering "what moves independently of what?"; 30 carry a parent and every one carries `moves_independently`. `shared_resource` is true for people and for allocations. `goes_stale` is true for the health colour, the weekly status, the deck, Cumberland's report, the PM forecast, burn, the startup checklist, the ICRA permit, the allocation and the grid. All `spoken`; nothing in this key is observed, documented or assumed at the entity level, since no document has arrived yet.
- `structure`: Work Management only; `own-account` with the brief's reason and the A21 point about the client's own account; one workspace, "Bellamy Ridge – Ops"; `native_reuse` "none" with the A6 note that the portfolio and projects are native objects and the A5 boards apply only if CRM or Service ever comes in; ten leanings; five parent-row-with-roll-up patterns; 24 `element_per_pain` rows (20 fixes, 3 none, 1 copies-today's-tool).
- `existing`: the client's account as the key and the record hold it, with the A21 statement that none of it is touched by the proof of concept; twelve incumbents with what each stays the record for and what it follows.
- `assumptions`: eighteen, each with the question that would replace it, including the two the client cannot answer (the bound account's tier; what the first cut may not show).
- `unmet_needs`: seven, under the s15 line above.
- `ai_opportunities`: six, all round 2 because the client never asked for AI or workflows: three workflows on P-21 (allocation overlap, ICRA expiry, milestone date change), two AI columns unprobed (what changed since last month; a forecast that moved), one agent on P-19 (drafts the summary page text, never sends).
- `verdict`: `build`. P1 and P2 have named entities and outcomes in the client's words, P3 has both as well, the product is chosen, the structure is stated with its leanings and the target is named. Eight conditions, the approval stop first, then the A11 point (none bites for an own-account target; A11-2 before any later build in the client's account), the workspace, the preflight check for portfolio tools, sample figures only, real project names and no patient-like data, the program shape shown as a question, and the committed-not-done list.
- `questions`: five, the ceiling. Q1, Q2, Q3 and Q5 are read-backs because signals exist; Q4 is discovery. Reused from the key's pool in build terms: items 2 and 14 in Q1, item 4 in Q2, item 10 in Q3, items 6 and 7 in Q4, item 11 in Q5. Dropped from the five and kept as assumptions with their questions: items 1 and 13 (the client's account and the security review; handover and a commitment under way), 3 (equipment jobs; assumption 1), 5 (the Procore boundary; assumption 18), 8 (the health rule; assumption 9), 9 (permissions; assumption 13), 12 (the six pilot projects; assumption 15), 15 (no patient information; a design constraint, assumption 16), 16 (warranty and the bid board; out of scope by the client's words).

The key's `should_plugin_propose_a_build: true` and its verdict agree with `build`, so the note gains no extra sentence. `rubric`, `expected_verdict` and `numbers` are untouched. No R-number, grade, gate name or verdict word is in the block; the script searched for them before writing, and two ordinary words it also caught ("gates" as a verb, "proposal" meaning our suggestion) were reworded rather than excused.

## 6. Flagged, not changed

- The s6 and s8 calendar overlap (both book Wednesday the 23rd at 2:00 pm Eastern) is recorded in COVERAGE and not touched; it is outside this fixture's own correctness.
- The client asked for real project names in the first cut (cue 411). In the user's own account that means the client's job names appear in sample data; they are not patient data and the block says so. If the planner wants a rule for client names in the user's own account, that is one decision for the set.

## 7. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (4 read-back, 1 discovery) |
| pains | 24 (15 excavated, 9 stated; 6 with no outcome in the client's words) |
| signals | 8 |
| entities | 36 (30 with a parent, all with `moves_independently`) |
| leanings | 10 |
| element_per_pain | 24 (20 fixes, 3 none, 1 copies-today's-tool) |
| patterns | 5 |
| incumbents | 12 |
| assumptions | 18 |
| unmet needs | 7 |
| AI opportunities | 6 (all round 2) |
| existing fields corrected | 5 (`vocabulary` ICRA and health, `expected_structures.notes`, `expected_structures.lookalike_traps[8]`, `traps[5]`) |
| transcript edits | 0 (417 cues unchanged) |
| key size | 2,742 lines from 1,602; 187,218 bytes from 121,629; 26 top-level fields |

Quotes the block introduces: 70 quote-and-location pairs were proven verbatim at their cues inside the build script before the file was written; the shared verifier then counted 283 pairs across the whole key, up from 222.

## 8. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo`, run after the last edit, exit code 0:

```
Fixture: s8-discovery-enterprise-pmo
Sources: transcript.txt (transcript/vtt, 417 units)

pairs found      283
verified         283  (of which presence only, no location cited: 25)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were reported; the transcript's units were not renumbered.
