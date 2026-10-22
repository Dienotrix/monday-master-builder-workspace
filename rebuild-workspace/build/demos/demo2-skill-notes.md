# solution-blueprint skill: notes from demo 2 (bramblewood-signs, strand 001)

Result: v0.1 revision 1 frozen, sha256 `1b99a48c279bc89422ff51ca67f8f43087fbde1226e9faaff53b38f675e4e6d6`, leak lint clean (0 block, 0 warn, 0 caution) on the third run. The element-key table has 78 rows (76 elements plus 2 UI steps). STRAND.md is now at `stage: blueprint` with `next_step` pointing at the card. No monday call was made and none was needed.

Each note gives where the problem is, what was wrong or missing, what I did, and what the skill should say. The most important come first.

## A. Design gaps (the biggest)

1. **There is no rule for a pain whose answer needs a cross-row or two-hop check.**
   - Where: design rules 1 to 3 and 7.
   - Problem: two pains need logic that native monday does not do:
     - Double booking: is another install using the same crew in the same part of the day?
     - Install after expiry: does the install fall after the job's permit end? That runs install → job → permit, a mirror of a mirror.
   - The readiness check promises both as "fixes", and its clearance asks for the flag to be "tested against a planted overlap". The skill says nothing about cases like this.
   - What I did:
     - Double booking: a status flag (Booking check) that the coordinator sets by hand, plus a this-week view sorted by crew, day and part of day so overlaps sit side by side. It is planted once in the sample data. Section 3 says "shown"; section 1 defers a flag that sets itself.
     - Install after expiry: a formula on Jobs over two mirrors (latest install date, earliest permit end).
   - Should say: when a pain needs a cross-row check, choose one of three answers and state which:
     - (a) a view that sorts so the clash sits on neighbouring rows, plus a flag set by hand;
     - (b) a formula over mirrors on the parent;
     - (c) deferral to a workflow or AI step in a later version.
   - The trace row should then read "partly" with the reason. It should never read "fixes" for something a person sets by hand.

2. **The readiness "AI opportunities" section is ignored.**
   - Where: Before anything and Design rules.
   - Problem: readiness.md lists four AI or workflow opportunities, each tied to a pain, marked "round 2" with probe ids. The skill does not say whether to plan them, defer them or list them. It also does not say what "round 2" means for this version.
   - What I did: deferred all four. They are named in plain words in section 1's "Not in this version" and in section 16. None was planned as an element.
   - Should say: AI opportunities are deferred unless the readiness marks one for this version. A deferred one is named in section 1. A planned one needs its element kind (workflow, ai_column, agent) and a probe.

3. **Formula columns are never mentioned.**
   - Where: Design rules.
   - Problem: the skill covers mirrors (rule 3) but not formulas. A formula cannot be filtered (G-33) and cannot trigger an automation (the readiness says so for permit expiry). G-32 proves formulas over number mirrors, but not over date mirrors with earliest or latest.
   - What I did:
     - Used two formulas: Permit check over two date mirrors, and Calculated end (approval date plus days valid).
     - Kept every view filter on plain columns.
     - Wrote a fallback in section 16 build checks and on the card: if the formula over date mirrors does not evaluate, it is dropped and the two mirrors are shown side by side.
   - Should say: formulas show values and nothing else. They are never filtered, never trigger anything, and a formula over a date mirror is a build check with a stated fallback.

4. **Rule 3's "also a plain column" leaves out who keeps the copy in step.**
   - Problem: rule 3 says a value a view filters on "is also a plain column", but not how that plain copy stays equal to the mirror (by hand, by an automation, or not at all).
   - What I did: designed every view to filter on the child board's own source columns, so no copy was needed.
   - Should say: filter on the source board's own column where you can. Where a copy is unavoidable, name who or what keeps it, and make that an assumed term.

5. **Rule 1 collides with the client's explicit wish.**
   - Problem: the operator rejected a separate Permits board twice ("permits live on the job"). The readiness leaning allows "connected items shown on the job". Rule 1 forbids subitems.
   - What I did: gave permits their own board, linked two-way and shown on the job through mirrors (permit states, first permit end), with the reasoning recorded in fork 1.
   - Should say: when the client refuses "a second board to open", use a linked board read through mirrors on the parent, and record it as a fork in the client's terms.

