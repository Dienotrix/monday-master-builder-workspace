# Platform research: Claude plugins for Cowork and Claude Code

Researched 2026-09-10 for "monday Master Builder" (DelOps). Written clean-room, with no input from any earlier plugin.

How to read this file:
- Every claim carries a source key in brackets, for example [CC-PREF]. The Sources table at the end maps each key to its URL.
- [LOCAL] means output of read-only commands on the user's Mac (Claude Code CLI 2.1.174).
- "Not confirmed" means the sources read do not settle the point.
- Section 7 holds design inferences. They are labeled as inferences, not source claims.
- Everything is paraphrased. Field names, keys and numbers are exact.

---

## 0. Top findings

1. **Cowork runs its sessions on Claude Code.** [CC-MANAGED] The claude.com plugin docs point to the Claude Code plugins reference as the technical spec. [PL-OVR] So the Claude Code plugin format applies in Cowork, with the exceptions in section 4.
2. **Cowork ignores `~/.claude` on the Mac.** It loads the skills, plugins and connectors enabled under Customize, which sync through the claude.ai account at session start. [CW-OVR][CC-SKILLS][CC-DESK] Local development with `--plugin-dir` or `claude plugin init` therefore only covers Claude Code.
3. **the user's CLI is about 94 releases behind.** The local CLI is 2.1.174. [LOCAL] The newest changelog entry is 2.1.268, dated 2026-09-10. [CC-CHANGELOG] Several documented features need newer builds (see 5.6). `claude update` exists. [LOCAL]
4. **Shell works differently in Cowork.**
   - Skill `!` shell injection is replaced by a placeholder. [CC-SKILLS]
   - Shell commands run through `mcp__workspace__bash`, and web fetches through `mcp__workspace__web_fetch`.
   - Deny rules on `Bash` or `WebFetch` carry over to those tools. `Bash(...)` allow rules do not. [CC-PERM]
5. **Plugin agents ignore three fields:** `hooks`, `mcpServers` and `permissionMode`. [CC-AGENTS][CC-PREF]
6. **Compaction limits:**
   - Invoked skill bodies are re-attached at up to 5,000 tokens each and 25,000 tokens in total, most recent first. [CC-SKILLS]
   - The skill listing (names and descriptions) is not re-injected at all. [CC-CTX]
7. **No plugin eval command exists.** Neither the docs nor the changelog through 2.1.268 mention one. [CC-CHANGELOG] Anthropic points to the skill-creator plugin for evals and benchmarks. [CC-SKILLS][BLOG-SC]
8. **Cross-surface skill limits are stricter than Claude Code's own.**
   - claude.ai and Cowork uploads require `name` of at most 64 characters, matching the directory, and `description` of at most 1,024 characters. [SK-HOWTO][PF-SKBP]
   - Claude Code only truncates `description` plus `when_to_use` at 1,536 characters. [CC-SKILLS]
9. **Current models overtrigger on emphatic prompts.**
   - Use plain wording and give the reason for a rule. [PF-PROMPT]
   - Opus 5 needs no "verify your work" instructions, but does need explicit length and scope guidance. [PF-OPUS5]
10. **Local Cowork sessions do not get cross-chat memory.** That memory works only in cloud Cowork. [SUP-MEM] Project memory is scoped to one project. [CW-PROJ][SUP-PROJ]

---

## 1. Plugin anatomy

### 1.1 plugin.json (`.claude-plugin/plugin.json`)

- **Required fields**
  - Only `name` is required: kebab-case, no spaces. It namespaces components, as in `/plugin:skill`. [CC-PREF]
  - The manifest itself is optional when components sit in default folders. [CC-PREF] Claude Desktop organization plugins do require it. [CD-EXT]
- **Metadata fields** [CC-PREF]
  - `$schema` (`https://json.schemastore.org/claude-code-plugin-manifest.json`), `displayName`, `version`, `description`, `author{name,email,url}`.
  - `homepage`, `repository`, `license`, `keywords`.
  - `metadata` (free-form; ignored at runtime) and `defaultEnabled` (default `true`).
- **Version precedence**
  - Setting `version` pins the plugin: users get updates only when it changes. [CC-PREF]
  - If `version` is set in both plugin.json and the marketplace entry, plugin.json wins silently. The docs advise setting it in one place only. [CC-PREF][CC-MKT]
  - For `displayName` and `defaultEnabled`, the marketplace entry wins over plugin.json. [CC-PREF]
- **Version resolution order:** plugin.json `version`, then the marketplace entry `version`, then the git commit SHA of the source. [CC-PREF]
  - Omitting `version` everywhere gives commit-SHA versioning, where every commit is an update. [CC-PREF]
  - `claude plugin validate --strict` fails a plugin with no `version`: it is a warning, and `--strict` promotes warnings to errors. [LOCAL]
- **Component path fields** (relative, starting with `./`) [CC-PREF]
  - `skills` adds to the default `skills/` folder.
  - `commands`, `agents`, `outputStyles` and `workflows` replace their default folders.
  - `hooks`, `mcpServers` and `lspServers` merge by their own rules.
  - Experimental: `experimental.themes` and `experimental.monitors`.
- **Other top-level fields:** `userConfig` (1.4), `dependencies` (plugin names, or `{name, version}` with a semver range) and `channels`. [CC-PREF]
- **Unknown fields** are ignored at runtime. `claude plugin validate` reports them as warnings, and `--strict` turns those into errors. [CC-PREF]

### 1.2 Directory conventions

- **Layout rule:** only `plugin.json` goes inside `.claude-plugin/`. Every other folder sits at the plugin root. [CC-PLUG]
- **Components** [CC-PREF][CC-PLUG][CC-AGENTS][CC-MKT]
  - `skills/<name>/SKILL.md`, plus reference files and `scripts/` inside the skill folder.
  - `commands/*.md`: flat skill files. These are legacy; new plugins should use `skills/`.
  - `agents/*.md`: a subfolder becomes part of the scoped ID, for example `my-plugin:review:security`.
  - `hooks/hooks.json`, `.mcp.json`, `.lsp.json` and `monitors/monitors.json`.
  - `bin/`: added to the Bash PATH. It is not allowed in plugins distributed through claude.ai organization settings.
  - `settings.json` (see 1.5), `output-styles/`, and `scripts/` by convention.
