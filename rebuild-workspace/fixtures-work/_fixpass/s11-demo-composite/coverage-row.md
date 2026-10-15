# s11-demo-composite — COVERAGE row after the fix pass

The row for the calibration table of `fixtures/COVERAGE.md` (thirteen columns, same as the existing row). Every count is true of the edited files on 2026-10-13.

| `s11-demo-composite/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C56 | R19 | 24 (9 / 13 / 1 / 1 / 0) | 2 (1) | 8 | 22 (4) | 13 | 5 (1 / 3 / 1) | 151 | reviewed 2026-10-13; fix pass applied 2026-10-13 |

Counts that moved: Quote strings 120 to 151 (the readiness block's pains, signals and leaning quotes, all verified at their locations by `verify_quotes.py`), and the Review column. Counts that did not move: rubric rows 24 (9 met, 13 partial, 1 missing, 1 met-with-residual), pains graded 2 (1 excavated), objections 8, traps 22 (4 look-alike), leak entries 13, requested changes 5 (1 add, 3 change, 1 remove). Outside the row: the transcript is 86 turns and 257 lines, about 9,006 words (from 82, 245 and 8,761); the key has 27 top-level fields, 548 lines; 48 transcript units carry 68 protected spans (from 47 and 64).

Note on the Review column: the user's review of this fixture is dated 2026-09-21 in FEEDBACK.md; the column reads as the brief prescribes for every row in this pass.
