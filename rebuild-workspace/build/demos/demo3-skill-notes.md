# solution-blueprint skill: notes from demo 3

## Result

- Revision: v0.1 revision 1, frozen as `blueprint-r1.md`, frozen sha256 `8779e1bb608cc99e52aa303857a861320f5e5c6b975d9b74a0846bb4845666b7`. The working and frozen sha are the same.
- Element-key table: 58 rows, of which 55 count toward `element_count` (3 are UI steps). The table parses cleanly with the ledger's own `element_table`, `element_recipients` and `element_templates` (read-only import, no write).
  - workspace 1 (W1, referenced)
  - folder 1
  - boards 4, all native installs: `5678953932 leads`, `5678953938 contacts`, `5678953942 accounts`, `5678953956 opportunities_or_deals` (named Opportunities)
  - columns 26
  - groups 2
  - views 4
  - form 1
  - dashboard 1 with 8 widgets
  - automations 2 (both notify the user only)
  - item batches 5
  - UI steps 3
- Sample rows: 87, all invented, in 5 batches: accounts 20, contacts 20, opportunities 20 + 12, leads 15. One planted case: a quiet quote that fires the alert on Monday 2026-10-26.
- Leak lint (`blueprint`):
  - first run: blocked, 6 wall blocks
  - after rewording: clean, with 0 blocks, 0 warnings and 0 cautions, both before and after the freeze
- `record.py check`: no blocks, no warnings, before the freeze and after the STRAND.md update.
- Record writes, all through the guard:
  - `version open`
  - the blueprint, written twice
  - `version.md`, with revision 1 and the Scope sentence
  - the freeze, which logged itself
  - `STRAND.md`, with stage `blueprint` and next_step set to the card
- `.work/staging/` deleted. No `__pycache__` anywhere under the home. No monday call.

## Notes, most important first

1. **Visit coverage once Sales Activities is left out** (Native installs, A38, "Leave Sales Activities out (G-159)"; Design rules 1 and 12).
   - What happened: the readiness check answers its visit-coverage pain with the Sales Activities board ("a sortable table view of visits by rep over ninety days"). Its native-reuse line and its board-architecture assumption also name five boards. The skill drops that board and sends activities to "the CRM's own activity timeline or wait for a later version". The timeline is not a sortable list across accounts, cannot be charted, and has no element kind in the ledger, so it cannot carry sample rows or a planned case. The skill gives no replacement for the coverage list.
   - What I did: a hand-set "Last visit" date on Accounts, a "Visit coverage" table view sorted by it, a dashboard chart of accounts by last-visit week, and a mirror of it on Opportunities. The trace reads "partly". I recorded the board-architecture assumption as revised from five boards to four (AS8), and made logging a few timeline entries a UI step.
   - What the skill should say: when the readiness check leans on Sales Activities, plan coverage as a date column on Accounts (trace "partly", set by hand, an assumption) and revise the readiness check's board-architecture assumption on the card. Timeline entries are a UI step, not sample rows, until the ledger has a kind for them.

