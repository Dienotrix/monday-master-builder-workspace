# s1-discovery-strong — fix pass changes (exemplar for the strong case)

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s1-discovery-strong/answer-key.json` only. `transcript.txt` is unchanged (242 units, no edit asked for). There is no README. The key was loaded, changed and dumped with its existing two-space indentation; a round-trip of the untouched file reproduced it byte for byte before any change, so the diff outside the new block is five fields and nothing else. The 25 fields keep their order; `readiness` is the 26th and last.

FEEDBACK.md has no entry for s1 (its fixture entries cover s11 to s25), so the only FEEDBACK material applied here is the cross-fixture sweep, the fix-pass rule from s14 and the standing lines from s11, s21 and s22.

## 1. The seven-pattern sweep over the key

Each hit became a `readiness.structure.leanings` entry. Where the hit sat in an existing field and that field was wrong, the field was corrected too; where the field was merely incomplete, the leaning carries it and the field stands (see "What the exemplar teaches", third call).

**One row where the call describes many.** Two hits.
- Staffing allocations. `vocabulary["allocations / percentages"].likely_monday_object` read "number column (percent) feeding the workload view": one percent per person is the Wall's cell, the place where Ravi's three bookings hid ("He was on the Wall at a hundred percent on the Oak Street fire station CDs. But two other PMs had also, separately, told him he was on their jobs.", 00:14:56). Corrected to allocation rows (person, job, week range, percent) rolled up per person per week. Leaning 1; settling condition is Jordan's copy of the Wall due the 15th and the PMs' willingness to enter per-job rows.
- Project, job and phase. The key already carries the two client constraints (several jobs per project; phase sets vary) in `traps` and `requested_changes`, but the vocabulary leaves phases as "subitems, or items on a connected Phases board" and nothing says what rolls up. Leaning 2 states the parent-row-with-roll-up shape (phases under jobs, jobs under projects, burn rolling up) with the burn level and the tier as its conditions. No field corrected: nothing there was wrong.

**A pain with no element that fixes it.** Three hits, all kept visible as `none` in `element_per_pain`.
- Fee builder rates out of date (P1.5, 00:06:43). Nothing in the build touches the rate table, which is confidential to Bev, Tess and the partners. Leaning 5.
- Owner approvals not tracked (P4.3, 00:23:33). Held for a second pass by agreement on the call. Leaning 9, and an entry in `unmet_needs`.
- The won pursuit retyped into Ajera (P5.1, 00:32:10). Direction unresolved; Bev keys it as today. Leaning 10, and an entry in `unmet_needs`.

**An alias-map entry that names more than one entity.** No hit. s1 has no alias map. The nearest candidates are glossary entries that pair a term with its derivative ("studio / studio leads", "burn / burn sheet", "fee builder / hours sheet"); each pairs one thing with its name variant or its tool, not two people, places or organisations, so they stand.

**Our framing labelled as the client's.** One soft hit. "RFQ" is the Consultant's word ("an RFQ lands on a Monday", 00:08:47); the client says "The RFP comes out" (00:05:45) and never repeats RFQ. The vocabulary entry already records this, but `entities_and_workflows[0]` ("Pursuit intake: RFQs and RFPs...") and the CRM `why` ("RFQ/RFP intake") presented it as the client's distinction. Both corrected to say whose word it is. Leaning 8 leans to a single source field (bid portal or PIC relationship), which the client did describe. Also checked and left: the October 1 framing (the R3 note already labels it the Consultant's), "Outlook" (already labelled), and the four-item first cut (Tess confirmed it out loud and added submittals, so it is the client's).

**A shared resource with no reservation tracking.** Two hits, one of them shared with pattern 1.
- People across jobs and offices: the allocation rows of leaning 1 are the reservation; the workload roll-up is what shows a double booking before Tuesday.
- Reviewers on submittals ("he was out sick for a week, and nobody reassigned it", 00:22:55). Leaning 6: reviewer, received date, due date from the contract window, a view of unassigned or past-due submittals; who covers for an absent reviewer was never discussed and is the condition.

**An artefact that can go stale with nothing to flag it.** Three hits.
- The pursuit's due date after an addendum ("Hallie's spreadsheet is a list, it doesn't know about addenda.", 00:08:23). Leaning 3: addenda as child rows, the parent's due date the latest one and showing which addendum set it.
- The fee sign-off after a rebuilt fee (00:06:43, 00:07:23). Leaning 4: sign-off tied to amount and file, reset on change.
- Hours and burn ("Some PMs are great, they export their hours from Ajera into their own burn sheet every week. Half of them don't.", 00:18:32). Leaning 7: an as-of date and source on hours; in v0.1 every hour is a sample value and the demo says so.

**An expected output the input cannot support.** No hit. Checked: the exact bleed ($504,920 is arithmetic on client inputs and the key says the client spoke "five hundred and four thousand"); the dates (every absolute date is labelled inferred from the weekday pairs and the October 1 meeting); the transcript statistics in `transcript_format` (recounted: 242 units, 5,734 spoken words against "about 5,730", the Consultant's longest turn 89 words at 00:40:02, all true); account facts (the key says unknown where the call is silent).

## 2. The "never written to" rule

s1 is not among the eleven keys FEEDBACK lists, and a search for "written to", "write back", "never touched", "read-only" and "one way" finds no no-write claim. One occurrence of the weaker form was found and reworded:
- `vocabulary["book of record"].likely_monday_object` read "none (integration rule: Ajera stays the source)". "Stays the source" is our rule resting only on the book-of-record line. Now: "none. Ajera stays the book of record for anything with a dollar sign (the client's words); writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of Ajera is our safe default, labelled as ours".

Checked and left, because each traces to a client quote: "Time entry stays in Ajera" (Jordan, 00:32:36: "Time entry stays in Ajera. The PMs are not entering time in two places.") in `expected_monday_products`, `integrations_mentioned`, `compliance_or_security_signals`, `traps` and `expected_structures.notes`; "Ajera is the book of record for anything with a dollar sign" (Tess, 00:32:55). "Should data flow one way into monday" in `expected_questions_before_building` is a question, which is the right shape. The readiness block's `existing.incumbents` entry for Ajera carries the same unresolved wording, and leaning 10 labels staying clear of Ajera as our default.

## 3. Standing lines where they bite

- **s21 (a commitment is `committed`, done only on evidence).** `commitments_and_next_steps[0].what` said the walkthrough was "with Tess, Jordan and Gordon (invited, attendance to be confirmed)". On the call nothing was sent: the Consultant will send the invite today, Tess will forward it and confirm by Friday the 18th. Now: "Committed on the call: first-version walkthrough with Tess and Jordan, Gordon to be invited by Tess (attendance to be confirmed by Friday the 18th)... Nothing is sent or confirmed yet." The same state is a verdict condition in the block. The R7 and R10 notes use similar wording ("he is invited to the next meeting") but sit in `rubric`, which the brief keeps untouched as v2 material; noted for the v2 pass. No `status` field was added to the commitments array, since that would change the shared s1 to s10 shape, which this pass does not do.
- **s22 (a board status set by a person is a claim).** Bites on burn and on returned submittals. Leaning 7 and `assumptions` say every hours figure in v0.1 is a sample value keyed by us and no figure on a board is Ajera's; leaning 6 and `element_per_pain` P4.1 say the returned status is a PM's claim and the stamped Bluebeam file is the evidence; leaning 9 says the same for owner approvals and the signed letter. The fee sign-off itself happens in monday under this design, so there it is the event, not a claim about another system.
- **s11 (inference targets questions, never fills evidence).** Four unconfirmed client ties are in `signals` and drive three of the five questions as read-backs; none appears as evidence or in an element.
- **s15 (a product limit never deletes a client need).** Microsoft single sign-on and named-person access on justice jobs cannot be shown in a proof of concept in the user's own account; both stay in `unmet_needs` with the reason.

## 4. The readiness block

Built from the key's own content in the brief's exact shape. Counts: pains 19 (the key's 19 entries, same quotes and locations, numbered P1.1 to P4.3 plus P5.1), signals 4, entities 24, leanings 10, element_per_pain 19 (one per pain id; three `none`, one `copies-today's-tool`), assumptions 10, unmet_needs 7, ai_opportunities 5 (all round 2: the client never asked for AI or workflows; all `unprobed`), questions 5 (three read-backs, two discovery), verdict `build`.

