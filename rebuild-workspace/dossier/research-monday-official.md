# monday.com official docs and offerings: research dossier

Research date: 2026-09-10. Scope: monday's own developer docs, support site, MCP docs, monday's public GitHub repos, and the claude.com plugin/connector listings. Written independently (clean-room); nothing taken from the old plugin.

How to read this file
- Every claim carries a source key in brackets, for example [D-rate]. Keys resolve to URLs in "Sources" at the end.
- "Not confirmed" means the official material is silent, ambiguous, or conflicting.
- "Inference" marks my reasoning, not a documented statement.
- Doc pages fetched as markdown (monday supports appending `.md` to any doc URL [D-llms]); most pages showed `updatedAt` between 2026-09-03 and 2026-09-10. Support articles were read through the public Zendesk Help Center API because the HTML pages return 403 to non-browser clients.
- GitHub source (mondaycom/mcp) is official monday code but not documentation; facts taken only from source are marked "(source)".

---

## 0. Ten findings that matter most for the build

1. Hosted MCP is `https://mcp.monday.com/mcp`, Streamable HTTP only; `/sse` is deprecated and unsupported [D-mcp-clients][D-mcp-integrate]. monday's own "Connect with Claude" support article still shows `/sse` for the custom-connector method [S-claude] (conflict: use `/mcp`).
2. MCP is preinstalled on every account and free on every plan, but an account admin controls it: a master "AI Connectors" toggle, a "Public Hosted MCP" sub-permission (covers Claude), and an optional "Specific Workspaces" scope [S-connectors][S-mcp-start]. Viewers have no MCP access; guests only if an Enterprise admin enables it [S-connectors].
3. Every MCP action runs as the authorizing user with that user's permissions; MCP calls count toward the account's daily API call limit (Standard 1,000 per day) [D-mcp-integrate][D-mcp-overview][D-rate].
4. Product binding: a workspace is tied to a product only by passing the account's numeric product ID (`account_product_id` / MCP `accountProductId`). monday's own CRM plugin documents that passing the string `crm` or omitting the ID creates a generic workspace [D-workspaces][D-mcp-create-workspace][G-crm-changelog][G-crm-skill].
5. Views: the documented `ViewKind` for create/update is only `APP`, `DASHBOARD`, `FORM`, `TABLE` [D-views]. Kanban, Gantt, Calendar, Timeline, Chart, Map exist only in the dev (preview) schema (source) [G-schema].
6. Dashboards: create and delete are documented; there is no documented query to read dashboards or widgets back, and no argument for widget layout or position [D-dash][D-dash-types]. Widget kinds documented: `APP_FEATURE`, `BATTERY`, `CHART`, `LISTVIEW`, `NUMBER` [D-dash-types].
7. Automations: MCP `create_automation` builds board automations from a structured natural-language description (one trigger, AND-only conditions, no branching) and has no public GraphQL equivalent; list/activate/deactivate/delete also exist; workspace-level workflows have plan/create/update/publish tools on the dev schema [D-mcp-create-automation][D-mcp-tools].
8. Formula columns can be created with an expression but are read-only, not filterable, and `display_value` does not support formulas that reference mirror or connect-boards columns [D-formula]. Mirror columns are create-and-read only [D-mirror].
9. The official monday.com Cowork plugin is small: one connector plus five everyday skills (items, status reports, single-board setup, docs, forms); no commands, agents, or hooks [G-cowork][C-plugin]. The same five skills ship as `mondaycom/skills` [D-ai][G-skills]. Nothing official covers multi-board solution architecture, product binding, relations/mirrors, dashboards, automations, verification, or client lifecycle.
10. No official "consultant / delegated partner access" mechanism for MCP or API was found (not confirmed). A guest cannot create boards [S-guest], so building needs a member or admin seat in the client account, or a client-owned custom OAuth app [D-mcp-oauthapp].

---

## 1. The official monday MCP server

### 1.1 Endpoint, availability, who can use it
- URL `https://mcp.monday.com/mcp`, transport Streamable HTTP; `https://mcp.monday.com/sse` is deprecated and not supported [D-mcp-clients][D-mcp-integrate][D-ai].
- Conflict: support article "Connect monday MCP with Claude" (updated 2026-08-21) lists `https://mcp.monday.com/sse` for manual custom connectors [S-claude].
- Preinstalled on all accounts; the marketplace listing is only for discoverability [S-connectors][S-mcp-tools]. Conflict: the marketing page still says admins must install the monday MCP app [M-mcp].
- All plans, no extra cost; "Standard API limits apply" [S-mcp-start][M-mcp].
- Admins and members on all tiers; on Enterprise, admins can enable guests (off by default); viewers have no MCP access [S-connectors].
- In Claude: available in the connector directory for Pro, Max, Team, Enterprise on web, desktop, mobile. Team and Enterprise need an owner to enable the connector for the organization, then each user connects via OAuth [S-claude]. The claude.com connector page lists 33 tools/capabilities with grouped names (for example `create_items_and_tasks`, `manage_agent`, `get_monday_knowledge`), added November 2025 [C-connector]; how those names map to the documented tool names is not confirmed.
- Compatible clients listed by monday: Claude, ChatGPT, Cursor, Microsoft Copilot and Copilot Studio, Gemini CLI, Gemini Enterprise, Mistral le Chat, Perplexity, Figma Make; coding tools including Claude Code via remote config [D-mcp-clients].
- A separate local "Apps MCP" exists for building monday marketplace apps; not needed for account builds [D-mcp-overview][D-ai].

### 1.2 Authentication and access control
- Three documented paths [D-mcp-integrate]:
  - OAuth via the hosted connector (default for compatible clients; OAuth 2.0 Authorization Code Grant, monday as IdP) [D-mcp-security]. The "Build with AI" page calls it OAuth 2.1 [D-ai].
  - Personal API token as `Authorization: Bearer <token>` for clients that support headers; token mirrors the user's UI permissions; "not for integrations used by other people" [D-mcp-token].
  - Your own OAuth app: caps the connection with app scopes (for example `boards:read` only), limits who can connect and which client; requires the admin to turn off the hosted connector or users can bypass it; Claude supports this via Settings > Connectors > Add custom connector with Client ID and Secret [D-mcp-oauthapp][D-mcp-claude-app].
  - Publicly distributed MCP clients must use dynamic client registration and submit monday's registration form [D-mcp-clients][D-mcp-integrate].
- Effective permission is the intersection of the user's monday permissions and the OAuth app's scopes [D-mcp-oauthapp].
- Admin controls [S-connectors]:
  - Administration > AI governance > AI permissions > AI Connectors: master toggle "Allow external AI agents to access your monday.com account data"; sub-permissions include separate Microsoft options and "Public Hosted MCP" (Claude, ChatGPT, Cursor, and others).
  - Admin > Apps > monday MCP > Permissions: "All Workspaces" (default, includes future workspaces) or "Specific Workspaces".
  - When disabled or out of scope, the error appears inside the AI client.
