# Map of BUILD-PLAN.md for the stage 1b re-cut

This map is the planner's input for re-cutting the build plan. It changes nothing that exists. Lines are cited as `L123` or `L120–L140` against BUILD-PLAN.md as it stood on 2026-10-13 (557 lines, no heading moved).

**How to read it.** Tiers are those of A19 and A18: v1-core, v2, v2-or-v3. A package is split when it holds more than one tier. Every tier here is provisional and the planner decides. "Surface-later" is a note, not a tier: it marks material that A20 pushes to the Cowork and Project work after v1. An acceptance item is cited by its ordinal among the dash-bullets of its package (WP1, WP3, WP5, WP9, WP10 and WP13 use bullets) or by its first words where the acceptance is one long paragraph (WP2, WP7, WP8, WP12, WP14, WP18).

**The file changed under this run.** Other processes edited BUILD-PLAN.md while this map was being written. The sentences that carried a GitHub handle (L88 and L520) now say "the user's GitHub account", and a workspace id in L17 became a placeholder. No line moved. Section 7 records those hits as they stood when read.

**Siblings in the same folder.** `build-readiness-spec.md` and `map-architecture.md` appeared during this run. I read the first before writing section 5, kept my own list of acceptance items, and say there where the two differ. I did not read the second.

---

## 1. Inventory

### 1.1 Headings

| Heading | Lines | Gist |
|---|---|---|
| `#` title and preamble | L1–L9 | Revision note (three revisions, last for A16), authority order (amendments over architecture over this file), and the map of sections 0 to 6. |
| `## 0` Three decisions still open (A11) | L11–L37 | A11-1 test account, A11-2 sample data in a live account, A11-3 retention (table L15–L19); two mechanical rules (L23–L24); four calibration questions with shipped defaults, tagged [L14], [L15], [L17], [L18] (table L28–L33); decisions 16 and 19 (L35). |
| `## 1` Order of work | L39–L78 | Stage diagram 0 to 5 (L41–L64); why stage 0 comes first (L66); what stage 1 carries (L68–L70); ordering inside stage 2 (L72); three sequencing defects (L74); four schedule splits (L76). |
| `## 2` Work packages | L80–L310 | Twenty packages, WP-S0 and WP0 to WP18, each with Files, Inputs, Acceptance, Size; size targets are limits (L82). |
| `### WP-S0` Stage-0 probes | L84–L90 | Probe list S0-1 to S0-15 (L88) and a results file; acceptance wants a dated result per probe. |
| `### WP0` Repo skeleton | L92–L98 | Marketplace and plugin manifests, `.gitignore`; `validate --strict`; no `CLAUDE.md`, `.mcp.json`, `commands/`, `bin/`. |
| `### WP1` `shared/` | L100–L119 | Nine shared files; eleven acceptance bullets (L107–L117); about 2,000 lines. |
| `### WP2` `mmb_common.py`, `record.py` | L121–L126 | Record, strands, lease primitives, check, close, migrate; one paragraph (L125); H20 to H22, H27, H35 to H38. |
| `### WP3` `ledger.py`, `gql_guard.py` | L128–L149 | Ledger, epoch fence, estimate, reconcile, compare, classify (33-board and 67-board fixtures); thirteen bullets (L135–L147). |
| `### WP4` `leak_lint.py` | L151–L156 | Figures, copied runs, markers, payload and docx checks, structural assertions, clean twin; one paragraph (L155). |
| `### WP5` Intake scripts | L158–L180 | `transcript_measure.py` and `transcript_prep.py`: measure, prep, identity, type, verify-quotes, delivery, set, document; thirteen bullets (L166–L178). |
| `### WP6` `sop_tools.py` | L182–L187 | SOP render tools: doctor, diagrams, doc-chunks, inputs; goldens; one paragraph (L186). |
| `### WP7` Record templates | L189–L194 | Thirty-nine templates; one paragraph of about 5,000 characters (L193). |
| `### WP8` Method skills | L196–L201 | `engagement`, `call-intake`, `discovery-check`; ten references; one paragraph (L200). |
| `### WP9` monday-write skills | L203–L225 | `solution-blueprint` and `account-build`; fourteen bullets (L210–L223). |
| `### WP10` Audit and drift | L227–L241 | `solution-audit` and `monday-drift-check`; six bullets (L234–L239). |
| `### WP11` Agents | L243–L248 | Four agents: summarizer, auditor, SOP drafter, research scout; one paragraph (L247). |
| `### WP12` Demo, SOP, close-out | L250–L255 | `demo-script`, `client-sop`, `client-closeout`, `archive_check.py`; one paragraph (L254). |
| `### WP13` Hooks, READMEs | L257–L271 | `hooks.json`, `guard.py`, READMEs, MAINTAINING, CHANGELOG; six bullets (L264–L269). |
| `### WP14` Fixtures, graders, runner | L273–L278 | Fixtures copied in, seed records r1 to r13, graders, headless runner; one paragraph (L277). |
| `### WP15` Sandbox scenarios | L280–L285 | T1 to T23, probe catalogue, sealed defect file; one paragraph (L284). |
| `### WP16` Release tooling | L287–L292 | `lint_plugin.py`, `sync_shared.py`, `cleanroom_scan.py`, `release.sh`; one paragraph (L291). |
| `### WP17` `demo_check.py` | L294–L300 | Run-sheet budget and gate checks; why it is its own package (L298); one paragraph (L299). |
| `### WP18` Fixtures s11 to s25 | L302–L308 | Calibration fixtures s11 to s24 and document fixture s25, written in stage 1; one paragraph (L307). |
| `## 3` File ownership | L312–L344 | 115 files, one owner each (L314); ownership table (L316–L334); repo-only files (L336); seven ownership notes in three paragraphs (L338–L342). |
| `## 4` Test plan | L346–L516 | Layers, fixtures, constructed inputs, headless runs, trigger tests, sandbox scenarios. |
| `### 4.1` Layers | L348–L360 | Seven-layer table; one rule with no test on purpose (the chat-boundary nudge, L360). |
| `### 4.2` The fixtures | L362–L406 | Ten reviewed fixtures (table L368–L379); fourteen calibration fixtures (table L383–L398); document fixture s25 (L400); native-board expectations (L402); leak block lists (L404); seed records r1 to r13 and broken records (L406). |
| `### 4.3` What fixtures cannot prove | L408–L421 | Eight behaviours covered by constructed inputs (L412–L419); the multi-call note (L421). |
| `### 4.4` Headless runs | L423–L480 | Runner command and rules (L425); H01 to H56 (L427–L480). |
| `### 4.5` Trigger tests | L482–L484 | About twenty prompts per model-invocable skill; should-not sets; user-only set; bars. |
| `### 4.6` Sandbox scenarios | L486–L514 | Rules for all (L488); T1 to T23 (L490–L514). |
| `## 5` Release checks | L518–L531 | Twelve numbered checks for `tools/release.sh` (separator at L533). |
| `## 6` Conflicts with ARCHITECTURE | L535–L557 | Seventeen rows; the intro says no row is live and most are folded into the architecture (L537). |

### 1.2 Work packages

Stage "as written" comes from the diagram at L41–L64 and the schedule splits at L76. "Depends on" lists what the plan says must exist first; where the plan only names an input I mark it (input).