- **Single-skill layout:** a plugin with exactly one skill may put `SKILL.md` at the root. Use `skills/` if it may grow. [CC-PLUG]
- **Validator warnings:** a `CLAUDE.md` at the plugin root triggers one. [CC-MKT]
- **Path containment:** paths and symlinks that point outside the plugin root are refused with `path escapes plugin directory`. [CC-PREF] The symlink loophole was closed in 2.1.261. [CC-CHANGELOG]
- **Cache:** marketplace installs are copied to `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`. The previous version is removed after about 14 days. [CC-PREF]
- **Node dependencies** install automatically only when a lockfile is present (`npm ci --ignore-scripts`, 60-second timeout). A failed install does not block the plugin. [CC-PREF]

### 1.3 Variables

- **Plugin variables** [CC-PREF][CC-HOOKS]
  - `${CLAUDE_PLUGIN_ROOT}`: the install directory. It changes on every update.
  - `${CLAUDE_PLUGIN_DATA}`: `~/.claude/plugins/data/<id>/`. It survives updates and is deleted on uninstall from the last scope, unless `--keep-data` is passed.
  - `${CLAUDE_PROJECT_DIR}`: the project root.
- **Where they are substituted** [CC-PREF]
  - Skill and agent content, and hook and monitor commands.
  - MCP stdio `command`/`args`/`env`, and remote `url`/`headers`.
  - LSP fields.
  - They are also exported as environment variables to hooks and to MCP and LSP subprocesses.
- **Skill-only substitutions:** `$ARGUMENTS`, `$ARGUMENTS[N]` or `$N`, `$name` (from the `arguments` field), `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}` and `${CLAUDE_SKILL_DIR}`. [CC-SKILLS]

### 1.4 User configuration (`userConfig`)

- **Per-key schema:** `type` (`string|number|boolean|directory|file`), `title` and `description`, plus optional `sensitive`, `required`, `default`, `multiple` and `min`/`max`. [CC-PREF]
- **How values are used**
  - Non-sensitive values can be substituted as `${user_config.KEY}` in skills, agents, MCP and LSP config, and hook commands. [CC-PREF]
  - All values reach hooks as `CLAUDE_PLUGIN_OPTION_<KEY>` environment variables. [CC-PREF]
  - Substitution is rejected in shell-form hook commands and in monitors. [CC-PREF]
- **Storage** [CC-PREF]
  - Non-sensitive values: `pluginConfigs` in `~/.claude/settings.json`.
  - Sensitive values: the macOS Keychain.
  - Project settings are ignored.
- **How to set values:** the `/plugin configure` flow, or `claude plugin install --config key=value`. [LOCAL]
- **Cowork:** support for user-installed plugins is not confirmed. For Claude Desktop organization plugins, a local MCP entry that references `${user_config.*}` is skipped, because per-user settings are not available there. [CD-EXT]

### 1.5 Plugin `settings.json`

- Only the `agent` and `subagentStatusLine` keys are supported. `agent` makes one of the plugin's agents the main thread. Unknown keys are ignored. [CC-PLUG]
- Behavior in Cowork: not confirmed.

### 1.6 marketplace.json for a private GitHub marketplace

- **Location:** `.claude-plugin/marketplace.json` at the repository root. [CC-MKT]
- **Required fields** [CC-MKT]
  - `name`: kebab-case. Reserved names include `claude-plugins-official`, `anthropic-plugins`, `agent-skills` and `knowledge-work-plugins`.
  - `owner{name, email?, url?}`.
  - `plugins[]`, each entry with `name` and `source`.
- **Optional top-level fields** [CC-MKT]
  - `$schema`, `description`, `version`.
  - `metadata.pluginRoot`: lets `source` be a bare name (2.1.239+).
  - `renames` (2.1.193+) and `allowCrossMarketplaceDependenciesOn`.
- **Optional plugin-entry fields:** `displayName`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `keywords`, `category`, `tags`, `defaultEnabled`, component paths, and `strict`. [CC-MKT]
  - `strict` defaults to `true`, meaning plugin.json is authoritative.
- **Source types** [CC-MKT]
  - A relative path such as `./plugins/x`, resolved from the marketplace root.
  - `github` (`repo`, `ref`, `sha`), `url` (git), `git-subdir` and `npm`.
  - `archive` (2.1.224+) and `command` (2.1.229+).
  - Organization-synced marketplaces accept only relative paths, `github`, `url` and `git-subdir`. [SUP-ORGPLUG][CC-MKT]
- **Private repos in Claude Code** [CC-MKT]
  - Claude Code uses the git credential helpers already configured, such as the one from `gh auth login`. SSH works if the key is loaded.
  - The `owner/repo` shorthand clones over SSH unless `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` is set.
  - Background auto-update disables credential helpers for HTTPS. Fixes: run `gh auth setup-git`, add a git URL rewrite scoped to the repo with a read-only token, or set `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1`.
- **Commands**
  - Add a marketplace: `/plugin marketplace add owner/repo[@ref]` or `claude plugin marketplace add` (with `--scope` and `--sparse`). [CC-MKT][LOCAL]
  - Install: `claude plugin install name@marketplace` (with `--scope user|project|local` and `--config`). [LOCAL]
- **Team pre-registration:** add `extraKnownMarketplaces` and `enabledPlugins` to `.claude/settings.json`. The folder must be trusted first. [CC-MKT]

---

## 2. Skills

### 2.1 Frontmatter (Claude Code; every field optional)

- **Fields:** `name`, `description` (recommended), `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort` (`low`, `medium`, `high`, `xhigh`, `max`), `context: fork`, `agent`, `background` (fork only, 2.1.218+), `hooks`, `paths`, `shell`, `metadata`, `license`, and `compatibility` (at most 500 characters). [CC-SKILLS]
- **Booleans** accept yes/no/on/off/1/0 from 2.1.218; earlier versions accept only true/false. [CC-PREF]

### 2.2 Limits

- **Claude Code**
  - `description` plus `when_to_use` is cut at 1,536 characters in the skill listing. No maximum is documented for `name`. [CC-SKILLS]
  - A plugin skill's command is `/<plugin>:<name>`. The bare `/<name>` also works unless another command already uses it. [CC-SKILLS]
- **claude.ai and Cowork uploads (Agent Skills spec)** [SK-HOWTO][PF-SKBP]
  - `name` is required: lowercase letters, digits and hyphens, at most 64 characters, matching the directory name, and not containing "anthropic" or "claude".
  - `description` is required: at most 1,024 characters, with no XML tags.
