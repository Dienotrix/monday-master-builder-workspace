# s3-followup-demo-feedback — fix pass changes

Editor's log, 2026-10-13. Everything in this fixture is fictional and stays fictional.

Files touched: `fixtures/s3-followup-demo-feedback/answer-key.json` only. `transcript.txt` is unchanged (187 units; no FEEDBACK entry asks for an edit, and the mess pass of the s11 rule applies to s12 to s25). `context-v0.1.md` is not edited, as the task set; the readiness block reads it as what exists. There is no README for s3, so there is no README to bring in line and no review-history line to write.

Method: the key was loaded, changed and dumped by script (`indent=2`, `ensure_ascii=False`, trailing newline) after a round trip without changes had reproduced the file byte for byte. The 25 fields keep their order; `readiness` is the 26th and last. A JSON-level diff of the file before and after shows one change outside the new block, in `entities_and_workflows[12]` (section 3, the fork). Every quote the block introduces was copied from the transcript and proven verbatim at its cited unit inside the script before the file was written (51 proofs); the shared verifier then found 183 pairs, 41 more than the 142 it found before the edit (17 pain quotes reused, 7 signals, 17 leaning quotes), with no miss, near-miss or location note. The key held no en dash before and holds none now, because the workspace keeps the name v0.1 gave it (section 6), so the file is still ASCII.

## 1. The fixture's own FEEDBACK entry

None. FEEDBACK.md has no entry for s3; its fixture entries cover s11 to s25. s3 is named once, in the s14 entry, as one of the eleven keys the "never written to" rule reaches (section 4). So the material applied here is the cross-fixture sweep, the fix-pass rule from s14, and the standing lines from s11, s21, s22 and s15.

## 2. The `direction` rename

Does not apply. s3 is an s1-to-s10 key with no `intake` field, and a search for `direction_of_show` finds nothing.

## 3. The seven-pattern sweep

Each pattern was checked against the transcript, the key and `context-v0.1.md`. A hit becomes a `readiness.structure.leanings` entry; a field is corrected only where a builder reading it alone would build the flaw (brief, section 8).

**One row where the call describes many.** Two hits.
- Milestones under a phase. "And some phases have two milestones. CDs sometimes bill at the fifty percent set and again at the hundred percent set. So it's not always one per phase." (00:20:21 Bev) and "And complete does not mean billed." (00:16:50 Bev). One phase row with a billing status would carry one value for two milestones and would mix work state with billing state. Leaning 1: milestones as child rows of the phase, billed-to-date and next milestone rolled up, phase status for work state only, billing type on the job and mirrored down (Bev's words are "a milestone job"; the Consultant's playback put it on each phase). No field corrected: the key's trap, `requested_changes` (the "not always one per phase" entry) and the vocabulary entry for "milestone" already say subitems or a connected board, and the "job or phase level to confirm" label is already there.
- Submittal revisions. The four stamp actions include "revise and resubmit" (00:22:15 Jordan), so one submittal cycles; one row with one action column would overwrite the first stamp when the GC resubmits. Leaning 2: one row per submittal with revisions as child rows or a revision number, the latest action and ball in court on the parent. No field corrected: the Submittals log entry in `requested_changes` lists columns and is incomplete rather than wrong, and the key's own question already asks whether a resubmittal is a new item or a revision.
- Considered, not hits: allocations (v0.1 already has one item per assignment with a timeline and a percent, and Jordan confirmed the Workload view); addenda (child rows in v0.1); portal registration (a people column holds several people).

**A pain with no element that fixes it.** One hit, kept visible.
- PMs updating their own people (P2.2, "Well. I'd trust these once Jordan isn't the only one updating them.", 00:12:22 Tess). Nothing in v0.1 or in the fifteen v0.2 changes gives a PM edit rights on their own job's rows; the Consultant parked it for setup. Leaning 6 states the shape (everyone sees everything; a PM edits only items where they are the PM, by board permission or a per-PM view) with the plan tier as its condition. In `element_per_pain` P2.2 is `copies-today's-tool`, because until the permission is set Jordan keys every row and the board is the Wall with a better view.
- The three P3 entries are not pains without an element: the burn element exists, but it fixes the pain only once Ajera is read. They are `copies-today's-tool` (section 6).

