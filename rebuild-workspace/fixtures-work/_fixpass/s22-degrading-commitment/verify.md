# s22-degrading-commitment — verifier report, first pass

Verifier's report, 2026-10-13. Everything here is fictional and stays fictional. I edited no fixture file. I compared the edited files with the editor's pre-edit copies kept in the session scratchpad, which is how the transcript and field-level checks below were made.

## Checks

1. **Quote verifier.** PASS. `verify_quotes.py ... --json` exits 0: 265 pairs, 263 verified (27 presence only), 1 skipped, 2 unparsed prose (the two `intake.second_hand` descriptions the baseline already lists), 0 near-misses, 0 misses, 0 unsupported, 0 location notes. Sources parse as 191 and 150 units.
2. **JSON validity and field order.** PASS. The key loads as UTF-8 with 27 fields. The first 25 match the s1 order exactly, `intake` is 26th and `readiness` is last. It is 477 lines, as the README and `changes.md` state.
3. **Readiness shape against brief section 3.** PASS. The top-level fields are schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions, in the brief's order. `schema` is `readiness/1` and `note` is the brief's text word for word. Every sub-object has exactly the brief's field names:
   - pains: id, quote, location, speaker_role, stated_or_excavated, outcome.
   - signals: quote, location, pain, not_confirmed.
   - entities: name, parent, moves_independently, shared_resource, goes_stale, source, evidence.
   - structure: products, build_target, build_target_reason, workspaces, native_reuse, leanings, patterns, element_per_pain.
   - leanings: question, option, quotes, locations, condition, pattern.
   - existing: account, incumbents (system, authority, evidence).
   - assumptions: statement, question.
   - unmet_needs: need, clock, why_not_met.
   - ai_opportunities: pain_or_need, kind, round, probe_basis, idea.
   - verdict: cleared_for, conditions, reason.
   - questions: text, kind, role, known.

   Value ranges hold:
   - Pain `stated_or_excavated` takes only the two allowed values.
   - Entity `source` is spoken (22) or assumed (1, with `evidence: null`).
   - Boolean fields are booleans.
   - The five AI kinds and the probe bases are valid.
   - Every signal and AI `pain_or_need` points at an existing pain id.
4. **Every key pain in `readiness.pains` and `element_per_pain`.** PASS. The key's ten `pains` entries equal the block's ten entries in order, quote and location identical. They are numbered P1.1 to P6.1 and `changes.md` explains the numbering. `element_per_pain` has ten rows in the same order: 4 fixes, 1 copies-today's-tool (P2.2, justified by exemplar rule two), 5 none.
5. **`moves_independently` on every entity with a parent.** PASS. Of 23 entities, 20 have a parent and all 20 carry yes or no. The 3 without a parent are unaffected.
6. **At most five questions.** PASS. There are five: 3 read-back, 2 discovery. Each has a role and a `known`. The account question is correctly absent for a prospect (A21).
7. **`cleared_for`.** PASS. The value is `build`. The old fields agree: `should_plugin_propose_a_build` is true and the verdict is "Nearly ready". The section 8 disagreement sentence is therefore correctly absent from the `note`.
8. **No sales word in the block.** PASS. I searched the serialized block for R-numbers, C-numbers, grade, gate, pass, fail, partial, missing, score and verdict. The only hits are the brief's own field names (`verdict` as the `element_per_pain` key and the `verdict` object), the word "pass" inside the standard `note` sentence's "fix pass", and the finance director's own "condition met" inside a signal quote. None is a grade or gate.
9. **`direction` rename.** PASS. `intake.type_header.call_1` and `call_2` both carry `direction`, in the same position (fourth field), and `direction_of_show` is absent from the key and the transcripts. Minor, not a fail: the README's conventions bullet still names the old field once, as the history of the rename. That is allowed ("the README's prose follows if it names the field"), but `changes.md` section 2 says the field "appears nowhere in the key or the README now", which is not literally true of the README.
10. **Never-written rule.** PASS. I searched the key for "never written", "not written", "write back", "writeback", "never touched" and the near forms "writes back", "writing back", "nothing writes" and "write into". Every route-software claim traces to the systems administrator's client quotes (call 2, 00:14:56; 00:22:28; 00:24:43), now located beside the claim, or is labelled as the Consultant's own commitment (`intake.claims_by_our_side[3]`). The accounting-system entries in `integrations_mentioned[2]` and in the incumbents read "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear ... is our safe default, labelled as ours". The hits in `rubric` (v2 material) are client-backed and untouched. "Never written up" in the P3 pain theme describes the loss paperwork and is not a system claim.
11. **Review entry, item 1 (loss charges).** PASS. Each change sits in the field the entry names:
    - `expected_questions_before_building[7]` is the open question: dock check before tipping or bin tags, the next route and Sunday invoice, who keys it. It names the facts at call 1 00:07:48, call 1 00:22:48 and call 2 00:02:39, is routed to the plant manager and finance director, and states that nothing in the key says a write-up reaches the route by itself.
    - `expected_structures.notes`, `integrations_mentioned[2]` and the two `vocabulary` entries (loss clause, soil dock) are rewritten as recorded.
    - In the whole key, "reaches the route" now occurs only in negations and "before the route closes" only in the finance director's quoted words.
    - The block carries it as leaning 6, `element_per_pain` P3.1 and P3.2 (none), an unmet need, a verdict condition and question 1.