- Security posture: MCP is a wrapper over the Platform API; per-user isolation; the server does not store or log OAuth tokens; prompt-injection defence is the client's responsibility; no customer self-service export of MCP or API audit logs [D-mcp-security].

### 1.3 API version used by MCP
- Clients can pin a version with the `Api-Version` header [D-mcp-integrate][D-ai]. The hosted server's default version is not stated in the docs (not confirmed). Whether Claude's directory connector lets you set that header is not documented (not confirmed).
- Newer tools (workflows, automations, agents, asset uploads) run against the dev (preview) schema and "are subject to change" [D-mcp-tools].
- Source: the open-source agent toolkit sets `API_VERSION = '2026-10'` (changed 2026-06-29), and several tools force `versionOverride: 'dev'`, including agents, automations management, asset upload, search, `get_user_context`, `undo_action`, parts of `get_board_items_page`, and form submission [G-version][G-toolkit]. The local npm server `@mondaydotcomorg/monday-api-mcp` defaults to `current` [G-mcp-pkg]. Inference: the hosted server likely tracks the toolkit (2026-10 RC plus dev), but this is not confirmed.

### 1.4 Documented tool list (Platform MCP tools page, "more than 60 tools") [D-mcp-tools]

Boards and items
- `create_board`: create a board in a workspace.
- `get_board_info`: board metadata, columns, groups, views, owners.
- `get_board_items_page`: paginate items with filters, sort, subitems.
- `get_board_activity`: board activity log for a time range.
- `board_insights`: aggregate, filter, group board data.
- `create_group`: add a group.
- `create_column`: add a column with type-specific settings.
- `get_column_type_info`: settings schema or filter/aggregation guidance for a column type.
- `create_item`: create an item, a subitem, or a duplicate.
- `change_item_column_values`: update one or more column values.

Workspaces and organization
- `create_workspace`: create workspace (name, kind, description, optional product ID).
- `update_workspace`: name, kind, description, product association.
- `list_workspaces`: workspaces available to the user.
- `workspace_info`: boards, docs, folders in a workspace.
- `create_folder`, `update_folder`: folders (color, icon, parent, position).
- `move_object`: move a board, folder, or overview (dashboard).

Docs
- `create_doc`: doc in a workspace or on an item's doc column, populated from markdown.
- `update_doc`: ordered operations (rename, append markdown, edit/create/delete/replace blocks, comments).
- `read_docs`: content as markdown plus block structure, or version history.

Dashboards and widgets
- `create_dashboard`: dashboard over one or more boards.
- `create_widget`: widget on a dashboard or board view.
- `all_widgets_schema`: JSON Schema for all widget types.

Views
- `create_view`, `update_view`: board view with filters and sort.
- `create_view_table`, `update_view_table`: table view with column visibility/order and group-by.

Forms (WorkForms)
- `create_form`: form plus backing board; returns form token.
- `get_form`: form by token.
- `update_form`: settings, appearance, password, tags, question order.
- `form_questions_editor`: create/update/delete one question (23 types, conditional visibility) [D-llms].
- `create_form_submission`: submit a response.

Users and teams
- `get_user_context`: current user, account (plan, products), relevant boards and workspaces.
- `list_users_and_teams`: users and teams by ID or name.

Updates and notifications
- `create_update`, `get_updates`: item comments.
- `create_notification`: bell notification, optional email.

Search and assets
- `search`: boards, docs, forms, folders (source adds items, workspaces, updates, timeline items, dashboards) [G-toolkit].
- `get_assets`: file metadata and download URLs.
- `get_asset_upload_url`, `finalize_asset_upload`: two-step upload and attach to an item (dev).

Workflows and automations
- `list_automations`: automations on a board with state and config.
- `manage_automations`: activate, deactivate, delete (dev).
- `create_automation`: board automation from natural language.
- `plan_workflow`: AI plan for workflows for a process.
- `create_workflow`: empty workspace-level workflow (dev).
- `update_workflow`: change a workflow draft from a prompt.
- `publish_workflow`: publish draft to live (dev).

AI agents (all dev)
- `manage_agent`: create, get, update, delete, activate, deactivate, run.
- `manage_agent_triggers`: list/add/remove triggers.
- `manage_agent_skills`: create skills, attach/detach.
- `manage_agent_knowledge`: grant/update/revoke board and doc access.
- `agent_catalog`: available trigger types and skills.

Meetings and monday dev
- `get_notetaker_meetings`: AI Notetaker meetings, summaries, action items.
- `get_monday_dev_sprints_boards`, `get_sprints_metadata`, `get_sprint_summary`: monday dev sprints.

API and schema
- `all_monday_api`: run any GraphQL query or mutation.
- `get_graphql_schema`, `get_type_details`: schema introspection.

UI components (called by the server, not directly): `show_table`, `show_chart`, `show_battery`, `show_assign`; only some clients render them [D-mcp-tools][S-mcp-tools].

### 1.5 Tools present in monday's open-source toolkit but not on the docs page (hosted availability not confirmed)
Source registry [G-toolkit]: `create_items` (max 20 per call), `update_items` (max 40 per call, across boards), `update_column`, `delete_column`, `delete_item`, `move_item_to_group`, `get_board_schema`, `use_template`, `check_template_status`, `add_content_to_doc` (also listed by support [S-mcp-tools]), `delete_update`, `update_assets_on_item`, `fetch_file_content`, `undo_action` (undo via activity-log record), `configure_ai_column`, `remove_ai_from_column`, `get_automation_runs`, `get_automation_statistics`, object-schema tools (`get_object_schemas`, `create_/update_/delete_object_schema`, `manage_object_schema_columns`, `manage_object_schema_board_connection`, `set_object_schema_column_active_state`, `delete_object_schema_columns`), `link_board_items_workflow`, `get_monday_knowledge` (also on the claude.com connector page [C-connector]), `submit_bug_or_feature_request`, Emails & Activities tools (`create_custom_activity`, `fetch_custom_activity`, `create_timeline_item`), `all_api_read` / `all_api_write`, and `manage_tools` (lists tools with an `enabled_by_default` flag and enables others). monday's CRM plugin also calls hyphenated CRM tools on the connector (`get-timeline-items`, `create-timeline-item`, `get-board-sequences`, `enroll-item-in-sequence`, `get-activity-insights`), and its changelog notes `get-board-sequences` had a 100% error rate on the external connector on Jul 7-11 [G-crm-changelog]. Inference: the live tool list can differ from the docs; read it at runtime.

