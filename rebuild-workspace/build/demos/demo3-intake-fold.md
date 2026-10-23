# Demo 3: what was folded into the intake skills

Written 2026-10-22. The changes made to `call-intake` and `build-readiness` from `demo3-readiness-grade.md` (section 6 points 1 to 8, and its other sections where noted), `demo3-intake-notes.md` (notes 1 to 12) and `intake-skill-notes.md` (A1 to C29). Each is written as a general rule for any call. Neither the fixtures, the answer key nor any client record was read.

Line counts after: `call-intake/SKILL.md` 90, `call-intake/references/intake-shapes.md` 102, `build-readiness/SKILL.md` 70, `build-readiness/references/readiness-guide.md` 105. Plugin lint: 0 errors in the four files.

## call-intake/SKILL.md (19)

1. Always: a client's yes to the user's side's playback goes under `## Agreed`, the user's side's wording with the client's confirming words; agreed scope, not a goal. Intake note 4.
2. Always: a quote cut short shows the cut with `…`. Grade section 5.
3. Always: take the whole input, not the headline of each theme. Grade 1 and 3.
4. Always: each `record.py` write refreshes the home's `clients-index.json`, which is expected. Intake note 12 (fourth point).
5. Before anything: the client's name. Ask the user once before `init` when the input does not give it; with no one to ask, a descriptive placeholder (trade and place), a slug that reads well later, a `gap` assumption, and `client rename` for the real name. Intake note 1.
6. Before anything: `init` records `own-account`; an input's offer of another target is an open question for the user, never a change. Intake note 7.
7. Saving step 4: with no date in the input, the stem carries the save date, `call_date` reads `unknown`, and a spoken clue goes under `## Call type`. Intake note 10.
8. Reading a call: minute-and-second stamps take a zero hour, `@00:MM:SS`. Intake note 3.
9. Speakers: the user's side's lead speaker is the user, whatever role word labels them. Intake note 12 (third point).
10. Quarantine: a scenario the user's side makes up is `[X]`; a client's estimate given under the user's side's what-if is kept as `estimate under a what-if`. Intake note 6.
11. Call type: a signal for `seat`. Intake note 12 (first point).
12. Call type: a later correction changes `call_type` and is logged; the stem stays. Author note A9 (the skills' half).
13. New "What to take", pains: workarounds kept by hand, "will not survive growth" lines, deferred pains marked `deferred`, a second pain or harm on its own line. Grade 1 and 2.
14. What to take, entities: children and neighbours by kind (routes, owners, stages, steps, agreements, money fields, roles, event kinds, locations, today's artefacts, outside approvers), each flag set per entity, `unknown` where silent. Grade 3.
15. What to take, constraints: non-negotiable rules go under `## Constraints`. Intake note 5.
16. What to take, open items: handover work (data brought across or left, an earlier attempt's fate, real names in sample rows, a goal set by someone absent) is an open question. Grade 5.
17. Writing step 1: the 120-line budget, condense as the reference says, never drop a goal, pain, entity or constraint. Intake note 2.
18. Writing step 4: the sentence about the template's exclusions table is gone; rows go under the template's `## Exclusions` heading. Intake note 11.
19. Hand back: adds deferred pains, entities, constraints, a placeholder name, a build-target offer and an accepted budget warning. Grade 2; intake notes 1, 2 and 7.

## call-intake/references/intake-shapes.md (10)

1. Speakers: the lead speaker on the user's side reads `the user`. Intake note 12 (third point).
2. Goals: a yes to a playback is not a goal. Intake note 4; grade section 2 (the scope statement taken as a goal).
3. Pains: the trailing `· deferred`; a workaround and a "will not survive" line are pains of their own. Grade 1 and 2.
4. New `## Constraints` heading and line form. Intake note 5.
5. Entities: children, neighbours and artefacts; `unknown` allowed; the three flags defined; each set per entity. Grade 3.
6. Figures: `estimate under a what-if`. Intake note 6.
7. Open questions: handover work and a build-target offer. Grade 5; intake note 7.
8. New `## Agreed` heading and line form. Intake note 4.
9. New "Condensing a long input": the order to condense in, what stays one per line, and accepting the warning. Intake note 2.
10. The document snapshot carries `## Constraints` too. Intake note 5.

## build-readiness/SKILL.md (20)

1. Always: a quote keeps the location of the line it came from, in a question too. Grade section 5 (quote 5).
2. Always: an `## Agreed` item frames the build and can settle a leaning, never a goal. Intake note 4; grade section 2.
3. Always: a number, threshold or automation of our own is `ours, provisional: <figure>`; an automation enters only on a pain or stated wish. Grade 7.
4. Before anything: the `clients-index.json` refresh is expected. Intake note 12 (fourth point).
5. Part 1: carry every pain line; workarounds, "will not survive" lines and deferred pains get a pain line and an element. Grade 1 and 2.
6. Part 2: carry every entity, children and neighbours by kind; flags from that entity's evidence, with the shared-resource and goes-stale meanings. Grade 3.
7. Part 3: preflight finds the native set or the build installs it on a bare workspace, not a condition; the client's word for a native entity is recorded and any relabel is the blueprint's, a native not installed by the build never renamed. Grade 4.
8. Part 4: the build target's reason from `CLIENT.md` or the default, and an offered target as an assumption. Intake note 7; grade section 4 (the build target assumption).
9. Part 4: on native boards the pattern's children are connected rows of their own board. Intake note 9.
10. Part 4: one pursuit with several outside documents leans to parent with child rows and a roll-up, on how often it happens. Grade 8.
11. Part 4: each intake route gets its element (a form, an import for lists). Grade section 3 (no import).
12. Part 4: each constraint gets its structure. Intake note 5.
13. Part 4: a hand-keyed value from another system gets a `<system> status as of` date. Grade 8.
14. Part 6: kinds by what the line is (a structural choice with a condition is never a `gap`), and an assumption for each open item, handover work, invented sample rows, an absent person's test, a placeholder name, an offered target and an approximated constraint. Grade 5; grade section 4 (sample rows, the absent approver's test, the build target); intake note 1.
15. Part 7: an unprobed constraint is an unmet need as well. Intake note 5.
16. Part 9: on an own-account build the workspace is the user's, and an unbound client account is no condition. Grade 4.
17. Part 9: a native board automation has no probe and adds no probe condition. Intake note 12 (fifth point).
18. Part 10: one question per unresolved structural choice first; record ownership, a leaver's records and who keys a hand-carried value earn their own. Grade 6.
19. Writing step 1: the exclusions table sentence is gone. Intake note 11.
20. Writing step 3: read `CLIENT.md`'s sha only after the `STRAND.md` write. Intake note 8 and script refusal 1.

## build-readiness/references/readiness-guide.md (10)

1. Pains: every line carried; `· deferred` with its outcome and element row. Grade 1 and 2.
2. Entities: what `shared resource` and `goes stale` mean, each per entity. Grade 3.
3. Structure, build target line: the reason when `CLIENT.md` has none, and an offered target. Intake note 7.
4. Structure, native reuse line: the client's word, and found by preflight or installed on a bare workspace. Grade 4.
5. Leanings: the pursuit-with-several-documents leaning and its condition. Grade 8.
6. Patterns: `as connected rows on <board>` for native children; the pattern for every parent whose children move on their own. Intake note 9; grade section 3 (the roll-up covered one parent only).
7. Element per pain: a hand-keyed value names its as-of date field and who keys it. Grade 8 and 6.
8. Assumptions: how each kind is chosen, `ours, provisional`, and handover lines. Grade 5 and 7.
9. Verdict: each condition names what it waits on; the own-account workspace wording; native boards are not a condition. Grade 4.
10. Questions: one per structural choice before a variant; a quote in `known` keeps its location. Grade 6; grade section 5.

59 changes in all.

## Not the skills'

1. The record map's 120-line budget for `calls/<stem>.md` does not fit a full discovery call, and fits less now that every pain and entity takes a line; it could scale with call length or client speakers. Intake note 2.
2. `init` writes `account_kind: own` and `build_target: own-account` silently, and `CLIENT.md` has no field for the build target's reason, which the readiness guide asks for. Intake note 7.
3. The record map makes call-intake the owner of an "open commitments" block in `STRAND.md`, which the template lacks. Intake note 12 (second point).
4. `record.py check` reads only `@H:MM:SS` and `@HH:MM:SS`; a minute-and-second form could be accepted. The skills now write a zero hour. Intake note 3.
5. The record map's `pains[]` pin has no deferred field; the skills write a trailing `· deferred` until it does. Grade 2.
6. The record map's `structure.patterns[]` form says only "as child rows"; it should allow connected rows on a native board. Intake note 9.
7. No `call-summary.md` or `document-summary.md` template, and the call summary's body is not pinned; the new `## Constraints` and `## Agreed` headings would join that pin. Author note A1.
8. No intake scripts (`transcript_measure.py`, `transcript_prep.py`, quote verification). Author note A3.
9. No `meetings.md` template or pinned line shape. Author note A4.
10. The readiness Markdown headings are not pinned beyond `## Assumptions`. Author note A5.
11. "The seven sweep patterns" are listed nowhere the skills may read. Author note A6.
12. The type-header state word: `proposed` in the record map against `assumed` in the design. Author note A7.
13. The flat front matter cannot carry the header's signals or candidates. Author note A8.
14. Whether a call-type correction should ever re-save the raw file under a new stem. Author note A9.
15. The `STRAND.md` template has no "what this build rests on" block. Author note A10.
16. No `open-questions.md` template. Author note A11.
17. A bare `leak_lint.py scan --strand <id>` with no path returns `could-not-run`; it could say that no draft exists instead. Intake notes, script refusals.
18. The reference is named `intake-shapes.md`, not WP8's `summary-and-recap.md`, because of a tooling refusal; the full skill can rename it. Author note C29.

**Status, 2026-10-22 (the next session).** Shown these points in three groups, the user picked all three to fix now: the record's own points (1 to 7, 9, 10 and 12 to 16, by one agent; `group1-log.md`, the record map patch applied by the main session), point 11 (the seven sweep patterns, now in `intake-shapes.md`; `group2-log.md`) and point 17 (R78 in WP4's `DECISIONS.md`). Point 4 is done for `record.py check` only; the leak lint and `ledger.py` still read a two-digit hour, so the zero hour stays the written form. Point 8 (the intake scripts) waits for WP5, and point 18 (the rename) for the full skill.

Author note A2 (the exclusions template's table) is already resolved in the template; only the skills' sentence about it needed removing (call-intake change 18, build-readiness change 19). Notes B13 to B25 are choices the skills already carry; C26 to C28 are status, not fixes.
