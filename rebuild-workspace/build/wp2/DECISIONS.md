# WP2 decisions: the gaps of CONTRACT.md section 4

Date: 2026-10-14. Internal build file: never client-facing.

This file settles G01 to G61 of `CONTRACT.md` so that `scripts/mmb_common.py` and `scripts/record.py` are coded against one reading. Anchors are the contract's: `BP:n` (BUILD-PLAN line), `A§section:line` (ARCHITECTURE), `RM:n` (`shared/record-map.md`), `AM:n` (AMENDMENTS), `1b:n` (stage-1b PLAN). Authority order: AMENDMENTS over ARCHITECTURE over BUILD-PLAN over `record-map.md`, which was pinned on 2026-10-13 and is the stale text wherever the 2026-10-14 re-cut moved. Where no source settles a point, the entry takes the smallest decision that makes the acceptance testable and keeps the scripts simple.

Each entry gives the decision, one sentence of reason naming the source that wins, and the follow-up: a `record-map.md` edit, a design text touch-up (ARCHITECTURE or BUILD-PLAN, and `shared/safety.md` where it repeats the same text), or none. One entry is marked **For the user** (G23); its recommended default is what the coders build until the user answers. Nothing here fills an A11 field, names a person, firm, account or workspace, or writes into the plugin folder.

---

### G01 Session label: key name, format, example

**Decision.** The key is `session_label` everywhere it appears: the lock, each lock history entry, `account.json` `guard_index.lease`, the `status --json` lease block, `build.json` `runs[]`, and `ledger.py --session-label`; the log header's last field reads "key or session label". `lease take` mints it as `YYYYMMDD-HHMM-xxxx`: the local date and minute of the take (G40) and four characters drawn with `secrets.choice` from `abcdefghijklmnopqrstuvwxyz0123456789`, re-drawn until the label equals no label in the lock's `history`, so "two takes on one day never collide" is a guarantee (test: patch the clock and a repeating random source, take and release 50 times in one minute, all labels distinct and matching `^\d{8}-\d{4}-[a-z0-9]{4}$`). A label is never free text and is compared as an exact string. The `CLIENT.md` mirror reads `"none"` or `"<short id> <version> (<session_label>)"`, for example `"001 v0.1 (20261015-1330-k7q2)"`.

**Reason.** ARCHITECTURE (A§9.8:933, A§7.3:524, A§5.4:355) wins over the stage-1 `chat_label` of RM:77 and RM:135, and A20 and A24 leave one surface, so the surface prefix goes; the `build v0.1 Tue` examples have neither shape and are illustrations.

**Follow-up.** Record-map edit: RM:77, RM:100, RM:116, RM:120, RM:135, RM:146, RM:163. Design text touch-up: the example labels at A§7.2:468, A§7.3:524, A§7.3:559 and A§9.8:939 become a minted label such as `20261015-1330-k7q2`; `shared/safety.md` section 8 says session label, not chat label.

### G02 The `lock/2` field list

**Decision.** `.work/lock.json` holds, in this key order: `schema` (`"lock/2"`), `kind` (`"build"`), `epoch` (integer), `strand`, `strand_title`, `version`, `run_id`, `session_label`, `taken_at`, `heartbeat_at` (each a string while `state` is `held`, and `null` otherwise), `state` (`none` | `held` | `released` | `broken`) and `history` (list); there is no `surface`, in the lock or in the status block. A history entry is `{event, at, epoch, strand, version, session_label, run_id, by, choice, reconcile, note}`: `event` `taken` | `released` | `broken` | `parked`; `at` in UTC (G40); `by` the acting session's label (the minted label on `taken`, the holder's on `released`, `null` on `broken` and `parked`, because the breaking session holds none); `choice` `resume` | `park` on `broken`, else `null`; `reconcile` the class counts of G04 on `broken`, else `null`; `note` on `broken` and `parked` the taking strand and the user's quoted words (`for 002: "..."`), else `null`. The template lock that `init` places is `{"schema": "lock/2", "kind": "build", "epoch": 0, ...every other field null..., "state": "none", "history": []}`.

**Reason.** A§9.8:933 wins over RM:135 and RM:147, and with one surface (A20, A24) a field with one possible value is dropped.

**Follow-up.** Record-map edit: RM:135, RM:146 to 147. Design text touch-up: `shared/safety.md` section 8 field list drops `surface`.

### G03 Epoch arithmetic, and how many log entries a break writes

**Decision.** Every take increments the epoch by one and every break increments it by one, with no special case: breaking a lease held at epoch E leaves the lock at E+1 in state `broken`, and the next take (the taker's on park, the fresh holder session's on resume) makes it E+2. A break writes three `lease` entries in one locked insert, top to bottom: one at strand position `-` with version `-` (the broken epoch, the holder's strand, title, version and label, the reconcile class counts, the choice and the user's words); one at the holder's position with the holder's version; one at the taking strand's position with version `-`; each strand-position entry names the choice and the broken epoch, and all three carry the holder's label as the header's last field. The strand-position entries are what keep "both strands' logs carry the choice" true after each strand's roll (G08).

**Reason.** A§9.8:933, RM:135 and BP:123 all state an increment on every take and every break, so the "epoch + 1" of A§9.8:945 and BP:502 is read as the take's own increment after the break; A§9.8:945 itself asks for both the record-level entry and both strands' logs, which with one record-wide log (A§7.6:645) is three entries.

**Follow-up.** Design text touch-up: A§9.8:945 "the new holder starts at `epoch + 1`" becomes "the new holder's take increments it again, to the broken epoch + 2"; BP:502 (H35) "002 holds epoch + 1" becomes "002 holds the broken epoch + 2"; the same sentence in `shared/safety.md` section 8.

### G04 How `lease break` learns conditions 2 to 5

**Decision.** The interface is `record.py lease break --label <holder's label> --epoch <holder's epoch> --for-strand <short id> --user-yes "<the user's words>" --account-id <id read live in this session> --choice resume|park [--park-yes "<the user's words>"]`; label and epoch are a compare-and-set against the lock (a mismatch is refused as "the lease changed since it was read"), and the five conditions are checked in order, every failing one listed in the refusal: (1) `heartbeat_at` more than 60 minutes old; (2) `--user-yes` present and containing the holder's short id as a whole token (`(?<!\d)001(?!\d)`) or its full id, so "yes, clear the lock" fails; (3) `--account-id` equal to `account.json` `account.id`, which must not be `unbound`; (4) the holder's `solution/build.json` has the `runs[]` entry whose `id` is the lock's `run_id`, in state `interrupted`, carrying `reconcile: {at, mode: "classify-only", classes: {adopt, retry, duplicate, partial, changed-since-verified, unrecorded-extra, missing}}` with `at` later than the lock's `heartbeat_at` (when the lock's `run_id` is `null`, nothing can have been written, so the condition holds and the counts are recorded empty); (5) `--choice` present. Missing arguments for conditions 2, 3 and 5 are refusals (exit 1), not usage errors. Park is further refused without `--park-yes`, when `duplicate` or `partial` is above zero, or when `--for-strand` is the holder; on park the holder's `STRAND.md` gets `state: "paused"` and the `## Paused` block of G52 naming the run, the version and the class counts, and the history gets `broken` then `parked`.

**Reason.** A§9.8:945 names the five conditions and no source gives the interface, so each condition becomes either a structured argument the session must supply (2, 3, 5) or a fact the script reads from the record (1, 4), which keeps "prose is not a yes" testable and leaves the live monday read in the session, the only place it can run.

**Follow-up.** Record-map edit: RM:120 (`runs[]` gains `reconcile`). Design text touch-up: BP:134 and BP:138 (WP3), `reconcile --classify-only` writes that `reconcile` object onto the interrupted run; A§9.8:945 and BP:123 name the flags; BP:248 (`recovery.md`, WP9) passes them.

### G05 What returns a parked strand to `active`

**Decision.** `record.py` gains one subcommand, `strand resume --strand <id>`, the only writer that returns a strand from `paused` to `active`: it refuses unless the strand is `paused`, while its `build.json` has any `runs[]` entry in `running` or `interrupted`, and while the lock is `held` for that strand; it then sets `state: "active"`, replaces the `## Paused` block's content with `none (resumed YYYY-MM-DD)`, writes a `strand` log entry ("resumed") and refreshes the index (G06). `lease take` accepts a `paused` strand (G53), so a parked strand's way out is: take, recovery, `ledger.py run end`, then `strand resume`; C25's catalogue gains `strand resume`.

**Reason.** A§7.7:686 and BP:502 require the return to `active` after the ordinary recovery and neither catalogue has a writer for it, so the smallest addition is one named subcommand rather than a side effect hidden in `ledger.py`, which never writes `STRAND.md`.

**Follow-up.** Design text touch-up: A§5.4:354 and BP:123 add `strand resume` to the catalogue; A§7.7:686 and A§8.11:836 name it as the last step of the resume; BP:248 (`recovery.md`, WP9) calls it after `run end`.

### G06 Who writes the strand index and the counters

**Decision.** `record.py` maintains the `CLIENT.md` strand index and counters: whenever any subcommand writes a `STRAND.md` (`strand open|pause|resume|kind|close`, `version open|mark|release`, `lease break` on park, and `guard` when its target is a `STRAND.md`), it regenerates the whole table under `## Strand index` from every `STRAND.md` (the G18 columns, rows by short id, `live objects` and `last activity` computed as in G54), sets `strands_total` (the number of strand folders) and `strands_open` (strands not `closed`), and sets `current_strand` to a newly opened strand only when it reads `"none"`. `check` blocks when the set of index rows differs from the set of `strands/NNN-*` folders or a counter differs from the folders, and warns when a row's title, kind, state, version, version state or clearance differs from its `STRAND.md`; `live objects` and `last activity` are display cells, refreshed at the same moments and never compared. `record_state` and `products_in_scope` stay with the skills.

**Reason.** BP:123 makes `check` block on any disagreement with the folders, so the only way to leave no blocking window is for the script that changes a strand to change the index in the same locked step, which is how A§8.10:828's "updates the strand index" already reads.

**Follow-up.** Record-map edit: RM:85 (the strand index is written by `record.py`, read by every skill). Design text touch-up: A§7.2:481 (owner `record.py`, not engagement); A§8.4:772 (the readiness check's index update happens through `record.py guard` on `STRAND.md`).

### G07 What `strand close` does itself

**Decision.** `strand close --strand <id>` does only this, in order: refuses while the lock is `held` for the strand, while the strand is `paused`, while any version's `version.md` `state` is `building` or `fixing`, and while any version that is not `released` has `close_reason: "none"`; rolls the strand's log (G08); sets `state: "closed"`, `stage: "closed"` and `closed: "<date>"` in `STRAND.md`; refreshes the index and counters (G06). The ownership record, `close-out.md`, the `SUMMARY.md` refresh (through `strand summary`), `live-map set`, `prior_builds` and the lint re-run stay with `client-closeout`, and `version.md` gains `close_reason` (`"none"` until `client-closeout` writes the reason through `guard`). C78's set of files that may change therefore also includes `CLIENT.md` (index and counters) and `.work/` (backups, the log baseline).

**Reason.** BP:296 gives A§8.10:828's other steps to `client-closeout`, while the fourth refusal comes from A§8.10:828, which wins, and needs a field `record.py` can read.

**Follow-up.** Record-map edit: RM:112 (`version/1` gains `close_reason`). Design text touch-up: A§8.10:828 says which steps are `record.py strand close` and that the close reason lives in `version.md`.

### G08 Log roll and the proof that history only grew

**Decision.** A roll moves whole entries, verbatim, out of the record `log.md`: `version release` moves every entry at the strand's position whose version field is the released version into `versions/<v>/log.md`, and `strand close` moves every remaining entry at the strand's position into `strands/<id>/log.md`; each rolled file is new (refused if it exists) with front matter `schema: "log/1"`, `client`, `strand`, `version` (or `"none"`), `rolled_at`, `entries`, `sha256`, and each roll leaves one pointer entry at the strand position (type `release` with key `released`, or type `strand` with key `closed`) whose body is `rolled_to: <record-relative path>` and `entries: <n> · sha256: <hex>`. Every entry hash, and the roll hash over the moved entries concatenated in file order, is sha256 of the entry's header and body lines with line endings normalised to LF, trailing blank lines dropped and every line ended by LF; `check` blocks when a rolled file's recomputed hash differs from its front matter or from its pointer entry, found by `rolled_to` in any log file. "History only grew" uses `.work/history.json` (`{"schema": "history/1", "entries": [<entry hash>, ...]}`, newest first): every `log` insert prepends its entry's hash, every roll removes the moved hashes and prepends the pointer's, and `check` blocks when the baseline is not an ordered subsequence of the current entry hashes (an entry changed or removed), and warns on an entry absent from the baseline (written by something other than `record.py`) or on a missing baseline, which the next insert rebuilds from the file.

**Reason.** A§7.6:645, which wins, requires the pointer and the hash check, and moving the strand's (or the released version's) own entries instead of "those below the live part" makes the roll deterministic and testable on a small fixture, while the 300-line live part (A§7.1:387) stays a budget warning.

**Follow-up.** Record-map edit: RM:66 (`history.json` defined); RM:166 (the roll sentence). Design text touch-up: A§7.6:645 and A§7.4:610, "that strand's entries below the live part" becomes "that strand's entries (at a release, those of the released version)"; A§7.1:437 defines `history.json`; A§5.4:354 "history files only grew" becomes "the log only grew", since the other history files have no script writer that could keep a baseline.

### G09 Concurrency mechanism versus the no-delete rule

**Decision.** Every read-modify-write in a record, and every read that feeds a decision, runs inside one record mutex: an advisory exclusive lock on byte 0 of `.work/record.mutex`, a zero-byte file opened with mode `"a+b"`, created on first use and never deleted, taken with `fcntl.flock(fd, LOCK_EX | LOCK_NB)` on POSIX and with `msvcrt.locking(fd, msvcrt.LK_NBLCK, 1)` after `seek(0)` on Windows, retried every 50 ms for up to 30 seconds and then exit 3, and released in a `finally`; these two branches are the tested per-system implementation A24 allows. A `log` insert is: take the mutex, re-read `log.md`, insert under the header, overwrite in place, update the baseline (G08), release; the lease primitives write `.work/lock.json`, then the `account.json` mirror, then the `CLIENT.md` mirror under one hold, and every primitive call rewrites both mirrors from the lock, so a crash between the writes heals at the next take, refresh, release or break. Because an in-place overwrite is not atomic, `status` and `check` also read under the mutex, and `ledger.py` and the hook must do the same or treat an unparsable file as "retry, then refuse".

**Reason.** A§5.3:341 and BP:123 forbid rename and delete, which rules out atomic-rename writes and exclusive-create lock files, and an operating-system byte-range lock on a persistent file is the standard-library mechanism that needs neither.

**Follow-up.** Record-map edit: RM:66 (`.work/record.mutex`). Design text touch-up: A§7.1:437 lists `record.mutex`; BP:134 (WP3), `ledger.py` holds `mmb_common.record_mutex` around every read and write of `account.json`, a `build.json` and the lock; A§9.10:955 and BP:305 (WP13), `guard.py` reads the lock under the same mutex or treats a torn read as a refusal.

### G10 Exit codes of refusals

**Decision.** 0: the command did its work with nothing to report. 1: `check` found a blocking finding, and every refusal (stale sha, lease held or not held, label or epoch mismatch, a failed break condition, a `non-platform` strand, a newer schema, a release with missing files, a close refusal, an invalid value such as a slug, a log type or a six-line body). 2: the command did its work, or `check` ran, and only warnings remain (including `version mark signed-off` with unconfirmed assumptions, G22). 3: it could not run (record or a required file missing or unreadable, malformed JSON in the lock or `account.json`, a missing template or `plugin.json`, a mutex timeout, Python below 3.9, a usage error, an unknown subcommand such as `migrate` or `tools-check`, an unexpected exception); `argparse` exits 2 on a usage error by default, so the parser subclass overrides `error()` to print the JSON envelope and exit 3. `status` exits 0 whenever it printed its object, whatever the findings, and 3 when it could not read the record; every other subcommand prints one JSON object, `{"ok": true|false, "command": "<name>", ...}`, with refusals as `"refusals": [{"file", "field", "problem", "expected"}]`, a could-not-run as `"error": {...}` with the same four keys, and `file` record-relative in POSIX spelling (`PurePath.as_posix()`) so the output is identical on both systems.

**Reason.** A§5.3:343 gives four codes and no mapping for refusals, and a refusal is the blocking case of a write, so it shares code 1, while one JSON envelope makes C21's four parts checkable by a test.

**Follow-up.** Design text touch-up: A§5.3:343 adds "a refusal exits 1; a usage error exits 3; `status` exits 0 when it printed".

### G11 Line ending written, and the raw-file rule

**Decision.** Text the scripts compose (front matter rewrites, log entries, rolled logs, `STRAND.md`, `version.md`, `SUMMARY.md`, the index, `settings.json`) is written as UTF-8 without a BOM and with LF only (`open(path, "w", encoding="utf-8", newline="\n")`), and a current file that arrives with CRLF, such as a `guard` staging file, is rewritten with LF; JSON files are written as `json.dumps(data, indent=2, ensure_ascii=False)` plus a final LF with key order kept, so the lease mirror and `ledger.py` never churn each other's formatting. Text is read with `encoding="utf-8-sig"` and universal newlines, so CRLF, LF and a leading BOM parse alike. Raw inputs (transcripts, documents, emails, images) and the snapshots that are copies (`blueprint-r<N>.md`, the release's `build.json` and `backlog.md`) are copied byte for byte and never re-encoded, so a CRLF transcript keeps its CRLF bytes and its recorded sha: C09 covers composed text and C60 covers copies.

