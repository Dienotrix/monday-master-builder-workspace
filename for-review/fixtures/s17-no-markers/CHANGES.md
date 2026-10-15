# s17-no-markers — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s17-no-markers/answer-key.json`, `fixtures/s17-no-markers/transcript.txt` (mess pass only, inside existing units) and `fixtures/s17-no-markers/README.md`. Work files beside this log: `keystyle.py` (the dumper that reproduces the key's own layout), `build_key.py` (every key change, in the brief's order, with a verbatim proof of every quote the block introduces before anything is written), `mess_pass.py` (the transcript edits, anchored on the old text of each line) and `coverage-row.md`.

Method for the key: load with ordered dicts, change, dump. The key's layout is not plain `indent=2` (objects inside arrays sit on one line, and a deeper object is spread only when it holds a list), so `keystyle.py` encodes that rule; a round trip of the untouched file reproduced it byte for byte before any change, and `build_key.py` asserts the same before it runs. The 25 fields keep their order, `intake` stays 26th and `readiness` is the 27th and last top-level field. The key was ASCII before and is UTF-8 now, because the workspace names carry the en dash the brief shows.

## 1. The review entry (FEEDBACK.md, s17 entry of 2026-10-10)

No fixture change. The entry's verdict is "keep, one item unclear": the user read "First demo (v0.1)" under `gates_met` as though the demo had happened. The disposition proposed renaming the gate pair across all keys, and the status line settles it as stage 1b input, not a fixture fix: the gates are v2 under A19, so the rename waits, and the lesson (say what the user is cleared to do, never a bare "met") went into the readiness check's `cleared_for` values instead. The brief also says s17 has no fixture changes. `expected_verdict`, its gate lists and `rubric` are therefore untouched here, and the README's review line says why.

## 2. The `direction` rename

`intake.type_header.direction_of_show` renamed to `direction`, in place (fourth key of the header, value `no-show` unchanged). It appears once in the key; the README named only the values, not the field, and now names the field once in its intake line so a reader knows the rename happened. `grep direction_of_show` over the fixture folder finds nothing.

## 3. The seven-pattern sweep

Each hit became a `readiness.structure.leanings` entry. Where the hit sat in an existing field and a builder reading that field alone would build the flaw, the field was corrected too; where the field was only silent, the leaning carries the addition (brief section 8, fourth rule).

**One row where the call describes many.** Two hits, and one shape already right.
- Orders. The key says "orders and reservations against the same lines" and the vocabulary puts a substitution "on the order line", but nothing says an order is a parent with one row per line, and `standing order` reads "item on the Orders board" with one status. The call has lines moving on their own: a substitute cultivar for part of an order (turn 66), a signed pick list "with anything refused crossed off" (turn 156), an order changed after the pick list is printed (turn 54). Leaning 1: order as parent, order lines as child rows connected to availability lines, status per line. No field corrected: nothing there was wrong, only incomplete.
- The chain's season-ahead pre-order (turns 136, 138): an order against planned production, not a counted bed, which "orders against the same lines" does not cover. Leaning 8, out of the first version until the trial is confirmed.
- Already right: bed counts rolled up to product lines. The stock module failed because "the system wants them by product" (turn 124), and the key's vocabulary and products already put counts by bed under the line. Recorded as the first roll-up pattern, not a hit.

**A pain with no element that fixes it.** Three `none` rows in `element_per_pain`, two of them leanings.
- P1.4, refused deliveries that sit on the dock (turns 156, 157). The key records the refusal but nothing returns the plant to stock or tells the grower. Leaning 6 and an unmet need.
- P5, parks purchase-order numbers in the sales coordinator's spreadsheet (turn 159). The key calls it a backlog seed; a column on the order is the obvious element, but the coordinator has not been met. Leaning 7 and an unmet need.
- P6, escalations go to the owner by default (turn 79). `none`, with no leaning: no structure changes whose number the customers have, and the pain eases only through P1's own element. Writing a leaning for it would be forcing one.

