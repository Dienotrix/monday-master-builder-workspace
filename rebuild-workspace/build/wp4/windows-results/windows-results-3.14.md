# WP4 Windows run, Python 3.14

Date: 2026-10-22 01:56 UTC (the evening of 2026-10-21 in this machine's time zone). Internal build file: never client-facing. Step 11 of `PLAN.md`, run by the main session on this machine, inline, with no agents, from a fresh pull of both repositories.

## System

- System: Windows-11-10.0.26200-SP0
- Python: 3.14.5 (`<home>\AppData\Local\Programs\Python\Python314\python.exe`, python.org, run as `py -3.14`, the newest `py --list` shows)
- File system encoding: utf-8; `os.name`: nt
- Plugin repository at commit `0764cdb`, a fresh `git pull` from `de75b04`, with nothing changed in the working tree before or after the run. Workspace repository at `003e242`. Both clones have `core.autocrlf` false.

## Unit suite

`py -3.14 -m unittest discover -s tests\unit -v`, with `$env:PYTHONDONTWRITEBYTECODE='1'`: exit 0, 634 tests in 262.6 s, result `OK (skipped=8)`. The 3.9 run went before this one, not beside it.

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

Skipped: the same eight tests as under 3.9, with the same reasons (listed in full in `windows-results-3.9.md`): five need a symbolic link, which fails with `[WinError 1314] A required privilege is not held by the client`, and three need a folder mode that denies access, which `os.chmod` does not give here. All eight ran and passed on macOS.

- `test_F09_X35_a_folder_linked_into_drafts_is_walked_or_stops (test_leak_lint.ReviewBlockingTest)`: no symbolic links.
- `test_G08_R36_R35_A24_an_archive_that_can_be_listed_but_not_searched_is_exit_3_naming_no_folder (test_leak_wall.ReviewPart2Test)`: "a mode without search does not deny access here".
- `test_G08_R36_X30_A24_L205_a_record_folder_that_cannot_be_searched_is_exit_3_naming_no_folder (test_leak_wall.ReviewPart2Test)`: "mode 000 does not deny access here".
- `test_G10_R38_X30_a_linked_folder_in_the_record_is_harvested_inside_and_stops_outside (test_leak_wall.ReviewPart2Test)`: no symbolic links.
- `test_G10_R38_X31_terms_walks_a_linked_folder_inside_the_folder_and_stops_on_one_outside (test_leak_wall.ReviewPart2Test)`: no symbolic links.
- `test_G15_R46_records_under_clients_or_archive_and_a_home_reached_through_a_link_pass (test_leak_wall.ReviewPart2Test)`: no symbolic links.
- `test_G09_mutex_reentry_through_a_second_spelling_does_not_wait (test_mmb_common.WriteTest)`: "no symbolic links here".
- `test_R39_init_stops_when_the_archive_cannot_be_looked_into (test_record_part2.InitTest)`: "modes deny nothing here".

Failures and errors: none.
Warnings: one `ResourceWarning: unclosed file <_io.BufferedReader name=3>` during `test_K46_K111_a_mutex_held_by_another_process_is_exit_3_and_nothing_is_written (test_ledger.FrameTest)`, which passes, the same as under 3.9 and on macOS.

## Lint

`py -3.14 tools\lint_plugin.py --root .`, with `$env:PYTHONDONTWRITEBYTECODE='1'`: exit 0, `lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 11 file(s)`, with the same six `not present yet` lines and the same warning as under 3.9 (no personal-names list at `<home>\monday-builder\personal-names-index.json`); the two outputs are line for line the same.

## Bytecode

`__pycache__` folders anywhere in the plugin repository after the run: 0.

## Line endings of the trap fixture (L220)

As in `windows-results-3.9.md`: 288 files, every one LF in the index and in the working tree, no carriage return on disk; the check does not depend on the interpreter.
