# s25-client-documents — fix pass verification, first pass

Verifier's report, 2026-10-13. Everything here is fictional and stays fictional. No fixture file was edited. I read brief sections 7 and 8, the editor's `changes.md`, the review entry (FEEDBACK.md lines 42 to 52, in `for-review/`), the baseline row, the key, the README and `coverage-row.md`. For comparison I used the editor's `answer-key.before.json` in a scratch copy.

## Checks

1. **JSON validity.** Pass. `answer-key.json` loads as UTF-8 JSON. The only non-ASCII character is the en dash in the workspace name, which the brief allows.
2. **Field order.** Pass. The 25 fields are in the s1 to s10 order, `intake` is 26th and `readiness` is 27th and last. The "before" key's field list is an exact prefix of the new one.
3. **Readiness shape, top level.** Pass. `schema` is `readiness/1`. The keys are `schema`, `note`, `pains`, `signals`, `entities`, `structure`, `existing`, `assumptions`, `unmet_needs`, `ai_opportunities`, `verdict`, `questions`. The `note` is the brief's text verbatim.
4. **Readiness shape, field by field.**
   - Every entry has exactly the brief's fields in `pains` (10), `signals` (6), `entities` (21), `leanings` (7), `assumptions` (14), `unmet_needs` (5), `ai_opportunities` (4, all round 2), `questions` (5) and `incumbents` (6).
   - `structure` holds `products`, `build_target`, `build_target_reason`, `workspaces`, `native_reuse`, `leanings`, `patterns` and `element_per_pain`.
   - `existing` holds `account` and `incumbents`.
   - Work Management is the only product. The build target is `own-account`, with the A21 reason text. There is one workspace, "Wexcombe – Ops", which matches one product.
   - Every leaning pattern is one of the seven sweep patterns or `fork`.
