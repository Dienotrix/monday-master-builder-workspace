# s16-shred-cue — fix pass changes

Editor's log, 2026-10-13. Everything in this fixture is fictional and stays fictional.

Files touched: `fixtures/s16-shred-cue/transcript.txt` (five Consultant cues, mess pass only), `fixtures/s16-shred-cue/answer-key.json` (the review entry's changes, the rename, the sweep, the no-write rule, the s21 wording, the measured counts, the `readiness` block) and `fixtures/s16-shred-cue/README.md` (counts and review history). Work files beside this log: `build_key.py` (the key edit, with its proofs), `keyfmt.py` (the serializer), `measure.py` (transcript statistics), `edit_readme.py`, `answer-key.before.json` (the key as it was), `coverage-row.md`.

Method. The key is a hybrid: two-space indentation at the top, every list entry on one line. A plain `json.dump` would have rewritten all 378 lines, so `keyfmt.py` reproduces the file's own rule (array elements compact; objects whose values are all scalars compact; arrays of scalars one per line; everything else expanded) and was proved byte-identical on the untouched file before any change. The key was then loaded, changed and dumped with it; 23 original lines changed, all listed below, and the 25 fields keep their order with `intake` 26th and `readiness` 27th and last. Every quote the key gains was proved verbatim at its cue by the script before the file was written (52 proofs), and `verify_quotes.py` was run after the transcript edit and after the key edit. The transcript's own grammar is kept: `cue N, HH:MM:SS.mmm, Label` and `cues N-M, HH:MM:SS.mmm, Label`, with the label exactly as printed (`R` for Ruairi), and no new location crosses a label change.

## 1. The review entry's two changes (FEEDBACK.md, s16, 2026-10-12)

**Change 1, the item grain becomes an open structural question with a leaning.** Applied exactly as recorded.
- `expected_monday_products[0].why` (key line 28 before the pass) no longer builds "jobs with the six stations as a status flow ... and permits held on the job". It now states the grain as open, with the leaning in the entry's own words (job as parent row; signs or sign packages as child rows that each move through the six stations, the job showing a roll-up; permits as their own rows linked to the job or the building, each with its expiry and the install date it guards; small jobs a single row), the monday constraint (all subitems of a board share one column set, so signs and permits cannot both be subitems cleanly; one likely needs its own connected board), the two things to settle with the client (how independently signs move through the shop; how permits map to signs, buildings and install dates), and the evidence the entry cites: "Two hundred and some signs across four four buildings, kicks off after the first of the year, and it's forty-one permits." (cues 210-211, the reconstruction with the `four` duplication kept inside the marks) and "Forty-one permits with the same install crew and the same crane," (cue 109), with the entry's reason that one job status cannot show signs of the same project in router, paint, wiring and install at once.
- `expected_structures.notes` carries the same open grain in place of "jobs with the six stations, permits on the job".
- `expected_questions_before_building[9]` (the key's own open question, line 181) keeps its question and gains the leaning and the settling conditions, so the question and the product line no longer contradict each other.
- Fields a builder would have read alone and built the flaw from were corrected and point at the leaning: `vocabulary["permit / re-permit"].likely_monday_object` ("columns on the job" builds one permit per job, and the hospital job has forty-one), `vocabulary["the board / the wall"]` and `vocabulary["magnet"]` (both put the station status on the job item), `expected_structures.lookalike_traps[4]` (the whiteboard trap pinned the status flow to the Jobs board), and `expected_structures.portfolio_reason` (now says the modelling question is open with its leaning). Left as they stand, because they are only silent on the row: `vocabulary["stations"]` ("status labels or groups, in this order") and `vocabulary["job / job number"]`.
- The readiness block carries it as leaning 1 (pattern "one row where the call describes many"), the parent-row-with-roll-up pattern, the entities `sign or sign package` (`moves_independently: unknown`, which is exactly the condition), `building` and `permit`, question 1 and assumptions 1 to 3.

**Change 2, a change-request element on the job.** Applied exactly as recorded.
- `expected_structures.notes` now carries the change request: its source (who heard it, through which channel), what changed, the sign or signs it affects, the current approved version, a required shop acknowledgment before the affected signs move on, a notification to the shop when one is raised, and one capture point the three people who hear of changes can all use (a form is the natural fit), since the estimator's spreadsheet stays where it is and is where the last change got stuck; who may raise one and who approves it is open, as the entry says.
- `expected_monday_products[0].why` names the element; `expected_questions_before_building[6]` now asks who approves as well as who may raise one, and names the element; `vocabulary["change order"].likely_monday_object` no longer reads "subitem or update on the job" (an update is a post, which is where a change would sit unseen) and describes the change request, with its shape (subitem or connected board) following the grain decision because of the shared subitem column set.
- The readiness block carries it as leaning 2 (pattern "a pain with no element that fixes it"), with the entry's four quotes at cues 130, 138, 142 and 227; `element_per_pain` P2.1 and P2.2 now read `fixes`, with P2.2's dependency on the estimator raising one recorded as assumption 9; question 2 reads Ruairi's wanted outcome back, because our play-back on the call (cues 269 to 273) never answered it.

## 2. The `direction` rename

`intake.type_header.direction_of_show` is now `direction`, in the same position (fourth key of the type header, between `relationship` and `output_class`), value `no-show` unchanged. The fixture has one input file and no `files[]` headers. `direction_of_show` appears nowhere in the key now. The README did not name the field; its intake bullet now records the rename so the counts section matches the key.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry; a field was corrected only where a builder reading it alone would build the flaw.

1. **One row where the call describes many.** One hit, the review entry's own: the job carrying one status and one permit field for a project of two hundred and some signs, four buildings and forty-one permits (leaning 1; fields corrected as in section 1). Considered and folded into the same leaning rather than given its own: the building as a layer (the hospital's two city and two county buildings with permits in November for the first), since the leaning already lets permits link to the job or the building. Considered and declined: the crane as "one row for many bookings", which is pattern 5 below.
2. **A pain with no element that fixes it.** Four hits.
   - P2 (change orders): the review entry's second change, leaning 2.
   - P2.3 "And when Ruairi's out, nobody walks the board." (cue 163): a screen version of the wall is still set by one person after a walk, which the floor-does-not-type constraint forces; the office sees it without walking out, but nobody moves it when he is out. `element_per_pain` P2.3 is `copies-today's-tool`, and leaning 8 carries a deputy, a stale-status view and the open question whether a station lead will tap a status on the shop tablet.
   - P3.1 (unchased quotes): a Quotes board with a next-chase date is what the spreadsheet lacks, but until quotes reach it by a feed or Ottilie keys them it is a second list of the same sixty quotes. `element_per_pain` P3.1 is `copies-today's-tool`; leaning 7 and assumption 11 carry the import question, which the key already asked (question 8 of the pool).
   - P5.1 "Everybody calls Dad." (cue 172): `none`. No board changes whom the landlord calls; the owner's two wins are served through P1 and P2, and the key already marks the habit internal only. Kept visible as a finding.
3. **An alias-map entry that names more than one entity.** No hit. The alias map has two entries, `R` = Ruairi and `Dad` = Gerrit Achterberg, one person each. Nearest candidate: the vocabulary entry "GC / landlord / tenant", which names three roles; it is a glossary line for one type column's values, not an alias entry, and the key already keeps it as such. Nothing split.
4. **Our framing labelled as the client's.** One hit. `expected_structures.lookalike_traps[3]` said "the client asked for permits on the job in Work Management". "Permits on the job" was the Consultant's play-back (cue 271); the client agreed the order ("Yes. That's the right order. Permits first, then the wall, then quotes.", cue 274) and added the install-date requirement (cue 276), not the shape. Corrected, and the point is written into leaning 1's option. Checked and left: the six stations (Ruairi's own list, cue 115), the three-piece order (the client's sentence at 274), the spreadsheet staying on day one (cue 256), "quotes are deals" (already labelled ours in the key, since the client never says "deal"), and install scheduling against the crane (presented in the product line as our addition, not as the client's ask).
5. **A shared resource with no reservation tracking.** Two hits.
   - The crane and the crews: one rented crane from one outfit ("and when they're booked, we're booked.", cue 19), booked for the Monday the permit had expired (cue 88), forty-one permits and one crane (cue 215). The key had "date or timeline column, or a connected Crane bookings board" and the question of who owns the install date, and nothing on who holds the crane when. Leaning 3: the booking and the crew on the install row, with the outfit's confirmation as the evidence and a booked status as our claim; its condition includes whether install scheduling is wanted in the first version at all, since the client ranked permits and the wall first. No field corrected: `vocabulary["the crane"]` is incomplete, not wrong.
   - A station as a queue: "the paint booth had three jobs queued that were all due the same day." (cue 166). Leaning 4: a per-station view sorted by install date; no capacity figure, because none was given. The entity `station` carries `shared_resource: true`.
