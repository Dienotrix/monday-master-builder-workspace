# WP2 build lease: adversarial review

Date: 2026-10-15. Internal build file: never client-facing. No code was changed.

Scope: `plugins/monday-master-builder/scripts/mmb_common.py` (the mutex, `heartbeat_age`, the lease primitives, the lock and its two mirrors) and the lease parts of `record.py` (`lease *`, `init`, `strand close`, `version release`, `check`), read against A§9.8, A§7.1, A§7.4, A§8.11, CONTRACT C82 to C113 and section 3.3, DECISIONS G01 to G05, G09, G48, G50 to G53 and the part-2 heartbeat rule.

Method: the repository suite passes (135 tests). Each finding marked "proved" was shown by a throwaway test run with `PYTHONDONTWRITEBYTECODE=1 /usr/bin/python3` on a copy of the unit fixture outside the repository (session scratch folder `lease_probe/`, probes P1 to P18 and R1 to R2; temporary, not kept). Failures on Windows were simulated by making `write_file` raise the `PermissionError` a sharing violation gives. Line numbers are as of this review.

Severity: **blocking** (fix before WP2 is accepted), **should fix** (fix in WP2 or before WP3 relies on it), **note**.

## Findings

### 1. A break does not decide who takes next, so the duplicate rule can be walked around (blocking)

- Where: `mmb_common.py:361-382` (`lease_take`) and `:422-455` (`lease_break`); `record.py:1447-1450` (the `next` hint is advice only).
- Scenario: strand 002 wants the lease; 001's lease is stale; the classify-only reconcile finds `duplicate 2, partial 1`. The user picks park; it is refused (C107). The user picks resume; the break succeeds and the lock goes to `broken`. The same session then runs `lease take --strand 002` and gets the lease. Nothing in `lease_take` reads the last history entry, so 002 now builds on an account holding 001's duplicates and partials, the exact state A§9.8 says a second builder can make unrecoverable. C111 ("the lease goes to a fresh session for the holding strand") and C112 ("the taker holds the lease") are stated but not enforced. The milder half: after a park for 002, the paused holder 001 can take first, which overrides the user's recorded choice (fail-closed for 002, but not what was decided).
- Proved: yes (P1: 002 took epoch 4 after a resume break whose reconcile found duplicate 2, partial 1; P2: paused 001 took epoch 4 after a park for 002).
- Smallest fix: in `lease_take`, when the lock is `broken`, read the newest history entries: after `broken` with choice `resume`, only the entry's `strand` may take; after `parked`, only the taking strand may take. The taking strand today lives only inside `note` (`for 002: "..."`); parse it, or (cleaner, a G02 amendment) add a `for_strand` key to the `broken` entry. `lease status` should show the reservation, so the briefing can say whose turn it is.

### 2. A null `run_id` on the lock is a wildcard for the fence and for refresh (should fix)

- Where: `mmb_common.py:477` (fence: `run_id not in (None, run_id)`), `:389-391` (refresh enters any run id while the lock has none), `:406-407` (`_reconcile`: no run id means nothing was written, so condition 4 holds with empty counts).
- Scenario A: the fence admits a write that presents any run id while the lock's `run_id` is still null, yet break condition 4 assumes that with a null `run_id` nothing can have been written, and waives the reconcile. If WP3 ever fences an account write before `run start` has entered the id (a crash between creating the `runs[]` entry and the refresh, or plain ordering), a later break skips the classify-only reconcile and a park is accepted with empty counts, so the duplicate check of C107 is vacuous. The two rules sit in the same file and contradict each other.
- Scenario B: after a resume break the fresh session takes (run id null). A woken old session that re-reads the lease from disk (finding 12 shows it is in both mirrors) presents the new epoch, the new label and its old run id: the fence says ok, and `lease_refresh` lets the old run id enter the new lease. The run-id part of the fence, which A§9.8 adds exactly for "a woken old session that re-read its ledger", only works once the new run has started.
- Proved: yes (P3: fence ok for `run-anything` with the lock's run id null, then a park break accepted with no reconcile at all; P4: the broken run's id accepted into epoch 4 by refresh).
- Smallest fix: the fence refuses while the lock's `run_id` is null (account-affecting writes happen only inside a run, after `run start`); `lease_refresh` refuses a run id already recorded in the history. The second assumes the resume path always opens a new run, which WP3 should confirm in `recovery.md`.

