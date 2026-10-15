# Stage 1b: BUILD-PLAN.md changelog

Written 2026-10-13 by the build-plan editor (E2) while re-cutting `rebuild-workspace/design/BUILD-PLAN.md` under `stage-1b/PLAN.md` sections 2 to 4, `build-readiness-spec.md` and A17 to A22. One entry per section as it was edited, each naming what changed and the plan decision (D1 to D26), amendment or map item it answers. Method: the document was edited in place one heading-delimited section at a time and saved after each, never regenerated in one write; where a section was a single very long line, the whole section was replaced from a prepared file.

## Entries

### Title block
- Revision note rewritten: revised 2026-10-13 under A17 to A22, A1 to A22 cited, the tier vocabulary stated; the authority line kept (plan acceptance item 8; must-do 1). The references to the earlier calibration file and the revision-notes file are gone (map 7.4 L3, L5); "the calibration reversed a rule" now reads "the fixture review reversed a rule".

### Section 0
- A11-1 row: the workspace name, its id and "the user's current monday account" removed; now "every write probe and every sandbox scenario waits for the workspace the user names" and P-22 to P-25 named as waiting on it (must-do 2; map 7.2 L17; PLAN section 7). WP-S0, WP1 and WP2 dropped from its carriers (WP-S0 is complete, map 6.5 L17).
- A11-2 row scoped by A21: the user's own account needs no decision; a client's own account asks once before the first revision there that plans sample rows (A21; D17 makes s21 the central case, so H47 joins its tests).
- A11-3 row: "the calibration's own working practice is recorded in A§13 as a candidate answer" removed (map 7.4); otherwise kept.
- The mechanical rules reworded for the scoped A11-2 and "a fresh session" (A20).
- The four-question table gains a tier column: L14 and L15 stay v1 (L15 now points at the readiness block instead of `discovery.md`, D1 and A17), L17 and L18 are marked v2 with their packages (WP17, `demo-script`) and no v1 carrier (must-do 2; map 8.3 tag tables). L14's carriers now WP7, WP9, WP19.
- The provisional-rules paragraph keeps only the intake rules; the delivery-calibration rules travel with the sales layer (must-do 2; map section 4 check 10).

### Section 1
- The order diagram is PLAN section 4 verbatim in shape (D4, acceptance item 6; must-do 3).
- "Why stage 0 stays first" is one line pointing at `tests/stage0/results.md` (A20; map 2.3, 6.5 L42, L66).
- The schema paragraph adds `readiness/1`, the three clearance strings and the audit's closing line as pinned in `record-map.md` in the fix pass, fences the grading values as v2, and marks `seat`, `relationship` and `money_live` v2 with hyphenated tokens everywhere (D1, D2, D3; spec sections 7 and 9).
- The fixtures paragraph records the review complete on 2026-10-13 and the fix pass after this run in PLAN section 7's order; "calibration fixtures" renamed "intake fixtures" and the earlier calibration file no longer cited (D17; map 7.4).
- The parallelism paragraph explains stage 4b and the round-two default (D4).
- "Three sequencing defects" and "four schedule splits" (history, map 7.4 L74, L76) replaced by the two splits that still hold; `cleanroom_scan.py` replaced by `agnostic_sweep.py` (D6, D9); `record.py home init` added to the stage-3 acceptance (D12).

### Section 2, WP-S0 and WP0
- WP-S0: tier v1-core, complete; the probe list collapsed to what the results established on the Code side, with the two design facts (no state in the plugin folder; `CLAUDE.md` inheritance, A22); the "old plugin" wording of S0-11 now "no other monday-building plugin"; `cowork-capabilities.md` and the S0-12/14/15 yes-or-no acceptance gone (A20; map 2.3, 6.5 L84–L90, 7.3 L88; must-do 4).
- WP0: tier v1-core, complete; `plugin.json` named as the one file that may carry the handle; `deferred/` added at the repo root (D5; PLAN acceptance 7).

