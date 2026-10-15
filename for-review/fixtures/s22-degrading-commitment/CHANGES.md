# s22-degrading-commitment — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional. Files touched: `fixtures/s22-degrading-commitment/answer-key.json`, `transcript-1.txt`, `transcript-2.txt` and `README.md`. The work was done by one script (kept in the session scratchpad, not in `fixtures-work/`), which proved every quote it wrote at its cited unit before writing and which reproduced the untouched key byte for byte with the key's own layout before any change was made. The verifier ran clean after the transcript edits and again after the key edits; the final run is pasted in section 9.

Build target for the readiness block: own-account, because the fixture is a prospect (A21). The key's own `should_plugin_propose_a_build: true` and the block's `build` agree, so the note sentence the brief reserves for the thin case is not added.

## 1. The review entry's two changes, exactly as recorded (FEEDBACK.md, s22 entry)

**Item 1, loss charges: a build design where an open question belongs.**

- `expected_questions_before_building[7]` (the loss write-up question) is now the open question in the entry's words: can the dock check bags before they are tipped, or tag bins by hotel; does the charge go on the hotel's next route, and so on the regular Sunday invoice; who keys it onto the route, since v0.1 writes nothing into the route software. Routed to the plant manager and the finance director. It names the three facts the entry rests on, each with its location: the route closes on the handheld at the last stop (call 1, 00:07:48), the bag is scanned and the bin is not (call 1, 00:22:48), the invoice runs weekly off the closed routes (call 2, 00:02:39). It ends: the write-up form is planned only once this is answered; nothing in this key says a write-up reaches the route by itself.
- `expected_structures.notes` (the former key line 235): the loss write-up is listed as the fifth object only as "planned once the open question is answered", with the three questions and their routing, and "never described as reaching the route by itself, since the route closes on the handheld at the last stop and the bag is tipped into a shared bin before damage is seen". The old clause "that reaches the route before it closes" is gone.
- `integrations_mentioned[2]` (the accounting system): the old "the loss write-up is designed to reach the route before it closes" is replaced. A loss charge reaches the invoice only through a route a person keys it onto, most likely the hotel's next route; carried as an open question, never as a write-up that reaches the route by itself. The same sentence applies the never-written rule to this system (section 4).
- `vocabulary["loss clause / loss charge"].likely_monday_object`: the write-up item is "planned only once the open question is answered", with the three questions named. `vocabulary["soil side / soil dock"].likely_monday_object`: the form's home "if the dock can check bags before they are tipped; otherwise the hotel is unknown by the time damage is seen and no form helps".
- The readiness block carries it as leaning 6, as `element_per_pain` P3.1 and P3.2 (`none`), as an unmet need with its January clock, as a verdict condition and as question 1 (a read-back of the finance director's own words at call 2, 00:11:49).
- Checked and left: the Consultant's playbacks that mention "a loss write-up from the soil dock" (call 1, 00:31:01; call 2, 00:21:19) are transcript quotes in `rubric` and stay; the key's statement of them as the client's accepted scope was already "a first look with a condition apiece" (R12 note, v2, untouched). A grep for "reaches the route" now finds only the two negations above.

**Item 2, par changes: the demo shows the queue, not the sheet changing.**

- `requested_changes[0].description` (the former key line 193, "must land on the stop it belongs to and show whether it has landed"): now the status says what it is, keyed into the route software by a named person and confirmed on the printed sheet by a named person; each status is a claim set by a person, never evidence that the route software or the sheet changed; v0.1 demonstrates the queue in front of the par table and the confirmation step, not the route sheet updating; the plant manager's condition (the entry's own quote, call 2, 00:22:22) and the systems administrator's six seconds later (call 2, 00:22:28) pull against each other for anything we build, and the demo says so. The quote on the entry is unchanged.
- `expected_structures.notes`: the "landed status for the desk and the plant managers" is replaced by the same wording, with both conditions quoted and located, and the automation on the approval list is now "a notification to the plant managers when a par change is marked confirmed".
- `vocabulary["par change"].likely_monday_object`: "linked to each stop it covers, with a status that says what it is (keyed ... by a named person; confirmed on the printed sheet by a named person): a claim set by a person, never evidence that the par table changed; the board is the queue in front of the par table, not the par table".
- `traps[23]` ("The par table stays in the route software ... whether it landed"): corrected to the same statement, with the administrator's two locations for the no-write condition and the sentence that v0.1 shows the queue and the confirmation, not the sheet, and that the two conditions pull against each other.
- The entry's unverified note (the planned connection is read-only; if it can read the par table back, a later version could confirm "landed" from the source system itself; not probed): recorded as a possibility and never a promise in `expected_questions_before_building[5]` (the read-only connection question, which gains the sentence "Unprobed, a possibility and never a promise: whether the par table itself can be read back..."), at the end of `expected_structures.notes`, in leaning 5's condition, in the unmet need for the plant manager's condition and in question 2.
- The two conditions as a fork: the key has no `forks` field, so there is no existing fork entry to carry a `leaning`; the fork lives in `readiness.structure.leanings[4]` with `pattern: "fork"` and in the three fields above. Noted for the planner in case the record map wants a fork entry outside the block.

