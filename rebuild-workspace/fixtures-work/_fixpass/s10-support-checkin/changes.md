# s10-support-checkin — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s10-support-checkin/answer-key.json` only. `transcript.txt` is unchanged (80 units, no edit asked for; the mess pass applies to s12 to s25). There is no README. The key was loaded, changed and dumped by script (`indent=2`, `ensure_ascii=False`, trailing newline) after a round trip without changes had reproduced the file byte for byte. The 25 fields keep their order; `readiness` is the 26th and last. The key is still ASCII, because no new workspace is named and so no en dash was needed. 717 lines before, 1,263 after (newline counts).

FEEDBACK.md has no entry for s10. It names s10 among the eleven keys for the "never written to" rule (s14 entry, item 2), so the material applied here is that rule, the cross-fixture sweep, the standing lines from s11, s15, s21 and s22, and the readiness block. Section 8 of the brief applies: the key says no build, and the block agrees with it for its own reasons (section 4 below).

## 1. The review entry

None. Nothing to apply.

## 2. The direction rename

Not applicable. The key has no `intake` field and `direction_of_show` does not appear anywhere in it (checked by search after the edit).

## 3. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit becomes a `readiness.structure.leanings` entry; a field is corrected only where a builder reading it alone would build the flaw.

1. **One row where the call describes many.** Two hits, both in the delivered build's own territory.
   - The consultant-fee need. An agreement per outside firm per job, several invoices under it arriving at their own times, some marked up and billed through (L56, L60, L62). One "remaining fee" number on a job row would copy today's afternoon of adding up PDFs. Leaning 1 states the parent-row-with-roll-up shape, for the conversation the Consultant committed to and for nothing else. No field corrected: `vocabulary["consultants / outside consultants"].likely_monday_object` says "none today" and is incomplete rather than wrong, so the leaning carries the shape.
   - The CDs phase and its two milestones. The reported issue is this pattern read the wrong way round: the build correctly carries one item per milestone, and Jordan read the phase as one line (L16, L20). Leaning 3 says no change to the build; the fix is the two names, which is the client's own housekeeping. Recorded under `patterns` as already applied in the delivered build, with the pursuit-and-addenda shape beside it (L46).
