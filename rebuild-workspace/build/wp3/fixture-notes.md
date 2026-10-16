# WP3 fixture notes: the synthetic reads

Date: 2026-10-16. Internal build file: never client-facing.

Step 4 of WP3 (PLAN section 3): the synthetic monday reads under `monday-master-builder/tests/fixtures/snapshots/`, their answer keys and their self-test `tests/unit/test_snapshots.py`. Amendment A29 makes these reads synthetic first: built from `shared/native-objects.md`, `shared/monday-gotchas.md`, the 2026-10 published schema (read with no account, U3) and, for agents, Vibe apps and workflows, `ai-offerings-findings.md` (P-19 to P-21). No monday account was read or written. Every answer key was written by hand from NO 5's rules in W81's order; a review aid in the session scratch folder recomputed only the fact tokens (reserved-id counts, marks, template views) and agreed with the hand-written signals on all 81 boards. It assigns no class.

## Files written

- `tests/fixtures/snapshots/`: `README.md`, `.gitattributes`, `schema-fields.json`, `identification.reads.json`, `identification.expected.json`, `native.reads.json`, `native.expected.json`, `compare/before.read.json`, `compare/after.read.json`, `compare/ledger-state.json`, `compare/appendix.md`, `compare/expected.json`, `reconcile/live-inventory.json`, `reconcile/ledger-state.json`, `reconcile/expected.json`.
- `tests/unit/test_snapshots.py`: 14 tests, standard library only, Python 3.9 syntax, nothing imported from `ledger.py`.

Identification: 22 boards, all in the totals (`converted_project_board` 1, `custom_object_other` 1, `doc_container` 1, `keyed_board_unrecognized_key` 1, `multi_level_board_not_project` 1, `normal_classic_board` 5, `portfolio_board` 1, `portfolio_shaped_board_without_key` 1, `project_board_origin_unknown` 1, `project_overview_companion` 2, `project_tasks_board` 3, `resource_planner_companion` 1, `subitems_board` 1, `workflow_object` 2), no limits. Native: 59 boards, 47 in the totals and 12 listed as limits (`custom_object_other` 1, `doc_container` 1, `keyed_board_unrecognized_key` 1, `native_crm_accounts` 2, `native_crm_activities` 2, `native_crm_companion_board` 2, `native_crm_contacts` 3, `native_crm_leads` 2, `native_crm_opportunities_or_deals` 3, `native_crm_opportunities_or_deals_subitems` 1, `native_crm_quotes_invoices` 1, `native_crm_quotes_invoices_subitems` 1, `native_descendant_misplaced` 1, `native_service_asset_management` 1, `native_service_csat_survey` 2, `native_service_employee_directory` 1, `native_service_employee_lifecycle` 1, `native_service_employee_lifecycle_subitems` 1, `native_service_incidents` 2, `native_service_portal` 3, `native_service_satellite_probable` 1, `native_service_service_contacts` 1, `native_service_tickets` 6, `native_service_tickets_subitems` 2, `normal_classic_board` 2, `portfolio_board` 1, `project_tasks_board` 1, `workflow_object` 1).

## Coverage: PLAN section 4.2

