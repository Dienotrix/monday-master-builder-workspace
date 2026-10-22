# Approval: Bramblewood Signs, store rollout proof of concept

v0.1, revision 1 (frozen, sha256 1b99a48c279bc89422ff51ca67f8f43087fbde1226e9faaff53b38f675e4e6d6). One yes covers everything below.

## 1. Where

- **Account:** your own monday account.
- **Workspace:** Builder Test Workspace, the closed Work Management workspace you named for every build. It is used as it is; nothing in it is created, renamed or changed apart from the new folder.
- **Folder:** a new folder, **Bramblewood – Ops**, inside that workspace. The three boards and the dashboard all go in it.
- Nothing else is touched. The client's own monday account (their job list, the coordinator's install board, the trade-show boards) is not read or written.

## 2. What this build rests on

All of these are assumed. None is written into monday as text.

**Assumptions**

1. One rollout store is one job, with its exterior and interior visits as two installs and its permits as linked rows. *If accounting picks one job number for the whole contract:* the installs and permits stay as they are and only the job rows regroup.
2. A permit lasts a number of days from its approval date, typed per permit. Its end date is typed into a real date column so the expiry alert can fire from it, and a formula shows the calculated date beside it as a check. *If the days are later kept per city:* the permit rows and the alert stay.
3. An install books one crew for a morning, an afternoon or a full day. A double booking is the same crew in the same part of the same day. *If the rule turns out different:* only the flag's meaning changes; the rows stay.
4. A survey books a crew like an install, as a visit with no job. *If surveys live somewhere else:* those rows move and the week view stays.
5. Hold is a stage of its own, with a reason (landlord, permit or deposit) that the production manager sets and clears. *More reasons* are just more choices.
6. Whoever receives the customer's approval records the approved revision and attaches the approval email to the job. The printed revision is noted when the job folder is printed. *If the forwarding carries on:* the fields stay and only who fills them changes.
7. Crews read their week in the mobile app, each crew lead on his own seat. *Until then:* the "install moved" alert goes to you, and the printout and the texts carry on.
8. The boards match what the spreadsheet holds today and no more. *Anything the working session adds* is new columns, not a rebuild.
9. Finished jobs stay on the jobs board in an Installed group with the date they were installed, instead of being deleted.

**Assumed terms:** each automation's trigger, condition and action (the table in section 5). *If one changes:* that automation is deleted and made again, and nothing else changes.

**Forks, built on the way the conversation leaned**

1. Permits get their own board, linked to the job and shown on it. *If the client wants them as cells on the job:* the permit columns move onto Jobs, which loses "any number of permits per job".
2. Installs get their own board linked to the job, with weeks as groups, which keeps the shape of the coordinator's prototype. *If they become rows under the job:* the week view and the phone view have to be rebuilt.
3. There is one job per rollout store until accounting answers.
4. A double booking is shown, not stopped. The coordinator sets the flag from the crew-sorted week view, and a flag that sets itself is deferred. *Warn or stop* is decided during implementation.
5. The phone view is the live schedule. Any printout is printed from the board.
6. A newly approved revision marks the job folder for reprint.
7. Installed jobs stay on the board.

**Not built in this version:** the second shop, quoting and invoicing, the accounting link, a crew follow-up for finished signs on the rack, which of the spreadsheet or the board is keyed first, and the four automated helpers from the readiness check (permit and booking checks that run by themselves, reading the approval email, and the Monday summary).

## 3. The boards