- **Body size:** keep SKILL.md under 500 lines. [CC-SKILLS][PF-SKBP][SK-HOWTO]
- **Description style:** third person, covering both what the skill does and when to use it, with specific trigger terms. [PF-SKBP]

### 2.3 Invocation controls and arguments

- **`disable-model-invocation: true`** [CC-SKILLS][CC-AGENTS]
  - Only the user can invoke the skill, and its description leaves Claude's context.
  - It also cannot be preloaded into subagents or used in scheduled runs.
- **`user-invocable: false`:** hidden from the `/` menu, but Claude can still invoke it. [CC-SKILLS]
- **Tool fields** [CC-SKILLS]
  - `allowed-tools` pre-approves tools until the user's next message. It does not restrict which tools are available.
  - `disallowed-tools` removes tools until the user's next message.
- **Arguments:** `$ARGUMENTS`, `$0` or `$ARGUMENTS[0]`, and named `$name` via `arguments`. An indexed placeholder with no value stays literal; a named one becomes empty. [CC-SKILLS]
- **Admin controls** [CC-SKILLS]
  - `skillOverrides` in settings, with states `on|name-only|user-invocable-only|off`.
  - Permission rules of the form `Skill(name)`.

### 2.4 Progressive disclosure

- **What loads when:** only name and description are preloaded. SKILL.md loads when the skill is used. Other files load only when read, and scripts run without their source entering context. [PF-SKBP]
- **File structure** [PF-SKBP]
  - Link reference files directly from SKILL.md (one level deep).
  - Give reference files over 100 lines a table of contents.
  - Use descriptive file names, and say whether a script should be run or read.
- **Content** [PF-SKBP]
  - Avoid time-sensitive statements and keep terminology consistent.
  - Give a default approach rather than many options.
  - Use checklists and validate-fix loops for fragile steps, and plan-validate-execute for batch or destructive changes.
- **MCP tools** mentioned in a skill should be fully qualified (server plus tool). [PF-SKBP]

### 2.5 Description budget across many skills

- **Budget:** the listing always contains every skill name. Descriptions are shortened to fit a budget of 1% of the model's context window, and the least-used skills lose their descriptions first. [CC-SKILLS]
- **Levers** [CC-SKILLS]
  - Raise the budget with `skillListingBudgetFraction` or `SLASH_COMMAND_TOOL_CHAR_BUDGET`.
  - Free budget by setting low-priority skills to `name-only`.
  - `/doctor` estimates the listing cost, and `/skill-doctor` flags skills that are never used.
- **After compaction** the listing is not re-injected. [CC-CTX]

### 2.6 Compaction

- **Skills:** the most recent invocation of each skill is re-attached after the summary. Each keeps its first 5,000 tokens, within a shared 25,000-token budget filled from the most recently invoked skill; older skills can drop out. [CC-SKILLS]
- **Other context:** the project-root CLAUDE.md is re-read. Instructions given only in conversation are lost. [CC-MEM]

### 2.7 Dynamic context injection

- **What it is:** a `!` command inline, or a fenced block marked `!`, runs before the skill reaches Claude. If the command fails, the whole invocation aborts. [CC-SKILLS]
- **In Cowork on desktop:** every `!` line is replaced with the `disableSkillShellExecution` placeholder. Skills synced from claude.ai never run these commands locally. [CC-SKILLS]

### 2.8 Skills as slash commands; is `commands/` still needed?

- **Same mechanism:** skills and commands are one thing. `commands/` flat files still work but are legacy; skills add supporting files and frontmatter controls. [CC-SKILLS][CC-PLUG]
- **Token accounting:** `claude plugin details` counts `commands/` entries under Skills. [CC-PREF]
- **In Cowork:** type `/` or click `+` to run plugin skills. [SUP-PLUG]
- **Verdict:** new plugins do not need `commands/`. [CC-PLUG]

### 2.9 `context: fork`

- **Behavior:** the skill body runs as a subagent task. `agent` selects `Explore`, `Plan`, `general-purpose`, or a custom subagent from `.claude/agents/`. [CC-SKILLS]
- **Open point:** whether `agent:` accepts a plugin-scoped agent name is not confirmed.
- **Caveats:** a backgrounded forked skill gets the narrower tool set, and its edits fall outside `/rewind` checkpoints. [CC-SKILLS]

---

## 3. Subagents in plugins

### 3.1 Frontmatter fields

- **Identity** [CC-AGENTS][CC-PREF]
  - `name`: required for user and project agents; lowercase with hyphens, no `:`. A plugin agent with no `name` loads under its filename.
  - `description`: required.
- **Behavior fields** [CC-AGENTS]
  - `tools`, `disallowedTools`, `model`, `permissionMode`, `maxTurns`.
  - `skills`: preloads the full content of the listed skills.
  - `mcpServers`, `hooks`.
  - `memory` (`user|project|local`), `background`, `effort`.
  - `isolation: worktree`, `color`, `initialPrompt`, `experimental.cacheTtl`.
- **Description budget:** if all agent descriptions together exceed 15,000 tokens, Claude Code shows a startup warning. [CC-AGENTS]
- **Broken frontmatter:** a plugin agent whose frontmatter does not parse still loads under its filename, with every field ignored. [CC-PREF]

### 3.2 Models

- **Values:** `sonnet`, `opus`, `haiku`, `fable`, a full model ID such as `claude-opus-5`, or `inherit`. [CC-AGENTS]
- **Resolution order:** a per-call `model` chosen by Claude, then frontmatter, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main session's model. [CC-AGENTS]

### 3.3 Tool allow and deny lists

- **Basics** [CC-AGENTS]
  - `tools` is an allowlist; omitting it inherits everything.
  - `disallowedTools` is applied first.
  - If no `tools` entry resolves to a real tool, the agent usually fails to launch.
- **MCP patterns** [CC-AGENTS]
  - `mcp__<server>` or `mcp__<server>__*` work in both lists.
  - `mcp__*` (every MCP tool) works only in `disallowedTools`.