6. **An artefact that can go stale with nothing to flag it.** Three hits, one of them the review entry's.
   - The change to the shop (the cross-fixture list names it for s16): the shop's version of a sign goes stale when a re-quote changes it. Leaning 2's "current approved version" and the acknowledgment before the affected signs move on are the flag; the entity `drawing` carries `goes_stale: true`.
   - The install date and the permit's fit: the date lives "On the board, in the install column." (125), "And in Lyle's head." (126) and in the permit spreadsheet "if somebody told her." (127); the warning the client asked for (cue 276) is computed from it, so a stale date gives a wrong warning. Leaning 5: one owned install date with a last-changed stamp, the warning re-raised when either input moves. The entities `install`, `permit`, `calendar reminders`, `magnet`, `the whiteboard` and the `Friday photo` carry `goes_stale: true`.
   - Copied lists: the permit spreadsheet seed (committed with amounts removed, cue 288) and any quote import drift from sheets that are still being kept. Leaning 6: source and import date on every copied row; Nkechi's sheet retires at the November cut-over at latest, the quoting spreadsheet does not retire in the first version.
7. **An expected output the input cannot support.** No hit. The statistics in `transcript_format`, `intake.export_family` and `intake.silence` were re-measured from the file (`measure.py`): 298 units, 121 adjacent same-label pairs (0.407), longest unit cue 177 at 37 words and 12.8 seconds, 33 lowercase-initial units, 34 without terminal punctuation, 53 of four words or fewer, 159.5 seconds unlabelled (0.117), one gap over three seconds (5.8 s before cue 179), the own-side stretch 21-23 at 64 words, nine zero-gap wedges at the listed cues. All true before the pass; the word figures moved with the mess pass and were updated (section 7). The date reasoning was checked: 8 October 2026 is a Thursday and 8 September 2026 is a Tuesday, so "Thursday the eighth" after a September call fits October, which the key states as a fit, not a pinned date. The bleed arithmetic in `numbers` is v2 material and was read, not edited; it is arithmetic on client inputs.

