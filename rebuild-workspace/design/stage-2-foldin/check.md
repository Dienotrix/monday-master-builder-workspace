# Stage 2 fold-in of A24 to A28: consistency check

Checked 2026-10-14 against `AMENDMENTS.md` (A24 to A28 with every "Answered 2026-10-14" line, plus A1, A11, A17 to A23). Documents read in full: `ARCHITECTURE.md`, `BUILD-PLAN.md`, `ROADMAP.md`, `stage-1b/build-readiness-spec.md`, with `SPEC.md` as the product reference. No design document was edited.

**Editor changelogs present:** all three: `arch-changelog.md`, `plan-changelog.md`, `roadmap-readiness-changelog.md`. They were read, but every finding below comes from the documents themselves.

**Clean on these sweeps:**
- No personal, firm, account or workspace name, and no GitHub handle.
- Every long numeric id in ARCHITECTURE is either an obvious placeholder or a monday template id already in `native-objects.md`'s catalogue.
- No AI credit pricing, no all-caps emphasis, and no A11 decision defaulted.
- None of these remain: a shell-only step, a fixed path or separator, a Trash or Recycle Bin step, GitHub as required, GitHub removed outright, a blocking sign-off, a fork-open element left unbuilt, assumptions written into the workspace, or the old full term read-back.
- These counts add up: installed files (89 and 94), templates (35), deferred files (29), headless ids (58, 174 runs), references (26), and the listing-cost character counts.

Types: contradiction (against an amendment as answered), inconsistency (between documents, or within one), count, stale, rule.

---

1. **ARCHITECTURE.md:32**, contradiction. "Automations, workflows, agents, sequences and irreversible steps are confirmed again at execution and never carry across sessions." Design principle 3 still states the pre-A28 rule without qualification, and the A1 row of 12.4 (L1116, "one grouped re-confirmation at execution") does the same. **Fix:** in both places, add that this holds in a client's account and for lists that notify real people. On an own-account proof of concept the card's one yes covers them (A28).

2. **ARCHITECTURE.md:320**, contradiction. "a **deep dive** after round one that reads the record's pains, the built version and the client's public sources". The `research-scout` row in section 4 still places the deep dive after round one. A27, 3.1 and 8.8 step 30 run it before the first build when the usual one to three days exist. **Fix:** say the deep dive runs before the first build when time allows and after round one only when it does not, as BUILD-PLAN WP11 already says.

3. **ARCHITECTURE.md:357**, contradiction. "the internal-evidence adjustments to that order are a reading, so `call-intake` proposes them with their quotes and the user confirms the order (8.3)". The `set` row of 5.4 still makes the package order a confirmation stop. A27, 8.3 (L763) and BUILD-PLAN H34 ("no confirmation asked") make it assumed and shown. **Fix:** replace "the user confirms the order" with "the order is recorded as assumed and shown, and a correction by the user re-runs what depended on it".

4. **ARCHITECTURE.md:356**, contradiction. "a per-file alias table proposed once for the user's confirmation". The `identity` description in 5.4 still asks for confirmation. 3.2 (L201) and 8.3 step 5 (L759) now record the alias table as assumed and stop only for an identity the evidence cannot settle (A27). **Fix:** align 5.4 with 3.2: proposed once, shown, recorded as assumed until the user corrects it.

5. **BUILD-PLAN.md:172**, contradiction. "a per-file alias table proposed once for confirmation with one canonical entry per person, place or organisation". WP5's `identity` acceptance and H44 (L509, "the alias table proposed once, confirmed") still expect a confirmation step. The architecture now makes it assume-and-show under A27, and the architecture editor flagged this for the plan. **Fix:** in WP5 and H44, change the alias table to "proposed once, shown and recorded as assumed, corrected by the user where needed", and grade the correction path rather than a confirmation.

6. **ARCHITECTURE.md:368**, inconsistency. "the six tokens, each `detected`, `proposed` or `confirmed`, where `proposed` is the best guess intake carries on with". The architecture keeps `proposed` as the best-guess state (also at L357, L625 and L759). BUILD-PLAN pins `detected`, `assumed` or `confirmed` (WP1 L105, WP5 L175, WP7 L196), and `record-map.md` is supposed to spell every such string once. **Fix:** pick one spelling and use it in both documents. `assumed` matches A27's wording and the readiness spec's `assumptions[].kind: call type`.

