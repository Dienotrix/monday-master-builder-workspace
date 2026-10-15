# Shared files — fix pass changes

Editor's log, 2026-10-13, the shared-files step of the fixture fix pass. Authority: `rebuild-workspace/design/stage-1b/PLAN.md` sections 2 (D1, D3, D5, D6, D11, D24) and 7, `build-readiness-spec.md` sections 2, 7 and 9, amendments A19, A21 and A22, and the brief's section 3 for the field names. No fixture, COVERAGE row, FEEDBACK entry, HANDOFF or design document was touched. Nothing was committed.

Starting state: the repository already carried two uncommitted edits from an earlier step of the same day, the removal of the archive owner's handle from `record-map.md` (the slug line) and from `leak-terms.txt` (the `<the handle>` line under the firm class), plus edits to four files under `tests/` that are not mine. Both earlier edits are kept; the diffs quoted below are against the last commit, so they show those lines too. The lint and the unit tests passed before any change here (0 errors, 31 tests).

## 1. `shared/record-map.md`

Edited by a script that replaced each anchor exactly once and refused to run otherwise, so nothing outside the listed spans moved. 254 lines before, 281 after.

- **Pinned section added.** `## Pinned: readiness`, placed directly after the strand-file vocabularies paragraph and before `## Pinned: call-type-vocabulary`, so the v1 vocabulary follows the v2 lists it replaces. It pins `readiness/1` field by field, with the names and value sets of brief section 3 exactly: `schema`, `note`, `pains[]` (`id`, `quote`, `location`, `speaker_role`, `stated_or_excavated` with `stated` or `excavated`, `outcome`), `signals[]` (`quote`, `location`, `pain`, `not_confirmed`), `entities[]` (`name`, `parent`, `moves_independently` with `yes`, `no` or `unknown`, `shared_resource`, `goes_stale`, `source` with `spoken`, `observed`, `documented` or `assumed`, `evidence`), `structure` (`products[]` of `Work Management`, `CRM`, `Service`; `build_target` of `own-account` or `client-account`; `build_target_reason`; `workspaces[]`; `native_reuse`; `leanings[]` of `question`, `option`, `quotes[]`, `locations[]`, `condition`, `pattern` with `fork`; `patterns[]`; `element_per_pain[]` of `pain`, `element`, `verdict` with `fixes`, `copies-today's-tool` or `none`), `existing` (`account`, `incumbents[]` of `system`, `authority`, `evidence`), `assumptions[]` (`statement`, `question`), `unmet_needs[]` (`need`, `clock`, `why_not_met`), `ai_opportunities[]` (`pain_or_need`, `kind` with `agent`, `ai_column`, `workflow`, `vibe_app` or `sequence`, `round` of `1` or `2`, `probe_basis` with `P-19`, `P-20`, `P-21` or `unprobed`, `idea`), `verdict` (`cleared_for` with `build`, `build-generic` or `none`, `conditions[]`, `reason`) and `questions[]` (`text`, `kind` with `read-back` or `discovery`, `role`, `known`). The closing paragraph gives the three machine values and their human strings, `cleared to build`, `cleared to build, generic` and `not yet`, each with the condition from the brief and the spec, the approval-card rule for the generic case (spec section 8) and the blueprint's reading of `none` (D1, D2). The section says that no script embeds it yet, so the lint does not check it; the lint's `PINNED` tuple names only the two existing sections, and the lint's own parser was run over the new heading to confirm it reads cleanly (112 backticked tokens, the clearance values and strings among them) and that the two checked sections still end at the right headings.
- **Strand table.** New row directly after `SUMMARY.md`: `` `readiness.md` | current | build-readiness | 200 lines | no | yes ``.
- **Deferred rows tagged in place, nothing deleted.** `discovery.md` (v2, writer discovery-check tagged v2), `solution/gaps.md` (v2, "demo-script (v2) reads it"), `versions/<v>/demo-script.md` (v2, writer demo-script tagged v2), `versions/<v>/export.md` (v2-or-v3, writer client-sop tagged v2-or-v3), `sop/SOP.md` and the `sop/diagrams/` row (v2-or-v3, writer tagged), `drafts/<date>-recap.md` (v2; the admin-prerequisites file in the same row stays v1 and the writer cell now says which is which), `deliverables/<v>/*` (v2-or-v3, writer tagged). A legend paragraph directly after the table says what the tag means (A19, D5), that the files behind the tags live under `deferred/`, and that `readiness.md` takes the place of `discovery.md` in v1 wherever the file lists the strand files a chat reads or a strand holds (D1), which covers the non-platform paragraph and the reading contract without editing either.
- **Vocabularies tagged.** In the strand-file vocabularies paragraph: `gaps.md` states (v2), `discovery.md` grades (v2) with the owner of their definitions now cited as `sales-method.md` under `deferred/shared/`, and the recap draft's `status` (v2); a closing sentence points at the readiness pin. In `strand/1`, `discovery_verdict`'s value list is tagged as a v2 grading list kept for the shape, with the v1 clearance named as `readiness.md`'s `verdict.cleared_for`.
- **small-group widened** (D3) in the paragraph under the call-type pin that defines a group: "a group, the small-group value, is two or more client attendees, below the large-room threshold, so a call with two client attendees is small-group". The reference to the calibration lesson that held the old "more than two" went with the old wording. No backtick was added inside the pinned section, so the token set the lint will compare with `transcript_prep.py` is unchanged (55 tokens).
- **Paths outside the record.** One sentence added after the `personal-names-index.json` item: the user's own entries live under `local/` (A22, D11): `settings.json`; `sandbox-accounts.txt` with its syntax recorded in full, one entry per line, `#` for a comment, fields separated by ` | ` in the order `kind | account_id | account_slug | workspace_id | label | note`, `kind` one of `sandbox` and `never-demo`, `workspace_id` one id or `*` for the whole account, the account host `<account_slug>.monday.com` so a match is on slug as well as id; and `leak-terms.txt` for the per-user additions, where the firm name and its renderings live. The sentence ends "Nothing user-specific ships in `shared/`."