### 1.6 Documented MCP limitations and behaviours
- Tool availability depends on permissions, plan features, and the AI client [S-mcp-tools].
- `create_automation`: needs board ID, trigger, and at least one action; one trigger; conditions optional and ANDed; no branching; may return `needs_clarification`; no public GraphQL equivalent [D-mcp-create-automation].
- `manage_agent`: dev schema; agents are created INACTIVE and must be activated; delete is permanent; `run` is fire-and-forget with no run-status query; no stable public GraphQL [D-mcp-manage-agent][G-toolkit].
- `update_doc` (source): text/code/list blocks update in place; divider, table, image, video, notice box, layout are immutable (replace instead); board, widget, doc embeds, giphy can only be deleted; markdown append cannot insert asset images (use an image block with `asset_id` or public URL); `delete_blocks` takes up to 100 IDs [G-toolkit].
- `get_board_info` (source): call before writes; a column's returned `settings` is not the input shape for `create_column`; use `get_column_type_info` schema mode [G-toolkit].
- `workspace_info` returns up to 100 of each object type (source) [G-toolkit].
- `create_dashboard` accepts at most 50 board IDs; `create_widget` settings must match `all_widgets_schema` (source) [G-toolkit].
- `search` requires a non-empty term; no "list everything" mode (source) [G-toolkit].
- `get_monday_dev_sprints_boards` only scans recently used boards (source) [G-toolkit].
- Multiple monday accounts in one Claude connector: nothing in monday's docs. A Claude Code feature request for multi-account connectors in Cowork was closed as a duplicate [G-cc-issue]. Not confirmed; inference: one connected monday account per Claude user at a time, switch by reconnecting.

---

## 2. Official monday plugins for Claude, and how a consultant plugin should relate

### 2.1 "monday.com" plugin (Cowork)
- Listing: publisher monday.com, Anthropic Verified, installs in Claude Cowork, OAuth; example prompts cover sprint status, project tracker creation, task assignment, weekly summaries, request forms [C-plugin].
- Source: `mondaycom/monday-claude-cowork-plugin`, v0.1.0, single commit 2026-06-01, MIT; referenced from Anthropic's `knowledge-work-plugins` marketplace as `monday-com` [G-cowork][G-kwp].
- Contents [G-cowork]:
  - Connector: `.mcp.json` server key `monday`, type http, `https://mcp.monday.com/mcp`.
  - Skills (auto-activating): `task-management`, `project-status-report`, `board-setup`, `docs-collaborator`, `forms-builder`.
  - No commands, agents, or hooks.
- Good at: everyday item create/update/assign/comment with column formatting; status reports (overdue, blockers, workload); creating a single board from a use-case template; docs with live column-value embeds and mentions; WorkForms intake [G-cowork].
- Guidance it encodes (useful as independent confirmation, do not copy): read board structure before writes; status labels are case-sensitive; stringify column values; scope user lookups by name; never edit a doc block you have not read; forms only create new items; form branding removal needs Pro+; formula columns need Pro+; check board-name collisions; the plugin redirects automation setup to the monday UI [G-cowork].
- Plan table in its README (plugin claim, not verified in support docs): docs capped at 3 on Free/Basic [G-cowork].
- Same five skills are published as Agent Skills: `npx skills add mondaycom/skills` [D-ai][G-skills].

### 2.2 "monday CRM" plugin (Claude Code)
- Listing: monday.com, Anthropic Verified, installs in Claude Code [C-crm-plugin]. In both `claude-plugins-official` and `knowledge-work-plugins` marketplaces, pinned to `mondaycom/mcp` `plugins/monday-crm` [G-cpo][G-kwp].
- v0.5.0 (2026-08-05), `defaultEnabled: false`, same `monday` http connector [G-crm].
- Skills: `activity-insights`, `automate-crm`, `daily-briefing`, `data-cleanup`, `forecast`, `log-activity`, `meeting-to-deal`, `run-sequence`, `workspace-builder` [G-crm].
- Tools are referenced as `mcp__monday__<tool>` in `allowed-tools` [G-crm].
- Documented gotchas: numeric product ID binds a workspace to CRM; CRM boards are ordinary `public` boards at API level (no custom-object board kind) [G-crm-changelog][G-crm-skill].

### 2.3 Complement, do not duplicate (recommendations; inference unless cited)
- Depend on the official connector rather than shipping a different endpoint. Both official plugins point at the same URL with server key `monday` [G-cowork][G-crm]. Whether Cowork merges a plugin-declared server with the directory connector, and what tool-name prefix results, is not confirmed. Prefer discovering available monday tools at runtime over hard-coding a prefix.
- Leave everyday operations (single item edits, quick status reports, simple forms, ad-hoc docs) to the official skills when installed. Own what they do not cover: client lifecycle, discovery, blueprint with approval stop, multi-board architecture with product binding, connect/mirror/formula wiring, dashboards and widgets, views, automations and workflows, build manifest of IDs, read-back verification, SOP and versions.
- Avoid skill-name collisions with the 14 official names above so auto-activation is predictable.
- The official skills and the MCP tool descriptions already carry per-tool mechanics; a consultant plugin can stay short by pointing to live introspection (`get_board_info`, `get_column_type_info`, `all_widgets_schema`, `get_type_details`) plus a short gotcha list (section 6).

---

## 3. Platform API essentials

### 3.1 Versioning
- Names are `YYYY-MM`; a new version each quarter (January, April, July, October); each version stable at least six months; lifecycle Release Candidate > Current > Maintenance > Deprecated (deprecated requests redirect to Maintenance; deprecation announced at least 6 months ahead) [D-versioning].
- Pass `API-Version` header; with no header the Current version is used; the `version` field reports which version served a call [D-versioning].
- Status on 2026-09-10: `2026-04` Maintenance, `2026-07` Current (default), `2026-10` Release Candidate [D-versioning]. Versions before `2025-04` are deprecated [D-release].
- Build-relevant changes [D-release]:
  - `2026-10` (RC): legacy User fields (`is_guest`, `is_admin`, `is_view_only`, photos, etc.) and `users(kind, newest_first, non_active)` removed; WorkForms `update_form_tag` and `showIfRules` removed; new `use_template` + `template_installation_status`, `change_board_kind`, `update_teams_board_role`, `duplicate_view`, `restore_view`, `create_board(use_mls_template, use_dataset_template)`, `create_board_export` (Enterprise), `search.users/updates/timeline_items`, `run_prompt`.
  - `2026-07` (Current): User overhaul; `users` without `limit` returns 200, max `limit` 1000; `connection_board_ids(connection_id)` rename; `Board.columns(capabilities)` has no default; new `search.workspaces`, `job_status`, validation-rule mutations, `create_doc_blocks`; WorkForms question additions (`HOUR`, `DISPLAY_TEXT`, `PAGE_BLOCK`, `show_if_rules`); bulk import (`ingest_items`, `backfill_items`) is 2026-07+ [D-bulk].
  - `2026-04`: `create_project`, `set_item_description_content`, `search`, doc version history/diff, `notetaker`, `object_relations`, `create_board(prompt)`, `workspaces(query_params: account_product_kind)`, `APP_FEATURE` and `LISTVIEW` widgets.
- Also available: an `Idempotency-Key` header for safe mutation retries (page listed, details not fetched) [D-llms].

