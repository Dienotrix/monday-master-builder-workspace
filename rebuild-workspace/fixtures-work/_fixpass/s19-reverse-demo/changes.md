# s19-reverse-demo — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s19-reverse-demo/answer-key.json`, `transcript.txt` and `README.md`. Backups of the three originals were kept outside the fixture for the diff. Method: the key was loaded, changed and dumped by a script with a dumper written for this file's own layout (top-level objects multi-line, every list entry on one line, deeper objects on one line unless they hold a list); a round trip of the untouched file reproduced it byte for byte before any change, so every difference in the diff is a logged change. The 25 fields keep their order, `intake` stays the 26th and `readiness` is the 27th and last. The key is UTF-8 now because of the en dash in the workspace name, which the brief allows. Every quote the block introduces was proven verbatim at its cited unit by the script before the file was written (the transcript edits ran first, so the proofs are against the edited file), and the shared verifier was run after the transcript edit and after the key edit.

The task's order is kept below: the review entry, the direction rename, the sweep, the never-written rule, the standing lines, the readiness block, the README, the coverage row.

## 1. The review entry (FEEDBACK.md, s19, 2026-10-12), applied as recorded

**Change 1, the alias map.** `intake.roster.alias_map`: the entry 'Tobias, Marco, Sal (crew leads)' became three entries, one per crew lead, each with its own forms ('Tobias', "Tobias's crew"; 'Marco', "Marco's crew"; 'Sal'). The collective 'the guys' (00:24:09) is not an alias of any one lead; it moved to `unresolved_mentions` as a note that collective forms are not alias forms. 'Ashgrove and Marlow (cities)' became two entries, each carrying its own validity from the review's quote ("Ashgrove's ninety days, Marlow's a hundred and eighty", 00:32:51 Noor Abdelrazek). The sweep (section 3, pattern 3) found a third composite the review did not list: 'Their guy' sat among the forms of Copperline Foods, and the customer's representative is a person, not the organisation, so he has his own entry with the hedged forty-four noted as his. 12 entries became 16.

