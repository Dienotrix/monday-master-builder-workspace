# `mmb_common.py` API, for the `record.py` writers

Date: 2026-10-14. Internal build file: never client-facing.

`plugins/monday-master-builder/scripts/mmb_common.py`, tested by `tests/unit/test_mmb_common.py`. Import it after `import sys` and `sys.dont_write_bytecode = True` (G49); the module sets the flag too, but only the caller can stop its own import writing a cache. Every `root` below is the record folder as a `Path`; every `rel` or `name` is record-relative POSIX spelling.

## Errors and exit codes

| Exception | `code` | Map to | Raised for |
|---|---|---|---|
| `Refusal` | 1 | exit 1, `"ok": false`, `"refusals": e.findings` | stale sha, lease refusals, newer or foreign schema, invalid value, absolute or escaping path, unknown strand |
| `FrontMatterError` (a `Refusal`) | 1 | exit 1 for a write; a blocking finding in `check` | unquoted value, duplicate key, `schema` not first, no `---` |
| `CannotRun` | 3 | exit 3, `"error": e.findings[0]` | file missing or unreadable, malformed JSON (lock, `account.json`, `plugin.json`), mutex timeout |

All three derive from `MMBError`. `e.findings` is a list of `{"file", "field", "problem", "expected"}` dicts (C21); a lease break or take can carry several. Catch `MMBError` once at the top of `main` and use `e.code`. Every part is non-empty (C21): an unreadable or non-JSON file has the field `(whole file)` (`WHOLE_FILE`), and a mutex timeout has the field `record.mutex`.

## Functions

**Home, plugin, paths**
- `home() -> Path`: `MMB_HOME` when set and non-empty, else `Path.home() / "monday-builder"`. `HOME_FOLDERS` lists the six folders `home init` creates.
- `read_settings() -> dict | None`: `local/settings.json` under the home; None when absent; `CannotRun` when not JSON.
- `plugin_version(plugin_root=None) -> str`: from `<plugin root>/.claude-plugin/plugin.json`; `PLUGIN_ROOT` is `Path(__file__).resolve().parent.parent`. `CannotRun` when missing or without `version`.
- `record_path(root, reference, base="") -> path`: a `/`-written reference (relative to the record folder `base`, `"."` or `""` for the record root) resolved under `root` of any flavour, `..` folded without touching the disk. `Refusal` (field `path`) for an absolute path in either spelling or one that leaves the record.
- `relative(root, path) -> str`: record-relative POSIX spelling, for messages.
- `strand_dir(root, short_id) -> Path`: `strands/<NNN-topic>/`; `Refusal` (field `strand`) when none matches.

**Reading, hashing, writing**
- `read_text(path, name=None) -> str`: UTF-8 with or without BOM, CRLF or LF read as LF; `CannotRun` when unreadable.
- `read_json(path, name=None) -> object`; `CannotRun` when unreadable or not JSON. `json_text(data) -> str`: the one JSON form (indent 2, `ensure_ascii=False`, final LF).
- `sha256_file(path) -> str`: hash of the bytes as stored (G60). `sha256_text(text) -> str`: the G08 entry hash (LF, trailing blank lines dropped, each line LF-ended); it matches the fixture's `history.json`.
- `backup_file(path, root, backup_dir=None) -> Path`: copies the old bytes to `<backup_dir or root/.work/backup>/<path from root>.<UTC stamp>`, `-2`, `-3` on a clash. For `settings.json` pass `root=home()/"local"`, `backup_dir=home()/"local"/"backup"`; for a card, `root=home()`, `backup_dir=<record>/.work/backup/home`.
- `write_file(path, data, root, backup=True, backup_dir=None) -> None`: `str` is written UTF-8 with LF (CRLF folded); `bytes` byte for byte (raw inputs, frozen copies). An existing file is backed up, then truncated and rewritten in place; a new file is created with `"xb"`. No rename, no delete.
- `guarded_write(path, data, root, expect_sha) -> None`: under the mutex, `Refusal` (field `sha256`) unless the file still hashes to `expect_sha`; `expect_sha=None` means the file must not exist. Then `write_file` with backup. Use it for record files only (it locks `root`).

**Front matter (G38)**
- `front_matter(text, name="") -> dict` and `split_front_matter(text, name="") -> (dict, body)`; `FrontMatterError` with the key as `field`.
- `set_front_matter(text, updates, name="") -> str`: sets only the quoted values, keeps comments, spacing and every other line, appends new keys before the closing `---`, stamps `updated` with the local minute when a value changes and the file has `updated`. Returns LF text, so an LF file whose values are unchanged comes back byte-identical (C11). `Refusal` for a multi-line value or a non-lowercase key.
- `schema_newer(found, expected_name) -> bool` and `require_schema(found, expected_name, name)` (`Refusal`, field `schema`, expected e.g. `client/2`). `SCHEMAS` holds G57's list.

**Time (G40)**
- `now_utc()`: the one clock; tests patch `mmb_common.now_utc`.
- `stamp(kind) -> str`: `utc` (`2026-11-05T14:30:00Z`), `backup`, and local `minute` (`updated`), `log` (log header), `date`, `label`.
- `parse_utc(text) -> datetime`; `heartbeat_age(text) -> (minutes, stale)`, stale meaning more than 3,600 seconds; a stamp more than `CLOCK_SKEW` (300 seconds) ahead of the clock gives minus the minutes it lies ahead and `stale` true, and one within the skew reads as 0 minutes (record.py part 2). `heartbeat_words(age, stale)` is the phrase every message uses for it.

**Mutex (G09)**
- `record_mutex(root, timeout=None)`: context manager on `.work/record.mutex` (created on first use, never deleted), re-entrant within one thread, so `record.py` can hold it around a primitive and its log insert. `CannotRun` after 30 s. It creates `.work/` on first use, so a tree hash in `status` and `check` tests should leave out `record.mutex`.

