# Dossier: client research method and client record engineering

Prepared 2026-09-10 for monday Master Builder (DelOps). Clean-room research: no material from the old plugin was read or used.
All web sources were accessed on 2026-09-10. Numbers in square brackets point to the source list at the end.

Labels used in this file:
- **Found**: the cited source says this.
- **Tested**: I ran it on the user's Mac today (python3 3.9.6, PyYAML 6.0.3, jsonschema 4.25.1, gh 2.100.0, git 2.50.1).
- **Inferred**: my recommendation for the build, based on the Found and Tested items. Budgets and thresholds marked Inferred are starting values to tune with scenario tests.

---

## Part A. Client research method

### A1. What Cowork's web tools can and cannot do

Found:
- Cowork has web search and web fetch. Web fetch runs on Anthropic's servers and only opens URLs that came from search results or that the user shared [1][2].
- The API version of web fetch has the same rule. It cannot open a URL that appears only in Claude's own output or only in the system prompt [4]. Whether URLs written into a plugin skill count as "shared" in Cowork is not documented (see Not confirmed).
- Web fetch does not handle pages built by JavaScript. Those need a real browser [4].
  - Cowork on desktop includes a built-in browser [2].
  - Claude in Chrome acts inside the user's own browser, with their logged-in sessions. It is available on Max and Team plans and rolling out to Pro [2].
  - Since 2026-08-12 the Chrome side panel runs a full Cowork session, saved to history and synced across devices [3].
- Fetch results come with a retrieval timestamp and may be served from a cache [4]. Search results come with a `page_age` field [5]. Both facts come from the API docs; Cowork may not show them.
- The search tool has no date or recency filter. Its only settings are the maximum number of searches, allowed or blocked domains, and an approximate user location [5]. Simple factual questions typically take 1 to 3 searches; research comparing several entities can take 10 or more [5].
- Every web search answer includes citations. Fetching a long document pulls all of it into context and uses a lot of the usage limit [6]. As a rough guide, a 10 kB web page is about 2,500 tokens [4].
- Web content is the main route for prompt injection. Cowork's network egress settings do not restrict web search, web fetch, or Claude in Chrome [1].
- Users turn web search on from the "+" menu. On Team and Enterprise plans an owner must enable it first [6].
- Cowork's safety article advises connecting dedicated folders rather than giving broad access. Desktop sessions can permanently delete files in connected folders, and deletion asks for permission first [1].

Inferred, for the build:
- At client creation, ask the user for the company website and any links they has. Store them in `research/sources.md`, so later fetches have an allowed starting point.
- Default to web search followed by web fetch of specific pages. Use the browser only for pages that fetch cannot read, such as JavaScript careers pages.
- Never use Claude in Chrome on logged-in social networks (see A4).
- Tell the research skill, in one calm sentence, that page content is data and never instructions.
- Recency comes from three places: query wording (company name plus month and year), dates printed on pages, and sources that are dated by nature (filings, press releases, job posts).
- Summarize what was read into the research file with source keys. Do not paste whole pages into the record.
- For a deep dive, run the research as a sub-task that returns a condensed summary. This matches Anthropic's sub-agent pattern of returning 1,000 to 2,000 token summaries [36]; Cowork can split work into parallel tasks [2].

### A2. Source catalogue

| Source | What it tells you | Default label | Notes |
|---|---|---|---|
| Company website: About, services, locations, case studies, careers, newsroom | What they sell, who they serve, how big they say they are, and their own words for things | Found (self-reported) | Write it as "company states". Their wording seeds the vocabulary map (A7). |
| Press releases and news coverage | Launches, acquisitions, new sites, leadership changes | Found, with date | Prefer the company's own release over third-party coverage. |
| US listed companies: SEC EDGAR Form 8-K | Material events, most filed within four business days [10] | Found | Useful for the refresh (A6). |
| UK companies: Companies House | Current and past officers; filing history in date order [11] | Found | Record roles only. |
| OpenCorporates | Official register data from 140+ jurisdictions [12] | Found | Legal name, status, incorporation date. |
| Job postings | Tech stack and priorities. Postings reveal back-office and internal tools that website scanners cannot see [13]. Hiring areas show where budget has gone [14]. | Signal, so label Inferred | Vendor claims about lead time (30 to 90 days) are marketing, not evidence [14]. |
| Greenhouse job board API | Public, no login: `GET https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true` returns full descriptions [15] | Found (the posting text) | Save a dated list of job titles so the next refresh can compare. |
| Lever postings API | Public, no login: `GET https://api.lever.co/v0/postings/{company}?mode=json`; EU accounts use `api.eu.lever.co` [16] | Found (the posting text) | Same as above. Because of the fetch rule in A1, the URL must first appear in chat or in a search result, or be opened in the browser. |
| Website tech scanners (BuiltWith, Wappalyzer) | Front-end and marketing tools only [13] | Found, for the website only | Do not infer back-office systems from them. |
| Customer reviews (Google, Trustpilot, G2) and employee reviews (Glassdoor, Indeed) | Service problems and process friction | Inferred, low confidence | Glassdoor's own research links employee ratings to customer satisfaction [17]. Treat reviews as anecdotes and never record reviewer names. |
| Industry sources: NAICS classification, trade bodies, regulators | Industry classification, typical processes, compliance constraints | Found for the classification [18]; Inferred for "companies like this usually..." | |

