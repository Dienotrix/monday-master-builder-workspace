# WP4 fixture notes: the leak-trap fixture

Date: 2026-10-17. Internal build file: never client-facing.

Step 4 of `PLAN.md`. It built `tests/fixtures/leak/` and its self-test `tests/unit/test_leak_fixture.py` in the plugin repository, against PLAN section 4, DECISIONS sections 1 to 3 and the X entries that name the fixture, CONTRACT 2.17 and 2.18, and the `Pinned: leak` section of `shared/record-map.md`. Nothing else in either repository was changed, and nothing was committed.

## 1. Layout

All paths are under `monday-master-builder/tests/fixtures/leak/`.

| Path | Holds |
|---|---|
| `manifest.json` | every case, machine-readable (section 2) |
| `README.md` | every case in words, one table row per planted case; the outcome legend; the known limits; what the fixture cannot prove; the closed list of invented names (X18) |
| `.gitattributes` | `* text eol=lf` |
| `home/local/settings.json` | the test `settings/1`: the invented firm `Thymbel Advisory` and three renderings, an invented default build account, two never-shown workspaces and a GitHub archive account (nod 11) |
| `home/local/leak-terms.txt` | the test local list: one colleague above the first class line (class `local`), then `class: firm` with `phonetic: Thymbel` and `whitelist: thimble` |
| `records/wrenfold-joinery/` | client record a, a kitchen joinery: `CLIENT.md`, a brief, a raw transcript, a call summary with a client-safe block, a client document in `inputs/` and its snapshot with a block and a `## Conflicts` row, two strands, strand 001's `exclusions.md` and `allowlist.md` |
| `records/marlbeck-freight/` | client record b, a haulage firm: `CLIENT.md`, a brief, a call summary with an alias table and a contact address, and strand 001's `exclusions.md` (X26: names in the body, a header, initials, an e-mail) |
| `overlays/` | four sets of files laid over record a for one case each: `third-party-excluded`, `allowlist-attempts`, `call-unmarked`, `snapshot-unmarked` |
| `cases/trap/`, `cases/key/`, `cases/rule/` | Markdown drafts, one file per planted case and per twin |
| `cases/payload/` | JSON tool inputs, one per planted case and per twin |
| `cases/blueprint/`, `cases/summary/`, `cases/intake/` | two blueprints, two strand summaries, two new call summaries |
| `docx/<case>/` | the XML parts of each `.docx` case (nod 3); the tests zip them with `zipfile` |

Counts, after the step-4b settlements (section 7): 125 planted cases and 125 twins (250 cases), 290 files. Of the planted cases, 110 block, 3 warn, 1 is a caution and 11 are known limits; 119 twins exit 0 and 6 exit 2 with a named warning. 168 cases run `scan`, 80 `payload` and 2 `blueprint`. The first build had 122 pairs in 284 files. All 24 payload kinds have a sample and a twin; 9 `.docx` cases cover the body, `docProps/core.xml`, `docProps/app.xml`, a header, a footer, footnotes, endnotes, comments and custom properties (X35).

## 2. The manifest format, and why

JSON, `schema: "leak-fixture/1"`. Python reads it with the standard library on both systems, it is the format of WP3's fixture keys, and step 6 grades from it without a parser of its own. Each case object carries:

- `id` (`<pair>-p` planted, `<pair>-t` twin), `role`, `group`, and `twin` on a planted case or `twin_of` on a twin;
- `record` (always `a`), `files` (the fixture files), `overlay` (or null) and `install` (each `from` and record-relative `to`, or a `zip` folder and the `.docx` path it becomes);
- `command`, `args` (after the command; `--record` is added by the runner) and `mode` (`full`, `summary`, `client-safe-block`, `blueprint`, or null for `payload`);
- `verdict`, `exit` and `outcome` (`blocks`, `warns`, `caution`, `limit`, `passes`);
- `expect`: each finding as `rule`, `class` (null where not asserted), `severity`, `where` (`line N` in a text file, the X22 path in a payload, the part in a `.docx`), and `match` or `family`;
- on a planted case, `rules`, `covers` (the category ids of DECISIONS section 3) and `summary`, plus `limit` on a limit case and `unchanged` on R14; on a twin, `why_clean`.

