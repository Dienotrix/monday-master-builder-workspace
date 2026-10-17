# WP4 decisions: the gaps of CONTRACT.md section 4

Date: 2026-10-17. Internal build file: never client-facing.

This file settles each gap of `CONTRACT.md` section 4, X01 to X47, so that the shared edits (step 3), the trap fixture (step 4), the trace check (step 4b) and the code (steps 5 and 6) are written against one reading. It is step 2 of `PLAN.md`. Nothing here is built yet; every entry says which step builds it and which test proves it.

## Sources

| Short | File | What was read |
|---|---|---|
| PLAN | `rebuild-workspace/build/wp4/PLAN.md` | all of it, with the user's answers on its status line |
| CON | `rebuild-workspace/build/wp4/CONTRACT.md` | all of it: clauses L01 to L279, shapes (section 3), gaps X01 to X47 (section 4), coverage (section 5) |
| A§ | `rebuild-workspace/design/ARCHITECTURE.md` | 5.3 and 5.4 (340 to 360), 6, 7.1 (440 to 442), 7.5 (613 to 627), 8.5 steps 4 and 5, 8.6 steps 9 and 17, 9.6 (912 to 922) |
| BP | `rebuild-workspace/design/BUILD-PLAN.md` | section 0 (A11), WP1's `leak-terms.txt` and `--terms` lines (113, 114), the WP4 block (153 to 159), the write path (252), WP14 (318 to 323), the file rows (364 to 382), 4.2 (405 to 448) |
| AM | `rebuild-workspace/design/AMENDMENTS.md` | A11, A12, A16, A17, A18, A20, A23, A24, A25, A28, A29 |
| RM, LT, SF | `shared/record-map.md`, `shared/leak-terms.txt`, `shared/safety.md` of the plugin | RM 5 to 80, 124 to 137, 255 to 370 (the `Pinned: ledger` form); LT all 195 lines; SF section 6 (80 to 90) |
| G, W, R | `rebuild-workspace/build/wp2/DECISIONS.md`, `rebuild-workspace/build/wp3/DECISIONS.md` | G10, G11, G39, G40, G49, G57, G58; W91; R8 |
| AI | `rebuild-workspace/design/ai-offerings-findings.md` | all of it (the agent, Vibe and workflow fields; the unprobed kinds) |
| MC | `plugins/monday-master-builder/scripts/mmb_common.py` | the function list and docstrings: `home`, `read_settings`, `read_text`, `read_json`, `json_text`, `sha256_file`, `sha256_text`, `write_file`, `backup_file`, `schema_newer`, `require_schema`, `record_mutex`, `relative`, `now_utc`, `stamp` |
| LP | `ledger.py` (the frame) and `tools/lint_plugin.py` (`PINNED`, `pinned_section`, `pinned_region`, `normalise_name`) | the parser, `emit`, `main`, the envelope and exit codes; how a `Pinned:` section is compared with a script's region |
| KEY | the twenty-five `expected_leak_blocklist` arrays under `rebuild-workspace/fixtures/s*/answer-key.json` | all 400 entries, read for the category map only; nothing is copied from them (D24) |

Authority order: AMENDMENTS over ARCHITECTURE over BUILD-PLAN over `record-map.md` and the other `shared/` files. The user's answers of section 1 bind like an amendment for this package. WP2's decisions G01 to G61 and WP3's W01 to W92 and R1 to R13 stand and are not reopened here.

## How to read an entry

Each gap entry is keyed by the contract's own id, `### Xnn <title>`, in the contract's order, and has three parts:

- **Decision.** What is built, with the numbers, shapes and flags a builder needs.
- **Reason.** The source that wins, named by anchor, and why.
- **Follow-up.** *Build:* the step that builds it. *Test:* the clause or the test that proves it. *Touch-up:* any change owed to a design file, listed again in section 5 and applied only at the user's word.

Anchors follow the contract: `A§:n` an ARCHITECTURE line, `BP:n` a BUILD-PLAN line (`BP:158.n` part n of the acceptance sentence), `AM:n`, `RM:n`, `LT:n`, `SF:n`, `AI:n`, `Lnnn` a clause, `PLAN §7.n` a conflict entry and `PLAN §8.n` a nod.

An entry marked **For the user** would stop the run until the user answers it. None is marked so. Every decision taken on the user's behalf where the sources are silent and the choice is not obvious is listed in section 7, "Worth the user's nod".

Every example in this file is invented and generic. No person, firm or monday account, workspace or object is named.

The sections: 1, the user's answers; 2, the gaps; 3, the category map; 4, the shared edits for step 3; 5, the touch-ups for the user's word; 6, what other packages owe; 7, worth the user's nod.

---

## 1. The user's answers, 2026-10-17

These are the user's decisions, recorded on PLAN's status line, in a fresh session, in their words: Q1 "(a) Names, terms, figures"; Q2 "(a) Guide the fixture now"; Q3 "(a) Cover them now"; Q4 "(a) Review plus fixture check"; sections 7 and 8 nodded, "Yes, one at a time".

### U1 Q1 (a): the wall holds names, terms and figures

**What it decides.** BP:158's form of the cross-client wall over A§:922's. Each record publishes into `<home>/clients-index.json` hashes of its normalised names (the client, its people, customers, partners and products as the record names them), of the terms of its `exclusions.md` files, and of its client figures above a floor this file sets. The wall blocks a payload term whose hash is in another client's entry and not in this record. `leak_lint.py index` writes the entry at init, after every intake and at close-out, and an entry stays after the record moves to `archive/`. `terms` over `shared/` at release checks the same digests.

**What it touches.** Clauses L168 to L199 and L279; gaps X01, X02, X21, X25 to X30, X45, X46. The design touch-ups to A§9.6, A§7.1, RM:76 and SF section 6 follow at the user's word (section 5).

### U2 Q2 (a): the twenty-five arrays guide the fixture now

**What it decides.** This file read the 400 prose entries of the twenty-five `expected_leak_blocklist` arrays and states every kind of leak they describe as a category, each with a planted case and a clean twin for the trap fixture (section 3). Nothing of the arrays is copied: the fixture is invented text in the same shapes (D24, A12). Grading the lint on the twenty-five keys is owed to WP14's leak grader on the seed records at stage 4, listed and not failed.

**What it touches.** Clauses L214 to L270; gaps X06, X13, X20, X39.

### U3 Q3 (a): the AI payload kinds are built in stage 2

**What it decides.** The payload walker covers an agent's name, role, role description, goal, plan, user prompt and knowledge-grant names; a Vibe prompt and app name; an AI column's prompt; a workflow's name, description and step text; a sequence's step text and recipient list; and a webhook's URL, now, from `ai-offerings-findings.md` (P-19 to P-21) and the connector shapes recorded there. Stage 4b adds only what new probes change (X14).

**What it touches.** Clauses L142 to L161; gaps X14, X22, X34.

### U4 Q4 (a): the bypass review plus the fixture trace check

**What it decides.** Step 7 is one adversarial review of bypasses, every blocking and should-fix finding proved by a throwaway probe outside the repository; step 4b is a Sonnet trace check of each planted case and twin against A§9.6 and this file, made without reading code. Every disagreement it finds is settled by the step-4 author before step 6 starts. This file's section 3 and the fixture README are what the trace check reads, so both are written to be checkable without code.

**What it touches.** Clauses L215, L216, L221, L222; gap X18.

### U5 Sections 7 and 8 are nodded, nod 14 changed

**What it decides.** The twenty readings of PLAN §7 and the fourteen nods of PLAN §8 are the user's accepted defaults, and this file decides in line with them. Nod 14 is changed by the user: every step runs one at a time, step 4 before step 5. So part 1 of the code (step 5) is written after the fixture exists, and may use the fixture's planted cases in its own tests as well as inline samples.

**What it touches.** Every gap that carries a PLAN §7 entry (X01 to X20); nods 1 to 13 as they are cited below (three test files, the copied frame, `.docx` from XML strings, planted records copied into a temporary home, the embedded common-word list, the counted category class, exclusions of every strand and the allowlist of one, `settings.json` required, redaction not defaulted, input hashes in the output, invented names only, `Pinned: leak` with one lint tuple, macOS first). Where a source forces a reading against a nod, the entry says so plainly. None does.

---

## 2. The gaps

Entries follow the contract's numeric order, X01 to X47, so the count of entries equals the count of gaps. Sections 4 and 5 gather what the entries owe to shared files and design files.

### X01 The wall's contents

**Decision.** The wall is BP:158's (U1). A record's index entry holds four hash lists, `names`, `phonetic`, `terms` and `figures`, built by one digest function (X27, X28) from the record's own files (X26). The wall runs inside `payload`, `blueprint`, `scan` (full and client-safe-block modes) and `wall`, and `terms` reads the same entries (X31). A payload candidate blocks with rule `wall` when its hash is in another entry's list and the same candidate is not in this record (X27). On top of the hashes the slugs of the other folders under `<home>/clients/` and `<home>/archive/` are checked as names (X21). The settled parts are: the floor (X25), the normalisation (X28), where names come from (X26), how a payload is cut into candidates (X27), the index shape and writer (X02), shared-file safety (X29), an absent index (X30), drafts (X45) and the stamp (X46).

**Reason.** The user's Q1 (a) binds (U1) over A§:922, A§:440, RM:76 and SF:90, which hold names only; AMENDMENTS A20 makes the lint the wall, and BP:158.19 is the acceptance it is held to.

**Follow-up.** *Build:* step 6. *Test:* L168 to L194 and L279 in `test_leak_wall.py`, on the two planted records. *Touch-up:* A§9.6:922, A§7.1:440, RM:76 and SF:90 say the index holds the vocabulary digest of names, terms and figures, keyed by a hashed slug (section 5, item 1).

### X02 The index has no writer, no schema and no owner row

**Decision.** `leak_lint.py index` is the one writer of `<home>/clients-index.json`. It reads this record's files and the index, and writes only the index (L09, L180). The schema is `clients-index/1`, written through `mmb_common.json_text` (two-space indent, `ensure_ascii=False`, LF, final newline):

```text
{
  "schema": "clients-index/1",
  "hash": "sha256-128",
  "normalisation": "wall/1",
  "entries": {
    "<key>": {
      "updated": "YYYY-MM-DDTHH:MM:SSZ",
      "names": ["<32 hex>", ...],
      "phonetic": ["<32 hex>", ...],
      "terms": ["<32 hex>", ...],
      "figures": ["<32 hex>", ...]
    }
  }
}
```

- `<key>` is the first 32 hex characters of `sha256("s:" + <the slug from CLIENT.md>)`. The slug is never stored in plaintext (A§:440), so the key carries no name.
- `hash` names the digest: sha256 of the UTF-8 form, cut to its first 128 bits (32 lowercase hex characters). `normalisation` names the text normalisation of X28 and the phonetic key of X32 together; a reader that meets another value is exit 3, the same as a newer schema.
- The four lists hold unique values sorted ascending; the entries are written in ascending key order. Nothing in the file is plaintext.
- The entry carries no state (open or archived) and no count: the lint never needs them, and fewer fields leak less.
- The schema check is the lint's own: `mmb_common.SCHEMAS` has no `clients-index` name and `mmb_common.py` stays byte-equal (L276), and `require_schema` raises a refusal (exit 1) where the lint needs exit 3. So the lint holds its own known-schema table, `clients-index/1` and `settings/1`, and a higher number or another name is exit 3 (G57's rule, the lint's exit code).
- The entry of a record at init holds what that record holds then: at least the client name and slug words from `CLIENT.md` (X26), its `exclusions.md` terms if engagement seeded any, and nothing else.
- Who calls it, and when (X47): the engagement skill after `record.py init` (WP8); `call-intake` after every saved call, document or email (WP8); `client-closeout` before the record moves to `archive/` (WP12). `record.py` is not changed (L276). The test of the three moments is L179, stage 4 headless.

**Reason.** PLAN §7.2 and Q1 (a) name `leak_lint.py index` as the writer and `clients-index/1` as the schema; A§:440 forbids plaintext; G57 sets the newer-schema rule and BP:158.32 makes every could-not-run exit 3; L276 keeps `mmb_common.py` unchanged.

**Follow-up.** *Build:* step 3 pins the shape (section 4); step 6 builds `index`. *Test:* L168, L176, L177, L181; a unit test writes `clients-index/2` and `normalisation: "wall/2"` and expects exit 3 from every reader. *Touch-up:* RM:76 and A§7.1:440 point at the pinned shape; G58's "written at a record close" reads "written by `leak_lint.py index` at init, after every intake and at close-out" (section 5, item 1). *Owed elsewhere:* WP8 and WP12 call `index` at the three moments (section 6).

### X03 Nine markers, eight listed; paths in one spelling

**Decision.** Two parts.

1. *Markers.* Step 3 adds the row `[A]` to the `markers` class of `shared/leak-terms.txt`, directly after the `[I]` row, and changes the class comment from "The eight evidence markers" to "The nine evidence markers" (section 4.2). The nine (`[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]`, `[Q/doc]`, `[X]`, `[E]`, `[I]`, `[A]`) are also embedded in the script's pinned region, and a unit test asserts that each of the nine is a literal row of the shipped `markers` class (L66). Markers match case-insensitively, as every literal row does (LT:18): a Markdown checkbox written `[x]` blocks as `[X]`. That is a false block the writer fixes by using another checklist form; it is listed for the user's nod (section 7, item 22).
2. *Paths.* No row is added for Windows paths. Before the `id-patterns` rows run on a line, the script also runs them on two copies of that line: one with every backslash turned into a forward slash, and one with percent-escapes decoded (`%2F`, `%5C`, `%7E` and the rest, with `urllib.parse.unquote`). A hit in any of the three copies blocks and is reported at the original position. So `clients\<slug>\calls\`, `.work\`, `strands\001-topic\`, `C:\Users\` and a mixed `clients/<slug>\calls\x` all block through the shipped POSIX rows. The class stays `id-patterns`.

**Reason.** A§:627, RM:272 and BP:158.5 ask for all nine, so LT:146 is the stale line; AM:40 to 44 (A24) and BP:158.7 ask for both spellings, and one rule in the script reaches every row without doubling the shipped list. The brief limits step 3's edit of `leak-terms.txt` to the `[A]` row, the comment and the category classes, which this reading respects.

**Follow-up.** *Build:* step 3 (the row and the comment); step 5 (the slash and decode copies). *Test:* L60 to L66, L67 to L69, L253, L255, L273. *Touch-up:* none.

### X04 Where the firm's renderings live

**Decision.** `local/settings.json` is the source of the firm rule: `firm.name` and every string of `firm.renderings[]` are literal renderings and are also matched by the phonetic rule (X32). `local/leak-terms.txt` holds the user's additions in the shipped syntax. Its rows under `class: firm` are further renderings (literal, `re:` or `phonetic:`) and `whitelist:` rows for the firm rule (X32). Rows of other classes block under their class. The lint reads both files on every command that runs the firm rule: `scan`, `payload`, `blueprint` and `terms` (X31). `wall` and `index` do not run it and do not need `settings.json`.

**Reason.** A§:916, BP:158.27 and RM:76 name `settings.json`, which `record.py home init` writes (G58); LT:5 to 6 and LT:35 to 36 are stage-1 comments that predate that writer, and A§ wins over LT. PLAN §8.8 (nodded) reads both files.

**Follow-up.** *Build:* step 5. *Test:* L38, L39, L41, L49. *Touch-up:* LT:5 to 6 and LT:35 to 36 say the renderings come from `local/settings.json` and the local list holds additions and the firm whitelist (section 5, item 3).

### X05 v1 surfaces

**Decision.** The lint checks A§9.6's surfaces and nothing rendered: planned text in the blueprint (`blueprint`), every payload (`payload`), every strand's `drafts/` and `deliverables/handoff/` (`scan`), live object names during the audit (`payload --kind generic`, handed by the audit), each strand's `SUMMARY.md` under two rules (X37), and the client-safe block of a call summary or a document snapshot at the moment it is written (X38). `.docx` input is read because BP:158.14 asks for it (X35). There is no PDF reader and no call to any outside tool (L05, L167).

**Reason.** A§:914 ("In v1 nothing is rendered") wins over SF:82, SF:90 and LT:11 to 14, which name `sop/`, rendered Word and PDF and `pdftotext`; `deliverables/handoff/` is v1 because RM's strand table says it is written "through the lint" on a `non-platform` strand.

**Follow-up.** *Build:* step 5 (`scan` targets and modes). *Test:* L123 to L127, L164, L167. *Touch-up:* SF section 6 and LT:11 to 14 list the v1 surfaces; RM:272's "in `sop/`, `drafts/`, `deliverables/`" reads "in `drafts/`, `deliverables/handoff/`" (section 5, items 4 and 13).

### X06 The three paraphrase categories, and what a string rule can reach

**Decision.** The three categories are A§:916's: personal and emotional stakes; remarks by client staff about colleagues; our own internal assessments of people. SF:84's closing tactics stay covered by the `method` class (cost-of-waiting, exit ramp, commitment question are already rows). The lint reaches them with one rule, `paraphrase`:

- A sentence blocks when it holds a cue phrase of one of six groups **and** a person reference. A person reference is a capitalised token that is not at the start of the sentence and not in the common-word list (X19), or one of these role words: boss, manager, director, owner, founder, partner, ceo, cfo, coo, cto, vp, president, chairman, chair, controller, colleague, coworker, co-worker, assistant, receptionist, supervisor, lead, mother, father, mum, mom, dad, wife, husband, son, daughter, brother, sister. Pronouns are not person references.
- The six cue groups, embedded in the script between `# pinned: paraphrase-cues` and `# end pinned` (a region `lint_plugin.py` does not compare, like the common words), each word matched on word boundaries after the normalisation of X28. The step-5 author writes each group at about the size shown, from the rule's own meaning and not from any call:
  - `assessment`: decision maker, approver, gatekeeper, blocker, champion, skeptic, sceptic, veto, influencer, holdout, long pole, single point of failure, weak link, a risk, ally, hostile, resistant, on board, will kill it, can kill it, signs off, not technical (about 30);
  - `emotional`: burnt out, burned out, burnout, stressed, crying, cried, upset, embarrassed, embarrassing, humiliated, ashamed, furious, scared, anxious, keeps me up, lose sleep, losing sleep, devastated, heartbroken (about 30);
  - `health-identity`: hospital, surgery, illness, sick leave, medical leave, diagnosis, pregnant, pregnancy, injury, injured, therapy, disability, mental health, rehab, nationality, citizenship, visa, immigrant, immigration, accent, ethnicity, religion, and about forty common demonyms (about 70);
  - `departure`: leave the business, leaving the company, quit, quits, quitting, resign, resigning, resignation, retire, retiring, retirement, let go, fired, laid off, poached, moving on, handing in notice (about 20);
  - `colleague-remark`: hates, can't stand, never answers, doesn't answer, won't answer, ignores, useless, lazy, clueless, hopeless, disgrace, nightmare, menace, careless, sloppy, unreliable, rude, will kill me, buried with (about 30);
  - `personal-life`: vacation, holiday, birthday, golf, hangover, kids, children, girlfriend, boyfriend, divorce (about 15).