| Case | Where it is |
|---|---|
| R0 paging to an empty page | every `boards_sweep` chain in both reads ends on `boards: []`; the native reads' empty workspaces `90100000207` and `90100000209` end on their first page |
| R1 a doc container | `90300000101` (`R1-doc-container`) |
| R2 a subitems board and its parent | `90300000103` and its parent `90300000102` |
| R3 a workflow object and another custom object | `90300000104`, `90300000106` (archived), `90300000105`; native `90300000232`, `90300000233` |
| R4 a portfolio | `90300000110`; native `90300000263` |
| R5 created, converted, unknown origin, transient key | `90300000111` and `90300000115` (created), `90300000113` (converted), `90300000114` (origin unknown), `90300000112` (`work-management::project`) |
| R6 an overview, live and deleted | `90300000116`, `90300000117` |
| R7 an unrecognised key | `90300000121`; native `90300000261`, which also carries v2 Leads lineage and ids |
| R8 a resource planner | `90300000118`; the near miss with four `rp_*` ids `90300000119` |
| R9 a portfolio-shaped board without a key | `90300000120` |
| R10 a multi-level board that is not a project | `90300000122` |
| R11 a normal board | `90300000123`, `90300000124` (archived), `90300000125` (deleted), `90300000102`, `90300000119` |
| C1 to C4 | projects of the identification key: `90300000111` connected (C1, C2, C3), `90300000112` C1 only, `90300000113` C2 only, `90300000114` neither, `90300000115` neither with C4 listed (shared folder and workspace) |
| every state | active throughout; archived `90300000106`, `90300000124`; deleted `90300000117`, `90300000125`; native archived Portals and deleted `90300000262` |
| CRM v2 and core v1, each entity | v2 `90300000201` to `90300000206`; v1 `90300000210` to `90300000215`, `90300000219` |
| companions (N6) | `90300000208` (relation and mirror marks), `90300000209` (mirror mark, unresolved chain) |
| Quotes & Invoices with its line items | `90300000216`, `90300000217`; generic ids alone `90300000218` |
| Products & Services | `90300000207` |
| Service families A to D, their subitems (N5) | A `90300000223`, `90300000224`; B `90300000220` to `90300000222`, `90300000225`, `90300000226`; C `90300000234` to `90300000241`, `90300000244`; D `90300000242`, `90300000243` |
| a satellite (N7) | `90300000227` |
| the Portal active and archived (N1a, N1b) | `90300000229` (active alias), `90300000230` (archived alias), `90300000231` (archived, by lineage) |
| lineage at 0, 1 and 2 hops, and unresolved | 0 `90300000201`; 1 `90300000211`, `90300000221`; 2 `90300000222`; UNRESOLVED `90300000206`, `90300000209`, `90300000237`, `90300000256` |
| a chain-broken native by reserved ids (N4) | `90300000237` (Tickets), `90300000206` (Sales Targets), `90300000207` |
| a template view id alone (N3) | `90300000234` |
| blank defaults and suffixed ids that count for nothing | `90300000258`, `90300000259`; suffixed ids beside a signature `90300000202` |
| the SLA mark as an attribute | `90300000223` |
| two look-alikes (N8) | `90300000250` (name and terminology), `90300000251` (terminology `"Activity "`) |
| a renamed native with changed terminology | `90300000204` (`Org`) and the 1-hop copy `90300000211` named with an unrelated word |
| an ordinary board linking into a native (N9) | `90300000254` |
| ordinary boards in a product workspace and in a test workspace | `90300000253` (`Client`), `90300000252` (`Call`); test workspace `90300000258`, `90300000259` |
| a native moved into a core workspace (N10) | `90300000260` |
| the boards the identification rules own | `90300000261` (keyed), `90300000233` (another custom object), `90300000228` (Start here doc), `90300000232`, `90300000263`, `90300000264` |
| a deleted native with lineage only | `90300000262` |
| the two known limits, as limits | L1 `90300000257` (planted ids) beside the genuine chain-broken natives; L2 `90300000256` (stripped native reads as a look-alike); L3 `90300000255` (default-shaped satellite) |
| a page on which `boards(ids:)` drops an id | native page 15: four ids requested, `90300000901` to `90300000903` missing |
| Compare: description, archived board, column digest, owner, agent `version_id`, agent state, workflow state | `compare/expected.json` flags `description-change`, `archived-board`, `column-digest-change`, `owner-change`, `agent-version-id-moved` (with its plan digest), `agent-state-moved`, `workflow-state-moved` |
| Compare: controls | `not_flagged`: an unchanged board, a board whose only change is `updated_at`, an automation, a form, a doc, a dashboard, a Vibe app, an unmoved protected row, a board dropped from the scope |
| Compare: a protected row moved before the before snapshot | `changed_outside`: `002:B1` |
| Compare: the appendix | documents 1 to 7: mutation, subscription, two operations (refused); a clean query, the word in a string, the word in a comment, a query string inside a JSON block (pass); a mutation after the section's end is not a document |
| Reconcile: the seven classes, automations first | `reconcile/expected.json` `full.cases`: adopt B6, A1, AG1, WF1; retry B8, B9; duplicate B7, VB2; partial B1, B2, VB1; changed-since-verified B3, A2, AG2; unrecorded-extra boards `90300000419` (predates its attempt) and `90300000421`, agent `90800000403`; missing B4, B5, DB2 |
| Reconcile: the classify-only run over a sibling strand | `classify_only`: asked by 002 for holder 001, run `run-2026-10-16-1` marked interrupted, the same seven counts |

## Coverage: contract clauses K423 to K447

| Clause | Where it is met |
|---|---|
| K423 the seven header keys | every reads file, snapshot read, inventory and ledger-state file; `test_headers` |
| K424 synthetic, `confirmed_by_capture` null | the same headers; `test_headers` |
| K425 `ring_modelled` | `release_candidate 2026-10` in every header; `test_headers` |
| K426 `sources` and `models` | every header's `sources`; `models` on every board, project, limit, flag, control, document and reconcile run; `check_key` |
| K427 the three id lists | every page; `test_pages_id_lists` |
| K428 the NO 2.6 page shape | every board page carries exactly the fields of the NO 2.6 query, aliases included; `test_every_response_path_is_listed` |
| K429 ids invented in ranges | README's id table; `test_ids_are_strings_in_their_ranges` |
| K430 catalogue ids from NO | template, view and fingerprint ids only; the test parses them from `native-objects.md` and checks no range holds one |
| K431 no account id; ids as strings | as K429; a number under an id key fails the test |
| K432 neutral names | README's stem list; `test_names_use_the_stems_and_no_leak_term` checks every name, title and terminology against it and against `leak-terms.txt` |
| K433 the answer keys in files of their own | `identification.expected.json`, `native.expected.json`; `check_key` |
| K434 `schema-fields.json` | 157 paths, the aliases, the JSON scalars and seven connector shapes; `test_every_response_path_is_listed` |
| K435 AI shapes from the findings | agents (P-19), Vibe apps (P-20), workflows (P-21) in the snapshot reads and the inventory, named in `sources` and `connector_shapes` |
| K436 the self-test passes | under `py -3.9` and `py -3.14` on Windows, 2026-10-16 |
| K437 `.gitattributes` | `* text eol=lf`; the test fails on any `\r` |
| K438 the compare fixtures | as the compare rows above; `test_compare_cases`, `test_appendix_documents` |
| K439 the reconcile fixtures | as the reconcile rows above; `test_reconcile_cases` |
| K440 R0 to R11, C1 to C4, every state | `test_identification_key` |
| K441 the native list | `test_native_key` and its case table |
| K442 the trace check | step 4b's (`fixture-check.md`), not written here |
| K443 reads and keys apart | no class, rule, confidence, signal or model key in a reads file; `test_no_answer_in_a_reads_file` |
| K444 no live read or write, no network | the package made none; the test imports no network module |
| K445 "met against synthetic reads" | the checklist's (step 9); the capture waits for A11-1 |
| K446 the id rule and names enforced by the self-test | `test_ids_are_strings_in_their_ranges`, `test_names_use_the_stems_and_no_leak_term`, without `tools/agnostic_sweep.py` |
| K447 the reads are the specification | "What these reads cannot prove" below |

