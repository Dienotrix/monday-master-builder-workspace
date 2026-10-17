# WP3 macOS run, Python 3.9

Date: 2026-10-17 12:21 UTC. Internal build file: never client-facing. Step 11 of `PLAN.md`, run by the main session on this machine.

## System

- System: macOS-26.6.2-arm64-arm-64bit
- Python: 3.9.6 (`/usr/bin/python3`, the system's own, which runs `/Library/Developer/CommandLineTools/usr/bin/python3`)
- File system encoding: utf-8; `os.name`: posix
- Plugin repository at commit `de75b04`, with no files changed.

## Unit suite

`/usr/bin/python3 -m unittest discover -s tests/unit -v`, with `PYTHONDONTWRITEBYTECODE=1`: exit 0, 330 tests in 22.2 s, result `OK`.

| Test file | Tests |
|---|---|
| `test_ledger.py` | 107 |
| `test_ledger_read.py` | 48 |
| `test_lint_plugin.py` | 21 |
| `test_mmb_common.py` | 50 |
| `test_record.py` | 51 |
| `test_record_part2.py` | 39 |
| `test_snapshots.py` | 14 |

Skipped: none. The symbolic-link test that Windows skips, `test_G09_mutex_reentry_through_a_second_spelling_does_not_wait (test_mmb_common.WriteTest)`, runs here and passes.
Failures and errors: none.
Warnings: one `ResourceWarning: unclosed file <_io.BufferedReader name=4>` during `test_K46_K111_a_mutex_held_by_another_process_is_exit_3_and_nothing_is_written (test_ledger.FrameTest)`, which passes. The test reads the holder process's stdout pipe and does not close it after `kill()` and `wait()`. Nothing was changed.

## Lint

`/usr/bin/python3 tools/lint_plugin.py --root .`: exit 0, `lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 10 file(s)`.

```
info: skills/: frontmatter: not present yet
info: agents/: frontmatter: not present yet
info: templates/: template-id: not present yet
info: templates/record/scope.md: handoff-sentence: not present yet
info: scripts/transcript_prep.py: pinned-agreement: not present yet (call-type-vocabulary unchecked)
info: scripts/transcript_measure.py: pinned-agreement: not present yet (permitted-constants unchecked)
warning: personal-names-index.json: personal-name: name list not found at <home>/monday-builder/personal-names-index.json; check not run
```

## Bytecode

`__pycache__` folders anywhere in the plugin repository after the run: 0.
