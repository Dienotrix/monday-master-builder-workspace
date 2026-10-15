# Research: client SOP, process diagrams, handoff deliverables

Product: monday Master Builder (DelOps). Researched 2026-09-10. Clean-room: nothing from the old plugin was read or used.

Evidence tags:
- **[local]**: checked read-only on the user's Mac today.
- **[Sn]**: cited source (list at the end).
- **[inferred]**: my reasoning, needs a test.
- **[unconfirmed]**: evidence conflicts or is missing.

---

## 0. Decisions in one screen

| Topic | Recommendation |
|---|---|
| SOP source of truth | `sop/SOP.md` plus `sop/diagrams/*.flow.json` are the only sources. Every client format is generated from them and never edited by hand. |
| Section lifecycle | Each section has a status `planned → built → confirmed`, stamped with a solution version. The v1.0 export refuses any section that is not confirmed. |
| Internal notes | The SOP writer reads an allowlist of files only. A deterministic leak lint runs on SOP.md and again on every rendered output, then the auditor re-checks. |
| Diagrams, primary | A bundled stdlib-only Python script turns a JSON flow spec into a swimlane SVG using plain `<text>` (safe in Office). The same spec also yields a step table and Mermaid text. |
| Diagrams, fallback | Mermaid text rendered where a browser exists: on the Mac, mermaid-cli pinned to 11.17.0 using the installed Chrome (no browser download). Otherwise the step table alone. |
| PNG for Word, slides, monday | Probe and pick a rasterizer: sharp → ImageMagick → LibreOffice (sandbox), or Chrome `--screenshot` (Mac). |
| Handoff package | PDF (the approved record), Word (editable), monday Doc (living copy, text-first, diagram images added by hand). Slides later, from the same assets. |
| Office file mechanics | Hand these to Anthropic's docx, pdf and pptx skills after a capability probe. Their licence is source-available: invoke them, never copy them. |

---

## 1. The client SOP

### 1.1 What the sources say, applied to this product

**EPA QA/G-6, 2007 [S1]**
- **Format:** there is no single correct format. Tailor it to the organisation and break the content into logical steps.
- **Title page:** title, ID, issue or revision date, owning unit, and who prepared and approved it, with dates.
- **Table of contents:** also marks which sections changed.
- **Body order:**
  - purpose and scope
  - definitions
  - roles and qualifications
  - ordered procedure steps, including troubleshooting
  - records
  - references
- **Visuals:** use diagrams and flow charts to summarise long step sequences.
- **Cautions:** list them, and repeat each one at the step where harm can happen.
- **Style:** concise, step-by-step, active voice, present tense. The reader is implied rather than addressed.
- **Review and revision:**
  - Before approval, someone other than the writer should try out the draft.
  - Update and re-approve whenever the process changes.
  - A revision may touch only the affected section, as long as the table of contents and the control notation record it.
  - Review periodically (the guide suggests every 1–2 years).
- **Document control:** every page shows short title or ID, revision number, date, and "page x of y". Keep a master list (version, date, status). Archive superseded versions so nobody uses them by mistake.
- **Checklists:** they belong to the SOP. Reference each one at the step where it is used, and attach it.

**Diátaxis [S2]**
- Keep three kinds of content in separate sections: how-to (procedures), reference (setup, glossary, admin facts) and explanation (process overviews). Mixing them weakens each one.

**Google procedure style [S3]**
- One intro sentence, then numbered steps.
- Start each step with an imperative verb, one action per step.
- Give the location before the action: "On the **Jobs** board, click **New item**."
- Bold UI names.
- Prefix optional steps with "Optional:". Letter any sub-steps.
- A single-step procedure is a bullet, not a numbered list.
- State the result after the action. Never write "above" or "below".

**Plain language [S4]**
- Address the reader as "you", use active voice, and keep sentences short (average about 20 words, maximum about 40).
- To reconcile with EPA: steps use the imperative (the reader is implied), and "you" is fine in explanatory text.

**RACI and swimlanes [S7][S8]**
- Each activity has exactly one Accountable person.
- Swimlane lanes are roles. Their value is in showing handoffs between roles.

**Change log and versions [S5][S6]**
- Keep a Changelog: newest first, ISO dates, entries grouped as Added / Changed / Removed / Fixed, plus an Unreleased section.
- SemVer: 0.y.z means anything may change, and 1.0.0 fixes the contract. This maps directly onto v0.x demos versus v1.0 sign-off.

### 1.2 Section set

Sections appear in a fixed order. A section is left out only when it would be empty.

