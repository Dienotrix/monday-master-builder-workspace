# s24-package — fix pass changes

Editor's log, 2026-10-13. Everything in this fixture is fictional and stays fictional.

Files touched: `fixtures/s24-package/answer-key.json`, `README.md`, and four transcript lines in `rec-4402-first-look.txt`, `rec-4397-production-walkthrough.txt` and `rec-4409-pricing.txt` (the mess pass, section 6). `rec-4418-discovery.txt` and `rec-4431-internal-review.txt` are unchanged. The key was loaded, changed and dumped by a script with a printer that reproduces the file's own layout (one entry per line inside expanded top-level containers); a round trip of the untouched key reproduced it byte for byte before any change. The 25 fields keep their order, `intake` follows them and `readiness` is the 27th and last. The key is UTF-8 as before; the workspace name adds the brief's en dash. A backup of the untouched fixture sits in the session scratchpad only.

Order of work, as the task set: the review entry's two changes; the direction rename; the seven-pattern sweep; the "never written to" rule; the standing lines; the readiness block; the README; the coverage row. The verifier ran after the transcript edits and again after the key was written; both runs are clean, and the second is pasted at the end.

## 1. The review entry (FEEDBACK.md, s24, 2026-10-10)

**Item 1, the Jobs-board stages.** The six stages, Art, Proof Out, Approved, In Production, Ready, Installed, replace "quoted to invoiced" in the four places the entry names, found by field rather than by line number:

- `expected_monday_products[0].why` (key line 34): "the stage from quoted to invoiced" is now the six the client confirmed on the discovery call, with the demo's eight named as the sales engineer's framing in the same clause.
- `vocabulary[0]` (`job`, line 90): `likely_monday_object` carries the six with their locations (rec-4418 31:25 and 32:11) and says the quoted-to-invoiced list was the sales engineer's; a job number exists only once a quote converts; quoting and invoicing stay outside the board. The `meaning` ("from the quote's yes to the invoice") is the life of a job and is untouched, as the entry says.
- `expected_structures.notes` (line 250): the stage list replaced in place.
- `expected_leak_blocklist`, the "Flag, do not remove" group (line 290): "the stages quoted to invoiced" is now the six.
- The demo's eight-stage list is recorded as our-side framing in a new `traps` entry (the 30th): the sales engineer's list at rec-4402 01:43, the account manager's "That's my spreadsheet with colors." recognising the board and not its endpoints, the client's own six at rec-4418 31:25 confirmed at 32:11, the job number at 04:31, the quotes at 05:15 and the agreed scope at rec-4409 02:46 and 03:40. A trap is where this key tells a grader what not to do, so the eight-stage list sits there rather than in the blueprint notes. Traps go from 29 to 30 and the coverage row follows.

**Item 1, the open question.** `expected_questions_before_building` gains a twelfth entry: what event or status hands a completed job to the office manager, who invoices 'once Jesse tells her it's done' (rec-4418 08:35). It says that the hand-off is a notification or a check the account manager owns, not a stage on the board, and that the accounting package is not touched for it. It is also the settling condition of readiness leaning 2 and question 4 of the block.

**Item 2, the pieces fork.** `intake.forks[0]` gains a `leaning` after `our_side_in_room`: the option (the separate Production board, option_b), the seven quotes the entry lists with their locations as parallel `quotes` and `locations` arrays (rec-4402 08:15; rec-4397 02:06 and 03:33; rec-4402 08:34; rec-4397 03:38; rec-4397 03:01; rec-4409 03:40), the live condition (show the account manager the rolled-up job row working, then ask the production manager to confirm the separate Production board, before history builds up, with the reversibility fact at rec-4397 03:10 attached) and a `status` line saying it is a leaning and not a decision, that the seller's internal pick (rec-4431 00:53) stays a delivery note, that only the user sets the blocking flag [L14] and that no numeric confidence is recorded. The fork's `handling` is reworded so the hand-off is no longer "which of these two architectures do you want?". The same leaning is mirrored as `readiness.structure.leanings[0]` with `pattern: fork`.