The top-level `home` block gives the run order step 6 follows: a fresh temporary `MMB_HOME` per case; settings and local list copied; both records copied; the case's overlay laid over record a; `index` run from record b and then record a; the case files installed; the command run. The grading rule is written there too: a planted case needs its exit code, its verdict and every `expect` entry; other findings in a planted case are reported, not failed; a twin fails on any block.

The README is generated from the same data, so the manifest and the README cannot drift, and the self-test checks the README's rows against the manifest in both directions (L221).

## 3. Worth the user's nod

Choices taken where the decisions are silent. Each is the safe or the plain reading; none blocks step 5.

1. **One fresh home per case**, with the overlay applied before `index` and the case files installed after it, so a draft or a payload never enters an index entry (X11).
2. **Overlays vary the record per case.** L258's "the same text outside the mark" is read as the same draft against a record whose two marks are removed (R10a, R10b); its twin is the same draft against the record as it is.
3. **Payload field names.** The fourteen standard kinds use the family names as keys (`name`, `description`, `label`); the AI kinds use the shapes recorded in `ai-offerings-findings.md` (`profile.name`, `goal`, `knowledge[0].name`, `steps[0].text`). The walker is generic (X22), so the names change no rule; the connector's own argument names are stage 4b's to confirm.
4. **The twenty trap categories are twenty-three ids**, split as DECISIONS 3.2 splits them (case-varied, possessive and comma-split names; customers as initials and in full).
5. **Limit cases exit 0** and twins exit 0, except six twins that carry an unrelated figure as the decisions' shapes ask (K01, K02, K04, K06, K07, R01), which exit 2 with the warning named.
6. **The sound-alike word and the whitelisted use are one word**, `thimble`, with one whitelist row; R13b's twin holds four everyday uses of it.
7. **Record a holds the everyday words of record b's names** (skipper, silver, lantern, market, fresh, freight), so the twins of T05, T14 and the like pass on this record's own set (X27) whatever the common-word list holds.
8. **R18's allowlist warnings appear only when a row meets a finding.** Its twin, under the same overlay, exits 0. Settled by DECISIONS Y06.
9. **The client-safe block of the call summary holds a `[Q]` line**, so that R04 has a quote inside a block (X24 defines a quote as a marked line). A block written by call-intake would not carry a marker.
10. **The raw transcript is an excerpt** and does not hold the quoted words. In a full record it would, and then R04's seven-word twin would block on the run rule from the transcript.
11. **K23b's supply clause sits in the snapshot's analyst note**, outside the block and not in the client's document, because X36 exempts only document text.
12. **Invented token shapes in R16** (`ghp_`, `AKIA`, `pk_test_`, a JSON web token) are fake, but a host's secret scanning may still flag them on a push. If it does, the user can allow them, or the tests can assemble them at run time.
13. **Two six-word runs remain in common with the answer keys** (section 6): both are the call summary's pinned front-matter fields `provenance: "first-hand"` and `handed_over_by: "none"`, not content. **Answered 2026-10-21 (the user, after a walkthrough):** "L218: accept. The two runs are the record map's pinned field names and values, not content. Record it as a decision and mark L218 met by decision." Recorded as R65 in `DECISIONS.md`.

### Found while building, for steps 5 and 6

These are places where the decisions, read literally, would fail a case the fixture asserts. The fixture keeps the safe expectation. All four are now settled in DECISIONS: ids by Y08 (new pair R21), the allowlist by Y01, the thimble by Y09 (R13b-t line 5), and the bracketed term by Y05.

- **Ids inside a real payload.** A real tool input carries workspace and board ids as digit strings of eight or more. X22 walks every string, so the id row would block every real write. The samples carry no ids. A rule is needed, such as reading a digit-only value under a key named `id`, `*_id` or `*_ids` as an id and not as text.
- **An allowlist row can feed the wall's own set.** X11 puts `allowlist.md` into O, so a row naming another client's name makes it "in this record" and clears the wall, while X10 says a wall hit is never cleared. R18 expects the block. Leaving `allowlist.md` out of O closes it.
- **"the thimble" keys to the firm.** The fused two-word window `thethimble` keys to `0MPL`, because the two `th` sounds collapse across the join, and X32's whitelist does not clear a hit that only contains the whitelisted word. The twins avoid the phrase. Keying each word before fusing, or clearing a window hit that contains a whitelisted occurrence, would fix it.
- **An allowlist row whose term is bracketed** (`- [E] [ok: ...]`): the row parser must read the last bracketed group as the key list.

## 4. What the fixture cannot prove