### A3. Citing with dates, and marking found versus inferred

Found:
- US intelligence analytic standards (ICD 203) require keeping source information separate from the analyst's assumptions and judgments. Assumptions that an argument depends on must be stated explicitly [19].
- Anthropic's guidance on reducing hallucinations:
  - Let Claude say it does not know.
  - Ground answers in direct quotes.
  - Check every claim against a source, and remove claims that have no support [20].
- For complex research, Anthropic suggests tracking competing hypotheses and confidence levels in notes [21].
- APA style adds a retrieval date only for pages that are designed to change and are not archived [22]. Most business pages (careers, about, pricing) are exactly that kind of page.
- Dates written year-month-day in one format sort correctly as plain text [23].

Inferred convention:
- Each research claim is one bullet that carries a label and a source key:
  - `[F]` for found.
  - `[I]` for inferred, with the keys it rests on and a confidence word (high, medium, or low).
  - `[Q]` for a client quote, verbatim, with the call file and the speaker's role.
- The source register in `research/sources.md` only grows, and keys are never renumbered. Each entry records the key, title, publisher, URL, date published (or "undated"), and date accessed.
- The validator rejects any `[F]` or `[I]` line in research files that has no source key.
- Example, using a made-up client:
  ```
  - [F] Opened a second warehouse in Leeds (S3, published 2026-06-02, accessed 2026-09-10).
  - [I] Probably still tracks stock in spreadsheets (S5 job post, S7 review). Confidence: medium.
  - [Q] Ops lead, calls/2026-09-08-discovery.md: "every Monday we rebuild the dispatch sheet"
  ```

### A4. Privacy limits: public, professional information only

Found:
- GDPR Article 5 principles: purpose limitation, data minimisation, accuracy, storage limitation, integrity, and accountability [24].
- Personal data that is publicly available is still covered by GDPR. B2B prospecting usually relies on legitimate interest, which needs a documented balancing test (secondary source) [25].
- The UK regulator (ICO) says to consider what people would reasonably expect. People are less likely to expect uses of data collected from other sources than from themselves [26].
- Special category data includes racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic and biometric data, health, sex life, and sexual orientation [27].
- LinkedIn does not permit crawlers, bots, or extensions that scrape or automate activity on its site, under section 8.2 of its User Agreement [28].

Inferred rules for the research skill:
- Research the organisation, not the people in it.
- For a person, record only name, job title, and role in the engagement. Take these from the company site, press, filings, or what the client says in calls.
- Never record personal social media, home details, family, health, politics, religion, personal finances, photos, or anything in the special categories.
- If a search turns up personal content, leave it out and do not mention it.
- No LinkedIn automation or scraping. The user can look at LinkedIn themselves and tell Claude what matters.
- Keep only what serves the engagement. At close-out, the client card keeps only the main contact's name and role.

### A5. Research depth tiers

Found:
- HubSpot (updated 2026-03-16) recommends two stages: a planning worksheet one to two days before the call, then a 15-minute review just before it [29].
- A sales vendor puts focused preparation for most B2B discovery calls at 10 to 15 minutes, with little extra value beyond about 15 minutes per account [30].
- Simple lookups take 1 to 3 searches; research across several entities takes 10 or more [5].

Inferred tiers:

| Tier | When | Search and fetch budget | Output |
|---|---|---|---|
| Quick brief | Before the first call; for small clients | Up to about 8 searches and 5 fetches | `research/YYYY-MM-DD-brief.md`, at most 1 page. Covers: what they do; size and locations; 3 to 5 dated recent events; likely monday use cases `[I]`; vocabulary seeds; 5 questions to ask. |
| Deep dive | Before the blueprint, or for multi-department or regulated clients | Up to about 25 searches and 15 fetches, run as a sub-task | `research/YYYY-MM-DD-deep-dive.md`, at most 3 pages. Adds: departments; systems signals from job posts; industry processes and compliance; competitors; risks; open questions. |
| Refresh | Before every later meeting | Up to about 5 searches | A dated section appended to `research/updates.md` (see A6). |

### A6. "What's new since the last meeting" refresh

Found: the building blocks.
- `page_age` on search results [5], and cached fetches with `retrieved_at` [4].
- 8-K filings arrive within four business days of the event [10].
- Companies House filing history is listed in date order [11].
- Cowork scheduled tasks can run in the cloud with no device online [2]. However, projects tied to a local folder support Cowork sessions on desktop only [8].

Inferred flow:
1. Set the cutoff to the later of `last_researched` (CLIENT.md front matter) and the date of the most recent call in `log.md`.
2. Check dated sources only:
   - the company newsroom and press releases
   - filings (EDGAR or Companies House)
   - news searched with the company name plus the month and year
   - the job-postings list compared with the saved snapshot
3. Keep items dated after the cutoff. Mark undated items "undated, first seen YYYY-MM-DD".
4. Record the results:
   - Append a dated section to `research/updates.md`, which is a history file.
   - Rewrite the "Recent" block in CLIENT.md with the top three items.
   - Set `last_researched`.