Where the key described the fork elsewhere it now carries the leaning in one clause, so no field contradicts the block: `expected_questions_before_building[0]` (rewritten to the new hand-off), `vocabulary[1]` (`piece`), `expected_monday_products[0].why`, `expected_structures.notes`, the fork trap, and the fork line in `accepted_behaviours`. Nothing in `rubric`, `expected_verdict` or `numbers` was touched.

## 2. The direction rename

`intake.files[*].type_header.direction_of_show` became `direction` in all five file headers, and the two `direction_of_show_note` fields (rec-4402, rec-4397) became `direction_note`, keeping the `<field>_note` convention and the field order. A search of the written key finds no `direction_of_show`. The README did not name the field; its conventions section now says what the dimension is called.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry. Where the hit sat in an existing field and a builder reading that field alone would build the flaw, the field was corrected too (the exemplar's test); where the field was only incomplete, the leaning carries it.

1. **One row where the call describes many.** Two hits. The job and its pieces, already the fork: leaning 1 and the parent-row-with-roll-up pattern (job with pieces as child rows, the stage rolling up). The proof with two approvers (rec-4397 10:46, 10:59): one Proof Out status with one stamp would carry one value for two people who answer separately; leaning 4 (one approval per approver, the rule running until both are in), condition the account manager's answer on sequential or parallel. No field corrected: the key already calls the mechanism unverified.
2. **A pain with no element that fixes it.** Two hits, both partial rather than empty, so no `none` verdict. The designer half of the production manager's chase (P1.2, "I chase designers for art and I chase customers for approvals"): the proof rule times Proof Out and nothing times Art; leaning 5. The customer's yes reaching the board (P1.2, P1.3): the no-login approval is a claim the seller's own side doubted, so in v0.1 a person sets Approved; leaning 10. P1.2 is `copies-today's-tool` for both reasons. Checked and left as `fixes`: P3.1, P3.2, P4.1, P5.1, P1.1, P1.3 (with their conditions in the element text).
3. **An alias-map entry that names more than one entity.** One hit, corrected. "Tamarack Peaks (credit union, customer)" carried "their Valley branch", "the Cheney branch" and "the branch manager" as forms: an organisation, two places and a person role in one entry. Split into four entries (the customer; the Valley branch; the Cheney branch; the credit union's branch managers, one per branch), with notes; 13 entries become 16 and the README follows. Leaning 6 carries the structural side: one job per branch, or child rows under one rebrand job, settled by whether the estimating system issues one job number per branch (rec-4418 05:10, 15:02, 12:12). The other entries were read and stand: each pairs a person with their short forms, roster spelling or misheard form.
4. **Our framing labelled as the client's.** Three hits. The Jobs-board stages (item 1 above; leaning 2). The piece stages: the flag-do-not-remove list carried "printed, laminated, cut, QC, ready", which is the sales engineer's list at rec-4402 05:27; the client's own are "Print. Laminate if it's laminated. Cut, or weed if it's vinyl. QC ... Then it's ready." (rec-4418 07:58) and the whiteboard's "Press, finish, QC, ready." (06:53). The list entry now says whose list is whose; leaning 3 (stations as the client names them, a piece skipping the ones its path does not pass). The remove entry in `requested_changes` quoted the seller's "No. Invoicing stays where it is. Nothing touches the books." as the client's request; its quote is now the owner's own exclusion at rec-4418 05:15 and the description says which exclusion is whose (also section 4). Checked and left: the seller's playbacks are already marked as framing in `second_hand`; the fifty an hour is already the seller's throughout.
5. **A shared resource with no reservation tracking.** One hit, one declined. The stations and the schedule: the stations are shared across every piece ("a rush bumps something else", 14:45; "whatever job was supposed to be on that press that afternoon", 18:51) and the schedule spreadsheet, which "is supposed to match" the wall (07:12), is the artefact that may have held a sequence per station per day; the package never says. `vocabulary["the schedule"].likely_monday_object` read "replaced by the Jobs board and its views", which a builder would take as the whole answer; corrected to say what is unknown and to point at leaning 7 (a queue by station in v0.1, nothing booked, the floor hour settles it). Crews are a shared resource with tracking already in the key (the same-crew-same-day warning), so they carry `shared_resource: true` in `entities` and need no leaning. Declined: material as a reservation. One roll can serve several pieces and the per-piece status is set from memory, but the client asked for exactly that thin column ("Thin's fine.") and has no number; it is an assumption with its question and `shared_resource: true`, `goes_stale: true` on the entity, not a leaning forced to fill the pattern.
6. **An artefact that can go stale with nothing to flag it.** Two hits. The printed ticket with the stapled proof (06:30, 17:07), today's real control, goes stale when a later version is approved or the due date moves after release; nothing in the key said whether it stays once the floor screen exists. Leaning 8 (the ticket stays until the production manager says otherwise; the job item shows that it changed after release; the ticket is reprinted by hand, since no board drives a shop printer, the s20 line); `vocabulary["ticket"]` points at it. The approved file (rec-4402 11:17; rec-4397 04:16; rec-4431 02:44): the lock the sales engineer showed would freeze the first approval, while a re-approved version must replace it; leaning 9, and P2.1 and P2.2 are `copies-today's-tool` until the restriction is verified on the tier bought, in the production manager's own words ("It's still a person picking the right file."). The whiteboard, the schedule, the account manager's spreadsheet and the group text carry `goes_stale: true` as replaced artefacts without leanings of their own.
7. **An expected output the input cannot support.** No hit. Checked: every date is read from a Date line or a booking on a prior call; the transcript statistics in `transcript_format` were recounted (lines, turns, words, shares and longest turns all matched before the mess pass and were updated for it, section 6); the "about 39% while the screen is shared" figure in `talk_share` holds when the frame is taken from 00:52 as the quarantine states it (38.7% before, 38.5% after); the lock, the no-login approval and the estimating export are already marked claims; the install lead's return on 1 September follows from rec-4397 09:45. The nearest candidate was the hand-off to invoicing, which the key had neither as a stage nor as a question; it is now a question (item 1), not an output.

## 4. The "never written to" rule

s24 is not one of the eleven keys FEEDBACK names, and a search for "never written", "written to", "write back", "writeback", "never touch", "read-only" and "one way" finds no claim in those words. The claim is there in another form: "Nothing touches the books." It is the seller's sentence (rec-4409 04:22), answering the office manager's "And the accounting package? Does it touch that?" (04:17) and welcomed with "Good." (04:28). A welcome of our sentence is not a client no-write rule, which is the s14 reading. Four occurrences reworded, each keeping the scope fact (invoicing is out of the agreed five items, which is the client's) and replacing the write claim with the rule's wording, writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the books is our safe default, labelled as ours:

- `company.current_tools[8]` (the accounting package): "Stays: 'Nothing touches the books.'" reworded, with the question, the seller's line and the "Good." cited at their locations.
- `integrations_mentioned[3]`: "invoicing stays there and nothing touches the books, on the office manager's question and the seller's answer" reworded.
- `requested_changes[8]` (the `remove`): description reworded for both systems; quote changed to the owner's own words at rec-4418 05:15 (pattern 4 above).
- `traps`, the quoting-and-invoicing entry: "excluded by the client on two calls" with three quotes, two of them the seller's, now attributes each line to its speaker (the owner's exclusion; the seller's scope read-back answered "Yes. That's it. Those five."; the seller's no-touch line welcomed by "Good.") and carries the rule's wording.

Checked and left: the estimating system, where the key already holds the direction open ("a second step", "shape held open", the export a claim); the `expected_structures.notes` line "quoting and invoicing stay where they are", which is scope, not a write claim; the rubric's R12 note, which is v2 material. The block's `existing.incumbents` entries for the estimating system and the accounting package use the rule's wording from the start.

## 5. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites four times and is written into the block: Approved set by the designer is his claim and the customer's email is the evidence (element P1.3, leaning 10); a pulled permit is the install lead's claim and the city's permit is the evidence (element P3.2); the material status is a person's claim about the stockroom (element P4.1, assumption 7); the done-to-invoice hand-off is the account manager telling the office manager, so a notification off Installed, not a status that means the books changed (question 4, assumption 12). No existing field claimed otherwise, so none was corrected.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked; does not bite in the fields. All thirteen `commitments_and_next_steps` carry owner, purpose and a date or "not set", the two "Done" demos and the spreadsheet are evidenced inside the package (the recordings; "that's what this was built from" and "You can tell."), and everything owed after 19 August says "unknown whether done". The block repeats the state in a verdict condition: the reprint-code pull, the loaded rate, the proposal and the floor hour were committed to the previous seller with no evidence any happened, and the user's own first meeting is unbooked. No `status` field was added to the commitments array, since that would change the s1 to s10 shape for one key.
- **s11 (inference targets questions; it never fills evidence).** Three unconfirmed client ties are in `signals` (the inbox-gone tie built on the no-login claim, the reprints-gone tie conditional on the lock, the floor-view tie conditional on by-piece rows) and drive the three read-back questions; none is cited as evidence or credited to an element. Two entities whose shape is unstated (the schedule's contents, the rebrand's job numbering) carry `moves_independently: unknown`.
- **s15 (a product limit never deletes a client need).** Six needs stay in `unmet_needs` with their clocks where the client gave one: the no-login approval and the two approvals (the credit union's proofs from 14 September), the operator seeing only the approved file (the fourth designer in the fall), the estimating-system connection, the second building (spring, if it happens), and a wall screen without a paid seat. Each says why v0.1 does not meet it; none is dropped because a claim was doubted or a tier is unknown.

## 6. The mess pass

Four edits, all on the seller's side, inside existing turns, outside every protected span (checked against the verifier's `--spans` listing before editing), with no turn added, removed or renumbered; unit and line counts are unchanged in every file:

- rec-4397 01:14 (the sales engineer, the longest turn of that call): "Way two. A separate production board." → "Way two. A separate, um, a separate production board." (+3 words; 103 → 106). The quarantine's 'I open Valley, four pieces, each with its stage.' is untouched.
- rec-4402 05:27 (the sales engineer, the longest turn of that call): "So a job has pieces." → "So a job has, a job has pieces." (+3; 90 → 93). The seeded pieces list and "Printed, laminated, cut, QC, ready." are untouched.
- rec-4402 00:31 (the seller): "And installs run on a group text" → "And installs, installs run on a group text" (+1; 70 → 71), after the quoted span.
- rec-4409 02:46 (the seller's scope read-back, the longest turn of that call): "Three, installs by crew" → "Three, um, installs by crew" (+1; 108 → 109), between the two protected spans.

Kept to eight words on purpose: the transcripts already carried an automatic export's mess from the adversarial review, and more words on the sales engineer in rec-4397 would have moved his stated share from 36% to 37%. `transcript_format` now reads about 1,590 words for rec-4402 and the three longest turns at their new lengths; every share stated in the key and in `talk_share` still rounds as written (recomputed in the build script with assertions). The README's "about 7,900 spoken words" holds (7,932). Documents, images and chat files do not exist in this fixture; the internal review and the discovery transcript were not edited.

## 7. The readiness block

Built in the brief's exact shape, from the key's own content, with every quote proven verbatim at its unit by the build script before writing (104 proofs) and then by the shared verifier.

- `pains`: the key's nine entries in array order, same quotes and locations, numbered P1.1 to P1.3, P2.1, P2.2, P3.1, P3.2, P4.1 and P5.1 (one id per key entry, theme number first, the exemplar's rule; P4 and P5 take `.1` for consistency). Stated or excavated follows the README (P1 to P3 excavated; P2.2 was volunteered on the demo and is `stated`; P4 and P5 stated). Outcomes are the client's words where they aim at the pain (rec-4418 27:43 for P1.1; rec-4402 11:17 for P2.1 and P2.2; rec-4418 28:13 for P3.1; rec-4397 06:49 for P3.2; rec-4397 10:38 for P4.1) and null for P1.2, P1.3 and P5.1, where no outcome words aim at them.
- `signals`: three (section 5).
- `entities`: 26, answering what moves independently of what. Sixteen carry a parent and all carry `moves_independently`; the crew, the station and the material are shared resources; the proof, the approved file, the art files, the ticket, the whiteboard entry, the schedule, the account manager's spreadsheet, the group text and the material go stale.
- `structure`: Work Management; `own-account` ("prospect, so the user's own account by default (A21)": the client has no account, the demos ran in the previous seller's demo workspace, and nothing has been bought); one workspace, "Penhallow – Ops"; native reuse none; ten leanings; three patterns (job and pieces; job and installs; a rebrand row with branch jobs, conditional on leaning 6); nine `element_per_pain` rows, six `fixes` and three `copies-today's-tool` (P1.2, P2.1, P2.2), none `none`.
- `existing`: "unknown, no account bound", with the A21 point that the proof of concept goes into the user's own account and the account question moves to handover; nine incumbents with what each stays the record for.
- `assumptions`: sixteen, each with the question that would replace it; the eleven pool questions that are not among the five live here (the reprint count, the loaded rate, the account and tier, the co-owner, what happened after 19 August, the second shop, the estimating system, the two approvals' mechanics, the floor screen's seat).
- `unmet_needs`: six (section 5).
- `ai_opportunities`: four, all round 2 (the client never asked for AI or workflows; the owner's "We'll put that in the rule." refers to a rule the sales engineer showed). The two workflows cite P-21, the agent P-19, the AI column is `unprobed`. No credit figure, price or package anywhere.
- `verdict`: `build`. Eight conditions, starting with the approval stop and the A11 point (none bites for an own-account target; the three A11 decisions stay open), then the workspace, the pieces element held unbuilt until the production manager confirms, seed data clear of the customer's branches and people, nothing tier-dependent promised, the s21 state of the previous seller's commitments, and the automations as one list.
- `questions`: five, the ceiling, in build terms. Three read-backs (the production manager's own words on the fork, on the lock, on the inbox) and two discovery questions (the done-to-invoice hand-off; one job number per branch or per rebrand). Each says what is known. Dropped from the five under A21 and the brief's rule: which account and tier (the proof of concept goes into the user's own account), the reprint count and the loaded rate (no build element depends on them), the co-owner and the post-19-August questions (the verdict carries them as conditions; they are the user's first to-dos, not build questions), the second shop (a seed).

The key's `should_plugin_propose_a_build: true` and its "Nearly ready" verdict agree with the block, so the `note` needs no second sentence. No R-number, grade, gate name, verdict word, "bleed" or "upside" appears in the block (asserted by the script).

## 8. The README

Brought in line: the key's line count (556) and the `readiness` block in the files table; the fork row carries the leaning and its condition; the counts section reads traps 30, pre-build questions 12, quotes 274 structured and 296 prose spans by the fixture's own check script with the shared verifier's 313 pairs explained, a new Readiness bullet with the block's counts, the intake bullet with 16 alias entries and the fork's leaning; the conventions section names `direction` and the mess-pass additions; the review-status paragraph records the user's review of 2026-10-10 and the fix pass in one "fix pass applied 2026-10-13: ..." sentence. The transcript totals (1,038 lines, about 7,900 words) hold.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (3 read-back, 2 discovery) |
| pains | 9 |
| signals | 3 |
| entities | 26 (16 with a parent, all with `moves_independently`) |
| leanings | 10 (1 fork, 9 sweep hits) |
| element_per_pain | 9 (6 fixes, 3 copies-today's-tool, 0 none) |
| incumbents | 9 |
| assumptions | 16 |
| unmet needs | 6 |
| AI opportunities | 4 |
| existing fields corrected or extended | 17 (listed in sections 1, 3 and 4) |
| traps | 30, from 29 |
| pre-build questions | 12, from 11 |
| alias-map entries | 16, from 13 |
| transcript edits | 4 turns, +8 words; units unchanged (173, 91, 34, 77, 63) |
| key size | 556 lines, from 397; 27 top-level fields |

Also run after the edits: the fixture's own read-only `fixtures-work/_work-s24/check.py`, which reports field order ok, 274 structured quotes, 296 inline prose spans (25 cited), bad 0.

## 10. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s24-package`, run after all edits, exit code 0:

```
Fixture: s24-package
Sources: rec-4397-production-walkthrough.txt (transcript/header-dot, 77 units); rec-4402-first-look.txt (transcript/header-dot, 91 units); rec-4409-pricing.txt (transcript/header-dot, 63 units); rec-4418-discovery.txt (transcript/header-dot, 173 units); rec-4431-internal-review.txt (transcript/header-dot, 34 units)

pairs found      313
verified         313  (of which presence only, no location cited: 37)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes: no unit was added or renumbered, so every citation's index still points at the unit with the same stamp.
