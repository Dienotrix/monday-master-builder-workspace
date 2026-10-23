# Demo 3 log: s6, an industrial supplies distributor, CRM

Internal build file: never client-facing. Demo 3 was the first to run every lean skill in turn, each by a fresh agent that read only its skill: `call-intake` and `build-readiness` on the raw transcript, `solution-blueprint`, then `account-build`. It was also the first CRM build, and the first in which the build installs monday's native CRM boards itself (A38). Ids of the account, the workspaces and every object stay in the client record and `local/`, never here. The agents' own notes are `demo3-intake-notes.md`, `demo3-readiness-grade.md`, `demo3-intake-fold.md`, `demo3-skill-notes.md` and `demo3-build-notes.md`; the native-board probe is `crm-natives-probe.md`.

## Before the demo, 2026-10-22

- **The user's answers:** A36 (three lint loosenings, and every nod in `demo2-log.md` accepted as a batch), the owed script fixes, a CRM test workspace (A37), demo 1 closed, and no list of test people yet.
- **A36 built** by an agent as R71 to R74: the named test workspaces are not client names, the firm's sound-alike rule spares everyday phrases, a payload may carry its frozen revision's planned values, and (found by the main session) a `- ` line inside an HTML comment is no longer read as an exclusion or allowlist row.
- **The demos' fixes** by an agent: `approval` no longer wants a referenced workspace among the irreversible steps; a departed object that is still live reaches the live map; automations are told apart by what `list_automations` returns; `intent --notifies user` is accepted; `freeze` logs itself; gotchas G-150 to G-154.
- **The exclusions template** carried a table the lint never reads, so a keep-out row written the template's way was not enforced. The template now has the `## Exclusions` heading and the row shape the lint reads.
- **Shared words regenerated** three times, each after the firm rule passed over `shared/` against an empty home: `pdftotext` stays out (check L05), and the phrases region keeps its last line on its own (test R41).
- **The lean intake skills** written by an agent from the design (29 notes in `intake-skill-notes.md`).

## Native CRM boards: the probe and A38

The CRM test workspace was created by the main session (closed, in the CRM product). The probe (`crm-natives-probe.md`) found:

1. A workspace made in the CRM product is empty (G-155).
2. `use_template` takes a Template Center id, and monday's CRM solution from the account's Template Center fails with an internal error; a public template installs (G-156).
3. A raw `create_board(template_id)` installs a genuine native, alone, with the template's rows and no automations (G-157).
4. Its empty relations name their intended board in their layout settings; `update_column` links them, two-way, each column on its own revision (G-158).
5. Sales Activities' source-item relation refuses every update, and v2 Deals keeps a stale Account mirror (G-159).
6. Template rows archive in batches (G-160).

Offered the user's install through the UI or the build's own, the user chose the build's own (A38). An agent built the ledger's side: an optional `template` column in the element-key table, `intent --template-id`, a `verify` that needs the template lineage and `items_count` 0, registration in the native board index, and the template's columns changed under the strand's approval. The main session narrowed R-B and R-D in `native-objects.md` 6.3, added 6.6 (natives the build installs) and the audit's exception in 6.4.

## Intake and readiness, from the raw transcript

A fresh agent ran `call-intake` and `build-readiness` alone on the transcript. The result: cleared to build, 8 goals, 15 pain lines, 8 entities and 13 assumptions, with no stop. The transcript names no company, so the record carries a descriptive placeholder name, listed as an assumption.

A Sonnet grader compared it with the s6 answer key (`demo3-readiness-grade.md`):

- **Matched:** the clearance, the call type and all four goals; five quotes spot-checked, all exact, one at the wrong location.
- **Missed:** 6 of 21 pains, and 5 of 30 entities, with 16 only partly. The skills kept each pain theme's headline and dropped the workarounds and the pains the client defers, and kept entities coarse.
- **Invented:** two specifics the call never gave (a seven-day flag, an assignment automation).

