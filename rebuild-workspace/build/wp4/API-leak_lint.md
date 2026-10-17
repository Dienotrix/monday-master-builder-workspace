# `leak_lint.py` part 1, for the part-2 agent

Date: 2026-10-17. Internal build file: never client-facing.

`plugins/monday-master-builder/scripts/leak_lint.py` (2,801 lines), tested by `tests/unit/test_leak_lint.py` (1,263 lines, 110 tests). Part 1 builds the frame, the loading and checking of every list, the readers (`.md`, `.txt`, `.docx`, payload JSON), every rule that needs one record and one text, the generic payload walker, and the commands `scan` and `payload`. `blueprint`, `wall`, `terms` and `index` sit in the parser and answer exit 3, "not built yet". The cross-client wall inside `scan` and `payload` is not built either, so a check in a home that holds another client record, or an index, stops with exit 3 (DECISIONS Z02). Nothing can return 0 on a path that is not built. Gates at hand-over: the whole suite green under `/usr/bin/python3` (3.9.6) and Python 3.14.6, 456 tests each (346 before, plus 110); `tools/lint_plugin.py` 0 errors, the `leak` pair compared; no `__pycache__` (section 9).

The decisions this follows are `DECISIONS.md` X01 to X47, Y01 to Y09 and the new Z01 to Z11 ("Added by code part 1 (step 5)").

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
| `# pinned: leak` | `MARKERS`, `KINDS`, `FAMILIES`, `KIND_FAMILIES`, `BLOCK_MARKS`, `HEADINGS`, `ROW_KEYS`, `EXCLUSION_KINDS`, `INDEX_FIELDS`, `INDEX_FORMS`, `SEVERITIES`, `VERDICTS`, `MODES`, `RULES`, `WALL_CLASSES`, `CLEARABLE`, `COUNTED_PREFIX`, `LOCAL_CLASS`: every token of `Pinned: leak` and no other string literal, no number and no backtick | yes, both ways (0 errors) |
| `# pinned: common-words` | `COMMON_WORDS` (1,098 words, about a hundred monday and work words among them), `RUN_MIN_DISTINCT = 2` | no |
| `# pinned: stop-words` | `PRODUCT_WORDS`, `STOP_WORDS` (titles, role and common acronyms) | no |
| `# pinned: paraphrase-cues` | `PARAPHRASE_CUES` (six groups), `ROLE_WORDS`, `PRONOUNS` | no |
| `# pinned: internal-vocabulary`, `# pinned: sales-framing` | the two vocabulary groups of X06 | no |
| `# pinned: cost-cues` | `COST_CUES`, `CURRENCY_CODES`, `RATE_SUFFIX` | no |
| `# pinned: confusables` | `CONFUSABLES` (Cyrillic and Greek look-alikes, dashes), `NARROW_SPACES` | no |
| `# pinned: credential-shapes` | `CREDENTIAL_SHAPES`, `LONG_SECRET` | no |
| `# pinned: internal-notes` | `INTERNAL_NOTE_PHRASES`, `FRONT_MATTER_LINE`, `SPEAKER_LABEL` | no |
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
| `tool-categories` | a sentence that hits three distinct `tool-category-` classes, in a paragraph with no proper noun; a single hit is never reported | X12 |
| `allowlist` (warn) | a row with no `ok`, on every run; a row that meets a finding it may not clear, once per finding, the block kept | X09, X10, Y06 |
| caution | a `term` of class `method`, `internal-vocabulary` or `sales-framing`, or a `paraphrase` cue, cleared by an ok row of the strand's own allowlist (normal forms equal); `cleared_by` names the row | X10, X39 |

Modes: `summary` runs the run and quote rules and the two assertions only, against every R source but the record's `SUMMARY.md` files (X37). `client-safe-block` checks only the text inside the file's well-formed blocks, with every rule but the run rule; malformed marks are exit 3 naming the line; no block is one warning, exit 2 (X38). A checked file never feeds its own check (Z04).

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

- The wall: `wall_hits` and the removal of `wall_guard`; the index (`index`, `clients-index/1`, the home mutex, the backup, X02, X29, X46); D and O (X26, X27), the slugs (X21), the coverage check (X30); the `wall` command.
- `blueprint` (sections 1 to 15, the prompt blocks, the glossary, exit 3 with no numbered section, X09) and `terms` (X31).
- The payload walker's proof over every kind of the trap fixture (X14, U3), and the wall inside `payload`.
- `test_leak_wall.py`, and the grading of the whole fixture in `test_leak_fixture.py`.
- The caller paragraph of X47 in this note, and the checklist rows.

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
