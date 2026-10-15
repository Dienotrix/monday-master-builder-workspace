# s15-shred-dense — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s15-shred-dense/answer-key.json` and `fixtures/s15-shred-dense/README.md`. `transcript.txt` is unchanged (487 units; see section 7 for why no mess pass was applied). Work files: this log, `coverage-row.md`, and the two scripts that made the edit (`apply.py`, which applies every change and proves every new quote at its transcript unit before writing, and `keystyle.py`, the dumper).

Method. The key was loaded, changed and dumped by script. The file's own style is not `indent=2`: dicts are printed open at the top two levels and every list entry sits compact on one line (the README says why: a 400-line writing budget). A dumper that reproduces that style round-tripped the untouched file byte for byte before any change was made, so the diff outside the edited paths is empty. The key had 26 top-level fields (the 25 in the s1 to s10 order, then `intake`); `readiness` is the 27th and last. The file was ASCII before and is UTF-8 now, because the workspace name carries the brief's en dash (the brief allows this). The key grew from 392 to 546 lines; the 400-line budget was a writing-stage constraint for the intake block and gives way to the brief, and the README now says so.

Verifier runs: after the key edit, after the README edit, and once more after the last file write, all three identical (section 10). A path-level diff of the edited key against a backup of the original lists exactly the fields named below and nothing else.

## 1. The review entry's four changes (FEEDBACK.md, s15 entry of 2026-10-11)

**Item 1, customer-facing over-closed.** The recorded change: "customer visibility is out of the first version by the client's choice; it is what closes the audit finding, so a later customer-facing requirement stays open, with the February renewal as its clock; how it is met is open." Applied where the key closed the need:
- `expected_monday_products[0].why` (key line 30): "customer-facing extras are out of the first version and deferred beyond v1 in any case" replaced by the recorded wording. In the same field "Nothing customer-facing in the first version" gained "by the client's choice".
- `traps[21]` ("Status calls look like a ticket desk..."): "Service extras are deferred beyond v1 in any case" replaced by the client's choice, with the client's quote ("Customers don't see anything in the first version.", L457), the open need, the February clock and the line that a product limit never deletes it.
- `requested_changes[2].description`: now says the choice is the client's and that the need stays open with its clock.
- `expected_structures.lookalike_traps[1]`: the trap stands (no customer portal in the first version) and gains the sentence that the need itself stays open.
- `expected_structures.notes`: "nothing customer-facing" now reads "nothing customer-facing in the first version by the client's choice (the customer-visibility need stays open)".
- `commitments_and_next_steps[9].what`: the same qualification.
- Readiness: `unmet_needs[0]` carries the need with the finding's quote (L64), the February clock with the January showing (L433), and why it is not met; leaning 8 holds the open question of how it is met; question 4 reads the January line back to the client. The roadmap defers the portal, not every way of showing a customer a status; the record flags the need to the user rather than dropping it.

**Item 2, site and discipline.** `expected_structures.notes` (key line 239) no longer lists site and discipline among the export's fields; it lists the fields the client named (L165) and says site and discipline stay wanted, with their source open until the export is inspected, and may have to be typed or derived. `vocabulary[14]` (the hub) and `vocabulary[16]` (micro / chem) say the same on their dropdown columns. `expected_questions_before_building[1]` (the export question) now asks whether site and discipline are in it. Readiness: leaning 2 (pattern "an expected output the input cannot support"), assumption 2, and question 2.

**Item 3, the automations are candidates.** `expected_questions_before_building[9]` (key line 203) rewritten as candidates to confirm, with the two reasons from the review (day five is when customers ring, L206; chem takes five to ten days, so a flat day-five warning fires on chem jobs that are on time). `expected_structures.notes` says "candidates to confirm with the client, not expected v0.1 logic" and gives the same reasons; "a warning at day five" became "a warning keyed to a date". `accepted_behaviours[14]` presents them as candidates, none of them expected v0.1 logic. Readiness: leaning 3 (pattern "our framing labelled as the client's"), assumption 14, question 5, and a verdict condition that none is created.

