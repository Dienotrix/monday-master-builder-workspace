# Interview notes — how the user will actually use the product

Status: folded into the design by stage 1b on 2026-10-13, with the decisions recorded as A21 and A22 and the rest in `stage-1b/PLAN.md` section 2.

The user asked (2026-10-11) for stage 0 and the core logic to be settled by interview rather than by reading long documents. Each answer is recorded here as the user gave it, with what it implies. These are inputs, not decisions: anything the user turns into a decision becomes an amendment in `AMENDMENTS.md`. Stage 1b reads this file. The three A11 decisions are not asked here.

## 2026-10-12

**Q1. Where will you build a POC for a real prospect?**
Mostly in the Claude desktop app's chat — "just the chat" today, though the user thinks Projects would be the better iteration and asked for help deciding, citing a Projects update released around 2026-10-09. The idea: grab whatever exists, even a single transcript, drop it in chat, and get a POC built so demoing can start. "Show, not just tell."
- Implies: the chat / Cowork surface is primary, so the Cowork probes are the relevant half of stage 0; S0-8 (Project instructions reach a new chat) and S0-15 (the shell can reach the record folder) become central.
- The user's sidebar shows Customize and Scheduled, where Cowork's plugins and tasks live, so "the chat" in this app may already be the surface the design calls Cowork. To confirm.
- The Projects update, as the user meant it: the official article "projects-redesigned" (claude.com/resources/articles/projects-redesigned), read 2026-10-12. A project is a goal-driven workspace: a coordinator splits the work into parallel threads, each a Claude Code cloud session on its own branch and copy of a repository. Per project: shared memory, a library (files added and artifacts produced), and configuration (cloud environment, connectors, plugins, instructions, model). Threads are cloud-only today; running on the user's machine is described as "coming very soon". Beta from 2026-09-17 for select Pro and Max users of Claude Code cloud sessions, widening since; chat and Cowork get it later, no dates. Each thread is a full Claude Code session, so usage limits are reached faster. Hooks and skills are not mentioned; how connectors and plugins behave inside threads is not described.
- Fit with the user's picture: the coordinator running the first build and the company research in parallel; shared memory and the library as the per-client repo; the monday connector and the plugin configured per client project.
- Cautions: beta and not yet on chat or Cowork; cloud threads cannot see `~/DelOps` on the Mac, so the client record would live in the project's repository or library, not under `MMB_HOME` — a stage 1b design question, manageable because the record is plain files and the archive already uses git; usage cost per thread.
- Assistant's recommendation (worth the user's nod): do not build v1 around the beta. Keep the record as plain files that can live in a folder or a repository, and add a probe for redesigned Projects once the user has access — does the plugin load in a thread, does the monday connector work there, do hooks run there. If all three hold, a Project per client may become the primary home and retire several Cowork probes.
- Candidate shape, not decided: one Project per client, holding the client's inputs, research and record, so every new chat starts with the client's context. Depends on S0-15.

**Q2. How fast must the first demo be ready after the transcript goes in?**
Ideally within the hour, especially the first demo. Tailored, but not deeply — one call gives only so much context. After that, sub-agents research the client's company so later builds improve as conversations continue, and the client's data accumulates in one place the user can draw on for presentations, flowcharts and documents.
- Implies a **time budget the design does not have**: nothing in SPEC, AMENDMENTS or ROADMAP sets a time to first demo. Stage 1b input: a fast first-build path — what must be in the first build, what waits for later rounds, and how the approval stop fits inside the hour.
- **Company research is already designed but unplaced:** ARCHITECTURE's agent table has `research-scout` (WebSearch, WebFetch, Read; no monday tools). The A19 ROADMAP never placed it. Stage 1b input: the user wants it, running after the first build to improve later ones.
- **The client "repo" is the client record (A14), which is v1.** Presentations, flowcharts and documents produced from it are v2 or v3 under A19 unless the user pulls them forward. To confirm with the user.

**Follow-up on Projects.** The user does not have the redesigned Projects yet and agreed to hold off. Recorded: no access as of 2026-10-12; the three-check probe for a Project (plugin loads in a thread, monday connector works there, hooks run there) waits until access arrives. The recommendation above stands as agreed.

