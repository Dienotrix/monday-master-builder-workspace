# WP4 step 3: shared edits log

2026-10-17. Internal build file: never client-facing.

All paths are inside the plugin repository. LF endings and no BOM were confirmed before and kept.

## Edits (line numbers after the edit)

1. 4.1 `plugins/monday-master-builder/shared/record-map.md`: new `## Pinned: leak` section, inserted before the `intake-report/1` heading, starting at line 370. 49 lines added (block plus one blank line).
2. 4.2 `plugins/monday-master-builder/shared/leak-terms.txt`:
   - line 146: "eight" changed to "nine" (1 line changed).
   - `[A]` inserted at line 156, between `[I]` and `[found]` (1 line added).
   - tool-category block appended at lines 197-307, after one blank line following `re: \[L1[4-8]\]` (111 lines added).
3. 4.3: confirmed, nothing beyond 4.2.
4. 4.4 `tools/lint_plugin.py`: the `("leak", "scripts/leak_lint.py")` tuple added to `PINNED`, line 19-20 (1 line changed, 1 added).

`git diff --stat`: exactly 3 files, 164 insertions, 2 deletions.

## Checks (PYTHONDONTWRITEBYTECODE=1)

- `/usr/bin/python3 tools/lint_plugin.py --root .`: 0 errors, 1 warning (personal-names-index.json not found; check not run), 7 not present yet (includes the `leak` pair, as expected).
- Same under python3.14: identical result.
- `/usr/bin/python3 -m unittest discover -s tests/unit`: 330 tests, FAILED (failures=1).
- python3.14 unit suite: 330 tests, FAILED (failures=1), the same one.
- `git diff --stat`: 3 files.
- `__pycache__`: none found in the plugin repository.

### Failure (not fixed, per instructions)

```
FAIL: test_clean_tree_passes (test_lint_plugin.LintPluginTest)
  File tests/unit/test_lint_plugin.py, line 61, in test_clean_tree_passes
    self.assertIn("0 error(s), 0 warning(s), 0 not present yet", self.clean)
AssertionError: ... not found in 'info: scripts/leak_lint.py: pinned-agreement: not present yet (leak unchecked)\nlint_plugin: 0 error(s), 0 warning(s), 1 not present yet, 14 file(s)\n'
```

Cause: the new `leak` PINNED tuple reports 1 not present yet on the clean fixture tree, while the test expects 0. The test needs updating (or leak_lint.py to exist) in a later step.

### Fixed by the main session, 2026-10-17

Section 4 of `DECISIONS.md` missed one thing that WP3 also needed: the lint-clean fixture under `tests/unit/fixtures/tools/lint-clean/` must carry every pinned pair, or `test_clean_tree_passes` sees one pair not present yet. Two small additions, in the same shape as WP3's `ledger` stub:

- `tests/unit/fixtures/tools/lint-clean/plugins/monday-master-builder/shared/record-map.md`: a `## Pinned: leak` section after `## Pinned: ledger`, with four synthetic tokens (`block`, `warn`, `clean`, `blocked`).
- `tests/unit/fixtures/tools/lint-clean/plugins/monday-master-builder/scripts/leak_lint.py` (new, five lines): a synthetic stand-in with the same four tokens between `# pinned: leak` and `# end pinned`.

After the fix, with `PYTHONDONTWRITEBYTECODE=1`: 330 tests OK under `/usr/bin/python3` (3.9.6) and the uv-managed 3.14.6; `tools/lint_plugin.py --root .` at 0 errors, 1 warning (no personal-names list on this machine) and 7 not present yet under both; no `__pycache__`; every edited file LF with no byte-order mark. The plugin diff is now five files: the three of section 4 and the two fixture files above.

## Added by the fixes to built packages, 2026-10-21 (R40)

At the user's word ("fix them now before run 3, including the former-names field for renames"). One file, one paragraph: the `client/2` section and nothing else.

### Edits (line numbers after the edit)

1. `plugins/monday-master-builder/shared/record-map.md`, line 109 (the paragraph under `### client/2, the front matter of CLIENT.md`), three insertions, nothing removed (1 line changed):
   - after "Then `ai_notice` (`not-yet` | `not-needed` | `given YYYY-MM-DD`) and `updated` (the local minute). ", inserted:

     > Last and optional, `former_names`: the client's earlier names, each one line with no `;`, joined by `; ` in the order they were dropped, empty or absent when the client has had no other name; a record written without it reads as having none, so it stays `client/2`. `record.py client rename --name "<new>"` is the one command that changes `name`: it appends the old name to `former_names` once, never drops an entry, refuses a name the client has or has had, and logs a record-level `decision` entry with key `rename`; the slug never changes. The user may also add an old name by hand. `leak_lint.py` reads every former name as one of the record's own names, so the field holds only this client's earlier names. 

   - "`record.py check` blocks on a missing field" became "`record.py check` blocks on a missing field (`former_names` apart)".
   - "a value outside its set" became "a value outside its set (for `former_names`, an empty name between the `;`)".

