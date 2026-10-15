# Answers 2 log (2026-10-14): simpler local archive, development-only deletes

No edit added or removed a line, so the line numbers below are the same before and after. `stage-1b/build-readiness-spec.md` mentions neither topic and was not edited. Revision-note line of each document gets the clause "archive simplified and development-only deletes allowed per the user's answers of 2026-10-14".

## ROADMAP.md
- L3: revision note extended with the clause.
- L45: record close is now a checksum manifest, a move into `archive/<slug>/` on the user's yes and a check against the manifest, no second copy; GitHub option keeps the local move.

## SPEC.md
- L3: revision note extended with the clause.
- L12: the home's `archive/` now keeps each closed client folder, moved there and verified against its manifest.
- L31: close-out bullet rewritten to manifest, move, verify; GitHub option keeps the local move.
- L46: item 12 rewritten the same way, in that item's wording.
- L64: out-of-scope `delete_*` line says the plugin deletes nothing and that development tooling under `tests/` and `tools/` is not the plugin, may delete its own test objects only in the user-named test workspace (A11-1, open) and only during development.
- L86: record hygiene now describes a move verified against a checksum manifest instead of a verified copy.
- L104: record-test row now expects the folder moved into `archive/`, passing the manifest check, nothing sent to any repository.

## BUILD-PLAN.md
- L3: revision note extended with the clause.
- L105: `record-map.md` home-tree entry describes `archive/<slug>/` as the moved, verified client folder, with no holding name beside it.
- L295: WP12 acceptance, local path rewritten (manifest, confirmed move, check, failed check leaves the record recoverable, nothing deleted); GitHub path keeps the local move; unit test covers manifest, move and a planted failed check.
- L328: WP15 acceptance restores `vibe_delete` and `delete_webhook` as the scenarios' cleanup, saying it is development tooling under `tests/` that never ships, inside the A11-1 workspace and only during development; the plugin statement stands.
- L367: `archive_check.py` file-table row rewritten to manifest, confirmed move, check, recoverable failure.
- L502: H36 pass condition now tests the manifest, the confirmed move into `archive/<slug>/`, a clean check, and a planted changed, missing or extra file failing it with the record recoverable.
- L570: T27 cleanup restored to `vibe_delete` by the scenario, development-only; the plugin sends no delete.
- L573: T30 cleanup restored to `delete_webhook` by the scenario, development-only; the handoff still names it as the client's switch-off step, never sent by the plugin.
- L593: release check 12's archive test now names the manifest, the move and the check.
- L607: section 6 row 5 says the user deletes from `archive/` by hand (was "empties").
- L609: section 6 row 7 describes the local path as manifest, move and check, no second copy.

## ARCHITECTURE.md
- L3: revision note extended with the clause.
- L129 to L130: tree comment for `archive.md` rewritten (manifest, move, verify, deleted from by hand).
- L147: `archive_check.py` tree comment now names the manifest and the check of the moved folder.
- L290: `client-closeout` section describes the manifest, the move on the user's yes and the check, no second copy.
- L340: "Scripts never delete or rename over a file" reworded so the record close is a move into `archive/`, verified against the manifest, refused if the target exists, and scripts delete nothing.
- L344: home tree entry for `archive/` rewritten, no holding name beside it.
- L358: `archive_check.py` row: `compare` checks the moved folder and a failure leaves it recoverable; size figure unchanged (230).
- L377: "Archived" column note says the local `archive/<slug>/` folder, not a copy.
- L438: section 7.1 home-path list entry for `archive/` rewritten.
- L644: `archive` log type now means the manifest, the move and its check.
- L829: 8.10 record close archive part rewritten: manifest, card copy and index refresh, move (a rename within the home), verify, failed check leaves the folder in place; GitHub option runs the local move as well.
- L861: authority-table row for the archive rewritten (manifest, yes, move, verify, deleted by hand).
- L898: exclusion paragraph gains one sentence that the exclusion binds the plugin and that development tooling may delete its own test objects in the A11-1 workspace during development.
- L1108: default 12.3-20 rewritten to manifest and move, no second copy.
- L1139: A24 trace row says the user deletes from `archive/` by hand (was "empties").
- L1141: A26 trace row names the manifest, the move and the check in `archive_check.py` and `archive.md`.

## Leftover check
`grep -c` for `.original` and `copy-and-compare` across the five files: 0 hits.

Note for the user: ARCHITECTURE L335 still says `.work/` "moves with the folder at record close but is never part of the verified archive"; with a whole-folder move and a manifest of every file, that clause may want a look.

## Full suite on both systems
The user's answer of 2026-10-14 (A24): the full headless suite, every id and every run, runs on both Windows and macOS before a release, beside the unit tests and the six end-to-end tests. Run counts are stated per system (58 ids, 174 runs on each system); no doubled total was written. Two edits add a line, so line numbers below are after the edit: BUILD-PLAN gains one line at L55 and ARCHITECTURE one at L165, and everything after shifts by one.