2. **A pain with no element that fixes it.** One hit covering the six P6 entries. Nothing in the delivered build or in anything cleared by this record answers them, and that is by design: the client calls the approving fine and the whole thing not urgent (L62, L64), and the Consultant committed to a conversation before any build (L63, L65). Leaning 2 holds the question of whether anything is built at all; every P6 row in `element_per_pain` reads `none`, which stays visible as the finding it is.
3. **An alias-map entry that names more than one entity.** No hit. The key has no alias map. The nearest candidates are the glossary pointer `vocabulary["owner, PIC, PM, pursuit, phase, CA, the Wall"]`, which lists seven carried terms and defines none of them as an entity record, and the "People named on this call" entry in `entities_and_workflows`, which is a list. Nothing split.
4. **Our framing labelled as the client's.** Two hits, both small, both corrected.
   - Fenwick's discipline. The transcript says only "how much of Fenwick's fee was left on the fire station" (L58); "civil" was our inference written as fact in `vocabulary["Fenwick"].meaning` and in `entities_and_workflows[12]`. Both now say the discipline is not stated, and `assumptions` carries it with its question. This is also the s11 line: inference targets questions and never fills evidence.
   - "The PIC, PM and marketing all notified" in `entities_and_workflows[5]`. Jordan says the PIC and the PM had it in their notifications before lunch (L46); marketing is the person who logged it, and that the automation also notifies her is our design, not his report. Corrected to say which is which.
   - Checked and left: "Tess's two-week view" (the Consultant's phrase at L47, which the client confirms at L48); "Karen's test" (the Consultant's words at L41, not used as the client's); "in daily use" for the Submittals log in `expected_monday_products[1].why`, where the client says "Karen uses it" and describes her filtering (L42) and "daily" is ours, left because it is a description of adoption and not a list, requirement or structure.
5. **A shared resource with no reservation tracking.** No hit. People across four offices are the shared resource, and the delivered Staff allocation board with its workload view is their reservation tracking (the pattern's "who holds it when" already exists). Outside consulting firms were considered: they are reused across jobs (L60) but engaged per job under their own agreement, and nothing on the call books their time or promises them twice, so inventing a booking for them would be our framing. Their `shared_resource` is false, with this reason.
6. **An artefact that can go stale with nothing to flag it.** One hit as a leaning, two carried in `entities`.
   - Des Moines allocation rows before the January hire decision (L69 to L72). Nothing in the record shows a row's age. Leaning 4 proposes a last-updated stamp or a stale-rows view, labelled as ours and not built from this call; the condition is whether the four PMs keep their rows current through December.
   - What is left of a consultant's fee (goes stale with every emailed PDF) is leaning 1's roll-up; the SOP billing section and the weekly Ajera import carry `goes_stale: true` in `entities` and an assumption asks whether the import date is shown. No leaning of their own, because nothing changes on this call.
   - Considered and declined: a flag for two same-named milestone items. That would be a build change the Consultant said is not needed (L25, L27); leaning 3 holds the naming convention instead.
7. **An expected output the input cannot support.** No hit. The `transcript_format` statistics were recounted and are all true: 80 units, 1,834 spoken words, about 1,954 with labels, 40 turns each, client share 62.9 percent, the Consultant's longest turn 56 words at L69, Jordan's 69 words at L58. The call date is held as unstated and the check-in window is labelled as arithmetic on the client's pattern. The null `numbers` quotes stay null.

## 4. The "never written to" rule

s10 is one of the eleven keys. Searched for "never written", "written to", "written back", "write back", "write-back", "writeback", "never touch", "not written", "writes back", "writing back", "read-only", "one direction" and "one-way": 25 occurrences in 12 places outside `rubric`.

Every one traces to a client quote, so none was reworded into the unresolved form. The current-state claim (the live import is one direction and nothing writes back) is Jordan's own report at L50: "Marcus asks me about once a fortnight whether anything writes back the other way and I tell him no, same as last time." The rule itself is the controller's, a client speaker, in the s3 transcript at 00:14:44: "And that nothing, ever, writes back into Ajera. It's one direction, Ajera to this." The key's convention for this client is cumulative, with carried evidence cited by s1 or s3 timestamp, so that is the trace used.

What was missing was the trace itself in the five places that state the rule for the consultant-fee need as if it were self-evident. Each now carries, once, "(the controller's condition, s3 00:14:44: 'nothing, ever, writes back into Ajera'; confirmed in live use at L50)" and a clause that what would be read from Ajera for the need, and how often, is unresolved: `integrations_mentioned[0]`, `compliance_or_security_signals[1]`, `traps[15]`, `accepted_behaviours[10]` and `expected_structures.notes`. The s3 quote appears only inside prose fields, never in a structured `quote` field, so the verifier does not look for it in this fixture's files. Left as they are, because they describe the current state and already cite or rest on L50: `company.current_tools[1]`, `entities_and_workflows[9]`, `account_context.existing_monday_setup`, the R1 and R9 notes (rubric, untouched), and `expected_questions_before_building[8]`, which is a question and so the right shape. The readiness block's Ajera incumbent line states the client's condition with its source, says the read side is unresolved and nothing from this call depends on it, and labels staying clear of Ajera as our safe default.

## 5. Standing lines, where they bite

- **s21 (a commitment is `committed`; done only on evidence).** Bites once. `entities_and_workflows[3]` said "Jordan renames the rows himself on every job in CA", which reads as done. Now: "Jordan commits to renaming the rows himself on every job in CA that afternoon (committed on the call, done only on evidence)". The six `commitments_and_next_steps` entries already carry owner, purpose and a date or "not set", and none claims delivery; the invite is "find a slot and send it over" and stays an open to-do, which the block's verdict conditions repeat. No `status` field was added, since that would change the s1 to s10 shape, which this pass does not do.
- **s22 (a board status set by a person is a claim).** Bites on the milestone status. An "invoiced" status with an Ajera invoice number is the controller's entry, and the number is the tie-out; it is never confirmation from Ajera. Recorded as an assumption with its question rather than as a field correction, because no field claims otherwise. Allocation rows kept current by a PM are the same kind of claim; leaning 4 says the January reading should carry its age.
- **s11 (inference targets questions, never fills evidence).** Five unconfirmed client ties are in `signals`, three of them drive read-back questions, and none appears as evidence or in an element. The Fenwick correction in section 3 is this line applied to an existing field.
- **s15 (a product limit never deletes a client need).** Nothing deleted. The cross-office view (the client's "portfolio thing") is out by the client's own scoping decision, not by a product limit, and stays in `unmet_needs` with the reason; the consultant-fee need and the staffing-data need are there too.

## 6. The readiness block

Built in the brief's exact shape from the key's own content.

- `pains`: the key's seven entries in array order, same quotes and locations. The six P6 entries are numbered P6.1 to P6.6 so each quote keeps its own element row. The seventh entry, which the key itself labels "Not a pain" (Jordan's expectation at L16), is carried as P7, the next free number, so every entry of the key is present; the `note` says so. All `stated`. `outcome` is "Knowing what's left." (L62) for P6.1, P6.2, P6.3 and P6.5; null for P6.4 (the client says the approving works) and P6.6 (no outcome words aim at it); for P7 the first sentence of his own expectation.
- `signals`: five. The controller's close habit as relayed (L36), the managing partner's question (L58), the IT provider's fortnightly check (L50), the agreements starting at the pursuit (L60), the COO's portfolio enquiry (L66).
- `entities`: twenty, fourteen with a parent, each with `moves_independently`. The delivered build's entities (owner, pursuit, addendum, form, view, job, phase, milestone item, import, person, allocation row, Des Moines group, submittal, close) and the need's (firm, agreement, invoice, what is left, markup, SOP). The allocation row is `documented` with null evidence because it comes from `account_context`, not from a line on this call.
- `structure`: Work Management and CRM, both live. `build_target` is `client-account`, reason "existing customer with a live account of their own (A21)": the account is Enterprise, paid and in daily use (L52; `account_context`), so the A21 default for prospects does not apply. `workspaces` names the one delivered workspace as continued under A21, since the record does not give its name and no new workspace is planned. Four leanings, three patterns (two in the delivered build, one for leaning 1 only), seven `element_per_pain` rows (six `none`, one `fixes`).
- `existing`: the live account as `account_context` describes it, and five incumbents with what each stays the record for.
- `assumptions`: ten, each with the question that would replace it, including the ones that fell out of the five questions.
- `unmet_needs`: three, with clocks where the client gave one.
- `ai_opportunities`: three, all round 2 (the client never asked for AI or workflows) and all `unprobed`.
- `verdict`: `none`. Reason: the only new pain is the consultant-fee need, which the client set aside as not urgent and whose shape is wholly open; our side committed on the call to a conversation before any build; the delivered build in the client's live account is confirmed in use and needs no change. Six conditions, starting with the approval stop and the A11-2 point for a client-account target, which is not asked now because nothing is built; the three A11 decisions stay open.
- `questions`: five, for the conversation the client asks for (L65), not for this call's recap. Q1, Q3 and Q4 are read-backs of L62 and L64, L60 and L50; Q2 and Q5 are discovery. Reused from the key's pool: items 2, 5, 6 and 7 in Q1 to Q3, item 9 in Q4, item 10 in Q5. Dropped from the pool for the block: reach and frequency (item 3) and trajectory (item 4), which decide a cost and a why-now rather than a build element and are v2 material; approval in monday or email (item 8), an assumption; the pursuit angle (item 11), folded into Q3; priority against the other open items and a date (item 12), a timing question with no element behind it.

No R-number, grade, gate name, verdict word or figure is in the block; the script searched for them before writing. `rubric`, `expected_verdict`, `numbers`, `should_plugin_propose_a_build` and `requested_changes` are byte for byte as they were.

**Judgment call, for the planner.** By the brief's letter P6 has a named entity and an outcome in the client's words, the product would be Work Management and the target is named, so a reading of `build-generic` is possible. I chose `none` because the task allows it for a support check-in and because three things on the record say so: the client set the need aside ("It isn't urgent", L64) and called the current approving fine (L62); the Consultant committed to a conversation before building (L65), which a cleared build would break (the s21 line in reverse); and the target is a live client account where nothing changes without the change check and the A11-2 question. The key's `should_plugin_propose_a_build: false` therefore agrees with the block, so the section 8 disagreement sentence was not needed and the note says instead why the two agree. If the planner prefers `build-generic` for every key with a stated pain, the block's leanings and assumptions already carry the shape, and only `verdict` would change.

## 7. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 7 (P6.1 to P6.6, P7) |
| signals | 5 |
| entities | 20 (14 with a parent, all with `moves_independently`) |
| leanings | 4 |
| element_per_pain | 7 (6 `none`, 1 `fixes`) |
| incumbents | 5 |
| assumptions | 10 |
| unmet needs | 3 |
| AI opportunities | 3 |
| existing fields corrected | 9 (`vocabulary` Fenwick; `entities_and_workflows` 3, 5, 12; `integrations_mentioned` 0; `compliance_or_security_signals` 1; `traps` 15; `accepted_behaviours` 10; `expected_structures.notes`) |
| transcript edits | 0 |
| key size | 1,263 lines, from 717 (newline counts); 26 top-level fields |

Counts COVERAGE tracks for s10 that did not move: traps 21, pains 7, vocabulary 15, expected questions 12, entities_and_workflows 13, commitments 6, requested changes 0/0/0, transcript 80 lines and about 1,834 spoken words. The quote count moved: the verifier finds 82 pairs now (61 before), the new block's 21 structured quotes.

## 8. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s10-support-checkin`, run after the last edit, exit code 0:

```
Fixture: s10-support-checkin
Sources: transcript.txt (transcript/line-plain, 80 units)

pairs found      82
verified         82  (of which presence only, no location cited: 9)
skipped          2  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes. The build script also proved each of the 23 quote strings the block introduces (21 distinct spans; two reused) verbatim at its cited line before the file was written, and asserted that the seven `pains` quotes and locations equal the key's own.
