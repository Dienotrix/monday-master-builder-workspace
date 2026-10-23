# Demo 4 log: the AI layer on demo 3

Internal build file: never client-facing. Demo 4 is round two of A27 on the CRM build demo 3 made: the four AI opportunities its `readiness.md` marks for round 2 (a quiet-quote workflow, an account visit summary, an enquiry sort by product line and region, a monthly forecast agent), built as the next version of strand 001 in the same folder. Ids of the account, the workspace and every object stay in the client record, `local/` and the session's notes, never here.

## The probes, 2026-10-23

Run by the main session in the CRM test workspace, under A17 and A18. The session that started this one relayed the task, so the permission layer refused the first live write until the user answered in this session. The user then said yes to the probe board and the probe workflow, asked whether an agent can be kept to one workspace, and, told that an agent has no workspace setting and is bounded by its knowledge, triggers, tools and instructions, said yes to one probe agent, to be deleted after its read-back. Offered two extras, the user chose one job run and not the workflow publish.

Made: a folder "Probe – AI layer" with a scratch board "AI probe" (eleven columns, five invented rows, one update); AI set on five of its columns (summary, two categories, a custom prompt, a thread summary, the last then removed); one column added to the native Accounts board of the earlier probe folder, with no AI on it (the call was refused, G-144), and one timeline note on one of its template rows. A second timeline note was refused by the permission layer and not retried. One probe workflow (seven steps asked, five kept, validated, run once on a scratch row, then archived). One probe agent (identity, one job, read access to the scratch board, one job run, then deleted). The scratch board and its folder stay in the test workspace, which the user described as safe to clear.

What the probes found, each a gotcha entry in section 14 of `shared/monday-gotchas.md`:

- **AI columns (G-140 to G-145).** AI is set on an existing column by one of eight raw `configure_*_ai_column` mutations; the tool roster has none. Nothing shows in the column's settings: the AI reads back as two or three read-only recipes per column in `board_automations`' legacy list, with the instructions or the custom prompt stored word for word, and `remove_ai_from_column` takes them away while keeping the column and its values. The backfill filled four rows within about ten seconds, a new row filled within seven, and the two categories were right on all five rows. A custom prompt must name a column as `{pulse.<column id>}`. The CRM activity timeline is not a source for a summary, extract or improve-text column; a summary of the updates thread came out in five parts naming the poster, whatever the instructions asked.
- **Agents (G-110 to G-116), re-checked against P-19.** The connector now splits an agent into an identity and jobs; job instructions and a schedule trigger read back word for word. The first instruction write after `create_blank` was lost while it switched the agent on; the next writes held. `version_id` no longer follows the instructions. A job run on the switched-off agent left nothing the API could read. Agents have no workspace field anywhere; a knowledge grant shows as a subscription in the board's activity log.
- **Workflows (G-130 to G-135), re-checked against P-21.** The expert's changes landed when its call timed out, as before; `validate_workflow` named each missing input. The expert could not set a wait step at all, so a workflow built through the API cannot wait for a person's answer. `run_workflow_once` ran the draft on one row: the AI step's text was written, the status set and the notification arrived, and `notifications` read the message back. `create_workflow` honoured its folder. Publishing was not re-tried.

## Platform changes, made and noted (A41)

What changed in monday since the 2026-09 probes, and what was updated in the same session:

