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
| 19 | A§9.6:918 (the second of the "two assertions a blocklist cannot express"); A§5.4:357 (`leak_lint.py` "carries the split-figure and tool-category assertions") | one assertion a blocklist cannot express runs on every scan, the split figure; the tool-category sentence and its reason go, until something like reusing one client's material for another arrives in v2 or v3 | A30, R64 |
| 20 | BP:158 ("the **two structural assertions** run on every scan ...") | "the split-figure assertion runs on every scan and is proved on `tests/fixtures/leak/`: a document carrying a figure only in split renderings fails"; the three-categories case and its two-category twin go | A30, R64 |
| 21 | `shared/safety.md` section 6, line 86 ("**Two assertions a blocklist cannot express** ...") | "**One assertion a blocklist cannot express** runs on every scan: a document that carries a figure only in its split renderings (digits broken across tokens, a number spelled across a line break) fails." The tool-category clause and its reason go; the phonetic-variant and trap-shape sentences stay. A shared edit, so `terms` and the `shared-words` region (R29) follow it | A30, R64 |

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

---

## Added by code part 2 (step 6), 2026-10-17

Writing `scripts/leak_lint.py` part 2 met eight places where an X, Y or Z entry is silent, or where two sources pull apart. Each is settled here; where a choice narrows what blocks, the entry says so and names the source that forces it. No earlier entry is edited; a later entry says which one it reads or narrows. The code and `tests/unit/test_leak_wall.py` already follow every entry below, and `API-leak_lint.md` lists them again for the user's nod.

### Z12 The harvest's stop list holds the plugin's own shipped words

**Decision.** X26 step 6's stop list also holds the days and months in full and every word of the plugin's own `shared/*.md` and `shared/*.txt` files, read fresh by `index` (and by the wall when it cuts the other folders' slugs). Such a word never enters a `names` digest on its own; a name of two or more words keeps it (X26 step 5). The client's name and slug from `CLIENT.md` stay in whatever they hold (X26 step 1). The payload side has no filter, so this changes only what an entry publishes.

**Reason.** X26 step 6 names "the plugin's own vocabulary" as a stop source, and L197 requires `terms` over the real `shared/` to exit 0 with the two planted records indexed. Without this, the headings every record carries (Discovery, Brief, Stakeholders, Strand) and ordinary words harvested inside a name (Store, Fresh) published into every entry and blocked `shared/` itself. A word the plugin ships is not client input, which is what BP:114 asks `terms` to prove absent.

**Follow-up.** *Build:* done. *Test:* `test_L197_terms_over_the_real_shared_folder_exits_0`, `test_L169_to_L173_L185_X26_...`. *Touch-up:* none. An entry changes when `shared/` changes; the next `index` run absorbs it.

### Z13 The wall's phonetic test, narrowed to what can be a misspelt name

**Decision.** Three readings of X26 step 8, X27 type 4 and Y09.

1. A single word's phonetic key is published only when no common word and no stop-list word (Z12) has the same key.
2. On the checked side, a run is keyed only when at least one of its words is outside the common words and the stop list, and its words hold seven letters or more in all, the floor X27 already sets for a single word.
3. A run's key is tested in its spaced form (the words' keys joined by a space). The index also stores the end-to-end join, so a name written fused (`MarlbekFrate`) keys as the spaced name does.

The literal hashes are unchanged: every correctly written name, in every normalised and fused form, still blocks.

