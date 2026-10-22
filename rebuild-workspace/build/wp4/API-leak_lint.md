# `leak_lint.py`, parts 1 and 2

Date: 2026-10-17. Internal build file: never client-facing.

`plugins/monday-master-builder/scripts/leak_lint.py` (2,801 lines), tested by `tests/unit/test_leak_lint.py` (1,263 lines, 110 tests). Part 1 builds the frame, the loading and checking of every list, the readers (`.md`, `.txt`, `.docx`, payload JSON), every rule that needs one record and one text, the generic payload walker, and the commands `scan` and `payload`. `blueprint`, `wall`, `terms` and `index` sit in the parser and answer exit 3, "not built yet". The cross-client wall inside `scan` and `payload` is not built either, so a check in a home that holds another client record, or an index, stops with exit 3 (DECISIONS Z02). Nothing can return 0 on a path that is not built. Gates at hand-over: the whole suite green under `/usr/bin/python3` (3.9.6) and Python 3.14.6, 456 tests each (346 before, plus 110); `tools/lint_plugin.py` 0 errors, the `leak` pair compared; no `__pycache__` (section 9).

The decisions this follows are `DECISIONS.md` X01 to X47, Y01 to Y09 and the new Z01 to Z11 ("Added by code part 1 (step 5)").

Part 2 (step 6) is at the end of this note ("Part 2: the wall, the index, blueprint and terms"). It builds the four commands that answered "not built yet", the wall inside `scan`, `payload` and `blueprint`, and X30's coverage check in place of Z02's interim stop. Sections 1 to 5 and 7 to 9 describe part 1 as it was handed over; where part 2 changes a line of them, the Part 2 section says so.

## 1. Commands, flags, exit codes and the envelope

Launch: `[interpreter, <plugin>/scripts/leak_lint.py, (--record <client folder>), <command>, flags...]`. `--record` is global and comes first; the current folder is the default. The record is any folder holding `CLIENT.md` (W91); without it, exit 3 naming `CLIENT.md`.