**Jobs**: one row per sold job; a rollout store is one job.
- Job number (text, typed by hand as today), Customer (text), Sign type (Channel letters, Pylon, Monument, Interior).
- Stage (status): Proofing, Permit, Fabrication, Ready, Scheduled, On hold, and Installed, which is the done label.
- Hold reason (Landlord, Permit, Deposit).
- Approved revision (number) and Approval email (file).
- Printed revision (number) and Traveller (status: Current or Reprint needed).
- Installs and Permits: two-way links to the other boards.
- Last install: the latest install date. Permit states: each linked permit's status. First permit end: the earliest permit end date.
- Permit check (formula): reads "A permit ends before the last install" when that is true.
- Installed on (date) and Notes (long text, which never reaches the crews' board).
- Groups: Rollout stores, Other jobs, Installed.

**Installs**: one row per crew visit (one crew, one site, one day or part of a day). A survey is a visit with no job.
- Job: the two-way link back to Jobs. Job number is mirrored from the job.
- Crew (Crew A, B, C), Install date, Part of day (Morning, Afternoon, Full day), Visit (Exterior, Interior, Survey).
- Site address, On the truck, and Meeting on site (a role, never a name).
- Visit status: Booked, Confirmed, and Done as the done label.
- Booking check: Clear, or Crew booked twice.
- Groups: Week of 19 Oct, Week of 26 Oct, Week of 2 Nov, Week of 9 Nov, Done.

**Permits**: one row per permit, any number per job.
- Job: the two-way link back to Jobs.
- City, Permit type (Sign, Electrical).
- Permit status: Not filed, Filed, Approved as the done label, Denied, Expired.
- Filed on, Approved on, Days valid.
- End date: a real date column, typed. Calculated end: a formula giving the approval date plus the days valid.
- Groups: Open permits, Closed permits.

## 4. Views, forms and the dashboard

- **Jobs:** "Held up and why" (on hold, sorted by reason) and "Installed history" (installed, newest first).
- **Installs:** "This week by crew" (this week, sorted by crew, then day, then part of day, so a double booking sits on two neighbouring rows) and "Crew phone view" (not done, by date, showing only job, job number, crew, date, part of day, address, truck and who they're meeting).
- **Permits:** "Waiting on the city" (filed, by filed date) and "Approved by end date" (approved, soonest end first).
- **Forms:** none. Everyone who enters data works on the boards, and the crews only read.
- **Dashboard "Ops overview"** in the folder, with five widgets:
  - Jobs by stage (chart)
  - Jobs by hold reason (chart)
  - Install calendar
  - Permits by status (battery)
  - Installs by crew (chart)

## 5. Automations

| board | trigger | action | recipients |
|---|---|---|---|
| Permits | 14 days before End date, at 07:00, if status is Approved | notify with the permit's name and its end date | you only |
| Installs | Install date changes | notify with the install's name, new date and crew | you only (standing in for the crew lead) |
| Jobs | Approved revision changes | set Traveller to Reprint needed | nobody |
| Jobs | Stage changes to Installed | set Installed on to today | nobody |
| Jobs | Stage changes to Installed | move to the Installed group | nobody |
| Installs | Visit status changes to Done | move to the Done group | nobody |

The automations are built last, after the sample rows, so creating the rows sets none of them off.

## 6. Sample data

There are 96 invented rows, each batch at most 20:

- **30 jobs:** 12 rollout stores, 13 other jobs and 5 installed.
- **40 installs**, including 3 surveys.
- **26 permits** across five invented cities.

Dates run from 5 October to 13 November, around this week. Past visits are already Done, and no open row is overdue except the ones planted to show an alert:

- one crew booked twice on the morning of Tue 27 Oct, flagged
- one permit that ends before its job's last install, so the permit check shows
- one approved permit whose two-week alert fires on 26 Oct
- one job whose traveller needs a reprint
- five jobs on hold with their reasons

Customers are descriptive ("Grocery rollout – Store 01", "Dental clinic"). Meeting contacts are roles. There are no prices, no client names and no real people.

## 7. Hard to undo

- **The folder**, and the three boards and dashboard inside it. Removing them means archiving by hand.
- **The six automations.** Automations made through the API cannot be switched off through the API. A wrong one is deleted and made again, never patched with a second.
- **The two two-way links.** Each one adds a linked column on both boards at once.

## 8. Left for you in monday

1. Add a calendar view of Installs by install date. A calendar view can't be created through the API.
2. Switch off the six automations by hand when the demonstration is over.

## 9. Leak check

Clean: no blocks and no warnings on revision 1.

Two things are checked at build time and reported if they fail:
- The permit check is a formula over two date mirrors, which hasn't been proved yet. If it doesn't evaluate, it is dropped and the job shows the last-install and first-permit-end values side by side instead.
- The expiry alert is shown as working only after the date-column probe passes.

The week groups are dated for a build this week or next. A later build needs a new revision.

---

**Approve v0.1 revision 1 as shown?**
