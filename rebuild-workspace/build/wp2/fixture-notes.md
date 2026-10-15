# WP2 fixture notes

Date: 2026-10-14. Internal build file: never client-facing.

Built in the plugin repository: `tests/unit/fixtures/home/` (a home as `home init` leaves it, holding one bound `client/2` record with strands 001 and 002 and a held lease), `tests/unit/fixtures/crlf/` (one CRLF copy of `CLIENT.md`), `tests/unit/fixtures/plugin/` (the stand-in plugin root of G31), `tests/unit/fixtures/README.md` and `tests/unit/fixtures/.gitattributes`; `tools/` untouched. Every version is below `v1.0` while G23 is open. The tree was checked against `record-map.md` and this folder's `DECISIONS.md`, with a throwaway cross-check (not kept) of field orders, both lease mirrors, the binding mirror, every sha256, the log baseline, the strand index, the live map against `live_objects`, references and links, quote locations and the absolute-path patterns of G30: no mismatch.

## Open choices

Where neither `DECISIONS.md` nor `record-map.md` settles a point, this is what the tree does.

1. **Stand-in templates (done).** Added as G31 describes, under `tests/unit/fixtures/plugin/`:
   - `.claude-plugin/plugin.json` carries `name`, `displayName`, `version` `0.1.0` and a one-line description. It has no author and no repository address.
   - `templates/record/` holds `CLIENT.md`, `log.md`, `account.json`, `lock.json`, `STRAND.md`, `readiness.md`, `exclusions.md` and `version.md`. Each is cut from the matching file in the tree: strand 002 for the three strand files, 001's `v0.1` for `version.md`. Each keeps the same front-matter keys in the same order, including the keys `record.py` sets (G16, G17, G28), with the values a fresh file has. Keys `record.py` fills that have no default (`slug`, `name`, `strand`, `title`, `opened`, `updated`, and so on) are `""`. `lock.json` is G02's template lock, and `account.json` has `unbound` account fields, empty blocks and an empty lease mirror.
   - The real `plugins/monday-master-builder/templates/record/` holds only a `.gitkeep`, so there was no real template to mirror. The names follow WP7's template list (BUILD-PLAN WP7) laid out flat under `templates/record/<name>` (G31), so stage 3 can copy the real folder in place of this one without changing the tests.
   - Three gaps remain for stage 3. WP7's list has no lock template, so either WP7 adds `lock.json` or `init` writes G02's lock through `mmb_common`, which C82's one-writer rule favours. No `blueprint.md` stand-in was added, although the brief named G29: no `record.py` subcommand fills `blueprint.md` from a template (`solution-blueprint` writes it). `build.json` was also left out, because only `init` places a template copy of it (G43).
   - `.gitattributes` also marks `plugin/**` as `-text`.
2. **Reference clock.** Nothing pins a clock for the fixture. The tree assumes `2026-11-05T14:30:00Z` and a machine on UTC, so log headers, `updated` values and labels equal the UTC stamps. Every fixture time is later than today, so an unpinned clock gives a negative heartbeat age, which G40 does not define. Tests must pin the clock.
3. **A lease on an audited version.** 001 holds a fresh lease (epoch 2, `run_id` null, taken after the showing) while `v0.1` is `audited`, so one tree serves both the version-file clauses and the lease clauses. No script rule or `check` rule forbids this (G50, G53), but no flow takes a lease on an audited version. Running and interrupted runs are made by mutating a copy.
4. **Schema strings outside G57's list.** The tree uses `blueprint/1` (from record-map) for `blueprint.md` and for its frozen copy. It uses `exclusions/1` and `audit/1` for the other two, following record-map's `<file-stem>/1` rule. G57's list of known schemas has none of the three. Read literally, the stem rule would give the frozen copy `blueprint-r1/1`, which a byte copy cannot carry. `check` must accept these schemas rather than treat them as an "unexpected name".
5. **Front matter of files nobody pins.** `readiness.md` has `schema`, `clearance` and `updated`. `exclusions.md` has `schema`, `strand` and `updated`. `blueprint.md` has `schema`, `strand`, `revision`, `sample_rows` and `updated`. `audit.md` has `schema`, `strand`, `version` and `updated`. Each carries `updated` because G38's writer sets it on every write.
6. **`readiness.md` body.** The parts follow record-map's order under capitalised headings, `## Note` to `## Questions`, to match G21's `## Assumptions`. Record-map says the parts sit "under the same names", which are lower case. Only the assumption lines have a pinned form. The list has one structural assumption still assumed, one structural assumption accepted and one `gap`, so G21's filter has entries to exclude.
7. **The log.**
   - No source says whether `lease take` or `lease release` writes a log entry; G03 covers only a break. The tree has a `lease` entry for the second take and folds the first take and release into the `build` entry.
   - Only the save stem and the pointer keys are settled. The other keys are chosen: `opened` for a strand open, the slug for `created`, the account slug for `binding`, `r1` for the approval, the run id for the build, the date for `shown` and the label for `lease`.
   - The email's `asked_by` is 001, because 002 opened after the email was saved.
   - `log.md` carries "Internal: never client-facing" before its title, following G30 and record-map, even though the example in A§7.6 has no such line.
