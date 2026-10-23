# Demo builds: plan

Date: 2026-10-21. Internal build file: never client-facing. Under A31 (demo first): real builds in monday from the fictional fixtures, to see whether the plugin can build real solutions, before more safety work.

## Where the demos are built

- **The test workspace the user named** (A11-1, answered 2026-10-21): a closed Work Management workspace in the account the user connected for development. Every live write goes there and nowhere else. Each demo gets its own folder in it, named as the fixture's workspace would be (`<client> – Ops`), in place of A21's new workspace per client while the plugin is being developed. The development tooling may delete test objects it created there (A18 as narrowed).
- **No id in a project file.** The account, the workspace and every object id live only in the client record under `clients/` and in `local/`, which git ignores.
- **The development home** is this project folder (`MMB_HOME`), as HANDOFF's State has it: `clients/<slug>/` holds each demo's record, and `local/settings.json` the user's own settings, written by `record.py home init` and ignored by git.

## Demo 1: s12, Ashenholt Environmental Laboratories

Work Management only, cleared to build, a clean transcript with a header. The first CRM demo (s6) waits for a test workspace in the CRM product, because CRM's native boards cannot be made in a Work Management workspace and a look-alike is never built (A5).

1. **Record.** `record.py home init` for the development home, then `record.py init` for the client and strand 001, then the transcript saved with `add-transcript --fixture`.
2. **Readiness.** The intake and readiness skills are not built yet, so `readiness.md` is written from the transcript with the answer key's `readiness` block as the reference. Demo 1 tests the build, not intake; a later demo runs intake for real.
3. **Blueprint.** `solution/blueprint.md` written by hand from ARCHITECTURE A§3.4, lean: what the build rests on (the assumptions, each `AS<n>`), the folder and boards, columns, groups, views, the automations, the dashboard, the sample data, what is left out, and the `## Element keys` table `ledger.py` reads.
4. **The approval card.** Shown to the user in chat. On a proof of concept in the user's own account one yes covers the whole revision (A28). Automations notify only the user; people columns assign only the user.
5. **The build,** through the write path of BP:252: `record.py freeze`, `ledger.py bind`, `approval`, `change-check`, `record.py lease take`, `ledger.py run start`, and per element `intent`, `leak_lint.py payload`, the connector call, `record` and `verify`; then `run end`. Round one only: boards, columns, groups, items, views, forms, automations and a dashboard; the AI layer is round two.
6. **The user looks at it in monday** and says what is wrong; that is the demo's real acceptance.
7. **The log.** `demo1-log.md` beside this file records every place a script got in the way, every gap in the design the build found, and what the lean skills must say. A script that refuses for a reason the design did not foresee is logged, and the build continues by the nearest path rather than stopping to polish the script.

## Demo 2: s19, Bramblewood Signs, through the lean skills (2026-10-22)

The user's go: "write the lean solution blueprint and account-build skills from demo 1's log, then run demo 2 through them." A sign shop rolling out a chain's store refits: jobs, installs, permits on their own expiry clocks, crews, and a Monday view of what goes out. Work Management only, cleared to build, in a new folder in the same test workspace.

- **The skills:** `plugins/monday-master-builder/skills/solution-blueprint/SKILL.md` and `skills/account-build/` (SKILL.md and `references/write-path.md`), written from demo 1's log; `tools/dev_test_workspace.py` (development only, never shipped) gives a record the named test workspace as a build target, in place of demo 1's hand edit.
- **The test:** a fresh agent that has read only the skill, not demo 1, writes the blueprint and the card; the user says yes or changes it; a fresh agent then builds it through account-build. Whatever the skills leave out shows up as a question or a mistake, and goes into `demo2-log.md`.
- **Set up by the main session, not by a skill** (no intake or readiness skill yet): the record `clients/bramblewood-signs/`, strand `001-store-rollout`, the transcript saved as a fixture, `readiness.md` rendered from the answer key.
- **The leak lint is loosened first** (A33), so the blueprint and payload checks no longer block on structural ids, small numbers, the blueprint's own prose or sample-row numbers.
- **Status, 2026-10-22:** the blueprint written by a fresh agent from the skill alone (v0.1 revision 1 frozen, lint clean), its card and 29 notes on the skill in `demo2-card.md` and `demo2-skill-notes.md`; the card approved by the user ("Ah okay, the card looks good."). The leak lint changed again first (A34: a client's own figures warn). **Built the same day** by a fresh agent from `account-build` alone, in three sittings with 103 monday calls: 70 of 76 rows verified, the five widgets not checkable, A2 departed into UI step U3; its notes are in `demo2-build-notes.md`. Both skills are revised from the two sets of notes, and `demo2-log.md` holds the findings. The user's look comes next (read-me row P7).

## Demo 3: s6, an industrial supplies distributor, CRM, through every lean skill (2026-10-22)

The user's go: "Yes, please create a new test workspace in CRM then." The first demo from a raw transcript, the first CRM build, and the first in which the build installs monday's native CRM boards (A37, A38).

- **Where:** a new folder in the CRM test workspace, a closed workspace in the CRM product made by the main session (A37). A Service demo needs a Service workspace, asked when it comes up.
- **The skills, in turn, each by a fresh agent:** `call-intake` and `build-readiness` (new) on the transcript, graded against the s6 key by a Sonnet agent; `solution-blueprint`; `account-build`.
- **Native boards:** probed first (`crm-natives-probe.md`), then built into the ledger, `native-objects.md` and both skills (A38).
- **Status, 2026-10-22:** built. 47 elements verified (48 with the referenced workspace), eight widgets not checkable, and the quiet-quote alert departed into UI step U4 (its condition stored inverted). The findings are in `demo3-log.md`, and every skill is revised from its agent's notes. The user's look comes next (read-me row P8).

## Demo 4: the AI layer on demo 3 (chosen 2026-10-23)

Asked what the next demo is, a Service fixture or the AI layer on demo 3, the user chose "AI layer on demo 3". It is round two of A27 on the CRM build that exists, with no new workspace.

- **What:** the four AI opportunities demo 3's `readiness.md` marks for round 2: a workflow that drafts the next step for a quiet quote and asks the owner to confirm it (P-21), an AI column summarising each account's last visits, an AI column sorting each new enquiry by product line and region, and an agent that drafts a monthly forecast note for the sales leader (P-19). Built as the next version of strand 001, in the same folder, on its own approval card.
- **Probe first (A17, A18):** AI columns are unprobed; P-19 and P-21 are re-checked against the connector as it is now, since G-65 showed it changes. Each finding becomes a gotcha entry before anything is built. Every account-level object (the agent, the workflow) takes the user's yes before it is made, the probe's included.
- **The skills:** solution-blueprint and account-build learn the element kinds `agent`, `workflow` and the AI column, with the ledger's kind words checked first. Agents and workflows notify only the user and reach only the strand's workspace (A21); no credit figure anywhere (A17).
- **Then:** the card, the user's yes, the build through account-build, and the user's look.

## Taken for demo 1 (worth the user's nod)

- The plugin has no templates yet (WP7). The record templates `record.py` needs are copied from the unit-test stand-ins into `plugins/monday-master-builder/templates/` as the first lean set, and grow from what the demos show.
- Demo 1 is run by the session by hand from the design documents; the lean `solution-blueprint` and `account-build` skills are written from it, and demo 2 runs through them.
- Left out of demo 1: the AI layer (round two), the audit skill (a read-back of every element stands in), the build notes, and the intake scripts.
