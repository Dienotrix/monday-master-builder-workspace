# account-build skill: notes from demo 3

## Result

Built. The first pass stopped at phase 7, when the permission layer refused A1's `create_automation`. The user then allowed the connector's automation, dashboard and widget tools, and the build resumed in the same run and finished. The run is ended, the lease is released, `version.md` is `built` with its `## Build` section, and `record.py check` and `ledger.py check` are both clean.

- **Built and verified: 47 elements**, plus the referenced workspace W1 verified by read (48 verified rows):
  - the folder F1 and the four native installs B1 to B4;
  - all 26 columns, both mirrors included;
  - the two groups and five item batches (87 rows);
  - four table views, the form B1.FM1, the automation A2 and the dashboard DB1.
- **Not checkable: 8**, the eight widgets DB1.W1 to DB1.W8 (G-11).
- **Departed: 1.** A1 was built but stored its condition inverted (note 1). It is live, marked departed in the live map, with UI step U4 to fix it.
- **UI steps: U1 to U5.** The three planned ones, U4 for A1's condition, and U5 to switch off both alerts after the demo.
- **monday calls: 102**, every connector call counted, schema reads and reconcile reads included. The one refused call is not counted.
- **Fallback fired:** Close probability. DB1.W2 and DB1.W7 sum Deal value.

## Notes, most important first

1. **A1 was stored with its condition inverted** (skill, phase 7; G-153). The prompt named the condition "Only if the status column Stage is Quoted". Write-path's prompt shape has no Conditions block, so that wording was my own. `create_automation` stored the condition block "If status is something" on Stage, label Quoted, with `shouldCheckIfStatusIsNot` true, titled "is not". The trigger was right: When date arrives on Last activity, 8:00 in the account's time zone, offset 7 days, receiver the user, and the message reads the item name and Last activity. The read carries no before or after field for the offset, so its direction is not checkable. What I did: as the skill says, verified it `mismatch` and departed it with decision `ui-step` (U4), without a second automation. It is live: as stored it alerts on quotes that are not Quoted, 7 days after their last activity. Write-path should give the Conditions block's shape, and say to read `shouldCheckIfStatusIsNot` on every status condition.

2. **Resuming a row left `attempting` whose call never left the session needs a reconcile, which neither the skill nor write-path mentions** (write-path, "When something goes wrong"). Write-path says only to read the board and record what exists, or depart the row. Reading `list_automations` showed nothing, but `intent --retry` (and `depart`) on an `attempting` row first needs `ledger.py reconcile --strand <id> --inventory <live-inventory/1 file>`, over a read made after the attempt began, classing the row `retry`. What I did: read the workspace (folders, boards, docs) and the automations on both build boards, wrote the `live-inventory/1` file record-map gives, and ran `reconcile`. It classed A1 `retry` and listed the probe folders' boards as unrecorded extras (left untouched). Then `intent --retry` and the call. Write-path should give this sequence, and say that a refused call (permission, lint) leaves the row `attempting` like a timeout does.

3. **UI step keys collide with the planned ones** (skill, phases 7 and 9). `depart --decision ui-step` mints the next free U number, and the planned U1 to U3 are written only in phase 9. Had A1 departed first, its fix would have taken U1, the kanban step's key. What I did: wrote U1 to U3 with `--key` before the departure, so A1's step became U4. The skill should write the planned UI steps before phase 7, or `depart` should skip keys the frozen revision names.

4. **A permission layer can refuse a write the approval covers** (skill, opening paragraph and phase 7). The skill says the scripts need allowing before the first command, but says nothing about the connector's write tools. `create_automation` was refused by the session's auto-mode classifier as an unrequested commit, after 43 elements were live. What I did: stopped, as the brief says, leaving the A1 row `attempting` with no call made. The skill should say, beside the script allowance, that every connector write tool the plan needs (`create_automation` and `create_widget` especially) is allowed before the first write, and what to do with an `attempting` row whose call never left the session (note 2). After the user allowed the tools, the build resumed in the same run.

