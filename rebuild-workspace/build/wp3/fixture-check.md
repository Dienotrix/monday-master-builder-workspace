# Fixture trace check (WP3 step 4b)

Date 2026-10-16. Internal build file: never client-facing.

## Method

Each board of the two classification fixtures was classified by hand from its read alone (type, key, hierarchy, columns, links, views, lineage pages, the workspace product, the docs, workflow-object and portfolio pages), applying R1 to R7, the Portal and subitems pre-emptions, N0 to N11 and then R8 to R11 in the order W81 sets, with the thresholds, family choice, confidence and lineage edge cases of W84 to W86 and the limit codes of W83. The answer key was opened only after each derivation was complete. Helper scripts only listed fields, recomputed the mechanical fields (state, items_count, N0, key, type, hierarchy and view signals, totals against board_count, the W73 digests) and compared them; every class, rule, confidence, install kind and limit was decided by hand. The compare and reconcile fixtures were derived from the before and after reads, the ledger state, the live inventory and the appendix, using W70 to W77. `fixture-notes.md` was read only after my own answers were fixed, and only to see how the author derived the cases where I disagreed. `ledger.py`, its tests, the self-test and the generator scripts were not read.

In the tables, "key" and "mine" give class / rule / confidence, then family and version, install kind, the SLA mark, review, limit codes and the lineage result. Where the cell for mine is "same" my derivation reached the key's full answer, signals included.

## Identification fixture (22 boards, 5 project entries)

| Board | Case | Key | Mine | Verdict | Reason |
|---|---|---|---|---|---|
| 90300000101 | R1-doc-container | doc_container / R1 / high; lineage NO_LINEAGE | same | agree | |
| 90300000102 | R2-parent-board | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000103 | R2-subitems | subitems_board / R2 / high; lineage NO_LINEAGE | same | agree | |
| 90300000104 | R3-workflow-object | workflow_object / R3 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000105 | R3-custom-object-other | custom_object_other / R3 / high; lineage NO_LINEAGE | same | agree | |
| 90300000106 | R3-workflow-object-archived | workflow_object / R3 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000110 | R4-portfolio | portfolio_board / R4 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000111 | R5-created-connected | project_tasks_board / R5 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000112 | R5-created-transient-key | project_tasks_board / R5 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000113 | R5-converted | converted_project_board / R5 / high; lineage NO_LINEAGE | same | agree | |
| 90300000114 | R5-origin-unknown | project_board_origin_unknown / R5 / high; lineage NO_LINEAGE | same | agree | |
| 90300000115 | R5-created-folder-shared | project_tasks_board / R5 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000116 | R6-overview-live | project_overview_companion / R6 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000117 | R6-overview-deleted | project_overview_companion / R6 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000118 | R8-planner | resource_planner_companion / R8 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000119 | R8-near-miss | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000120 | R9-portfolio-shaped | portfolio_shaped_board_without_key / R9 / low; review; lineage NO_LINEAGE | same | agree | |
| 90300000121 | R7-unrecognised-key | keyed_board_unrecognized_key / R7 / low; review; lineage NO_LINEAGE | same | agree | |
| 90300000122 | R10-multi-level | multi_level_board_not_project / R10 / high; lineage NO_LINEAGE | same | agree | |
| 90300000123 | R11-normal | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000124 | R11-archived | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000125 | R11-deleted | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |

Totals recomputed: 22 boards, no limits, `board_count` 22 equals the sum of totals (22) plus limits (0); each total agrees (`normal_classic_board` 5, `project_tasks_board` 3, `project_overview_companion` 2, `workflow_object` 2, the other ten classes 1 each). `reports` is empty (both workspaces are core), `sweep_complete` true (both workspaces end on an empty page), `unreadable_ids` empty, which agree.

