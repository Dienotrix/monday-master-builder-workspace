# WP3 contract checklist: `ledger.py`

Date: 2026-10-16. Internal build file: never client-facing.

This file turns the acceptance of work package WP3 into numbered, separately testable clauses, copies the shapes the code must honour, and lists what the sources leave open or state two ways. It decides nothing. A builder ticks each clause by one test or one inspection; a reviewer reads section 4 before writing code, because every entry there is a choice the sources do not make. The approved plan (`PLAN.md`) is a constraint, not a source of new rules: its answers to Q1 to Q4 and the thirteen nods of its section 8 are carried where a clause rests on them, and each entry of its section 7 is carried into section 4.

## 1. Header: sources and how to read this file

### Sources

| Short | File | What was read |
|---|---|---|
| BP | `rebuild-workspace/design/BUILD-PLAN.md` | WP3 block (lines 126 to 151; the acceptance list is lines 134 to 149, one bullet per line), section 0 and A11 (11 to 24), stage notes (62 to 70), the inputs line of WP1 (101), file ownership (365 to 386), section 4.4 (468 to 470), headless rows H23 to H26 (492 to 495), H35 (504), H39 (508) and H58 (527). Cited as `BP:line` |
| A§ | `rebuild-workspace/design/ARCHITECTURE.md` | 5.3 and 5.4 (338 to 362), 7.1's file map (390, 398, 399, 417) and its `.work/` paragraph (438), 7.3 (484 to 582), 7.8 (689 to 718), 8.6 (788 to 802), 8.7 steps 23 to 25 (807 to 809), 8.9 (823, 825), 8.10 (829, 831), 8.11 (833 to 837), 9.4 to 9.10 (875 to 967), 10.4 (1028), 11 (1036 to 1095). Cited as `A§section:line`. Line numbers are those of the file today; WP2's contract cites some of these lines one lower, because a design touch-up added a line to 5.3 after it was written |
| AM | `rebuild-workspace/design/AMENDMENTS.md` | A29 (10 to 14), A28 (16 to 20), A25 (46 to 58), A24 (40 to 44), A21 (78 to 85), A18 (104 to 110), A17 (112 to 120), A11 (173 to 177), A1 (179 to 183), A3 (188 to 195). Cited as `AM:line` |
| RM | `monday-master-builder/plugins/monday-master-builder/shared/record-map.md` | file map (1 to 30), `.work/` and home paragraphs (68, 70), ids and keys (75, 77), `client/2` (103), `account/1` (119), `build/2` (123), `live-map/1` (127 to 134), `lock/2` (138 to 142). Cited as `RM:line` |
| NO | `shared/native-objects.md` (same plugin folder) | the whole file, 202 lines. Cited as `NO n` for a section, or `NO n:line` for a line (2.1 is line 15, 2.6 is lines 36 to 57, 3 is 59 to 88, 4 is 90 to 123, 5 is 125 to 158, 6 is 160 to 188, 7 is 190 to 198, 8 is 200 to 202) |
| GO | `shared/monday-gotchas.md` | entries G-07 to G-11, G-69, G-71 to G-90 and G-91 to G-108. Cited by entry id as `G-nn`; the WP2 decisions use `Gnn` without the hyphen, so the two never collide |
| SF | `shared/safety.md` | sections 1 to 5 and 9 (approval classes, the irreversible rows IR-01 to IR-15, the approvals rule, recovery) |
| RB | `shared/read-back.md` | the table (lines 20 to 53), in particular the AI-kinds row at line 53 |
| AI | `rebuild-workspace/design/ai-offerings-findings.md` | the whole file, 77 lines (the source the user approved for agent, Vibe app and workflow shapes, PLAN Q2). Cited as `AI:line` |
| Gnn | `rebuild-workspace/build/wp2/DECISIONS.md` | G01, G02, G04, G05, G09, G10, G11, G15, G39, G40, G47, G48, G49, G50, G51, G53, G57, the amended G09, G39, G50, G51, G53 and the lease fixes (590 to 624), C129 (630). Cited as `Gnn` |
| MC | `plugins/monday-master-builder/scripts/mmb_common.py` and `rebuild-workspace/build/wp2/API-record.md` | the function list, the docstrings of `MMBError`, `json_text`, `write_file`, `guarded_write`, `read_json`, `record_mutex`, `lease_refresh`, `lease_release`, `lease_fence`; the CLI frame (API-record lines 1 to 60). Cited as `MC:name` and `API:line` |
| PLAN | `rebuild-workspace/build/wp3/PLAN.md` | all of it. Cited as `PLAN §n`, with `PLAN §7.n` for an entry of its conflicts list and `PLAN §8.n` for a nod |

Authority order (BP:5, HANDOFF): AMENDMENTS over ARCHITECTURE over BUILD-PLAN. `record-map.md` and the other `shared/` files are stage-1 files that lag A24 to A28 and A17 to A18 in places; where RM or SF or RB and A§ differ, section 4 lists both. A29 governs the test inputs: every classification, compare and reconcile clause here is graded against synthetic reads first.

### How to read a clause

Each clause is one requirement. The line under it gives:

- **Src**: where it comes from, as BP line, A§ section and line, RM line, NO section, AM line, Gnn, PLAN section. "A§ only" or "BP only" marks a clause that rests on one source; section 4 lists the whole family.
- **Accept**: when it is accepted. The vocabulary is fixed:
  - `stage 2 unit`: a unit test against WP2's unit fixture (`tests/unit/fixtures/`) or against the synthetic reads of A29, with the Windows side simulated where it matters (`PureWindowsPath`, a CRLF copy of the fixture tree, an injected clock). Test record variants (an own-account record, a client-account record, a sibling client, a held and a broken lease) are built in each test's setup (PLAN §8.2).
  - `stage 4 headless Hnn`: the headless row that exercises the clause once WP14's runner and the seed records exist. WP3's rows are H23 to H26 and the ledger halves of H35, H39 and H58 (BP:149).
  - `Windows run`: needs a real Windows machine (PLAN step 10).
  - `macOS run`: needs a real Mac (PLAN step 11).
  - `capture (A11-1)`: anything the synthetic reads cannot settle, which waits for a scrubbed read-only capture once the user names a test workspace (A29, AM:10 to 14). A clause graded against synthetic reads says "met against synthetic reads; confirmed at capture (A11-1)". The capture takes no default and nothing in this package writes to any account.
- **Test**: one line saying how to tick it.

Clause ids use the prefix `K` so they never collide with WP2's `C` numbers. Gap ids use `W`. A clause that depends on an open gap names it ("see W42"); it does not settle it.

---

## 2. Clauses

### 2.1 Runtime and cross-system rule

- **K01** `ledger.py` imports only the standard library: no third-party package.
  - Src: A§5.3:340; AM:42 (A24). Accept: stage 2 unit; Windows run. Test: walk the script's imports with `ast` and check every module is standard library.
- **K02** `ledger.py` and its three test files use Python 3.9 syntax only: no `match` statement, no `X | Y` union evaluated at runtime.
  - Src: A§5.3:340; BP:148 (last sentence). Accept: stage 2 unit. Test: `ast.parse(source, feature_version=(3, 9))` on each file, run under the newest Python.
- **K03** `sys.dont_write_bytecode = True` is the first statement after `import sys`, before `mmb_common` is imported.
  - Src: BP:134; G49. Accept: stage 2 unit. Test: parse the module; the statement after `import sys` is that assignment, and the `mmb_common` import node follows it.
