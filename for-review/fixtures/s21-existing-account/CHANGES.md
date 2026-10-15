# s21-existing-account — fix pass changes

Editor's log, 2026-10-13. Everything in the fixture is fictional and stays fictional. Files touched: `fixtures/s21-existing-account/answer-key.json`, `transcript.txt` and `README.md`. Before-copies of all three sit beside this log (`answer-key.before.json`, `transcript.before.txt`, `README.before.md`), with the scripts that made the changes (`render.py`, `stage1.py`, `stage23.py`, `stage4.py`).

Method. The key was loaded, changed and dumped by script. Its layout is not `json.dump`'s: every list entry and every second-level key sits on one line, so `render.py` reproduces that layout and was proven byte for byte against the untouched file before the first edit. The `readiness` block is printed two levels deeper (one entry per line) so it can be read; the README says so. The 25 fields keep their order, `intake` follows them, and `readiness` is the 27th and last field. Every string replacement in the key and the README was asserted to match exactly once. Every quote the block introduces was copied from the transcript and proven at its unit by the script before the file was written, and the shared verifier was run after each stage (four runs, all clean).

## 1. The review entry's changes (FEEDBACK.md, s21 entry of 2026-10-11)

**Item 1, the costing delta joins `requested_changes`.** A `change` entry was inserted first in the array, as the main build: keep Bethan's form and her cells as subitems; the cell total onto the parent so the Studies board reads it through a connection (the drift at 00:18:20 named as the failure it fixes); unverified until tried on a copy (00:19:46); access to her workspace pending the client's IT (00:20:26); plus the monthly per-agency costed-versus-actual view (00:17:34, 00:21:47) once the finance source for actual is resolved; chosen by Bethan from the two approaches at 00:19:16 and approved by Henrietta at 00:35:53. Its quote is Bethan's choice, "Either of those would do it, honestly. The first one. I don't want to lose the form." (00:19:57), verified by presence like the array's other quotes. The array is now 1 add, 3 change, 1 remove.

**Item 2, the rota archive has no approval from Henrietta.** The wording "archive proposed; Idris accepts; Henrietta's approval still required before anything changes" now stands wherever the archive is described: `requested_changes` (the `remove` entry), `rubric` R12's note (the sentence that said the label handover and the archive were both agreed with Henrietta's yes now separates the two), `commitments_and_next_steps` (the archive entry's `what` and `owner`), `intake.prior_attempts[0].disposition`, `expected_structures.lookalike_traps[2]`, the trap that begins "The dead rota board is archived, never deleted", `expected_monday_products[0].why` and `purpose_of_this_fixture` item (8). The R12 note is rubric material, which the brief otherwise leaves alone; it was changed because the review entry names "wherever the archive is described", and only the sentence about the archive moved; the grade did not.

**Item 3, the booking link is committed, not delivered.** The evidence state is now "committed to send today", with owner (the Consultant) and purpose (the 45-minute working session on a copy of the costing board), in `purpose_of_this_fixture` item (5) and the R10 note (the two places the entry cites by line), in `commitments_and_next_steps[0]` (`what` and `date`: "not yet sent", done only on evidence) and in `intake.next_step` (`state` and `mechanism`). R10's status stays `met`; the entry says the grading question waits for v2.

## 2. The `direction` rename

`intake.type_header.direction_of_show` is `direction` in the header and in each of the three `segments`; `direction_of_show_note` follows as `direction_note`. The dictionary was rebuilt so key order is unchanged. The README's two sentences naming the field now name `direction` and `direction_note`, and the old name does not appear in the key or the README (the README's history paragraph says "direction-of-show value" in prose). The signal text "decides direction of show for the middle segment" is prose about the concept, not the field, and stands.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry. A field was corrected when a builder reading it alone would build the flaw; where the field was only incomplete, the leaning carries it (brief, section 8).

