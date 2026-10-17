# What the user owns — review, run, decide, clean up

Everything in this folder is yours to look at. The documents here are copies (refreshed 2026-10-13; fixtures added 2026-09-20); give feedback in chat and the assistant applies it to the originals (paths below). `stage0/` is a link into the repo, so what you type into its `results.md` lands in the right place. Priority 1 items decide direction and should happen before stage 2 goes far.

## 1. Review and sign off (direction)

| # | Item | File in this folder | Original | What to do | Why it matters | Priority | Status |
|---|---|---|---|---|---|---|---|
| R1 | **The product spec** | `01-SPEC.md` (148 lines) | `~/DelOps/monday-master-builder-dev/rebuild-workspace/design/SPEC.md` | Read end to end. Mark anything that is not what you want built, and anything missing. Reply with line numbers or quotes. | The only document that defines the product. | **1** | re-cut 2026-10-13, reviewed by interview the same day; aligned 2026-10-14 with your answers on A25 and A26 (GitHub optional, sign-off warns, narrower read-back), please read once |
| R2 | **Your decisions as recorded** | `02-AMENDMENTS.md` (A1–A29) | `…/design/AMENDMENTS.md` | Check each amendment says what you decided, at the strength you meant. | These override every other document. | **1** | **updated 2026-10-16**: A29 added (WP3's recorded reads are synthetic first; its consequences, the assistant's reading, nodded by you on 2026-10-16 at WP3's go); earlier, A24 to A28 added from the SPEC interview, and your answers of 2026-10-14 added under A25 and A26; please read A29 to A24 once |
| R3 | **Scope split** | `03-ROADMAP.md` | `…/design/ROADMAP.md` | Confirm the v1 / v2 / v2-or-v3 split; move items if not. | Decides what "complete" means and what is built first. | 2 | re-cut 2026-10-14 under A24 to A28 (Windows and Mac, local archive with GitHub optional, goals first, one yes on own-account proofs of concept), please read once |
| R4 | **The sales method as rewritten** | `04-METHOD.md` — read §4 (demo, incl. 4.11 group calls, 4.12 voice), §6 (recap, 6.6 handover), §7.1 (claims in live speech), §11 (open questions for you) | `~/DelOps/monday-master-builder-dev/rebuild-workspace/dossier/research-delops-method.md` | Say where the written method should not have changed to match observed practice. | Now a v2 document (A19). | 3 | reviewed 2026-09-19; deferred to v2 |
| R5 | **Your voice specification** | `05-HOUSE-STYLE.md` | `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/house-style.md` | Strike anything that does not sound like you; add shapes you actually use. | Now a v2 document (A19). | 3 | reviewed 2026-09-19; deferred to v2 |
| R6 | **Intake fixtures s11–s25** | `fixtures/` — start with `fixtures/00-HOW-TO-REVIEW.md` | `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s11-…` to `s25-…` and the new rows in `COVERAGE.md` | Per fixture: read the README; skim the transcript for realism; spot-check that the answer key concludes what you would want. | The keys are the specification the intake code is graded against; once signed, the code must match you. | 2 | **reviewed 2026-10-13; fix pass applied 2026-10-13** — each folder under `fixtures/` carries `CHANGES.md` with what changed and why, every key now has a `readiness` block, and `COVERAGE.md` is recomputed |
| R7 | What the real calls changed (optional) | `06-REAL-CALL-LESSONS.md` — top section and §9 | `…/design/REAL-CALL-LESSONS.md` | Skim; object where a rule is wrong. | Background to R4 and R5; the intake lessons still apply to v1. | 3 | optional |
| R8 | **Stage 1b run plan and the build-readiness check** | not copied here; read `~/DelOps/monday-master-builder-dev/rebuild-workspace/design/stage-1b/PLAN.md` (section 2 is the decisions list) and `build-readiness-spec.md` | same files | Nod or object to the decisions in chat; the run starts on your go with multi-agent mode on for that run | They shape every v1 document the run rewrites | **1** | **complete 2026-10-13**: run done, 36 findings fixed; acceptance and seven open points in `stage-1b/acceptance.md`; the re-cut documents are rows R1 to R3 |
| R9 | **What WP3 leaves for your word** | not copied here; read `~/DelOps/monday-master-builder-dev/rebuild-workspace/build/wp3/DECISIONS.md` section 3 ("Shared edits for the user's word", "Design touch-ups for the user's word") and the follow-ups of its later sections, and the choices worth your nod in `wp3/API-ledger.md` and `wp3/fixture-notes.md` | same files | Say which edits and touch-ups to apply (A29's three first), and nod or object to the builders' choices | They bring the design documents and the other shared files in line with what WP3 built; none blocks stage 2's acceptance | 2 | **open since 2026-10-17** |

## 2. Run

| # | Item | Where | What to do | Status |
|---|---|---|---|---|
| P1 | **Stage-0 probe pack** | `stage0/README.md` (what to run), `stage0/results.md` (where answers go) — linked into the repo | Run with the assistant as guided steps on 2026-10-12. | **done for v1** (A20: v1 runs in Claude Code on the Mac; every plugin-behaviour probe passed) |
| P2 | **WP2 Windows checks** | `windows-run/wp2-windows-bundle.zip` (copy-only route), or `monday-master-builder/tests/windows/` in a clone | Run under Python 3.9 and the newest Python 3; the results go to `rebuild-workspace/build/wp2/windows-results/`. | **done 2026-10-16** with the assistant, from a clone on Windows 11 under Python 3.9.13 and 3.14.5: every automated check passed; the four optional manual checks (OneDrive, Ctrl+C, WSL, network share) were not run |
| P3 | **WP3 macOS run** | on the Mac, in `~/DelOps/monday-master-builder-dev/` | Open a new Claude Code session there and send: "First run `git pull` in this folder and in `monday-master-builder/`. Then read HANDOFF.md in full and follow its section 8: the next run is the WP3 macOS run its State section describes. Run it inline, keep the results in `rebuild-workspace/build/wp3/macos-results/`, tick K17, K81 and K436 in `CHECKLIST.md`, and report to me plainly; commit and push only at my word. Then propose the plan for WP4 (`leak_lint.py`) and start nothing without my go." | **open**; the Windows half is done (2026-10-17: 330 tests OK under Python 3.9.13 and 3.14.5, lint 0 errors, `wp3/windows-results/`) |

## 3. Decide (asked at the moment each first matters — nothing to do now)

| # | Decision | When it is asked |
|---|---|---|
| D1 | Which account carries write probes and sandbox scenarios [A11-1] | before the next live monday test, and before 1.0.0 |
| D2 | Whether sample data may live in a live client account [A11-2] | before the first client build that plans sample rows |
| D3 | Transcript and document redaction and retention [A11-3] | before the first real client transcript or document is saved |
| D4 | Policy for a chain-broken native descendant (P-16) | ships as "protect it as native and ask"; change if you disagree |
| D5 | Four fixture-review questions [L14 fork refusal, L15 consumption placement, L17 demo environment as an asset, L18 credential substitute] | each ships with a stated default; change any when you like |
| D6 | Your GitHub handle in design and repository files | **closed 2026-10-13**: the handle is each user's own configuration, so it was removed from every file (the design documents, amendment A8, the stage-0 results, the shipped leak list and record map); the one exception is the plugin's own `repository` address in `plugin.json`, which names the publisher rather than the user, and changes only if the plugin is published under an organisation |
| D7 | The people on your account who may be used for testing (assignments, notifications, automations) | yours to send when real proof-of-concept builds start (your word, 2026-10-17); it becomes an amendment, and the names live only in your `local/settings.json` |

## 4. monday UI steps (no API path)

| # | Step | Where in monday | Status |
|---|---|---|---|
| — | None at present. | — | — |

## 5. Housekeeping

| # | Item | Status |
|---|---|---|
| H1 | Empty the Trash: `~/.Trash/real-calls-calibration-20260912-203915` holds the four real client calls and every analysis of them | open |
| H2 | The original VTT you downloaded is still in `~/Downloads` (your file; not touched) | yours |
| H3 | After stage 0: remove the `stage0-probe` plugin in Customize → Plugins, and delete the chat-side "stage-0 test" Project and the test chats (the zip and the test folder are already in the Trash) | open |
