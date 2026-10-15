# Map of ARCHITECTURE.md for the stage 1b re-cut

Status: complete. All 1,307 lines of the source were read. The source file's modification time changed twice during the run, at 03:08 and 03:14. The first change replaced the GitHub handle with neutral wording at several lines. The second left the byte size unchanged. Line numbers did not move. I re-verified every heading range, and a sample of cited lines, against the file as it stood at the end.

This file maps `rebuild-workspace/design/ARCHITECTURE.md` (1,307 lines) against amendments A20, A19, A18 and A17 and against `ROADMAP.md`. It edits nothing in the source. It is input for the editing run that re-cuts the document.

How to read it.

- A range runs from a heading's own line to the line before the next heading, so it includes the closing rule. Three heading-looking lines at L655, L658 and L1019 sit inside code fences. They are example text and are not in the inventory.
- Tiers are v1-core, v2, v2-or-v3, split and unclear, as A19 and A18 define them. "Surface" means A20.
- "A19 kept" means the A19 rule for v2 items: file kept, no skill built. For v2-or-v3 items A19 says deferred and does not say kept, so the column says "deferred" for those.
- Cites are source line numbers, written L123 or L120–L140. Quotes are never longer than one sentence.
- The map names no person, firm, workspace or account. It says "the handle" for a GitHub handle and "an account id" for an id.

---

## 1. Section inventory

Every `##` and `###` heading. The title line is listed first. Gist is one line.

| Heading | Lines | Gist |
|---|---|---|
| `#` Title block | L1–L4 | Title and revision note; says which amendments were folded in and points to the spec, build plan and amendments. |
| `## 0` Base, grafts and how to read this | L5–L31 | Proposal B as base, C's chassis grafted on, the graft table, evidence tags, gotcha id scheme, clean-room statement. |
| `## 1` Design principles | L32–L43 | Seven principles: record is memory, two doors for risk, approve content, stored state, live facts, client-facing lane, short instructions. |
| `## 2` Plugin layout | L44–L172 | Repo tree naming every shipped file, the file count (111) and what deliberately does not ship. |
| `## 3` Skills | L173–L174 | Heading only. Ten skills follow in 3.1 to 3.10, with conventions in 3.0. |
| `### 3.0` Conventions for every skill | L175–L184 | Frontmatter limits, reserved names, body shape, state-first rule, base-name tools, data-not-instructions, chaining. |
| `### 3.1` `engagement` | L185–L195 | Front door: briefing from the record, routing, new client and account binding, strands, research, versions. |
| `### 3.2` `call-intake` | L196–L206 | One very long paragraph (L203) turning calls, packages and client documents into the record, plus recap, delivery notes, claims and voice-bank marks. |
| `### 3.3` `discovery-check` | L207–L217 | The sales rubric: per-pain checks, R1 to R12, verdict, five gates, conflict rules, gap questions (L214 is 7,900 characters). |
| `### 3.4` `solution-blueprint` | L218–L230 | Blueprint design, required sections, change tables, allowlist, estimate, approval card and freeze. |
| `### 3.5` `demo-script` | L231–L253 | Run-sheet for meetings the user leads: prep block, budgets, check-ins, close, claims in speech. |
| `### 3.6` `client-sop` | L254–L262 | Progressive SOP drafting from a client-safe bundle, export tiers, hand-off to the doc copy. |
| `### 3.7` `account-build` | L263–L272 | The write door: change check, preflight, ordered build, ledger, one automations list, resume, doc-copy, sample-cleanup. |
| `### 3.8` `solution-audit` | L273–L282 | Independent read-only audit with before and after snapshots and write detection. |
| `### 3.9` `client-closeout` | L283–L292 | Strand close, record close, ownership review, live-map promotion, archive on the Mac. |
| `### 3.10` `monday-drift-check` | L293–L302 | Roster and schema diff, probes, overlay updates, sandbox-only write probes. |
| `### 3.11` Listing cost | L303–L306 | Size of the model-invocable descriptions and the always-on token target. |
| `### 3.12` The voice specification | L307–L314 | `house-style.md`: register, DO and DON'T lists, per-speaker profiles, regeneration as a release step. |
| `## 4` Agents | L315–L329 | Four optional agents in one table: restrictions, model, input, return, fallback. |
| `## 5` Scripts, runtime and where everything runs | L330–L331 | Heading only. |
| `### 5.1` Where things run [cowork] | L332–L341 | Table of the device shell, the cloud shell and Code on the Mac; probe S0-4 for rendered files. |
| `### 5.2` How a skill reaches a script | L342–L349 | The ladder: plugin path, else a sha-checked copy into `.work/tools/`, else fail closed. |
| `### 5.3` Script rules | L350–L358 | Standard library only, no deletes, flat front matter, exit codes, `--expect-sha`, the `MMB_HOME` root. |
| `### 5.4` Script catalogue | L359–L377 | One row per script with size, subcommands and ownership; the intake report schema (L367). |
| `## 6` Templates | L378–L385 | Notable templates and what each carries. |
| `## 7` The client record | L386–L389 | Heading and ownership note: `shared/record-map.md` owns the section. |
| `### 7.1` File map | L390–L461 | Kinds and budgets; record-level table (L398–L416) and strand-level table (L420–L446); the four strand files (L450); reading contract (L452); call-set fields and thirteen call labels (L454); `.work/` contents (L456); paths outside the record under `MMB_HOME` (L458); naming (L460). |
| `### 7.2` `CLIENT.md` front matter | L462–L500 | Schema `client/2` fields: binding, tier, products, record state, lease mirror, the three open A11 fields, page size, AI notice; body blocks and their single owners. |
| `### 7.3` `account.json` and `build.json` | L501–L603 | Two ledgers: the record-level account file and the per-strand build ledger; element key vocabulary and status transitions (L602). |
| `### 7.4` Version states | L604–L630 | Versions belong to the strand; state machine planned to released with required files; v1.0 release rule (L629). |
| `### 7.5` Evidence markers | L631–L647 | Eight markers with a "counts toward the rubric" column; the citation contract and its refusals. |
| `### 7.6` `log.md` | L648–L664 | Log format, entry header, entry types, roll at strand close. L655 and L658 are example text inside a code fence. |
| `### 7.7` `STRAND.md`, `SUMMARY.md` and strand kinds | L665–L701 | Strand front matter (kind, output class, stage, version state, verdict, SOP behind), strand kinds, SUMMARY rules, strand states. |
| `### 7.8` `live/live-map.md` | L702–L731 | Live-map fields, the three constraint values, how blueprint and audit honour them, interim values at run end. |
| `### 7.9` Non-platform strands | L732–L743 | What a non-platform strand holds and never has, the fixed hand-off sentence, hybrid strands (A13). |
| `### 7.10` Migration from a single-engagement record | L744–L749 | `client/1` to `client/2` migration steps. |
| `## 8` Key flows | L750–L751 | Heading only. |
| `### 8.1` Every client chat | L752–L760 | Locate the record, status, eight-line briefing, routing, chat boundaries (A10). |
| `### 8.2` New client and account binding | L761–L769 | Six steps: slug and shell, setup questions, instructions paste, binding, ledger bind, admin checklist and research. |
| `### 8.3` Call intake | L770–L783 | Seven steps (L772–L778), the call set (A15, L780) and the client document (A16, L782). |
| `### 8.4` Discovery check | L784–L787 | The grading flow: per pain, R1 to R12, verdict, five gates, stakeholders, gap questions, override. |
| `### 8.5` Blueprint, approval and freeze | L788–L800 | Steps 1 to 8: gate, product fit, account read, draft, allowlist and term read-back, approval card, hedged replies and forks, freeze. |
| `### 8.6` Change check, preflight and build | L801–L816 | Steps 9 to 21 (numbering continues from 8.5): guard, recovery, lease, account check, change check, preflight, re-confirm, build order (L810), write loop, errors, irreversible steps, automations, end of run. |
| `### 8.7` Audit | L817–L826 | Steps 22 to 28. |
| `### 8.8` Demo, SOP and release | L827–L833 | Steps 29 to 32: demo-script, client-sop, doc copy, release. |
| `### 8.9` Iteration | L834–L839 | Delta versions inside a strand; a new strand is not a delta. |
| `### 8.10` Close-out | L840–L845 | Strand close and record close; archive and cleanup on the Mac. |
| `### 8.11` Recovery after an interruption | L846–L853 | Reconcile classes; sibling-strand recovery. |
| `## 9` Safety model | L854–L857 | Heading and ownership note: `shared/safety.md` is the one home. |
| `### 9.1` Authority table | L858–L877 | Table of actions, who may do them, where, and the gate. |
| `### 9.2` Approvals | L878–L881 | Only the user's own message counts; nothing carries across chats. |
| `### 9.3` Account binding | L882–L885 | The single binding query, the cadence of account checks, mismatch handling. |
| `### 9.4` Irreversible operations in v1 | L886–L906 | Table of operations that cannot be undone and their handling (L890–L903); the v1 exclusion list (L905). |
| `### 9.5` Automation approvals | L907–L916 | One approval for the whole list; grouped re-confirmation at execution; no API switch-off; the row card. |
| `### 9.6` Leak lint | L917–L928 | Where the lint runs, what it blocks, the trap shapes, the SOP exemptions, fail-closed, the cross-client check. |
| `### 9.7` Audit write detection | L929–L934 | Before and after snapshots, their scope, tester writes. |
| `### 9.8` Concurrency and the contended build lease | L935–L952 | Per-record lease with epoch fence, minted chat label, cross-client rule, holder discovery, release, stale lease, break. |
| `### 9.9` Quota, plan tier and ownership | L953–L956 | API-call estimate and headroom; owners and automation ownership. |
| `### 9.10` Hooks | L957–L968 | Three PreToolUse matchers routed to one script; native-board protection by id; defence in depth only. |
| `### 9.11` Confidentiality exposure during delivery | L969–L982 | Shared-screen rules, demo environment, how access is requested, credentials never handled, client-driven screens. |
| `### 9.12` Claims discipline | L983–L998 | The claims store, the prep read, in-speech rules, audience routing, if-asked list, correction loop. |
| `## 10` monday knowledge and drift | L999–L1000 | Heading only. |
| `### 10.1` Where a skill gets a fact | L1001–L1011 | Six-step order of authority. |
| `### 10.2` The gotcha list | L1012–L1031 | Gotcha file size and format, status vocabulary, the never-say block (L1030). L1019 is example text inside a code fence. |
| `### 10.3` The knowledge overlay | L1032–L1037 | Overlay folder outside the plugin, three rules, fold-back into releases. |
| `### 10.4` Read-back table | L1038–L1041 | The read that proves each write kind, with blind spots. |
| `### 10.5` Drift handling | L1042–L1047 | Per-check and scheduled drift routine; dated watch. |
| `## 11` Native CRM and Service objects, portfolios and projects | L1048–L1053 | Implements A5, A6, A7; sources and how the two rule sets compose. |
| `### 11.1` What the API does and does not tell us [live] | L1054–L1074 | Live findings on nativeness, lineage, portfolios, projects, dashboards, cost. |
| `### 11.2` Three layers | L1075–L1080 | Detect, guard, verify. |
| `### 11.3` Portfolio and project work | L1081–L1094 | The portfolio default and the build rules from the live run. |
| `### 11.4` Service in v1 | L1095–L1106 | Entity set, detection, portal, build and audit, deferred extras. |
| `## 12` Decision log | L1107–L1108 | Heading only. |
| `### 12.1` Critic contradictions | L1109–L1139 | Table of 26 rows (C1 to C29, some paired). |
| `### 12.2` Critic gaps | L1140–L1163 | Table of 19 gaps and their status. |
| `### 12.3` Decisions made, and defaults | L1164–L1171 | The user's decisions (D2 to D24), the three reopened by A11, defaults D1 to D27 (L1170). |
| `### 12.4` Amendments | L1172–L1192 | How A1 to A16 landed; no rows for A17 to A20. |
| `### 12.5` Judge dealbreakers | L1193–L1205 | Dealbreakers raised against proposals A, B, C and the fix for each. |
| `### 12.6` Live findings that changed a decision | L1206–L1226 | Table of live findings and what each changed. |
| `### 12.7` Calibration findings that reversed a round-one rule | L1227–L1246 | Table of round-one rules reversed by the real-call calibration. |
| `## 13` Pending items and safe defaults | L1247–L1270 | Three open A11 decisions (L1251–L1259), calibration questions (L1261), Cowork runtime probes S0 (L1263), monday probes P (L1265), the user's own steps (L1267). |
| `## 14` Deferred to v1.x, and risks | L1271–L1307 | Deferred list (L1273) and a 30-row risk table (L1275–L1306). |

