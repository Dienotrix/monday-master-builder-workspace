# Stage 2 fold-in of A24 to A28: fixes for the consistency check

Applied 2026-10-14 against `check.md` (28 findings), with `AMENDMENTS.md` A24 to A28 and every "Answered 2026-10-14" line as the authority. Each entry gives the finding, fixed or not fixed, the document and the line range after editing, and one sentence on what changed. Line ranges are as they stood when the entry was written; a later edit higher in the same file may shift them by a few lines.

## Findings

1. **Fixed.** ARCHITECTURE.md L32 (principle 3) and L1116 (12.4, A1 row), A28. The execution-time confirmation is now stated for a client's account and for lists that notify real people; on an own-account proof of concept the card's one yes covers the lists and irreversible steps.

2. **Fixed.** ARCHITECTURE.md L320 (`research-scout` row), A27. The deep dive now runs before the first build when the usual one to three days exist, and after round one only when they do not, matching 3.1, 8.8 step 30 and BUILD-PLAN WP11.

3. **Fixed.** ARCHITECTURE.md L357 (`transcript_prep.py set`), A27. The package order is recorded as assumed and shown with its quotes; a correction by the user re-runs what depended on it. No confirmation stop.

4. **Fixed.** ARCHITECTURE.md L356 (`transcript_measure.py identity`), A27. The alias table is proposed once, shown and recorded as assumed until the user corrects it, with a stop only for an identity the evidence cannot settle, as in 3.2 and 8.3 step 5.

5. **Fixed.** BUILD-PLAN.md L172 (WP5 `identity`), L510 (H44) and L287 (WP11 `transcript-summarizer` input), with ARCHITECTURE.md L318 (section 4 summarizer row) for the same wording, A27. The alias table is proposed once, shown and recorded as assumed, corrected by the user where needed, with a stop only for an identity the evidence cannot settle; H44 now grades the correction path (a planted correction replaces the entry it names and re-runs what depended on it) instead of a confirmation, and the summarizer receives the table with its state rather than a "confirmed" table.

6. **Fixed.** ARCHITECTURE.md L357, L368, L625, L759, A27. The best-guess header state is spelled `assumed` throughout (`detected`, `assumed` or `confirmed`), matching BUILD-PLAN WP1, WP5 and WP7 and the readiness spec's `kind: call type`. Worth the user's nod: the choice of `assumed` over `proposed` as the pinned string.

7. **Fixed.** BUILD-PLAN.md L105 (WP1 `record-map.md`), L127 (WP3 tier), L135, L146, L257 (WP9), L328 (WP15), L364 (section 3 table), L544 (T1), A25 and A28. The plan now uses the architecture's ledger field names, `sample_data: true` on every sample row and `assumption_refs` on an element built on an assumption, and WP1 pins both; the `assumed` status stays on the leaning or assumed term itself, which the element cites. Worth the user's nod: the choice of the architecture's names over the plan's `sample` and `assumed` marks.

8. **Fixed.** BUILD-PLAN.md L105 (WP1), A28. The approval modes now match A§7.3: `approval_mode` is `own-account-poc` or `per-list`, and an `irreversible_yes` row's `mode` is `card` or `at-execution`, all pinned once in `record-map.md`. The third "item's own yes" mode is gone; an item's yes at execution is the `at-execution` mode.

9. **Fixed.** ARCHITECTURE.md L551 and L573 (7.3 example ledger), A28. The example is an own-account build whose agent notifies nobody, so its approval entry now reads `"approval_mode": "own-account-poc"` and its `irreversible_yes` row `"mode": "card"`.

10. **Fixed.** BUILD-PLAN.md L122 (WP2 acceptance), L164 (WP5 why two scripts), L179 to L180 (WP5 `document` and a new `email` bullet), L461 (4.3 constructed input 9), A16 as extended 2026-10-13. The plan now takes the architecture's model: `transcript_measure.py email` writes `input_kind: email` with sender, recipients, date, thread order and attributed forwards, and each attachment gets its own `document` pass linked to the message. No file, fixture or size count changes: the subcommand was already inside the architecture's 600-line figure, which WP5 already holds. Worth the user's nod: email as its own input kind rather than as documents.

11. **Fixed.** ARCHITECTURE.md L894 (9.4, last row), SPEC L64 and L137. Deleting an agent, a Vibe app or any object is now never sent by v1 in any account, the user's own included; removal is a by-hand step named in the close-out, and a superseded proof of concept is archived where the roster allows.