12. **Review entry, item 2 (par changes).** PASS.
    - `requested_changes[0].description`, `expected_structures.notes`, `vocabulary["par change"]` and `traps[23]` now say the status is a named person's claim, v0.1 shows the queue and the confirmation step and not the sheet updating, and the two conditions (call 2, 00:22:22 and 00:22:28) pull against each other.
    - The unverified read-only read-back is recorded as a possibility in `expected_questions_before_building[5]`, the notes, leaning 5's condition and question 2.
    - The standing line (a board status set by a person is a claim) also covers the credit status.
    - The key has no `forks` field, so the fork lives in leaning 5 with `pattern: "fork"`. `changes.md` flags this for the planner.
13. **Field-level change set outside the block.** PASS. Against the pre-edit key, 21 paths changed, 2 were renamed (`direction`), none were added or removed. All 21 are accounted for in `changes.md`: the items above, the sweep corrections (`entities_and_workflows[8]`, `integrations_mentioned[0]`), the s21 line (`commitments_and_next_steps[9]` and `[10]`) and the word-count fields. `rubric`, `expected_verdict` and `numbers` are untouched.
14. **Transcript edits.** PASS. A diff against the pre-edit files shows exactly six changed lines: call 1 at 00:21:37, 00:23:11 and 00:28:30; call 2 at 00:02:21, 00:14:38 and 00:22:50. Each is a filler, false start or tail added inside an existing unit. The 00:22:50 edit sits after the protected first sentence; the spans listing shows no protected span in the other five edited units (the `--spans` hit at call 1 L82 is a different unit from call 2 00:14:38). Unit counts are 191 and 150, equal to the pre-edit parse (the baseline table's s22 row has one cell fewer than its header and carries no units-parsed figure, so I compared with the pre-edit files directly). The units protected and spans figures move from 165 and 176 to 167 and 182 only because the block's new located quotes protect more spans, not because any quoted text changed.
15. **README counts.** PASS. I recomputed by the README's own rule (whitespace tokens after the label, bracket tags and bare `--` excluded). Call 1 has 4,947 words and a longest Consultant turn of 127 at 00:21:37; call 2 has 3,589 words and a longest turn of 128 at 00:21:19. Client shares are 71% (39 / 32) and 64% (34 / 16 / 7 / 7). Each matches the README, `transcript_format`, `intake.files[].words_spoken`, `max_unit_words.call_1` and `delivery_notes.call_1.longest_own_side_turn`. Counts re-derived from the key all match: rubric 36 (27 / 5 / 2 / 1 / 1), objections 8, traps 30, leak list 18, requested changes 4 (2 add, 2 change, 0 remove), commitments 12, pre-build questions 10, vocabulary 16, entities and workflows 13, integrations 5, compliance 6, accepted behaviours 14, attendees 5, quote strings 263 (236 located plus 27 presence-only). The block counts in the README (6 signals, 23 entities, 9 leanings, 10 element rows, 7 incumbents, 14 assumptions, 6 unmet needs, 5 AI opportunities, 5 questions) match the key. Planted-defect locations are unchanged, and the verifier confirms the quotes at them.
16. **`coverage-row.md`.** PASS. All columns match the files: 36 (27 / 5 / 2 / 1 / 1), 4 (3), 8, 30 (6), 18, 4 (2 / 2 / 0), 263. The Review column reads "reviewed 2026-10-13; fix pass applied 2026-10-13". The only moved count is quote strings, 231 to 263 (verified: 263 = 236 + 27). The row has the existing thirteen-column shape.
17. **Prose quotes inside key fields.** PASS. I extracted the long single-quoted client phrases from the block and from the changed fields and searched them in the transcripts after normalizing. The two non-matches were an apostrophe cut-off inside a question and a status label ("Confirmed on the printed sheet"), neither a quotation.
18. **Thin-case note (section 8).** Not applicable. The old fields and the block agree.

## Result

PASS