### Section 2, WP1
- Tier split, with the leaving list (sales files, sales fields of the header, demo and voice clauses) and the gains (readiness shape and strings, AI-kind gotcha areas, read-back rows) stated (PLAN section 3 packages table; must-do 4).
- Bullet 1 (R1–R12, gates, scope matrix) and bullet 8 (`house-style.md`) leave; `record-map.md` fences the grading values (D1, D2; map 1.2 WP1).
- `record-map.md` bullet gains `readiness/1`, the three clearance strings and the audit's two closing strings, `shown` and `signed-off`, the `override` log type, the AI-kind log types and element keys, `readiness.md` and `exclusions.md` rows, the home tree with `local/`, hyphenated tokens, `small-group` widened, `direction`, the three sales fields marked v2, the fork `leaning` (D1, D2, D3, D11, D21; spec section 7; FEEDBACK s24 schema note).
- Gotchas bullet: "no entry is written from a learn file" removed (map 7.3 L109); "`demo-script` reads it at generation" replaced by the blueprint reading the never-say block (A19); the AI-kind areas added from `ai-offerings-findings.md`, with the unprobed kinds marked (A17, A18; PLAN acceptance 3).
- Native-objects bullets: "all 43 natives read" generalised; template catalogue ids named as the permitted long-id class (D6); D26 stated with P-22.
- `safety.md` bullet: the delivery-exposure rules of A§9.11 replaced by the approval classes per kind, the workspace rule (A21), never-demo by workspace (D22), the lease without the cross-client file and with the one question (D10); the credential rule kept.
- `read-back.md` bullet gains docs, forms, dashboards, automations and the AI kinds (A18, P-19 to P-21; PLAN acceptance 3).
- `sandbox-accounts.txt` bullet replaced by the `leak-terms.txt` without a firm class and the trap categories from the rule (D11, D24; map 7.2 L116).
- `cleanroom_scan.py` bullet replaced by the agnostic sweep (D6; map 7.3 L117).
- Size: gotchas 520 after stage 4b, named as a size resolution for A§10.2 (map 8.3 gotcha budget); total about 1,700 lines without the deferred files.
- For the checker (map 8.3): A§10.2 gotcha budget and A§7.1 home tree should say the same; A§2 should list `readiness.md`, `exclusions.md` and `agent-prompt.md`.