- A `paraphrase` finding blocks, names its group as its class, and may be cleared by an allowlist row of the payload's own strand naming the cue phrase, with a caution (X10, X39): a cue word can be a client's own vocabulary (a clinic's "hospital", a staffing firm's "resignation"), and A§:920 lets the allowlist clear vocabulary rules.
- Beside it, two embedded vocabulary groups block as `term` findings and are clearable the same way: `internal-vocabulary` (the plugin's own words the shipped `method` class lacks: composite block, candidate segment, own-side stretch, swallowed assent, boundary artifact, shred index, talk share, delivery notes, alias table, intake report, type header, structure inventory states such as proposed-and-displaced and compound show) and `sales-framing` (upsell, up-sell, cross-sell, land and expand, land-and-expand, expansion opportunity, closing tactic).

How each of the seven trap categories CON names reads, with the expected outcome step 4 plants (the fixture states the same in its README):

| Trap category (A§:918) | How the lint reaches it | Planted outcome |
|---|---|---|
| the seller's own commercial terms | the seller's rate or day-rate figure is in the record's figure set (X25); cost-of-waiting and similar are `method` rows | blocks (`figure`, or `term` class `method`) |
| an assessment of a named individual | `paraphrase`, group `assessment` | blocks |
| small talk | `paraphrase`, group `personal-life`, only with a person reference | the planted case carries a named person and a `personal-life` cue and blocks; a second planted case of small talk with no person and no cue is a known limit and passes, marked `limit` |
| third parties named in passing | only through `exclusions.md` or the wall | known limit: the planted case passes, marked `limit`; the same name listed in the record's `exclusions.md` blocks in a second case |
| a hypothetical about a named person leaving | `paraphrase`, group `departure` | blocks |
| the seller's own internal account structure | the `seller-account` rule: the names of `never_show_workspaces[]`, `default_build_account.slug` and `github_account` from `settings.json` block as literals (with the separators of X32), and the ids of those workspaces and that account block even inside a link | blocks |
| a health or nationality remark about an absent person | `paraphrase`, group `health-identity` | blocks |

A planted case marked `limit` is in the fixture so that the outcome is asserted and a later change is seen; the README states the limit and names the authoring rule that guards it (call-intake keeps small talk and asides out of the client-safe block, X38).

**Reason.** A§:916 lists the three categories among what the lint blocks, and SF:88 says the lint enforces "what a string rule can reach"; the cue-and-person rule is the narrowest string rule that reaches them, and BP:158.30 asks for every category planted with a twin. Fail safe: a false block costs a rewrite and the allowlist answers a client's own vocabulary. The `seller-account` rule reads only `settings.json`, which L10 allows.

**Follow-up.** *Build:* step 5 (`paraphrase`, the vocabulary groups, `seller-account`). *Test:* L103, L234, L236 to L238, L246 to L248; the fixture asserts each outcome above. *Touch-up:* SF:84 names A§'s three categories (section 5, item 5); the embedded groups may later move into `leak-terms.txt` as shipped classes (section 5, item 10).

### X07 One user's firm in a shipped file

**Decision.** Nothing is built from SF:86's sentence. The fixture's phonetic pair is an invented firm name and an invented-for-the-purpose ordinary English word whose phonetic key equals it (X32), so the rule is proved without describing any user's firm (PLAN §8.11). SF:86 is reworded at the user's word as a case the rule handles: "A firm name may sound like a common word, so the string list is backed by a phonetic-variant rule with a whitelist of legitimate uses."

**Reason.** A12 and A22 keep anything user-specific out of shipped files; SF:86 describes one user.

**Follow-up.** *Build:* step 4 (the pair). *Test:* L54, L261. *Touch-up:* SF:86 (section 5, item 6).

### X08 The command forms

**Decision.** Six subcommands and one global flag. The launch is `[interpreter, <plugin>/scripts/leak_lint.py, (--record <client folder>), <command>, flags...]`; `--record` is global, comes before the command, and defaults to the current folder (W91). The record is any folder holding `CLIENT.md`, under `clients/` or under `archive/`.

| Command | Flags | Needs | Reads | Writes | Rules |
|---|---|---|---|---|---|
| `scan` | `[--strand <NNN>]`, `[--spans]`, `[<path> ...]` | record, `settings.json` | the paths, or, with none, every existing `strands/*/drafts/` and `strands/*/deliverables/handoff/` (one strand's with `--strand`); the lists; the record's sets; the index and the folder names under `clients/` and `archive/` | nothing | by mode (below) |
| `payload` | `--strand <NNN>`, `--kind <kind>`, `--file <path>`, `[--spans]`, all but `--spans` required | record, `settings.json` | the payload file, the lists, the record's sets, the index and folder names | nothing | every rule, the wall included |
| `blueprint` | `--strand <NNN>` required, `[--spans]` | record, `settings.json` | that strand's `solution/blueprint.md`, the lists, the record's sets, the index and folder names | nothing | every rule, the wall included; glossary text exempt from the run rule only |
| `wall` | `--text <text>` required | record | the record's own-set files, the index and folder names | nothing | the wall alone |
| `terms` | `<folder>` required, positional | `settings.json`; no record | every file under the folder, the index and folder names, the lists | nothing | the wall's digests and slugs against every entry, and the firm rule (X31) |
| `index` | none | record | this record's files and the index | `<home>/clients-index.json` only | none |

- `scan` modes, chosen by the path and reported in the output as `mode`: a `SUMMARY.md` directly under `strands/<id>/` is `summary` (X37); a `.md` file under `calls/`, or a `document-summary/1` snapshot under `inputs/`, is `client-safe-block` (X38); every other file is `full`. A folder is walked recursively (X35). `blueprint` reports mode `blueprint`.
- Every path handed to `scan`, `payload` or `blueprint` must resolve inside the record folder (W91, X22); a path outside it is exit 3 naming it. `terms` takes a folder outside any record by design.
- `--strand` takes a three-digit short id; an id with no `strands/<NNN>-*` folder is exit 3. A `scan` path under `strands/<id>/` takes its strand from the path, and a `--strand` that disagrees with it is exit 3.
- `--spans` adds a `span` to each blocking finding (X23).
- No command takes an account id, a token or a workspace (L10).

**Reason.** A§:357 lists the actions, mixing subcommands and flags; PLAN §7.8 (nodded) reads subcommands with the wall always on inside `payload` and `blueprint`, and A§:922's "runs on every payload and every planned name" is met by running it inside them. W91's frame is the precedent for `--record` and for inputs inside the record.

**Follow-up.** *Build:* step 5 (`scan`, `payload`, `blueprint`, the frame); step 6 (`wall`, `terms`, `index`, the wall inside the others). *Test:* L20 to L22, L32, L189. *Touch-up:* A§5.4:357's subcommand column reads `scan`, `payload`, `blueprint`, `wall`, `terms`, `index` (section 5, item 2).

### X09 Unpinned record shapes the lint reads

**Decision.** Step 3 pins these shapes in `record-map.md` under `Pinned: leak` (section 4.1), and WP7's templates follow them:

- **The client-safe block.** An opening line that reads exactly `<!-- client-safe:start -->` and a closing line that reads exactly `<!-- client-safe:end -->`, each alone on its line (surrounding spaces ignored). A file may hold several blocks one after the other. An opening mark with no closing mark, a second opening mark inside an open block, or a closing mark with no opening mark makes the whole file exempt nothing, and the lint reports one `warn` naming the file and the line (rule `copied-run`, class null; problem "client-safe marks not well formed; nothing in this file is exempt"). A malformed mark never exempts more than a well-formed one (L97).
- **The glossary.** In `solution/blueprint.md`, the same form with `<!-- glossary:start -->` and `<!-- glossary:end -->`, with the same malformed-mark rule.
- **Conflict rows.** In a call summary and in a document snapshot, every line under a level-2 heading that reads `## Conflicts` (letter case ignored), up to the next heading of level 1 or 2, or the end of the file. A missing heading means no conflict rows. Over-reading here only adds blocks.
- **`exclusions.md` rows.** Under a level-2 heading `## Exclusions`, every line that starts with a hyphen and a space is a row: the term, then optionally a space and one bracketed list of `key: value` pairs separated by semicolons. The keys are `kind` (`name`, `term` or `figure`), `added` (a date), `by` and `source`. When `kind` is absent, a term the figure parser reads as a number is a figure and any other is a term. A row whose term is empty is exit 3 naming the file and the line. Lines outside the heading, comments and blank lines are ignored.
- **`allowlist.md` rows.** Under a level-2 heading `## Allowlist`, the same row form with the keys `ok` (the user's words, or `yes`), `date` and `class`. A row without a non-empty `ok` clears nothing and is reported as a `warn` (rule `allowlist`). The `class` key is informative; what a row may clear is set by X10 and LT:27.
- **The blueprint's client-facing text.** The text under level-2 headings numbered 1 to 15 (`## 1`, `## 1.`, `## 1 Title` up to `## 15 ...`), each up to the next level-1 or level-2 heading, plus every prompt block of RM:136 (`### Prompt <KEY>` and its first fenced `text` block) wherever it sits. A blueprint with no numbered level-2 heading is exit 3 for `blueprint` ("cannot find sections 1 to 15").

**Reason.** PLAN §7.9 (nodded) has WP4 pin them now, as WP3 pinned the element-key table; A§:920 says the rest of a snapshot "its marks, conflicts and markers" stays inside the rule, and RM's blueprint row says sections 1 to 15 feed the bundle. Explicit open and close marks make an unclosed block exempt nothing, which is the fail-safe reading; a heading-delimited conflict section may only over-read, which is also safe.

**Follow-up.** *Build:* step 3 (the pins); step 5 (the readers). *Test:* L92, L94 to L97, L102, L163, L271; the fixture's planted records carry each shape. *Owed elsewhere:* WP7's `call-summary.md`, `document-summary.md`, `exclusions.md`, `allowlist.md` and blueprint templates carry these forms (section 6).

### X10 Per client or per strand

**Decision.** A payload, a blueprint check or a scan is checked against the exclusions of every strand of the record (`strands/*/solution/exclusions.md`) and against the allowlist of its own strand only (`strands/<NNN>-*/solution/allowlist.md`). The strand is `--strand` for `payload` and `blueprint`, and the path's strand for `scan`; a record-level file (none of the v1 scan targets is one) has no strand and nothing in it is cleared. What an allowlist row may clear: a `term` finding of class `method` (shipped or local), of the embedded vocabulary groups `internal-vocabulary` and `sales-framing`, and a `paraphrase` finding by its cue phrase (X06). It never clears the firm, `plugin`, `assistant`, `pain-ids`, `markers`, `id-patterns`, `local` or `seller-account` classes, a figure, a split figure, a copied run, a quote, an exclusion, a wall hit, a credential or an internal note (L114 to L119). A row matches a finding when its term equals the matched text after the normalisation of X28. A cleared finding is reported with severity `caution`, its rule and class kept, and `cleared_by` naming the row's file and line. A row that names something a row may not clear leaves the block in place and adds one `warn` (rule `allowlist`, "this class is never cleared by an allowlist").

**Reason.** PLAN §8.7 (nodded) and RM:42 to 43 place both files per strand; "do not show this" is the client's word about the client, so every strand's exclusions apply. LT:27 and A§:920 set what a row may clear; the embedded groups are vocabulary rules in A§:920's sense.

**Follow-up.** *Build:* step 5. *Test:* L43, L44, L113 to L119, L121, L264. *Touch-up:* none.

### X11 "Client-derived figures" and "internal files"

**Decision.** The lint builds five sets from the record on every run, reading files fresh (nothing is cached or copied into the record, A§:922): **F**, the record's numbers (split into cost figures and record numbers by X25); **R**, the internal-run sources of the copied-run rule; **Q**, the client quotes; **D**, the names the record publishes into its index entry (X26); **O**, the record's own set for the wall (X27). A file is read when its extension is `.md`, `.txt` or `.docx` (X35); `.json` files of the record are never read for these sets. The table says which set each part of the record feeds.

| Part of the record | F | R | Q | D | O |
|---|---|---|---|---|---|
| `CLIENT.md`, `meetings.md`, `log.md` | yes | yes | no | yes | yes |
| `research/**` | yes | yes | yes | yes | yes |
| `calls/*.transcript.txt` (raw) | yes | yes | no | yes | yes |
| `calls/*.md` outside the client-safe block | yes | yes | yes | yes | yes |
| text inside a well-formed client-safe block (calls and snapshots) | yes | no | yes | yes | yes |
| `inputs/` raw files the lint can read (`.txt`, `.docx`, and a `.md` whose front matter is not `document-summary/1`) | yes | no: the client-document text, the exemption source | no | yes | yes |
| `inputs/` raw files it cannot read (`.pdf`, images, spreadsheets) | not read; not exit 3, because they are exemption sources and not inputs to check, and a missing exemption only adds blocks | | | | |
| `inputs/*.md` snapshots outside the block | yes | yes; their `[Q/doc]` extracts are also client-document text | yes | yes | yes |
| conflict rows (X09) | yes | yes, and a run found there blocks even where it matches client-document text (X36) | yes | yes | yes |
| `strands/*/` Markdown: `STRAND.md`, `SUMMARY.md`, `readiness.md`, `close-out.md`, every `solution/*.md` but the blueprint, `versions/*/*.md` but the blueprint copies | yes | yes | yes | yes | yes |
| the blueprint (`solution/blueprint.md`, `versions/*/blueprint-r*.md`): sections 1 to 15, the prompt blocks and the glossary (X09) | no | no | no | no | yes |
| the rest of the blueprint | yes | yes | yes | yes | yes |
| `solution/exclusions.md` | its figure rows | no | no | its rows feed `terms` | yes |
| `solution/allowlist.md`, `live/live-map.md` | no | no | no | no | yes |
| `strands/*/drafts/`, `strands/*/deliverables/`, `.work/`, every `.json` | no | no | no | no | no |

- A client figure from a client document is a client figure with the document as its source (A16), so readable raw inputs feed F.
- The client-facing parts of the blueprint feed no set but O: they are what reaches monday, the session copies them into payloads, and their invented sample values must not block their own payloads. A client figure or a copied run that reaches them is caught when `blueprint` checks them against the other sets.
- `drafts/` and `deliverables/` feed nothing, so a leak sitting in a draft never makes itself "this record's" for the wall or a source for its own run.
- `.work/` holds backups of older versions and intake reports derived from the raw transcripts, which F and R already read.
- A file the table says to read that cannot be read or decoded is exit 3 naming it (L202).

**Reason.** PLAN §7.11 (nodded) reads every file but client documents, `drafts/` and the exempt blocks; A§:916 and A§:920 give the exemptions; A16 (AM:122 to 133) makes a document's figure a client figure; RM's blueprint row says sections 1 to 15 feed the bundle, so they are client-facing text and not an internal source.

**Follow-up.** *Build:* step 5 (F, R, Q); step 6 (D, O). *Test:* L45, L46, L78, L202; a record variant with one figure in `calls/` and one in `inputs/` (both in F) and one run in `drafts/` (not in R). *Touch-up:* A§:920 states that the blueprint's client-facing sections are not an internal source for the run rule (section 5, item 15).

### X12 The client's tool categories

**Decision.** The vocabulary is shipped in `leak-terms.txt` as fifteen counted classes, one per category, each named `tool-category-<name>` (the rows are in section 4.2). The script counts any class whose name starts with `tool-category-` and never reports a single hit of one. The assertion, rule `tool-categories`, fails (blocks) a sentence that hits three or more distinct category classes when its paragraph holds no proper noun:

- A paragraph is a block of text between blank lines; a heading is a paragraph of its own; each payload string is split the same way. A sentence ends at `.`, `!` or `?` followed by whitespace or the end, and at every line break, so a list item and a table row are each a sentence.
- A proper noun is a token that starts with an upper-case letter, is not the first token of its sentence, is not `I`, and whose lower-case form is in neither the common-word list nor the category rows; or an all-capital token of two to six letters that is not a category row and not in the embedded stop list of common acronyms (X26). monday's product words (`monday`, Work Management, CRM, Service, Dev, Vibe) are never proper nouns for this rule.
- Two categories in a sentence, or three spread over three sentences, pass (L108, L109); a paragraph with a proper noun is outside the assertion (L110).
- It runs in `scan` in every mode, in `payload` and in `blueprint`, and not in `terms`, `wall` or `index`, which check client inputs rather than client-facing text (X31).

**Reason.** PLAN §8.6 (nodded) chose a shipped vocabulary under a counted class, fail-safe over precise, because the record pins no list of the client's tools; one class per category needs no new row syntax in LT:17 to 29. A§:918 and BP:158.25 set the count and the scope.

**Follow-up.** *Build:* step 3 (the classes); step 5 (the assertion). *Test:* L104, L107 to L111, L260, L275. *Touch-up:* none. The vocabulary is listed for the user's nod (section 7, item 21).

### X13 The twenty-five arrays

**Decision.** Both counts hold and were checked here: the twenty-five arrays hold 400 prose entries, and the ten reviewed fixtures, s1 to s10, hold 158 of them (21, 15, 14, 15, 10, 19, 14, 16, 15 and 19), which is BP:448's figure. Section 3 maps every kind of leak they describe to a planted case and a twin. The grading on the keys stays with WP14's leak grader on the seed records at stage 4 (U2, L267, L268).

**Reason.** Q2 (a) binds; BP:323 and BP:448 give the grader to WP14.

**Follow-up.** *Build:* step 4 (`fixture-notes.md` lists each category of section 3 against its planted case). *Test:* L266 by inspection; L267 to L269 owed to stage 4. *Touch-up:* none.

### X14 The AI payload kinds, their fields and their stage

**Decision.** Built in stage 2 (U3). The walker is generic: it visits every string at every depth, object keys included, and every number (X22), so no field list limits it (L134). The field families are pinned for the fixture, the trace check and the report, as the union of BP:158.16, A§:914 and AI:10 to 59:

| Kind | Field families |
|---|---|
| `agent` | `name`, `role`, `role_description`, `goal`, `plan`, `user_prompt`, `knowledge_name` |
| `vibe_app` | `prompt`, `app_name` |
| `ai_column` | `name`, `prompt` |
| `workflow` | `name`, `description`, `step_text` |
| `sequence` | `name`, `step_text`, `recipient` |
| `webhook` | `url` |
| `automation` | `name`, `request_text` |
| `item_batch` | `name`, `seed` |
| `doc` | `name`, `markdown` |
| `workspace`, `folder`, `board`, `group`, `column`, `view`, `form`, `subitems`, `dashboard`, `widget`, `portfolio`, `project`, `publication`, `activation` | `name`, `description`, `label` |
| `generic` | every family |

The step-4 author builds one sample per kind with one planted leak per family and a clean twin (L160). Stage 4b adds only: the argument names the AI column, sequence and webhook probes establish (P-26 to P-28), agent jobs if the roster carries them (AI:11), and any field the P-19 to P-21 re-probes move. None changes the walker.

**Reason.** U3 binds over BP:51; the sources differ on fields, and the union is the fail-safe reading; AI:72 and AI:76 record the three unprobed kinds.

**Follow-up.** *Build:* step 3 (the pin); step 6 (the walker and the AI samples). *Test:* L142 to L161. *Touch-up:* BP:158's "(stage 4b)" for the AI kinds reads "built in stage 2; stage 4b adds what new probes change" (section 5, item 12).

### X15 Credentials

**Decision.** A rule `credential`, built into the script (its patterns between `# pinned: credential-shapes` and `# end pinned`, a region `lint_plugin.py` does not compare), blocks on every surface. It is never cleared. The shapes, each matched case-insensitively unless marked:

1. an authorisation scheme and a token: `\b(bearer|basic|token)\s+[A-Za-z0-9._~+/=-]{16,}`;
2. a secret pair: a key word (`password`, `passwd`, `pwd`, `pass`, `secret`, `token`, `api_key`, `api-key`, `apikey`, `access_key`, `access-key`, `client_secret`, `auth`) followed by optional spaces, `:` or `=`, optional quotes and a value of four or more non-space characters;
3. a URL with user info: `[a-z][a-z0-9+.-]*://[^/\s:@]+:[^/\s@]+@`;
4. a URL query parameter named `token`, `key`, `api_key`, `apikey`, `access_token`, `auth`, `secret`, `signature`, `sig`, `password`, `pwd` or `code` with a value of six or more characters;
5. known token shapes, case-sensitive: a three-part JSON web token (`eyJ` and three dot-separated base64url parts of ten or more characters each), an access key id (`AKIA` and sixteen capitals or digits), prefixed keys (`sk_`, `pk_` or `rk_` with `live_` or `test_` and sixteen or more alphanumerics), repository tokens (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` and thirty-six or more), chat-platform tokens (`xoxa-`, `xoxb-`, `xoxp-`, `xoxr-`, `xoxs-`) and a private-key header (`-----BEGIN` ... `PRIVATE KEY-----`);
6. a long mixed string outside a URL: thirty-two or more characters from letters, digits and `+/=_-` holding at least one digit, one lower-case and one upper-case letter.

URL parts are found as in X34; shapes 3 and 4 run on the URL text after percent-decoding.

**Reason.** BP:158.17 and A17 (AM:118: "a prompt never carries a credential") name the rule though A§:916's list does not; AMENDMENTS outranks the gap in A§. PLAN §7.15 (nodded) adds a credential class. It lives in the script because step 3's edit of the shipped list is limited (brief) and a credential shape is a pattern, not vocabulary. Shape 6 trades some false blocks (a pasted data string) for catching tokens no prefix names, which is the fail-safe side.

**Follow-up.** *Build:* step 5. *Test:* L76, L155, L156, L263; one invented sample per shape, each with a twin. *Touch-up:* A§9.6:916 adds "credentials (token and key shapes, authorisation headers, secret pairs, URLs carrying user info or a token)" to what the lint blocks (section 5, item 7).

### X16 Nothing records that the lint passed

**Decision.** Every output carries `inputs`, one object per file the lint read, in path order, each `{"file": <record-relative POSIX path, or home-relative as "<home>/...">, "sha256": <mmb_common.sha256_file>}`, the record files read for the sets included; a file looked for and absent is listed with `"state": "absent"` and no hash. `payload` also carries `args_digest`: the sha256 of `json.dumps(<the parsed payload>, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` encoded as UTF-8, so a hook that sees the tool input can recompute it from the object it is about to send, whatever spacing the session used. Both are present on every exit code that printed findings, exit 1 included (L210). `ledger.py` is not changed.

**Reason.** PLAN §7.16 and §8.10 (nodded); BP:252 puts the lint between `ledger.py intent` and the call; L276 keeps `ledger.py` byte-equal.

**Follow-up.** *Build:* step 5. *Test:* L31, L210. *Owed elsewhere:* WP13's hook, or a later ledger field, compares `args_digest` with the tool input before a write (section 6).

### X17 The pain-id patterns

**Decision.** Kept as shipped for this run: `P`, `N`, `S`, `O`, `C` with one or two digits and `R1` to `R12` block, and an allowlist cannot clear them (LT:27, A§:920 "never ... ids"). A collision blocks and is reported with class `pain-ids` (L59). The fixture's twins avoid these tokens. The cost is real: an IT service desk's "P1" priority, a severity "S1", a mask grade "N95" and a licence class "C1" cannot be written into a client's workspace without rewording. A narrowing is proposed for the user's word (section 5, item 9): an allowlist row may clear one exact pain-id token that is the client's own vocabulary, with a caution, the row naming the token and carrying the user's OK, while every other id stays unclearable. It needs A§:920's "never ... ids" to be amended, so it is not built now.

**Reason.** LT:130 to 143 and A§:920 are clear, and keeping them is the fail-safe reading; only the user can amend A§:920.

**Follow-up.** *Build:* step 5 (as shipped). *Test:* L58, L59, L114. *Touch-up:* section 5, item 9.

### X18 `tools/agnostic_sweep.py` does not exist yet

**Decision.** Until WP16 builds it, two checks stand in. The fixture README carries a closed list of every capitalised name and every firm rendering the fixture uses, each marked invented. `test_leak_fixture.py` fails on a capitalised token in any fixture file (outside the README's own prose) that is neither in that list, nor in the common-word list, nor at the start of a sentence. Step 4b's trace check reads the list against the rule that every name is invented. When `agnostic_sweep.py` exists, it runs over `tests/fixtures/leak/` as well (WP16).

**Reason.** PLAN §7.18 and §8.11 (nodded); A12 and BP:158.30 require invented names.

**Follow-up.** *Build:* step 4. *Test:* L217. *Owed elsewhere:* WP16 sweeps the fixture (section 6).

### X19 No word list in the standard library

**Decision.** The script embeds about a thousand common English words, lower case, between `# pinned: common-words` and `# end pinned`, written by the step-5 author as a frequency-ordered list of ordinary words (function words, common verbs, nouns and adjectives), plus about sixty monday and work words in the same region (board, item, items, status, group, column, owner, date, timeline, dashboard, view, form, automation, workflow, update, task, project, team, client, customer, report, request, file, doc, due, priority, stage, deadline, and the like). English only in v1. The filter:

- A six-word stretch counts toward the copied-run rule only when at least two of its six tokens are outside the list. A number is always outside the list. So a run is "made mostly of common words" when five or six of its six words are common. The constant is `RUN_MIN_DISTINCT = 2`, held beside the list.
- The same test applies to the near-copy windows of X24 (two of eight).
- It does not apply to the quote rule, to figures, markers, ids, exclusions, credentials, the firm rule or the wall (L99).
- The step-4 fixture carries a common-word run (ignored) and a twin run of client vocabulary (blocks); if the step-5 author tunes the constant on the fixture, the new value is logged in this file under "Added by the review fixes" with its reason.

**Reason.** PLAN §8.5 (nodded) embeds the list; A§:920 says "mostly" and leaves the threshold to the fixture. Five of six is the plain reading of "mostly"; the quote rule is left unfiltered because a client's eight-word sentence is evidence whatever words it uses, which is the fail-safe side.

**Follow-up.** *Build:* step 5. *Test:* L98, L99, L259, L274. *Touch-up:* none.

### X20 The headless half

**Decision.** Owed to stage 4, listed and counted apart in the checklist, never failed: L179 (the three `index` moments, WP8 and WP12), L199 (`terms` at release, WP16), L209 (callers stop on exit 3, WP9, WP13, WP8, WP12), L267 and L268 (the twenty-five keys and the two non-removals, WP14's grader), and L269 (the seed home's index, WP14). WP14's seed home must carry an index entry for every seed record under its `clients/`, built by `leak_lint.py index`, or every headless payload exits 3 under X30 (section 6).

**Reason.** PLAN §7.20 and Q2 (a); BP:321 and BP:448 give the seed home and the grader to WP14.

**Follow-up.** *Build:* step 9 lists them. *Test:* L270. *Owed elsewhere:* section 6.

### X21 The slugs of the other folders

**Decision.** The slug check stays, beside the hashes. Every folder directly under `<home>/clients/` and `<home>/archive/` other than this record's own is a slug, read from the folder listing only (no file inside it is opened). Each slug is split at its hyphens into tokens and goes through the same candidate test as an index name (X27, X28), so a payload holding "fernhollow-supply", "Fernhollow Supply" or "fernhollowsupply" for an invented slug `fernhollow-supply` blocks with rule `wall`. Archived folders are checked too, so a closed client stays walled even with no entry. The slug is never written into the index in plaintext: the entry's key is its hash (X02). This record's own slug never blocks on the wall.

**Reason.** A§:922 and SF:90 add the slug check, and Q1 (a) only widens what the index holds; keeping both is the fail-safe reading. A§:440's "never plaintext" is met by hashing the key.

**Follow-up.** *Build:* step 6. *Test:* L190, L191, L176 (no slug string in the index bytes). *Touch-up:* none.

### X22 How a payload is handed in, and how a kind is named

**Decision.**

- **The file.** The payload file is the tool call's input exactly as the session will send it, as one JSON value (an object or an array), written by the session inside the record, under `.work/strands/<NNN>-<topic>/` by convention (W91). It is read with `utf-8-sig`; invalid JSON is exit 3 naming it. There is no wrapper schema and no standard-input form.
- **The kind.** `--kind` takes one of the pinned kinds: the twenty-three object types of `Pinned: ledger` (`workspace` to `activation`) and `generic`. Any other value is exit 3, so a misspelt kind is seen at once rather than walked under the wrong field families. The audit's live object names and any text that fits no kind go in as `generic`.
- **The walk.** Every string value at every depth is checked, every object key is checked as a string, and every JSON number is rendered as its decimal text and checked by the figure and number rules only. A string that begins with `{` or `[` and parses as JSON (monday's `column_values` is often a JSON string) is checked as a string and also walked as JSON. Booleans and null are skipped. A finding's `field` is a path such as `$.steps[2].text` or `$.column_values<json>.text_1`; a key's own path ends in `<key>`.
- **The relation to `ledger.py intent`.** The session runs `intent`, writes the payload file, runs `payload`, and sends exactly the parsed object it handed over; `args_digest` (X16) lets a hook prove it. Nothing in `ledger.py` changes.
- **No string at all.** A payload with no string and no number exits 0 with an empty findings list (L159).

**Reason.** W91 requires every handed input to lie inside the record so findings name record-relative paths; one canonical object is what a later hook can compare (PLAN §7.16). Reusing the ledger's object types keeps one vocabulary across the two scripts; L158 allows exit 3 for an unknown kind.

**Follow-up.** *Build:* step 3 (the kinds in `Pinned: leak`); step 5 (the reader); step 6 (the walker). *Test:* L32, L131, L133, L134, L158, L159, L161; a `column_values` JSON string with a planted name blocks at its inner path. *Owed elsewhere:* WP9's write path writes the payload file and passes `--kind` (section 6).

### X23 Redaction against "never edit"

**Decision.** "Written but not defaulted" is met by `--spans` on `scan`, `payload` and `blueprint`: each blocking finding gains `span: {"start": <n>, "end": <n>}`, character offsets into the decoded text of that file (or that payload string) before normalisation. Nothing in the plugin passes `--spans`; nothing is removed or edited by any command, with or without it. The lint's output does not read the A11 fields of the record (L212). If A11-3 is ever answered with redaction, the caller that applies it works on a copy and uses the spans; the lint stays "block and report, never edit".

**Reason.** PLAN §8.9 (nodded); A§:357 and A§:916 forbid edits; BP:158.33 asks only that the behaviour be written; BP:19 keeps A11-3 open with no default.

**Follow-up.** *Build:* step 5. *Test:* L211, L212. *Touch-up:* none.

### X24 What a word, a run and a quote are

**Decision.**

- **Words.** The text is normalised as X28 says (format characters removed, NFKC, look-alikes folded, case folded, diacritics stripped). A word is a maximal run of letters and digits; an apostrophe inside a word is removed ("don't" is `dont`); a hyphen, a slash and every other mark are separators; Markdown marks (`*`, `_`, `#`, `|`, `>`, backticks) are separators. So case, punctuation, line breaks, table cells and emphasis never break a match.
- **A copied run.** Six or more consecutive words of the checked text equal to six consecutive words of an R source (X11), subject to the common-word filter (X19) and the exemptions (X36). Each maximal stretch is one finding, reported at its first word, naming the R file it was found in (the first in path order). Five words never block on this rule (L89).
- **A near copy.** An eight-word window of the checked text that equals an eight-word window of an R source in seven of its eight positions (one word changed) is also a `copied-run` block, with `near: true` in the finding, under the same filter and exemptions. A run with words reordered, or broken by two changes within eight words, is a known limit for the review to probe.
- **A client quote.** In the Q sources (X11), a line that holds one of the five quote markers (`[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]`, `[Q/doc]`): the text between double quotation marks (straight or curly) on that line, or, where the line has none, the line's text with the marker, the location forms (LT:164 to 166) and the speaker label before a colon removed. A stretch of eight or more consecutive words of the checked text equal to eight consecutive words of a quote is a `quote` block, whether or not the copied-run rule also fires or is exempt there; where both fire on one stretch, one finding is reported, rule `quote`. Seven words never block on this rule.
- **`[Q/doc]` extracts are quotes.** So a stretch of eight or more words of a client document blocks when that stretch was quoted as evidence in a snapshot, while six or seven words of it pass (the run exemption, X36).

**Reason.** A§:916 and BP:158.3 to 4 give the lengths and nothing finer; matching on normalised words is the fail-safe reading that the review's bypasses (re-punctuation, emphasis, case) cannot get round; the near-copy check goes beyond A§'s literal rule to meet the one-word-changed bypass PLAN §3 names for step 7, and is listed for the user's nod.

**Follow-up.** *Build:* step 5. *Test:* L88 to L90, L251, L252; a twin with one word changed in a six-word run passes, and the same change inside an eight-word copy blocks as a near copy. *Touch-up:* none.

### X25 Figures: formats, floor, and what counts

**Decision.**

- **Reading a number.** After normalisation (full-width digits fold under NFKC), the parser reads: digits with an optional decimal part; thousands separators `,`, `'` or a narrow space between a head of one to three digits and groups of exactly three (a plain space there is a split rendering, below); a currency sign (`$`, `£`, `€`, `¥`) or code (`USD`, `GBP`, `EUR`, `CAD`, `AUD`, `NZD`, `CHF`) before or after, with or without a space; a magnitude suffix `k`, `K`, `m`, `M`, `mm`, `bn` or a word `thousand`, `million`, `billion`, `grand`, with or without a space; English number words (units, teens, tens, `hundred`, `thousand`, `million`, `billion`, `a` for one before a magnitude, `and`, hyphens), `point` decimals ("one point two million"), and "half a million" or "a quarter of a million"; and a percent sign, "percent" or "per cent". A lower-case `m` attached to a number with no currency is read both ways (million and plain), and both readings are checked.
- **Value and precision.** Each number has a value and a precision, the unit of its last written digit: `45,000` is exact; `45k` and "forty-five thousand" have precision 1,000; `1.2M` has 100,000; `130.8k` has 100.
- **Not numbers.** Well-formed dates (`2026-10-17`, `17/10/2026`, `10/17/2026`, `17.10.2026`, "17 October 2026", "October 17"), times (`14:30`), a year 1900 to 2099 written alone, versions (`v0.1`, `1.2.3`) and ordinals in a list (`1.`, `2)`) are not figures and are not warned. A year becomes a figure only when written with a currency sign or a magnitude.
- **Record side (F).** In the F sources (X11), a number of value 10 or more is a **cost figure** when its sentence holds a cost cue, and a **record number** otherwise. The cost cues are a currency sign, code or word (dollar, buck, pound, euro, grand) and the cost words, embedded between `# pinned: cost-cues` and `# end pinned` (cost, price, priced, pricing, rate, loaded, salary, wage, pay, paid, fee, budget, spend, threshold, signs, signature, sign-off, invoice, invoiced, billed, billing, revenue, margin, profit, loss, lost, write-off, written off, credit, refund, penalty, overrun, saving, worth, value, contract, renewal, discount, payback, bleed, upside, hourly, per hour, an hour, day rate, and their plurals). A cost-cued percentage is a cost figure of kind percent.
- **Payload side.** A number v with precision p matches a figure F when the difference is less than the larger of the two precisions (so, for an invented figure of 318,460, `318k` and `$319k` match it and `317k` does not). Then:
  - a match with a cost figure of 1,000 or more is a `figure` block, in any rendering;
  - a match with a cost figure from 10 to 999 is a `figure` block when the payload's own sentence holds a cost cue or the number carries a currency sign or a rate suffix (`/hr`, `/h`, "an hour", "per hour"); otherwise it is a `record-number` warning ("matches a client figure with no cost word beside it");
  - a percentage matches only a cost figure of kind percent, and blocks;
  - a match with a record number is a `record-number` warning: the "flag, do not remove" group, reported and kept (X39);
  - any other number of 10 or more is a `number` warning (A§:920 "other numbers");
  - a number below 10 is never reported.
- **Exclusion figures.** A figure row of any `exclusions.md` matches in every rendering with the same tolerance, at any value, as an `exclusion` block (L87).
- **Split renderings.** A run of digit groups joined by single spaces, dots, hyphens, slashes, underscores, Markdown table pipes, emphasis marks or a line break, read as one number, and number words broken by a line break or a hyphen at a line end, are split renderings. A split rendering that matches a cost figure or an exclusion figure is a `split-figure` block (the first structural assertion, L105); one that reads as a date or matches a record number is a `split-figure` warning; any other is ignored (L106).
- **In a link.** The figure and split-figure rules run on URL text after percent-decoding; number warnings skip URLs.
- **The wall's figures.** An entry's `figures` list holds each cost figure of 1,000 or more whose exact value has three or more significant digits, and each exclusion figure of any value, hashed as `f:<n>e<k>`: k = 0 is the exact value, and for each k from 1 to 9 the value divided by 10^k, both truncated and rounded, wherever that keeps three or more significant digits (exclusion figures: one or more). A payload number of precision 10^k is tested as `f:<round(v / 10^k)>e<k>`. Percentages are not in the wall. So two clients' round thresholds (an invented `65,000` in each record) never collide on the wall, while a distinctive invented `318,460` does, in every rendering of the five.
- **Limits.** Colloquial digit-by-digit forms (invented examples: "three-one-eight", "three eighteen", "three-twenty-ish" for 318,460) and approximate wording far from the figure ("about a third of a million") are not matched; the fixture's README states them.

**Reason.** A§:916 and BP:158.2 give the five formats and A§:920 the warnings; A§:916 says "client-derived **cost** figures", so a number with no cost cue is a volume or process fact, the "flag, do not remove" group of BP:158.22 and BP:448, reported and kept. Q1 (a) asks for a floor so that a common number shared by two clients does not block; three significant digits keeps round thresholds out of the wall while every rendering of a distinctive figure stays in. The tolerance follows the keys' own pairing of a truncated magnitude form with an exact total, read as a category (KEY). Both readings of an ambiguous `m` are the fail-safe side.

**Follow-up.** *Build:* step 5 (parser, F, payload side, split renderings); step 6 (the wall's figures). *Test:* L78 to L87, L105, L106, L175, L184, L249, L250; a 5 × 5 test of record format against payload format (L84). *Touch-up:* none.

### X26 Where a record's own names live

**Decision.** A record's `names` list (D) is harvested, not read from a roster, and no person is told from a product (every kind of name is a name):

1. `CLIENT.md`'s `name` value, and its `slug` split at hyphens: always included, whatever the filters below say.
2. In every D source (X11), every maximal run of one to four tokens that each begin with an upper-case letter, where `of`, `and`, `&`, `the` and `de` may join two capitalised tokens inside a run. Each run and each of its contiguous sub-runs is a candidate.
3. Every all-capital token of two to six letters (an acronym, such as a client's customer written as initials).
4. Every e-mail address: its local part split at dots, hyphens and underscores, the local part fused, and each domain label of three or more letters other than the last.
5. Kept, after the normalisation and suffix stripping of X28: a candidate of two or more tokens, unless every token is in the stop list; a single token of three or more characters, or an acronym of two letters, that is in neither the common-word list nor the stop list.
6. The stop list, embedded beside the common words: the days and months; monday's product and feature words; the plugin's own vocabulary (the shipped list's `plugin`, `assistant`, `method` and `markers` rows); titles (Mr, Mrs, Ms, Dr); role acronyms (CEO, CFO, COO, CTO, VP, HR, IT, PM, PMs, QA); and common acronyms (CRM, ERP, SOP, API, ETA, PDF, KPI, ROI, SLA, FAQ, UK, US, USA, EU, ID, OK, AM, TV, BI).
7. Each kept candidate is hashed in its spaced form, and a candidate of two or more tokens also in its fused form.
8. `phonetic` holds the hash of the phonetic key (X32) of each kept candidate of two or more tokens, and of each kept single token of seven or more letters.

`terms` holds every term row of every strand's `exclusions.md`, through the same normalisation, spaced and fused. Names sit in a header (a participant line, an export header) as often as in the body, so headers are read like any other line.

**Reason.** Q1 (a) says "as the record names them" and no source names a roster; A§:918's "names harvested from the body rather than the roster" and "alias-map entries that are ordinary words" are traps against reading a roster only. Excluding a common single word from the digest (while keeping it inside a multi-word name) stops an alias such as an ordinary word blocking every other client's prose, and the own-record test of X27 catches what over-harvesting adds.

**Follow-up.** *Build:* step 6. *Test:* L169 to L174, L185; the planted record carries a name only in a body line, a customer as initials and in full, a partner whose name is two ordinary words, and an e-mail address.

### X27 How a payload's terms are extracted for the wall

**Decision.** One function, `wall/1`, cuts any text into candidates, on both sides: when `index` builds an entry (with the filters of X26), when the lint builds this record's own set O (no filters), and when a payload, a draft, a blueprint section, a `--text` or a `terms` file is checked (no filters). After the normalisation of X28 the candidates of a text are:

1. every token of three or more characters, and every token of two letters written in capitals in the checked text (initials);
2. every run of two, three and four adjacent tokens, across commas and line breaks but not across a sentence end or a blank line;
3. fused forms: wherever adjacent tokens are joined by a non-space separator (`-`, `.`, `_`, `@`, `/`, `&`, `+`, or none, as in a camel-case word), the concatenation of each contiguous run of two to four of them, so `fernhollow-supply.example`, `j.doe@fernhollow` and `FernhollowSupply` all yield fused candidates; tokens joined by plain spaces are not fused, so the ordinary words "on track" never become a product called "Ontrack";
4. phonetic keys of the candidates of type 2, and of single tokens of seven or more letters.

A candidate of the checked text **blocks** with rule `wall` when its hash is in another entry's `names`, `terms` or `phonetic` list, or it equals another folder's slug form (X21), **and** the same candidate (its normal form, or for a phonetic hit its key) is not in O. O is built fresh from this record's O sources (X11) by the same function, held in plaintext in memory, never written. Numbers are tested as X25 says, against other entries' `figures` and O's numbers. A one-word client name that is an ordinary word blocks wherever it is not also in this record; since a record nearly always holds the ordinary word, that case passes in practice, while a rare or invented one-word name blocks.

**Reason.** A hash can be compared only with the hash of a candidate, so the candidates must cover every shape A§:918 plants: case, possessive and comma-split names (normalisation and type 2), a partner name of two ordinary words (type 2), a product fused from a word and a preposition (type 3 with its spaced twin passing), an e-mail with its separator lost (type 3), a name corrupted in a hypothetical (type 4), and names in a quotation (types 1 and 2). BP:158.19's "and not this client's record" is the own-set test; reading the whole record but `drafts/`, `.work/` and JSON for O keeps a leak in a draft from clearing itself.

**Follow-up.** *Build:* step 6. *Test:* L182 to L188, L192 to L194, L279; the fixture's wall cases (section 3). *Touch-up:* none.

### X28 Normalisation, and what protects the hashes

**Decision.** The normalisation `wall/1`, used by every rule that compares words (the wall, the firm and phonetic rules, exclusions, runs, quotes, the allowlist match), in this order:

1. remove every character of Unicode category Cf (zero-width spaces and joiners, the byte-order mark, the soft hyphen, bidirectional marks);
2. NFKC (full-width letters and digits, ligatures and non-breaking and narrow spaces fold to their plain forms);
3. fold look-alike letters: a table embedded between `# pinned: confusables` and `# end pinned` maps the Cyrillic and Greek letters that look like Latin ones (such as Cyrillic а, е, о, р, с, у, х, і, ј, ѕ and Greek α, ε, ι, κ, ν, ο, ρ, τ, υ, χ, upper and lower case) to the Latin letter;
4. case fold, then NFD and drop the combining marks (diacritics);
5. tokenise as X24 says, dropping a trailing possessive `'s` or `’s` before apostrophes are removed;
6. for names, terms and slugs, drop trailing legal-suffix tokens: inc, incorporated, llc, ltd, limited, plc, gmbh, corp, corporation, co, company, lp, llp, sa, ag, bv, nv, pty, pte, srl, oy, ab;
7. the spaced form joins tokens with one space; the fused form joins them with nothing.

Positions in findings are reported in the original text: the normaliser keeps a map from each normalised character back to its original offset.

The hash is `sha256(<prefix> + <form>)` over UTF-8, cut to its first 32 hex characters, with the prefixes `n:` (names and terms), `p:` (phonetic keys), `f:` (figures) and `s:` (the entry key). No salt. The index lives under the user's own home, beside every client's folder in plaintext, so hashing keeps names out of the file and out of anything copied from it, not out of a reader who can already open the folders; an unsalted digest also lets WP14 build a seed index that every run reproduces. This limit is stated in the API note.

**Reason.** Q1 (a) and A§:440 say "normalised" and nothing more; PLAN §3 names the bypasses step 7 will try (look-alikes, zero-width and non-breaking characters, full-width digits, case, possessives, diacritics), and one normalisation on both sides of the hash closes them together. `tools/lint_plugin.py`'s `normalise_name` (NFKD, lower case) is the precedent, widened to keep digits and word boundaries.

**Follow-up.** *Build:* step 5 (the normaliser); step 6 (the hashes). *Test:* L169, L188; one test per step above with a planted name in each disguise. *Touch-up:* none.

### X29 One shared file written by many records

**Decision.** `index` holds the home mutex, `mmb_common.record_mutex(<home>)`, which is `<home>/.work/record.mutex`, a zero-byte file created on first use and never deleted. Under it, `index` reads the index fresh, replaces only this record's entry, and writes the file in place with `mmb_common.write_file(<home>/clients-index.json, text, root=<home>, backup_dir=<home>/local/backup)`, so the old bytes are first copied to `local/backup/clients-index.json.<UTC stamp>` (G39's place for home files). It writes nothing when the new bytes equal the old (X46). There is no temporary file and no rename (A§5.3, scripts never rename over a file). A reader takes the same mutex while it reads the index when `<home>/.work/record.mutex` already exists, and reads without it otherwise, so a reader never creates a file in the home (L09); a torn read is invalid JSON and therefore exit 3, never a pass. No entry is ever removed: an entry whose record no longer exists stays and keeps that client walled.

**Reason.** A§:440 rules out a cross-client lease file, and a short-held lock on one home file is not one; `record_mutex` and `write_file` are WP2's tested primitives, and `mmb_common.py` stays unchanged (L276). A§5.3 forbids deletes and renames.

**Follow-up.** *Build:* step 6. *Test:* L177, L181; two `index` runs from two records in two threads leave both entries; a reader during a write sees either file whole or exits 3. *Touch-up:* A§5.3:346 and RM:76 add `<home>/.work/record.mutex` (the index's mutex) and `local/backup/` for the index's backups (section 5, item 11).

### X30 An absent index while other records exist

**Decision.** An absent `clients-index.json` reads as empty. Then a coverage check runs, in every command that runs the wall (`payload`, `blueprint`, `scan` in full and client-safe-block modes, `wall`, `terms`): every folder directly under `<home>/clients/` or `<home>/archive/`, other than this record, that holds a `CLIENT.md` (tested with `is_file`; nothing inside is opened) must have an entry whose key is the hash of its folder name. If any lacks one, the run is exit 3 with `error` naming no folder: problem "<n> other client records under the home have no index entry, so the wall cannot see them", expected "run leak_lint.py index from each of those records, then run this again". A fresh home, where this record is the only one, passes the check, so the first run of a new user is unaffected. `index` refuses (exit 3) a record whose `CLIENT.md` slug differs from its folder name, so a key always matches its folder.

**Reason.** A§:920 and BP:158.32 fail closed; reading as empty (SF:90, G58) is safe only while there is nobody to wall off. Naming the folders would carry other clients' slugs into this session's output, which A20's wall exists to prevent; the user can list their own home.

**Follow-up.** *Build:* step 6. *Test:* L48 (an empty home passes), L198; a home with a second record folder and no index exits 3, and passes once `index` has run from it. *Owed elsewhere:* WP14's seed home (X20).

### X31 What `--terms` runs

**Decision.** `terms <folder>` needs no record and reads `local/settings.json` (exit 3 without it, as every command that runs the firm rule). It runs:

- the wall's digests of **every** entry of the index (there is no own record, so nothing is skipped), names, terms, phonetic keys and figures, by `wall/1` (L196: one shared function);
- the slug check against every folder under `<home>/clients/` and `<home>/archive/`;
- the coverage check of X30;
- the firm rule: `firm.name`, `firm.renderings[]`, the local `class: firm` rows, the phonetic rule and its whitelist.

It does not run the shipped list's rows, the markers, the ids, the runs, the quotes or the two assertions: `shared/` legitimately holds the plugin's own vocabulary (LT:14 to 15), and those rules guard client-facing text, not client inputs. It reads every file under the folder recursively: `.md`, `.txt`, `.json`, `.py`, `.yml`, `.yaml`, `.csv`, `.html`, `.xml`, `.toml`, `.ini` and `.cfg` as UTF-8 text, and `.docx` as X35 says. It skips only `.git/` and `__pycache__/` folders and the system files `.DS_Store`, `Thumbs.db` and `desktop.ini`; any other file it cannot read is exit 3, since an unread file proves nothing. The output carries `entries_compared` and `slugs_compared`; with no index and no other folders both are 0 and the run is exit 0 (L198). At the build guard (A§8.6 step 9) the skill runs `blueprint --strand` on the strand, not `terms`: `terms` is the release check over a folder.

**Reason.** BP:114 says `terms` "proves nothing from any client input is in it", which is the digests, the slugs and the firm name; L197 keeps the shipped vocabulary from reporting itself. A§8.6 step 9 names `--terms` at the build guard without saying over what, and the blueprint check is the one that proves the frozen text.

**Follow-up.** *Build:* step 6. *Test:* L195 to L198 (over a copy of `shared/` with one planted client name, and over the real `shared/`); L199 owed to WP16. *Touch-up:* A§8.6 step 9 reads `leak_lint.py blueprint --strand <id>` (section 5, item 2).

### X32 The phonetic rule, "comma-split" and the whitelist's home

**Decision.**

- **The key (part of `wall/1`).** For a word: normalise (X28) and keep letters a to z only; at the start, rewrite `kn`, `gn`, `pn` to `n`, `wr` to `r`, `ps` to `s`, `wh` to `w` and `x` to `s`; then, left to right, rewrite `ph` to `f`, `ck` to `k`, `sch` to `sk`, `tch` and `ch` to `X`, `sh` to `X`, `th` to `0`, `dg` to `j`, `qu` to `kw`, `x` to `ks`, `gh` before a consonant or at the end to nothing, `c` before `e`, `i` or `y` to `s`, other `c` to `k`, `g` before `e`, `i` or `y` to `j`, `q` to `k`, `z` to `s`, `v` to `f`; map `b` and `p` to `P`, `f` to `F`, `k` and `g` to `K`, `j` to `J`, `s` to `S`, `t` and `d` to `T`, `l` to `L`, `m` and `n` to `M`, `r` to `R`, keeping `X` and `0`; drop `w`, `h`, `y` and the vowels, except that the first letter of the word is kept (a vowel as `A`, `w` as `W`, `h` as `H`, `y` as `Y`); collapse runs of one symbol. A key of a run is the words' keys joined by one space; a fused run has one key. For example the ordinary word `harbour` and an invented name `Harbur` both key to `HRPR`.
- **What it matches.** The firm rule takes as phonetic sources `firm.name`, each `firm.renderings[]` entry and each `phonetic:` row of the local list's `firm` class; every other class's `phonetic:` rows are sources for their own class. For a source of n words, the candidates are the windows of n and n + 1 adjacent words, spaced and fused, and every single token, each of four or more letters. A candidate blocks (rule `phonetic`, the source's class) when its key equals the source's key, or when its folded letters are within a Damerau–Levenshtein distance of 1 of the source's (sources of five to seven letters) or 2 (eight or more letters). Below five letters only the key counts.
- **The whitelist.** A `whitelist:` row in the local list's `firm` class clears a firm phonetic hit wherever it sits in that class; in any other class a `whitelist:` row clears hits of the `phonetic:` row directly above it (LT:25). A whitelist row clears a hit when the hit's matched text equals the row after normalisation, or when the hit lies inside an occurrence of the row in the text (a row "harbour master" clears the word inside it). A whitelist never clears a literal rendering: the exact firm name and each rendering block whatever the whitelist says.
- **Comma-split and the other spellings.** For every literal row of two or more words (shipped and local, all classes) and every firm rendering, the gaps between the words match one or more of: whitespace, a line break, `,`, `.`, `-`, `_`, `/`, `|` and `·`. For firm renderings, `seller-account` values, exclusion terms and the shipped `plugin` class, the fused form (no gap at all) also matches. So "Example, Firm", "Example-Firm", "Example\nFirm" and "ExampleFirm" all block for an invented rendering "Example Firm"; a legal suffix after a comma ("Example Firm, Inc.") blocks because the rendering is inside it.
- **Limit.** No rule reaches a misspelling that changes the key and also sits beyond the edit distance; the fixture states it.

**Reason.** A§:918 and LT:23 to 26 name the rule and give no algorithm, and the standard library has none, so the key is pinned here to be built and tested; the edit distance catches the misspellings a key misses. RM:76's `firm` has no whitelist field, so the firm's whitelist can live only in the local list. Taking only the whitelist (and not the common-word list) as the exemption is the fail-safe side: a false phonetic block is fixed by one whitelist row, which BP:158.28 and BP:158.29 ask for anyway.

**Follow-up.** *Build:* step 5. *Test:* L51 to L54, L228, L261; a unit test of the key on twenty invented words with their expected keys, written by the step-5 author from this entry. *Touch-up:* none.

### X33 The local list and a row that does not parse

**Decision.** The shipped list and the local list share one parser and one set of rules:

- a row above the first `class:` line of the local list belongs to class `local`, which blocks and is never cleared; in the shipped list such a row is exit 3;
- a `class:` name is letters, digits and hyphens; any other is exit 3 naming the file and the line;
- a `re:` row that does not compile, or (local list only) one holding a quantified group that itself contains a quantifier, such as `(a+)+` or `(\w*)*`, is exit 3 naming the file and the line, the second as "a pattern that can run for a very long time";
- a `whitelist:` row outside the `firm` class with no `phonetic:` row directly above it (blank and comment lines aside) is exit 3;
- a `phonetic:` or `whitelist:` row with an empty term is exit 3;
- any other line is a literal, so a mistyped prefix becomes a harmless literal;
- a zero-byte local list adds nothing; an absent one reads as empty and is listed in `inputs` with `"state": "absent"`, with no warning, because `settings.json`, which is required, carries the firm rule; a local list that exists and cannot be read or decoded is exit 3.

**Reason.** A§:920 and BP:158.32 fail closed on anything the lint cannot apply as written; G58 writes a zero-byte local list at `home init`, and an older hand-built home without it loses nothing the required settings file does not supply.

**Follow-up.** *Build:* step 5. *Test:* L38, L200, L201; one case per bullet.

### X34 Links

**Decision.** A link is the target of a Markdown link or image (`[text](target)`, `![alt](target)`), the value of an HTML `href` or `src` attribute, an angle-bracket autolink, or a bare URL beginning `http://`, `https://` or `mailto:`, up to the first whitespace or closing bracket. Only the eight-digit monday id row of `id-patterns` (LT:190) skips link targets: the id is masked in a copy of the line before that one row runs. The link's visible text is ordinary text. Every other rule runs on link targets too, on the text as written and on a percent-decoded copy: the firm and phonetic rules, `seller-account` (whose workspace and account ids block even inside a link, X06), exclusions, the wall, paths (a `file://` URL to a home folder blocks), credentials, figures and markers. A webhook's `url` field is a link and is checked the same way: its ids pass, and user info, a token parameter, a path, an excluded term or another client's name in it block. A look-alike that is not one of these forms (`hxxp://`, a URL without a scheme) is not a link, and its ids block.

**Split ids.** Outside links, digit groups of two to four digits joined by single spaces, hyphens or dots whose digits total eight or more (an id written `1234 5678` in an export header, or a phone number in groups) block under the same id row, reported with class `id-patterns`, unless the groups read as a well-formed date or time (X25). This reaches A§:918's "identifier that appears only in a header" in its spaced and hyphenated forms, and a person's phone number with it.

**Reason.** LT:169 to 171 strip URLs before the id class only; BP:158.8 says ids "outside links"; BP:158.16 and BP:158.17 put the webhook's URL under the credential and path rules. Exempting only the one row the sources exempt is the fail-safe reading.

**Follow-up.** *Build:* step 5; the webhook samples in step 6. *Test:* L72 to L74, L155, L257.

### X35 `.docx` parts and the extensions a scan takes

**Decision.**

- **Parts.** A `.docx` is read in memory with `zipfile` (L130): `word/document.xml` is required; `docProps/core.xml`, `docProps/app.xml`, `docProps/custom.xml`, `word/header*.xml`, `word/footer*.xml`, `word/footnotes.xml`, `word/endnotes.xml` and `word/comments.xml` are read when present, and a missing one is no error. The output lists `parts_read` for each file. Text: the `w:t` texts of each `w:p` paragraph are joined with nothing (a word split across runs reads as one word, L128), `w:tab` gives a space, `w:br` and `w:cr` a line break, each paragraph a line; in a property part each element's text is one line, named by its element (`dc:creator`, `Company`). XML entities are decoded by the parser. A finding names the part and the paragraph number.
- **Guards.** A part holding `<!DOCTYPE` or `<!ENTITY` is exit 3 (a Word part never needs one, and this closes entity-expansion attacks); a member over 50 MB uncompressed, an archive over 200 MB uncompressed in all, or a member over 1 MB compressed more than 100 to 1, is exit 3. No member name is ever used as a path.
- **Missing body.** A file that is not a zip archive, or one with no `word/document.xml`, is exit 3 naming it (L129).
- **A folder scan.** `scan` walks a folder recursively and reads `.md`, `.txt`, `.docx` and `.json` (a `.json` file is walked as a payload of kind `generic`). It skips only the system files `.DS_Store`, `Thumbs.db` and `desktop.ini`. Any other file, a hidden one included, is exit 3 naming it with expected "a file the lint can read (.md, .txt, .docx, .json); move this one out of the folder or convert it": a draft the lint cannot read cannot be marked ready (A§:920).

**Reason.** BP:158.14 names the body and the two property parts; headers, footers, notes, comments and custom properties carry text to the client just as well, and reading them is the fail-safe side. A§:920 makes an unread client-facing file a stop.

**Follow-up.** *Build:* step 5. *Test:* L123 to L132, L225; the tests build each `.docx` from XML strings with `zipfile` (PLAN §8.3), one with a leak in a header and one in a custom property.

### X36 The exempt blocks, and a run found in two places

**Decision.** The exemptions are from the copied-run rule only (A§:916, A§:920). Inside a client-safe block, the glossary or copied client-document text, every other rule still applies when that text is checked or copied: markers, ids, figures, the firm, exclusions, the wall, the quote rule, the paraphrase rule (L163). For a six-word stretch of checked text the run rule decides in this order:

1. the stretch is in a conflict row (X09): it blocks, even where it also matches client-document text, because a disputed statement is not the client's settled word (BP:158.12);
2. the stretch matches client-document text (the readable raw files of `inputs/` and the `[Q/doc]` extracts, X11): it passes the run rule, even where an internal file also holds it, since every snapshot's extract repeats the document's words;
3. the stretch is in any other R source: it blocks;
4. otherwise it passes.

Text inside a client-safe block or a glossary is simply not an R source, so a stretch copied from one passes unless the same words also stand in an R source outside the block. The quote rule applies to all of them (X24), so an eight-word client quote inside a client-safe block still blocks when copied.

**Reason.** A§:920 lists the exemptions and keeps "the rest of a snapshot, its marks, conflicts and markers" inside the rule; BP:158.11 and BP:158.12 require the same run to pass from the document and to block from the conflict rows, which only the precedence above gives; the narrow reading of BP:158.9 and 10 ("passes" as passes the run rule) is the fail-safe one.

**Follow-up.** *Build:* step 5. *Test:* L46, L91 to L96, L163, L251, L258.

### X37 `SUMMARY.md`

**Decision.** `scan` of a `SUMMARY.md` directly under `strands/<id>/` runs in mode `summary`: the copied-run rule (with the near-copy check, the common-word filter and the exemptions), the quote rule, and the two structural assertions (L104). Its R sources are every R source of X11 except every `SUMMARY.md` of the record, its own and the other strands' (the designed carry-over between strands, already linted). Markers, ids, method terms and the firm rule are not run in this mode: the summary is an internal file that legitimately holds them, and every later client-facing text built from it is checked in full. Exit codes as usual.

**Reason.** BP:158.31 and LT:14 name the two rules "because it feeds later client-facing text"; BP:158.26 runs the assertions on every scan.

**Follow-up.** *Build:* step 5. *Test:* L165. *Owed elsewhere:* `record.py strand summary` (WP2) is not changed; the session runs the scan before asking the user's yes on the summary (WP8 or WP12 skill text, section 6).

### X38 The client-safe block, at the moment it is written

**Decision.** `call-intake` runs `scan calls/<stem>.md` (or `scan inputs/<stem>.md`) after writing a call summary or a document snapshot. The lint runs in mode `client-safe-block`: it checks only the text inside the file's well-formed client-safe blocks, with every rule except the copied-run rule (the block is exempt from it): the paraphrase rule and the quote rule among them, so the three categories and long quotes are kept out when the block is written. A file with marks that are not well formed is exit 3 naming the line, since the lint cannot tell what is client-safe. A file with no block exits 2 with one `warn` ("no client-safe block in this file").

**Reason.** A§:916: the three categories "are also kept out of the client-safe block at the moment `call-intake` writes it, because that block is exempt from the copied-run rule"; one mode of `scan` meets it with no new command.

**Follow-up.** *Build:* step 5. *Test:* L103 (the block-mode cases), L94, L95. *Owed elsewhere:* WP8's `call-intake` runs the scan and treats exit 1 and exit 3 as stops (section 6).

### X39 "Flag, do not remove" and "caution"

**Decision.** Three severities: `block` (exit 1), `warn` and `caution` (exit 2 when no block). The "flag, do not remove" group is the volume and process numbers of the record: they are record numbers (X25), and a payload number that matches one is a `record-number` warning, reported for the user's decision and never removed, since the lint edits nothing (L120). Other numbers are `number` warnings. A `caution` is a finding an allowlist row cleared (X10): its rule and class stay, it carries `cleared_by`, and it says "kept as the client's own word". A warning says something the user should look at; a caution says something was cleared on the user's own allowlist row. Both are listed under `findings` with their severity, and the counts by severity are in `counts`. The s2-shaped case is built as invented text: an ordinary method word that is also an invented client's own word for a work item, with an allowlist row (caution, exit 2) and without one (block, exit 1).

**Reason.** BP:158.22 and BP:158.23 describe the two non-removals as behaviours, and BP:448 says the group "belongs in client-facing documentation"; reporting without blocking is the only way to both report and keep it. A§:920 makes other numbers warnings.

**Follow-up.** *Build:* step 5. *Test:* L113, L120, L121, L122, L262.

### X40 What an "internal note" is

**Decision.** An internal note is any of: text copied from an internal file (the copied-run and near-copy rules, X24); a `method` term or a term of the embedded `internal-vocabulary` group (X06, clearable as vocabulary); and, under the rule `internal-note`, which is never cleared:

- the line "Internal: never client-facing", and the phrases "never client-facing", "internal only", "not for the client" and "note to self";
- a flat front-matter line (a lower-case key, a colon and a double-quoted value at the start of a line), or a `---` line followed by a `schema:` line;
- a transcript speaker label, "Speaker" and a number.

These are embedded between `# pinned: internal-notes` and `# end pinned`. Everyday words that internal notes also use ("to do", "if asked", "do not show") are not on the list, because a client's own procedure text uses them.

**Reason.** BP:158.17 and AM:118 (A17) name internal notes without defining them; the marks of the record's own internal files are the one shape a string rule can recognise for certain.

**Follow-up.** *Build:* step 5. *Test:* L77, L156, L263.

### X41 The finding shape, the `ok` field and the wall's finding

**Decision.** Every command prints one JSON object through `mmb_common.json_text` (UTF-8, LF, no byte-order mark):

```text
{
  "ok": <true on exit 0 and exit 2; false on exit 1 and exit 3>,
  "command": "<name as typed>",
  "verdict": "clean" | "warnings" | "blocked" | "could-not-run",
  "mode": "full" | "summary" | "client-safe-block" | "blueprint"   (scan and blueprint only),
  "strand": "<NNN>" | null,
  "inputs": [ {"file", "sha256"} or {"file", "state": "absent"} ... ],
  "args_digest": "<hex>"   (payload only),
  "findings": [ ... ],
  "counts": {"block": n, "warn": n, "caution": n},
  "error": {"file", "field", "problem", "expected"}   (exit 3 only)
}
```

- **`ok` never reads as a pass on exit 3.** It is true only on exit 0 and exit 2, which is where a caller may go on. This departs from W91's `ok` ("the exit code is not 1") on purpose, because a gate that fails closed cannot have a field a caller might read alone that says true when the lint did not run; `verdict` says the same thing in a word. A usage error prints `"command": null`, as in `ledger.py`. Below Python 3.9 the script prints the envelope with `"ok": false` and exits 3 before importing anything else (L206).
- **A finding** is `{"file", "field", "problem", "expected", "rule", "class", "severity", "line", "column", "match", "source"}`, plus `part` for a `.docx` part, `near` for a near copy, `cleared_by` for a caution and `span` with `--spans`. `file` is record-relative in POSIX spelling (L12), `<home>/...` for a home file, or the folder-relative path under `terms`. `field` is the payload path (X22), or `line <n>` in a text file, or the part and paragraph in a `.docx`. `line` and `column` are numbers from 1 (null in a payload). `match` is the checked text's own matched words, cut to 80 characters. `source` is the record-relative file a set came from (the R file of a run, the call holding the quote, the file the figure was harvested from), or null.
- **A wall finding** names the checked text's own match and the rule `wall`, with `class` set to `name`, `term`, `figure` or `slug` and `source` null. Its problem reads "matches a <name, term or figure> of another client record under the home". It never names the other record, its slug, its key or anything only that record holds (L29, L192): naming the other client would carry that client into this client's session, which the wall exists to stop.
- **Order.** Inputs in the order given, a folder's files in sorted POSIX path order, then by position, then by rule name; two runs on the same bytes print the same bytes (L30).
- **Exit 3 after findings.** Findings found before a failure may be printed; the exit code stays 3 and the verdict `could-not-run` (L208). Exit precedence is 3, then 1, then 2, then 0.

**Reason.** G10 gives the four parts and the codes; BP:158.32 makes exit 3 a stop for every caller, so the field a caller reads must agree with it; A20 forbids carrying one client into another's build.

**Follow-up.** *Build:* step 5 (the frame); step 6 (wall findings). *Test:* L21, L23, L27, L29, L30, L192, L205, L206, L208; a test asserts `ok` is false on every exit-3 case of L200 to L207.

### X42 Limits

**Decision.** A text input over 20 MB, a payload file over 20 MB, a payload nested deeper than 64 levels (counting JSON walked inside strings), and the `.docx` limits of X35 are each exit 3 naming the file and the limit. `re:` rows run line by line; a line longer than 10,000 characters is run in windows of 10,000 characters overlapping by 200. The walker is iterative, not recursive. The local list's patterns pass the static check of X33. Any unexpected exception inside any rule is exit 3 with the envelope (L205). No time cap is set in-process: with patterns checked and inputs capped, a run is bounded by its input.

**Reason.** A lint that fails closed must turn every input it cannot finish into exit 3 (A§:920, BP:158.32); the caps are far above any record's real files (RM's budgets are hundreds of lines).

**Follow-up.** *Build:* step 5. *Test:* L128, L130, L205; one test per cap with an injected limit.

### X43 Files, tests and interpreters

**Decision.** Three test files, as PLAN §8.1 nodded: `tests/unit/test_leak_lint.py` (step 5: the frame, the lists, the rules on one text, the readers), `tests/unit/test_leak_fixture.py` (step 4: the fixture's self-test and the grading of every planted case and twin), `tests/unit/test_leak_wall.py` (step 6: the wall, the index, the payload walker, `terms`). On macOS the suite runs under `/usr/bin/python3` (3.9 on this Mac, WP3's practice) and the newest installed Python 3, with `PYTHONDONTWRITEBYTECODE=1`; on Windows under `py -3.9` and the newest. The built sizes of the script and the tests are reported as facts beside BP:159's 540 and 460, which are estimates.

**Reason.** PLAN §8.1 and §9 (nodded); BP:156 names one test file, and three keep the steps from writing the same file.

**Follow-up.** *Build:* steps 4 to 6. *Test:* L14, L17 to L19. *Touch-up:* BP:156 lists the three test files (section 5, item 17).

### X44 The personal-names index

**Decision.** The lint does not read `personal-names-index.json` in v1. It is the agnostic sweep's local name list (BP:114, `tools/lint_plugin.py`'s `check_personal_names` already reads it), not one of the lint's inputs, and SF:88's "personal names absent from the SOP's role and approver tables" warning belongs to the v2 SOP (A19).

**Reason.** L10 limits the lint's reads under `local/` to two files, and A§:346 and A§:440 do not list the name index as a lint input; RM:76's "the lint's name list" is a stage-1 phrase.

**Follow-up.** *Build:* nothing. *Test:* L10 (the spy on opens). *Touch-up:* RM:76 calls it "the agnostic sweep's name list" (section 5, item 8).

### X45 Whether the wall runs on `drafts/`

**Decision.** Yes. `scan` runs the wall in modes `full` and `client-safe-block`, so a draft or a client-safe block holding another client's name, term or figure blocks with rule `wall`, as a payload does. Mode `summary` does not run it (X37).

**Reason.** A§:916 lists other clients' names among what the lint blocks on every surface A§:914 names, `drafts/` among them; A§:922 and BP:158.19 name payloads and planned names without excluding drafts, and the fail-safe reading takes the wider surface.

**Follow-up.** *Build:* step 6. *Test:* L279.

### X46 A time stamp in an index entry

**Decision.** Each entry carries `updated`, the UTC time of the write that last changed it, as `YYYY-MM-DDTHH:MM:SSZ` from `mmb_common.stamp("utc")` (the one clock, G40). `index` writes nothing when the entry's four lists are unchanged, so a rerun on an unchanged record leaves the file byte-equal and makes no backup (L177). The lint's printed output carries no local time.

**Reason.** G40 sets the form; a stamp that changes only with the content keeps reruns idempotent and still tells the user how fresh an entry is.

**Follow-up.** *Build:* step 6. *Test:* L177, L278 (the clock patched).

### X47 The callers and where fail-closed is proved

**Decision.** WP4 proves its own exits and states the rule for callers in `API-leak_lint.md`: exit 0 and exit 2 go on (the warnings and cautions are shown to the user); exit 1 stops that write, draft or blueprint stage until the text is changed; exit 3 stops it the same way and is never retried as if it had passed; the caller keeps the printed `inputs` hashes and `args_digest` with its record of the write. The callers, each proving its own side at stage 4 (section 6):

| Caller | Package | Command | When |
|---|---|---|---|
| account-build's write path | WP9 | `payload` | between `ledger.py intent` and every call (BP:252) |
| solution-blueprint | WP9 | `blueprint` | after the blueprint is drafted, before the card; and at the build guard (A§8.6 step 9) |
| the hook | WP13 | compares `args_digest` | before a write it can see |
| engagement | WP8 | `index` | after `record.py init` |
| call-intake | WP8 | `scan` (client-safe-block mode), `index` | after each saved call, document or email |
| solution-audit | WP10 | `payload --kind generic` | on live object names during the audit |
| client-closeout | WP12 | `scan`, `index` | `drafts/` again at close-out, then `index` before the move to `archive/` |
| the strand summary step | WP8 or WP12 | `scan` (summary mode) | before the user's yes on `SUMMARY.md` |
| release checks | WP16 | `terms` | over `shared/` (BP:114) |
| the headless runner and leak grader | WP14 | all | on the seed home |

**Reason.** BP:158.32 gives the rule to every caller, and the callers are other packages' files.

**Follow-up.** *Build:* step 6 writes the API note's caller paragraph (L277). *Test:* L209 and L277 owed to stage 4; WP4's own exits by L200 to L208.

---

## 3. The category map

This section is what step 4 builds the trap fixture from and what step 4b checks it against. It states categories from the rule (D24): every kind of leak the twenty-five arrays describe, written as a kind and never as an instance. No figure, name, phrase or quote of any array, transcript or call is in it, and none may enter the fixture. Every planted case and twin is invented text in the same shape.

How to read the outcomes. **blocks**: exit 1 with at least one finding of the rule named. **warns**: exit 2, a `warn` of the rule named, no block. **caution**: exit 2, a `caution`. **limit**: no string rule reaches it; the planted case exits 0 or 2 with no block, the README names the limit and the authoring rule that guards it, and the test asserts that outcome so a change is seen. A **twin passes** when it has no blocking finding; a twin should exit 0 wherever its shape allows, and any warning it carries is named in the README.

### 3.1 The kinds of leak the arrays describe

| # | Category | Planted case (shape) | Clean twin | Rule | Outcome |
|---|---|---|---|---|---|
| K01 | Cost totals and their components, in every rendering, including a truncated or rounded magnitude form | a record call summary states an invented six-digit cost total beside a cost word; a draft and a payload carry it as bare digits, with separators, with a currency sign, with `k`, spoken, and in a truncated `k` form | the same sentences with an unrelated invented figure | `figure` | blocks (twin warns `number`) |
| K02 | Hourly and loaded rates | the record gives an invented two-digit rate "an hour, loaded"; a payload says "<n> an hour" | the same number in a sentence about minutes, no cost word | `figure` | blocks (twin warns `record-number`) |
| K03 | Cost inputs: hours and frequencies behind a cost figure | the record says a task "costs <n> hours a week"; payload A pairs that number with a rate; payload B states it alone | a process sentence with no number | `figure`; `record-number` | A blocks; B warns |
| K04 | Upside and opportunity figures | an invented revenue-at-stake figure beside "worth" or "upside" in the record, copied into a payload | an unrelated figure | `figure` | blocks |
| K05 | Write-off, loss, credit and penalty amounts | an invented write-off amount in the record, in a payload in `k` form | an unrelated figure | `figure` | blocks |
| K06 | Spend thresholds and signing limits | an invented round approval limit beside "signature" in the record, in this client's own payload | an order size that is in no record | `figure` | blocks (twin warns `number`) |
| K07 | Margin percentages and average values | an invented margin percentage beside "margin" in the record, in a payload as `%` | another percentage | `figure` | blocks (twin warns `number`) |
| K08 | Pricing material for the engagement: rates, day rates, payback, cost-of-waiting | the seller's invented day rate in the record, and a `method` row, in one draft line | a neutral next-steps line | `figure`; `term` (`method`) | blocks |
| K09 | The seller's placeholder or rejected figures | an invented placeholder rate the user's side spoke, in the record, copied into a payload | an unrelated figure | `figure` | blocks |
| K10 | Failure narratives told as stories | A: six words of the record's invented incident narrative in a draft; B: the same incident retold in new words with no cue | a neutral process description | `copied-run`; none | A blocks; B limit |
| K11 | Emotional and personal stakes | an invented named person and an `emotional` cue in one sentence | the same shape about a report being late | `paraphrase` (`emotional`) | blocks |
| K12 | Health, medical and personal-life detail | an invented named person and a `health-identity` cue; a second with a `personal-life` cue | the same shapes about a schedule | `paraphrase` | blocks |
| K13 | Stakeholder assessments and decision power, and titles set against what a person does | an invented named person and an `assessment` cue; a second about a title mismatch with no cue | the approval step described by team, not person | `paraphrase` (`assessment`); none | first blocks; second limit |
| K14 | Remarks by client staff about colleagues | an invented named person and a `colleague-remark` cue | the same shape about a tool | `paraphrase` (`colleague-remark`) | blocks |
| K15 | Objection text and adoption-risk remarks | A: eight words of an invented `[Q]` line in a call summary's body; B: eight words of an invented quote that sits inside the client-safe block; C: the objection paraphrased | seven words of the quote inside the block (the run rule is exempt there and the quote rule needs eight) | `quote`; `quote`; none | A blocks; B blocks; C limit; the twin passes |
| K16 | Alternatives in play and competitive context | an invented competing vendor listed in the record's `exclusions.md`, named in a payload | "another option was considered" | `exclusion` | blocks |
| K17 | Other clients' names, data and examples | the second planted record's name, a term of its exclusions and a distinctive figure, in the first record's payload | the same payload with this record's own names | `wall` | blocks |
| K18 | The seller's brand, plugin, assistant and tool names, and the seller's colleagues | the invented firm rendering, a `plugin` row, an `assistant` row, and an invented colleague name listed in the test local list | the same lines in neutral words | `term` (`firm`, `plugin`, `assistant`, `local`) | blocks |
| K19 | Method vocabulary, grades, gate and verdict words, pain and criterion ids, evidence and status markers | one line per class: a `method` row, a grade beside a criterion id, a pain id, the nine markers, `[found]` | look-alike ordinary text with brackets and no ids | `term` | blocks |
| K20 | Internal artefacts: record paths, file names, timestamps, line and cue numbers, intake and delivery vocabulary, alias tables, speaker labels | a POSIX path, a Windows path, a record file name, a timestamp location, `L142`-style and cue-style locations, an `internal-vocabulary` word, "Speaker 2" | ordinary words without separators or numbers | `term` (`id-patterns`, `markers`, `internal-vocabulary`); `internal-note` | blocks |
| K21 | Customer identities and customer personal data (names tied to failures, phone numbers, addresses, member data, access codes) | an invented customer in `exclusions.md` and an invented phone number in digit groups, in a seed value | "the customer's number is kept on the ticket" | `exclusion`; `term` (`id-patterns`, split id) | blocks; an address with neither is a limit, stated |
| K22 | Third parties' personal data and third parties named in passing | an invented outside contact named once in the record and in a draft; the same name in `exclusions.md` in a second case | the role named, not the person | none; `exclusion` | first limit; second blocks |
| K23 | Confidential commercial material: contract values, salaries, contract terms | an invented contract value beside "contract"; six words of an invented contract clause from a snapshot | neutral wording | `figure`; `copied-run` | blocks |
| K24 | Account, meeting and recording identifiers from export headers | an invented ten-digit id written in spaced groups, taken from a header line | a date and a time in the same line | `term` (split id) | blocks (twin passes) |
| K25 | Attendance remarks, small talk, banter and jokes | A: an invented named person with a `personal-life` cue; B: banter with no person and no cue | a scheduling sentence | `paraphrase`; none | A blocks; B limit |
| K26 | Names and figures seeded in a demonstration and narrated on screen, presented as client facts | an invented figure from an `[X]` line beside a cost word; an invented demo name from the same line | neutral sample data | `figure`; none | figure blocks; the name is a limit (it is in this record) |
| K27 | Claims by the seller or a previous seller, repeated as fact | six words of the claim copied from the record; the claim paraphrased | a plain statement of what was built | `copied-run`; none | copy blocks; paraphrase limit |
| K28 | Backlog framed as an upsell or expansion | a `sales-framing` phrase in a draft | "possible next improvements" | `term` (`sales-framing`) | blocks |
| K29 | Internal fit and risk judgements, scope-limit reasoning, the seller's commercial clock | a `method` row such as a fit phrase; an internal deadline paraphrased | neutral scope wording | `term` (`method`); none | first blocks; second limit |
| K30 | Name variants and identity artefacts (misheard spellings, coerced names) | a phonetic variant of the invented firm name; a phonetic variant of the second record's name | the whitelisted ordinary word | `phonetic`; `wall` | blocks (twin passes) |
| K31 | Sensitive asides on public-sector work | an aside with a `colleague-remark` cue and a person; an aside with neither | neutral item names | `paraphrase`; none | first blocks; second limit |
| K32 | Volume and process facts: the "flag, do not remove" group | the record gives an invented headcount; a draft states it | the same sentence with no number | `record-number` | warns, file unchanged (L120) |
| K33 | The client's own vocabulary that collides with a blocked word | an invented client work-item word equal to a `method` row, with an allowlist row; the same without the row | | `term` (`method`) | caution with the row; blocks without |
| K34 | Client document text, and the same words in a conflict row | six words of an invented client document in a payload; six words of that snapshot's conflict row | | `copied-run` | document passes; conflict row blocks |
| K35 | Withheld figures that must not be reconstructed or estimated | a draft gives an estimate the record never states | | none | limit: the lint sees only figures the record holds |
| K36 | Measures of the seller's own delivery (talk share, delivery notes) | an `internal-vocabulary` word in a draft | neutral wording | `term` (`internal-vocabulary`) | blocks |

### 3.2 The trap categories of A§:918

Each is planted once with a twin (L226 to L248). The outcomes of the seven judgement categories are X06's.

| Trap category | Planted case (shape) | Rule | Outcome |
|---|---|---|---|
| case-varied organisation names | the invented firm rendering and the second record's name in capitals and in mixed case | `term` (`firm`); `wall` | blocks |
| possessive organisation names | both with `'s` and `’s` | `term`; `wall` | blocks |
| comma-split organisation names | both written "First, Second" and across a line break | `term`; `wall` | blocks |
| an identifier only in a header | an invented id that the record holds only in a raw transcript's header, in spaced groups | `term` (split id) | blocks |
| alias-map entries that are ordinary words | the second record's alias table maps a person to an ordinary word; the first record's draft uses that word in its everyday sense, and, in a second case, with the person's surname | `wall` | everyday use passes; with the surname blocks |
| names harvested from the body | a name the second record holds only in a body line | `wall` | blocks |
| a client's customers as an acronym | the second record's customer as initials | `wall` | blocks |
| a client's customers as a full name | the same customer in full | `wall` | blocks |
| the seller's own commercial terms | X06 | `figure`; `term` | blocks |
| dates whose digits are split | a date written with its digits spaced | `split-figure` | warns; the twin, the date written whole, exits 0 |
| an assessment of a named individual | X06 | `paraphrase` | blocks |
| small talk | X06 | `paraphrase`; none | one blocks; one limit |
| third parties named in passing | X06 | none; `exclusion` | one limit; one blocks |
| a partner name that reads as two ordinary words | the second record's partner, two capitalised ordinary words | `wall` | blocks; the two words apart in a sentence pass |
| a client's name corrupted inside hypotheticals, in a file with no header | the second record's name misspelt in a hypothetical, in a headerless draft | `wall` (phonetic) | blocks |
| a product name that is an ordinary word fused to a preposition | the second record's fused product name | `wall` (fused) | blocks; the two words written apart pass |
| two vendors' names substituted for each other | vendor A in `exclusions.md`; a payload names A where the record speaks of B | `exclusion` | blocks; the twin naming B passes |
| an e-mail address with its separator lost | the second record's invented contact address written without its dot or `@` | `wall` (fused) | blocks |
| several client first names inside one quotation | three first names of the second record inside quotation marks | `wall` | blocks |
| a counterparty, its part-owner and its tools in one sentence | the second record's counterparty and part-owner by name, with three tool categories | `wall`; `tool-categories` (only proper-noun-free text) | blocks on the wall; the twin with roles and two categories passes |
| a hypothetical about a named person leaving | X06 | `paraphrase` (`departure`) | blocks |
| the seller's own internal account structure | an operational workspace name from the test `settings.json` | `seller-account` | blocks |
| a health or nationality remark about an absent person | X06 | `paraphrase` (`health-identity`) | blocks |

### 3.3 The rule cases of BP:158

Each of L249 to L265 is planted as PLAN §4.1 lists them; the rules and outcomes are fixed by the entries above: the five formats and the split rendering (X25), the six-word run in three placements (X36), the eight-word quote and its seven-word twin (X24), the nine markers (X03), the ids (X17, X34), both path spellings and a mixed one (X03), HTML comments (LT:189), the eight-digit id in and out of a link (X34), the three exempt blocks beside the same text outside them (X09, X36), the common-word run (X19), the tool-category sentence at three and at two (X12), the firm's renderings, phonetic variants, whitelisted uses and the sound-alike ordinary word (X32), the flag group and the caution case (X39), one credential per shape of X15, one internal note per form of X40, an excluded term in each standard field family (X14), the allowlist rows that try to clear a figure, a quote, a run, a marker, an id, an exclusion and a wall hit and clear nothing, and the one that clears a `method` term (X10), and a payload sample per kind with a planted leak per field family (X14).

### 3.4 What the map cannot prove

As PLAN §4.2 and L222 say: that these categories are the whole set; that a client's real vocabulary behaves like the invented one; the false-positive rate on real client text, which stage 4's seed records and the twenty-five keys begin to measure; and anything about a language other than English. The `limit` rows above are known gaps, not passes.

---

## 4. For step 3: the shared edits

Step 3 makes exactly the four edits below, and no other. Paths are relative to the plugin repository, `monday-master-builder/`. Copy each block as it stands, byte for byte, with LF line endings and no byte-order mark. Do not add, remove or reword anything, and do not add backticks anywhere in the new record-map section beyond those shown: `tools/lint_plugin.py` compares every backticked token of that section with the script, so a stray backtick becomes an error once `leak_lint.py` exists. Log what was done in `rebuild-workspace/build/wp4/shared-edits.md`. When done, run `python3 tools/lint_plugin.py` from the plugin repository (0 errors expected; the `leak` pair is reported as not yet present, a warning) and the whole unit suite under both Pythons (all tests pass, as before).

### 4.1 `plugins/monday-master-builder/shared/record-map.md`: the `Pinned: leak` section

Insert the block below as a new level-2 section directly after the `## Pinned: ledger` section, that is after its last paragraph (the one that ends "A delete is refused for every kind.") and before the heading line that starts `## ` and names `intake-report/1`. Leave one blank line before the new heading and one after the block's last line. This one section holds every pinned token and every pinned record shape of WP4 (X02, X09, X14, X22, X41).

```text
## Pinned: leak

The vocabulary and the record shapes that scripts/leak_lint.py reads and reports. Every backticked token in this section, and only these, is embedded between the pinned markers of scripts/leak_lint.py, and tools/lint_plugin.py asserts the two agree; until leak_lint.py exists the lint reports the pair as not yet present. The rules are described in ARCHITECTURE 9.6 and the WP4 decisions; this section pins the words and the shapes.

| Field | Values |
|---|---|
| evidence markers, all nine blocked in drafts and in every payload | `[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]`, `[Q/doc]`, `[X]`, `[E]`, `[I]`, `[A]` |
| payload kind | `workspace`, `folder`, `board`, `group`, `column`, `view`, `form`, `subitems`, `doc`, `dashboard`, `widget`, `automation`, `portfolio`, `project`, `workflow`, `agent`, `ai_column`, `vibe_app`, `sequence`, `webhook`, `item_batch`, `publication`, `activation`, `generic` |
| field family | `name`, `description`, `label`, `seed`, `markdown`, `request_text`, `role`, `role_description`, `goal`, `plan`, `user_prompt`, `knowledge_name`, `prompt`, `app_name`, `step_text`, `recipient`, `url` |
| block marks | `<!-- client-safe:start -->`, `<!-- client-safe:end -->`, `<!-- glossary:start -->`, `<!-- glossary:end -->` |
| headings the lint reads | `## Conflicts`, `## Exclusions`, `## Allowlist` |
| row keys | `kind`, `added`, `by`, `source`, `ok`, `date`, `class` |
| exclusion row kind | `name`, `term`, `figure` |
| index | `clients-index/1`, `schema`, `hash`, `normalisation`, `entries`, `updated`, `names`, `phonetic`, `terms`, `figures` |
| index digest and normalisation | `sha256-128`, `wall/1` |
| severity | `block`, `warn`, `caution` |
| verdict | `clean`, `warnings`, `blocked`, `could-not-run` |
| scan mode | `full`, `summary`, `client-safe-block`, `blueprint` |
| rule | `term`, `phonetic`, `seller-account`, `figure`, `split-figure`, `copied-run`, `quote`, `exclusion`, `wall`, `credential`, `internal-note`, `paraphrase`, `tool-categories`, `number`, `record-number`, `allowlist` |
| wall finding class | `name`, `term`, `figure`, `slug` |
| class an allowlist row may clear | `method`, `internal-vocabulary`, `sales-framing`, `assessment`, `emotional`, `health-identity`, `departure`, `colleague-remark`, `personal-life` |
| counted class prefix | `tool-category-` |
| class of a local row above any class line | `local` |

The field families each payload kind plants in the trap fixture. The lint checks every string, every object key and every number of a payload whatever its kind; this table says where the fixture puts one leak per family.

| Kind | Field families |
|---|---|
| `agent` | `name`, `role`, `role_description`, `goal`, `plan`, `user_prompt`, `knowledge_name` |
| `vibe_app` | `prompt`, `app_name` |
| `ai_column` | `name`, `prompt` |
| `workflow` | `name`, `description`, `step_text` |
| `sequence` | `name`, `step_text`, `recipient` |
| `webhook` | `url` |
| `automation` | `name`, `request_text` |
| `item_batch` | `name`, `seed` |
| `doc` | `name`, `markdown` |
| `workspace`, `folder`, `board`, `group`, `column`, `view`, `form`, `subitems`, `dashboard`, `widget`, `portfolio`, `project`, `publication`, `activation` | `name`, `description`, `label` |
| `generic` | every family |

The record shapes the lint reads:

- The client-safe block of a call summary and of a document snapshot opens with a line that reads exactly `<!-- client-safe:start -->` and closes with a line that reads exactly `<!-- client-safe:end -->`, each alone on its line; a file may hold several blocks one after another. An opening mark with no closing mark, a second opening mark inside an open block, or a closing mark with no opening mark makes the whole file exempt nothing. The blueprint's client-safe glossary uses `<!-- glossary:start -->` and `<!-- glossary:end -->` the same way.
- Conflict rows are the lines under a level-2 heading `## Conflicts` in a call summary or a document snapshot, up to the next level-1 or level-2 heading.
- The rows of a strand's exclusions file are the lines under its level-2 heading `## Exclusions` that start with a hyphen and a space: the term, then optionally one bracketed list of pairs separated by semicolons, each pair written as the key, a colon, a space and the value. The keys are `kind` (one of `name`, `term` and `figure`; when it is absent, a term that reads as a number is a figure), `added` (a date), `by` and `source`. A row whose term is empty is an error. The rows of a strand's allowlist file have the same form under its level-2 heading `## Allowlist`, with the keys `ok` (the user's words, or yes), `date` and `class`; a row without a non-empty `ok` clears nothing.
- The blueprint's client-facing text is the text under its level-2 headings numbered 1 to 15, each up to the next level-1 or level-2 heading, and every prompt block of the element-key section above, wherever it sits.
- A payload is the tool input the session will send, written as one JSON file inside the record and handed over with its payload kind; a string that holds a JSON object or array is walked as JSON as well.
- The index, clients-index.json under the home: `schema` is `clients-index/1`; `hash` is `sha256-128`, the first 32 hex characters of a sha256; `normalisation` is `wall/1`; `entries` maps each record's key, the digest of its slug, to an object of `updated` (a UTC time) and four sorted lists of digests, `names`, `phonetic`, `terms` and `figures`. Nothing in the file is plaintext, and leak_lint.py index is its only writer.
```

### 4.2 `plugins/monday-master-builder/shared/leak-terms.txt`: the `[A]` row, the comment and the category classes

Three edits, in this order.

1. Change line 146 from

   ```text
   # The eight evidence markers of 7.5, the method's two names for them, the status markers,
   ```

   to

   ```text
   # The nine evidence markers of 7.5, the method's two names for them, the status markers,
   ```

2. Insert one new line, `[A]`, directly after the line `[I]` (line 155) and before the line `[found]`.

3. Append the block below at the end of the file, after the last line (`re: \[L1[4-8]\]`), with one blank line between that last line and the block's first line, and end the file with a single LF.

```text
# Tool categories (9.6, the second structural assertion). Every class below whose name starts
# with tool-category- is counted and never blocked: leak_lint.py fails a sentence that names
# three or more distinct categories in a paragraph with no proper noun, and a single hit is
# never reported. The rows are generic category words, never product names, and an allowlist
# has nothing to clear here.

class: tool-category-accounting
accounting system
accounting software
accounting package
bookkeeping software
general ledger
invoicing software
invoicing tool

class: tool-category-crm
crm
customer relationship management
contact database
sales pipeline tool

class: tool-category-erp
erp
enterprise resource planning

class: tool-category-spreadsheet
spreadsheet
spreadsheets
shared sheet
workbook

class: tool-category-scheduling
scheduling tool
scheduling software
scheduling app
booking system
rota tool
rostering software
dispatch software
calendar tool

class: tool-category-hr
payroll system
payroll software
hr system
hris
timesheet tool
time tracking tool
timekeeping system

class: tool-category-ticketing
ticketing system
ticketing tool
help desk
helpdesk
service desk tool

class: tool-category-messaging
chat tool
team chat
messaging app
email client
shared inbox

class: tool-category-documents
document management system
file share
shared drive
cloud storage
e-signature tool
wiki

class: tool-category-inventory
inventory system
warehouse management system
stock control system
barcode scanner
point of sale

class: tool-category-field
telematics
gps tracking
fleet tracking
route planning tool
field service app

class: tool-category-lab-quality
lims
laboratory information system
quality management system

class: tool-category-design
cad software
drawing software
estimating software
quoting tool
takeoff software

class: tool-category-marketing
email marketing tool
marketing automation
survey tool
panel software
website builder

class: tool-category-reporting
bi tool
reporting tool
dashboard tool
data warehouse
```

### 4.3 The category class

The fifteen `tool-category-` classes of 4.2, item 3, are the category class nod 6 needs. Nothing else is added for it: the script recognises the classes by their name prefix, which 4.1 pins as `tool-category-`.

### 4.4 `tools/lint_plugin.py`: one tuple in `PINNED`

Replace

```text
PINNED = (("call-type-vocabulary", "scripts/transcript_prep.py"),
          ("permitted-constants", "scripts/transcript_measure.py"),
          ("ledger", "scripts/ledger.py"))
```

with

```text
PINNED = (("call-type-vocabulary", "scripts/transcript_prep.py"),
          ("permitted-constants", "scripts/transcript_measure.py"),
          ("ledger", "scripts/ledger.py"),
          ("leak", "scripts/leak_lint.py"))
```

Nothing else in the file changes.

### 4.5 What step 5 owes these pins

For the step-5 author, not step 3: `leak_lint.py` holds one region between the lines `# pinned: leak` and `# end pinned` containing every token of 4.1 as a string literal in tuples (the markers, the kinds, the families, the kind-to-family table, the marks, the headings, the row keys and kinds, the index's schema, keys and two values, the severities, the verdicts, the modes, the rules, the wall classes, the clearable classes, the prefix and `local`), and no other string literal. The other embedded lists (`common-words`, `paraphrase-cues`, `cost-cues`, `confusables`, `credential-shapes`, `internal-notes`, and the stop list and the two vocabulary groups `internal-vocabulary` and `sales-framing` with their rows) sit in their own `# pinned: <name>` regions, which `lint_plugin.py` does not compare. Inside the `leak` region no comment may carry a backtick, since `lint_plugin.py` reads backticked words in the region's comments as embedded tokens too. A unit test asserts that the nine markers of the region are each a literal row of the shipped `markers` class (L66).

---

## 5. Touch-ups for the user's word

Design and shared-file changes the entries owe. They are applied only when the user says so, and nothing in the run depends on them: the code and the fixture follow this file. PLAN §7's entries 4 to 7 are items 3, 4, 5 and 6.

| # | File and anchor | Change | From |
|---|---|---|---|
| 1 | A§9.6:922, A§7.1:440, RM:76, SF:90; G58's follow-up | the index holds the vocabulary digest of names, terms, phonetic keys and figures, keyed by a hashed slug, in the pinned `clients-index/1` shape; `leak_lint.py index` writes it at init, after every intake and at close-out; an entry stays after the move to `archive/`; an absent index reads as empty only while no other record exists | X01, X02, X30 |
| 2 | A§5.4:357; A§8.5 step 5; A§8.6 steps 9 and 17; BP:252 | the subcommands are `scan`, `payload`, `blueprint`, `wall`, `terms`, `index`; the build guard runs `blueprint --strand`; the write path runs `payload --strand --kind --file` on the tool input | X08, X22, X31 |
| 3 | LT:5 to 6, LT:35 to 36 | the firm's name and renderings come from `local/settings.json`; the local list holds additions and the firm's whitelist | X04 (PLAN §7.4) |
| 4 | SF section 6 (lines 82, 90); LT:11 to 14 | the v1 surfaces: planned text, payloads, `drafts/`, `deliverables/handoff/`, live names at the audit, `SUMMARY.md`, the client-safe block when written; no rendered file and no `pdftotext` | X05 (PLAN §7.5) |
| 5 | SF:84 | the three paraphrase categories are A§:916's; closing tactics stay covered by the `method` class | X06 (PLAN §7.6) |
| 6 | SF:86 | "A firm name may sound like a common word, so the string list is backed by a phonetic-variant rule with a whitelist of legitimate uses." | X07 (PLAN §7.7) |
| 7 | A§9.6:916 | add credentials, internal notes and the seller's own account names from local settings to what the lint blocks | X06, X15, X40 |
| 8 | RM:76 | `personal-names-index.json` is the agnostic sweep's name list, not the lint's | X44 |
| 9 | A§9.6:920; LT:27, LT:132 to 133 | for the user's decision, not a wording fix: let an allowlist row clear one exact pain-id token that is the client's own vocabulary (an incident priority, a severity, a product grade), with a caution and the user's OK, every other id staying unclearable | X17 |
| 10 | `shared/leak-terms.txt` | optionally move the embedded groups (`internal-vocabulary`, `sales-framing`, the paraphrase cues) into shipped classes, so the vocabulary has one home | X06 |
| 11 | A§5.3:346, RM:76 | the home holds `.work/record.mutex` (the index's mutex) and `local/backup/` holds the index's backups | X29 |
| 12 | BP:158 ("(stage 4b)"), BP:51 | the AI payload kinds are built in stage 2; stage 4b adds what new probes change | X14 |
| 13 | RM:272 | "blocks all nine in `drafts/`, `deliverables/handoff/` and every monday payload" (no `sop/` in v1) | X05 |
| 14 | A§9.6:920 | a run in a snapshot's conflict rows blocks even where it matches the client's document; a `[Q/doc]` extract is a client quote for the eight-word rule | X24, X36 |
| 15 | A§9.6:920 | the blueprint's client-facing sections, its prompt blocks and its glossary are not an internal source for the copied-run rule; they are checked by `blueprint` | X11 |
| 16 | A§9.6:922 | the wall also runs on `drafts/` and the client-safe block | X45 |
| 17 | BP:156, BP:159 | three test files; the sizes are estimates | X43 |
| 18 | A§9.6:920 ("Warnings, not blocks: other numbers") | add "and the record's own volume and process numbers, which are reported and kept" | X25, X39 |

## 6. What other packages owe

Not WP4's to build; each package proves its own side, most at stage 4 (X20, X47).

| Package | Owes |
|---|---|
| WP7 (templates) | the client-safe marks in `call-summary.md` and `document-summary.md`; the `## Conflicts` heading in both; `exclusions.md` and `allowlist.md` with their headings and row form; the blueprint template's numbered sections 1 to 15 with no internal keys, markers or quotes in them, and the glossary marks (X09) |
| WP8 (engagement, call-intake) | `index` after `record.py init` and after every saved call, document or email; `scan` of each new call summary or snapshot in client-safe-block mode, exit 1 and 3 as stops (X02, X38) |
| WP9 (solution-blueprint, account-build) | `blueprint --strand` before the card and at the build guard; on every write, the tool input written as the payload file inside the record and `payload --strand --kind --file` between `ledger.py intent` and the call; exit 1 and 3 as stops (X08, X22, X47) |
| WP10 (solution-audit) | live object names handed to `payload --kind generic` (X05) |
| WP12 (client-closeout) | `scan` of `drafts/` again at close-out; `index` before the record moves to `archive/` (X02) |
| WP8 or WP12 (the strand summary step) | `scan` of `SUMMARY.md` before the user's yes (X37) |
| WP13 (the hook) | compare `args_digest` with the tool input before a write it can see (X16) |
| WP14 (fixtures, graders, runner) | a seed home whose index holds an entry, built by `leak_lint.py index`, for every seed record under its `clients/` (X20, X30); the leak grader over the twenty-five arrays and the two non-removals (L267 to L269) |
| WP16 (release tooling) | `terms` over `shared/` at release (L199); `agnostic_sweep.py` over `tests/fixtures/leak/` (X18) |

## 7. Worth the user's nod

Decisions taken on the user's behalf where the sources are silent and the choice is not obvious. Each was taken on the safer side; none stops the run. The user may change any of them, and the entry named says what changes with it.

1. **Cost figures and volume numbers are told apart by a cost word in the same sentence of the record** (X25). A number with no cost cue is a record number: matched in a payload it warns ("flag, do not remove") instead of blocking. A cost figure the record writes with no cost word nearby therefore only warns.
2. **The floors** (X25): numbers below 10 are never reported; a client cost figure of 1,000 or more blocks in any rendering; one from 10 to 999 blocks only beside a cost word, a currency sign or a rate suffix in the payload, and otherwise warns.
3. **A rounded or truncated form matches the exact figure** (X25): for an invented 318,460, "318k" and "$319k" both match, within the precision written.
4. **The wall's figures hold only cost figures of 1,000 or more with three or more significant digits** (X25), so two clients' round thresholds never block each other; this client's own round figures still block in its own payloads.
5. **Names are harvested from the whole record's text**, every capitalised run, acronym and e-mail part, and not from a roster (X26); a single common word is kept out of the digest, though not out of a multi-word name.
6. **The wall cuts a payload into every word, every run of two to four words, fused forms across hyphens, dots and other joiners, and phonetic keys** (X27), and also matches misspelt names by phonetic key. This catches more and may block a rare word that happens to sound like another client's name; the remedy is a rewrite, since the allowlist never clears the wall.
7. **"Not in this client's record" means anywhere in the record but `drafts/`, `deliverables/`, `.work/` and JSON files** (X11, X27), so a leak in a draft cannot clear itself.
8. **An absent index while other client records exist is exit 3**, and the message gives a count, not the folders' names (X30). A fresh home is unaffected; a home with an older, unindexed record stops until `index` runs there.
9. **The hashes are unsalted sha256, cut to 128 bits, with a short prefix** (X28). They keep plaintext out of the file, not out of a reader who can already open the client folders beside it.
10. **Archived folders' slugs are walled too** (X21), so a closed client stays walled even without an entry.
11. **A wall finding never names the other client** (X41): it says the payload's own words match another record.
12. **`ok` is false on exit 3**, unlike `ledger.py`'s envelope, where `ok` is true unless the exit code is 1 (X41).
13. **The blueprint's client-facing sections, prompt blocks and glossary are not a source for the copied-run rule** (X11), because payloads are copied from them; `blueprint` is exit 3 when it cannot find sections numbered 1 to 15 (X09).
14. **A run in a snapshot's conflict rows blocks even where it is also the client's own document text, and a `[Q/doc]` extract counts as a client quote** (X36, X24). Disputed or quoted client text stays out of monday verbatim.
15. **A near copy blocks**: eight words matching an internal file's eight in seven places (X24). This goes beyond A§'s literal six-word rule.
16. **The paraphrase rule** (X06): a sentence with a person reference and a cue phrase from six embedded groups blocks; a client whose own vocabulary holds a cue word (a clinic's "hospital") clears it with an allowlist row, which leaves a caution. Two more embedded vocabulary groups (`internal-vocabulary`, `sales-framing`) block and clear the same way.
17. **The seller's own account structure** (X06): the names of the user's never-shown workspaces, the default account's slug and the GitHub account from `settings.json` block as literals, and those workspaces' and that account's ids block even inside a link.
18. **A long mixed-case string of 32 or more characters blocks as a credential** (X15, shape 6), so a pasted data string may block.
19. **An unknown payload kind is exit 3; object keys and numbers are walked; a string holding JSON is walked as JSON** (X22).
20. **`.docx` headers, footers, notes, comments and custom properties are read; a part with a DTD is exit 3; size caps apply; any file in `drafts/` the lint cannot read is exit 3**, hidden files included, system files aside (X35).
21. **The tool-category vocabulary**: fifteen generic categories shipped in `leak-terms.txt` (section 4.2), and the proper-noun test of X12. The assertion runs in `scan`, `payload` and `blueprint`, not in `terms` or `wall`, which L104's "whatever the subcommand" reads more widely.
22. **Markers match case-insensitively, as every literal row does**, so a Markdown checkbox `[x]` blocks as the marker `[X]` (X03).
23. **An absent `local/leak-terms.txt` reads as empty** rather than exit 3 (X33), since the required `settings.json` carries the firm rule.
24. **`SUMMARY.md` is checked under the copied-run and quote rules and the two assertions only, against every source but the summaries themselves; the client-safe block is checked, when written, under every rule but the copied-run rule** (X37, X38).
25. **The pain-id patterns are kept as shipped** (X17), with their cost to a client's own "P1" or "S1"; a narrowing is proposed in section 5, item 9.
26. **The index's mutex is `<home>/.work/record.mutex`**, a new zero-byte file in the home, and its backups go to `local/backup/` (X29).
27. **A caution, like a warning, gives exit 2** (X39), so a payload carrying the client's own allowlisted word always exits 2.
28. **The phonetic key and the edit distances of X32**, with the whitelist as the only exemption: an ordinary word that sounds like the firm's name blocks until a whitelist row names it.
29. **"Mostly common words" is five of six** (X19), with about sixty monday and work words counted as common; the quote rule is not filtered.
30. **Seven of the trap shapes are known limits in part** (section 3, the `limit` rows): small talk with no person, third parties named once, a paraphrased narrative, objection or claim, a title remark, an address, a withheld figure. The fixture asserts them so a later rule's reach is seen.
31. **An index entry's `updated` changes only when its digests change**, so a rerun writes nothing (X46).
32. **`index` refuses a record whose `CLIENT.md` slug differs from its folder name** (X30).

---

## Added by the fixture check (step 4b), 2026-10-17

The trace check of the fixture (`fixture-check.md`, F01 to F14) and the fixture author's own notes found nine places where an X entry is silent or two entries disagree. Each is settled here, on the safe side where the sources are silent. No X entry is edited; a Y entry says which one it narrows. The fixture already follows every entry below.

### Y01 The allowlist feeds no set

**Decision.** `solution/allowlist.md` feeds none of the five sets of X11: not F, R, Q, D, and not the wall's own set O. This narrows X11's row "`solution/allowlist.md`, `live/live-map.md`", which now reads "O: `live/live-map.md` only". A row that names another client's name therefore leaves the wall block in place, as X10 says. `exclusions.md` keeps its X11 row: a row there that names another client's name still blocks, under the exclusion rule.

**Reason.** X10 and A§:920 ("never ... other clients' names") say an allowlist row never clears a wall hit; X11's O column would let one row do so. A§ wins over a table in this file. Found by F01 and by the fixture notes.

**Follow-up.** *Build:* step 5 (the set reader), step 6 (O). *Test:* R18-p line 7 blocks with rule `wall`.

### Y02 A date written in spaced groups is a date, not an id

**Decision.** Three digit groups joined by single spaces, dots, hyphens or slashes, of one or two, one or two and four digits (or four, two and two), that form a real calendar date with a year from 1900 to 2099, read day-month-year, month-day-year or year-month-day, are a date for X34's split-id rule. The id row stays quiet, and the run is reported only as the `split-figure` warning of X25. This narrows X34's "well-formed date or time (X25)" to include the spaced form. Every other run of groups totalling eight digits or more still blocks as an id.

**Reason.** X34 already exempts groups that read as a date. X25 and section 3.2 set the outcome for "dates whose digits are split" at warns. Section 3.2 is the specific entry, and it wins. A spaced id that happens to be a valid date still warns, so nothing passes silently. Found by F02.

**Follow-up.** *Build:* step 5. *Test:* T10-p warns (exit 2); T04-p (`8314 2290 57`) still blocks.

**Worth the user's nod.** An id written in three spaced groups that happens to form a valid date only warns.

### Y03 The four mark lines are never checked text

**Decision.** A line that is exactly one of the four pinned marks (`<!-- client-safe:start -->`, `<!-- client-safe:end -->`, `<!-- glossary:start -->`, `<!-- glossary:end -->`), surrounding spaces ignored, is removed from the checked text before any rule runs, in every mode. Positions still map to the original lines. A mark line holding any other text is not a mark (X09) and is checked like any other text, so the `<!--` row blocks it. This narrows LT:190's HTML-comment row for those four exact lines only.

**Reason.** X09 pins the marks as record structure. X36 and X38 treat what lies between them as client text, never the marks themselves. Without this entry, every blueprint with a glossary would block on its own marks. Found by F03.

**Follow-up.** *Build:* step 5. *Test:* R10c-t passes; a mark with a trailing word blocks (step 5's unit test).

### Y04 A secret pair may have spaces on both sides of its separator

**Decision.** X15 shape 2 reads: a key word, optional spaces, `:` or `=`, optional spaces, optional quotes, then a value of four or more non-space characters.

**Reason.** Notes write `password: x` and `password = x` far more often than `password:x`. BP:158.17 asks that no credential reach an account, and the wider shape is the safe one. Found by F04.

**Follow-up.** *Build:* step 5. *Test:* R16-p line 2; P-group-p, P-dashboard-p, P-agent-p and P-generic-p.

### Y05 How an allowlist or exclusions row is split

**Decision.** A row's key list is its last bracketed group, when that group ends the line and its content reads as `key: value` pairs separated by semicolons, each key a pinned row key. Everything before it, trimmed, is the term. If the line ends in no such group, the whole text after the leading hyphen is the term and the row has no keys. An allowlist row with no keys has no `ok`, so it clears nothing and warns (X09). So `- [E] [ok: yes; class: markers]` has the term `[E]`. This narrows X09's "the term, then optionally one bracketed list".

**Reason.** A marker, a pain id or any bracketed client word can be a term. Reading the first bracket as the key list would leave an empty term and stop the run (exit 3). Taking the last group, and only when it parses, never widens what a row clears. Found by F05 (a) and by the fixture notes.

**Follow-up.** *Build:* step 5. *Test:* R18-p under the `allowlist-attempts` overlay (the `[E]` row parses, and the block stays).

### Y06 When an allowlist row warns

**Decision.** A row that names something no allowlist row may clear (X10) adds its `allowlist` warning only when it meets a finding it may not clear: one warning per such finding. A row that meets nothing says nothing. A row without a non-empty `ok` still warns on every run, as X09 says.

**Reason.** X10 ties the warning to "leaves the block in place", which happens only at a match. A warning on every run would turn every clean text in that strand into exit 2 and hide the real ones. Found by F05 (b) and by the fixture notes (nod 8).

**Follow-up.** *Build:* step 5. *Test:* R18-p carries the warnings; R18-t, under the same overlay, exits 0.

### Y07 Where the second internal-note shape is reported

**Decision.** X40's second front-matter shape (a line of three hyphens followed by a `schema:` line) is one `internal-note` finding reported at the hyphen line. An unquoted `schema:` line is not reported a second time. A quoted one is also a flat front-matter line, so it may be reported under both shapes.

**Reason.** X40 names the pair as one form and gives no position. The hyphen line is where the form begins. Found by F10.

**Follow-up.** *Build:* step 5. *Test:* R17-p line 7.

### Y08 Structural ids in a real tool input

**Decision.** In a payload, a value directly under a structural id key is a monday id, not text, when it is a digit string with no leading zero, a positive JSON integer, or a list of them. The structural keys are:

`id`, `ids`, `account_id`, `workspace_id`, `workspace_ids`, `workspaceId`, `workspaceIds`, `folder_id`, `folder_ids`, `folderId`, `board_id`, `board_ids`, `boardId`, `boardIds`, `group_id`, `groupId`, `item_id`, `item_ids`, `itemId`, `itemIds`, `parent_id`, `parentId`, `parent_item_id`, `doc_id`, `docId`, `object_id`, `objectId`, `view_id`, `viewId`, `dashboard_id`, `dashboardId`, `widget_id`, `widgetId`, `automation_id`, `automationId`, `workflow_id`, `workflowId`, `agent_id`, `agentId`, `app_id`, `appId`, `user_id`, `user_ids`, `userId`, `userIds`, `team_id`, `team_ids`, `teamId`, `teamIds`, `owner_ids`, `subscriber_ids`.

Such a value is exempt from the eight-digit id row of `id-patterns`, the split-id rule of X34, and the figure, split-figure, number and record-number rules. Every other rule still runs on it: `seller-account` above all, so an id of a never-shown workspace or of the user's default account still blocks under a structural key. An id anywhere else blocks as before: in free text, under any other key, inside a JSON string that is not a structural value, or with a leading zero, a sign, a space or any other character. The key itself is checked as a string, as X22 says. Inside a `column_values` JSON string the same rule applies at every depth (a board-relation value of `item_ids`, for example).

The list lives in the script between `# pinned: structural-id-keys` and `# end pinned`, a region `tools/lint_plugin.py` does not compare, like the common words. No `Pinned: leak` token is added, because no other record file names these keys, and the lint-clean fixture is not touched. `tests/unit/test_leak_fixture.py` holds a copy, which step 5 keeps equal by a unit test.

**Reason.** X22 walks every string, and the id row (LT:191) blocks digits outside links. Every real write carries the ids of the workspace, board or item it targets, so without this entry every write would block. Structural keys are where the connector expects ids. Exempting only those values, and only in the exact id shape, keeps every id in text blocked. Keeping `seller-account` on them is the safe side, since a write into the user's own never-shown workspace must stop anyway. Found by the fixture notes.

**Follow-up.** *Build:* step 5 (the region and the rule), step 6 (the walker). *Test:* R21-p blocks on a never-shown workspace id under `workspace_id`, an id in a description and an id under `notes_ref`. R21-t passes with ids under `workspace_id` (a string) and `folder_id` (a JSON integer). *Owed elsewhere:* WP9 writes ids only under these keys (section 6).

**Worth the user's nod.** The key list, and the choice to keep `seller-account` on structural values.

### Y09 The phonetic key of a fused window

**Decision.** When the phonetic rule fuses two or more adjacent words of the checked text into one candidate (X32, the windows of n and n + 1 words), the candidate's key is the words' keys joined end to end, each word keyed on its own, with no collapse across the join. A single written token keeps its one key. This narrows X32's "a fused run has one key". The edit distance of X32 still runs on the fused letters.

**Reason.** Keyed as one word, "the thimble" fuses to `thethimble`. Its two `th` sounds collapse into one, so it keys to `0MPL`, the firm's key, and the whitelist cannot clear it, because the hit only contains the whitelisted word. So the most natural use of the whitelisted word would block. Keying each word apart gives `0` + `0MPL` = `00MPL`, while the split renderings still match: `Thym Bell` keys to `0M` + `PL` = `0MPL`. Found by the fixture notes.

**Follow-up.** *Build:* step 5. *Test:* R13b-t line 5 (`The thimble stays in the drawer.`) passes; R13b-p line 3 (`Thym Bell`) still blocks.

**Worth the user's nod.** A misspelling whose sounds collapse only across a word gap (two words that run into each other) is no longer matched by the key, only by the edit distance.

---

## Added by code part 1 (step 5), 2026-10-17

Writing `scripts/leak_lint.py` part 1 met eleven places where an X or Y entry is silent, or where two sources pull apart. Each is settled here on the safe side. No X or Y entry is edited; a Z entry says which one it reads or narrows. The code and its tests already follow every entry below, and `API-leak_lint.md` lists them again for the user's nod.

### Z01 Percent-decoding is the script's own

**Decision.** The percent-decoded copies of X03 and X34 are made by a small decoder in the script: every run of `%XX` escapes is decoded as UTF-8, with the replacement character for bytes that do not decode, which is what `urllib.parse.unquote` does. The script imports no `urllib` module.

**Reason.** X03 names `urllib.parse.unquote` as the means; CONTRACT L10's test walks the imports for `urllib`, `socket`, `http` and `ssl`. Both are met when the behaviour is X03's and the import is absent. The contract's test is the stricter of the two.

**Follow-up.** *Build:* done. *Test:* `test_L01_L10_...` and `test_L67_L68_L69_X03_...` (a `%2F` path blocks). *Touch-up:* none.

### Z02 Until the wall is built, a home with another record stops the check

**Decision.** In part 1, `scan` in modes `full` and `client-safe-block`, and `payload`, exit 3 (field `wall`) when the home holds a `clients-index.json`, or a folder under `<home>/clients/` or `<home>/archive/` other than this record that holds a `CLIENT.md`. Only the folder listing is read. A home that holds this record alone runs every part-1 rule, since the wall would have nothing to compare. Mode `summary` does not run the wall (X37) and is not stopped. `blueprint`, `wall`, `terms` and `index` answer exit 3, "not built yet". Step 6 replaces `wall_hits` and removes the stop.

**Reason.** The step-5 brief: nothing may return 0 on a path that is not built. X30 and BP:158.32 fail closed when the wall cannot see another record. A fresh home is X30's own passing case.

**Follow-up.** *Build:* step 6 replaces it. *Test:* `test_X01_part_1_has_no_wall_...`. *Touch-up:* none.

### Z03 An id after a mark blocks once real links are masked

**Decision.** The eight-digit id row of `id-patterns` runs as shipped on a copy of the line with every link target masked (X34). Beside it, on the same masked copy, the script also blocks any run of eight or more digits with no letter or digit on either side, reported as the same row. So an id after a slash, an equals sign or a hyphen in something that only looks like a link (`hxxp://...`, a URL without a scheme) blocks, while an id inside a real link still passes.

**Reason.** X34 says a look-alike link is not a link "and its ids block". The shipped row's lookbehind, `(?<![\w/=?&#.-])`, would exempt the digits after a slash in it. X34 is the later and more specific reading, and masking the real links first keeps the exemption the row was written for.

**Follow-up.** *Build:* done. *Test:* `test_L72_L73_L74_X34_...`. *Touch-up:* for the user's word, the shipped row could be widened the same way, so the list says what the script does. Step 7 may probe the cost: a decimal with eight digits after its point now blocks.

### Z04 A checked file never feeds its own check

**Decision.** While a file is checked, the entries its own text put into F, R, Q and E are left out: the whole file in modes `full` and `summary`, and its client-safe block text in mode `client-safe-block`. The rest of the file still counts there, so a quote in its body copied into its block still blocks.

**Reason.** X37 and X38 check record files that are themselves set sources (a strand's `SUMMARY.md`, a call summary, a snapshot). Read literally, every figure and quote of such a file would match itself and block. Drafts are never sources (X11), so this changes nothing for them.

**Follow-up.** *Build:* done. *Test:* `test_L165_X37_...`, `test_L103_X38_...`. *Touch-up:* none.

### Z05 What a split rendering is, and two quiet numbers

**Decision.** Three readings of X25 and X34.

1. Digit groups joined by a single space, a line break, a table pipe or emphasis marks form a split rendering whatever their lengths. Groups joined by a dot, a hyphen, a slash or an underscore form one only when the next group has three digits, as thousands do.
2. The parts of a digit chain that reads as a date (Y02) are not numbers, so they give no number warning.
3. A plain digit string of eight or more digits gives no `number` or `record-number` warning: it is an id, and the id row blocks it. The figure rules still run on it.

**Reason.** X25 lists the joiners but not group sizes. Without the three-digit condition every decimal (`1.5`) and every range (`10-12`) would be read as a split figure. Item 2 follows X25's "dates are not figures and are not warned". Item 3 only removes noise beside a block that stays.

**Follow-up.** *Build:* done. *Test:* `test_L105_L106_...`, `test_X34_Y02_...`. *Touch-up:* none. Listed for the user's nod.

### Z06 The seller-account ids run on every JSON number

**Decision.** A JSON number is checked by the figure and number rules (X22) and also by the `seller-account` id rule, whether or not it sits under a structural key.

**Reason.** Y08 keeps `seller-account` on structural values "above all", including JSON integers. X22 names only the figure and number rules for numbers. Running the seller check on every number is the safe side: the user's own workspace id must never pass as a number.

**Follow-up.** *Build:* done. *Test:* `test_Y08_structural_ids`. *Touch-up:* none.

### Z07 A scan's mode and strand when it takes several paths

**Decision.** When the files of one `scan` run in more than one mode, the output's `mode` is null and each file checked in mode `summary` or `client-safe-block` carries its own `mode` in `inputs`. A scan that checks no file prints `full`. A path outside `strands/` (a record-level file, such as a call summary) has no strand whatever `--strand` says, so nothing in it is cleared (X10). `--strand` narrows the default targets and must agree with every path under `strands/`.

**Reason.** X41 gives one `mode` field and X08 lets a scan take several paths. X10 says a record-level file has no strand.

**Follow-up.** *Build:* done. *Test:* `test_X08_strand_rules`, `test_L165_X37_...`. *Touch-up:* none.

### Z08 The embedded word lists as written

**Decision.** The step-5 author wrote the groups X06, X19 and X25 leave to that step. Three choices go beyond the entries:

1. The `health-identity` group leaves out three demonyms that are everyday trade words in client text (`french`, as in doors and polish; `polish`, the verb; `dutch`, as in a barn or an oven). About forty-five others are in.
2. The cost cues add `charge`, `charges` and `charged` to X25's list.
3. A lower-case `mm` after a number with no currency is read both ways, as million and as plain, as X25 reads a lower-case `m`.

**Reason.** X06 lets the author write each group "from the rule's own meaning". A cue that is an ordinary trade word would block a joiner's or a decorator's text beside any name. Item 2 adds blocks, never removes one. Item 3 is the reading X25 gives `m`, applied to the unit it most often stands for (`18mm`).

**Follow-up.** *Build:* done. *Test:* `test_L103_X06_...`, `test_X25_ambiguous_lower_case_m_...`. *Touch-up:* the groups may later move into `leak-terms.txt` (section 5, item 10). For the user's nod.

### Z09 Help is a usage error

**Decision.** The parser has no `-h` or `--help`. Either is a usage error: exit 3 with the envelope.

**Reason.** argparse's help prints text and exits 0. A gate that fails closed has no path to 0 that checked nothing (BP:158.32, G10).

**Follow-up.** *Build:* done. *Test:* `test_L20_L21_...`. *Touch-up:* none.

### Z10 The generic walker is built in part 1

**Decision.** `payload_units` walks every string, every object key and every number at every depth, with JSON inside strings, Y08's structural values and X42's depth limit, in part 1. Nothing in it depends on the kind, which is checked against the pinned list only. Step 6 proves it over every kind of the trap fixture and adds the wall inside it.

**Reason.** X22 says no field list limits the walker. PLAN §3 gives "the payload walker over every kind" to step 6. With no kind-specific code, building it once now keeps one walker, and step 6 still owns its proof.

**Follow-up.** *Build:* step 6 may keep or change it. *Test:* `PayloadTest` here; the kinds' samples in step 6. *Touch-up:* none.

### Z11 A legal suffix need not be written

**Decision.** A firm rendering, a seller-account name, an exclusion term or a `plugin` row that ends in legal-suffix tokens (X28 step 6's list) also matches without them, with the gaps and the fused form of X32. So an exclusion row `Example Supply Ltd` also blocks `Example Supply` and `ExampleSupply`.

**Reason.** X28 applies step 6 "for names, terms and slugs", and the firm rule and the exclusions are among the rules that compare words. Matching the shorter form only adds blocks.

**Follow-up.** *Build:* done. *Test:* `test_X28_step_6_...`. *Touch-up:* none.
