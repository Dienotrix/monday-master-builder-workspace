# WP2 Windows check results

- Run at: 2026-10-16T15:45:06Z (UTC), 51 s
- Interpreter: C:\Users\<user>\AppData\Local\Programs\Python\Python39\python.exe (3.9.13)
- Mode: full

## 1. System

- os.name: nt
- sys.platform: win32
- sys.version: 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)]
- sys.executable: C:\Users\<user>\AppData\Local\Programs\Python\Python39\python.exe
- sys.prefix: C:\Users\<user>\AppData\Local\Programs\Python\Python39
- sys.base_prefix: C:\Users\<user>\AppData\Local\Programs\Python\Python39
- virtual environment: False
- platform: Windows-10-10.0.26200-SP0
- machine: AMD64
- sysconfig platform: win-amd64
- python source: python.org-style MSVC build (most likely the python.org installer)
- mmb_common mutex branch: msvcrt (imports)
- mutex probe: ok (taken, re-entered, released)
- temp folder: C:\Users\<user>\AppData\Local\Temp
- filesystem encoding: utf-8
- stdout encoding: utf-8

py -0p:

```
-V:3.14 *        C:\Users\<user>\AppData\Local\Programs\Python\Python314\python.exe
 -V:3.9           C:\Users\<user>\AppData\Local\Programs\Python\Python39\python.exe
```

## 2. Unit suite

- Status: ran
- Result: pass
- Summary: ran 161 tests in 23.089 s; OK (skipped=1)
- took 23.5 s

```
......................................................................s..........................................................................................
----------------------------------------------------------------------
Ran 161 tests in 23.089s

OK (skipped=1)
```

## 3. Lease review items

### Item 1: Mutex: processes serialised, re-entrance, timeout (msvcrt branch)

- Status: ran
- Result: pass
- Summary: serialised: True; re-entrant: True; second handle refused with the timeout: True
- branch taken: msvcrt (imports)
- 4 processes x 20 locked read-sleep-write cycles: exits [0, 0, 0, 0], counter 80 (want 80), mutex file 0 bytes (want 0), 1.5 s
- re-entrance in one thread: ok
- second handle in this process (another thread), timeout 0.5 s: refused after 0.50 s, exit code 3, field record.mutex
- took 2.0 s

### Item 2: Take race with eight processes; refresh against break

- Status: ran
- Result: pass
- Summary: take race: one winner, epoch 3, mirrors agree: True; refresh against break consistent in 3 of 3 rounds
- take race, 8 processes: exits [0, 1, 1, 1, 1, 1, 1, 1]; lock after {'state': 'held', 'epoch': 3, 'label': '20261016-1144-ibj5', 'mirrors_agree': True}; winner's label 20261016-1144-ibj5
- refresh against break, round 1 (3 breaks, 3 refreshes on a stale lease): break exits [1, 0, 1], refresh exits [1, 1, 1]; lock after {'state': 'broken', 'epoch': 4, 'label': None, 'mirrors_agree': True}; consistent: True
- refresh against break, round 2 (3 breaks, 3 refreshes on a stale lease): break exits [1, 1, 1], refresh exits [0, 0, 0]; lock after {'state': 'held', 'epoch': 3, 'label': '20261016-1144-3edd', 'mirrors_agree': True}; consistent: True
- refresh against break, round 3 (3 breaks, 3 refreshes on a stale lease): break exits [1, 1, 1], refresh exits [0, 0, 0]; lock after {'state': 'held', 'epoch': 3, 'label': '20261016-1144-v0qv', 'mirrors_agree': True}; consistent: True
- took 14.5 s

### Item 3: Holder killed with Popen.kill() (TerminateProcess, as taskkill /F): time to reacquire

- Status: ran
- Result: pass
- Summary: another process acquired the mutex 0.06 s after Popen.kill() (pass under the 30 s mutex timeout)
- child exit code after kill: 1; it had exited 0.06 s after the kill
- a fresh process afterwards: acquired 0.00
- took 0.2 s

### Item 4: Unlock after the body raised