| # | Section | Type | Content | Allowed inputs |
|---|---|---|---|---|
| 0 | Cover and document control | – | Client; title "Operating Procedures – monday.com"; SOP version (= solution version) and revision; status Draft or Confirmed; date; prepared by DelOps; approved by (client name, role, date). The footer repeats short title, version and "page x of y". | versions/, sign-off record |
| 1 | Purpose and scope | explanation | Business outcomes supported; processes in scope; what stays outside monday; connected systems; how each role should use the document. | blueprint (client part) |
| 2 | Roles and responsibilities | reference | Role catalogue mapping client job title → monday user type (admin, member, viewer, guest [S29]) → team → boards used → procedures owned. A RACI per process with one Accountable each. The client's system owner. Support contact and how to request changes. | blueprint, build.json |
| 3 | Process overviews | explanation | One subsection per process: trigger, outcome, swimlane diagram, 5–10 line narrative, handoffs, what monday does automatically, related procedures. Plus one board map showing the boards and their connections in business terms. | flow specs, build.json |
| 4 | Procedures by role | how-to | Grouped by role, each titled as a task. Each has: when to do it; before you start; numbered steps; cautions at the critical step (for example deleting items, or changing a label that drives an automation); result ("done when"); what happens next automatically; linked checklist. | blueprint, verified build |
| 5 | Your monday setup explained | reference | Workspace map. For each board: what one item represents; what the groups mean; key columns (meaning, who updates them); a status label table (label → meaning → who sets it → what it triggers); automations written as "When… then… so that…"; forms; dashboards and the question each answers; integrations; views; board links. No raw IDs in body text. | build.json plus a live read at export |
| 6 | Administration | reference + how-to | Adding and removing people and choosing their user type; teams; board permissions and ownership (only admins and members can own boards [S29]); safe-change checks before renaming or deleting labels or columns used by automations, formulas, dashboards or integrations (checked live, not from memory); who owns each automation and integration; housekeeping cadence; how to request a v1.x change; SOP review date. | build.json, gotchas list, live read |
| 7 | Troubleshooting and FAQ | reference | Table of what you see / why / what to do / who can fix it, grouped by role. | auditor findings, client-safe FAQ candidates (1.4) |
| 8 | Glossary | reference | monday terms plus the client's own words mapped to monday objects ("Job = an item on the Jobs board"). One definition per term, used consistently. | blueprint, build.json |
| 9 | Change log | – | One Keep a Changelog entry per SOP version, plus review history. | versions/ |
| A | Appendices | – | Checklists (go-live, onboarding a new starter) and a board link index for admins. | as above |

**No screenshots in v1 of the product [inferred]:**
- There is no dependable way to capture the client's monday UI from Cowork.
- Screenshots go stale whenever monday changes its UI.
- Use bold UI names and board links instead.

### 1.3 Progressive authoring tied to solution versions

**Front matter.** SOP.md carries: `client`, `sop_version`, `solution_version`, `revision`, `status` (draft or confirmed), `updated`.

**Section marker.** Each section heading line carries an HTML comment, which every export strips:
`<!-- sop id=proc-job-intake status=built since=v0.2 verified=v0.3 confirmed=- src=blueprint#job-intake,build.json:boards.jobs -->`

**Status meanings:**
- **`planned`:** in the approved blueprint but not yet in monday. It never appears in client output, except in a labelled "Coming next" box on v0.x drafts.
- **`built`:** exists in monday and passed read-back plus the auditor at `verified=vX.Y`.
- **`confirmed`:** the client accepted it at a demo or at sign-off (`confirmed=vX.Y`; the date lives in versions/).
- **Rework:** a section that changes in v1.x drops back to `built` until the client confirms it again.