| Command | Flags | State in part 1 |
|---|---|---|
| `scan` | `[--strand <NNN>]`, `[--spans]`, `[<path> ...]` | built. No path: every existing `strands/*/drafts/` and `strands/*/deliverables/handoff/` (one strand's with `--strand`). A folder is walked recursively; `.md`, `.txt`, `.docx` and `.json` are read (a `.json` as a payload of kind `generic`); `.DS_Store`, `Thumbs.db` and `desktop.ini` are skipped; any other file is exit 3 (X35). Modes by path (X08): `strands/<id>/SUMMARY.md` is `summary`; a `.md` under `calls/`, or a `document-summary/1` snapshot under `inputs/`, is `client-safe-block`; anything else is `full`. |
| `payload` | `--strand <NNN>`, `--kind <kind>`, `--file <path>`, `[--spans]`; all but `--spans` required | built. `--kind` is one of the 24 pinned kinds, else a usage error (exit 3). The file is one JSON value, read with `utf-8-sig`, inside the record. |
| `blueprint` | `--strand <NNN>`, `[--spans]` | parser only; exit 3 "not built yet" |
| `wall` | `--text <text>` | parser only; exit 3 "not built yet" |
| `terms` | `<folder>` | parser only; exit 3 "not built yet" |
| `index` | none | parser only; exit 3 "not built yet" |

Every path handed in must resolve inside the record (W91, X22), symbolic links resolved; outside is exit 3 naming it. `--strand` takes a three-digit id with a `strands/<NNN>-*` folder; a `scan` path under another strand is exit 3. There is no `-h`: help is a usage error (Z09).

Exit codes: 0 clean, 1 at least one block, 2 warnings or cautions only, 3 could not run. Precedence 3, then 1, then 2, then 0 (X41). A usage error is exit 3, never argparse's 2. A refusal raised inside `mmb_common` is exit 3 here too, because exit 1 means a leak and nothing else (L25). Any other exception is exit 3 with the envelope (L205).

The envelope (X41), one JSON object through `mmb_common.json_text`, UTF-8, LF, no byte-order mark:

```text
{"ok": <true on 0 and 2, false on 1 and 3>, "command": "<name>" | null on a usage error,
 "verdict": "clean" | "warnings" | "blocked" | "could-not-run",
 "mode": "full" | "summary" | "client-safe-block" | null   (scan only; null when its files ran in several modes, Z07),
 "strand": "<NNN>" | null,
 "inputs": [{"file", "sha256"[, "parts_read"][, "mode"]} or {"file", "state": "absent"}, ...]   (sorted by file),
 "args_digest": "<sha256 hex>"   (payload only),
 "findings": [...], "counts": {"block": n, "warn": n, "caution": n},
 "error": {"file", "field", "problem", "expected"}   (exit 3 only)}
```

- `inputs` lists every file read: the shipped list as `<plugin>/shared/leak-terms.txt`, the two home files as `<home>/local/...`, every record file read for the sets, the exclusions and allowlist files looked for (absent ones with `"state": "absent"`), and the checked files. The hash is the sha256 of the bytes as stored, the same value `mmb_common.sha256_file` gives. It is printed on every exit, exit 1 included (L210).
- `args_digest` is the sha256 of `json.dumps(<parsed payload>, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` as UTF-8 (X16).
- A finding is `{"file", "field", "problem", "expected", "rule", "class", "severity", "line", "column", "match", "source"}`, plus `part` for a `.docx` part, `near: true` for a near copy, `cleared_by` for a caution and `span` with `--spans`. `field` is `line <n>` in a text file, `<part> paragraph <n>` (or `<part> <element>` in a property part) in a `.docx`, and the payload path (`$.steps[2].text`, `$.column_values<json>.text_1`, `$.Key<key>`, `$["odd key"]`) in a payload, where `line` and `column` are null. `match` is the checked text's own words, cut to 80 characters. `source` is the record file a set entry came from, or null.
- Order: findings of the checked files in the order given (a folder's files in sorted path order), then by position and rule; the record-file warnings (malformed marks, allowlist rows) after them, by file and line. Two runs on the same bytes print the same bytes (L30).
- `--spans` adds `span: {"start", "end"}` to each blocking finding: character offsets into the decoded text of that file as stored (after the byte-order mark, before CRLF is read as LF), into one payload string, or into one `.docx` part's extracted text. Nothing calls it and nothing is ever edited (X23).

For callers (X47, L277): run `payload` after `ledger.py intent` and before the call (BP:252); exit 0 and 2 go on, with every warning and caution shown to the user; exit 1 stops that write, draft or stage until the text changes; exit 3 stops it the same way and is never read as a pass. Keep `inputs` and `args_digest` with the record of the write. Step 6 writes the full caller paragraph.

## 2. The public functions part 2 builds on

- **Frame.** `main(argv)`, `build_parser()`, `COMMANDS` (command name to `cmd_x(run) -> exit code`; part 2 replaces `cmd_not_built` for its four), `emit`, `envelope(run, code)`, `outcome(run)`, `cannot(file, field, problem, expected)` (a `mc.CannotRun`), `read_bytes(path)` (every read goes through it; tests spy on it), `python_too_old(version)`.
- **Run.** `Run(command, args)`: `locate()` (W91), `name(path)` (record-relative, or `<home>/...`), `read(path, name, limit)` (bytes, hash recorded, caps), `text(path, name)` (decoded, LF), `absent(name)`, `add(finding)`; attributes `root`, `home`, `lists`, `exclusions`, `sets`, `inputs`, `findings`, `wall_checked`. `decode(data, name)` returns the LF text and the map back to stored offsets.
- **Normalisation (X24, X28).** `fold(text)` returns a `Variant` (the folded text and, per character, its original offset); `fold_variant`, `fold_text`, `percent_decode(variant)` (Z01), `slashed(variant)`, `words_of(text)` (folded, possessive dropped, apostrophes removed), `normal_form(text)` (spaced form), `tokenise(original, folded)` (tokens with original spans, case, sentence and paragraph), `sentence_spans`, `paragraph_spans`, `link_spans`. Legal suffixes (X28 step 6) are in `LEGAL_SUFFIXES`; part 1 uses them only for literal rows (Z11), the wall's hashes are part 2's.
- **Phonetic (X32, Y09).** `phonetic_key(word)`, `letters(word)`, `edit_distance(a, b, limit)`, `PhoneticSource(cls, term, origin, whitelist)` with `.keys` (spaced, joined per word, and the one-word key of the fused letters) and `.limit`. The wall's phonetic digests should use `phonetic_key` per word and join without collapse, as Y09 says.
- **Numbers (X25).** `parse_numbers(folded_variant, original, masks=None)` returns `Number`s (exact `Fraction` value, precision, percent, currency, rate, cue, split, spans in the folded text; a lower-case `m` or `mm` gives two readings); `number_masks`, `date_spans`, `digit_chains`, `chain_is_date` (Y02), `id_chains` (X34), `whole_number(term)`, `precision_of(value)`. The wall's `f:<n>e<k>` hashes can be built from `Number.value` and `Number.precision`.
- **Lists.** `parse_list(text, name, local)`, `Lists(rows, settings)` (`.literals` as `Pattern`s, `.regexes`, `.phonetic`, `.firm_whitelist`, `.seller_ids`, `.category_words`, `.plugin_words`, `.id_row`), `load_shipped`, `load_local`, `load_settings`, `load_lists(run)`. `Lists.plugin_words` is the plugin's own vocabulary X26 adds to the stop list.
- **Record sets (X11, Y01).** `record_files(run)`, `kind_of(rel)`, `file_segments(run, rel, text)` (each `Segment` tagged body or block and with the sets it feeds: `F`, `R`, `Q`, `E`, `C` for a conflict row), `build_sets(run)` returning `Sets` (`cost`, `cost_percent`, `record`, `record_percent`, `runs`, `docs`, `quotes`, and `near("runs")` / `near("docs")`). Part 2 adds D and O; `file_segments` already says which text is client-safe, conflict or blueprint client-facing, so O and D can be built from the same segments (X11's table, Y01: the allowlist feeds nothing).
- **Shapes (X09, Y05).** `block_lines`, `section_lines`, `blueprint_client_lines` (sections 1 to 15, prompt blocks, glossary), `is_snapshot`, `quote_texts`, `row_parts`, `section_rows`, `load_exclusions(run)` (`Exclusions.patterns`, `.figures`), `load_allowlist(run, short)`, `strand_folder(run, short)`.
- **Readers.** `docx_parts(data, name)` (X35 guards), `docx_text(run, path, name)`, `payload_units(file, data, strand, seq)` (the generic walker, Z10), `file_units(run, rel, path, strand, seq)`, `scan_targets`, `inside_record`.
- **Checking.** `Unit(...)` (one text, a `.docx` part or one payload string or number; `own` says which set entries to skip, Z04), `Check(run, unit).execute()` returning raw hits, `check_unit(run, unit)` (dedupe, containment, allowlist, spans, then `run.add`). **The wall hook is `wall_hits(run, check)`**: part 2 replaces it with the real wall, which gets the unit, its folded text and its tokens from `check`, and removes `wall_guard`. `Check.execute` calls it for every mode but `summary`; `cmd_payload` calls it once before the units.

## 3. The pinned regions

| Region | Holds | Compared by `tools/lint_plugin.py` |
|---|---|---|
| `# pinned: leak` | `MARKERS`, `KINDS`, `FAMILIES`, `KIND_FAMILIES`, `BLOCK_MARKS`, `HEADINGS`, `ROW_KEYS`, `EXCLUSION_KINDS`, `INDEX_FIELDS`, `INDEX_FORMS`, `SEVERITIES`, `VERDICTS`, `MODES`, `RULES`, `WALL_CLASSES`, `CLEARABLE`, `LOCAL_CLASS`: every token of `Pinned: leak` and no other string literal, no number and no backtick | yes, both ways (0 errors) |
| `# pinned: common-words` | `COMMON_WORDS` (1,098 words, about a hundred monday and work words among them), `RUN_MIN_DISTINCT = 2` | no |
| `# pinned: stop-words` | `PRODUCT_WORDS`, `STOP_WORDS` (titles, role and common acronyms) | no |
| `# pinned: paraphrase-cues` | `PARAPHRASE_CUES` (six groups), `ROLE_WORDS`, `PRONOUNS` | no |
| `# pinned: internal-vocabulary`, `# pinned: sales-framing` | the two vocabulary groups of X06 | no |
| `# pinned: cost-cues` | `COST_CUES`, `CURRENCY_CODES`, `RATE_SUFFIX` | no |
| `# pinned: confusables` | `CONFUSABLES` (Cyrillic and Greek look-alikes, dashes), `NARROW_SPACES` | no |
| `# pinned: credential-shapes` | `CREDENTIAL_SHAPES`, `LONG_SECRET` | no |
| `# pinned: internal-notes` | `INTERNAL_NOTE_PHRASES`, `CLEARABLE_NOTES` (R62), `FRONT_MATTER_LINE`, `SPEAKER_LABEL` | no |
| `# pinned: structural-id-keys` | `STRUCTURAL_ID_KEYS` (Y08) | no; `test_Y08_the_fixture_copy_...` keeps `test_leak_fixture.py`'s copy equal, reading that file |

A new token in `Pinned: leak` must be added to the `leak` region as a string literal, and nothing else may go there, or the lint fails. `test_L161_L271_L272_...` runs the tool's own `pinned_section` and `pinned_region` on the two files.

## 4. The rules and the decision each follows

| Rule (class) | What blocks or warns | Follows |
|---|---|---|
| `term` (every shipped and local class) | literal rows on folded text with LT:18's boundaries; rows of two or more words also across `,` `.` `-` `_` `/` `|` `·`, whitespace and a line break; `re:` rows line by line on the line as written, with backslashes as slashes, percent-decoded and folded, in windows of 10,000 for long lines | LT:17 to 29, X03, X32, X33, X42 |
| `term` (`firm`) | `firm.name`, `firm.renderings[]` and local `class: firm` rows, tokenised, with the gaps, the fused form and the legal-suffix form | X04, X32, Z11 |
| `phonetic` (`firm` or the row's class) | windows of n and n + 1 words and single tokens of four or more letters whose key equals the source's, or within edit distance 1 (5 to 7 letters) or 2 (8 or more); cleared by the class's whitelist rows; never beside a literal hit of its class | X32, Y09 |
| `seller-account` | the names of `never_show_workspaces[]`, `default_build_account.slug` and `github_account` (tokenised, gaps, fused); their ids digit-bounded anywhere, links and structural values included, and on every JSON number | X06, Y08, Z06 |
| `term` (`markers`, `pain-ids`, `method`, `plugin`, `assistant`, `id-patterns`) | the shipped rows; the nine markers are literal rows of the shipped `markers` class | X03, X17, L66 |
| `term` (`id-patterns`) | the eight-digit row with link targets masked, and the same row beside any mark (Z03); split ids, digit groups of two to four joined by a space, hyphen or dot totalling eight digits, not a date (Y02), outside links; HTML comments, with the four mark lines removed first | X34, Y02, Y03, Z03 |
| `term` (`internal-vocabulary`, `sales-framing`) | the embedded groups, as literal rows | X06 |
| `internal-note` | the five phrases; a flat front-matter line; a `---` line followed by `schema:` (reported at the hyphens); `Speaker <n>` | X40, Y07 |
| `credential` | the six shapes (a secret pair also with a quote after the key word); shapes on the line and its percent-decoded copy; shape 6 outside links only | X15, Y04 |
| `exclusion` (`name`, `term`, `figure`) | every strand's exclusion terms, tokenised with the gaps and the fused form; figure rows by value, any value, every rendering | X09, X10, X25, Y05 |
| `figure` | a number matching a cost figure of 1,000 or more; one of 10 to 999 beside a cost cue, a currency sign or a rate suffix; a percentage matching a cost percentage; within the larger precision; in links too, on the percent-decoded copy | X11, X25 |
| `split-figure` | a digit chain (Z05) or number words across a line break matching a cost or exclusion figure (block), a record number or a date written in spaced groups (warn) | X25, Y02, Z05 |
| `record-number`, `number` (warn) | a match with a record number, or a cost figure of 10 to 999 with no cue; any other number of 10 or more; never inside a link, never a plain run of eight digits or more | X25, X39, Z05 |
| `copied-run` | six words equal to an R source's, two of them outside the common words; conflict rows first (block), then client-document text (pass), then R (block); a near copy, eight words with one changed (`near: true`); one finding per maximal stretch, naming the first R file | X11, X19, X24, X36 |
| `quote` | eight words equal to eight of a client quote (the text in quotation marks on a `[Q]`-family line, or the line without its marker, locations and speaker); not filtered and not exempt; one finding when it and a run share a stretch | X24 |
| `paraphrase` (the six groups) | a sentence with a cue phrase and a person reference (a capitalised token not first in its sentence and not a common word, pronoun or stop word, or a role word); the cue itself never counts as the person | X06 |
| `allowlist` (warn) | a row with no `ok`, on every run; a row that meets a finding it may not clear, once per finding, the block kept | X09, X10, Y06 |
| caution | a `term` of class `method`, `internal-vocabulary` or `sales-framing`, a `paraphrase` cue, or an `internal-note` finding of "internal only", "internal use only" or "not for clients", cleared by an ok row of the strand's own allowlist (normal forms equal); `cleared_by` names the row | X10, X39, R62 |

Modes: `summary` runs the run and quote rules and the number rules (the split-figure assertion among them) only, against every R source but the record's `SUMMARY.md` files (X37). `client-safe-block` checks only the text inside the file's well-formed blocks, with every rule but the run rule; malformed marks are exit 3 naming the line; no block is one warning, exit 2 (X38). A checked file never feeds its own check (Z04).

## 5. Worth the user's nod

Choices taken where the decisions are silent; each is on the safe side or is the plain reading. The first eleven are DECISIONS Z01 to Z11.

1. Percent-decoding is the script's own, so no `urllib` import (Z01).
2. Until the wall is built, a check in a home with another record or an index stops with exit 3 (Z02).
3. An eight-digit id beside a slash or any other mark blocks once real links are masked, so a look-alike link's id blocks (Z03). A decimal with eight digits after its point now blocks too.
4. A checked file never feeds its own check (Z04).
5. Dot, hyphen, slash and underscore join a split figure only before a three-digit group; date chains' parts and plain eight-digit runs give no number warning (Z05).
6. The seller-account ids run on every JSON number (Z06).
7. A mixed-mode scan prints `mode: null` and per-input modes; a record-level path has no strand (Z07).
8. Three demonyms that are trade words (`french`, `polish`, `dutch`) are out of the health-identity group; `charge` and its forms are cost cues; `mm` is read both ways (Z08).
9. `-h` is a usage error (Z09).
10. The generic payload walker is built now; step 6 proves it per kind (Z10).
11. A legal suffix need not be written for a firm rendering, a seller name, an exclusion or a plugin row to block (Z11).
12. A person reference never comes from the first token of a sentence, as X06 says. So "Maren is burnt out." alone does not block; "We heard that Maren is burnt out." does. Titles and common acronyms (the stop list) are not person references either.
13. Markers keep blocking case-insensitively, so a Markdown checkbox `[x]` blocks as `[X]` (X03, nod 22 of DECISIONS section 7).
14. The `.docx` reader also reads `w:delText` (tracked deletions) and `w:instrText` (field codes), because they travel with the file; a line break inside a paragraph reads as a space, so one paragraph is one line. In a property part, a custom property's `name` attribute is read as well as its value.
15. The narrow and thin spaces are kept as a thousands separator before folding; a plain space between digit groups is a split rendering (X25).
16. The allowlist's warnings point at the row (its file and line) and name the finding they met in the problem text.
17. The record warnings X09 and X38 ask for (malformed marks, no client-safe block) use the rule `copied-run`, as X09's warning does, since no other pinned rule fits.
18. The shipped list is named `<plugin>/shared/leak-terms.txt` in `inputs` and in findings, beside the `<home>/` names X16 gives.
19. A symbolic-linked folder inside the record is not followed when the sets are read; a linked file is read.

## 6. What is left for step 6

Updated by part 2, 2026-10-17.

- Done in part 2: the wall (`wall_hits` replaced, `wall_guard` removed); the index (`index`, `clients-index/1`, the home mutex, the backup, X02, X29, X46); D and O (X26, X27), the slugs (X21), the coverage check (X30); the `wall` command; `blueprint` (X09, X36) and `terms` (X31); the payload walker proved over every kind of the trap fixture (X14, U3), with the wall inside `payload`; `test_leak_wall.py`; the caller paragraph of X47 (Part 2, section P5).
- Not part 2's: the grading of the whole fixture is the separate harness `tests/unit/test_leak_grading.py`, written by another agent at the same time; `test_leak_fixture.py` stays the fixture's self-test, unchanged. Part 2's own informal run of the fixture is in P7.
- Left after step 6: the checklist rows (step 9, PLAN section 3), and the stage-4 clauses of X20 (L179, L199, L209, L267 to L269), owed to WP8, WP12, WP14 and WP16.

## 7. Agreement with the fixture, checked informally

A throwaway probe in the session's scratch folder (not in the repository) ran all 248 `scan` and `payload` cases of `tests/fixtures/leak/manifest.json` (the two `blueprint` cases skipped) with record a alone in a fresh home and the wall hook set to report nothing. Grading as the manifest says, with the `wall` expectations set aside: every expected finding of every planted case is found at its place with its rule, class and severity, every planted exit code that does not rest on the wall agrees, and every twin passes with its expected exit code. No disagreement for step 6 to settle. The cases whose only expectation is the wall (T05 to T08, T14 to T16, T18 to T20, K17 and the wall lines of others) were not graded here; they are step 6's.

## 8. Follow-ups outside part 1's files

- No change is needed to `mmb_common.py`, `record.py`, `ledger.py`, any existing test, the trap fixture or `test_leak_fixture.py`. All are byte-equal.
- The lint-clean stand-in `tests/unit/fixtures/tools/lint-clean/plugins/monday-master-builder/scripts/leak_lint.py` was added by step 3 (`shared-edits.md`); it is untouched.
- For the user's word, not needed by the code: widen the shipped eight-digit id row as Z03 does (LT:191), so the list says what the script does; the touch-ups of DECISIONS section 5 stand as they are.

## 9. Gate results

All from the plugin repository, `monday-master-builder/`, on this Mac, with `PYTHONDONTWRITEBYTECODE=1`.

| Command | Result |
|---|---|
| `/usr/bin/python3 -m unittest discover -s tests/unit` | Python 3.9.6: 456 tests, OK (346 before, plus 110) |
| `~/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14 -m unittest discover -s tests/unit` | Python 3.14.6: 456 tests, OK |
| `/usr/bin/python3 tools/lint_plugin.py --root .`, and under 3.14.6 | 0 errors, 1 warning (the personal-name list is not on this machine), 6 not present yet; the `leak` pair compared and in agreement |
| `find . -name __pycache__` | none |
| `wc -l` | `scripts/leak_lint.py` 2,801; `tests/unit/test_leak_lint.py` 1,263 |

---

# Part 2: the wall, the index, blueprint and terms

Added by step 6, 2026-10-17. `plugins/monday-master-builder/scripts/leak_lint.py` is now 3,439 lines (2,801 in part 1), tested by `tests/unit/test_leak_lint.py` (110 tests, three of them updated, below) and the new `tests/unit/test_leak_wall.py` (814 lines, 50 tests). The decisions it follows are the earlier ones and DECISIONS Z12 to Z19 ("Added by code part 2 (step 6)"). No command answers "not built yet" any more, and every path still fails closed: exit 3, never 0, whenever something could not be read, parsed or checked.

## P1. The commands, as built

| Command | Flags | Needs | Reads | Writes | Prints beyond section 1's envelope |
|---|---|---|---|---|---|
| `scan` | as part 1 | record, `settings.json` | as part 1, and for the wall in modes `full` and `client-safe-block`: the index, the folder listing under `<home>/clients/` and `<home>/archive/`, and the shipped list and the `shared/` files when the index holds another entry or there are other folders (Z12, Z13) | nothing | nothing new |
| `payload` | as part 1 | record, `settings.json` | the same | nothing | nothing new |
| `blueprint` | `--strand <NNN>`, `[--spans]` | record, `settings.json` | the strand's `solution/blueprint.md`, the lists, the sets, the wall's inputs | nothing | `mode: "blueprint"` |
| `wall` | `--text <text>` | record; no settings | the record's O sources, the index, the folder listing, and the shipped list and `shared/` when the index holds another entry or there are other folders | nothing | nothing new; the text is reported as file `--text`, field `line <n>` |
| `terms` | `<folder>` | `settings.json`; no record (`--record` is ignored) | every file under the folder (X31, Z14), the lists, the index, the folder listing | nothing | `entries_compared`, `slugs_compared` |
| `index` | none | record; no settings | `CLIENT.md` and every file X11 reads, every strand's `exclusions.md`, the shipped list, the `shared/` files, the index | `<home>/clients-index.json`; `<home>/.work/record.mutex` (created on first use); `<home>/local/backup/clients-index.json.<UTC stamp>` before each rewrite | `written`: true or false |

Changes to section 1's lines: the `blueprint`, `wall`, `terms` and `index` rows are built; Z02's interim stop is gone, replaced by X30's coverage check (P2). The `inputs` list now also carries `<home>/clients-index.json` (or its `"state": "absent"`) and `<plugin>/shared/<file>` for the files Z12 reads.

## P2. The wall

- **When it runs.** In `payload` (built once before the units, so the index and coverage checks run even for a payload with no string), `blueprint`, `scan` in modes `full` and `client-safe-block` (X45; never in `summary`, X37), `wall` and `terms`. It runs on every string unit, every `.docx` part, and on JSON numbers for its figure part (Z17).
- **Building it** (`build_wall`, once per run). Read the index (P3); list the folders directly under `<home>/clients/` and `<home>/archive/`, this record's own and any of its name left out (Z18); the coverage check of X30: a folder holding a `CLIENT.md` (tested with `is_file`, nothing inside opened) whose name's key has no entry is exit 3, `error.file` `<home>/clients-index.json`, `error.field` `entries`, problem "<n> other client record(s) under the home ha(s|ve) no index entry, so the wall cannot see them", naming no folder. Then the union of every other entry's four lists, the slugs (X21: each folder name's tokens, its sub-runs kept by X26's filters, spaced and fused, with phonetic keys), and O, built fresh from this record's O sources (every file X11 reads but `strands/*/solution/allowlist.md`, Y01), in memory only, with the files that hold each candidate (Z15). With nothing to compare, O is not built.
- **Checking a unit.** wall/1 (`wall_cut`, `wall_candidates`) cuts the folded text, and the percent-decoded copy when there is one, into X27's candidates; the fused forms of type 3 also join a word broken by a hyphen at a line end and one broken by runs of `*`, `_`, `~` or backticks (R31). A candidate blocks with rule `wall` when its `n:` digest is in another entry's `names` (class `name`) or `terms` (class `term`), or its form is a slug form (class `slug`), and O holds it in no file but the one being checked. Phonetic keys are tested as Z13 says, against the entries' `phonetic` lists and the slugs' keys (class `name`, or `slug`). Numbers are tested as X25 and Z17 say (class `figure`). Overlapping hits of one class merge into one finding over the longest stretch.
- **The finding.** `rule: "wall"`, `class` one of `name`, `term`, `figure`, `slug`, `problem` "matches a <name, term, figure> of another client record under the home" (or "matches the folder name of another client record under the home"), `expected` "the text without it: another client's names, terms and figures never reach this client", `source: null`, and `match` the checked text's own words. It never names the other record, its slug or its key (X41, L192). An allowlist row never clears it and warns (X10, Y01).
- **What the hashes protect** (X28, nod 9). The digests are unsalted sha256 cut to 128 bits, with the prefixes `n:`, `p:`, `f:` and `s:`. They keep names, terms and figures out of the index file and out of anything copied from it; they do not keep them from a reader who can already open the client folders beside it in the same home. An unsalted digest also lets WP14 build a seed index that every run reproduces.

## P3. The index

- **Shape.** X02's `clients-index/1` exactly, through `mmb_common.json_text`: `schema`, `hash` (`sha256-128`), `normalisation` (`wall/1`), `entries` in ascending key order; each entry `updated` (UTC, `mmb_common.stamp("utc")`) then `names`, `phonetic`, `terms`, `figures`, each unique and sorted. The key is `digest("s:", <slug>)`. Nothing in the file is plaintext (L176).
- **What an entry holds** (`build_entry`). `names` and `phonetic`: X26's harvest over the D text of every record file (X11's D column: the blueprint's client-facing lines and the skipped files left out), with Z12's stop list and Z16's readings, plus the `CLIENT.md` name and slug whatever the filters say; phonetic keys as Z13 item 1 says. `terms`: every name and term row of every strand's `exclusions.md`, spaced and fused, with and without trailing legal suffixes. `figures`: every cost figure of F (X25) of 1,000 or more with three or more significant digits, at n of 100 or more for each k; every exclusion figure at n of 1 or more (Z17).
- **Writing.** Under `mmb_common.record_mutex(<home>)`: read the index fresh, replace this record's entry, keep its old `updated` when the four lists are unchanged, and write with `mmb_common.write_file(..., backup_dir=<home>/local/backup)` only when the bytes differ (X46: a rerun writes nothing and makes no backup). No temporary file, no rename, and no entry is ever removed, so an archived or deleted record stays walled (L178).
- **Reading.** Every reader takes the same mutex while it reads when `<home>/.work/record.mutex` exists, and never creates it (X29). An absent index reads as empty (L48). Exit 3, naming `<home>/clients-index.json`, for a schema other than `clients-index/1` (a higher number says "newer"), another `hash` or `normalisation`, invalid JSON (so a torn read is never a pass), or any malformed part (Z18). `index` refuses to overwrite such a file.
- **Refusals.** `index` is exit 3 when `CLIENT.md` has no slug or its slug is not the folder's name (X30), before anything is written.

## P4. `blueprint` and `terms`

- **`blueprint`** (Z19). The client-facing lines of X09 are checked under every rule, the wall included; the glossary is a separate unit exempt from the copied-run rule only (L163). The blueprint's own internal sections still count as an internal source for its client-facing text. Malformed glossary marks warn, exempt nothing, and the text after each mark is checked up to the next heading. Exit 3 for a missing blueprint, an unknown strand, or no numbered level-2 heading ("cannot find sections 1 to 15").
- **`terms`** (X31, Z14). Every file under the folder, sorted by path, skipping `.git/`, `__pycache__/` and the three system files; `.md`, `.txt`, `.json`, `.py`, `.yml`, `.yaml`, `.csv`, `.html`, `.xml`, `.toml`, `.ini`, `.cfg` read as UTF-8, `.docx` as X35 says, an empty file of any name read as empty, anything else exit 3. It runs the wall with no own record (every entry, every folder's slug, the coverage check) and the firm rule (the firm literals, the local `class: firm` rows and the firm's phonetic sources with their whitelist), and nothing else: no shipped row, marker, id, run, quote or assertion. Findings name folder-relative files.

## P5. For callers (X47, L277)

Run `payload` after `ledger.py intent` and before every call (BP:252); `blueprint --strand` after the blueprint is drafted, before the card, and at the build guard; `scan` on `drafts/` and `deliverables/handoff/` before anything is marked ready, on each new call summary or snapshot as call-intake writes it, and on `SUMMARY.md` before the user's yes; `payload --kind generic` on live names during the audit; `index` after every saved call, document or email, after every edit of `exclusions.md`, `research/` or strand Markdown (G13, R44; owed to WP8 and WP12), and before a record moves to `archive/`, for the files a caller writes itself: `record.py` runs it for its record after every command that changed a file the harvest reads, `init` included (R48, V1), so a write made through `record.py` needs no run of its own; `terms` over `shared/` at release. On every one of them: exit 0 and exit 2 go on, and every warning and caution is shown to the user; exit 1 stops that write, draft, stage or release until the text changes; exit 3 stops it the same way and is never read or retried as a pass, whatever `findings` holds. Keep the printed `inputs` hashes, and `args_digest` for a payload, with the record of the write, so a hook can prove the bytes it sees were the bytes checked. An exit 3 that names `<home>/clients-index.json` and `entries` means another record in the home has never been indexed: run `index` from that record (the user knows which; the lint will not say), then run the check again. An exit 3 that names the same file and field and says another record has changed since its last index means that record's entry is older than its files (R44): run `index` from each record changed since its last index, then run the check again. The callers prove their own side at stage 4 (L209, X20).

## P6. Code: what part 2 added and changed

- **Added.** `digest`, `word_key`, `wall_cut`, `wall_candidates`, `wall_keys`, `half_up`, `figure_forms`, `tested_form`, `significant`, `text_numbers`, `vocabulary`, `wall_stop`, `kept`, `harvest`, `name_digests`, `spaced_and_fused`, `d_text`, `build_entry`, `read_index`, `index_text`, `home_folders`, `Own`, `Wall`, `build_wall`, `record_texts`, `plugin_words`, `numbered_section`, `marked_lines`, `client_identity`, and `cmd_blueprint`, `cmd_wall`, `cmd_index`, `cmd_terms`. `wall_hits(run, check)` keeps its name and signature and now holds the real wall.
- **Changed in part 1's code.** `Run` gains `texts`, `wall`, `stop`, `record` and `extra` and loses `wall_checked`; `build_sets` reads the record through `record_texts`, so each file is read once per run for the sets, O and the harvest; `Lists.plugin_words` comes from `plugin_words(rows)`; `Unit` in modes `blueprint` and `glossary` excludes no own file (Z19); `Check.execute` has modes `wall` and `terms`, and runs the wall on number units; `Check.runs_and_quotes` treats mode `glossary` as exempt from runs; `envelope` prints `run.extra`. `wall_guard` and `cmd_not_built` are gone.
- **Unchanged.** Every pinned region, `shared/record-map.md` (no token added to `Pinned: leak`), `mmb_common.py`, `record.py`, `ledger.py`, the fixture, `test_leak_fixture.py` and every other test file but the three updated tests below.
- **Tests of part 1 updated** (only those asserting the interim answers): `test_X08_commands_part_2_builds_are_exit_3_not_built_yet` became `test_X08_the_part_2_commands_are_built_and_none_answers_not_built_yet`; `test_X01_part_1_has_no_wall_so_another_record_or_an_index_stops_the_check` (Z02) became `test_X30_another_record_without_an_index_entry_stops_the_check`; `test_L04_G49_...` expects the new exit codes of its eight command forms.

## P7. Agreement with the fixture, checked informally

A throwaway probe in the session's scratch folder (not in the repository) ran all 250 cases of `tests/fixtures/leak/manifest.json` (168 `scan`, 80 `payload`, 2 `blueprint`; the manifest holds no `wall`, `terms` or `index` case) as the README's steps say: both records copied into a fresh home, the overlay laid over record a, `index` run from record b and then record a, the case installed and run in record a. Graded as the manifest says (exit code, verdict, each `expect` entry matched by rule, severity, `where` and class; no block in a twin): every planted case and every twin passes, wall cases included (T01 to T03, T05 to T08, T14 to T16, T18 to T20, K17, K30, R18, the five payload kinds with a wall line, D09). No disagreement with the manifest.

Notes for the grading harness, not disagreements:

- For a `.docx` case the manifest's `where` is the part (`docProps/custom.xml`), while a finding's `field` is the part and its element or paragraph (`docProps/custom.xml vt:lpwstr`); the part is also in the finding's own `part` key, which is the one to compare.
- An `expect` entry with `where: null` (R18's allowlist warning) names no place; any finding of its rule and severity meets it.

Beyond the manifest: `terms` over the real `shared/` with both records indexed exits 0 (`entries_compared` 2, `slugs_compared` 2), and so does `terms` over the whole plugin folder. Run the other way, from record b over every draft case of the fixture, record a's names, terms and figures block as they should, and two ordinary words that open a sentence in record a and are not common words ("Rework", "Laminate") block too (Z16, item 5).

## P8. Worth the user's nod (part 2)

Each is DECISIONS Z12 to Z19; all are on the safe side or forced by a clause, as each entry says.

1. The harvest drops, as single words, every word the plugin's own `shared/` files use, and the days and months (Z12).
2. The wall's phonetic test skips runs made only of ordinary words and runs of fewer than seven letters, and publishes no single-word key an ordinary word shares (Z13). A misspelt name whose key an ordinary word shares is caught only by its literal forms.
3. `terms` reads an empty file of any name, so `shared/.gitkeep` passes (Z14).
4. A checked record file never makes its own words this record's for the wall (Z15).
5. A capitalised word at the start of a sentence is harvested as a name when it is not a common word, so it blocks in another record that does not hold it (Z16, item 5).
6. The wall compares figures by their f-forms on both sides, rounding half up, and tests JSON numbers and digit chains too (Z17).
7. A folder with this record's name under `clients/` or `archive/` is this record (Z18, item 4); L190 is proved with the other folder holding no `CLIENT.md`, since X30 stops the clause's literal setup (Z18, item 5).
8. The blueprint's own internal sections are a source for its client-facing text, and a broken glossary mark exempts nothing (Z19).

## P9. Gate results (part 2)

All from the plugin repository, `monday-master-builder/`, on this Mac, with `PYTHONDONTWRITEBYTECODE=1`.

| Command | Result |
|---|---|
| `/usr/bin/python3 -m unittest discover -s tests/unit` | Python 3.9.6: 509 tests, OK: 456 before, 50 in `test_leak_wall.py`, and 3 in the other agent's `test_leak_grading.py`, which passed in this run and are counted apart |
| `~/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14 -m unittest discover -s tests/unit` | Python 3.14.6: 509 tests, OK, the same split. One `ResourceWarning` (an unclosed file) is printed by `test_ledger.py`, as before; no part-2 test raises one |
| `/usr/bin/python3 tools/lint_plugin.py --root .`, and under 3.14.6 | 0 errors, 1 warning (the personal-name list is not on this machine), 6 not present yet; the `leak` pair compared and in agreement |
| `find . -name __pycache__` (the whole workspace) | none |
| `wc -l` | `scripts/leak_lint.py` 3,439; `tests/unit/test_leak_wall.py` 814; `tests/unit/test_leak_lint.py` 1,270 |
| the fixture probe (P7) | 250 of 250 cases as the manifest says |

Files changed by part 2: `scripts/leak_lint.py`, `tests/unit/test_leak_lint.py` (three tests), `tests/unit/test_leak_wall.py` (new), and in the workspace this note and `DECISIONS.md` (Z12 to Z19 appended). Nothing is committed.

---

# Part 1 review fixes (step 8)

Added by step 8, 2026-10-17. The fixes to the 27 blocking and should-fix findings of `leak-review.md` part 1, and to six of its notes, follow `DECISIONS.md` R01 to R28 ("Added by the review fixes, part 1 (step 8)"). `scripts/leak_lint.py` is now 3,963 lines; `tests/unit/test_leak_lint.py` is 1,675 lines with 143 tests (110 before, plus `ReviewBlockingTest`, 11, and `ReviewShouldFixTest`, 22). No command, flag or envelope field is added or removed. Where a line of sections 1 to 5 or of Part 2 no longer holds, this section says so.

## S1. Changes to section 1 (commands and exit codes)

- **`scan` with nothing to check is exit 3** (R22): with no path given, every existing `drafts/` and `deliverables/handoff/` is walked as before, and when no file is found (no such folder, an empty one, or the drafts in a misnamed folder), or a given path holds no file, the error is field `path`, "no draft or handoff file to check". Z07's "a scan that checks no file prints `full`" no longer occurs.
- **A folder linked into a scanned folder** is walked when it resolves inside the record, each real folder once, and is exit 3 naming the link when it resolves outside (R09).
- **New exit 3 cases** (all with the envelope, `ok` false): an `inputs/*.md` whose front matter names `document-summary/<n>` above 1, or another schema (field `schema`, R03); an `exclusions.md` line the reader cannot apply as a row (R04); a `.docx` holding an `altChunk`, a member under `embeddings/` or a nested document or HTML, RTF or Office member (R08), with problem "this document has another file inside it" and expected "take that file out and add it as its own input, then run this again" (the user's wording, 2026-10-19); pictures under `word/media/` and `word/printerSettings/printerSettings<n>.bin` never trip it; a UTF-16 `.docx` part with a DTD (R08); a malformed client-safe mark of the near-miss kind in mode `client-safe-block` (R19); a local `re:` row whose repeat holds a variable repeat or an alternation (R20); a `settings.json` key written twice, or a seller value with no letter or digit (R28).

## S2. Changes to section 4 (the rules)

| Rule (class) | What changed | Follows |
|---|---|---|
| every rule | each unit with a tag or an entity is also checked as an HTML-decoded copy (block tags as line breaks); a hit the plain copy made is not repeated | R05 |
| every rule that folds | Hangul fillers, variation selectors and the other default-ignorable characters dropped; more look-alikes (dotless i, small capitals, Cherokee, Armenian); U+2028, U+2029 and U+0085 as line breaks; repeated percent-decoding | R12 |
| `term`, `exclusion`, `seller-account`, `internal-note` (literals) | a boundary only on a side with a word character; a hyphenated row also matches its words with X32's gaps; a tokenised row of two words or more also matches as consecutive tokens whatever marks sit between | R07, R13, R11 |
| `term` (`id-patterns`) | new shipped rows for `research/`, `solution/`, `versions/`, `drafts/`, `deliverables/`, `live/`, five record file names, `%USERPROFILE%` and `$HOME`; the id row runs on every JSON number that is not structural; it skips a raw JSON string that is walked, digits after a decimal point, and warns (`split-figure`) on an eight-digit `YYYYMMDD` date; only a link with a scheme hides an id, and a bare URL ends at a comma or a pipe | R15, R02, R25, R26, R27 |
| `figure`, `exclusion` (figure rows), `split-figure`, `number` | a number may follow a sign, a dash, a slash, a quote or an abbreviation's full stop; a currency code may sit on the digits and is a cost cue; a hyphen may stand before a magnitude word; a thousands comma or apostrophe followed by a space or a break joins a split figure | R01, R21 |
| `phonetic` | a source with `th` or `ph` has a second key with them read as `t` and `p` | R16 |
| `credential` | the widened shapes and the secret-like looser pairs of R10, on the folded line too | R10 |
| `internal-note` | "not client-facing", "internal use only", "not for clients"; `SPEAKER_00` and `Speaker A:`; a front matter block with `schema:` anywhere | R17 |
| `copied-run`, `quote` | the near copy also takes a word dropped or added; a near quote (`near: true`) at the six inner positions, filtered by the common words; a quote line gives its whole utterance as well as its quoted words | R14, R06 |
| `paraphrase` | a role word needs a possessive or a name beside it; `owner` and `lead` are not role words; six process cues need a name; `english`, `american`, `visa` are not cues | R23 |
| `tool-categories` | plurals count; `e.g.`, `i.e.`, `etc.`, `vs.`, `approx.` end no sentence; seven everyday rows count only beside a more specific category; a day or a month is never a proper noun | R24 |
| `allowlist` (warn) | an `ok` whose first word says no, not yet or ask clears nothing and warns | R18 |
| readers | an `inputs/*.md` is a snapshot by its schema, quoted or not; front matter with no schema is internal; the exclusions reader is strict; the `.docx` reader reads Word's shown attributes, `people.xml` and external relationship targets, part names in any case | R03, R04, R08 |

Section 5 (worth the user's nod) gains the list at the end of the R entries. Section 2 gains `html_copy`, `html_hits`, `input_kind`, `front_matter_lines`, `token_forms`, `token_matches`, `deletion_index`, `risky_pattern`, `secretish`, `id_kind`, `ok_granted`, `near_mark`, `real_links`, `percent_decode_all`, `strict_rows` and `Check.near_windows`, `Check.credentials`, `Check.id_hit`, `Check.number_id`; `Sets.near` is replaced by `Sets.index(which, kind)`. `is_snapshot` now takes `(rel, text)`. `Unit` gains `raw_json`.

## S3. Pinned regions

`credential-shapes` gains `QUOTES`, `SECRET_KEYS`, `LOOSE_KEYS`, `LOOSE_SECRET` and `SECRET_AT_END`; `confusables` gains its additions, `IGNORABLE` and `LINE_BREAKS`; `internal-notes` and `paraphrase-cues` change as R17 and R23 say (`NAME_ONLY_CUES`, `POSSESSIVES` added). The `leak` region and `Pinned: leak` are unchanged, and `tools/lint_plugin.py` still compares them in agreement.

## S4. Gate results (step 8)

See `leak-review.md`, "Fixes for part 1", for the gate and the live probes.

---

# Part 2 review fixes (step 8)

The fixes to the findings of `leak-review-part2.md` follow `DECISIONS.md` R29 onward ("Added by the review fixes, part 2 (step 8)"). This section names only what changes a function's behaviour, a pinned region or a command's output.

## T1. The harvest (R32, G04)

- **New pinned region** `# pinned: shared-phrases`, after `shared-words`: `SHARED_PHRASES`, the 67 capitalised runs of two to four words that `shared/*.md` and `shared/*.txt` write, each word made of letters and a stop word. The script now has 13 pinned regions; `test_L274_L275_...` counts them. `shared_phrases(base=None)` gives what the region should hold for the folder as it is now, for the unit test and a reviewed regeneration only, as `shared_vocabulary()` does for `shared-words`.
- **`kept(words, stop, small, initials=False, phrases=SHARED_PHRASES)`** drops a candidate of two or more words only when it is one of `phrases` or every word is in `small`, X26 step 6's own list (days and months, product words, titles and acronyms, the shipped plugin, assistant, method and markers rows); `stop` filters single words only. **`harvest(text, stop, small, alt=False, phrases=SHARED_PHRASES)`** passes both on. **`wall_stop(run)`** returns `(stop, vocabulary_keys, small)`.
- **What an entry holds** (P3, `build_entry`): a name of two `shared/` words, such as `Signal Path`, is now in `names`, and so are its fused and phonetic forms. The slugs of other folders (P2) are cut by the same rule. The two planted records' entries are unchanged, and `terms` over the real `shared/` still exits 0.

## T2. A long exclusion term's windows (R33, G05)

- **New function `term_windows(term, small, phrases=SHARED_PHRASES)`**: for an exclusion term or name of five words or more, the spaced and fused forms of every window of two to four consecutive words, in both readings of R30's letters; a window whose every word is a common word or in `small`, or that is one of `phrases`, is left out. A term of four words or fewer gives nothing.
- **What an entry holds** (P3, `build_entry`): `terms` holds those windows beside the whole term's forms of `spaced_and_fused`. `wall_candidates`, `wall/1` and `clients-index/1` are unchanged. The two planted records' entries are unchanged, since their terms are of two words each.

## T3. The payload walker reads a JSON string literal (R34, G06)

- **`payload_units(file, data, strand, seq)`**: before it looks for JSON in a string, it drops the format characters (Cf and the F12 ignorables) and strips the rest; it then parses a form that starts with `{`, `[` or `"`. An object or list is walked as before (R25 unchanged). A string result is a unit of its own at `<path><json>` (for example `$.value<json>`, or `$.column_values<json><json>.text_1` for an object string quoted again), checked by every rule and parsed again in turn, within the depth limit of 64. A string that starts with `"` and does not parse is checked as raw text only. The same holds for a `.json` file that `scan` reads, which goes through the same walker.

## T4. One slug, two clients (R35, G07)

- **New function `twin_folder(run)`**: first the record's place (R46, T12); then exit 3 when `<home>/clients/<name>` or `<home>/archive/<name>`, under the root that does not hold the record, is a folder that is not this record (a path that cannot be looked at counts as one). `error.file` is `<home>/archive/` or `<home>/clients/`, `error.field` `(whole file)`; the error names the root, never a folder or a name. `build_wall` calls it first for a record (so `payload`, `blueprint`, `scan` with the wall, and `wall`), and `index` calls it after `client_identity`. `terms`, which has no record, does not.
- **New function `name_key(name)`**: the `n:` digest of the `CLIENT.md` name's full spaced form, or None for no name.
- **`index`** (P3, refusals): exit 3, `<home>/clients-index.json`, field `entries`, when the entry under this record's key does not hold `name_key` of this record's name; nothing is written. A same-name re-index replaces as before.
- **`build_wall`** (P2): the entry under this record's key is skipped as its own only when it holds `name_key` of this record's name; otherwise it joins the wall as another client's. `home_folders` is unchanged.

## T5. A home path that cannot be looked at (R36, G08)

- **New function `path_kind(path)`**: `"dir"`, `"file"`, `"other"` or None (no such path) by `os.stat`, a link followed; any other failure raises `OSError`. The wall's home checks use it in place of pathlib's `is_dir`, `is_file` and `exists`, whose answer differs between 3.9 (raises) and 3.14 (False).
- **`home_folders`** (P2): a folder directly under `<home>/clients/` or `<home>/archive/`, or its `CLIENT.md`, that cannot be looked at is exit 3, `error.file` `<home>/clients/` or `<home>/archive/`, `error.field` `entries`, problem "a folder under the home cannot be read, so the wall cannot tell whether it is a client record"; the error names no folder. X30's coverage test still counts a `CLIENT.md` that is a regular file.
- **`twin_folder`** (T4): a path it cannot look at counts as a twin under 3.14 as under 3.9.
- **`read_index`** (P3): exit 3, `<home>/clients-index.json`, `(whole file)`, problem "the home cannot be read, so the index or its mutex cannot be looked at", when either cannot be looked at; an index that is not there still reads as empty.

## T6. A blueprint's frozen copies are not its own source (R37, G09)

- **New method `Own.left_out(file)`**: the files O leaves out while `file` is checked. For a blueprint file (`kind_of` gives `blueprint`) it is every blueprint file of the same strand, `solution/blueprint.md` and each `versions/*/blueprint-r*.md`; for any other file it is the file alone, as before. `Own.has(kind, value, file)` keeps its signature and subtracts each left-out file that holds the value.
- **Checking a unit** (P2): a candidate is this record's when O holds it in a file other than those left out, so after `record.py freeze` the `blueprint` check at the build guard still blocks another client's name that only the blueprint and its copies hold. Another strand's blueprint files still count as O, and payloads are unchanged (X11).

## T7. A linked folder in `terms` and in the record's sets (R38, G10)

- **New functions `walk_inside(top, base, failed, outside, skip=None)`, `walk_files(...)` and `real_parts(real, base)`**: one walk for `scan`, `terms` and `record_files`. A folder or file reached through a link is followed when it resolves inside `base`, each real folder and file once, and named by its real place relative to `base`, so a link never changes a file's name or kind. One that resolves outside calls `outside(path, folder)`, which raises exit 3 naming the link, never its target. `skip(parts)` leaves out a folder by its real place. `scan_targets` keeps R09's behaviour and message through it.
- **`terms`** (P4): `base` is the folder checked. A linked folder or file that resolves outside it is exit 3, `error.file` the link's path relative to the folder, problem "a linked folder resolves outside the folder checked" (or "a linked file"); inside, it is walked and its files are named where they really are. `.git/` and `__pycache__/` are skipped by the real folder's name. A link loop is read once or is exit 3 as a file that cannot be read.
- **`record_files`** (the sets, O and the index's harvest): a linked folder inside the record is harvested under its real name, and a folder `skipped_dir` leaves out (`.work/`, a strand's `drafts/` and `deliverables/`) stays out when a link points into it. A linked folder or file that resolves outside the record is exit 3 for every command that reads the sets, `error.file` the link's record-relative path, problem "a linked folder resolves outside the record" (or "a linked file"). Section 5's item 19 no longer holds: a linked folder is followed, and a linked file outside the record is a stop.

# Fixes to built packages, 2026-10-21

## U1. The slug key is shared with `record.py init` (R39)

- **`digest`** is now `mmb_common.digest`, the same function under the same name, so L196's one digest function lives in `mmb_common.py`. Its output is unchanged.
- The three uses of the slug key (`build_wall`'s coverage check and own key, `cmd_index`) call `mc.slug_key(slug)`, which is `digest("s:", slug)`. `clients-index/1` and every command's output are unchanged.

## U2. A renamed client keeps its entry (R40)

- **New function `holds_own_name(entry, names)`**: true when the entry's `names` holds `name_key` of any of `names`. `index` and `build_wall` call it with this record's `CLIENT.md` name followed by its former names (`mmb_common.former_names` of the `former_names` field, `; `-joined, absent or empty meaning none), in place of T4's test on the name alone.
- **`client_identity(run)`** returns `(name, slug, former names)`; **`build_entry(run, client, slug, former=())`** publishes each former name in X26 step 1's forms (spaced, fused, trailing legal suffixes dropped, both readings of G02's letters), as it does the name.
- **`index`** (T4): the entry under this record's key is replaced when it holds the name or any former name; otherwise exit 3 as before, `<home>/clients-index.json`, field `entries`, with the problem now "the entry under this record's slug belongs to another client (it holds neither this record's CLIENT.md name nor any of its former names), and an entry is never replaced by another client's" and the expected "one slug per client: give this record another slug, or, if this client was renamed, keep its old name with record.py client rename or in CLIENT.md's former_names, then run index again". It still names no folder or name.
- **`build_wall`** (T4): the entry under this record's key is its own when it holds the name or any former name.
- **`SHARED_WORDS`** gains `rename`, which `record-map.md`'s `client/2` section now writes; `terms` over the changed `shared/` passed against the region before it was regenerated. `SHARED_PHRASES` is unchanged.
- A record with no `former_names` reads, indexes and walls exactly as under T4. `clients-index/1` is unchanged.

# Part 2 review fixes, continued (step 8), 2026-10-21

## T8. A one-word name written split (R42, G11)

- **`Wall.hits`** (P2, checking a unit): a spaced run of two or three tokens with only white space between them, that passes Z13 item 2's gate (a word outside the ordinary words, seven letters or more in all) and has no hit of its own, is also looked up joined through `Wall.name_class` (class `name`, `term` or `slug`), unless O holds the spaced run in a file other than those left out. `wall_candidates`, `wall_keys`, `build_entry`, `Own` and `clients-index/1` are unchanged, and no phonetic key is added.

## T9. Plural and apostrophe shapes (R43, G12)

- **`fold(text, offsets=None, alt=False)`** (P1's normalisation, every rule): `APOSTROPHES` (U+2018, U+02BC, U+00B4, the backtick, U+FF07) between two letters or digits become `'`, so `words_of`, `tokenise` and wall/1 read `O‘Rourke` and ``O`Rourke`` as `orourke`. A backtick with a space or a mark beside it is unchanged. `vocabulary` sends an ASCII line holding a backtick through `fold`.
- **`Wall.hits`** (P2, checking a unit): a candidate with no hit of its own goes to **`Wall.shape_class(form, words, fused, split, initial, file)`**, which looks up each word with a plural ending removed (**`plural_stems(word)`**: `s`, and `es` after `s`, `x`, `z`, `ch` or `sh`; nothing for `ss` or a stem under three characters), and a one-letter token fused to the capitalised word after it across `INITIAL_GAP` (spaces, or one apostrophe shape with spaces around it). A split run's shape that passes Z13 item 2's gate (`Wall.gated`) is also looked up joined. Nothing is looked up when O holds the candidate. `wall_candidates`, `build_entry`, `Own` and `clients-index/1` are unchanged; no phonetic key is added.

## T10. An entry older than its record (R44, G13)

- **New function `record_walk(root, failed, outside)`**: `{record-relative name: path}` of every `.md`, `.txt` and `.docx` under a record folder that may feed a set, through `walk_files` with `record_files`' skip (`.work/`, a strand's `drafts/` and `deliverables/`, `.git/`). **`record_failures(run)`** gives this record's `(failed, outside)`; **`record_files(run)`** is `sorted(record_walk(run.root, *record_failures(run)))`, unchanged in what it returns.
- **New functions `feeds_entry(rel)`, `newest_change(found, failed)`, `entry_is_older(entry, newest)` and `other_record_newest(path)`**: the files whose text reaches an entry are those `record_walk` finds but the allowlist and the live map (`kind_of` gives `skip`), with every strand's `exclusions.md` kept. Their newest change is the latest `st_mtime` or `st_ctime` by `os.stat`; no file is opened, and a file gone since the walk is passed over. An entry is older when that change is at or after the end of its stamped second plus `ENTRY_SLACK` (2) seconds.
- **`build_wall`** (P2): after X30's coverage check, each folder `home_folders` lists whose key has an entry is walked with `record_walk` and compared. Exit 3, `error.file` `<home>/clients-index.json`, `error.field` `entries`, problem "<n> other client record(s) under the home ha(s|ve) changed since (its|their) last index, so the wall may not see what was added to (it|them)", expected "run leak_lint.py index from each client record changed since its last index, then run this again", naming no folder. A folder in such a record that cannot be listed, or a link that leads out of it, is exit 3 on the same file and field, problem "a client record under the home cannot be looked through, so the wall cannot tell whether its index entry is current". This record's own entry is never compared. `home_folders` now gives `(name, holds CLIENT.md, path)`.
- **`index`** (P3): the clock and the newest change of this record's files are taken before any file is read. The entry is replaced when the lists differ or when the entry is older than the record's files; `updated` is then the later of the clock and the newest change, so a rerun with nothing changed still writes nothing (X46), while an edit that changes no list now writes a new stamp.
- **`read_index`** (P3): an `updated` that matches the pattern but is not a real moment (month 13) is exit 3 on `entries.<key>.updated`, "not a UTC time".
- **P5**: `index` also runs after every edit of `exclusions.md`, `research/` or strand Markdown.

## T11. An emptied or half-restored entry (R45, G14)

- **New function `entry_is_damaged(entry, folder=None)`**: true when the entry's `names` list is empty, or, with a folder name given, when it lacks `name_key(folder)`, the spaced `n:` digest of that name, which X26 step 1 always publishes for the slug.
- **`build_wall`** (P2): after X30's coverage check and before R44's age check, every entry is tested, each with its folder's name when a folder under the home has its key. Exit 3, `error.file` `<home>/clients-index.json`, `error.field` `entries`, problem "<n> entr(y|ies) of the index (is|are) damaged: leak_lint.py index always writes a client's folder name among its names, and (it holds|they hold) no names, or not that one, so the index was emptied or only partly restored", expected "run leak_lint.py index from each client record under the home; if the index was restored from a backup, restore the whole file from that backup, not part of it; then run this again", naming no folder, slug or key. This record's own entry is tested for an empty `names` list only. `read_index` and `clients-index/1` are unchanged.
- **`index`** (P3, refusals): an entry under this record's key that holds neither this record's names (R35, R40) nor the slug's spaced digest is damaged, not another client's. It is replaced when this record's new lists hold every digest it still holds; otherwise exit 3, `<home>/clients-index.json`, field `entries`, problem "the entry under this record's slug is damaged (it lacks the slug's name, which index always writes) and holds digests this record would not write, so replacing it could drop another client's wall", expected "restore the whole clients-index.json from its backup under <home>/local/backup/, then run index again"; nothing is written. R35's refusal is unchanged for an entry that holds the slug's digest.

## T12. A record not under the home in use (R46, G15)

- **`twin_folder(run)`** checks first that the record's resolved parent is `<home>/clients` or `<home>/archive`, the home resolved with `os.path.realpath` and both compared through `os.path.normcase`, so a home reached through a link matches. Otherwise exit 3, `error.file` `CLIENT.md`, `error.field` `record`, problem "this record is not under <home>/clients/ or <home>/archive/ of the home in use, so the wall cannot see the client records beside it", expected "a record at <home>/clients/<slug>/ or <home>/archive/<slug>/: point MMB_HOME at the home that holds this record, or move the record into that home's clients/, then run this again", naming no path. The twin test then looks only at the other root.
- **Where it runs**: wherever `twin_folder` runs, so `payload`, `blueprint`, `scan` with the wall and `wall` (through `build_wall`) and `index` (after `client_identity`; nothing is written). `terms`, a summary-mode `scan` (no wall, X37) and `locate`'s own refusal of a folder with no `CLIENT.md` are unchanged. A record folder that is a link in `clients/` to a folder outside the home is now exit 3.

## T13. Ordinary single words (R47, G16)

- **New function `lower_words(text, alt=False)`**: the words a D text writes in lower case as prose, each a token with no capital letter that is joined to neither neighbour by a `FUSE_GAP`, by no gap or across a backtick.
- **New function `inflection_stems(word)`**: R43's `plural_stems`, `ies` as `y`, and `ed` or `ing` removed with a final `e` restored or a doubled letter undone; stems of three characters or more.
- **`kept`** (T1): a single word is also dropped when one of its `inflection_stems` is in `stop`. The other folders' slugs (P2) are cut by the same rule.
- **`build_entry(run, client, slug, former=())`** (P3) now returns `(lists, single)`: a harvested candidate of one word that `lower_words` finds in any D text of the record is not published; runs and X26 step 1's forms are unchanged. `single` is the sorted single words the entry publishes. `clients-index/1` is unchanged.
- **`index`** (P1): the output gains `single_words`, `{"count": <n>, "words": [<sorted single words>]}`, this record's own words, printed whether or not the entry is written.

# Fixes to built packages, part 2, 2026-10-21

## V1. `record.py` keeps its record's entry current (R48)

- **New function `run_command(argv=None)`**: `(exit code, envelope)` of one command, printing nothing; `main(argv)` is `run_command` followed by `emit`, and prints the same bytes as before. `record.py` loads this file by path and calls `run_command(["--record", <record>, "index"])` in process; it also calls `record_walk` and `feeds_entry` (T10) to tell whether a command changed a file the entry is built from.
- **P5**: `record.py` runs `index` for its record after every command that changed such a file, after its own mutex is released; when the index stops, its error comes back to the session as a warning in `record.py`'s envelope (exit 2), the write kept. Callers still run `index` after files they write themselves, without `record.py`. No command's output, `clients-index/1` or any rule of the lint is changed.

# Part 2 review fixes, run 4 (step 8), 2026-10-21

## T14. The blueprint's sixteen sections (R49, G18)

- **New function `section_number(line)`**, replacing `numbered_section`: the number a level-2 heading opens with, followed by `.`, `)`, `:`, white space or the end of the line (`SECTION_NUMBER`), or None. `## 4)` and `## 4:` are section 4 beside X09's pinned `## 4`, `## 4.` and `## 4 Title`; `## **4. Boards**`, `## Section 4: Boards` and `## Four. Boards` give None. `blueprint_client_lines` uses it, so X11's segments and D read the sections the same way; `CLIENT_SECTIONS` is 1 to 15.
- **New function `section_problem(lines)`**: None, or the (field, problem, expected) of the stop. `blueprint` (P4) is exit 3 on `<strand>/solution/blueprint.md`: field `(whole file)`, problem "cannot find sections 1 to 15", unless level-2 headings numbered 1 to 15 are each found once and in order before section 16 (the expected value names the first section missing, repeated or out of order); field `line <n>`, problem "a level-<1|2> heading that is not one of the sixteen numbered sections sits before section 16, so the text under it would not be checked", for a level-2 heading that is no numbered section, or a level-1 heading after section 1, before section 16. Both expected values end "write the sixteen section headings as blueprint-guide.md numbers them (## 4. Structure mapping), with every added item inside one of them as a level-3 subsection (### <item>), then run this again". Text after section 16 is internal under any heading; with no section 16, every heading after section 15 counts as before it. The check runs where X09's did, after the wall is built.
- **For callers** (P5): the blueprint template and the solution-blueprint skill write the sixteen numbered level-2 headings in the pinned shape, each once and in order, with added items as level-3 subsections and headings inside prompt text at level 3 or below (owed to WP7 and WP9).

## T15. A word whose plural is a stop word (R50)

- **New function `plural_forms(word)`**: the shapes `word + "s"` and `word + "es"` that R43's `plural_stems` reads back as `word`, so `requirement` gives `requirements` and `class` gives `classes`.
- **`kept`** (T1, T13): a single word is also dropped when one of its `plural_forms` is in `stop`, as it is when one of its `inflection_stems` is. The other folders' slugs (P2) are cut by the same rule. Runs, X26 step 1's forms, the checked side and `clients-index/1` are unchanged; `index`'s `single_words` shows the words that remain.

## T16. O holds only this client's own words (R51, G17)

- **New function `own_text(rel, text)`**: the part of a record file that feeds O, or None. `calls/`, `inputs/` and `research/` files give their whole text; `CLIENT.md` gives its front matter's `name`, slug and `former_names`, a blank line between them (nothing when the front matter cannot be read); a blueprint file (`kind_of` gives `blueprint`) gives its client-facing lines (`blueprint_client_lines`) with every other line blanked in place; every other file, the allowlist included, gives None. `build_wall` adds to O only what it gives; `ALLOWLIST_FILE` is gone.
- **Building it** (P2): O is built from the parts above, not from every file X11 reads. `record_texts`, the sets F, R, Q and E, D and the index's harvest are unchanged, and so are `Own.left_out` (R37, Z15) and `Own.has`.
- **For callers** (P5): a name this client uses that sits only in working notes, the log or strand files, and also in another client's entry, now blocks in this client's output; the way out is a call, a document or a research note that holds it.

## T17. A section heading's title is checked (R52)

- **New constant `SECTION_TITLES`**: the sixteen titles of the blueprint template, as the guide numbers them. A heading whose title has the same normalised words (X24) as its own section's title is plugin vocabulary and is not checked.
- **New function `section_titles(lines)`**: {line index: the line with only its title kept} for each level-2 heading numbered 1 to 15 whose title is not its section's own. The title is the text after the number and its separator, before any closing hashes; the number, the hashes and the marks are blanked, so positions stay.
- **`blueprint`** (P4): each such title is checked in the blueprint unit with its section's text, under every rule the body meets, the wall included, and never as glossary text; a finding on it carries the heading's line and column. No other output changes.
- **Sets** (P2): in every blueprint file, the heading lines of sections 1 to 15 feed none of F, R and Q, as the client-facing lines do not. They still feed D, and O is unchanged.
- **For callers** (P5): the blueprint template and `blueprint-guide.md` write the titles exactly as `SECTION_TITLES` holds them (owed to WP7); a title the session changes is checked like the section's text.

## T18. A run, a quote or a name split over payload strings (R53, G19)

- **New function `check_joined(run, file, units, strand)`**: `payload` (P1) runs it after every unit's own check, and `scan` after the units of each `.json` file it reads, which go through the same walker (T3). It joins the payload's strings in walk order with single line breaks and checks that one text under `spanning_rules` (copied runs, quotes and the wall), and its HTML-decoded copy the same way. Keys, numbers, structural ids and a string that holds JSON do not join; the strings walked inside such a string join in its place. A payload with fewer than two such strings gives nothing.
- **New function `spanning_rules(run, check)`**: `runs_and_quotes` and the wall on one `Check`. `html_hits` gains an optional `rules` argument that narrows the rules run on the decoded copy; every rule runs by default, as before.
- **A finding of the joined text**: only a hit that spans two or more strings is kept, and only when no finding of its rule and class in one of those strings overlaps it. It is reported at the first string it touches: `field` is that string's path, `match` the whole hit with the line breaks shown as spaces, and a new key, `fields`, lists the paths of every string it spans. With `--spans`, `span` covers the part of the first string the hit holds. No other output changes; `blueprint` and the text files of `scan` are unchanged.
- **`Unit.joins`**: true for a payload string that joins, set by `payload_units`.

## T19. A key written twice in one JSON object is exit 3 (R54, G20)

- **New function `strict_json(text, base="$")`**: `json.loads` with `object_pairs_hook=unique_pairs`, so a key written twice in one object is refused. It raises `ValueError` when the text is not JSON at all, and `RepeatedKey(path, key)` when it is: only then is the text parsed a second time, its objects kept as `Pairs`, and walked in X22's order to give the path of the first repeated key, ending in `<key>` (for example `$.item_name<key>`). Text after the value is still not JSON, so a plain sentence that opens with an object holding a repeated key is not refused.
- **`json_value(text, name, once)`** reads through `strict_json` for every JSON file the lint reads: the payload file, a `.json` file `scan` reads, `local/settings.json` and `<home>/clients-index.json`. The old `unique` flag, which only the settings set, is gone. A repeated key is exit 3: `error.file` the file's name, `error.field` the key's path, `error.problem` "the key "<key>" is written twice in one object, so what the file says depends on the program that reads it", and `error.expected` says to write each key once, as the tool will receive it (payload and scan), as `record.py home init` writes it (settings), or as `index` writes it, with the backup to restore (index). The settings' error field was the bare key; it is now the path.
- **`payload_units`**: a string that holds JSON (T3) is parsed by `strict_json` with the base `<path><json>`; a repeated key inside it is exit 3 at the path through that string, such as `$.column_values<json>.text_1<key>`. `args_digest` is null when the file itself has a repeated key, and is printed as before when the key is repeated inside a string, since the digest is taken before the walk; exit 3 is never a pass either way. The same key at two depths, or in two objects, is not repeated.
- **New helper `key_path(path, key)`**: X22's path of a key, shared by the walker and `strict_json`. `terms` reads `.json` files as text, so it is unchanged; the lint reads no other JSON (not `account.json`, the lock or the fixture's `manifest.json`).

## V2. The strict JSON reader is shared with `mmb_common.py` (R55)

- **`strict_json`, `RepeatedKey` and `key_path`** are now `mc.strict_json`, `mc.RepeatedKey` and `mc.key_path`, moved unchanged with `SIMPLE_KEY`, so T19's reader has one implementation, which `mmb_common.read_json` and `record.py init`'s index read use too. `unique_pairs` and `Pairs` live there as private helpers. No command's output changes.

## T20. A table row reads its header and first cell for the cost cue (R56, G21)

- **New function `table_cues(text)`**: `(start, end, cue)` for each body row of a Markdown table in a folded text, where `cue` says whether the table's header row or the row's first cell holds a cost cue. A table is a line holding a pipe followed by a rule row (`TABLE_RULE`, outer pipes and colons optional) and the lines holding a pipe after it, or a run of lines that each start with a pipe, its first line the header.
- **`parse_numbers`**: a number whose own sentence holds no cost cue takes its row's `cue` when it sits in a table body row, unless it is a bare run of eight digits or more (`ID_SHAPE`, the id row's shape). `Number.cue` is otherwise as before, so F's split, the wall's `figures` and the checked side's figure rule for 10 to 999 all read tables the same way. The function runs only on a text that holds a pipe.
- **Pinned region `cost-cues`**: `COST_CUES` gains `amount`, `amounts`, `total`, `totals`, `fuel` and `fuels`. No command's output shape changes; `index` can publish more figures for a record whose tables or sentences hold these words.

## T21. An exclusion figure's wall forms keep two significant digits (R57, G22)

- **New function `exclusion_top(value)`**: the largest k at which an exclusion figure's form still holds its first two significant digits, or its one for a figure written with one significant digit; 0 for a figure below 10.
- **`figure_forms(value, floor, top=9)`**: k runs from 0 to `top`. `build_entry` (P3) passes `exclusion_top(value)` for each exclusion figure, so P3's "every exclusion figure at n of 1 or more" now reads: at n of 1 or more for k from 0 to `exclusion_top`. Cost figures and O call it as before. `clients-index/1` is unchanged; an entry with an exclusion figure publishes fewer figure digests after its next `index`.

## T22. Cents and exponents on the wall (R58, G23)

- **`tested_forms(value, precision)`** replaces `tested_form`: a list of the forms to test, the rounded one and, for a number whose precision is below a unit, the truncated one too. `Wall.hits` (P2) blocks when any of them is in another entry's `figures` and O does not hold it.
- **`NUMBER` and `parse_numbers`**: a new optional group `exp` after the decimals, `e[+-]?\d{1,2}` on the folded text; value and precision are both scaled by its power of ten, and such a number is never `plain`. Every number rule, F's split and the wall read it. No command's output shape changes.

## T23. Initials written with spaces or full stops (R60, G25)

- **`Wall.initials(tokens, gaps, file)`**, called by **`Wall.hits`** (P2, checking a unit) for each reading of the text: it finds runs of tokens that are each one letter written as a capital, with a gap that fully matches `INITIALS_GAP` (`\.?[ \t]*`: spaces or tabs, after at most one full stop) between each two. Every contiguous run of two to six of them is looked up fused through `Wall.name_class` (`T F M`, `T. F. M.` and `K H L F T` as `tfm` and `khlft`, class `name`, `term` or `slug`), unless O holds the run spaced in a file other than those left out. A lower-case letter, a comma, a word or a line break between the letters ends a run. `wall_candidates`, `build_entry`, `Own` and `clients-index/1` are unchanged.

## T24. Everyday method rows block only hyphenated (R61, R13 (b))

- **New pinned region** `# pinned: everyday-method-rows`, after `sales-framing`: `EVERYDAY_METHOD_ROWS`, the hyphenated `method` rows whose spaced form is an everyday phrase (`never-say`, `not-obtainable`, `cost-of-waiting`, `exit-ramp`). The script now has 14 pinned regions; `test_L274_L275_...` counts them, and a unit test keeps each entry a hyphenated literal `method` row of `shared/leak-terms.txt`.
- **`literal_regex(term, tokenised=False, fused=False, plural=False, spaced=True)`**: with `spaced` false, a hyphenated row puts `HYPHEN_GAP` (a run of gap marks holding a hyphen, an underscore, a slash, a pipe or a middle dot) where the row has its hyphen, and X32's `GAP` elsewhere. `Lists` passes `spaced=False` for a `method` row in the region, from either list. Every other row, and every other class, is built as R13 built it. No command's output shape changes; `scan`, `payload` and `blueprint` find fewer `method` terms where those four rows are written spaced.

## T25. Three internal-use phrases are clearable per client (R62, R17 (b))

- **Pinned region `internal-notes`** gains `CLEARABLE_NOTES`, the normal forms `internal only`, `internal use only` and `not for clients`. The region count is unchanged.
- **`apply_allowlist(run, unit, text, findings)`**: an `internal-note` finding whose matched text has one of those normal forms is cleared by an ok row of the strand's own allowlist whose term has the same normal form, as a `method` term is: severity `caution`, rule `internal-note` and class null kept, `cleared_by` naming the row, and the caution counted in `counts`. A row without an ok, or with an ok that says no, clears nothing. Every other `internal-note` finding (the speaker labels, the front-matter line and block, "never client-facing", "not client-facing", "not for the client", "note to self") is never cleared, and a row that names one still adds the `allowlist` warning. No command's output shape changes; `scan`, `payload` and `blueprint` can now exit 2 where such a row exists.

## T26. A `.com` address without a scheme hides its ids (R63, R27 widened)

- **`COM_ADDRESS`**, beside `SCHEMED`: a web address with no scheme whose host is one or more labels of ASCII letters, digits and hyphens ending in `.com`, then `/` and a path that stops at whitespace, a comma, a pipe or a closing bracket, as a bare URL does. It does not start after a letter, a digit, `_`, `.`, `-`, `@`, `/`, `:` or `%`, so `hxxp://example.com/...`, `ops@example.com/...` and `ex_ample.com/...` are not addresses.
- **`real_links(text)`** now returns the schemed link targets and every `COM_ADDRESS` span, sorted. Only the id row's mask reads it (`Check.regex_rows`, the shipped row and Z03's `ID_WIDE`). `link_spans`, the split ids, the credentials, the figures and every other rule are unchanged. No command's output shape changes; `scan`, `payload` and `blueprint` find fewer `id-patterns` ids where an id sits in such an address.

## T27. The tool-category check is dropped (R64, A30)

- **Removed:** the rule `tool-categories` (from `RULES`), `COUNTED_PREFIX`, `Check.tool_categories`, `Check.paragraph_of`, `Check.proper`, `Lists.category_words`, `Pattern.counted` (so `Pattern(rule, cls, regex, origin, term, tokenised=False)`), `EVERYDAY_CATEGORIES`, `CALENDAR_FORMS` and `literal_regex`'s `plural` argument (so `literal_regex(term, tokenised=False, fused=False, spaced=True)`). The pinned `leak` region holds every token of `Pinned: leak` as before, now without `tool-categories` and `tool-category-`.
- **Kept:** `SENTENCE_END`'s rule that a full stop after `e.g.`, `i.e.`, `etc.`, `vs.` or `approx.` ends no sentence, for the cost cue and the paraphrase rule; `sentence_spans` and `paragraph_spans`. The split-figure assertion is unchanged.
- **`Check.execute`**: a `summary` scan no longer runs `Check.literals` (its literal rows ran only to count categories); it runs the number rules and the run and quote rules.
- **`shared-words`** is regenerated after the shared edit: 47 words out, none in. `shared-phrases` is unchanged.
- No command's output shape changes; `scan`, `payload` and `blueprint` never report `tool-categories`, and a sentence that named three tool categories is checked by the other rules only.

# Changed by A33, 2026-10-22

The four loosenings of A33, after demo 1 (`DECISIONS.md` R66 to R69). No command, flag, rule name or envelope field is added or removed; a command reports fewer findings where these say so. The pinned regions are unchanged but for the `cost-cues` comment, and the `structural-id-keys` region still equals `test_leak_fixture.py`'s copy.

- **Ids as arguments (R66).** New `ID_KEY` and `structural_key(key)`: a key of `STRUCTURAL_ID_KEYS`, or `id`/`ids`, any key ending `_id`/`_ids`, or a camel-case key ending `Id`/`ID`/`Ids`/`IDs` after a lower-case letter or a digit, in any case. `payload_units` (section 2, T3) marks a digit-only value under such a key structural, and an object key made only of digits (no leading zero) structural too, as monday keys widget and mirror settings by board id. `paid`, `valid` and `grid` are not id keys; an id in text and the user's own ids still block.
- **Small numbers (R67).** New `SMALL_FIGURE = 100`. `Sets.add_numbers` keeps no figure below 100 in F (cost or record; percentages as before). `Check.classify` returns for a number below 100 after the exclusions, and `Check.split_match` tries only the exclusions below 100: such a number never blocks as a figure and never warns. `words_number` reads "<n> and a half <thousand|million|billion|grand>". Section 4's rows change: `figure` is a number matching a cost figure of 1,000 or more, or one of 100 to 999 beside a cost cue, a currency sign or a rate suffix, or a percentage matching a cost percentage; `record-number` and `number` warn on numbers of 100 or more (percentages of 10 or more). The index's `figures` are unchanged (cost figures of 1,000 or more).
- **The blueprint (R68).** `Check.execute` runs no `runs_and_quotes` in modes `blueprint` and `glossary`, so `blueprint` reports no `copied-run` or `quote` finding; a malformed glossary mark still warns (rule `copied-run`, X09). P4's line "under every rule, the glossary exempt from the copied-run rule only" now reads: under every rule but the copied-run and quote rules. `payload` and `scan` keep both, and the blueprint's internal text is still a source for them (Z19).
- **Sample rows (R69).** `Unit` gains `sample`; `payload_units(file, data, strand, seq, sample=False)` sets it on every unit, and `cmd_payload` passes `sample=True` for `--kind item_batch`. A sample unit's numbers raise no `number` or `record-number` warning (in `classify` and `split_match`); cost figures, cost percentages, exclusions, the split-figure assertion, the wall and every string rule still run. `html_hits` carries the flag to the decoded copy.
- **For callers (P5).** Run `blueprint` before the card as before; a copied run or a quote in the blueprint no longer stops it, and the payload check at each write is the gate for them. An `item_batch` payload's exit 2 now means a warning that is not about an invented number.
- **The fixture.** Six cases change their expectation (K02-p, K02-t, K03a-p, K03b-p, R10c-p, R14-p); `test_leak_grading.py` holds the override until `a33-fixture.patch` (the session's scratch folder, `a33/`) is applied to `tests/fixtures/leak/manifest.json` and its README, after which it changes nothing. Counts with it: 106 blocks, 1 warns, 1 caution, 16 limits, 124 passes.

# Changed by A34, 2026-10-22

A client's own figures warn in their own build (`DECISIONS.md` R70). No command, flag, rule name or envelope field is added or removed, and the pinned regions are unchanged but for the `cost-cues` comment. A finding changes its severity where this says so; nothing else changes shape.

- **The client's own figures warn (R70).** `Check.classify` reports the rule `figure` with severity `warn` where it blocked: a number matching a cost figure of 1,000 or more, one of 100 to 999 beside a cost cue, a currency sign or a rate suffix, and a percentage matching a cost percentage. `Check.split_match` reports `split-figure` with severity `warn` for a cost figure in split form. The problem texts are the same; the expected text is the new `OWN_FIGURE_EXPECTED`, "check the client's own figure is meant for their build; it is reported and kept". This holds for every command that runs the figure rules (`scan` in its full, summary and client-safe-block modes, summary reading split figures only, `payload` and `blueprint`), every form they read (digits, words, abbreviations, currency signs and codes, spaced thousands, table cells, a line break, an HTML tag or entity, a JSON number, a link) and sample rows.
- **Still blocking.** An exclusion figure, at any value and in every form (`exclusion` of class `figure`, and `split-figure` for its split form); another client's figure on the wall (`wall` of class `figure`); and every rule that is not about the record's own figures. Section 4's `figure` row now reads: warns on a number matching a cost figure of 1,000 or more, or one of 100 to 999 beside a cost cue, a currency sign or a rate suffix, or a percentage matching a cost percentage; `split-figure` warns for the client's own figure and blocks for an exclusion figure.
- **Sample rows (R69, R70).** An `item_batch`'s cost figures and cost percentages warn as anywhere else; its other numbers still raise no `number` or `record-number` warning. R69's "cost figures, cost percentages ... still run" now reads: they run, and warn.
- **For callers (P5).** Exit 2 from `payload` or `blueprint` may now be a client's own figure: the write goes ahead and the warning is shown to the user. Exit 1 still stops the write; a payload holding an own figure and a real block exits 1 with both findings. `--spans` gives a span for blocks only, so an own-figure warning carries none. An allowlist row that names an own figure no longer meets a block, so it adds no allowlist warning.
- **The fixture.** Eighteen planted cases change: nine whose only block was the client's own figure now warn, exit 2 (K01-p, K05-p, K06-p, K07-p, K09-p, K26a-p, R01-p, R02-p, D06-p); seven keep another block and expect the figure as a warning (T09-p, R18-p, R22-p, P-board-p, P-project-p, P-agent-p, P-generic-p); and K04-p and K23a-p expect the figure as a warning beside the copied run of the brief that blocked with it all along, now named. `a34-fixture.patch` (this folder) carries the manifest and README changes; `test_leak_grading.py`'s counts are 97 blocks, 10 warns, 1 caution, 16 limits, 124 passes. `a34-shared.patch` (this folder) moves the client's own figures from the blocks to the warnings in `shared/safety.md`, with no word new to `shared/`.

# Changed by A36, 2026-10-22

The three loosenings of A36, after demo 2, and one reader fix (`DECISIONS.md` R71 to R74). No command, flag, rule name or envelope field is added or removed, and no pinned region changes; a command reports fewer findings where these say so.

- **The named test workspace (R71).** New `REFERENCED_ORIGIN`, `referenced_workspaces(run)` and `unnamed(text, names)`. In a record whose `CLIENT.md` `build_target` is `own-account`, `build_entry` masks, in every D text before the harvest, each name that a strand's `solution/build.json` holds as an `objects` row of `type` `workspace` and `origin` `pre-existing-referenced`, so `index` publishes neither the name nor its words, and `single_words` no longer lists them. The ledger is read through `Run.text`, so it is listed among the inputs; a ledger that cannot be read gives no name. The same words elsewhere in the record, a `created` workspace and a client-account record are harvested as before. The ledger does not feed R44's age check.
- **The firm's sound-alike rule (R72).** New `ordinary(word)`: a common word, a stop word or a common word's plural. `Check.phonetic` reports no hit of a `firm` source whose window is all ordinary words and whose letters are not the firm's own. The literal firm rows, other phonetic classes and the whitelist are unchanged.
- **Planned values in a payload (R73).** New `ELEMENT_KEYS`, `Plan(streams)` (with `grams`, `sub`, `dele` and `holds(gram, lookups)`), `planned_streams(lines)`, `frozen_plan(run, strand)` and `Run.plans`. `Check.near_windows(words, which, usable, exempt, planned=None)` takes a filter applied to each window's sources. In `payload` only, `Check.runs_and_quotes` drops the payload strand's blueprint files as sources of a six-word run, or of a near copy, that the frozen revision (`STRAND.md` `version`, `version.md` `revision`, `versions/<v>/blueprint-r<N>.md`) holds among its planned values: sections 1 to 15, the prompt blocks and the glossary, section 16's sample data plan, and the element-key table's name cells. Other sources still report `copied-run`; `scan`, `blueprint` and the quote rule are unchanged.
- **Commented rows (R74).** `section_rows` skips the lines of an HTML comment, one line or several, as `strict_rows` does, so an example row in a comment under `## Exclusions` or `## Allowlist` is read by neither the exclusions nor the allowlist.
- **For callers (P5).** A payload that writes what the frozen revision plans now passes where it blocked; a payload written before the strand's first freeze still meets the copied-run rule on the blueprint. Run `index` again in a demo record once its build's approval has written the referenced `W1`, so its entry drops the test workspace's name.
- **The fixture and `shared/`.** The trap fixture is unchanged and no planted case changes its outcome. `a36-shared.patch` (this folder) adds the three loosenings to `shared/safety.md` in words already in `shared/`.
