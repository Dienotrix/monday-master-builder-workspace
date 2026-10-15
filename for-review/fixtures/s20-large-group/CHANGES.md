# s20-large-group — fix pass changes

Editor's log, 2026-10-13. Everything in the fixture is fictional and stays fictional.

Files touched: `fixtures/s20-large-group/answer-key.json`, `transcript.txt` (the mess pass only, inside three existing Consultant units) and `README.md`. Method: the key was loaded, changed and dumped by script with a layout-preserving dumper, because this key is hand-laid-out (list entries on one line, the flat intake sub-blocks single lines, the plant sub-blocks one entry per line). The dumper learns which containers were multi-line from the original text and reproduces them; a round trip without changes reproduced the file byte for byte (128,542 bytes) before any edit. The 25 fields keep their order, `intake` stays 26th and `readiness` is the 27th and last. Every quote the block introduces was copied from the transcript and asserted verbatim at its unit by the build script before the file was written; the shared verifier then checked the whole key (278 pairs, zero misses). The verifier was run after each of the five stages, not only at the end.

## 1. The review entry, applied as recorded (FEEDBACK.md lines 200 to 209)

**Remake nuance (a fixture fix).** The follow-up now defines and measures both metrics rather than choosing one, and the record notes the definitional difference.
- `commitments_and_next_steps[3].what`: the remake-log count defines and measures customer-visible remakes (what the customer sees, the sales director's count) and work built twice (at least one panel through the shop twice, the production manager's count), each counted the same way throughout; the conflict is noted as a difference of definition and not only of figure.
- `traps[3]`: "which is itself the gap question, and the remake-log count in a week is the route" became the definitional difference noted beside the figures, with the count measuring both metrics.
- `intake.conflicts[0].handling`: "then a question on which count the record should carry" was the old route and contradicted the change; it now reads that the count defines and measures both metrics and that neither figure is carried until the book says.
- `intake.corrections_block_for_next_meeting[1]`: the count "will count both: remakes the customer saw and panels built twice".
- `vocabulary["remake / remake log"].likely_monday_object`: the paper log is counted two ways.
- Left, per the brief: the `rubric` P1 Cost inputs note and `expected_verdict.note` item (3) still say "then which count the record should carry". Both are v2 material the pass does not edit; noted for the v2 pass.

**Item 1: automatic ticket reprinting is a requirement, not a proven capability.** The requirement is that the floor knows when its ticket or proof is outdated; the default is a reprint-required flag set by the change with the ticket printed by hand; automatic printing only through an integration and only once probed; the production administrator validates.
- `expected_monday_products[0].why` (key line 40 in the review): "the ticket printed from the job so it reprints when the job changes" became the flag, hand printing and the probed integration.
- `vocabulary["job ticket / ticket"].likely_monday_object` (key line 100 in the review): "a printed view of the job item that reprints when the item changes" became the same, with the production administrator validating.
- `integrations_mentioned[5]`: "a printed ticket that reprints" was an output requirement; now a ticket that "reprints itself" is one form the production manager would accept ("I don't care how", 00:36:48), a board does not drive a shop printer, and the flag with hand printing is the default.
- `traps[20]`: "a printed ticket that reprints are conditions from the floor" was wrong: her conditions are screens, not tablets, and a ticket that prints (00:41:47, 00:45:23); reprinting itself is one of two forms she offered. Corrected.
- `traps[27]`: the automation list names "the reprint-required flag set by a change to the job or its approved proof" instead of "the ticket reprint trigger".
- `expected_questions_before_building[6]`: asks which changes set the flag, who prints by hand, and whether any print route is worth probing; the production administrator validates.
- `expected_structures.notes` and `commitments_and_next_steps[12].what`: "the printed ticket driven by the job" and "printed ticket from the job" now carry the flag.
- The lean in `readiness.structure.leanings` (leaning 2) carries the whole requirement with its quotes, including "Lettie prints it off the job sheet, one ticket per job" (00:17:31), and the production administrator's validation is a verdict condition.