**Export rules by version:**
- **v0.x:** the draft is optional. Watermark and cover read "Draft for review – vX.Y". Only built or confirmed sections appear, plus "Coming next".
- **v1.0:** the export is blocked if any included section is not confirmed. The approval block must be filled in.
- **v1.x:** the SOP version follows the solution version. A wording-only fix bumps `revision` (EPA's revision number plus date) and adds a Fixed entry to the change log.

**SOP.md is a "current" file:**
- Rewrite it to present truth at each version, with no strike-through history.
- History lives in two places: the change log section and the frozen files in `deliverables/vX.Y/`.
- Condense it at each version, like the rest of the client record.

**Content rules:**
- SOP.md holds only built or confirmed facts.
- Nothing inferred.
- No client quotes; those stay in research/ and calls/.

**Drift guard at export [inferred]:**
- Collect every monday object named in SOP.md or in a flow spec: boards, groups, columns, status labels, automations, forms, dashboards.
- Each must resolve by name in build.json and in a fresh live read.
- Any mismatch blocks the export and lists the differences.

**Meeting rhythm (new chat per meeting):**
- The meeting wrap-up updates only the SOP sections affected by decisions the client confirmed.
- It also writes client-safe FAQ candidates (see 1.4).
- It never copies raw notes into the SOP.

**"Tested by someone else":** EPA's advice maps to the read-only auditor. Before a section moves from planned to built, the auditor walks each new procedure against the live account [inferred].

### 1.4 Keeping internal sales notes out

1. **Allowlist the SOP writer's inputs.**
   - Allowed:
     - `solution/blueprint.md` (client-facing parts only)
     - `solution/build.json`
     - `versions/`
     - `sop/`
     - the client-safe section of `solution/backlog.md`
     - the gotchas list
   - Never read:
     - `CLIENT.md`
     - `research/`
     - `calls/` (summaries and transcripts)
     - `discovery.md`
     - `log.md`
     - any internal heading anywhere
2. **Separate internal content structurally in source files.**
   - Blueprint and backlog entries keep internal reasoning under a fixed heading (for example `### Internal`), which the SOP step skips mechanically.
   - Client questions from calls reach the SOP only through a "For the SOP (client-safe)" list. The meeting wrap-up writes that list in client wording.
3. **Isolate the context [inferred].** Run SOP drafting as its own skill or subagent, given only the allowlisted files. It cannot leak what it never read.
4. **Lint deterministically.** A script runs on SOP.md, then again on text extracted from each rendered output. It flags:
   - denylisted terms, both global and per client: budget, price, discount, deal, objection, champion, blocker, competitor names, the stage and scoring terms of the user's sales method, "internal", "inferred";
   - leftover markers, HTML comments, TODOs, and file paths into the client record;
   - raw monday IDs outside links;
   - personal names that are not in the roles or approval tables;
   - quotation marks around client speech.

   Failures are reported loudly with line references. Nothing is auto-fixed.
5. **Give flow specs no free-text notes field**, so nothing internal can travel inside a diagram.
6. **Run an auditor pass on the finished package.** It checks for leakage and for factual match against the live account.

---

## 2. Process diagrams

### 2.1 Environment facts that decide the approach

| Environment | Facts |
|---|---|
| The user's Mac [local] | **Runtimes:** node v25.8.2, npx 11.11.1; python 3.9.6 with PyYAML 6.0.3 and jsonschema. **Apps:** Google Chrome 152.0.7977.83, Arc, Safari, Microsoft Word; no PowerPoint, Keynote or Pages. **Missing tools:** soffice, pandoc, dot, mmdc, rsvg-convert, ImageMagick, wkhtmltopdf, pdftoppm (Claude's PDF reader failed without it); no `~/.cache/puppeteer`. **Built-in tools present:** macOS `textutil` (converts html to docx/odt/rtf), `qlmanage`, `sips`, `cupsfilter`. |
| Cowork local VM (third-party teardowns, Jan and Apr 2026) | **System:** Ubuntu 22.04 ARM64 under Apple Virtualization, about 4 GB RAM. **Runtimes:** Python 3.10.12, Node 22.22.0. **Tools:** pandoc 2.9.2, ImageMagick 6.9.11; global node packages docx, pptxgenjs, pdf-lib, sharp. **Network:** proxy allowlist including api.anthropic.com, pypi.org, files.pythonhosted.org, registry.npmjs.org, github.com [S41][S42]. |
| Conflicting reports [unconfirmed] | In April 2026 a user reported that registry.npmjs.org returned 403 in Cowork, with github.com, jsdelivr, unpkg and cdnjs also blocked. This broke a built-in slide skill that ran `npm install` [S43]. A second report: extra allowlisted domains were not honoured under "Package managers only" [S44]. |
| Official statements | **Where code runs:** local Cowork sessions run code in an isolated VM with its own egress filtering; cloud sessions (beta) run in Anthropic sandboxes. **MCP:** local MCP servers run on the host and do not run in cloud sessions. **Egress scope:** egress settings do not govern web fetch, web search or MCP [S37][S38]. **Default list:** "package managers only" covers npm, PyPI, GitHub, Yarn, crates.io and Ubuntu; Pro and Max users toggle it in Settings › Capabilities. **Gap:** the article does not say whether Cowork uses the same list [S39]. |
| Anthropic cloud sandbox reference (Managed Agents; may differ from Cowork) | Ubuntu 24.04 x86_64. **Tools:** LibreOffice headless, Poppler, qpdf, pandoc, ImageMagick, TeX Live. **Browser:** Playwright with Chromium at `/opt/pw-browsers/chromium`, not on PATH. **Python libraries:** python-docx, python-pptx, pypdf, Matplotlib [S40]. |

**Implications [inferred]:**
- **No render-time downloads:** nothing the renderer needs may be fetched while rendering.
- **Browser downloads are blocked:** Chrome for Testing comes from storage.googleapis.com, which is on no package-manager list.
- **Portable scripts:** they must run on Python 3.9 and 3.10, and on Node 22 and 25.
- **Probe first:** every deliverable job starts with a capability probe (section 4).

### 2.2 Options evaluated

#### (a) Mermaid source rendered with `@mermaid-js/mermaid-cli` via npx

**Package facts [S11]**
- Version 11.17.0, published 2026-09-02.
- Depends on mermaid ^11.14, katex, Font Awesome, @mermaid-js/layout-elk and @mermaid-js/mermaid-zenuml.
- Puppeteer is a peer dependency (^23, ^24 or ^25). Node ^18.19 or ≥20.
- mermaid 12.0.0 was published today (2026-09-10 07:43 UTC) while the CLI still targets 11. Pin exact versions.

**Download size**
- The main npm packages alone total about 267 MB unpacked: mermaid 125 MB, zenuml 48 MB, layout-elk 28 MB, Font Awesome 25 MB, and others [S11, summed].
- Puppeteer's install step then downloads Chrome for Testing (about 170 MB on macOS, per Puppeteer's docs) and chrome-headless-shell into `~/.cache/puppeteer` [S12].
- Today's Chrome for Testing 153 zip sizes [S14]:

  | Build | mac-arm64 | linux64 |
  |---|---|---|
  | Chrome | 191 MB | 196 MB |
  | Headless shell | 99 MB | 120 MB |