5. If nothing new turned up, say "nothing new found" explicitly rather than padding.
6. A scheduled cloud refresh cannot write into a local-folder project unless the desktop app is open (see Not confirmed). Start with a refresh run by hand at the start of each meeting chat.

### A7. Vocabulary map: the client's words to monday objects

Found:
- Ubiquitous language (from domain-driven design) means one shared, precise vocabulary between domain experts and builders, refined as understanding grows [31].
- monday boards are made of groups of items. Each board can rename "item" to the client's own term (for example "book"), and the board then offers "New book" [32].
- In the monday API:
  - `item_terminology` is a read-only field on boards.
  - `item_nickname` can be set through `create_board`, and through `update_board` from API version 2026-04 [33].
  - Item IDs have the GraphQL `ID!` type [34].
- Anthropic's skill guidance: pick one term and use it consistently [35].

Inferred:
- Keep the map as a table in `discovery.md`, which is a current file, and copy the top terms into CLIENT.md. Columns:
  1. Their term
  2. Verbatim quote with call file
  3. What it means
  4. monday object
  5. Name used in the account
  6. Status: confirmed or assumed
- Starting mapping categories. These are assumptions to confirm by inspecting the live account, not rules:

  | Their concept | monday object |
  |---|---|
  | A kind of record (job, order, client, asset) | A board, with the item nickname set to their word |
  | A property of the record | A column |
  | A workflow state | Status labels |
  | A bucket or phase | A group |
  | A checklist step | A subitem |
  | An intake | A form |
  | A report | A dashboard |

- Use their words in the account (board names, item nickname, status labels) and in the SOP. Keep monday's own terms for internal files.
- Terms that are ambiguous or used two ways go onto the question list for the next call.

---

## Part B. Client record engineering

### B1. Anthropic guidance, condensed

Found:
- **Context engineering** (2025-09-29) [36]:
  - Keep lightweight references (paths, URLs) and load the data only when needed.
  - Let the agent discover context step by step; file names, sizes, and timestamps signal what matters.
  - Compaction keeps decisions and open issues and drops redundant tool output. Tune it for recall first, then precision.
  - Structured notes written to files outside the context window act as memory.
  - Sub-agents return condensed summaries.
- **Memory tool** [37]:
  - Claude checks its memory directory before starting work.
  - For work spanning many sessions: a first session sets up a progress log and a checklist. Each later session reads them first and updates them before ending.
  - Mark work done only after end-to-end verification.
  - Cap file sizes and let Claude page through long files. Periodically delete files that have not been used in a long time. Strip sensitive data before writing.
  - `view` truncates text files longer than 16,000 characters.
- **Claude Code memory** [38]:
  - Aim for under 200 lines per CLAUDE.md. Files load in full every session up to 4 MiB, and longer files reduce adherence.
  - The auto-memory index `MEMORY.md` loads only its first 200 lines or 25 KB, one line per entry. Topic files are read when needed.
  - When Claude writes a memory file that has front matter, the harness adds a `modified` ISO timestamp.
  - The project-root CLAUDE.md is re-read after compaction. HTML block comments are stripped before loading.
  - In Cowork sessions, imports in user-level memory files that point outside the working folder are skipped.
- **Skill authoring** [35]:
  - Keep the SKILL.md body under 500 lines.
  - Reference files should link directly from SKILL.md, one level deep. Claude may preview nested files with a partial read.
  - Add a table of contents to reference files longer than 100 lines.
  - Use descriptive file names and forward slashes.
  - Use plan, then validate, then execute, with a validator that gives specific error messages.
  - Write at least three evaluations and test with every model you plan to use.
- **Long-running agents** (2025-11-26) [39]:
  - Keep feature lists in JSON; the model is less likely to wrongly overwrite JSON than Markdown.
  - Use git commits as recovery points.
  - Each session starts by reading the progress notes and the git log.
- **Prompting best practices** [21]:
  - Structured formats such as JSON for state; free text for progress notes; git for tracking state.
  - A fresh context that rediscovers state from files can work better than compaction.
  - Replace "CRITICAL: You MUST use this tool" with a plain "Use this tool when...", and explain why an instruction matters.
- **Context editing plus memory** (2025-09-29): 39% better than baseline on an internal Anthropic evaluation. In a 100-turn web search evaluation, context editing cut token use by 84% [40].

Inferred, mapped to the product:
- **CLIENT.md is the index** (like MEMORY.md): short, read first, pointing to other files by relative path.
- **A new chat per meeting is a fresh context.** Its first step reads CLIENT.md, the latest entries in `log.md`, and only the files that meeting needs. Aim for about 10k tokens or less before work begins.
- **`build.json` is the machine state** (every monday ID), checked against a schema. Markdown holds the narrative.
- **`log.md` is the progress log.**
- **Consider a local git repo in each client folder from day one**, committing at the end of each meeting and each version. That gives checkpoints, makes the append-only rule checkable, and turns close-out into a push. Git works on the host; whether it works inside Cowork is not confirmed.

### B2. Current files versus history files

Found:
- Architecture decision records are numbered, never edited, and marked superseded instead [41].
- Keep a Changelog: newest entry first, ISO dates, and an "Unreleased" section that moves under a version number at release [42].
- The memory tool's multi-session pattern pairs a progress log with a checklist [37].
- Claude may preview a file with a partial read from the top [35].

