# s14-shred-block — COVERAGE row after the fix pass

The row for the calibration table of `fixtures/COVERAGE.md` (thirteen columns, same order as the existing row). Two cells moved: Quote strings, from 154 to 191, because the readiness block cites its own quotes and the shared verifier counts every structured pair; and Review, to the string the brief fixes.

| `s14-shred-block/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C58 (a) | none | 36 (27 / 3 / 3 / 2 / 1) | 4 (3) | 12 | 30 (7) | 15 | 7 (2 / 4 / 1) | 191 | reviewed 2026-10-13; fix pass applied 2026-10-13 |

Counts checked against the edited files on 2026-10-13: rubric rows 36 (27 met, 3 partial, 3 missing, 2 met-with-residual, 1 not-obtainable; no grade changed); pains graded 4 with 3 excavated (P1 to P4 in the rubric; the key's `pains` array still holds its ten entries); objections 12; traps 30, look-alike traps 7; leak entries 15; requested changes 7 (2 add, 4 change, 1 remove); quote strings 191 (the verifier's "pairs found", 154 before the block). The transcript is untouched: 415 units, 829 lines, 6,448 words. The key has 27 top-level fields (`intake` then `readiness`) and 503 lines.

Note for the merge step: the user's review of this fixture is dated 2026-10-11 in `for-review/FEEDBACK.md`; the Review cell carries the brief's fixed string, and `changes.md` beside this file records the actual review date.
