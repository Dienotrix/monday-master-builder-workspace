# BUILD-PLAN touch-ups from WP2, 2026-10-16

| Anchor | Decision | Outcome | Change |
|---|---|---|---|
| BP:23 (section 0) | G14 | applied | the three A11 signals named: `sample_rows: "planned"` on a client-account build, a `fixture: no` save entry, a `sandbox` account kind without a line in `sandbox-accounts.txt` |
| BP:123 (WP2), break flags | G04 | applied | "all five conditions" → also names the flags `--label`, `--epoch`, `--for-strand`, `--user-yes`, `--account-id`, `--choice`, `--park-yes` |
| BP:123 (WP2), strand resume | G05 | applied | `strand list` and `strand pause` → plus `strand resume`, the only writer from paused to active, after recovery ends its run |
| BP:123 (WP2), `--update` | G33 | applied | "never overwrites a settings file that exists" → "... unless `--update` names the answer to change" |
| BP:123 (WP2), `env` entry | G35 | applied | "walkthrough sets in the environment" → records, with the user's yes, an `env` entry in the Claude Code user settings |
| BP:123 (WP2), `SANDBOX.md` | G58 | applied | `sandbox/` → `sandbox/` with `SANDBOX.md` placed from the template |
| BP:123 (WP2), G23 answer | G23 (settled 2026-10-15) | applied | purpose sentence + "so a sign-off of a `v0.x` leaves it a proof of concept and `v1.0` is opened next as one more iteration of the same strand" |
| BP:134 (WP3), bytecode | G49 | applied | new bullet: `sys.dont_write_bytecode = True` first after `import sys` in `ledger.py` |
| BP:134 (WP3), mutex and JSON form | G09, G11 | applied | new bullet: every `account.json`, `build.json` and lock access inside `mmb_common.record_mutex`; JSON written in `record.py`'s form |
| BP:134 (WP3), post-commit failures | G09 amended (R4) | applied | same new bullet: `ledger.py` reports post-commit failures as exit 3, field `committed`, top-level `committed` object |
| BP:134 (WP3), `bind` | G15 | applied | "writes `account.json.account` from the binding document" → "..., with `bound_at`" |
| BP:134 (WP3), run start and fence | G50, G51, G51 amended | applied | "every write refreshes the lease heartbeat" → `run start` refreshes with its run id before any fenced write; every account-affecting write calls `lease_fence` first (moves the heartbeat, no separate refresh); an unrunnable fence is a stop; later decision replaced the old refresh-on-every-write text |
| BP:138 (WP3), reconcile | G04 | applied | classes written as findings → also as the interrupted run's `reconcile` object (`at`, `mode`, `classes`) |
| BP:157 (WP4) | G49 | applied | acceptance now opens with `sys.dont_write_bytecode = True` first in `leak_lint.py` |
| BP:167 (WP5) | G49 | applied | new first acceptance bullet: both transcript scripts set `sys.dont_write_bytecode = True` first |
| BP:296 (WP12), bytecode | G49 | applied | `archive_check.py` sets `sys.dont_write_bytecode = True` first |
| BP:296 (WP12), `.gitattributes` | G60 | applied | GitHub path: record also carries a `.gitattributes` of `* -text` |
| BP:305 (WP13), mutex and bytecode | G09, G49 | applied | "reads the record's lock only" → "..., under the record mutex, or treats a torn read as a refusal"; `guard.py` sets `sys.dont_write_bytecode = True` first |
| BP:305 (WP13), test_guard | G30 | applied | `test_guard.py` also proves a stale native index downgrades guarded writes to an ask |
| BP:198 (WP7), keys record.py sets | G31 | applied | added "every template carries each front-matter key that `record.py` sets in it" |
| BP:198 (WP7), readiness.md | G21, G28 | applied | assumptions get the line form `- <statement> [kind: ...; state: ...]` plus `  question:` line; clearance also in front matter as `clearance`, `none` until the check has run |
| BP:198 (WP7), version.md and audit.md | G27 | applied | version.md body headings named (`## Scope`, `## Build`, `## Reactions`, `## Events`); audit.md headings and last-line verdict added |
| BP:198 (WP7), blueprint.md | G29 | applied | blueprint carries `sample_rows`, shipped `"none"` |
| BP:198 (WP7), purpose wording | G23 as settled and refined | applied | "proof of concept until sign-off" → "below `v1.0`", since a later decision says a sign-off of a `v0.x` leaves it a proof of concept (not on the owed list; kept consistent) |
| BP:207 (WP8), first-run.md | G32, G35 | applied | connector check now made by the session, `home init` checks Python; adds the offer of the `env` entry with the user's yes |
| WP8 first-run walkthrough | Added by lease fixes (R11) | applied | adds the one-environment rule of `shared/safety.md` section 8 (one OS environment writes a record at a time; record home outside a cloud-synced folder) |
| WP8 (`versions.md`), v1.0 | G23 refined 2026-10-15 | applied | "proof of concept until sign-off" → "below `v1.0`"; adds the front door proposes `v1.0` when the sale closes, and `v1.0` continues the same strand and workspaces from the last `v0.x` |
| BP:244 (WP9) | G29 | applied | `solution-blueprint` also sets `blueprint.md` `sample_rows` to `planned` when the revision plans sample rows, else `none` |
| BP:248 (WP9, `recovery.md`), flags and resume | G04, G05 | applied | passes the choice to `lease break` with its flags; calls `strand resume` after `run end` |
| BP:248 (WP9, `recovery.md`), new run | G51 amended | applied | adds: the resume path opens a new run and never re-enters the broken lease's run id |
| WP9 briefing line (`reserved_for`) | R1 (lease fixes) | applied | WP9 holds no briefing line; the briefing order lives in WP8's `routing.md`, so "held lease named with ..." gained "and a broken lease with the strand it is kept for (`reserved_for`)" |
| BP:487 (H20) | G30 | applied | "a stale native index downgrades guarded writes to an ask" → `check` reports it as a warning; the downgrade is WP13's, owned by `test_guard.py` |
| BP:502 (H35), epoch | G03 | applied | "002 holds epoch + 1" → "002 holds the broken epoch + 2" |
| BP:502 (H35), reservation | R1 (lease fixes) | applied | resume-first: the break keeps the lease for 001 (`reserved_for`) and every other take is refused until that one |
| BP:524 (H57) | G32, G33 | applied | Python check by the script, connector checked by the session (WP8's half); two doors marked WP8's half; second run "keeps the settings ... unless `--update` names an answer to change" |
| BP:533 (H66) | G23 as settled and refined | applied | purpose "proof of concept before the event" → "below `v1.0`, so the event leaves a `v0.x` a proof of concept", and `v1.0` continues the same strand and workspaces |
| BP:207 (WP8), two doors | G32 | already present | first-run.md already explains the two doors; only the connector and `env` parts changed (see above) |
