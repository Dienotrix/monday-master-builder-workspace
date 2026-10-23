# Approval card: sales pipeline v0.2, the AI layer (revision 1)

Industrial supplies distributor, Toledo. Version v0.2 of the sales pipeline, revision 1, frozen (sha256 starts `390dcc7e`). It adds monday's AI to what v0.1 built: four AI pieces and nothing else. One yes covers the whole card.

*Changed at the user's word on 2026-10-23 (A42): the build no longer takes the AI off the AI columns when the demonstration is over, since the user deletes the demonstration's boards. This supersedes that one sentence of the frozen revision (sections 15 and 16); no new revision is made.*

## 1. Where

- **Account:** your own account, the one v0.1 was built in. It is checked again at the start of the build, before anything is written.
- **Workspace:** the CRM test workspace you named for demonstrations, used as it stands.
- **Folder:** "Industrial supplies distributor, Toledo – CRM", the folder v0.1 made. Everything this version makes goes into it.
- **Nothing else is touched.** No new board and no install. No column, view, group, form, alert or dashboard that v0.1 built is changed. What is added: seven columns on three boards, fourteen sample rows, one doc, one workflow, and one AI agent. The agent belongs to the account, so its reach is set by hand: it reads the Opportunities board and writes only in the new doc.

## 2. What this build rests on

Everything below is assumed until the client confirms it. v0.1's assumptions and its two forks still stand, and this version builds no new fork.

