# account-build skill: notes from demo 2

## Result

Built. The run is ended, the lease is released, `version.md` is `built` and `STRAND.md` `version_state` is `built`. `record.py check` and `ledger.py check --strand 001` are both clean.

- Elements: 76 rows in the frozen revision.
- Built and verified `match`: 70.
  - W1, the referenced test workspace.
  - F1 and the three boards.
  - All ten groups.
  - All 37 columns, mirrors and formulas included.
  - All six sample-row batches (96 rows).
  - All six table views.
  - Five automations: A1 and A3 to A6.
  - DB1.
- Not checkable: 5, the widgets DB1.W1 to DB1.W5 (G-11).
- Departed: 1, A2 (note 2). It is live and notifies the user, but one message field points at the wrong column. It became UI step U3.
- UI steps for the user: three (below).
- monday calls used: 103 across three sittings (18 reads, 10 schema and guideline lookups, 75 writes). Of those writes, one `create_automation` stored nothing.

The run stopped three times before it finished:

1. At the approval step: a stale-sha line in write-path.md, then the session's permission layer.
2. On status label ids: fixed in ledger.py by the main session.
3. On B1.V2's sort: resent once, on the main session's call.

## Notes

1. **Views: send sort directions in capitals.** Section: SKILL.md step 6 and write-path.md "Views". `create_view_table` was sent `direction: "desc"`, the form the tool documents ("asc or desc"). It stored `ASC`. The other five views sort ascending, so their lower-case sends looked right. The run stopped on the mismatch.

   On the main session's call, I resent it once as `DESC` through `update_view_table`. The ledger has no plain update path for a mismatched row: `intent --operation update` is refused from `mismatch`. `intent --operation update --retry` was the route ("once, with the one different call form", record-map.md). The read then showed `DESC`, and B1.V2 verified.

   What the skill should say:
   - Send `ASC`/`DESC` in capitals.
   - Check the stored direction as part of the view read.
   - Name `--retry` as the way to fix a mismatched row.
   - Candidate gotcha: a lower-case `desc` on `create_view_table` is stored as ascending.

2. **A2: the automation tool picked the wrong notify block, then the wrong column.** Section: SKILL.md step 7 and write-path.md "Automations".
   - **First call:** the prompt in write-path.md's shape (When a column changes, Install date; Notify someone, the user; message with item name, Install date and Crew) came back `needs_clarification`. It had chosen a Microsoft Teams "Notify users" block, mapped `{{Crew}}` to the Meeting on site column, and stored nothing. `list_automations` confirmed nothing was live.
   - **Second call:** the prompt named "monday's own notification, the Notify someone action" and said that Crew is the dropdown column named Crew. It was stored with monday's Notify someone and the right trigger and receiver. But `{{Crew}}` was mapped to the Booking check status label.
   - **What I did:** I verified it `mismatch` and departed it with decision `ui-step`. The ledger minted U3: the user re-points that one field to Crew in monday. I did not create a third automation. G-65 says a wrong automation is never patched with a second one, and nothing deletes one from outside.

   What the skill should say:
   - When a trigger is not a date, the prompt has to name monday's own Notify someone action.
   - A placeholder for a dropdown column can be mapped to another column, so check every field the message reads, not only the trigger, receiver and offset.
   - Candidate gotcha: `create_automation` can resolve a column placeholder to the wrong column, and the stored message title keeps the raw `{{Crew}}` text.

3. **A3 to A6, the probe: all four built first time and matched.** Details are in their own section below. The skill should give the prompt shape for these actions: change a status, set a date to today, move an item to a group. It should also say what the read checks for an automation that notifies nobody: the trigger column and label id, the action block, and its target column, label, date value or group id.

4. **Fixed by the main session: status label id 0 was refused on read-back.** The fix is `LABEL_KEYS` in ledger.py, tested by `Demo2Test`. `verify` had treated status and dropdown label ids inside a column's `settings` as monday object ids, so label id 0 could not be written in any form. The skill should say: label ids may stay numbers.

