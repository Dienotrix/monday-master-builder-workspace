# ARCHITECTURE.md fold-in of A24 to A28: changelog

Editor: the architecture editor of stage 2's first task, 2026-10-14. Source of truth: `AMENDMENTS.md` A24 to A28 with every "Answered 2026-10-14" line. Line ranges are after editing, at the moment each entry was written; later entries above a passage may shift it by a few lines.

Status: complete. Every passage in the map's section 1 was re-read and edited or confirmed; the map's "reviewed and left alone" list was left alone.

## Entries

### Title block and section 0 (L3, L14, L21)
- L3, A24 to A28: the revision note now names A1 to A23 as folded on 2026-10-13 and says the document was re-cut 2026-10-14 under A24 to A28.
- L14, A24: the plugin-root row says stage 0 proved resolution on the Mac and the Windows re-run checks it before the first release.
- L21, A24: the `[s0]` tag says the run was on a Mac, the product targets both systems, the probes re-run on Windows, and a finding that differs names its system.

### Section 2, plugin layout (L40 to L167)
- L42, A24: install is on the user's machine, Windows or Mac; the per-session-copy observation is marked as seen on the Mac and re-checked on Windows.
- L66 to L67, A24: `hooks.json` matchers route to `guard.py` in a command form that resolves on both systems.
- L71 to L76, A27, A28, A25: `record-map.md` notes the readiness shape gains a goals list before pains; `safety.md` carries the own-account one yes and where assumptions may live.
- L85 to L91, A24, A26, A27: `first-run.md` lists the firm name, default account, optional never-shown workspaces, the optional local-or-GitHub archive choice, Python and the connector on the running system, the GitHub tool only when chosen; `new-client.md` asks only what cannot be inferred; `research.md` runs the deep dive before the first build when days allow; `versions.md` carries version purpose and the sign-off warning.
- L96, A27: `call-types.md` records the best guess as assumed; the fallback applies when it cannot tell.
- L102, A27: `readiness-guide.md` names goals and pains first.
- L108 to L109, A25, A28: `approval.md` lists assumed terms and forks built on their leaning, and the one yes or the yes per list.
- L117 to L119, A28: `build-loop.md` seed data follows the realism and sample-marking rule; `automations.md` has own-account and client-account confirmation modes; `changes-removals.md` keeps own yes for publication and activation in a client's account.
- L129 to L130, A24, A26: `archive-on-mac.md` is renamed `archive.md`: the local archive by default, the GitHub option when chosen.
- L141, L147, A24, A26: `mmb_common.py` builds the home from the user's home directory; `archive_check.py` does the local copy-and-compare, clone comparison for the GitHub option only.
- L151, L155, A26: `client-gitignore.txt` is marked GitHub option only (kept, per the answered line); `archive-handoff.md` is what the archive holds.
- L160 to L164, A24: the sweep's handle rule reads "in a project file"; `release.sh` becomes `release.py`, Python, running the six end-to-end tests on both systems.
- L167, A24, A26: counts re-totalled and unchanged: 8 SKILL.md, 26 references, 3 agents, 6 shared, 7 scripts, 35 templates, 4 others, 89 files (the rename adds nothing; `client-gitignore.txt` stays). `release.py` is repo-only and not counted.

### Section 3.0, conventions (L178)
- L178, A24: the script invocation is one form that must resolve on both systems; the Mac form stage 0 proved is kept as the known case and the Windows re-run settles the spelling before WP2 fixes the shared form.

### Section 3.1, `engagement` (L183 to L192)
- L189, A24: the once-per-session Python and plugin-root check runs on the system in use, Windows or Mac.
- L189, A27: new-client setup asks only what it cannot infer and shows the rest as assumed; the deep dive runs before the first build when the one to three days exist, the plugin proposing the cadence and the user setting it.
- L189, A25: recording `signed-off` lists unconfirmed structural assumptions as a warning and records the event if the user still chooses to.
- L191, A26: first-run settings are the firm name and renderings, the default account, the optional never-shown workspaces, the archive choice, and a GitHub account only when GitHub is chosen.

### Section 3.2, `call-intake` (L194 to L205)
- L200, A27: the call type is a best guess recorded as assumed with its signals; intake carries on and tells the user; a correction re-runs what depended on it; it stops only when it cannot tell.
- L200, A27: the A11-3 question is named as a stop no inference can replace; the alias table is shown and recorded as assumed, with a stop only for an identity the evidence cannot settle.
- L200, A25: reactions after a showing note which assumption, assumed term or fork leaning each confirmation covers; the confirmation recorded is always the user's, reporting the client.