**An alias-map entry that names more than one entity.** No hit. The four entries (the owner, the sales coordinator, the bookkeeper, the hypothetical customer contact) each resolve to one person. The nearest candidate is `mentioned_not_present`'s "three drivers and four crew leads (unnamed)", which is a roster list, not an alias entry, and stands.

**Our framing labelled as the client's.** No hit. Checked and left: the play-back at turn 231 is labelled ours in R12 and the client's additions are quoted from them; the owner's tablet test is marked relayed; the office coordinator as the account's administrator is the client's own choice (turns 257, 258). The nearest candidate is the word "reservations", which is the Consultant's (turn 231) where the client says "spoken for" (turn 164) and "promised" (turns 169, 188); the key never attributes it to the client, so no field moved, and the block's `entities` row for the reservation carries `source: assumed` and says whose word it is.

**A shared resource with no reservation tracking.** One hit, one candidate declined.
- Stock promised on a live quote. "I could be holding four hundred Thuja for a bid that lost, or I could sell them to a garden centre and the bid wins. I don't know which." (turn 188). The key puts quotes on the Deals board with lines "as subitems or a connected board" and never connects them to stock, so the grower would still not see what is promised. Leaning 3: quote lines connected to availability lines, shown as promised without dropping the line, with whether a quote should hold stock as the condition the client has not answered.
- Trucks and drivers ("Three drivers, two trucks and a van", turn 156) are reused across orders and Thursdays are the big day, but no pain or need on the call touches despatch scheduling; inventing one would be our framing. The entity row records the fact with `shared_resource: true` and nothing is built on it.

**An artefact that can go stale with nothing to flag it.** Three hits, two of them in fields that were corrected.
- The emailed list itself ("So it's wrong before it's sent.", turn 46). The client requires the email to continue (turn 235), so the fix is not to remove it but to stamp it and to check confirmations on the board. Leaning 4. **Field corrected:** `vocabulary["the avail"].likely_monday_object`, which read "plus the emailed export of it" and would have rebuilt the undated snapshot; it now names the count-date and send-time stamp and says a confirmation is checked on the board.
- The bed count's age. A Friday count is Wednesday's problem (turns 31, 103), and the build does not make counting more frequent. Leaning 5. **Field corrected:** `vocabulary["bed / bed count"].likely_monday_object`, which had no date on the count item; it now carries the date it was counted.
- The order record itself. Today the sales order is keyed in the accounting system and the pick list prints from it (turn 35); the build puts orders on a board; the accounting system stays for invoicing (turn 212). Keyed in both places, the Orders board is the stock module's failure again ("So I was typing it twice and it was still wrong.", turn 124). Leaning 2 leans to keying once on the board with the office coordinator raising the sales order and invoice from the signed pick list, as she invoices today, and names the condition (whether the accounting system needs the sales order first). No field corrected, because no field says where the order is keyed; the question is in the five.