## 4. The "never written to" rule

s16 is one of the eleven keys FEEDBACK names. A search for "written", "write", "touch", "book of record", "one-way" and "read-only" found these claims:
- `integrations_mentioned[0]`, "Not to be touched ... never written back". It traces to a client line, Rosamund relaying the accountant's condition: "She'd want to know it doesn't touch the accounting system." (cue 236) followed by "Which it won't, I assume." (cue 237). The accountant was not on the call. Reworded to say exactly that, with "nothing is written back in v0.1", and the rule's wording added: writeback and integration direction beyond that are unresolved, v0.1 does not depend on either, staying clear of the system is our safe default, labelled as ours.
- `compliance_or_security_signals[2]`, "The accounting system is the book of record for amounts and must not be written to". "Book of record" is our phrase; nobody on the call said it. Reworded to the client trace (cue 236, relayed, with "I assume" at 237), "v0.1 writes nothing to it and does not depend on writing to it", and a note that "book of record" was ours.
- `expected_structures.notes`, "The accounting system is never written to." Now: not written to in v0.1, resting on the relayed expectation at cues 236 and 237 and on nothing stronger; the unresolved wording; our safe default labelled as ours.
- `integrations_mentioned[1]`, "a read-only import or a later step, never a replacement". "Never a replacement" traces to cue 256; "read-only import" is ours and is now labelled as our default and as the key's own question.
- Checked and left: `entities_and_workflows[10]` ("the accountant must not see the accounting system touched", a paraphrase of cue 236 presented as a decision fact); `expected_questions_before_building[7]` ("is a one-way import acceptable on day one?", a question, which is the right shape); the portal line ("no integration asked for or promised", true). The readiness block's `existing.incumbents` entry for the accounting system uses the rule's wording, and the verdict's last condition says nothing is written to the accounting system, the quoting spreadsheet or the permit portals.