The new word `rename` entered `leak_lint.py`'s pinned `shared-words` region (R40, U2 of the API note), after `terms` over the changed `shared/` had passed against the region as it was.

### Checks (PYTHONDONTWRITEBYTECODE=1)

- `/usr/bin/python3 tools/lint_plugin.py`: 0 errors, 1 warning (no personal-names list on this machine), 6 not present yet; the same under the uv-managed 3.14.6. The lint-clean fixture needed no change.
- `/usr/bin/python3 -m unittest discover -s tests/unit`: 571 tests OK.
- LF endings and no byte-order mark kept.

## Added by the follow-up, run 5 (step 8), 2026-10-21 (R61, R62, A30)

Every edit below was made by the main session at the user's word; the R64 run logged them and edited nothing under `shared/`. The user's approvals, in their words:

- For R61 and A30, in `leak-terms.txt` and `record-map.md`: "Yes, I approve both shared edits: in shared/leak-terms.txt remove the spaced rows "exit ramp" and "cost of waiting" (R61), and remove the tool-category comment block and its fifteen tool-category- classes (A30); in shared/record-map.md remove the "counted class prefix | tool-category-" row from Pinned: leak".
- Then, for A30: "in record-map.md's Pinned: leak rule row, remove `tool-categories` (A30)".
- For R62: "replace leak-terms.txt's allowlist comment (lines 27 to 29) with R62's five lines naming the three clearable internal notes".

### Edits

1. `plugins/monday-master-builder/shared/leak-terms.txt`, class `method` (R61): two rows removed, nothing added.
   - `exit ramp`, the row just above `exit-ramp`.
   - `cost of waiting`, the row just below `cost-of-waiting`.
2. `plugins/monday-master-builder/shared/leak-terms.txt`, the allowlist comment, lines 27 to 29 (R62): three lines replaced by five.
   - The old three lines:

     ```
     # The per-client allowlist may clear a row of class method only. Rows of every other class
     # are never cleared by an allowlist (9.6). A term that is also the client's own vocabulary
     # survives with a caution rather than being removed.
     ```

   - The new five lines (now lines 27 to 31):

     ```
     # The per-client allowlist may clear a row of class method only. Rows of every other class
     # are never cleared by an allowlist (9.6). The lint also lets it clear the internal notes
     # "internal only", "internal use only" and "not for clients" for one client, and never the
     # speaker labels or the note front matter. A term that is also the client's own vocabulary
     # survives with a caution rather than being removed.
     ```

3. `plugins/monday-master-builder/shared/leak-terms.txt`, the end of the file (A30): the tool-category block removed, 111 lines in all (lines 197 to 307 of the committed file), so the file now ends at `re: \[L1[4-8]\]`. The block was a blank line, this comment, a blank line, and fifteen classes holding 75 rows of generic category words:

   ```
   # Tool categories (9.6, the second structural assertion). Every class below whose name starts
   # with tool-category- is counted and never blocked: leak_lint.py fails a sentence that names
   # three or more distinct categories in a paragraph with no proper noun, and a single hit is
   # never reported. The rows are generic category words, never product names, and an allowlist
   # has nothing to clear here.
   ```

   The fifteen classes, in order: `tool-category-accounting`, `tool-category-crm`, `tool-category-erp`, `tool-category-spreadsheet`, `tool-category-scheduling`, `tool-category-hr`, `tool-category-ticketing`, `tool-category-messaging`, `tool-category-documents`, `tool-category-inventory`, `tool-category-field`, `tool-category-lab-quality`, `tool-category-design`, `tool-category-marketing`, `tool-category-reporting`.
4. `plugins/monday-master-builder/shared/record-map.md`, `## Pinned: leak` (A30): the row ``| counted class prefix | `tool-category-` |`` removed (1 line).
5. `plugins/monday-master-builder/shared/record-map.md`, `## Pinned: leak`, the `rule` row (A30): `` `tool-categories`, `` removed from between `` `paraphrase`, `` and `` `number` `` (1 line changed).

### What followed in the script and the checks

- R62's comment added no word to and dropped none from `leak_lint.py`'s `shared-words` region (R29), as R62's probe said.
- After edits 1, 3, 4 and 5, `test_L197_terms_over_the_real_shared_folder_exits_0` passed against the regions as they were. R64 then regenerated `shared-words`: 47 words that only the removed classes wrote left it, none entered; `shared-phrases` (R32) was unchanged. `leak_lint.py`'s pinned `leak` region lost `tool-categories` and `COUNTED_PREFIX` with the check (R64), so `tools/lint_plugin.py`'s pinned comparison and its `shared-region` check (R41) agree again.
- `/usr/bin/python3 tools/lint_plugin.py`: 0 errors, 1 warning (no personal-names list on this machine), 6 not present yet. The lint-clean fixture needed no change.
- LF endings and no byte-order mark kept.
