# s23-symmetric-shred — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s23-symmetric-shred/answer-key.json` and `fixtures/s23-symmetric-shred/README.md`. `transcript.txt` is unchanged (264 units; the reason is in section 7). The key was loaded, changed and dumped by a small serializer (`keyfmt.py` in this folder) that reproduces the file's own layout: dicts pretty at two spaces, list elements one per line and compact, dicts two levels down inside `intake` compact. A round trip of the untouched file reproduced it byte for byte before any change, and the raw diff afterwards touches only the lines named below plus the appended block. The 25 fields keep their order, `intake` stays 26th, and `readiness` is the 27th and last. The key grew from 349 to 496 lines. The edit script is `apply.py` in this folder; it proved every new quote at its cited line before writing, and the shared verifier then ran clean.

## 1. The review entry (FEEDBACK.md, s23, 2026-10-13), applied as recorded

**Item 1: the true talk share is author-only data.** The entry names key line 162 and the intake block at line 284; both matched the file before editing.
- `traps[1]` (line 162) now reads: the by-label figure is a label count, not a measurement; report it with a warning that shredding likely understates it, never a corrected figure; the true share is fixture ground truth from the generation plan that no grader expects as output. The last sentence, on not ranking speakers by label counts, stays.
- `intake.shred` gains `talk_share_true_note` directly after `talk_share_true_by_words`, saying the figures are fixture ground truth, not derivable from the transcript and not expected from any grader, and that the graded output is the by-label figure with the warning. `quietest_speaker` leads with the by-label figure and the warning, and marks the 9.1 percent and 618 words as the generation plan's.
- The same reading was carried everywhere the key spoke of "her figure with its error" or "in truth": `purpose_of_this_fixture` (two phrases), `transcript_format` (the "in truth" clause marked as ground truth no grader expects), `attendees[4].role`, `accepted_behaviours[3]` ("a label count that shredding likely understates, gives no corrected figure"), and `intake.confidence.propagation`. The accepted behaviour itself, 6.1 to 6.7 percent by label with the warning, is unchanged, which is what the entry says is right.
- README: the defect table's second repair, the Measurements paragraph and the Checks-run paragraph now say the true share is the generator's and that the adversarial re-derivation was an authoring check, not something a plugin is expected to produce.

**Item 2: the pack checklist checks presence, not version.** Key line 31 matched. `expected_monday_products[0].why` now says each pack document is a child row of the job carrying its state (draft, issued, signed, approved); the checklist verifies that the current issued or approved version is in the pack rather than that a document exists; a pack built before a document's final version arrived shows as outdated, as does one built before the object list changed. The same correction in `vocabulary["pack, job pack"].likely_monday_object`, `expected_structures.notes` and `expected_structures.lookalike_traps[6]`. A builder reading any of those fields alone would have built the spreadsheet's tick, which is the flaw that failed at the port, so the fields are corrected and leaning 1 carries the shape and its condition.

**Item 3: crate assignment needs availability tracking.** Key line 31 matched. `expected_monday_products[0].why` now says the crate schedule is a three-week view over a Crates board keyed on Margit's numbers where each crate carries its state, its location and which job holds it for which dates, so a crate is never promised twice and an available one is not rebuilt. The same in `vocabulary["crate, travel frame"].likely_monday_object` (state, location, holdings as child rows), `expected_structures.notes` and `lookalike_traps[4]`. The crate number stays Margit's and nothing is renumbered, as the entry asks. Leaning 2 carries the shape.

No new look-alike trap was added for either item, so the trap counts the coverage row tracks do not move; the corrected traps say the right thing.

## 2. The direction rename

`intake.type_header.direction_of_show` is now `direction`, in the same position with the same value (`no-show`). The key has no package files, so there was only the one occurrence; `direction_of_show` no longer appears in the key. The README did not name the field; its Counts paragraph now says the field was renamed, so a reader of the README and the key sees the same name.

## 3. The seven-pattern sweep