- **Tool name formats**
  - Ordinary servers: `mcp__<server>__<tool>`. Plugin-bundled servers: `mcp__plugin_<plugin>_<server>__<tool>`. [CC-MCP][CC-PREF]
  - claude.ai connectors that Claude Code fetches itself: `mcp__claude_ai_<server>__<tool>`. [CC-PERM]
  - In Desktop local sessions, connectors are registered in-process as `type: "sdk"` servers. [CC-MCP] Their tool-name prefix there is not confirmed.
- **Cowork shell tools:** shell is `mcp__workspace__bash` and web fetch is `mcp__workspace__web_fetch`. Deny rules on `Bash`/`WebFetch` apply to them; allow rules do not. [CC-PERM] Whether an agent's `tools: Bash` covers `mcp__workspace__bash` is not confirmed.
- **Spawning:** the `Agent(type,...)` syntax restricts types only for a main-thread agent started with `--agent`. In a subagent's `tools`, listing `Agent` allows spawning, and any type list is ignored. [CC-AGENTS]
- **Always removed from subagents:** `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode` (unless in plan mode), `Workflow` and `TaskOutput`, among others. `Agent` is also removed at the depth limit. [CC-AGENTS]

### 3.4 Fields ignored for plugin agents

- `hooks`, `mcpServers` and `permissionMode` are ignored, for security. [CC-AGENTS][CC-PREF]
- The docs' workaround is to copy the agent into `.claude/agents/`, or to add session-wide permission rules. [CC-AGENTS]

### 3.5 Nesting and concurrency

- **Depth:** subagents can nest up to 3 layers below the main conversation by default (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`). [CC-AGENTS]
- **Concurrency:** up to 20 run at once by default (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`). [CC-AGENTS]
- **Version:** these caps need Claude Code 2.1.217 or later. [PF-OPUS5]

### 3.6 Foreground vs background

- **Background tool set:** background subagents keep every MCP tool, but only these built-ins [CC-AGENTS]:
  - Read, Grep, Glob, Bash, PowerShell, Edit, Write, NotebookEdit
  - WebFetch, WebSearch, TodoWrite, Skill, ToolSearch
  - EnterWorktree, ExitWorktree, Monitor, TaskStop, SendMessage, Artifact
- **When they run in background:** wherever fork mode is on (the interactive default), and whenever the agent sets `background: true`. [CC-AGENTS]
- **Permissions:** prompts from background subagents surface in the main session. [CC-AGENTS]
- **Starting context** [CC-AGENTS][CC-MEM]
  - Gets: its own system prompt, the task message, CLAUDE.md (except for Explore and Plan), and preloaded skills.
  - Does not get: the conversation history or the parent's auto memory.

### 3.7 How a skill should direct Claude to a plugin agent

- **Two documented ways** [CC-AGENTS]
  - Name the agent in natural language; Claude decides whether to delegate.
  - Use an @-mention, `@agent-<plugin>:<agent>`, which guarantees that agent runs.
- **Whole session:** `claude --agent <plugin>:<agent>` runs a session as that agent. [CC-AGENTS]
- **Descriptions drive delegation,** so keep them short and specific. [CC-AGENTS]
- **Resuming:** custom agents return an ID and can be resumed with `SendMessage`. [CC-AGENTS]

### 3.8 Availability: Cowork vs chat

- The help center says hooks and sub-agents run only in Cowork and appear greyed out in chat. [SUP-PLUG]
- claude.com says plugins are not used in Chat at all. [CW-PLUG]
- The Desktop changelog adds organization-plugin skills and hooks to Chat. [CW-CHANGELOG]
- Treat Cowork and Claude Code as the supported surfaces.

---

## 4. Cowork specifics

### 4.1 Runtime model

- **Two execution modes** [SUP-ARCH]
  - Cloud sessions are the default: a sandbox per session on Anthropic infrastructure, destroyed when the session ends.
  - Local sessions remain available for existing desktop deployments: the agent loop runs on the device, and code runs in an isolated Linux VM (Apple Virtualization.framework on macOS).
- **Local file access:** the help center calls cloud the default (in beta). Access to local files, the browser or the computer needs the Desktop app open and connected. [SUP-COWORK]
- **Local architecture** [ENG-CONTAIN]
  - The agent loop and local MCP servers run on the host; code runs inside the guest VM.
  - The chosen workspace folder and the `.claude` folder are mounted into the VM.
  - Credentials stay in the host keychain.
- **Sandboxed shell:** Desktop admin docs name `curl`, `pip`, `npm`, `git` and plugin commands as things that run in Cowork's sandboxed shell. [CD-PROXY][CD-CONF]
- **Open point:** which mode the user's sessions use is not confirmed.

### 4.2 Installing a plugin from a private GitHub marketplace

- **Steps** [CW-PLUG][ACAD-FIN]
  1. In Cowork, open Customize, then Plugins (Browse plugins, then Personal).
  2. Click `+`, choose Add marketplace (from GitHub), and enter `https://github.com/owner/repo` or `owner/repo`.
  3. Install the plugin. Later, click Update on the marketplace to pull changes.
- **Hosts:** GitHub, including Enterprise, is supported; GitLab and Bitbucket work only for public repos. [CW-PLUG]
- **Private-repo access**
  - How a personal (non-organization) account authenticates to a private GitHub repo is not confirmed.
  - Team and Enterprise organizations must use private or internal repos, synced through the Claude GitHub App. [SUP-ORGPLUG]
  - A private plugin source works there only if it shares the marketplace repo's owner, or sits on the org's GitHub Enterprise with the app installed. [SUP-ORGPLUG][CC-MKT]
- **File upload alternative**
  - Upload a plugin file on the Plugins page. [CW-PLUG] Cowork's customize flow produces a `.plugin` package. [ACAD-CUST]
  - Cowork limits: 200 MB uncompressed per package, 5,000 files per package, 512 MB marketplace archive, 500 plugins per marketplace, 25 marketplaces. [CW-PLUG]
  - Organization manual uploads: `.zip` files up to 50 MB. [SUP-ORGPLUG]
- **Updates**
  - Cowork checks the source marketplace for updates and warns before an update would overwrite local edits. [CW-PLUG]
  - Desktop added an auto-update option for custom marketplaces in v1.40609.0. [CW-CHANGELOG]
- **Where plugins live**
  - In Cowork and cloud sessions, plugins enabled for the account download to `~/.claude/plugins/synced/` in the session environment and load as `<name>@synced`. A same-named plugin from another source wins. [CC-PREF]
  - The help center says plugins you add yourself are saved locally. [SUP-PLUG]