Seen and left alone, because the task said to change nothing else; for the planner, each one line: the file's intro still says the lint asserts "the two pinned sections" (there are three now, one unchecked, and the new section says so itself); the `MMB_HOME` default still reads `~/DelOps` where D11 makes it `~/monday-builder/`; `deliverables/handoff/*` is v2-or-v3 by D15 but is not in the task's list, so it is untagged; the strand index example and the `STRAND.md` owner block still carry the discovery-check verdict; the version states still carry `demoed` (D2's `shown`); the paths paragraph still lists `leases.json` and `claims/` (D10, D13) and the scripts table still lists `gql_guard.py`, `sop_tools.py` and `demo_check.py` (D7, D16); the Migration section stands (D8). None of these is a fix-pass item in PLAN section 7.

## 2. `shared/leak-terms.txt`

198 lines before, 194 after. Under `class: firm` the phonetic rule, its three whitelist lines, the four renderings and the two comment blocks were removed; the class now holds one comment saying the user's own firm name and its renderings, with any `phonetic:` rule and `whitelist:` lines, come from `local/leak-terms.txt` under `MMB_HOME`, written by the first-run walkthrough from `local/settings.json`, that nothing user-specific ships in the file (D24, A22), and that the GitHub account and monday account names are held by `local/settings.json` and `local/sandbox-accounts.txt`. The header's first sentence no longer lists "the consultancy's name in its renderings" among the shipped terms and says where they come from instead; the paragraph was re-wrapped to the file's line length. The syntax block still documents `phonetic:` and `whitelist:` because the local file uses them. Every other class is byte for byte as it was. Left alone and noted: the `class: method` comment still says `sales-method.md` is the home of the criterion list, and that file is now under `deferred/shared/`; the task kept the other classes as they are, so the comment stands and the planner may re-point it with the method class when v2 is scheduled.

## 3. `deferred/` created; two files moved

`deferred/README.md` written: what the folder is (v2 and v2-or-v3 files kept, no skill built, never shipped; outside the token count, the lint and the release checks), why it exists (A19, D5), a table of what is in it with the layer and the former path, the note that both files moved unchanged on 2026-10-13 so their internal `shared/<file>` paths mean the shipped folder as of that date, the layout later deferred skills, templates and scripts will use, and the rules that still apply (fictional or generic only; the lint and the agnostic sweep before any promotion back). `git mv` moved `plugins/monday-master-builder/shared/sales-method.md` and `house-style.md` to `deferred/shared/`; git records both as renames with no content change.

## 4. `shared/sandbox-accounts.txt` retired

`git rm` after the syntax was recorded in `record-map.md` (section 1). The shipped file held no entries, so nothing user-specific was lost; its two explanatory blocks (the [A11-1] note and the never-demo definition) live on in `safety.md`, which is not mine and still cites the file by its old path (see section 7).

## 5. The clean-room scan retired (D6)

`git rm` of `tools/cleanroom_scan.py`, `tests/unit/test_cleanroom_scan.py` and the four files under `tests/unit/fixtures/tools/cleanroom/` (the folder went with them); the stale `__pycache__` folders under `tools/` and `tests/unit/` were deleted so no compiled copy lingers. `tools/README.md` rewritten: the intro names only `test_lint_plugin.py`, and the scan's section is now "The clean-room scan (retired 2026-10-13)", giving the reason (the quarantined corpus it compared against no longer exists; the clean-room rule itself stands) and saying that the agnostic sweep, `tools/agnostic_sweep.py`, arrives in stage 2 as release check 8 with the six things D6 says it fails on. The `lint_plugin.py` section is unchanged. 36 lines before, 20 after.

## 6. Lint and tests

Neither the lint nor a test assumed a moved or removed file, so no compensating change was needed: the lint's only shared-file check (`shared-copy`) iterates whatever is under `shared/`, its link check reads Markdown links and `${CLAUDE_PLUGIN_ROOT}` paths and the remaining references to the moved files are backticked prose, and the lint tests run against their own synthetic trees. The unit count fell from 31 to 21, the ten retired scan tests.

`python3 tools/lint_plugin.py`, from `~/DelOps/monday-master-builder-dev/monday-master-builder`, exit 0:

```
info: skills/: frontmatter: not present yet
info: agents/: frontmatter: not present yet
info: templates/: template-id: not present yet
info: templates/record/scope.md: handoff-sentence: not present yet
info: scripts/transcript_prep.py: pinned-agreement: not present yet (call-type-vocabulary unchecked)
info: scripts/transcript_measure.py: pinned-agreement: not present yet (permitted-constants unchecked)
warning: personal-names-index.json: personal-name: name list not found at /Users/caramelm4/DelOps/personal-names-index.json; check not run
lint_plugin: 0 error(s), 1 warning(s), 6 not present yet, 7 file(s)
```

`python3 -m unittest discover -s ~/DelOps/monday-master-builder-dev/monday-master-builder/tests/unit`, from the same folder, exit 0:

```
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.047s

OK
```

## 7. For the owners of files I do not hold

- `shared/safety.md` (lines 27, 41, 147, 179) and `shared/monday-gotchas.md` (line 397) still name `shared/sandbox-accounts.txt`, `shared/sales-method.md` or `house-style.md` by their old paths, as backticked prose. The lint passes because they are not links; stage 2's agnostic sweep fails on a reference to a retired file, so WP1's owner should re-point them to `local/sandbox-accounts.txt` and `deferred/shared/` before that check runs.
- `tests/stage1-acceptance-*.md` and `tests/stage0/*` record the scan's runs as history; left as they are.

## 8. Paths created, moved or removed

Created:
- `~/DelOps/monday-master-builder-dev/monday-master-builder/deferred/README.md`
- `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_fixpass/shared-changes.md` (this log)

Moved (`git mv`):
- `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/sales-method.md` → `~/DelOps/monday-master-builder-dev/monday-master-builder/deferred/shared/sales-method.md`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/house-style.md` → `~/DelOps/monday-master-builder-dev/monday-master-builder/deferred/shared/house-style.md`

Removed (`git rm`):
- `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/sandbox-accounts.txt`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/tools/cleanroom_scan.py`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/tests/unit/test_cleanroom_scan.py`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/tests/unit/fixtures/tools/cleanroom/` (four files: `quarantine/learn-notes.md`, `tree/allowed.md`, `tree/clean.md`, `tree/copied.md`)

Edited in place:
- `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/record-map.md`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/leak-terms.txt`
- `~/DelOps/monday-master-builder-dev/monday-master-builder/tools/README.md`
