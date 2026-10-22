# Probe: how a new CRM workspace gets monday's native CRM boards (A5, A37)

Internal build file: never client-facing. Run by the main session on 2026-10-22, in the new CRM test workspace (A37), ring 2026-10 release candidate. Ids stay in the client records and `local/`, never here. Template ids are monday's own constants, as in `shared/native-objects.md`.

1. **A workspace created through the API in the CRM product is empty.** `create_workspace` with the CRM product's account product id makes a closed workspace whose `account_product.kind` is `crm`, with no boards and no folders. Nothing native comes with it, so a CRM build in a new workspace (A21) has no native boards to use until something installs them.
2. **`use_template` cannot take a board template id.** Its `template_id` is a 32-bit `Int`, and monday's CRM board template ids (`5678953932` and the rest) do not fit: "Int cannot represent non 32-bit signed integer value". It installs another kind of template, probably the multi-board solutions of the template centre, asynchronously: `template_installation_status(process_id)` reports `board_ids` and a `board_ids_map` from each template board to its new board. The API has no query that lists those templates or their ids.
3. **A raw `create_board(template_id: <board template id>, workspace_id, folder_id, board_kind: public)` installs a genuine native.** With v2 Leads (`5678953932`) it returned a board named as asked, in the folder, with:
   - `created_from_board_id` equal to the template id (lineage resolved at 0 hops, `N2`) and `item_terminology` "Lead";
   - the template's views (`source_view_id` `124433515`, `124433523` and `124433528`, the v2 Leads view ids of section 3.2);
   - the reserved ids `lead_owner`, `lead_status`, `lead_email`, `lead_company` and `lead_phone`;
   - the CRM feature columns `enrolled_sequences_*` and `custom_*` (`CRM_FEATURE_MARK`);
   - three `staticImage` relations (`CRM_RELATION_MARK`).
   
   By every rule in `native-objects.md` it is a native install. This is the call guard R-D blocks in a build.
4. **But it arrives alone and not empty.** Its relations to Contacts and Accounts (`link_to_contacts`, `link_to_accounts7`) have `boardIds: []`, with layout settings keyed by the template's board ids; only its self-relation (duplicate detection) points at itself. It brings the template's own three groups and 15 sample items. A linked set installed board by board therefore needs every relation column pointed at the set's other boards (`update_column` on a native, which guard R-B blocks), and the template's sample items cleared or kept.
5. **Left in the workspace:** the folder "Probe – native install" and the one probe board, both test objects.
6. **The in-account CRM solution does not install through `use_template`.** The user found monday's CRM solution in the account's own Template Center (an in-app template page; the public site has no page for that id). `use_template` with its id and the CRM test workspace failed twice with `Internal server error` (`DOWNSTREAM_SERVICE_ERROR`), once with a folder name and board kind and once with only the two required arguments, and created nothing. The documented errors are only the two managed-template limits and `USER_UNAUTHORIZED`, and `solution_extra_options` is undocumented.
7. **`use_template` itself works.** A public template, "Single Project" (id `122904`, from its public page), returned a `process_id` at once, and `template_installation_status` reported `IN_PROGRESS` with its boards mapped from the template's. So the gap is the CRM product's solution, not the mutation.
8. **Also left in the workspace:** the folder "Probe – use_template check" and the boards that template installed, test objects.

## The build's own install, probed after A38 (2026-10-22)

9. **Four more natives from their template ids, with the probe's Leads, make a v2 set:** Contacts (`5678953938`), Accounts (`5678953942`), Deals (`5678953956`, the v2 Opportunities template under the name asked) and Sales Activities (`5678953951`). Each came with `created_from_board_id` equal to its template id and the template's own rows: 16, 13, 18 and 10, and Leads' 15. Sent as four aliased `create_board` calls in one request, the call **timed out and all four boards were made anyway**. Install one board per call, and read the workspace before any retry.
10. **What each template's links were meant for** is readable before linking: an empty `boardIds` with `dataSourceLayoutConfigs` keyed by the intended template board id. For the v2 set:
    - Leads: `link_to_contacts` to Contacts and `link_to_accounts7` to Accounts. Its self-relation `connect_boards8` (duplicate detection) already points at itself.
    - Deals: `deal_contact` to Contacts, `connect_boards31` to Accounts, and `link_to_accounts_management` to an onboarding companion.
    - Accounts: `account_contact` to Contacts, plus three companion links (projects, onboarding, invoices).
    - Contacts: no links of its own.
    - Activities: `activity_item` holds template board ids and its own.
11. **Linking works through `update_column` with `{"boardIds": [<installed board>]}`,** with `allowCreateReflectionColumn: true` kept where the template had it. Five links went in: Leads to Contacts and to Accounts, Deals to Contacts and to Accounts, and Accounts to Contacts. Where the template allowed it, monday added the reflection column on the other board, named "link to <board>" (Contacts got "link to Deals" and "link to Accounts", Accounts got "link to Deals"), so those links are two-way (A32) and the reflection columns want renaming. The update keeps `displayType` and drops the template's `dataSourceLayoutConfigs`, `staticImage` and `boardId`, so the linked item's card loses its layout and the column loses its `CRM_RELATION_MARK`, which is cosmetic for the build and matters for detection (item 15).
12. **The revision is per column, not per board.** Each column has its own `revision`, and the one an `update_column` returns is that column's. Passing it to another column on the same board fails with "Board revision mismatch" (409); each column's own revision, read once before linking, works.
13. **Sales Activities' `activity_item` cannot be re-pointed:** `update_column` answers "Resource not found" (404) twice, with and without `allowMultipleItems`. It still lists template board ids. Activities stay out of a native set until a way is found. The CRM product's own activity timeline (the connector's timeline tools) is the likely place for activities instead.
14. **The template's rows archive cleanly in batches:** 18 aliased `archive_item(item_id:)` calls in one request returned every item `archived`. No template carried an automation (`board_automations`, items and legacy both empty on all five boards). The raw `BoardAutomation` field is `active`, while the `list_automations` tool returns `is_active`.
15. **Still stale after linking:** Deals' mirror `deal_account` keeps `relation_column {deal_contact}` and the template ids `2673708477` and `1631647074` (the `V2_OPPS_FINGERPRINT`), so it shows nothing. A blueprint either re-points such a mirror as a planned column row or leaves it, and says which. Detection still reads every board as native by lineage, template view ids and reserved ids, but the linked relations no longer carry `staticImage`.

**Where this leaves A5 for new CRM workspaces (2026-10-22):** monday's CRM solution goes in through the UI only, or the build installs the natives board by board (item 3) and links them itself (item 4). Asking monday support about `use_template` and CRM solutions is the third way.

**For the user's choice:**
- (a) the user installs monday's CRM solution in each new CRM workspace through the UI, once, and the build detects and uses those boards as A5 designed;
- (b) the build installs the natives itself, board by board from the template ids, links their relations and clears the template's sample items, which needs R-B and R-D narrowed for natives the build itself installs;
- (c) find a solution-template id `use_template` accepts, which the API does not list.