### 3.2 Limits
- Complexity per minute: personal tokens 10M points combined read+write (1M on trial/free); app tokens 5M read and 5M write; per-query cap 5M; query `complexity` to monitor [D-rate].
- Daily calls (reset midnight UTC): Free/Basic/Standard 1,000; Pro 10,000; Enterprise 25,000; MCP calls count; rate-limit errors and complexity-only queries count 0.1 [D-rate][D-mcp-overview].
- Minute rate: Enterprise 5,000, Pro 2,500, others 1,000 queries per minute [D-rate].
- Concurrency: Enterprise 250, Pro 100, others 40 [D-rate].
- IP: 5,000 requests per 10 seconds (`IP_RATE_LIMIT_EXCEEDED`) [D-rate].
- Mutation-specific: `create_board` and `duplicate_board` 40 per minute; `duplicate_group` 40 per minute; portfolio connection 15 per minute; formula `display_value` 10,000 per minute and max 5 formula columns per request [D-rate][D-boards][D-groups][D-formula].
- Bulk import: 19,000 item creates/updates per account per hour for `ingest_items`; 100 jobs per hour [D-bulk]. Template status polling: about 60 requests per minute per account [D-templates].
- Errors: `ComplexityException`, `DAILY_LIMIT_EXCEEDED`, minute and concurrency errors, all with `retry_in_seconds`; headers `RateLimit-Policy` and `RateLimit` [D-rate]. Application errors return HTTP 200 with an `errors` array and possibly partial `data`; each response has `request_id` [D-errors].
- Common error codes worth handling: `ColumnValueException`, `InvalidColumnIdException`, `ItemNameTooLongException` (1-255 chars), `missingRequiredPermissions` (OAuth scope), `UserUnauthorizedException`, `USER_ACCESS_DENIED` (inactive, view-only, or unconfirmed email), `DeleteLastGroupException` (409) [D-errors]. `ItemsLimitationException` cites 10,000 items per board [D-errors] while Enterprise mondayDB 2.0 allows 100K [S-mondaydb] (plan-dependent; exact non-Enterprise cap not confirmed).

### 3.3 Pagination
- `items_page` (nested in `boards` or `groups`): `limit` default 25, max 500; returns `cursor` (null when done); cannot combine `cursor` and `query_params` in one call; returns active items only [D-itemspage].
- `next_items_page(cursor, limit)` at root; cursors expire 60 minutes after the first request [D-nextpage].
- `items(ids)`: up to 100 IDs; use `state` for archived/deleted [D-itemspage].
- `boards`, `workspaces`, `docs`: `page` (starts at 1) and `limit` (default 25) [D-boards][D-workspaces][D-docs].
- `users`: 200 by default without `limit`, max 1000 (2026-07+) [D-release].

---

## 4. Build capabilities and documented limitations

### 4.1 Workspaces and product binding
- `create_workspace(name, kind: open|closed, description, account_product_id)`; `update_workspace(id, attributes{name, description, account_product_id})`; add/remove users and teams as owner or subscriber; `delete_workspace` [D-workspaces][D-users].
- Kinds: query enum `open`, `closed`, `template`; create mutation lists `open`, `closed`; MCP page lists `open`, `closed`, `template` [D-workspaces][D-mcp-create-workspace]. Closed workspaces are Enterprise [S-workspaces].
- Main workspace: cannot be deleted, have members removed, or change type [S-workspaces]; may not be queryable until a multi-product migration finishes (pre-migration ID `null`/`-1`) [D-workspaces].
- Products on the account: `account { products { id kind tier } }`; `plan` returns null on multi-product accounts [D-account]. `workspaces(query_params: {account_product_kind})` (2026-04+) accepts `core`, `crm`, `forms`, `marketing`, `project_management`, `service`, `software`, `whiteboard` [D-workspaces].
- Binding: pass the numeric product ID when creating, or move later via `update_workspace`, `update_board_hierarchy(account_product_id)`, `update_overview_hierarchy(account_product_id)`, or MCP `move_object(accountProductId)` [D-workspaces][D-boards][D-dash-types][G-toolkit]. The string kind does not bind (monday CRM plugin) [G-crm-changelog].
- Moving content between products (UI rules) [S-move-products]: product core boards cannot move (CRM: Leads, Deals, Contacts, Accounts, Activities; dev: Tasks, Sprints, Epics, Bugs Queue); whole workspaces can move; connect and mirror columns keep working; move connected boards together in one folder; users who are not members of the destination product become view-only there.

### 4.2 Folders
- MCP `create_folder` (color, icon, font weight, parent) and `update_folder` (name, color, icon, position, parent) [D-llms]. GraphQL folder reference not fetched (argument details not confirmed).
- UI limits: up to 2 layers of subfolders (3 levels total); deleting a folder archives its boards and deletes its dashboards [S-folders].

### 4.3 Boards and board kinds
- `create_board` arguments: `board_name`, `board_kind` (`public` main, `private`, `share` shareable), `workspace_id`, `folder_id`, `description`, owner and subscriber user/team IDs, `empty` (no default items), `item_nickname`, `template_id`, `prompt` (AI structure, 2026-04+), `use_mls_template` and `use_dataset_template` (2026-10+). Creator becomes owner for private/shareable boards or when no owners are given [D-boards].
- Other board mutations: `duplicate_board` (structure; structure+items; structure+items+updates; async, may return partial data), `update_board` (name, description, communication, item_nickname), `update_board_hierarchy` (workspace, folder, product, position), `archive_board`, `delete_board`, `change_board_kind` (2026-10+), `set_board_permission` (Enterprise board owners; contributor/editor/viewer), `update_teams_board_role` (2026-10+, max 50 teams), `create_board_export` (Enterprise, 2026-10+) [D-boards].
- `boards` query hierarchy: the boards page says omitted `hierarchy_types` returns only classic boards unless IDs are given [D-boards]; the multi-level guide says 2026-04+ returns both by default [D-mlb]. Conflict; pass `hierarchy_types` explicitly.
- Plan gates: private boards Pro+; shareable boards and guests Standard+; Free plan 2 seats, 3 boards, 200 items [S-plans][S-guest].
- Scale (Enterprise, mondayDB 2.0): 100K items and 100K connected items per board, 500K items per dashboard; 60 connected boards per board (portfolio 200); with these limits, duplicating a board with values, auto number column, and changing column type are unsupported [S-mondaydb].
- Templates: `use_template(template_id, destination_workspace_id, destination_folder_id/name, destination_name, board_kind, owners, callback_url_on_complete)` runs as a background job; poll `template_installation_status(process_id)` every 2-5 seconds; boards are empty shells while IN_PROGRESS; no public query lists templates, get the ID from the Template Center URL; 2026-10+ [D-templates].
- Projects and portfolios: projects on Pro and Enterprise; portfolio connection Enterprise only; converting a board to a project cannot be undone [S-board-vs-project][S-portfolio]. API has `create_portfolio` (async `callback_url`, 2026-07), `create_project` (2026-04), project-to-portfolio connection (15/min) [D-release][D-rate]; portfolio "agent skill" guides exist [D-llms].
- Multi-level boards: up to 5 levels of subitems on the same board ID, shared columns, rollup capability on numbers/date/timeline/status; initially project boards in the portfolio solution [D-mlb].

