# monday Master Builder — what it does, and what is still to come

Re-cut 2026-10-13 under amendments A17 to A23, and re-cut 2026-10-14 under A24 to A28: build first, in Claude Code on the user's machine, Windows or Mac, with identical behaviour on both; the stage-2 consistency check of that day is applied; archive simplified and development-only deletes allowed per the user's answers of 2026-10-14, and full headless suite on both systems per the user's answer of 2026-10-14. "Designed" means specified and buildable; "built" means the code exists and passes its acceptance. Nothing is promised in an account until it has been probed live there.

## The objective, in one line
Take any form of information — normally starting as transcripts — and build a monday.com proof of concept or functional demo for the potential client: CRM, Service and Work Management, the proper structure selected, the API reviewed as needed, the correct boards used, and built on top of monday's main AI offerings.

## v1 — the proof-of-concept builder (stages 2–5)

**Take in whatever arrived**
- [ ] One call, a handed-over package of calls, client documents (SOPs, flowcharts, requirements, exports), or any mix, in any order (A15, A16)
- [ ] Any transcript export format, detected by measurement
- [ ] Real-transcript repair: mis-attributed speakers, shredded sentences, composite blocks, name variants, split numbers; four confidence states; verbatim quotes only, with a refusal tier
- [ ] Documents as evidence: author, date, status; documented process kept apart from lived process; flowcharts read into the structure inventory
- [ ] The call type proposed as a best guess with the signals behind it and marked assumed; intake carries on and tells the user, a correction re-runs what depended on it, and intake stops to ask only when it cannot tell (A27)

**Decide what to build**
- [ ] Build-readiness check in nine parts, opening with the client's goals and pains: then which entities, which product and structure, what already exists, what the build rests on, what it does not meet, the AI opportunities, enough to build or not, and the questions. It ends in one of three clearances (cleared to build; cleared to build, generic; not yet), asks at most five questions that would close the gap, and can be overridden by the user with the override recorded. Thin input still gets a generic build with its assumptions listed, because a basic demo beats nothing; before the approval card the plugin asks only what it cannot infer, and everything else is assumed, labelled and shown on the card (A27)
- [ ] First-run walkthrough: creates the home folder and its tree itself, `monday-builder` under the user's home directory by default on either system; asks the firm name and its renderings, the default account to build in, optionally the workspaces never shown, and one optional question, archive to a local folder (the default) or to a GitHub repository; checks Python and the monday connector on the system it runs on, and the GitHub tool only when the user picks GitHub; warns about a `CLAUDE.md` above the clients folder (A22, A24, A26)
- [ ] Local settings folder (`local/settings.json`): the user's own values, such as the firm name for the leak list, the default build target, the workspaces never shown, and a GitHub account only when the user chose the GitHub archive; the plugin itself names none of them
- [ ] One record per client, strands inside, versions per strand, a one-page summary per strand
- [ ] Prior live builds as protected context; bespoke non-platform work recorded and handed off (A13)

**Design the structure**
- [ ] Blueprint for Work Management, CRM and Service on the native boards, detected by lineage and id, never by name
- [ ] Portfolio with connected projects by default on Enterprise Work Management, with the job-level view
- [ ] Change tables against what exists; a fork or an open structural question built on its leaning with the user's yes and marked assumed, the card saying what a later switch to the other option would and would not keep, and the user's blocking flag the one way to stop that part (A25)
- [ ] Assumed items on the card: when the client cannot be reached before a proof of concept, the automation conditions and a general overview of the board architecture are listed marked assumed, the user's yes lets the build go ahead, and they are checked with the client at the next contact; column names and status labels show on the card for the user to check and are not confirmed separately. The user is always the one who confirms, passing on what the client said (A25)
- [ ] One approval card, opening with what the build rests on; automations, workflows, agents and sequences each shown as a list with every recipient; on a proof of concept in the user's own account one yes covers the whole revision, lists and irreversible steps included, and in a client's account, or where a list's rows notify real people, each list takes its own yes and the irreversible steps are confirmed again at execution (A28); hedged answers do not count; frozen revision

**Build it in the user's own account, by default**
- [ ] Build target and workspace rule (A21): the proof of concept goes into the user's own monday account unless the user names another; each product gets its own new workspace; nothing is written outside the workspaces the record names; never-demo applies by workspace
- [ ] Workspaces, folders, boards, groups, columns, relations, mirrors, formulas, items and seed data, subitems, views, forms, docs, dashboards, widgets, automations, portfolios, projects
- [ ] Sample rows for realism over the hour (A28): dozens per board where dashboards and roll-ups need real numbers, a handful where a board only has to read well; plausible invented names and figures in the client's industry, from the call and the research brief, minus the exclusion list; every value marked as sample in the record and never cited as a fact
- [ ] **monday Workflows** (A18): authored through the workflow tools, validated, published with the final activation state in one step, proved by a trigger test; publication is its own yes in a client's account and within the card's yes on an own-account proof of concept (A28)
- [ ] **AI agents with authored prompts** (A17): role, instructions, knowledge, skills, triggers and scope written from the record, injected literally, read back, deactivated until verified; activation is its own yes in a client's account and within the card's yes on an own-account proof of concept (A28)
- [ ] **AI columns**, **Vibe apps** bound to recorded boards with code versions read back, **CRM sequences**, **webhooks**, notifications as designed outputs; HTTP blocks where monday hosts them natively
- [ ] Every write: intent → leak lint → call → record → read-back → verify; resumable without duplicates
- [ ] Change check before the first write; self-refreshing knowledge overlay; build lease; quota estimate; account check; native-board guard; never-demo workspaces
- [ ] Independent read-only audit that proves it changed nothing, ending in a "cleared to show" line; drift check
- [ ] Build notes after every audited version (A23): what was built, why, the pain trace, the assumptions to confirm, a short paragraph per open item (what was assumed, why, what the client needs to clarify, A25), a board-logic diagram and a process map, and a presentation checklist, as Markdown and a browser page; internal, with a client copy only on request
- [ ] Round two, the AI layer: a second round adds agents, AI columns, Vibe apps, workflows and sequences from the AI opportunities in the blueprint, on its own approval card; the two rounds are an order of work, not a wait, so with the usual one to three days of preparation round two is built and audited before the first showing (A27); activation and publication are separate yeses in a client's account and within the card's yes on an own-account proof of concept (A28)
- [ ] The first hour is the floor, not the typical case (A27): with the usual one to three days before the meeting, the deep research runs before the first build, the sample data is refined, and round two is built and audited before the first showing; the plugin proposes the cadence from the time available and the user sets it
- [ ] Versions carry their purpose (A25): proof of concept (`v0.x`) until sign-off, working solution from `v1.0`; recording `signed-off` warns, listing every structural assumption not yet confirmed or accepted, and does not block
- [ ] Strand and record close-out (A24, A26): the record close has `archive_check.py` write a checksum manifest of every file, then on the user's yes moves the client folder from `clients/` into `archive/<slug>/` under the home and verifies the moved folder against the manifest, with no second copy and no git at runtime, and the user deletes from `archive/` by hand on either system, with no Trash or Recycle Bin; where the user chose the GitHub archive, a private repository and a clone-and-verify close-out as well, and the local move into `archive/` still happens

