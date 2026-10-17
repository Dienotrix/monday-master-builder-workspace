# WP4 contract checklist: `leak_lint.py`

Date: 2026-10-17. Internal build file: never client-facing.

This file turns the acceptance of work package WP4 into numbered, separately testable clauses, copies the shapes the code must honour, and lists what the sources leave open or state two ways. It decides nothing. A builder ticks each clause by one test or one inspection; the decisions step reads section 4 before anything is built, because every entry there is a choice the sources do not make. The approved plan (`PLAN.md`) is a constraint, not a source of new rules: the user's answers to its Q1 to Q4 (all four "(a)"), the nods of its sections 7 and 8 (nod 14 changed) and the carry-overs of its section 1 are carried where a clause rests on them, and each entry of its section 7 is carried into section 4.

## 1. Header: sources and how to read this file

### Sources

| Short | File | What was read |
|---|---|---|
| BP | `rebuild-workspace/design/BUILD-PLAN.md` | the WP4 block (153 to 159; line 158 is the acceptance sentence), section 0 and A11 (11 to 24), stage 4b (51), the `--terms` release use (114), the write path (252), the stage 4 grader and fixtures copy-in (320 to 323, 410, 448), the file row (368), the repo-only rule (382). Cited as `BP:line` |
| A§ | `rebuild-workspace/design/ARCHITECTURE.md` | 5.3 home and local settings (346), the 5.4 `leak_lint.py` row (357), the `allowlist.md` and `exclusions.md` rows (370), the file map's `clients-index.json` (440), 7.5 evidence markers (613 to 627), the allowlist-proposal and per-write steps of the build order (783, 798), 9.6 (912 to 922). Cited as `A§section:line` or `A§:line` |
| AM | `rebuild-workspace/design/AMENDMENTS.md` | A28 (16 to 20), A24 (40 to 44), A25 (46 to 58), A23 (60 to 68), A20 (87 to 93), A18 (104 to 110), A17 (112 to 120), A16 (122 to 133), A12 (159 to 163), A11 (173 to 177). Cited as `AM:line` |
| RM | `monday-master-builder/plugins/monday-master-builder/shared/record-map.md` | lines 21, 24, 42, 43, 76 and 255 to 275 (the log paragraph and the evidence markers table). Cited as `RM:line` |
| LT | `shared/leak-terms.txt` (same plugin folder) | the whole file, 195 lines; its syntax is lines 17 to 29. Cited as `LT:line` |
| SF | `shared/safety.md` | section 6 (lines 80 to 90). Cited as `SF:line` |
| AI | `rebuild-workspace/design/ai-offerings-findings.md` | the whole file, 77 lines (the source of the AI payload fields, PLAN Q3). Cited as `AI:line` |
| MC | `plugins/monday-master-builder/scripts/mmb_common.py` | the function list and docstrings only (32 to 660): `MMBError` and its subclasses, `home`, `read_settings`, `read_json`, `read_text`, `json_text`, `write_file`, `sha256_file`, `sha256_text`, `schema_newer`, `require_schema`, `record_mutex`, `relative`. Cited as `MC:name` |
| Gnn | `rebuild-workspace/build/wp2/DECISIONS.md` | G10 (83), G11 (91), G40 (327), G49 (399), G57 (463), G58 (471). Cited as `Gnn` |
| W91, R8 | `rebuild-workspace/build/wp3/DECISIONS.md` | W91 (1006 to 1014, the record locator and the frame) and R8 (1160, the cross-record read). Cited by id |
| KEY | `rebuild-workspace/fixtures/s1-discovery-strong/answer-key.json` | the shape of the `expected_leak_blocklist` array only: a list of prose strings. Nothing from any array is copied here. Cited as `KEY` |
| W3C | `rebuild-workspace/build/wp3/CONTRACT.md` | the form copied (sections 1 to 5), and its section 3.4 (the envelope) and section 4 (the form of a gap). Cited as `W3C` |
| PLAN | `rebuild-workspace/build/wp4/PLAN.md` | all of it. Cited as `PLAN §n`, with `PLAN §7.n` for an entry of its conflicts list and `PLAN §8.n` for a nod |

Authority order (BP:5, HANDOFF): AMENDMENTS over ARCHITECTURE over BUILD-PLAN. `record-map.md`, `safety.md` and `leak-terms.txt` are stage-1 files that lag A24 to A28 and A17 to A18 in places; where RM or SF or LT and A§ differ, section 4 lists both.

### Anchors re-checked

Every line the plan and the brief cite was re-read at the anchor given, and none has moved: BP:153 to 159, 368, 382, 252, 114, 51, 321; A§:346, 357, 370, 440, 613 to 627, 912 to 922; RM:21, 24, 42, 43, 76, 258 to 272; LT:17 to 29; SF:80 to 90; AM:19, 65, 115, 118, 130, 173 to 177; G10, G11, G40, G49, G57, G58, W91, R8. Three small corrections to how the plan words things, for the decisions step:

- AM:130 (A16) says a client document lives in `inputs/` "under the same leak-lint, neutral-naming and retention rules as transcripts". It does not itself say that `[Q/doc]` is blocked or that a client document is exempt from the copied-run rule. Those two statements are in A§:920 (the exemption), A§:627 and RM:272 (all nine markers blocked in `drafts/` and every payload) and BP:158.
- BP:410 is the heading of the ten reviewed fixtures. What it points at, the leak grader reading `expected_leak_blocklist`, is stated at BP:323 and BP:448.
- BP:448 counts "158 entries" in the ten reviewed fixtures' keys; the plan counts 400 prose entries in 25 arrays (PLAN §1). Both can hold (ten keys against twenty-five), but the figure is carried as a gap (X13).

### How to read a clause

Each clause is one requirement. The line under it gives:

- **Src**: where it comes from, as BP line, A§ line, RM line, LT line, AM line, Gnn, PLAN section. `BP:158.n` means part n of the acceptance sentence BP:158, split as the coverage table in section 5.1 shows (parts 1 to 33). `BP:368.n` means item n of the BP:368 row (items 1 to 7). "A§ only" or "BP only" marks a clause that rests on one source.
- **Accept**: when it is accepted. The vocabulary is fixed:
  - `stage 2 unit`: a unit test against inline samples, the trap fixture of `tests/fixtures/leak/`, or a temporary home with the two planted client records, with the Windows side simulated where it matters (`PureWindowsPath`, a CRLF copy of a sample, an injected path spelling). Test records are built in each test's setup (PLAN §8.4).
  - `macOS run`: needs this Mac (PLAN step 10).
  - `Windows run`: needs a real Windows machine (PLAN step 11).
  - `stage 4 headless`: needs WP14's runner, seed records and leak grader (BP:321, BP:323, BP:448). Owed, listed, not failed, as WP3's headless rows were.
- **Test**: one line saying how to tick it.

Clause ids use the prefix `L`. Gap ids use `X`. A clause that depends on an open gap names it ("see X12"); it does not settle it. Where a clause names a command form, the form is provisional: the plan reads subcommands `scan`, `payload`, `blueprint`, `terms`, `index` and `wall`, and X08 holds the question.

Standing constraints that clauses name: Python 3.9 or newer, standard library only; identical behaviour on Windows and macOS; exit codes 0 clean, 1 blocked, 2 warnings only, 3 could not run (fail closed); no account is read or written; redaction is written and not defaulted (A11-3 stays open). Every name, figure, firm name and rendering in any example or fixture is invented and generic (A12); no real person, firm or monday account, workspace or object id appears in this file.

---

## 2. Clauses

### 2.1 Runtime and cross-system rule

- **L01** `leak_lint.py` imports only the standard library: no third-party package.
  - Src: A§5.3:340; AM:42 (A24); PLAN §1. Accept: stage 2 unit; Windows run. Test: walk the script's imports with `ast` and check every module is standard library.
- **L02** The script and its three test files use Python 3.9 syntax only: no `match` statement, no `X | Y` union evaluated at runtime.
  - Src: BP:123 (the WP2 acceptance, which WP4 inherits); AM:42; PLAN §8.1. Accept: stage 2 unit. Test: `ast.parse(source, feature_version=(3, 9))` on each file, run under the newest Python.
- **L03** `sys.dont_write_bytecode = True` is the first statement after `import sys`, before `mmb_common` is imported.
  - Src: BP:158.1; G49. Accept: stage 2 unit. Test: parse the module; the statement after `import sys` is that assignment, and the `mmb_common` import node follows it.
- **L04** No `__pycache__` and no other file appears in the plugin folder after any subcommand runs.
  - Src: BP:158.1; G49 (the same test as WP2's C18 and WP3's K04). Accept: stage 2 unit; Windows run. Test: run every command form from a writable temporary copy of the plugin folder, in one test with the bytecode variable dropped from the child's environment, and assert the copy's file list is unchanged.
- **L05** No shell step: no `os.system`, no `shell=True`, no `os.popen`; any `subprocess` call takes a list.
  - Src: A§5.3:340; AM:42. Accept: stage 2 unit. Test: search the script for those names.
- **L06** Every path is built with the standard library's path handling from the record folder or the home it is given; none is built by joining strings with a fixed separator or from a literal `~`.
  - Src: A§5.3:340; AM:42. Accept: stage 2 unit; Windows run. Test: run every command form against a record under a folder whose name holds a space; search the script for `"/"` and `"\\"` joins.
- **L07** Text is read with either line ending and with or without a leading byte-order mark, and a CRLF, an LF and a BOM copy of the same input give the same findings and the same exit code.
  - Src: G11; AM:42 ("transcripts and documents are read with either line ending"); BP:155. Accept: stage 2 unit; Windows run. Test: run each of an LF, a CRLF and a BOM copy of one planted file; the three outputs are equal except the recorded hash of the input bytes.
- **L08** Every JSON file the lint writes is two-space indented, `ensure_ascii=False`, LF line endings, no byte-order mark, a final newline, key order kept, through `mmb_common.json_text`.
  - Src: G11; MC:json_text; PLAN §1 (the index, Q1). Accept: stage 2 unit; Windows run. Test: after `index`, the file's bytes equal `json_text(json.loads(bytes))` and contain no `\r`.
- **L09** The lint writes no file except the index entry (2.13). Every other subcommand leaves the whole record and the whole home byte-equal.
  - Src: A§5.4:357 ("block and report, never edit"); PLAN §8.9. Accept: stage 2 unit. Test: hash the record and the home before and after each subcommand but the index one; the hashes are equal.
- **L10** No account is read or written: the script imports no network module, takes no account id or token as an argument, and reads no file under `local/` other than `settings.json` and `leak-terms.txt`.
  - Src: BP:19 and BP:158 (A11 stays open); PLAN §1, §6. Accept: stage 2 unit. Test: walk the imports for `socket`, `urllib`, `http`, `ssl`; search the argument parser for an account or token flag; spy on opens under `local/` and assert only the two files.
- **L11** With `MMB_HOME`, `HOME` and `USERPROFILE` pointed at temporary folders, no subcommand touches anything under the real home, and no path in the script or the tests names a development folder.
  - Src: A§5.3:346; AM:69 to 76 (A22); PLAN §8.4. Accept: stage 2 unit. Test: canary folders for `HOME` and the default home are unchanged after every command form; search the script and the tests for a literal development path.
- **L12** Findings name the input file record-relative (or home-relative) in POSIX spelling, so the output is identical on both systems.
  - Src: G10; W91; AM:42. Accept: stage 2 unit; Windows run. Test: run with the path flavour simulated as Windows and compare the `file` parts to the POSIX run.
- **L13** The script carries its own copy of the small CLI frame (envelope, refusal helper, parser, exit codes) and does not move it into `mmb_common.py`.
  - Src: PLAN §8.2; W91 (the same choice for `ledger.py`). Accept: stage 2 unit (inspection). Test: `mmb_common.py` is byte-equal to its WP2 and WP3 copy; `leak_lint.py` defines its own frame.
- **L14** The files exist: `scripts/leak_lint.py`, `tests/unit/test_leak_lint.py`, `tests/unit/test_leak_wall.py`, `tests/unit/test_leak_fixture.py` and `tests/fixtures/leak/`.
  - Src: BP:156; PLAN §8.1 (three test files where BP:156 names one; see X43). Accept: stage 2 unit (inspection). Test: list the files; the three test files load and run.
- **L15** `tests/fixtures/leak/` is repo-only: no file of it lies under `plugins/monday-master-builder/`, and none is named in the plugin's shipped file list.
  - Src: BP:382. Accept: stage 2 unit (inspection). Test: the fixture's path is outside the plugin folder; the plugin manifest names none of its files.
- **L16** The test records and the two planted client records are built in each test's setup into a temporary `MMB_HOME`; no file is added to WP2's `tests/unit/fixtures/` and nothing is written under any other fixture folder.
  - Src: PLAN §8.4; BP:156. Accept: stage 2 unit (inspection). Test: the file lists of `tests/unit/fixtures/` and of `tests/fixtures/snapshots/` are equal before and after the package.
- **L17** The three test files pass on macOS under the oldest installed Python 3 that is 3.9 or newer and under the newest installed Python 3, WP2's and WP3's suites included.
  - Src: BP:155 ("tests on Windows and macOS"); AM:42; PLAN step 10. Accept: macOS run. Test: run the whole unit suite on the Mac under each interpreter with `PYTHONDONTWRITEBYTECODE=1` and keep the result. Which interpreter stands for 3.9 on the Mac is X43.
- **L18** The same test files pass on Windows under Python 3.9 and under the newest installed Python 3, WP2's and WP3's suites included.
  - Src: BP:155; AM:42; PLAN step 11. Accept: Windows run. Test: run the whole unit suite under `py -3.9` and the newest launcher and keep the result.
- **L19** The built size of `leak_lint.py` and of its tests is reported as a fact beside the planned 540 and 460 lines, which are estimates.
  - Src: BP:159; PLAN §9. Accept: stage 2 unit (inspection). Test: `wc -l` of each file appears in the checklist.

### 2.2 The CLI frame, envelope and exit codes

- **L20** The subcommand surface covers the actions A§5.4:357 lists: a scan of files, a check of one payload, a check of the blueprint's planned names and glossary, a check of a folder for terms (`--terms`), the cross-client check (`--wall`), and the index-writing action of Q1. The command forms are provisional (X08).
  - Src: A§5.4:357; BP:158.15 (`--payload`); PLAN §7.8, Q1 (a). Accept: stage 2 unit. Test: the dispatch table names one handler for each of those actions; no handler is missing and none is named in no source.
- **L21** An unknown subcommand, a missing required flag and any other usage error each print the JSON envelope and exit 3, not the parser's default exit 2.
  - Src: G10; W91. Accept: stage 2 unit. Test: run `leak_lint.py migrate` and a command with a required flag missing; exit 3, `"ok"` present, an `error` object.
- **L22** The record is located the way `record.py` and `ledger.py` locate it: a global `--record <folder>` before the command, the current folder by default. A folder with no `CLIENT.md` is exit 3 naming that file, for every command that needs a record.
  - Src: W91; PLAN §1 (the WP3 frame row). Accept: stage 2 unit. Test: run from a folder with no `CLIENT.md`; exit 3 naming the file. Which commands need a record is X08.
- **L23** Every command prints one JSON object, UTF-8, LF, shaped `{"ok": ..., "command": "<name as typed>", ...}`, with no `\r` and no byte-order mark.
  - Src: G10; W91. Accept: stage 2 unit; Windows run. Test: parse the output of each command form; keys `ok` and `command` are present; the output has no `\r`. What `ok` holds on exit 2 and exit 3 is X41.
- **L24** Exit 0 means the lint ran, read every input and found nothing to report.
  - Src: BP:158.32; G10. Accept: stage 2 unit. Test: one clean twin per kind of input exits 0 with an empty findings list.
- **L25** Exit 1 means at least one blocking finding, from any rule, and no command exits 1 for any other cause.
  - Src: A§5.4:357; G10 (the constraint of this package). Accept: stage 2 unit. Test: one planted case per blocking rule exits 1; a usage error and an unreadable file do not.
- **L26** Exit 2 means no blocking finding and at least one warning.
  - Src: A§:920 ("Warnings, not blocks: other numbers"); SF:88. Accept: stage 2 unit. Test: a text whose only finding is a number that is in no record set exits 2.
