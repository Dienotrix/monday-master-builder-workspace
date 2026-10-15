# s13-header-absent — fix pass changes

Editor's log, 2026-10-13. Everything in the fixture is fictional and stays fictional.

Files touched: `fixtures/s13-header-absent/answer-key.json`, `transcript.txt` (one unit, the mess pass) and `README.md`. Method: the key was loaded and dumped by a layout-preserving serializer that reads from the file which containers are expanded and which are printed on one line, because the s13 key keeps every list entry on one line and a plain `json.dump` would have rewritten all of it. A round trip of the untouched file reproduced it byte for byte before any change. The 25 fields keep their order, `intake` stays 26th and `readiness` is the 27th and last. Every quote the block introduces was copied from the transcript and proven verbatim at its cited unit inside the edit script before the file was written (37 proofs, including the ten `outcome` strings, which the shared verifier does not check because the field name carries no "quote"). The shared verifier then ran clean at 195 pairs. The key went from 349 to 511 lines, ASCII before and UTF-8 now (the two en dashes in the workspace names).

The authority order followed: the fixture's own FEEDBACK entry (lines 82 to 92) first, then the `direction` rename, the seven-pattern sweep, the "never written to" rule, the standing lines, the readiness block, the README and the coverage row.

## 1. The FEEDBACK entry, applied as recorded

**1. The finance manager's surname (wrong).** The key named him "Torsten Holmquist" and said the surname came from the user's invite, which the plugin never sees; the preamble (line 2) gives only "Torsten".
- `attendees[4].name`: "Torsten Holmquist" → "Torsten (finance manager; surname unknown)", the same shape as Leonor and Harriet. `attendees[4].role`: the sentence "The surname is not spoken; it is the name the user's invite carried." → "The surname is never spoken, and the preamble (line 2) names him by first name only; the invite itself is not an input, so the surname is a question to the user, who holds the invite, never a guess."
- `intake.roster.alias_map[4].canonical`: "Torsten (finance manager; surname from the user's invite: Holmquist)" → "Torsten (finance manager; surname unknown: never spoken; the preamble names him by first name only, so the surname is a question to the user, who holds the invite)". Forms unchanged.
- The same gap sat in two more fields, which the review's seventh sweep pattern names for s13 ("an expected output the input cannot support (s13 surname)"): `traps[7]` no longer says the key "carries the surname the invite supplied"; it now says the surname is as unknown as the other two, that the user is asked for it, and that taking one from anywhere but the input or inventing one is wrong. `accepted_behaviours[4]` no longer offers "from the user's invite ... or leaving it unknown; both are correct"; it accepts only first name and role with the surname unknown, plus the question to the user.
- The question to the user: `expected_questions_before_building` gains a twelfth item asking the user for the surname, saying the record carries "Torsten (finance manager; surname unknown)" until then. It is not one of the five readiness questions, because no build element changes with its answer and the five go to the client; it lives in the key's own pool and in the alias map's wording.
- README: the "Conventions" paragraph on surnames rewritten (section 7 below).

**2. "The accounting system is never written to" (too strong).** Three occurrences, each replaced with the client-side state the review gives, and our default labelled as ours.
- `expected_monday_products[0].why`: "...stays the source of the project number; the accounting system is never written to." → "...stays the source of the project number. The accounting system's integration and write behaviour are unresolved, pending the finance manager (31:16, 37:45); v0.1 does not depend on either, and the first version staying clear of the accounting system is our own safe default, labelled as ours."
- `integrations_mentioned[1]`: "never written to; the finance manager's question, on the list" → "integration and write behaviour unresolved, pending the finance manager ('That's a Torsten question. Put it on the list.'); v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours".
- `expected_structures.notes`: "the accounting system never written to; interpreting out." → "the accounting system's integration and write behaviour unresolved, pending the finance manager, with the first version staying clear of it as our own safe default; interpreting out."
- The key's open question on the accounting system (`expected_questions_before_building[3]`) already had the right shape and stands. The block's `existing.incumbents` entry for the accounting system and leaning 4 use the same wording.