**Item 2: the job board flattens production, and its stages are our playback.** The floor stages stay visible in the model; the grain is an open structural question with a leaning; the playback stages are recorded as our framing.
- `expected_monday_products[0].why` (key line 40): "one job board with the client's stages (proofing, production, ready, installed, invoiced)" became: the office-level stages are the Consultant's playback at 00:43:29, our framing accepted as "the right shape", not the client's list; the floor stages print, cut, fab, paint, assembly, ready (00:17:31) stay visible; the grain is open with the leaning named (store or job as parent with the office-level stages and the weekly roll-up; packages as children through the floor stages).
- `expected_structures.notes`: "with the client's stages" corrected the same way.
- `vocabulary["job"]`, `vocabulary["floor board"]`: the parent row and the child rows' floor stages, with the office-level stage labelled as our playback.
- `vocabulary["fascia sign / wayfinding package / pharmacy counter set"]` (key line 111, the glossary entry that "already floats subitems"): "subitems or a deliverable dropdown per store job" kept only the child rows; a dropdown on the store row would carry one stage for three things that move separately.
- `expected_questions_before_building[3]` gains the leaning; `commitments_and_next_steps[12].what` says the floor stages are visible.
- Leaning 1 in the block carries the question with the client's words (00:06:22, 00:17:31, 00:44:48) and the Consultant's "with the stages you use, proofing, production, ready, installed, invoiced" (00:43:29) cited as our framing.
- Not edited: `traps[22]` already said the playback is the Consultant's framing; the `rubric` R12 row cites the playback as the asked quote and stays (v2).

## 2. The `direction` rename

`intake.type_header.direction_of_show` is now `direction`, same position, same value (`no-show`). The key has no `intake.files[]` (one file). `direction_of_show` appears nowhere in the folder now. The README never named the field; one sentence was added saying what it is called.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry. A field was corrected when a builder reading it alone would build the flaw; where the field was only incomplete, the leaning carries it (exemplar rule).

1. **One row where the call describes many.** Four hits.
   - The job, the store and its packages (FEEDBACK item 2). One row per job with office-level stages would carry one stage for a fascia sign, a wayfinding package and a counter set that move through the floor separately, and one status for a job whose remade panel is back in paint while three hang. Leaning 1; fields corrected as in section 1.
   - Remakes. `vocabulary["remake / remake log"]` offered "status or subitem on the job"; the status branch is one value for eleven remade panels and builds the flaw. Corrected to a child row per remake event (panel, whether it was caught before shipping), which is also what lets both remake metrics be counted later. Leaning 4.
   - Proof versions. Several versions per job, one approved; and "a hundred and forty stores, which will each have their own proof" (00:17:17) may mean a proof per package. Leaning 3; `vocabulary["proof"]` ("file column plus a version and an approval status on the job") is incomplete, not wrong, so it stands.
   - Install visits. A job can take two visits (Traverse City); one install date on the job hides the second. Carried in leaning 5 with the crews.
2. **A pain with no element that fixes it.** One hit and one partial. P2.1 (quotes retyped): the board gives the floor sight of the typed job, but the typing stays until the estimating tool exports a won quote, which was never asked; `element_per_pain` says `copies-today's-tool` and leaning 8 carries the dependency. P4.1 (crews turn up to jobs not ready): the roll-up fixes the in-house cause (a panel back in paint) but nothing fixes "the permit's not through" or "the site's not ready for us"; both stay as hand-keyed claims in leaning 5 and as an unmet need (s15). No pain has `none`; the nearest candidate for `none` was P3.2, whose lag is measured in a system v0.1 does not touch, and it kept `fixes` because the flag removes the cause the controller named.
3. **An alias-map entry that names more than one entity.** Two hits, both corrected in `intake.alias_map`.
   - `Saginaw / Flint` named two places, two job sheets and, through the branch, a crew. Split into `Saginaw` and `Flint`, one place each, each with a note saying that the sheet is an artefact and the crew a resource. The map has 19 entries now (README updated). Leaning 6 says what "Flint" names in the build.
   - `Cordelia (marketing)` carried the form "the admin (possibly)". The administrator is unknown ("Who set it up originally I genuinely couldn't tell you", 00:10:01), so the form tied an unidentified person to a named one by inference. Removed; the note says the admin is a separate person until named (s11 line: inference never fills evidence).
   - Declined: "the pharmacy chain (unnamed)" lists "their project manager" and "their compliance people" among its forms; they are the customer's people spoken of only through the customer, not separate entities in this record, and the entry stands.