## 5. Standing lines where they bite

- **s21 (a commitment is committed, with owner, purpose and when; done only on evidence).** `commitments_and_next_steps[0].what` listed the walkthrough as "with Rosamund, Ruairi, Nkechi and the owner"; the owner's attendance is Rosamund's intention ("I'll forward it.", cue 286; "I'd want Dad to see the permit piece and the wall.", cue 278) and he has not said yes. Now "Committed on the call ... the owner is to be brought by Rosamund and his attendance is not confirmed by him". Entries 1 to 4 (the invite, the forward, the permit spreadsheet, the recap) now open with "Committed on the call" or "Committed, conditional on", and say nothing is sent or received yet. Owners and dates were already present and stand. No `status` field was added, since that would change the shared shape; the same state is in the verdict's conditions and in assumption 15. The R10 note says "The Consultant sends the invite on the day of the call" and sits in `rubric`, which is v2 material and untouched; noted for the v2 pass.
- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites in four places, all in the block: the permit's submitted, approved and expiry dates are keyed by Nkechi from the portal and are her claim, the portal is the evidence (incumbent entry; unmet need 4); a booked crane is a claim about the rental outfit's calendar until the outfit confirms (leaning 3; incumbent entry; unmet need 5); the install date on the board is a claim about what Lyle and the customer agreed (leaning 5); the station status is set by one person after a walk, as the magnet is today, which is why P2.3 is `copies-today's-tool` (leaning 8). The shop's acknowledgment of a change request happens in monday under this design, so there it is the event, not a claim about another system.
- **s11 (inference targets questions, never fills evidence).** Seven unconfirmed client ties are in `signals`, each naming what our side never confirmed, and two of the five questions are read-backs of them (Ruairi's wanted outcome at cue 227, which our play-back did not answer; the owner's two wins relayed at cues 229 and 230). None is used as evidence or in an element. Where a shape is inferred rather than spoken, the entity says so (`sign or sign package` and `drawing` carry `moves_independently: unknown`).
- **s15 (a product limit never deletes a client need).** Eight needs the build does not meet stay in `unmet_needs` with their clocks: the win rate (the estimator's, a different room), the remake and backcharge actuals, quotes without double keying, the permit's status without checking the portal by hand, crane availability from the outfit, the wall staying up until the owner trusts the screen (spring), shop-floor status moves without typing (January), and what remakes look like once the hospital job runs.

## 6. The readiness block

Built in the brief's exact shape as the 27th and last field. The old verdict fields (`should_plugin_propose_a_build: true`, `expected_verdict`, `rubric`, `numbers`) agree with the block's clearance, so the `note` carries no extra sentence; none of them was edited.

- `pains`: the key's ten `pains` entries in array order, same quotes and locations. Ids follow the key's themes with a running number after the dot: P1.1 to P1.3, P2.1 to P2.4, P3.1, then the two unnumbered entries get the next free numbers, P4.1 (install dates in three places, cue 126) and P5.1 (escalations to the founder, cue 172). P1 and P2 entries are `excavated`, as the key grades them; P3.1, P4.1 and P5.1 are `stated`. Outcomes are verbatim from the client: Nkechi's at cue 225 (P1.1, P1.2), Rosamund's at cues 222-223 (P1.3, P2.4, P4.1) and 224 (P2.3), Ruairi's at cue 227 (P2.1, P2.2); P3.1 and P5.1 carry null, because no outcome words on the call aim at quotes or at the escalation habit. `speaker_role` names the role, never the person, with Ruairi's label given as `R`.
- `signals`: seven (cues 227, 230, 229, 260, 237, 267, 292).
- `entities`: twenty-six, seventeen with a parent, every one with `moves_independently`. `shared_resource` is true for the station, the crews, the crane and its booking; `goes_stale` is true for the drawing, the permit, the whiteboard, the magnet, the Friday photo, the install, the crane booking, the two spreadsheets and the calendar reminders. The owner is listed so that no board is ever made from him. All sources are `spoken`, each with a cue; the two inferred shapes are marked `unknown` rather than given an assumed source.
- `structure`: Work Management and CRM; `own-account`, reason "prospect, so the user's own account by default (A21)": there is no account ("That's the extent of it.", cue 265), the tier is never stated and nothing has been bought; workspaces `Tallgrass – Ops` and `Tallgrass – CRM` with the brief's en dash (the key was ASCII before and is UTF-8 now, which the brief allows; the transcript stays ASCII); native reuse Deals/Opportunities relabelled Quotes, Accounts, Contacts conditional, detected in the user's own account before quotes are mapped; eight leanings; one pattern applied (parent-row-with-roll-up, with what rolls up stated); ten `element_per_pain` rows (seven `fixes`, two `copies-today's-tool`, one `none`).
- `existing`: "unknown, no account bound" with the A21 point, and eight incumbents with what each stays the record for. The key's own question "Which account will this go in ..." (pool question 1) and `account_context.existing_monday_setup` still say the plugin should ask which account; under A21 the proof of concept does not need it, so it is not one of the five and `existing.account` says it moves to handover. Both existing fields were left as they are, as the s1 exemplar did.
- `assumptions`: sixteen, each with the question that would replace it. Pool questions that are not among the five live here: stations complete (4), the shop screen (5), quote fields and accounts (8), the seed (9), the account at handover (1).
- `unmet_needs`: eight (section 5, s15).
- `ai_opportunities`: five, all round 2, because the client never asked for AI or workflows. The two workflows cite P-21, as the s5 exemplar did for that kind; the AI column, the agent and the sequence are `unprobed`. No credit figure, price or package anywhere.
- `verdict`: `build`. Two pains with named entities and wanted outcomes in the client's words, two products chosen, the structure stated with its leanings, the build target named. Seven conditions, the approval stop first; no A11 question first matters for an own-account build, and the three A11 decisions stay open; the grain confirmation, the owner's unconfirmed attendance, the committed-not-sent items, native CRM detection and the no-write line follow.
- `questions`: five, the ceiling. Q1 (grain; discovery; Ruairi and Nkechi), Q2 (change request; read-back of cue 227; Ruairi, then Rosamund and Ottilie), Q3 (the owner's test and his attendance; read-back of cues 229 and 230; Rosamund and the owner), Q4 (install date owner and crane booking; discovery; Ruairi and Lyle), Q5 (permit offices and the warning; discovery; Nkechi). From the key's pool: 10 is Q1, 7 is Q2, 6 is Q4, 2 and 3 are Q5; 1, 4, 5, 8 and 9 are assumptions with their questions. Each says what the record already holds, by cue.

No R-number, grade, gate name or verdict word is in the block; the script scanned for them before writing (and rejected one ordinary use of "missing" in an assumption question, which was reworded so no grader could misread it). `excavated` appears only as the value the brief's own field `stated_or_excavated` takes.

## 7. Transcript edits (mess pass, brief section 5)

Five Consultant cues, none quoted in the key or the README, none the longest unit, none of four words or fewer, each edited inside its own unit: cue 52 (a repeated half-phrase and a "So"), cue 182 (a false start and an "honestly"), cue 207 (a restart of the question), cue 266 (an "Okay", a repeat of "that's fine", a "you" and a "later on"), cue 280 (a false start). The number of units (298), their numbering, their timing lines, the line count (1,193) and every speaker label are unchanged; the longest unit is still cue 177 at 37 words and 12.8 seconds; the same-label pair count (121), the lowercase-initial count (33), the terminal-punctuation count (34) and the short-unit count (53) are unchanged. Word count 3,173 to 3,195 (3,180 to 3,202 with bracketed tokens); client share by words 0.754 to 0.749, by seconds 0.746 unchanged; by-speaker shares still round to Rosamund 41, Ruairi 17, Nkechi 17. Updated in the key: `transcript_format` ("about 3,195 spoken words"), `intake.export_family.words` and its note, `intake.silence.talk_share.client_by_words`; in the README: the file table and the intake bullet. The verifier was run after the transcript edit (124 of 124, before the key changed) and after the key edit.

## 8. README

Brought in line: the file table (3,195 words, the talk shares, the key's 537 lines and the `readiness` block), the Products bullet (grain open, change request named), the Quotes bullet (162 checked strings, with the 38 new ones accounted for), the intake bullet (3,195 words, 74.9 percent, the `direction` rename), a new Readiness bullet with the block's counts, the conventions bullet (the one-line-per-entry convention kept; the 400-line budget superseded by the block; UTF-8), the review status ("Reviewed by the user on 2026-10-12" in place of "Not yet reviewed") and, at the end of the review-history paragraph, the one-sentence line "Fix pass applied 2026-10-13: ...". Fifty-eight lines, from fifty-seven.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 10 |
| signals | 7 |
| entities | 26 (17 with a parent, all with `moves_independently`) |
| leanings | 8 |
| element_per_pain | 10 (7 fixes, 2 copies-today's-tool, 1 none) |
| incumbents | 8 |
| assumptions | 16 |
| unmet needs | 8 |
| AI opportunities | 5 |
| existing key fields corrected or reworded | 23 lines (listed in sections 1 to 5 and 7) |
| transcript units edited | 5 (298 units, unchanged count) |
| key size | 537 lines, 27 top-level fields, from 378 lines and 26 |
| quote pairs verified | 162 of 162, from 124 |

## 10. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s16-shred-cue`, final run after all edits, exit code 0:

```
Fixture: s16-shred-cue
Sources: transcript.txt (transcript/vtt, 298 units)

pairs found      162
verified         162  (of which presence only, no location cited: 24)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
refused_quotes   6 entries in 1 list(s) are the key's own refusals and are not checked
```

No location notes were reported: the fixture's units were not renumbered, every citation keeps its index, stamp and label. The edit script's own walk proved 52 quote strings at their cues before writing, including the ten outcome strings and the quotes embedded in prose fields, which the shared verifier does not pair.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | The founder out of the day-to-day by spring | cue 217, 00:16:06.393, Rosamund Achterberg | P5.1, P2.3 |
| G2 | Monday morning, every job: where on the floor, when it installs, whether the permit's good | cues 222-223, 00:16:31.119, Rosamund Achterberg | P1.3, P2.3, P2.4, P4.1 |
| G3 | The permit tells her before it expires, not her telling herself | cue 225, 00:16:46.144, Nkechi Brandvold | P1.1, P1.2 |
| G4 | The board big on a shop screen, magnets moving when a change comes in | cue 227, 00:16:57.485, R | P2.1, P2.2 |

Assumption kinds: leaning 10, gap 4, board-architecture 2.

Verifier: 162 pairs, 162 verified, 0 misses and 0 near-misses before; 166 pairs, 166 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G1 (the founder out of the day-to-day by spring) is relayed by his daughter about him, kept because she gives it as one of the company's two reasons for acting now and the key's R3 cites it as the client-side clock, with the relay said in its speaker role; G2 is the merged run at cues 222-223, which the key's intake lists as a clean two-unit run with no wedge or duplication and itself cites at R6, while every other goal is one whole cue; the owner's relayed wins (crane not out empty, not paying for the same sign twice) and the November and January dates were left out as relayed wins and a delivery clock.
