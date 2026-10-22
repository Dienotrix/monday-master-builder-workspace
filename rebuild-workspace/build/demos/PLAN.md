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

## Taken for demo 1 (worth the user's nod)

- The plugin has no templates yet (WP7). The record templates `record.py` needs are copied from the unit-test stand-ins into `plugins/monday-master-builder/templates/` as the first lean set, and grow from what the demos show.
- Demo 1 is run by the session by hand from the design documents; the lean `solution-blueprint` and `account-build` skills are written from it, and demo 2 runs through them.
- Left out of demo 1: the AI layer (round two), the audit skill (a read-back of every element stands in), the build notes, and the intake scripts.