- **K04** No `__pycache__` or any other file appears in the plugin folder after any subcommand runs.
  - Src: BP:134; G49 (the same test as WP2's C18). Accept: stage 2 unit; Windows run. Test: run every command form from a writable temporary copy of the plugin folder, in one test with the bytecode variable dropped from the child's environment, and assert the copy's file list is unchanged.
- **K05** No shell step: no `os.system`, no `shell=True`, no `os.popen`; any `subprocess` call takes a list.
  - Src: A§5.3:340; AM:42. Accept: stage 2 unit. Test: search the script for those names.
- **K06** Every path is built with the standard library's path handling from the record folder it is given; none is built by joining strings with a fixed separator or from a literal `~`.
  - Src: A§5.3:340; AM:42. Accept: stage 2 unit; Windows run. Test: run every command form against a record under a folder whose name holds a space; search the script for `"/"` and `"\\"` joins.
- **K07** Every JSON file `ledger.py` writes is two-space indented, `ensure_ascii=False`, LF line endings, a final newline, key order kept.
  - Src: BP:134; G11; MC:json_text. Accept: stage 2 unit; Windows run. Test: after each writing subcommand, the file's bytes equal `mmb_common.json_text(json.loads(bytes))`, and the key order of every untouched block equals its order before the call.
- **K08** JSON is read with either line ending and with or without a leading byte-order mark, and parses to the same value.
  - Src: G11; MC:read_json. Accept: stage 2 unit; Windows run. Test: run `check` on an LF, a CRLF and a BOM copy of `account.json` and one `build.json`; the output is identical.
- **K09** Text `ledger.py` composes outside JSON (`live/live-map.md`) is UTF-8 with LF only and no byte-order mark.
  - Src: A§5.3:342; G11. Accept: stage 2 unit; Windows run. Test: simulate Windows, write the file, assert no `\r` and no BOM.
- **K10** No write path renames or deletes: the script never calls `os.rename`, `os.replace`, `os.remove`, `os.unlink`, `shutil.move`, `shutil.rmtree`, `Path.unlink` or `Path.rename` on a record file.
  - Src: A§5.3:341. Accept: stage 2 unit; Windows run. Test: spy on those calls while every writing subcommand runs; compare file identity before and after a rewrite.
- **K11** Every rewrite of an existing record file copies the old bytes into `.work/backup/` first, then overwrites the same file in place, through `mmb_common.write_file`.
  - Src: A§5.3:341; G39; MC:write_file. Accept: stage 2 unit. Test: after a write, the backup holds the old bytes under the record-relative path with a UTC stamp, and the file holds the new. See W20 for the per-strand `build.json.bak`.
- **K12** A record whose `account.json`, `build.json` or lock schema is newer than the plugin knows refuses every writing subcommand with nothing written; `check` still reads it and reports one blocking finding per newer file.
  - Src: G57; A§5.3:343. Accept: stage 2 unit. Test: set `account.json` to `account/2`, run each writing subcommand and assert refusal and an equal tree hash; run `check` and assert the finding. See W36.
- **K13** The files exist: `scripts/ledger.py`, `tests/unit/test_ledger.py`, `tests/unit/test_ledger_read.py`, `tests/unit/test_snapshots.py`, and `tests/fixtures/snapshots/` with the synthetic reads.
  - Src: BP:129; PLAN §8.1. Accept: stage 2 unit (inspection). Test: list the files; the three test files load and run.
- **K14** The test record variants are built in each test's setup from WP2's unit fixture; no file is added to `tests/unit/fixtures/`.
  - Src: PLAN §8.2. Accept: stage 2 unit (inspection). Test: the file list of `tests/unit/fixtures/` is equal before and after the package.
- **K15** `ledger.py` carries its own copy of the small CLI frame (envelope, refusal helper, parser) and does not move it into `mmb_common.py`.
  - Src: PLAN §8.3; API:57 to 59 (the list of what could move later). Accept: stage 2 unit (inspection). Test: `mmb_common.py` is byte-equal to its WP2 copy; `ledger.py` defines its own frame.
- **K16** With `MMB_HOME`, `HOME` and `USERPROFILE` pointed at temporary folders, no subcommand touches anything under the real home, and no path in the script or the tests names a development folder.
  - Src: A§5.3:346; AM:42; AM:69 to 76 (A22). Accept: stage 2 unit. Test: canary folders for `HOME` and the default home are unchanged after every command form; search the script and tests for a literal development path.
- **K17** The three test files pass on macOS under Python 3.9 and under the newest installed Python 3.
  - Src: BP:148 (last sentence); AM:42; PLAN step 11. Accept: macOS run. Test: run the suite on the Mac under each interpreter with `PYTHONDONTWRITEBYTECODE=1` and keep the result.
- **K18** The same three test files pass on Windows under Python 3.9 and under the newest installed Python 3, WP2's suite included.
  - Src: BP:148 (last sentence); AM:42; PLAN step 10. Accept: Windows run. Test: run the whole unit suite under `py -3.9` and `py -3.14` and keep the result.
- **K19** The built size of `ledger.py` and its tests is reported as a fact beside the planned 700 and 700 lines, which are estimates.
  - Src: BP:151; PLAN §9. Accept: stage 2 unit (inspection). Test: `wc -l` of each file appears in the checklist.

### 2.2 The CLI frame, envelope and exit codes

- **K20** The subcommand surface is exactly the catalogue of A§5.4:356: `check`, `bind`, `approval`, `change-check`, `run start`, `run heartbeat`, `run end`, `intent`, `record`, `verify`, `depart`, `ui-step`, `irreversible-yes`, `reconcile`, `estimate`, `snapshot`, `compare`, `classify`, `native-map`, `live-map`, `live-map set`, `workspaces`.
  - Src: A§5.4:356; BP:135 (the record-level list). Accept: stage 2 unit. Test: the dispatch table equals that list of 22 command forms; no other name is accepted.
- **K21** An unknown subcommand is a could-not-run error with the JSON envelope and exit 3.
  - Src: G10. Accept: stage 2 unit. Test: run `ledger.py migrate`; exit 3, `"ok": false`, an `error` object.
- **K22** The record is located the way `record.py` locates it, and exit 3 follows when no record or no `account.json` is found there.
  - Src: API:9 (the model); A§5.3:344. Accept: stage 2 unit. Test: run from a folder with no `CLIENT.md`; exit 3 naming the file. See W91.
- **K23** Every command prints one JSON object, UTF-8, LF, shaped `{"ok": <exit code is not 1>, "command": "<name>", ...}`.
  - Src: G10; API:10. Accept: stage 2 unit; Windows run. Test: parse the output of each command form; keys `ok` and `command` are present and the output has no `\r`.
- **K24** A refusal prints `"refusals": [{"file", "field", "problem", "expected"}]`, every part non-empty, `file` record-relative in POSIX spelling so the output is the same on both systems.
  - Src: G10; A§5.3:344. Accept: stage 2 unit; Windows run. Test: for each planted defect, assert four non-empty parts and a slash-separated `file`, with the path flavour simulated as Windows.
- **K25** A could-not-run prints `"error": {"file", "field", "problem", "expected"}`, every part non-empty; an error about a whole file names the field `(whole file)`, and a mutex timeout names `record.mutex`.
  - Src: G10; DECISIONS:632 (the whole-file field). Accept: stage 2 unit. Test: feed a file that is not JSON and a held mutex; assert the four parts and the two field names.
- **K26** Exit 0 means the command did its work with nothing to report.
  - Src: G10; A§5.3:344. Accept: stage 2 unit. Test: one clean call per command form exits 0.
- **K27** Exit 1 is a refusal of any kind, or `check` with a blocking finding.
  - Src: G10; A§5.3:344. Accept: stage 2 unit. Test: one refusal per refusal clause of 2.9 exits 1 and leaves the tree hash unchanged.
- **K28** Exit 2 means the command did its work or `check` ran and only warnings remain.
  - Src: G10; A§5.3:344. Accept: stage 2 unit. Test: a `check` on a record with one warning exits 2.
- **K29** Exit 3 means could not run: a missing or unreadable record or file, malformed JSON, a mutex timeout, a fence that could not run, a usage error, an unknown subcommand, an unexpected exception.
  - Src: G10; BP:134. Accept: stage 2 unit. Test: one case each; every one prints the `error` envelope.
- **K30** A usage error prints the JSON envelope and exits 3, not the parser's default exit 2.
  - Src: G10; API:11. Accept: stage 2 unit. Test: call a command with a required flag missing; exit 3 and a parsable envelope.
- **K31** Every finding and refusal names the file, the field, the problem and the expected value.
  - Src: A§5.3:344 (the exit-codes sentence). Accept: stage 2 unit. Test: the helper that runs the commands in the tests asserts four non-empty parts on every finding it sees, as WP2's does.

### 2.3 The one-writer rule and the `guard_index.lease` exception

- **K32** `ledger.py` is the only code that writes `account.json`, with the single exception of the `guard_index.lease` block that the lease primitives in `mmb_common.py` write.
  - Src: BP:135; BP:386; A§5.4:356; A§7.3:538. Accept: stage 2 unit. Test: after each command form, the changed bytes of `account.json` lie only in blocks the command may write; the lease block's bytes are identical.
- **K33** `ledger.py` is the only code that writes a strand's `solution/build.json`.
  - Src: BP:135; A§5.4:356. Accept: stage 2 unit (inspection). Test: no other script in the plugin folder opens `build.json` for writing; every `build.json` change in a test follows a `ledger.py` command.
- **K34** `ledger.py` never writes `.work/lock.json` and never writes `CLIENT.md`'s `lease` field; every lock change goes through the `mmb_common` primitives.
  - Src: BP:135; BP:386; A§5.4:354. Accept: stage 2 unit. Test: search the script for the lock path and the `lease` field; a spy on file writes sees no write to either from `ledger.py` itself.
- **K35** `ledger.py` never parses the lock itself: lease state, the fence and the release come only from `mmb_common` functions.
  - Src: BP:135; G51. Accept: stage 2 unit (inspection). Test: the script reads `.work/lock.json` nowhere; the fence and the release are calls to `lease_fence` and `lease_release`.
- **K36** Every write of `account.json` by `ledger.py` re-reads the file inside the mutex and leaves `guard_index.lease` exactly as it found it, so a lease change made between two ledger commands is never overwritten.
  - Src: BP:135; BP:386; A§5.4:356. Accept: stage 2 unit. Test: take a lease with the primitives, run `workspaces`, read the block back; the epoch, label and heartbeat are the primitives' values.
- **K37** This package's tests never write the `guard_index.lease` block or the lock directly: lease state in a test is set only by the `mmb_common` primitives and read back from them.
  - Src: BP:135 ("this package's tests never touch"). Accept: stage 2 unit (inspection). Test: search the three test files for a write to the lock path or to that block.
- **K38** The record-level subcommands `bind`, `change-check`, `native-map`, `classify`, `snapshot`, `compare`, `live-map`, `live-map set` and `workspaces` write `account.json`, write no `build.json`, and take `--strand` only to stamp who asked.
  - Src: BP:135; A§5.4:356. Accept: stage 2 unit. Test: run each with `--strand` naming a strand and assert no `build.json` changed; the stamp is the only use of the flag. See W92 for where the stamp is kept.
- **K39** Every other subcommand takes `--strand` and writes that strand's ledger only; `run end` also writes the live-map files (2.8 and 2.14) and `reconcile --classify-only` writes the holder's ledger (2.17).
  - Src: BP:135; BP:139. Accept: stage 2 unit. Test: after each strand-level command, only that strand's `build.json` (and the named exceptions) changed.
- **K40** A strand-level subcommand refuses a strand that has no `build.json` (a `non-platform` strand), without creating one.
  - Src: A§7.3:540; RM:123. Accept: stage 2 unit. Test: run `run start` for a `non-platform` strand in the fixture variant; refusal naming `solution/build.json`, no file created.

### 2.4 The record mutex and post-commit `committed` reports

- **K41** Every read and write of `account.json` runs inside `mmb_common.record_mutex`.
  - Src: BP:134; G09. Accept: stage 2 unit; Windows run. Test: a spy on `record_mutex` and on the file opens shows no open of `account.json` outside a hold.
- **K42** Every read and write of a strand's `build.json` runs inside the record mutex.
  - Src: BP:134; G09. Accept: stage 2 unit; Windows run. Test: as K41 for `build.json`.
- **K43** Every read and write of the lock runs inside the record mutex; the fence and the release, which take it themselves, are the only lock reads `ledger.py` makes.
  - Src: BP:134; G09; MC:lease_fence. Accept: stage 2 unit. Test: as K41 for the lock path.
- **K44** A command that reads a value in order to decide takes the mutex before the read and keeps it through its write, so the decision cannot go stale between them.
  - Src: G09 ("every read that feeds a decision"). Accept: stage 2 unit. Test: for `intent`, `record`, `verify`, `run end`, patch the mutex to record entry and exit; the read and the write sit inside one hold.
- **K45** A hold of the mutex by `ledger.py` followed, inside it, by a call to `lease_fence` or `lease_release` (which take it again) works in one process: the second take returns at once and the outer hold is still held on exit.
  - Src: PLAN §7.20; MC:record_mutex (re-entrant within a thread). Accept: stage 2 unit. Test: take the mutex, call the fence, assert no timeout, and assert a second process still cannot take it until the outer hold ends. See W26.
- **K46** A mutex that cannot be taken (30 seconds held, or a file system without locks) is exit 3 and a stop, never a skipped lock.
  - Src: G09; BP:134 (the stop-not-skip rule of the fence, applied to the mutex); DECISIONS:616. Accept: stage 2 unit; Windows run. Test: hold the mutex from a second process, run `intent`, assert exit 3 and no write.
- **K47** Two writers on one record, run at once, both finish with no torn file and no lost update.
  - Src: G09. Accept: stage 2 unit; Windows run. Test: run two `record` calls for different keys from two processes against one strand; both rows are present afterwards and `build.json` parses.
- **K48** When a step after a committed change fails, the command exits 3.
  - Src: BP:134; A§5.3:344. Accept: stage 2 unit. Test: force the second write of `run end` to fail after the first; exit 3.
- **K49** That exit 3 carries the error field `committed`.
  - Src: BP:134; A§5.3:344; DECISIONS:606. Accept: stage 2 unit. Test: the `error.field` of the forced failure is `committed`.
- **K50** That exit 3 also carries a top-level `committed` object saying what was written and what is still to do, so the session neither repeats the change nor loses it.
  - Src: BP:134; A§5.3:344; A§7.1:438. Accept: stage 2 unit. Test: the object names each file already written and each step not done; see W33 for its fields.
- **K51** The `committed` report is raised through `MMBError`'s `committed` keyword, as `record.py` raises it.
  - Src: BP:134 ("the way `record.py` does"); MC:MMBError. Accept: stage 2 unit (inspection). Test: the forced failure of K48 is an `MMBError` with `committed` set.

### 2.5 `bind` and `workspaces`

- **K52** `bind` writes `account.json.account` (`id`, `slug`, `name`, `kind`, `build_target`, `tier`, `bound_user_id`, `builder_role`, `products[]`) from the binding document, leaving no field at `unbound`.
  - Src: BP:135; A§8.2:751; RM:119; G15. Accept: stage 2 unit. Test: bind the template record from a binding document; every listed field holds the document's value. See W37.
- **K53** `bind` writes `account.bound_at`.
  - Src: BP:135; G15. Accept: stage 2 unit. Test: the field is set after bind and holds the form W14 settles.
- **K54** `bind` records the build target as `own-account` by default and `client-account` when the work is a build for an existing customer, with `account.kind` agreeing: `own` with `own-account`, `client` with `client-account`, `sandbox` with `none`.
  - Src: BP:135; AM:78 to 81 (A21); G15; RM:103. Accept: stage 2 unit. Test: bind the three record kinds; each pair is written; a disagreeing pair is refused.
- **K55** `bind` refuses an account listed in `local/sandbox-accounts.txt` on a client record, matching on the slug as well as the id.
  - Src: BP:135; A§5.4:356; A§8.2:751; SF 3; RM:70. Accept: stage 2 unit. Test: a settings home whose sandbox file lists the account's slug; bind on a `client` record is refused naming the line.
- **K56** `bind` refuses a sandbox record bound to any account that is not a sandbox account.
  - Src: BP:135 ("and the reverse"); A§5.4:356. Accept: stage 2 unit. Test: bind a `sandbox` record to an account absent from the sandbox file; refused.
- **K57** `bind` binds an own-account record only to the default build-target account in `local/settings.json` (`default_build_account`).
  - Src: BP:135; A§5.4:356; A§8.2:751; RM:70. Accept: stage 2 unit. Test: bind to the default passes; bind to another account is refused.
- **K58** `bind` refuses to change an account that is already bound: one account per client record, and no strand rebinds.
  - Src: SF 3 (one account per client, none may rebind); A§5.4:356. Accept: stage 2 unit. Test: bind twice with different ids; the second is refused and the first value stands. See W37.
- **K59** `bind` records no operational (never-show) workspace as a client workspace or a build target; the never-demo list is not a bind target.
  - Src: BP:135; RM:70. Accept: stage 2 unit. Test: bind with a never-show workspace in settings; `client_workspaces` stays empty and no target is written.
- **K60** The values `bind` writes are exactly the values `record.py check` compares with `CLIENT.md`: `account.id`, `slug`, `bound_user_id`, `bound_at`, `build_target` and `kind`.
  - Src: G15; BP:386. Accept: stage 2 unit. Test: after `bind`, copy those values into `CLIENT.md`'s `monday_*` fields and run `record.py check`; no binding finding. See W22 for the order of the two writes.
- **K61** Ids `bind` stores (account id, user id) are strings.
  - Src: A§5.4:356 ("ids stored as strings"); RM:119. Accept: stage 2 unit. Test: a binding document carrying a number is refused (K131) or stored as a string per W35.
- **K62** `workspaces` records a product's workspace, `{id, name, created_in}` under `core`, `crm` or `service`, in `client_workspaces` when the build creates it.
  - Src: BP:135; A§7.3:538; RM:119; AM:83. Accept: stage 2 unit. Test: record one entry per product; the block holds the three fields and no other product changes.
- **K63** `workspaces` refuses a product outside `core`, `crm` and `service`.
  - Src: RM:119. Accept: stage 2 unit. Test: product `dev` refused.
- **K64** `workspaces` adds the workspace id to `guard_index.client_workspace_ids`, the set `intent` and the hook refuse a write outside of.
  - Src: A§5.4:356; A§7.3:538; G47. Accept: stage 2 unit. Test: after `workspaces`, the id is in the list and `intent` against it passes. See W38.
- **K65** `workspaces` refuses an operational (never-show) workspace id as a client workspace.
  - Src: BP:135; A§5.4:356; RM:70. Accept: stage 2 unit. Test: a workspace id that settings list as never-show is refused with the settings line quoted.
- **K66** A later strand or a later product adds its own entry; `workspaces` never reuses or overwrites another product's entry.
  - Src: A§7.3:538; AM:83. Accept: stage 2 unit. Test: record `core`, then `crm`; the `core` entry is byte-equal afterwards. See W39 for a second workspace in one product.
- **K67** `workspaces` and every other writer keep each id in `guard_index.build_targets_by_strand` inside `guard_index.client_workspace_ids`: the client's workspaces are the ceiling.
  - Src: G47; BP:146. Accept: stage 2 unit. Test: try to write a target outside the client set; refused, and `record.py check` on the result is clean.
- **K68** Workspace and folder ids that `workspaces` stores are strings.
  - Src: A§5.4:356; RM:119. Accept: stage 2 unit. Test: as K61.

### 2.6 `approval` and the approval modes (A25, A28)

- **K69** `approval` appends an `approvals[]` entry holding `version`, `qualified_version`, `revision`, `frozen_file`, `sha256`, `approved_at`, `approved_words`, `approved_in_session`, `approval_mode`, `element_count`, `irreversible_listed`, `automations_listed`, `workflows_listed`, `agents_listed`, `sequences_listed`, `rests_on` and `live_objects_touched`.
  - Src: A§7.3:551 to 556; RM:123 (shorter list). Accept: stage 2 unit. Test: record an approval; the entry has all seventeen fields in that order. See W06, W42.
- **K70** `approval` refuses when `sha256` is not the sha256 of the frozen file it names, as the file is on disk.
  - Src: A§5.4:356 ("frozen sha matches the approval"); BP:135 (WP2 `freeze` returns the sha). Accept: stage 2 unit. Test: change one byte of the frozen copy; refused naming both hashes. See W42 on how the sha is computed.
- **K71** `approval` refuses an element key in its lists that is not in the frozen revision's element-key table, the table pinned in `record-map.md` as part of `blueprint/1`.
  - Src: PLAN §5 Q1 (a); DECISIONS:630. Accept: stage 2 unit. Test: an approval listing `B9` against a revision that lists only `B1` is refused. See W42.
- **K72** `approval_mode` is `own-account-poc` when the card's one yes covered the lists and the irreversible steps of a proof of concept in the user's own account, and `per-list` otherwise.
  - Src: A§7.3:582; AM:18; A§8.6:796. Accept: stage 2 unit. Test: record the same revision on an own-account record and on a client-account record; the modes differ as stated. See W09, W44.
- **K73** On `own-account-poc` the card's one yes is a valid `approval_ref` for every list, irreversible and publication row of that revision, except a list whose rows notify a real person.
  - Src: BP:137; AM:18; A§9.5:904. Accept: stage 2 unit. Test: on the own-account record, `intent` for a list row, an irreversible row and a publication row with `approval_ref` equal to the card's passes.
- **K74** In a client's account, a list row whose `approval_ref` is only the card's yes is refused.
  - Src: BP:137; BP:148; A§9.5:904. Accept: stage 2 unit. Test: on the client-account record, `intent` for an automation row with only the card's yes is refused.
- **K75** In a client's account, an irreversible row without its own yes and its execution confirmation is refused.
  - Src: BP:148; A§8.6:800; A§9.4:898. Accept: stage 2 unit. Test: `intent` for an archive row with no recorded yes is refused; the same row after `irreversible-yes` passes.
- **K76** A row on a list that notifies a real person is refused on the card's yes alone, in either account.
  - Src: BP:137; BP:148; A§9.5:910. Accept: stage 2 unit. Test: on the own-account record, a row whose `notifies` names a person other than the bound user is refused. See W45.
- **K77** On `own-account-poc` no execution-time confirmation is required for list, irreversible or publication rows.
  - Src: BP:148; A§8.6:800 and :801; AM:18. Accept: stage 2 unit. Test: the whole own-account revision of K81 passes with no `irreversible-yes` call and no grouped reply recorded.
- **K78** Every `approval_ref` names its approval mode as `record-map.md` pins it, so a ref resolves to an `approvals[]` entry and through it to a mode.
  - Src: BP:137. Accept: stage 2 unit. Test: resolve each `approval_ref` in the fixture variants; each has one entry and one mode. See W09, W43.
- **K79** Under `own-account-poc`, each `irreversible_yes` row carries `mode: card` and the card's `approval_ref` instead of a yes taken at execution.
  - Src: A§5.4:356; A§7.3:575 and :582; AM:18. Accept: stage 2 unit. Test: `irreversible-yes` on the own-account record writes `mode: card` and the ref. See W09 for the mode of a per-list row.
- **K80** The approval entry an `approval_ref` points at is read from disk at the time of the write, not carried in memory.
  - Src: A§8.6:800. Accept: stage 2 unit. Test: change the entry between two calls; the second call sees the change.
- **K81** A test records the same revision twice, once on an own-account record and once on a client-account record, and asserts K73 to K77 on the pair.
  - Src: BP:148. Accept: stage 2 unit; Windows run; macOS run. Test: the one test exists and passes on both systems.
- **K82** An approval's `rests_on` counts the clearance, the purpose, the assumptions, the assumed terms and the forks built on their leaning.
  - Src: A§7.3:555; A§7.3:582; AM:46 to 58. Accept: stage 2 unit. Test: the five keys are present; the counts are integers.
- **K83** `irreversible_listed`, `automations_listed`, `workflows_listed`, `agents_listed` and `sequences_listed` hold element keys, and the keys of a publication or activation (`WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT`) belong in `irreversible_listed` as their own steps.
  - Src: A§7.3:553 and :554; A§7.3:582; A§9.4:891 to 894. Accept: stage 2 unit. Test: an approval with `VB1.PUB` listed under `irreversible_listed` is accepted; the same key under `automations_listed` is refused. See W10, W11.
- **K84** `live_objects_touched` holds `{key, constraint}` pairs whose keys are qualified live-map keys and whose constraint is one of the three values.
  - Src: A§7.3:556; A§7.8:710. Accept: stage 2 unit. Test: a pair with constraint `maybe` is refused.
- **K85** An object built on a fork's leaning or an assumed term lists those items in `assumption_refs`, drawn from the frozen revision, so that it can be named while any of them is not yet confirmed or accepted.
  - Src: BP:137; A§7.3:582; AM:46 to 58 (A25). Accept: stage 2 unit. Test: a row with `assumption_refs` set round-trips through `record`; the field is a list of strings. See W46.
- **K86** Every seeded item row carries `sample_data: true`, so `verify`, the audit and the build notes can tell a sample value from a fact.
  - Src: BP:137; AM:19 (A28); A§7.3:582. Accept: stage 2 unit. Test: a seed row recorded without the flag is refused or recorded `true` per W11; a non-sample row carries `false`.
- **K87** `assumption_refs` and `sample_data` survive `record`, `verify` and `run end` unchanged.
  - Src: BP:148. Accept: stage 2 unit; Windows run; macOS run. Test: set both on a row, run the three commands, and compare the two fields byte for byte.

### 2.7 `change-check`

- **K88** `change-check` writes `account.json.change_check` with `at`, `for_strand`, `ring`, `versions_seen`, `release_notes_since`, `roster_diff {added, removed, renamed}`, `schema_diff`, `result` and `approved_by_user`.
  - Src: A§7.3:500 to 502; RM:119; AM:188 to 195 (A3); A§8.6:794. Accept: stage 2 unit. Test: run it with a change check handed in as a file (W49); the block holds the nine fields. See W08 for `result` against `verdict`.
- **K89** `change_check.at` is written in UTC as `YYYY-MM-DDTHH:MM:SSZ`.
  - Src: A§7.3:500; G40; A§9.10:958 (the hook reads "dated today"). Accept: stage 2 unit. Test: with the clock patched, the stamp parses with the UTC format.
- **K90** `change_check.for_strand` is the strand that asked.
  - Src: A§7.3:500; A§8.6:794; BP:135. Accept: stage 2 unit. Test: `--strand 002` writes `"002"`.
- **K91** `release_notes_since` is `<date> (read)` or `not-read`, and nothing else.
  - Src: RM:119; A§8.6:794. Accept: stage 2 unit. Test: any other value is refused.
- **K92** `roster_diff` has exactly the three lists `added`, `removed` and `renamed`.
  - Src: RM:119; A§7.3:501. Accept: stage 2 unit. Test: a missing or extra key is refused.
- **K93** `approved_by_user` is `null` or a log reference, and `change-check` sets it only when a log reference is given.
  - Src: RM:119; A§8.6:794. Accept: stage 2 unit. Test: a call with no reference leaves it `null`.
- **K94** The record says whether a change touches this build: a change that does is recorded so that it stops the build, and an unrelated change is recorded and the build continues.
  - Src: A§8.6:794; AM:195. Accept: stage 2 unit. Test: two inputs, one touching and one not; the `result` values differ. See W49.
- **K95** `change-check` changes no block of `account.json` other than `change_check`.
  - Src: BP:135; A§7.3:488. Accept: stage 2 unit. Test: hash every other block before and after.

### 2.8 The fence and the run: `run start`, `run heartbeat`, `run end`, the one question

- **K96** `run start` refreshes the lease with its run id, through `mmb_common.lease_refresh`, before any fenced write.
  - Src: BP:135; G50; G51 amended (DECISIONS:604); MC:lease_refresh. Accept: stage 2 unit. Test: after `run start`, the lock's `run_id` is the new run's and the heartbeat moved.
- **K97** `run start` stamps the lease epoch into the strand's `lease_epoch_at_run`.
  - Src: BP:135; A§7.3:549; A§8.6:792. Accept: stage 2 unit. Test: the field equals the epoch presented.
- **K98** `run start` appends a `runs[]` entry with `id`, `version`, `kind`, `session_label`, `lease_epoch`, `another_build_running`, `started_at`, `heartbeat_at`, `ended_at` null, `state` `running`, `calls_estimated`, `calls_used` null and `account_checks`.
  - Src: A§7.3:560 to 564; RM:123. Accept: stage 2 unit. Test: the entry has the listed keys in that order. See W30 for the id and the kind.
- **K99** `run start` records the answer to the one question, "is another build running anywhere?", in the run entry.
  - Src: BP:135; A§8.6:792; A§9.8:938 (D10). Accept: stage 2 unit. Test: the answer text and its time are in `another_build_running`. See W30.
- **K100** A yes to the one question stops the run: the answer is recorded and no run goes on.
  - Src: A§8.6:792; A§9.8:938. Accept: stage 2 unit. Test: `run start` with a yes records it and the run is not left `running`. See W30.
- **K101** `run start` is refused when the lock is not held under the presented epoch and label, and the lock is left as it was.
  - Src: G50; MC:lease_refresh. Accept: stage 2 unit. Test: a wrong label and a wrong epoch are each refused.
- **K102** A run id enters the lease only while the lock's `run_id` is `null`, and never a run id an earlier lease carried.
  - Src: G50 amended (DECISIONS:604); MC:lease_refresh. Accept: stage 2 unit. Test: a second `run start` under the same lease is refused, and so is an old run's id under a new lease.
- **K103** `run start` records an account check, `{at, before: "run start", result}`, in `account_checks`.
  - Src: A§7.3:564; A§8.6:798. Accept: stage 2 unit. Test: the entry is present with the three keys. See W24.
- **K104** Every account-affecting write calls `mmb_common.lease_fence` first.
  - Src: BP:135; A§5.4:356; A§9.8:944; G51 amended. Accept: stage 2 unit; stage 4 headless H35. Test: spy on `lease_fence` while each command W28 names runs; the call precedes the first write.
- **K105** The fence refuses a write that carries an old `--lease-epoch`.
  - Src: BP:135; BP:504 (H35). Accept: stage 2 unit; stage 4 headless H35. Test: break and retake the lease with the primitives; a write with the old epoch is refused.
- **K106** The fence refuses a write that carries the new epoch with the old `--session-label`.
  - Src: BP:135; BP:504; A§9.8:934. Accept: stage 2 unit; stage 4 headless H35. Test: as K105 with the new epoch and the old label.
- **K107** The fence refuses a write that carries the new epoch and label with the old run id.
  - Src: BP:135; BP:504; A§9.8:934. Accept: stage 2 unit; stage 4 headless H35. Test: as K105 with the new epoch, new label and old run id.
- **K108** A fence refusal exits 1, changes no file, and names which of the three parts failed.
  - Src: G51; G10; MC:lease_fence (the reason text). Accept: stage 2 unit. Test: the refusal's `problem` names epoch, label or run, and the tree hash is unchanged.
- **K109** A write made before `run start`, while the lock carries no run id, is refused.
  - Src: G51 amended; MC:lease_fence. Accept: stage 2 unit. Test: take a lease, run `intent` without `run start`; refused with the "no run has started" reason.
- **K110** A passing fence moves the heartbeat, so the write needs no separate refresh.
  - Src: BP:135; G51 amended. Accept: stage 2 unit. Test: the lock's `heartbeat_at` after a fenced write is later than before.
- **K111** A fence that cannot run (exit 3, a mutex timeout or a malformed lock included) is a stop, never a skip: the write is not made.
  - Src: BP:135; G51 amended. Accept: stage 2 unit. Test: hold the mutex or tear the lock; the command exits 3 and writes nothing.
- **K112** A fenced write that lacks `--lease-epoch`, `--session-label` or the run, is refused, and the missing value is never filled from the lock.
  - Src: A§9.8:934 (the carry rule); BP:135. Accept: stage 2 unit. Test: omit each of the three in turn; each omission is refused. See W29.
- **K113** `intent` presents the epoch, label and run id to the fence before any monday call is made, so a write from a session that is not the holder fails at the ledger.
  - Src: A§9.10:958; A§5.4:356. Accept: stage 2 unit. Test: a session with another strand's label is refused at `intent`.
- **K114** `run heartbeat` moves the heartbeat through the refresh primitive and appends no lock history entry.
  - Src: A§5.4:356; BP:68; MC:lease_refresh. Accept: stage 2 unit. Test: the history length is unchanged and `heartbeat_at` moves. See W31.
- **K115** `run end` releases the lease through `mmb_common.lease_release`, a state change that keeps the file and the history.
  - Src: BP:135; A§9.8:942; MC:lease_release. Accept: stage 2 unit. Test: after `run end` the lock is `released` and its history gained one `released` entry.
- **K116** `run end` records `calls_used`, `ended_at` and the run's end state in the run entry.
  - Src: A§8.6:802; RM:123. Accept: stage 2 unit. Test: the three fields are set. See W32.
- **K117** `run end` writes the strand's verified objects into `live/live-map.md` and `account.json.live_objects` in one step.
  - Src: BP:135; A§7.8:718; A§8.6:802. Accept: stage 2 unit. Test: after `run end`, every verified object has a row in each file and the two agree row for row.
- **K118** The rows `run end` creates carry the interim constraint `change-with-own-yes` and the source `pending strand close`.
  - Src: BP:135; A§7.8:718; RM:134. Accept: stage 2 unit. Test: read the new rows.
- **K119** A row is created only for an object a read-back verified.
  - Src: BP:135; A§7.8:706. Accept: stage 2 unit. Test: objects in `planned`, `attempting`, `written`, `mismatch` and `departed` get no row; one `verified` with result `match` does. See W60.
- **K120** `run end` releases the lease in the same step in which it writes the live map, with a `committed` report if a later write fails after an earlier one.
  - Src: BP:135; BP:134; A§8.6:802. Accept: stage 2 unit. Test: inject a failure after each of the writes of `run end` in turn; each failure is exit 3 with `committed` naming what stands. See W25.
- **K121** A clean stop before any write (a yes to the one question, a failed change check, a preflight finding) releases the lease at once.
  - Src: A§9.8:942; A§8.6:795. Accept: stage 2 unit. Test: after the stop, the lock is `released`. See W30.

### 2.9 The refusals of BP:135, one clause each

- **K122** A status transition the chain does not allow is refused, naming the row, its status and the status asked for.
  - Src: BP:135; A§7.3:582; RM:123. Accept: stage 2 unit; stage 4 headless H35. Test: for each pair of the six statuses and `departed` and `removed`, the allowed ones (K183) pass and every other is refused with the tree unchanged. See W13.
- **K123** A missing `approval_ref` on an irreversible row is refused.
  - Src: BP:135; A§7.3:582; RM:123. Accept: stage 2 unit. Test: `intent` for an archive row with no `approval_ref`; refused.
- **K124** A missing `approval_ref` on a list-approved row (an automation, workflow, agent or sequence) is refused.
  - Src: BP:135; A§5.4:356; A§9.5:904; RM:123 (automation only). Accept: stage 2 unit. Test: one `intent` per list kind with no ref; each refused. See W07.
- **K125** A missing `approval_ref` on a publication or activation row (`WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT`) is refused.
  - Src: BP:135; BP:137; A§9.4:891 to 894. Accept: stage 2 unit. Test: one `intent` per publication key with no ref; each refused. See W07.
- **K126** A missing `approval_ref` on a removed row is refused.
  - Src: BP:135; A§5.4:356; RM:123. Accept: stage 2 unit. Test: a transition to `removed` with no ref is refused. See W56.
- **K127** A `prior_state` on any row whose origin is not `pre-existing-modified` or `other-strand-modified` is refused.
  - Src: BP:135; A§5.4:356; A§7.3:582. Accept: stage 2 unit. Test: a `created` row with `prior_state` set is refused.
- **K128** A row whose origin is `pre-existing-modified` or `other-strand-modified` and which has no `prior_state` is refused.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: each of the two origins without `prior_state`; refused.
- **K129** An `other-strand-modified` row whose target the live map marks `do-not-change` is refused.
  - Src: BP:135; A§7.3:582; A§7.8:712; BP:508 (H39). Accept: stage 2 unit; stage 4 headless H39. Test: set a row's constraint to `do-not-change` in the fixture variant; `intent` against it is refused quoting the constraint and its source; against `change-with-own-yes` it passes.
- **K130** An `other-strand-modified` row also requires `source_strand` and an `approval_ref`.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: omit each; each omission refused.
- **K131** An id stored as a number is refused, wherever an id is written.
  - Src: BP:135; A§5.4:356; RM:119. Accept: stage 2 unit. Test: a JSON input whose `id` is the number `123` is refused; the string `"123"` passes. See W35.
- **K132** A parent key that does not resolve is refused.
  - Src: BP:135; A§5.4:356. Accept: stage 2 unit. Test: a column row whose `parent_key` names a board absent from `objects` is refused. See W58.
- **K133** A stale `--expect-sha` is refused, and nothing is written.
  - Src: BP:135; A§5.3:345; G60. Accept: stage 2 unit. Test: read the sha, change `build.json` by another call, write with the old sha; refused naming both. See W34.
- **K134** A write whose `--lease-epoch` differs from `.work/lock.json` is refused.
  - Src: BP:135; A§9.8:934. Accept: stage 2 unit; stage 4 headless H35. Test: as K105.
- **K135** A write whose `--session-label` differs from the lock's is refused.
  - Src: BP:135; A§9.8:934. Accept: stage 2 unit; stage 4 headless H35. Test: as K106.
- **K136** A write whose run is not the lock's `run_id` is refused.
  - Src: BP:135; A§9.8:934. Accept: stage 2 unit; stage 4 headless H35. Test: as K107. See W29.

### 2.10 The scope check (A21)

- **K137** `intent` refuses any write whose target workspace is outside the strand's entry in `build_targets_by_strand`.
  - Src: BP:136; A§5.4:356; A§7.3:538. Accept: stage 2 unit. Test: a write targeting a client workspace that is not in strand 001's entry, from strand 001, is refused naming the strand and the id.
- **K138** A strand's entry in `build_targets_by_strand` holds only workspaces created for this client, or recorded as built earlier for the same client.
  - Src: BP:136; AM:83. Accept: stage 2 unit. Test: no command writes an id into an entry unless it is in `client_workspace_ids`. See W38.
- **K139** For an agent's trigger target, `intent` refuses any reference outside the client's workspaces.
  - Src: BP:136; A§5.4:356; A§9.10:958. Accept: stage 2 unit. Test: a trigger naming a board of a sibling client's workspace is refused. See W41.
- **K140** For an agent's knowledge grant, `intent` refuses any reference outside the client's workspaces.
  - Src: BP:136; BP:527 (H58). Accept: stage 2 unit; stage 4 headless H58. Test: a grant to a board outside the client's workspaces is refused.
- **K141** For a Vibe app's board binding, `intent` refuses any board outside the client's workspaces.
  - Src: BP:136; AM:83. Accept: stage 2 unit. Test: a binding to an outside board is refused.
- **K142** For a webhook's board, `intent` refuses any board outside the client's workspaces.
  - Src: BP:136. Accept: stage 2 unit. Test: as K141 for a webhook.
- **K143** For a sequence's board, `intent` refuses any board outside the client's workspaces.
  - Src: BP:136. Accept: stage 2 unit. Test: as K141 for a sequence.
- **K144** A workspace creation is recorded as an irreversible row with its product and the client it is for.
  - Src: BP:136; A§9.4:890; SF 4 (IR-14). Accept: stage 2 unit. Test: the row has `irreversible: true`, the product and the client slug. See W11 on where the product and client are kept.
- **K145** A second workspace in the same product for the same client is refused unless the record says the direction changed.
  - Src: BP:136; AM:83 (A21). Accept: stage 2 unit. Test: a second `crm` workspace is refused on a record with no direction-change field. See W39, which settles nothing about the field.
- **K146** A unit test proves the refusal of a planted write into a sibling client's workspace.
  - Src: BP:136. Accept: stage 2 unit. Test: the test exists; the planted write is refused.
- **K147** A unit test proves the refusal of a planted write into an operational (never-show) workspace.
  - Src: BP:136; BP:527. Accept: stage 2 unit. Test: the test exists; the workspace is one that settings list as never-show.
- **K148** A unit test proves the pass of the same write into the client's own workspace.
  - Src: BP:136; BP:527. Accept: stage 2 unit; stage 4 headless H58. Test: the test exists; the write is accepted.
- **K149** A board the record cannot place in any workspace is treated as outside the client's workspaces, and the write is refused.
  - Src: PLAN §8.9; PLAN §7.16. Accept: stage 2 unit. Test: `intent` against a board id that no row and no `native_board_index` entry places; refused. See W40.
- **K150** A scope refusal quotes the rule it applies (A21) and names the target and the strand.
  - Src: BP:527 (H58); AM:83. Accept: stage 2 unit; stage 4 headless H58. Test: the refusal's `expected` holds the A21 wording and the workspace ids.

### 2.11 Rows and classes for every element kind (A18; all kinds in stage 2, PLAN Q2 (a))

- **K151** `objects[].type` accepts exactly `workspace`, `folder`, `board`, `group`, `column`, `view`, `form`, `subitems`, `doc`, `dashboard`, `widget`, `automation`, `portfolio`, `project`, `workflow`, `agent`, `ai_column`, `vibe_app`, `sequence` and `webhook`.
  - Src: BP:137; A§7.3:582. Accept: stage 2 unit. Test: one row of each kind is accepted; `item` and any other word is refused. See W11.
- **K152** An element key has the shape of its kind: `W1`, `F1`, `B1`, `B1.G2`, `B1.C3`, `B1.V1`, `B1.FM1`, `B1.SUB`, `D1`, `DB1`, `DB1.W2`, `A1`, `PF1`, `PJ1`, `WF1`, `AG1`, `B1.AI1`, `VB1`, `SQ1`, `WH1`, with `WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT` for a publication or activation and `U1` for a UI step; keys are bare inside a strand's ledger and qualified (`001:B1`) anywhere else.
  - Src: A§7.3:582; RM:77. Accept: stage 2 unit. Test: a key of the wrong shape for its type is refused; a qualified key in a strand's own ledger is refused.
- **K153** Every row is checked for its type's fields and value types, the AI kinds included.
  - Src: A§5.4:356; BP:137. Accept: stage 2 unit. Test: one malformed row per kind (a missing `name`, a list where a string belongs); each refused with the field named.
- **K154** `intent` derives the approval class of every row from its kind, origin and operation, and decides from the class whether an `approval_ref` is required and whether an own yes is required.
  - Src: BP:137; BP:135; SF 4 and 5; A§9.4:877 to 896. Accept: stage 2 unit. Test: a table-driven test over the twenty kinds and the A§9.4 operations. See W10 for where the class table is pinned.
- **K155** A workspace row and a folder row are irreversible and need an `approval_ref`.
  - Src: A§9.4:890; SF 4 (IR-14); RM:123. Accept: stage 2 unit. Test: `intent` for each with no ref is refused.
- **K156** A row for an archive of a board, group or item, for the first subitem on a classic board (with its companion id), for a form question created through the questions editor, or for a multi-level template board, is irreversible and needs an `approval_ref`.
  - Src: A§9.4:880 to 884; SF 4 (IR-02 to IR-06). Accept: stage 2 unit. Test: one `intent` per operation with no ref; each refused; the subitem row records `companions.subitems_board_id` once known.
- **K157** A row that changes labels or columns that dependants use, or adds a column to a pre-existing board or to a board another strand built, is irreversible, needs `prior_state` and an `approval_ref`, and is refused when the live map marks the board `do-not-change`.
  - Src: A§9.4:888 and :889; SF 4 (IR-12, IR-13); A§7.8:712. Accept: stage 2 unit. Test: three cases against `free`, `change-with-own-yes` and `do-not-change` targets.
- **K158** An automation row is irreversible and a list-approved row, needs an `approval_ref`, and is built last in round one.
  - Src: A§9.4:879; A§9.5:904; RM:123; A§8.6:797. Accept: stage 2 unit. Test: the row needs the ref; the approval entry lists its key under `automations_listed`.
- **K159** A second automation row is refused for an automation key while the first is `written`, `mismatch` or `verified` and live.
  - Src: A§9.5:910 ("never create a second one while the first is live"); SF 5. Accept: stage 2 unit. Test: `intent` for the key again after `record`; refused.
- **K160** A workflow row is a list-approved row; its publication, `WF1.PUB`, is a row of its own with its own `approval_ref` that names the activation state decided before publishing.
  - Src: BP:137; A§9.4:891; A§9.5:904; AI:61 and :66. Accept: stage 2 unit. Test: the publication row needs its ref; its `what` names `inactive` or `active`. See W09, W11.
- **K161** An agent row is a list-approved row, is created inactive, and carries `prompt_ref`.
  - Src: A§9.4:892; A§7.3:571; AI:14 and :26; BP:137. Accept: stage 2 unit. Test: an agent row whose first recorded `state` is `active` is refused.
- **K162** An agent activation, `AG1.ACT`, is a row of its own with its own `approval_ref`, allowed only after the agent's read-back has matched.
  - Src: A§9.4:892; A§8.6:797. Accept: stage 2 unit. Test: `intent` for `AG1.ACT` while `AG1` is `written` is refused; after `verify` match, it passes with a ref.
- **K163** An AI column row is approved as a row of the same card, with its prompt text and bound board, and carries a read-back of `not-checkable` until its kind has been probed.
  - Src: A§9.5:904; A§10.4:1028; A§8.6:797. Accept: stage 2 unit. Test: `verify` on an `ai_column` row with result `match` is refused (see K198); `not-checkable` is accepted. See W57.
- **K164** A Vibe app row is created asynchronously and carries its code version and `is_published` at verify.
  - Src: BP:137; A§7.3:582; A§11.1:1056; AI:37 to 45. Accept: stage 2 unit. Test: the row is accepted with `id` null while `attempting`; `verify` stores both values.
- **K165** A Vibe publication, `VB1.PUB`, is a row of its own with its own `approval_ref`, and is allowed only after the delivered app has been diffed against the request.
  - Src: BP:137; A§9.4:893; AM:116 (A17). Accept: stage 2 unit. Test: `intent` for `VB1.PUB` while `VB1` is not `verified` is refused; it needs its own ref.
- **K166** A sequence row is a list-approved row whose approval shows every recipient, and its activation, `SQ1.ACT`, is a row of its own with its own yes.
  - Src: A§9.4:894; A§9.5:904. Accept: stage 2 unit. Test: the row needs `notifies`; `SQ1.ACT` needs its ref.
- **K167** A webhook row is accepted only when the frozen revision lists its endpoint, and needs its own yes.
  - Src: A§9.4:895; AM:105 to 110 (A18). Accept: stage 2 unit. Test: a webhook row absent from the approval's element list is refused.
- **K168** A dashboard row records the board ids and widget ids sent at creation, because nothing reads them back.
  - Src: G-90; G-11; A§11.1:1059. Accept: stage 2 unit. Test: the row holds both lists. See W15 for the field.
- **K169** A widget row keeps the id from its create response and has its `verify.result` set to `not-checkable`.
  - Src: A§7.3:582; G-11; G-89; A§10.4:1028. Accept: stage 2 unit. Test: a widget row without an id is refused; `verify match` on a widget is refused.
- **K170** A portfolio or project row is created asynchronously: it is accepted with no id while `attempting`, and its companion ids (tasks board, overview, planner, folder) are recorded before anything is connected.
  - Src: BP:137; A§11.1:1056 and :1057; A§11.3:1074; G-71; G-72. Accept: stage 2 unit. Test: `intent` for the connect is refused while the companions are not recorded. See W15.
- **K171** Connecting a project to a portfolio and converting a board to a project are irreversible rows with their own yes.
  - Src: A§9.4:885 and :886; SF 4 (IR-07, IR-08); G-77; G-80. Accept: stage 2 unit. Test: each `intent` with no ref refused.
- **K172** A row of an asynchronous kind (Vibe app, portfolio, project) is found by a poll with a stated ceiling before it is recorded as written, and a row that is not found by the ceiling stays `attempting`.
  - Src: BP:137; A§8.6:798; G-71; AI:37. Accept: stage 2 unit. Test: `record` with no id leaves the row `attempting`. See W54 for the ceiling per kind.
- **K173** `intent` refuses any delete of any object: v1 sends no delete in any account.
  - Src: A§9.4:896 and :900; AM:106 (A18). Accept: stage 2 unit. Test: an `intent` whose operation is a delete is refused. See W50 for the operation field.
- **K174** For an agent, `version_id_at_build` records the `version_id` read after the plan write.
  - Src: BP:137; A§7.3:571 and :582; AI:21 and :27. Accept: stage 2 unit. Test: after `verify`, the row's field equals the value in the read handed in. See W52.
- **K175** An agent row's `prompt_ref` names the frozen revision and the element key (`v0.2r2#AG1`) where the frozen prompt text sits.
  - Src: A§7.3:571; PLAN §5 Q1 (a). Accept: stage 2 unit. Test: the form is checked by K243; the place is pinned in `blueprint/1`. See W42.
- **K176** Every row's `blueprint_ref` names its frozen revision and element key in the ledger form `vNrM#KEY`.
  - Src: A§7.3:573; RM:77; DECISIONS:630. Accept: stage 2 unit. Test: `v0.1r1#B1` is accepted; the key half is looked up by `check` (K243).
- **K177** An account-level object (a row that no workspace holds) carries `workspace_scope`, the client workspaces it may read and write; every other row carries `workspace`, which must be one of the client's.
  - Src: A§7.3:582; AM:83. Accept: stage 2 unit. Test: a board row with `workspace_scope` and no `workspace` is refused; an agent row with `workspace_scope` passes. See W11.
- **K178** A row's `origin` is `created`, `pre-existing-modified`, `pre-existing-referenced` or `other-strand-modified`, and nothing else.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: any other word refused.
- **K179** A `parent_key` is `null` for a workspace and for an account-level row, and otherwise names a row of the same ledger whose id equals the row's `parent_id`.
  - Src: A§7.3:566; A§8.6:798 (a create whose parent is not a recorded id). Accept: stage 2 unit. Test: a mismatched `parent_id` is refused; a parent with no id yet is refused for a create. See W58.
- **K180** `creator_user_id`, `owner_user_ids` and `notifies` hold strings and lists of strings.
  - Src: A§7.3:572; RM:123. Accept: stage 2 unit. Test: a number inside any of the three is refused.
- **K181** `companions` holds only `subitems_board_id`, `doc_container_board_id`, `form_board_id`, `overview_board_id` and `planner_board_id`.
  - Src: RM:123; A§11.3:1074. Accept: stage 2 unit. Test: a `folder_id` or `tasks_board_id` inside `companions` is accepted or refused as W15 settles; the five named keys pass.
- **K182** A call that timed out counts as possibly applied: its row stays `attempting`, and an id read out of an error payload may be recorded.
  - Src: A§8.6:798; SF 9. Accept: stage 2 unit. Test: `record` with `--timed-out` (flag per W50) leaves `attempting`; recording an id from an error is accepted.
- **K183** The statuses are `planned`, `attempting`, `written`, `verified` and `mismatch`, then `departed` and `removed`, and the allowed moves are `planned` to `attempting` to `written` to `verified` or `mismatch`, and any status to `departed` or `removed`.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: the allowed pairs pass; this is the positive half of K122. See W13 for what the chain leaves out.
- **K184** `intent` sets the row to `attempting` with `attempt {run_id, started_at, intent_digest}`.
  - Src: A§7.3:568; A§8.6:798. Accept: stage 2 unit. Test: after `intent`, the three fields are present. See W47.
- **K185** `record` stores the id returned by the call and moves the row to `written`.
  - Src: A§8.6:798; A§7.3:582. Accept: stage 2 unit. Test: after `record`, `id` is a string and `status` is `written`. See W50.

### 2.12 `verify`, per kind

- **K186** `verify` records `verify {read, at, result, digest, note}` on the row.
  - Src: A§7.3:569 and :570; RM:123. Accept: stage 2 unit. Test: after `verify`, the block holds the five keys. See W51.
- **K187** `verify.result` is `match`, `mismatch`, `not-checkable` or `needs-user`, and nothing else.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: any other word refused.
- **K188** A `match` moves the row from `written` to `verified`, and a `mismatch` moves it to `mismatch`.
  - Src: A§7.3:582; A§8.6:798. Accept: stage 2 unit. Test: both moves. See W13 for `not-checkable` and `needs-user`.
- **K189** `verify` refuses an empty `read`: a result is never recorded without the read that produced it, and an expert's or generator's success message is never recorded as a verified fact.
  - Src: A§8.6:799; AI:57 and :67. Accept: stage 2 unit. Test: `verify` with no read is refused.
- **K190** A `not-checkable` or `needs-user` result is recorded with a note saying who checks it and how, and is never reported as a match.
  - Src: A§8.7:827; A§10.4:1028; RB:29. Accept: stage 2 unit. Test: the note is required for both; the output does not say `match`.
- **K191** `verify` refuses to mark an agent verified while its plan read differs from the frozen prompt text.
  - Src: BP:137. Accept: stage 2 unit. Test: a read whose plan differs by one character is refused; the equal plan passes. See W52.
- **K192** An agent's read names its plan, state, `version_id`, trigger list and knowledge list, and expects the two default triggers the platform adds.
  - Src: A§7.3:569; AI:19; A§9.4:892. Accept: stage 2 unit. Test: the `read` of an agent row without the five parts is refused; the two default triggers are not reported as extras.
- **K193** An agent's skill attachments and a trigger's configured board are recorded `not-checkable` and left to the by-eye list.
  - Src: AI:20 and :30; A§10.4:1028. Accept: stage 2 unit. Test: a verify that claims `match` for skills is refused.
- **K194** `verify` refuses to mark a Vibe app verified while the delivered app differs from the request, unless the user's yes to the difference is recorded.
  - Src: BP:137; AI:48; AM:116. Accept: stage 2 unit. Test: a difference with no yes refused; the same with the yes passes. See W53.
- **K195** A Vibe app is verified only when its status is `READY`.
  - Src: A§8.6:797; AI:35 and :40. Accept: stage 2 unit. Test: a read with status `GENERATING` is refused.
- **K196** A Vibe app's verify records its status, `is_published` and its code version.
  - Src: A§7.3:582; A§10.4:1028; AI:45. Accept: stage 2 unit. Test: the three values are in the row.
- **K197** A workflow's verify rests on the `objects` read of its state and on its draft validation, and a live trigger binding, which no read proves, is recorded `needs-user` with the sandbox trigger test named.
  - Src: A§10.4:1028; AI:58 and :68. Accept: stage 2 unit. Test: a workflow row cannot be `match` on the binding.
- **K198** An AI column, a sequence and a webhook are recorded `not-checkable` until their kind has been probed, and `match` is refused for them.
  - Src: A§10.4:1028; A§8.6:797; RB:53. Accept: stage 2 unit. Test: `verify match` on each of the three kinds refused; `not-checkable` accepted. See W57.
- **K199** A board-level permission is verified through the board's `permissions` field, and permissions below board level are recorded `not-checkable`.
  - Src: G-108; RB:28 and :29; A§10.4:1028. Accept: stage 2 unit. Test: a column-level permission with `match` refused.
- **K200** A portfolio's project is recorded connected only when both halves hold, the tasks board in the portfolio's link settings and one portfolio row linking items of that board; one half alone is recorded as a partial link for review.
  - Src: A§11.3:1076; NO 7.3; G-78. Accept: stage 2 unit (synthetic reads); capture (A11-1). Test: a verify handed both halves passes; one half is `needs-user` with the words "partial link". Met against synthetic reads; confirmed at capture (A11-1).
- **K201** A `match` records `verify.digest`, and the row's live-map `digest` and `last_verified` come from that verified read.
  - Src: A§7.3:530 and :570; A§7.8:704 and :716 (a protected row must return with its recorded digest). Accept: stage 2 unit. Test: the digest is present after `match`, and `run end` writes the same digest into `live_objects`. See W73 for how a digest is made.

### 2.13 `depart`, `ui-step` and `irreversible-yes`

- **K202** `depart` appends a `departures[]` entry holding `key`, `version`, `what`, `error_code`, `attempts` and `decision`.
  - Src: A§7.3:576; RM:123. Accept: stage 2 unit. Test: the entry has the six keys. See W55.
- **K203** `depart` moves the row to `departed`.
  - Src: A§7.3:582; A§8.6:799. Accept: stage 2 unit. Test: the row's status after `depart`.
- **K204** A departure's `decision` is recorded as the user chose it: a UI step, a blueprint revision or a later retry.
  - Src: A§8.6:799. Accept: stage 2 unit. Test: each of the three is accepted. See W55.
- **K205** A departure lists no more than the first call form and one different call form in `attempts`.
  - Src: A§8.6:799 ("at most one different call form"). Accept: stage 2 unit. Test: a third attempt is refused.
- **K206** `error_code` is recorded as read out of the error's message string, not guessed.
  - Src: A§8.6:799. Accept: stage 2 unit. Test: an empty `error_code` is refused.
- **K207** `ui-step` appends a `ui_steps[]` entry holding `key`, `what`, `owner`, `target_version` and `status`.
  - Src: A§7.3:577; RM:123. Accept: stage 2 unit. Test: the entry has the five keys. See W55.
- **K208** A UI step's key has the shape `U1`.
  - Src: A§7.3:582. Accept: stage 2 unit. Test: a key of another shape refused.
- **K209** A UI step's `status` is `open` or `done`.
  - Src: RM:123. Accept: stage 2 unit. Test: any other word refused.
- **K210** `irreversible-yes` appends an `irreversible_yes[]` entry holding `key`, `what`, `at`, `mode`, `approval_ref` and `log_ref`.
  - Src: A§7.3:575; RM:123. Accept: stage 2 unit. Test: the entry has the six keys. See W48.
- **K211** `irreversible-yes` refuses a key that is not in the approval's `irreversible_listed`.
  - Src: A§7.3:553 and :575; A§8.6:800. Accept: stage 2 unit. Test: an unlisted key refused.
- **K212** `irreversible_yes[].at` is a UTC stamp.
  - Src: G40; A§7.3:575. Accept: stage 2 unit. Test: the stamp parses with the UTC format. See W14.
- **K213** In a client's account each irreversible step is answered per item: a yes is recorded for the steps the user said yes to and for no others.
  - Src: A§8.6:800; BP:148. Accept: stage 2 unit. Test: three listed steps, a yes to the first and third; only two entries exist, and `intent` for the second is refused.
- **K214** A yes recorded under one run is not accepted for an irreversible write in a later run or session.
  - Src: A§8.6:800; SF 4 (the yes never carries to another session). Accept: stage 2 unit. Test: record a yes, end the run, take a new lease and start a new run; `intent` for the same row is refused until a new yes. See W48 for how the session is told.
- **K215** An archive's yes carries its containment evidence.
  - Src: A§8.6:800; A§9.4:880. Accept: stage 2 unit. Test: an archive row's yes with no evidence is refused. See W56 for the field.
- **K216** A row that has taken a yes carries `irreversible: true`, and the yes is findable from the row by its key.
  - Src: A§8.6:800; A§7.3:572. Accept: stage 2 unit. Test: after `irreversible-yes` and `intent`, the row is irreversible and the entry has its key.

### 2.14 The live map: `live-map` and `live-map set`

- **K217** `live-map` writes `live/live-map.md` from `account.json.live_objects`, with front matter `schema: "live-map/1"`, `client`, `rows` and `updated`, and one table.
  - Src: BP:386; A§7.8:691; RM:127. Accept: stage 2 unit. Test: the front matter has the four keys and `rows` equals the table's row count. See W59.
- **K218** The table's header line is `key | monday id | kind | built by | state | constraint | source | dependants | last verified`.
  - Src: RM:129 to 131; A§7.8:693 to 704 (one more column, `workspace`). Accept: stage 2 unit. Test: the header text. See W59.
- **K219** `live/live-map.md` and `account.json.live_objects` are written in the same step and agree row for row; a row on one side only is what `record.py check` blocks.
  - Src: BP:64; RM:127; A§7.8:691; BP:135. Accept: stage 2 unit. Test: after every writer, `record.py check` reports no live-map finding.
- **K220** A row's key is fully qualified (`001:B1`) and its monday id is a string.
  - Src: A§7.8:695; RM:77. Accept: stage 2 unit. Test: a bare key or a numeric id refused.
- **K221** A row's `kind` is any kind of the element-key list.
  - Src: RM:134; A§7.8:697. Accept: stage 2 unit. Test: each of the twenty kinds accepted. See W59 for the spelling of the AI kinds.
- **K222** A row's `built by` is a qualified version, or `client` or `native`.
  - Src: RM:134; A§7.8:699. Accept: stage 2 unit. Test: a bare `v0.1` refused.
- **K223** A row's `state` is one of the values the sources name: `active`, `archived`, `removed-by-platform`, and for an agent, workflow or sequence that exists but does not run, `inactive`.
  - Src: RM:134; A§7.8:700. Accept: stage 2 unit. Test: each accepted. See W59, which settles nothing about `inactive`.
- **K224** A row's `constraint` is `do-not-change`, `change-with-own-yes` or `free`.
  - Src: RM:134; A§7.8:701 and :710 to 714. Accept: stage 2 unit. Test: any other word refused.
- **K225** A row's `source` is a client quote with its call location, a user decision with its log reference, `pending strand close`, or `migration default, not confirmed with the client`.
  - Src: RM:134; A§7.8:702. Accept: stage 2 unit. Test: an empty source is refused.
- **K226** Workspaces are rows of the live map too.
  - Src: A§7.8:706. Accept: stage 2 unit. Test: `run end` after a verified workspace row writes a `workspace` row.
- **K227** `live-map set --key --constraint --source` sets one row's constraint and source.
  - Src: BP:135; A§7.8:718; A§8.10:829. Accept: stage 2 unit. Test: the row's two fields change and no other field does.
- **K228** `live-map set` refuses a key that has no row.
  - Src: BP:135; A§7.8:708. Accept: stage 2 unit. Test: an unknown key refused. See W62.
- **K229** `live-map set` refuses a constraint outside the three values.
  - Src: A§7.8:701. Accept: stage 2 unit. Test: refused.
- **K230** `live-map set` refuses an empty `--source`, so the interim `pending strand close` is replaced by a stated origin.
  - Src: A§7.8:718; A§8.10:829. Accept: stage 2 unit. Test: refused.
- **K231** `live-map set` writes the live-map file and `live_objects` in one step, as `run end` does.
  - Src: BP:135; A§7.8:691. Accept: stage 2 unit. Test: both files carry the new values after one call.
- **K232** A later `run end` leaves a row's constraint and source as `live-map set` last wrote them.
  - Src: A§7.8:718 (the strand close promotes the constraint). Accept: stage 2 unit. Test: promote a row, run another run's `run end`; the promoted values stand. See W61.
- **K233** `live-map` and `live-map set` are record-level and take `--strand` only to stamp who asked.
  - Src: BP:135. Accept: stage 2 unit. Test: as K38.

### 2.15 `check`

- **K234** `ledger.py check` verifies that `account.json` is `account/1` and every strand's `build.json` is `build/2`, known and not newer.
  - Src: A§7.1:390 and :417 ("must pass `ledger.py check`"); G57. Accept: stage 2 unit. Test: a `build/3` file is a blocking finding. See W63.
- **K235** `check` verifies the blocks and fields of `account.json` and `build.json` against the shapes of section 3.
  - Src: A§7.3:488 to 540; RM:119; RM:123. Accept: stage 2 unit. Test: delete one field per block; each is a finding naming file and field. See W06.
- **K236** `check` verifies each object's fields and value types per type, the AI kinds included.
  - Src: A§5.4:356. Accept: stage 2 unit. Test: as K153, through `check`.
- **K237** `check` verifies that `type`, `origin`, `status`, `state` and `verify.result` take only their listed values.
  - Src: A§7.3:582; RM:123. Accept: stage 2 unit. Test: one bad value each. See W12.
- **K238** `check` verifies that ids are strings.
  - Src: A§5.4:356. Accept: stage 2 unit. Test: a numeric id in a hand-edited file is a finding.
- **K239** `check` verifies that every parent key resolves.
  - Src: A§5.4:356. Accept: stage 2 unit. Test: a dangling `parent_key` is a finding.
- **K240** `check` verifies that `prior_state` appears only where the origin allows and is present where it is required.
  - Src: A§5.4:356; A§7.3:582. Accept: stage 2 unit. Test: both directions.
- **K241** `check` verifies that every irreversible, list-approved, publication and removed row has an `approval_ref` that resolves to an approval.
  - Src: A§5.4:356; BP:135. Accept: stage 2 unit. Test: a dangling ref is a finding. See W07, W43.
- **K242** `check` verifies that each approval's `sha256` equals the sha256 of its frozen file on disk.
  - Src: A§5.4:356 ("frozen sha matches the approval"); A§9.7:928 (the ledger's sha in the snapshots). Accept: stage 2 unit. Test: a changed frozen file is a blocking finding.
- **K243** `check` resolves the key half of every `blueprint_ref` and `prompt_ref` (`v0.1r4#B1`) against the element-key table of the frozen revision; the revision half is `record.py check`'s.
  - Src: DECISIONS:630 (C129); PLAN §5 Q1 (a); PLAN §1 (the probe). Accept: stage 2 unit. Test: on the fixture, `v0.1r1#B9` blocks and `v0.1r1#B1` passes. See W42 for where the table sits.
- **K244** `check` verifies that no `other-strand-modified` row targets a live-map row marked `do-not-change`.
  - Src: A§7.3:582; A§7.8:712. Accept: stage 2 unit. Test: a planted row is a finding.
- **K245** `check` verifies that every row's `workspace`, and every entry of `workspace_scope`, is one of the client's workspaces.
  - Src: A§7.3:582; AM:83. Accept: stage 2 unit. Test: a planted outside workspace is a finding. See W40.
- **K246** `check` writes no file, and reads `account.json` and each `build.json` inside the mutex.
  - Src: BP:134; API:40 (the model's test). Accept: stage 2 unit. Test: the tree hash is equal before and after.
- **K247** `check` exits 1 when a blocking finding exists, 2 when only warnings exist, 0 when none, and 3 when it cannot read the record.
  - Src: G10; A§5.3:344. Accept: stage 2 unit. Test: one fixture per code.
- **K248** On an untouched copy of WP2's unit fixture, `check` reports nothing, or exactly the findings W06 settles.
  - Src: PLAN §7.2; API:55 (the fixture passes `record.py check`). Accept: stage 2 unit. Test: run `check` on the fixture copy. See W06.
- **K249** `check` verifies that every `irreversible_yes` entry names a key listed in an approval's `irreversible_listed` and an `approval_ref` that resolves.
  - Src: A§7.3:553 and :575. Accept: stage 2 unit. Test: a planted orphan entry is a finding.

### 2.16 `estimate` (A17)

- **K250** `estimate --strand` counts `create_items` batches at 20 items per call.
  - Src: BP:138; A§9.9:952. Accept: stage 2 unit. Test: 41 items count as 3 calls; 40 as 2; 0 as 0.
- **K251** `estimate --strand` counts `update_items` batches at 40 items per call.
  - Src: BP:138; A§9.9:952. Accept: stage 2 unit. Test: 81 updates count as 3 calls.
- **K252** The estimate includes the classification query's cost as calls: one call per page.
  - Src: BP:138; A§9.9:952; NO 2.6:57. Accept: stage 2 unit. Test: a record with 120 boards and 50 per page adds 3 calls. See W65.
- **K253** The estimate includes the classification query's cost as complexity, a second figure beside the calls.
  - Src: BP:138; A§9.9:952; NO 2.6:57. Accept: stage 2 unit. Test: the output holds a calls figure and a complexity figure for the query. See W65.
- **K254** The classification query pages at 25 to 50 boards, never 200.
  - Src: A§9.9:952; NO 2.6:57; G-92. Accept: stage 2 unit. Test: the page size used is within 25 to 50.
- **K255** The estimate counts the automation monthly action estimate against the plan's allowance where one exists.
  - Src: BP:138; A§9.5:910. Accept: stage 2 unit. Test: a plan with an allowance of 250 and two automations at 100 each is reported over; a plan with no allowance is reported as none. See W64.
- **K256** The estimate counts preflight (about 12 calls), one read-back per settings-bearing write or batch, the polls of an asynchronous creation, the account checks, and the audit (about 3 calls per board, the doc pages, and the per-kind reads of round two).
  - Src: A§9.9:952. Accept: stage 2 unit. Test: each component appears in the output with its count. See W65.
- **K257** `estimate --strand` reports the other open strands' approved-but-unbuilt estimates beside its own, against the one daily allowance.
  - Src: BP:138; A§9.9:952; BP:508 (H39). Accept: stage 2 unit; stage 4 headless H39. Test: two strands with approvals; strand 002's output shows strand 001's figure and the shared headroom. See W67.
- **K258** The script reads a sibling strand's approvals itself and prints totals only; the session reads nothing of the sibling's `build.json`.
  - Src: PLAN §8.8; PLAN §7.13; BP:508 (H39); A§7.8:708. Accept: stage 2 unit. Test: the output holds no element key, name or id of the sibling. See W68.
- **K259** A warning appears when the estimate exceeds 30% of the headroom, with an offer to split the build across days; the headroom is the daily total minus today's usage minus the client reserve.
  - Src: A§9.9:952. Accept: stage 2 unit. Test: a case just under and just over 30%.
- **K260** When `platform_api` cannot be read, the estimate assumes 1,000 calls a day and warns above 250.
  - Src: A§9.9:952. Accept: stage 2 unit. Test: the unreadable case warns at 251 and not at 250.
- **K261** The classification query is paid once per record per staleness window, never once per strand: a second strand's estimate inside the window counts it as already paid.
  - Src: BP:138; A§9.9:952; A§11.2:1065. Accept: stage 2 unit. Test: strand 001 and strand 002 estimates inside and outside the window; the query appears in one and is absent from the other inside the window. See W66.
- **K262** The estimate names which planned elements are AI-powered.
  - Src: BP:138; AM:117 (A17). Accept: stage 2 unit. Test: a plan with an agent, an AI column, a Vibe app and a board names the first three. See W69.
- **K263** The estimate states no credit figure and computes nothing from one; a credit field a tool returns is recorded as present and nothing else.
  - Src: BP:138; AM:117; A§9.9:952. Accept: stage 2 unit. Test: no output key or value holds a credit figure, a price or a package.
- **K264** The estimate prints a low and a high figure for the calls.
  - Src: A§7.3:557 (`estimated_calls [low, high]`); RM:123. Accept: stage 2 unit. Test: the output holds two numbers with low at most high. See W64.

### 2.17 `reconcile`

- **K265** `reconcile --strand` produces all seven classes from a recorded live inventory.
  - Src: BP:139; A§8.11:835. Accept: stage 2 unit (synthetic reads); stage 4 headless H23. Test: the reconcile fixture yields at least one element in each class. Met against synthetic reads; confirmed at capture (A11-1).
- **K266** The seven class tokens are `adopt`, `retry`, `duplicate`, `partial`, `changed-since-verified`, `unrecorded-extra` and `missing`.
  - Src: G04; RM:123; A§8.11:835 (prose forms). Accept: stage 2 unit. Test: the output keys equal that list.
- **K267** An element is `adopt` when exactly one live match exists under the recorded parent or scope and was created after the attempt started.
  - Src: A§8.11:835; SF 9. Accept: stage 2 unit (synthetic reads). Test: one case that is adopt and two that are not (two matches; created before). See W71 for what "match" is per kind.
- **K268** An element is `retry` when its attempt left nothing live.
  - Src: A§8.11:835. Accept: stage 2 unit (synthetic reads). Test: an `attempting` element with no live match. See W71.
- **K269** An element is `duplicate` when more than one live object matches it; the extra becomes an archive or deactivation proposal with its own yes, and the user chooses.
  - Src: A§8.11:835; SF 9. Accept: stage 2 unit (synthetic reads). Test: two live matches classify `duplicate`; nothing is archived. See W71.
- **K270** An element is `partial` when its live object exists but was not completed.
  - Src: A§8.11:835 (the class is named and not defined). Accept: stage 2 unit (synthetic reads). Test: a board with the recorded columns missing. See W71.
- **K271** An element is `changed-since-verified` when a verified element's live read no longer equals its recorded digest.
  - Src: A§8.11:835; A§7.3:570. Accept: stage 2 unit (synthetic reads). Test: a verified row whose live digest moved. See W71, W73.
- **K272** A live object with no row is `unrecorded-extra`, and is never adopted when it predates the attempt.
  - Src: A§8.11:835; SF 9. Accept: stage 2 unit (synthetic reads). Test: an unknown live board created before the attempt is `unrecorded-extra` and not offered for adoption.
- **K273** A recorded element with no live object is `missing`.
  - Src: A§8.11:835. Accept: stage 2 unit (synthetic reads). Test: a verified row whose live object is absent. See W71.
- **K274** Automations are listed first in the output.
  - Src: BP:139; A§8.11:835; SF 9. Accept: stage 2 unit; stage 4 headless H23. Test: in the output order, every automation precedes every other element.
- **K275** The AI kinds follow the automations: agents, then Vibe apps, then workflows.
  - Src: A§8.11:835; BP:492 (H23). Accept: stage 2 unit. Test: the order of the second group. See W71.
- **K276** The AI kinds are classified like any other, from the agent, Vibe and workflow lists of the inventory.
  - Src: BP:139; A§8.11:835; AI:10, :35, :55. Accept: stage 2 unit (synthetic reads); capture (A11-1). Test: an agent, a Vibe app and a workflow each land in a class. Met against synthetic reads; confirmed at capture (A11-1).
- **K277** A lost `create_automation` reply is reported as needing the user's confirmation after the board's automation list is seen, on an own-account proof of concept too.
  - Src: A§8.11:835; SF 5; AM:18. Accept: stage 2 unit. Test: an `attempting` automation with a live match is reported with that flag and is not silently adopted. See W71.
- **K278** `reconcile` reads the recorded live inventory from `.work/strands/<id>/live-inventory.json`.
  - Src: A§8.11:835; RM:68. Accept: stage 2 unit. Test: the command takes no other source. See W70 for the file's shape.
- **K279** `reconcile --strand <holder> --classify-only`, run from a sibling strand's session, writes the classes into the holder's ledger as findings.
  - Src: BP:139; A§8.11:837. Accept: stage 2 unit; stage 4 headless H35. Test: after the call, the holder's `build.json` holds the findings. See W72 for where.
- **K280** It also writes the interrupted run's `reconcile` object: `at` in UTC, `mode: "classify-only"`, and `classes`, the counts of the seven tokens.
  - Src: BP:139; G04; RM:123. Accept: stage 2 unit; stage 4 headless H35. Test: the object has the three keys; `at` parses as UTC.
- **K281** It marks that run `interrupted`; the run is the one whose id is the lock's `run_id`.
  - Src: BP:139; G04; DECISIONS:37. Accept: stage 2 unit; stage 4 headless H35. Test: the run's `state` is `interrupted`. See W72.
- **K282** It adopts, retries and archives nothing: no row's status, id or field changes.
  - Src: BP:139; A§8.11:837. Accept: stage 2 unit; stage 4 headless H35. Test: every `objects` row is byte-equal before and after.
- **K283** The classify-only write is made under the record mutex and needs no lease epoch or session label, because the sibling that runs it holds no lease on the holder's strand.
  - Src: A§8.11:837; A§9.8:946; BP:139. Accept: stage 2 unit. Test: run it with no fence flags while the lease is stale and held by the holder. See W72.
- **K284** The `classes` object always carries all seven keys as integers, zero where a class is empty.
  - Src: G04; DECISIONS:37 (the break reads `duplicate` and `partial`). Accept: stage 2 unit. Test: an all-adopt inventory prints seven keys.
- **K285** The reconcile scenarios of H23 and the classify-only half of H35 pass headless.
  - Src: BP:149; BP:492; BP:504. Accept: stage 4 headless H23, H35. Test: the two rows pass once WP14's runner and seeds exist. See W04.

### 2.18 `snapshot`, `compare` and its tokenizer (A§9.7)

- **K286** `snapshot` records the read it is handed as a machine file in the record, with its ring, its time and its scope.
  - Src: BP:135; A§7.1:399; A§9.7:928; RM:26. Accept: stage 2 unit. Test: the file exists after the call with those three fields. See W19, W74.
- **K287** A snapshot's scope is the strand's own elements plus every live-map row marked `do-not-change` or `change-with-own-yes`, whatever strand built it.
  - Src: A§9.7:928; A§8.7:809. Accept: stage 2 unit. Test: a read holding an out-of-scope board is refused or trimmed. See W74.
- **K288** A snapshot records the sha256 of the strand ledger and of `account.json`.
  - Src: A§9.7:928. Accept: stage 2 unit. Test: both hashes are in the file and equal the files' hashes.
- **K289** A snapshot can hold each part A§9.7 lists: the board inventory, the per-board digests, automations, forms, doc block counts, dashboards, and for round two agents, workflows and Vibe apps.
  - Src: A§9.7:928. Accept: stage 2 unit (synthetic reads). Test: the compare fixture's snapshots carry every part.
- **K290** `snapshot` makes no monday call and reads no monday: it records what the session hands it.
  - Src: A§5.3:340; A§9.7:928. Accept: stage 2 unit. Test: no network module is imported. See W78.
- **K291** `compare` is offline: it reads two recorded snapshots from the record and nothing else.
  - Src: BP:140; PLAN §4.2. Accept: stage 2 unit. Test: run with the network module blocked; the result is unchanged.
- **K292** `compare` flags a description change.
  - Src: BP:140; BP:493 (H24). Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: the compare fixture's description change is flagged. Met against synthetic reads; confirmed at capture (A11-1).
- **K293** `compare` flags an archived board.
  - Src: BP:140; BP:493. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for an archived board.
- **K294** `compare` flags a changed column digest.
  - Src: BP:140; BP:493. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for a column digest. See W73.
- **K295** `compare` flags an owner change.
  - Src: BP:140; BP:493. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for an owner.
- **K296** `compare` flags an agent whose `version_id` moved.
  - Src: BP:140; BP:493; AI:21. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for a `version_id`.
- **K297** `compare` flags an agent whose state moved.
  - Src: BP:140; BP:493; AI:21. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for an agent state, and a state move leaves `version_id` equal.
- **K298** `compare` flags a workflow whose state moved.
  - Src: BP:140; BP:493. Accept: stage 2 unit (synthetic reads); stage 4 headless H24. Test: as K292 for a workflow state.
- **K299** `compare` flags nothing for the controls: unchanged boards, and changes outside the list of K292 to K298 that W75 leaves unnamed.
  - Src: BP:140; PLAN §4.2. Accept: stage 2 unit (synthetic reads). Test: the fixture's control pairs produce no flag. See W75.
- **K300** A protected live-map row whose digest moved before the before snapshot is reported as changed outside this strand, not as a write during the audit.
  - Src: A§9.7:928; A§7.8:716; PLAN §4.2. Accept: stage 2 unit (synthetic reads). Test: the planted row is reported under that wording and not in the write-detected list.
- **K301** A changed-outside-this-strand finding is reported, never auto-fixed, and never voids the strand's own result.
  - Src: A§7.8:716; A§8.7:811. Accept: stage 2 unit. Test: the output marks it a finding against the record and writes no live-map change.
- **K302** `compare` also compares the ledger's and `account.json`'s sha256 between the two snapshots.
  - Src: A§9.7:928. Accept: stage 2 unit. Test: a changed ledger between snapshots is flagged.
- **K303** The documents-appendix scan refuses any document that carries a mutation operation.
  - Src: BP:140; A§9.7:928; AM:184 to 186 (A2); A§8.7:809. Accept: stage 2 unit. Test: the planted mutation document is refused.
- **K304** The scan refuses any document that carries a subscription operation.
  - Src: BP:140; A§9.7:928. Accept: stage 2 unit. Test: the planted subscription is refused.
- **K305** The scan refuses any document that carries more than one operation.
  - Src: BP:140; A§9.7:926 and :928. Accept: stage 2 unit. Test: the planted two-operation document is refused, whichever operation comes first.
- **K306** The scan passes a clean single query.
  - Src: BP:140. Accept: stage 2 unit. Test: the planted clean query passes.
- **K307** The word "mutation" inside a string literal or a comment does not trip the scan.
  - Src: BP:140; PLAN §4.2. Accept: stage 2 unit. Test: the planted documents with the word in a string and in a comment pass.
- **K308** The tokenizer lives inside `ledger.py` and not in a script of its own.
  - Src: BP:140; A§9.7:928 (D7). Accept: stage 2 unit (inspection). Test: no other script holds it. See W77 for what it must tokenize.
- **K309** A unit test on planted documents proves K303 to K307.
  - Src: BP:140. Accept: stage 2 unit. Test: the test exists and covers all five cases.
- **K310** Each flag names the object, the field and the two values, so the finding has four parts.
  - Src: A§5.3:344; A§8.7:810. Accept: stage 2 unit. Test: assert four non-empty parts on every flag. See W76.
- **K311** The offline compare of H24 passes headless.
  - Src: BP:149; BP:493. Accept: stage 4 headless H24. Test: the row passes once WP14's runner and seeds exist. See W04.

### 2.19 `classify` on the identification fixture (R0 to R11, C1 to C4)

Every clause in 2.19 to 2.24 is graded against the synthetic reads of A29 and says so: "met against synthetic reads; confirmed at capture (A11-1)". The classes are the ones NO 5 names; section 3 lists them.

- **K312** `classify` reads the recorded response pages it is handed, and classifies every board on every page.
  - Src: BP:141; PLAN §4.1; A§11.2:1065. Accept: stage 2 unit (synthetic reads); capture (A11-1). Test: run it on `identification.reads.json`; each board gets one class. See W78 for how the pages are handed over.
- **K313** R0: every state is classified, active, archived and deleted, and the sweep is complete only when it ended on an empty page.
  - Src: NO 5:131; A§11.2:1065; G-09. Accept: stage 2 unit (synthetic reads). Test: the fixture's page chain ends on an empty page; a chain cut short is reported incomplete. Met against synthetic reads; confirmed at capture (A11-1).
- **K314** State is an attribute and never a role; a deleted board is classified from its board-level fields and its lineage only.
  - Src: NO 5:127; A§11.2:1065; G-77. Accept: stage 2 unit (synthetic reads). Test: a deleted board with no columns is classified; its state is an attribute.
- **K315** R1: `type` `document` is a `doc_container`, with its doc id from the docs list.
  - Src: NO 5:132. Accept: stage 2 unit (synthetic reads). Test: the fixture's doc container.
- **K316** R2: `type` `sub_items_board` is a `subitems_board`, with its parent taken from the board whose subtasks settings name it.
  - Src: NO 5:133. Accept: stage 2 unit (synthetic reads). Test: the fixture's subitems board and its parent. See W81.
- **K317** R3: `type` `custom_object` is a `workflow_object` when it is in the workflow objects set, and otherwise a `custom_object_other`.
  - Src: NO 5:134; PLAN §7.8. Accept: stage 2 unit (synthetic reads). Test: the fixture's workflow object and another custom object. See W79, W81.
- **K318** R4: key `work-management::portfolio` is a `portfolio_board`.
  - Src: NO 5:135. Accept: stage 2 unit (synthetic reads). Test: the fixture's portfolio.
- **K319** R5: key `work-management::portfolio-project` or `work-management::project` is a `project_tasks_board` when at least two of the four `project_*` ids are present or the board carries the tasks template's lineage.
  - Src: NO 5:136; NO 7.2. Accept: stage 2 unit (synthetic reads). Test: the fixture's created tasks board.
- **K320** R5: the same keys with fewer than two of those ids and no template lineage give a `converted_project_board`.
  - Src: NO 5:136; G-80. Accept: stage 2 unit (synthetic reads). Test: the fixture's converted board.
- **K321** R5: the same keys with columns hidden and no template lineage give a `project_board_origin_unknown`.
  - Src: NO 5:136. Accept: stage 2 unit (synthetic reads). Test: the fixture's board of unknown origin.
- **K322** R5: the transient key `work-management::project` and the settled key mean the same role.
  - Src: NO 7.1; G-73; A§11.1:1057. Accept: stage 2 unit (synthetic reads). Test: two fixture boards differing only in that key get the same class.
- **K323** R6: key `work-management::standalone` is a `project_overview_companion`, and a deleted one means its project was connected.
  - Src: NO 5:137. Accept: stage 2 unit (synthetic reads). Test: one live and one deleted overview in the fixture.
- **K324** R7: any other non-null key is a `keyed_board_unrecognized_key` that stops for review and never falls through to a later rule.
  - Src: NO 5:138; A§11.2:1065. Accept: stage 2 unit (synthetic reads). Test: the fixture's unrecognised key.
- **K325** R8: key null and at least five of the nine `rp_*` ids is a `resource_planner_companion`.
  - Src: NO 5:153; NO 7.2. Accept: stage 2 unit (synthetic reads). Test: the fixture's planner, and a board with four ids that is not one.
- **K326** R9: key null and at least five `portfolio_project_*` ids is a `portfolio_shaped_board_without_key`, for review.
  - Src: NO 5:154. Accept: stage 2 unit (synthetic reads). Test: the fixture's portfolio-shaped board.
- **K327** R10: `hierarchy_type` `multi_level` is a `multi_level_board_not_project`.
  - Src: NO 5:155. Accept: stage 2 unit (synthetic reads). Test: the fixture's multi-level board.
- **K328** R11: anything left is a `normal_classic_board`.
  - Src: NO 5:156. Accept: stage 2 unit (synthetic reads). Test: the fixture's ordinary board.
- **K329** No board with a non-null key is classified `normal_classic_board`.
  - Src: BP:141; NO 5:138. Accept: stage 2 unit (synthetic reads); stage 4 headless H25. Test: for every keyed board in the fixture, the class is not R11's.
- **K330** The converted project is separated from the created one.
  - Src: BP:141; BP:494 (H25). Accept: stage 2 unit (synthetic reads); stage 4 headless H25. Test: the two fixture boards get K320's and K319's classes.
- **K331** The multi-level non-project board is not read as a project.
  - Src: BP:141; BP:494. Accept: stage 2 unit (synthetic reads); stage 4 headless H25. Test: the fixture's multi-level board gets K327's class.
- **K332** C1 and C2: a project is connected only when its tasks board is in the portfolio's link column settings and one portfolio row links items on that board.
  - Src: BP:141; NO 7.3; A§11.3:1076; G-78. Accept: stage 2 unit (synthetic reads). Test: the fixture's connected project is reported connected. See W80 for which of C1 to C4 is which.
- **K333** One half alone is reported as `partial link - review`, never as connected.
  - Src: NO 7.3; A§11.3:1076. Accept: stage 2 unit (synthetic reads). Test: the fixture's two one-half cases. See W80.
- **K334** Neither half is `unconnected`, naming the overview when a relation column of the project targets an R6 board.
  - Src: NO 7.3. Accept: stage 2 unit (synthetic reads). Test: the fixture's unconnected project. See W80.
- **K335** C4: folder, workspace and name evidence never counts toward a connection.
  - Src: BP:141; NO 7.3 and 7.4; A§11.3:1076. Accept: stage 2 unit (synthetic reads). Test: the fixture's project sharing a folder with a portfolio and not connected stays unconnected.
- **K336** A portfolio whose items page carries a non-null cursor is reported as an incomplete read, and no project is called unconnected from it.
  - Src: NO 7.3. Accept: stage 2 unit (synthetic reads). Test: the fixture page with a cursor.
- **K337** On the identification fixture, no board is misclassified.
  - Src: BP:141; BP:494. Accept: stage 2 unit (synthetic reads); stage 4 headless H25. Test: compare every result with `identification.expected.json`; zero differences.
- **K338** The fixture states its own totals per class, and the totals add up to the fixture's board count.
  - Src: BP:141; PLAN §4.1. Accept: stage 2 unit. Test: sum the totals; equal to the number of boards; and `classify`'s own totals equal them.
- **K339** The classify rows H25 pass headless.
  - Src: BP:149; BP:494. Accept: stage 4 headless H25. Test: the row passes once WP14's runner and seeds exist. See W04.

### 2.20 `classify` on the native fixture (N0 to N12)

- **K340** N0: the workspace's product kind is a soft gate: it picks the catalogue to prefer, and both catalogues run on every board.
  - Src: NO 5:139; NO 2.5; A§11.1:1046. Accept: stage 2 unit (synthetic reads). Test: a CRM native in a core workspace is still matched.
- **K341** N1a: a custom object in the Portal `objects()` set, read in both the active and the archived alias, is a `native_service_portal`, definitive.
  - Src: NO 5:140; NO 4.4; G-100. Accept: stage 2 unit (synthetic reads). Test: the fixture's active and archived Portals.
- **K342** N1b: a custom object with the Portal lineage or the Portal template view is a `native_service_portal`, strong, which finds an archived Portal and does not swallow a workflow object.
  - Src: NO 5:141; NO 4.4. Accept: stage 2 unit (synthetic reads). Test: an archived Portal found by lineage; a workflow object not found. See W81.
- **K343** N2: a lineage walk that resolves to a template id is a `native_<product>_<entity>` with install kind `direct_install` at zero hops and `descendant_copy(n)` beyond.
  - Src: NO 5:142; NO 2.1. Accept: stage 2 unit (synthetic reads). Test: the 0-, 1- and 2-hop fixtures. See W83 for the class vocabulary.
- **K344** N3: a view whose `source_view_id` is in the template view ids is a `native_<product>_<entity>` with install kind `direct_install`.
  - Src: NO 5:143; NO 2.2. Accept: stage 2 unit (synthetic reads). Test: the fixture's board with a template view id and a cleared lineage.
- **K345** N4: a reserved-id signature that meets its entity's threshold is a `native_<product>_<entity>`, with install kind `descendant_fingerprint` when the lineage is `UNRESOLVED` or `NO_LINEAGE`.
  - Src: NO 5:144; NO 2.3. Accept: stage 2 unit (synthetic reads). Test: the chain-broken fixture natives. See W84.
- **K346** N5: a subitems board with its line-item threshold met, its tickets-subitems threshold met, or resolved lineage is a `native_<product>_<entity>_subitems`.
  - Src: NO 5:145. Accept: stage 2 unit (synthetic reads). Test: the fixture's line-items board and tickets subitems. See W81.
- **K347** N6: a board with no signature, in a CRM workspace, carrying a CRM relation mark or a CRM mirror mark is a `native_crm_companion_board`, at moderate confidence.
  - Src: NO 5:146; NO 2.4. Accept: stage 2 unit (synthetic reads). Test: the fixture's companions.
- **K348** N7: a Service board with native terminology that is the relation target of a classified native Tickets board, and has neither lineage nor a template view, is a `native_service_satellite_probable`, for review only.
  - Src: NO 5:147. Accept: stage 2 unit (synthetic reads). Test: the fixture's satellite.
- **K349** N8: a board in a CRM or Service workspace with a null key, no lineage, no reserved ids, no marks and a native name or terminology is a `lookalike_board`.
  - Src: NO 5:148; BP:144. Accept: stage 2 unit (synthetic reads). Test: the fixture's two look-alikes.
- **K350** N9: a board in a CRM or Service workspace with no signal and no imitation is an `ordinary_board_in_product_workspace`.
  - Src: NO 5:149. Accept: stage 2 unit (synthetic reads). Test: the fixture's ordinary boards in product workspaces.
- **K351** N10: a native fingerprint on a board whose product is not CRM or Service is a `native_descendant_misplaced`, for review.
  - Src: NO 5:150; G-106. Accept: stage 2 unit (synthetic reads). Test: the fixture's native moved into a core workspace.
- **K352** N11: otherwise a board is an `ordinary_board`, handed back to R8 to R11.
  - Src: NO 5:151. Accept: stage 2 unit (synthetic reads). Test: the fixture's ordinary boards in a test workspace end as R11's class.
- **K353** N12: family and version, install kind (`direct_install`, `descendant_copy(n)`, `descendant_fingerprint`, `lineage_unresolved`), the SLA mark, state and items count are recorded as attributes beside the class, never as the class.
  - Src: NO 5:152; A§11.2:1065. Accept: stage 2 unit (synthetic reads). Test: the expected key's attributes equal the output's for every native board.
- **K354** A board on which any N rule fires is never reported as `normal_classic_board`.
  - Src: NO 5:127; A§11:1040. Accept: stage 2 unit (synthetic reads). Test: every native in the fixture.
- **K355** The native rules apply after the key gates R4 to R7 and before R8, so a native with no key does not fall through to R11.
  - Src: NO 5:127; A§11:1040; A§11.2:1065. Accept: stage 2 unit (synthetic reads). Test: a keyed board and a native, each reaching its own rule. See W81.
- **K356** CRM natives and their descendants are classified, in the v2 and the core v1 catalogues, each entity, the companions and the Quotes & Invoices and Products & Services boards included.
  - Src: BP:141; NO 3. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: every CRM board of the fixture equals its expected class.
- **K357** Service natives and their descendants are classified in families A to D, their subitems and satellites included.
  - Src: BP:141; NO 4; A§11.4:1087. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: every Service board of the fixture equals its expected class.
- **K358** The Service Portal is classified in both its active and its archived state.
  - Src: BP:141; NO 4.4; A§11.4:1089. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: as K341 and K342.
- **K359** From-scratch look-alikes are classified as such.
  - Src: BP:141; BP:495 (H26). Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: as K349.
- **K360** Ordinary boards inside product workspaces are classified `ordinary_board_in_product_workspace`.
  - Src: BP:141. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: as K350.
- **K361** Ordinary boards in a test workspace are classified as ordinary.
  - Src: BP:141. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: as K352.
- **K362** The boards the identification ruleset owns, keyed boards, another custom object and a product's "Start here" doc, keep their identification class rather than a native one.
  - Src: BP:141; NO 4.1:104. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the three fixture boards keep their R-classes.
- **K363** A "Start here" doc stays a `doc_container` and its template lineage is an attribute.
  - Src: NO 4.1:104; BP:141. Accept: stage 2 unit (synthetic reads). Test: the fixture's doc.
- **K364** A deleted native is classified from its lineage alone.
  - Src: NO 2.1:15; NO 5:127. Accept: stage 2 unit (synthetic reads). Test: the fixture's deleted native.
- **K365** On the native fixture, no board is misclassified, across every class the rule set names.
  - Src: BP:141; BP:495. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: compare every result with `native.expected.json`; zero differences.
- **K366** The native fixture states its own totals per class, and a grader that cannot add the classes to the fixture's total has the wrong fixture.
  - Src: BP:141. Accept: stage 2 unit. Test: the totals add up to the board count; `classify`'s totals equal them.
- **K367** The classify rows H26 pass headless.
  - Src: BP:149; BP:495. Accept: stage 4 headless H26. Test: as K339. See W04.
- **K368** Each result carries its rule id, its signals and its confidence.
  - Src: NO 5:158; A§11.2:1065. Accept: stage 2 unit (synthetic reads). Test: every output entry has the three; compare with the key. See W85.
- **K369** A reserved id is matched by its id and then its type is read to pick the family; a type is never asserted for a reserved id.
  - Src: NO 2.3:19; G-96. Accept: stage 2 unit (synthetic reads). Test: a board whose `deal_close_probability` is a formula is a v2 Opportunities, one whose is numbers a v1 Deals.
- **K370** The product's catalogue constants (template ids, template view ids, reserved ids, thresholds, default names and terminologies) are those of NO 3, 4 and 5, with no constant added.
  - Src: NO 3 to 5; PLAN §4.1. Accept: stage 2 unit. Test: compare the script's tables with the sections of NO. See W87.

### 2.21 Lineage (BP:142)

- **K371** Lineage is walked hop by hop to a terminal id, not read once.
  - Src: BP:142; NO 2.1; G-94. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the 2-hop fixture resolves only if the walk follows the second hop.
- **K372** A 0-hop direct install resolves.
  - Src: BP:142. Accept: stage 2 unit (synthetic reads). Test: a board pointing at a template id.
- **K373** A 1-hop duplicate resolves.
  - Src: BP:142. Accept: stage 2 unit (synthetic reads). Test: a board pointing at a native install that points at a template.
- **K374** A 2-hop copy of a copy resolves.
  - Src: BP:142. Accept: stage 2 unit (synthetic reads). Test: a chain of three boards ending at a template.
- **K375** A hop whose id is in a template catalogue ends the walk as `RESOLVED_TEMPLATE`, with the entity and family known and the hop count equal to the distance.
  - Src: NO 2.1. Accept: stage 2 unit (synthetic reads). Test: the three fixtures give hop counts 0, 1 and 2.
- **K376** A null `created_from_board_id` ends the walk as `NO_LINEAGE`.
  - Src: NO 2.1; G-94. Accept: stage 2 unit (synthetic reads). Test: a board with a null pointer.
- **K377** An id the read does not return ends the walk as `UNRESOLVED`.
  - Src: NO 2.1; G-94; G-92. Accept: stage 2 unit (synthetic reads). Test: the fixture's unreadable intermediate.
- **K378** The walk stops after five hops.
  - Src: NO 2.1. Accept: stage 2 unit (synthetic reads). Test: a six-hop chain ends at the fifth hop. See W86 for the result.
- **K379** An unreadable intermediate ends the chain as `UNRESOLVED` and never as "not native".
  - Src: BP:142; A§11.1:1047. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the fixture board is not classed ordinary on that ground.
- **K380** An id requested and not returned is recorded as unreadable, never as deleted and never as non-native, by a diff of requested ids against returned ids on every page.
  - Src: NO 2.6:57; G-92; A§11.1:1051; BP:147. Accept: stage 2 unit (synthetic reads). Test: the fixture page whose `boards(ids:)` drops an id.
- **K381** Lineage still works on a deleted board, where columns and views come back empty.
  - Src: NO 2.1; G-77. Accept: stage 2 unit (synthetic reads). Test: as K364.
- **K382** Each resolved or unresolved chain is recorded as `lineage {chain, resolved, note}`, and each unreadable intermediate is collected for `unreadable_intermediate_ids`.
  - Src: A§7.3:506; A§11.1:1047; RM:119. Accept: stage 2 unit (synthetic reads). Test: the expected key's lineage objects equal the output's.

### 2.22 Reserved-id signatures (BP:143)

- **K383** Reserved-id signatures stand alone where the chain breaks, because a native's chain can be broken in a live account.
  - Src: BP:143; NO 2.3; G-96. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the chain-broken fixture native is classified by its reserved ids alone.
- **K384** A chain-broken native found by its reserved ids alone has install kind `descendant_fingerprint`.
  - Src: NO 5:144; PLAN §4.2. Accept: stage 2 unit (synthetic reads). Test: as K383, the attribute.
- **K385** A template view id alone classifies a board where the lineage is cleared.
  - Src: NO 2.2; A§11.1:1045. Accept: stage 2 unit (synthetic reads). Test: as K344.
- **K386** The blank-board defaults `person`, `status`, `date4` and `date0` are excluded from every signature.
  - Src: BP:143; NO 2.3; G-98. Accept: stage 2 unit (synthetic reads). Test: a board of blank defaults only matches no entity.
- **K387** A randomly suffixed id never disqualifies a board.
  - Src: BP:143; NO 2.3; G-96. Accept: stage 2 unit (synthetic reads). Test: a native carrying suffixed ids beside its signature still classifies.
- **K388** A randomly suffixed id never counts toward a signature.
  - Src: BP:143; NO 2.3. Accept: stage 2 unit (synthetic reads). Test: a board of suffixed ids only is not matched.
- **K389** Each entity's threshold is the one NO gives: three for leads, opportunities or deals, contacts, accounts, activities, quotes and invoices, and sales targets; two for products and services; six for line items; six for tickets; four for ticket subitems; five for asset management; four (weak) for employee lifecycle and two (weak) for employee directory; lineage only for deals subitems; no signature for Incidents, CSAT Survey and Service Contacts.
  - Src: NO 3.3; NO 4.3. Accept: stage 2 unit. Test: one board one id under and one at each threshold.
- **K390** Quotes and Invoices, whose ids are generic, need corroboration by lineage, a template view id or its terminology.
  - Src: NO 3.3:85. Accept: stage 2 unit (synthetic reads). Test: the six generic ids alone do not classify.

### 2.23 Look-alikes (BP:144)

- **K391** Both look-alike boards are caught by N8.
  - Src: BP:144; BP:495. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: both fixture look-alikes get N8's class.
- **K392** Neither look-alike is caught by its name.
  - Src: BP:144; NO 6.1; G-97. Accept: stage 2 unit (synthetic reads). Test: rename a look-alike; the class is unchanged; the class never depends on the name.
- **K393** A renamed native whose item terminology changed is still classified native.
  - Src: BP:144; G-97. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the fixture's renamed native.
- **K394** A board that merely links into a native stays ordinary: inbound relations are ignored when classifying.
  - Src: BP:144; G-104. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the fixture's ordinary board with a relation into Tickets.
- **K395** The imitation test compares against the native default names and terminologies exactly, a trailing space included, and leaves `Org` and `Client` out.
  - Src: NO 5:158; G-97. Accept: stage 2 unit (synthetic reads). Test: terminology `"Activity "` (trailing space) and `Activity` both match, since NO 5:158 lists both; a terminology differing from every entry only in case or spacing, such as `activity` or `"Activity  "`, does not; `Org` and `Client` flag nothing. (Corrected 2026-10-16 after the trace check: the earlier Test line said `"Activity"` does not match, which contradicts NO 5:158.)

### 2.24 The two known limits (BP:145)

- **K396** Planted reserved ids inside a product workspace classify the same as a chain-broken native, and the result is reported as a known limit with its reason.
  - Src: BP:145; NO 6.1 and 6.5; G-93; G-107. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the fixture's planted board gets the chain-broken native's class, marked `limit`.
- **K397** A native stripped of its template columns with a broken chain reads as ordinary or as a look-alike, and the result is reported as a known limit with its reason.
  - Src: BP:145; NO 6.5; G-107. Accept: stage 2 unit (synthetic reads); stage 4 headless H26. Test: the fixture's stripped native, marked `limit`.
- **K398** The two limits are reproduced as limits and never counted as passes: neither is resolved, and the expected key lists them apart from the totals of passes.
  - Src: BP:145; BP:495. Accept: stage 2 unit (synthetic reads). Test: the totals of passes exclude them; the output names the reason.
- **K399** A default-shaped satellite (Incidents, CSAT Survey, Service Contacts) that has lost its lineage is stated as a limit and never guessed.
  - Src: A§11.4:1088; NO 6.5; G-107. Accept: stage 2 unit (synthetic reads). Test: the fixture's lineage-stripped copy is reported as a limit.

### 2.25 `native-map` and the `guard_index` fields (BP:146)

- **K400** `native-map` records the signals and the confidence per entity.
  - Src: BP:146; A§7.3:503 to 510. Accept: stage 2 unit (synthetic reads). Test: each entry holds `signals[]` and `confidence`.
- **K401** Each `native_map` entry holds `board_id`, `rule`, `confidence`, `signals[]`, `lineage {chain, resolved, note}` and `confirmed_by_user`, with `family` on a Service entity and `projects[]` on a portfolio.
  - Src: RM:119; A§7.3:504 to 507. Accept: stage 2 unit. Test: the keys per entry. See W16 for the entity names.
- **K402** `confidence` is `high`, `medium` or `low`.
  - Src: RM:119. Accept: stage 2 unit. Test: any other word refused.
- **K403** `native-map` refuses to mark any entry below high confidence as confirmed.
  - Src: BP:146; RM:119. Accept: stage 2 unit. Test: `confirmed_by_user: true` on a `medium` entry refused. See W88.
- **K404** `native-map` stores the flat `native_board_index` in `guard_index`, keyed by board id, with the product and entity as the value.
  - Src: BP:146; A§7.3:514; NO 6.2. Accept: stage 2 unit (synthetic reads). Test: every native in the fixture is a key; no ordinary board is. See W16.
- **K405** It stores `native_board_ids_by_entity` and `product_workspaces`, the workspace id to product kind map.
  - Src: A§7.3:512 and :515; NO 6.2. Accept: stage 2 unit (synthetic reads). Test: the two blocks equal the expected key's.
- **K406** It stores `account_products`, each with id, kind and default workspace id.
  - Src: A§7.3:513; RM:119. Accept: stage 2 unit (synthetic reads). Test: the block's keys.
- **K407** It stores `template_source_ids` and the unreadable intermediate ids, and `template_view_ids`.
  - Src: BP:146; A§7.3:516 to 518; NO 6.2. Accept: stage 2 unit (synthetic reads). Test: the unreadable intermediate of K377 appears. See W18 for one field or two.
- **K408** It stores `reserved_column_ids` with each entity's ids and threshold, and the blank-default exclusions.
  - Src: BP:146; A§7.3:519 and :520. Accept: stage 2 unit. Test: the block equals NO 3.3 and 4.3 for the entities seen.
- **K409** It stores `native_default_names_and_terminology`, for the ask path only.
  - Src: A§7.3:521; NO 6.2. Accept: stage 2 unit. Test: the list equals NO 5:158's names.
- **K410** It stores `portal_object_ids` per state, `active` and `archived`.
  - Src: BP:146; A§7.3:522. Accept: stage 2 unit (synthetic reads). Test: the fixture's Portals under their states. See W16.
- **K411** `build_targets_by_strand` holds each strand's workspace and folder ids, with the record's targets as their union and the client's workspaces as the ceiling.
  - Src: BP:146; A§7.3:523 and :524. Accept: stage 2 unit. Test: the union of entries is a subset of `client_workspace_ids`. See W38.
- **K412** The `lease` mirror in `guard_index` (strand, epoch, label, heartbeat) is left exactly as the lease primitives wrote it.
  - Src: BP:146; BP:135; A§7.3:525. Accept: stage 2 unit. Test: as K36 for `native-map` and `classify`.
- **K413** `record_provenance` holds the coverage of the read and a staleness budget in days.
  - Src: BP:146; A§7.3:526; NO 6.2. Accept: stage 2 unit. Test: both keys present. See W90.
- **K414** Inside a client's own CRM or Service workspace the native set is detected after creation, and an empty set is reported as "product boards not installed here", never as "no natives".
  - Src: BP:146; A§11.5:1095 (D26). Accept: stage 2 unit (synthetic reads). Test: a read of an empty client CRM workspace gives the first wording. See W89.
- **K415** In the user's own account the sweep covers the whole account for natives, while the build itself reads and writes only the client's workspaces.
  - Src: A§11.2:1065; AM:83. Accept: stage 2 unit. Test: a native outside the client's workspaces is recorded in the index and is not a build target.
- **K416** The native map and the guard index are record level, written once per record per staleness window and read by every strand.
  - Src: A§11.2:1065; BP:135. Accept: stage 2 unit. Test: a second `native-map` call for another strand replaces rather than duplicates.
- **K417** The user confirms the map before it is used, always for anything below high confidence.
  - Src: A§11.2:1065; NO 5:158. Accept: stage 2 unit. Test: an unconfirmed entry is reported as unconfirmed. See W88, which sets this against K403.

### 2.26 The select-not-filter query rule (BP:147)

- **K418** A multi-board query selects reserved column ids and never filters on them.
  - Src: BP:147; G-83; A§11.1:1058. Accept: stage 2 unit. Test: scan the detection query of NO 2.6 and every query text `ledger.py` holds or emits for a reserved id inside a filter or `query_params`; none found. See W78.
- **K419** The detection query reads the column list unfiltered, because a type filter on `unsupported` returns nothing.
  - Src: NO 2.6; G-99. Accept: stage 2 unit. Test: the query text has `columns { id type }` with no type filter for the signature read.
- **K420** Every page's requested ids are diffed against its returned ids.
  - Src: NO 2.6:57; G-92. Accept: stage 2 unit (synthetic reads). Test: as K380.
- **K421** The query pages in batches of 25 to 50 with an explicit limit.
  - Src: NO 2.6:57; G-92. Accept: stage 2 unit. Test: as K254.
- **K422** The one `boards` query shape of NO 2.6 is used unchanged for every run.
  - Src: NO 2.6:36. Accept: stage 2 unit (inspection). Test: the text the script holds equals NO 2.6's query.

### 2.27 The synthetic reads themselves (A29)

The reads under `tests/fixtures/snapshots/` are built from the findings in `shared/`, from monday's published schema for 2026-10 (PLAN Q3 (a)) and, for the agent, Vibe and workflow shapes, from `ai-offerings-findings.md` (PLAN Q2 (a)). Nothing here reads or writes a live account.

- **K423** Every reads file opens with a `fixture` header object holding `synthetic: true`, `ring_modelled`, `schema_source`, `sources`, `built`, `confirmed_by_capture` and `id_rule`.
  - Src: AM:12; PLAN §4.1. Accept: stage 2 unit. Test: the fixture self-test loads every reads file and checks the seven keys.
- **K424** Every reads file is marked synthetic, and `confirmed_by_capture` is `null` until a scrubbed capture has been compared with it at A11-1.
  - Src: AM:10 to 14; BP:17 (A11-1). Accept: stage 2 unit; capture (A11-1). Test: no file carries `synthetic: false` or a non-null `confirmed_by_capture` in this package.
- **K425** `ring_modelled` names the ring whose shapes the file follows, `release_candidate 2026-10`.
  - Src: AM:14; PLAN §4.1; NO (intro). Accept: stage 2 unit. Test: the field's value.
- **K426** The header's `sources` names the `shared/` sections and gotcha ids the file follows, and every board names the section or gotcha it models.
  - Src: AM:14; PLAN §4.1. Accept: stage 2 unit. Test: the self-test finds a `models` entry on every board of the answer key and a `sources` entry in every header.
- **K427** Every page records `requested_ids`, `returned_ids` and `missing_ids`.
  - Src: G-92; PLAN §4.1. Accept: stage 2 unit. Test: the self-test checks the three lists on every page and that `missing_ids` is requested minus returned.
- **K428** The pages have the shape the query of NO 2.6 returns, so that a scrubbed capture can take a synthetic page's place one for one and be compared shape for shape.
  - Src: AM:13 and :14; PLAN §4.1; NO 2.6. Accept: stage 2 unit (inspection); capture (A11-1). Test: every field of a page is in the query's field list.
- **K429** Every board, workspace, view, item, user and object id in a reads file is invented, in one documented range per type that overlaps nothing in monday's template catalogue.
  - Src: AM:14; PLAN §4.1; NO 3.1 and 3.2. Accept: stage 2 unit. Test: the self-test checks every id against its type's range and against the template lists.
- **K430** The template ids and template view ids a fixture uses are monday's own constants from NO 3.1, 3.2, 4.1, 4.2 and 7.2, the one class of long numeric id a tested file may carry.
  - Src: NO (intro); PLAN §4.1. Accept: stage 2 unit. Test: every long numeric id in the files is in a documented range or in those lists.
- **K431** No id from any account enters a file; ids are strings.
  - Src: AM:14; HANDOFF non-negotiables; GO G-92. Accept: stage 2 unit. Test: the self-test fails any id outside the ranges and constants, and any numeric id.
- **K432** Every name in a fixture is a neutral invented word, with no person, firm, account or workspace of any real kind.
  - Src: AM:14; PLAN §4.1. Accept: stage 2 unit (inspection). Test: the self-test checks names against a list of allowed stems; a reviewer reads the files.
- **K433** The answer keys sit in files of their own, `identification.expected.json` and `native.expected.json`, holding for each board the class, the rule id, the N12 attributes, the confidence and `models`, and the totals per class.
  - Src: PLAN §4.1; BP:141. Accept: stage 2 unit. Test: the self-test checks the five fields per board and that the totals add up to the board count.
- **K434** A `schema-fields.json` lists the published-schema types and fields the reads use, with the source and the date read, and every field a read carries is in it.
  - Src: AM:11; PLAN §4.1; PLAN Q3 (a). Accept: stage 2 unit. Test: every field in every page is listed. See W03.
- **K435** The agent, Vibe app and workflow shapes follow `ai-offerings-findings.md` and are marked synthetic.
  - Src: PLAN Q2 (a); PLAN §4.3; AI:10, :35, :55. Accept: stage 2 unit. Test: the fixtures' `sources` name that file; a reviewer checks each AI shape against it. See W03.
- **K436** A fixture self-test in `test_snapshots.py` passes: every reads file marked synthetic with its ring and sources; the totals per class add up to the board count; every id invented in its range or a monday catalogue id; every field in the schema field list; every board names the section or gotcha it models.
  - Src: PLAN step 4. Accept: stage 2 unit; Windows run; macOS run. Test: the test passes on both systems.
- **K437** A `.gitattributes` keeps every file under `tests/fixtures/snapshots/` LF on both systems.
  - Src: PLAN §4.1; A§5.3:342. Accept: stage 2 unit; Windows run. Test: no `\r` in any fixture file after a checkout on Windows.
- **K438** The compare fixtures hold before and after snapshot pairs with a description change, an archived board, a changed column digest, an owner change, a moved agent `version_id`, a moved agent state and a moved workflow state, beside controls that must not flag, a protected live-map row that moved before the before snapshot, and an appendix holding a mutation, a subscription, a two-operation document, a clean query, and the word "mutation" inside a string and a comment.
  - Src: PLAN §4.2; BP:140; A§9.7:928. Accept: stage 2 unit. Test: the self-test lists each case in the answer key and `compare` finds it.
- **K439** The reconcile fixtures hold a live inventory in the shape of A§8.11 (boards with `created_at`, folders, docs, automations per board, dashboards by stored id, the agent, Vibe and workflow lists) and the strand ledger state it is reconciled against, so that each of the seven classes arises, and a sibling strand for the classify-only run.
  - Src: PLAN §4.2; A§8.11:835 and :837. Accept: stage 2 unit. Test: every class is expected at least once; `reconcile` reproduces the key. See W70.
- **K440** The identification fixture covers R0 to R11 and C1 to C4 and every state.
  - Src: PLAN §4.2; BP:141. Accept: stage 2 unit. Test: the answer key names a board for each rule and each state.
- **K441** The native fixture covers CRM v2 and core v1 with each entity, companions, Quotes & Invoices with its line items, Products & Services, Service families A to D with subitems and a satellite, the Portal active and archived, lineage at 0, 1 and 2 hops and one ending unreadable, a chain-broken native, a template view id alone, blank defaults and suffixed ids, the SLA mark, two look-alikes, a renamed native, an ordinary board linking into a native, ordinary boards in a product workspace and in a test workspace, a native moved into a core workspace, the boards the identification rules own, a deleted native, the two known limits, and a page on which `boards(ids:)` drops an id.
  - Src: PLAN §4.2; BP:141 to 146. Accept: stage 2 unit. Test: the answer key names a board for each.
- **K442** A trace check of the reads is done before the read side is built: each expected class is read against NO 5 and the gotcha cited, without reading any code, and every disagreement is settled by the author of the reads.
  - Src: PLAN §5 Q4 (a); PLAN step 4b. Accept: stage 2 unit (inspection). Test: `fixture-check.md` exists and lists no unsettled disagreement.
- **K443** The reads and the answer keys are separate files, so a capture can replace a reads file without touching its key.
  - Src: PLAN §8.5. Accept: stage 2 unit (inspection). Test: no answer appears in a reads file.
- **K444** The package makes no live read and no live write, and its tests open no network connection.
  - Src: BP:17; AM:10 to 14; AM:173 to 177 (A11). Accept: stage 2 unit. Test: the three test files run with the network module blocked.
- **K445** Every classify, compare and reconcile clause is marked in the checklist "met against synthetic reads"; the capture and the comparison of synthetic against captured shapes join the A11-1 moment.
  - Src: AM:14; PLAN §4.3. Accept: capture (A11-1). Test: the checklist's status column for those clauses; the capture itself waits for the workspace the user names.
- **K446** The fixture's id rule and neutral names are enforced by its own self-test until the agnostic sweep exists.
  - Src: PLAN §8.6; PLAN §7.18. Accept: stage 2 unit. Test: K429 to K432 pass without `tools/agnostic_sweep.py`. See W05.
- **K447** The reads are the specification until a capture exists: a shape the synthetic read does not model is not graded.
  - Src: AM:14; PLAN §4.3. Accept: stage 2 unit (inspection). Test: the checklist lists what the synthetic reads cannot prove (that monday returns these shapes today, that nothing moved since the ring, anything the findings never observed).

### 2.28 The headless halves (BP:149)

H23, H24, H25 and H26 are covered by K285, K311, K339 and K367. The clauses below cover the ledger halves of the three rows WP3 proves for others and the sharing rule.

- **K448** The three-part fence refusal of H35 passes headless: a ledger write carrying the old epoch, or the new epoch with the old session label or the old run id, is refused with the reason.
  - Src: BP:149; BP:504. Accept: stage 4 headless H35. Test: the row passes on seed record r13 once WP14's runner exists. See W04.
- **K449** The `do-not-change` refusal of H39 passes headless: an element targeting the `do-not-change` row is refused, and the `change-with-own-yes` target is planned as `other-strand-modified` with `prior_state`.
  - Src: BP:149; BP:508. Accept: stage 4 headless H39. Test: the row passes on seed record r13. See W04.
- **K450** The estimate half of H39 passes headless: `estimate --strand` shows the other strand's approved-but-unbuilt calls, and that strand's `readiness.md`, `blueprint.md` and `build.json` are never read by the session.
  - Src: BP:508; BP:138. Accept: stage 4 headless H39. Test: the row passes; the grader finds no read of the sibling's files. See W68.
- **K451** The scope refusal of H58 passes headless: a ledger `intent` naming a workspace outside the client's is refused with the rule quoted.
  - Src: BP:149; BP:527. Accept: stage 4 headless H58. Test: the row passes on seed record r14.
- **K452** The same element inside the client's workspaces passes every ledger check.
  - Src: BP:527. Accept: stage 4 headless H58. Test: the row passes on seed record r14.
- **K453** H24 to H26 are WP3's rows and WP10 cites them: the scenarios are shared, the files are not, and WP3 adds no WP10 file.
  - Src: BP:149; BP:384. Accept: stage 2 unit (inspection). Test: no file under `skills/solution-audit/` or `skills/monday-drift-check/` is changed by WP3.
- **K454** The checklist lists every headless row WP3 owes and the seed records and runner each needs, as owed to stage 4 and not as failed.
  - Src: PLAN §7.19; BP:149. Accept: stage 2 unit (inspection). Test: the list is in the checklist.

---

## 3. Shapes

Each shape is copied from the source that gives it. Where A§ and RM differ, a field list per block is marked **both**, **A§ only** or **RM only**; the template files under `tests/unit/fixtures/plugin/templates/record/` follow RM. Section 4 lists each difference (W06 and the entries it points to). Nothing here picks a side.

### 3.1 `account/1`, `account.json` (A§7.3:488 to 538; RM:119)

Key order: A§'s example puts `updated_at` last; RM and the WP2 template put it third, after `client_slug`. Key order is kept as found (G11).

| Block | Fields | Marking |
|---|---|---|
| top level | `schema` (`"account/1"`), `client_slug`, `updated_at`; then the blocks below | both |
| `account` | `id`, `slug`, `name`, `kind` (`own` or `client` or `sandbox`), `build_target` (`own-account` or `client-account` or `none`), `tier`, `bound_user_id`, `bound_at`, `builder_role`, `products[]` of `{id, kind}` with kind `core`, `crm` or `service`; every field `"unbound"` in the template | both |
| `client_workspaces` | per product `core`, `crm`, `service`: `{id, name, created_in}` (`created_in` is a qualified version such as `001/v0.1`); `{}` before any | both |
| `api` | `connector_ring`, `execute_code_ring`, `read_at`. A§'s example gives `execute_code_ring` as `"2026-10 (pinned)"`; RM says both rings are `"<kind> <version>"` strings such as `"release_candidate 2026-10"` | both (format differs) |
| `change_check` | `at`, `for_strand`, `ring`, `versions_seen[]`, `release_notes_since` (`"<date> (read)"` or `"not-read"`), `roster_diff {added, removed, renamed}`, `schema_diff[]`, `approved_by_user` (null or a log reference); the outcome field is `result` in A§ and `verdict` in RM | both, except the outcome field (A§ `result`, RM `verdict`) |
| `native_map` | `crm.<entity>`, `service.<entity>`, `portfolio.<key>`, each `{board_id, rule, confidence, signals[], lineage {chain[], resolved, note}, confirmed_by_user}`; `rule` is one of `N0`, `N1a`, `N1b`, `N2` to `N11`, `R0` to `R11`, `C1` to `C4` (`N12` records attributes beside them); `confidence` is `high`, `medium` or `low` | both |
| `native_map` (more) | `family` on a Service entity; `projects[]` of `{tasks_board_id, overview_board_id, overview_state, planner_board_id, folder_id, connected}` on a portfolio; nothing below `high` is ever `confirmed_by_user: true` | RM only |
| `guard_index` | `captured_at`, `ring`, `product_workspaces {workspace id: kind}`, `account_products[]` of `{id, kind, default_workspace_id}`, `native_board_index {board id: "product/entity"}`, `native_board_ids_by_entity`, `template_source_ids[]`, `unreadable_intermediate_ids[]`, `template_view_ids[]`, `reserved_column_ids {entity: {ids[], threshold}, blank_default_exclusions[]}`, `native_default_names_and_terminology[]`, `portal_object_ids {active[], archived[]}`, `client_workspace_ids[]`, `build_targets_by_strand {short id: {workspace_ids[], folder_ids[]}}`, `lease {strand, epoch, session_label, heartbeat_at}` (written by the lease primitives only), `record_provenance {coverage, staleness_budget_days}` | both |
| `guard_index` (BP) | BP:146 lists `template_source_ids` "including the unreadable intermediates", where A§ and RM keep `unreadable_intermediate_ids` as a field of its own (W18) | BP differs |
| `live_objects` | keyed by qualified element key: `monday_id`, `kind`, `name_at_build`, `owner_strand`, `introduced_in`, `state`, `constraint`, `constraint_source`, `digest`, `last_verified`, `dependants[]` | both |
| `live_objects` (more) | `workspace` | A§ only |
| `prior_builds[]` | `{strand, closed, summary}` | both |

### 3.2 `build/2`, `strands/<id>/solution/build.json` (A§7.3:540 to 580; RM:123)

| Block | Fields | Marking |
|---|---|---|
| top level | `schema` (`"build/2"`), `client_slug`, `strand`, `account_ref` (`"../../../account.json"`), `account_id_at_bind`, `lease_epoch_at_run`, `reads_live[]` (qualified keys), `updated_at` | both |
| `approvals[]` | `version`, `qualified_version`, `revision`, `frozen_file`, `sha256`, `approved_at`, `approved_words`, `approved_in_session`, `element_count`, `irreversible_listed[]`, `automations_listed[]`, `live_objects_touched[]` of `{key, constraint}` | both |
| `approvals[]` (more) | `approval_mode` (`own-account-poc` or `per-list`), `workflows_listed[]`, `agents_listed[]`, `sequences_listed[]`, `rests_on {clearance, purpose, assumptions, assumed_terms, forks_on_leaning}` | A§ only |
| `preflight` | `at`, `version`, `daily_total`, `used_today`, `client_reserve`, `estimated_calls [low, high]`, `roster_ok`, `stale_gotchas[]`, `findings[]` | both |
| `preflight` (more) | `workspaces_ok` | A§ only |
| `runs[]` | `id` (`run-YYYY-MM-DD-N`), `version`, `kind`, `session_label`, `lease_epoch`, `started_at`, `heartbeat_at`, `ended_at`, `state`, `calls_estimated`, `calls_used`, `account_checks[]` of `{at, before, result}` | both |
| `runs[]` (more) | `another_build_running` (the answer to the one question) | A§ only |
| `runs[]` (more) | `reconcile {at, mode, classes}`, written by `reconcile --classify-only`; `kind` is `build` or `doc-copy`; `state` is `running`, `ended` or `interrupted` | RM only |
| `objects{}` | keyed by bare element key: `type`, `id`, `name`, `parent_key`, `parent_id`, `origin`, `source_strand`, `introduced_in`, `changed_in[]`, `state`, `status`, `attempt {run_id, started_at, intent_digest}`, `verify {read, at, result, digest, note}`, `creator_user_id`, `owner_user_ids[]`, `irreversible`, `sample_data`, `approval_ref`, `notifies[]`, `companions {}`, `role`, `prior_state`, `blueprint_ref` | both |
| `objects{}` (more) | `workspace`, `workspace_scope[]`, `assumption_refs[]`, `prompt_ref`, `version_id_at_build` | A§ only |
| `objects{}` (more) | `url`; `companions` limited to `subitems_board_id`, `doc_container_board_id`, `form_board_id`, `overview_board_id`, `planner_board_id` | RM only |
| `irreversible_yes[]` | `key`, `what`, `at`, `log_ref` | both |
| `irreversible_yes[]` (more) | `mode` (`card` shown), `approval_ref` | A§ only |
| `departures[]` | `key`, `version`, `what`, `error_code`, `attempts[]`, `decision` | both |
| `ui_steps[]` | `key`, `what`, `owner`, `target_version`, `status` (`open` or `done`) | both |

Values: `status` moves `planned` to `attempting` to `written` to `verified` or `mismatch`, and from any state to `departed` or `removed`; `verify.result` is `match`, `mismatch`, `not-checkable` or `needs-user`; `origin` is `created`, `pre-existing-modified`, `pre-existing-referenced` or `other-strand-modified`. Forms of reference: a frozen element is `v0.1r4#B1` inside the strand's ledger, `001/v0.1r4` and `001:B1` elsewhere (RM:77). A run id is `run-YYYY-MM-DD-N` (RM:123).

### 3.3 The `lock/2` fields the fence reads

The full shape is RM:138 to 142 and G02, and is WP2's; `ledger.py` never reads the file itself (K35). The fence, `mmb_common.lease_fence(root, epoch, session_label, run_id)`, returns `(ok, reason)` from a read under the mutex and passes only when:

- `state` is `held` and the lock's shape is sound;
- `epoch` equals the presented epoch (compared as text);
- `session_label` equals the presented label, which is non-empty;
- `run_id` is not `null` (a run has started under this lease) and equals the presented run id.

It moves `heartbeat_at` (lock and the `account.json` mirror, no backup) in the same hold when it passes. `lease_refresh(root, epoch, session_label, run_id)` enters the run id once, only while the lock's `run_id` is `null` and never a run id an earlier lease carried. `lease_release(root, epoch, session_label)` sets `state` `released`. The session label has the form `YYYYMMDD-HHMM-xxxx` (G01), the heartbeat is stale after 3,600 seconds (G40), timestamps in the lock are UTC (`YYYY-MM-DDTHH:MM:SSZ`), and the epoch is an integer that rises by one on every take and every break (RM:138).

### 3.4 The JSON envelope and the exit codes (G10; API:7 to 18)

```text
every command but a status read:
  {"ok": <true unless the exit code is 1>, "command": "<name>", ...payload}
a refusal (exit 1):         "refusals": [{"file", "field", "problem", "expected"}, ...]
a could-not-run (exit 3):   "error":    {"file", "field", "problem", "expected"}
an error after a commit:    "error": {"field": "committed", ...}, plus a top-level "committed": {...}
file: record-relative, POSIX spelling; a whole-file error names the field "(whole file)"; a mutex timeout names "record.mutex"
```

| Exit | When |
|---|---|
| 0 | the command did its work with nothing to report |
| 1 | a refusal of any kind; `check` with a blocking finding |
| 2 | the command did its work, or `check` ran, and only warnings remain |
| 3 | could not run: missing or unreadable record or file, malformed JSON, mutex timeout, a fence that could not run, usage error, unknown subcommand, unexpected exception |

### 3.5 The rules of NO 5, by id and class name

Conditions are in NO 5:129 to 156 and are not copied here. A rule that fires gives the class on its row.

| Rule | Class | Rule | Class |
|---|---|---|---|
| R0 | none (page until empty; every state) | N5 | `native_<product>_<entity>_subitems` |
| R1 | `doc_container` | N6 | `native_crm_companion_board` (moderate) |
| R2 | `subitems_board` | N7 | `native_service_satellite_probable` (review only) |
| R3 | `workflow_object` or `custom_object_other` | N8 | `lookalike_board` |
| R4 | `portfolio_board` | N9 | `ordinary_board_in_product_workspace` |
| R5 | `project_tasks_board`, `converted_project_board` or `project_board_origin_unknown` | N10 | `native_descendant_misplaced` (review) |
| R6 | `project_overview_companion` | N11 | `ordinary_board` (handed back to R8 to R11) |
| R7 | `keyed_board_unrecognized_key` (stop and review) | N12 | attributes beside the class, never the class |
| N0 | none (context only; product kind is a soft gate) | R8 | `resource_planner_companion` |
| N1a | `native_service_portal` (definitive) | R9 | `portfolio_shaped_board_without_key` (review) |
| N1b | `native_service_portal` (strong) | R10 | `multi_level_board_not_project` |
| N2 | `native_<product>_<entity>` (`direct_install` at 0 hops, else `descendant_copy(n)`) | R11 | `normal_classic_board` |
| N3 | `native_<product>_<entity>` (`direct_install`) | C1 to C4 | connection proof from both halves of a portfolio link; one half is `partial link - review`; folder evidence never counts (NO 7.3; which number is which is W80) |
| N4 | `native_<product>_<entity>` (`descendant_fingerprint` when lineage is `UNRESOLVED` or `NO_LINEAGE`) | | |

Lineage results: `RESOLVED_TEMPLATE`, `NO_LINEAGE`, `UNRESOLVED` (NO 2.1). Install kinds: `direct_install`, `descendant_copy(n)`, `descendant_fingerprint`, `lineage_unresolved` (NO 5:152). Corroborating marks: `CRM_RELATION_MARK`, `CRM_FEATURE_MARK`, `CRM_MIRROR_MARK`, `V2_OPPS_FINGERPRINT`, `SERVICE_SLA_MARK`, `PORTAL_MARK` (NO 2.4).

### 3.6 The seven reconcile classes and the `reconcile` object

The classes, with the hyphenated tokens of G04 and RM:123 and the prose forms of A§8.11:835 and SF 9: `adopt`, `retry`, `duplicate`, `partial`, `changed-since-verified`, `unrecorded-extra` (prose: unrecorded extra), `missing`.

The object `reconcile --classify-only` writes onto the interrupted run (G04, RM:123):

```json
"reconcile": {
  "at": "<UTC, YYYY-MM-DDTHH:MM:SSZ>",
  "mode": "classify-only",
  "classes": {"adopt": 0, "retry": 0, "duplicate": 0, "partial": 0,
              "changed-since-verified": 0, "unrecorded-extra": 0, "missing": 0}
}
```

`record.py lease break` reads it under five conditions (G04): the holder's run whose `id` is the lock's `run_id` is `interrupted`, carries this object, and `at` is later than the lock's `heartbeat_at`; park is refused when `duplicate` or `partial` is above zero.

### 3.7 The compare items of A§9.7 (A§9.7:928)

A snapshot covers: the strand ledger's sha256 and `account.json`'s; the inventory (`boards(workspace_ids, state: all)` with id, name, type, state, description, `updated_at`, folder, kind); per in-scope board a digest of columns (id, title, type, revision, settings), groups, view settings, owners and subscribers; automations (id, active, `updated_at`); forms through `get_form`; doc block counts; dashboards by stored id; and for round two agents (plan digest, state, `version_id`, triggers, grants), workflows (the `objects` read with state) and Vibe apps (status, `is_published`, code version). In scope: the strand's own boards plus every live-map row marked `do-not-change` or `change-with-own-yes`.

BP:140 names six changes `compare` flags: a description change, an archived board, a changed column digest, an owner change, an agent whose `version_id` or state moved, a workflow whose state moved. A§8.7:810 and A§9.7 name more (a changed digest, state, description, plan text or active flag; activity entries by the connected user). W75 lists the difference.

### 3.8 The element keys and the `objects[].type` vocabulary (A§7.3:582)

| Key | Type | Key | Type |
|---|---|---|---|
| `W1` | `workspace` | `A1` | `automation` |
| `F1` | `folder` | `PF1` | `portfolio` |
| `B1` | `board` | `PJ1` | `project` |
| `B1.G2` | `group` | `WF1` | `workflow` |
| `B1.C3` | `column` | `AG1` | `agent` |
| `B1.V1` | `view` | `B1.AI1` | `ai_column` |
| `B1.FM1` | `form` | `VB1` | `vibe_app` |
| `B1.SUB` | `subitems` | `SQ1` | `sequence` |
| `D1` | `doc` | `WH1` | `webhook` |
| `DB1` | `dashboard` | `WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT` | a publication or activation, listed as its own irreversible step (no `type` of its own: W11) |
| `DB1.W2` | `widget` | `U1` | a UI step (a `ui_steps[]` key, not an object) |

Inside a strand's own ledger and blueprint the keys are bare; anywhere else they are qualified (`001:B1`). The live map's `kind` column spells the AI kinds as words with spaces in A§7.8:697 ("AI column", "Vibe app") and says only "any kind of the element-key list" in RM:134 (W59).

---

## 4. Gaps and contradictions

Each entry is something the sources leave unspecified or state two ways, so a coder would have to decide. Nothing here is resolved. Each gives the readings with their anchors and the clauses it touches. Entries are grouped by theme; the numbers are stable ids and not an order of importance. Section 5 maps the entries of `PLAN.md` section 7 to them, with the result of re-checking each anchor.

### Test inputs and what they are held to

- **W01 Recorded reads that do not exist (PLAN §7.1).** A§11:1040 says `tests/fixtures/snapshots/` holds the native run and the identification run with zero misclassified; BP:101 (the WP1 inputs line) and BP:130 (the WP3 inputs line, with a re-capture of any read older than the current ring) rely on them. `tests/fixtures/` holds only `.gitkeep`; there is no `snapshots/` folder. AM:10 to 14 (A29) says synthetic reads first, a scrubbed capture later. Reading one: the three design lines stand and the reads are owed as recordings. Reading two: A29 supersedes all three, and they read as synthetic reads with the ring they model until the capture. PLAN §4 and the answers of 2026-10-16 take the second; the three design touch-ups are owed. Touches K423 to K447.
- **W02 The AI kinds in stage 2 or stage 4b (PLAN §7.11).** BP:68 says stage 4b exists because the AI offerings are additions to files WP3 and others own, and BP:137 labels the AI-kind rows "stage 4b"; BP:128 gives WP3 the ledger rows and approval classes for the AI kinds, and BP:140, BP:492 (H23) and BP:493 (H24) ask for agents, Vibe apps and workflows in `compare` and `reconcile` now. PLAN Q2 (a) builds all of it in stage 2. Open: the words "stage 4b" in BP:137 stay as written, and what stage 4b still adds (PLAN says only what new probes change) is not listed. Touches K158 to K169, K174, K276, K296 to K298.
- **W03 Sources for the agent, Vibe and workflow shapes (PLAN §7.11).** AM:12 names the `shared/` findings and monday's published schema. `shared/monday-gotchas.md` ends at G-108; A§10.5:1032 and BP:101 expect entries for agents, Vibe apps and workflows (G-110 to G-139) and none exist; RB:53 says no read is named for these kinds. The connector's agent, Vibe and workflow tools are not GraphQL, so the published schema does not describe them; the only source is `ai-offerings-findings.md` (AI), which lives under `rebuild-workspace/design/`, not `shared/`. Separately, G-69 (line 227) says published workflows are out of v1 and SF 4:66 excludes published workflows, CRM sequences and webhooks from v1 builds, against AM:104 to 110 (A18) and A§9.4:891 to 895, which bring them in. Reading one: the findings file is the source and the stale lines are stale. Reading two: the stage-1 files are checked first. Touches K160, K197, K434, K435.
- **W04 The headless rows need stage 4 (PLAN §7.19).** H23 to H26 and the ledger halves of H35, H39 and H58 (BP:149) need WP14's runner (BP:468 to 470) and the seed records r13 and r14 (BP:504, BP:527), which do not exist. They are owed later, as WP2's were. Touches K285, K311, K339, K367, K448 to K454.
- **W05 `tools/agnostic_sweep.py` does not exist (PLAN §7.18).** `tools/` holds `lint_plugin.py`, `README.md` and `.gitkeep`; BP:70 puts the sweep in WP16, stage 2, and A§5.4:362 describes it. Until it exists the fixture's own self-test enforces the id rule. Touches K446.

### Shapes: record map against architecture

- **W06 `account/1` and `build/2` in `record-map.md` lag A§7.3 (PLAN §7.2).** RM:123 has no `approval_mode`, `rests_on`, `workflows_listed`, `agents_listed` or `sequences_listed` on an approval, no `mode` or `approval_ref` on an `irreversible_yes` row, no `assumption_refs`, `workspace`, `workspace_scope`, `prompt_ref` or `version_id_at_build` on an object, no `workspaces_ok` in `preflight` and no `another_build_running` on a run; RM:119 has no `workspace` on a `live_objects` row. A§7.3:551 to 575 carries them all. Also: RM adds `url` on an object, `reconcile` on a run, `family` and `projects[]` on `native_map` and the run `kind` and `state` vocabularies, none of which A§ shows; A§'s example `api.execute_code_ring` is `"2026-10 (pinned)"` where RM says `"<kind> <version>"`; A§ puts `updated_at` last and RM third; the WP2 template and fixture follow RM, so a `check` that requires A§'s fields fails the fixture. Reading one: A§ wins by the authority order and the record-map edit is owed (PLAN step 3). Reading two: the new fields are optional on entries written before the edit. Touches K69, K235, K248.
- **W07 When `approval_ref` is required (PLAN §7.3).** RM:123: an irreversible, automation or removed row. A§5.4:356: an irreversible, list or removed row. BP:135: an irreversible, list-approved, publication or removed row. A§7.3:582 adds that an `other-strand-modified` row needs `approval_ref` "exactly as `pre-existing-modified` does", which leaves open whether a `pre-existing-modified` row needs one. PLAN §7.3 reads the widest, BP's. Touches K123 to K126, K130, K241.
- **W08 `change_check.result` against `verdict` (PLAN §7.4).** A§7.3:502 calls the outcome field `result` (example text "no change affecting this build"); RM:119 and the WP2 template call it `verdict`. Neither gives a vocabulary. Touches K88, K94.
- **W09 The approval-mode vocabulary is not pinned.** BP:137 says every `approval_ref` names its approval mode "as `record-map.md` pins it", and RM has no `approval_mode` and no mode values. A§7.3:582 gives `approval_mode` `own-account-poc` or `per-list`, and `mode: card` on an `irreversible_yes` row under the first; it names no `mode` value for a row whose yes was taken at execution (per-list), and does not say whether the `approval_ref` string itself carries the mode or only resolves to an entry that does. PLAN §8.10 puts the ledger vocabulary under a `Pinned:` heading. Touches K72, K78, K79, K160.
- **W10 The approval class of each kind.** BP:137 gives each row kind "its approval class from `safety.md`". SF 4 has IR-01 to IR-15 for irreversible operations and SF 5 for automations; it has no row for a workflow, an agent activation, a sequence, a webhook or an AI column, only IR-15 for a Vibe publication, and SF 4:66 excludes several of them. A§9.4:877 to 896 lists them with no ids. The ledger has no `class` field: only `irreversible` (a boolean) and the approval's `*_listed` arrays, and AI columns, Vibe apps and webhooks have no list array although A§9.5:904 approves AI columns and Vibe apps "as rows of the same card". SF 4:63 (IR-14) also says "prefer an existing workspace", against AM:83. Reading one: the class is derived from kind and operation by a table pinned in the record map. Reading two: the class is stored on the row. Touches K83, K124, K125, K154.
- **W11 The `objects[].type` vocabulary has holes.** (i) BP:137 and AM:19 want every seeded item row marked `sample_data: true`, and A§7.3:582's twenty types include no `item`; items are rows of `objects` with an unlisted type, or not rows at all (only a per-board or per-batch row), and A§8.6:798 batches writes at 20. (ii) A§7.3:582 lists `WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT` as keys "listed as its own irreversible step", and BP:137 calls them rows with their own `approval_ref`; no `type` names them, so they are rows of `objects` with an unlisted type or only entries of `irreversible_listed` and `irreversible_yes`. (iii) A§7.3:582 says an account-level object carries `workspace_scope` and every other object `workspace`, without saying which kinds are account-level (A21 names agents; BP:136 names an agent, a Vibe app, a webhook and a sequence; a workflow is a workspace object per AI:55). (iv) BP:136 wants a workspace creation recorded with its product and the client it is for, and no object field holds either. Touches K86, K144, K151, K160, K177.
- **W12 `objects[].state` has no vocabulary, and a referenced row has no lifecycle.** A§7.3 shows `active` and `inactive`; A§7.8:700 lists `active`, `archived`, `inactive`, `removed-by-platform` for the live map; RM:134 drops `inactive`; RM:123 gives no list for an object's `state`. A `pre-existing-referenced` row (a native, say) is not created by the build, so the chain `planned` to `written` hardly applies to it. Touches K223, K237.
- **W13 The status chain's edges.** A§7.3:582 gives `planned` to `attempting` to `written` to `verified` or `mismatch`, and any state to `departed` or `removed`, and says other transitions are refused. Not stated: a move out of `mismatch` (A§8.6:799 allows one different call form and a fresh read-back), out of `verified` when a later version changes the object (A§8.9:823, `changed_in[]`), out of `departed` (a "later retry" is a `decision`, A§8.6:799) and out of `removed`; and what `verify.result` `not-checkable` or `needs-user` does to `status`, since the chain ends at `verified` or `mismatch`. Touches K122, K183, K188, K190.
- **W14 The time form of each field.** G40 makes machine timestamps that are compared UTC (`...Z`) and human-facing values local with no zone. A§7.3 shows `bound_at` and `last_verified` as local minutes, `change_check.at` with `Z`, and `"..."` for `approved_at` and the run times; RM:131 shows the live map's `last verified` as a date; WP2's fixture `build.json` writes UTC with `Z` for approvals, runs, `updated_at` and `verify.at`. Which of `bound_at`, `approved_at`, `started_at`, `heartbeat_at`, `ended_at`, `preflight.at`, `verify.at`, `attempt.started_at`, `irreversible_yes.at`, `updated_at`, `last_verified`, `captured_at` and `read_at` is UTC is not stated. Touches K53, K89, K212.
- **W15 Where companions, dashboard sets, widgets and project folders are kept.** RM:123's `companions` has five keys (subitems, doc container, form, overview, planner board ids); A§11.3:1074 and G-72 say to record the tasks board, overview, planner and folder ids "as companions" before connecting, and RM:119's `native_map.portfolio.projects[]` has `tasks_board_id` and `folder_id`. G-90 says the board ids and widget ids sent to a dashboard are "the only record" and no field holds them. Touches K168, K170, K181.
- **W16 `native_map` entity names, and which classes enter which index.** A§7.3:504 keys entities as `crm.leads` and `crm/leads`; NO 3 and 4 name `opportunities_or_deals`, `products_services`, `quotes_invoices`, `qi_line_items`, `sales_targets`, `deals_subitems`, `tickets`, `tickets_subitems`, `incidents`, `csat_survey`, `service_contacts`, `asset_management`, the two employee entities and the Portal. Which classes get a `native_map` entry (natives N1 to N5, companions N6, satellites N7, misplaced N10, portfolio roles R4 to R6, look-alikes N8) and which boards are put in `native_board_index`, the only thing a hook protects by (A§9.10:964; NO 6.5 says protect as native and ask), is not stated; nor is where a Portal found by the lineage fallback is listed in `portal_object_ids`. Touches K401, K404, K410.
- **W17 Where `classify` results go.** A§11.2:1065 puts them in `account.json.native_map` (record level) and in the strand's `objects[].role` "with each board's rule id, signals and confidence"; BP:135 makes `classify` record-level, writing `account.json` only, with `--strand` as a stamp. `objects[].role` is one field with no place for a rule id, signals or confidence, and the boards classified are mostly not the strand's own objects. Touches K38, K368, K401.
- **W18 The `guard_index` list.** BP:146 lists `template_source_ids` "including the unreadable intermediates"; A§7.3:516 and :517, RM:119 and NO 6.2 keep `unreadable_intermediate_ids` as a field of its own. BP:146 also omits `native_board_ids_by_entity`, `native_default_names_and_terminology` and `client_workspace_ids`, which A§ and RM carry. Touches K405, K407, K409.

### Files, writers and the mutex

- **W19 Where snapshots live (PLAN §7.5).** A§8.7:807 puts the before snapshot in `.work/strands/<id>/audit/`; A§7.1:399 and RM:26 list `live/snapshots/<date>-<strand>.json` written by `ledger.py`, archived with the record. A before and an after snapshot of one strand on one date have the same name under the second scheme. Reading one: both, for different jobs. Reading two: one place only. Touches K286, K291.
- **W20 A per-strand `build.json.bak` (PLAN §7.6).** A§7.1:438 and RM:68 list `build.json.bak` among the files under `.work/strands/<id>/`; G39 and the same paragraph of RM:68 keep every backup under `.work/backup/<record-relative path>.<UTC stamp>` and no per-strand backup folder. Touches K11.
- **W21 The log has one writer (PLAN §7.14).** A§8.6:792 puts the one question's answer "in the run entry and the log", A§8.6:800 puts each yes "on the object and in the log", and A§8.6:802 ends a run with "a log entry"; RM:14 and API:25 make `record.py log` (`insert_entries`, which also moves `.work/history.json`) the one writer. `irreversible_yes[].log_ref` (A§7.3:575) names a log entry the ledger did not write. Reading one: the ledger prints the entry text and the skill writes it (PLAN §8.4). Reading two: the ledger calls into `record.py`. Reading three: the ledger writes `log.md` itself. Touches K116, K210.
- **W22 The binding mirror after `bind` (PLAN §7.15).** G15 makes `record.py check` block until `CLIENT.md`'s binding fields (and `client_workspaces`) equal `account.json`; `ledger.py` writes `account.json` only, and `CLIENT.md`'s front matter is engagement's (BP:386). The order of the two writes, and what `check` says between them, are not stated. Touches K60.
- **W23 Who writes the version state at `run end`.** A§9.8:942 says `run end` "sets the version state" and A§8.6:802 says "state `built`"; the ledger writes `account.json` and `build.json` only (BP:135), `version.md` belongs to engagement, build, audit and intake (A§7.1:421), and `record.py` has `version open|mark|condense-*|release` and no state setter (A§5.4:355). Reading one: `run end` writes it, as an exception to the one-writer lines. Reading two: the build skill writes it through the guard. Reading three: `run end` records the run's state only. Touches K116.
- **W24 Fields with no named writer.** The `api` block; `account.tier`, `products[]` and `builder_role` (the one-document query of SF 3 returns the account's id, slug, name, tier and the user, not a role or products); the whole `preflight` block, which A§8.6:795 describes and no catalogue subcommand writes; `reads_live[]`; the `account_checks[]` entries after `run start` (A§8.6:798 and SF 3 want one at every batch of 20 writes and before a create whose parent is not a recorded id); `account_id_at_bind`, `client_slug` and `strand` in a strand's `build.json` (the template holds `unbound` and empty text); `updated_at` in both files. Touches K52, K88, K98, K103.
- **W25 Files outside the three the mutex clause names.** BP:134 names `account.json`, a `build.json` and the lock. `live/live-map.md`, `live/snapshots/*.json` and `.work/strands/<id>/live-inventory.json` are not named. `run end` writes a run entry, the live map, `live_objects` and the lease release "in one step" (BP:135, A§8.6:802): four writes in an order no source gives. WP2's primitives write the lock last (G09 amended). Touches K117, K120.
- **W26 Mutex re-entry (PLAN §7.20).** `mmb_common.record_mutex` is re-entrant within a thread, keyed on the resolved path (MC); WP2 tests re-entry through a second spelling of the path. PLAN asks for a test in one process before anything relies on it. Reading one: rely on the docstring. Reading two: the test comes first. Touches K45.
- **W27 The delta diff has no subcommand.** A§8.9:823 says "`ledger.py` diffs the approved element table against the strand's `build.json`, so unchanged elements keep their ids and only the difference is built"; no subcommand of A§5.4:356 or BP:135 to BP:149 does it. Reading one: `approval` computes it. Reading two: `intent` per element. Reading three: a subcommand outside the catalogue. Touches K69, K71.

### The fence, the run and the lease interplay

- **W28 Which subcommands are behind the fence.** A§5.4:356 and BP:135 say "every account-affecting write"; A§9.10:958 says `intent` presents the three parts; A§9.8:944 says "every approval reply refreshes it too", though an approval comes before any run and the fence passes only inside a run. Candidates: `intent`, `record`, `verify`, `depart`, `irreversible-yes`, `ui-step`, `run heartbeat`, `run end` (whose release takes only epoch and label), `approval`, `workspaces`, `live-map set`, `snapshot`, `compare`, `bind`, `change-check` (A§8.6:792 to 794 puts it after the lease is taken). Touches K104, K113.
- **W29 Where the presented run id comes from.** A§5.4:356 and A§9.8:934 compare the lock's `run_id` with "the run the strand's ledger is in", which reads as a value taken from `build.json`; A§9.8:934 also says a woken old session that re-reads its ledger after a resume-first break would pass an epoch-only fence, so the run must be carried in the session. `mmb_common.lease_fence` takes the run id as an argument; no source names a flag. Touches K107, K112, K136.
- **W30 `run start`'s details.** (a) The form of the one question's answer: free text such as "no, answered 13:31" (A§7.3:561) or a yes and no. (b) What a yes writes and which subcommand releases the lease at once (A§9.8:942; A§8.6:792). (c) How the run id `run-YYYY-MM-DD-N` is minted: local or UTC date, `N` counted per strand or per record. (d) Which `kind` a run takes: RM:123 gives `build` and `doc-copy`, `doc-copy` is deferred (BP:380), and a fix run (A§8.6:812) has no stated kind. (e) Whether a second `running` run is refused (A§8.6:791 says recovery comes first, and the ledger's part is not stated). (f) The source of `calls_estimated`. Touches K98 to K100, K121.
- **W31 `run heartbeat`.** A§5.4:356 lists it; BP:68 says the heartbeat is refreshed "on every write"; BP:135 says the fence moves it. What `run heartbeat` is for beyond that, and whether it also writes `runs[].heartbeat_at` in `build.json` (A§7.3:562) as well as the lock's, is not stated. Touches K114.
- **W32 `run end`'s details.** (a) The release takes epoch and label (MC:lease_release) and the fence also needs the run id: whether `run end` passes the fence first. (b) The run entry's end state: `ended` (RM:123), against "state `built`" (A§8.6:802), which is the version's (W23). (c) The source of `calls_used`. (d) What happens when a row is still `attempting` at the end. Touches K115 to K117.
- **W33 The fields of `committed` for the ledger.** WP2 reports a take, a release, a break and a repair this way (DECISIONS:606); A§7.1:438 says only "naming what is written and what is still to do". The ledger's own cases (the writes of `run end`; `bind` writing `account.json` while the mirror is not yet written) have no stated fields. Touches K50.
- **W34 `--expect-sha`.** A§5.3:345 says it is taken "on every write to `build.json`"; BP:135 lists a stale `--expect-sha` among the refusals without scoping it. The ledger has no read subcommand to give the session the current sha (`record.py guard --file X` prints one, API:46, and that is `record.py`), so a write must return the new sha for the next; whether it also applies to `account.json`; and whether the hash is of the bytes (`mmb_common.sha256_file`) or of normalised text (`sha256_text`; G60 raised the question). Touches K133.
- **W35 Ids as numbers.** Command-line values are text, so a numeric id can arrive only in a JSON input file, in a hand-edited file `check` reads, or in a document handed to `bind`; no source says which routes the ledger accepts. Touches K61, K131.
- **W36 The newer-schema set for the ledger.** G57 has every writing command read the schema of `CLIENT.md`, `log.md`, `account.json`, the lock and each `STRAND.md` and `version.md` it touches; the ledger touches `account.json`, a `build.json`, the lock and `live-map.md` (schema `live-map/1`, known to `mmb_common`). Which files it reads for this is not stated. Touches K12.

### `bind`, `workspaces` and the scope check

- **W37 `bind`'s interface.** The binding document (A§8.2:751; SF 3) arrives as a file, a JSON text or flags, and which fields come from it (it has no role and no product list); the settings keys read are `default_build_account {slug, id}` and `never_show_workspaces[]` (RM:70) and the sandbox file's `kind | account_id | account_slug | workspace_id | label | note` lines, which also carry `never-demo` kinds; a second bind (SF 3: "none may rebind") and a repeat of the same values; how a `sandbox` record (build target `none`) is bound. Touches K52 to K59.
- **W38 `workspaces`' interface, and who writes the target lists.** A§7.3:538 gives `workspaces` the `client_workspaces` entry; the writers of `guard_index.client_workspace_ids`, of each strand's `build_targets_by_strand` entry and of its `folder_ids` are not named: BP:135 has `bind` record "the client's workspaces as they are created", and BP:146 has `native-map` store `build_targets_by_strand` "with the record's targets as their union". Folders (an irreversible row, A§9.4:890) have no subcommand. Reading one: `workspaces` writes all three. Reading two: `native-map` rebuilds the targets. Reading three: `intent` extends a strand's entry when it creates a workspace. Touches K62 to K67, K137, K138, K411.
- **W39 One workspace per product against a new direction (PLAN §7.12).** `client_workspaces` is keyed by product (A§7.3:497, RM:119), so it holds one workspace per product, and A§7.3:538 says a later strand or product "adds an entry rather than reusing"; AM:83 and A§8.9:825 open fresh workspaces for a completely different direction and keep the old ones; BP:136 refuses a second workspace in a product "unless the record says the direction changed" and no field says so. SF 4:63 (IR-14) says "prefer an existing workspace or folder", against AM:83. PLAN §8.13 proposes an additive field and leaves the choice to the decisions step. Touches K66, K145.
- **W40 A board the record cannot place (PLAN §7.16).** BP:136 refuses an account-level reference outside the client's workspaces; a board named in a grant or a trigger may be in no row, no `native_board_index` entry and no live-map row, so it has no recorded workspace. PLAN §8.9 reads: outside, and refused. Touches K139 to K143, K149, K245.
- **W41 The scope input form, and the operational list.** How a write's target workspace, a trigger's board, a knowledge grant (`READ` or `READ_WRITE`, AI:18), a Vibe binding, a webhook board and a sequence board reach `intent` (repeated flags, a payload file) is not stated. The operational list is `never_show_workspaces[]` in `local/settings.json` (RM:70) and `never-demo` lines of the sandbox file (RM:70, which also allow `*` for a whole account); BP:135 says the refusal "sits in `intent` and `workspaces`", yet any workspace outside the client's set is refused already by BP:136, so the list adds a reason only where an operational workspace is also in the client's set. Which list the ledger reads, and whether it reads `local/` at all, is open. Touches K59, K65, K137, K147.

### Approvals

- **W42 `approval`'s interface, and the element table (PLAN §7.10, Q1).** Flags are unstated (frozen file, sha, words, session, mode, lists, counts, touched live objects). PLAN Q1 (a) has WP3 pin an `## Element keys` table (key, kind, name at least) and the place of an agent's prompt text in `record-map.md` as part of `blueprint/1`; its layout is the decisions step's. DECISIONS:630 records why: `blueprint-guide.md` (WP9) does not exist and the fixture's `## Elements` table is the fixture author's layout. `mmb_common.sha256_file` hashes bytes and `sha256_text` hashes line-ending-normalised text (G60 raised the question; `record.py freeze` returns two matching values), and which one `approval` compares is not stated. Who creates the `planned` rows A§7.3:582 starts from, `approval` or the first `intent`, is not stated. Touches K69 to K71, K175, K243.
- **W43 The form of `approval_ref`, and where a list's own yes lives.** The fixture and A§7.3:572 write `v0.1r1` and `v0.2r2`; the entry's own fields are `version`, `qualified_version` (`001/v0.2`) and `revision`. How a ref resolves to an `approvals[]` entry across strands, and where a list's own grouped yes at execution is recorded (A§9.5:906: one grouped reply; `automations_listed` holds the approved list, and no field holds the reply), are not stated. Touches K74, K78, K80, K241.
- **W44 Mode derivation at the edges.** A§7.3:582 and AM:18 give `own-account-poc` for a proof of concept in the user's own account where notifications reach only the user. Not stated: the mode on a `sandbox` record (build target `none`); on a `working-solution` version (`v1.0` and on, AM:53) in the user's own account; and for a revision that mixes lists, since `approval_mode` is one value per approval entry while AM:18 and A§9.5:910 take only a notifying list out of the card's yes. Touches K72, K73, K76.
- **W45 "A real person" (PLAN §7.17).** AM:18 says "notifications reach only the user"; A§9.5:910 says in the user's own account recipients are the user and a row that notifies anyone else takes its list's own yes; PLAN §8.7 reads any recipient other than the bound user. What `notifies[]` holds (user ids, names, team ids, guests, email addresses for a sequence), and what a "client user who agreed" is (A§9.5:910, where sample data is present in a client's account), are not stated. Touches K76, K166, K181.
- **W46 The form of `assumption_refs`.** BP:137 says "from the frozen revision"; the id form of an assumption, an assumed term or a fork is not pinned, and whether each is confirmed or accepted lives in the record, not the ledger (AM:46 to 58; BP:137 "while any of them is not yet confirmed or accepted"). The counts in `rests_on` come from the session. Touches K82, K85.
- **W47 What `intent_digest` is, and how a changed row voids an approval.** A§7.3:568 shows `intent_digest` with no definition. A§9.5:910 says any change to board, trigger, condition, action, recipient, prompt text or scope voids the approval for that row; checking that needs a comparison of the intended write with the frozen row, whose structure is not pinned (W42). Reading one: the ledger checks key, kind and target against the element table only. Reading two: it compares a digest of the intended write with a frozen one. Touches K184.
- **W48 `irreversible-yes`'s interface.** The flags; the numbering the user answers ("yes to 1 and 3, not 2", A§8.6:800) against element keys; how "a yes never carries to another session" is told: `approved_in_session` is free text (A§7.3:551 shows `session-1015-1330`) while the minted label is `YYYYMMDD-HHMM-xxxx` (G01); the containment evidence an archive's yes carries has no field in A§7.3:575 or RM:123; the `mode` of a per-list yes (W09). Touches K79, K210 to K215.

### Change check

- **W49 `change-check`'s interface.** The four reads of A§8.6:794 (the live `version` and `versions`, the release notes and changelog, the schema introspection of the queries and mutations the build sends, the connector roster diff) happen in the session; the script has no monday access, so they arrive as a file or flags. The outcome vocabulary (W08), the log reference in `approved_by_user`, and whether `run start` or `intent` refuses without a change check dated today (A§8.6:794 stops "before any write"; the hook reads "dated today", A§9.10:958; no source gives the ledger a rule) are open. Touches K88 to K95.

### `intent`, `record`, `verify`, `depart`, `ui-step`

- **W50 `intent`'s and `record`'s interfaces.** The flags for key, type, name, parent, origin, workspace or scope, operation (create, update, archive, delete, activate, publish), the target references of W41, a timed-out call, the id returned, `blueprint_ref` and `--expect-sha`. Seeded items (batches of 20, A§9.9:952) may be one row each or one per batch (W11). Touches K151 to K185.
- **W51 `verify`'s interface, and how it learns the read.** The result may arrive as flags (`--result`, `--read`, `--digest`, `--note`) or as a file holding the read. Whether the script compares anything (K191 needs the plan text, K194 the diff) or only records what it is told is open. The digest function is W73. Touches K186 to K201.
- **W52 The agent's `version_id` and the prompt comparison.** BP:137 says the `version_id` is "read after the plan write"; AI:16 says the update reply is stale on the plan, AI:17 that an update can activate, AI:21 that `version_id` changes with the plan and not the state. Which moment it is taken (after the plan read-back, after the deactivate, after triggers and knowledge grants), whether a later plan change in a fix run replaces it (`changed_in[]`), how the frozen prompt text reaches the comparison (a file, a hash, through `prompt_ref` and the Q1 pin), whether the comparison is exact or normalised for line endings (AI:10 returns the plan "in full" as markdown), and whether a prompt hash is kept (A§7.3 has none), are not stated. Touches K174, K175, K191.
- **W53 The Vibe difference and the user's yes.** BP:137 refuses `verified` while the delivered app differs from the request "without the user's yes to the difference". The difference is a reading of code versions and the build conversation (AI:41, AI:48) made by the session; the script can only require a recorded yes, and no field holds it or the difference text (`verify.note` is the nearest). The source of the request text is the frozen spec. Touches K194.
- **W54 Poll ceilings per asynchronous kind.** A§8.6:798 says "a poll with a stated ceiling". G-71: boards appear 6 to 35 seconds after creation, "give it at least a minute"; A§11.1:1056: "at least a minute before failing"; AI:40: a Vibe app is `READY` about a minute later; A§11.3:1079: roll-ups fill within about 45 seconds; G-73: a key settles in about 40 seconds. No source gives a ceiling per kind, nor says whether it lives in the ledger or in `build-loop.md` (WP9); K256 needs a poll count per kind. Touches K172, K256.
- **W55 `depart`'s and `ui-step`'s interfaces.** The `decision` vocabulary (A§8.6:799: a UI step, a blueprint revision or a later retry; A§7.3:576 shows "UI step U3"); the form of `attempts[]` (A§7.3:576 shows `flat`, `wrapped`); who numbers `U` keys (A§7.3:582 calls `U1` a UI step among the blueprint's stable ids, while a step that arises at build has no blueprint key); the owner vocabulary; who sets `done`; how an unprobed AI kind's UI step (A§8.6:797) is created, by `depart` or by `ui-step`; the link between a departure and its UI step. Touches K202 to K209.
- **W56 `removed`, archive and containment.** A§7.3:582 has status `removed`; A§9.4:896 and :900 say v1 sends no delete and archives instead; an archive sets an object `state` of `archived` (A§7.8:700) and the sources do not say whether it also sets status `removed`. BP:135 and A§5.4:356 require an `approval_ref` on a removed row. The containment evidence an archive shows (A§8.6:800) has no field. Touches K126, K215.
- **W57 `read-back.md` lags A§10.4.** RB:53 says no read is named for agents, AI columns and Vibe apps; A§10.4:1028 names the reads for agent, Vibe app and workflow and says AI column, sequence and webhook stay `not-checkable`; A§7.3:569 carries an agent's `verify.read`. BP:137 sends each row to its read-back in `read-back.md`. Touches K163, K192, K197, K198.
- **W58 Parent keys across strands.** RM:77 makes a bare key valid inside the strand's own ledger and a qualified key valid elsewhere; a second strand's board whose workspace was built by the first (AM:83, A§8.9:823) has a parent in another strand's `build.json`, which a session never reads (A§7.1:434). Whether such a parent is resolved through `live_objects` (`001:W1`) is not stated. Touches K132, K179.

### The live map

- **W59 The live map's fields and states.** A§7.8:693 to 704 has columns including `workspace`, `built by`, `last verified`; RM:129 to 131's header has no `workspace`; `live_objects` carries `name_at_build`, `owner_strand`, `introduced_in`, `digest` and more, yet the two are "mirrored field for field". `inactive` is a state in A§7.8:700 and not in RM:134. The AI kinds are "AI column" and "Vibe app" in A§7.8:697 and `ai_column` and `vibe_app` as types. `last verified` is a date in RM:131 and a minute in A§7.3:531. The grouping by strand the map takes at its 250-line and 16 KB budget (A§7.1:398) has no form. Touches K217 to K225.
- **W60 Which rows `run end` writes.** A§7.8:706 says workspaces are rows, and that native and other pre-existing objects appear with `built by: client` or `native`; `run end` creates rows for verified objects, so the subcommand that creates native and client rows is not named. Not stated: rows for groups, columns, views, seeded items, `pre-existing-referenced` objects, departed and removed objects. Touches K119, K226.
- **W61 `run end` against promoted constraints.** A§7.8:718 has `run end` create a row at the interim value; it does not say what a later run's `run end` does to a row that exists (refresh digest, `last_verified` and dependants and keep the constraint, or reset). Touches K232.
- **W62 `live-map set`'s interface and ownership.** A§7.8:708 says a strand must not edit a live-map row it did not build; BP:135 makes `live-map set` record-level with `--strand` as a stamp only. Whether a strand's close may set only that strand's rows (A§8.10:829) is a check no source assigns; several rows in one call are not mentioned. Touches K227 to K230.

### `check`

- **W63 What `ledger.py check` validates.** A§7.1:390 and :417 say the files "must pass `ledger.py check`" and A§8.6:790 runs it at the guard; no source lists its checks. `record.py check` already blocks on `account_id_at_bind` mismatch, a live-map and `live_objects` disagreement and a build target outside the client's workspaces (BP:123, G47). Whether `ledger.py check` repeats those, and whether a stale native index (A§5.4:355), a stale lease or a change check older than today are its warnings, is open. Touches K234 to K249.

### `estimate`

- **W64 `estimate`'s interface and inputs.** The flags; the inputs not in the ledger: the plan's allowance for automation actions, each automation's action estimate, the account's daily total and today's usage (read from `platform_api` in preflight, A§8.6:795), the client reserve (a 14-day median scaled, A§9.9:952), and the count of items and updates (from the element table or from seeded rows). Where the result is stored (`preflight.estimated_calls`, `runs[].calls_estimated`, nowhere) is not stated. Touches K250 to K264.
- **W65 The cost figures.** The figures are 25,000 to 90,000 complexity per page of 7 to 17 boards (NO 2.6:57), about 167,000 for one `items_page` page, and a budget of "about 20M" (NO 2.6:57) or "the per-minute complexity allowance" (A§9.9:952), whose unit and period are not stated. No source gives a cost per board or a formula for a page of 25 to 50. Preflight about 12 calls, one read-back per settings-bearing write or batch and about 3 calls per board of audit are the only per-component counts; there is no table of calls per element kind. Touches K252, K253, K256.
- **W66 The staleness window.** A§9.9:952 and A§11.2:1065 say "once per record per staleness window". `record_provenance.staleness_budget_days` (7 in the template) and NO 6.3 R-J (the guard asks when `captured_at` is past it) are the only stated budget. Whether the estimate's window is the same budget, where `captured_at` comes from, and what "paid" means when the window is current (zero for every strand) are not stated. Touches K261, K413.
- **W67 What "approved-but-unbuilt" counts.** Which strands are "open" (`state` `active`; a `paused` one?); which version counts (an approval with no ended run?); `approvals[]` holds `element_count` and no estimate, while `preflight.estimated_calls` is one pair per strand written at preflight (A§8.6:795), so a strand approved and not yet preflighted has no figure; a strand part-way through a run may count its remainder. Touches K257.
- **W68 `estimate` against H39 (PLAN §7.13).** BP:138 has `estimate --strand` report other open strands' approved-but-unbuilt estimates; BP:508 (H39) says strand 001's `build.json` is never read by the session; A§7.1:434 and A§9.9:952 say the same of any other strand's `build.json`. PLAN §8.8 reads: the script reads the sibling's approvals and prints totals only. Touches K258, K450.
- **W69 The AI-powered set.** BP:138 and AM:117 (A17) say the estimate names which elements are AI-powered so the user can price them: agents, AI columns and Vibe apps are named by A17; whether a workflow or a sequence is (A18) depends on whether it holds an AI block, which an element row's `type` does not say. Touches K262.

### `reconcile` and the digest

- **W70 The live inventory's shape, and how the session hands it (PLAN §7.9).** A§8.11:835 names the reads and the file `.work/strands/<id>/live-inventory.json` and pins no shape: boards with `type`, `state` and `created_at`; folders; docs; `list_automations` per board; dashboards by stored id; the agent, Vibe and workflow lists (AI:10, :35, :55). The key a live object is matched on is not stated. Touches K265, K278, K439.
- **W71 The operational test per reconcile class (PLAN §7.9).** The sources give prose for `adopt` (A§8.11:835: exactly one live match under the recorded parent or scope, created after the attempt started), `unrecorded-extra` (never adopted if it predates the attempt) and `duplicate` (the user chooses; the extra becomes an archive or deactivation proposal); `retry`, `partial`, `changed-since-verified` (which needs a digest, W73) and `missing` have no test. "A match" per kind is not stated (a board by name, type and parent; an automation by stored title, which is the request text cut at about 60 characters, SF 5, and its trigger; an agent by name; a Vibe app by name and binding; a workflow by name; a dashboard by stored id; a widget, which no read returns, not at all). "Created after the attempt started" needs `created_at`, which some reads lack. The lost-reply rules (A§8.11:835: a lost `create_automation` reply always needs the user's re-confirmation; a lost agent `update` reply needs a `get`; a lost `publish_workflow` reply needs the `objects` read) have no stated place in the output. Touches K267 to K277.
- **W72 What `reconcile` writes, and under what authority.** (a) BP:139 has `--classify-only` write the classes "as findings" and as the run's `reconcile` object; `runs[].reconcile.classes` holds counts only (G04), and `build.json` has no findings array of its own (`preflight.findings[]` is the preflight's). (b) A full `reconcile --strand` is described as classifying "so the user approves the plan" (A§8.11:835); what it writes, and the `mode` value of a full run (RM:123 gives `classify-only` only), are not stated. (c) The classify-only run is made from a sibling's session that holds no lease for the holder's strand, so no fence applies; `reconcile` is not in the record-level list, so `--strand` names the target and not a stamp. (d) A lock with no run id, a holder run already `interrupted`, and a second classify-only call are not mentioned. Touches K279 to K284.
- **W73 What a digest is.** `verify.digest` (`ag1:9a1b...`, `b1:7c0e...` in A§7.3), `live_objects.digest`, the "column digest" of compare (id, title, type, revision, settings; A§9.7:928) and the agent's "plan digest" have no definition of the function, the canonical form of its input, its prefix or its length (the fixture shows eight hex digits), nor of who computes it (the script from a handed read, or the session). Touches K201, K271, K294.

### `snapshot` and `compare`

- **W74 `snapshot`'s shape and interface (PLAN §7.9).** There is no file shape; the name `<date>-<strand>.json` collides for a before and an after snapshot (W19); the input is a file or flags; how scope is applied (trim or refuse); what `compare` is given (two paths, two labels); where the "before" digest of a protected row comes from when the row moved before the before snapshot (A§9.7:928). Touches K286 to K289.
- **W75 The compare scope.** BP:140 names six things `compare` flags. A§9.7:928's snapshot also holds automations (id, active, `updated_at`), forms, doc block counts, dashboards, Vibe apps (status, `is_published`, code version), view settings, subscribers, an agent's plan digest, triggers and grants; A§8.7:810 marks an audit `write-detected` on "any changed digest, state, description, plan text or active flag". The activity-log and tool-call checks are not the ledger's. Reading one: `compare` flags exactly BP's six. Reading two: it flags every difference between the snapshots. Touches K292 to K299.
- **W76 `compare`'s output, exit code and writes.** Whether flags make exit 1, 2 or 0 with a list; BP:135 names `compare` among the record-level writers of `account.json` and no source says what it writes there; the `write-detected` verdict is the audit's (A§8.7:810) and the ledger gives findings; the output's grouping of changes inside the window and changes outside this strand. Touches K300, K310.
- **W77 The tokenizer's scope.** The "small tokenizer" (A§9.7:928) must handle string literals, block strings, comments, punctuators and names; count top-level operations including the anonymous `{ ... }` form; treat fragment definitions (not operations), `extend` and schema definitions, directives and variables definitions; and say what a syntax error does (refuse, which fails closed, or pass). The documents appendix's format in `audit.md` (how documents are delimited, which are GraphQL, and whether `execute_code` JavaScript or a variables object can appear) is not pinned. Touches K303 to K308.

### `classify` and `native-map`

- **W78 `classify` consumes reads; it does not run the query.** A§11.2:1065 says "`ledger.py classify` runs one query per page and applies both rule sets"; a script has no monday access (A§5.3:340; A§5.4:355 leaves the connector to the session). NO 2.6 gives the query for the session to send. So `classify` takes response pages: as which files or paths, in which format, and with what handling of the lineage walk, which needs reads of each hop's board (`boards(ids:)`) that no single page holds. Reading one: the session hands every hop's reads. Reading two: `classify` prints the next ids to fetch and is called again. R0's "page until empty" is the session's loop. BP:147's rule is a property of the query text, which is in NO 2.6 (a WP1 file) unless `ledger.py` emits queries. Touches K290, K312, K313, K371, K418, K422.
- **W79 R3 needs the workflow objects set (PLAN §7.8).** NO 5:134 reads "the workflow `objects()` set"; NO 2.6's query has `objects` aliases only for the Portal; NO 7.2:194 says the workflow object's template lineage "is also reported on blank boards, so never decisive alone". Reading one: the query gains a workflow-objects alias (an edit to a WP1 file). Reading two: R3 is read from fields it has (type, lineage, default columns; G-69). Touches K317, K422.
- **W80 C1 to C4 are named, not defined (PLAN §7.7).** NO 7.3 and A§11.3:1076 describe "both halves" as `C1` and `C2` and the folder exclusion as `C4`; G-78 agrees; `C3` is never described. PLAN's reading (connected, one half only, neither, folder evidence) is an inference. The rows of a portfolio's link need its items page, and NO 2.6's query "fetches no items", so the connection rules need a read the query does not carry (and a cursor rule, NO 7.3). Touches K332 to K336.
- **W81 The rule order against the type gates.** NO 5:127, A§11:1040 and A§11.2:1065 put R1 to R3 (type gates) and R4 to R7 (key gates) before N0 to N11. N1 is for a `custom_object` (the Portal) and N5 for a subitems board, the two types R3 and R2 classify first (`workflow_object` or `custom_object_other`; `subitems_board`). Reading one: N1 and N5 pre-empt R3 and R2 for the boards they match. Reading two: R2 and R3 win and N1 and N5 never fire. Reading three: R3's `custom_object_other` is replaced when N1 fires. Touches K316, K317, K342, K346, K355.
- **W82 How many N rules.** BP:141 and A§11:1040 say N0 to N12; NO 5:127 and A§11.2:1065 say N0 to N11 with N12 as attributes; N1 has two ids, N1a and N1b (RM:119). Touches K340 to K353.
- **W83 The class vocabulary, and how a limit or a review is shown.** `native_<product>_<entity>` has product tokens (`crm`, `service`), entity names (W16) and a `_subitems` suffix, and no closed list; the identification classes are closed (section 3.5). How the two known limits (BP:145), the review classes (`N7`, `N10`, `R7`, `R9`, a partial link) and the "not installed here" report are shown in the output is not stated. Touches K343, K353, K396 to K399.
- **W84 Threshold ties and family choice.** Ids shared across entities (`contact_account` and `account_contact`, `contact_deal`, `account_deal`) can meet two thresholds on one board; no tie rule is given. The v1 or v2 family is picked by "reading the type" (NO 2.3) and the Service family A to D by extended ids and lineage, with no procedure. Touches K345, K369, K389.
- **W85 Confidence.** `high`, `medium` or `low` per result: NO 5 calls N1a definitive, N1b strong, N6 moderate, and A§11.1:1048 says reserved ids stand alone; A§7.3:508 shows `high` for an N4 on a dead-end chain. No mapping from rule and signals to level is given. Touches K368, K402, K403.
- **W86 Lineage edge cases.** A cycle; the result when the fifth hop is not terminal (`UNRESOLVED`, or its own value); the hop count's definition; and whether `source_view_id` is walked like lineage (NO 2.2 and G-95: "walk a non-template value like a lineage pointer"), which needs reads of other boards' views, while BP:142 speaks of lineage only. Touches K378, K385.
- **W87 Where the catalogue constants live.** The script embeds the template ids, template view ids, reserved ids, thresholds and names of NO 3 to 5, or it reads `shared/native-objects.md` at run time (the plugin folder is a per-session copy and readable); PLAN §8.10 adds a pinned vocabulary and a lint tuple, and a drift test between document and script is not described for the catalogues. `guard_index.template_source_ids` is a per-account copy, so a constant and a preflight read must be told apart. Touches K370, K407 to K409.
- **W88 Confirmation of a map entry below high confidence.** RM:119 says nothing below `high` is ever `confirmed_by_user: true`, and BP:146 says `native-map` refuses to mark it confirmed. A§11.2:1065 and NO 5:158 say the user confirms the map before it is used, "always for anything below high confidence"; NO 8 (P-9, P-16) defaults to confidence plus the user's confirmation and to "protect as native and ask". Reading one: a below-high entry is never confirmed and is only protected. Reading two: the user's review of it is recorded in a field other than `confirmed_by_user`. Touches K403, K417.
- **W89 `classify` and `native-map`, and the "not installed here" report.** BP:135 lists both as record-level writers; BP:146 has `native-map` record signals and confidence and store `guard_index`; A§11.2:1065 says "results ... go into `account.json.native_map`". Whether `classify` prints and `native-map` stores, or each stores; what `native-map` is handed; where "product boards not installed here" (A§11.5:1095, BP:146) is reported and under which conditions (a workspace in `client_workspace_ids`, product `crm` or `service`, an empty native set). Touches K400, K404, K414.
- **W90 Provenance fields.** `record_provenance.coverage` is free text in A§7.3:526 (the example reads "workspaces read: all of the client's; natives swept account-wide, pages 1-5"); `captured_at` and `ring` come from the reads (the query returns `version { kind value }`); `staleness_budget_days` is 7 in the template and its source is not stated; a synthetic read's `captured_at` is its fixture's `built`. Touches K413.

### The CLI frame

- **W91 The record locator and global flags.** `--record` before the command and the current folder as the default (API:9) are WP2's choices, not sources for the ledger; two-word commands (`run start`, `live-map set`) have no stated parser form beyond `lease take` in WP2. Touches K20 to K23.
- **W92 What the `--strand` stamp is.** BP:135 and A§5.4:356 say record-level subcommands take `--strand` "only to stamp who asked". Only `change_check.for_strand` is a field; no field exists for `bind`, `workspaces`, `native-map`, `classify`, `snapshot`, `compare`, `live-map` or `live-map set`. The stamp may go in the output only, in a log entry (W21), or in a new field. Touches K38, K233.

---

## 5. Coverage

### 5.1 Every sentence of BP:126 to 151, and the clauses that cover it

Quotes are cut to fifteen words or fewer.

| BP line | Sentence (quoted) | Clauses |
|---|---|---|
| 128 | "gains the ledger rows and approval classes for the AI kinds" | K151 to K185 |
| 128 | "the build-target binding and the workspace scope check (A17, A18, A21)" | K54, K55 to K57, K137 to K150 |
| 128 | "the approval modes and the `assumption_refs` and `sample_data` fields (A25, A28)" | K72 to K87 |
| 128 | "and tests on Windows and macOS (A24)" | K17, K18 |
| 128 | "Leaves the v1 acceptance: `gql_guard.py` (D7, A2)" | K308 (the tokenizer lives in `ledger.py`) |
| 129 | "`scripts/ledger.py`, `tests/unit/test_ledger.py`, `tests/fixtures/snapshots/`" | K13, K423 to K441 |
| 130 | "A§7.3, A§8.6, A§8.11, A§9.7, A§9.9, A§11; A1, A17, A18, A21, A24, A25, A28" | K69 to K121 (A§7.3, A§8.6), K265 to K285 (A§8.11), K286 to K311 (A§9.7), K250 to K264 (A§9.9), K312 to K422 (A§11) |
| 130 | "the recorded reads behind the two classification fixtures, with the ring each read was taken on" | K423 to K428 (read as synthetic reads, A29; W01) |
| 134 | "`sys.dont_write_bytecode = True` is the first statement after `import sys`" | K03, K04 |
| 134 | "the same first line holds for every shipped script that imports a sibling" | K03 (this script only; the other scripts are their packages') |
| 134 | "Every read and write of `account.json`, a `build.json` and the lock" | K41, K42, K43, K44, K45, K46, K47 |
| 134 | "two-space indent, LF, a final newline, key order kept" | K07, K08, K09 |
| 134 | "When a step after a committed change fails, `ledger.py` reports it" | K48, K49, K50, K51 |
| 135 | "The only writer of `account.json` (`account/1`, record level)" | K32 |
| 135 | "and of every strand's `solution/build.json` (`build/2`)" | K33 |
| 135 | "with the one stated exception of `account.json.guard_index.lease`" | K32, K36, K37 |
| 135 | "take `--strand` only to stamp who asked, every other subcommand takes `--strand`" | K38, K39, K40 |
| 135 | "`bind` writes `account.json.account` from the binding document, with `bound_at`" | K52, K53 |
| 135 | "records the build target ... and the client's workspaces as they are created" | K54, K62, K63, K64, K66, K67, K68 |
| 135 | "refuses a sandbox account on a client record and the reverse" | K55, K56 |
| 135 | "binds an own-account record only to the default build-target account" | K57, K58 |
| 135 | "the operational workspaces are a never-demo list, not bind targets" | K59, K65, K147 |
| 135 | "Refuses a disallowed status transition" | K122, K183 |
| 135 | "a missing `approval_ref` on an irreversible, list-approved, publication or removed row" | K123, K124, K125, K126 |
| 135 | "a `prior_state` on anything but `pre-existing-modified` or `other-strand-modified`" | K127, K128 |
| 135 | "an `other-strand-modified` row whose target the live map marks `do-not-change`" | K129, K130, K244 |
| 135 | "an id stored as a number" | K131 |
| 135 | "an unresolvable parent key" | K132 |
| 135 | "a stale `--expect-sha`" | K133 |
| 135 | "any account-affecting write whose `--lease-epoch` or `--session-label` differs" | K134, K135, K105, K106 |
| 135 | "or whose run is not the lock's `run_id`" | K136, K107 |
| 135 | "the three-part fence that stops a woken dead session" | K104 to K112 |
| 135 | "`run start` stamps the epoch into the strand's ledger" | K97 |
| 135 | "records the answer to the one question" | K98, K99, K100 |
| 135 | "refreshes the lease with its run id before any fenced write" | K96, K101, K102 |
| 135 | "every account-affecting write calls `mmb_common.lease_fence` first" | K104, K110, K113 |
| 135 | "a fence that cannot run ... is a stop, never a skip" | K111 |
| 135 | "`run end` releases the lease" | K115, K120 |
| 135 | "never by writing the lock file directly, and `ledger.py` never parses the lock itself" | K34, K35 |
| 135 | "`run end` also writes the strand's verified objects into `live/live-map.md`" | K117, K219, K220 |
| 135 | "at the interim constraint `change-with-own-yes` with source `pending strand close`" | K118 |
| 135 | "a row is created only for an object a read-back verified" | K119 |
| 135 | "`live-map set --key --constraint --source` sets one row's constraint and source" | K227, K228, K229, K230, K231, K232 |
| 136 | "refuses any write whose target workspace is outside the strand's entry" | K137, K138 |
| 136 | "it refuses any reference outside the client's workspaces" | K139, K140, K141, K142, K143 |
| 136 | "a workspace creation is recorded as irreversible with its product and the client" | K144 |
| 136 | "a second workspace in the same product for the same client is refused" | K145 |
| 136 | "A unit test proves the refusal on a planted write into a sibling client's workspace" | K146 |
| 136 | "and into an operational workspace, and the pass on the client's own" | K147, K148, K149, K150 |
| 137 | "the ledger carries one row kind per element kind the blueprint may plan" | K151, K152, K153, K155 to K159, K161, K164, K166 to K171 |
| 137 | "each with its approval class from `safety.md`, its read-back from `read-back.md`" | K154, K163, K192, K197, K198, K199 |
| 137 | "its asynchronous handling where creation returns no handle" | K164, K170, K172 |
| 137 | "for an agent the `version_id` read after the plan write" | K174 |
| 137 | "a Vibe publication and a workflow publication are rows of their own" | K160, K165, K125 |
| 137 | "every `approval_ref` names its approval mode as `record-map.md` pins it" | K78, K79 |
| 137 | "the card's one yes is a valid `approval_ref` for every list, irreversible and publication row" | K73, K77 |
| 137 | "a row whose `approval_ref` is only the card's yes is refused" | K74, K75, K76 |
| 137 | "lists them in `assumption_refs` from the frozen revision" | K85 |
| 137 | "every seeded item row carries `sample_data: true`" | K86 |
| 137 | "`verify` refuses to mark an agent verified while its plan read differs" | K191 |
| 137 | "refuses to mark a Vibe app verified while the delivered app differs from the request" | K194 |
| 138 | "counts batches correctly (items at 20, updates at 40)" | K250, K251 |
| 138 | "includes the classification query cost as both calls and complexity" | K252, K253, K254 |
| 138 | "counts the automation monthly action estimate against the plan allowance" | K255 |
| 138 | "reports the other open strands' approved-but-unbuilt estimates beside its own" | K257, K258, K259 |
| 138 | "paid once per record per staleness window, never once per strand" | K261 |
| 138 | "names which planned elements are AI-powered and states no credit figure" | K262, K263 |
| 139 | "produces all seven classes from a recorded live inventory, automations listed first" | K265 to K278 |
| 139 | "writes the classes into the holder's ledger as findings" | K279, K283 |
| 139 | "the interrupted run's `reconcile` object (`at`, `mode: classify-only`, `classes`)" | K280, K284 |
| 139 | "with the run marked `interrupted`" | K281 |
| 139 | "adopts, retries and archives nothing" | K282 |
| 140 | "flags a description change, an archived board, a changed column digest, an owner change" | K292, K293, K294, K295, K299 |
| 140 | "an agent whose `version_id` or state moved, and a workflow whose state moved" | K296, K297, K298 |
| 140 | "from the recorded snapshots, **offline**" | K286 to K291 |
| 140 | "refuses any document that carries a mutation or subscription operation or more than one operation" | K303, K304, K305, K306, K307 |
| 140 | "the small tokenizer living here rather than in a script of its own" | K308 |
| 140 | "with a unit test on planted documents" | K309 |
| 141 | "`classify` reproduces **both** rule sets from the recorded reads" | K312, K337, K365 |
| 141 | "rules R0 to R11 and connection rules C1 to C4 over every board with zero misclassified" | K313 to K328, K332 to K337 |
| 141 | "zero \"normal\" results for keyed boards" | K329 |
| 141 | "the converted project separated from the created one" | K330 |
| 141 | "the multi-level non-project board not read as a project" | K331 |
| 141 | "rules N0 to N12 over every board with zero misclassified across every class the rule set names" | K340 to K355, K365 |
| 141 | "CRM natives and descendants, Service natives and descendants including Portals, from-scratch look-alikes" | K356, K357, K358, K359 |
| 141 | "ordinary boards inside product workspaces, ordinary boards in a test workspace" | K360, K361 |
| 141 | "the boards the identification ruleset owns rather than the native one" | K362, K363 |
| 141 | "The fixture states its own totals per class" | K338, K366, K433 |
| 142 | "Lineage is walked hop by hop to a terminal id, not read once" | K371, K375, K376, K378 |
| 142 | "a 0-hop direct install, a 1-hop duplicate and a 2-hop copy of a copy all resolve" | K372, K373, K374 |
| 142 | "an unreadable intermediate ends the chain as `UNRESOLVED` rather than as \"not native\"" | K377, K379, K380, K381, K382 |
| 143 | "Reserved-id signatures stand alone where the chain breaks" | K383, K384, K385 |
| 143 | "blank-board defaults (`person`, `status`, `date4`, `date0`) are excluded from every signature" | K386 |
| 143 | "a randomly suffixed id never disqualifies a board and never counts toward one" | K387, K388 |
| 144 | "Both look-alikes are caught by N8 and neither is caught by name" | K391, K392, K395 |
| 144 | "a renamed native with changed item terminology is still classified native" | K393 |
| 144 | "the board that merely links into a native stays ordinary" | K394 |
| 145 | "planted reserved ids inside a product workspace classify the same as a chain-broken native" | K396 |
| 145 | "a native stripped of its template columns with a broken chain reads as ordinary or as a look-alike" | K397 |
| 145 | "The two known limits are reproduced as limits, not as passes" | K398, K399 |
| 145 | "Both are reported with their reason rather than resolved." | K396, K397, K398 |
| 146 | "`native-map` records signals and confidence per entity" | K400, K401, K402 |
| 146 | "refuses to mark anything below high confidence as confirmed" | K403, K417 |
| 146 | "stores in `account.json.guard_index` the flat `native_board_index` keyed by board id" | K404 to K410 |
| 146 | "`build_targets_by_strand` with the record's targets as their union" | K411, K67 |
| 146 | "the `lease` mirror with strand and epoch" | K412 |
| 146 | "`record_provenance` with a staleness budget" | K413 |
| 146 | "an empty set is reported as \"product boards not installed here\"" | K414, K415, K416 |
| 147 | "A multi-board query **selects** reserved column ids and never filters on them" | K418, K419, K420, K421, K422 |
| 148 | "on the first, every list, irreversible and publication row passes on the card's one yes" | K73, K77, K81 |
| 148 | "a list row without its own yes and an irreversible row without its own yes ... are both refused" | K74, K75, K81 |
| 148 | "a row on a list that notifies a real person in either account" | K76, K81 |
| 148 | "`assumption_refs` and `sample_data` survive `record`, `verify` and `run end` unchanged" | K87 |
| 148 | "Tests run on Windows and macOS (A24)" | K17, K18 |
| 149 | "Headless **H23 to H26** pass" | K285, K311, K339, K367 |
| 149 | "the ledger halves of **H35** (the three-part fence refusal, the classify-only reconcile)" | K448, K285, K105 to K107 |
| 149 | "and **H39** (the `do-not-change` refusal)" | K449, K450, K129 |
| 149 | "the ledger half of **H58** (the scope refusal)" | K451, K452, K150 |
| 149 | "the scenarios are shared, the files are not" | K453, K454 |
| 151 | "**Size:** 700 lines; tests 700." | K19 |

### 5.2 The WP2 carry-overs and the other constraints of PLAN §1

| Item | What WP3 owes | Clauses |
|---|---|---|
| C129, the key half (DECISIONS:630) | resolve the key half of `v0.1r4#B1`; probe `v0.1r1#B9` blocks and `v0.1r1#B1` passes | K243, K71, K175, K176 |
| G09 amended (DECISIONS:606) | every read and write of `account.json`, a `build.json` and the lock inside the mutex; a failure after a commit exits 3 with `committed` | K41 to K51 |
| G51 amended (DECISIONS:604) | `run start` refreshes with its run id; every account-affecting write calls `lease_fence` first, which moves the heartbeat; a fence that cannot run is a stop | K96, K102, K104, K109, K110, K111, K112 |
| G49 | `sys.dont_write_bytecode = True` as the first statement after `import sys` | K03, K04 |
| G11 | two-space indent, `ensure_ascii=False`, LF, final newline, key order kept; read with `utf-8-sig` | K07, K08, K09 |
| G15 | `bind` writes `bound_at` and `build_target`, `kind` one of `own`, `client`, `sandbox` | K52, K53, K54, K60 |
| G01 | `session_label` is the key; a minted label form | K106, K112, K135 |
| G04 | the `reconcile {at, mode, classes}` object, hyphenated class names | K266, K280, K284 |
| G10 | exit codes and the JSON envelope | K20 to K31 |
| G39 | backups under `.work/backup/` | K11 (W20) |
| G40 | time format | K89, K212, K280 (W14) |
| G47 | `client_workspace_ids` is the set writes are refused outside of | K64, K67, K137, K245 |
| G50 | a run id enters only through the refresh, only while the lock's is `null` | K96, K102 |
| G57 | a newer schema refuses writes | K12 |
| PLAN Q1 (a) | the element-key table and the prompt's place pinned in `blueprint/1` | K71, K175, K243 (W42) |
| PLAN Q2 (a) | all AI kinds in stage 2, `ai-offerings-findings.md` a source | K151 to K185, K435 (W02, W03) |
| PLAN Q3 (a) | monday's public schema for 2026-10, no account | K434 |
| PLAN Q4 (a) | the review of the write path, and the trace check of the reads | K442 |
| PLAN §8 nods 1 to 13 | three test files; variants built in setup; own CLI frame; no log write; separate answer keys; invented id ranges; "real person" reading; estimate reads siblings; unplaceable board refused; pinned vocabulary; two agents side by side; Windows first; new-direction field | K13, K14, K15, K258, K443, K429, K76, K149, K72 (W21, W39, W45, W68; nods 10 to 12 are process, not clauses) |

### 5.3 PLAN §7, and the gap that carries each entry

Each anchor of PLAN §7 was re-checked against the source line it cites. All hold, with the corrections noted.

| PLAN §7 | Subject | Gap | Check of the anchors |
|---|---|---|---|
| 1 | recorded reads that do not exist | W01 | A§11:1040, BP:101 and BP:130 hold. Correction: `tests/fixtures/` holds only `.gitkeep`; the `snapshots/` folder itself does not exist |
| 2 | `build/2` in the record map lags A§7.3 | W06 | RM:123 and A§7.3:551 to 575 hold; W06 adds the RM-only fields and the `live_objects.workspace` gap PLAN does not list |
| 3 | when `approval_ref` is required | W07 | RM:123, A§5.4:356 and BP:135 hold; W07 adds the `pre-existing-modified` ambiguity of A§7.3:582 |
| 4 | `change_check.result` against `verdict` | W08 | A§7.3:502 and RM:119 hold; the WP2 template also says `verdict` |
| 5 | where snapshots live | W19 | A§8.7:807, A§7.1:399 and RM:26 hold; W19 adds the same-day name collision |
| 6 | a per-strand `build.json.bak` | W20 | A§7.1:438, RM:68 and G39 hold |
| 7 | C1 to C4 | W80 | NO 7.3 and A§11.3:1076 hold; G-78 names `C1`, `C2` and `C4` too |
| 8 | R3 needs the workflow objects set | W79 | NO 5:134 and NO 7.2:194 hold |
| 9 | no pinned shape for the live inventory or a snapshot; the seven classes are prose | W70, W71, W74 | A§8.11:835 holds; SF 9 repeats the prose |
| 10 | blueprint element keys are unpinned | W42 | DECISIONS:630 holds; PLAN Q1 (a) is answered, and the table's layout is the decisions step's |
| 11 | AI kinds in stage 2 or 4b; A29's sources | W02, W03 | BP:68, BP:137, BP:140, BP:492 and BP:493 hold; W03 adds the missing G-110 to G-139 and the stale G-69 and SF 4:66 |
| 12 | one workspace per product against a new direction | W39 | A§7.3:497, AM:83, A§8.9:825 and BP:136 hold; W39 adds SF 4:63 (IR-14) |
| 13 | `estimate` against H39 | W68 | BP:138 and BP:508 hold |
| 14 | the log has one writer | W21 | A§8.6:792 and :802 hold; W21 adds A§8.6:800 and `log_ref` |
| 15 | the binding mirror after `bind` | W22 | G15 and BP:386 hold |
| 16 | the scope check needs each board's workspace | W40 | BP:136 holds |
| 17 | "a real person" | W45 | BP:137, BP:148 and AM:18 hold |
| 18 | `tools/agnostic_sweep.py` does not exist | W05 | `tools/` holds `lint_plugin.py`, `README.md` and `.gitkeep` |
| 19 | the headless rows need stage 4 | W04 | BP:468 to 470, BP:504, BP:527 hold |
| 20 | mutex re-entry | W26 | the `record_mutex` docstring holds |

### 5.4 Totals

Clauses: K01 to K454, 454 in all. Gaps: W01 to W92, 92 in all.