Build target: `own-account`, reason "prospect, so the user's own account by default (A21)": the firm has no usable account (one lapsed free board), Gordon has not been heard, and nothing has been bought, so it is a prospect in every sense. Workspaces "Brackenholt – CRM" and "Brackenholt – Ops", named for the fictional client with the brief's en dash (the key was ASCII-only before; it is UTF-8 now, which the brief allows). Products CRM and Work Management; native reuse is the Deals board relabelled Pursuits and the Accounts board for owners, Contacts, Leads and Activities only if asked.

A note on the key's existing account question ("Should the build go in a new monday account or the one behind Anneke's old board..."): under A21 the proof of concept does not need it, so it is not among the five questions and `existing.account` says it moves to handover. The key's own list of twelve questions is left as it is; the question still stands for the client's eventual account.

Verdict conditions list the approval stop first and say that no A11 question first matters for an own-account build (A21: sample data in the user's own account needs no decision); the three A11 decisions stay open. `rubric`, `expected_verdict` and `numbers` are untouched. No R-number, grade, gate name or verdict word is in the block (the script searched for them before writing).

## 5. Coverage row

`coverage-row.md` holds the row. The first table of COVERAGE.md has three columns and no counts, so the row is unchanged in form and content. No count that COVERAGE tracks for s1 moved: traps 33, pains 19, vocabulary 37, expected questions 12, entities_and_workflows 17, commitments 12, transcript 242 units. The key has 26 top-level fields now.

## 6. Verifier output

`python3 -I verify_quotes.py fixtures/s1-discovery-strong`, run after all edits, exit code 0:

```
Fixture: s1-discovery-strong
Sources: transcript.txt (transcript/line-bracket, 242 units)

pairs found      218
verified         218  (of which presence only, no location cited: 25)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

An independent check inside the build script also tested every quote the block introduces against the transcript line at its timestamp before writing (193 structured quote-location pairs across the whole key, zero misses).

## What the exemplar teaches

Three judgment calls other editors will meet.

1. **Pain ids when the key has more quotes than pains.** The s1 key holds 19 pain entries under four themes plus one unnumbered "minor" one. The brief says `id` follows the key's P-numbering and the verifier wants every pain of the key in `pains` and in `element_per_pain`. I kept all 19 entries and numbered them P1.1 to P4.3, so each quote keeps its own id and its own element, and gave the unnumbered retyping pain P5.1 as the next free number, saying so. The alternative, one entry per theme, would have dropped quotes the key already verified and hidden the two P1 sub-pains that have no element. Decide this the same way: one id per key entry, theme number first, running number after the dot.

2. **"copies-today's-tool" is an honest verdict, not an insult to the structure.** P3.3 ("the PMs aren't wrong, it's busywork") is fixed by burn rolling up from Ajera hours. In v0.1 the hours are sample values keyed by us, so until a feed exists the burn element is a burn sheet in monday, which is what the PMs refused to keep. I marked it `copies-today's-tool` and let the leaning and the Ajera question carry the dependency. Where a structure only fixes the pain once an integration exists, say so in the verdict rather than crediting the fix in advance; the approval card then shows the user what the first version really proves.

3. **When a sweep hit corrects the existing field and when it only becomes a leaning.** The brief says a hit in an existing field is corrected too. I corrected fields that were wrong (one percent per person; "Ajera stays the source"; RFQ as the client's word; Gordon "invited") and left fields that were only incomplete (burn as "formula column and dashboard widget", fee sign-off as "status column with an approver"), where the leaning adds the as-of date or the reset without the vocabulary entry being false. The test: would a builder reading the field alone build the flaw? If yes, correct it and point at the leaning; if the field is merely silent, the leaning is enough and the diff stays small. Either way the change is logged by field.
