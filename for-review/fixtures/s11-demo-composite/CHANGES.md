# s11-demo-composite — fix pass changes

Editor's log, 2026-10-13. Everything in the fixture is fictional and stays fictional.

Files touched: `fixtures/s11-demo-composite/transcript.txt`, `answer-key.json` and `README.md`. Copies of the three originals sit in `orig/` beside this log. Work files here: `keyfmt.py` (a serializer that reproduces the key's hand layout: one space per level, one line per list item, a dict on one line when all its values are scalars; proven by a byte-for-byte round trip of the untouched key before any edit), `edit_b1.py`, `edit_b2.py`, `edit_b3.py`, `recite_b3.py`, `edit_key1.py`, `edit_key2.py`, `edit_readme.py` (the edits, in the order run), `final_verify.txt`. Every key change was made by loading, changing and dumping through `keyfmt.py`; every transcript edit asserted that its target string was unique and sat outside every span the verifier protects. The verifier ran after each step: B1, B2, B3, the re-cite, key step 1, key step 2, and once more at the end. Zero misses, zero near-misses and zero location notes at every run except the one expected miss after B3, which the re-cite step cleared.

A note on the task text: it says the transcript has 47 units. The transcript had 82 turns; 47 is the number of units the verifier protects (the baseline's "units protected" column). Nothing was lost in translation, and the counts below are the turn counts.

## 1. The review entry (FEEDBACK.md, s11 first note), applied as recorded

The note asks for false starts, screen-navigation filler, one mid-tour interruption, an unfinished sentence, one repeated explanation across the Consultant's long turns, and the "instant principle" reply taking two turns. The second note is stage 1b input and changed nothing here. Edits, in three steps:

**B1, inside existing units (eleven edits, no unit added, no stamp moved).** False starts at 01:49 ("So. Let me -- let me say"), 04:19 ("the salesperson, which is going to be, well, mostly it'll be -- anyway."), 47:34 ("The way it -- so, the boards work on a phone"). Navigation filler at 04:19 ("Now the -- where's it gone. Now the Clients board. Sorry, wrong tab, that's the filter. There."; "Hang on, can you still see this? Desmond? The small screen. Okay. Events."), 13:22 ("Let me just get -- no, that's the event, I want the quote. There."), 22:53 ("hang on, it's -- there"), 38:46 ("Which is -- no, that's Items, sorry, they sit next to each other. Count-in."). One repeated explanation at 19:11: the one-set-of-lines point from 13:22 said again ("the items here are the lines, the same lines, I said this on the quote, the quote's lines are the event's lines, it's one set, so I won't say it a third time"). Two clauses that never finish: 04:19 ("mostly it'll be -- anyway") and 26:26 ("the last thing a crew lead wants at six in the morning is -- well. Nothing else."). A filler "um" at 26:26.

**B2, the mid-tour interruption (two units added).** The tour at 04:19 is split where the count-in story reaches "their job is done, they go home." Desmond interrupts at [10:39] with a question about the mechanism ("Sorry. Hang on. Who's marking that? In the story. Who's actually typing it in?"), and the Consultant answers and picks the tour back up at [10:45] ("The crew lead. On a phone, at the dock, in the story. ... Where was I. Short, damaged. Yes."). Desmond was chosen over Hattie so that the tour's closing line ("Hattie, you said you'd interrupt, and you didn't.") stays true; the question is about who types the count, so it adds nothing to the key's counts of "by truck" (three) or the phone ask (three). Stamps were computed from the word rate: 1,077 words in 380 seconds before the interruption (170 words a minute) and 416 words in 147 seconds after it (170), inside the file's 130 to 175 spread. The tour therefore becomes two own-side stretches; the first part, at 1,077 words, is still the file's longest unit and still the planted "very long single-presenter turn".

**B3, the two-turn reply (two units added, two stamps moved).** The 25:39 turn, which answered Hattie's correction with the principle at once, is now a wrong first attempt ("I'd put a flag on the tent, a sort of warning on the tent rows ... no. Hang on. That's the same column wearing a different hat."); Hattie corrects at [25:55] ("I don't want a warning. I want to know which wedding the tent's already on. The tent and the floor. Not the chairs."); the principle follows at [26:03], trimmed by one clause ("and it's the version I'd have built if I'd asked you instead of Anjali", which no field cited) so that the window to the block fits. To keep the block's stamp at [28:05], which twenty-four citations and the composite-block key point at, Anjali's "Fine. Do the crew board." moved from 26:09 to [26:22] and the crew-board turn from 26:17 to [26:26]; the five turns run at 174 words a minute over the 146-second window, at the top of the spread. The verifier then reported one miss (R8's third evidence at 26:09, found at 26:22). Re-cited: `rubric[7].evidence[2].location` to 26:22; `rubric[0].note` ("restatements at 13:22, 19:11, 26:26 and 38:46"); `intake.quarantine[...].not_quarantined`, whose list of client turns inside the share now reads "25:23, 25:55, 26:22, 37:02". These are the only location references that moved; the fixture's grammar is stamp plus label, so nothing else re-pointed. The rubric edits touch locations only, which section 5 of the brief requires after new turns; no grade, quote or note content changed.

**Counts regenerated after the three steps** (by the same word-splitting method that reproduced the old figures exactly: 8,761 words, 18.4%, the four phase figures and 6,217 showing-window words): 86 turns, 257 lines, 9,006 words; by label Consultant 81.7%, client 18.3% (Anjali 12.9%, Hattie 3.5%, Desmond 1.9%); block 878 words, 9.7% of the file; attributable client 769, our side 7,359, client share of attributable 9.5%; if the segments are confirmed 17.2%; phases 387 words at 35.1%, 1,680 at 2.4%, 4,774 at 25.7% (8.9% attributable), 2,165 at 11.3%; showing window 6,454 words at 19.6%; sixteen " -- " restarts in thirteen turns; ten units at or under four words (unchanged); own-side stretches 1,077 and 416 (the tour), 536 (19:11), 470 (38:46). Written into `purpose_of_this_fixture`, `transcript_format`, `traps[11]` (the tour stretch) and `traps[12]` (the by-label share), `accepted_behaviours[2]`, `expected_leak_blocklist[8]` ('18.3%'), `intake.export_family`, `intake.detectors`, `composite_blocks.28:05.not_composite`, `rejoined_sentences`, `own_side_stretches` (now four), `talk_share` (every figure), `delivery_notes[0]` and `[1]`, and `delivery_notes[3]` (good practice gains the two-turn reply). The transcript stays ASCII with LF endings.

## 2. The `direction` rename

`intake.type_header.direction_of_show` is now `direction` and its sibling `direction_of_show_note` is `direction_note`, in the same positions. `accepted_behaviours[6]`, which said "where direction of show changes", now says "where the direction changes". The README does not name the field, so its prose did not need to follow.

## 3. The seven-pattern sweep

Each hit is a `readiness.structure.leanings` entry; a field was corrected where a builder reading it alone would build the flaw, and left where it was only incomplete.

1. **One row where the call describes many.** Three hits. (a) The ten-by-twenty: one Items row with an owned quantity of two, while Hattie's new 25:55 line asks "which wedding the tent's already on" and 25:23 says "There are two of them." A count cannot name a wedding. Leaning 1: one child row per physical tent and per dance floor section under the item type, the committed count rolling up. `vocabulary["the ten-by-twenty; dance floor sections"]` ("Items rows with an owned quantity, first on the committed column") was left: it is true of v0.2 and only incomplete; the leaning carries the shape and verdict condition 4 says it is decided before the column is finished. (b) The event's six-value status, with Delivered and Collected duplicating what the movements carry; leaning 3 derives the event state from the movements and the count-in. `entities_and_workflows[3]` already labels the six as the Consultant's, unconfirmed, so it stands. (c) The committed count on the event date when a tent is out from the day before to the day after; leaning 2, filed under the shared-resource pattern because the window is the reservation.
2. **A pain with no element that fixes it.** One hit, P5 (venue coordinators), by agreement on the call a question and not a build: `none` in `element_per_pain`, leaning 8, an unmet need. The nearest other candidate, "Half of them have got cracked screens and no data on the weekend" (18:06), is a blocker in the key rather than a pain and is kept as an unmet need (section 5).
3. **An alias-map entry that names more than one entity.** No hit. Eight entries, one person each; the Ferenc entry pairs one person with the seed-data uses of his name, which is a note about position, not a second entity.
4. **Our framing labelled as the client's.** Three hits, all corrected. (a) `vocabulary["short / damaged"]` presented the Consultant's count-in labels as the client's term: no client speaker says "short" or "damaged" on this call; Desmond says "shortage" (44:26) and Hattie "eight chairs" and "cigarette burns" (41:57). The entry now reads "shortage (the client's word); short / damaged (the Consultant's labels)". (b) `vocabulary["the Thursday board / the whiteboard"]` said "the client keeps calling it the Thursday board"; the term is spoken only inside the composite block, side-only; "the whiteboard" is attributed at 51:23. Both fields of the entry now say so, and `vocabulary["count sheet / count-in"]` says "count-in" is ours. (c) `expected_leak_blocklist[11]`, the CAUTION line, listed 'short', 'damaged' and 'the Thursday board' as "the client's own vocabulary"; it now keeps 'shortage' and 'the whiteboard' as the client's and holds the three others until read back. Also under this pattern: `integrations_mentioned[4]` said the spreadsheet is "replaced by the Events board", our assumption about a tool kept by someone who was not in the room; it now says so and points at leaning 9. Leaning 7 collects the vocabulary question. Checked and left: "movement" (already labelled ours), the event labels (already labelled), the venue-as-client-type (ours, labelled in `expected_structures`).
5. **A shared resource with no reservation tracking.** Two hits. (a) The tent across its turnaround window (leaning 2, above). (b) Trucks as four fixed groups with no row for a hired fifth truck ("on a Saturday in June I need five", side-only) and nowhere for a person-and-truck rule to live ("Ade doesn't drive truck three", side-only); leaning 4 proposes a short Trucks list as the group source and keeps the look-alike trap against a Trucks board of work, so `expected_structures.lookalike_traps[3]` stands.
6. **An artefact that can go stale with nothing to flag it.** Two hits. (a) Paper on the truck after the event changes: "the printout in truck three still had him on both" (side-only) and the pick list the Consultant offers to print at 13:22; leaning 5 (printed-at stamp, changed-since-print flag, phone first, paper the client's choice). (b) The owned quantity, which the Consultant himself says goes "quietly wrong" when nobody changes it (19:11); leaning 6 (kept-by and as-of date, a write-off proposed from a Damaged line, an unverified marker on a stale count). The whiteboard photo and the spreadsheet carry `goes_stale` in `entities` with no leaning of their own: both are what the build replaces.
7. **An expected output the input cannot support.** No hit of the kind the pattern means. Checked: every transcript statistic in the key was regenerated (section 1); the dates stay inferred and labelled; the account facts say unknown; 'four trucks' and 'sixteen magnets' stay unconfirmed in `company.size`. One claim of a kind the s21 line covers was found and is in section 5.

## 4. The "never written to" rule

A search of the key for "never written", "written to", "written back", "write back", "writeback", "never touch", "not written", "read-only", "one way" and "book of record" found nothing; s11 is not among the eleven keys FEEDBACK names. One occurrence of the weaker form was reworded: `integrations_mentioned[0]` ("the Consultant states that nothing connects to it in the first version and the client does not object. Not in scope.") now adds "Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours." The readiness block's incumbent entry for the accounting system carries the same wording from the start. No client line on this call says anything about writing to the accounting system; Desmond's "when Bram does the invoices" (44:26) is the only client mention, and it is where the invoices live, not a rule.

## 5. Standing lines where they bite

- **s21 (a commitment is `committed`; done only on evidence).** `commitments_and_next_steps[0].owner` said "the invite to the three attendees was sent during the call at 60:49". On the call the Consultant says "I'm sending the invite to the three of you now, while we're on"; nothing shows it arrived. Now: "the Consultant said at 60:49 that the invite to the three attendees was being sent while on the call: committed, not evidenced as received." The same change in `intake.delivery_notes[3]` ("the invite committed on the call, by the Consultant's own word at 60:49") and `intake.next_close_list[4]` ("with the invite confirmed as received rather than taken as sent"). The R10 note says "the invite sent on the call" and sits in `rubric`, which the brief keeps as v2 material; noted for the v2 pass, not edited. Verdict condition 7 carries the state. No `status` field was added to the commitments array (shared shape).
- **s22 (a board status set by a person is a claim).** Bites three times and is written into the block: a movement status flipped by a crew lead is a claim about where the truck is (leaning 3, `element_per_pain` P3.3); a tick on an open charge is a person's claim that the bookkeeper billed it, never evidence from the accounting system (incumbent 1, `element_per_pain` P4.1); the owned quantity is a typed number (leaning 6). The one live structural change (Sent back at 17:07) is our own action on our own demo board, so it is an event, not a claim about another system.
- **s11 (inference targets questions; it never fills evidence).** Eight `signals`, each naming what our side never confirmed, including the new 25:55 line; four of the five questions are read-backs built on them; the two block-sourced entities whose detail is side-only cite the block location, which the key's own tier rules cap, and nothing from the block is the basis of any clearance.
- **s15 (a product limit never deletes a client need).** Six `unmet_needs` with their clocks: text to crew leads, the scanner, Saturday use on phones without data, the red grid on a phone, the person-and-truck rule, the coordinators.

## 6. The readiness block

Built in the brief's exact shape as the 27th and last top-level field. Counts: pains 9 (the key's nine entries, same quotes and locations, numbered P1, P2, P3.1 to P3.4, P4.1, P4.2, P5, theme number first and a running number after the dot where a theme holds several quotes; P4's two entries are `excavated`, as the key grades P4), signals 8, entities 26 (18 with a parent, all carrying `moves_independently`), leanings 9, element_per_pain 9 (eight `fixes`, one `none`; no `copies-today's-tool`, because the same-day notification and the pick list fix their pains without an integration, and the charge reaching the invoice by hand is recorded as an incumbent, not credited), incumbents 7, assumptions 14, unmet needs 6, AI opportunities 3 (all round 2: the client never asked for AI or workflows; the workflow cites P-21, the agent P-19, the AI column is unprobed), verdict `build` with 7 conditions, questions 5 (4 read-backs, 1 discovery).

Pain outcomes are verbatim client lines (22:46 for P2, the side-only "Yes. Yes, that's the thing. The whiteboard goes." for P3.1 to P3.3, 47:24 for P3.4, 44:26 for P4), proven present in the transcript by the edit script; P1 and P5 carry null, because no client words aim at an outcome for them.

Build target `own-account`, reason "prospect, so the user's own account by default (A21)": the client has no account, the demo ran in the Consultant's own, and the owner has seen nothing. Workspaces "Quillhaven – CRM" and "Quillhaven – Ops" with the brief's en dash, so the key is now UTF-8 (the transcript stays ASCII). Products CRM and Work Management; native reuse Deals/Opportunities as Quotes, Accounts as Clients, Contacts for coordinators only once asked; the Work Management boards built new in the Ops workspace, nothing copied from the demo account. The key's first pre-build question (which account) moves to handover under A21 and is not one of the five; its second, third, fifth, sixth, ninth and eleventh are reused in build terms across the five.

`should_plugin_propose_a_build` is true and the readiness verdict is `build`, so the note needs no second sentence. `rubric`, `expected_verdict` and `numbers` are untouched except for the two location references of section 1. A regex search over the block for R-numbers, grades, gate names and verdict words found one word, "missing", inside the client's own quote "That's the missing dance floor." (P1); it is the client's word and stays.

## 7. README and coverage row

README: the files table (257 lines, 86 turns, 9,006 words, the by-label shares, the longest turn 1,077 at [04:19] with the interruption named; the key 27 fields, 548 lines, `readiness` last), the planted-defects row for the long turn (two stretches split by one client question), the quote count (151 counted by the verifier plus the gap answer under `answer`, which is why the old line said 121 against the row's 120), the own-side stretch count (4), a new readiness-count line for the COVERAGE row, the conventions bullet on the mess (what the fix pass added and which two stamps moved), the review status (reviewed by the user 2026-09-21, kept) and the one-sentence fix-pass line. `coverage-row.md` holds the row: only Quote strings (120 to 151) and the Review column moved; every other count was re-measured from the edited key and is unchanged.

## 8. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 9 |
| signals | 8 |
| entities | 26 (18 with a parent) |
| leanings | 9 |
| element_per_pain | 9 (8 fixes, 1 none) |
| incumbents | 7 |
| assumptions | 14 |
| unmet needs | 6 |
| AI opportunities | 3 |
| existing fields corrected | 9 (three vocabulary entries, the leak list caution line, two integrations lines, one commitment owner, one delivery note, one next-close item), plus the direction rename and the count refresh |
| transcript edits | 11 in-unit edits, 4 units added, 2 stamps moved; 82 to 86 turns; 8,761 to 9,006 words |
| key size | 548 lines, from 395; 27 top-level fields |

## 9. Verifier output

`python3 -I verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s11-demo-composite`, run after all edits, exit code 0:

```
Fixture: s11-demo-composite
Sources: transcript.txt (transcript/header-bracket, 86 units)

pairs found      151
verified         151  (of which presence only, no location cited: 25)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were reported. `--spans` lists 48 protected units carrying 68 spans (from 47 and 64). The composite block's nine segments were re-checked by the verifier's segment test on every block citation (segment starts and ends unchanged, since no edit touched the block), and the README's planted-defect table still points at [28:05] for the block, at [04:19] and [10:45] for the long turn, and at the unchanged stamps for the ties and the close.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | The whiteboard gone before the Larchmere Hall contract starts in March | 51:23 Anjali Venkataraman (General Manager) | P3.1, P3.2, P3.3, P3.4 |

Assumption kinds: leaning 6, gap 6, call-type 1, board-architecture 1.

Verifier: 151 pairs, 151 verified, 0 misses and 0 near-misses before; 152 pairs, 152 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G1 is the general manager relaying the owner's March deadline for the whiteboard, kept because she adopts it in her own voice ("Before March."), cited at 51:23 rather than inside the composite block; the sales manager's "I want to know which wedding the tent's already on" and the warehouse manager's same-day shortage line were left out as the wanted outcomes of single pains (P2, P4), and the block-attribution assumption is tagged call-type, as s9 did for inferred speakers.
