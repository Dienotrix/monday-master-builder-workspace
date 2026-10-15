# s10-support-checkin: verifier report, first pass

Verifier run of 2026-10-13. No fixture file was edited. Everything here is fictional and stays fictional.

## Checks of brief section 7

1. **JSON validity and field order.** Pass. `answer-key.json` loads; 26 top-level fields, the 25 s1 to s10 fields in order (scenario_id through expected_leak_blocklist), `readiness` last. s10 has no `intake`, which is correct. The file is ASCII, 1,263 lines, as the log says.
2. **`readiness` complete, field by field against section 3.** Pass. Top-level fields are schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions, in the brief's order. `schema` is `readiness/1`. Pains carry id, quote, location, speaker_role, stated_or_excavated, outcome. Signals carry quote, location, pain, not_confirmed. Entities carry exactly the seven fields. `structure` carries products, build_target, build_target_reason, workspaces, native_reuse, leanings, patterns, element_per_pain. Leanings carry question, option, quotes, locations, condition, pattern. `existing`, assumptions, unmet_needs, ai_opportunities and verdict (cleared_for, conditions, reason) all have the shaped fields.
3. **Every key pain in `readiness.pains` and `element_per_pain`.** Pass. The key's 7 pains are present in array order (P6.1 to P6.6, P7), quotes and locations equal to the key's own; 7 element rows with the same ids. The section 8 numbering rule is followed and the unnumbered seventh entry is explained in the note and in `changes.md`.
4. **`moves_independently` on every entity with a parent.** Pass. 20 entities, 14 with a parent, every one has yes, no or unknown (the only unknown is the markup, with a stated reason in the log).
5. **At most five questions.** Pass. 5, ordered, each with kind (read-back, discovery, read-back, read-back, discovery), role and known.
6. **Valid `cleared_for`.** Pass. `none`, with the approval stop first among six conditions and the A11-2 point.
7. **No sales word in the block.** Pass. A search of the block for R-numbers, grade, gate, pass/fail and verdict words found only the field name `verdict` (the brief's own key name), the sentence in `note` that says "see verdict", and the transcript verb "pass it to Bev" in a quote. None is a sales verdict. No R-number, grade or gate name appears.
8. **`direction` rename.** Pass by not applying. s10 has no `intake`; `direction_of_show` is absent from the file.
9. **"Never written to" rule.** Pass. The search finds 14 hits outside the rubric. The current-state claim traces to Jordan at L50 (confirmed in the transcript: "whether anything writes back the other way and I tell him no"). The rule traces to the controller in s3 at 00:14:44 (confirmed: s3 transcript line 94, "that nothing, ever, writes back into Ajera"). The five prose places that stated it as self-evident now cite that source and say the read side is unresolved. The readiness Ajera incumbent line labels staying clear of Ajera as our safe default. Nothing needed rewording to the "unresolved" form because each claim has a client trace; the log records this.
10. **Review entry.** Pass. There is no FEEDBACK entry for s10, as the task states; nothing to apply. The section 8 tension is handled: the key says `should_plugin_propose_a_build: false` and the block says `none`, so the two agree and no disagreement sentence is required; the note says so and gives the reason. The judgment call (none against build-generic) is flagged for the planner in the log; I find it defensible, since the client set the need aside (L64), the Consultant committed to a conversation first (L65), and the target is a live client account. "None" with the reason is a valid verdict here.
11. **`verify_quotes.py` clean.** Pass. Rerun with `--json`: 82 pairs, 82 verified (9 presence only), 2 skipped (the two null `numbers` quotes), 0 unparsed, 0 near-misses, 0 misses, 0 unsupported, 0 warnings, no location notes.
12. **Unit count and spans.** Pass. The transcript has 80 units (80 non-empty lines), unchanged; its modification time is 13 September, before the pass, so no edit was made. The key's own 80-line statement predates the pass. The baseline table row for s10 lists only ten values under eleven headers (the units parsed column is missing for every row), so the unit count comes from the verifier's source line (80 units) and the file itself. Baseline protected units 35 and spans 49 are from the old key; the verifier now reports 38 protected units because the block cites existing lines with new quotes. No quoted span in the transcript changed, since the transcript is unchanged and all 82 quotes verify.
13. **README.** Not applicable. s10 has no README (s1 to s10).
14. **Coverage row.** Pass. `coverage-row.md` says the first-table row is unchanged and gives the tracked counts; I recounted against the files: traps 21, pains 7, vocabulary 15, expected questions 12, entities_and_workflows 13, commitments 6, requested changes 0, 80 lines, 1,834 spoken words (1,954 with labels), client share 62.9 percent, Consultant's longest turn 56 words at L69, Jordan's 69 words at L58. All true. Quote pairs 82 matches the verifier.
15. **Thin-case section 8 note.** Not required; the key is not a thin case and the old and new verdicts agree.
16. **Entity and sweep spot checks.** The consulting-firm entity lists civil, landscape, acoustical and commissioning, all in Jordan's L54 line. The Fenwick discipline is no longer stated as civil, which was the inference the log corrected.

## Observations, not failures

- The baseline table in `baseline.md` has a missing column for all rows; this does not affect s10.
- The log counts "25 occurrences in 12 places" for the search terms, which includes broader terms than mine (14 hits for the brief's terms). Both conclusions agree.

## Result

PASS
