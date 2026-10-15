# WP2 contract checklist: `mmb_common.py` and `record.py`

Date: 2026-10-14. Internal build file: never client-facing.

This file turns the acceptance of work package WP2 into numbered, separately testable clauses, copies the shapes the code must honour, and lists what the sources leave open or state two ways. It decides nothing. A builder ticks each clause by one test or one inspection; a reviewer reads section 4 before writing code, because every entry there is a choice the sources do not make.

## 1. Header: sources and how to read this file

### Sources

| Short | File | What was read |
|---|---|---|
| BP | `rebuild-workspace/design/BUILD-PLAN.md` | WP2 block (lines 118 to 124, the Acceptance paragraph is line 123), the passages it points to: section 0 A11 rules (lines 11 to 24), stage notes (62 to 70), WP3 scope notes (134), WP7 acceptance for `init` (198), WP9 lease step (248), WP12 close-out (296), file ownership (364 to 384), seed records and broken records (448), headless rows H19 to H22, H27, H35 to H37, H57, H66 (486 to 533), release checks (584 to 594) |
| A§ | `rebuild-workspace/design/ARCHITECTURE.md` | sections 5.2 to 5.4, 7.1, 7.2, 7.4, 7.6, 7.7, 9.8, plus 7.3 (the `guard_index.lease` block only), 7.8, 7.9, 8.2, 8.8 and 8.10 where the WP2 text points at them. Cited as `A§section:line` |
| RM | `monday-master-builder/plugins/monday-master-builder/shared/record-map.md` | whole file. Cited as `RM:line`. It is the stage-1 text and has not yet taken the A24 to A28 additions (BP:98), so it disagrees with A§ in places; every such place is in section 4 |
| AM | `rebuild-workspace/design/AMENDMENTS.md` | A24 (lines 34 to 38), A25 (40 to 51), A26 (24 to 32), including each "Answered 2026-10-14" line, plus A21, A22, A27, A28 where WP2 names them |
| 1b | `rebuild-workspace/design/stage-1b/PLAN.md` | the D-numbered decisions. BP cites D8, D10, D11, D12, D21, D25 for WP2 but defines none of them in its own text; their definitions are at 1b:31 (D8), 1b:33 (D10), 1b:34 (D11), 1b:35 (D12), 1b:44 (D21), 1b:48 (D25). They predate A22 to A28 and are used here only as pointers |

Authority order (BP:5): AMENDMENTS over ARCHITECTURE over BUILD-PLAN. `record-map.md` is a WP1 file that gains the A24 to A28 additions in stage 2 before WP2 builds against it (BP:98); until it does, where RM and A§ differ, section 4 lists both.

### How to read a clause

Each clause is one requirement. The line under it gives:

- **Src**: where it comes from, as BP line, A§ section and line, RM line, AM line.
- **Accept**: when it is accepted. The vocabulary is fixed:
  - `stage 2 unit`: a unit test or an inspection against `tests/unit/fixtures/`, with the Windows side simulated (for example `PureWindowsPath`, CRLF copies of the fixture tree, an injected clock). BP:123 says every subcommand except `init` and `home init` is accepted here.
  - `stage 3`: `init` and `home init`, accepted with WP7's templates (BP:70, BP:123 last sentences).
  - `stage 4 headless Hnn`: the headless row that exercises the clause, once WP14's runner exists. WP2's rows are H20, H21, H22, H27, H35, the `strand close` half of H36, the record half of H37, the `home init` half of H57 and the sign-off half of H66 (BP:123). H19 belongs to WP12 and H15 to the freeze owner; WP2 supplies `version release` and `freeze` to them (BP:382).
  - `Windows run`: needs a real Windows machine, in addition to the simulated test; release check 2 and the stage-5 re-run (BP:584, BP:80 to 84).
- **Test**: one line saying how to tick it.

A clause that rests on A§ or RM but not on BP:123 says so in its Src line ("A§ only"); section 4 lists the whole family.

---

## 2. Clauses

### 2.1 Runtime and cross-system rule (both scripts)

- **C01** Both scripts run on Python 3.9 and newer and import only the standard library: no third-party package, no PyYAML.
  - Src: BP:123; A§5.3:340; A§5.3:342. Accept: stage 2 unit; Windows run. Test: walk each script's imports with `ast` and check every module is standard library; run the suite under 3.9.
- **C02** Python 3.9 syntax only: no `match` statement, no `X | Y` union evaluated at runtime, nothing newer than 3.9.
  - Src: A§5.3:340; BP:123. Accept: stage 2 unit. Test: `ast.parse(source, feature_version=(3, 9))` on both scripts and both test files, under the newest Python.
- **C03** The unit tests pass on macOS on Python 3.9 and on the newest installed Python 3.
  - Src: BP:123; BP:364; A§5.3:340. Accept: stage 2 unit. Test: run both test files under each interpreter.
- **C04** The same tests pass on Windows, each on Python 3.9 and the newest installed Python 3.
  - Src: BP:123; BP:584 (release check 2); AM:36. Accept: Windows run. Test: run the suite on the Windows machine under both interpreters and record the result beside the system.
- **C05** No shell step anywhere: neither script starts a shell, calls `os.system`, uses `shell=True`, or relies on a shell-only command; every file, process and path operation is Python.
  - Src: BP:120; A§5.1:330; AM:36. Accept: stage 2 unit. Test: search both scripts for `os.system`, `shell=True`, `os.popen`; any `subprocess` call takes a list and no shell.
- **C06** Every path is built with the standard library's path handling from the home directory the standard library reports (`Path.home()` or equivalent), never from a literal `~`, never by joining strings with a fixed separator.
  - Src: BP:123; A§5.3:340; A§5.3:345; AM:36. Accept: stage 2 unit; Windows run. Test: search both scripts for `"/"` or `"\\"` joins, `"~"`, `expanduser("~")`, `os.sep` literals; run every subcommand against paths containing spaces.
- **C07** A test asserts the same record tree resolves on both systems: a record-relative reference found in a record file resolves to the same file whether the tree is opened under Windows path rules or POSIX rules.
  - Src: BP:123. Accept: stage 2 unit (simulated with `PureWindowsPath` and `PurePosixPath` and a CRLF copy of the fixture tree); Windows run (the real tree). Test: resolve every reference in the fixture tree under both flavours and compare the set of targets.
- **C08** Text files are read with either line ending (LF or CRLF) and parse to the same result.
  - Src: BP:123; A§5.3:340; AM:36. Accept: stage 2 unit; Windows run. Test: load each fixture record file in an LF copy and a CRLF copy; the parsed front matter, log entries and strand index are equal.
- **C09** Text files the scripts write carry one line ending, the same on both systems, so a record moved between systems reads the same.
  - Src: BP:123. Accept: stage 2 unit; Windows run. Test: write with the platform simulated as Windows and as POSIX and compare bytes; then read each on the other. See G11, which line ending.
- **C10** Transcripts and documents are read with either line ending wherever the scripts read them (add-transcript and add-document input, and any count the scripts take).
  - Src: BP:123; A§5.3:340. Accept: stage 2 unit; Windows run. Test: add a CRLF transcript and an LF copy of it; any value derived from the text (line count, stem) is equal.
- **C11** Flat front matter round-trips with quotes preserved: reading a file and writing it back unchanged gives the same front matter, every value still quoted, key order unchanged.
  - Src: BP:123; A§5.3:342. Accept: stage 2 unit. Test: round-trip every fixture file; compare after normalising line endings.
- **C12** Front matter is flat `key: "value"` lines, every value quoted, with `schema` as the first field, parsed without PyYAML.
  - Src: A§5.3:342; RM:96. Accept: stage 2 unit. Test: parse a file with an unquoted value and one with `schema` not first; `check` reports each with file and field.
- **C13** Every record file carries a `schema` key. A record whose `schema` is newer than the plugin knows refuses writes: every writing subcommand stops with the reason and changes no file.
  - Src: BP:123 ("a record whose schema is newer than the plugin refuses writes"); A§5.3:342; RM:96; BP:487 (H20); 1b:31 (D8). Accept: stage 2 unit; stage 4 headless H20. Test: set `CLIENT.md` to `client/3`; run `log`, `strand open`, `add-transcript`, `lease take`, `version mark`; each refuses and a before and after hash of the tree is equal.
- **C14** A rewrite of a current file first copies the old file into `.work/backup/`, then overwrites the file in place.
  - Src: BP:123; A§5.3:341. Accept: stage 2 unit. Test: rewrite a fixture file; the backup holds the old bytes and the file holds the new.
- **C15** No write path renames or deletes: neither script calls `os.rename`, `os.replace`, `os.remove`, `os.unlink`, `shutil.move`, `shutil.rmtree`, or `Path.unlink`/`rename` on a record or home file, and a rewrite keeps the same file (same inode where the system has one).
  - Src: BP:123 ("no rename and no delete"); A§5.3:341. Accept: stage 2 unit; Windows run (in-place overwrite semantics and locking differ). Test: wrap those calls with a spy and run every writing subcommand; compare file identity before and after a rewrite.
- **C16** Every out-of-record path is resolved from one root, `MMB_HOME`. When the variable is set it wins; when unset the root is `monday-builder` under the reported home directory, on either system.
  - Src: BP:123; A§5.3:345; RM:68. Accept: stage 2 unit; Windows run. Test: with the variable unset, the root equals `Path.home() / "monday-builder"`; with it set to a temp folder, every derived path (clients, cards, monday-knowledge, sandbox, archive, local) is under it.
- **C17** With `MMB_HOME` pointed at a temporary folder, no subcommand touches anything under the real home.
  - Src: BP:123. Accept: stage 2 unit. Test: set `HOME` and `USERPROFILE` to a canary folder, run every subcommand with `MMB_HOME` set elsewhere, and assert the canary and the real default home are unchanged.
- **C18** Nothing is written into the plugin's own folder (the plugin root is a per-session copy).
  - Src: BP:123; A§5.1:332. Accept: stage 2 unit. Test: run every subcommand from a read-only copy of the plugin folder. See G49 on the bytecode cache.
- **C19** No script or test hard-codes a development folder or a personal path: the clients folder comes only from `MMB_HOME`, so the same code serves the build phase and the shipped phase.
  - Src: BP:123 ("during build and test ... once the plugin ships", A22); AM:62 to 67. Accept: stage 2 unit. Test: search both scripts and both test files for any literal path under a development folder; `agnostic_sweep.py` once it exists.
- **C20** Exit codes: 0 ok, 1 blocking findings, 2 warnings only, 3 could not run. `check` returns 1 when any blocking finding exists, 2 when only warnings exist, 0 when none, and 3 when it cannot read the record.
  - Src: BP:123 ("exit codes 0/1/2/3 as specified"); A§5.3:343. Accept: stage 2 unit. Test: one fixture per code. See G10 for the codes of refusals.
- **C21** Every finding and refusal message names the file, the field, the problem and the expected value.
  - Src: A§5.3:343; BP:123 (`check` "reports file, field, problem and expected value"). Accept: stage 2 unit. Test: for each planted defect, the message (and the JSON finding) carries all four parts.
- **C22** WP2 fixes the one invocation form for its scripts that resolves on both Windows and macOS (interpreter command and plugin-root spelling), written down once and used by the tests.
  - Src: A§5.2:336; BP:62; BP:80 to 84. Accept: Windows run. Test: launch both scripts through that form on both systems. Depends on the stage-0 Windows re-run; see G36.
- **C23** `mmb_common.py` is a library with no subcommands, holding: flat front matter read and write, sha256, the guarded in-place write after backup, record paths as path objects, the home and `local/settings.json`, the plugin version, and the lease primitives.
  - Src: A§5.4:353; BP:123. Accept: stage 2 unit. Test: import it and assert each named function exists and runs on the fixture; `python mmb_common.py` has no CLI behaviour.
- **C24** The plugin version is read from `plugin.json` and used for `status --json` (`plugin_version`) and for the version stamp in `local/settings.json`.
  - Src: A§5.4:353; RM:142; A§5.3:345. Accept: stage 2 unit. Test: change the version in a copy of `plugin.json`; `status --json` reflects it. See G36 on locating the file.
- **C25** The subcommand surface is exactly the catalogue of A§5.4:354: `home init`, `init`, `status`, `check`, `log`, `guard`, `add-transcript`, `add-document`, `freeze`, `lease take|refresh|release|status|break`, `strand open|list|pause|kind|close|summary`, `version open|mark|condense-plan|condense-apply|release`, `card`. `migrate` and `tools-check` do not exist, and `check` has no `sop/` clause.
  - Src: A§5.4:354; BP:120; 1b:31, 1b:32 (D8, D9). Accept: stage 2 unit. Test: the dispatch table equals that list; `migrate` and `tools-check` return the unknown-subcommand refusal.
- **C26** Size limits: `mmb_common.py` at most 250 lines, `record.py` at most 580, the two test files together at most 480.
  - Src: BP:124; BP:76 ("limits, not goals"); A§5.4:353 to 354. Accept: stage 2 unit (inspection). Test: `wc -l`.
- **C27** The files exist: `scripts/mmb_common.py`, `scripts/record.py`, `tests/unit/test_mmb_common.py`, `tests/unit/test_record.py`, and `tests/unit/fixtures/` holding a hand-built `client/2` record tree with two strands and a lock file, owned by WP2 and distinct from WP14's seed records.
  - Src: BP:121; BP:70; BP:380. Accept: stage 2 unit (inspection). Test: list the files; load the fixture tree with `check` and expect the planned result.

### 2.2 Home and first run (`home init`)

- **C28** `home init` creates the home tree under `MMB_HOME`: `clients/`, `cards/`, `monday-knowledge/`, `sandbox/`, `archive/`, `local/`.
  - Src: BP:123; A§5.3:345; A§8.2:745; RM:68. Accept: stage 3; stage 4 headless H57. Test: run on an empty temp `MMB_HOME`; assert the six folders.
- **C29** `home init` writes `local/settings.json` from the walkthrough's answers: the firm name and its renderings for the leak list, the default build-target account, optionally the operational workspaces that are never on a shared screen, and the archive choice (a local folder by default, or a GitHub repository).
  - Src: BP:123; A§5.3:345; A§8.2:745; AM:26; AM:29. Accept: stage 3; stage 4 headless H57. Test: run with fictional answers; read the file back and compare each field. See G34 (key names are not pinned).
- **C30** The GitHub account is written to `local/settings.json` only when the user picks the GitHub archive; otherwise no GitHub account is stored.
  - Src: BP:123; AM:29; A§5.3:345; BP:524 (H57). Accept: stage 3; stage 4 headless H57. Test: the local-archive run leaves no account field or value; the GitHub run stores a fictional one.
- **C31** `local/settings.json` also records the home's creation date and the plugin version that wrote it.
  - Src: A§5.3:345 (A§ only; not in BP:123). Accept: stage 3. Test: read both values after `home init`; the version equals `plugin.json`.
- **C32** `home init` seeds `local/leak-terms.txt` and `local/sandbox-accounts.txt` empty.
  - Src: BP:123; A§5.3:345. Accept: stage 3; stage 4 headless H57. Test: both files exist with zero bytes (or zero entries).
- **C33** `home init` checks Python and the connector on the system it runs on and reports each result.
  - Src: BP:123; A§5.4:354 (adds the plugin root); A§8.2:745; BP:524 (H57). Accept: stage 3; stage 4 headless H57. Test: the output names Python and the connector with a result each. See G32 on how the connector is detected.
- **C34** The GitHub tool is checked only when the GitHub archive is picked. With the local archive nothing about GitHub is checked and no GitHub account is asked for.
  - Src: BP:123; AM:29; BP:524 (H57). Accept: stage 3; stage 4 headless H57. Test: two runs; the first reports no GitHub check, the second reports one.
- **C35** `home init` warns when a `CLAUDE.md` sits in any folder above the clients folder.
  - Src: BP:123; A§5.3:345; AM:62 to 67; BP:524 (H57). Accept: stage 3; stage 4 headless H57; Windows run. Test: plant `CLAUDE.md` in a parent of the temp home; the warning names the folder. See G37.
- **C36** `home init` runs once and again on request, and never overwrites a `local/settings.json` that exists; a second run says so.
  - Src: BP:123; BP:524 (H57). Accept: stage 3; stage 4 headless H57. Test: change the file by hand, run again; the bytes are unchanged and the output says the settings were kept. See G33.