Inferred rules:

| Path | Kind | Rule |
|---|---|---|
| `CLIENT.md` | current | Rewrite. About 2 pages. |
| `research/YYYY-MM-DD-brief.md`, `research/YYYY-MM-DD-deep-dive.md` | snapshot | New file per run; frozen once written. |
| `research/sources.md` | history | Append only; keys never reused. |
| `research/updates.md` | history | Append dated sections. |
| `calls/YYYY-MM-DD-<meeting>.md` (summary) | snapshot | Frozen after the meeting. Corrections go in a dated note at the end. |
| `calls/YYYY-MM-DD-<meeting>.transcript.txt` | raw | Never edited (except redaction, see B8). |
| `discovery.md` | current | Rewrite. Holds confirmed answers with call references, open gaps, and the vocabulary map. |
| `solution/blueprint.md` | current | Rewrite. A frozen copy goes to `versions/` at each release. |
| `solution/build.json` | current (machine) | Rewrite through a checked write only; never merge by hand. |
| `solution/backlog.md` | current | Rewrite. |
| `versions/vX.Y/` | snapshot | Frozen at release: blueprint, build.json, demo script, archived history. |
| `sop/SOP.md`, `sop/diagrams/` | current, client-facing | Rewrite. No internal notes. |
| `deliverables/` | snapshot | Exact files sent to the client. |
| `log.md` | history | Append only, newest first under a fixed header, one dated entry per event. |

- Newest-first works well here: a partial read from the top shows the latest entries.
- The append-only check: the previous file body, below the header, must still appear unchanged at the end of the new file. The check compares against the last commit, or a saved copy if the folder has no git.

### B3. Size budgets and condensing at version boundaries

Found anchors:
- CLAUDE.md: under 200 lines.
- MEMORY.md: loads 200 lines or 25 KB.
- SKILL.md: under 500 lines; table of contents above 100 lines.
- Memory tool `view` truncates at 16,000 characters.
- About 2,500 tokens per 10 kB of text.

Sources: [38][35][37][4].

Inferred budgets, which the validator should warn about rather than block:

| File | Budget | When over |
|---|---|---|
| `CLIENT.md` | 150 lines or less, 8 KB or less (about 2 pages, about 2k tokens) | Move detail into linked files. |
| `discovery.md` | 250 lines or less | Drop resolved items; keep answers with call references. |
| `solution/blueprint.md` | 400 lines or less, with a table of contents at the top | Move appendices into a linked file. |
| `solution/backlog.md` | 150 lines or less | Move shipped items into version notes. |
| `log.md` (live part) | 200 lines or less | Condense at the next version. |
| `research/updates.md` (live part) | 150 lines or less | Condense at the next version. |
| Call summary | 120 lines or less | Keep only decisions, requirements, quotes, and open questions. |
| Transcripts | No limit | Never loaded whole by default; search them for quotes. A one-hour call is roughly 10 to 12k tokens (estimate). |
| `sop/SOP.md` | No hard limit | Table of contents; one section per process. |
| `build.json` | No line limit | Must pass the schema. |

Inferred condensing procedure when version vX.Y is released:
1. **Freeze.** Copy `solution/blueprint.md`, `solution/build.json`, the demo script, and a backlog snapshot into `versions/vX.Y/`.
2. **Roll the history.** Move `log.md` and `research/updates.md` entries older than this release into `versions/vX.Y/log.md` and `versions/vX.Y/updates.md`. Leave one summary entry in each live file, for example: "vX.Y released on date; N entries moved to versions/vX.Y/log.md". Nothing is lost; the live file stays small.
3. **Rewrite the current files.** Update CLIENT.md (status, version, next steps), discovery.md (drop resolved gaps), and backlog.md (drop shipped items).
4. **Recall first.** Before removing a line from a current file, confirm the fact survives in a frozen snapshot, the log, or a call summary [36].
5. **Check and commit.** Run the validator (sizes, links, front matter, build.json), then commit if the folder uses git.

### B4. File formats and validation with PyYAML and jsonschema

Found and Tested:
- `yaml.load` is as powerful as pickle and unsafe on untrusted input. Use `yaml.safe_load` [43].
- YAML 1.1 treats `y/n/yes/no/on/off/true/false`, in any common casing, as booleans [44].
- Tested with PyYAML 6.0.3 and `safe_load`:
  - `region: NO` becomes `False`.
  - `updated: 2026-09-10` becomes a `datetime.date` object.
  - `version: 0.10` becomes the float `0.1`, so version 0.10 silently turns into 0.1.
  - A schema expecting strings rejects all three.
- Tested fix: a safe loader without the timestamp rule keeps dates as strings. Versions and yes/no-like words must still be quoted.
  ```python
  import yaml

  class FrontMatterLoader(yaml.SafeLoader):
      """Safe loader that leaves dates as plain strings."""

  FrontMatterLoader.yaml_implicit_resolvers = {
      ch: [(tag, rx) for tag, rx in rs if tag != "tag:yaml.org,2002:timestamp"]
      for ch, rs in yaml.SafeLoader.yaml_implicit_resolvers.items()
  }
  # yaml.load(text, Loader=FrontMatterLoader) -> {'updated': '2026-09-10', ...}
  ```