**Q3. What is on screen at minute 60?**
Far more than two or three boards and a dashboard: "there can easily be a whole workspace built out" in an hour, sample dummy data included. The user has watched Claude work and calibrates the first build at full-workspace scale.
- Implies: the first-hour build is a complete workspace for the client's process, with sample rows, not a sketch. Stage 1b input: the fast first-build path is sized as a whole workspace, and the build loop's per-element read-back and verification (A18) have to fit that budget — a speed question to measure on the test workspace, not assume.
- Still open: whether the AI pieces (agents, AI columns, Workflows, Vibe) are in the first hour or the second round.

**Q4. Is a few minutes of plan approval acceptable inside the hour?**
Yes — "like with Claude Code, plan and then build." Ideally the product needs fewer approvals over time "as you get more experience".
- Implies: the current shape (one approval of the frozen blueprint revision, automations approved as one list per A1) matches the user's expectation for the plan stop.
- New input, touching A1, A17 ("each creation asks" for account-level objects) and the standing live-account rules: **graduated approvals** — approvals that fade as trust builds. Not decided; which approvals may fade and which never do is the next question. Anything irreversible, anything that reaches real people, and the standing rules stay as they are unless the user decides otherwise in an amendment.

**Q5. Are the AI pieces in the first-hour workspace?**
Boards first, AI after — unless the call explicitly asks for workflows or AI features, in which case they come in the first build. The user also wants the product to **suggest AI use cases** from what the client describes. Example given (generic): a client wants a view of all their properties and to dispatch crews to each one — that reads as a Vibe app, so the product should suggest it and then build it in monday alongside the workspace.
- Implies: two rounds by default — round one the workspace with sample data, round two the AI layer — with the order flipped for anything the client explicitly asked for. Stage 1b input: the blueprint carries an "AI opportunities" section, each suggestion tied to a pain or a stated need and to an element kind (agent, AI column, Workflow, Vibe app, sequence), proposed for the user to accept.
- Known constraints from the probes: Vibe generation is asynchronous and the generator can reinterpret the spec (P-20); publication is a separate irreversible step with its own yes (A17). A Workflow publishes once per draft with no activate-later tool (P-21).

**Q6. Which approvals should fade first as trust builds?**
Not decided — "maybe we hold those approvals for now." Recorded: every approval stays as designed (the plan stop, each account-level object, publication, changes to existing objects). Graduated approvals are revisited after real use.

**Q7. Where do transcripts come from, and how do they arrive?**
Mostly a video-meeting tool's transcript, sometimes a conversation-intelligence platform's, sometimes an AI notetaker's — "it usually depends" (the user named Zoom, Gong and Fireflies). They arrive either pasted into the chat or as a text file.
- Implies: intake must handle three named export grammars plus pasted text with no file metadata at all (no header, no call date — s13 and s15 already rehearse the no-header case). Stage 1b / WP5 input: confirm each named tool's export shapes from public format documentation, with invented content only, and check the fixtures cover them; shipped files keep category words, per the clean-room rule.
- The monday connector can also read meetings recorded by monday's own notetaker; the user did not name it as a source, so it stays a possible later convenience, not a v1 path.

**Q8. Is it just the user, and could two builds run at once?**
"Mainly just me": one consultant building for one client at a time, never parallel builds. Several consultants share one monday account, each in their own Claude session and their own workspaces. Convention: each project gets a brand-new workspace named after the client, so nothing collides with another workspace or teammate.
- Implies: the cross-client lease (one user, two builds at once) protects against something that does not happen in practice; isolation comes from the new workspace per client. Stage 1b input: simplify the lease to a within-record guard plus the one "is another build running?" question, and drop S0-15's lease rationale (its other paths — knowledge overlay, cards, claims store — still need an answer).
- **New build-target convention, not in the design:** SPEC and ARCHITECTURE speak of writing to "the client's monday account" and carry workspace ids per strand, but never say "a new workspace per client, named after the client". Creating a workspace is in SPEC's irreversible class (line 64), so it is confirmed at approval and at execution.
- **A collision to settle:** monday ties each workspace to one product (the native-board probe reads `workspace { account_product { kind } }`), and native CRM and Service boards live only in their product's workspaces (native-boards-report, N10). A client needing CRM and Work Management may therefore need more than one workspace. Asked next.
- Not an answer to A11-2 (sample data in a live client account), which concerns building inside a client's own account and stays open.

**Clarification on Q7.** The three named tools were examples. Input arrives in many shapes: a client may send only an email with SOP documents, and the build then rests on some guesswork and is generalised a little until more feedback or more calls arrive.
- Implies: A15 and A16 already say any mix, any order, one path; an **email** is a further input class (sender, date, forwarded thread) not listed in A16 — stage 1b input.
- Implies, for the build-readiness check: thin input does not block a build; it decides how generic the build is. Reconciled with the evidence rules the user enforced in the fixture review: the build may rest on assumptions, but each assumption is labelled as one in the record and becomes a question for the next call. Inference shapes the build and the questions; it never becomes evidence.