**An alias-map entry that names more than one entity.** No hit. s3 has no alias map. The nearest candidates in `vocabulary`: "Staff allocation (board) / the Wall (nickname)" is one board with two names; "partner" is one word with two meanings, which the entry already separates; "submitted / short-listed / interview / won / lost" and "CD set / fifty percent set / hundred percent set" are values of one column. Nothing split.

**Our framing labelled as the client's.** No hit. Checked and found already labelled: the milestone status set ("not reached, ready to invoice, and invoiced" is the Consultant's playback, confirmed by Bev at 00:21:36; the vocabulary entry says so and the key's first question asks whether "Not reached" is right); billing type "On each phase" (the trap and the `requested_changes` entry both say job or phase level to confirm); the No-go position in the stage order (the trap says the Consultant's read-back placed it and Tess confirmed); the saved view's columns (the Consultant proposed PIC, addenda and fee sign-off at 00:08:37, Tess said "That's it. Save it as that", and the key's fifth question still asks which columns). The PM edit scope is Jordan's own question (00:10:39), the firm-wide log is Jordan's "One board." (00:22:15), and the per-job window is Jordan's "So it's per job." (00:22:53). The one place our framing shaped the record is the milestone level, and the leaning carries it.

**A shared resource with no reservation tracking.** One hit.
- Reviewers. "The reviewer was out sick, and his queue was in, like, four different spreadsheets in four job folders, so nobody knew he had anything." (00:23:07 Jordan). The log board with a reviewer column is the reservation; what the call never settled is who covers for an absent reviewer. Leaning 4: reviewer, received date, due back from the job's window, a view of unassigned, past-due or out-reviewer submittals; the cover question is the condition. People across jobs are already reserved by the allocation rows, which the client confirmed; no second hit.

**An artefact that can go stale with nothing to flag it.** Two hits.
- Burn figures. "I don't believe any number I didn't put there. Not until I know where it came from and when." (00:14:04 Bev) and "Billing. The fee is at billing rates, so burn has to be at billing rates too, or it looks better than it is." (00:14:26 Bev). Leaning 5: a source and an as-of date on every hours and spent figure, at billing rates, outdated once older than the WIP cycle; in v0.2 every figure is a labelled sample. No field corrected: the key already says burn stays on sample data and must be at billing rates.
- The pursuit's addendum status. From `context-v0.1.md`: the automation watches a status column on the pursuit that a person sets to "New addendum", beside the addenda subitems, so a second addendum can be logged under a parent still reading "Reviewed". The client confirmed the behaviour ("And it goes to more than one person, which is the whole point.", 00:04:12 Tess), not the mechanism. Leaning 7: the trigger moves to the child row and the parent's status and latest date derive from the children; the change check before v0.2 is the condition. No field corrected: `entities_and_workflows[3]` says "logged on the pursuit, with a notification", which is not wrong.
- Considered, not hits: Hallie's two test pursuits (the trap already says they are test items; they carry `goes_stale` in `entities`); the fee sign-off after a rebuilt fee (an s1 leaning, carried in `entities` as `goes_stale` without a second leaning here).