**Item 4, the meeting date.** The recorded change: keep it relative, "Thursday the 17th, 14:00, month unstated". Applied at the three places the review names and one more:
- `commitments_and_next_steps[0].date` (key line 142): "2026-09-17 14:00 (... month and year inferred from the weekday ...)" is now "Thursday the 17th, 14:00, month unstated (the input carries no call date; timezone unstated)".
- `commitments_and_next_steps[7].date` and `[9].date` (key lines 149 and 151): "Before 2026-09-17" is now "Before Thursday the 17th (month unstated)".
- `rubric[9].note` (R10, key line 42): the sentence "The weekday and date fit Thursday 17 September 2026 with the call earlier that month" is now the relative form with the reason. This is the one edit inside `rubric`, which the brief otherwise keeps untouched as v2 material; the review names line 42 explicitly and the brief says the fixture's entry is applied exactly as recorded, and FEEDBACK is the authority behind the brief, so the more specific instruction won. Only that sentence changed; the rest of the note, its evidence and its status are as they were. Worth the planner's nod.
- `traps[17]`: "Thursday the seventeenth fits 17 September 2026 (1 September 2026 is a Tuesday)" is now the relative form with the reason that a weekday with a day of the month does not fix a month.
- README: the dates paragraph no longer names September 2026.

## 2. The `direction` rename

`intake.type_header.direction_of_show` is now `direction`, `direction_of_show_note` is now `direction_note` (the old name carried the field name inside it, and the verifier checks that `direction_of_show` is absent), and each of the three `intake.type_segments[]` entries carries `direction` in place of `direction_of_show`. Values unchanged. The README's review-history sentence named "the direction-of-show header wording" and now says "the direction header wording".

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry; an existing field was corrected only where a builder reading it alone would build the flaw.