**Q9. A client needing CRM and Work Management?**
One workspace per product (e.g. "<client> – CRM" and "<client> – Ops"), tied together with automations that push from one product to the other — for example, a deal reaching closed-won in CRM creates a project in Work Management.
- Implies: the blueprint plans one workspace per product and a list of cross-product links. Each link is an automation or a Workflow, approved as part of the list (A1), and API-created automations cannot be switched off through the API (A1), so each needs its UI switch-off step.
- **Probe needed:** can an automation or Workflow created through the API act across two product workspaces? Testing it needs a second workspace in another product, outside the one test workspace the live rules allow — so planning that probe is the moment the open A11-1 decision (which account carries write probes) is asked. Not asked now.

**Q10. Plugin and folders in the chat?**
Yes: the plugin is added through Customize before anything starts. Every new client demo begins with a new folder, to keep things organised. Ideally the product walks the user through creating a proper folder hierarchy and makes it easy to start a new chat in which each new client's folder gets created.
- The design already has most of this: `new-client.md` (slug, tree, setup questions, binding, admin checklist, AI notice), one record per client at `~/DelOps/monday-master-builder-dev/clients/<slug>/` (A14), and step 1 of the new-client flow ("check the connected folder is empty… `record.py init` builds the record shell"). The design assumes the user connects an empty folder per client.
- Difference to settle: the user pictures the plugin creating the client's folder from a new chat. The Cowork device shell only reaches connected folders, so that works only if a parent "clients" folder is connected, which lets every chat see every client's files. Asked next.
- New v1 input: a first-run setup walkthrough (the folder hierarchy, the plugin check, how to start a client chat) for any consultant, kept generic per A12.
- For stage 0: the Cowork probes can run as written — the plugin route through Customize and folder connection are both familiar to the user.

**Q11. Folder setup — one connected folder per client (A), or one connected parent folder (B)?**
**A, for now**: for each new client the user creates an empty folder and connects it to the new chat; the plugin fills it. Each chat sees one client's files only.
- Matches the design (`new-client.md`, step 1 of the new-client flow). The first-run walkthrough teaches exactly this: make `~/DelOps/monday-master-builder-dev/clients/<client>/`, connect it, start the chat. "For now" — revisit after real use.
- Consequence for stage 0: with only the client's folder connected, the shared files at the `~/DelOps` root (knowledge overlay, cards, claims store) are reachable only if S0-15 says so; the fallbacks the design already names apply until then.

**Q12. Should assumptions show in monday during the demo?**
No — they stay in the user's notes. "Demos' end goal is to help sell", so the workspace looks clean and finished.
- Implies: nothing in monday marks a guess; the record lists every assumption the build rests on, each tied to the question that would confirm it, so the user knows what to check during or after the demo. Consistent with neutral naming (nothing internal is written into monday).

**Addition to Q12 — what "the notes" are.** The user's notes document should also capture the client's goals and objectives, and start building flowcharts of the logic of the boards.
- Implies: the record carries one living notes document per client — goals and objectives, the assumptions with their confirming questions, open questions, and a flowchart of how the boards, items and automations connect. Stage 1b input: a text-based diagram (for example a mermaid block in markdown) needs none of the rendering tools A19 deferred, so the board-logic flowchart can be v1; polished client-facing diagrams and documents stay v2 unless pulled forward.

**Q13. After the first demo — iterate or start fresh?**
Iterate when the next round builds on similar groundwork and logic. If the client turns out to have a completely different vision of the solution, start from scratch — "and that's okay."
- Implies: numbered versions inside a strand for iteration; a pivot is a fresh build (a new version or strand from scratch, new workspaces). **The old workspaces are not archived straight away** (the user, 2026-10-12): they stay as they are, and archiving is a later, separate step on the user's yes. Stage 1b settles the mechanics.
- **Stated priority:** "For this plug in, our main concern right now is not token consumption. I'd rather have you use more tokens and be building something awesome, than to try to optimize but have a deprecated build-out." Whether this covers the plugin's runtime, the development process, or both is asked next; until then the 2026-09-20 cost policy stands for development.

