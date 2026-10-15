# s12-header-present — COVERAGE row after the fix pass

The row for the second table of `fixtures/COVERAGE.md` (calibration fixtures, thirteen columns), with every count true of the edited files. Two cells moved: Quote strings (158 to 199, the readiness block's 41 pairs, all verified) and Review. Rubric rows, pains graded, objections, traps, leak entries and requested changes are unchanged by the pass; the alias map grew from 18 to 20 entries, which this table does not track (the README does).

| `s12-header-present/` | calibration fixture | `transcript.txt`, `meeting-chat.txt`, `answer-key.json`, `README.md` | C57 (a) | none | 36 (24 / 6 / 3 / 2 / 1) | 4 (3) | 9 | 32 (6) | 16 | 4 (2 / 2 / 0) | 199 | reviewed 2026-10-13; fix pass applied 2026-10-13 |

Counts behind the row, re-measured from the files on 2026-10-13: transcript 214 units, 674 lines, 5,389 spoken words (cues excluded, the key's method), client share 66.2%, longest own-side turn 102 words at 14:39:55, 0 colliding timestamps, 1 adjacent same-label pair, 0 lowercase-initial units, 20 units at or under four words, nine ' -- ' breaks, six [laughs]; chat 11 messages, unchanged; key 27 top-level fields (25, `intake`, `readiness`), 550 lines; `verify_quotes.py` 199 pairs, 199 verified, 0 misses, 0 near-misses.