- **jsonschema version.** The Mac has 4.25.1. The next release, 4.26.0 (2026-01-07), requires Python 3.10 or newer [45]. So 4.25.1 is the ceiling on this Mac's Python 3.9.6. Scripts must also avoid syntax newer than 3.9, such as `match` and `X | Y` type unions evaluated at runtime.
- **Validation API** [46]:
  - Use `Draft202012Validator` with `check_schema` for the schema itself.
  - Use `iter_errors` to report every error, not just the first.
  - Format keywords are not enforced unless a `FormatChecker` is passed.
  - Tested: with `FormatChecker()`, this install catches bad `date`, `date-time`, and `uri` values. The set of checked formats depends on optional packages, so print `FormatChecker().checkers` on any other machine.
  ```python
  from jsonschema import Draft202012Validator, FormatChecker
  Draft202012Validator.check_schema(schema)
  v = Draft202012Validator(schema, format_checker=FormatChecker())
  for e in sorted(v.iter_errors(doc), key=lambda e: list(e.path)):
      # file_path = the record file being checked
      print(f"{file_path}: {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
  ```
- JSON is less likely than Markdown to be wrongly overwritten by the model, which suits `build.json` [39]. YAML front matter is a convention popularised by Jekyll [47].

Inferred format decisions:
- **Markdown files** carry a small front matter block: 8 keys or fewer, every value quoted, a `schema` key for future migrations. Example for CLIENT.md, using a made-up client:
  ```yaml
  ---
  schema: "client/1"
  slug: "acme-logistics"
  name: "Acme Logistics Ltd"
  status: "building"            # prospect | discovery | building | live | closed
  version: "0.3"
  updated: "2026-09-10"
  last_researched: "2026-09-02"
  transcripts_retain_until: "2027-09-30"
  ---
  ```
- **Call summary front matter:** `date`, `type`, `transcript` (relative path), `recording_link`, `recording_consent` (`"yes"`, `"no"`, or `"unknown"`, always quoted).
- **`build.json`** has a top-level `schema_version`, `client_slug`, `version`, `updated_at`, `monday_api_version`, `verified_at`, plus arrays of workspaces, boards (with groups and columns), docs, dashboards, forms, and anything else built.
  - Store every monday ID as a string, exactly as returned, together with its name. GraphQL `ID` values arrive as strings; this was not checked on every endpoint.
  - Use `additionalProperties: false` on object definitions, so a typo becomes an error instead of passing silently.
- **Validator script** (standard library plus PyYAML and jsonschema only) checks:
  - front matter against a schema chosen by file type
  - that required files exist
  - size budgets (warnings)
  - that relative links resolve
  - no absolute paths such as `/Users/`
  - no internal-only sections in `sop/` or `deliverables/`
  - the append-only rule on history files (B2)
  - that `[F]` and `[I]` lines have source keys
  - `build.json` against its schema
  - Every message names the file, the field, the problem, and what is expected [35].

### B5. Naming conventions

Found:
- Year-month-day dates sort chronologically as text when the format is consistent [23]. Keep a Changelog uses ISO dates [42].
- A standard slug rule: convert to ASCII, lowercase, drop characters other than letters, digits, underscores, hyphens, and spaces, turn spaces and repeated dashes into one dash, and trim [48].
- Use descriptive file names and forward slashes [35].

Inferred:
- **Client slug:** slug of the common company name without legal suffixes (ltd, inc, gmbh). At most 40 characters, matching `^[a-z0-9]+(-[a-z0-9]+)*$`. Never renamed once created, because it is the folder name, the Cowork project, and the repo name.
- **Dated files:** `YYYY-MM-DD-<topic-slug>.<ext>`. A second file on the same day gets `-2`.
- **Call pairs share a stem:** `calls/2026-09-08-discovery.md` and `calls/2026-09-08-discovery.transcript.txt`.
- **Versions:** `versions/v0.1/`, `versions/v1.0/`, `versions/v1.1/`. Always quote version strings in YAML.
- **Archive repo:** `client-<slug>`, private, on the user's GitHub account.

### B6. Self-contained client folders and later sharing

Found:
- **Cowork projects** can start from scratch, be imported from a chat project, or wrap an existing local folder [7]:
  - New Cowork projects are saved to the Claude account and available on other devices.
  - Projects made from an existing folder stay local to that computer.
  - Memory is scoped to one project.
  - Team and Enterprise plans can share projects with "Can view" or "Can edit" access.
  - Projects exist only in Cowork, not in Claude Code.
- Projects tied to a local folder support Cowork sessions on desktop only [8].
- Cloud sessions are the default. They reach local files only through the desktop app, only in connected folders, and only while the app is open [9][8].
- **GitHub personal accounts:** a collaborator gets access to the whole repository, and in a private repo that means write access. Finer control needs an organization [49]. GitHub Free allows unlimited private repos and collaborators [50].

