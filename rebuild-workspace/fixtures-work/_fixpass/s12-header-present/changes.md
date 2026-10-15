# s12-header-present — fix pass changes

Editor's log, 2026-10-13. Everything in the fixture is fictional and stays fictional.

Files touched: `fixtures/s12-header-present/answer-key.json`, `transcript.txt` (six of our side's turns, inside their units) and `README.md`. `meeting-chat.txt` is not edited. The key was loaded, changed and dumped by script in its own style (two-space indentation, every list entry and every three-key dict on one line); a round trip of the untouched file reproduced it byte for byte before any change, and the same dumper still does after. Field order is kept: the 25 fields in the s1 to s10 order, then `intake`, then `readiness` as the 27th and last. `rubric`, `expected_verdict`, `numbers`, `should_plugin_propose_a_build` and `accepted_behaviours` are untouched (a JSON diff of the rubric is empty). Every quote the block introduces was proven verbatim at its cited unit by the build script before the file was written (47 proofs), and the shared verifier agrees (199 pairs, 0 misses).

Authority applied, in the order the task set: the s12 entry in `for-review/FEEDBACK.md` (lines 136 to 147), the direction rename, the seven-pattern sweep, the never-written rule from the s14 entry, the standing lines from s11, s21, s22 and s15, the readiness block in the brief's shape, the README, the coverage row.

## 1. The review entry's changes, as recorded

The user's verdict: keep the intake and the pains; one change to the build model. Not a fork, since no two client speakers disagreed, so the key gains no `forks` entry and the change lives as an open structural question with a leaning in `readiness.structure.leanings`, with the fields that stated the old structure corrected to point at it.

**Item 1, hold time at the wrong level.** The key tracked the batch by its earliest hold time and left the per-analysis clocks in the lab system, at the four places FEEDBACK cites and two more that said the same thing.
- `expected_monday_products[0].why` (key line 39): "every batch ... with its earliest hold time ... a sub line on the batch with an owned due date" became the shared board without a batch-level date, and a sentence naming the open structural question and its leaning: analyses as child rows under the batch, each with its own clock, the batch showing the next open clock; settled by what the nightly file carries and by the sub-desk owner.
- `vocabulary["hold time"].likely_monday_object` (line 98): "date column for the earliest hold time ... per-analysis clocks stay in the lab system" became the leaning in full, with the reason the batch-level date fails (it stops watching once the first clock is handled; the misses happen per analysis, "Four batches where an analysis didn't start in time", 14:15:58).
- `vocabulary["batch"].likely_monday_object` (line 97): "the item, not a subitem" stands, with the analyses as child rows named as the leaning, so a builder reading the batch entry alone does not build one row.
- `traps[22]` (line 194): "The board tracks the batch by its earliest hold time; per-analysis clocks stay in the lab system." became the open question with its leaning and the instruction not to decide it from the login sheet's one row per batch.
- `expected_structures.notes` (line 263): the receiving board's column list loses "earliest hold time" and "sub due date and owner"; a sentence records the leaning and what settles it.
- `expected_structures.lookalike_traps[2]` (line 258) listed "per-analysis clocks ... as boards" as a look-alike. With the leaning, clocks on child rows are the proposed shape, so the trap now names the login queue and results as the look-alikes and says the child rows carry a date and a status, never a result.
- `expected_questions_before_building[0]` (line 213) asked whether "the earliest hold time per batch" is derivable; it now asks whether the file lists analyses per batch, whether per-analysis hold times are in it or derivable from collection time and each method's holding period, and whether it carries the receiving lab.
- Leaning 1 in the block carries the question, the option, the four quotes it rests on (14:11:10, 14:15:58, 14:09:53, 14:36:35) and the settling condition (the header row the IT provider committed for the ninth, then the LIS lead).

**Item 2, subcontracts have the same one-to-many problem.** The sub fields were on the batch at lines 105, 133 and 263 and in two more places.
- `vocabulary["sub"].likely_monday_object` (line 105): "a sub due date somebody owns, on the same batch" became which lab, sent when, due when and who chases, as fields on the outsourced analysis row, second-hand until the sub-desk owner is heard.
- `integrations_mentioned[3]` (line 133): "the ask is an owned due date on the batch" became the client's ask in the client's terms (a due date that is theirs; knowing a sub is late before the client does), with "a line on the batch" labelled as our first cut and superseded by the leaning. This is also the one hit of sweep pattern four; see section 3.
- `expected_structures.lookalike_traps[4]` (line 260): "an owned due date on the batch" became the fields on the analysis row.
- `expected_structures.notes` and `expected_monday_products[0].why`: as above.
- **"Also"**: the sub-desk owner was not on the call ("she's not on today", 14:12:14), so `entities_and_workflows[7]` (Subcontract) is now marked second-hand and says only some of a batch's analyses go out, and `expected_questions_before_building[6]` is routed to her as questions whose answers become fields on the analysis row. Leaning 2 carries the same, with 14:12:14, 14:25:34 and 14:31:31 behind it and her return after the twentieth as the condition. Question 3 of the block is hers.

## 2. The direction rename

`intake.type_header.direction_of_show` became `direction`, in place, value `no-show` unchanged; the type header's field order is otherwise the same. The key has no `intake.files[]` headers (one meeting, not a package), and the README does not name the field, so nothing else moved. A search of the whole key for `direction_of_show` finds nothing.

## 3. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit becomes a `structure.leanings` entry; where a builder reading an existing field alone would build the flaw, that field was corrected too; where the field was only incomplete, the leaning carries it.

1. **One row where the call describes many.** Two hits, both the review's: the batch and its analyses (leaning 1) and the batch and its outsourced analyses (leaning 2); fields corrected as listed in section 1. Considered and declined: project and batches (the project is a group or a connected board in the vocabulary, and batches are already the rows); bottles under a batch (the clock is per analysis, not per bottle, so bottles do not move on their own; whether a child row is per analysis or per bottle and analysis is folded into leaning 1's condition); the authority's two districts (a client value, separate contracts, no row of ours).
2. **A pain with no element that fixes it.** Three full hits and two partial ones, all visible in `element_per_pain`. P4 proposals re-keyed (`none`; parked by the client; leaning 3). P5 the county portal double entry (`none`; the portal is theirs; the county-facing view is an addition, not a replacement; leaning 4). P7 the paper safety form (`none`; a relayed wish; leaning 5). P2 is reached in part: the board and the county view fix the time per enquiry and the county's calls, and the engineers' enquiries, which are most of the hundred and ninety ("Usually the engineer, because their client is asking them.", 14:22:12), stay calls until the parked portal question is settled after the audit (leaning 6, and an unmet need). P6's element exists (a phone view for the field) but its content was never specified on the call, only the device and the signal; leaning 9 says what it is assumed to show and what settles it. No existing field was wrong for these; the key already parks proposals and the portal and labels the safety form a relay.
3. **An alias-map entry that names more than one entity.** Two hits, both corrected in `intake.alias_map`. The water authority's entry carried "their compliance manager" (a person, possibly two: the letter at 14:16:20 and the south district at 14:29:45) and "the county one", which at 14:16:15 is a batch of county samples, not the authority; both forms removed, and the compliance manager has an entry of his or her own. The laboratory's entry carried "the main lab", "the satellites" and "the south lab", which are places and the location value a batch moves between; the three forms moved to a new entry for the three labs as places. 18 entries became 20. Leaning 8 carries the structural side (location as a value on the batch, never a board per lab, with how a satellite batch reaches the board as the condition). Checked and left: the parent group ("the group", "my group" are the organisation), the sub desk ("Solveig", one person), the field coordinator ("Field", his own nickname).
4. **Our framing labelled as the client's.** One hit: "the ask is an owned due date on the batch" in `integrations_mentioned[3]`, where "on the batch" is our first cut at 14:39:55 ("Subs as a line on the same batch with a date somebody owns") and the client said only "There's no due date anywhere that's ours." (14:25:34) and "I want to know a sub is late before the client does." (14:31:31). Corrected as in section 1. Checked and left: "field sampling coordinator" is the Consultant's phrasing at 14:08:46 of the client's own "I coordinate field sampling. Put that." (14:08:32), and the key already marks it self-described; the first cut as a whole was accepted by the approver ("It's the right first cut. Receiving first.", 14:40:39) and so is the client's acceptance of our shape, with the lab director's reservation recorded; the order of the four pains is the Consultant's play-back confirmed by the approver and qualified by the lab director, and the key records both; "priority must sort" in `traps[24]` derives from the rush desk's "The flag doesn't sort anything" and is addressed to the plugin, not attributed to the client.
5. **A shared resource with no reservation tracking.** No hit. The nearest candidates are the field crews and the vans ("four crews, three vans, and I schedule all of it", 14:08:07; a re-sample needs "a van and two people", 14:19:32) and the transfer van between the labs. They are reused across jobs, so `entities` carries them with `shared_resource: true`, and `assumptions` says scheduling stays with the field coordinator outside the build with the question that would change it. Declined as a leaning because the client asked for a day list on a phone and never for scheduling; inventing a crew board would be our framing. The sections' bench capacity is not booked and was not discussed.
6. **An artefact that can go stale with nothing to flag it.** One hit, the one that matters for this build. The receiving board is fed from a nightly file ("Nightly. Project, batch, analyses, status codes, dates", 14:36:35), so every fed row is a snapshot up to a day old, which matters on forty-eight-hour clocks, and anything a person sets on it (status, who has it, a sub date) is a claim about the lab system or a sub, never evidence. Leaning 7: an as-of time and source on every fed row, the alert reckoning with the file's age, every v0.1 value sample data and the demo saying so. No field corrected: the key already says the file is nightly and never promises live status. The artefacts the board replaces (the six-thirty printout, the whiteboard that "gets overwritten") carry `goes_stale: true` in `entities`; the report (a partial superseded by a revised one) and the morning text to the crews do too, the last as assumed.
7. **An expected output the input cannot support.** One small hit and the counts. `company.size`, `expected_monday_products[1].why` and `expected_structures.native_boards_required[0].why` said "two hundred and twelve proposals a year"; the chat says "212 proposals last year, 71 won" (chat 14:26:40), one year's count, not a rate. All three now say "last year", and the rate is an assumption with its question for the business development director. The counts the key measures were re-measured and are true (section 5 for the ones the mess pass moved). Checked and found supported: the weekday-date pairs against the header's Thursday 8 October 2026 (the twenty-first is a Wednesday, the twenty-second a Thursday, the twentieth a Tuesday); the bleed arithmetic; the 44-second longest gap after 14:39:55; the one adjacent same-label pair (14:14:52 and 14:15:14).