## 2. The `direction` rename

`intake.type_header.call_1.direction_of_show` and `intake.type_header.call_2.direction_of_show` are `direction`, in the same position in each header, same value (`no-show`). `direction_of_show` appears nowhere in the key or the README now; the README's conventions bullet says so. The README never named the field before.

## 3. The seven-pattern sweep over the key

Each hit is a `readiness.structure.leanings` entry; where it sat in an existing field and a builder reading that field alone would build the flaw, the field was corrected too (exemplar rule three). Nine leanings in all.

1. **One row where the call describes many.** Two hits.
   - A par change. One form item "linked to the stop" carried one landed status, but a hotel's change can cover every line ("go through every item", call 1, 00:12:29) and, for a hotel with two properties, two stops on two plants' routes keyed by two desks (call 1, 00:15:06 and 00:16:38). Leaning 1: a par-change request as the parent row, one child row per stop it covers, each with its own keyed-by and confirmed status, "all confirmed" rolling up. **Field corrected:** `vocabulary["par change"]` and `requested_changes[0]` now say "each stop it covers" (both were being rewritten under item 2 anyway).
   - A short. The Sable Point was "a short and an over on the same stop" (call 1, 00:11:42); one row per short with a type value cannot hold both. Leaning 2: one row per item line (stop, item, quantity, short or over), grouped by stop and day, the count of lines light mirrored to the stop. `expected_structures.notes` now says "one row per item light"; `vocabulary["over"]` ("a type value on the shortage log, not a second board") stands, because it is right once rows are per item.
   - Both patterns are in `structure.patterns` as parent-row-with-roll-up.
2. **A pain with no element that fixes it.** Five `none` rows in `element_per_pain`, two of them with leanings of their own.
   - P4.1 rewash: nothing in the five objects counts it, and nothing may be seeded from the relayed guess. Leaning 3; an unmet need.
   - P5.1 the pack check ("Nobody sits between the sheet and the bag", call 1, 00:07:09): the shortage log records a short after it exists; a packed-light flag at the dock needs the sheet's lines per stop, which the sample day does not carry. Leaning 4; an unmet need. P1.2 (the lost account, nobody rang) is `none` for the same reason: nothing in v0.1 warns the hotel before the cage opens.
   - P3.1 and P3.2 are `none` because the write-up waits on the open question of section 1.
3. **An alias-map entry that names more than one entity.** No hit. The twelve entries each name one person, place or organisation. Nearest candidates: "Rhiannon" (one person with two roles, plant manager and route office at Halcott) and "Halcott" (one place, also used for its staff: "Halcott stopped filling theirs in"). Both stand.
4. **Our framing labelled as the client's.** Two hits, both corrected.
   - `entities_and_workflows[8]` read "Loss write-up today: a paper form that is supposed to go to the finance side and mostly does not". No client line mentions a form of any kind for losses; the client says the soil side has "nowhere to put it" (call 1, 00:19:10) and "who's going to write it up" (call 1, 00:17:59). **Corrected** to: nothing is written up on the day; the soil side sees the damage and has nowhere to put it; the finance director finds losses through replacement orders months later; the open questions in the client's words, with both locations.
   - `integrations_mentioned[0]` read "Condition from the systems administrator and the approver: nothing writes into it". The no-write condition is the administrator's alone ("Read out of it, fine. Write into it, no.", call 2, 00:14:56; call 2, 00:22:28). The approver's conditions are different: the drivers do nothing extra ("If the answer is they scan and then also type, no.", call 2, 00:06:36) and the handheld piece in writing. **Corrected**, and the entry now also labels "source of truth" as the Consultant's phrase (call 1, 00:30:49) against the plant manager's "the one that prints" (call 1, 00:30:18). Leaning 9.
   - Checked and left: the five-part first cut is the Consultant's playback and the R12 note already says so; "landed" is the operations director's own word (call 1, 00:24:56); "three taps" is the plant manager's; the thirty-day window is the contract's in the client's words.