- First run: roughly 0.5 GB downloaded and about 1 GB on disk [inferred].

**Headless browser**
- A headless browser is required.
- To skip the browser download, set `PUPPETEER_SKIP_DOWNLOAD=1` (on the first, installing run) and `PUPPETEER_EXECUTABLE_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"` [S13].
- As root on Linux, pass `-p puppeteer-config.json` containing `{"args":["--no-sandbox"]}` [S10].
- Some package managers skip install scripts, which leads to a "Could not find Chrome" error [S12].

**Usage [S9]**
- Command: `npx -p @mermaid-js/mermaid-cli@11.17.0 mmdc -i in.mmd -o out.svg -c mermaid.json`.
- Other flags: `-e`, `-t`, `-b`, `-w`, `-H`, `-s`, `-C`, `-q`, `--pdfFit`.
- Markdown input renders every fenced diagram to `name-1.svg`, `name-2.svg` and so on, and rewrites the links.

**Office gotcha [S17][S18]**
- By default Mermaid puts labels inside `foreignObject`. The text then disappears in PowerPoint, Word, Inkscape and librsvg.
- Fix: set the root-level `"htmlLabels": false` (`flowchart.htmlLabels` is deprecated), or ship PNG.

**Reliability**
- **Mac:** good once cached, using the local Chrome 152 rather than Puppeteer's pinned build. Compatibility is likely but not guaranteed [inferred].
- **Cowork:** poor. npm access is disputed, the browser download is blocked, and there is no confirmed Chromium on PATH.

**Verdict:** an optional local upgrade path, never a hard dependency. Never use public render services (mermaid.ink, public Kroki) for client content; they send the process to a third party [inferred].

#### (b) Mermaid in a self-contained HTML deliverable, printed to PDF

**Bundle**
- `mermaid.min.js` measured on jsDelivr: 3.57 MB for mermaid 11, 5.58 MB for mermaid 12 [S19].
- Vendor v11 (MIT) into the plugin. Loading from the CDN needs internet when the file is opened, and Cowork blocks jsDelivr [S43].

**How the PDF gets made**
- Mermaid runs in the browser of whoever opens the file, so producing the HTML needs no tooling anywhere.
- The PDF comes from the viewer's Print dialog.
- On the Mac it can be automated: `Google Chrome --headless --no-pdf-header-footer --print-to-pdf=out.pdf --virtual-time-budget=10000 file:///…` [S15].
- Unconfirmed: whether `--print-to-pdf` waits for Mermaid's asynchronous render. Test with `startOnLoad:false` plus `await mermaid.run()`.
- Use a temporary `--user-data-dir` so the run does not collide with the user's open Chrome [inferred].
- Cowork cannot automate the PDF: no Chrome is confirmed in the VM.

**Pros**
- CSS print control (`@page`, `break-inside: avoid`).
- Diagrams stay vector in the PDF.

**Cons**
- 3.6 MB of JavaScript inside a client file.
- HTML attachments are often blocked by mail and file-sharing tools [inferred].
- No native swimlanes. Subgraphs only approximate lanes, and ordering control is weak. ELK layout is a separate package [S11][S16].
- Nothing reusable for Word or monday.

**Verdict:** an acceptable fallback viewer, weaker than (c) as the standard output.

#### (c) Dependency-free generator: JSON (or YAML) flow spec → SVG

**Runtime**
- Python stdlib runs as-is on 3.9.6 (Mac) and 3.10 (Cowork). Node would also work.
- Make JSON the canonical spec format. YAML needs PyYAML, which is on the Mac but unconfirmed in Cowork, and Node would need a YAML package.

**Layout.** Swimlanes are a constrained layout, not general graph drawing [inferred]:
- lanes are roles (rows);
- a step's column is its longest-path rank from the start;
- decisions branch to neighbouring rows or columns;
- loop-back edges route through a gutter;
- connectors are orthogonal.

Estimated size: about 400–700 lines including tests [inferred].

**SVG that works in Office**
- Plain `<text>` and `<tspan>` only, never `foreignObject`.
- `viewBox` plus width and height.
- `<title>` and `<desc>` for alt text.
- Font stack `Arial, Helvetica, Liberation Sans, sans-serif`, which has matching metrics on Mac, Windows and LibreOffice [inferred].
- SVG has no text wrapping. Wrap using a per-character width table for Helvetica/Arial (or a conservative average), and cap label length.

**Other outputs from the same spec**
- Mermaid text, for the fallback render and previews.
- A step table (Step / Who / Where in monday / Result), for the SOP, the monday Doc and accessibility.

**Rasterizing:** Word needs a PNG fallback, and slides and monday images need PNG. See section 4.

**Validation.** Written in stdlib inside the script, since jsonschema is on the Mac but unconfirmed in Cowork. Checks:
- exactly one start;
- decisions have at least 2 labelled exits;
- every lane is used;
- labels are at most 60 characters;
- every monday reference resolves in build.json.