6. **Rule 4 collides with weeks as groups.**
   - Problem: rule 4 says groups split open from finished. The client asked to keep weeks as groups (the prototype's one success).
   - What I did: four dated week groups plus a Done group.
   - Should say: a grouping the client asked for comes first, with one finished group added after it. The rule should also say who creates next week's group, which is a UI step or an assumed term. I left that open, and it should be added.

7. **Exact names, "dates around the week of the build", and an unknown build date cannot all hold.**
   - Where: rule 9 and the element-key rule "Name every row exactly as it will be built".
   - Problem: the week groups ("Week of 19 Oct" and so on) and the sample dates are frozen. The build date is unknown at freeze, and the build happens only after the yes.
   - What I did: dated everything for a build this week or next, and wrote in section 16 and on the card that a later build needs a new revision.
   - Should say one of two things:
     - (a) Sample dates and dated group names are relative to the build day ("week of build + 0..3"), and account-build resolves them. The table then names the pattern.
     - (b) A build that slips past a named week needs a new revision.

8. **Rule 7's "at a time of day" is ambiguous for change triggers.**
   - Problem: the install-date-changed alert has no time of day.
   - What I did: applied the time only to the date trigger (07:00, 14 days before end date). The change trigger notifies at once.
   - Should say: date triggers name a time; change triggers fire when the change happens.

9. **People columns before the test-people list.**
   - Problem: rule 7 bars notifying anyone but the user, and the readiness leaning wants crew leads as people. The skill does not say what to do with a people column in the meantime.
   - What I did: made Crew a dropdown (Crew A, B, C), deferred a crew-lead people column, and had the move alert go to the user, standing in for the lead.
   - Should say: until the list arrives, plan people as a dropdown or leave the people column empty, and say which.

10. **The default Name column is not covered.**
    - Problem: the skill does not say whether to rename it, whether it is an element, or what item terminology to use.
    - What I did: left it as "Name", unkeyed.
    - Should say one line about it.

## B. Data policy and record gaps

11. **The skill's rule on names contradicts the readiness and the call.**
    - Problem: rule 9 says "Invented names". The readiness says "the sample rows carry the client's job names and customers, which the key allows". In the call, the owner wants it shown on the operator's own jobs. The run rules and CLAUDE.md (neutral names, no firm names) agree with the skill.
    - What I did: used invented, neutral names only (descriptive customers such as "Grocery rollout – Store 01", invented cities and job numbers), and said so on the card.
    - Should say: the skill's rule wins over any readiness permission while A30 is strict, and the card names the choice.

12. **Exclusions are not synced with the readiness.**
    - Problem: the readiness clearance says the production manager's April change "stays out of everything that leaves the room", but exclusions.md is empty, so the lint cannot enforce it. The skill only says to read exclusions.md.
    - What I did: kept the matter out of every client section and every sample row. I did not add an exclusions row: the skill does not say to, and record-map gives exclusions to the user and call-intake.
    - Should say: compare the readiness's keep-out lines with exclusions.md before the lint. If one is missing, ask the user once to add the row (or add it with the user's OK), then lint.

13. **The skill points at summaries that do not exist.**
    - Problem: "the call or document summaries the readiness check cites": the readiness cites only timestamps, and the record holds a raw transcript and no summary.
    - What I did: read the transcript.
    - Should say: if no summary exists, read the transcript, and restate it without quoting (sections 1 to 15 forbid quotes anyway).

14. **The record itself has inconsistencies.**
    - These are not skill gaps, but they matter for the test.
    - readiness.md says "Written for demo 1 (A31)", but this is demo 2.
    - The readiness's working session, "Tuesday 20 October", falls before today, 22 October.
    - The readiness lists 13 assumptions, three of which do not touch this build. I said so in section 16.

15. **The workspace name is ambiguous.**
    - Problem: the skill says the folder is `<client> – Ops`. CLIENT.md's name is "Bramblewood Signs"; the readiness names "Bramblewood – Ops".
    - What I did: used the readiness name, "Bramblewood – Ops", because it is the specific one.
    - Should say whether `<client>` is CLIENT.md `name` or a short form, and which source wins.

16. **There is no step for the plan tier.**
    - Problem: section 14 asks for it, CLIENT.md says `monday_tier: unknown`, and a blueprint makes no monday reads.
    - What I did: wrote that nothing needs more than boards, table views, mirrors, formulas, six automations and one dashboard, and that the final account's plan is read before anything is built there.
    - Should say what to write when the tier is unread.

17. **The record is left without a log entry.**
    - Problem: `freeze` and the guard writes add no entry to log.md. The skill does not ask for `record.py log`.
    - What I did: nothing. log.md shows "version opened" and then nothing for the blueprint or the freeze.
    - Should say: either add a log step (blueprint drafted, revision N frozen with its sha), or `freeze` should log itself.

18. **Other files the full skill owns are not mentioned.**
    - Problem: record-map.md gives solution-blueprint backlog.md, allowlist.md, open-questions.md (insert a fork, mark it bypassed) and dependencies.md. The lean skill names none of them.
    - What I did: none were written.
    - Should say: either "not in the lean version", or when to write them.

