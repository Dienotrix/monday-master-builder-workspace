# ARCHITECTURE touch-ups from WP2, 2026-10-16

| Anchor | Decision | Outcome | Change |
|---|---|---|---|
| A§5.2 (was 336) | G36 | applied | "WP2 fixes the one form both share" → scripts find the plugin from their own path; only the interpreter command waits for the Windows re-run |
| A§5.3 (was 340) | G11 | applied | new bullet: composed text UTF-8, LF, no BOM; raw files and frozen copies are byte copies |
| A§5.3 (was 343) | G10, G09 amended (R4) | applied | exit-code bullet gains: refusal exits 1, usage error 3, `status` 0 when it printed; exit 3 may carry `committed` |
| A§5.3 (was 345), MMB_HOME | G35 | applied | walkthrough records `MMB_HOME` as a Claude Code settings `env` entry with the user's yes |
| A§5.3 (was 345), CLAUDE.md | G37 | applied | "any folder above `clients/`" → "from the home folder up to the root of the drive" |
| A§5.4 mmb_common row (was 353) | G51 | applied | lease primitives gain sync, repair and `lease_fence` (the one epoch, label and run comparison) |
| A§5.4 record.py row (was 354) | G05, R5, R6 | applied | catalogue gains `strand resume`, `lease sync`, `lease repair` |
| A§5.4 record.py row | G08 | applied | "history files only grew" → "the log only grew" |
| A§5.4 record.py row | G22 | applied | `signed-off` described with `--go-on`: no record without it while the list is non-empty |
| A§5.4 record.py row | G25 | applied | `version open`, the condense pair, `strand list`, `card` described |
| A§5.4 record.py row | G27, G30 | applied | missing required file warns except at `released`, where it blocks; sentence on blocking versus warning severities |
| A§5.4 record.py row | G32 | applied | `home init` leaves the connector to the session; no longer checks it |
| A§7.1 `.work/` paragraph (was 437) | G08, G09, G39, G46; G09 amended (R4); R5, R6 | applied | adds `record.mutex`, defines `history.json`, drops per-strand `backup/`, lists `condense-plan.json` and `summary-plan.md`; user clears `.work/backup/` only; exit 3 may carry `committed`; `lease sync`, `lease repair` and the `repaired` event |
| A§7.2 (was 468), A§7.3 (was 524), A§7.3 (was 559) | G01 | applied | example labels `build v0.1 Tue` and `build v0.2 Thu` → minted labels `20261015-1330-k7q2` and `20261015-0910-m3x8` (the A§9.8:939 example follows with 9.8) |
| A§7.2 (was 481) | G06 | applied | strand index owner "engagement" → `record.py`, read by every skill |
| A§7.3 (was 493) | G15 | applied | example `account` gains `"bound_at"` |
| A§7.4 (was 587) | G23 as answered and refined by the user, 2026-10-15 | applied | "`v1.0` means the client has signed off..." → `v1.0` is the working solution, proposed when the sale closes; continues the same strand and workspaces as one more iteration (8.9 continue rule), never a fresh build; open assumptions listed to confirm; a `v0.x` sign-off leaves it a proof of concept |
| A§7.4 (was 598) | G27 | applied | "Missing files block the release" → a missing file warns in every other state and blocks at release |
| A§7.4 (was 610), A§7.6 (was 645) | G08 | applied | roll moves the strand's entries, at a release those of the released version (7.6 now names both destinations); the `lease` log type also lists `repaired` |
| A§7.7 (was 682) | G43 | applied | adds the `output_class` defaults of `strand open` |
| A§7.7 (was 684) | G42 | applied | "takes the user's yes to a plan" → two steps, `--plan` then `--apply` with the sha after the user's yes |
| A§7.7 (was 686), A§8.11 (was 836) | G05 | applied | both: `record.py strand resume` returns the strand to `active` after the run ends |
| A§8.2 (was 745) | G32 | applied | script no longer checks the connector; the session does |
| A§8.3 (was 758) | G14 | applied | `add-transcript` and `add-document` refuse a non-fixture input while A11-3 is open |
| A§8.3 (was 759) | G13 | applied | save entry named, with its lines |
| A§8.3 (was 768) | G13 | applied | `--came-with` named, refused unless the target was saved as an email |
| A§8.4 (was 772) | G06 | applied | strand index update goes through `record.py guard` on `STRAND.md` |
| A§8.5 (was 785) | G41 | applied | `freeze` reads `revision` from `version.md` and writes its `sha256` |
| A§8.8 (was 815) | G20 | applied | `version mark shown` flags given in full (`--date`, `--audience`, `--account`, `--words`) |
| A§8.8 (was 817) | G20, G22, G23 (user's refinement, 2026-10-15) | applied | `signed-off` flags in full and `--go-on`; "which is what `v1.0` means" → a `v0.x` sign-off leaves it a proof of concept, `v1.0` is proposed when the sale closes and continues the same strand and workspaces as one more iteration (8.9), open assumptions listed to confirm |
| A§8.10 (was 828) | G07 | applied | `close_reason` lives in `version.md`; the last three steps with the refusals are `record.py strand close`, the rest stay with `client-closeout` |
| A§8.10 (was 830) | G25 | applied | `record.py card` does the copy to `<home>/cards/` |
| A§8.11 (was 836) | G05 | applied | see the 7.7 row: `strand resume` named in 8.11's last sentence |
| A§9.8 (was 933), label | G01 | applied | label built from "a timestamp and a short random suffix" → `YYYYMMDD-HHMM-xxxx`, redrawn until unique in the history |
| A§9.8 (was 933), run_id | G50 | applied | new sentence: a take leaves `run_id` null; the first refresh after `ledger.py run start` sets it |
| A§9.8 (was 933), carry rule | R12 option (a) | already present | carry-rule sentence left as instructed |
| A§9.8 (was 939) | G01 | applied | briefing example label `build v0.1 Tue` → `20261015-1330-k7q2` |
| A§9.8 (was 943) | G48; G51 amended (R2, R3, R9) | applied | "refreshed on every ledger write" → every account-affecting write first passes the fence, which needs a run and moves the heartbeat before the write; `check` reports a stale lease as a warning |
| A§9.8 (was 945), flags | G04 | applied | break's flags named: `--label`, `--epoch`, `--for-strand`, `--user-yes`, `--account-id`, `--choice`, `--park-yes` |
| A§9.8 (was 945), epoch | G03 | applied | "starts at `epoch + 1`" → the break raises the epoch by one and the next take again, so the new holder holds the broken epoch + 2 |
| A§9.8 (was 945), reservation | R1 | applied | the break keeps the lease for the strand its choice names; every other take refused; `reserved_for`; lapses when that strand is closed |
| A§9.8 new paragraph | R6 (G39 amended) | applied | "When the lock itself is lost": `lease repair`, the `repaired` event, the epoch above every known epoch, `broken` or `released` |
| A§9.10 (was 955) | G09 | applied | `guard.py` reads the lock under the record mutex, or treats a torn or unparsable read as a refusal |

## Check, 2026-10-16 (main session)

Every edit in both logs was read against its decision in DECISIONS (G01, G03 to G05, G08 to G11, G13 to G15, G20 to G23, G25, G27 to G30, G32, G33, G35, G36, G41 to G43, G46, G48 to G51, G58, G60, and the lease fixes' R1 to R6). One fix:

| Anchor | Decision | Outcome | Change |
|---|---|---|---|
| A§5.4 `record.py` row, and A§8.8 step 31 | G22, A25 | fixed in check | "a warning that does not block: without `--go-on` it records nothing" read as a block → "a warning the user can pass rather than a block: without `--go-on` it shows the list and records nothing"; the same in step 31 |

Left as it was: the 7.2 and 7.3 examples show epoch 7 with label `20261015-1330-k7q2` for `001 v0.1` and with `20261015-0910-m3x8` for a `v0.2` run. One epoch has one label and one version, so the examples disagree, as the old descriptive labels did; a re-cut of the examples, not a touch-up, would settle it.