**One row where the call describes many.** Two hits.
- The pack. Eamon's checklist is "one row per job, with a tick for each document" (the sentence is a refused quote, crossing L134 to L135; L135's second sentence and L137 carry it whole), and the documents move independently: the licence went from draft to issued at six the night before (L126), the agreement was unsigned twice (L131), the packing list and the forms go wrong when the museum changes the object list (L135). One row with ticks is one value for many. Leaning 1: parent-row-with-roll-up, documents as child rows with state, pack status on the job. This is the same hit as pattern 6 and FEEDBACK item 2, and the fields were corrected under section 1.
- The object. The inventory system has one object line per job (L54), the museum's question is about an object across jobs (L84), and the same object is two strings on two jobs (L223). Leaning 4 keeps one object row per job line for the first version, with the two identifiers as columns, and names the condition under which the object becomes the parent with its job appearances as children: a clean, consistent reference from the ten-object sample. No field corrected: `vocabulary["object"]` ("item on an Objects board connected to its job") is incomplete, not wrong, since the lookup by reference across job lines still answers the question once the reference is clean.

**A pain with no element that fixes it.** One hit, one considered.
- Pain 5 (the crew grid redone every Monday, L74): nothing in the build touches Marek's calendar or his printed grid, nobody asked, and the look-alike list warns against a crew grid board. `none` in `element_per_pain`, leaning 7, and an entry in `unmet_needs`.
- Pain 6 (the inventory system's three states, L64): considered as a no-element pain and not recorded as one. The key itself calls it a cause behind P1 and P3, and the monday job's own stages between booked and out are the element aimed at it; the inventory system's states are untouched, and the row says so.

**An alias-map entry that names more than one entity.** No hit. The four entries (the founder, the person in finance, the crew chief, the consortium) each resolve to one person or one body. The nearest candidate is "the consortium", which resolves to seven museums; it is one tendering body whose members are unnamed, and the key invents no organisation for it, so it stands. In `vocabulary`, "the store, Ravensdale" names two places, but as two values of one location column, which is the right shape; nothing split.

**Our framing labelled as the client's.** One hit. `attendees[2].decision_role` said Margit "will enter the book once", and `vocabulary["the book"]` said "entered once by Margit". Entering the book once at a desk is Thandiwe's proposal (L232, L234); Margit's own words are "no typing in the shop" (L201) and "I'm not renumbering four hundred crates for a computer" (L238), and she never answered the proposal. Both fields corrected to say whose proposal it is; leaning 6 labels it as ours until she says so, and question 3 reads it back to her. Checked and left: the three-week horizon (Margit's, L72), "one tap" (Margit's, L220), the five pieces at L246 (the key already calls it our playback and grades the assent as swallowed), the order reports, packs, crates (L216 to L218, the client's), and the five feed questions (labelled as Thandiwe's throughout).

**A shared resource with no reservation tracking.** One hit: crates, FEEDBACK item 3, leaning 2, with holdings (job, from, to) as child rows of the crate. Considered and declined: vans and handlers are booked across jobs too, but by Marek in a shared calendar and a printed grid that nobody asked to replace; recorded as a need the build does not meet rather than forced into a leaning.

**An artefact that can go stale with nothing to flag it.** Three hits.
- The pack (FEEDBACK item 2): leaning 1, fields corrected as above.
- The condition photographs and the job folder on the drive. Photographs reach the drive late or never (L88, L80), and the only flag today is Eamon's Friday chase list (L120). Leaning 3: the report item holds the photographs from the phone, and a view of outgoing reports with no photograph replaces the chase list. No field corrected: `vocabulary["condition report (outgoing, incoming)"]` already has photo uploads on the item.
- Rows read from the inventory system. A job confirmed after the nightly file ran (L253) is not on the board until the next read, and nothing in the key said a row shows when it was last read. Leaning 5: an as-of time and a source on every fed row; in v0.1 every row is a sample value and the board says so. No field corrected; the feed entry in `integrations_mentioned` is incomplete, not wrong.

**An expected output the input cannot support.** Two hits, both field corrections and neither a structural leaning, because neither is a structure question; there is no restructure to make visible, and forcing a leaning would be our framing.
- The true talk share: FEEDBACK item 1, section 1 above.
- `company.name` read "Aldergate Fine Art Services (called 'Aldergate')". The transcript says "Aldergate" once (L15) and never the longer name; a grader comparing the name would expect words the input does not carry. Now "Aldergate (the only name spoken, L15; no longer trading name is said)". The README already calls the company Aldergate.
- Checked and left: the dates (labelled inferred from "nearly November" and the weekday); the transcript statistics in `transcript_format` and `intake.export_family`, recounted from the file and all true (264 units, 6,803 words, by-label words and shares, 70 lowercase-initial, 74 unterminated, 23 short, 3 adjacent same-label pairs, longest unit 168 words at L246, then L189 at 130 and L98 at 117); and the client share of 63.09 percent, which is the by-label figure and is derivable.

One factual slip found while checking the file, outside the patterns: `transcript_format` said "Currency is pounds, said once"; it is said twice (L129, L151). Corrected.

## 4. The "never written to" rule

s23 is one of the eleven keys FEEDBACK s14 names. A search for "never written", "written to", "write back", "writeback", "read only", "read-only", "never touch", "nothing goes into" and "goes back into" found four claims, and none traces to a client quote: the client says the system must not be replaced (L207), that values never leave it (L211), that invoicing keeps running from it and the person in finance wants that kept (L96, L97), and that nothing is typed twice (L170). "We never write anything back" is Thandiwe's sentence (L182), "Read only" is the Consultant's (L179), and "Nothing goes into the inventory system" is the Consultant's playback (L246). Each occurrence now reads "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of it is our safe default, labelled as ours", with the client-backed requirements kept beside it and their lines cited:
- `purpose_of_this_fixture`: "left as the book of record and read only" reworded.
- `expected_monday_products[0].why`: "stays the book of record, read only, with invoicing untouched" reworded; invoicing stays the client's requirement.
- `integrations_mentioned[0]`: "read only, never written to" reworded, with the four client requirements listed.
- `expected_structures.notes`: "the inventory system is never written to and invoicing is untouched" reworded.
- README line 16: "read from the inventory system and never writing to it" reworded the same way.

Checked and left: `current_tools[1]`, "the accounting system ... is never touched by hand", which describes today in Eamon's words (L96), not the build; `compliance_or_security_signals[0]`, where "never leaving the inventory system" is about the values and is Constance's (L211); and the `expected_questions_before_building` feed question, which is a question, the right shape. The readiness block's incumbent entry for the inventory system carries the same unresolved wording from the start.

## 5. Standing lines, where they bite

- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Two owners the call never gave were corrected. `commitments_and_next_steps[0]` listed the managing director among the attendees of the walkthrough; Constance said "If I ask him he'll come" (L209) and never said she would ask, so the entry now says he attends if she asks him, and her part of the owner line is to confirm the slot and decide whether she asks him. Entry 6 named Constance as the one to invite the crew chief; Margit asked for him (L257) and the Consultant noted it (L258), and nobody took the invitation, so the owner now says it is unassigned on the call. The walkthrough slot was already recorded as proposed and unconfirmed, the invite and recap as "tomorrow", and nothing as done, so the rest stands. No `status` field was added to the commitments array, for the reason the exemplars give: one decision for all twenty-five keys, not a shape change in one.
- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites three times and is written in: a pack document's state is set by Eamon when the email lands, and the email is the evidence (leaning 1's condition, assumption 2, the email incumbent); the monday job's stages between booked and out are people's claims and nothing here is evidence the inventory system changed (`element_per_pain` P6, incumbent 1); and the Crates board's state and location are what someone entered, which is why the one-time book entry matters (leaning 6). The condition report itself is captured in monday from the phone, so there the photograph is the event, not a claim about another system.
- **s11 (inference targets questions; it never fills evidence).** Six unconfirmed client ties sit in `signals` (the first cut accepted piece by piece, the conditional "one tap, maybe", the managing director's relayed win and relayed conditions, the slot and the crew chief's invitation, and the book entry Margit never answered). They drive the three read-back questions and appear in no element and no evidence. The three swallowed assents are never re-attributed: the signals quote the client units around them, not the tokens.
- **s15 (a product limit never deletes a client need).** Four needs the first version does not meet stay in `unmet_needs` with their clocks: the consortium's on-request access within twenty-four hours (February), the crew grid, loans in, and the vendor's feed answers.