**3. Status words (wording).** Nobody said the tool's words win; the client asked for one shared vocabulary.
- `requested_changes[1].description`: "one status, one word per step, identical to the translation tool's step names, so nothing says 'delivered' in one place and 'sent' in another" → "a shared status vocabulary, one word per step that means the same thing to every person and in every place; confirm the exact labels with the client, so nothing says 'delivered' in one place and 'sent' in another." The quote ("Whatever the word is, it's the same word.") stands.
- `expected_questions_before_building[2]`: "the exact step names in the translation tool, in order, so the one status uses the same words" → "agree the one set of words with the client, and find out whether the translation tool's statuses can be renamed to them or have to be mapped, which is the decision underneath."
- The same requirement was hard-coded in two build fields a builder would read first, so both were corrected: `expected_monday_products[0].why` "one status whose words match the translation tool's steps" → "one status with a shared vocabulary across people and systems, exact labels to confirm"; `expected_structures.notes` "one status matching the tool's steps" → "one status with a shared vocabulary and labels to confirm". Leaning 6 carries the question. The rubric R12 note still says "one status with one word per step"; it sits in `rubric`, which the brief keeps untouched as v2 material, and is noted for the v2 pass.

## 2. The `direction` rename

`intake.type_header.direction_of_show` → `direction`, value "no-show" unchanged, position in the object unchanged. One occurrence; the key has no `files[]` package header. The README does not name the field, so no prose followed. `direction_of_show` is absent from the key.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry; a field was corrected only where a builder reading it alone would have built the flaw.