2. **The v2 template's own inventory is missing** (Native installs, first bullet; Writing the blueprint, "Name every row exactly as it will be built").
   - What happened: `native-objects.md` gives reserved column ids and thresholds, not the v2 templates' column titles, groups, status labels, form views, or which relations arrive empty. Three gaps followed.
     - The skill lists "Deals to Contacts and to Accounts" as relations the template leaves empty, but `native-objects.md` 2.3 and 2.4 say v2 `deal_account` is a mirror, the stale one the skill itself mentions. So it is unclear whether v2 Opportunities has any empty relation to Accounts.
     - The templates also carry counterpart relations (`contact_account`, `contact_deal`, `account_deal`). Nothing says whether linking one side reuses them as the reflection or leaves them empty beside the new "link to …" column G-158 describes. A board could end up with two columns of the same name.
     - Template groups and stage labels are unknown, so rule 6 ("a new board's default group becomes the first planned group") does not map onto a template with several groups.
   - What I did:
     - Opportunities to Accounts: planned as a column row with a build check (link the template's empty relation if there is one, else create a new two-way connect column of the same name).
     - Unplanned template relations: left as installed and kept out of the views.
     - Opportunities groups: the template's first group is renamed Open quotes. Its second is renamed Closed, or created if there is none, and further template groups are left empty, since `delete_*` stays blocked on natives.
     - Leads, Contacts and Accounts: their groups and Lead status labels are kept as installed.
     - Template columns kept as installed: described in section 11 by role, not given element rows.
   - What the skill (or `native-objects.md` 3) should say: a short v2 inventory per template (column titles and types, groups, status labels, which relations arrive empty and which pair with each other). Also a rule for template groups and for template relations the plan leaves alone.

3. **The two invented specifics** (Design rule 9; Writing the blueprint, section 16 assumed terms).
   - What happened: both specifics the grader flagged are in the readiness check's own Assumptions list as `[kind: automation-condition; state: assumed]`, each with a question. So the brief's condition (the readiness check marks them as assumptions the card can carry) holds. Each carries more than the build can do:
     - the seven-day flag notifies "its owner, and its manager after fourteen";
     - the enquiry automation creates a lead from the website and assigns it by region.
   - What I did: kept the triggers marked assumed (AT1, AT2). Cut the owner and manager recipients (rule 9, notify the user only; rule 10, no other people). Cut the website creation and the routing by region (no web connection, no people). The card says the client never gave either.
   - What the skill should say: an automation-condition assumption in the readiness check that the call never stated goes on the card as assumed, with the words "not from the call". Recipients beyond the user, and assignment to people, collapse to the user alone, and the card names what was cut.

4. **Hard to undo misses the installed natives** (The approval card, item 7).
   - What happened: item 7 lists the folder, a workspace and the automations. The record map says an installed native takes "no update, archive or convert". `native-objects.md` 6.3 says "a column added to a native cannot be removed again". So the four installed boards and their added columns cannot be undone by the build either.
   - What I did: listed the four boards and the columns added to them under item 7 of the card and under irreversible operations in section 15.
   - What the skill should say: add "each native install, and every column added to it" to item 7 and to section 15.

5. **The guard will ask at every native create** (Native installs; `native-objects.md` 6.3 R-H).
   - What happened: R-H asks on any `create_board` whose name matches a native default name. Leads, Contacts, Accounts and Opportunities all match, so the build will meet four asks the card does not prepare the user for.
   - What I did: nothing in the blueprint. I am noting it here.
   - What the skill should say: whether R-H is meant to fire on a planned native install (A38). If it is, the card should say the four asks will come. If it is not, R-H should skip a row with an approved template cell.

6. **Rule 12 and a Contacts board** (Design rule 12).
   - What happened: "Nothing that would read as … a real person's name" cannot hold on a Contacts board, whose rows are people.
   - What I did: invented first and last names, invented emails at example.com and 555 phone numbers. The card says every row is invented.
   - What the skill should say: contacts take plainly invented names, with an example domain and 555 numbers.

7. **Wall blocks on ordinary words, with no source** (Saving, checking and freezing, step 4).
   - What happened: the first lint run blocked six times on the cross-client wall, on "Central" (four times), "and the CRM's" and "the installed", all with `source: null`. Two of these are everyday phrases, and nothing tells the writer which record or term they came from. That is right for the wall, but makes the fix guesswork.
   - What I did: reworded. The region labels became West, North, East. "and the CRM's own contact columns" became "and the other contact columns the CRM brings". "if the installed board offers none" became "if the board offers none". It ran clean the second time.
   - What the skill should say: a wall block on ordinary words is fixed by rewording the phrase around it, and costs a guard rewrite, not a revision, as long as it runs before the freeze. Pick placeholder labels (regions, sources) that the wall does not hold.

8. **Charts by month, and the headline number on a CRM board** (Design rule 11).
   - What happened: the rule says "a column chart by week from a date column", but the client asks for a monthly forecast over three months. The rule also says "a number widget cannot be limited to a group", so a total of Forecast value includes won rows if the template's likelihood gives Won its full value.
   - What I did: grouped the forecast chart by month, with a build check (week if month is not offered). Kept a total-forecast number and a battery by stage as the headlines, and added a build check that widgets over the template's formula columns fall back to Deal value.
   - What the skill should say: a date axis groups by week or month, whichever the client's question uses. On CRM natives, name the headline totals that stay meaningful when they cannot be limited to a group (counts, or Deal value with a stage chart beside it).

9. **Relabelling the template's stage** (Design rule 6; Native installs, "any further column … as rows of that board").
   - What happened: the readiness check's stages (prospect, quoted, verbal, won, lost) need the template's own stage column relabelled. In v2, Close probability is a formula, probably keyed on those labels, and Forecast value depends on it. The skill says nothing about relabelling a template column that other template columns read.
   - What I did: relabelling is a column row on the native (an update, card class). A build check reads Close probability and Forecast value on one row after the relabel, with Deal value as the fallback.
   - What the skill should say: relabelling a native's status column is a column row with a build check on every template formula that reads it.

10. **Build date and frozen dates** (Design rule 12).
    - What happened: "Dates around the week of the build" assumes a known build date. The blueprint freezes before the user's yes, and a date-triggered planted case needs the build to land before its trigger date.
    - What I did: anchored the sample dates on the week of 2026-10-19 and planted the alert for Monday 2026-10-26 at 8:00. Section 16 and the card say a build that starts after 2026-10-25 needs a new revision.
    - What the skill should say: plant a date-trigger case far enough out that a next-day build still reaches it, and state the last build date on the card.

11. **The A11 sample-data field** (Design rule 12; The approval card, last paragraph).
    - What happened: `CLIENT.md` holds `sample_data_in_account: "unanswered"`. The skill plans sample rows without saying whether that field matters for an own-account proof of concept.
    - What I did: planned the rows, left the field open and did not ask, since "the three A11 decisions stay open".
    - What the skill should say: whether invented sample rows in the user's own account are covered without that answer. I read it as covered.

12. **Naming the referenced workspace in the table** (Where it will be built, second and third bullets).
    - What happened: sections 1 to 15 must not name the test workspace, but "Name every row exactly as it will be built" puts its name in W1's name cell. The blueprint lint does not read name cells, so it passed.
    - What I did: W1 is named "CRM Test Workspace" in the element-key table only.
    - What the skill should say: confirm that W1's name cell is exempt from the wall, or have it written as "referenced" and read live at the build.

13. **The readiness condition and A38** (Before anything, third bullet).
    - What happened: the readiness clearance's condition says "a CRM build needs a workspace in that product with its native boards". A38 says the workspace holds none and the build installs them.
    - What I did: treated A38 as overriding and said so in section 16's build checks.
    - What the skill should say: a readiness condition that A38 supersedes is answered in section 16, not reopened.

14. **The "builder" in sections 1 to 15** (Writing the blueprint, client-readable sections).
    - What happened: with people limited to the user, sections 1 to 15 need a plain word for who hears the alerts. "The user" is internal, and naming the user's firm is forbidden.
    - What I did: wrote "the builder".
    - What the skill should say: give the plain word, for example "the person building the demonstration".

## Lint blocks and warnings

First `leak_lint.py blueprint` run, six blocks, all on the `wall` rule, class `name`, the same text each time ("matches a name of another client record under the home"), `source: null`:

| line (draft) | matched text | in neutral words | real leak |
|---|---|---|---|
| 37 | Central | a placeholder region label in the list of assumptions | no: an ordinary word that also sits in another record's names; reworded to North |
| 131 | Central | the same label in the Leads Region column | no; reworded |
| 140 | and the CRM's | a phrase in the Contacts column table ("and the CRM's own contact columns") | no: an everyday phrase that near-matches another record's name; reworded |
| 153 | Central | the Region column on Accounts | no; reworded |
| 169 | Central | the Region column on Opportunities | no; reworded |
| 238 | the installed | a phrase in the lead-conversion UI step ("if the installed board offers none") | no: an everyday phrase; reworded |

Second and later runs: clean, with 0 blocks, 0 warnings and 0 cautions. `record.py check`: no blocks and no warnings on every run.