5. **A shared resource with no reservation tracking.** No hit in the brief's sense. Nearest candidates, named and declined: the van back out (a driver pulled off his route, call 1, 00:12:13) is an ad hoc pull recorded in "what we did" on the short, not a booking; the shelf stock (clean linen shared across every account on tomorrow's routes) is the route software's par domain and nobody asked for it to move. Both carry `shared_resource: true` in `entities`, as does the soil-side bin, whose sharing across hotels is the provenance problem of section 1. No leaning was forced.
6. **An artefact that can go stale with nothing to flag it.** Two hits.
   - The stops view is a copy of the route sheets; in v0.1 every row is a typed sample value and later a read-only mirror. Leaning 7: an as-of marker and a source on every row, said out loud ("As long as it's said out loud that it's a sample.", call 1, 00:32:31). `expected_structures.notes` now says "with its as-of marker". `vocabulary["route sheet"]` stands as incomplete rather than wrong.
   - The printed route sheet goes stale when a par change is keyed after the nightly print. Leaning 8: the child row's two statuses against the print, with a view of changes not yet keyed before tonight's print; the sheet itself is not ours to reprint.
   - The whiteboard (wiped weekly) and the soil-dock tally sheet carry `goes_stale: true` in `entities` and need no leaning: the log replaces the first and nothing replaces the second until the count exists.
7. **An expected output the input cannot support.** One hit, which is the review entry's item 1: a write-up "that reaches the route before it closes" cannot be produced from the mapped process. Leaning 6 carries it, with the three client lines it rests on. Everything else checked holds: the transcript statistics were recounted by the README's own rule and matched before the mess pass (4,937 and 3,573 words, 121 and 128 for the longest Consultant turns, 15 and 12 short turns, zero adjacent same-label pairs, client shares 71% and 64%); the weekdays fit November 2026 (Thursday the 12th, Monday the 9th, Tuesday the 24th); the rebuilt bleed range is arithmetic on the key's own inputs and is labelled an inference.

## 4. The "never written to" rule

s22 is one of the eleven keys FEEDBACK names, and the user's note says its no-write phrasing is client-backed. Each occurrence was traced:

- Backed by the systems administrator ("Read out of it, fine. Write into it, no.", call 2, 00:14:56; "Show me nothing writing into the route software and I'm in.", 00:22:28; "Yes, if it doesn't write into my system.", 00:24:43) and kept, with the location now stated beside it where it was not: `integrations_mentioned[0]` (also corrected for attribution, section 3.4), `expected_monday_products[0].why` ("read-only, nothing writing back" gains "the systems administrator's condition, call 2, 00:14:56"), `expected_questions_before_building[5]` ("Nothing writes back" gains "the systems administrator's condition"), `traps[23]` (rewritten, section 1), `expected_structures.notes` ("No write to the route software (the administrator's condition; staying clear of it is also our default, labelled as ours)"), `requested_changes[2]` (already carries the quote; unchanged).
- Our own commitment, labelled as ours and left: `intake.claims_by_our_side[3]` ("Nothing I build writes into the route software", the Consultant at call 1, 00:32:05, recorded as a constraint the blueprint must honour).
- Reworded under the rule: `integrations_mentioned[2]`, the accounting system. The old entry implied a no-write choice ("rather than to write into accounting") that no client line supports. Now: "Writeback and integration direction for it are unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours." The readiness `existing.incumbents` entry for the accounting system says the same.
- Left as v2 material: the R9 note's "the route software stays the source of truth and nothing writes into it" sits in `rubric`, which this pass does not edit; it is client-backed in any case.