- **Plans:** plugins are on all paid plans. [SUP-PLUG] Cowork is on Pro, Max, Team and Enterprise. [SUP-COWORK][SUP-PROJ]

### 4.3 Projects, folders, instructions

- **What a project holds:** a description, one or more local folders, instructions, links, linked chat projects, and project-scoped memory. [CW-PROJ]
- **Ways to create one:** start from scratch, import a claude.ai project, or use an existing folder. [CW-PROJ][SUP-PROJ]
- **Instruction layers**
  - Global instructions (Settings, then Cowork), project instructions, and organization preferences on Enterprise. [ACAD-CTX]
  - Folder instructions apply when a local folder is selected, and Claude can update them itself. [SUP-COWORK] Where they are stored is not confirmed.
- **Files** [CW-PROJ]
  - Files Claude creates land in the project's folders.
  - Dragged-in files are copied to the first folder.
  - Claude reads individual files up to 50 MB.
- **Archiving** removes name, instructions, links and memory, but leaves the attached folders untouched. [CW-PROJ]
- **Conflicting sources on sync and sharing**
  - claude.com: projects live only on the computer and are not shareable. [CW-PROJ]
  - Help center: new Cowork projects sync to the account, folder-based projects stay local, and sharing exists on Team and Enterprise. [SUP-PROJ]
- **CLAUDE.md**
  - Whether Cowork auto-loads a `CLAUDE.md` inside the attached folder is not confirmed.
  - Desktop Cowork does skip imports in the user-scope CLAUDE.md that point outside the session's working directory. [CC-MEM]

### 4.4 Bundled scripts (python3, node, shell)

- **Running code:** Cowork runs code and shell commands [SUP-COWORK] through `mcp__workspace__bash` [CC-PERM]. `pip`, `npm`, `git` and `curl` run in the sandboxed shell. [CD-PROXY]
- **Skill scripts:** skills may bundle Python, JavaScript/Node or Bash scripts. Claude can install PyPI or npm packages when the network allows it. [SK-HOWTO]
- **Runtime versions**
  - The Python and Node versions and libraries in the Cowork VM are not confirmed.
  - For comparison only: Claude Code cloud sessions use Ubuntu 24.04 with Python 3, Node, git and gh preinstalled. [CC-CLOUD] That page covers Claude Code on the web, not Cowork.
- **Plugin paths:** `${CLAUDE_PLUGIN_ROOT}` is substituted in skill content. [CC-SKILLS] Whether that path is reachable from inside the VM is not confirmed, although the `.claude` folder is mounted into the guest. [ENG-CONTAIN]

### 4.5 Filesystem scope

- **Scope:** Claude reads and writes only connected folders, and permanently deleting a file needs explicit permission. [SUP-COWORK][SUP-SAFE]
- **Checks:** each local tool call is checked against permissions. [SUP-ARCH] Mount modes include read-only, read-write, and read-write-no-delete. [ENG-CONTAIN]
- **Allowed folders:** Desktop can now attach the home folder and similar locations, excluding Claude config, credentials and shell startup files. [CW-CHANGELOG]
- **Mechanism:** Cowork grants folder access through allow rules it supplies at launch. [CC-MANAGED]

### 4.6 Network access

- **Cloud sessions** [SUP-ARCH][SUP-SAFE]
  - All traffic leaves through a mandatory proxy, and only allow-listed destinations are reachable.
  - Private, internal and metadata addresses are blocked, and sessions cannot reach home or company networks.
  - Connector tokens stay server-side.
- **Local sessions**
  - Egress follows the organization's network egress settings. [SUP-ARCH]
  - The managed key `coworkEgressAllowedHosts` lists hosts the agent's shell and web fetch may reach. [CD-CONF][CD-WEB]
- **Individual plans:** chat code-execution egress is set in Settings, then Capabilities (off, package managers, allowlist, or all domains). [SUP-FILES] Whether that setting also governs Cowork is not confirmed.
- **What egress rules don't cover:** web search, web fetch and MCP connectors. [SUP-COWORK][SUP-SAFE] Connectors reach services through Anthropic's cloud, not the local network. [SUP-PLUG]

### 4.7 git and gh

- **Documentation gap:** no source documents git or gh as available and authenticated inside Cowork.
- **Evidence**
  - `git` commands are among those run in the sandboxed shell. [CD-CONF][CD-PROXY]
  - Credentials stay on the host and never enter the VM. [ENG-CONTAIN][CD-EXT]
- **Conclusion:** whether `gh`, signed in to the user's GitHub account on the Mac, works inside Cowork is not confirmed.
- **Code tab:** the Desktop Code tab uses the host's git and `gh`. [CC-DESK]

### 4.8 Web search

- Web search is available in Cowork; Team and Enterprise owners can turn it off. [SUP-COWORK][SUP-SAFE]
- Web fetch is limited to search results and URLs the user has shared. [SUP-SAFE]

### 4.9 monday.com connector

- **The connector** [CONN-MONDAY]
  - A directory connector published by monday.com, at `https://mcp.monday.com/mcp`, using OAuth.
  - The directory page lists 33 tools.
  - Add it via Customize or Connectors. [CC-DESK][SUP-PLUG]
- **monday's own plugin:** monday.com also publishes an Anthropic Verified Cowork plugin named "monday.com". [PLUG-MONDAY]
- **Introspection tools** [MON-MCP]
  - The monday MCP server offers `get_graphql_schema`, `get_type_details` and `all_monday_api` (dynamic GraphQL).
  - The dynamic API tools are beta, off by default in the self-hosted server, and incompatible with read-only mode.
  - Which tools the hosted connector exposes by default is not confirmed.
- **Traffic and policy**
  - Connector calls run server-side, and tokens never enter the sandbox. [SUP-ARCH][CC-CLOUD]
  - Organizations can set tool policies of `allow`, `ask` or `blocked`. [CD-EXT][CC-MCP]
- **In Claude Code** [CC-MCP]
  - Connectors appear in `/mcp` when signed in with a claude.ai account. `ENABLE_CLAUDEAI_MCP_SERVERS=false` or `disableClaudeAiConnectors` turns them off.
  - MCP output warns at 10,000 tokens and is capped at 25,000 by default (`MAX_MCP_OUTPUT_TOKENS`); larger results are saved to a file.
  - Tool search defers tool schemas by default.
