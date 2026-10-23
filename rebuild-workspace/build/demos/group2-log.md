# Group 2 log: the seven sweep patterns (point 11, author note A6)

## Where they came from

`for-review/FEEDBACK.md`, "Cross-fixture patterns from the review", item 1 (the sweep list, seven bullets; the section's first sentence names two, the user's review of the fixtures added five). The fixture fix pass brief (`rebuild-workspace/fixtures-work/_fixpass/BRIEF.md`, section 4, "The seven-pattern sweep") lists the same seven in the same order, and the fix-pass change logs cite them by number. `stage-1b/PLAN.md` section 7 records only that the sweep ran. Confirmed: seven.

## The seven, as written in `intake-shapes.md`

1. One row where the call describes many: write the parts as entities with a parent and "moves on its own: yes"; the readiness check makes the leaning.
2. A pain with no element that fixes it: keep the pain and its outcome; the readiness check shows the gap as verdict `none`.
3. An alias that names more than one entity, or many names for one: one entry per person, place or organisation; fold only when the call shows they are one; never merge distinct ones.
4. Our framing labelled as the client's: record it as the user's side's, or under Agreed; never a goal or the client's stages.
5. A shared resource with no reservation tracking: flag `shared across jobs: yes`, quote how it is booked, ask who holds it when.
6. An artefact that can go stale with nothing to flag it: flag `goes stale: yes`, quote the failure, ask how anyone would know.
7. An expected output the input cannot support: write only what the input carries; say what is missing under "What the input cannot see".

## Files changed

- `monday-master-builder/plugins/monday-master-builder/skills/call-intake/references/intake-shapes.md`: new section "The seven sweep patterns" (file not renamed).
- `.../skills/call-intake/SKILL.md`: one "Always" line pointing to it.
- `.../skills/build-readiness/references/readiness-guide.md`: one line under "The headings, in order" pointing to it for patterns 1, 2, 5 and 6.
- This log.

Patterns 1, 2, 4, 5 and 6 were already partly carried (entity flags, "Element per pain", the "Always" rule on the client's words); the section states the rule once and points to those places.

Lint: `py -3.14 tools\lint_plugin.py --root .` gave 0 errors, 1 warning (no personal-names list), no `__pycache__` left.

*Nod:* the section's text for patterns 5 and 6 asks intake to put a question under `## Open questions` (who holds a shared resource when; how anyone knows an artefact is out of date). That adds open questions the shapes did not ask for before; say if intake should only set the flag and leave the questions to the readiness check.
