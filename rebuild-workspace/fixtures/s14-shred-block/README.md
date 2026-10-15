# s14-shred-block

**Calibration fixture.** The block-export shred case: REAL-CALL-LESSONS.md C58a, BUILD-PLAN.md section 4.2 row s14, headless run H42. Reversal guarded: none. Written from those two parameters and nothing else; the client, its people, figures and dates are invented.

## Files

| File | What it is |
|---|---|
| `transcript.txt` | Block export, 415 units on 829 lines, `M:SS Label: text`, one unit per line with a blank line between. Start-only, unpadded, variable-width stamps. No header, no call date, no end times. |
| `answer-key.json` | The 25 reviewed fields in the s1 to s10 order, plus an `intake` block asserting the repair and, last, a `readiness` block (`readiness/1`, added in the fix pass of 2026-10-13). 503 lines; UTF-8 since the fix pass (one en dash, in the workspace name). |

## The call

A discovery call with Norhaven, an event services company (sound, lighting, video, staging and crew for about four hundred and twenty shows a year; sixty on the payroll, a hundred and forty freelancers; two warehouses). Three client speakers: the operations director (Meera Ganguly, approver up to thirty thousand), crew and logistics (Dermot Shanley), and the warehouse lead (Aileen Rusnak, dialling in from the floor). The managing director and the finance manager are absent. The client's own bleed is a hundred and seventy thousand a year in pounds; the build is Work Management for shows, kit on the show, the crew grid and check-in, with the client's hire system left as the book of record. Currency is pounds. Weekday clues fit the last days of September 2026; the next step is Tuesday 6 October at eleven.

## Planted defects and the repair the key asserts

| Defect | Where | Repair asserted |
|---|---|---|
| Unpadded, variable-width, start-only stamps | throughout (`0:02` to `59:07`) | family and dialect measured before reading; no timestamp shape assumed |
| Five colliding stamps | L119/L121, L243/L245, L277/L279, L367/L369, L463/L465 | recorded; never used to order, merge or drop a unit; stamp plus label stays unique |
| One out-of-order fragment | L449 (31:12) then L451 (31:09) | nothing reordered; the sentence re-joined for Dermot across the interposed unit as `[Q/recon]`; not quotable as one string |
| Lowercase-initial units (40) and unterminated units (32) | throughout | shredded sentences re-joined to their true owners in the intake record; each quoted from its own unit; nothing joined across a label |
| Fifty-seven units of four words or fewer | throughout | fragments may corroborate and never originate; the answer half of an adjacent question-answer pair is kept with both unit numbers |
| Single-letter unit `s` mid-sentence under the wrong label | L367, between Dermot's L365 and L369 | boundary artifact, owner unresolved; never re-attributed; excluded from talk share; Dermot's sentence quoted from L369 alone |
| Headline figure split across three units and two labels | L463 / L465 / L467 | reconstructed for Dermot as `[Q/recon]` at the lower confidence; the grade rests on Meera's whole token at L469 |
| Composite block under one client's label | L205 (174 words, 96 s) | composite splitter fires on measured unit length; six side-only segments, nothing attributed to Meera, evidence capped at Partial; wedge flagger ran; not evaluable, no end times (missing observability, never "found nothing") |

## Counts

Rubric rows: 36 (27 met, 2 met-with-residual, 3 partial, 3 missing, 1 not-obtainable; no advisory row, because the call type resolves). Every row carries the `asked` flag.

Pains: 10 listed, 4 graded (P1 to P4), 3 excavated (P1, P2, P3).

Objections: 12 (Must check with someone 3, Wrong time next quarter 2, Team won't adopt it 2, We'll build it ourselves 1, Talking to other partners 1, monday itself is the problem 1, Outside the map 2).

Traps: 30. Leak blocklist entries: 15. Requested changes: 2 add, 4 change, 1 remove. Look-alike traps: 7. Native boards required: 0 (Work Management only, by design). Portfolio expected: false (no account, tier unknown). Questions before building: 10. Accepted behaviours: 14. Vocabulary entries: 16.