- **Bundling it in the plugin:** a plugin `.mcp.json` remote server that needs sign-in prompts for it on install in Cowork [CW-PLUG], and gets stable names `mcp__plugin_<plugin>_<server>__<tool>` [CC-MCP].

### 4.10 Memory

- **Chat memory:** cloud Cowork shares memory with chat; local Cowork sessions do not. [SUP-MEM][BLOG-MEM]
- **Project memory** [SUP-PROJ][CW-PROJ][SUP-MEM][ACAD-CTX]
  - Each project has its own memory, and nothing crosses between projects.
  - Outside a project, each session starts fresh apart from global instructions.
- **Editing:** users view and edit memory in Settings, then Memory, under Topics. [BLOG-MEM][SUP-MEM]
- **Claude Code auto memory** is machine-local: `~/.claude/projects/<project>/memory/MEMORY.md`, with the first 200 lines or 25KB loaded. [CC-MEM] Whether it runs in Cowork is not confirmed.

---

## 5. Quality tooling

### 5.1 `claude plugin validate [--strict]`

- **What it checks** [CC-PREF][CC-MKT]
  - On a plugin: plugin.json, `hooks/hooks.json`, and frontmatter in the default `skills`, `agents` and `commands` folders.
  - On a marketplace: marketplace.json schema, duplicate names and path traversal.
- **Exit codes and output:** 0 pass, 1 fail, 2 run error. `--json` needs 2.1.259. [CC-PREF]
- **Limits of a run** [CC-MKT]
  - Validating a folder without a manifest (such as `./my-plugin/agents`) needs 2.1.233.
  - A plugin run does not check a root `SKILL.md`.
  - Paths set in plugin.json are only checked for existence, and symlinks are not followed.
- **Local sample:** `--strict` failed the official skill-creator plugin because its missing `version` is a warning. [LOCAL]

### 5.2 `claude plugin details` (token cost)

- **Output:** a component inventory (Skills including `commands/`, Agents, Hooks, MCP servers, LSP servers) with projected cost. [CC-PREF]
  - "Always-on" is listing text added to every session.
  - "On-invoke" is shown per component.
  - Estimates come from the count_tokens API, with a character-based fallback.
- **Usage:** the plugin must be installed, or loaded with `claude --plugin-dir <dir> plugin details <name>` (the flag goes before the subcommand). [LOCAL]
- **Local sample:** skill-creator costs about 87 tokens always-on and about 8.2k tokens on invoke. [LOCAL]

### 5.3 `claude plugin tag`

- **What it does:** creates a `{name}--v{version}` git tag after checking that plugin.json and any enclosing marketplace entry agree. [LOCAL][CC-PREF]
- **Options:** `--dry-run`, `--push`, `--remote`, `-m` (with `%s` for the version), and `-f` to skip the dirty-tree and tag-exists checks. [LOCAL][CC-PREF]
- **Why tags matter:** the tag convention feeds dependency version resolution. [CC-MKT]

### 5.4 Status of plugin evals

- There is no `claude plugin eval` in 2.1.174 [LOCAL], and the docs and changelog through 2.1.268 mention none. [CC-CHANGELOG][CC-PREF]
- The Skills best-practices page says there is currently no built-in way to run skill evaluations. [PF-SKBP]

### 5.5 Anthropic's skill-creator evaluation approach

- **Availability:** install with `/plugin install skill-creator@claude-plugins-official`. [CC-SKILLS] It also works in claude.ai and Cowork. [BLOG-SC]
- **What it does** [BLOG-SC]
  - Create, eval, improve and benchmark modes.
  - Parallel isolated runs with and without the skill; a grader, a blind A/B comparator and an analyzer.
  - Metrics: pass rate, time, tokens and variance.
  - Description tuning against trigger prompts.
- **Files and scripts** [SC-GH]
  - `evals/evals.json`: `skill_name`, plus `evals[]` entries with `id`, `prompt`, `expected_output`, `files` and `assertions`.
  - Workspace: `iteration-N/eval-ID/{with_skill, without_skill or old_skill}/outputs`.
  - `grading.json` holds `expectations[{text, passed, evidence}]`.
  - Aggregation runs through `scripts.aggregate_benchmark`. The review viewer is `eval-viewer/generate_review.py`, with `--static` for Cowork.
  - Trigger evals use about 20 should- and should-not-trigger queries with a 60/40 train/test split. `scripts.run_loop` needs `claude -p`.
- **By surface** [SC-GH]
  - Cowork has subagents but no display, so use the static HTML viewer.
  - claude.ai has no subagents, so runs are sequential and baselines are skipped.

### 5.6 Other supported ways to test

- **Evaluation-driven development** [PF-SKBP]
  - Record failures without the skill, write three scenarios, measure a baseline, then write minimal instructions and iterate.
  - Test with every model you plan to use.
  - Refine with one Claude instance and test with a fresh one.
- **Headless scenario runs** [CC-HEADLESS][CC-CLI]
  - `claude -p` with `--plugin-dir`.
  - `--output-format json`, which includes `total_cost_usd`, and `--json-schema`.
  - `--max-turns`, `--max-budget-usd`, `--allowedTools` and `--disallowedTools`, and `--no-session-persistence`.
  - `--bare` skips auto-discovery, so pass the plugin explicitly.
- **Local development loop**
  - `--plugin-dir` accepts a folder, a `.zip`, or a folder of plugins (2.1.265+). `/reload-plugins` picks up edits. [CC-PLUG]
  - `claude --debug` shows load errors. [CC-PREF] `/context` shows which agents and memory files loaded. [CC-PLUG][CC-MEM]
- **Before a claude.ai upload:** run `skills-ref validate ./my-skill`. [SK-HOWTO]
- **Features newer than the local 2.1.174 CLI** [CC-MKT][CC-PREF][CC-SKILLS][CC-PLUG][PF-OPUS5]
  - Validating a skills or agents folder without a manifest: 2.1.233.
  - `validate --json`: 2.1.259.
  - yes/no booleans and fork `background`: 2.1.218.
  - `metadata.pluginRoot` and the `@synced` identity: 2.1.239.
  - A folder of plugins in `--plugin-dir`: 2.1.265.
  - Subagent depth and concurrency caps: 2.1.217.

---

## 6. Prompting guidance for current models