As PLAN 4.2 says: that the categories of A§:918 and DECISIONS 3.1 are the whole set; that a client's real vocabulary behaves like the invented one; the false-positive rate on real client text, which only stage 4's seed records and the twenty-five keys begin to measure; and anything about a language other than English. Two more, from this build: the twins pass the wall partly because record a holds the same everyday words (nod 7), which a real record may not; and the records are excerpts, so a run or a quote that a full transcript would also hold is not tested (nod 10). The eleven `limit` cases are known gaps, asserted so that a later rule's reach is seen.

## 5. Coverage

Each category and rule case of DECISIONS section 3 against its planted cases (the pair id; each pair is `<id>-p` and `<id>-t`).

| Category | Cases |
|---|---|
| trap:case-varied-names | T01 |
| trap:possessive-names | T02 |
| trap:comma-split-names | T03 |
| trap:identifier-in-header | T04 |
| trap:alias-ordinary-word | T05 |
| trap:name-from-body | T06 |
| trap:customer-acronym | T07 |
| trap:customer-full-name | T08 |
| trap:seller-commercial-terms | T09 |
| trap:split-date | T10 |
| trap:assessment-of-individual | T11 |
| trap:small-talk | T12a, T12b |
| trap:third-party-in-passing | T13a, T13b |
| trap:partner-two-ordinary-words | T14 |
| trap:corrupted-name-in-hypothetical | T15 |
| trap:fused-product-name | T16 |
| trap:vendor-substitution | T17 |
| trap:email-separator-lost | T18 |
| trap:first-names-in-quotation | T19 |
| trap:counterparty-owner-tools | T20 |
| trap:departure-hypothetical | T21 |
| trap:seller-account-structure | T22a, T22b |
| trap:health-remark-absent-person | T23 |
| key:K01 | K01, R01 |
| key:K02 | K02 |
| key:K03 | K03a, K03b |
| key:K04 | K04 |
| key:K05 | K05 |
| key:K06 | K06 |
| key:K07 | K07 |
| key:K08 | T09 |
| key:K09 | K09 |
| key:K10 | K10a, K10b |
| key:K11 | K11, R20 |
| key:K12 | T23, K12 |
| key:K13 | T11, K13b |
| key:K14 | K14 |
| key:K15 | K15a, K15c, R04, R19b |
| key:K16 | K16 |
| key:K17 | K17 |
| key:K18 | K18 |
| key:K19 | K19, R05, R06 |
| key:K20 | K20, R07 |
| key:K21 | K21a, K21b |
| key:K22 | T13a, T13b |
| key:K23 | K23a, K23b |
| key:K24 | T04 |
| key:K25 | T12a, T12b |
| key:K26 | K26a, K26b |
| key:K27 | K27a, K27b |
| key:K28 | K28 |
| key:K29 | K29a, K29b |
| key:K30 | T15, K30, R13b |
| key:K31 | K31a, K31b |
| key:K32 | R14 |
| key:K33 | R15a, R15b |
| key:K34 | R03b |
| key:K35 | K35 |
| key:K36 | K36 |
| rule:figures-five-formats | R01 |
| rule:figures-split-renderings | R02 |
| rule:copied-run-placements | R03a, R03b |
| rule:quote-eight-words | R04 |
| rule:markers-nine | R05 |
| rule:internal-ids | R06 |
| rule:record-paths | R07 |
| rule:html-comments | R08 |
| rule:monday-id-link | T22b, R09 |
| rule:exempt-blocks-and-glossary | R10a, R10b, R10c |
| rule:common-word-run | R11 |
| rule:tool-categories-three-two | R12 |
| rule:firm-renderings-phonetic-whitelist | R13a, R13b |
| rule:flag-do-not-remove | K03b, R14 |
| rule:caution | R15a, R15b |
| rule:credentials | R16 |
| rule:internal-notes | R17 |
| rule:exclusion-per-family | the fourteen standard kinds, P-automation, P-item_batch, P-doc, P-generic |
| rule:allowlist-limits | R18 |
| rule:payload-per-kind | P-workspace, P-folder, P-board, P-group, P-column, P-view, P-form, P-subitems, P-doc, P-dashboard, P-widget, P-automation, P-portfolio, P-project, P-workflow, P-agent, P-ai_column, P-vibe_app, P-sequence, P-webhook, P-item_batch, P-publication, P-activation, P-generic |
| rule:docx-parts | D01 to D09 |
| rule:summary-two-rules | R19, R19b |
| rule:client-safe-block-at-intake | R20 |
| rule:wall-records | K17 |
| rule:structural-ids (Y08) | R21 |
| rule:payload-keys-and-numbers (X22) | R22 |