### Section 2, WP2
- Tier v1-core; `migrate`, the `client/1` tree and H38 out (D8); the `sop/` clause out (v2-or-v3); `leases.json` and "where reachable" out (D10, map 6.5 L125); `home init` with `local/settings.json` in (D11, D12, A22); the generic default home with the user's value in the environment (D11); `readiness.md` and `exclusions.md` placed by `strand open`, with `check` rules for the verdict string and a missing exclusions file (D1, Q14); `version event shown|signed-off` (D21); an email taken in as documents (A16, Q7, map 9.5); Python 3.9 and newer tested on what the Mac has (D25); "chat" became "session" (A20, D20); H57 added to its tests.
### Section 2, WP3
- Tier v1-core; `gql_guard.py` out (D7); `bind` records the build target and refuses an operational workspace (A21, D11); the scope check that refuses writes outside the strand's build-target workspaces and account-level references outside the client's workspaces (A21; PLAN acceptance 3); rows and approval classes per element kind, Vibe and workflow publications as rows of their own, `verify` rules for agents and Vibe apps (A17, A18, P-19, P-20); `estimate` names AI-powered elements with no credit figure (A17); `compare` watches agent `version_id` and workflow state; D26's empty-native-set wording; the one question logged at `run start` (D10); H58's ledger half added.
- Agnostic: the earlier setup's `results/*.json` and `live-tests/*` inputs, "58 of the 67 boards", the past date 2026-10-01, the "67 boards across 19 workspaces" and "33 boards" counts, "the account's flagship natives", the renamed "Accounts board with terminology Org" all removed; the fixtures now state their own totals (map 7.2 L131, L139, L141, L142; 7.5 L131).
### Section 2, WP4
- Tier v1-core; `--payload` covers the AI-kind payloads and the strand's exclusions (A17, A18, Q14); the cross-client wall through hashed digests in `clients-index.json` (A20; map 9.3 Q14); the firm-name rule reads `local/settings.json` (D11, D24); trap list as categories (D24); fixtures gain two planted client records.
### Section 2, WP5
- Tier split; `delivery` out with the report block reserved (A19; map 1.2 WP5); `type` keeps all six fields with hyphenated tokens, `small-group` widened, the three sales fields marked recorded-not-read, and the framing job named (D3); PDFs read by the session when no tool exists (D25); email as a document (Q7); "ran; not evaluable" (FEEDBACK s22); no date pinned from a weekday (FEEDBACK s15); the alias-map one-entry rule (FEEDBACK cross-fixture); "calibration fixtures" now "intake fixtures"; "the buildability check" history removed (map 7.4 L162); the voice-bank eligibility field removed from the report (map 9.2 Q11, decided here with D3's v2 marking: the fields that only the voice bank reads leave with it).
### Section 2, WP6
- v2-or-v3 stub, files under `deferred/` when built; docs as a v1 kind explained with the chunk rule in `build-loop.md` (D5, D16).

### Section 2, WP7
- Tier split with the three lists (33 v1 files including the three new templates and three research files; six v2 and two v2-or-v3 in `deferred/`; `project-instructions.txt` surface-later) (PLAN tier table; D5; A20).
- Gains `readiness.md` (nine parts, `readiness/1`), `exclusions.md`, `agent-prompt.md` (A17), the blueprint subsections "what this build rests on", "AI opportunities" and the workspace plan inside the sixteen sections (D19), the parent-row-with-roll-up pattern (FEEDBACK cross-fixture), the fork `leaning` (FEEDBACK s24), the build target and workspaces on `CLIENT.md` and `account.json` (A21), `shown` and `signed-off` events in place of the two flags (D21), the clearance and `override` on `STRAND.md` (D1), switch-off steps per kind in `close-out.md` (A17, A18, D15), `client-card.md` and `archive-handoff.md` as record-close outputs (D15), `SANDBOX.md`, "the user's own domain" in place of "our own domain" (map 7.6 L193).
- Leaves: run-sheet, recap, claims ledger, the demo inventory and deferred-answer register, who-has-seen-what, `discovery.md` and `gaps.md`, the SOP cover (A19; map 1.2 WP7). The `project-instructions.txt` acceptance clause removed (A20).
- Research files counted as three so the template total reconciles (43 + 3 new = 46; see section 3 entry). For the checker: A§6 should name the three research files and the three new templates.
### Section 2, WP8
- Tier split; `discovery-check`, `rubric.md`, `prep-and-objections.md` out (A19, D1); `first-run.md` in (D12, A22); the build target and the time budget asked at setup (A21, Q2); no claims store (D13); research brief offered (D14); session boundaries rephrased for the Code side (D20); the briefing counts questions blocking clearance and names the never-demo workspaces at `audited` (D1, D22); the readiness check named as what the front door runs after every intake (D1, spec section 1); the evidence law homed in `transcripts.md` (map 9.2 Q7, decided here: the non-evidence, conflict and citation rules are intake law and live in the intake reference, not in the deferred method file); the committed-not-done line (FEEDBACK s21); the unconfirmed-signal carry-forward (FEEDBACK s11); pivot wording (Q13); `summary-and-recap.md` keeps its name with the summary half only, flagged for the checker against A§2; the pricing and call-review routing refinements marked as leaving (map 1.2 WP8); H-list recomputed (H18, H33 out; H57 and the intake half of H56 in).
### Section 2, WP19 (new)
- The build-readiness package, acceptance list built from `build-readiness-spec.md` sections 1 to 3 and 8 to 9 and the map's 5.3 reconciled to D1 (own skill, one reference, `readiness.md`, the blueprint as consumer with the override) and D2 (three strings here, "cleared to show" in the audit) (must-do 4; PLAN acceptance 2). Map 5.3 items 1 to 14 each have a bullet; item 5's "cleared to show" moved to WP10; item 7's evidence home is `transcripts.md` and `record-map.md`; item 12's cap is five (spec section 8); item 13's fixture expectations per D17.
### Section 2, WP9
- Tier v1-core; `doc-copy.md` and the S0-15 clause out (D9, map 6.5 L212); reads the clearance and logs the override (D1); the card opens with "what this build rests on"; the workspace plan and rule (A21, Q8, Q9, Q13; D26); `ai-elements.md` with the AI kinds, round two, publication yeses, the build order with agents last (A17, A18, D4; P-19 to P-21; PLAN acceptance 3); the one question before the first write (D10); docs with the chunk rule (D16); `gaps.md` and the claims path replaced by `open-questions.md`, `readiness.md`, `exclusions.md` and the research files; sample data scoped by A21; probe ids P-26 to P-28 used for AI columns, sequences and webhooks (new ids after PLAN section 7's P-22 to P-25; for the checker against ARCHITECTURE's probe list); H-list recomputed (H09 out, H58 to H63 in).
### Section 2, WP10
- Tier v1-core; the closing line `cleared to show` or `not cleared to show` with the never-demo workspaces beside it (D2, D22); `ai-checks.md` with one check per AI kind (A17, A18, P-19 to P-21); the A21 nothing-written-elsewhere assertion; the drift check's probe set extended to P-19 to P-28; "verdict" wording removed from the audit text (V1 vocabulary check); audit halves of T25 to T30 cited.
- For the checker: A§2 should list `ai-elements.md` (WP9) and `ai-checks.md` (WP10); A§3.8 the closing line.

### Section 2, WP11
- Tier split; `sop-drafter` out to `deferred/`; `research-scout` v1 with its two modes and the `[I]` rule (D14, Q2, Q14); the S0-5/S0-6b fallback sentences removed (A20; map 6.5 L247).
### Section 2, WP12
- Tier split; `demo-script` and `client-sop` reduced to deferred stubs (A19, D5); close-out keeps strand close, record close, archive and cleanup with switch-off steps per kind (A17, A18, D15), `client-card.md` and `archive-handoff.md` at record close (D15), the pivot rule (Q13), one command name on one surface (A20; map 2.3 L254), the archive account from `local/settings.json` (D11), the `gh`-absent manual steps as the file-based equivalent without the probe name (map 6.5 L254), no `sop/` or `deliverables/` in the archive list (v2-or-v3).
### Section 2, WP13
- Tier split; matcher scope for the agent, Vibe, workflow, sequence, AI-column and webhook tools with the ask-and-ledger-refuses design for account-level objects (A17, A21; PLAN acceptance 3); the hook reads the lock only (D10); the sibling-client target in the tests (A20); README one surface with the install path, the default home and the walkthrough, file-based equivalents noted (A20, A22); S0 results stated as facts (map 6.5 L266); [L17] [L18] out, [L14] [L15] kept (must-do 2); the voice-bank step out (map 1.2 WP13); P-22 to P-28 and `deferred/` in MAINTAINING; the guard specification cited from `native-objects.md` instead of the earlier setup's json (map 7.5 L260). "names no other plugin" added.
### Section 2, WP14
- Tier split; v1 graders read the fields D17 names plus `readiness`; the readiness grader with the two review checks, the ceiling and the AI-kind expectations (D17, spec section 6; PLAN acceptance 3); r14 added; the seed home carries `local/settings.json` and a `clients-index.json` digest and no claims store (D11, D13); `tests/README.md` says no other monday-building plugin (map 7.3 L277); the `fixtures-work/` scratch scripts sentence removed (map 7.5 L277); the run-sheet graders, the r7 plants, the three status values and the 25-field grading marked as leaving.
### Section 2, WP15
- T24 to T31 added (a write refused outside the client's workspaces; one per AI kind; the cross-product automation), T7 marked v2-or-v3 (D18); P-19 to P-21 cited by their file; P-22 to P-28 listed as waiting for the test workspace (PLAN section 7); the `leases.json` plant removed from T9 (D10); `live-tests/manifest.json` input removed (map 7.5 L283); cleanup per AI kind.
### Section 2, WP16
- `agnostic_sweep.py` in per D6; `sync_shared.py` and `cleanroom_scan.py` out (D6, D9); lint gains the `deferred/` link rule and the no-state-in-plugin rule; the name index moves under `local/` (D11).
### Section 2, WP17
- v2 stub; the never-demo rule's v1 home named (D22; map 9.3 Q15).
### Section 2, WP18
- Tier split, complete with review closed 2026-10-13 and the fix pass after this run (D17); the `readiness` block, `direction`, `small-group`, the fork `leaning` and the FEEDBACK sweep list written into the fix-pass acceptance (D3, D17, spec section 6, FEEDBACK cross-fixture entry); the earlier calibration file and its lessons rows gone, "intake fixtures" used, the grading passes of s25 marked v2 (map 7.4; map 1.2 WP18); `cleanroom_scan.py` replaced by `agnostic_sweep.py` as the precondition (D6); the fixtures workspace located without an absolute path (map 7.5 L364).

### Section 3
- Ownership table rebuilt: 94 rows (90 installed plus four repo-root), owners for the new files (WP19's skill and reference, `first-run.md` under WP8, `ai-elements.md` under WP9, `ai-checks.md` under WP10, the three new templates under WP7), `archive_check.py` kept with WP12 now that WP12 is the close-out package (map 8.1 L326), `gql_guard.py` gone, `shared/*` at six (must-do 5; map 8.1).
- The deferred files listed with tier and no v1 owner, 27 in all, future owner in brackets (D5; PLAN acceptance 1).
- Slips of map 8.2 fixed: H30 and H31 now owned by WP19; H09 moved from WP9 to WP19; the double listings resolved by the "one package of record" paragraph; H19 owned by WP12 with WP2 supplying the subcommand; H47's "H03's s2 grade" is fixed in the 4.4 row.
- History paragraphs ("the rise from 96", "previous revision", "found this round", "buildability check") removed (map 7.4 L314, L338–L342); the writer paragraph kept and extended to `readiness.md`, `exclusions.md`, `local/settings.json`; the claims-store writers paragraph replaced by "no claims store in v1" (D13).
- Counts recomputed: seven scripts, 33 templates, eight skills with 28 references, three agents, two hook files, six shared files (must-do 11). For the checker: A§2 and A§5.4 should carry 90 installed files and these kind counts (map 8.3).

### Section 4.1 to 4.3
- 4.1: a tier column; layer 6 is the Code-side install smoke test (D6 check 12); layer 7 is the agnostic sweep (D6); Python wording (D25); the sandbox layer runs in the workspace the user names (A11-1); the nudge rule rephrased for sessions (D20) (must-do 6).
- 4.2: the absolute path to the fixtures workspace removed (map 7.5 L364); "calibration" and the earlier calibration file gone; the fixtures table rebuilt with a v1-proof column and a v2-kept-unread column per fixture (must-do 6); s1's named accounting product generalised (map 7.6 L370); s21 rewritten as the central existing-account case under A21 with A11-2 scoped (D17); the s12, s15, s16, s18, s21, s22, s23 and s24 rows carry the fixture review's agreed changes as v1 proof (FEEDBACK entries); "our side" is "the user's side" throughout (map 7.6); the Lessons-row column dropped; the grading totals removed from the counts sentence; seed records r2, r7, r8 reworded for readiness and the `shown` and `signed-off` events (D2, D21), r14 added, the `client/1` broken record replaced by two new broken records (D8); "demoed" no longer appears.
- 4.3: nine constructed inputs: the bleed case (v2) and the sign-off export refusal (v2-or-v3) dropped; items 6 and 7 are the two readiness cases H30 and H31 (D18); item 8 non-English moved to H64; item 9 the email-only generic case under H09 (Q7; spec section 1); the readiness cases that need no constructed input named; the proper name of the three-call chain and "three real calls" removed (map 7.6 L421, 7.4 L421).

### Section 4.4
- Tier column on every row (must-do 6); 64 ids, H38 retired (D8, D18); 56 v1-core, 6 v2 (H16, H18, H33, H51, H52, H55), 1 v2-or-v3 (H17); 168 runs recomputed over v1 ids.
- H09 replaced by the readiness run on s1, s2, s5 and the email-only input (D1, D2, D17); H30 and H31 are the two readiness constructed cases (D18); H08, H34 and H56 reworded for readiness (map 3.3); the non-English case moved to H64.
- New rows: H57 walkthrough (D12), H58 write refused outside the client's workspaces (A21), H59 docs as an element kind (D16), H60 to H63 the AI kinds (A17, A18) (must-do 6; PLAN D18).
- v2 clauses removed from H07, H28, H29, H40, H43, H45, H46, H49, H50 and H54 (map 3.3, 3.4); H47 rewritten as the A21 existing-account case with the FEEDBACK s21 corrections, and its "H03's s2 grade" slip gone (map 8.2); H41, H42, H44, H48 carry the fixture review's agreed changes; "chat" is "session" (A20); "our" is "the user's" (map 7.6); H19's "three real calls" gone (map 7.4); H50 spells tokens hyphenated and `they-show-current` (D3, map 6.2); H37 names `build-readiness` instead of `demo-script` among the refusals.

### Section 4.5
- Tier line; the discovery-check prompts replaced by readiness prompts (two should-start prompts, two should-not "grade" prompts, and the four-calls prompt chaining readiness once) (D1; map 3.5, 5.1); the "old plugin's territory" set and the placeholder firm name gone, with monday's official plugin the only plugin named in the should-not set (map 7.3 L484, 7.6 L484; must-do 6); the demo-script and client-sop prompts gone; "publish the app" joins the user-only set (A17); "with the old plugin disabled" is "no other monday-building plugin enabled".
### Section 4.6
- Tier column; the workspace the user names and `local/sandbox-accounts.txt` in the rules (A11-1, D11); T1 builds two new client workspaces with the AI subsection present and nothing built in round one (A21, Q5); T2 ends with the audit's closing line (D2); T7 marked v2-or-v3; T8 adds the exclusions term and reads the firm renderings from settings; T9's cross-client case is the one question (D10; map 6.5 L500); T13 creates the client's product workspaces and raises the UI install step (D26, P-22); T18 kept v1 (D16); T22 says unmet needs; T24 to T31 added per D18 (a write refused outside the client's workspaces; one per AI kind, T25 to T30, each citing its probe; the cross-product automation T31, P-23); "verdict" in T23 is "result".
### Section 5
- Per D6: check 1 reads "no other monday-building plugin is enabled (S0-11)" with the archive account from settings; check 2 the Mac's 3.9 and the newest installed Python 3; check 8 the agnostic sweep; check 12 the Code-side install smoke test; check 6's ranges recomputed over the v1 rows with the v2 rows named as not run; check 7's minor-release subset gains T24 and T25 and excludes T7; check 10's tags recomputed to [L14] [L15] with [L17] [L18] travelling with the sales layer and only intake rules checked (must-do 7).
### Section 6
- Replaced whole by the four new conflicts of D23: readiness against the discovery check, the AI kinds against the exclusion list, one surface against two, the workspace rule against "prefer an existing workspace" (must-do 8). The seventeen history rows are gone (map 8.4, 7.4 L537–L557).

### Citation pass after the sections
- A§ citations aligned with the architecture's re-cut subsection headings as they stood when checked: A§3.3 is now `build-readiness`, so Decision 16 cites A§12.3 alone; A§9.12 (claims discipline, v2) dropped from WP1 and WP12 inputs; A§8.4 (the readiness check), A§7.4 (version states and events), A§5.3 (the home and local settings), A§8.8 (shown, release and round two), A§9.5 (list approvals), A§9.11 (confidentiality on a shared screen) and A§11.5 (D26) cited where the plan builds to them.
- "verdict" and "gate" words in v1 prose replaced by "clearance", "check", "signal", "result", "conditioned" and "decides which doors may open"; `verdict` remains only as the name of readiness part 8 and the `readiness/1` field, which `build-readiness-spec.md` sections 2 and 7 fix, and in v2 columns and the deferred lists. For the checker: PLAN section 6's "no verdict word in v1 text" meets the spec's own field name here; the plan follows the spec.

## Map section 9: who answered each question

| Q | Answered by |
|---|---|
| 1 AI offerings shape | D4: additions across WP1, WP3, WP4, WP7, WP9, WP10, WP13, WP15 in stage 4b, after stage 4 |
| 2 Stage placement | D4: stage 4b, a stage of its own after stage 4 |
| 3 What "show" means | D2 and D21: `shown` is an event the user records; the audit says `cleared to show`; the run-sheet flags are gone from `version.md` |
| 4 Where v2 files live | D5: `deferred/` at the repo root |
| 5 Readiness home | D1: WP19, its own skill with one reference and `readiness.md` |
| 6 Verdict words | D2: three clearance strings in the check, the two closing strings in the audit |
| 7 Evidence law | Editor: pinned in `transcripts.md` (WP8) and `record-map.md` (WP1); WP19 links and never restates |
| 8 The consumer | D1: `solution-blueprint` reads the clearance and logs the override; `account-build` checks nothing new |
| 9 `gaps.md` | Editor: v2 with the demo layer; readiness questions live in `readiness.md` and `open-questions.md` |
| 10 Call-type header | D3: all six proposed, three drive v1, three marked v2; hyphenated tokens; `small-group` widened; `direction` in the fix pass |
| 11 `delivery` and the voice bank | D3's v2 marking applied by the editor: the subcommand, the report's delivery block and the voice-bank eligibility field leave; the MAINTAINING step leaves (WP13) |
| 12 Briefing a client-folder session | D12 and A22: the walkthrough, the generic home outside any development folder, the `CLAUDE.md` warning |
| 13 Default home | D11: `~/monday-builder/` with the user's value in the environment |
| 14 The wall between clients | Editor, within A20: `leak_lint.py --payload` reads hashed digests from `clients-index.json` (WP4) |
| 15 Never-demo | D22: `local/settings.json`, the briefing at `audited`, the audit's closing line |
| 16 Lease scope | D10: within-record lease plus the one question; `leases.json` gone |
| 17 Claims store | D13: v2; the never-say block and the irreversible table keep what A19 keeps |
| 18 Docs as an element kind | D16: v1, chunk rule in `build-loop.md`, T18 stays, WP6 whole deferred |
| 19 `research-scout` | D14: v1, two modes |
| 20 Check 8 | D6: the agnostic sweep |
| 21 `sync_shared.py` | D9: gone, with its lint clause |
| 22 `migrate`, `client/1`, H38 | D8: gone; H38 retired |
| 23 Fixtures | D17: all 25 stay; the fix pass adds `readiness`; s21 is the A21 case |
| 24 Test ids | D18: numbering kept, H30 and H31 reassigned, new H and T rows; check 6 recomputed |
| 25 Python 3.11 | D25: 3.9 and newer, tested on what the Mac has |
| 26 PDF text | D25: the session reads the pages when no text tool exists and the report says so |

Map section 6 carried items: 6.1 the advisory overclaim is gone with the status values (D3 marks them v2; nothing in v1 text pins `advisory`); 6.2 hyphenated tokens everywhere (D3); 6.3 `direction` renamed in the fix pass (D3); 6.4 `small-group` widened to two or more client attendees (D3); 6.5 every stage-0 reference handled as the table says; 6.6 Python (D25), the name index under `local/` (D11), the scans before WP5 (WP18), records and settings under the home (D11, A22).

Map section 7 hits: 7.1 no handle anywhere in the document; 7.2 the workspace name, its id, the account references, the account-derived counts and the renamed-board detail are gone; 7.3 no earlier plugin named, "no other monday-building plugin" everywhere, monday's official plugin the only one named (in the should-not set); 7.4 the calibration file, the revision notes, "real call", the three-call chain's name, the revision history and section 6 are gone, "calibration" survives nowhere; 7.5 the earlier setup's json inputs, `live-tests/`, `fixtures-work/`, `cowork-capabilities.md`, `client/1`, the passed date and the absolute path are gone; 7.6 the named accounting product, the placeholder firm, the proper name of the chain are gone and "our" survives only inside quoted prompts and a client quote; 7.7 `MMB_HOME` default is generic (D11).

## Left for the checker

Compared against map section 9 and PLAN section 1, these are the points where the architecture must say the same thing (map 8.3) or where the editor chose and the checker should confirm:

1. **Counts** (PLAN acceptance 8): 90 installed files, 94 ownership rows, 27 deferred files, seven scripts, 33 templates (46 with the deferred ones), eight skills, 28 references, three agents; `monday-gotchas.md` at 520 lines after stage 4b; the budgets `record.py` 560, `ledger.py` 680, `leak_lint.py` 540, `transcript_prep.py` 300, `guard.py` 200. A§2, A§5.4 and A§10.2 should carry the same numbers.
2. **New reference files** the plan names and A§2 should list: `engagement/references/first-run.md`, `build-readiness/references/readiness-guide.md`, `solution-blueprint/references/ai-elements.md`, `solution-audit/references/ai-checks.md`; the three new templates `readiness.md`, `exclusions.md`, `agent-prompt.md`; three research files under the record; `summary-and-recap.md` keeps its name with the summary half only.
3. **Probe ids** P-26 (AI column), P-27 (sequence), P-28 (webhook) are new here, after PLAN section 7's P-22 to P-25; the architecture's probe list should carry them or the plan renumbers.
4. **The `verdict` field name** inside the readiness block against PLAN section 6's vocabulary rule (see the citation pass above).
5. **H38 retired, not renumbered**, so the headless table runs H01 to H64 with one retired row; 56 v1 ids, 168 runs.
6. **The `delivery` fields** of `intake-report/1` (voice-bank eligibility) are dropped from the report in the plan; A§5.4's report row should agree.
7. **The never-demo mechanism in v1** is a briefing line and the audit's closing line (D22); if the architecture keeps a stop in `account-build`, the plan's WP9 should gain it.
8. **A§3.3 renumbering**: the plan cites A§3.3 as `build-readiness` and A§12.3 for Decision 16; if the architecture moved the fallback decision elsewhere, section 0's last paragraph needs the new number.
9. **Email as an input class** (interview Q7) is written as "documents" under A16 in WP2, WP5 and WP8; no amendment names it, so the user may want a line in AMENDMENTS or the architecture's 8.3, which already titles itself "calls, documents and emails".
10. **Section 3's `client-closeout` references** are assumed to be two and `demo-script`'s and `client-sop`'s two each; A§2 decides the real split, and the 94 count moves by the difference.