The reference page covers Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5, Opus 4.8, 4.7 and 4.6, Sonnet 5, Sonnet 4.6 and Haiku 4.5. [PF-PROMPT]

### 6.1 Calm vs emphatic language

- **Drop the shouting:** strong wording that was added to fix undertriggering now makes models overtrigger. Say "use X when..." instead of all-caps CRITICAL/MUST. [PF-PROMPT]
- **Target your defaults:** replace blanket "if in doubt, use the tool" rules with specific when-to-use guidance. [PF-PROMPT]
- **Explain why:** skill-creator's own guidance prefers explaining the reason over rigid MUSTs, and keeping prompts lean. [SC-GH]
- **Opus 5:** remove "verify" and "double-check" instructions. The model already checks its own work, and these cause over-verification. [PF-OPUS5]
- **Fable 5:** brief instructions steer it well, and older, heavily prescriptive skills can degrade its output. [PF-FABLE5]

### 6.2 Explicit instructions

- **Be direct:** state the desired output and constraints clearly, and use numbered steps when order matters. [PF-PROMPT]
- **Give reasons:** Claude generalizes from them. [PF-PROMPT][PF-FABLE5]
- **Phrase positively:** say what to do rather than what to avoid, and match the prompt's formatting to the output you want. [PF-PROMPT]
- **Action vs suggestion:** "change X" gets action; "suggest changes to X" gets suggestions. [PF-PROMPT]
- **Sonnet 5** follows instructions literally and does not extend a rule to other items on its own, so state the scope. [PF-SONNET5]
- **Opus 5** [PF-OPUS5]
  - Ask for brevity explicitly, and calibrate the length of written documents.
  - Constrain task scope.
  - Give explicit criteria for when to spawn subagents.
- **Fable 5** [PF-FABLE5]
  - Pause only for destructive or irreversible actions, real scope changes, or input only the user can give.
  - Base progress reports on actual tool results.
  - State limits on actions nobody asked for.
- **Risky actions:** ask before actions that are hard to reverse or visible to others. [PF-PROMPT]

### 6.3 Examples

- **Few-shot:** 3 to 5 relevant, varied examples inside `<example>` or `<examples>` tags; XML tags also separate instructions, context and inputs. [PF-PROMPT]
- **Canonical over exhaustive:** a few varied canonical examples work better than a long list of edge cases. [ENG-CTX]
- **In skills:** give concrete input/output pairs. [PF-SKBP]
- **Show good behavior:** examples of the desired style work better than instructions about what to avoid. [PF-OPUS5][PF-SONNET5]

### 6.4 Context engineering and long-running memory files

- **Right altitude:** aim for specific heuristics, avoiding both brittle hard-coded logic and vague guidance, with few high-signal tokens. [ENG-CTX]
- **Just-in-time retrieval:** keep lightweight identifiers (paths, IDs) and load the data at runtime. [ENG-CTX]
- **Long-horizon techniques** [ENG-CTX]
  - Structured notes kept outside the context window.
  - Compaction that preserves decisions and open issues.
  - Subagents that return condensed summaries of about 1,000 to 2,000 tokens.
- **State tracking** [PF-PROMPT]
  - JSON for structured state, free text for progress notes, and git for checkpoints.
  - A fresh context window can rediscover state from files.
- **Memory systems** [PF-FABLE5]
  - One lesson per file, each with a one-line summary.
  - Record corrections and confirmed approaches, with the reason.
  - Don't save what files already record; update an existing note rather than duplicating it; delete notes that prove wrong.
- **Size discipline in Claude Code** [CC-MEM]
  - Keep each CLAUDE.md under about 200 lines, specific and free of contradictions.
  - The MEMORY.md index loads its first 200 lines or 25KB; detail goes in topic files.
  - HTML comments are stripped from CLAUDE.md, and memory files get a `modified` timestamp (2.1.214+).
- **Long inputs:** put long documents above the question, and quote the relevant parts before answering. [PF-PROMPT]

---

## 7. Build implications (inferences from the sources above)

1. **Distribution.** Use one private GitHub repo that is also the marketplace, with the plugin under `./plugins/monday-master-builder/`.
   - Set `version` only in plugin.json.
   - For each release: run `claude plugin validate --strict`, bump the version, then `claude plugin tag --push`.
2. **Test on both surfaces.** Use Claude Code with `--plugin-dir`, and Cowork via Customize.
   - Smoke-test private-repo access in Cowork first. Plugin upload is the fallback.
3. **Skill frontmatter to the strictest common rules.**
   - `name` equals the directory name, at most 64 characters; `description` at most 1,024, third person, covering what and when.
   - Put `disable-model-invocation: true` on entry points with side effects (build, close-out). This also keeps them out of subagent preloads.
4. **Scripts.** Avoid `!` injection and `Bash(...)` allow rules.
   - Have skills tell Claude to run `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/..."`.
   - Keep scripts standard-library only: the Mac has only pyyaml and jsonschema, and the Cowork VM runtime is unknown.
   - Scripts should check that required tools exist.
5. **Context budget.**
   - Put each skill's essential rules in its first ~5,000 tokens; that is what survives compaction.
   - Keep the number of skills and their description text small.
   - Move procedures into reference files linked from SKILL.md.
6. **Read-only auditor agent.**
   - Use `disallowedTools` (Write, Edit, and monday write tools once their names are verified on each surface).
   - Avoid a narrow `tools` allowlist: it could resolve to zero tools in Cowork and fail to launch.
   - Plugin agents can't carry hooks or `permissionMode`.
7. **Approval stops belong in the main thread.** Subagents lack `AskUserQuestion`, so approval questions go in main-thread skills, not in agents.
8. **monday introspection.**
   - Prefer schema tools (`get_graphql_schema`, `get_type_details`) if the connector exposes them.
   - Query narrowly, because of the 25k-token MCP output cap.
   - Pick names that don't collide with monday's own "monday.com" plugin.
9. **The client folder is the memory.**
   - Don't rely on Cowork project memory: local sessions lack chat memory, and archiving a project deletes its memory.
   - Have skills explicitly read CLIENT.md and log.md rather than assuming CLAUDE.md auto-loads.
   - Follow the documented habits: short index files, one line per entry, and detail in topic files.
10. **Close-out archive.** Plan to run git and gh from Claude Code on the Mac, where credentials live, unless git push from inside Cowork is verified.
    - Deleting the local folder will trigger Cowork's explicit delete permission prompt.