**Testing:** golden-file snapshots per scenario (linear flow, 2 decisions, rework loop, 6 lanes, long labels). Output is deterministic, so diffs are meaningful.

**Cons**
- More code to own and maintain.
- A plainer look than Mermaid or ELK.
- Complex processes must be split; suggested cap about 6 lanes and 25 steps per diagram [inferred].

**Considered but not primary**
- **`beautiful-mermaid` 1.1.3:** MIT, no DOM, synchronous SVG, 2.1 MB. Depends on elkjs (EPL-2.0 or GPL-3.0). Subgraph and classDef support is undocumented [S11][S20].
- **`@viz-js/viz` 3.30.0:** Graphviz compiled to WebAssembly; renders DOT to SVG in Node with no native dependencies; 5 MB. Graphviz clusters can serve as lanes [S11][S21].
- Both need npm or vendoring, plus a licence review before bundling.

#### (d) monday Docs

**Block types via the API [S22]**
- **Text:** normal_text, large_title, medium_title, small_title, quote.
- **Lists:** bulleted_list, numbered_list, check_list.
- **Media and structure:** image, video, table, layout, code, divider, notice_box, page_break.
- There is no diagram or Mermaid block.

**Image blocks**
- Two documented shapes: `{url, width, assetId, alignment, direction, aspectRatio}` for a monday asset, or `{publicUrl, width, alignment, direction}`.
- A community report says only `publicUrl` works; asset IDs and uploads fail [S27].

**Limits [S22]**
- Tables: at most 10 columns × 25 rows at creation. Dimensions are fixed afterwards.
- `create_doc_blocks` (API 2026-07 and later) creates at most 25 blocks per call.

**GraphQL [S23][S24]**
- `create_doc`.
- `add_content_to_doc_from_markdown(docId, markdown, afterBlockId)`. Which markdown syntax is supported is not documented.
- `import_doc_from_html(html, workspaceId, title, folderId, kind)`. Handles formatted text, emoji, quotes, tables, lists, code, dividers and headers; images are not listed.
- `export_markdown_from_doc(docId, blockIds)`.
- `duplicate_doc`, `update_doc_name`, `delete_doc`.
- Doc version history and diff (API 2026-04 and later).

**Platform MCP tools [S25][S26]**
- `create_doc`, and `read_docs` (`include_blocks` returns block IDs).
- `update_doc` takes up to 25 ordered operations per call: `set_name`, `add_markdown_content`, `update_block`, `create_block` (including image, table, layout, notice_box), `delete_block`, `replace_block`, `add_comment`.
  - It stops at the first failure.
  - Content nested inside a block created in the same call needs a second call.
- `get_asset_upload_url` and `finalize_asset_upload` attach a file to an item, not to a doc block.
- `all_monday_api`, `get_graphql_schema`, `get_type_details`.

**Consequence.** A diagram in a monday Doc needs a public image URL, and publishing a client's process diagram publicly is a confidentiality risk. Instead:
1. Use step tables plus a notice box that points to the PDF.
2. The user drags the PNGs into the Doc by hand (a close-out checklist item).
3. Optionally, attach the PDF and PNGs to an "Operating procedures" item using the asset tools. Unconfirmed: whether the file upload to the presigned URL can get out of the Cowork VM.

Clients can export a monday Doc to PDF, Word or Markdown themselves [S28].

#### (e) Anthropic's docx, pdf and pptx skills

**Availability and licence**
- Available in the Claude apps and in Cowork whenever code execution is on [S36].
- In Claude Code, available via `document-skills@anthropic-agent-skills`; the user's Claude Code already lists them [S30].
- Licence is source-available, not open source [S30]. The plugin names the skill and hands it content. It never copies skill text or scripts, which the clean-room rule also requires.