1. **One row where the call describes many.** One hit. The recruiter week view: the key described it as "read from the Studies board's field dates" and `vocabulary["session"]` as "item on a recruiter week view", which together let a builder make one row per study carrying its field dates, the shape of the dead rota board that "never had the sessions on it" (00:23:55). Leaning 1: one row per session (date, centre, room, recruiters, headcount) under the study, bounded by the Studies field dates; typed by Leonie, so Studies stays read-not-typed for the account leads; child rows on Studies or a connected sessions board is the open choice. The leaning says the link to the Studies dates is our design drawn from Idris's account, not his words. **Field corrected:** `vocabulary["session"].likely_monday_object`. Considered and left: the cell count typed on the form against the subitems (folded into pattern 6); the costing board itself already has cells as child rows, which is the pattern applied, not a hit.
2. **A pain with no element that fixes it.** One hit, P1.6 (costed versus actual, 00:22:02): the view's actual half has no source in v0.1. Leaning 5 says the view shows the costed half only and that a typed actual figure is a claim about the accounting system, never its number. `element_per_pain` marks it `copies-today's-tool`, by the brief's definition (a structure that fixes the pain only once a data feed exists that v0.1 does not have); today's tool is a shrug, and a half view does not answer the question. Every other pain has an element; P1.3's element rests on an assumption (Philippa reads the board) that is listed with its question, and the third keying into the accounting system stays an unmet need.
3. **An alias-map entry that names more than one entity.** One hit. `intake.alias_map["Farraday"]` read "an agency and its study; not a person", two things in one entry. **Field corrected:** the agency is the one entity, "the Farraday one" (00:09:16) its study and "the Farraday invoice" (00:37:30) its invoice. The structural consequence (agency as one value per agency on the study row, never a board of agencies) sits in leaning 6 rather than in a leaning of its own, because that is where the agency value's home is decided. Checked and left: `vocabulary["the sheet"]` names two spreadsheets, but it is a vocabulary entry that already says "confirm which", not an alias entry.
4. **Our framing labelled as the client's.** One soft hit, and one hit the review entry had already found. The soft hit: `expected_structures.lookalike_traps[1]` keyed the per-agency view by "the agency value already on Studies", and `vocabulary["client / agency / brand"]` placed agency "on Studies"; the call puts agency on the costing form (00:15:14) and never says Studies has it. **Fields corrected:** both, to "the costing form carries agency today; Studies only if a column exists there, read live". Leaning 6 carries it. The review entry's item 2 (an approval of Henrietta's that was ours) is logged in section 1. Checked and left: "read, not typed" is the Consultant's phrase, but Henrietta adopted it out loud ("Read, not typed. Good way of putting it.", 00:35:02), so it is hers; the four-part scope is the Consultant's playback, confirmed by "That's the shape." (00:34:33).
5. **A shared resource with no reservation tracking.** One hit: recruiters and rooms, booked across sessions and studies, with Leonie's colour-coded sheet as the only reservation record ("two recruiters booked on it and neither of them knew", 00:23:13; "nobody could read the colours and we lost two sessions", 00:24:24). Leaning 2: each session row names its recruiters, room and centre, with a per-recruiter and per-room view of the week. `entities` carries `shared_resource: true` for recruiter and room. No existing field was wrong; the `add` entry already lists sessions, rooms, recruiters and headcount from Idris's words.
6. **An artefact that can go stale with nothing to flag it.** Two hits. The costed number after a late cell or an n change: a working roll-up moves the parent, but the number already sent to the agency is a snapshot, and Bethan "doesn't always know it's changed" (00:18:49). Leaning 3: the parent keeps the total as sent and its date, and shows the difference. The study code: typed on the form and on Studies, and a space in one copy "never lined up" (00:16:13). Leaning 4: typed once on Studies, read by the costing board. Neither field was wrong (`vocabulary["costed brief / costing"]` and `vocabulary["code"]` are silent, not false), so the leanings carry both. Checked and left: Leonie's photo (replaced by leaning 1's live view), finance's copy of the sheet (replaced), the two duplicate status labels (the label handover is the element).
7. **An expected output the input cannot support.** No hit in the pattern's sense. Checked: the transcript statistics in `transcript_format`, `intake.format` and the README were recounted from the file under the README's own definition before and after the mess pass and match (see section 6); the 20 November year is already marked as coming from the intake call date; the titles and the prior build's date are already marked as the record's. The "agency already on Studies" claim was the one assertion the input does not support, and it is logged under pattern 4.

## 4. The "never written to" rule

A search of the key for "never written", "written to", "written back", "write back", "writeback", "never touch" and "never connected" found three claims, each traced: the panel software "never to be connected or copied" (`integrations_mentioned`, `vocabulary`, `compliance_or_security_signals`, `expected_structures.notes`) traces to Idris, "It never goes near a board and it never will, we've been through that with the, er, the agencies' compliance people more than once." (00:27:14); bank details staying in the accounting system traces to Henrietta (00:32:11); the accounting system read being "a question for Philippa, never assumed" is a question, the right shape. Nothing needed rewording. The new `existing.incumbents` entry for the accounting system uses the rule's wording from the start (writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours), and the unmet need for the third keying repeats it.

## 5. Standing lines, where they bite

- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Bites on the booking link (section 1, item 3). The other nine commitments were read against the line and stand: each carries owner, purpose and a date or "not set", and none claims delivery; the archive entry now also carries its approval state. The verdict's last condition names the four commitments (the link, the recap, Idris's photo, Bethan's access request) as committed, not done. No `status` sub-field was added, for the reason the exemplars give: that is one decision for all twenty-five keys.
- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites twice in the block: leaning 2 and `element_per_pain` P2.1 say a session status set by Leonie is her claim that the recruiter knows, and the wall screen is what the recruiters read; leaning 5 and the accounting-system incumbent say a typed actual figure is a claim about the accounting system. Nothing in the key's existing fields presented a status as evidence.
- **s11 (inference targets questions; it never fills evidence).** Six `signals`, each naming what our side never confirmed, drive the three read-back questions (Philippa reading the board, the code typed once, Leonie owning a board). Inferred shapes carry `source: observed` or `assumed` in `entities`; two entities' `evidence` is an observation on the screen share, marked `observed`.
- **s15 (a product limit never deletes a client need).** Five `unmet_needs` stay in the record with their clocks where the client gave one: actual beside costed, the third keying, the forty-eight-hour turnaround (not measured by any board in v0.1), the recruiters' week at both centres (conditional), and n at screener sign-off.

## 6. Transcript: the mess pass (brief, section 5)

Six unquoted Consultant turns gained a false start, a filler or a repeated half-phrase: 00:04:55, 00:05:44, 00:20:40, 00:21:36, 00:25:42 and 00:27:05. Each was checked against the verifier's `--spans` list first; none holds a quoted span, none is a presence-only quote, and none contains a blocklisted phrase. Unit count, numbering and every timestamp are unchanged (`diff` on the stamps is empty; six lines differ). Sixteen words were added: 4,769 became 4,785; the longest turn is still 83 words at 00:33:57; 24 turns at or below four words and 20 adjacent same-label pairs, as before; client share 67% as before, with Henrietta's share moving from 27% to 26% by rounding (26.5% became 26.4%). `transcript_format` ("About 4,785 spoken words", the shares) and `intake.format.words_spoken` (4785) follow; the README's transcript row follows. Judgment: the README records two earlier roughening passes, so the Consultant's side was already partly messy; the six turns were the ones still in writer-clean sentences.

## 7. The readiness block, field by field

- `note`: the brief's text, plus one sentence on the client-account target (A11-2) and one on the pain numbering. No v2 disagreement to record: `should_plugin_propose_a_build` is `true` and the block clears a build.
- `pains`: the key's nine entries in array order, same quotes and locations, numbered after their themes: P1.1 to P1.6, P2.1, P2.2, and the unnumbered incumbent-friction entry as P3.1, the next free number. `stated_or_excavated`: excavated where a Consultant question drew the line out (P1.1, P1.2, P2.1, P2.2, P3.1), stated where the client volunteered it or answered Henrietta's own question (P1.3 to P1.6). Outcomes are verbatim: Henrietta's "costs it once, in one place" (00:28:25) and "one of it" (00:28:41), Bethan's Fridays (00:28:59), Idris's week (00:29:03) and wall screen (00:26:01), Henrietta's "someone here who can change things" (00:05:55); P1.6 carries null because nobody said what the view is for beyond the ask.
- `signals`: six.
- `entities`: thirty, answering what moves independently of what: the brief/study with its cells, n, code, field dates, sessions, status label and invoice; recruiters and rooms as shared resources; six artefacts that go stale (the code copy, the parent total, the sent number, the two sheets and finance's copy, the photo, the dead board).
- `structure`: Work Management; `client-account`, "existing customer with a live account of their own (A21)"; `workspaces` are the two existing ones (the Studies board's workspace, name not spoken, and Bethan's own), because A21's rule plans new workspaces unless the build continues workspaces already built for the same client, which this one does, so no "Kelbrook – Ops" is planned and the key stays ASCII; `native_reuse` none; six leanings; two patterns; nine `element_per_pain` rows (eight `fixes`, one `copies-today's-tool`, no `none`).
- `existing`: the bound account as the key describes it, and five incumbents with field authority.
- `assumptions`: thirteen, each with its question. `unmet_needs`: five. `ai_opportunities`: four, all round 2 (nobody asked for AI or workflows); the two workflows cite P-21, the two AI columns are unprobed, as the probe findings stand.
- `verdict`: `build`, nine conditions beginning with the approval stop and "A11-2 asked first (client-account target)", and a one-sentence reason in the spec's terms.
- `questions`: five, the ceiling: two discovery (access; the roll-up on a copy) and three read-backs (Philippa, the code and the Studies columns, Leonie). From the key's nine pre-build questions: items 1, 2, 3, 4 and 7 are reused in build terms; items 6, 8 and 9 (labels, admins, seats) became assumptions with preflight or handover questions; item 5 (the loaded rate) stays out of the block, because it is pricing material, and is named in Q3's `known` as a separate conversation.
- Sales vocabulary: the script refused to write the block if it held an R-number, a gate name, a grade or a verdict word; none is in it.

