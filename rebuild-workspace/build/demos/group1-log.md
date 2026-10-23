# Group 1 log: the record's own points from the demo 3 intake fold

Written 2026-10-22. The fourteen points of `demo3-intake-fold.md`, "Not the skills'", that belong to the record: 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14, 15 and 16. Internal build file.

## Files

In the plugin tree (`monday-master-builder/`):

- `plugins/monday-master-builder/scripts/record.py`
- `plugins/monday-master-builder/templates/record/CLIENT.md` and `STRAND.md` (changed)
- `plugins/monday-master-builder/templates/record/call-summary.md`, `document-summary.md`, `meetings.md` and `open-questions.md` (new)
- `tests/unit/test_record_part2.py`: a new class `IntakeFoldTest`, 17 tests, and `SCRIPTS` added to its import from `test_record`

As a patch, not applied: `rebuild-workspace/build/demos/group1-shared.patch`, the record map (`plugins/monday-master-builder/shared/record-map.md`) only, made with `git diff` from the plugin root in the scratch copy. `git apply --check` passes against the real tree. No fixture changed, so there is no `group1-fixture.patch`. `tools/lint_plugin.py` and its tests are unchanged: no pin the lint checks needed them.

**The `group1 override`.** Ten of the 17 tests read a pin of the record map. Each goes through one helper, `IntakeFoldTest.pinned()`, which skips while the map lacks the pin. The `if` block in that helper carries the comment `# group1 override`. Remove that block once the patch is applied, so that a missing pin fails rather than skips.

## Point by point

