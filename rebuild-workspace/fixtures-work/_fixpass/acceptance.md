# Fixture fix pass — closing record

Written 2026-10-13 by the planner. The pass applied the user's review of the fixtures (`for-review/FEEDBACK.md`) and the stage 1b decisions to all 25 answer keys and the shared files, in the order of `rebuild-workspace/design/stage-1b/PLAN.md` section 7.

## What ran

- Step 1, three agents: `verify_quotes.py`, the quote-at-location verifier, proven on the unedited set (3,818 quote strings, 3,812 verified, no miss, the six others pointers, prose or an image label; `baseline.md`); the exemplar keys s1 (strong) and s5 (thin), whose logs became section 8 of `BRIEF.md`.
- Step 2, fifty-four agents: for each of the other 23 fixtures an editor on the session model, a Sonnet verifier, and a fixer plus a second verifier only on a fail (s8, a spliced quote in a readiness question; s24, a filler count; s25, a missing leaning and a count); the shared-files step; the merge step. Every fixture ends PASS. About 55 minutes and 9.3M subagent tokens in all, no agent errors.
- Closing by the planner: the whole-set check (`fixpass_final.py` in the session scratchpad): every key valid with `readiness` last, `direction_of_show` gone, at most five questions, a valid clearance and no sales word in the block; the verifier clean on all 25; the shared-file moves and retirements in place; lint at zero errors and the 21 remaining unit tests passing; every coverage table with consistent columns; the handle only in the plugin manifest; the review copies current.

## What changed

- Every key: the `readiness` block (`readiness/1`, pinned in `shared/record-map.md`), the seven-pattern sweep with each hit as a leaning, the "never written to" rule, the standing lines. s11 to s25: `direction` in place of `direction_of_show`, the review entry's changes, the mess pass inside existing units (s11 with its two new turns and a full re-cite). s24's fork carries its `leaning`.
- Coverage: 25 rows merged, the calibration totals recomputed from the rows (432 traps, 95 look-alike; 80 requested changes; 3,073 quote strings, readiness blocks included; rubric and pains unchanged), every "pending review" cleared.
- Shared files: `readiness/1` and the three clearance strings pinned; the v2 rows fenced in place; `small-group` widened; the firm class out of `leak-terms.txt`; `sales-method.md` and `house-style.md` under `deferred/shared/` with a README; `sandbox-accounts.txt` retired, its syntax recorded under the home's `local/`; the clean-room scan, its test and fixtures removed; the shipped default home now `~/monday-builder` (A22, D11); stale paths in `safety.md` and `monday-gotchas.md` corrected; the record map's intro counts three pinned sections.
- Review material: `for-review/fixtures/` refreshed for s11 to s25 with a `CHANGES.md` in each folder, the new `COVERAGE.md`, and a dated note in `00-HOW-TO-REVIEW.md`; FEEDBACK entries marked applied.

## Left as it stands

- The lint's one warning: the personal-name index does not exist yet, so that check does not run (known since stage 1).
- Nothing is committed; the repository carries the moves, removals and edits as working changes.
- The remaining shared-file re-cut (the AI-kind gotcha areas and read-back rows, the full WP1 pass) is stage 2's work, per the re-cut BUILD-PLAN.
