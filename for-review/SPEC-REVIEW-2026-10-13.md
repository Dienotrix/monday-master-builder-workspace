# SPEC review by interview, 2026-10-13

The user reviews `rebuild-workspace/design/SPEC.md` as a conversation, section by section. Each round records the user's answer and what it changes. Edits to SPEC are applied in one pass at the end of the interview; decisions are recorded as amendments as they are made.

## Round 1: the opening and who it is for

- **Question 1, the first-run walkthrough and the surface.** Answer: a major correction. The plugin must be agnostic and work on Windows and Mac. Recorded as A24 the same minute. SPEC edit pending: the "One surface" bullet, the home folder bullet, the walkthrough bullet and every "on the Mac" phrase.
- **Question 2, the session rule.** Carried to round 2.
- **A24 follow-ups.** The user has a Windows machine with Claude Code for the Windows probe run: yes. The record close moves a closed folder into a holding folder under the home instead of the Trash or the Recycle Bin, emptied by hand: yes. Both go into A24's consequences as confirmed and into the SPEC close-out step.

## Before the restart: two points the user caught reading the document

- **A24 sharpened in the user's words:** identical behaviour on macOS and Windows; every filesystem, process, Python, archive and cleanup operation OS-independent or with a tested platform-specific implementation; no supported system may require the other; release criteria: install, intake, build, interruption recovery, audit and archive tests on both. Recorded in A24.
- **A25, new:** assumptions may carry a proof of concept when the user approved them and they stay visibly unconfirmed; a client-approved working solution needs the structural assumptions confirmed or explicitly accepted before production use; an unconfirmed structural decision never by itself prevents a proof of concept. Resolves the conflict between the readiness check and the architecture's pre-build confirmation of structure, terms and forks. SPEC edits pending: the readiness bullet, the blueprint bullet, the approval card, the build step, lifecycle steps 5 to 7 and 11, and the safety section.

The rounds restart from round 1.

## Round 1 (restart): the opening and who it is for

- **Walkthrough.** Simpler: no GitHub account; the plugin creates the local home folder itself; firm name and default account stay; the never-shown workspaces become optional. Recorded as A26, with the archive turned local. SPEC edits pending: the home and walkthrough bullets, the close-out bullet and lifecycle step 12, the safety section's archive line, the success criteria's daily-use and record rows, the worked day's close.
- **Session rule.** Keep: a nudge is nice, the user decides. No edit.

## Round 2: intake and the readiness check

- **First thing looked for:** goals and pains. Part 1 becomes "goals and pains" with a `goals` list added to `readiness/1`; the keys get it in a small follow-up pass. Recorded in A27.
- **Call type:** proceed on the best guess, stop only when the plugin cannot tell; show, not tell; a basic demo beats nothing. Recorded in A27. SPEC edits pending: the intake bullet and lifecycle step 2, the readiness bullet and lifecycle step 3, the first-hour paragraph.

## Round 3: the blueprint, the approval card and the build

- **Approvals:** one yes for the whole card on an own-account proof of concept; per-list yeses kept for client accounts and anything notifying real people. Recorded in A28.
- **Sample rows:** realism over the hour; dozens where dashboards need numbers; invented plausible names and figures in the client's industry are fine, minus the exclusion list, marked as sample. Recorded in A28. SPEC edits pending: the approval card bullet, lifecycle steps 6 and 7, the first-hour paragraph, the success criteria row "First hour".

## Round 4: after the build

- **Audit before the first showing:** worth running; keep as written. No edit.
- **Iterate or fresh:** the plugin proposes with its reason, the user confirms. Added to A21. SPEC edit pending: the iterate-or-fresh bullet and lifecycle step 10.

## Round 5: v1 scope

- **Languages:** English only in v1. Keep. No edit.
- **Deletion:** by hand everywhere, the user's own account included; the plugin sends no delete call in any account. SPEC edit pending: "in a client account" becomes "in any account, the user's own included" in the out-of-scope list and the safety section.

## Round 6: how it stays safe

- **Execution-time confirmation of irreversible steps:** the card's yes is enough on an own-account proof of concept; kept for client accounts. Added to A28. SPEC edit pending: the irreversible-steps bullet and lifecycle step 7.
- **Neutral naming:** workspaces stay strictly neutral, so they can be handed over as they are. Keep. No edit.

## Round 7: how v1 proves itself

- **The user's own acceptance tests, on the assistant's recommendation, accepted:** the first-hour run on s5 and then s1 in the user's own account, transcript to audited workspace with build notes, clock running; and the refusal test, a planted element outside the client's workspaces and an agent scoped to a third workspace, both refused before any call. These lead the stage 5 end-to-end run.
- **Time ceiling:** none; the first-hour row says measured and recorded. SPEC edit pending.

## Round 8: the worked day, and what live testing changed

- **The worked day:** reads right, with one correction of cadence: there are normally one to three days of preparation before the client meeting. The first hour is the floor, not the typical case. Pending: an amendment line making the two-round default cadence depend on the time available (deep research before the first build and round two before the first showing when there is time), and the worked day rewritten over two days.
- **Kanban, Gantt and calendar views:** the user asks for a live re-check of the API and the connector before the spec repeats the September finding. Checked in this session; result below.
- **View check result (2026-10-13, live schema, read-only):** the connector's `create_view` tool accepts TABLE, DASHBOARD, FORM and APP; the API's `ViewKind` enum holds the same four values, and `BoardView.type` is a free string only when read. Kanban, Gantt, calendar, timeline, chart and workload views still cannot be created through the API or the connector; the September finding (gotcha G-line 157: KANBAN rejected before sending, raw KANBAN, CALENDAR and GANTT rejected as absent enum values, APP needing an `app_feature_id`) stands unchanged. One probe added for the test workspace, P-29: whether the APP kind with a built-in view's app feature id creates one of these views. The change check re-reads `ViewKind` at every build, so the day monday adds a kind the build picks it up.

## Round 9: the hand-made views, and the open decisions

- **Kanban, Gantt and calendar:** listed in the build notes' presentation checklist for the user to add when they choose; no walk-through before the showing. Added to A23. SPEC edits pending: the audit and build-notes bullet, the views line under what live testing changed (re-checked 2026-10-13).
- **The three open decisions:** left until each first matters; the test workspace is named when the first live probe asks. No edit.

## Outcome

Nine rounds, two questions each. Decisions recorded as amendments as they were made: A24 (Windows and Mac, identical behaviour, with release criteria), A25 (assumptions may carry a proof of concept; a working solution needs them confirmed), A26 (no GitHub account; local home and archive), A27 (show, not tell: goals and pains first, best-guess call type, the hour as the floor with one to three days of preparation the usual case), A28 (one yes on an own-account proof of concept, irreversible steps included; realism over the hour; invented sample data allowed), and lines added to A21 (iterate or fresh proposed by the plugin) and A23 (hand-made views on the checklist). SPEC is rewritten from this log in one pass; ARCHITECTURE, BUILD-PLAN, ROADMAP and the readiness spec fold A24 to A28 in as the first task of stage 2, and the 25 keys gain the `goals` list in a small follow-up pass.