1. **The call summary's budget.** `record.py check` now gives a call summary that sits beside its saved transcript one line per 30 words of that transcript, at least 120 and at most 250. A summary with no transcript beside it keeps 120. It is still a warning, never a block, and the warning names the transcript and the figures. Demo 3's transcript has about 6,000 words, so its budget is now 202 lines. Record map: the `calls/<date>-<type>.md` row. Code: `CALL_BUDGET` and `Check.budget()`.
2. **The build target's reason.** `CLIENT.md` gains an optional `build_target_reason`, after `build_target` in the template. `init` writes the default's reason ("the default: a proof of concept is built in the user's own account until the user names another target") and prints `build_target` and `build_target_reason` in its output. A template without the key gets it appended, so an older template still works. `check` treats the field as optional, as it treats `former_names`, so a record written before it stays clean. Record map: `client/2`, and the readiness `structure` row (the reason from `CLIENT.md`, else the default's). The `created` log entry is unchanged.
3. **Open commitments in `STRAND.md`.** The template gains `## Open commitments`, after `## Next step`, with its line form in a comment: `- <what> · owner: <role> · when: <date or unknown> · from: calls/<stem>.md`. A line leaves the block only on evidence that the commitment was kept. Record map: section owners.
4. **Minute-and-second stamps.** `check`'s location pattern now reads `@MM:SS` (and `@M:SS`) beside `@H:MM:SS` and `@HH:MM:SS`, and its warning text lists `@MM:SS`. The record map keeps the zero hour (`@00:03:44`) as the form to write, because `leak_lint.py` and `ledger.py` still read only a two-digit hour. See the stop below.
5. **Deferred pains.** The readiness pin's `pains[]` gains an optional `deferred` (`true` when the client puts the pain off; absent reads `false`), and the line in `readiness.md` and in the call summary ends ` · deferred`, as the skills write it.
6. **Connected rows.** `structure.patterns[]` also allows `parent-row-with-roll-up: <parent> with <children> as connected rows on <board>, <roll-up> on the parent` where the children are rows of a native board of their own.
7. **The summary templates and the body pin.** New `call-summary.md` and `document-summary.md` templates, front matter as the record map pins it, then the headings in order. The record map pins the call summary's body: `## Call type`, `## Speakers`, `## Goals`, `## Pains`, `## Constraints`, `## Signals`, `## Entities`, `## Current tools`, `## Figures`, `## Open questions`, `## Agreed`, `## Commitments`, `## What the input cannot see`, `## Conflicts` when there is one, and `## Client-safe block` last. The document snapshot's body is pinned the same way, with `## Sections` first. A test checks that each template's headings follow the pinned order.
9. **`meetings.md`.** A new template (`meetings/1`: `schema`, `client`, `updated`), with `## Meetings` and `## Packages` and their line forms in comments. The record map pins the meeting line, `- <YYYY-MM-DD> · <call type> · calls/<stem>.md · client: <roles>; ours: the user · strands: <short ids> · <first-hand or handed-over>`, and the package line. The who-has-seen-what block is left out in v1, as the lean skill has it.
10. **The readiness headings.** The readiness pin now names the headings in order: `## Note`, `## Goals`, `## Pains`, `## Signals`, `## Entities`, `## Structure` with `### Leanings`, `### Patterns` and `### Element per pain`, `## Existing`, `## Assumptions`, `## Unmet needs`, `## AI opportunities`, `## Verdict` (holding `cleared_for`) and `## Questions`. A test checks the pin against the readiness guide's order. No script reads them yet; see the nod.
12. **The state word.** The call-type pin now reads `detected`, `assumed` or `confirmed`, `assumed` being the best guess intake carries on with (A27). `check` now reads the six type-header fields of a `call-summary/1` file: each must be `<value> <state>` or `unresolved`. `proposed`, the word first pinned, reads as `assumed` with no warning, so the three demo records stay clean. A missing field or another state word is a warning. Code: `TYPE_FIELDS`, `TYPE_STATES` and `Check.call_types()`.
13. **Signals stay in the body.** The record map says the front matter stays flat. Signals, an unresolved field's candidates and fallback, and any segments sit under `## Call type`. No front-matter field was added.
14. **A type correction keeps the stem.** The record map pins that a correction is written into the summary (the field becomes `confirmed`) and logged as a `call` entry keyed by the stem with no `path:` line, and that the raw file is never saved again under a new stem. `add-transcript` already refused the same bytes twice. Its refusal for a transcript now adds that a corrected type keeps the stem.
15. **What this build rests on.** The `STRAND.md` template gains `## What this build rests on`, after `## Headline and top pains`. It holds `- clearance: <the clearance string>`, `- assumptions: <n> in readiness.md, <n> structural`, then each structural assumption as `readiness.md` writes it, without its question. build-readiness owns it (ARCHITECTURE 3.3 has build-readiness write this block). Record map: section owners.
16. **`open-questions.md`.** A new template (`open-questions/1`: `schema`, `strand`, `updated`), with `## Open questions`. One line per question, numbered `Q1`, `Q2`, … and never renumbered: `- Q1: <the question> · kind: <kind> · state: <open | answered | bypassed> · who can answer: <role> · known: <what the record already holds> · source: <a file and its location, or a log header>`. A conflict's two statements sit under it, one indented `statement:` line each. The record map pins the line and adds the states `open` and `answered` beside `bypassed`.

## Stop

- **Point 4, partly.** `leak_lint.py` (`LOCATION`, two-digit hour) and `ledger.py` (`QUOTE_AT`, a live-map source) still read only `@HH:MM:SS`. Those files are not this group's. So `@MM:SS` passes `record.py check` but is not a location for the leak lint or for a live-map source. The record map therefore keeps the zero hour as the written form, and the skills should keep writing it. Widening the other two is a separate change.

## Nods

- *Nod (1):* the figure is one line per 30 words, between 120 and 250. Words were chosen over lines or speaker turns because they do not depend on how a transcript breaks its lines. Document snapshots keep 120: their raw file may be a PDF or an image, with no word count to read.
- *Nod (2):* `ledger.py bind` mirrors `build_target` and does not touch the reason. If a binding ever changes the target, the reason stays as it was until a skill rewrites it through the guard.
- *Nod (7, 9):* the record map names `## Sections` but not the email and image headings of a document snapshot (`## Messages`, `## Text of the image`, `## Attachments`). It also names the package block without its heading. Naming them would add words such as "messages", "attachments", "screenshot" and "packages" to the `shared/` vocabulary, which would make `leak_lint.py`'s shared-words region disagree with the folder and fail the plugin lint. That region belongs to another group. The templates and the intake shapes still carry those headings. They can be named in the map once the region is regenerated.
- *Nod (10):* no check reads the readiness headings. The two earlier demo records use older headings (for example `## Goals and pains`), so a heading check would warn on them.
- *Nod (12):* `proposed` is accepted with no warning, not with one, so the three demo records stay clean. Any other word warns.
- *Nod (15, 16):* the line forms of the two strand blocks and of `open-questions.md` are new. They follow the forms the summaries already use. The `open` and `answered` states are new beside `bypassed`.

## Lines the intake skills should change (main session)

call-intake, `SKILL.md`:

- "Writing the summaries", step 1: start each summary from the record template, `${CLAUDE_PLUGIN_ROOT}/templates/record/call-summary.md` for a call or `document-summary.md` for a document or an email, copied into `.work/staging/`. Replace "The budget is 120 lines" with "The budget is one line per 30 words of the saved transcript, at least 120 and at most 250 (120 for a document), a `record.py check` warning".
- Step 5: when the record has no `meetings.md`, start it from `templates/record/meetings.md` with `client` set to the slug, through the guard with `--expect-sha none`.
- Step 6: also write the call's open commitments under `STRAND.md`'s `## Open commitments`, one line each: `- <what> · owner: <role> · when: <date or unknown> · from: calls/<stem>.md`.
- "The call type": "Write each field as its value and `proposed`" becomes "… its value and `assumed`". Step 7's log line becomes `call_type <label> assumed`.
- "The call type", last sentence: log the correction as `record.py --record <folder> log --strand <id> --type call --key <stem> --line "call_type <old> to <new> · confirmed by the user"`, with no `path:` line. The stem stays.
- "The build target": `init` records `own-account` with its reason in `CLIENT.md` `build_target_reason`, and prints both.
- "Reading a call", locations: keep the zero hour. `record.py check` also reads `@MM:SS`, but the leak lint and `ledger.py` do not yet.

call-intake, `references/intake-shapes.md`:

- The front matter block: `"<value> assumed"` in place of `"<value> proposed"`. The paragraph after it: "`assumed` is the pinned word for the best guess intake carries on with; the user's correction makes it `confirmed`."
- Under each shape, one line: the call summary starts from `templates/record/call-summary.md`, the snapshot from `document-summary.md`, and `meetings.md` from `meetings.md`.

build-readiness, `SKILL.md`:

- Part 4, the build target: "`CLIENT.md`'s where it gives one" becomes "`CLIENT.md` `build_target_reason`, which `init` writes".
- "Writing and checking", step 3: also write `STRAND.md`'s `## What this build rests on`: `- clearance: <the string>`, `- assumptions: <n> in readiness.md, <n> structural`, then each structural assumption line as `readiness.md` writes it, without its question.
- When the full skill writes `solution/open-questions.md`, it starts it from `templates/record/open-questions.md`.

build-readiness, `references/readiness-guide.md`:

- The build target line: "reason: <from CLIENT.md `build_target_reason`, or: the record's default; …>".

## For `wp2/DECISIONS.md` (to paste, if the main session wants it there)

## Added by the intake fold, 2026-10-22

- **A call summary's budget grows with its transcript (demo 3 intake fold, 1).** `check` gives `calls/<stem>.md` one line per 30 words of `calls/<stem>.transcript.txt`, at least 120 and at most 250, and 120 with no transcript. It stays a warning. Reason: a full discovery call no longer fits 120 lines now that every pain and entity takes its own line. Follow-up: none.
- **`client/2` gains an optional `build_target_reason` (2).** `init` writes the default's reason and prints the target and the reason. `check` reads a record without it as having none, so the schema stays `client/2` (G57). Reason: the readiness check copies the reason from `CLIENT.md`. Follow-up: `ledger.py bind` does not rewrite it.
- **`check` reads `@MM:SS` (4).** Reason: files whose lines carry minutes and seconds. Follow-up: `leak_lint.py` and `ledger.py` still read a two-digit hour, so the zero hour stays the written form.
- **`check` reads a call summary's six type-header fields (12, 13).** Each is `<value> <state>` (`detected`, `assumed`, `confirmed`) or `unresolved`. `proposed` reads as `assumed`. Anything else is a warning. Reason: A27 names the state `assumed`, and records written with `proposed` must still pass.
- **A corrected call type keeps the stem (14).** `add-transcript`'s refusal of bytes already saved says so for a transcript. Reason: a raw file is saved once.

## Gates

Commands from the plugin root with `$env:PYTHONDONTWRITEBYTECODE='1'`. The brief's form, `py -3.x -m unittest tests.unit.test_record tests.unit.test_record_part2 tests.unit.test_lint_plugin`, cannot import `test_record_part2` (it imports `test_record` by its bare name), so each run set `PYTHONPATH` to `tests\unit` as well.

| Where | Python | Result |
|---|---|---|
| Scratch copy, patch applied | 3.9 | 146 tests, OK, 1 skipped (as before: 129 before, 17 added) |
| Scratch copy, patch applied | 3.14 | 146 tests, OK, 1 skipped |
| Real tree, patch not applied | 3.9 | 146 tests, OK, 11 skipped (the 10 pin tests and the earlier one) |
| Real tree, patch not applied | 3.14 | 146 tests, OK, 11 skipped |
| Both | 3.14 | `tools\lint_plugin.py --root .`: 0 errors, 1 warning (no personal-names list), 4 not present yet |

Tests first: the six code tests for points 1, 2 (two), 4, 12 and 14 failed before the change. The template test for points 7, 9 and 16 passed from the start, because the templates were written before it.

The record map's words were checked against `leak_lint.py`'s shared-words and shared-phrases regions after the edit: no word or phrase added or lost.

The whole suite in the scratch copy (3.14, `discover -s tests/unit`): 699 tests, one failure, in `test_leak_wall.py` (`test_G11_R42_X27_…`, the word "handover"). It is not from this group. "handover" is in `leak_lint.py`'s shared words through the tree's uncommitted change to `shared/monday-gotchas.md`, which was there when the copy was taken.

No `__pycache__` was left in the scratch copy, the plugin tree or the client records.

## The three demo records

`py -3.14 plugins\monday-master-builder\scripts\record.py --record <record> check`, with `MMB_HOME` set to the development home, read-only, once with the scratch copy's `record.py` and once with the real tree's: each of the three records gives exit 0, no blocking finding and no warning. Demo 3's call summary carries `proposed` in all six fields and is 120 lines against its new budget of 202.
