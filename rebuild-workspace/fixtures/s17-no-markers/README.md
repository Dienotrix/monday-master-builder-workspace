# s17-no-markers (calibration fixture, C59)

A first-hand discovery call with a wholesale plant nursery, exported by a meeting-assistant tool as a block export that marks nothing. There is no bracketed cue, ellipsis, dash or "inaudible" anywhere in the file, and every fragment carries a confident full-name label; the file is nonetheless heavily shredded and holds one composite block. The key asserts the repair: the absence of markers raises the doubt level instead of lowering it, grading runs per turn rather than per file, and evidence from the repaired block is capped at Partial until the user confirms who spoke. Fictional client, people, figures and dates; everything in it is invented from the parameters in BUILD-PLAN.md section 4.2 and REAL-CALL-LESSONS.md C59 and from nothing else.

## Files

| File | What it is |
|---|---|
| `transcript.txt` | Plain text, 779 lines: a header line `Speaker Name MM:SS` above one text line per turn, blank line between turns. 260 turns, 00:03 to 33:54, about 5,683 spoken words. No participant header, no call date, no end times. |
| `answer-key.json` | The 25 fields in the s1 to s10 order, plus an `intake` block and, since the fix pass, a `readiness` block (`readiness/1`) as the last field. 530 lines. |

Give the plugin `transcript.txt` alone. Every location in the key is `turn N, MM:SS, Speaker Name`, with turn N the Nth header line; evidence from inside the composite block is `turn 183, 21:36, labelled Teodora Okoro, segment k (side-only)`. A quote never crosses a label; a sentence whose first word sits under another label is quoted from the owner's turn, starting lowercase.

## The planted defects and what the key asserts

| Defect | Where | What the key asserts |
|---|---|---|
| Zero artifact markers | whole file | `intake.markers` records 0 of every kind and `doubt_level: raised`; the report says the shred and composite signals raised it. A run that treats the clean surface as a clean file fails. |
| Heavy shred, tails | 33 turns begin with the previous speaker's closing word(s); turn 104 (`right`) may | Each is re-joined to the turn carrying the semantic bulk at probable; 104 is held as "boundary artifact, owner unresolved" and never re-attributed. The load-bearing ones: 213 `invoicing.` (Ilse's blocker), 197 `counting.` (our tail, not her assent), 63 `looked.`, 188 `drifts.` |
| Heavy shred, heads | 10 Consultant turns end with the next speaker's opening word (48, 56, 81, 100, 129, 146, 171, 200, 210, 238) | The three most load-bearing pain statements (P1 Stated at 57, P2 Stated at 101, R6 at 172) begin this way and are quoted from the client's turn alone; the heads are never read as our speech. |
| Split figures | 39/40 across labels; 95/96 same label; 146/147 across labels | Joined at the lower confidence, logged, cited only as reconstructions; the bleed is quoted from turn 192 where the sum is whole. |
| One composite block | turn 183, 410 words, 21:36 to 24:31, labelled Teodora Okoro | Six segments marked speaker-unresolved; the decisive signal is the second-person address to the label; the words-against-wall-clock signal does not fire (141 wpm). Nothing is attributed to the label; client segments are cited side-only. |
| The cap | R7 and P3 Workaround rest on the block | R7 grades Partial (Met if the block is attributed to its label, Missing if it is discarded; both wrong), so the verdict is Nearly ready; on confirmation of the speakers R7 and P3 Workaround regrade Met and the verdict becomes Discovery complete. |
| Per turn, not per file | Teodora's clean turns (57, 62, 132, 172, 192, 232) | Certain and Met; a file-level downgrade fails. |
| Talk share | block is 7.2 percent of words | Refused, with the reason; per-side counts that exclude the block and say so are acceptable. |

Genuine speech that a label-pattern rule would wrongly repair: 15, 25, 32 and 140 are one speaker completing or echoing another and are left as they are.

## Counts for the COVERAGE.md row