## 4. The "never written to" rule

s12 is not among the eleven keys the s14 entry lists, but a search for "written", "write back", "writeback", "never touch", "read-only" and "one way" found one claim: `integrations_mentioned[0]` said of the lab system "Read-only, one way, results never carried". "Results never carried" traces to the quality manager (14:32:02) and stays; "Read-only, one way" traces to no client line (the client said the bench will not type twice, 14:34:46, and that the LIS lead must be in the room for anything that connects, 14:33:30; neither is a no-write rule). Reworded to the fix-pass form: writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the lab system is our safe default, labelled as ours; anything that connects needs the LIS lead in the room, which is the approver's words. The block's `existing.incumbents` entry for the lab system uses the same wording. Checked and left: "the lab system stays the record for results" (the quality manager's boundary and our restatement, which he accepted, "Then we're fine.", 14:32:38); "the county's compliance portal: theirs, not ours ... stays" (the client's "which is their system, not ours", 14:14:09); "a read-only view" for the county in `lookalike_traps[5]`, which is about our board, not a client system.

## 5. Standing lines where they bite

- **s22 (a board status set by a person is a claim).** Bites throughout: leaning 7, leaning 2 (the sub due date is a person's claim until the result lands), `element_per_pain` P3, the verdict's last condition, and the incumbent line for the nightly file, which is the only evidence from the lab system that reaches the board.
- **s21 (a commitment is `committed`, done only on evidence).** Checked; the key's ten `commitments_and_next_steps` entries each carry owner, purpose and a date and none claims delivery; the chat line at 14:44:07 ("Invite ... coming this afternoon") is a promise, not a sent invite, and the key already says so under R10. The verdict condition states it: the walkthrough is committed, not held; the invite is ours to send, the controller is the approver's to fetch; each becomes done only on evidence. No status field was added, since that would change the shared shape.
- **s11 (inference targets questions, never fills evidence).** Seven unconfirmed client ties are in `signals`, and four of the five questions are read-backs of them; none is counted as evidence or built into an element. Two entities (the morning list's content) and one role (the invoice step) carry `assumed` or `unknown` rather than a location.
- **s15 (a product limit never deletes a client need).** Six `unmet_needs`, with their clocks where the client gave one: status the county can see by December under the January first clause (v0.1 is sample data in the user's own account and cannot be given to the authority), the portal double entry, proposals, the engineers' enquiries (after the audit), the safety form, and the crews on a phone with one bar (seats and tier unverified).

## 6. The readiness block, field by field

- `schema` readiness/1; `note` as the brief gives it, plus one sentence that the receiving model is an open structural question with a leaning and not a fork.
- `pains`: the key's nine entries in theme order with their own quotes and locations. P1 holds three entries (the headline at array index 0, the mechanism at 1, the root at 8), numbered P1.1, P1.2, P1.3; P2 to P7 keep their numbers. Stated or excavated follows the key's R2 note (P1 to P3 excavated, the rest stated). Outcomes are verbatim client words proven at their units: "Zero hold-time misses on anything that came through our door in time." (14:31:31) for P1.1 and P1.3, "One screen where I can see every batch that's due this week, across all three labs, without asking Ronan." (14:31:01) for P1.2, "And the county can see theirs without calling Fenella." for P2, "And I want to know a sub is late before the client does." for P3, the phone line (14:38:51) for P6; null for P4, P5 and P7, where no outcome words aim at them.
- `signals`: seven (the LIS lead's capability as a colleague's claim, the receiving lead as the bridge, the lab director's reservation on the alert, the approver's "if that's real" on the county view, the parked portal, the chat wish on proposals, the relayed safety form).
- `entities`: twenty-seven, answering what moves independently of what: the analysis moves independently of the batch (its own clock, its own start, possibly a sub), the batch of the project, the project of the client; the bottle, the clock and the rush flag do not; crews and vans are shared resources; the printout, the whiteboard, the nightly file, the report and the morning list go stale.
- `structure`: Work Management; `own-account`, "prospect, so the user's own account by default (A21)"; one workspace, "Ashenholt – Ops" (the en dash makes the formerly ASCII key UTF-8, which the brief allows); native reuse none in the first build, with the key's own CRM rule if proposals come in; nine leanings; one pattern (batch with analyses as child rows, the next open clock and the where-is-it on the parent, sub fields on the analysis row); nine `element_per_pain` rows (five `fixes`, one `copies-today's-tool`, three `none`). P1.2 is the honest `copies-today's-tool`: until the nightly file is live, a shared board the satellites type into is the login sheet with more editors, which is the two-systems objection.
- `existing`: the HR account described from the key's `account_context`, with A21 placing the build in the user's own account and the account question at handover; eleven incumbents with what each stays the record for.
- `assumptions`: seventeen, each with the question that would replace it; the controller's and the account questions from the key's pool live here.
- `unmet_needs`: six (section 5). `ai_opportunities`: four, all round 2 (the client asked for alerts in substance but never for AI or workflows); the two workflows cite P-21 as the thin exemplar does, the AI column and the agent are unprobed.
- `verdict`: `build`, with eight conditions starting at the approval stop and the A11 point (none bites; own-account target; the three decisions stay open), the receiving model held open until the header row and the LIS lead, the sub fields held until the sub-desk owner, the walkthrough as committed not held, the accreditation boundary, and the claim rule.
- `questions`: five. Q1 read-back to the LIS lead (the file's header row: analyses per batch, hold time, receiving lab); Q2 read-back to the lab director and the receiving lead (what the day-before alert is on a forty-eight-hour clock); Q3 discovery to the sub-desk owner after the twentieth; Q4 read-back to the approver on the county view; Q5 read-back to the field coordinator and the safety officer. From the key's twelve: items 1, 2 and 4 are in Q1, 5 in Q2, 7 in Q3, 6 in Q4, 8 in Q5; items 3 (the controller) and 12 (the invite) are verdict conditions and assumptions, since no build element changes with them; 9 and 11 are assumptions; 10 (which account) is out under A21 and stays in the key's own list for handover.

## 7. Transcript edits (brief section 5, the s11 mess rule)

Our side spoke in writer-clean paragraphs in most of its longer turns, so six unquoted Consultant turns received a light mess pass inside their units: a false start at 14:04:22 ("This is a, this is a conversation"), a restart at 14:35:02 ("it either reads, either it reads"), a filler and a navigation phrase at 14:36:26 ("the, um, the nightly one"), a repeated half-clause at 14:41:00 ("I won't ask you to, I won't ask you to"), a filler and a repeated half-explanation at 14:42:51 ("So, um, the next step ... your data stays where it is"), and a repetition at 14:44:11 ("just the header, no results"). None of these turns holds a quoted span (`--spans` was read first), no ' -- ' break or cue was added, and no turn crosses 102 words. Twelve diff lines, six turns. Unit count 214, numbering and timing lines unchanged; 0 collisions, 1 adjacent same-label pair, 0 lowercase-initial units, 20 short units, longest turn 102 words at 14:39:55, nine ' -- ' breaks and six [laughs] all unchanged. Word count 5,363 to 5,389 (cues excluded, the key's method), client share 66.6% to 66.2%; `transcript_format` and `intake.export_family.words` in the key, and the README, say so. The chat file is not edited.

## 8. README

Counts brought in line: 5,390 words and 66.2% in the files table; 550 lines and the `readiness` block in the key's row; 199 quote strings (167 located, 32 presence-only; 158 original and 41 from the block); 20 alias-map entries; the one-line convention bullet now explains the block's exceptions and the line count. Review status: "Not yet reviewed by the user" became the user's review of 2026-10-12 with its verdict, and a closing one-sentence line "Fix pass applied 2026-10-13: ..." lists what moved.

## 9. Left as it is, and flagged

- `traps[29]` and `account_context.existing_monday_setup` still tell the plugin to ask which account the build goes into. Under A21 the first version goes into the user's own account and that is a handover question; `existing.account` says so. Not rewritten, to keep the diff to what the review and the sweep asked; one decision for all keys if the planner wants the A21 default written into the traps.
- The key's own twelve `expected_questions_before_building` stand as a pool; the block's five are the readiness choice.
- `expected_verdict.note` still says "Propose the Work Management blueprint and a v0.1 of the receiving board"; v2 material, untouched, and it does not contradict the block.

## 10. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (4 read-back, 1 discovery) |
| pains | 9 (P1.1 to P1.3, P2 to P7) |
| signals | 7 |
| entities | 27 (18 with a parent, all with `moves_independently`) |
| leanings | 9 |
| element_per_pain | 9 (5 fixes, 1 copies-today's-tool, 3 none) |
| incumbents | 11 |
| assumptions | 17 |
| unmet needs | 6 |
| AI opportunities | 4 |
| verdict conditions | 8 |
| existing fields corrected | 20 string edits across 10 top-level fields, 2 alias entries added, 1 field renamed |
| transcript edits | 6 turns, +26 words |
| key size | 550 lines, 27 top-level fields (from 393 lines, 26 fields) |

## 11. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s12-header-present`, run after the last edit to the key and the transcript (and again after the README, unchanged), exit code 0:

```
Fixture: s12-header-present
Sources: meeting-chat.txt (chat/header-time-first, 11 units); transcript.txt (transcript/header-time-last, 214 units)

pairs found      199
verified         199  (of which presence only, no location cited: 32)
skipped          3  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes: this fixture's locations name a stamp and a label, not an index, and no unit was renumbered. The three skipped values are the key's own nulls (`true_source.quote` in `intake.second_hand`), as at baseline.