Inferred:
- Every link inside a client folder is relative. No absolute paths, no references to plugin files, no references to other clients.
- CLIENT.md opens with a five-line map of the folder, so a teammate without the plugin can navigate it.
- Client-facing content lives only in `sop/` and `deliverables/`, with no sales notes, so those folders can be shared alone.
- Connect only `~/DelOps/monday-master-builder-dev/clients/<slug>` to that client's Cowork project, never all of `~/DelOps` [1].
- Sharing later works per repo. Inviting a teammate to `client-<slug>` exposes one client; one repo for all clients would expose every client.
- Consequence of wrapping `~/DelOps/monday-master-builder-dev/clients/<slug>` as the Cowork project: it is desktop-only, not synced, and cannot use Cowork's own project sharing. The files on disk, backed by GitHub, are the record. This is a deliberate trade-off (see Open questions).

### B7. Archiving to a private GitHub repo with gh

Found and Tested:
- **Create:** `gh repo create <name> --private --source <dir> --push [--description ...] [--disable-issues] [--disable-wiki]` [51].
- **Archive and unarchive:** `gh repo archive [<repo>] [-y]` and `gh repo unarchive [<repo>]` both exist in gh 2.100.0 (Tested). An archived repo is read-only and can be unarchived later [52].
- **Clone:** `gh repo clone <owner/repo> [<dir>]` (Tested).
- **Delete needs an extra permission.** `gh repo delete` requires the `delete_repo` scope. The user's gh token has only `gist`, `read:org`, `repo`, `workflow` (Tested), so the plugin cannot delete a remote repo by accident.
- **Initial branch:** git 2.50.1 supports `git init -b main` (Tested).
- **Size limits:** Git warns above 50 MiB per file; GitHub blocks files above 100 MiB. Keep repos under 1 GB; under 5 GB is strongly recommended [53].
- **Ignore rules:** `.gitignore` does not affect files already tracked (use `git rm --cached`). `git check-ignore` shows which rule applies [54].
- **Removing a file after it was pushed** means rewriting history with git-filter-repo. Clones and forks keep copies, and GitHub Support must clear cached views [55]. So exclusions and redaction must be settled before the first commit.
- **GitHub staff access:** staff do not open private repo content except for automated or manual scanning for vulnerabilities, malware, or terms violations; for support the owner asked for; or to meet legal obligations [56].

Inferred decision: **one private repo per client.**
- Access is granted per repo.
- Retention and deletion can be handled per client.
- Restore is a single clone.
- Each repo stays small.
- The only cost is many repos, which the `client-` prefix handles.
- A single all-clients repo only makes sense if nobody else will ever be given access and every client can share one retention policy.

Inferred `.gitignore` for each client folder:
```
.DS_Store
*.tmp
~$*
.env
*.key
*.pem
*.mp3
*.m4a
*.wav
*.mp4
*.mov
*.webm
scratch/
```
- The audio and video lines keep recordings out; recordings are stored as links only.
- Whether raw transcripts are included is a retention decision (B8). If they are excluded, add `calls/*.transcript.txt` before the first commit.

Inferred close-out flow. Run it where gh is signed in: on the host through Claude Code or the user's terminal.
1. **Pre-flight.**
   - The validator passes, and the SOP has been handed over.
   - Write the one-page client card: status, dates, repo URL, and the main contact's name and role. No transcripts, no internal notes.
2. **Retention pass** (B8): redact or remove anything that must not be archived.
3. **Commit.** Run `git init -b main` if the folder has no repo yet, add `.gitignore`, and commit.
4. **Create the private repo:**
   ```
   gh repo create client-<slug> --private --source ~/DelOps/monday-master-builder-dev/clients/<slug> --push --disable-issues --disable-wiki --description "DelOps client record"
   ```
5. **Verify.** Clone into a temporary folder. Compare `git ls-files` with the local folder and run the validator on the clone.
6. **Archive:** `gh repo archive <owner>/client-<slug> -y`.
7. **Delete the local folder only after step 5 passes and the user says yes in chat.** Moving it to the Trash is reversible; `rm -rf` is not. Record the archive date and repo URL on the client card.

Inferred restore flow:
1. `gh repo clone <owner>/client-<slug> ~/DelOps/monday-master-builder-dev/clients/<slug>`
2. Only if changes are needed: `gh repo unarchive <owner>/client-<slug>`.
3. Run the validator. Wrap the folder in a Cowork project again. Add a "restored" entry to `log.md`.
4. At the next close-out, push and archive again.

### B8. Privacy and retention for call transcripts

Found:
- **US recording consent:** federal law needs one party's consent, but about a dozen states require every party's consent. If any participant is in an all-party state, get consent or do not record [57].
- **GDPR storage limitation** [24] and the ICO's guidance [58]:
  - Set retention periods and justify them.
  - Review what you hold periodically.
  - Erase or anonymise data you no longer need.
- Transcripts can contain special category data by accident [27].
- **Claude consumer plans** (Free, Pro, Max, including Claude Code) [59][60]:
  - Whether chats are used for model training depends on the user's choice in Privacy Settings.
  - Retention is 5 years if training is allowed and 30 days if not.
  - Commercial plans are excluded from these consumer terms.
  - Cowork cloud session data on Team and Enterprise plans is not used for training [9].
- GitHub's limited access to private repos [56], and the difficulty of removing data after a push [55], are covered in B7.

Inferred policy, for the user to confirm:
- **No recordings in the folder, only links.** Transcripts are plain text that the user provides. Each call summary records `recording_consent`.
- **At intake, redact what the engagement does not need:**
  - personal chit-chat
  - health, family, and other special category details
  - third parties' personal details
  - Replace each with `[personal detail removed]`.
  - Client business statements stay verbatim.