- Rubric rows: 30. By status: 21 met, 6 partial (R5, R7, R12, P2 Cost inputs, P3 Workaround, P3 Cost inputs), 2 missing (R11, P3 Trajectory), 1 met-with-residual (R4). Every row carries `asked` (28 true, 2 false). `not-obtainable` and `advisory` are not exercised.
- Graded pains: 3 (P1 the avail sells what is not there, P2 production grows blind, P3 quotes lost in the sent folder); 2 excavated (P1, P2); P3 becomes excavated when the block's speaker is confirmed. `pains` array: 11 entries (P4, the twice-weekly hand-built list, is stated and not graded).
- Numbers: bleed met-with-residual, "Eighty thousand. Call it eighty." (about $81,000: $44,200 sales time confirmed, about $20,800 credits guessed, $16,000 waste guessed); upside partial, the chain's conditional $180,000 a season that the client refuses to count.
- Objections: 8. By spec name: Team won't adopt it 2, Must check with someone 1, We'll build it ourselves 1, Price feels high 1, Just send a proposal or pricing 1, Wrong time, next quarter 1, Outside the map 1.
- Traps: 27. Look-alike traps: 6. Leak block list: 14 entries, including one "flag, do not remove" group.
- Requested changes: 2 add, 3 change, 0 remove (pre-build requirements; no build exists).
- Commitments: 8. Pre-build questions: 10. Vocabulary: 15. Accepted behaviours: 15.
- Quotes: 160 quote-and-location pairs after the fix pass by `fixtures-work/_fixpass/verify_quotes.py` (122 before the readiness block, 32 of them presence-only), zero misses and zero near-misses; the readiness block's 38 pairs use the same location grammar. The earlier figure of 113 checked strings (90 with a location, 23 quote-only, plus `account_context.evidence_quote_or_null` and the intake quotes) is `fixtures-work/_work-s17/check.py`'s count of the 25 fields and the intake block, and still holds for them.
- Verdict: Nearly ready. Gates: Solution blueprint met, Build met, First demo (v0.1) met, Pricing or proposal prep not met, v1.0 sign-off not met. `should_plugin_propose_a_build` true.
- Products: Work Management (availability from bed counts, orders, despatch) plus CRM (quotes on native Deals/Opportunities, Accounts, Contacts conditional). Native boards required: 3. `portfolio_expected` false (no account, no tier). Tier unknown.
- Readiness block (`readiness/1`, fix pass 2026-10-13): 11 pains (the key's eleven entries, numbered P1.1 to P1.4, P2.1, P2.2, P3.1, P3.2, P4, P5, P6), 6 signals, 27 entities, 8 leanings, 11 element-per-pain rows (3 `none`), 7 incumbents, 15 assumptions, 7 unmet needs, 4 AI opportunities (all round 2), verdict `build` with 6 conditions, 5 questions (2 read-backs). Build target own-account; workspaces one per product.
- Intake block: block export, no end times, no header; markers 0 of every kind, doubt raised; 1 composite block with 6 segments (4 client-side, 2 our side); 44 fragment entries (43 re-joined, 1 unresolved); 4 genuine completions left alone; 3 re-joined figures; 6 refused quotes; 3 question-answer pairs kept; 4 alias-map entries; 0 wedges (family cannot produce them; the report says so); talk share refused; 3 second-hand items; type header `discovery`, `partner-led`, `new-logo`, `no-show` (the `direction` field, renamed from `direction_of_show` in the fix pass), `configured-structure`.

## Conventions and deviations worth knowing

- Location form `turn N, MM:SS, Speaker Name` is new to the set (s9 uses `paragraph N`, s16 `cue N`), because this export's timestamps are start-only and the turn is the unit the pipeline works on.
- The key uses `met-with-residual` and the per-criterion `asked` flag. It does not exercise `not-obtainable` or `advisory`; other calibration fixtures carry `not-obtainable`, and no calibration fixture carries a positive `advisory` row, because every fixture's type resolves; the value's positive case is the constructed unresolvable fragment of BUILD-PLAN.md section 4.3, item 8 (H50).
- Call type and the type header use the tokens `shared/record-map.md` pins for the type header (the ARCHITECTURE.md 8.3 step 5 values in their hyphenated form, with the fixture's reasoning in a `_note` beside each field) and the labels of 7.1 verbatim.
- Tool references are category words throughout, one category per sentence: the accounting system, a spreadsheet, a free task app, a phone, a clipboard.
- Dates are relative and fit October 2026: the call early in the month, the walkthrough Tuesday 13 October at 16:00 local, the credits list by the Friday after the call. No transcript states its own date. Plant cultivar names are invented.
- To stay under the 400-line budget, every list entry is printed on one line. The field set and order are unchanged from s1 to s10.

## Review status

Written to its row in BUILD-PLAN.md section 4.2 and to C59 in REAL-CALL-LESSONS.md section 6, and to nothing else. Adversarially reviewed 2026-09-20 (WP18): every quote re-verified verbatim at its location; two transcript consistency defects repaired without touching a cited quote (the boxwood arithmetic at turn 66, and turn 184 naming the thirteenth before turn 240 sets it), fourteen disfluencies added on turns that carry no quoted string, and the key's speaker-change count, gap claim, turn-2 attribution and turn-184 quote corrected. Reviewed by the user 2026-10-10 (FEEDBACK.md: keep, one item unclear; the 'First demo (v0.1)' gate wording is stage 1b input, not a fixture change, so the key's gate lists stand as v2 material). Fix pass applied 2026-10-13: the `readiness` block was added as the last field, `direction_of_show` became `direction`, every claim that the accounting system is never written to was reworded as unresolved with staying clear of it labelled as our default, the walkthrough was recorded as committed rather than held with the bookkeeper to be asked, three vocabulary entries were corrected from the structure sweep, the talk-share figures were recomputed, and a mess pass added 71 words of false starts and repeats inside eleven existing turns, none inside a cited span, so the turn count, numbering and stamps are unchanged and all 160 quote pairs verify.

At stage-1 acceptance (2026-09-20) the type-header values in `answer-key.json` were re-spelled as the tokens `shared/record-map.md` pins, with each value's prose moved to a `_note` field beside it; no quote, location, grade or count changed.