| WP | Name | Files it owns | Depends on | Stage as written | Provisional tier and reason | v2 and v2-or-v3 acceptance items (split packages) |
|---|---|---|---|---|---|---|
| WP-S0 | Stage-0 Cowork and runtime probes (L84–L90) | `tests/stage0/README.md`, `tests/stage0/results.md` | A§13 and `cowork-capabilities.md` (input, L87) | 0 | v1-core, complete. A20 narrowed it to Code-side probes and all passed (HANDOFF section 7). Five Cowork-only probes (S0-2, S0-3, S0-4, S0-8, S0-10) are not needed. | none |
| WP0 | Repo skeleton and manifests (L92–L98) | `marketplace.json`, `plugin.json`, `.gitignore` | A§2 (input) | 1 | v1-core, complete. Its no-`CLAUDE.md` rule (L96) meets the client-folder question in section 9. | none |
| WP1 | `shared/`: one home per fact (L100–L119) | `shared/record-map.md`, `sales-method.md`, `house-style.md`, `safety.md`, `monday-gotchas.md`, `read-back.md`, `native-objects.md`, `leak-terms.txt`, `sandbox-accounts.txt` | WP18 keys for the pins (L44, L70); WP-S0 results (L42); earlier probe files (input, L103) | 1 | split. Seven files are v1-core. `sales-method.md` and `house-style.md` are v2 (files kept, no skill built, A19). | Bullet 1 "Every R1 to R12 name and every gate name…" (L107). Bullet 8 "`house-style.md` carries the register targets…" (L114). Clauses in v1 bullets: bullet 2 (L108) pins the call-type header, whose pinned vocabulary includes fields only sales uses (`seat`, `relationship`, `money_live`); bullet 3 "`demo-script` reads it at generation" (L109); bullet 7 "the delivery-exposure rules of A§9.11" (L113); bullet 10 "which `demo_check.py gate` reads" (L116). |
| WP2 | `mmb_common.py` and `record.py` (L121–L126) | `scripts/mmb_common.py`, `scripts/record.py`, `tests/unit/test_mmb_common.py`, `test_record.py`, `tests/unit/fixtures/` | WP1 pins (L68); `mmb_common.py` before `ledger.py run start` (L72) | 2; `record.py init` accepted in 3 with WP7 (L52, L76) | v1-core. Record, strands, lease, check and close are the A14 and A15 core. | none. Two fragments to trim: `sop/` in the non-platform check (L125 "or `sop/` under a `non-platform` strand", v2-or-v3), and `migrate` with the `client/1` tree (L123, L125; an earlier schema, see section 9). |
| WP3 | `ledger.py` and `gql_guard.py` (L128–L149) | `scripts/ledger.py`, `scripts/gql_guard.py`, `tests/unit/test_ledger.py`, `test_gql_guard.py`, `tests/fixtures/snapshots/` | WP2 lease primitives (L72); WP1; recorded reads from earlier probe files (input, L131) | 2 | v1-core. Ledger, fence, change check, native map and classify are the build safety layer. It has no row yet for the AI element kinds (A17, A18). | none |
| WP4 | `leak_lint.py` (L151–L156) | `scripts/leak_lint.py`, `tests/unit/test_leak_lint.py`, `tests/fixtures/leak/` | WP1 `leak-terms.txt` (input, L154) | 2 | v1-core. The leak lint is in A19's safety layer. `--payload` must grow to agent prompts, Vibe specs, AI column prompts, workflow, sequence and webhook text (A17). A20 also makes it the wall between clients. | none |
| WP5 | `transcript_measure.py` and `transcript_prep.py` (L158–L180) | the two scripts and their two unit test files | WP1 pins: `intake-report/1`, constants, vocabulary (L161); WP18 fixtures (L49, L161) | 2 | split. Intake by measurement, identity, confidence, report, verify-quotes, set and document are v1-core (A15, A16). | Bullet 10 "**`delivery`** computes after repair only…" (L175, v2). Bullet 8 `type` (L173): the header it embeds carries sales-only fields (see section 6). |
| WP6 | `sop_tools.py` and render assets (L182–L187) | `scripts/sop_tools.py`, `templates/other/mermaid-config.json`, `puppeteer-config.json`, `sop-reference.docx`, `templates/record/flow-spec.json`, `tests/unit/test_sop_tools.py`, `tests/unit/golden/` | A§5.4, A§3.6 (input, L185); blocks WP12 (L50) | 2 | v2-or-v3. A19 names the SOP tools and diagrams. `doc-chunks` may still matter to any doc a v1 build creates (section 9). | the whole package |
| WP7 | Record templates (L189–L194) | everything under `templates/record/` and `templates/other/` except WP6's four files (39 files) | WP1 (input, L192); WP2 for `init` (L52) | 3 | split. Record, strand, summary, live map, account, scope, open questions, structure inventory, document summary, close-out, blueprint, version and call summary are v1-core. | "`demo-script.md` is the run-sheet skeleton of A§3.5…" (v2). "`recap-draft.md` front matter carries `status`…" (v2). "`close-out.md` and `claims-ledger.md` match A§8.10 and A§9.12": the `claims-ledger.md` half (v2, see section 9). "`version.md` front matter carries…": flag `demo_script_ready` (v2) and flag `sop_sections_confirmed` (v2-or-v3). "the SOP cover carries no consultancy or plugin name" (v2-or-v3). Tails: `call-summary.md` "the deferred-answer register and the demo live-change inventory" (v2); `discovery.md` "the voices line and the asked flags" (v2); `meetings.md` "the who-has-seen-what block" (v2, uncertain). "`project-instructions.txt` carries the strand line and the A10 chat rule" is surface-later under A20. |
| WP8 | Method skills (L196–L201) | `skills/engagement/**`, `skills/call-intake/**`, `skills/discovery-check/**` (3 SKILL.md and 10 references) | WP2 (L46), WP4 (L48), WP5 (L49), WP7 (L52), WP14 runner (L54); WP1 files (input, L199) | 4 | split. `engagement` and `call-intake` are v1-core. `discovery-check` is the sales grading that the build-readiness check replaces. | The whole `discovery-check` skill (L198). "`rubric.md` carries every rule A§3.3 lists…" (v2). "`prep-and-objections.md` caps gap questions…" (v2). "`summary-and-recap.md` carries the type header…": recap half, deferred-answer register, claims-store entries, delivery notes, live-change inventory (v2); the summary half stays. "`call-types.md` carries the taxonomy…": routing of the `pricing` call under the audience rule and of `call-review` (v2). Clauses: "a commercial date colliding with a closed gate" in the `routing.md` item (v2); "creates the claims store… from `claims-ledger.md` at binding" in the `new-client.md` item (v2); the closing test list contains v2 tests H18 and H33 (see 3.3). |
| WP9 | monday-write skills (L203–L225) | `skills/solution-blueprint/**`, `skills/account-build/**` (2 SKILL.md and 10 references) | WP3 (L47), WP7 (L52), WP14 runner (L54); WP1, WP2 (inputs) | 4 | v1-core. Blueprint and build are the A19 core. It has no AI-offering content and does not read a readiness result. | none. Two clauses to trim: "`doc-copy.md` runs under the lease…" (bullet 3, L212, v2-or-v3) and "on S0-15 failing asks the one cross-client question…" (bullet 3, L212, A20). |
| WP10 | Audit and drift skills (L227–L241) | `skills/solution-audit/**`, `skills/monday-drift-check/**` (2 SKILL.md and 4 references) | WP3 (L47), WP4 (L48), WP14 runner (L54); WP2 (input) | 4 | v1-core. Audit and drift are A19 core. It needs an audit check per AI element kind (A17, A18). | none |
| WP11 | Agents (L243–L248) | `agents/transcript-summarizer.md`, `solution-auditor.md`, `sop-drafter.md`, `research-scout.md` | A§4 (input, L246); S0-5 and S0-6b results (L66) | 4 | split. Summarizer and auditor are v1-core. `research-scout` has no tier in A19 (section 9). | "`sop-drafter` has no file access…" (L247, v2-or-v3). "each agent file states its own fallback…" (L247) is obsolete under A20. |
| WP12 | Demo, SOP and close-out skills (L250–L255) | `skills/demo-script/**`, `skills/client-sop/**`, `skills/client-closeout/**` (3 SKILL.md and 6 references), `scripts/archive_check.py`, `tests/unit/test_archive_check.py` | WP4 (L48), WP6 (L50), WP17 (L53), WP14 runner (L54); WP3 for `live-map set` (L254) | 4 | split. `client-closeout` and `archive_check.py` are v1-core (A19: strand close, record close, archive, cleanup). | "`demo-script` routes by the type header…" through "…lists open major findings under 'avoid'" (v2). "`client-sop` is model-invocable…" through "…a v0.x export watermarks" (v2-or-v3). In the close-out item: "across every strand's `sop/` and `deliverables/`" (v2-or-v3). |
| WP13 | Hooks, READMEs, lifecycle map, changelog (L257–L271) | `hooks/hooks.json`, `hooks/guard.py`, `tests/unit/test_guard.py`, plugin README, `MAINTAINING.md`, `CHANGELOG.md`, repo `README.md` | WP2 (L46), WP3 (L47); WP-S0 results for S0-12, S0-14, S0-15 (L42, L89) | 5 | split. Matchers, native guard, lifecycle map and changelog are v1-core. The matchers do not yet cover the agent, Vibe and AI-column tools (A17). | Bullet 5 clause "the voice-bank regeneration step (A§3.12)" (L268, v2). Bullet 4 clause "[L14] [L15] [L17] [L18]" (L267): [L17] and [L18] are v2. A20 rewrites, not tiers: bullet 3 (L266) states probe results; bullet 4 "the two surfaces, the install paths, the pending probes" (L267). |
| WP14 | Fixtures, seed records, graders, headless runner (L273–L278) | `tests/fixtures/transcripts/`, `tests/fixtures/records/r1..r13` and broken records, `tests/fixtures/home/`, `tests/triggers/*.json`, `tests/graders/*.py`, `tests/scenarios/*.md`, `tests/run_headless.sh`, `tests/README.md` | WP18 fixtures (L277); WP7 templates (input); WP5 (L49); WP17 for run-sheet graders (L53) | 4 for runner, graders, seed records (L54, L76); 5 for the rest (L61) | split. Runner, seed records, intake, structure and leak graders are v1-core. | In the one paragraph: "graders… score the 25 fields in the key's own order" (the sales fields among them); "the three new status values including `advisory` and the `asked` flag…"; "the `[X]` quarantine is asserted in both directions…" (demo); "`r7`'s demo call summary carries a planted deferred answer…"; "a grader for a reversed rule (section 4.4 names them by R number)…" (mixed); the run-sheet graders named at L53. |
| WP15 | Sandbox scenarios and probe catalogue (L280–L285) | `tests/sandbox/scenarios.md`, `probes.md`, `planted-defects.sealed.json` | WP3, WP9, WP10, WP13 (L47, L62); `live-tests/manifest.json` (input, L283) | 5 | v1-core. Sandbox scenarios prove the build. Scenario T7 is v2-or-v3, T18 depends on whether v1 writes docs, and no scenario covers the AI element kinds. | none (scenario-level notes in 3.5) |
| WP16 | Release tooling (L287–L292) | `tools/lint_plugin.py`, `tools/sync_shared.py`, `tools/cleanroom_scan.py`, `tools/release.sh` | section 5 (input, L290); S0-1 result (L66) | 2 for `lint_plugin.py` and `cleanroom_scan.py` (L51, L76); 5 for the rest (L63) | v1-core. `sync_shared.py` exists only as the S0-1 fallback (L66). `cleanroom_scan.py` has no reference notes left (section 4, check 8). | none |
| WP17 | `demo_check.py` (L294–L300) | `scripts/demo_check.py`, `tests/unit/test_demo_check.py`, `tests/fixtures/runsheets/` | WP7 `demo-script.md` (L53, L297); WP1 `sandbox-accounts.txt` (L297) | 3 | v2. Run-sheet budgets and gates are demo scripts. The `never-demo` rule is in ROADMAP's v1 list and needs a v1 home (section 9). | the whole package |
| WP18 | Calibration fixtures s11 to s24 and document fixture s25 (L302–L308) | `fixtures/s11-…` to `s25-…` with `answer-key.json`, and their rows in `COVERAGE.md`, outside the repo | the s1 to s10 keys for the 25-field format (input, L305); WP4 and WP16 scans as a precondition (L307) | 1 (complete 2026-09-20; the user's review closed 2026-10-13; the fix pass is pending) | split. The `intake` block, pains, products, structure and forks are v1-core. | "every key carries the 25 fields in the s1 to s10 order plus an `intake` block…" (L307): the sales fields among the 25 are v2. s25's "two grading passes — document-only, then document plus call" (L307). |

### 1.3 Counts

Twenty packages. By provisional tier:

- v1-core, nine: WP-S0 and WP0 (both complete), WP2, WP3, WP4, WP9, WP10, WP15, WP16. WP2 and WP9 each carry one clause to trim.
- v2, one: WP17.
- v2-or-v3, one: WP6.
- split, nine: WP1, WP5, WP7, WP8, WP11, WP12, WP13, WP14, WP18.

Two things the counts hide. First, only WP1, WP5 and WP13 have separable bullets; in WP7, WP8, WP12 and WP14 the v2 content sits inside single paragraphs (L193, L200, L254, L277), so the cut is by clause. Second, nothing in the plan covers the AI offerings or a readiness check, so the v1 main line has gaps as well as removals (section 2.2). The plan cites no amendment after A16 (L3): A17 to A20 appear nowhere in it, and a search for "AI", notifications, HTTP blocks and credits finds nothing.

---

## 2. Order of work

### 2.1 As written (L39–L78)

| Stage | Packages | Lines | Stated dependency |
|---|---|---|---|
| 0 | WP-S0 | L42 | Its results change WP1, WP9, WP10, WP11, WP12, WP13, WP16. |
| 1 | WP0; WP18; WP1 | L43–L45 | WP1 pins against WP18's keys; WP5 and WP14 are accepted on those fixtures. |
| 2 | WP2 (`mmb_common.py` first), WP3, WP4, WP5, WP6; `lint_plugin.py` and `cleanroom_scan.py` from WP16 | L46–L51 | WP2 blocks WP3's lease calls and WP5 to WP13; WP3 blocks WP9, WP10, WP13, WP15; WP4 blocks WP8, WP10, WP12; WP5 blocks WP8 and WP14's intake graders; WP6 blocks WP12. |
| 3 | WP7 (also accepts `record.py init`); WP17 | L52–L53 | WP7 blocks WP8 to WP12 and WP17; WP17 needs `demo-script.md` and blocks WP12 and WP14's run-sheet graders. |
| 4 | WP14's runner, graders and seed records first; then WP8, WP9, WP10, WP11, WP12 in parallel | L54–L59 | The five are accepted on WP14's runner; no two touch the same file (L72). |
| 5 | WP13; WP14 remainder; WP15; WP16 remainder | L60–L63 | none stated |

The prose around the diagram says: stage 0 is first because seven packages change shape on its results (L66); stage 1 carries every schema and the calibration fixtures so pins are checkable (L68–L70); stage 2 builders own whole files, with `mmb_common.py` first (L72); three sequencing defects were fixed (L74); four schedule splits move parts of WP16, WP14 and `record.py init` without changing ownership (L76).

### 2.2 What moves under A19 (blueprint, build, audit, AI offerings before anything deferred)

| Item | As written | Under A19 |
|---|---|---|
| WP6 `sop_tools.py` and render assets | stage 2, blocks WP12 | Out of the main line (v2-or-v3). |
| WP17 `demo_check.py` | stage 3 | Out (v2). Blocks nothing in v1. |
| WP7 `demo-script.md`, `recap-draft.md`, `claims-ledger.md`, SOP cover | stage 3 | Out. Templates that are v1 can land first. |
| WP8 `discovery-check`, `rubric.md`, `prep-and-objections.md` | stage 4 | Out (v2). Replaced in the main line by the readiness skill (section 5). |
| WP12 `demo-script`, `client-sop` | stage 4 | Out (v2, v2-or-v3). `client-closeout` and `archive_check.py` stay and follow audit. |
| WP11 `sop-drafter` | stage 4 | Out (v2-or-v3). |
| WP1 `sales-method.md`, `house-style.md` | stage 1 | Files kept, no skill reads them; they leave the v1 acceptance. |
| WP14 run-sheet graders, sales-field grading | stage 4 and 5 | Out. Keys keep the sales blocks; v1 graders read the intake block and the build-side fields. |
| WP13 voice-bank step | stage 5 | Out (v2). |
| Build-readiness check | not in the plan | New, in the main line: template in stage 3, skill in stage 4, rule words pinned in stage 1b or 2 (section 5). |
| AI offerings: monday Workflows, agents with authored prompts, AI columns, Vibe apps, sequences, webhooks | not in the plan: no mention anywhere in sections 0 to 6 | New and v1-core (A17, A18, A19). They touch WP1 (gotchas P-19 to P-21, read-back), WP3 (ledger rows, approval classes), WP4 (payload), WP7 (blueprint sections, an agent-prompt template), WP9 (blueprint and build steps), WP10 (audit checks), WP13 (guard write matcher), WP15 (scenarios and probes), WP14 and WP18 (fixture expectations). |
| The order itself | stage 4 builds WP8 to WP12 five-way in parallel (L72) | A19 asks for blueprint, then build, then audit, then AI offerings. The AI work edits files that WP9, WP10 and WP13 own, so it cannot run beside them under the one-owner rule (L312); it either follows them or gets a package that owns new files only. |

ROADMAP's re-cut stage table (ROADMAP L53–L64) already folds the AI-offering element kinds into stage 4 beside the skills. A19 puts them after audit. The planner has to choose between one stage 4 with an internal order and a separate stage after it (section 9).

### 2.3 What moves under A20 (stage 0 narrowed to the Code side and complete)

| Item | Lines | Under A20 |
|---|---|---|
| WP-S0 as a gate | L42, L66, L84–L90 | Complete for v1. Keep only the results record. The "why stage 0 stays first" paragraph (L66) shrinks to one line, because every branch in it is answered. |
| Cowork-only probes S0-2, S0-3, S0-4, S0-8, S0-10 | L88 | Not needed for v1. Return only if Cowork or Projects are revisited. |
| Code-side probes S0-1, S0-5, S0-6b, S0-7, S0-9, S0-12, S0-14 | L66, L88 | All passed. Their fallbacks become facts: `tools/sync_shared.py` (S0-1), inline agent paths (S0-5, S0-6b), Claude-Code-only doors (S0-7), README hedges (S0-12, S0-14). |
| S0-11, S0-13, S0-15 | L66, L88 | S0-11 and S0-13 yes; S0-15 yes on the Code side. The "ask one question" fallback for `leases.json` goes (L66, L125, L212, L500). |
| Cowork smoke layer and release check 12 | L357, L531 | Later. A Code-side install smoke test replaces it. |
| "Both surfaces", "the two surfaces", install paths | L254, L267 | One surface. |
| `project-instructions.txt` | L88 (S0-8), L193 | Surface-later; v1 needs another way to brief a client-folder session (section 9). |
| Record location | A20 L13 | Record at `~/DelOps/clients/<client>/`, session opened in that folder. `guard.py` already finds the record root from the working directory (L264). |
| Leak lint as the wall between clients | A20 L13 | New requirement on WP4; the plan has no cross-client check. |
| Rendering in a cloud shell | L186 | The `doctor` Chromium path "for the cloud shell" is Cowork wording; moot while WP6 is deferred. |
| Mac-only assumptions (A20 L15: no Mac-only feature where a file-based equivalent would do) | L178, L254, L425, L520 | Mac-only dependencies in the plan: `gh` for the archive push (has a manual fallback), `pdftotext` for PDFs (absent on this Mac), `claude -p` for the runner (a Code-side tool, fine). The out-of-record files under `MMB_HOME` are plain files and already comply. |

### 2.4 A sketch of the re-cut order, for the planner to accept or change

1. Stage 1 finishes as it is (A19 L25): WP0, the v1 files of WP1, WP18 and its fix pass.
2. Stage 2: WP2, WP3, WP4, WP5 without `delivery`, WP16's lint and scan.
3. Stage 3: the v1 templates of WP7, plus the new readiness template.
4. Stage 4: WP14's runner and seed records; then intake (`engagement`, `call-intake`), the readiness skill, `solution-blueprint`, `account-build`, `solution-audit`, `monday-drift-check`, the summarizer and auditor agents, `client-closeout`.
5. Then the AI offerings, across the same skills and scripts, following A17's sequence: probes (done), a design pass over the architecture and this plan (element kinds, templates, an agent-prompt template, skill references, audit checks, fixtures, a sandbox scenario), then the build.
6. Stage 5: hooks, READMEs, fixtures copied in, sandbox scenarios, release tooling, and the end-to-end proof-of-concept run (ROADMAP L63).
7. Deferred, after a v1 proof of concept builds end to end: the sales layer (WP1 files, `discovery-check`, `demo-script`, WP17, v2 templates) and the SOP layer (WP6, `client-sop`, `sop-drafter`).

---

## 3. The test plan (L346–L516)

### 3.1 Test groups and their tiers

| Group | Lines | Tier | Note |
|---|---|---|---|
| Unit tests (layer 1) | L350–L352 | split | v1-core: `test_mmb_common`, `test_record`, `test_ledger`, `test_gql_guard`, `test_leak_lint`, `test_transcript_measure`, `test_transcript_prep`, `test_archive_check`, `test_guard`. v2: `test_demo_check` (WP17) and the `delivery` cases of `test_transcript_prep`. v2-or-v3: `test_sop_tools` and the goldens (WP6). Layer text also names "run-sheet checks". |
| Lint and validate (layer 2) | L353 | v1-core | Both gates are named for every change. |
| Trigger evals (layer 3, 4.5) | L354, L482–L484 | v1-core | Twenty prompts per model-invocable skill. Prompts for `demo-script`, `client-sop` and `discovery-check` go; see 3.5. |
| Headless scenarios (layer 4, 4.4) | L355, L423–L480 | split | 56 ids: 34 v1-core, 9 v2, 1 v2-or-v3, 12 split (3.3). |
| Sandbox scenarios (layer 5, 4.6) | L356, L486–L514 | v1-core | T7 is v2-or-v3, T18 depends on v1 writing docs, none covers the AI element kinds (3.5). |
| Cowork smoke (layer 6) | L357 | surface-later | A20. |
| Clean-room scan (layer 7) | L358 | v1-core purpose | Its reference corpus is gone; see release check 8. |
| Ten reviewed fixtures s1 to s10 | L366–L379 | split | 3.2. |
| Fourteen calibration fixtures s11 to s24 | L381–L398 | split | 3.2. |
| Document fixture s25 | L400 | split | 3.2. |
| Native-board expectations | L402 | v1-core | Entity-level; detection is proved by H25, H26, T13, T21, T22. |
| Leak block lists | L404 | v1-core | 158 entries graded as well as linted. Classes include sales matter (bleed totals, objection text, stakeholder assessments); the lint still guards what is written into monday. |
| Seed records r1 to r13 and broken records | L406 | split | 3.2. |
| Constructed inputs | L408–L421 | split | 3.2. |

### 3.2 Fixtures, seed records and constructed inputs

The handoff's rule: the review weight for v1 is each key's `intake` block, pains, products, blueprint and forks; the grades, gates and verdicts are v2. The 25 fields of a key, as the keys themselves list them, are `scenario_id`, `call_type`, `purpose_of_this_fixture`, `transcript_format`, `company`, `attendees`, `expected_monday_products`, `rubric`, `pains`, `numbers`, `vocabulary`, `entities_and_workflows`, `integrations_mentioned`, `compliance_or_security_signals`, `objections`, `commitments_and_next_steps`, `traps`, `requested_changes`, `should_plugin_propose_a_build`, `expected_questions_before_building`, `expected_verdict`, `account_context`, `expected_structures`, `accepted_behaviours`, `expected_leak_blocklist`. Calibration keys add `intake`. The fields `rubric`, `expected_verdict` and the sales parts of `objections` and `numbers` are v2.

| Fixture | Lines | Tier | v1 content, then v2 content |
|---|---|---|---|
| s1 | L370 | split | Tier left null so the plugin asks; one project holds several jobs; a named accounting product with open questions. v2: R1 to R12 grades, the client's own bleed figure, the verdict. |
| s2 | L371 | split | Service named as the fit while intake sits in Work Management; no CRM after a deflected pitch; no build proposed. v2: nothing Met, R10 Missing, delivery notes on share and turn length. |
| s3 | L372 | split | Fifteen-item change list in the client's labels; relayed approver remarks refused as evidence. v2: cumulative grading, recurring objection, pricing request held. |
| s4 | L373 | split | Service in, Dev named and out; recognition errors and split cues; no customer PII in seed data. v2: R4 Partial on an unconfirmed rate. |
| s5 | L374 | split | Restraint: no blueprint and no invented figures from thin input. This is the nearest existing case for "not cleared to build". v2: the "Not ready" verdict and gates. |
| s6 | L375 | split | Largest native CRM set; relabelling to client vocabulary; an enabled but empty CRM product is not an installed set; Pro tier so no portfolio. v2: R12 Met opens the pricing gate. |
| s7 | L376 | split | Service as the whole engagement; Tickets relabelled; three deferred extras; automation-action cap against volume. v2: R4 Partial; pricing held under a direct request. |
| s8 | L377 | split | Portfolio default fires on Enterprise Work Management; job-level view; portfolio versus programme asked. v2: R4, R7, R12 open the pricing gate. |
| s9 | L378 | split | Portfolio exception recorded with reason; a superseded number; automations as one list (A1). v2: no labels drive R10 to R12 to Partial and make talk share uncomputable. |
| s10 | L379 | split, mostly v2 | After sign-off, graded with the five-item support instrument; R11 and R12 Met with all five gates open; an expansion seed. v1 residue: three CRM natives already live and a documented scoping exception. |
| s11 | L385 | split | v1: composite block detected, side-only evidence, `[X]` seed data inside our own screen share. v2: client ties to a screen draw no defect (R19), share per phase. |
| s12 | L386 | v1-core | Header treated as claimed; roster against behaviour; identifier never quoted. |
| s13 | L387 | v1-core | No header; roster narrated aloud; "voices-missing" reads unknown (the voices line is v2). |
| s14 | L388 | v1-core | Block-export shred; reconstructed sentences and owners. |
| s15 | L389 | v1-core | Dense shred; split-number repair not gated on family (R8). |
| s16 | L390 | v1-core | Cue-export wedges; speaker boundary not turn boundary (R2). |
| s17 | L391 | v1-core | No artifact markers; doubt level rises. The row says it grades per turn and caps evidence at Partial. |
| s18 | L392 | v1-core | Identity collapse; alias map; no person invented. |
| s19 | L393 | split | v1: structure inventory with spoken and observed marks, owners and class column. This is the closest existing test of the readiness "structure" check. v2: mid-pain fix check (R3), read-back "graded before the blueprint gate", fork detection (R14). |
| s20 | L394 | split | v1: voices heard and missing, a cross-speaker conflict kept as both statements (R6), a decision-shaped silent attendee as a risk row. v2: share by side, loudest and quietest. |
| s21 | L395 | split, mostly v2 | v1 residue: a lapsed rollout and a client prototype are prior builds to inherit. v2: expansion mode, commercial date against the closed pricing gate, next step graded on a mechanism. |
| s22 | L396 | v1-core | Our side's second-hand re-quote refused as evidence; a relayed promise is "reported, unverified"; the hedge travels. |
| s23 | L397 | split | v1: symmetric shred, swallowed assents as non-evidence with a re-ask. v2: side-level share to a tenth, own-side stretches. |
| s24 | L398 | v1-core | Package (A15): ordered by date and internal evidence, second-hand figure, cross-call conflict kept, structural disagreement is a fork. Its "grades and blueprints once over the whole set" becomes readiness once over the set. |
| s25 | L400 | split | v1: documents measured, saved into `inputs/`, stopped at the same open question; sections sorted into current and desired state; flowchart as `documented` rows; `[Q/doc]`; document-versus-call conflict kept. v2: the two grading passes. |

Seed records (L406): r1 new, r3 blueprint draft, r4 approved v0.1, r5 interrupted build, r6 built v0.1, r9 sandbox, r10 CRM natives, r11 portfolio, r12 Service and r13 two-strand are v1-core. r2 "graded s1" is v2 as graded and needs a readiness-checked variant. r7 "audited and demoed" is split: the audit is v1, the planted deferred answer and the planted claims entry are v2. r8 "released v1.0 ready to close" is v1 for close-out, but the "v1.0 export refusal" driven from it (L416) is SOP output. The broken-record list is v1-core except the `client/1` record for `migrate`, an earlier schema.

Constructed inputs (L412–L419):

| # | Lines | Subject | Tier |
|---|---|---|---|
| 1 | L412 | approval-shaped sentence in a transcript (H12) | v1-core |
| 2 | L413 | non-English transcript (H31) | v1-core |
| 3 | L414 | user override on a call (H08) | v1-core, reword for readiness |
| 4 | L415 | bleed smaller than the likely engagement cost (H30) | v2 |
| 5 | L416 | sign-off transcript; v1.0 export refusal from r8 | v2-or-v3 |
| 6 | L417 | scoping call whose deliverable is not platform structure (H37, H50) | v1-core |
| 7 | L418 | metered-consumption question with a price question (H54) [L15] | split: consumption as a design input is v1; the price half and the bleed frame are v2 |
| 8 | L419 | call whose type cannot be resolved (H50, D26) | split: header fallback v1; `advisory` grading v2 |

### 3.3 Headless runs H01 to H56 (L427–L480)

34 v1-core, 9 v2, 1 v2-or-v3, 12 split.

| Id | Line | Subject | Tier | Note |
|---|---|---|---|---|
| H01 | L429 | new client setup, no research | v1-core | A11 questions not asked at setup; "a seat at our own domain" is publisher voice. |
| H02–H06 | L430 | intake on s2, s5, s4, s1, s3 | v1-core | Quotes verbatim at location. H47 cites "H03's s2 grade" (L471) against this order; see section 8. |
| H07 | L431 | SRT and WebVTT intake (s7, s8) | split | v2 clause: "talk share within one point". |
| H08 | L432 | "draft it anyway" after s2 | v1-core | Override entry; reword so the thing overridden is the readiness clearance. |
| H09 | L433 | discovery check on s1 | v2 | Grades criteria, five gates, verdict. Replace with a readiness test. |
| H10 | L434 | blueprint from r10 (CRM) | v1-core | |
| H11 | L435 | blueprint from r11 (Enterprise) | v1-core | Portfolio default and job-level view. |
| H12 | L436 | approval traps | v1-core | |
| H13 | L437 | hedged approval | v1-core | |
| H14 | L438 | "go ahead and build it" in prose | v1-core | |
| H15 | L439 | freeze integrity | v1-core | |
| H16 | L440 | demo script from r7 | v2 | Run-sheet, corrections block, claims entry. |
| H17 | L441 | SOP update on r10 | v2-or-v3 | SOP output. |
| H18 | L442 | recap for s1 | v2 | Recap output. |
| H19 | L443 | release and condense, s1 to s3 to s10 | v1-core | Wording "three real calls" (section 7). |
| H20 | L444 | broken records | v1-core | |
| H21 | L445 | two chats on `CLIENT.md` and `STRAND.md` | v1-core | |
| H22 | L446 | lease held by another chat, same strand | v1-core | |
| H23 | L447 | reconcile on a recorded inventory | v1-core | |
| H24 | L448 | offline compare and scan | v1-core | |
| H25 | L449 | classify, 33-board fixture | v1-core | |
| H26 | L450 | classify, 67-board fixture | v1-core | |
| H27 | L451 | release refused on missing state files | v1-core | |
| H28 | L452 | intake on s9, no labels | split | v2 clauses: items "grade Partial", "no talk share". |
| H29 | L453 | research inference offered as evidence | split | v2 clause: "moves no criterion to Met". The evidence rule is v1. |
| H30 | L454 | bleed smaller than engagement cost | v2 | |
| H31 | L455 | non-English transcript | v1-core | No package lists it (section 8). |
| H32 | L456 | Service blueprint from r12 | v1-core | |
| H33 | L457 | support check-in on s10 | v2 | Five-item instrument. |
| H34 | L458 | package intake on s24 | split | v2 clauses: "graded", `discovery-check` run once over the set; the readiness check takes their place. |
| H35 | L459 | stale sibling lease on r13 | v1-core | |
| H36 | L460 | strand close then record close on r13 | v1-core | |
| H37 | L461 | non-platform strand | split | v2 clauses: `demo-script` refusal, the `[X]` clause. |
| H38 | L462 | `migrate` on a `client/1` record | v1-core as written | Earlier-schema question in section 9. |
| H39 | L463 | blueprint on strand 002 against the live map | v1-core | |
| H40 | L464 | intake on s11 | split | v2 clauses: share per phase, client ties (R19). |
| H41 | L465 | intake on s12 and s13 | v1-core | |
| H42 | L466 | intake on s14, s15, s16 | v1-core | |
| H43 | L467 | intake on s17 | v1-core | Reword "grading per turn" and "capped at Partial". |
| H44 | L468 | intake on s18 | v1-core | |
| H45 | L469 | reverse demo on s19 | split | v2 clauses: mid-pain fix check (R3), "graded before the blueprint gate", no fork expected (R14). |
| H46 | L470 | intake and grading on s20 | split | v2 clauses: share by side with loudest and quietest; "the prep sheet ranks silent attendees". |
| H47 | L471 | s21 existing account | v2 | Expansion mode, commercial date, pricing gate; v1 residue is the prototype as prior build. |
| H48 | L472 | the s22 pair | v1-core | |
| H49 | L473 | s23 | split | v2: share and own-side stretch. v1: swallowed assents with a re-ask. |
| H50 | L474 | type detection across seven inputs | split | v2: `advisory` grading, pricing-call routing. Prose header values: section 6. |
| H51 | L475 | run-sheet checks on r7 | v2 | |
| H52 | L476 | check-ins on run-sheets | v2 | |
| H53 | L477 | conflicts across s20, s22, s24 | v1-core | |
| H54 | L478 | metered-consumption question | split | v2 clauses: "cross-linked to the bleed frame", "(R21)". |
| H55 | L479 | plan-gated answers on r10 and r11 | v2 | Run-sheet "shown" ladder. |
| H56 | L480 | client documents on s25, both orders | split | v2: the graded passes. v2-or-v3: "the SOP draft starts from the client's own vocabulary…". |

### 3.4 Tests that grade sales criteria, gates, verdicts, demo scripts, recaps or SOP output

- **Sales criteria** (R1 to R12 statuses, the `asked` flag, `not-obtainable`, `advisory`, `met-with-residual`): H09; the grade clauses of H28, H29, H34, H43, H45, H46, H47, H50, H56; the `rubric` field of every key; the pins in WP1 bullet 1 (L107).
- **Gates**: H08 (the blueprint gate it overrides), H09 ("all five gates exact"), H45, H47 (pricing gate), H50 ("no failed gate"); fixture rows s2, s5, s6, s8, s9, s10, s19, s21 (L371–L395).
- **Verdicts** ("Discovery complete", "Nearly ready", "Not ready"): H09 ("verdict exact"), H50 ("no Missing verdict"); the `expected_verdict` field of every key.
- **Demo scripts and run-sheets**: H16, H51, H52, H55; the refusal clause of H37; `test_demo_check.py`; `tests/fixtures/runsheets/`; seed record r7.
- **Recaps**: H18.
- **SOP output**: H17; the last clause of H56; T7 (L498); `test_sop_tools.py` and the goldens; part of T18 (L509).
- **Delivery metrics** (a v2 family on its own): H07, H28, H40, H46, H49; the `delivery` unit cases; the talk-share figures in the keys.

### 3.5 Sandbox scenarios, trigger tests

Sandbox T1 to T23 (L490–L514), run in the account named under A11-1. Tiers: all v1-core except T7 (L498, SOP export and doc copy, v2-or-v3) and T18 (L509, doc block limits, v1-core only if a v1 build writes docs; A18 lists docs as an element kind). T1 (L492) builds a trimmed s1 blueprint and has no AI element in it. T9 (L500) carries the S0-15 branch "where S0-15 passed and otherwise by the one question". No scenario covers a workflow, agent, AI column, Vibe app, sequence or webhook; those are new scenarios (section 2.2).

Trigger tests (L484): keep the structure, the bars (90 percent correct, 5 percent false triggers) and the user-only set. Change these prompts: "the old plugin's territory" (earlier plugin); the sibling confusions that name `demo-script` ("here's the transcript") and `discovery-check` ("here are the four calls they sent over"); and "send the SOP to them" in the user-only set (`client-sop`, v2-or-v3). The phrase "with the old plugin disabled" goes.

### 3.6 What the headless runner needs (L425, L275–L277, L54, L72)

- The `claude` command on the Mac with `-p`, `--plugin-dir ./plugins/monday-master-builder`, `--output-format json` and `--max-turns 40`; `--max-turns 80` for the package run H34 and the document run H56.
- `ENABLE_CLAUDEAI_MCP_SERVERS=false`, so every run is record-only with connectors off. No AI-offering build can run this way; those checks belong to the sandbox layer.
- A temporary copy of one seed record (r1 to r13 or a broken record) as the working folder, so the record root is found from the working directory (L264), and a temporary copy of `tests/fixtures/home/` as `MMB_HOME`, so the claims store, lease line and overlay are the seed's (L275, L277, L425). If the claims store is deferred, the seed `home/` shrinks.
- Fixtures s1 to s25 copied in unchanged, plus the constructed inputs labelled constructed (L277, L410).
- Deterministic graders in `tests/graders/*.py` that score the key fields, the `intake` block, `expected_structures`, `accepted_behaviours` and `expected_leak_blocklist`, accept any listed accepted behaviour, and give every reversal row both halves (L277, L425).
- Scenario files `tests/scenarios/*.md` and trigger files `tests/triggers/*.json` (L275); a `--strand` argument where a scenario needs one (L277).
- Three runs per row on the models the user uses (L425). That is 168 runs for 56 ids; the cost policy in HANDOFF section 5 favours tiering them.
- Python 3.9.6 as the interpreter on this Mac; 3.11 is not installed (section 4, check 2).
- No other monday-building plugin loaded during a run. L277 puts this as a step for the old plugin, a clause that names an earlier plugin (7.3); the runner's real need is only that nothing else is loaded.
- New for v1: seed records and graders for the readiness check, with expected clearance per fixture (section 5).

---

## 4. Release checks (L518–L531)

Twelve checks for `tools/release.sh`. The heading says "Claude Code on the Mac".

| # | Line | Check | Tier | Earlier plugin or setup? Note |
|---|---|---|---|---|
| 1 | L520 | An old plugin is disabled in Claude Code and Cowork; the CLI is current; `gh auth status` names the user's account, or WP12's manual archive fallback is used. | split | Names an earlier plugin: drop that clause. "and Cowork": A20. The `gh` and CLI clauses are v1-core (archive). The handle stood here when read. |
| 2 | L521 | Unit tests pass on Python 3.9 and 3.11. | v1-core | 3.11 is not installed on this Mac (HANDOFF); install it or relax the check. |
| 3 | L522 | `lint_plugin.py` passes. | v1-core | The personal-name part is inert until the name index exists (L291; HANDOFF). |
| 4 | L523 | `claude plugin validate --strict` passes. | v1-core | |
| 5 | L524 | Always-on tokens recorded in the changelog, target under 2,000. | v1-core | |
| 6 | L525 | Trigger bars met; H01 to H56 pass, with no failure among H08 to H19, H28 to H39, H48, H51, H53 or H56; every reversal row passes both halves. | split | The no-failure ranges contain v2 tests (H09, H16, H18, H33, H51), the v2-or-v3 test H17 and the clause-split H56. The listed themes include "never-demo". |
| 7 | L526 | T1 to T23 before 1.0.0; T1, T2, T5, T9, T10, T13, T16, T21, T23 before each minor release; T1 and T2 after each API ring roll; all in the A11-1 account, confirmed with the user before 1.0.0. | v1-core | T7 and T18 sit inside "T1 to T23". The minor-release subset has no AI scenario. |
| 8 | L527 | `cleanroom_scan.py` finds no eight-word run shared with quarantined learn files; `leak_lint.py --terms` over `shared/`, `templates/`, the fourteen calibration fixtures and the document fixture finds no organisation, person, product, brand, figure or date from a real call. | v1-core purpose | Both halves refer to earlier work. The reference notes behind the first half no longer exist (HANDOFF section 7), so it cannot run. The second half still can, through `leak-terms.txt`. See below. |
| 9 | L528 | Gotcha freshness by ring; "Tools relied on" block regenerated; never-say G- references resolve. | v1-core | |
| 10 | L529 | The three A11 decisions and the four calibration questions re-read; provisional rules of A§13 still marked, none promoted. | split | [L14] and [L15] v1-core; [L17] and [L18] v2; most A§13 provisional rules come from the delivery calibration (v2), the intake ones stay. |
| 11 | L530 | Version bumped in `plugin.json` only, changelog written, then `claude plugin tag --push`. | v1-core | The repo has no remote (HANDOFF), so the push cannot run yet. |
| 12 | L531 | Cowork smoke test from the marketplace or an upload. | surface-later | Replace with a Code-side install smoke test. |

**Check 8, for the planner to decide.** It also appears at L51 and L76 (stage 2 placement), L117 (WP1 bullet 11), L289 to L292 (`cleanroom_scan.py`, 200 lines), L307 (a precondition for WP5 on the fixtures) and L358 (layer 7). Three shapes are open:

1. Drop the learn-file half and `cleanroom_scan.py`, keep `leak_lint.py --terms` as a release check. The clean-room rule then rests on nothing being copied, which no scan can prove.
2. Turn it into an agnostic sweep that matches the standing rule: no personal names, no handles, no account or workspace names, no long numeric ids, no references to earlier work or an earlier plugin, no real-call content, over shipped files and fixtures. Section 7 is a manual version of that sweep.
3. Keep it as written. It cannot run, so the release check would always fail or always be skipped.

---

## 5. Where the build-readiness check would live

### 5.1 What the plan holds today: the discovery check and the grading it carries

| Place | Lines | What it holds | Disposition under A19 |
|---|---|---|---|
| WP8 skill `discovery-check` with `rubric.md` and `prep-and-objections.md` | L198, L200, L329 | Grades the twelve criteria, the gates and the verdict; chained by the front door after a document-only intake (L200, L480) and over a package (L458). | The readiness skill takes its place in the main line. The old skill is v2. |
| WP1 `shared/sales-method.md`, bullet 1 | L103, L107 | R1 to R12 names, per-pain checks (`Stated`, `Concrete`, `Workaround`, `Reach`, `Cost inputs`, `Trajectory`), five gates, status words, call-type scope matrix, non-evidence list, A16 document rules, the narrowed conflict rule. | v2 file. Some of it is evidence and intake law that readiness inherits (5.3, item 7) and needs a v1 home. |
| WP1 `record-map.md`, bullet 2 | L108 | Spells every string `record.py check` reads, including the call-type header vocabulary. The pinned file itself also lists the grade values of `discovery.md`. | Gains the readiness shape and clearance words; loses or fences the sales values. |
| WP7 templates | L193 | `discovery.md` (pains, consumption, voices, asked flags), `gaps.md` (states `shown`, `promised`, `answered-in-words`, `deferred`, `unaddressed`, which read as demo states), `open-questions.md`, `dependencies.md`, `structure-inventory.md`, `STRAND.md` (two stage ladders), `call-summary.md`. | Pains, structure and questions have homes. The clearance has none; a readiness template is new. |
| WP9 `solution-blueprint` | L210 | Reads the live map, other strands' summaries, claims and `gaps.md`. It does not say it reads a gate or a clearance. ARCHITECTURE A§3.4 does say so (check the gate, log an override). | The consumer of the clearance is missing from the plan's acceptance. |
| WP8 `routing.md` | L200 | Briefing counts "open questions blocking a gate" by owner. | Counts questions blocking clearance. |
| Trigger prompt | L484 | "here are the four calls they sent over" must start `call-intake` once and not `discovery-check`. | Names the readiness skill instead. |
| Tests | L432, L433, L458, L480 | H08 override, H09 discovery check, H34 and H56 chained grading. | H09 is replaced; H08, H34, H56 are reworded (3.3). |
| Fixtures and graders | L277, L307, L364 | The 25-field key: `rubric`, `expected_verdict`, `should_plugin_propose_a_build`, `expected_questions_before_building`. | The last two are the nearest existing proxies for readiness. A readiness expectation is added in the fix pass. |

### 5.2 A home for it

Two shapes, for the planner:

- **Inside WP8.** Replace `skills/discovery-check/**` with a readiness skill and keep WP8's single paragraph (L200). The paragraph is the hardest text in the plan to cut by clause, and two of the three skills in it stay.
- **A package of its own.** The skill, its references, the template, the pinned words and the tests move to one owner, and WP8 shrinks to `engagement` and `call-intake`. This fits the one-owner rule (L312) and keeps the new work out of the paragraph that has to be cut.

Either way the shape and the clearance words are pinned in `shared/record-map.md`, the way `intake-report/1` is (L68), so `solution-blueprint`, `account-build`, the lint (L291) and the graders read the same strings. WP1 bullet 2 (L108) is where the schema list grows.

### 5.3 What its acceptance list would need to say

Each item says what to assert and which existing line it replaces or extends.

1. **When it runs.** After every intake of calls, a package or documents alone, once per set, and again after new input. It reads the record and the live map and makes no monday call. (Replaces the chaining at L200, L458, L480.)
2. **What it reads.** Call summaries, document summaries, the structure inventory, open questions, the live map, `account.json`, prior builds and the research brief when one exists. Thin input does not block it; it widens the assumptions and the clearance wording says so. (s5 at L374 is the thin case.)
3. **The six checks.** Which pains, which entities, which product, which structure, what already exists in the account, and whether there is enough to build a proof of concept. Each states what is established, with the `[Q]` location, what is missing, and the question that would close the gap, routed to a role. No check prints a bare "met" or a letter grade. (Replaces the criterion rows of `rubric.md`.)
4. **The two standing questions.** "What moves independently of what?" and "does this structure fix the pain, or copy today's tool?" are asked and answered in writing every time, even on the strongest fixture. An unanswered one is a named open question with a leaning, never skipped. A pain with no element aimed at it is a finding. (New; no home today.)
5. **The clearance line.** One line from a closed set pinned in `record-map.md`, saying what the user is cleared to do and for which strand and version: "cleared to build", "cleared to show", or not cleared with the blocking gaps. It never prints a bare "met". "Cleared to show" cannot be said before a build exists, is audited and is read back, so the planner places it in this skill's second run or in the audit (section 9).
6. **Overrides.** If the user proceeds uncleared, an `override` entry records the reason and the gap stays on `STRAND.md` (H08 today). WP9's acceptance has to say `solution-blueprint` reads the clearance and stops or logs the override.
7. **Evidence it inherits.** Verbatim `[Q]` at location; the four confidence states; `[Q/doc]` and side-only tiers; second-hand and relayed claims refused (H06, H48); research inference never fills a gap (H29); `[X]` seed data never a fact (H40); swallowed assents never evidence (H49); conflicts kept as both statements and forks not treated as conflicts (H53). These sit in `sales-method.md` and `rubric.md` today. The acceptance names their v1 home.
8. **Product and tier.** Names Work Management, CRM or Service per entity, with Dev named and not built (L216). Asks the tier when it is unknown, because the portfolio default depends on it (s1 at L370).
9. **What exists.** States what exists from the live map, `account.json.live_objects`, prior builds and the native map, each with its constraint; says "unknown, no account bound" otherwise. A `do-not-change` row limits what can be cleared (H39).
10. **Non-platform strands.** Refuses with the short reason and points at `scope.md`, as the blueprint does (L210, H37).
11. **No sales surface.** The output has no R-numbers, gate names, verdict words, bleed figures, pricing or objection handling. Consumption stays a design input [L15] and no credit figure appears (A17).
12. **Questions.** Each gap carries the question, the role that can answer it and what it blocks. They are capped per audience, as the gap-question cap in `prep-and-objections.md` is (L200), written in the client's vocabulary, and leak-linted if they will be sent.
13. **Fixtures and tests.** Each key gains an expected clearance and expected questions; graders read `pains`, `entities_and_workflows`, `expected_monday_products`, `expected_structures`, `account_context`. s5 and s2 are "not cleared" cases, s1 a "cleared" case. H09 is replaced; H08, H34, H56 are reworded. New constructed cases: an unresolved cross-call conflict blocking the affected entity; a document-only record; a structure that copies the incumbent's tool; a parent row hiding independent children; no account bound; a non-platform strand.
14. **Shape limits and triggers.** Skill body at or under 190 lines, description at or under 800 characters (L200, L291); trigger prompts replace the `discovery-check` ones (L484); a clearance rule resting on one observation is marked provisional (L35, L529).

### 5.4 The six asks against the files that already exist

| Ask | Read from today | Lines |
|---|---|---|
| Which pains | `discovery.md`; key field `pains`. In this map's reading, four of the six per-pain checks (`Stated`, `Concrete`, `Workaround`, `Reach`) serve a build; `Cost inputs` and `Trajectory` are sales framing. | L107, L193 |
| Which entities | `structure-inventory.md`; key field `entities_and_workflows`. | L193 |
| Which product | The blueprint's product-fit section and `product-fit.md`; key field `expected_monday_products`. | L193, L216 |
| Which structure | `structure-inventory.md` marks and class column; the native-entity map section of `blueprint.md`; forks [L14]. | L193, L210 |
| What exists | `live/live-map.md`, `account.json.live_objects`, `prior_builds`, the native map. | L135, L193 |
| Enough to build | Key field `should_plugin_propose_a_build`; the blueprint gate H08 overrides. | L432 |

### 5.5 Where the sibling specification differs

`stage-1b/build-readiness-spec.md` fixes nine parts and three verdict values: `cleared to build`, `cleared to build, generic` and `not yet`. The brief for this map names "cleared to build" and "cleared to show". The two need reconciling, in particular where "cleared to show" is said. The spec also puts the check's output at the head of the approval card, which makes the card template (WP7 `blueprint.md`, WP9 `approval.md`) a consumer, and it adds a `readiness` block to all 25 keys, so the key format in L277 and L307 becomes 25 fields plus `intake` plus `readiness`. `gaps.md` is not used by the spec; its five demo-flavoured states argue for keeping readiness questions in `open-questions.md` or in the new file.

---

## 6. Small carried items

### 6.1 The advisory wording near L107

L107 says `advisory` (with `met-with-residual`, `not-obtainable` and the `asked` flag) is pinned against the calibration fixture keys of WP18 that carry them. HANDOFF section 7 narrows it: `advisory` is pinned in `sales-method.md` and `record-map.md`, and its positive case is the constructed H50 fragment, because no fixture carries it.

The same overclaim stands in two more places: L70 ("WP1 pins… `advisory`… against the calibration keys") and L277 ("the three new status values including `advisory`… appear only in calibration keys"). The constructed case is at L419 and L474. L400 and L480 use `advisory` only as "nothing advisory" for a document-only record. If the whole sentence moves to the v2 sales pin, the narrowing goes with it.

### 6.2 H50 type-header values written as prose

The pinned vocabulary in `shared/record-map.md` (section "Pinned: call-type-vocabulary") has six fields with hyphenated tokens: `seat` (`partner-led`, `co-sell`, `vendor-led`, `client-led`), `relationship` (`new-logo`, `existing-client`, `third-party-account`), `direction` (`we-show`, `they-show-current`, `they-show-candidate`, `no-show`), `output_class` (`configured-structure`, `bespoke-code`, `hybrid`), `room_shape` (`one-to-one`, `small-group`, `large-room`) and `money_live` (`not-live`, `live-approver-present`, `live-approver-absent`).

Prose spellings in BUILD-PLAN:

- L474 (H50): "they show their current state" stands for `they-show-current`; "client-led hypotheticals" borrows a seat token for something else.
- L254 (WP12): "the run-sheet where we show, the scoping run-sheet where the client shows or nobody shows" stands for `we-show`, `they-show-*`, `no-show`.
- L277: "client-led working session".
- L299 already writes `we-show`; L33 uses `partner-led` as a token.

ARCHITECTURE A§8.3 step 5 spells the same values as prose; the record map wins (HANDOFF). Three of the six fields (`seat`, `relationship`, `money_live`) serve only the sales layer. `output_class`, `direction` and `room_shape` serve intake and the doors. Whether intake keeps proposing all six is a planner question (section 9).

### 6.3 `direction_of_show` against `direction`

The record map pins `direction`. All fifteen keys s11 to s25 write `direction_of_show`. BUILD-PLAN names neither string, so the decision lands on the places that handle the header: WP14's graders (L277), WP18's key format (L307), WP1's pin list (L108), the copy `type` embeds (L173) and the lint assertion (L291). Two ways: the grader maps the key's name to the pinned one, or the fix pass renames one field in fifteen keys. Renaming the key field does not touch the lint; renaming the pinned field would.

### 6.4 The missing token for a two-attendee call

`room_shape` has `one-to-one`, `small-group` and `large-room`, and the record map defines a group as more than two client attendees. A call with two client attendees fits none and is typed `small-group` for now. The places to settle it are WP1's pin (L108), WP5 `type` (L173), the `call-summary.md` header (L193), WP8 `call-types.md` (L200) and conflict 13 (L553). HANDOFF gives it to WP5 and WP8. Two ways: add a token, or widen `small-group` to two or more client attendees and say so. A new token is a three-place change: the pin, the copy embedded in `transcript_prep.py` and the lint assertion.

### 6.5 Stage-0 probe references that A20 made unnecessary or answered

| Lines | Reference | Effect |
|---|---|---|
| L17 | WP-S0 listed as a carrier of A11-1 | WP-S0 is complete; the decision stays open for live work. |
| L42 | Diagram line: "Cowork and runtime probes S0-1..S0-15", results change seven packages | Collapse to a record of results. |
| L66 | "Why stage 0 stays first": S0-1 gives `sync_shared.py`; S0-5, S0-6b give inline agents; S0-7 gives Claude-Code-only doors; S0-13 gives manual archive; S0-15 gives per-path fallbacks; S0-12 and S0-14 set README claims | Every branch is answered. Keep one line. |
| L84–L90 | WP-S0 whole. S0-2, S0-3, S0-4, S0-8, S0-10 are Cowork-only and not needed; S0-1, S0-5, S0-6b, S0-7, S0-9, S0-12, S0-14 passed; S0-11 and S0-13 yes; S0-15 yes on the Code side | Reduce to results. |
| L87 | Input `cowork-capabilities.md` | Cowork findings; later. |
| L89 | Acceptance: explicit yes or no for S0-12, S0-14, S0-15 | Answered. |
| L125 | `leases.json` written "where reachable" | Always reachable on the Code side. |
| L212 | `build-loop.md`: "on S0-15 failing asks the one cross-client question" | Remove the branch. |
| L247 | Agent fallbacks "if S0-5 or S0-6b failed" | Remove. |
| L254 | Archive "(S0-13)" manual steps | Keep the manual-steps behaviour for `gh` absent; drop the probe name. |
| L266 | README "states the S0-12, S0-14 and S0-15 results" | State them as facts. |
| L333 | `agents/*` proof "S0-5 and S0-6b fallbacks stated" | Remove. |
| L336 | `tests/stage0/*` listed repo-only | Keep the results file. |
| L500 | T9 "where S0-15 passed and otherwise by the one question" | Read `leases.json`; drop the question. |
| L549 | Conflict 9, WP-S0 added as first package | History. |
| L357, L520, L531 | Cowork smoke layer, "Claude Code and Cowork", release check 12 | Later. |

### 6.6 Other HANDOFF section 7 items that touch plan lines

- Python 3.11 is not installed on the Mac; the plan requires 3.9 and 3.11 at L125, L299, L352, L521.
- The lint's personal-name check is inert until the name index exists (L291).
- `leak_lint.py --terms` over `shared/` and the fixtures runs once WP4 lands (L307, L527).
- Where client records live and where per-user local settings live (L96, L193, L264, WP2 `init`).
- The fixture fix pass follows 1b, and WP5 cannot be accepted before it (L307).

---

## 7. Agnostic sweep hits

Nothing is fixed here. Each row is a line and a few words. The handle, the workspace name, the id and the proper names are not written out; "the handle" and "an account id" stand for them.

### 7.1 A GitHub handle

| Line | Words |
|---|---|
| L88 | S0-13 sentence, "signed in as" followed by the handle. Present when I read it; now rewritten to "the user's GitHub account". |
| L520 | Release check 1, "`gh auth status` names" followed by the handle. I read this line only after the outside edit. The file grew by exactly the size of two such rewrites (32 bytes), which fits L88 plus L520. |

### 7.2 A monday account, workspace or id

| Line | Words |
|---|---|
| L17 | A11-1 row: a named demo workspace, its eight-digit id (now a placeholder) and "on the user's current monday account", kept as "the status quo". |
| L116 | `sandbox-accounts.txt` "carries the workspace named under [A11-1]" and "the user's own operational account ids marked `never-demo`": account ids in a shared file. |
| L297 | WP17 reads "the `never-demo` ids in `shared/sandbox-accounts.txt`". |
| L131 | Fixture built from earlier recorded reads of one account: "58 of the 67 boards"; nine "re-captured live". |
| L139 | Counts from one probed account: "67 boards across 19 workspaces", 26 CRM and 27 Service natives. |
| L141, L142 | "the account's flagship natives have broken chains"; "the renamed native Accounts board". |
| L545 | Conflict 5: "The live run classified 67 boards across 19 workspaces". |

### 7.3 An earlier or other plugin

| Line | Words |
|---|---|
| L88 | S0-11 "is the old plugin disabled". |
| L109 | "no entry is written from a learn file". |
| L117 | WP1 bullet 11: "the quarantined learn files". |
| L277 | `tests/README.md` "states that the old plugin must be disabled first". |
| L484 | "the old plugin's territory" prompts, and "with the old plugin disabled". The same line names "monday's official plugin territory", another plugin. |
| L520 | Check 1 names the old plugin by its product name. |
| L527 | Check 8: "the quarantined learn files". |

### 7.4 Earlier work and the real-call calibration

| Lines | Words |
|---|---|
| L3 | Revision note: "the real-call calibration (`REAL-CALL-LESSONS.md`)". |
| L5 | "Where the calibration reversed a rule the first revision of this plan had written in". |
| L103, L107, L305, L307, L364, L381 | `REAL-CALL-LESSONS.md` named as the source of rules and fixture parameters. L383 has a "Lessons row" column. |
| L117, L306, L307, L381, L527 | "from a real call", "real-call content": sentences about what must not appear, which refer to the calls. |
| L421 | "the … chain, s1 then s3 then s10, which is three real calls" (and a proper name; see 7.6). |
| L443 | "calibrated against three real calls". |
| L547 | Conflict 7: "Replaced by the ten real fixtures". |
| L3, L5, L7, L19, L26, L35, L44, L70, L103, L107, L109, L117, L161, L200, L267, L275, L277, L302, L306, L307, L364, L371, L381, L410, L417, L421, L527, L529, L537, L546 | The word "calibration" (calibration fixtures, calibration questions, calibration keys). It names the real-call calibration. The planner may rename the fixture class. |
| L74, L76 | "Three sequencing defects this round found and fixed"; "Four schedule splits". |
| L119 | "as revised twice". |
| L162, L306 | "the buildability check found…". |
| L314 | "The rise from 96 is the sixteen files the second revision added". |
| L338, L340, L342 | "in the previous revision"; "found this round"; "found by the buildability check". |
| L537–L557 | All of section 6: the history of conflicts, "No row is live". |

### 7.5 An earlier setup

| Lines | Words |
|---|---|
| L103 | Inputs `live-tests/gotchas-draft.md`, `live-tests/native-boards-report.md`, `results/native-board-rules.json`, `results/identification-rules.json`. |
| L131, L260 | `results/…json` files cited as inputs. |
| L283 | `live-tests/manifest.json` as an input. |
| L131 | "before the ring rolls around 2026-10-01": a date that has passed. |
| L277 | "the scratch build scripts in `fixtures-work/`". |
| L87 | Input `cowork-capabilities.md`. |
| L123, L125, L406, L462, L550 | `client/1` record and `migrate`: an earlier record schema. |
| L364 | An absolute path under the user's home folder to the fixtures workspace: it carries the machine account name. |

### 7.6 A named person or a firm other than the publisher

| Line | Words |
|---|---|
| L421 | A proper name for the s1, s3, s10 chain (a client or a firm). |
| L370 | A named third-party accounting product in s1's row. |
| L484 | A placeholder firm name in the prompt "log my call with …". |
| L193, L429 | "a named seat at our own domain": publisher voice ("our"). Also "our side" and "ours" at L200, L277, L371, L373, L389, L395, L410, L433, L461, L472. |

A scan of capitalised words found no other proper name in BUILD-PLAN.md.

### 7.7 Not hits, and one to decide

- L17, L89, L284, L489, L500, L526 say "the account named under [A11-1]". That is a placeholder for an open decision.
- L19 and L277 (last clause) state the rule against real client data.
- L291 names the word "consultant" as a lint target, which is a rule.
- To decide: the default `MMB_HOME` is `~/DelOps` (L66, L88, L125, L210), a folder named for the publisher. A20 fixes it for v1, but the standing rule says anything specific to one user belongs in local settings (section 9).

---

## 8. File ownership (section 3) and conflicts (section 6)

### 8.1 Owner lines that name a v2 or v2-or-v3 file (L316–L336)

| Line | Owner line | What is deferred inside it |
|---|---|---|
| L319 | `shared/*` (9) to WP1 | `sales-method.md` and `house-style.md` (v2). The proof column lists "the voice specification" (v2). |
| L324 | `scripts/sop_tools.py` to WP6 | The whole row (v2-or-v3). |
| L325 | `scripts/demo_check.py` to WP17 | The whole row (v2). The proof names the `never-demo` refusal, a rule ROADMAP lists for v1. |
| L326 | `scripts/archive_check.py` to WP12 | The file is v1-core, but its owner is mostly deferred. Consider a v1 close-out owner. |
| L327 | Four render assets to WP6 | The whole row (v2-or-v3). |
| L328 | `templates/**`, the rest (39), to WP7 | `demo-script.md`, `recap-draft.md`, `claims-ledger.md` (v2) and the SOP cover (v2-or-v3). The row lists no file names, so the cut has to be written into it. |
| L329 | `engagement`, `call-intake`, `discovery-check` to WP8 | `discovery-check` and two of its references (v2); `summary-and-recap.md` is split. The proof column lists v2 tests (H18, H33). |
| L332 | `demo-script`, `client-sop`, `client-closeout` to WP12 | Two of three skills are deferred. The proof lists H16, H17, H51, H52, H55 (deferred) with H19, H36, H37, H56. |
| L333 | `agents/*` to WP11 | `sop-drafter.md` (v2-or-v3). The proof says "S0-5 and S0-6b fallbacks stated" (A20). |
| L336 | Repo-only list | `tests/fixtures/runsheets/` (WP17, v2); `tests/stage0/*` (WP-S0, complete). |
| L342 | Claims store writers | `engagement` creates it and `call-intake` writes to it (both v1 skills); `demo-script` writes to it (v2). |
| L314, L557 | 115 rows, 111 installed files, ten scripts, 43 templates | Every count changes with the cut. |

### 8.2 Ownership slips that do not depend on tier

- H30 and H31 appear in no package's list; they occur only at L413, L415, L454 and L455 and inside check 6's ranges (L525).
- H09 is listed for WP9 (L223, L330) but tests `discovery-check`, a WP8 skill.
- H36 and H37 are listed under both WP2 (L125) and WP12 (L332); H56 under both WP8 (L200) and WP12 (L332); H39 under WP3 (L147) and WP9 (L223); H24 to H26 under WP3 and WP10 (L147, L239). H19, which tests release and condense, is listed under WP12 (L332).
- H47 cites "H03's s2 grade" (L471), but the row at L430 runs s2, s5, s4, s1, s3, so H03 is s5 and s2 is H02.

### 8.3 What the re-cut must keep consistent with ARCHITECTURE

| Item | BUILD-PLAN lines | Note |
|---|---|---|
| File counts and the file map | L314, L557 | A§2 and A§5.4 carry the same counts and the script budgets. Cutting WP6, WP17 and the demo and SOP skills changes both. |
| Script line budgets | L550, L557 | `demo_check.py` and `sop_tools.py` leave; `transcript_prep.py` loses `delivery`. |
| Blueprint sections | L193, L555 | Sixteen numbered sections with `client-view` cutting 1 to 15. New content (AI-offering sections, a "what this build rests on" part) must sit inside them, or both documents change the count. |
| Lease | L342, L554 | Primitives in `mmb_common.py` and the two mirrors. Any simplification changes A§9.8 and A§5.4 as well. |
| `ledger.py bind` | L552 | A§5.4 and A§8.2 step 5. |
| Call-type vocabulary home | L553 | Trimming the sales fields changes A§8.3 step 5 and A§7.1, and the embedded copy in `transcript_prep.py` and the lint assertion (L291). |
| Retention default | L544 | `unanswered`, A§7.2. |
| Automations as one approval | L541 | A1; A§9.5, A§3.7, A§9.1. |
| Detection by measurement | L546 | A§5.4. |
| Native rule names | L551 | `N0` to `N12`; A§0 and A§11.2. |
| Gotcha numbering and budget | L542, L543 | G-91 onward; 460 lines; A§10.2. |
| A16 pieces | L556 | Inputs, `document` subcommand, `[Q/doc]`. |
| Stage list and WP-S0 | L549 | A§13. |
| Tag tables of section 0 | L17–L19, L30–L33 | Each tag lists the packages and tests that carry it. [L17] and [L18] go with the demo layer, and the lists have to be recomputed after the cut. Release check 10 (L529) reads the same tags. |
| New text | none in this file | A19 and A20 have to be folded into ARCHITECTURE. A17 asked for a design pass over both documents for the AI kinds, and none is visible in BUILD-PLAN. |

### 8.4 Section 6 itself

The intro says no row is live (L537). Rows 5, 7 and 8 describe earlier revisions of the plan (L545, L547, L548). Rows 1 to 4, 6 and 9 to 16 are folded into the architecture and kept as a record; row 17 records count and budget changes. Under the agnostic rule the section is history of earlier work and has no place in the re-cut. If a section 6 stays, its rows should be the new conflicts: the readiness check against `discovery-check`; the AI element kinds against the architecture's exclusion list; A20's single surface against the two-surface text.

---

## 9. Open questions for the planner

### 9.1 Shape of the v1 main line

1. **AI offerings.** Is this one new package after audit, or additions across WP1, WP3, WP4, WP7, WP9, WP10, WP13 and WP15 in order? BUILD-PLAN has no text on the AI kinds at all (agents, AI columns, Vibe apps, Workflows, sequences, webhooks), so this is new writing and not tier marking. The one-owner rule (L312) and the five-way parallel stage 4 (L72) decide which shape works.
2. **Stage placement.** ROADMAP puts the AI-offering element kinds in stage 4 beside the skills (ROADMAP L62). A19 says blueprint, build, audit, then AI offerings (A19 L25). One stage with an internal order, or two stages?
3. **What "show" means in v1.** A19's objective ends in a "functional demo", and the v2 list removes run-sheets and the close. Yet `version.md` still carries `demo_script_ready` (L193), the gate list still has "First demo (v0.1)" (L107), and the readiness line says "cleared to show". What stays of "show", and which record fields hold it?
4. **Where v2 files live.** `sales-method.md`, `house-style.md`, `demo-script.md`, `recap-draft.md` and `claims-ledger.md` are "files kept, no skill built". Do they stay in the plugin tree (and in the always-on token count, check 5, and the lint), move to a v2 folder, or leave the repo?

### 9.2 The readiness check

5. **Home.** Inside WP8 or a package of its own (5.2).
6. **Verdict words.** The brief says "cleared to build" and "cleared to show"; the sibling spec says `cleared to build`, `cleared to build, generic` and `not yet`. Where is "cleared to show" said, if at all (5.3 item 5)?
7. **Evidence law.** The non-evidence list, the A16 document rules, the narrowed conflict rule and the side-only evidence rule live in `sales-method.md` and `rubric.md`. Where are they pinned for v1 (5.3 item 7)?
8. **The consumer.** Should WP9's acceptance say `solution-blueprint` reads the clearance and logs an override, as ARCHITECTURE A§3.4 does? Does `account-build` check it too (A§3.7 stop conditions)?
9. **`gaps.md`.** Its states read as demo states. Keep it as the register of client asks for blueprint planning (L210), or use it for readiness gaps?
10. **Call-type header.** Which of the six fields and thirteen labels does intake still propose in v1 (6.2)? The two-attendee token (6.4) and `direction_of_show` (6.3) fall out of the same decision.
11. **`delivery` and the voice bank.** Drop the subcommand only, or also the `intake-report/1` fields that feed it (voice-bank eligibility and tier, L172) and the MAINTAINING step (L268)? The report schema is pinned in stage 1, and the summarizer agent reads it (L247).

### 9.3 Surface and safety

12. **Briefing a client-folder session.** Records at `~/DelOps/clients/<client>/` inherit the development `CLAUDE.md` (HANDOFF section 7). The interview notes list three fixes: records outside the development folder, the development workspace moved, or development instructions that stand down. WP0's no-`CLAUDE.md` rule (L96) covers the repo only, and `project-instructions.txt` (L193) is surface-later. How does a client session get its instructions in v1?
13. **Default home.** `MMB_HOME` defaults to `~/DelOps` (L66, L88, L125, L210), a folder named for the publisher. A20 fixes it for v1. Keep it, or ship a neutral default with the user's value in local settings?
14. **The wall between clients.** A20 makes the leak lint the wall (A20 L13). WP4 has no cross-client check. Should it compare a payload with other clients' vocabulary, using hashes the way `clients-index.json` does (L291)?
15. **`never-demo` accounts.** They are in ROADMAP's v1 list (ROADMAP L33), but the plan homes them in WP17 (v2) and in `sandbox-accounts.txt`. Which v1 component enforces them (`ledger.py bind`, the hook, the account check)? And where do the ids live, given that account ids stay out of project files (L116)?
16. **Lease scope.** The interview (Q8) suggests a within-record guard plus one question, because the user builds for one client at a time. The apparatus is in WP2 (L125), WP3 (L135), WP9 (L212), WP13 (L264), H22, H35, T3 and T9. This is interview input, not a decision.
17. **Claims store.** v2, or a thin v1 that keeps "nothing is promised that is not built"? `engagement` creates it (L200), `call-intake` writes to it, `solution-blueprint` reads it (L210), `demo-script` writes to it, and the seed `home/` carries it (L275).
18. **Docs as an element kind.** A18 lists docs. If a v1 build writes docs, `doc-chunks` and T18 stay and WP6 splits. The interview's notes document with a text flowchart (Q12 addition) needs no rendering tools. `doc-copy.md` (L212) is the SOP copy and stays deferred.
19. **`research-scout`.** The interview (Q2) says the user wants it, running after the first build; A19 does not place it. Tier and stage? H01 "no research" (L429) and H29 (L453) touch it, and the sibling spec reads a research brief when one exists.

### 9.4 Tests and release

20. **Check 8.** Which of the three shapes in section 4?
21. **`sync_shared.py`.** S0-1 passed, so does it go, with its lint clause (L66, L291)?
22. **`migrate`, `client/1` and H38** (L123, L125, L406, L462). No earlier record exists. Keep, or drop as a reference to an earlier schema?
23. **Fixtures.** s10 and s21 are mostly v2; keep them as v1 fixtures for their residue? Does the fix pass add a readiness expectation to every key? HANDOFF fixes the order as 1b, then one fix pass, then one verification, and WP5 waits on it (L307).
24. **Test ids.** Keep the H and T numbering with deferred rows marked, or renumber? Assign H30 and H31. Check 6 names ranges that include v2 tests (L525). Three runs of 56 ids is 168 runs.
25. **Python 3.11.** Required at L125, L299, L352 and L521; the Mac has 3.9.6 only. Install it or relax the check.
26. **PDF text.** WP5 `document` reads PDFs "through `pdftotext` when present" (L178), and this Mac has none. Accept `unknown` text, or let the model read the PDF pages?

### 9.5 Interview inputs that touch plan lines

These are inputs in `INTERVIEW-NOTES.md`, not decisions.

| Interview note | Touches |
|---|---|
| Q2: a time budget for the first demo and a fast first-build path; research after the first build | New text for WP8, WP9 and WP11 |
| Q3, Q16: the first build is a whole workspace with sample data; the AI layer is never optional | T1's scale (L492); the sample-data rules [A11-2] (L18) |
| Q5: the blueprint carries an AI-opportunities section; boards first, AI second unless asked | `blueprint.md` (L193) inside the sixteen-section rule (L555) |
| Q7 and its clarification: an email is a further input class; thin input generalises the build | WP5, WP8 `transcripts.md`, `record.py add-*` (L125) |
| Q8: one workspace per client named after the client; lease simplification | WP2, WP3, WP9 |
| Q9: one workspace per product with cross-product automations, a probe needed | WP9 build order, WP15 probes |
| Q10, Q11: a first-run walkthrough; folder setup A | WP8 `new-client.md` (L200) |
| Q12 addition: one living notes document per client with a text flowchart | WP7 templates (L193), WP6 `diagrams` |
| Q13: a pivot is a fresh build; old workspaces are not archived at once | WP12 close-out, WP9 `changes-removals.md` |
| Q14: sample data from the client's real world, with an exclusion list | WP7, WP9, WP4 |
| Q4, Q6: approvals stay as designed | none |

---

## Summary

Twenty packages: nine v1-core (two of them complete), one v2, one v2-or-v3, nine split. Most splits are clause-level inside single-paragraph acceptance lists (L193, L200, L254, L277). The plan has no text at all on the AI offerings or on a readiness check, so the v1 main line needs new writing as well as cuts. Stage-0 references (section 6.5), release checks 1, 8 and 12, and the files that carry account ids or an earlier plugin's name are where the sweep and A20 bite hardest.