### 3. The fence does not move the heartbeat (should fix)

- Where: `mmb_common.py:468-479`; the C100 stand-in in `test_mmb_common.py:543-551` shows the intended use as fence, then refresh, two separate holds.
- Scenario: the holder's heartbeat is 60 minutes old (it waited on an approval). It passes the fence and starts a write. Two minutes later another session runs the classify-only reconcile over the holder's strand (stamped after the old heartbeat) and breaks with park; every condition holds. The holder's write lands after the reconcile read, so the reconcile never saw it and the taker builds over an unrecorded object. The break's protection ("a write after the reconcile moves the heartbeat past it") depends on the refresh happening before the write, in the same hold as the fence, and the primitive leaves that order to WP3.
- Proved: yes (P14: fence ok at 60 minutes, heartbeat unchanged, park break accepted two minutes later).
- Smallest fix: one call that fences and, when the fence passes, moves the heartbeat in the same hold (`lease_fence(..., refresh=True)`, or have `lease_fence` refresh always), and the WP3 contract says it runs before every account-affecting write.

### 4. A primitive that commits and then fails tells the session it failed (should fix)

- Where: `mmb_common.py:321-332` (`_commit` writes the lock first, then the mirrors); `record.py:1384-1390` (take, then the log insert), `:1414-1446` (break, then the park write and the log insert), `:1398-1403` (release, then the log insert).
- Scenario: on Windows a sharing violation on `account.json` or `log.md` (an editor, the sync client or an on-access scanner holding it) makes the write after the lock fail. For a take, the lock is now `held` by a minted label that was never printed: the session sees exit 3, a retake is refused as "another session of this strand", and the lease stays fresh and unusable for 60 minutes; the only ways out are a break or reading the label back from disk, which the carry rule forbids. For a break, the lock is `broken` at epoch + 1 and (on park) the holder is already `paused`, but the three `lease` entries of G03 are missing (C108, C109), and a retry is refused because the lease changed. For a release, the lease is free but the log has no entry.
- Proved: yes (P5: exit 3, lock held at epoch 3 by a label not in the output, retake exit 1, `check` blocking on both mirrors; P5b: the same after a committed take when the log insert fails; P11: lock `broken` epoch 3, holder `paused`, no `broken` entry in the log, retry refused on `epoch`).
- Smallest fix: when anything fails after the primitive returned or after the lock write, raise `CannotRun` whose finding carries what was committed: for a take the epoch and the label (so the session can release, or refresh to heal the mirrors); for a break the new epoch, the choice and the entries still to write. For the mirror-write failure inside `_commit` the same applies; writing the lock last instead would also avoid the orphan but not the log gap.

### 5. A mirror left behind by a failed write has no repair path (should fix)

- Where: `mmb_common.py:321-332`; `record.py:543-554` (`check` blocks on a mirror mismatch), `:1046-1048` (`guard` refuses any change to the `CLIENT.md` lease line); G09 says a crash between the writes "heals at the next take, refresh, release or break".
- Scenario: a release fails between the lock and the `account.json` mirror. The lock says `released`, both mirrors still name the holder, `check` blocks, and a retried release is refused because the state is no longer `held`. A refused call never reaches `_commit`, so only a successful take and release heals the mirrors. At record close (every strand closed) or on a record whose open strands are `non-platform` or have no version, no take is possible, `guard` refuses a hand fix of `CLIENT.md`, and `account.json` is not hand-editable by design, so `check` blocks for good and the record close, which needs `check` clean (safety.md section 1), cannot proceed.
- Proved: yes (P6: release exit 3, retry exit 1, lock `released`, `check` blocking `CLIENT.md lease` and `account.json guard_index.lease`). The "no take possible" half is by reading.
- Smallest fix: a primitive that rewrites both mirrors from the lock with the lock unchanged (`_commit` already does this) and a `record.py lease sync` that calls it; `check`'s expected text names it. G09's sentence becomes "at the next successful lease call, or `lease sync`".