5. **Every key pain present in `readiness.pains`.** Pass. The key's 10 `pains` entries match the block's 10 entries one for one (P1.1 to P1.5, P2.1 to P2.3, P3.1, P4.1), with identical quote and location. The numbering follows the exemplar rule. Stated or excavated agrees with the key's theme text: P3.1 and P4.1 are "stated, not graded", and the document statements are stated.
6. **Every pain in `element_per_pain`.** Pass. There are 10 rows, one per pain id: 7 `fixes`, 3 `copies-today's-tool` (P2.1 to P2.3), 0 `none`. The three `copies-today's-tool` verdicts are carried by leaning 4 and by question 3, which is the section 8 rule.
7. **`moves_independently` on every entity with a parent.** Pass. 11 of the 21 entities have a parent, and all 21 carry `moves_independently` with a value of `yes`, `no` or `unknown`. (`changes.md` says 10 with a parent; see fix 2.)
8. **At most five questions.** Pass. There are 5: 2 read-back (Q1, Q4) and 3 discovery. Each has `text`, `kind`, `role` and `known`. The "which monday account" question is not among them, as A21 requires for a prospect.
9. **Valid `cleared_for`.** Pass. The value is `build`. Six conditions; the first is the approval stop. The A11 line says no A11 question first matters for an own-account build and that the three decisions stay open.
10. **No sales word in the block.** Pass. I searched the block for R-numbers, grade words, gate names, "Nearly ready", "Not ready", met, partial, missing and "verdict". The only hits are the field names `verdict` (the brief's own), the phrase "fix pass" in `note`, and "ready to sign" in the certificate wording, which is client language and not a verdict. The v2 fields `rubric`, `expected_verdict`, `numbers`, `should_plugin_propose_a_build`, `pains`, `objections`, `commitments_and_next_steps`, `accepted_behaviours` and `expected_leak_blocklist` are byte-identical to the "before" key.
11. **`direction` rename.** Pass. `intake.type_header.direction` is present with value `no-show`, in the original position. `direction_of_show` appears nowhere in the key. The four `intake.files[]` entries carry no header fields. The README names the rename twice.
12. **"Never written to" rule.** Pass. The search terms were "never written", "not written", "write back", "writeback", "never touched", "written to", "written back", "never a write", "read-only", "one way", "never write". I found:
    - five occurrences of the unresolved-direction wording (`integrations_mentioned[0]`, `requested_changes[0].description`, `traps[26]`, the readiness `incumbents` entry for the results database, and a question's `known`);
    - the client's own lines (the database "cannot be replaced or altered", "stays the system of record", "can't be the place results live") kept as client constraints;
    - one unrelated hit, "never written into the figure's own fields", in `intake`, which is about the key's marking of an inferred sequence and not about a client system.
    
    The wording is "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the results database is our safe default, labelled as ours". Compliant.
13. **The review entry's items applied as recorded.** Pass. The entry is "keep, no fixture change". The three documents stay separate and no file was merged. The "Also" line says the gates read "First demo (v0.1) met" and that the s17 rename covers it. That is stage 1b input and waits for v2, so `expected_verdict.gates_met` is untouched, which the diff confirms. The README records the review and the disposition.
14. **Sweep corrections present in the fields `changes.md` names.** Pass. A structural diff of the key against the "before" copy lists exactly these paths and nothing else: `requested_changes[0].description`, `traps[19]`, `traps[26]`, `integrations_mentioned[0]`, `expected_structures.notes`, `vocabulary[5]`, `vocabulary[12]` and `vocabulary[14]` (`likely_monday_object`), `intake.alias_map` (11 to 14 entries, with `[2].note`, `[9]` and `[10]` changed and `[11]` to `[13]` added), the `direction` rename, and the added `readiness`. The three vocabulary entries now read "one child row per test under the sample (readiness, leaning 1)" and the like.
15. **Quote verifier clean.** Pass. `verify_quotes.py ... --json` gives 167 pairs found, 166 verified (11 presence only), 2 skipped (the two deliberate nulls), 0 unparsed prose, 0 near-misses, 0 misses, 1 unsupported. The unsupported one is `/rubric[0]/evidence[4]/quote`, the figure label "Log in sample register" in the PNG, which the baseline already lists. There are no location notes. All 36 new pairs verify, including the 8 new document extracts and the 20 new call quotes.
16. **Transcript units and spans.**
    - Pass on the unit count: the transcript has 88 units, 88 lines, 00:00:03 to 00:15:28. The baseline lists 56 "units parsed" for s25, which is the count of units carrying a quoted span, not transcript units; the after-run lists 58.
    - Pass on the difference: 3 new spans were added, at 00:13:45, 00:08:50 and 00:06:03, because the block cites those lines.
    - I diffed the verifier's spans output of the "before" key against the after key. Every previously quoted span is still contained in an after span, and no span was removed or shortened. The one apparent removal (00:06:03, 284 to 432) is that span now sitting inside a longer new span (239 to 432).
    - The transcript, docx, pdf and png are unmodified (modification times are 20 September; only the key and the README carry 13 October).
17. **Transcript edits inside existing units.** Pass, with none made. The decline of the mess pass is reasoned in `changes.md` section 7: the transcript had a mess pass on 2026-09-20, and the one long Consultant turn is a cited read-back.
18. **README counts against the files.** Pass. All of these are true of the files:
    - transcript 88 lines, 2,056 words (the Files table says "about 2,055", which is a fair round figure), client share 62.6 percent, longest unit 105 words at 00:06:03, Consultant's longest 85 at 00:12:48, 7 units of four words or fewer, 7 occurrences of " -- ", 9 `[laughs]`, 1 `[pause]`;
    - key 551 lines, 27 fields, alias map 14;
    - rubric 24 (11 / 8 / 1 / 3 / 1), objections 7, traps 36, leak entries 18, requested changes 3 add / 2 change, commitments 8, expected questions 10, vocabulary 16, accepted behaviours 17, attendees 3;
    - the readiness line (10 pains, 6 signals, 21 entities, 7 leanings, 10 element rows with 7 and 3, 6 incumbents, 14 assumptions, 5 unmet needs, 4 AI opportunities, 6 conditions, 5 questions with 2 and 3);
    - planted-defect locations: the conflict at 00:04:01 and 00:04:25 (lines 22 and 24), the interjection at 00:07:31, `Speaker 2` at 00:05:41, the platform claim at 00:13:51, the long playback at 00:12:48.
    
    The README is 97 lines, as `changes.md` says.
19. **`coverage-row.md` against the files.** Pass. Thirteen columns, the same as the existing row. Rubric 24 (11 / 8 / 1 / 3 / 1), pains 2 (2), objections 7, traps 36 (6), leak 18, requested changes 5 (3 / 2 / 0), quote strings 167 (the verifier's pairs found). The Review column reads "reviewed 2026-10-13; fix pass applied 2026-10-13". The COVERAGE.md row still shows 131 and "user review pending" because the merge step has not run, which is as the brief says.
20. **Section 8 note for a thin-case key.** Not applicable. `should_plugin_propose_a_build` is `true` and the v2 line is "Nearly ready", so the old fields agree with `cleared_for: build`. The `note` carries only the brief's text, correctly.
21. **Fork rule, brief section 3.** Fail. Leaning 3 (the priority approval, pattern `fork`) is in the block. The brief says a fork "keeps its existing entry elsewhere in the key and gains the same `leaning` there". The existing entry is `intake.conflicts[0]`, and it carries no leaning. The diff shows it unchanged, and `changes.md` does not say it was declined. See fix 1.
22. **`changes.md` counts.** One slip. Section 10 says 21 entities "10 with a parent"; the key has 11. Every other count in that table matches the key. See fix 2.

## Result

FAIL, on two small points. The key's data, the quotes, the sweep corrections, the README and the coverage row are all sound.

FAIL. Fixes needed:

1. `fixtures/s25-client-documents/answer-key.json`, `intake.conflicts[0]` (the entry for "whether a priority request is approved by the Laboratory Manager before allocation"): add a `leaning` field carrying the same leaning as `readiness.structure.leanings[2]`. The text is the option "priority flag with a notification built; the approval step built neither way; if the 9th settles on the procedure it becomes a status the Laboratory Manager sets (W-3), if on reception's route the flag alone", with the condition "the Quality Manager and the Laboratory Manager together on the 9th". Put it after the entry's existing fields, and keep the entry's quotes unchanged. Then rerun `verify_quotes.py`, which must stay at 0 misses, and log the change in `changes.md` section 3 or 10 and in the README's fix-pass line.
2. `fixtures-work/_fixpass/s25-client-documents/changes.md`, section 10, the `entities` row: change "21 (10 with a parent, all with `moves_independently`)" to "21 (11 with a parent, all with `moves_independently`)".

---

# Second pass, after the fixer

Verifier's report, 2026-10-13. Everything here is fictional and stays fictional. No fixture file was edited. I read `fix.md`, the changed key, README and `changes.md`, and reran the checks against the pre-pass copy `answer-key.before.json`.

## Checks

1. **Fix 1, `intake.conflicts[0].leaning`.** Pass. The entry now ends with `leaning` after `callback`. Its `option` and `condition` equal `readiness.structure.leanings[2]` word for word (compared by script). The entry's other fields are unchanged.
2. **Fix 2, `changes.md` section 10.** Pass. The entities row reads "21 (11 with a parent ...)", and the key holds 21 entities, 11 with a parent.
3. **README and `changes.md` log the fix.** Pass. The README's fix-pass line and `changes.md` (method paragraph, section 3, section 10) name the conflict leaning.
4. **JSON validity and field order.** Pass. UTF-8 JSON, 27 fields, the 25 in s1 to s10 order, `intake` 26th, `readiness` 27th and last; the pre-pass field list is an exact prefix.
5. **Structural diff against the pre-pass copy.** Pass. The paths that differ are the ones `changes.md` names: `traps[19]`, `traps[26]`, `requested_changes[0].description`, `expected_structures.notes`, `integrations_mentioned[0]`, three `vocabulary` entries, the alias map, the type-header rename, `intake.conflicts[0].leaning` and the added `readiness`. `rubric`, `expected_verdict`, `numbers`, `should_plugin_propose_a_build`, `pains`, `objections`, `commitments_and_next_steps`, `accepted_behaviours` and `expected_leak_blocklist` are identical.
6. **Readiness shape.** Pass. Twelve top-level fields in the brief's order; `schema` is `readiness/1`; the second-pass counts match the first pass (10 pains, 21 entities, 5 questions).
7. **Every pain present, with an element row.** Pass. The key's 10 pain quotes equal the block's 10 in order; `element_per_pain` has one row per id, in the same order.
8. **`moves_independently`.** Pass. All 21 entities carry yes, no or unknown, including the 11 with a parent.
9. **Questions and `cleared_for`.** Pass. 5 questions; `cleared_for` is `build`; the first condition is the approval stop.
10. **No sales word in the block.** Pass. A scan of the block's text for R-numbers, grade, gate, "Nearly ready", "Not ready", met, partial, missing and "Ready" found nothing.
11. **Direction rename.** Pass. `intake.type_header.direction` is `no-show`; `direction_of_show` is absent from the file.
12. **Never-written rule.** Pass. "writeback" appears five times, all in the unresolved-direction wording; "never written" appears once, in the unrelated sentence about the key's own marking of an inferred sequence; "not written", "write back" and "never touched" do not appear.
13. **Review entry.** Pass. The entry is "keep, no fixture change"; the three documents stay separate; the "Also" line waits for v2 and `expected_verdict.gates_met` is untouched.
14. **Quote verifier.** Pass. `--json`: 167 pairs, 166 verified (11 presence only), 2 skipped, 0 unparsed, 0 near-misses, 0 misses, 1 unsupported (the figure label in the PNG, as in the baseline), no warnings, no location notes. The pair count did not move, as `fix.md` says.
15. **Transcript units and quoted spans.** Pass. 88 lines and 88 units, as at the first pass; the baseline's 56 counts units with a quoted span. The transcript, docx, pdf and png carry their 20 September modification times, so no quoted span changed; the fix touched no quote.
16. **README and coverage row.** Pass. The README is 97 lines, the key 551 lines, as stated; the key's line count did not change with the fix. `coverage-row.md` is unchanged and its counts (24, 2, 7, 36, 18, 5, 167) still hold.
17. **Section 8 thin-case note.** Not applicable. The old verdict fields agree with `build`.

## Result

PASS. Both fixes from the first pass are applied and nothing else moved.
