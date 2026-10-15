# s23-symmetric-shred — verifier report, first pass

Verifier's log, 2026-10-13. I edited no fixture file. Everything here is fictional and stays fictional. Checks follow brief section 7, then section 8. Evidence comes from loading the key with Python, from `verify_quotes.py --json` and `--spans`, and from reading the transcript lines the key cites.

## Section 7

1. **JSON validity.** Pass. `answer-key.json` loads as UTF-8 JSON. It is 496 lines, which matches the README and `changes.md`.
2. **Field order.** Pass. There are 27 top-level fields: the 25 in the s1 to s10 order, `intake` 26th, `readiness` 27th and last. The 26 fields of `answer-key.before.json` appear in the same order at the front.
3. **Readiness present and complete.** Pass.
   - Top-level order is `schema, note, pains, signals, entities, structure, existing, assumptions, unmet_needs, ai_opportunities, verdict, questions`, exactly as in brief section 3.
   - `schema` is `readiness/1`.
   - Every sub-object carries exactly the brief's fields in the brief's order:
     - pains: `id, quote, location, speaker_role, stated_or_excavated, outcome`
     - signals: `quote, location, pain, not_confirmed`
     - entities: `name, parent, moves_independently, shared_resource, goes_stale, source, evidence`
     - structure: `products, build_target, build_target_reason, workspaces, native_reuse, leanings, patterns, element_per_pain`
     - leanings: `question, option, quotes, locations, condition, pattern`
     - element_per_pain: `pain, element, verdict`
     - existing: `account, incumbents`, with incumbents `system, authority, evidence`
     - assumptions: `statement, question`
     - unmet_needs: `need, clock, why_not_met`
     - ai_opportunities: `pain_or_need, kind, round, probe_basis, idea`
     - verdict: `cleared_for, conditions, reason`
     - questions: `text, kind, role, known`
   - `build_target` is `own-account`. Its reason is the brief's A21 prospect wording. The one workspace is "Aldergate – Ops", with the en dash, which fits a single Work Management product. `native_reuse` begins "none: no CRM or Service entity".
