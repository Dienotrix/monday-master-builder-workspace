Industrial supplies distributor, Toledo: sales pipeline and forecast, v0.1 revision 1 (frozen, sha256 8779e1bb608cc99e52aa303857a861320f5e5c6b975d9b74a0846bb4845666b7). One yes covers everything below.

**1. Where**

Your own monday account, bound and its plan tier read at the start of the build, before anything is written. The workspace is CRM Test Workspace, the closed CRM workspace you named for CRM demos. It is used as it stands and not changed. Inside it the build makes one new folder, "Industrial supplies distributor, Toledo – CRM", and everything goes in that folder. Nothing else in the account is touched.

**2. What this build rests on (all assumed until the client confirms)**

- *Assumed:* the company's name was not given, so the folder carries a descriptive name. A later name is a rename, and nothing else changes.
- *Assumed:* a quote moves through Prospect, Quoted, Verbal, Won (done) and Lost. If the client uses other stages, the labels are renamed and the rows are kept. Stages added or removed later mean the sample rows and the forecast's likelihoods need another look.
- *Assumed:* a stocking agreement or blanket order is a "Quote type", not a board of its own. If it later needs its own term or review date, columns can be added. A board of its own would mean moving rows.
- *Assumed:* Region is a status on leads, accounts and opportunities, with three placeholder labels (West, North, East), and each regional manager follows one region. The real names are a label rename. If region turns out to follow the rep and not the customer, the column stays but who sets it changes.
- *Assumed:* the business system's quote number is typed in by hand, and nothing connects to it in this build. A later connection would fill the same column.
- *Assumed:* the forecast is value times stage likelihood, from the CRM's own Close probability and Forecast value columns, over close dates in the next three months. A different rule for verbals or stocking agreements changes the likelihoods, not the boards.
- *Assumed:* inside sales use the same boards and log calls the same way.
- *Assumed:* the build is four of the CRM's own boards (Leads, Contacts, Accounts, Opportunities) and one overview. This replaces the five boards the readiness check assumed, because the CRM's Sales Activities board cannot be linked when it is installed on its own. Calls and visits go on each record's activity timeline instead, and a hand-set "Last visit" date on the account drives the coverage list. A visits board in a later version would keep everything built here.
- *Assumed:* "Last activity" on a quote and "Last visit" on an account are set by hand by whoever logs the contact.
- *Assumed term (from the readiness check's own assumption):* a Quoted deal with no logged activity for seven days raises an alert, which only you hear, at 8:00. The client never gave the seven days, and the owner and manager recipients it assumed are not built, because people are you alone until the test-people list arrives. A different number of days is a change made in monday, where the automation also has to be switched off and rebuilt (see 7).
- *Assumed term (from the readiness check's own assumption):* each new lead raises an alert, which only you hear, with its name and region. The client never gave the readiness check's routing of each website enquiry to a person by region, so that part is not built: there is no website connection and no one else to route to.
- *Fork on its leaning:* a prospect starts as a lead and becomes one account, one contact and one opportunity at the first quote. If conversion moves to the first order, the boards stay the same and only the moment changes.
- *Fork on its leaning:* a requote stays on the same opportunity with a new quote number, and earlier numbers go in its updates. If each number needs its own value and status, a quote board would be added and the opportunities would stay.

**3. The boards** (each installed from the CRM's own template, its sample rows archived first)

- **Leads:** one row is a company or person not yet quoted. It keeps the CRM's Status, Email, Company, Phone and Owner columns. It adds links to Contacts and Accounts (filled when a lead converts), Region, Source (Website form, Trade show, Phone or email, Rep prospecting), Next step (a few words) and Next step date. Groups are as the CRM installs them.
- **Contacts:** one row is a buyer or manager. It keeps the CRM's contact columns and carries the other side of the Leads, Opportunities and Account links. Groups are as installed.
- **Accounts:** one row is a customer company. It keeps the CRM's account columns. It adds links to Leads, Contacts and Opportunities, Region, Account owner (you, or empty for a house account), Last visit (a date), Account notes (buying habits, when to call), and Pipeline value, a mirror that sums the linked opportunities' values. Groups are as installed.
- **Opportunities** (the CRM's deals board, named in the client's word): one row is one deal or quote. It keeps the CRM's Owner, Deal value, Expected close date, Close probability and Forecast value. It adds links to Contacts and Account, Stage (the template's stage relabelled as above), Quote number, Quote type (Quote, Stocking agreement), Region, Next follow-up, Last activity, and Account last visit (the template's stale Account mirror, re-pointed to show the account's latest visit). Groups: Open quotes, then Closed for won and lost. The owner moves a quote to Closed.

All links are two-way.

**4. Views, form and the dashboard**

- Views:
  - Leads, "Next steps": every lead, soonest next step first.
  - Accounts, "Visit coverage": every account, oldest visit first, with owner, region, last visit and pipeline value.
  - Opportunities, "Open pipeline": stage is Prospect, Quoted or Verbal, soonest close first.
  - Opportunities, "Quiet quotes": stage is Quoted, oldest last activity first.
- Form: "New lead" on Leads. It asks for company, contact, email, phone, source, region and next step, and needs a monday login.
- Dashboard: "Sales overview", over Leads, Accounts and Opportunities.

| widget | kind | question it answers |
|---|---|---|
| Quotes by stage | pie chart, opportunities by stage | how many quotes sit at each stage |
| Forecast by close month | column chart, forecast value by expected close month | what is likely to close in each of the next three months |
| Open quotes by owner | column chart, opportunities by owner | who carries what (shows you alone until the test-people list arrives) |
| Pipeline by region and stage | stacked column chart, deal value by region, stacked by stage | how the pipeline splits across regions |
| Leads by source | pie chart, leads by source | where new companies come from |
| Customers by last visit | column chart, accounts by last visit week | who has been visited lately and who has not |
| Forecast value | number, total forecast value | the headline forecast |
| Quote progress | battery, opportunities by stage | how far the pipeline has moved toward won |

**5. Automations**

| board | trigger | action | recipients |
|---|---|---|---|
| Opportunities | seven days after Last activity, at 8:00, when Stage is Quoted | notify with the opportunity's name and its Last activity date | you only |
| Leads | a lead is created | notify with the lead's name and its Region | you only |

**6. Sample data**

87 rows, all invented, none a real customer, person or deal from the call, and nothing from the business system or the workbook. That holds even though the call named customers.

- 20 accounts, in an industrial manufacturing mix across the three regions. Four are house accounts with no owner, and last visits run from late July to this week.
- 20 contacts, one for each account.
- 32 opportunities: 22 open (4 Prospect, 12 Quoted, 6 Verbal) and 10 closed (6 Won, 4 Lost). Six are stocking agreements. They close from late October to late January, and no open row is past its follow-up.
- 15 unconverted leads across the four sources.

Dates sit around this week. The planted case is one Quoted stocking agreement with its last activity on 19 October. The quiet-quote alert fires on it at 8:00 on Monday 26 October, and it sits first in "Quiet quotes". A build that starts after 25 October needs a new revision.

**7. Hard to undo**

- The new folder.
- The four boards installed from the CRM's templates. The build cannot archive or remove them, and a column added to one cannot be removed again.
- The two automations. Once made through the API, they cannot be switched off through the API, only in monday.

**8. Left for you in monday**

- Add a kanban view of Opportunities by stage.
- Before the showing, log two or three calls and visits on sample accounts' activity timelines, so the timeline is seen working.
- Try the CRM's own lead conversion on one sample lead. If the installed board offers none, show it by linking the lead to its account and contact.

**9. Build checks (unproved, with their fallbacks)**

- Relabelling the template's stage may not carry through its Close probability and Forecast value formulas. The build reads one row after relabelling. If they don't follow, the forecast chart and the forecast number use Deal value instead, and the forecast item is reported as not yet built.
- Widgets over a formula column (forecast by month, forecast value) are unproved. The fallback is Deal value. If the chart offers only weeks, it groups by week.
- The template may carry no empty relation from Opportunities to Accounts. If so, the build makes a new two-way link of the same name. Template relations the plan does not link stay as installed and are kept out of the views.
- Re-pointing the stale Account mirror is unproved. If it fails, the mirror is left as installed, renamed "Account last visit", and kept out of the views.
- A form on an installed Leads board is unproved. If it fails, adding the form becomes a step for you in monday.

**10. Lint warnings**

None. The leak check was clean and the record check reported no blocks and no warnings.

Yes to build this as written?