**docx [S31]**
- Builds files with docx-js (npm `docx`, preinstalled in Anthropic's sandbox).
- A table of contents needs built-in `HeadingLevel` headings.
- Every image needs an explicit `type`. SVG needs `type:"svg"` plus a `fallback` in PNG, JPG, GIF or BMP [S34].
- QA converts to PDF through a LibreOffice wrapper and renders the pages with pdftoppm.
- Word for Microsoft 365 renders SVG on Windows and Mac; Word 2013 and earlier do not; SVG editing works only in the desktop apps [S35].

**pdf [S32]**
- reportlab to create files; pypdf and qpdf to merge or split.
- No HTML-to-PDF path, so diagrams go in as raster images.

**pptx [S33]**
- pptxgenjs (preinstalled) to create decks.
- SVG icons are rasterized with sharp.
- A validation script, and LibreOffice → PDF → images for visual QA.

**Readiness by environment**
- **the user's Mac under Claude Code:** the skills' runtime is missing (`docx` module, soffice, pdftoppm), so they would either install packages or fail [local].
- **Cowork:** the preinstalled set looks right [S41], but a skill that tried `npm install` has failed there [S43].
- Probe before invoking.

### 2.3 Recommendation

- **Primary: (c).**
  - It is the only option that behaves the same in Cowork and on the Mac, with no network and no install.
  - It produces SVG that works in Office, lanes that match the SOP's roles table, and HTML or PDF with no JavaScript.
  - The same spec also feeds the step tables for the monday Doc and the Mermaid text.
- **Fallback 1 (better-looking where a browser exists):** option (a) on the Mac with the installed Chrome and pinned versions, fed by the Mermaid text that (c) emits. Alternatively, open the (b) HTML in a browser and print it.
- **Fallback 2 (always works):** step tables in every format, with the diagram left out and a note. The job log records why.
- **monday Docs (d):** text-first; images are added by hand only.
- **Office formats (e):** hand the file mechanics to the Anthropic skills once the probe passes.

| | (a) mmdc | (b) HTML + Mermaid | (c) stdlib SVG | (d) monday Doc | (e) skills |
|---|---|---|---|---|---|
| Works in Cowork offline | no / unconfirmed | viewer only | yes | text yes, images manual | likely (probe) |
| Works on the Mac today | yes, with Chrome | yes | yes | yes | needs installs |
| Install or download | about 270 MB npm, plus about 290 MB browser unless skipped | 3.6 MB vendored | none | none | preinstalled in sandbox |
| Safe to insert in Office | only with htmlLabels:false or PNG | n/a | yes | n/a | yes, needs PNG |
| Swimlane control | weak | weak | strong | – | – |
| Build effort | low | low | medium | low | low |

### 2.4 Flow spec sketch

```json
{
  "id": "job-intake", "title": "New job request to scheduled job",
  "kind": "swimlane", "solution_version": "v0.3",
  "lanes": [{"id": "office", "label": "Office coordinator"}, {"id": "pm", "label": "Project manager"}, {"id": "monday", "label": "monday (automatic)"}],
  "steps": [
    {"id": "s1", "lane": "office", "type": "start", "label": "Customer request received"},
    {"id": "s2", "lane": "office", "type": "task", "label": "Log the request", "procedure": "proc-log-request", "monday": {"board": "Jobs", "column": "Status", "value": "New"}},
    {"id": "s3", "lane": "monday", "type": "automation", "label": "Notify project manager"},
    {"id": "s4", "lane": "pm", "type": "decision", "label": "Enough detail?"},
    {"id": "s5", "lane": "pm", "type": "end", "label": "Job scheduled"}
  ],
  "edges": [{"from": "s1", "to": "s2"}, {"from": "s2", "to": "s3"}, {"from": "s3", "to": "s4"}, {"from": "s4", "to": "s5", "label": "Yes"}, {"from": "s4", "to": "s2", "label": "No"}]
}
```

- **Step types:** start, task, decision, automation, external (another system), end.
  - Automation steps get their own style, so clients see what monday does for them.
- **Second diagram kind:** `board-map`, generated from the board connections in build.json.
- **No notes field:** specs have no free-text field.
- **Files:**
  - `sop/diagrams/<id>.flow.json` is the source; `<id>.svg` and `.png` are generated. All three are current files.
  - Copies are frozen into `deliverables/vX.Y/` as history.

---

## 3. Handoff package

| Format | Role | Produce in Cowork | Produce on Mac (Claude Code) | Diagrams | Watch-outs |
|---|---|---|---|---|---|
| PDF | The approved record at each version | docx skill, then LibreOffice to PDF through its wrapper [S31]; or reportlab via the pdf skill [S32] | Chrome headless print of SOP.html with inline SVG [S15] | vector (Mac) or PNG | A4 or Letter per client; footer control notation; LibreOffice in the Cowork VM is unconfirmed |
| Word (.docx) | Copy the client can edit | docx skill [S31] | Several routes (see note below) | SVG plus required PNG fallback [S34] | Table of contents needs HeadingLevel headings; the user can check the file locally in Word [local] |
| monday Doc | Living copy inside the client's account | MCP `create_doc` plus `update_doc` (≤25 operations per call), or `import_doc_from_html` [S23][S26] | same | step tables; images added by hand | Tables ≤10×25. Markdown coverage is undocumented, so read back with `read_docs` or `export_markdown_from_doc` and diff. Record the doc ID in build.json. Keep the version out of the doc name; it lives in the control block. |
| HTML (optional) | Quick preview or print source | stdlib generator (inline SVG, no JavaScript) | same | inline SVG | Tiny and easy to archive |
| Slide deck (future) | Training or go-live briefing | pptx skill (pptxgenjs, sharp) [S33] | needs installs; the user has no PowerPoint or Keynote [local] | PNG | Derived from SOP.md, never a source |

**Word on the Mac: routes**
1. Install `docx` into `${CLAUDE_PLUGIN_DATA}`. Claude Code auto-installs a plugin's locked npm dependencies, without install scripts and with a 60-second timeout [S45]. Whether Cowork does the same is unconfirmed.
2. Open SOP.html in Word and use Save As.
3. `textutil -convert docx` also exists, but it is lossy and its image handling is unverified [local].

**Future deck outline.** Generated entirely from confirmed SOP sections, with speaker notes taken from the procedures:
1. Title and version
2. What changes, per role
3. One slide per process diagram
4. Board tour, one slide per board, in business terms
5. Automations that save work
6. Go-live checklist
7. Getting help and requesting changes

**Package by milestone**
- **v0.x:** an optional draft PDF, watermarked.
- **v1.0:** PDF, Word, monday Doc, diagrams (SVG and PNG) and change log. `deliverables/v1.0/manifest.json` records file names, hashes, the monday doc ID and URL, and the lint and audit results.
- **v1.x:** before editing the monday Doc, pull its version history (or `export_markdown_from_doc`) and diff it against the last delivery to catch edits the client made [S23]. Then regenerate and redeliver.
- **Close-out:** hand over the final v1.x package. The one-page client card records the delivered version and where each copy lives.
- **File naming:** `<slug>-operating-procedures-v1.0-2026-09-10.pdf`.

**Export pipeline.** Each step blocks the next if it fails.
1. Freeze the version and the section statuses.
2. Compare a live read against build.json (drift guard).
3. Regenerate diagrams and check their monday references.
4. Run the leak lint on SOP.md.
5. Run the capability probe, then render the formats.
6. Extract text from the outputs and lint again. For docx, unzip `word/document.xml` with the stdlib; for monday, use `read_docs`.
7. Read-only auditor review.
8. Write the versions/ entry, the log.md line and the manifest.

---

## 4. Capability probe

Run this first. Every check is read-only.

**Checks**
- **Runtimes:** `python3 --version`, `node --version`.
- **Binaries:** `command -v soffice pdftoppm pandoc convert magick dot rsvg-convert`.
- **Node modules:** `node -e "require.resolve('docx')"`, and the same for `sharp` and `pptxgenjs`.
- **Python:** `python3 -c "import yaml"`.
- **Browsers:** `test -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"`, and look for `/opt/pw-browsers/chromium*` [S40].

**Selection order [inferred]**
- **PNG rasterizer:**
  1. sharp, which reads SVG [S46]
  2. ImageMagick
  3. `soffice --convert-to png`
  4. Chrome `--screenshot --window-size=W,H` on a one-image HTML wrapper [S15]
  5. none: Word diagram images are turned off, with a note saying why
- **PDF:**
  1. Chrome print (Mac)
  2. docx skill plus LibreOffice
  3. pdf skill
  4. give the user the HTML to print
- **Word:**
  1. docx skill
  2. otherwise skip it, with a note

Record the chosen path in log.md.

**Escape hatch to evaluate later [unconfirmed]**
- A plugin-bundled stdio MCP server, written in plain Node with no dependencies.
- In local sessions it would run on the host [S37], so it could drive the host's Chrome for printing and screenshots from Cowork.
- Costs: extra security surface, and no support in cloud sessions.

---

## 5. Scenario tests to build

- **Leak trap:**
  - Seed discovery.md, calls/ and a blueprint `### Internal` block with marker phrases: a budget figure, "champion", a competitor name.
  - No output format may contain any of them.
- **Status gating:**
  - Include one `planned` section.
  - The v0.3 draft shows it only under "Coming next".
  - The v1.0 export is refused and names the section.
- **Drift:**
  - Rename a status label on the live board.
  - The export stops and lists the label, the board and where the SOP mentions it.
- **Diagram set:**
  - Build a diagram with 5 lanes, 2 decisions, a rework loop and 60-character labels.
  - Inserted into Word 365, the SVG shows all its text.
  - Output is byte-identical across runs and between Python 3.9 and 3.10.
- **Environment matrix:**
  - Cowork with npm blocked still produces PDF or HTML, plus the monday Doc text.
  - Claude Code on the Mac produces a Chrome-printed PDF and PNGs.
  - With no rasterizer, Word is produced without images and with a visible note.
- **monday Doc:**
  - A 60-block SOP is created correctly through chunked `update_doc` calls.
  - An 11-column table is split before sending.
  - The read-back diff is empty.
- **Mermaid fallback:**
  - mmdc with `PUPPETEER_SKIP_DOWNLOAD` and the system Chrome renders without writing `~/.cache/puppeteer`.
  - An SVG made with `htmlLabels:false` shows its text in Word.

---

## Sources

- S1. EPA, *Guidance for Preparing Standard Operating Procedures (EPA QA/G-6)*, EPA/600/B-07/001, April 2007. https://www.epa.gov/sites/default/files/2015-06/documents/g6-final.pdf (landing page: https://www.epa.gov/quality/guidance-preparing-standard-operating-procedures-epa-qag-6-march-2001)
- S2. Diátaxis. https://diataxis.fr/
- S3. Google developer documentation style guide, Procedures. https://developers.google.com/style/procedures
- S4. Digital.gov, Principles of plain language. https://digital.gov/guides/plain-language/principles
- S5. Keep a Changelog 1.1.0. https://keepachangelog.com/en/1.1.0/
- S6. Semantic Versioning 2.0.0. https://semver.org/
- S7. Responsibility assignment matrix (RACI). https://en.wikipedia.org/wiki/Responsibility_assignment_matrix ; https://www.atlassian.com/work-management/project-management/raci-chart
- S8. Swimlane. https://en.wikipedia.org/wiki/Swimlane
- S9. mermaid-cli README. https://github.com/mermaid-js/mermaid-cli
- S10. mermaid-cli, Linux sandbox issue. https://github.com/mermaid-js/mermaid-cli/blob/master/docs/linux-sandbox-issue.md
- S11. npm registry metadata via `npm view`, 2026-09-10: @mermaid-js/mermaid-cli, puppeteer, mermaid, @mermaid-js/layout-elk, @mermaid-js/mermaid-zenuml, @zenuml/core, @fortawesome/fontawesome-free, beautiful-mermaid, @viz-js/viz, elkjs, docx. https://www.npmjs.com/package/@mermaid-js/mermaid-cli
- S12. Puppeteer, Installation. https://pptr.dev/guides/installation
- S13. Puppeteer, Configuration. https://pptr.dev/api/puppeteer.configuration
- S14. Chrome for Testing, last known good versions (zip sizes read with HTTP HEAD). https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
- S15. Chrome Headless command-line reference. https://developer.chrome.com/docs/automation-and-testing/headless-cli ; https://developer.chrome.com/docs/chromium/headless
- S16. Mermaid flowchart syntax. https://mermaid.js.org/syntax/flowchart.html
- S17. Mermaid config schema (root `htmlLabels`; diagram-level setting deprecated). https://mermaid.js.org/config/schema-docs/config.html
- S18. Mermaid issue #7021, SVG text missing in Inkscape and PowerPoint. https://github.com/mermaid-js/mermaid/issues/7021 ; mermaid-cli issue #112: https://github.com/mermaid-js/mermaid-cli/issues/112
- S19. jsDelivr mermaid bundles, sizes measured. https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js
- S20. beautiful-mermaid. https://github.com/lukilabs/beautiful-mermaid
- S21. viz-js. https://github.com/mdaines/viz-js
- S22. monday API, Blocks. https://developer.monday.com/api-reference/reference/blocks
- S23. monday API, Docs. https://developer.monday.com/api-reference/reference/docs
- S24. monday API, Export markdown from doc. https://developer.monday.com/api-reference/reference/export-markdown-from-doc
- S25. monday Platform MCP tools. https://developer.monday.com/api-reference/docs/platform-mcp-tools
- S26. monday Platform MCP, update_doc. https://developer.monday.com/api-reference/docs/update-doc
- S27. monday Community, Add images to monday doc using API. https://community.monday.com/t/add-images-to-monday-doc-using-api/121390
- S28. monday Support, Share and export your workdocs. The page returned 403 to the fetcher, so its content comes from the search result summary. https://support.monday.com/hc/en-us/articles/8563692121746-Share-and-export-your-workdocs
- S29. monday Support, User types explained; Permissions on monday.com (search result summaries). https://support.monday.com/hc/en-us/articles/360002144900-User-types-explained ; https://support.monday.com/hc/en-us/articles/360019222479-Permissions-on-monday-com
- S30. anthropics/skills README (document skills are source-available). https://github.com/anthropics/skills
- S31. anthropics/skills, docx SKILL.md. https://github.com/anthropics/skills/blob/main/skills/docx/SKILL.md
- S32. anthropics/skills, pdf SKILL.md. https://github.com/anthropics/skills/blob/main/skills/pdf/SKILL.md
- S33. anthropics/skills, pptx SKILL.md. https://github.com/anthropics/skills/blob/main/skills/pptx/SKILL.md
- S34. docx-js ImageRun source (SVG requires a fallback). https://github.com/dolanmiu/docx/blob/master/src/file/paragraph/run/image-run.ts
- S35. Microsoft Support, Edit SVG images in Microsoft 365. https://support.microsoft.com/en-us/office/edit-svg-images-in-microsoft-365-69f29d39-194a-4072-8c35-dbe5e7ea528c
- S36. Claude Help Center, What are skills? https://support.claude.com/en/articles/12512176-what-are-skills
- S37. Claude Help Center, Claude Cowork architecture overview. https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
- S38. Claude Help Center, Use Claude Cowork safely. https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
- S39. Claude Help Center, Create and edit files with Claude (network egress). https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- S40. Claude Platform docs, Cloud sandbox reference (Managed Agents). https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference
- S41. P. Vieito, Inside Claude Cowork (January 2026). https://pvieito.com/2026/01/inside-claude-cowork
- S42. Pluto Security, Inside Claude Cowork (April 2026). https://pluto.security/blog/inside-claude-cowork-how-anthropics-autonomous-agent-actually-works/
- S43. anthropics/claude-code issue #43334, npm registry blocked in the Cowork sandbox. https://github.com/anthropics/claude-code/issues/43334
- S44. anthropics/claude-code issue #51400, Cowork egress additional domains not enforced. https://github.com/anthropics/claude-code/issues/51400
- S45. Claude Code plugins reference (`${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, dependency install). https://code.claude.com/docs/en/plugins-reference
- S46. sharp (reads SVG input). https://sharp.pixelplumbing.com/
