# WP3 record-map edits applied

Date: 2026-10-16. Internal build file: never client-facing.

This file logs step 3 of WP3: the thirteen record-map edits of `DECISIONS.md` section 3, applied to `plugins/monday-master-builder/shared/record-map.md`, and the one tuple added to `tools/lint_plugin.py`. Line numbers are in `record-map.md` after all edits.

| Item | W ids | Where in `record-map.md` | What changed |
|---|---|---|---|
| 1 | W09, W10, W11, W12, W13, W08, W55, W71, W72, W85 | `## Pinned: ledger`, lines 340 to 366, after `## Pinned: permitted-constants`; the intro of line 3 and of `## Pinned: readiness` (line 279) now say "the pinned sections" | New section holding only the pinned tokens in a field and values table, plus a prose line on how the approval class is derived with no backticks; `("ledger", "scripts/ledger.py")` added to `PINNED` in `tools/lint_plugin.py` (lines 17 to 19). |
| 2 | W63 | Record-level table line 16 (`account.json`) and strand table line 44 (`solution/build.json`) | "passes `ledger.py check`" now points at the check paragraph under `build/2`. |
| 3 | W19, W74 | Table row line 26 (`live/snapshots/...`); `snapshot/1` paragraph, line 68, after the strand file tables | The path becomes `<date>-<strand>-<version>-<label>.json`; the shape of the snapshot file and the scope rule are written out. |
| 4 | W20, W70 | `.work/` paragraph, line 72; `live-inventory/1` paragraph, line 74 | `build.json.bak` dropped with the note on backup generations; `live-inventory.json` points at the new `live-inventory/1` shape. |
| 5 | W58 | `## Naming and references`, Versions bullet, line 83 | A `parent_key` may be a qualified live-map key resolved through `live_objects`. |
| 6 | W11 | `## Naming and references`, Element keys bullet, line 84 | Adds `B1.IB1`, `WF1`, `AG1`, `B1.AI1`, `VB1`, `SQ1`, `WH1`, `WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT`; the "not listed here yet" sentence is replaced. |
| 7 | W42, W46 | `### summary/1, scope/1, version/1 and the rest`, `blueprint/1` sentences, lines 121 to 135 | The `## Element keys` table and its example, the `### Prompt <KEY>` block, the resolution of `blueprint_ref` and `prompt_ref`, and the `AS<n>`, `AT<n>`, `FK<n>` ids. |
| 8 | W06, W08, W14, W16, W24, W37, W39, W80, W82 | `### account/1`, line 139 | `bind` as writer of `account`, `api` and refreshes; `superseded_workspaces[]`; `change_check.result`; `native_map` entities, one entry each, portfolio key, `projects[].connected` tokens, the `rule` sentence with `R0` and `N0`; `native_board_index` value form; `live_objects.workspace`, local-date `last_verified` and each writer. |
| 9 | W06, W07, W09, W11, W12, W13, W15, W30, W43, W45, W48, W50, W51, W56, W58, W64, W72, W73 | `### build/2`, line 143, and the status table, lines 145 to 162 | Field writers; optional-on-read rule with defaults; approval fields and `approval_mode`; `preflight.workspaces_ok`; run id and `another_build_running`; the 23 types; `state` values; `approval_ref` form; `notifies[]` forms; companions, `item_ids[]`, `product`, `workspace`, `workspace_scope`, `refs[]`, `assumption_refs`, `prompt_ref`, `version_id_at_build`, `live_key`, `read_values`; `digest` defined; `irreversible_yes[]` and `departures[]` forms; the status table. |
| 10 | W25, W71, W63 | `**Ledger write orders.**` line 164; `**Reconcile classes.**` line 176; `**What ledger.py check blocks and warns on.**` line 190, all after the `build/2` status table | Three new paragraphs: the write-order table with the committed report, the per-kind matches with the class table, and the check list. |
| 11 | W59, W60, W61, W62 | `### live-map/1`, header and example lines 196 to 199, paragraph line 201 | Ten-column header with a `workspace` cell, `inactive` among the states, kinds as type tokens, and the `run end` rules for creating and refreshing rows. |
| 12 | W25 | `### lock/2`, `**Writes and repairs.**`, line 209 | Added a sentence pointing at Ledger write orders. |
| 13 | W77 | `## Version states`, `audited` row, line 240 | The documents appendix format: `graphql` or `gql` fences, `query` strings inside `json` fences, any other fence refused by `ledger.py compare`. |

## Gates

Run from the repo root with `PYTHONDONTWRITEBYTECODE=1`.

- Lint, `py -3.14 tools\lint_plugin.py --root .`: 0 errors, 1 warning (the personal-names list is absent on this machine), 7 not present yet, including `scripts/ledger.py: pinned-agreement ... (ledger unchecked)` as information.
- `test_[mr]*.py`: 140 tests, OK with 1 skipped, under Python 3.9 and 3.14.
- `test_lint_plugin.py`: 21 tests, 20 pass and 1 fails under both Pythons. `test_clean_tree_passes` asserts "0 not present yet" for the `tests/fixtures/lint-clean` tree, which has no `scripts/ledger.py`, so the new tuple adds one information line. No record-map sentence is involved. The fix is outside this step's files: either a stub `scripts/ledger.py` with the pinned region in `tests/fixtures/lint-clean`, or the assertion changed to "1 not present yet".