### Section 3.3, `build-readiness` (L207 to L233)
- L213, A25, A27: thin input gives a basic demo rather than nothing; approved assumptions carry a proof of concept while visibly unconfirmed. Stale line fixed: the fixture fix pass is complete (2026-10-13); the `goals` list reaches the record-map pin and the 25 answer keys in a follow-up pass.
- L217, A27: part 1 is "Goals and pains", goals with quotes and locations first; still nine parts.
- L219, A25: an open structural question is built on its leaning with the user's yes, marked assumed, with what a later switch keeps.
- L221, A25: assumptions live in the record, on the card and in the build notes, and stay assumed until the user reports the client's confirmation or acceptance.
- L224, A27: a generic clearance is built and shown with its assumptions listed rather than held for better inputs.
- L231, A28: approving the card on an own-account proof of concept also covers the lists and irreversible steps.

### Section 3.4, `solution-blueprint` (L235 to L246)
- L241, A28: sample rows follow realism over the hour, invented but plausible, every value marked sample in the record.
- L241, A25: where the client cannot be reached, the automation conditions and board-architecture overview go on the card as assumed.
- L243 section 1, A25: "what this build rests on" adds the version purpose, the assumed terms, and forks and open questions built on their leaning with what a switch would keep.
- L243 section 4, A25: structure must be confirmed or accepted before a working solution, not before any build; a proof of concept may rest on it unconfirmed with the user's yes.
- L243 section 5, A25: a fork open at approval is built on its leaning, marked assumed; the user's blocking flag [L14] is the one stop.
- L243 sections 13 and 14, A28: the per-list yes holds in a client's account and for lists notifying real people; the card's one yes covers lists on an own-account proof of concept; the data policy carries the sample-row counts.

### Section 3.7, `account-build` (L256 to L268)
- L260, A28: the description asks for each list and irreversible step unless the card's yes covered them (780 characters, under the 800 limit).
- L266, A28: publication and activation keep their own yes in a client's account; the grouped list re-confirmation holds in a client's account and for lists that notify real people, while on an own-account proof of concept the card's one yes covers lists and irreversible steps and the build does not stop again; sample rows follow the realism rule and are recorded `sample_data`. `sample-cleanup`'s archive yes is unchanged, since cleanup is not part of an approved revision.

### Section 3.8, `solution-audit` (L270 to L280)
- L280, A25, A23: the build notes give each open item a short paragraph (what was assumed, why, what the client needs to clarify); assumptions never enter the client's workspace; the notes are the seed of the later master document (solution, why, diagrams, how to use, SOPs), the v2-or-v3 SOP and handoff package, nothing of it v1.

### Section 3.9, `client-closeout` (L282 to L290)
- L286, A26: the description archives locally by default or to GitHub if chosen (779 characters).
- L290, A24, A26: "on the Mac" becomes the user's machine, Windows or Mac; the archive is a local verified copy-and-compare into `archive/<slug>/`, the holding folder emptied by hand, no repository, clone, git, Trash or Recycle Bin; GitHub runs only when chosen; `archive.md` describes both; `archive-handoff.md` records what is kept and what the user deletes by hand.

### Section 5, scripts and runtime (L325 to L362)
- L329, A24, A26: one surface on two systems with identical behaviour, Linux following without being a target; `git` and the GitHub tool needed only on the GitHub path; hook findings marked as seen on the Mac and re-checked on Windows; Python 3.9 floor and the newest Python tested on both systems.
- L331, A24: "a feature only one system has"; paths from the standard library's home directory, no fixed separator, either line ending; Projects revisit "when they can reach the user's machine".
- L335, A24, A26: the invocation form must resolve on both systems, the Windows re-run settling its spelling before WP2; `.work/` moves with the folder but is never part of the verified archive, and the `.gitignore` keeps it out only on the GitHub path.
- L339, A24: tests run on both systems; path objects and either line ending.
- L340, A26: the one removal a script makes is the record close's, of a client folder whose copy in `archive/` was verified and on the user's yes.
- L344, A24, A26: the home is `monday-builder` under the standard library's home directory; the walkthrough explains setting `MMB_HOME` per system; `archive/` added to the home tree; `settings.json` drops the mandatory GitHub account, keeping it only when GitHub is chosen, and gains the archive choice.
- L352 to L358, A24 to A28: `mmb_common.py` builds path objects; `home init` checks the GitHub tool only on the GitHub path; `version mark signed-off` prints unconfirmed structural assumptions as a non-blocking warning and records the list; `ledger.py` records the own-account card yes as `approval_mode: own-account-poc`, each covered step as an `irreversible-yes` row with `mode: card`; `transcript_measure.py` reads either line ending and keeps the same PDF fallback on both systems; `transcript_prep.py type` carries `proposed` tokens on as assumed; `archive_check.py` is a manifest-based local copy-and-compare with the GitHub clone comparison for that path only (line figure kept at 190, total "about 3,110" unchanged).
- L360, A24: repo tooling is all Python (`tools/release.py`); the sweep's handle rule reads "in a project file", a user's handle living only in local settings.