---

## 2. Tier per subsection

A unit is a `###` subsection, or a `##` section that has no subsections. Sections that only hold subsections (3, 5, 7, 8, 9, 10, 11, 12) are not tiered themselves. That gives 73 units: v1-core 39, split 26, v2 5, unclear 2, v2-or-v3 1.

A unit is marked split when a separable part of it is v2 or v2-or-v3: a whole paragraph, bullet, numbered step, table row or column, or a run of clauses that make up one feature (L203 is a single paragraph built of such runs). A unit with only a stray phrase of that kind keeps its main tier, and the touches are named in the reason.

| Unit | Lines | Tier | Reason, and what is v2 or v2-or-v3 inside a split |
|---|---|---|---|
| `## 0` Base, grafts, how to read | L5–L31 | split | v1-core: base choice, the front door, approval, audit, runtime, size, leak-lint and test-asset grafts (L11–L22), evidence tags (L24), gotcha ids (L26), clean room (L28). v2: the "Method depth and drift" row (L21) names rubric depth, delivery notes and recap status. v2-or-v3: the "Export" row (L18). Surface: L9, L16 and the [cowork] tag at L24. |
| `## 1` Design principles | L32–L43 | v1-core | All seven principles hold in v1. Principle 6 (L40) names the SOP drafter, a v2-or-v3 phrase; principle 4 (L38) mentions client-facing exports. |
| `## 2` Plugin layout | L44–L172 | split | Tree rows, by line. v2: `sales-method.md` L66, `house-style.md` L67, `discovery-check/` L88–L93, `demo-script/` L115–L119, `demo_check.py` L147, `recap-draft.md` and `prep-sheet.md` L154, `discovery.md` L155, `gaps.md` L156, `demo-script.md` L157. v2-or-v3: `client-sop/` L120–L124, `doc-copy.md` L109, `sop-drafter.md` L138, `sop_tools.py` L148, `SOP.md` and `flow-spec.json` L157, `export-manifest.md` L159, `mermaid-config.json`, `puppeteer-config.json` and `sop-reference.docx` L160. Surface: L52, L60, L129, L158. File count at L169 changes. |
| `### 3.0` Conventions | L175–L184 | v1-core | Applies to every skill that is built. L177 cites Cowork and claude.ai uploads (surface); L178 reserves the old plugin's names (agnostic). |
| `### 3.1` `engagement` | L185–L195 | v1-core | Front door stays. v2 touches in the briefing line (L192): discovery verdict and open gaps, SOP behind, overdue commitments. Surface: "the Project's connected folder" (L192). Research at three depths (L189, L192) is not named in A19; see part 10. |
| `### 3.2` `call-intake` | L196–L206 | split | All in L203 unless noted. v1-core: date, type and attendees; roster rules; package as a set; client document intake with the `documented` marker; non-English stop; the A11 transcript question and redaction; `add-transcript`; the pipeline; alias table; summariser delegation; quote verification; the calls file with type header, strand tag, what the transcript cannot see and quarantined spans; `structure-inventory.md` on a reverse demo or prototype review; backlog seeds; STRAND, CLIENT and log updates. v2: the recap draft (L200, L203), delivery notes, the restated-and-unanswered objection, voice-bank marks, the five-item short check on support and check-in calls, the claims-store writes, third-party claims, `gaps.md` and the confirmation ledger after a demo, the live-change inventory on a demo, the register of deferred answers. v2-or-v3: the "For the SOP" part of the client-safe block. Unclear: commitments turned into owned dated items; the call-type header (see part 10). |
| `### 3.3` `discovery-check` | L207–L217 | v2 | The whole skill is the sales rubric. Carry-overs that build-readiness may reuse: cross-call conflicts kept side by side (A15, L214), the document-evidence rules (A16, L214), the platform-consumption design input (A17, L214), the strand `kind` and `output_class` reading (L214), "not obtainable from this room" role routing (L214). |
| `### 3.4` `solution-blueprint` | L218–L230 | v1-core | Mostly stays. v2 clauses in L225: check the blueprint gate and log an override; read the claims store; read `gaps.md` and plan the most-repeated ask. L227: "platform consumption" points at `discovery.md`, a grading file. Also L227 "before the first demo segment". No AI element kinds in the section list (part 7). |
| `### 3.5` `demo-script` | L231–L253 | v2 | The whole skill: run-sheet, scoping run-sheet, countable budgets, check-ins, close, claims in speech. |
| `### 3.6` `client-sop` | L254–L262 | v2-or-v3 | The whole skill. The export tier choice (L261) leans on the cloud shell and the preinstalled docx and pdf skills. |
| `### 3.7` `account-build` | L263–L272 | v1-core | v2-or-v3 inside: the `doc-copy` mode (L267, L271). `sample-cleanup` stays (the cleanup). "Automations are built last" (L271) has to become "AI offerings after automations" under A17 (part 7). The cross-client lease stop (L271) is a target of the lease simplification (part 9, item 6). |
| `### 3.8` `solution-audit` | L273–L282 | v1-core | One v2 phrase: "the blueprint gate" reported beside the verdict (L281). |
| `### 3.9` `client-closeout` | L283–L292 | v1-core | Matches A19's close-out. Small v2-or-v3 piece: confirming the final package was handed over (L287). Unclear: the one-page client card (L287). Surface: two surfaces and the Cowork-to-Mac split (L291). |
| `### 3.10` `monday-drift-check` | L293–L302 | v1-core | Change check and overlay (A3, A4). The sandbox-accounts file (L301) touches the open A11 test-account decision. |
| `### 3.11` Listing cost | L303–L306 | v1-core | Needs a recount after the re-cut; the figure assumes six model-invocable skills. |
| `### 3.12` Voice specification | L307–L314 | v2 | The whole subsection is the house voice. L311 reports measurements from real calls. L311 also routes regeneration to Code on the Mac, a surface remark. |
| `## 4` Agents | L315–L329 | split | Rows: `transcript-summarizer` L321 v1-core; `solution-auditor` L322 v1-core; `sop-drafter` L323 v2-or-v3; `research-scout` L324 unclear (research is in the record by A14 but not in A19's list). L326 view-only user for the auditor (pending P-12). |
| `### 5.1` Where things run [cowork] | L332–L341 | split | Device shell row L336 and Mac row L338 are needed but restated for a single Mac shell. The cloud-shell row L337 and the S0-4 paragraph L340 serve rendering only (v2-or-v3) and are Cowork-only. The whole subsection is surface. |
| `### 5.2` The ladder | L342–L349 | v1-core | Needed in Code too, since the plugin path must resolve (S0-1 stays on A20's list). Steps 2 and 3 are a fallback to keep or drop after S0-1. Surface wording at L348. |
| `### 5.3` Script rules | L350–L358 | v1-core | Rules hold. L353 cites probe S0-3 (Cowork-only); L357 explains `MMB_HOME` by the device shell's separate home (Cowork). |
| `### 5.4` Script catalogue | L359–L377 | split | v1-core: `mmb_common.py`, `record.py`, `ledger.py`, `leak_lint.py`, `transcript_measure.py`, `archive_check.py`. v2: `demo_check.py` L369; `transcript_prep.py` `delivery` (L368). v2-or-v3: `sop_tools.py` L370. Unclear: `gql_guard.py` L371 (A2 says no query guard). L367 `document` stays; L364 `client-view` and `manifest` need a check. |
| `## 6` Templates | L378–L385 | split | Section 6 itself names these. v1-core: `STRAND.md`, `SUMMARY.md`, `scope.md`, `close-out.md`, `live-map.md`, `meetings.md`, `account.json`, `admin-prerequisites.md`, `document-summary.md`, `structure-inventory.md`, and `call-summary.md` without its type-header scoring. v2: the `discovery.md` additions (client-built assets, platform consumption, voices line, asked flags), the `demo-script.md` skeleton and `claims-ledger.md` (all L382). v2-or-v3: `sop-reference.docx` and the `SOP.md` cover (L382). The tree adds `recap-draft.md` and `prep-sheet.md` (v2, L154) and `export-manifest.md` (v2-or-v3, L159). Surface: `project-instructions.txt` is the Cowork Project paste (L382). |
| `### 7.1` File map | L390–L461 | split | v1-core: `CLIENT.md`, `log.md`, `account.json`, `calls/*.transcript.txt` and `calls/*.md`, `inputs/*`, `live/*`, `.gitignore`, `.work/`, and strand files `STRAND.md`, `SUMMARY.md`, `blueprint.md`, `scope.md`, `backlog.md`, `allowlist.md`, `build.json`, `open-questions.md`, `dependencies.md`, `structure-inventory.md`, `version.md`, `blueprint-r<N>.md`, `audit*.md`, release snapshots, `close-out.md`; the reading contract (L452); the call-set fields (L454). v2: `calls/*-prep.md` L409, `discovery.md` L424, `gaps.md` L432 and its description in L450, `demo-script.md` L437, `drafts/*-recap.md` L442, the who-has-seen-what block of `meetings.md` (L454), most of the thirteen call labels (L454). v2-or-v3: `export.md` L438, `sop/SOP.md` L440, `sop/diagrams/*` L441, `deliverables/<v>/*` L443, `.work` entries `sop-inputs/`, `doc-chunks/`, `render/` (L456). Unclear: `research/*` L404–L406, `client-card.md` L414, `deliverables/handoff/*` L444, the claims store `claims/<slug>.md` (L458). Surface: L458 and L460. |
| `### 7.2` `CLIENT.md` front matter | L462–L500 | split | v1-core: binding, tier, products, record state, strand count, lease mirror, A11 fields, AI notice. v2-or-v3: `page_size` (L491, asked at the first export). v2: the strand-index columns "discovery verdict" and "SOP behind" (L499); stakeholders and decision roles written by `discovery-check` (L499) need a v1 owner. |
| `### 7.3` `account.json`, `build.json` | L501–L603 | v1-core | Core of the build and safety model. Gaps for A17 and A18: the element key list (L602) and the `objects.type` values have no workflow, agent, AI column, Vibe app, sequence or webhook kinds. `SOP.doc` (L602) is v2-or-v3. The example holds real-looking numeric ids (L511–L553, L588, L659). |
| `### 7.4` Version states | L604–L630 | split | v1-core: `planned` to `audited`, `fixing`, the per-strand counter, `released` as a condense-and-freeze step. v2: the `demoed` state (L609, L624) and the v1.0 release conditions (L629: R6, R11, confirmed export, sign-off evidence). Release "after the demo intake" (L627) needs a new trigger. |
| `### 7.5` Evidence markers | L631–L647 | split | v1-core: the eight markers and the citation contract, including the refusal tier (ROADMAP L13). v2: the "Counts toward the rubric" column (L633–L642) and the grading phrases in L646 ("grading is per turn", "capped at Partial"). |
| `### 7.6` `log.md` | L648–L664 | v1-core | Format, header and roll at strand close stay. Touches in the entry-type list (L663): `discovery`, `demo`, `sent` are v2; `sop`, `export`, `doc-copy`, `deliverable` are v2-or-v3; `override` is unclear (it overrides gates, but L694 calls overrides "any"); there is no entry type for the A17 and A18 kinds. |
| `### 7.7` Strand files and kinds | L665–L701 | split | v1-core: `kind`, `state`, `depends_on`, SUMMARY rules, strand states. v2: `discovery_verdict` (L684), `sop_behind` (L685), stage values `discovery`, `demo`, `signed-off`, `expanding` (L680), the `demoed` value (L683), body block "verdict and top gaps" (L694), the "demo door" reading `output_class` (L696). Unclear: `next_step` as a dated meeting (L686); the stage ladder needs the new stage order (part 7). |
| `### 7.8` Live map | L702–L731 | v1-core | The kind list (L710) stops at portfolio and project; A17 and A18 kinds are absent. L730 points at the migration default (7.10). |
| `### 7.9` Non-platform strands | L732–L743 | v1-core | Matches A13. v2 touches: `discovery.md` in the strand (L736), `demo-script` refusal (L737), claims discipline on drafts (L739). Unclear: `deliverables/handoff/*` (L736), a client-facing hand-off package, which A19 defers. |
| `### 7.10` Migration | L744–L749 | unclear | Nothing has shipped, so no `client/1` record exists to migrate. It reads as an earlier-setup reference; candidate to drop (part 8, part 10). |
| `### 8.1` Every client chat | L752–L760 | v1-core | v2 touches in the briefing (L756): discovery verdict and open gaps, gate collision with a commercial date, SOP behind, next meeting, overdue commitments. Surface: runtime detection (L754) and "a different Project and folder" (L759). |
| `### 8.2` New client and binding | L761–L769 | v1-core | Surface: connected folder (L763) and the Cowork Project paste (L765). v2: the claims store creation (L767). Landing spot for the first-run walkthrough (part 9). |
| `### 8.3` Call intake | L770–L783 | split | v1-core: steps 1 to 4, the pipeline in step 5, steps 6 and 7 for backlog and `STRAND.md` updates, the call set (L780), the client document (L782), scoping and working-session routing (L778). v2: the seat, relationship and money parts of the type header (L776), delivery notes and recap draft (L777), routing by type into `discovery-check`, `gaps.md`, the confirmation ledger, the live-change pass, version release and SOP update (L778), pricing and call-review handling (L778), the five-item short check (L778). Unclear: the call-type header as a whole (part 10). |
| `### 8.4` Discovery check | L784–L787 | v2 | The whole flow. Carry-overs: the vocabulary map with ambiguous terms turned into questions (feeds the client term read-back, 8.5 step 5), the client-built assets and consumption sections, stakeholders and decision process, conflicts. |
| `### 8.5` Blueprint, approval, freeze | L788–L800 | split | v2: step 1 (L792), check the gate and record an override; the build-readiness check replaces it. The rest is v1-core. The approval card (L797) lists automations only; the A17 and A18 lists are absent. |
| `### 8.6` Change check, preflight, build | L801–L816 | v1-core | The build order (L810) stops at automations. Lease step (L805) is the target of part 9. |
| `### 8.7` Audit | L817–L826 | v1-core | Step 25 (L822) runs `gql_guard.py scan` on the appendix (see part 10 on A2). No per-kind checks for A17 and A18 kinds. |
| `### 8.8` Demo, SOP and release | L827–L833 | split | v2: step 29 (L829). v2-or-v3: steps 30 and 31 (L830–L831). v1-core: step 32, the release mechanism (L832), whose trigger "after the demo intake" changes. |
| `### 8.9` Iteration | L834–L839 | v1-core | v2 touch: the five-item short check (L836). Landing spot for iterate versus fresh build (part 9). |
| `### 8.10` Close-out | L840–L845 | v1-core | Matches A19. v2-or-v3 pieces: "final package was handed over" and the lint of `sop/` and `deliverables/` (L842, L844). Surface: the Cowork and Mac split (L842, L844). |
| `### 8.11` Recovery | L846–L853 | v1-core | The reconcile classes cover boards, folders, docs, dashboards and automations (L848); per-kind inventories for the A17 and A18 kinds are absent. |
| `### 9.1` Authority table | L858–L877 | split | v1-core: every row except L873. v2 and v2-or-v3: L873 (save client-facing files by `client-sop` and the recap draft). Surface: the "Where" column at L868, L869 and L875. Lease rows L865 and L867 are targets of part 9. |
| `### 9.2` Approvals | L878–L881 | v1-core | Stays as written. |
| `### 9.3` Account binding | L882–L885 | v1-core | Stays. |
| `### 9.4` Irreversible operations | L886–L906 | split | v1-core: rows L890–L897 and L900–L903. v2-or-v3: L898 (doc block deletion, only in doc-copy) and L899 (asset upload, for SOP images on the Mac). Superseded: the exclusion paragraph L905 lists published workflows, AI agents and AI columns, CRM sequences, webhooks and notifications, which A17 and A18 moved into scope. Missing rows for the new kinds. L903 conflicts with a new workspace per client (part 9). |
| `### 9.5` Automation approvals | L907–L916 | v1-core | The pattern (one list, every recipient shown, grouped re-confirmation, switch-off step) is what A17 and A18 extend to workflows, agents and sequences. |
| `### 9.6` Leak lint | L917–L928 | split | v1-core: planned names, payloads, audit names; blocked categories (L921) such as consultancy, plugin and assistant names, cost figures, copied runs, quotes, markers, ids, other clients' names; the trap-shape fixtures (L923); fail closed. v2: recap and admin checklist as `drafts/` (L919), method vocabulary, objection text, stakeholder assessments and closing tactics (L921). v2-or-v3: lint of `sop/`, rendered Word and PDF text and properties, doc-copy read-back (L919); the exemptions paragraph (L925); the one-category-per-sentence assertion (L923); the `pdftotext` rule (L925). Surface: L927. Agnostic: L923. |
| `### 9.7` Audit write detection | L929–L934 | v1-core | Names `gql_guard.py scan` (L933); see part 10. |
| `### 9.8` Build lease | L935–L952 | v1-core | Target of the lease simplification (part 9). Surface: L939 (`surface` field, chat label built from the surface) and L943 ("the client's own Project", S0-15). |
| `### 9.9` Quota, plan tier, ownership | L953–L956 | v1-core | Estimate and headroom stay; the fast first-build path (part 9) reads from here. |
| `### 9.10` Hooks | L957–L968 | v1-core | A17 says the guard's write matcher covers the agent, Vibe and AI-column tools. The example regex at L959 would not match tool names such as the vibe tools, the run-once workflow tool or the hyphenated sequence tools seen in this session's roster; check against the live roster. Surface: L967 (Cowork wording, S0-12). |
| `### 9.11` Confidentiality exposure | L969–L982 | split | v2: L973 and L975 (shared screen, demo environment, `demo_check.py gate`), L981 (client driving the screen). v1-core: L977 (access requested as a named seat at the lowest level) and L979 (credentials never handled). Agnostic: L971, L973, L977, L979. |
| `### 9.12` Claims discipline | L983–L998 | v2 | The whole subsection: claims store, prep read, in-speech rules, if-asked list, correction loop. What A19 keeps (nothing unverified is built or promised; the never-say list; the live-probe rule) lives in 10.2 and 9.4, not here. Surface: L987. |
| `### 10.1` Where a skill gets a fact | L1001–L1011 | v1-core | L1003 notes `configure_ai_column` counts as absent from the roster, a fact the AI stage will need. |
| `### 10.2` The gotcha list | L1012–L1031 | v1-core | The never-say block (L1030) stays under A19; its reader `demo-script` is v2. The area list (L1014) has no AI-kind areas. Agnostic: L1028 and L1030. |
| `### 10.3` Knowledge overlay | L1032–L1037 | v1-core | Already outside the plugin folder. Surface: L1036. |
| `### 10.4` Read-back table | L1038–L1041 | v1-core | No read-back row for workflows, agents, AI columns, Vibe apps, sequences or webhooks. |
| `### 10.5` Drift handling | L1042–L1047 | v1-core | L1044 expects the next ring roll "around 2026-10-01", a date before today. |
| `### 11.1` What the API tells us | L1054–L1074 | v1-core | Live findings. L1099 and similar lines refer to an unnamed earlier account. |
| `### 11.2` Three layers | L1075–L1080 | v1-core | Detect, guard, verify. The `lease` mirror in `guard_index` (L1078) follows 9.8. |
| `### 11.3` Portfolio and project work | L1081–L1094 | v1-core | One v2 touch: L1093 says "any demo of it contains a job-level segment". The job-level view in the blueprint stays. L1093 also cites two real client rooms (part 8). |
| `### 11.4` Service in v1 | L1095–L1106 | v1-core | L1103's pushback on the deferral reads as objection handling (v2 flavour); the deferral itself stays. |
| `### 12.1` Critic contradictions | L1109–L1139 | split | v1-core: C1 to C4, C6 to C14, C16, C19, C24 to C26. v2-or-v3: C5 (doc images, also Cowork), C20 (Mermaid), C27 (SOP bundle). v2: C21 rubric phrase, C22 and C23 recap, C28 `discovery.md`. Surface: C5, C17, C18. Conflicts with A17 and A18: C15. Agnostic: C29. |
| `### 12.2` Critic gaps | L1140–L1163 | split | v1-core: gaps 1, 3 to 7, 12, 14, 16, 18, 19. Sandbox file: gap 10 (L1153). Surface: gap 2 (L1145). Lease: gap 8 (L1151). Migration: gaps 9 and 17 (L1152, L1160). Old plugin: gap 11 (L1154). v2-or-v3: gap 13 page size and gap 15 doc copy (L1156, L1158). |
| `### 12.3` Decisions and defaults | L1164–L1171 | split | v2: D7 (L1166), D22, D27 (L1170). v2-or-v3: D12 (L1166). v1-core: D1, D2, D3, D9, D10, D13, D16, D17, D18, D19, D20, D21, D23, D26. Unclear: D25 (research) and D4 (sign-off evidence). Superseded: D24 "AI agents: out" (L1166). Surface: D6 (L1170). Open: D5, D11, D14. Agnostic: D15 and the named test workspace in D5 (L1170). |
| `### 12.4` Amendments | L1172–L1192 | split | Rows A1 to A16 stay as history. v2 and v2-or-v3 content inside A15, A16 rows (claims store, SOP carry-over, `discovery-check` chain). Surface: A8 and A10 rows. Needs new rows A17 to A20. Agnostic: A13, A14 rows cite lessons ids; A11 row names the test workspace. |
| `### 12.5` Judge dealbreakers | L1193–L1205 | unclear | A history of proposals A, B and C being judged. Several rows are surface (L1198, L1202), SOP (L1200) or lease (L1204). The planner decides whether any of it survives the re-cut. |
| `### 12.6` Live findings | L1206–L1226 | v1-core | Each row backs a v1 decision. |
| `### 12.7` Calibration findings | L1227–L1246 | split | v1-core: rows 1 and 2 (L1233–L1234, intake). v2: the other rows (delivery, segments, numbers, pre-call gate, seat, pricing, demo environment, "not written on purpose"). The whole subsection is an earlier-work reference (L1229). |
| `## 13` Pending items and safe defaults | L1247–L1270 | split | v1-core: the three A11 decisions (L1251–L1259), calibration questions 14 and 15 (L1261), monday probes P-1 to P-18 (L1265), U-01, U-02, V-01 (L1267). v2: questions 17 and 18 and most of the provisional-rules list (L1261). Surface: all of L1263 (S0 probes). Gap: no probes for the A17 and A18 kinds. |
| `## 14` Deferred, and risks | L1271–L1307 | split | Deferred list (L1273): the entries "published workflows; AI agents and AI columns; CRM sequences and email; webhooks; notifications and updates" conflict with A17 and A18; "doc images from Cowork" is surface; pricing, proposals and ROI is out. Risk rows: v1-core for most; surface L1277 and L1278; lease L1287 and L1288; migration L1292; v2 L1293, L1294, L1295, L1298; no rows for the AI kinds. |

---

## 3. Named components

Each row gives the line where the component is first specified (usually the layout tree in section 2), the section that defines it, its tier, and whether A19's "file kept, no skill built" applies.

### 3a. Skills

| Skill | First specified | Defined | Kind | Tier | A19 kept |
|---|---|---|---|---|---|
| `engagement` | L75 | 3.1, L185–L194 | model-invocable front door | v1-core | not applicable |
| `call-intake` | L82 | 3.2, L196–L205 | model-invocable | v1-core, split (part 2) | recap, delivery-note, claims and voice-bank parts: files kept, no skill |
| `discovery-check` | L88 | 3.3, L207–L216 | model-invocable | v2 | yes: file kept, no skill built; v1 needs a build-readiness check instead (no component for it, part 3i) |
| `solution-blueprint` | L94 | 3.4, L218–L229 | model-invocable | v1-core | not applicable |
| `demo-script` | L115 | 3.5, L231–L252 | model-invocable | v2 | yes |
| `client-sop` | L120 | 3.6, L254–L261 | model-invocable | v2-or-v3 | deferred; A19 does not say kept |
| `account-build` | L100 | 3.7, L263–L271 | door, user-only | v1-core | `doc-copy` mode deferred (v2-or-v3) |
| `solution-audit` | L110 | 3.8, L273–L281 | door, user-only | v1-core | not applicable |
| `client-closeout` | L125 | 3.9, L283–L291 | door, user-only | v1-core | SOP-handover wording deferred |
| `monday-drift-check` | L130 | 3.10, L293–L301 | door, user-only | v1-core | not applicable |

### 3b. Skill reference files

| File | First specified | Defined or described | Tier | A19 kept |
|---|---|---|---|---|
| `engagement/references/routing.md` | L78 | 3.1 L192; flow 8.1 | v1-core (its stage table needs the new stage list, part 7) | no |
| `engagement/references/new-client.md` | L79 | 3.1 L192; flow 8.2 | v1-core | no |
| `engagement/references/research.md` | L80 | 3.1 L189, L192 | unclear (research at three depths) | no |
| `engagement/references/versions.md` | L81 | 3.1 L192; 7.4 | v1-core (check "release" and "recall check" against 7.4) | no |
| `call-intake/references/transcripts.md` | L85 | 3.2; 5.4 L367 | v1-core (its delivery-notes part is v2) | partly: delivery notes kept |
| `call-intake/references/call-types.md` | L86 | 3.2; 8.3 step 5 | split: detection signals and fallback v1-core or unclear; routing by type to discovery and demo is v2 | partly |
| `call-intake/references/summary-and-recap.md` | L87 | 3.2 L203 | split: summary sections, client-safe block, commitments v1-core; recap rules and status v2 | partly |
| `discovery-check/references/rubric.md` | L91 | 3.3 L214 | v2 | yes |
| `discovery-check/references/numbers.md` | L92 | 3.3 end of L214 | v2 | yes |
| `discovery-check/references/prep-and-objections.md` | L93 | 3.3 | v2 | yes |
| `solution-blueprint/references/blueprint-guide.md` | L97 | 3.4 L227 | v1-core (section list and element ids; no AI kinds yet) | no |
| `solution-blueprint/references/product-fit.md` | L98 | 3.4; 11.4 | v1-core | no |
| `solution-blueprint/references/approval.md` | L99 | 3.4; 8.5 | v1-core | no |
| `account-build/references/change-check.md` | L103 | 3.7; A3 | v1-core | no |
| `account-build/references/preflight.md` | L104 | 3.7; 8.6 | v1-core | no |
| `account-build/references/build-loop.md` | L105 | 3.7; 8.6 | v1-core (build order lives here; needs the AI offering steps) | no |
| `account-build/references/automations.md` | L106 | 3.7; 9.5 | v1-core (the one-list rule must extend to workflows, agents, sequences) | no |
| `account-build/references/changes-removals.md` | L107 | 3.7; 9.4 | v1-core | no |
| `account-build/references/recovery.md` | L108 | 3.7; 8.11 | v1-core | no |
| `account-build/references/doc-copy.md` | L109 | 3.7 L267 | v2-or-v3 | deferred |
| `solution-audit/references/snapshots.md` | L113 | 3.8; 9.7 | v1-core | no |
| `solution-audit/references/audit-checks.md` | L114 | 3.8 | v1-core (needs checks per AI element kind) | no |
| `demo-script/references/segments.md` | L118 | 3.5 | v2 | yes |
| `demo-script/references/prep-and-close.md` | L119 | 3.5 | v2 | yes |
| `client-sop/references/sop-writing.md` | L123 | 3.6 | v2-or-v3 | deferred |
| `client-sop/references/sop-export.md` | L124 | 3.6 | v2-or-v3 | deferred |
| `client-closeout/references/close-out.md` | L128 | 3.9; 8.10 | v1-core (ownership options and hand-over note need a look) | no |
| `client-closeout/references/archive-on-mac.md` | L129 | 3.9 L291; 8.10 | v1-core, surface rewrite (the name assumes a separate Mac step) | no |
| `monday-drift-check/references/probe-catalog.md` | L133 | 3.10 | v1-core | no |
| `monday-drift-check/references/overlay.md` | L134 | 3.10; 10.3 | v1-core | no |

### 3c. Agents

| Agent | First specified | Defined | Tier | A19 kept |
|---|---|---|---|---|
| `transcript-summarizer` | L136 | table row L321 | v1-core | no |
| `solution-auditor` | L137 | table row L322 | v1-core | no |
| `sop-drafter` | L138 | table row L323 | v2-or-v3 | deferred |
| `research-scout` | L139 | table row L324 | unclear (company research; see part 10) | no |

### 3d. Scripts

| Script | First specified | Defined | Tier | A19 kept |
|---|---|---|---|---|
| `mmb_common.py` | L141 | row L363 | v1-core | no |
| `record.py` | L142 | row L364 | v1-core (check `client-view`, `card`, `manifest`) | no |
| `ledger.py` | L143 | row L365 | v1-core | no |
| `leak_lint.py` | L144 | row L366 | v1-core | no |
| `transcript_measure.py` | L145 | row L367 | v1-core | no |
| `transcript_prep.py` | L146 | row L368 | split: `type`, `verify-quotes`, `set` v1-core; `delivery` v2 | `delivery` kept |
| `demo_check.py` | L147 | row L369 | v2 | yes |
| `sop_tools.py` | L148 | row L370 | v2-or-v3 | deferred |
| `gql_guard.py` | L149 | row L371 | unclear (A2 says no query guard) | no |
| `archive_check.py` | L150 | row L372 | v1-core | no |

Subcommands to review inside scripts that are v1-core as a whole:

- `record.py` (L364): `manifest` is the export manifest (v2-or-v3); `client-view` cuts the blueprint's internal section for the SOP bundle (L227, L425; v2-or-v3 or unclear); `card` writes the client card (unclear); `migrate` serves 7.10 (unclear, probably drop); `lease take/refresh/release/status/break` is the target of the lease simplification; `add-document`, `strand *`, `version *`, `freeze`, `guard`, `check`, `log` stay.
- `ledger.py` (L365): every lease flag (`--lease-epoch`, `--chat-label`) follows the lease decision; `classify`, `native-map`, `live-map`, `snapshot`, `compare`, `estimate`, `reconcile` stay; no subcommand is named for the A17 and A18 kinds, which is fine if object types carry the difference.
- `leak_lint.py` (L366): reading `.docx` and PDF text and metadata is the v2-or-v3 part; payload, blueprint and terms modes stay.
- `transcript_prep.py` (L368): `delivery` is v2; `type`, `verify-quotes` and `set` stay, with `type` shrunk to what the doors and routing need.
- `gql_guard.py` (L371): 12.4 resolves A2 as "no gate before the read, a scan after" (L1177); the user said no guard is needed (A2), so a 140-line script is a choice to confirm.

### 3e. Hooks

| Hook | First specified | Defined | Tier | A19 kept |
|---|---|---|---|---|
| `hooks/hooks.json` (three PreToolUse matchers) | L62 | 9.10, L959; L169 | v1-core | no |
| `hooks/guard.py` (twelve checks, per L169) | L63 | 9.10, L959 | v1-core | no |
| matcher 1: monday write tools by base name, refuse unless a live lease, a recent account check, today's change check and an in-target board | none in the tree | L959 | v1-core; regex needs the A17 and A18 tool families | no |
| matcher 2: dual-use tools (`all_api_read`, `all_monday_api`, `execute_code`, `run_action`), ask instead of refuse | none in the tree | L961 | v1-core | no |
| matcher 3: native boards by recorded id and lineage (refuse `duplicate_board`, structural writes on native ids, `create_board` in a product workspace outside targets, template ids, reserved column ids, `move_object` on a native) | none in the tree | L963–L965; 11.2 L1078 | v1-core | no |

### 3f. Templates

| Template | First specified | Defined or described | Tier | A19 kept |
|---|---|---|---|---|
| `CLIENT.md` | L152 | 7.1, 7.2 | v1-core | no |
| `log.md` | L152 | 7.6 | v1-core | no |
| `meetings.md` | L152 | 3.1 L194; 6 L382; 7.1 L402, L454 | v1-core; its who-has-seen-what block and demo-environment fields are v2 (L454, L975) | partly |
| `account.json` | L152 | 7.3 | v1-core | no |
| `live-map.md` | L152 | 7.8 | v1-core | no |
| `sources.md` | L152 | 3.1 (research) | unclear (research) | no |
| `research-brief.md`, `research-deep-dive.md`, `research-updates.md` | L153 | 3.1 | unclear (research) | no |
| `call-summary.md` | L153 | 6 L382 | v1-core; the type-header scoring, deferred-answer register and live-change inventory are v2 | partly |
| `document-summary.md` | L154 | 6 L382 | v1-core | no |
| `recap-draft.md` | L154 | 3.2 L203 | v2 | yes |
| `prep-sheet.md` | L154 | 3.3 | v2 | yes |
| `client-gitignore.txt` | L154 | 8.10 | v1-core | no |
| `STRAND.md` | L154 | 7.7 | v1-core | no |
| `SUMMARY.md` | L155 | 7.7 | v1-core | no |
| `discovery.md` | L155 | 3.3; 6 L382 | v2 (v1 needs a readiness file in its place) | yes |
| `blueprint.md` | L155 | 3.4 | v1-core | no |
| `backlog.md` | L155 | 3.2 L203; 3.4 | v1-core | no |
| `allowlist.md` | L155 | 3.4; 9.6 | v1-core | no |
| `build.json` | L155 | 7.3 | v1-core | no |
| `open-questions.md` | L156 | 3.3 L214; 7.1 | v1-core | no |
| `dependencies.md` | L156 | 3.4 L225; 7.9 | v1-core (non-platform strands, A13) | no |
| `gaps.md` | L156 | 3.2 L203; 3.5 | v2 (the demo gap ledger) | yes |
| `structure-inventory.md` | L156 | 3.2 L203; 6 L382 | v1-core | no |
| `scope.md` | L156 | 7.9; 6 L382 | v1-core | no |
| `version.md` | L157 | 7.4 | v1-core (its reactions block and confirmation ledger are v2) | partly |
| `audit.md` | L157 | 3.8 | v1-core | no |
| `demo-script.md` | L157 | 3.5; 6 L382 | v2 | yes |
| `SOP.md` | L157 | 3.6; 6 L382 | v2-or-v3 | deferred |
| `flow-spec.json` | L157 | 3.6; 5.4 L370 | v2-or-v3 | deferred |
| `close-out.md` | L157 | 3.9; 6 L382 | v1-core | no |
| `project-instructions.txt` | L158 | 6 L382 | v1-core, surface rewrite (Cowork Project paste) | no |
| `admin-prerequisites.md` | L158 | 6 L382 | v1-core | no |
| `automation-card.md` | L158 | 9.5 | v1-core (extend to the other list kinds) | no |
| `export-manifest.md` | L159 | 3.6 | v2-or-v3 | deferred |
| `client-card.md` | L159 | 3.9 L287 | unclear (record-close card; no A19 mention) | no |
| `archive-handoff.md` | L159 | 3.9 L291; 6 | v1-core, surface (the Cowork-to-Mac HANDOVER note) | no |
| `claims-ledger.md` | L159 | 6 L382; 9.12 | v2 (claims store); check 9.12 | yes |
| `mermaid-config.json`, `puppeteer-config.json` | L160 | 3.6 | v2-or-v3 | deferred |
| `sop-reference.docx` | L160 | 6 L382 | v2-or-v3 | deferred |
| `SANDBOX.md` | L160 | 9.11; 3.10 | v1-core (check body at 9.11) | no |

Record files that 7.1 names but the tree gives no template line (L152–L160):

- `research/sources.md`, `research/<date>-brief.md`, `research/<date>-deep-dive.md`, `research/updates.md` (L404–L406): templates exist as `sources.md` and `research-*.md`; tier unclear.
- `calls/<date>-<type>-prep.md` (L409): v2, written by `discovery-check`.
- `versions/<v>/blueprint-r<N>.md` (L435): v1-core, written by `record.py freeze`.
- `versions/<v>/export.md` (L438): v2-or-v3.
- `live/snapshots/<date>-<strand>.json` (L413): v1-core.
- `sop/diagrams/*` (L441) and `deliverables/<v>/*` (L443): v2-or-v3.
- `deliverables/handoff/*` (L444): unclear.
- `.work/` files `lock.json`, `history.json`, `cards-index.json`, `claims-queue/`, `migration-sources/` (L456): the lock follows 9.8; `cards-index.json` and `claims-queue/` exist only to cover an unreachable shared root (a Cowork concern); `migration-sources/` serves 7.10.

### 3g. Shared reference files

| File | First specified | Defined or described | Tier | A19 kept |
|---|---|---|---|---|
| `record-map.md` | L65 | 7 (L388); 5.4 | v1-core; its call-type vocabulary and label list are unclear or v2 | partly |
| `sales-method.md` | L66 | 3.3, 3.2 | v2 | yes |
| `house-style.md` | L67 | 3.12 | v2 | yes |
| `safety.md` | L68 | 9 | v1-core; the delivery-exposure part (9.11) needs a look | no |
| `monday-gotchas.md` | L69 | 10.2 | v1-core | no |
| `read-back.md` | L70 | 10.4 | v1-core | no |
| `native-objects.md` | L71 | 11 | v1-core | no |
| `leak-terms.txt` | L72 | 9.6 | v1-core; "method vocabulary" entries tie to the sales method | no |
| `sandbox-accounts.txt` | L73 | 9.11; 3.10 L301 | v1-core as a mechanism, but it holds the user's account ids inside a shipped folder (part 8, part 9) | no |

Notes on `shared/`. The never-say block and the generated "Tools relied on" block sit inside `monday-gotchas.md` (L69, L1014, L1030). The tree counts nine shared files (L169); `record-map.md` also pins the call-type vocabulary and label list (L65, L454), the intake-report and status shapes (L65) and the script version and sha table (L345).

### 3h. Repo-level and tooling files

| File | First specified | Defined or described | Tier | A19 kept |
|---|---|---|---|---|
| `.claude-plugin/marketplace.json` | L51 | 2 | v1-core | no |
| `README.md` (repo) | L52 | 2 | v1-core; install wording is Cowork (part 4) | no |
| `MAINTAINING.md` | L53 | 2; 3.12 L311 | v1-core; the voice-regeneration step is v2 | partly |
| `CHANGELOG.md` | L54 | 3.11 | v1-core | no |
| `plugin.json` | L59 | 2 | v1-core | no |
| plugin `README.md` | L60 | 2 | v1-core; "the two surfaces" is stale under A20 | no |
| `tests/` | L161 | 2 | v1-core, with v2 graders to split out (BUILD-PLAN, not in this file) | partly |
| `tools/lint_plugin.py` | L163 | 3.0 | v1-core | no |
| `tools/sync_shared.py` | L164 | 5.2 | v1-core, only if probe S0-1 fails (S0-1 stays under A20) | no |
| `tools/cleanroom_scan.py` | L165 | 0 L28 | unclear (it scans against the quarantined files of an earlier plugin; part 8) | no |
| `tools/release.sh` | L166 | 2 | v1-core | no |
| `.work/` runtime folder (`lock.json`, `intake/`, `backup/`, `tools/`) | L63, L345, L348, L353, L367 | 5.2, 5.3, 9.8 | v1-core | no |
| `~/DelOps/clients/<slug>/` (the record root) | L394 | 7.1 | v1-core | no |
| `MMB_HOME/clients-index.json` (hashed client names) | L458 | 9.6 L927 | v1-core | no |
| `MMB_HOME/cards/<slug>.md` (one-page cards) | L458 | 8.10 L844 | unclear (client card) | no |
| `MMB_HOME/monday-knowledge/` (`overlay.md`, `roster-baseline.json`, `schema-baselines/`, `flags.json`, `checks.log`) | L458, L1034 | 10.3 | v1-core | no |
| `MMB_HOME/sandbox/` with `SANDBOX.md` (the sandbox Project) | L458 | 9.1 L876; 3.10 | v1-core; surface (a Project) | no |
| `MMB_HOME/leases.json` (cross-client lease line) | L458, L943 | 9.8 | v1-core; target of the lease simplification | no |
| `MMB_HOME/claims/<slug>.md` (claims store) | L458, L987 | 9.12 | v2 | yes |

### 3i. Components the document does not have yet

Checked against the whole document, not only the tree.

- The build-readiness check (A19): no skill, reference, template or script. Nearest items are `discovery-check` (L88–L93), `discovery.md` (L155), the blueprint gate (L225, L792) and flow 8.4. `ROADMAP.md` lists a readiness skill among the stage 4 skills; this file has none.
- Element kinds for the AI offerings (A17, A18): no reference, template, agent-prompt template, audit check, read-back row, probe, hook-matcher entry, element key, live-map kind, log type or irreversible row. The only mentions are exclusions (L905, L1166, L1273).
- A first-run setup walkthrough for a consultant: nothing. Nearest is `new-client.md` (L79), the stage-0 checklist in the repo README (L52) and `admin-prerequisites.md` (L158), all per client.
- A local settings file for the user's own values: nothing. Nearest are `sandbox-accounts.txt` (L73), `leak-terms.txt` (L72) and the `MMB_HOME` root (L357).
- A client exclusion list for sample data: nothing. Nearest is the per-client `allowlist.md` (L155), which clears vocabulary only (L925).
- An email input class: nothing. Inputs named are transcripts (L200) and client documents (L782).
- A post-build research agent: nothing. `research-scout` (L139, L324) runs before design and reads organisation sources only (D25, L1170).
- Folder-inherited instructions: `project-instructions.txt` (L158) is a paste for a Cowork Project; no file is written into the folder tree.
- A fast first-build path and a two-round default: nothing. Nearest is the delta version (8.9) and the estimate with its 30% warning (L955).
- An "AI opportunities" blueprint section: nothing. Nearest is the requirement trace from pain to element (L227).
- Assumption labels: only the inference marker `[I]` (L642), which "can only shape a question".

---

## 4. Surface passages under A20

Passages that assume Cowork, a Cowork Project per client, the device shell, the cloud shell, `$HOME/mnt`, connected folders or Cowork-only probes. No `$HOME/mnt` path appears anywhere in the source; the file-access assumptions are the connected-folder and device-shell wording below.

| Lines | What assumes the old surface | What would change |
|---|---|---|
| L9 | The case for chassis C cites a second connected folder in every Cowork Project plus a Mac-side install step. | History only. State that the Mac shell and the local folder make both problems moot; remove Cowork wording. |
| L16 | Graft row "Script delivery and runtime": "No second connected folder, no install step." | Reword. Keep the plugin-path rule, tested on the Code side (S0-1 stays on A20's list). |
| L24 | Evidence tag [cowork], defined as the user's capability report of 2026-09-11. | Replace with a Code-side tag or keep as history; the tag is used in the 5.1 heading (L332). |
| L52 | Repo README: install via "Customize > add marketplace, or upload". | Claude Code install path (marketplace add from Code); upload is a Cowork and claude.ai route. |
| L60 | Plugin README: "the two surfaces". | One surface in v1; Cowork and chat-side Projects listed as later (A20). |
| L129, L287, L291 | `archive-on-mac.md` and the two-surface close-out (`strand` and `record` in Cowork, then `archive` on the Mac). | One session does record close and archive on the Mac. The surface hop disappears. |
| L158, L382 | `project-instructions.txt`: six lines the user pastes into each Cowork Project. | Becomes instructions the client folder inherits (part 9); no paste step. Its content (read `CLIENT.md` first, fresh chat for heavy work) carries over. |
| L159 | `archive-handoff.md`, the HANDOVER note of what exists only locally (L291). | Not needed when the record is already on the Mac; keep only a local-versus-archived list if wanted. |
| L177 | "Cowork and claude.ai uploads reject XML-like tags in descriptions." | The no-angle-bracket rule can stay as portability; drop the Cowork reason. |
| L192 | `engagement` locates the record via "the Project's connected folder, or the path the user names", and detects the runtime once per chat. | Locate the record from the current folder (`~/DelOps/clients/<client>/`). Runtime detection shrinks to checking Python and the plugin path. |
| L261 | `client-sop` export "follows the tier chosen by `sop_tools.py doctor`". | Tiers rest on cloud-shell tools; deferred with the SOP (v2-or-v3). |
| L332–L340 | All of 5.1, heading marked [cowork]. | Rewrite as one Mac shell, one row. |
| L336 | Device shell: aarch64 VM, Python 3.10, Node 22, git 2.34, about 45 s per call, deletes need a one-time approval. | Replace with the Mac's own shell facts (Python 3.9.6 on the Mac, per L338). The call limit and the delete prompt go. |
| L337 | Cloud shell: rendering tools; `mcp.monday.com` and `storage.googleapis.com` refused; no pip or npm. | Serves rendering only (v2-or-v3). Drop for v1. |
| L338 | Code on the Mac row: Python 3.9.6, git, `gh` signed in. | Becomes the only row. Credentials and archive steps no longer need a second surface. |
| L340 | Probe S0-4: how a rendered file reaches `deliverables/<v>/`; `presented` versus `saved` marks. | S0-4 is Cowork-only. Drop; the `presented` mark goes with it. |
| L345, L348 | Ladder step 2 copies scripts into `.work/tools/<plugin-version>/`; "No second connected folder and no Mac-side install step". | Keep step 2 only if S0-1 fails on the Code side. Reword L348. |
| L353 | "Probe S0-3 confirms which operations prompt in the device shell." | S0-3 is Cowork-only. Drop. |
| L357 | `MMB_HOME` defaults to `~/DelOps`; the device shell's own home "is not the Mac's". | A20 makes `~/DelOps` the real home. Keep `MMB_HOME` for the test runner; drop the device-shell caution. |
| L456 | `.work/claims-queue/` and `.work/cards-index.json` exist so work continues when the shared root is unreachable from the device shell. | Drop with their fallbacks, or keep as plain defensive code. |
| L458 | Paths under `MMB_HOME`: `cards/` "(one-page cards, Mac)", `sandbox/` "(the sandbox Project, with `SANDBOX.md`)"; reachability "from a device shell is probe S0-15"; fallbacks include "the cards to the Mac" and a claims queue "for the Mac to fold in". | Under A20 the root is reachable, so the fallbacks go. The sandbox Project becomes a sandbox folder. S0-15's meaning changes (A20 cites it as Code-side evidence). |
| L460 | The slug "is the folder, the Project and the archive repo name". | Drop "the Project". |
| L754 | 8.1 step 1: detect the runtime once, "which shells exist, whether the scripts are reachable, which document tools are present". | Shrinks to checking Python and the plugin path. Document tools matter only for the deferred SOP. |
| L759 | 8.1 step 6: a different client is always a fresh chat "since that is a different Project and folder". | A session opened in that client's folder (A20, interview Q11). |
| L763 | 8.2 step 1: check the connected folder is empty. | Check `~/DelOps/clients/<slug>/`. |
| L765 | 8.2 step 3: print `project-instructions.txt` to paste into the Cowork Project. | Write the instructions into the client folder instead (part 9). |
| L766 | 8.2 step 4: refuse ids listed in `shared/sandbox-accounts.txt`. | The mechanism stays; the list moves to local settings (part 9). |
| L842, L844 | 8.10: strand close marked Cowork; record close split into a "Cowork part" and a "Mac part"; `archive-handoff.md` lists what exists only locally. | One session on the Mac does both halves. The surface split and the handoff note go. |
| L868, L869, L875 | 9.1 "Where" column: close a strand "Cowork", close the record "Cowork, then the Mac", archive "Claude Code on the Mac". | Every cell becomes the Mac session. |
| L899 | 9.4 row: asset upload "only for SOP images, on the Mac, at the user's request". | v2-or-v3, with the doc copy; the Mac qualifier goes. |
| L927 | The cross-client lint check "works in Cowork" through a hashed copy of the index in `.work/cards-index.json`, refreshed at init and close-out, with a 90-day warning; the Mac close-out step "runs it for real". | Read `~/DelOps/clients-index.json` directly; the copy, the 90-day rule and the warning go. |
| L939, L943 | The lock file holds a `surface` field and the chat label is built from "the surface"; within-record contention is authoritative because the file is "reachable from the client's own Project"; the cross-client line is written "where that root is reachable" (S0-15). | One surface value; reachability is assumed. This ties to the lease simplification (part 9). |
| L967 | Hooks: "behaviour in Cowork is unverified (probe S0-12)". | Reword for Code; S0-12 stays on A20's list. |
| L987 | Claims store fallback: "Where the root is unreachable (S0-15)" the prep removes figures and queues entries "for the Mac to fold in". | v2 anyway; drop the fallback. |
| L1036 | "If the overlay folder is not reachable from a Cowork chat, the bundled knowledge applies and the briefing says the overlay was not read." | Drop, or keep as a plain defensive branch. |
| L1117 | C5: doc images "proven from the Mac shell only; in Cowork the copy is text-first". | v2-or-v3 (doc copy); drop the Cowork half. |
| L1128, L1129 | C17 "Cowork and Claude Code only; folder-wrapped local projects" and C18 "a cloud session with a Mac device shell". | Superseded by A20. |
| L1145 | Gap 2 "Cowork environment": closed by probes S0-1 to S0-15. | Narrow to the Code-side probes. |
| L1170 | D6: "cloud session with the Mac bridge, folder-wrapped projects, git on the Mac". | Superseded by A20. |
| L1183, L1185 | A8 row "Honoured throughout section 5"; A10 row removes "One chat per meeting" from "the Project instructions template". | Replace the A8 row with an A20 row; the instructions template moves to inherited folder files (part 9). |
| L1198, L1202 | Dealbreaker rows about a second connected folder and a cross-client name check "in Cowork". | History; drop with 12.5 if the planner agrees. |
| L1263 | The whole S0 paragraph, headed "Cowork runtime (S0)". | Drop S0-2, S0-3, S0-4, S0-8, S0-10 (A20). Keep S0-1, S0-5, S0-6b, S0-7, S0-9, S0-12, S0-14. S0-11, S0-13 and S0-15 are not ruled on by A20 (part 10). S0-7's default, builds only from Claude Code on the Mac, becomes the base case. |
| L1273 | Deferred list item "doc images from Cowork". | Reword or drop. |
| L1277, L1278 | Risk rows: scripts unreachable in a Cowork chat; `disable-model-invocation` not honoured in Cowork. | Reword for Code or drop. |

---

## 5. Sales-grading touchpoints

Where the discovery check, the R-criteria, gates, verdicts, gap questions, demo scripts, recaps or the sales method drive a flow, a field, a template or a file. In v1 the build-readiness check takes their place.

| Lines | Touchpoint | Drives |
|---|---|---|
| L21 | Graft row "Method depth and drift": discovery rubric depth, delivery notes, recap status. | Names the sales content taken from proposal A. |
| L66 | `shared/sales-method.md`: per-pain checks, R1 to R12, verdict, gates, objection map, demo principles. | Linked by every grading and demo skill. |
| L67, L307–L313 | `shared/house-style.md` and 3.12, the voice. | Register of recaps and run-sheets. |
| L88–L93 | `discovery-check` skill and its three references (`rubric.md`, `numbers.md`, `prep-and-objections.md`). | The grading itself. |
| L115–L119 | `demo-script` skill and its two references. | Run-sheets and the close. |
| L146, L368 | `transcript_prep.py` `type` embeds the header vocabulary; `delivery` computes talk share, restated-and-unanswered windows. | Type scopes which criteria apply; delivery feeds delivery notes. |
| L147, L369 | `demo_check.py` (`budget`, `gate`). | Run-sheet checks. |
| L154–L157 | Templates `recap-draft.md`, `prep-sheet.md`, `discovery.md`, `gaps.md`, `demo-script.md`. | Files written by the sales skills. |
| L189, L192 | `engagement` description and briefing: discovery verdict and open gaps, SOP behind, next meeting, overdue commitments; routing per `routing.md`. | The front door routes on grading state. |
| L200, L203 | `call-intake` drafts a recap, adds delivery notes, raises the restated-and-unanswered objection, marks voice-bank turns, runs the short check on support and check-in calls, writes `gaps.md` and the confirmation ledger after a demo. L200 ends with "discovery-check does that next". | The intake hands off to grading. |
| L211–L216 | All of 3.3. | The rubric, verdict, gates, gap questions, prep sheet. |
| L225 | `solution-blueprint` checks the blueprint gate and logs an override; reads `gaps.md` and plans the most-repeated ask; reads the claims store. | A gate sits in front of design. |
| L227 | Blueprint section on platform consumption points at `discovery.md`; the structure mapping is "confirmed before the first demo segment". | Design depends on a grading file and a demo step. |
| L231–L252 | All of 3.5. | Run-sheets, budgets, close. |
| L281 | `solution-audit` reports "the verdict and the blueprint gate separately". | Audit output uses a grading gate. |
| L382 | Templates: `discovery.md` gains client-built assets, platform consumption, voices line, asked flags; `demo-script.md`; `call-summary.md` opens with the call-type header of four dimensions and two modifiers. | Record structure follows the rubric. |
| L394, L424, L736 | `discovery.md` is a strand-level file; "a second strand is graded on its own evidence". Non-platform strands also hold it. | A grading file inside the record layout. |
| L409 | `calls/<date>-<type>-prep.md` is written by `discovery-check`. | Next-meeting prep sheet. |
| L430, L450 | `open-questions.md` is written by `discovery-check`; its per-kind cap equals the gap-question cap of method section 2.5. | Needs a v1 writer; the `conflict` kind (A15) stays. |
| L432, L450 | `gaps.md`: five states, repeat counts, "supplies the run-sheet's most-repeated-ask refusal and its spoken gap line". | Demo-driven ledger. |
| L433 | `structure-inventory.md`: "discovery-check grades its read-back". | Grading step on an input artefact. |
| L437, L442 | `demo-script.md` under `versions/`; `drafts/<date>-recap.md`. | Sales files in the strand layout. |
| L454 | Thirteen call labels; `call_type` scopes which criteria apply. | Typing exists to scope the rubric. |
| L464, L499, L684, L685 | `discovery verdict` and `SOP behind` in the strand index and `STRAND.md`. | Fields carried per strand. |
| L609, L624, L683 | `demoed` version state: entered when intake processes the demo transcript; needs the demo script, the demo summary, reactions and confirmations. | State machine step before `released`. |
| L627, L832 | Release is proposed "after the demo intake". | Release trigger. |
| L629 | v1.0 release needs agreed R6 criteria, R11 Met for every in-scope pain, a confirmed export and sign-off evidence. | Rubric criteria gate a release. |
| L633–L642, L646 | Evidence-marker table column "Counts toward the rubric"; grades Partial and Missing; "grading is per turn". | Markers carry grade effects. |
| L663 | Log types `discovery`, `override`, `demo`, `sent`, `commitment`. | Log vocabulary. |
| L680, L686, L694, L696 | `STRAND.md` stage ladder with `discovery`, `demo`, `signed-off`, `expanding`; `next_step` as a dated meeting; body block "verdict and top gaps"; `output_class` read by "the demo door". | Strand front page. |
| L756 | 8.1 briefing: "verdict and open gaps", gate-versus-commercial-date collision, SOP behind, next meeting, overdue commitments. | Front-door routing. |
| L776 | 8.3 step 5: the type header (seat, relationship, direction of show, output class; room shape, money live) and conservative fallbacks that demote "every type-specific rubric rule to advisory". | Typing drives grading scope. |
| L777 | 8.3 step 6: delivery notes and the recap draft. | Intake output. |
| L778 | 8.3 step 7: routing by label into `discovery-check`; demo fills `gaps.md`, the confirmation ledger, the live-change pass, offers version release and SOP update; pricing call under method section 4.10; call-review claims; five-item short check. | Intake hand-off. |
| L780, L782 | A package and a lone document each "chain `discovery-check`", then the blueprint, once. | Hand-off to grading. |
| L784–L787 | All of 8.4. | The grading flow. |
| L792 | 8.5 step 1: "Check the gate ... record an override". | Gate in front of the blueprint. |
| L829, L836 | 8.8 step 29 `demo-script`; 8.9 "intake plus grading" and the short check. | Iteration and demo prep. |
| L873 | 9.1 row "Save client-facing files": `client-sop` and the recap draft. | Authority for sales and SOP files. |
| L919, L921 | 9.6 runs on the recap in `drafts/` and blocks method vocabulary, objection text, stakeholder assessments, alternatives in play and closing tactics (deadline anchors, cost-of-waiting math, planned commitment questions, exit-ramp notes). | Lint categories named after sales artefacts. |
| L925 | 9.6 recap shown with a "not checked, do not send yet" banner when the lint cannot run. | Recap behaviour. |
| L971–L981 | 9.11 demo and delivery exposure: shared screen, demo environment, `demo_check.py gate`, the client driving the screen. | Live-delivery rules. |
| L983–L995 | All of 9.12: claims store, prep read, in-speech rules, audience routing (method section 4.10), if-asked list, correction loop. | Claims discipline in live speech. |
| L1030 | The never-say block is "read at generation" by `demo-script`. | The block stays (A19); its reader is v2. |
| L1093, L1103 | 11.3 "any demo of it contains a job-level segment"; 11.4 fixture s7 where the client pushes back on the deferral. | Demo and objection touches inside v1 sections. |
| L1132, L1133, L1136, L1137 | C21 "count toward the rubric", C22 and C23 recaps, C27 the drafter never sees `discovery.md`, C28 `discovery.md` budget "calibrated on the multi-call pack". | Decision-log rows. |
| L1166, L1170 | D7 "discovery gate: warn and log", D8 pricing, D4 sign-off evidence, D22 recap after every meeting, D26 type-specific rubric rules go advisory, D27 claims store. | Defaults the user set or the design took. |
| L1190, L1191 | A15 and A16 rows: `discovery-check` and the blueprint "run once over the whole set"; a document-only client "graded under the document rules alone". | Amendment landings. |
| L1200 | Dealbreaker fix: "the 'SOP behind' line is in the briefing". | |
| L1236–L1243 | 12.7 rows on segments, numbers, pre-call gate, pricing, check-ins, close. | Calibration findings for delivery. |
| L1261 | Calibration questions 14 (blocking fork), 15 (consumption beside the bleed frame), 17 (demo environment), 18 (credential for a client-count claim) and the provisional-rules list. | 14 and 15 feed the blueprint; 17 and 18 are sales. |
| L1273, L1295–L1298 | Deferred list: pricing, proposals, ROI, "any call-type cell the calibration did not evidence"; risk rows on call-type misdetection, re-quoted figures, behavioural rules from a few sellers. | |
| L1293, L1294 | Risk rows: improvised figure or claim spoken live; the user's own operational account on a shared screen. | Delivery risks; both point at `demo_check.py` and the claims store. |

---

## 6. Record fields tied to grading

Type-header tokens, `direction`, the gates fields, grades and verdict fields, and where each is defined.

| Field or token | Defined at | Notes |
|---|---|---|
| Type header: four dimensions (seat, relationship, direction of show, output class) and two modifiers (room shape, money live in the room) | Definition and detection at L776; template at L382 (each `detected`, `proposed` or `confirmed`); vocabulary pinned in `record-map.md` (L454) | Only `output_class` also lives on `STRAND.md` (L676), where the doors read it. The other five tokens exist for the rubric scope matrix. |
| `direction` (direction of show: we show, they show their current state, they show a candidate solution, nobody shows) | L776 | Another meaning of "direction" is the per-flow direction in `dependencies.md` (L450). L1261 calls direction a co-sell signal. |
| Thirteen call labels (`call_type`, and the stem of `calls/<date>-<type>.md`) | L454 | Eight chain `discovery-check` (L778): seven in one list and `pricing` as well. |
| Call front matter: `call_type`, `sequence`, `package`, `provenance`, `handed_over_by`, `attendees`, `strands` | L454 | `provenance`, `package` and `sequence` serve A15 and stay in v1; `call_type` is the grading hook. |
| `discovery_verdict` (not-graded, not-ready, nearly-ready, complete) | L684; moved off `CLIENT.md` at L464; strand-index column L499 | |
| `sop_behind` | L685; L464; L499; briefing L756 | A SOP field. |
| Stage values `discovery`, `demo`, `signed-off`, `expanding` | L680 | Platform and hybrid ladder. |
| `version_state` value `demoed` | L683; state machine L609, L624 | |
| The five gates: Solution blueprint, Build, First demo (v0.1), Pricing or proposal prep, v1.0 sign-off | Named at L214 | The blueprint gate is R1 at least Partial and R2 Met (L214). This file gives no field schema for gate results; the shape lives in the rubric reference. Gate state is kept in `discovery.md` (L211, L394, L424). |
| Verdict values: Discovery complete, Nearly ready, Not ready | L214 | Verdict is Complete when R2, R3, R4, R7 are Met (L214). |
| Grades `met`, `partial`, `missing`, `advisory`, not applicable; Met-with-residual; "not obtainable from this room"; the `asked?` flag | L214 | `advisory` is the type-demotion state. |
| Per-pain checks Stated, Concrete, Workaround, Reach, Cost inputs, Trajectory | L214 | |
| Bleed states and the unpriced slot | L214 | |
| Evidence-marker column "Counts toward the rubric" | L633–L642 | |
| Override entries | L663 (log type), L694 (`STRAND.md` block), L787 (8.4 text), L792 (8.5 step 1) | |
| `meetings.md` presenter, environment and who-has-seen-what block | L454 | Demo-oriented. |
| Per-pain confirmation ledger in `version.md` | L246, L624, L778 | Read by R11 and the close. |
| Delivery-note measures | L203, L368, L777 | |
| `kind` (platform, non-platform, hybrid) and `output_class` (configured-structure, bespoke-code, hybrid) on `STRAND.md` | L675–L676, L696; rule D26 at L1170 | Not grading. Both are read by the doors and survive into v1. `output_class` is the same distinction as the fourth type-header dimension (L776). |
| Gate default D7, "warn and log" | L1166 | The user's decision for the discovery gate. A19 replaces the check, so whether the same warn-and-log behaviour carries to build-readiness is a question (part 10). |
| "Platform consumption" section in `discovery.md` | L214, L227, L1261 | A17 keeps the consumption question as a design input, but its home file is a grading file. |
| Strand-index columns on `CLIENT.md` | L499 | Short id, title, kind, state, version and version state, discovery verdict, SOP behind, live object count, last activity. |

---

## 7. Stage order and the AI-offering stage

### 7a. Where the stages are listed today

1. **The flow, as section 8 runs it.** Intake (8.3, L770), discovery check (8.4, L784), blueprint, approval and freeze (8.5, L788), change check, preflight and build (8.6, L801), audit (8.7, L817), demo, SOP and release (8.8, L827), iteration (8.9, L834), close-out (8.10, L840). Recovery (8.11, L846) sits off the line. Steps are numbered through the flows: 1 to 8 in 8.5, 9 to 21 in 8.6, 22 to 28 in 8.7, 29 to 32 in 8.8.
2. **The strand `stage` ladder** (L680): new, discovery, blueprint, building, demo, signed-off, expanding, closing, closed. A non-platform strand uses new, scoping, handed-off, closed. There is no audit stage and no AI stage. `discovery`, `demo`, `signed-off` and `expanding` are sales stages.
3. **The version state machine** (L609, table L616–L625): planned, approved, building, built, fixing, audited, demoed, released. The audit already sits ahead of the deferred states (`demoed`, and `released` after a demo), which matches A19's wish to put the audit before anything deferred.
4. **The build order inside the build door** (L810, step 16): workspace and folders; boards; groups; plain columns; relation columns; mirrors and formulas; items and seed data; links; views and board-first forms; docs; dashboards and widgets; automations last. The same order is stated at L271 and L911. The element key list (L602) follows it. The fuller order lives in `build-loop.md` (L105), which is not in this file.
5. **Project stages** (stage 0, 1, 1b, 2 and so on) are not in this file. It points to BUILD-PLAN sections and work packages (L26, L1014, L1153, L1255), and the S0 probes sit at L1263.

### 7b. Where the AI element kinds sit today

- Nowhere in the build order, the key list (L602), the live-map kinds (L710), the blueprint sections (L227), the approval card (L797), the read-back table (L1040), the audit checks (3.8), the hook matcher (L959), the log types (L663), the recovery inventory (L848), the probe list (L1265) or the risk table (L1275–L1306).
- They appear only as exclusions: the v1 exclusion list (L905), "D24 AI agents: out" (L1166), the deferred list (L1273), and C15, "Only v1-scope items were probed" (L1126). Published workflows, CRM sequences, webhooks, and notifications and updates are named at L905 and L1273 and nowhere else. Vibe apps are not named at all.
- Neighbouring facts that still hold: `configure_ai_column` counts as absent from the roster (L1003); the gotcha areas include "automations and workflows" (L1014); the never-say block carries a metered-allowance row (L1030), consistent with A17's rule of no credit figures; consumption is a recorded design input (L214, L227, L1261).

### 7c. What A17, A18 and A19 ask for, and where it would go

- A17 builds agents last, after automations, enables nothing an agent can act on until it has been read back, and makes Vibe publication a separate irreversible step. A19 orders the stages blueprint, build, audit, then the AI offerings, ahead of anything deferred.
- Two readings. (a) The AI kinds extend the build order after automations, inside 8.6 step 16 (L810) and step 20 (L814). (b) The AI kinds are a second round after the audit, as a new version with its own approval card, build and audit (7.4, 8.9). Both put the AI kinds after automations. They differ on whether the audit (8.7) sits between the rounds. Reading (b) matches the two-round default in part 9. The planner chooses.
- Places that need the new kinds either way: key list (L602), live-map kinds (L710), `STRAND.md` stage ladder (L680), approval card (L797), build order (L810) and list confirmation (L814), audit report (L824), recovery inventory (L848), irreversible table and exclusion paragraph (L886–L905), automation approvals (L907–L916), hook matcher (L959), read-back table (L1040), gotcha areas (L1014), decision rows D24 (L1166) and C15 (L1126), amendment rows (L1172–L1192), probes (L1265), deferred list and risks (L1273–L1306).

---

## 8. Agnostic sweep hits

Lines only, with a few words each. Nothing is fixed here. The publisher's name in the plugin manifest is allowed. Every occurrence of a GitHub handle is listed, and the handle itself is not written.

Not hits: no personal name appears in the source (I scanned mid-sentence capitalised words outside code). The example client in the JSON and log samples (L469–L470, L511, L593, L655, L659) is fictional. The publisher's name inside `~/DelOps/...` folder paths (L225, L357, L394, L458, L829, L844, L927, L1034, L1170, L1263) matches the folder A20 itself names.

| Lines | What refers to the past, another plugin or a named party |
|---|---|
| L3 | Revision note cites the real-call calibration (`REAL-CALL-LESSONS.md`) and `REVISION-NOTES-2.md`. Earlier work and real calls. |
| L7, L9, L11–L22 | Design history: proposals A, B and C and judge scores. Internal provenance, not a plugin reference; the planner decides whether it stays. |
| L22 | "cross-plugin should-not-trigger set": tests against other plugins. |
| L24 | [cowork] tag defined by the user's capability report of 2026-09-11. Earlier setup facts. |
| L26 | Live-test result files and counts (boards and workspaces) from earlier runs; no account named. |
| L28 | Clean-room statement: the old plugin and the quarantined `dossier/learn-*.md` files. |
| L46, L49, L338 | GitHub handle. It stood at these three lines when I first read them, and the source was changed at 03:08 on the day of this run, during my read. Replacement wording ("the user's GitHub account" and similar) now stands at L460, L844, L1166 and L1263 too; those lines probably held the handle as well, but I never saw them with it. |
| L51, L59 | The publisher's name in `marketplace.json` and `plugin.json`. Allowed; listed for completeness. |
| L73 | `sandbox-accounts.txt` holds the user's sandbox slugs and ids and operational account ids inside a shipped shared folder. |
| L165, L374 | `cleanroom_scan.py` scans against the quarantined learn files of an earlier plugin. |
| L178 | Reserved names include "the old plugin's names". |
| L214 | Scope-matrix cells marked unspecified where "the calibration did not evidence" them (the real-call calibration). |
| L248 | "the dossier's plan-gate list": the quarantined research dossier. |
| L309, L311 | Voice bank "fully genericised" from real turns; measured rates for "one colleague" against the user. |
| L382 | "on a real call the client's own question about how we should be granted access was asked and answered by nobody": a real call. |
| L450, L776 | "what the calibration asked for", "the fork that mattered most surfaced during a demo of ours", and "ships provisional on one observation": traces of the real-call calibration. |
| L456, L663, L730, L744–L749 | Migration from a single-engagement record (`migration-sources/`, the `migration` log type, the migration-default live-map source, all of 7.10). It refers to an earlier record shape that never shipped. |
| L511–L553, L571–L593, L659 | Example JSON and log entry hold numeric ids shaped like real monday ids (account, product, board, workspace, template, view and user ids) from earlier live runs. The ids are not repeated here. |
| L923 | Leak-lint paragraph: "The user's own firm name" is hard-wired into a phonetic-variant rule, said to have "appeared in several renderings across real transcripts". The trap-shape list after it (merger counterparty, a named person leaving, a health detail about an absent colleague, the seller's internal account structure) reads as drawn from real calls. |
| L963 | Cites a live report for a native Accounts board "renamed with its terminology changed" and two look-alikes: data from one earlier account. |
| L971 | "the worst exposure the calibration found": a specific earlier incident from a real call (an operational board shown to a prospect's room). |
| L973 | `shared/sandbox-accounts.txt` again: the user's own operational account ids marked never-demo; "one observation". |
| L977, L979, L981 | "our own dossier rather than from any call"; "on the one observation, floating it produced an immediate offer"; "provisional: one observation" and "the observed request that shaped a whole build": real-call traces. |
| L985 | "the calibration found that most damaging claims were improvised answers". |
| L1028, L1030 | "nothing from the quarantined learn files enters as a rule"; "two of our own people gave opposite answers in two calls"; "a colleague's earlier meeting". |
| L1052, L1056, L1099, L1180, L1212, L1217, L1265 | Counts and findings from earlier live runs on unnamed accounts (boards, workspaces, "more than 500 workspaces"). Data only; no account named. |
| L1057, L1059, L1066, L1265, L1267 | Numeric ids from earlier live runs: template, view, board and automation ids. Some are monday-wide template ids; the automation id in U-01 (L1267) is account-specific. Not repeated here. |
| L1128, L1129, L1145, L1170 | Cowork-era decisions C17, C18, gap 2 and D6 as settled history (earlier setup). |
| L1138 | C29: "The learn files stay quarantined"; `cleanroom_scan.py` runs at every release. |
| L1154, L1170, L1263 | The old plugin: gap 11 ("The old plugin is disabled before any test (S0-11); trigger tests include official-plugin prompts"), D15, and probe S0-11. |
| L1160 | Gap 17 calls the `client/1` to `client/2` move "the first migration the plugin ships": an earlier record shape. |
| L1170, L1186, L1255 | A named test workspace appears in D5 (L1170), the A11 row (L1186) and twice in the A11 table (L1255). The name is not repeated here. |
| L1170 | D25 names a third-party networking platform in a policy line, only to rule out automation against it. Low severity: a firm other than the publisher. |
| L1188, L1189 | A13 and A14 rows cite "lessons decision 12", "C115", "C116", "C117" and "lessons decision 13": ids in `REAL-CALL-LESSONS.md`. |
| L1229 | 12.7 intro names `REAL-CALL-LESSONS.md`. |
| L1257 | "The calibration recorded one candidate answer, the way it was itself run": how earlier work was done. |
| L1261 | "lessons decisions 14 to 18" and "roughly twenty of the calibration's changes rest on one observation". |
| L1273 | Deferred list: "any call-type cell the calibration did not evidence", and C116. |
| L1286, L1298 | Risk rows: "multi-call calibration" and "Behavioural rules induced from a handful of sellers". |

---

## 9. Landing spots for new inputs

Each item gives where it would land, what already exists there, and the gap or conflict.

**1. Fast first-build path, about one hour, a whole workspace with sample rows.**
- Lands in: 8.6 (L801–L816) as a mode of the build door, listed with the other modes at 3.7 (L271), with sizing at 8.5 step 5 (L796) where `ledger.py estimate` already runs and in 9.9 (L955).
- Exists: an API-call estimate with a warning above 30% of headroom and an offer to split across days (L955, L1285); a seed-data step (L810); `sample-cleanup` (L271). Nothing is sized by time or built as a one-pass path.
- Gap or conflict: the sample-data question is open with no default (L1256, L490), so the path cannot assume sample rows. A new workspace is a listed irreversible step (L903). One yes per irreversible item (L813), a read-back after every write (L811) and the 20-write account check (L811) set a floor on speed.

**2. Two-round default.** Boards, views, dashboards, forms, working automations and docs first; the AI layer second; order flipped when the client asked for AI.
- Lands in: the order at 8.6 step 16 (L810); the round split in the blueprint's "version scope and deferred items" (L227); the second round as a delta version at 8.9 (L836).
- Exists: delta versions that build only the difference (L836); automations last (L810); a version scope section (L227).
- Gap: no rule that puts an AI layer second, none that flips the order, and no statement of whether round two takes its own approval card and audit. As a new version it would (7.4).

**3. "AI opportunities" section in the blueprint.**
- Lands in: 3.4 (L227), as a named subsection inside one of the sixteen sections, which is how the document says additions must go so the count, the `client-view` cut and the lint range do not move. Candidate hosts are product fit and the requirement trace (both L227). Also `blueprint-guide.md` (L97).
- Exists: the trace from pain and quote to element id and acceptance check (L227).
- Gap: there are no AI element kinds to tie a suggestion to (part 7), so the section depends on new keys at L602.

**4. A new workspace per client, one workspace per product, with cross-product automations or workflows as approved list rows.**
- Lands in: 3.4 L227 (workspace and product binding; board inventory split new, pre-existing changed, pre-existing referenced), 8.6 step 16 (L810), 9.4 (L903); the list rows in 9.5 (L907–L916) and the card at 8.5 step 6 (L797).
- Exists: numeric product id passed and `account_product.kind` read back (C13, L1125); `product_workspaces` in the guard index (L533, L1078); `build_targets_by_strand` holding workspace ids (L544); an automations list that shows recipients (L915).
- Gap or conflict: L903 says prefer an existing workspace or folder and treat a new one as a listed irreversible step. Native CRM and Service boards sit in the account's own product workspaces and are found across non-default ones (L1099, L1217), so "one workspace per product" needs a stated rule beside native reuse (A5). The automation row has one board field (L227); a cross-product row needs more.

**5. Email as an input class beside transcripts and documents.**
- Lands in: 8.3 as a third block beside the call set (L780) and the client document (L782); the skill description at 3.2 (L200); `record.py add-document` (L364) and `transcript_measure.py document` (L367) with a new input kind; the `inputs/` rows (L410–L411); a marker beside `[Q/doc]` (L639); `document-summary.md` (L154, L382).
- Exists: documents as authored evidence with author, date, status, section anchors and a citation form (L782, L639). That path is the nearest fit, and it already lets any combination arrive in any order.
- Gap: threads, quoted replies, forwards and sender roles. The A11 retention question (L1257) must name emails. The copied-run exemption for client-authored text (L925) needs a ruling.

**6. Build lease simplified to a within-record guard plus one "is another build running?" question.**
- Lands in: 9.8 (L935–L952). Ripples at 3.7 (L271), 8.6 step 11 (L805), 8.7 step 22 (L819), 8.8 step 32 (L832), 8.10 (L842, L844), 8.11 (L848–L850), 9.1 (L865, L867), 9.10 (L959), 5.4 (L363–L365), 7.1 (L456, L458), 7.2 (L485), 7.3 (L545, L569, L578), 7.4 (L620), 7.7 (L700), 11.2 (L1078), 12.2 gap 8 (L1151), 12.5 (L1204), and the risks at L1287 and L1288.
- Exists: the one plain question already exists, as the fallback when the shared root is unreachable (L943, L458, L1263). The within-record lease exists in full: epoch fence, minted label, heartbeat, three mirrors and a five-condition break.
- Change: promote the question to the cross-client mechanism, drop `leases.json`, and decide how much of the within-record machinery stays. The hook (L959) reads the lock and its heartbeat, so it changes with it.

**7. First-run setup walkthrough for any consultant.**
- Lands in: a step before 8.2 (L761), as the front door's first-ever run; wording in `new-client.md` (L79) and the plugin README (L60). 8.2 is per client and starts from the slug.
- Exists: the install and stage-0 checklist in the repo README (L52), per-client setup questions (L764), admin prerequisites (L768), runtime detection at the start of every chat (L754).
- Gap: nothing creates `~/DelOps`, writes the user's settings (item 13), checks Python and the connector once, or explains the doors.

**8. Client exclusion list for sample data.**
- Lands in: the blueprint's data and sample-data policy (L227); the A11 sample-data row (L1256) and `sample_data_in_account` (L490); the leak lint (L921).
- Exists: the per-client allowlist (L155, L925), which does the opposite job; the hashed cross-client name index that keeps other clients' names out (L921, L927); the sample-data question itself, still open.
- Gap: no list of names or terms that sample rows must avoid, and no named file. The record, beside `allowlist.md`, is the natural home.

**9. A research agent that runs after the first build to improve later rounds.**
- Lands in: the agents table (L319–L324) as a new row or a second mode of `research-scout`; `research.md` (L80); 8.9 (L836) between round one and round two. The pre-build brief is offered at 8.2 step 6 (L768).
- Exists: `research-scout`, organisation research on the public web with no monday tools (L324; D25, L1170); three tiers (L189). "Scheduled research refreshes" is deferred (L1273).
- Gap: purpose and inputs differ, since it should read the build and the record rather than only the client's sources. Agents cannot ask the user or write state (L317), so the main thread saves what it returns.

**10. Assumptions labelled in the record and turned into questions for the next call.**
- Lands in: the markers (L642), the `open-questions.md` kinds (L450), the blueprint's default clause (L798) and client decisions (L227), and the build-readiness check that replaces the gap questions of 8.4 (L786).
- Exists: `[I]` inference marks with a basis, which "can only shape a question" (L642); question kinds conflict, technical, access, commercial, policy, ask (L450); a default clause with three states, take it, override with a reason, or fork open (L798); at most five ordered gap questions, each showing what is known (L786, v2).
- Gap: no `assumption` label for build decisions made without evidence, and no step that carries unresolved ones into the next call's questions.

**11. Iterate versus fresh build; old workspaces left in place until the user says otherwise.**
- Lands in: 8.9 (L834–L839), the live map (7.8, L702–L731), 8.10 (L842).
- Exists: delta builds inside a strand (L836); a new strand starts at its own v0.1 and is not a delta (L838); at strand close "nothing is removed from the client's monday account" (L842); no `delete_*` (L905).
- Gap: no way to ask for a rebuild of the same scope that is not a delta, and no explicit rule that a superseded workspace stays until the user says. Live-map states are active, archived and removed-by-platform (L712).

**12. No state kept in the plugin's own folder, because it is a per-session copy.**
- Lands in: 5.2 (L342–L348), 5.3 (L357), 10.3 (L1034).
- Exists: the design already keeps mutable state in the record or under `MMB_HOME`, ships the overlay outside the plugin ("The plugin ships its knowledge read-only", L1034), and copies scripts into the record's `.work/tools/` (L345). `house-style.md` changes only at release (L311).
- Gap: `shared/sandbox-accounts.txt` (L73) is a user-edited file inside `shared/`; `leak-terms.txt` (L72) is shipped and may need per-user terms such as a firm name. Both break the rule if edited in place.

**13. Where a user's local settings live (monday account entries, firm name, GitHub account).**
- Lands in: 5.3 (L357) as a named settings file under `MMB_HOME`, listed in 7.1 (L458). Readers: `leak_lint.py` (firm name, L923), `ledger.py bind` and 8.2 step 4 (sandbox ids, L766), `archive_check.py` and 8.10 (GitHub account, L844), `monday-drift-check` (L301), the hook (never-demo ids, L973).
- Exists: the principle for GitHub only, D17 (L1166). The firm name sits in the leak denylist (L72, L923). Account entries sit in `sandbox-accounts.txt` (L73). The per-client binding is in `account.json` (L503) and is record data, not a user setting.
- Gap: no settings file; three kinds of user value live in three places. The publisher's name in `plugin.json` stays (allowed).

**14. Client records inheriting the instructions of the folder above them.**
- Lands in: the `project-instructions.txt` template (L158, L382), 8.2 step 3 (L765), and the hook's upward walk to the first folder holding `CLIENT.md` (L959).
- Exists: the six-line content (L382); a hook that already finds the record root by walking up. The plugin ships no `CLAUDE.md` on purpose (L169); that concerns the plugin package, not the user's folders.
- Change: write the shared instructions once at the folder above the clients and keep only client-specific lines in each client folder, as the input asks. Probe S0-8 (L1263) was the Cowork form of this question.

---

## 10. Open questions for the planner

Three findings are most likely to change the plan.

- The document has no home for A17, A18 or A19. It names no build-readiness component and no element kind, key, blueprint section, read-back, audit check, hook entry or probe for the AI offerings, and four rows conflict with A17 and A18 (L905, L1126, L1166, L1273). The re-cut rewrites that contract. It does not append to it.
- The record and version vocabulary is sales-shaped. `discovery.md`, `discovery_verdict`, `sop_behind`, the stage ladder, the `demoed` state, the v1.0 release rule and the call-type header (L424, L680–L686, L609, L629, L776) all sit in files that stage 2 scripts (`record.py status`, `check`) will read. They need a v1 definition before stage 2 starts.
- Three new inputs collide with existing rules. A workspace per client and per product runs against L903 and against native-board reuse. The lease simplification touches about twenty places (part 9, item 6). Local settings have no file, and the file meant to hold the user's account ids sits in a shipped folder (L73).

The open questions follow.

1. **No home for build-readiness.** Nothing in the document names the A19 check (part 3i). Which host: a new skill, a mode of `engagement`, or a section of `solution-blueprint`? Which file replaces `discovery.md` (L155, L424), which field replaces `discovery_verdict` (L684) and the briefing line (L756)? Does D7, "warn and log" (L1166), carry over, so a gap warns and logs the user's reason (L211) instead of blocking?
2. **What survives of the call-type header.** Thirteen labels (L454) and a header of four dimensions and two modifiers (L776) exist to scope the rubric. `output_class` is also read by the doors (L676, D26 at L1170), and scoping and working-session routing (L778) feeds the non-platform path (A13). Which tokens stay in v1, and where is the vocabulary pinned?
3. **Research.** Neither A19's v1 list nor its v2 list names company research, and A14 keeps research in the record. `research-scout`, `research.md`, `research/*` (L80, L139, L404–L406) and D25 (L1170) are tiered unclear. Is the post-build research agent (part 9, item 9) the same agent or a new one?
4. **Client card, handoff note, hand-off package.** `client-card.md`, `archive-handoff.md` (L414, L844) and `deliverables/handoff/*` (L444, L736) sit between record close (v1) and the handoff package (v2-or-v3). Which are v1? A18 wants a switch-off step "in the handoff" for anything the API cannot switch off (L913, L1176, L1279), so which v1 file carries those steps once the SOP is deferred? `close-out.md` (L157, L842) is the likely home.
5. **Rows that contradict A17 and A18 and must be rewritten, not appended.** L905 (exclusion list), L1166 (D24 "AI agents: out"), L1273 (deferred list), L1126 (C15, only v1-scope items probed). Of L905, `delete_*` stays out (A18) and bulk import stays a size limit (C12, L1124); A18 does not mention user invites and role changes, so their status is open.
6. **Workspace rule against native boards.** L903 prefers an existing workspace or folder. The new input asks for a new workspace per client and per product. Native CRM and Service boards sit in the account's own product workspaces, may not be moved, and are found across non-default workspaces (L1099, L1217, L1078). Who decides the workspace: the blueprint (L227) or preflight?
7. **Probes A20 does not rule on.** A20 keeps S0-1, S0-5, S0-6b, S0-7, S0-9, S0-12, S0-14 and drops S0-2, S0-3, S0-4, S0-8, S0-10. S0-11 (the old plugin, L1154, L1263), S0-13 (`gh` on the Mac, L1263) and S0-15 (the shared root, L1263) are not named, and S0-15 now reads as answered. This file also has no probe for any AI kind, although A17 and A18 put probes first.
8. **`gql_guard.py`** (L149, L371, L822, L933). A2 says no document-parsing guard is needed; 12.4 keeps a scan after the fact (L1177). Keep a 140-line script and its tests, or drop it?
9. **7.10 migration.** Nothing has shipped, so no `client/1` record exists. Drop 7.10, `record.py migrate` (L364), `.work/migration-sources/` (L456), the `migration` log type (L663), the live-map default (L730), gap 17's wording (L1160) and the risk row (L1292)? A general schema-upgrade mechanism (`versions.md`, L81) is a separate matter.
10. **`sandbox-accounts.txt`** (L73, L301, L766, L876, L973, L1153, L1294). The test account (A11-1) is open and the project rule bars account ids in project files. The never-demo half serves demo screens (v2). The v1 halves are the bind check that refuses a sandbox id on a client record and the reverse (L766, L365) and the sandbox-only write probes (L301, L876). Where do those ids live (part 9, item 13), and what becomes of `SANDBOX.md` and the sandbox Project (L158, L458)?
11. **Version labels carry sales meaning.** v0.1 is "First demo" in the gate names (L214), `demoed` is a state (L609), v1.0 needs R6 and R11 and sign-off evidence (L629), and the stage ladder has `demo` and `signed-off` (L680). With no demo in v1 and a two-round default, what do v0.1, v0.2 and a release mean, and what is sign-off?
12. **Blueprint section numbers are not in this file.** L227 says "sixteen and numbered" yet lists about thirty clauses and gives no numbers, so "AI opportunities" cannot be pinned to a section number. The numbering lives in `blueprint-guide.md`, which this file does not contain.
13. **Three new inputs run into open decisions.** The fast path with sample rows needs the sample-data answer (L1256). Email as an input needs the retention question to name emails (L1257). A new workspace per client touches the irreversible list (L903). None may be defaulted.
14. **Provenance of the lint trap list.** The shapes at L923 and the phonetic rule on the user's own firm name read as drawn from real calls, and the project rule is that nothing comes from them. Rewrite from scratch, or check provenance first? The same question applies to the "provisional" calibration rules the v2 files keep (L1261).
15. **Chat boundaries.** A10 is phrased as "a different Project and folder" (L759, L1185). Under A20 option A it is a session opened in the client's folder. Does the front door's nudge at heavy-work boundaries stay as written?
16. **Counts and dates that will move.** 111 files, ten skills, 30 references, 43 templates (L169); six model-invocable descriptions and the token target (L303–L305); four doors (L177); ten scripts (L1301); the 190-line body limit for a build skill that now carries the AI kinds (L179, L271). The ring-roll date "around 2026-10-01" (L1044) is before today. The title block and 12.4 stop at A16 (L3, L1172–L1192), and the document still calls itself the "Final v1 design" (L3).