- G-69 said a workflow object lands at the workspace root and that published workflows are out of v1; the folder is now honoured, and A18 had already brought workflows in. G-69 updated, pointing at G-130 to G-135.
- P-19's agent model (one plan, `version_id` as the drift signal, a trigger's board unreadable) has changed: identity and jobs, `version_id` static, trigger settings readable. Recorded in G-110 to G-116 and a dated section of `design/ai-offerings-findings.md`.
- P-21's "the expert cannot display dynamic text" no longer holds (G-131).
- `ledger.py`: an AI column now verifies against its recipes (it was "not checkable until probed"), and an agent's job instructions are compared with their own frozen prompt blocks (`### Prompt AG<n>.J<m>`); two tests in `Demo4Test`, entries under "Added by demo 4" in WP3's `DECISIONS.md`.
- `shared/read-back.md` names the reads for AI columns, agents and workflows; `shared/record-map.md` gives the job prompt blocks and the `{pulse.<element key>}` form; the gotchas' "Tools relied on" block lists the AI tools.
- `solution-blueprint` and `account-build` (with `write-path.md`) learn the kinds `ai_column`, `workflow` with `publication`, and `agent` with `activation`, the ledger's own words, checked against `record-map.md` and `ledger.py` first.
- The lint's shared-words region regenerated after `terms` passed over `shared/` against an empty home: three generic phrases ("an ai", "the ai", "the crm") and 75 words added, none removed.

**Gates after these edits (Windows):** 701 unit tests OK under `py -3.9` and `py -3.14` (8 Windows skips, as before), `lint_plugin.py` 0 errors under both (one warning, no personal-names list), no `__pycache__`.

## The blueprint, 2026-10-23

A fresh agent that read only the solution-blueprint skill wrote v0.2 revision 1 of strand 001 (17 element-key rows: three AI columns on Leads and Accounts, four plain columns, two sample batches of 8 and 6 rows, a Forecast notes doc, the workflow and its publication, the agent and its activation, three UI steps), clean on `leak_lint.py blueprint` and `record.py check`, and froze it (sha256 `390dcc7e…`, checked by the main session). Its card is `demo4-card.md` and its 26 notes on the skill `demo4-skill-notes.md`.

Acted on at once:
- **Note 5 (the skill was wrong):** `{pulse.B3.C7}` can never pass the blueprint lint, since `C7` meets the pain-id row. The placeholder is now the column's planned name, `{pulse.Visit log}`, in the skill, `write-path.md`, the record map, G-143 and `ledger.py` (`keyed_prompt` reads an id back as its row's name); the shared words regenerated again (one word more). This revision has no custom-prompt AI column, so it is unaffected.
- **The card's switch-off line for AI columns** says the build removes their AI when the demonstration ends; `account-build` has no ledger step for that and names it as a step in monday instead. The user is told when the card is shown.
- **Note 13:** account-build gained a line for the doc an agent writes into, built before the agent.