An agent folded the grade's eight points and the run's notes into the two skills (59 changes); 18 points belong to scripts, templates or the record map (below). Demo 3 went on from the readiness as written.

## The blueprint

A fresh agent wrote v0.1 revision 1 from the skill alone, frozen at 58 table rows:

- four native installs (Leads, Contacts, Accounts, Opportunities), with Sales Activities left out;
- two alerts to the user, both marked assumed and "not from the call";
- a dashboard of eight widgets, charts first (A35);
- 87 invented sample rows.

The lint blocked six times on the wall, all false (below). The agent's 14 notes were folded into the blueprint skill: visit coverage without Sales Activities, template groups and counterpart relations, a stage relabel with a check on the formulas that read it, invented automations named "not from the call", invented contacts, the last build day on the card, natives as hard to undo, and a plain word for the user. The user approved the card: "Yes, build demo 3 as written on the card."

## The build

A fresh agent built it from `account-build` alone, in two sittings, with 102 monday calls:

- 47 elements built and verified (48 with the referenced workspace), the eight widgets not checkable, and one departed (A1).
- The run is ended and the lease released. The main session re-ran `record.py check` and `ledger.py check`, both clean.
- Live reads showed the four natives in the folder with their template lineage, the 87 rows, every link two-way, both alerts on, and the dashboard in the workspace.

1. **The permission layer refused `create_automation`** after 43 elements were live, as an "unrequested commit". The assistant could not write the allow rules (self-modification), so the user copied in a settings file that adds the connector's automation, dashboard and widget tools. The build resumed in the same run. The skill now says every connector write tool the plan needs is allowed first.
2. **A refused call left its row `attempting`.** Retrying it needed `ledger.py reconcile` over a fresh live inventory, which neither skill said. That is now in `write-path.md`.
3. **A1, the quiet-quote alert, was stored with its condition inverted** ("Stage is not Quoted", `shouldCheckIfStatusIsNot: true`) from an inline condition in the prompt. It is live and notifies only the user. It departed to UI step U4, and the user said to leave it ("can you just continue, it's okay"). Now G-161, and `write-path.md` gives a conditions block.
4. **The native installs went as A38 planned:**
   - four boards, one call each, with their template rows archived (15, 16, 13 and 18), each verified by lineage and `items_count` 0, and registered as natives;
   - five links, made two-way, with every reflection renamed;
   - the stale Account mirror re-pointed to the account's last visit;
   - a form on the installed Leads board, with login required.
5. **The template already had two planned columns** (Leads' Region, Deals' Last activity). The agent changed them rather than add a second column of the same name. Both skills now say so, and G-162 lists what the v2 templates bring.
6. **The Close probability fallback fired.** The template's formula reads its own stage labels, so the forecast chart and number sum Deal value, and the likelihood forecast is recorded as not built.
7. **A planned UI step's key could be taken by a departure,** since `depart` mints the next free U number. The skill now writes the planned UI steps at the run's start.
8. **Smaller points, all folded into the skill:**
   - `monday_tier_source` takes `preflight`;
   - native installs and automations take the card's yes, not `--irreversible`;
   - tools beyond the roster go in the change check's `added`;
   - widgets stay `written` in the ledger;
   - a date axis can group by month;
   - a payload is the call's arguments, never the GraphQL text, and carries nothing that is not sent.

## Every lint block and warning in demo 3 (for the user's pick, A34)

| Where | Rule | What tripped it | A real leak? |
|---|---|---|---|
| Blueprint, run 1 | wall (six) | "Central" (four times), "and the CRM's", "the installed": ordinary words another demo record's index publishes | no |
| Build, every lead and contact | id pattern | phone values, which are digits only and eight or more long | no |
| Build, three accounts, one lead, three contact values | wall | the plan's own invented names, which other demo records publish | no |
| Build, boards and links | id pattern, pain id | the agent's own mistakes: raw query text in a payload, and a note field naming element keys | no |
| Build, status columns | record-number (warn) | label colour numbers matching numbers in the transcript | no |
| Build, sample deal values | figure (warn) | invented values near the call's cost figures, A34's own-figure warning | no |

