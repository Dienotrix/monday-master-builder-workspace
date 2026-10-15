# Cowork capability check — results

Run: 2026-09-11 (America/New_York) · read-only except for this report file.

## 1. Session
Cloud session — the main shell runs in an ephemeral Anthropic-hosted Linux container, **not** on your Mac. It is additionally linked to your Mac ("mac-lan", darwin/arm64) through a device bridge, so there are two shells. Cloud shell: Ubuntu 24.04.4 LTS, Linux 6.18.44, x86_64. Device shell (your Mac's Cowork VM): Linux 6.8.0-136, aarch64.

## 2. Folder access
Connected folder: `~/DelOps/monday-master-builder-dev/rebuild-workspace` (seen from the device shell as `$HOME/mnt/rebuild-workspace`). Read/write confirmed — this report was created there. Note: the check spec said to connect `~/DelOps/cowork-check`; the folder actually connected is `rebuild-workspace`, so the report landed there. File deletion was initially blocked ("Operation not permitted") and required a one-time approval prompt, which was granted for this session only.

## 3. Shell and languages
Two shells: `Bash` (cloud container) and `device_bash` (your Mac, scoped to connected folders, ~45s per call, no deletes without approval).

| | cloud | device (Mac) |
|---|---|---|
| python3 | 3.11.15 | 3.10.12 |
| node | v22.22.2 | v22.23.2 |
| npm | 10.9.7 | 10.9.8 |
| git | 2.43.0 | 2.34.1 |
| gh | not available | not available |
| pip | 24.0 | (not probed) |

## 4. Python packages (cloud)
`yaml` imports · `jsonschema` imports · `docx` imports · `reportlab` imports · `openpyxl` imports · `PIL` imports · `matplotlib` imports. All seven available.

## 5. Document tools (cloud PATH)
`pandoc` /usr/bin/pandoc (3.1.3) · `soffice` /usr/bin/soffice (LibreOffice 24.2.7.2) · `pdftoppm` /usr/bin/pdftoppm · `convert` /usr/bin/convert (ImageMagick; `magick` not present) · `rsvg-convert` not available · `mmdc` ~/.npm-global/bin/mmdc (Mermaid CLI) · `chromium`/`google-chrome` not on PATH, but Chromium 141.0.7390.37 is installed at `/opt/pw-browsers/chromium` for Playwright.

## 6. Node packages (cloud)
`npx` present (10.9.7) — but `npx --yes` for a package not already cached would fail, because the npm registry is blocked (see §7). `npm config get registry` = `https://registry.npmjs.org/`. `require('docx')` ok · `require('pptxgenjs')` ok · `require('sharp')` ok — all three pre-installed.

## 7. Network (cloud container, via the agent proxy)
| URL | result |
|---|---|
| https://pypi.org | 403 — blocked by egress policy |
| https://registry.npmjs.org | 403 — blocked by egress policy |
| https://github.com | 400 on a bare HTTP GET, but reachable for git (see §8) |
| https://api.github.com | 200 |
| https://mcp.monday.com/mcp | blocked (proxy CONNECT denied) |
| https://storage.googleapis.com | blocked (proxy CONNECT denied) |

`pip download requests` and `npm ping` both fail. Net effect: **no new Python or Node packages can be installed** — what is preinstalled is what you get. The monday.com MCP connector still works, because it is routed through Anthropic's MCP proxy rather than this shell.

## 8. Git and GitHub
`gh` is not installed, so `gh auth status` cannot be run — treat as not signed in. No git credential helper or URL rewrite is configured. `git ls-remote` against a non-existent repository under the user's GitHub account fails with `fatal: could not read Username for 'https://github.com': terminal prompts disabled` — an **authentication-missing** error, not a network error. Anonymous reads do work: `git ls-remote` against a public repo returned refs successfully.

## 9. Built-in skills and plugins
Account skills: `import-memory`, `morning`, `skill-creator`, `xlsx`, `pptx`, `pdf`, `docx`. Plugins: `documents` (doc_outline/read/search/edit/resolve_changes/create/check_layout/export). Session-provided skills also visible: `design`, `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`, `cowork-plugin`, `explain-usage`, `setup-claude`, `workflow-authoring`, `claude-in-chrome`. **docx, pdf and pptx skills: all three available.**

## 10. Subagents
Yes — `Agent` (types: claude, general-purpose, Explore, Plan, claude-code-guide, statusline-setup). A `Workflow` tool for multi-agent orchestration is also present but requires explicit opt-in.

## 11. monday connector
Connected and authenticated (signed in), enabled in this chat. Tool prefix: `mcp__monday_com__` — the user-context read tool is `mcp__monday_com__get_user_context`. It was called once (read-only) and returned an enterprise account with core/CRM/software/service/marketing products. No write tool was called.

## 12. Web
Yes — `WebSearch` and `WebFetch`. Two browsers are also reachable: Claude's built-in browser (`mcp__remote-devices__Claude_Browser__*`) and Claude in Chrome (`mcp__claude-in-chrome__*`). Computer use on the Mac is available but not yet turned on.

## 13. Memory and instructions
Persistent user memory is wired up (`mcp__memory__*`) but currently **empty** — no profile, no preferences, no files. No `CLAUDE.md` or other project-instruction file exists in the connected folder or the cloud workspace, so there are no project instructions in effect for this task.

---

## Summary

**Running small Python or Node scripts:** yes, comfortably. The cloud container has Python 3.11 and Node 22 with a generous preinstalled library set, and your Mac's Cowork shell has Python 3.10 and Node 22 for working on files in place. The one hard limit is that you cannot install anything new — pypi.org and registry.npmjs.org are both blocked by egress policy, so any script has to run on what is already there.

**Making Word, PDF and slide files:** yes, several ways over. The Documents plugin handles .docx/.cd/.pdf authoring and export natively; python-docx, openpyxl, reportlab, pptxgenjs and the docx Node package are all preinstalled; and pandoc plus LibreOffice are on the PATH for conversion. The docx, pdf, pptx and xlsx skills are all available.

**Turning diagrams into images:** yes. Mermaid CLI (`mmdc`) is installed, Chromium 141 is present for headless rendering, and ImageMagick (`convert`) plus `pdftoppm` cover raster conversion. The one gap is `rsvg-convert`, so plain SVG→PNG should go through ImageMagick or Chromium instead.

**Pushing to a private GitHub repo:** no, not as configured. The `gh` CLI is not installed, no git credentials or credential helper are set, and a push would fail at authentication rather than at the network — anonymous reads of public repos work fine, and api.github.com answers 200. To push, you would need to supply a token or configure a credential helper first, and note that `gh` cannot be installed here because package registries are blocked.
