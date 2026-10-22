# WP4 grading harness notes

Date: 2026-10-17. Internal build file: never client-facing.

The harness is `monday-master-builder/tests/unit/test_leak_grading.py`. It grades `scripts/leak_lint.py` against `tests/fixtures/leak/manifest.json`. It changes neither the fixture nor the lint, and `test_leak_fixture.py` is untouched.

## 1. How each case is built

Each case gets a fresh temporary folder (its name holds a space), with `MMB_HOME` pointed at the home inside it and `HOME` and `USERPROFILE` at an empty canary folder. The steps are the manifest's own `home.steps`:

1. copy the settings and the local list;
2. copy both records to `clients/<slug>`;
3. lay the case's overlay over record a, path for path;
4. run `index` from record b and then from record a (`--record <home>/clients/<slug>`);
5. install the case's files; a `zip` entry zips every file under its fixture folder with `zipfile`, member names relative and in POSIX spelling, into the `.docx` path;
6. run the case's command with `--record` and the manifest's `args`.

Nothing is written to the real home or to the fixture. The temporary folder is removed after the case. The run hashes every fixture file before and after and fails if one changed. A case with `unchanged` (R14) also compares its installed file's hash before and after the run.

## 2. How it calls the lint, and why

In process: `leak_lint.main(argv)` with `sys.stdout` replaced by an object with a `buffer`, so the envelope's bytes are captured, then parsed as JSON. The API note names `main(argv)` and the part-1 tests use the same pattern. A subprocess for 250 cases plus 500 `index` runs would be slow, and the in-process run has no state that carries between cases (every list is loaded per run). The script is loaded by path, so nothing is cached beside it, and the header sets `sys.dont_write_bytecode`.

## 3. What it asserts

Three tests. `test_manifest_counts_and_twins` checks 250 cases, 125 planted, 125 twins, each planted case's twin both ways, and the outcome totals (110 blocks, 3 warns, 1 caution, 11 limits, 125 passes) and command totals (168 scan, 80 payload, 2 blueprint). `test_index_builds_for_both_records` checks that `index` answers exit 0 from record b and then record a. `test_every_case` runs one `subTest` per case, labelled with the id:

- exit code and verdict exactly as the manifest says;
- planted: every `expect` entry matched by a finding of the same rule and severity, the same class where one is named, at the same place (the same `field`, the same `.docx` part, or a path under it); a block where the case blocks; other findings are not failed;
- twin: no block finding, and every `expect` entry (the warnings a twin is known to carry);
- known limit: exit 0, verdict clean, no block finding, so a later rule that catches the case shows up as a failure to look at;
- no case is skipped or marked as an expected failure.

On failure the message carries the lint's answer: exit, verdict, the error field if any, and the first findings.

## 4. Results

Run from `monday-master-builder/` with `PYTHONDONTWRITEBYTECODE=1`, as `python -m unittest tests.unit.test_leak_grading -v`.

| | Python 3.9.6 (`/usr/bin/python3`) | Python 3.14.6 |
|---|---|---|
| cases passed | 4 of 250 | 4 of 250 |
| cases failed, waiting for part 2 | 246 | 246 |
| cases failed for another reason | 0 | 0 |
| other tests | counts test passes; index test fails (part 2) | the same |
| run time | about 4.4 s | about 3.2 s |

After both runs, `find` shows no `__pycache__` anywhere under the workspace, a sorted `shasum` of every file under `tests/fixtures/` is identical before and after, and `git status` shows only the new test file.

The 4 passing cases are the summary-mode ones (R19-p, R19-t, R19b-p, R19b-t): X37 says summary mode does not run the wall and Z02 does not stop it.

## 5. The failing cases

All 246 fail for part 2, none for another reason.

- **244 cases, every case except the summary ones and the two blueprint ones.** Every home holds two records, and `index` is not built, so Z02 stops each check: exit 3, field `wall`, "the cross-client wall is not built in this version of the lint, and the home holds 1 other client record(s) or an index". The lint's current answer for each is exit 3, verdict could-not-run, no findings. Their ids are every case id of the manifest except R19-p, R19-t, R19b-p, R19b-t, R10c-p and R10c-t. (`test_index_builds_for_both_records` fails for the same reason: `index` answers exit 3, "not built yet".)
- **R10c-p and R10c-t** (blueprint): exit 3, field `blueprint`, "the blueprint command is not built yet". They need part 2's `blueprint`; the home stop would also apply.

To see whether anything besides part 2 is wrong, I ran every case once more in a scratch script, not kept, in a home with record a alone (no record b, no index), so Z02 does not apply. In that run 22 cases still disagree with the manifest, and every one is a missing `wall` finding or the blueprint command:

- a `wall` entry the lint cannot produce yet: T01-p, T02-p, T03-p, T05-p, T06-p, T07-p, T08-p, T14-p, T15-p, T16-p, T18-p, T19-p, T20-p, K30-p, K17-p (it also answers exit 2 where the manifest says 1), R18-p, P-group-p, P-publication-p, P-agent-p, P-item_batch-p, P-generic-p and D09-p. In each of them the rules part 1 owns (term, exclusion, figure, credential and the rest) matched, and only the wall entry was missing; the exit is 1 where another block stands, and 0 or 2 where the wall was the only block;
- R10c-p and R10c-t: blueprint not built.

So the manifest, the fixture and the lint's part 1 agree on every case that part 1 can answer: no finding of the harness's own.

## 6. Re-run when part 2 lands

The same command. Once the wall, `index` and `blueprint` are built, the 246 should pass or show a real disagreement. The API note had no "Part 2" section when this was written, so the harness assumes `index` takes no flags and answers exit 0.