### 6. A torn or missing lock has no way back, and G39 invites deleting it (should fix)

- Where: `mmb_common.py:327` (the lock is rewritten in place with `backup=False`), `:354-359` (`lease_init` refuses when the file exists, and only `init` calls it); DECISIONS G39 ("kept until the user clears `.work/` by hand"); A§7.1 calls `.work/` scratch.
- Scenario: Ctrl+C or a killed process between the truncating `open(..., "wb")` and the write leaves `lock.json` empty; or the user clears `.work/` to drop backups, as G39 says they may. Every lease command, `status` and `check` then exit 3; no backup of the lock exists; `init` refuses a non-empty folder. The epoch and the history (which the audit's independence check reads, A§9.8) are gone, and the only way back is a hand-written lock whose epoch the user must guess. Separately, on macOS, deleting `.work/record.mutex` while a session holds it lets the next opener lock a new file, so two holders run at once until the first releases.
- Proved: yes for the dead end (P7: exit 3 from `lease status`, `lease take`, `check` and `status`; zero lock backups; `lease_init` refuses the empty lock). The mutex-unlink case is by reading of flock semantics.
- Smallest fix: back up the lock on take, release and break, as the mirrors already are (refresh can stay without one); add a repair path that rebuilds a missing or unparsable lock as `released` at one above the larger of the `account.json` mirror's epoch and the newest lock backup's epoch, with that backup's history; reword G39 to "clears `.work/backup/`", never the whole `.work/`.

### 7. `lease take` uses denylists where G50 and G53 give allowlists (should fix)

- Where: `mmb_common.py:368-373`.
- Scenario: G53 allows a take "only when `state` is `none`, `released` or `broken`"; the code refuses only `held`, so a lock whose state is any other string is taken over. The strand checks refuse only `kind == "non-platform"`, `state == "closed"` and `version == "none"`, so a STRAND.md with the `kind` key missing or misspelt, a state of `Closed`, an empty version or a version with no folder all take the lease. `check` would flag the bad values, but nothing makes a session run `check` before a take.
- Proved: yes (P8: missing kind, `non_platform`, `Closed`, version `""` and version `v9.9` with no folder all taken; P16: lock state `Held` taken over at epoch 3).
- Smallest fix: allowlists: lock state in `none | released | broken`; kind in `platform | hybrid`; strand state in `active | paused`; version matching `v\d+\.\d+` with `versions/<v>/version.md` present.

### 8. Any locking error reads as "another writer held the record" after 30 seconds (should fix)

- Where: `mmb_common.py:255-268` (`except OSError` returns False for every failure on take).
- Scenario: `flock` raising `ENOTSUP` or `ENOLCK` (some network or FUSE mounts on macOS), or `msvcrt.locking` failing for a reason other than the region being locked, is treated as contention: every command waits the full 30 seconds and then says another writer holds the record. The real cause is never shown, and the user is sent looking for a second session that does not exist.
- Proved: yes (P10: `flock` patched to raise `ENOTSUP`; after the timeout, "another writer held the record").
- Smallest fix: treat only `EWOULDBLOCK`/`EAGAIN` (POSIX) and `EACCES`/`EDEADLOCK` (msvcrt) as contention; raise `CannotRun` naming the error for anything else.

### 9. A malformed lock makes the fence fail open and `check` crash (should fix)

- Where: `mmb_common.py:475` (fence compares the label without requiring one), `:428` (the break's compare-and-set does the same); `record.py:543-565` (`check` validates only `state` and the mirrors).
- Scenario: a held lock with `session_label` null (a hand edit or a partial restore after finding 6): `lease_fence(epoch, None)` returns ok, so a caller that lost its label passes. A held lock with `heartbeat_at` null: `check`, `status` and every take of any strand exit 3 with a `ValueError` instead of a finding, and no break is possible. `check` never validates the lock's shape (epoch an integer at or above every history epoch, a held lock's strand, label and heartbeat present and parseable, the label format, history a list).
- Proved: yes (P15: fence `(True, "ok")` with a null label; P9: `check` and `lease take` exit 3 with a null heartbeat).
- Smallest fix: the fence and the break's compare-and-set require a non-empty presented label, as `_require_holder` does; `check` validates the lock's shape as blocking findings, and `heartbeat_age` callers in `check` and `status` catch a malformed stamp and report it.

### 10. The heartbeat rule guards one clock direction only (note)

- Where: `mmb_common.py:65-72` (`heartbeat_age`), `:413-415` (condition 4 compares the reconcile stamp, from the breaker's clock, with the heartbeat, from the holder's); `record.py:564`.
- Scenario A, holder's clock behind by D minutes: the stale threshold shrinks to 60 − D, and beyond 60 a live, just-refreshed lease is breakable, with condition 4 satisfied because the two stamps come from two clocks. One machine has one clock, so this needs a second clock: a WSL2 session (whose clock is known to lag after the host sleeps) writing a record that native Windows also writes, or two machines on a synced folder (finding 11).
- Scenario B, clock stepped back more than five minutes on one machine (a large time correction after sleep): a fresh lease with no run yet reads as "not fresh: the clocks disagree", break condition 1 holds and condition 4 is waived, so it can be broken at once; the take refusal even suggests a break. The fence then refuses the holder's later writes, and nothing was written before `run start`, so the cost is a lost lease, not a double write. This is the trade the part-2 decision chose.
- Also: `check`'s expected text for a future heartbeat is missing a verb ("each machine that writes this record on the right time").
- Proved: yes, with the two clocks simulated by switching the patched clock (P12: heartbeat 13:20 written "now", breaker at 14:30, break accepted; P13: age −6, fresh false, break accepted).
- Smallest fix: read the lock file's modification time beside `heartbeat_at`: stale only when both are over 60 minutes old, and condition 4 needs the reconcile later than both. On one machine they agree; for a WSL2 writer on a Windows drive the modification time comes from the host clock. Fix the wording at `record.py:564`.

### 11. The mutex excludes only processes in one OS environment (note)

- Where: `mmb_common.py:255-268` and G09.
- Scenario: two sessions on one record from two lock mechanisms do not exclude each other: a WSL session (`fcntl.flock` over `/mnt/c`) and a native Windows session (`msvcrt` byte-range lock); a Python from MSYS2 or Cygwin (reports `posix`, emulated `flock`) and a python.org Python on the same Windows machine; two machines on a synced folder. Both read `released`, both take, both get the same epoch with different labels, and the fence passes on each side until the sync settles. D10's one question before the first write is the only guard left, and it relies on the user knowing about the other session.
- Proved: no (needs two environments).
- Smallest fix: state in `safety.md` section 8 and the first-run walkthrough that one record is written from one OS environment at a time, and keep the record home off synced folders; the Windows run below confirms the WSL case.

### 12. A session that lost its label has no legal path but a 60-minute wait, and the label is on disk in three places (note)

- Where: A§9.8:933 ("a session that has lost them ... runs resume, which takes the lease afresh"), G53 ("a session that already holds the lease ... never takes again"), `mmb_common.py:372` (a take is refused while held, same strand included).
- Scenario: after compaction the build session no longer has its epoch and label. It cannot refresh or release, a take is refused, and a break needs the lease stale for 60 minutes plus the user's yes. Meanwhile the label is in `CLIENT.md`, the epoch and label are in `account.json`'s mirror, and `lease status` prints both; with the run id still null they pass the whole fence (finding 2). The carry rule is the only thing between a forgetful session and reading them back.
- Proved: yes for the exposure (P18: fence ok with the epoch and label read from the `account.json` mirror).
- Smallest fix: a decision for the user: accept the wait and correct A§9.8's sentence, or allow a same-strand takeover (a break of a fresh lease by the holder's own strand, with the user's yes naming it). Finding 2's fix narrows the exposure either way.

### 13. A user-paused strand can take the lease (note)

- Where: `mmb_common.py:368-371`; G53 allows `paused` for the park path (G05).
- Scenario: `strand pause` (the user's own pause, with no interrupted run) leaves a strand that can take the lease and build while still `paused`; G53's reason covers only a parked strand.
- Proved: yes (P17: user-paused 001 took epoch 3, still `paused`).
- Smallest fix: accept `paused` only when the strand's `build.json` has an `interrupted` run (the park path).

### 14. Long reads under the mutex can time out a builder's heartbeat (note)

- Where: `record.py:461` (`check` runs under the mutex and hashes every raw input), `:1711-1758` (`version release` runs `check` twice under it); `MUTEX_TIMEOUT` 30 seconds.
- Scenario: on a record with large raw inputs, or on Windows with on-access scanning, a meeting session's `check` holds the mutex long enough that the build session's refresh exits 3. If WP3 treats a failed refresh as skippable, the heartbeat stops moving during a live build.
- Proved: no.
- Smallest fix: WP3 treats a refresh timeout as a stop, never a skip; optionally hash raw inputs before taking the mutex and re-check only their size and modification time inside it.

### 15. `init` checks for an empty folder before it takes the mutex (note)

- Where: `record.py:1918-1936`.
- Scenario: two `init` runs for the same slug at once both see an empty folder; the second, once it gets the mutex, overwrites the first's `CLIENT.md`, `log.md` and `account.json` (with backups) and only then is refused by `lease_init`, leaving a log that no longer holds the baseline's `created` entry.
- Proved: no (rare; by reading).
- Smallest fix: repeat the emptiness check inside the mutex, ignoring `.work/record.mutex`.

### 16. `shared/safety.md` section 8 still describes the old lease (note)

- Where: `plugins/monday-master-builder/shared/safety.md:103-109`.
- Scenario: it names `chat_label` and `surface` in the lock, a `--chat-label` flag, and a cross-client `leases.json` under the home that `lease take` writes; the code, G01, G02 and D10 have none of these. A WP3 or WP13 builder who reads `safety.md` first builds against the wrong shape. The G01 to G03 follow-ups already list this edit.
- Proved: not applicable.
- Smallest fix: apply the G01 to G03 follow-ups to `safety.md` section 8 before WP3 starts.

## Checked and holding

- Eight processes racing a take on one machine (macOS `flock`): exactly one winner, epoch + 1, the lock's label is the winner's (R1).
- A refresh and a break racing on a stale lease: serialised; one break wins, every later call is refused (R2).
- Epoch arithmetic follows G03: take + 1, break + 1, release unchanged, init 0; the history keeps every entry with the epoch of the lease it describes; nothing decrements it.
- Labels: re-drawn until unused in the history; compared as exact strings; refresh, release and break refuse a missing or different label.
- Breaks: the compare-and-set refuses a lease that changed; every failing condition is listed; park needs its own yes and refuses `duplicate` or `partial`.
- `version release`, `condense-plan` and `condense-apply` refuse while any strand holds the lease; `strand close`, `pause` and `resume` refuse while their strand holds it; all read the lock under the mutex.
- No code path in either file deletes or renames a file; the lock is a state change, never removed.
- A mirror that disagrees with the lock is rewritten by the next successful primitive call, and `check` blocks on it meanwhile.

## What a real Windows run must exercise

1. `test_C52_G09_mutex_serialises_processes` and `test_G09_mutex_is_reentrant_and_times_out` under a python.org Python: the `msvcrt` branch, a second handle in the same process refused, and the timeout path.
   Outcome (2026-10-16): passed under both Pythons. Four processes by 20 cycles ended at 80, and a second handle in the same process was refused after its 0.5-second timeout with exit 3.
2. The take race of R1 (eight processes) and the refresh-against-break race of R2.
   Outcome: passed under both. One winner of eight, epoch 3, mirrors agreeing; the refresh against the break was consistent in 3 of 3 rounds.
3. A process killed with `taskkill /F` while it holds the mutex: time how long until another process gets it (Windows releases such locks "depending on available resources").
   Outcome: passed under both. The harness killed the holder with `Popen.kill()` (TerminateProcess, as `taskkill /F` does), and another process had the mutex 0.06 seconds later under 3.9 and 0.05 under 3.14, well inside the 30-second mutex timeout.
4. Unlock after the body raised: `seek(0)` then `LK_UNLCK` must not raise, so an error inside the hold is not masked.
   Outcome: passed under both. The error reached the caller unmasked, the mutex was free in and out of the process at once, and unlocking after the file position moved did not raise.
5. Sharing violations during take, release and break: hold `account.json`, `CLIENT.md` and `log.md` open with no write sharing (a small `CreateFileW` call with share mode 0 is enough) and record the output; this is findings 4 and 5 on real Windows.
   Outcome: passed under both; every command answered with one JSON object. With share mode 0 on any of the three files, or writes denied on `account.json` or `CLIENT.md`, the command exited 3 with the lock unchanged, and a retry after the hold closed succeeded. With writes denied on `log.md`, the lease change committed and the exit 3 carried `committed`, as finding 4's fix intends; a retry was then refused (exit 1) because the change had already happened, and `lease sync` left the mirrors agreeing.
6. A record home inside a OneDrive-synced folder: take and refresh during an upload.
   Outcome: not run; it needs a person and was optional. `safety.md` section 8 already keeps the record home out of a synced folder.
7. Ctrl+C in a Windows console during `lease take`: the state of `lock.json` afterwards (finding 6).
   Outcome: not run; it needs a person and was optional.
8. A WSL session and a native session on the same record under `C:\`: confirm the two mutexes do not exclude each other (finding 11), and read the WSL clock against the host after the machine sleeps (finding 10).
   Outcome: not run; it needs a person and was optional. Findings 10 and 11 stay as kept below, with the rule in `safety.md` section 8.
9. Which `os.name` and lock branch each Python on the machine reports (python.org, Store, MSYS2 or Cygwin if present).
   Outcome: observed. Two python.org Pythons, 3.9.13 and 3.14.5, both `nt` on the `msvcrt` branch with the mutex probe ok; no MSYS2 or Cygwin Python was found.
10. A home given with a different drive-letter case or an 8.3 short name: the mutex re-entrance key is the absolute path string, so two spellings in one process would wait on themselves.
   Outcome: passed under both. The other drive-letter case and the 8.3 short name each entered the mutex at once. The 8.3 spelling differs from the given one under `normcase(abspath)` and agrees under `Path.resolve()`.
11. `msvcrt.locking` on an SMB share, if a record is ever kept on one.
   Outcome: not run; it needs a person and a share, and was optional.

The run of 2026-10-16 used python.org Python 3.9.13 and 3.14.5 on Windows 11; the results, with the Windows user name replaced by `<user>`, are in `windows-results/`. Finding 8's test, `test_R8_G09_a_locking_error_is_named_not_read_as_contention`, ran on the `msvcrt` branch in the unit suite under both and passed.

## Fixes

Date: 2026-10-15. Applied by the lease-fix pass; the decisions are recorded under "Added by the lease fixes" at the end of `DECISIONS.md`. Line numbers are as of this section, in `scripts/mmb_common.py` (688 lines) and `scripts/record.py` (2,110 lines). Each test named below fails on the scripts as they were at this review and passes now. The suite is 153 tests (135 before, 18 added) and green under `/usr/bin/python3` (3.9) and Python 3.14; `tools/lint_plugin.py` reports 0 errors. Existing tests that encoded the old rules were brought in line: C91 and C112 now open strand 002's version (and C91 adds the interrupted run a paused take needs), C100 and C113 start a run before fencing, C110 expects `for_strand` on the `broken` entry, C99 expects `reserved_for`, C25 the two new subcommands, and part 2's C107/C112, C108 to C113 and C166 open 002's version through `version open` and refresh with a run id before fencing.

| # | Outcome | Where | Tests |
|---|---|---|---|
| 1 | Fixed: `broken` and `parked` entries carry `for_strand`; while `broken`, the newest entry keeps the lease for one strand (resume: the holder's; park: the taker's; repair: its `for_strand`), every other take refused, a reservation for a closed strand lapsing; `lease status` and `status --json` show `reserved_for`; the record-map lock section says so | `mmb_common.py:312` (`_event`), `:437` (`_reserved`), `:448` (`_closed`), `:486` (take), `:553` (break), `:592` (status); `shared/record-map.md` lock and status sections | `test_mmb_common.LeaseFixTest.test_R1_C111_a_resume_break_keeps_the_lease_for_the_holders_strand`, `test_R1_C112_after_a_park_only_the_taker_takes`, `test_R1_G53_a_reservation_for_a_closed_strand_lapses`; `test_record_part2.LeaseFixTest.test_R1_C99_C111_status_names_whose_take_comes_next` |
| 2 | Fixed: the fence refuses while the lock has no `run_id`; a refresh refuses a run id an earlier lease carried | `mmb_common.py:608` (fence), `:519` (refresh) | `test_R2_G50_G51_no_fenced_write_before_a_run_and_no_old_run_in_a_new_lease` |
| 3 | Fixed: a fence that passes moves the heartbeat in the same mutex hold (`_beat`) | `mmb_common.py:608`, `:506` | `test_R3_G51_the_fence_moves_the_heartbeat_before_the_write` |
| 4 | Fixed: `_commit` writes both mirrors and the lock last, so a failed write leaves the lease unchanged and is retryable, with a `CannotRun` naming the file; a failure after the primitive committed is exit 3 with field `committed` and a top-level `committed` object (take: epoch, label, entry; release; break: result, entries, park line; repair) | `mmb_common.py:388` (`_commit`), `:38` (`MMBError.committed`); `record.py:1384` (`FINISH`), `:1387` (`committed`), `:1398`, `:1415`, `:1437`, `:1487`, `:2099` | `test_R4_G09_a_failed_mirror_write_leaves_the_lease_as_it_was`; `test_R4_C87_C98_C109_a_failure_after_the_commit_reports_what_was_committed` |
| 5 | Fixed: `record.py lease sync` rewrites both mirrors from the lock, the lock unchanged; `check`'s mirror findings name it; with the lock written last a failed release is simply retried | `mmb_common.py:632` (`lease_sync`); `record.py:1430`, `:543` (`check` text) | `test_R5_C84_G09_lease_sync_heals_the_mirrors_and_a_failed_release_can_be_retried` |
| 6 | Fixed: take, release, break and repair back the lock up; `record.py lease repair --user-yes` rebuilds a missing, torn or malformed lock in place (torn bytes backed up, never deleted) one epoch above the newest sound backup and the `account.json` mirror, with the backup's history and a `repaired` entry, `broken` and kept for the mirror's holder or else `released`; every exit 3 on an unreadable lock names it; G39 and RM:68 now say the user clears `.work/backup/`, never `.work/`. The mutex-unlink case on macOS is not guarded in code: a lock on a fresh file cannot see the deleted one, so the guard is the rule that `.work/` itself is never cleared (record-map, `safety.md` section 8) | `mmb_common.py:322` (`read_lock`), `:388` (backup on state changes), `:640` (`_backups`), `:646` (`lease_repair`); `record.py:1437` | `test_R6_G39_take_release_and_break_back_up_the_lock`; `test_R6_C83_lease_repair_rebuilds_a_torn_lock_for_its_holder`, `test_R6_C97_lease_repair_keeps_the_newest_sound_backups_history` |
| 7 | Fixed: allowlists for the lock state (`none`, `released`, `broken`), kind (`platform`, `hybrid`), strand state (`active`, or `paused` on the park path) and version (`vX.Y` with its `version.md`) | `mmb_common.py:463` (take, lines 473 to 487); a lock state outside the four is refused by the shape check at `:346` | `test_R7_G50_G53_a_take_needs_allowlisted_values` |
| 8 | Fixed: only `EWOULDBLOCK`/`EAGAIN` (POSIX) and `EACCES`/`EDEADLOCK` (msvcrt) count as contention; any other locking error is exit 3 at once, naming it | `mmb_common.py:259` (`_os_lock`) | `test_R8_G09_a_locking_error_is_named_not_read_as_contention` (Windows run: the msvcrt branch) |
| 9 | Fixed: `lock_findings` checks G02's shape (schema, history, epoch, state, the held fields and their forms, null fields otherwise); every primitive refuses a malformed lock naming the repair, the fence returns `(False, reason)`, `check` blocks on the same findings, `lease status` and `status` report an unparsable heartbeat as null; the fence and the break's compare-and-set need a non-empty label | `mmb_common.py:346`, `:372` (`_files`), `:560`, `:621`, `:592`; `record.py:451`, `:557` | `test_R9_G51_a_held_lock_without_a_label_passes_neither_fence_nor_break`; `test_R9_C131_C153_a_malformed_lock_is_a_finding_not_a_crash` |
| 10 | Kept, with the wording fixed: see below | `record.py:566` | none (text only) |
| 11 | Kept in code; the rule is now stated: see below | `shared/safety.md` section 8, "One environment per record" | none |
| 12 | Kept, open with the user: see below | none | none |
| 13 | Fixed: `paused` takes only with an `interrupted` run in the strand's `build.json` (the park path) | `mmb_common.py:474` | `test_R13_G05_G53_a_strand_the_user_paused_does_not_take` |
| 14 | Kept: see below | none | none |
| 15 | Fixed: `init` repeats the emptiness check inside the mutex, a `.work/` holding only `record.mutex` counting as empty | `record.py:1953` (`occupied`), `:1983` | `test_record_part2.LeaseFixTest.test_R15_C44_a_second_init_of_the_slug_writes_nothing` |
| 16 | Fixed: `shared/safety.md` section 8 rewritten to the lease as built (session label and `--label`, no `surface`, no `--chat-label`, no `leases.json`, the one question, the allowlists, the fence, the three break entries and the broken epoch + 2, the reservation, the write order, `lease sync`, `lease repair`, `.work/backup/` only); its "Who may hold it" follows A§9.8 (intake, the readiness check, blueprint drafting), dropping the deferred SOP, doc-copy and demo-script cases | `shared/safety.md` section 8 | none (text) |

### Why 10, 11, 12 and 14 stay

- **10, one clock direction.** The lock's modification time as a second clock would make every age depend on the file system's clock as well as `now_utc`, which the unit tests pin and the file system does not follow, and it still needs two clocks to go wrong: one machine has one clock. Scenario B is the trade the part-2 decision chose (a stepped-back clock costs a lease, never a double write, since the fence refuses the holder's next write). What changed: `safety.md` section 8 now says to write a record from one environment at a time and keep the machine's clock right, which removes the WSL and two-machine cases of scenario A, and `check`'s expected text reads "set the clock of each machine that writes this record to the right time; until then the lease reads as not fresh and may be broken". Revisit if the Windows run (item 8) shows a lagging WSL clock writing the same record in practice.
- **11, one OS environment.** No standard-library lock spans WSL and Windows, two Pythons with different lock emulations, or two machines on a synced folder, so the fix is the rule, now in `safety.md` section 8 ("One environment per record": one environment writes a record at a time; the record home stays out of a cloud-synced folder). WP8's first-run walkthrough should repeat it (a DECISIONS follow-up); the Windows run's item 8 confirms the WSL case.
- **12, a session that lost its label.** A decision for the user, recorded under "Open with the user (R12)" in DECISIONS: accept the 60-minute wait and correct A§9.8:933, or allow a same-strand takeover with the user's yes. The build keeps the wait, which `safety.md` section 8 now states, and A§9.8:933 is left until the user answers. Finding 2's fix narrows the exposure: nothing passes the fence before `run start`, and no old run id enters a new lease.
- **14, long reads under the mutex.** Hashing raw inputs outside the mutex would split `check`'s one consistent read into two and needs its own re-check; nothing in WP2 times out today. The risk sits with WP3, and two things now close it there: the fence is the refresh (finding 3), so a mutex timeout on it is a refused write rather than a skipped refresh, and DECISIONS' G51 amendment tells WP3 that a fence or refresh that cannot run is a stop, never a skip.

### Not done here

- `shared/safety.md` sections 1 to 5, 7, 9, 10, 12 and 13 still say "chat" where A§9.8 says "session" (a WP1 vocabulary pass, listed in DECISIONS).
- The design text touch-ups the new decisions list (A§5.3, A§5.4, A§7.1, A§9.8, BP:134, BP:248, BP:502) are not applied; they are listed with each decision.
- The Windows run list above stands; finding 8's test and the write-order change (items 1, 5 and 7) are the parts it now also exercises.

**Finding 12, settled 2026-10-15:** the user chose to keep the 60-minute wait (option a). No code change; ARCHITECTURE 9.8's carry rule corrected to match.