8. **Table forms.** An empty live-map `dependants` cell reads `none`, mirrored as `[]` in JSON. The live map has a separator line, although record-map's pinned block shows none. `STRAND.md` `workspaces` uses the `client_workspaces` form, `core:40000001`.
9. **Time formats with no pinned form.** `monday_bound_at` holds the UTC stamp of `account.bound_at`, because G15 compares the two as a mirror. `monday_tier_read_at` is a date, and `last_verified` is a date on both sides of the live map.
10. **`approved_in_session`.** No lease is held when a revision is approved, so the approving session has no minted label. The tree stores the plain string "blueprint session of 2026-10-26".
11. **JSON blocks `record.py` does not read.**
    - They follow record-map's field lists rather than the longer example in A§7.3: no `approval_mode`, `rests_on`, `workspace`, `assumption_refs` or `workspaces_ok`, and `change_check.verdict` rather than `result`.
    - `runs[]` carries `another_build_running`. Record-map's `runs[]` list leaves it out, but its version-state table and G27 require it.
    - `role` and `url` are named without a value set, so both are null.
    - The ended run has no `reconcile`.
    - In JSON, `revision` is the integer 1; in front matter it is the string `"1"`.
12. **Files left out that a script would have written.** `.work/record.mutex` (created on first use), `.work/backup/`, the client folder's `CLAUDE.md` (stage 3; record-map's table also lacks the row A§7.1 has for it), `sandbox/SANDBOX.md` (placed from a WP7 template, G58), call and document snapshots, and `meetings.md`. Each empty home folder holds a `.gitkeep`, which the copy recipe drops.
13. **002's `exclusions.md`.** Kept, because `strand open` places it (G43), although the brief named an exclusions file only where sample rows are planned. It also keeps `solution/` from being an empty folder.
14. **`.gitattributes`.** `home/**`, `crlf/**` and `plugin/**` are marked `-text`. A Windows checkout with automatic CRLF conversion then keeps the bytes the recorded sha256 values hash, and keeps the CRLF copy as CRLF. A repository-level rule would do the same; G60 asks for the same rule on the GitHub archive path.
15. **The CRLF file.** The copy is of `CLIENT.md`, because it has front matter with comments and the strand index (C08, C11). It sits at its own relative path under `crlf/home/`, so it can be laid over a copy of the home. The test makes CRLF transcripts (C10, C60) from the LF transcript.
16. **Account defaults.** `sample_data_in_account` is `unanswered`, as asked, although the comment in A§7.2 says the bind step sets `not-needed` on an own-account record; G14 keeps it silent. In the settings, `default_build_account` is the bound account, and `never_show_workspaces` has one entry so a filled list is tested.

## Differences found

`DECISIONS.md` against `record-map.md`:

- RM:138 says the lock's string fields, `run_id` included, are "each a string while state is held". G50 sets `run_id` to null at the take, until `run start`. G02 uses the same wording as RM:138, so `DECISIONS.md` also disagrees with itself here. The tree follows G50.
- G57's list of known schemas leaves out `blueprint/1`, which RM:115 names, and the `<file-stem>/1` schemas RM:115 prescribes (choice 4).
- G08 defines an entry hash with trailing blank lines dropped and every line ending in LF. RM:182 says only "line endings normalised to LF". The baseline in `.work/history.json` follows G08.
- G27 and RM's version-state table require `another_build_running` on a running run, but RM:123's `runs[]` list leaves it out (choice 11).

Inside `record-map.md`, or between the brief and the decisions:

- The pinned live-map block at RM:130 has no separator line, while the strand index at RM:92 has one (choice 8).
- The brief placed the transcript in `inputs/`. G12 and RM:20 place it in `calls/<stem>.transcript.txt`, which is where it is.
- G31 puts stand-in templates in the fixture folder, and the first brief did not list them. They were added in a second pass (choice 1).
- G02 describes the template lock that `init` places, but WP7's list of 35 templates has no lock file (choice 1).