12. **Fixed.** BUILD-PLAN.md L328 (WP15 acceptance), L570 (T27), L573 (T30), SPEC L64. The sandbox cleanups no longer send `vibe_delete` or `delete_webhook`: the run lists a by-hand removal step for the user, and `delete_webhook` stays only as the client's named switch-off step in the handoff. SPEC is unchanged. Worth the user's nod: the alternative was a sandbox carve-out in SPEC's out-of-scope line; this run took the smaller change that keeps SPEC as written.

13. **Fixed.** BUILD-PLAN.md L546 (T3), A28 with A§8.11 and SPEC's Recovery criterion. An interrupted automation create is now re-confirmed by the user after the board's automation list is shown on both approval modes, since the card's yes approved one creation and not a second.

14. **Fixed.** One mechanism, stated in all four documents and SPEC, A24 and A26 as answered 2026-10-14: the record is copied into `archive/<slug>/` and verified file by file, that copy is the archive, and on the user's yes the original folder moves to `archive/<slug>.original/` beside it; the user empties `archive/` by hand. On the GitHub path the repository and its verified clone are made as well, and the local archive still runs. ARCHITECTURE.md L340, L344, L377, L438, L644, L829, L861, L862; BUILD-PLAN.md L105, L295 (WP12), L367, L502 (H36); SPEC.md L12, L31, L46, L86 ("instead" now "as well" in L31 and L46); ROADMAP.md L45. Worth the user's nod: the holding name `archive/<slug>.original/`, and the GitHub path running the local archive as well rather than moving the folder only.

15. **Fixed.** SPEC.md L99 (Audit criterion) and BUILD-PLAN.md L553 (T10). The agent plan edit of A§9.7 is kept, since agents are v1 and the before-and-after snapshot already digests an agent's plan; T10 now lists five tester writes and SPEC's figure is 5, with the five named. ARCHITECTURE 9.7 is unchanged. Worth the user's nod: a success-criterion figure in SPEC moved from 4 to 5.

16. **Fixed.** BUILD-PLAN.md L545 (T2) and L328 (WP15 acceptance), SPEC L99 and L103. T2 now places one sealed defect on each AI kind SPEC names (workflow, agent, AI column, Vibe app, sequence, webhook, doc) and three on round-one structure, requires the defect on every AI kind built among the nine found, and moves a kind's defect to round-one structure, named as not yet covered, when that kind's probe has not passed; the sealed-file acceptance cites that spread. SPEC is unchanged. Worth the user's nod: the substitution rule for an unprobed kind (P-26 to P-28 still wait on the test workspace).

17. **Fixed.** SPEC.md L94 (Readiness criterion), A27. The condition now reads "once their keys carry the `goals` list in the `readiness` block (the stage-2 follow-up pass)", and adds that every goal sits verbatim at its location; the `readiness` block itself has been in all 25 keys since the 2026-10-13 fix pass.

18. **Fixed.** SPEC.md L73 (deferred, v2 or v3), A25 as answered 2026-10-14 and the user's request relayed with this run. The bullet now names the master document the plugin generates for the client: the solution and why, with diagrams, how to use it and the SOPs, seeded by the build notes (A23, A25), with nothing of it in v1. This matches ROADMAP, BUILD-PLAN and ARCHITECTURE, which already named it.

19. **Fixed.** ARCHITECTURE.md L747 (8.2 step 2), BUILD-PLAN.md L206 (WP8 `new-client.md`) and L471 (H01), A27. Both documents now carry the same setup list: build target, anything already live, the first strand's topic and kind, website and links, the AI notice, the exclusions seed, and the time available before the first showing, from which the plugin proposes the cadence and the user sets it. Still asked in one message, and only where the inputs and settings do not answer.

20. **Fixed.** ARCHITECTURE.md L222 (3.3 part 5), A25 and A27 as answered 2026-10-14. Part 5 now follows the readiness spec: besides the gaps it lists the assumed call type, the automation conditions and the board-architecture overview when the client cannot be reached, and each fork or open structural question built on its leaning; column names and status labels are not confirmed one by one; each open item gets a short build-notes paragraph; the user is the one who confirms. It says that an assumed call type appears in the assumptions list as `kind: call type` while the call summary's header keeps its own `assumed` state.

21. **Fixed.** BUILD-PLAN.md L110 (WP1 `safety.md` approval classes) and L255 (WP9 irreversible list), A17, A18 and A§9.4. Agent activation, sequence activation and webhook creation are added to both lists, matching SPEC L82 and ARCHITECTURE 9.4 and 7.3 (`AG1.ACT`, `SQ1.ACT`).

22. **Fixed.** BUILD-PLAN.md L604 (section 6, row 2), A28. The resolution now says a Vibe publication and a workflow publication take their own yes in a client's account, and that on an own-account proof of concept the card's one yes covers them.