## 6. The readiness block, field by field

- `pains`: the key's six entries in array order, same quotes and locations. P1 to P4 keep the key's numbers; the two unnumbered entries (the crew grid, the three states) become P5 and P6, the next free numbers, so each has its own `element_per_pain` row. P1 to P3 are excavated, as the key says; P4 to P6 stated. Outcomes are verbatim from L200 (Constance, for P1), L202 (Eamon, for P2) and L201 (Margit, for P3); P4 to P6 carry null because no outcome words aim at them.
- `signals`: six, each with the pain it bears on and what our side never confirmed.
- `entities`: thirty, answering what moves independently of what. Twenty have a parent and each carries `moves_independently`. The six pack documents are listed separately under the job pack because each arrives from its own source and changes version on its own, which is the whole of FEEDBACK item 2. The crate is a shared resource; the crate holding is `assumed` with no evidence, because nothing on the call describes how long a job holds a crate. The book, the whiteboard, the nightly file and every fed row go stale. The insurance value is listed so that it is visibly never built.
- `structure`: Work Management only; `own-account` because the client is a prospect with no account (A21); one workspace, "Aldergate – Ops", with the brief's en dash (the key was ASCII before and is UTF-8 now, which the brief allows); native reuse none, since no CRM or Service entity exists; seven leanings; three parent-row-with-roll-up patterns (job and pack documents, crate and holdings, job and objects); six `element_per_pain` rows: four `fixes`, one `copies-today's-tool`, one `none`.
- `existing`: "unknown, no account bound" with the A21 point, and eight incumbents with what each stays the record for.
- `assumptions`: thirteen, each with the question that would replace it; the questions that did not make the five live here.
- `unmet_needs`: four.
- `ai_opportunities`: five, all round 2, because nobody on the client side asked for AI or workflows. Three workflows cite P-21 and the agent cites P-19, the probe findings the design names for those kinds; the AI column is `unprobed`.
- `verdict`: `build`. Three pains have entities and a wanted outcome in the client's own words, the product is chosen, the structure is stated with its leanings, the target is named. Eight conditions, starting with the approval stop and the A11 point (none bites for an own-account target; the three decisions stay open), then the workspace, sample rows only, the unagreed first cut, the unconfirmed slot, the feed as a question, and the December window with the glove test.
- `questions`: five, the ceiling. Q1 reads the first cut back to Constance (pool item 10's first-cut re-ask, in build terms); Q2 asks Eamon for the document states (new, from FEEDBACK item 2); Q3 reads Margit's own words back against our book-entry proposal and asks how long a job holds a crate (pool item 6 plus FEEDBACK item 3); Q4 reads the reference field back from the sample (pool item 3); Q5 asks which feed mechanism the first version runs on (pool item 2). Dropped from the pool and kept as assumptions: the account question (item 1; under A21 not one of the five for a prospect), the photo size test (item 4; already a commitment), the value's confidentiality (item 5; assumption 12), who may see a report (item 7; assumption 7), the December days (item 8; assumption 13), sample data (item 9; assumption 6), and the total and the slot (item 10; v2 material and the recap respectively).

The key's `should_plugin_propose_a_build: true` and its own verdict leave the blueprint gate open, so the block's `build` does not disagree with them and the `note` carries no extra sentence. `rubric`, `expected_verdict` and `numbers` are untouched. The script searched the block for R-numbers, grades, gate names, verdict words, "bleed", "upside" and "rubric" before writing and found none; the one use of "excavated" is the schema's own `stated_or_excavated` value.

### Two judgment calls worth recording

1. **P4 is `copies-today's-tool`, by the exemplar's definition.** Two identifier columns are not today's one field with a slash, but they fix the pain only once the feed's normalising step exists, and the Ravensdale half is fixed only once someone has entered the book. v0.1 has neither: its identifiers are sample values and its Crates board holds what someone keyed. The row says so, and leaning 4, leaning 6 and questions 3 and 4 carry the two dependencies.
2. **Pattern 7 produced corrections and no leaning.** Both hits (the true talk share, the longer company name) are facts the input cannot support, not structure questions, so correcting the fields is the whole of the fix; a leaning with a "live condition that settles it" would have been invented. Logged here so the verifier sees the choice rather than a gap.