1. **Visits go in a visit log (assumed).** Each visit or call is written as one short dated sentence in a new Visit log column on the customer, beside the CRM activity timeline. monday's AI cannot read the timeline, so a visit logged only there never reaches the summary. *If this changes later:* if visits move to a board of their own, the Visit summary column stays and its source changes; the log lines already written stay.
2. **Product lines (assumed).** Enquiries are sorted into the five lines the sales leader listed on the call (fasteners, abrasives, cutting tools, safety, general MRO consumables), plus "Several lines" and "Unclear". *If this changes later:* the labels are relabelled and the instructions rewritten in a new revision. Rows already sorted keep their label until their Enquiry text changes.
3. **The region rule is a stand-in (assumed, ours).** The suggested region follows the place an enquiry names: West for Indiana, Illinois and further west; North for Michigan and further north; East for Ohio, Pennsylvania and further east. This is a placeholder like v0.1's West, North and East labels. *If this changes later:* the real regions replace the labels and the rule. The hand-set Region column stays the team's own choice throughout.
4. **When a follow-up is drafted (assumed term, not from the call).** The trigger is the morning a quoted deal's Next follow-up date arrives, at 8:00 in the account's time zone, and only when Stage is Quoted. The workflow drafts the step, sets the deal's Follow-up check to Waiting and notifies you. The owner confirms by setting the check to Confirmed, or to Not needed. Owner and manager notices are cut: only you hear. *If this changes later:* a published workflow cannot be edited by the build. A different trigger or recipient means switching this one off in monday and publishing a new one. The two columns stay.
5. **What the monthly note holds (assumed term, not from the call).** The note is drafted on the first day of each month at 7:00. It covers open quotes (Prospect, Quoted, Verbal) expected to close in the next ninety days, given as totals of Deal value by month, stage, region and owner, with the five largest quotes and the Quoted deals that have had no contact for more than seven days (v0.1's quiet-quote term). It uses Deal value, not likelihood, because v0.1's build found that the CRM's Close probability does not follow the relabelled stages. *If this changes later:* the job's instructions are rewritten in a new revision; the notes already written stay in the doc.
6. **The note goes into a doc and nobody is sent anything (assumed, ours).** The helper writes the note into a new Forecast notes doc in the folder. The sales leader reads it there and sends it on in their own words; the helper sends nothing. *If this changes later:* the doc and its notes stay.

## 3. The boards

No new board. Groups are unchanged on every board; new sample rows go into each board's first group, beside v0.1's.

- **Leads** (one row is a company or person not yet quoted). Three new columns:
  - **Enquiry** (long text): what the enquiry asks for, in the enquirer's own words, including where they are.
  - **Product line** (status, filled by AI): one of Fasteners, Abrasives, Cutting tools, Safety, MRO consumables, Several lines or Unclear.
  - **Suggested region** (status, filled by AI): one of West, North, East or Unclear. The existing Region column stays set by hand.
- **Accounts** (one row is a customer company). Two new columns:
  - **Visit log** (long text): one dated sentence per visit or call, saying when, who went and what was said.
  - **Visit summary** (long text, filled by AI): one line written from the log.
- **Opportunities** (one row is one deal or quote). Two new columns:
  - **Drafted next step** (long text): written by the workflow.
  - **Follow-up check** (status): Waiting, Confirmed (marked done) or Not needed. The workflow sets Waiting; the owner sets the rest.
- **Contacts:** nothing new.
- **New doc, Forecast notes,** in the folder: one heading and the line "A forecast note is added here on the first day of each month." The helper adds each month's note under a dated heading.

## 4. Views, forms and the dashboard

- **Views:** none new. The new columns show on each board's main table. Whether the Visit coverage view also shows Visit summary is checked by eye; the view is not changed.
- **Forms:** none new. The New lead form is unchanged; adding the Enquiry question to it is left for you (U6), so that an enquiry typed into the form gets sorted too.
- **Dashboard:** the Sales overview is unchanged, with its eight widgets as built. A chart of new enquiries by product line or region is deferred.

## 5. Automations and the AI layer

| board | trigger | action | recipients |
|---|---|---|---|
| Opportunities | Next follow-up date arrives, 8:00 account time, only when Stage is Quoted (new: the workflow below) | draft the next step with AI, write it into Drafted next step, set Follow-up check to Waiting, notify | you only |
| Opportunities | seven days after Last activity, 8:00 (v0.1's Quiet quote alert, unchanged; its condition is still yours to fix, U4) | notify | you only |
| Leads | a lead is created (v0.1's New lead alert, unchanged) | notify with the lead's name and Region | you only; it fires once for each of the eight new sample enquiries |

These elements are AI-powered and use the account's AI: the three AI columns, the workflow's AI step and the agent.

### AI columns

**Product line**, on Leads.
- What it fills: a category, as a status column.
- Source: the Enquiry column.
- Existing rows: the backfill is left on, but v0.1's 15 sample leads have no Enquiry text, so they stay empty. The eight new enquiries are sorted as they are added.

Instructions:

```text
Sort the enquiry by the product line it asks about.
Fasteners: bolts, nuts, screws, washers, anchors, threaded rod.
Abrasives: grinding wheels, cut-off wheels, flap discs, sanding discs and belts.
Cutting tools: drills, end mills, taps, saw blades, inserts.
Safety: gloves, safety glasses, hearing protection, respirators, high-visibility wear.
MRO consumables: tape, lubricants, cleaners, wipes, marking paint and other shop supplies.
Choose Several lines when the enquiry asks about more than one of these lines, and Unclear when it names no product.
```

**Suggested region**, on Leads.
- What it fills: a category, as a status column.
- Source: the Enquiry column.
- Existing rows: as for Product line; the 15 existing leads stay empty.

Instructions:

```text
Sort the enquiry by where the customer is, from the town, county or state it names.
West: Indiana, Illinois and anywhere further west.
North: Michigan and anywhere further north.
East: Ohio, Pennsylvania and anywhere further east.
Choose Unclear when the enquiry names no place.
```

**Visit summary**, on Accounts.
- What it fills: a summary, as a long text column.
- Source: the Visit log column. It never reads the activity timeline or the updates thread.
- Existing rows: the backfill is left on, but v0.1's 20 sample customers have no visit log, so they stay empty until someone writes a visit. The six new customers are summarised as they are added.

Instructions:

```text
Summarise the visit log in one line of no more than twenty-five words. Start with the date of the latest visit or call, then what the customer said or asked for, then what was promised next. Use only what the log says, and leave out any price or margin.
```

### Workflow: Quiet quote follow-up draft (on Opportunities)

1. **Trigger:** the Next follow-up date arrives, at 8:00 in the morning, in the account's time zone.
2. **Condition:** only when Stage is Quoted.
3. **AI step (custom prompt):** drafts the next follow-up step from the quote's own columns, with the prompt below.
4. **Change a column:** writes the draft into Drafted next step.
5. **Change a column:** sets Follow-up check to Waiting.
6. **Notify (you only):** "Follow-up drafted for [Name]: [the draft]. Set Follow-up check to Confirmed when it is done."

Nothing follows the owner's Confirmed or Not needed on its own: a workflow built through the API cannot wait for a person.

- **The one test run.** Before publishing, the build runs the draft once on the sample quote "Harborview Metal Works stocking agreement" (Quoted, in Open quotes). That fills its Drafted next step, sets it to Waiting and sends you **one notification**. If that quote's stage has changed since v0.1, another Quoted quote is used and named in the build notes.
- **Published switched on.** From then on it runs on each Quoted deal whose follow-up date arrives. Among v0.1's sample quotes that is up to twelve deals between the build and mid-November, each sending you one notification.

Prompt for the AI step (each bracketed name is that column of the quote):

```text
Draft the next follow-up step on this quote, for its owner to confirm.
Quote: [Name], for [Account], contact [Contacts].
Quote number [Quote number], type [Quote type], deal value [Deal value].
Last logged contact [Last activity]; follow-up due [Next follow-up].
Write one or two sentences the owner can act on today: who to contact, what to ask, and one reason to get in touch now, such as the stock held on the shelf for a stocking agreement. Use only the facts above. Never invent a price, a discount, a date, a product or a person's name, and never write to the customer: this note is for the owner.
```

### Agent: Forecast note helper (account-level, switched on at the end of the build)

- **Job, "Monthly forecast note":** on the first day of each month at 7:00 in the account's time zone, it reads the Opportunities board and writes one dated note in the Forecast notes doc. The first scheduled note falls on 1 November.
- **Reads:** the Opportunities board only. **Writes:** the Forecast notes doc only. Nothing else in the account; no tools, no skills.
- **Two triggers monday adds to every agent:** "When agent is mentioned" and "When agent is assigned". They stay. Its instructions tell it to do nothing but the forecast note.
- **Switched on:** yes, last, after the workflow is published.

Identity:

```text
You are the forecast note helper for the sales team of an industrial supplies distributor.
You work only with the Opportunities board and the Forecast notes doc in this folder, and with nothing else in the account. You read the Opportunities board, and you write only in the Forecast notes doc.
Write plain, short sentences for a sales leader who reads your note and sends it on in their own words.
Use only the values you can read on the Opportunities board. Never invent, estimate or round a figure, a date, a customer or a person; when a value is missing, say so.
Never contact anyone, never send an email or a message, and never write anything outside monday.
If you are asked to do anything other than draft or explain the monthly forecast note, say that you only draft the monthly forecast note.
```

Job, "Monthly forecast note":

```text
Each time this job runs, draft the forecast note and add it to the Forecast notes doc, under a heading with today's date.
Read the Opportunities board. Take the open quotes, those whose Stage is Prospect, Quoted or Verbal, and keep the ones whose Expected close date falls within the next ninety days.
Then write, in this order:
1. The total Deal value of those quotes and how many there are.
2. The total for each of the next three months, by Expected close date.
3. The total for each stage, Prospect, Quoted and Verbal, so the reader can weigh a verbal yes against a quote still out.
4. The total for each Region and for each Owner.
5. The five largest quotes in the window, each with its name, Stage, Deal value and Expected close date.
6. The quotes at Quoted whose Last activity is more than seven days ago, each with its name and Last activity date.
Use Deal value, never Forecast value or Close probability, which do not follow this board's stages yet. Keep the note short, no longer than one page, and add no advice or prediction of your own.
```

## 6. Sample data

Fourteen new rows, all invented in the client's trade. None is a real customer, person or visit from the call; every name was checked against the companies the call names and passed the leak check. No phone numbers.

**Leads, 8 enquiries.**
- Rows: Meadowbrook Tube Bending, Clearwater Pump Repair, Hollis Creek Creamery, Ridgeway Machine and Tool, Bellwood Sign Company, Kettle Run Fabricators, Kingsbury Boat Lifts, Tall Pines Pallet.
- Five came through the website form and have no owner yet. Three were phoned or emailed in, and are owned by you and the two test users, one each.
- Region is left empty on all eight, for whoever routes them. Next step dates run from 2 to 12 November.

**Accounts, 6 customers.**
- Rows: Sterling Gear Works, Highland Spring Bottling, Eastbrook Tank and Trailer, Morrow Creek Grain Systems, Lantern Hill Plastics, Birchfield Millwrights.
- Account owners are spread across you and the two test users, two each.
- Visit lines run from mid-August to 21 October, and each Last visit matches the newest line.

**Planted cases.**
- An enquiry that names no place: Bellwood Sign Company, expected Suggested region Unclear.
- An enquiry for three lines: Kettle Run Fabricators, expected Product line "Several lines".
- A customer with one thin visit a month old: Morrow Creek Grain Systems.
- The workflow's one run on the quiet quote above.

The eight new enquiries each set off the New lead alert, so you get eight notifications as they are added.

**Last day the build can start: Friday 30 October 2026.** After that, the next step dates and visit lines stop reading as current, and the helper's first scheduled note moves to 1 December; a later build needs a new revision.

## 7. Hard to undo

- **No new folder, workspace or install.** v0.1's folder and boards are used as they are.
- **Seven columns added to the CRM's own boards** (Enquiry, Product line, Suggested region, Visit log, Visit summary, Drafted next step, Follow-up check). A column added to a native board cannot be removed, and the build never removes or archives a native.
- **The AI columns fill from the moment their AI is set.** The build leaves them as they are: you delete the demonstration's boards afterwards.
- **The workflow's publication cannot be taken back through the API.** It is published switched on, and switching it off is a step in monday (U8).
- **The agent is an account-level object,** switched on at the end of the build. The build switches it off when you say the demonstration is over.
- **The automations:** v0.1's two alerts stay as they are and are live. Switching both off after the demonstration is already v0.1's step U5. This version adds no automation.
- **The Forecast notes doc** stays in the folder.

## 8. Left for you in monday

- **U6:** add the Enquiry column to the New lead form as a question.
- **U7:** run the Monthly forecast note job once in monday and read the first note in Forecast notes. The API cannot read what the helper wrote.
- **U8:** when the demonstration is over, switch off the Quiet quote follow-up draft workflow.

Still open from v0.1: U1 (kanban of Opportunities by stage), U2 (log a few timeline entries), U3 (try lead conversion), U4 (fix the Quiet quote alert's condition), U5 (switch off both alerts after the demonstration).

## 9. Build checks

**Unproved, each with its fallback:**
- **AI on a column of a CRM native board.** The probes set AI on a plain board; the one try on a native was refused for its source, not for being native. *Fallback:* the column stays a plain column, and the build notes say which AI piece was not built.
- **A condition step in a workflow built through monday's workflow builder.** The probe built a trigger, an AI step, column changes and a notify, but no condition. *Fallback:* the workflow is built without the condition, so it drafts for every open quote whose follow-up date arrives; the build notes say so.
- **The agent writing into a doc it has read-and-write access to.** Not proved, and an agent's output cannot be read through the API. *Fallback:* you check the first note by eye (U7). If nothing lands in the doc, the note is read where monday shows the helper's run, and a later revision moves its output to an update on a named row.

**Also checked during the build:**
- The workflow's time and zone are given explicitly, because the builder defaulted to 09:00 UTC in the probe, and read back. The workflow passes monday's validation before its one run.
- The agent's instructions and job are read back after every write, because the first write after creating an agent can be lost. Its state is read after every write too.
- Each AI column is checked by the recipe monday stores for it: its kind, source and instructions. Two or three new rows are read a minute after each batch. A category that differs from the planted expectation is shown to you, not treated as a failure.

## 10. Lint warnings

None. The frozen revision is clean on the leak lint and on the record check. Two lines were reworded before freezing, one blocked and one warned on, so nothing is left to show.