7. **ARCHITECTURE.md:580**, inconsistency. "`sample_data: true` marks every sample row, which is never cited as a fact (A28)." The architecture names the ledger fields `sample_data` (also at L268 and L795) and `assumption_refs`. BUILD-PLAN calls them "the `sample` mark" and "the `assumed` mark" (WP1 L105, WP3 L135, WP3 L146, T1 L543). **Fix:** settle one field name for each and use it in both documents and in `record-map.md`'s pin. Either `sample_data` and `assumption_refs`, or `sample` and `assumed`.

8. **BUILD-PLAN.md:105**, inconsistency. "the approval modes a ledger row's `approval_ref` can carry, the card's one yes on a proof of concept in the user's own account, a list's own yes and an item's own yes (A28)". BUILD-PLAN lists three approval modes. ARCHITECTURE 7.3 (L580) defines two values of `approval_mode`, `own-account-poc` and `per-list`, plus `mode: card` or `at-execution` on `irreversible_yes` rows. **Fix:** state the same set in both. For example, the two `approval_mode` values plus the two `irreversible_yes` modes, with the strings pinned once in `record-map.md`.

9. **ARCHITECTURE.md:551**, contradiction. `"approval_mode": "per-list"`. The 7.3 example ledger uses `per-list` and an `at-execution` irreversible yes (L573), but the example record is an own-account build (`"kind": "own"`, `"build_target": "own-account"`, L492) whose only listed agent notifies nobody. Under A28 that revision is `own-account-poc`. **Fix:** change the example to `own-account-poc` with `"mode": "card"` on the `irreversible_yes` row. Or switch the example account to `client-account` so `per-list` is the correct mode.

10. **BUILD-PLAN.md:179**, inconsistency. "takes an email export as a document whose author, date and status are the sender's role, the send date and `email` (Q7)". BUILD-PLAN WP5 and WP2 (L122) treat an email as documents with `input_kind: document`. ARCHITECTURE gives `transcript_measure.py` its own `email` subcommand writing `input_kind: email` (5.4 L356, 8.3 L755 and L767). Its `document-summary.md` also carries `input_kind: "document" | "email"` (section 6). **Fix:** choose one model. Either add the `email` subcommand and `input_kind: email` to WP5's files and acceptance, or reduce the architecture to the email-as-documents form.

11. **ARCHITECTURE.md:894**, contradiction. "never in a client account; in the user's own account only as the cleanup of a superseded proof of concept, listed and confirmed like an archive". The last row of the 9.4 table allows delete calls in the user's own account. This contradicts SPEC L64 ("Any `delete_*` call in any account, the user's own included") and SPEC L137 ("v1 sends no delete call in any account"). It also contradicts the architecture's own L898 and 3.7 ("v1 sends no `delete_*`"). **Fix:** change the row's handling to "never sent by v1 in any account; removal is a by-hand step named in the close-out", matching SPEC.

12. **BUILD-PLAN.md:569**, inconsistency. "`vibe_delete` is the sandbox cleanup and is recorded as never allowed in a client account". T27, T30 (L572, "deletion is the sandbox cleanup") and WP15 (L327, "a Vibe app is deleted only in the sandbox") send delete calls in the sandbox account. SPEC L64 excludes any `delete_*` call in any account. **Fix:** either add a sandbox-cleanup carve-out to SPEC's out-of-scope line, saying who sends it and under which record kind, or make these cleanups archive plus a by-hand removal step.

13. **BUILD-PLAN.md:545**, contradiction. "the automation re-confirmed after the list is shown where the record's approval mode requires an execution-time confirmation, and resumed under the card's yes where it does not (A28)". T3 lets an interrupted automation create resume under the card's yes on an own-account proof of concept. ARCHITECTURE 8.11 (L833) says a lost `create_automation` reply always needs the user to re-confirm, own-account proof of concept included, "since the card's yes approved one creation and not a second". SPEC's Recovery criterion (L101) agrees. **Fix:** make T3 require the re-confirmation after the board's automation list is shown on both approval modes.