**Change 2, the permit model.** The one permit per job became any number of permits per job, each with city, approval date, validity and expiry, with a flag on an install scheduled outside a permit's validity and a job-level permit status named as not enough. Fields corrected, because a builder reading any of them alone would have built one permit per job:
- `expected_monday_products[0].why`: "carrying the permit on the job (city, approval date, days it lasts ...)" is now "carrying its permits on the job, any number of them (a Copperline store usually carries two), each with its city, approval date, validity and an expiry that lands in a real date column, ... and an install scheduled outside a permit's validity is flagged (a job-level permit status is not enough)".
- `vocabulary[permit ...].likely_monday_object`: "columns on the job: city, status, approval date, days valid, an expiry formula" is now permit rows under the job, any number, with the expiry written to a real date column "because a formula output cannot trigger a native automation (the user's finding, a probe for the next test account)", the separate board named as displaced twice, and a pointer to readiness leaning 1.
- `expected_structures.notes`: the same correction in the structure sentence.
- `requested_changes[0].description`: says any number of permits per job with the flag, and says whose sentence each part is (see pattern 4).
- `entities_and_workflows[2]` (Permit): adds that a store usually carries two permits, so a job holds any number.
- `expected_questions_before_building[3]`: gains how many permits one job can carry and the question to the coordinator about the dropped Permits board, asked before the structure under 'permits on the job' is chosen.
- `expected_structures.lookalike_traps`: one added, the job-level permit cell or single expiry, and an expiry as a formula column with an alert expected from it.
- `traps`: one added, the expiry in a real date column with the reason and the probe, and the many-permits job. 25 became 26.
- `intake.corrections_block_for_next_meeting`: a fourth line, asking the coordinator why the Permits board was dropped (00:29:45 gives the operator's objection; whether anything else) and how many permits a job can carry. 3 became 4.
The user's point that a calculated expiry must land in a real date column because formula outputs cannot trigger native automations is written where the expiry is designed (vocabulary, notes, traps, leaning 1, assumption 11, verdict condition 5), each time as the user's finding recorded as a probe for the next test account, never as a settled gotcha.

**Change 3, double-booking prevention.** A visible conflict flag for one crew on two installs in one morning or two crews on one became a first-version requirement, tested against a planted overlap, with warn-or-prevent confirmed during implementation and the workload view named as not enough on its own ("workload view ... showed everyone green", the review's words from the inventory). Fields: `expected_monday_products[0].why` and `expected_structures.notes` carry the requirement; `requested_changes` gains an `add` entry quoting the coordinator's own naming of the gap ("The part I couldn't do is the part that matters, which is stopping the double-booking and knowing about the permits.", presence-checked); `vocabulary[Install Week / the wall].likely_monday_object` gains the flag; `expected_structures.lookalike_traps` gains the workload view alone; `expected_questions_before_building[4]` gains what counts as a morning and warn or prevent; `pains[11].theme` is now "P7 Double-booking not prevented (stated by the builder as her prototype's gap; a required visible conflict flag in the build; not graded in the v2 rubric)", quote and location unchanged. Requested changes 6 (3 add, 2 change, 1 remove) became 7 (4, 2, 1).

Confirmed and left as the review confirms them: the screen-sharing boundaries, the prototype kept apart from the current state, the Consultant's premature fix at 00:16:12 flagged, and the read-back applying the operator's hold correction.

## 2. The direction rename

`intake.type_header.direction_of_show` is `direction`, and the same inside each of the three `segments[]` entries. The prose in `purpose_of_this_fixture` ("proposes the type header with direction they-show-current"), `accepted_behaviours[0]` and `intake.type_header.signals[0].result` ("decides direction:") follows. The README's plant table names the field and now reads "`direction` `they-show-current` (the field was `direction_of_show` before the fix pass)". `direction_of_show` no longer appears anywhere in the key.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry; where it sat in an existing field that was wrong, the field was corrected (listed in section 1 or here); where the field was only incomplete, the leaning carries it.

1. **One row where the call describes many.** Three hits.
   - Permits: one permit colour per job on the Sheet, one permit on the job in the key, two permits per store on the call (00:32:15). Leaning 1, permit rows under the job; the fields in section 1 corrected.
   - Installs: a job with two installs is two rows on the prototype (00:28:00) and a store is two visits (00:31:53). The key already says "installs as subitems or connected items so a job can have two", so no field was wrong; leaning 2 states the parent-row shape and what rolls up (next install date and crew), and keeps open whether the installs stay items on the connected install-week board the client wants kept.
   - Copperline: one job number or forty-one is accounting's question (00:17:40, "It matters for everything.", 00:17:53). Already a question and a trap in the key; leaning 3 records the leaning (one job per store under the customer) and the condition (accounting's answer, committed by the operations director at 00:46:04).
2. **A pain with no element that fixes it.** Three hits.
   - P7.1, the double booking: the review's change 3; leaning 4 and an element.
   - P5.1, installed history deleted from the Sheet: nothing in the key said rows are kept. Leaning 8: installed jobs stay in an Installed or Done group with their date; the status is the operator's claim and accounting's invoice is the record. `expected_structures.notes` was not changed: it names the jobs board and does not say to delete anything, so the leaning carries the addition.
   - P1.3, finished signs on the rack: no element clears a permit or makes the customer call. Leaning 9 says so and `element_per_pain` keeps it visible as `none`; the customer call is in `unmet_needs`.
3. **An alias-map entry that names more than one entity.** Three hits: the crew leads, the cities (both from the review) and the representative under Copperline Foods (found here). Field corrected (section 1) and leaning 10 states what each is in the build. Considered and left: 'the stores' under Copperline Foods, which names the sites of that customer's programme rather than another organisation; the readiness entities separate the customer, the programme and the store.
4. **Our framing labelled as the client's.** One soft hit. `requested_changes[0]` said the permit requirement was "stated by the client", when the sentence "a permit has a city, a date it was approved, and a number of days it lasts" is the Consultant's restatement at 00:33:38 and the client's own words are the expiry, the two cities' days and the date on the binder tab, confirmed with "Yes. That." (00:33:52) and "Write that down too." (00:34:03). The description now says whose sentence each part is, including that 'any number per job' and the flag are this pass's reading. Leaning 11 records it. Checked and left: the phone view (Reuben, 00:37:03), the Monday view (Ingrid, 00:37:29), the four blockers (counted back from the client's words), the seven labels and four groups (the operator's), the 'four Mondays' measure (the operator's, accepted by the delegate); the pinged-crew-lead automation is already labelled the Consultant's in `claims_store` and `traps`.
5. **A shared resource with no reservation tracking.** One hit, the crews, which is the review's change 3: three crews booked across installs and a survey with nothing that shows a crew twice. Leaning 4. Considered and left: the trucks, which travel with their crew and are costed with it ("the three of them and the truck"), so they are not booked separately; `entities` carries the truck as `assumed` with no evidence location.
6. **An artefact that can go stale with nothing to flag it.** Three hits, as leanings only, because the vocabulary entries they touch are incomplete rather than wrong.
   - The Friday print with handwriting on it (00:08:44) once the phone view exists: leaning 5, with crew adoption of the app as the condition.
   - The traveller with a superseded revision stapled on (00:19:21, 00:20:34): leaning 6, the printed revision recorded on the job and a reprint-required flag when a later revision is approved.
   - The Sheet and the board during the four Mondays, which is today's drift again unless one is keyed first (00:13:55, 00:41:22): leaning 7.
   Also carried in `entities` without a leaning of their own, because the structure already replaces them: the prototype's typed permit status copied from the binder, and the Sheet's colours and copied job numbers.