**On either system**
- [ ] Windows and Mac with identical behaviour (A24): every shipped script and hook Python 3.9 or later, standard library, invoked in a form that resolves on both; paths built from the home directory the standard library reports, never with a fixed separator; transcripts and documents read with either line ending; release and headless-test tooling in Python, not shell; release checks run the unit tests, the full headless suite and the six end-to-end tests (install, intake, build, interruption recovery, audit, archive) on both systems, the GitHub archive too wherever it is set up. Linux follows from the same rules without being a target

**Safety throughout**
- [ ] Leak lint on everything written into the account; neutral naming; no personal names; the three open decisions asked when they first matter, never defaulted; one build at a time within a record; nothing unverified promised or built; assumptions stay visible, kept in the record, on the card and in the build notes, never as text in the client's workspace, and never turned into fact (A25)

## v2 — bring your own method (deferred; files kept, no skills built)
- [ ] Sales grading: the twelve criteria, gates, verdicts, gap questions in sales terms
- [ ] Demo run-sheets and the close; recap drafts; objection handling; the house voice
- [ ] Claims discipline in live speech; the delivery lessons
- [ ] Learning from transcripts across engagements
- [ ] Authored scripts (Python or otherwise) in a workflow code step, a Vibe app, or outside monday

## v2 or v3 — the client SOP and handoff package
- [ ] SOP in Word and PDF with diagrams and step tables, starting from the client's own SOP; the copy inside monday; and the master document the plugin generates for the client: the solution and why, with diagrams, how to use it, and the SOPs, seeded by the build notes (A23, A25); nothing of it is v1

## Later
- [ ] monday Dev builds; Service extras (customer portal, email-to-ticket, SLA policy); bulk import beyond about 500 rows; slide decks. Pricing stays the user's.

## Build stages (re-cut 2026-10-13, updated 2026-10-14)

| Stage | Contents | State |
|---|---|---|
| 0 | Runtime probes in Claude Code, first on macOS; the re-run on the user's Windows machine, with a short Windows list (how hooks are launched, how the plugin root path is spelled, whether the GitHub tool is present where the GitHub archive is chosen), belongs to the same package, WP-S0 (A24) | complete for v1 on macOS (2026-10-12); the Windows re-run waits, before the first release |
| 1 | repo skeleton, the shared/ fact files, intake fixtures s11-s25, acceptance tools | complete; the fixture review closed 2026-10-13 |
| 1b | design re-cut: ARCHITECTURE, BUILD-PLAN and SPEC re-cut under A17 to A22; v1 tiers, readiness check specified, stages reordered | complete 2026-10-13, with its consistency check and fix |
| fixture fix pass | readiness block on all 25 keys, the direction rename, the sweep list, the fixture edits from the review, deferred files moved, then one verification | complete 2026-10-13 |
| 2 | first, the fold-in of A24 to A28 into ARCHITECTURE, BUILD-PLAN, ROADMAP, SPEC and the readiness spec; then the goals pass on the 25 answer keys and the record-map pin (A27); then WP2 to WP5 and the agnostic sweep (WP16): record, ledger, leak lint, intake and sweep scripts, in Python 3.9 or later and system-neutral | current; the fold-in is its first task |
| 3 | v1 record templates, the readiness template, the agent-prompt template | |
| 4 | test runner, graders and seed records first; then the skills and agents for engagement, intake, readiness, blueprint, build, audit, drift check and close-out | |
| 4b | the AI offerings (Workflows, agents, AI columns, Vibe apps, sequences, webhooks) across the packages, in order | |
| 5 | hooks, READMEs, fixtures copied in, sandbox scenarios, release tooling in Python; release checks on Windows and macOS (the unit tests, the full headless suite and the six end-to-end tests); end-to-end proof of concept in a test workspace, where the first-hour floor is measured and recorded with its figure (the first decision, A11-1, is asked first) | |
| v2 / v3 | the sales layer, then the SOP layer and the master document, from `deferred/` | after a v1 proof of concept builds end to end |

**Waiting on the user, independent of the stages:** the three open decisions at the moment each first matters (A11-1 before the next live test); the user's Windows machine for the stage-0 re-run before the first release (A24).