## 8. README

Brought in line: the transcript row (words and shares), the key row (27 fields, 866 lines), the plant row for the next step (committed, not delivered), the requested-changes count (1 add, 3 change, 1 remove, with the archive's approval state), the quote count after the pass (194 strings, 191 verified, 3 pointers), the header-shape sentences (`direction`, `direction_note`), the layout sentence (the `readiness` block prints one entry per line), one review-history sentence beginning "Fix pass applied 2026-10-13:", and the review status (reviewed 2026-10-11 in FEEDBACK, fix pass applied 2026-10-13). The earlier review-pass paragraphs are history and stand.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 9 (P1.1 to P1.6, P2.1, P2.2, P3.1) |
| signals | 6 |
| entities | 30 (19 with a parent, all with `moves_independently`) |
| leanings | 6 |
| element_per_pain | 9 (8 fixes, 1 copies-today's-tool) |
| incumbents | 5 |
| assumptions | 13 |
| unmet needs | 5 |
| AI opportunities | 4 |
| verdict conditions | 9 |
| existing fields corrected by the sweep | 4 (`lookalike_traps[1]`, two `vocabulary` entries, one `alias_map` entry) |
| fields changed by the review entry | 14 places across 11 fields (section 1) |
| transcript edits | 6 turns, 16 words, 0 units or stamps |
| key size | 866 lines, from 274; 27 top-level fields |

## 10. For the planner

- The brief fixes the Review column as `reviewed 2026-10-13; fix pass applied 2026-10-13`; s21's review entry is dated 2026-10-11. The coverage row uses the brief's string, and says so.
- `structure.workspaces` for a client-account build that continues existing workspaces holds descriptions of the existing workspaces rather than "<Client> – Product" names. If the record map wants a fixed form for that case (for example a `continues_existing: true` flag), that is one decision for s21 and any later client-account key.
- The R10 note was edited for its evidence state only, because the review entry cites that line; the grade and every other rubric row are untouched.

## 11. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s21-existing-account`, final run after every edit, exit code 0:

```
Fixture: s21-existing-account
Sources: transcript.txt (transcript/line-bracket, 262 units)

pairs found      194
verified         191  (of which presence only, no location cited: 25)
skipped          3  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

The three skipped values are the same three bare location pointers the baseline records (`intake.current_state_met_early.from_quotes`); no location note was reported in any run. The stage scripts also proved the nine `outcome` strings, the thirty entity `evidence` locations and the five incumbent `evidence` locations against the transcript before writing, since those keys carry no "quote" name and the shared verifier does not read them.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | This time, someone here who can change things, not emailing and waiting | 00:05:55 Henrietta Weyland (Director of Operations) | P3.1 |
| G2 | A monthly view per agency of what was costed against what it came in at | 00:21:47 Bethan Tull (Fieldwork Manager) | P1.6 |
| G3 | Each brief costed once, in one place; the agency's number is Philippa's number | 00:28:25 Henrietta Weyland (Director of Operations) | P1.1, P1.2, P1.3, P1.4, P1.5 |
| G4 | The recruiters see their week without Leonie retyping it | 00:29:03 Idris Machado (Recruitment Team Lead) | P2.1, P2.2 |

Assumption kinds: gap 5, leaning 5, board-architecture 2, automation-condition 1.

Verifier: 194 pairs, 191 verified, 0 misses and 0 near-misses before; 198 pairs, 195 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- every goal is something the client wants next, not what the live Studies, Incentives or digest already does (the "don't touch the Friday email" line is a constraint, not a goal); G1 is the director's own "this time" aim, which is also the wanted outcome of the incumbent friction P3.1, kept because she states it as what she would do differently; G2 cites only the first half of the sentence the backchannel splits (00:21:47, ending "against what"), never across the Consultant's label, and Bethan says Henrietta cares about it, which Henrietta confirms at 00:22:12; Hamish's "stop hearing about the sheet" was left out as relayed, and "I get my Fridays back" and the wall-screen line as single-pain outcomes.
