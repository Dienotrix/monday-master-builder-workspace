# Bellamy Ridge Construction Group: what v0.1 contained

This is a plain description of the first version shown to the client, for use with the follow-up call transcript in this folder. The discovery call is in `s8-discovery-enterprise-pmo`.

**Shown:** Wednesday September 23, 2026, 2:00 p.m. Eastern, a screen-share walkthrough of 45 minutes, which is the meeting agreed at the end of the discovery call. Marisol Bettencourt (PMO Director), Warren Tibbetts (Senior Project Manager) and Ines Kovalenko (Resource Manager) all attended. There is no transcript of that walkthrough. Afterwards all three were given read-only access to the workspace so they could go back into it themselves, which is how the senior project manager comes to have looked a superintendent up in the workload view on the Friday. That access is to the Consultant's own account, not to anything of the client's.

**Where:** not in the client's own monday account. Stefan, their IT director, still has the security questionnaire open, so nothing was put into their tenant. v0.1 was built in a monday account of the Consultant's, in one workspace called "Bellamy Ridge PMO (v0.1)", on a plan where portfolios and projects are available, so the portfolio layer could be shown at all. The client's own Enterprise account, its 220 seats, preconstruction's bid board and safety's incident board were not touched.

**Data:** the sample data is invented, loosely based on what the client sent after the discovery call: Cumberland's reporting template, the August summary page, two tabs of Ines's grid and Warren's forecast sheet. Sage 300 is not connected, so every budget and spent-to-date figure is a sample number typed in by hand. No loaded rates and no salaries appear anywhere. No patient information and no photographs of any kind.

**Real names:** Marisol asked for real job names rather than placeholders. Three were used, all of them named out loud on the discovery call: Cumberland bed tower, Waverly cath lab, Pellham fit-out. The other three pilot jobs, the Chattanooga ones, were not built.

## Portfolio

**Bellamy Ridge Portfolio**, a monday portfolio with the three projects connected to it.

- Roll-up columns: Health (red/amber/green, rolled up from the project), Burn % , Next owner milestone (name), Next milestone date, PM, Office, Program.
- Program values: Cumberland on the bed tower, Waverly on the cath lab, Pellham on the fit-out. There is no program grouping and no per-program view; the column exists but nothing is done with it.
- With three rows connected it looks thin, which is part of why the follow-up call goes the way it does.

## Projects

Three projects, each created with monday's project tool from a single project template called **Occupied renovation**. All three carry the same groups and columns.

- Project-level fields: Health (status: Green, Yellow, Red), Percent complete (number), PM (people), Superintendent (people), Office (dropdown: Knoxville, Chattanooga, Huntsville), Program (dropdown), Project type (dropdown: Ground-up, Occupied renovation, Equipment), Owner (text, the health system).
- **Startup** group: the 60-something-line Excel checklist trimmed to 18 items, including insurance certificates, notice to proceed, preconstruction meeting, ICRA, badging, submittal log setup and schedule baseline. Columns: Owner (people), Due date, Status (Not started, Working on it, Done).
- ICRA items sit in the Startup group with an **Expires** date column, on all three projects.
- **Phases** group: phase items with Timeline, Phase budget (number, sample), Spent to date (number, sample), Burn % (formula) and Status.
- **Milestones** group: milestone items with Contractual (yes/no), Baseline date, Current date and Owner-facing (checkbox). The Cumberland bed tower has eleven, including first patient day; the cath lab has four and the Pellham fit-out three. There is no history beyond baseline versus current: when a date moves, the move itself is not recorded.
- Nothing about drawings, RFIs, submittals or daily reports. Those stay in Procore, and the walkthrough said so.

## Resource view

**Resource allocation**, a board with one item per assignment of a person to a project.

- Columns: Person (people), Role (dropdown: Project manager, Superintendent, Project engineer), Office, Project (connected to the three projects), Timeline, Allocation % (number), Occupied-work qualified (checkbox).
- About sixty people seeded across the three offices from Ines's two grid tabs. Four superintendents are ticked as occupied-work qualified, Junie Rasco among them.
- Views: the main table, plus a Workload view named **Who's over**, showing each person by week with effort taken from Allocation % and capacity set at 100%. People over capacity show in red.
- Field crews are not in it, at the client's request.
- Every row is a commitment. There is no distinction between a person being requested and a person being confirmed, and no rule about who may confirm.

## Dashboard

**PMO overview**, reading from the portfolio, with six widgets: Projects by health (pie), Burn by project (bar), Next owner milestones in the next 30 days (table), Projects by program (pie), People over capacity (table, from Resource allocation) and Active projects (numbers).

## Automation

One, on the projects: when an ICRA Expires date is 30 days away, notify the project manager.

## Not in v0.1

- The ground-up and equipment project templates (only occupied renovation was built)
- Any connection to Sage 300; all burn figures are sample numbers
- The three Chattanooga pilot projects
- A Cumberland program view, and anything shaped like the template Cumberland sent for January
- Any view or dashboard aimed at the executive committee
- Milestone change history beyond baseline versus current
- Requested-versus-confirmed on allocation, and any permission model at all
- Microsoft single sign-on, permissions, restricted columns and anything for the security review
- Field crews, warranty calls, and preconstruction's pipeline
- Anything at all inside the client's own monday account