### BUILD-PLAN.md
- L3: revision line gains "full headless suite on both systems per the user's answer of 2026-10-14".
- L54 to L56: stage 5 now lists the full headless suite, the unit tests and the six end-to-end tests on both systems.
- L83: the Windows re-run also settles the invocation form on Windows for the scripts, the hooks and the headless runner's child process.
- L321: WP14 acceptance says the runner and graders run the full suite on Windows and on macOS, with the same pass conditions.
- L337: WP16 acceptance says a release shows checks 2, 6 and 12 passed on both systems, check 6 being the runner started on each.
- L397: section 4.1 headless row, "Where" now says every id and every run on both Windows and macOS.
- L468: section 4.4 says 58 ids, 174 runs on each system, the whole suite on both systems before a release (check 6); the intake-and-archive-only repeat inside check 12 is gone.
- L581: section 5 introduction now needs checks 2, 6 and 12 passed on both systems.
- L588: release check 6 says the 58 ids, 174 runs on each system, pass on Windows and on macOS (was the user's machine).
- L608: changelog table row 5 lists the full headless suite and release checks 2, 6 and 12.

### ARCHITECTURE.md
- L3: revision line gains the clause.
- L163 to L165: `release.py` tree comment says the unit tests, the full headless suite with its graders and the six end-to-end tests run on each of Windows and Mac.
- L1140: A24 trace row adds the full headless suite to the release checks.
- L1205: section 14 release-checks sentence adds the full headless suite.
- L1220: the Windows-versus-Mac risk row adds the full headless suite to the pre-release runs.

### SPEC.md
- L3: revision line gains the clause.
- L105: Platform success criterion gains "the full headless suite passes on both Windows and macOS".

### ROADMAP.md
- L3: revision note gains the clause.
- L48: "On either system" group now names the full headless suite beside the unit tests and the six end-to-end tests.
- L78: stage 5 row names the full headless suite among the tests run on both systems.

## Emails and the goal check

Two of the user's answers of 2026-10-14 applied: emails arrive as pasted text or screenshots and never as mail files (A16, the line added 2026-10-14), and the readiness spec's third grader check, that every goal carries its verbatim quote at its location, now joins the two. No edit added or removed a line, so the line numbers below are the same before and after. `ROADMAP.md` has no line that describes email intake or counts the grader checks and was not edited. `SPEC.md` already listed "every goal sits verbatim at its location" among its readiness criteria (L94), so it needed no goal-check edit. The readiness spec's section 7 and section 9 wording on the `goals[]` pin was left alone, as asked. Each edited document's revision line gains "emails as pasted text or screenshots, and the goal-quote grader check, per the user's answers of 2026-10-14"; in ARCHITECTURE and SPEC the clause is verbatim although neither document needed a goal-check edit.

### ARCHITECTURE.md
- L3: revision line gains the clause.
- L199: call-intake description trigger "forwards an email thread" becomes "pastes an email or a screenshot of one" (description now 797 characters, under the 800 cap).
- L202: call-intake responsibilities restate email intake as pasted text handled like a document, a screenshot read by the model and cited by image and region, an attachment only as its own input, and no mail-file or mailbox parsing.
- L357: `transcript_measure.py` row: `email` now measures pasted text only, reads no mail file or mailbox and lists no attachment; a screenshot is read by the model, not the script.
- L369: `document-summary.md` snapshot: the map gains image regions for a screenshot, and "the attachments it carried" becomes an attachment the user added as its own input and said came with it.
- L395: `inputs/` file-map row: "an email with its attachments" becomes pasted text or a screenshot saved as an image, with an attachment only as its own input.
- L435: a conflict with a call may be anchored by image and region for a screenshot.
- L756: step 1 says pasted email text goes to `transcript_measure.py email` and a screenshot is measured by no script.
- L768: the email paragraph of 8.3 rewritten into pasted text, screenshot and attachment cases, with `unknown` wherever the text or image does not show a field and no mail-file or mailbox parsing.
- L1132: A16 trace row says emails arrive as pasted text or screenshots and never as mail files, per the user's answer of 2026-10-14.

### BUILD-PLAN.md
- L3: revision note gains the clause.
- L123: WP2 `add-document` acceptance: an email arrives as pasted text or a screenshot saved as an image, an attachment only when the user adds it as its own input.
- L165: "Why two scripts": `email` is for pasted email text; a screenshot is read by the model and measured by no script.
- L181: WP5 `email` acceptance bullet rewritten to pasted text only, no `.eml`, no attachment listing, with the screenshot handling stated beside it.
- L207: WP9 `transcripts.md` acceptance describes the email intake in its three shapes in place of "as a document set".
- L218: WP10 "when it runs" lists an email as pasted text or a screenshot in place of "with attachments".
- L232: WP10 fixtures and tests: the readiness graders carry three checks, the third being every goal's verbatim quote at its location.
- L321: WP14 readiness grader: "the two checks" becomes "the three checks" with the goal-quote check named.
- L462: constructed input 9 becomes one screenshot and one pasted thread plus one document the user added separately, with its link to H09 kept.
- L476: H09 adds "every goal carries its verbatim quote at its location" beside the independence note and element-per-pain checks.

### SPEC.md
- L3: revision line gains the clause.
- L20: intake-of-any-mix bullet: "an email with its attachments" becomes pasted text or a screenshot, and a sentence states how each is cited, that unshown fields stay `unknown`, and that an attachment counts only as its own input.
- L68: out-of-scope line gains parsing of mail files or mailboxes.

### stage-1b/build-readiness-spec.md
- L3: revision line gains the clause.
- L9: section 1 lists "an email as pasted text or a screenshot" in place of "an email with attachments".
- L48: section 6: "may join the two" becomes "joins the two then, so the grader checks are three", naming the goal-quote check.

### Left alone and worth the user's nod
- Script size figures: `transcript_measure.py` is still listed at 600 lines (ARCHITECTURE L357 and L361, BUILD-PLAN WP5 size). The `email` pass now parses less (no mail file, no attachment listing), so the figure may shrink; it was left as it stands.
- Not yet designed: how `verify-quotes` treats an extract cited from a screenshot, since the written-out text is the model's own reading of the image. The documents say only "cited by image and region".
- The constructed screenshot of input 9 has to be built as an image fixture by whoever writes WP14's inputs; the plan does not say how.