### 4.4 Groups
- `create_group(board_id, group_name ≤255, group_color hex, relative_to, position_relative_method)`; `position` deprecated [D-groups].
- `update_group` attributes: `title`, `color`, `position`, `relative_position_after`, `relative_position_before`; `duplicate_group` (40/min); `archive_group`; `delete_group` (deleting the last group fails) [D-groups][D-errors].
- New boards come with default content unless `empty: true` [D-boards]; monday's own plugin removes the default `topics` group after creating its groups [G-cowork].

### 4.5 Columns and value formats
- `create_column(board_id, title, column_type, description, defaults JSON, id, after_column_id, capabilities)`; `defaults` is validated against `get_column_type_schema(type)`; custom `id` is 1-20 chars, lowercase letters and underscores, unique, never reusable even after deletion [D-columns].
- `update_column` requires the column `revision` (optimistic concurrency) and can set `settings`, `title`, `description`, `width`; also `change_column_title`, `change_column_metadata`, `delete_column`; typed `create_status_column` and `create_dropdown_column` exist [D-columns][D-coltypes].
- Writes: `change_simple_column_value` (string), `change_column_value` (JSON), `change_multiple_column_values` (JSON map, simple and JSON mixed, e.g. `{"text":"x","status":{"label":"Done"}}` or `"status":"Done"`); `create_labels_if_missing` needs structure-edit permission [D-columns].
- Writable types: button, checkbox, color_picker, board_relation, country, date, dependency, dropdown, email, file, hour, link, location, long_text, doc, name, numbers, people, phone, rating, status, subtasks, tags, text, timeline, time_tracking, vote, week, world_clock [D-coltypes].
- Read-only: creation_log, formula, item_id, last_updated, mirror, progress. Not in `column_values`: auto_number. Deprecated: person, team (use people). No direct support: integration [D-coltypes].
- Reading: use inline fragments per value type; `settings_str` deprecated since 2025-10, use typed `settings` [D-coltypes][D-connect].
- Filtering: `items_page(query_params.rules)` with per-type operators; people by `person-<id>` with `any_of` [D-itemspage].
- Per-type value formats live on each column's reference page; MCP `get_column_type_info` returns the schema [D-coltypes][D-mcp-tools]. Inference: introspect per board rather than keeping a static manual.

### 4.6 Board relations and mirror columns
- Connect boards (`board_relation`): create with `defaults {boardIds:[...], allowMultipleItems (default true), allowCreateReflectionColumn (default false, creates the reverse column on the target board)}`; link items with `change_multiple_column_values` `{"col":{"item_ids":[...]}}` or in `create_item`; clear with `null`; `change_simple_column_value` not supported; the column must already have `boardIds` configured; `text`/`value` return null, use `display_value`, `linked_item_ids`, `linked_items`; `connection_board_ids(connection_id)` [D-connect][D-errors].
- Mirror: create with `defaults {"settings":{"relation_column":{"<connect_col_id>":true},"displayed_linked_columns":[{"board_id":"...","column_ids":["..."]}]}}`, optional `sumType` (status: `doneOnly`/`allStatuses`) and `calcType` (date: `earliestToLatest`/`earliest`/`latest`); read only, no filter, update, or clear; `text`/`value` null, use `display_value` or `mirrored_items` [D-mirror].
- Dashboards can use connect and mirror columns in widgets [S-dashboards].
- Cross Account Copier hides a connect column when its linked board is not copied along [S-copier].

### 4.7 Formula columns
- Create via `create_column(column_type: formula, defaults: {"settings":{"formula":"{col_a} * {col_b}"}})`; references use column IDs; empty formula means manual setup in the UI [D-formula].
- Cannot update or clear; cannot filter; read via `FormulaValue.display_value` with limits (10,000/min, 5 columns per request, not for formulas referencing mirror or connect columns) [D-formula].
- Plan: formula and time tracking are not available on Free/Basic; full column center on Pro [S-plans].

### 4.8 Subitems
- Classic boards: subitems live on a hidden subitems board with its own board ID and columns [D-mlb]. `create_subitem(parent_item_id, item_name, column_values, create_labels_if_missing)` [D-subitems]; MCP `create_item` accepts a parent for subitems [D-mcp-tools].
- Multi-level boards: same board ID for all levels, up to 5 deep; rollups (numbers SUM/MIN/MAX, date MIN/MAX, timeline MIN_MAX, status COUNT_KEYS returned as `BatteryValue`); pass `capabilities: [CALCULATED]` to read rollups; creating the first subitem copies or clears parent rollup values [D-mlb][D-subitems].
- Items cannot be converted to subitems and subitems cannot be repositioned with `change_item_position` [D-items]. Webhooks for subitem events use the parent board ID [D-webhooks].

### 4.9 Items: single and bulk
- `create_item(board_id, item_name, group_id, column_values JSON string, create_labels_if_missing, position_relative_method, relative_to)` [D-items].
- Also: `duplicate_item(with_updates)` (updates copied asynchronously), `change_item_position`, `set_item_description_content` (markdown, 2026-04+, loses text colors), `update_assets_on_item`, `move_item_to_group`, `move_item_to_board` (if `columns_mapping` is given, map every column; formula columns cannot be mapped), `archive_item`, `clear_item_updates`, `delete_item` [D-items].
- Bulk (2026-07+) [D-bulk]:
  - `ingest_items`: CSV upload to a pre-signed URL (valid 10 minutes), max 10,000 rows, 150 MB, optional UPSERT via `on_match` on a column, counts toward 19,000 items/account/hour.
  - `backfill_items`: account admin only, max 20,000 rows, create-only, does not trigger automations or write the activity log; intended for one-time initial loads.
  - Poll `fetch_job_status`; 100 jobs per hour shared; CSV header `name` first then exact column IDs; supported columns: board relation, checkbox, date, dropdown, email, link, location, long text, number, people, phone, status, text, timeline.
- MCP batch (source): `create_items` up to 20 per call, `update_items` up to 40 per call; later entries are skipped after a minute-rate-limit hit [G-toolkit].

### 4.10 Views
- Read: `boards { views { id name type settings filter sort tags access_level } }` [D-views].
- `create_view(board_id, type, name, filter, sort, settings, tags, filter_user_id/team_id)` with `type` in `APP`, `DASHBOARD`, `FORM`, `TABLE`; `create_view_table` and `update_view_table` with `TableViewSettingsInput` (column visibility, order, group-by); `update_view`, `delete_view`; `duplicate_view` and `restore_view` 2026-10+; `get_view_schema_by_type` [D-views].
- Kanban, Gantt, Calendar, Timeline, Chart, Map view kinds appear only in the dev schema used by monday's toolkit (source) [G-schema]; not documented, not confirmed usable.