14. **BUILD-PLAN.md:294**, inconsistency. "only after a clean compare and the user's confirmation is the record folder moved out of `clients/` into `archive/`". The local archive first copies the record into `archive/<slug>/` (ARCHITECTURE 8.10 L829), and then the original folder is also moved into `archive/`. No document says where the original lands, beside or over the verified copy. SPEC L31 also says a GitHub-archive user gets the repository "instead", while ARCHITECTURE and BUILD-PLAN move the folder into `archive/` on that path too. **Fix:** state one mechanism in all four documents and SPEC, for example "the verified copy in `archive/<slug>/` is the archive, and the original moves to a named holding path such as `archive/<slug>.original/`". Also change SPEC's "instead" to "as well".

15. **SPEC.md:99**, count. "all 4 tester writes during an audit detected". SPEC and T10 (BUILD-PLAN L552) count four tester writes. ARCHITECTURE 9.7 (L926) lists five: a description edit, an archive, a column settings change, an item value change, and an agent plan edit. **Fix:** either add the agent plan edit to T10 and make SPEC's figure 5, or drop it from 9.7's sealed test.

16. **SPEC.md:99**, inconsistency. "At least 9 of 10 sealed defects found, including one per AI kind". SPEC's Audit criterion requires one sealed defect per AI kind, but T2 (BUILD-PLAN L544) only says "ten defects sealed by a separate session". SPEC L103 names seven kinds: workflow, agent, AI column, Vibe app, sequence, webhook and doc. At least seven of the ten sealed defects would therefore be AI-kind defects, and nothing in the plan says so. **Fix:** either specify in T2, or in the sealed-defect file's acceptance, which defects cover which AI kinds, with any count change, or narrow SPEC to the AI kinds the round-two sandbox build carries.

17. **SPEC.md:94**, stale. "On the 25 fixtures, once their keys carry the `readiness` block". All 25 keys have carried the `readiness` block since the fix pass of 2026-10-13. What is still pending is the `goals` list of A27. **Fix:** change the condition to "once their keys carry the `goals` list in the `readiness` block (the stage-2 follow-up pass)", and add that every goal sits verbatim at its location.

18. **SPEC.md:73**, inconsistency. "**v2 or v3:** the client SOP skill and its tools, the diagrams and exports, the doc copy, and the handoff package." SPEC does not name the master document the user asked for later (A25, answered 2026-10-14): the solution and why, with diagrams, how to use it and the SOPs, seeded by the build notes. ROADMAP L61, BUILD-PLAN L197 and L607, and ARCHITECTURE L280 and L1214 all name it. **Fix:** add to SPEC's v2-or-v3 bullet "the master document the plugin generates for the client (the solution and why, with diagrams, how to use it, and the SOPs), seeded by the build notes (A23, A25); nothing of it is v1".

19. **ARCHITECTURE.md:747**, inconsistency. "Ask the setup questions in **one message**, and only those the record cannot answer (A27): the **build target** ...". The 8.2 step 2 list adds website and links, the AI notice and the first exclusion terms, but omits the time available before the first demo. BUILD-PLAN `new-client.md` (L205) and H01 (L470) ask the time available, from which the cadence is proposed (A27, as 3.1 says). They do not list the other three. **Fix:** give both documents the same list. Add the time available to 8.2 step 2, and add website, the AI notice and the exclusions seed to WP8 and H01, or drop them from 8.2.

20. **ARCHITECTURE.md:222**, inconsistency. "Every gap the first build fills by assumption, each labelled `[A]` in the record (7.5) with the question that would replace it." Part 5 in 3.3 still covers only gaps. The readiness spec (L19), which the folded text is meant to follow, also covers several other items:
    - the assumed call type
    - the automation conditions and the board-architecture overview when the client cannot be reached
    - the forks on their leaning
    - the rule that column names and status labels are not confirmed one by one
    - the build-notes paragraph per open item

    **Fix:** fold the readiness spec's part 5 text into 3.3 part 5. Say whether an assumed call type also appears in the assumptions list, as `readiness/1`'s `kind: call type` implies, while keeping its `proposed`/`assumed` header state.