Put to the user (A34: the lint is loosened only at the user's word), and decided as **A42** the same day:
- **Note 7:** the payload lint refused element keys (`B1.C4`) staged as JSON keys, and a line break inside an escaped long-text value before a date (`\n15`, read as N15 by the case-blind pain-id row); the main session reproduced both. The user chose to read decoded JSON (R79) and to let element keys pass (R80, against the main session's recommendation of a skill fix only); built with four tests in `A42Test`, entries in WP4's `DECISIONS.md`, a sentence in `shared/safety.md`, the shared words regenerated.
- **Note 9:** a call's real customers in sample rows: "that's fine even during demo building". The blueprint skill's rule 12 now allows them and no longer checks sample names against the call.
- **The AI columns' switch-off:** "Why remove the AI at all? These are all just demo tests, I can just delete the boards afterwards." The build leaves AI columns as they are; the card is changed, and A42 supersedes the frozen revision's one sentence, with no new revision. account-build's switch-off section says the same.

## The build, 2026-10-23

The user's yes: "Yes, build v0.2 as the changed card shows." A fresh agent followed `account-build` alone, in two runs with 80 monday calls; its 26 notes and account are `demo4-build-notes.md`.

- **First run (45 calls), stopped:** the seven columns, the three AI columns and both sample batches built and verified (all 16 planted categories and all six visit summaries as planned); the workflow drafted through the expert. Then the permission layer refused the expert request that named the user, by display name, as the notify step's only recipient: the skill told the build to give the user by id, and the leak lint blocked the id in the request's text. The agent stopped and ended the run, as told.
- **The user's decision, A43:** "Lint passes own ids (Recommended)", built as R81 (in a `workflow` payload the bound user's id and the strand's own row ids pass the id row), with two tests; `write-path.md` now runs each expert request through the lint as a `workflow` payload.
- **Second run (35 calls):** the notify step set by id, validated, run once on the planned sample quote (every step succeeded, one notification to the user, read back). The run showed the AI step had received two column ids as literal text after a correcting request (G-136); one retry fixed six of eight fields, while [Account] and [Contacts] went to a mirror and an email column (G-137). The workflow and its publication departed into UI steps U9 (map the two fields) and U10 (publish it switched on). The doc, the agent (identity and job word for word, knowledge on Opportunities read and the doc read and write, no tools, no skills) and its activation were built and verified.
- **Result:** 12 elements verified, 2 departed, none not checkable; `record.py check` and `ledger.py check` clean; v0.2 `built`. The main session's own live reads confirmed the AI columns' values on all 14 new rows, the agent ACTIVE with its identity, job, schedule and two grants, and the doc in the folder. Notifications to the user: 8 from v0.1's New lead alert as the sample leads went in, 1 from the run once.

Fixed after the build, in the same sitting:
- **`ledger.py`:** a verified activation now sets its agent row's state (note 25: the agent read `inactive` while monday had it on, so a switch-off would have skipped it); test `test_demo4_3_…`, entry 3 under "Added by demo 4" in WP3's `DECISIONS.md`. Demo 4's own record keeps the old state; account-build's switch-off also reads the activation row.
- **`tools/dev_test_workspace.py`:** without `--product` a workspace the record knows keeps its product, and a different one is refused (note 4: the CRM test workspace was nearly relabelled `core`); one test.
- **Gotchas G-136 to G-138** (a correcting expert request can turn fields into text; an AI step may not be offered connect columns; the expert finds boards by name account-wide) and G-116's doc grant by object id.
- **The skills:** account-build (`--touches` on a next version, the referenced-workspace step only with a `W1` row, batches that wait for their AI column, two payload checks per AI column, the run-once failure path, a workflow draft's state written `inactive`, the time zone from `me`, a stop part-way, inventory times kept whole, a 500's retries); the blueprint skill (a next version's UI keys, assumption ids, the earlier build's notes, `--touches`, two AI columns for two sorts, a `### Prompt WF<n>` block, the doc key, a mirror for a linked name an AI step needs).

For the user, not changed (A34):
- **Lint, build note 9:** the Product line labels, the client's own product lines planned and approved on the card, met the copied-run rule against the call's transcript when the label colours were numbers, and passed with colour names, which break the joined run. Candidates: a planned label list is not a copied run from the source the plan cites, and the verdict should not turn on the payload's shape.
- **Lint, build note 11:** "on board" was read by the paraphrase rule as a remark about a person.

## The user's look, 2026-10-23

"Done. One piece of feedback for dashboards. Everything is the same size. For us humans, it's nice to have slight variance, for example, the var charts with the months, would be nice if it was the full length so that it is easier to see among the rest of the other widgets. Outside of that, demo looks fine so far." Recorded as A44. The connector has no way to size or place a widget (G-163), so the blueprint now plans each widget's size and the order the build makes them in, and the resizing is a UI step on the card. A read of the workflow after the user's "Done" still found no live version, so U9 and U10 stay open.

## Open, for later

- **The user's steps in monday:** U9 (map the AI step's Account and Contacts, if the builder offers them) and U10 (publish the workflow switched on), with v0.1's U1 to U5 and v0.2's U6 to U8.
- A seven-label status column answered a server error twice and was made once no label used id 5; not proved (build note 8), worth a probe.
- The visit summaries sometimes say "no next step was promised" where the log names one; a wording point for the AI column's instructions in a later revision.

- Drift in an agent's instructions is caught at verify by the text, not by the digest, since `version_id` is static; adding the plan and jobs to the inventory digest belongs to the audit's design.
- `shared/safety.md` section 3 still lists published workflows among what v1 client builds exclude, and section 4 still says nothing from the AI family is built until its stage lands; both predate A18's reading and these probes. Not changed here, since neither is a platform change.