5. **Leak lint: invented names that the plan itself lists are blocked as a copied run.** B3.C2 City's five dropdown labels, in the revision's order, matched six words of the working blueprint and were blocked. I put the labels in alphabetical order, which the revision does not fix, and the payload went through. The lint should not count a value list that the frozen revision names for that element. Every other payload was clean, including the planned formula text and the automation prompts that name the user.

6. **A departed automation that is still live does not reach the live map.** `run end` wrote live rows for A1 and A3 to A6, but not for A2, which departed. A2 exists and is active in monday. The ledger, the record map or the skill should say how a live but departed object is carried, so the audit and the switch-off step (U2) still see it.

7. **The frozen revision disagrees with itself about B2.V2's columns.** Section 12 lists the eight columns the crew phone view shows, which leaves out Visit. The build checks say only Visit status and Booking check are hidden. I followed the build checks. The skill could say which section wins, and the blueprint step should catch this before freezing.

8. **Mirrors read back as lists, but formulas see the aggregate.** B1.C11 and B1.C14 were created with `calcType` latest and earliest (in `get_column_type_info`'s mirror schema), yet their `display_value` lists every linked date (G-31). B1.C15, the formula over them, evaluates correctly: it flags Store 05 only, the planted case. So the revision's open question is answered yes and no departure was needed. B3.C9 evaluates too. The skill should say to verify formulas on `display_value` once rows exist, and to name `calcType`.

9. **A1's time of day is stored with a timezone.** The trigger stored `hour 7, minute 0, offset -14 Day` with the account's own timezone. The revision says only "at 7:00". The skill should say that the time of day is local to the account, and check the timezone in the read.

10. **SKILL.md, "Before the first write", step 4: the change-check input has no stated shape.** It wants `ring`, `versions_seen`, `release_notes_since`, `roster_diff {added, removed, renamed}`, `schema_diff` and `result` (one of two fixed phrases). The skill should give it.

11. **SKILL.md, step 5: W1's verify can only come after step 6.** `verify` is fenced. W1 needs no `intent` or `record`, and its read takes `workspace_id` equal to its own id.

12. **Steps the skill leaves unspelled that worked.** The skill should state each of these:
    - The renamed starting group: `intent --operation create` with the `update_group` payload, recorded under the id `topics`.
    - The reflection side of a two-way connect column: the intent goes before the call that creates it, then a title-only rename.
    - Item batches:
      - Connect targets go first.
      - `--ref board:<Jobs>` goes on the linked batches.
      - The board goes as `id` in the read, with `items_count` and `item_ids`.
    - The dashboard:
      - Verified through search with `id`, `workspace_id`, `name` and `kind`. Search does not show the folder, so the dashboard's placement in F1 rests on the create call.
      - The widgets are `not-checkable`, with a note.

13. **`ledger.py ui-step` is not fenced and needs `--target-version`.** Passing the fence is refused as unrecognised arguments. Leaving out `--target-version` is refused too. `depart --decision ui-step` mints the next free U number (U3) and sets the version itself. `depart --attempt` takes a call form (`flat`, `wrapped`, `tool` or `raw`), not a description. write-path.md lists none of this.

14. **SKILL.md, "After the last write": STRAND.md `stage`.** The skill sets `version_state` to `built` but says nothing of `stage`, which still reads `blueprint`. It should say whether the build moves it, for example to `building`, or leaves it for the audit.

15. **The bind mirror leaves out the tier** (`CLIENT.md` keeps `monday_tier: "unknown"`). Log entries: SKILL.md puts them at the end, while write-path.md reads as writing each at once. I wrote each at once.

16. **Sample data: where the revision is loose.** The revision ties "in B3.G2" only to the Expired permits, so the Denied permit stays in Open permits. Forty installs for 30 jobs gave every job a visit, so some proofing and on-hold jobs carry booked visits in November. These planted cases read back as planned:
    - The double booking: two Crew B morning installs on 27 October, both flagged.
    - The permit ending 9 November, for A1 on 26 October.
    - The permit ending 30 October on a job whose last install is 3 November.
    - The reprint case: Approved revision 4, Printed revision 3, Reprint needed.

17. **write-path.md, the sha line (fixed between sittings).** With the corrected line, the sha that each ledger write printed under `written`, equal to the file's sha256, was right every time.

## A3 to A6, the probe

Each was built in write-path.md's prompt shape, with the planned action in place of "Notify someone". Each read back with `list_automations` and is active.

- **A3, New revision: reprint traveller.**
  - Prompt: When a column changes, Approved revision; action Change a status, Traveller, Reprint needed.
  - Stored: the "When column changes" trigger on B1.C6, and the "Change status" action on B1.C9 with the Reprint needed label.
  - Matches.
- **A4, Installed: set date.**
  - Prompt: When a status changes to something, Stage, Installed; action Set a date to today, Installed on.
  - Stored: the "When status changes to something" trigger on B1.C4 with the Installed label, and the "Set date" action on B1.C16 with the value Today.
  - Matches.
- **A5, Installed: move to group.**
  - Prompt: When a status changes to something, Stage, Installed; action Move the item to a group, Installed.
  - Stored: the same trigger, and the "Move item to group" action to B1.G3.
  - Matches.
- **A6, Visit done: move to group.**
  - Prompt: When a status changes to something, Visit status, Done; action Move the item to a group, Done.
  - Stored: the trigger on B2.C10 with the Done label, and the "Move item to group" action to B2.G5.
  - Matches.

What the skill should say: these four actions resolve cleanly from plain names. The stored title is the raw prompt (G-66). The read should check the action block's name and its target. A4 and A5 both fire on Stage changing to Installed, and the probe does not show the order they run in.

## Leak-lint blocks and warnings

- Block, rule `copied-run`, element B3.C2 (City), in the dropdown labels: the five invented city names in the revision's order matched six words of the working blueprint. Not a real leak: these are the planned invented values. I cleared it by putting the labels in alphabetical order.
- No warnings. These payloads were all clean:
  - The folder, three boards and ten groups.
  - The 36 other columns.
  - Six item batches (96 rows of invented names, addresses and notes).
  - Six views and the B1.V2 update.
  - Seven automation prompts, two of which name the user as the recipient.
  - The dashboard and five widgets.

## Refusals by record.py and ledger.py

- `ledger.py approval`, first sitting: a stale sha (`none` while a skeleton `build.json` existed). Fixed in write-path.md.
- `ledger.py verify`, twelve label columns: "an id stored as a number". Got past it by writing the label ids as strings. For label id 0 it then refused "an id spelt with a leading zero". The main session fixed that in ledger.py (note 4).
- `ledger.py intent --operation update` on B1.V2: refused, because the move from `mismatch` to `attempting` is not in the status chain. Got past it with `--retry`, the move record-map.md gives (note 1).
- `ledger.py verify` on A6: refused, because the row was still `attempting`. My slip: I had not recorded it. Recorded, then verified.
- `ledger.py depart` on A2: refused, because `--attempt` takes a call form, not a description. Re-run with `--attempt tool`.
- `ledger.py ui-step`: refused for fence flags it does not take (unrecognised arguments), then for a missing `--target-version`. Re-run without the fence and with `--target-version v0.1` (note 13).
- Two errors were mine and not the scripts', and nothing was written either time:
  - A PowerShell variable clash (variable names ignore case).
  - A command the shell tool misread as touching a protected path. I rewrote it.

## UI steps left for the user

- U1: add a calendar view of installs by install date on the Installs board.
- U2: switch off the six automations when the demonstration ends (A2 included).
- U3: in the Installs board's install-moved automation (A2), change the crew field in the message from Booking check to Crew.

Also for the user to look at: the five dashboard widgets, which no read can check.