### 4.11 Forms (WorkForms)
- `create_form(destination_workspace_id, destination_folder_id or name, destination_name for the backing board, board_kind, owners, subscribers)` returns a token; `form(formToken)` query requires access to the backing board; GraphQL mutations seen: `create_form_question`, `update_form_question`, `create_form_tag` (tag update removed in 2026-10), `activate_form`, `update_form` (title, description, question order), `update_form_settings` [D-form][D-release]. Question delete, deactivation, password and branding are handled by MCP `form_questions_editor` and `update_form` actions [D-mcp-tools][G-toolkit]; their GraphQL mutation names were not fetched (not confirmed).
- Token is the string after `/forms/` in the share URL [D-form].
- Question types (source): Boolean, ConnectedBoards, Country, DisplayText, Date, DateRange, Email, File, Hour, Link, Location, LongText, MultiSelect, Name, Number, PageBlock, People, Phone, Rating, ShortText, Signature, SingleSelect, Subitems, Updates; conditional `show_if_rules` [G-toolkit][D-release].
- Forms only create new items (monday plugin guidance) [G-cowork]. Branding removal Pro+ [G-cowork].

### 4.12 Docs
- `docs` query by `ids` (internal) or `object_ids` (the ID in the URL), `workspace_ids`, `page`/`limit` [D-docs].
- `create_doc(location: workspace {workspace_id, name, kind} | doc column on an item)`; `add_content_to_doc_from_markdown(docId, markdown, afterBlockId)` returns `block_ids`; `import_doc_from_html(workspaceId, html, title, folderId, kind)` supports formatted text, emoji, quote, table, list, code, divider, titles; `update_doc_name`, `duplicate_doc`, `delete_doc`; `doc_version_history` and `doc_version_diff` (2026-04+); `export_markdown_from_doc` [D-docs][D-llms].
- Blocks: CRUD plus `create_doc_blocks` (2026-07+); table blocks max 5 columns by 5 rows, fixed after creation [D-blocks][D-release].
- Images: via image blocks with an asset ID or public URL; markdown append does not take asset images (source) [G-toolkit]. Assets upload through the two-step MCP upload tools (dev) [D-mcp-tools].
- Doc kinds main, private, shareable; private docs cannot include guests [S-workdocs].
- MCP `create_doc` creates then appends markdown; `update_doc` operations listed in 1.6 [G-toolkit].

### 4.13 Dashboards and widgets
- `create_dashboard(name ≤255, workspace_id, board_ids, board_folder_id, kind PRIVATE default | PUBLIC)`; `update_dashboard`; `update_overview_hierarchy` (workspace, folder, product, left-pane position); `delete_dashboard` [D-dash][D-dash-types].
- `create_widget(parent {kind: DASHBOARD | BOARD_VIEW, id}, kind, name, settings JSON, filter)`; `filter` only works on board-view widgets; settings shape from `all_widgets_schema`; `delete_widget` [D-dash].
- Documented widget kinds: `APP_FEATURE`, `BATTERY`, `CHART`, `LISTVIEW`, `NUMBER` [D-dash-types]. The toolkit's generated schema also lists `CALENDAR` and `GANTT`, and the dev schema adds more (source) [G-schema]; not confirmed.
- Reading back: dashboard types are "not independently queryable"; no documented dashboards or widgets query [D-dash-types]. The dev schema has `overviews` (id, name, kind, folder, workspace; no widgets) and `load_dashboard_data(dashboard_id)` (source) [G-schema]; MCP `search` can find dashboards (source) [G-toolkit]. Inference: verify dashboards by recording IDs at creation time, not by reading widgets back.
- Layout: no documented argument for widget position or size (not confirmed).
- Limits: connected boards per dashboard Free 1, Basic 1, Standard 5, Pro 20, Enterprise 50; up to 30 widgets (text widgets excluded); 20,000 items across connected boards; dashboards can be deleted but not archived [S-dashboards][S-plans].

### 4.14 Automations and workflows
- Board automations via MCP: `list_automations`, `manage_automations` (activate, deactivate, delete), `create_automation` (natural language, rules in 1.6); no public GraphQL for creation [D-mcp-tools][D-mcp-create-automation]. The current schema includes a `board_automations` query (source) [G-schema][D-mcp-tools]. Toolkit also has `get_automation_runs` and `get_automation_statistics` (source) [G-toolkit].
- Workflows (workspace level, cross-board): `plan_workflow`, `create_workflow` (returns object ID and draft ID), `update_workflow` (AI prompt), `publish_workflow` [D-mcp-tools][D-llms]. AI workflow builder is Pro and Enterprise; workflows can span workspaces and products; they are copied with workspace templates [S-workflows].
- Monthly action quotas (automations and integrations counted separately): Standard 250 each, Pro 25,000 each, Enterprise 250,000 each; condition steps and per-recipient notifications consume actions; custom templates count as automation actions; only Enterprise can buy more; when exhausted the account cannot edit or add automations, and overage is deducted from the next month [S-automation-limits][S-plans]. Inference: Free and Basic have no automation quota (the Standard section introduces it) [S-plans].

### 4.15 Webhooks
- `create_webhook(board_id, url ≤255 chars, event, config)`; events: `change_column_value`, `change_status_column_value`, `change_subitem_column_value`, `change_specific_column_value` (config `{"columnId":...}`, not for subitem columns), `change_name`, `create_item`, `item_archived`, `item_deleted`, `item_moved_to_any_group`, `item_moved_to_specific_group`, `item_restored`, `create_subitem`, `change_subitem_name`, `move_subitem`, `subitem_archived`, `subitem_deleted`, `create_column`, `create_update`, `edit_update`, `delete_update`, `create_subitem_update` [D-webhooks].
- URL must echo the `challenge`; JWT signing and non-removable webhooks only when created with an integration app token; retries once a minute for 30 minutes; `webhooks(board_id)` query [D-webhooks]. Delete mutation not fetched (not confirmed here).

