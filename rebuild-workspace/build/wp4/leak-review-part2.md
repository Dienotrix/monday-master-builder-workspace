# Leak lint: the adversarial review, part 2 (WP4 step 7)

Date: 2026-10-17. Internal build file: never client-facing.

Frozen script reviewed: `frozen2/plugins/monday-master-builder/scripts/leak_lint.py`, sha256 `7544bdb6d5c579bb…` (3,439 lines), as part 2 left it. Part 2's reach is the cross-client wall and its index, the payload walker over every kind, `blueprint`, `wall` and `terms`. The single-text rules are part 1's (`leak-review.md`, F01 to F41) and are not repeated here; where a part 1 finding also reaches the wall, this file says so in one line.

The specification read: DECISIONS U1, X01, X02, X08, X11, X14, X21, X22, X25 to X32, X37, X42, X45, X46, Y01, Y08, Y09 and Z10 to Z19; `API-leak_lint.md` Part 2 (P1 to P9); ARCHITECTURE 9.6 (lines 912 to 922) and 7.1 (the home and the archive).

## How to re-run the probes

`$SCR = <scratchpad>/wp4-review`

- `$SCR/probes2/harness.py` is part 1's harness with `SCRIPT` pointed at `frozen2/` and its homes under `probes2/homes/`. `$SCR/probes2/harness2.py` adds a second record and runs `index`, `wall`, `terms` and `blueprint`.
- The home holds record a, `brindle-tiles` (part 1's record, where every check runs), and record b, `fernhollow-supply`, the other client. Record b's research brief names, each in a capitalised body line: the client Fernhollow Supply, its people Odalys Brekke and Tavish Quorne, its customer Østby Freight, its partner Blue Harbour, its product Tallowmere, its carrier Pell-Ardent Logistics, the fuel cost 412,870 beside a cost word, and the address ops.desk@fernhollowsupply.example. Its strand exclusions hold the term "night shift overtime rebate scheme" and the figure 58,315. Some probes add a line to it. Every name and figure is invented.
- Run a probe: `cd $SCR/probes2 && PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3 G01.py`. Add `PROBE_PY=<home>/.local/share/uv/python/cpython-3.14-macos-aarch64-none/bin/python3.14` to run the lint under 3.14. `REPRODUCED` means the finding stands; `ok` means the line behaves as expected (the controls, and the case once fixed).
- G01 runs a copy of the frozen plugin under `probes2/plugin-copy/`, so the frozen copy is never changed. `Z13.py` and `Z13-cli.py` are the measurement of the Z13 section; `Z13.out` holds the run. `probes2/explore/` holds the exploration scripts.
- Every probe gave the same result under 3.9.6 and 3.14, except G08, which is about that difference.

## Counts

| Rank | Findings |
|---|---|
| blocking | 10: G01 to G10 |
| should fix | 11: G11 to G21 |
| note | 8: G22 to G29 |

The most serious finding is G01. The harvest's stop list is read fresh from the plugin's `shared/` files every time `index` runs (Z12). A client name that has leaked into `shared/` therefore removes itself from that client's entry the next time the client is indexed. After that, `terms` over `shared/` passes the leak at release, and every other record's wall loses the name.

---

## Blocking

### G01. A name that has leaked into `shared/` drops out of its own client's entry, and `terms` then passes it

- **Function.** `wall_stop` (line 2574), `kept` (line 2592), through `build_entry` and `cmd_terms`.
- **Input.** Record b is indexed while `shared/` is clean. Then `shared/monday-gotchas.md` gains the line `- Example: Odalys Brekke asked for Tallowmere sync on the depot board.` (in the plugin copy). Record b's next intake runs `index`.
- **Probe.** `G01.py`.
- **Actual.** Before b's re-index, `terms` over `shared/` blocks (exit 1). After it, `terms` over `shared/` exits 0. Record a's wall now passes `Open Tallowmere today.` and `Ask Odalys Brekke.` (exit 0). Each word is now a `shared/` word, so the single word is dropped, and so is the two-word name, because every word of it is in the stop list.
- **Expected.** `terms` blocks the leak (exit 1), and record b's entry still holds its names.
- **Decision.** X31 and BP:114: `terms` "proves nothing from any client input is in" `shared/`. U1: the entry holds the record's names. Z12's reason ("a word the plugin ships is not client input") assumes `shared/` is clean, which is the very thing `terms` is there to prove.
- **Fix.** Do not derive the stop list from the live `shared/` folder. Embed it as a pinned region of the script (as the common words are), regenerate it only at release after `terms` has passed against the previous list, and have `tools/lint_plugin.py` compare it. A word is then added to the stop list only after a review that saw it.

### G02. Letters with no decomposition (ø, æ, ł, đ, ð, þ, œ) meet neither their plain spelling nor the key

- **Function.** `fold` (line 386), X28 step 4: NFD drops combining marks, but `ø`, `æ`, `ł`, `đ`, `ð`, `þ` and `œ` are base letters with no decomposition. `letters` (line 640) then drops them from the phonetic key, so a first-letter `Ø` changes the key too.
- **Input.** Record b writes `Østby Freight`, `Łukasz Dærvel` and `Đorin Sæther`. A text writes `Ask Ostby about the loads.`, `Oestby`, `Lukasz Daervel`, `Lukasz Darvel`, `Dorin Saether`, `Dorin Sather`. And the other way round: record b writes `Ostby`, the text writes `Østby`.
- **Probe.** `G02.py`.
- **Actual.** Exit 0 for every one, in both directions. `Østby` written as in the record blocks, and `O` with a combining stroke (U+0338) blocks.
- **Expected.** A `wall` block, exit 1. People type these names without the special letter as often as with it.
- **Decision.** X28 step 4 (diacritics folded on both sides of the hash) and PLAN §3 ("diacritics").
- **Fix.** After NFD, map the undecomposed Latin letters through a pinned table: `ø`→`o`, `æ`→`ae`, `œ`→`oe`, `ł`→`l`, `đ` and `ð`→`d`, `þ`→`th`, `ħ`→`h`, `ŧ`→`t`, `ı`→`i`, `ŀ`→`l`. For `æ` and `œ`, also hash the one-letter reading (`a`, `o`). Since `fold` serves every rule, the firm and exclusion rules gain the same fix.

### G03. A name broken inside the word by a line-end hyphen or a Markdown mark

- **Function.** `wall_candidates` (line 2482) with `FUSE_GAP` (line 2448). It fuses only across `[-._@/&+]{1,3}`, so `-` followed by a line break, or `**`, `*`, `~~` or a backtick, leaves two tokens that never fuse.
- **Input.** `Open the Tallow-\nmere app today.`; `Ask Fern-\nhollow about the depots.`; `Fern- \n hollow`; `Open Tallow**mere** today.`, and the same with `*`, `~~` and a backtick. A `doc` payload whose `markdown` holds `Tallow-\nmere`.
- **Probe.** `G03.py`.
- **Actual.** Exit 0 for every one. The phonetic test does not reach them either: the two halves key separately and are under seven letters each.
- **Expected.** A `wall` block. Line-end hyphenation is the same word, and the Markdown forms render as the name.
- **Decision.** X27 type 3 (tokens joined with no space are fused); PLAN §3 names "hyphenation" for this review. X24 makes the Markdown marks separators, which is right for the word rules but means the wall must fuse across them.
- **Fix.** Add a hyphen and a line break with optional spaces around it, `-[ \t]*\n[ \t]*`, and the runs `[*_~`]+` to the fuse gaps. On the hyphen form, test the fused word only, so a real compound broken at a line end still meets its spaced twin.

### G04. A partner name of two ordinary words is never published when `shared/` uses both words

- **Function.** `kept` (line 2598): a candidate of two or more words is dropped when every word is in the stop list. Z12 widened that list to about 3,600 words, every word of the plugin's `shared/` files.
- **Input.** Record b: `Their marketing partner is Green Field.` and `Their rota tool comes from Clear Path.` A text: `We use Green Field for coastal runs.`; `The rota sits in Clear Path.`
- **Probe.** `G04.py`. It also counts, among the 2,970 two-word names that can be built from 55 words firms use in names (`blue`, `north`, `clear`, `field`, `gate`, `path`, `point`, `works` and so on), how many the harvest drops this way.
- **Actual.** Exit 0 for both. 462 of the 2,970 names (16 percent) are never published. 22 of the 55 words are `shared/` words. The control, `Blue Harbour`, blocks, because `harbour` is not a `shared/` word.
- **Expected.** A `wall` block. A partner name that reads as two ordinary words is one of A§:918's trap categories.
- **Decision.** U1 (the client's partners and products as the record names them), A§:918, X26 step 2 (a capitalised run is a candidate).
- **Fix.** Drop a multi-word candidate only when the run as a phrase appears in the plugin vocabulary (headings such as "Discovery Brief"), or when every word is in X26's own small stop list (days, months, product words, titles), never because each word on its own is a `shared/` word. Keep Z12's word-level filter for single words only. Re-run L197 to confirm that `shared/` still passes.

### G05. Another record's exclusion term of five words or more never meets the wall

- **Function.** `build_entry` (line 2700) hashes each exclusion term whole, spaced and fused. `wall_candidates` cuts spaced runs and fused forms of at most four tokens.
- **Input.** Record b's exclusions: `night shift overtime rebate scheme` (term) and `Harrow Lane yard expansion plan` (name). A text: `We run the night shift overtime rebate scheme too.`; the same hyphenated; `The Harrow Lane yard expansion plan starts soon.`
- **Probe.** `G05.py`.
- **Actual.** Exit 0 for all three. The four-word control `the depot lease buyback` blocks.
- **Expected.** A `wall` block of class `term` or `name`.
- **Decision.** U1 and X26 (every term row of every strand's `exclusions.md`); X02 (the `terms` list).
- **Fix.** In `build_entry`, also hash every window of two to four words of a longer term, and do not publish a window whose words are all common or stop words. Or let the cutter make longer runs, up to the longest term length the index declares. The first keeps `wall/1`'s cut unchanged.

### G06. A JSON string literal, monday's value shape for a text column, is not walked

- **Function.** `payload_units` (line 3153): a string is walked as JSON only when it starts with `{` or `[`. A value such as `"\"Ask \\u00d8stby about the loads\""`, which is what `change_column_value` takes for a text column and what Python's default `json.dumps` writes, is checked only as raw text, with its `\uXXXX` escapes intact.
- **Input.** `{"board_id": 41873925, "column_id": "text", "value": "\"Ask \\u00d8stby about the loads\""}`; `{"value": "\"T\\u00e4llowmere desk\""}`; a `column_values` object string with a zero-width space before its `{`.
- **Probe.** `G06.py`.
- **Actual.** Exit 0 for all three. The plain string and the object-shaped `column_values` both block, and so does JSON nested twice.
- **Expected.** A `wall` block at `$.value<json>`.
- **Decision.** X22 (a string that parses as JSON is also walked) and L134 (no field the walker does not visit).
- **Fix.** Try `json.loads` on every string whose stripped form starts with `{`, `[` or `"`, with format characters dropped first. When the result is a string, check it as its own unit at `<path><json>`. When it is an object or a list, walk it as now.

### G07. Two records with one slug: an archived client loses its wall

- **Function.** `home_folders` (line 2780) skips any folder named as this record. `build_wall` (line 2893) skips the entry keyed by this record's name. `cmd_index` (line 3311) replaces the entry under that key. `record.py init` checks only `clients/<slug>`, not `archive/<slug>`.
- **Input.** An archived client at `archive/brindle-tiles` (its own names, indexed). A new, different client created at `clients/brindle-tiles`, the same slug with a legal suffix dropped. A third record, `clients/corbel-hire`.
- **Probe.** `G07.py`.
- **Actual.** From the new record, `Open Tallowmere today.` exits 0, because the archived client's entry is skipped as its own. After the new record runs `index`, the third record also passes `Tallowmere` and `Odalys Brekke` (exit 0): the archived client's entry has been overwritten.
- **Expected.** Both block. X29: "no entry is ever removed: an entry whose record no longer exists stays and keeps that client walled". L178.
- **Decision.** X21, X29, X30 and Z18 item 4. Z18 item 4 reads "a folder with this record's own name is this record", which holds only while slugs are unique across `clients/` and `archive/`.
- **Fix.** In the lint, exit 3 when a folder of this record's name exists under the other root (`archive/` for a record in `clients/`, and the other way round), and when `index` would replace an entry whose `CLIENT.md` name differs. Owed to WP2: `record.py init` refuses a slug that exists under `archive/`. Recording the client name's digest in the entry would let `index` tell the two apart.

### G08. A record folder that cannot be searched: exit 0 under 3.14, and the other slug printed under 3.9

- **Function.** `home_folders` (line 2782), `(entry / "CLIENT.md").is_file()`. Python 3.9's pathlib raises `PermissionError`, and the generic handler prints its message. Python 3.14's returns False.
- **Input.** Record b present and never indexed, with its folder at mode 000 (no search permission). Text `Open Tallowmere today.`, and a payload `{"name": "Tallowmere loads"}`.
- **Probe.** `G08.py`. The lines labelled 3.9 and 3.14 each run under the interpreter they name.
- **Actual.** Under 3.14: exit 0 for both the text and the payload. The folder counts as a slug only, and the coverage check never runs. Under 3.9: exit 3, but `error.problem` holds the full path `…/clients/fernhollow-supply/CLIENT.md`.
- **Expected.** Exit 3 on both interpreters, naming no other folder.
- **Decision.** X30 (fail closed; the error names no folder, because the slug would reach this session), A24 (identical behaviour on both systems), L205.
- **Fix.** Use `os.stat` on `entry / "CLIENT.md"` in a `try`. Treat `FileNotFoundError` and `NotADirectoryError` as "no record", and treat any other `OSError` as `cannot("<home>/clients/", "entries", "a folder under the home cannot be read, so the wall cannot tell whether it is a client record", ...)` with no folder name. Do the same for `entry.is_dir()`.

### G09. The frozen blueprint copy makes the blueprint's own words "this record's", so the build-guard check is blind

- **Function.** `kind_of` (line 1418) and `build_wall` (line 2921). Every `versions/*/blueprint-r*.md` is an O source. Z15 leaves out only the file being checked, `solution/blueprint.md`, and not its byte-equal frozen copy.
- **Input.** `solution/blueprint.md` whose section 4 reads `Jobs board, with a Tallowmere sync column for depot loads.`, then `versions/v0.1/blueprint-r1.md` with the same bytes, as `record.py freeze` writes it at approval.
- **Probe.** `G09.py`.
- **Actual.** The blueprint check blocks before the freeze (exit 1) and exits 0 after it. The payload of the planned name passes in both cases; that is X11 as decided, since the blueprint is O for payloads.
- **Expected.** The blueprint check at the build guard (P5) blocks. Its use is to catch what the index learned between drafting and building, for example another record indexed after the draft check, and after the freeze it can never block on the wall.
- **Decision.** Z15 ("a checked record file never makes its own words this record's"), X45 and L189, P5's build-guard check.
- **Fix.** For `blueprint`, leave out of O every blueprint-kind file of the same strand (`solution/blueprint.md` and its `versions/*/blueprint-r*.md`), not only the checked path. Better still for payloads: count a blueprint's client-facing lines as O only when the latest `blueprint` run on those bytes was clean. The session can record that run's `inputs` hash, as P5 already asks.

### G10. `terms` skips a linked folder in silence

- **Function.** `cmd_terms` (line 3335): `os.walk` without `followlinks` lists a linked folder in `dirs` and never descends into it.
- **Input.** A folder to check that holds `notes.md` and a link `examples -> ../elsewhere`, where `elsewhere/example.md` reads `Example: open Tallowmere for the depot loads.`
- **Probe.** `G10.py`.
- **Actual.** Exit 0. The control, the same file copied in as a plain file, blocks.
- **Expected.** Exit 3 ("an unread file proves nothing"), or the linked folder read.
- **Decision.** X31: "It skips only `.git/` and `__pycache__/` folders and the system files ...; any other file it cannot read is exit 3". This is part 1's F09 in the `terms` walker; a release bundle follows links.
- **Fix.** Walk with `followlinks=True` and a guard on resolved folders already seen, or refuse a linked folder with exit 3 naming it. Do the same in `record_files` for the index's harvest.

---

## Should fix

### G11. A one-word name written as two words

- **Function.** `wall_candidates` (X27 type 3 fuses only non-space joins) and `Wall.hits` (line 2855): a checked run is keyed only in its spaced form, while the index holds the single word's key.
- **Input.** `Open Tallow Mere today.`; `Fern Hollow runs depots.`
- **Probe.** `G11.py`.
- **Actual.** Exit 0. `Fern Hollow Supply` blocks only because `Supply` is published on its own (see G16).
- **Expected.** A block. Speech-to-text and hand typing split compound names this way, and A§:918's corrupted-name trap covers it.
- **Decision.** X27 types 3 and 4; Z13 item 3 covers the other direction only (a fused spelling of a spaced name).
- **Fix.** Keep X27's rule that spaces are not fused for the literal hash, so "on track" never becomes "Ontrack". On the checked side, also test the end-to-end key of each run of two or three words against `phonetic`. This catches the split spelling through the single word's key, where Z13 item 1 has published it.

### G12. Plural, plural-possessive and apostrophe shapes

- **Function.** `tokenise`, `POSSESSIVE` (line 314), `TOKEN` (line 313): only a trailing `'s` or `’s` is dropped, and only `'` and `’` join a word.
- **Input.** `We use Blue Harbours for runs.`; `The Fernhollows run depots.`; `The Fernhollows' depots.`; record b's `O'Rourke Lifts` written as `O‘Rourke` (U+2018), `OʼRourke` (U+02BC), `O´Rourke` (U+00B4), ``O`Rourke`` and `O Rourke`, each alone.
- **Probe.** `G12.py`.
- **Actual.** Exit 0 for all of them. `Kestle Fresh Food` blocks only by its first word.
- **Expected.** A block. PLAN §3 names "plural and singular" and possessives, and the apostrophe shapes are what keyboards and word processors produce.
- **Decision.** X28 step 5, PLAN §3.
- **Fix.** On the checked side, also test each token with a trailing `s`, `es` or `s'` removed. Fold U+2018, U+02BC, U+00B4, U+0060 and U+FF07 to `'` inside a word before tokenising. A one-letter token followed by an apostrophe shape and a capitalised word fuses (`o rourke` to `orourke`).

### G13. The coverage check proves an entry exists, not that it is current

- **Function.** `build_wall` (line 2884): any entry satisfies the coverage check. P5's index moments (init, each saved call, document or email, and before archive) leave out edits to `exclusions.md`, `research/`, `CLIENT.md` and the strand files.
- **Input.** After record b was indexed, its `exclusions.md` gains `Quarrow Point depot` and a new call names `Ysolde Marrick`. No `index` run follows.
- **Probe.** `G13.py`.
- **Actual.** Exit 0 for `Ask about the Quarrow Point depot.` and `Ysolde Marrick will call.`. After `index` from b, the name blocks.
- **Expected.** Exit 3 ("an entry older than its record"), or the callers re-index on every write of a D source.
- **Decision.** X30 (fail closed while the wall cannot see), X02 and P5 (the moments). An exclusion added during solution design never reaches the wall until the next intake.
- **Fix.** In `build_wall`, compare each other entry's `updated` with the newest modification time of the files X11 reads in that folder. This takes `os.stat` only, and opens no file, as X30 requires. Exit 3 naming no folder when the entry is older. Add "after every edit of `exclusions.md`, `research/` or strand Markdown" to P5's moments (WP8, WP12).

### G14. An emptied or half-restored entry passes the reader

- **Function.** `read_index` (line 2744) checks shapes, not content.
- **Input.** Record b's entry with all four lists set to `[]`.
- **Probe.** `G14.py`.
- **Actual.** Exit 0 for `Open Tallowmere today.`. Only the slug still blocks.
- **Expected.** Exit 3. `index` always publishes at least the `CLIENT.md` name and slug (X26 step 1), so an entry with an empty `names` list cannot be one it wrote.
- **Decision.** Z18 item 3 (malformed is exit 3) and X26 step 1.
- **Fix.** Treat an entry with an empty `names` list as malformed. A cheap second check: the entry must hold `digest("n:", <its folder name spaced>)`, which the reader can compute from the folder name alone.

### G15. The record is checked against whatever home `MMB_HOME` names

- **Function.** `Run.locate` (line 692) and `build_wall`: nothing checks that the record lies under `<home>/clients/` or `<home>/archive/`.
- **Input.** Records a and b indexed in one home. Record a checked with `MMB_HOME` set to another home that holds no records: a hook with a different environment, a moved home, or a record copied out.
- **Probe.** `G15.py`.
- **Actual.** Exit 0 for the text and the payload.
- **Expected.** Exit 3: the wall cannot see this record's neighbours.
- **Decision.** X30 and BP:158.32 (fail closed); A§5.3 (records live at `<home>/clients/<slug>/` or `<home>/archive/<slug>/`).
- **Fix.** In every command that runs the wall, exit 3 unless the record's resolved parent is `<home>/clients` or `<home>/archive`.

### G16. Ordinary words published as one-word names block other records, and nothing clears them

- **Function.** `harvest` and `kept` (X26 step 5, Z16 item 5): a capitalised single word that is not among the 1,098 common words or the `shared/` words is published.
- **Input.** Record b's brief publishes `supply`, `freight`, `pallets`, `logistics`, `harbour` and `thursdays` (the stop list holds `thursday`, not the plural). Across the three invented records of the measurement, the single names include `analyst`, `collect`, `extracts`, `holdings`, `market`, `rework`, `laminate`, `skipper` and `silver`. Record a's draft: `Supply notes for the depot.` / `Pallets arrive on Thursdays and the freight van collects them.` / `Logistics are handled by the yard team, and the Harbour Road site stores the spare grout.`, with allowlist rows for `Freight` and `Supply`.
- **Probe.** `G16.py`.
- **Actual.** Exit 1, with six `wall` blocks on ordinary words; the allowlist rows only warn (X10). Once any record file holds the six words, the draft passes. That is the only way out, and it teaches the session to launder (G17).
- **Expected.** Ordinary words do not block, or the user has a way to clear them that does not open the wall to real names.
- **Decision.** PLAN nod 6 accepts a rare word blocking; Z16 item 5 is listed for the user's nod. This measures the cost: it is ordinary vocabulary, not rare words.
- **Fix.** Publish a single word only when it is never seen in lower case in the record's own D text (a real name is capitalised every time), and add plural and inflected forms of the stop words. Show the user the single words an entry will publish at `index` time.

### G17. Any file the session writes into the record makes a name "this record's"

- **Function.** `Own` and `build_wall` (line 2921): O is every file X11 reads but the allowlist, and most of them (`STRAND.md`, `solution/*.md`, `research/**`, `log.md`, `meetings.md`) are written by the session.
- **Input.** A payload `{"name": "Tallowmere sync", "description": "Depot loads"}`, then one line in `solution/build-notes.md` (`Mirror the Tallowmere sync column.`) or in `log.md`.
- **Probe.** `G17.py`.
- **Actual.** Exit 1 alone; exit 0 after either line.
- **Expected.** The block stays. A mix-up of two clients is exactly what writes such a line.
- **Decision.** X27 ("and not this client's record") as decided. This is the price of that reading, and the user should see it.
- **Fix.** For the own test, count only the client-originated sources (`calls/`, `inputs/`, `CLIENT.md`), or require a name to be in one of them as well as in a session-written file. A session-written file can still feed D and F.

### G18. A blueprint section whose heading is not read as 1 to 15 goes unchecked

- **Function.** `blueprint_client_lines` (line 1347) and `numbered_section` (line 1254).
- **Input.** `## 1. Purpose` as the first section, then a section headed `## 4) Boards`, `## 4: Boards`, `## **4. Boards**`, `## Section 4: Boards` or `## Four. Boards`, holding `Jobs board, with a Tallowmere sync column. Fuel budget 412,870.`
- **Probe.** `G18.py`.
- **Actual.** Exit 0 for the five shapes; `## 4. Boards` and `## 4.Boards` block. The one good heading keeps the file from exit 3.
- **Expected.** The section is checked, or the run stops.
- **Decision.** X09 (pins `## 1`, `## 1.`, `## 1 Title`) and Z19. A drift in the template or the session's heading style silently turns client-facing text internal.
- **Fix.** Exit 3, "cannot find sections 1 to 15", unless headings numbered 1 to 15 are each found once and in order. Also accept `)` and `:` after the number.

### G19. Nothing spans two payload fields

- **Function.** `payload_units` and `check_unit`: every string is its own unit.
- **Input.** Part 1's internal run split five and five over `name` and `description`; a client quote split four and four over two workflow `steps[].text`; record b's partner `Blue Field` written as two column titles.
- **Probe.** `G19.py`.
- **Actual.** Exit 0 for all three. Each control in one field blocks.
- **Expected.** A block for the run and the quote. F41 left this to part 2.
- **Decision.** A§:916 (runs and quotes in any payload), X22.
- **Fix.** Also check one joined text per payload: every string in walk order, joined by single line breaks, under the copied-run, quote and wall rules only. Report a hit there at the first field it touches, and dedupe it against the per-field hits.

### G20. A duplicate key in the payload file: the first value is never checked

- **Function.** `json_value` (line 762): `json.loads` keeps the last value.
- **Input.** `{"board_id": 41873925, "item_name": "Tallowmere sync", "item_name": "Depot loads"}`.
- **Probe.** `G20.py`.
- **Actual.** Exit 0, and `args_digest` describes the object without the first value. A duplicate inside a `column_values` string is caught, because the raw string is checked too.
- **Expected.** Exit 3: a file whose meaning depends on the reader is not one the lint can vouch for.
- **Decision.** X22 (the file is the tool input exactly as it will be sent).
- **Fix.** `json.loads(text, object_pairs_hook=...)` that raises on a repeated key, for the payload file and for JSON walked inside strings. Use it for the index too.

### G21. A cost figure in a table without a cost word never enters the wall

- **Function.** `build_entry` (line 2702) publishes only F's cost figures. X25 makes a number a cost figure only when its sentence holds a cost cue, and a table row with a label such as `Fuel` and a header `Amount` holds none.
- **Input.** Record b: `| Fuel | 731,946 |` under `| Line | Amount |`. A text: `The line comes to 731,946.`
- **Probe.** `G21.py`, line "table figure without a cost word".
- **Actual.** Exit 0.
- **Expected.** A `figure` block. Client figures sit in tables more often than in sentences.
- **Decision.** U1 ("its client figures above a floor"); X25 (the cost cue, read sentence by sentence).
- **Fix.** For a Markdown table row, read the header row and the row's first cell as part of the sentence for the cost cue, and add `amount`, `total`, `fuel` and `spend` row labels to the cues. Or publish, at the wall's three-digit floor, every non-date number of 1,000 or more from a client-originated source. Part 1's figure rule gains the same.

---

## Notes

- **G22. Exclusion figures at n ≥ 1 block coarse round numbers in every other record.** Record b's exclusion figure 58,315 gives the forms `5e4`, `6e4` and `1e5`, so `We expect fifty thousand visits.` and `We need a hundred thousand rows.` block in record a (`G21.py`). This is X25's tolerance and Z17 item 1 as decided, and an allowlist cannot clear it. Consider a floor of two significant digits for exclusion figures on the wall.
- **G23. Figure renderings the wall does not key** (`G21.py`). `4.1287e5` (an exponent in text), the range `400k-413k` (part 1's F01, which the wall inherits through `parse_numbers`), and `412,870.50` against an integer figure (rounding half up gives `412871e0`) all pass. `0.41M` passes by Z17 item 1. Held: `$412,870`, `412,870 USD`, `£413k`, `412.87k`, `412'870`, a narrow no-break space, dot thousands, `412_870`, number words, and a JSON number.
- **G24. A structural id key exempts another client's figure from the wall.** `{"board_id": 412870}` and `{"item_ids": [412870]}` pass (`explore/e6.py`). This is Y08 and Z17 item 5 as decided, and part 1's F33 for `id`, here over all of Y08's keys.
- **G25. Misses as decided.** A one-word name under seven letters misspelt (`Brekk` for `Brekke`) has no key (X27 type 4). A look-alike the table lacks (Armenian `օ` in `Quorne`) is part 1's F12; the phonetic key backstops it for names of seven letters or more. Initials the other record never wrote (`FS`, `T F M`) pass (X26 step 3).
- **G26. What the index never sees** (X11, X25, X26 as decided): names that sit only in `inputs/` PDFs, images or spreadsheets; every `.json` file (`account.json` and `build.json` hold workspace and board names); `drafts/` and `deliverables/`; lower-case names; and non-cost numbers (`The fleet moves 1,284 pallets a week.` gives no figure).
- **G27. A record folder without a `CLIENT.md` is a slug only** (`explore/e8.py`): a record mid-init or with its file renamed is never asked for an entry. This is X30 as decided; Z18 item 5 relies on it.
- **G28. `terms` skips folders named `.git` and `__pycache__` at any depth** (`G10.py`, last line). This is X31 as decided; a `.git` folder that is not the repository's own is unusual.
- **G29. Size.** A payload of 20,001 short strings takes 6.6 seconds (`explore/e6.py`); there is no time cap (X42). Thirty JSON strings nested inside each other exceed the depth limit and exit 3, which is the safe side.

---

## Z13: the narrowing of the phonetic test, measured

**What Z13 changed.** Item 1: a single word's key is published only when no common or stop word shares it. Item 2: a checked run is keyed only when one of its words is not ordinary and its words hold seven letters or more. Item 3 adds the joined key on the index side. Item 3 only adds blocks, so the measurement keeps it on both sides and compares the script with and without items 1 and 2.

**How it was measured.** `Z13.py` runs the frozen module in process, with nothing written anywhere. Its output is in `Z13.out`, and `Z13-cli.py` shows the same through the command line.

**Part A: misspellings that keep the key.** One interior vowel was changed, or a consonant doubled. Every name is generated from invented syllables.

| Names | n | blocked both ways | blocked only before Z13 | blocked only after | blocked neither way |
|---|---|---|---|---|---|
| one-word names, 7 to 11 letters | 200 | 171 | 29 | 0 | 0 |
| two-word names under 7 letters | 100 | 0 | 100 | 0 | 0 |
| two-word names of 9 letters or more | 100 | 100 | 0 | 0 | 0 |
| two ordinary words, US/UK spelling swapped | 400 | 400 | 0 | 0 | 0 |

- 29 of 200 one-word names (about one in seven) share their key with an ordinary or `shared/` word, so their misspellings now pass. Record b's own client name is one of them: `Fernhollow` keys to `FRML`, which an ordinary word shares, so `Fernholow` and `Fernhallow` pass while `Fernhollow` blocks (`Z13-cli.py`). `Tallowmere` (`TLMR`) is not shared, and `Talowmeer` still blocks.
- Every two-word name under seven letters (a short first name and surname, such as an invented `Ky Varn`) now passes when misspelt (`Ky Vorn`); before Z13 every one blocked.
- Longer two-word names (`Odalis Breke` for `Odalys Brekke`) and US/UK spelling pairs are unchanged.

**Part B: ordinary text against 87 names harvested from three invented records.** No own set, as `terms` runs. The counts are hits from the key alone.

| Text | Words | Before Z13 | After |
|---|---|---|---|
| the plugin's `shared/` files | 52,877 | 43 | 0 |
| the plugin's four scripts | 88,649 | 23 | 0 |
| docstrings of 12 standard-library modules | 20,414 | 7 | 4 |
| the fixture's twins | 1,016 | 0 | 0 |

- **What stopped blocking.** `formula` (with `formula9`, `formula13` and the like, 33 of the 66 hits in the plugin), `lease for`, `forward`, `limited`, `bearing`, `payloads`, `call at`, `call it`, `kill it` and `lease_free`. Each is an ordinary word or pair whose key equals that of an invented name of the three records. The four hits left in the standard-library text are all `getmembers`, a code word.
- **The trade in one sentence.** Z13 removes about one false block per 2,300 words of ordinary prose and plugin text (69 in 161,940), and in exchange lets through, when misspelt, every short two-word name and about one in seven one-word names. The correctly written name still blocks in every case.

**For the user's confirmation, two questions.** *Answered 2026-10-19:* both no, by A30, whose reading the user nodded ("Yes this is correct."). The wall blocks another client's names in their normal forms and need not chase misspellings by sound, so Z13 stands as built.

- **Short two-word names.** Item 2's seven-letter floor is the larger miss. A floor of five letters (not seven) for two-word runs, with the run still needing one word outside the ordinary words, would bring back the short person names. The false positives above came from runs of ordinary words, which item 2's first clause already stops.
- **One-word names.** Item 1 could keep a suppressed key whenever the word was harvested more than once, or in `CLIENT.md`. That would cover a record's own client name, which is the case here.

---

## What held

- **Normalisation on both sides of the hash.** These blocked on the wall: upper and lower case, a no-break space, a zero-width space and a soft hyphen inside a name, full-width letters, the Cyrillic look-alikes in the table, a combining accent added (`Tállowmere`), a possessive, a comma-split name, a name across a single line break, a name in two Markdown table cells, a camel-case fusion, a name in a URL host, in a URL path slug, percent-encoded, an e-mail address with and without its dot, and the slug written spaced, hyphenated and fused (`explore/e1.py`, `explore/e9.py`).
- **The harvest.** Body-line names, initials written in the record, hyphenated names (spaced, hyphenated and fused all blocked), and people's first or last name alone.
- **Figures.** Every rendering listed under G23 as held. The floor kept two-significant-digit renderings out (`0.41M`), as Z17 item 1 says.
- **The index.** Exit 3 for a newer schema, another normalisation, a torn file, an empty file, an upper-case key, and an unindexed record under `clients/`, under `archive/` or behind a linked folder. An archived, indexed record stays walled. Neither the index bytes nor any finding nor the coverage error carries another client's name or slug (G08's 3.9 traceback aside). Two `index` runs from two records at once kept both entries in every one of eight rounds, and readers running alongside never exited 0 (`explore/e7.py`). `terms` over the real `shared/` exits 0 with both records indexed.
- **The walker.** Object keys, numbers under ordinary keys (integers and floats), strings under structural keys, a top-level array, JSON three levels deep inside strings, the 64-level depth limit (exit 3), and booleans and null skipped. A misspelt `--kind` is a usage error (exit 3).
- **`blueprint`.** A planned name of the other record in a numbered section blocks, and the glossary is exempt from the copied-run rule only, with the wall still running on it.
- **Interpreters.** Python 3.9.6 and 3.14 gave the same result on every probe but G08.

---

## Fixes for part 2 (step 8), 2026-10-19

The original probes under `$SCR/probes2/` and the frozen copy `$SCR/frozen2/` were lost when the Mac restarted on 2026-10-19, which cleared `/private/tmp`. Each fixed finding's lasting proof is its unit test in `tests/unit/test_leak_wall.py`, which fails on the script as reviewed and passes now. Where a finding was also confirmed by a probe, the probe was rebuilt from the finding's minimal input under `$SCR/probes2-live/` and run against the live script; the rows say which.

| Finding | Rank | Outcome | Test, or the reason it is kept | Decision |
|---|---|---|---|---|
| G01 | blocking | fixed: the stop list's `shared/` words are the pinned `shared-words` region, compared with the folder by a unit test | `test_G01_X31_L195_U1_...`, `test_G01_Z12_...`; probe `G01_before.py` rebuilt: the first test fails with the stop list read live | R29 |
| G02 | blocking | fixed: `fold` spells the undecomposed letters plain; the wall also tries the second reading of ø, æ and œ on both sides | `test_G02_X28_letters_..._meet_their_plain_spellings`, `test_G02_X28_the_other_way_round_...`; both failed before the change | R30 |
| G03 | blocking | fixed: the wall fuses across a line-end hyphen (spaces allowed around the break) and across runs of `*`, `_`, `~` and backticks; the spaced twin stays | `test_G03_X27_a_name_broken_by_a_line_end_hyphen_or_a_markdown_mark_is_fused`; it failed before the change | R31 |
| G04 | blocking | fixed: a run of two or more words is dropped only as a phrase of the pinned `shared-phrases` region or when every word is in X26's own small list; `shared/` words filter single words only. The fixture's entries are unchanged; of the 2,970 rebuilt names, 2 are dropped now against 110 before | `test_G04_U1_X26_..._is_published_and_blocks`, `test_G04_Z12_the_embedded_shared_phrases_...`; `Signal Path` and the region test failed before the change (`Green Field` and `Clear Path` already blocked after R29); count probe rebuilt as `<scratchpad>/wp4-run1/g04/measure.py` | R32 |
| G05 | blocking | fixed: `build_entry` also publishes every window of two to four words of an exclusion term of five words or more, spaced and fused, leaving out a window of common words and X26's small list only, or a plugin phrase; the cut of `wall/1` and the index schema are unchanged (the user's choice of the review's first fix, 2026-10-21). Each of the two review terms publishes 9 of 9 windows | `test_G05_R33_U1_X26_an_exclusion_term_of_five_words_or_more_blocks_on_the_wall`, `test_G05_R33_a_window_of_common_words_only_is_not_published`, `test_G05_R33_a_term_of_four_words_or_fewer_publishes_what_it_did_before`; the first two failed before the change; no probe rebuilt | R33 |
| G06 | blocking | fixed: the walker drops format characters before it looks for JSON and also parses a string that starts with `"`; a JSON string literal (a text column's value) is checked as its own unit at `<path><json>`, an object or list is walked as before | `test_G06_R34_X22_L134_a_json_string_literal_is_walked_as_its_own_unit`; it failed before the change; no probe rebuilt | R34 |
| G07 | blocking | fixed in the lint: a folder of this record's name under the other root (`archive/` or `clients/`) is exit 3 for the wall and `index`, naming no folder; `index` will not replace an entry that lacks this record's `CLIENT.md` name digest; the wall keeps such an entry as another client's. `clients-index/1` unchanged. Owed to WP2: `record.py init` refuses a slug under `archive/` or already in the index | `test_G07_R35_X29_L178_two_records_with_one_slug_never_take_the_archived_clients_wall`; it failed before the change; clean control `test_G07_R35_an_archived_record_with_no_twin_and_a_same_name_reindex_work_as_before`; no probe rebuilt | R35 |
| G08 | blocking | fixed: the wall looks at home paths with `os.stat` (`path_kind`), not pathlib; a folder under `clients/` or `archive/`, or its `CLIENT.md`, that cannot be looked at is exit 3 on `<home>/clients/` or `<home>/archive/`, field `entries`, naming no folder; `twin_folder` counts such a path as a twin under 3.14 too; `read_index` is exit 3 when the index or its mutex cannot be looked at | `test_G08_R36_X30_A24_L205_a_record_folder_that_cannot_be_searched_is_exit_3_naming_no_folder`, `test_G08_R36_R35_A24_an_archive_that_can_be_listed_but_not_searched_is_exit_3_naming_no_folder`; the first failed before the change under both interpreters (b's path under 3.9.6, exit 0 under 3.14.6), the second under 3.14.6; both pass under both; no probe rebuilt | R36 |
| G09 | blocking | fixed: while a blueprint file is checked, O leaves out every blueprint file of its strand (`solution/blueprint.md` and each `versions/*/blueprint-r*.md`), so the frozen copy no longer makes the blueprint's words this record's and the build-guard check blocks; another strand's blueprint files, any other record file and payloads (X11) are unchanged. The review's second fix (blueprint lines O for payloads only after a clean `blueprint` run) is not built and waits for the user's word | `test_G09_R37_Z15_X45_L189_the_frozen_blueprint_copy_never_makes_its_own_words_this_records`; it failed before the change at the first frozen copy; clean controls `test_G09_R37_a_word_held_outside_this_strands_blueprint_files_is_still_this_records` (its last case, the other strand's own check, failed before too); no probe rebuilt | R37 |
| G10 | blocking | fixed: one walk (`walk_inside`) for `scan`, `terms` and `record_files`: a linked folder or file is followed when it resolves inside the folder walked, once, under its real name, and is exit 3 naming the link, never its target, when it resolves outside; a link into `drafts/` still feeds no set | `test_G10_R38_X31_terms_walks_a_linked_folder_inside_the_folder_and_stops_on_one_outside`, `test_G10_R38_X30_a_linked_folder_in_the_record_is_harvested_inside_and_stops_outside`; both failed before the change with exit 0, the second because a linked file outside the record made `Tallowmere` this record's; no probe rebuilt | R38 |
| G11 | should fix | fixed: on the checked side, a run of two or three words with only white space between them that passes Z13 item 2's gate is also looked up joined against the other entries' names and terms and the slugs, unless O holds the run; plain spaces are still never fused on the publishing side or in O. The review's route (the run's key against `phonetic`) is not built: it misses `Fern Hollow`, whose key Z13 item 1 withholds | `test_G11_R42_X27_a_one_word_name_written_as_two_or_three_words_blocks`; it failed before the change; clean control `test_G11_R42_X27_ordinary_two_word_phrases_never_fuse_into_another_records_single_word`; no probe rebuilt, a count probe in `<scratchpad>/wp4-run3/g11/measure.py` (0 new hits over 150,819 tokens) | R42 |
| G12 | should fix | fixed: `fold` reads U+2018, U+02BC, U+00B4, the backtick and U+FF07 as an apostrophe between two letters or digits, on both sides of the hash and for every word rule; on the checked side only, each word is also looked up with a trailing `s`, or `es` after a sibilant, removed, and a one-letter token is fused to the capitalised word after it across spaces or one apostrophe shape; stems and fused initials are never published. `O´Rourke`, ``O`Rourke`` and `O Rourke` already blocked through R31 and R42; `Kestle Fresh Foods` now blocks on the whole name | `test_G12_R43_X28_plural_and_apostrophe_shapes_of_another_records_name_block`; it failed before the change; clean control `test_G12_R43_ordinary_plurals_and_markdown_code_stay_clean`; no probe rebuilt, a count probe in `<scratchpad>/wp4-run3/g12/measure.py` (0 new hits over 151,269 tokens) | R43 |
| G13 | should fix | fixed: after X30's coverage check, `build_wall` walks each other record that has an entry with the index harvest's own walk (`record_walk`) and compares the newest modification or status-change time of the files that feed an entry (allowlist and live map left out), by `os.stat` only, with the entry's `updated`, allowing the stamp's second and 2 seconds; an older entry is exit 3 on `<home>/clients-index.json`, `entries`, giving a count and naming no folder; this record's own entry is never compared; `index` stamps the later of the clock and the newest change, and writes a new stamp after an edit that changes no list; P5 gains the moment "after every edit of `exclusions.md`, `research/` or strand Markdown", owed to WP8 and WP12 | `test_G13_R44_X30_P5_an_entry_older_than_its_record_is_exit_3_until_that_record_is_indexed`; it failed before the change; clean controls `test_G13_R44_an_untouched_record_a_skipped_file_and_this_records_own_entry_never_trip_it` (failed before only at record b's check of record a's edit) and `test_G13_R44_a_change_within_the_stamps_second_and_the_slack_is_not_older`; no probe rebuilt | R44 |
| G14 | should fix | fixed: after X30's coverage check, `build_wall` is exit 3 on `<home>/clients-index.json`, `entries`, giving a count and naming no folder, when an entry's `names` list is empty or, where its folder is under the home, lacks that folder name's spaced digest, which X26 step 1 always publishes (`entry_is_damaged`); `index` from the record replaces such an entry under its key when its new lists hold every digest the entry still holds, and otherwise is exit 3 and points at the backup; `read_index` and `clients-index/1` unchanged; no path through `index` writes an empty `names` list, so both of the review's checks are built | `test_G14_R45_Z18_X26_an_emptied_or_half_restored_entry_is_exit_3_until_its_record_is_indexed`; it failed before the change; clean controls `test_G14_R45_a_normal_entry_one_with_names_only_and_an_archived_one_with_no_folder_pass` and `test_G14_R45_X26_index_always_writes_the_folders_name_even_with_no_client_name`; no probe rebuilt | R45 |
| G15 | should fix | fixed: `twin_folder` (R35) first checks that the record's resolved parent is `<home>/clients` or `<home>/archive`, the home resolved too so a linked home matches; otherwise every run that builds the wall from a record, and `index`, is exit 3 on `CLIENT.md`, `record`, telling the user to point `MMB_HOME` at the home that holds the record or move the record into that home's `clients/`, naming no path; the twin test then looks only at the other root. `terms`, a summary-mode `scan` and a folder with no `CLIENT.md` are unchanged | `test_G15_R46_X30_a_record_checked_against_a_home_that_does_not_hold_it_is_exit_3`; it failed before the change with exit 0; clean control `test_G15_R46_records_under_clients_or_archive_and_a_home_reached_through_a_link_pass`; no probe rebuilt | R46 |
| G16 | should fix | fixed: `build_entry` publishes a harvested single word only when the record never writes it in lower case as prose (`lower_words`; lower case inside an address, a link, a joined name or a code word does not count; runs and X26 step 1's forms are always kept); `kept` drops a plural or inflected form of a stop word (`inflection_stems`, so `thursdays` falls with `thursday`); `index` prints `single_words`, the count and the sorted single words. The planted entries drop one word each: `holdings` (b, 20 to 19) and `extracts` (a, 22 to 21) | `test_G16_R47_X26_ordinary_words_published_as_one_word_names_stop_blocking`, `test_G16_R47_real_one_word_names_keep_blocking_and_index_shows_the_single_words`; both failed before the change; probes rebuilt as `<scratchpad>/wp4-run3/g16/draft.py` (the review's draft: exit 1 with four name blocks before, exit 0 after) and `measure.py` | R47 |
| G17 | should fix | fixed at the user's word (2026-10-21): O, the wall's own set, holds only `calls/`, `inputs/` and `research/` whole, `CLIENT.md`'s name, former names and slug, and the blueprint's client-facing lines (X11, R37); `log.md`, `meetings.md`, `CLIENT.md`'s body, the strand files, the `solution/` notes and the blueprint's other lines still feed the harvest and the sets, and never O (`own_text`). The 250 grading cases keep their outcomes, and no existing test needed a change | `test_G17_R51_X27_X11_a_line_the_session_wrote_never_makes_another_records_name_this_records`; it failed before the change at `solution/build-notes.md`; clean control `test_G17_R51_a_name_in_this_records_calls_inputs_or_research_and_its_own_names_still_pass`; probe `<scratchpad>/wp4-run4/g17/probe.py` (the `CLIENT.md` names) | R51 |
| G18 | should fix | fixed: `blueprint` is exit 3, "cannot find sections 1 to 15", unless level-2 headings numbered 1 to 15 are each found once and in order before section 16; `## 4)` and `## 4:` are section 4 too, the bold, "Section 4" and "Four" shapes are not; a level-2 heading that is no numbered section, or a level-1 heading after section 1, before section 16 is exit 3 on its line; the error says to write the sixteen headings as `blueprint-guide.md` numbers them, with added items as level-3 subsections. The short test blueprints and the fixture's `R10c-p.md` and `R10c-t.md` gain the full set of headings, their text in place (the main session's decision, 2026-10-21) | `test_G18_R49_X09_section_4_written_with_a_bracket_or_a_colon_is_checked`, `test_G18_R49_X09_a_blueprint_without_sections_1_to_15_each_once_and_in_order_is_exit_3`, `test_G18_R49_D19_a_heading_that_is_no_section_before_section_16_is_exit_3`; all three failed before the change; clean control `test_G18_R49_Z19_in_a_full_blueprint_the_glossary_is_exempt_from_the_copied_run_rule_only`; no probe rebuilt | R49 |
| G19 | should fix | fixed: `payload` also checks one joined text per payload, every string that joins in walk order joined by single line breaks, under the copied-run, quote and wall rules only, and its HTML copy; keys, numbers and structural ids do not join, and a string holding JSON joins through the strings walked inside it; a hit across strings is reported at the first field it touches with `fields` naming the strings it spans, and dropped when a per-field finding of its rule and class overlaps it; a `.json` file under `scan` is joined too. The 250 grading cases keep their outcomes and findings; about 8 ms more on the fixture's largest payload | `test_G19_R53_A916_X22_a_run_a_quote_or_a_name_split_over_two_payload_fields_blocks`; it failed before the change; clean control `test_G19_R53_ordinary_joins_pass_and_a_run_inside_one_field_is_reported_once`; probe rebuilt as `<scratchpad>/wp4-run4/g19/probe.py` (the three inputs exit 0 with the joined check off, exit 1 with it on), with `measure.py` and `size.py` beside it | R53 |
| G20 | should fix | fixed: every JSON file the lint reads (the payload file, a `.json` file under `scan`, the settings and the index) and every JSON string the walker opens is read strictly; a key written twice in one object is exit 3 at the key's path, naming the key and saying to write it once, as the tool will receive it; text that only opens like JSON stays plain text, and the same key at two depths passes. The 250 grading cases keep their outcomes | `test_G20_R54_X22_a_key_written_twice_in_a_payload_is_exit_3_naming_the_key`, `test_G20_R54_X02_a_key_written_twice_in_the_index_or_the_settings_is_exit_3`; both failed before the change; clean control `test_G20_R54_a_key_at_two_depths_a_repeat_in_plain_text_and_the_fixture_pass`; no probe rebuilt | R54 |
| G21 | should fix | fixed: a number in a Markdown table body row also reads the table's header row and the row's first cell for X25's cost cue (`table_cues`), on the record's side and the checked side; a bare run of eight digits or more is never lent the cue; the cost cues gain `amount`, `total` and `fuel` with their plurals (`spend` was there). The review's second option is not built (G22). The planted records publish the same wall figures before and after (1 and 6), and the 250 grading cases keep their outcomes | `test_G21_R56_U1_X25_a_cost_figure_in_a_table_without_a_cost_word_in_its_row_blocks_on_the_wall`, `test_G21_R56_X25_a_cost_figure_in_a_table_of_this_records_own_files_meets_the_figure_rule`; both failed before the change; clean control `test_G21_R56_counts_dates_and_ids_in_a_table_publish_no_figure_and_a_cued_sentence_works_as_before` (failed before only at its two cost-headed amounts); no probe rebuilt, a count probe in `<scratchpad>/wp4-run4/g21/measure.py` | R56 |
| G22 | note | fixed: an exclusion figure's wall forms stop at the largest k that still holds its first two significant digits, or its one for a figure written with one (`exclusion_top`); k = 0 is always kept. 58,315 keeps `58e3` and drops `5e4`, `6e4` and `1e5`, so `fifty thousand visits` and `a hundred thousand rows` pass in record a while `58k`, `58.3k` and `fifty-eight thousand` block; 60,000 keeps `6e4`. Cost figures, O and the checked side are unchanged, and the record's own exclusion rule still matches every rendering. The 250 grading cases keep their outcomes; `test_L174_L175_X25_...` now asserts `42e2`, not `4e3`, for 4,250 | `test_G22_R57_X25_Z17_an_exclusion_figure_blocks_its_renderings_and_no_longer_a_one_digit_round_number`, `test_G22_R57_a_figure_written_with_one_significant_digit_keeps_its_own_round_forms`; both failed before the change; no probe rebuilt | R57 |
| G23 | note | fixed: a checked number below a unit's precision is tested at k = 0 truncated as well as rounded (`tested_forms`), so `412,870.50` meets 412,870; the parser reads an exponent on digits (`4.1287e5`, `4.1287E+05`), judged a normal form under A30, since a JSON number written that way was already held; each end of a range (`400k-413k`) already blocked through R01 (part 1's F01), and the test now holds it. `0.41M` and `4.1e5` stay out by Z17 item 1. The 250 grading cases keep their outcomes | `test_G23_R58_X25_A30_a_figure_with_cents_either_end_of_a_range_or_an_exponent_blocks_on_the_wall`; it failed before the change at `412,870.50`; clean control `test_G23_R58_Z17_two_digit_renderings_other_amounts_and_words_with_an_e_stay_clean`; no probe rebuilt | R58 |
| G24 | note | kept: `{"board_id": 412870}` and `{"item_ids": [412870]}` still pass the wall's figure test, as decided | Y08 exempts a value in the id shape under a structural key from the figure rules, and Z17 item 5 takes that exemption to the wall; R53 keeps structural ids out of the joined text too. Y08's key list is still open for the user's nod, so the exemption stays until that nod settles it | Y08, Z17 item 5 |
| G25 | note | kept, one part already changed: `Brekk` for `Brekke` and initials the other record never wrote (`FS`) still pass; Armenian `օ` in `Quorne` now blocks, since R12 (part 1) added it to the look-alike table. Seen beside it: record b of the fixture writes `TFM`, and `T.F.M.` and `T-F-M` block while `T F M` passes, since plain spaces fuse only under Z13 item 2's seven-letter gate (R42) | a misspelling by sound is outside the wall (A30, Z13, X27 type 4), and the harvest takes only initials the record writes (X26 step 3); probe `<scratchpad>/wp4-run4/g25/probe.py` | X27, X26, A30, R12 |
| G26 | note | kept: names only in `inputs/` spreadsheets, `.json` files such as `account.json`, `drafts/` and `deliverables/`, lower-case names and uncued numbers (`1,284 pallets`) still give no entry digest. R47 widened the lower-case part (a single word the record ever writes in lower case is not published) and R56 lends a table's header cue to its rows; neither changes the note | the index reads X11's D sources only (`.md`, `.txt`, `.docx`), drafts feed no set (X45), names are capitalised runs (X26) and figures need a cost cue (X25); probe `<scratchpad>/wp4-run4/g25/probe2.py` | X11, X25, X26, X45 |
| G27 | note | kept: a folder under `clients/` with no `CLIENT.md` is still checked by its slug only (`Brindle Tiles` blocks as `slug`, a name inside it passes), and the coverage check never asks it for an entry. R44, R45 and R46 left it as it was | X30 tests `CLIENT.md` with `is_file` and opens nothing, and Z18 item 5 relies on it; probe `<scratchpad>/wp4-run4/g25/probe2.py` | X30, Z18 |
| G28 | note | kept: `terms` still skips folders named `.git` and `__pycache__` at any depth; R38 moved `terms` onto `walk_inside` and kept the skip (`TERMS_SKIP`) | X31 names the two folders; a `.git` folder that is not the repository's own is unusual; probe `<scratchpad>/wp4-run4/g25/probe2.py` | X31, R38 |
| G29 | note | kept with the figure: 20,001 short strings now take 15.0 s with no digit in them and 20.2 s as R53's `step <i> of the yard plan` (11.7 s and 15.1 s with the joined check off), against the review's 6.6 s for a payload whose text was lost: about 2.3 to 3.1 times. The time is linear (0.74 ms per string at 2,500, 5,000, 10,000 and 20,001 strings), and the profile spreads it over every rule a string meets (the wall about a third, R53's joined check about a quarter, the shipped rows and the phonetic rule most of the rest), so there is no single local cause; 3.9.6, in process | X42 sets no time cap and bounds a run by its input; a real tool input is far smaller (R53 measured the fixture's largest payload at about 42 ms); the 64-level depth limit is still exit 3; probes `<scratchpad>/wp4-run4/g29/size.py` and `scale.py` | X42 |

R50 fixes a gap the G18 fix found, not a finding of the review: with the template's section 3 title `Requirement trace`, a record's entry published `requirement` and `terms` over the real `shared/` then blocked on `requirements`, so the harvest now drops a single word whose plural is a stop word too (`plural_forms`), tested by `test_G18_R50_R47_the_sixteen_section_titles_publish_no_word_and_terms_over_shared_passes` and `test_G18_R50_a_real_one_word_name_under_a_section_heading_still_publishes_and_blocks`.

R52 fixes a gap the R50 fix found, not a finding of the review: `blueprint` did not check the words of a section 1 to 15 heading itself, so `## 4. Tallowmere mapping` passed; each such heading's title is now checked with its section, the template's own titles excepted (`SECTION_TITLES`), tested by `test_R50_R52_X09_Z19_a_section_headings_title_is_checked_with_its_section` and `test_R50_R52_a_blueprint_whose_headings_are_the_template_titles_passes_as_before`.

R60 fixes the gap the notes agent found while checking G25, not a finding of the review: record b writes `TFM`, and `T.F.M.` blocked while `T F M`, `T. F. M.` and initials of five or six letters spaced or dotted passed, so every run of two to six single capitals with spaces, tabs or a full stop between them is now looked up fused, tested by `test_G25_R60_X26_initials_written_with_spaces_or_full_stops_block_as_fused_ones_do`, `test_G25_R60_X26_five_and_six_letter_initials_block_spaced_or_dotted` and `test_G25_R60_capital_runs_that_match_no_initials_and_lone_letters_stay_clean`.