How the BP:158 cases of PLAN 4.1 land: the copied run in three placements is R03a (internal, blocks), R03b (conflict row, blocks) and R03b's twin (client document, passes); the three exempt blocks are R10a, R10b and R10c, each twin passing; the common-word run is R11's twin; two tool categories are R12's twin; the sound-alike word is R13b's twin; the allowlist row that clears a method term is R15a.

## 6. Commands and results

All from the plugin repository, `monday-master-builder/`, on this Mac.

| Command | Result |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 -m unittest tests/unit/test_leak_fixture.py` | Python 3.9.6: 16 tests, OK |
| the same under `~/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14` | Python 3.14.6: 16 tests, OK |
| `PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 -m unittest discover -s tests/unit` | 346 tests (330 before, plus 16), OK |
| the same under Python 3.14.6 | 346 tests, OK |
| `/usr/bin/python3 tools/lint_plugin.py --root .`, and under 3.14.6 | 0 errors, 1 warning (the personal-name list is not on this machine) under both |
| `find . -name __pycache__` | none |

Checks made outside the repository, in the session's scratch folder, and not kept:

- A probe compared every six-word run of the fixture (README aside) with the 78 files under `rebuild-workspace/fixtures/`. Of the first build's shared runs, three phrases were reworded and the cost total was changed. The two that remain are the pinned front-matter fields of nod 13.
- A sanity pass applied rough versions of the decided rules to every twin and limit case: no six-word run from record a outside the cases that copy one on purpose, no word or run of record b's harvested names absent from record a, no phonetic match of record b's names or of the firm, no cue phrase beside a person, and no number of ten or more in a twin expected to exit 0, apart from dates, a time and ids inside links, which X25 and X34 exempt. It found the `the thimble` case of section 3 and the `.example` label that record a now also holds.
- The self-test's own checks were probed: an unlisted capitalised name is reported, and a shipped literal row is matched only on its word boundaries.

## 7. The trace check's settlements and the re-run gates

The step-4b trace check (`fixture-check.md`) raised 14 findings: 4 unclear and 10 notes. All are settled in its Settlements section. Seven changed the fixture (F06, F08, F09, F10, F11, F12 and F13's wording) and seven were kept with a reason. The decision-level points became DECISIONS Y01 to Y09, under "Added by the fixture check (step 4b), 2026-10-17". Y01 to Y06 cover F01 to F05, Y07 covers F10, and Y08 and Y09 settle the author's own concerns. Y02, Y08 and Y09 carry a line for the user's nod.

What changed in the fixture:

- T03-p line 4: a comma-split colleague name.
- R17-p lines 7 and 8: the second front-matter shape.
- New pairs: R19b (the quote rule in summary mode), R21 (structural ids, Y08) and R22 (an object key and a bare number).
- R13b-t line 5: `The thimble`, under Y09.
- Wording in the README.
- Two figures. The saw budget 62,000 is now 73,000 and the twins' 8,400 is now 8,700, in every rendering and file. A search under `rebuild-workspace/fixtures/` finds neither new figure in any rendering, and a search of the fixture finds neither old one.

`test_leak_fixture.py` gained the two new rule-case ids, a copy of Y08's structural keys (so the twin check reads payloads as the lint will) and path handling for an object key and a JSON number. No `Pinned: leak` token was added, and `record-map.md` and the lint-clean fixture are untouched.

| Command (from `monday-master-builder/`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `/usr/bin/python3 -m unittest tests/unit/test_leak_fixture.py` | Python 3.9.6: 16 tests, OK |
| the same under `cpython-3.14-macos-aarch64-none/bin/python3.14` | Python 3.14.6: 16 tests, OK |
| `/usr/bin/python3 -m unittest discover -s tests/unit` | 346 tests, OK |
| the same under Python 3.14.6 | 346 tests, OK |
| `tools/lint_plugin.py --root .` under both | 0 errors, 1 warning (the personal-name list is not on this machine) |
| `find` for `__pycache__` in the repository and the scratch folder | none |
| byte check of all 290 fixture files | UTF-8, LF only, no byte-order mark |
| six-word probe against `rebuild-workspace/fixtures/` | the same two pinned front-matter runs as before (nod 13), nothing else |

## 8. Changed by the review fixes, part 2: R49 (G18), 2026-10-21

DECISIONS R49 has `blueprint` stop with exit 3 unless level-2 headings numbered 1 to 15 are each found once and in order, and no other level-1 or level-2 heading sits among them before section 16. A real blueprint always holds the sixteen sections (A§6, D19), so a blueprint with sections 1 to 3 only is now exit 3, and the two blueprint cases would have stopped there.

- `cases/blueprint/R10c-p.md` and `R10c-t.md` gain the empty headings `## 4. Structure mapping` to `## 16. Internal`, appended after section 3. Sections 1 to 3, their text and every line number are unchanged, so R10c-p's run still sits at line 12 in section 3 and R10c-t's in the glossary of section 2. The manifest and the README need no change.
- The headings use no capitalised word but the first of each, so the invented-names check (X18) is unaffected, and no shipped term.
- `test_leak_fixture.py` and `test_leak_grading.py` pass unchanged with the new files.