- **Default retention:**
  - Raw transcripts stay local during the engagement.
  - At close-out, summaries and quotes are archived.
  - Raw transcripts are either deleted or archived with `transcripts_retain_until` set.
  - When that date passes, remove them from the repo, which means a history rewrite (B7). Settle the choice before the first commit.
- **The client card** keeps no personal data beyond the main contact's name and role.
- **Check the user's Claude privacy setting and plan**, since client transcripts pass through Claude.

### B9. Writing instructions and record files for current models

Found:
- Specific, concise instructions that can be verified work best. Conflicting rules get resolved arbitrarily [38].
- Explain why a rule exists instead of shouting it. Remove over-prompting ("If in doubt, use X") that causes tools to over-trigger [21].
- Write skill descriptions in third person, stating what the skill does and when to use it [35].

Inferred:
- Instructions inside CLIENT.md and plugin files use plain sentences with a reason attached. Hard constraints belong in scripts and validators (such as the append-only check) rather than capital letters.

---

## Open questions for the user

1. **Cowork project type.** Wrap `~/DelOps/monday-master-builder-dev/clients/<slug>` as the project (desktop-only, not synced, no Cowork sharing)? Or create Cowork-native projects (synced to the account) and keep the files alongside?
2. **Where validation and close-out run.** Can Cowork sessions (cloud by default) run the Python validator with PyYAML and jsonschema, and git or gh with the user's credentials? If not, those steps run from Claude Code on the Mac.
3. **Local git from the start.** Use a local git repo in each client folder from day one (checkpoints, checkable append-only rule), or only at close-out?
4. **Transcript retention.** Delete raw transcripts at close-out, or archive them with a retain-until date? Do client contracts or NDAs say anything about this?
5. **Jurisdictions.** Where are the user and their clients based? That decides whether GDPR, UK GDPR, or US all-party consent rules apply.
6. **Claude plan and privacy.** Which plan is the user on (Pro, Max, or Team), and what is their model-training setting? Do clients need him on a commercial plan?
7. **Client card location.** Where does it live (for example `~/DelOps/cards/<slug>.md`), and is it backed up anywhere?
8. **Research budgets.** Are the proposed search and fetch budgets per tier acceptable given usage limits, since long fetches use a lot of the limit?

## Not confirmed

- Whether URLs written into plugin skill text are fetchable in Cowork, or must come from the user's message or search results. The API rule excludes system-prompt-only URLs.
- The Python version and packages in the Cowork sandbox, and whether git or gh with host credentials are available there.
- Whether Cowork shows `page_age` or `retrieved_at` from web tools, or can bypass the fetch cache. These are documented for the API only.
- What "Cowork won't change a project's contents" means for local-folder projects in the web, desktop, and mobile article.
- Whether a scheduled cloud task can write into a local-folder project.
- That every monday API endpoint returns IDs as strings (implied by the GraphQL `ID` type, not checked per endpoint). The fields of the `item_nickname` input type were not read.
- That item terminology accepts lowercase only. This was reported from monday's "basics of items" support page, which returned 403 when fetched.
- The 30 to 90 day lead time for job-posting signals, which is a vendor marketing claim.
- The exact list of all-party consent states, which varies between sources (roughly 11 to 12; Connecticut, Michigan, and Oregon are sometimes marked unsettled).
- The wording of LinkedIn User Agreement section 8.2, seen through LinkedIn Help and secondary sources, not the agreement page itself.
- Whether GitHub displays YAML front matter nicely in `.md` files.
- All size, search, and fetch budgets in this file, which are proposals to tune with scenario tests.

---

## Sources (all accessed 2026-09-10)