11. **One Cowork project per client.** Attach `~/DelOps/clients/<slug>/` and keep project instructions short, pointing to CLIENT.md.
    - Archiving the project at close-out removes only its metadata and memory.
12. **Verification steps.** Keep read-back verification and the auditor as explicit, named workflow steps; they are deliverables.
    - Avoid generic "double-check your work" wording, which causes over-verification on Opus 5.
    - Fable 5 guidance favors fresh-context verifier subagents over self-critique.
13. **Upgrade Claude Code** from 2.1.174 before relying on flags documented for 2.1.2xx.

---

## 8. Not confirmed / open questions

- **Private marketplace auth in Cowork:** how a personal (Pro/Max) account authenticates to a private GitHub marketplace. The org route uses the Claude GitHub App.
- **`userConfig` in Cowork:** whether user-installed plugins can use it.
- **Cowork VM runtime:** Python and Node versions, preinstalled libraries, and whether pip/npm installs are allowed by default on individual plans.
- **git/gh in Cowork:** whether either works authenticated, given that credentials stay on the host.
- **Connector tool names:** the prefix in Cowork and Desktop sessions (in-process `sdk` servers), and whether agent `tools`/`disallowedTools` MCP patterns match it.
- **Agent tool mapping:** whether an agent's `tools: Bash` maps to `mcp__workspace__bash` in Cowork.
- **Fork agents:** whether a skill's `agent:` field accepts a plugin-scoped agent name.
- **Folder instructions and CLAUDE.md:** where folder instructions are stored, and whether Cowork auto-loads `CLAUDE.md` from the attached folder.
- **Auto memory in Cowork:** whether Claude Code auto memory is active there.
- **Plugin `settings.json`:** whether the `agent` key works in Cowork.
- **Hooks in Cowork:** where hook commands run (host or VM).
- **Session mode:** whether the user's Cowork sessions run locally or in the cloud. Sources say cloud is the default, and local folders need the Desktop app connected.
- **Bundled version:** which Claude Code version Claude Desktop bundles.
- **Hosted monday tools:** which tools the connector exposes, including schema introspection and `all_monday_api`.
- **Account plan:** the user's plan tier, which affects org GitHub sync, sharing and egress controls.
- **Conflicting sources**
  - Plugins in Chat: [SUP-PLUG] vs [CW-PLUG].
  - Project sync and sharing: [SUP-PROJ] vs [CW-PROJ].
  - Where plugins live: stored locally [SUP-PLUG] vs synced into the session [CC-PREF].

---

## Sources

| Key | URL |
|---|---|
| CC-PLUG | https://code.claude.com/docs/en/plugins |
| CC-PREF | https://code.claude.com/docs/en/plugins-reference |
| CC-MKT | https://code.claude.com/docs/en/plugin-marketplaces |
| CC-SKILLS | https://code.claude.com/docs/en/skills |
| CC-AGENTS | https://code.claude.com/docs/en/sub-agents |
| CC-HOOKS | https://code.claude.com/docs/en/hooks |
| CC-MCP | https://code.claude.com/docs/en/mcp |
| CC-PERM | https://code.claude.com/docs/en/permissions |
| CC-MEM | https://code.claude.com/docs/en/memory |
| CC-CTX | https://code.claude.com/docs/en/context-window |
| CC-DESK | https://code.claude.com/docs/en/desktop |
| CC-CLOUD | https://code.claude.com/docs/en/cloud-environments |
| CC-MANAGED | https://code.claude.com/docs/en/managed-settings |
| CC-HEADLESS | https://code.claude.com/docs/en/headless |
| CC-CLI | https://code.claude.com/docs/en/cli-reference |
| CC-CHANGELOG | https://code.claude.com/docs/en/changelog |
| CW-OVR | https://claude.com/docs/cowork/overview |
| CW-PLUG | https://claude.com/docs/cowork/guide/plugins |
| CW-PROJ | https://claude.com/docs/cowork/guide/projects |
| CW-CHANGELOG | https://claude.com/docs/cowork/changelog |
| CD-EXT | https://claude.com/docs/third-party/claude-desktop/extensions (Claude Desktop admin docs) |
| CD-CONF | https://claude.com/docs/third-party/claude-desktop/configuration |
| CD-PROXY | https://claude.com/docs/third-party/claude-desktop/network-proxy |
| CD-WEB | https://claude.com/docs/third-party/claude-desktop/web-tools |
| PL-OVR | https://claude.com/docs/plugins/overview |
| SK-HOWTO | https://claude.com/docs/skills/how-to |
| CONN-MONDAY | https://claude.com/connectors/monday |
| PLUG-MONDAY | https://claude.com/plugins/monday-com |
| SUP-PLUG | https://support.claude.com/en/articles/13837440-use-plugins-in-claude |
| SUP-ORGPLUG | https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization |
| SUP-COWORK | https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork |
| SUP-SAFE | https://support.claude.com/en/articles/13364135-use-claude-cowork-safely |
| SUP-ARCH | https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview |
| SUP-PROJ | https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork |
| SUP-MEM | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context |
| SUP-FILES | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude |
| ACAD-CTX | https://academy.claude.com/courses/introduction-to-claude-cowork/giving-cowork-context |
| ACAD-FIN | https://academy.claude.com/tutorials/install-financial-services-plugins-for-cowork |
| ACAD-CUST | https://academy.claude.com/tutorials/how-to-customize-plugins-in-cowork |
| BLOG-MEM | https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it |
| BLOG-SC | https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills |
| SC-GH | https://github.com/anthropics/claude-plugins-official/blob/main/plugins/skill-creator/skills/skill-creator/SKILL.md (Anthropic's GitHub org) |
| ENG-CONTAIN | https://www.anthropic.com/engineering/how-we-contain-claude |
| ENG-CTX | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| PF-SKBP | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices |
| PF-PROMPT | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices |
| PF-OPUS5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5 |
| PF-SONNET5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5 |
| PF-FABLE5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5 |
| MON-MCP | https://github.com/mondaycom/mcp (vendor, monday.com) |
| LOCAL | Read-only CLI runs on the user's Mac: `claude --version`; `claude plugin validate/details/tag/install/marketplace --help`; `claude plugin validate --strict` and `claude --plugin-dir <dir> plugin details` against the official skill-creator plugin clone |