5. **The leak lint refuses things a native CRM build needs** (write-path, "The payload"). It blocked every phone number (the id-pattern rule matches any run of eight or more digits, and monday's phone value is digits only), three of the frozen revision's own sample account names, one lead name and three contact values (wall rule: words that are names in another client record). What I did: the lint's own remedy, the text without it. Four companies renamed, three contact values changed, phones left empty on leads and contacts. The revision asked for 555 phone numbers. The skill should say that phone values cannot pass the lint and that a sample plan never asks for them, and the blueprint step should lint its sample names before the revision is frozen, so the build does not rename approved rows.

6. **A planned new column can already exist in the template** (skill, phase 2, "On an installed native"). The Leads template brings a Region status (with three other labels) and the Opportunities template brings a Last activity date; the revision plans both as new columns. What I did: took the template's columns as B1.C3 and B4.C8 (update rows: Region relabelled to the three planned labels, Last activity a title-only update with its own title), rather than add a second column of the same name that the automation prompts could not tell apart. The skill should say to match planned new columns against the template's columns by name and type first, and the blueprint should name them as the template's.

7. **The payload is the call's arguments, not the GraphQL text** (write-path, "The payload"). My first board payload carried the raw mutation text; the lint blocked the three ids inside the query string. With the arguments as fields it passed. Write-path should say so for raw calls. My own explanatory "note" fields in two payloads were also blocked (element keys read as pain ids); a payload should carry nothing that is not sent.

8. **The template's relations did not match the build check's expectations** (revision section 16, two-way pairs). Opportunities does carry an empty relation to Accounts (titled Account), so B4.C2 is that column linked, not a new connect column; it shared the name Account with the stale mirror until the mirror was renamed. Contacts carries no relation of its own to accounts, deals or leads, so B2.C1, B2.C2 and B2.C3 are all reflections. The two Leads relations carried no `allowCreateReflectionColumn`; G-158 says keep it "where the template had it", A32 and the plan say two-way, so I set it true and both reflections appeared. The skill should say a relation is made two-way whether or not the template set the flag.

9. **The Close probability fallback fired** (revision section 16, Stage relabel). The template's Close probability formula reads the old stage names, so every open stage reads 5 per cent, Won 100 and Lost 0, and Forecast value is a twentieth of Deal value. The build check's fallback: DB1.W2 and DB1.W7 are to sum Deal value, and section 1 item 6 (the forecast from likelihood) is shown as not yet built. Applied: both widgets sum Deal value, and version.md's Build section says the likelihood forecast is not built.

10. **`monday_tier_source` has no "bind" value** (skill, before the first write, step 2). `record.py` accepts only `preflight`, `client statement` or `unread`. Written as `preflight`. The skill should name the value.

11. **The irreversible list** (skill, step 3). The revision's section 15 lists the installed boards and the automations as irreversible; the skill says `--irreversible` only for workspace and folder rows. Followed the skill (`--irreversible F1 --referenced W1`); under the own-account card the boards and automations took the card class. The skill should say whether section 15's boards belong on the flag.

12. **The change check's roster diff** (skill, step 4). The skill does not say whether tools the session has beyond the roster belong in `added`. I listed them all (68); nothing was removed.

13. **The form on a native Leads board works** (revision section 16, B1.FM1). A FORM view was created, eleven questions hidden, the title set and "require login" turned on first, all read back through `get_form`. The fallback did not fire. The Leads template also brings its own "Web Form" view, which the build did not touch; its login setting was not read.

14. **Smaller observations.** Relabelling Stage removed the omitted labels, the empty default included, without error. The stale mirror's revision changed when its relation column (then Contacts) was linked, though the mirror itself was not touched. A title-only update that changes nothing returned the same revision. Archiving the template rows has no ledger row of its own; it sits between the board's `record` and its `verify`, which the skill could say in one line. A widget verified `not-checkable` stays `written` in the ledger, not `verified`, so a count of verified rows leaves the widgets out. The dashboard appeared in search at once, scoped to the workspace. `all_widgets_schema` offers month grouping on a date axis, so DB1.W2's week fallback was not needed. The `live-inventory/1` file needs a `read_at`; I stamped it seconds after the reads it holds, since the tools return no read time.

## The native installs

- **B1 Leads** from 5678953932: one `create_board` call, into F1; 15 template rows archived in one aliased call; read showed `created_from_board_id` 5678953932, `items_count` 0, in the folder. Verified.
- **B2 Contacts** from 5678953938: one call; 16 rows archived in one call; verified the same way.
- **B3 Accounts** from 5678953942: one call; 13 rows archived in one call; verified.
- **B4 Opportunities** from 5678953956, named Opportunities at the create: one call; 18 rows archived in one call; verified. Its three template groups stay; the first two renamed Open quotes (B4.G1) and Closed (B4.G2); Lost/On Hold is left empty.
- No call timed out and no retry was needed. The ledger registered all four in the native board index.

**Links**, each by `update_column` on that column's own revision, each reflection renamed by a title-only update and read back on both boards:

- B1.C1 Contacts (the template's empty contacts relation) to B2; reflection B2.C1 Leads.
- B1.C2 Accounts (the template's empty accounts relation) to B3; reflection B3.C1 Leads.
- B4.C1 Contacts (the template's Contact relation, renamed) to B2; reflection B2.C2 Opportunities.
- B4.C2 Account (the template's empty accounts relation) to B3; reflection B3.C3 Opportunities.
- B3.C2 Contacts (the template's contacts relation, renamed) to B2; reflection B2.C3 Account.

Template relations the plan does not link (the Leads duplicate detector, the Opportunities and Accounts links to onboarding, projects and invoices boards) were left as installed and hidden in the planned views. None has the name of a planned reflection.

**Mirrors.** The stale template mirror on Opportunities was re-pointed as B4.C9 Account last visit, through B4.C2 to B3.C6 Last visit, `calcType` latest; the rows show the linked account's last visit. Its fallback did not fire. B3.C8 Pipeline value was created through B3.C3 over Deal value, sum; as G-31 says, its `display_value` lists each linked value.

**Build-check fallbacks:** the Close probability fallback fired (note 9), and with it the widget fallback: DB1.W2 and DB1.W7 sum Deal value. The stale-mirror, form and month-grouping fallbacks did not fire.

## Leak-lint blocks and warnings

- Blocks, id-pattern rule: board payloads (raw query text carrying the workspace, folder and template ids; my mistake, note 7); every lead phone number (not a leak, note 5).
- Blocks, pain-id rule: four reflection payloads whose own note field named element keys (my text, not a leak).
- Blocks, wall rule: a reflection payload note naming a board key (matched another record's name); three sample account names and one sample lead name from the plan; two invented contact surnames and one job title (not leaks in the sense of copied text, but words another client's record holds; changed).
- Warnings, record-number rule: status colour numbers on the Region, Source and Stage columns match numbers in the call transcript (not a leak).
- Warnings, figure rule: many sample deal values, and one account note's wording, sit near cost figures from the discovery call (invented values in the revision's range; not a leak; the note was reworded).

## Refusals by `record.py` or `ledger.py`

None. `record.py check` blocked once, between `bind` and `approval`, while the ledger's account at bind was still unbound; `approval` cleared it. I read the ledger's retry rule before resuming, so `intent --retry` was never refused: it needs the reconcile of note 2. Outside the scripts, the session's permission layer refused the first `create_automation` call (note 4).

## UI steps left for the user

All five are in the ledger, owner the user:

- U1: add a kanban view of Opportunities by stage.
- U2: log two or three calls and visits on sample customers' activity timelines.
- U3: try the CRM's own lead conversion on one sample lead.
- U4: in the Quiet quote alert on Opportunities, change the condition from "is not" to "is" Quoted, and check that the trigger reads 7 days after Last activity.
- U5: when the demo is over, switch off both alerts in monday (the Quiet quote alert, live and departed, and the New lead alert).
- Also worth a look, though not a ledger step: the Leads template's own "Web Form" view, whose login setting the build did not read, and the eight widgets, which can only be checked by eye.
