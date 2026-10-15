# s15-shred-dense (calibration fixture, C58b)

The high-density twin of s14. One first-hand discovery call with a food and water testing laboratory, exported by a tool that starts a new unit at every pause and hands out a fresh label shape as it does so. The file is dishonestly tidy: no ellipsis, no end times, no header, no two adjacent units with the same label string, and a third of the units under five words. Fictional client, fictional people, fictional figures; everything in it is invented. It guards reversal R8, gate the habits and not the repairs.

## Files

| File | What it is |
|---|---|
| `transcript.txt` | Plain text block export, 487 lines, one unit per line as `M:SS Label: text`, start-only stamps from 0:02 to 33:36. About 4,800 spoken words; client share about 65 percent by words after the small talk is dropped. |
| `answer-key.json` | The 25 fields in the s1 to s10 order, plus an `intake` block and, since the fix pass, a `readiness` block (`readiness/1`) as the last field. 546 lines. |

Give the plugin `transcript.txt` and compare with `answer-key.json`. Locations are `L<n>, M:SS, <label exactly as printed>` for one unit and `L<a>-<b>, M:SS, <person> (merged run)` for a run of adjacent units by one person under any label shapes, whose quote is the unit texts joined by one space.

## What is planted, and what the key asserts

| Plant | Where | What the key asserts |
|---|---|---|
| Four label shapes for five people, 18 label strings | throughout (`Tamsin Greaves`, `Greaves, Tamsin`, `TAMSIN GREAVES`, `Tamsin`; same for the other three; `Consultant` and `CONSULTANT`) | One roster of five; the alias table proposed once; casing, the comma and the presence of a surname carry no identity signal. |
| Zero adjacent same-label pairs | throughout | A flag needing a second signal, never proof: after alias resolution 188 of 486 adjacent pairs are the same person, so the exporter assigned a fresh shape at every pause. Labels are not voided; same-person units merge into turns for talk share. |
| Split numbers with no ellipsis anywhere | L41-42 (`It's about 2` / `thousand a week`), L304-305 (`Thirty` / `two an hour, loaded.`), L298-299, L129-130, L309-310; one across two speakers at L190-191 | The split-number repair runs, not gated on family (R8); the joined figure carries the lower confidence; the cross-speaker 420 is never one quote and is cited whole from L193. |
| Hesitation as full stops mid-clause | L64, L128, L190, L314, L325 (`fifty-four. thousand`), L382 (`under. ten thousand`), L3-4, L7-8 | The ellipsis reading does not run; no step treats a full stop as a sentence boundary, or the bleed total and the budget threshold are lost. |
| Our side narrating hypotheticals with the participants' names | L148 (a spoken story, no screen); L355-373 (a sketch over a shared screen, including `Oisin's moved on`) | The names and events are seed data positionally and quarantined; nothing becomes a record fact; the client's answers and reactions around them stay evidence. |
| Our side completing client sentences | L102-103, L251-252 | The completion is not evidence; each fact counts through the client's own later line. |
| A vocative answered by someone else | L182 (`Oisin.` answered by Tamsin), L303 | The vocative names the addressee, never the next label. |
| Small talk that re-identifies | L10-15 | Dropped at intake, never in the record. |
| A deliberately incomplete key | `intake.key_completeness`; the six P2 rubric rows carry no `asked` flag | Lists are lower bounds; a run that finds more is not wrong; a grader that requires exhaustiveness or the flag on every row fails by design. |

## Counts for the COVERAGE.md row

- Rubric rows: 24. By status: 18 met, 2 partial (R12, P2 Trajectory), 1 missing (R11), 2 met-with-residual (R4, P1 Cost inputs), 1 not-obtainable (R5). `asked`: 17 true with an `asked_quote`, 1 false (R11), 6 absent on purpose (the P2 rows).
- Graded pains: 2 (P1 status chasing, P2 on-hold samples), both excavated. `pains` array: 13 entries (P3, the retail turnaround report, is folded into P1 at the client's own word and not graded per check).
- Numbers: bleed met-with-residual, the client's own "fifty-four thousand a year" in pounds (exact 53,904) with the lab time effort-quantified and rate pending; upside not-obtainable from this room, routed to the absent MD.
- Objections: 8. By spec name: Must check with someone 2, Just send a proposal or pricing 1, Team won't adopt it 1, Wrong time, next quarter 1, We'll build it ourselves 1, Talking to other partners 1, Outside the map 1.
- Traps: 30. Look-alike traps: 6. Leak block list: 16 entries, including one "flag, do not remove" group and one seed-data caution.
- Requested changes: 1 add, 4 change, 0 remove (pre-build requirements; no build exists).
- Commitments: 10. Pre-build questions: 10. Vocabulary: 17. Accepted behaviours: 16.
- Quotes: 209 checked strings, 179 with a location and 30 quote-only (29 `quote` fields plus `account_context.evidence_quote_or_null`); every one verified verbatim against its cited line or merged run (`verify_quotes.py`, 2026-10-13: 209 verified, no miss, no near-miss). The 43 added since the adversarial review are the readiness block's: its 13 pains reuse the key's own quotes and locations, and its signals and leanings cite 30 further client lines.
- Readiness block (`readiness/1`, added in the fix pass of 2026-10-13): 13 pains (P1.1 to P1.6, P2.1 to P2.5, P3.1, P3.2; the key's 13 entries numbered by theme in array order), 5 unconfirmed signals, 23 entities, each with its parent (or none) and a `moves_independently` answer, 10 leanings (one per sweep hit or review item), 13 element-per-pain rows (9 fixes, 2 copies-today's-tool, 2 none), 8 incumbents, 14 assumptions, 4 unmet needs (customer visibility first, with the February renewal as its clock), 4 AI opportunities (all round 2), 5 questions (2 read-backs, 3 discovery); cleared for `build`; build target `own-account`, one workspace, Work Management only.
- Verdict: Discovery complete. Gates: Solution blueprint met, Build met, First demo (v0.1) met, Pricing or proposal prep not met, v1.0 sign-off not met. `should_plugin_propose_a_build` true.
- Products: Work Management only. Native boards required: none. `portfolio_expected` false (no account, tier never stated). One lapsed free trial board, nothing in it.
- Intake block: 1 file, block family, 487 units, 18 label strings in 4 shapes resolving to 5 people (5 alias entries); 0 adjacent same-label pairs and 188 same-person adjacencies; 156 units under five words (32 percent); 9 split or stop-broken figures; 8 hesitation stops; 14 re-joined runs listed; 7 question-answer pairs kept; 2 quarantine spans and 2 client hypotheticals not quarantined; 4 vocative bindings; 4 second-hand items; 4 withheld or unpriced items; 1 duplicate unit; 0 composite blocks; wedges not applicable (no end times); type header `discovery` with 3 segments and 5 signals; 3 delivery notes.

## Conventions and deviations worth knowing

- The key uses two of the calibration statuses, `met-with-residual` (R4 and one per-pain row) and `not-obtainable`, and the per-criterion `asked` flag. It does not exercise `advisory`, because the type resolves cleanly.
- The `asked` flag is absent from the six P2 rows on purpose, so a grader can be checked for grading a row on status alone (WP14).
- Every list entry is printed on one line, which kept the key under the 400-line writing budget before the fix pass; the `readiness` block follows the same style (its `structure`, `existing` and `verdict` objects are printed open one level deeper so that each leaning and each element row sits on its own line) and takes the file to 546 lines; the intake sub-objects are flat lists at `intake` level (`type_segments`, `type_signals`, `alias_map`, `quarantine_spans`) rather than nested.
- The call type header carries the tokens `shared/record-map.md` pins (the ARCHITECTURE.md 8.3 step 5 values in their hyphenated form, with the reasoning in a `_note` beside each field) and the label list of 7.1 verbatim, and records a mid-call segment change (a two-minute `we-show` segment inside a call whose direction is `no-show`).
- Tool references are category words, at most one category per sentence, in the transcript and the key alike: the lab system, a spreadsheet, the shared inbox, the phone system, text messages. The product is named once, lowercase, as a lapsed trial.
- Currency is pounds, said once; the setting is the north of England; no timezone is stated. Dates are relative and stay so: the walkthrough is Thursday the 17th, 14:00, month unstated, because no transcript states its own date and a weekday with a day of the month does not fix a month (the fix pass removed an earlier pin to a month).
- Real place names (Normanton, Wakefield, Carlisle) are used on purpose, as in s1 to s10. The retail account is deliberately unnamed by the client and stays unnamed everywhere.
- `Dara Vasseur` replaced an earlier surname that collided with an s20 attendee; person and organisation names are unique across unrelated fixtures.
- Speech artefacts are left as spoken and not enumerated in the key: stutters and restarts (L31, L61, L81, L245, L265), one `[inaudible]` token at L393 on the line whose speaker said his sound was crackly, and one recognition slip at L428 (`there roadmap`). A run that flags them is right; a run that invents a word or a speaker for them is wrong. None of them touches a cited line.

## Review status

Written to its row in BUILD-PLAN.md section 4.2 and to C58b in REAL-CALL-LESSONS.md section 6, and to nothing else. One adversarial review pass on 2026-09-20 re-verified all 166 quotes at their locations, re-measured every count in the intake block, corrected four key notes (a presence remark, a speaker attribution in P1 Cost inputs, the R3 note on L64, the direction header wording) and added the speech artefacts above. Reviewed by the user on 2026-10-11 (FEEDBACK.md, s15 entry: keep, with four changes), and the fix pass applied 2026-10-13: the four review changes (customer visibility out of the first version by the client's choice and kept open as the need that closes the audit finding with the February renewal as its clock; site and discipline wanted with their source open until the export is inspected; the three automations as candidates to confirm; the walkthrough date kept relative), the `direction` rename in the intake header, the seven-pattern sweep (ten leanings), the never-written rule on the lab system, the standing lines, the `readiness` block, and these counts; transcript untouched; `COVERAGE.md` row re-stated in `fixtures-work/_fixpass/s15-shred-dense/coverage-row.md`.

At stage-1 acceptance (2026-09-20) the type-header values in `answer-key.json` were re-spelled as the tokens `shared/record-map.md` pins, with each value's prose moved to a `_note` field beside it; no quote, location, grade or count changed.