## 7. Transcript: no mess pass, and why

The brief allows a mess pass on s12 to s25 "with judgment" where our side speaks in writer-clean paragraphs. It was not applied here, for three reasons. First, the own-side speech is already messy by construction: 83 shredded boundaries cut into the Consultant's and Thandiwe's units at both ends ("Hi, all. Mostly listening, yes. I'll have" at L9, "borrowing money. Good. I would have got that" at L31), and the two duets are the fixture's planted delivery defect. Second, every word count in `intake.export_family` and `intake.shred`, and in the README's Measurements, is a measured ground truth: an added word anywhere moves `words_true`, the by-label counts and shares, the shred's side balance and the longest-unit figures, and the true shares could not be honestly recomputed without the generator's plan, which the review has just marked as author-only data. Third, the three long clean units (L98, L189, L246) are where the swallowed assents sit; editing around them risks the very spans the fixture protects. Unit count, numbering and timing lines are unchanged, and no location moved.

## 8. README

Brought in line: the key's line count (496) and the `readiness` block in the Files table; the no-write sentence in "The call"; the quietest-speaker repair in the defect table; the renamed field and a new Readiness paragraph in Counts; the true-share marking in Measurements and Checks run; the quote count (197 quote fields plus `evidence_quote_or_null`, 198 pairs, 173 with a location); the field-order sentence in Conventions; and the Review status, which now records the user's review of 2026-10-13 and carries the one-sentence "fix pass applied 2026-10-13: ..." line. No count the README gives for rubric rows, pains, objections, traps, leak entries, requested changes, vocabulary, commitments, entities or integrations moved.