**Reason.** Keys are short, so ordinary pairs of words keyed like two-word names ("call at" like an invented first and last name, "lease for", "held no") and ordinary single words keyed like one-word names ("forward" like an invented carrier's name). Over the real `shared/` and the plugin's own scripts these blocked, against L197. PLAN nod 6 accepts that the wall "may block a rare word"; these were common ones, which the allowlist could not clear (X10). The narrowing is the least that makes L197 hold and keeps the planted misspellings (T15, K30) blocking.

**Follow-up.** *Build:* done. *Test:* `test_X27_fused_and_phonetic_candidates_and_their_twins`, `test_L197_...`. *Touch-up:* none. For the user's nod: a misspelt name whose key an ordinary word shares is caught only by its literal forms. **Answered 2026-10-19:** settled by A30, whose reading the user nodded ("Yes this is correct."): Z13 stands as built, and the two follow-ups of `leak-review-part2.md` (a five-letter floor for two-word runs, and keeping the client's own name's key) are answered no.

### Z14 `terms` reads an empty file of any name, and has no record of its own

**Decision.** Under `terms`, a zero-byte file is read as empty text whatever its extension; a file with content outside X31's list is still exit 3. With no record, every index entry is compared, every folder under `<home>/clients/` and `<home>/archive/` is a slug, and the coverage check of X30 asks an entry of every one of them that holds a `CLIENT.md`. `--record`, when given, is ignored by `terms`.

**Reason.** X31 says an unread file is exit 3 "since an unread file proves nothing"; an empty file holds nothing to prove, and `shared/` ships `.gitkeep`, so L197 could not pass otherwise. X08 gives `terms` no record, so nothing is skipped as its own.

**Follow-up.** *Build:* done. *Test:* `test_X31_Z14_what_terms_reads_and_where_it_stops`, `test_L198_X30_...`. *Touch-up:* none.

### Z15 A checked record file never makes its own words this record's

**Decision.** Z04 extends to the wall. While the wall checks a record file (a call summary or a snapshot in mode `client-safe-block`, the blueprint), that file's own candidates, keys and figure forms are left out of O, so a word counts as this record's only when another O source holds it. O keeps, per word, the files that hold it. Drafts and payloads are never O sources (X11), so nothing changes for them.

**Reason.** X11 puts call summaries, snapshots and the blueprint's client-facing parts in O, and X45, L162 and L189 require another client's name in a client-safe block and in a planned name to block. Read literally, the file being checked would make the name its own and pass. Z04 settled the same pull for F, R, Q and E.

**Follow-up.** *Build:* done. *Test:* `test_L279_X45_...`, `test_L189_...`. *Touch-up:* none.

### Z16 How wall/1 cuts a text, as built

**Decision.** The readings X26 and X27 leave to the builder.

1. A harvested name is a run of capitalised tokens joined by spaces or tabs, a hyphen, an ampersand or a plus, with `of`, `and`, `the` and `de` allowed between two capitalised tokens; never across a line break, a comma or another mark. Each sub-run of one to four tokens that starts and ends on a capitalised token is a candidate. A lone legal suffix is never a name.
2. An e-mail address gives its local parts, those parts spaced and fused, and each domain label of three or more letters other than the last (spaced and fused when the label holds a hyphen).
3. A checked text's runs cross commas and single line breaks and stop at `.`, `!` or `?` before whitespace (closing quotes and brackets may sit between) and at a blank line. Tokens are fused across up to three of `-`, `.`, `_`, `@`, `/`, `&`, `+`; a camel-case word is already one token.
4. A wall hit is reported over its matched tokens; overlapping hits of one class are merged into one finding, so the finding shows the longest matching stretch.
5. A capitalised word at the start of a sentence is harvested like any other, since X26 makes no exception.

**Reason.** X26 and X27 fix what is a candidate but not every separator. Each reading takes the wider side on the checked text, where more candidates only add blocks, and the narrower side in the harvest, where a wider run would publish phrases that are not names.

**Follow-up.** *Build:* done. *Test:* `test_L188_X28_...`, `test_L169_to_L173_...`. *Touch-up:* none. For the user's nod (item 5): an ordinary word that opens a sentence in one record and is not a common word ("Rework", "Laminate" in the planted record a) blocks in another record's text that does not hold it. The fixture's informal run from record b shows two such blocks.

### Z17 The wall's figures, as built

**Decision.** Five readings of X25's last bullets.

1. "Keeps three or more significant digits" is read as n of three digits or more at each k (n of 100 or more); an exclusion figure keeps n of 1 or more.
2. Rounding is half up on both sides, so a figure and its rounded rendering always meet.
3. A number whose precision is below a unit is tested at k = 0, rounded.
4. The own test for a figure is the same form test as the hash test: O holds every f-form, at n of 1 or more, of every number its sources hold, and a number is this record's when its tested form is among them. X25's tolerance is not used on the wall.
5. Digit chains read whole (X25's split renderings) and JSON numbers are tested too, except a structural id (Y08); percentages never are.

**Reason.** X25 states the forms and the test for the other records' side only; testing O by the same forms keeps one comparison on both sides of the hash, which X28 asks for. Items 1 to 3 settle arithmetic X25 leaves open; item 5 takes X22's "every number" to the wall's figure part, the wider side.

**Follow-up.** *Build:* done. *Test:* `test_L184_X25_...`, `test_L174_L175_X25_...`. *Touch-up:* none.

### Z18 The index and its readers, as built

**Decision.**

1. `index` runs no rule. The record warnings that reading the sets raises (malformed client-safe marks) are scan's and are not printed by `index`. Its output carries `written`: true when it wrote the file, false when the bytes would be the same.
2. `index` reads the shipped list and the `shared/` files for the stop list (Z12), this record's files and the index, and nothing else.
3. The index is malformed, exit 3 for every reader and never overwritten by `index`, when the top level holds any field but the four of X02, an entry key is not 32 hex characters, an entry holds any field but `updated` and the four lists, `updated` is not a UTC stamp, or a list holds anything but 32-hex strings. Sorting is written, not required on read.
4. A folder under `<home>/clients/` or `<home>/archive/` with this record's own name is this record: it is neither a slug nor counted by the coverage check, and the own entry is the one keyed by the folder's name.
5. L190's test ("the index emptied and the other record folder present") cannot exit 0 beside X30, which stops a home with an unindexed record. It is proved with the other folder present without a `CLIENT.md`: the folder is then a slug only, the name held only by the removed entry passes, the slug blocks, and no file inside the folder is opened.

**Reason.** X02, X29, X30 and X46 fix the shape and the writer; these are the edges they leave. Item 5: X30 is the later and more specific entry and fails closed, so it wins over L190's literal setup.

**Follow-up.** *Build:* done. *Test:* `IndexTest`, `test_L190_X21_...`. *Touch-up:* none.

### Z19 `blueprint`, as built

**Decision.** `blueprint --strand <NNN>` reads that strand's `solution/blueprint.md` and checks its client-facing text: the lines X09 names (sections 1 to 15, the prompt blocks, the glossary), every other line blanked so positions stay. The glossary's text is one unit exempt from the copied-run rule only; the rest is one unit under every rule, the wall included. Z04's own-file exclusion does not apply: the client-facing text feeds no set (X11), so a run or a figure copied from the blueprint's own internal sections still blocks. Glossary marks that are not well formed give one `warn`, exempt nothing, and the lines from each mark to the next level-1 or level-2 heading are checked too. A missing blueprint is exit 3 naming it; a blueprint with no numbered level-2 heading is exit 3, "cannot find sections 1 to 15" (X09).

**Reason.** X08, X09 and X36 fix the surface and the exemption; X11 makes the internal rest of the blueprint an internal source, which Z04 would otherwise hide from its own client-facing text. Checking the text after a broken mark is the fail-safe side of X09's malformed-mark rule.

**Follow-up.** *Build:* done. *Test:* `BlueprintTest`. *Touch-up:* none.

---

## Added by the review fixes, part 1 (step 8), 2026-10-17

The adversarial review of part 1 (`leak-review.md`, part 1, F01 to F41) found places where a reading of an X, Y or Z entry let a leak through, or blocked ordinary client text for no protection. The fixes below make or change a decision; each is settled on the fail-safe side unless the entry says it narrows a block, and then it names the source that wins. No earlier entry is edited; an R entry says which one it reads, widens or narrows. Every R entry has a unit test in `tests/unit/test_leak_lint.py` named after its finding (`test_F01_...` to `test_F41_...`). The entries marked **For the user's nod** are listed again at the end.

### R01 A number may follow a sign, a dash, a slash, a quote or an abbreviation

**Decision.** The number reader refuses a number only inside a digit run (after a digit and `.`, `,`, `'` or a narrow space) or after a full stop that does not follow a letter. So `-184,260`, `−184,260`, `150k-184k`, `year/184,260`, `'184k'` and `c.184k` are numbers, read by their absolute value. A currency code may sit straight on the digits (`USD184,260`, `EUR184k`), and a currency sign or code on a number counts as its cost cue. A hyphen may stand before a magnitude word (`184-thousand`), not before `k`, `m`, `mm` or `bn`. Dates, times, versions, years and list ordinals stay masked as before.

**Reason.** X25: a match with a cost figure of 1,000 or more blocks "in any rendering", and X22 checks every JSON number by the figure rules. The old lookbehind refused the second figure of every range and every signed figure. Cost: the second number of an ordinary range ("pages 10-12") now warns too, which changes no exit code that the first number did not already set.

**Follow-up.** *Build:* done. *Test:* `test_F01_X25_...`. *Finding:* F01.

### R02 A monday id written as a JSON number blocks outside a structural key

**Decision.** A JSON number that Y08 does not mark structural (any other key, a list under a key that is not structural, a float, a negative number) is checked by the id row as its decimal text, reported as `term`, class `id-patterns`. Z05 item 3's silence on a plain run of eight digits now rests on a block that runs.

**Reason.** Y08: an id "anywhere else blocks as before", and only a positive JSON integer under a structural key is exempt.

**Follow-up.** *Build:* done. *Test:* `test_F02_Y08_...`. *Finding:* F02.

### R03 How an `inputs/*.md` file is placed

**Decision.** An `inputs/*.md` file whose front matter (a `---` block opening the file) holds a `schema:` line naming `document-summary/1`, quoted or not, is a snapshot. A higher `document-summary/<n>` is exit 3 ("newer than this lint's"), and any other schema is exit 3, both with field `schema`. A front matter block with no `schema:` line is read as an internal file (F, R and Q), never as client-document text. A file with no front matter stays a raw client document (E), as X11 says. This narrows X11's row "a `.md` whose front matter is not `document-summary/1`" to a `.md` with no front matter.

**Reason.** X11 and X36 make a snapshot's body and conflict rows R sources; G57 as X02 applies it makes a newer schema exit 3; A§:920 fails closed. Front matter the lint cannot place must never feed the copied-run exemption, which is the one rule an E source loosens.

**Follow-up.** *Build:* done. *Test:* `test_F03_X11_G57_...`. *Finding:* F03. **For the user's nod:** a raw client `.md` that arrives with its own front matter is read as internal text, so copying it blocks until the session saves it without front matter or as a snapshot.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "Okay that makes sense, then yes, let's play it safe."

### R04 An exclusions file is read whole or not at all

**Decision.** For `exclusions.md` only, exit 3 naming the file and line on: a heading of the form `## Exclusions ...`, `### Exclusions` or deeper that is not exactly `## Exclusions`; a bullet or numbered line in a file with no `## Exclusions` heading; any line under the heading that is not a `- ` row, a blank line, an HTML comment or a sub-heading; and a row whose last bracketed group reads as `key: value` pairs but holds a key outside the pinned row keys. `allowlist.md` keeps the lenient reading of X09 and Y05, where a lost row only removes a clearing.

**Reason.** X09 makes an empty term exit 3 and X33 makes anything a list reader cannot apply exit 3; A§:920 and BP:158.32 fail closed. Y05 kept the last-group reading so that it "never widens what a row clears"; for an exclusion a dropped row widens what passes, so the safe side there is the stop.

**Follow-up.** *Build:* done. *Test:* `test_F04_X09_X33_...`. *Owed elsewhere:* WP7's `exclusions.md` template keeps prose above the heading only (section 6). *Finding:* F04.

### R05 HTML is decoded for every rule

**Decision.** Every unit whose text holds a tag or an entity is also checked as an HTML-decoded copy: each tag becomes a space, a block tag (`p`, `br`, `div`, `li`, `tr`, `td`, `h1` to `h6` and the like) a line break, and each entity is decoded with `html.unescape`. Every rule runs on that copy; a hit the plain copy already made (same rule, class and overlapping place) is not reported twice. Positions map back to the text as written. HTML comments are not tags, so the `<!--` row still sees them.

**Reason.** X24 (emphasis and marks "never break a match"), X28 (one normalisation for every rule that compares words) and A§9.6 ("every monday text payload"): monday holds update and long-text bodies as HTML.

**Follow-up.** *Build:* done. *Test:* `test_F05_X24_X28_...`. *Finding:* F05.

### R06 A quote line gives its whole utterance as well as its quoted words

**Decision.** For the Q set, a `[Q]`-family line that holds double quotation marks gives both the quoted spans and the line's text with the marker, the locations and the speaker removed. The E set (a snapshot's `[Q/doc]` extracts) keeps the quoted spans only, so the exemption does not grow.

**Reason.** A§:916 and X36: a client quote of eight or more words blocks, also when held in a client-safe block. X24's "the text between double quotation marks" was written for a line that quotes its whole utterance; taking both is the fail-safe reading.

**Follow-up.** *Build:* done. *Test:* `test_F06_X24_...`. *Finding:* F06.

### R07 A literal's boundary only where the term has a word character

**Decision.** A literal row takes LT:18's boundary only on a side whose end character is a letter or digit, so `overloaded[I]`, `[Q]Ysolde` and `note[E]s` hold their markers.

**Reason.** X03 (the nine markers block) and A§:916 (evidence markers); LT:18's boundary exists to keep a word from matching inside another word, which a bracket already does.

**Follow-up.** *Build:* done. *Test:* `test_F07_X03_...`. *Finding:* F07.

### R08 What a `.docx` reader reads, and what stops it

**Decision.** Besides X35's parts, the reader reads `word/people.xml`, every attribute Word shows (`author`, `initials`, `instr`, `tooltip`, `descr`, `title`, in any namespace) and the `Target` of every relationship with `TargetMode="External"` in `_rels/*.rels`, each as its own line. Part names are matched in any letter case (F40). Exit 3 on any `altChunk` element, any member under `embeddings/` and any member named `.docx`, `.docm`, `.dotx`, `.dotm`, `.htm`, `.html`, `.mht`, `.mhtml`, `.rtf`, `.xlsx`, `.xlsm`, `.pptx` or `.bin`; nested archives are never opened. The DTD guard also runs on the part with its zero bytes removed, so a UTF-16 part is guarded too (F29).

**Reason.** X35: what travels with the file reaches the client, and reading it is the fail-safe side; A§:920: a draft the lint cannot read cannot be marked ready.

**Follow-up.** *Build:* done. *Test:* `test_F08_X35_...`, `test_F29_X35_...`, `test_F40_X35_...`. *Findings:* F08, F29, F40. **For the user's nod:** a draft `.docx` with an embedded object or an imported chunk is exit 3 until the object is removed.

**Answered 2026-10-19 (the user, relayed by the planning session):** keep the stop, in plain words, and build nothing more for embedded files. "I don't think this would ever happen. The only embedded item would be an image at most, but never another file. I would skip this functionality/worry until we cross the bridge. For now, the plug in would just say there was another file, please extract that and submit it seperately." *Applied the same day:* an embedded file, a nested document or an imported chunk is exit 3 with problem "this document has another file inside it" and expected "take that file out and add it as its own input, then run this again"; a picture under `word/media/` never trips it, and neither does a printer-settings part (`word/printerSettings/printerSettings<n>.bin`), which holds no text. Test: `test_R08_another_file_inside_stops_in_plain_words_and_a_picture_passes`.

### R09 A folder linked into a scanned folder is walked, or stops

**Decision.** `scan` follows a linked folder inside a scanned folder when it resolves inside the record (each real folder once) and is exit 3 naming the link when it resolves outside. The sets reader (`record_files`) is unchanged.

**Reason.** X35 and BP:158.32: anything in the folder the lint cannot check is a stop; a linked file was already handled this way.

**Follow-up.** *Build:* done. *Test:* `test_F09_X35_...`. *Finding:* F09.

### R10 Credentials just outside the six shapes

**Decision.** X15's shapes widen as follows, all in the `credential-shapes` region and never cleared:

- shape 1 also takes an `Authorization:` header with any scheme and eight or more characters, and `basic` with eight or more base64 characters when they hold a digit, `+`, `/` or `=`, or start lower case with a capital inside;
- shape 2's key word may carry a prefix (`secret_key`, `private_token`, `my-password`), and adds `pw`, `passphrase` and `passcode`;
- a looser pair takes the key words above and `api key`, `access key`, `client secret`, `login`, `credentials` and `key`, with `:`, `=`, `|`, ` is ` or ` was ` as the separator, only when the value looks like a secret (a digit, a capital after a small letter, or a mark such as `.`, `@`, `_` or `/` inside it, a passphrase's hyphens too; never a common word or a single hyphenated word);
- a key word at a line's end with `:` or `=`, and a secret-like value starting the next line;
- shape 4 takes any parameter whose name ends in `token`, `key`, `secret`, `password`, `passwd` or `pwd`;
- a run of 32 or more hex digits within 24 characters after a key word;
- every shape also runs on the folded line (F12).

**Reason.** X15 and Y04 with BP:158.17 and A17 ("a prompt never carries a credential"): notes write credentials loosely, and the secret-like test keeps "the password is reset every month" and "Login: use your work email" passing.

**Follow-up.** *Build:* done. *Test:* `test_F10_X15_Y04_...`, `test_F12_X28_...`. *Findings:* F10, F12. **For the user's nod:** the secret-like test, which lets a word-only passphrase after `login:` or ` is ` pass.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "Yes R10 gets my nod"

### R11 Tokenised names match on the token stream

**Decision.** A row of two or more words of the firm, the plugin class, the seller's names and every exclusion also matches its words (and its form without legal suffixes) as consecutive tokens, whatever marks sit between them: emphasis, brackets, a colon, a possessive on any word. The literal and the fused forms stay as they are.

**Reason.** X28 lists the exclusions among the rules that compare normalised words, X24 says emphasis and punctuation never break a match, and X28 step 5 drops a possessive per token.

**Follow-up.** *Build:* done. *Test:* `test_F11_X24_X28_...`. *Finding:* F11.

### R12 Normalisation widened

**Decision.** X28 step 1 also drops the Default_Ignorable_Code_Point characters that are not of category Cf (the Hangul fillers, the combining grapheme joiner, the Mongolian and variation selectors), before and after NFKC. The look-alike table adds the dotless `ı` and `ȷ`, Latin small capitals, Cherokee capitals that read as Latin letters, Armenian `օ`, `ս`, `ո`, `հ`, `զ`, `ց` and three capitals, and a few Cyrillic and Greek letters. U+2028, U+2029 and U+0085 read as line breaks. The slashed path copy is made from the folded line, so a full-width backslash is a path separator. A percent-encoding is decoded until it stops changing, three rounds at most (F41).

**Reason.** X28 steps 1 to 3 for every rule that compares words, and PLAN §3's look-alike and zero-width bypasses; X03 for the path and percent copies.

**Follow-up.** *Build:* done. *Test:* `test_F12_X28_...`, `test_F41_X03_...`. *Findings:* F12, F41.

### R13 A hyphenated literal row matches its words spaced

**Decision.** A literal row made of words joined by spaces, hyphens or full stops and holding a hyphen inside a word (`run-sheet`, `if-asked list`, `never client-facing`) is built from its words with X32's gaps, so `run sheet` and `run, sheet` block as `run-sheet` does. A row with any other mark (the markers, `first demo (v0.1)`) stays literal.

**Reason.** X24 (a hyphen is a separator) and X32 (the gaps of a row of two or more words); X40's mark "never client-facing" must also block written without its hyphen.

**Follow-up.** *Build:* done. *Test:* `test_F13_X24_X32_...`. *Finding:* F13. **For the user's nod:** method rows such as `never-say`, `run-sheet` and `not-obtainable` now also block the ordinary phrases "never say", "run sheet" and "not obtainable"; they are clearable vocabulary, so a client's own use takes an allowlist row and a caution (X10, X39).

**Answered 2026-10-19 (the user, relayed by the planning session):** option (b). "B". A method row's spaced form blocks only where it is not an everyday phrase: "run sheet" and "if asked list" block spaced, while "never say", "not obtainable", "cost of waiting" and "exit ramp" block only hyphenated, so an agent prompt's "Never say a price" passes. The same test is applied to the other hyphenated method rows, and the picks are listed for the user's nod. *Owed:* the change, in the follow-up after the part 2 fixes.

### R14 Near copies with a word dropped or added, and near quotes

**Decision.** The near copy of X24 also matches a checked window of seven words that equals an eight-word window of R with one word left out (a word dropped), and a checked eight-word window that equals one with a word left out on each side (a word added). The same eight-word check, with the deletion check, runs against Q as a `quote` block with `near: true`, but only at the six inner positions of an eight-word window, so seven consecutive quote words still never block (L90, L252). Both use the common-word filter of X19 (two of the window's words outside the common words) and the precedence of X36.

**Reason.** X24 added the near copy for PLAN §3's "copied run with one word changed"; a dropped or added word is the same light edit. X24 and X36 make the quote rule the one guard on block-held text.

**Follow-up.** *Build:* done. *Test:* `test_F14_X24_...`, `test_F15_X24_X36_...`. *Findings:* F14, F15. **For the user's nod:** a near quote is filtered by the common-word test, which the exact quote rule is not.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "yes"

### R15 Record paths the shipped rows now cover

**Decision.** `shared/leak-terms.txt`, class `id-patterns`, gains the literals `meetings.md`, `readiness.md`, `close-out.md`, `exclusions.md` and `allowlist.md`, the row `re: \b(?:research|solution|versions|drafts|deliverables|live)/(?=[\w.-]*\.(?:md|txt|docx|json)\b|[\w.-]+/|\s|$)` (a record folder followed by a file, another folder, a space or the end, so "solution/approach" passes) and `re: %USERPROFILE%|\$HOME\b`. The `Pinned: leak` section is unchanged.

**Reason.** A§:916 ("record paths") and X03 (paths in either spelling through the shipped rows); RM pins these folders and files.

**Follow-up.** *Build:* done. *Test:* `test_F16_X03_...`. *Finding:* F16. **For the user's nod:** the review asked for the user's word on a change to the shipped list.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "yes"

### R16 A th heard as t is a second phonetic key

**Decision.** A phonetic source whose letters hold `th` or `ph` has a second key with `th` read as `t` and `ph` as `p`; a candidate matching either key blocks. Candidates keep one key.

**Reason.** X32 and D24 with BP:158.28: a transcript spells a name the way it sounds; the edit distance alone misses `Timbel` for a seven-letter source.

**Follow-up.** *Build:* done. *Test:* `test_F17_X32_...`. *Finding:* F17.

### R17 Internal notes in their common spellings

**Decision.** The `internal-notes` region adds the phrases "not client-facing", "internal use only" and "not for clients"; the speaker label is `speaker` with optional spaces or an underscore and a number (`SPEAKER_00`), or a single letter followed by `:`, `)` or `]` (`Speaker A:`); and a `---` line opening a block that holds a `schema:` line anywhere before its closing `---` (within forty lines) is reported at the hyphens. This widens X40 and Y07.

**Reason.** X40 and Y07: the marks of internal files are "the one shape a string rule can recognise for certain", so their common spellings belong with them.

**Follow-up.** *Build:* done. *Test:* `test_F18_X40_...`. *Finding:* F18. **For the user's nod:** "internal use only" and "not for clients" block and are never cleared, so a client's own board described as "for internal use only" must be worded otherwise, as "internal only" already must.

**Answered 2026-10-19 (the user, relayed by the planning session):** option (b). "b". "internal only", "internal use only" and "not for clients" still block by default, but become clearable per client through the allowlist, passing with a caution (a Service build may say "Internal use only, not visible to the customer"); speaker labels and note front-matter blocks stay never cleared. *Owed:* the change, in the follow-up after the part 2 fixes.

### R18 An `ok` that says no clears nothing

**Decision.** An allowlist row whose `ok` value's first word is `no`, `not`, `nope`, `never`, `pending`, `tbc`, `tbd`, `todo`, `ask`, `asked`, `awaiting`, `waiting`, `unanswered`, `unknown`, `maybe`, `none`, `false` or `n` clears nothing and warns on every run, as a row with no `ok` does.

**Reason.** X09 (`ok` is "the user's words, or `yes`") and A§:920 ("every row needs the user's OK").

**Follow-up.** *Build:* done. *Test:* `test_F19_X09_...`. *Finding:* F19.

### R19 A mark written slightly wrong is a malformed mark

**Decision.** A line that reads like one of the four marks once folded (letter case, spacing, a missing space and a dash look-alike aside) but is not the exact mark is a mark not well formed: exit 3 in mode `client-safe-block`, the record warning when the sets are read, and for a glossary mark `blueprint`'s warning, with the text from the mark to the next heading checked.

**Reason.** X38 keeps the three categories out of the block "at the moment call-intake writes it"; X09 makes a malformed mark exempt nothing; BP:158.32.

**Follow-up.** *Build:* done. *Test:* `test_F20_X09_X38_...`. *Finding:* F20.

### R20 The local list's patterns are checked at every depth

**Decision.** Besides X33's static check, a local `re:` row is parsed with the standard regular-expression parser (`re._parser` from Python 3.11, `sre_parse` before) and is exit 3 at load when a repeat of two or more holds, at any depth, a repeat of variable length or an alternation, such as `(a|aa)+` or `(?:(?:a+))+`. A fixed count (`(?:,\d{3})+`) and a single-character alternation the parser turns into a set are not refused.

**Reason.** X33 and X42 ("with patterns checked and inputs capped, a run is bounded by its input"); the old check saw only a quantified group with no inner parentheses.

**Follow-up.** *Build:* done. *Test:* `test_F21_X33_X42_...`. *Finding:* F21.

### R21 A thousands comma followed by a break or a space joins a split figure

**Decision.** Z05 item 1 gains a joiner: a `,`, `'` or `’` followed by spaces or a line break joins two digit groups when the next group has three digits.

**Reason.** X25: a figure split by a line break is a split rendering, the first structural assertion.

**Follow-up.** *Build:* done. *Test:* `test_F22_X25_...`, `test_F05_...` (`184,<br>260`). *Finding:* F22.

### R22 A scan that judges nothing is exit 3

**Decision.** `scan` with no file to check (no path given and no file under any `drafts/` or `deliverables/handoff/`, or a path given that holds no file) is exit 3, field `path`, "no draft or handoff file to check". This replaces Z07's "a scan that checks no file prints `full`". No `--allow-empty` flag is added, since no caller needs one yet.

**Reason.** A§:920 and BP:158.32: "no draft is marked ready" when the lint cannot run; Z09's reasoning, a gate that fails closed has no path to 0 that checked nothing.

**Follow-up.** *Build:* done. *Test:* `test_F23_Z07_...`. *Owed elsewhere:* WP12's close-out runs `scan` only for a strand with drafts or handoff files, or reads exit 3 with this field as "nothing to check" and says so to the user (section 6). *Finding:* F23. **For the user's nod:** a strand with no draft at close-out stops rather than reading clean.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes, "nothing to check" rather than "all clean". "Whoops, I'd say nothing to check."

### R23 The paraphrase rule's person and process cues, narrowed

**Decision.** Three readings of X06's rule:

1. A role word counts as a person reference only when a possessive pronoun or a possessive name sits in the two tokens before it (`her manager`, `Ysolde's manager`), or a capitalised name sits directly beside it (`the approver, Penwith`). A capitalised name not first in its sentence counts as before.
2. `owner` and `lead` are no longer role words (X19 lists `owner` as a monday word; "lead time").
3. The cues `signs off`, `approver`, `a risk`, `blocker`, `holiday` and `holidays` count only beside a name, never beside a role word; `english`, `american` and `visa` leave the health-identity group, as Z08 dropped three trade demonyms.

This narrows what blocks. "The manager is burnt out." now passes; "Her manager is burnt out." and "We heard Ysolde is burnt out." still block.

**Reason.** X06 chose the fail-safe side because "a false block costs a rewrite", but a rule that blocks ordinary SOP text ("the item owner signs off", "if a fitter is sick, the supervisor reassigns the job") gets each strand an allowlist row per sentence, which hides the real cases. Z08 already narrowed the same group for the same reason. A§:916's three categories concern people, which a possessive or a name identifies; a bare role word in a procedure does not.

**Follow-up.** *Build:* done. *Test:* `test_F24_X06_...`. *Finding:* F24. **For the user's nod:** a remark about an unnamed "the manager" passes.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "yes"

### R24 The tool-category assertion: plurals, abbreviations and everyday nouns

**Decision.** A counted row also matches with a plural `s` or `es`. A full stop after `e.g.`, `i.e.`, `etc.`, `vs.` or `approx.` does not end a sentence (for every rule that reads sentences). The rows `spreadsheet`, `spreadsheets`, `wiki`, `team chat`, `shared drive`, `shared inbox` and `email client` count toward the three only when the sentence also holds a more specific category. A day or a month, plural or short (`Fridays`, `Sept`), is never a proper noun (F37).

**Reason.** X12 is fail-safe over precise and offers no allowlist; a rule that blocks "Export the spreadsheet to the shared drive and post the link in team chat" gets switched off, which loses what X12 protects. The plural and abbreviation readings only add blocks.

**Follow-up.** *Build:* done. *Test:* `test_F25_X12_...`, `test_F37_X12_...`. *Findings:* F25, F37. **For the user's nod:** three everyday tool nouns alone in one sentence pass.

**Answered 2026-10-19 (the user, relayed by the planning session):** moot. "Yes, and also, the blocking of client's tools in sentences sounds too strict"; asked to choose, the user chose to drop the check: the tool-category assertion is dropped everywhere until v2 or v3, recorded under A30 ("Added 2026-10-19, the tool-category check dropped for now"); the split-figure assertion stays. *Owed:* removing the check and its tests, the clauses it proved marked changed by decision (A30), and the A§9.6, BP:158 and `safety.md` touch-ups listed, in the follow-up after the part 2 fixes.

### R25 A JSON string that is walked skips the id rows as a raw string

**Decision.** A payload string that parses as a JSON object or list, and so is walked (X22), is not checked by the eight-digit id row or the split-id rule as a raw string; every other rule still runs on it, and every value inside is checked by the walk, the id row included (R02).

**Reason.** Y08: "inside a `column_values` JSON string the same rule applies at every depth"; without this every connect-boards or people value blocked on its own structural ids, with nothing to clear it.

**Follow-up.** *Build:* done. *Test:* `test_F26_Y08_...`. *Finding:* F26.

### R26 Long numbers that are not ids

**Decision.** The id row (the shipped row, Z03's widening and R02) skips digits that follow a decimal point which follows a digit (a coordinate's tail), and turns eight digits that form a real `YYYYMMDD` date from 1900 to 2099 into the `split-figure` date warning of Y02. Every other run of eight digits or more still blocks.

**Reason.** Z03 asked step 7 to probe the cost of its widening; Y02 already treats a date in spaced groups as a date that warns, so nothing passes silently.

**Follow-up.** *Build:* done. *Test:* `test_F27_Z03_Y02_...`. *Finding:* F27. **For the user's nod:** an eight-digit id that happens to read as a date only warns, as Y02 accepted for the spaced form.

**Answered 2026-10-19 (the user, relayed by the planning session):** yes. "yes im okay with that"

### R27 Only a link with a scheme hides its ids

**Decision.** For the id row, only a link target that starts with `http://`, `https://` or `mailto:` is masked; a relative Markdown or `href` target such as `boards/<id>` is checked. A bare URL stops at a comma or a pipe, so an id after one is checked. This narrows X34's "the target of a Markdown link" for the id row's mask.

**Reason.** Z03: a URL without a scheme "only looks like a link", and its ids block; BP:158.8 exempts ids inside links only.

**Follow-up.** *Build:* done. *Test:* `test_F31_F32_X34_...`. *Findings:* F31, F32. **For the user's nod:** the review asked for it.

**Answered 2026-10-19 (the user, relayed by the planning session):** widened. "I would say also include things as links if it has the .com/ or monday.com/". Reading: besides a link with a scheme, a web address written without one whose host ends in `.com` followed by `/` (so `yourcompany.monday.com/boards/123` and `example.com/page`) also counts as a link that hides its ids; other endings stay checked unless the user says otherwise. *Owed:* the change, in the follow-up after the part 2 fixes.

### R28 Settings read strictly

**Decision.** `settings.json` with a key written twice in one object is exit 3, and a seller id, slug, workspace name or GitHub account that holds no letter or digit (blank, spaces only, `--`) is exit 3 naming the field, rather than dropped.

**Reason.** A§:920 and X33: a list the lint cannot apply as written is a stop; a dropped value would remove a block without a word.

**Follow-up.** *Build:* done. *Test:* `test_F39_X04_...`. *Finding:* F39.

### For the user's nod (step 8)

R03 (a raw `.md` with front matter is internal), R08 (a `.docx` with an embedded object is exit 3), R10 (the secret-like test), R13 (hyphenated method rows block their spaced phrases), R14 (near quotes, filtered), R15 (the shipped list's new rows), R17 (two new internal-note phrases, never cleared), R22 (an empty scan is exit 3), R23 (the paraphrase rule narrowed), R24 (three everyday tool nouns pass), R26 (an eight-digit date only warns), R27 (only a schemed link hides an id).

---

## Added by the review fixes, part 2 (step 8), 2026-10-19

The adversarial review of part 2 (`leak-review-part2.md`, G01 to G29) found places where the wall, its index, the payload walker, `blueprint` or `terms` let a leak through. The fixes below make or change a decision; each is settled on the fail-safe side unless the entry says it narrows a block, and then it names the source that wins. No earlier entry is edited; an R entry says which one it reads, widens or narrows. A30 (the user's reading nodded on 2026-10-19) bounds the wall: another client's name, term or figure in its normal forms, not misspellings by sound. Every R entry has a unit test in `tests/unit/test_leak_wall.py` named after its finding (`test_G01_...` onward).

### R29 The harvest's stop list is a reviewed region, not the live `shared/` folder

**Decision.** The words of the plugin's own `shared/*.md` and `shared/*.txt` files that X26 step 6 and Z12 put in the stop list come from a pinned region of the script, `shared-words` (`SHARED_WORDS`), and never from the folder as it is at run time. `wall_stop` reads no folder. `shared_vocabulary()` gives what the region should hold for the folder as it is now; the unit test `test_G01_Z12_...` fails whenever the two differ, in either direction. The region is regenerated only after `terms` over the changed `shared/` has passed against the region as it was. One word, the PDF tool name that L05 bars from the script text, is left out of the region, which can only keep it as a name, never clear one. Z12 is narrowed in its source only: the same words are stop words, read from a reviewed copy.

**Reason.** X31 and BP:114 win over Z12's "read fresh": `terms` is there to prove that nothing from any client input is in `shared/`, so `shared/` cannot be trusted as the source of the very stop list `terms` relies on. Read live, a client name that had leaked into `shared/` dropped out of its own client's entry at the next `index`, after which `terms` passed it and every other record's wall lost it (U1: the entry holds the record's names).

**Follow-up.** *Build:* done. *Test:* `test_G01_X31_L195_U1_a_name_leaked_into_shared_stays_in_its_entry_and_terms_blocks_it`, `test_G01_Z12_the_embedded_shared_words_equal_the_shipped_shared_folder`; `test_L274_L275_...` counts the twelfth region. *Touch-up:* the review asked for `tools/lint_plugin.py` to compare the region; this run may not edit that tool, so the unit test holds the comparison, and moving it into the release check is left for a later run. *Finding:* G01.

### R30 Letters with no decomposition are spelt plain, and three have a second reading on the wall

**Decision.** `fold` (X28 step 4) now spells the Latin letters that NFD does not decompose as plain letters, after case folding: ø as o, æ as ae, œ as oe, ł as l, đ and ð as d, þ as th, ħ as h, ŧ as t, ı as i, ŀ as l (`UNDECOMPOSED`, in the `confusables` region). Since `fold` serves every rule, the single-text rules gain the same reading. The wall also tries the second reading of ø (oe), æ (a) and œ (o) (`ALT_READINGS`) on both sides of the hash: an entry's harvest, the `CLIENT.md` name and the exclusion terms add the second reading's forms when the source holds one of the three letters, O adds them for this record's own files, and a checked text holding one is read both ways. The single-text rules take the first reading only.

**Reason.** X28 step 4 and PLAN §3 ("diacritics") win: a name is compared with its diacritics folded on both sides, and people write these names without the special letter as often as with it. Without a table, the letters were dropped from the key and kept in the digest, so `Ostby` never met `Østby` in either direction. A30 bounds the second readings to the normal transliterations, not to spellings by sound.

**Follow-up.** *Build:* done. *Test:* `test_G02_X28_letters_with_no_decomposition_meet_their_plain_spellings`, `test_G02_X28_the_other_way_round_a_plain_record_name_meets_the_special_letter`. *Touch-up:* the second reading on the single-text rules (a record's own exclusion term written with ø, met by a draft written with oe) is not built; the first reading covers the plain spelling. *Finding:* G02.

### R31 A word broken by a line-end hyphen or by Markdown marks is fused on the wall

**Decision.** The wall's fuse gaps (`FUSE_GAP`, read by `wall_candidates`, X27 type 3) now also hold a hyphen at a line end with spaces or tabs on either side of the break (`-[ \t]*\r?\n[ \t]*`), and any run of the Markdown marks `*`, `_`, `~` and the backtick. So `Tallow-` at a line end before `mere`, `Fern- ` before ` hollow`, `Tallow**mere**`, `Tallow~~mere~~` and the same with a backtick all yield the fused candidate. The spaced twin is still a candidate, as before, so a real compound broken at a line end still meets its spaced name, and the hyphen form adds the fused word only. X24 is unchanged: the marks stay separators for the word rules, and only the wall fuses across them. A dash with a space before it, a line break with no hyphen, a hyphen before a blank line, and marks with a space beside them are not fuse gaps.

**Reason.** X27 type 3 wins: tokens joined with no space are one word, and PLAN §3 names hyphenation for the review. A line-end hyphen is the same word split for layout, and the Markdown forms render as the name, so a two-token cut let `Tallowmere` through in every one. Since wall/1 serves both sides, O gains the same fused forms from this record's own files; that can clear a block only where this record itself writes the word, which is what O is for.

**Follow-up.** *Build:* done. *Test:* `test_G03_X27_a_name_broken_by_a_line_end_hyphen_or_a_markdown_mark_is_fused` (a product and the client's name across the line-end hyphen with and without spaces; `**`, `*`, `~~`, `__` and a backtick; a `doc` payload's `markdown`; the candidates of `Blue-` and `Harbour`; and clean controls that keep `on` and `track` apart). *Touch-up:* the harvest's own gap (`HARVEST_GAP`) is unchanged, so a record that writes its own name broken across a line still harvests only the capitalised half; the checked side is where the finding was. *Nod:* a mark on one side of a word only, as in `**on**track`, fuses the two words; that is the fail-safe reading, and it may block an ordinary pair written that way. *Finding:* G03.

### R32 A run of two or more words is dropped only as a plugin phrase or a run of X26's own stop words

**Decision.** `kept` (X26 step 5) drops a candidate of two or more words only when the run, as a phrase, is in the pinned region `shared-phrases` (`SHARED_PHRASES`), or when every word is in X26 step 6's own small list: the days and months, the product words, the titles and the role and common acronyms, and the words of the shipped plugin, assistant, method and markers rows. A word of `shared/` (Z12, the `shared-words` region of R29) still drops a single word, and no longer drops a run because each of its words is one. A phrase in the plugin vocabulary is a capitalised run of two to four words that the harvest cuts from `shared/*.md` and `shared/*.txt` (X26 step 2, legal suffixes stripped), whose every word is made of letters and is a stop word of the whole list; headings are counted where they are written as such runs. The region holds 67 phrases today (`native crm`, `in progress`, `sales targets`, `work management` and so on). Like the words, the phrases come from the reviewed region and never from the folder at run time (R29); `shared_phrases()` gives what the region should hold for the folder as it is now, and a unit test fails whenever the two differ. `wall_stop` now also returns the small list. The same rule cuts the other folders' slugs (X21), so a slug's sub-run of two `shared/` words is now a slug form too.

**Reason.** U1 and A§:918 win over Z12's reach: the entry holds the client's partners and products as the record names them, and "a partner name that reads as two ordinary words" is one of the trap categories. Z12 was written to keep the plugin's own headings and single ordinary words out of the digests; read word by word it also dropped any name whose two words both happen to appear somewhere in `shared/`, such as `Signal Path`. A phrase list keeps what Z12 was for (the plugin's own runs never publish, so `terms` over `shared/` still passes, L197) while a name built from those words is published. Every phrase of the region has every word in the old stop list, so the new drops are a subset of the old ones and the change only widens what an entry publishes; nothing that blocked before passes now.

**Follow-up.** *Build:* done. *Test:* `test_G04_U1_X26_a_partner_name_of_two_ordinary_or_shared_words_is_published_and_blocks` (record b's `Green Field`, `Clear Path` and `Signal Path` are in its entry and block in record a's text, with `Blue Harbour` as the control that already blocked; clean controls: the plugin phrase `Native CRM`, the run `Monday CRM` of small-list words, and the single words `signal` and `path` stay out of the entry and pass), `test_G04_Z12_the_embedded_shared_phrases_equal_the_shipped_shared_folder`; `test_L274_L275_...` counts the thirteenth region. `Signal Path` and the region test failed before the change; `Green Field` and `Clear Path` already blocked, because R29's region leaves out the common words that the live reading the review saw had held. L197 and every clean twin of `test_leak_grading.py` pass. *Measured:* the two planted records publish the same multi-word candidates as before (12 each, none added). Of the 2,970 two-word names built from 55 words firms use in names, the script before this change dropped 110 (11 of the 55 words are stop words; the review's 462 and 22 predate R29); it now drops 2, `Anchor Gate` both ways, because both words come from the shipped plugin rows that X26 step 6 names. *Touch-up:* the phrase comparison sits in the unit test beside R29's, not in `tools/lint_plugin.py`, for the same reason. The widening is on the fail-safe side: another record's capitalised run of two ordinary or `shared/` words now publishes, so the same run in this record's text blocks unless this record also writes it, and `terms` at release can stop on a record heading that `shared/` writes in lower case; no such case showed up in the fixture or the count. *Nod:* runs holding a word with a digit (`P G01`, `H1 and H2`, `D1 and D2`) are left out of the region to keep it small, so a record that writes `H1 and H2` as a name-like run publishes it, and the same words in another record's text block. *Finding:* G04.

### R33 A long exclusion term also publishes its windows of two to four words

**Decision.** `build_entry` (X26, the `terms` list of X02) now publishes, for an exclusion term or name of five words or more, every window of two to four consecutive words of it as well as the whole term, each in the spaced and fused forms the entry already uses and in both readings of R30's letters (`term_windows`). A window is left out when every word is a common word or a word of X26's own small list (R32's `small`: days and months, product words, titles and acronyms, the shipped plugin, assistant, method and markers rows), or when it is a phrase of the `shared-phrases` region. A term of four words or fewer publishes exactly what it did before. `wall_candidates` is unchanged, so `wall/1`'s cut and `clients-index/1` do not change. The user chose this fix, the review's first, over a narrower one of four-word windows only, on 2026-10-21, in their words: "take the review's G05 fix as written (windows of two to four words)".

**Reason.** U1 and X26 win: the entry holds every term row of every strand's `exclusions.md`, and the wall is there to stop it in another client's text. `wall/1` cuts no run longer than four words (X27 type 2), so a term of five words or more was published only in a form that no checked text could ever produce, and `night shift overtime rebate scheme` passed in full, spaced or hyphenated. Windows meet the cut where it is, which keeps `wall/1` and the index schema as they are.

**Follow-up.** *Build:* done. *Test:* `test_G05_R33_U1_X26_an_exclusion_term_of_five_words_or_more_blocks_on_the_wall` (record b's `night shift overtime rebate scheme` as a term and `Harrow Lane yard expansion plan` as a name block in record a's text spaced, hyphenated and as the name, with the four-word control `the depot lease buyback`; the windows `overtime rebate scheme`, `Harrow Lane yard`, `rebate scheme`, `night shift` and `expansion plan` block on their own), `test_G05_R33_a_window_of_common_words_only_is_not_published` (of `crate return for the night`, `crate return` and its longer windows are published and block, while `for the night`, `the night`, `return for` and `return for the night` are not published and `Book the room for the night.` passes), `test_G05_R33_a_term_of_four_words_or_fewer_publishes_what_it_did_before` (the entry's `terms` equal the whole-term forms exactly, and `The depot lease is new.` passes). The first two failed before the change. The two planted records, whose terms are of two words, publish the same entries, and every clean twin of `test_leak_grading.py` passes. *Measured:* each of the two review terms has nine windows (four of two words, three of three, two of four); all nine are published for each, 18 windows and 36 digests in all, and none is left out, since every window holds a word that is not common (`shift`, `overtime`, `rebate`, `scheme`, `harrow`, `lane`, `yard`, `expansion`). The test's `crate return for the night` publishes three of its nine and leaves out six. *What the user accepted:* a two- or three-word slice of another client's long term now blocks this client's ordinary text when the slice is not all common words: with record b's terms above, `Our rebate scheme is new.`, `night shift` and `expansion plan` in record a's text block unless record a writes them too. That is the fail-safe side, and its cost is false blocks on ordinary pairs drawn from another client's long terms. *Touch-up:* none; the wall's notes in the API note gain T2. *Nod:* the review says "common or stop words" without naming the stop list. This reads it as R32 does for runs: the common words plus X26's own small list, and the `shared-phrases` region, not the `shared/` words of Z12, which filter single words only since R32. So a window such as `expansion plan` (a `shared/` word and a common word) is published; the phrase region keeps a window the plugin itself writes from stopping `terms` over `shared/` at release (L197). *Finding:* G05.

### R34 A JSON string literal in a payload string is walked as its own unit

**Decision.** The payload walker (`payload_units`, X22) drops the format characters (category Cf and the F12 ignorables) from a string before it decides whether the string holds JSON, and now tries `json.loads` on a stripped form that starts with `{`, `[` or `"`. A result that is an object or a list is walked as before, and R25 still spares the raw string the id rows. A result that is a string, which is what a text column's value is (`change_column_value` takes `"\"…\""`, and `json.dumps` writes non-ASCII letters as `\uXXXX`), is checked as its own unit at `<path><json>`, and it goes through the same test in turn, so a JSON string nested inside a string literal is walked too, within the existing depth limit of 64. A string that starts with `"` and does not parse is checked as raw text only, with no error. The raw string keeps every rule, the id rows included, because R25's reason (structural ids inside a walked object) does not reach a single string value.

**Reason.** X22 ("a string that parses as JSON is also walked") and L134 (no field the walker does not visit) win: the walker opened only objects and lists, so a text column's value was read with its escapes intact, `Østby` never met `Østby`, and another client's name went to monday under the commonest value shape there is. A zero-width space before a `column_values` object hid it the same way, because `str.strip` keeps format characters.

**Follow-up.** *Build:* done. *Test:* `test_G06_R34_X22_L134_a_json_string_literal_is_walked_as_its_own_unit` (record b's `Østby` and `Tallowmere` block in record a's `item_batch` payload at `$.value<json>` as a text column's escaped value with its board and column ids, and as `"Tällowmere desk"` folded; at `$.column_values<json>.text_1` behind a zero-width space; and at `$.column_values<json><json>.text_1` as an object string quoted again. The controls, which blocked before: the plain string, the object string, and JSON nested twice. Clean: a string that opens with a quoted word, an unclosed quote, a literal of ordinary words, and a literal behind a zero-width space all exit 0.) It failed before the change at the first case. *Touch-up:* the API note gains T3. *Nod:* a whole payload value written as a quoted sentence, with its quotes, is now checked twice, with and without them; that can add findings, never clear one. *Finding:* G06.

### R35 One slug, two clients: the twin folder stops the run, and an entry is own only when it holds this record's name

**Decision.** Three changes to the lint. First, `twin_folder` stops every run that builds the wall from a record (`payload`, `blueprint`, `scan` in full and client-safe-block modes, `wall`) and every `index` run with exit 3 when a folder of this record's name exists under the home's other root: `archive/` for a record in `clients/`, `clients/` for a record in `archive/`, either for a record outside the home. It looks at those two paths only (no listing, no file opened), counts a path it cannot look at as a twin, and its error names the root and no folder or name (X30): problem "a folder with this record's name is also under <home>/archive/, so the wall cannot tell this record from that client", expected "one folder per slug across <home>/clients/ and <home>/archive/: give one of the two records another slug, then run this again". Second, `index` refuses (exit 3, `<home>/clients-index.json`, field `entries`) to replace an entry under this record's key that does not hold the digest of this record's `CLIENT.md` name in its `names` (`name_key`, the full spaced form X26 step 1 always publishes); a record with no name cannot replace an entry either. Re-indexing the same client, same name, replaces its own entry as before. Third, `build_wall` skips the entry under this record's key as its own only when that entry holds this record's name; otherwise the entry stays on the wall as another client's, so a record created on a slug whose archived folder is gone still sees the old client's names. The `clients-index/1` shape is unchanged. Z18 item 4 now holds only once `twin_folder` has passed, and Z18 item 2 gains two path checks for `index`.

**Reason.** X29 and L178 win over Z18 item 4: "no entry is ever removed: an entry whose record no longer exists stays and keeps that client walled". Z18 item 4's "a folder with this record's own name is this record" held only while slugs are unique across `clients/` and `archive/`, which nothing enforced, so a new client on an archived client's slug skipped that client's entry as its own and its first `index` overwrote it, and then every other record lost the archived client's wall. The digest the entry already holds tells the two apart without a new field, so the pinned shape stays (the review's other fix, a name digest field in the entry, would change it). Exit 3 with no folder named follows X30, which keeps other clients' slugs out of this session.

**Follow-up.** *Build:* done. *Test:* `test_G07_R35_X29_L178_two_records_with_one_slug_never_take_the_archived_clients_wall` (an archived client at `archive/brindle-tiles`, named Brindle Tiles Ltd, indexed with `Tallowmere` and `Odalys Brekke`; a new client Brindle Tiles Co at `clients/brindle-tiles`; a third record `clients/corbel-hire`: `wall` and `index` from either twin are exit 3 with no slug or name in the error, the entry is unchanged and the third record blocks both names; with the archived folder then removed, the new record's `index` is still exit 3, the entry stays, and `Open Tallowmere today.` blocks from the new record and the third, while the new record's own name passes) failed before the change at its first case. Clean control `test_G07_R35_an_archived_record_with_no_twin_and_a_same_name_reindex_work_as_before` (the archived record, no twin, passes its own `Tallowmere`, re-indexes under the same name with a new name `Quarrow Pine` added, and the third record blocks both) passed before and after. *Owed to WP2:* `record.py init` refuses a slug that already exists under `archive/`, and also a slug whose key `digest("s:", slug)` is already in `clients-index.json`, which covers an archived folder the user has removed; this run may not edit `record.py`. *Touch-up:* the API note gains T4. Two gaps stay: a different client whose name folds to the old entry's name or to the slug's words (a new Brindle Tiles beside an old Brindle Tiles Ltd) passes the name test and is caught only by the twin folder while it exists, and from a third record the stale entry satisfies X30's coverage check for the new folder, so the new client is unwalled for others until it has its own slug; the new record's refused `index` is the loud signal. *Nod:* a client renamed in `CLIENT.md` (same client, new name) is now refused by `index`, because only the name tells a re-index from another client; the old entry stays walled, and the record's new names reach no other record until the user decides how a rename is handled (for example a former-name field in `CLIENT.md`, owed to WP2). *Nod:* a record with no `name` in `CLIENT.md` indexes once and is refused after, the fail-safe reading of an entry that cannot be matched. *Finding:* G07.

### R36 A path under the home that cannot be looked at stops the wall, alike on 3.9 and 3.14

**Decision.** The wall looks at home paths with `os.stat` through one helper, `path_kind`, and no longer with pathlib's `is_dir`, `is_file` or `exists`. No such path (`FileNotFoundError`, `NotADirectoryError`) is "not there", as before; any other failure is exit 3 on both interpreters. In `home_folders`, a folder directly under `<home>/clients/` or `<home>/archive/`, or its `CLIENT.md`, that cannot be looked at (a folder at mode 000, or a root that can be listed but not searched) is exit 3 with `error.file` `<home>/clients/` or `<home>/archive/`, `error.field` `entries`, problem "a folder under the home cannot be read, so the wall cannot tell whether it is a client record", expected "every folder directly under <home>/clients/ and <home>/archive/ readable by the user who runs the lint, then run this again", naming no folder. `twin_folder` (R35) now counts a path it cannot look at as a twin under 3.14 too, as R35 says. `read_index` is exit 3, `<home>/clients-index.json`, `(whole file)`, when the index or the mutex `<home>/.work/record.mutex` cannot be looked at, instead of reading the index as absent or the mutex as free. X30's coverage test is unchanged in meaning: `CLIENT.md` counts when it is a regular file, a link followed.

**Reason.** X30 and A24 win. pathlib's checks changed between the two interpreters: under 3.9 they raise `PermissionError`, and L205's handler printed its message, which held the other record's full path and so its slug; under 3.14 they answer False, so the unreadable record counted as a slug only, the coverage check never saw it, and the run passed. X30 fails closed and names no folder, because the slug would carry that client into this session; A24 asks for identical behaviour on both systems, which includes both supported interpreters; L205 makes every unexpected failure exit 3. The review's fix, `os.stat` in a `try`, gives one answer on both.

**Follow-up.** *Build:* done. *Test:* `test_G08_R36_X30_A24_L205_a_record_folder_that_cannot_be_searched_is_exit_3_naming_no_folder` (record b holds `Tallowmere`, never indexed, its folder at mode 000: `wall --text "Open Tallowmere today."` and the payload `{"name": "Tallowmere loads"}` are exit 3 with the error above, and no slug or name of record b anywhere in the envelope; with the mode restored, X30's coverage check stops the run, and once b is indexed the text blocks) failed before the change under both interpreters, naming b's path under 3.9 and passing with exit 0 under 3.14; `test_G08_R36_R35_A24_an_archive_that_can_be_listed_but_not_searched_is_exit_3_naming_no_folder` (record b moved to `archive/`, the archive at mode 400: `wall`, `payload` and `index` are exit 3 on `<home>/archive/`, naming nothing of b) failed before the change under 3.14 only. Both skip on Windows and when the tests run as root, where these modes deny nothing; both restore the mode before the temporary home is removed. `ReviewPart2Test` passes under 3.9.6 and 3.14.6. *Touch-up:* the API note gains T5. Left as they are, since neither is the wall's and neither differs in its exit code: `load_local` and `load_settings` under `<home>/local/` (an unsearchable `local/` is exit 3 on both, because the settings file is required), and `locate`'s look at this record's own `CLIENT.md` (exit 3 on both, naming only this record). *Nod:* a folder under the home, or a `CLIENT.md`, that is a link loop or fails in any other way than "not there" was "no record" under 3.9's pathlib and is now exit 3; this is the fail-safe reading, and the user can list their own home to find it. *Finding:* G08.

### R37 While a blueprint is checked, none of its strand's blueprint files makes its words this record's

**Decision.** Z15 now leaves out of O, while a blueprint file is checked, every blueprint file of the same strand: `strands/<strand>/solution/blueprint.md` and every `strands/<strand>/versions/*/blueprint-r*.md` (X11's blueprint row, `kind_of` giving `blueprint`), not only the checked path. So a word of the blueprint counts as this record's only when a file outside that strand's blueprint files holds it. `Own.left_out(file)` gives the files left out; `Own.has` subtracts each of them. Every other checked file still leaves out only itself, as before. Three things stay as they were: another strand's blueprint and its frozen copies are O sources for this strand's check; a word held by any other file of the record (a call, the research, `STRAND.md`) is still this record's; and payloads are unchanged, so a planned name from the blueprint passes in a payload, as X11 decided.

**Reason.** Z15, X45, L189 and P5's build-guard check (X47) win: a checked record file never makes its own words this record's, and `blueprint` runs again at the build guard to catch what the index learned after the draft check, for example another record indexed since. `record.py freeze` writes the approved blueprint's bytes into `versions/`, and that copy is an O source (X11), so after the freeze every word of the blueprint was its own and the build-guard check could never block on the wall: the finding's `Tallowmere` blocked before the freeze and passed after it. The frozen copies are the blueprint itself, so Z15's reason covers them. The change only takes words out of O for a blueprint check, so it can add blocks and never clear one.

**Follow-up.** *Build:* done. *Test:* `test_G09_R37_Z15_X45_L189_the_frozen_blueprint_copy_never_makes_its_own_words_this_records` (record b holds `Tallowmere`; record a's blueprint reads `Jobs board, with a Tallowmere sync column for depot loads.` in section 4; `blueprint` blocks before the freeze, with one frozen copy, and with two; the payload `{"name": "Tallowmere sync"}` still passes) failed before the change at the first frozen copy. `test_G09_R37_a_word_held_outside_this_strands_blueprint_files_is_still_this_records` (clean: the word in record a's research brief, or in strand 002's blueprint, or in strand 002's frozen copy alone, makes it this record's and strand 001's check passes; then strand 002's own check, with its frozen copy present and strand 001 holding nothing, blocks) failed before the change at its last case only; its clean cases passed before and after. Both pass under 3.9.6 and 3.14.6. *Touch-up:* the API note gains T6. One gap stays by X11's design: a name that reached one strand's blueprint unchecked is O for another strand's check and for payloads. The review's second fix would close it for payloads, and is left for the user's word. In plain terms: today a blueprint's client-facing lines count as this record's own words for every payload, whether or not the blueprint passed its check. The second fix would count them only while the latest `blueprint` run on exactly those bytes was clean, so a name that came into the blueprint without a clean check, or that another record was indexed with after the check, would block in the payload too instead of passing. It would change X11's table (the blueprint row becomes "O for payloads only after a clean run"), and it needs a record of each `blueprint` run that the payload check can read: the blueprint's `inputs` hash and the verdict, kept with the strand. The lint writes only the index (L09), so either the caller (solution-blueprint, WP9) keeps that record and the lint trusts it, or L09 is widened to let the lint write it; and a payload with no such record would treat the blueprint as not this record's, so its planned names block until the blueprint has a clean run. *Nod:* the rule follows the checked file, not the command, so `scan` pointed at a blueprint file or a frozen copy also leaves out the strand's other blueprint files; that only adds blocks. *Finding:* G09.

### R38 A linked folder is walked inside the folder checked and stops outside it, in `terms` and in the record's sets

**Decision.** R09's rule now holds for every walk of the lint, through one helper, `walk_inside` (with `walk_files` for the files): a linked folder is followed when it resolves inside the folder walked, each real folder once, and is exit 3 naming the link when it resolves outside. `terms` walks the folder it checks this way; a linked folder or file that resolves outside that folder is exit 3, `error.file` the link's path relative to the folder, problem "a linked folder resolves outside the folder checked" (or "a linked file"), expected "files inside the folder only; copy them in or remove the link, then run this again". `record_files`, which feeds the sets, O and the index's harvest, does the same with the record as the base: a linked folder inside the record is harvested, and one that resolves outside is exit 3 naming the link's record-relative path, never its target. A file reached through a link is named by its real place, once, so a link never changes a file's name or kind: a strand's `drafts/` reached through `research/` is still a draft and feeds no set. `scan` keeps R09's behaviour and message through the same helper.

**Reason.** X31 and X35 win: anything in the folder the lint cannot check is a stop, and an unread file proves nothing. `os.walk` without `followlinks` lists a linked folder and never descends into it, so `terms` passed a release folder whose linked examples held another client's name, while a release bundle follows links and ships those files. In the record's sets the same skip was the safe side, but the linked file next to it was not: read through the link, a file outside the record made its words this record's, so the wall passed another client's name. X30 keeps the error to the link in this record, because the target may be another client's folder. The change only adds stops and files read; the one name it moves is a file reached through a link, which is now named where it really is.

**Follow-up.** *Build:* done. *Test:* `test_G10_R38_X31_terms_walks_a_linked_folder_inside_the_folder_and_stops_on_one_outside` (record b holds `Tallowmere`; a folder holds `notes.md` and `examples -> ../elsewhere`, whose `example.md` reads `Example: open Tallowmere for the depot loads.`: exit 3 naming `examples` and nothing of `elsewhere`; the control, the same folder copied in, blocks at `examples/example.md`; a link `also -> examples` and a loop `examples/again -> .` give that one finding once; a linked file to `../elsewhere/example.md` is exit 3 naming it; two links that point at each other are exit 3) failed before the change at its first case, exit 0. `test_G10_R38_X30_a_linked_folder_in_the_record_is_harvested_inside_and_stops_outside` (in record a, `research/extra.md` linked to that file, `research/examples` to its folder, and `research/theirs` to record b's `research/`: `wall` and `index` are exit 3 naming the link and nothing of the target or of record b; a link into `drafts/` and one to `calls/` leave the harvest as it was; in record b, `research/linked-plan -> more` is harvested once, as `research/more/plan.md`) failed before the change at its first case: read through the link, the outside file made `Tallowmere` record a's own and the wall passed it, exit 0. Both pass under 3.9.6 and 3.14.6, and skip where no symbolic link can be made. *Touch-up:* the API note gains T7; section 5's item 19 no longer holds. *Nod:* a linked file that resolves outside the folder or the record was read before and is exit 3 now, in `terms` and in the sets alike, since `scan` already stops on such a file (R09's reason) and this keeps one rule everywhere; the user can copy such a file in. *Finding:* G10.

## Added by the fixes to built packages, 2026-10-21

WP4's review found gaps that sit in packages already built, which no later run of those packages will pick up. They are fixed here at the user's word ("fix them now before run 3", 2026-10-21). Each entry is in R29's shape; in place of a *Finding* line it names the R entry whose follow-up it settles, and the package's own `DECISIONS.md` gains a short entry that points here.

### R39 `record.py init` refuses a slug another client record holds

**Decision.** `record.py init` refuses (exit 1, `CLIENT.md`, field `slug`) when the slug is already used: a folder of that name under `<home>/archive/`, a folder of that name under `<home>/clients/` other than the init's own folder, or the slug's key in `<home>/clients-index.json`, which outlives an archived folder the user has removed. The refusal names the slug the user typed and nothing of the other client: problem "the slug <slug> is already used by another client record under the home, open or archived, and a slug belongs to one client for good", expected "a slug no client record has used: choose another slug, then run init again". It runs before anything is written. Init reads the index without trusting it, under the home mutex when that mutex exists, as `read_index` does, and never creates the mutex: an index that cannot be read as `clients-index/1` with 32-hex keys is exit 3 (`<home>/clients-index.json`, `(whole file)`), and a home path that cannot be looked at is exit 3 naming the root or the index only (R36's `os.stat` reading). The slug key has one implementation: `digest` moved to `mmb_common.py` unchanged, with `slug_key(slug)` = `digest("s:", slug)` beside it; `leak_lint.py` keeps the name `digest` as `mc.digest` and calls `mc.slug_key` for its three slug keys. Moving the four-line function was the smallest change that leaves one implementation, since `record.py` cannot import `leak_lint.py` without loading the whole lint. No other `record.py` command creates or moves a record: `home init` makes the six home folders, `strand open` a strand inside a record, and the move into `archive/<slug>/` (A26) belongs to WP12's `client-closeout archive` and `archive_check.py`, not built yet.

**Reason.** X29 and L178: an index entry is never removed, so an archived client keeps its wall and its slug for good. R35 makes the lint stop a run, after the fact, when two records share a slug; refusing at `init` keeps the second record from being made at all, which is the earlier and cheaper stop. X30 keeps another client's name and folder out of this session, so the refusal names only what the user typed. An index init cannot read cannot prove a slug free, so it stops rather than passes (L205's fail-safe).

**Follow-up.** *Build:* done. *Test:* `test_R39_C44_init_refuses_a_slug_an_archived_or_indexed_client_already_used` (an archived client at `archive/brindle-tiles`, named Brindle Tiles Ltd and indexed: init of `brindle-tiles` for Brindle Tiles Co is refused at the home and at a folder outside it, writing nothing and naming neither the old name, its folder nor the key; with the archived folder removed the index entry still refuses; an archived folder with no entry refuses; a second `larkmoor-joinery` outside the home is refused while `clients/larkmoor-joinery` exists, and the old `folder` refusal at that folder is unchanged; once the archive and the entry are gone the slug inits and checks clean), `test_R39_init_stops_on_an_index_it_cannot_read` (a torn index, a list, a newer schema, `entries` not an object, a key that is not 32-hex, and a folder in the index's place are each exit 3 writing nothing; a sound index without the slug passes), `test_R39_init_stops_when_the_archive_cannot_be_looked_into` (the archive at mode 400 is exit 3 on `<home>/archive/`; skipped on Windows and as root), all in `test_record_part2.py`'s `InitTest`; `test_R39_one_slug_key_for_the_index_and_init` in `test_mmb_common.py`; `test_L195_L196_...` in `test_leak_wall.py` now finds the one digest in `mmb_common.py`. All three failed before the change. The whole suite passes under 3.9.6 (566 tests); no 3.14 interpreter is on this machine, and the code uses nothing that differs between the two. *Touch-up:* `API-record.md`, `API-mmb_common.md` and the API note's U1. *Owed to WP12:* the close-out move refuses when `<home>/archive/<slug>` already exists, and never merges into or replaces it. *Settles:* R35's item owed to WP2. *Nod:* an archived client's slug is taken for good, even after the user deletes its archived folder, because its index entry stays (X29); a new client of the same name takes a slug with one more word. *Nod:* init checks the index's schema and keys only; a deeper fault in an entry passes init and stops the lint's next run with exit 3.

### R40 A renamed client keeps its index entry: `former_names` in `CLIENT.md`, kept by `record.py client rename`

**Decision.** `CLIENT.md`'s front matter gains `former_names`, the client's earlier names, each one line with no `;`, joined by `; `, empty or absent when the client has had no other name. It is optional and comes last, where the front-matter writer appends a new key, so the schema stays `client/2`: a record written before it reads, checks and indexes as before, and `record.py check` blocks only on a present value with an empty name between the `;`. `mmb_common.former_names(value)` is the one reading of the field, used by both scripts. `record.py` had no command that changes the name, so it gains `client rename --name "<new>"`: under the record mutex it sets the new name, appends the old one to `former_names` once, never drops an entry, and logs a record-level `decision` entry with key `rename`; it refuses (exit 1, nothing written) a new name that is the current name, one that is already a former name, and a name that is not one line or holds `;`. In `leak_lint.py`, one test, `holds_own_name`, now decides R35's two questions: `index` replaces the entry under this record's key, and `build_wall` skips it as this record's own, when the entry holds the digest of the current name or of any former name. `build_entry` publishes every former name in X26 step 1's forms beside the name, so every other record stays walled against the old names. An entry under the same slug that holds none of these names is still refused and still walled, exactly as R35 built it.

**Reason.** R35's first nod: the entry's names are the only thing that tells a re-index of the same client from another client on the same slug, so a client renamed in `CLIENT.md` (a typo fixed, a rebrand) looked like a different client, `index` refused, and names the client added later never reached other records' walls. The old name written down by the rename is the evidence R35 lacked, and the test stays on the digest the entry already holds, so `clients-index/1` keeps its shape (X29). Publishing the old names keeps X29's promise that a client stays walled under what the index once held. On the schema: G57 makes a writer refuse only a newer schema, and a bump to `client/3` would make every plugin built before this change refuse to write a record that merely carries the new field, while the field changes no reading of a record without it; the build ledger's optional fields set the same precedent (`build/2`, read by their defaults).

**Follow-up.** *Build:* done. *Test:* in `test_leak_wall.py`, a client named Blue Harbour Logistics at `clients/larch-depot` (neither name shares a word with the slug, so only the entry tells them) and a third record `clients/corbel-hire`: `test_R40_X29_a_client_renamed_through_record_py_keeps_its_entry_and_its_old_name_walled` (renamed to Østby Freight through `record.py client rename`: `index` replaces the entry, which holds the old name, the new name and `Tallowmere`; `Quarrow Pine`, added after the rename, is indexed too; from the third record all four block; the renamed record's own `Blue Harbour Logistics is now Østby Freight; Quarrow Pine and Tallowmere stay.` passes) and `test_R40_a_rename_by_hand_with_the_old_name_in_former_names_works_alike` both failed before the change at their first `index` (exit 3, R35's refusal); `test_R40_R35_a_rename_by_hand_without_the_old_name_is_still_refused` (no field, an empty one, and another client's name in it: `index` exit 3, the entry unchanged, the old name still blocks from the third record) passed before and after. R35's two G07 tests pass unchanged, and the planted records, which have no `former_names`, run every other test as before. In `test_record_part2.py`, `RenameTest`: `test_R40_rename_keeps_every_old_name_once_and_refuses_a_name_already_had` (on the fixture record, which has no field and checks clean: two renames give `Larkmoor Joinery; Larkmoor Joinery Co`, the log entry, a backup and a clean check; the current name, either former name, a name with `;` and a blank name are refused with nothing written; an old name already kept by hand is not added twice; `status` returns the field) and `test_R40_former_names_is_optional_and_checked_when_present` (empty and well-formed values check clean, an empty name between the `;` blocks). `NewerSchemaTest` now runs all 24 writing commands. The whole suite passes under 3.9.6 (571 tests), and the changed files under 3.14.6. *Touch-up:* `record-map.md`'s `client/2` paragraph (logged in `shared-edits.md`); the pinned `shared-words` region gains `rename`, which that paragraph now writes, after `terms` over the changed `shared/` passed against the old region; the API note gains U2; WP2's `API-record.md` and `DECISIONS.md` carry the command and a pointer here. Two edits sit outside this run's list, both forced by the new command: `test_record.py`'s catalogue test (`test_C25_...`) gains `client rename`, and WP2's `API-mmb_common.md` still owes one line for `former_names(value)`. `init` writes no `former_names`, because the record templates were not this run's to touch; absent reads as empty. The rename leaves `CLIENT.md`'s body (its `# <name>` heading, the engagement skill's block) as it is. *Settles:* R35's first nod. *Nod:* anyone who writes another client's name into `former_names` makes that client's entry this record's: the next `index` replaces it, and that client then stays walled only under the names this record publishes, not its own terms, figures and other names. So the field is only ever written by `record.py client rename` or by the user by hand, and the map says it holds only this client's earlier names. *Nod:* the prompt called a name the client already has, or has had, a usage error; `record.py`'s frame gives that a refusal (exit 1, `CLIENT.md`, field `name` or `former_names`), as `strand kind` refuses a kind the strand already has, and keeps exit 3 for a missing `--name`. *Nod:* a client name holding `;` cannot be kept as a former name, so `client rename` refuses to move it; `init` still accepts such a name, which only matters if that client is later renamed.

### R41 The release lint compares the `shared-words` and `shared-phrases` regions with the shipped `shared/` folder

**Decision.** `tools/lint_plugin.py` gains a check, `shared-region`: it reports an error on the region's line in `scripts/leak_lint.py` when `SHARED_WORDS` or `SHARED_PHRASES` differs from what `shared_vocabulary()` or `shared_phrases()` gives for the shipped `shared/` folder now. The message names the region and counts the words or phrases missing from it and the extra ones it holds, never the words themselves, and says what to do: run `leak_lint.py terms` over the changed `shared/`, then regenerate the region with the function named. The derivation keeps one implementation: the lint loads the tree's own `leak_lint.py` by path (`importlib.util.spec_from_file_location`), with the tree's own `mmb_common.py` placed under that name for the load, and calls the script's functions. The script imports cleanly: at import it only defines its constants and functions, sets `sys.dont_write_bytecode` and stops below Python 3.9, which the lint never runs under. The lint sets `sys.dont_write_bytecode` before the load, since the loader writes a cache before the script's own line runs, and puts it and `sys.modules` back as it found them, so no `__pycache__` is left beside the scripts. `shared-words` leaves out the PDF tool name, as R29's unit test does. A missing `leak_lint.py`, a missing `shared/` or a region not written yet is `not present yet`, as for the other checks; a script that will not load, or a derivation that fails, is an error naming the exception's type only. The unit tests in `test_leak_wall.py` stay as they are: they guard development, the lint guards release.

**Reason.** R29 and R32 put the stop words and phrases in reviewed regions so that `shared/` is never trusted at run time, and that holds only while each region matches the folder that ships; R40 showed the regions move whenever `shared/` does. The review asked for the release check to make the comparison, and a unit test alone is not run at release. Loading the script, rather than copying its `vocabulary`, `harvest` and list parsing into the tool, keeps one reading of `shared/`, so the lint and the unit tests cannot drift apart.

**Follow-up.** *Build:* done. *Test:* in `tests/unit/test_lint_plugin.py`, `test_R41_the_real_tree_has_its_shared_regions_equal_to_shared` (the repository's own tree: exit 0, no `shared-region` line, and `sys.dont_write_bytecode` and `sys.modules["mmb_common"]` as before), `test_R41_a_word_shared_gained_that_the_region_lacks_is_an_error` (a copy of the tree whose `shared/safety.md` gains the invented word `Quillanbrook`: exit 1, `shared-words` with one word missing, the word itself not printed, no cache in the copy's `scripts/`), `test_R41_an_extra_phrase_in_the_region_is_an_error` (a copy whose `SHARED_PHRASES` gains `tallowmere depot`: exit 1, `shared-phrases` with one extra), `test_R41_a_script_without_the_regions_is_not_present_yet` (the `lint-clean` fixture's stand-in script). `test_clean_tree_passes` now counts the fixture's two `not present yet` lines, and `test_empty_root_reports_absent_and_passes` checks the absent `shared/`. The whole suite passes under 3.9.6 (575 tests), `test_lint_plugin.py` under 3.14.6 (25 tests), and `tools/lint_plugin.py` gives 0 errors on the repository under both, with no `__pycache__` left. *Touch-up:* `tools/README.md` describes the check. There is no WP16 folder in the workspace yet, so the pointer that the section's note asks for in the package's own `DECISIONS.md` is owed to WP16's first run. *Settles:* R29's and R32's touch-ups.

## Added by the review fixes, part 2, continued (step 8), 2026-10-21

This section continues the part 2 review fixes (R29 to R38) after the fixes to built packages (R39 to R41), in the same shape and with a *Finding* line.

### R42 A one-word name written as two or three words is looked up joined on the checked side

**Decision.** In `Wall.hits`, a checked run of two or three tokens with only white space between them (spaces, tabs or one line break; no comma, mark, sentence end or blank line) is also looked up joined, `Tallow Mere` as `tallowmere`, against the other entries' `names` and `terms` and the other folders' slug forms. The run must pass Z13 item 2's gate, as for its phonetic key: at least one of its words is outside the ordinary words (the common words and the stop list), and its words hold seven letters or more in all. A hit is class `name`, `term` or `slug`, as for any candidate. The joined form is tested against O like any candidate, and the lookup is skipped when O holds the spaced run itself. Nothing else moves: `wall_candidates` and X27 type 3 still fuse no plain spaces, so the publishing side, the index and O are unchanged, and a record that writes `on track` never publishes or holds `ontrack`. The review's route, the run's end-to-end key against `phonetic`, is not built: it catches `Tallow Mere` (`TL` and `MR` join to `TLMR`, Tallowmere's key) but misses `Fern Hollow`, because Z13 item 1 does not publish Fernhollow's key `FRML`, which an ordinary word shares, and because the run's keys joined (`FRMHL`) are not the word's key in any case. The plain lookup catches every split of a correctly written one-word name that the key would catch, and the ones whose key item 1 withheld; the key adds only a split that is also misspelt, which A30 does not ask the wall to chase.

**Reason.** X27 types 3 and 4 and A§:918's corrupted-name trap: speech-to-text and hand typing split compound names this way, and Z13 item 3 covered only the other direction (a fused spelling of a spaced name). A split spelling is a normal form of the name, the same letters in the same order, not a spelling by sound, so it sits inside A30's bound: the wall blocks another client's name in its normal forms and need not chase misspellings. X27's rule that plain spaces are not fused wins on the publishing side and in O, since it is there so that ordinary words never become another client's product. On the checked side Z13 item 2's gate keeps the ordinary pairs out: a run made only of ordinary words is never joined, so `on track`, `follow up` and `hand over` pass even where another record publishes `Ontrack`, `Followup` or `Handover` with a key, which Z13 item 1 gives a single word of seven letters or more that no common or stop word shares. Under the review's route an ordinary pair would have blocked only against such a word, and only when one of its words was outside the ordinary words; under R42 such a pair blocks against the published word whatever its length, so `work shop` (`shop` is not a common word) would block where another record publishes `Workshop`, while `lay out` stays under the seven-letter floor. Measured over the 150,819 tokens of `shared/*.md` and the plugin's scripts against the two planted records' entries, the joined lookup adds no hit (probe `<scratchpad>/wp4-run3/g11/measure.py`).

**Follow-up.** *Build:* done. *Test:* `test_G11_R42_X27_a_one_word_name_written_as_two_or_three_words_blocks` (record b's `Tallowmere` and `Fernhollow`: `Open Tallow Mere today.`, `Fern Hollow runs depots.`, three words, a line break, lower case and a `doc` payload all block; the entry holds Tallowmere's key and not Fernhollow's, the review route's miss) failed before the change at `Open Tallow Mere today.`; `test_G11_R42_X27_ordinary_two_word_phrases_never_fuse_into_another_records_single_word` (six single words of record b, each blocking when written whole; seven ordinary phrases that join to them, a comma split and a sentence split all pass; a run record a writes itself passes while the fused name still blocks) passed before and after, as a clean control should. The leak gates pass under 3.9.6 (237 tests), and the two G11 tests and G03's under 3.14.6. *Touch-up:* the API note gains T8. *Nod:* when this record's own files write the spaced run (`the Tallow Mere estate`), the joined lookup is skipped, so the record can use its own words even where another client's one-word name joins to them; the fused spelling `Tallowmere` still blocks in that record. X27 says a candidate O holds passes, and is silent on whether the run or its joined form is the candidate here. Taking the joined form would block a record's own words with no way to clear them (X10), and adding joined forms to O would let a record's spaced words clear the fused name too, which narrows a block that stands today; skipping on the run narrows nothing that blocked before. *Finding:* G11.

### R43 Plural, plural-possessive and apostrophe shapes of another record's name block on the wall

**Decision.** Two changes. First, `fold` (X28, the input to step 5) reads five more apostrophe shapes as `'` when a letter or digit sits on each side of them: the left single quotation mark (U+2018), the modifier letter apostrophe (U+02BC), the acute accent (U+00B4, before NFKC would turn it into a space), the backtick and the full-width apostrophe (U+FF07). X24 then removes the apostrophe as it does `'` and `’`, so `O‘Rourke`, `OʼRourke`, `O´Rourke`, ``O`Rourke`` and `O＇Rourke` are all the word `orourke`, and `Fernhollow‘s` drops its possessive. Because wall/1 is one normalisation, this reaches every rule that compares words, the single-text rules of part 1 included, and both sides of the hash: the harvest, the index, O and the checked text. A shape with a space or a mark on either side is unchanged, so a backtick around a whole word, as Markdown code, is still a separator (X24) and still fuses on the wall only where R31 says. Second, on the checked side only, `Wall.shape_class` looks up two more shapes of a candidate that has no hit of its own: each word with a plural ending removed (`plural_stems`: a trailing `s`, and `es` after `s`, `x`, `z`, `ch` or `sh`; no stem from a word ending in `ss` or under three characters), spaced or fused as the candidate is; and a one-letter token followed by a capitalised word, with spaces or one apostrophe shape between them (`INITIAL_GAP`), fused to it (`O Rourke`, `O’ Rourke` to `orourke`). A plural possessive such as `Fernhollows'` is the plural, since the trailing apostrophe was never part of the token. For a run of two or three words with only white space between them, a shape that passes Z13 item 2's gate is also looked up joined, as R42 does for the run itself, so `Fern Hollows` meets `Fernhollow` while `follow ups` never meets `Followup`. Nothing is looked up when O holds the candidate itself, as R42 skips its joined lookup. No stem or fused initial is published, keyed or added to O, so the index and `clients-index/1` are unchanged.

**Reason.** X28 step 5 and PLAN §3: the review is told to try possessives, and A30 bounds the wall at another client's names in their normal forms. A plural and a plural possessive are normal forms of a name, and the apostrophe shapes are what keyboards, word processors and speech-to-text put in a name such as O'Rourke; none is a spelling by sound. The fold sits in `fold` rather than on the checked side because X28 keeps one normalisation on both sides of the hash: a record that writes `OʼRourke` must publish the same `orourke` that a check of `O'Rourke` looks up, and O must hold it the same way. The stems stay on the checked side because they are guesses (`cases` gives `case` and `cas`): looked up, a wrong stem blocks only when another record publishes that very word, while published, it would put words in the index that no record wrote. `es` is removed only where English adds it, which keeps most junk stems out. The initial fuse needs the word after the initial to be capitalised, so a one-letter word before an ordinary lower-case word is never joined. On the live script, `O´Rourke`, ``O`Rourke`` and `O Rourke` already blocked through R31 and R42, which came after the frozen copy the review read, and `Kestle Fresh Food` already blocked on its whole name; its plural `Kestle Fresh Foods` blocked only as `Kestle Fresh`, and now blocks as the whole name. Measured over the 151,269 tokens of `shared/*.md` and the plugin's scripts against the two planted records' entries, the new shapes add no hit (probe `<scratchpad>/wp4-run3/g12/measure.py`). No fixture file and no `shared/` file holds one of the five shapes inside a word, so the planted entries and the `shared-words` region are unchanged.

**Follow-up.** *Build:* done. *Test:* `test_G12_R43_X28_plural_and_apostrophe_shapes_of_another_records_name_block` (record b gains Fernhollow Supply, Blue Harbour, O'Rourke Lifts, Kestle Fresh Food and Tallowmere; the review's eight inputs, the full-width shape, `O’ Rourke`, `Tallowmeres`, `Fernhollow‘s`, `Fern Hollows`, both possessives of `Blue Harbour` and a `doc` payload all block with class `name`, and `Kestle Fresh Foods` blocks on its whole name) failed before the change at `We use Blue Harbours for runs.`; `test_G12_R43_ordinary_plurals_and_markdown_code_stay_clean` (eight ordinary plurals, plural possessives, a capital `A` or `I` before a capitalised word, a code word in backticks, two code words side by side, quotation marks and an acute accent after a word all pass; `words_of` keeps backticked words apart and folds the five shapes; R31's ``Tallow`mere` `` still blocks; a plural this record writes itself passes while its singular still blocks) failed before the change only at the `words_of` fold, and its texts passed before and after, as a clean control should. The leak gates pass under 3.9.6 (239 tests), and `ReviewPart2Test` under 3.14.6. *Touch-up:* the API note gains T9; `vocabulary` folds an ASCII line holding a backtick through `fold`, so it still reads what `fold` reads. *Nod:* the fold reaches part 1's word rules as well as the wall. That is the fail-safe reading of X28's one normalisation, and X28 step 5 wins over X24 for a backtick between two letters or digits, which is now an apostrophe inside a word instead of a separator. For the word rules this can join two words that a source wrote with a backtick between them and a checked text wrote apart, so a copied run across such a join could be missed; no shipped or fixture text holds one. A plural of another record's published word blocks wherever the word itself does, `Layouts` against a record that publishes `Layout` included. The initial fuse has no seven-letter floor, so a capital initial written apart from a capitalised word joins whatever its length. *Finding:* G12.

### R44 An index entry older than its record's files stops the wall, as an absent one does

**Decision.** `build_wall` now checks, after X30's coverage check, that each other entry is current. For every folder `home_folders` lists whose key has an entry, it walks the folder with `record_walk`, the walk `record_files` uses for the index's harvest (so the two never drift), keeps the files whose text reaches an entry (`feeds_entry`: every file the sets and `d_text` read, and every strand's `exclusions.md`; not the allowlist or the live map, which feed O only), and takes the newest of their modification and status-change times by `os.stat` alone (`newest_change`), opening no file. The entry is older (`entry_is_older`) when that time is at or after the end of its `updated` second plus two seconds (`ENTRY_SLACK`). Any older entry is exit 3, `error.file` `<home>/clients-index.json`, `error.field` `entries`, problem "<n> other client record(s) under the home ha(s|ve) changed since (its|their) last index, so the wall may not see what was added to (it|them)", expected "run leak_lint.py index from each client record changed since its last index, then run this again", naming no folder, slug or name; the count is given, as the coverage check gives its count. A folder inside such a record that cannot be listed, or a link that leads out of it, is exit 3 on the same file and field, "a client record under the home cannot be looked through, so the wall cannot tell whether its index entry is current", also naming nothing. This record's own entry is never compared, since its folder is not in the list. `index` now takes the clock and this record's newest change before it reads any file, replaces the entry when the lists differ or when the old entry is older than the record's files, and stamps `updated` with the later of the clock and the newest change. `read_index` also refuses an `updated` that fits the pattern but is not a real moment. `clients-index/1` is unchanged. The check runs wherever the wall is built: `payload`, `blueprint`, `scan` with the wall, `wall` and `terms`.

**Reason.** X30 wins: the wall fails closed while it cannot see, and an entry built before the record's last change is the same blindness as an absent one, only quieter. X02 and P5 set when `index` runs, and their moments (init, each saved call, document or email, before archive) leave out an exclusion added during solution design, a research note and a strand file; the finding's `Quarrow Point depot` and `Ysolde Marrick` passed in another record's text with exit 0 until the next intake. A stat compares times and reads no content, so no other client's file is opened in this session, which X30 requires. On the time rules: `updated` keeps whole seconds and is cut down to the second, so a file written later in the same second as the stamp is newer by up to one second without being an edit after the index; two seconds more cover file systems whose times are coarse (FAT and exFAT keep two-second times) and a small disagreement between a shared folder's clock and this one. The status-change time is read beside the modification time because a file copied or moved into the record keeps an older modification time, while its status-change time is the moment it arrived (on Windows the field is the creation time, which a copy also sets). The stamp is the later of the clock and the newest change so that an entry is never older than the files it was just built from: a file whose time runs ahead of the clock would otherwise keep its record's entry older for good, and no `index` run could clear it.

**Follow-up.** *Build:* done. *Test:* `test_G13_R44_X30_P5_an_entry_older_than_its_record_is_exit_3_until_that_record_is_indexed` (after both records are indexed, record b's `exclusions.md` gains `Quarrow Point depot` and a new call names `Ysolde Marrick`, with no `index` after: from record a, `wall` on `Ask about the Quarrow Point depot.` and on `Ysolde Marrick will call.`, a payload and a draft `scan` are exit 3 with the error above and nothing of record b in the envelope, and `terms` is exit 3; after `index` from b, the term and the name block with exit 1 and `terms` passes) failed before the change at its first case, exit 0. `test_G13_R44_an_untouched_record_a_skipped_file_and_this_records_own_entry_never_trip_it` (clean: an untouched indexed record blocks and passes as before; new files under `.work/`, `drafts/` and `deliverables/`, the allowlist, the live map and two `.json` files change nothing and a rerun of `index` writes nothing; record a's own edit never stops record a, while from record b it is exit 3 until record a is indexed; an edit to `log.md` that changes no list is exit 3, and `index` then writes a new stamp with the same lists, and a rerun writes nothing) failed before the change only at record b's check of record a's edit; its clean cases passed before and after. `test_G13_R44_a_change_within_the_stamps_second_and_the_slack_is_not_older` (an entry stamped 09:30:00 is not older for a change up to 09:30:02.999, and is older from 09:30:03) errored before, the function being new. The tests move a file's time a minute ahead with `os.utime`, since the tests' clock is patched to an earlier day. `test_L168_...` and `test_L177_...` now expect the stamp that rule gives, the later of the patched clock and the copied files' real times, in place of the patched clock alone; their other assertions are unchanged. The leak gates pass under 3.9.6 (79 tests in `test_leak_wall.py`, 242 in the four files), and `ReviewPart2Test` and `IndexTest` under 3.14.6 (40 tests). *Touch-up:* the API note gains T10, and P5's moments gain "after every edit of `exclusions.md`, `research/` or strand Markdown". *Owed to WP8 and WP12:* those callers run `index` after every edit of `exclusions.md`, `research/` or strand Markdown they make, as P5 now says. *For the main session:* `record.py`, already built, writes files the entry reads through its own commands: `log.md` on nearly every writing command (lease take and release, strand open, pause, resume, kind, close and summary, version open, mark and release, freeze, add-transcript, add-document, log, client rename), `CLIENT.md` (the strand index, the lease mirror on take and release, rename), `STRAND.md`, `readiness.md`, `scope.md` and `version.md`, and a new `solution/exclusions.md` from the template at `init` and `strand open`. It writes nothing under `research/`. Whether `record.py` should run `index` after its own writes is the main session's call. *Nod:* the cost in use: any edit in one client's record to a file the harvest reads stops every other client's lint with exit 3 until that client is re-indexed. Since `record.py` writes `log.md` on nearly every command, a working session in one record usually leaves its entry older, so switching to another client starts with an exit 3 that names no record; running `index` in each record before leaving it avoids it. *Nod:* the two-second slack means an edit made within about three seconds after an `index` run began is not seen; a shorter slack would trip on coarse file times. *Nod:* the status-change time also moves when a file's mode or links change, so `chmod` on a harvested file makes the entry older; and `index` now writes a new stamp, with a backup, after an edit that changes none of the four lists, which narrows X46's "nothing at all when the four lists are unchanged" to "when the lists are unchanged and the entry is not older than the record's files". A rerun with nothing changed still writes nothing. *Nod:* `updated` can now lie ahead of the clock when a file's time does; it then reads as "not older than the files it was built from", which is all the wall asks of it. *Nod:* a folder inside another client record that cannot be listed, or a link that leads out of it, now stops every other record's wall too, where before the wall never looked inside. A removed file or folder does not make the entry older, since a removal adds nothing to it; a change to the plugin's `shared/` or shipped list is not measured, as neither is a record's file. *Finding:* G13.

### R45 An index entry without its folder's name stops the wall, and its own record's index repairs it

**Decision.** `build_wall` now checks, after X30's coverage check and before R44's age check, that no entry is damaged (`entry_is_damaged`): an entry whose `names` list is empty, or, where a folder directly under `<home>/clients/` or `<home>/archive/` has the entry's key, an entry that does not hold that folder name's spaced digest (`name_key(<folder name>)`, computed from the name alone; no file is opened). Any damaged entry is exit 3, `error.file` `<home>/clients-index.json`, `error.field` `entries`, problem "<n> entr(y|ies) of the index (is|are) damaged: leak_lint.py index always writes a client's folder name among its names, and (it holds|they hold) no names, or not that one, so the index was emptied or only partly restored", expected "run leak_lint.py index from each client record under the home; if the index was restored from a backup, restore the whole file from that backup, not part of it; then run this again". It gives the count and names no folder, slug or key. The check runs wherever the wall is built: `payload`, `blueprint`, `scan` with the wall, `wall` and `terms`. This record's own entry is tested for an empty `names` list only, since its folder is not among the others. `index` changes in one place: an entry under this record's key that holds neither this record's name nor a former name (R35, R40) and also lacks the slug's spaced digest is damaged, not another client's. It is replaced when this record's new lists hold every digest it still holds, which an emptied entry always satisfies; otherwise `index` is exit 3 on the same file and field, problem "the entry under this record's slug is damaged (it lacks the slug's name, which index always writes) and holds digests this record would not write, so replacing it could drop another client's wall", expected "restore the whole clients-index.json from its backup under <home>/local/backup/, then run index again", and writes nothing. `read_index` and `clients-index/1` are unchanged. The script was checked against the review's premise after R35 and R40: `client_identity` refuses a slug with no word and a slug that is not the folder's name, and `build_entry` adds the slug's words to the candidates unfiltered beside the name and the former names, so every entry `index` writes holds the folder name's spaced digest, a record with no `CLIENT.md` name included. No path writes an empty `names` list, so `index` needed no new refusal of its own lists, and the review's second check is built.

**Reason.** Z18 item 3, X26 step 1 and X30 win. Z18 item 3 checks the index's shape, and an entry of four empty lists, or one whose lists were partly restored, fits that shape while walling less than its record holds; from record a the review's emptied entry passed `Open Tallowmere today.` with exit 0, and only the slug still blocked. Since X26 step 1 always publishes the slug, which X30 makes the folder's name, an entry without that name cannot be one `index` wrote, so the reader can tell a damaged entry without opening any file of the other record, and X30 has it fail closed as for an absent entry. The check sits in the wall's readers rather than in `read_index`, because Z18 item 3 has `index` never overwrite a malformed index; there, the record whose entry was emptied could not repair it, and the error could only point at a backup. At `index`, R35's name test cannot judge an entry that holds no names, and R35's refusal would have told the user to give the record another slug. X26 step 1 wins over R35's test for such an entry, since another client's entry on this slug, as `index` wrote it, would hold the slug's digest. Replacing it only when nothing it holds is dropped keeps the fail-safe side: the wall that every other record builds after the replacement holds every digest it held before.

**Follow-up.** *Build:* done. *Test:* `test_G14_R45_Z18_X26_an_emptied_or_half_restored_entry_is_exit_3_until_its_record_is_indexed` (record b holds `Tallowmere`; its entry with all four lists `[]`: `wall` on `Open Tallowmere today.`, a payload, a draft `scan` and `terms` are exit 3 with the error above and nothing of record b in the envelope; `index` from record b replaces the entry with the lists a fresh index gives, and the name blocks with exit 1; a half-restored entry holding only `Tallowmere`'s digest, with and without the other three lists, and an entry with empty `names` alone, are each exit 3 and repaired the same way; an entry with empty `names` and a term digest record b would not write is refused by `index`, the file unchanged) failed before the change at its first case, exit 0. `test_G14_R45_a_normal_entry_one_with_names_only_and_an_archived_one_with_no_folder_pass` (clean: a normal entry, an entry with names and empty `terms` and `figures`, an archived entry with its folder, and an archived entry whose folder is gone each block `Open Tallowmere today.` and pass `Open the depot today.`) and `test_G14_R45_X26_index_always_writes_the_folders_name_even_with_no_client_name` (record b with `name: ""` indexes an entry that holds `name_key("marlbeck-freight")`) passed before and after, as clean controls should. The leak gates pass under 3.9.6 (82 tests in `test_leak_wall.py`, 245 in the four files), and `ReviewPart2Test` and `IndexTest` under 3.14.6 (43 tests). *Touch-up:* the API note gains T11. *Nod:* the error gives a count and no record, as X30 asks, so the user re-indexes every record under the home or restores the whole index from its backup; an archived record whose folder is gone cannot be re-indexed, so for its entry only the backup restores it. *Nod:* `index` takes a damaged entry under its key for this record's when every digest it still holds is among this record's new lists. If it was in fact another client's on the same slug (possible only where R39's `init` check was passed by hand and the twin folder is gone), nothing is lost at that replacement, but the digests then count as this record's, and a later re-index after this record drops one of those words drops it from the wall too. *Nod:* a half-restored own entry that still holds this record's name is skipped as its own and replaced by its next `index` (R35), so it is not tested against the folder name; the other records' walls test it. *Finding:* G14.

### R46 A record that is not under the home in use stops the wall and `index`

**Decision.** `twin_folder` (R35) now checks the record's place first, in every run that builds the wall from a record (`payload`, `blueprint`, `scan` in full and client-safe-block modes, `wall`) and in `index`. The record's resolved parent must be `<home>/clients` or `<home>/archive`, with the home side resolved too (`os.path.realpath`, compared through `os.path.normcase`), so a home reached through a link matches; otherwise the run is exit 3 with `error.file` `CLIENT.md`, `error.field` `record`, problem "this record is not under <home>/clients/ or <home>/archive/ of the home in use, so the wall cannot see the client records beside it", expected "a record at <home>/clients/<slug>/ or <home>/archive/<slug>/: point MMB_HOME at the home that holds this record, or move the record into that home's clients/, then run this again". The error names no path and no folder. The twin test that follows now looks only at the other root, since the record's own root holds the record itself; R35's "either root for a record outside the home" no longer arises, because such a record stops at the first check. One check covers both findings, as the review asked. `terms`, which has no record, and a `scan` in summary mode, which runs no wall (X37), are unchanged, and a folder with no `CLIENT.md` still stops at `locate` as before.

**Reason.** X30 and BP:158.32 win: the wall fails closed while it cannot see, and A§5.3 puts every record at `<home>/clients/<slug>/` or `<home>/archive/<slug>/`. The wall learns a record's neighbours only from the home that `MMB_HOME` names, so a record checked against another home (a hook with another environment, a moved home, a record copied or moved out) saw an empty or foreign index and passed another client's name with exit 0; the finding's `Open Tallowmere today.` passed from record a against a home with no records. `index` stops too, because its entry would land in an index that holds no folder of this record, where R35 and R45 would later read it as another client's entry on that slug. Both sides are resolved because `locate` resolves the record and `MMB_HOME` is read as written; on this Mac `/tmp` and the test homes under `/var` are links to `/private`, and a plain string compare would stop every record there.

**Follow-up.** *Build:* done. *Test:* `test_G15_R46_X30_a_record_checked_against_a_home_that_does_not_hold_it_is_exit_3` (records a and b indexed, b holding `Tallowmere`; with `MMB_HOME` naming a second home that holds the settings and no record, `wall` on `Open Tallowmere today.`, a payload, a draft `scan` and `index` from record a are exit 3 with the error above and nothing of record b in the envelope, and no index is written in the second home; record a moved out of its home is exit 3 for `wall` and `index`, the index unchanged) failed before the change at its first case, exit 0. Clean control `test_G15_R46_records_under_clients_or_archive_and_a_home_reached_through_a_link_pass` (a record under `clients/` blocks `Open Tallowmere today.` and passes `Open the depot today.`; so does one named through a linked home, by the link and by its real path, with a payload blocking and `index` writing nothing; so does a record moved under `archive/`; a `scan` of a plain file in a folder with no `CLIENT.md` stops at `CLIENT.md`, `record`, "no CLIENT.md in the folder plain"; a summary-mode `scan` from a record checked against the second home is exit 0 with no wall finding) passed before and after. The leak gates pass under 3.9.6 (84 tests in `test_leak_wall.py`, 247 in the four files); no 3.14 interpreter was on this machine for this run, and the check uses only `os.path.realpath`, `os.path.normcase` and `Path.resolve`, which behave alike on both for an existing record. *Touch-up:* the API note's T4 gains the check, and T12 is added. *Nod:* a record folder that is itself a link placed in `<home>/clients/` and pointing outside the home is now exit 3, because its resolved parent is not the home's root; this is the review's rule and the fail-safe reading, since such a folder could be linked into two homes and each would wall it against only its own neighbours. The user moves the folder itself into the home. *Nod:* a summary-mode `scan` from a record outside the home still runs, since it runs no wall and the finding asks only for the commands that do. *Finding:* G15.

### R47 A single word is published only when its record never writes it in lower case, and plurals of stop words fall with them

**Decision.** Two changes to what an entry publishes, and one to what `index` prints. First, `build_entry` (X26 step 5) collects, over the same D text it harvests, the words the record writes in lower case as prose (`lower_words`): a token with no capital letter, joined to neither neighbour by a fuse gap of X27 type 3 (`-`, `.`, `_`, `@`, `/`, `&`, `+`, a line-end hyphen, Markdown marks), by no gap at all or across a backtick, in both readings of R30's letters. A harvested candidate of one word that is among them is not published. A run of two or more words keeps the word, and X26 step 1's forms (the `CLIENT.md` name, the former names and the slug) are added after the filter, so they are always published. Lower case inside an e-mail address, a link, a joined name such as `tallowmere-sync` or a code word does not count, so the parts of an address the harvest takes under step 4 are still published unless the record also writes them in its prose. Second, `kept` drops a single word that is a plural or inflected form of a stop word (`inflection_stems`): R43's plural stems, `ies` as `y`, and `ed` or `ing` removed, with a final `e` restored or a doubled letter undone, any stem of three characters or more. The stop words are X26 step 6's list as `wall_stop` returns it (the days and months, the product words, the titles and acronyms, the shipped plugin, assistant, method and markers rows, and the `shared-words` region), not the common-word list. Since `kept` also cuts the other folders' slugs (X21), a slug word such as `thursdays` falls the same way there. Third, `index` prints `single_words`: the count and the sorted single words this record's entry publishes, its own words, so the user can see them. `wall/1`, O, the checked side and `clients-index/1` are unchanged.

**Reason.** X26's own reason wins: a common single word is kept out of the digest so that an ordinary word never blocks every other client's prose, and the 1,098 common words cover too little of the vocabulary a record writes. The review measured the cost Z16 item 5 left for the user's nod: `supply`, `freight`, `pallets`, `logistics`, `harbour` and `thursdays` published by one record blocked another record's ordinary sentences, the allowlist only warns on the wall (X10), and the only way out was to write the words into the record, which G17 calls laundering. A real name is capitalised every time a record writes it, so a word the record also writes in lower case as prose is an ordinary word, and the record is the source that wins for its own words. The joined and code forms are left out because a name is written there in lower case for the medium, not because it is ordinary; leaving them out keeps more words published, the fail-safe side. `thursday` is a stop word and `thursdays` was not, though no record writes a name that way. Reading "stop words" as X26 step 6's list and not the common words keeps a surname such as `Banks` published, the fail-safe reading, since the lower-case rule already drops an ordinary plural the record writes in lower case. Whatever PLAN nod 6 accepted for rare words, these were ordinary ones; PLAN nod 6 as now written is the tool-category assertion's "fail-safe over precise", and the "may block a rare word" that Z13 quotes is not in it.

**Follow-up.** *Build:* done. *Test:* `test_G16_R47_X26_ordinary_words_published_as_one_word_names_stop_blocking` (record b writes the review's six words capitalised, in `Fernhollow Supply`, `Østby Freight`, `Blue Harbour`, `Pell-Ardent Logistics` and `Pallets ship on Thursdays.`, and five of them also in lower case; none of the six is in its entry, while `tallowmere`, `fernhollow`, both readings of `Østby` and the four runs are; record a's draft from the review is exit 0 with no wall finding) failed before the change at `supply`; before it, the draft was exit 1 with four name blocks, `Pallets`, `Thursdays`, `Logistics` and `Harbour`, while `Supply` and `freight` passed because record a's own brief writes both (O), which also keeps the slug word `freight` of `marlbeck-freight` from blocking there. `test_G16_R47_real_one_word_names_keep_blocking_and_index_shows_the_single_words` (lower case only in `ops@tallowmere.example`, a link, `tallowmere-sync`, a backticked `tallowmere` and `fernhollow_depot` keeps both names published; `Tallowmere`, `Fernhollow`, `Østby`, `Ostby` and `Banks` block with class `name`; `Fridays`, `Thursdays` and `Quillon`, which the record also writes as `quillon`, are not published; `index` prints the sorted single words, each in `names`) failed before the change at `fridays`; its blocking texts passed before and after, as a clean control should. `test_leak_grading.py` grades its 250 cases with every planted case blocking and every clean twin passing. The leak gates pass under 3.9.6 (86 tests in `test_leak_wall.py`, 249 in the four files), and `ReviewPart2Test` under 3.14.6 (36 tests). *Measured:* with the two planted records of `tests/fixtures/leak/` indexed, record b (`marlbeck-freight`) published 20 single words before and 19 after, dropping `holdings` (from `holding`, a `shared/` word; `Quessel Holdings` is still published as a run), and record a (`wrenfold-joinery`) 22 before and 21 after, dropping `extracts` (from `extract`, a `shared/` word). The lower-case rule drops none of the planted single words, since each planted record writes its single names capitalised only; it drops the ordinary words of the review's input. Probes `<scratchpad>/wp4-run3/g16/measure.py` and `draft.py`, each run against a copy of the script before and after. *Touch-up:* the API note gains T13. *Nod:* the rule cannot catch a real one-word name that the record also writes in lower case somewhere in its prose, such as a product named after an ordinary word (`the quillon login`), or a name a speech-to-text transcript writes in lower case: such a name is no longer published as a single word, though every run it sits in still is, and the client's name and slug always are. A word another client's record writes only inside an address, a link, a joined name or a code word stays published. *Nod:* the lower-case test is exact, so a record that writes `pallet` in lower case and only `Pallets` capitalised still publishes `pallets`; that keeps more words published. *Nod:* the files the session writes (`STRAND.md`, `research/`, `log.md` and the rest of D) count as the record's own prose, as they do for D today, so a session's own lower-case line can take a single word out of its record's entry; G17, which this finding leads into, is not changed here. *Nod:* the other folders' slugs (X21) are cut from the folder listing alone and are unchanged apart from the plural stems: an ordinary word in another client's folder name, such as `freight` in `marlbeck-freight`, still blocks wherever this record does not write it (X27), and in the review's own home `supply` of `fernhollow-supply` would have blocked the review's draft that way. *Finding:* G16.

## Added by the fixes to built packages, part 2, 2026-10-21

This section holds the fixes made at the user's word to packages already built, after the part 2 review fixes R42 to R47, in R39's shape.

### R48 `record.py` runs `index` for its record after a command that wrote a file the harvest reads

**Decision.** At the end of a `record.py` command that succeeded (exit 0 or 2) and changed a file the record's index entry is built from, `record.py` runs `leak_lint.py index` for that record before it prints. Which files count is the lint's, not a list of commands: before the command and again after it, `record.py` walks the record with `record_walk`, keeps the files `feeds_entry` accepts (R44) and marks each with its modification time, status-change time and size by `os.stat`, opening none; any difference between the two marks is a write, a rewrite that leaves the record's newest time where it was included. So `lease refresh` (only `.work/lock.json`), `lease status`, `strand list`, `check` and a write to the live map run no index, and `log`, `init`, `add-transcript`, `add-document`, `freeze`, `guard`, `card`, the `strand`, `version` and other `lease` commands and `client rename` run it whenever they change such a file. Whether the entry is then replaced stays `index`'s own decision (the four lists, and `entry_is_older` with R44's slack), so the two cannot drift; `init` writes the record's first entry this way. `status`, which prints status/1 bare and never writes, and `home init`, which has no record, run none. The index runs in process: `record.py` loads `leak_lint.py` from its own folder by path, once per process (`importlib.util.spec_from_file_location`, as R41's release lint does), and calls the new `leak_lint.run_command(argv)`, which returns `(exit code, envelope)` and prints nothing; `main()` is now `run_command` then `emit`, its output unchanged. It runs in `record.py`'s `main()`, after the command has returned and so after the command's `record_mutex(<record>)` is released, and `index` takes only the home's mutex: `record.py` never holds both, so no lock order can invert. If the index stops (exit 1 or 3: a twin folder, a damaged or unreadable index, a record outside the home), or `leak_lint.py` cannot be loaded, the command's own write stays as it is and the envelope gains a `warnings` entry, `{file, field, problem, expected}` with the index's own file and field (`<plugin>/scripts/leak_lint.py`, `(whole file)` when the lint could not be loaded): problem "this command's writes are done and kept, but this record's entry in the client index was not brought up to date, because leak_lint.py index stopped with exit <n>: <its problem>. Until it is, other client records' lint may stop with exit 3, and their wall may not see what this record now holds", expected the index's own expected value followed by "(the run meant is leak_lint.py index from this record; record.py also runs it after its next write)". The exit code is then 2, WP2's "done, warnings only" (C20), and `ok` stays true. An index that runs adds nothing to the envelope. The index's error names no other client's folder (X30), so neither does the warning.

**Reason.** R44 makes the wall fail closed on an entry older than its record, and `record.py` writes `log.md` on nearly every command, so a working session in one client left its entry older and the next client's lint started with an exit 3 that named no record (R44's nod). The user asked, on 2026-10-21, that `record.py` run `index` for its record after any command that wrote a file the harvest reads. The prompt's test was "the entry absent or older"; `entry_is_older` alone leaves R44's slack window, in which a second command within about three seconds of the first (a skill's `add-transcript` and then `log`) would leave its new names out of the entry while every wall reads the entry as current. Running `index` after every harvested write and leaving the replace to `index` closes that window for `record.py`'s own writes and keeps one rule. Marks per file rather than R44's newest time, because a file whose time lies ahead of the clock keeps the newest time unchanged across a rewrite of another file. In process rather than a child: `record.py`'s source rules bar `subprocess` (C01, C82), `sys.executable` can be empty, or a launcher stub on Windows, in embedded and store-installed interpreters, and a child would cost a second interpreter start and a second stdout to keep out of the one envelope; in process the index runs with the same `mmb_common`, `MMB_HOME` and clock as the command, on Python 3.9 and 3.14 alike. A stopped index is a warning, not a refusal, because the command's write is done and correct; the stop it causes is in other records' lint, and the warning tells the session why and what to run.

**Follow-up.** *Build:* done. *Test:* in `test_record_part2.py`, `IndexAfterWriteTest`: `test_R48_R44_a_write_the_harvest_reads_runs_index_and_one_that_writes_none_runs_none` (on the fixture record, which has no entry: `log` runs one index, whose entry holds `Quarrow Pine` and which a rerun finds current; `lease refresh`, `lease status`, `strand list`, `check`, `status` and a write to the live map run none and leave the index byte-equal; `strand pause` runs one), `test_R48_init_writes_the_records_first_entry`, `test_R48_an_index_that_stops_leaves_the_write_and_shows_a_warning` (a torn index and a twin folder under `archive/`: exit 2, `ok` true, the log entry written, one warning on `<home>/clients-index.json` or `<home>/archive/`, the index unchanged; once fixed, the next `log` brings the entry up to date), `test_R48_a_lint_that_cannot_be_loaded_leaves_the_write_and_shows_a_warning` and `test_R48_C18_G49_from_a_plugin_copy_the_output_is_one_envelope_and_no_cache_is_left` (a subprocess `log` from a plugin copy without `PYTHONDONTWRITEBYTECODE`: one JSON object, the entry written, the copy unchanged). In `test_leak_wall.py`, `test_R48_R44_X30_a_record_py_write_in_another_record_keeps_its_entry_current_and_its_new_names_walled` (record b's `log.md` edited by hand makes record a's `wall` exit 3; `record.py log` in record b with `Ysolde Marrick` then makes record a's wall run again, `Ysolde Marrick will call.` and `Ask Ysolde today.` block from record a and pass from record b; a `record.py log` in record a with `Ostrella Hinges` blocks from record b). All six failed before the change (the five at `lint_module`, the wall test at the new name's digest). Existing tests changed so the index can run, not to weaken it: `test_record.py`'s `make_plugin` copies `leak_lint.py` and `shared/leak-terms.txt` through one helper, `add_lint`, which `test_ledger.py`'s `make_plugin` calls too (its source rule now admits the import of `test_record`, as part 2's does); `test_C43_...` inits under `<home>/clients/`, since R46 has `index` refuse a record outside the home; R40's `renamed_works` expects the rerun of `index` to write nothing after `record.py client rename`, which has already run it. *Measure:* on the fixture record, `record.py log` as a subprocess takes 0.22 s against 0.11 s before (median of 15 runs, Python 3.9.6) and 0.13 s against 0.05 s (3.14.6): about 0.04 s to load `leak_lint.py`, two walks of about 2 ms and the index itself. A command that changes no harvested file pays the load and the walks, 0.06 s for `lease status`. *Gates:* the whole suite passes under 3.9.6 (595 tests); `test_record.py` (51), `test_record_part2.py` (49), `test_leak_wall.py` (87), `test_ledger.py` (107), `test_leak_lint.py` (144) and `test_lint_plugin.py` (25) under 3.14.6; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* WP2's `API-record.md` and `DECISIONS.md`; the API note gains V1 and P5's moments change. *Owed to WP8 and WP12:* unchanged: callers still run `index` after files they write themselves, outside `record.py` (P5). *Nod:* the prompt asked for an index when the entry is absent or older; this runs it after every harvested write, for the slack window above, and `index` writes nothing when nothing changed (X46). *Nod:* when `leak_lint.py` cannot be loaded, `record.py` cannot tell whether a command wrote, so every command with an envelope that succeeds carries the warning, `check` included, whose exit becomes 2. *Nod:* a record that cannot be walked (a folder that cannot be listed, a link out of it) counts as written, so `index` runs after every command, reads included, and its stop shows as the warning each time until the record is fixed. *Nod:* the index runs after the record's mutex is released, so another session's write in between is caught by `index`'s own clock taken before it reads (R44), and the next write indexes again. *Nod:* a rewrite that keeps a file's size inside one coarse time step (FAT keeps two-second times) shows no change; every log entry changes `log.md`'s size. *Nod:* a command that stops with exit 3 after a committed lease change runs no index; the `record.py log` that finishes its entries by hand then runs it.

## Added by the review fixes, part 2, run 4 (step 8), 2026-10-21

This section continues the part 2 review fixes after R48, in R29's shape and with a *Finding* line.

### R49 `blueprint` stops unless sections 1 to 15 are found, each once and in order, with no other heading among them

**Decision.** `blueprint` is exit 3, "cannot find sections 1 to 15", unless the blueprint's level-2 headings numbered 1 to 15 are each found once and in order, before section 16 when there is one. X09's error for a blueprint with no numbered heading becomes this wider one. A number is read after `## ` followed by `.`, `)`, `:`, white space or the end of the line (`section_number`), so `## 4) Boards` and `## 4: Boards` are section 4 beside the pinned `## 4`, `## 4.` and `## 4 Title`; `## **4. Boards**`, `## Section 4: Boards` and `## Four. Boards` are not, and leave section 4 unfound. The same reading holds wherever the blueprint's sections are read (`blueprint_client_lines`, so X11's segments and D as well as the check). Following D19, a level-2 heading that is not one of the sixteen numbered sections, or a level-1 heading after section 1, sitting before section 16 is also exit 3, on `line <n>` of the blueprint, because X09 ends a section's text at the next level-1 or level-2 heading and the text under it would go unchecked. Text after section 16 stays internal under any heading, as before. A blueprint with no section 16 runs its sections to the end of the file, so every heading after section 15 counts as before section 16. The error's expected value says what to do: write the sixteen section headings as `blueprint-guide.md` numbers them (`## 4. Structure mapping`), with every added item inside one of them as a level-3 subsection, then run this again; the section stop also names the first section missing, repeated or out of order (`section_problem`). The check sits where X09's did, after the wall is built, so an index stop still comes first.

**Reason.** X09 and Z19 make the text under the sections numbered 1 to 15 the blueprint's client-facing text, and A§6 (the solution-blueprint skill) and D19 fix the blueprint at sixteen numbered sections, with every item added since sitting inside one of them as a named subsection, so that the count and the lint's section range never move and "16 Internal" comes last. A real blueprint therefore always holds sections 1 to 15 and then 16, and a heading the lint does not read as one of them can only be a drift in the template or the session's style, which silently turned client-facing text internal: the review's `Jobs board, with a Tallowmere sync column. Fuel budget 412,870.` under `## 4) Boards` and four other shapes passed with exit 0, because one good heading kept the file from X09's exit 3. Stopping is the fail-safe side; guessing at bold, word or "Section" shapes would only move the edge. Reading `)` and `:` as numbered moves the lines under such a heading out of D and the blueprint's internal sets and into the client-facing text, which narrows the harvest for that heading: X09 and X11 win, since the section is client-facing whatever its punctuation, and `blueprint` now checks it.

**Follow-up.** *Build:* done. *Test:* `test_G18_R49_X09_section_4_written_with_a_bracket_or_a_colon_is_checked` (record b holds `Tallowmere`; in an otherwise full blueprint the finding's text under `## 4. Boards`, `## 4.Boards`, `## 4 Boards`, `## 4) Boards` and `## 4: Boards` blocks with a wall `name` finding; the same blueprint with a clean section 4 is exit 0 with no finding) failed before the change at `## 4) Boards`. `test_G18_R49_X09_a_blueprint_without_sections_1_to_15_each_once_and_in_order_is_exit_3` (`## **4. Boards**`, `## Section 4: Boards` and `## Four. Boards`, a section left out, a section repeated after section 16, two sections swapped and section 16 before section 15 are each exit 3, "cannot find sections 1 to 15", the expected value naming `## 4. Structure mapping`; the full blueprint is exit 0) failed before the change at `## **4. Boards**`. `test_G18_R49_D19_a_heading_that_is_no_section_before_section_16_is_exit_3` (`## Boards`, `# Boards` and `## 17. Boards` between sections 4 and 5, and `## Contents` before section 1, are exit 3 on the heading's line, the expected value naming the level-3 subsection; `### Boards` inside section 4 is checked and blocks; text under `## Build notes` and `# Appendix` after section 16 gives no finding) failed before the change at `## Boards`. `test_G18_R49_Z19_in_a_full_blueprint_the_glossary_is_exempt_from_the_copied_run_rule_only` (a copied run inside the glossary passes; a marker and another client's name inside it block; the run outside it blocks) passed before and after, as a control. The decision of 2026-10-21 (the main session's, on the design above): the short test blueprints are smaller than any real one can be, so they were given the full set of section headings, their planted text left in its section. In `test_leak_wall.py` a helper, `sections(first, last)`, writes the empty headings, and ten tests use it: L162, L163, both X09 tests that write a blueprint with sections, X11, L04, L47, L189 and the two G09 tests; `X09_only_the_client_facing_text_is_checked` now reads the prompt's line from its text, and its `## Build notes` sits after section 16. The trap fixture's `cases/blueprint/R10c-p.md` and `R10c-t.md` gain the headings of sections 4 to 16 after section 3, every line before them unchanged, so the manifest, the README and `test_leak_fixture.py` need no change (`fixture-notes.md`, section 8). *Gates:* `test_leak_wall.py` 91 tests and the four leak files 254, all passing under 3.9.6; `ReviewPart2Test` 41 under 3.14.6. *Touch-up:* the API note gains T14. *Owed to WP7 and WP9:* a blueprint missing any of sections 1 to 15 now stops `blueprint`, so WP7's blueprint template and `blueprint-guide.md`, and the solution-blueprint skill, write the sixteen numbered level-2 headings in the pinned shape, each once and in order, with every added item as a level-3 subsection and internal notes under section 16. *Nod:* a blueprint missing any of sections 1 to 15, or holding another level-1 or level-2 heading before section 16, now stops `blueprint` with exit 3 instead of passing with part of its text unchecked; the template and the skill above must honour this, and neither is built yet. *Nod:* the prompt named level-2 headings; a level-1 heading after section 1 hides text the same way, so it stops too, while the title above section 1 does not. *Nod:* a heading line inside a fenced block counts as a heading, as it did, so an agent or Vibe prompt whose text holds a `## ` heading before section 16 is exit 3; before, such a line ended its section and hid the text after it. The skill writes headings inside prompt text at level 3 or below. *Nod:* a word of a section heading reaches D, as the blueprint's internal text does (X11), so a heading word the stop list lacks is published as a single name: with `Requirement trace` as section 3, record a's entry published `requirement`, and the checked side's plural stem (R43) then blocked `requirements` in a `shared/` file under `terms`, in L04. The test helper writes `Requirements trace`; the real headings' words want a place in the stop list when WP7 ships them. *Finding:* G18.

### R50 A single word whose plural is a stop word is a stop word too

**Decision.** R47 widened in the fail-safe-for-release direction. `kept` (X26 step 5) drops a single word when one of its plural forms is a stop word, as R47 drops a plural or inflected form of one. The plural forms are `plural_forms`: the word with `s` added and with `es` added, each kept only where R43's `plural_stems` reads it back as the word, so the harvest runs R43's checked-side rule the other way (`requirement` with `requirements`, `class` with `classes`). A possessive needs no rule of its own, since X24 removes the apostrophe: `requirement's` is the word and `requirements'` its plural. The stop words are R47's, X26 step 6's list as `wall_stop` returns it with the `shared-words` region, not the common words. The other folders' slugs (X21) are cut by the same rule. Runs, X26 step 1's forms, the checked side, O and `clients-index/1` are unchanged. With the sixteen section titles of the blueprint template written in the pinned shape, sentence case as `blueprint-guide.md` numbers them (`## 3. Requirement trace`), no word or run of a title is published from a record after this change, so the fallback of harvesting nothing from the numbered level-2 headings of `solution/blueprint.md` is not taken: the headings stay in D, as X11 and R49 have them.

**Reason.** L04 and L197 win over R47's narrower reading: `terms` over the shipped `shared/` must pass with every record indexed. R43 reads a checked plural as its singular, so a single word a record publishes blocks every plural of it, and `shared/` writes `requirements`. R47 dropped the plural of a stop word but not a singular whose plural is one, so section 3's own title made every record with a blueprint publish `requirement`, trip the release check and block `requirements` in every other record's prose. Now the two sides agree: no word is published that R43 would read off a plural stop word. The change only takes single words out of entries, which narrows the wall; the source that wins is named above. A name is lost only when it is also an ordinary word whose plural the plugin's own vocabulary writes, and its runs, the client's name and the slug are still published.

**Follow-up.** *Build:* done. *Test:* `test_G18_R50_R47_the_sixteen_section_titles_publish_no_word_and_terms_over_shared_passes` (record a's blueprint carries the sixteen titles in the template's own words; no word and no run of two to four words of a title, spaced or fused, is in its entry or its `single_words`; `plural_forms` gives `requirements`, `boxes` and `classes`; `terms` over the real `shared/` is exit 0 with no finding, and `blueprint` exit 0) and `test_G18_R50_a_real_one_word_name_under_a_section_heading_still_publishes_and_blocks` (record b's blueprint carries the sixteen titles, with `Quorrin` in section 16's body and `### Brindle handover` under it, and its brief `Tallowmere`; all three are published and block from record a with class `name`, `requirement` is not, and `Check the requirements today.` and `List the requirement traces.` pass) both failed before the change at `requirement`. R49's helper `sections` is back to the template's own words: `SECTION_TITLES` now holds the sixteen titles as `rebuild-workspace/design/ARCHITECTURE.md` lists them (`Requirement trace`, and `Version scope and deferred items`, `Live objects this strand touches`, `Native-entity map`, `Groups, views, forms, docs, dashboards` and `Irreversible operations, UI steps and client decisions` in place of the shortened ones), and the ten tests that use it pass unchanged. The earlier R43 and R47 tests pass, and `test_leak_grading.py` grades its 250 cases with every outcome kept. The leak gates pass under 3.9.6 (93 tests in `test_leak_wall.py`, 256 in the four files), and `ReviewPart2Test` under 3.14.6 (43 tests). *Measured:* the two planted records publish the same single words with and without the change (19 for record b, 21 for record a); with the sixteen titles in sentence case nothing of them is published (probes `<scratchpad>/wp4-run4/g18b/probe.py` and `measure.py`). *Touch-up:* the API note gains T15; `leak-review-part2.md` notes the fix under its table, with no row, since no finding of the review asked for it. *Owed to WP7:* when the blueprint template and `blueprint-guide.md` land, their headings are plugin vocabulary. R29's `shared-words` and R32's `shared-phrases` regions, and R41's release check, should cover them as they cover `shared/`, so that no word or run a session copies from them is published from a record; the template writes the titles in sentence case, as the guide numbers them. *Nod:* the titles in title case (`## 3. Requirement Trace`) still publish: probe `titlecase.py` in the same folder found `trace` and fifteen runs such as `Live Objects`, `UI Steps`, `Plan Tier` and `The Lists` in record a's entry, and `terms` over the real `shared/` then blocked in five of its files. That is the fail-safe side (the release check stops, and other records' prose that writes those runs blocks), so headings are still harvested, and WP7's owed item above closes it. *Nod:* a real one-word name that is also an ordinary word whose plural with `s` or `es` is a stop word is no longer published as a single word.

*Found by:* the G18 fix (R49)

### R51 Only this client's own words make a name this record's: calls, inputs, research and `CLIENT.md`'s names

**Decision.** O, this record's own set for the wall (X27), now holds only this client's own words: every file under `calls/`, `inputs/` and `research/`, whole, and from `CLIENT.md` its `name`, its `former_names` (R40) and its slug, read from the front matter. The session's working files no longer feed O: `log.md`, `meetings.md`, `CLIENT.md`'s body, and every strand file (`STRAND.md`, `SUMMARY.md`, `readiness.md`, `close-out.md`, the `solution/` notes, `exclusions.md`, `versions/*/*.md`) and the live map. The blueprint's client-facing lines (sections 1 to 15, the prompt blocks and the glossary, as X09 and R49 read them) stay O, as X11 decided; its other lines are blanked in place, so they feed nothing and no candidate runs across them. One function, `own_text(rel, text)`, gives the part of a record file that feeds O, or nothing. Every file still feeds F, R, Q and D as X11's table says, so the index's harvest and the figures are unchanged; only the own test narrows. R37's rule (none of the strand's blueprint files is O while a blueprint is checked) and Z15 (a checked file never makes its own words this record's) are unchanged, and the allowlist still feeds no set (Y01). This changes X27's reading of "and not this client's record", and X11's O column, from the whole record to the parts named above. The user's decision (2026-10-21), word for word: "count calls/, inputs/, CLIENT.md (with former names) and research/ as this client's own words; working notes, the log and strand files no longer count. Update the tests that relied on the old reading."

**Reason.** The user's words above are the source that wins, over X27's reading and X11's O column. Under the old reading any file the session writes made a word this record's, and a mix-up of two clients is exactly what writes such a line: the finding's payload `{"name": "Tallowmere sync", "description": "Depot loads"}`, where `Tallowmere` is another record's name, blocked alone and passed after one line in `solution/build-notes.md` (`Mirror the Tallowmere sync column.`) or in `log.md`. Now only what came from the client, or the research the session gathered about this client, can clear it. The blueprint is not a working note in the user's sense, for two reasons. Its client-facing lines are the plan the client approves and the build copies into monday, so a payload built from it carries its planned names by design (X11). And those lines are the one session text the wall itself checks before they are built: `blueprint` runs the wall on exactly those lines at the draft check and again at the build guard (R37, R49, P5), and while it does, none of the strand's blueprint files counts as O (R37), so a name enters them only past a check that blocks it. The blueprint's internal lines (section 16 and the rest) get no such check, so they are working notes and no longer count. The slug is kept beside the names because it is the record's own folder name (X30), which X26 step 1 publishes beside the name; it is the record's identity, not a note. The change only takes text out of O, so it can add blocks and never clear one.

**Follow-up.** *Build:* done. *Test:* `test_G17_R51_X27_X11_a_line_the_session_wrote_never_makes_another_records_name_this_records` (record b holds `Tallowmere` and its fuel figure `186,730`; the finding's payload, and `{"description": "Fuel comes to 186,730 a year."}`, block alone and still block after the line `Mirror the Tallowmere sync column. Fuel was 186,730 last year.` in record a's `solution/build-notes.md`, `log.md`, `meetings.md`, `STRAND.md`, `SUMMARY.md`, `readiness.md` or `versions/v0.1/notes.md`, in section 16 of the blueprint, or in `CLIENT.md`'s body) failed before the change at `solution/build-notes.md`, exit 0. Clean control `test_G17_R51_a_name_in_this_records_calls_inputs_or_research_and_its_own_names_still_pass` (the name and the figure pass once a line holding them is in the call's transcript, the call summary, the raw panel procedure, the research brief or a new research note; record a's own name passes while record b's brief writes it and no other file of record a does, `CLIENT.md`'s name and slug each clearing it (probe `<scratchpad>/wp4-run4/g17/probe.py`: with neither, the test fails); `Tallowmere Joinery` in `former_names` passes `Tallowmere sync`; the planned name in the blueprint's section 4 passes in a payload; a name written only in record a's build notes is still published by `index` and blocks from record b) passed before and after, as a clean control should. The seven tests an earlier attempt broke, which left `research/` out of O, rely on a word in `research/`, which the user's decision counts; each one's intent is "this client's own word passes", so each keeps what it proves and none needed a change: `test_L187_a_term_in_both_records_passes` (`Brindlecombe Paints` in each record's `research/2026-10-01-vendors.md`); `test_X11_X27_a_draft_never_makes_another_clients_name_this_records_own` (`Quessel Holdings` in `research/2026-10-02-partners.md`, while the draft and `.work/` copies still clear nothing); `test_X27_fused_and_phonetic_candidates_and_their_twins` (`skipper`, `Silver` and `lantern` in record a's brief, the words of the fixture's twins `T05-t` and `T14-t`); `test_G09_R37_a_word_held_outside_this_strands_blueprint_files_is_still_this_records` (the brief's line, and strand 002's blueprint, whose word sits in section 4, a client-facing line); the clean case of `test_G11_R42_X27_ordinary_two_word_phrases_never_fuse_into_another_records_single_word` (`Tallow Mere` in `research/2026-10-21-notes.md`); the clean case of `test_G12_R43_ordinary_plurals_and_markdown_code_stay_clean` (`Blue Harbours` in the same note); and `test_G16_R47_X26_ordinary_words_published_as_one_word_names_stop_blocking` (`supply` and `freight` in the brief). No test relied on a session file making a word this record's; the G17 test above holds the new reading. `test_leak_grading.py` grades its 250 cases with every outcome kept; `T05-t` and `T14-t` pass, their words sitting in `research/`. The leak gates pass under 3.9.6 (95 tests in `test_leak_wall.py`, 258 in the four files), and `ReviewPart2Test` under 3.14.6 (45 tests). *Touch-up:* the API note gains T16. *Nod:* the cost in use: a name this client uses that sits only in working notes, the log or strand files, and also in another client's entry, now blocks in this client's output. The way out is a call, a document or a research note that holds it; an allowlist row does not clear the wall (X10). *Nod:* the gap it leaves: a mix-up written into a research note still clears a name, and so does one written into a call summary or a document snapshot under `inputs/`, which the session writes from the client's words; the user's decision counts those folders whole. *Nod:* the blueprint's client-facing lines stay this record's for payloads, for the reasons above; R37's gap is unchanged, so a name that reached one strand's blueprint without a clean `blueprint` run is O for another strand's check and for payloads, and the review's second fix for it still waits for the user's word. *Nod:* the prompt read "CLIENT.md (with former names)" as `CLIENT.md`'s name and former names, and the slug was added as the record's folder name; `CLIENT.md`'s body (the strand index, the stakeholders, the folder map) is written by the session and no longer counts, so a stakeholder named only there, and also in another client's entry, blocks until a call, document or research note holds the name. *Nod:* a `CLIENT.md` whose front matter cannot be read gives O nothing, which only adds blocks; `index` already refuses such a record. *Finding:* G17.

### R52 A section heading's title is checked with its section, and the template's own titles are not

**Decision.** X09 and Z19 widened. `blueprint` now checks the title of each level-2 heading numbered 1 to 15 as part of that section's text: the words after the number and its separator (R49's `SECTION_NUMBER`), before any closing hashes, kept in place on the heading's line with the number and the marks blanked (`section_titles`), so a hit is reported at the heading's own line and column. The title is checked in the blueprint unit, under every rule the section's body meets, the wall included, and never as glossary text, even where a glossary block runs across the heading. A heading whose title is its section's own title in the blueprint template is not checked: the script holds the sixteen titles as `SECTION_TITLES`, the same words as R50's test helper, and compares the title's normalised words (X24, so letter case and punctuation aside) with its own section's title only. A template title under another number, or with a word added, is checked whole. Because the title is client-facing, the heading lines of sections 1 to 15 feed none of F, R and Q in any blueprint file (the checked one, its frozen copies and the other strands' blueprints), as the client-facing body does not (X11). They still feed D, as R49 and R50 have them, and they do not join O.

**Reason.** The heading is client-facing: sections 1 to 15 feed the bundle (`shared/record-map.md` line 39), and the heading goes with its section, so its words belong to it. Before the change `## 4. Tallowmere mapping`, where `Tallowmere` is another record's name, passed with exit 0. The template's own titles are plugin vocabulary, not client data, and two rules flagged them once headings were checked: section 6's `Live objects this strand touches` holds `strand`, a `method` term of the shipped list, and the two titles of six words or more (sections 14 and 15) blocked as runs copied from the blueprint's own heading lines, which fed R. The exact-title rule keeps the first from blocking every blueprint, and taking the headings out of F, R and Q keeps any long title the session writes from being a run copied from itself or from a frozen copy. That second part narrows a block: a scan or payload that copies six or more words of a section 1 to 15 heading no longer blocks as a copied run. X11 and Z19 win, since client-facing blueprint text feeds no set. Keeping the headings in D only adds blocks elsewhere, and leaving them out of O can only add blocks; both are the fail-safe side.

**Follow-up.** *Build:* done. *Test:* `test_R50_R52_X09_Z19_a_section_headings_title_is_checked_with_its_section` (record b holds `Tallowmere`; `## 4. Tallowmere mapping`, `## 4.Tallowmere mapping`, `## 4 Tallowmere mapping`, `## 4) Tallowmere mapping`, `## 4: Tallowmere mapping` and `## 4. Tallowmere mapping ##` block with one wall `name` finding at the heading's line and the column of the name; `## 4. The cutting list names each panel by cabinet`, a run of record a's research brief, blocks as one copied run at the heading's line, with or without a glossary under it; `## 4. Fuel budget 186,730`, record b's figure, blocks with a wall `figure` finding at the heading's line; a glossary holding that run under `## 4. Structure mapping` passes, so Z19's rule is unchanged) failed before the change at `## 4. Tallowmere mapping`, exit 0. Clean control `test_R50_R52_a_blueprint_whose_headings_are_the_template_titles_passes_as_before` (the sixteen template titles in record a's blueprint, its frozen copy, strand 002's blueprint and record b's blueprint, all indexed: `blueprint` is exit 0 with no finding; the same with section 4's heading `## 4. Jobs board with one sync column for each yard`, a long title of the session's own, in all three of record a's files; `lint.SECTION_TITLES` equals the helper's; `section_titles` keeps a title-case template title out and keeps `Product fit` under section 4 and a custom title, each alone in its place) passed before at its blueprint check and failed at `section_titles`; with the check built and the headings still feeding R, its long-title case failed with a copied run from the blueprint itself. The earlier R49 and Z19 tests pass unchanged, and `test_leak_grading.py` grades its 250 cases with every outcome kept. The leak gates pass under 3.9.6 (97 tests in `test_leak_wall.py`, 260 in the four files), and `ReviewPart2Test` under 3.14.6 (47 tests). *Touch-up:* the API note gains T17. *Owed to WP7:* the blueprint template and `blueprint-guide.md` write the sixteen titles exactly as `SECTION_TITLES` holds them, in sentence case; when they land, a release check (`tools/lint_plugin.py`, as R41 does for the `shared/` regions) should compare `SECTION_TITLES` with the template, so the two cannot drift apart. *Nod:* section 6's template title, `Live objects this strand touches`, writes `strand`, a `method` term the lint blocks anywhere else in client text, and the client sees it in the bundle. The lint lets it pass as the template's own title; WP7 may want a client word there instead. *Nod:* a template title with any word changed or added is checked whole, so `## 6. Live objects this strand touches for the yard` blocks on `strand`; the way out is the template's title as it stands, with the added words in the section's text. *Nod:* a section heading's words still reach D, as R49's nod said, and do not join O, though R51 makes the blueprint's client-facing body O; a name written only in a heading of this record's blueprint is therefore not this record's for a payload, which only adds blocks.

*Found by:* the R50 fix

### R53 A run, a quote or a name split over payload strings is checked on one joined text

**Decision.** After every string of a payload has been checked on its own, `payload` checks one joined text (`check_joined`): every string that joins, in walk order (X22), joined by single line breaks, under the copied-run, quote and wall rules only (`spanning_rules`), on the text and on its HTML-decoded copy (F05). Object keys do not join. X22 checks each key as a string of its own at `<key>`, and R25 already treats what is structural in a payload as structure; a key is the API's field name (`name`, `description`, `text_1`), so joining it would put a structural word between every two values and break the very runs the join is for. Numbers do not join, since X22 gives them the figure and number rules only, and neither does a structural id, so G24's exemption (Y08) stands. A string that holds JSON (R25, R34) does not join as raw text; the strings walked inside it join in its place, so the join follows the walk into `column_values`. The single-text rules (terms, markers, ids, figures, phonetic, paraphrase, tool categories) stay with each string, so the joined text never reports them a second time. A hit inside one string is that string's own check's and is dropped. A hit that spans strings is reported at the first string it touches, with a new key, `fields`, naming every string it spans, unless a finding of its rule and class in one of those strings already overlaps it; so a run found in one field is reported once, also where the next field goes on with it. A JSON file that `scan` reads goes through the same walker (T3), so it is joined the same way.

**Reason.** A§:916 (runs of six or more words and client quotes of eight or more words, in every monday text payload) and X22 (every string value at every depth is checked) win. The walker made each string its own unit, so part 1's internal run split five and five over `name` and `description`, a client quote split four and four over two workflow steps, and another client's partner written as two column titles each passed with exit 0, while each in one field blocked; F41 left the split quote to part 2. A single line break is already white space inside a run for these three rules: runs and quotes read across lines, and the wall's candidates and R42's join cross one line break but not a blank line or a sentence end. So the join blocks only what one text holding the same words would block. Keeping to the three rules that read across words keeps the per-field findings the only report of everything else. The change adds blocks and clears none.

**Follow-up.** *Build:* done. *Test:* `test_G19_R53_A916_X22_a_run_a_quote_or_a_name_split_over_two_payload_fields_blocks` (record a's brief line `Laminate offcuts pile up beside the panel saw before collection` split five and five over a board's `name` and `description`; the call's quoted words `every quote goes out late because the cutting` split four and four over two workflow `steps[].text`; record b's partner `Blue Field` as two column titles; the run split over two text columns of a `column_values` string beside a structural id in `item_ids`: each blocks once, at its first field, with `fields` naming the strings it spans; the one-field controls blocked before; a draft `columns.json` under `scan` is joined too; the run split between a key and its value passes; `--spans` covers the first field's part) failed before the change at the first split case, exit 0. Clean control `test_G19_R53_ordinary_joins_pass_and_a_run_inside_one_field_is_reported_once` (a workflow of ordinary steps; the column titles `On`, `track`, `Blue`, `Status` and `Field` while record b publishes `Ontrack` and `Blue Field`; `Panel saw` and `before collection`: each exit 0 with no finding; a run, a run that goes on into the next field, a quote and `Blue Field`, each inside one field, reported once and without `fields`) passed before and after, as a clean control should. Probe `<scratchpad>/wp4-run4/g19/probe.py`, run with the joined check switched off, reproduces the finding's three inputs (exit 0, each control exit 1); with it on, all six block. `test_leak_grading.py` grades its 250 cases with every outcome kept, and `<scratchpad>/wp4-run4/g19/measure.py` finds every case's findings the same with the joined check on and off. *Measured:* on `P-generic-p.json`, the trap fixture's largest payload (722 bytes, 17 strings), `payload` takes about 42 ms against 34 ms, so about 8 ms more (the median of 40 runs, 3.9.6, in process). On G29's size, 20,001 short strings, it takes 19.8 s against 15.0 s (`<scratchpad>/wp4-run4/g19/size.py`); X42 sets no time cap. The leak gates pass under 3.9.6 (99 tests in `test_leak_wall.py`, 262 in the four files), and `ReviewPart2Test` under 3.14.6 (49 tests). *Touch-up:* the API note gains T18. *Nod:* a run split between an object key and its value passes, since keys do not join; each is still checked alone, and monday's tool inputs do not carry prose as keys. *Nod:* any string that sits between the two halves in walk order breaks the join, as a word between them would in one field: two column titles with a column `type` or a text id between them are not joined, and neither are halves in fields that are not next to each other. Joining every pair of strings would cost far more and would join unrelated fields. *Nod:* the prompt named payloads; a `.json` file that `scan` reads is walked the same way, so the fail-safe reading joins it too. *Finding:* G19.

### R54 A key written twice in one JSON object is exit 3, in every JSON file the lint reads

**Decision.** Every JSON file the lint reads is read strictly (`strict_json`): a key written twice in one object, with the same value or another, is exit 3 naming the file, the key's path in X22's form (`$.item_name<key>`) and the key, and saying to write each key once. This covers the payload file (X22), a `.json` file `scan` reads (it goes through the same walker, T3), `local/settings.json` (already strict since R28; its error field is now the path, not the bare key) and `<home>/clients-index.json`, whose error also points at the backup. A string in a payload that holds JSON (R25, R34) is read the same way, and a repeated key inside it is exit 3 at the path through that string (`$.column_values<json>.text_1<key>`). A string that only looks like JSON stays plain text: text after the object means it is not JSON, so a sentence that opens with an object repeating a key is checked as text, as before. The same key at two depths, or in two objects, is not repeated. The lint reads no other JSON: `terms` reads `.json` files as text, where a repeated key changes nothing, and `account.json`, the lock and the fixture's `manifest.json` are not read by the lint at all. The check costs nothing on a file without a repeated key: the hook compares a count, and the second, slower parse that finds the path runs only after a repeat is found.

**Reason.** X22 (the payload file is the tool input exactly as it will be sent, read as one JSON value) and A§:920 (a file the lint cannot apply as written is a stop) win. `json.loads` keeps the last value of a repeated key, while another reader may keep the first, so the first value was never checked: the finding's `{"board_id": 41873925, "item_name": "Tallowmere sync", "item_name": "Depot loads"}` passed with exit 0, and `args_digest` described an object without another client's name, which a reader that keeps the first value would send. A file whose meaning depends on its reader is not one the lint can vouch for. In the index the same repeat would let one copy of an entry hide another, and the wall would lose a record's names without a word.

**Follow-up.** *Build:* done. *Test:* `test_G20_R54_X22_a_key_written_twice_in_a_payload_is_exit_3_naming_the_key` (the finding's input, the same key written twice with one value, a repeat inside a workflow step, and a repeat inside a `column_values` string, plain and behind a zero-width space: each exit 3 on the payload file at the key's path, the problem naming the key and the expected text saying to write it once, as the tool will receive it; a `columns.json` draft under `scan` the same) failed before the change at the first case, exit 0. `test_G20_R54_X02_a_key_written_twice_in_the_index_or_the_settings_is_exit_3` (record b's entry written twice in the index; a second `schema` key in the settings: exit 3 on each at its path) failed before the change at the index, which passed. Clean control `test_G20_R54_a_key_at_two_depths_a_repeat_in_plain_text_and_the_fixture_pass` (`name` at two depths, `title` in two columns, `text_1` at two depths inside a `column_values` string, a sentence that opens with an object repeating `item_name`, and `item_name:` twice in plain text: each exit 0 with no finding; every JSON file of the trap fixture, and every JSON string inside one, writes each key once) passed before and after, as a clean control should. `test_leak_grading.py` grades its 250 cases with every outcome kept. The leak gates pass under 3.9.6 (102 tests in `test_leak_wall.py`, 265 in the four files), and `ReviewPart2Test` under 3.14.6 (52 tests); `tools/lint_plugin.py` reports no error. *Touch-up:* the API note gains T19; `json_value` loses its `unique` flag, since every caller is strict now. *Nod:* a key written twice with the same value both times is exit 3 too; the lint does not judge which copies are harmless, and the session's own writer never repeats a key. *Nod:* the index is read strictly as well, as the review asked, so a hand-merged index with an entry written twice stops every check and `index` itself until the last copy is restored from `<home>/local/backup/`. *Nod:* the prompt named the payload file and the index; a `.json` draft under `scan` goes through the same walker, so the fail-safe reading makes it strict too. *Finding:* G20.

### R55 `mmb_common.read_json` and `record.py`'s index reader refuse a key written twice, through the lint's one strict reader

**Decision.** The strict JSON reader moves from `leak_lint.py` into `mmb_common.py` unchanged: `strict_json(text, base="$")`, which raises `ValueError` on text that is not JSON and `RepeatedKey(path, key)` on a key written twice in one object, with `key_path` and `SIMPLE_KEY` beside it. `leak_lint.py` keeps the names `strict_json`, `RepeatedKey` and `key_path` as `mc.strict_json`, `mc.RepeatedKey` and `mc.key_path`, so R54's reading and output are unchanged and there is one implementation, as R39 did for `digest`. `read_json` reads through it: a repeated key is `CannotRun` (exit 3) naming the file, with the key's path in X22's form as the field (`$.archive<key>`), the problem "the key "<key>" is written twice in one object, so what the file says depends on the program that reads it" and the expected "each key written once in its object: keep the copy meant and remove the other"; text that is not JSON keeps its old error. `record.py`'s `index_keys` reads `<home>/clients-index.json` through `strict_json` too, and a repeated key there is R39's unreadable-index stop (exit 3, `<home>/clients-index.json`, `(whole file)`), its message unchanged. A repeated key takes each caller's existing path for a file that is not JSON, and no caller changed: `home init` (`local/settings.json`) is exit 3; `check`'s settings check turns the `CannotRun` into a warning, as it does a torn file (G34), the field now the key's path; `read_settings` (`ledger.py`'s never-show workspaces and default build account, `record.py`'s archive choice), `account.json`, `build.json`, `.work/history.json`, the condense plan, the session's input files under `ledger.py`, another record's `account.json` in the cross-record check and the run-id count are exit 3 through each script's `main()`; the lock, read through `read_lock`, is exit 3 on `.work/lock.json`, field `lock`, with the problem naming the key and the expected naming the repair, so `lease repair` accepts such a lock as torn and skips a lock backup that repeats a key; `ledger.py`'s inventory copy reads as absent, as a torn copy does. A file `record.py`, `ledger.py` or `mmb_common.py` writes itself never repeats a key, because `json_text` dumps a dict, so the strictness bites only on a file edited or merged by hand, or one a session hands in. `ledger.py`'s `json` fenced blocks inside markdown keep their plain reading; they are no file of the record's state.

**Reason.** R28 and R54 made the lint refuse a settings file or an index with a key written twice, because `json.loads` keeps the last copy while another reader may keep the first. `record.py` and `ledger.py` read the same settings with `json.loads`, and `record.py init` the same index, so one file meant two things: the lint stopped on it while the scripts acted on the last copy, and `init` could find a slug free in an index the lint refused. Reading the scripts' own state files the same way is the fail-safe side: a hand-merged lock or `account.json` with two epochs or two bindings is a file the scripts cannot vouch for, and it stops with the error a torn file gives, rather than a silent pick. One reader, moved rather than copied, keeps the scripts and the lint from drifting apart.

**Follow-up.** *Build:* done. *Test:* `test_R55_R54_a_key_written_twice_in_one_object_is_exit_3_naming_its_path` in `test_mmb_common.py` (a repeat at the top, inside an object, inside a list's object and under a key that needs brackets: `RepeatedKey` with X22's path, and `read_json` exit 3 with that path as the field, the problem naming the key and the expected saying to write it once; the same key at two depths and in two objects reads as `json.loads` reads it; `leak_lint.py` has no `def strict_json(` and uses `mc.strict_json`). In `test_record_part2.py`, `test_R55_R28_home_init_stops_on_settings_that_write_a_key_twice` (a torn settings file and one with `archive` written twice: each exit 3 on `local/settings.json`, nothing written), `test_R55_R28_check_reads_settings_that_write_a_key_twice_as_a_torn_file` (`schema` written twice: the same exit code and blocking set as a torn file, one warning at `$.schema<key>` naming the key) and `test_R55_R39_init_stops_on_an_index_that_writes_a_key_twice` (an entry key, `schema` and an entry's `names` each written twice: exit 3 on `<home>/clients-index.json`, `(whole file)`, R39's problem, nothing written; the index with each key once passes). In `test_ledger.py`, `test_R55_a_lock_that_writes_a_key_twice_stops_as_a_torn_lock_does` (`epoch` written twice in a held lock: `intent` is exit 3 with the torn lock's file, field and expected, nothing written, the problem naming the key; the lock as written runs). All five failed before the change; R54's lint tests pass unchanged. *Gates:* the whole suite passes under 3.9.6 (615 tests); under 3.14.6 `test_mmb_common.py` (52), `test_record.py` (51), `test_record_part2.py` (52), `test_ledger.py` (108), the four leak files (265) and `test_lint_plugin.py` (25) pass; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* WP2's `API-mmb_common.md`, `API-record.md` and `DECISIONS.md`; the API note gains V2. `ledger.py` is unchanged, so WP3's notes are too. *Nod:* `check` stays as it was for settings it cannot read, a warning rather than a stop, so a settings file with a repeated key warns in `check` while the lint and `home init` stop on it. *Nod:* a key written twice with the same value both times stops the scripts too, as it does the lint (R54).
*Found by:* the G20 fix (R54)

### R56 A table row's sentence reads its header row and first cell for the cost cue, and amount, total and fuel are cost cues

**Decision.** When the number parser (`parse_numbers`) decides whether a number's sentence holds a cost cue (X25), a number in a body row of a Markdown table also reads the table's header row and the row's first cell (`table_cues`). A table is a line holding a pipe followed by a rule row (`|---|---|`, colons and outer pipes optional) and every line holding a pipe after it; a run of lines that each start with a pipe and have no rule row is read as a table whose first line is the header. A cost cue in the number's own sentence counts as before, and the borrowed cue is only added, never taken away. A bare run of eight digits or more, the id row's shape (X34), is never lent a table's cue, and dates, times, versions, years and list ordinals stay masked, so neither is a figure in a table cell. The cost cues of the pinned `cost-cues` region gain `amount`, `amounts`, `total`, `totals`, `fuel` and `fuels`; `spend`, `spends`, `spending` and `spent` were there already. The parser serves both sides, so the reading holds everywhere X25 reads a cue: on the record's side (F's split into cost figures and record numbers, and so the wall's `figures`, U1) and on the checked side (a figure from 10 to 999 beside a cost word). The review's second option, publishing every number of 1,000 or more from a client source, is not built: coarse round numbers would then collide across clients, as note G22 already shows for exclusion figures.

What this changes for part 1: a cost figure in a table of this record's own files is now a cost figure of F, not a record number, so a draft or a payload that writes it is a `figure` block (1,000 or more in any rendering, 10 to 999 beside a cost word) where it was a `record-number` warning. A table in a checked draft or payload lends its rows the header's cue too, so a client figure from 10 to 999 under an `Amount` column blocks, and under a `Count` column still warns. No finding moves to a lesser severity.

**Reason.** U1 (the wall holds the record's client figures above a floor) and X25 (the cost cue, read sentence by sentence) win. X12 makes each table row its own sentence, so a row such as `| Fuel | 731,946 |` under `| Line | Amount |` held no cost word, and the figure never entered the wall: the finding's text `The line comes to 731,946.` passed in record a with exit 0. Client figures sit in tables more often than in sentences, and the header is where a table says what its numbers mean. The first cell is read as well because a full stop inside it (`Fuel, est.`) cuts the row into two sentences. The second option was not chosen because three significant digits on every client number would put ordinary volumes and counts on the wall, where two clients' coarse forms meet (G22). The change adds cost figures and blocks, and clears none.

**Follow-up.** *Build:* done. *Test:* `test_G21_R56_U1_X25_a_cost_figure_in_a_table_without_a_cost_word_in_its_row_blocks_on_the_wall` (record b's brief holds the finding's table; a table whose cost word `Cost` is only in the header; one whose only cue, `Fuel, est.`, is in a first cell cut off by a full stop; one written without outer pipes under `Spend`; one under `Total` with no rule row; and the sentences `The amount for the cold store came to 263,914.` and `Fuel came to 618,275 last year.`: all seven figures are in record b's entry, `The line comes to <figure>.` blocks with a `figure` wall finding in record a for each, and the finding's text passes in record b) failed before the change at the entry, which held none of the seven. `test_G21_R56_X25_a_cost_figure_in_a_table_of_this_records_own_files_meets_the_figure_rule` (part 1: record a's brief gains `| Varnish | 58,214 |` and `| Varnish tin | 145 |` under `| Line | Amount |`; the draft `We set aside 58,214 for the varnish.` and a draft table row `| Varnish tin | 145 |` under `| Item | Amount |` each block with rule `figure` only, and the same row under `| Item | Count |` is a `record-number` warning) failed before the change at the first draft, exit 2. Clean control `test_G21_R56_counts_dates_and_ids_in_a_table_publish_no_figure_and_a_cued_sentence_works_as_before` (a `| Week | Pallets |` table of counts, a cost-headed table whose rows hold the dates `2026-08-14` and `14 August 2026` and the order ids `52817403` and `61940275`, and the sentence `The yard holds 4,318 pallets on a busy night.`: none of the counts, ids, date digits or the year is in record b's entry and `We moved 2,617 pallets in week 34.` passes in record a, while the two amounts in the id rows and the brief's cued 186,730 are published and `Fuel comes to 186,730 a year.` blocks) failed before the change only at the two amounts; its clean parts passed before and after. `test_leak_grading.py` grades its 250 cases with every outcome kept. The leak gates pass under 3.9.6 (105 tests in `test_leak_wall.py`, 268 in the four files), and `ReviewPart2Test` under 3.14.6 (55 tests). *Measured:* the two planted records publish the same wall figures before and after: record b 1 (186,730, from 2 cost figures), record a 6 (1,450, 12,600, 23,750, 41,200, 96,400 and 263,480, from 13 cost figures and 7 record numbers). The fixture's only tables, the strand tables of both `CLIENT.md` files and record b's call alias table, hold no cost word and no number of 10 or more, and its one use of a new cue word, `fuel` in record b's brief, sits in a sentence `spend` already cued (probe `<scratchpad>/wp4-run4/g21/measure.py`, outputs `before.txt` and `after.txt` beside it). *Touch-up:* the API note gains T20; X25's list of cost words is read with the six above added, in the pinned region, and X25's text is left as decided. *Nod:* the whole header row lends its cue to every cell of a row, not only the column under the cost word, so `| Week | Pallets | Cost |` makes the pallet counts cost figures too; that only adds blocks. *Nod:* `total` and `fuel` are cues in any sentence, not only in a table, so a record line such as `The total came to 4,212 pallets.` now makes a cost figure that warned before; that only adds blocks. *Nod:* an id written in groups (`52 817 403`) reads as a number and is lent a table's cue; only the bare run of eight digits or more is the id shape, which is the fail-safe side. *Nod:* only Markdown tables are read this way, as the review asked; a table in a `.docx` input or written in HTML has no pipes and is not read as a table, so a cost figure there still needs a cost word in its own sentence. *Finding:* G21.

### R57 An exclusion figure keeps two significant digits on the wall, or its own one

**Decision.** An exclusion figure's wall forms (`build_entry`, X25's last bullets, Z17 item 1) now stop at the largest k whose form still holds the figure's first two significant digits, or its one for a figure written with one significant digit (`exclusion_top`); the exact form, k = 0, is always kept. So 58,315 publishes `58315e0`, `5831e1`, `5832e1`, `583e2` and `58e3`, and no longer `5e4`, `6e4` or `1e5`; 4,250 publishes `4250e0`, `425e1`, `42e2` and `43e2`, no longer `4e3`; 60,000, a figure of one significant digit, keeps `6e4` (`sixty thousand`, precision 10,000) and drops `1e5`, the round-up of 0.6 past its own leading digit. `figure_forms` takes the top k as an optional third argument; cost figures (n of 100 or more, three significant digits) and O (n of 1 or more at every k, Z17 item 4) are unchanged. The checked side is unchanged: a number is tested at its own precision (Z17 items 2 and 3), so `58k`, `58.3k`, `$58,315` and `fifty-eight thousand` still meet 58,315, while `fifty thousand`, `sixty thousand` and `a hundred thousand` in another record no longer do. The record's own exclusion rule (X25, L87, single text) is untouched: it still matches every rendering within X25's tolerance in the record that holds the row.

**Reason.** X25's own reason for the floor wins, with A30's bound: Q1 (a) asks for a floor so that a common number shared by two clients does not block, and A30 asks the wall to block another client's figure in its normal forms. A one-significant-digit rounding of a five-digit figure (`5e4` for 58,315) is not a rendering of that figure but a round number every record writes, and since an allowlist cannot clear the wall (X10, Y01), `We expect fifty thousand visits.` blocked in every other record with no way out. Two significant digits is one step looser than the three Z17 item 1 gives the harvested cost figures, which keeps exclusion figures, rows the user barred on purpose, the wider of the two. A figure the user wrote with one significant digit is its own round form, so it keeps that form. This narrows a block: X25's "(exclusion figures: one or more)" and Z17 item 1's "an exclusion figure keeps n of 1 or more" are read as above.

**Follow-up.** *Build:* done. *Test:* `test_G22_R57_X25_Z17_an_exclusion_figure_blocks_its_renderings_and_no_longer_a_one_digit_round_number` (record b's exclusion 58,315: the five forms above are in its entry and `5e4`, `6e4` and `1e5` are not; `58,315`, `$58,315`, `58k`, `58.3k` and `fifty-eight thousand` block with a `figure` wall finding in record a; the review's `fifty thousand visits` and `a hundred thousand rows`, `sixty thousand people` and `60k visits` pass with no wall finding) failed before the change at the entry, which held `5e4`. `test_G22_R57_a_figure_written_with_one_significant_digit_keeps_its_own_round_forms` (60,000 keeps `6e4` and `sixty thousand` and `60k` block; 4,250 keeps `42e2` and `43e2`, `4.25k` blocks, and `four thousand boxes` passes; neither entry holds `1e5` or `4e3`) failed before the change at `1e5`. `test_L174_L175_X25_...` asserted `4e3` for the exclusion figure 4,250, which Z17 item 1 gave; it now asserts `42e2` and the absence of `4e3`. `test_leak_grading.py` grades its 250 cases with every outcome kept: no planted record holds an exclusion figure. The leak gates pass under 3.9.6 but for G23's two tests, which wait for R58. *Touch-up:* the API note's figure lines read with this floor. *Nod:* a one-significant-digit rounding of an exclusion figure (`sixty thousand` for 58,315) no longer meets the wall in another record, which X25 had blocked; it still blocks in the record that holds the row, and the wall still blocks the figure's own forms of two digits or more. *Finding:* G22.

### R58 A figure written with cents or with an exponent meets the wall, and so does either end of a range

**Decision.** Two readings change, and one is confirmed. First, a checked number whose precision is below a unit is tested at k = 0 both rounded half up and truncated (`tested_forms`, which replaces `tested_form`), so `412,870.50` and `412,870.99` meet a figure of 412,870 as X25's tolerance says they do (a difference below the larger precision, here 1); a number of a unit or coarser is tested rounded only, as before, and a hit on either form blocks unless O holds that form. Second, the number parser (`parse_numbers`, X25's "Reading a number") reads an exponent written on digits, `e` or `E`, an optional sign and one or two digits, with nothing after but what may follow any number: `4.1287e5` and `4.1287E+05` are 412,870 of precision 10, `4.13e5` is 413,000 of precision 1,000. The parser serves both sides and every number rule, so the record's side (F) and part 1's figure and number rules read the same value. A token that runs on into letters (`#4e5b6c`, `4e`) is no number, as before. Third, each end of a range is already read on its own since R01 (part 1's F01): `400k-413k`, `400k–413k` and `413k-430k` each give 413,000, which meets 412,870's `413e3`; the test now holds it. `0.41M` stays out by Z17 item 1, and so does `4.1e5`, two significant digits of the same figure.

**Reason.** U1 and A30 win: the wall blocks another client's figure in its normal forms. A figure written with its cents is the same figure, and half-up rounding alone (Z17 item 2) sent `412,870.50` to `412871e0`, which the integer figure never publishes, so X25's own tolerance was not kept on the wall. The exponent is the form a spreadsheet, a JSON export or a calculation prints, and a JSON number written `4.1287e5` was already held (Z17 item 5), so the same digits in a string passing was a gap of the parser, not a choice. Neither is a misspelling. Truncating only below a unit keeps Z17 item 3's k = 0 and adds no coarse form. The change adds blocks and clears none.

**Follow-up.** *Build:* done. *Test:* `test_G23_R58_X25_A30_a_figure_with_cents_either_end_of_a_range_or_an_exponent_blocks_on_the_wall` (record b's brief gains `The fuel cost came to 412,870 last year.`; in record a `412,870.50`, `412,870.99`, `$412,870.50`, `400k-413k`, `413k-430k`, `400k–413k`, `4.1287e5`, `4.1287E+05` and `4.13e5` each block with a `figure` wall finding, and `4.1287e5` passes in record b) failed before the change at `412,870.50`, exit 0. Clean control `test_G23_R58_Z17_two_digit_renderings_other_amounts_and_words_with_an_e_stay_clean` (`0.41M`, `412,860.50`, `4.1e5`, `1e3 rows`, the colour `#4e5b6c`, `Step 4e` and the build `4.1287`: no wall finding, exit 0) passed before and after. `test_leak_grading.py` grades its 250 cases with every outcome kept. The leak gates pass under 3.9.6 (109 tests in `test_leak_wall.py`, 272 in the four files). *Touch-up:* the API note gains T22; X25's reading of a number is read with the exponent added. *Nod:* the exponent is read by every number rule, not only the wall's, so a draft line such as `We logged 2e4 scans.` is now a `number` warning (20,000) where it was nothing; that only adds warnings and blocks. *Nod:* a checked amount with cents is tested truncated as well as rounded, so `412,869.50` meets a figure of 412,870 by rounding and `412,870.50` by truncation; between two clients' figures one unit apart such an amount can meet both, which is the fail-safe side. *Finding:* G23.

### R59 `ledger.py` reads a json block of the documents appendix through the one strict reader

**Decision.** `appendix_documents` (W77), which reads the `json` fenced blocks of an audit file's `## Documents appendix`, now parses each block with `mmb_common`'s `strict_json` (R55) instead of `json.loads`. A block in which a key is written twice in one object gives the document no text, the path a block that does not parse already takes: `compare` lists it as a refused document and a blocking finding against the appendix file, `field` `document <n> (line <m>)`, with the reason "a json block in which the key "<key>" is written twice in one object". A malformed block keeps its reason, "a json block that does not parse", and a block with each key once, or with the same key at two depths or in two objects, reads as before. No other read of `ledger.py` changes, and no command's output shape does.

**Reason.** R55 left these blocks on the plain reader because they are no file of the record's state, but they are what `compare` judges the audit by: `json.loads` keeps the last copy of a repeated key, so `{"query": "mutation { ... }", "query": "query { ... }"}` was scanned as the read-only query while another reader, the tool that ran the document among them, may have kept the mutation. A document the scan cannot vouch for is refused, as a torn one is; that is the fail-safe side, and one reader keeps `ledger.py`, `record.py` and the lint from meaning different things by the same text.

**Follow-up.** *Build:* done, `scripts/ledger.py` only. *Test:* `test_R59_R55_a_json_block_that_writes_a_key_twice_is_refused_as_a_malformed_block_is` in `tests/unit/test_ledger.py` (a block with `query` written twice, one with `note` written twice inside a list's object, a torn block and a sound one: the first three give no text, the first two naming their key and the third its old reason, and the fourth gives its query; the same key at two depths and in two objects reads every query) failed before the change at the first block, which gave the last query. *Gates* (for R57 to R59 together): the whole suite passes under 3.9.6 (623 tests); under 3.14.6 `test_ledger.py` (109), `test_leak_lint.py` (144), `test_leak_wall.py` (109, `ReviewPart2Test` 59), `test_leak_grading.py` (3, the 250 cases) and `test_leak_fixture.py` (16) pass; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* WP3's `DECISIONS.md` gains a pointer under "Added by WP4, 2026-10-21", and `API-ledger.md` a line. *Nod:* the repeated key is a blocking refusal of that document (exit 1), as a malformed block is, not a could-not-run exit 3, because that is the path a malformed block takes there today.
*Found by:* the R55 fix

## Added by the follow-up, run 5 (step 8), 2026-10-21

This section holds the gap the notes agent found while checking note G25 and the four answers the user gave on 2026-10-19 (R13 (b), R17 (b), R27 widened, and A30's dropped tool-category check), built after the part 2 fixes, in R29's shape.

### R60 Initials written with spaces or full stops between single capitals are looked up fused on the checked side

**Decision.** In `Wall.hits`, the checked side scans each text for runs of tokens that are each a single letter written as a capital, with only spaces or tabs between each two, and at most one full stop just after a letter (`INITIALS_GAP`): `T F M`, `T  F  M`, a tab between the letters, `T. F. M.`, `T.F.M.` and `T. F. M` all qualify. `Wall.initials` looks up every contiguous run of two to six such letters fused, `tfm`, `fs`, `khlft`, against the other entries' `names` and `terms` and the other folders' slug forms. A hit is class `name`, `term` or `slug`, as for any candidate. So `A T F M` meets `TFM`, and `X B H R D L T Y` meets `BHRDLT`. The rule holds for capital letters only, so ordinary prose with a lone `a` or `I` (`I said a word`) and lower-case letters (`t f m`, `f. s.`) are never fused. Letters split by a comma, a word or a line break are not a run either. The lookup is skipped when O holds the run in its spaced form, as R42 skips its joined lookup, and a fused form O holds passes as any candidate does. Nothing else moves: `wall_candidates` and X27 type 3 still fuse no plain spaces and still stop at four tokens, so the publishing side, the index and O are unchanged.

**Reason.** X26 step 3 publishes the initials a record writes, an all-capital token of two to six letters such as record b's `TFM` for its customer, and X27 type 3 fuses them on the checked side only when dots, hyphens or nothing join the letters, and only up to four tokens. Written with spaces, or with a full stop and a space after each letter, the same initials passed. Plain spaces fuse only under Z13 item 2's seven-letter gate (R42), which a run of two to six letters never meets. A full stop and a space read as a sentence end (X27's `RUN_BREAK`). R43's initial fuse joins one letter to the word after it, which gives `tf m` and not `tfm`. Initials of five or six letters passed in every shape but the fused one. Spaced and dotted initials are a normal form of initials the other record wrote, the same letters in the same order, not a spelling by sound, so they sit inside A30's bound. The main session read the brief's "single spaces" as plain spaces as opposed to dots, not as exactly one space (2026-10-21), so any run of spaces or tabs counts. The length cap is six because X26 step 3 publishes initials of two to six letters: a longer run can only match through a sub-run of six or fewer, and every sub-run is tried. X27's rule that plain spaces are not fused wins on the publishing side and in O, as in R42. The checked side keeps ordinary words out by needing every token to be one capital letter, so a run of capitals blocks only where another record published those very initials.

**Follow-up.** *Build:* done. *Test:* `test_G25_R60_X26_initials_written_with_spaces_or_full_stops_block_as_fused_ones_do` (record b's `TFM`, and `FS` added for Fernhollow Supply: `T F M` mid-sentence and at a sentence end, two spaces, tabs, `T. F. M.`, `T.F.M.`, `T. F. M`, `T.F.M`, `T.  F.  M.`, `TFM`, `F S`, `F. S.`, `A T F M` and a `doc` payload all block with class `name`) failed before the change at `Send the T F M report weekly.`. `test_G25_R60_X26_five_and_six_letter_initials_block_spaced_or_dotted` (record b gains `KHLFT` and `BHRDLT`, both published; spaced, dotted, dotted and spaced, double-spaced, and inside a longer run of capitals, all block) failed before the change at `Book the K H L F T run.`. `test_G25_R60_capital_runs_that_match_no_initials_and_lone_letters_stay_clean` passed before and after, as a clean control should. It covers `I A M`, `Plan B`, `Grade A B C`, `A. B. C. D. E.`, a lone `I` and `a`, lower-case `t f m`, `f s` and `f. s.`, and letters split by a comma, a word or a line break, which all pass; a spaced run record a writes itself passes while `TFM` still blocks. The trap fixture is unchanged, and its 250 grading cases keep their outcomes. *Gates:* under 3.9.6, `test_leak_wall.py` passes 112 tests and the four leak files pass 275; under 3.14.6, `ReviewPart2Test` passes 62; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* the API note gains T23. *Nod:* a capital letter that ends one sentence and a capital that starts the next are read as initials, as `T. F` is. So `Plan A. I think` is looked up as `ai`, and it blocks only where another record published those very initials and this record does not hold them. *Nod:* a run this record's own files write spaced (`the T F M crew`) is its own, so the lookup is skipped there, as R42 does, while the fused `TFM` still blocks in that record. A record that writes its own initials as `T. F. M.` only, which O does not hold spaced or fused, is blocked in that shape where another record published them; that is the fail-safe side.
*Found by:* the notes agent, checking G25

### R61 A method row whose spaced form is an everyday phrase blocks only hyphenated

**Decision.** R13 is narrowed for the `method` class only. A hyphenated method row listed in the pinned region `everyday-method-rows` (`EVERYDAY_METHOD_ROWS`) blocks only where a joining mark stands at its hyphen: `literal_regex(..., spaced=False)` puts `HYPHEN_GAP` there, a run of X32's gap marks that holds a hyphen, an underscore, a slash, a pipe or a middle dot, with spaces, commas or full stops allowed beside it. So `never-say`, `never - say`, `never_say` and `NEVER—SAY` (the dash folds to a hyphen, X28) block, while `Never say a price` and `not, obtainable` pass. The region holds the user's four picks, `never-say`, `not-obtainable`, `cost-of-waiting` and `exit-ramp`. Every other hyphenated method row keeps R13's spaced matching, and so do the other classes: the markers, the plugin rows and the internal-note marks (`never client facing` still blocks). The picks live in the script, not in `shared/leak-terms.txt`, so the list's syntax is unchanged; a unit test keeps every entry a hyphenated literal row of class `method` of the shipped list. The region is the fourteenth; `test_L274_L275_...` counts it. `tools/lint_plugin.py` does not check it, as it does not check the other script-only regions.

Every hyphenated method row, judged by whether its spaced form reads as ordinary client prose (a client, an agent prompt or a board description using it for its plain meaning) or as the method's own words; fail-safe when unsure:

| Row | Spaced form | Blocks spaced | Reason |
|---|---|---|---|
| `never-say` | never say | no | the user's pick; an agent prompt's "Never say a price" |
| `not-obtainable` | not obtainable | no | the user's pick; "the part is not obtainable" |
| `cost-of-waiting` | cost of waiting | no | the user's pick; the shipped spaced row `cost of waiting` was removed at the user's word, see the follow-up |
| `exit-ramp` | exit ramp | no | the user's pick; the shipped spaced row `exit ramp` was removed at the user's word, see the follow-up |
| `run-sheet` | run sheet | yes | the user's pick |
| `if-asked list` | if asked list | yes | the user's pick |
| `support-call check` | support call check | yes | the method's name for one check; a service desk client might say it, so unsure, and fail-safe |
| `short support-call instrument` | short support call instrument | yes | the method's own words |
| `skipped-step map` | skipped step map | yes | the method's own words |
| `deferred-answer register` | deferred answer register | yes | the method's own words |
| `client-safe block` | client safe block | yes | the method's own words; R13's test keeps it |
| `met-with-residual` | met with residual | yes | a grade name; "met with residual doubts" is English but rare, so unsure, and fail-safe |
| `v1.0 sign-off` | v1.0 sign off | yes | the method's gate name, with its version |

`first demo (v0.1)` holds brackets, so R13 left it literal and it is not in the table.

**Reason.** R13 (b), the user's answer: a method row's spaced form blocks only where it is not an everyday phrase. X10 and X39 keep a client's own use of a blocking phrase usable through an allowlist row and a caution, but an agent prompt or a board description written by the plugin has no such row, so an everyday phrase that blocks there stops ordinary work. The narrowing reaches only rows of the clearable `method` class (X10); the markers and internal-note marks are never cleared, and R13's spaced matching stays on them. Where a row is not plainly everyday, the fail-safe side wins and it keeps blocking spaced. The source that wins for the four rows is the user's answer, over R13's build.

**Follow-up.** *Build:* done. *Test:* `test_R13_R61_X39_an_everyday_method_phrase_passes_spaced_and_blocks_hyphenated` (a `generic` payload's "Never say a price." exits 0 and "Never-say a price." blocks; "not obtainable" and "not, obtainable" pass in a draft; `never-say`, `not-obtainable`, `not - obtainable`, `not_obtainable`, a non-breaking hyphen and `NEVER—SAY` block; the `exit-ramp` and `cost-of-waiting` rows' own patterns no longer match their spaced forms; since the shared edit below, "Take the exit ramp now." and "Show the cost of waiting." pass) failed before the change at the payload. `test_R13_R61_method_rows_of_the_methods_own_jargon_block_spaced_and_hyphenated` (`run sheet`, `if asked list`, `if, asked list`, `deferred answer register` and `client safe block`, spaced and hyphenated, and the internal-note mark `never client facing`) passed before and after, as a control should. `test_R13_R61_the_everyday_method_rows_are_hyphenated_method_rows_of_the_shipped_list` failed before the change, the region not existing. The trap fixture is unchanged, and its 250 grading cases keep their outcomes. *Gates:* under 3.9.6, `test_leak_wall.py` passes 115 tests and the four leak files pass 278; under 3.14.6, `ReviewPart2Test` passes 65; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* the API note gains T24. *Follow-up, done by the main session at the user's word (2026-10-21):* the run that built R61 could not finish the answer, because `shared/leak-terms.txt` listed "exit ramp" and "cost of waiting" as rows of their own beside their hyphenated rows. The user approved the shared edit in their words: "Yes, I approve both shared edits: in shared/leak-terms.txt remove the spaced rows "exit ramp" and "cost of waiting" (R61) ...". The main session removed the two rows (logged word for word in `shared-edits.md`); hyphenated "cost of waiting" in the five fixture cases that wrote it spaced (K19-p, T09-p, P-view-p, P-workflow-p and P-generic-p), with the two `match` entries of `manifest.json` and the README rows (`fixture-notes.md` section 9); updated `test_R13_R61_X39_...`, which now asserts that "Take the exit ramp now." and "Show the cost of waiting." pass; and updated `test_leak_lint.py`'s L33 (`exit-ramp` blocks, `boexit-rampx` passes, and "Take the exit ramp now." passes) and L57 ("Show the cost-of-waiting." blocks). CONTRACT's acceptance example for L33 (LT:18 to 19) is marked changed by decision (R13 (b), R61). The 250 grading cases kept their outcomes. *Nod:* the region's picks and the table above. *Nod:* a joining mark with spaces beside it, as in "never - say", blocks, since a hyphen is a separator (X24) and blocking is the fail-safe side; a comma, a full stop or spaces alone do not.
*Answers:* R13 (b), the user, 2026-10-19

### R62 "Internal only", "internal use only" and "not for clients" are cleared per client by an allowlist row, with a caution

**Decision.** X40 and X10 are narrowed for three internal-note phrases. An `internal-note` finding whose matched text has the normal form (X28) `internal only`, `internal use only` or `not for clients` is cleared by an ok row of the strand's own allowlist whose term has the same normal form, as a `method` term is cleared (X10, X39): severity `caution`, rule `internal-note` and class null kept, `cleared_by` naming the row, "kept as the client's own word" added to the problem, and the caution counted in `counts`, so the run exits 2 when nothing else blocks. Without such a row the three phrases block as before. The three normal forms are `CLEARABLE_NOTES`, in the pinned region `internal-notes` beside the phrases, so the region count is unchanged; a unit test keeps each one the normal form of an `INTERNAL_NOTE_PHRASES` entry. The spellings the phrase rows already match share the normal form and are cleared with them (`INTERNAL-USE-ONLY`, `internal-only`). The row needs no `class` key: X09 makes `class` informative, and X10 matches a row by its term alone, which is how a `method` row clears today; a row with `class: internal-note`, or any other class, clears the same. A row matches the phrase as matched, not the sentence around it, so the row reads `internal use only`; a row of the whole sentence "Internal use only, not visible to the customer" clears nothing. A row without an ok, or with an ok that says no (R18), clears nothing and warns (X09). Everything else in the region is never cleared: the speaker labels, the front-matter line, the front-matter block, "Internal: never client-facing", "never client-facing", "not client-facing", "not for the client" and "note to self". A row naming one of them leaves the block and adds X10's `allowlist` warning.

**Reason.** R17 (b), the user's answer: a Service build may say "Internal use only, not visible to the customer" as the client's own words for a board or a field, so the three phrases become clearable per client and pass with a caution, while speaker labels and note front matter stay never cleared. X10 and X39 already give a client's own word this path for vocabulary, and reusing it keeps one allowlist rule. The source that wins for the three phrases is the user's answer, over X40's and X10's "never cleared". Where the answer is silent the fail-safe side holds: "not for the client" (X40's own phrase) and "not client-facing" (R17's spelling of "never client-facing") stay never cleared.

**Follow-up.** *Build:* done. *Test:* `test_R17_R62_X39_an_internal_use_phrase_is_cleared_by_its_own_row_with_one_caution` (a `generic` payload's "Internal use only, not visible to the customer.", "Internal only: the depot rota.", "Not for clients: the stock sheet." and "Keep it INTERNAL-USE-ONLY." block with no row for the phrase; with an ok row they exit 2 with counts of one caution, no block and no warning, and `cleared_by` naming the row) failed before the change at the second payload. `test_R17_R62_X40_speaker_labels_front_matter_and_the_other_marks_stay_never_cleared` (`SPEAKER_00:`, `Speaker A:`, a front-matter block, a front-matter line and the other four marks, each with an ok row for it present, block with no caution) and `test_R17_R62_X09_a_row_with_an_empty_ok_clears_no_internal_use_phrase` (no ok, an empty ok and `ok: pending`) passed before and after, as controls should. The trap fixture is unchanged, and its 250 grading cases keep their outcomes. *Gates:* under 3.9.6, `test_leak_wall.py` passes 118 tests and the four leak files pass 281; under 3.14.6, `ReviewPart2Test` passes 68; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* the API note gains T25, its caution row and the region's new name; `leak-review.md`'s F18 row names R62. *Shared edit, for the user's word:* `shared/leak-terms.txt` lines 27 to 29 say the allowlist may clear a row of class `method` only. The three phrases live in the script's `internal-notes` region, not in the list, so the comment is now incomplete. This run may not edit `shared/`. Replace the three lines with these five:

```
# The per-client allowlist may clear a row of class method only. Rows of every other class
# are never cleared by an allowlist (9.6). The lint also lets it clear the internal notes
# "internal only", "internal use only" and "not for clients" for one client, and never the
# speaker labels or the note front matter. A term that is also the client's own vocabulary
# survives with a caution rather than being removed.
```

A probe on a copy of `shared/` found that the new lines add no word to and drop none from the `shared-words` region (R29), so `test_G01_Z12_...` keeps passing and the region needs no regeneration. *Nod:* "not for the client" and "not client-facing" stay never cleared, because the answer names only the three phrases. *Nod:* a row clears the phrase alone, never the whole sentence it sits in, as X10 matches every row.
*Answers:* R17 (b), the user, 2026-10-19

### R63 A `.com` web address written without a scheme hides its ids

**Decision.** R27 is widened for the id row's mask. Besides a link target with a scheme, a web address with no scheme whose host is one or more dot-separated labels of letters, digits and hyphens ending in `.com`, followed by `/` and a path, counts as a link that hides its ids. It is masked from the start of its host to where R27 stops a bare URL: whitespace, a comma, a pipe or a closing bracket (`COM_ADDRESS`, read by `real_links`). So `yourcompany.monday.com/boards/123456789`, `example.com/page/12345678`, `www.example.com/a/12345678` and the same address as a Markdown target pass. A host does not start after a letter, a digit, `_`, `.`, `-`, `@`, `/`, `:` or `%`, so a sentence that only holds `.com/` inside other text is not masked. Everything else stays as R27 left it: an id in the same sentence outside the address, an id after a comma or a pipe, `example.org/...`, `example.co.uk/...`, `example.com` with no slash, `example.com/` followed by a space, and a look-alike such as `hxxp://example.com/...` all block. Only the id row's mask widens: the shipped row and Z03's widening run on the masked copy, while `link_spans`, the split-id rule, the credentials, the paths, the figures, the wall and every other rule still run over the address.

**Reason.** The user's answer to R27: "I would say also include things as links if it has the .com/ or monday.com/", read as a host ending in `.com` followed by `/`. X34 and Z03 called every URL without a scheme a look-alike whose ids block; the source that wins for a `.com` address with a slash is the user's answer, over Z03's "a URL without a scheme only looks like a link" and X34's "its ids block". Other endings stay checked because the answer names `.com` only, and that is the fail-safe side. A look-alike scheme (`hxxp://`) keeps blocking because X34 and Z03 name it, and the answer is about a missing scheme, not a broken one.

**Follow-up.** *Build:* done. *Test:* `test_R27_R63_X34_a_com_address_without_a_scheme_hides_its_ids` (a `generic` payload's `yourcompany.monday.com/boards/123456789`, `example.com/page/12345678,` before a comma, `www.example.com/a/12345678`, an address in brackets, an address as a Markdown target and `EXAMPLE.COM/page/12345678|` exit 0) failed before the change at the first text. `test_R27_R63_X34_an_id_outside_the_address_or_after_another_ending_still_blocks` (an id after the address in the same sentence, after a comma or a pipe inside the address, `example.org`, `example.co.uk`, `example.com` with no slash or with a space after the slash, `hxxp://`, `ops@example.com/...`, `example.comb/...`, `ex_ample.com/...` and a split id `run-1234-5678` in the address, each blocking with an `id-patterns` id) and `test_R27_R63_L155_a_credential_in_a_com_address_without_a_scheme_still_blocks` (a token parameter blocks as a credential and a `clients/...` path as a term in such an address) passed before and after, as controls should. The trap fixture is unchanged, and its 250 grading cases keep their outcomes. *Gates:* under 3.9.6, `test_leak_wall.py` passes 121 tests and the four leak files pass 284; under 3.14.6, `ReviewPart2Test` passes 71 and `test_leak_grading.py` 3; `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Touch-up:* the API note gains T26; `leak-review.md`'s F31 and F32 rows name R63. `shared/leak-terms.txt` needs no change: its id-patterns comment says an id inside a link is exempt, which still holds. *Nod:* a split id written in groups inside such an address (`example.com/page/run-1234-5678`) still blocks, because the change widens only the id row's mask, as the answer's reading says, and the split-id rule reads `link_spans`. *Nod:* a host's labels are ASCII letters, digits and hyphens, so an address whose host holds another letter (`østby.com/x/12345678`) stays checked, the fail-safe side. *Nod:* an address right after `@`, `/` or `:` is not masked, so `ops@example.com/page/<id>` and a protocol-relative `//example.com/page/<id>` keep blocking.
*Answers:* R27 widened, the user, 2026-10-19

### R64 The tool-category check is dropped everywhere; the split-figure assertion stays

**Decision.** `leak_lint.py` runs no tool-category check. Removed: the `tool-categories` rule (`RULES` and the pinned `leak` region), `COUNTED_PREFIX` (the `tool-category-` prefix), the counting of rows of such classes in `Check.literals`, `Check.tool_categories` with its sentence and paragraph test, `Check.paragraph_of`, `Check.proper` (the proper-noun test), `Lists.category_words`, `Pattern.counted`, `EVERYDAY_CATEGORIES` (R24's seven everyday rows), `CALENDAR_FORMS` (F37's days and months), and `literal_regex`'s `plural` argument (R24's plural `s` or `es` for a counted row). A `summary` scan, whose literal rows ran only to count categories, now runs no literal row at all: it runs the number rules (the split-figure assertion among them) and the run and quote rules, as before. Kept: R24's full stop after `e.g.`, `i.e.`, `etc.`, `vs.` and `approx.`, which ends no sentence for every rule that reads sentences, the cost cue of a number and the paraphrase rule (`SENTENCE_END`); `sentence_spans` and `paragraph_spans`, which the cost cue, the paraphrase rule and the phonetic windows read. F37's rule that a day or a month is never a proper noun served only the dropped proper-noun test and goes with it; the paraphrase rule's own person test never read it, and the wall's harvest keeps its own `CALENDAR_WORDS` stop list (X26 step 6). The split-figure assertion is unchanged (A30). The `shared-words` region (R29) is regenerated after the shared edit: 47 words that only the removed classes wrote leave it (`spreadsheet`, `payroll`, `wiki`, `ticketing`, `warehouse`, `stock` and so on); the `shared-phrases` region (R32) is unchanged. The trap fixture loses its tool-category case, R12-p and its twin R12-t, and the rule category `tool-categories-three-two`, so the grading harness has 248 cases: 124 planted and 124 twins; 109 blocks, 3 warns, 1 caution, 11 limits and 124 passes; 166 `scan`, 80 `payload` and 2 `blueprint`.

**Reason.** A30, the user's decision of 2026-10-19: "the blocking of client's tools in sentences sounds too strict"; offered a warning in client builds, dropping the check or keeping it, the user chose to drop it, so the lint runs no tool-category check anywhere until something like reusing one client's material for another arrives in v2 or v3, and the split-figure assertion stays. That answers R24: its plural, everyday-row and proper-noun readings existed only for the check. A30 wins over A§:918's second assertion, BP:158's three-categories case, SF:86, X12 and PLAN §8.6; section 5's rows 19 to 21 bring the first three in line. The sentence reading of R24 is kept because it serves two rules that stay, and dropping it would split a cost word from its number at an abbreviation.

**Follow-up.** *Build:* done, `scripts/leak_lint.py`; the lint-clean fixture under `tests/unit/fixtures/tools/` stubs no `leak` rule and needed no change. *Test:* the check's own tests go from `test_leak_lint.py`: `test_L107_to_L111_tool_categories`, `test_L104_assertions_run_in_payloads_too`, `test_F25_X12_tool_categories_plural_abbreviations_and_everyday_nouns` and `test_F37_X12_a_day_or_a_month_is_not_a_proper_noun`. New: `test_F25_R64_a_full_stop_after_an_abbreviation_ends_no_sentence` (the part kept: "The tray cost, e.g. 27 in all." and the same with `i.e.`, `approx.`, `vs.` and `etc.` block as a figure beside a cost word, while "The tray cost. 27 in all." only warns, and "We heard that, e.g. Penwith is burnt out." blocks as a paraphrase while the same with a full stop passes), which failed on a probe copy whose `SENTENCE_END` ended a sentence at every full stop; `test_L104_R64_the_split_figure_assertion_runs_in_payloads_too` (L104 for the assertion that stays); `test_L107_R64_three_tool_categories_in_one_sentence_are_no_finding` (L107's planted sentence is clean, and `tool-categories` is not a rule). `test_L274_L275_embedded_regions_and_no_counted_class` replaces the count of fifteen classes: the shipped list holds no `tool-category` class and the script no `COUNTED_PREFIX`, since a class left in the list would now block as an ordinary term class. `test_leak_fixture.py` drops `tool-categories-three-two` from its rule categories and its skip of the counted classes, and counts 15 pinned rules; `test_leak_grading.py` counts the 248 cases above. Both pass once the fixture patch is applied. *Fixture:* the trap fixture is not edited here; the user approved those edits for the main session. The patch `r64-fixture.patch` in the session's scratch folder (`wp4-run5/`) removes `cases/rule/R12-p.md` and `R12-t.md`, their two `manifest.json` entries and the category, and R12-p's README row, and sets the README's counts (124 planted, 124 twins, 288 files; 27 rule cases of BP:158); `git apply` takes it from the plugin repository's root (`fixture-notes.md` section 9). *Regions:* `test_L197_terms_over_the_real_shared_folder_exits_0` passed against the regions as they were, then `SHARED_WORDS` was regenerated (47 words out, none in), and `test_G01_Z12_...`, `test_G04_Z12_...` and `tools/lint_plugin.py`'s `shared-region` check (R41) pass. The two planted records publish the same index entries before and after (names 41 and 44, terms 2 and 6, figures 5 and 20, phonetic keys 32 and 30). *Gates* (in a scratch copy of the plugin repository with the patch applied, `PYTHONDONTWRITEBYTECODE=1`): under 3.9.6 the whole suite passes, 634 tests; under 3.14.6 the four leak files pass 283 (`test_leak_lint.py` 143, `test_leak_wall.py` 121 with `ReviewPart2Test` 71, `test_leak_grading.py` 3 over the 248 cases, `test_leak_fixture.py` 16). In the real repository `tools/lint_plugin.py` gives 0 errors; no `__pycache__` is left. *Changed by decision (A30):* CONTRACT's L104 and L112 (both assertions become the one), L107 to L111, L260 and L275, and acceptance rows 25 and 26, each marked in `CONTRACT.md`. *Touch-up:* section 5 rows 19 to 21 (A§9.6, BP:158 and `safety.md` section 6), for the user's word; the API note gains T27, and its rule table and pinned-region row lose the check; `leak-review.md`'s F25 and F37 rows name R64. `test_leak_wall.py` held no tool-category test. *Shared edits:* made by the main session at the user's word and logged in `shared-edits.md`: the tool-category comment block and its fifteen classes out of `shared/leak-terms.txt`, and the `counted class prefix` row and `tool-categories` out of `record-map.md`'s `Pinned: leak`. *Nod:* T20-p's summary and T20-t's `why_clean` still mention tool categories as plain text; no rule reads them, and they are left as they are. *Nod:* `CONTRACT.md` had no clause marked changed by decision before this entry, so the mark takes the shape of WP3's checklist status, as a sub-line under each clause.
*Answers:* R24, A30, the user, 2026-10-19

## Added by the checklist (step 9), 2026-10-21

The checklist found one clause a decision of the user's could settle either way, L218, and the user settled it after a walkthrough in the main session.

### R65 L218 covers content, not the record map's pinned field names and values

**Decision.** L218 ("no run of six words in common with" an answer key, a transcript, a call or an earlier plugin) reads as covering the fixture's content. The record map's pinned front-matter field names and their fixed values are schema, not content, and a run made of them does not count against it. The two runs the probe found, both in the header of the fixture's call summary (`records/wrenfold-joinery/calls/2026-09-08-discovery.md`, the document snapshot beside it and the two overlays that copy them) and both read as plain words across `provenance: "first-hand"` and `handed_over_by: "none"`, are such runs. Answer keys s12 and s25 hold the same words because they record what a correct call summary's header carries. L218 is met by this decision.

**Reason.** The user's decision of 2026-10-21, in their words: "L218: accept. The two runs are the record map's pinned field names and values, not content. Record it as a decision and mark L218 met by decision." `shared/record-map.md` requires both fields on every call summary (`provenance`: `first-hand` | `handed-over`; `handed_over_by`: a role, or `none`), so any correct header for a first-hand call holds the run, and so does any key that describes one; the clause exists to keep the fixture from being lifted from the keys or from a call, which these two lines are not. Reordering the header to break the run was offered and not chosen: it would meet the clause's letter without changing anything about where the fixture came from.

**Follow-up.** *Build:* none. *Test:* none; L218's Accept line is an inspection with a throwaway probe, and `fixture-notes.md` section 6 records its result. *Touch-up:* CONTRACT L218 carries a "Changed by decision (R65)" line; `fixture-notes.md` nod 13 records the answer; the checklist marks L218 met by decision. *Answers:* `fixture-notes.md` nod 13, the user, 2026-10-21.

## Added by A33 (demo first), 2026-10-22

Demo 1 had seventeen blocks from `leak_lint.py` and none was a leak (`build/demos/demo1-log.md`, findings 11, 12, 13 and 25). The user decided A33 on 2026-10-22: the lint is loosened where the demo showed it blocking for nothing. These four entries build the assistant's reading of it, in R29's shape.

### R66 A key that names a monday id is structural, and so is an object key made only of digits

**Decision.** Y08's structural keys widen from a list to a rule (`structural_key(key)`): a key of the pinned `STRUCTURAL_ID_KEYS`, or one that `ID_KEY` reads as naming an id, which is `id` or `ids` alone, any key ending `_id` or `_ids`, and a camel-case key ending `Id`, `ID`, `Ids` or `IDs` after a lower-case letter or a digit, each in any case. So `parentFolderId`, `board_folder_id`, `parent_container_id`, `parentItemId`, `accountProductId`, `position_object_id`, `BOARD_ID` and `boardIDs` are structural, while `paid`, `valid`, `grid`, `android`, `PAID` and `BOARDID` are not, since a word that merely ends in the letters is no id key. A digit-only value under such a key, or each one in a list under it, is a monday id as before (`is_structural`: no leading zero, or a positive integer). An object key made only of digits, with no leading zero, is structural too, since monday keys a widget's settings and a mirror's settings by board id (`{"x_axis_columns": {"<board id>": ["status"]}}`); its key unit skips the id row, the number rules and the split ids, as a structural value does. The pinned region stays as it is, because `test_leak_fixture.py` holds a copy of it that a unit test keeps equal; the rule holds every key of the list, and a unit test says so. Unchanged: an id written into a name, a description, a label or a message, a digit-only value under any other key, a key with a leading zero, and the user's own account ids, which block under any key, structural or not (X06, Z06).

**Reason.** A33, first point: "ids that are arguments are not text". Demo 1's move (`parentFolderId`), its dashboard (`board_folder_id`, `parent_container_id`) and all four widgets (board ids as object keys) were blocked as carrying internal ids, and none was a leak (finding 11). monday names its id arguments in both spellings, so a list that grows by one key per demo blocks the next demo the same way; a rule on the key's ending covers the arguments the tools have and will add. The camel form needs its capital `I` after a lower-case letter or a digit so that an ordinary English key ending in the letters is never read as one, which is the fail-safe side.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`ID_KEY`, `structural_key`, `payload_units`). *Test:* `test_A33_R66_a_key_that_names_an_id_is_structural_and_a_word_ending_in_the_letters_is_not` and `test_A33_R66_ids_under_id_keys_and_board_ids_as_object_keys_pass` (a `widget` payload with the six keys above, the upper-case and plural forms, and board ids as keys inside a JSON settings string and in an object, exit 0 with no finding), both failing before the change; `test_A33_R66_an_id_written_as_text_still_blocks` (an id in a name, a description, a label, a message, under `paid` and `valid`, as text under `parentFolderId`, as a key with a leading zero, and as a value under a board-id key; the user's own workspace id under `parentFolderId` and as a key blocks as `seller-account`), passing before and after, as controls should. The trap fixture is unchanged by this entry: its only planted id under a key, R21-p's `notes_ref`, still blocks. *Demo:* the four demo 1 payloads A33 names (the board, the dashboard and two widgets) are clean against the demo record, and so is every other payload of the run. *Nod:* a key ending in a lower-case `id` after a lower-case letter (`parentFolderid`) is not structural, so its id blocks; no monday tool the demo used spells a key that way.

### R67 A number below 100 is no client figure, in digits or in words, on either side

**Decision.** A number below 100 (`SMALL_FIGURE`), written in digits or in words, is never a client figure. On the record's side, `Sets.add_numbers` keeps no figure below 100 in F, cost or record (it kept none below 10 before). On the checked side, `classify` returns at once for a number below 100 once the client's exclusions have been tried, so it neither blocks as a figure nor warns as a record number or as a number to check, and `split_match` tries only the exclusions for a split figure below 100. So "one", "Satellite 1", "two-way", "27 an hour", "$27", "34 staff" and "ninety-nine" pass. A client figure of 100 or more blocks in every form it did, and `words_number` now also reads "four and a half thousand" (and "two and a half million") as 4,500 (2,500,000), so 4,500 blocks written as `4500`, `4,500`, `4.5k`, `$4.5k`, `4 500`, "four thousand five hundred" and "four and a half thousand". Unchanged: a percentage keeps its own rule (a cost percentage blocks, any other of 10 or more warns), an exclusion figure blocks at any value, and the wall's figures are untouched (the index publishes only cost figures of 1,000 or more, so no entry changes).

**Reason.** A33, second point: "small numbers are not client figures". The cause of demo 1's three false positives (findings 13 and 25) was two readings meeting. The record's readiness file put "ten business days" in one sentence with "renewal", a cost cue, so "ten" was a cost figure of 10; and a number written in words takes the unit of its last written digit as its precision, so "ten" read as 10 to the nearest ten and matched every number from 1 to 19 (X25's precision rule, meant for "forty-five thousand"). The blueprint's "one" sat in a sentence with "values", and "Satellite 1", "Satellite 2" and "two-way" in a table under a "Values" header, both cost cues (R56), so each matched "the client's cost figure 10 beside a cost word". The rush line's "charged double" made no figure: its "three-day" was below 10 already. Dropping figures below 100 on both sides removes the cause: a word such as "ten" in the record can no longer become a figure, and a count, a label or a step in the checked text can no longer meet one; it also stops "a hundred" (100 to the nearest hundred) from meeting the 10. Percentages are kept because a written percentage is matched only with the record's percentages and a percent mark makes a deliberate figure, not a count; exclusions are kept because the user writes each one on purpose.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`SMALL_FIGURE`, `Sets.add_numbers`, `Check.classify`, `Check.split_match`, `words_number`). *Test:* `test_A33_R67_the_cause_a_word_number_beside_a_cost_word_was_a_figure_give_or_take_its_last_digit` (the readiness sentence parses to 10 with a cue and a precision of 10); `test_A33_R67_demo_1s_three_texts_pass_in_the_blueprint_and_in_a_payload` (demo 1's three texts, against a record whose readiness puts "ten" beside "renewal" and holds a rush line "charged double", pass `blueprint` and `payload`, and "a hundred" beside "rate" only warns); `test_A33_R67_numbers_below_100_in_digits_or_words_never_match_nor_warn`; `test_A33_R67_a_client_figure_of_100_or_more_still_blocks_in_every_form` (4,500 in the seven forms above, in a payload and in the blueprint, and 150 beside "fee"). The first of them failed before the change for want of `SMALL_FIGURE`, the other three on their texts; under the old lint "Ten working days, charged double." and "Rush orders cost three times as much." blocked against the 10. Updated, because they used the test record's 27 an hour and 34 staff: `test_L85_L86_X25_floors_and_warnings`, `test_L120_L262_flagged_numbers_are_reported_and_the_file_kept` and `test_F25_R64_a_full_stop_after_an_abbreviation_ends_no_sentence` now show the same floors and cues with figures of 100 to 999 written into the test's record. *Fixture:* four planted cases expected the old reading: K02-p (the record's loaded hourly rate, "38 an hour", blocked) and K03a-p ("14 hours a week at 38 an hour", blocked) now pass, and K03b-p ("14 hours", warned) and R14-p ("46 staff", warned) now exit 0; K02-t, K02-p's twin, no longer warns. The fixture is not edited here: `test_leak_grading.py` lays the new expectations over the manifest's, each planted one as a known limit, and the manifest and README patch is `a33-fixture.patch` in the session's scratch folder (`a33/`), which `git apply` takes from the plugin repository's root; with it applied and the override removed, `test_leak_fixture.py`, `test_leak_grading.py` and the blueprint tests pass. *Nod:* a client's hourly rate below 100, such as 38 an hour, no longer blocks, even beside a rate suffix or a currency sign (K02-p); keeping a figure of 10 to 99 beside a rate suffix or a currency sign as a block would be a small exception in `classify`, if the user wants it. *Nod:* with K03b-p and R14-p out of the warnings, the fixture's `flag-do-not-remove` category has no planted case that still warns; a case with a record number of 100 or more would restore it, for the main session to add with the patch.

### R68 The blueprint's prose meets no copied-run or quote rule; every payload still does

**Decision.** `blueprint` checks the blueprint's client-facing text (sections 1 to 15, their headings, the prompt blocks and the glossary) under every rule but the copied-run rule and the quote rule, near copies included: `Check.execute` runs `runs_and_quotes` for no unit of mode `blueprint` or `glossary`. It keeps the firm, the plugin and assistant names, the markers, the credentials, the internal ids and record paths, the exclusions, the figures (under R67), the paraphrase cues, the internal notes and the cross-client wall. `payload` keeps every rule, the run and quote rules included, and the blueprint's internal sections, its element-key table among them, still count as an internal source for every payload (Z19). `scan` is unchanged.

**Reason.** A33, third point: the blueprint never goes to a client in v1 (its client copy is v2 or v3), and its prose restates the client's own facts by design; twelve of demo 1's blocks before the card were six-word runs shared with `readiness.md`, the transcript and the blueprint's own element-key table (finding 13), none a leak. Every string written into monday is still checked in full at the write, which is the real client-facing gate.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`Check.execute`, `cmd_blueprint`'s docstring). *Test:* `test_A33_R68_a_restated_run_and_quote_pass_the_blueprint_and_block_a_payload` (a blueprint restating a run of `readiness.md`, a run of its own element-key table in section 16 and an eight-word client quote passes with no finding; the same three in a payload block as `copied-run`, with the readiness file and the blueprint as sources, and as `quote`), failing before the change; `test_A33_R68_the_blueprint_keeps_the_firm_markers_credentials_ids_and_record_paths` and, in `test_leak_wall.py`, `test_A33_R68_the_blueprint_keeps_the_wall_and_a_payload_keeps_runs_and_quotes` (another client's name in the blueprint blocks on the wall; the brief's run in a payload blocks). Updated in `test_leak_wall.py`, each asserting the new reading and, in place of the run, a rule the blueprint keeps: `test_L163_X36_the_fixture_blueprint_and_its_glossary`, `test_X09_malformed_glossary_marks_exempt_nothing_and_warn` (the broken mark still warns), `test_X11_the_blueprints_own_internal_text_still_counts` (now through a payload), `test_G18_R49_Z19_in_a_full_blueprint_the_glossary_is_exempt_from_the_copied_run_rule_only` and `test_R50_R52_X09_Z19_a_section_headings_title_is_checked_with_its_section` (a heading's title is shown checked with the firm's name). *Fixture:* R10c-p, the brief's run in the blueprint's section 3, now passes, exit 0, a known limit; R10c-t is unchanged. The override and the patch of R67 carry it. *Touch-up, for the main session:* the solution-blueprint skill and `blueprint-guide.md` need no longer ask for client-facing sections free of copied runs and quotes (demo 1's note 7), while the ids, keys and assumption ids stay in section 16; X09, X36 and L163's run clause read with this entry.

### R69 An item batch's numbers raise no number warning; every other rule still runs on it

**Decision.** In a payload of kind `item_batch`, every unit is marked sample (`Unit.sample`, set by `payload_units` at `cmd_payload`'s word), and a sample unit's numbers raise no `number` warning and no `record-number` warning, nor does a split figure in it. Every other rule runs on it as on any payload: the firm and the other terms, ids, markers, credentials, notes, the exclusions (names, terms and figures, at any value), the copied-run and quote rules, the wall, the split-figure assertion, and the client's cost figures and cost percentages, which still block.

**Reason.** A33, fourth point: every value of an item batch is invented (A28), so a number in it is not a client fact, and demo 1's sample rows warned on every invented number, twice per row (finding 12), which hid any warning that mattered. The cost-figure block is kept on sample rows: A33's heading names the warnings, A30 keeps client figures strict in a client-facing payload, and a sample value equal to one of the client's cost figures would put the client's own figure in the build, which the block exists to stop; demo 1's five item batches meet none, so the block costs the demo nothing.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`Unit.sample`, `payload_units`, `cmd_payload`, `Check.classify`, `Check.split_match`, `html_hits`). *Test:* `test_A33_R69_an_item_batch_raises_no_number_warning` (rows with invented numbers and the record number 1,350 exit 0 with no finding as `item_batch`, and warn as `board`), failing before the change; `test_A33_R69_every_other_rule_still_runs_on_an_item_batch` (the firm, an id in text, an exclusion name and figure, a cost figure, a credential, a marker, a split exclusion figure and a copied run each block in a sample row), passing before and after, as controls should. The trap fixture's two `item_batch` cases (K21a and P-item_batch) keep their outcomes. *Nod:* the user may read A33's "its numbers are not compared with the record's figures" as dropping the cost-figure block on sample rows as well; that is a small change to `Check.classify` and `Check.split_match`, left for the user's word.

*Gates for R66 to R69* (the plugin repository on Windows, `PYTHONDONTWRITEBYTECODE=1`): under `py -3.9` (3.9) and `py -3.14` (3.14) the whole suite passes, 648 tests each with 8 skips on this machine (636 before, plus 11 in `test_leak_lint.py` and 1 in `test_leak_wall.py`); `tools/lint_plugin.py --root .` gives 0 errors; no `__pycache__` is left. Against the lint as it was before A33, nine of the twelve new tests failed or errored and the three controls passed. In a scratch copy with `a33-fixture.patch` applied and the overrides removed, `test_leak_fixture.py`, `test_leak_grading.py` and the blueprint tests pass under 3.9. Every payload of demo 1's run, the board, dashboard and two widget payloads A33 names among them, exits 0 against the demo record.
*Answers:* A33, the user, 2026-10-22

## Added by A34, 2026-10-22

The user decided A34 on 2026-10-22, asked whether a client's own figures in their own build should warn instead of block: "Yes let's warn instead of block, i think the blocks are too strict, in general I think some of the lint leak is too strict." This entry builds it, in R66's shape. The broader point of A34, that the user picks what loosens next from demo 2's log, is not built here: no other rule changes.

### R70 A client's own figure warns in its own build; the exclusions and the wall still block

**Decision.** Where the lint checks text for a client's own build (`scan` in its full, summary and client-safe-block modes, `payload` and `blueprint`), a figure of the client's own record that the figure rules match is a warning, not a block: rule `figure`, severity `warn`, for a number matching a cost figure of 1,000 or more, one of 100 to 999 (`SMALL_FIGURE`) beside a cost cue, a currency sign or a rate suffix, or a percentage matching a cost percentage; rule `split-figure`, severity `warn`, for a cost figure in split form. Every form the rules read is covered, since only the severity changes: digits, words ("four and a half thousand", "four thousand five hundred"), abbreviations (4.5k, $4.5k, 2m), currency signs and codes, spaced thousands (4 500, 4.500), a figure split across a table row's cells or a line break, an HTML tag or entity between its digits, a JSON number and a link. The problem text is kept and the expected text is `OWN_FIGURE_EXPECTED` ("check the client's own figure is meant for their build; it is reported and kept"), so the user sees which figure, from which record file, and the write goes ahead (exit 2). Sample rows (`item_batch`, R69) warn the same way for such a figure, and R69's other number warnings on sample rows stay off. Still blocking: every figure on the client's `exclusions.md`, at any value and in every form (`exclusion` of class `figure`, and `split-figure` for its split form), which `classify` and `split_match` try first as before; another client's figure on the cross-client wall (`wall` of class `figure`), which `wall_hits` reports apart from the figure rules and does not change; and every rule that is not about a figure. A payload holding an own figure and a real block exits 1 with both findings.

**Reason.** A34, first two points: "a client's own figures warn", and "still blocking: another client's figures in any of their forms (the cross-client wall), every figure on the client's `exclusions.md` at any value, and everything else A30 and A33 keep strict". A client's own figure in the client's own build is the client's own fact, written back to them, and the user reads every warning before the write; the leaks the figure rules exist to stop are the figures the user has said to keep out (the exclusions) and the figures of another client (the wall), and both keep blocking. Keeping the rule names and changing only the severity says the change best: the findings, their sources and the forms they match stay as they were, so a later decision can move a severity back without touching the matching. The figure rules are the only code that compares the checked text with the record's own figures (`Check.numbers`, which calls `classify` and `split_match` with the record's cost and record pools), and the wall and the exclusions reach their own hits before or apart from those pools, so the change is confined to four `hit` calls. A34 supersedes "client figures" in A30's list of what stays strict in a client-facing payload; A33's four points stand.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`OWN_FIGURE_EXPECTED`, `Check.classify`, `Check.split_match`, the `cost-cues` comment). *Test:* in `test_leak_lint.py`, `A34Test`: `test_A34_R70_a_client_figure_of_100_or_more_warns_in_every_form_in_a_payload_a_blueprint_and_a_scan` (4,500 in eight forms and 157 beside a rate suffix, a currency sign and a cost word, each exit 2 with the rule and its severity shown, in a payload, a blueprint and a scan, and 4500 as a JSON number), `test_A34_R70_a_figure_split_in_a_payload_and_in_a_scanned_summary_warns` (spaced, across a line break, across table cells, with a full stop, and in a strand summary), `test_A34_R70_a_cost_percentage_warns_in_a_payload_a_blueprint_and_a_scan` (31% and "31 per cent"), `test_A34_R70_an_item_batch_warns_on_a_client_figure_and_on_no_other_number`, `test_A34_R70_an_exclusion_figure_still_blocks_at_any_value` (47,500 in four forms and an exclusion figure of 64, in a payload, a blueprint, a scan and an item batch) and `test_A34_R70_a_payload_with_an_own_figure_and_a_real_block_still_exits_1`; in `test_leak_wall.py`, `A34Test.test_A34_R70_another_clients_figure_on_the_wall_still_blocks_beside_an_own_figure_that_warns` (record a's 73,000 warns while record b's 186,730 blocks on the wall in four forms, in a payload, a scan, an item batch and a blueprint; and the other way round from record b). Against the lint as it was, six of the seven failed and the exclusion control passed. Updated, each with an `# A34 (R70)` comment where its expectation changed: in `test_leak_lint.py`, `test_L78_X11_figures_from_calls_research_and_client_documents`, `test_L79_to_L84_five_formats_against_five_record_formats`, `test_X25_rounded_and_truncated_forms_within_precision`, `test_L85_L86_X25_floors_and_warnings`, `test_X25_ambiguous_lower_case_m_is_read_both_ways`, `test_L105_L106_split_renderings`, `test_X25_figures_in_links_block_and_warnings_skip_links`, `test_L104_R64_the_split_figure_assertion_runs_in_payloads_too` (an exclusion figure in split form now shows the block), `test_L114_to_L118_L264_Y06_rows_that_may_not_clear_leave_the_block_and_warn`, `test_L124_to_L128_X35_docx_parts`, `test_F01_X25_a_figure_after_a_sign_a_dash_a_slash_or_a_quote_is_a_number`, `test_F05_X24_X28_html_entities_and_tags_never_break_a_match`, `test_F12_X28_invisible_characters_look_alikes_and_line_separators`, `test_F22_X25_a_figure_split_at_its_thousands_comma`, `test_F25_R64_a_full_stop_after_an_abbreviation_ends_no_sentence`, `test_A33_R67_numbers_below_100_in_digits_or_words_never_match_nor_warn`, `test_A33_R67_a_client_figure_of_100_or_more_still_blocks_in_every_form`, `test_A33_R68_the_blueprint_keeps_the_firm_markers_credentials_ids_and_record_paths` and `test_A33_R69_every_other_rule_still_runs_on_an_item_batch`, with a helper `Base.assertOwnFigure`; where a test proved that a part or a shape is read at all (the .docx footnotes, an HTML entity, a line separator), it now plants the exclusion figure 47,500, which blocks, and shows the client's own figure warning beside it; in `test_leak_wall.py`, `test_G21_R56_X25_a_cost_figure_in_a_table_of_this_records_own_files_meets_the_figure_rule`; in `test_leak_grading.py`, the outcome counts. *Fixture:* eighteen planted cases expected the old reading. Nine whose only block was the client's own figure now warn, exit 2, outcome `warns` (K01-p, K05-p, K06-p, K07-p, K09-p, K26a-p, R01-p, R02-p, D06-p); seven keep another block and expect the figure as a warning (T09-p, R18-p, R22-p, P-board-p, P-project-p, P-agent-p, P-generic-p; R18-p's summary now says its figure row has nothing to clear); and K04-p and K23a-p, whose payloads also repeat a run of the brief, keep exit 1 from that copied run, which blocked beside the figure all along and is now named in their `expect` and `rules`. K02-p's limit text now says a rate of 100 or more warns. The counts become 97 blocks, 10 warns, 1 caution, 16 limits and 124 passes (106 and 1 before). Nothing under `tests/fixtures/` or `shared/` is edited here: `a34-fixture.patch` (manifest and README) and `a34-shared.patch` (`shared/safety.md`: the client's own figures move from what the lint blocks to its warnings, the exclusions and other clients' figures are named among the blocks, and the split-figure assertion warns for an own figure; no word new to `shared/`, so `shared-words` is unchanged) are in this folder, and `git apply --check` takes both from the plugin repository's root. *Answers R69's nod:* the cost-figure block on sample rows becomes a warning, as A34 says.
*Nod:* a cost percentage warns at any value, 31% included. A34's "a figure of 100 or more" is read as A33's floor, which never applied to percentages; reading it as covering percentages would leave every real cost percentage blocking, since they are almost all below 100.
*Nod:* "a figure split across fields" is read as the split forms the lint reads today: across the cells of a table row, a space, a full stop, a line break or an HTML tag. A figure split over two separate payload strings (`{"name": "Overtime 4", "description": "500 a month"}`) is not read as a figure today, before or after A34, since the joined text of G19 runs only the run, quote and wall rules; it raises a number warning at most.
*Nod:* an allowlist row that names a client's own figure no longer meets a block, so it adds no allowlist warning (R18-p's row for 73,000); the figure's own warning still shows.

*Gates for R70* (the plugin repository on Windows, `PYTHONDONTWRITEBYTECODE=1`): in a scratch copy of the repository with `a34-fixture.patch` and `a34-shared.patch` applied, the whole suite passes under `py -3.9` (3.9) and `py -3.14` (3.14), 655 tests each with 8 skips on this machine (648 before, plus 6 in `test_leak_lint.py` and 1 in `test_leak_wall.py`), and `tools/lint_plugin.py --root .` gives 0 errors and the one known personal-names warning. In the real repository, without the patches, the four leak test files run 302 tests under 3.9 with 6 skips, and three tests fail only because the manifest is not patched yet: `test_leak_grading.py`'s `test_every_case` (the eighteen cases above) and `test_manifest_counts_and_twins` (the new counts), and `test_leak_wall.py`'s `test_L133_to_L161_X14_every_kind_is_walked_family_by_family`, which reads the four `P-` cases' expectations from the manifest. No `__pycache__` is left in either tree.
*Answers:* A34, the user, 2026-10-22

## Added by A36, 2026-10-22

The user decided A36 on 2026-10-22, shown the four blocks of demo 2, none a leak (`build/demos/demo2-log.md`, the table "Every lint block and warning in demo 2" and findings 1, 2 and 14): "yes do all 3 and the batch". These entries build its three loosenings, in R70's shape, and a gap the main session found in the same file (R74). Nothing else is loosened: the wall on other clients' names, terms and figures, the firm in every form, the exclusions, markers, credentials, internal ids, record paths and the payload check at every write stand.

### R71 A test workspace the user named, held as a referenced row in an own-account record, is not one of that record's names

**Decision.** The index stops harvesting the name of every workspace the record's ledger holds as a referenced row, when the record is built in the user's own account (`referenced_workspaces`): an `objects` row of any strand's `solution/build.json` with `type` `workspace` and `origin` `pre-existing-referenced`, in a record whose `CLIENT.md` `build_target` is `own-account`. Before the harvest, every occurrence of such a name in the record's D texts, in any letter case and with any spacing or marks between its words, is replaced by a line break (`unnamed`), so neither the name nor any run of its words is published, and its words leave the single words `index` shows. The rule reads the ledger, never a fixed name, so the CRM test workspace to come is covered as the first two are. Unchanged: the client's name, slug and former names (X26 step 1); the same words written anywhere else in the record, so another name that shares a word with the workspace's is still harvested; a workspace the ledger holds as `created`; a referenced workspace in a client-account record, which is the client's own and stays on the wall; and every other list of the entry.

**Reason.** A36 (a): "the cross-client index stops publishing the name of a test workspace the user named for development builds, and the words of that name". Demo 2's blueprint met the wall twice on "test workspace" because demo 1's element-key table plans `W1` under the test workspace's name, and the index published it as demo 1's (finding 1). The ledger is the one place that says, in fields, that a workspace exists, is never written and is only built into: account-build approves `W1` with `--referenced` (`ledger.py`'s `pre-existing-referenced`), and demo 1's and demo 2's records both hold their `W1` that way. `build_target` keeps the rule to the user's own account, where a workspace is the user's and never a client's; in a client's account a referenced workspace may carry the client's name. Masking the name where it is written, rather than dropping its words from the harvest, is the narrower cut: a client's word that happens to sit in the workspace's name is still published wherever the client writes it.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`REFERENCED_ORIGIN`, `referenced_workspaces`, `unnamed`, `build_entry`). *Test:* in `test_leak_wall.py`, `A36Test`: `test_A36_R71_a_named_test_workspace_and_its_words_leave_the_index` (record b made an own-account demo whose blueprint plans `W1` as "Copperlane Test Workspace", then "Saltry CRM Test Workspace", with the ledger row referenced; its entry holds neither name, fused or spaced, nor "test workspace" nor the first word, still holds "marlbeck freight", and record a's payload and blueprint that say "the test workspace the user named" and the full name meet no wall), failing before the change; `test_A36_R71_the_other_clients_names_and_an_unreferenced_workspace_still_block` (record b's own name, and "Copperlane Haulage" from its research, still wall; a workspace held as `created`, and a referenced one in a client-account record, still wall), passing before and after, as controls should. *Demo:* not re-run against the demo records, since `index` writes the home's index; demo 1's record holds its test workspace as a referenced row with `build_target` `own-account`, so its next index drops the name.
*Nod:* the ledger is not among the files whose times make an entry older (R44 walks text files only), so a record whose ledger gains its referenced row keeps publishing the name until its next index, which a change to any of its text files forces. Before its build's approval a new demo's entry still publishes the name, so two demos designed side by side would meet it as demo 2 did. Taking the plan's `W1` row from the blueprint instead would cover that time, but the blueprint does not say in a field whether a workspace is referenced or created.
*Nod:* a referenced workspace counts only where `build_target` is `own-account`; a `sandbox` record (`build_target` `none`) keeps its workspace names on the wall.

### R72 The firm's sound-alike rule spares a phrase made only of ordinary words

**Decision.** In `Check.phonetic`, a near sound of a source of class `firm` (the firm's name and renderings from the settings, and any `phonetic:` row of class `firm` in a list) is not reported when every word of the matched window is ordinary (`ordinary`: a common word, a stop word, or the plural of a common word) and its letters are not the firm's own letters. So "real names" and "call more" pass. Unchanged: the firm's name and renderings in every written form (the literal rule: letter case, spaced, fused, tokenised, as a domain), a near sound with any word outside the ordinary words ("Kwellmoor", "Quelmore", "call Moore"), the firm's own letters written apart, the whitelist, and every phonetic source of another class.

**Reason.** A36 (b): "the phonetic rule that backs the firm name stops firing on everyday phrases ... the firm name and its renderings in every written form still block". Demo 2's "real names" took one phonetic key with a rendering of the firm term (finding 2). The rule exists to catch the firm's name misheard or misspelt in a transcript or a document, which leaves at least one word that is no ordinary word; two ordinary words that sound like it are prose. The words are judged by the lint's own common-word list, so the rule needs no list of phrases and no whitelist row per phrase. The literal rule is untouched, so every written form of the name and renderings still blocks, whatever words it is made of.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`ordinary`, `Check.phonetic`). *Test:* in `test_leak_lint.py`, `A36Test`: `test_A36_R72_a_near_sound_of_the_firm_made_of_ordinary_words_passes` ("call more", which keys as the test firm "Quellmoor" does, in a scan and a payload, in three letter cases), failing before the change; `test_A36_R72_the_firm_in_every_form_and_a_near_sound_that_is_no_ordinary_word_still_block` (the name, a rendering, the domain, upper case, spaced, two misspellings and "call Moore", each in a scan and a payload), passing before and after. *Nod:* only the firm's sources are narrowed, since A36 names the firm; a local `phonetic:` row of another class keeps firing on ordinary words, and its whitelist rows serve it as before.
*Nod:* "ordinary" is the lint's common-word list with the stop words and plurals. The decision's other example, "only a capitalised one", is not taken, because a misspelt firm name in a lower-case transcript line would then pass.

### R73 A payload's run that the frozen revision plans as a value is not copied from that strand's blueprint

**Decision.** In `payload`, a run of six words, or a near copy of seven or eight (F14), is not looked up in the blueprint files of the payload's own strand (the working `solution/blueprint.md` and its `versions/` copies) when the same run is a planned value of the strand's frozen revision (`frozen_plan`, `Plan`, `planned_streams`). The frozen revision is the one the build writes from: `STRAND.md`'s `version`, that version's `version.md` `revision`, and `versions/<version>/blueprint-r<revision>.md`. Its planned values are its client-facing lines (sections 1 to 15, the prompt blocks and the glossary), section 16's sample data plan (a subsection whose title holds the word "sample", or a line that opens with it, A28) and each `name` cell of the element-key table. A checked window one word away from a planned value counts as planned too, so a column's title written beside its labels does not bring the block back. Unchanged: the rest of section 16 (assumption ids, assumed terms, forks, build checks) and the table's key and kind cells, which still count; every other internal source, such as `readiness.md` or a call, which still blocks the same run; a strand with no frozen revision, or one whose revision planned other values; the quote rule; `scan` of a `.json` file; and `blueprint`, which has no run rule since R68.

**Reason.** A36 (c): "a run of words in a payload that matches the frozen revision's own planned value for that element (a label list, a view's name, a column's values) is not a copied run". Demo 2's B3.C2 labels, five invented cities in the revision's order, matched six words of section 16's sample data plan in the working blueprint (finding 14): the source was the blueprint itself, and the build was writing what the user approved. The frozen revision is the approved text, so a run that matches it is the plan, not a leak; the working blueprint alone may have changed since the freeze, so it is not enough. Only the blueprint as a source is narrowed, since A36 keeps the internal sections that hold ids, keys and assumptions: a run copied from them, or from any other internal file, still blocks.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`ELEMENT_KEYS`, `Plan`, `planned_streams`, `frozen_plan`, `Run.plans`, `Check.runs_and_quotes`, `Check.near_windows`). *Test:* in `test_leak_lint.py`, `A36Test`: `test_A36_R73_planned_labels_and_a_planned_view_name_pass_a_payload` (five invented towns planned in section 16's sample data plan, as a dropdown's labels inside a settings string beside the column's title and as a plain list, and an eight-word view name from the element-key table, each exit 0), failing before the change; `test_A36_R73_an_internal_run_another_source_and_an_unfrozen_plan_still_block` (a run of a section 16 assumption blocks from the blueprint; the towns copied into `readiness.md` block with that file as the source; with no frozen revision, or a revision that planned another town, the labels block), passing before and after. *Touch-up, for the main session:* the solution-blueprint skill could pin the sample data subsection's title (`### Sample data plan`), which the lint finds by the word "sample". *Nod:* the lint does not know which element a payload writes, so a run that matches any planned value of the frozen revision passes, not only that element's; the payload command has no flag that names the element.
*Nod:* a run that the revision plans and that another internal file also holds still blocks from that file; the decision names the planned value, and the other file is a source A36 does not narrow.

### R74 A row inside an HTML comment is not an exclusion or allowlist row

**Decision.** `section_rows` skips every line inside an HTML comment under `## Exclusions` and `## Allowlist`, a comment on one line or over several, as `strict_rows` already did, so an example row in a comment is never read as a live exclusion or allowlist row. A row after the comment is read as before.

**Reason.** The main session found that `strict_rows` let a comment pass the exclusions' fail-closed check while `section_rows` still read the `- ` lines inside it, so an example row in a template's comment became a live exclusion, and in an allowlist would clear a term; the two readers now agree. The main session changed `templates/record/exclusions.md` to an exact `## Exclusions` heading with a comment that holds no `- ` line; it is not touched here.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`section_rows`). *Test:* in `test_leak_lint.py`, `A36Test.test_A36_R74_a_commented_example_row_is_not_read_and_a_real_row_after_it_is` (a single-line comment, a comment over four lines and one whose last line is a row, under both headings, give only the real row after them; in the strand's exclusions, the commented names and figure meet no exclusion in a payload while the real rows block), failing before the change.

*Gates for R71 to R74* (the plugin repository on Windows, `PYTHONDONTWRITEBYTECODE=1`): in the real repository the four leak test files run 309 tests under `py -3.9` (3.9) and `py -3.14` (3.14), 6 skips each and no failure (302 before, plus 5 in `test_leak_lint.py` and 2 in `test_leak_wall.py`); against the lint as it was, the three tests of the loosenings and R74's test failed and the three controls passed. No existing test changed its expectation and the trap fixture is unchanged, so there is no fixture patch. `a36-shared.patch` (this folder) adds the three loosenings to `shared/safety.md` in words already in `shared/` (`shared-words` and `shared-phrases` unchanged); `git apply --check` takes it from the plugin repository's root, and in a scratch copy with it applied the four leak files pass under 3.9, 309 tests. `tools/lint_plugin.py --root .` gives 0 errors and the one known personal-names warning in both trees. No `__pycache__` is left.
*Answers:* A36, the user, 2026-10-22

## Added by A39, 2026-10-22

The user decided A39 on 2026-10-22, shown demo 3's lint blocks and warnings, none a leak, and three candidates to loosen (`build/demos/demo3-log.md`, the table "Every lint block and warning in demo 3" and the paragraph after it): "I agree with the rules to loosen for the lint." These entries build the three loosenings, in R71's shape. Nothing else is loosened: the firm name in every form, the exclusions, the wall on other clients' real names, terms and figures, markers, credentials, internal ids written as text, record paths and the payload check at every write stand.

### R75 A phone column's value in a payload's column values is not an id

**Decision.** In `payload_units`, a string is marked phone (`Unit.phone`) when it sits inside a `column_values` or `columnValues` map (`COLUMN_VALUES`, read without underscores or case, as an object or a string of JSON), under a key that names a phone column (`PHONE_COLUMN`: `phone`, `lead_phone`, `contact_phone`, `phone_<suffix>`, `phone4`), and has one of the two shapes monday takes for a phone column: the digits, with an optional leading plus and at most fifteen of them, and optionally a space and a two-letter country code (`4195550123 US`, `PHONE_TEXT`); or the `phone` of an object that holds only `phone` and a two-letter `countryShortName` (`phone_object`), that object also allowed as a string of JSON. The walk carries each value's place (`child_place`), and a string holding JSON passes its place to the JSON inside it, so an item batch's `columnValues` string is read the same way. `Check.regex_rows` skips the id row for a phone unit, as it does for a structural id. Unchanged: the same digits in a name, a description, a label, an update or a text column; digits under a phone column that are not a phone's shape (a sentence, a three-letter code, an object with another key beside them); a phone shape outside a column-values map; a JSON number under a phone column; the user's own account ids, which still block there as `seller-account` (X06); the split-id rule; and the numbers, the exclusions, the wall and every other rule on the phone's string.

**Reason.** A39 (d): "a value under a phone column (digits only, often eight or more) no longer meets the id-pattern rule; a run of digits written into a name, a description, a label or a message still does." Demo 3's build met the id row on every lead's and contact's phone, and the build left the phones empty to get past it (`demo3-build-notes.md`, note 5). The narrowest sound signal is the place and the shape together. The column id alone would spare whatever a payload writes under it, a sentence with an id in it included, and the shape alone would spare an object of digits anywhere in a payload. Inside a column-values map the key is a column id, which monday makes from the column's type (`phone_mm8k2q4z`) or the native template fixes (`lead_phone`, `contact_phone`, `phone`); the shape then says the value is a number to dial and nothing else. The user's own account ids stay blocking because they are the leak X06 names, whatever field holds them.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`COLUMN_VALUES`, `PHONE_COLUMN`, `PHONE_DIGITS`, `PHONE_TEXT`, `COUNTRY_CODE`, `child_place`, `phone_object`, `payload_units`, `Unit.phone`, `Check.regex_rows`). *Test:* in `test_leak_lint.py`, `A39Test`: `test_A39_R75_a_phone_columns_value_in_column_values_passes` (four phone columns in both shapes, in an item batch's `column_values` string, a create-item `column_values` object and a `columnValues` string holding a phone object as JSON, each exit 0 with no finding; and beside a phone that passes, an id in a long-text column still blocks, at that field only), failing before the change; `test_A39_R75_digits_written_as_text_or_outside_a_phone_columns_value_still_block` (the digits in an item name, in a text column, in a sentence under a phone column, beside a three-letter code, in a phone object with a note beside it, in a phone object outside column values, under a column named `phonetic_notes`, and written in groups in a description each block on the id row; the user's own account id as a phone value blocks as `seller-account`), passing before and after, as controls should. *Demo:* demo 3's lead batch, given a 555 phone on each of its fifteen rows, gave 15 id-pattern blocks against the scratch home before the change and exit 0 after.
*Nod:* a phone column whose id the build sets without the word phone keeps the block, the fail-safe side; monday's own ids for phone columns all carry it.
*Nod:* a phone number written with spaces, brackets or dashes (`+1 (419) 555-0123`) still meets the split-id rule, since monday stores the digits only and the build need not send it formatted; and a JSON number under a phone column still meets the id row, since monday takes a phone as a string.
*Nod:* any digits of phone shape under a phone column pass the id row, so an internal id written there would pass it too; the user's own account ids, the exclusions and the wall still block it there, and the id row still reads every other column.

### R76 The index publishes names, not the ordinary words, codes and short generic phrases a record capitalises

**Decision.** Three changes to what an entry publishes, and one to the phrases the plugin writes. First, `harvest` takes `entry`, which `build_entry` passes: a run of two or more words that starts or ends with a function word (`FUNCTION_WORDS`, `edge_word`: articles, pronouns, conjunctions, prepositions, the forms of be, do and have, the contractions as the tokeniser writes them, and greetings and answers), unless that word is written in capitals as an acronym (`US`, `IT`, `OR`), is not a candidate; its sub-runs still are. Second, after R47's lower-case filter, `build_entry` drops every candidate that `generic` names: a code, one to three letters and then one to four digits (`CODE_WORD`: `P2`, `C10`, `AS1`, `A37`), or a run that holds one; a single word of `EVERYDAY_WORDS` (compass and time-zone words, number words, month abbreviations, holidays, the words of a transcript's header and speaker labels, and conversational words such as `understood`, `officially`, `yeah` and `bye`), or its plural; and a run whose every word is an everyday one (a common word, a stop or `shared/` word, a word of `EVERYDAY_WORDS`, a joiner, or an inflected form of one) and that holds a word of `GENERIC_WORDS`, the titles, acronyms, days and months of X26 step 6 (`Account ID`, `Meeting ID`, `Try the CRM`). Third, `shared_phrases()` also takes a capitalised run whose words are common words beside at least one stop word, and `SHARED_PHRASES` is regenerated (101 phrases, 70 before), so a phrase the plugin writes, such as monday's `Quotes & Invoices`, is no client's name under G04. Unchanged: X26 step 1's forms (the `CLIENT.md` name, the former names and the slug), which are always published; `kept`, the slugs of other folders (X21), O, `wall/1` and the checked side; `clients-index/1`; and every run of common or `shared/` words alone, such as `Blue Harbour`, `Signal Path` or `Cold Store`, which stays a name (G04).

**Reason.** A39 (e): "the cross-client index stops publishing ordinary words, lower-case tokens and short generic phrases as a client's names ... so the wall blocks another client's real names and terms and not the everyday words a record happens to capitalise." Demo 3's blueprint met the wall on `Central`, "and the CRM's" and "the installed", and the main session's `terms` run over `shared/` met `account_id`, `P-2` and "an AI", each published by another demo record. Each has a cause the harvest can tell without a dictionary. A run that begins or ends with a function word is a sentence's words around a name, and X26 step 2 already makes every sub-run a candidate, so the name inside ("So Tallowmere") stays published and the checked side still meets it. A key or a code is the record's own reference to its plan, never a client's name. A run of everyday words that holds an acronym or a title is a label (`Account ID`), and a name-like part of it is a sub-run of its own. `Central` is a time zone, which no rule of the harvest can tell from a name, so a short list of word families serves; it holds only words that name nothing on their own. `GENERIC_WORDS` leaves out monday's product words and the shipped rows' words, because firms name themselves with work, service or management and a method row holds everyday words (`store`, of `claims store`), and G04 keeps a name of two everyday or `shared/` words published: with those words as the trigger, `Cold Store` left the trap fixture's record and G04's own test failed. `Quotes & Invoices` is monday's native board name, which `shared/native-objects.md` writes; G04's phrase list missed it only because `quotes` is a common word. `desc` needed nothing: it has been a `shared/` word since the gotcha on sort directions.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`FUNCTION_WORDS`, `CODE_WORD`, `GENERIC_WORDS`, `EVERYDAY_WORDS`, `edge_word`, `harvest`, `generic`, `build_entry`, `shared_phrases`, the `shared-phrases` region and its comment). *Test:* in `test_leak_wall.py`, `A39Test`: `test_A39_R76_ordinary_words_codes_and_generic_phrases_leave_the_index` (record b's note writes demo 3's shapes: `14:02 Central`, "And the CRM's", "The Installed", "An AI", "Account ID:", `P2`, "C10 and B4", "Officially" and "Quotes & Invoices"; none is in its entry, spaced or fused, nor among its single words, while `marlbeck freight` and `dockon` are; from record a, a payload, a draft and `wall` holding "Central", "and the CRM's", "the installed", `account_id`, `quotes_invoices` and "an AI" meet no wall, `wall` on "Pain P-2 and column C10." meets none, `terms` over a folder holding both texts exits 0, and the same `P-2` in a payload still blocks on the id row), failing before the change; `test_A39_R76_another_clients_names_terms_and_figures_still_block` (record b writes "So Tallowmere", "And Brindmoor Tackle", `Ysenne Corvath`, "Hollin CRM" and "the Account Halvery"; from record a, `Tallowmere`, `Brindmoor Tackle`, `Ysenne Corvath`, `Ysenne`, `Hollin`, `Silver Lantern`, `Account Halvery`, `Marlbeck Freight`, `Dockon`, `TFM` and `Wendell Ayo` block as names in a payload and in `wall`, the cold-chain surcharge as a term and 186,730 as a figure), passing before and after. G04's `test_G04_U1_X26_...` and `test_G04_Z12_...` pass unchanged. *Measured:* on a scratch copy of the development home's `clients/` and `local/`, the three demo records published 87, 108 and 125 single words before and 39, 47 and 70 after, and 90, 110 and 111 runs before and 54, 38 and 61 after; nothing is published after that was not before, and every word dropped is a code or an everyday word (`central`, `eastern`, `north`, `understood`, `thanksgiving` and the like). `terms` over `shared/` against that home went from exit 1 with 39 wall blocks to exit 0. The trap fixture's records publish the same single words (19 and 21); `wrenfold-joinery`'s entry loses `Meeting ID`, spaced and fused, `marlbeck-freight`'s is unchanged, and no planted case changes its outcome. The words, before and after, are in the session's scratch folder, `a39/index-before-after.md`. *For the main session:* re-index the development home's records, since an entry changes only at its next `index`.
*Nod:* `EVERYDAY_WORDS` is a list of word families, not a dictionary, so an everyday word outside it that a record capitalises and never writes in lower case is still published alone (`plastics`, `welding`, `ridge`, `feedback`), the fail-safe side. A word in it is never published alone, so a one-word name that is such a word (a firm called Central) blocks only through its runs and its own record's X26 step 1 forms.
*Nod:* the word for the person who runs a call, which the demo transcripts use as a speaker label, cannot be put in the list, since `tools/lint_plugin.py` keeps that word out of every shipped file. It stays published as a single word wherever a transcript capitalises it; a transcript that labels that speaker another way avoids it.
*Nod:* a name that begins or ends with a function word (`The Hague`) publishes only its inside (`Hague`), which the checked side still meets, and a product code of the code shape (`A4`, `U2`) is not published, alone or in a run.
*Nod:* a run of everyday and `shared/` words with no title, acronym, day or month in it (`Accounts and Contacts`, `Region West`, `Health and Safety`) is still published, since G04 keeps such a run as a possible name; the demo records publish a few. The widened phrase list holds 31 more of the plugin's own phrases (`Microsoft Teams`, `Template Center`, `Web Form` and others), so a client's run equal to one of them is not published.

### R77 A label's colour, index or position in a column's settings is not a record number

**Decision.** In `payload_units`, a JSON integer or a digit-only string under `color`, `index` or `position` (`LABEL_NUMBER_KEYS`) of a label in the `labels` list (`LABEL_LISTS`) of a column's settings (`SETTINGS_KEYS`: `columnSettings`, `settings`, `settings_str` or `defaults`, read without underscores or case, as an object or a string of JSON, nested settings included) is marked label (`Unit.label`), and so is the raw string of such settings written as JSON, whose values the walk reads one by one. A label unit's numbers raise no `record-number` and no `number` warning (`Check.classify`'s `quiet`, `Check.split_match`), as a sample row's do. Unchanged: the label's own text ("153 crates" still warns); a colour outside a label list or outside a column's settings; the exclusions at any value, which block on a colour as anywhere; the client's cost figures, which warn; the id row on a JSON number; and every rule on every other value.

**Reason.** A39 (f): "the numbers inside a status or dropdown column's settings (label colours, indexes) raise no record-number warning." Demo 3's status columns warned on each colour that matched a number in the transcript (colours of 108 and over in `columnSettings.labels`); a colour is monday's number, never the client's. The place is the signal: a settings key, its label list and the three keys that hold monday's numbers, so a number that a label's text carries is still read as before. The raw JSON string stays quiet because the values inside it are each walked, and a label's text there still warns.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`SETTINGS_KEYS`, `LABEL_LISTS`, `LABEL_NUMBER_KEYS`, `child_place`, `payload_units`, `Unit.label`, `Check.classify`, `Check.split_match`). *Test:* in `test_leak_lint.py`, `A39Test`: `test_A39_R77_label_colours_and_indexes_in_a_columns_settings_raise_no_number_warning` (the record holds 153 and 108; a status column's labels with those colours and indexes and a colour as a string, as a `columnSettings` object, a `columnSettings` string and a `settings_str` string, and a dropdown's `defaults` string with `settings.labels` and a position, each exit 0 with no finding), failing before the change; `test_A39_R77_a_number_in_a_label_or_outside_the_labels_still_warns_and_an_exclusion_or_an_id_blocks` (a label's text "153 crates", a colour on a board, a colour beside the label list in the settings and a `labels` object in column values each warn as `record-number`; the exclusion figure 47,500 as a colour, as a number and as a string, blocks, and an id-shaped colour blocks on the id row), passing before and after. *Demo:* demo 3's 54 payloads against the scratch home went from 7 with warnings (11 `record-number` and 32 own-figure warnings) to 2 (A34's 32 own-figure warnings on its sample deal values); none blocked before or after.
*Nod:* the plain `number` warning is quiet on a label colour too, not only `record-number`: a colour that matches no record number is no number for the client either, and A33's sample rows quiet the same pair.
*Nod:* monday's older settings maps (`labels_colors`, `labels_positions_v2`) are not read as label numbers, so a number in them still warns; their colours are hex strings, and demo 3 used the label list.

*Gates for R75 to R77* (the plugin repository on Windows, `PYTHONDONTWRITEBYTECODE=1`): in the real repository the four leak test files run 315 tests under `py -3.9` (3.9.13) and `py -3.14` (3.14.5), 6 skips each and no failure (309 before, plus 4 in `test_leak_lint.py` and 2 in `test_leak_wall.py`); against the lint as it was, the three tests of the loosenings failed and the three controls passed. No existing test changed its expectation and the trap fixture is unchanged, so there is no fixture patch. `a39-shared.patch` (this folder) adds the three loosenings to `shared/safety.md` in words already in `shared/` (`shared-words` and `shared-phrases` unchanged by it); `git apply --check` takes it from the plugin repository's root, and in a scratch copy with it applied the four leak files pass under 3.9, 315 tests. `tools/lint_plugin.py --root .` gives 0 errors and the one known personal-names warning in both trees. No `__pycache__` is left.
*Answers:* A39, the user, 2026-10-22

## Added by the intake fold, 2026-10-22

Demo 3's intake fold (`build/demos/demo3-intake-fold.md`, point 17, "Not the skills'") found that a bare `leak_lint.py scan --strand <id>`, with no path, answered `could-not-run` in words that read as a fault of the lint. No decision of the user's changes; the entry below is a wording fix inside R22's existing exit.

### R78 A scan with no path and no draft says that no draft exists

**Decision.** In `cmd_scan`, when no path is given and no draft or handoff file is found, the stop is still exit 3 (R22, F23: a scan that judged nothing never reads as clean), but its error now names the case. With `--strand`, the error's file is that strand's `drafts/` folder (`strands/<NNN-name>/drafts/`), its problem is "no draft exists for strand NNN: its drafts/ and deliverables/handoff/ hold no file", and its expected says to pass the path of the file to check after `scan`. Without `--strand`, the file is `strands/` and the problem says no strand's `drafts/` or `deliverables/handoff/` holds a file. A path that is given and holds no file keeps R22's "no draft or handoff file to check", now naming the path given. The exit code, the verdict and the envelope are unchanged.

**Reason.** The old message named `strands/` and "no draft or handoff file to check", which a caller read as the lint failing to run. The case is a plain answer: the skill asked for a check and there is nothing yet to check. The exit stays 3 because a check that read no file must not look clean or blocked.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`cmd_scan`). *Test:* in `test_leak_lint.py`, `IntakeFoldTest`: `test_17_a_bare_strand_scan_with_no_draft_says_no_draft_exists` (exit 3, verdict `could-not-run`, the strand's `drafts/` as the file, the problem naming strand 001, no inputs), failing before the change; `test_17_a_bare_scan_with_no_draft_anywhere_says_so_without_a_strand` (the no-strand wording, exit 3), failing before; `test_17_a_scan_with_a_real_path_or_a_draft_to_find_behaves_as_before` (a path scans clean, a bare scan finds that draft once it exists, and an empty given folder keeps R22's message), passing before and after, as a control. *Demo:* the scratch record's `scan --strand 001`, with no draft, gave exit 3 and "no draft or handoff file to check" under `strands/` before the change, and exit 3 with "no draft exists for strand 001" under that strand's `drafts/` after.
*Nod:* a skill that treats exit 3 from a bare scan as a stop still stops; it can now tell from the problem that the cause is a missing draft and not a lint fault.
*Answers:* the intake fold, 2026-10-22

## Added by A42, 2026-10-23

The user decided A42 on 2026-10-23, shown demo 4's blueprint agent's notes 7 and 9 (`build/demos/demo4-skill-notes.md`) and the main session's reproduction of both lint refusals: "Check decoded text" for the line breaks, and "Loosen the lint" for element keys. Built by the main session in the same sitting, in R75's shape. Nothing else is loosened: the firm name in every form, the exclusions, the wall, markers, credentials, internal ids written as text, record paths, qualified element keys and pain ids written alone stand.

### R79 A payload value that holds JSON is read with its escapes decoded

**Decision.** In `payload_units`, when a payload string parses as JSON (an object, a list, or a string, R34), the unit's own text becomes `json_decoded` of the parsed value: the JSON written again with every key and string as it is, not escaped, and JSON held in a string inside it rendered the same way, up to three levels; `line_starts` follows. The decoded values are still walked one by one as before (X22, F26, R34), so the raw unit's change touches only what the raw string alone could show: a pattern across two values, which still meets it, and the escape artefacts, which no longer do.

**Reason.** A42: "Check decoded text". Demo 4's blueprint agent staged a visit log written over two lines, and the pain-id row `\bN\d{1,2}\b`, matched without regard to case, met `n15` in the raw string's `\n15`; the same text as an object, or on one line, passed (reproduced by the main session). Every term row read the raw escapes the same way (`\t`, `é`). Decoding the raw string keeps the patterns that span two values, which skipping it would have lost; decoding it by its own literals cannot work on JSON held in a string, whose quotes no longer pair once the outer layer is decoded, so the text is rendered from the parsed value.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`json_decoded`, `payload_units`). *Test:* in `test_leak_lint.py`, `A42Test`: `test_A42_R79_an_escaped_line_break_before_a_date_is_not_a_pain_id` (a two-line visit log in an item batch's `column_values` string, the same JSON held in a string inside a string, and a text column's line break before a number, each exit 0 with no finding; an escaped tab before a real `S1` still meets it, in the decoded raw string and in the value); its first case is the refusal the main session reproduced against the old lint; `test_A42_R79_a_pain_id_inside_json_still_blocks_in_the_value_and_the_decoded_string` (a `P3` after a line break blocks at the raw field and at the value), a control.
*Nod:* the raw string's text is now the decoded rendering, so a finding on it quotes the decoded text; its field is unchanged.

### R80 The column part of an element key is not a pain id

**Decision.** In `Check.regex_rows`, a match of a `pain-ids` row is skipped when the text right before it is the head of an element key (`ELEMENT_KEY_HEAD`: a board, workspace, folder, doc, dashboard, automation, portfolio, project, UI step, agent, workflow, Vibe app, sequence or webhook letter, one to three digits and a dot, not preceded by a word character or a colon), so `C9` in `B3.C9`, `b3.c7` or `{pulse.B3.C7}` passes. Unchanged: a pain id written alone (`C9`, `P3`), after any other dot (`x.C9`), and a key qualified with its strand (`001:B3.C9`), which the qualified-key row reports whole.

**Reason.** A42: "Loosen the lint". Demo 4's blueprint agent staged its sample-name check under element keys, and the payload lint refused `B1.C4` to `B1.C7` as pain ids; the skill's first custom-prompt placeholder, `{pulse.B3.C7}`, failed the blueprint lint the same way. The main session had recommended a skill fix and no lint change, since an element key never belongs in what monday shows; the user chose the loosening. The narrowest form is the key's own shape: only the part after a key's head is spared, and only for the pain-id class.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`ELEMENT_KEY_HEAD`, `Check.regex_rows`). *Test:* in `test_leak_lint.py`, `A42Test`: `test_A42_R80_an_element_key_in_a_payload_passes` (a key as a JSON key, keys in a list, lower case, and inside a `{pulse.…}` placeholder, each exit 0); the JSON-key case is the refusal reproduced against the old lint; `test_A42_R80_a_pain_id_alone_after_a_dot_or_in_a_qualified_key_still_blocks` (`C9` alone, `001:B3.C9`, `x.C9` and a `P3` beside a key each block), a control.
*Nod:* an element key now passes in any text the lint reads, the blueprint's client-facing sections included; the blueprint skill's rule that sections 1 to 15 carry no element key is what keeps them out there.
*Answers:* A42, the user, 2026-10-23

### R81 In a workflow request, the record's own user and objects pass the id row

**Decision.** `cmd_payload` collects, for a payload of kind `workflow` only, `own_ids`: the bound user id in the record's `account.json` and every numeric id of six digits or more among the strand's `solution/build.json` rows. `Check.id_hit` passes a match of the id row whose digits are one of them. A file that cannot be read gives no ids, so every id blocks as before. Unchanged: every other id in a workflow request, every id in a payload of any other kind, the split-id rule, the user's own account ids (`seller-account`), the exclusions, the wall and every other rule.

**Reason.** A43: the user chose "Lint passes own ids (Recommended)". The workflow expert takes its whole configuration as free text, and without ids it could neither tell the account's three boards of one name apart nor resolve the user as a recipient (`build/demos/demo4-build-notes.md`, notes 11 to 13); the main session's probe had set the recipient by id. The ids the record itself holds are arguments of its own build, as A33's structural keys are; the place (a workflow request) and the source (the record's own ledger and binding) together keep the loosening to that.

**Follow-up.** *Build:* done, `scripts/leak_lint.py` (`own_ids`, `cmd_payload`, `Check.id_hit`). *Test:* in `test_leak_lint.py`, `A43Test`: `test_A43_R81_a_workflow_request_names_its_own_user_and_board_by_id` (a request naming the bound user and the strand's board by id, exit 0 with no finding); `test_A43_R81_another_id_another_kind_or_no_ledger_still_blocks` (another id in a workflow request, the user's id in an automation payload and the board's id in a board name each block on the id row, and with no `account.json` and no ledger the user's id blocks in a workflow request), a control. The blocked request of the demo 4 build is the case reproduced.
*Nod:* any numeric id of the strand's ledger passes, a column's or an item's included where monday's ids are numeric, since the ledger holds only what this strand built or referenced.
*Answers:* A43, the user, 2026-10-23
