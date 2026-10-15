# s8-discovery-enterprise-pmo: verifier report, first pass

Verified 2026-10-13. Everything here is fictional and stays fictional. No fixture file was edited. For the "before" state I compared against the pre-edit snapshot of the key and transcript that the session kept in its scratchpad (`snap/s8-discovery-enterprise-pmo/`).

Fixture files: `answer-key.json` (edited), `transcript.txt` (WebVTT, unchanged). There is no README for s1 to s10. The review entry for s8 is "No review entry", so the checks are the sweep, the never-written rule, the standing lines, the readiness block, and the A6 portfolio default on the structure.

## Checks from brief section 7

1. **JSON validity.** Pass. The key loads as UTF-8 JSON; a dump with two-space indent, `ensure_ascii=False` and a trailing newline reproduces the file byte for byte.
2. **Field order.** Pass. 26 top-level fields; the first 25 are in the original s1 to s10 order (identical to the snapshot's order), `readiness` is last, and there is no `intake` field in this fixture.
3. **Readiness present and complete, field by field against brief section 3.** Pass. Top level: schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions, in that order. `schema` is `readiness/1`; `note` is the brief's text. `structure` has products, build_target, build_target_reason, workspaces, native_reuse, leanings, patterns, element_per_pain, in order. Every pain, signal, entity, incumbent, assumption, unmet need, AI opportunity and leaning carries exactly the brief's field names. `build_target` is `own-account` with the brief's reason; `workspaces` is `["Bellamy Ridge – Ops"]` with the en dash; products are Work Management only, with the A6 portfolio explained in `native_reuse`.
4. **Every key pain in `readiness.pains` and in `element_per_pain`.** Pass. The key holds 24 pains; `readiness.pains` holds 24 with identical quote and location for each (compared pair by pair), ids P1.1 to P5.2. `element_per_pain` has 24 rows in the same order (20 fixes, 3 none, 1 copies-today's-tool), matching changes.md.
5. **`moves_independently` on every entity with a parent.** Pass. 36 entities, 30 with a parent, all 36 carry yes, no or unknown (29 yes, 6 no, 1 unknown). Every entity has the seven fields in order, boolean flags are real booleans, `source` is always `spoken`. Note, not a failure: parents are written as short names ("project", "person", "health system") and resolve to the longer entity names by prefix; every one resolves.
6. **At most five questions.** Pass. Five (four read-back, one discovery), each with text, kind, role, known. Each read-back rests on a signal present in `signals`.
7. **Valid `cleared_for`.** Pass. `build`. The verdict lists the approval stop first, then the A11 point, and the reason is one sentence. The key's `should_plugin_propose_a_build: true` agrees with `build`, so no section 8 note sentence is needed; none was added.
8. **No sales word in the block.** Pass. I searched every non-quote string in the block for R-numbers, grade, gate, verdict, Met/Partial/Unmet, proposal, pricing, score and pass/fail. The only hits are ordinary words: "pass" in "fix pass", "propose"/"proposed" in the Consultant's own quoted phrase, in a leaning option and in a Power BI description. None is a sales term. The key field name `verdict` is the brief's own name for the block's `verdict` object.
9. **Direction rename.** Pass (nothing to do). s8 has no `intake` and no `type_header`; `direction_of_show` is absent and no key named `direction` exists. The word appears only in prose ("integration direction").
10. **Never-written rule.** Pass. I searched the whole key for "never written", "not written", "write back", "writeback", "never touch", "written to", "read-only", "one way", "stays the source", "untouched" and "not touched". "Writeback" appears three times, all in the corrected form ("writeback and integration direction unresolved; v0.1 does not depend on either; staying clear is our safe default, labelled as ours"), for Procore, Sage and the burn leaning. "Untouched" and "not touched" appear for the client's own monday account (incumbent and verdict condition 3); those are our scope decision under A21 (the proof of concept is built in the user's own account), not a claim about a client system's data, so they do not need a client quote. The original key had none of these phrases, which matches changes.md section 2.
11. **Review-entry items applied.** Pass. There is no review entry. Against the snapshot, exactly five existing fields changed: `vocabulary[3]` (health), `vocabulary[11]` (ICRA), `traps[5]`, `expected_structures.lookalike_traps[8]`, `expected_structures.notes`; plus the added `readiness`. `rubric`, `expected_verdict`, `numbers` and `should_plugin_propose_a_build` are identical to the snapshot. Each change matches its entry in changes.md and its leaning in the block. The two short inline quotes the edits introduced ("Occupied-renovation supers, there are four.", "it's per work area, and it expires") are each found once in the transcript.
12. **`verify_quotes.py`.** Pass. Run with `--json`: 417 units, 283 pairs found, 283 verified (25 presence-only), 0 skipped, 0 unparsed prose, 0 near-misses, 0 misses, 0 unsupported, 0 warnings, no location notes, empty `refused_quotes_not_checked`. The pre-edit key gave 222 pairs; every quote string in the old key is still in the new key (0 missing), so 61 pairs were added.
13. **Transcript unit count and quoted spans.** Pass. The transcript is byte-identical to the snapshot (same SHA-1, `cmp` clean) and unchanged in time since 12 September; 417 cues, 417 timing lines. The baseline row for s8 records 134 units holding spans and 167 merged spans (its `units parsed` column is not in the table; the current 417 equals the 417 the verifier read from the snapshot). The `--spans` output now shows 152 units and 186 spans: the rise is the new block's quotes, and because the text is identical and every old quote persists, no previously quoted span moved.
14. **README and coverage row.** Pass, with one wording error (fix 2). There is no README for s8. `coverage-row.md` carries the three-column row and it is identical to line 22 of `COVERAGE.md`. The counts it states are true of the key: traps 31, pains 24, vocabulary 24, expected questions 16, entities_and_workflows 14, commitments 9, objections 8, 417 cues, 26 top-level fields, UTF-8 key, ASCII transcript (no non-ASCII bytes in the transcript). The row's closing paragraph says the review line "lives in `changes.md` beside this file"; it does not (see fix 2).
15. **Thin-case note.** Not applicable. s8 is a strong case and the verdict agrees with the old fields.

## Further checks I ran

- **Entity evidence locations** (not covered by the quote verifier, since the field is not named quote): all 36 cue numbers and timestamps match the transcript, and the speaker matches. The incumbent evidence stamps also match.
- **Pain outcomes** (also outside the verifier): every non-null outcome is verbatim in the transcript; 6 are null as changes.md says (P2.5, P4.1 to P4.3, P5.1, P5.2). Counts match changes.md: 15 excavated, 9 stated.
- **Changes.md counts:** signals 8, entities 36, leanings 10, patterns 5, incumbents 12, assumptions 18, unmet needs 7, AI opportunities 6 all match the file. Leaning patterns are drawn from the seven-pattern list only, and the "no hit" results (alias map, expected output) are written as results rather than forced leanings, as section 8 asks.
- **Inline quotes inside prose fields of the block** (questions, assumptions, leanings, conditions): I checked every single-quoted span of three words or more against the transcript. One does not match; see fix 1.

## Findings

- **Inline quote spliced from two speakers.** `readiness.questions[2].text` addresses Ines and says the June collision was 'confirmed, verbally, in the hall'. The transcript has Warren saying "I had him confirmed. Verbally." (cue 155) and Ines saying "Verbally, in the hall, which is the problem." (cue 156). The quoted string joins the two and is not verbatim at either cue, and it puts Warren's word in Ines's mouth. The brief requires every quote the block introduces to be copied from the transcript.
- **Review line not where the coverage row says.** `coverage-row.md` says the review line is in `changes.md`, which holds no such line.

## Result

FAIL

1. `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo/answer-key.json`, `readiness.questions[2].text`: replace 'confirmed, verbally, in the hall' with a verbatim quote from the transcript, for example 'Verbally, in the hall, which is the problem' (Ines, cue 156), or drop the quote marks and paraphrase ("the June collision was a verbal confirmation in the hall"). Rerun `verify_quotes.py` and the inline-quote check afterwards; the key must stay at zero misses.
2. `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_fixpass/s8-discovery-enterprise-pmo/coverage-row.md`, last paragraph: either add the line `reviewed 2026-10-13; fix pass applied 2026-10-13` to `changes.md` (the s1 exemplar's coverage-row.md carries the same sentence, so the merge step may expect it there) or reword the paragraph so it no longer says the line already lives in `changes.md`.


---

# Second pass

Verified 2026-10-13 after the fixer's round (`fix.md`). Everything here is fictional and stays fictional. No fixture file was edited. For the "before" state I used the same pre-edit snapshot in the session scratchpad (`snap/s8-discovery-enterprise-pmo/`).

## Fixes from the first pass

1. **Spliced quote in `readiness.questions[2].text`.** Pass. The text now opens "Ines, on the June collision you said 'Verbally, in the hall, which is the problem'." That span is Ines Kovalenko's own line (transcript line 625, cue 156), and Warren's "I had him confirmed. Verbally." (line 621) is no longer quoted. I re-ran the inline-quote check over every single-quoted span of fifteen characters or more in the whole block, normalising case, spacing and apostrophes: no span is missing from the transcript.
2. **Coverage row's claim about the review line.** Pass. The last paragraph of `coverage-row.md` now says the review line `reviewed 2026-10-13; fix pass applied 2026-10-13` is stated in that file and not in `changes.md`, and leaves the merge step to record it. The statement is true: `changes.md` holds no such line and no longer claims to.

## Checks from brief section 7, again

1. **JSON validity.** Pass. The key loads as UTF-8; a two-space dump with `ensure_ascii=False` and a trailing newline reproduces the file byte for byte.
2. **Field order.** Pass. 26 top-level fields, the first 25 in the original order, `readiness` last, no `intake`.
3. **Readiness shape.** Pass. Top level: schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions. `structure`: products, build_target, build_target_reason, workspaces, native_reuse, leanings, patterns, element_per_pain. `note` is the brief's text.
4. **Every pain present.** Pass. 24 pains in the key, 24 in `readiness.pains` with identical quote and location pair by pair, and 24 `element_per_pain` rows whose pain ids equal the id set.
5. **`moves_independently`.** Pass. 30 entities carry a parent, each with yes, no or unknown.
6. **At most five questions.** Pass. Five: four read-back, one discovery.
7. **`cleared_for`.** Pass. `build`, which agrees with the key's `should_plugin_propose_a_build: true`, so no section 8 note sentence is needed and none is present.
8. **No sales word in the block.** Pass. Searched for R-numbers, grade, gate, Met, Partial, Unmet, proposal, pricing, score: no hits. The word "verdict" appears only as the field name of each `element_per_pain` row and of the block's `verdict` object, which are the brief's own names.
9. **Direction rename.** Pass. No `intake`, no `type_header`; `direction_of_show` is absent from the file.
10. **Never-written rule.** Pass. Searching the whole key: "never written", "not written", "write back", "never touch", "written to" give no hits. "Writeback" appears three times, all in the corrected "unresolved; v0.1 does not depend on either" form. "Untouched" and "not touched" appear once each, about the client's own monday account, which is our A21 scope decision and not a claim about a client system's data.
11. **Review-entry items.** Pass. There is no review entry. Against the snapshot, the only changed existing fields are `vocabulary`, `traps` and `expected_structures`, the same five edits the first pass confirmed; `rubric`, `expected_verdict`, `numbers` and `should_plugin_propose_a_build` are identical. The fixer's edit sits inside `readiness`, so no existing field moved.
12. **`verify_quotes.py --json`.** Pass. 417 units, 283 pairs found, 283 verified (25 presence-only), 0 skipped, 0 unparsed prose, 0 near-misses, 0 misses, 0 unsupported, 0 warnings, no location notes, 0 refused quotes. The counts equal the first pass, as the fixer said they would.
13. **Transcript units and quoted spans.** Pass. `cmp` against the snapshot is clean, 417 timing lines, 57,171 bytes, all bytes below 128. The baseline row gives no separate unit count; its units-parsed figure for s8 is the 417 the verifier reads. The `--spans` output shows 152 units and 186 spans, the same as the first pass; the baseline's 134 units and 167 spans rose only through the new block's quotes, and every earlier quote persists, so no previously quoted span moved.
14. **README and coverage row.** Pass. There is no README for s8 (s1 to s10 have none). `coverage-row.md` carries the three-column row, identical to line 22 of `COVERAGE.md`, and its stated counts match the key as the first pass showed (traps 31, pains 24, vocabulary 24, expected questions 16, entities_and_workflows 14, commitments 9, objections 8, 417 cues, 26 fields).
15. **Thin-case note.** Not applicable; s8 is a strong case.

## Result

PASS
