# Merge step log, 2026-10-13

## 1. COVERAGE.md

All 25 rows were replaced from each fixture's `coverage-row.md`. The row was taken as the single line starting with the fixture's folder name, because several files carry a heading and a note around it.

- s1 to s10 (first table, three columns): merged. All ten rows were identical to the existing rows, as the editors said (no counts in that table, no fourth column).
- s11 to s25 (calibration table, thirteen columns): merged, all fifteen changed. Review column now reads `reviewed 2026-10-13; fix pass applied 2026-10-13`.
- Column check: every row has the expected count (3 or 13), and a pass over every table in the file found the same number of columns in every row.
- First paragraph: "grades discovery against the method spec (...)" became "reads the inputs, checks build-readiness, proposes a monday blueprint" (the plugin sentence now reads: reads the inputs, checks build-readiness, proposes a monday blueprint, builds it in the client's account, and writes demo scripts and SOPs).
- Calibration section: "**User review is pending on every row.**" became "The user's review of all fifteen closed on 2026-10-13; the fix pass was applied the same day, and each folder's README records what changed."

Left as they were, by the instruction to change nothing else, and worth a look: the intro paragraph (line 7) still says the review of each is pending, and the calibration totals line and the objections, traps, requested changes and leak-entry notes still say "pending review" and carry pre-pass totals (for example 2,519 quote strings). The totals were not recomputed from the new rows.

## 2. FEEDBACK.md

- Added the line under the "Agreed order" paragraph.
- Appended " Applied 2026-10-13 in the fixture fix pass." to the Status line of 13 entries: s11 (first note only), s12, s13, s14, s15, s16, s18, s19, s20, s21, s22, s23, s24.
- Appended " The sweep ran over all 25 keys on 2026-10-13." to the Cross-fixture patterns Status line.
- No other words changed. s11's second note, s17 and s25 untouched.

## 3. Review copies

- `for-review/fixtures/COVERAGE.md` replaced with the new file.
- Fresh copies of s11 to s25 under `for-review/fixtures/` (old folders removed first, `.DS_Store` excluded), each with its `_fixpass/<fixture>/changes.md` added as `CHANGES.md`. A diff against the source folders shows only the added CHANGES.md in each.
- `for-review/fixtures/00-HOW-TO-REVIEW.md`: the dated paragraph added directly under the title; the rest unchanged.

## 4. Problems

No coverage-row.md was missing. None was malformed in the sense of a bad row; the exemplar-style files (s1, s2, s5, s10 and others) carry notes and headings around the row, handled by picking the one row line. No fallbacks were needed.

## Paths refreshed

- ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/COVERAGE.md
- ~/DelOps/monday-master-builder-dev/for-review/FEEDBACK.md
- ~/DelOps/monday-master-builder-dev/for-review/fixtures/COVERAGE.md
- ~/DelOps/monday-master-builder-dev/for-review/fixtures/00-HOW-TO-REVIEW.md
- ~/DelOps/monday-master-builder-dev/for-review/fixtures/s11-demo-composite to s25-client-documents (15 folders)
