# WP4 step 8, part 2 fixes: the common brief for one finding

You fix one finding of the adversarial review of `leak_lint.py`, part 2. Your prompt names the finding, its decision number and anything specific to it. Everything else is here.

## Where things are

- Plugin repository: `<home>/DelOps/monday-master-builder-dev/monday-master-builder`
  - The script: `plugins/monday-master-builder/scripts/leak_lint.py`
  - The tests for this work: `tests/unit/test_leak_wall.py`, class `ReviewPart2Test` (G01 and G02's tests are there; copy their shape and helpers).
  - The trap fixture: `tests/fixtures/leak/` (two planted client records, `manifest.json`). The grading harness: `tests/unit/test_leak_grading.py`.
- Workspace files: `<home>/DelOps/monday-master-builder-dev/rebuild-workspace/build/wp4/`
  - `leak-review-part2.md`: your finding's section, and the table "Fixes for part 2 (step 8), 2026-10-19" at the end.
  - `DECISIONS.md`: the section "Added by the review fixes, part 2 (step 8), 2026-10-19" near the end. R29 and R30 are the model for an entry's shape (Decision, Reason, Follow-up with Build, Test, Touch-up, Finding). Read the decisions your finding cites by grepping their headings (for example `### X27`).
  - `API-leak_lint.md`: the script's interface notes.
- Scratch space for any probe you rebuild: the session's scratchpad folder, which your prompt names. The review's own probes were lost; rebuild one only if it helps, from the finding's minimal input.

The script is about 4,000 lines. Read it around the functions your finding names; grep for them, because the review's line numbers are from an older frozen copy and have moved.

## The steps, saving after each one

1. **Test.** Write the finding's test or tests in `ReviewPart2Test`, named `test_<finding>_<decision>_<what it proves>`, and confirm they fail on the script as it is.
2. **Fix** `leak_lint.py`.
3. **Run the gates** from the plugin repository's root, always with `PYTHONDONTWRITEBYTECODE=1`:
   - `/usr/bin/python3 -m unittest tests.unit.test_leak_wall` (about 40 seconds)
   - then the four leak files together: `/usr/bin/python3 -m unittest tests.unit.test_leak_lint tests.unit.test_leak_wall tests.unit.test_leak_grading tests.unit.test_leak_fixture`
   Every test passes, except a test of a later finding that your prompt says is expected to fail.
4. **Decision entry.** Append your R entry at the end of `DECISIONS.md`, after the last R entry, in R29's shape. Settle on the fail-safe side; if the fix narrows a block, name the source that wins. If the decisions are silent on a choice you had to make, take the fail-safe reading and add a line starting `*Nod:*` to the Follow-up, in plain words, for the user.
5. **Table row.** Add your finding's row to the "Fixes for part 2" table in `leak-review-part2.md`, in G01's shape.
6. **Interface notes.** Update `API-leak_lint.md` only if a function's behaviour, a pinned region or a command's output changed.

## Rules

- Python standard library only; the code runs on Python 3.9 and 3.14. Match the surrounding code: its naming, comment density and idiom.
- Every name, term and figure in a test is invented. Use the review's invented ones (Fernhollow Supply, Tallowmere, Østby Freight, Blue Harbour, Brindle Tiles and so on) or new invented ones. No real person, firm or monday account, no real ids, nothing from any earlier work. The person who uses the plugin is "the user", they/them.
- Calm prose in every file: short sentences with reasons, no capitals for emphasis.
- A30 bounds the wall: another client's name, term or figure in its normal forms, not misspellings by sound.
- Touch only `leak_lint.py`, `test_leak_wall.py` and the three workspace files above. Do not edit anything under `shared/`, `tools/lint_plugin.py`, another package's script, or another finding's code. If your fix seems to need one of those, stop and say so in your return. A gap you find in a package that is already built (WP2's `record.py` and `mmb_common.py`, WP3's `ledger.py`, `tools/lint_plugin.py`) also goes in your return, and the main session fixes it in the same sitting (the user, 2026-10-21); "owed to" is only for packages not built yet (WP7 onward).
- No git command that changes anything: no add, commit, stash, checkout or reset.
- Leave no `__pycache__` folder anywhere in the repository.

## Your return

Under 80 words: the files you changed, the test names, the R number, a one-line result, the gate counts (tests run, failures), and any nod or stop.