23. **Fixed.** BUILD-PLAN.md L527 (H61), A28. The scenario is retitled "a Vibe publication under each approval mode (on r14, and with `--target client-account`)", which is what its pass condition already tests.

24. **Fixed.** BUILD-PLAN.md L17 ([A11-1] row) and SPEC.md L144 (open decisions), A11-1 left open. The row now says P-22 to P-28 wait on the test workspace, and SPEC's list adds the AI column write, the sequence and the webhook, matching ARCHITECTURE section 13 and WP10, WP13 and WP15. No A11 decision is defaulted.

25. **Fixed.** BUILD-PLAN.md L122 (WP2), L258 (WP9), L372 (section 3, WP10 row), L381 (owners of record). WP9 now claims the card half of H66 only; WP2 cites the `strand close` half of H36 and the `home init` half of H57 instead of claiming both whole; H57 joins the split list as WP8's, with WP2 proving the `home init` half; WP10's table row adds H65 and the build-notes half of H66, which its acceptance already claimed. No test count changes. Worth the user's nod: WP2's half of H36 is named `strand close`, what H36 exercises in `record.py`, rather than the check's suggested `version release`, which H36 does not run.

26. **Fixed.** ARCHITECTURE.md L352 to L360 (5.4) and L278 (3.8). The architecture now carries BUILD-PLAN's figures: `mmb_common.py` 250, `record.py` 580, `ledger.py` 700, `archive_check.py` 230, and the `solution-audit` SKILL.md 190. Re-totalled: 250 + 580 + 700 + 540 + 600 + 300 + 230 = about 3,200 lines, up from 3,110, and the line now lists the seven figures it sums. BUILD-PLAN is unchanged.

27. **Fixed.** ROADMAP.md L74 (stage 2 row). The row now reads "then WP2 to WP5 and the agnostic sweep (WP16): record, ledger, leak lint, intake and sweep scripts", matching BUILD-PLAN's split across WP2, WP3, WP4, WP5 and WP16.

28. **Fixed.** BUILD-PLAN.md L122 (WP2 `check`), ARCHITECTURE.md L353 (`record.py check`), stage-1b/build-readiness-spec.md L52 (section 7), A27. WP2's check now accepts `none` as "the check has not run yet", so a fresh strand is not blocked, and `cleared_for` takes `not-yet` for the check's own result so the two meanings cannot be confused. The readiness spec says the follow-up keys pass moves the pinned `none` to `not-yet` in `shared/record-map.md` (L208) and in the one answer key that carries it (s10); this run edits neither, since both are outside the documents it was given. Worth the user's nod: the `not-yet` spelling, and carrying the pin and key change in the follow-up pass.

**Revision notes.** Each of the five documents already said it was re-cut 2026-10-14 under A24 to A28; each now adds that the stage-2 consistency check of that day is applied (ARCHITECTURE.md L3, BUILD-PLAN.md L3, ROADMAP.md L3, SPEC.md L3, stage-1b/build-readiness-spec.md L3). No stale state line needed changing beyond finding 17: ROADMAP already shows stage 1b and the fixture fix pass complete on 2026-10-13 and stage 2 current, with this fold-in as its first task.

## Worth the user's nod

Decisions the amendments did not settle, each taken as the smallest reasonable one and kept out of `AMENDMENTS.md`:
- Finding 6: the best-guess header state is spelled `assumed`, not `proposed`.
- Finding 7: the ledger fields are `sample_data` and `assumption_refs`, the architecture's names.
- Finding 10: an email is an input of its own kind (`input_kind: email`) with its own subcommand, not a set of documents.
- Finding 12: sandbox cleanups of a Vibe app or a webhook are by-hand steps, so SPEC's "no `delete_*` in any account" stands with no carve-out.
- Finding 14: the original record folder moves to `archive/<slug>.original/` beside the verified copy, and the GitHub path runs the local archive as well.
- Finding 15: SPEC's tester-write figure moves from 4 to 5, keeping the agent plan edit.
- Finding 16: in T2, a kind whose probe has not passed has its sealed defect moved to round-one structure and is named as not yet covered.
- Finding 25: WP2's half of H36 is `strand close`, not the check's suggested `version release`.
- Finding 28: `cleared_for` takes `not-yet`; the pinned `none` in `shared/record-map.md` and in the s10 answer key move in the follow-up keys pass, not in this run.

## Totals

28 findings: 28 fixed, 0 not fixed. Counts changed and re-totalled: the 5.4 script total (3,110 to about 3,200 lines) and the `solution-audit` SKILL.md (185 to 190) in ARCHITECTURE; SPEC's tester writes (4 to 5). No file, template, fixture or headless-test count changed. The three A11 decisions stay open, and nothing measures or prices AI credits.