- Status: ran
- Result: pass
- Summary: error kept, mutex free afterwards in and out of process, direct unlock clean: True
- ValueError reached the caller unmasked (probe raised inside the hold)
- retaken in this process at once: ok
- taken by another process: acquired 0.00
- _os_lock unlock with the file position moved: ok (unlock after the position moved does not raise)
- took 0.1 s

### Item 5: Sharing violations on account.json, CLIENT.md and log.md during take, release and break

- Status: ran
- Result: pass
- Summary: every command answered with one JSON object and either left the lease unchanged or reported what it committed: True (see the table; the retry column is data)
- took 9.8 s

| hold | file | command | hold check | exit | first finding | lock | committed | retry after close | lease sync |
|---|---|---|---|---|---|---|---|---|---|
| share mode 0 | account.json | take | effective (PermissionError) | 3 | account.json / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 8jwf27ni\\mmb home\\clients\\larkmoor-joinery\\account.json' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | account.json | release | effective (PermissionError) | 3 | account.json / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 55_b8vis\\mmb home\\clients\\larkmoor-joinery\\account.json' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | account.json | break | effective (PermissionError) | 3 | account.json / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 9ubdqx4f\\mmb home\\clients\\larkmoor-joinery\\account.json' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | CLIENT.md | take | effective (PermissionError) | 3 | CLIENT.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 1ehiycjm\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | CLIENT.md | release | effective (PermissionError) | 3 | CLIENT.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check cc_cd2rq\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | CLIENT.md | break | effective (PermissionError) | 3 | CLIENT.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check dx6ra76l\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | log.md | take | effective (PermissionError) | 3 | log.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check tkpgn_2u\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | log.md | release | effective (PermissionError) | 3 | log.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check _ujqg4dy\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| share mode 0 | log.md | break | effective (PermissionError) | 3 | log.md / (whole file): cannot read the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 88qink18\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | account.json | take | effective (PermissionError) | 3 | account.json / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check cxzccpfa\\mmb home\\clients\\larkmoor-joinery\\account.json'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | account.json | release | effective (PermissionError) | 3 | account.json / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check wcr1sj7u\\mmb home\\clients\\larkmoor-joinery\\account.json'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | account.json | break | effective (PermissionError) | 3 | account.json / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check xm302mt3\\mmb home\\clients\\larkmoor-joinery\\account.json'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | CLIENT.md | take | effective (PermissionError) | 3 | CLIENT.md / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check zv9ue_tg\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | CLIENT.md | release | effective (PermissionError) | 3 | CLIENT.md / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 3pqe67eo\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | CLIENT.md | break | effective (PermissionError) | 3 | CLIENT.md / lease: could not write the file: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check _se3_7pt\\mmb home\\clients\\larkmoor-joinery\\CLIENT.md'; the lease is unchanged, the lock being written last | lock unchanged | no | exit 0 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | log.md | take | effective (PermissionError) | 3 | .work/lock.json / committed: the take of epoch 3, session 20261016-1145-gwpl was committed, then a later write failed: PermissionError: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 2my1vwki\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock changed to held/3 | yes | exit 1 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | log.md | release | effective (PermissionError) | 3 | .work/lock.json / committed: the release of epoch 3 was committed, then a later write failed: PermissionError: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check qd7qj2sc\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock changed to released/3 | yes | exit 1 | exit 0; mirrors agree after: True |
| read sharing only (writes denied) | log.md | break | effective (PermissionError) | 3 | .work/lock.json / committed: the break of epoch 3 (choice resume, for strand 001) was committed, then a later write failed: PermissionError: [Errno 13] Permission denied: 'C:\\Users\\<user>\\AppData\\Local\\Temp\\mmb win check 2ds80fpq\\mmb home\\clients\\larkmoor-joinery\\log.md' | lock changed to broken/4 | yes | exit 1 | exit 0; mirrors agree after: True |

### Item 6: A record home inside a OneDrive-synced folder: take and refresh during an upload