7. **An expected output the input cannot support.** No hit. Recounted from the transcript before any edit: 338 lines, 4 system lines, 334 turns, 6,177 words by whitespace split (the key's `words`), 141 words at 00:43:24 and 133 at 00:41:46, eight [laughs], one [inaudible], 36 ' -- ' (31 inside a turn, 5 at the end), the nine adjacent same-label pairs and the eight units without terminal punctuation at the stamps the key names, client share 66 percent with the three shares by segment; the weekday-date pairs fit a call in the week of Monday 12 October 2026 (Tuesday 20 October, Monday 19 October, Monday 11 January 2027, Thursday 26 November are all right); $190 x 4 x 2 x 12 is $18,240. After the transcript edits the counts that moved were updated (section 5 below).

## 4. The "never written to" rule

s19 is one of the eleven keys FEEDBACK names. A search for "never written", "written to", "write back", "writes back", "never touch", "read-only" and "one way" found two occurrences, both ours and neither traced to a client quote (no line on this call says anything about writing to the accounting system; the client's condition is that the job numbers keep matching, 00:38:08):
- `integrations_mentioned[0]`: "nothing writes back" is now "Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours (no line on this call says anything about writing to it; the client's condition is that the job numbers keep matching)".
- `traps[10]`: "do not propose writing to the accounting system" is now "Writeback and integration direction are unresolved and v0.1 depends on neither; staying clear of the accounting system is our safe default, labelled as ours and not as a client rule".
Checked and left: "not connected" about text messages (not a client system of record), "whether anything reads the mailbox is not asked" (a question), "Neither was requested as an integration" (a fact about the call). The readiness block's incumbent line for the accounting system uses the rule's wording, and questions 1 says the same.

## 5. Standing lines, where they bite

- **s11 (inference targets questions; it never fills evidence).** Seven unconfirmed client ties are in `signals`, each naming what our side never confirmed, and three of the five questions are read-backs of them (the Active Jobs list and the job numbers; two permits per store; the two-row job and the survey as a word). No signal appears as evidence or in an element. Two entities are `assumed` (the truck) or `unknown` (the chart and the widget) rather than given a reading.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked across the ten `commitments_and_next_steps` entries: each carries owner, purpose and a date or "not set", and none is recorded as done; the invite is "I'll send the invite to the three of you today" and the read-back "by end of day tomorrow", both still commitments. No field was changed. The verdict's seventh condition says the working session and the written read-back are committed by the Consultant, not sent, and that the owner has seen nothing. No `status` sub-field was added, for the reason the exemplars give.
- **s22 (a board status set by a person is a claim, never evidence that the source system changed).** Bites three times and is written into the block each time: a permit's approved status on a board is the coordinator's claim about the city and the city's approval is the evidence (incumbent line for the binder, element P3.2, leaning 1's question); the approved revision on the job is a claim until the customer's reply is attached (incumbent line for email, leaning 6, element P2.1, assumption 6); the Installed status is the operator's claim and accounting's invoice is the record (leaning 8). The hold itself is set on the board under this design, so there it is the event.
- **s15 (a product limit never deletes a client need).** Six needs stay in `unmet_needs` with their clocks: crews for the stores near Fort Wayne, the owner's own picture of good, the rework figure and the two rates, the customer call behind a sign on the rack, preventing (not only flagging) a double booking, and a crew lead seeing a change on his phone at six-forty. The formula limit on the expiry does not delete the alert the client needs; it moves the expiry into a real date column and records the probe.

## 6. Transcript mess pass (brief section 5, s11 rule)

Four Consultant turns were roughened inside their units, around the quoted spans and never inside one: 00:23:01 (a restart, "I'm going to -- I'm going to ask you to stop there", before the phrase the segment event quotes); 00:30:22 (a repeated "right at the start" between the opening and the quoted "Why now?"); 00:41:46 (a false start, "either Active Jobs or -- either Active Jobs or its successor", and a "so," in the playback, after the quoted opening sentences); 00:45:03 ("Okay. Um, so, next thing." before the quoted "What I'd like next"). The read-back at 00:43:24 is left as it is: it is read from notes, and its 141 words anchor the composite splitter's reasoning in `intake.detectors`. The number of units (334 turns plus 4 system lines), their numbering and their stamps did not change; the script asserted the stamps line by line.

Counts updated in the key (`transcript_format`, `intake.export_family.words`, `intake.delivery_notes[0]`) and the README: words 6,177 to 6,196 (about 6,200); ' -- ' 36 (31 inside a turn, 5 at the end) to 38 (33, 5); the playback 133 to 139 words, still the second longest turn behind the read-back's 141; Ingrid's share 18 to 17 percent, the whole-call client share still about 66 percent and the three segment shares still about 74, 65 and 58 percent by the same whitespace count. `verify_quotes.py` was run after the transcript edit and again after the key edit: zero misses, zero near-misses, no location notes.

## 7. The readiness block

Built in the brief's exact shape from the key's own content. Build target `own-account`, reason "prospect, so the user's own account by default (A21); the client's own Pro account holds the coordinator's prototype, which this key treats as a prior build to inherit in shape, not as a target". Product Work Management only; one workspace, "Bramblewood – Ops" (en dash); native reuse none, with the enabled-but-unopened CRM product named as the reason it is not a CRM entity. `existing.account` says what the client's account holds and that nothing in it is read, changed or written; the owner's wish to see it on the operator's own jobs is met with the client's job names and customers in the sample rows, which the key already allows, and no quote amounts.

- `pains`: the key's twelve entries in array order, same quotes and locations, numbered P1.1 to P7.1 (theme number first, running number after the dot, as the exemplar rule says); the unnumbered prototype gap is P7.1 as the next free number. P1, P2 and P4 entries are `excavated` per the key's R2 note, the rest `stated`. Outcomes are verbatim from 00:37:03 (the crew sees the change on a phone), 00:37:17 (the permit is in the thing and the thing tells Reuben), 00:37:29 (one thing on Monday) and 00:29:11 (right on Monday morning); P1.3, P2.1, P2.2 and P5.1 carry null because no outcome words aim at them.
- `signals`: seven (two permits per store; the two-row job; the Active Jobs list; which two leads hold seats; the leads added as users without knowing; the survey as a word; "slower than the Sheet").
- `entities`: 27, answering what moves independently of what: job, job number, install, permit, city, proof revision, approval email, hold, crew (the shared resource), crew lead, truck, install-week slot, survey, customer, the Copperline programme, store, and the artefacts that go stale (the two Sheet tabs, the print, the traveller, Active Jobs, the prototype and its typed status, the unnamed chart and widget). 17 carry a parent, all with `moves_independently`.
- `structure`: eleven leanings (sections 3 and 1), three parent-row-with-roll-up patterns (permits under the job, installs under the job, store under the customer), twelve `element_per_pain` rows (eleven `fixes`, one `none` for P1.3; no `copies-today's-tool`, because no element here waits on an integration: the job number stays keyed by hand as today and the key says so).
- `existing`: the account as above and eight incumbents with what each stays the record for.
- `assumptions`: thirteen, each with the question that would replace it; two are answered by preflight or the probe rather than by the client.
- `unmet_needs`: six (section 5, s15).
- `ai_opportunities`: four, all round 2 because the client never asked for AI or workflows (the coordinator asked only whether the workload view could be made to work). The two workflows cite P-21, the agent P-19, the AI column is `unprobed`, which is what the probe findings cover.
- `verdict`: `build`, eight conditions starting with the approval stop and the A11 point (none bites for an own-account target; the three decisions stay open), then the workspace, accounting's answer, the date-column probe, the planted overlap, the committed-not-sent session and read-back, and the April change kept out. `should_plugin_propose_a_build` is true and the key's v2 verdict agrees, so the `note` carries no second sentence.
- `questions`: five, the ceiling: three read-backs and two discovery questions, each routed and each saying what is known. Reused from the key's pool of nine: item 1 (Q1), items 4 and 3 in part (Q2, Q4), item 9 (Q5); Q3 is the correction-list re-ask. Dropped from the five, by the rule that a question stays only when a build element changes with its answer and that assumptions carry the rest: the crews' seats and phone fields (assumption 5 and preflight), column permissions (assumption 8), the three unconfirmed objects (assumption 10), the live account read (preflight), the proof convention (assumption 6, folded into Q5). Under A21 "which monday account" is not one of the five for a prospect.

No R-number, grade, gate name or verdict word is in the block; the script searched for them before writing. `rubric`, `expected_verdict` and `numbers` are untouched.

## 8. README

Brought in line: the transcript word and share counts; the key's line count and the `readiness` block in the file table; `direction` in the plant table; traps 26 (look-alike 9); requested changes 4 add, 2 change, 1 remove; the `pains` note naming P7 and the P1.1 to P7.1 numbering; quote strings 233 with the breakdown (206 with a location, of them 44 in the readiness block; 27 quote-only); 16 alias-map entries and 4 correction-list lines; the stale "400-line budget" line; and the review-history paragraph with the sentence "Fix pass applied 2026-10-13: ..." listing every change in one sentence.

## 9. Coverage row

`coverage-row.md` holds the row with the counts true of the edited files: traps 26 (9), requested changes 7 (4 / 2 / 1), quote strings 233, Review "reviewed 2026-10-13; fix pass applied 2026-10-13". Rubric rows, graded pains, objections and leak entries did not move.

## 10. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 12 (P1.1 to P7.1) |
| signals | 7 |
| entities | 27 (17 with a parent, all with `moves_independently`) |
| leanings | 11 |
| element_per_pain | 12 (11 fixes, 1 none) |
| incumbents | 8 |
| assumptions | 13 |
| unmet needs | 6 |
| AI opportunities | 4 |
| existing fields corrected or extended | 17 (listed in sections 1 to 4) |
| transcript edits | 4 turns, inside their units, +19 words |
| key size | 569 lines, from 398 |

## 11. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s19-reverse-demo`, final run after all edits:

```
Fixture: s19-reverse-demo
Sources: transcript.txt (transcript/line-bracket, 334 units)

pairs found      233
verified         233  (of which presence only, no location cited: 27)
skipped          1  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

Exit code 0.
