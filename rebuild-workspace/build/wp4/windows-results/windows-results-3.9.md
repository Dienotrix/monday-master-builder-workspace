# WP4 Windows run, Python 3.9

Date: 2026-10-22 01:51 UTC (the evening of 2026-10-21 in this machine's time zone). Internal build file: never client-facing. Step 11 of `PLAN.md`, run by the main session on this machine, inline, with no agents, from a fresh pull of both repositories.

## System

- System: Windows-10-10.0.26200-SP0 (as Python 3.9's `platform` names it; the machine is Windows 11 Pro, build 26200, which 3.14 reports as Windows-11)
- Python: 3.9.13 (`<home>\AppData\Local\Programs\Python\Python39\python.exe`, python.org, run as `py -3.9`)
- File system encoding: utf-8; `os.name`: nt
- Plugin repository at commit `0764cdb`, a fresh `git pull` from `de75b04`, with nothing changed in the working tree before or after the run. Workspace repository at `003e242`. Both clones have `core.autocrlf` false.

## Unit suite

`py -3.9 -m unittest discover -s tests\unit -v`, with `$env:PYTHONDONTWRITEBYTECODE='1'`: exit 0, 634 tests in 285.0 s, result `OK (skipped=8)`. The 3.14 run went after this one, not beside it.

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

The same 634 tests per file as the macOS run.

Skipped: eight, each a test that needs a symbolic link or a folder mode that denies access, neither of which this Windows account can make. Five fail to make a link with `[WinError 1314] A required privilege is not held by the client` (Windows makes symbolic links only with Developer Mode or an administrator's right, as WP2's and WP3's runs found); three find that `os.chmod` does not deny access here. All eight ran and passed on macOS (`macos-results/`), so their behaviour is proved there and not on Windows.

- `test_F09_X35_a_folder_linked_into_drafts_is_walked_or_stops (test_leak_lint.ReviewBlockingTest)`: "this system makes no symbolic links: [WinError 1314] A required privilege is not held by the client", for the link `drafts\linked` to the strand's `shared` folder in the test's temporary home (`<home>\AppData\Local\Temp\leak lint …\home with space\clients\hollowmere-bakery\strands\001-wholesale-orders\`).
- `test_G08_R36_R35_A24_an_archive_that_can_be_listed_but_not_searched_is_exit_3_naming_no_folder (test_leak_wall.ReviewPart2Test)`: "a mode without search does not deny access here".
- `test_G08_R36_X30_A24_L205_a_record_folder_that_cannot_be_searched_is_exit_3_naming_no_folder (test_leak_wall.ReviewPart2Test)`: "mode 000 does not deny access here".
- `test_G10_R38_X30_a_linked_folder_in_the_record_is_harvested_inside_and_stops_outside (test_leak_wall.ReviewPart2Test)`: "this system makes no symbolic links: [WinError 1314] A required privilege is not held by the client", for the link `research\extra.md` in the record `wrenfold-joinery` to `elsewhere\example.md` outside it (`<home>\AppData\Local\Temp\leak wall …\`).
- `test_G10_R38_X31_terms_walks_a_linked_folder_inside_the_folder_and_stops_on_one_outside (test_leak_wall.ReviewPart2Test)`: "this system makes no symbolic links: [WinError 1314] A required privilege is not held by the client", for the link `bundle\examples` to `..\elsewhere` (`<home>\AppData\Local\Temp\leak wall …\`).
- `test_G15_R46_records_under_clients_or_archive_and_a_home_reached_through_a_link_pass (test_leak_wall.ReviewPart2Test)`: "this system makes no symbolic links: [WinError 1314] A required privilege is not held by the client", for the link `linked home` to `home with space` (`<home>\AppData\Local\Temp\leak wall …\`).
- `test_G09_mutex_reentry_through_a_second_spelling_does_not_wait (test_mmb_common.WriteTest)`: "no symbolic links here" (WP2's skip, as in WP2's and WP3's Windows runs).
- `test_R39_init_stops_when_the_archive_cannot_be_looked_into (test_record_part2.InitTest)`: "modes deny nothing here".

Failures and errors: none.
Warnings: one `ResourceWarning: unclosed file <_io.BufferedReader name=3>` during `test_K46_K111_a_mutex_held_by_another_process_is_exit_3_and_nothing_is_written (test_ledger.FrameTest)`, which passes. It is the same warning the WP3 and WP4 macOS runs recorded (the test reads the holder process's stdout pipe), noted there and not fixed.

## Lint

`py -3.9 tools\lint_plugin.py --root .`, with `$env:PYTHONDONTWRITEBYTECODE='1'`: exit 0, `lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 11 file(s)`.

```
info: skills/: frontmatter: not present yet
info: agents/: frontmatter: not present yet
info: templates/: template-id: not present yet
info: templates/record/scope.md: handoff-sentence: not present yet
info: scripts/transcript_prep.py: pinned-agreement: not present yet (call-type-vocabulary unchecked)
info: scripts/transcript_measure.py: pinned-agreement: not present yet (permitted-constants unchecked)
warning: personal-names-index.json: personal-name: name list not found at <home>\monday-builder\personal-names-index.json; check not run
```

The `leak` pinned pair and the `shared-region` check (R41) are compared and agree.

## Bytecode

`__pycache__` folders anywhere in the plugin repository after both runs: 0 (none in the workspace either). The real home (`<home>\monday-builder`) does not exist after the run: the tests use temporary homes only. `git status --porcelain --ignored` in the plugin repository shows only the two ignored `tests/windows/windows-results-*.md` files of WP2's run, last written 2026-10-16.

## Line endings of the trap fixture (L220)

`git ls-files --eol tests/fixtures/leak`: 288 files, every one `i/lf w/lf attr/text eol=lf` (LF in the index and in the working tree; `tests/fixtures/leak/.gitattributes` is `* text eol=lf`). A byte check of the same 288 files on disk found no carriage return in any of them, and `[F] test_files_utf8_lf_no_bom` passes under both interpreters.
