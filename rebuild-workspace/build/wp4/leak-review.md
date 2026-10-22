# Leak lint: the adversarial review (WP4 step 7)

Date: 2026-10-17. Internal build file: never client-facing.

## Part 1: the rules (frozen at 4f28132)

Reviewed: `plugins/monday-master-builder/scripts/leak_lint.py` and `shared/leak-terms.txt` exactly as committed at `4f28132`, exported with `git archive` into the session's scratch folder. The specification is `DECISIONS.md` (U1 to U5, the X entries, Y01 to Y09, Z01 to Z11), `API-leak_lint.md` part 1 and ARCHITECTURE 9.6. The wall, the index and the payload walker's field coverage are left to the second pass.

### How to re-run the probes

The probes live in the scratch folder:

`$SCR = <scratchpad>/wp4-review`

- `$SCR/frozen/` is the exported copy at `4f28132`. Every probe runs `$SCR/frozen/.../scripts/leak_lint.py`. To probe a fixed script, change `SCRIPT` in `harness.py`.
- `$SCR/probes/harness.py` builds a fresh home under `$SCR/homes/<id>/` for each probe. The home holds an invented `settings/1`, an invented client record `brindle-tiles` with one strand `001-job-board`, and a call summary. The call carries the cost figure 318,460, one `[Q]` quote, an internal run and a client-safe block. The harness then runs `leak_lint.py --record <home>/clients/brindle-tiles scan` (or `payload --strand 001 --kind generic --file .work/strands/001-job-board/p.json`) with `MMB_HOME` set to that home.
- Run a probe: `cd $SCR/probes && PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 F01.py`. To run the lint under 3.14, add `PROBE_PY=<home>/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14`. Each line prints the exit code and the blocking rules. `REPRODUCED` means the finding still stands; `ok` means the line behaves as expected (the controls, and the case once it is fixed).
- `$SCR/probes/explore/` holds the wider exploration scripts the findings came from. They are kept for context only.
- Every probe gave the same result under Python 3.9.6 and 3.14.

Invented test values: the firm `Pellmark Advisory` (renderings `Pellmark`, `pellmark.example`); the seller's never-shown workspace `Ledger Room Internal` (id 73915088) and default account `fallow-yard-build` (73915062); an exclusion `Odell Quarry` and a figure row `77,250`; client staff `Odile` and `Maren`. F17 uses a separate firm, `Thymbel`.

### Counts

| Rank | Findings |
|---|---|
| blocking | 11: F01 to F11 |
| should fix | 16: F12 to F27 |
| note | 14: F28 to F41 |

The most serious finding is F01. A cost figure written right after a hyphen, a dash, a minus sign, a slash, a full stop or a straight quote is not read as a number at all. The same happens with a currency code written straight onto the figure. So the ordinary range "300k-318k" and a negative "-318,460" both leak the client's figure.

---

### Blocking

#### F01. A figure after a sign, a dash, a slash or a quote is not a number

- **Rule and function.** `figure`, `exclusion` (figure rows) and `split-figure`, all through `parse_numbers` and the `NUMBER` pattern (script line 997). The pattern's lookbehind is `(?<![\w.,' /-])`. It refuses a number that follows `-`, `/`, `.`, `,` or `'`, and dashes and the minus sign fold to `-` first. A currency code needs a word boundary after it, so `USD318,460` has neither a code nor a number. The magnitude takes only a space before it, so `318-thousand` reads as 318. Neither `digit_chains` nor the word reader picks any of these up.
- **Input.** `The budget sits at 300k-318k for the year.` Also: `-318,460`, `−318,460`, `'318k'`, `USD318,460`, `EUR318k`, `c.318k`, `per year/318,460`, `a 318-thousand-dollar rework cost`, the exclusion figure in `Fee band 70k-77k.`, the JSON number `-318460`, and `"-318,460"` inside a `column_values` string.
- **Probe.** `F01.py`.
- **Actual.** Exit 0, or exit 2 with only a `number` warning on the first figure of a range. No figure block.
- **Expected.** A `figure` block (an `exclusion` block for 77k), exit 1.
- **Decision.** X25: "a match with a cost figure of 1,000 or more is a figure block, in any rendering"; the five formats of A§:916. X22: every JSON number is checked by the figure rules.
- **Fix.** Narrow the lookbehind to what it guards against, a digit run's tail: `(?<![^\W_])(?<!\d[.,' ])`. Read a leading `-`, `−` or `+` as a sign (match on the absolute value). Accept a currency code written straight onto the digits, `(?:usd|...)(?=\d)`. Allow `[ \t-]?` before a magnitude word. Keep the date, version and ordinal masks as they are, and re-run the 5 × 5 format test with each form prefixed by `-`, `/`, `'` and a glued code.

#### F02. A monday id as a JSON number passes

- **Rule and function.** `id-patterns` in `Check.execute` (line 2326). A unit of kind `number` runs only `numbers()` and `seller_ids()`, never the id row. Z05 item 3 then silences the number warning for a plain run of eight digits or more, on the premise that "the id row blocks it".
- **Input.** `{"name": "Jobs", "notes_ref": 41873925}`; `{"refs": [41873925]}`; `{"board_id": 41873925.0}`.
- **Probe.** `F02.py`.
- **Actual.** Exit 0 for the first two. Exit 2 with a `number` warning for the float under `board_id`. The control, `"notes_ref": "41873925"` as a string, blocks.
- **Expected.** An `id-patterns` block, exit 1.
- **Decision.** Y08: an id "anywhere else blocks as before: ... under any other key". Only "a positive JSON integer" directly under a structural key is exempt, so a float is not.
- **Fix.** In `execute` for a number unit that is not structural, run `ID_WIDE` on its decimal text (the integer part of a float with a zero fraction too) and report the id row.

#### F03. A snapshot with an unquoted or newer schema becomes the client's document

- **Rule and function.** `copied-run`, `quote` and the conflict rows, through `is_snapshot` and `SNAPSHOT` (lines 1366 and 324), and `file_segments`. `SNAPSHOT` accepts only `schema: "document-summary/1"` with quotation marks. Any other `inputs/*.md` counts as a raw client document, which feeds E, the copied-run exemption. So a snapshot written `schema: document-summary/1`, or one a later plugin writes as `document-summary/2`, loses all of this: its internal read stops being an R source, its conflict rows stop blocking, its `[Q]` lines stop being quotes, and all of its text exempts matching runs anywhere.
- **Input.** `inputs/2026-09-10-procedure.md` with `schema: document-summary/1` and an internal line, `Our read: the depot planner is overloaded and quietly resents the new owner.`, plus a conflict row. A draft copies both.
- **Probe.** `F03.py`.
- **Actual.** Exit 0. The control, the same snapshot with the quoted schema, blocks twice under `copied-run`. Scanning the newer-schema snapshot itself runs in mode `full`, not exit 3.
- **Expected.** `copied-run` blocks. For `document-summary/2`, exit 3: a newer schema.
- **Decision.** X11 (snapshot body and conflict rows feed R); X36 order 1 (conflict rows block even where the document matches); G57 as X02 applies it (a newer schema is exit 3); A§:920, fail closed.
- **Fix.** Treat as a snapshot any `inputs/*.md` whose front matter holds a `schema:` line naming `document-summary/<n>`, quoted or not. Exit 3 when n is higher than 1. Exit 3 on an `inputs/*.md` whose front matter names any other schema. A front matter block the lint cannot place should never feed E.