- Status: not run (manual; optional)
- Result: -
- step 1: py tests\windows\run_windows_checks.py --copy-fixture "%OneDrive%\mmb-check" (PowerShell: "$env:OneDrive\mmb-check"); it prints the record folder, called RECORD below.
- step 2: py plugins\monday-master-builder\scripts\record.py --record "RECORD" lease release --epoch 2 --label 20261105-1405-r2d6, then the same with: lease take --strand 001 (note the epoch and label it prints).
- step 3: While OneDrive shows the folder syncing, run lease refresh --epoch EPOCH --label LABEL a few times, then lease status. Send the outputs.

### Item 7: Ctrl+C in a Windows console during lease take: the state of lock.json afterwards

- Status: not run (manual; optional)
- Result: -
- step 1: py tests\windows\run_windows_checks.py --copy-fixture "%TEMP%\mmb-ctrlc"; release as in item 6.
- step 2: Run record.py --record "RECORD" lease take --strand 001 and press Ctrl+C straight away; repeat (release with the printed epoch and label between tries) until one try is cut short.
- step 3: Run lease status and send its output, and say whether .work\lock.json still opens as JSON.

### Item 8: A WSL session and a native session on one record under C:\, and the WSL clock after sleep

- Status: not run (manual; optional)
- Result: -
- step 1: py tests\windows\run_windows_checks.py --copy-fixture C:\mmb-check; then in Windows: py tests\windows\run_windows_checks.py --hold-mutex "RECORD" --seconds 60
- step 2: Within that minute, in WSL from the same folder (under /mnt/c/...): python3 tests/windows/run_windows_checks.py --try-mutex "/mnt/c/mmb-check/.../larkmoor-joinery" --seconds 5. "acquired" means the two do not exclude each other.
- step 3: After the machine has slept and woken: at the same moment run date -u +%FT%TZ in WSL and (Get-Date).ToUniversalTime().ToString("s") in PowerShell, and send both.

### Item 9: Lock branch per interpreter (py -0p and MSYS2 or Cygwin if present)

- Status: ran
- Result: observed
- Summary: 2 interpreter(s) reported
- took 0.5 s

| interpreter | os.name | sys.platform | version | source | branch | mutex probe |
|---|---|---|---|---|---|---|
| C:\Users\<user>\AppData\Local\Programs\Python\Python314\python.exe | nt | win32 | 3.14.5 | python.org-style MSVC build (most likely the python.org installer) | msvcrt (imports) | ok (taken, re-entered, released) |
| C:\Users\<user>\AppData\Local\Programs\Python\Python39\python.exe | nt | win32 | 3.9.13 | python.org-style MSVC build (most likely the python.org installer) | msvcrt (imports) | ok (taken, re-entered, released) |

### Item 10: Drive-letter case and 8.3 short path: does the mutex wait on itself

- Status: ran
- Result: pass
- Summary: no self-wait for: drive letter in the other case, 8.3 short path
- given: C:\Users\<user>\AppData\Local\Temp\mmb win check 1m5mec7l\mmb home\clients\larkmoor-joinery
- drive letter in the other case: c:\Users\<user>\AppData\Local\Temp\mmb win check 1m5mec7l\mmb home\clients\larkmoor-joinery | same file: True | Path.resolve() equal: True | normcase(abspath) equal: True | mutex: entered at once (no self-wait)
- 8.3 short path: C:\Users\<user>\AppData\Local\Temp\MM3503~1\MMBHOM~1\clients\LARKMO~1 | same file: True | Path.resolve() equal: True | normcase(abspath) equal: False | mutex: entered at once (no self-wait)
- long path (same as given: 8.3 names may be off on this volume): not tested
- took 0.0 s

### Item 11: msvcrt.locking on an SMB share, if a record is ever kept on one

- Status: not run (manual; optional)
- Result: -
- step 1: py tests\windows\run_windows_checks.py --copy-fixture "\\server\share\mmb-check"
- step 2: In one window: --hold-mutex "RECORD" --seconds 60; in a second window within the minute: --try-mutex "RECORD" --seconds 5 ("refused" is right). If a second machine can reach the share, repeat the try there.
- step 3: Send both outputs.