- **L27** Exit 3 means the lint could not run or could not read an input, and it prints `"error": {"file", "field", "problem", "expected"}`, every part non-empty, `file` in POSIX spelling, `(whole file)` as the field when the whole file is the problem.
  - Src: BP:158.32; G10; W91. Accept: stage 2 unit. Test: one case for each cause listed in 2.14; assert the four non-empty parts.
- **L28** One run reports every blocking finding and every warning it finds in every input, not only the first, so one pass shows all that must change.
  - Src: A§5.4:357 ("block and report"); A§:916. Accept: stage 2 unit. Test: a file with five planted leaks of five rules reports five findings in one run.
- **L29** Every finding names the input, where in it (line and column, or the payload field path), the rule, the class when a list row matched, and whether it blocks or warns. A finding never carries text that only the other client's record holds.
  - Src: G10 (four parts); LT:20 to 21 ("the lint reports the class beside each hit"); A§:922. Accept: stage 2 unit. Test: assert the parts on every finding the tests see; assert a wall finding holds no string that appears only in the other record's files. The exact finding shape is X41.
- **L30** The order of findings is deterministic: inputs in the order given or sorted by path, then by position, then by rule; two runs on the same bytes give byte-equal output.
  - Src: G10 (identical output on both systems); PLAN §8.10. Accept: stage 2 unit; Windows run. Test: run twice and on both path flavours; compare bytes.
- **L31** The output carries the sha256 of every input the lint read, the payload included, as `MC:sha256_file` computes it, so a later caller can match the bytes that were sent to the bytes that passed.
  - Src: PLAN §7.16 (X16), §8.10. Accept: stage 2 unit. Test: the hash for each input equals `sha256_file` of that file; the payload's hash equals the hash of the bytes handed in.
- **L32** Where the lint reads an input file the session hands it (a payload file, a blueprint file, a folder to scan), either the rule of W91 applies (the file lies inside the record folder) or X22 says why not.
  - Src: W91 ("an input file the session hands must lie inside the record folder"). Accept: stage 2 unit. Test: hand a path outside the record; the result is what X22 settles. Open: X22.

### 2.3 The inputs the lint loads

This section holds the clauses for a good read. A file that cannot be read is exit 3 and is covered in 2.14.

- **L33** The shipped list is read from `shared/leak-terms.txt` of the plugin folder, found from the script's own location, and a literal row matches case-insensitively wherever the characters on either side are not letters or digits.
  - Src: LT:18 to 19; A§:916. Accept: stage 2 unit. Test: a row `exit ramp` blocks "the exit ramp" and `exit ramp.`, and does not block inside "boexit rampx" (letters on both sides).
- **L34** A line starting with `#` and a blank line are ignored, and a `class: <name>` line puts every row below it, until the next `class:` line, in that class; every hit reports its class.
  - Src: LT:17, 20 to 21. Accept: stage 2 unit. Test: a two-class sample list gives each hit its own class name in the finding.
- **L35** A `re: <pattern>` row is a Python regular expression matched case-insensitively.
  - Src: LT:22. Accept: stage 2 unit. Test: `re: \bP\d{1,2}\b` blocks "p3" and "P12" and not "P123".
- **L36** A `phonetic: <term>` row marks the term for the phonetic-variant rule as well as the literal match, and a `whitelist: <term>` row names a legitimate use that the phonetic rule directly above it never blocks.
  - Src: LT:23 to 26; A§:918. Accept: stage 2 unit. Test: a sample list with one phonetic row and one whitelist row below it parses to those two roles; the rule itself is L52 to L54.
- **L37** The shipped `firm` class is empty on purpose and the lint loads it as empty: it blocks nothing from the shipped file in that class.
  - Src: LT:31 to 39; BP:113. Accept: stage 2 unit. Test: with no firm name in settings and an empty local list, no input is blocked by a firm hit; settings without a firm name is exit 3 (L42).
- **L38** `local/leak-terms.txt` under the home is read in the same syntax as additions to the shipped list; a zero-byte file, which is what `home init` writes, adds nothing and changes no exit code.
  - Src: A§5.3:346; G58; PLAN §1. Accept: stage 2 unit. Test: run the same input with a zero-byte local list and with the file absent from a hand-built home (the absent case is X33), then with one added row; the zero-byte run equals the run with no additions, and the added row blocks and reports its class.
- **L39** A row of the local list in the `firm` class blocks, as the firm rule's per-user additions.
  - Src: LT:5 to 6, LT:31 to 36; PLAN §7.4 (X04). Accept: stage 2 unit. Test: a local list with `class: firm` and one invented rendering blocks that rendering.
- **L40** `local/settings.json` is read with `utf-8-sig`, must carry the schema `settings/1`, and a `schema` that is the same name with a higher number, or another name, is exit 3 with the file named and nothing judged.
  - Src: G57; G11; RM:76; MC:schema_newer. Accept: stage 2 unit. Test: set `schema` to `settings/2`; exit 3, no verdict on any input.
- **L41** `firm.name` and the strings of `firm.renderings[]` are read from `settings.json`; `renderings` may be empty; every value is a string.
  - Src: RM:76; A§5.3:346; BP:158.27. Accept: stage 2 unit. Test: a settings file with a name and two renderings blocks all three; one with an empty `renderings` array blocks the name.
- **L42** A missing or unreadable `settings.json`, a malformed one, or one whose `firm.name` is empty is exit 3 naming the file and the field, for every command that runs the firm rule.
  - Src: PLAN §8.8 (nodded); BP:158.32. Accept: stage 2 unit. Test: remove the file; truncate it; set an empty name; each is exit 3 with the field named. Which commands run the firm rule is X31.
- **L43** The strand's exclusions are read from `solution/exclusions.md` of every strand of the record, and a payload is checked against all of them; a strand with no file adds no rows.
  - Src: PLAN §8.7 (nodded), §7.10; RM:43; A§:920. Accept: stage 2 unit. Test: a record with two strands, one term in each strand's file; a payload with the term of the second strand blocks, whichever strand the payload is for.
- **L44** The allowlist is read from `solution/allowlist.md` of the payload's own strand only; another strand's allowlist is never read, and a strand with no file clears nothing.
  - Src: PLAN §8.7; RM:42; A§:920. Accept: stage 2 unit. Test: a row in strand A's file clears a method term for A's payload and clears nothing for B's. How the lint is told the strand is X10.
- **L45** The record's own files supply the sets the rules compare against: client figures, client quotes, runs from internal files, and the record's own names. The internal files are every file of the record except the text of client documents and emails in `inputs/`, the marked client-safe blocks, and `drafts/`.
  - Src: PLAN §7.11 (reading); A§:916, A§:920; RM:21, RM:24. Accept: stage 2 unit. Test: a record variant with one planted figure in `calls/` and one in `inputs/`; both enter the figure set; a run copied from `drafts/` is not read as an internal-file run. The enumeration is X11.
- **L46** The text of each client document or email in `inputs/` is read as the exempt set for the copied-run rule, and for no other rule.
  - Src: A§:916, A§:920; AM:122 to 133 (A16); BP:158.11. Accept: stage 2 unit. Test: a six-word run found in a client document passes the run rule and a figure from the same document still blocks. Whether the quote rule applies to that text is X36.
- **L47** `clients-index.json` is read from the home root with `utf-8-sig`; it must carry the schema `clients-index/1`; a newer schema, another name or malformed JSON is exit 3.
  - Src: G57; G11; PLAN §7.2. Accept: stage 2 unit. Test: write `clients-index/2`, then a truncated file; exit 3 in each case.
- **L48** A `clients-index.json` that does not exist reads as empty: the wall has nothing to compare against and the lint does not exit 3 for that cause alone.
  - Src: SF:90; G58 (`home init` does not create it). Accept: stage 2 unit. Test: a home with no index file and a clean payload exits 0. Whether this is safe when other records exist is X30.

### 2.4 The term rules: names, ids, markers, paths, credentials

- **L49** Every firm rendering (the name and each entry of `renderings[]`) blocks, case-insensitively, wherever it appears with the boundary rule of L33.
  - Src: BP:158.27; A§:916; RM:76. Accept: stage 2 unit. Test: planted invented firm name and each invented rendering block in a name field and in a draft; the clean twin passes.
- **L50** A case-varied rendering and a possessive rendering (`'s` and `’s`) of a firm rendering block.
  - Src: A§:918 (first trap category); BP:158.27. Accept: stage 2 unit. Test: `EXAMPLE FIRM`, `Example firm's` and `example firm’s` block.
- **L51** A rendering split by a comma, or by a line break, still blocks; what "comma-split" means is X32.
  - Src: A§:918 (comma-split organisation names). Accept: stage 2 unit. Test: the fixture's comma-split case blocks and its twin passes. Open: X32.
- **L52** The phonetic-variant rule blocks a spelling the lists do not write out when it is a phonetic variant of a firm rendering or of a `phonetic:` row.
  - Src: A§:918; LT:23 to 24; BP:158.27 ("catches every rendering the fixture plants"). Accept: stage 2 unit. Test: an invented firm name and an invented misspelling of the kind a transcript would carry both block. The algorithm is X32.
- **L53** A whitelist row clears the legitimate uses the phonetic rule would otherwise block.
  - Src: LT:25 to 26; A§:918; BP:158.28. Accept: stage 2 unit. Test: the whitelisted phrase passes while an unlisted phonetic variant beside it still blocks.
- **L54** An ordinary word that sounds like the invented firm name does not block: a test asserts no false positive on it.
  - Src: BP:158.29 (X07); A§:918; LT:25 to 26. Accept: stage 2 unit. Test: the invented ordinary word of the fixture, in three sentences, exits 0.
- **L55** The firm rule runs on every scan, every payload and every planned name, and on the text read from a `.docx` property part.
  - Src: A§:914, A§:916; BP:158.14, BP:158.27. Accept: stage 2 unit. Test: the same invented rendering planted in a draft, in a payload name and in `docProps/core.xml` blocks in each.