**An expected output the input cannot support.** No hit. Recounted from the transcript: 187 units, 3,966 spoken words against "about 3,970", 4,459 tokens with labels against "about 4,460", client share 62.0 percent (Tess 22.5, Bev 21.3, Jordan 18.3 against the key's 22, 21, 18), the Consultant's longest turn 103 words at 00:24:14, first stamp 00:00:03 and last 00:30:30, ASCII only. All true. The call date "inferred as 2026-09-25" rests on `context-v0.1.md` dating the walkthrough to Thursday September 24, 2026 and the call's "yesterday", so it is supported by a document in the fixture, not pinned from a weekday alone (the s15 line). The counts COVERAGE tracks for s3 (29 traps, 15 requested changes as 7/6/2, 141 `quote` fields before this pass) were recounted and are true of the file.

## 4. The "never written to" rule

s3 is one of the eleven keys the s14 entry names. A search of the key for "writes back", "written back", "write back", "writeback", "never written", "not written", "never touch", "read-only", "one direction", "one-way", "nothing writes", "stays in Ajera", "lives in Ajera" and "book of record" found the phrasing in `purpose_of_this_fixture`, `company.current_tools[0]`, `expected_monday_products[1].why`, `rubric[0]` (evidence and note), `vocabulary[15]` and `[17]`, `entities_and_workflows[7]` and `[9]`, `integrations_mentioned[0]`, `compliance_or_security_signals[1]`, `commitments_and_next_steps[5].what`, `traps[10]`, `requested_changes[10].description`, `expected_questions_before_building[6]`, and `accepted_behaviours[8]` and `[10]`.

Every one of them traces to a client quote on this call, so none is reworded:
- "nothing writes back", "one direction", "read-only" and "time entry, invoices stay in Ajera" trace to the controller: "And that nothing, ever, writes back into Ajera. It's one direction, Ajera to this. Time entry stays in Ajera, invoices stay in Ajera, and I am not reconciling two systems at month-end." (00:14:44 Bev Halvorsen), repeated as her written condition at 00:26:41.
- "Paid lives in Ajera" and "no payment status" trace to 00:19:48 Bev Halvorsen: "Don't show me paid. Paid lives in Ajera."
- `compliance_or_security_signals[1]` opens with "Ajera stays the book of record", which is the s1 client's phrase, but the no-write clause that follows it traces to 00:14:44, so the entry stands.
- `commitments_and_next_steps[5]` and `accepted_behaviours[8]` describe the one-page description the Consultant committed to send, whose content answers Bev's three things; the "nothing writes back" in it is hers.

The distinction this fixture adds to the rule: here the client settled the direction (one way, Ajera to monday, nothing back), so it is not ours to label as our safe default. What is unresolved is whether a read exists at all (the API has never been enabled; the IT provider wants the fields in writing first). The block's `existing.incumbents` entry for Ajera says exactly that: direction is the client's own condition, the read is unresolved, and neither v0.1 nor v0.2 depends on a read.

## 5. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites hardest on the milestones. Leaning 1 and the P5 rows of `element_per_pain` say that ready to invoice is the PM's claim that a milestone was hit, that the signed letter or the issued set is the evidence, and that invoiced is a claim about Ajera until the invoice number is typed by the person who raised it. Leaning 5 says no burn figure on a board is Ajera's figure until a read exists. The second AI idea reports board state, never Ajera's; the third suggests a date from the letter and never sets the status.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked across the fifteen `commitments_and_next_steps` entries: each carries owner, purpose and a date or "not set", and none claims delivery. Bev's entry already notes that only the Harwood schedule was confirmed, not the list of milestone jobs. The block carries the state as verdict conditions: the invite, the written change list and the Ajera page are committed, not sent; the samples are committed for Monday, not received; the Submittals log and the milestones wait for them. No `status` field was added, for the reason the exemplars give: that would change the shared s1-to-s10 shape, which is one decision for all twenty-five keys.
- **s11 (inference targets questions; it never fills evidence).** Seven unconfirmed client ties sit in `signals`, each naming what our side never confirmed: Gordon's relayed "That's the Larkspur fix.", Gordon's relayed clinic question, Bev's "that is not what DD burned", Hallie's relayed reaction and ask, Marcus's relayed API statement, Jordan's portal-pull ask, and Jordan's "owner approvals sneaking back in". Three of the five questions are read-backs built on them. None appears as evidence or in an element. One entity (the submittal revision) is `source: assumed` with `evidence: null`.
- **s15 (a product limit never deletes a client need).** Six entries in `unmet_needs` keep needs the build does not meet: automatic portal pulls, PMs updating their own people, burn on the firm's own figures, something for Gordon before Thursday, owner approvals, and invoices before each district's cutoff; each says why and carries the clock the client gave, or null.

## 6. The readiness block, field by field

- `pains`: the key's seventeen `pains` entries in array order, same quotes and locations. Ids follow the key's themes with a running number after the dot: P5.1 to P5.6, P3.1 and P3.2 (the two P3 entries that come first), P4.1 and P4.2, P1.1, P2.1 and P2.2, then P3.3 ("I don't believe any number I didn't put there", the key's third P3 entry). The three "Feedback on v0.1" entries have no P-number in the key, so they take the next free number as P6.1 (the dashboard), P6.2 (the CRM default stages) and P6.3 (the generic phase statuses), as the brief's section 8 directs; the key's own leak block lists P1 to P5, and P6 lives only inside the block. P1 to P5 are `excavated` (the key's R2 note: P1 to P3 on s1, P4 and P5 on this call); P6.1 to P6.3 are `stated`. Outcomes are verbatim from the client: Bev's "When a PM marks it ready to invoice, I want to know that day." (00:20:39) for the six P5 entries; "With one list, I filter by reviewer and I see it in ten seconds." for P4; "And it goes to more than one person, which is the whole point." for P1.1; Jordan's staffing-call sentence for P2.1 and "I want the PMs updating their own people in here, which is the big thing." for P2.2; "Not until I know where it came from and when." for P3.3; "I need the list.", Tess's stage list and Jordan's phase list for P6.1 to P6.3. P3.1 and P3.2 carry null: the only outcome words aimed at burn on this call are conditions ("I'll believe it when it's our numbers"), and the s1 outcome is not on this transcript.
- `signals`: seven (section 5).
- `entities`: twenty-eight, twenty-one with a parent, every one with `moves_independently`. Milestones, submittal revisions, addenda and allocations move independently of their parents; billing type, the review window and portal registration do not; PM edit scope is `unknown`. `shared_resource` is true for people and reviewers. `goes_stale` is true for the fee sign-off, portal registration, the milestone's hit state, hours and burn, the WIP report, allocations and the two test pursuits. Sources: `spoken` with a transcript location, `observed` with the `context-v0.1.md` section named, one `assumed`.
- `structure`: CRM and Work Management, as in v0.1. `build_target` is `own-account` with the brief's reason string. `workspaces` is `["Brackenholt Operations"]`, the one workspace `context-v0.1.md` records: spec section 9 plans one workspace per product "unless the build continues workspaces already built for the same client", and the key's accepted behaviours rule out a second workspace, so the A21 default is not applied and a verdict condition and an assumption say so. `native_reuse` names the native Deals/Opportunities and Accounts boards and the remap rule if v0.1's boards are look-alikes. Seven leanings (sections 3 and 5), five patterns applied, seventeen `element_per_pain` rows: thirteen `fixes`, four `copies-today's-tool` (P3.1, P3.2, P3.3 until Ajera is read; P2.2 until PMs edit their own rows), no `none`.
- `existing`: the v0.1 build as `context-v0.1.md` describes it, read under A21 as the user's own account, with preflight named for the board ids and the plan; the client's own account unbound, tier unknown. Seven incumbents with what each stays the record for (section 4 for Ajera).
- `assumptions`: sixteen, each with the question that would replace it, including the workspace decision, the native-board assumption and the tier.
- `unmet_needs`: six (section 5).
- `ai_opportunities`: five. Two are round 1, because the client asked for them in substance on the call: Bev's same-day notification ("When a PM marks it ready to invoice, I want to know that day.") and Jordan's automatic portal pulls ("Can it go get the addenda off the bid portals by itself?"); both are `workflow` with P-21 as the probe basis, following the s5 exemplar. The agent and the AI column are round 2 and `unprobed`.
- `verdict`: `build`. Ten conditions, starting with the approval stop and the A11 point (none bites for an own-account target; the three A11 decisions stay open), then the workspace, the native boards, the two build tranches and their committed inputs, sample-only figures, the committed-not-sent items, no price, the plan read at preflight, and the client's three clocks. The key's `should_plugin_propose_a_build` is `true` and its verdict proposes v0.2, so the two sides agree and the `note` gains no extra sentence; it does say that `context-v0.1.md` is read as what exists.
- `questions`: five, the ceiling. Q1 (Ajera fields and the API), Q3 (the fork) and Q5 (PM edit scope) are read-backs on signals; Q2 (milestones) and Q4 (the submittal log) are discovery. Each is routed and says what is known. Reused from the key's eleven: items 1 and 7 wholly, items 3 and 6 wholly, item 2 in part. Dropped into assumptions: who counts as finance (item 2 in part), the form field type (item 8), the sample remap and the hit rate (item 4), the view's columns and Gordon (item 5), the native boards (item 10, a preflight read) and the plan tier (item 11, a preflight read of the build account under A21). Dropped as the user's own decision rather than a client question: whether to build the larger items before or after scope is agreed (item 9); the verdict conditions sequence them instead.

## 7. Fields corrected or extended outside the block

One. `entities_and_workflows[12]` ("Owner approvals stay deferred; only the billing milestone is tracked") gained the fork and its leaning, as the brief directs for a fork that keeps its existing entry elsewhere in the key: Jordan's "That's owner approvals sneaking back in, by the way." (00:20:08) against Tess's "No. It's just the billing piece. We said owner approvals later, and I still mean later." (00:20:13); leaning billing only, the signed letter linkable as evidence, no approval workflow; settled by whether Tess counts a linked letter as approvals tracking. The two quotes are inside the string rather than structured pairs, which is why the verifier's pair count rose by 41 and not 43. No other existing field was changed; no sweep hit required a correction, because in each case the existing field was incomplete rather than wrong (section 3).

## 8. Left as it is, and flagged for the planner

- **Workspaces across the s1, s3 and s10 chain.** The s1 block names two workspaces for this client (one per product, A21), written as a build from nothing. `context-v0.1.md`, written earlier, records the build the user actually showed as one workspace, and this block continues it. The two blocks disagree only because they describe different moments; s10's editor will meet the same question. If the planner wants one answer for the chain, it is whether `context-v0.1.md` or the A21 default governs a fixture that describes an existing version.
- **`account_context.tier`** still says the tier is "asked at the scoping session". Under A21 the build account's plan is read at preflight and the client's eventual tier is a handover question; the block says so, and the field is left as the key's v2 reading.
- The key's `expected_questions_before_building` is left as its eleven items; the block's five are a selection in build terms, not a replacement.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (3 read-back, 2 discovery) |
| pains | 17 (14 excavated, 3 stated) |
| signals | 7 |
| entities | 28 (21 with a parent, all with `moves_independently`) |
| leanings | 7 (6 sweep patterns, 1 fork) |
| element_per_pain | 17 (13 fixes, 4 copies-today's-tool, 0 none) |
| incumbents | 7 |
| assumptions | 16 |
| unmet needs | 6 |
| AI opportunities | 5 (2 round 1, 3 round 2) |
| existing fields changed | 1 (`entities_and_workflows[12]`, the fork) |
| transcript edits | 0 (187 units unchanged) |
| key size | 2,163 lines, from 1,288; 26 top-level fields |

## 10. Verifier output

`python3 -I ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_fixpass/verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s3-followup-demo-feedback`, run after the only edit, exit code 0:

```
Fixture: s3-followup-demo-feedback
Sources: context-v0.1.md (context, 42 units); transcript.txt (transcript/line-time-last, 187 units)

pairs found      183
verified         183  (of which presence only, no location cited: 41)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were reported; no unit was renumbered. The same run on the untouched key, before the edit, found 142 pairs with zero misses, so the pass added 41 verified pairs and broke none.
