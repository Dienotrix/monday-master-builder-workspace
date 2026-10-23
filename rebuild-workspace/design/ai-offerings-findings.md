# monday AI offerings — what the live probes established

Three element kinds were probed live on 2026-09-13 through the monday connector (API ring 2026-10 release candidate): AI agents, Vibe apps and Workflows. This file keeps what those probes showed about monday itself. Nothing in it depends on a particular account: object, board, skill and trigger ids are always looked up live at build time and never written into the plugin. Each finding is a candidate gotcha entry for stage 1b, which moves these element kinds into the main line (A17, A18, A19). AI credits are neither measured nor priced (A17); where a tool returns a credit field, only its existence is noted.

## AI agents

**What the connector exposes.**
- **Trigger catalogue** (`agent_catalog list_triggers`): 18 trigger types can be attached programmatically, each with a block reference, required fields and dependency chains. Board-scoped: item created, deleted, archived or moved to the board; subitem created, deleted, archived or status changed; status changes to a value (board, then status column, then value); column changes; button clicked; update created; form submitted. Account-scoped: user joined the account; board created. Time: "Every time period", with a cron-like schedule (daily, weekly or monthly; hour, minute, IANA timezone, days). Two are integration-shaped (a chat-platform button wait, and a notetaker meeting-ended trigger that needs an admin key). OAuth and third-party triggers (chat, mail, CRM vendors) cannot be attached through the tools: a blueprint that relies on one carries a UI step, not a build step.
- **Skills catalogue** (`agent_catalog list_skills`): account-wide and specific to each account, so skill ids are looked up live and never embedded.
- **Agent object** (`manage_agent get`): `id`, `kind`, `state` (ACTIVE, INACTIVE, ARCHIVED, FAILED), a `profile` (name, role, role description, avatar, colour), `goal`, `plan` (the instructions as markdown, returned in full), `user_prompt` (stored as metadata), `version_id` and timestamps. `create` generates profile, goal and plan from a prompt; `create_blank` takes them literally; `update` changes name, role, description, identity, plan or model; `delete` is permanent; `run` is fire-and-forget with no run-status query. Models come from a fixed list.
- Job-specific instructions belong in agent jobs (`manage_agent_jobs`), which the catalogue tool mentions but the connector roster may not carry. The live roster is the authority at build time.

**What happened when agents were written.**
- `create_blank` creates an agent with an empty plan, and it starts INACTIVE.
- Agent Identity is an account-level feature that can be switched off. When it is, `update` with `identity` is refused (`IDENTITY_NOT_ENABLED`), while `plan` still works. Never design around `identity` without checking the account.
- The response to `update` is stale on `plan`: it reported the plan empty after setting it. A `get` returned the plan verbatim. The text that is approved is the text that is injected, and only a read-back proves it.
- An update can activate an agent. An agent created INACTIVE was ACTIVE after a plan update, with no activate call. The build step is update, read the state back, deactivate if it should be off.
- Knowledge grants (a board or doc, READ or READ_WRITE) can be added, listed and removed.
- Triggers: `add` returns no node id, and `list` is the only read-back. Every new agent also carries two triggers it was never asked for ("When agent is mentioned", "When agent is assigned"); the blueprint lists them and the audit expects them. A trigger's configured board is not readable back (`field_summary` is null).
- Skills: `add` can report "Skill added" when nothing was attached; a later `remove` answered `SKILL_NOT_ATTACHED`. There is no per-agent skill list, so a skill attachment cannot be verified through the API and goes on the by-eye list.
- `version_id` changes when the plan changes and not when the state changes, so it is a clean drift signal for instructions and none for state.
- Explicit `activate` and `deactivate` work; removing triggers and knowledge works; `delete` is final and returns the deleted object once.
- Agents are account-level objects with no workspace field. A test boundary around an agent exists only through what its plan and its knowledge grants name.

**Consequences for the design.**
- Inject authored instructions with `create_blank` and `update` on `plan`, never with `create`, so the approved prompt is the injected prompt.
- After every agent write: read the plan, the state and the triggers back; compare `version_id` against the frozen revision to detect drift.
- Resolve board, column and status ids before wiring triggers, as for automations.
- An agent's write scope is not a property the tools expose. The guard checks trigger targets against the strand's build targets, and the audit reads the plan for board references.
- Skills and a trigger's board binding are by-eye checks, listed as such in the handoff.

## Vibe apps

**What the connector exposes.**
- **App object** (`vibe_list`): `id`, owner, `name`, `status` (CREATED, GENERATING, PROCESSING_MESSAGE, DEPLOYING, READY), `variant` (board view, item view, Vibe item view, object, dashboard widget, full-stack object, campaigns), `is_published` and `published_at`, `state`, a feature reference id, and `access_protection`, which some accounts or variants do not support.
- **Deep read** (`vibe_get`): metadata and an editor link, plus optional slices for status (refreshes stuck states, adds `is_busy`), the build conversation (filterable by date) and code versions (up to 50). An app's code history and its generation conversation are both readable.
- **Create** (`vibe_create`): a natural-language prompt, an optional workspace, board ids to bind (the allowed count depends on the tier), a view id for the dashboard-widget variant, and an optional model. It returns at once; generation is asynchronous and is polled through `vibe_get`. Build messages carry a `credits_used` field.