### Section 6, templates (L368)
- L368, A27: the call-type header keeps its three states; `proposed` is the best guess carried on as assumed.
- L368, A26, A28: `archive-handoff.md` lists what the local archive holds and what is left to delete by hand; `client-gitignore.txt` is the GitHub path's only; `exclusions.md` is the list the realism rule reads. Template count unchanged at 35.

### Section 7.1, file map (L375 to L440)
- L377, A26: the scratch kind is "never part of the verified archive"; a sentence says the Archived column means the local `archive/` by default or GitHub when chosen.
- L396, A26: the `.gitignore` row is written at init on the GitHub path only.
- L431, A25: `open-questions.md`'s "what it blocks" notes a structural question blocks a proof of concept only through the user's blocking flag [L14].
- L435, A27: `call_type` is the best guess, recorded as assumed with its signals until corrected or confirmed.
- L439, A24, A26: `archive/` added to the paths under the home.
- L441, A26: the slug names the folder under `archive/`; the repository name belongs to the GitHub path only. The A11-3 retention cells are unchanged (the decision stays open; only the destination changed).

### Section 7.3, `build.json` (L482 to L580)
- L549, L553, L567, L570, A25, A28: the example approval gains `approval_mode`, and `rests_on` gains `purpose`, `assumed_terms` and `forks_on_leaning`; the object row gains `assumption_refs`; the `irreversible_yes` row gains `mode` and `approval_ref`.
- L577, A25, A28: `other-strand-modified` takes its own yes at execution in a client's account and the card's yes on an own-account proof of concept; a new paragraph defines `approval_mode` (`own-account-poc` or `per-list`), `mode: card` rows, `assumption_refs` and `sample_data` as never cited.

### Section 7.4, versions and events (L582 to L609)
- L584, A25: `version.md` front matter gains `purpose` (`proof-of-concept` or `working-solution`).
- L586, A25: "no criteria behind it" is replaced: a version carries its purpose; `v1.0` is recorded by the user reporting the client; recording it lists unconfirmed structural assumptions as a warning and does not block.
- L592, L607, A25: the events line and the Events paragraph keep the list of unconfirmed structural assumptions with the `signed-off` record. The `released` row is unchanged.

### Section 7.5, evidence markers (L611 to L627)
- L623, A25: `[A]` covers assumed terms and forks built on their leaning, is cleared by the client's confirmation or acceptance as the user reports it, and stays assumed until then.
- L625, A27, A28: an assumed call type uses the header's `proposed` state, and sample values carry `sample_data` and no evidence marker, so they can never be cited.

### Section 7.6, `log.md` (L644)
- L644, A25, A26, A27: `decision` covers the user's approval of assumptions and a corrected call type; `archive` covers the local move by default and the GitHub archive when chosen. No new entry type.

### Section 7.7 and 7.8, strands and live map (L646 to L716)
- L677, A25: the "what this build rests on" body block holds the version purpose, the assumptions, the assumed terms and forks built on their leaning.
- L679, A25: recording `signed-off` shows the warning and advances the stage regardless.
- L683, A25: `SUMMARY.md` records which assumptions the client confirmed or accepted (as the user reported) and which remain assumed.
- L704, A28: `change-with-own-yes` takes its own yes at execution in a client's account and the card's one yes on an own-account proof of concept.

### Section 8.2, first run and new client (L742 to L751)
- L744, A24, A26: the walkthrough asks the firm name and default account, offers the never-shown workspaces and the local-or-GitHub archive choice, creates the home under the standard library's home directory with `archive/`, checks Python and the connector on the running system, and the GitHub tool plus a stored GitHub account only on the GitHub path; the fresh-session nudge stays a suggestion.
- L747, A27: setup asks only what the record cannot answer; the rest is assumed, labelled and shown on the card.

