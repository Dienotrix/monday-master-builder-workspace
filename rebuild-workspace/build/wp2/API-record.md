# `record.py` part 1, for the part-2 agent

Date: 2026-10-14. Internal build file: never client-facing.

`plugins/monday-master-builder/scripts/record.py` (1,437 lines), tested by `tests/unit/test_record.py` (48 tests). Part 1 built the frame and `status`, `check`, `log`, `guard`, `freeze`, `add-transcript`, `add-document` and `strand open|list|pause|kind|close|summary|resume` (`strand resume` is G05's addition to the catalogue). Part 2 builds `lease *`, `version *`, `card`, `home init` and `init`, which today answer "not built yet" with exit 3.

## The CLI frame

- Launch: `[interpreter, <plugin root>/scripts/record.py, (--record <client folder>), <command> [action] flags...]`. The record is the current folder unless `--record` (a global flag, before the command) names one; `main()` exits 3 when the folder holds no `CLIENT.md`. Part 2's `home init` and `init` run where no record exists yet, so they need that check skipped: test `name` in `main()` before the `CLIENT.md` test.
- Output: one JSON object, written by `emit()` as UTF-8 with LF. Every command but `status` gets the envelope `{"ok": code != 1, "command": "<name>", **payload}`; `status` prints the status/1 object bare (G10, G19).
- Errors: raise `mc.Refusal(*findings)` (exit 1, `"refusals": [...]`), `mc.CannotRun(...)` (exit 3, `"error": {...}`); a finding is `(file, field, problem, expected)` with `file` record-relative POSIX. `refuse(*reasons)` drops `None` entries and raises one Refusal listing the rest, so a command lists every failing reason at once. Any other exception becomes exit 3 with the envelope. A usage error (argparse) is exit 3 through `Parser.error`, as are `migrate` and `tools-check`.

| Exit | When |
|---|---|
| 0 | done, nothing to report; `status` whenever it printed |
| 1 | any refusal; `check` with a blocking finding |
| 2 | done with warnings only (`check`; G22's `version mark signed-off`) |
| 3 | could not run: missing record, file, template or `plugin.json`, malformed lock or `account.json`, mutex timeout, usage error, not built yet, unexpected exception |

## Adding a subcommand

1. Write `def cmd_x(root, args):` returning `(exit code, payload dict)`.
2. Put it in `COMMANDS` in place of `None` (the key is the command as typed: `"lease take"`, `"home init"`).
3. Add its flags in `build_parser()`: the parser of each command is `groups[name]`, created from `COMMANDS`; add a flag with `groups["lease take"].add_argument(...)`. Required flags are usage errors (exit 3); validate values in the command and refuse (exit 1), as G10 asks.
4. Inside: `with mc.record_mutex(root):`, then `refuse_newer(root, *paths it will touch)` before anything is written (C13, G57), then validate with `refuse(...)`, then write. After writing any `STRAND.md`, call `refresh_index(root)` in the same hold (G06). Log through `insert_entries(root, [new_entry(strand, type, version, key, body_lines)])`; never write `log.md` another way.

## Shared helpers inside `record.py`

- Reading: `read_doc(root, path) -> (fields, body, text)`; `write_fm(root, path, updates)` (backup, then in place, only when a value changes); `front_text(pairs)` builds a front-matter block; `strand_folders(root)`; `version_folders(strand folder)` sorted by number; `vnum("v1.0") -> (1, 0)`; `runs(root, folder)` (a strand's `build.json` `runs[]`); `strand_doc(root, short) -> (folder, path, rel, fields, text)` with the schema refusal done; `holds_lease(root, short)` returns the refusal tuple or `None`.
- Schemas and templates: `schema_for(rel)` (which schema a place must carry), `refuse_newer(root, *paths)` (always also reads `CLIENT.md`, `log.md`, `account.json`, the lock and `history.json`), `fill(name, values)` (a template with the owned keys set and `updated` stamped; exit 3 when the template or a key is missing, G31).
- Log (G08): `split_log(text) -> (head, entries)`, `entry_parts(entry) -> (header groups or None, body lines)` with groups `(time, strand, type, version, key)`, `values_of(body)` (the `key: value` parts, ` · ` split), `entries_in(root)` over the record log and every rolled log, `insert_entries(root, new, removed=())` (the one log writer; it moves `.work/history.json` too), `roll_hash(entries)` (sha256 of the moved entries in file order, each LF-ended, trailing blank lines dropped). Part 2's `version release` roll uses `insert_entries(root, [pointer], removed=moved)` and `roll_hash` exactly as `cmd_strand_close` does, with `versions/<v>/log.md`, `version` set to the version, and the pointer typed `release` with key `released`; `check` already verifies any rolled log under `strands/*/versions/*/`.
- Index and blocks: `refresh_index(root, opened=None)`, `index_rows(root)`, `set_block(text, "## Heading", lines)` (G52's `## Paused`; part 2's park writes it with the same call), `section(body, heading)`, `heading(body, name)`, `last_line(text)`.
- Check: `Check(root).run()` returns the object with `blocking`, `warnings`, `newer`; after `run()`, `check.required(folder, vdir, version fields, version body, build)` gives G27's missing items per state row, which `version release` can reuse to refuse with the list (C167); `summary_plan(root, folder, draft) -> (text, reasons)` is G42's validation, which `version release --summary-plan-sha` can reuse.
- Tables: `LOG_TYPES` (between `# pinned: log-types` and `# end pinned`), `STATES`, `CLEARANCES`, `LADDER`, `OUTPUT_CLASS`, `ROWS`, `BUDGETS`, `SUMMARY_HEADINGS`.

## How the tests build a plugin root and a home

- `make_plugin(target)` copies `tests/unit/fixtures/plugin/` and then `scripts/mmb_common.py` and `scripts/record.py` into `target/scripts/`. `Base.setUpClass` builds one such root per class and loads `record.py` from it with `importlib`, so `PLUGIN_ROOT` and `TEMPLATES` point at the copy; `mmb_common` is the one module the test file imported, so `mock.patch.object(mc, "now_utc", ...)` pins the clock for record.py too.
- `Base.setUp` copies `fixtures/home/` to a temporary folder whose name holds a space, sets `MMB_HOME` to it and `HOME`/`USERPROFILE` to an empty canary, pins the clock to `2026-11-05T14:30:00Z`; `tearDown` asserts the canary and the real default home are untouched (C17).
- Helpers: `run_record(*argv) -> (code, data)` runs `main(["--record", root, ...])` in process and asserts every finding has four non-empty parts (C21); `ok(...)` asserts exit 0; `refused(...)` asserts exit 1 and an unchanged tree and returns the `(file, field)` pairs; `check()` returns `(code, blocking pairs, warning pairs)` and asserts `check` wrote nothing; `tree()` hashes the record without `record.mutex`; `fm`, `edit_fm`, `edit_json`, `append`, `stage` (a staging or source file in the temp folder), `entries(rel)`.
- Subprocess runs use `[sys.executable, <copy>/scripts/record.py, ...]`, no shell, with `PYTHONDONTWRITEBYTECODE=1` (C52); the C18 test drops that variable and gives the interpreter a home of its own to prove G49's first line alone keeps the plugin folder clean. A subprocess cannot pin the clock, and the fixture's times lie after today, so assert on blocking findings only there.
- Template tests patch `self.rec.TEMPLATES`; in stage 3 point `make_plugin` at WP7's real `templates/` instead.

## Choices taken where the decisions are silent (worth the user's nod)

- `--record` global flag; `guard --file X` without `--from` prints the sha (the read half); `--expect-sha none` creates a new file; `guard` refuses logs, `SUMMARY.md`, frozen blueprints, `.work/` and non-Markdown files, refuses a staged `CLIENT.md` that changes `lease`, stamps `updated`, and rewrites the index after a `CLIENT.md` or `STRAND.md` write.
- `log` refuses a blank body line; `--body-file` drops trailing blank lines.
- `strand kind` needs `--reason`, logs `kind: <old> to <new> · reason: ...`, sets `output_class` to the new kind's default unless `--output-class` is given, and resets `stage` to `new` when the old stage is not on the new kind's ladder (the fixture's `intake` under `non-platform`).
- `add-*` take `--redactions N` (default 0, G13's count); `--came-with` only with `--kind document`; the output carries `lines` for a `.txt` file (C10).
- `status --strand` of an unknown strand is a refusal (exit 1); a `CLIENT.md` that does not parse is exit 3 for `status`.
- `check` also blocks on a slug other than the folder name, a `STRAND.md` or `version.md` whose identity fields disagree with its folder, a strand folder without `STRAND.md`; it warns on a relative link that does not resolve or leaves the record, an out-of-form or unlisted type in an existing log entry, a version folder without `version.md`; it checks every `blueprint-r*.md` against its approval, not only the current revision.

## Fixture changes

None: `record.py check` on an untouched copy of `tests/unit/fixtures/home/clients/larkmoor-joinery/` exits 0 with no findings, in process at the pinned clock and as a subprocess at today's clock.

## What could move into `mmb_common` later

`emit`, `Usage`/`Parser` and `refuse` (ledger.py prints the same envelope), `schema_for` and `refuse_newer` (every writer needs the G57 refusal), `split_log`, `entry_parts`, `values_of` and `roll_hash` (`archive_check.py` and the graders read the log), `strand_folders`, `version_folders`, `runs`, `front_text`. `tools/lint_plugin.py` could add `("log-types", "scripts/record.py")` to `PINNED` once `record-map.md` carries a `Pinned: log-types` heading; until then `test_C51` compares `LOG_TYPES` with record-map's sentence.

## mmb_common

No bug found. Not a bug but on the record: `mmb_common.py` is 466 lines against C26's 250, and `test_mmb_common.py` (645) with `test_record.py` (846) is far past the 480 for both test files.

---

# `record.py` part 2

Date: 2026-10-15. Internal build file: never client-facing.

`record.py` is now 2,058 lines (1,437 after part 1), `mmb_common.py` 479 (466). Part 2 is tested by `tests/unit/test_record_part2.py` (646 lines, 29 tests), which reuses `test_record.py`'s `Base`; part 1's catalogue test now asserts every entry is built. The suite is 135 tests, green on Python 3.9 and 3.14; lint 0 errors.

## What part 2 built

- **`lease take [build] --strand`**, **`lease refresh --epoch --label [--run-id]`**, **`lease release --epoch --label`**, **`lease status`**, **`lease break --epoch --label --for-strand --user-yes --account-id --choice resume|park [--park-yes]`**: thin callers of the `mmb_common` primitives under the record mutex, with `refuse_newer` before any write. A missing label or epoch is a refusal (exit 1, C90), never a usage error. A take returns the minted label once, with a `carry` line; take and release write a `lease` log entry at the strand's position (`taken, epoch N` / `released, epoch N`, key the label, as the fixture's own entry reads); a refresh writes none. A break writes G03's three entries in one insert (record level, the holder's position with its version, the taker's position), each keyed by the holder's label; a park also sets the holder's `STRAND.md` to `paused` with a `## Paused` line naming the run, the version, the reconcile counts and the user's park words, and refreshes the index. The output's `next` names the take that follows.
- **`version open --strand [--version]`**: `version.md` from the template (state `planned`, purpose from the number, `opened` today), `STRAND.md` `version` and `version_state: planned`, a `version · opened` log entry, the index. Default: the next minor after the highest version folder, `v0.1` first.
- **`version mark shown|signed-off --strand [--version] [--date] --words` with `--audience [--account]` (shown) or `--by [--go-on]` (signed-off)**: G20 to G24. `shown` appends its date to `shown` (every repeat kept) and an event under `## Events`; `signed-off` lists the strand's structural assumptions still `assumed` (G21), and without `--go-on` a non-empty list records nothing and exits 2; with it the event is recorded with the list kept beside it and exits 2 (0 when the list is empty). Never exit 1 on that ground. Both advance the stage (G16) and leave the version state alone, and log at the strand's position with the event date as key.
- **`version condense-plan --strand --from <plan.json>`** and **`version condense-apply --strand --plan-sha`**: G25. The plan is validated and stored as `.work/strands/<folder>/condense-plan.json` with each file's sha; apply removes each line once through `guarded_write` (backup, in place, `updated` stamped) and logs `version · - · condensed`. Both refuse while any strand holds the lease.
- **`version release --strand --condense-plan-sha --summary-plan-sha [--version]`**: G26. One refusal lists every reason: the lease held by any strand, a state other than `audited`, every file `check.required` finds missing for the rows the version has passed (G27), the two files it freezes (`solution/build.json`, `solution/backlog.md`) when absent, a snapshot already present, from `v1.0` a missing `signed-off` event, and either plan's sha or a file changed since the condense plan. Then, in order: the byte-copied snapshots, `version.md` released, the condense plan applied, `SUMMARY.md` written from the stored summary plan (rendered after the version is released, so `versions` and `summary_current_to` name it), the version's log entries rolled into `versions/<v>/log.md` with one `release · released` pointer, `STRAND.md` `version_state` (when current) and `summary_current_to`, the index. It returns `release_checks`, the released-row gaps found afterwards (empty, exit 0).
- **`card --strand`**: G25. `client-card.md` copied byte for byte to `<home>/cards/<slug>.md`, an existing card backed up under `.work/backup/home/`, a `closeout · card` entry at `-`.
- **`home init`** and **`init`**: built against the stand-in templates; stage 3 accepts them with WP7's. `main()` skips the `CLIENT.md` test for these two (`NO_RECORD`).
  - `home init [--firm-name --firm-rendering… --default-account-slug --default-account-id --never-show "<id>=<name>"… --archive local|github --github-account --home <folder> --update]`: the six folders, `local/settings.json` in G34's key order (never replaced without `--update`; with it, a backup in `local/backup/` and only the named answers changed, `created` kept, `github_account` dropped when the archive becomes local), `local/leak-terms.txt` and `local/sandbox-accounts.txt` empty, `sandbox/SANDBOX.md` from `templates/other/`. `checks` reports `python`, `plugin_root` and `connector` ("checked by the session"), and `git` and `gh` through `shutil.which` only when the archive in effect is GitHub. Warnings (exit 2): every folder from the home up to the drive's root holding a `CLAUDE.md` (G37), and a GitHub tool absent on the GitHub path. A home other than the default carries `set_mmb_home` (the `env` entry, and the `setx` or profile line for this system).
  - `init --slug --name --topic --title --kind --reason [--output-class]`: the record at `--record`, or `<home>/clients/<slug>/`. `CLIENT.md` and `log.md` filled, `account.json` and (platform or hybrid) strand 001's `build.json` as template copies with only `client_slug` and `strand` set and every binding value `unbound`, the folder's own `CLAUDE.md`, a `.gitignore` from `client-gitignore.txt` only when `local/settings.json` says `archive: github`, the first lock through `mc.lease_init`, a `created` entry, then strand 001 through the same code as `strand open`. The result checks clean (C39).
- **Refactors of part 1, behaviour unchanged**: `strand open` is split into `strand_reasons`, `strand_files` and `place_strand`, which `init` shares; the roll that `strand close` wrote inline is `roll()`, which `version release` shares (strand close's file is byte-identical).

## The heartbeat rule (a part 1 defect, fixed in the one place an age is computed)

`mmb_common.heartbeat_age` returned now minus heartbeat, so a heartbeat in the future gave a negative age that read as fresh. The rule now: a heartbeat up to five minutes (`CLOCK_SKEW`, 300 seconds) ahead of this machine's clock reads as 0 minutes old, which absorbs ordinary clock jitter; one further ahead returns minus the whole minutes it lies ahead and is never fresh, because the clocks disagree and the stamp proves nothing about the holder. So `status` and `lease status` say `fresh: false` with the negative age; `check` warns (file `.work/lock.json`, field `heartbeat_at`, "heartbeat N minutes ahead of this machine's clock: the clocks disagree"); a take's refusal says the heartbeat is "not fresh: the clocks disagree"; and break condition 1 holds, the epoch fence still refusing a woken holder's next write. Condition 4 is unchanged: with a run on the lock, the reconcile must still be stamped after the heartbeat, so such a break waits (failing closed where objects could be lost). `heartbeat_words` gives every message the same phrase. Tests at the pinned clock still see the fixture as fresh; at today's clock the untouched fixture copy now checks with exactly that one warning (exit 2, nothing blocking).

## Choices taken where the decisions are silent (worth the user's nod)

- **G23 sits in three small functions** (`purpose_for`, `sign_off_updates`, `next_version`, under a comment block naming G23): purpose follows the number only, a signed-off `v0.x` stays a proof of concept and the output's `next` proposes `version open --version v1.0`. The alternative reading is a change to `sign_off_updates` (return `{"purpose": "working-solution"}` for a `v0.x`) and `next_version` (return `v1.0` once a `v0.x` is signed off).
- **Signed-off follows G22's two calls**: the first call lists and records nothing (exit 2); the user's go-on is `--go-on`. A second signed-off on one version records a second event and moves `signed_off` to the newer date.
- **`version open`** refuses a version not above the highest opened (which covers an existing folder) and a non-canonical one (`v01.2`); it does not refuse while the strand holds the lease, since a meeting session may open the next version while a build runs (A§9.8).
- **Condense plan form**: a JSON list of `{"file", "line", "survives_in"}`, record-relative. A current file of the strand is a Markdown file under it that `guard` may write and that is not under `versions/`; `line` must equal a whole body line (front matter is never condensed), and a line listed twice must occur twice; `survives_in` must exist when the plan is made and differ from `file`, so a release-time snapshot cannot be named before it exists; an empty list is how a release with nothing to condense says so. The stored plan is `{strand, entries, files: {path: sha256}}`.
- **Release order and its pointer**: the pointer entry carries a third line, `frozen: build.json, backlog.md · condensed lines: N · summary: written|refreshed`, so no separate `summary` or `version` entry is written for a release. A missing `--condense-plan-sha` or `--summary-plan-sha` is a refusal, not a usage error.
- **`lease break`** refuses an unknown `--for-strand` and user words that span lines before calling the primitive (a log body line is one line); when the taking strand is the holder itself (the holder's own fresh session resuming), the third entry would repeat the second and is not written.
- **`init`** refuses a folder whose name is not the slug and a folder that is not empty (naming up to six of its entries); it reads the archive choice from `local/settings.json` (local when there is none); it leaves `account_kind` and `build_target` at the template's own-account values, because the build target is a setup question asked after `init` and written through `guard` and `ledger.py bind`. The client folder's `CLAUDE.md` text lives in `record.py` (`CLIENT_CLAUDE`), since WP7's list has no template for it.
- **`home init`** takes `--home` only as an absolute folder; the GitHub tools are checked whenever the archive in effect is GitHub, a kept settings file included; `--firm-rendering` defaults to the firm name; `--update` refuses a settings file with a newer schema.
- **`card`** refuses (exit 1) when the record has no `client-card.md`.

## Fixture changes

Three stand-in templates added under `tests/unit/fixtures/plugin/templates/`: `record/build.json`, `record/client-gitignore.txt` and `other/SANDBOX.md` (WP7's names); `fixtures/README.md` says so and notes the real-clock result above. The record tree itself is unchanged.

## Not covered by part 2's tests

C37 (the two doors, which G32 moves to WP8's `first-run.md`) and the connector half of C33 (the session's roster). C83 to C86, C97 and C100 stay with `test_mmb_common.py`. Stage 3 re-runs C28 to C44 with WP7's templates; the Windows runs remain.

## Changed by the lease fixes, 2026-10-15

- **`lease sync`** (no flags): both mirrors rewritten from the lock, no log entry. **`lease repair --user-yes "<words>"`**: rebuilds a missing, torn or malformed lock (refused when it is sound), one record-level `lease` entry keyed `repaired`, and `next` naming the take that comes next. Both are in `COMMANDS` (C25).
- `lease status` and `status --json` carry `lease.reserved_for`; `lease break`'s output carries it too.
- A failure after a lease change committed (the log insert of a take, a release, a break or a repair, a park's `STRAND.md`, the index) exits 3 with `"error"` field `committed` and a `"committed"` object holding what was committed and the entries still to write; a take's also holds its epoch and label.
- `check` blocks on a malformed lock (`mmb_common.lock_findings`) instead of exiting 3 (a lock that is not JSON still exits 3, naming the repair), and its mirror findings name `lease sync`.
- `init` repeats the empty-folder check inside the record mutex. `refuse_newer(root, *paths, skip=())` can leave out a fixed file (the repair skips the lock).
