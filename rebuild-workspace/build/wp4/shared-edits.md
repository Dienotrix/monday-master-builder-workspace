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