### Section 8.3, intake (L753 to L767)
- L757, A26, A27: the A11-3 question names the archive as local by default or GitHub; it is called the one stop on the first-hour path no inference can replace.
- L759, A27: the alias table is shown and assumed; the call type is a best guess recorded `proposed` and carried on as assumed, intake telling the user and a correction re-running what depended on it. The conservative fallback now holds only when intake cannot tell and stops to ask; a call with no code markers leans `configured-structure`, so the fallback no longer blocks output by default.
- L760, A25: reactions after a showing note which assumption each confirmation covers.
- L763, A27: the call-set order is proposed and assumed like the call type, the user free to correct it.

### Section 8.4, readiness (L769 to L771)
- L771, A27, A25: goals and pains first; open structural questions carry a leaning a proof of concept may rest on; the check re-runs after a corrected call type.

### Section 8.5, blueprint, approval and freeze (L773 to L784)
- L777, A25: step 1 carries assumptions, open structural questions with their leaning and forks into section 1, beside the assumed terms.
- L780, A28: step 4 sample rows follow realism over the hour and are marked sample.
- L781, A25: step 5's client term read-back is narrowed: column names and status labels show on the card for the user to check; the automation conditions and the board-architecture overview are what the user confirms as solution architect; when the client cannot be reached they go on the card as assumed and are checked at the next contact.
- L782, A25, A28: step 6's card adds the version purpose, assumed terms, forks on their leaning with what a switch keeps, each fork's leaning, the client terms for checking, and the approval mode by target.
- L783, A25, A23: step 7 builds a fork open on its leaning, marked assumed, with a build-notes paragraph; the user's blocking flag [L14] is the one stop; whether it also refuses the freeze stays the pending part of L14.
- L784, A25, A28: step 8 records the approval mode; only a fork flagged blocking is left unbuilt.

### Section 8.6, build (L786 to L800)
- L792, A28: step 15's plan re-confirm says no confirmations beyond the card's yes on an own-account proof of concept.
- L793, A28: step 16 seed data follows the realism rule and is recorded `sample_data`; publication and activation take their own yes in a client's account and the card's yes on an own-account proof of concept.
- L796 to L797, A28: steps 19 and 20, the per-number irreversible yes and the grouped list confirmation, apply in a client's account (and for lists notifying real people); on an own-account proof of concept the build does not stop again, each `irreversible_yes` row pointing at the card's approval in the ledger; rows are read back either way.

### Section 8.8, shown, release and round two (L812 to L817)
- L814, A25: reactions after a showing record which assumptions each confirmation covers.
- L815, A27: round two is an order of work, not a wait; with the usual one to three days the deep dive runs before the first build, sample data is refined and round two is built and audited before the first showing; the plugin proposes the cadence and the user sets it.
- L816, A25: "No criteria sit behind it" is replaced by the sign-off warning listing unconfirmed structural assumptions, recorded with the event, never blocking; `v1.0` starts the working-solution versions.

### Section 8.10, close-out (L825 to L829)
- L827, A24, A26: strand close runs on Windows or Mac; "nothing is pushed, nothing moves to the Trash" becomes "nothing moves into `archive/`, nothing is pushed".
- L829, A24, A26: the record close's archive part is local by default: manifest, copy into `archive/<slug>/`, compare, card and index, then on the user's yes the original leaves `clients/`; `archive/` is emptied only by the user; no Trash, Recycle Bin, repository, clone or git. The GitHub archive is described as the chosen option, ending with the same move into `archive/`. The A11-3 refusal stays.