Intake block: 1 composite block (6 segments), 0 wedges, 5 timestamp collisions, 1 inversion, 1 single-letter turn, 14 re-joined sentences with owners, 8 refused quotes, 4 question-answer pairs kept, 4 split numbers, 2 alias entries, 3 relayed or sourced figures, 0 unit-unresolved figures.

Verdict: Discovery complete. Gates met: Solution blueprint, Build, First demo (v0.1). Not met: Pricing or proposal prep, v1.0 sign-off. `should_plugin_propose_a_build`: true.

Readiness block (fix pass, 2026-10-13): 10 pains (P1.1 to P6.1, the key's ten entries with their own quotes), 6 signals, 24 entities, 9 leanings, 3 patterns, 10 element-per-pain rows (7 fixes, 1 copies-today's-tool, 2 none), 6 incumbents, 14 assumptions, 7 unmet needs, 4 AI opportunities (all round 2), 5 questions (2 read-backs, 3 discovery); cleared for `build`, target `own-account`, one workspace, Work Management only.

## Measurements (for the COVERAGE.md row)

About 6,450 spoken words; client share about 60 percent by words (Meera 28.5, Dermot 17.5, Aileen 14.3); longest own-side unit 72 words (L21); longest unit 174 words (L205); one adjacent same-label pair (L751/L753); artefacts `[laughs]` x4, `[crosstalk]` x1; no ellipsis; ASCII only; LF line endings. Location convention: `L<line>, M:SS Label` with the stamp and label exactly as printed; composite-block segments add `(composite block, side-only)`.

## Checks run

Every `quote` in the 25 fields (150 of them) is a verbatim substring of exactly one transcript line, and its `L<line>` points at that line with the printed stamp and label; the readiness block's quotes and the key's other structured quotes bring the shared verifier's count to 191 pairs, all verified at their locations (`fixtures-work/_fixpass/verify_quotes.py`, 2026-10-13); every single-quoted phrase in a note carries the transcript's own casing; every re-joined sentence in the intake block is assembled from its owner's units only, with a second speaker's genuine completion left under its own label. Checked by script at review; the script is not kept with the fixture. Field order matches s1 to s10; R-names, per-pain check names and gate names match s1's key character for character; objection types lead with a section 5.2 name or `Outside the map:`. Names were scanned against every other fixture folder; the warehouse was renamed once to avoid a place name used in s19. Measured at review, not assumed: the five collisions, the one inversion, the one adjacent same-label pair, the 40 lowercase-initial, 32 unterminated and 57 short units, the 174-word block and its 96-second gap, and the word totals above. Speech mess was added at review in units no quote touches (eight self-repairs and repeats at the first pass; fifteen fillers, false starts and repeats across both sides at the second, because a consultant with no disfluency in 172 turns is a writer's artefact), with each unit's first character, terminal punctuation and short-unit class unchanged, so no count moved but the word total. Not yet run: `leak_lint.py --terms` and `cleanroom_scan.py`, which land in stage 2 (WP4, WP16).

At stage-1 acceptance (2026-09-20) the type-header values in `answer-key.json` were re-spelled as the tokens `shared/record-map.md` pins, with each value's prose moved to a `_note` field beside it; no quote, location, grade or count changed.

Reviewed by the user 2026-10-11 (`for-review/FEEDBACK.md`, s14 entry); fix pass applied 2026-10-13: the scarce, collision-prone kit is now identified by the client's rule and counted from the data with "about 200" recorded as our proposed clean-up size, every no-write claim about the hire system became "writeback and integration direction unresolved; v0.1 does not depend on either", the wedge detector's expected answer became "ran; not evaluable, no end times" with "found nothing" unacceptable without that reason, `direction_of_show` became `direction`, the seven-pattern sweep landed as nine leanings with three vocabulary and one alias-map field corrected, and the `readiness` block was added as the key's last field; no quote, location, grade or count changed, and the transcript is untouched.