4. **Our framing labelled as the client's.** Two hits and one soft hit.
   - The stages (FEEDBACK item 2; leaning 1).
   - "a printed ticket that reprints" as a floor condition (`traps[20]`; section 1; leaning 2).
   - `expected_structures.notes` said "a screen-on-the-wall view per station"; the client said screens on the wall, and whether per station or one board is the key's own question 8. Corrected to "per station or one board is an open question"; leaning 10.
   - Checked and left: the leadership criteria (already relayed and labelled), "Service extras are deferred beyond v1 in any case" (the client asked for no desk or portal, so no client need is deleted; s15 does not bite), the four blockers (the client's own words).
5. **A shared resource with no reservation tracking.** One hit. Six two-person crews scheduled on a spreadsheet a week at a time, and a wasted trip means "that crew was supposed to be somewhere else the day they go back" (00:35:12). `vocabulary["install / crew / wasted trip"]` said "install schedule off the jobs", which a builder would make a date column on the job; corrected to visit rows with crew, date and go-conditions and a per-crew week view. Leaning 5. Declined: the router (reused across jobs and down since Friday, but no booking or contention is described; it is an entity with `shared_resource: true` and no leaning), the five designers (capacity, not a booking), coordinators (owners).
6. **An artefact that can go stale with nothing to flag it.** Three hits.
   - The ticket and the proof print-out (FEEDBACK item 1; leaning 2). The same leaning says the ticket prints the approved proof's dimensions, never the survey's, because Quarrington was a survey column typed into a ticket (00:07:52).
   - The weekly rollout status, built by hand every Friday from data that changes by Monday. Leaning 9: a view over the roll-up with its as-of time.
   - The Flint sheet, a copy that drifts from the Saginaw one; fixed by one board (P2.3) and carried in leaning 6, no separate leaning.
   - Also marked in `entities` with `goes_stale: true` and no leaning of their own: the job sheet row, the floor board (it shows where a ticket was moved, not where the job is), the install schedule, site readiness, a superseded proof version.
7. **An expected output the input cannot support.** No hit. Recounted before any edit and all true: 265 units, 6,011 words, client share 72% (4,328), the Consultant's longest turn 179 words at 00:43:29, the longest client turn 82 at 00:06:22, 38 units at or under four words, 8 adjacent same-label pairs, five ` -- ` (three inside units, two at line ends), [laughs] x3, [inaudible] x2, [crosstalk] x2, Delphine 58 turns at 35% of client words, Ximena 10 turns at 4%. The rollout customer is nowhere named. The dates: the key pins October 2026 from "Wednesday the twenty-first" together with "this autumn", "this quarter to build, January to be live" and "the week of February ninth", not from the weekday alone, and labels month and year inferred; the year is the fixture's calendar. Left as it is, and written down as an assumption with its question in the block.

## 4. The "never written to" rule

A search for "never written", "written to", "write back", "writeback", "never touch", "not written", "read-only" and "one way" finds no no-write claim in this key; s20 is not among the eleven keys FEEDBACK names. One direction claim was found and reworded:
- `integrations_mentioned[1]` called the accounting system the "destination of the installed signal for invoicing" and said "the connection is designed with the financial controller after November". "After November, talk to me" (00:30:59) says nothing about direction, and the client's instruction covers only the source of the job number (00:44:48, 00:45:06). Now: the job number's source by the client's instruction; whether the installed signal reaches the system and in which direction is unresolved; writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours; the client's own freeze until November holds regardless.
- The same direction assumption sat in `commitments_and_next_steps[11].what` ("Design the accounting-system connection (job numbers, installed signal)"), `expected_monday_products[0].why` ("typed until November and connected after") and `vocabulary["job number"]` ("sourced from the accounting system after"). All three now say typed in v0.1 and labelled as typed, any connection a conversation after November, direction unresolved.
- Checked and left, because each traces to a client quote: "Nothing may connect to it before November" (00:30:59, 00:31:16 by the Consultant echoing her), "the estimating tool stays" (00:44:48; the key already keeps the export question open and promises no integration). The block's incumbents line for the accounting system and leaning 7 use the rule's wording.

## 5. Standing lines, where they bite

- **s22 (a board status set by a person is a claim).** Bites on `ready`, the installed flag, the approval status and the permit and site confirmations. `vocabulary["ready"]` now says ready on the job is rolled up from its packages' floor stages and a hand-set ready is a claim, which is how the Traverse City trip happened; `vocabulary["install / crew / wasted trip"]` says the installed flag is the installer's claim with a date until a photo or the customer's sign-off is attached. In the block: leaning 3 (the approval status is the coordinator's claim, the reply the evidence), leaning 5 (permit and site readiness are keyed claims), leaning 7 (the invoice stays in the accounting system and the board shows the flag, not the invoice), and the `existing.incumbents` lines.
- **s21 (a commitment is `committed`, done only on evidence).** `commitments_and_next_steps[0].what` said "the managing director asked to attend"; on the call the operations director said "I'll ask Gideon", so it now reads "to be asked by the operations director; nothing is sent or confirmed yet". The other twelve entries each carry owner, purpose and a date or "not set" and none claims delivery. The walkthrough's committed state is a verdict condition. No `status` field was added (one decision for all keys, as the exemplars say).
- **s11 (inference targets questions, never fills evidence).** The "the admin (possibly)" alias form was removed (section 3). Eight unconfirmed ties are in `signals` and drive the two read-back questions; none is used as evidence or in an element. The installed flag is the one `entities` row marked `source: assumed` with `evidence: null`, because it is our element.
- **s15 (a product limit never deletes a client need).** Seven `unmet_needs`, among them a ticket that reprints itself (a board does not drive a printer), the invoice following the install without a person in between (the freeze and the unresolved direction), crews not driving to unpermitted or unready sites (no element), designers staying in the design tool (unanswered), the customer's weekly status in the customer's hands (nothing customer-facing in v0.1), remake labour counted, and crew access that does not cost a seat each (the owed written answer).