21. **BUILD-PLAN.md:110**, inconsistency. "irreversibles with their own yes (a new workspace or folder, Vibe publication, a workflow published, `connect_project_to_portfolio`, the first subitem, the multi-level template board)". The irreversible classes in `safety.md` (WP1) and the irreversible list in WP9 (L254) omit agent activation, sequence activation and webhook creation. SPEC L82 lists activating an agent, and ARCHITECTURE 9.4 (L890 to L893) and 7.3 (`AG1.ACT`, `SQ1.ACT`) list all three. **Fix:** add agent activation, sequence activation and webhook creation to both lists in BUILD-PLAN.

22. **BUILD-PLAN.md:603**, stale. "a Vibe publication and a workflow publication are irreversibles with their own yes". Row 2 of section 6 states the resolution without A28's qualifier, though row 9 later changes it. **Fix:** append "in a client's account; on an own-account proof of concept the card's one yes covers them (A28)".

23. **BUILD-PLAN.md:526**, stale. "a Vibe publication taking its own yes (on r14)". H61's scenario title still says publication takes its own yes. Its pass condition on r14, an own-account proof of concept, is that the card's one yes covers publication. **Fix:** retitle it, for example "a Vibe publication under each approval mode (on r14, and with `--target client-account`)".

24. **BUILD-PLAN.md:17**, count. "Before the first write probe (P-22 to P-25 wait on it)". The [A11-1] row still names four waiting probes. ARCHITECTURE section 13 (L1206), WP10, WP13 and WP15 name P-22 to P-28, adding the AI-column, sequence and webhook probes. SPEC L144 also lists only the four P-22 to P-25 subjects. **Fix:** change the row to "P-22 to P-28 wait on it", and extend SPEC's list with the AI column, the sequence and the webhook.

25. **BUILD-PLAN.md:380**, count. "H66 belongs to WP9 with WP2 proving the sign-off half and WP10 the build-notes half." The owners of record disagree with the acceptance lists in four places:
    - WP9 (L257) claims "the card and build-notes half of H66".
    - H57 is in both WP2's (L122) and WP8's (L205) acceptance, with no split stated.
    - WP2 lists H36 whole, though H36 belongs to WP12.
    - WP10's row in the section 3 table (L371) omits H65, which WP10's acceptance (L277) claims.

    **Fix:** make WP9 claim "the card half" only. Name one owner for H57 with the other half cited, or add H57 to the split list. Make WP2 cite "the `version release` half of H36", and add H65 to WP10's table row.

26. **ARCHITECTURE.md:360**, count. "About 3,110 lines in all, the same figures the packages in BUILD-PLAN hold a builder to." The script sizes in 5.4 differ from the BUILD-PLAN packages:

    | Script | 5.4 | BUILD-PLAN |
    |---|---|---|
    | `mmb_common.py` | 240 | 250 (WP2) |
    | `record.py` | 560 | 580 (WP2) |
    | `ledger.py` | 680 | 700 (WP3) |
    | `archive_check.py` | 190 | 230 (WP12) |

    That is about 3,200 lines against 3,110. The `solution-audit` SKILL.md is also 185 in 3.8 against 190 in WP10. **Fix:** bring 5.4 and 3.8 to BUILD-PLAN's figures, or the reverse. Then restate the total.

27. **ROADMAP.md:74**, inconsistency. "then WP2, the scripts: record, ledger, leak lint, intake, agnostic sweep, in Python 3.9 or later and system-neutral". ROADMAP puts all of stage 2's scripts under WP2. BUILD-PLAN (L45 to L46) splits them across WP2 (record), WP3 (ledger), WP4 (leak lint), WP5 (intake) and WP16 (agnostic sweep). **Fix:** write "then WP2 to WP5 and the agnostic sweep (WP16): record, ledger, leak lint, intake and sweep scripts, ...".

28. **ARCHITECTURE.md:353**, inconsistency. "that `readiness.md` carries one of the three clearance strings or `none`". `record.py check` in 5.4 accepts `none`, which a fresh `readiness.md` from the template carries before the first run. WP2's acceptance (BUILD-PLAN L122) blocks "a `readiness.md` whose clearance is not one of the three pinned strings", which would block every new strand. `readiness/1` (readiness spec L52) also uses `none` in `cleared_for` to mean `not yet`. **Fix:** allow `none` in WP2's check, as "not yet run". Give `cleared_for` a value distinct from that `none`, such as `not-yet`, so the two meanings cannot be confused.