## 9. Changed by the follow-up, run 5 (step 8), 2026-10-21

### R61 (R13 (b)): "cost of waiting" hyphenated, made by the main session at the user's word

With the shipped spaced row `cost of waiting` removed from `shared/leak-terms.txt` (the user's approval is in `shared-edits.md`), the spaced phrase no longer blocks, and the cases that planted it spaced would have lost their expected `method` finding. The main session wrote it hyphenated, which still blocks through the row `cost-of-waiting`:

- `cases/key/K19-p.md` line 1: "The cost-of-waiting is shown on the board."
- `cases/trap/T09-p.md` line 1: "Our day rate of 1,450 means the cost-of-waiting grows each week."
- `cases/payload/P-view-p.json` `$.description`: "Shows the cost-of-waiting".
- `cases/payload/P-workflow-p.json` `$.description`: "Runs the cost-of-waiting check".
- `cases/payload/P-generic-p.json` `$.prompt`: "Explain the cost-of-waiting".
- `manifest.json`: the two `match` entries that read `cost of waiting` now read `cost-of-waiting`.
- `README.md`: the rows of T09-p, K19-p, P-view-p, P-workflow-p and P-generic-p name the hyphenated words.

No twin changed, every case keeps its exit code and verdict, and the grading harness's 250 cases kept their outcomes.

### A30 (R64): the tool-category case removed, as a patch for the main session

The lint runs no tool-category check (A30, R64), so the fixture's case for it goes. The R64 run did not edit the fixture; it wrote the change as `r64-fixture.patch` in the session's scratch folder (`wp4-run5/`), a unified diff that `git apply` takes from the plugin repository's root, for the main session to apply at the user's word:

- `cases/rule/R12-p.md` (the planted sentence with three tool categories) and `cases/rule/R12-t.md` (its twin with two) are deleted.
- `manifest.json`: the entries of R12-p and R12-t are removed, and `tool-categories-three-two` leaves `categories.rule`. The file is otherwise byte-equal, written back with the same two-space indent.
- `README.md`: R12-p's row is removed; the counts read 124 planted cases, 124 twins and 288 files; the heading of the rule cases reads "(27)". The case ids are not renumbered, so the rule cases go from R11 to R13a.
- T20-p's summary and T20-t's `why_clean` still mention tool categories as plain text. No rule reads them, and they are left as they are.

`test_leak_fixture.py` (the rule categories, 15 pinned rules, no skip of the counted classes) and `test_leak_grading.py` (248 cases: 124 planted, 124 twins; 109 blocks, 3 warns, 1 caution, 11 limits, 124 passes; 166 `scan`, 80 `payload`, 2 `blueprint`) are changed in the repository and pass once the patch is applied.

| Command (in a scratch copy of the plugin repository with the patch applied, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `/usr/bin/python3 -m unittest discover -s tests/unit` | Python 3.9.6: 634 tests, OK |
| the four leak files under `cpython-3.14.6-macos-aarch64-none/bin/python3.14` | Python 3.14.6: 283 tests, OK (`test_leak_fixture.py` 16, `test_leak_grading.py` 3) |
| `git apply` of the patch on a fresh copy of `tests/fixtures/leak/` | applies cleanly; the result equals the edited copy file for file |
| `git apply --check` in the plugin repository | clean |