**Q14. Sample data — the client's real world, or generic?**
The client's real world: their products, their kind of customers, their terms and realistic figures — which is why background research on the client matters, to tailor the demo. Nothing is excluded unless the client explicitly says not to put something in the demo.
- Implies: sample rows are built from the call, the documents and the research; anything the client asks to keep out goes on an exclusion list in the record, and the build honours it (s13's "client names not visible to freelancers" is the kind of statement that lands there). Neutral naming still applies: nothing names the user's firm, the product or the assistant.

**Q15. Does "quality over tokens" cover the plugin's runtime, the development sessions, or both?**
Both — build something of quality, without wasting tokens. "Using ultracode for this, or using fable 5.1 isn't really necessary."
- **Clarified by the user the same day:** not against multi-agent mode or the top model (Fable 5.1) — against using them on every chat and prompt, which is waste. The top model was used deliberately for part of the plugin's foundation. The user now calls the multi-agent mode "multi agent mode".
- Implies, for development: the 2026-09-20 cost policy stands — multi-agent mode and the top model where they pay (foundation and design work, high-stakes judgment, genuinely parallel or adversarial work), Opus- or Sonnet-tier otherwise — and the assistant recommends the heavier option when a task warrants it. For the plugin's runtime: quality first — research, verification and the full workspace are worth their tokens — with each agent on the tier that does its job well, not the most expensive by default.

**Q16. What is always in an awesome first-demo workspace?**
Everything the question listed — boards with the right views (Kanban, Gantt, calendar), dashboards, forms, automations that actually fire, docs — plus Workflows, AI agents and Vibe apps where they can be used. "I always try to upsell AI features to clients."
- Implies: the first-hour build covers boards, views, dashboards, forms, working automations and docs. The AI layer is never optional: the blueprint always carries the AI-ideas section, and the round-two AI build is the default follow-on rather than an extra (built in round one when the client asked for AI). The plugin names which elements are AI-powered so the user can price them (A17); it never prices credits.
- Each of these kinds has probe findings or gaps already on file: dashboards (only number, chart and battery widgets are promised until the others are checked by eye in a test account), automations (API-created ones cannot be switched off through the API), Workflows (P-21), agents (P-19), Vibe (P-20). Forms and docs need checking against the gotchas before they are promised.

**Finding during stage 0 (2026-10-12): which side of the app holds a folder.**
The user ran the first check in a new session on the desktop app's **Code side**, because the chat side cannot connect a folder to a chat. On the Code side the shell is the Mac's own: it reached all of `~/DelOps`, not just the selected folder.
- Changes Q11: Option A's isolation ("each chat sees only one client's files") holds only where the shell is scoped to the connected folder, as in Cowork's device shell. On the Code side it is organisation by convention, not a wall; the leak lint is what keeps one client's details out of another's build there. The user chose A on the stronger description and is told so.
- Open, decisive for the surface: can a chat-side **Project** connect a Mac folder (the original design assumed "a Cowork Project whose connected folder sits inside `~/DelOps`")? If not, the realistic home for client builds is the Code side, and most Cowork-specific probes stop mattering.
- **Answered the same day (S0-16):** a chat-side Project's Context folder is a **copy in a cloud container**, not a connection. The thread read the marker file and wrote a test file into `/mnt/project-files/stage0-test/`; nothing reached the Mac. The chat side also turned out to have the **redesigned Projects** (a coordinator that starts parallel threads, an Overview), so Q1's "no access" no longer holds as of 2026-10-12.
- So there are two possible homes, and the choice is the user's: the **Code side** (runs on the Mac, record in `~/DelOps/monday-master-builder-dev/clients/<client>/`, works today), or **a chat-side Project per client** (cloud; the record lives in the Project's shared folder and library, not on the Mac; parallel threads for build and research, as the user pictured). The record is plain files, so the design can keep both open while the remaining Project checks run: does the plugin load in a thread, does the monday connector work there, do hooks run there.

**Finding for stage 1b (2026-10-12): client folders inherit the development instructions.** A Claude Code session opened anywhere under `~/DelOps` loads `~/DelOps/monday-master-builder-dev/CLAUDE.md` from the parent folder — the first Code-side test chat answered "hello" by reading `HANDOFF.md`. With `MMB_HOME` defaulting to `~/DelOps` and client records at `~/DelOps/monday-master-builder-dev/clients/<client>/` (A20), every client session would start with this project's development instructions. Stage 1b decides the fix: client records outside the development folder (a different `MMB_HOME`), or the development workspace moved, or development instructions that stand down outside the product repo. Also observed: each folder a session opens in gets its own auto-memory, so a client session's memory is per client folder.