#### F04. An exclusions row that does not parse is dropped in silence

- **Rule and function.** `exclusion`, through `section_rows`, `row_parts` and `load_exclusions` (lines 1610, 1599 and 1651). Only `- ` lines directly under an exact `## Exclusions` heading are read, and everything else is ignored. Y05 then takes a bracket group as keys only when every key is pinned, so `[kind: name; note: from the call]` stays part of the term. The term `Odell Quarry [kind: name; note: from the call]` can never match.
- **Input.** In `strands/001-job-board/solution/exclusions.md`: `* Odell Quarry`, `-Odell Quarry`, `1. Odell Quarry`, `### Exclusions`, `## Exclusions (client asked)`, `- Odell Quarry [kind: name; note: from the call]`, `- 77,250 [knd: figure]`. The draft reads `Order from Odell Quarry this week. Fee 77,250.`
- **Probe.** `F04.py`.
- **Actual.** Exit 2, with only the `number` warning on 77,250. The control row `- Odell Quarry` blocks.
- **Expected.** Exit 3 naming the file and line, so the client's "do not show this" is never lost.
- **Decision.** X09 (an empty term is exit 3); X33's rule for lists, "anything it cannot apply is exit 3"; A§:920 and BP:158.32, fail closed. Y05 kept the last-group reading so it "never widens what a row clears". For an exclusion, though, an unparsed group widens what passes.
- **Fix.** For `exclusions.md`, exit 3 on any of these:
  - a non-blank, non-comment line under the heading that is not a `- ` row;
  - a file with rows or bullets but no `## Exclusions` heading;
  - a last bracket group that looks like keys (`\[\s*[a-z_]+\s*:`) but holds an unpinned key.

  Keep the lenient reading for `allowlist.md`, where a lost row only removes a clearing.

#### F05. HTML entities and tags break every word rule