| Project entry | Key | Mine | Verdict |
|---|---|---|---|
| 90300000110 / 90300000111 | connected; rules ['C1', 'C2', 'C3']; note None | same (111 has C1, C2 and the C3 reflection column; 112 holds C1 only, since no portfolio row links its items; 113 holds C2 only, since it is not in the link's boardIds; 114 has neither half and no relation to an overview; 115 has neither half, a relation to the live overview 90300000116, and shares folder 90200000001 with the portfolio, so C4 is listed and not counted) | agree |
| 90300000110 / 90300000112 | partial link - review; rules ['C1']; note None | same (111 has C1, C2 and the C3 reflection column; 112 holds C1 only, since no portfolio row links its items; 113 holds C2 only, since it is not in the link's boardIds; 114 has neither half and no relation to an overview; 115 has neither half, a relation to the live overview 90300000116, and shares folder 90200000001 with the portfolio, so C4 is listed and not counted) | agree |
| 90300000110 / 90300000113 | partial link - review; rules ['C2']; note None | same (111 has C1, C2 and the C3 reflection column; 112 holds C1 only, since no portfolio row links its items; 113 holds C2 only, since it is not in the link's boardIds; 114 has neither half and no relation to an overview; 115 has neither half, a relation to the live overview 90300000116, and shares folder 90200000001 with the portfolio, so C4 is listed and not counted) | agree |
| None / 90300000114 | unconnected; rules []; note None | same (111 has C1, C2 and the C3 reflection column; 112 holds C1 only, since no portfolio row links its items; 113 holds C2 only, since it is not in the link's boardIds; 114 has neither half and no relation to an overview; 115 has neither half, a relation to the live overview 90300000116, and shares folder 90200000001 with the portfolio, so C4 is listed and not counted) | agree |
| None / 90300000115 | unconnected; rules ['C4']; note overview 90300000116 | same (111 has C1, C2 and the C3 reflection column; 112 holds C1 only, since no portfolio row links its items; 113 holds C2 only, since it is not in the link's boardIds; 114 has neither half and no relation to an overview; 115 has neither half, a relation to the live overview 90300000116, and shares folder 90200000001 with the portfolio, so C4 is listed and not counted) | agree |

## Native fixture (59 boards, 1 project entry, 1 report)

| Board | Case | Key | Mine | Verdict | Reason |
|---|---|---|---|---|---|
| 90300000201 | crm-v2-leads | native_crm_leads / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000202 | crm-v2-opportunities | native_crm_opportunities_or_deals / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000203 | crm-v2-contacts | native_crm_contacts / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000204 | crm-v2-accounts-renamed | native_crm_accounts / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000205 | crm-v2-activities | native_crm_activities / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000206 | crm-v2-sales-targets-chain-broken | native_crm_sales_targets / N4 / high; version unknown; descendant_fingerprint; limits L1; lineage UNRESOLVED | same | agree | |
| 90300000207 | crm-products-services | native_crm_products_services / N4 / high; version unknown; descendant_fingerprint; limits L1; lineage NO_LINEAGE | same | agree | |
| 90300000208 | crm-companion-marks | native_crm_companion_board / N6 / medium; version unknown; lineage NO_LINEAGE | same | agree | |
| 90300000209 | crm-companion-unresolved | native_crm_companion_board / N6 / medium; version unknown; lineage_unresolved; lineage UNRESOLVED | same | agree | |
| 90300000210 | crm-v1-deals | native_crm_opportunities_or_deals / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000211 | crm-v1-deals-copy-1hop | native_crm_opportunities_or_deals / N2 / high; family crm_core v1; descendant_copy(1); lineage RESOLVED_TEMPLATE hops 1 | same | agree | |
| 90300000212 | crm-v1-contacts | native_crm_contacts / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000213 | crm-v1-leads | native_crm_leads / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000214 | crm-v1-accounts | native_crm_accounts / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000215 | crm-v1-activities | native_crm_activities / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000216 | crm-quotes-invoices | native_crm_quotes_invoices / N2 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000217 | crm-qi-line-items | native_crm_quotes_invoices_subitems / N5 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000218 | crm-qi-generic-ids-only | ordinary_board_in_product_workspace / N9 / high; limits L2; lineage NO_LINEAGE | same | agree | |
| 90300000219 | crm-v1-deals-subitems | native_crm_opportunities_or_deals_subitems / N5 / high; family crm_core v1; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000220 | service-b-tickets | native_service_tickets / N2 / high; family B; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000221 | service-b-tickets-copy-1hop | native_service_tickets / N2 / high; family B; descendant_copy(1); lineage RESOLVED_TEMPLATE hops 1 | same | agree | |
| 90300000222 | service-b-tickets-copy-2hop | native_service_tickets / N2 / high; family B; descendant_copy(2); lineage RESOLVED_TEMPLATE hops 2 | same | agree | |
| 90300000223 | service-a-tickets-sla | native_service_tickets / N2 / high; family A; direct_install; SLA mark; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000224 | service-a-tickets-subitems | native_service_tickets_subitems / N5 / high; family A; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000225 | service-b-csat | native_service_csat_survey / N2 / high; family B; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000226 | service-b-contacts | native_service_service_contacts / N2 / high; family B; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000227 | service-satellite | native_service_satellite_probable / N7 / low; review; lineage NO_LINEAGE | same | agree | |
| 90300000228 | service-b-start-here-doc | doc_container / R1 / high; family B; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same class, rule, confidence | agree (note) | Class, rule, lineage and family agree. The key gives sla_mark null while README line 58 says sla_mark is given on a doc_container whose lineage resolves to a native template (see summary item 4). |
| 90300000229 | portal-active | native_service_portal / N1a / high; family Portal; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000230 | portal-archived-alias | native_service_portal / N1a / high; family Portal; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000231 | portal-archived-lineage | native_service_portal / N1b / high; family Portal; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000232 | workflow-object-not-portal | workflow_object / R3 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000233 | custom-object-other | custom_object_other / R3 / high; lineage NO_LINEAGE | same | agree | |
| 90300000234 | service-c-csat-view-only | native_service_csat_survey / N3 / high; family C; direct_install; lineage NO_LINEAGE | same | agree | |
| 90300000235 | service-c-tickets | native_service_tickets / N2 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000236 | service-c-incidents | native_service_incidents / N2 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000237 | service-c-tickets-chain-broken | native_service_tickets / N4 / high; family B or C; descendant_fingerprint; limits L1; lineage UNRESOLVED | same | agree | |
| 90300000238 | service-c-asset-management | native_service_asset_management / N2 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000239 | service-c-employee-lifecycle | native_service_employee_lifecycle / N2 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000240 | service-c-employee-directory | native_service_employee_directory / N2 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000241 | service-c-tickets-subitems | native_service_tickets_subitems / N5 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000242 | service-d-tickets | native_service_tickets / N2 / high; family D; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000243 | service-d-incidents | native_service_incidents / N2 / high; family D; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000244 | service-c-lifecycle-subitems | native_service_employee_lifecycle_subitems / N5 / high; family C; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000250 | lookalike-name | lookalike_board / N8 / medium; limits L2; lineage NO_LINEAGE | same | agree | |
| 90300000251 | lookalike-terminology | lookalike_board / N8 / medium; limits L2; lineage NO_LINEAGE | same | agree | |
| 90300000252 | ordinary-terminology-activity | ordinary_board_in_product_workspace / N9 / high; limits L2; lineage NO_LINEAGE | lookalike_board / N8 / medium; limits L2; lineage NO_LINEAGE; signals add imitation:terminology | **disagree** | The terminology `Activity` is itself in the NO 5:158 default list (the list names `Activity` and `"Activity "` separately, and 90300000205, a genuine v2 Sales Activities board, carries `Activity`). N8 applies: product crm, key null, NO_LINEAGE, zero reserved ids, zero marks, terminology equals a default exactly (G-97: compare exactly, without trimming). The key says no imitation, which the written rule does not support. Totals are unaffected (the board is in limits[]); the limits[] row class, the board entry, the signals and the README case row change. |
| 90300000253 | ordinary-terminology-client | ordinary_board_in_product_workspace / N9 / high; limits L2; lineage NO_LINEAGE | same | agree | |
| 90300000254 | ordinary-links-into-native | ordinary_board_in_product_workspace / N9 / high; limits L2; lineage NO_LINEAGE | same | agree | |
| 90300000255 | default-shaped-satellite | ordinary_board_in_product_workspace / N9 / high; limits L2+L3; lineage NO_LINEAGE | same class, rule, confidence | agree (note) | Class, rule, confidence, L2 and L3 agree. The board entry lists L2 and L3 but the top-level limits[] row holds only L3 (see summary item 3). |
| 90300000256 | stripped-native | lookalike_board / N8 / medium; limits L2; lineage UNRESOLVED | same | agree | |
| 90300000257 | planted-ids | native_crm_leads / N4 / high; version unknown; descendant_fingerprint; limits L1; lineage NO_LINEAGE | same | agree | |
| 90300000258 | ordinary-test-blank-defaults | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000259 | ordinary-test-suffixed-ids | normal_classic_board / R11 / high; lineage NO_LINEAGE | same | agree | |
| 90300000260 | native-moved-to-core | native_descendant_misplaced / N10 / low; family sales_crm v2; direct_install; fingerprint crm/accounts; review; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000261 | keyed-board-with-native-signals | keyed_board_unrecognized_key / R7 / low; review; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000262 | deleted-native-lineage-only | native_crm_contacts / N2 / high; family sales_crm v2; direct_install; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000263 | portfolio-cursor | portfolio_board / R4 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |
| 90300000264 | project-incomplete-read | project_tasks_board / R5 / high; lineage RESOLVED_TEMPLATE hops 0 | same | agree | |

Totals: 59 boards (57 swept plus 90300000220 and 90300000221, which only the lineage-hop pages return). Twelve boards are in limits[] (206, 207, 218, 237, 250, 251, 252, 253, 254, 255, 256, 257), the totals add to 47, and 47 + 12 = 59 = `board_count`, which agrees. Each total recounts correctly from my classes; moving 252 from N9 to N8 changes no total, since it stays in limits[]. `unreadable_ids` (90300000901, 902, 903) equals the union of the two hop page `missing_ids` and agrees. `sweep_complete` true agrees: all eight swept workspaces end on an empty page, and workspace 90100000208 is reached only by hop pages. The hop walk agrees: 211 resolves through 210 (1 hop), 221 through 220 (1), 222 through 221 and 220 (2), 206, 209, 237 and 256 end UNRESOLVED at 901, 902, 903 and 901, and no id is left for `next_ids`. `native_board_index` (43 entries: every `native_` class including N6, N7, N10 and the three Portals, never N8, N9, R-classes or the workflow object) and `portal_object_ids` (active 229; archived 230 and 231, by board state) agree with W16. `reports`: 90100000207 (crm, empty) reports "product boards not installed here", 90100000201 and 90100000203 hold natives, 90100000205 and 206 are core; agrees.

| Project entry | Key | Mine | Verdict |
|---|---|---|---|
| None / 90300000264 | incomplete read - review; rules [] | same (neither half: link targets empty, the one portfolio item links no item; the portfolio items page ends on cursor c-000001, so W80 gives incomplete read - review; confidence is not carried on a project entry) | agree |

## Compare fixture (27 entries)

Method: the two reads were diffed field by field and each difference was kept or dropped by W75; the W73 digests were recomputed (columns 303 `columns:d5e22944` to `columns:bc67b9ab`, plan `plan:18ba9741` to `plan:2c859f18`, the protected row digests `b1:a5fd4249` against `b1:597a09cf`, `b2:1e555f1f` equal, `b3:9a823b26`) and all match the key.

| Entry | Case | Key | Mine | Verdict | Reason |
|---|---|---|---|---|---|
| scope | scope | boards 301, 302, 303, 304, 305, 306, 311, 312; live rows ['002:B1', '002:B2']; dropped ['309'] | same: B1 to B6 (301 to 306), plus 311 and 312 (do-not-change and change-with-own-yes; 313 is free); 309 is a read entry outside the scope; its column change is therefore not flagged | agree | |
| board:90300000301.description | description-change | flag: Weekly intake to Weekly intake and triage | flag, same field and problem string | agree | |
| board:90300000302.state | archived-board | flag: active to archived | flag, same field and problem string | agree | |
| board:90300000303.columns_digest | column-digest-change | flag: columns:d5e22944 to columns:bc67b9ab | flag, same field and problem string | agree | |
| board:90300000304.owners | owner-change | flag: ["90600000001"] to ["90600000001","90600000002"] | flag, same field and problem string | agree | |
| agent:90800000301.version_id | agent-version-id-moved | flag: vid-000001 to vid-000002 | flag, same field and problem string | agree | |
| agent:90800000301.plan_digest | agent-version-id-moved | flag: plan:18ba9741 to plan:2c859f18 | flag, same field and problem string | agree | |
| agent:90800000302.state | agent-state-moved | flag: ACTIVE to INACTIVE | flag, same field and problem string | agree | |
| workflow:90300000308.state | workflow-state-moved | flag: active to archived | flag, same field and problem string | agree | |
| 002:B1 | protected-row-moved-before | changed outside: b1:a5fd4249 to b1:597a09cf, moved in ['before', 'after'] | same (recorded digest from the ledger over the name `Ivrel Ledger`; both snapshots show `Ivrel Ledger Old`; warning, not a flag) | agree | |
| board:90300000305 | control-unchanged-board | not flagged | not flagged | agree | |
| board:90300000306 | control-updated-at-only | not flagged | not flagged | agree | |
| automation:91100000301 | control-unchanged-automation | not flagged | not flagged | agree | |
| form:90400030102 | control-unchanged-form | not flagged | not flagged | agree | |
| doc:91300000301 | control-unchanged-doc | not flagged | not flagged | agree | |
| dashboard:91200000301 | control-unchanged-dashboard | not flagged | not flagged | agree | |
| vibe_app:90900000301 | control-unchanged-vibe-app | not flagged | not flagged | agree | |
| board:90300000312 | control-protected-row-unmoved | not flagged | not flagged | agree | |
| board:90300000309 | control-dropped-from-scope | not flagged | not flagged | agree | |
| document 1 | appendix-mutation | refused (mutation) | refused (mutation) | agree | |
| document 2 | appendix-subscription | refused (subscription) | refused (subscription) | agree | |
| document 3 | appendix-two-operations | refused (more than one operation) | refused (more than one operation) | agree | |
| document 4 | appendix-clean-query | pass (one query) | pass (one query) | agree | |
| document 5 | appendix-word-in-string | pass (one query) | pass (one query) | agree | |
| document 6 | appendix-word-in-comment | pass (one query) | pass (one query) | agree | |
| document 7 | appendix-json-query-string | pass (one query) | pass (one query) | agree | |
| exit code | exit | 1 | 1 (flags and refused documents block; the changed-outside row alone would give 2) | agree | |

Tokenizer traps, traced by hand against W77: document 5 holds the word in a variable default string and inside a string argument nested in braces within the selection set, one `query` operation, passes; document 6 holds it in a `#` comment before a query, passes; document 7 is a `json` fence whose one `query` string parses to one query, passes; the `graphql` block after `## Notes` lies outside the appendix section and is never read; document 3 is a `gql` fence with two operations (refused), document 1 a mutation, document 2 a subscription. No fenced block in the appendix has a refused info string. Controls: 305 (unchanged), 306 (updated_at only), the automation, form, doc, dashboard and Vibe app (unchanged reads), 312 (protected row unmoved) and 309 (dropped) are all correctly absent from the flags. `ledger_sha256` and `account_sha256` are not in these reads (README says so); K302 is untested by this pair.

## Reconcile fixture (31 entries)

Method: W71 applied row by row to the ledger state and `live-inventory.json`; the identity digests of every verified row were recomputed from the inventory (W1, W2, F1, B1, D1 and DB1 equal their recorded digests; B3, A2 and AG2 differ; B4, B5 and DB2 have no live match or are deleted), and the intent digests recompute as recorded. Live objects were claimed by W71's list, and each attempting row was matched on name, workspace and created_at.

| Output position | Key | Kind | Key class | Mine | Verdict | Reason |
|---|---|---|---|---|---|---|
| 1 | A1 | automation | adopt; live ['401']; confirm true; needs_read None; predates false | same | agree | |
| 2 | A2 | automation | changed-since-verified; live ['402']; confirm false; needs_read None; predates false | same | agree | |
| 3 | AG1 | agent | adopt; live ['401']; confirm false; needs_read manage_agent get; predates false | same | agree | |
| 4 | AG2 | agent | changed-since-verified; live ['402']; confirm false; needs_read None; predates false | same | agree | |
| 5 | None | agent | unrecorded-extra; live ['403']; confirm false; needs_read None; predates false | same | agree | |
| 6 | VB1 | vibe_app | partial; live ['401']; confirm false; needs_read None; predates false | same | agree | |
| 7 | VB2 | vibe_app | duplicate; live ['402', '403']; confirm false; needs_read None; predates false | same | agree | |
| 8 | WF1 | workflow | adopt; live ['420']; confirm true; needs_read None; predates false | same | agree | |
| 9 | B1 | board | partial; live ['401']; confirm false; needs_read None; predates false | same | agree | |
| 10 | B2 | board | partial; live ['402']; confirm false; needs_read None; predates false | same | agree | |
| 11 | B3 | board | changed-since-verified; live ['403']; confirm false; needs_read None; predates false | same | agree | |
| 12 | B4 | board | missing; live []; confirm false; needs_read None; predates false | same | agree | |
| 13 | B5 | board | missing; live ['405']; confirm false; needs_read None; predates false | same | agree | |
| 14 | B6 | board | adopt; live ['416']; confirm false; needs_read None; predates false | same | agree | |
| 15 | B7 | board | duplicate; live ['417', '418']; confirm false; needs_read None; predates false | same | agree | |
| 16 | B8 | board | retry; live []; confirm false; needs_read None; predates false | same | agree | |
| 17 | B9 | board | retry; live []; confirm false; needs_read None; predates false | same | agree | |
| 18 | None | board | unrecorded-extra; live ['419']; confirm false; needs_read None; predates true | same | agree | |
| 19 | None | board | unrecorded-extra; live ['421']; confirm false; needs_read None; predates false | same | agree | |
| 20 | DB2 | dashboard | missing; live []; confirm false; needs_read None; predates false | same | agree | |

Order: automations (A1, A2), agents (AG1, AG2, then the unrecorded extra agent), Vibe apps (VB1, VB2), workflows (WF1), then boards in key order with the board extras after B9, then dashboards; agrees with W71 and K274 and K275.

| Row | Key bucket | Mine | Verdict | Reason |
|---|---|---|---|---|
| D1 | unchanged | unchanged | agree | live digest equals the recorded one; no child row carries this `parent_key` |
| DB1 | unchanged | unchanged | agree | live digest equals the recorded one; no child row carries this `parent_key` |
| F1 | unchanged | unchanged | agree | live digest equals the recorded one; no child row carries this `parent_key` |
| W1 | unchanged | partial | **disagree** | W71 reads: a `verified` row whose live digest is unchanged "while a row under it (by `parent_key`) is not `verified`" is `partial`. W1's live digest is unchanged, and B2 (written), B6 to B9 and A1 (attempting), B10 (planned), B11 (departed) and B12 (removed) all carry `parent_key` W1 or sit under it, and none is verified. By the letter W1 is `partial` (counts: partial 4, unchanged 4). The key evidently reads "under it" as structural parts (columns and groups under a board) and not as every child by `parent_key`. The rule text is ambiguous between those two readings; see the summary. |
| W2 | unchanged | unchanged | agree | live digest equals the recorded one; no child row carries this `parent_key` |
| B10 | not_started | not_started | agree | planned |
| B11 | not_reconciled | not_reconciled | agree | departed or removed |
| B12 | not_reconciled | not_reconciled | agree | departed or removed |
| B1.C1 | not_in_inventory (column, written) | same | agree | columns and groups are in no inventory (W71) |
| B1.G1 | not_in_inventory (group, verified) | same | agree | columns and groups are in no inventory (W71) |

Classes: adopt 4, retry 2, duplicate 2, partial 3, changed-since-verified 3, unrecorded-extra 3, missing 3 agree with my derivation, W1 aside. Traps traced: 419 (created 08:30, before B9's attempt at 09:07) is listed as an extra with `predates_attempt` true and B9 is `retry`; 421 is an extra; 431 (native index), 432 (the `live_objects` monday_id) and 433 (workspace 90100000403, outside strand 001's targets) are correctly not extras; A1's live title is 48 characters and is a prefix of the row name, so it matches by the 40-character rule and adopts with confirm; WF1 adopts with confirm because the read has no created_at; AG1 carries needs_read; agent 403 (created 09:25, after the earliest attempt) is an extra; DB2 is missing through the dashboards read's `missing_ids`.

| Classify-only run | Key | Mine | Verdict | Reason |
|---|---|---|---|---|
| holder 001, asked by 002 | run run-2026-10-16-1 to state interrupted; mode classify-only; counts equal the full run; findings 20 in the same order; objects unchanged | same (the lock run_id names the run; its state is `running`; every count and finding equals the full run's) | agree | The lock heartbeat is 09:35 and the inventory is read 10:30, 55 minutes apart; ARCHITECTURE calls a heartbeat stale after 60 minutes, and the classify-only call refuses a fresh lease, so the test must set its clock at or after 10:35. The fixture does not state this (see plausibility). If W1 is read as partial (summary item 2) the classify-only findings would list it too. |

## Coverage against PLAN section 4.2

Identification: every item has a board. R0 paging to an empty page: pages 2 and 4. R1: 101. R2: 102 (parent) and 103. R3: 104 and 106 workflow objects, 105 other. R4: 110. R5: created 111, converted 113, unknown origin 114, transient key 112. R6: live 116, deleted 117. R7: 121. R8: 118 (plus the near miss 119). R9: 120. R10: 122. R11: 123. C1 to C4: connected 111, one half (112 on C1, 113 on C2), neither 114, folder evidence 115. States: active, archived (106, 124), deleted (117, 125). Complete.

Native: complete against the list: CRM v2 (leads, opportunities, contacts, accounts, activities, sales targets) and core v1 (deals, contacts, leads, accounts, activities, Quotes & Invoices); companions N6 (208, 209); Quotes & Invoices with line items (217); Products & Services (207); Service A (223, 224), B (220 to 222, 225, 226, 228), C (234 to 241, 244), D (242, 243); the satellite N7 (227); the Portal active, archived by alias and archived by lineage (229 to 231); lineage at 0, 1 and 2 hops and UNRESOLVED (206, 209, 237, 256); N4 on a chain-broken native (206, 237) and on planted ids (257); N3 (234); blank defaults and suffixed ids that count for nothing (258, 259); the SLA mark (223, the `_lst/_ewh/_itr/_ttp` stem has four ids); two look-alikes (250, 251) and the stripped native (256); the renamed native `Org` (204); an ordinary board linking into a native (254); ordinary boards in product and test workspaces; N10 (260); the keyed board, the other custom object and the Start here doc staying `doc_container`; the deleted native (262); the known limits L1, L2, L3; a page that drops three ids (page 15). Compare: all of the PLAN list is present. Reconcile: all seven classes, automations first, and the classify-only run.

Gaps that PLAN does not require but a grader could use: no W84 tie case (two entities meeting their thresholds, which would give medium confidence); no R3 case without a `workflow_objects` page (low confidence, W79); no Service family B or D subitems board or D Start here doc; no R11 board in a service workspace that is L3-shaped; no N10 board from a Service template; no N3 case on a CRM family without lineage.

`models` citations: each cited rule, section and probe was read against the behaviour; the large majority carry it. Weak or indirect citations: `G-74` on 90300000105 and 90300000233 (G-74 is about portfolio and project keys being invisible to `objects()`; the behaviour of a custom object outside the workflow set is better carried by G-100 and W79); `G-65` on the unchanged automation control (G-65 is about switching off, not about an unchanged read); `G-88` on the unchanged form control (G-88 is about a form on a project tasks board); `G-81` on 90300000114 (G-81 gives the order; the hidden-columns origin-unknown case is carried by NO 5 R5, which is also cited); `G-77` on the deleted board 90300000125 (G-77 concerns the deleted overview board, though the empty columns of a deleted board are the same behaviour). None changes an answer. `AI:21` resolves to line 21 of `ai-offerings-findings.md` (the `version_id` drift note), which is the right anchor for the agent flags. K-numbers cite CONTRACT items and were spot-checked (K272, K287, K300, K302, K336), not all re-read.

One naming point, not a disagreement: W16 lists `lifecycle_subitems` and `deals_subitems` as entity names, while W83 and the N5 row give the class as `native_<product>_<parent>_subitems`; the key follows W83 (`native_service_employee_lifecycle_subitems`, `native_crm_opportunities_or_deals_subitems`), which is the more explicit text.

## Plausibility against the sources

Agrees: ids are strings throughout; column ids and types follow NO 2.6 and the gotchas (`name`/`person`/`status`/`date4`, `date0` on subitems boards, `person` typed `people` on the Portals and `person` on the workflow objects as G-98 gives, suffixed ids all match `^[a-z_0-9]+_(mk|mm)[a-z0-9]{6,8}$`, the SLA helper ids match the helper regex and not the suffix regex as NO 2.4 describes, `staticImage` values are from the five-name set, Quotes & Invoices relations carry `{}` settings as G-101 says, v1 `activity_item` carries no `staticImage`, `enrolled_sequences_` is `unsupported`); the links alias holds exactly the relation, subtasks and mirror columns; deleted boards return empty columns and views and zero items (G-77); the overview is at the root and the tasks board and planner share a folder (G-72); the planner `rp_connected_project` settings are `{}` (NO 7.4); the Portal, the Portal view `200776197` and the workflow objects with a `FeatureBoardView` follow G-100, G-69 and W79; account product kinds are `core`, `crm`, `service`; the agent, Vibe and workflow shapes follow P-19 to P-21 (agent states, the two unrequested triggers, `version_id` moving with the plan and not with the state, which the compare fixture uses correctly, no agent workspace field, Vibe statuses `GENERATING` and `READY`, workflow objects board-backed). The `workflow_objects` and `portfolio_items` pages follow W79 and W80.

Names: every invented name is a neutral coined word or a plain descriptive phrase; none reads as a real organisation, person or product. The native default names used (Leads, Tickets, Portal and so on) are monday's own and are meant.

Observations that are not answer-key disagreements:

- (summary item 5) G-10 and G-69 say workflow objects appear in `boards(workspace_ids, state: all)` as `custom_object` boards, and the identification and native reads do include such boards, yet the compare reads (workflow 90300000308) and the reconcile inventory (workflow 90300000420) omit them from `inventory[]` and `boards[]` while the doc container boards (307, 410) are present. If a capture lists them, the reconcile run would see an unclaimed board in a target workspace that the key does not account for (it would have to be claimed as WF1's match). Unsure whether this is a modelling gap or a deliberate separation.

- The project tasks boards (111, 115, 264) carry a `TableBoardView` named Main table; G-72 says a created tasks board carries one Gantt view, and G-85 says Gantt views read back as type null. No rule reads these views, so no answer changes.

- In `reconcile/ledger-state.json`, AG2's `attempt.started_at` (2026-10-14T10:59:00Z) predates its own run `run-2026-10-15-1`, which started 2026-10-15T08:58:00Z, and AG2 and A2 each have `verify.at` equal to `attempt.started_at`. No class changes, but the strand's earliest attempt (used for agent extras) is then the 14th and not the 15th; the two readings differ only if an agent were created between those times, and none is.

- The lock heartbeat (09:35) against the inventory read (10:30) is 55 minutes, inside the 60-minute freshness window of ARCHITECTURE; the classify-only test needs a stale lease and so needs its clock set after 10:35. The fixture says nothing of this.

- The two portfolio boards differ in `portfolio_project_priority` type (status in the identification reads, mirror in 263); harmless.

## Summary

Checked: 81 boards (22 identification, 59 native), 6 project entries, 1 report, 27 compare entries and 31 reconcile entries, 146 entries in all. Disagreements: 5.

| # | Where | What | Mark |
|---|---|---|---|
| 1 | native `90300000252` (`ordinary-terminology-activity`) | The key gives N9 `ordinary_board_in_product_workspace`, high, with L2; the written rule gives N8 `lookalike_board`, medium, with L2, because `Activity` is in the NO 5:158 terminology list (G-97: compare exactly). Fix by changing the key and README, or change the board's terminology to a word outside the list if an N9 case on terminology is wanted. | the key is wrong |
| 2 | reconcile `W1` | The key lists W1 as `unchanged`. W71 read to the letter makes it `partial`, because its live digest is unchanged while rows with `parent_key` W1 are not verified. Readings: (a) every child row by `parent_key` counts, so W1 is partial and the counts become partial 4, unchanged 4; (b) only structural parts of the row (columns, groups, views, forms under a board) count, so W1 is unchanged and B1 is partial through B1.C1 (the key's reading). The rule needs a sentence saying which. | the rule text is ambiguous |
| 3 | native `90300000255` limits | The board entry lists L2 and L3, the top-level limits[] row only L3 (fixture-notes item 8: one row per board, most specific code, to keep `board_count` equal to totals plus limits). Readings: (a) one row per board, so L2 is not listed at the top level (the key); (b) one row per code, which breaks W01's `board_count` formula (it would give 60). W83 says an L2 attaches to every N9. | the rule text is ambiguous |
| 4 | native `90300000228` attributes | README line 58 says sla_mark is given on a doc_container whose lineage resolves to a native template; the key and fixture-notes item 5 give sla_mark null there (boolean on native classes only). Readings: given (false) or null. No rule text decides it. | the rule text is ambiguous |
| 5 | compare and reconcile reads | Workflow object boards (308, 420) are absent from the inventories though G-10 and G-69 put such boards in `boards(state: all)`; see the plausibility section. | unsure |

Every other board, flag, changed-outside row, control, document verdict, class, order and count agrees with my derivation. The key is wrong in one place (item 1); the rest need a sentence in a rule or a README line, or a decision by the step-4 author.