4. **Every key pain in `readiness.pains` and in `element_per_pain`.** Pass. The key has 6 pains. All 6 appear in the block as P1 to P6, in order, with quote and location equal to the key's. The two unnumbered key entries (crew grid, three states) became P5 and P6, and `changes.md` says so. `element_per_pain` has 6 rows, P1 to P6: four `fixes`, one `copies-today's-tool` (P4), one `none` (P5).
5. **`moves_independently` on every entity with a parent.** Pass. The block has 30 entities, 20 with a parent. All 20 carry `yes` or `no`. The remaining 10 carry the field too.
6. **At most five questions.** Pass. There are 5, three read-back and two discovery. Each carries a role and what is known. The three read-backs are backed by signals.
7. **Valid `cleared_for`.** Pass. The value is `build`. The conditions list the approval stop first and say no A11 question bites for an own-account target.
8. **No sales word in the block.** Pass. A search of the block text for R-numbers, "grade", "gate", "bleed", "upside", "rubric", "blueprint", "proceed", "Nearly ready" and "Not ready" found nothing. The only hits are the schema's own field name `verdict`, the word "excavated" as the schema's value, and "failed" and "ready" in ordinary quoted speech.
9. **Direction rename.** Pass. `intake.type_header.direction` is `no-show`. `direction_of_show` appears nowhere in the key, and the README names the rename.
10. **Never-written rule.** Pass. I searched key and README for "never written", "not written", "written to", "write back", "writeback", "never touched", "read only", "never touch", "nothing goes into", "goes back into", "untouched" and "never write". The key's own claims now read "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of it is our safe default, labelled as ours". This is the case in `purpose_of_this_fixture`, `expected_monday_products[0].why`, `integrations_mentioned[0]`, `expected_structures.notes` and the README's "The call". The client-backed requirements stay beside it with lines cited: L96, L97 and L207. I checked those lines. L96 is Eamon on invoicing running from the inventory system, and L207 is Constance on Lionel's question about replacement.
    - Left in place, correctly: `current_tools[1]` "never touched by hand" (Eamon's L96) and "invoicing is untouched" (the client's requirement).
    - "We never write anything back" (L182) and "Read only" (L179) now appear only as the speakers' own sentences.
    - The block's incumbent for the inventory system uses the same wording.
11. **FEEDBACK s23 entry, each change in the field it names.** Pass.
    - Item 1 (true share is author-only data):
      - `traps[1]` now reads "Report the by-label figure with a warning that shredding likely understates it, never a corrected figure; the true share is fixture ground truth ... which no grader expects as output".
      - `intake.shred.talk_share_true_note` was added after `talk_share_true_by_words`.
      - `quietest_speaker`, `accepted_behaviours[3]`, `attendees[4].role`, `transcript_format` and `confidence.propagation` follow the same reading.
      - The README's defect row, Measurements and Checks run say the same. The accepted 6.1 to 6.7 percent by label is unchanged.
    - Item 2 (pack checks version, not presence): states draft, issued, signed and approved. The checklist verifies the current issued or approved version, and a pack built early shows as outdated. This is in `expected_monday_products[0].why`, `vocabulary["pack, job pack"]`, `expected_structures.notes` and `lookalike_traps[6]`, and leaning 1 carries it with its condition.
    - Item 3 (crate availability): state, location and which job holds a crate for which dates, so a crate is never promised twice and an available one is not rebuilt. This is in `expected_monday_products[0].why`, `vocabulary["crate, travel frame"]`, `expected_structures.notes` and `lookalike_traps[4]`, and leaning 2 carries it. The crate number stays Margit's (L238).
    - The entry's own line references matched: key line 162 held the trap and the intake block sat near line 284.
12. **`verify_quotes.py` clean.** Pass. Exit 0: pairs 198, verified 198, presence-only 25, skipped 0, unparsed prose 0, near-misses 0, misses 0, unsupported 0, warnings 0. The 10 `refused_quotes` are the key's own refusals and are not checked. No location notes were reported. Baseline was 166 pairs. The 32 new pairs are 6 pains, 6 signals and 20 leaning quotes. All 69 locations in the block, covering pains, signals, leanings and the entity and incumbent evidence, match the stamp and label printed at their line.
13. **Outcome strings, outside the verifier's reach.** Pass. The three `outcome` strings are not under a key named "quote". I checked them by hand. P1 appears verbatim at L200, P2 at L202 and P3 at L201. P4 to P6 are `null`.
14. **Transcript edits inside existing units, unit count unchanged.** Pass. `transcript.txt` is untouched: its modification time is 20 September, before the pass, and `changes.md` section 7 gives the reasons for no mess pass. The verifier parses 264 units, and I counted 264 lines, 6,803 words, 168 words in the longest unit (L246), and ASCII only. The baseline row for s23 omits the "units parsed" column, because every row has one value too few for its header. So the baseline gives no unit count to compare against. The comparison rests on the unchanged file and on the key's pre-pass `transcript_format`, which already said 264 units on 264 lines.
15. **No quoted span changed.** Pass. The `--spans` output lists the same protected spans in the unchanged file. Because the transcript is untouched and the verifier reports zero misses, every span is intact.
16. **README counts true of the files.** Pass. I recounted from the key and transcript:
    - rubric rows 36 (27 met, 4 partial, 1 met-with-residual, 3 missing, 1 not-obtainable); `asked` true on 32, each with an `asked_quote`;
    - 6 pains; 8 objections; 28 traps; 15 leak entries;
    - requested changes 6 (2 add, 4 change, 0 remove); 7 look-alike traps;
    - 10 questions; 12 accepted behaviours; 15 vocabulary entries; 8 commitments;
    - 12 entities and workflows; 7 integrations; 7 compliance signals;
    - intake counts: 83 shred events, 13 re-joined sentences, 10 refused quotes, 5 question-answer pairs, 3 split numbers, 5 second-hand items;
    - 6,803 words; shares by label 30.5, 6.4, 20.8, 29.2 and 13.0; client share 63.09 percent;
    - 496 lines; 198 quote pairs, of which 25 are presence only (24 quote-only plus the account-context quote);
    - the readiness line (6 pains, 6 signals, 30 entities with 20 parented, 7 leanings, 3 patterns, 6 rows with 4, 1 and 1, 8 incumbents, 13 assumptions, 4 unmet needs, 5 AI, 5 questions with 3 and 2).

    Nothing in the README contradicts the files.
17. **`coverage-row.md` against the files.** Pass. It differs from the existing row only in quote strings (166 to 198, which is the verifier's pair count) and in the Review column ("reviewed 2026-10-13; fix pass applied 2026-10-13"). All other columns are true of the files: 36 (27 / 4 / 3 / 1 / 1), 4 (3), 8, 28 (7), 15, 6 (2 / 4 / 0). The COVERAGE.md row itself still reads 166 and "user review pending", as expected, because the merge step edits it.
18. **Thin-case note.** Not applicable. This is a strong-case key. `should_plugin_propose_a_build` is true and the block's `build` agrees with it, so the `note` correctly carries no extra sentence. `rubric`, `expected_verdict` and `numbers` were not changed. The comparison against `answer-key.before.json` shows changes in 11 top-level fields plus 3 `intake` sub-fields, plus the appended `readiness`, and none of the changed fields is one of the three untouched ones.

## Section 8

- **Old verdict fields:** untouched and consistent with the block.
- **Pain ids:** one id per key entry, with the unnumbered ones taking the next free numbers and logged.
- **`copies-today's-tool`:** P4 uses it honestly, with the dependency carried by leanings 4 and 6 and by questions 3 and 4.
- **Sweep with "no hit":** the alias-map pattern says no hit, names its nearest candidate and declines it. Pattern 7 produced two field corrections and no forced leaning, which is the rule.
- **Questions:** chosen by the build-element and signal test. The account question is correctly absent under A21.
- **Workspace name:** uses the en dash.
- **Verifier discipline:** the final run is pasted in `changes.md` and I reproduced it.

## Non-blocking observations

These do not change the status.

1. One `entities[].parent` value, "object on a job", resolves to no entity name. The object entity is named "object (as the inventory system lists it: one line per object per job)". This applies to three entities: the condition report, the condition-report request and the claim. The meaning is clear, but a tool matching parents by name would miss them. Pointing the three at the exact name would make the tree join up.
2. The README's defect table heading still says the quietest speaker's figure "is wrong by 2.7 points", and the shred's `side_balance` and `counting_rule` still say "in truth". Both are framed as fixture ground truth and are not presented as graded output, so they sit inside the intent of item 1.
3. The baseline table has no "units parsed" value in any row, so a later check cannot read s23's unit count from it.

PASS