1. **One row where the call describes many.** One hit. A project with twelve languages sat "in review for six days, waiting on one language" (18:17) while the other eleven were done, and the German manual was split across three translators (13:32); one project item with one status, one assignee and one due date carries one value for many languages. `vocabulary["project"].likely_monday_object` read "item on a Projects board", so it was corrected to the parent item with one child row per language (or per assignment), status and due date rolled up. `expected_monday_products[0].why` "a project as one item" → "one parent item ... with a child row per language where the languages move apart". Leaning 1; conditions: the senior PM's columns (due before the nineteenth) and the tool's step model (the API answer). Considered and declined: quotes (the retailer's "a listing at a time" is one quote per listing already) and freelancers' bookings (pattern 5, below).
2. **A pain with no element that fixes it.** Two hits, both kept visible. The minor pain, freelancer invoices matched by hand to emailed purchase orders (22:36), has no element in v0.1: `none` in `element_per_pain` P6.1, leaning 7, and an `unmet_needs` entry. P3 (invoicing waits for an email) has an element, the delivered status feeding a delivered-not-invoiced view, but in v0.1 that status is the PM's claim and depends on the PM remembering, exactly as the email does ("When I remember.", 20:26), so P3.1 and P3.2 are `copies-today's-tool` until the tool's own delivered step can be read; leaning 3 and question 3 carry the dependency, by the exemplar's second lesson.
3. **An alias-map entry that names more than one entity.** No hit. The eight alias-map entries each name one person. Nearest candidates: the vocabulary rows "job" (two senses, already kept apart by the key) and "the framework" (the medical device contract and the state agency tender), which names two contracts under one term but says so and is a term, not an alias; declined.
4. **Our framing labelled as the client's.** Two hits. The status requirement "identical to the translation tool's step names" traces to the Consultant's "same in both places" at 36:53, not to the client (FEEDBACK item 3; leaning 6). The delivered-not-invoiced list and the managing director's screen come from our play-back at 35:11, accepted as "the right shape. To show us." (36:03); the screen rests on the operations director's own "the Friday answer to come off a screen" (29:10), the finance list on nothing the finance manager said, because he never spoke. `expected_monday_products[0].why` now labels both as ours until the finance manager has been heard; leaning 5. Checked and left: the go-ahead gate (36:16, the client's), email-only outreach (36:58, the client's), interpreting out (37:19, the client's), the phone requirement (42:17, the client's).
5. **A shared resource with no reservation tracking.** One hit, the central pain. Freelancers are booked across projects by five PMs and the vendor manager, and the only reservation today is a "busy until" column updated "which is never" (15:40). `vocabulary["the pool ..."].likely_monday_object` read "a Linguists board ... with language pair, subject and availability", which is the "busy until" column again, so it was corrected to availability derived from booking rows with dates, never a hand-set value; `expected_monday_products[0].why` says the same. Leaning 2; conditions: whether PMs who book direct will create the row, and what "free" means (question 4). The three in-house reviewers (the Japanese reviewer booked twice in one day, 15:56) and the one layout person are the same shape and carry `shared_resource: true` in `entities`.
6. **An artefact that can go stale with nothing to flag it.** Two hits. The delivered-not-invoiced view depends on an "invoiced" state that only the finance manager can set, by hand, from an accounting system v0.1 never reads; nothing flags a row he has billed and not ticked. Leaning 4: an invoiced-on date with setter and as-of, every row labelled unconfirmed against the accounting system. The quote log's status "mostly sent" because "nobody updates it" (08:29): a Quotes board with a status column alone is the log again. `expected_monday_products[1].why` now adds a sent date and an ageing flag; leaning 8. Declined: the project number copied across once (the tool stays its source and no renumbering is described).
7. **An expected output the input cannot support.** One hit, the surname (section 1, item 1; `traps[7]` and `accepted_behaviours[4]` corrected). The transcript statistics the key asserts were recounted from the file (240 units, 5,796 words, 74.8 percent, 190 words at 02:29 over 72 seconds, 121 at 35:11, 24 short units, two without terminal punctuation, zero same-label pairs, 61/35/30/18 turns) and were all true before the mess pass; the ones the mess pass moves were rewritten from the recount (section 8). The date is already held as a fit, not a fact.

## 4. The "never written to" rule

s13 is one of the eleven keys FEEDBACK names, and its three occurrences are the FEEDBACK item above (section 1, item 2). A search for "written to", "write back", "writeback", "never touch", "one-way" and "read-only" found one more of the weaker form: `vocabulary["the tool / the translation tool"].likely_monday_object` read "a one-way read if its API works", which rests on our question at 38:01, not on a client line. Now: "whether its project list and step statuses can be read is the senior PM's question to the vendor, and the direction of any connection is unresolved; v0.1 copies the project number across once". Checked and left: "read-only" for the medical device portal (Devika, 38:45: "You can't do anything with it except look and download.", a client quote); "even read-only" in the linguist-access trap (about board access, not a system); "is a one-way read acceptable" in `expected_questions_before_building[1]`, which is a question and the right shape.

## 5. Standing lines, where they bite

- **s21 (a commitment is `committed`, done only on evidence).** Bites on the walkthrough. `commitments_and_next_steps[0].what` read as if the managing director and the finance manager were attending; on the call the Consultant will send the invite this afternoon and the operations director will "add Harriet and Torsten" (40:44), with the finance manager "if he can get in the room by then" (40:12). Now: "Committed on the call: ... the operations director will add the managing director and the finance manager to the invite, so their attendance is her commitment, not confirmed. Nothing is sent or confirmed yet." The owner line says the same. The verdict's conditions repeat it. The rubric R10 note and `expected_verdict.gates_met` ("the audience on the nineteenth includes the approver and the finance manager") say the stronger thing; both are v2 fields the brief keeps untouched, noted for the planner. No `status` sub-field was added to the commitments array, so the shared shape stands.
- **s22 (a board status set by a person is a claim).** Bites on delivered, invoiced and review. Leanings 3 and 4 and `element_per_pain` P3.1, P3.2 say the delivered and invoiced statuses are claims until the tool's delivered step can be read and the finance manager has said how he wants to be told; P2.2 and P5.1 say the review status is the reviewer's own record and the tool's review step stays the evidence; verdict condition 5 says it once for the block.
- **s11 (inference targets questions, never fills evidence).** Seven unconfirmed client ties are in `signals` (the relayed ten-day lag, the finance manager's veto as relayed, the export, the "two days of Torsten", the managing director's relayed win condition and what she will look for, the vendor's API claim). Two of the five questions are read-backs of them; none appears as evidence or in an element, and the delivered-not-invoiced list carries `source: assumed` with no evidence location in `entities`.
- **s15 (a product limit never deletes a client need).** Six `unmet_needs`: the invoice matching (P6.1), sign-in through the company's email accounts and the data-location answer (cannot be shown in the user's own account), freelancer replies reaching the board without a login (email in needs an integration v0.1 does not set up), a read of the tool's project list and statuses, the dead quotes (second in the client's order), and the relayed split count. Each keeps its clock where the client gave one.

## 6. The readiness block

Built in the brief's exact shape. Counts: pains 10 (one id per key entry, P1.1 to P1.3, P2.1 to P2.2, P3.1 to P3.2, P4.1, P5.1, and the unnumbered minor pain as P6.1, by the exemplar's rule), signals 7, entities 29 (17 with a parent; every entry carries `moves_independently`), leanings 8, patterns 2, element_per_pain 10 (7 `fixes`, 2 `copies-today's-tool`, 1 `none`), incumbents 9, assumptions 14, unmet_needs 6, ai_opportunities 5 (all round 2: nobody asked for AI or workflows on the call; the two workflows cite P-21, the two agents P-19, the AI column is unprobed), questions 5 (2 read-backs, 3 discovery), verdict `build`.

- `pains`: `stated_or_excavated` follows the key (P1 and P2 excavated, the rest stated). `outcome` is verbatim from the client where words aim at the pain: Rafael's "I want to see who's free. Before I email them." (29:50) for P1, the operations director's two sentences at 29:10 for P2, Niamh's one-status line (29:35) for P3.1, Devika's "I want to know which quotes are dead." (30:02) for P4.1; null for P3.2, P5.1 and P6.1, where no outcome words exist.
- `structure`: Work Management and CRM; `own-account` because the firm is a prospect with no monday account (A21); workspaces "Corvane – Ops" and "Corvane – CRM"; native reuse the Deals/Opportunities board relabelled Quotes and the Accounts board after the first version, Contacts only if asked, detected in the bound account before quotes are mapped.
- `existing.account`: "unknown, no account bound", with the A21 point that the proof of concept goes into the user's own account and the client's eventual account is a handover question, not one of the five. Nine incumbents with what each stays the record for; the accounting system in the FEEDBACK wording.
- `verdict`: `build`. Six conditions, the approval stop first; no A11 question first matters for an own-account build and the three A11 decisions stay open. The reason sentence names the test and the honest limit: two elements are copies of today's tool until the translation tool can be read.
- `questions`: five, the ceiling. Q1 read-back to the finance manager through the operations director (the accounting system and how he wants to be told). Q2 the status vocabulary, in the FEEDBACK's two parts (agree the words; rename or map), to the senior PM with the vendor. Q3 the tool's API, to the same. Q4 bookings and what "free" means, to the vendor manager with the PMs. Q5 read-back to the managing director through the operations director (her relayed win condition, what she will look for, whether she will be on the nineteenth). Reused from the key's pool: items 2, 3, 4, 5 and 11. Dropped from the five and held as assumptions with their questions: client-name visibility (item 6), review evidence (item 7), the framework's shape (item 8), the columns (item 9), the seed (item 10), and contacts; item 1, which monday account, is not one of the five for a prospect (A21); item 12, the surname, goes to the user and not to the client.
- No R-number, grade, gate name or verdict word is in the block (the script searched before writing); `rubric`, `expected_verdict` and `numbers` are untouched. The key's `should_plugin_propose_a_build` is `true` and the block says `build`, so the two agree and the note needs no extra sentence.

## 7. README

`README.md` brought in line: the transcript row notes the mess pass and the client share 74.6 percent; the key row names the `readiness` block and 511 lines; pre-build questions 12; quotes 195 checked strings, 167 with a location; a new counts bullet for the readiness block; the surname paragraph rewritten to the FEEDBACK reading; the line-budget convention updated; a new convention line on the v1 block versus the v2 fields, the accounting-system wording and the status wording; the review status now records the user's review of 2026-10-11 and the merge step; and one sentence beginning "Fix pass applied 2026-10-13:" at the end.

## 8. Transcript: the mess pass

The s11 rule, applied with judgment. The Consultant's turns in s13 already carry false starts (06:54, 22:26, 38:18) and hedges (34:47); the one writer-clean paragraph on our side is the play-back at 35:11 (121 words, no quoted span in it, confirmed with `--spans`). Edits inside that unit only: "Okay. So --" at the start, "one status, one status that everyone uses", "sits beside it, next to it,", "that doesn't move," and "And nothing for the interpreting team". Twelve words added; the unit count (240), the numbering, the stamps and every other line are unchanged; the unit stays the third-longest in the file (133 words, under the 142 at 03:58), so the long-unit order the detectors cite holds. Recounted and rewritten from the file: `intake.export_family.words` 5,796 → 5,808; `transcript_format` client share 74.8 → 74.6 percent (Wilhelmina 37, Niamh 18, Rafael 12, Devika 7) and the Consultant's longest turn 121 → 133 words; `intake.detectors.composite_splitter` "35:11 at 121" → 133 and the words-per-minute triple 158, 167, 140 → 158, 167, 153 (still inside the plausible band, so the splitter's finding stands); `intake.delivery_notes[0]` the same two figures. The 41:17 refusal and the 01:39 agenda were left: both hold protected spans and neither is a clean paragraph in the sense the rule means.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 10 |
| signals | 7 |
| entities | 29 (17 with a parent) |
| leanings | 8 |
| element_per_pain | 10 (7 fixes, 2 copies-today's-tool, 1 none) |
| incumbents | 9 |
| assumptions | 14 |
| unmet needs | 6 |
| AI opportunities | 5 (all round 2) |
| existing fields corrected | 22 fields outside the block (27 substitutions, counting each one; sections 1 to 5 and 8), including the renamed `direction` field and the added twelfth pre-build question |
| expected_questions_before_building | 12 (from 11) |
| transcript edits | 1 unit (35:11), 12 words added, 240 units unchanged |
| key size | 511 lines (from 349), 27 top-level fields |

## 10. For the planner

- `rubric[9]` (R10) and `expected_verdict.gates_met[2]` still say the approver and the finance manager are in the audience on the nineteenth; `rubric[11]` (R12) still says "one word per step". All three are v2 fields the brief keeps untouched; the s21 state and the FEEDBACK wording are in the v1 fields and the block.
- The key is over the stage-1 400-line budget because of the block; the README says so.

## 11. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s13-header-absent`, run after the last edit to the key or the transcript (the README edits came after and touch no quote), exit code 0:

```
Fixture: s13-header-absent
Sources: transcript.txt (transcript/header-time-last, 240 units)

pairs found      195
verified         195  (of which presence only, no location cited: 28)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes: the file's grammar is stamp plus label, no unit was renumbered, and every citation resolved at its unit.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | The first framework project goes into something that isn't a spreadsheet, before January | 25:48 Wilhelmina Strachan | P2.1, P2.2 |
| G2 | A project is one thing, in one place, from quote to invoice | 29:10 Wilhelmina Strachan | P2.1, P2.2, P3.1, P5.1 |
| G3 | One status: one word that means the same thing to everyone | 29:35 Niamh Kettleborough | P2.2, P3.1 |
| G4 | See which freelancers are free before emailing them, and the PMs see it too | 29:50 Rafael Quintanilla | P1.1, P1.2, P1.3 |

Assumption kinds: gap 6, leaning 5, board-architecture 2, automation-condition 1.

Verifier: 195 pairs, 195 verified, 0 misses and 0 near-misses before; 199 pairs, 199 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G2 to G4 are the "sitting here in March" answers the key also uses as pain outcomes, kept because each is said as "I want" and G2 and G4 span whole pain groups, while G3 (one status) is the narrowest and could be folded into G2 if four is too many; the operations director's "Friday answer off a screen" and the account manager's dead quotes were left out as single-pain outcomes, and the managing director's credits wish was left out because the operations director says she is guessing it.