- **L56** The plugin and assistant names of the shipped list (class `plugin`: the product's names and its prefix patterns; class `assistant`) block.
  - Src: A§:916; LT:41 to 53; BP:113. Accept: stage 2 unit. Test: one row of each class and one `re:` row of class plugin block; the twin passes.
- **L57** Method-class terms block, and grades block only beside a criterion, pain or check id or another grade, in either order.
  - Src: LT:55 to 128. Accept: stage 2 unit. Test: three method terms block; an ordinary "Met" with no id passes; "Met" beside a criterion id blocks, in both orders.
- **L58** Pain, number, stakeholder, objection, commitment and criterion ids block, and so do element keys outside a strand and fully qualified versions.
  - Src: LT:130 to 143; A§:916 ("internal ids in context"). Accept: stage 2 unit. Test: `P3`, `N2`, `S1`, `O4`, `C2`, `R7`, `001:B1` and `001/v0.1` block; `P123` does not.
- **L59** A collision of a client's own word with a pain-id pattern blocks and is reported, never skipped silently.
  - Src: LT:132 to 133. Accept: stage 2 unit. Test: a payload with "P1" is blocked with the class `pain-ids` in the finding. What this costs on ordinary text is X17.
- **L60** The five forms `[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]` and `[Q/doc]` each block in `drafts/` and in every payload field.
  - Src: BP:158.5; A§:627; RM:272; LT:148 to 152. Accept: stage 2 unit. Test: each of the five planted in a name, a doc markdown field and a draft blocks.
- **L61** `[Q/doc]` blocks as its own marker even though a client document's extract is exempt from the copied-run rule in `inputs/`.
  - Src: BP:158.5; A§:621, A§:627. Accept: stage 2 unit. Test: a payload line holding `[Q/doc]` beside text copied from a client document blocks on the marker; the copied text alone passes the run rule.
- **L62** `[X]`, `[E]` and `[I]` each block in `drafts/` and in every payload field.
  - Src: A§:627; LT:153 to 155. Accept: stage 2 unit. Test: each planted and blocked; ordinary bracketed text such as `[1]` passes.
- **L63** The bare assumption marker `[A]` blocks in `drafts/` and in every payload field, so an assumption's marker never reaches the workspace, since assumptions live in the record, the approval card and the build notes only.
  - Src: BP:158.5; A§:625; AM:46 to 58 (A25); RM:272. Accept: stage 2 unit. Test: `[A]` blocks in a name and a doc body; this needs a row the shipped list lacks today (X03).
- **L64** An amendment tag such as `[A12]` or `[A14-2]` and a flag tag such as `[L14]` block.
  - Src: LT:194 to 195. Accept: stage 2 unit. Test: each planted tag blocks; the twin with plain brackets passes.
- **L65** The status and transcript-artefact markers (`[found]`, `[inferred]`, `[pre-read]`, `[unpriced]`, `[inaudible]`, `[laughs]`, `[crosstalk]`, `[live ...]`, `[doc ...]`) and the citation locations (`@00:12:31`, `cue 82`, `cues 82-85`, `L142`, `L142-144`) block.
  - Src: LT:156 to 166. Accept: stage 2 unit. Test: each planted form blocks; a sentence with "the cue was clear" passes.
- **L66** All nine markers of A§:627 are blocked, and a test loops over exactly the nine and fails if the shipped list and the script disagree on the set.
  - Src: BP:158.5; A§:627; RM:272; PLAN §7.3. Accept: stage 2 unit. Test: the nine as one parametrised list; the markers' names embedded in the script between pinned markers equal the nine of `record-map.md` (L271 and L272).
- **L67** Record paths in POSIX spelling block: `~/`, `/Users/`, `/home/`, `clients/<slug>/`, `.work/`, `calls/`, `strands/`, `inputs/` and the `NNN-topic/` folder form.
  - Src: BP:158.7; A§:916; LT:172 to 179. Accept: stage 2 unit; Windows run. Test: one planted path of each form blocks; the twin ("calls" as an ordinary plural, with no slash) passes.
- **L68** Record paths in Windows spelling block: the same folders written with backslashes, such as `clients\<slug>\`, `.work\` and `strands\<NNN-topic>\`, and a drive-letter user path.
  - Src: BP:158.7; AM:40 to 44 (A24); LT:173 (the drive form only). Accept: stage 2 unit; Windows run. Test: each backslash form blocks; run once under POSIX and once with the path flavour simulated as Windows. The shipped list covers only the drive form today (X03).
- **L69** A path written in mixed spelling (slashes and backslashes in one string) blocks.
  - Src: BP:158.7; AM:40 to 44. Accept: stage 2 unit; Windows run. Test: `clients/<slug>\calls\x` blocks.
- **L70** The record's own file names block as literals: `CLIENT.md`, `STRAND.md`, `SUMMARY.md`, `discovery.md`, `blueprint.md`, `log.md`, `account.json`, `build.json`, `live-map.md`.
  - Src: LT:180 to 188; A§:916. Accept: stage 2 unit. Test: each name blocks in a payload; a file name outside the list passes.
- **L71** An HTML comment blocks.
  - Src: BP:158; A§:916; LT:189. Accept: stage 2 unit. Test: `<!-- note -->` blocks; a plain `<b>` tag passes.
- **L72** A raw monday id of eight or more digits outside a link blocks; one of seven digits does not block on this rule.
  - Src: BP:158.8; A§:916; LT:190. Accept: stage 2 unit. Test: an invented eight-digit number in prose blocks; a seven-digit number does not (it may warn as a number, L85).
- **L73** The same eight-digit number inside a link passes the id rule; what counts as a link is X34.
  - Src: BP:158.8; LT:169 to 171; A§:916. Accept: stage 2 unit. Test: the twin with the number inside a Markdown link target exits 0 on this rule.
- **L74** The stripping of URLs applies to the id class only: a firm rendering, a marker or another client's term inside a link still blocks.
  - Src: LT:169 to 171 ("before this class runs"). Accept: stage 2 unit. Test: a link whose text or target holds an invented firm rendering blocks. See X34 for the readings.
- **L75** A 64-character hash, a gotcha or probe id (`G-12`, `S0-4`, `P-19`) and a design id block.
  - Src: LT:191 to 193; A§:916. Accept: stage 2 unit. Test: one planted sample of each blocks.
- **L76** A payload string shaped like a credential blocks: a token or key pattern, a bearer or basic authorisation header, a `password=` style pair, and a URL carrying user info or a token parameter.
  - Src: BP:158.17; AM:112 to 120 (A17, "never carries a credential"); PLAN §7.15. Accept: stage 2 unit. Test: one invented sample of each shape in a name field blocks; the twin passes. The shapes and the rule's home are X15.
- **L77** A payload carrying text copied from an internal note blocks; what an "internal note" is, beyond a copied run, is X40.
  - Src: BP:158.17; AM:118 (A17). Accept: stage 2 unit. Test: the planted note text of the fixture blocks and its twin passes. Open: X40.

### 2.5 Client figures

- **L78** The lint builds from the record the set of client-derived figures, as numeric values, so a figure matches by value and not by how it is spelled. A figure in a client document of `inputs/` is a client figure with the document as its source.
  - Src: A§:916 ("client-derived cost figures in any common format"); AM:122 to 133 (A16, "a stated figure in a document is a client figure"); PLAN §7.11. Accept: stage 2 unit. Test: a record variant with `45,000` in a call summary and `62,500` in a client document; both values enter the set and each is reported with its source file. What "client-derived" covers is X25.
- **L79** A figure written as bare digits (`45000`) that is in the set blocks.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: planted `45000` blocks in a payload name and a draft; the twin with an unrelated number does not.
- **L80** A figure written with thousands separators (`45,000`) that is in the set blocks.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: planted `45,000` blocks.
- **L81** A figure written with a magnitude letter (`45k`) that is in the set blocks.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: planted `45k` blocks. Letter case and spacing are X25.
- **L82** A figure written with a currency sign and a magnitude letter (`$45k`) that is in the set blocks.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: planted `$45k` blocks.
- **L83** A figure spelled in words ("forty-five thousand") that is in the set blocks.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: planted "forty-five thousand" blocks; the same words for another value pass this rule. Other spoken forms are X25.
- **L84** A figure blocks in any of the five formats whatever format the record itself uses: a record that holds `$45,000` blocks `45k` in a payload.
  - Src: BP:158.2; A§:916. Accept: stage 2 unit. Test: five record variants, one per format, and five payloads, one per format; the twenty-five pairs all block.
- **L85** A number that is in no record set is a warning, not a block, and the run exits 2 when nothing else is found.
  - Src: A§:920; SF:88; PLAN §7.11. Accept: stage 2 unit. Test: a payload with an unrelated `1,200` exits 2 with one warning. Whether very small numbers warn is X25.
- **L86** A number below the floor of the decisions step is not harvested as a client figure and cannot block; it is at most a warning. The floor's value is not set here.
  - Src: PLAN Q1 (a) ("above a floor the decisions step sets"), §7.11. Accept: stage 2 unit. Test: with the floor read from where X25 puts it, a figure one below the floor passes and one at the floor blocks. Open: X25.
- **L87** A figure in the record's exclusions is matched as a figure of the record, in the same five formats.
  - Src: A§:370 (exclusions: names, terms and figures); PLAN §7.11. Accept: stage 2 unit. Test: a figure row in `exclusions.md` blocks in each of the five formats.

### 2.6 Copied runs, quotes and the exemptions

- **L88** A run of six or more consecutive words copied from an internal file blocks, and the finding names the file it came from.
  - Src: BP:158.3; A§:916. Accept: stage 2 unit. Test: a payload line holding six consecutive words of a call summary blocks; the twin with one word changed in the middle passes this rule. What counts as a word, a case or punctuation difference is X24.
- **L89** A run of five words copied from an internal file does not block on this rule.
  - Src: BP:158.3. Accept: stage 2 unit. Test: five consecutive words of the same call summary exit 0.
- **L90** A client quote of eight or more words blocks, whether or not the same words would also be a copied run.
  - Src: BP:158.4; A§:916. Accept: stage 2 unit. Test: an eight-word quote from a `[Q]` line of a call summary blocks and the finding names the rule `quote`; a seven-word part of it does not block on the quote rule. The quote set's source and the overlap with the run rule are X24.
- **L91** A run of six words that matches the text of a client document or email in `inputs/` passes the run rule.
  - Src: BP:158.11; A§:920; AM:122 to 133 (A16). Accept: stage 2 unit. Test: six consecutive words of a client document in `inputs/` exit 0 on this rule.
- **L92** The same six-word run copied from that snapshot's conflict rows blocks.
  - Src: BP:158.12; A§:920 ("its marks, conflicts and markers stays inside the rule"). Accept: stage 2 unit. Test: the run taken from a conflict row of the document snapshot blocks; the run taken from the client's own text does not. The row form is X09.
- **L93** The rest of a snapshot outside its client-safe block (its section map, marks and markers) stays inside the run rule.
  - Src: A§:920; RM:24. Accept: stage 2 unit. Test: a six-word run from the snapshot's section map blocks.
- **L94** The marked client-safe block of a call summary passes the run rule.
  - Src: BP:158.9; A§:920; RM:21. Accept: stage 2 unit. Test: six consecutive words inside the mark of a call summary exit 0 on this rule; the same words outside the mark block. The mark's syntax is X09.
- **L95** The marked client-safe block of a document snapshot passes the run rule.
  - Src: BP:158.9; A§:920; RM:24. Accept: stage 2 unit. Test: as L94, with a document snapshot.
- **L96** The blueprint's client-safe glossary passes the run rule.
  - Src: BP:158.10; A§:920. Accept: stage 2 unit. Test: six consecutive words inside the glossary exit 0 on this rule. The glossary's syntax is X09.
- **L97** A block mark that is malformed, unclosed or nested wrongly never exempts more text than the well-formed mark would; it exempts none or is exit 3.
  - Src: A§:920 ("Fail closed"); BP:158.32. Accept: stage 2 unit. Test: delete the closing mark; the text after the opening mark blocks or the run exits 3, and no later text in the file passes on the strength of the mark. Open: X09.
- **L98** A run made mostly of common words is ignored by the run rule.
  - Src: BP:158.13; A§:920 ("the filter tuned on the leak-trap fixture"). Accept: stage 2 unit. Test: a six-word run of common words copied from a call summary exits 0; a six-word run holding client vocabulary blocks. The threshold and the word list are X19.
- **L99** The common-word filter is for runs only: it does not clear a figure, a marker, an id, an exclusion or another client's name.
  - Src: BP:158.13; A§:920. Accept: stage 2 unit. Test: a run of common words that also holds an eight-digit id blocks on the id.

### 2.7 Exclusions and the paraphrase categories

- **L100** A payload field holding a term of any strand's `exclusions.md` blocks, in a name, a description, a label, a seed value, a doc markdown field and an automation request text alike.
  - Src: BP:158.18; A§:370; PLAN §8.7. Accept: stage 2 unit. Test: one excluded name planted in each of six field kinds blocks; an invented sample value that is not excluded passes.
- **L101** The exclusions apply to planned names at the blueprint stage and to everything in `drafts/` as well as to payloads.
  - Src: A§:370 ("the blueprint, the sample-data step and the lint read it"); AM:16 to 20 (A28, "minus the client's exclusion list"). Accept: stage 2 unit. Test: an excluded name in a planned name and in a draft blocks.
- **L102** An `exclusions.md` that exists and cannot be read or parsed is exit 3; the lint does not proceed as if the list were empty.
  - Src: A§:920 ("Fail closed"); BP:158.32. Accept: stage 2 unit. Test: an exclusions file with undecodable bytes exits 3 naming it. The row form is X09.
- **L103** A planted paraphrase of each of the three categories of A§:916 (personal and emotional stakes; a remark by client staff about a colleague; our own internal assessment of a person) is blocked, and its clean twin passes.
  - Src: A§:916; PLAN §7.6. Accept: stage 2 unit. Test: three planted cases and three twins in the fixture. Met only if the planted cases block; what a string rule can reach is X06; who checks the client-safe block when it is written is X38.

### 2.8 The two structural assertions

- **L104** Both assertions run on every scan, whatever the subcommand and whatever the input kind, and no flag turns either off.
  - Src: BP:158.26; A§:918 ("run on every scan"). Accept: stage 2 unit. Test: run each subcommand on a file that trips each assertion; every run reports it.
- **L105** A document that carries a figure of the record only in split renderings fails: digits broken across tokens, or a number spelled across a line break.
  - Src: BP:158.24; A§:918. Accept: stage 2 unit. Test: the planted `45 000` and "forty-\nfive thousand" cases fail and the report names the rule `split-figure`.
- **L106** A split rendering of a number that is not in the record's set does not fail.
  - Src: A§:918 ("a figure" read as a client figure); A§:920. Accept: stage 2 unit. Test: the twin with an unrelated split number exits 0 or 2, not 1.
- **L107** A proper-noun-free paragraph that names three of the client's tool categories in one sentence fails.
  - Src: BP:158.25; A§:918. Accept: stage 2 unit. Test: the planted sentence with three category words fails and the report names the rule `tool-categories`.
- **L108** The same paragraph with two categories in the sentence passes.
  - Src: BP:158.25; A§:918. Accept: stage 2 unit. Test: the twin with two category words exits 0.
- **L109** Three categories spread over three sentences of the paragraph pass; the assertion counts a sentence, not a paragraph.
  - Src: A§:918 ("in one sentence"). Accept: stage 2 unit. Test: the same three words in three sentences exit 0 on this rule.
- **L110** A paragraph that holds a proper noun is outside this assertion; it may still be blocked by another rule.
  - Src: A§:918 ("a proper-noun-free paragraph"). Accept: stage 2 unit. Test: the planted sentence with one invented proper noun added is not reported by this assertion.
- **L111** A single category word alone never produces a finding.
  - Src: PLAN §8.6 ("a class the lint counts rather than blocks"). Accept: stage 2 unit. Test: a paragraph with one category word exits 0. The vocabulary and the count rule across the client's own categories are X12.
- **L112** Both assertions are proved on `tests/fixtures/leak/`: each has a planted failing case and a passing twin, and the fixture names them.
  - Src: BP:158.26; BP:368.2. Accept: stage 2 unit. Test: the fixture README lists the four cases; each case's expected exit is asserted by `test_leak_fixture.py`.

### 2.9 The allowlist, the warnings and the two non-removals

- **L113** An allowlist row of the payload's own strand clears a method-class term, and the result carries a caution, never silence.
  - Src: BP:158.21; LT:27, LT:56 to 57; A§:920. Accept: stage 2 unit. Test: a row for an ordinary method word clears it and the output holds one caution naming the row.
- **L114** An allowlist row clears nothing of class firm, plugin, assistant, pain-ids, markers or id-patterns.
  - Src: LT:27 to 29; A§:920. Accept: stage 2 unit. Test: a row naming an invented firm rendering, a plugin name and a pain id each leaves the block in place.
- **L115** An allowlist row naming a figure does not clear a figure block.
  - Src: BP:158.21; A§:920. Accept: stage 2 unit. Test: a row `45000` leaves `45000` blocked in all five formats.
- **L116** An allowlist row does not clear a client quote of eight or more words.
  - Src: BP:158.21; A§:920. Accept: stage 2 unit. Test: a row holding the quote leaves it blocked.
- **L117** An allowlist row does not clear a copied run of six or more words.
  - Src: BP:158.21; A§:920. Accept: stage 2 unit. Test: a row holding the run leaves it blocked.
- **L118** An allowlist row does not clear a marker, an id, a term of the exclusions or another client's name.
  - Src: A§:920. Accept: stage 2 unit. Test: one row of each kind; the four blocks stay.
- **L119** A row in another strand's allowlist clears nothing for this strand's payload.
  - Src: PLAN §8.7. Accept: stage 2 unit. Test: strand B's payload with a method word that only strand A's file clears blocks.
- **L120** A "flag, do not remove" group is reported and kept: the lint reports its entries and removes or edits nothing; the scanned file's bytes are unchanged after the run.
  - Src: BP:158.22; BP:448. Accept: stage 2 unit. Test: the fixture's rebuilt group (invented text in the same shape) is reported and the file hash is unchanged. Whether the report is a block or a warning, and what the group is, is X39.
- **L121** A blocked word that is also the client's own vocabulary survives with a caution when the strand's allowlist holds its row, and blocks when it does not.
  - Src: BP:158.23; LT:28 to 29, LT:56 to 57. Accept: stage 2 unit. Test: the fixture's invented text in the shape of the "callback" case: with the row, no block on that word and a caution; without the row, a block.
- **L122** A warning never blocks: a run that has warnings and no block exits 2 and the warnings are listed in the output.
  - Src: A§:920; G10 (the constraint of this package). Accept: stage 2 unit. Test: a payload with two unrelated numbers exits 2 with two warnings.

### 2.10 Reading the inputs: `.md`, `.txt`, `.docx` and payload JSON

- **L123** `.md` and `.txt` files are read as UTF-8 text, and a `.docx` is read as a zip archive with the standard library; the lint reads no other format.
  - Src: A§5.4:357 ("reads `.md`, `.txt` and payload JSON"); BP:158.14. Accept: stage 2 unit. Test: the reader names the three text kinds and JSON; an input of another extension is handled as L132 says.
- **L124** A `.docx` is read from `word/document.xml`, `docProps/core.xml` and `docProps/app.xml`, and the finding names the part the text came from.
  - Src: BP:158.14; LT:12 to 13. Accept: stage 2 unit. Test: three samples built with `zipfile` from XML strings, each with a planted leak in one part; each finding names its part.
- **L125** A leak in the body text of `word/document.xml` blocks.
  - Src: BP:158.14. Accept: stage 2 unit. Test: the planted invented firm rendering in the body blocks; the twin passes.
- **L126** A leak in a field of `docProps/core.xml` (author, title, subject, last modified by and the like) blocks.
  - Src: BP:158.14; LT:12 to 13 ("document properties"). Accept: stage 2 unit. Test: the planted rendering in the author field blocks.
- **L127** A leak in a field of `docProps/app.xml` (company, manager and the like) blocks.
  - Src: BP:158.14; LT:12 to 13. Accept: stage 2 unit. Test: the planted rendering in the company field blocks.
- **L128** A word split across several text runs of `word/document.xml` is read as one word: a firm rendering broken across two runs still blocks, and XML entities are decoded before matching.
  - Src: BP:158.14; A§:918 (split renderings). Accept: stage 2 unit. Test: the invented rendering split over two `w:t` elements blocks; `&amp;` in a name reads as `&`.
- **L129** A `.docx` that is not a zip archive, or has no `word/document.xml`, is exit 3 naming the file. Whether a missing `docProps` part is exit 3 or an empty text is X35.
  - Src: BP:158.32. Accept: stage 2 unit. Test: a text file renamed `.docx` and an archive without the body part each exit 3.
- **L130** A `.docx` is read in memory: no member is extracted to disk and no member path is trusted as a path.
  - Src: L09 (no write); X42 (limits); BP:158.14. Accept: stage 2 unit. Test: a sample whose member name holds `../` is never opened as a path; the home and the record are byte-equal after the run.
- **L131** Payload JSON is read with `utf-8-sig`; invalid JSON is exit 3 naming the file.
  - Src: G11; BP:158.15. Accept: stage 2 unit. Test: a truncated payload file exits 3.
- **L132** An input of an extension the lint does not read, and an input whose bytes are not valid UTF-8 (for a text kind), is exit 3 naming the file, never skipped.
  - Src: BP:158.32; A§:920. Accept: stage 2 unit. Test: a `.rtf` file and a Latin-1 `.txt` each exit 3. Which extensions a folder scan takes is X35.

### 2.11 The payload: generic walk, the standard kinds, the AI kinds

- **L133** A payload is checked by walking every string value at every depth, in objects and in arrays, and each finding names the field path.
  - Src: BP:158.15; A§:914. Accept: stage 2 unit. Test: a leak nested three levels down in an array of objects blocks and the finding's path reaches it.
- **L134** A string field that the field list for its kind does not name is still checked.
  - Src: BP:158.15, BP:158.17 ("no ... reaches an account-level object"); PLAN Q3 (the walker is generic over string fields). Accept: stage 2 unit. Test: add an unnamed field holding a planted leak to a sample of each kind; it blocks.
- **L135** On every payload field the full rule set runs: the firm rule, the plugin and assistant names, method terms, ids, markers, paths, credentials, figures, runs, quotes, exclusions and the wall.
  - Src: A§:914, A§:916; BP:158.15, BP:158.17. Accept: stage 2 unit. Test: one planted case per rule inside a name field blocks, and the finding names that rule.
- **L136** A payload name (item, group, board, column, workspace or other object name) with a planted leak blocks and its twin passes.
  - Src: BP:158.15 ("names"). Accept: stage 2 unit. Test: sample payload and twin in the fixture.
- **L137** A payload description with a planted leak blocks and its twin passes.
  - Src: BP:158.15 ("descriptions"). Accept: stage 2 unit. Test: as L136.
- **L138** A payload label (a status or dropdown label) with a planted leak blocks and its twin passes.
  - Src: BP:158.15 ("labels"). Accept: stage 2 unit. Test: as L136.
- **L139** A payload seed value (a sample row's value) with a planted leak blocks and its twin passes; an invented sample value that matches nothing passes.
  - Src: BP:158.15 ("seed values"); AM:16 to 20 (A28). Accept: stage 2 unit. Test: as L136, with a seed value equal to an excluded name (blocks) and one invented value (passes).
- **L140** Doc markdown, including headings, list items and table cells, with a planted leak blocks and its twin passes.
  - Src: BP:158.15 ("doc markdown"); BP:252. Accept: stage 2 unit. Test: a leak in a table cell and in a heading each block.
- **L141** Automation request text with a planted leak blocks and its twin passes.
  - Src: BP:158.15 ("automation request text"). Accept: stage 2 unit. Test: as L136.
- **L142** An agent's name is checked and a planted leak blocks.
  - Src: BP:158.16; Q3 (a); A§:914. Accept: stage 2 unit. Test: sample payload and twin for the agent name field.
- **L143** An agent's role, and its role description, are checked and a planted leak blocks.
  - Src: BP:158.16; AI:10 (the `profile` holds name, role, role description). Accept: stage 2 unit. Test: one planted leak in each field blocks. The role description is in AI only (X14).
- **L144** An agent's goal is checked and a planted leak blocks.
  - Src: BP:158.16; AI:10. Accept: stage 2 unit. Test: sample and twin.
- **L145** An agent's plan (its instructions, markdown) is checked in full and a planted leak anywhere in it blocks.
  - Src: BP:158.16; AI:10, AI:26; AM:112 to 120 (A17). Accept: stage 2 unit. Test: a leak in the last paragraph of a multi-paragraph plan blocks.
- **L146** The names of an agent's knowledge grants (a board or a doc it may read) are checked and a planted leak blocks.
  - Src: A§:914 ("knowledge-grant names"); AI:18; BP:158.16 does not name them. Accept: stage 2 unit. Test: a grant name holding an excluded term blocks. A§ only (X14).
- **L147** A Vibe prompt is checked and a planted leak blocks.
  - Src: BP:158.16; Q3 (a); AI:37 (the create prompt). Accept: stage 2 unit. Test: sample and twin.
- **L148** A Vibe app name is checked and a planted leak blocks.
  - Src: A§:914 ("a Vibe prompt and app name"); BP:158.16 does not name it. Accept: stage 2 unit. Test: sample and twin. A§ only (X14).
- **L149** An AI column prompt is checked and a planted leak blocks.
  - Src: BP:158.16; Q3 (a); AI:72. Accept: stage 2 unit. Test: sample and twin. No finding of AI records a field shape for this kind (X14).
- **L150** A workflow's name is checked and a planted leak blocks.
  - Src: BP:158.16; A§:914. Accept: stage 2 unit. Test: sample and twin.
- **L151** A workflow's description is checked and a planted leak blocks.
  - Src: BP:158.16; AI:55 (name and description are read back from the workflow object). Accept: stage 2 unit. Test: sample and twin.
- **L152** A workflow's step text is checked and a planted leak blocks, including text in several steps of one workflow.
  - Src: BP:158.16; A§:914; AI:55, AI:59. Accept: stage 2 unit. Test: a leak in the third of four steps blocks. The step shape is X14.
- **L153** A sequence's step text is checked and a planted leak blocks.
  - Src: BP:158.16; A§:914. Accept: stage 2 unit. Test: sample and twin. Sequences were not probed (AI:76, X14).
- **L154** A sequence's recipient list is checked entry by entry: a recipient that is another client's person or an excluded term blocks, and the list passes when no entry hits.
  - Src: BP:158.16; AM:104 to 110 (A18, "recipients shown"); A§:914. Accept: stage 2 unit. Test: a list of three invented addresses with one in an excluded row blocks and names the entry.
- **L155** A webhook's URL is checked: a credential in it (user info, a token parameter) blocks, a record path in it blocks, and an excluded or another client's term in it blocks.
  - Src: BP:158.16, BP:158.17; AM:112 to 120; PLAN §7.15. Accept: stage 2 unit. Test: three invented URLs each carrying one of the three block, the twin passes. The URL exemption of the id rule is L73; the readings are X34.
- **L156** An agent plan, a Vibe prompt and an AI column prompt that carry a credential, an internal note, a record path or anything the lint would refuse in a client-facing document each block.
  - Src: AM:112 to 120 (A17: "a prompt never carries a credential, an internal note, or anything the leak lint would refuse"); BP:158.17. Accept: stage 2 unit. Test: one planted credential, one note, one path in each of the three prompt fields; nine blocks.
- **L157** A term of another client's entry reaches no account-level object: the same prompt, name and recipient fields block on a wall hit.
  - Src: BP:158.17, BP:158.19; AM:112 to 120. Accept: stage 2 unit. Test: the planted other-client name in an agent name, a Vibe prompt and a sequence recipient entry each blocks, with the two planted records.
- **L158** A payload whose kind the lint does not know is never passed unchecked: it is checked as generic strings or it exits 3.
  - Src: BP:158.32; BP:158.17. Accept: stage 2 unit. Test: a payload with an unnamed kind and a planted leak does not exit 0. How a kind is named is X22.
- **L159** A payload with no string value exits 0 with an empty findings list.
  - Src: A§:914. Accept: stage 2 unit. Test: `{"count": 3}` exits 0.
- **L160** Every AI kind named in L142 to L155 has a payload sample with one planted leak per field family and a clean twin in `tests/fixtures/leak/`, and the fixture self-test walks each one.
  - Src: PLAN Q3 (a), §4.1. Accept: stage 2 unit. Test: the fixture README lists each kind and field; the self-test asserts planted blocks and twin passes.
- **L161** The payload kinds and their field lists are pinned in `record-map.md` under `Pinned: leak`, and the script's copy agrees with the map.
  - Src: PLAN §8.12. Accept: stage 2 unit. Test: `tools/lint_plugin.py` compares the two lists and reports 0 errors.

### 2.12 Planned names, `drafts/`, `SUMMARY.md` and the build notes copy

- **L162** Planned names at the blueprint stage are each checked with the full name rules and the wall.
  - Src: A§:914; A§:922 ("every planned name"); BP:158.19. Accept: stage 2 unit. Test: a planned name holding an invented firm rendering blocks; one holding another client's name blocks on the wall.
- **L163** The blueprint's client-safe glossary is read and passes the run rule only; every other rule applies to glossary text as to any text.
  - Src: A§:920 ("exempt from the copied-run rule"). Accept: stage 2 unit. Test: a glossary line holding a marker blocks on the marker while its six-word run passes. This is the narrow reading of BP:158.10 (X36).
- **L164** Everything under `drafts/` is scanned, every `.md`, `.txt` and `.docx`, and a second scan at close-out gives the same result on the same bytes.
  - Src: A§:914; A§:916. Accept: stage 2 unit. Test: a drafts folder with one planted leak per file kind blocks each; two runs give equal findings.
- **L165** `SUMMARY.md` is scanned under the copied-run rule and the quote-length rule, and a planted leak of each blocks.
  - Src: BP:158.31; LT:14. Accept: stage 2 unit. Test: a `SUMMARY.md` holding a six-word run of an internal file blocks; one holding an eight-word quote blocks; the twin passes. Which other rules apply to it, and what its internal-file set is, are X37.
- **L166** A client-facing copy of the build notes passes the lint like a draft: the markers, the bare `[A]`, internal ids and record paths in it block, and a clean copy exits 0.
  - Src: AM:60 to 68 (A23, "passes the leak lint"); A§:914; BP:158.5. Accept: stage 2 unit. Test: a build-notes copy with one assumption written as a question passes; the same copy with `[A]` blocks.
- **L167** The lint has no rendered-file pass in v1: it reads `.docx` input because BP:158 asks for it, and it has no PDF reader and no call out to a PDF tool.
  - Src: A§:914 ("In v1 nothing is rendered"); BP:158.14; SF:90 (`pdftotext`, stale). Accept: stage 2 unit (inspection). Test: no `pdftotext` and no subprocess call in the script (L05). The stale lines are X05.

### 2.13 The cross-client wall and the index

All of this rests on Q1 (a). The floor, the normalisation, the term extraction and the index schema are gaps (X01, X02, X25 to X29).

- **L168** `leak_lint.py index` writes this record's entry into `<home>/clients-index.json`, keyed by the record's slug, and creates the file when it is absent.
  - Src: PLAN Q1 (a); A§:922; A§:440. Accept: stage 2 unit. Test: run on the first planted record in an empty home; the file exists with one entry. The entry's shape is X02.
- **L169** The entry holds the sha256 of the normalised client name.
  - Src: PLAN Q1 (a); A§:440; RM:76. Accept: stage 2 unit. Test: the hash of the normalised invented client name is in the entry; the normalisation is X28.
- **L170** The entry holds the sha256 of each normalised name of a person the record names.
  - Src: PLAN Q1 (a) ("its people"); BP:158.19. Accept: stage 2 unit. Test: each planted person name's hash is in the entry. Where the record names people is X26.
- **L171** The entry holds the sha256 of each normalised customer the record names, the client's own customers in full name and in acronym.
  - Src: PLAN Q1 (a) ("customers"); A§:918 ("a client's own customers as acronym and as full name"). Accept: stage 2 unit. Test: both spellings of a planted customer are in the entry.
- **L172** The entry holds the sha256 of each normalised partner the record names.
  - Src: PLAN Q1 (a) ("partners"). Accept: stage 2 unit. Test: each planted partner is in the entry.
- **L173** The entry holds the sha256 of each normalised product the record names.
  - Src: PLAN Q1 (a) ("products"). Accept: stage 2 unit. Test: each planted product is in the entry.
- **L174** The entry holds the sha256 of each normalised term of the record's `exclusions.md`, every strand's file.
  - Src: PLAN Q1 (a); PLAN §8.7. Accept: stage 2 unit. Test: one term from each of two strands' files is in the entry.
- **L175** The entry holds the sha256 of each client figure at or above the floor, as a normalised value, and no figure below it.
  - Src: PLAN Q1 (a) ("client figures above a floor"). Accept: stage 2 unit. Test: with a figure above and a figure below the floor in the record, only the first's hash is present. The floor and the value form are X25, X28.
- **L176** The index never holds plaintext of any name, term or figure of a record.
  - Src: A§:440 ("never plaintext"); RM:76; SF:90. Accept: stage 2 unit. Test: after `index`, search the file's bytes for every planted name, term and figure as text, in each of the five figure formats; none is found. The slug is the one plaintext field the sources allow (X21).
- **L177** `index` replaces this record's entry in place and leaves every other entry byte-equal; two runs on the same record give a byte-equal file.
  - Src: PLAN Q1 (a); L08. Accept: stage 2 unit. Test: write both planted records' entries, rerun the first, compare bytes to the second write.
- **L178** An entry stays in the index after its record moves to `archive/<slug>/`, so a closed client stays walled.
  - Src: PLAN Q1 (a). Accept: stage 2 unit. Test: write the planted record's entry, move the record folder to `archive/`, run the wall from the other planted record with a payload holding the first client's term; it blocks.
- **L179** A record's entry exists after init, is refreshed after every intake and is refreshed at close-out.
  - Src: PLAN Q1 (a); A§:922 ("refreshed at init and at close-out"); BP:321. Accept: stage 4 headless. Test: the callers (`record.py` and the intake skills, WP2 and WP7) run `index` at those three moments; the headless runner reads the home's index after each. WP4 owes only the action (L168); X02 holds who calls it.
- **L180** `index` opens only this record's files and the index file; it opens no file inside another client's folder.
  - Src: A§:922; AM:87 to 93 (A20); R8 (the precedent for a script that reads other records is for ids, and is not extended here without X21). Accept: stage 2 unit. Test: spy on opens during `index` with both planted records present; no path under the other record is opened.
- **L181** A second `index` run from another record, after the first, leaves both entries present; no entry is lost.
  - Src: A§:440 ("no cross-client lease file exists", D10); PLAN Q1 (a). Accept: stage 2 unit. Test: run `index` from record A, then from record B, then read both. Two runs at the same moment are X29.
- **L182** The wall blocks a payload name that matches a hash in another client's entry and is not in this record's own terms.
  - Src: BP:158.19, BP:158.20; PLAN Q1 (a). The terms of a free text that are hashed are X27. Accept: stage 2 unit. Test: the first planted record's payload holding the second client's invented name exits 1 with the rule `wall`.
- **L183** The wall blocks a payload term that matches a hash from another client's exclusions terms.
  - Src: BP:158.19 ("term"); PLAN Q1 (a). Accept: stage 2 unit. Test: the planted term blocks.
- **L184** The wall blocks a payload figure whose hash is in another client's entry and not in this record's own figures.
  - Src: BP:158.19 ("figure"); PLAN Q1 (a). Accept: stage 2 unit. Test: the planted other client's figure, in each of the five formats, blocks.
- **L185** The wall blocks a match on each of the five kinds of name an entry holds: client, person, customer, partner and product.
  - Src: PLAN Q1 (a). Accept: stage 2 unit. Test: five planted payloads, one per kind, each blocks.
- **L186** A payload with no term, name or figure of any other client's entry passes the wall and exits 0: the planted clean pass.
  - Src: BP:158.20; PLAN Q1 (a). Accept: stage 2 unit. Test: the clean payload on both planted records exits 0.
- **L187** A term that is in both this record and another client's entry passes the wall; it blocks only when it is in another entry and not in this record.
  - Src: BP:158.19 ("and not this client's record"); PLAN Q1 (a). Accept: stage 2 unit. Test: a vendor name shared by both planted records passes; a name only in the other record blocks.
- **L188** A name that differs from the entry's only in letter case gives the same hash on both sides and blocks. The full normalisation (punctuation, possessives, diacritics, spacing) is X28.
  - Src: PLAN Q1 (a) ("normalised names"); A§:440. Accept: stage 2 unit. Test: an upper-case payload name blocks against a title-case entry.
- **L189** The wall runs on every payload and every planned name, whichever command checks them, and it also runs alone for one planned name.
  - Src: A§:922; BP:158.19; PLAN §7.8. Accept: stage 2 unit. Test: a wall hit blocks through `payload`, through `blueprint`, and through the wall's own action.
- **L190** The wall reads the other clients' side only from `clients-index.json`, plus the folder names under `<home>/clients/` where X21 keeps them.
  - Src: A§:922; BP:158.19. Accept: stage 2 unit. Test: with the index emptied and the other record folder present, a payload holding that client's name passes the hash check (the slug check is X21); no file inside the other folder is opened.
- **L191** A payload holding the slug of another folder under `clients/` blocks, and one holding this record's own slug does not block on the wall.
  - Src: A§:922 ("and against the slugs of the other folders under `<home>/clients/`"); PLAN §7.1 (silent on slugs). Accept: stage 2 unit. Test: the planted slug blocks. Whether the slug check survives Q1 (a) is X21; this clause stays open until it is answered.
- **L192** A wall finding names the payload's own term and the rule `wall`, and carries no name, slug or figure that only the other record holds.
  - Src: A§:922; L29. Accept: stage 2 unit. Test: grep the output of a hit for every string that is only in the other record; none is found. Whether it may name the other client is X41.
- **L193** The wall is proved on the two planted records in one test file: one hit and one clean pass, with the first record as the payload's own and the second as the other client.
  - Src: BP:158.20; PLAN §4.1. Accept: stage 2 unit. Test: `test_leak_wall.py` builds both records in a temporary home, runs `index` for each, then the hit and the clean pass.
- **L194** The wall is symmetric: the same two records with the roles swapped give a hit and a clean pass the other way.
  - Src: BP:158.20; PLAN §4.1. Accept: stage 2 unit. Test: swap the roles in the same test and assert both outcomes.

### 2.14 `--terms` over `shared/`

- **L195** `terms` over a folder applies the index's digests to every text file under it and exits 1 when any digest matches, naming the file and the line.
  - Src: BP:114; PLAN Q1 (a). Accept: stage 2 unit. Test: a copy of a `shared/` folder with one planted client name exits 1 naming the file and line; the same copy without it exits 0.
- **L196** `terms` and the wall use the same digest function: a term the wall blocks, `terms` blocks.
  - Src: PLAN Q1 (a) ("`--terms` over `shared/` at release checks the same digests"). Accept: stage 2 unit. Test: run both on one planted term; both block. A source-level test asserts one shared function.
- **L197** `terms` over the shipped `shared/` folder does not report the shipped list's own terms (the plugin names, the method terms, the ids) as findings.
  - Src: LT:14 to 15 ("Internal files (the record, shared/, skills) legitimately contain these terms"); BP:114. Accept: stage 2 unit. Test: run over the real `shared/` with the two planted records indexed; exit 0. Which rules `terms` runs is X31.
- **L198** `terms` states in its output how many index entries it compared against, so a run against an empty index is visible.
  - Src: BP:114 ("proves nothing from any client input is in it"); L48. Accept: stage 2 unit. Test: the output holds the entry count; with no index file it holds zero. Open: X30, X31.
- **L199** At release, `terms` over the real `shared/` of the repository, against the home that holds the closed and open clients' entries, exits 0.
  - Src: BP:114. Accept: stage 4 headless. Test: the release check runs it on the release machine; owed to WP16's release checks.

### 2.15 Fail closed

- **L200** The shipped list missing, unreadable or holding a row that does not parse is exit 3 naming the file and the line.
  - Src: BP:158.32; A§:920. Accept: stage 2 unit. Test: rename the list; corrupt one `re:` row; each exits 3. Invalid rows are X33.
- **L201** `settings.json` unreadable, malformed, newer, or without a firm name is exit 3 (L40 to L42), and `leak-terms.txt` present but unreadable is exit 3.
  - Src: BP:158.32; PLAN §8.8. Accept: stage 2 unit. Test: make the local list unreadable (permissions or undecodable bytes); exit 3.
- **L202** A record file the lint must read to build a set (`exclusions.md`, an allowlist that exists, a call or document read for figures, quotes and runs) that cannot be read or decoded is exit 3, not skipped.
  - Src: A§:920; BP:158.32. Accept: stage 2 unit. Test: one undecodable `calls/` file in the record variant exits 3 naming it.
- **L203** An index that is malformed, newer or unreadable is exit 3 (L47).
  - Src: G57; BP:158.32. Accept: stage 2 unit. Test: as L47.
- **L204** An input file or payload that is unreadable, undecodable, not a zip (for `.docx`), not JSON (for a payload) or of an unreadable kind is exit 3.
  - Src: BP:158.32. Accept: stage 2 unit. Test: one case each.
- **L205** An unexpected exception inside any rule is exit 3 with the envelope; no traceback reaches the caller as a pass and no exit 0 follows a rule that did not finish.
  - Src: G10 ("an unexpected exception"); BP:158.32. Accept: stage 2 unit. Test: patch one rule to raise; exit 3 and `error` present.
- **L206** Python below 3.9 is exit 3 before any other work, with the envelope.
  - Src: G10; AM:42. Accept: stage 2 unit. Test: unit test of the version check function with an injected version tuple.
- **L207** There is no path to exit 0 when an input could not be read: a failure injected at each file read of a run, one read at a time, always gives exit 3.
  - Src: PLAN §3 (step 7); BP:158.32. Accept: stage 2 unit. Test: a spy raises `OSError` at the first, second, third and every later open of one run; every run exits 3.
- **L208** A run that exits 3 never reports exit 0 or 2 for any part of the work, and findings found before the failure may appear but do not lower the exit code.
  - Src: BP:158.32; A§:920. Accept: stage 2 unit. Test: a run with one blocked input and one unreadable input exits 3.
- **L209** Every caller treats exit 3 as fail-closed: no payload is sent, no draft is marked ready, and the blueprint stage does not proceed. The lint's API note states this for callers; the callers prove it.
  - Src: BP:158.32; A§:920; BP:252. Accept: stage 4 headless. Test: the callers' rows (the write path of WP9, the hook of WP13, `call-intake`) force exit 3 and show no write; WP4 owes the note, listed not failed. See X47.
- **L210** The hash of every input read is in the output even on exit 1, so a blocked payload can be told from the one that is fixed and retried.
  - Src: PLAN §7.16. Accept: stage 2 unit. Test: a blocked payload's output holds its hash; the edited payload's hash differs.

### 2.16 Redaction written, not defaulted, and A11

- **L211** Redaction behaviour is written and not defaulted: a way to report the spans a redaction would remove exists, nothing calls it by default, and nothing in any file is removed or edited.
  - Src: BP:158.33; PLAN §8.9; BP:19. Accept: stage 2 unit. Test: `scan` with the spans option lists start and end offsets for each blocking finding and edits nothing; the default run leaves every byte as it was. Reconciling this with "never edit" is X23.
- **L212** The lint's output does not vary with the A11 fields of the record: the same input gives the same findings with `transcript_redaction` set to `unanswered` and to another value.
  - Src: BP:19 ("no default may be assumed"); BP:158.33. Accept: stage 2 unit. Test: two copies of one record variant differing only in that field; equal output.
- **L213** No subcommand reads or writes an account, and nothing in the output or the tests names an account, a workspace or an object id.
  - Src: BP:13, BP:17 (A11-1); CLAUDE.md of the project; L10. Accept: stage 2 unit. Test: search the script, the tests and the fixture for monday id patterns of eight or more digits outside the planted id cases; the planted ones are invented numbers.

### 2.17 The trap fixture (`tests/fixtures/leak/`)

The fixture is the specification the lint is graded on: every planted case has a clean twin, so false positives count as much as misses. These clauses are written so that a reader who sees no code can check them from the fixture's own README (L221).

- **L214** The fixture folder holds the planted text and its clean twins, the payload samples, the two planted client records under `records/`, a test `settings.json`, a `.gitattributes` and a `README.md`; `.docx` samples are not files in it (L225).
  - Src: PLAN §4.1; BP:156. Accept: stage 2 unit (inspection). Test: list the folder; each named item is present and no binary file is present.
- **L215** Every planted case names the rule it plants and the A§:918 trap category or BP:158 rule case it stands for, and has an expected outcome (blocks, or reported and kept, or caution).
  - Src: BP:158.30; PLAN §3 (step 4). Accept: stage 2 unit. Test: the self-test reads the README table and fails on a case with no rule, no category or no expected outcome.
- **L216** Every planted case has a clean twin that keeps the sentence's shape and carries none of the leak, and each twin passes: no blocking finding.
  - Src: BP:158.30; BP:368.1; A§:918 ("Each has a clean twin"). Accept: stage 2 unit. Test: the self-test runs the lint over every twin and asserts no block; it runs it over every planted case and asserts the expected outcome.
- **L217** Every name, figure, firm name, rendering and id in the fixture is invented, including the phonetic pair (an invented firm name and an invented ordinary word that sounds like it); nothing names a real person, a real firm, the user's own firm, or any monday account, workspace or object.
  - Src: AM:159 to 163 (A12); BP:158.30; PLAN §8.11. Accept: stage 2 unit (inspection). Test: the README states each name as invented; the sweep of `tools/agnostic_sweep.py` runs over the fixture once WP16 builds it (X18); until then the self-test and the trace check enforce it.
- **L218** Nothing in the fixture is copied from an answer key, a transcript of the fixtures workspace, a call or an earlier plugin: no run of six words in common with any of them.
  - Src: A§:918 ("not from any call", D24); PLAN §3 (step 4). Accept: stage 2 unit (inspection). Test: a throwaway probe outside the repository compares every fixture line with the arrays and transcripts for shared runs and reports none; the probe is not part of the repository.
- **L219** No term of the shipped list appears in any clean twin, so a twin that fails fails for a real reason.
  - Src: PLAN §3 (step 4). Accept: stage 2 unit. Test: the self-test runs the shipped list's literal and regular-expression rows over every twin file and asserts no hit (other than rows the twin is meant to carry, listed in the README).
- **L220** Every fixture file is LF, UTF-8, no byte-order mark, and a `.gitattributes` keeps every file LF on both systems.
  - Src: G11; PLAN §4.1. Accept: stage 2 unit; Windows run. Test: check bytes; the Windows run checks the files after a clone.
- **L221** The README holds one table row per planted case: the file, where the planted text is, the rule, the category, the expected outcome, the twin file and why the twin is clean; the self-test asserts the rows and the files agree in both directions.
  - Src: PLAN Q4 (a) (a reader who sees no code can check it); PLAN §4.1. Accept: stage 2 unit. Test: delete a file or add one without a row; the self-test fails.
- **L222** The README states what the fixture cannot prove: that the categories of A§:918 are the whole set, that a client's real vocabulary behaves like the invented one, the false-positive rate on real client text, and anything about a language other than English.
  - Src: PLAN §4.2. Accept: stage 2 unit (inspection). Test: the four statements are present.
- **L223** The test settings file holds the invented firm name and its renderings in the `settings/1` shape, and each test copies it into its temporary `MMB_HOME`.
  - Src: PLAN §4.1, §8.11; RM:76. Accept: stage 2 unit. Test: the file parses as `settings/1`; the tests never read it from the fixture folder directly.
- **L224** The two planted client records are text files under `records/`, each holding what the lint reads (`CLIENT.md`, a call summary with a marked client-safe block, a document snapshot with conflict rows, an `exclusions.md`, an `allowlist.md` where a case needs one, a client document in `inputs/`); each test's setup copies them into a temporary home.
  - Src: PLAN §4.1, §8.4; BP:156. Accept: stage 2 unit. Test: after setup the temporary home holds both records; the fixture folder is unchanged after the test.
- **L225** `.docx` samples are built by the tests from XML strings with `zipfile`, with leaks planted in the body, in `docProps/core.xml` and in `docProps/app.xml`; no binary file enters the repository.
  - Src: PLAN §8.3; BP:156. Accept: stage 2 unit. Test: the tests create the three samples in a temporary folder; the repository holds no `.docx`.

Each clause from L226 to L248 is one trap category of A§:918, planted as text with a clean twin. Each is accepted when the planted case behaves as the README says and the twin passes (L216). Where a string rule has no obvious reach for the category, the expected outcome is set by the decisions step (X06) and the clause is met when the lint gives it.

- **L226** Case-varied organisation names.
  - Src: A§:918; BP:158.30. Accept: stage 2 unit. Test: planted and twin as L216.
- **L227** Possessive organisation names.
  - Src: A§:918; BP:158.30. Accept: stage 2 unit. Test: as L226.
- **L228** Comma-split organisation names (X32).
  - Src: A§:918; BP:158.30. Accept: stage 2 unit. Test: as L226.
- **L229** An identifier that appears only in a header.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L230** Alias-map entries that are ordinary words.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226; the twin uses the same ordinary word in its everyday sense.
- **L231** Names harvested from the body rather than the roster.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L232** A client's own customers as an acronym.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L233** A client's own customers as a full name.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L234** The seller's own commercial terms.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L235** Dates whose digits are split.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L236** An assessment of a named individual.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L237** Small talk.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L238** Third parties named in passing.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L239** A partner name that reads as two ordinary words.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L240** A client's name corrupted inside hypotheticals in a file with no header.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L241** A product name that is an ordinary word fused to a preposition.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L242** Two vendors' names substituted for each other.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L243** An email address with its separator lost.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L244** Several client first names inside one quotation.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L245** A counterparty, its part-owner and its tools in one sentence.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226.
- **L246** A hypothetical about a named person leaving the business.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L247** The seller's own internal account structure.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).
- **L248** A health or nationality remark about an absent person.
  - Src: A§:918. Accept: stage 2 unit. Test: as L226 (X06).

The next clauses are the rule cases of BP:158 and PLAN §4.1, each planted with a twin.

- **L249** A planted figure in all five formats (`45000`, `45,000`, `45k`, `$45k`, "forty-five thousand") against a record holding it, and a twin with an unrelated figure.
  - Src: BP:158.2; PLAN §4.1. Accept: stage 2 unit. Test: five planted lines block; the twin passes.
- **L250** A planted document carrying a figure only in split renderings, and its twin.
  - Src: BP:158.24; PLAN §4.1. Accept: stage 2 unit. Test: the planted document fails; the twin passes.
- **L251** A planted six-word copied run, the same run inside a client document in `inputs/` (passes), and inside that snapshot's conflict rows (blocks).
  - Src: BP:158.3, BP:158.11, BP:158.12; PLAN §4.1. Accept: stage 2 unit. Test: three placements, three expected outcomes.
- **L252** A planted eight-word client quote and a twin of seven words in the same shape.
  - Src: BP:158.4; PLAN §4.1 ("an eight-word quote"). Accept: stage 2 unit. Test: the quote blocks on the quote rule.
- **L253** All nine markers, one planted line each, and a twin with ordinary brackets.
  - Src: BP:158.5; PLAN §4.1. Accept: stage 2 unit. Test: nine blocks; the twin passes.
- **L254** Internal ids (pain, number, stakeholder, objection, commitment and criterion ids, element keys, probe ids) and a twin with look-alike ordinary text.
  - Src: BP:158.6; PLAN §4.1. Accept: stage 2 unit. Test: the ids block; the twin passes.
- **L255** Record paths in Windows and POSIX spelling, and a mixed one, with a twin that names ordinary words without a separator.
  - Src: BP:158.7; AM:40 to 44. Accept: stage 2 unit; Windows run. Test: each spelling blocks.
- **L256** HTML comments, with a twin holding a plain tag.
  - Src: BP:158; PLAN §4.1. Accept: stage 2 unit. Test: blocks and passes.
- **L257** An eight-digit invented number outside a link (blocks) and the same number inside a link (passes).
  - Src: BP:158.8; PLAN §4.1. Accept: stage 2 unit. Test: two placements, two outcomes.
- **L258** The marked client-safe block of a call summary, of a document snapshot, and the glossary (each passes the run rule), each beside the same text outside the mark (blocks).
  - Src: BP:158.9, BP:158.10; PLAN §4.1. Accept: stage 2 unit. Test: three passes and three blocks.
- **L259** A run made mostly of common words, ignored, with a twin run of client vocabulary that blocks.
  - Src: BP:158.13; PLAN §4.1. Accept: stage 2 unit. Test: one passes and one blocks.
- **L260** Three tool categories in one sentence of a proper-noun-free paragraph (fails) and two (passes).
  - Src: BP:158.25; PLAN §4.1. Accept: stage 2 unit. Test: one fails and one passes.
- **L261** The firm's renderings, its phonetic variants, its whitelisted uses and one ordinary word that sounds like it (passes).
  - Src: BP:158.27 to BP:158.29; PLAN §4.1. Accept: stage 2 unit. Test: renderings and variants block; whitelisted use and ordinary word pass.
- **L262** The "flag, do not remove" group and the "caution" case, rebuilt as invented text in the same shape the keys describe.
  - Src: BP:158.22, BP:158.23; PLAN §4.1. Accept: stage 2 unit. Test: the group is reported and the file is unchanged; the caution case behaves as L121.
- **L263** Planted credentials in each shape of L76, a planted internal note, and an excluded term in each payload field kind, each with a twin.
  - Src: BP:158.17, BP:158.18; PLAN §4.1. Accept: stage 2 unit. Test: each blocks; twins pass.
- **L264** Planted allowlist rows that attempt to clear a figure, a quote, a copied run, a marker, an id, an exclusion and another client's name (none clears), and one row that clears a method term.
  - Src: BP:158.21; PLAN §4.1. Accept: stage 2 unit. Test: seven blocks stay; one clears with a caution.
- **L265** Payload samples for every standard kind (name, description, label, seed value, doc markdown, automation request text) with one planted leak per kind and a clean twin.
  - Src: BP:158.15; PLAN §4.1. Accept: stage 2 unit. Test: the self-test walks each sample.

### 2.18 What needs WP14: the twenty-five keys and the seed home

- **L266** Every class of leak that BP:448 names has a planted case and a twin in the trap fixture: cost totals and components in numeric, comma, `$`, `k` and spoken forms; loaded rates and cost inputs; write-off, loss and threshold amounts; objection text; stakeholder assessments; remarks about colleagues; failure narratives; alternatives in play; method vocabulary, pain ids and evidence markers; customer or member personal data. The decisions step reads the arrays to choose the cases and writes the cases into the fixture notes without copying any entry.
  - Src: PLAN Q2 (a); BP:448; BP:157. Accept: stage 2 unit (inspection). Test: `fixture-notes.md` lists each class against one planted case in the README; no line of any array is reproduced (L218).
- **L267** The leak grader of WP14 reads each fixture's `expected_leak_blocklist` array and scores each entry against the lint's run over that seed record's payloads and drafts; the arrays are prose entries and the grader owns how each is matched.
  - Src: BP:323; BP:448; PLAN Q2 (a), §7.13. Accept: stage 4 headless. Test: the grader runs on the twenty-five keys; owed to WP14, listed in the checklist and not failed. The count (25 arrays, 400 entries) against BP:448's 158 is X13.
- **L268** The two deliberate non-removals are scored on the seed records: the "flag, do not remove" group (s1, s5, s6, s10) is reported and kept, and the blocked word that is the client's own vocabulary (s2) survives with a caution.
  - Src: BP:158.22, BP:158.23; BP:448. Accept: stage 4 headless. Test: the grader's rows for those fixtures; owed to WP14.
- **L269** In a headless run the lint reads the seed home's `clients-index.json`, which holds one other client's digest, and a payload holding a planted term of that other client blocks.
  - Src: BP:321; BP:158.19. Accept: stage 4 headless. Test: the headless runner sets `MMB_HOME` to the seed home and the grader asserts the block; owed to WP14.
- **L270** The checklist lists the headless clauses (L179, L199, L209, L267 to L269) as owed to WP14 and WP16 and counts them apart from the clauses met by test.
  - Src: PLAN §6, Done means. Accept: stage 2 unit (inspection). Test: the checklist's totals add up to the clause total.

### 2.19 Pins, shared edits and the write path

- **L271** `record-map.md` carries a `Pinned: leak` section that holds the nine markers, the payload kinds and their field lists, the client-safe block marks and the glossary mark, the `clients-index/1` shape, and the row forms of `allowlist.md` and `exclusions.md`.
  - Src: PLAN §8.12, §7.9; RM:42, RM:43. Accept: stage 2 unit (inspection). Test: the heading and each item are present; the contents are the decisions step's (X02, X09, X22).
- **L272** One tuple joins the `PINNED` list of `tools/lint_plugin.py`, and the tool reports 0 errors, so the tool proves that the script and the map agree.
  - Src: PLAN §8.12, step 3. Accept: stage 2 unit. Test: run the tool; 0 errors; alter one marker in the script and see an error.
- **L273** The shipped `leak-terms.txt` names nine markers and carries a row for the bare `[A]`, and its comment says nine.
  - Src: PLAN §7.3, step 3; A§:627; LT:146. Accept: stage 2 unit. Test: the file's markers class holds the nine; the comment says nine.
- **L274** The common-word list (about a thousand English words) is embedded in the script between pinned markers; it is not a new `shared/` file; English only.
  - Src: PLAN §8.5; A§:920. Accept: stage 2 unit (inspection). Test: the markers exist and the list length is in the checklist; no new file under `shared/`. Open: X19.
- **L275** The tool-category vocabulary is shipped in `leak-terms.txt` under a class the lint counts and does not block.
  - Src: PLAN §8.6. Accept: stage 2 unit. Test: the class is in the file; a sentence with one of its words exits 0 (L111). Open: X12.
- **L276** The shared edits leave WP2's and WP3's tests passing under both interpreters, and `record.py`, `ledger.py` and `mmb_common.py` are byte-equal to their copies before WP4.
  - Src: PLAN §3 (steps 3, 5), §8.10. Accept: stage 2 unit. Test: the whole suite passes; hash the three scripts before and after.
- **L277** The lint's API note says where the lint sits in the write path (after `ledger.py intent`, before the call, as BP:252 orders them), what a caller reads (the exit code and the input hashes) and that exit 3 is a stop.
  - Src: BP:252; A§:798; PLAN §7.16. Accept: stage 2 unit (inspection); stage 4 headless (the callers' side). Test: `API-leak_lint.md` holds the paragraph; the callers' rows follow the order.

### 2.20 Time stamps and the wall on drafts

- **L278** Any machine timestamp the lint writes (in an index entry, if the settled shape carries one) is UTC as `YYYY-MM-DDTHH:MM:SSZ` from the one clock of `mmb_common`, and the lint's output carries no local time.
  - Src: G40; MC:now_utc. Accept: stage 2 unit. Test: patch the clock; the written stamp equals the patched UTC value in that form. Whether the entry carries a stamp is X46.
- **L279** A draft that holds another client's name, term or figure blocks on the wall, as a payload does.
  - Src: A§:916 (the wall is among what the lint blocks on every surface of A§:914); A§:922 (names `payload` and planned names only); BP:158.19. Accept: stage 2 unit. Test: the planted other-client name in a file under `drafts/` exits 1 with the rule `wall`. Open: X45.

---

## 3. Shapes

Each shape is copied from the source that gives it. Where the sources are silent the shape is not written; section 4 lists the gap. Nothing here picks a side.

### 3.1 The nine evidence markers (A§7.5:615 to 625; RM:258 to 270)

A§:627 and RM:272: `leak_lint.py` blocks all nine in `drafts/` and every monday payload. The markers live in `research/`, `calls/`, `inputs/`, `readiness.md` and the internal parts of the blueprint.

| Marker | Meaning (A§:617 to 625, shortened) | Required with it |
|---|---|---|
| `[Q]` | client quote, verbatim, never tidied | speaker role, side, location in the transcript (`@00:12:31`, `cue 82`, `cues 82-85`, `L142-144`) |
| `[Q?]` | quote with an unclear speaker | as `[Q]`, plus a note |
| `[Q/side]` | side-only quote, speaker not resolvable | the side, the unit or block range, a note |
| `[Q/recon]` | a sentence assembled from several units | as `[Q]`, plus every unit number |
| `[Q/doc]` | a verbatim extract from a client document or email | the document and its section or page, the author or sender by role where known, the input's date and status |
| `[X]` | quarantined: spoken inside a demonstration frame or under a hypothetical marker | the frame's location and the reason |
| `[E]` | external fact from a dated source | source key `S#` from the register |
| `[I]` | inference | its basis and a confidence word |
| `[A]` | assumption: a build decision made without evidence, never written into monday as if the client had said it | its basis, the question that would replace it, and once reported, the client's confirmation or explicit acceptance |

### 3.2 The leak-terms syntax (LT:17 to 29), copied

```text
Syntax. One term per line. A line starting with # is a comment; blank lines are ignored.
  term               a literal, matched case-insensitively wherever the characters on
                     either side are not letters or digits
  class: <name>      every line below, until the next class:, belongs to this class,
                     and the lint reports the class beside each hit
  re: <pattern>      a Python regular expression, matched case-insensitively
  phonetic: <term>   the term is also matched by the phonetic-variant rule of 9.6,
                     which catches renderings this list does not spell out
  whitelist: <term>  a legitimate use the phonetic rule directly above it never blocks;
                     the test suite asserts no false positive on it
The per-client allowlist may clear a row of class method only. Rows of every other class
are never cleared by an allowlist (9.6). A term that is also the client's own vocabulary
survives with a caution rather than being removed.
```

The shipped file's classes, in order (LT:31 to 195): `firm` (empty on purpose), `plugin`, `assistant`, `method` (including the grade patterns), `pain-ids` (including element keys and versions), `markers`, `id-patterns` (paths, record file names, HTML comments, eight-digit ids, 64-character hashes, probe and design ids, `[A<n>]` tags and `[L14]` to `[L18]` flags). It has no class for tool categories and no row for the bare `[A]`.

### 3.3 The `firm` block of `settings/1` (RM:76; A§5.3:346)

```text
local/settings.json  (settings/1):
  schema, created (a date), plugin_version,
  firm {name, renderings[]}        for the leak list
  default_build_account {slug, id}, never_show_workspaces[] of {id, name} (possibly empty),
  archive ("local" | "github"), github_account (only when archive is "github")
  every id a string
local/leak-terms.txt  the per-user additions to the shipped list (zero-byte at `home init`, G58)
```

`home init` creates `local/leak-terms.txt` as a zero-byte file and writes `local/settings.json` (G58). The shape has no field for a phonetic rule or a whitelist.

### 3.4 The index, as far as the sources state it

No source gives a schema. What each says:

| Source | Statement |
|---|---|
| A§:440 | `clients-index.json` is "sha256 of normalised client names only, never plaintext; the lint's wall reads it" |
| RM:76 | listed among the paths under the home: "sha256 of normalised client names only" |
| A§:922 | "holds only sha256 hashes of normalised client names, refreshed at init and at close-out"; checked together with "the slugs of the other folders under `<home>/clients/`" |
| SF:90 | the same, "reads as empty while it does not exist yet" |
| BP:158 | "the hashed vocabulary digest every other client record under the home publishes into `clients-index.json`": a name, term or figure |
| BP:321 | a seed home holds "a `clients-index.json` with one other client's digest" |
| G58 | `home init` does not create it; "written at a record close and whose absence its readers treat as empty" |
| PLAN Q1 (a) | each record's entry holds hashes of its normalised names (client, people, customers, partners, products as the record names them), the terms of its `exclusions.md`, and its client figures above a floor; `leak_lint.py index` writes it at init, after every intake and at close-out; an entry stays after the record moves to `archive/`; the schema name pinned in PLAN §7.2 is `clients-index/1` |

### 3.5 The JSON envelope and the exit codes (G10; W91)

```text
every command:   {"ok": <the exit code is not 1>, "command": "<name as typed>", ...payload}
a refusal-like result (exit 1): findings, each {"file", "field", "problem", "expected"}
a could-not-run (exit 3):       "error": {"file", "field", "problem", "expected"}
file: record-relative, POSIX spelling; a whole-file error names the field "(whole file)"
```

| Exit | When (this package's constraint) |
|---|---|
| 0 | clean: nothing to report |
| 1 | blocked: at least one blocking finding |
| 2 | warnings only |
| 3 | could not run: fail closed, every caller stops |

W91's envelope reads `"ok"` as true unless the exit code is 1, which makes `ok` true on exit 3. X41 holds the question for a gate.

### 3.6 The exemptions, the rows the lint reads, and the three paraphrase categories

- **Exemptions (A§:920; RM:21, RM:24):** the marked client-safe block in each call summary (`calls/<date>-<type>.md`) and input snapshot (`inputs/<date>-<title>.md`), the blueprint's client-safe glossary, and any run that matches the text of a client document or email in `inputs/` are exempt from the copied-run rule. RM:21 and RM:24 give the column "the marked client-safe block only"; no mark is pinned.
- **Allowlist row (RM:42):** `solution/allowlist.md`, "solution-blueprint, with the user's OK per row", 80 lines. **Exclusions row (RM:43):** `solution/exclusions.md`, "engagement seeds it at new client; the user and call-intake add rows ...; solution-blueprint, the sample-data step and the lint read it", 80 lines. A§:370: the exclusions are "names, terms and figures that sample rows, agent prompts and Vibe prompts must never carry". No row syntax is pinned.
- **The five figure formats (A§:916):** 45000, 45,000, 45k, $45k, "forty-five thousand".
- **The three paraphrase categories (A§:916):** personal and emotional stakes; remarks by client staff about colleagues; our own internal assessments of people.
- **The two assertions (A§:918):** a document that carries a figure only in its split renderings (digits broken across tokens, a number spelled across a line break) fails; a proper-noun-free paragraph that names three of the client's tool categories in one sentence fails.

### 3.7 The trap categories (A§:918), copied in order

case-varied, possessive and comma-split organisation names; an identifier that appears only in a header; alias-map entries that are ordinary words; names harvested from the body rather than the roster; a client's own customers as acronym and as full name; the seller's own commercial terms; dates whose digits are split; an assessment of a named individual; small talk; third parties named in passing; a partner name that reads as two ordinary words; a client's name corrupted inside hypotheticals in a file with no header; a product name that is an ordinary word fused to a preposition; two vendors' names substituted for each other; an email address with its separator lost; several client first names inside one quotation; a counterparty, its part-owner and its tools in one sentence; a hypothetical about a named person leaving the business; the seller's own internal account structure; and a health or nationality remark about an absent person. Each has a clean twin.

### 3.8 The AI kinds' fields, as the sources state them

| Kind | Fields named by BP:158 (stage 4b there) | Fields named by A§:914 | What AI says exists |
|---|---|---|---|
| Agent | name, role, goal, plan | name, role, plan, knowledge-grant names | `profile` (name, role, role description, avatar, colour), `goal`, `plan` (markdown), `user_prompt` (metadata), knowledge grants (a board or doc, READ or READ_WRITE), triggers, skills (AI:10, AI:18 to 20) |
| Vibe app | a Vibe prompt | a Vibe prompt and app name | `vibe_create` takes a natural-language prompt, an optional workspace, board ids, a view id, a model; the app has `name` (AI:35, AI:37) |
| AI column | an AI column prompt | an AI column's prompt | not probed; eight `configure_*_ai_column` mutations exist and were not exercised (AI:72, AI:76) |
| Workflow | name, description, step text | name, description and step text | `create_workflow` makes an object with name, description, privacy, folder, state; the expert states each binding of a draft except dynamic (templated) text (AI:55, AI:59) |
| Sequence | step text and recipient list | step text | not probed (AI:76); A18 says recipients are shown on the card (AM:104 to 110) |
| Webhook | URL | URL | `create_webhook` exists in raw GraphQL and was not exercised (AI:72, AI:76) |

## 4. Gaps and contradictions

Each entry is something the sources leave unspecified or state two ways, so a coder would have to decide. Nothing here is resolved. Each gives the readings with their anchors and the clauses it touches. Entries X01 to X20 are the entries of `PLAN.md` section 7, in its order, with the result of re-checking each anchor; X21 to X47 are found while writing the clauses. The numbers are stable ids and not an order of importance, and the decisions step answers them one by one.

### The wall and the index

- **X01 The wall's contents (PLAN §7.1; answered in part by Q1 (a)).** BP:158 has every other record publish a "hashed vocabulary digest" and the lint fail on a name, term or figure; A§:922, A§:440, RM:76 and SF:90 have the index hold hashes of normalised client names only. The user chose BP's form (Q1 (a)). Still open after the answer: the value of the floor (X25), the normalisation (X28), where the record's names live (X26), how a payload's terms are extracted (X27), and the design touch-ups to A§9.6, A§7.1, RM:76 and `safety.md` section 6, which follow at the user's word. Touches L168 to L194.
- **X02 The index has no writer, no schema and no owner row (PLAN §7.2).** A§:922 says it is refreshed at init and at close-out; G58 says it is "written at a record close" and that `home init` does not create it; `record.py` writes nothing of it; RM:76 lists it with no schema and no row in the file map; Q1 (a) adds "after every intake" and names `leak_lint.py index` as the writer. Not stated: the schema (PLAN §7.2 reads `clients-index/1`), how entries are keyed (by slug, by a hash of the client name), what the entry holds beyond the digests (a version, a count, a stamp, the record's state open or archived), whether a record at init holds anything but its client name, and who calls `index` at each moment (`record.py init` and `record.py close` would call another script; the intake skills would run a command; or the session). Touches L168 to L181, L179, L271.
- **X21 The slugs of the other folders (not in PLAN §7).** A§:922 and SF:90 add a second check to the hashes: the slugs of the other folders under `<home>/clients/`. BP:158 and Q1 (a) mention only the digest. A slug is plaintext and may be the client's name; the index in A§:440 is "never plaintext". Open: whether the slug check stays; whether archived folders' slugs are checked (they are not under `clients/`); whether the slug is the key of the index entry in plaintext. Touches L176, L190, L191.
- **X26 Where a record's own names live.** Q1 (a) says "its people, customers, partners and products as the record names them". No source says which file or field holds each: `CLIENT.md`, the alias map in a call summary, `readiness.md`, `structure-inventory.md`, `blueprint.md` are all candidates; A§:918 has "names harvested from the body rather than the roster" as a trap. Open: which files are read for names, whether names are taken from a roster field or harvested from body text, and how a person is told from a product. Touches L169 to L173.
- **X27 How a payload's terms are extracted for the wall.** A hash can only be compared with the hash of a candidate string. A payload is free text. Not stated: the candidate strings (every word, every run of two to n words, capitalised runs only), the largest n, and what happens to a client whose name is one ordinary word (a hit on every use of that word, or an exception). A§:918 has "a partner name that reads as two ordinary words". Touches L182 to L187.
- **X28 Normalisation, and what protects the hashes.** Q1 (a) says "normalised" and A§:440 says "normalised client names"; no source gives the normalisation (case, punctuation, possessives, diacritics, spacing, a legal suffix such as "Inc"), nor whether the hash is salted. An unsalted sha256 of a short name can be reversed by trying a list of names; no source says whether that matters for a file under the user's own home. Touches L169 to L175, L188.
- **X29 One shared file written by many records.** A§:440 says "no cross-client lease file exists" (D10). The index is one file under the home written from every record's session. Not stated: whether a write is atomic, whether two sessions at the same moment lose an entry, whether the old bytes are backed up (as `mmb_common.write_file` does under the record, G39, into `.work/backup/`, which a home file has no record for), and whether an entry for a record that no longer exists can be removed. Touches L177, L181.
- **X30 An absent index while other records exist.** SF:90 and G58: an absent index reads as empty. A§:920 and BP:158.32: fail closed. A home with three clients and no index file is a lint that cannot see the wall; reading it as clean lets a payload pass unchecked. Open: whether absence is exit 3 once the home holds another record, or a warning, or silent; what the wall says to the user. Touches L48, L198.
- **X45 Whether the wall runs on `drafts/` (not in PLAN §7).** A§:916 lists other clients' names among what the lint blocks, and A§:914 lists `drafts/` among the surfaces; A§:922 says `--wall` "runs on every payload and every planned name" and says nothing of drafts; BP:158 gives the wall to `--payload` only. Touches L279.
- **X46 A time stamp in an index entry.** G40 sets UTC `Z` for machine timestamps; no source says an entry carries one. Touches L278.

### Markers, paths and lists

- **X03 Nine markers, eight listed; paths in one spelling (PLAN §7.3).** A§:627 and RM:272 have the lint block all nine; LT:146 says "eight", and its markers class has no bare `[A]` (its `\[A\d{1,2}(-\d)?\]` at LT:194 matches amendment tags only). BP:158 names `[A]` and `[Q/doc]`. Separately, the path rows at LT:172 to 179 are POSIX forms (`clients/...`, `.work/`) and only the user-directory row at LT:173 has a Windows form, while BP:158 and A24 ask for record paths in both spellings. Owed: one row and one comment in `leak-terms.txt`, and Windows-spelling rows or a rule in the script (step 3). Touches L63, L66, L68, L69, L273.
- **X04 Where the firm's renderings live (PLAN §7.4).** A§:916, BP:158.27 and RM:76 put them in `local/settings.json` (`firm {name, renderings[]}`); G58 makes `local/leak-terms.txt` an empty seed; LT:5 to 6 and LT:31 to 36 say the walkthrough writes them into `local/leak-terms.txt`. Reading in the plan: `settings.json` is the source and the local list holds per-user additions. Touches L38, L39, L41, L49.
- **X07 One user's firm in a shipped file (PLAN §7.7).** SF:86 says "the user's own firm name is a near-homophone of a common word", which describes one user; A12 and A22 want nothing user-specific in `shared/`. A touch-up for the user's word. Touches L54.
- **X12 The client's tool categories (PLAN §7.12).** A§:918 and SF:84 speak of "the client's tool categories"; the record has no field for them and `leak-terms.txt` has no category vocabulary. PLAN §8.6 reads: a shipped vocabulary under a counted class, any three distinct categories in one sentence of a proper-noun-free paragraph fail, whether or not they are the client's. Open: the vocabulary, how a sentence and a proper noun are told, and whether a paragraph the client owns (in a client document) is subject. Touches L107 to L111, L275.
- **X17 The pain-id patterns (PLAN §7.17).** LT:130 to 143 block `S3`, `C1`, `P1`, `N2`, `O4`, `R7` and the like, and only the `method` class may be cleared (LT:27). An ordinary text with a stakeholder "S1" or a support tier is blocked with no remedy except rewriting. The clean twins will show the cost. Touches L58, L59.
- **X19 No word list in the standard library (PLAN §7.19).** A§:920 and BP:158.13 say "runs made mostly of common words" with a filter "tuned on the leak-trap fixture". Not stated: the list, its size (PLAN §8.5 reads about a thousand English words), the threshold ("mostly": half, two thirds), and whether the filter applies to quotes. Touches L98, L99, L274.
- **X33 The local list and a row that does not parse.** LT:17 to 29 does not say: what class applies to a row above the first `class:` line of a local file; what happens to an invalid `re:` pattern (skipped, or exit 3); whether a `whitelist:` row below a non-phonetic row is an error; whether a missing `local/leak-terms.txt` (an older home) is empty or exit 3. A§:920 and BP:158.32 say fail closed. Touches L38, L200.
- **X32 The phonetic rule, "comma-split" and the whitelist's home.** A§:918 and LT:23 to 26 name a "phonetic-variant rule" and give no algorithm; the standard library has none. "Comma-split organisation names" (A§:918) is not defined (a name written "Example, Firm", or a name followed by a comma and a suffix). RM:76's `firm` has no whitelist or phonetic field, so a whitelist for a firm rendering can live only in `local/leak-terms.txt` as `whitelist:` rows. Open: the algorithm and its reach; whether the rule applies to every rendering or to each `phonetic:` row; where a firm whitelist is written. Touches L51 to L54, L228.
- **X44 The personal-names index (not in PLAN §7).** RM:76 lists `personal-names-index.json` under the home as "the lint's name list"; A§:346 and A§:440 do not list it; BP:114 names a "local name index" for `agnostic_sweep.py`; SF:88 says "Warnings, not blocks: ... personal names absent from the SOP's role and approver tables", which belongs to the v2 SOP (A19). Open: whether the lint reads this file in v1, and what it does with it.

### Surfaces, commands and shapes

- **X05 v1 surfaces (PLAN §7.5).** A§:914 says "In v1 nothing is rendered, so there is no rendered-file pass"; SF:82 and LT:11 to 14 still name `sop/`, `deliverables/`, rendered Word and PDF and their document properties, and SF:90 names `pdftotext`. BP:158 asks for `.docx` reading. Reading in the plan: A§ wins, `.docx` reading stays, `safety.md` section 6 and the header of `leak-terms.txt` are touch-ups. Touches L123 to L127, L167.
- **X06 The three paraphrase categories, and what a string rule can reach (PLAN §7.6).** A§:916 names personal and emotional stakes, remarks by client staff about colleagues, and our own internal assessments of people; SF:84 has closing tactics in place of the third and adds method vocabulary, objection text and alternatives in play (v2, A19). SF:88 says "the lint enforces what a string rule can reach". Seven of A§:918's trap categories (the seller's commercial terms, an assessment of a named individual, small talk, third parties in passing, a hypothetical about a person leaving, the seller's account structure, a health or nationality remark) are judgments about meaning. No source gives the lint a mechanism for them. Reading in the plan: A§; the `method` class stays. Open: which of those cases the lint blocks, by what string rule, and which are marked as outside a string rule's reach and left to authoring rules. Touches L103, L234, L236 to L238, L246 to L248.
- **X08 The command forms (PLAN §7.8).** A§:357 lists `scan`, `--payload`, `--blueprint`, `--terms` and `--wall`, mixing subcommands and flags; BP:158 has `--payload` read the wall; A§:922 has `--wall` run on every payload and planned name; Q1 adds an index-writing action. Reading in the plan: subcommands `scan`, `payload`, `blueprint`, `terms` and `index`, the wall always on inside `payload` and `blueprint`, and `wall` alone for a planned name. Open: the flags; which commands need a record (`terms` over `shared/` needs none; the wall needs the home and a record); whether `scan` takes a folder. Touches L20, L22, L189.
- **X09 Unpinned record shapes the lint reads (PLAN §7.9).** The marked client-safe block (RM:21, RM:24), the glossary of the blueprint, a snapshot's conflict rows (A§:920 "its marks, conflicts and markers"), and the row forms of `allowlist.md` (RM:42) and `exclusions.md` (RM:43) have no pinned syntax; WP7's templates come in stage 3. A§:370 says exclusions hold names, terms and figures; RM:42 says each allowlist row needs the user's OK, with no field for it. Reading in the plan: WP4 pins them in `record-map.md` now and WP7 follows. Open: the mark, the row forms, how an unclosed mark reads, and whether the OK is a field the lint checks. Touches L92, L94 to L97, L102, L271.
- **X10 Per client or per strand (PLAN §7.10).** A§:370, A§:920 and SF:88 speak of a per-client allowlist and exclusions list; RM:42 and RM:43 place both under each strand's `solution/`. Reading in the plan (nod 7): exclusions of every strand of the record, the allowlist of the payload's own strand. Not stated: how the lint is told the strand (a `--strand` flag, as `ledger.py` has one), and what an allowlist is when the caller names none. Touches L43, L44, L119.
- **X11 "Client-derived figures" and "internal files" (PLAN §7.11).** A§:916 does not enumerate them. Reading in the plan: every file of the record except the text of client documents and emails in `inputs/`, `drafts/` and the exempt blocks, with figures harvested under a floor and every other number a warning. Not stated: whether `readiness.md`, `blueprint.md`, `research/` and `strands/*/` files are in the set, and whether `.work/` is. Touches L45, L78.
- **X22 How a payload is handed in, and how a kind is named (not in PLAN §7).** No source pins the payload file: its JSON shape, whether it names its kind (agent, Vibe app, AI column, workflow, sequence, webhook, a board's names), how `ledger.py intent` and the payload relate (BP:252 puts `leak_lint.py --payload` between `intent` and the call), whether a payload may be read from standard input, and whether the file must lie inside the record as W91 requires of every input the session hands. A§:914 lists the kinds in prose. Touches L32, L131, L133, L158, L161, L271.
- **X14 The AI payload kinds, their fields and their stage (PLAN §7.14; Q3 (a) answered).** BP:51 and BP:158 put the AI kinds in stage 4b; the user chose stage 2. The sources differ on the fields: BP:158 names an agent's name, role, goal and plan; A§:914 names name, role, plan and knowledge-grant names; AI:10 adds a role description and `user_prompt`. A§:914 adds a Vibe app name that BP omits. The AI column, the sequence (step text, recipient list) and the webhook were not probed (AI:72, AI:76), so no field shape for them exists in any source; a workflow's step text is a draft the expert states except dynamic text (AI:59). What stage 4b still adds is not listed. Touches L142 to L161.
- **X15 Credentials (PLAN §7.15).** BP:158 ("no credential ... reaches an account-level object") and AM:112 to 120 (A17, "a prompt never carries a credential") name a rule; A§:916's list of what the lint blocks names none. Reading in the plan: a credential class (token and key shapes, bearer and basic headers, `password=`-style pairs, URLs carrying user info or a token parameter) joins the id patterns. Open: the shapes, whether the rule lives in `leak-terms.txt` or in the script, and the false-positive cost on long ordinary strings and hashes (L75 already blocks 64-character hashes). Touches L76, L155, L156.
- **X40 What an "internal note" is.** BP:158 and AM:118 say no internal note reaches an account-level object; no source defines one. Candidates: any text copied as a run from an internal file (the run rule), any text carrying a method term, any note field of the record. Touches L77, L156.
- **X41 The finding shape, the `ok` field and the wall's finding.** W91's envelope has `ok` true unless the exit code is 1, so a could-not-run (exit 3) prints `"ok": true` unless the code sets it false. For a gate that fails closed, a caller reading `ok` alone would pass on exit 3. The finding fields for a lint (file, position, rule, class, severity) are not pinned; G10's four parts (file, field, problem, expected) are. Also open: whether a wall finding names the other client (helpful to the user, but it carries one client's name into another client's session). Touches L23, L29, L192.
- **X47 The callers and where fail-closed is proved.** BP:158.32 says "every caller treats 3 as fail-closed". The callers are in other packages: the write path of WP9 (BP:252), the hook of WP13, `call-intake` and the blueprint skill of WP7, the audit, the record close. WP4 can state the rule and prove its own exit; each caller proves its own side at stage 4. No list of callers exists. Touches L209, L277.

### Figures, runs and quotes

- **X24 What a word, a run and a quote are.** A§:916 and BP:158 say "six or more consecutive words" and "eight or more words". Not stated: how words are split (hyphens, apostrophes, numbers, markdown marks, punctuation), whether the match ignores case and punctuation, how a run broken by a changed or reordered word is read, and what a "client quote" is: a `[Q]` line of a call summary, a `[Q/doc]` extract, or any quoted text. A seven-word stretch of a `[Q]` line copied into a payload already fails the six-word rule if the call summary is an internal file, so the eight-word rule only adds anything where the run rule is exempt or off: a client document in `inputs/` (exempt from the run rule) or a client-safe block. Open: whether the quote rule applies to those places. Touches L88 to L90.
- **X25 Figures: formats, floor, and what counts.** The five formats are listed (A§:916). Not stated: letter case and spacing of `45K` and `45 k`; other spoken forms ("forty five thousand", "45 thousand", "45m", "half a million"); currency signs other than `$`; decimals and percentages; the floor's value (Q1 (a) leaves it to the decisions step, so that a common number shared by two clients does not block); whether the floor applies to a record's own figure set as well as to the wall (PLAN §7.11 says it does); what "other numbers" are warned (A§:920, SF:88) and whether a date or an id is one; and whether a figure in an exclusions row is matched in the five formats. Touches L78 to L87, L175, L184.
- **X36 The exempt blocks, and a run found in two places.** BP:158 says the lint "passes" the client-safe block, the glossary and a run matching a client document; A§:916 and A§:920 say they are exempt "from the copied-run rule" only. Not stated: whether a marker, an id or an excluded term inside a block still blocks (L163 reads A§), whether a run that is both in a client document and in an internal file is exempt, and whether the quote rule applies to a block that holds a client's quote. Touches L46, L91, L94 to L96, L163.
- **X37 `SUMMARY.md`.** BP:158 and LT:14 lint it "under the copied-run and quote-length rules because it feeds later client-facing text". Not stated: whether markers, ids and method terms (which it legitimately holds, being an internal file) are also scanned; which files it is compared with, since a summary is built from the very files a run would be copied from. Touches L165.
- **X38 The client-safe block, at the moment it is written.** A§:916 says the three paraphrase categories "are also kept out of the client-safe block at the moment `call-intake` writes it". Whether the lint checks the block then, by a mode that scans one block, or `call-intake` does it by its own rule, is not stated. Touches L103.
- **X39 "Flag, do not remove" and "caution".** BP:158 and BP:448 say a "flag, do not remove" group is reported and kept (s1, s5, s6, s10) and a blocked word that is the client's vocabulary survives with a caution (s2). The keys are prose outside the repository. Not stated: what in a text marks a group as one to flag (a class, a marked row, a record field), whether "reported" is a block or a warning, and how the caution differs in output from a warning. Touches L113, L120, L121, L262.

### Tests, inputs and the rest

- **X13 The twenty-five arrays (PLAN §7.13).** They are prose entries in answer keys outside the repository, and the grading is WP14's at stage 4 (Q2 (a)). The plan counts 400 entries in 25 arrays; BP:448 says "158 entries" across the ten reviewed fixtures. Both can be true; neither is checked here. The array's shape (one prose string per entry) was seen; its content is not carried. Touches L266, L267.
- **X16 Nothing records that the lint passed (PLAN §7.16).** BP:252 puts the lint between `ledger.py intent` and the call, and WP3 built no field for it. Reading in the plan: the lint's output carries the sha256 of every input, so a later hook or ledger field can match the bytes sent; `ledger.py` is not changed in WP4. Touches L31, L210, L277.
- **X18 `tools/agnostic_sweep.py` does not exist yet (PLAN §7.18).** It is WP16's, so it cannot sweep the fixture's invented names in this run; the fixture self-test and the trace check enforce the rule until it does. Touches L217.
- **X20 The headless half (PLAN §7.20).** Grading on the twenty-five keys, the seed home's index and the callers' fail-closed rows are owed to WP14 and WP16 at stage 4. They are listed and counted, not failed. Touches L179, L199, L209, L267 to L270.
- **X23 Redaction against "never edit".** A§:357 says the lint is "block and report, never edit" and A§:916 says "Blocks, never auto-fixes"; BP:158 says "Redaction behaviour is written but not defaulted [A11-3]". A11-3 itself is the open decision about transcript redaction and retention in the record (BP:19), not about this lint. PLAN §8.9 reads: `scan --spans` reports the spans a redaction would remove, nothing calls it, nothing is removed. Open: whether that satisfies "written", and whether the A11 answer ever turns it into an edit. Touches L211, L212.
- **X31 What `--terms` runs.** BP:114 says `leak_lint.py --terms` over `shared/` "proves nothing from any client input is in it". `shared/` legitimately holds the plugin names, method terms, ids and markers (LT:14 to 15), and `leak-terms.txt` is itself a list of them. Not stated: which rules `terms` runs (the digest check only, per PLAN Q1 (a); the firm name; the exclusions of the records), which files it takes (every text file, `.md`, `.txt`, `.json`), whether it needs a record or `settings.json`, and whether it excludes `leak-terms.txt`. Touches L195 to L199.
- **X34 Links.** LT:169 to 171 say the lint strips URLs before the id class runs, so an id inside a link is exempt; BP:158 says ids "outside links". Not stated: what a link is (a Markdown link target, a bare URL, an HTML `href`, a URL in a webhook field), whether the link text counts, what a URL-encoded or look-alike link is, and how a webhook URL (which is only a URL) is checked at all if URLs are stripped. Touches L73, L74, L155.
- **X35 `.docx` parts and the extensions a scan takes.** BP:158 names `word/document.xml` and the two `docProps` files; a `.docx` may also carry headers, footers, footnotes, comments and custom properties (not named by any source). Not stated: whether a missing `docProps` part is an error, which file extensions a folder scan reads and what it does with an image or a PDF in `drafts/`. Touches L123 to L132.
- **X42 Limits.** No source states a size cap or a time cap on an input, a limit on the nested depth of a payload, a guard against a zip archive that expands very far, or a guard against a regular expression in a user-edited local list that runs for a very long time. A lint that fails closed has to decide what it does with an input it cannot finish. Touches L128, L130, L205.
- **X43 Files, tests and interpreters.** BP:156 names one test file (`tests/unit/test_leak_lint.py`); PLAN §8.1 builds three (`test_leak_lint.py`, `test_leak_wall.py`, `test_leak_fixture.py`). BP:159 gives 540 and 460 lines, which PLAN §9 reads as estimates. The Mac's oldest Python 3 may be newer than 3.9 (WP3's practice was `/usr/bin/python3` for the oldest). Touches L14, L17, L19.

## 5. Coverage

### 5.1 Every part of BP:158, and the clauses that cover it

BP:158 is one sentence. It is split here into 33 parts, numbered as the `BP:158.n` tags in the clauses. Quotes are cut to fifteen words or fewer.

| Part | What BP:158 asks (quoted or shortened) | Clauses |
|---|---|---|
| 1 | "sets `sys.dont_write_bytecode = True` as its first statement after `import sys`" | L03, L04 |
| 2 | "blocks a planted figure in all five number formats" | L78 to L84, L87, L249 |
| 3 | "blocks a six-word copied run" | L88, L89, L251 |
| 4 | "an eight-word client quote" | L90, L252 |
| 5 | "all nine markers including `[Q/doc]` and `[A]`" (the assumption's marker kept out of the workspace) | L60 to L66, L253 |
| 6 | "internal ids" | L58, L59, L75, L254 |
| 7 | "record paths in both Windows and POSIX spelling" | L67 to L69, L255 |
| 8 | "eight-digit monday ids outside links" | L72 to L74, L257 |
| 9 | "passes the marked client-safe block of a call summary and of a document snapshot" | L94, L95, L258 |
| 10 | "the glossary" | L96, L163, L258 |
| 11 | "a six-word run that matches the text of a client document in `inputs/`" | L46, L91, L251 |
| 12 | "still blocking the same run copied from that snapshot's conflict rows" | L92, L93, L251 |
| 13 | "ignores runs made mostly of common words" | L98, L99, L259 |
| 14 | "reads `.docx` by unzipping `word/document.xml` plus the two `docProps` files" | L123 to L132, L225 |
| 15 | "`--payload` checks names, descriptions, labels, seed values, doc markdown, automation request text" | L133 to L141, L162, L265 |
| 16 | "an agent's name, role, goal and plan, a Vibe prompt, an AI column prompt ... a webhook's URL" | L142 to L161 |
| 17 | "no credential, internal note, record path or other client's term reaches an account-level object" | L76, L77, L155 to L157, L263 |
| 18 | "`--payload` also fails on any term the strand's `exclusions.md` lists" | L43, L87, L100 to L102, L174, L263 |
| 19 | "the cross-client wall: `--payload` reads the hashed vocabulary digest" and fails on a name, term or figure | L168 to L192, L279 |
| 20 | "proved on the two planted records with one hit and one clean pass" | L193, L194, L224 |
| 21 | "an allowlist row clears a vocabulary term and fails to clear a figure, a quote or a copied run" | L113 to L119, L264 |
| 22 | "a 'flag, do not remove' group is reported and kept (s1, s5, s6, s10)" | L120, L262, L268 |
| 23 | "a blocked word that is also the client's own vocabulary survives with a caution" | L121, L262, L268 |
| 24 | "a document carrying a figure only in split renderings fails" | L105, L106, L250 |
| 25 | "a proper-noun-free paragraph naming three of the client's tool categories in one sentence fails while two pass" | L107 to L111, L260, L275 |
| 26 | "the two structural assertions run on every scan and are proved on `tests/fixtures/leak/`" | L104, L112 |
| 27 | "the firm-name rule reads the firm's renderings from `local/settings.json`, catches every rendering the fixture plants" | L40 to L42, L49 to L52, L55, L261 |
| 28 | "its whitelist clears the legitimate uses" | L53, L261 |
| 29 | "a test asserts no false positive on an ordinary word" | L54, L261 |
| 30 | "carries the trap categories of A§9.6 as planted text and a clean twin" | L214 to L248 |
| 31 | "`SUMMARY.md` is linted under the copied-run and quote-length rules" | L165 |
| 32 | "exit 3 when it cannot run, and every caller treats 3 as fail-closed" | L27, L200 to L210 |
| 33 | "Redaction behaviour is written but not defaulted [A11-3]" | L211, L212 |

The other lines of the WP4 block and the inputs the brief names:

| Source line | What it asks | Clauses |
|---|---|---|
| BP:155 | Tier v1-core; gains the wall (A20), the AI-kind payloads (A17, A18) and record paths in either system's spelling with tests on Windows and macOS (A24) | L168 to L194, L142 to L161, L67 to L69, L17, L18, L255 |
| BP:156 | Files: the script, the tests, `tests/fixtures/leak/` with planted text, docx and payload samples and two planted client records under a temporary home | L14, L16, L214, L224, L225, L265 |
| BP:157 | Inputs: A§9.6, the shipped list, `local/settings.json` and `local/leak-terms.txt`, the strand's `exclusions.md`, the twenty-five arrays, the trap categories | L33 to L48, L266, L214 to L248 |
| BP:159 | Size 540 lines, tests 460 | L19 |
| BP:252 | The write path puts `leak_lint.py --payload` between `ledger.py intent` and the call | L31, L210, L277 |
| BP:114 | `leak_lint.py --terms` over `shared/` at release | L195 to L199 |
| BP:382 | `tests/fixtures/leak/` is repo-only, never shipped | L15 |
| BP:321 | Stage 4 copies fixtures in; the seed home holds a `clients-index.json` with one other client's digest | L179, L269 |
| BP:323, BP:410, BP:448 | The leak grader reads `expected_leak_blocklist`; the classes the arrays recur on; the two non-removals | L266 to L268 |
| BP:51 | The AI offerings are stage 4b | L142 to L161 (the user's Q3 (a) puts them in stage 2) |
| BP:19, BP:13 to 24 | A11-3 open; redaction not defaulted; no account read | L10, L211 to L213 |

### 5.2 Every item of the BP:368 row

| Item | Clauses |
|---|---|
| 1 "planted-leak fixtures with a clean twin" | L214 to L248, L216 |
| 2 "the two structural assertions" | L104 to L112, L250, L260 |
| 3 "the firm-name rule from local settings" | L40 to L42, L49 to L55, L261 |
| 4 "the cross-client wall" | L168 to L194, L279 |
| 5 "the AI payloads" | L142 to L161 |
| 6 "allowlist limits" | L113 to L119, L264 |
| 7 "fail-closed exit 3" | L27, L200 to L210 |

### 5.3 The items of PLAN §1's table (what earlier packages left for WP4)

| Item | What WP4 owes | Clauses |
|---|---|---|
| G49 | `sys.dont_write_bytecode = True` first after `import sys`; the plugin copy unchanged after every subcommand | L03, L04 |
| G58 | `home init`'s zero-byte `local/leak-terms.txt` and `settings.json`'s `firm {name, renderings[]}`; a clause on an empty or missing file | L38, L41, L42, L48 (and X33 for the missing local list) |
| G10 | exit codes 0, 1, 2, 3 and the JSON envelope | L21 to L30 |
| G11 | JSON read with `utf-8-sig`; written two-space, LF, final newline | L07, L08, L40, L47, L131 |
| G40 | the time format | L278 |
| G57 | a newer schema is exit 3 (`clients-index.json`, `settings.json`) | L40, L47, L203 |
| W91 | the record located like `record.py`; the CLI frame copied, not moved | L13, L22, L23, L32 |
| R8 | the precedent that a script may read other records under the home | L180, X21, X29 |

### 5.4 The clause families of PLAN §3 (step 1)

| Family | Clauses |
|---|---|
| Runtime and cross-system | L01 to L19 |
| The CLI frame and exit codes | L20 to L32 |
| The inputs the lint loads (shipped list, local list, settings, exclusions, allowlist, the record's internal files) | L33 to L48 |
| Firm and its phonetic variants; plugin and assistant names; markers; internal ids; record paths in both spellings; HTML comments; monday ids outside links; credentials | L49 to L77 |
| Figures in five formats | L78 to L87 |
| Copied runs, quotes, exemptions, the common-word filter | L88 to L99 |
| Exclusions; the three paraphrase categories | L100 to L103 |
| The two structural assertions | L104 to L112 |
| The allowlist limits, the two non-removals, warnings | L113 to L122 |
| `.docx` reading | L123 to L132 |
| The payload kinds, the AI kinds | L133 to L161 |
| Planned names, `drafts/`, `SUMMARY.md` under two rules, the build notes copy | L162 to L167 |
| The wall and its index | L168 to L194, L279 |
| `--terms` over `shared/` | L195 to L199 |
| Fail closed | L200 to L210 |
| Redaction written and not defaulted | L211 to L213 |
| The trap fixture | L214 to L248 (categories), L249 to L265 (rule cases) |
| Stage 4 headless (the twenty-five keys, the seed home) | L179, L199, L209, L266 to L270 |
| Pins, shared edits, the write path | L271 to L277 |

### 5.5 The user's answers and the amendments

| Answer or amendment | Clauses |
|---|---|
| Q1 (a), the wall | L168 to L194, L195 to L199, L279; gaps X01, X02, X21, X25 to X30 |
| Q2 (a), the twenty-five keys | L266 to L270; gap X13 |
| Q3 (a), the AI kinds in stage 2 | L142 to L161; gap X14 |
| Q4 (a), a trace check of the fixture | L221, L222 (the README is readable without code); the check itself needs no clause |
| A11 (all three open) | L10, L211 to L213 |
| A12 (no personal names) | L217 |
| A16 (a client document in `inputs/`) | L46, L78, L91, L92 |
| A17 (a prompt is leak-linted, no credential) | L145, L156 |
| A18 (every payload kind the connector exposes) | L142 to L161 |
| A20 (the lint is the wall) | L168 to L194 |
| A23 (a client copy of the build notes passes the lint) | L166 |
| A24 (Windows and Mac, both path spellings) | L06, L12, L17, L18, L67 to L69, L220, L255 |
| A25 (`[A]` never reaches the workspace) | L63 |
| A28 (sample data minus the exclusions) | L101, L139 |

### 5.6 A§9.6, sentence by sentence

| A§ line | What it says | Clauses |
|---|---|---|
| 914 | Runs on: planned names, every payload (AI kinds included), `drafts/`, live object names during the audit, `drafts/` again at close-out | L133 to L161, L162, L164; live object names during the audit are a payload read back and are not a separate input here (X22) |
| 916 | Blocks, never auto-fixes: firm and renderings; plugin and assistant names; figures in five formats; copied runs; quotes; markers, assumption labels, internal ids; other clients' names; paths, HTML comments, ids; the client's exclusions; three paraphrase categories | L49 to L103, L168 to L194 |
| 918 | The two assertions; the phonetic rule; the trap fixture and its twins | L104 to L112, L52 to L54, L214 to L248 |
| 920 | Exemptions; common words; warnings; the allowlist's limits; fail closed | L88 to L99, L85, L122, L113 to L119, L200 to L210 |
| 922 | The wall | L168 to L194, L279 |

### 5.7 PLAN §7, and the gap that carries each entry

Each anchor of PLAN §7 was re-checked against the source line it cites. All hold, with the corrections noted.

| PLAN §7 | Subject | Gap | Check of the anchors |
|---|---|---|---|
| 1 | the wall's contents | X01 | BP:158, A§:922, A§:440, RM:76, SF:90 hold; Q1 (a) is answered; the floor, the normalisation and the schema stay open |
| 2 | the index has no writer, schema or owner row | X02 | A§:922, RM:76 hold; G58 adds that `home init` does not create the file and that it is "written at a record close" |
| 3 | nine markers, eight listed | X03 | A§:627, RM:272, LT:146, LT:194 hold; X03 adds that the path rows are POSIX only |
| 4 | where the firm's renderings live | X04 | A§:916, BP:158, RM:76, LT:5, LT:35 hold |
| 5 | v1 surfaces | X05 | A§:914, SF:82, LT:11 to 14, SF:90 hold |
| 6 | the three paraphrase categories | X06 | A§:916, SF:84 hold; X06 adds seven trap categories no string rule reaches |
| 7 | one user's firm in a shipped file | X07 | SF:86 holds |
| 8 | the command forms | X08 | A§:357, BP:158, A§:922 hold |
| 9 | unpinned record shapes | X09 | RM:21, RM:24, RM:42, RM:43 hold |
| 10 | per client or per strand | X10 | A§:370, A§:920, SF:88, RM:42, RM:43 hold |
| 11 | "client-derived figures" and "internal files" | X11 | A§:916 holds |
| 12 | the client's tool categories | X12 | A§:918, SF:84 hold; the shipped list has no category class |
| 13 | the twenty-five arrays | X13 | BP:157, BP:321, BP:323 hold; BP:448 counts 158 entries in ten keys |
| 14 | AI payload kinds in stage 2 or 4b | X14 | BP:51, BP:158 hold; the user chose stage 2; the sources differ on the fields |
| 15 | credentials | X15 | BP:158, AM:118 hold; A§:916's list names none |
| 16 | nothing records that the lint passed | X16 | BP:252 holds |
| 17 | the pain-id patterns | X17 | LT:130 to 143, LT:27 hold |
| 18 | `agnostic_sweep.py` does not exist | X18 | `tools/` holds `lint_plugin.py` and its README only (as WP3 found) |
| 19 | no word list in the standard library | X19 | A§:920 holds |
| 20 | the headless half | X20 | BP:321, BP:323, BP:448 hold |

### 5.8 Totals

Clauses: L01 to L279, 279 in all. Gaps: X01 to X47, 47 in all.