1. Anthropic Help Center, "Use Claude Cowork safely" (updated about 2 weeks before access). https://support.claude.com/en/articles/13364135-use-claude-cowork-safely
2. Anthropic Help Center, "Get started with Claude Cowork" (updated about 1 week before access). https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
3. 9to5Mac, "Claude's Chrome side panel is now a full Cowork session", 2026-08-12. https://9to5mac.com/2026/08/12/claude-cowork-chrome/
4. Claude Platform Docs, "Web fetch tool". https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool
5. Claude Platform Docs, "Web search tool". https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
6. Anthropic Help Center, "Enable and use web search" (updated 2026-09-10). https://support.claude.com/en/articles/10684626-enable-and-use-web-search
7. Anthropic Help Center, "Organize your tasks with projects in Claude Cowork". https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork
8. Anthropic Help Center, "Use Claude Cowork on web, desktop, and mobile". https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile
9. Anthropic Help Center, "Claude Cowork architecture overview". https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview
10. Investor.gov (SEC), "Form 8-K" glossary. https://www.investor.gov/introduction-investing/investing-basics/glossary/form-8-k
11. GOV.UK, "Searching the Companies House register". https://www.gov.uk/guidance/searching-the-companies-house-register
12. OpenCorporates. https://opencorporates.com/
13. TheirStack Docs, "How to discover the tech stack of any company". https://theirstack.com/en/docs/guides/how-to-discover-tech-stack-of-any-company
14. PredictLeads, "How to use job openings data for sales prospecting" (vendor). https://predictleads.com/blog/how-to-use-job-openings-data-for-sales-prospecting/
15. Greenhouse, "Job Board API". https://docs.greenhouse.io/job-board.html
16. Lever, postings-api documentation. https://github.com/lever/postings-api
17. Glassdoor for Employers, "The link between Glassdoor reviews and customer satisfaction". https://www.glassdoor.com/employers/resources/link-between-glassdoor-reviews-customer-satisfaction/
18. U.S. Census Bureau, "North American Industry Classification System". https://www.census.gov/naics/
19. ODNI, Intelligence Community Directive 203, "Analytic Standards". https://www.intelligence.gov/assets/documents/intelligence-community-directives/ICD_203.pdf
20. Claude Platform Docs, "Reduce hallucinations". https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
21. Claude Platform Docs, "Prompting best practices" (sections: Be clear and direct; Add context; Tool usage; Long-horizon reasoning and state tracking; Research and information gathering). https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
22. APA Style, "When do you include a retrieval date in a citation?". https://apastyle.apa.org/learn/faqs/when-include-retrieval-date
23. IETF RFC 3339, section 5.1 "Ordering". https://www.rfc-editor.org/rfc/rfc3339#section-5.1
24. GDPR Article 5. https://gdpr-info.eu/art-5-gdpr/
25. GDPR Local, "B2B Marketing GDPR Compliance Guide" (secondary). https://gdprlocal.com/b2b-gdpr/
26. ICO, "How do we apply legitimate interests in practice?". https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/lawful-basis/legitimate-interests/how-do-we-apply-legitimate-interests-in-practice/
27. GDPR Article 9. https://gdpr-info.eu/art-9-gdpr/
28. LinkedIn Help, "Prohibited software and extensions". https://www.linkedin.com/help/linkedin/answer/a1341387
29. HubSpot, "Pre-call planning" (updated 2026-03-16). https://blog.hubspot.com/sales/pre-call-planning
30. Salesmotion, "The sales rep's 15-minute account research checklist" (vendor). https://salesmotion.io/blog/account-research-checklist-template
31. Martin Fowler, "Ubiquitous Language". https://martinfowler.com/bliki/UbiquitousLanguage.html
32. monday Community, "Tip of the week #5: renaming your items". https://community.monday.com/t/tip-of-the-week-5-make-sense-of-your-board-by-renaming-your-items/76514
33. monday API reference, "Boards" (`item_terminology`; `item_nickname` in create_board and update_board). https://developer.monday.com/api-reference/reference/boards
34. monday API reference, "Items". https://developer.monday.com/api-reference/reference/items
35. Claude Platform Docs, "Skill authoring best practices". https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
36. Anthropic Engineering, "Effective context engineering for AI agents", 2025-09-29. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
37. Claude Platform Docs, "Memory tool". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
38. Claude Code Docs, "How Claude remembers your project". https://code.claude.com/docs/en/memory
39. Anthropic Engineering, "Effective harnesses for long-running agents", 2025-11-26. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
40. Claude Blog, "Managing context on the Claude Developer Platform", 2025-09-29. https://claude.com/blog/context-management
41. Michael Nygard, "Documenting Architecture Decisions", 2011-11-15. https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
42. Keep a Changelog 1.1.0. https://keepachangelog.com/en/1.1.0/
43. PyYAML Documentation. https://pyyaml.org/wiki/PyYAMLDocumentation
44. YAML 1.1 boolean type. https://yaml.org/type/bool.html
45. PyPI, jsonschema (4.26.0, 2026-01-07, requires Python 3.10+). https://pypi.org/project/jsonschema/
46. jsonschema documentation, "Schema Validation". https://python-jsonschema.readthedocs.io/en/stable/validate/
47. GitHub Docs, "Using YAML frontmatter". https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter
48. Django documentation, `django.utils.text.slugify`. https://docs.djangoproject.com/en/5.2/ref/utils/#django.utils.text.slugify
49. GitHub Docs, "Permission levels for a personal account repository". https://docs.github.com/en/account-and-profile/reference/permission-levels-for-a-personal-account-repository
50. GitHub Changelog, "Private repositories with unlimited collaborators available to all GitHub accounts", 2020-04-14. https://github.blog/changelog/2020-04-14-private-repositories-with-unlimited-collaborators-available-to-all-github-accounts-and-changes-to-github-paid-plans/
51. GitHub CLI manual, `gh repo create`. https://cli.github.com/manual/gh_repo_create
52. GitHub Docs, "Archiving repositories". https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories
53. GitHub Docs, "About large files on GitHub". https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
54. Git documentation, `gitignore`. https://git-scm.com/docs/gitignore
55. GitHub Docs, "Removing sensitive data from a repository". https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
56. GitHub Terms of Service (private repository access). https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
57. Reporters Committee for Freedom of the Press, "Reporter's Recording Guide". https://www.rcfp.org/introduction-to-reporters-recording-guide/
58. ICO, "Principle (e): Storage limitation". https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/storage-limitation/
59. Anthropic, "Updates to Consumer Terms and Privacy Policy", 2025-08-28. https://www.anthropic.com/news/updates-to-our-consumer-terms
60. Anthropic Privacy Center, "Is my data used for model training?" (updated 2026-03-16). https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
