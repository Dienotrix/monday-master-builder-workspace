# Stage 1b consistency check

Written 2026-10-13 by the checker (V1) after reading SPEC.md, ARCHITECTURE.md, BUILD-PLAN.md, ROADMAP.md, the three changelogs, the refresh notes, the plan, the readiness spec and A17 to A22, and after running the sweeps the plan names. Line numbers are those of the files as they stood at the time of the check. Each finding names the file, the line, a short quote, a type (wrong, missing, unclear, inconsistent), a severity (blocking, should-fix, minor) and the fix. Findings are ordered most severe first. The last section lists what was checked and found clean, so the fix pass does not re-check it.

## Findings

### Blocking

**1. ARCHITECTURE still cites the earlier setup's result files and carries counts read from a real account.**
- File and lines: `ARCHITECTURE.md` L23 ("Gotcha ids `G-01` to `G-90` refer to `live-tests/gotchas-draft.md`", "they live in `live-tests/results/native-board-rules.json` and `native-boards-report.md` (67 boards, 19 workspaces, 0 misclassified)"); L979 ("Entries are grouped by area following `live-tests/gotchas-draft.md`", "written at WP1 from `native-board-rules.json` and `native-boards-report.md`"); L1017 ("Sources: `live-tests/results/native-board-rules.json` and `native-boards-report.md` (67 boards across 19 workspaces, 0 misclassified, plus ten adversarial cases); `results/identification-rules.json` (33 boards, 0 misclassified"); L929 ("a single page of 33 boards"); L939 ("[live native-boards-report §5, §7]"); L1021 and L1128 ("all 43 natives read"); L1141 ("misread 7 of 33 boards").
- Type: wrong (no `live-tests/` folder exists anywhere under the workspace; `find` returns nothing) and inconsistent (the plan's acceptance item 7 and the build-plan editor removed the same references and counts from BUILD-PLAN as agnostic hits, plan-changelog WP3 and map 7.2, 7.5).
- Severity: blocking. The plan's acceptance item 7 says no earlier setup is named, and the planner's retired-file sweep must find nothing.
- Fix: cite the homes that exist: `shared/monday-gotchas.md` for G-01 onward, `shared/native-objects.md` for the native rules and template ids, `tests/fixtures/snapshots/` for the recorded reads. Drop the board and workspace counts ("67 boards", "19 workspaces", "43 natives", "33 boards", "7 of 33") or restate them as "the recorded reads" without figures; keep the `[live]` tags with a dated probe reference only. The evidence tag at L939 becomes "[live, native-objects.md]".

**2. The four model-invocable skill descriptions exceed the 800-character limit the same document sets.**
- File and lines: `ARCHITECTURE.md` L165 ("`description` at most **800 characters**"), L293 ("Four model-invocable descriptions at or under 800 characters each is at most 3,200 characters"); the descriptions at L178 (`engagement`, 929 characters), L189 (`call-intake`, 811), L202 (`build-readiness`, 867), L230 (`solution-blueprint`, 923). The four doors are inside the limit (745, 756, 782, 701).
- Type: inconsistent; the document's own examples break its rule, and `lint_plugin.py` (BUILD-PLAN L325) fails on a description over 800 characters.
- Severity: blocking. A builder copying these descriptions into stage 4 fails the lint, and 3.11's "at most 3,200" is false of the text (the four sum to 3,530).
- Fix: trim each of the four to 800 characters or fewer, keeping the "Use when" and "Not for" clauses, then recount 3.11. The `build-readiness` description can lose the nine-part list, which `readiness-guide.md` owns.

**3. The round-two build order contradicts A17's "agents are built last".**
- File and lines: `AMENDMENTS.md` A17, Safety bullet (L56: "agents are built last, after automations"); `BUILD-PLAN.md` L238 ("then automations, then workflows, then agents last, with a Vibe app after the boards it binds"); `SPEC.md` L42 ("Agents are built last."); against `ARCHITECTURE.md` L259 ("adds the AI kinds **after the automations**: workflows, agents, AI columns, Vibe apps, sequences and webhooks") and L779 (8.6 step 16, the same order with agents second of six).
- Type: inconsistent, with the amendment on one side.
- Severity: blocking. AMENDMENTS override the architecture, and the three documents disagree on the order a builder follows.
- Fix: reorder 3.7 and 8.6 step 16 so agents close round two (workflows, AI columns, Vibe apps, sequences, webhooks, then agents), and say why in one clause: an agent's grants and triggers name boards and apps that must exist first. Check 9.5 L885 and 12.4's A17 row still read true afterwards.

### Should-fix

**4. The planned gotcha ids for the AI areas collide with ids already in use.**
- File and lines: `ARCHITECTURE.md` L979 ("**G-10x agents** ... **G-11x Vibe apps** ... **G-12x workflows** ... **G-13x AI columns, sequences and webhooks**"), L23 ("enter the gotcha list as `G-91` onward at WP1", stated as future), L1009 (the watch list "every G-10x to G-12x entry").
- Type: wrong. `shared/monday-gotchas.md` already holds G-01 to G-108 (108 entries; the native-identity entries run from G-91), so G-100 to G-108 are taken, and WP1's stage-1 work is done, not pending.
- Severity: should-fix.
- Fix: start the AI areas after the last id in the shipped file (for example G-110 agents, G-120 Vibe apps, G-130 workflows, G-140 unprobed kinds), say at L23 that the native entries are in the file, and update the 10.5 watch list and BUILD-PLAN L99 ("continuing at G-91" is right; add where the AI areas start) to the same numbers.

**5. The file, reference and deferred counts disagree between the two documents and with their own lists.**
- File and lines: `ARCHITECTURE.md` L158 ("8 SKILL.md, 24 references, 3 agents, 6 shared files, 7 scripts, 33 templates ... **85 files**"); `BUILD-PLAN.md` L346 ("A§2's **90 installed** files", "eight skills with 28 references", "The rows below come to **94 files**"), L194 (WP8: "2 SKILL.md and 9 references", while its own list names four engagement references and three intake references and ARCHITECTURE's tree has eight, `research.md` included), L228 (WP9: "2 SKILL.md and 11 references", while the tree has nine plus the new `ai-elements.md`, ten), L255 (WP10: five, which agrees once `ai-checks.md` is added), L366 ("Twenty-seven files in all" deferred) against ARCHITECTURE L54 to L60 and L1187, whose deferred tree also holds `doc-copy.md` (L57) and `numbers.md` (L1187), twenty-nine.
- Type: inconsistent. Two files BUILD-PLAN names as stage-4b references, `solution-blueprint/references/ai-elements.md` and `solution-audit/references/ai-checks.md`, are absent from ARCHITECTURE's tree and its 24; BUILD-PLAN's "90 installed" also counts `CHANGELOG.md`, which the tree places at the repo root (L50), as installed, since 94 less the four repo-root files named at L346 leaves it inside.
- Severity: should-fix (plan acceptance item 8: counts recomputed and true).
- Fix: add `ai-elements.md` and `ai-checks.md` to ARCHITECTURE's tree with a "(stage 4b)" note, making 26 references and 87 installed files (8 + 26 + 3 + 6 + 7 + 33 + 4); correct BUILD-PLAN WP8 to eight references and WP9 to ten; make section 3 read 87 installed plus five repo-root files (`marketplace.json`, `.gitignore`, `MAINTAINING.md`, the repo `README.md`, `CHANGELOG.md`), 92 rows, 26 references; settle the deferred list at one number by adding `doc-copy.md` and `numbers.md` to BUILD-PLAN L366 or dropping them from ARCHITECTURE. Delete "to be mirrored in A§10.2" at BUILD-PLAN L108, since 10.2 already says 520.

**6. WP7's template list has 32 names, places `readiness.md` at record level and omits `client-gitignore.txt`.**
- File and lines: `BUILD-PLAN.md` L184 ("Thirty-three v1-core templates"), L185 (record level ends "`document-summary.md`, `readiness.md`"; per strand lists fourteen; `client-gitignore.txt` appears nowhere), L189 ("33 files"); `ARCHITECTURE.md` L141 to L148 (the tree: twelve record-level files including `client-gitignore.txt`, fifteen per strand including `readiness.md`, six other), L366 ("`readiness.md` is strand level on purpose"), and BUILD-PLAN's own WP19 L202 ("the strand file `readiness.md`").
- Type: wrong (the count) and inconsistent (the level).
- Severity: should-fix.
- Fix: move `readiness.md` into the per-strand list, add `client-gitignore.txt` to the record-level list, and recount to 33.

**7. Script line budgets differ between the catalogue and the packages.**
- File and lines: `ARCHITECTURE.md` L339 to L345 (`mmb_common.py` 250, `record.py` 500, `ledger.py` 660, `leak_lint.py` 420, `transcript_measure.py` 620, `transcript_prep.py` 250, `archive_check.py` 190; L347 "About 2,890 lines in all") against `BUILD-PLAN.md` L116 ("240 and 560"), L141 ("680"), L149 ("540"), L174 ("600 and 300"), L285 ("190"), which sum to 3,110.
- Type: inconsistent (the plan-changelog's "left for the checker" item 1 asked for this to be settled).
- Severity: should-fix.
- Fix: pick one set. The package figures are the acceptance limits a builder is held to, so ARCHITECTURE 5.4 should carry 240, 560, 680, 540, 600, 300, 190 and "about 3,110 lines", or the packages should be lowered to the catalogue's; either way the two must match.

**8. `record.py` subcommands named in BUILD-PLAN no longer exist in ARCHITECTURE, and one event command has two names.**
- File and lines: `BUILD-PLAN.md` L115 ("`tools-check` refuses a version or sha mismatch"; "`version event --strand shown|signed-off` records the event"), L188 ("`record.py client-view` cuts exactly sections 1 to 15"); `ARCHITECTURE.md` L324 ("the copy ladder is gone with `sync_shared.py` and `record.py tools-check` (D9)"), L340 (the subcommand list, which has `version mark` and neither `tools-check` nor `client-view`), L593 and L798 ("`record.py version mark`"), L1187 (`record.py client-view` and `manifest` listed as v2-or-v3).
- Type: inconsistent.
- Severity: should-fix (a builder of WP2 would build a dropped command, and the WP7 acceptance depends on a tool that is deferred).
- Fix: in BUILD-PLAN L115 drop the `tools-check` clause and rename `version event` to `version mark`; in L188 replace "`record.py client-view` cuts exactly sections 1 to 15" with "the lint's section range stops before section 16" (ARCHITECTURE L235) and move the cut to the deferred note.

**9. ROADMAP uses a clearance string that does not exist and says never-demo applies to accounts.**
- File and lines: `ROADMAP.md` L17 ("one of three clearances (cleared to build, cleared with assumptions, not yet)"); L36 ("native-board guard; never-demo accounts").
- Type: wrong. The pinned strings are `cleared to build`, `cleared to build, generic` and `not yet` (plan D2, ARCHITECTURE L216, BUILD-PLAN L57); never-demo applies by workspace (A21, ARCHITECTURE L949).
- Severity: should-fix (plan acceptance item 1 says ROADMAP says the same as the other documents; the vocabulary check of plan section 6).
- Fix: write "cleared to build, generic" at L17 and "never-demo workspaces" at L36.

**10. Decision numbers are cited across two numbering systems and one citation is wrong.**
- File and lines: `BUILD-PLAN.md` L35 ("Decision 16 (which conservative fallback wins) is settled in A§12.3", "Decision 19 is a caveat rather than a decision: a number of intake rules rest on one observation"); `ARCHITECTURE.md` L1087, where 12.3's D16 is "the CLI upgraded before release tooling" and D19 is "connector: the claude.ai connector", while the fallback is D25 and the provisional rules sit in section 13; `ARCHITECTURE.md` L223 and L755 ("The override (D1, D7)"), where D1 is the plan's decision (the readiness home) but D7 is 12.3's own item (the readiness override), since the plan's D7 drops `gql_guard.py`; 12.3 L1083 to L1087 number the user's decisions D1 to D27, overlapping the plan's D1 to D26, and disambiguate only twice ("D14 of the plan", "D21 of the plan").
- Type: wrong (L35) and unclear (the double numbering).
- Severity: should-fix.
- Fix: in BUILD-PLAN L35 cite "A§12.3, D25" and "A§13's provisional rules"; in ARCHITECTURE give 12.3's items a prefix that cannot be read as the plan's (for example "decision 7 of 12.3", or renumber them R-free as "12.3-7"), and write "(D1 of the plan; 12.3's readiness-override rule)" at L223 and L755. Also check L158, L907 and L1096, where "D7" is the plan's and reads correctly, stay unambiguous after the change.

**11. The hook's behaviour on an account-level write differs: ARCHITECTURE refuses, BUILD-PLAN asks.**
- File and lines: `ARCHITECTURE.md` L935 ("and, for an agent or Vibe write, that every board or workspace id in the payload is one of the client's. It refuses otherwise."); `BUILD-PLAN.md` L295 ("because an account-level object carries no workspace a hook can read, the matcher **asks** on an agent, Vibe or sequence write and shows the target ids it found in `tool_input`, and the ledger's scope check is what refuses"), L513 (H58: "asks on an agent knowledge grant outside the client's workspaces, which the ledger then refuses"), L554 (T24, the same).
- Type: inconsistent.
- Severity: should-fix (WP13's tests assert one behaviour and the architecture specifies the other).
- Fix: choose one. BUILD-PLAN's reading rests on the probe fact that agents have no workspace field (WP1 L99), so ARCHITECTURE L935 should read "asks, showing the ids it found, and `ledger.py intent` refuses" and 9.1's account-level row (L834) and 14's agent-scope risk row (L1194) should name the ledger as the refusing check.

**12. The record-root discovery order differs, and A20's file-based rule is the one that should lead.**
- File and lines: `BUILD-PLAN.md` L295 ("It finds the record root from `CLAUDE_PROJECT_DIR` when set, otherwise by walking up from the working directory"); `ARCHITECTURE.md` L935 ("by walking up from the working directory to the first folder holding `CLIENT.md` (the file-based rule of A20; an app-specific project variable is used only when it agrees)"), L320 (the same rule stated for the surface).
- Type: inconsistent.
- Severity: should-fix.
- Fix: BUILD-PLAN L295 reads "by walking up from the working directory to the first folder holding `CLIENT.md`; an app-specific project variable is consulted only when it agrees, and the hook asks when neither resolves".

**13. `exclusions.md` has two writers.**
- File and lines: `ARCHITECTURE.md` L401 ("engagement seeds it at new client; the user and solution-blueprint add rows"), L731 (setup asks for "the first names and terms for `solution/exclusions.md`"); `BUILD-PLAN.md` L372 ("`exclusions.md` is written by `call-intake` and read by the lint and the build"), L115 (`strand open` "places `readiness.md` and `exclusions.md` from the templates").
- Type: inconsistent (the one-writer rule of section 3).
- Severity: should-fix.
- Fix: BUILD-PLAN L372 reads "seeded by `engagement` at new client, grown by the user and by `call-intake` when a client says something must not appear, read by `solution-blueprint`, the sample-data step and the lint"; ARCHITECTURE L401 adds `call-intake` to the writers if that is wanted, so both say the same.

**14. The evidence marker count is eight in BUILD-PLAN and nine in ARCHITECTURE.**
- File and lines: `BUILD-PLAN.md` L98 ("the eight evidence markers including `[Q/doc]`"), L148 ("all eight markers including `[Q/doc]`"); `ARCHITECTURE.md` L601 to L609 (nine rows, `[A]` added), L611 ("`leak_lint.py` blocks all nine"), L1089 ("one convention of nine markers").
- Type: inconsistent.
- Severity: should-fix (the lint's acceptance names the count it must block).
- Fix: "nine evidence markers including `[Q/doc]` and `[A]`" at L98 and "all nine markers" at L148.

**15. The `sample_data_in_account` field has different values in the two documents.**
- File and lines: `ARCHITECTURE.md` L458 ("`sample_data_in_account: "not-needed"` # open (A11-2) only when build_target is client-account: allowed | not-allowed, asked before the first such build; "not-needed" in the user's own account"); `BUILD-PLAN.md` L23 ("`record.py check` treats an A11 field left at `unanswered` as a blocking finding"), L188 ("`sample_data_in_account: "unanswered"` [A11-2]"), L460 (H01: "each shipped `unanswered` in `CLIENT.md`").
- Type: inconsistent. `unanswered` is not in the architecture's value list for this field, yet `record.py check` keys on it.
- Severity: should-fix.
- Fix: ARCHITECTURE L458 lists `unanswered | allowed | not-allowed | not-needed`, ships `unanswered`, and says `record.py strand open` or the bind step sets `not-needed` when the build target is the user's own account; BUILD-PLAN L188 says the same.

**16. Probe ids P-26 to P-28 exist only in BUILD-PLAN.**
- File and lines: `BUILD-PLAN.md` L235 ("unprobed until P-26 runs", P-27, P-28), L265, L299, L317, L556, L559, L560; `ARCHITECTURE.md` L1179 (the probe list ends at P-25 and names "the unprobed kinds of that family, AI columns, sequences and webhooks" without ids), L999 (flags for P-22 and P-24 only).
- Type: missing (the plan-changelog's "left for the checker" item 3).
- Severity: should-fix.
- Fix: add P-26 (an AI column configured and read back), P-27 (a sequence created, activated and read back) and P-28 (a webhook created and read back) to ARCHITECTURE section 13 with their defaults, and extend "P-22 to P-25 wait for A11-1" to P-28; add their flags to 10.3 if the overlay is to carry them.

**17. Part 8 of the readiness block is called "clearance" in one document and "verdict" in the other, and the verdict word survives in two v1 places.**
- File and lines: `ARCHITECTURE.md` L216 ("**Clearance: what the user is cleared to do.**"), L651 (`clearance:` on `STRAND.md`); `BUILD-PLAN.md` L207 ("The verdict is a statement about this record today"), L209 ("the verdict as what the user is cleared to do"), L215 ("**The verdict** is one of three pinned strings"), L188 ("the verdict as one of the three pinned strings"); and `ARCHITECTURE.md` L269 ("The report separates verdict from currency"), L486 (`"verdict": "no change affecting this build"` in `change_check`).
- Type: inconsistent (plan section 6: no verdict word in v1 text; the plan-changelog argued that the spec's own field name, `verdict` in `readiness/1`, is the exception).
- Severity: should-fix.
- Fix: BUILD-PLAN uses "clearance" for part 8 at L188, L207, L209 and L215, matching ARCHITECTURE and the `STRAND.md` field; ARCHITECTURE L269 reads "separates the result from currency" (the plan-changelog removed the word from BUILD-PLAN's audit text) and L486 renames the JSON key to `result`. The one remaining `verdict`, the `readiness/1` field name from the readiness spec section 7, is pinned in the fix pass; the fix pass should pin it as `clearance` so the rule holds without an exception, and the spec's section 7 note already allows that.

**18. Header field names are hyphenated in 8.3 and snake_case everywhere else.**
- File and lines: `ARCHITECTURE.md` L743 ("`output-class`", "`room-shape`", "`money-live`" as field names, "in v1 only `output-class`, `direction` and `room-shape` drive behaviour"), L1187 ("`money-live` header tokens"), L1214 ("A `direction` or `output-class` token"); against L665 and L1087 (`output_class`), and `BUILD-PLAN.md` L57, L98, L167 (`output_class`, `room_shape`, `money_live`, with hyphens on the token values only).
- Type: inconsistent. D3 hyphenates the token values; the keys and the record map use snake_case field names (`direction_of_show` becomes `direction`).
- Severity: should-fix (WP1 pins the vocabulary; the two documents must spell the fields alike).
- Fix: at L743, L1187 and L1214 write the field names `output_class`, `room_shape`, `money_live` and keep the values hyphenated.

**19. Two jobs ARCHITECTURE assigns to scripts are missing from the packages that own them.**
- File and lines: `ARCHITECTURE.md` L907 ("a scan of the appendix that refuses any document containing a mutation or subscription operation or more than one operation (the small tokenizer lives inside `ledger.py compare`"), L1096 (A2 row, the same); `BUILD-PLAN.md` L131 (WP3's `compare` acceptance names digests and states only) and L260 (WP10 relies on it). `ARCHITECTURE.md` L935 ("At every release `tools/lint_plugin.py` diffs the live roster against the pattern and lists any write-shaped tool the families miss"); `BUILD-PLAN.md` L325 (WP16's lint list has no roster diff) and L295 (WP13 does not ask for it).
- Type: missing.
- Severity: should-fix.
- Fix: add to WP3 L131 "and scans the audit appendix, refusing any document that carries a mutation or subscription or more than one operation, with a unit test on planted documents"; add to WP16 L325 "diffs the live roster, or the recorded baseline, against the hook's pattern families and lists any write-shaped tool they miss", and name that check in release check 3 or 9.

**20. The word "calibration" and "stage 6" survive in the refreshed files.**
- File and lines: `ROADMAP.md` L47 ("the delivery lessons from the real-call calibration"), L62 ("calibration fixtures s11-s25"); `for-review/00-READ-ME-FIRST.md` L11 ("Confirm the v1 / stage 6 / v2 split"), L14 ("**Calibration fixtures s11–s25**"), L32 ("Four calibration questions").
- Type: inconsistent (BUILD-PLAN renamed them "intake fixtures" and dropped "calibration" everywhere, plan-changelog map 7.4; the stage order has no stage 6) and, at ROADMAP L47, a reference to the real-call work the plan bars.
- Severity: should-fix for ROADMAP L47 and L62; minor for the three lines of `00-READ-ME-FIRST.md`.
- Fix: ROADMAP L47 "the delivery lessons" and L62 "intake fixtures s11-s25"; `00-READ-ME-FIRST.md` L11 "the v1 / v2 / v2-or-v3 split", L14 "Intake fixtures s11–s25", L32 "Four fixture-review questions".

### Minor

**21. "Nine columns" for a ten-field live map.**
- `BUILD-PLAN.md` L188 ("`live-map.md` (`live-map/1`) has the nine columns of A§7.8"); `ARCHITECTURE.md` L675 to L686 list ten (key, monday id, kind, workspace, built by, state, constraint, source, dependants, last verified; `workspace` was added under A21).
- Type: wrong. Fix: "the ten columns".

**22. `shown` and `signed-off` are stages on the strand ladder and "not states" in 7.4.**
- `ARCHITECTURE.md` L647 (stage ladder "... audited | shown | signed-off | closing | closed") against L593 ("`shown` and `signed-off` are not states") and L578.
- Type: unclear. The two ladders are different axes, but a reader meets the contradiction first. Fix: one sentence at L647 or L665: "the strand stage advances on the event; the version state does not change".

**23. Skill and reference size budgets differ by a few lines between the documents.**
- `ARCHITECTURE.md` L225 (`build-readiness` 180, reference 190) against `BUILD-PLAN.md` L223 (190 and 170); L196 (`transcripts.md` 170) against L197 (180); L259 (`build-loop.md` 170) against L250 ("the rest at or under 150"); L269 (`audit-checks.md` 180) against L269 ("none over 160").
- Type: inconsistent. Fix: copy the package figures into the architecture or the reverse; the package is the acceptance.

**24. The design voice says "our side", "ours" and "we" in ARCHITECTURE and SPEC where BUILD-PLAN says "the user's side".**
- `ARCHITECTURE.md` L192, L209, L212, L219, L235, L355 ("a named seat at our own domain"), L416, L743, L745, L951 ("What our own environment must not expose"), L953, L957, L961, L995, L1087; `SPEC.md` L20 ("telling our side's framing"), L21 ("do we know enough"), L110 ("Nothing of ours is live"). BUILD-PLAN has none outside quoted prompts (plan-changelog, map 7.6).
- Type: inconsistent. Not a name, so not a rule breach, but the plan asks for "the user" throughout. Fix: "the user's side", "the user's own domain", "the user's own environment"; the readiness question can read "does the record hold enough".

**25. "spec part 8" should be "spec section 8".**
- `ARCHITECTURE.md` L217, L223, L766 ("spec part 8"). The spec's "parts" are the nine parts of the block; the two user decisions sit in its section 8. L609's "part 5" is correct. Fix: write "readiness spec section 8".

**26. SPEC puts the one question before the lock; ARCHITECTURE takes the lock first.**
- `SPEC.md` L40 ("asks whether another build is running anywhere and logs the answer, then holds the record's own lock"), L114 (the same order); `ARCHITECTURE.md` L774 (step 11: `lease take`, then the one question) and L917 ("after the lease is taken, the build asks").
- Type: inconsistent. Fix: SPEC L40 and L114 "takes the record's own lock, asks whether another build is running anywhere and logs the answer".

**27. The home tree is listed without `sandbox/` in two places.**
- `SPEC.md` L12 ("`clients/` ..., `cards/`, `monday-knowledge/` ..., and `local/`"; also no `clients-index.json`); `BUILD-PLAN.md` L98 and L115 (the same four); `ARCHITECTURE.md` L333, L424, L728 include `sandbox/` and `clients-index.json`.
- Type: inconsistent. Fix: add `sandbox/` (and, in SPEC, the hashed `clients-index.json`) or drop it from the architecture's `home init`.

**28. Two leftovers in WP2's acceptance.**
- `BUILD-PLAN.md` L115 ("mints and returns the session label (surface, timestamp, short random suffix"), where "surface" is the two-surface design's field that D10 and A20 removed (`ARCHITECTURE.md` L913: "from a timestamp and a short random suffix"); and L115 ("a record whose `schema_version` is newer than the plugin refuses writes") against the `schema` key the architecture uses (L330, L712, L1089).
- Type: inconsistent. Fix: drop "surface"; write "`schema`".

**29. WP3's bind rule mixes accounts and workspaces, and cites the wrong step.**
- `BUILD-PLAN.md` L126 ("refuses to bind an operational workspace listed in `local/settings.json` as a build target (A§5.4, A§8.2 step 5)"). Binding is to an account (`ARCHITECTURE.md` L341, L733: the bind rules are in 8.2 step 4; step 5 writes the ids), and the operational workspaces are a never-demo list, not bind targets; the workspace rule already keeps writes out of them.
- Type: unclear. Fix: "refuses a sandbox account on a client record and the reverse, and binds an own-account record only to the default build-target account (A§5.4, A§8.2 step 4)"; keep the operational-workspace refusal in `intent` and `workspaces`, where L127 already has it.

**30. The install path is described two ways.**
- `ARCHITECTURE.md` L42 ("installed in Claude Code on the Mac by adding the repo as a marketplace from the desktop app's Code side"); `BUILD-PLAN.md` L298, L387, L580 ("through Customize"). Type: unclear. Fix: one sentence in both: the repo is added as a marketplace and the plugin is enabled in Customize, or whichever the stage-0 results recorded.

**31. The word "gate" survives in three v1 passages outside the classification sense.**
- `ARCHITECTURE.md` L102 ("plan-tier gates" in the `product-fit.md` line), L828 (the authority table's column "Gate"), L1219 ("scenarios instead of document gates"). The classification uses at L1017, L1042 and L1099 ("key gates `R4`-`R7`", "soft gate") are a different sense and can stay.
- Type: inconsistent with plan section 6. Fix: "plan-tier limits", column "Condition", "document checks".

**32. HANDOFF section 7 carries a stale carry-over paragraph, and the sections around it are older than the run.**
- `HANDOFF.md` L57 ("Carried into stage 1b (small, recorded by the fix pass): BUILD-PLAN line ~107 narrows to 'advisory is pinned ...'; ARCHITECTURE A§8.3 step 5 and BUILD-PLAN H50 spell type-header values as prose ... the keys write `direction_of_show` ..."): the advisory line is gone from BUILD-PLAN, the tokens are hyphenated in both documents, and the rename is now plan section 7's fix-pass item. Outside section 7: L3 ("current as of 2026-09-20"), L10 ("1,300 lines"), L11 ("18 work packages"), L12 ("re-cut under A19"), L43 and L56 (`cleanroom_scan.py`, retired by D6).
- Type: inconsistent. Severity: minor, because the Design and Stage 1b lines of section 7 do match the files. Fix: replace L57's paragraph with "folded into stage 1b; the `direction` rename and the `small-group` widening are fix-pass items (PLAN section 7)". The lines outside section 7 are the planner's to refresh, since the run's scope stops at section 7.

**33. A22's two phases are not stated in words in BUILD-PLAN.**
- `BUILD-PLAN.md` L115 (WP2: the generic default and the environment variable), L196 (WP8: "where the clients folder lives and that it sits outside any development folder"), L75 (WP-S0: "which A22 answers"); `ARCHITECTURE.md` L366 states both phases.
- Type: missing (check item 4 asks for the two phases in both). Fix: one clause in WP2 or WP8: "during build and test the clients folder sits inside the development home; once the plugin ships, outside any development folder (A22)".

**34. ARCHITECTURE sections 4 and 5.4 carry no explicit tier word.**
- `ARCHITECTURE.md` L301 to L311 (agents) and L337 to L347 (scripts): the title block (L3) says every component carries a tier; these two tables imply v1-core by omission and say so only for `sop-drafter` and the three dropped scripts.
- Type: missing. Fix: one sentence at the top of each: "every row below is v1-core".

**35. `account_kind: sandbox` has no `build_target` value.**
- `ARCHITECTURE.md` L437 ("`account_kind: "own"` # own | client | sandbox: mirrors build_target") and L438 ("`build_target`: own-account | client-account"). Type: unclear. Fix: add `sandbox` to `build_target`'s values or say the sandbox record sets `build_target: "none"`.

**36. "Calibration" wording in the review checklist.**
- Covered under finding 20 for `for-review/00-READ-ME-FIRST.md` L11, L14 and L32; listed here so the minor count is complete.

## Checked and found clean

- `grep -rIl -i <the handle>` over the workspace: one hit, `monday-master-builder/plugins/monday-master-builder/.claude-plugin/plugin.json`, as the plan allows.
- The earlier-plugin, proposal, judge, critic, revision-notes grep over the four documents: no hit (the four matches at ARCHITECTURE L172, L235, L353, L1141 are the word "judgement").
- The three review copies are byte-identical to their originals (`cmp` on SPEC, AMENDMENTS, ROADMAP).
- No named test workspace, no account, workspace, board, user or automation id from a real account: every id of seven or more digits in the four documents is either a template or template-view id that `shared/native-objects.md` lists (5678953932, 7819831530, 5727048235, 5561655961, 6410079972, 8179060947, 176205535, 174990912, 174990913, 9449773054, 200776197, 7830923787, 2673708477, 1631647074) or an obviously invented example id (1000000x, 1100000000x, 1200000000x, 2000000x, 1234567).
- Cowork appears only as a later surface (SPEC L11, ARCHITECTURE L320, L1177, L1187, BUILD-PLAN L592); no file names it as current. The publisher's name appears once (SPEC L3, as author).
- No capitals used for emphasis in any of the four documents.
- `discovery.md`, `discovery_verdict` and `demoed` survive only inside deferred or v2 lists (ARCHITECTURE L58, BUILD-PLAN L188, L366); `discovery_verdict` and `demoed` appear nowhere.
- Every `A§` citation in BUILD-PLAN names a heading that exists (A§2, 3.1 to 3.4, 3.7 to 3.10, 4, 5.3, 5.4, 6, 7, 7.1 to 7.5, 7.7 to 7.9, 8.1 to 8.11, 9, 9.5 to 9.11, 10.2 to 10.5, 11, 11.3, 11.5, 12.3, 13), and the ones spot-checked say what they are cited for, except the two step numbers noted in findings 10 and 29. Every package ARCHITECTURE names (WP1 at L23 and L979) exists in BUILD-PLAN.
- A17 to A22 each have a home in ARCHITECTURE 12.4 (L1111 to L1116) and in BUILD-PLAN (A17 and A18 in WP1, WP3, WP4, WP7, WP9, WP10, WP13, WP15; A19 in the title block, WP1, WP8, WP12, WP19; A20 in WP-S0, WP2, WP11, WP12, WP13; A21 in WP1, WP3, WP7, WP9, WP10, WP13, WP15 and section 6 row 4; A22 in WP-S0, WP2, WP8, WP13). A21's workspace rule appears in the blueprint (ARCHITECTURE L233, L762; BUILD-PLAN L234), the build (L257, L777; L236), the ledger scope check (L341; L127), the hook (L935; L295) and the audit (L269, L793; L262). A22's generic default home, walkthrough and warning appear in both (ARCHITECTURE L333, L728; BUILD-PLAN L115, L196, L298).
- The readiness spec's nine parts, three clearance values, five-question ceiling, two standing questions, the card's first section and the override rule are in ARCHITECTURE 3.3 and 8.4 and in BUILD-PLAN WP19; the audit's `cleared to show` line is in ARCHITECTURE 3.8 and 8.7 and in BUILD-PLAN WP10 and T2.
- The AI kinds appear in every place the architecture map's part 7c listed (key list 7.3, live-map kinds 7.8, `STRAND.md` 7.7, approval card 8.5, build order and list confirmation 8.6, audit 8.7, recovery 8.11, irreversible table and exclusion paragraph 9.4, list approvals 9.5, hook 9.10, read-back 10.4, gotcha areas 10.2, 12.3 and 12.4, probes 13, deferred list and risks 14); the four contradicting rows are gone.
- Headless arithmetic holds: 64 ids less H38 retired, six v2 rows and one v2-or-v3 row leave 56 v1-core ids and 168 runs; release check 6 names the same v2 rows.
- ROADMAP's stage table matches PLAN section 4 and BUILD-PLAN section 1; the INTERVIEW-NOTES and FEEDBACK status lines are present and dated 2026-10-13.
- Dates: no passed date is stated as future in the four documents; the example dates in ARCHITECTURE 7.3 and 7.6 are near-future illustrations and the ring roll (L1009) is 2027-01-01.

## Count by severity

- Blocking: 3 (findings 1 to 3)
- Should-fix: 17 (findings 4 to 20)
- Minor: 16 (findings 21 to 36)
- Total: 36