## 6. The readiness block, field by field

- `pains`: the key's eleven `pains` entries in array order, same quotes and locations. The key numbers them by theme only, so the ids are P1.1 to P1.3, P2.1 to P2.4, P3.1, P3.2, P4.1, and the unnumbered change-orders entry is P5.1, the next free number. `stated_or_excavated` follows the key's theme grading: P1 to P4 are excavated (the rubric records cross-speaker composition and the Consultant's questions), P5.1 is stated (the account manager volunteered it: "Can I add to that"). `outcome` is verbatim where a client said what they wanted: Imogen's "the ticket is never wrong" (00:36:48) for P1.1 to P1.3, Henrike's "I stop being a switchboard" (00:37:12) for P2.2, Delphine's "One screen. Not the job sheet, not two job sheets" (00:36:23) for P2.3 and her "the floor knows before the panel's cut" for P5.1. Null for P2.1 (nobody said what they wanted instead of retyping; "Answer the phone" is what the time would go to), P2.4 (no words aim at the weekly status; "without me living in the job sheet" at 00:40:32 is her account of what the managing director will ask), P3.1 and P3.2 (the financial controller had left before the forward question) and P4.1 (the installation manager gave none). Those nulls are why Q1 and Q4 exist.
- `signals`: eight. The production manager's "I don't care how" (never confirmed that a flag with hand printing is "the same thing"); the production administrator narrated as the person who "lives this more than any of us" and never heard; "That's the right shape" with nothing read back piece by pain; the financial controller's "It doesn't scale" with the installed flag played back after she had left; the installation manager's Traverse City account with the playback's install piece drawing no response from him; the branch manager's "Flint sees the same screen" against her "we'll quietly keep ours" five minutes later; the relayed leadership criteria; the coordination lead ruling out a typed job number while v0.1 types it.
- `entities`: thirty, answering what moves independently of what. Packages move independently of the store or job, panels of packages, proof versions of the job, change orders and remake events of the job, visits of the job, permits of the fascia sign; the quote, the survey, the job number, the approval and the invoice do not. Shared resources: the crews and the router. Stale artefacts: the job sheet row, the Flint sheet, the ticket, the proof print-out, a superseded proof version, the floor board, the install schedule, site readiness, the weekly status. Twenty-four have a parent and every one of them carries `moves_independently`.
- `structure`: Work Management only; `own-account`, "prospect, so the user's own account by default (A21)"; one workspace, "Ostlerby – Ops" (one product, one workspace, named for the fictional client with the brief's en dash, which makes the key UTF-8; the brief allows it); native reuse none, no CRM or Service entity; ten leanings (section 3); three parent-row-with-roll-up patterns (store or job with packages; job with visits; job with remake events); eleven `element_per_pain` rows, ten `fixes` and one `copies-today's-tool` (P2.1).
- `existing`: the account line says the proof of concept goes into the user's own account under A21, read at preflight, and that the client's own marketing account (Standard as self-corrected, 25 seats, administrator unknown) is a handover question; nine incumbents with what each stays the record for, the accounting system carrying the never-written wording.
- `assumptions`: fifteen, each with its question, among them the grain of non-rollout jobs, one proof per job in v0.1, made-up jobs, the typed job number, who prints and who moves stages, crews as a value on the visit, permits and site confirmations as keyed claims, the weekly status as a view, the Flint sheet holding nothing the board lacks (the read-back that fell out of the five questions lives here), the account manager keying changes, the automation allowance, the October 2026 dating, coordinators as owners, sample remake rows.
- `unmet_needs`: seven (section 5).
- `ai_opportunities`: five, all round 2, because the client never asked for AI or workflows. Three workflows cite P-21 (the reprint-required flag, the installed notification, the Friday rollout summary); one agent cites P-19 (where is job X, scoped to this client's workspace); one AI column is `unprobed` (reading the approval reply into columns for a coordinator to confirm, never to set the status).
- `verdict`: `build`. At least one pain has an entity and a wanted outcome in the client's words (P1.1, the ticket), the product is chosen, the structure is stated with its leanings, the build target is named. Seven conditions, the approval stop first, then that no A11 question first matters for an own-account build (the three stay open), the walkthrough as committed and not held, the production administrator's validation, the November freeze and the marketing administrator as handover points, made-up jobs unless the client prefers the sheets, and the floor stages shown as the floor's with the office-level stages labelled as ours.
- `questions`: five, the ceiling. Q1 is a read-back to the financial controller (she never heard the installed flag; the direction of any connection is not assumed). Q2 is a read-back to the production manager and the production administrator (the flag and hand printing against "I don't care how"). Q3 is a discovery question on the grain to the operations director and the production manager. Q4 is a discovery question to the installation manager on how crews are booked and where permits and site confirmations live. Q5 is a discovery question to the sales director on whether the estimating tool exports a won quote, which decides whether P2.1 is fixed or copied. Reused from the key's pool: items 4 (grain), 7 (the ticket), 10 (install), 11 (the installed flag); item 9 (Flint) was the sixth candidate, a read-back with a live signal, and went to the assumptions with its question because five is the ceiling and a view's columns change with it, not the shape. Dropped under A21: item 1 (which account) and items 2 and 3 (tier and seats), which are handover and the owed written answer, not the proof of concept; item 13 (the managing director's criteria) stays a condition of the walkthrough and a v2 matter, since no build element changes with it.
- The key's `should_plugin_propose_a_build` is `true` and its verdict "Discovery complete", so the block does not disagree with the v2 fields and the `note` carries the brief's two sentences only.
- No sales word is in the block: the build script searched it for R-numbers, gate, grade, Met, partial, missing, the three verdict strings, bleed, upside, rubric, not-obtainable and met-with-residual before writing.

## 7. Transcript: the mess pass

Under the s11 rule, applied with judgment: the Consultant's turns already carry false starts in about ten places, and the one writer-clean paragraph is the 179-word playback. Twelve words were added inside three existing units, each outside every quoted span (checked against the verifier's `--spans` listing before editing), with the stamps, labels, unit count and numbering unchanged:
- 00:38:29 (line 220): "Let's talk about, let's talk about how a decision like this gets made here" (+3; the quoted span is the last sentence of the unit).
- 00:43:29 (line 244): "Four. Install, um, install scheduling" (+2) and "Quoting stays in the estimating tool, I've heard that. ... Is that, is that the right shape?" (+5); the three quoted spans ("Let me play back ...", "with the stages you use ...", "An installed flag that tells Hester ...") are untouched.
- 00:47:51 (line 261): "and who in marketing, who actually looks after the account" (+2; no quote cites the unit).

Re-measured after the edit and written into the key and the README: 6,023 spoken words (from 6,011), the Consultant 1,695 (from 1,683), client share still 72% (4,328 of 6,023; 71.9% unrounded), the longest turn 186 words at 00:43:29 (from 179; still 79 s by the next start). Fields updated: `transcript_format` (three places), `intake.export_family.words` and `.max_unit_words`, `intake.detectors.composite_splitter`, `intake.share_by_side` (`client_by_words`, `our_side_by_words`, `longest_own_side_turn`) and `intake.delivery_notes[0]`. Unchanged and re-checked: 265 units, 268 lines, 38 units at or under four words, 8 adjacent same-label pairs, the per-speaker percentages, the own-side stretch lengths (the two stretches at 00:36:02 and 00:33:00 were not edited).

## 8. README

Brought in line: the transcript row (6,023 words), the key row (`intake` then `readiness`, 556 lines), the remake plant row (both metrics), the quote count (278 strings after the pass: 250 pairs, 54 from the block, 28 presence-only; 224 before), the alias-map count (19), a new counts bullet for the readiness block, the layout note (the 400-line budget was the authoring budget; the block takes the key to 556 lines in the same layout), the `direction` field named, the review status (reviewed by the user on 2026-10-12; the COVERAGE row updated by the merge step), and the one-sentence review-history line "Fix pass applied 2026-10-13: ..." at the end.

## 9. Coverage row

`coverage-row.md` holds the row in the thirteen columns of the s11 to s25 table. Only the quote-strings count moved (224 to 278); the Review column reads `reviewed 2026-10-13; fix pass applied 2026-10-13`.

## 10. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 11 (P1.1 to P5.1; 10 excavated, 1 stated; 6 with an outcome in the client's words) |
| signals | 8 |
| entities | 30 (24 with a parent, all with `moves_independently`; 2 shared resources; 9 that go stale) |
| leanings | 10 |
| element_per_pain | 11 (10 `fixes`, 1 `copies-today's-tool`, 0 `none`) |
| incumbents | 9 |
| assumptions | 15 |
| unmet needs | 7 |
| AI opportunities | 5 (all round 2; P-21 x3, P-19 x1, unprobed x1) |
| verdict | `build`, 7 conditions |
| existing fields corrected or reworded | 25 (listed in sections 1 to 5) |
| alias-map entries | 19 (from 18) |
| transcript edits | 3 units, +12 words, 0 units added |
| key size | 556 lines, 27 top-level fields (from 393 lines and 26) |

## 11. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s20-large-group`, run after every stage and finally after the mess pass and the count updates, exit code 0:

```
Fixture: s20-large-group
Sources: transcript.txt (transcript/line-bracket, 265 units)

pairs found      278
verified         278  (of which presence only, no location cited: 28)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were raised (no unit was renumbered). The build script's own assertions covered the 54 quotes the block introduces and the eleven `outcome` strings, which carry no location of their own and are therefore not among the verifier's pairs.

## 12. For the planner

- The `rubric` P1 Cost inputs note and `expected_verdict.note` item (3) still phrase the remake route as "which count the record should carry"; both are v2 fields the brief keeps untouched, and the v2 pass should align them with the two-metric change.
- The dating of the call (October 2026) rests on four client phrases and the fixture's calendar; the key labels it inferred and the block lists it as an assumption. If the s15 rule is read strictly (keep dates relative unless the input carries the call date), the `commitments_and_next_steps[0].date` string "2026-10-21 14:00 Eastern (Wednesday the 21st; month and year inferred)" is a candidate for "Wednesday the 21st, 14:00 Eastern, month inferred from the autumn clock, year unstated". Not changed here, because the s20 review entry did not ask for it and the month is not pinned from the weekday alone.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | Go after the hospital framework, showing how they'd run forty sites at once | 00:32:40 Delphine Castellane (Operations Director) | P2.3, P2.4 |
| G2 | One thing showing every live job, where it is, who's got it, what's late | 00:36:23 Delphine Castellane (Operations Director) | P2.2, P2.3, P2.4 |
| G3 | The ticket is never wrong: the floor sees what the customer signed | 00:36:48 Imogen Achebe (Production Manager) | P1.1, P1.2, P1.3, P5.1 |
| G4 | The building running on it in January, before the rollout's first stores | 00:40:54 Delphine Castellane (Operations Director) | P2.4 |

Assumption kinds: leaning 9, gap 5, automation-condition 1.

Verifier: 278 pairs, 278 verified, 0 misses and 0 near-misses before; 282 pairs, 282 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G1 is the operations director's own answer to what she would go after ("The hospital framework."), kept because she names the build as what stops the bid (she cannot show forty sites run at once), while s16's looser "Bigger wayfinding" upside was not counted; the managing director's two wins were left out because she relays them and declines to adopt them ("I'm not going to put words in his mouth"), which the key records as her account and not his words, and the coordination lead's switchboard line and the branch manager's same-screen line were left out as single-pain outcomes (P2.2, P2.3).
- G1's quote moved within the same turn at 00:32:40 from "The hospital framework." to the sentence that states the aim and its blocker.