### Section 8.11, recovery (L831 to L835)
- L833, A28: a lost `create_automation` reply still needs re-confirmation on an own-account proof of concept, since the card approved one creation, not a second (matches SPEC's recovery criterion).

### Section 9.1 to 9.6, authority, approvals, irreversible steps, lists, lint (L838 to L927)
- L849, L850, L853 to L855, A28: the Condition cells for creating an agent, changing another strand's object, creating a list item, publishing or activating, and an irreversible operation split by target: own yes or grouped confirmation at execution in a client's account (and for rows notifying real people), the card's one yes on an own-account proof of concept.
- L857, A25: recording `signed-off` shows unconfirmed structural assumptions first, as a non-blocking warning.
- L859 to L860, A24, A26: the "push to GitHub, archive, delete locally ... on the Mac ... moved to the Trash" row becomes a local archive row (Windows or Mac, verified copy-and-compare, folder moved into `archive/`, emptied by hand) plus a separate GitHub row for the chosen option. Table rows now 18 (was 17).
- L866, A28: approvals gain the settled own-account proof-of-concept exception; graduated approvals stay deferred and unrelated.
- L894, A28: one sentence under the irreversible table: Handling describes a client's account; on an own-account proof of concept the card's one yes covers each listed step, and a step reaching real people keeps its own yes on either target. Rows unchanged.
- L900, A28: "Which target asks how" paragraph in 9.5: per-list approval and execution re-confirmation for a client's account and lists notifying real people; the card's one yes covers lists on an own-account proof of concept, rows still shown and read back.
- L906, A28: a row notifying anyone other than the user takes its list's own yes and grouped reply on either target.
- L926, A24: the cross-client wall reads "on either system".

### Section 9.9 and 9.10, quota and hooks (L946 to L962)
- L948, A27, A28: the first-hour estimate is a floor, not a ceiling; realism may take longer; with one to three days the estimate covers both rounds; D4's split orders the work.
- L952, A24: hook findings are marked as seen on the Mac; `hooks.json` uses a command form that resolves on both systems; the Windows re-run checks hook launch.
- L954, A24: the record-root walk uses the standard library's path handling, no fixed separator.

### Section 0 table and section 4 (L12, L314)
- L12, A28: the approval row says per-item confirmations at execution apply in a client's account, one card yes on an own-account proof of concept.
- L314, A24: the agents' stage-0 findings are marked as seen on the Mac and re-checked on Windows.

### Section 12, decision log (L1094 to L1186)
- L1102, stale state: the stage 1b citation notes that stage 1b is complete as of 2026-10-13.
- L1104, A26: 12.3-17 is the GitHub owner for the GitHub archive only; the default archive needs no account.
- L1108, A24, A25, A26, A27: 12.3-4 gains version purpose and the non-blocking sign-off warning; 12.3-6 becomes Windows or Mac; 12.3-20 is replaced by the local archive default with git and GitHub only on the chosen path; 12.3-25 says the strand's class is proposed and set by the user at strand open or by approving the card that shows it, against the per-call header as a best guess.
- L1123, L1135, L1137, A26, A24: the A11 row notes the refusal guards both archives; the A20 row notes "on the Mac" described where stage 0 ran; the A22 row's home moves to `monday-builder` under the user's home directory.
- L1139 to L1143, A24 to A28: five new rows say where each amendment landed. The amendments table now runs A1 to A28 (28 rows).
- L1174, L1175, A24: the stage-0 findings row is marked as seen on the Mac and re-checked on Windows; Projects revisit "when they can reach the user's machine".

### Section 13, pending items (L1188 to L1210)
- L1198, A26: the A11-3 question's archive part names local by default or GitHub; the decision stays open with no default.
- L1202, A25: L14 is restated as the user's blocking flag, the one way to stop a fork's elements being built; whether it also refuses the freeze stays open with the same default.
- L1204, A24, A26: stage 0 is complete on macOS; the probes re-run on the user's Windows machine before the first release inside WP-S0 (not a new package) with the short Windows list (hook launch, plugin-root spelling, GitHub tool only where GitHub is chosen); release checks run the unit tests and the six end-to-end tests on both systems, the archive test covering local on both and GitHub wherever set up.

### Section 14, deferred and risks (L1212 to L1252)
- L1214, A25: the v2-or-v3 list places the later master document (solution and why, diagrams, how to use, SOPs) with the handoff package, seeded by the build notes.
- L1218 to L1219, A24: the plugin-root risk is rated per system; a new risk row covers behaviour differing between Windows and Mac, mitigated by Python-only tooling, path objects, either line ending and release checks on both systems. Risk rows now 36 (was 35).
- L1222, A28: a wrong automation's execution re-confirmation applies in a client's account; the card's yes covers it on an own-account proof of concept.
- L1229, A27, A25: thin input: a basic demo beats nothing; the mitigation is visible assumptions through to the sign-off warning.
- L1243, A27: a misdetected token is a best guess the user may correct at any time; the fallback holds while intake asks; the doors read the class the user sets or approves.

## Counts re-totalled
- Installed files: 89, unchanged (8 SKILL.md, 26 references, 3 agents, 6 shared, 7 scripts, 35 templates, `plugin.json`, the plugin README, `hooks.json`, `guard.py`). `archive-on-mac.md` is renamed `archive.md`; `client-gitignore.txt` stays for the GitHub path.
- Scripts: 7, unchanged; script lines "about 3,110", unchanged (`archive_check.py` keeps 190 for both paths).
- Repo tools: `release.sh` becomes `release.py`; not an installed file.
- Skill descriptions after editing: engagement 776, call-intake 783, build-readiness 668, solution-blueprint 783, account-build 780, solution-audit 718, client-closeout 779, monday-drift-check 701 characters, all under 800.
- Readiness parts: nine, unchanged. Blueprint sections: sixteen, unchanged. Build-notes sections: six, unchanged.
- Tables: authority table 18 rows (one row split in two); amendments table 28 rows; risk table 36 rows.

## Worth the user's nod
- **`archive-on-mac.md` renamed `archive.md`** (section 2 and wherever cited). The amendments drop the Mac framing but do not name the file. The BUILD-PLAN editor may need the same rename.
- **The one script invocation form is left to the Windows re-run.** A24 says scripts are invoked "in a form that resolves on both systems" without naming it (`python3` is not a given on Windows). The architecture keeps the Mac form as proven and lets the stage-0 Windows re-run settle the shared spelling before WP2, rather than picking `python`, `py -3` or a launcher now.
- **The per-file alias table becomes assume-and-show** (3.2). A27's "asks only what it cannot infer" covers the whole first-hour path; the alias table is now shown and recorded as assumed, with a stop only for an identity the evidence cannot settle. The "never inferring an identity silently" rule stays.
- **The local archive's mechanics** (3.9, 5.3, 5.4, 8.10). `archive_check.py prepare` hashes every file into a manifest, the folder is copied into `archive/<slug>/`, `compare` checks the copy, and only then, on the user's yes, the original leaves `clients/`. That removal is written as the one exception to "scripts never delete". The whole folder is copied, `.work/` and any input the retention answer keeps out included, and `archive-handoff.md` lists what the user is left to delete by hand, so the plugin itself deletes nothing the user has not seen listed. The alternative, a plain rename into `archive/` checked against the manifest afterwards, would avoid the exception but departs from the "copy-and-compare" wording of A26 and SPEC.
- **Call-type token states keep their names** (6, 5.4). `detected`, `proposed`, `confirmed` stay; `proposed` now means the best guess carried on as assumed. Renaming it `assumed` would ripple into fixtures and graders.
- **The own-account yes in the ledger** (5.4, 7.3): an approval entry carries `approval_mode: own-account-poc` or `per-list`, and `irreversible-yes` rows carry `mode: card` (or `at-execution`) with the card's `approval_ref`. The field names are the editor's choice.
- **`sample-cleanup` keeps its own yes** (3.7). It runs outside an approved revision, so the A28 card yes does not reach it.
- **Where version purpose and assumption links live** (7.3, 7.4). Purpose is a `version.md` front-matter field, `purpose: proof-of-concept | working-solution`, echoed in `build.json`'s `rests_on`; an element built on an assumption lists it in `assumption_refs`. The field names are the editor's choice; `record.py status` may need `purpose` in its pinned shape (a WP2 detail).
- **`output_class` without code markers leans `configured-structure`** (8.3 step 5). This replaces the old effect of the fallback, `bespoke-code` until the user set the class, which blocked any buildable claim. The fallback still holds while intake asks because the markers point both ways. A27 and "a basic demo beats nothing" point this way, but the exact inference is the editor's.
- **The call-set order is assumed rather than confirmed** (8.3). Intake carries on with its proposed order and the user may correct it. BUILD-PLAN's graders score "the order"; they should score the settled order (for the BUILD-PLAN editor).
- **A blocking flag stops the build of that fork's elements, not the freeze** (8.5 steps 7 and 8). Whether it also refuses the freeze stays the pending part of L14.
- **On the GitHub path the local folder also moves into `archive/`** (8.10), not to the Trash, so the holding-folder rule of A24 holds on both paths.
- **Recovery keeps its re-confirmation on an own-account proof of concept** (8.11). This follows SPEC's recovery criterion: no list row is re-created without a fresh confirmation.
- **12.3-25: the strand's class can be set by approving the card** that shows it, not only by an answer at strand open. This squares "asks only what it cannot infer" (A27) with "no door runs on a class the user has not seen".
- **For the other editors:** BUILD-PLAN H44 expects the alias table "proposed once, confirmed", and its graders score the call-set order. Both are now assume-and-show in the architecture. BUILD-PLAN's file lists should also take the `archive.md` rename and `tools/release.py`.