**An expected output the input cannot support.** No hit. The transcript statistics in `transcript_format` and `intake.export_family` were recounted after the mess pass and the ones that moved were updated (section 7): 260 turns, 779 lines, non-decreasing stamps with no collisions, exactly one adjacent same-label pair (95 and 96), 49 lowercase-initial turns, 51 without terminal punctuation, 44 at or under four words, the block at 410 words and the next-longest turn at 177, no bracket, ellipsis, double hyphen or parenthesis and no artifact word anywhere, ASCII only. The absolute dates are labelled inferred. The one output that only the user can supply (who spoke the block's segments) is a question to the user, as the key already has it.

## 4. The "never written to" rule

s17 is one of the eleven keys FEEDBACK's s14 entry names. Four occurrences, each resting on the client's "the accounting system stays" (turn 212) and the Consultant's own "Nothing I'd propose touches invoicing" (turn 213), neither of which is a no-write statement:
- `integrations_mentioned[0]`: "stays as the invoicing system and is never written to" became "stays as the invoicing system in the client's words ('And the accounting system stays.'); writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours".
- `compliance_or_security_signals[3]`: "and must not be written to" became the same unresolved wording, with what the client did say in brackets.
- `requested_changes[2].description`: "and nothing writes to it" became the rule's wording; the client quote on the entry is unchanged.
- `expected_structures.notes`: "the accounting system is never written to" became "stays the invoicing system, with writeback and integration direction unresolved ...".

Checked and left: `expected_monday_products[0]` ("The accounting system stays for invoicing") and `account_context` ("the only system of record"), which are the client's words. The R9 note in `rubric` uses "staying for invoicing" and is v2 material in any case. The block's `existing.incumbents` entry for the accounting system and leaning 2 carry the same unresolved wording.

## 5. Standing lines where they bite

- **s21 (a commitment is `committed`, done only on evidence).** `commitments_and_next_steps[0]` said the walkthrough was "with Teodora, Rasmus, Ilse and the owner, the bookkeeper invited" and its owner "Teodora brings the owner". On the call the invite is still to be sent (turn 243), Teodora will forward it (turn 244) and the bookkeeper was offered by Ilse "if you want her" (turn 242) and never asked. Now: "Committed on the call: ... the owner to be brought by Teodora once the invite reaches him (attendance not yet confirmed); the bookkeeper to be asked by Ilse (offered at turn 242, not confirmed with her) ... Nothing is sent or confirmed yet", with the owner field saying who sends and who forwards. The same state is a verdict condition. The R10 note's "the bookkeeper invited" sits in `rubric`, untouched as v2 material; noted for that pass. No `status` field was added, since that would change the shared shape of the array across the set.
- **s22 (a board status set by a person is a claim).** Bites on the Orders board. `vocabulary["standing order"]` read "a cancelled status that notifies the grower"; it now says who sets it (whoever reads the chain's email) and that the status is a claim about the email, not evidence of it. The P2.2 element row says the same; leaning 2 keeps the accounting system's own records as the record of invoicing.
- **s11 (inference targets questions, never fills evidence).** Six unconfirmed client signals are in `signals`, two of them from the composite block cited side-only, and they drive the two read-back questions (Q1 to the owner in person, Q4 to the sales manager and grower). None appears as evidence or in an element. One entity (the reservation) is `source: assumed` with the client's own words named instead.
- **s15 (a product limit never deletes a client need).** Seven `unmet_needs`: phone entry in the rain with gloves (turn 253), the Monday email to about a hundred and forty customers without typing, prices invisible to leads (tier unknown), no training for a different forty seasonal people (turn 223), refused deliveries, parks purchase-order numbers, and credits with a reason. Each keeps its clock where the client gave one and says why the first version does not meet it.

## 6. The readiness block

Built in the brief's exact shape from the key's own content. Counts: pains 11, signals 6, entities 27 (19 with a parent, every one with `moves_independently`), leanings 8, element_per_pain 11 (eight `fixes`, three `none`, no `copies-today's-tool`), incumbents 7, assumptions 15, unmet_needs 7, ai_opportunities 4 (all round 2, because the client never asked for AI or workflows; the workflow cites P-21 and the agent P-19; the two AI columns are `unprobed`), questions 5 (two read-backs, three discovery), verdict `build` with six conditions.

**Pain ids.** The key's `pains` array holds eleven entries under themes P1 to P4 and three unnumbered ones. Per the exemplar rule they are numbered P1.1 to P1.3, P2.1, P2.2, P3.1, P3.2 and P4 in array order; the refused-deliveries entry, whose theme says "folds into P1", is P1.4; the parks purchase-order entry is P5 and the escalations entry P6, the next free numbers. P1 and P2 entries are `excavated` as the key grades them, P1.4 is `stated` because only the quote is folded in, and P3, P4, P5 and P6 are `stated`. Outcomes are verbatim from the three R6 answers (turns 172, 174, 176) where they aim at the pain; P1.3, P1.4, P3.1, P3.2, P5 and P6 carry `null` because no outcome words aim at them, and P3's clearance does not need one.

**Signals.** The owner's tablet test (relayed, turn 179), the decision threshold (block segment 3, side-only, `pain: null` because it is about the decision process rather than a pain and is the fixture's central unconfirmed signal), the forty live quotes (segment 1), the closed yes at turn 187, the chain's figure (turn 135) and the sales coordinator's predicted resistance (turn 225).

**Structure.** Products Work Management and CRM in the client's order; `own-account` because the nursery is a prospect with no account of any kind (A21); workspaces "Fenwater – Ops" and "Fenwater – CRM"; native reuse is the Deals/Opportunities board relabelled Quotes and the Accounts board, Contacts only if asked. Three roll-up patterns (product line with bed counts; order with order lines; quote with quote lines). The key's existing account question ("Which account will this go in...") is not among the five under A21 and `existing.account` says it moves to handover; the key's own pool of ten questions is left as it is.

**Verdict.** `build`: three pains carry an entity and a wanted outcome in the client's words, the products are chosen, the structure is stated with its leanings and the target is named. Conditions: the approval stop first; no A11 question first matters for an own-account build and the three A11 decisions stay open; the user confirms the block's speakers before the decision process is treated as attributed; leaning 2 answered or carried as an assumption and said so on the card; the walkthrough committed, not held; seeds only from the files once they arrive. The key's `should_plugin_propose_a_build: true` and its "Nearly ready" verdict do not disagree with the block, so the `note` is the brief's two sentences alone. No R-number, grade, gate name or verdict word is in the block (the script searches for them before writing).

**Questions.** Q1 read-back to the owner in person (the whole decision passage, which exists only side-only); Q2 discovery to the office coordinator (where the order is keyed, leaning 2); Q3 discovery to the grower (the bed model and count rhythm, pool items 3 and 4 and leaning 5); Q4 read-back to the sales manager and grower (quotes against stock, leaning 3, and who described the workaround); Q5 discovery to the office coordinator and sales manager (the emailed list and prices, pool items 5 and 6). Dropped from the five and kept as assumptions with their questions: reservations and the fifty-unit rule (pool item 7), substitutions and credits (item 8), the quote fields (item 9), seeds (item 10, routed to the user), the account (item 2, A21). Pool item 1 (who spoke the block) is to the user and sits in the verdict conditions.

## 7. Transcript: the mess pass

The s11 rule, applied with judgment inside existing units: eleven turns gained 71 words of false starts, repeats and a half-explanation said twice, eight on the Consultant's side (turns 9, 90, 100, 127, 186, 204, 231, 245) and three on the client's (turns 18, 42, 199, where the reviewer had flagged writer-clean client speech). Every edit is anchored on the old text of its line in `mess_pass.py`; none sits inside a cited span (the `--spans` listing was read first and the Consultant's five protected spans, at turns 9, 184, 231, 243 and 250, are untouched); no turn's first character, terminal punctuation or four-words-or-fewer status changed; no bracket, ellipsis, dash, parenthesis or artifact word entered the file, because the fixture's point is zero markers. 260 turns, 779 lines and every stamp are as they were. The verifier was run after the transcript edit and again after the key edit: zero misses, zero near-misses, no location notes.

Counts that moved with the words, updated in the key: `transcript_format` ("about 5,683 spoken words", from 5,612), `intake.export_family.words` (5683), `intake.composite_blocks[0].share_of_file_words` (0.072, from 0.073), `intake.silence.talk_share.reason` and `traps[5]` ("7.2 percent", from 7.3), and `talk_share.if_computed_anyway` (about 69 percent client with the block counted under its label, unchanged; 66 percent with it excluded, from 67). The shred and density figures (49, 51, 44, one adjacent same-label pair, 410-word block, 141 words per minute) were recounted and did not move.

## 8. README

Brought in line: the transcript word count; the key described as 25 fields plus `intake` and `readiness`, 530 lines (from 387); the talk-share figure; a Readiness block line in the counts; the quote line now gives the verifier's 160 pairs with the earlier `check.py` count kept as what it measured; the intake line names the `direction` rename; the review status gives the user's review of 2026-10-10 and its disposition, and the one-sentence review-history line "Fix pass applied 2026-10-13: ...".

## 9. Coverage row

`coverage-row.md` holds the full thirteen-column row. Every count was re-measured from the edited key and matches the existing row except Quote strings, 122 to 160 (the block's 38 pairs). The Review column reads "reviewed 2026-10-10; fix pass applied 2026-10-13": the true review date from FEEDBACK rather than the brief's sample date, flagged there for the merge step.

## 10. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 11 |
| signals | 6 |
| entities | 27 (19 with a parent, all with `moves_independently`) |
| leanings | 8 |
| element_per_pain | 11 (8 fixes, 3 none) |
| incumbents | 7 |
| assumptions | 15 |
| unmet needs | 7 |
| AI opportunities | 4 (all round 2) |
| existing fields corrected or reworded | 11 (`vocabulary` x3, `integrations_mentioned`, `compliance_or_security_signals`, `requested_changes`, `expected_structures.notes`, `commitments_and_next_steps`, `traps[5]`, `transcript_format`, four intake values, one intake key renamed) |
| transcript edits | 11 turns, +71 words, 0 new units |
| key size | 530 lines, from 389 (`wc -l`; the README had said 387) |
| verifier pairs | 160, from 122 |

## 11. For the planner

- The key's `rubric` R10 note still says "the bookkeeper invited"; v2 material, left as the brief requires.
- The brief's Review column text gives 2026-10-13 as the review date; s17's user review is dated 2026-10-10 in FEEDBACK, and the row carries the true date. One decision for the merge step if the column is meant to carry the fix-pass verification date instead.
- `signals[1]` carries `pain: null` because the decision threshold is not tied to a pain. If the verifier wants a pain id on every signal, the nearest is P3.1 (the passage sits inside the quote workaround), but that would be a stretch.

## 12. Verifier output

`python3 -I fixtures-work/_fixpass/verify_quotes.py fixtures/s17-no-markers`, run from `rebuild-workspace` after every edit above; the final run:

```
Fixture: s17-no-markers
Sources: transcript.txt (transcript/header-time-last, 260 units)

pairs found      160
verified         160  (of which presence only, no location cited: 32)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
refused_quotes   6 entries in 1 list(s) are the key's own refusals and are not checked
exit code 0
```

No location note was reported (the `--json` report lists 160 pairs, all `verified`, none carrying a note), so no citation needs re-citing.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | The avail actually right by the first week of February, when the chain orders | turn 142, 16:36, Teodora Okoro | P1.1, P1.2 |
| G2 | Look at a line, say yes, three hundred, Thursday, and not phone anybody | turn 172, 20:18, Teodora Okoro | P1.1, P1.2, P1.3 |
| G3 | See what's sold before he pots on | turn 174, 20:29, Rasmus Wrenfield | P2.1, P2.2 |

Assumption kinds: gap 6, leaning 5, board-architecture 3, automation-condition 1.

Verifier: 160 pairs, 160 verified, 0 misses and 0 near-misses before; 163 pairs, 163 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G2 cites the sales manager's second sentence at turn 172 ("I want to look at a line…"), which is whole inside her turn, rather than the key's R6 line "want to say yes…", whose first word sits under our label at turn 171; no goal comes from the turn 183 composite block, so the owner's bed-twelve test (relayed at turn 179 and repeated inside the block) and the office coordinator's Mondays back (the outcome of the single pain P4) were left out.