- **C37** `home init` explains the two doors.
  - Src: BP:524 (H57); A§8.2:745. Accept: stage 3; stage 4 headless H57. Test: the output of a first run names both doors. See G32 on whether the script or the skill says it.
- **C38** The first-run walkthrough sets `MMB_HOME` in the environment in a form that works on both systems, and says how to set it on the system it runs on rather than assuming one shell.
  - Src: BP:123; A§5.3:345. Accept: stage 3; Windows run. Test: on each system the printed instruction, followed literally, makes a new session resolve the chosen home. See G35.

### 2.3 `init` (record shell)

- **C39** `record.py init` builds the record shell and the first strand `strands/001-<topic>/` from the templates, and the result passes `record.py check` with zero findings.
  - Src: BP:198; A§8.2:747; BP:70; BP:123. Accept: stage 3 (with WP7's templates). Test: run on an empty folder under a temp home, then `check`; exit 0 and no findings.
- **C40** `init` places the template copies of `CLIENT.md`, `account.json` and the strand's `build.json` with `unbound` values; this is a template copy, not a ledger write.
  - Src: BP:384; BP:198. Accept: stage 3. Test: after `init` every binding field reads `unbound`; no ledger code ran.
- **C41** `init` writes the client folder's own short `CLAUDE.md` (at most 10 lines): read `CLIENT.md` first, a fresh session for a build or an audit, nothing written into monday except through the build command.
  - Src: A§8.2:747; A§7.1:402; AM:68. Accept: stage 3. Test: the file exists, is at most 10 lines and carries those three instructions.
- **C42** `init` ships the three A11 fields at record level as `unanswered`: `transcripts_at_close`, `transcript_redaction`, `sample_data_in_account`.
  - Src: BP:198; A§7.2:471 to 473; BP:472 (H01). Accept: stage 3. Test: read the three fields after `init`.
- **C43** The record's `.gitignore` is placed only when the archive choice is GitHub.
  - Src: A§7.1:401; AM:29; BP:296. Accept: stage 3. Test: with the local choice no `.gitignore` exists; with the GitHub choice it does.
- **C44** The slug is lowercase ASCII with hyphens, at most 40 characters, and is never renamed; `init` refuses a slug that breaks the rule.
  - Src: A§7.1:441; RM:72. Accept: stage 3. Test: a 41-character slug, an uppercase slug and a non-ASCII slug are each refused. (The refusal itself is an inference; see G56.)

### 2.4 Guarded rewrite and the log

- **C45** `guard` refuses a current-file rewrite when the file's sha256 changed since the session read it.
  - Src: BP:123 ("`guard` refuses a stale sha"); A§5.3:344. Accept: stage 2 unit. Test: read the file and note its sha, change the file from outside, ask `guard` to allow a rewrite with the noted sha; it refuses.
- **C46** `guard` allows the rewrite when the sha is unchanged, and the rewrite then follows C14.
  - Src: A§5.3:344; BP:123. Accept: stage 2 unit. Test: unchanged file; the write goes through and the backup exists.
- **C47** Two sessions writing different blocks of `CLIENT.md` and of `STRAND.md`: the second write is refused as stale, the second session re-reads, writes its own block, and both blocks survive; no block is lost.
  - Src: BP:488 (H21); A§9.8:935; RM:85. Accept: stage 2 unit; stage 4 headless H21. Test: two scripted sessions; assert both blocks present in the final file.
- **C48** `log` re-reads the log file immediately before inserting, and inserts the new entry under the file header, newest first.
  - Src: BP:123; A§7.6:645. Accept: stage 2 unit. Test: append from a stale in-memory copy; both the older and the new entries are present, new first.
- **C49** Every log entry carries the strand position: the strand's short id, or `-` for a record-level event.
  - Src: BP:123; A§7.6:645; BP:488 (H21). Accept: stage 2 unit; stage 4 headless H21. Test: one entry with `--strand 001`, one without; the headers read `001` and `-`.
- **C50** The log entry header is exactly `## YYYY-MM-DD HH:MM · <strand or -> · <type> · <version or -> · <key or session label>`, followed by at most five lines.
  - Src: A§7.6:645; RM:162 to 166. Accept: stage 2 unit. Test: regex over every entry written; an entry body over five lines is rejected or flagged (see G45).
- **C51** `log` accepts the entry types of A§7.6:645 and no others (the list in section 3.5 of this file).
  - Src: A§7.6:645; RM:166. Accept: stage 2 unit. Test: each listed type is accepted; an unlisted type is not. Whether an unlisted type is refused is an inference; see G45.
- **C52** Two concurrent `log` inserts both survive: two processes inserting at the same moment leave two intact entries and a readable file.
  - Src: BP:123; BP:488 (H21). Accept: stage 2 unit; stage 4 headless H21; Windows run (file locking differs). Test: start several processes at a barrier, each inserting once; count the headers. See G09 on the mechanism.
- **C53** Log entries are never edited: `check` proves nothing below the new entries changed ("history only grew"), and a correction is a new entry naming the one it corrects.
  - Src: A§7.6:638; A§7.6:645; A§5.4:354 ("history files only grew"); BP:448 (a rewritten history entry). Accept: stage 2 unit; stage 4 headless H20. Test: edit one old entry in the fixture log; `check` blocks and names the file.
- **C54** `freeze --strand` freezes the strand's working blueprint into `versions/<v>/blueprint-r<N>.md` and returns two sha256 values that match: the working blueprint's and the frozen copy's.
  - Src: BP:123; A§7.1:421; A§7.4:601. Accept: stage 2 unit. Test: run `freeze`; the two returned values are equal and equal to an independent sha256 of the frozen file. H15 exercises the same behaviour (owner other, BP:482). See G41.

### 2.5 Intake files (`add-transcript`, `add-document`)

- **C55** `add-transcript --strand` saves the transcript at record level under `calls/`, refuses to overwrite an existing file, and records a sha256.
  - Src: BP:123; A§7.1:393; RM:20. Accept: stage 2 unit. Test: save once; save the same target again and see the refusal and an unchanged file; the recorded sha equals a fresh hash of the saved bytes. See G12, G13.
- **C56** `add-document --strand` saves a client document at record level into `inputs/`, refuses to overwrite, and records a sha256.
  - Src: BP:123; A§7.1:395; A§5.4:354. Accept: stage 2 unit. Test: as C55 for `inputs/`.
- **C57** An email arrives through `add-document` as an input of its own kind, `input_kind: email`, as pasted text saved unchanged.
  - Src: BP:123 (A§5.4, A16, Q7); A§5.4:354; A§7.1:395. Accept: stage 2 unit; stage 4 headless H09 (owner other). Test: add a pasted email; the saved bytes equal the input and the kind is recorded as `email`. See G13.
- **C58** An email may also arrive as a screenshot saved as an image, bytes unchanged.
  - Src: BP:123; A§5.4:354; A§7.1:395. Accept: stage 2 unit. Test: add a PNG as an email input; the saved file equals the input byte for byte.
- **C59** An attachment is taken in only when the user adds it as its own input: saved as a document through `add-document`, and linked to the email only when the user says it came with it. Adding an email never creates an attachment file or a link by itself.
  - Src: BP:123; A§5.4:354. Accept: stage 2 unit. Test: add an email, then check `inputs/` holds only the email; add a document with the link instruction and see the link recorded. See G13 on where the link lives.
- **C60** Raw files are saved once and never edited: the saved bytes equal the input bytes (no line-ending rewrite), and the recorded sha256 is of those bytes.
  - Src: A§7.1:378 (raw: saved once, never edited); BP:123 ("saved unchanged"); RM:7. Accept: stage 2 unit; Windows run. Test: a CRLF transcript is saved with its CRLF bytes intact. In tension with C09; see G11.
- **C61** Both subcommands take `--strand` only to stamp who asked; the files land at record level (`calls/`, `inputs/`), never under `strands/`.
  - Src: A§5.4:354; A§7.1:380; A§7.1:393 to 395. Accept: stage 2 unit. Test: path assertion on the saved file.
- **C62** Dated files are named `YYYY-MM-DD-<topic>`; a second file the same day takes `-2`.
  - Src: A§7.1:441; RM:74. Accept: stage 2 unit. Test: two files the same day; the second ends `-2`. In tension with C55; see G12.

### 2.6 Strands

- **C63** `strand open` assigns the next zero-padded ordinal, monotonic per record and never reused, including after a strand is closed or paused.
  - Src: BP:123; A§7.1:441; RM:73. Accept: stage 2 unit. Test: open three strands, close the second, open another; the new id is `004`. See G56 on the source of the counter.
- **C64** A strand id is `NNN-<topic>`: a three-digit ordinal and a topic slug of at most 24 lowercase ASCII characters; the folder is `strands/<id>/`; the short id is the ordinal alone.
  - Src: A§7.1:441; RM:73. Accept: stage 2 unit. Test: a 25-character topic and an uppercase topic are refused (refusal inferred; see G56); the folder name equals the id.
- **C65** `strand open` takes the kind (`platform`, `non-platform`, `hybrid`) together with its reason, and records both: the kind in `kind`, the reason in `opened_reason`.
  - Src: BP:123; A§7.7:651 to 682; RM:104. Accept: stage 2 unit. Test: open one strand of each kind; read both fields.
- **C66** `strand open` places `readiness.md` and `exclusions.md` from the templates, `readiness.md` under the strand and `exclusions.md` under `solution/`.
  - Src: BP:123; A§7.1:410; A§7.1:415. Accept: stage 2 unit (templates: see G31); stage 3. Test: after `strand open`, both files exist at those paths.
- **C67** A fresh strand's `readiness.md` carries the clearance value `none`, which is distinct from the check's own `not yet`.
  - Src: BP:123; A§5.4:354; RM:212. Accept: stage 2 unit. Test: read the clearance after `strand open`.
- **C68** `strand open` writes the strand's `STRAND.md` (`strand/1`) with `state: active`, `stage: new`, `version: none`, `version_state: none`, `clearance: none`.
  - Src: A§7.7:651 to 676 (inferred; BP:123 names only the two template files). Accept: stage 2 unit. Test: read the front matter after `strand open`. See G06, G43.
- **C69** For a `non-platform` strand, `strand open` creates no `versions/`, no `solution/blueprint.md`, no `solution/build.json`.
  - Src: A§7.1:429; A§7.9:724. Accept: stage 2 unit. Test: open a `non-platform` strand; list its tree.
- **C70** `strand list` exists and is exercised: it lists every strand of the record.
  - Src: BP:123; A§5.4:354. Accept: stage 2 unit. Test: list a two-strand fixture; both short ids appear. The columns are not specified (G25).
- **C71** `strand pause` exists and is exercised: it sets the strand's `state` to `paused`.
  - Src: BP:123; A§7.7:686. Accept: stage 2 unit. Test: pause an active strand; read `state`. See G52.
- **C72** `strand kind` changes the kind only while the strand has no versions; otherwise it refuses. A change writes a `strand` log entry.
  - Src: BP:123; A§7.7:682; RM:104. Accept: stage 2 unit. Test: change kind on a fresh strand (passes, log entry present); change kind on a strand with `versions/v0.1` (refused).
- **C73** `strand close` rolls that strand's log entries out of the record log into `strands/<id>/log.md` as a snapshot, leaves one pointer entry behind, and records the hashes of the moved entries.
  - Src: BP:123; A§7.6:645; A§8.10:828; BP:503 (H36). Accept: stage 2 unit; stage 4 headless H36. Test: close a strand with three entries; the moved file holds them, the record log holds one pointer, the hashes are recorded. See G08.
- **C74** `strand close` refuses while that strand holds the lease.
  - Src: BP:123; A§8.10:828; BP:503 (H36). Accept: stage 2 unit; stage 4 headless H36. Test: hold the lease for the strand; close; refused, nothing moved.
- **C75** `strand close` refuses while the strand is `paused`.
  - Src: BP:123; A§7.7:686; BP:503 (H36). Accept: stage 2 unit; stage 4 headless H36. Test: pause then close; refused.
- **C76** `strand close` refuses while any version of the strand is `building` or `fixing`.
  - Src: BP:123; A§8.10:828. Accept: stage 2 unit. Test: one fixture per state; each refused.
- **C77** `strand close` refuses while an unreleased version has no close reason recorded.
  - Src: A§8.10:828 (A§ only; not in BP:123). Accept: stage 2 unit. Test: an unreleased version with no reason; refused. See G07.
- **C78** After a strand close, nothing is archived, nothing is moved into `archive/`, and no file outside the strand's own front matter, its rolled log and the pointer entry changes.
  - Src: A§8.10:828; BP:503 (H36); BP:296. Accept: stage 2 unit; stage 4 headless H36. Test: hash the tree before and after, excluding the strand's `STRAND.md`, its `log.md`, the record `log.md`; `archive/` is empty.
- **C79** `strand summary` writes `SUMMARY.md` (`summary/1`) at or under 80 lines, after the user's yes to a plan, and sets `summary_current_to`.
  - Src: BP:123; A§7.7:684; RM:108. Accept: stage 2 unit; stage 4 headless H36 (the 80-line check). Test: run the plan step then the write step; line count at most 80; `summary_current_to` equals the version. See G42.
- **C80** `SUMMARY.md` carries the front matter `strand`, `title`, `kind`, `versions`, `closed`, `summary_current_to`, `budget_lines` and the nine blocks in the order of section 3.12.
  - Src: A§7.7:684; RM:108. Accept: stage 2 unit. Test: parse a written summary; fields and block order equal the list.
- **C81** For a `non-platform` strand the built-objects block of `SUMMARY.md` reads "nothing built inside the product".
  - Src: A§7.7:684; RM:108. Accept: stage 2 unit. Test: write a summary for a `non-platform` fixture strand; the block text matches.

### 2.7 Lease: primitives, mirrors, take, refresh, release

- **C82** The lease primitives in `mmb_common.py` are the only code that writes `.work/lock.json`; `record.py` and `ledger.py` call them and neither writes the file itself.
  - Src: BP:123; BP:68; BP:384; A§5.4:353; A§9.8:933. Accept: stage 2 unit. Test: static scan of `record.py` for any write to `lock.json`; the primitives are importable and callable.
- **C83** The primitives are take, refresh, release and break; each is a state change and none deletes the file. The lock `state` takes only `none`, `held`, `released`, `broken`.
  - Src: BP:123; RM:135; A§9.8:941. Accept: stage 2 unit. Test: run each; the file exists afterwards and `state` is in the set; the delete spy of C15 stays silent.
- **C84** The lock's two mirrors, `CLIENT.md`'s `lease` field and `account.json.guard_index.lease`, are written by the same primitives in the same call as the lock, and by nothing else.
  - Src: BP:123; BP:384; A§9.8:933; RM:135. Accept: stage 2 unit. Test: after each primitive, the lock and both mirrors agree; a grep shows no other code writes either mirror.
- **C85** The mirror values follow the pinned shapes: `CLIENT.md` `lease` is `"none"` or `"<strand> <version> (<label>)"`; `guard_index.lease` is `{strand, epoch, label, heartbeat_at}` with `strand` null when none is held.
  - Src: A§7.2:468; A§7.3:524; RM:100; RM:116; RM:135. Accept: stage 2 unit. Test: compare after take and after release. The label's field name differs between sources; see G01.
- **C86** Writing the `account.json` mirror changes only `guard_index.lease`; every other field of `account.json` is left as it was.
  - Src: BP:134; BP:384; A§5.4:355. Accept: stage 2 unit. Test: parse `account.json` before and after a primitive; all keys but that block are equal.
- **C87** `lease take` records `kind: "build"`, the strand, its title, the version, `taken_at`, `heartbeat_at` and `state: "held"`, and the epoch.
  - Src: A§9.8:933; RM:135. Accept: stage 2 unit. Test: take; read every field.
- **C88** `lease take` increments the epoch, which is `0` before the first take.
  - Src: BP:123; A§9.8:933; RM:135. Accept: stage 2 unit. Test: take, release, take; epochs 1 then 2.
- **C89** `lease take` mints the session label from a timestamp and a short random suffix and returns it; two takes on one day never collide.
  - Src: BP:123; A§9.8:933; RM:77. Accept: stage 2 unit. Test: force many takes in one minute with a fixed clock; all labels distinct; format matches section 3.9. See G01 for the exact format.
- **C90** `refresh`, `release` and `break` require the label; a missing or different label is refused as another session.
  - Src: BP:123; A§9.8:933. Accept: stage 2 unit. Test: call each with no label and with a wrong label.
- **C91** `lease take` refuses a `non-platform` strand.
  - Src: BP:123; A§7.9:724; BP:504 (H37). Accept: stage 2 unit; stage 4 headless H37. Test: take for a `non-platform` fixture strand; refused with the reason.
- **C92** `lease take` refuses while another strand holds the lease, and the refusal names the holder with strand, title, version, session label, heartbeat age, and fresh or stale.
  - Src: BP:123; BP:502 (H35); A§9.8:939. Accept: stage 2 unit; stage 4 headless H35. Test: fixture with strand 001 holding a stale lease; take for 002; every named item is present in the message.
- **C93** `lease take` refuses while another session of the same strand holds the lease, naming the holder as in C92.
  - Src: BP:123; BP:489 (H22). Accept: stage 2 unit; stage 4 headless H22. Test: take twice for the same strand; the second is refused with strand, version, session label and heartbeat age.
- **C94** The refusal of C92 and C93 also says: that nothing local is blocked (intake, the readiness check and a blueprint revision may continue); that the audit and the release for any strand are blocked while a build is live; and the three ways forward (wait for the run to end, ask the holder's session to release it with `record.py lease release`, or break it if stale, staleness stated as a fact).
  - Src: A§9.8:939; BP:489 (H22: "says what the waiting session may still do locally"); BP:502 (H35: "the three ways forward"). Accept: stage 2 unit; stage 4 headless H22 and H35. Test: assert the message carries each of the four statements.
- **C95** A heartbeat older than 60 minutes reads stale; 60 minutes or less reads fresh; nothing expires on its own, so a stale lease stays `held` until someone breaks it.
  - Src: BP:123; A§9.8:943; RM:135. Accept: stage 2 unit. Test: injected clock at 59, 60 and 61 minutes; at 61 `fresh` is false and `state` is still `held`.
- **C96** `lease refresh` sets `heartbeat_at` on the lock and on the `account.json` mirror and appends no history entry.
  - Src: RM:135; A§9.8:943; A§9.8:933. Accept: stage 2 unit. Test: refresh; heartbeat moves, `history` length unchanged.
- **C97** The lock `history` list gets an entry on a take, a release, a break and a park, never on a refresh, and entries are retained, never deleted. An entry has `event`, `at`, `epoch`, `strand`, `version`, the label, `run_id`, `by`, `choice`, `reconcile`, `note`.
  - Src: RM:135; A§9.8:933. Accept: stage 2 unit. Test: take, refresh, release; history has two entries, take and release, with the listed fields.
- **C98** `lease release` sets the state to `released`, keeps the file and the history, and works only for the holder's label.
  - Src: A§9.8:941; RM:135. Accept: stage 2 unit. Test: release by the holder (state `released`); release with another label (refused).
- **C99** `lease status` reports the lease block of C118: held or not, state, epoch, strand, title, version, label, run id, taken_at, heartbeat_at, heartbeat age in minutes, fresh.
  - Src: A§5.4:354; RM:146 to 152. Accept: stage 2 unit. Test: compare its output with `status --json`'s `lease` block.
- **C100** The primitives are callable by `ledger.py` as library functions under the same refusal rules (refresh on every ledger write, release at `run end`), so ledger code never edits the lock directly.
  - Src: BP:68; BP:134; A§5.4:353. Accept: stage 2 unit. Test: import and call each primitive from a test standing in for `ledger.py`.

### 2.8 Lease: break

- **C101** `lease break` is refused unless all five conditions of A§9.8:945 hold; each of C102 to C106 is one condition, and the refusal names the condition that failed.
  - Src: BP:123; A§9.8:945. Accept: stage 2 unit; stage 4 headless H35. Test: five runs, each with exactly one condition false; each refused with its own message; one run with all true; accepted.
- **C102** Condition 1: the holder's heartbeat is stale.
  - Src: A§9.8:945; BP:123. Accept: stage 2 unit. Test: a fresh lease; break refused.
- **C103** Condition 2: the user says yes in this session naming the holding strand; prose about "clearing the lock" is not a yes.
  - Src: A§9.8:945; BP:502 (H35: "refused without the user's yes naming 001"). Accept: stage 2 unit; stage 4 headless H35. Test: call without the naming yes (refused); with a yes naming another strand (refused). See G04.
- **C104** Condition 3: an account check passes, so the break happens in the right account.
  - Src: A§9.8:945. Accept: stage 2 unit. Test: supply a failing account check; refused. See G04.
- **C105** Condition 4: recovery ran first over the holder's strand, not the taker's, in classify-only mode (adopting, retrying and archiving nothing).
  - Src: A§9.8:945; A§8.11:836. Accept: stage 2 unit. Test: no reconcile result supplied for the holder; refused. See G04.
- **C106** Condition 5: the user has chosen what happens to the interrupted run, `resume` or `park`.
  - Src: A§9.8:945; BP:123. Accept: stage 2 unit. Test: no choice supplied; refused.
- **C107** A break with `park` is refused when the holder's reconcile found any element in the `duplicate` or `partial` class, and parking needs its own yes.
  - Src: A§9.8:945; BP:502 (H35). Accept: stage 2 unit; stage 4 headless H35. Test: reconcile summary with one `duplicate`; park refused; resume allowed.
- **C108** A break records the user's resume-or-park choice in both strands' logs.
  - Src: BP:123; BP:502 (H35: "both strands' logs carry the choice"). Accept: stage 2 unit; stage 4 headless H35. Test: after the break, entries exist for the holder's strand and the taker's strand carrying the choice. See G03.
- **C109** A break also writes a `lease` log entry at record level (strand position `-`) with the broken epoch, the holder, the reconcile summary and the choice.
  - Src: A§9.8:945; A§7.6:645. Accept: stage 2 unit; stage 4 headless H35. Test: read the entry. See G03 on the count of entries.
- **C110** A break increments the epoch, and the new holder starts at epoch plus one.
  - Src: A§9.8:933; A§9.8:945; BP:502 (H35: "002 holds epoch + 1"). Accept: stage 2 unit; stage 4 headless H35. Test: epoch before and after break and take. See G03, which sources disagree on the arithmetic.
- **C111** Break with `resume`: the lease goes to a fresh session for the holding strand, with a label minted by that take; the holder's strand then runs the ordinary recovery.
  - Src: A§9.8:945; BP:502 (H35). Accept: stage 2 unit; stage 4 headless H35. Test: after the break the lock names the holder's strand and a new label.
- **C112** Break with `park`: the holder's strand goes to `paused` with what is unresolved written into its `STRAND.md`; the taker holds the lease with a new epoch and a label minted by its take.
  - Src: A§9.8:945; A§7.7:686; BP:502 (H35). Accept: stage 2 unit; stage 4 headless H35. Test: read the holder's `STRAND.md` `state` and the unresolved block; read the lock.
- **C113** After a break the old session's presented epoch, label or run id no longer matches the lock, so the lock state alone is enough for the ledger to refuse it with a reason: a write with the old epoch, with the new epoch and the old label, or with the new epoch and the old run id.
  - Src: A§9.8:933; BP:134; BP:502 (H35). Accept: stage 2 unit; stage 4 headless H35. Test: compare each stale triple against the lock through the primitives' reader. The ledger-side refusal is WP3's; see G51.

### 2.9 `status --json`

- **C114** `status --json` is one call that returns one JSON object with the keys `schema` (`status/1`), `generated_at`, `plugin_version`, `record_schema`, `migration_needed`, `record`, `strands`, `lease`, `interrupted`, `findings`.
  - Src: BP:123; RM:137 to 152; A§5.4:354. Accept: stage 2 unit. Test: validate the output of the fixture against section 3.1. See G19 on `migration_needed`.
- **C115** `record` carries every `client/2` front-matter field by name, as the strings they are, including the build target and the client's workspaces.
  - Src: BP:123; RM:143; RM:139. Accept: stage 2 unit. Test: compare keys with the `CLIENT.md` front matter of the fixture. See G15.
- **C116** `strands` has one entry per strand with every `strand/1` field by name and the computed values `qualified_version`, `open_versions`, `live_objects`, `last_activity`, `run`.
  - Src: RM:144 to 145; BP:123. Accept: stage 2 unit. Test: two-strand fixture; both entries have the full field set and correct computed values.
- **C117** Each `strands` entry carries the strand's version, version state, version purpose and clearance.
  - Src: BP:123 (adds purpose); A§5.4:354 (adds `stage`, `shown`, `signed_off`); RM:144 (none of purpose, shown, signed_off). Accept: stage 2 unit. Test: read each field for a strand with a `shown` event. See G19.
- **C118** The `lease` block has `held`, `state`, `epoch`, `strand`, `strand_title`, `version`, the label, `surface`, `run_id`, `taken_at`, `heartbeat_at`, `heartbeat_age_minutes`, `fresh`; when nothing is held, `held` is false, `state` is `none`, `released` or `broken`, and the last epoch is kept.
  - Src: RM:146 to 152; BP:123 ("and the lease block"). Accept: stage 2 unit. Test: one status per lock state. See G01.
- **C119** `run` is null when the strand has no open run; otherwise it has `id`, `state`, `heartbeat_at`, `heartbeat_age_minutes`.
  - Src: RM:145; RM:152. Accept: stage 2 unit. Test: strands with and without a running entry in `build.json`.
- **C120** `--strand <id>` returns the same object with exactly one entry in `strands`.
  - Src: BP:123; RM:152. Accept: stage 2 unit. Test: compare with and without `--strand`.
- **C121** `interrupted` lists `{strand, run_id, version}` for each run in state `interrupted`.
  - Src: RM:148. Accept: stage 2 unit. Test: fixture with an interrupted run.
- **C122** `findings` has `blocking` and `warnings`, each entry `{file, field, problem, expected}`, the same findings `check` would report.
  - Src: RM:149. Accept: stage 2 unit. Test: plant one blocking and one warning defect; compare with `check`.
- **C123** Front-matter values come back as the strings they are; computed values come back as JSON types (booleans, integers, null, arrays).
  - Src: RM:139; RM:96. Accept: stage 2 unit. Test: type assertions on `fresh`, `epoch`, `heartbeat_age_minutes`, `live_objects`, `strands_open`.
- **C124** `status` changes nothing in the record.
  - Src: A§5.4:354 ("the front door's one read"); inferred. Accept: stage 2 unit. Test: hash the tree before and after.

### 2.10 `check`

- **C125** `check` blocks on a binding mismatch between `CLIENT.md` and `account.json` (the account id, slug, bound user, bound time) and on a build target that differs between them.
  - Src: BP:123; A§5.4:354; RM:100. Accept: stage 2 unit; stage 4 headless H20. Test: change `monday_account_id` in `CLIENT.md` only; blocking finding.
- **C126** `check` blocks on a strand ledger whose `account_id_at_bind` differs from `account.json`'s account id.
  - Src: BP:123; RM:120; BP:448. Accept: stage 2 unit; stage 4 headless H20. Test: edit the strand's `build.json`; blocking finding.
- **C127** `check` enforces the required files of the version state, in the table of section 3.6, and blocks on a missing file at release.
  - Src: BP:123; A§7.4:598 to 606; A§5.4:354. Accept: stage 2 unit; stage 4 headless H20, H27. Test: for each state remove one required file; finding names the file. See G27 on non-release states.
- **C128** `check` blocks when the strand index in `CLIENT.md` disagrees with the folders on disk.
  - Src: BP:123; A§5.4:354; RM:87 to 92. Accept: stage 2 unit; stage 4 headless H20. Test: add a strand folder with no index row; remove a row; each blocks. See G18.
- **C129** `check` blocks on a fully qualified reference that does not resolve (`001/v0.1`, `001:B1`, `001/v0.1r4`; inside a strand's ledger `v0.1r4#B1`).
  - Src: BP:123; RM:75; A§7.1:441. Accept: stage 2 unit; stage 4 headless H20. Test: a dangling `001:B9` in the live map; blocking finding.
- **C130** `check` blocks on a live-map row absent from `account.json.live_objects`, and on one absent from the live map.
  - Src: BP:123; RM:124 ("a row present on one side and absent on the other is blocking"). Accept: stage 2 unit; stage 4 headless H20. Test: delete one row from each side in turn.
- **C131** `check` blocks when either lease mirror disagrees with the lock file.
  - Src: BP:123; A§5.4:354; BP:384; RM:135. Accept: stage 2 unit; stage 4 headless H20. Test: change the `CLIENT.md` mirror; then the `account.json` mirror; each blocks.
- **C132** `check` blocks on `versions/`, `blueprint.md` or `build.json` under a `non-platform` strand; there is no `sop/` clause.
  - Src: BP:123; BP:120; A§7.1:429; A§7.9:724; BP:504 (H37). Accept: stage 2 unit; stage 4 headless H37. Test: plant `solution/blueprint.md` in a `non-platform` strand; blocking.
- **C133** `check` blocks on a `scope.md` that lacks the fixed hand-off sentence as its final section.
  - Src: BP:123; A§7.9:725; RM:110. Accept: stage 2 unit; stage 4 headless H20. Test: remove the sentence; blocking. Verbatim text in section 3.7.
- **C134** `check` blocks on a `readiness.md` whose clearance is neither one of the three pinned strings nor `none`.
  - Src: BP:123; A§5.4:354; RM:212; BP:448. Accept: stage 2 unit; stage 4 headless H20. Test: set a clearance of `ready`; blocking. See G28.
- **C135** `check` treats `none` as valid, meaning the check has not run yet, and does not confuse it with its own `not yet`.
  - Src: BP:123; A§5.4:354; RM:212. Accept: stage 2 unit. Test: a fresh strand's `readiness.md` yields no clearance finding.
- **C136** `check` blocks on a strand whose revision plans sample rows while `exclusions.md` is absent.
  - Src: BP:123; A§7.1:415. Accept: stage 2 unit. Test: a fixture strand with sample rows planned and no exclusions file. See G29 on how "plans sample rows" is detected.
- **C137** `check` blocks on a rolled log whose moved entries do not hash as recorded.
  - Src: BP:123; A§7.6:645; BP:448. Accept: stage 2 unit; stage 4 headless H20. Test: alter one moved entry in a rolled strand log; blocking. See G08.
- **C138** `check` warns when a file exceeds its size budget (the budgets are in section 3.11).
  - Src: BP:123; A§5.4:354; A§7.1:384 to 428. Accept: stage 2 unit. Test: grow a fixture file past its budget; a warning, exit code 2 if nothing else.
- **C139** `check` warns when the whole record passes the soft 4 MB, excluding `calls/*.transcript.txt`, `inputs/*.<ext>` and `.work/`, and names the largest strands.
  - Src: BP:123 ("per-record soft 4 MB"); A§7.1:429; RM:64. Accept: stage 2 unit. Test: a fixture over 4 MB; the warning names strands by size. See G44 on the excluded set.
- **C140** `check` blocks when `SUMMARY.md` passes 120 lines, and when `live/live-map.md` passes 400 lines.
  - Src: A§7.1:409; A§7.1:397; RM:36; RM:25. Accept: stage 2 unit. Test: a 121-line summary and a 401-line live map; each blocks.
- **C141** (umbrella) `check` blocks on an A11 field left `unanswered` at the moment it matters and is silent otherwise; the rule is ticked by C142 to C146 together.
  - Src: BP:123; BP:23. Accept: stage 2 unit. Test: C142, C143, C144, C145 and C146 all pass.
- **C142** A11-2: with a build target of `client-account`, a revision planning sample rows in any strand while `sample_data_in_account` is `unanswered` is blocking.
  - Src: BP:18; BP:23; A§7.2:473; A§7.2:479. Accept: stage 2 unit; stage 4 headless H39. Test: client-account fixture with sample rows planned; blocking; the own-account twin is silent. See G14, G29.
- **C143** A11-3: saving the first non-fixture transcript or document while `transcripts_at_close` or `transcript_redaction` is `unanswered` is blocking.
  - Src: BP:19; BP:23; A§7.2:471 to 472. Accept: stage 2 unit; stage 4 headless H56 (owner other). Test: a record with a real input and an unanswered field; blocking; a fixture-marked input is silent. See G14.
- **C144** A11-1: a record bound for write probes while the probe workspace is unanswered is blocking.
  - Src: BP:17; BP:23. Accept: stage 2 unit. Test: a record bound for write probes; blocking. See G14.
- **C145** At every other moment an A11 field at `unanswered` produces no finding at all, not even a warning.
  - Src: BP:23; RM:100. Accept: stage 2 unit; stage 4 headless H01 (setup asks none of the three). Test: a freshly created record with all three `unanswered`; `check` exit 0, no findings.
- **C146** `check` never fills an A11 field in: it writes nothing.
  - Src: BP:23; RM:100. Accept: stage 2 unit. Test: hash before and after on a record that triggers each block.
- **C147** `check` accepts the A11 value sets: `transcripts_at_close` `unanswered|exclude|archive`; `transcript_redaction` `unanswered|none|offered-per-call|always`; `sample_data_in_account` `unanswered|allowed|not-allowed|not-needed`.
  - Src: A§7.2:471 to 473; RM:100. Accept: stage 2 unit. Test: each listed value passes; an unlisted value is a finding. See G15 (`not-needed`).
- **C148** `check` reports a native-board index past its staleness budget (`guard_index.captured_at` against `record_provenance.staleness_budget_days`).
  - Src: BP:448; BP:487 (H20: "a stale native index downgrades guarded writes to an ask"). Accept: stage 2 unit; stage 4 headless H20. Test: a fixture with an old `captured_at`; finding present. See G30, G47 (severity, and whether the downgrade is a hook matter).
- **C149** `check` reports a strand whose `build_targets_by_strand` entry names a workspace outside the client's workspaces.
  - Src: BP:448; BP:487 (H20: "the out-of-scope build target"). Accept: stage 2 unit; stage 4 headless H20. Test: plant a foreign workspace id; finding names the strand and the id. See G47.
- **C150** `check` reports a raw transcript or input whose sha256 differs from the recorded one (an edited transcript).
  - Src: BP:448; A§7.1:393. Accept: stage 2 unit; stage 4 headless H20. Test: edit a byte of a fixture transcript.
- **C151** `check` reports a frozen blueprint whose sha256 differs from the one in `version.md` and `build.json.approvals` (a hand-edited frozen blueprint).
  - Src: BP:448; A§7.4:601. Accept: stage 2 unit; stage 4 headless H20. Test: edit the frozen file.
- **C152** `check` reports an absolute path in either spelling (Windows `C:\...` and POSIX `/...`) found in a record file, with the same result on both systems.
  - Src: BP:448 (A24); A§7.1:441 ("Links are relative only"). Accept: stage 2 unit; Windows run. Test: two planted paths, one in each spelling; both reported on each system.
- **C153** `check` reports a stale lease.
  - Src: BP:448 (a stale lease among the broken records); BP:487 (H20). Accept: stage 2 unit; stage 4 headless H20. Test: the fixture's stale lock; a finding. See G48 for severity.
- **C154** `check` verifies the front matter and `schema` of the record and strand files.
  - Src: A§5.4:354 (A§ only). Accept: stage 2 unit. Test: a file without `schema`; finding.
- **C155** `check` reports a link that is not relative.
  - Src: A§5.4:354; A§7.1:441 (A§ only). Accept: stage 2 unit. Test: an absolute link; finding.
- **C156** `check` reports an evidence marker that carries no location, and reports any marker or internal id found under `drafts/`.
  - Src: A§5.4:354; A§7.5:626 (A§ only). Accept: stage 2 unit. Test: a `[Q]` with no location in `calls/`; a marker in a `drafts/` file. See G61 (nine or eight markers).
- **C157** `check` looks for the line "Internal: never client-facing" at the top of every internal template-derived file.
  - Src: A§6:367 (A§ only); RM:112. Accept: stage 2 unit. Test: a file without it; finding.

### 2.11 `version` subcommands

- **C158** `version open` creates the version's `versions/<v>/version.md` with `strand`, `qualified_version` and `purpose` in its front matter.
  - Src: A§5.4:354; A§7.4:585; BP:198. Accept: stage 2 unit. Test: open `v0.1`; read the three fields. See G25.
- **C159** A version's purpose reads `proof-of-concept` below `v1.0` and `working-solution` from `v1.0`.
  - Src: BP:123; A§7.4:585; A§7.4:587; BP:533 (H66). Accept: stage 2 unit; stage 4 headless H66. Test: `v0.1` and `v0.9` read proof-of-concept; `v1.0` reads working-solution. See G23.
- **C160** `version mark --strand <id> shown` records the event with its date, the user's words and the account the version was shown in; a version may be marked `shown` more than once.
  - Src: BP:123; A§7.4:608; A§7.4:610; A§8.8:815. Accept: stage 2 unit. Test: mark twice; both events kept. See G20 (audience by role is in A§ and not in BP).
- **C161** `version mark --strand <id> signed-off` records the event with its date, the user's words and who by role.
  - Src: BP:123; A§7.4:593; A§8.8:817. Accept: stage 2 unit; stage 4 headless H66. Test: mark; read the event. See G20.
- **C162** Before recording `signed-off`, the command lists every structural assumption of the strand not yet confirmed or explicitly accepted, as the user reported the client's word.
  - Src: BP:123; A§7.4:587; AM:46 to 48. Accept: stage 2 unit; stage 4 headless H66. Test: fixture with one `assumed` structural assumption; it is listed. See G21.
- **C163** The listing is a warning, not a block: when the user goes on, the event is recorded anyway; the command never refuses on that ground.
  - Src: BP:123; A§5.4:354; AM:46; BP:533 (H66). Accept: stage 2 unit; stage 4 headless H66. Test: sign off with an unconfirmed assumption; the event is recorded, exit code not 1 for that reason. See G22.
- **C164** The list the warning showed is kept with the event, in `version.md`.
  - Src: A§7.4:608; BP:198; BP:533 (H66: "with the list kept beside it"). Accept: stage 2 unit; stage 4 headless H66. Test: read the event after the call; the list is present.
- **C165** Recording `shown` or `signed-off` advances the strand's `stage` and leaves the version state unchanged; recording `signed-off` advances the stage whether or not assumptions remain.
  - Src: A§7.7:680. Accept: stage 2 unit. Test: before and after, `stage` moves and `version_state` does not. See G16.
- **C166** `version release --strand` refuses while any strand holds the lease, not only the strand being released.
  - Src: BP:123; A§9.8:935; A§7.4:610. Accept: stage 2 unit. Test: another strand holds the lease; release for 001 is refused.
- **C167** `version release --strand` refuses while a file required for the state is missing, and the refusal lists the missing files.
  - Src: BP:123; BP:494 (H27); A§7.4:606. Accept: stage 2 unit; stage 4 headless H27. Test: remove each file of the `released` row in turn; refused with the list.
- **C168** For `v1.0`, the `signed-off` event recorded is one of the files required to release.
  - Src: A§7.4:606. Accept: stage 2 unit. Test: release `v1.0` with and without the event.
- **C169** `version release --strand` refreshes the strand's `SUMMARY.md`.
  - Src: BP:123; A§7.7:684. Accept: stage 2 unit; stage 4 headless H19 (owner WP12). Test: after a release `summary_current_to` equals the released version and the file is at most 80 lines.
- **C170** `version release --strand` also freezes the strand's snapshots (`build.json`, `backlog.md`, `log.md` under `versions/<v>/`), rolls the strand's entries out of the record log, and condenses the strand's current files, in the user's one yes.
  - Src: A§7.4:610; A§8.8:818; BP:486 (H19). Accept: stage 2 unit; stage 4 headless H19 (owner WP12). Test: every removed line's fact found in a snapshot, the summary or the log. See G26.
- **C171** `version condense-plan` shows line by line where each removed fact survives; `condense-apply` applies the plan after the user's yes; lines with no surviving copy stay. Both refuse while any strand holds the lease.
  - Src: A§5.4:354; A§7.4:610; A§9.8:935. Accept: stage 2 unit. Test: plan, then apply; assert no line without a surviving copy is removed; take the lease and see both refuse. See G25.

### 2.12 Other subcommands

- **C172** `card` exists and takes `--strand`.
  - Src: A§5.4:354 (named, with no acceptance sentence in BP:123). Accept: stage 2 unit. Test: the subcommand is in the dispatch table and accepts the flag. See G25.

### 2.13 WP2's halves of the headless rows

Each row is accepted when WP14's runner runs it; the unit clauses named must already pass.

- **C173** H20 (broken records): `record.py check` names each defect with file and field, including the strand-level ones of BP:448, the bad clearance string and the out-of-scope build target; a newer schema refuses writes; a stale native index is reported.
  - Src: BP:487; BP:448. Accept: stage 4 headless H20. Test: the seed's broken records through `check`. Builds on C13, C53, C125 to C139, C148 to C153.
- **C174** H21 (two sessions on `CLIENT.md` and `STRAND.md`): the guard forces a re-read; both log entries survive with their strand position; no block is lost.
  - Src: BP:488. Accept: stage 4 headless H21. Test: the run. Builds on C45 to C49, C52.
- **C175** H22 (lease held by another session of the same strand): the build refuses and names the holder with strand, version, session label and heartbeat age, and says what the waiting session may still do locally.
  - Src: BP:489. Accept: stage 4 headless H22. Test: the run. Builds on C93, C94.
- **C176** H27 (release refused): missing state files block the release with the list.
  - Src: BP:494. Accept: stage 4 headless H27. Test: the run. Builds on C127, C167.
- **C177** H35 (stale lease held by a sibling strand, on the two-strand seed): the build for 002 refuses naming 001's title, version, session label, heartbeat age and "stale", with the three ways forward; `lease break` is refused without the user's yes naming 001 and refused on park when the classify-only reconcile finds a `duplicate` or `partial`; on resume-first the lease goes to a fresh session for 001; on park 001 is `paused` with the unresolved list in its `STRAND.md` and 002 holds epoch plus one with a label minted by the take; a ledger write carrying the old epoch, or the new epoch with the old label or the old run id, is refused with the reason; both strands' logs carry the choice; a later resume of 001, once 002 has released, ends the run and returns 001 to `active`.
  - Src: BP:502. Accept: stage 4 headless H35. Test: the run. Builds on C92 to C94, C101 to C113. The last clause has no record.py command; see G05.
- **C178** H36, WP2's half (`strand close`, then record close, on the two-strand seed): the strand close refuses while 001 holds the lease and while 001 is `paused`, then closes once resumed with `SUMMARY.md` at or under 80 lines and the log rolled with hashes verified, nothing archived and nothing moved into `archive/`.
  - Src: BP:503; BP:123. Accept: stage 4 headless H36. Test: the run. Builds on C73 to C79.
- **C179** H37, WP2's half (a `non-platform` strand): `record.py lease take` refuses the strand and `record.py check` blocks the planted `blueprint.md`.
  - Src: BP:504; BP:123. Accept: stage 4 headless H37. Test: the run. Builds on C91, C132.
- **C180** H57, WP2's half (the first-run walkthrough on an empty home): `home init` creates the home tree with `archive/`, writes `local/settings.json` with the firm renderings, default build target, operational workspaces and archive choice (local by default) and no GitHub account; reports the Python and connector checks and runs no GitHub check; a second walkthrough picking GitHub checks the tool and records a fictional account; a planted `CLAUDE.md` above the clients folder raises the warning; the two doors are explained; a second run refuses to overwrite the settings and says so.
  - Src: BP:524. Accept: stage 4 headless H57 (and stage 3). Test: the run. Builds on C28 to C38.
- **C181** H66, WP2's half (assumptions carried to sign-off): `record.py version mark --strand signed-off` on the seed with its unconfirmed structural assumption lists it, warns, and records the event when the user goes on, with the list kept beside it, never refusing; the version's purpose reads proof of concept before the event and working solution at `v1.0`.
  - Src: BP:533. Accept: stage 4 headless H66. Test: the run. Builds on C159 to C164. See G23 on "before the event".

---


## 3. Shapes

Every block below is copied verbatim from the named file and line; nothing is reworded. Where two sources give the same shape in different words, both are copied under their own anchors and section 4 lists the difference. Field names inside a copied block are the source's, even where the sources disagree.

### 3.1 `record.py status --json`

**RM:139 to 152** (the pinned shape):

````text
One JSON object, the front door's one read and the graders' too; front-matter values come back as the strings they are, computed values as JSON types:

```
{"schema": "status/1", "generated_at": "...", "plugin_version": "0.1.0", "record_schema": "client/2", "migration_needed": false,
 "record": {every client/2 field by name},
 "strands": [{every strand/1 field by name, "qualified_version": "001/v0.1", "open_versions": ["v0.1"], "live_objects": 0,
              "last_activity": "2026-09-12", "run": {"id": "...", "state": "running", "heartbeat_at": "...", "heartbeat_age_minutes": 4}}],
 "lease": {"held": true, "state": "held", "epoch": 7, "strand": "001", "strand_title": "...", "version": "v0.1", "chat_label": "...",
           "surface": "cowork", "run_id": "...", "taken_at": "...", "heartbeat_at": "...", "heartbeat_age_minutes": 22, "fresh": true},
 "interrupted": [{"strand": "001", "run_id": "...", "version": "v0.1"}],
 "findings": {"blocking": [{"file": "...", "field": "...", "problem": "...", "expected": "..."}], "warnings": []}}
```

`run` is null when the strand has no open run. `--strand <id>` returns the same object with one entry in `strands`. `lease.held` is false, with `state` `none`, `released` or `broken` and the last `epoch`, when nothing is held.
````

**BP:123** adds: 

````text
`status --json` is one call returning the shape `record-map.md` pins, the record fields with the build target and the client's workspaces, a `strands[]` array with each strand's version, version state, version purpose and clearance, and the lease block, or one strand with `--strand`;
````

**A§5.4:354** adds:

````text
`status --json` is the front door's one read: record fields, a `strands[]` array (each with `stage`, `clearance`, `version`, `version_state`, `shown`, `signed_off`) and the lease block, or one strand with `--strand`; its shape is pinned in `record-map.md`, because four skills and the graders read it.
````

### 3.2 The strand index

**RM:87 to 92**:

````text
The strand index is one table with this header line and one row per strand; `record.py check` compares it with the folders on disk and blocks on a difference:

```
| strand | title | kind | state | version | version state | verdict | SOP behind | live objects | last activity |
| 001 | Service desk intake | platform | active | v0.1 | approved | nearly-ready | no | 0 | 2026-09-12 |
```
````

**A§7.2:481** (the index is a body block of `CLIENT.md`, owner engagement):

````text
**strand index** (engagement), one row per strand with short id, title, kind, state, version and version state, **clearance**, live object count and last activity, which is how the record shows several strands at once;
````

### 3.3 `lock/2`, its history entry and its two mirrors

**RM:133 to 135**:

````text
Written only by the lease primitives in `mmb_common.py`, which `record.py lease` and `ledger.py` call; a take, a refresh, a release and a break are state changes and the file is never deleted. Fields: `schema`, `kind` (`build`), `epoch` (an integer, `0` before the first take, incremented on every take and every break), `strand`, `strand_title`, `version`, `run_id`, `chat_label`, `surface`, `taken_at`, `heartbeat_at`, `state` (`none` | `held` | `released` | `broken`), `history[]`. A heartbeat older than 60 minutes reads stale; nothing expires on its own. A history entry is appended on a take, a release, a break and a park, never on a refresh: `{event, at, epoch, strand, version, chat_label, run_id, by, choice, reconcile, note}` with `event` `taken` | `released` | `broken` | `parked`, `by` the chat label acting, `choice` `resume` | `park` on a break and null otherwise, and `reconcile` the classify-only summary on a break. The two mirrors, `lease` in `CLIENT.md` and `account.json.guard_index.lease`, are written in the same call, and `record.py check` blocks when either disagrees with the lock.
````

**A§9.8:933** (field list, fence and label, as ARCHITECTURE states them):

````text
**One exclusive `build` lease per record**, in `.work/lock.json` (schema `lock/2`), taken by a strand and holding `kind`, `epoch`, `strand`, `strand_title`, `version`, `run_id`, `session_label`, `taken_at`, `heartbeat_at` and `state`, with a `history` list that is retained rather than deleted, because the audit's independence check reads it (3.8) and because a break must be reconstructable afterwards. `epoch` is a fence token: it increments on every take and every break, it is stamped into the holding strand's `build.json` as `lease_epoch_at_run`, and `ledger.py` refuses any account-affecting write whose `--lease-epoch` does not match the current lock, so a session that was presumed dead and wakes up cannot write. **Session identity** is minted, not inferred: `record.py lease take` builds the session label from a timestamp and a short random suffix, returns it, and `refresh`, `release`, `break` and every fenced ledger write present it beside the epoch; a missing or different label is another session.
````

**Mirror 1, `CLIENT.md` `lease`.** A§7.2:468:

````text
lease: "none"                          # mirrors .work/lock.json: "none", or "001 v0.1 (build v0.1 Tue)"
````

RM:100 (fragment):

````text
`lease` (`"none"`, or `<strand> <version> (<chat label>)` mirroring the lock; a disagreement is blocking)
````

**Mirror 2, `account.json` `guard_index.lease`.** A§7.3:524:

````text
                  "lease": {"strand": "001", "epoch": 7, "session_label": "build v0.1 Tue", "heartbeat_at": "..."},
````

A§7.3:537 (fragment):

````text
`guard_index.lease` mirrors `.work/lock.json` so a hook can read the holder and the epoch from the same file it already reads for the native index; that one block is written by the lease primitives in `mmb_common.py`, not by `ledger.py` (5.4, 9.8), and `record.py check` blocks when it disagrees with the lock.
````

RM:116 (fragment):

````text
`lease {strand, epoch, chat_label, heartbeat_at}` (the mirror the lease primitives write; `strand` null when none is held)
````

### 3.4 `CLIENT.md` and `STRAND.md` front matter

**`client/2`, A§7.2:447 to 477:**

````text
```yaml
---
schema: "client/2"
slug: "acme-logistics"
name: "Acme Logistics"
account_kind: "own"                    # own | client | sandbox: mirrors build_target
build_target: "own-account"            # own-account | client-account, chosen at setup (A21); "none" on a sandbox record
monday_account_id: "unbound"
monday_account_slug: "unbound"
monday_bound_user_id: "unbound"
monday_bound_at: "unbound"
monday_tier: "unknown"                 # as read at the last preflight
monday_tier_read_at: "never"           # the tier is only as good as its date
monday_tier_source: "unknown"          # preflight | client statement | unread
products_in_scope: "core,crm"          # core | crm | service; the union across open strands
client_workspaces: "none"              # per product once created, "core:10000001;crm:10000002"; mirrors account.json (A21)
record_state: "active"                 # active | closing | closed
strands_open: "1"
strands_total: "1"
current_strand: "001"                  # the strand a new session defaults to; may be "none"
live_build: "no"                       # yes once anything of ours is live in this account; drives the prior-build reads (7.8)
lease: "none"                          # mirrors .work/lock.json: "none", or "001 v0.1 (build v0.1 Tue)"
last_input: "none"                     # the newest call, document or email
last_researched: "never"
transcripts_at_close: "unanswered"     # open (A11-3): exclude | archive, asked before the first real input is saved; record level, asked once per client
transcript_redaction: "unanswered"     # open (A11-3): none | offered-per-call | always, asked at the same moment
sample_data_in_account: "unanswered"   # open (A11-2): unanswered | allowed | not-allowed | not-needed; ships "unanswered"; asked before the first build in a client's account that plans sample rows; the bind step sets "not-needed" when build_target is own-account
ai_notice: "not-yet"                   # given YYYY-MM-DD | not-yet | not-needed
updated: "2026-10-13T09:10"
---
```
````

**`client/2`, RM:100** (the stage-1 field list; differs, see G15):

````text
Identity: `slug`, `name`, `account_kind` (`client` | `sandbox`). Binding, each `"unbound"` until `ledger.py bind` writes `account.json.account` and mirrors it here, a difference being blocking: `monday_account_id`, `monday_account_slug`, `monday_bound_user_id`, `monday_bound_at`. Tier: `monday_tier` (`"unknown"` until read), `monday_tier_read_at` (`"never"` until read), `monday_tier_source` (`preflight` | `client statement` | `unread`). Scope and state: `products_in_scope` (comma-joined from `core`, `crm`, `service`, the union across open strands), `record_state` (`active` | `closing` | `closed`), `strands_open`, `strands_total`, `current_strand` (a short id or `"none"`), `live_build` (`"no"` until anything of ours is live), `lease` (`"none"`, or `<strand> <version> (<chat label>)` mirroring the lock; a disagreement is blocking). Activity: `last_call` (`"none"` or a date), `last_researched` (`"never"` or a date), `updated` (ISO minute). The three open A11 fields stay at record level, asked once per client at the moment each first matters and never at setup: `transcripts_at_close` (`unanswered` | `exclude` | `archive`) and `transcript_redaction` (`unanswered` | `none` | `offered-per-call` | `always`), asked before the first real transcript or document is saved [A11-3]; `sample_data_in_account` (`unanswered` | `allowed` | `not-allowed`), asked before the first revision in any strand plans sample rows [A11-2]. Then `page_size` (`unset` | `letter` | `a4`, asked at the first export) and `ai_notice` (`not-yet` | `not-needed` | `given YYYY-MM-DD`). `record.py check` blocks on an A11 field left `unanswered` at the moment it matters — a build proposed in any strand, the first non-fixture transcript or document, a record bound for write probes [A11-1] — and is silent otherwise; it never fills one in.
````

**`strand/1`, A§7.7:651 to 676:**

````text
```yaml
---
schema: "strand/1"
strand: "001"
slug: "001-service-desk"
title: "Service desk intake"
kind: "platform"                       # platform | non-platform | hybrid
output_class: "configured-structure"   # configured-structure | bespoke-code | hybrid
opened: "2026-10-12"
opened_reason: "new queue raised on the 2026-10-10 call"
state: "active"                        # active | paused | closed
stage: "readiness"                     # platform and hybrid: new | intake | readiness | blueprint | building | audited | shown | signed-off | closing | closed
                                       # non-platform: new | scoping | handed-off | closed
version: "none"
version_state: "none"                  # planned | approved | building | built | fixing | audited | released; always "none" on a non-platform strand
clearance: "none"                      # none | cleared to build | cleared to build, generic | not yet (3.3)
override: "none"                       # none, or the date and reason the user built past a "not yet"
round: "none"                          # one | two: which round the open version is (D4)
workspaces: "none"                     # this strand's build-target workspaces per product once created (A21)
next_step: "readiness check after the 2026-10-10 call is taken in"
depends_on: "none"                     # other strands whose live objects this one reads or changes
summary_current_to: "none"             # the version SUMMARY.md was last written against
closed: "none"
updated: "2026-10-12T09:10"
---
```
````

**`strand/1`, RM:104** (the stage-1 field list; differs, see G16):

````text
`strand` (short id), `slug` (full id), `title`, `kind` (`platform` | `non-platform` | `hybrid`), `output_class` (`configured-structure` | `bespoke-code` | `hybrid`), `opened`, `opened_reason`, `state` (`active` | `paused` | `closed`), `stage` (platform and hybrid: `new` | `discovery` | `blueprint` | `building` | `demo` | `signed-off` | `expanding` | `closing` | `closed`; non-platform: `new` | `scoping` | `handed-off` | `closed`), `version` (`"none"` or `"v0.1"`), `version_state` (`none` or a state of the table below; always `none` on a non-platform strand), `discovery_verdict` (`not-graded` | `not-ready` | `nearly-ready` | `complete`; a v2 grading list, kept for the shape, while in v1 the clearance is `readiness.md`'s `verdict.cleared_for`, pinned below), `sop_behind` (`yes` | `no`), `next_step` (date, time, what, and `(owner: the user)` or another role), `depends_on` (`none` or short ids), `summary_current_to` (`none` or a version), `closed` (`none` or a date), `updated`. Kind is set at `record.py strand open` from the user's answer and recorded with its reason, and changed only through `record.py strand kind` while the strand has no versions, with a `strand` log entry. `non-platform` means work outside monday — an application, a script, an integration against a third-party system — recorded and handed off, never designed or built (A13 as narrowed by A17). `hybrid` carries both `blueprint.md` and `scope.md`, the boundary line in each and no element in both.
````

**Which command reads or writes which field.** The sources state only the rows marked *stated*; the rest is the reading a builder would need, marked *inferred*, and G06, G43 and G52 ask for it to be decided.

| Field (file) | Command | Reads or writes | Basis |
|---|---|---|---|
| `lease` (`CLIENT.md`) | lease primitives | writes, in the same call as the lock | stated: BP:123, A§9.8:933 |
| `lease` (`CLIENT.md`) | `check` | reads, blocks on disagreement | stated: BP:123 |
| `monday_account_id`, `monday_account_slug`, `monday_bound_user_id`, `monday_bound_at`, `build_target` (`CLIENT.md`) | `check` | reads, against `account.json` | stated: BP:123, A§5.4:354 |
| `transcripts_at_close`, `transcript_redaction`, `sample_data_in_account` (`CLIENT.md`) | `init` | writes as `unanswered` | stated: BP:198, A§7.2:471 to 473 |
| the same three | `check` | reads, blocks at the moment it matters | stated: BP:123, BP:23 |
| `schema` (every file) | every writing subcommand | reads, refuses when newer | stated: BP:123 |
| `kind`, `opened_reason` (`STRAND.md`) | `strand open`, `strand kind` | writes | stated: BP:123, A§7.7:682 |
| `state` (`STRAND.md`) | `strand pause`, `strand close`, `lease break` (park) | writes `paused`, `closed`, `paused` | stated: BP:123, A§7.7:686, A§9.8:945 |
| `closed` (`STRAND.md`) | `strand close` | writes | stated: A§8.10:828 |
| `summary_current_to` (`STRAND.md`, `SUMMARY.md`) | `strand summary`, `version release` | writes | stated: A§7.7:684 |
| `stage` (`STRAND.md`) | `version mark` | writes | stated: A§7.7:680 |
| `clearance` (`STRAND.md`) | `strand open` | writes `none` | stated: A§7.7:666, BP:123 |
| `clearance` (`readiness.md`) | `strand open`, `check` | writes `none`, reads | stated: BP:123 (field name: G28) |
| `version`, `version_state` (`STRAND.md`) | `version open`, `version release` | writes | inferred |
| `strands_open`, `strands_total`, `current_strand`, `record_state` and the strand index (`CLIENT.md`) | `strand open`, `strand close`, `strand pause` | writes | inferred; owner is engagement in RM:85, see G06 |
| `last_input` (`CLIENT.md`) | `add-transcript`, `add-document` | writes | inferred |
| `updated` (both files) | every writing subcommand | writes | inferred |

### 3.5 The log: file header, entry header and types

**A§7.6:632 to 645:**

````text
```markdown
---
schema: "log/1"
client: "acme-logistics"
---
# Log: Acme Logistics
Newest first. One entry per event. Entries are never edited; a correction is a new entry naming the one it corrects.

## 2026-10-15 15:40 · 001 · automation · v0.1 · A1
Approved in session: "yes to all". Card: account 1234567, board Jobs 11000000006, trigger Status to Done, recipient the dispatch lead (user 20000002).

Header: `## YYYY-MM-DD HH:MM · <strand or -> · <type> · <version or -> · <key or session label>`, then at most five lines. The strand position carries the short id, or `-` for a record-level event (a binding, a research pass, a lease break, a record close); the version is bare because the strand position already qualifies it. Types: `created`, `binding`, `workspace` (a client workspace created or continued, A21), `research`, `call`, `document`, `email`, `conflict`, `readiness`, `override`, `superseded` (only where both figures concern the same commitment, from the same speaker, inside one call; any other pair is a `conflict`, and no arithmetic runs between the two), `scope`, `blueprint`, `approval`, `change-check`, `preflight`, `build`, `departure`, `irreversible`, `automation`, `workflow`, `agent`, `ai-column`, `vibe`, `sequence`, `webhook`, `write-failed`, `recovery`, `audit`, `write-detected`, `shown`, `signed-off`, `lint`, `version`, `release`, `strand` (opened, paused, closed), `lease` (taken, released, broken, parked), `live-map` (a constraint set or changed), `summary` (a strand summary written or refreshed), `api-surprise`, `decision` (including the user's approval of the assumptions on a card and a corrected call type, A25, A27), `commitment`, `closeout`, `archive` (the manifest, the move of the client folder into `archive/<slug>/` and its check, with the GitHub archive as well when chosen, A26). Only `record.py log` writes entries: it re-reads the file and inserts under the header, so two sessions never overwrite each other, and `check` proves nothing below the new entries changed. There is one record-wide log; at a strand close that strand's entries below the live part move to `strands/<id>/log.md` as a snapshot, leaving one pointer entry behind, and `check` verifies the roll by hashing the moved entries so "history only grows" survives the roll.
````

**RM:160 to 166** (the stage-1 text; the type list differs, see G45):

````text
`log.md` (`log/1`, front matter `schema` and `client`) is one record-wide history, newest first, entries never edited, written only by `record.py log`, which re-reads the file and inserts under the header. An entry is this header line, then at most five lines:

```
## YYYY-MM-DD HH:MM · <strand or -> · <type> · <version or -> · <key or chat label>
```

The strand position is the short id, or `-` for a record-level event (a binding, a research pass, a lease break, a record close); the version is bare because the strand position qualifies it. Types: `created`, `binding`, `research`, `call`, `document`, `conflict`, `discovery`, `override`, `superseded` (only the same commitment from the same speaker inside one call; any other pair is a `conflict`, with no arithmetic between the two), `scope`, `blueprint`, `approval`, `change-check`, `preflight`, `build`, `departure`, `irreversible`, `automation`, `write-failed`, `recovery`, `audit`, `write-detected`, `demo`, `sop`, `export`, `doc-copy`, `deliverable`, `sent`, `lint`, `version`, `release`, `strand`, `lease`, `live-map`, `summary`, `api-surprise`, `decision`, `commitment`, `migration`, `closeout`, `archive`. At a strand close that strand's entries below the live part move to `strands/<id>/log.md` with one pointer entry left behind, and `check` verifies the roll by hashing the moved entries.
````

### 3.6 Version states, the two events, purpose, and the files each state requires

**A§7.4:585 to 587** (purpose):

````text
`version.md` carries `strand`, `qualified_version` and `purpose` (`proof-of-concept` or `working-solution`, A25) in its front matter. The record has no version counter of its own: the strand index in `CLIENT.md` shows every strand's version and state at once, `record.py status --json` returns them, and wherever a session needs one version (the build door, the audit door, the release) it takes the strand from the command or from `current_strand` and the version from that strand. A `non-platform` strand has no versions at all (7.9).
````

````text
**A version carries its purpose (A25):** every `v0.x` is a proof of concept, which may rest on assumptions the user approved as long as they stay visibly unconfirmed, and from `v1.0` a version is a working solution, whose structural assumptions are confirmed or explicitly accepted before production use. `v1.0` means the client has signed off the build as their working system: an event the user records, reporting what the client said, since the plugin never deals with the client directly. Recording it lists every structural assumption not yet confirmed or accepted, as a warning; it does not block, and the user records the event anyway if they choose. A completely different direction from the client is not a new version; it is a fresh strand with fresh workspaces, and the old ones are kept (8.9, A21).
````

**A§7.4:589 to 594** (the ladder and the events):

````text
planned ─approve→ approved ─run→ building ─all verified or departed→ built ─audit pass→ audited ─release→ released
                                    ▲                                   │
                                    └────────────── fixing ←─audit fail─┘
events the user records on an audited or released version: shown (date, audience by role), signed-off (date, who by role, the unconfirmed structural assumptions listed at that moment)
````

**A§7.4:596 to 606** (required files per state, checked by `record.py check`):

````text
Paths below are relative to the strand folder.

| State | Entered when | Files that must exist (checked by `record.py check`) |
|---|---|---|
| `planned` | a blueprint revision targets this version | `solution/blueprint.md`, `versions/<v>/version.md` with scope and revision |
| `approved` | the user's unhedged yes is recorded | `blueprint-r<N>.md` whose sha256 matches `version.md` and `build.json.approvals`; an approval entry in `log.md` |
| `building` | the change check and preflight have passed and the first write is about to run; the `runs[]` entry and the lease are taken earlier, at step 11, and the state stays `approved` until then | a `runs[]` entry in state `running` carrying the lease epoch and the answer to the one question, `.work/lock.json` held by this strand, `change_check` in `account.json` for this strand and `preflight` present |
| `built` | every in-scope element is verified, departed or a listed UI step | the build section of `version.md` (departures, UI steps, surprises, calls estimated and used); a build log entry |
| `fixing` | an audit leaves an open blocker or major finding | `audit.md` with findings |
| `audited` | an audit with valid write detection ends `cleared to show`, or ends `not cleared to show` and the user accepted every open finding with a reason | `audit.md` with the write-detection result, the documents appendix and the closing line |
| `released` | the release step completes | frozen `build.json`, `backlog.md`, `log.md`; condensed current files; for `v1.0` the `signed-off` event recorded. Missing files block the release |
````

**A§7.4:608** (events):

````text
**Events.** `shown` and `signed-off` are not states; `record.py version mark` records each with its date and the audience by role, and `version.md` keeps them with the client's reactions and confirmations per pain, which `call-intake` writes from the next call (3.2). A version may be `shown` more than once. Nothing in the plugin can observe a demo, so the user is the one who records it (D2). The `signed-off` record also keeps the list of structural assumptions the warning showed, so a working solution never carries an assumption as if it were a fact (A25).
````

**RM:154 to 156** (the stage-1 text; has `demoed`, see G17):

````text
Per strand; a `non-platform` strand has none. `planned` → `approved` → `building` → `built` → `audited` → `demoed` → `released`, with `fixing` between an audit that fails and the retry. The files `record.py check` requires, relative to the strand: `planned`, `solution/blueprint.md` and `versions/<v>/version.md` with scope and revision; `approved`, a `blueprint-r<N>.md` whose sha256 matches `version.md` and `build.json.approvals`, and an `approval` log entry; `building`, a `runs[]` entry in `running` carrying the lease epoch, the lock held by this strand, `change_check` in `account.json` for this strand and `preflight` present; `built`, the build section of `version.md` and a `build` log entry; `fixing`, `audit.md` with findings; `audited`, `audit.md` with the write-detection result and the documents appendix; `demoed`, the frozen `demo-script.md`, the demo call summary and the reactions in `version.md`; `released`, the frozen `build.json`, `backlog.md`, `log.md` and `updates.md`, the condensed current files and, for v1.0, a sign-off block. A missing file blocks the release; `presented` in `export.md` is accepted for a v0.x export and blocks v1.0.
````

**BP:198 (fragment)**, the `version.md` front matter as WP7 ships it:

````text
`version.md` front matter carries `strand`, `qualified_version`, state, revision, sha, the version's purpose (proof of concept until sign-off, working solution from `v1.0`), and the events `shown` and `signed-off` with their dates, `signed-off` keeping the list of structural assumptions not yet confirmed or accepted that its warning showed (D21, A25), and its body has the reactions block the confirmation ledger lands in;
````

### 3.7 Readiness clearance strings, `none`, and the fixed hand-off sentence

**BP:64 (fragment):**

````text
the three clearance strings, `cleared to build`, `cleared to build, generic` and `not yet`, beside the audit's closing line, `cleared to show` or `not cleared to show`, with the grading values of the former discovery file fenced off as v2 (D1, D2,
````

**RM:212** (`readiness/1`, the machine values and the human strings; `none`):

````text
`cleared_for` is the machine value; the check says it to the user as a human string, and `STRAND.md` and the approval card carry the string. `build` is `cleared to build`: at least one pain with an entity and a wanted outcome, the product chosen, the structure stated with its leanings, the build target named. `build-generic` is `cleared to build, generic`: the same, with the structure resting mostly on assumptions; the build goes ahead as a generalised version, the assumptions list is the agenda for the next contact, and the approval card's "what this build rests on" section is the user's yes to them. `not-yet` is `not yet`: no pain or entity firm enough to build on; the questions are the next step. A fresh `readiness.md`, before the check has run, carries `none`, which is never a result of the check. solution-blueprint reads the machine value, and `not-yet` or `none` stops the blueprint unless the user overrides with a reason, logged as `override` (plan decisions D1 and D2). No grade, R-number, gate name or sales verdict appears in the block; those lists are v2 and are tagged so above.
````

**A§7.7:666** (`STRAND.md`):

````text
clearance: "none"                      # none | cleared to build | cleared to build, generic | not yet (3.3)
````

**A§5.4:354 (fragment)** (what `check` looks for):

````text
that `readiness.md` carries one of the three clearance strings or `none`, which means the check has not run yet and is distinct from the check's own `not-yet` (readiness spec section 7),
````

**The fixed hand-off sentence.** RM:110 (verbatim) and A§7.9:725:

````text
> Building this work happens outside this product. This record holds its scope, open questions, dependencies, access needs and next steps; it does not design or build it.
````

````text
*"Building this work happens outside this product. This record holds its scope, open questions, dependencies, access needs and next steps; it does not design or build it."*
````

### 3.8 Exit codes

**A§5.3:343:**

````text
- Exit codes: 0 ok, 1 blocking findings, 2 warnings only, 3 could not run. Every message names file, field, problem and expected value.
````

### 3.9 Session label format and the stale-heartbeat threshold

**BP:123 (fragments):**

````text
**mints and returns the session label** (timestamp and a short random suffix; two takes on one day never collide) which `refresh`, `release` and `break` then require,

and reads a heartbeat older than 60 minutes as stale;
````

**A§9.8:933 (fragment):**

````text
**Session identity** is minted, not inferred: `record.py lease take` builds the session label from a timestamp and a short random suffix, returns it, and `refresh`, `release`, `break` and every fenced ledger write present it beside the epoch; a missing or different label is another session.
````

**A§9.8:939 (fragment, the example label in the briefing line):**

````text
interrupted-work line reads "strand 002 is waiting: strand 001 (Service desk intake) holds the build lease for v0.1, taken 13:30, last heartbeat 13:52 in session 'build v0.1 Tue'";
````

**A§9.8:943 (fragment):**

````text
a heartbeat older than 60 minutes is stale. Nothing expires on its own: a stale lease stays held until someone breaks it, and the briefing keeps saying so, because the account may hold half-written objects and silence would be worse than a stuck lease.
````

**RM:77 (fragment, the stage-1 format):**

````text
**Chat label**: minted by `record.py lease take` as `<surface>-<YYYYMMDD-HHMM>-<four random characters>`, surface `cowork` or `claude-code`, for example `cowork-20260915-1330-k7q2`; two takes on one day never collide.
````

### 3.10 The five conditions for breaking a lease, and what a break records

**A§9.8:945** (verbatim; the five conditions are the colon-list in the first sentence):

````text
**Breaking one safely.** `record.py lease break` is refused unless all five hold: the heartbeat is stale; the user says yes in this session naming the holding strand, and prose about "clearing the lock" is not a yes; an account check passes, so the break happens in the right account; recovery runs first **over the holder's strand, not the taker's**, in classify-only mode (8.11), adopting, retrying and archiving nothing; and the user chooses what happens to the interrupted run, recorded in both strands' logs. The choice is **resume it first** (the default the product recommends: the lease is handed to a fresh session for the holding strand, which runs the ordinary recovery and finishes or departs each element) or **park it** (the holder's run stays `interrupted`, its unverified elements stay `attempting`, the strand goes to `paused` with what is unresolved written into its `STRAND.md`, and the taker takes the lease with a new epoch). Parking needs its own yes and is refused when the holder's reconcile found any element in the `duplicate` or `partial` class, because those are exactly the states a second builder can make unrecoverable. Breaking writes a `lease` log entry at record level with the broken epoch, the holder, the reconcile summary and the user's choice; the new holder starts at `epoch + 1`, and the old session, if it ever wakes, is refused by the fence token at its first ledger write and told why.
````

### 3.11 Size budgets `check` warns on

Budgets are warnings from `record.py check` unless marked blocking (A§7.1:378). **A§7.1:384 to 402, record level:**

````text
| Path | Kind | Written by | Budget | Client-facing | Archived |
|---|---|---|---|---|---|
| `CLIENT.md` | current | engagement, plus one block per skill | 160 lines, 10 KB | no | yes |
| `log.md` | history | all, through `record.py log`; every entry carries a strand field | live part 300 lines; rolls at each release and each strand close | no | yes |
| `meetings.md` | history | call-intake; engagement for a meeting never ingested | 150 lines | no | yes |
| `account.json` | machine, current | `ledger.py` only | must pass `ledger.py check` | no | yes |
| `research/sources.md` | history | engagement | none | no | yes |
| `research/<date>-brief.md`, `-deep-dive.md` | snapshot | engagement, through `research-scout` (D14) | 80 / 200 lines | no | yes |
| `research/updates.md` | history | engagement | live part 150 lines | no | yes |
| `calls/<date>-<type>.transcript.txt` | raw, sha recorded | call-intake | none | no | per `transcripts_at_close`, which is **open with no default** (A11-3, section 13) |
| `calls/<date>-<type>.md` | snapshot | call-intake | 120 lines | the marked client-safe block only | yes |
| `inputs/<date>-<title>.<ext>` | raw, sha recorded | call-intake, through `record.py add-document`: a client document (A16) or an email as pasted text or a screenshot saved as an image (an attachment only when the user adds it as its own input) | none | no | per `transcripts_at_close`, **open with no default** (A11-3): the retention question covers documents and emails as well as transcripts |
| `inputs/<date>-<title>.md` | snapshot | call-intake, from `document-summary.md` | 120 lines | the marked client-safe block only | yes |
| `live/live-map.md` | current | `ledger.py live-map` at the end of a run; client-closeout at a strand close | 250 lines, 16 KB; blocking at 400, which means the map needs grouping by strand | no | yes |
| `live/snapshots/<date>-<strand>.json` | machine | `ledger.py` | none | no | yes |
| `client-card.md`, `archive-handoff.md` | current, snapshot | client-closeout, record level | 1 page, 60 lines | no | yes |
| `.work/` | scratch | scripts | none | no | never |
| `.gitignore` | current | engagement at init, on the GitHub archive path only (A26) | none | no | yes |
| `CLAUDE.md` (the client folder's own instruction file, 8.2) | current | engagement at init | 10 lines | no | yes |
````

**A§7.1:406 to 427, strand level:**

````text
| Path | Kind | Written by | Budget | Client-facing | Archived |
|---|---|---|---|---|---|
| `STRAND.md` | current | engagement, plus one block per skill | 120 lines | no | yes |
| `SUMMARY.md` | current | `record.py strand summary`, with the user's yes | 80 lines; blocking at 120 | no | yes |
| `readiness.md` | current | build-readiness (3.3) | 250 lines | no | yes |
| `solution/blueprint.md` | current | solution-blueprint | 400 lines | no; its glossary and names are written for the client, nothing in it is sent | yes; absent on a `non-platform` strand |
| `solution/scope.md` | current | solution-blueprint, on `non-platform` and `hybrid` strands only (7.9) | 200 lines | the sections marked hand-off are what the user passes on | yes |
| `solution/backlog.md` | current | solution-blueprint; call-intake inserts under Incoming | 150 lines | no | yes |
| `solution/allowlist.md` | current | solution-blueprint, with the user's OK per row | 80 lines | no | yes |
| `solution/exclusions.md` | current | engagement seeds it at new client; the user and call-intake add rows when a client says something must not appear; solution-blueprint, the sample-data step and the lint read it | 80 lines | no | yes |
| `solution/build.json` | machine, current | `ledger.py` only | must pass `ledger.py check` | no | yes; absent on a `non-platform` strand |
| `solution/open-questions.md` | current | build-readiness; call-intake inserts, solution-blueprint inserts a fork (8.5 step 7) and marks `bypassed` | 150 lines | no | yes |
| `solution/dependencies.md` | current | solution-blueprint; call-intake inserts on a scoping or working-session call (8.3 step 7) | 120 lines | no | yes |
| `solution/structure-inventory.md` | current | call-intake after a reverse demo or prototype review; build-readiness reads it | 200 lines | no | yes |
| `versions/<v>/version.md` | current while open, snapshot at release | engagement, build, audit, intake (own sections) | 150 lines | no | yes |
| `versions/<v>/blueprint-r<N>.md` | snapshot at approval | `record.py freeze --strand` | none | no | yes |
| `versions/<v>/audit.md`, `audit-2.md` | snapshot | solution-audit | 200 lines | no | yes |
| `versions/<v>/build-notes.md`, `build-notes.html` | snapshot, regenerated per version on `cleared to show` (A23) | solution-audit | 250 lines; the page carries the same text and the two diagrams | no; a client-facing copy only on request, through the lint | yes |
| `versions/<v>/build.json`, `backlog.md`, `log.md` | snapshot at release | `record.py version release --strand` | none | no | yes |
| `drafts/<date>-admin-prerequisites.md` | snapshot | engagement, only when the build target is the client's account | 60 lines | yes, as a draft the user sends | yes |
| `close-out.md` | snapshot | client-closeout, strand level | 60 lines | no | yes |
| `log.md` | snapshot | `record.py strand close`, the strand's rolled history | none | no | yes |
````

**A§7.1:429 (the whole-record budget and the `non-platform` file set):**

````text
A `non-platform` strand has `STRAND.md`, `SUMMARY.md`, `readiness.md`, `solution/scope.md`, `open-questions.md`, `dependencies.md`, `drafts/` and `close-out.md`; nothing under `versions/`, no `blueprint.md`, no `build.json`; `record.py check` blocks on any of those appearing (7.9). Whole record: soft 4 MB excluding `calls/*.transcript.txt`, `inputs/*.<ext>` and `.work/`, reported with the largest strands named.
````

### 3.12 `SUMMARY.md` (`summary/1`)

**A§7.7:684:**

````text
**`SUMMARY.md`** (schema `summary/1`, at most 80 lines, blocking at 120) is the only strand file a later strand reads. Front matter: `strand`, `title`, `kind`, `versions`, `closed`, `summary_current_to`, `budget_lines`. Body, in order: what the work was in two lines and why it opened; the pains it served, one line each in the client's vocabulary with no quote over seven words, because the copied-run and quote-length lint rules apply to it; what was built, as fully qualified element keys to monday ids grouped by workspace and board, each pointing at its live-map row rather than repeating it; what the client confirmed, as pointers to the call summaries holding the quotes, and which assumptions the client confirmed or accepted, as the user reported it, and which are still assumed, so a later strand never reads an assumption as a fact (A25); what must not be broken and where that came from; what the client learned about our cost of change, in their words; ownership and switch-off status at close; open backlog seeds carried forward with the strand that should pick them up if known; and dates opened, shown, signed off, released and closed. For a `non-platform` strand the built-objects block reads "nothing built inside the product" and the hand-off state takes its place. It is written at the first version release and refreshed at every later release and at strand close by `record.py strand summary`, which takes the user's yes to a plan the way the condense step does; between releases it is stale by design and `summary_current_to` says so.
````

**RM:108 (fragment):**

````text
`SUMMARY.md` (`summary/1`): `strand`, `title`, `kind`, `versions`, `closed`, `summary_current_to`, `budget_lines`; then nine blocks in order — what the work was and why it opened; the pains it served, one line each, no quote over seven words; what was built, as qualified keys to monday ids grouped by board, each pointing at its live-map row; what the client confirmed, as pointers to the call summaries; what must not be broken and where that came from; the client's words on our cost of change; ownership and switch-off status at close; backlog seeds carried forward; dates opened, released and closed. On a non-platform strand the built block reads "nothing built inside the product".
````

### 3.13 The A11 fields and their `unanswered` value

**A§7.2:471 to 473:**

````text
transcripts_at_close: "unanswered"     # open (A11-3): exclude | archive, asked before the first real input is saved; record level, asked once per client
transcript_redaction: "unanswered"     # open (A11-3): none | offered-per-call | always, asked at the same moment
sample_data_in_account: "unanswered"   # open (A11-2): unanswered | allowed | not-allowed | not-needed; ships "unanswered"; asked before the first build in a client's account that plans sample rows; the bind step sets "not-needed" when build_target is own-account
````

**RM:100 (fragment):**

````text
The three open A11 fields stay at record level, asked once per client at the moment each first matters and never at setup: `transcripts_at_close` (`unanswered` | `exclude` | `archive`) and `transcript_redaction` (`unanswered` | `none` | `offered-per-call` | `always`), asked before the first real transcript or document is saved [A11-3]; `sample_data_in_account` (`unanswered` | `allowed` | `not-allowed`), asked before the first revision in any strand plans sample rows [A11-2]. Then `page_size` (`unset` | `letter` | `a4`, asked at the first export) and `ai_notice` (`not-yet` | `not-needed` | `given YYYY-MM-DD`). `record.py check` blocks on an A11 field left `unanswered` at the moment it matters — a build proposed in any strand, the first non-fixture transcript or document, a record bound for write probes [A11-1] — and is silent otherwise; it never fills one in.
````

**BP:23 (the mechanical rule):**

````text
- `record.py check` treats an A11 field left at `unanswered` as a **blocking** finding at the moment it matters, when a build in a client's account is proposed in any strand with sample rows planned (A11-2), when the first non-fixture transcript or document is saved (A11-3), when a record is bound for write probes (A11-1), and as silent at every other time. It never fills one in.
````

**BP:19 (fragment, A11-3's shipped value):**

````text
`transcripts_at_close` and `transcript_redaction` ship as `unanswered`, the value A§7.2 gives an open A11 field, not `exclude`.
````

**BP:18 (fragment, A11-2's field):**

````text
the answer is the record-level field `sample_data_in_account` in `CLIENT.md` (A§7.2)
````

### 3.14 The home tree and `local/settings.json`

**A§5.3:345:**

````text
- **One home for everything outside the record (D11).** `mmb_common.py` resolves every out-of-record path from one root, the **home**: `monday-builder` under the user's home directory as the standard library reports it, on Windows and Mac alike, by default, overridden by the `MMB_HOME` environment variable, which the first-run walkthrough records (D12, A24); the walkthrough says how to set the variable on the system it runs on rather than assuming one shell. While the plugin is built and tested this user's value is set locally, outside every project file (A22). Under the home: `clients/<slug>/` (the records, 7.1), `cards/`, `clients-index.json`, `monday-knowledge/` (10.3), `sandbox/` (a folder holding `SANDBOX.md` for sandbox probes), **`archive/`**, the holding folder that keeps each closed client folder, moved there as `archive/<slug>/` and verified against its manifest, and which the user deletes from by hand (8.10, A24, A26), and **`local/`**, the user's own settings, never shipped and never read from the plugin folder: `settings.json` (the firm name and its renderings for the leak list, D24; the default build-target account, A21; optionally the operational workspaces that are never on a shared screen, D22; the archive choice, local by default or GitHub, and the user's GitHub account only when GitHub is chosen, 12.3-17, A26; the home's creation date and the plugin version that wrote it), `sandbox-accounts.txt` (the accounts where write probes may run, same syntax as before, moved out of `shared/`), and `leak-terms.txt` (per-user additions to the shipped denylist). The headless runner sets `MMB_HOME` to a temporary home, so no test run reads or writes the user's real files. The walkthrough warns when a `CLAUDE.md` sits in any folder above `clients/`, because a client session would inherit it (A22).
````

**BP:123 (fragment, `home init`):**

````text
**`home init`** creates the home tree itself (`clients/`, `cards/`, `monday-knowledge/`, `sandbox/`, `archive/`, `local/`), writes `local/settings.json` from the walkthrough's answers (the firm name and its renderings for the leak list, the default build-target account, optionally the operational workspaces that are never on a shared screen, and the archive choice, a local folder by default or a GitHub repository, with the user's GitHub account written only when GitHub is picked, A26), seeds `local/leak-terms.txt` and `local/sandbox-accounts.txt` empty, checks Python and the connector on the system it runs on and reports each, checks the GitHub tool only when the GitHub archive is picked, and asks for no GitHub account otherwise, warns when a `CLAUDE.md` sits in any folder above the clients folder, runs once and again on request, and never overwrites a settings file that exists (A§5.3, D12);
````

### 3.15 Naming, the `non-platform` file set and the `.work/` layout

**A§7.1:441 (naming):**

````text
Naming: slug is lowercase ASCII with hyphens, at most 40 characters, legal suffixes dropped, never renamed; it is the folder name, the folder name under `archive/` after the record close, and, on the GitHub archive path only, the repository name (`client-<slug>`, under the GitHub account in `local/settings.json`, A26). A strand id is `NNN-<topic>`: a zero-padded ordinal assigned by `record.py strand open`, monotonic per record, never reused and never renamed, plus a topic slug of at most 24 lowercase ASCII characters; the ordinal alone (`001`) is the **short id** used in log entries, lease records, element keys and version references, and the full id is the folder name. Dated files are `YYYY-MM-DD-<topic>`, with `-2` for a second the same day. A transcript and its summary share one stem. Versions are quoted strings (`"v0.1"`) and are unambiguous inside a strand; every reference that leaves a strand folder (the live map, `account.json`, a log entry, another strand's change table) is **fully qualified**: a version as `001/v0.1`, an element as `001:B1`. Links are relative only. Workspaces written into monday are named after the client and the product in neutral words, for example "<client> – CRM" and "<client> – Ops", never after the user's firm, the product or the assistant (A21).
````

**A§7.9:723 to 724 (what a `non-platform` strand holds and never has):**

````text
- **What the record holds.** A strand of kind `non-platform` has `STRAND.md`, `SUMMARY.md`, `readiness.md` (its part 6 is where the need is recorded), `solution/scope.md`, `solution/open-questions.md`, `solution/dependencies.md`, `drafts/` and `close-out.md`. `scope.md` (schema `scope/1`, written by `solution-blueprint`, the one skill that turns evidence into a design artifact) carries, in this order: what already exists and who built it; the scope, expressed as a delta where a client-built artefact is inherited (inherited, in scope, client-side change, access unlock); the open technical questions, as pointers into `open-questions.md`; the external dependencies, as pointers into `dependencies.md`; the access needed, with an owner on each side and a state per item; the next steps with owners and dates; and the process rows for human-in-the-loop work, one row per step with system, owner, mode and an acceptance check, including steps outside the platform. The sections marked hand-off are the hand-off content: in v1 the user passes them on themselves, through the lint, and no package is rendered (D15).
- **What it never has.** No `blueprint.md`, no `versions/`, no `build.json`, no build lease, no element kinds, no build stage and no audit. `record.py check` blocks on any of those appearing under a `non-platform` strand; `record.py lease take` refuses the strand; `/account-build` and `/solution-audit` each refuse it with the same short reason (3.7, 3.8); `solution-blueprint` writes `scope.md` and nothing else, no approval card, no freeze; the front door's routing for such a strand names hand-off as the next step and never a door. `STRAND.md` uses the stage ladder `new | scoping | handed-off | closed` and keeps `version: "none"`.
````

**A§7.1:437 (`.work/`):**

````text
`.work/` holds `lock.json` (the record's lease, 9.8), `history.json`, `intake/` (the intake reports, 5.4), `backup/`, and per strand `strands/<id>/` with `backup/`, `live-inventory.json`, `audit/` and `build.json.bak`.
````


---

## 4. Gaps and contradictions

Each entry is something the sources leave unspecified or state two ways, so a coder would have to decide. Nothing here is resolved. Each gives both anchors and the clauses it touches. The entries are grouped by topic under the headings below; the numbers are stable ids and not an order of importance.

### Lease and session identity

- **G01 Session label: key name, format, example.** RM:77, RM:135 and RM:142 to 147 call it `chat_label` and pin `<surface>-<YYYYMMDD-HHMM>-<four random characters>` with surface `cowork` or `claude-code`; A§9.8:933, A§7.3:524 and the `runs[]` row of A§7.3 call it `session_label`; BP:123 says only "timestamp and a short random suffix"; the example label in A§9.8:939 and A§7.2:468 is `build v0.1 Tue`, which has neither shape. The JSON key (it appears in the lock, both mirrors, the status block and `runs[]`), the exact format and whether a label is ever free text are all open. Touches C85, C89, C118.
- **G02 The `lock/2` field list.** RM:135 lists `chat_label` and `surface` among the fields and RM:147 puts `surface` in the status lease block; A§9.8:933 lists `kind`, `epoch`, `strand`, `strand_title`, `version`, `run_id`, `session_label`, `taken_at`, `heartbeat_at`, `state`, `history` with no `surface`. A20 and A24 leave one surface, so `cowork` is no longer a value. Whether `surface` stays, and with which values, is open. The history entry's `by` ("the chat label acting", RM:135) follows G01. Touches C87, C97, C118.
- **G03 Epoch arithmetic, and how many log entries a break writes.** A§9.8:933 says the epoch increments "on every take and every break"; A§9.8:945 says "the new holder starts at epoch + 1" and BP:502 (H35) says "002 holds epoch + 1". A break (plus one) followed by the taker's take (plus one) gives plus two; one combined step gives plus one. The epoch handed to the fresh session in the resume-first case is not stated. On the log: BP:123 and BP:502 say "both strands' logs"; A§9.8:945 says a `lease` entry "at record level"; A§7.6:645 has one record-wide log with a strand position, `-` for a record-level event. One entry at `-`, two (one per strand), or three is open. Touches C108 to C112.
- **G04 How `lease break` learns conditions 2 to 5.** A§9.8:945 and BP:123 name the five conditions; no source gives the interface through which the script learns the user's naming yes, the account check result, the classify-only reconcile summary (and whether it found `duplicate` or `partial`) or the choice. "Prose about clearing the lock is not a yes" cannot be told by a script unless the yes arrives as a structured argument; and the account check needs a monday read that `record.py` cannot make. Touches C103 to C107.
- **G05 What returns a parked strand to `active`.** A§7.7:686 and BP:502 (H35) say a parked strand returns to `active` after a resume in a fresh session; the `record.py` catalogue (A§5.4:354, BP:123) has `strand pause` and no resume or state setter, and the `ledger.py` list (A§5.4:355) has none. Who writes `STRAND.md` `state: "active"`? Touches C177.
- **G48 Severity of a stale lease in `check`.** BP:448 lists a stale lease among the broken records and H20 (BP:487) passes only if `check` names the defects; A§9.8:943 says a stale lease stays held and the briefing keeps saying so. A held lease is legitimate state, and a blocking finding would make a record with an interrupted run unreleasable in the state recovery runs in. Block, warn, or list in `status` only is open. Touches C153.
- **G50 `lease take` inputs and `run_id`.** BP:248 gives `record.py lease take build --strand` returning the epoch and the label; A§7.4:602 says the lease is taken before the `runs[]` entry exists; the lock has a `run_id` field and the fence checks it (A§9.8:933). Where `run_id` enters the lock (at the take, a later refresh by `run start`, or a separate primitive) is open, as are the sources of `version` and `strand_title` (flags or `STRAND.md`).
- **G51 The fence comparison.** BP:68, BP:134 and A§9.8:933 have `ledger.py` refuse a write whose epoch, label or run id differs from the lock; BP:123 lists only take, refresh, release and break as primitives. Whether `mmb_common.py` also exposes the three-part comparison (one implementation) or `ledger.py` reads the lock itself (reads are not exclusive) is open; H35 depends on it. Touches C113.
- **G52 `strand pause`.** BP:123 says it "exists and is exercised"; A§7.7:686 says it is set by the user, or by a break that parks, with "what is unresolved" written into `STRAND.md`. Its arguments, whether it refuses a strand that holds the lease, and its log entry are not stated. Touches C71, C112.
- **G53 Lease transitions not covered.** Not stated: a `take` by a session that already holds the lease for the same strand; a `take` while the state is `released`, `broken` or `none` (A§9.8:941 implies it is allowed); a `release` of a released lease; a `refresh` of a lease not held; a `take` for a `hybrid` strand (A§7.9:724 and BP:123 refuse only `non-platform`). Touches C91 to C98.

### Strands and the log

- **G06 Who writes the strand index and the counters.** RM:85 and A§7.1:386 give the `CLIENT.md` strand index to engagement and the counters (`strands_open`, `strands_total`, `current_strand`, `record_state`) to no named script; BP:123 makes `check` block when the index disagrees with the folders on disk; A§8.10:828 has the strand close "update the strand index". Whether `strand open|pause|close` update the index and the counters, or engagement does it later (leaving a window in which `check` blocks), is open. Touches C68, C128.
- **G07 What `strand close` does itself.** BP:123 lists three refusals and the log roll; A§8.10:828 adds a fourth refusal (an unreleased version with no recorded close reason), the ownership record, `close-out.md`, a `SUMMARY.md` refresh, `live-map set`, `prior_builds`, `state: closed`, `closed:` and the index; BP:296 gives most of those to `client-closeout`. Which of the extras `record.py` does, and where a version's close reason lives (neither BP:198 nor RM:112 lists a field for it), is open. Touches C77, C78.
- **G08 Log roll and the proof that history only grew.** A§7.6:645 moves "that strand's entries below the live part"; BP:123 says "rolls that strand's log entries out"; A§7.1:387 gives the live part as 300 lines. Open: whether every entry of the strand moves or only those past the live part; where the hashes of moved entries are recorded (the pointer entry, the strand log's front matter, or `.work/history.json`, which A§7.1:437 names and no source defines); what the hash covers (entry text with line endings normalised or raw); the pointer entry's type. "History only grew" (A§5.4:354) needs a stored baseline for entries below the new ones, which is the same question. Touches C53, C73, C137.
- **G43 What `strand open` writes.** BP:123 names `readiness.md` and `exclusions.md`; the strand also needs `STRAND.md` (A§7.7:651 to 676), its folders, and values for `output_class` (A§7.7:682 says kind is "proposed from the input" and output class is "the same distinction seen from the deliverable's side"), `opened`, `workspaces`. Which values are defaults and which come from the caller is open. Touches C65, C68.
- **G45 `log` input validation and the type list.** A§7.6:645's type list differs from RM:166: RM has `discovery`, `demo`, `sop`, `export`, `doc-copy`, `deliverable`, `sent` and `migration` (dropped by D8), and lacks `workspace`, `email`, `readiness`, `shown`, `signed-off`, `workflow`, `agent`, `ai-column`, `vibe`, `sequence`, `webhook`. Neither source says whether an unlisted type, or a body over five lines, is refused. Touches C50, C51.
- **G54 Computed values in `status --json`.** RM:144 to 145 names `open_versions`, `live_objects`, `last_activity` and `run` with no definition: which versions count as open, what `live_objects` counts, where `last_activity` comes from (newest entry for the strand in the log, or file times), and which run is "open". Touches C116, C119.
- **G56 Ordinal source and name validation.** BP:123 and A§7.1:441 say the ordinal is monotonic and never reused; the counter's source (highest folder under `strands/`, `strands_total` in `CLIENT.md`, or the log) is not stated, and the two can disagree. A§7.1:441 states the slug and topic rules (40 and 24 lowercase ASCII characters) without saying that `init` or `strand open` refuse a breach. Touches C44, C63, C64.

### Cross-system behaviour and storage

- **G09 Concurrency mechanism versus the no-delete rule.** BP:123 needs two concurrent `log` inserts to both survive and `lease take` to refuse a second taker; A§5.3:341 and BP:123 forbid rename and delete and require in-place overwrite. A re-read followed by an insert is not atomic across processes; a lock needs different primitives on Windows and POSIX, and an exclusive-create lock file would have to be removed or reused, which meets the no-delete rule. The mechanism is not named. Touches C52, C92, C93.
- **G10 Exit codes of refusals.** A§5.3:343 states 0, 1, 2, 3 as "ok, blocking findings, warnings only, could not run"; BP:123 adds only "as specified". What a refusal returns (stale sha, lease held, `non-platform` strand, newer schema, release with missing files, a close refusal), and what `status --json` returns when findings are blocking, is open. Touches C20 and every refusal clause.
- **G11 Line ending written, and the raw-file rule.** BP:123 says text is "written with one" line ending and does not name it; A§7.1:378 says raw files are "saved once, never edited" and BP:123 says add-transcript "record a sha256". A CRLF transcript saved unchanged hashes differently from the same text saved on the other system; normalising edits a raw file. Whether current files keep an existing ending or are rewritten to the one ending is also open. Touches C09, C10, C60.
- **G36 Invocation form and finding the plugin.** A§5.2:336 says "WP2 fixes the one form both share" after the stage-0 Windows re-run settles the spelling; that re-run lands in stage 5 (BP:80 to 84) and WP2 is stage 2 (BP:62). How the scripts find `plugin.json` for `plugin_version` (A§5.4:354), and the plugin's templates, when the plugin root is a per-session copy (A§5.1:332), is open. Touches C22, C24, C66.
- **G38 Front matter details.** BP:123 says only "quotes preserved". A§7.2:447 to 477 and A§7.7:651 to 676 show trailing `# comment` text on value lines, and BP:198 says the templates' comments carry the stage ladders and the "re-run after every new input" note. Whether comments survive a rewrite, how an embedded `"` or backslash is escaped, where a new key is placed, whether unknown keys survive, and how blank lines are treated are open. Touches C11, C12.
- **G39 Backup naming and place.** BP:123 and A§5.3:341 copy into `.work/backup/`; A§7.1:437 also has `strands/<id>/backup/`. The name scheme (a fixed name overwritten each time is itself an overwrite), retention, and which folder a strand file uses are not stated. Touches C14.
- **G40 Time format and zone.** A§7.2:475 shows `updated: "2026-10-13T09:10"` with no zone; A§7.3 shows `change_check.at` ending in `Z`; the log header has `HH:MM`; the label has `YYYYMMDD-HHMM`; the lock's `taken_at` and `heartbeat_at` are unspecified. The 60-minute test depends on one zone across a Windows and a Mac machine and across a clock change. Touches C89, C95.
- **G49 Bytecode cache.** BP:123 says nothing is ever written into the plugin's own folder; Python writes `__pycache__` beside an imported module (`record.py` imports `mmb_common`) unless bytecode writing is off or a cache prefix is set. Touches C18.
- **G60 What the sha is a hash of.** `guard` (A§5.3:344) and the frozen-blueprint sha (A§7.4:601; BP:123 `freeze`) compare sha256 values; under A24 a text file can differ only in its line endings between systems, and hash differently. Bytes or line-ending-normalised text is not stated. Touches C45, C54, C151.

### Intake files

- **G12 Name collision.** BP:123 says `add-transcript` and `add-document` "refuse to overwrite"; A§7.1:441 and RM:74 say a second dated file the same day takes `-2`, and a second call of the same type on one day is ordinary. Whether the script refuses, picks `-2`, or takes the stem from the caller is open. Touches C55, C56, C62.
- **G13 Where the sha, the input kind and the attachment link are recorded.** BP:123 and A§5.4:354 say "record a sha256", `input_kind: email`, and an attachment "linked to the email when the user says it came with it". The raw files carry no front matter; the snapshot `.md` is call-intake's (A§7.1:394, 396) and the intake report is `transcript_measure.py`'s (RM:254). Which store `record.py` writes to (a log entry of type `document` or `email`, `.work/history.json`, both), the flag that carries the link, and the accepted image extensions are open. Touches C55, C57, C59.
- **G14 How `check` knows an A11 moment.** BP:23, A§7.2:479 and RM:100 give the moments as states of the world (a build proposed in any strand with sample rows planned; the first non-fixture transcript or document saved; a record bound for write probes) and not as fields: how a transcript is known to be a fixture, how "saved" differs from "already saved", and how a record is known to be "bound for write probes" (`account_kind: sandbox`, `build_target: none`, an entry in `local/sandbox-accounts.txt`) are open. So is whether `add-transcript` and `add-document` themselves refuse while the field is `unanswered`, or only `check` reports it (BP:472 H01, BP:523 H56: "the transcript stop fires no more than once"). Touches C142 to C144.

### Record-map against ARCHITECTURE

RM is the stage-1 text (BP:98); where it differs from A§, A§ wins by the authority order, but the builder still has to know which is current. These entries state both.

- **G15 `client/2` fields.** RM:100 has `account_kind` `client | sandbox`, `last_call`, `page_size`, and `sample_data_in_account` `unanswered | allowed | not-allowed`, and has no `build_target`, `client_workspaces` or `last_input`; A§7.2:447 to 477 has `account_kind` `own | client | sandbox`, `build_target`, `client_workspaces`, `last_input`, `ai_notice` and `sample_data_in_account` with `not-needed`. BP:198 follows A§. Touches C115, C147.
- **G16 `strand/1` fields and stage ladder.** RM:104 has `discovery_verdict`, `sop_behind` and `stage` `new | discovery | blueprint | building | demo | signed-off | expanding | closing | closed`; A§7.7:651 to 676 has `clearance`, `override`, `round`, `workspaces` and `stage` `new | intake | readiness | blueprint | building | audited | shown | signed-off | closing | closed`. Which `stage` value `version mark shown` writes depends on the answer. Touches C65, C68, C165.
- **G17 Version states and `version/1`.** RM:156 has the state `demoed` with `demo-script.md` among its files, and RM:112 gives `version/1` the fields `demo_script_ready` and `sop_sections_confirmed`; A§7.4:589 to 594 and BP:198 have no `demoed` (D2: `shown` is an event), and `version.md` carries `purpose` and the events. Touches C127, C158, C160.
- **G18 Strand index header.** RM:87 to 92: `| strand | title | kind | state | version | version state | verdict | SOP behind | live objects | last activity |`; A§7.2:481: short id, title, kind, state, version and version state, clearance, live object count, last activity. `verdict` against `clearance`, and the v2 `SOP behind` column, decide what `check` compares. Touches C128.
- **G19 `status --json` strand and top-level fields.** BP:123 lists, per strand, version, version state, version purpose and clearance; A§5.4:354 lists `stage`, `clearance`, `version`, `version_state`, `shown`, `signed_off`; RM:144 lists "every strand/1 field by name" plus computed values and none of `purpose`, `shown`, `signed_off`. RM:142 keeps `migration_needed` although migration is dropped (D8; BP:120). The shape of `shown` and `signed_off` (date, boolean or list) is open. Touches C114, C117.
- **G44 Budgets.** RM:37 gives `readiness.md` 200 lines; A§7.1:410 gives 250. RM has no row for `exclusions.md` (A§7.1:415, 80 lines) or for the build notes (A§7.1:423). The record's 4 MB soft limit excludes `calls/*.transcript.txt` and `.work/` in RM:64 and also `inputs/*.<ext>` in A§7.1:429. Where a budget is given in lines and KB ("160 lines, 10 KB", A§7.1:386), which one warns is open. Touches C138, C139.
- **G46 `.work/` layout and dropped items.** RM:66 lists `cards-index.json`, `migration-sources/`, `claims-queue/` and `tools/<plugin-version>/`; A§7.1:437 does not. RM:68 still has `leases.json` and `claims/` (dropped by D10 and D13) and RM:274 still has `record.py tools-check` (dropped, D9; A§5.2:336). `history.json` is named at A§7.1:437 and defined nowhere. Touches C25, C53.
- **G47 `guard_index` and "the client's workspaces".** A§7.3:524 has `client_workspace_ids` and `session_label`; RM:116 lacks `client_workspace_ids` and has `chat_label`. The out-of-scope build target test (BP:448, H20) compares `build_targets_by_strand` to the client's workspaces: `guard_index.client_workspace_ids`, `account.json`'s `client_workspaces`, or the `CLIENT.md` string `"core:10000001;crm:10000002"` (A§7.2:462) is open. Touches C148, C149.
- **G61 Evidence marker set.** A§7.5:612 to 626 has nine markers (with `[A]`) and says `leak_lint.py` blocks all nine in `drafts/`; RM:170 to 181 has eight (no `[A]`). `check`'s "no markers or internal ids under `drafts/`" (A§5.4:354) needs the set, and "internal ids" is not defined. Touches C156.

### Versions and sign-off

- **G20 Event data.** BP:123 says `version mark` records "its date, the user's words and, for `shown`, the account it was shown in"; A§7.4:593 and 608 say `shown` carries date and audience by role and `signed-off` carries date, who by role and the assumptions listed; A§8.8:815 gives `record.py version mark shown --strand <id> --date ... --audience <roles>`. The "account it was shown in" appears only in BP; "the user's words" only in BP. Touches C160, C161.
- **G21 "Structural assumption".** A§7.4:587 and AM:46 to 47 name the automation conditions and a general overview of the board architecture, and AM:49 adds a fork built on its leaning; RM:206 gives `assumptions[]` kinds `gap`, `call-type`, `automation-condition`, `board-architecture`, `leaning` with state `assumed` or `accepted`; A§7.5:624 has the `[A]` marker; BP:106 has `assumption_refs` in the ledger. Which kinds count as structural, and which file `record.py` reads to build the list (the `readiness.md` block, the `STRAND.md` "what this build rests on" block, or the ledger), is open. Touches C162, C181.
- **G22 Warn then record.** BP:123, A§5.4:354 and H66 say the command lists, warns, and records "when the user goes on". A script has no second prompt: one call that prints and records, or two calls with a confirm flag, is open. Touches C163.
- **G23 What makes a version `v1.0`.** A§7.4:587 says from `v1.0` a version is a working solution and `v1.0` "means the client has signed off"; A§8.8:817 says `version mark signed-off` "is what `v1.0` means"; BP:123 says purpose reads proof of concept below `v1.0` and working solution from `v1.0`; H66 (BP:533) says it reads proof of concept "before the event and working solution at `v1.0`". Whether the event relabels `v0.3` as `v1.0`, opens a `v1.0`, or flips purpose on the event, and what purpose a `v0.x` carries after its own `signed-off`, is open. Touches C159, C181.
- **G24 `version mark` preconditions.** A§7.4:593 says the events are recorded "on an audited or released version"; BP:123 and A§5.4:354 give no refusal for another state, such as `shown` before an audit. Touches C160, C161.
- **G25 Subcommands with a name and no acceptance sentence.** A§5.4:354 lists `version open`, `version condense-plan`, `version condense-apply`, `card`, `lease refresh|release|status` and `strand list`; BP:123 describes behaviour only for `strand list` and `strand pause` ("exist and are exercised"), `lease take` and `break`, and `version mark` and `release`. `card` is described nowhere in the sources read. Open: `version open`'s inputs, the condense plan's format and the two-step interface, the columns of `strand list`. Touches C70, C158, C171, C172.
- **G26 What `version release` does.** BP:123 says it refuses (lease held, file missing) and "refreshes `SUMMARY.md`"; A§7.4:610 and A§8.8:818 add freezing the snapshots, rolling the strand's entries, and condensing current files; RM:53 and RM:156 list `updates.md` among the frozen files and A§7.1:424 and A§7.4:606 do not. Whether a `shown` or `signed-off` event is a precondition (A§8.8:818 reads as a trigger) is open. Touches C169, C170.
- **G27 Required-file severity.** BP:123 says "missing files for the version state at release"; A§5.4:354 says "(blocking at release)"; A§7.4:598 says every state's files are "checked by `record.py check`" with no severity; RM:156 says "a missing file blocks the release". Whether a missing file in `building` or `built` blocks, warns or waits for a release attempt is open. Touches C127.
- **G41 `freeze`.** BP:123 says it "returns two matching sha256 values"; A§7.1:421 and A§7.4:601 say the frozen copy's sha equals the one in `version.md` and `build.json.approvals`. Which two values, the output format, how `<N>` advances, whether a second freeze of an unchanged blueprint is allowed, and who writes `version.md`'s `revision` and `sha256` are not stated. Touches C54.
- **G42 `strand summary`.** BP:123 says "writes `SUMMARY.md` at or under 80 lines from the user's yes to a plan"; A§7.7:684 says it "takes the user's yes to a plan the way the condense step does". The plan's format, the two-step interface, what each of the nine blocks is generated from (a script cannot write "pains in the client's vocabulary" alone), and what happens past 80 lines are open. RM:108 ends the dates block at "opened, released and closed", A§7.7:684 at "opened, shown, signed off, released and closed". Touches C79, C80.

### `check`

- **G28 Where `readiness.md` carries the clearance.** BP:123 and A§5.4:354 say `readiness.md` carries one of three strings or `none`; A§6:369 says "the clearance and its conditions in front matter"; RM:189 to 212 pins `readiness/1` with `verdict.cleared_for` and machine values `build | build-generic | not-yet`, the human strings living on `STRAND.md` and the card. The key in the front matter, whether `check` accepts a machine value, and whether `STRAND.md`'s `clearance` is compared with `readiness.md`'s are open. Touches C134, C135.
- **G29 The signal for "plans sample rows".** BP:123 and A§7.1:415 (exclusions) and A11-2 (BP:18, BP:23) use the condition; no source names the field or section that says a revision plans sample rows (the blueprint's sample-data section, a `sample_data` row in the ledger, RM:120, or a card field), and the first two are written by later packages. Touches C136, C142.
- **G30 `check` duties differ between sources, and most severities are unstated.** BP:123 lists twelve blocking checks, the A11 rule and the budget warnings; A§5.4:354 adds schema checks, relative links, markers carry a location, nothing under `drafts/`, history only grew; A§6:367 adds the "Internal: never client-facing" line; BP:448 and H20 (BP:487) add an edited transcript, a hand-edited frozen blueprint, an absolute path in either spelling, a stale lease, a stale native index and an out-of-scope build target. Which of the additions block and which warn is open for most, and H20's "a stale native index downgrades guarded writes to an ask" reads as hook behaviour (WP13) while WP2 owns H20's pass. Touches C148 to C157.
- **G55 `check` modes.** BP:123 and A§5.4:354 speak of "blocking at release" and of A11 findings "at the moment it matters"; no source gives `check` flags for a release-time pass, a strand scope, or the moment the calling skill is at. A single full pass would block on A11 fields at times the rule calls silent (BP:23). Touches C127, C141 to C145.
- **G57 Reads on a newer schema.** BP:123, A§5.3:342 and RM:96 say a record with a newer schema "refuses writes"; whether `status` and `check` may still read it (and `status --json` carries `record_schema`, RM:142) is not stated. Touches C13.

### `home init`

- **G31 Templates in stage 2.** BP:123 accepts every subcommand except `init` and `home init` in stage 2 against `tests/unit/fixtures/`; `strand open` places `readiness.md` and `exclusions.md` from templates (BP:123) that WP7 ships in stage 3 (BP:70, BP:198), and the plugin's `templates/` folder is empty on 2026-10-14. Where `strand open` reads templates in stage 2, and whether the WP2 fixture carries them, is open. Touches C66, C67.
- **G32 `home init` interface and what it can check.** BP:123 and A§5.4:354 say it writes `settings.json` "from the walkthrough's answers", and no source says how the answers arrive (flags, a JSON file, prompts) or what the script prints. "The connector's presence in the roster" (A§5.4:354, A§8.2:745) is not readable by a script outside the session; A§5.4:354 also checks "the plugin root", absent from BP:123. Whether "the two doors are explained" (H57) comes from the script or from the `first-run.md` reference of A§8.2:745 is open. Touches C33, C37.
- **G33 Re-running `home init`.** BP:123 and H57 (BP:524) say it "never overwrites a settings file that exists" and "a second run refuses to overwrite the settings and says so"; A§5.4:354 says it "runs again on request without overwriting an answer it is not asked to change", which reads as allowing a requested change. Touches C36.
- **G34 `settings.json` key names.** BP:106 says `record-map.md` carries "the fields of `local/settings.json`" once stage 2 lands them; the file as it stands names none (RM:68 gives only the path). `home init`, `check` ("a `local/settings.json` that `check` reads", BP:198), `ledger.py bind` (BP:134), `leak_lint.py` and the H57 grader need the same names. The shape of the firm renderings, the operational workspaces, and the archive choice values is open; the `sandbox-accounts.txt` syntax is at RM:68. Touches C29 to C32.
- **G35 Setting `MMB_HOME`.** BP:123 says the walkthrough "sets in the environment in a form that works on both systems"; A§5.3:345 says it "says how to set the variable on the system it runs on rather than assuming one shell". A child process cannot set its parent's environment, so whether `home init` prints instructions, writes a profile or calls a system tool is open; and a non-default home chosen by the user cannot be recorded in `settings.json`, which lives under that home. Touches C38.
- **G37 Range of the `CLAUDE.md` warning.** BP:123 and A§5.3:345 say "any folder above the clients folder": to the filesystem root, to the user's home, or including the home folder itself is open. In tests the temporary home sits under a system temp folder. Touches C35.
- **G58 Home items beyond the six folders.** A§5.3:345 and A§7.1:439 also name `clients-index.json`, the `monday-knowledge/` overlay, `sandbox/SANDBOX.md` and `cards/<slug>.md`; BP:123 has `home init` create the six folders and the two seeded files. Whether `home init` creates `clients-index.json` and `SANDBOX.md` is open. Touches C28, C32.
- **G59 The D-numbered decisions.** BP:120 to 123 cite D8, D10, D11, D12, D21, D25, Q7 and Q14 and define none; they are defined at 1b:31 to 48 and predate A22 to A28 (1b:34 places the user's GitHub account in settings unconditionally and gives a development home value; 1b:31 keeps a `schema_version` field while A§5.3:342 and RM:96 put a `schema` key on every file). Q7 and Q14 are interview items not found in the files read. Touches C13, C25, C29.