**The user took all three on 2026-10-22, as A39** ("I agree with the rules to loosen for the lint"), to be built in the next session. **Built the same day in the next session** as R75 to R77 in WP4's `DECISIONS.md`, with six tests; the demo records re-indexed, and `terms` over `shared/` is clean against the development home. The three records' entries lost every code and everyday word (87, 108 and 125 single words before, 39, 47 and 70 after).

Every block, none a leak. The same pattern showed in the main session's `terms` run over `shared/`, where the demo records' indexes publish `account_id`, `desc`, `P-2` and "an AI" as names. Candidates to loosen, for the user to pick from:

- (d) a value under a phone column is not an id;
- (e) the index stops publishing ordinary words, lower-case tokens and short generic phrases as client names;
- (f) a status or label colour number raises no record-number warning.

## Worth the user's nod

- **A37 and A38 readings:** the CRM workspace's name "CRM Test Workspace", and "clear the template rows" read as archiving them.
- **The ledger agent's A38 nods:**
  - companions, subitems boards and the Portal are refused as install templates;
  - updating, archiving or converting the installed board itself stays refused;
  - a second native of one entity in a workspace is refused;
  - groups are narrowed with columns;
  - `items_count` counts active rows only, which a live read confirmed.
- **G-65 was stale; probed 2026-10-22 in the next session.** On the probe Leads board, one automation notifying only the user: `manage_automations` deactivate and activate both worked, read back by `list_automations` as `is_active` false and then true. G-65 is rewritten, and `safety.md`, `read-back.md` and the never-say line follow it. Switching a demo's automations off is now a build step (account-build, "Switching the automations off", run as `switch-off`), tried on a scratch copy of this record: A2 went `inactive` through the ledger and both checks stayed clean. A departed automation (A1 here) takes no ledger write, so it stays a UI step. The probe automation is left switched off.
- **Guard R-H, answered 2026-10-22:** the user chose to have R-H skip a planned native install under R-D's conditions; a native-named board with no template id still asks (A38, `native-objects.md` 6.3 and 6.6).
- **Demo 3 went on from the readiness as written,** rather than re-running intake after the fold.
- **The blueprint skill now puts sample names through the payload lint before freezing,** and plans no phone numbers.

## Not the skills', from the intake fold

Eighteen points for scripts, templates and the record map, listed in `demo3-intake-fold.md` under "Not the skills'":

- the 120-line budget of a call summary;
- `init`'s silent build target;
- the missing open-commitments block, call-summary, `meetings.md` and `open-questions.md` templates;
- the `pains[]` pin without a deferred field;
- the summary body and readiness headings not pinned;
- no intake scripts yet;
- the call-type state word;
- a bare `scan --strand` with no path;
- and smaller ones.

## For the user in monday

In the CRM test workspace, folder "Industrial supplies distributor, Toledo – CRM": the Leads, Contacts, Accounts and Opportunities boards, their views, the "New lead" form and the "Sales overview" dashboard (links given in the session). UI steps left:

- U1: add a kanban view of Opportunities by stage.
- U2: log a few calls and visits on sample accounts' activity timelines.
- U3: try the CRM's own lead conversion on one sample lead.
- U4: in the quiet-quote alert, change "is not" to "is" Quoted, and check the trigger reads 7 days after Last activity.
- U5: switch both alerts off when the demonstration ends. Since G-65's probe, the build switches A2 off itself on the user's word (`switch-off`); A1, departed, stays this UI step.

Also worth a look: the Leads template's own "Web Form" view, whose login setting the build did not read, and the eight widgets, which only an eye can check. The planted quiet quote alerts on Monday 26 October at 8:00, once U4 is done. The two probe folders ("Probe – native install", "Probe – use_template check") are test objects the development tooling may clear.
