# WP3 Windows run, Python 3.9

Date: 2026-10-17 11:49 UTC. Internal build file: never client-facing. Step 10 of `PLAN.md`, run by the main session on this machine.

## System

- System: Windows-10-10.0.26200-SP0
- Python: 3.9.13 (<home>\AppData\Local\Programs\Python\Python39\python.exe)
- File system encoding: utf-8; `os.name`: nt
- Plugin repository at commit `1baecc9`, with these files changed since it (the review fixes and part 2, not yet committed):

  - ` M plugins/monday-master-builder/scripts/ledger.py`
  - ` M plugins/monday-master-builder/shared/record-map.md`
  - ` M tests/unit/test_ledger.py`

## Unit suite

`py -3.9 -m unittest discover -s tests/unit -v`, with `PYTHONDONTWRITEBYTECODE=1`: exit 0, 330 tests in 52.3 s, result `OK (skipped=1)`.

| Test file | Tests |
|---|---|
| `test_ledger.py` | 107 |
| `test_ledger_read.py` | 48 |
| `test_lint_plugin.py` | 21 |
| `test_mmb_common.py` | 50 |
| `test_record.py` | 51 |
| `test_record_part2.py` | 39 |
| `test_snapshots.py` | 14 |

Skipped: `test_G09_mutex_reentry_through_a_second_spelling_does_not_wait (test_mmb_common.WriteTest)` ('no symbolic links here').
Failures and errors: none.

## Lint

`py -3.9 tools/lint_plugin.py --root .`: exit 0, `lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 10 file(s)`.

```
info: skills/: frontmatter: not present yet
info: agents/: frontmatter: not present yet
info: templates/: template-id: not present yet
info: templates/record/scope.md: handoff-sentence: not present yet
info: scripts/transcript_prep.py: pinned-agreement: not present yet (call-type-vocabulary unchecked)
info: scripts/transcript_measure.py: pinned-agreement: not present yet (permitted-constants unchecked)
warning: personal-names-index.json: personal-name: name list not found at <home>\monday-builder\personal-names-index.json; check not run
```

## Bytecode

`__pycache__` folders anywhere in the plugin repository after the run: 0.

