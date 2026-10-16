# WP3 decisions: the gaps of CONTRACT.md section 4

Date: 2026-10-16. Internal build file: never client-facing.

This file settles each gap of `CONTRACT.md` section 4, W01 to W92, so that the synthetic reads (step 4) and the code (steps 5 and 6) are written against one reading. Each entry gives a decision, the reason that names the source that wins, and a follow-up. An entry marked **For the user** carries a recommended default that the coders build unless the user says otherwise.

Anchors follow the contract: `BP:n` is a BUILD-PLAN line, `A§section:line` an ARCHITECTURE line, `AM:n` an AMENDMENTS line, `RM:n` a line of `shared/record-map.md`, `NO n` a section of `shared/native-objects.md`, `G-nn` an entry of `shared/monday-gotchas.md`, `SF n` a section of `shared/safety.md`, `RB:n` a line of `shared/read-back.md`, `AI:n` a line of `rebuild-workspace/design/ai-offerings-findings.md`, `Gnn` an entry of `rebuild-workspace/build/wp2/DECISIONS.md`, `API:n` a line of `wp2/API-record.md`, `MC:name` a function of `scripts/mmb_common.py`, `Knnn` a contract clause and `PLAN §n` a section of `wp3/PLAN.md`. Authority order: AMENDMENTS over ARCHITECTURE over BUILD-PLAN over `record-map.md` and the other `shared/` files. The user's answers of 2026-10-16 (section 1) bind like an amendment for this package. WP2's decisions G01 to G61, as amended, stand and are not reopened here.

---

## 1. The user's answers, 2026-10-16

These are the user's decisions, not this file's. The user, in this session: "Go: take the recommended answers to Q1 to Q4, nod to A29's consequences and to section 8, and start sitting A." And as relayed by the main session, in the user's words: "Yes: start WP3 with the recommended answers, Q1 (a), Q2 (a), Q3 (a), Q4 (a), and my nod to A29's consequences and the plan's section 8 nods. Run it as planned, sitting A first, and commit nothing without my word."

### U1 Q1 (a): the element-key table is pinned in `blueprint/1`

WP3 pins, in `record-map.md` as part of `blueprint/1`, the table of element keys every blueprint revision carries and the place an agent's prompt text sits. `blueprint_ref`, `prompt_ref` and the key half of C129 then resolve against the frozen file, and WP7's template and WP9's guide follow the pin later. The layout is W42's.

### U2 Q2 (a): all of WP3's acceptance is built in stage 2

The AI kinds (agents, AI columns, Vibe apps, workflows, sequences, webhooks) get their ledger rows, approval classes, `compare` cases and `reconcile` cases now, with `ai-offerings-findings.md` (P-19 to P-21) as a source beside `shared/` for their shapes, marked synthetic like every other read. Stage 4b adds only what new probes change (W02 lists it).

### U3 Q3 (a): monday's public schema for 2026-10, no account involved

The published schema is monday's public schema for API version 2026-10, read from `https://api.monday.com/v2/get_schema?format=sdl&version=2026-10` with no account and no token. It was fetched on 2026-10-16: 621,124 bytes of SDL, saved outside the repository in the session scratch folder (`...\scratchpad\monday-schema-2026-10\schema-2026-10.graphql`). Only a field list (`tests/fixtures/snapshots/schema-fields.json`, W01) goes into the repository.

### U4 Q4 (a): the write-path review plus the trace check of the reads

Step 7 is one adversarial review of the write path, and step 4b is a Sonnet trace check of the synthetic reads against NO 5 and the cited gotchas, made without reading any code. Every disagreement the trace check finds is settled by the step-4 author before step 6 starts.

### U5 A29's consequences are nodded (AM:14)

The consequences AM:14 marks as the assistant's reading are taken: the classification, compare and reconcile acceptance is met against synthetic reads first and says so, and the scrubbed capture and its shape comparison join the A11-1 moment. The three design lines that assume recorded reads (A§11:1040, BP:101, BP:130) go on the list of touch-ups for the user's word at the end of this file.

### U6 PLAN section 8's thirteen items are nodded

The thirteen items of PLAN §8 are taken as written: three test files; test record variants built in setup; `ledger.py`'s own CLI frame; no log write by the ledger; reads and answer keys in separate LF files; one invented id range per type; a real person is any recipient other than the bound user; `estimate` reads sibling approvals and prints totals only; a board the record cannot place is outside and refused; the ledger vocabulary pinned under `Pinned:` with one lint tuple; steps 4 and 5 side by side; Windows first, then macOS; and an additive field for a new direction (W39), marked for the user if it would change `record.py`'s mirror check.

---

## 2. The gaps

Entries follow the contract's order and its theme headings. Section 3 of this file gathers the record-map edits, the shared edits and the design touch-ups the entries owe.

### Test inputs and what they are held to

### W01 Recorded reads that do not exist

**Decision.** Reading two: A29 supersedes A§11:1040, BP:101 and BP:130, and the reads WP3 grades `classify`, `compare` and `reconcile` against are synthetic reads with the ring they model until the capture (U5). Step 4 builds them under `tests/fixtures/snapshots/`, LF only, UTF-8 with no byte-order mark:

| File | What it is |
|---|---|
| `README.md` | what each file is; the id table below; the allowed name stems; how a scrubbed capture replaces a reads file one for one |
| `.gitattributes` | `* text eol=lf` |
| `schema-fields.json` | the published-schema paths the reads use (below) |
| `identification.reads.json`, `identification.expected.json` | the R0 to R11 and C1 to C4 reads and their answer key |
| `native.reads.json`, `native.expected.json` | the N0 to N12 reads and their answer key |
| `compare/before.read.json`, `compare/after.read.json` | two snapshot reads in the shape `snapshot` takes (W74) |
| `compare/ledger-state.json` | the strand rows and `live_objects` the snapshots are scoped against |
| `compare/appendix.md` | an audit file whose `## Documents appendix` holds the planted documents (W77) |
| `compare/expected.json` | the flags, the changed-outside rows and the document verdicts |
| `reconcile/live-inventory.json` | a `live-inventory/1` file (W70) |
| `reconcile/ledger-state.json` | the holder strand's rows and runs it is reconciled against |
| `reconcile/expected.json` | the full run's elements in output order, and the classify-only counts |

