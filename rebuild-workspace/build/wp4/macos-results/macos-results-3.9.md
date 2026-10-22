# WP4 macOS run, Python 3.9

Date: 2026-10-21 23:00 UTC. Internal build file: never client-facing. Step 10 of `PLAN.md`, run by the main session on this machine, inline, after the part 2 review fixes and the follow-up (R29 to R64).

## System

- System: macOS-26.7.1-arm64-arm-64bit
- Python: 3.9.6 (`/usr/bin/python3`, the system's own, which runs `/Library/Developer/CommandLineTools/usr/bin/python3`)
- File system encoding: utf-8; `os.name`: posix
- Plugin repository at commit `4f28132` with WP4 sitting B's work uncommitted in the working tree (28 paths: the scripts, the shared edits, the tests and the trap fixture HANDOFF lists). Not a fresh pull: the checkpoint commit comes at the user's word before the Windows run.

## Unit suite

`/usr/bin/python3 -m unittest discover -s tests/unit -v`, with `PYTHONDONTWRITEBYTECODE=1`: exit 0, 634 tests in 117.3 s, result `OK`. The 3.14 run went side by side with this one, so both times read high.

| Test file | Tests |
|---|---|
| `test_leak_fixture.py` | 16 |
| `test_leak_grading.py` | 3 (the 248 grading cases of the trap fixture) |
| `test_leak_lint.py` | 143 |
| `test_leak_wall.py` | 121 |
| `test_ledger.py` | 109 |
| `test_ledger_read.py` | 48 |
| `test_lint_plugin.py` | 25 |
| `test_mmb_common.py` | 52 |
| `test_record.py` | 51 |
| `test_record_part2.py` | 52 |
| `test_snapshots.py` | 14 |

Skipped: none. The tests that Windows or a root user skips (the symbolic-link tests, the unsearchable-folder tests of R36 and R39) run here and pass.
Failures and errors: none.
Warnings: one `ResourceWarning: unclosed file <_io.BufferedReader name=4>` during `test_K46_K111_a_mutex_held_by_another_process_is_exit_3_and_nothing_is_written (test_ledger.FrameTest)`, which passes. It is the same warning WP3's macOS run recorded (the test reads the holder process's stdout pipe), noted there and not fixed.

## Lint

`/usr/bin/python3 tools/lint_plugin.py --root .`: exit 0, `lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 11 file(s)`.

```
info: skills/: frontmatter: not present yet
info: agents/: frontmatter: not present yet
info: templates/: template-id: not present yet
info: templates/record/scope.md: handoff-sentence: not present yet
info: scripts/transcript_prep.py: pinned-agreement: not present yet (call-type-vocabulary unchecked)
info: scripts/transcript_measure.py: pinned-agreement: not present yet (permitted-constants unchecked)
warning: personal-names-index.json: personal-name: name list not found at <home>/monday-builder/personal-names-index.json; check not run
```

The `leak` pinned pair and the `shared-region` check (R41) are compared and agree.

## Bytecode

`__pycache__` folders anywhere in the plugin repository after the run: 0. The real home (`<home>/monday-builder`) does not exist before or after the run: the tests use temporary homes only.