**Reason.** BP:123 asks for one written line ending and A§7.1:378 says raw files are never edited, and the two hold together once composed text and copied bytes are kept apart.

**Follow-up.** Record-map edit: RM:96 (encoding, line endings and the JSON form). Design text touch-up: A§5.3:340 adds "written with LF, UTF-8, no BOM; raw files and frozen copies are byte copies"; BP:134 (WP3) writes JSON in the same form.

### G12 Name collision

**Decision.** `add-transcript` and `add-document` build the stem `YYYY-MM-DD-<topic>` from `--date` (default today, local) and `--type` (transcript) or `--title` (document), each a lowercase ASCII hyphenated slug of at most 24 characters for a type and 40 for a title; when any file in the target folder already starts with `<stem>.`, they take `<stem>-2`, then `-3`, and so on, and the file is opened with mode `"xb"` (exclusive create), so no path is ever overwritten, even in a race. A source whose sha256 equals one already recorded in a save entry (G13) is refused as "already saved as <path>", and a document with extension `.md` is refused (its raw name would collide with the snapshot `<stem>.md`) with expected "save the copy as .txt". Transcripts are saved as `calls/<stem>.transcript.txt`; documents and emails as `inputs/<stem>.<source extension, lowercased>`.

**Reason.** A§7.1:441, which wins, makes a second same-day file ordinary with `-2`, and BP:123's "refuses to overwrite" still holds because the script never writes an existing path and refuses the same bytes twice.

**Follow-up.** Record-map edit: RM:74 ("`-2`, `-3`, … assigned by `record.py add-transcript` and `add-document`").

### G13 Where the sha, the input kind and the attachment link are recorded

**Decision.** Each save writes one log entry at strand position `-` (the files are record level), version `-`, type `call` for a transcript or `document` or `email` per `--kind document|email` (default `document`), key the stem, with exactly these body lines: `path: <record-relative path>`, `sha256: <hex of the saved bytes>`, `input_kind: <transcript|document|email> · fixture: <yes|no> · asked_by: <short id> · redactions: <n>`, and, for an attachment only, `came_with: <record-relative path of the email input>`; `CLIENT.md` `last_input` is set to the stem. The attachment link is `add-document --came-with inputs/<file>`, refused unless that path has a save entry with `input_kind: email`; adding an email creates no other file and no link. An email is `.txt` (pasted text) or an image with extension `.png`, `.jpg`, `.jpeg`, `.gif` or `.webp` (a screenshot), any other extension with `--kind email` being refused; `check` blocks on a raw file under `calls/` (`*.transcript.txt`) or `inputs/` (not `.md`) with no save entry, and on one whose bytes no longer hash to the recorded `sha256`.

**Reason.** A§8.3 step 4 (A§8.3:759) already has the save log the sha256 and the redaction count, so the log, which is archived and guarded by "history only grew", is the one durable store, whereas `.work/` is scratch and never archived.