19. **There is nowhere to record the user's yes.**
    - Problem: "Record the user's words" names no file or field before account-build. Options would be STRAND.md, version.md `## Events`, or the conversation.
    - Should say where the user's yes is kept.

## C. Element-key table and its coupling to ledger.py

20. **The kind words are missing.**
    - Problem: the skill lists key forms but gives only one kind word (`ui_step`). The words `item_batch`, `automation`, `dashboard`, `widget` and the rest come from ledger.py's TYPES. ledger.py refuses an unknown kind at approval.
    - What I did: read ledger.py and used its words.
    - Should say: list the kinds, which are workspace, folder, board, group, column, view, form, doc, dashboard, widget, automation, item_batch and ui_step.

21. **A referenced W1 cannot be marked, and the ledger contradicts itself.**
    - Problem: the skill says to plan the test workspace as "a referenced row (W1)", but the table has no column for origin. ledger.py `approval` takes `--referenced W1`, yet it also requires every workspace and folder under `--irreversible` (MUST_LIST). So a workspace that is never written must still be listed as an irreversible step.
    - What I did:
      - Wrote W1 as a normal row named "Builder Test Workspace".
      - Wrote in section 16 that W1 is referenced, never written, and that F1 is the first irreversible step.
      - On the card, listed only the folder as hard to undo.
    - Should say how to mark a referenced row (for example a note in section 16, or an `origin` column). ledger.py should also exempt referenced rows from MUST_LIST.

22. **Mirror sources and two-way pairs have no place in the table.**
    - Problem: the table carries key, kind, name and notifies only.
    - What I did: listed the pairs and mirror sources in section 16's build checks.
    - Should say: put them in section 16, or add a `refs` column.

23. **Section 6's fixed heading uses a banned word.**
    - Problem: the heading is "Live objects this strand touches", but sections 1 to 15 must contain no internal word "such as strand". The lint exempts template titles, but the client still reads the word.
    - Should say: rename the section, for example "Live objects this work touches".

## D. Scripts: refusals and how I got past them

24. **Leak lint, run 1: blocked three times.**
    - The wall rule fired twice on "test workspace" in sections 7 and 14 ("matches a name of another client record under the home"). The A31 test workspace's name is harvested as a name from another client record, so the plain description that development builds need trips the wall in every A31 record.
    - The phonetic rule fired once on "real names" (in section 14), as a near-sound of the user's firm term.
    - Fixed by rewording to "a closed Work Management workspace set aside for demonstrations" and "nobody's actual name". Runs 2 and 3 were clean.
    - The skill should warn about the test-workspace wording, or the index should stop harvesting the test workspace's name as a client name.

25. **The skill never mentions MMB_HOME.** The lint reads `<home>/clients-index.json` and `<home>/local/settings.json`. The skill does not say MMB_HOME must be set or how home is found; I set it as the run instructions said.

26. **The scripts give little usage help.**
    - `leak_lint.py --help` returns a could-not-run envelope (no help is defined).
    - `record.py --help` lists no commands.
    - I took the flags from the skill and from the parser code: `version open` defaults to the next version and needs no `--version`, and `--strand` is the three-digit id.

27. **The skill does not say where to stage files.** `guard --from <staged file>` needs a staged copy. I staged in the client record's `.work/staging/`, inside the record and never guarded, and deleted it after the last write. The skill should name the staging place and say to clean it up.

28. **The skill's interpreter line is wrong for this machine.** It says `py -3` on Windows; this run needed `py -3.9`. Minor; the skill should defer to the environment's pinned interpreter.

29. **No other refusals.** The guard, version open, freeze and `record.py check` (run once before freezing; the skill does not ask for it, and it is worth adding) all passed first time. My own helper script failed once on Python 3.9's `write_text(newline=)`; that was not the plugin.

## E. Smaller wording points

- The front matter placeholders `"<v0.1>"` and `"<N>"`: it is unclear whether the angle brackets stay. I wrote `"v0.1"` and `"1"`. The skill should say that revisions start at 1.
- `sample_rows: "planned"`: the skill does not list the other allowed values.
- The skill does not say where the readiness clearance conditions go (the expiry probe, and the planted overlap tested before the first look). I put them in section 16 build checks and in card item 9.
- The skill cites A5, A11, A21, A28, A31, A32, ARCHITECTURE A§3.4 and BUILD-PLAN WP9, none of which a client session can read. The rules are restated inline well enough, except "round 2" and "referenced row".
- Dashboard: the skill does not say whether a chart widget can group by a dropdown column (Hold reason, Crew). I assumed it can; it is unproved.