**Lease primitives** (the only writers of `.work/lock.json`, `CLIENT.md` `lease` and `account.json` `guard_index.lease`). Each takes the mutex, checks the schemas of the lock, `account.json` and `CLIENT.md` before writing anything (`Refusal`, C13), writes the lock, then the `account.json` mirror, then the `CLIENT.md` mirror, and writes a mirror only when its value changes.
- `lease_init(root) -> None`: the first lock for `init`, state `released`, epoch 0, empty history, per the main-session addition after G02 (G02's own template said `none`). `Refusal` (field `state`) when a lock exists.
- `lease_take(root, strand) -> {epoch, session_label, strand, version, taken_at}`: title and version read from the strand's `STRAND.md`. One `Refusal` lists every reason: `kind` non-platform, `state` closed, `version` none, and `state` on the lock when held, whose text names holder, title, version, label, heartbeat age, fresh or stale, what may go on, and the three ways forward (C92 to C94). A paused or hybrid strand may take.
- `lease_refresh(root, epoch, session_label, run_id=None) -> {epoch, session_label, run_id, heartbeat_at}`: no history entry, no backup. `run_id` is accepted while the lock has none or the same one (G50); otherwise `Refusal` (field `run_id`).
- `lease_release(root, epoch, session_label) -> {epoch, state}`.
- Refresh and release need state `held` with the same label and epoch; anything else is `Refusal` (field `session_label`), a released lease included.
- `lease_break(root, epoch, session_label, for_strand, user_yes, account_id, choice, park_yes=None) -> {broken_epoch, epoch, choice, reconcile, for_strand, holder}`: compare-and-set first (field `epoch`, "the lease changed since it was read"), then one `Refusal` listing every failing condition by field: `heartbeat_at`, `user_yes`, `account.id` (file `account.json`), `runs[].reconcile` (file the holder's `build.json`), `choice`, and on park `park_yes`, `reconcile`, `for_strand`. On success the lock goes to `broken` at epoch + 1 with a `broken` entry, plus `parked` on park; no take happens. `holder` carries the broken lease's seven lock fields. `record.py` still writes the three `lease` log entries (G03), the park's `STRAND.md` state and `## Paused` block (G52), and the index; hold `record_mutex` around the whole call.
- `lease_status(root) -> dict`: G19's block, in that key order; age and `fresh` are None unless held.
- `lease_fence(root, epoch, session_label, run_id=None) -> (ok, reason)`: G51, every failing part named in `reason`.
- `read_lock(root) -> dict`: plain read, `CannotRun` when missing or malformed.

History entries carry the `epoch` of the lease they describe: a `broken` or `parked` entry shows the holder's epoch, while the lock shows that epoch plus one.

## Notes for the tests

- Run the suite as `python -m unittest discover -s tests/unit`; `tests/unit` is not a package, so `-t .` cannot import it, and the existing lint tests import the same way.
- Subprocess tests should pass `PYTHONDONTWRITEBYTECODE=1` (G49). The macOS system Python 3.9 otherwise writes its own standard-library cache under `HOME/Library/Caches` at startup, before any plugin code runs, which trips the C17 canary.
- Pin the clock with `mock.patch.object(mmb_common, "now_utc", ...)`. Local stamps follow the machine's zone, so compare them with `CLOCK.astimezone().strftime(...)`, not literals.
- The Windows branch of the mutex (`msvcrt`) and the in-place overwrite semantics are only exercised on a real Windows run (C04, C15, C52).

## Changed by the lease fixes, 2026-10-15

See `lease-review.md` "Fixes" and the last section of `DECISIONS.md`.

- `MMBError(*findings, committed=None)`: `committed` carries what a lease change committed before a later write failed; `record.py` prints it as a top-level `"committed"` object beside `"error"`.
- The primitives write both mirrors first and the lock last; a failed write is `CannotRun` naming the file, the lease unchanged. A take, a release, a break and a repair back the lock up to `.work/backup/.work/lock.json.<stamp>`; a refresh and the fence do not.
- `lock_findings(lock) -> [(file, field, problem, expected)]`: G02's shape (schema `lock/2`, history, epoch, state, the held fields). Every primitive refuses (`Refusal`) a malformed lock with these findings; `check` blocks on them. `read_lock` names `record.py lease repair` when the lock is missing or not JSON.
- `lease_take`: allowlists (lock `none | released | broken`; kind `platform | hybrid`; state `active`, or `paused` with an `interrupted` run; version `vX.Y` with its `version.md`), and while the lock is `broken` only the reserved strand may take.
- `lease_refresh`: also refuses a `run_id` an earlier history entry carries.
- `lease_break`: refuses an empty label; the `broken` and `parked` entries carry `for_strand`; the result adds `reserved_for`.
- `lease_status`: adds `reserved_for` last; age and `fresh` are null for a heartbeat that does not parse.
- `lease_fence(root, epoch, session_label, run_id)`: needs a non-empty label and a run on the lease equal to `run_id` (nothing passes while the lock's `run_id` is null); when it passes it moves the heartbeat in the same hold, so `ledger.py` calls it before every account-affecting write and needs no separate refresh for that write. A malformed lock or newer schema returns `(False, reason)`.
- `lease_sync(root) -> {epoch, state, rewritten}`: both mirrors from the lock, the lock unchanged.
- `lease_repair(root, user_yes) -> {epoch, state, reserved_for, from_backup, mirror}`: rebuilds a missing, torn or malformed lock in place, as DECISIONS states.
- `record_mutex`: a locking error other than contention is `CannotRun` at once (field `lock`).