## 9. Coverage row

`coverage-row.md` holds the row, same thirteen columns as the existing one. The only count that moved is Quote strings, 166 to 198 (the verifier's pairs); the Review column reads `reviewed 2026-10-13; fix pass applied 2026-10-13`.

## 10. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (3 read-back, 2 discovery) |
| pains | 6 |
| signals | 6 |
| entities | 30 (20 with a parent, all with `moves_independently`) |
| leanings | 7 |
| patterns | 3 |
| element_per_pain | 6 (4 fixes, 1 copies-today's-tool, 1 none) |
| incumbents | 8 |
| assumptions | 13 |
| unmet needs | 4 |
| AI opportunities | 5 |
| verdict | build, own-account, one workspace |
| existing fields corrected | 20 string values across 16 fields, plus one key renamed and one note added |
| transcript edits | 0 |
| key size | 496 lines, from 349 |

## 11. Verifier output

`python3 -I verify_quotes.py fixtures/s23-symmetric-shred`, run after every edit to the key (the README edits touch no quote) and once more at the end; this is the final run.

```
Fixture: s23-symmetric-shred
Sources: transcript.txt (transcript/line-time-first, 264 units)

pairs found      198
verified         198  (of which presence only, no location cited: 25)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
refused_quotes   10 entries in 1 list(s) are the key's own refusals and are not checked
```

Exit code 0. No location notes were reported. The `apply.py` script proved each quote the block introduces at its cited line before writing (every `pains`, `signals` and `leanings` quote, the three `outcome` strings, and every `evidence` location in `entities` and `incumbents`); the shared verifier's 198 pairs include the key's 25 presence-only quotes, unchanged from before the pass.