## Derivations: identification

| Case | Board | Rules, in order | Class | Source |
|---|---|---|---|---|
| `R1-doc-container` | `90300000101` | type document: R1 fires first; doc id from the docs page | `doc_container` (R1, high) | NO 5 R1, G-10 |
| `R2-parent-board` | `90300000102` | type board, key null; N0 core; no lineage, no template view, one tickets id (subitems) under 6, no mark; N10 needs a fingerprint; N11 hands back; R8 0 rp ids, R9 0, R10 classic; R11 | `normal_classic_board` (R11, high) | NO 5 R11, NO 5 N11, G-10 |
| `R2-subitems` | `90300000103` | type sub_items_board: R2; N5 inside it does not fire (no line-item or ticket-subitem ids, no lineage); parent 90300000102 names it in its subtasks settings | `subitems_board` (R2, high) | NO 5 R2, G-10, G-44 |
| `R3-workflow-object` | `90300000104` | type custom_object: N1a no (not in either Portal alias), N1b no (lineage 105719650 is not Portal's, no Portal view); R3: in the ACTIVE workflow objects set; the lineage is a signal only (NO 7.2) | `workflow_object` (R3, high) | NO 5 R3, NO 7.2, G-69, G-100 |
| `R3-custom-object-other` | `90300000105` | type custom_object: N1a and N1b no; R3: in neither workflow objects page | `custom_object_other` (R3, high) | NO 5 R3, G-74 |
| `R3-workflow-object-archived` | `90300000106` | type custom_object, archived: N1 no; R3: in the ARCHIVED workflow objects page; state is an attribute | `workflow_object` (R3, high) | NO 5 R3, G-09, G-100 |
| `R4-portfolio` | `90300000110` | type board; key work-management::portfolio: R4 | `portfolio_board` (R4, high) | NO 5 R4, NO 7.1, G-74, G-81 |
| `R5-created-connected` | `90300000111` | key ::portfolio-project: R5; four project_* ids and lineage 9857787491: project_tasks_board | `project_tasks_board` (R5, high) | NO 5 R5, NO 7.2, G-72 |
| `R5-created-transient-key` | `90300000112` | key ::project (the transient key): R5 as for ::portfolio-project; same class as 90300000111 | `project_tasks_board` (R5, high) | NO 5 R5, NO 7.1, G-73 |
| `R5-converted` | `90300000113` | key ::portfolio-project: R5; no project_* id, null lineage, columns visible: converted_project_board | `converted_project_board` (R5, high) | NO 5 R5, G-80 |
| `R5-origin-unknown` | `90300000114` | key ::portfolio-project: R5; columns hidden (none returned) and no template lineage: project_board_origin_unknown | `project_board_origin_unknown` (R5, high) | NO 5 R5, G-81 |
| `R5-created-folder-shared` | `90300000115` | key ::portfolio-project: R5 with four project_* ids; shares folder 90200000001 with the portfolio | `project_tasks_board` (R5, high) | NO 5 R5, NO 7.3, G-78 |
| `R6-overview-live` | `90300000116` | key ::standalone: R6, before R9 could read its five portfolio_project_* ids | `project_overview_companion` (R6, high) | NO 5 R6, G-72 |
| `R6-overview-deleted` | `90300000117` | deleted, columns and views empty; key ::standalone: R6; deleted means its project was connected | `project_overview_companion` (R6, high) | NO 5 R6, G-77 |
| `R8-planner` | `90300000118` | key null; N0 core; lineage resolves to the planner template, a NO 7.2 role id and no native entity, so N2 does not fire; N11 hands back; R8: seven rp_* ids | `resource_planner_companion` (R8, high) | NO 5 R8, NO 7.2, G-72 |
| `R8-near-miss` | `90300000119` | key null; N stage finds nothing; N11; R8 no (four rp_* ids, five needed); R9 no; R10 classic; R11 | `normal_classic_board` (R11, high) | NO 5 R8, NO 5 R11 |
| `R9-portfolio-shaped` | `90300000120` | key null; N stage finds nothing; N11; R8 no; R9: five portfolio_project_* ids, for review | `portfolio_shaped_board_without_key` (R9, low) | NO 5 R9, G-81 |
| `R7-unrecognised-key` | `90300000121` | key lundrask_app::register is none of R4 to R6's: R7 stops for review | `keyed_board_unrecognized_key` (R7, low) | NO 5 R7, G-81 |
| `R10-multi-level` | `90300000122` | key null; N stage finds nothing; N11; R8 and R9 no; R10: hierarchy multi_level, terminology task decides nothing | `multi_level_board_not_project` (R10, high) | NO 5 R10, G-10, G-81 |
| `R11-normal` | `90300000123` | key null; suffixed ids count for nothing; N11; R8 to R10 no; R11 | `normal_classic_board` (R11, high) | NO 5 R11 |
| `R11-archived` | `90300000124` | archived, returned by state: all; as 90300000123; R11 | `normal_classic_board` (R11, high) | NO 5 R0, NO 5 R11, G-09 |
| `R11-deleted` | `90300000125` | deleted: no columns or views, board fields and lineage only; nothing fires; R11 | `normal_classic_board` (R11, high) | NO 5 R0, NO 5 R11, G-77 |

Projects (W80):

- `90300000111`: C1 in the link's boardIds; C2 item 90500000001 links item 90500000101 on it; C3 its relation board_relation_mkq7r2d1 targets the portfolio: connected. Result `connected`, rules C1, C2, C3.
- `90300000112`: C1 in the link's boardIds; no portfolio row links its items: partial link - review. Result `partial link - review`, rules C1.
- `90300000113`: not in the link's boardIds; C2 item 90500000002 links item 90500000301 on it: partial link - review. Result `partial link - review`, rules C2.
- `90300000114`: neither half; workspace 1, no folder or workspace shared with a portfolio: unconnected. Result `unconnected`, rules none.
- `90300000115`: neither half; shares folder and workspace with the portfolio (C4, not counted); its relation targets R6 board 90300000116: unconnected, naming the overview. Result `unconnected`, rules C4.

## Derivations: native

| Case | Board | Rules, in order | Class | Source |
|---|---|---|---|---|
| `crm-v2-leads` | `90300000201` | N0 crm; N2: lineage resolves at 0 hops to v2 leads; N3 and N4 agree | `native_crm_leads` (N2, high) | NO 5 N2, NO 2.1, NO 3.1, G-94 |
| `crm-v2-opportunities` | `90300000202` | N0 crm; N2 at 0 hops; deal_close_probability is a formula and deal_account carries the v2 fingerprint: v2; the suffixed formula_mm3gb9sn and the feature column neither count nor disqualify | `native_crm_opportunities_or_deals` (N2, high) | NO 5 N2, NO 2.3, NO 2.4, G-96, G-99 |
| `crm-v2-contacts` | `90300000203` | N0 crm; N2 at 0 hops | `native_crm_contacts` (N2, high) | NO 5 N2, NO 3.1, G-101 |
| `crm-v2-accounts-renamed` | `90300000204` | renamed, terminology Org; N0 crm; N2 at 0 hops; account_deal is a relation: v2; the name decides nothing | `native_crm_accounts` (N2, high) | NO 5 N2, NO 6.1, G-97 |
| `crm-v2-activities` | `90300000205` | N0 crm; N2 at 0 hops | `native_crm_activities` (N2, high) | NO 5 N2, NO 3.1 |
| `crm-v2-sales-targets-chain-broken` | `90300000206` | N0 crm; N2 no: the chain ends UNRESOLVED at 90300000901, which the ids page dropped; N3 no; N4: six sales_targets ids, threshold 3: descendant_fingerprint, high (crm workspace); L1 | `native_crm_sales_targets` (N4, high; limit L1) | NO 5 N4, NO 2.1, G-92, G-94, G-96 |
| `crm-products-services` | `90300000207` | N0 crm; no lineage, no template view (NO 3.2 lists none); N4: four product_and_service ids, threshold 2; terminology item decides nothing; descendant_fingerprint; L1 | `native_crm_products_services` (N4, high; limit L1) | NO 5 N4, NO 3, NO 3.3, G-97 |
| `crm-companion-marks` | `90300000208` | N0 crm; N2 to N4 no (no lineage, no view, no reserved id); N6: a relation with staticImage accounts and a mirror showing company_domain | `native_crm_companion_board` (N6, medium) | NO 5 N6, NO 2.4, NO 3 |
| `crm-companion-unresolved` | `90300000209` | N0 crm; N2 no (UNRESOLVED at 90300000902); N3, N4 no; N6: a mirror showing deal_value | `native_crm_companion_board` (N6, medium) | NO 5 N6, NO 2.4, G-94 |
| `crm-v1-deals` | `90300000210` | N0 crm; N2 at 0 hops; deal_close_probability is numbers: v1 | `native_crm_opportunities_or_deals` (N2, high) | NO 5 N2, NO 2.3, G-96 |
| `crm-v1-deals-copy-1hop` | `90300000211` | named with an unrelated word; N0 crm; N2: 90300000210 then template 2658101899, 1 hop: descendant_copy(1); its view points at the install's view, not a template view | `native_crm_opportunities_or_deals` (N2, high) | NO 5 N2, NO 2.1, NO 2.2, G-94, G-97 |
| `crm-v1-contacts` | `90300000212` | N0 crm; N2 at 0 hops | `native_crm_contacts` (N2, high) | NO 5 N2, NO 3.1 |
| `crm-v1-leads` | `90300000213` | N0 crm; N2 at 0 hops | `native_crm_leads` (N2, high) | NO 5 N2, NO 3.1, NO 3.2 |
| `crm-v1-accounts` | `90300000214` | N0 crm; N2 at 0 hops; account_deal is a mirror: v1 | `native_crm_accounts` (N2, high) | NO 5 N2, NO 2.3 |
| `crm-v1-activities` | `90300000215` | N0 crm; N2 at 0 hops; activity_item carries no staticImage, so no relation mark | `native_crm_activities` (N2, high) | NO 5 N2, NO 3, G-101 |
| `crm-quotes-invoices` | `90300000216` | N0 crm; N2 at 0 hops; its six generic ids count because lineage, two template views and terminology Document # corroborate | `native_crm_quotes_invoices` (N2, high) | NO 5 N2, NO 3, NO 3.3, G-95 |
| `crm-qi-line-items` | `90300000217` | type sub_items_board: R2 with N5 inside; seven line_item ids (threshold 6) and lineage 18393462843; parent 90300000216 is Quotes & Invoices | `native_crm_quotes_invoices_subitems` (N5, high) | NO 5 N5, NO 3.3, G-101 |
| `crm-qi-generic-ids-only` | `90300000218` | N0 crm; the six generic Quotes & Invoices ids without lineage, view or terminology do not classify (NO 3.3); no mark; N8 no (reserved ids present, no imitation); N9; L2 | `ordinary_board_in_product_workspace` (N9, high; limit L2) | NO 5 N9, NO 3.3:85 |
| `crm-v1-deals-subitems` | `90300000219` | type sub_items_board: R2 with N5 inside; blank defaults and a suffixed id only, so lineage 2658102037 decides; parent 90300000210 is Deals | `native_crm_opportunities_or_deals_subitems` (N5, high) | NO 5 N5, NO 3.3, G-107 |
| `service-b-tickets` | `90300000220` | returned by ids page 2; N0 service; N2 at 0 hops, family B | `native_service_tickets` (N2, high) | NO 5 N2, NO 2.1, G-92 |
| `service-b-tickets-copy-1hop` | `90300000221` | returned by ids page 1, beside the three dropped ids; N2: 90300000220 then the template, descendant_copy(1) | `native_service_tickets` (N2, high) | NO 5 N2, NO 2.1, G-92, G-94 |
| `service-b-tickets-copy-2hop` | `90300000222` | N0 service; N2: 90300000221 (ids page 1), 90300000220 (ids page 2), template 5727048235: 2 hops, descendant_copy(2) | `native_service_tickets` (N2, high) | NO 5 N2, NO 2.1, G-94 |
| `service-a-tickets-sla` | `90300000223` | N0 service; N2 at 0 hops, family A; four SLA helpers share the stem formula_mm3jtrd: the mark is an attribute | `native_service_tickets` (N2, high) | NO 5 N2, NO 5 N12, NO 2.4, G-102 |
| `service-a-tickets-subitems` | `90300000224` | type sub_items_board: R2 with N5 inside; five ticket-subitem ids (threshold 4) and lineage | `native_service_tickets_subitems` (N5, high) | NO 5 N5, NO 4.3 |
| `service-b-csat` | `90300000225` | N0 service; default-shaped ids only; N2 at 0 hops decides | `native_service_csat_survey` (N2, high) | NO 5 N2, NO 4.3, G-107 |
| `service-b-contacts` | `90300000226` | N0 service; default-shaped; N2 at 0 hops decides | `native_service_service_contacts` (N2, high) | NO 5 N2, NO 4.3 |
| `service-satellite` | `90300000227` | N0 service; no lineage, no template view, no signature; N6 is CRM only; N7: terminology Contact name and the target of native Tickets 90300000223's connect_boards2; review | `native_service_satellite_probable` (N7, low) | NO 5 N7, NO 6.5, G-107 |
| `service-b-start-here-doc` | `90300000228` | type document: R1 first; its lineage to the family-B Start here doc is an attribute | `doc_container` (R1, high) | NO 5 R1, NO 4.1:104 |
| `portal-active` | `90300000229` | type custom_object: N1a in R3's place: in portal_active | `native_service_portal` (N1a, high) | NO 5 N1a, NO 4.4, G-100 |
| `portal-archived-alias` | `90300000230` | type custom_object, archived: N1a through the portal_archived alias | `native_service_portal` (N1a, high) | NO 5 N1a, NO 4.4, G-100 |
| `portal-archived-lineage` | `90300000231` | type custom_object, archived, in neither Portal alias: N1a no; N1b on Portal lineage and view | `native_service_portal` (N1b, high) | NO 5 N1b, NO 4.4, G-100 |
| `workflow-object-not-portal` | `90300000232` | type custom_object: N1a no, N1b no (lineage 105719650 and no Portal view); R3 in the workflow set | `workflow_object` (R3, high) | NO 5 R3, NO 4.4, G-100 |
| `custom-object-other` | `90300000233` | type custom_object: N1 no; R3: in neither workflow page | `custom_object_other` (R3, high) | NO 5 R3, G-74 |
| `service-c-csat-view-only` | `90300000234` | renamed, lineage cleared; N2 no; N3: the form view's source_view_id is C's CSAT template view | `native_service_csat_survey` (N3, high) | NO 5 N3, NO 2.2, G-95 |
| `service-c-tickets` | `90300000235` | N0 service; N2 at 0 hops | `native_service_tickets` (N2, high) | NO 5 N2, NO 4.1 |
| `service-c-incidents` | `90300000236` | N0 service; every id a monday default; N2 at 0 hops decides | `native_service_incidents` (N2, high) | NO 5 N2, NO 4.3, G-107 |
| `service-c-tickets-chain-broken` | `90300000237` | N0 service; N2 no (UNRESOLVED at 90300000903); no template view; N4: twelve tickets ids, threshold 6; extended ids present: family B or C; descendant_fingerprint, high; L1 | `native_service_tickets` (N4, high; limit L1) | NO 5 N4, NO 2.3, G-96 |
| `service-c-asset-management` | `90300000238` | N0 service; N2 at 0 hops; five asset ids agree | `native_service_asset_management` (N2, high) | NO 5 N2, NO 4.3 |
| `service-c-employee-lifecycle` | `90300000239` | N0 service; N2 at 0 hops; the weak signature agrees | `native_service_employee_lifecycle` (N2, high) | NO 5 N2, NO 4.3 |
| `service-c-employee-directory` | `90300000240` | N0 service; N2 at 0 hops; the weak signature agrees | `native_service_employee_directory` (N2, high) | NO 5 N2, NO 4.3 |
| `service-c-tickets-subitems` | `90300000241` | type sub_items_board: R2 with N5 inside; four ticket-subitem ids and lineage | `native_service_tickets_subitems` (N5, high) | NO 5 N5, NO 4.3 |
| `service-d-tickets` | `90300000242` | N0 service; N2 at 0 hops, family D | `native_service_tickets` (N2, high) | NO 5 N2, NO 4.1 |
| `service-d-incidents` | `90300000243` | N0 service; N2 at 0 hops, family D | `native_service_incidents` (N2, high) | NO 5 N2, NO 4.3 |
| `service-c-lifecycle-subitems` | `90300000244` | type sub_items_board: R2 with N5 inside; blank defaults only, lineage 5561656359 decides; parent 90300000239 | `native_service_employee_lifecycle_subitems` (N5, high) | NO 5 N5, NO 4.1 |
| `lookalike-name` | `90300000250` | N0 crm; no lineage, no view, no reserved id (all suffixed), no mark; N6 no; N8: name Leads and terminology Lead imitate a native; L2 | `lookalike_board` (N8, medium; limit L2) | NO 5 N8, G-97 |
| `lookalike-terminology` | `90300000251` | N0 crm; no lineage, view, reserved id or mark; N8: terminology "Activity " with its trailing space matches exactly; L2 | `lookalike_board` (N8, medium; limit L2) | NO 5 N8, NO 5:158, G-97 |
| `ordinary-terminology-call` | `90300000252` | N0 crm; no signal; terminology Call is outside the NO 5:158 list, so no imitation; N8 no; N9; L2 | `ordinary_board_in_product_workspace` (N9, high; limit L2) | NO 5 N9, NO 5:158, G-97 |
| `ordinary-terminology-client` | `90300000253` | N0 crm; no signal; terminology Client is outside the imitation set; N8 no; N9; L2 | `ordinary_board_in_product_workspace` (N9, high; limit L2) | NO 5 N9, NO 5:158, G-97 |
| `ordinary-links-into-native` | `90300000254` | N0 service; its relation into Tickets 90300000223 is outbound and ignored; nothing else; N9; L2 | `ordinary_board_in_product_workspace` (N9, high; limit L2) | NO 5 N9, G-104 |
| `default-shaped-satellite` | `90300000255` | N0 service; an Incidents shape with every id a monday default, no lineage, no view; terminology item, so N7 and N8 do not fire; N9; L2 and L3 | `ordinary_board_in_product_workspace` (N9, high; limit L2, L3) | NO 5 N9, NO 6.5, G-107 |
| `stripped-native` | `90300000256` | N0 crm; chain UNRESOLVED at 90300000901, template columns gone; no reserved id, no mark; N8 on the name and terminology; the stripped native reads as a look-alike: L2 | `lookalike_board` (N8, medium; limit L2) | NO 5 N8, NO 6.5, G-107 |
| `planted-ids` | `90300000257` | N0 crm; no lineage, no view; N4: three planted lead ids meet the threshold; reads the same as a chain-broken native: descendant_fingerprint, high; L1 | `native_crm_leads` (N4, high; limit L1) | NO 5 N4, NO 6.1, G-93 |
| `ordinary-test-blank-defaults` | `90300000258` | N0 core; blank defaults and suffixed ids match nothing; N11 hands back; R8 to R10 no; R11 | `normal_classic_board` (R11, high) | NO 5 N11, NO 5 R11, NO 2.3, G-98 |
| `ordinary-test-suffixed-ids` | `90300000259` | N0 core; deal_stage_mkd1f2g3 and the like are suffixed ids, never reserved; N11; R11 | `normal_classic_board` (R11, high) | NO 5 N11, NO 5 R11, NO 2.3, G-96 |
| `native-moved-to-core` | `90300000260` | N0 core; the v2 accounts fingerprint (N2 at 0 hops) in a workspace that is neither crm nor service: N10, for review | `native_descendant_misplaced` (N10, low) | NO 5 N10, NO 2.5, G-106 |
| `keyed-board-with-native-signals` | `90300000261` | key lundrask_app::register: R7 stops for review before any N rule, though its lineage and ids are v2 leads | `keyed_board_unrecognized_key` (R7, low) | NO 5 R7, NO 8 P-9, G-91 |
| `deleted-native-lineage-only` | `90300000262` | deleted: no columns or views; N2 on lineage alone at 0 hops; state is an attribute | `native_crm_contacts` (N2, high) | NO 5 N2, NO 2.1, G-77 |
| `portfolio-cursor` | `90300000263` | key work-management::portfolio: R4; its items page ends on a non-null cursor | `portfolio_board` (R4, high) | NO 5 R4, NO 7.3 |
| `project-incomplete-read` | `90300000264` | key ::portfolio-project: R5 with four project_* ids | `project_tasks_board` (R5, high) | NO 5 R5, NO 7.3 |

Project (W80):

- `90300000264`: not in the link's boardIds (none), no row seen linking it, and portfolio 90300000263's items page ends on cursor c-000001: incomplete read - review. Result `incomplete read - review`, rules none.

## Choices taken

Where the decisions are silent, the smallest choice was taken and is recorded here.

1. **Signal tokens.** The decisions name no vocabulary for `signals`. README's table fixes one: facts, not rule verdicts, each present whenever its condition holds, so `N0:<kind>` appears on every board and `lineage:`, `view:` and `reserved:` wherever their axis holds, even on a board an earlier rule decided (the keyed board `90300000261` lists its v2 Leads lineage and ids). Only the imitation and relation-target tokens are confined to N7 and N8 results, and `N11` to boards handed back.
2. **A lineage that resolves to a NO 7.2 role template** (portfolio, tasks, overview, planner, workflow object) is `RESOLVED_TEMPLATE` with its `lineage:` token, but names no native entity, so N2 does not fire on it (the planner `90300000118` reaches R8).
3. **N10 is the product gate on N2 to N4.** N2 to N4 come before N10 in W81's order, yet N10 must fire on a native fingerprint outside a crm or service workspace (NO 2.5, K340). The reading taken: a fingerprint found by N2, N3 or N4 in a workspace whose product is neither crm nor service gives N10, with the fingerprint's product and entity in the `fingerprint` attribute.
4. **N9 is what is left in a product workspace after N8**, read with "no signals" meaning no signal token beyond `N0`. A board whose six generic Quotes & Invoices ids lack corroboration (`90300000218`) carries reserved ids, so it is not a look-alike (N8 needs zero) and ends at N9.
5. **Family and version.** CRM: `family` `sales_crm` or `crm_core` and `version` `v2` or `v1`, after NO 3's two catalogue names, with W84's type rules first; an unknown generation is `family` null, `version` `unknown`. Service: `family` from the template family; W84's extended-id fallback (`B or C`, `A or D`) is applied to Tickets boards only, because the pooled set is Tickets'; `version` null. `sla_mark` is a boolean on every native class and on a Start here doc whose lineage resolves (false there), and null elsewhere.
6. **`install_kind` beyond N2 to N4.** N1a, N1b and N5 take the install kind of their lineage; an N6 or N7 board whose chain ends unresolved takes `lineage_unresolved`, one with no lineage null. A Start here doc (R1) carries its family-B lineage as `family` and `install_kind` (NO 4.1:104).
7. **The `native_board_index` value of an N7 board** is `service/satellite_probable`; W16 names no entity for it.
8. **One `limits` row per board, with every code.** Every N9 result in a service workspace that is L3 is also L2, so a board can hold two codes. To keep `board_count` equal to the totals plus the length of `limits` (W01), the top-level list carries one row per board: `code` is the most specific code (L3 before L1 before L2) and an added `codes` lists every code the board's own `limits[]` holds, so the two always agree.
9. **Every N4 `descendant_fingerprint` result and every N8 and N9 result is a limit** (W83), so the Products & Services board, Sales Targets and the chain-broken Tickets board sit in `limits`, not in the totals, beside the planted and stripped boards. Their classes are still the native classes the rules give.
10. **The cursor case lives in the native reads.** W80 calls every project with neither half an incomplete read when *any* portfolio's items page carries a cursor, so a cursor in the identification reads would turn both of its unconnected projects into incomplete reads. The native reads carry the cursor portfolio `90300000263` and its project `90300000264` instead.
11. **A project entry carries `note`** (W01's shape plus one field), naming the overview of an unconnected project as NO 7.3 and W80 ask.
12. **`requested_ids` on the side reads.** The workspaces and portfolio-items reads request ids and are diffed; the account-products, docs and workflow-objects reads request none, so `requested_ids` is empty and `returned_ids` lists what came back.
13. **`objects()` state casing.** `Object.state` is a String in the schema; the reads write `active` and `archived`, as `Board.state` does. Agent states (`ACTIVE`, `INACTIVE`) and Vibe statuses (`READY`, `GENERATING`) keep P-19's and P-20's capitals.
14. **Board ids inside `settings` JSON are strings** (`boardIds`), to keep every id a string; monday may return numbers there.
15. **Dashboards have no query root** in the 2026-10 schema: `Dashboard` is reached only as a mutation's return type, so `schema-fields.json` maps the dashboard paths to `Mutation.create_dashboard` and `Dashboard.*`. How the session reads a dashboard by stored id is its own (G-11, G-90).
16. **The inventories carry the workflow objects' boards**, as `boards(workspace_ids, state: all)` returns them (G-10, G-69): `90300000308` in both snapshot inventories and `90300000420` in the live inventory, each as a `custom_object`. A workflow object's board is the same object as the workflow (its `objects()` id is its board id, W01), so in `reconcile` the board is claimed by WF1's adopt match and is no unrecorded extra; in `compare` its board state moves with the workflow's and is flagged a second time, under the same case. A doc container stays in the board list and is claimed through `docs[].object_id` (W71).
17. **A live object that W71 counts as a row's match** (the `live_ids` of an adopt or a duplicate) is not listed again as an unrecorded extra; a match that predates the row's attempt is, with `predates_attempt: true` (K272).
18. **The compare scope.** `scope.boards` holds the strand's board rows and the protected live rows' boards; a strand's automations, form, doc, dashboard, agents, workflow and Vibe app are in scope by their row ids. The inventory part is compared across every board it holds; its out-of-scope boards are unchanged, so either reading of W75 gives the same flags. A board in the per-board part that is in no scope (`90300000309`) is dropped, not flagged.
19. **Compare's expected output.** `compare/expected.json` gives each flag's field, its two values, the problem text (strings raw, lists as compact JSON) and the expected text; the after snapshot's path, the fourth part, is the record path `snapshot` writes, which the reads cannot know. The version-id move also moves the plan digest, since `version_id` changes with the plan (P-19), so it is flagged twice.
20. **Snapshot digests.** `columns` is taken over the column list sorted by `id`; `plan` over the plan text. Triggers are a list of names and knowledge a list of grants; neither moves in this fixture.
21. **Digest inputs.** Each ledger-state file carries a `digest_fields` list naming every digest's place, prefix and fields, so the self-test recomputes each one; `verify.read` points at it.
22. **Names.** Invented stems were checked against the leak list and replaced where a stem is a known product or place name. monday's native default names and terminologies (`Leads`, `Opportunities`, `Contact name`, `"Activity "`, `Org`, `Client`) are used where a case needs them, as G-97 and NO 5:158 describe.
23. **The workflow objects set is read** in both fixtures (W79), so every R3 result is at high confidence; the unread case (`workflow_objects:unread`, low) is left to a unit test that drops those pages.

## What these reads cannot prove

As A29 says, the classification, compare and reconcile acceptance is met against these synthetic reads, and the capture and the shape comparison join the A11-1 moment. Until then:

- that monday returns these shapes today, field for field, for this ring or any later one;
- that nothing moved since the ring the findings modelled (`release_candidate 2026-10`, probes of 2026-09-11 to 2026-09-13);
- anything the findings never observed, among them: the casing of `Object.state` in an `objects()` reply; whether board ids inside `settings` JSON come back as strings or numbers; the type strings of `views { type }`; the settings shape of a mirror (`displayed_linked_columns`); the types of the SLA helper columns; what a doc container's column list holds; whether a workflow object's board state moves with the workflow's state; that an archived Portal can be missing from the archived alias (the N1b case models NO 4.4's fallback, not an observed omission); the shape of a trigger list and a knowledge grant in `manage_agent`; `get_form`'s reply; a Vibe app's code-version form and an agent's `version_id` form; the path by which a dashboard is read by stored id;
- that the client workspaces each key assumes for `reports` are the ones a real record would hold: they come from `account.json`, which no read carries.

## Trace check, settled

Step 4b (`fixture-check.md`) agreed with every board, project, flag, document and reconcile element but five points. Each is settled here; the files were regenerated, every digest recomputed, and the self-test passes under `py -3.9` and `py -3.14`.

1. **Native `90300000252` (the key was wrong).** NO 5:158's terminology list holds both `Activity` and `"Activity "`, so the board's terminology `Activity` imitates a native and N8 would fire; the key's N9 did not follow the rule. The case was meant as an ordinary board in a product workspace, so the read changed: its terminology is now `Call`, outside the list, and the case id is `ordinary-terminology-call`. Class `ordinary_board_in_product_workspace`, rule N9, high, L2, as before; the totals and the `limits` row are unchanged (59 boards, 47 in the totals, 12 limits). The exact-match case stays with the look-alike `90300000251` (`"Activity "`). For the main session: contract clause K395's test ("terminology `"Activity "` matches and `"Activity"` does not") contradicts NO 5:158, which lists both forms; the clause's test needs rewording (for instance: `"Activity "` matches exactly, and a terminology outside the list, or one differing only by case or trailing space from a listed form that is not itself listed, does not).
2. **Reconcile `W1` (the key stands, the wording is ambiguous).** W71's `partial` test reads "a `verified` row whose live digest is unchanged while a row under it (by `parent_key`) is not `verified`". Read to the letter, every container whose children are mid-build is partial: a workspace or a folder would be partial whenever any board in it is attempting, retried or planned, though those children get classes of their own, and `record.py lease break` would refuse to park on every interrupted run. The intent of `partial`, "a live object that exists but is not complete" (A§8.11:835, K270's "a board with the recorded columns missing"), is the object's own parts. The key keeps that reading: the rows that count are the parts of the object, which carry no live identity of their own in the inventory (groups, columns, views, forms, subitems, AI columns, item batches and widgets), so B1 is partial through B1.C1 and W1 is `unchanged`. A board, folder, doc, automation or dashboard under a workspace or a board is an object with its own row and class and does not make its parent partial. For the main session: W71's `partial` row should say which rows "under it" count, for instance "a row under it by `parent_key` whose type is a part of its parent (group, column, view, form, subitems, ai_column, item_batch, widget)".
3. **Native `90300000255` limits (made to agree).** W01 fixes `board_count` as the totals plus the length of `limits`, so `limits` stays one row per board; W83 puts L2 on every N9 and L3 on this one too. Each `limits` row now carries `codes`, every code of the board's entry, beside `code`, its most specific (L3, then L1, then L2), so the entry (`["L2", "L3"]`) and the row (`code` L3, `codes` `["L2", "L3"]`) agree. For the main session: W01's `limits` row shape (`{board_id, code, class, reason, models}`) should gain `codes`, or W83 should say L3 subsumes L2.
4. **Native `90300000228` (made to agree).** README says `family`, `version`, `install_kind` and `sla_mark` are given on a `doc_container` whose lineage resolves to a native template (NO 4.1:104); the key gave `sla_mark` null. The key now gives `false` there, as on every native class, so README and key agree. No rule text decides it; the smallest choice is that a given attribute set is given whole.
5. **Workflow-object boards in the inventories (added).** `boards(workspace_ids, state: all)` returns workflow objects as `custom_object` boards (G-10, G-69), and W70 and W74 take the inventory from that read unfiltered, so a capture would list them. The compare inventories now carry `90300000308` (`custom_object`, archived in the after read with its workflow) and the live inventory carries `90300000420` (`custom_object`, created 09:34). In `compare` the board's state move is flagged as `board:90300000308.state` beside `workflow:90300000308.state`, both under `workflow-state-moved` (W75 flags any inventory board whose state moved). In `reconcile` the board is the same object as the workflow WF1 adopts (a workflow object's `objects()` id is its board id, W01), so it is claimed by that match and raises no unrecorded extra; the classes are unchanged. Whether a workflow object's board state moves with the workflow's is not observed and stays in "What these reads cannot prove". For the main session: W71's claim list should name "a board whose id is a workflow row's id or that workflow's live match" so a workflow's backing board is never an unrecorded extra.

DECISIONS and contract wording for the main session to clarify: K395's test (point 1); W71's `partial` row (point 2); W01's `limits` row shape or W83 on L3 and L2 (point 3); W71's claim list for workflow-object boards (point 5).