Every reads file, the two snapshot reads, the inventory and both ledger-state files open with a `fixture` object of seven keys, in this order: `synthetic: true`; `ring_modelled: "release_candidate 2026-10"`; `schema_source: {"version": "2026-10", "url": "https://api.monday.com/v2/get_schema?format=sdl&version=2026-10", "read": "2026-10-16", "field_list": "schema-fields.json"}`; `sources` (the `shared/` sections and gotcha ids it follows, such as `"NO 2.6"`, `"NO 5"`, `"G-92"`, and for the agent, Vibe and workflow shapes the probe ids `"P-19"`, `"P-20"`, `"P-21"`, never a path outside the repository); `built: "2026-10-16"`; `confirmed_by_capture: null`; `id_rule` (one sentence pointing at README's id table). An expected file carries the same object plus `answers_for` (the file it keys).

A reads file is `{"fixture": {...}, "captured_at": "2026-10-16T00:00:00Z", "pages": [...]}`. A page is `{"page": <n>, "kind": <kind>, "request": {"document": <"NO 2.6" or the GraphQL text>, "variables": {...}}, "response": {"data": {...}}, "requested_ids": [...], "returned_ids": [...], "missing_ids": [...]}`. The kinds:

- `boards_sweep`: the NO 2.6 query with `boards(workspace_ids: $ws, state: all, limit: 50, page: $p)`; `requested_ids` is `[]`, `returned_ids` the board ids returned, `missing_ids` `[]`. The last sweep page of each workspace returns `boards: []` (R0).
- `boards_ids`: the NO 2.6 query by `$ids`, used for lineage hops; `missing_ids` is requested minus returned, in request order (G-92).
- `workspaces`: `workspaces(ids:) { id name kind account_product { id kind } }`.
- `account_products`: `account { products { id kind default_workspace_id } }` (W89).
- `docs`: `docs(workspace_ids:) { id object_id name workspace_id }`.
- `workflow_objects`: `objects(object_type_unique_keys: ["monday_workflows::workflow"], workspace_ids: $ws, state: ACTIVE|ARCHIVED, limit: 500) { id state }`, one page per state (W79).
- `portfolio_items`: `boards(ids: [<portfolio>]) { items_page(limit: 100) { cursor items { id column_values(ids: ["portfolio_project_link"]) { ... on BoardRelationValue { linked_item_ids linked_items { id board { id } } } } } } }` (W80).

For every kind but the two board kinds, the three id lists refer to the ids that kind requests. The response holds GraphQL's `data` object with the field names of the query, aliases included (`portal_active`, `portal_archived`, `links`).

An answer key (`*.expected.json`) is `{"fixture", "board_count", "boards": {"<board id>": {...}}, "totals": {"<class>": <n>}, "limits": [...], "projects": [...], "reports": [...], "sweep_complete": true, "unreadable_ids": [...]}`; the native key adds `native_board_index` and `portal_object_ids` as `native-map` must store them. A board entry holds `case` (a short case id README names), `class`, `rule`, `attributes {family, version, install_kind, sla_mark, state, items_count}` (null where the rules give none), `confidence`, `signals[]` (compared as a set), `lineage {chain, resolved, result, hops, note}`, `review` (true for R7, R9, N7 and N10), `limits[]` (the codes of W83) and `models[]` (non-empty: the NO rule or section, or the gotcha it follows, such as `"NO 5 R5"` or `"G-80"`). `totals` counts every board not listed in `limits`; `limits` lists `{board_id, code, class, reason, models}` for the known-limit boards, apart from the passes; `board_count` equals the sum of `totals` plus the length of `limits` (BP:141). `projects` lists `{portfolio_id, tasks_board_id, result, rules, models}` (W80); `reports` lists `{workspace_id, product, report}` (W89).

Ids are strings. Column ids, group ids and view types keep monday's own string forms: reserved catalogue ids, the blank defaults, and suffixed ids of the form `^[a-z_0-9]+_(mk|mm)[a-z0-9]{6,8}$`. Template ids and template view ids are monday's constants from NO 3.1, 3.2, 4.1, 4.2, 4.4 and 7.2, with the two fingerprint ids of NO 2.4. Every other numeric id is invented, eleven digits long, in one range per type. No range holds an id of those catalogues (eight to eleven digits; the two eleven-digit ones begin `100` and `183`) or of WP2's unit fixture (eight digits):

| Type | Range, inclusive |
|---|---|
| workspace | `90100000001` to `90100009999` |
| folder | `90200000001` to `90200009999` |
| board, and every board-backed object: doc containers, subitems boards, custom objects, the Portal and workflow objects, whose `objects()` id is their board id | `90300000001` to `90300999999` |
| view | `90400000001` to `90400999999` |
| item | `90500000001` to `90509999999` |
| user | `90600000001` to `90600009999` |
| object (an `objects()` id that is not board-backed; none is expected) | `90700000001` to `90700009999` |
| agent | `90800000001` to `90800009999` |
| Vibe app | `90900000001` to `90900009999` |
| workflow draft | `91000000001` to `91000009999` |
| automation | `91100000001` to `91100999999` |
| dashboard | `91200000001` to `91200009999` |
| doc (`docs[].id`, distinct from its container board) | `91300000001` to `91300009999` |
| account; product | `91400000001` to `91400000099`; `91500000001` to `91500000099` |
| widget; team | `91600000001` to `91600099999`; `91700000001` to `91700000999` |

An agent's `version_id` and a Vibe app's code version are invented strings (`"vid-000001"`, `"1"`), because P-19 and P-20 give no form. Names are neutral invented words from README's stem list.

`schema-fields.json` is `{"schema_version": "2026-10", "source": "https://api.monday.com/v2/get_schema?format=sdl&version=2026-10", "read": "2026-10-16", "sdl_bytes": 621124, "aliases": {"portal_active": "objects", "portal_archived": "objects", "links": "columns"}, "paths": {"boards": "Query.boards", "boards.columns.id": "Column.id", ...}, "connector_shapes": {"agents": "P-19", "vibe_apps": "P-20"}}`: every dotted response path any reads file carries, mapped to the schema `Type.field` it resolves to, and the connector-tool shapes the schema cannot describe, each with its probe id.

`tests/unit/test_snapshots.py` imports nothing from `ledger.py` and asserts: every file above exists and is LF, UTF-8, with no byte-order mark; every header has the seven keys, `synthetic` true, `confirmed_by_capture` null and the ring above; every page has the three id lists, and `missing_ids` equals requested minus returned; every response path is in `paths` (aliases resolved) or under a `connector_shapes` key; every numeric id is a string, inside its type's range or among the catalogue ids it parses out of `shared/native-objects.md`; no name is outside the stem list or on the shipped leak list; each answer key has exactly one entry per board of its reads, every entry complete with non-empty `models`, rule ids from W82's set, and `board_count` equal to totals plus limits; the identification key names a board for each of R1 to R11, C1 to C4 and each state (active, archived, deleted); the native key names a case for each item of PLAN §4.2's native list; the compare and reconcile keys name each planted case of PLAN §4.2; and every digest in the ledger-state and expected files equals W73's function over its fields, recomputed by the test.

**Reason.** AM:10 to 14 (A29) decides synthetic reads first, and PLAN §4, nodded by the user (U5, U6), fixes their marking, their separation from the keys and the id rule.

**Follow-up.** Design touch-ups, owed by A29: A§11:1040 ("the recorded reads in `tests/fixtures/snapshots/`" becomes "the synthetic reads there, marked synthetic with the ring they model until a scrubbed capture confirms them at A11-1"); BP:101 (the WP1 inputs line takes `native-objects.md` from the probe findings, not from recorded reads); BP:130 (the WP3 inputs line: synthetic reads with the ring they model, the capture and the shape comparison at A11-1).

### W02 The AI kinds in stage 2 or stage 4b

**Decision.** All of WP3's acceptance is built in stage 2, the AI kinds included (U2): their rows, classes, `verify` rules, `estimate` lines and their `compare` and `reconcile` cases. Stage 4b adds only what new probes change:

1. Any field the P-19, P-20 or P-21 re-probes show moved (the agent list and get fields, the Vibe statuses and slices, the workflow `objects` fields): the synthetic shapes, the field list and the code follow.
2. The probes of AI columns, sequences and webhooks (A18, pending): each kind's read-back moves from `not-checkable` to a named read, which adds a `verify` rule and the kind's `compare` and `reconcile` coverage.
3. The Vibe publication probe (IR-15): the publication read (`is_published`, `published_at`) confirmed, and whether a publication can be undone.
4. Agent jobs, if the roster carries `manage_agent_jobs` (AI:11).
5. The gotcha entries for agents, Vibe apps and workflows (A§10.5:1032 expects G-110 onward) replace the probe ids in the fixtures' `sources`.

**Reason.** The user's answer U2 binds; BP:140, H23 and H24 ask for the AI kinds now, and BP:68's reason for stage 4b (files owned by other packages) does not apply to the files WP3 owns.

**Follow-up.** Design touch-up: BP:137, "(A18, stage 4b)" becomes "(A18; built in stage 2 from the probe findings; stage 4b adds what new probes change)". Stage-4b remainder: the five items above.

### W03 Sources for the agent, Vibe and workflow shapes

**Decision.** Reading one. `ai-offerings-findings.md` (P-19 to P-21) is the source for the agent, Vibe app and workflow shapes, cited in the fixtures by probe id; A§9.4:891 to 895 and A§10.4:1028 are the source for their handling. G-69's "published workflows are out of v1 (A§14)" (`monday-gotchas.md` line 227) and the exclusion sentence of `safety.md` section 4 (line 66: published workflows, CRM sequences and webhooks excluded from v1 builds) are stale against A18, and the code does not read them; it embeds A§9.4's rules.

**Reason.** AM:104 to 110 (A18) brings these kinds into v1 and U2 names the findings file as their source, over stage-1 text written before A18.

**Follow-up.** Shared edits, for the user's word; neither the code nor the reads depend on them before stage 2 acceptance: `monday-gotchas.md` G-69's "Do instead" drops "published workflows are out of v1 (A§14)" and says "publish once with the activation state decided beforehand (P-21)"; `safety.md` section 4 line 66 drops published workflows, CRM sequences and webhooks from the excluded list and points at their rows (W10). The AI-kind gotcha entries (G-110 onward) are WP1's at stage 4b (W02 item 5).

### W04 The headless rows need stage 4

**Decision.** H23 to H26 and the ledger halves of H35, H39 and H58 are owed to stage 4, with WP14's runner and the seed records r13 and r14; the checklist lists each as owed, with the runner and the seed it needs, never as failed (K454). In stage 2 the same scenarios run as unit tests on the synthetic reads and on record variants built in setup. The tests are three files (PLAN §8 item 1):

| File | Code part | What it proves |
|---|---|---|
| `tests/unit/test_ledger.py` | part 1 (step 5) | the frame, `check`, `bind`, `workspaces`, `approval`, `change-check`, `run start`, `run heartbeat`, `run end`, `intent`, `record`, `verify`, `depart`, `ui-step`, `irreversible-yes`, `live-map`, `live-map set`; the fence, and the mutex re-entry first of all (K45, W26); the write orders and every `committed` report; the scope refusals; both approval modes on one revision (K81); G49's plugin-copy test; the cross-system cases |
| `tests/unit/test_ledger_read.py` | part 2 (step 6) | `classify` on both fixtures against their keys, `native-map`, `snapshot`, `compare` and its tokenizer, `reconcile` full and classify-only, `estimate`; the catalogue drift test of W87 |
| `tests/unit/test_snapshots.py` | the reads (step 4) | the self-test of W01, independent of `ledger.py` |

Record variants are built in each test's setup from a temporary copy of WP2's unit fixture (PLAN §8 item 2), and lease state only through the `mmb_common` primitives (K37).

**Reason.** BP:149 and BP:468 to 470 put the headless rows in stage 4; PLAN §7.19 and §8 items 1 and 2, nodded (U6), fix the owed list and the three files.

**Follow-up.** Stage-4 remainder: H23 to H26 and the ledger halves of H35, H39 and H58, on WP14's runner with seeds r13 and r14. Design touch-up: BP:129 names the three test files.

### W05 `tools/agnostic_sweep.py` does not exist

**Decision.** Until WP16's sweep exists, `test_snapshots.py` enforces the id rule and the neutral names (W01). When the sweep is written, it accepts a long numeric id under `tests/fixtures/snapshots/` only inside README's documented ranges, and everywhere else only from the template catalogue of `native-objects.md`.

**Reason.** PLAN §7.18 and §8 item 6 (nodded, U6); A§5.4:362 makes the sweep fail on a long numeric id outside the catalogue, so it has to know the ranges to pass WP3's fixtures.

**Follow-up.** Design touch-up: A§5.4:362 adds "or, under `tests/fixtures/snapshots/`, inside the invented ranges its README documents"; WP16's block in BUILD-PLAN carries the same sentence.

### Shapes: record map against architecture

### W06 `account/1` and `build/2` in `record-map.md` lag A§7.3

**Decision.** Reading one: A§7.3 wins, and `ledger.py` writes every field A§7.3:551 to 575 carries, in A§'s positions, plus the fields these decisions add (listed under section 3). One reading rule keeps WP2's accepted fixture and template valid: a field or table column that WP3's record-map edit adds is optional when `ledger.py` reads an entry written without it, with the default given here, and is always present in what `ledger.py` writes. The defaults: `approval_mode` absent reads as `per-list`; `workflows_listed`, `agents_listed`, `sequences_listed` as `[]`; `rests_on` as null; `preflight.workspaces_ok` as null; `irreversible_yes[].mode` and `.approval_ref` as null; on an object `workspace`, `prompt_ref`, `version_id_at_build`, `live_key`, `product` as null and `workspace_scope`, `assumption_refs`, `refs`, `item_ids` as `[]`, `read_values` as `{}`; `live_objects.workspace` as null; the live map read without its `workspace` column (W59). RM's own additions stand (`url` on an object, `reconcile` on a run, `family` and `projects[]` on `native_map`, the run `kind` and `state` vocabularies). `api.connector_ring` and `api.execute_code_ring` take RM's form `"<kind> <value>"`, built from `version { kind value }` (W37). Key order is kept as found; a `build.json` that `approval` creates follows the WP2 template's order (`updated_at` after `reads_live`, then the blocks).

**Reason.** The authority order puts A§7.3 over RM:119 and RM:123, and PLAN §8 item 2 (nodded) forbids touching WP2's fixture, so the new fields must read as optional where that fixture lacks them.

**Follow-up.** Record-map edit: RM:119 and RM:123 gain every A§-only field of contract section 3 and the fields these decisions add (section 3 lists them); RM:123 states the optional-on-read rule. Design touch-up: A§7.3:499's `"2026-10 (pinned)"` becomes `"release_candidate 2026-10"`.

### W07 When `approval_ref` is required

**Decision.** Every object row carries an `approval_ref`, whatever its class: every planned element comes from an approved frozen revision. `intent` refuses a row without one (with `--approval-ref`, or defaulted to the row's planned ref, W42), `verify` refuses one on a `pre-existing-referenced` row recorded without it, and `check` blocks any row without one. A `pre-existing-modified` row needs `prior_state`, its `approval_ref` and its own yes exactly as an `other-strand-modified` row does (W10). This covers BP:135's irreversible, list-approved, publication and removed rows and RM's automation rows.

**Reason.** BP:135 is the widest of the three readings and A§7.3:582 ties `other-strand-modified` to `pre-existing-modified`; requiring the ref everywhere is narrower to code and test than a per-class rule, and no source forbids it.

**Follow-up.** Record-map edit: RM:123, "`approval_ref` (required on an irreversible, automation or removed row)" becomes "(required on every row: the approval entry, `vNrM`, of the revision that planned it)". Design touch-up: A§5.4:356 "for irreversible, list and removed rows" becomes "on every row".

### W08 `change_check.result` against `verdict`

**Decision.** The field is `result`, with two values: `no change affecting this build` and `change affecting this build`. `change-check` writes `result` and drops a `verdict` key from the block it rewrites. On read, a block with `verdict` and no `result` (WP2's template and fixture) is read as if `verdict` were `result`, with no finding.

**Reason.** A§7.3:502 wins over RM:119 by the authority order; A§8.6:794 needs only the two outcomes, stop or go on, and A§'s example text is the first.

**Follow-up.** Record-map edit: RM:119, `verdict` becomes `result` with the two values. WP7's `account.json` template carries `result` (stage 3).

### W09 The approval-mode vocabulary is not pinned

**Decision.** `approvals[].approval_mode` is `own-account-poc` or `per-list` (W44 derives it). `irreversible_yes[].mode` is `card` (covered by the card's one yes under `own-account-poc`, written by `intent`), `per-item` (an irreversible or publication step answered by number at execution) or `grouped` (a list's one grouped reply at execution). An `approval_ref` is the string `vNrM` (W43); it does not spell the mode, it resolves to exactly one `approvals[]` entry of the same `build.json`, and that entry carries the mode. "Names its approval mode" (BP:137) is read as "resolves to an entry that names it". The values sit in record-map under `Pinned: ledger` (PLAN §8 item 10).

**Reason.** A§7.3:582 gives the two approval modes and `mode: card`; A§8.6:800 and :801 give the two execution-time forms of a yes, per item and grouped.

**Follow-up.** Record-map edit: the new section `Pinned: ledger` carries the modes, and RM:123's `irreversible_yes[]` gains `mode` and `approval_ref` (and `evidence`, W56). Design touch-up: BP:137, "names its approval mode as `record-map.md` pins it" becomes "resolves to an approval entry that names its approval mode".

### W10 The approval class of each kind

**Decision.** Reading one: the class is derived, never stored, from the row's type, operation and origin by one table embedded in `ledger.py` and pinned in record-map under `Pinned: ledger`. The row stores `irreversible: true` for every class but `card`.

| Class | Rows | Own yes at execution, `per-list` | Own yes at execution, `own-account-poc` |
|---|---|---|---|
| `card` | every create not named below: board, group, column on a board this strand created, view, board-first form view, doc, dashboard, widget, `item_batch`, portfolio, project, `ai_column`; every `pre-existing-referenced` row | none | none |
| `list` | a create of an `automation` (also IR-01), `workflow`, `agent` or `sequence` | a `grouped` yes in this run | none, unless the row's `notifies` names anyone but the bound user: then a `grouped` yes |
| `irreversible` | a create of a `workspace` or `folder` (IR-14) or a `subitems` companion (IR-03); operation `connect` on a project (IR-07) and `convert` on a board (IR-08); a column created on a board this strand did not create (IR-13); every row of origin `pre-existing-modified` or `other-strand-modified` (IR-12, IR-13); any row `intent` is given `--ir IR-04`, `IR-05` or `IR-06` | a `per-item` yes in this run | none |
| `publication` | a `publication` row (`WF1.PUB`, `VB1.PUB`) or an `activation` row (`AG1.ACT`, `SQ1.ACT`) | a `per-item` yes in this run | none, except `SQ1.ACT`, which reaches real people: a `per-item` yes |
| `webhook` | a create of a `webhook` | a `per-item` yes in this run | a `per-item` yes: it sends to an external endpoint |
| `removed` | operation `archive` on any row (IR-02) | a `per-item` yes with containment evidence | none, but the evidence is still required |

Every class requires the `approval_ref` (W07). Operation `delete` is refused for every kind (K173). `--ir` only raises a `card` row to `irreversible`; it never lowers a class. IR-14's "prefer an existing workspace" does not bind: A21's new workspace per client and product is the rule.

**Reason.** A§9.4:877 to 898 gives the operations and their handling, with the rule that a step reaching real people keeps its own yes on either target (A§9.4:898); AM:16 to 19 (A28) gives the card's coverage, and AM:83 (A21) wins over SF 4:63.

**Follow-up.** Record-map edit: `Pinned: ledger` gains the class table's tokens (the six classes and the operations `create`, `update`, `archive`, `activate`, `publish`, `connect`, `convert`, `delete`). Shared edit, for the user's word, not needed before stage 2 acceptance: `safety.md` section 4 gains rows for workflow publication, agent activation, sequence activation and webhook creation (the A§9.4 rows), and IR-14's "prefer an existing workspace or folder" becomes "a new workspace per client and product (A21)".

### W11 The `objects[].type` vocabulary has holes

**Decision.** (i) Seeded items are recorded as one row per `create_items` call of at most 20 items: type `item_batch`, key `<board key>.IB<n>` (`B1.IB1`), `parent_key` the board, `id` null, the returned item ids in a new field `item_ids[]` (strings), and `sample_data: true` for every batch `intent` is given `--sample-data`; a seed batch without the flag is refused, because a seed batch is sample data by definition (A28). `intent` reads no A11 field: the A11-2 stop stays with `record.py check` (BP:23). (ii) A publication or activation is a row of its own: type `publication` for a `.PUB` key and `activation` for an `.ACT` key, `parent_key` the base key (`WF1`), `id` the parent's monday id once the parent has one; its `what` names the decided state (`inactive` or `active`). The type list is A§7.3:582's twenty plus `item_batch`, `publication` and `activation`. (iii) The account-level kinds are `agent`, `vibe_app`, `sequence` and `webhook`: they carry a non-empty `workspace_scope` and `workspace: null`. Every other row carries `workspace`; a `workspace` row's own `workspace` is null until `record` sets it to its own id. (iv) A workspace row carries a new field `product` (`core`, `crm` or `service`); the client it is for is the record's own (`build.json` `client_slug`), one client per record.

**Reason.** BP:137 and AM:19 need a row per seeded batch marked sample, BP:137 makes publications rows of their own, BP:136 names the account-level kinds and asks for the product, and A§8.6:798 batches items at 20.

**Follow-up.** Record-map edit: RM:78 (the element keys) gains the AI and workflow keys of A§7.3:582, `<board>.IB<n>`, and the publication and activation keys; RM:123's `objects` gains `item_ids[]` and `product`, and the type list gains the three types. Design touch-up: A§7.3:582's type list gains `item_batch`, `publication`, `activation`, and its key list `B1.IB1`.

### W12 `objects[].state` has no vocabulary, and a referenced row has no lifecycle

**Decision.** `objects[].state` is `active`, `inactive`, `archived`, `removed-by-platform`, or null while the row has no read (planned, attempting). `inactive` is allowed for `agent`, `workflow`, `sequence`, `automation` and `activation` rows only. A `pre-existing-referenced` row is never written to monday: it is created `planned` by `approval` and moves `planned` to `verified` (or `mismatch`) in one `verify` call that carries the read proving the object exists (its id, kind, workspace); it never passes through `intent` or `record`.

**Reason.** A§7.8:700 wins over RM:134 and gives the four states; nothing in A§8.6 sends a write for a referenced object, so only its read-back applies.

**Follow-up.** Record-map edit: RM:123 gives `state` its values; RM:134 gains `inactive`; the transition table of W13 carries the `planned` to `verified` move for referenced rows.

### W13 The status chain's edges

**Decision.** The allowed moves, and the command that makes each; every other move is refused (K122):

| From | To | By |
|---|---|---|
| `planned` | `attempting` | `intent` |
| `planned` | `verified`, `mismatch` | `verify`, on a `pre-existing-referenced` row only |
| `attempting` | `attempting` | `intent --retry`, a new attempt replacing `attempt` (after a timeout, or a reconcile `retry`) |
| `attempting` | `written` | `record` with an id (or item ids) |
| `attempting` | `removed` | `record` after an `archive` intent |
| `written` | `verified` | `verify --result match` |
| `written` | `mismatch` | `verify --result mismatch` |
| `written` | `written` | `verify --result not-checkable` or `needs-user`: the verify block is recorded, the status stays |
| `mismatch` | `attempting` | `intent --retry`, once: the one different call form of A§8.6:799; never for an automation, which departs instead (W50) |
| `verified` | `attempting` | `intent --operation update` (a later version or a fix changes the object; the version joins `changed_in[]`), or `--operation archive` |
| `removed` | `removed` | `verify` recording the archive's read-back |
| `departed` | `attempting` | `intent --retry`, only when the departure's decision is `later-retry` |
| `departed` | `planned` | `approval` of a later revision whose table lists the key again |
| any but `removed` | `departed` | `depart` |

`removed` is final. `not-checkable` and `needs-user` never make a row `verified`, so no live-map row is created for it (W60).

**Reason.** A§7.3:582 gives the chain and A§8.6:798 and :799 the retry, the one different call form and the user's three choices; A§8.9:823 a later version's change; K190 forbids reporting `not-checkable` as a match.

**Follow-up.** Record-map edit: RM:123's status sentence becomes the table above, kept in the `build/2` section; its status tokens are also listed under `Pinned: ledger`.

### W14 The time form of each field

**Decision.** Every timestamp `ledger.py` writes into JSON is UTC, `YYYY-MM-DDTHH:MM:SSZ`, through `mmb_common.stamp("utc")`: `bound_at`, `api.read_at`, `change_check.at`, `approved_at`, `preflight.at`, `started_at`, `heartbeat_at`, `ended_at`, `account_checks[].at`, `attempt.started_at`, `verify.at`, `irreversible_yes[].at`, `reconcile.at`, `captured_at`, `updated_at`, and a snapshot's `taken_at`. What the user reads is local with no zone: `live_objects.last_verified` and the live map's `last verified` cell are the local date (`YYYY-MM-DD`) of the verifying `verify.at`; the live map's front-matter `updated` is the local minute; a run entry's `another_build_running` text carries the local minute (`"no, answered 09:18"`). A run id's date is the UTC date of its `started_at` (W30).

**Reason.** G40 makes compared machine time UTC and human time local; WP2's fixture writes UTC for approvals, runs and `updated_at` and a date for `last_verified`, and RM:131 shows a date.

**Follow-up.** Design touch-up: A§7.3:495's `bound_at` example and A§7.3:531's `last_verified` example take these forms (`"2026-10-13T09:10:00Z"`, `"2026-10-15"`). Record-map edit: RM:119's `live_objects.last_verified` is "a local date".

### W15 Where companions, dashboard sets, widgets and project folders are kept

**Decision.** `companions` gains two keys, `tasks_board_id` and `folder_id`, for a project row (A§11.3:1074, G-72); the seven keys are the only ones accepted. A new field `refs[]` on every row holds the ids a write names outside its own parent, as `"<kind>:<id>"` strings with kind `board`, `workspace`, `doc`, `view` or `column`: a dashboard's board set (the only record, G-90), an agent's trigger targets and knowledge grants, a Vibe app's bound boards, a webhook's or a sequence's board, a relation column's target boards. A widget is a row of its own whose `id` is the create response's id. A project's portfolio is its `parent_key`.

**Reason.** A§11.3:1074 and G-72 ask for the tasks board and folder ids before any connect, G-90 makes the ids sent to a dashboard the only record, and one list serves the scope check of W41 as well.

**Follow-up.** Record-map edit: RM:123's `companions` gains `tasks_board_id` and `folder_id`, and `objects` gains `refs[]`.

### W16 `native_map` entity names, and which classes enter which index

**Decision.** Entity names are NO's, lower case: CRM `leads`, `opportunities_or_deals`, `contacts`, `accounts`, `activities`, `products_services`, `quotes_invoices`, `qi_line_items`, `sales_targets`, `deals_subitems`, `companion`; Service `tickets`, `tickets_subitems`, `incidents`, `csat_survey`, `service_contacts` (NO 4.1's family-B `contacts`, renamed so it never meets CRM's), `asset_management`, `employee_lifecycle`, `employee_directory`, `lifecycle_subitems`, `portal`. A class is `native_<product>_<entity>`, and an N5 board's class is `native_<product>_<parent entity>_subitems` (`native_crm_quotes_invoices_subitems`, `native_service_tickets_subitems`; `unknown` as the parent when neither lineage nor R2's parent names it). `native_board_index` takes every board whose class begins `native_`: N1a, N1b, N2 to N5, N6 (entity `companion`), N7 (protected as native and asked about, P-16) and N10 (under the entity its fingerprint names); never N8, N9, N11 or an R class. Its value is `"<product>/<entity>"`, with `_subitems` boards as `"crm/quotes_invoices_subitems"`. `native_map.<product>.<entity>` holds one entry per entity, the board of highest confidence, then fewest hops, then lowest id; every board of the entity is in `native_board_ids_by_entity`. `native_map.portfolio` is keyed by the portfolio's board id. A Portal enters `portal_object_ids` under its board `state`: `active` for an active board, `archived` for an archived one, whichever of N1a or N1b found it.

**Reason.** NO 3.1, 4.1 and 5 name the entities and classes, NO 6.5 and P-16 protect what may be native, and A§9.10:964 protects by the index alone, so every board that may be native belongs in it.

**Follow-up.** Record-map edit: RM:119's `native_map` sentence names the entity list, the one-entry-per-entity rule and the portfolio key; `native_board_index`'s value form gains the subitems example. Shared edit, for the user's word, not needed before acceptance: NO 4.1's family-B `contacts` reads `service_contacts`, as NO 4.3 already does.

### W17 Where `classify` results go

**Decision.** `classify` writes nothing: it prints the classification of the reads it is handed. `native-map` runs the same classification and stores it in `account.json` (`native_map` and `guard_index`, W89). A strand row's `role` holds only the class of a board the strand references or modifies, the `native_board_index` value (`"crm/leads"`) or the portfolio-family class (`project_tasks_board`), set by `verify` from `account.json` when the row's id is in the index or the portfolio map; it is null on every other row. The rule id, signals and confidence stay in `native_map`, record level, and are never copied into a strand.

**Reason.** BP:135 keeps `classify` and `native-map` record level, A§7.1:434 keeps a strand to its own ledger, and one field cannot hold a rule id, signals and confidence.

**Follow-up.** Design touch-up: A§11.2:1065 and NO 5:158, "and the strand's `objects[].role` with each board's rule id, signals and confidence" becomes "and, for a board a strand references, its class in that row's `role`"; the NO 5:158 change is a shared edit, for the user's word, not needed before acceptance.

### W18 The `guard_index` list

**Decision.** Two fields, as A§7.3:516 and :517, RM:119 and NO 6.2 have them: `template_source_ids` holds the template ids of NO 3.1, 4.1, 4.4 and 7.2 that the reads met plus the catalogue's template ids for every product the account carries, and `unreadable_intermediate_ids` holds the account's own unreadable intermediates. BP:146's "including the unreadable intermediates" is read as "beside": the hook matches a raw `template_id` against both (R-D). `native-map` writes every `guard_index` field A§7.3 lists, BP:146's omissions included.

**Reason.** A§ and RM agree against BP:146, and NO 6.3's R-D already reads both lists.

**Follow-up.** Design touch-up: BP:146, "`template_source_ids` including the unreadable intermediates" becomes "`template_source_ids` and `unreadable_intermediate_ids`", and the list gains `native_board_ids_by_entity`, `native_default_names_and_terminology` and `client_workspace_ids`.

### Files, writers and the mutex

### W19 Where snapshots live

**Decision.** One place for the snapshot of record: `live/snapshots/<YYYY-MM-DD>-<short id>-<version>-<label>.json`, with the local date, the strand's short id, the version and the label `before` or `after` (`2026-10-28-001-v0.1-before.json`), created with mode `"xb"` and `-2`, `-3` appended on a clash, never overwritten. `.work/strands/<id>/audit/` is scratch for the raw reads the session hands to `snapshot`; nothing reads it back.

**Reason.** A§7.1:399 and RM:26 make `live/snapshots/` the archived machine file `ledger.py` writes, and the label and the version end the same-day collision of W19's second reading.

**Follow-up.** Record-map edit: RM:26's path becomes `live/snapshots/<date>-<strand>-<version>-<label>.json`. Design touch-up: A§7.1:399 the same path; A§8.7:807, "the before snapshot (9.7) into `.work/strands/<id>/audit/`" becomes "the before snapshot (9.7), written by `ledger.py snapshot` into `live/snapshots/`, from reads kept in `.work/strands/<id>/audit/`".

### W20 A per-strand `build.json.bak`

**Decision.** There is none. Every rewrite `ledger.py` makes backs the old bytes up through `mmb_common.write_file` into `.work/backup/<record-relative path>.<UTC stamp>` (G39), so a strand ledger's backups land under `.work/backup/strands/<id>/solution/`. A rewrite of a scratch file under `.work/strands/<id>/` (the copied inventory) also backs up there.

**Reason.** G39, accepted in WP2, keeps every backup under `.work/backup/` and drops the per-strand folder; RM:68 and A§7.1:438 still list the old name.

**Follow-up.** Record-map edit: RM:68 drops `build.json.bak`. Design touch-up: A§7.1:438 the same.

### W21 The log has one writer

**Decision.** Reading one (PLAN §8 item 4, nodded): `ledger.py` writes no log entry. Every command after which the design asks for a log entry prints it under `"log"`, as a list of `{strand, type, version, key, lines}` that `record.py log --strand --type --version --key --line ...` takes as given: `bind` (type `binding`), `workspaces` (`workspace`), `approval` (`approval`), `change-check` (`change-check`), `run start` (`build`, "run started" or "stopped: another build is running"), `estimate --write` (`preflight`), `irreversible-yes` (`irreversible`), `depart` (`departure`), `run end` (`build`, "run ended, calls used N"), `reconcile` (`recovery`), `live-map set` (`live-map`). `irreversible_yes[].log_ref` is the header line of that log entry when the session passes it (`--log-ref`), and null otherwise.

**Reason.** RM:14 and API:25 make `record.py log` the one writer, so it alone moves `.work/history.json`; printing the entry keeps the one-writer rule and the design's log lines both true.

**Follow-up.** Design touch-up: A§8.6:792, :800 and :802, "in the log" reads "in the log, through `record.py log` with the entry the ledger prints".

### W22 The binding mirror after `bind`

**Decision.** `bind` writes `account.json` only. Its output carries `"mirror"`: the exact values of `CLIENT.md`'s `monday_account_id`, `monday_account_slug`, `monday_bound_user_id`, `monday_bound_at`, `account_kind` and `build_target`, which `engagement` then writes through `record.py guard`. `workspaces` does the same for `client_workspaces` (`"none"` or the `product:id` pairs joined by `;`). Between the two writes `record.py check` blocks on the mirror, as G15 means it to; `bind`'s and `workspaces`' output says so in `"next"`.

**Reason.** BP:386 gives `CLIENT.md`'s front matter to `engagement` and G15 makes `check` the proof of the mirror; writing the machine half first means the human half always copies a committed value.

**Follow-up.** Design touch-up: A§8.2:751 adds "then the mirror through `record.py guard`, with the values `bind` prints".

### W23 Who writes the version state at `run end`

**Decision.** Reading three: `run end` records the run's own state (`ended`) and never touches `version.md`. The build skill sets `version.md` `state: "built"` through `record.py guard` after `run end` returns.

**Reason.** A§7.1:421 gives `version.md` to the skills through the guard and A§5.4:356 makes `ledger.py` the writer of the two ledger files only, which outweighs the shorthand of A§9.8:942 and A§8.6:802.

**Follow-up.** Design touch-up: A§9.8:942, "records calls used and sets the version state" becomes "records calls used; the build skill then sets the version state through `record.py guard`"; A§8.6:802 the same.

### W24 Fields with no named writer

**Decision.** Each field gets one writer:

| Field | Writer |
|---|---|
| `api` (`connector_ring`, `execute_code_ring`, `read_at`) | `bind`, at the binding and at every refresh (W37) |
| `account.tier`, `products[]`, `builder_role`, `name` | `bind`, at the binding and at every refresh |
| `preflight` (the whole block) | `estimate --strand --inputs FILE --write` (W64) |
| `reads_live[]` | `approval`: the sorted union of every approval's `live_objects_touched` keys |
| `account_checks[]` | `run start` (the first, `before: "run start"`), then `run heartbeat --account-check` (W31) |
| `account_id_at_bind`, `client_slug`, `strand` in a `build.json` | `approval`, when they read `unbound` or `""` (the template), from `account.json` and the strand folder; an `account_id_at_bind` that differs from `account.id` is refused |
| `updated_at` in either file | every `ledger.py` write of that file |
| `lease_epoch_at_run` | `run start` |

**Reason.** A§8.6:795 and :798 and SF 3 name what is read and when; giving each field to the command that already runs at that moment adds no subcommand to A§5.4:356's catalogue.

**Follow-up.** Record-map edit: RM:119 and RM:123 name each writer beside its field.

### W25 Files outside the three the mutex clause names

**Decision.** Every `ledger.py` command takes `mmb_common.record_mutex(root)` once, at its start, and keeps it until it has printed: every file it reads or writes (`account.json`, a `build.json`, `live/live-map.md`, a snapshot, the copied inventory, a frozen blueprint, `CLIENT.md`, `STRAND.md`, `version.md`) is read and written inside that one hold, and the lease primitives it calls re-enter it (W26). A command that writes more than one file writes in this order:

| Command | Writes, in order | On a failure after the first write |
|---|---|---|
| `run start` (answer `no`) | 1 `lease_refresh` with the new run id (the primitive writes the `account.json` mirror, then the lock); 2 the strand's `build.json` (the run entry, `lease_epoch_at_run`) | exit 3 with `committed`; `next` is the same call with `--run-id <id>`, which `run start` accepts only while the lock carries that run id and `build.json` has no run of that id |
| `run start` (answer `yes`) | 1 `build.json` (the run entry, state `ended`); 2 `lease_release` | `committed`; `next` is `record.py lease release --epoch <e> --label <l>` |
| `run end` | 1 `lease_fence` (moves the heartbeat; not a commit); 2 `account.json` (`live_objects`, `updated_at`); 3 `live/live-map.md`; 4 `build.json` (the run entry ended); 5 `lease_release` | `committed`; `next` is the same `run end` call, which is safe to repeat: when the named run is already `ended` and the lock still carries it, `run end` rewrites steps 2 and 3 (no change when equal) and releases |
| `live-map set` | 1 `account.json` (the row); 2 `live/live-map.md` | `committed`; `next` is `ledger.py live-map`, which renders the map from `live_objects` |
| `reconcile --inventory` | 1 `.work/strands/<id>/live-inventory.json` (the copy); 2, with `--classify-only`, the holder's `build.json` | `committed`; `next` is the same call without `--inventory`, which reads the copy |

`bind`, `workspaces` and `native-map` write `account.json` alone; `live-map` writes `live/live-map.md` alone; `snapshot` writes one new file; every other writing command writes one `build.json`. A single write that fails is exit 3 naming its file, with nothing committed. The lock is always written last, by the primitive, so `run end`'s order leaves a crash before step 4 as a `running` run with a stale heartbeat, the ordinary recovery trigger (A§8.11), and a crash between steps 4 and 5 is handled by W72's classify-only rule for an `ended` run.

**Reason.** G09 amended (DECISIONS:606) puts every decision's read and write in one hold and the lock last; BP:135 asks for `run end`'s writes "in one step", which one hold and a repeatable call give.

**Follow-up.** Record-map edit: a "Ledger write orders" paragraph after RM:123 carries this table, and the `lock/2` section's "Writes and repairs" paragraph (RM:142) points at it. Design touch-up: A§7.1:438's `committed` sentence points at the same table.

### W26 Mutex re-entry

**Decision.** Reading two: the test comes first. The first test of `test_ledger.py` holds `record_mutex` in the test process, calls `lease_fence` and `lease_release` inside the hold, asserts both return without waiting, then asserts from a child process that the mutex is still held until the outer hold ends (K45). `ledger.py` runs in one thread and takes the mutex once per command with the record root as given; it never opens a second spelling of the path itself.

**Reason.** PLAN §7.20 asks for the in-process proof before anything relies on it; `record_mutex` keys its re-entry on the resolved path and the thread, so one thread and one root are what the proof covers.

**Follow-up.** None.

### W27 The delta diff has no subcommand

**Decision.** Reading one: `approval` computes it. After validating, `approval` compares the frozen revision's element-key table (W42) with the strand's `objects`: a key absent from `objects` gets a new `planned` row (type from the table's kind, `name`, `introduced_in` the version, `approval_ref` and `blueprint_ref` this revision); a key present keeps its row, its id and its status untouched; a `departed` key the table lists again goes back to `planned` (W13); a key in `objects` that the table no longer lists is reported and left as it is. The output carries `delta {new[], kept[], replanned[], not_in_table[]}`. A change to a kept element is planned at build time by `intent --operation update`, which adds the version to `changed_in[]`.

**Reason.** A§8.9:823 says "`ledger.py` diffs the approved element table against the strand's `build.json`"; `approval` is the one command that holds both at the moment a version is approved.

**Follow-up.** Design touch-up: A§8.9:823 names `ledger.py approval` as the command that diffs.

### The fence, the run and the lease interplay

### W28 Which subcommands are behind the fence

**Decision.** The account-affecting subcommands, every one fenced, are `intent`, `record`, `verify`, `depart`, `irreversible-yes`, `run heartbeat`, `run end` and `workspaces`. Each takes `--lease-epoch`, `--session-label` and `--run-id` and runs in this order inside its one mutex hold: (1) the newer-schema check (W36); (2) every validation, collecting every refusal; (3) if any, refuse with them all and write nothing, not even a heartbeat; (4) `mmb_common.lease_fence(root, epoch, session_label, run_id)`; a `(False, reason)` is a refusal (exit 1, file `.work/lock.json`, field `lease`, the reason as problem, expected "the epoch and session label this session's take returned and the run id `run start` returned"), and an exception from the fence (a `CannotRun`: a mutex timeout, an unreadable lock) propagates as exit 3: a stop, never a skip, with nothing written; (5) a fresh read of `account.json`, because the passing fence rewrote its lease mirror, and of the strand's `build.json`; (6) the writes. `run start` does not call the fence: it refreshes with its run id through `mmb_common.lease_refresh` before any fenced write can pass, which is what lets the fence pass at all (G51 amended). Not fenced, because they precede a run, follow it, or touch no account: `check`, `bind`, `approval`, `change-check`, `run start`, `ui-step`, `reconcile`, `estimate`, `snapshot`, `compare`, `classify`, `native-map`, `live-map` and `live-map set` (a strand close, which runs with no lease held, A§8.10:829). A§9.8:944's "every approval reply refreshes it too" is read as the execution-time reply, `irreversible-yes`, which the fence covers; the card's approval comes before any run.

**Reason.** BP:135 and A§5.4:356 fence every account-affecting write and G51 amended makes the fence pass only inside a run; validating before the fence keeps a refusal free of writes (K27) while the fence still runs before any write.

**Follow-up.** Design touch-up: A§5.4:356 names the eight fenced subcommands; A§9.8:944, "every approval reply" becomes "every execution-time yes (`irreversible-yes`)".

### W29 Where the presented run id comes from

**Decision.** From the session: `run start` prints the run id it minted, the session holds it beside the epoch and the label from that moment, and every fenced command takes it as `--run-id`. `ledger.py` never fills a missing epoch, label or run id from the lock or from `build.json` (K112): a fenced command whose three flags are not all present is refused (exit 1) naming the missing one; the flags are optional in the parser so that a missing one is a refusal, not a usage error.

**Reason.** A§9.8:934's carry rule holds the session's values and never re-reads them from disk, because a woken old session that re-read its ledger would otherwise pass; G04's choice in WP2 makes a missing value a refusal.

**Follow-up.** Design touch-up: A§5.4:356 and A§9.8:934, "the run the strand's ledger is in" becomes "the run id `run start` returned, presented as `--run-id`".

### W30 `run start`'s details

**Decision.** `run start --strand <id> --lease-epoch <e> --session-label <l> --another-build-running no|yes [--answer-words "<the user's words>"] --account-check match [--run-id <id>] --expect-sha <sha>`. (a) The answer is stored as text: `"no, answered HH:MM"` or `"yes, answered HH:MM: <words>"`, with the local minute. (b) A `yes` appends the run entry with `state: "ended"`, `ended_at` equal to `started_at` and `calls_used: 0`, enters no run id into the lock, and releases the lease through `lease_release` in the same call (W25); no fenced write can follow. (c) A run id is `run-YYYY-MM-DD-N`: the UTC date of `started_at`, and `N` one more than the highest `N` of that date among the runs of every strand's `build.json` in the record, read inside the script, so no two strands mint the same id and `lease_refresh` never meets one an earlier lease carried. `--run-id` is accepted only for the retry of W25. (d) `kind` is always `build`; a fix run is a build run; `doc-copy` is refused as deferred (BP:380). (e) A `running` run of this strand that is not the lock's (its session lost the lease) is set to `interrupted` in the same write; the output's `recovery_first` is true when any row is `attempting` or any run was set `interrupted`, and the session reconciles before any new write. (f) `calls_estimated` is copied from `preflight.estimated_calls` when `preflight.version` is the run's version, else null until `estimate --write` sets it (W64). `run start` also refuses: a strand whose `STRAND.md` version is `none`; a version with no approval entry for `version.md`'s revision; an approval whose `sha256` is not the frozen file's; `--account-check` other than `match` (the stop before any write of A§9.3); and every refusal `lease_refresh` raises, passed through. It appends `account_checks[0]` as `{at, before: "run start", result: "match"}`.

**Reason.** A§8.6:791 and :792, A§9.8:938 and :942 and RM:123 give the one question, the stop, the release and the id form; G50 and G51 amended let a run id enter only once, so it must be unique record-wide.

**Follow-up.** Record-map edit: RM:123's run `id` sentence adds "N counted per UTC date across every strand of the record", and `kind` notes `doc-copy` as deferred.

### W31 `run heartbeat`

**Decision.** `run heartbeat --strand <id> --lease-epoch --session-label --run-id [--account-check match|mismatch --before "<what>"] --expect-sha <sha>` passes the fence, which moves the lock's heartbeat and its mirror (no history entry, K114), and writes the run entry's `heartbeat_at` in `build.json`. With `--account-check` it appends `{at, before, result}` to `account_checks[]`; a `mismatch` is recorded and the output says `stop: true`, the session stopping before any write. Every other fenced command that writes `build.json` also sets the run's `heartbeat_at`.

**Reason.** A§5.4:356 lists the subcommand and A§7.3:562 carries the run's own `heartbeat_at`; A§8.6:798 and SF 3 ask for an account check at every batch of 20 writes, which needs a writer.

**Follow-up.** None.

### W32 `run end`'s details

**Decision.** `run end --strand <id> --lease-epoch --session-label --run-id --calls-used <n> --expect-sha <sha>`. (a) It passes the fence first, then releases through `lease_release(epoch, label)` last (W25). (b) The run's end state is `ended`; `version.md` is not touched (W23). (c) `calls_used` is the session's count, a non-negative integer. (d) It refuses while any row whose `attempt.run_id` is this run is `attempting`: the session records, departs or reconciles it first; `written` rows (a `not-checkable` read) do not block. The output carries `live_rows {created[], refreshed[], archived[]}` and the log entry.

**Reason.** BP:135 and A§8.6:802 release in the same step, A§9.8:942 releases only through the primitive, and an `attempting` row left at the end is exactly the recovery trigger A§8.11 names.

**Follow-up.** Design touch-up: A§8.6:802, "state `built`" becomes "the run `ended`; the skill then sets the version `built`" (with W23).

### W33 The fields of `committed` for the ledger

**Decision.** A failure after a committed write raises `MMBError` with the keyword `committed` and exits 3. The `error` object is `{"file": <the file whose write failed>, "field": "committed", "problem": "<the OS error>; <n> earlier write(s) of this call stand", "expected": <the next call>}`, and the top-level `committed` object is `{"command": "<name>", "written": [<record-relative paths, in order>], "not_written": [<paths or steps>], "lease": null | {"refreshed": {"epoch", "session_label", "run_id"}} | {"released": {"epoch"}}, "run_id": <id or null>, "next": "<the exact call that completes it>"}`. W25 gives `next` per command.

**Reason.** G09 amended asks `ledger.py` to report its post-commit failures the way `record.py` does, and A§7.1:438 asks for what is written and what is still to do.

**Follow-up.** None.

### W34 `--expect-sha`

**Decision.** Every command that writes a `build.json` takes `--expect-sha <sha>` and refuses, with nothing written, when the file's `mmb_common.sha256_file` (the bytes, G60) differs; `--expect-sha none` means the file must not exist yet (`approval` creating a strand's first ledger). Exempt: `reconcile --classify-only`, which a sibling's session runs over a ledger it never reads (A§7.1:434), under the mutex. `account.json` takes no sha, since its writers decide inside the mutex. Every writing command's output carries `"written": {"<record-relative path>": "<new sha256>"}`, and `check` prints `"shas"` for `account.json` and every `build.json`, so the session always holds the current sha without reading the file.

**Reason.** A§5.3:345 takes it "on every write to `build.json`" and G60 settled the hash as bytes; the output sha closes W34's missing read.

**Follow-up.** None.

### W35 Ids as numbers

**Decision.** A JSON input file (a binding document, a reads file, an inventory, a verify read, a snapshot read, an estimate inputs file, a change-check file) whose value under a key `id`, `ids`, or a key ending `_id` or `_ids` is a JSON number is refused (K131), naming the file and the key path; a string of digits passes, and nothing is ever coerced. A command-line value that names a monday id (`--id`, `--parent-id`, `--workspace`, `--scope`, the id half of `--ref`) must match `^[0-9]+$` and is stored as the string given. `check` blocks a number found under such a key in `account.json` or a `build.json` (K238).

**Reason.** RM:99 and RM:119 store every monday id as a string and BP:135 refuses a number; a key-name rule is the one test that covers every input shape.

**Follow-up.** None.

### W36 The newer-schema set for the ledger

**Decision.** Before anything is written, every writing command reads the schema of `CLIENT.md` (`client/2`), `account.json` (`account/1`), `live/live-map.md` (`live-map/1`) when it exists, and the `STRAND.md` (`strand/1`), `version.md` (`version/1`) and `build.json` (`build/2`) of every strand it reads or writes, and refuses naming each newer one (G57). The lock's schema is checked by the primitives the command calls (`_files`), never by `ledger.py`. `check` reads the same set and reports one blocking finding per newer file. A snapshot or inventory file carries its own schema (`snapshot/1`, `live-inventory/1`) and a newer one is refused by the command that reads it.

**Reason.** G57 sets the rule for every writer, and K35 keeps the lock away from `ledger.py`.

**Follow-up.** Record-map edit: the schema list gains `snapshot/1` and `live-inventory/1` (W70, W74).

### `bind`, `workspaces` and the scope check

### W37 `bind`'s interface

**Decision.** `bind --binding <file> [--strand <id>]`. The file is the `data` object of one read-only document, SF 3's account check with two fields added: `query { me { id name kind } account { id slug name tier products { id kind } } version { kind value } }` (every field is in the 2026-10 schema; `me.kind` is the user kind, `account.products` the account's products), plus an optional top-level `execute_code_version {kind, value}` when `execute_code` was read on another ring. `bind` writes `account.id`, `slug`, `name`, `tier`, `bound_user_id` (`me.id`), `builder_role` (`me.kind`, lower case), `products[]` (`{id, kind}` for every product of kind `core`, `crm` or `service`), `kind` and `build_target` (copied from `CLIENT.md`'s `account_kind` and `build_target`, which `engagement` set at `init`; a pair that disagrees is refused, K54), `bound_at` (now, at the first binding only), `api {connector_ring: "<kind> <value>", execute_code_ring, read_at}`, `client_slug` when empty, and `updated_at`. It refuses: on a `client` record, an account whose id or slug is on a `sandbox` line of `local/sandbox-accounts.txt` (K55); on a `sandbox` record, an account on no `sandbox` line (K56); on an `own` record, an account whose id and slug are not both `local/settings.json`'s `default_build_account` (K57); an `account.id` already bound to another id (K58: no rebind). A second `bind` with the same account id, slug and bound user is a refresh: it rewrites `tier`, `products`, `builder_role`, `name` and `api` and keeps `bound_at`, which is how preflight records products, tier and role (A§8.6:795); a refresh with another bound user is refused, and the session asks the user (A§9.3). `bind` reads `never-demo` lines and `never_show_workspaces` for nothing: it writes no workspace (K59). The output carries `mirror` (W22) and the log entry.

**Reason.** A§8.2:751 and SF 3 fix the binding document and its refusals, A§9.3 one account per client with no rebind, and the account check's one document already returns everything but the role and the products, which two more fields of the same query give.

**Follow-up.** Record-map edit: RM:119's `account` sentence names `bind` as the writer of `api` and of a refresh. Shared edit, for the user's word, not needed before acceptance: `safety.md` section 3's one-document query gains `kind` on `me` and `products { id kind }` on `account` for the binding (the check itself may stay the short form).

### W38 `workspaces`' interface, and who writes the target lists

**Decision.** Reading one: `workspaces` writes all three lists. It is fenced and has three forms, each with `--strand <id> --lease-epoch --session-label --run-id`:

- `--product core|crm|service --id <id> --name "<name>" --created-in <short>/<vX.Y> [--direction-change "<log ref>"]` records a workspace the build created: `client_workspaces[product] = {id, name, created_in}`, the id added to `guard_index.client_workspace_ids`, to the strand's `build_targets_by_strand` `workspace_ids`, and to `guard_index.product_workspaces` with the product read back at creation (A§8.6:797).
- `--use <id>` adds a workspace already in `client_workspace_ids` to the strand's `workspace_ids`: a later strand building on the same client's workspaces (A21).
- `--folder <id> --in-workspace <id>` adds a folder to the strand's `folder_ids`; its workspace must already be in the strand's `workspace_ids`.

It refuses a product outside the three (K63), an id in the operational list of W41 (K65, quoting the settings or sandbox line), an id already recorded for another product, a `created-in` that is not this strand's qualified version, a `--use` id outside the client's set, and a second workspace in a product that already has one unless `--direction-change` is given (W39). `native-map` never adds or removes a target: it keeps `build_targets_by_strand` as found and refuses to store when any target lies outside `client_workspace_ids` (K67, K411). `intent` never extends a target list. The output carries `mirror` for `CLIENT.md`'s `client_workspaces` and `STRAND.md`'s `workspaces` (`product:id` pairs joined by `;`).

**Reason.** A§7.3:538 gives `workspaces` the workspace rule's record and G47 makes `client_workspace_ids` the ceiling; one writer for all three lists is the reading that keeps them consistent, and BP:146's "with the record's targets as their union" is satisfied by `native-map` keeping them.

**Follow-up.** Design touch-up: BP:135's "records ... the client's workspaces as they are created" moves from `bind` to `workspaces`; BP:146's `build_targets_by_strand` clause reads "kept as `workspaces` wrote them, with the client's workspaces as the ceiling".

### W39 One workspace per product against a new direction

**Decision.** An additive field, as PLAN §8 item 13 proposes: `account.json` gains `superseded_workspaces[]` of `{product, id, name, created_in, superseded_in, direction_change}`. `workspaces --product <p> --id <new> ... --direction-change "<log ref>"`, where the log reference is the user's logged decision to start fresh (A21: the plugin proposes, the user confirms), moves the product's current entry into `superseded_workspaces` with `superseded_in` the new strand's qualified version, and writes the new entry in its place. Both ids stay in `client_workspace_ids` (the old workspaces are kept and stay the client's, A§8.9:825), the new id joins the new strand's targets and the old stays in its own strand's. Without `--direction-change`, a second workspace in a product is refused (K145). `client_workspaces` keeps one entry per product, so `record.py check`'s mirror check is unchanged and this entry is not for the user.

**Reason.** AM:83 (A21) and A§8.9:825 open fresh workspaces for a new direction and keep the old, BP:136 needs the record to say so, and an additive list leaves WP2's mirror check as built.

**Follow-up.** Record-map edit: RM:119 gains `superseded_workspaces[]`. Design touch-up: A§7.3:538 names it. Shared edit, for the user's word, not needed before acceptance: `safety.md` IR-14 (with W10).

### W40 A board the record cannot place

**Decision.** Fail closed (PLAN §8 item 9, nodded). A board, doc, view or column id that a write names is placed only by the record: a row of this strand's `objects` with that id (its `workspace`, or the nearest ancestor row's), or an `account.json` `live_objects` row with that `monday_id` and a `workspace`. Anything else is outside the client's workspaces and the write is refused, naming the id and saying how to place it: record the object as a `pre-existing-referenced` row and verify it with a read that shows its workspace (W12). A native board an agent will read is therefore planned as a referenced row, which the blueprint does anyway.

**Reason.** BP:136 refuses any reference outside the client's workspaces, A§11.2:1066 makes "a write to a board the index does not know fails closed" the design's posture, and a session's claim is not a record.

**Follow-up.** None.

### W41 The scope input form, and the operational list

**Decision.** `intent` takes the target and every reference as flags: `--workspace <id>` (the row's own workspace, for every kind but the four account-level ones), `--scope <id>`, repeated (an account-level row's `workspace_scope`), and `--ref <kind>:<id>`, repeated, with kind `board`, `workspace`, `doc`, `view` or `column`, for every trigger target, knowledge grant, Vibe binding, webhook or sequence board, dashboard board and relation target (stored in `refs[]`, W15). The checks: the row's `workspace` must be in the strand's `build_targets_by_strand` entry (K137); every `--scope` workspace and every referenced workspace must be in `client_workspace_ids`, and every referenced board, doc, view or column must be placed (W40) in one (K139 to K143). The operational list is read from the home, through `mmb_common`: the ids of `local/settings.json` `never_show_workspaces[]` and the `workspace_id` of every `never-demo` line of `local/sandbox-accounts.txt` (a `*` line names no workspace and is the demo gate's, WP9). An id on the list is refused by `workspaces` and, as a target, scope or reference, by `intent`, with the reason "an operational workspace (never-demo), never a build target" added to the outside refusal. Every scope refusal names the strand and the id, and its expected text quotes A21: "inside this client's workspaces: the plugin never writes into any other workspace (A21)" (K150).

**Reason.** BP:135 puts the operational refusal in `intent` and `workspaces`, RM:70 gives both lists, and BP:136 and BP:527 (H58) want the rule quoted.

**Follow-up.** None.

### Approvals

### W42 `approval`'s interface, and the element table

**Decision.** The `blueprint/1` element-key table (U1). Every blueprint revision carries, once, a level-2 heading that reads exactly `## Element keys`, followed (blank lines allowed) by a Markdown table whose header cells, trimmed and lower case, begin `key | kind | name`; further columns may follow (`purpose`, say) and are not read. One row per element, until the first line that does not begin with `|`:

```text
## Element keys

| key | kind | name |
|---|---|---|
| W1 | workspace | Larkmoor Joinery – Ops |
| B1 | board | Jobs |
| B1.V1 | view | Jobs by stage |
| AG1 | agent | Dispatch helper |
| AG1.ACT | activation | activate Dispatch helper |
| U1 | ui_step | Kanban view on Jobs |
```

`key` is a bare element key of K152's shapes (one pair of backticks around it is stripped), unique in the table; `kind` is an `objects[].type` value (W11), or `ui_step` for a `U<n>` key; `name` is the planned name, non-empty, `\|` standing for a pipe. An agent's prompt text, an AI column's prompt and a Vibe app's request each sit under a level-3 heading that reads exactly `### Prompt <KEY>` (`### Prompt AG1`), in the first fenced block after it: an opening fence of three or more backticks followed by `text`, the prompt, and a closing fence of the same backticks alone on its line. `blueprint_ref` and `prompt_ref` (`v0.1r4#B1`) resolve to the strand's `versions/v0.1/blueprint-r4.md`: the key half must be a row of that file's table, and for `prompt_ref` that file must hold the key's prompt block. Prompt text is compared after turning CRLF and CR into LF and dropping trailing newlines, and is otherwise exact.

On WP2's unit fixture the frozen `blueprint-r1.md` has `## Elements` with the columns `key | kind | name | purpose`: the right rows under another heading. So the fixture needs a stand-in, which a WP3 test adds in its own temporary copy only (PLAN §8 item 2): it rewrites the heading line to `## Element keys` in the copy's `versions/v0.1/blueprint-r1.md` and sets the copy's `version.md` `sha256` and `build.json` `approvals[0].sha256` to the new file's sha. On that copy `v0.1r1#B1` passes and a row whose `blueprint_ref` is set to `v0.1r1#B9` blocks (C129's probe). On an untouched copy `check` reports exactly one warning, "frozen before the element-key table was pinned: keys not resolved", for that file (K248).

`approval --strand <id> --sha256 <hex> --words "<the user's words>" --session "<where the yes was given>" [--version vX.Y] [--revision N] [--irreversible <key> ...] [--touches <qualified key>=<constraint> ...] --expect-sha <sha>|none`. `--version` defaults to `STRAND.md` `version` and `--revision` to that version's `version.md` `revision`. It refuses: a `non-platform` strand; an unbound account; a `--sha256` that is not both the frozen file's `sha256_file` and `version.md`'s `sha256` (K70); a version and revision already approved; a frozen file with no table, or a table with a duplicate key, a key of the wrong shape or an unknown kind; an `--irreversible` key not in the table, or of kind `automation`, `workflow`, `agent` or `sequence` (those are lists, K83); a table row of kind `workspace`, `folder`, `publication`, `activation` or `webhook` missing from `--irreversible`; an agent, AI column or Vibe app row with no prompt block; a `--touches` key absent from `live_objects`, given a constraint other than its live one, or marked `do-not-change` (A§7.8:716). The entry it appends, in A§7.3:551's order: `version`, `qualified_version`, `revision` (integer), `frozen_file`, `sha256`, `approved_at`, `approved_words`, `approved_in_session` (the `--session` text: the blueprint session holds no lease label), `approval_mode` (W44), `element_count` (the table's rows whose kind is neither `publication`, `activation` nor `ui_step`), `irreversible_listed` (the `--irreversible` keys in table order), `automations_listed`, `workflows_listed`, `agents_listed`, `sequences_listed` (the table's rows of each kind, in table order), `rests_on` (W46) and `live_objects_touched`. It then plans the delta (W27), giving an agent, AI column or Vibe app row its `prompt_ref`, sets `reads_live` and the three binding fields (W24), and creates `build.json` from the `build/2` skeleton when the strand has none (`--expect-sha none`).

**Reason.** The user's answer U1 (Q1 (a)) pins the table and the prompt's place in `blueprint/1`, and names the heading; DECISIONS:630 leaves the key half of C129 to WP3, and the fixture's own heading is not the pin, so the stand-in lives only in a test's copy.

**Follow-up.** Record-map edit: RM:115's `blueprint/1` sentence gains the table, the prompt block and the resolution rule above. Design touch-ups: A§3.4's blueprint sections name `## Element keys` and `### Prompt <KEY>`; BP's WP7 block (the blueprint template carries both) and WP9 block (`blueprint-guide.md` says where keys and prompts sit).

### W43 The form of `approval_ref`, and where a list's own yes lives

**Decision.** An `approval_ref` is `v<version number>r<revision>` (`v0.1r1`, `v0.2r2`), and it resolves only inside the strand's own `build.json`, to the one `approvals[]` entry whose `version` and `revision` it spells; a ref never names another strand's approval (an `other-strand-modified` row is approved by its own strand's card). A list's own grouped yes at execution, and an irreversible step's own yes, are `irreversible_yes[]` entries written by `irreversible-yes` (W48), one per key, with `mode` `grouped` or `per-item`; `automations_listed` and the other lists hold what was approved, and the entries hold what was confirmed. The entry an `approval_ref` names is read from disk inside the command's hold, never carried from an earlier call (K80).

**Reason.** A§7.3:572 and the fixture use `vNrM`, RM:77 keeps the ledger form inside the strand, and A§8.6:800 and :801 give the yes per item and the grouped reply, which need one place each.

**Follow-up.** Record-map edit: RM:123's `approval_ref` names the form and the resolution.

### W44 Mode derivation at the edges

**For the user.** The amendments leave one case between them: A28's one yes is "for a proof of concept in the user's own account", and the separate yes per list stays "for a build in a client's account and for any list whose rows notify real people". A working solution (`v1.0` and later, A25) built in the user's own account and notifying only the user falls in neither sentence.

**Decision.** `approval_mode` is `own-account-poc` exactly when `account.build_target` is `own-account` and the version's purpose is `proof-of-concept` (`version.md` `purpose`, or, where absent, a version below `v1.0`); otherwise `per-list`. Recommended default, which the coders build unless the user says otherwise: a working solution in the user's own account is `per-list`. A `sandbox` record (build target `none`) is `per-list`, since it is neither the user's own build target nor a proof of concept for a client; this fills nothing of A11-1, which stays the choice of the test workspace. A revision whose lists mix rows is one mode for the entry; a row that notifies anyone but the bound user needs its own yes in either mode (W10, W45).

**Reason.** AM:16 to 19 (A28) scopes the one yes to a proof of concept in the user's own account, and AM:53 (A25) makes `v1.0` a working solution; the stricter reading fails closed where the amendments are silent.

**Follow-up.** For the user: confirm `per-list` for a working solution in the user's own account, or choose `own-account-poc` for it. Design touch-up, either way: A§7.3:582 states the derivation.

**Answered by the user, 2026-10-16:** `per-list`, as recommended. In the user's words, relayed by the main session: "W44: per-list. A working solution in my own account takes a separate yes per list, as recommended. Carry on with sitting A." And in this session, in the user's own words: "W44: per-list. A working solution in my own account takes each list's own yes and execution-time confirmation; carry on with steps 3 to 5." The decision above stands as written; the design touch-up to A§7.3:582 stays on the list for the user's word at the end.

### W45 "A real person"

**Decision.** A real person is any recipient other than the bound user (PLAN §8 item 7, nodded). `notifies[]` holds strings: a monday user id (digits), `team:<id>`, or `email:<address>` for a sequence or mail recipient. A row whose `notifies` holds any entry other than `account.bound_user_id` needs its own yes at execution in either mode (`grouped` for a list row, `per-item` otherwise). A client user who agreed (A§9.5:910) is a real person too: the agreement limits who a sample-data row may notify, which is A11-2's ground, and does not replace the yes.

**Reason.** AM:18 (A28) takes the card's yes only where notifications reach the user alone, and A§9.5:910 sends every other recipient to its list's own yes.

**Follow-up.** Record-map edit: RM:123's `notifies[]` names the three forms.

### W46 The form of `assumption_refs`

**Decision.** An assumption, an assumed term and a fork built on its leaning carry ids of the forms `AS<n>`, `AT<n>` and `FK<n>`, which the frozen revision's "what this build rests on" section gives them. `intent --assumption-ref <id>`, repeated, sets `assumption_refs`, and each id must occur as a whole word in the frozen file of the row's `approval_ref`. `approval` fills `rests_on` itself: `clearance` from `STRAND.md`, `purpose` from `version.md`, and `assumptions`, `assumed_terms`, `forks_on_leaning` as the counts of distinct `AS`, `AT` and `FK` ids in the frozen file (zero where it uses none, as WP2's fixture). Whether each is confirmed or accepted stays in the record (`readiness.md`, `version.md`), never in the ledger.

**Reason.** BP:137 draws the refs from the frozen revision and AM:46 to 58 (A25) keeps confirmation in the record; deriving the counts from the same ids keeps `approval`'s flags few.

**Follow-up.** Design touch-up: A§3.4 (the blueprint's "what this build rests on" section) and BP's WP7 block give each item its `AS`, `AT` or `FK` id. Record-map edit: RM:115 names the three id forms beside the element-key table.

### W47 What `intent_digest` is, and how a changed row voids an approval

**Decision.** `intent_digest` is the first eight hex digits of the sha256 of W73's canonical JSON of the intended write: `{key, type, operation, name, parent_id, workspace, workspace_scope, refs, notifies, payload_sha256}`, with lists sorted and `payload_sha256` the sha of the payload file the session will send (`--payload-sha`, optional, null when absent). Reading one for voiding: `intent` refuses a row whose key is not in the table of its `approval_ref`'s frozen revision, whose type differs from the table's kind, or, on a create, whose name differs from the table's name. A change to a trigger, condition, action, recipient, prompt text or scope inside the payload voids the row by A§9.5:910 and is the session's to catch before the call, by comparing the payload with the frozen row; the ledger records the digest so the audit can see what was intended.

**Reason.** The table pins key, kind and name only (W42), which is what a script can compare without parsing a blueprint's prose; the fixture's eight-digit digests set the length.

**Follow-up.** None.

### W48 `irreversible-yes`'s interface

**Decision.** `irreversible-yes --strand <id> --key <key> [--key <key> ...] --mode per-item|grouped --what "<the step in plain words>" [--evidence "<containment evidence>"] [--log-ref "<log header>"] --lease-epoch --session-label --run-id --expect-sha <sha>`. It is fenced, so a yes belongs to the run that recorded it. It writes one entry per key, `{key, what, at, mode, approval_ref, evidence, log_ref}`, with `approval_ref` the key's row's ref. A `per-item` key must be in its approval's `irreversible_listed`; a `grouped` key must be in one of its four list arrays (K211 widened to the lists). An `archive` step needs `--evidence` (K215). The user's numbered answer ("yes to 1 and 3, not 2") is mapped to keys by the session, which passes only the keys said yes to (K213). `intent` accepts a yes for a row only when the entry's `at` is not earlier than the presented run's `started_at` (K214): a yes never carries to another run, so never to another session. Under `own-account-poc`, `intent` writes the `card` entry itself for a covered row (W10), and an explicit `per-item` or `grouped` yes is still accepted.

**Reason.** A§8.6:800 and :801 give the two forms and the never-carries rule, A§9.4:880 the evidence, and A§7.3:575 the entry; a session-label string would not tell runs apart, the run's start does.

**Follow-up.** Record-map edit: RM:123's `irreversible_yes[]` becomes `{key, what, at, mode, approval_ref, evidence, log_ref}` (W09, W56).

### Change check

### W49 `change-check`'s interface

**Decision.** `change-check --strand <id> --from <file>`. The session makes the four reads of A§8.6:794 and writes a JSON file `{ring, versions_seen[], release_notes_since, roster_diff {added[], removed[], renamed[]}, schema_diff[], result, approved_by_user}`; `change-check` validates it (K91 to K93, and `result` one of W08's two values) and writes `account.json.change_check` with `at` now and `for_strand` the `--strand` given, replacing the block whole. The judgement whether a change touches this build is the session's, recorded in `result`; `approved_by_user` is null or the header of the log entry holding the user's yes to go on. The gate sits in `intent`: it refuses a write unless `change_check.for_strand` is this strand, the local date of `change_check.at` is today's local date, and `result` is `no change affecting this build` or `approved_by_user` is set. `run start` does not need it, since the change check comes after the lease and the one question (A§8.6 steps 11 and 13). `change-check` is not fenced.

**Reason.** A§8.6:794 stops "before any write" and A§9.10:958 has the hook read "dated today"; the first write is `intent`, and the reads are the session's because the script has no monday access.

**Follow-up.** Design touch-up: BP's WP13 block, `guard.py` reads "dated today" as the local date of `change_check.at`, the same rule.

### `intent`, `record`, `verify`, `depart`, `ui-step`

### W50 `intent`'s and `record`'s interfaces

**Decision.** `intent --strand <id> --key <key> --operation create|update|archive|activate|publish|connect|convert|delete [--type <type>] [--name <name>] [--origin created|pre-existing-modified|other-strand-modified] [--parent-key <key>] [--parent-id <id>] [--workspace <id>] [--scope <id> ...] [--ref <kind>:<id> ...] [--notifies <recipient> ...] [--approval-ref vNrM] [--prompt-ref vNrM#KEY] [--ir IR-nn] [--sample-data] [--assumption-ref <id> ...] [--prior-state <file>] [--source-strand <short> --live-key <short>:<key>] [--evidence "<text>"] [--payload-sha <hex>] [--retry]`, with the three fence flags and `--expect-sha`. A planned row lends its type, name and refs; values given must agree with them. A key absent from `objects` is accepted only for an `item_batch` (`B1.IB<n>`, parent a board row of this strand). The operation must fit the row: `create` on a planned row, `update` on a `verified` or `written` row, `archive` on a row with an id, `activate` on an `activation` row, `publish` on a `publication` row, `connect` on a project, `convert` on a board; `delete` is refused for every kind (K173). Preconditions: an `activation` or `publication` row needs its parent `verified` (K162, K165), except `SQ1.ACT`, which is refused in v1 until sequences are probed (A§9.4:894); a project `connect` needs the row's `companions` to hold `tasks_board_id` and `overview_board_id` (K170); an automation row in `mismatch` is never retried: a second automation is not created while the first is live (A§9.5:910), and the row departs with a switch-off step instead. `--prior-state` (a JSON file, stored as its object) is required on `pre-existing-modified` and `other-strand-modified` and refused elsewhere (K127, K128); `other-strand-modified` also needs `--source-strand` and `--live-key`, a row of `live_objects` whose constraint is not `do-not-change` (K129, K130), stored in a new field `live_key`. Then come the change-check gate (W49), the scope checks (W41), the class and its yes (W10, W48), and the write: status `attempting`, `attempt {run_id, started_at, intent_digest}` (W47), every field given, `irreversible` by class, and under `own-account-poc` the `card` entries of W10.

`record --strand <id> --key <key> [--id <id>] [--item-id <id> ...] [--url <url>] [--companion <name>=<id> ...] [--timed-out] [--id-from-error] [--pending --polled-seconds <n>]`, with the fence flags and `--expect-sha`. With an id (or the item ids of a batch) it moves `attempting` to `written`; after an `archive` intent it moves the row to `removed` with `state: "archived"`. `--timed-out` with no id leaves the row `attempting` and says "possibly applied: reconcile before any retry" (K182); `--id-from-error` stores the id read out of an error payload and leaves the row `attempting`; `--pending` (an asynchronous kind with no handle yet) leaves it `attempting` and reports the poll ceiling (W54). A `workspace` row's `workspace` becomes its own id; a `subitems` row's id is also written into its parent board's `companions.subitems_board_id`; `--companion` sets a project's `tasks_board_id`, `overview_board_id`, `planner_board_id` or `folder_id`.

**Reason.** A§8.6:797 to 799, A§9.4 and A§9.5:910 give the order, the preconditions and the error paths; flags keep each call testable without a payload format the ledger would have to own.

**Follow-up.** Record-map edit: RM:123's `objects` gains `live_key`. Design touch-up: BP's WP9 block (`build-loop.md` passes these flags).

### W51 `verify`'s interface, and how it learns the read

**Decision.** `verify --strand <id> --key <key> --result match|mismatch|not-checkable|needs-user --read <file> [--note "<text>"]`, with the fence flags and `--expect-sha`. The file is `{"read": "<the read made: the query or tool and its fields>", "object": {<the fields the read returned>}, ...}`; an empty `read` or `object` is refused (K189), and `not-checkable` and `needs-user` need `--note` saying who checks and how (K190). The script compares what it can and records the rest: it computes `verify.digest` from `object` by W73, sets the status by W13, and for a `pre-existing-referenced` row stores `id`, `workspace` (`object.workspace_id`) and `role` (W17). Per kind: `match` is refused for `ai_column`, `sequence`, `webhook` and `widget` (K169, K198), for a workflow `publication` row (its live trigger binding is not readable, K197: it is `needs-user`, naming the sandbox trigger test), and for an `object` that carries `column_permissions`, `item_permissions` or `subitem_permissions` (K199). An `agent` read must carry `plan`, `state`, `version_id`, `triggers[]` and `knowledge[]` (K192); the two default triggers, "When agent is mentioned" and "When agent is assigned", are expected and never extras; a `skills` key is refused, since no per-agent skill read exists (K193); `match` is refused while `plan` differs from the frozen prompt of `prompt_ref` (K191) and while `state` is `ACTIVE` with the row's activation not verified (an update can activate, AI:17). A `vibe_app` read must carry `status`, `is_published`, `code_version` and `differs_from_request` (true or false); `match` needs `status` `READY` (K195), and when `differs_from_request` is true, a non-empty `user_yes_to_difference` and `difference`, both copied into `verify.note` (K194). A `workflow` read needs `state` and `validation`, and `match` needs `validation` to be `no issues`. A project `connect` read carries `link_board_ids` and `row_board_ids`; `match` needs the tasks board in both, and one half only is `needs-user` with the note "partial link" (K200). A new field `read_values {}` keeps what A§7.3:582 asks to keep: an agent's `state` and `version_id` (and `version_id_at_build` takes the `version_id` of each matching read), a Vibe app's `status`, `is_published` and `code_version`, a workflow's `state`.

**Reason.** BP:137's refusals need the plan text and the Vibe difference in the script's hands, A§10.4:1028 and AI:16 to 21, :35 to 48 and :55 to 68 give each kind's read and its blind spots, and the session alone can make the read.

**Follow-up.** Record-map edit: RM:123's `objects` gains `read_values {}`.

### W52 The agent's `version_id` and the prompt comparison

**Decision.** `version_id_at_build` is the `version_id` of the read that last verified the agent as a match: the final read-back after the plan write, the deactivation, the triggers and the grants (AI:21: it moves with the plan only, so the moment inside the build does not change it). A later plan change in a fix run or a later version (`intent --operation update`) is verified again, and its match replaces the value, the version joining `changed_in[]`. The frozen prompt reaches the comparison through `prompt_ref` (W42): `verify` reads the prompt block from the frozen file itself, and compares it with the read's `plan` after line endings are normalised and trailing newlines dropped. No prompt hash is kept.

**Reason.** BP:137 asks for the `version_id` after the plan write and AI:10 returns the plan in full; reading the frozen file at verify time is exact and needs no extra field.

**Follow-up.** None.

### W53 The Vibe difference and the user's yes

**Decision.** The difference between the delivered app and the request is the session's reading (code versions, the build conversation, `vibe_ask`), handed to `verify` in the read file as `differs_from_request`, `difference` and `user_yes_to_difference`; `verify` refuses `match` while the app differs without the user's words, and records both in `verify.note` (`"differs: <difference>; the user's yes: <words>"`). The request text is the frozen `### Prompt VB1` block. `VB1.PUB` needs `VB1` verified, so a publication always follows the diff (K165).

**Reason.** AI:41 and :48 make the diff the audit's main job and a reading only the session can make; BP:137 asks the script to require the user's yes.

**Follow-up.** None.

### W54 Poll ceilings per asynchronous kind

**Decision.** `ledger.py` holds one table of poll ceilings, outside the pinned vocabulary: portfolio and project 120 seconds, Vibe app 300 seconds, each polled every 10 seconds. `record --pending --polled-seconds <n>` below the ceiling leaves the row `attempting` and says "keep polling"; at or past it, it leaves the row `attempting` and says "not found by the ceiling: run reconcile, then retry or depart". `estimate` counts 4 to 12 polls for a portfolio or a project and 6 to 30 for a Vibe app (W65).

**Reason.** G-71 and A§11.1:1056 ask for at least a minute and saw boards after 35 seconds, and AI:40 saw a Vibe app ready after about a minute; doubling the observed for portfolios and projects, and allowing five minutes for a generator, keeps a ceiling stated (A§8.6:798).

**Follow-up.** Design touch-up: BP's WP9 block, `build-loop.md` cites these ceilings.

### W55 `depart`'s and `ui-step`'s interfaces

**Decision.** `depart --strand <id> --key <key> --what "<what failed>" --error-code <code> [--attempt <form> [--attempt <form>]] --decision ui-step|blueprint-revision|later-retry [--ui-what "<step>" --ui-owner "<owner>"]`, with the fence flags and `--expect-sha`. It appends `{key, version, what, error_code, attempts[], decision}` and moves the row to `departed`. `attempts[]` holds the call-form labels tried (`flat`, `wrapped`, `tool`, `raw`), at most two (K205); `error_code` is the code read out of the error's message, never empty (K206), and `UNPROBED` with no attempt for a kind built as a UI step because it has no probe yet (an AI column, A§8.6:797). With `--decision ui-step`, `depart` also appends the UI step in the same write and the decision reads `ui-step U<n>`. `ui-step --strand <id> [--key U<n>] --what "<step>" --owner "<owner>" --target-version vX.Y` appends `{key, what, owner, target_version, status: "open"}`; without `--key` it takes the next free `U<n>` after the table's `U` keys and the existing steps; `ui-step --strand <id> --key U<n> --done` sets `done`. `owner` is `the user` or a role, non-empty. `ui-step` is not fenced, since a UI step may be recorded or ticked off outside a run; `--expect-sha` applies.

**Reason.** A§8.6:799 gives the three choices and the one different call form, A§7.3:576 and :577 the entries, and A§7.3:582 makes `U1` a blueprint id, so a key minted at build time must not collide with one.

**Follow-up.** Record-map edit: `Pinned: ledger` gains the decision tokens and `ui_steps` statuses; RM:123's `departures[].decision` names the `ui-step U<n>` form.

### W56 `removed`, archive and containment

**Decision.** An archive is a row's status `removed` and state `archived`: `intent --operation archive` (class `removed`, W10) then the call, then `record`, which sets both (W50); `verify` then records the archive's read-back (`state: archived` through `state: all`) on the `removed` row. v1 never deletes. The containment evidence an archive shows is stored in a new field `evidence` on the `irreversible_yes` entry (`irreversible-yes --evidence`, or `intent --evidence` for the `card` entry under `own-account-poc`); an archive without it is refused (K215).

**Reason.** A§9.4:896 and :900 archive instead of deleting, A§7.3:582 has `removed` as a status and A§7.8:700 `archived` as a state, and A§8.6:800 asks for the evidence.

**Follow-up.** Record-map edit: RM:123's `irreversible_yes[]` gains `evidence` (with W48).

### W57 `read-back.md` lags A§10.4

**Decision.** `ledger.py` follows A§10.4:1028: the agent, Vibe app and workflow reads of W51 are named, and AI columns, sequences and webhooks stay `not-checkable` until probed. RB:53's "no read is named yet" is stale and the code does not read `read-back.md`.

**Reason.** A§10.4:1028 wins over RB:53 by the authority order, and A§8.6:798 sends each write to "the read named in `shared/read-back.md`", which therefore has to catch up.

**Follow-up.** Shared edit, for the user's word, not needed before stage 2 acceptance: `read-back.md` line 53 becomes three rows (agent, Vibe app, workflow) with A§10.4's reads, compares and blind spots, and one row for AI column, sequence and webhook: `not-checkable` until probed.

### W58 Parent keys across strands

**Decision.** A `parent_key` is a bare key of the same ledger, or, for a parent another strand built, its qualified live-map key (`001:W1`), which must be a row of `account.json` `live_objects` whose `monday_id` equals the row's `parent_id`. No other qualified key is accepted in a strand's ledger (K152 holds for row keys). `check` resolves both forms.

**Reason.** RM:77 qualifies every reference that leaves the strand, A§8.9:823 and AM:83 build a later strand into an earlier strand's workspaces, and A§7.1:434 keeps the session out of the other strand's `build.json`, so the live map is the one place the parent can be found.

**Follow-up.** Record-map edit: RM:77 and RM:123 say a `parent_key` may be a qualified live-map key.

### The live map

### W59 The live map's fields and states

**Decision.** The table's header is A§7.8's ten columns: `key | monday id | kind | workspace | built by | state | constraint | source | dependants | last verified`. Each column is a `live_objects` field: `monday_id`; `kind` (the `objects[].type` token, so `ai_column` and `vibe_app`, never the prose "AI column"); `workspace` (the workspace id, or for an account-level object `account: <id>; <id>` with its scope); `built by` (`introduced_in`, a qualified version, or `client` or `native`, which `live_objects.introduced_in` then holds); `state`; `constraint`; `source` (`constraint_source`); `dependants` (joined with `, `, or `none`); `last verified` (`last_verified`, a local date). `name_at_build` and `digest` are kept in `live_objects` only: "mirrored field for field" is read as every map column being a `live_objects` field. `state` is `active`, `archived`, `inactive` (an agent, workflow, sequence or automation that exists but does not run) or `removed-by-platform`. Rows are sorted by key, which groups them by strand, in one table; past the 250-line budget `record.py check` warns, and no sub-headings are written in v1. A pipe inside a cell is written `\|`. The front matter is `schema: "live-map/1"`, `client`, `rows` (the row count as a string) and `updated` (the local minute), and the line "Internal: never client-facing" follows it. A map written with RM's nine columns (WP2's fixture) is read with `workspace` null and no finding, and rewritten in ten columns at the next write (W06).

**Reason.** A§7.8:693 to 704 wins over RM:129 to 134 and gives the `workspace` column and `inactive`; `record.py check` reads only the first cell, so the extra column changes nothing it does.

**Follow-up.** Record-map edit: RM:129 to 134, the ten-column header and example, `inactive`, and the kind tokens. Design touch-up: A§7.8:697's kind list uses the type tokens.

### W60 Which rows `run end` writes

**Decision.** For every row of the strand with status `verified`, of every type but `item_batch`, `run end` writes the `live_objects` row `"<short id>:<key>"` and its map row. A `pre-existing-referenced` or `pre-existing-modified` row gets `built by` `native` when its id is in `native_board_index`, else `client`. An `other-strand-modified` row creates no row of its own: it refreshes the row its `live_key` names (W61). A `removed` row whose live row exists sets that row's state to `archived`. `departed`, `planned`, `attempting`, `written` and `mismatch` rows get nothing (K119). Workspaces are rows like any other (K226). A new row takes the interim `change-with-own-yes` with source `pending strand close` (K118), `owner_strand` the strand, `introduced_in` the row's qualified version, `digest` and `last_verified` from its matching `verify`, and `dependants` the qualified keys of the strand's verified rows whose `parent_key` is this row.

**Reason.** A§7.8:706 creates a row only for a verified object and shows natives and client objects with their own `built by`; an item batch is sample data, not structure.

**Follow-up.** Record-map edit: RM:134's sentence on `run end` names these rules.

### W61 `run end` against promoted constraints

**Decision.** When the row exists, a later `run end` refreshes `monday_id`, `kind`, `workspace`, `state`, `digest`, `last_verified` and `dependants`, and keeps `name_at_build`, `owner_strand`, `introduced_in`, `constraint` and `constraint_source` exactly as they are (K232). Only `live-map set` changes a constraint.

**Reason.** A§7.8:718 gives the strand close, through `live-map set`, the promotion of a constraint, and a constraint the client stated must not be reset by a rebuild.

**Follow-up.** None.

### W62 `live-map set`'s interface and ownership

**Decision.** `live-map set --key <qualified key> --constraint do-not-change|change-with-own-yes|free --source "<source>" --strand <short id>` sets one row's `constraint` and `constraint_source`, in `account.json` and then the map (W25). It refuses a key with no row (K228), another constraint (K229), an empty source or `pending strand close` (K230), and a row whose `owner_strand` is not `--strand` (A§7.8:708: a strand edits only the rows it built). One row per call. It is not fenced: a strand close runs with no lease held. `live-map --strand <id>` (no action) renders the map from `live_objects` and writes nothing else.

**Reason.** BP:135 sets one row's constraint and source, A§7.8:708 forbids editing another strand's row, and A§8.10:829 runs the strand close with the lease free.

**Follow-up.** Design touch-up: BP:135, "take `--strand` only to stamp who asked" gains "and `live-map set`, which also refuses a row its strand did not build".

### `check`

### W63 What `ledger.py check` validates

**Decision.** `check [--strand <id>]` reads `account.json`, every strand's `build.json` (or the one named), `live/live-map.md` and every frozen file an approval or a ref names, inside the mutex, and writes nothing. Blocking: a schema unknown or newer (K234); a block or field of contract section 3 missing or of the wrong type, the added fields read by W06's defaults (K235, K236); a value outside its vocabulary for `type`, `origin`, `status`, `state`, `verify.result`, `approval_mode`, `irreversible_yes[].mode`, run `kind` and `state`, `constraint`, UI step `status` and the reconcile classes (K237); an id stored as a number (K238); a parent key that does not resolve or a `parent_id` that disagrees (K239, W58); `prior_state` where the origin forbids it or missing where it needs it, and an `other-strand-modified` row without `source_strand` or `live_key` (K240); a row without an `approval_ref` or with one that resolves to no entry, and an `irreversible_yes` entry whose key is listed nowhere or whose ref does not resolve (K241, K249); an approval whose `sha256` is not its frozen file's (K242); the key half of a `blueprint_ref` or `prompt_ref` that the frozen table does not hold (K243); an `other-strand-modified` row whose live row is `do-not-change` (K244); a `workspace` or `workspace_scope` id outside `client_workspace_ids`, or an account-level row without a scope (K245); a `verified` row whose `verify.result` is not `match`; two `running` runs in one strand; a live-map row and a `live_objects` row that differ in any column, or a row on one side only; and, as `record.py check` also blocks them, an `account_id_at_bind` that is not `account.id` and a build target outside the client's workspaces. Warnings: a frozen file without the element-key table (W42); a native index older than `record_provenance.staleness_budget_days` (A§5.4:355); a `running` run whose `build.json` `heartbeat_at` is more than 60 minutes old ("recovery first", A§8.11). The output is `{"ok", "command": "check", "findings": {"blocking": [], "warnings": []}, "shas": {...}}` (W34), exit 1, 2, 0 or 3 (K247).

**Reason.** A§7.1:390 and :417 make both files "pass `ledger.py check`" and A§5.4:356 lists the checks the ledger owns; repeating `record.py`'s two ledger checks keeps "passes `ledger.py check`" true on its own.

**Follow-up.** Record-map edit: a short paragraph after RM:123 lists what `ledger.py check` blocks and warns on, and RM:16 and RM:44 ("passes `ledger.py check`") point at it; the paragraph stays outside `Pinned: ledger`, whose backticked tokens the lint matches one for one.

### `estimate`

### W64 `estimate`'s interface and inputs

**Decision.** `estimate --strand <id> [--inputs <file>] [--write --expect-sha <sha>]`. The element counts come from the strand's own rows with status `planned` or `attempting`, by type. Everything the ledger cannot know comes in the inputs file, from the session's preflight reads: `{daily_total (platform_api's daily limit, or null when it cannot be read), used_today, client_reserve, roster_ok, stale_gotchas[], workspaces_ok, findings[], items, updates, automation_actions_monthly, plan_allowance (or null), boards_to_classify, portfolios, doc_pages}`, every count an integer, every absent count 0. Without `--write` it only prints. With `--write` (the inputs file required) it writes `build.json` `preflight` (`at`, `version`, `daily_total`, `used_today`, `client_reserve`, `estimated_calls [low, high]`, `roster_ok`, `stale_gotchas`, `workspaces_ok`, `findings`) and sets the running run's `calls_estimated` to the same pair; it is not fenced. The output: `calls [low, high]`; `components` (each W65 line as `[low, high]`); `classification_query {calls, complexity, paid, window_days}`; `classification_side_reads {calls, complexity}`; `automation_actions {monthly, allowance, over}` (`over` null without an allowance, K255); `ai_powered[]` and `may_be_ai_powered[]` (W69); `other_strands[]` (W67); `headroom` (the daily total, or 1,000 when unread, minus today's usage and the client reserve) and `headroom_after_others` (less the other strands' high figures); `warnings[]`: the estimate's high figure above 30% of the headroom, with the offer to split the build across days (K259), and, when `daily_total` is null, a high figure above 250 (K260).

**Reason.** A§9.9:952 lists the components and the warnings and A§8.6:795 makes preflight the moment they are read; writing `preflight` here gives the block its writer (W24) without a new subcommand.

**Follow-up.** Record-map edit: RM:123's `preflight` names `estimate --write` as its writer.

### W65 The cost figures

**Decision.** One table in `ledger.py`, with its sources beside each line. For `w` the strand's rows that are not item batches, `i` the seed items, `u` the item updates, `n` the boards to classify and `p` the portfolios:

| Component | Low | High |
|---|---|---|
| preflight | 12 | 12 |
| writes | `w + ceil(i/20) + ceil(u/40)` | low plus a fifth, rounded up (one different call form, A§8.6:799) |
| read-backs | as writes, low | as writes, high |
| polls | 4 per portfolio or project, 6 per Vibe app | 12 per portfolio or project, 30 per Vibe app (W54) |
| account checks | `1 + ceil(writes low / 20)` | low plus one per row whose class is not `card` (SF 3) |
| audit | 3 per board, subitems, portfolio or project row, plus `doc_pages`, plus 3 per agent, 1 per Vibe app, 1 per workflow | the same |
| classification query | `ceil(n/50)` calls; `3,600 n` complexity | `ceil(n/25)` calls; `5,300 n` complexity |
| classification side reads | `4 + p` calls (workspaces, docs, two workflow-object states, one items page per portfolio); `167,000 p` complexity | `4 + 2p + ceil(n/25)` calls (a second items page each, lineage hops); `334,000 p` complexity |

Complexity is reported, never added to the calls; the calls total sums the rows above, the two classification lines only when the query is not already paid (W66).

**Reason.** NO 2.6:57 gives 25,000 to 90,000 for pages of 7 to 17 boards (about 3,600 and 5,300 a board) and 167,022 for one items page; A§9.9:952 gives preflight, the batches, one read-back per write or batch, the polls, the account checks and about 3 calls per board of audit; no source gives more, so the table states what it assumes.

**Follow-up.** Design touch-up: A§9.9:952 points at the table in `ledger.py` for the figures.

### W66 The staleness window

**Decision.** The window is `guard_index.record_provenance.staleness_budget_days`, the same budget R-J reads (NO 6.3). The classification query is `paid` when `guard_index.captured_at` is set and less than that many days old: it then counts zero calls and zero complexity in every strand's estimate, and says so. Otherwise it counts in the estimate of the strand that asks, and once `native-map` stores a fresh read (`captured_at` now), every later estimate inside the window sees it paid (K261).

**Reason.** A§9.9:952 and A§11.2:1065 pay it once per record per staleness window, and the record holds one budget and one capture time.

**Follow-up.** None.

### W67 What "approved-but-unbuilt" counts

**Decision.** Another strand is open when its `STRAND.md` `state` is `active` or `paused`. Its approved-but-unbuilt figure is W65's writes, read-backs, polls and account checks over its rows with status `planned` or `attempting`, which covers a strand approved and not yet preflighted and a strand part-way through a run alike; preflight, audit and the classification query are left out, being per run or per record. A strand with none is not listed.

**Reason.** BP:138 compares the strands against one daily allowance; the rows are the one figure every strand has whatever its stage, while `preflight.estimated_calls` exists only after a preflight.

**Follow-up.** None.

### W68 `estimate` against H39

**Decision.** PLAN §8 item 8 (nodded): the script reads each other open strand's `build.json` itself, only the `type` and `status` of its rows, and prints `{"strand": "<short id>", "calls": [low, high]}` per strand: no key, name or id of the sibling (K258). The session reads nothing of the sibling's.

**Reason.** BP:508 (H39) forbids the session reading 001's `build.json`, and BP:138 needs 001's figure; the script is not the session.

**Follow-up.** Design touch-up: A§7.1:434's reading contract adds "a script may read another strand's ledger and print totals only".

### W69 The AI-powered set

**Decision.** `ai_powered[]` lists the strand's planned keys of type `agent`, `ai_column` and `vibe_app`. `may_be_ai_powered[]` lists its `workflow` and `sequence` keys, with the note "AI-powered when the blueprint gives them an AI step", since a row's type does not say. No credit figure, price or package appears anywhere in the output, and a credit field a read returns is reported as present and nothing more (K263).

**Reason.** AM:117 (A17) names agents, AI columns and Vibe apps and forbids pricing; A18's workflows and sequences may or may not hold an AI step.

**Follow-up.** None.

### `reconcile` and the digest

### W70 The live inventory's shape, and how the session hands it

**Decision.** The session writes its reads into a file and passes it: `reconcile --strand <id> --inventory <file>` validates it, copies it to `.work/strands/<id>/live-inventory.json` and reads that copy; without `--inventory`, `reconcile` reads the copy already there (K278). The shape, `live-inventory/1`:

```text
{"schema": "live-inventory/1", "strand": "001", "read_at": "<UTC>", "ring": "<kind> <value>",
 "workspaces": [{"id", "name", "kind"}],
 "boards":     [{"id", "name", "type", "state", "created_at", "workspace_id", "board_folder_id",
                 "object_type_unique_key", "hierarchy_type"}],
 "folders":    [{"id", "name", "workspace_id", "created_at"}],
 "docs":       [{"id", "object_id", "name", "workspace_id", "created_at"}],
 "automations":[{"id", "board_id", "title", "active", "created_at", "updated_at"}],
 "dashboards": {"requested_ids": [], "returned": [{"id", "name", "workspace_id", "kind"}], "missing_ids": []},
 "agents":     [{"id", "name", "state", "version_id", "created_at"}],
 "vibe_apps":  [{"id", "name", "status", "is_published", "code_version", "board_ids", "created_at"}],
 "workflows":  [{"id", "name", "state", "workspace_id", "published", "active"}]}
```

The boards are `boards(workspace_ids, state: all)` over the client's workspaces, the automations `list_automations` on every board the run touched, the dashboards read by stored id with the id diff of G-92, the agents `manage_agent list` (P-19), the Vibe apps `vibe_list` (P-20), and the workflows the `objects` read with what the draft read and `validate_workflow` showed (P-21); every field but the connector shapes is in the 2026-10 schema. Times are UTC `YYYY-MM-DDTHH:MM:SSZ` or null; `strand` must be the `--strand` given; a synthetic copy may carry the `fixture` header of W01. The key a live object is matched on is W71's, per kind.

**Reason.** A§8.11:835 names the reads and the file, and the schema settles the fields the GraphQL reads return (`Folder`, `Document` and `BoardAutomation` carry `created_at`; `Dashboard` and `Object` do not, which W71 allows for).

**Follow-up.** Record-map edit: RM:68's `live-inventory.json` points at a new `live-inventory/1` shape paragraph.

### W71 The operational test per reconcile class

**Decision.** `reconcile` gives every row of the strand at most one class, and every unclaimed live object one, by these tests. A live match of a row, per kind: a `workspace` by id, else by name; a `board`, `subitems`, `portfolio` or `project` row a live board with the row's name, the row's workspace (or, inside a folder row, that folder's id as `board_folder_id`), the matching `type` (`board`, `sub_items_board`) or key (`work-management::portfolio`, `work-management::portfolio-project` or `::project`) and a state other than `deleted`; a `folder` or `doc` by name and workspace; an `automation` by `board_id` equal to its parent board's id and a title equal to the row's `name` after whitespace is collapsed and case folded, or a live title of at least 40 characters that the row's name begins with (the stored title is the request cut short, SF 5); a `dashboard` by stored id only; an `agent` by name; a `vibe_app` by name and bound boards (its `board` refs, as a set); a `workflow` by name and workspace; a `publication` or `activation` row by its parent's live entry (a workflow's `published`, an agent's `state` `ACTIVE`, a Vibe app's `is_published`). Groups, columns, views, forms, widgets, item batches, AI columns, sequences and webhooks are in no inventory: they are listed under `not_in_inventory` with their status and the read to make. A live object is claimed when its id is a row's `id`, `item_ids`, `companions` value or a doc row's container (`object_id`), or a `live_objects` `monday_id`, or in `native_board_index`.

| Class | Test |
|---|---|
| `adopt` | an `attempting` row whose recorded id (read from an error) is live, or which has no id and exactly one unclaimed live match created at or after `attempt.started_at`. An adopted automation carries `confirm: true` always (a lost `create_automation` reply needs the user's re-confirmation after seeing the board's automation list, on an own-account proof of concept too, K277); an agent carries `needs_read: "manage_agent get"` (its `update` reply is stale on the plan); a workflow, and any match whose `created_at` the read lacks, carries `confirm: true` |
| `retry` | an `attempting` row with a recorded id that is not live, or with no unclaimed live match created at or after its attempt started |
| `duplicate` | an `attempting` row with two or more unclaimed live matches created at or after its attempt started (or, with no `created_at`, two or more matches); every candidate id is listed, and each but the one the user keeps becomes an archive proposal (boards, docs, items) or a deactivation proposal (agents; for an automation, a switch-off step), each with its own yes |
| `partial` | a row whose live object exists but is not complete: a `written` or `mismatch` row whose id is live; a `verified` row whose live digest is unchanged while a row under it (by `parent_key`) is not `verified`; a Vibe app whose live `status` is not `READY` |
| `changed-since-verified` | a `verified` row whose live object is present and whose identity digest (W73) over the inventory's fields differs from `verify.digest` |
| `unrecorded-extra` | an unclaimed live object of the strand's target workspaces (`build_targets_by_strand`), or an unclaimed agent or Vibe app created at or after the strand's earliest attempt; one that predates the attempt of a row it matches is listed with `predates_attempt: true` and is never offered for adoption (K272) |
| `missing` | a `written`, `mismatch` or `verified` row whose id is not live, or is live in state `deleted` |

A `verified` row with nothing changed and nothing incomplete is listed under `unchanged`, `planned` rows under `not_started`, `departed` and `removed` rows under `not_reconciled`: none of these takes a class. The output lists elements in this order (K274, K275): automations, then agents, then Vibe apps, then workflows, then every other kind in key order, a kind's unrecorded extras after its rows; each element is `{key or null, kind, class, live_ids[], confirm, needs_read, predates_attempt, note}`. `classes` holds the seven counts, zero where empty (K284).

**Reason.** A§8.11:835 and SF 9 give adopt, duplicate and unrecorded extra in prose, the lost-reply rules and the order; the four other classes follow the status chain (W13), so each test reads only a row's status, its attempt time, its digest and the inventory.

**Follow-up.** Record-map edit: `Pinned: ledger` carries the seven tokens; a paragraph after RM:123 gives the table above. Design touch-up: A§8.11:835 points at it for the tests.

### W72 What `reconcile` writes, and under what authority

**Decision.** (a) `reconcile --strand <holder> --classify-only [--asked-by <short id>] [--inventory <file>]` writes the holder's `build.json` once: the run whose `id` is the lock's `run_id` (read through `mmb_common.lease_status`, never from the lock itself) gets `state: "interrupted"` and `reconcile {at, mode: "classify-only", classes, findings[]}`, `findings` being `{key, class, live_ids, note}` per element; a second call replaces the object. It refuses unless the lease is held by `<holder>` and is not fresh (a live holder's run is never marked from outside). A run already `ended` is marked `interrupted` too: that is the case of a `run end` cut between its run write and its release (W25), and the mark is what lets a break meet condition 4. With no run id on the lock nothing can have been written: no run is marked, the classes are printed, and G04's condition 4 holds as WP2 built it. A lock run id with no run in the holder's ledger is refused, naming it. (b) `reconcile --strand <id>` without `--classify-only`, run in the holder's own session after a takeover, writes nothing but the inventory copy and prints the plan for the user's approval (A§8.11:835); its output says `"mode": "full"`, a value that never enters a ledger. Adoption, retry and departure then go through `record`, `intent --retry` and `depart` in a new run. (c) Neither form is fenced, and the classify-only form takes no sha (W34); both run inside the mutex. (d) The covered edge cases are above.

**Reason.** BP:139 and A§8.11:837 write the classes into the holder's ledger as findings without a lease, G04's break reads the object, and A§8.11:835 has the user approve the plan before anything is adopted.

**Follow-up.** Record-map edit: RM:123's `reconcile` becomes `{at, mode, classes, findings[]}` (`lease_break` reads only `classes`, so WP2's code is unchanged).

### W73 What a digest is

**Decision.** One function, in `ledger.py`: `digest(prefix, fields)` is `prefix + ":" +` the first eight hex digits of the sha256 of `json.dumps(fields, sort_keys=True, separators=(",", ":"), ensure_ascii=False)` encoded as UTF-8, where `fields` is the kind's field list with every absent field null, ids as strings, id lists sorted, and object lists sorted by `id`. The script computes every digest itself, from the read it is handed. A row's digest (`verify.digest`, then `live_objects.digest`) has the row's bare key in lower case as its prefix (`b1:`, `b1.c3:`, `ag1:`) and these identity fields: workspace `name, kind`; folder `name, workspace_id`; board, subitems, portfolio, project `name, type, state, workspace_id, board_folder_id`; doc `name, workspace_id`; automation `active, updated_at`; dashboard `name, workspace_id, kind`; agent `state, version_id`; Vibe app `status, is_published, code_version`; workflow `name, state`; group `title, color, position`; column `id, title, type, settings`; view `name, type, settings`; item batch `item_ids`; publication and activation the parent's `state` or `is_published`. The same fields are what the inventory carries, so `reconcile` and the audit's protected rows recompute them. A snapshot's own digests use the prefixes `columns` (`id, title, type, revision, settings` per column), `groups`, `views`, `form`, `plan`, `triggers` and `grants` (W74). `intent_digest` is the same hash with no prefix (W47).

**Reason.** A§7.3's examples and WP2's fixture show a key prefix and eight hex digits, and A§9.7:928 lists what a column digest covers; one canonical form makes a digest recomputable by `verify`, `reconcile`, `snapshot` and the fixture self-test alike.

**Follow-up.** Record-map edit: RM:123 defines `digest` by this paragraph.

### `snapshot` and `compare`

### W74 `snapshot`'s shape and interface

**Decision.** `snapshot --strand <id> --label before|after --read <file>` writes one new file (W19) from the read the session hands it; the version is the strand's `STRAND.md` version. The read file:

```text
{"read_at": "<UTC>", "ring": "<kind> <value>",
 "inventory":   [{"id", "name", "type", "state", "description", "updated_at", "board_folder_id", "board_kind", "workspace_id"}],
 "boards":      [{"id", "columns": [{"id", "title", "type", "revision", "settings"}],
                  "groups": [{"id", "title", "color", "position"}], "views": [{"id", "type", "settings"}],
                  "owners": ["<id>"], "subscribers": ["<id>"]}],
 "automations": [{"id", "board_id", "active", "updated_at"}],
 "forms":       [{"board_id", "view_id", "form": {<get_form's reply>}}],
 "docs":        [{"id", "block_count"}],
 "dashboards":  [{"id", "name", "workspace_id", "kind"}],
 "agents":      [{"id", "state", "version_id", "plan", "triggers": [], "knowledge": []}],
 "workflows":   [{"id", "name", "state"}],
 "vibe_apps":   [{"id", "status", "is_published", "code_version"}]}
```

The file written, `snapshot/1`: `{schema, strand, version, label, taken_at, read_at, ring, ledger_sha256, account_sha256, scope {boards[], live_rows[], dropped[]}, inventory[], boards[] of {id, columns_digest, groups_digest, views_digest, owners, subscribers}, automations[], forms[] of {board_id, view_id, form_digest}, docs[], dashboards[], agents[] of {id, state, version_id, plan_digest, triggers_digest, grants_digest}, workflows[], vibe_apps[], protected[] of {key, monday_id, recorded_digest, digest_at_snapshot, moved}}`. The scope is the strand's own rows of board kinds, agents, workflows and Vibe apps that have ids, plus every `live_objects` row marked `do-not-change` or `change-with-own-yes`, whatever strand built it (K287). The inventory keeps every board of the client's workspaces; every other part keeps in-scope objects only. A read entry outside the scope is trimmed, not refused, and its id is listed in `scope.dropped` and in the output (a read over the client's workspaces always holds other boards). `ledger_sha256` and `account_sha256` are the two files' `sha256_file` at that moment. `protected[]` holds, per in-scope live row whose kind the read covers, the recorded `live_objects.digest`, the identity digest recomputed from the read (W73), and `moved` when they differ, so a row that moved before the before snapshot is known at once (A§9.7:928). `compare --before <path> --after <path> [--appendix <path>]` takes two record-relative snapshot paths of the same strand and version, labelled `before` and `after`, and refuses any other pair.

**Reason.** A§9.7:928 lists what a snapshot covers and how its scope is drawn, and the script has no monday access (K290), so it digests the reads it is handed and keeps the digests, never the raw reads.

**Follow-up.** Record-map edit: a `snapshot/1` shape paragraph beside RM:26.

### W75 The compare scope

**Decision.** Reading two, inside the snapshot's scope: `compare` flags every difference between the two snapshots in the fields A§9.7 lists, a superset of BP:140's six. Flagged: an inventory board that appears or disappears, or whose `name`, `type`, `state`, `description`, `board_folder_id`, `board_kind` or `workspace_id` moved; an in-scope board's `columns_digest`, `groups_digest` or `views_digest`, its `owners` or its `subscribers`; an automation's `active` or `updated_at`, or one that appears or disappears; a form's `form_digest`; a doc's `block_count`; a dashboard's `name`, `kind` or `workspace_id`; an agent's `state`, `version_id`, `plan_digest`, `triggers_digest` or `grants_digest`; a workflow's `name` or `state`; a Vibe app's `status`, `is_published` or `code_version`; `ledger_sha256` and `account_sha256` (K302). Not flagged: a board's `updated_at` (an item write or a client's own activity moves it, and the audit's activity check is not the ledger's) and anything dropped from the scope. The fixture's controls are unchanged pairs and a board whose only change is its `updated_at`. A protected row with `moved` true in the before snapshot is reported as changed outside this strand (K300), never as a write during the window.

**Reason.** A§8.7:810 voids an audit on "any changed digest, state, description, plan text or active flag", which BP:140's six do not exhaust, and A§9.7:928 sets the fields; the activity-log and tool-call checks belong to the audit skill.

**Follow-up.** Design touch-up: BP:140, "flags a description change, ..." becomes "flags every change A§9.7 lists, among them a description change, ...".

### W76 `compare`'s output, exit code and writes

**Decision.** `compare` writes nothing. It prints `findings {blocking: [...], warnings: [...]}` as `check` does: each flag and each refused document is blocking; each changed-outside row is a warning. A flag's four parts are the after snapshot's path, the field `<kind>:<id>.<field>` (`board:90300000012.description`), the problem `<before> to <after>`, and the expected "unchanged during the audit window"; a changed-outside row's expected is "a finding against the record, reported as changed outside this strand, never fixed here". Exit 1 when anything blocks (the audit is `write-detected`, which is the audit's verdict to write, A§8.7:810), 2 when only warnings remain, 0 when nothing differs. BP:135's list of record-level commands is read as "write no strand ledger", which `compare` keeps by writing nothing.

**Reason.** A§8.7:810 gives the verdict to the audit and A§7.8:716 keeps a changed-outside row from voiding the strand's own result, so the two need different severities; `check`'s envelope already carries both.

**Follow-up.** Design touch-up: BP:135 and A§5.4:356, "Record-level subcommands ... write `account.json`" becomes "write no strand ledger: those that write, write `account.json` or a record-level file under `live/`, and `classify` and `compare` write nothing".

### W77 The tokenizer's scope

**Decision.** The documents appendix is the `## Documents appendix` section of the file `--appendix` names, to the next level-2 heading or the end. Its documents are, in order and numbered from 1: every fenced block whose info string is `graphql` or `gql`, and, inside every `json` fenced block, every string under a key named `query`. Any other fenced block in the section is refused as a document the scan cannot read: the scan fails closed. The tokenizer follows GraphQL's lexical grammar: whitespace, commas and a byte-order mark are skipped; `#` starts a comment to the end of the line; `"` strings with backslash escapes and `"""` block strings (with `\"""`) are single tokens; the punctuators are `! $ & ( ) ... : = @ [ ] { | }`; names are `[_A-Za-z][_0-9A-Za-z]*`; numbers are integers and floats; any other character is a syntax error. At the top level (no open brace, parenthesis or bracket) a definition starts with `{` (an anonymous query), or the name `query`, `mutation` or `subscription` (an operation of that type), or `fragment` (a fragment definition, not an operation); the type-system words `schema`, `scalar`, `type`, `interface`, `union`, `enum`, `input`, `directive` and `extend` make the document not executable. After the start, names, variables, defaults, directives and parenthesised variable definitions are skipped to the selection set, whose braces are counted to its close. A document is refused when it holds a mutation or a subscription, more than one operation, no operation, a type-system definition, or a syntax error (an unterminated string, unbalanced brackets, a stray character, a definition with no selection set); it passes otherwise. Each verdict names its reason, so the word "mutation" inside a string or a comment never trips it (K307).

**Reason.** BP:140 and A§9.7:928 put a small tokenizer here and ask for these refusals; GraphQL's own lexical rules are the smallest grammar under which strings and comments cannot hide or fake an operation, and failing closed on what it cannot read keeps the scan honest.

**Follow-up.** Record-map edit: RM:173 (the `audited` row of the version-state table) gains a sentence naming the appendix format (`graphql` or `gql` fences, and `query` strings inside `json` fences). Design touch-up: BP's WP10 block, `solution-audit` writes its appendix in that format.

### `classify` and `native-map`

### W78 `classify` consumes reads; it does not run the query

**Decision.** `classify --reads <file> [--strand <id>]` takes a reads file in W01's shape, reads `account.json` for the client's workspaces and the known unreadable ids, and writes nothing. Lineage is walked over every board the file's pages return; a hop id that is no template id, is returned by no page and is in no page's `missing_ids` (nor in `guard_index.unreadable_intermediate_ids`) is listed in `next_ids`, and the boards waiting on it get class `pending` and are left out of the totals. The session fetches `next_ids` with a `boards_ids` page of the same query, appends it to the file and calls again, until `next_ids` is empty; the synthetic fixtures carry every hop, so one call completes. The sweep is complete (`sweep_complete: true`) when every workspace a `boards_sweep` page names ended on a page with `boards: []` (R0, K313). `ledger.py` holds the NO 2.6 query text and the side reads' texts (W01) as constants and prints the NO 2.6 text as `next_query` beside `next_ids`; none filters on a reserved id (the portfolio items read selects `portfolio_project_link` with `column_values(ids:)`, as G-83 allows), and a test asserts the held NO 2.6 text equals the block in `native-objects.md` (K418, K422). The output: `boards {<id>: {class, rule, attributes, confidence, signals, lineage, review, limits}}`, `totals`, `limits[]`, `projects[]`, `reports[]`, `unreadable_ids[]`, `next_ids[]`, `sweep_complete`.

**Reason.** A§5.3:340 and A§5.4:355 leave every monday call to the session, NO 2.6 gives the query, and BP:142's hop-by-hop walk needs reads no single page holds.

**Follow-up.** Design touch-up: A§11.2:1065, "`ledger.py classify` runs one query per page" becomes "the session runs one query per page and `ledger.py classify` applies both rule sets to the pages".

### W79 R3 needs the workflow objects set

**Decision.** Neither reading's edit: NO 2.6's query stays unchanged (K422), and the workflow objects set is a separate read the session makes beside it, `objects(object_type_unique_keys: ["monday_workflows::workflow"], workspace_ids: $ws, state: ACTIVE)` and the same for `ARCHIVED`, carried as two `workflow_objects` pages (W01). R3 gives `workflow_object` to a `custom_object` board whose id is in that set and `custom_object_other` to one that is not, both at high confidence, once the Portal test of W81 has not fired. With no `workflow_objects` page in the file, a custom object that is not a Portal is `custom_object_other` at low confidence with the finding "workflow objects set not read". Lineage `105719650` is reported as a signal and never decides alone (NO 7.2).

**Reason.** NO 5:134 needs the set and G-74 shows `objects()` returns workflow objects by that key; one more read keeps the one detection query as WP1 pinned it, and NO 7.2 forbids deciding on the lineage alone.

**Follow-up.** Shared edit, for the user's word, not needed before stage 2 acceptance (the code and the reads carry the read already): NO 5:134 and NO 2.6 name the workflow-objects read beside the detection query.

### W80 C1 to C4 are named, not defined

**Decision.** Each number pinned to one condition of NO 7.3, for a portfolio X and a project tasks board P (an R5 board): `C1`, the portfolio half, P's id is in `targets(X)`, the `boardIds` of X's `portfolio_project_link` column (falling back to the relation with `settings.type == "hierarchy"`); `C2`, the row half, at least one item of X links items on P, read from a `portfolio_items` page; `C3`, the project-side reflection, a `board_relation` of P other than the link whose `boardIds` holds X, corroboration only; `C4`, the exclusion, a shared folder, workspace or name, which never counts. Per P, the result: `connected` (C1 and C2, rules `["C1", "C2"]`, plus `C3` when present); `partial link - review` (one of C1 and C2); `unconnected` (neither, for every portfolio; the note names the overview when a relation of P targets an R6 board; `C4` is listed when P shares a folder or workspace with a portfolio, to show it was not counted); `incomplete read - review` when P has neither half and some portfolio's items page carries a non-null cursor, so no project is called unconnected from it (K336). A connected or partial P gets one entry per portfolio it touches; an unconnected one a single entry with `portfolio_id` null. `native_map.portfolio.<X>.projects[]` takes `{tasks_board_id, overview_board_id, overview_state, planner_board_id, folder_id, connected}` with `connected` the result token and `planner_board_id` null (a planner cannot be tied to its project from the API, NO 7.4).

**Reason.** NO 7.3 and A§11.3:1076 describe the two halves, the reflection column and the exclusion, and G-78 names C1, C2 and C4; giving C3 to the reflection column ties each number to a test NO 7.3 states, and the four fixture cases of PLAN §4.2 stay as they are.

**Follow-up.** Shared edit, for the user's word, not needed before acceptance: NO 7.3 names C1 to C4 one by one as above. Record-map edit: RM:119's `projects[].connected` takes the four result tokens.

### W81 The rule order against the type gates

**Decision.** Reading one: N1 and N5 pre-empt R3 and R2 for the boards they match. The order is R0 (the sweep), R1, then R2 with N5 inside it (a `sub_items_board` that meets N5 is `native_<product>_<parent>_subitems` under rule `N5`, its parent found as R2 finds it; otherwise `subitems_board`), then R3 with N1 inside it (a `custom_object` with Portal membership is `native_service_portal` under `N1a`, one with Portal lineage or the Portal template view under `N1b`; otherwise W79's R3), then R4 to R7, then N0 and N2 to N11 for the remaining `board` boards, then R8 to R11 for what N11 hands back.

**Reason.** NO 5:127 slots the N rules in after R4 to R7, yet N1 is for a `custom_object` and N5 for a subitems board, which R3 and R2 would otherwise classify first; only pre-emption lets every class NO 5 names occur.

**Follow-up.** Shared edit, for the user's word, not needed before acceptance: NO 5:127 states the pre-emption in one sentence.

### W82 How many N rules

**Decision.** The rule ids a board's result carries are `R1` to `R11`, `N1a`, `N1b`, `N2` to `N10` and the connection results `C1` to `C4`. `R0` is the sweep and `N0` the soft gate: neither is ever a board's rule; N0's product kind is reported as a signal. `N11` never ends a classification: it hands the board to R8 to R11, whose rule is reported, with `N11` among the signals. `N12` is the attribute set beside the class. BP:141 and A§11:1040's "N0 to N12" covers all of these and needs no change.

**Reason.** NO 5:139, :151 and :152 define N0 as context, N11 as a hand-back and N12 as attributes, and RM:119 already splits N1 into N1a and N1b.

**Follow-up.** Record-map edit: RM:119's `rule` sentence says R0 and N0 never appear on a board.

### W83 The class vocabulary, and how a limit or a review is shown

**Decision.** The class vocabulary is closed: the identification classes of NO 5 (contract section 3.5); `native_crm_<entity>` and `native_service_<entity>` over W16's entity lists; `native_<product>_<parent>_subitems`; `native_service_portal`; `native_crm_companion_board`, `native_service_satellite_probable`, `lookalike_board`, `ordinary_board_in_product_workspace` and `native_descendant_misplaced` (the fingerprint's product and entity in an extra attribute `fingerprint`); and `pending` (W78), never final. A review is `review: true` on R7, R9, N7, N10, a `partial link - review` and an `incomplete read - review`. A known limit is a code in the result's `limits[]`, with its reason in the output's `limits` list: `L1` on every N4 result with install kind `descendant_fingerprint` ("planted reserved ids read the same as a chain-broken native", NO 6.5, G-93); `L2` on every N8 and N9 result ("a native stripped of its template columns with a broken chain reads as this", NO 6.5, G-107); `L3` on every N9 or R11 result in a `service` workspace whose column ids are all monday defaults with no lineage ("a default-shaped satellite that lost its lineage", A§11.4:1088, NO 6.5). A limit is reported, never resolved: the class stays the one the rules give. "Product boards not installed here" is a `reports[]` line (W89).

**Reason.** BP:145 has the two limits reproduced as limits with their reason and A§11.4:1088 adds the third; a limit cannot be detected on a single board, only flagged wherever the rules cannot tell the cases apart.

**Follow-up.** None.

### W84 Threshold ties and family choice

**Decision.** When two entities meet their thresholds on one board, the entity with more of its own reserved ids present wins; then the one whose product matches the workspace's product (N0); then the one listed first in NO 3.3 or 4.3. Both entities appear in `signals` and the confidence drops to `medium`. The CRM family is read from types, never asserted (K369): `deal_close_probability` of type `formula` or `account_deal` of type `board_relation` or `V2_OPPS_FINGERPRINT` gives `v2`; `deal_close_probability` of type `numbers` or `account_deal` of type `mirror` gives `v1`; otherwise the lineage's family, else `unknown`. The Service family is the template family of a resolved lineage or a template view id (`A`, `B`, `C`, `D`); without either, the extended ids (`item_id_1`, `time_tracking3`, `formula9`, `status_163`) give `B or C` and their absence `A or D`.

**Reason.** NO 2.3 and 3 pick the family by reading the type and NO 4.3 says only families B and C carry the extended ids; the tie rule is the smallest that makes the answer key deterministic.

**Follow-up.** None.

### W85 Confidence

**Decision.** `high`: R1 to R6, R8, R10, R11; R3 with the workflow set read; N1a, N1b, N2, N3; N4 when the workspace's product matches the entity's or a corroborating mark is present; N5 with resolved lineage or with its threshold met in a matching product; N9; a `connected` or `unconnected` project. `medium`: N4 otherwise; N5 otherwise; N6 (moderate); N8 (shape, never intent); any result whose entity was a tie (W84). `low`: R7, R9, N7, N10, R3 without the workflow set, and a `partial link - review` or `incomplete read - review`.

**Reason.** NO 5 calls N1a definitive, N1b strong and N6 moderate and marks R7, R9, N7 and N10 for review, A§11.1:1048 lets reserved ids stand alone, and A§7.3:508 shows `high` for an N4 inside a CRM workspace on a dead-end chain.

**Follow-up.** None.

### W86 Lineage edge cases

**Decision.** The walk follows `created_from_board_id` from the board: an id in a template catalogue ends it `RESOLVED_TEMPLATE`, with `hops` the number of boards passed through on the way (0 when the board itself points at the template); a null id ends it `NO_LINEAGE`; an id no page returns (in a page's `missing_ids` or in `unreadable_intermediate_ids`) ends it `UNRESOLVED` and is collected for `unreadable_intermediate_ids`; an id met twice ends it `UNRESOLVED` with the note "cycle"; a chain still open after five hops ends `UNRESOLVED` with the note "longer than 5 hops". `lineage.resolved` is true for `RESOLVED_TEMPLATE` only and `lineage.result` holds the token. `source_view_id` is read one hop only, for N3: a view's `source_view_id` in the template view ids proves a direct install; it is not walked.

**Reason.** NO 2.1 gives the walk, its three results and the cap of five; NO 2.2 makes one template view id proof of a direct install, and BP:142 asks for the lineage walk only.

**Follow-up.** None.

### W87 Where the catalogue constants live

**Decision.** Embedded in `ledger.py`, in one block of tables copied from NO 2.4, 3.1 to 3.3, 4.1 to 4.4, 5:158 and 7.2, never read from `native-objects.md` at run time. `test_ledger_read.py` parses those sections of `native-objects.md` (their backticked ids, numbers and names) and asserts the script's tables equal them, which is the drift test; the lint is not involved, since its pinned check reads `record-map.md` only. `guard_index.template_source_ids` and `template_view_ids` are written by `native-map` from these constants (the catalogue the hook matches against), while `unreadable_intermediate_ids` is the only per-account list.

**Reason.** NO is the one home of the catalogue and the plugin folder is a per-session copy, so either place works; constants keep `classify` independent of a Markdown parser, and the test keeps the two from drifting.

**Follow-up.** None.

### W88 Confirmation of a map entry below high confidence

**Decision.** Reading one: an entry below `high` is never `confirmed_by_user: true`, and `native-map --confirm` on one is refused (K403). Every below-high entry is reported under `needs_review` with "protect as native and ask" on each `native-map` and `classify` call, and is protected through `native_board_index` whatever its confidence (W16). A§11.2:1065's "the user confirms the map ... always for anything below high confidence" is read as the user reviewing it every time it matters, never as a mark.

**Reason.** BP:146 and RM:119 agree, and NO 8 (P-9, P-16) defaults to confidence plus the user's word and to protecting as native and asking, which a standing mark would undercut.

**Follow-up.** Design touch-up: A§11.2:1065 and NO 5:158 (a shared edit, for the user's word, not needed before acceptance), "the user confirms the map before it is used, always for anything below high confidence" becomes "the user confirms the high-confidence entries; anything below high stays unconfirmed, is protected as native and is asked about each time it matters".

### W89 `classify` and `native-map`, and the "not installed here" report

**Decision.** `classify` prints (W78); `native-map --reads <file> --coverage "<one line>" [--staleness-days <n>] [--confirm <product>/<entity> ...] [--strand <id>]` classifies the same reads and writes `account.json` once. It rebuilds `native_map` whole from this read (keeping `confirmed_by_user: true` on an entry whose board and rule are unchanged, and setting it for each `--confirm`ed high entry) and writes `guard_index`: `captured_at` and `ring` (W90); `product_workspaces` from the `workspaces` pages and the boards' `workspace.account_product.kind`, keeping what `workspaces` recorded; `account_products` from the `account_products` page; `native_board_index` and `native_board_ids_by_entity` (W16); `template_source_ids` and `template_view_ids` from the constants (W87); `unreadable_intermediate_ids` (the union of the earlier list and this read's); `reserved_column_ids` for the entities seen, with `blank_default_exclusions` `person`, `status`, `date4`, `date0`; `native_default_names_and_terminology` (NO 5:158's list); `portal_object_ids`; `record_provenance`. It keeps `client_workspace_ids`, `build_targets_by_strand` and the `lease` block exactly as found, re-read in the hold. It refuses to store while `next_ids` is not empty or a swept workspace has no final empty page. "Product boards not installed here" is reported, never "no natives", for each workspace in `client_workspace_ids` whose product is `crm` or `service` and in which no board classifies `native_`; the output names the UI step A§11.5:1095 asks for, which the session records with `ui-step`.

**Reason.** BP:146 has `native-map` record and store, BP:135 keeps both record level, and A§11.5:1095 and D26 give the report and its step.

**Follow-up.** Design touch-up: A§11.2:1065, "Results ... go into `account.json.native_map`" names `native-map` as the writer.

### W90 Provenance fields

**Decision.** `record_provenance.coverage` is the `--coverage` text, one line, stating what was read (as A§7.3:526's example). `captured_at` is the reads file's `captured_at`, else the time of the call; for a synthetic file it is the fixture's `built` date at `00:00:00Z`. `ring` is `"<kind> <value>"` from the pages' `version`, which must agree on every page (a mixed file is refused). `staleness_budget_days` is `--staleness-days`, else the value already stored, else 7 (the template's value).

**Reason.** A§7.3:526 and NO 6.2 name the fields and NO 6.5 asks the coverage to say how partial the read was; the reads carry the ring themselves.

**Follow-up.** None.

### The CLI frame

### W91 The record locator and global flags

**Decision.** `ledger.py` carries its own copy of `record.py`'s small frame (PLAN §8 item 3): `emit`, a `Usage` exception, a `Parser` whose `error()` raises it, and `refuse`; `mmb_common.py` is not changed (K15). Its first statement after `import sys` is `sys.dont_write_bytecode = True`, before `mmb_common` is imported (G49). The launch is `[interpreter, <plugin>/scripts/ledger.py, (--record <client folder>), <command> [action] flags...]`: `--record` is global and comes before the command, the current folder is the default, and a folder without `CLIENT.md` or `account.json` is exit 3 naming the missing file. `run` is a group with a required action (`start`, `heartbeat`, `end`); `live-map` takes an optional action, `set`, and alone renders the map. Every command prints one JSON object, UTF-8 with LF: `{"ok": <exit code is not 1>, "command": "<name as typed>", "asked_by": <the --strand stamp or null>, ...payload}`, with `refusals` on exit 1 and `error` on exit 3, every finding `{file, field, problem, expected}` non-empty, `file` record-relative in POSIX spelling, `(whole file)` for a whole-file error and `record.mutex` for a mutex timeout; exit codes 0, 1, 2, 3 as G10. A usage error, an unknown command and an unexpected exception are exit 3 with the envelope. JSON is written through `mmb_common.json_text` and `write_file` (G11, G39) and read with `utf-8-sig`. An input file the session hands (`--binding`, `--from`, `--read`, `--reads`, `--inventory`, `--inputs`, `--prior-state`, `--before`, `--after`, `--appendix`) must lie inside the record folder, so every finding names a record-relative path; the session writes its read files under `.work/strands/<id>/`, which is scratch and never archived. A file outside the record is refused.

The subcommand catalogue (fence flags: `--lease-epoch`, `--session-label`, `--run-id`; "sha": `--expect-sha`):

| Subcommand | Required flags | Optional flags | Reads | Writes | Fenced | Refuses (beyond the frame and a newer schema) |
|---|---|---|---|---|---|---|
| `check` | none | `--strand` | `account.json`, every `build.json`, `live/live-map.md`, frozen files | nothing | no | none: findings, exit 1, 2 or 0 (W63) |
| `bind` | `--binding` | `--strand` | the file, `CLIENT.md`, `local/settings.json`, `local/sandbox-accounts.txt` | `account.json` (`account`, `api`, `client_slug`) | no | sandbox on a client record and the reverse, an own record off its default account, a rebind, a disagreeing kind and target, a refresh with another user (W37) |
| `workspaces` | `--strand`, fence, one form: `--product --id --name --created-in` / `--use` / `--folder --in-workspace` | `--direction-change` | `account.json`, the two home files | `account.json` (`client_workspaces`, `superseded_workspaces`, `guard_index` lists) | yes | a bad product, an operational id, a second workspace without a direction change, a `--use` outside the client's set (W38, W39) |
| `approval` | `--strand`, `--sha256`, `--words`, `--session`, sha | `--version`, `--revision`, `--irreversible`, `--touches` | `STRAND.md`, `version.md`, the frozen file, `account.json`, `build.json` | `build.json` (the entry, planned rows, `reads_live`, the binding fields; created when absent) | no | W42's list |
| `change-check` | `--strand`, `--from` | none | the file, `account.json` | `account.json` (`change_check`) | no | values outside their sets (W49) |
| `run start` | `--strand`, `--lease-epoch`, `--session-label`, `--another-build-running`, `--account-check`, sha | `--answer-words`, `--run-id` | `STRAND.md`, `version.md`, the frozen file, every strand's runs, `account.json` | the lock and its mirror (refresh, or release on a yes), `build.json` | no (it refreshes) | no version or approval, a stale frozen sha, a mismatched account, `doc-copy`, every refusal of the refresh (W30) |
| `run heartbeat` | `--strand`, fence, sha | `--account-check`, `--before` | `build.json` | the lock's heartbeat (fence), `build.json` | yes | a run that is not this strand's running run |
| `run end` | `--strand`, fence, `--calls-used`, sha | none | `build.json`, `account.json` | `account.json` (`live_objects`), `live/live-map.md`, `build.json`, the lock (release) | yes | a row of this run still `attempting`, another strand's or an ended run except the retry (W32) |
| `intent` | `--strand`, `--key`, `--operation`, fence, sha | W50's list | `build.json`, `account.json`, the frozen file, the two home files | `build.json` (the row; `card` yes entries) | yes | transitions, approval refs, prior state, `do-not-change`, ids, parents, scope, the change-check gate, the class's yes, preconditions, `delete` (K122 to K150, W50) |
| `record` | `--strand`, `--key`, fence, sha | `--id`, `--item-id`, `--url`, `--companion`, `--timed-out`, `--id-from-error`, `--pending`, `--polled-seconds` | `build.json` | `build.json` | yes | a row not `attempting`, a numeric or malformed id |
| `verify` | `--strand`, `--key`, `--result`, `--read`, fence, sha | `--note` | the read file, `build.json`, the frozen file, `account.json` | `build.json` | yes | W51's per-kind list |
| `depart` | `--strand`, `--key`, `--what`, `--error-code`, `--decision`, fence, sha | `--attempt` (two at most), `--ui-what`, `--ui-owner` | `build.json` | `build.json` (departure, and a UI step) | yes | an empty error code, a third attempt, a `removed` row (W55) |
| `ui-step` | `--strand`, sha, and `--what --owner --target-version` or `--key --done` | `--key` | `build.json` | `build.json` | no | a key not `U<n>`, a taken key, an unknown key to mark done |
| `irreversible-yes` | `--strand`, `--key`, `--mode`, `--what`, fence, sha | `--evidence`, `--log-ref` | `build.json` | `build.json` | yes | a key listed nowhere for its mode, an archive without evidence (W48) |
| `reconcile` | `--strand` | `--inventory`, `--classify-only`, `--asked-by` | the inventory, `build.json`, `account.json`, the lease status | the inventory copy; with `--classify-only` the holder's `build.json` | no | a malformed inventory; for classify-only a fresh or absent lease, a lease held by another strand, a lock run missing from the ledger (W72) |
| `estimate` | `--strand` | `--inputs`, `--write`, sha | `build.json` and the other open strands' rows, `account.json` | with `--write`, `build.json` (`preflight`, the run's `calls_estimated`) | no | `--write` without inputs, a negative count |
| `snapshot` | `--strand`, `--label`, `--read` | none | the read file, `build.json`, `account.json`, `STRAND.md` | one new file under `live/snapshots/` | no | a label other than `before` or `after`, a strand with no ledger (W74) |
| `compare` | `--before`, `--after` | `--appendix`, `--strand` | the two snapshots, the appendix | nothing | no | a pair not of one strand and version labelled before and after; findings exit 1 or 2 (W76) |
| `classify` | `--reads` | `--strand` | the reads file, `account.json` | nothing | no | a malformed reads file, a numeric id, mixed rings |
| `native-map` | `--reads`, `--coverage` | `--staleness-days`, `--confirm`, `--strand` | the reads file, `account.json` | `account.json` (`native_map`, `guard_index` but `lease`) | no | pending lineage, an unfinished sweep, a below-high `--confirm`, a target outside the client's set (W88, W89) |
| `live-map` | none | `--strand` | `account.json` | `live/live-map.md` | no | none |
| `live-map set` | `--key`, `--constraint`, `--source`, `--strand` | none | `account.json` | `account.json` (the row), `live/live-map.md` | no | an unknown key, a bad constraint, an empty or interim source, a row of another strand (W62) |

How the session hands a read: always as a file path argument, the file a JSON object in the shape of the command: `classify` and `native-map` take a reads file (W01), `snapshot` a snapshot read (W74), `compare` two snapshot files `snapshot` wrote and an audit file (W77), `reconcile` a `live-inventory/1` file (W70), `verify` a verify read (W51), `bind` a binding document (W37), `change-check` a change-check file (W49), `estimate` an inputs file (W64).

**Reason.** G10 and API:7 to 18 give the frame `record.py` uses, which BP:134 asks `ledger.py` to match, and PLAN §8 item 3 (nodded) keeps it a copy; A§5.4:356 gives the catalogue, and keeping inputs inside the record keeps every finding record-relative on both systems.

**Follow-up.** None beyond A§5.4:356's touch-ups of W28 and W76.

### W92 What the `--strand` stamp is

**Decision.** On a record-level command `--strand` stamps who asked: it is printed as `asked_by` in the output and stored only where a field already exists (`change_check.for_strand`, a snapshot's `strand`), never in a new field and never in a log entry the ledger writes (it writes none, W21; the skill's log entry carries the strand position). Where a record-level command's work belongs to a strand, the same value also names it: `workspaces` extends that strand's targets (and the fence checks that strand's lease), `snapshot` draws that strand's scope, and `live-map set` refuses a row that strand did not build. No record-level command writes a `build.json` (K38).

**Reason.** BP:135 and A§5.4:356 make the flag a stamp on those commands, and the three uses named are the ones the commands cannot do without.

**Follow-up.** Design touch-up: BP:135 adds "for `workspaces`, `snapshot` and `live-map set`, the strand whose targets, scope or rows the call concerns".

---

## 3. What the entries owe

### Record-map edits

For step 3, which applies them now to `plugins/monday-master-builder/shared/record-map.md` (line numbers as of 2026-10-16):

1. **A new section `## Pinned: ledger`**, after `## Pinned: permitted-constants` (PLAN §8 item 10). Its backticked tokens, and no other backticks in its prose: the object types `workspace`, `folder`, `board`, `group`, `column`, `view`, `form`, `subitems`, `doc`, `dashboard`, `widget`, `automation`, `portfolio`, `project`, `workflow`, `agent`, `ai_column`, `vibe_app`, `sequence`, `webhook`, `item_batch`, `publication`, `activation` (W11); the origins `created`, `pre-existing-modified`, `pre-existing-referenced`, `other-strand-modified`; the statuses `planned`, `attempting`, `written`, `verified`, `mismatch`, `departed`, `removed` (W13); the verify results `match`, `mismatch`, `not-checkable`, `needs-user`; the object states `active`, `inactive`, `archived`, `removed-by-platform` (W12); the approval modes `own-account-poc`, `per-list`, and the yes modes `card`, `per-item`, `grouped` (W09); the classes `card`, `list`, `irreversible`, `publication`, `webhook`, `removed` and the operations `create`, `update`, `archive`, `activate`, `publish`, `connect`, `convert`, `delete` (W10); the run kinds `build`, `doc-copy` and states `running`, `ended`, `interrupted`; the constraints `do-not-change`, `change-with-own-yes`, `free`; the change-check results `no change affecting this build`, `change affecting this build` (W08); the departure decisions `ui-step`, `blueprint-revision`, `later-retry` and the UI step statuses `open`, `done` (W55); the reconcile classes `adopt`, `retry`, `duplicate`, `partial`, `changed-since-verified`, `unrecorded-extra`, `missing` and the mode `classify-only` (W71, W72); the confidences `high`, `medium`, `low` (W85). The same step adds `("ledger", "scripts/ledger.py")` to `PINNED` in `tools/lint_plugin.py`; until `ledger.py` exists the lint reports that pair as information ("not present yet"), so it stays at 0 errors.
2. **RM:16 and RM:44** ("passes `ledger.py check`") point at the new check paragraph (item 10, W63).
3. **RM:26**: the snapshot path becomes `live/snapshots/<date>-<strand>-<version>-<label>.json` (W19), and a `snapshot/1` shape paragraph follows the file tables (W74).
4. **RM:68**: drop `build.json.bak` (W20); `live-inventory.json` points at a new `live-inventory/1` shape paragraph (W70).
5. **RM:77**: a `parent_key` may be a qualified live-map key, resolved through `live_objects` (W58).
6. **RM:78**: the element keys gain A§7.3:582's AI and workflow keys (`WF1`, `AG1`, `B1.AI1`, `VB1`, `SQ1`, `WH1`), the publication and activation keys (`WF1.PUB`, `VB1.PUB`, `AG1.ACT`, `SQ1.ACT`) and `B1.IB1`, and the sentence "their keys ... are not listed here yet" goes (W11).
7. **RM:115** (`blueprint/1`): the `## Element keys` table, the `### Prompt <KEY>` block, the resolution of `blueprint_ref` and `prompt_ref` (W42), and the `AS<n>`, `AT<n>`, `FK<n>` ids (W46).
8. **RM:119** (`account/1`): `live_objects` gains `workspace` (W06); `change_check.verdict` becomes `result` with its two values (W08); `bind` writes `api` and refreshes `tier`, `products`, `builder_role` and `name` (W24, W37); `native_map` names the entity list, one entry per entity and the portfolio keyed by board id, and `native_board_index`'s value form gains the subitems example (W16); the `rule` sentence says `R0` and `N0` never appear on a board (W82); `projects[].connected` takes `connected`, `partial link - review`, `unconnected`, `incomplete read - review` (W80); a new `superseded_workspaces[]` (W39); `live_objects.last_verified` is a local date (W14); each field names its writer (W24).
9. **RM:123** (`build/2`): every A§-only field of contract section 3 (`approval_mode`, `rests_on`, `workflows_listed`, `agents_listed`, `sequences_listed`; `preflight.workspaces_ok`; `runs[].another_build_running`; on an object `assumption_refs`, `workspace`, `workspace_scope`, `prompt_ref`, `version_id_at_build`), and the fields these decisions add: on an object `item_ids[]`, `product` (W11), `refs[]` (W15), `live_key` (W50), `read_values {}` (W51), and `companions.tasks_board_id`, `companions.folder_id` (W15); on `irreversible_yes[]` `mode`, `approval_ref` and `evidence` (W09, W48, W56); on `runs[].reconcile` `findings[]` (W72). Also: the optional-on-read rule with its defaults (W06); `approval_ref` required on every row, its `vNrM` form and its resolution (W07, W43); the `state` values (W12); the status table (W13); the type list of 23 (W11); the `notifies[]` forms (W45); the run id's `N` counted per UTC date across the record, and `doc-copy` deferred (W30); `preflight` written by `estimate --write` (W64); `departures[].decision` in the form `ui-step U<n>` (W55); `digest` defined (W73); each field's writer (W24).
10. **Three new paragraphs after RM:123**: "Ledger write orders", the table of W25; "Reconcile classes", the per-kind matches and the class table of W71; "What `ledger.py check` blocks and warns on", W63's list.
11. **RM:129 to 134** (`live-map/1`): the ten-column header and its example row with a `workspace` cell, `inactive` among the states, the kind column in type tokens (W59), and RM:134's sentence on `run end` giving W60's rules.
12. **RM:142** (the lock's "Writes and repairs"): a pointer to the ledger write orders (W25).
13. **RM:173** (the `audited` row): the documents appendix format (W77).

### Shared edits for the user's word

None is needed before stage 2 acceptance: the code embeds its own rules and the synthetic reads carry their own sources.

1. `monday-gotchas.md` line 227, G-69's "Do instead": drop "published workflows are out of v1 (A§14)", say "publish once with the activation state decided beforehand (P-21)" (W03).
2. `safety.md` section 4 line 66: drop published workflows, CRM sequences and webhooks from the excluded list and point at their rows (W03); the same section gains rows for workflow publication, agent activation, sequence activation and webhook creation, from A§9.4:891 to 895 (W10).
3. `safety.md` section 4 line 63 (IR-14): "prefer an existing workspace or folder" becomes "a new workspace per client and per product (A21)" (W10, W39).
4. `safety.md` section 3 line 40: the binding reads `me { kind }` and `account { products { id kind } }` in the same one document (W37).
5. `read-back.md` line 53: rows for agent, Vibe app and workflow with A§10.4:1028's reads, and one row for AI column, sequence and webhook, `not-checkable` until probed (W57).
6. `native-objects.md`: NO 2.6 and the R3 row at line 134 name the workflow-objects read beside the detection query (W79); line 99's family-B `contacts` reads `service_contacts` (W16); line 127 states that N1 and N5 pre-empt R3 and R2 (W81); line 158's role sentence (W17) and its below-high sentence (W88); NO 7.3 (line 196) names C1 to C4 one by one (W80).
7. The AI-kind gotcha entries (G-110 onward) are WP1's at stage 4b (W02, W03).

### Design touch-ups for the user's word

A29's three, owed first (W01, U5):

1. A§11:1040: the recorded reads become the synthetic reads, marked synthetic with the ring they model until a scrubbed capture confirms them at A11-1.
2. BP:101: the WP1 inputs line takes `native-objects.md` from the probe findings, not from recorded reads.
3. BP:130: the WP3 inputs line reads synthetic reads with the ring they model; the capture and the shape comparison join A11-1.

ARCHITECTURE:

4. A§3.4: the blueprint's sections name `## Element keys`, `### Prompt <KEY>` and the `AS`, `AT`, `FK` ids (W42, W46).
5. A§5.4:356: `approval_ref` on every row (W07); the eight fenced subcommands (W28); the presented run id (W29); what record-level subcommands write (W76).
6. A§5.4:362: the sweep accepts the documented ranges under `tests/fixtures/snapshots/` (W05).
7. A§7.1:399: the snapshot path (W19).
8. A§7.1:434: a script may read another strand's ledger and print totals only (W68).
9. A§7.1:438: no `build.json.bak` (W20); the `committed` sentence points at the ledger write orders (W25).
10. A§7.3:495 and :531: the `bound_at` and `last_verified` examples in their time forms (W14).
11. A§7.3:499: `execute_code_ring` as `"release_candidate 2026-10"` (W06).
12. A§7.3:538: `superseded_workspaces` (W39).
13. A§7.3:582: the types `item_batch`, `publication`, `activation` and the key `B1.IB1` (W11); the approval-mode derivation (W44).
14. A§7.8:697: the kind list in type tokens (W59).
15. A§8.2:751: the mirror through `record.py guard` with the values `bind` prints (W22).
16. A§8.6:792, :800, :802: the log entry through `record.py log` (W21); `run end` ends the run and the skill sets `built` (W23, W32).
17. A§8.7:807: the before snapshot written by `ledger.py snapshot` into `live/snapshots/` (W19).
18. A§8.9:823: `ledger.py approval` diffs the element table (W27).
19. A§8.11:835: points at the reconcile class tests (W71).
20. A§9.8:934: the run id presented as `--run-id` (W29).
21. A§9.8:942: the version state set by the skill through the guard (W23).
22. A§9.8:944: "every approval reply" becomes "every execution-time yes" (W28).
23. A§9.9:952: points at the cost table (W65).
24. A§11.2:1065: the session runs the query and `classify` applies the rules (W78); `native-map` writes the map (W89); `role` holds a referenced board's class only (W17); below-high entries stay unconfirmed and are asked about (W88).

BUILD-PLAN:

25. BP:129: the three test files (W04).
26. BP:135: `workspaces`, not `bind`, records the client's workspaces (W38); `live-map set` refuses a row its strand did not build (W62); what record-level subcommands write (W76); what `--strand` names on `workspaces`, `snapshot` and `live-map set` (W92).
27. BP:137: "(A18, stage 4b)" becomes "built in stage 2; stage 4b adds what new probes change" (W02); an `approval_ref` resolves to an entry that names its mode (W09).
28. BP:140: `compare` flags every change A§9.7 lists (W75).
29. BP:146: `template_source_ids` and `unreadable_intermediate_ids` as two fields, with the omitted fields named (W18); `build_targets_by_strand` kept as `workspaces` wrote it (W38).
30. WP7's block: the blueprint template carries the element-key table, the prompt blocks and the assumption ids (W42, W46); the `account.json` template carries `result` (W08).
31. WP9's block: `blueprint-guide.md` says where keys and prompts sit (W42); `build-loop.md` passes `intent`'s and `record`'s flags and cites the poll ceilings (W50, W54).
32. WP10's block: `solution-audit` writes its documents appendix in the pinned format (W77).
33. WP13's block: `guard.py` reads "dated today" as the local date of `change_check.at` (W49).
34. WP16's block: the agnostic sweep's ranges sentence (W05).

For the user: W44 (the approval mode of a working solution in the user's own account; the default built is `per-list`). Answered by the user on 2026-10-16: `per-list`.


## Added by the trace check, 2026-10-16

The trace check of the synthetic reads (`fixture-check.md`, step 4b) found five points; the reads' author settled them (`fixture-notes.md`, "Trace check, settled"). These clarify the wording the points turned on. None changes a decision; each says which reading the reads and the code follow.

- **W01 amended: a `limits` row carries `codes`.** A row of an answer key's `limits` list is `{board_id, code, codes, class, reason, models}`: `codes` holds every limit code of the board's entry, and `code` the most specific of them, in the order `L3`, then `L1`, then `L2`. `limits` stays one row per board, so `board_count` equals the totals plus the length of `limits`. Reason: W83 puts `L2` on every N8 and N9 result and `L3` on a default-shaped satellite that lost its lineage, so one board can carry two codes, and the entry and the row have to agree.
- **W71 clarified: what "a row under it" means for `partial`.** A `verified` row is `partial` when one of its own parts is not `verified`: a row whose `parent_key` is this row's key and whose type is a part of this kind, namely a board's `group`, `column`, `view`, `form`, `subitems`, `ai_column` and `item_batch`, and a dashboard's `widget`. A `workspace` or a `folder` is never `partial` through what it contains, because the boards, docs and folders inside it take classes of their own. Reason: the intent of `partial` is a live object that exists but is not complete (A§8.11:835); read to the letter, every container whose contents are mid-build would be partial, and `record.py lease break` would refuse every park.
- **W71 clarified: a workflow claims its backing board.** A `workflow` row's live match also claims the `custom_object` board whose id is the workflow object's id (W01's id table makes them one id), so that board is never listed as an `unrecorded-extra`. Reason: `boards(workspace_ids, state: all)` returns workflow objects as `custom_object` boards (G-10, G-69), and the inventory is taken from that read unfiltered (W70).
- **K395's Test line corrected in `CONTRACT.md`.** NO 5:158 lists both `Activity` and `"Activity "`, so both match exactly; what fails the exact match is a difference in case or spacing.