### 4.16 Users, teams, permissions
- User types: admin; member; viewer (read-only, cannot use the API, unlimited and free); guest (external domain only; only invited shareable boards; can use the API, add columns, views, automations; cannot create boards or be board owner); product non-member; custom roles Enterprise [S-user-types][S-guest].
- Guests: Standard+; Standard includes 3 free guests then 4 guests per seat; unlimited on Pro and Enterprise [S-guest].
- API: `add_users_to_board` (owner/subscriber), `add_users_to_team`, `add_users_to_workspace`, `invite_users(emails, product, user_role GUEST|MEMBER|VIEW_ONLY)`, `activate_users` (≤200), `deactivate_users` (admin only, ≤200; also deactivates that user's integrations and automations), `update_users_role` (admin only, ≤200, not self), `update_multiple_users`, `delete_subscribers_from_board`, `remove_users_from_team`, `delete_users_from_workspace` [D-users].
- `invite_users` product enum: `crm`, `dev`, `forms`, `knowledge`, `service`, `whiteboard`, `workflows`, `work_management` [D-users].
- Token permissions mirror UI permissions; app tokens are limited by scopes [D-auth].

### 4.17 Products and native boards
- Products: monday AI work platform (formerly Work Management), monday CRM, monday dev, monday service [S-move-products]; the official plugin also names campaigns [G-cowork].
- Native core boards (cannot move products): CRM Leads, Deals, Contacts, Accounts, Activities; dev Tasks, Sprints, Epics, Bugs Queue [S-move-products]. Service ships a Tickets board with groups Unassigned tickets, Open tickets, Waiting for response, Resolved tickets [S-service-tickets].
- Creating a product's native boards through the API is not documented (not confirmed). monday's CRM plugin builds CRM boards as ordinary public boards inside a CRM-bound workspace [G-crm-skill].
- Portfolio solution is Enterprise; creating a project from a portfolio also creates a Resource planner by default; only Enterprise project boards can join a portfolio [S-portfolio].
- Object schemas (account-level schemas that define board structure and connect boards) have API and MCP tools; details not fetched [D-llms][G-toolkit].

### 4.18 monday AI agents
- AI agents live in an "AI Agents" tab; builder tabs Brain (instructions, knowledge and access, tools, skills, model), Jobs (per-task trigger and instructions), Channels (e.g. WhatsApp, Telegram), Activity; consume AI credits; available on the AI work platform, other products "coming soon" [S-agents][S-agent-build].
- API: dev schema only; MCP `manage_agent` and related tools; no stable public GraphQL [D-mcp-manage-agent].
- Bring Your Own Agent (beta) connects external agents, including Anthropic Claude Managed Agents; needs the admin "External agents" AI permission [S-byoa][D-ai].

---

## 5. Building via API or MCP on behalf of clients

- Identity: all MCP actions appear as the user who authorized them and are limited to that user's permissions [D-mcp-integrate][S-connectors]. No documented partner or delegated-admin mode for MCP or API (not confirmed).
- Seat choice:
  - Guest: cannot create boards; MCP for guests only if an Enterprise admin enables it [S-guest][S-connectors]. Not viable for building.
  - Viewer: no API or MCP [S-user-types][S-connectors].
  - Member or admin in the client account: can build; some actions need admin (`backfill_items`, user role changes, deactivation) [D-bulk][D-users]. Inference: billable seat cost falls on the client.
- Client-admin checklist before a build [S-connectors]: AI Connectors master toggle on; "Public Hosted MCP" checked; monday MCP workspace scope set to "All Workspaces", or the target workspaces added under "Specific Workspaces" (inference: a newly created workspace may fall outside a specific-workspace scope).
- Tighter control option: the client admin creates an OAuth app with limited scopes and shares its credentials only with the consultant, after turning off the hosted connector [D-mcp-oauthapp][D-mcp-claude-app]. Tradeoff: every other user in the account then loses the one-click connector.
- Multiple client accounts: no monday guidance; see 1.6 (not confirmed). Inference: reconnect the connector per client and confirm the account at session start with `get_user_context`.
- Ownership: board creator becomes owner by default [D-boards]; deactivating a user deactivates the automations and integrations they created [D-users]. Inference: assign client owners at creation and hand automations to a client user before offboarding.
- Plan-driven limits live in the client's account: daily API calls (Standard 1,000), action quotas, dashboard board caps, private boards, formula, portfolio, closed workspaces, board permissions, exports [D-rate][S-automation-limits][S-dashboards][S-plans].
- Moving a build between accounts: Cross Account Copier requires admin on both accounts with the same email, main boards and dashboards inside a folder, no US-EU copy, connected boards in the same folder, automations one board at a time [S-copier].
- Partner program: partners can create client accounts with trial extensions; partner demo accounts are not admin [P-partners].
- Free developer sandbox accounts exist for testing [D-llms].
- Audit: no customer self-service MCP audit export [D-mcp-security]; board and user activity logs are queryable [D-llms][D-release].

---

## 6. Short gotcha list the API cannot reveal on its own

1. Use `/mcp`, not `/sse` [D-mcp-clients].
2. Bind workspaces to a product with the numeric product ID from `account.products` [G-crm-changelog][D-account].
3. Only TABLE, APP, DASHBOARD, FORM views are documented [D-views].
4. Dashboards and widgets cannot be read back or laid out via documented API [D-dash-types].
5. Connect column must have `boardIds` before linking; write it with `change_multiple_column_values` [D-connect].
6. Mirror and formula are read-only; formula `display_value` ignores mirror/connect references [D-mirror][D-formula].
7. Custom column IDs are permanent and never reusable [D-columns].
8. `create_board` and `duplicate_board` are limited to 40 per minute [D-boards].
9. New boards include default content unless `empty: true` [D-boards].
10. Forms create items only; `update_form_tag` is gone in 2026-10 [G-cowork][D-release].
11. Doc blocks such as tables, images, layouts are immutable; tables cap at 5x5 [G-toolkit][D-blocks].
12. Template IDs come from the Template Center URL; install is async [D-templates].
13. `create_automation` has no branching and may ask for clarification [D-mcp-create-automation].
14. Plan gates: private boards Pro, formula Pro, guests Standard, workflows Pro, portfolio Enterprise, closed workspaces Enterprise, `set_board_permission` Enterprise [S-plans][S-guest][S-workflows][S-portfolio][S-workspaces][D-boards].
15. `items_page` cursors expire after 60 minutes [D-nextpage].
16. `boards` default hierarchy filter is documented inconsistently; pass `hierarchy_types` [D-boards][D-mlb].
17. Deactivating the builder's user deactivates their automations and integrations [D-users].

---

## 7. Conflicts and unconfirmed points

- `/sse` shown in a support article vs deprecated in developer docs [S-claude][D-mcp-clients].
- "Admins must install the MCP app" vs "preinstalled" [M-mcp][S-connectors].
- Hosted MCP default API version not documented; toolkit uses 2026-10 plus dev [G-version].
- Tools in the toolkit source vs docs list; hosted availability not confirmed [G-toolkit][D-mcp-tools].
- `boards` default hierarchy behaviour conflicts [D-boards][D-mlb].
- Items-per-board cap: 10,000 in error docs vs 100K Enterprise [D-errors][S-mondaydb].
- Workspace kind `template` on create: MCP page yes, GraphQL create enum no [D-mcp-create-workspace][D-workspaces].
- Dashboard read-back, widget layout, non-table view kinds, native product board creation, folder GraphQL details, webhook deletion: not documented or not fetched.
- Multi-account connectors in Claude: no official monday statement [G-cc-issue].
- Docs cap of 3 on Free/Basic appears only in the official plugin README [G-cowork].

---

## Sources

Developer docs (developer.monday.com)
- D-llms: https://developer.monday.com/api-reference/llms.txt
- D-mcp-overview: https://developer.monday.com/api-reference/docs/mondaycom-mcp
- D-mcp-integrate: https://developer.monday.com/api-reference/docs/integrate-with-monday-mcp
- D-mcp-clients: https://developer.monday.com/api-reference/docs/compatible-mcp-clients
- D-mcp-token: https://developer.monday.com/api-reference/docs/mcp-api-token
- D-mcp-oauthapp: https://developer.monday.com/api-reference/docs/control-mcp-access-with-oauth-app
- D-mcp-claude-app: https://developer.monday.com/api-reference/docs/integrating-monday-mcp-with-claude-custom-app
- D-mcp-tools: https://developer.monday.com/api-reference/docs/platform-mcp-tools
- D-mcp-security: https://developer.monday.com/api-reference/docs/monday-mcp-security-overview
- D-mcp-create-workspace: https://developer.monday.com/api-reference/docs/create-workspace
- D-mcp-create-automation: https://developer.monday.com/api-reference/docs/create-automation
- D-mcp-manage-agent: https://developer.monday.com/api-reference/docs/manage-agent
- D-ai: https://developer.monday.com/api-reference/docs/build-on-monday-with-ai
- D-auth: https://developer.monday.com/api-reference/docs/authentication
- D-versioning: https://developer.monday.com/api-reference/docs/api-versioning
- D-release: https://developer.monday.com/api-reference/docs/release-notes
- D-rate: https://developer.monday.com/api-reference/docs/rate-limits
- D-errors: https://developer.monday.com/api-reference/docs/error-handling
- D-bulk: https://developer.monday.com/api-reference/docs/importing-items-in-bulk
- D-mlb: https://developer.monday.com/api-reference/docs/working-with-multi-level-boards
- D-workspaces: https://developer.monday.com/api-reference/reference/workspaces
- D-account: https://developer.monday.com/api-reference/reference/account
- D-boards: https://developer.monday.com/api-reference/reference/boards
- D-groups: https://developer.monday.com/api-reference/reference/groups
- D-columns: https://developer.monday.com/api-reference/reference/columns
- D-coltypes: https://developer.monday.com/api-reference/reference/column-types-reference
- D-connect: https://developer.monday.com/api-reference/reference/connect
- D-mirror: https://developer.monday.com/api-reference/reference/mirror
- D-formula: https://developer.monday.com/api-reference/reference/formula
- D-subitems: https://developer.monday.com/api-reference/reference/subitems
- D-items: https://developer.monday.com/api-reference/reference/items
- D-itemspage: https://developer.monday.com/api-reference/reference/items-page
- D-nextpage: https://developer.monday.com/api-reference/reference/next-items-page
- D-views: https://developer.monday.com/api-reference/reference/board-views
- D-form: https://developer.monday.com/api-reference/reference/form
- D-docs: https://developer.monday.com/api-reference/reference/docs
- D-blocks: https://developer.monday.com/api-reference/reference/blocks
- D-dash: https://developer.monday.com/api-reference/reference/dashboards-and-widgets
- D-dash-types: https://developer.monday.com/api-reference/reference/dashboards-and-widgets-other-types
- D-webhooks: https://developer.monday.com/api-reference/reference/webhooks
- D-users: https://developer.monday.com/api-reference/reference/users
- D-templates: https://developer.monday.com/api-reference/reference/templates

Support (support.monday.com)
- S-connectors: https://support.monday.com/hc/en-us/articles/35696101067154-Managing-AI-Connectors-and-MCP-Access
- S-claude: https://support.monday.com/hc/en-us/articles/28515704603666-Connect-monday-MCP-with-Claude
- S-mcp-start: https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP
- S-mcp-tools: https://support.monday.com/hc/en-us/articles/32364501317906-monday-MCP-available-tools
- S-move-products: https://support.monday.com/hc/en-us/articles/5379956206866-How-to-move-content-between-products
- S-user-types: https://support.monday.com/hc/en-us/articles/360002144900-User-types-explained
- S-guest: https://support.monday.com/hc/en-us/articles/115005340405-How-to-get-started-as-a-guest
- S-dashboards: https://support.monday.com/hc/en-us/articles/360002187819-The-Dashboards
- S-automation-limits: https://support.monday.com/hc/en-us/articles/360017556179-Automation-and-Integration-actions-and-limits
- S-plans: https://support.monday.com/hc/en-us/articles/115005320209-Available-plan-types-on-Work-Management
- S-workflows: https://support.monday.com/hc/en-us/articles/11378232387730-The-AI-workflow-builder-FAQs
- S-agents: https://support.monday.com/hc/en-us/articles/33347027353746-AI-Agents-on-monday-com
- S-agent-build: https://support.monday.com/hc/en-us/articles/38411699315346-Build-and-configure-your-AI-agent
- S-byoa: https://support.monday.com/hc/en-us/articles/36885999990930-Bring-your-external-agent-into-monday-com
- S-board-vs-project: https://support.monday.com/hc/en-us/articles/25575124855954-Board-vs-project-what-s-the-difference
- S-portfolio: https://support.monday.com/hc/en-us/articles/13337066797202-The-portfolio-solution
- S-mondaydb: https://support.monday.com/hc/en-us/articles/20705455822354-mondayDB-2-0
- S-copier: https://support.monday.com/hc/en-us/articles/360007913040-How-to-copy-boards-and-dashboards-between-accounts
- S-service-tickets: https://support.monday.com/hc/en-us/articles/17344652945810-Managing-tickets-with-monday-service
- S-workspaces: https://support.monday.com/hc/en-us/articles/360010785460-Getting-started-with-workspaces
- S-folders: https://support.monday.com/hc/en-us/articles/115005316845-Folders
- S-workdocs: https://support.monday.com/hc/en-us/articles/360021702939-monday-workdocs

Claude listings
- C-plugin: https://claude.com/plugins/monday-com
- C-crm-plugin: https://claude.com/plugins/monday-crm
- C-connector: https://claude.com/connectors/monday

monday and Anthropic GitHub
- G-cowork: https://github.com/mondaycom/monday-claude-cowork-plugin
- G-skills: https://github.com/mondaycom/skills
- G-mcp-pkg: https://github.com/mondaycom/mcp/tree/master/packages/monday-api-mcp
- G-toolkit: https://github.com/mondaycom/mcp/tree/master/packages/agent-toolkit/src/core/tools
- G-version: https://github.com/mondaycom/mcp/blob/master/packages/agent-toolkit/src/utils/version.utils.ts
- G-schema: https://github.com/mondaycom/mcp/tree/master/packages/agent-toolkit/src/monday-graphql
- G-crm: https://github.com/mondaycom/mcp/tree/master/plugins/monday-crm
- G-crm-changelog: https://github.com/mondaycom/mcp/blob/master/plugins/monday-crm/CHANGELOG.md
- G-crm-skill: https://github.com/mondaycom/mcp/blob/master/plugins/monday-crm/skills/workspace-builder/SKILL.md
- G-kwp: https://github.com/anthropics/knowledge-work-plugins/blob/main/.claude-plugin/marketplace.json
- G-cpo: https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json
- G-cc-issue: https://github.com/anthropics/claude-code/issues/27567

Other
- M-mcp: https://monday.com/w/mcp
- P-partners: https://partners.monday.com/authorized-partners/tutorials-faq/