## 5. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence that the source system changed).** This fixture's own line. It bites on the par-change status (every field in section 1, item 2, and leaning 5), on the credit status (`vocabulary["credit"].likely_monday_object` now reads "set by a person as a claim that a credit was raised; the credit itself and its amount stay in the accounting system"; `expected_structures.notes` says the same) and on any loss charge on a board (the accounting incumbent entry). The demo's sentence of what it does not show is a verdict condition.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Two `commitments_and_next_steps` entries claimed delivery. Entry 10 (the route sheet and whiteboard photo) said "done: 'It went yesterday...'" on the sender's word alone; it now reads "reported sent by the plant manager on call 2 ... receipt not confirmed on the call; done once the files are opened", with the date "reported sent 11 November". Entry 9 (the technical partner's call) keeps "done", because the systems administrator, who attended, says it happened (call 2, 00:01:27); its date field now says that this is the evidence and that what was said in the meeting stays reported, unverified. The other ten entries are committed with owner, purpose and date and claim nothing delivered; the walkthrough invite, the three columns, the per-head answer, the bleed write-up and the recap correction are open commitments and verdict conditions carry the ones the build depends on. No `status` field was added, for the reason the exemplars give.
- **s11 (inference targets questions; it never fills evidence).** Six unconfirmed client ties are in `signals`, each naming what our side never confirmed, and three of the five questions are read-backs of those words. None appears as evidence or in an element: the handheld posting stays reported and unverified, and the one `assumed` entity (the stops view) carries `evidence: null`.
- **s15 (a product limit never deletes a client need).** Six `unmet_needs`: the rewash count, the par change landing on the sheet, the handheld posting with no extra step, loss charges on the invoice, the pack check, and being told when the other plant changes a par. Each keeps the client's clock where one was given and says why v0.1 does not meet it.

## 6. Transcript edits (brief section 5, the s11 mess pass)

Six Consultant turns, all inside existing units, none of them a quoted span, all writer-clean before: call 1, 00:21:37 (the playback: "the job, um, the job effectively lives on a paper sheet" and "depending on whether Nadia's -- on whether Nadia's in"), 00:23:11 ("you use to, um, to coordinate"), 00:28:30 ("Then I'd like -- I'd like Ezekiel"); call 2, 00:02:21 ("can I start with -- can I start with"), 00:14:38 (an added tail, "To the first version, I mean."), 00:22:50 ("it changes it quite a lot," after the protected first two sentences). The verifier's `--spans` listing was read first: 00:21:37, 00:23:11, 00:28:30, 00:02:21 and 00:14:38 carry no protected span; 00:22:50's span is the first two sentences and the edit sits after it. Unit counts, numbering and timing lines are unchanged (191 and 150). Word counts moved: call 1 from 4,937 to 4,947 and the Consultant's longest turn from 121 to 127 words (still 00:21:37); call 2 from 3,573 to 3,589 (the longest turn stays 128 at 00:21:19); client shares stay 71% and 64% and the per-speaker shares are unchanged at the rounding. Updated to match: `transcript_format`, `intake.files[].words_spoken`, `intake.export_family.max_unit_words.call_1`, `intake.delivery_notes.call_1.longest_own_side_turn`, the README's files table and the coverage row. The README's notes on `--` as a restart marker and on short turns were re-checked and still hold.

## 7. The readiness block, field by field

