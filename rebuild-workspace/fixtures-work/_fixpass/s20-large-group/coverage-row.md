# s20-large-group — COVERAGE row after the fix pass

The row for the s11 to s25 table of `fixtures/COVERAGE.md` (thirteen columns, same order as the existing row). Every count is true of the edited files on 2026-10-13.

| `s20-large-group/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C63 | R6 | 36 (27 / 5 / 1 / 2 / 1) | 4 (4) | 9 | 28 (6) | 19 | 3 (1 / 2 / 0) | 278 | reviewed 2026-10-13; fix pass applied 2026-10-13 |

Counts that moved: quote strings 224 to 278 (the `readiness` block introduces 54 quote-and-location pairs, all verified; `verify_quotes.py` reports 278 pairs found, 278 verified, 28 of them presence-only, zero misses and zero near-misses). Counts that did not move: rubric rows 36, graded pains 4 (all excavated), objections 9, traps 28 (6 look-alike), leak entries 19, requested changes 3. Outside the row: the transcript is still 265 units and 268 lines, now 6,023 spoken words (12 added inside three uncited Consultant turns by the mess pass), client share still 72%; the key has 27 top-level fields (`readiness` last) and 556 lines; the alias map has 19 entries.
