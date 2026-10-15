# Record-map edits applied (WP2 decisions)

Date: 2026-10-14. Internal build file: never client-facing.

Applied to `shared/record-map.md` from the closing "Record-map edits" list of `DECISIONS.md`. The line given is where the edit sits in the file after editing (287 lines now). 27 listed edits, plus the revision-note clause.

| Edit | Entry | Line after | What changed |
|---|---|---|---|
| Revision note | n/a | 3 | The opening paragraph, which carries the "as amended" statement, gains "WP2 decisions of 2026-10-14 applied (build/wp2/DECISIONS.md)". The file has no separate revision note. |
| RM:20, RM:23 | G13 | 20, 23 | Both raw rows now read "raw, sha recorded in the save entry of `log.md`". |
| Strand table | G44 | 37, 43, 52 | `readiness.md` budget is 250 lines; new rows `solution/exclusions.md` (80 lines) and `versions/<v>/build-notes.md`, `build-notes.html` (250 lines), taking their owners and client-facing values from A§7.1. |
| RM:53 | G26 | 55 | `updates.md` is dropped from the release snapshots. |
| RM:64 | G44 | 66 | The 4 MB exclusion adds `inputs/*.<ext>`, and the `non-platform` file list follows A§7.1:429 (`readiness.md`, no `deliverables/handoff/`, no `sop/` clause). |
| RM:66 | G08, G09, G39, G46 | 68 | `.work/` lists `history.json` (defined), `record.mutex`, timestamped `backup/` generations and the plan files, and drops the five retired items and the per-strand extras. |
| RM:68 | G34, G46, G58 | 70 | The home list is A§5.3:345's (with `SANDBOX.md` and `archive/`), `leases.json` and `claims/` are gone, `settings.json` carries the G34 fields, and the Cowork fallback sentence is removed. |
| RM:72 | G56 | 74 | The slug is the folder name, the folder name under `archive/` and, on the GitHub path only, `client-<slug>`. |
| RM:74 | G12 | 76 | The `-2`, `-3`, ... suffix is assigned by `record.py add-transcript` and `add-document`. |
| RM:77 | G01 | 79 | "Chat label" becomes "Session label", minted as `YYYYMMDD-HHMM-xxxx` with the example `20261015-1330-k7q2`. |
| RM:85 | G06, G52 | 87 | The strand index is owned by `record.py` and read by every skill, and `STRAND.md` gains the `## Paused` block, owner `record.py`. |
| RM:87 to 92 | G18 | 89 to 94 | New nine-column header, a separator line and a matching example row; the sentence above it states what `check` blocks and warns on (G06). |
| RM:96 | G11, G38, G40 | 99 | Escapes, comments, new and unknown keys, UTF-8 without BOM with LF, the JSON form and the two time forms are stated. |
| RM:100 | G14, G15 | 103 | `client/2` follows A§7.2's list (no `last_call`, no `page_size`) and the A11 sentence names the three signals. |
| RM:104 | G16 | 107 | `strand/1` follows A§7.7's field list and both stage ladders; `discovery_verdict` and `sop_behind` are gone. |
| RM:108 | G42 | 111 | `SUMMARY.md` front matter is restated and the nine headings are named, with dates "opened, shown, signed off, released and closed". |
| RM:112 | G07, G17, G20, G29, G30 | 115 | `version/1` fields of G17 with the `## Events` block, `blueprint/1` carries `sample_rows`, and the "Internal: never client-facing" line sits directly after the front matter. |
| RM:116 | G01, G15, G47 | 119 | `account` gains `bound_at` and `build_target` with `kind` `own` / `client` / `sandbox`, a `client_workspaces` block is added, `guard_index` gains `client_workspace_ids[]`, and `lease` uses `session_label`. |
| RM:120 | G01, G04 | 123 | `runs[]` uses `session_label` and gains `reconcile {at, mode, classes}`, and `approved_in_chat` becomes `approved_in_session`. |
| RM:135 | G01, G02, G03 | 138 | `lock/2` field list of G02 without `surface`, `session_label` throughout, the history entry as G02, and the E then E+1 then E+2 epoch arithmetic. |
| RM:142 to 152 | G01, G02, G19, G54 | 145 to 156 | The status object uses `schema_newer`, adds `purpose`, `shown` and `signed_off`, drops `surface` and `chat_label`, and the G54 definitions are written out. |
| RM:156 | G17, G26, G27 | 160 to 170 | No `demoed`, the required files become a table with the pinned headings, `released` has no `updates.md`, and missing files warn except at `released`, where they block the release. |
| RM:163 | G01 | 179 | The header reads "key or session label". |
| RM:166 | G08, G13, G45 | 182 | The 44 types of A§7.6:645 with the pinned-marker note, the save entry's body lines, and the roll as G08 states it (pointer with `rolled_to` and `sha256`, `history.json` baseline). |
| RM:170 to 181 | G61 | 196, 198 | An `[A]` row is added, "all nine" replaces "all eight", and `readiness.md` replaces `discovery.md`. |
| RM:191, RM:206, RM:212 | G21, G28 | 208, 223, 229 | In the readiness section only the named tokens changed: `clearance` in the `readiness.md` front matter with its human values, and the assumption line form under `## Assumptions`. |
| RM:272 to 278 | G46 | removed | "Scripts the record copies" is deleted. |
| RM:280 to 282 | G46 | removed | "Migration" is deleted; the file now ends after the `intake-report/1` section (line 287). |

## Left as they were, not named by the list

- Line 134 (live-map `source` values) still names `migration default, not confirmed with the client`.
- Line 60 still has the `deliverables/handoff/*` row beside the v2 rows, although the `non-platform` list no longer names it.
- Line 70 keeps `personal-names-index.json` in the home list, since only `leases.json` and `claims/` were named for removal.
- Line 83 (the reading contract) still says "A chat".
- In RM:68 the sentence "Within-record contention depends on none of them." was removed with the Cowork fallback sentence, because it had no antecedent without it.
- In RM:68 the phrase "where the user's firm name and its renderings live" was dropped from `leak-terms.txt`, since G34 puts the firm name and renderings in `settings.json`.