1. **One row where the call describes many.** One hit: the job and its tests. "one sample, one job, but a job can have six tests" (L94), "the tests are scheduled off the job" (L99), results arrive "as they come" (L116), micro and chem run on different clocks, and some jobs have two reports (L129-130). One row per job with one status and one due carries one value for several things once a job mixes disciplines. Leaning 1 leans to one row per job in v0.1 (the client's unit and what the export lists) with tests as child rows only if the export is per test or Dara wants a due per test; the `patterns` entry records the parent-row-with-roll-up shape as held ready, not applied. No field corrected: `vocabulary[2]` already says "subitems or a dropdown, if tests are shown at all" and the export question already asks "one row per job or per test". Considered and declined: urgents and holds, which are one per job.
2. **A pain with no element that fixes it.** Three hits, all kept visible. P2.5 (form quality at intake, L90): nothing in the build reaches the paper form or the customer; leaning 9, `element_per_pain` `none`, `unmet_needs[2]`. P1.6 (the retention remark, L238, internal by the client's marking): no element is aimed at it; leaning 10, `none`, `unmet_needs[3]`, and it never leaves the record. The customer-visibility need (review item 1), which is not a pain entry of the key but the client's central need: leaning 8 and `unmet_needs[0]`. Two further rows are `copies-today's-tool` rather than `none` (section 6).
3. **An alias-map entry that names more than one entity.** No hit. The key's five `alias_map` entries each resolve one person's four label shapes to one name. Nearest candidates checked and left: "Dara's team" at L114 and L148, already recorded as a mention and not a label; "the retail account", "the retail people" and "their technical team", which are one customer and its staff, not alias-map entries.
4. **Our framing labelled as the client's.** One hit, the automations (section 1, item 3): the key presented the on-hold reminder, the day-five warning and the urgents notifications as the build's logic when every one is ours and none was agreed; fields corrected. One soft hit, carried in leaning 6 without a field correction: the name against each hold is the client's ask (L364, L458-459), the "rung step" is the Consultant's addition in the play-back (L454) that nobody objected to; `expected_structures.notes` now labels it. Checked and left as labelled already: the four-piece first version (the Consultant's play-back, agreed as "the right shape" at L455 and recorded as ours in R12); "the first version stays out of the lab" (the Consultant's proposal at L441, accepted by Dara at L442-443, recorded as accepted); P3 folded into P1 (the client's own "it's a symptom of the first one", L293, before the Consultant's proposal); "the floor" (the Consultant's word at L330, repeated by Tamsin at L331 and recorded as such).
5. **A shared resource with no reservation tracking.** No hit. Nothing on the call is booked across jobs: the lab system schedules tests, the analysts are scheduled by it and stay out of the first version, the signatories act in the lab system. Nearest candidate declined: the fridge shelf, which samples share but nobody books. `analyst` and `signatory` carry `shared_resource: true` in `entities` so the fact is recorded; no leaning, because inventing a booking element would be our framing.
6. **An artefact that can go stale with nothing to flag it.** Three hits, the central ones for this fixture.
   - The board as a copy of the nightly export: a status on it is last night's value while the calls are hourly ("It's just not live, right.", L166). Leaning 4: an as-of date on the board and beside the status on every row; in v0.1 the board is one night's sample and says so. Field: no correction; `vocabulary[5]` and `vocabulary[15]` are silent rather than wrong, and the loading question already exists.
   - The typed due after the result slips ("we told them Thursday and it was Friday", L212). Leaning 5: due carries who typed it and when, and a view of jobs past their typed due and not yet authorised; nothing derives or moves it (L461).
   - The on-hold sample itself, which expires ("by Friday a micro sample from Tuesday is out of date", L249). Leaning 6: date in and age on the on-hold list, oldest first, the micro shelf life visible once discipline has a source (leaning 2).
   - Recorded in `entities` with `goes_stale: true` and no leaning of their own: the whiteboard, Oisin's spreadsheet and Tamsin's workbook (the artefacts the views replace), the chain of custody form (a bakery copied last month's, L269), the urgent flag (two lists that mostly agree, L146-147).
7. **An expected output the input cannot support.** Three hits. Site and discipline from an export the client listed without them (section 1, item 2; leaning 2; fields corrected). The meeting date pinned from a weekday (section 1, item 4; fields corrected). The retail account's rows in an export whose customer names are scrubbed: the turnaround view is for one customer the client will not name, so without a stable code in the customer field the view cannot pick its rows out. Leaning 7 (ask Joost for a code or pseudonym per customer; otherwise the view runs over all jobs and says so); `expected_questions_before_building[1]` now asks it; assumption 7. Checked and left: the transcript statistics (re-measured at stage-1 acceptance; the transcript is unchanged) and the bleed arithmetic (the client's own sum).

## 4. The "never written to" rule

s15 is one of the eleven keys FEEDBACK names. No client line says the lab system is never written to. The sentence the key leaned on, "What goes into the lab system stays in the lab system, and anything else reads from it.", is the Consultant's (L415); Dara's "Then we're fine." (L416) accepts it, and her own constraint is no double entry ("My analysts will not type the same thing twice.", L413). Joost's vendor remark (L393-394) is about reads. This is the s14 shape exactly (our sentence, the client's assent), so each occurrence became the unresolved wording:
- `purpose_of_this_fixture`: "reads from the lab system's export and never writes to it" is now "reads from the lab system's export; writeback and integration direction are unresolved and the first version depends on neither".
- `expected_monday_products[0].why`: "nothing written to the lab system" is now the full rule sentence, labelled as ours.
- `integrations_mentioned[0]`: "the system of record, never written to (...)" now attributes the quoted sentence to the Consultant with Dara's acceptance and the client's own constraint, then the rule sentence.
- `traps[23]`: "The lab system is never written to" is now the rule with the reason; the export and vendor sentences that followed are unchanged.
- `expected_structures.lookalike_traps[2]`: "or writing anything back to it; the board mirrors the export and reads only" is now the rule.
- `expected_structures.notes`: "nothing written to the lab system" is now the rule.
- `requested_changes[3].description`: "whatever goes into the lab system stays there" is attributed to the Consultant and the rule added; the client's quote on the entry (no double entry) is what it supports.
Checked and left because each traces to the client or is a different claim: `vocabulary[8]` "the act stays in the lab system" (where authorisation happens, L121-123); `compliance_or_security_signals[3]` "nothing in the build may show a status as authorised that the lab system has not authorised" (the s22 line, kept); `objections[2].type` and `rubric[8].note` "reads from the export" (a read, which the client's export line supports). The readiness block's lab-system incumbent carries the same unresolved wording.

## 5. Standing lines where they bite

- **s22 (a board status set by a person is a claim).** Bites on the status column and on due. Leaning 4, assumption 8, the lab-system incumbent and a verdict condition say the board's status is the export's copy as of its night and never evidence of the lab system's current state; leaning 5 says due is a typed judgement ("As long as nobody thinks it's true because it's on a screen.", L372). The rung step is the record of a person's act (someone rang), which is what it claims to be, so it is not dressed up as the customer having been reached.
- **s21 (a commitment is committed, done only on evidence).** `commitments_and_next_steps[0].what` said the walkthrough was "with the MD invited". On the call nothing was sent: the Consultant will send the invite today (L471), Tamsin will put the MD on it and chase him this week (L466), and his attendance is her hope. Now: "the MD to be invited (Tamsin forwards the invite and chases him this week; his attendance is unconfirmed). Committed on the call; the invite is not yet sent." The same state is a verdict condition. The other nine commitments already carry owner, purpose and a date or "Not set", and none claims delivery; no `status` field was added, because that would change the shared shape of one key alone. The R10 rubric note also says "with the MD invited"; that sentence is v2 material and was left, noted for the v2 pass.
- **s11 (inference targets questions, never fills evidence).** Five unconfirmed client ties are in `signals` (the two on-hold reactions inside our sketch frame and at L459, the January showing for the retail technical team, Tamsin's read of the MD, the Carlisle whiteboard line) and drive the two read-back questions; none is used as evidence or in an element. One entity (`on-hold owner`) carries `source: assumed` because nobody owns a hold today ("It's nobody's.", L156).
- **s15 (a product limit never deletes a client need).** This fixture's own line. Customer visibility stays in `unmet_needs` with its clock and in leaning 8, and the fields that had closed it are reopened (section 1, item 1).

## 6. The readiness block

Built in the brief's exact shape from the key's own content. The block's dicts `structure`, `existing` and `verdict` are printed open one level deeper than the file's rule for other fields, so each leaning and each element row sits on its own line while every list entry stays compact, as elsewhere in the file.

- `pains`: the key's 13 entries in array order with their own quotes and locations, numbered by theme: P1.1 to P1.5, P2.1 to P2.5, P3.1, P3.2, and P1.6 for the last entry (the retention remark, which the key files under P1 at the end of the array). `stated_or_excavated` follows the key's own labels: the two entries the key marks "(excavated)" (P1.1, P2.1) are excavated, the rest stated. `outcome` is verbatim client speech aimed at the pain: Oisin's one-screen call (L342) for P1.1, P1.2 and P1.4; Dara's lab nobody walks into (L345) for P1.3; the on-hold list with a name (L364) for P2.1, P2.2 and P2.4; "the bakery thing doesn't happen" (L362) for P2.3; Tamsin's Monday-morning view (L347) for P3.1; "If I could see status I could see turnaround." (L294) for P3.2; null for P1.5, P2.5 and P1.6, where no client words aim at the pain.
- `signals`: five (section 5).
- `entities`: 23, answering "what moves independently of what?": the job and its tests, report, status code, due, on-hold state and owner, urgent flag, sample and form; customer and the retail account; site and discipline (sources open); status call, void or re-test; analyst and signatory as shared resources; the whiteboard, the spreadsheet, the export and the workbook as artefacts that go stale; the accreditation visit.
- `structure`: Work Management only; `own-account` with the A21 reason (a prospect: one lapsed trial board, no products, tier never stated); one workspace, "Marrowbeck – Ops"; native reuse none; 10 leanings; one pattern entry (held ready, not applied); 13 `element_per_pain` rows: 9 `fixes`, 2 `copies-today's-tool` (P1.5, because due is typed by Dara alone in v0.1, so the urgents view still rests on one person when she is out; P3.1, because the turnaround view runs on one hand-loaded night until a scheduled import exists, which is the spreadsheet the export lands in today), 2 `none` (P2.5, P1.6).
- `existing`: "unknown, no account bound" with the A21 point; eight incumbents with what each stays the record for.
- `assumptions`: 14, each with the question that would replace it.
- `unmet_needs`: 4 (customer visibility with the February clock; a current board; form quality; the retention risk).
- `ai_opportunities`: 4, all round 2 because the client never asked for AI or workflows (the one product mention is a lapsed trial, L169): a workflow (P-21) for the hold reminder once confirmed, an AI column (unprobed) for a plain where-is-it sentence, an agent (P-19) for the weekly turnaround summary, and a Vibe app (P-20) as one later way to meet the customer-visibility need without the vendor's portal, marked not in the first version.
- `verdict`: `build`. Two excavated pains with named entities and wanted outcomes in the client's words, one product, a stated structure with its leanings and the user's own account as target meet the brief's test. Eight conditions, the approval stop first, then the A11 point (none bites for an own-account target; the three decisions stay open), the workspace name, sample data (scrubbed export or invented; the sketch names are seed data only), the committed-not-booked walkthrough, no automation created, the as-of statement on the board, and the open customer need shown to the user. The key's `should_plugin_propose_a_build: true` and "Discovery complete" agree with the clearance, so the note gains no extra sentence.
- `questions`: five, the ceiling. Q1 and Q4 are read-backs (the on-hold tie; the January showing); Q2, Q3 and Q5 are discovery (the export; due; the candidate notifications). Reused from the key's ten: items 2, 3 and 8 in Q2, item 4 in Q3, items 5 and 6 in Q1, item 7 in Q4, item 10 in Q5. Dropped from the five: the account question (item 1; under A21 the proof of concept goes into the user's own account, and the client's account moves to handover), and November's exact dates (item 9; scheduling, not build; the first version stays out of the lab by design). Everything dropped is in the record as an assumption with its question.

No R-number, grade, gate name or verdict word is in the block; the script searched for them before writing. Two ordinary words a wider search turns up are not that vocabulary: "met" as a verb in "how it is met is open", which is the review's own recorded wording for item 1, and "seed data" in the verdict condition about the sketch names, which the key's traps and leak list already use in the same sense. `rubric` (bar the one date sentence of section 1), `expected_verdict` and `numbers` are untouched.

## 7. Transcript: no mess pass applied, and why

Section 5 of the brief applies the mess pass "with judgment" where our side speaks in writer-clean paragraphs. The Consultant's turns here already carry the hesitations the rule wants: "or, well, maybe one sketch" (L18), "I don't know" twice inside the sketch (L357, L359), "Good question, and I don't know yet" (L370), "I'll be honest" (L447). The one clean paragraph, the 130-word play-back at L454, is quoted at both ends (R12 evidence and the asked quote) and is a measured plant: the longest unit in the file, one of the three units the composite splitter scans, and the "longest own-side stretch" delivery note. Any word added anywhere would move eight measured figures in `intake` (words, the share under five words, talk share by speaker to three decimals, the longest unit) and the README's counts, for no gain in realism. Judgment: leave the transcript as it is. Unit count, numbering and stamps unchanged; nothing to re-cite.

## 8. README

Brought in line: the key file's description and line count (546, with the `readiness` block named); the quotes count (209: 179 with a location, 30 quote-only) with the verifier result and where the 43 new strings come from; a new "Readiness block" counts bullet; the 400-line sentence, now stating what the budget was and that the block takes the file past it in the file's own style; the dates paragraph, relative with the reason; the review-history sentence, which names the user's review of 2026-10-11 and the fix pass applied 2026-10-13 in one sentence, and "the direction header wording" in place of "direction-of-show". Counts that did not move were re-checked and left: traps 30 (6 look-alike), requested changes 1 / 4 / 0, commitments 10, pre-build questions 10, vocabulary 17, accepted behaviours 16, leak entries 16, objections 8, rubric rows 24.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 13 (2 excavated, 11 stated) |
| signals | 5 |
| entities | 23 (14 with a parent; all carry `moves_independently`) |
| leanings | 10 |
| element_per_pain | 13 (9 fixes, 2 copies-today's-tool, 2 none) |
| incumbents | 8 |
| assumptions | 14 |
| unmet needs | 4 |
| AI opportunities | 4 (all round 2) |
| existing fields corrected | 22 leaf paths outside `intake` and `readiness` (listed in sections 1, 4 and 5; counted by a path diff against the backup) |
| rename | 5 paths (`type_header` two fields, `type_segments` three) |
| transcript edits | 0 |
| key size | 546 lines from 392; 27 top-level fields from 26 |
| quote pairs | 209 from 166 (13 reused pains, 5 signals, 25 leaning quotes) |

Coverage row in `coverage-row.md`: same columns as the existing row, quote strings 209, Review column `reviewed 2026-10-13; fix pass applied 2026-10-13`; every other count unchanged and true of the edited files.

## 10. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s15-shred-dense`, final run after the last file write, exit code 0:

```
Fixture: s15-shred-dense
Sources: transcript.txt (transcript/line-time-first, 487 units)

pairs found      209
verified         209  (of which presence only, no location cited: 30)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were reported (no unit was renumbered). Independently, `apply.py` proved 36 new quote strings verbatim at their units before writing (6 `outcome` strings, which the shared verifier does not pair because the field name carries no "quote", plus the 5 signals and 25 leaning quotes), and re-proved the 13 reused pain quotes at their locations.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | Phone goes, one screen shows the job and when it's out, answer and hang up | L342, 22:18, Oisin Farrelly | P1.1, P1.2, P1.4 |
| G2 | A Monday view of the retail account's turnaround, without a spreadsheet and without her | L347, 22:36, Tamsin | P3.1, P3.2 |
| G3 | The retail account renews in February with the audit finding closed | L350, 22:52, Tamsin | P1.1, P1.4 |

Assumption kinds: leaning 8, gap 5, board-architecture 1.

Verifier: 209 pairs, 209 verified, 0 misses and 0 near-misses before; 212 pairs, 212 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G3 (the February renewal with the audit finding closed) is the operations director's read of the MD's win, kept with the key's own wording ("her read", L353) in its speaker role because she adopts it and it is the clock of the key's first unmet need; the lab manager's "Nobody walks into my lab" and the on-hold "list with a name on it" were left out as single-pain or group outcomes said inside the sketch frame, and each goal quote is one whole unit cited with the label exactly as printed.