**What happened when an app was written.**
- A board-view app was created at once and reached READY about a minute later, with code version 1 live and the full build conversation readable.
- **The generator changed the spec on its own.** The bound board had no status column, so it substituted the creation date and said so in its reply. Only the read-back caught it.
- `vibe_ask` answered a read-only question with an accurate description of the app in about eight seconds: a usable read-back of behaviour, in prose.
- A board-view app exists on its board as a real board view while the app lives.
- `vibe_delete` removed the app and its board view; nothing was left to clean up by hand.
- Publication was not exercised. `vibe_publication` exists, and `is_published` and `published_at` are its read-back.

**Consequences for the design.**
- A Vibe app fits the build loop: create, poll, read the code versions and the conversation, compare the delivered app with the request, verify. Diffing against the request is the audit's main job here, because the generator may reinterpret a spec.
- Publication is a distinct state and a distinct tool, so A17's separate yes for publication maps onto a real boundary.
- Generation has no completion signal beyond polling; the same poll-and-match discipline as other asynchronous creations applies.

## Workflows

**What happened when a workflow was written.**
- `create_workflow` creates a workspace object (`monday_workflows::workflow`), readable through `objects(ids)` with name, description, privacy, folder, state, creator and workspace.
- The workflow expert resolves boards from its own option list, which can differ from what the API returns: it could not see a board the API could read. Pass ids the expert can see, and expect refusals on boards the API reads.
- The expert answered "General error" twice — and both calls had applied the change before failing. Neither its errors nor its success messages are evidence; read the draft back.
- `validate_workflow` returned no issues on a correct draft: a real gate.
- The expert can state each binding of a draft, except dynamic (templated) text, which it cannot display.
- `publish_workflow` with `shouldActivate: false` was honoured: the workflow was published and inactive, and a real trigger (an item created on the bound board) produced no run. The expert meanwhile called it "published and active", an inference from the draft's live mode rather than a read of its state.
- Publishing consumed the draft: the live id equals the old draft id, and a second `publish_workflow` with `shouldActivate: true` returned 404. No tool in the roster activates an already-published workflow, so a workflow published inactive can be activated later only through a new draft or the UI.
- Asked to activate it, the expert said it cannot change runtime configuration, and then stated the live workflow had no board, contradicting its own reading of the draft.
- Raw GraphQL exposes `unpublish_object`, `archive_object` and `delete_object`; `archive_object` cleaned up the probe workflow.

**Consequences for the design.**
- Workflows are buildable: create, author through the expert, read back, validate, then publish once with the final activation state decided beforehand.
- Every expert call is followed by a read-back through `validate_workflow`, the `objects` query and the draft. An expert answer is never recorded as a verified fact.
- A live workflow's trigger binding is not reliably readable back. A trigger test in a sandbox is the only proof that it runs on the intended board.

## Exposed through raw GraphQL, not yet exercised

`delete_column`, `delete_object`, `delete_board_automation`, `unpublish_object`, eight `configure_*_ai_column` mutations, `remove_ai_from_column`, `create_webhook` and `delete_webhook`, and `run_prompt`. Columns cannot be removed through the connector's tool roster, which has no `delete_column`; that is a roster limit, not an API one, and the policy in client accounts stays archive-only.

## Not yet probed

Vibe publication; agent run results (runs are fire-and-forget, with no run-status query); AI column writes; webhooks; CRM sequences (A18). Each is probed in a test account before anything is promised, and the test account is the open A11-1 decision.

## Re-checked 2026-10-23, and AI columns probed

Demonstration 4's probes, in the CRM test workspace, re-checked P-19 and P-21 against the connector as it then was and probed AI columns for the first time. The findings are gotcha entries G-110 to G-145 in the plugin's `shared/monday-gotchas.md`, section 14, and `read-back.md` names the reads. What changed against the sections above:

- **Agents.** The connector now splits an agent into an agent-level identity (`plan` is kept as a legacy alias) and jobs, each with its own instructions and triggers, which read back word for word (G-113). The update's answer was stale in both directions, and the first instruction write after `create_blank` was lost while it switched the agent on (G-110, G-111). `version_id` no longer moves with the instructions (G-114). A scheduled trigger's settings are now readable (G-113). New tools: `manage_agent_jobs`, `manage_agent_tools` (integrations, whose notify blocks need a connected chat account) and a skill `create` that writes into the account-wide catalogue (G-116). A job run left nothing readable (G-115). Unchanged: the two default triggers, no per-agent skill list, no workspace field.
- **Workflows.** Unchanged: the expert's changes land when its call fails or times out (G-130), `validate_workflow` is a real gate (G-131). New: `run_workflow_once` runs a draft on a chosen item with real effects and its status reads per step (G-133), and the notification it sends reads back through `notifications` (G-134). The expert now writes out templated text, and it cannot set a wait step (G-131, G-132). `create_workflow` honours its folder (G-135). Publishing was not re-tried; the one-shot publish above stands.
- **AI columns.** Set on an existing column by eight raw `configure_*_ai_column` mutations, read back as recipes on the board, switched off by `remove_ai_from_column` (G-140, G-141); the backfill and new rows fill within seconds (G-142); a custom prompt names columns as `{pulse.<id>}` (G-143); the activity timeline is not a source (G-144).