- `pains`: the key's ten `pains` entries in array order, same quotes and locations. The key numbers four themes; the entries are numbered P1.1 to P1.3, P2.1 and P2.2, P3.1 and P3.2 and P4.1, and the two unnumbered entries the key marks "Stated, not graded" take the next free numbers, P5.1 (the shelf short because the wash is behind) and P6.1 (the two plants not seeing each other's changes), per exemplar rule one. P1 to P3 are `excavated`, as the R2 note says; P4 and the two ungraded entries are `stated`. Outcomes are verbatim from the client: the operations director's one screen (call 1, 00:24:56) for P1.1, with its last sentence for P1.3 and its par-change clause for P2.1; the plant manager's "on the route sheet before the pack floor prints it" (call 1, 00:25:26) for P2.2; the finance director's "Loss charges on the invoice..." (call 2, 00:11:49) for P3.1 and P3.2; null for P1.2 (the co-owner's "no more Lindenmoors" is relayed and stays a stakeholder note), P4.1, P5.1 and P6.1.
- `signals`: six, all from call 2, listed in section 5 under the s11 line. One of them is the finance director's "Good. Then that's my condition met."; the word "met" there is hers, inside a quote, not a grade.
- `entities`: twenty-three, twenty with a parent, each with `moves_independently`. The par change moves independently of the stop and covers more than one; the route sheet does not move on its own and goes stale; the bin, the shelf stock and the driver-and-van are the shared resources; the whiteboard, the tally sheet and our own stops view go stale; the stops view is the one `assumed` entry with `evidence: null`.
- `structure`: Work Management; `own-account` with the A21 reason; one workspace, "Ravensmere – Ops" (the en dash makes a formerly ASCII key UTF-8, which the brief allows); native reuse none, with the reason; nine leanings; two patterns; ten `element_per_pain` rows (four `fixes`, one `copies-today's-tool` for P2.2, five `none`). P2.2 is `copies-today's-tool` by exemplar rule two: the queue and the two statuses replace the route supervisor's inbox check, and the sheet still changes only when a person keys it into the route software, as today, until the par table can be read back.
- `existing`: "unknown, no account bound", with the A21 point and the handover question; seven incumbents, the route software, the handhelds and the accounting system with what each stays the record for and what follows, the whiteboards, the tally sheet, email and text, and the vendor's module named so it is never proposed back.
- `assumptions`: fourteen, each with the question that would replace it. They hold what fell out of the five questions: the routes conflict (fifty-eight against forty-nine; no v0.1 element depends on it), the per-head seats, the dashboards' contents, the thirty-day clock's start, the credit status, the sample day (invented by us; the pre-read sheet and photo are never typed in, per the key's own trap).
- `unmet_needs`: six (section 5, the s15 line).
- `ai_opportunities`: five, all round 2, because nobody on either call asked for AI or workflows. Two workflows cite P-21 (the workflows probe), the agent P-19, the Vibe app P-20, the AI column `unprobed`. Each is tied to one pain and says what it never does (write to the route software, reach a hotel).
- `verdict`: `build`. Three pains have named entities and wanted outcomes in the client's words, the product is chosen, the structure is stated with its leanings and the build target is the user's own account. Eight conditions, the approval stop first, then the A11 sentence (no A11 question first matters for an own-account build; the three decisions stay open), the three columns in writing before the 24th, the loss-charge open question before any form is planned, the par-change status shown as a claim with the demo saying what it does not show, nothing writing into or connecting to the route software in v0.1 with the sample day said out loud, no rate and no hotel-facing form, and the boiler-week blackout.
- `questions`: five, the ceiling. Q1 (read-back, finance director and plant manager) is the review entry's loss-charge question in the finance director's own words. Q2 (read-back, plant manager and systems administrator) reads both conditions back, says what v0.1 shows, and asks the unprobed read-back of the par table. Q3 (read-back, plant manager with the route supervisor and Halcott's plant manager) reads back "has to count both plants" and asks who logs a short and whether a short is one row per item. Q4 (discovery, our technical partner) is the key's first pool question in build terms: what was shown, and whether anything handheld-shaped is ever in scope. Q5 (discovery, operations director and the desk) asks the par-change shape per stop and what the one screen shows about a change. Reused from the key's pool: items 1, 6, 7 and 8 in part. Dropped from the five and held as assumptions or left to the key's own list: the bleed rebuild (item 2; sales material, v2), the routes conflict (item 3), the rewash count (item 4; an unmet need with its clock), the account and seats (item 5; under A21 not one of the five for a prospect), Service later (item 9; the client has not asked), Brindlewood's stops in the sample day (item 10; assumption 6).

No R-number, grade, gate name or verdict word is in the block; the script searched for them before writing. `rubric`, `expected_verdict` and `numbers` are untouched.

## 8. README and coverage row

README: the files table (word counts, the longest turn, the key's line count and 27th field), a new "Readiness block" bullet in the counts section, the quotes bullet (263 checked strings: 236 pairs and 27 quote-only), the conventions bullet (the layout, the block's opened-out sub-objects, the old 400-line budget now passed, `direction`), the review-status sentences (reviewed by the user on 2026-10-11; the adversarial paragraph no longer says "still not reviewed"), and the one-sentence fix-pass line at the end. `coverage-row.md` holds the row; the one count that moved is quote strings, 231 to 263.

Layout note for the verifier: the key prints every list entry and every second-level key on one line, which `json.dumps(indent=2)` would not reproduce, so the script dumps with the file's own rule (proved byte for byte on the untouched file) and opens out `readiness.structure`, `readiness.existing` and `readiness.verdict` one level so their lists read one entry per line. The key is 477 lines, from 333.

## Counts

| item | count |
| --- | --- |
| readiness questions | 5 (3 read-back, 2 discovery) |
| pains | 10 (P1.1 to P6.1) |
| signals | 6 |
| entities | 23 (20 with a parent, all with `moves_independently`) |
| leanings | 9 (one a fork) |
| element_per_pain | 10 (4 fixes, 1 copies-today's-tool, 5 none) |
| incumbents | 7 |
| assumptions | 14 |
| unmet needs | 6 |
| AI opportunities | 5 (all round 2) |
| existing fields changed outside the block | 17 paths changed, 2 renamed (`direction`), 0 added, 0 removed |
| transcript edits | 6 turns, 0 units added |
| key size | 477 lines and 27 fields, from 333 and 26 |

## 9. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s22-degrading-commitment`, the final run after every edit, exit code 0:

```
Fixture: s22-degrading-commitment
Sources: transcript-1.txt (transcript/line-bracket, 191 units); transcript-2.txt (transcript/line-time-last, 150 units)

pairs found      265
verified         263  (of which presence only, no location cited: 27)
skipped          1  (null, empty or a bare location pointer)
unparsed prose   2
near-misses      0
misses           0
unsupported      0

UNPARSED PROSE AND UNSUPPORTED FORMS
- /intake/second_hand[0]/figure_as_requoted [unparsed] a description about a quote, not a quotation | about twenty a week, hedged ('I think', 'about')
- /intake/second_hand[1]/contrast_with_the_wrong_requote [unparsed] a description about a quote, not a quotation | right numbers, right meaning, no assent sought; the only defect is the source named in the room, an…
```

The two unparsed entries are the key's own descriptive fields, present before the pass and reported, not failed, as the verifier's header says. No location notes were raised: no unit was renumbered. The edit script's own proofs covered the 32 located quotes the block introduces and the fourteen client phrases quoted inside prose fields, all verbatim at their units.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | One screen: this week's shorts across both plants, and whether each par change landed | call 1, 00:24:56 Genevieve Okundaye (Director of Operations) | P1.1, P2.1, P6.1 |
| G2 | The par change is on the route sheet before the pack floor prints it | call 1, 00:25:26 Declan Pellingham (Plant Manager) | P2.1, P2.2 |
| G3 | Take on the two hotels turned down in the summer over Saturday counts | call 2, 00:11:16 Genevieve Okundaye (Director of Operations) | P1.1, P5.1 |
| G4 | Loss charges on the invoice, inside the thirty days, not a credit memo weeks later | call 2, 00:11:49 Annika Brannock (Finance Director) | P3.1, P3.2 |
| G5 | Shorts on it by early December, if they can, before Brindlewood starts in January | call 2, 00:19:12 Genevieve Okundaye (Director of Operations) | P1.1, P1.2, P1.3 |

Assumption kinds: gap 8, leaning 3, automation-condition 2, board-architecture 1.

Verifier: 265 pairs, 263 verified, 0 misses and 0 near-misses before; 270 pairs, 268 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G5 is taken as the operations director last states it, on call 2 ("And shorts by early December, if we can."), which softens her call-1 form ("if shorts are on it by early December I'll sleep"), so the goal carries the hedge; G2 cites the plant manager's call-1 aim, whole inside the second half of the re-joined sentence (00:25:26), because his last statement on call 2 ("Show me the par change landing on the sheet and I'm in.") is the same aim put as a condition, unchanged in substance; G4 is the finance director's own call-2 aim, preferred over the operations director's call-1 relay of it; G3 (the two turned-away hotels) makes five, one over the usual, and could go if five is too many; the handheld promise, the drivers-do-nothing-extra rule and "nothing writes into the route software" were left out as conditions, and Brindlewood as a keep the finance director will not count as a gain.
