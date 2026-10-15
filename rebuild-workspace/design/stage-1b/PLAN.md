# Stage 1b — run plan

Written 2026-10-13 by the planner after the two document maps and the user's decisions of the same day (A21, A22, D6 closed, the superseded drafts retired). The run re-cuts SPEC, ARCHITECTURE and BUILD-PLAN under A17 to A22, refreshes ROADMAP and the review copies, and touches AMENDMENTS only to add decisions the user makes. Nothing in `shared/`, the fixtures or the answer keys changes in this run; section 7 lists what the fixture fix pass does afterwards.

Files in this folder: `map-architecture.md` and `map-build-plan.md` (line-anchored maps of the two big documents), `build-readiness-spec.md` (the check that replaces sales grading), this plan, and the run's own outputs (`arch-changelog.md`, `plan-changelog.md`, `spec-notes.md`, `check.md`, `fix.md`, `acceptance.md`).

## 1. What stage 1b must deliver (the acceptance list)

1. **Tiers everywhere, and agreeing.** Every package, template, skill, reference, script, agent, hook, test and release check in BUILD-PLAN carries `v1-core`, `v2` or `v2-or-v3`; every ARCHITECTURE section and named component is tiered or cut; ROADMAP and SPEC say the same. The tier tables in section 3 are the source.
2. **The build-readiness check is designed.** ARCHITECTURE has the skill, the strand file, the shape sketch and the flow (replacing 8.4); BUILD-PLAN has the package with its acceptance list, tests and fixture expectations; both match `build-readiness-spec.md` including its section 9.
3. **The AI offerings are in the main line.** Element kinds, element keys, live-map kinds, blueprint subsections (including "AI opportunities"), approval as lists with every recipient shown, the round-two default, build order, read-back rows, audit checks, recovery inventory, hook matcher scope, log types, probes P-19 to P-21 cited by their file, Vibe publication as its own irreversible yes, and account-level objects limited to the client's workspaces (A21). The four rows that contradict A17 and A18 are rewritten (ARCHITECTURE L905, L1126, L1166, L1273 before the edit).
4. **A20, A21 and A22 are folded in.** One surface, Claude Code on the Mac, with file-based equivalents noted wherever a Mac-only feature is used; the per-client build target with the workspace rule; never-demo by workspace; client folders in two phases; a generic default home; the first-run walkthrough; a local settings file; no state in the plugin folder; the leak lint as the wall between clients.
5. **The deferred layers are marked and moved out of the main line**: demo scripts, recap drafts, objection handling, the house voice, claims discipline in speech, the client SOP, the SOP tools, the doc copy, the demo check, the SOP drafter. Files kept, no skill built (section 2, D5).
6. **The stage order is rewritten** (section 4): 1 done, 1b, 2 scripts, 3 templates, 4 skills, agents and runner, 4b the AI offerings, 5 hooks, READMEs, scenarios, release and the end-to-end proof of concept, then v2 and v3.
7. **Agnostic and current.** No GitHub handle outside `plugin.json`; no account, workspace, board, user or automation id from any real account (monday's own template catalogue ids may stay); no earlier plugin or setup named; no person or firm other than the publisher; no reference to the retired proposals, judges, critique or revision notes; no date that has already passed stated as future. The inline sweeps in section 6 prove it.
8. **Counts and headers recomputed**: file, script, template, skill, agent and reference counts; the always-on token target; script line budgets; the title blocks name A1 to A22 and the revision date.
9. **SPEC rewritten** to the new shape in about two pages; ROADMAP's checklist and stage table current; the review copies refreshed; `for-review/00-READ-ME-FIRST.md`, `HANDOFF.md` section 7 and the status lines of `INTERVIEW-NOTES.md` and `FEEDBACK.md` updated.
10. **One consistency check and one fix pass**, both recorded in this folder, and an acceptance report that walks this list.

## 2. Decisions the planner took (worth the user's nod)

Each is applied by the editors unless the user objects. The map question it answers is cited as `A-Qn` (architecture map, part 10) or `B-Qn` (build-plan map, section 9).

- **D1. Readiness home** (A-Q1, B-Q5, B-Q8). A skill of its own, `build-readiness`, model-invocable, with one reference `readiness-guide.md`; the strand file `readiness.md` replaces `discovery.md`; in BUILD-PLAN it is a new package, WP19, so WP8 shrinks to `engagement` and `call-intake` and the hardest paragraph to cut is not cut by clause. `solution-blueprint` reads the clearance: `not yet` stops the blueprint unless the user overrides with a reason, logged as `override` and kept visible on `STRAND.md` (D7's warn-and-log carries over). `account-build` needs an approved revision, which needs a clearance or an override, so it checks nothing new.
- **D2. Clearance words** (B-Q3, B-Q6). The check says `cleared to build`, `cleared to build, generic` or `not yet`. The audit report ends with `cleared to show` or `not cleared to show`. The version event `shown` replaces the `demoed` state and is recorded by the user; `v1.0` means the client has signed off the build as their working system, an event the user records, with no criteria behind it.
- **D3. The call-type header** (A-Q2, B-Q10, HANDOFF carry-overs). Intake keeps proposing all six tokens, because the keys grade them and the detection exists; in v1 only `output_class`, `direction` and `room_shape` drive behaviour, and `seat`, `relationship` and `money_live` are marked v2 in the vocabulary. The type header's one v1 job beyond routing is telling our side's framing from the client's words. Spelling: hyphenated tokens everywhere, the record map wins. The two-attendee call: `small-group` widens to "two or more client attendees" and the pin says so, rather than a new token in three places. `direction_of_show` in the fifteen keys is renamed to `direction` in the fix pass; the pin does not move.
- **D4. Stage order and the AI offerings** (B-Q1, B-Q2, A§7 reading b). The AI kinds are designed now, in this run, which is A17's "design pass over the architecture and the build plan". Their build is stage 4b: additions to the files WP1, WP3, WP4, WP7, WP9, WP10, WP13 and WP15 own, sequenced after stage 4 rather than beside it, so the one-owner rule holds by order. In the product they are round two of a strand by default, a new version with its own card, build and audit, and round one when the client asked for AI or workflows.
- **D5. Where v2 files live** (B-Q4). Out of the shipped tree. The repo gains `deferred/` at its root, outside `plugins/`, holding `sales-method.md`, `house-style.md` and, when they are written, the v2 and v2-or-v3 skills, templates and scripts. They stay out of the always-on token count and the lint. Moving the two existing files is a fix-pass item.
- **D6. Release checks** (B-Q20, map section 4). Check 1 drops the earlier plugin and reads "no other monday-building plugin is enabled (S0-11)". Check 8 becomes the agnostic sweep: a tool `tools/agnostic_sweep.py` that fails on a personal name from the local name index, a GitHub handle outside `plugin.json`, a long numeric id outside the template catalogue list in `native-objects.md`, an earlier plugin's name, a firm name other than the publisher, and a reference to a retired file; `cleanroom_scan.py` and its tests are retired, since the corpus it compared against no longer exists, and the clean-room rule stays a rule; `leak_lint.py --terms` stays a capability and leaves the release list. Check 2 reads "the Mac's Python 3.9 and the newest installed Python 3". Check 12 becomes a Code-side install smoke test.
- **D7. `gql_guard.py` is dropped** (A-Q8). A2 says no query guard; the audit's write detection rests on snapshots and the document scan.
- **D8. Migration is dropped** (A-Q9, B-Q22). 7.10, `record.py migrate`, `.work/migration-sources/`, the `migration` log type, the live-map migration default and H38 go; nothing has shipped. A `schema_version` field stays on the record, with upgrades designed when a second schema exists.
- **D9. `sync_shared.py` and the copy ladder are dropped** (B-Q21). S0-1 passed, so skills name scripts through the plugin root; the ladder is "plugin root, else fail closed". `.work/tools/` goes with it.
- **D10. The lease** (A-Q item 6, B-Q16). The within-record lease stays as the guard against an interrupted or duplicated run (lock, heartbeat, epoch fence, break with the user's yes). The cross-client `leases.json` and its contention design go; before the first write of a run the build asks the one question, "is another build running anywhere?", and logs the answer. The hook reads the record's lock only.
- **D11. Local settings and the home** (A-Q10, B-Q13, B-Q15). `MMB_HOME` defaults to `~/monday-builder/`, overridden by the `MMB_HOME` variable, which the first-run walkthrough sets; during build and test this user's value is `~/DelOps` (A22). Under the home: `clients/`, `cards/`, `monday-knowledge/`, and `local/` with `settings.json` (the user's GitHub account for the archive, the firm name and its renderings for the leak list, the default build-target account, the operational workspaces that are never on a shared screen), `sandbox-accounts.txt` (moved out of `shared/`, same syntax) and `leak-terms.txt` (per-user additions). The shipped `sandbox-accounts.txt` is retired and `leak-terms.txt` ships without a firm class. `claims/` is not created in v1 (D13).
- **D12. The first-run walkthrough.** A reference `first-run.md` under `engagement` plus `record.py home init`: creates the home tree, writes `local/settings.json` from a few questions, checks Python, the connector, `gh`, warns when a `CLAUDE.md` sits above the clients folder, and explains the two doors. Runs once, and again on request.
- **D13. The claims store is v2** (B-Q17). What A19 keeps lives in the gotcha list's never-say block and the irreversible table; the blueprint marks any unprobed kind as unprobed. `engagement` no longer creates a claims file.
- **D14. Research stays in v1** (A-Q3, B-Q19). One agent, `research-scout`, two modes: a quick brief before the first build when time allows, and the deep dive after round one, feeding round two and the sample data (Q2, Q14). `research/*` is v1.
- **D15. Close-out files** (A-Q4). `close-out.md` carries ownership and the switch-off steps; `client-card.md` and `archive-handoff.md` are v1 because the record close needs them; `deliverables/handoff/*` is v2-or-v3.
- **D16. Docs are an element kind in v1** (B-Q18). A build may create monday docs from blueprint text with read-back; the chunking rule lives in the build loop; `doc-copy.md` (the SOP copy) stays deferred and `sop_tools.py` is not built.
- **D17. Fixtures** (B-Q23). All 25 stay v1 fixtures; the keys keep their sales blocks marked v2; the fix pass adds the `readiness` block; v1 graders read `intake`, the pains, products, structure, forks and `readiness`. s21 becomes the central existing-account case under A21.
- **D18. Test ids** (B-Q24). Numbering kept; deferred rows marked v2; H30 and H31 become the two readiness cases that need constructed inputs (an unresolved cross-call conflict blocking an entity; a structure that copies the incumbent's tool); new H rows for the walkthrough, the workspace rule and the AI kinds; new T rows: a write refused outside the client's workspaces, one scenario per AI kind, the cross-product automation. Check 6's ranges are recomputed.
- **D19. Blueprint sections** (A-Q12). Sixteen numbered sections stay; new content sits inside them as named subsections: "what this build rests on" in section 1, "AI opportunities" in the requirement trace, the workspace plan in the binding section. `blueprint-guide.md` pins the numbers in stage 4.
- **D20. Chat boundaries** (A-Q15). A10 rephrased for the Code side: a new session per client folder, a fresh session for a build or an audit, otherwise the same session; the nudge stays.
- **D21. Versions.** `v0.1` is the first proof of concept (round one), `v0.2` the AI layer by default; `shown` and `signed-off` are events; a release condenses after either.
- **D22. Never-demo in v1** (B-Q15). The operational workspaces live in `local/settings.json`; because the plugin never writes outside the client's workspaces (A21), the v1 mechanism is a reminder: the briefing names them whenever a version is `audited`, and the first-run walkthrough records them. Screen scripting itself is v2.
- **D23. History inside the documents.** ARCHITECTURE section 0 keeps a short lineage paragraph without proposal names; 12.1 and 12.2 fold their still-live decisions into 12.3; 12.5 goes; 12.7 keeps its two intake rows; 12.4 keeps one row per amendment, A1 to A22. BUILD-PLAN section 6 is replaced by the new conflicts: readiness against the discovery check, the AI kinds against the exclusion list, one surface against two, the workspace rule against the old "prefer an existing workspace" line.
- **D24. The leak-lint trap list** (A-Q14). The trap shapes are restated as categories from the rule, not from any call; the firm class moves to local settings (D11).
- **D25. Python and PDFs** (B-Q25, B-Q26). Scripts run on 3.9 and newer and are tested on what the Mac has; a PDF's text is read by the session itself page by page when no text tool exists, and the intake records that it did.
- **D26. Native boards inside a client's own workspaces** (A-Q6). A client's CRM or Service workspace is created in that product; after creation the native entity set is detected inside it; if the product did not install native boards there, the plugin asks the user to add the product's board set from monday's UI, a UI step with an owner, and never builds look-alikes (A5). Whether creation installs them is probe P-22, run when A11-1 is answered.

## 3. Tier tables (the source the editors follow)

**Skills, agents and scripts**

| Component | Tier |
|---|---|
| `engagement`, `call-intake`, `build-readiness` (new), `solution-blueprint`, `account-build`, `solution-audit`, `client-closeout`, `monday-drift-check` | v1-core |
| `demo-script` | v2 |
| `client-sop` | v2-or-v3 |
| `transcript-summarizer`, `solution-auditor`, `research-scout` | v1-core |
| `sop-drafter` | v2-or-v3 |
| `mmb_common.py`, `record.py`, `ledger.py`, `leak_lint.py`, `transcript_measure.py`, `transcript_prep.py` (without `delivery`), `archive_check.py` | v1-core |
| `demo_check.py` | v2 |
| `sop_tools.py` | v2-or-v3 |
| `gql_guard.py`, `sync_shared.py`, `cleanroom_scan.py`, `record.py migrate` | dropped (D7, D8, D9, D6) |
| `tools/agnostic_sweep.py` (new), `tools/lint_plugin.py`, `tools/release.sh` | v1-core |

**Shared files and templates**

| Component | Tier |
|---|---|
| `record-map.md`, `safety.md`, `monday-gotchas.md`, `read-back.md`, `native-objects.md`, `leak-terms.txt` | v1-core |
| `sales-method.md`, `house-style.md` | v2, moved to `deferred/` |
| `sandbox-accounts.txt` | retired from `shared/`; its syntax lives in `local/` (D11) |
| Record templates: `CLIENT.md`, `log.md`, `meetings.md`, `account.json`, `live-map.md`, `sources.md`, research files, `call-summary.md`, `document-summary.md`, `readiness.md` (new), and per strand `STRAND.md`, `SUMMARY.md`, `blueprint.md`, `backlog.md`, `allowlist.md`, `exclusions.md` (new), `build.json`, `open-questions.md`, `dependencies.md`, `structure-inventory.md`, `scope.md`, `version.md`, `audit.md`, `close-out.md`; other: `admin-prerequisites.md`, `automation-card.md`, `client-card.md`, `archive-handoff.md`, `agent-prompt.md` (new), `SANDBOX.md` | v1-core |
| `discovery.md`, `gaps.md`, `recap-draft.md`, `prep-sheet.md`, `demo-script.md`, `claims-ledger.md` | v2 |
| `SOP.md`, `flow-spec.json`, `export-manifest.md`, `mermaid-config.json`, `puppeteer-config.json`, `sop-reference.docx` | v2-or-v3 |
| `project-instructions.txt` | surface-later (Cowork) |

**Packages** (BUILD-PLAN; the split column names what leaves the v1 acceptance)

| Package | Tier | Leaves the v1 acceptance |
|---|---|---|
| WP-S0, WP0 | v1-core, complete | |
| WP1 | split | `sales-method.md`, `house-style.md`, the sales fields of the header pin, the demo and voice clauses; gains the readiness shape and clearance strings, the AI-kind gotcha areas and read-back rows |
| WP2 | v1-core | `migrate`, the `sop/` clause; gains `home init` and the exclusions file |
| WP3 | v1-core | `gql_guard.py`; gains ledger rows and approval classes for the AI kinds and the workspace scope check |
| WP4 | v1-core | gains the cross-client wall and the AI-kind payloads |
| WP5 | split | `delivery` |
| WP6 | v2-or-v3 | whole |
| WP7 | split | the v2 and v2-or-v3 templates above; gains `readiness.md`, `exclusions.md`, `agent-prompt.md`, the blueprint subsections |
| WP8 | split | `discovery-check` and its two references, the recap half, the claims clauses; keeps `engagement` and `call-intake`; gains `first-run.md` |
| WP19 (new) | v1-core | the readiness skill, reference, template words and tests |
| WP9 | v1-core | `doc-copy.md`, the S0-15 clause; gains the AI kinds, round two, the workspace plan and rule |
| WP10 | v1-core | gains an audit check per AI kind and the "cleared to show" line |
| WP11 | split | `sop-drafter`; `research-scout` gains its second mode |
| WP12 | split | `demo-script`, `client-sop`; keeps `client-closeout` and `archive_check.py` |
| WP13 | split | the voice-bank step, [L17] and [L18]; gains matcher scope for the AI tools and the one-surface wording |
| WP14 | split | run-sheet graders and sales-field grading; gains readiness and AI-kind expectations |
| WP15 | v1-core | gains scenarios for the workspace rule and the AI kinds; T7 is v2-or-v3 |
| WP16 | v1-core | `sync_shared.py`, `cleanroom_scan.py`; gains `agnostic_sweep.py` |
| WP17 | v2 | whole |
| WP18 | split | the sales fields of the keys; the fix pass adds `readiness` |

## 4. The stage order after 1b

```
stage 1   done: WP0, WP1's v1 files, WP18 and its fix pass (after this run), WP16's lint
stage 1b  this run
stage 2   WP2, WP3, WP4, WP5 (no delivery), agnostic_sweep.py
stage 3   WP7's v1 templates, the readiness template, the agent-prompt template
stage 4   WP14's runner, graders and seed records first; then engagement, call-intake,
          build-readiness, solution-blueprint, account-build, solution-audit,
          monday-drift-check, the three agents, client-closeout
stage 4b  the AI offerings across WP1, WP3, WP4, WP7, WP9, WP10, WP13, WP15, in that order
stage 5   hooks, READMEs, fixtures copied in, sandbox scenarios, release tooling,
          the end-to-end proof of concept in the test workspace (A11-1 asked first)
v2 / v3   the sales layer, then the SOP layer, from deferred/
```

## 5. The run: agents, ownership, order

Six agents, each owning whole files, each writing its result file as it goes, each returning only a path and a headline.

| Agent | Model and effort | Owns | Reads | Writes |
|---|---|---|---|---|
| E1 architecture editor | session model, high | `ARCHITECTURE.md` | `map-architecture.md`, this plan, the readiness spec, AMENDMENTS A17–A22, INTERVIEW-NOTES, the stage-1b entries of FEEDBACK, `ai-offerings-findings.md`, `tests/stage0/results.md` | the re-cut file in place, section by section with the Edit tool; `stage-1b/arch-changelog.md` |
| E2 build-plan editor | session model, high | `BUILD-PLAN.md` | `map-build-plan.md`, this plan, the readiness spec, the same amendments and notes | the re-cut file in place; `stage-1b/plan-changelog.md` |
| E3 spec writer | session model, high | `SPEC.md` | this plan, the readiness spec, AMENDMENTS, ROADMAP, the two maps' summaries | the new SPEC, about two pages; `stage-1b/spec-notes.md` |
| E4 refresher | Sonnet, medium | `ROADMAP.md`, `for-review/01-SPEC.md`, `02-AMENDMENTS.md`, `03-ROADMAP.md`, `00-READ-ME-FIRST.md`, the status lines of `INTERVIEW-NOTES.md` and `FEEDBACK.md`, HANDOFF section 7 | the three re-cut documents | the refreshed files |
| V1 checker | session model, high | `stage-1b/check.md` | everything above | anchored findings: file, line, type (wrong, missing, unclear, inconsistent), severity |
| F1 fixer | session model, high | the files the findings name | `check.md` | the fixes; `stage-1b/fix.md` |

Order: E1, E2 and E3 in parallel (no shared files); then E4; then V1; then F1; then the planner's inline sweeps and acceptance report. The editors keep the `##` numbering of ARCHITECTURE stable so BUILD-PLAN's `A§n` citations still resolve, and renumber only inside a section. Both long documents are edited in place and saved after every section; a full-file rewrite in one write is not allowed.

Briefs for E1 and E2 are the maps' numbered parts plus sections 2 to 4 of this plan. Each must-do item in the maps (part 10 of the architecture map, section 9 of the build-plan map) is answered either by a decision above or by the editor, and the changelog says which.

## 6. The consistency check, and the inline sweeps

V1 checks: tiers agree across the four documents; the vocabulary of section 2 is used identically and no `discovery.md`, `discovery_verdict`, `demoed`, gate or verdict word appears in v1 text; every `A§` citation in BUILD-PLAN resolves and every package named in ARCHITECTURE exists; each of A17 to A22 has a stated home; the readiness spec's nine parts, three clearance values and shape appear in both documents and the audit's "cleared to show" line exists; counts agree between the documents; the prose is calm and says "the user"; the review copies are identical to their originals; ROADMAP's stage table and HANDOFF's state match the files.

The planner runs after F1: the handle sweep (one hit, `plugin.json`), the long-id sweep (nothing outside the template catalogue), the earlier-plugin and retired-file name sweep (nothing), the "Cowork as primary surface" read of the three documents, and the stage-1b acceptance report against section 1.

## 7. What this run leaves for the fixture fix pass and stage 2

- Fix pass (done 2026-10-13; logs, verifier reports and the closing record in `rebuild-workspace/fixtures-work/_fixpass/`), in this order: the `readiness` block on all 25 keys; `direction_of_show` renamed to `direction`; the FEEDBACK sweep list over all 25 keys; the s11 mess pass and the other fixture edits recorded in FEEDBACK; the `small-group` widening; `readiness/1` and the clearance strings pinned in `record-map.md` with the grading values fenced as v2; `sales-method.md` and `house-style.md` moved to `deferred/`; `sandbox-accounts.txt` retired from `shared/`; the firm class removed from `leak-terms.txt`; then one verification over the keys and the shared files.
- Probes that wait for A11-1: P-22 (does creating a CRM or Service workspace install the native boards), P-23 (can an automation or workflow act across two product workspaces), P-24 (can an agent's access be limited to named workspaces), P-25 (a formula result landing in a real date column for alerts, from s19).
- Stage 2 starts from the re-cut BUILD-PLAN, with WP2 first.

## 8. Open for the user

- The nod on section 2, in particular D1, D2, D4, D5, D6, D11 and D14, which change what the user will see.
- The readiness spec's two open items: decided 2026-10-13, five questions and the card (its section 8).
- The nod on section 2 was given on 2026-10-13 and the run started the same day with multi-agent mode on for it.
- The go for the run, and multi-agent mode switched on for it.
