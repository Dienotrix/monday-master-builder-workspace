# s18-identity-collapse — verifier report, first pass

Verified 2026-10-13. No fixture file was edited. Each line is a check, its result and the evidence.

## Quote verifier

- PASS. `verify_quotes.py ... --json` reports 193 pairs, 193 verified (31 presence only), 0 skipped, 0 unparsed, 0 near-misses, 0 misses, 0 unsupported, 0 warnings. No location notes. The count matches `changes.md` section 10.
- PASS. Quoted spans unchanged. The `--spans` output shows 129 protected units and 147 spans. The five mess-pass insertions sit at 00:01:56, 00:19:37, 00:34:29, 00:37:52 and 00:44:22. Only 00:01:56 holds a span ("I'm not going to show you anything today."); it is intact and the insertion is before it. The other four units hold no span. Because every cited quote still verifies verbatim at its location, no span can have changed.
- Note on the baseline. The baseline row for s18 holds ten values under eleven headers (146, 146, 0, 0, 0, 0, 0, 31, 115, 127), so the "units parsed" figure is not readable from it. The units count is therefore taken from the README's "262 turns on 266 lines ... as before" and from the file: see the unit check below. The baseline's 31 presence-only pairs match today's 31. The protected-unit and span counts grew (115 to 129, 127 to 147) because the readiness block cites 47 new pairs; that is expected.

## Structure of the key

- PASS. JSON loads as UTF-8. The only non-ASCII character is the en dash in the workspace name, which the brief allows.
- PASS. Field order: the first 25 fields equal the s1 key's first 25 in order; `intake` is 26th and `readiness` is 27th and last.
- PASS. `readiness` keys in brief order: schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions. `schema` is `readiness/1`. The `note` is the brief's text.
- PASS. `structure` carries products (Work Management), build_target `own-account`, the brief's A21 reason, workspaces (`Brindlehaven – Ops`), native_reuse, leanings, patterns, element_per_pain. Each leaning has question, option, quotes, locations, condition, pattern. Each pain has id, quote, location, speaker_role, stated_or_excavated, outcome. Each signal has quote, location, pain, not_confirmed. Each entity has all seven fields. Each assumption, unmet need and AI opportunity has the brief's fields.
- PASS. Every key pain is in `readiness.pains`: the ten quotes and locations equal the key's `pains` array in order. The ten ids (P1.1 to P1.3, P2.1, P2.2, P3.1, P3.2, P4.1, P3.3, P5.1) equal the ten `element_per_pain` rows exactly. Verdicts: seven fixes, two copies-today's-tool, one none (P4.1), which is also in `unmet_needs`.
- PASS. 27 entities, 19 with a parent, every one with `moves_independently` in yes, no or unknown.
- PASS. 5 questions, within the ceiling, each with text, kind (read-back or discovery), role and known.
- PASS. `verdict.cleared_for` is `build`, a valid value. Conditions open with the approval stop. The reason is one sentence.
- PASS. No R-number, grade, gate name or verdict word in the block. A search of every string value found only "fix pass" in the brief's own note, "passes" in ordinary prose in leaning 9, and the field name `verdict` itself. A21, A11 and P-19/P-21 are the brief's own references.
- PASS. Thin-case note: not required. `should_plugin_propose_a_build` is true and `expected_verdict.verdict` is "Discovery complete", so they agree with `build`. The note carries only the brief's sentence, as `changes.md` says.
- PASS. `direction` rename: `intake.type_header.direction` is `no-show`; `direction_of_show` appears nowhere in the folder (key, README, transcript).
- PASS. Never-written rule. A search of the key for the listed phrases finds each claim reworded to "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear ... is our safe default, labelled as ours" (key lines 15, 28, 116, 117, 162, 198, 227, 451, 475, 476 and others). The remaining hits are the transcript quote "Agreed, and nothing writes to it", the R9 rubric note (which cites our own line and is v2 material, logged), a question about a read-only export, and "untouched" about the three ordinary words. None is a claim that a client system is never written to.

## The review entry (FEEDBACK.md lines 176 to 186)

- PASS, item 1. `expected_monday_products[0].why` requires one capacity-aware schedule across lift-out, launch, relaunch, visitor lift and repeat lift, each with boat, type, date and tide window, checked against the day's tide-set capacity, with the arrangement an implementation choice and provisional. It is carried into `accepted_behaviours[1]`, `lookalike_traps[4]`, the vocabulary entries for lift, launch, hoist, visitor lift and re-lift, question 3 and `expected_structures.notes`. Leaning 1 cites 00:05:29, 00:21:08, 00:20:01 and 00:09:48, the review's four quotes.
- PASS, item 2. The job card lists requested work items, each done or remaining, updated by the workshop manager or the office; the printed sheet carries the remaining items; the launch warning fires on a launch inside the fortnight with work remaining. Present in `why`, `accepted_behaviours[1]`, `requested_changes[1]`, vocabulary (job card, the sheet, launch), and question 6. Leaning 2 cites 00:05:00, 00:11:34, 00:23:18 and 00:36:51, the review's quotes. `rubric`, `expected_verdict` and `numbers` are untouched.

## Transcript and counts

- PASS. Transcript: 262 `[HH:MM:SS]` units, 267 split lines (266 lines plus the final newline), matching the README and the verifier's 262. The five insertions are inside existing units, stamps strictly increasing and unit numbering unchanged. ASCII only.
- PASS. README words: 6,178 by whitespace split after the label (recounted exactly). Talk share recounted: Tadhg Devlin 27.2, Jon Ashby 17.6, John Rudge 14.8, borrowed label 13.5, Consultant 26.9; client 73.1 percent. Longest unit 118 words at 00:38:40. 24 units of four words or fewer. Lowercase-initial units at 00:05:49 and 00:15:03. Zero adjacent same-label pairs.
- PASS. Planted defects: `John` 21 spoken uses (58 minus 37 labels), `Maxine` 36 (66 minus 30 labels). `tide` 14 (13 ordinary plus one vocative), `tie` 3 (2 plus 1), `tag` 2 (1 plus 1), so three coerced against sixteen ordinary. The README places the coerced words at 00:05:49, 00:11:11 and 00:15:03; the first and last are the lowercase-initial stamps.
- PASS. Alias map: 7 entries, 30 forms (13, 4, 5, 4, 1, 2, 1), as the README states. Key is 534 lines; longest line 2,646 characters.
- PASS. Quote strings: 163 on the COVERAGE basis, 132 with a location and 31 quote-only (objections 12, commitments 6, requested changes 6, intake signals 4, numbers 2, account context 1), as the README states; 193 in the verifier.
- PASS. `coverage-row.md`: 13 columns in the calibration-table shape. Rubric 36 (23 met, 7 partial, 2 missing, 3 met-with-residual, 1 not-obtainable, matching the stated order), objections 12, traps 28 with 7 look-alike, leak entries 15, requested changes 6 (3 add, 2 change, 1 remove), quote strings 163. Review column reads "reviewed 2026-10-13; fix pass applied 2026-10-13". The pains-graded figure "4 (2)" is unchanged from the old COVERAGE row.
- PASS. Standing lines: `commitments_and_next_steps[0]` and `[1]` now say committed at 00:43:10 and 00:43:32, not yet done. Entry `attendees[3].decision_role` separates our play-back from what the workshop manager asked for.

## Result

PASS
