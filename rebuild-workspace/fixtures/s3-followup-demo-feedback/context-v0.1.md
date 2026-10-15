# Brackenholt Architects + Engineers: what v0.1 contained

This is a plain description of the first version shown to the client, for use with the follow-up call transcript in this folder. The discovery call is in `s1-discovery-strong`.

**Shown:** Thursday September 24, 2026, 10:00 a.m. Central, a video walkthrough of about 40 minutes. Tess Kowalczyk (COO) and Jordan Pruitt (Operations Manager) attended, and Gordon (managing partner) joined for the first 20 minutes, which covered pursuits. There is no transcript of that walkthrough. Afterwards Tess, Jordan and Hallie (marketing coordinator) had logins so they could click around.

**Where:** a monday.com trial account set up for this engagement, with one workspace, "Brackenholt Operations". Pursuits and owners use monday CRM. Jobs, phases, submittals and staffing use monday Work Management.

**Data:** the sample data is invented, loosely based on the scrubbed copies Jordan sent (the Wall, the pursuit log and one Ajera export). Ajera is not connected: hours and spent-to-date figures are sample numbers. No rates or salaries appear anywhere.

## Boards

1. **Pursuits** (CRM, one item per pursuit)
   - Stage (status): New, Qualified, Proposal, Negotiation, Won, Lost. These are the CRM-style default labels, left unchanged.
   - Office (dropdown): Madison, Milwaukee, Rockford, Des Moines. Market (dropdown): K-12, Municipal and civic, Healthcare, Justice.
   - Owner (connected to Owners). Solicitation (dropdown): RFQ, RFP. Source (dropdown): Bid portal, PIC relationship.
   - PIC, PM, Marketing (people). Due date (date with time). Bid portal (link). Portal contacts (people).
   - Addendum (status): None, New addendum, Reviewed. Latest addendum (date).
   - Fee (number). Fee sign-off (status): Pending, Approved, Rejected. Fee proposal (file).
   - Addenda subitems: Addendum no., Received (date), What changed (text).
   - Views: the main table only. During the walkthrough the board was filtered live to pursuits due in the next two weeks, but that filter was not saved as a view.
   - Sample items include a city hall renovation with two logged addenda.

2. **Owners** (CRM accounts, one item per client organisation, such as a school district, city or county, or health system)
   - Type (dropdown), Office (dropdown), Pursuits (connected), Jobs (connected).

3. **Jobs** (Work Management, one item per Ajera job, grouped by office)
   - Job number (text), Project (text), Job type (dropdown: Architecture, Engineering-only, Additional service), Owner (connected), PIC and PM (people), Status (Active, On hold, Closed), Phases (connected).
   - The Oak Street fire station appears as one project with two jobs: the base building and the apparatus bay equipment package.
   - Submittals subitems give each job a basic submittal list: Submittal (name), Received (date), Due back (date), Reviewer (people), Status (Open, Returned).

4. **Phases** (Work Management, one item per job phase)
   - Job (connected), Phase (dropdown: SD, DD, CDs, Bidding, CA, Design; engineering-only jobs use Design and CA), Status (blank, Working on it, Stuck, Done), Timeline.
   - Phase fee (number), Hours to date (number, sample), Spent to date (number, sample, basis not specified), Burn % (formula: Spent to date / Phase fee), PM (mirrored from the job).
   - There is nothing about billing or invoicing.

5. **Staff allocation** (Work Management, one item per assignment of a person to a job)
   - Person (people), Office and Studio (dropdowns), Job (connected), Timeline, Allocation % (number).
   - Groups: Madison, Milwaukee, Rockford, Des Moines (empty).
   - Views: the table, and a Workload view named "Staff allocation" that shows each person by week, with effort taken from Allocation % and capacity set at 100%. People over capacity show in red. The sample data has one structural engineer at 140% across three jobs, with two Rockford engineers at 60%.

## Dashboard

**Firm overview**, with six widgets: Pursuits by stage (pie chart), Pursued fee by office (bar chart), Pursuits by market (pie chart), Phases by status (battery), Burn by job (bar chart) and Total pursued fee (numbers).

## Form

**New pursuit**, a form on the Pursuits board for Hallie and the PICs. Its questions are pursuit name, owner, solicitation (RFQ or RFP), source, due date and time, bid portal link, office, market and notes. It has no question about who is registered on the portal.

## Automation

On Pursuits: when Addendum changes to "New addendum", notify the people in PIC, PM and Marketing.

## Not in v0.1

- Owner approvals (deferred at discovery)
- A live Ajera connection
- Handover from a won pursuit to a job
- Permissions, restricted columns and Microsoft single sign-on
- Des Moines staff (the group exists but is empty)