- **Rule and function.** `exclusion`, `term`, `phonetic`, `figure`, `split-figure`, `copied-run` and `quote` in `Check.__init__`. The text has a folded copy and a percent-decoded copy, but no HTML-decoded copy. In `Odell&nbsp;Quarry` the gap `&nbsp;` is not in `GAP`. `<b>` adds a token `b` that breaks a six-word run, and `<br>` and `&#44;` split a figure into pieces no rule joins.
- **Input.** Payload `{"body": "<p>Order from Odell&nbsp;Quarry this week.</p>"}`. Also `<b>Odell</b> Quarry`, `Pell&#109;ark`, `318,<br>460`, `$318&#44;460`, and an internal run with `<b>`, `<i>` and `<u>` on three of its words or `<br>` inside it.
- **Probe.** `F05.py`.
- **Actual.** Exit 0 or 2 for every form. The control, the plain run, blocks.
- **Expected.** A block for each.
- **Decision.** X24: case, punctuation, line breaks, table cells and emphasis "never break a match". X28: one normalisation for every rule that compares words. A§9.6: "every monday text payload". monday stores update and long-text bodies as HTML, and an editor or a session writes `&nbsp;` and `<br>` without thinking.
- **Fix.** Add a third copy beside the percent-decoded one. Blank each tag to one space and decode entities with `html.unescape` (the `html` module is not on L10's import ban), keeping the offset map. Run the literal, phonetic, number, run and quote rules on it as `vfd` is run.

#### F06. A client quote with a quoted word inside it is lost

- **Rule and function.** `quote`, through `quote_texts` (line 1379). When a `[Q]` line holds any double quotation marks, only the quoted spans are the quote. A line such as `[Q] Odile: we lose the "grout" batch sheets on the yard almost every week` gives the one-word quote `grout`. Inside a client-safe block the line feeds Q only, not R, so nothing else catches the copy.
- **Input.** That line inside the call's client-safe block. The draft reads `We lose the grout batch sheets on the yard almost every week.`
- **Probe.** `F06.py`.
- **Actual.** Exit 0. The control quote, wholly in quotation marks, blocks.
- **Expected.** A `quote` block on the 11 words.
- **Decision.** A§:916 (client quotes of eight or more words block); X36 ("an eight-word client quote inside a client-safe block still blocks when copied"). X24's "the text between double quotation marks" is written for a line that quotes its whole utterance. The fail-safe reading takes both.
- **Fix.** Return both the quoted spans and the whole remainder of the line (marker, locations and speaker removed) as quote texts.

#### F07. A marker written straight onto a word is missed

- **Rule and function.** `term`, class `markers`, through `literal_regex` (line 542). Every literal takes `(?<![^\W_])` and `(?![^\W_])` as its boundaries. For `[I]` the boundary falls outside the brackets, so `overloaded[I]` fails on the `d` before the bracket.
- **Input.** `The planner is overloaded[I].`; `[Q]Odile said the sheets go missing.`; `See the note[E]s.`
- **Probe.** `F07.py`.
- **Actual.** Exit 0. The control, `overloaded [I].`, blocks.
- **Expected.** A `markers` block. A footnote-style marker written straight after a word is the most natural way to cite evidence inline.
- **Decision.** X03 (the nine markers block); A§:916 ("evidence markers, assumption labels").
- **Fix.** In `literal_regex`, add the leading boundary only when the term's first character is a word character, and the trailing one only when its last is.

#### F08. A `.docx` carries text Word shows that the reader never reads

- **Rule and function.** Every rule on a `.docx`, through `docx_parts` and `word_paragraphs` (lines 1772 and 1729). Only these are read:
  - the `w:t`, `w:delText` and `w:instrText` element text of the listed parts;
  - a property part's element text and the `name` attribute.

  Not read:
  - an altChunk (`word/afchunk.docx`, `.htm` or `.mht`, which Word renders inline as body text);
  - `w:author` on comments and on tracked insertions and deletions;
  - hyperlink targets in `word/_rels/*.rels` and in `w:fldSimple/@w:instr`;
  - picture alt text (`wp:docPr/@descr`, `@title`);
  - embedded objects under `word/embeddings/`.
- **Input.** Each probe case is a separate `.docx` with the firm name, or a record path, in one of the places just listed.
- **Probe.** `F08.py`.
- **Actual.** Exit 0 for each. The control, the firm in the body, blocks.
- **Expected.** A block. Where the lint cannot read a part that Word will show, exit 3.
- **Decision.** X35 ("headers, footers, notes, comments and custom properties carry text to the client just as well, and reading them is the fail-safe side"); A§:920 (a draft the lint cannot read cannot be marked ready).
- **Fix.** Read the attributes a reader sees: `w:author` and `w:initials` on any element, `w:instr`, `descr` and `title`. Read `Target` of every relationship with `TargetMode="External"`. Exit 3 on any `altChunk` element, any member under `word/embeddings/` and any part with an `.htm`, `.mht`, `.rtf` or `.docx` member name, rather than reading nested archives.

#### F09. A folder linked into `drafts/` is skipped

- **Rule and function.** Every rule, through `scan_targets` (line 2526). `os.walk` does not follow a symbolic link to a folder and does not report it either. The linked folder's files are never checked, and the scan prints `clean`.
- **Input.** `strands/001-job-board/drafts/linked`, a link to a folder inside the record that holds `Pellmark set this up.`
- **Probe.** `F09.py`.
- **Actual.** Exit 0; the linked file is not in `inputs` as a checked file. Naming the folder directly blocks.
- **Expected.** Exit 3, or the files checked.
- **Decision.** X35 (anything in the folder the lint cannot read is exit 3); BP:158.32, fail closed. A linked file is already handled: one that resolves outside the record is exit 3.
- **Fix.** In the walk, for every entry of `dirs` that is a link, either walk it (with the inside-record check `target_of` already does) or exit 3 naming it.

#### F10. Credentials just outside the six shapes

- **Rule and function.** `credential`, through `CREDENTIAL_SHAPES` and `LONG_SECRET` (lines 256 and 269).
- **Input.** `API key: 9f8e7d6c5b4a39281706f5e4d3c2b1a0`. The key word is written with a space, and lower-case hex fails shape 6's upper-case test. Also:
  - `The password is Tilework42 for the portal.` (no separator);
  - `pw: Tilework42`;
  - `passphrase = blue-otter-lamp`;
  - `Login: depot.admin / Tilework42`;
  - `Password:` with the value on the next line;
  - `?private_token=Ab12Cd34Ef56Gh78` (`\btoken` fails after `_`);
  - `Authorization: Basic dXNlcjpwYXNz` (12 characters, under 16).
- **Probe.** `F10.py`.
- **Actual.** Exit 0 for each. The control, `password: Tilework42`, blocks.
- **Expected.** A `credential` block.
- **Decision.** X15 and Y04, with BP:158.17 and A17: a prompt never carries a credential. Y04 widened shape 2 because notes write credentials loosely, and these are the same notes.
- **Fix.**
  - Add to shape 2's key words: `api key` with a space, `pw`, `passphrase`, `passcode`, `login`, `credentials`. Let the separator be `:`, `=`, ` is ` or a line break.
  - In shape 4, accept any parameter name ending in `token`, `key`, `secret` or `password`.
  - Lower shape 1's floor to 8 characters for `basic`.
  - In shape 6, also block a 32-plus run of hex digits when it follows a key word.

#### F11. An excluded or seller name broken by a mark outside the gap set

- **Rule and function.** `exclusion` and `seller-account`, through `literal_regex` and `GAP` (line 309). The gap is `[\s,.\-_/|·]+`, so emphasis, brackets, a colon, an ampersand or a possessive on an inner word breaks the match. These rows have no phonetic backstop, unlike the firm.
- **Input.** `We met Odell **Quarry** today.`; `Odell (Quarry)`; `Odell's Quarry`; `Ledger Room **Internal**`; `Ledger's Room Internal`.
- **Probe.** `F11.py`.
- **Actual.** Exit 0 for each. The control, `Odell Quarry`, blocks.
- **Expected.** An `exclusion` or `seller-account` block.
- **Decision.** X28 lists exclusions among the rules that compare normalised words, tokenised as X24 says. X24: emphasis and punctuation "never break a match". X28 step 5 drops a possessive per token.
- **Fix.** For tokenised rows (firm, plugin, seller names, exclusions), match on the token stream rather than on folded characters. Compare `words_of(term)` against consecutive `Check.tokens` (the possessive already dropped), allowing a line break between tokens, and report the span from the first token to the last. Keep the fused form as it is.

---

### Should fix

#### F12. Invisible characters and look-alikes the normaliser misses

- **Rule and function.** Every literal rule, `credential` and the path rows, through `fold` and `CONFUSABLES` (lines 386 and 241), `notes_and_credentials` (line 1953) and `variants_of` (line 1911).
  - The Hangul fillers U+3164 and U+115F to U+1160 are category Lo. They are invisible but kept as letters.
  - The table lacks dotless `ı` (U+0131), Armenian `օ` and `ս`, Cherokee capitals and Latin small capitals.
  - Credentials run on the unfolded line, so a full-width colon, a Cyrillic `а` or a zero-width space inside `password` passes.
  - The slashed path copy is made only when the raw line holds `\`, so a full-width `＼` passes.
  - A line separator U+2028 inside a figure splits it, because the split-figure joiners take only `\n`.
- **Input.** `We met Odㅤell Quarry today.`; `clㅤaude code`; `master buılder`; `Ledger Rօօm Internal`; `password：Tilework42`; `calls＼2026-09-01.md`; `318 460`.
- **Probe.** `F12.py`.
- **Actual.** Exit 0 or 2. The firm is backed by the phonetic rule, so the firm with a filler blocks.
- **Expected.** A block.
- **Decision.** X28 steps 1 to 3, used by every rule that compares words. PLAN §3 names look-alikes and zero-width characters for every rule.
- **Fix.**
  - Drop every Default_Ignorable_Code_Point, not only category Cf: add U+115F, U+1160, U+3164, U+FFA0, U+180B to U+180F, U+FE00 to U+FE0F and U+E0100 to U+E01EF.
  - Widen the table with the missing letters.
  - Run the credential shapes on the folded copy as well, and make the slashed copy from the folded text.
  - Read U+2028, U+2029 and U+0085 as line breaks in `decode`.

  These are mostly deliberate disguises, which is why this is ranked below blocking.

#### F13. A literal row with a hyphen inside a word does not match the words spaced

- **Rule and function.** `term` (`method`) and `internal-note`, through `literal_regex` without tokenising (line 542). `folded.split()` keeps `run-sheet` as one word, so its hyphen is a literal character and not a gap.
- **Input.** `Check the run sheet for Friday.`; `the if asked list`; `the skipped step map`; `Copy the client safe block.`; `Internal build file: never client facing.`
- **Probe.** `F13.py`.
- **Actual.** Exit 0. The control, `run-sheet`, blocks.
- **Expected.** A block.
- **Decision.** X32 (the gaps of a row of two or more words); X24 (a hyphen is a separator); X40 (the mark "never client-facing").
- **Fix.** Build every literal from `words_of(term)` with `GAP` between the words, as the tokenised rows already are. Keep the fused form for the fused classes only.

#### F14. The near copy misses a dropped or added word

- **Rule and function.** `copied-run`, through `near_index` and `runs_and_quotes` (lines 1551 and 2256). The near copy matches eight words with one substituted, in the same positions. Dropping one word every five words leaves no six-word stretch and no aligned window.
- **Input.** The research note holds `The depot planner rebuilds the weekly crew rota by hand from the paper diary every Monday before the vans leave the yard.` The draft reads `The depot planner rebuilds weekly crew rota by hand the paper diary every Monday the vans leave the yard.`
- **Probe.** `F14.py`.
- **Actual.** Exit 0. The control, one word changed, blocks.
- **Expected.** A `copied-run` block, `near: true`.
- **Decision.** X24 added the near copy for PLAN §3's "copied run with one word changed". Its stated limits are reordering and two changes within eight words. A dropped or added word is the same light edit as a substitution.
- **Fix.** Add a deletion neighbourhood. For every eight-word window of R, index its eight seven-word deletions. For the checked text, look up each seven-word window directly (a word was added in R) and each eight-word window's deletions (a word was dropped). Apply the same filter and the same exemptions.

#### F15. A quote held in a client-safe block, with one word changed, passes

- **Rule and function.** `quote`, through `runs_and_quotes`. The quote rule has no near copy. Text in a client-safe block feeds Q but not R, so the near copy of the run rule does not cover it either.
- **Input.** `[Q] Odile: "the van drivers never see the revised fitting list until lunch"` in the block. The draft reads `The van drivers never see the updated fitting list until lunch.`
- **Probe.** `F15.py`.
- **Actual.** Exit 0. The verbatim control blocks.
- **Expected.** A `quote` block.
- **Decision.** X24 and X36: the quote rule is the one guard on block text.
- **Fix.** Run the eight-word near check (and F14's deletion check) against Q too.

#### F16. Record paths the shipped rows do not cover

- **Rule and function.** `term`, class `id-patterns`, through the shipped list (LT, `class: id-patterns`).
  - The folder rows cover `calls/`, `strands/`, `inputs/`, `.work/` and `clients/<slug>/`.
  - The file rows cover `CLIENT.md`, `STRAND.md`, `SUMMARY.md`, `discovery.md`, `blueprint.md`, `log.md`, `account.json`, `build.json` and `live-map.md`.
  - Not covered: `research/`, `solution/`, `versions/`, `drafts/`, `deliverables/`, `live/`, `meetings.md`, `readiness.md`, `close-out.md`, `exclusions.md`, `allowlist.md`, `%USERPROFILE%` and `$HOME`.
- **Input.** `See research/2026-09-01-brief.md for more.` Also `solution/exclusions.md`, `drafts/`, `deliverables/handoff/close-out.md`, `meetings.md`, `allowlist.md` and `%USERPROFILE%\monday-builder\local\`.
- **Probe.** `F16.py`.
- **Actual.** Exit 0. The control, `calls/`, blocks.
- **Expected.** An `id-patterns` block.
- **Decision.** A§:916 ("record paths"); X03 (paths in either spelling through the shipped rows).
- **Fix.** For the user's word, since the shipped list is a pinned file: add `re: \b(research|solution|versions|drafts|deliverables|live)/`, the record file names RM pins, and `re: (%USERPROFILE%|\$HOME\b)`.

#### F17. The phonetic key misses a th spelling heard as t

- **Rule and function.** `phonetic`, through `phonetic_key` and `PhoneticSource` (lines 583 and 662). `th` always keys to `0`. For a source of five to seven letters only an edit distance of 1 is allowed, so `Timbel` (key `TMPL`, distance 2) passes.
- **Input.** Firm `Thymbel` (a separate settings file); `Timbel set this up.`; `Tymbol`; `Timble`.
- **Probe.** `F17.py`.
- **Actual.** Exit 0. The control, `Thimbel`, blocks.
- **Expected.** A `phonetic` block. A transcript spells a name the way it sounds.
- **Decision.** X32 and D24; BP:158.28.
- **Fix.** Give a source a second key with `th` read as `t` (and `ph` as `p`). Or compare keys with one symbol's edit distance allowed, as the letters already are.

#### F18. Internal notes the pinned shapes miss

- **Rule and function.** `internal-note`, through `INTERNAL_NOTE_PHRASES`, `SPEAKER_LABEL` and `notes_and_credentials` (lines 274, 277 and 1953).
- **Input.** `SPEAKER_00: we lose the sheets.` (the label diarisation tools write); `Speaker A:`; `Draft notes, not client-facing.`; `For internal use only.`; `Not for clients.`; front matter whose first line is not `schema:` and whose values are unquoted.
- **Probe.** `F18.py`.
- **Actual.** Exit 0. The control, `Speaker 2:`, blocks.
- **Expected.** An `internal-note` block.
- **Decision.** X40 and Y07. The marks of internal files are "the one shape a string rule can recognise for certain", so their common spellings belong with them.
- **Fix.**
  - `SPEAKER_LABEL = r"\bspeaker[ \t_]*(?:\d+|[a-z])\b"`.
  - Add the phrases `client-facing` after `not`, `internal use only`, and `not for clients`.
  - Report a `---` line that opens a block holding a `schema:` line anywhere before the closing `---`.

#### F19. An allowlist row with `ok: no` clears

- **Rule and function.** `allowlist`, through `load_allowlist` and `apply_allowlist` (lines 1688 and 2471). Any non-empty `ok` value counts.
- **Input.** `- readiness [ok: no]`, `[ok: pending]`, `[ok: not yet, ask the user]`. The draft reads `The readiness check is done.`
- **Probe.** `F19.py`.
- **Actual.** Exit 2, the `method` term cleared to a caution.
- **Expected.** Exit 1, with the row warning that it clears nothing.
- **Decision.** X09 (`ok` is "the user's words, or `yes`"); A§:920 ("every row needs the user's OK").
- **Fix.** Refuse to clear when the `ok` value's first word is `no`, `not`, `pending`, `tbc`, `todo` or `ask`, and warn as for an empty `ok`. Better still, pin the form, `ok: yes` followed by the user's words.

#### F20. A slightly wrong client-safe mark reads as no block

- **Rule and function.** Mode `client-safe-block`, through `file_units` (line 2586). `<!--client-safe:start-->`, `<!-- Client-safe:start -->` and a dash look-alike are not marks. The file then has "no client-safe block": exit 2, and nothing in it is checked.
- **Input.** A call summary that wraps `We heard Maren is burnt out and Pellmark knows it.` in `<!--client-safe:start-->` and `<!--client-safe:end-->`.
- **Probe.** `F20.py`.
- **Actual.** Exit 2, one warning. The control marks give exit 1 (`paraphrase`, firm).
- **Expected.** Exit 3, "marks not well formed". `call-intake` goes on at exit 2.
- **Decision.** X38 (the three categories are kept out of the block "at the moment call-intake writes it"); X09 (a malformed mark exempts nothing); BP:158.32.
- **Fix.** Treat a line matching `(?i)^\s*<!--\s*client.?safe\s*:\s*(start|end)\s*-->\s*$` that is not the exact mark as a malformed mark: exit 3 in this mode, and the record warning in the sets.

#### F21. Local patterns that slip past the static check run for a very long time

- **Rule and function.** The `re:` rows of the local list, through `NESTED` (line 308) in `parse_list`. The check sees only a quantified group without inner parentheses. `(?:(?:a+))+b` and an ambiguous alternation such as `(a|aa)+b` pass it.
- **Input.** Local list `class: codes`, `re: (?:(?:a+))+b`; a draft of 34 letters `a`.
- **Probe.** `F21.py`.
- **Actual.** No exit within the probe's 15 seconds. `(a|aa)+b` takes 3 seconds on 34 characters and doubles with every two more.
- **Expected.** Exit 3 at load: "a pattern that can run for a very long time".
- **Decision.** X33 and X42 ("with patterns checked and inputs capped, a run is bounded by its input").
- **Fix.** Make the check recursive: walk the pattern with `sre_parse` (in the standard library through 3.14, deprecated) or a small bracket-matching scan. Refuse any repeated group that holds a repeat or an alternation at any depth. Failing that, cap each local row's run with a per-line length limit.

#### F22. A figure split at its thousands comma by a line break or a space

- **Rule and function.** `split-figure`, through `digit_chains` and `CHAIN_JOIN` (lines 1219 and 1025). A comma is not a joiner, so `318,` and a break before `460` read as two small numbers.
- **Input.** `The rework cost was 318,\n460 last year.`; `318, 460`.
- **Probe.** `F22.py`.
- **Actual.** Exit 2, two `number` warnings. The control, `318 460`, blocks.
- **Expected.** A `split-figure` block.
- **Decision.** X25 (split renderings joined by a line break, the first structural assertion).
- **Fix.** Accept `,` or `'` followed by whitespace or a line break as a joiner before a group of exactly three digits.

#### F23. A scan with nothing to check prints clean

- **Rule and function.** `cmd_scan` (line 2674). With no `drafts/` folder, an empty one, or drafts written to a misnamed folder, the scan checks no file and returns exit 0 with verdict `clean`. Z07 gives it mode `full` but does not decide the exit.
- **Input.** An empty `drafts/`. Then a record whose only draft sits in `strands/001-job-board/draft/`.
- **Probe.** `F23.py`.
- **Actual.** Exit 0, clean.
- **Expected.** Exit 3, or a warning naming the empty target, so close-out never reads "clean" when nothing was judged.
- **Decision.** A§:920 and BP:158.32, fail closed: "no draft is marked ready" when the lint cannot run. Z09's reasoning ("a gate that fails closed has no path to 0 that checked nothing") applies here as well.
- **Fix.** When no path is given and no file is found, exit 3 with "no draft or handoff file to check". Accept a `--allow-empty` flag only if a caller needs it.

#### F24. Paraphrase false positives on ordinary process text

- **Rule and function.** `paraphrase`, through `Check.person` and `ROLE_WORDS` (lines 2090 and 201). The person test counts a role word anywhere in the sentence, and `owner` is also monday's own People column. Process cues (`signs off`, `approver`, `a risk`, `blocker`, `holiday`, `sick`, `quit`, `visa`) and the trade demonyms `english` and `american` sit in the cue groups.
- **Input.** `The item owner signs off the quote before it moves to Done.` Also:
  - `The site manager is the approver for refunds over the limit.`
  - `A long lead time is a risk for the install date.`
  - `The owner wants English oak shelves and American walnut doors.`
  - `The supervisor sets holiday cover in the rota each month.`
  - `If a fitter is sick, the supervisor reassigns the job.`
  - `The owner pays by Visa or bank transfer.`
- **Probe.** `F24.py`.
- **Actual.** Exit 1 for each, rule `paraphrase`.
- **Expected.** Pass. Each line is ordinary client SOP text. Each needs an allowlist row per strand, with the user's ok, before it can be written.
- **Decision.** X06 chose fail-safe ("a false block costs a rewrite"). Z08 already removed three trade demonyms for this reason, and the same reasoning covers `english` and `american` (oak, walnut) and `visa` (the card).
- **Fix.**
  - Count a role word as a person only with a possessive, a name beside it, or a determiner naming one person (`her manager`, `the owner, Maren`).
  - Drop `owner` and `lead` from the role words, since X19 lists `owner` as a monday word.
  - Move `signs off`, `approver`, `a risk`, `blocker`, `holiday` and `visa` to need a proper-name person.
  - Drop `english`, `american` and `visa`, as Z08 did for three others.

#### F25. The tool-category assertion blocks ordinary instructions

- **Rule and function.** `tool-categories`, through `Check.tool_categories` and the shipped `tool-category-*` rows (line 2220).
  - The rows include everyday nouns (`spreadsheet`, `shared drive`, `team chat`, `shared inbox`, `wiki`, `email client`). A how-to sentence naming three of them blocks, and the allowlist cannot clear it.
  - The rows are singular, so `payroll systems, booking systems and shared drives` passes.
  - `e.g.` ends a sentence, which splits one sentence into two.
- **Input.** `Export the spreadsheet to the shared drive and post the link in team chat.`; `We use a spreadsheet, a shared inbox and a wiki for the team.`; the plural and `e.g.` forms.
- **Probe.** `F25.py`.
- **Actual.** The two instructions block, exit 1. The plural and `e.g.` forms give exit 0.
- **Expected.** The instructions pass, and the plural and `e.g.` forms block.
- **Decision.** X12 (fail-safe over precise, with no allowlist). A rule that blocks ordinary SOP text gets switched off, which loses the protection X12 wants.
- **Fix.**
  - Match each category row with an optional plural `s` or `es`.
  - Do not end a sentence after `e.g.`, `i.e.`, `etc.`, `vs.` or `approx.`.
  - Count `spreadsheet`, `wiki`, `team chat`, `shared drive`, `shared inbox` and `email client` only when the sentence also holds a more specific category. Or let the strand's allowlist clear the assertion by naming the sentence.

#### F26. A structural id inside a `column_values` string blocks the outer string

- **Rule and function.** `id-patterns` on the payload string unit, through `payload_units` (line 2614). The JSON string is checked once as text and once walked as JSON. Y08 exempts `item_ids` and `id` only in the walk, so the raw string still blocks.
- **Input.** `{"board_id": 41873925, "item_name": "Job 12", "column_values": "{\"board_relation_1\": {\"item_ids\": [41873926]}}"}`; a people value `{"person": {"personsAndTeams": [{"id": 41873927, "kind": "person"}]}}`.
- **Probe.** `F26.py`.
- **Actual.** Exit 1 at `$.column_values`.
- **Expected.** Pass: every write with a connect-boards or people value would otherwise block, with no way to clear it.
- **Decision.** Y08 ("Inside a column_values JSON string the same rule applies at every depth (a board-relation value of item_ids, for example)").
- **Fix.** When a string parses as JSON and is walked, run the text rules on the raw string with the structural values masked, or skip the id row on the raw string, since the walk covers every inner value. This sits in the walker, so the second pass may take it.

#### F27. The widened id row blocks long numbers that are not ids

- **Rule and function.** `id-patterns`, through `ID_WIDE` (Z03, line 306).
- **Input.** `Depot at 51.50735095, -0.12775829.` (coordinates, common in field-service seed data); `Report 20261017 attached.` (a compact date); `PO-20261017 ships Friday.`
- **Probe.** `F27.py`.
- **Actual.** Exit 1. None of these can be cleared.
- **Expected.** Pass, or a warning.
- **Decision.** Z03 asked step 7 to probe this cost. The digits after a decimal point and the eight-digit compact date are not monday ids. Y02 already treats a date in spaced groups as a date.
- **Fix.** Keep Z03's widening after `/`, `=`, `?`, `&`, `#` and `-`. Exempt digits that follow a decimal point which follows a digit (`\d\.\d{8,}`), and an eight-digit run that is a valid `YYYYMMDD` date from 1900 to 2099. A date hit becomes the `split-figure` date warning Y02 uses.

---

### Notes

- **F28. Empty files.** An empty `.md`, one holding only a byte-order mark, or only whitespace, exits 0. Nothing in it can leak, so this is safe. An empty `.json` and an empty `.docx` are exit 3, as they should be.
- **F29. The DTD guard is byte-based.** It is bypassed by a UTF-16 part: `<!DOCTYPE` in UTF-16 bytes does not match `rb"<!\s*(?:DOCTYPE|ENTITY)"`. Expat then expands the internal entity, and the text is checked, so nothing leaks (probe `explore/explore10.py`, case `utf16 doctype`). Decode the part's declared encoding before the check, or refuse a part that is not UTF-8.
- **F30. Formats outside X25.** Indian grouping (`3,18,460`), the rupee sign, `lakh` and `crore`, and a European decimal comma (`1,2 Mio.`) are not read. X19 limits v1 to English; the fixture README could list these as limits.
- **F31. A Markdown link masks any target.** In `[the board](boards/41873925)` and `[the board](hxxp://x.example/boards/41873925)` the id passes. X34 counts any Markdown link target as a link, while Z03 says a URL without a scheme "only looks like a link". Worth the user's word: mask a target only when it starts with a scheme the LINKS pattern names.
- **F32. A bare URL takes the next token.** `https://x.example/a,41873925` and `https://x.example/a|41873925` take the comma or pipe and the id into the masked link.
- **F33. A cost figure under the key `id` is never checked.** `{"id": 318460}` is exempt from the figure rules (Y08 as decided). The key `id` is generic; the user may want it tied to the object's own id only.
- **F34. Split ids outside X34's shape.** `4187/3925` (slash-joined) and `4 1873925` (a group of seven) give no block. X34 names spaces, hyphens and dots, and groups of two to four.
- **F35. Y09 still blocks two ordinary words.** `A thin bell rang.` blocks for the firm `Thymbel`: `thin` + `bell` keys to `0M` + `PL`, which is `0MPL`. That is a sound-alike by design, and the whitelist row `thin bell` clears it. Y09 fixed the case it was written for (`the thimble` passes), and plurals of the whitelisted word pass.
- **F36. The paraphrase rule's known misses.** A name as the first token (`Maren is burnt out.`), a pronoun, a lower-case name and initials all pass. This is nod 12 of the API note and X06 as decided.
- **F37. The tool-category exemption is broad.** Any capitalised day or month (`every Friday`) counts as a proper noun and exempts the paragraph, because the stop list is used only for all-capital tokens. A Markdown list of three categories passes, since each item is its own sentence (X12 as decided).
- **F38. Front-matter false positives.** A lower-case line such as `status: "Working on it" means the crew has started.` blocks as an internal note and cannot be cleared. A `---` rule followed directly by `Schema: ...` in client text blocks too. Both are rare in client text.
- **F39. Settings read loosely.** `settings.json` with a duplicate `name` key keeps the last value, as `json.loads` does. A whitespace-only seller id or slug is dropped without a word. A `--`-only slug is dropped too.
- **F40. Header and footer part names are matched case-sensitively.** `word/Header2.xml` is not read. Word writes lower case, so this is low risk. A case-insensitive match is free.
- **F41. Other ways into the exemption and the quote rule.**
  - A client quote split across two payload fields (four words in each) passes, because each string is its own unit. This belongs to the second pass.
  - A double percent-encoding (`calls%252F`) is decoded only once.
  - Any `inputs/*.md` without front matter that the session writes itself becomes client-document text, the copied-run exemption (X11 as decided). A session must never save internal notes under `inputs/`.

---

### What held

- **Normalisation.** These forms blocked on every rule that has a word list: full-width letters and digits, ligatures, mathematical bold letters, non-breaking, thin and narrow spaces, zero-width spaces and joiners inside a word, the soft hyphen, combining accents, the Cyrillic and Greek letters in the table, and upper or mixed case. The rules: the firm, exclusions, `method`, `plugin`, `assistant`, the internal vocabulary and the markers.
- **The firm rule.** Every disguise tried blocked, by its literal or by the phonetic backstop:
  - emphasis, brackets, a colon or a possessive;
  - a Hangul filler, a zero-width joiner or an enclosing mark;
  - Cyrillic or Armenian letters, or a dotless i;
  - the domain rendering;
  - the comma-split, hyphenated and fused forms.

  Misspellings within the edit distance (`Thimbel`, `Thymbell`, `Thym-bel`, `Thymbal`) blocked too.
- **Figures.** These blocked:
  - currency before or after, with or without a space;
  - `k`, `m` and `bn`, and number words with `point`, `half a` and `a quarter of a`;
  - a markdown table cell split, spaced digits, and dot thousands (as a split rendering);
  - full-width and Arabic-Indic digits;
  - `+`, `~`, `≈`, `±`, parentheses and `/yr`;
  - JSON floats and exponents;
  - a figure inside `column_values`, and inside a link (percent-decoded).
- **Ids.** Full-width and Arabic-Indic digits, spaced and hyphenated groups, a non-breaking space or a zero-width space inside, an underscore prefix, an unquoted `href`, and a bare `hxxp://` look-alike all blocked. An id inside a real link passed.
- **Y08 structural values.** A leading zero, a sign, a space or a decimal string under a structural key blocked. A never-shown workspace id blocked under a structural key, as a float and as a negative number (Z06).
- **Paths.** Backslash, mixed separators, `../`, `%2F`, `%5C`, `file:///Users/` and `~/` all blocked. A drafts file linked to outside the record is exit 3.
- **Credentials.** A JSON web token, an access key id, a long mixed string, a secret pair with emphasis or quotation marks around the key word, and a URL with percent-encoded user info all blocked.
- **Quotes and runs.** Seven words of a quote pass and eight block. A block-held quote copied verbatim blocks. A run with one word changed (near copy), re-punctuated, with two changes far apart, with a word inserted every five words, or with its clauses reordered still blocked.
- **Exit 3.** These all gave exit 3:
  - a UTF-16 or undecodable draft or local list;
  - an empty or non-zip `.docx`, and empty or invalid JSON;
  - a missing settings file, a blank or punctuation-only firm name, a newer settings schema;
  - wrong types in the renderings, workspaces, ids or GitHub account;
  - a bad class name, a whitelist with no phonetic row, a nested-quantifier pattern;
  - `-h`, an index in the home, and a malformed mark (two opening marks, an unclosed block).
- **The allowlist.** It never cleared the firm, an id, a figure, a credential or an exclusion. It fed no set (Y01). The last bracket group was read as keys (Y05). An upper-case `OK:` key cleared nothing. A non-clearable match warned once per finding (Y06).
- **`.docx`.** Text in headers, footers, footnotes, endnotes, text boxes and core properties blocked, and a figure joined across a non-breaking hyphen blocked.
- **Tool categories.** These blocked: a table row, hyphenated or capitalised category words, an acronym category, a Cyrillic letter inside a word, and a heading's proper noun (not counted for the paragraph below it).
- **Interpreters.** Python 3.9.6 and 3.14 gave the same result on every probe.

---

## Fixes for part 1

Step 8, 2026-10-17. Each finding of part 1 was re-run first against the live script (parts 1 and 2): all 27 probes still reproduced, so part 2 had changed none of them. The probes were copied to `$SCR/probes-live/` with `SCRIPT` pointed at the live `leak_lint.py` and the homes under `$SCR/homes-live/`; `$SCR/probes-live/runall.sh` runs them all. The originals are unchanged. Every test below is in `tests/unit/test_leak_lint.py` (classes `ReviewBlockingTest` and `ReviewShouldFixTest`); each was run against the committed script and shipped list before the fix and failed there (F21's hangs), and passes now. The decisions made or changed are `DECISIONS.md` R01 to R28.

### Blocking

| Finding | Outcome | Test | Decision |
|---|---|---|---|
| F01 | fixed: a number after a sign, a dash, a slash, a quote or an abbreviation; a glued currency code (also a cost cue); a hyphen before a magnitude word | `test_F01_X25_a_figure_after_a_sign_a_dash_a_slash_or_a_quote_is_a_number` | R01 |
| F02 | fixed: the id row on every JSON number that is not structural | `test_F02_Y08_a_monday_id_as_a_json_number_outside_a_structural_key_blocks` | R02 |
| F03 | fixed: a snapshot by its schema, quoted or not; a newer or another schema is exit 3; front matter with no schema is internal | `test_F03_X11_G57_a_snapshot_is_read_by_its_schema_quoted_or_not_and_a_newer_one_stops` | R03 |
| F04 | fixed: the exclusions reader is strict (exit 3 naming the line); the allowlist stays lenient | `test_F04_X09_X33_an_exclusions_row_that_does_not_parse_is_exit_3` | R04 |
| F05 | fixed: an HTML-decoded copy of every unit under every rule | `test_F05_X24_X28_html_entities_and_tags_never_break_a_match` | R05 |
| F06 | fixed: Q takes the quoted words and the whole utterance; E unchanged | `test_F06_X24_a_quote_line_with_a_quoted_word_inside_keeps_its_whole_quote` | R06 |
| F07 | fixed: a boundary only on a side with a word character | `test_F07_X03_a_marker_written_straight_onto_a_word_blocks` | R07 |
| F08 | fixed: Word's shown attributes, `people.xml` and external relationship targets read; altChunk, embeddings and nested or HTML parts exit 3 | `test_F08_X35_docx_text_word_shows_is_read_and_parts_it_cannot_read_are_exit_3` | R08 |
| F09 | fixed: a linked folder inside the record is walked; one outside is exit 3 | `test_F09_X35_a_folder_linked_into_drafts_is_walked_or_stops` | R09 |
| F10 | fixed: the widened shapes and the secret-like looser pairs | `test_F10_X15_Y04_credentials_just_outside_the_six_shapes` | R10 |
| F11 | fixed: tokenised rows of two words or more also match as consecutive tokens | `test_F11_X24_X28_an_excluded_or_seller_name_broken_by_any_mark_blocks` | R11 |

### Should fix

| Finding | Outcome | Test | Decision |
|---|---|---|---|
| F12 | fixed: default-ignorable characters dropped, more look-alikes, credentials on the folded line, the slashed copy from the folded line, line separators as breaks | `test_F12_X28_invisible_characters_look_alikes_and_line_separators` | R10, R12 |
| F13 | fixed: a hyphenated literal row also matches its words with the gaps (markers and other marked rows stay literal). The user's answer to R13, option (b), is built by R61 (2026-10-21): four method rows whose spaced form is everyday block only hyphenated; `exit ramp` and `cost of waiting` still block spaced through their own shipped rows, which R61 leaves to the user | `test_F13_X24_X32_a_hyphenated_row_matches_its_words_spaced`; R61's three `test_R13_R61_...` | R13, R61 |
| F14 | fixed: the deletion neighbourhood (a word dropped or added) | `test_F14_X24_a_near_copy_with_a_word_dropped_or_added_blocks` | R14 |
| F15 | fixed: near quotes at the six inner positions, so seven quote words still pass | `test_F15_X24_X36_a_block_held_quote_with_one_word_changed_or_dropped_blocks` | R14 |
| F16 | fixed in `shared/leak-terms.txt` (the review's fix, with a tail so "solution/approach" passes); listed for the user's nod | `test_F16_X03_record_paths_the_shipped_rows_now_cover` | R15 |
| F17 | fixed: a second key with `th` as `t` and `ph` as `p` | `test_F17_X32_a_th_spelling_heard_as_t_is_a_sound_alike` | R16 |
| F18 | fixed: three phrases, the two speaker forms (a letter only before `:`, `)` or `]`), a front matter block with `schema:` anywhere. The user's answer to R17, option (b), is built by R62 (2026-10-21): "internal only", "internal use only" and "not for clients" still block, and an ok row of the strand's allowlist clears them to a caution; speaker labels and front matter stay never cleared | `test_F18_X40_internal_notes_in_their_common_spellings`; R62's three `test_R17_R62_...` | R17, R62 |
| F19 | fixed: an `ok` whose first word says no, not yet or ask clears nothing and warns | `test_F19_X09_an_allowlist_ok_that_says_no_clears_nothing` | R18 |
| F20 | fixed: a near-miss mark is a malformed mark (exit 3 in block mode, the warning in the sets and in `blueprint`) | `test_F20_X09_X38_a_client_safe_mark_written_slightly_wrong_is_exit_3` | R19 |
| F21 | fixed: the parsed pattern checked at every depth (`re._parser`, or `sre_parse` before 3.11) | `test_F21_X33_X42_local_patterns_that_can_run_for_a_very_long_time_are_exit_3` | R20 |
| F22 | fixed: a thousands comma with a space or a break joins a split figure | `test_F22_X25_a_figure_split_at_its_thousands_comma` | R21 |
| F23 | fixed: exit 3, "no draft or handoff file to check"; no `--allow-empty` flag, since no caller needs one | `test_F23_Z07_a_scan_with_nothing_to_check_is_exit_3` | R22 |
| F24 | fixed as the review proposed: anchored role words, `owner` and `lead` dropped, six cues need a name, three cues dropped; listed for the user's nod, since it narrows X06 | `test_F24_X06_paraphrase_cues_in_ordinary_process_text_pass` | R23 |
| F25 | fixed: plurals, the abbreviations, the everyday rows only beside a specific category. The user dropped the tool-category check (A30, the answer to R24), built by R64 (2026-10-21): the check, its plurals and its everyday rows are gone; the abbreviations still end no sentence, for the cost cue and the paraphrase rule | `test_F25_R64_a_full_stop_after_an_abbreviation_ends_no_sentence` (the tool-category test removed) | R24, R64 |
| F26 | fixed: a raw JSON string that is walked skips the id rows | `test_F26_Y08_a_structural_id_inside_a_column_values_string_passes` | R25 |
| F27 | fixed: a decimal tail is skipped and an eight-digit date warns | `test_F27_Z03_Y02_long_numbers_that_are_not_ids` | R26 |

No should-fix finding was kept.

### Notes

| Finding | Outcome | Test or reason |
|---|---|---|
| F28 | no change needed | an empty text holds nothing that can leak; empty `.json` and `.docx` stay exit 3 |
| F29 | fixed | `test_F29_X35_a_utf16_part_with_a_dtd_is_exit_3` (R08) |
| F30 | kept | X19 limits v1 to English; the fixture README may list the forms when a case is next added (it may change only with a case) |
| F31 | fixed, for the user's nod. The user's answer to R27, widened, is built by R63 (2026-10-21): a web address with no scheme whose host ends in `.com` and a slash (`yourcompany.monday.com/boards/<id>`) also hides its ids; other endings and look-alikes such as `hxxp://` stay checked | `test_F31_F32_X34_only_a_real_link_masks_an_id` (R27); R63's three `test_R27_R63_...` |
| F32 | fixed; R63's `.com` address stops at a comma or a pipe too | the same test (R27); R63's three `test_R27_R63_...` |
| F33 | kept | Y08 as decided and nodded; the user may tie `id` to the object's own id |
| F34 | kept | a slash-joined form would block every year pair ("2024/2025"); X34's shape stands |
| F35 | no change needed | a sound-alike by design; the whitelist row clears it (Y09) |
| F36 | no change needed | nod 12 of the API note and X06 as decided |
| F37 | fixed (the day or month part); the Markdown list part kept as X12 decided. Moot since R64 (2026-10-21): the tool-category check is dropped (A30), and the day-or-month rule went with its proper-noun test | none (`test_F37_X12_...` removed by R64) |
| F38 | kept | rare in client text; both are internal-note shapes X40 chose |
| F39 | fixed | `test_F39_X04_settings_read_strictly` (R28) |
| F40 | fixed | `test_F40_X35_header_part_names_in_any_case` (R08) |
| F41 | fixed for the double percent-encoding; the split quote across payload fields is part 2's walker; the `inputs/*.md` reading is X11 as decided | `test_F41_X03_a_double_percent_encoding_is_decoded` (R12) |

### False-positive cost, checked

- The fixture's 250 cases, twins included, grade as the manifest says under both Pythons (`test_leak_grading.py`), and `test_leak_fixture.py` passes (no twin carries a shipped row, the new ones included).
- `terms` over the real `shared/` with both fixture records indexed still exits 0 (`test_L197_...`).
- New costs the user should know of, each in its R entry: the second number of a range now warns (R01); hyphenated method rows block their spaced phrases, clearable (R13); "internal use only" and "not for clients" block, never cleared (R17); an empty scan stops (R22). Narrowings, also for the nod: R23, R24, R26, R27.

### Gate results

All from the plugin repository with `PYTHONDONTWRITEBYTECODE=1`, on this Mac.

| Check | Result |
|---|---|
| `/usr/bin/python3 -m unittest discover -s tests/unit` | Python 3.9.6: 542 tests, OK (509 before, plus 33: 11 blocking, 22 should-fix and notes); the grading harness's 250 cases included |
| the same under `cpython-3.14 .../python3.14` | Python 3.14.6: 542 tests, OK |
| `/usr/bin/python3 tools/lint_plugin.py --root .`, and under 3.14.6 | 0 errors, 1 warning (the personal-name list is not on this machine), 6 not present yet; the `leak` pair compared and in agreement |
| `find <workspace> -name __pycache__` | none |
| live probes F01 to F27 (`$SCR/probes-live/runall.sh`), the lint under 3.9.6 and under 3.14.6 | every line gives its expected result, the same under both. F03's `document-summary/2` line prints `REPRODUCED` because the probe's `expect()` counts only blocks; it gives exit 3, which is what the finding expects. F23 and F26 give exit 3 and exit 0 or 2 (a number warning in the probe's own `Job 12`), as expected |
| sizes | `scripts/leak_lint.py` 3,963 lines; `tests/unit/test_leak_lint.py` 1,675 lines |

Files changed: `plugins/monday-master-builder/scripts/leak_lint.py`, `plugins/monday-master-builder/shared/leak-terms.txt`, `tests/unit/test_leak_lint.py`; in the workspace this section, `DECISIONS.md` (R01 to R28) and `API-leak_lint.md` ("Part 1 review fixes"). `record-map.md`, the fixture, `test_leak_fixture.py`, `test_leak_grading.py` and `test_leak_wall.py` are unchanged. Nothing is committed.