**Follow-up.** Record-map edit: RM:20 and RM:23 ("sha recorded in the save entry of `log.md`"); RM:166 (the save entry's body lines). Design text touch-up: A§8.3:759 names the save entry and its lines; A§8.3:768 names `--came-with`.

### G14 How `check` knows an A11 moment

**Decision.** A11-3 has arrived once any save entry has `fixture: no`: `add-transcript` and `add-document` themselves refuse a save without `--fixture` while `transcripts_at_close` or `transcript_redaction` is `unanswered` (exit 1, naming both fields and the open question, writing nothing), and `check` blocks if a `fixture: no` save entry exists while either field is `unanswered`. A11-2 has arrived when `build_target` is `client-account` and any platform or hybrid strand's `solution/blueprint.md` has `sample_rows: "planned"` (G29), and `check` then blocks while `sample_data_in_account` is `unanswered`; A11-1 has arrived when `account_kind` is `sandbox`, and `check` then blocks while `local/sandbox-accounts.txt` under the home holds no `sandbox` line. `--fixture` is the only way an input is marked fictional (the default is real, so the stop fails closed), no script ever sets an A11 field, and at every other moment no finding of any severity is produced.

**Reason.** BP:23 and A§8.3 step 3 (the input is not saved until the question is answered) settle the moments but not their signals, and these three are the cheapest facts already present in the record or the home.

**Follow-up.** Record-map edit: RM:100 (the A11 sentence names the three signals). Design text touch-up: BP:23 names the signals; A§8.3:758 says `add-transcript` and `add-document` refuse a non-fixture input while A11-3 is unanswered.

### G15 `client/2` fields

**Decision.** `client/2` is A§7.2's list, in its order: `schema`, `slug`, `name`, `account_kind` (`own` | `client` | `sandbox`), `build_target` (`own-account` | `client-account` | `none`), `monday_account_id`, `monday_account_slug`, `monday_bound_user_id`, `monday_bound_at`, `monday_tier`, `monday_tier_read_at`, `monday_tier_source` (`preflight` | `client statement` | `unread`), `products_in_scope`, `client_workspaces` (`"none"` or `product:id` pairs joined by `;`), `record_state` (`active` | `closing` | `closed`), `strands_open`, `strands_total`, `current_strand`, `live_build` (`yes` | `no`), `lease`, `last_input`, `last_researched`, `transcripts_at_close` (`unanswered` | `exclude` | `archive`), `transcript_redaction` (`unanswered` | `none` | `offered-per-call` | `always`), `sample_data_in_account` (`unanswered` | `allowed` | `not-allowed` | `not-needed`), `ai_notice` (`not-yet` | `not-needed` | `given YYYY-MM-DD`), `updated`; there is no `last_call` and no `page_size`. `check` blocks on a missing field, a value outside its set, an `account_kind` that does not match `build_target` (own and own-account, client and client-account, sandbox and none), and a binding mirror that differs from `account.json`: `monday_account_id` and `account.id`, `monday_account_slug` and `account.slug`, `monday_bound_user_id` and `account.bound_user_id`, `monday_bound_at` and `account.bound_at`, `build_target` and `account.build_target`, `account_kind` and `account.kind`, `client_workspaces` and `account.json` `client_workspaces` (`"none"` matching `{}`); it warns on an unknown field.

**Reason.** A§7.2:447 to 477 wins over RM:100 and BP:198 already follows it; `account.json` needs a `bound_at` for RM:100's "mirrors it here" to hold for all four binding fields.

**Follow-up.** Record-map edit: RM:100 rewritten to this list; RM:116 (`account` gains `bound_at` and `build_target`, `kind` becomes `own` | `client` | `sandbox`). Design text touch-up: A§7.3:493 example `account` gains `"bound_at"`; BP:134 (WP3) `bind` writes it.

### G16 `strand/1` fields and stage ladder

**Decision.** `strand/1` is A§7.7:651 to 676 in its order: `schema`, `strand`, `slug`, `title`, `kind`, `output_class`, `opened`, `opened_reason`, `state`, `stage`, `version`, `version_state`, `clearance`, `override`, `round`, `workspaces`, `next_step`, `depends_on`, `summary_current_to`, `closed`, `updated`; `stage` takes `new | intake | readiness | blueprint | building | audited | shown | signed-off | closing | closed` on a platform or hybrid strand and `new | scoping | handed-off | closed` on a non-platform one, and there is no `discovery_verdict` and no `sop_behind`. `version mark` sets `stage` to `shown` or `signed-off`, except that a `shown` event leaves a stage of `signed-off` as it is; `strand close` sets `closed`; `check` blocks on a stage outside the ladder for the strand's kind.

**Reason.** A§7.7 wins over RM:104, whose grading and SOP fields D1, D2 and D5 removed.

**Follow-up.** Record-map edit: RM:104 rewritten to this list.

### G17 Version states and `version/1`

**Decision.** Version states are `planned`, `approved`, `building`, `built`, `fixing`, `audited`, `released`, with no `demoed`. `version/1` front matter, in order: `schema`, `strand`, `version`, `qualified_version`, `state`, `purpose` (`proof-of-concept` | `working-solution`), `revision` (`"none"` or an integer string), `sha256` (`"none"` or hex), `opened`, `released` (`"none"` or a date), `shown` (`"none"` or dates joined by `; `), `signed_off` (`"none"` or a date), `close_reason` (G07), `updated`; the body carries `## Scope`, `## Build`, `## Reactions` and `## Events` (G20), and `demo_script_ready` and `sop_sections_confirmed` are gone. `check` warns when the current version's `state` differs from `STRAND.md` `version_state`.

**Reason.** A§7.4:589 to 608 and BP:198 win over RM:112 and RM:156 (D2: `shown` is an event, not a state).

**Follow-up.** Record-map edit: RM:112, RM:156.

### G18 Strand index header

**Decision.** The index is the block under the heading `## Strand index` in the body of `CLIENT.md`: the header line `| strand | title | kind | state | version | version state | clearance | live objects | last activity |`, the separator `|---|---|---|---|---|---|---|---|---|`, then one row per strand ordered by short id, the first cell being the short id; `check` reads only lines inside that block whose first cell matches `\d{3}`. There is no `verdict` and no `SOP behind` column; what `check` compares is in G06.

**Reason.** A§7.2:481 wins over RM:87 to 92, whose `verdict` and `SOP behind` are v2 (D1, D5).

**Follow-up.** Record-map edit: RM:87 to 92 (header and example row).

### G19 `status --json` strand and top-level fields

**Decision.** `status` (with or without `--json`, which prints the same object) returns `{"schema": "status/1", "generated_at", "plugin_version", "record_schema", "schema_newer", "record", "strands", "lease", "interrupted", "findings"}`, where `schema_newer` (boolean, G57) replaces `migration_needed`, `record` holds every `CLIENT.md` front-matter key as the string it is, and `findings` is `check`'s `{blocking, warnings}`. Each `strands[]` entry holds every `STRAND.md` front-matter key as a string, plus `qualified_version` (`"001/v0.1"` or `null`), `purpose` (the current version's `version.md` `purpose`, or `null`), `shown` (array of the current version's shown dates, possibly empty), `signed_off` (its date or `null`), and `open_versions`, `live_objects`, `last_activity` and `run` (G54); `stage`, `clearance`, `version` and `version_state` come through as `STRAND.md` keys, so BP:123's purpose and A§5.4:354's `shown` and `signed_off` are all present. The lease block is G02's lock fields as `{held, state, epoch, strand, strand_title, version, session_label, run_id, taken_at, heartbeat_at, heartbeat_age_minutes, fresh}`, with `heartbeat_age_minutes` and `fresh` `null` when nothing is held, and `--strand <id>` narrows only `strands`.

**Reason.** A§5.4:354 and BP:123 each add fields to RM:142 to 152 and D8 dropped migration, so the object is the union, with the dead field replaced by the one fact the front door needs on a newer record.

**Follow-up.** Record-map edit: RM:142 to 152.

### G20 Event data

**Decision.** `version mark shown --strand <id> --date YYYY-MM-DD --audience "<roles>" --account "<account slug>" --words "<the user's words>"` and `version mark signed-off --strand <id> --date YYYY-MM-DD --by "<role>" --words "<the user's words>" [--go-on]`, with `--version vX.Y` defaulting to `STRAND.md` `version`, `--date` to today and `--account` to `CLIENT.md` `monday_account_slug`. Each event appends one entry under `## Events` in `version.md`: `### shown YYYY-MM-DD` with lines `- audience: ...`, `- account: ...`, `- words: "..."`, or `### signed-off YYYY-MM-DD` with `- by: ...`, `- words: "..."` and `- unconfirmed structural assumptions:` followed by one indented line per item (G21) or `none`. Front matter `shown` gains the date (repeat events are all kept) and `signed_off` is set, and a `shown` or `signed-off` log entry is written at the strand position with the version.

**Reason.** BP:123 (date, the user's words, the account) and A§7.4:593 and A§8.8:815 (audience or signer by role) do not conflict, so the event records the union.

**Follow-up.** Record-map edit: RM:112 (the events block). Design text touch-up: A§8.8:815 and A§8.8:817 give the full flag lists.

### G21 "Structural assumption"

**Decision.** A structural assumption is an entry of the strand's `readiness.md` assumptions of kind `automation-condition`, `board-architecture` or `leaning` in state `assumed`; `gap` and `call-type` are not structural, and an `accepted` entry counts as explicitly accepted. `record.py` reads them from `strands/<id>/readiness.md`, inside the section headed `## Assumptions`, one assumption per line in the pinned form `- <statement> [kind: <kind>; state: <assumed|accepted>]`, with its question on the next line as `  question: <text>`. It never changes an assumption's state, which moves only when the user reports the client's word through the readiness skill.

**Reason.** AM:47 and AM:49 name the automation conditions, the board-architecture overview and a fork built on its leaning, which are exactly three of RM:206's kinds, and `readiness.md` is where A25 keeps assumptions until a confirmation takes one off the list.

**Follow-up.** Record-map edit: RM:191 and RM:206 (the line form in `readiness.md`). Design text touch-up: BP:198 (WP7), the `readiness.md` template's part 5 uses that line form.

### G22 Warn then record

**Decision.** Two calls. `version mark signed-off ...` without `--go-on` records the event at once when the list is empty (exit 0); otherwise it records nothing, prints the list under `"unconfirmed"` with `"recorded": false`, and exits 2. The same call with `--go-on`, made after the user has seen the list and said to go on, records the event with the list as it reads at that moment, prints it with `"recorded": true`, and exits 2 when the list is non-empty; no path through the command exits 1 because of assumptions.

**Reason.** BP:123, A§5.4:354 and BP:533 put the user's choice between the warning and the record, and a script cannot prompt, so the choice arrives as a flag.

**Follow-up.** Design text touch-up: A§5.4:354 and A§8.8:817 name `--go-on`.

### G23 What makes a version `v1.0`

**For the user.** What recording `signed-off` on a `v0.x` does to that version: A§7.4:587 and A§8.8:817 say the sign-off "is what v1.0 means", BP:123 ties purpose to the version number, and a version folder is never renamed. The question for the user: when the client signs off a `v0.3` build as their working system, should that `v0.3` itself become the working solution, or should the next version be opened as `v1.0`?

**Decision (recommended default, built until the user answers).** Purpose follows the version number only: `version open` writes `proof-of-concept` below `v1.0` and `working-solution` from `v1.0`, and no event changes it. A `signed-off` event on a `v0.x` is recorded with its warning and leaves that version a proof of concept; the front door then proposes `version open --version v1.0` as the next version, and releasing any version from `v1.0` on refuses until that version carries its own `signed-off` event. The alternative the user may prefer: the event sets the signed-off version's `purpose` to `working-solution`, and `version open` after it defaults to `v1.0`.

**Reason.** The sources state both readings and no source wins between them; the default keeps purpose a pure function of a name that never changes (A§5.3:341), which is the simplest to code and test.

**Follow-up.** Design text touch-up after the answer: A§7.4:587, A§8.8:817, BP:123 and BP:533 (H66) say which reading holds.

### G24 `version mark` preconditions

**Decision.** `version mark` refuses (exit 1) unless the target version's `version.md` `state` is `audited` or `released`, with expected "an audited or released version"; it also refuses on a `non-platform` strand, which has no versions, and on a `closed` strand.

**Reason.** A§7.4:593 states the precondition and wins over BP:123's silence on it.

**Follow-up.** None.

### G25 Subcommands with a name and no acceptance sentence

**Decision.** `version open --strand <id> [--version vX.Y]` creates `versions/<v>/version.md` from the template (G17 fields; `state: "planned"`, `purpose` from the number, `revision: "none"`, `opened` today) and sets `STRAND.md` `version` and `version_state: "planned"`, defaulting to the next minor after the highest existing version (`v0.1` first) and refusing an explicit version not above it, an existing folder, and a `non-platform` or `closed` strand. `version condense-plan --strand <id> --from <plan.json>` validates a plan the session wrote, a list of `{"file", "line", "survives_in"}` (`file` a current file of the strand, `line` present verbatim in it, `survives_in` an existing record-relative file; an entry without `survives_in` is refused, so a line with no surviving copy can never be removed), stores it with each file's sha as `.work/strands/<id>/condense-plan.json` and prints it with its sha; `version condense-apply --strand <id> --plan-sha <hex>` removes those lines through guarded writes, refusing a different sha or a file changed since the plan, and both refuse while any strand holds the lease. `strand list` prints `{"strands": [...]}` with the nine index cells per strand (G18), and `card --strand <id>` copies the record's `client-card.md` to `<home>/cards/<slug>.md` (backing up an existing card per G39), `--strand` only stamping who asked, with a `closeout` log entry at position `-`.

**Reason.** A§5.4:354 names these subcommands and no source describes them, so each gets the narrowest behaviour its name and A§7.4:610 and A§8.10:830 ("the card is copied to `<home>/cards/`") support.

**Follow-up.** Design text touch-up: A§5.4:354 describes `version open`, the condense pair, `strand list` and `card`; A§8.10:830 says `record.py card` does the copy.

### G26 What `version release` does

**Decision.** `version release --strand <id> --condense-plan-sha <hex> --summary-plan-sha <hex> [--version vX.Y]` refuses while the lock is `held` by any strand, unless the version's `state` is `audited`, while any file the release needs is missing (G27, listed in the refusal), while a version from `v1.0` on has no `signed-off` event, and when either sha does not match its stored plan; a `shown` or `signed-off` event is not otherwise a precondition. In the user's one yes it then: copies `solution/build.json` and `solution/backlog.md` byte for byte into `versions/<v>/`, rolls the version's log entries into `versions/<v>/log.md` (G08), applies the condense plan (G25), writes `SUMMARY.md` from the summary plan (G42), sets `version.md` `state: "released"` and `released`, sets `STRAND.md` `version_state: "released"` (when it is the current version) and `summary_current_to`, refreshes the index, and returns the result of `check`'s `released`-row checks. There is no `updates.md` snapshot.

**Reason.** A§7.4:606 and A§7.4:610 win over RM:53 and RM:156, and A§8.8:818 reads as the moment the front door proposes a release, not as a refusal.

**Follow-up.** Record-map edit: RM:53 and RM:156 (drop `updates.md`).

### G27 Required-file severity

**Decision.** For each version, `check` requires the files of its current state's row and of the rows it has passed through, except that `building` and `fixing` are checked only while current: `planned` (`solution/blueprint.md`; `version.md` with `revision` not `none` and a `## Scope` heading); `approved` (`blueprint-r<revision>.md` whose sha equals `version.md` `sha256` and the `build.json` approval entry for that version and revision; an `approval` log entry at the strand position with that version); `building` (a `running` run for the version with `lease_epoch` and `another_build_running` set, the lock `held` by this strand, `change_check.for_strand` this strand, `preflight.version` this version); `built` (a `## Build` heading in `version.md`; a `build` log entry); `fixing` (an `audit*.md` with `## Findings`); `audited` (the newest `audit*.md` with `## Write detection`, `## Documents appendix` and a last non-empty line `cleared to show` or `not cleared to show`); `released` (`versions/<v>/build.json`, `backlog.md`, `log.md`, and from `v1.0` a `signed-off` event). A missing file is a warning in every state but `released`, where it is blocking, and `version release` refuses on any missing file of the rows it needs (G26), which is where "blocking at release" bites; "condensed current files" is not checked by a script.

**Reason.** A§5.4:354 ("blocking at release") and RM:156 ("a missing file blocks the release") win over a reading in which every intermediate state blocks, and the headings are the smallest strings that make A§7.4:598 to 606 checkable.

**Follow-up.** Record-map edit: RM:156 (the pinned headings and the severity). Design text touch-up: BP:198 (WP7), the `version.md` and `audit.md` templates carry those headings; A§7.4:598 states the severity.

### G28 Where `readiness.md` carries the clearance

**Decision.** `readiness.md` carries the clearance in its front matter as `clearance`, holding the human string `cleared to build`, `cleared to build, generic` or `not yet`, or `none` before the check has run (`strand open` writes `none`); the machine value stays `verdict.cleared_for` (`build` | `build-generic` | `not-yet`) in the body for `solution-blueprint`, and `check` reads only the front-matter field. Any other value, a machine value included, is blocking, with the four allowed strings as expected; a difference between `readiness.md` `clearance` and `STRAND.md` `clearance` is a warning.

**Reason.** A§6:369 ("the clearance and its conditions in front matter") and A§5.4:354 win, and the human strings are the ones BP:123 and A§7.7:666 spell, while RM:212 keeps the machine value for the blueprint.

**Follow-up.** Record-map edit: RM:191 and RM:212 (the front-matter `clearance` and its four values). Design text touch-up: BP:198 (WP7), the `readiness.md` template's front matter has `clearance: "none"`.

### G29 The signal for "plans sample rows"

**Decision.** The signal is one front-matter field of the strand's `solution/blueprint.md`, `sample_rows` (`"planned"` | `"none"`), shipped `"none"` in the template and set by `solution-blueprint` when the current revision plans sample rows. `check` blocks on `sample_rows: "planned"` with `solution/exclusions.md` absent (C136), and the same field marks the A11-2 moment (G14).

**Reason.** No source names the signal, and a flat front-matter field on the file that plans the rows is the one fact a script can read without parsing a later package's prose.

**Follow-up.** Record-map edit: RM:112 (`blueprint/1` carries `sample_rows`). Design text touch-up: BP:198 (WP7, the `blueprint.md` template) and BP:244 (WP9, `solution-blueprint` sets it).

### G30 `check` duties and severities

**Decision.** Blocking: malformed front matter, a missing or misplaced `schema`, a newer or unexpected schema (G57), an absolute path, any of the nine markers or an internal id under `drafts/` (G61), an edited or unrecorded raw input (G13), a frozen blueprint whose sha differs, and a build target outside the client's workspaces (G47). Warning: a quote marker without a location (G61), a missing "Internal: never client-facing" line (expected as the first line after the front matter of every record `.md` except those under `drafts/` and `CLAUDE.md`), a stale native index (`guard_index.captured_at` older than `record_provenance.staleness_budget_days`), and a stale lease (G48). An absolute path is a token in a composed record file (not a raw input, not under `.work/`) that matches a drive path `[A-Za-z]:[\\/]`, a UNC path `\\host\`, `~/`, or `/` followed by one of `Users`, `home`, `Volumes`, `private`, `tmp`, `var`, `opt`, `mnt`, `root`, `etc`, `usr`, `srv`, `media` and a further segment, each preceded by the start of a line, whitespace, a quote or `(` and not inside a URL, so both spellings report alike on both systems; an internal id is a qualified key (`\d{3}:[A-Z]+\d`), a qualified version (`\d{3}/v\d+\.\d+`), a session label, a run id (`run-\d{4}-\d{2}-\d{2}-\d+`) or a gotcha id (`G-\d{2,3}`), never a bare element key, which ordinary prose collides with. "A stale native index downgrades guarded writes to an ask" in H20 is the hook's behaviour (WP13); WP2's half of H20 is that `check` reports it.

**Reason.** BP:448 and BP:487 list the defects H20 must name without severities, so blocking is kept for what corrupts the record or leaks the user's machine or internal ids, and warning for legitimate state and hygiene.

**Follow-up.** Design text touch-up: BP:487 (H20) moves "downgrades guarded writes to an ask" to WP13's `test_guard.py`; A§5.4:354 states the severities.

### G31 Templates in stage 2

**Decision.** Templates are read from `<plugin root>/templates/record/<name>`, the plugin root being `Path(__file__).resolve().parent.parent`, never an environment variable; `record.py` fills a template by copying it and setting only the front-matter keys it owns (G38's writer), and refuses with exit 3 when the template or one of those keys is missing. In stage 2 the WP2 fixture carries minimal stand-in templates (`STRAND.md`, `readiness.md`, `exclusions.md`, `version.md`, and the `CLIENT.md`, `log.md`, `account.json` and lock shapes the fixture tree uses) under `tests/unit/fixtures/plugin/templates/record/`, and the tests copy `scripts/`, those templates and a stand-in `.claude-plugin/plugin.json` into a temporary plugin root and run from there; in stage 3 the same tests run again against WP7's real `templates/`.

**Reason.** BP:70 accepts everything but `init` and `home init` in stage 2 against WP2's own fixtures, and a temporary plugin root also exercises C18 and the plugin-root lookup of G36 without any test-only switch in shipped code.

**Follow-up.** Design text touch-up: BP:198 (WP7), every template carries the front-matter keys `record.py` sets (G16, G17, G28, G29).

### G32 `home init` interface and what it can check

**Decision.** `home init` takes the answers as flags: `--firm-name "<name>"`, `--firm-rendering "<text>"` (repeatable), `--default-account-slug <slug>`, `--default-account-id <id>`, `--never-show "<workspace id>=<name>"` (repeatable, optional), `--archive local|github` (default `local`), `--github-account <account>` (required with `github`, refused with `local`), `--home <folder>` (G35) and `--update` (G33); on a home with no `settings.json` the firm name and the default account are required. It reports `checks`: `python` (version, at least 3.9), `plugin_root` (the path and whether `plugin.json` reads), `connector` as `"checked by the session"` (a script cannot see the session's tool roster), and, only with `--archive github`, `git` and `gh` as `found` or `absent` through `shutil.which`, running no external command. The two doors and the one-session-per-client rule are explained by the walkthrough reference `first-run.md` (WP8), not by the script, so C33's connector half and C37 move to WP8's half of H57.

**Reason.** BP:123 and A§5.4:354 say what `home init` writes and checks but not how the answers arrive, and the connector's presence in the roster is readable only inside the session.

**Follow-up.** Design text touch-up: A§5.4:354 and A§8.2:745, the session checks the connector; BP:524 (H57) gives "the two doors are explained" and the connector check to WP8's half (BP:207).

### G33 Re-running `home init`

**Decision.** A re-run never replaces `local/settings.json`: without `--update` the file stays byte-identical and the output says `"settings": "kept"` with the way to change an answer; with `--update` and one or more answer flags it backs the file up (G39) and rewrites in place only the keys those flags name, refreshing `plugin_version`, keeping `created` and every other key, and removing `github_account` when the archive becomes `local`. Folders and seeded files that exist are left as they are, and missing ones are created.

**Reason.** A§5.4:354, which wins, allows changing an answer the user asks to change, and BP:123's and H57's "never overwrites ... says so" hold for every run that does not ask.

**Follow-up.** Design text touch-up: BP:123 and BP:524 add "unless `--update` names the answer to change".

### G34 `settings.json` key names

**Decision.** `local/settings.json` is `{"schema": "settings/1", "created": "YYYY-MM-DD", "plugin_version": "<from plugin.json>", "firm": {"name": "...", "renderings": ["..."]}, "default_build_account": {"slug": "...", "id": "..."}, "never_show_workspaces": [{"id": "...", "name": "..."}], "archive": "local" | "github", "github_account": "..."}`, every id a string, `never_show_workspaces` possibly empty, and `github_account` present only when `archive` is `github`. `check` warns, with `local/settings.json` as the file, when the file is absent or breaks this shape; `local/sandbox-accounts.txt` keeps the RM:68 syntax.

**Reason.** BP:106 asks `record-map.md` to carry these fields and no source names them, so the names follow A§5.3:345's wording.

**Follow-up.** Record-map edit: RM:68 (the `settings.json` fields).

### G35 Setting `MMB_HOME`

**Decision.** `home init` never sets an environment variable and never edits a profile or a settings file outside the home; it resolves the home from `MMB_HOME`, else `Path.home() / "monday-builder"`, and `--home <folder>`, accepted only while `MMB_HOME` is unset, creates the tree in a folder the user named. When the home used is not the default, the output carries `"set_mmb_home"` with the line that records it: an `"env": {"MMB_HOME": "<folder>"}` entry in the user's Claude Code user settings, which applies to every session on Windows and macOS alike without assuming a shell, and, as the system's own alternative, `setx MMB_HOME "<folder>"` on Windows or a line in the login shell's profile on macOS. The walkthrough (WP8) offers to add the settings entry with the user's yes and otherwise shows the line; the home's own location is not stored in `settings.json`, which lives under it.

**Reason.** A§5.3:345 says the walkthrough says how to set the variable on the system it runs on, and a child process cannot set its parent's environment, so the script states the form and the session applies it with the user's yes.

**Follow-up.** Design text touch-up: A§5.3:345 and BP:123 ("sets in the environment") name the Claude Code settings `env` entry; BP:207 (WP8, `first-run.md`) carries the offer.

### G36 Invocation form and finding the plugin

**Decision.** Each script resolves everything from its own location: the plugin root is `Path(__file__).resolve().parent.parent`, `plugin.json` is `<plugin root>/.claude-plugin/plugin.json` (read for `version`; missing or unreadable is exit 3), and templates are found as in G31; no script reads `CLAUDE_PLUGIN_ROOT`, so the scripts behave the same under `python3`, `python` or `py -3`. Each script checks `sys.version_info >= (3, 9)` before anything else and exits 3 below it, and the unit tests launch scripts as `[sys.executable, str(script_path), ...]` with no shell. The shared form in skill text stays `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/<name>.py"`, proven on macOS, until the stage-5 Windows re-run fixes the Windows spelling of the interpreter command; C22 is accepted only at that run.

**Reason.** A§5.2:336 defers the form to the Windows re-run, which lands in stage 5 (BP:80 to 84), and locating files from `__file__` leaves only the interpreter command for that run to settle.

**Follow-up.** Design text touch-up: A§5.2:336 records that the scripts find the plugin from their own path, so only the interpreter command remains for the re-run.

### G37 Range of the `CLAUDE.md` warning

**Decision.** The warning names every folder from the home itself (`MMB_HOME` or the default) up to the filesystem anchor (walking `Path.parents`, so up to `C:\` or `/`) that holds a file named `CLAUDE.md`; `clients/` and everything below it are not searched, since a client folder's own `CLAUDE.md` is intended (A22). Each hit is one warning with the folder as `file` and expected "no CLAUDE.md above the clients folder"; the test plants the file in the temporary home's parent and asserts that folder is named.

**Reason.** A§5.3:345 and BP:123 say "any folder above `clients/`", the home folder is the first such folder, and a session inherits every ancestor's `CLAUDE.md` up to the root.

**Follow-up.** Design text touch-up: A§5.3:345 adds "from the home folder up to the root of the drive".

### G38 Front matter details

**Decision.** Front matter is the lines between a first line `---` and the next `---`; each non-blank line is either a comment line (optional whitespace, then `#`) or `key: "value"`, with `key` matching `[a-z_][a-z0-9_]*` and an optional `# comment` after the closing quote, and inside a value `\"` is a quote, `\\` a backslash and every other character literal. The writer changes only the quoted value of the line it sets and keeps everything else on that line (spacing, comment) and every other line (comments, blank lines, unknown keys, order) byte for byte, appends a new key as `key: "value"` just before the closing `---`, sets `updated` to the local minute (G40) on every write, and refuses a file with a parse error (an unquoted value, a duplicate key, `schema` not the first key, no closing `---`), which `check` reports as blocking with the key as field. Values are single-line strings.

**Reason.** BP:123 (quotes preserved) and A§5.3:342 leave the rest open, and BP:198 puts the stage ladders in comments, which therefore have to survive every rewrite.

**Follow-up.** Record-map edit: RM:96 (escapes, comments, new and unknown keys).

### G39 Backup naming and place

**Decision.** Before an in-place rewrite of a current file, its old bytes are copied to `.work/backup/<record-relative path>.<UTC stamp YYYYMMDDTHHMMSSffffffZ>` (folders created as needed, the file opened with `"xb"`, `-2` appended on a clash), one new file per rewrite, kept until the user clears `.work/` by hand; strand files therefore land under `.work/backup/strands/<id>/...` and no per-strand `backup/` folder is used. A lease refresh that changes only the heartbeat writes the `account.json` mirror without a backup (the lock's history is the record of state changes), while every take, release and break backs up both mirror files. Files under the home are backed up to `<home>/local/backup/` (`settings.json`) or into the record's `.work/backup/home/` (a card).

**Reason.** A§5.3:341 and BP:123 ask for a backup before every rewrite, timestamped generations are the only naming under which no backup is itself overwritten, and skipping heartbeat-only backups keeps a long build from writing one `account.json` copy per ledger write.

**Follow-up.** Record-map edit: RM:66 (`backup/` naming). Design text touch-up: A§7.1:437 drops the per-strand `backup/`.

### G40 Time format and zone

**Decision.** Machine timestamps in JSON (the lock and its history, the `guard_index.lease` mirror, `status` `generated_at`, `reconcile.at`) are UTC as `YYYY-MM-DDTHH:MM:SSZ`, written from `datetime.now(timezone.utc)` and parsed with `strptime(value, "%Y-%m-%dT%H:%M:%SZ")` (Python 3.9's `fromisoformat` rejects `Z`); every age and the 60-minute rule are computed from them, stale meaning more than 3,600 seconds and `heartbeat_age_minutes` the floor of the elapsed minutes. Human-facing values are the writing machine's local time with no zone, as the shapes show them: `updated` (`YYYY-MM-DDTHH:MM`), the log header (`YYYY-MM-DD HH:MM`), dates (`YYYY-MM-DD`) and the label's `YYYYMMDD-HHMM`. The clock is one function in `mmb_common` that tests patch in process; shipped code has no clock override.

**Reason.** A§7.2:475 and A§7.3:499 show both forms without a rule, and UTC for everything that is compared makes the stale test identical across zones and clock changes, while local time keeps what the user reads in their own day.

**Follow-up.** Record-map edit: RM:96 (the two time forms).

### G41 `freeze`

**Decision.** `freeze --strand <id>` reads `STRAND.md` `version` (refusing `none` and a `non-platform` strand) and that version's `version.md` `revision` (refusing `none`), takes the sha256 of `solution/blueprint.md`'s bytes, copies them with `"xb"` to `versions/<v>/blueprint-r<revision>.md` (refused if it exists, so a second freeze of one revision is refused and a changed blueprint needs a new revision), re-reads the copy, and prints `{"working_sha256", "frozen_sha256", "frozen_file", "revision"}`, exiting 3 if the two differ. It then sets `version.md` `sha256`. `solution-blueprint` advances `revision` (through `guard`) when it drafts a revision, and the approval entry, its log entry and the `approved` state belong to the approval step, not to `freeze`.

**Reason.** BP:123 asks for two matching values and A§7.4:601 for the sha in `version.md` and the approvals, and a byte copy verified by a re-read gives both without line-ending doubt (G60).

**Follow-up.** Design text touch-up: A§8.5:785 (step 8) says `freeze` reads `revision` from `version.md` and writes its `sha256`.

### G42 `strand summary`

**Decision.** Two steps: `strand summary --strand <id> --plan <draft.md>` validates a draft the session wrote, stores it as `.work/strands/<id>/summary-plan.md` and prints its sha; `strand summary --strand <id> --apply <sha>` writes `SUMMARY.md` from the stored draft as a guarded write and sets `STRAND.md` `summary_current_to`. Validation sets the front matter (`schema: "summary/1"`, `strand`, `title`, `kind` and `closed` from `STRAND.md`, `versions` the released versions joined by `, `, `summary_current_to` the newest released version or `none`, `budget_lines: "80"`), requires the nine headings in order, `## What the work was`, `## Pains it served`, `## What was built`, `## What the client confirmed`, `## What must not be broken`, `## Cost of change, in the client's words`, `## Ownership and switch-off at close`, `## Backlog seeds carried forward`, `## Dates` (opened, shown, signed off, released, closed), requires `nothing built inside the product` as the third block's text on a `non-platform` strand, and refuses a result over 80 lines. The prose of every block is the session's; `check` warns past 80 lines and blocks past 120.

**Reason.** A§7.7:684 wins over RM:108 on the dates, and a script can hold the shape, the budget and the yes but cannot write pains in the client's vocabulary, so the session drafts and the script validates and writes.

**Follow-up.** Record-map edit: RM:108 (the nine headings and the dates). Design text touch-up: A§7.7:684 names the two steps.

### G43 What `strand open` writes

**Decision.** `strand open --topic <slug> --title "<title>" --kind platform|non-platform|hybrid --reason "<why>" [--output-class configured-structure|bespoke-code|hybrid] [--depends-on <short ids>]` creates `strands/<NNN-topic>/` and its `solution/`, writes `STRAND.md` from the template with `strand`, `slug`, `title`, `kind`, `output_class` (default `configured-structure` for platform, `bespoke-code` for non-platform, `hybrid` for hybrid), `opened` (today), `opened_reason`, `state: "active"`, `stage: "new"`, `depends_on` (default `none`) and every other field `"none"`, places `readiness.md` (with `clearance: "none"`) and `solution/exclusions.md` from the templates, writes a `strand` log entry ("opened", with kind and reason) and refreshes the index (G06). It creates no `versions/`, `blueprint.md` or `build.json` for any kind; `init` creates strand 001 through the same code and, per BP:384, also places strand 001's `build.json` template copy for a platform or hybrid first strand, which matches an unbound record, while on a later strand `build.json` is created by `ledger.py` at its first write, so no template copy can disagree with a bound account (C126).

**Reason.** BP:123 names only the two templates, A§7.7:651 to 676 gives the fields, and A§7.7:682 makes the kind the user's answer, which leaves only defaults for the script to choose.

**Follow-up.** Design text touch-up: A§7.7:682 states the `output_class` defaults.

### G44 Budgets

**Decision.** Budgets are A§7.1's: `readiness.md` 250 lines, `solution/exclusions.md` 80, `versions/<v>/build-notes.md` 250, and the rest of A§7.1:384 to 428; a budget given in lines and KB warns when either is exceeded (one finding naming both), KB being 1,024 bytes and lines counted with `splitlines()`, and the record `log.md` warns past 300 lines. The soft 4 MB is the total size of the record's files excluding `calls/*.transcript.txt`, every non-`.md` file directly under `inputs/`, and `.work/`; past 4,194,304 bytes it warns once and names the three largest strand folders with their sizes.

**Reason.** A§7.1 wins over RM:37 and RM:64.

**Follow-up.** Record-map edit: RM:37 (readiness 250 lines); the strand table gains `solution/exclusions.md` (80 lines) and `versions/<v>/build-notes.md`, `build-notes.html` (250 lines); RM:64 (the excluded set).

### G45 `log` input validation and the type list

**Decision.** The type list is A§7.6:645's 44 types, embedded in `record.py` between pinned markers so `tools/lint_plugin.py` can assert it agrees with `record-map.md`. `log --strand <short id or -> --type <type> --version <vX.Y or -> --key "<key or session label>" (--line "<text>" ... | --body-file <path>)` refuses an unlisted type, more than five body lines, an empty or multi-line key, a key containing ` · `, a body line starting with `## `, a strand position that is neither `-` nor an existing strand's short id, and a version that matches neither `v\d+\.\d+` nor `-`. The entry's time comes from the clock (G40), never from the caller, and `check` warns on an existing entry with more than five body lines, since history is never edited to fix it.

**Reason.** A§7.6:645 wins over RM:166 (D8 dropped `migration`, D5 the SOP and demo types), and refusing at the one writer is the cheapest way to keep every header parseable.

**Follow-up.** Record-map edit: RM:166 (the 44 types and the pinned-marker note).

### G46 `.work/` layout and dropped items

**Decision.** `.work/` holds `lock.json`, `history.json` (G08), `record.mutex` (G09), `intake/`, `backup/` (G39), and per strand `strands/<id>/` with `live-inventory.json`, `audit/`, `build.json.bak`, `condense-plan.json` and `summary-plan.md` (G25, G42). `cards-index.json`, `migration-sources/`, `claims-queue/`, `tools/<plugin-version>/`, `leases.json` and `claims/` do not exist; `record.py tools-check` and `record.py migrate` do not exist and fall to the unknown-subcommand exit 3 (G10); record-map's "Scripts the record copies" and "Migration" sections go.

**Reason.** A§7.1:437 and D8, D9, D10 and D13 win over RM:66, RM:68 and RM:272 to 282.

**Follow-up.** Record-map edit: RM:66, RM:68; delete RM:272 to 278 and RM:280 to 282. Design text touch-up: A§7.1:437 lists the added files.

### G47 `guard_index` and "the client's workspaces"

**Decision.** For the out-of-scope build target, the client's workspaces are `account.json` `guard_index.client_workspace_ids`: `check` blocks, naming the strand and the id, on any id in `guard_index.build_targets_by_strand[<strand>].workspace_ids` that is not in that list. The `CLIENT.md` string `client_workspaces` and `account.json` `client_workspaces` are compared as a mirror under G15, and `guard_index.lease` uses `session_label` (G01).

**Reason.** A§7.3:537 makes `client_workspace_ids` the set that `intent` and the hook refuse against, and A§7.3:522 to 524 win over RM:116.

**Follow-up.** Record-map edit: RM:116 (`guard_index` gains `client_workspace_ids`; `lease` uses `session_label`).

### G48 Severity of a stale lease in `check`

**Decision.** A held lease whose heartbeat is stale is a warning (file `.work/lock.json`, field `heartbeat_at`, problem "held by <strand> (<title>) <version>, session <label>, heartbeat <n> minutes old: stale", expected "resume the holder in a fresh session, or break the lease"), carried in `status` findings as well; it never blocks by itself, since the release, the audit and the record close already refuse on any held lease.

**Reason.** A§9.8:943 makes a stale held lease legitimate, lasting state until someone breaks it, and H20 (BP:487) needs it named, not blocking.

**Follow-up.** Design text touch-up: A§9.8:943 adds "`record.py check` reports it as a warning".

### G49 Bytecode cache

**Decision.** Every shipped script that imports a sibling sets `sys.dont_write_bytecode = True` as its first statement after `import sys`, before importing `mmb_common`, so no `__pycache__` is written beside the scripts; the unit tests set it before importing from the temporary plugin copy and pass `PYTHONDONTWRITEBYTECODE=1` in every subprocess's environment. C18's test runs every subcommand from a writable temporary copy of the plugin folder and asserts that the copy's file list is unchanged afterwards, since a read-only copy would hide the cache (Python skips it silently there).

**Reason.** BP:123 forbids writes into the plugin folder, and the import of `mmb_common` is the one write Python makes there on its own.

**Follow-up.** Design text touch-up: the acceptances of WP3 (BP:134), WP4 (BP:157), WP5 (BP:167), WP12 (BP:296) and WP13's `guard.py` (BP:305) carry the same first line.

### G50 `lease take` inputs and `run_id`

**Decision.** `lease take [build] --strand <id>` (the kind word optional, `build` its only value) reads `title` and `version` from the strand's `STRAND.md`, refuses `version: "none"`, a `non-platform` strand, a `closed` strand and a `held` lock (G53), sets `run_id` to `null`, and prints `{"epoch", "session_label", "strand", "version", "taken_at"}`. `run_id` enters the lock once, through the refresh primitive's optional `run_id` argument, which `ledger.py run start` passes and which is accepted only while the lock's `run_id` is `null`.

**Reason.** BP:248 and A§7.4:602 have the take precede the run, so `run_id` cannot be known at the take, and reading the title and version from `STRAND.md` keeps the call to the one argument BP:248 shows.

**Follow-up.** Design text touch-up: A§9.8:933 says `run_id` is set by the first refresh after `run start`; BP:134 (WP3) `run start` refreshes with `run_id`.

### G51 The fence comparison

**Decision.** `mmb_common` exposes the one comparison, `lease_fence(record_root, epoch, session_label, run_id)`, returning `(ok, reason)` from a read under the mutex: ok only when `state` is `held`, `epoch` and `session_label` equal the lock's, and `run_id` equals the lock's (or the lock's is still `null`, before `run start`), the reason naming which of the three failed. `ledger.py` calls it before every account-affecting write and never parses the lock itself, and C113 is tested against this function.

**Reason.** BP:68 and A§5.4:353 make `mmb_common` the lease's one module, and one implementation of the three-part fence is what H35's old-epoch, old-label and old-run cases rest on.

**Follow-up.** Design text touch-up: A§5.4:353 lists `lease_fence` among the primitives; BP:134 (WP3) calls it.

### G52 `strand pause`

**Decision.** `strand pause --strand <id> --reason "<the user's words>"` refuses a strand that is not `active` and a strand that holds the lease (fresh or stale), sets `state: "paused"`, writes the `STRAND.md` body block `## Paused` with `- paused YYYY-MM-DD by the user: <reason>` (replacing any earlier content of that block; appended at the end of the body when the block is absent), writes a `strand` log entry ("paused") and refreshes the index. A park writes the same block from the break (G04), and `strand resume` (G05) clears it.

**Reason.** A§7.7:686 has the user, or a break that parks, set `paused` with what is unresolved written into `STRAND.md`, and one block for both keeps the reader and `strand resume` simple.

**Follow-up.** Record-map edit: RM:85 (`STRAND.md` body block `## Paused`, owner `record.py`).

### G53 Lease transitions not covered

**Decision.** A take is allowed only when `state` is `none`, `released` or `broken`; a session that already holds the lease keeps its label and never takes again. A refresh or a release needs `state: "held"` with the presented label and epoch and is otherwise refused, a release of a released lease included; a break needs `state: "held"` (G04). A `hybrid` strand may take (its platform half builds), a `paused` strand may take (the resume path, G05), and a `closed` or `non-platform` strand may not.

**Reason.** A§9.8:941 and the refusal rules of BP:123 imply these, and stating them as one transition table leaves no call undefined.

**Follow-up.** None.

### G54 Computed values in `status --json`

**Decision.** `open_versions` lists the strand's versions whose `version.md` `state` is not `released` and whose `close_reason` is `none`, sorted by number; `live_objects` counts the `account.json` `live_objects` entries whose `owner_strand` is the strand and whose `state` is `active` or `inactive`; `last_activity` is the date of the newest log entry at the strand's position across the record log and the strand's rolled logs, or `null`. `run` is the newest `build.json` `runs[]` entry in state `running`, as `{id, state, heartbeat_at, heartbeat_age_minutes}`, or `null`; an `interrupted` run appears only in the top-level `interrupted` list as `{strand, run_id, version}`.

**Reason.** RM:144 to 148 names these values without defining them, and these definitions read only files that already exist.

**Follow-up.** Record-map edit: RM:152 (the definitions).

### G55 `check` modes

**Decision.** `check` has one mode, a full pass over the record, and takes no moment or release flag (`--json` is accepted and changes nothing, since it always prints JSON). The A11 rules fire on the record-state signals of G14 and so stay silent at other moments without any flag, and the release-time requirements are applied by `version release` itself (G26, G27).

**Reason.** BP:23 and A§5.4:354 describe moments, which G14 turns into record state, so no source needs a mode.

**Follow-up.** None.

### G56 Ordinal source and name validation

**Decision.** The next ordinal is one more than the highest `NNN` among the `strands/NNN-*` folders (`001` on an empty record), zero-padded to three digits and refused past `999`; since no script deletes or renames a folder, the counter is monotonic and never reuses an id. `init` refuses a slug that does not match `^[a-z0-9]+(-[a-z0-9]+)*$` or is longer than 40 characters, and `strand open` refuses a topic that does not match that pattern or is longer than 24 characters, each with the rule as expected.

**Reason.** A§7.1:441 states the rules, and the scripts' no-delete rule (A§5.3:341) makes the folders a sufficient source.

**Follow-up.** Record-map edit: RM:72 (the slug sentence follows A§7.1:441: the folder name, the folder name under `archive/`, and `client-<slug>` only on the GitHub path).

### G57 Reads on a newer schema

**Decision.** The known schemas are embedded in `mmb_common`: `client/2`, `strand/1`, `log/1`, `lock/2`, `account/1`, `build/2`, `summary/1`, `version/1`, `readiness/1`, `scope/1`, `live-map/1`, `status/1`, `history/1`, `settings/1`; a known file whose schema has the same name and a higher number, or an unexpected name, counts as newer. Every writing subcommand first reads the schemas of `CLIENT.md`, `log.md`, `account.json`, `.work/lock.json` and every `STRAND.md` and `version.md` it will touch, and refuses with nothing written if any is newer. `status` and `check` still read such a record: `status` sets `schema_newer: true`, and both report one blocking finding per newer file and skip that file's field checks.

**Reason.** A§5.3:342 and RM:96 say only that writes are refused, and reading on keeps the front door able to say why.

**Follow-up.** None.

### G58 Home items beyond the six folders

**Decision.** `home init` creates `clients/`, `cards/`, `monday-knowledge/`, `sandbox/`, `archive/` and `local/`, writes `local/settings.json`, creates `local/leak-terms.txt` and `local/sandbox-accounts.txt` as zero-byte files, and places `sandbox/SANDBOX.md` from the template when it is absent. It does not create `clients-index.json`, which is written at a record close and whose absence its readers treat as empty, or anything under `cards/`.

**Reason.** BP:123 names the six folders and the two files, and `SANDBOX.md` is the one item A§5.3:345 places under `sandbox/`, where it carries the open A11-1 question in words.

**Follow-up.** Design text touch-up: BP:123 adds `sandbox/SANDBOX.md`.

### G59 The D-numbered decisions

**Decision.** The D-numbered decisions are read as pointers only: every file carries a `schema` key and there is no `schema_version` field (A§5.3:342 over 1b:31); a GitHub account is stored only on the GitHub archive path (A26 over 1b:34); no development home value appears in any project file (A22 over 1b:34); Q7 (emails) and Q14 (exclusions) are taken as A§8.3:768 and A§7.1:415 state them.

**Reason.** AMENDMENTS A22 to A28 and the 2026-10-14 ARCHITECTURE win over the 2026-10-13 stage-1b plan.

**Follow-up.** None.

### G60 What the sha is a hash of

**Decision.** There is one file hash, `mmb_common.sha256_file(path)`, the sha256 of the file's bytes as stored, used by `guard`, `freeze`, the save entries and every `check` comparison; log-entry and roll hashes are of LF-normalised entry text (G08), because entries are parsed text rather than files. Since composed files are written with LF (G11) and raw and frozen files are byte copies, a record moved between systems keeps every hash; a file an editor rewrote with other line endings counts as changed, which for `guard` means a re-read.

**Reason.** A§5.3:344 and A§7.4:601 compare hashes without saying of what, and bytes are the only reading under which "saved unchanged" (BP:123, A§7.1:378) and the recorded sha agree.

**Follow-up.** Design text touch-up: BP:296 (WP12), on the GitHub path the record carries a `.gitattributes` of `* -text` so a clone keeps the bytes the manifest hashed.

### G61 Evidence marker set

**Decision.** The marker set is A§7.5's nine: `[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]`, `[Q/doc]`, `[X]`, `[E]`, `[I]`, `[A]`. `check` blocks on any of the nine, or an internal id (G30), in a file under `strands/*/drafts/`, and warns on a quote marker (`[Q]`, `[Q?]`, `[Q/side]`, `[Q/recon]`, `[Q/doc]`, `[X]`) with no location on its line, a location being `@HH:MM:SS`, `cue N`, `cues N-M`, `L<n>`, `paragraph <n>`, `§<n>`, `p.<n>` or `region`, in `research/`, `calls/*.md`, `inputs/*.md`, `readiness.md` and `solution/blueprint.md`.

**Reason.** A§7.5:612 to 626 wins over RM:170 to 181.

**Follow-up.** Record-map edit: RM:170 to 181 (an `[A]` row; RM:181 "all nine", `readiness.md` in place of `discovery.md`).

---

## Record-map edits

In `shared/record-map.md` line order; another step applies them.

- **RM:20, RM:23** (G13): the raw rows say "sha recorded in the save entry of `log.md`".
- **RM:31 to 60, strand table** (G44): `readiness.md` (RM:37) 250 lines; new rows `solution/exclusions.md` (current, engagement seeds it, 80 lines) after RM:42 and `versions/<v>/build-notes.md`, `build-notes.html` (snapshot, solution-audit, 250 lines) after RM:50.
- **RM:53** (G26): drop `updates.md` from the release snapshots.
- **RM:64** (G44): the 4 MB exclusion adds `inputs/*.<ext>`; the `non-platform` file list follows A§7.1:429 (`readiness.md`, no `deliverables/handoff/`, no `sop/` clause).
- **RM:66** (G08, G09, G39, G46): `.work/` holds `lock.json`, `history.json` (the log baseline), `record.mutex`, `intake/`, `backup/` (timestamped generations by record-relative path), and per strand `live-inventory.json`, `audit/`, `build.json.bak`, `condense-plan.json`, `summary-plan.md`; drop `cards-index.json`, `migration-sources/`, `claims-queue/`, `tools/<plugin-version>/` and the per-strand `backup/`, `sop-inputs/`, `doc-chunks/`, `render/`.
- **RM:68** (G34, G46, G58): the home list becomes A§5.3:345's (`clients/`, `cards/`, `clients-index.json`, `monday-knowledge/`, `sandbox/` with `SANDBOX.md`, `archive/`, `local/`), dropping `leases.json` and `claims/`; add the `settings.json` fields of G34; the Cowork fallback sentence goes.
- **RM:72** (G56): the slug is the folder name and the name under `archive/`, and `client-<slug>` only on the GitHub archive path.
- **RM:74** (G12): `-2`, `-3`, … assigned by `record.py add-transcript` and `add-document`.
- **RM:77** (G01): "Session label", minted as `YYYYMMDD-HHMM-xxxx`, for example `20261015-1330-k7q2`.
- **RM:85** (G06, G52): the strand index is written by `record.py`; `STRAND.md` gains the body block `## Paused`, owner `record.py`.
- **RM:87 to 92** (G18): header `| strand | title | kind | state | version | version state | clearance | live objects | last activity |`, a separator line, and a matching example row.
- **RM:96** (G11, G38, G40): escapes `\"` and `\\`, trailing comments and comment lines kept, new keys appended before the closing `---`, unknown keys kept; text written UTF-8 without BOM with LF; JSON written as `json.dumps(indent=2, ensure_ascii=False)` plus LF; UTC `YYYY-MM-DDTHH:MM:SSZ` in JSON, local time with no zone in front matter, log headers and dates.
- **RM:100** (G14, G15): `client/2` as A§7.2's list (`account_kind` `own|client|sandbox`, `build_target`, `client_workspaces`, `last_input`, `sample_data_in_account` with `not-needed`; no `last_call`, no `page_size`); the A11 sentence names the three signals of G14.
- **RM:104** (G16): `strand/1` as A§7.7's list and ladders.
- **RM:108** (G42): the nine `SUMMARY.md` headings, the dates "opened, shown, signed off, released and closed".
- **RM:112** (G07, G17, G20, G29, G30): `version/1` fields of G17 including `purpose`, `shown`, `signed_off`, `close_reason`, the `## Events` block of G20, no `demo_script_ready` or `sop_sections_confirmed`; `blueprint/1` carries `sample_rows`; the "Internal: never client-facing" line sits directly after the front matter.
- **RM:116** (G01, G15, G47): `account` gains `bound_at` and `build_target`, `kind` `own|client|sandbox`; `client_workspaces` block; `guard_index` gains `client_workspace_ids`; `lease {strand, epoch, session_label, heartbeat_at}`.
- **RM:120** (G01, G04): `runs[]` uses `session_label` and gains `reconcile {at, mode, classes}`; `approved_in_chat` becomes `approved_in_session`.
- **RM:135** (G01, G02, G03): `lock/2` field list of G02 without `surface`, `session_label` for `chat_label`, history `by` and `note` as G02, the increment rule stated with the break-then-take arithmetic.
- **RM:142 to 152** (G01, G02, G19, G54): `schema_newer` for `migration_needed`; strand entries add `purpose`, `shown`, `signed_off`; lease block `session_label`, no `surface`; the computed-value definitions of G54.
- **RM:156** (G17, G26, G27): no `demoed`; the required-file table with its pinned headings; `released` without `updates.md`; missing files warn except at `released` and block the release.
- **RM:163** (G01): "key or session label".
- **RM:166** (G08, G13, G45): A§7.6:645's 44 types (embedded in `record.py` between pinned markers); the save entry's body lines; the roll as G08 states it (the strand's or the released version's entries, the pointer with `rolled_to` and `sha256`).
- **RM:170 to 181** (G61): add the `[A]` row; "all nine"; `readiness.md` in place of `discovery.md`.
- **RM:191, RM:206, RM:212** (G21, G28): `readiness.md` carries `clearance` (human string or `none`) in its front matter; assumptions as `- <statement> [kind: <kind>; state: <state>]` under `## Assumptions`.
- **RM:272 to 278** (G46): delete "Scripts the record copies".
- **RM:280 to 282** (G46): delete "Migration".

## Design touch-ups

ARCHITECTURE, in line order:

- **A§5.2:336** (G36): the scripts find the plugin from their own path; only the interpreter command waits for the Windows re-run.
- **A§5.3:340** (G11): composed text written UTF-8, LF, no BOM; raw files and frozen copies are byte copies.
- **A§5.3:343** (G10): a refusal exits 1, a usage error 3, `status` 0 when it printed.
- **A§5.3:345** (G35, G37): `MMB_HOME` recorded through the Claude Code settings `env` entry with the user's yes; the `CLAUDE.md` search runs from the home folder to the root of the drive.
- **A§5.4:353** (G51): `lease_fence` among the primitives.
- **A§5.4:354** (G05, G08, G22, G25, G27, G30, G32): `strand resume` in the catalogue; "the log only grew"; `--go-on`; `version open`, the condense pair, `strand list` and `card` described; required-file and other severities; the session, not the script, checks the connector.
- **A§7.1:437** (G08, G09, G39, G46): `.work/` gains `record.mutex`, defines `history.json`, drops the per-strand `backup/`, lists the plan files.
- **A§7.2:468, A§7.3:524, A§7.3:559, A§9.8:939** (G01): example labels become a minted label.
- **A§7.2:481** (G06): the strand index is written by `record.py`.
- **A§7.3:493** (G15): `account` gains `bound_at`.
- **A§7.4:587** (G23): after the user's answer.
- **A§7.4:598** (G27): the severity of a missing required file.
- **A§7.4:610, A§7.6:645** (G08): the roll moves the strand's entries, at a release those of the released version.
- **A§7.7:682** (G43): `output_class` defaults.
- **A§7.7:684** (G42): the two-step summary.
- **A§7.7:686, A§8.11:836** (G05): `strand resume` ends a park.
- **A§8.2:745** (G32): the session checks the connector.
- **A§8.3:758, A§8.3:759, A§8.3:768** (G13, G14): the save entry and its lines; `add-*` refuses a non-fixture input while A11-3 is unanswered; `--came-with`.
- **A§8.4:772** (G06): the index update goes through `record.py guard`.
- **A§8.5:785** (G41): `freeze` reads `revision` and writes `version.md` `sha256`.
- **A§8.8:815, A§8.8:817** (G20, G22, G23): the full `version mark` flags, `--go-on`, and the G23 answer.
- **A§8.10:828, A§8.10:830** (G07, G25): which close steps are `record.py strand close`; `close_reason` in `version.md`; `record.py card` copies the card.
- **A§9.8:933** (G01, G50): label format; `run_id` set by the first refresh after `run start`.
- **A§9.8:943** (G48): `check` warns on a stale lease.
- **A§9.8:945** (G03, G04): the new holder holds the broken epoch + 2; the break's flags.
- **A§9.10:955** (G09): `guard.py` reads the lock under the record mutex or treats a torn read as a refusal.

BUILD-PLAN, in line order:

- **BP:23** (G14): the three A11 signals.
- **BP:123** (G04, G05, G33, G35, G58, G23): the break flags; `strand resume`; "unless `--update` names the answer"; the `env` entry; `sandbox/SANDBOX.md`; the G23 answer.
- **BP:134, BP:138** (WP3; G04, G09, G11, G15, G50, G51): `reconcile` written onto the interrupted run; the record mutex around every `account.json`, `build.json` and lock access; the JSON form; `bind` writes `bound_at`; `run start` refreshes with `run_id`; writes go through `lease_fence`.
- **BP:134, BP:157, BP:167, BP:296, BP:305** (G49): `sys.dont_write_bytecode = True` first in `ledger.py`, `leak_lint.py`, the two transcript scripts, `archive_check.py` and `guard.py`.
- **BP:198** (WP7; G21, G27, G28, G29, G31): `readiness.md` front matter `clearance: "none"` and the assumption line form; `version.md` and `audit.md` headings; `blueprint.md` `sample_rows: "none"`; every template carries the keys `record.py` sets.
- **BP:207** (WP8; G32, G35): `first-run.md` explains the two doors, checks the connector, and offers the `env` entry.
- **BP:244** (WP9; G29): `solution-blueprint` sets `sample_rows`.
- **BP:248** (WP9; G04, G05): `recovery.md` passes the break flags and calls `strand resume` after `run end`.
- **BP:296** (WP12; G60): `.gitattributes` of `* -text` on the GitHub path.
- **BP:305** (WP13; G09, G30): `guard.py` reads under the mutex; `test_guard.py` owns "a stale native index downgrades guarded writes to an ask".
- **BP:487** (H20; G30): the downgrade clause moves to WP13.
- **BP:502** (H35; G03): "002 holds the broken epoch + 2".
- **BP:524** (H57; G32, G33): the two doors and the connector check are WP8's half; the second run keeps the settings unless `--update` names an answer.
- **BP:533** (H66; G23): after the user's answer.

`shared/safety.md` (WP1), section 8 (G01, G02, G03): "session label" for "chat label", no `surface`, and the epoch sentence as A§9.8:945 is touched up.


## Added by the main session, 2026-10-14

- **After G02: no lock template.** `init` writes the first `.work/lock.json` through `mmb_common`'s lease primitives (state `released`, epoch 0, empty history), so the lease primitives stay the one writer of the lock (C82). WP7's template list gains no `lock.json`; the stand-in under `tests/unit/fixtures/plugin/templates/record/` was removed.

## Added by part 2, 2026-10-15

- **After G40: a heartbeat ahead of the clock.** `mmb_common.heartbeat_age`, the one place an age is computed, reads a heartbeat up to five minutes ahead of this machine's clock as 0 minutes old (clock jitter), and one further ahead as minus the whole minutes it lies ahead and never fresh: the clocks disagree, so it proves nothing about the holder. `status` and `lease status` then say `fresh: false`, `check` warns on `.work/lock.json` `heartbeat_at` ("N minutes ahead of this machine's clock: the clocks disagree"), a take's refusal names it, and break condition 1 holds; condition 4 still needs the reconcile stamped after the heartbeat, so with a run on the lock a break waits. Reason: the old reading turned a future stamp (the fixture read before its dates, or two machines with skewed clocks) into a lease that looked fresh and could never be broken, while the epoch fence already refuses a woken holder. At the fixture's pinned clock nothing changes; at the real clock an untouched fixture copy now checks with this one warning.

## Added by the lease fixes, 2026-10-15

These settle the findings of `lease-review.md` (R1 to R16 below are its findings 1 to 16); its "Fixes" section maps each finding to the code and the test. Nothing here fills an A11 field or names a person, firm, account or workspace.

- **After G02 and G53: whose take comes next after a break (R1).** A `broken` and a `parked` history entry gain a twelfth key, `for_strand`, the `--for-strand` the break ran for (the strand `note` already names). While the lock is `broken`, its newest entry keeps the lease for one strand and `lease take` refuses every other, naming it: after a `broken` entry with `choice: resume`, the entry's `strand` (the holder's, whose fresh session runs the ordinary recovery, C111); after a `parked` entry, its `for_strand` (the taker, C112); after a `repaired` entry (below), its `for_strand`. A reservation for a strand whose `STRAND.md` reads `closed` lapses, so a taker that closes never leaves the parked holder without a way back. G19's lease block gains a last key, `reserved_for` (the strand, or `null`), in `lease status` and `status --json`, and the break's output carries it too. Reason: A§9.8:945 hands the lease to a named strand on each choice, and without the reservation a resume over duplicate and partial elements let the taker build first. Follow-up: record-map edit applied (lock and status sections); design text touch-up A§9.8:945 and BP:502 (H35): "the break keeps the lease for the strand the choice names; every other take is refused until that one"; WP9's briefing line reads `reserved_for`.

- **G51 amended: the fence needs a run and moves the heartbeat (R2, R3, R9).** `lease_fence(root, epoch, session_label, run_id)` passes only when the lock is `held` and sound, the epoch matches, the presented label is non-empty and matches, and the lock carries a `run_id` equal to the presented one: while the lock's `run_id` is `null` nothing passes, because account-affecting writes happen only inside a run. When it passes it moves the heartbeat (lock and `account.json` mirror, no backup) in the same mutex hold, so a write never starts behind a heartbeat a break could read as stale; a malformed lock or a newer schema returns `(False, reason)`. `lease_refresh` refuses a `run_id` that any history entry already carries ("a run enters only the lease it starts under"). The break's compare-and-set also refuses an empty presented label. Reason: G04's condition 4 waives the reconcile when the lock has no run, which is only sound if nothing can be written before `run start`; and A§9.8:943's "refreshed on every ledger write" has to hold before the write, not after it. Follow-up: design text touch-up BP:134 (WP3): `ledger.py run start` refreshes with its run id before any fenced write; every account-affecting write calls `lease_fence` first and needs no separate refresh for it; a fence that cannot run (exit 3, a mutex timeout included) is a stop, never a skip; BP:248 (`recovery.md`, WP9) opens a new run on the resume path, never re-enters the broken lease's run id.

- **G09 amended: the lock is written last, and a failure after a commit says what was committed (R4).** A primitive writes the `account.json` mirror, then the `CLIENT.md` mirror, then the lock, so a write that fails (a sharing violation on Windows, for one) leaves the lease as it was and the same call can be retried; the failure is exit 3 naming the file and saying the lease is unchanged (or, for the lock itself, that it may be torn and naming the repair). When a step after the primitive fails (the log insert, a park's `STRAND.md`, the index), `record.py` exits 3 with `"error"` field `committed` and a top-level `"committed"` object: for a take the epoch, the label and the entry still to write, with the expected text telling the session to hold that epoch and label as a take's output; for a release the epoch and the entry; for a break the break's result, the three entries and on park the `## Paused` line; for a repair its result and entry. `MMBError` gains an optional `committed` keyword. G09's "heals at the next take, refresh, release or break" becomes "heals at the next successful lease call, or `record.py lease sync`". Reason: a committed change reported as a bare failure orphaned a take under a label never printed and broke a lease with no log entries. Follow-up: design text touch-up A§5.3:343 and A§7.1:437 (exit 3 may carry `committed`); WP3's `ledger.py` reports its own post-commit failures the same way.

- **New subcommand `record.py lease sync` (R5).** No flags; under the mutex it rewrites both mirrors from the lock with the lock unchanged (`mmb_common.lease_sync`), writes no log entry and returns `{epoch, state, rewritten}`. `check`'s expected text for either mirror ends "record.py lease sync rewrites it from the lock". Reason: a mirror left behind by a failed write blocked `check`, and so the release and the record close, with no writer allowed to fix it. Follow-up: C25's catalogue gains `lease sync`; A§5.4:354 lists it.

- **G39 amended and a new subcommand `record.py lease repair --user-yes "<the user's words>"` (R6).** A take, a release, a break and a repair back the lock up before rewriting it (`.work/backup/.work/lock.json.<stamp>`); a refresh and the fence do not. The user clears `.work/backup/` by hand, never the whole `.work/`, which holds the lock and the mutex. `lease repair` (`mmb_common.lease_repair`) runs only when the lock is missing, not JSON or malformed (refused when it reads and is sound, and refused for a newer lock schema), needs the user's words on one line, and rebuilds the lock in place, the torn file backed up first, never deleted: the epoch is one above the largest epoch the newest sound lock backup (its own and its history's) and the `account.json` mirror know, so any session holding the lost lease is fenced out; the history is that backup's plus a `repaired` entry (`epoch` the largest known, `strand` and `session_label` the mirror's holder, `for_strand` the strand the lock is kept for, `note` the sources and the user's words); the state is `broken`, kept for the mirror's holder (or the strand the backup kept it for), as a resume break would keep it, else `released`. It writes one record-level `lease` entry keyed `repaired`, and its output's `next` names the take that comes next. Every exit 3 on an unreadable lock names the repair. Reason: a torn or missing lock left every lease command, `status` and `check` at exit 3 with no way back but a hand-written lock and a guessed epoch. Limit: a backup holds the lock as it was before its last state change, so a break whose own lock write tore loses that break's reservation, and the user's yes is what guards it. Deleting `.work/record.mutex` while a session holds it is not guarded in code (a new file takes a new lock); the record-map and `safety.md` say the user never clears `.work/` itself. Follow-up: record-map edit applied (RM:68 backup sentence, the lock section); design text touch-up A§7.1:437 and A§9.8 (the event `repaired`; the repair); C25's catalogue gains `lease repair`.

- **G50 and G53 amended: a take reads allowlists (R7, R13).** A take needs the lock in `none`, `released` or `broken` (and, after a break or a repair, the reservation above); the strand's `kind` `platform` or `hybrid`; its `state` `active`, or `paused` only when its `build.json` has a run in `interrupted` (the park path of G05; a strand the user paused does not take); and its `version` of the form `vX.Y` with `versions/<v>/version.md` present. Reason: the denylists let a missing or misspelt kind, a `Closed` state, an empty or unopened version and a `Held` lock state through, and G53's reason for `paused` covers only a parked strand. Follow-up: none beyond the record-map lock section.

- **The lock's shape is checked (R9).** `mmb_common.lock_findings(lock)` returns blocking findings for a lock that is not G02's shape: `schema` `lock/2`; `history` a list of objects, each with an `event` of `taken | released | broken | parked | repaired` and an integer `epoch`; `epoch` an integer at or above every history epoch; `state` one of the four; while `held`, `strand` three digits, `version` `vX.Y`, `session_label` of the G01 form, `taken_at` and `heartbeat_at` UTC stamps, `run_id` null or a string; otherwise those seven fields null. Every primitive refuses a malformed lock with these findings (exit 1, each naming the repair), `check` blocks on them, and `lease status` (so `status`) reports a heartbeat that does not parse as `heartbeat_age_minutes` and `fresh` null instead of exiting 3. A newer `lock/<n>` stays a schema refusal (G57). Reason: a null label passed the fence and a null heartbeat crashed `check`, `status` and every take. Follow-up: none.

- **The record mutex names a locking error (R8).** Only `EWOULDBLOCK`/`EAGAIN` from `flock` and `EACCES`/`EDEADLOCK` from `msvcrt.locking` count as another holder; any other `OSError` on the take is exit 3 at once, file `.work/record.mutex`, naming the error and asking for a local file system with locks. Reason: an unsupported lock on a network or synced mount read as 30 seconds of contention and sent the user looking for a second session. Follow-up: the Windows run (review list, item 1) confirms the `msvcrt` errno.

- **`init` checks the folder again under the mutex (R15).** The emptiness check repeats inside the record mutex, a `.work/` holding only `record.mutex` counting as empty, so a second `init` of the same slug is refused before it writes anything. Follow-up: none.

- **`check`'s clock wording (R10, partly).** The expected text for a heartbeat ahead of the clock reads "set the clock of each machine that writes this record to the right time; until then the lease reads as not fresh and may be broken". The two-clock rule itself stays as the part-2 decision chose (see the review's Fixes, finding 10).

- **`shared/safety.md` section 8 (R11, R16).** Rewritten to the lease as built: `session_label` and `--label`, no `surface`, no `--chat-label`, no `leases.json` (the one question of D10 instead), the take's allowlists, the fence's run and heartbeat, the three break entries and the broken epoch + 2, the reservation and `reserved_for`, the write order, `lease sync` and `lease repair`, `.work/backup/` as the only part the user clears, and a new paragraph "One environment per record" (one OS environment writes a record at a time; the record home stays out of a cloud-synced folder; the machine's clock stays right). It now says what the build does for a session that lost its label (it waits for the stale heartbeat and a break); whether to keep that is still open with the user (review finding 12), and A§9.8:933's sentence is left as it is until then. Follow-up: WP1's other sections of `safety.md` still say "chat" where A§9.8 says "session" (sections 1 to 5, 7, 9, 10, 12 and 13); WP8's first-run walkthrough repeats the one-environment rule.

- **Open with the user (R12).** A session that lost its epoch and label after compaction has no legal path but the 60-minute wait and a break, while the label sits in both mirrors and `lease status`. Either accept the wait and correct A§9.8:933 ("runs resume, which takes the lease afresh"), or allow a same-strand takeover (a break of a fresh lease by the holder's own strand, with the user's yes naming it). Recommended default, built: the wait, since R2's fence now refuses any write before `run start` and any old run id, which narrows what a session that read the label back from disk can do.

## Added by the checklist fixes, 2026-10-15

These settle the four not-met clauses of `CHECKLIST.md` other than the size limit (C26): C13, C21, C127 and C129. Nothing here fills an A11 field or names a person, firm, account or workspace.

- **C129: the `#KEY` half of the ledger form is WP3's.** `record.py check` resolves the revision half of `v0.1r4#B1` (the version folder holds `blueprint-r4.md`) and does not look the key up. No source says where a blueprint lists its element keys: ARCHITECTURE 7.3 and `record-map.md` call the keys "the blueprint's stable ids" and list their kinds; 3.4 spreads element ids over several of the sixteen numbered sections (the requirement trace, the board inventory, the columns, groups and views, the lists) and leaves the section list to `blueprint-guide.md`, a WP9 file that does not exist yet; `record-map.md` pins no element table for `blueprint/1` (its one pinned field is `sample_rows`, G29); and the `## Elements` table in the stage-2 fixture's blueprint is the fixture author's own layout, which a script must not turn into the contract. `build.json` objects carry their own bare key and a `blueprint_ref` to the frozen revision, so looking the key up in the ledger would only confirm a row against itself. The key half belongs to `ledger.py` (WP3), which owns element keys and writes every `blueprint_ref` and `prompt_ref`. Reason: a guessed table layout would reject every real blueprint that lists its keys differently. Follow-up: once WP3 and WP9 pin where `blueprint-guide.md` lists keys, add the key lookup to `check` (or to `ledger.py`'s own verification) with the probe the checklist names: `v0.1r1#B9` blocks and `v0.1r1#B1` passes on the fixture. Until then `v0.1r1#B9` passes `check`, and the checklist row says so.

- **After G10 and C21: an error about a whole file names that file as the field.** The exit-3 errors for a file that cannot be read, a file that is not JSON, a template that is not JSON and a settings file that is not an object carry the field `(whole file)` (`mmb_common.WHOLE_FILE`), because no key or part of the file is the one that failed; the mutex timeout carries the field `record.mutex`, the mutex file's own name. The catch-all for an unexpected exception keeps the exception's class as the field and, when the exception has no message, says "an internal error with no message", so the four parts of C21 are non-empty on every error object. Reason: five construction sites printed an empty field, which A§5.3:343 does not allow. Follow-up: none; the unit tests assert all four parts non-empty on every refusal, finding and error object they produce.

- **C13 and C127 changed no behaviour.** C13 is now asserted for all 23 writing subcommands in one test that also checks the 23 names against the catalogue. C127 is asserted for each version state row: a missing item warns in its own state; the planned, approved and built rows block once the version is `released`; the building and fixing rows are checked only while current, as G27 says, so at release the removed audit of a `fixing` version is blocked by the `audited` row. A removed frozen file or `build.json` also blocks as a dangling reference (C129), which the test accepts as the only other blocking finding.

## Settled with the user, 2026-10-15

- **G23: the default stands.** Every `v0.x` during the sales process is a functional proof of concept; a sign-off of a `v0.x` leaves it one; when the user reports the sale closed, the plugin proposes `v1.0`, the working solution (AMENDMENTS A25, answered 2026-10-15). The code needs no change.
- **C26, size:** the built size is accepted; BUILD-PLAN's WP2 size line now carries the built figures.
- **G23, refined by the user the same day:** the move from proof of concept to working solution is smooth. `v1.0` continues the same strand and workspaces from the last `v0.x` as one more iteration (A21's continue rule), never a fresh build; the open assumptions are listed to confirm. Design touch-up owed: A§7.4 and A§8.8 say so; the front door (WP8) proposes `v1.0` when the user reports the sale closed.
- **Lease review finding 12: option (a), the user's choice of 2026-10-15.** A session that lost its epoch and label waits until the lease is stale (60 minutes after the last refresh), then the lease is broken with the user's yes and taken afresh; no same-strand takeover. As built; A§9.8's carry-rule sentence now says so.
