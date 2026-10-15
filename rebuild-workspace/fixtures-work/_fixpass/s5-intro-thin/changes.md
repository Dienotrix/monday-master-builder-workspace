# s5-intro-thin — fix pass changes (exemplar for the thin case)

Editor's log, 2026-10-13. Files touched: `fixtures/s5-intro-thin/answer-key.json` only. The transcript is unchanged, as the task set. FEEDBACK.md has no entry for s5, so there are no fixture-specific items to apply; the sweep, the "never written to" rule, the standing lines and the readiness block are the whole pass here.

Method: the key was loaded, changed and dumped by script (`indent=2`, `ensure_ascii=False`, trailing newline), after a round trip without changes had reproduced the file byte for byte. The 25 fields keep their order; `readiness` is the 26th and last. Every quote the block introduces was copied from the transcript and proven verbatim at its cited unit before the file was written (29 such proofs in the script, 88 pairs in the shared verifier afterwards).

## 1. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit becomes a `structure.leanings` entry; where it also sat in an existing field, that field was corrected.

1. **One row where the call describes many.** Two hits.
   - Committees. "who's doing what" (00:02:24 Jolene Varga) and "each one kind of runs however their chair wants to run it" (00:01:51) describe many moving things under one committee. One item per committee with one status would carry one value for many. Leaning: parent-row-with-roll-up, committee as parent, tasks as child rows. **Field corrected:** `vocabulary["committees"].likely_monday_object` from `board (one item or group per committee)` to the parent-with-children shape, pointing at the leaning.
   - Events. Two registration routes and the events lead's own spreadsheet (00:05:28). Leaning: one row per event with a count, child rows only if he tracks work per registrant. No existing field needed correcting; the vocabulary entries for events already allow "item or group".
   - Considered, not a hit: member and renewal. For a first version one current renewal per member is enough; renewal history is an assumption with its question, not a structural hit, because nothing on the call says past cycles are tracked.
2. **A pain with no element that fixes it.** Two hits, kept visible in `element_per_pain`. P9 (reminders not trusted) and P10 (the clunky portal): nothing we build reaches the portal's reminder emails or decides whether the portal stays. P7 (each chair runs things differently): a board shape does not change a chair's practice, and "somebody set something up and then nobody used it" (00:06:09) is the evidence that a shape alone did not. Both land as leanings with their settling conditions, and P9 and P10 also land in `unmet_needs` (s15 line, below).
3. **An alias-map entry that names more than one entity.** No hit. The key has no alias map. `vocabulary` was read as the nearest thing: "chapter meetings / webinars / field days" names three event types, which are values of one column, not three things that move independently; "education committee / professional development committee" is one committee with two names; "the board / board retreat / board members" is one group. Nothing split.
4. **Our framing labelled as the client's.** No hit. The key already labels the executive director's items as secondhand, "all over the place" as a relayed phrase, and "a better spreadsheet and a couple of habits" as the Consultant's. Near miss checked: "who's doing what" was first spoken by the client at 00:01:51 before the Consultant echoed it at 00:02:19 and the client repeated it at 00:02:24, so the P6 quote is hers.
5. **A shared resource with no reservation tracking.** No hit. Nothing on the call is booked or reused across jobs. Volunteers helping across committees and events was considered and left out: it is not stated, and inventing a shared resource to fit the pattern would be our framing. Every entity carries `shared_resource: false`.
6. **An artefact that can go stale with nothing to flag it.** One hit, the central one for this fixture. The coordinator's Excel tracker is a copy of the portal that drifts ("i also keep my own tracker in excel because i don't totally trust it", 00:04:04). A renewals board that mirrors the portal is the same artefact again. Leaning: members on native CRM boards (A5), with the import date shown on any copied row, and the portal left as the record. **Fields corrected:** `vocabulary["members"].likely_monday_object` (a from-scratch members board named as the look-alike it is) and `vocabulary["tracker / renewal tracker"].likely_monday_object` (follow-up work as items; blank headers as a column list, never rows; a copied list shows its import date). The events lead's spreadsheet and the credits spreadsheet carry `goes_stale` in `entities` without a leaning of their own: both are out of the first version by assumption.
7. **An expected output the input cannot support.** No hit in the sense the pattern means (fixture ground truth graded as an output). The month of "tuesday the twenty second" is already held open by the key. The one tension the pass does raise is between the key's v2 verdict ("Not ready", no build) and the readiness clearance; see section 5.

## 2. The "never written to" rule

A search of the key for "never written", "written to", "written back", "write back", "writeback", "never touch" and "not written" found nothing, so no existing claim needed rewording. s5 is not one of the eleven keys FEEDBACK names. The new `existing.incumbents` line for the portal uses the rule's wording from the start: writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the portal is our safe default, labelled as ours. No client line on this call says anything about writing to the portal, so no stronger statement is available.

## 3. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites on renewals. The leaning for P9 and P10 says a reminded-or-renewed status is a claim about the portal, never evidence from it, and the unmet need for trustworthy reminders says why the build does not meet it. The portal incumbent line says what stays there.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked; does not bite. The key's seven `commitments_and_next_steps` entries each carry owner, purpose and a date or "no date given", and none is recorded as done. The invite is "i'll send the invite today" and stays a commitment. The hedged "yeah i can probably do that" keeps its hedge. No status field was added, because nothing here claims delivery and adding a sub-field to one key alone would break the shape across the set; if the planner wants `status: committed` on every key, that is one decision for all twenty-five.
- **s11 (inference targets questions; it never fills evidence).** Applied through `signals` (seven unconfirmed ties, each naming what was never confirmed) and through the two `read-back` questions that quote the client's own words back. Two entities whose shape is inferred, the committee task and the events spreadsheet's contents, carry `source: assumed` and `evidence: null` rather than a location.
- **s15 (a product limit never deletes a client need).** Applied in `unmet_needs`: trustworthy reminders (P9) and the portal decision (P10) stay in the record as the client's needs with their clocks, even though no element of this build meets them. The key's trap about Service extras being "deferred beyond v1 in any case" was checked against the s15 shape and does not bite here: the client asked for no portal and no ticketing, so no need is being deleted.

## 4. The readiness block, field by field

- `pains`: the key's eleven `pains` entries in array order, same quotes and locations, numbered P1 to P11. Only P1 was numbered in the key; the rest are the ungraded quotes COVERAGE describes, and the verifier wants every one present, so they are numbered in order and P1 keeps its meaning. All `stated`; the key says no pain is excavated. `outcome` is verbatim from 00:06:45 where the client's "one place where we can see stuff" answers the cluster of scatter-and-visibility pains (P1, P3, P4, P6, P8, P11); P5 carries her guess at the executive director's outcome; P2, P7, P9 and P10 carry null because no outcome words aim at them.
- `signals`: seven. The executive director's two relayed items, the partial lapsed follow-up, the portal contract, the bookkeeper's question, the credits spreadsheet, the abandoned setup.
- `entities`: fifteen, answering "what moves independently of what?". Members, renewals, follow-ups, events, registrations and committees move independently; the tracker and the events spreadsheet are artefacts that go stale; payment status goes stale because it is answered from elsewhere. The board of directors is listed as a stakeholder group so no monday board is ever made from it.
- `structure`: Work Management and CRM; `own-account` because the society is a prospect (A21); two workspaces named after the fictional client, one per product; native CRM reuse by detection in the user's own account; five leanings; one pattern applied; eleven `element_per_pain` rows with all three verdict values in use (eight `fixes`, one `copies-today's-tool` for P9, two `none` for P7 and P10).
- `existing`: "unknown, no account bound" for the client's side, with the A21 point that the user's own account is read at preflight; seven incumbents with what each stays the record for.
- `assumptions`: fifteen, each with the question that would replace it. This is the long list the thin case expects, and it is the agenda for the 22nd. Two questions are routed to the user or to preflight rather than to the client (which realistic values may appear; what tier the bound account has), because the client cannot answer them.
- `unmet_needs`: four, two of them pains with no element (P9, P10), two things the first version leaves out by assumption (credits, registrations).
- `ai_opportunities`: three, all round 2, because the client never asked for AI or workflows (she asked whether monday was "like a project management thing", 00:08:56). The workflow cites P-21; the AI column and the sequence are `unprobed`, which is what the probe findings say for those kinds.
- `verdict`: `build-generic`. The reason sentence states the test from the spec: stated pains with named entities and one wanted outcome in the client's words, with the structure resting mostly on assumptions. Six conditions, starting with the approval stop and the A11 point (none bites, own-account target).
- `questions`: five, the ceiling, in build terms. Q1 and Q4 are read-backs because signals exist (the relayed "all over the place" and the abandoned setup); Q2, Q3 and Q5 are discovery. Each says what is known. Reused from the key's pool: item 8 and item 3 in Q1, items 6 and 11 in Q2, items 1 and 2 in part in Q3, item 7 in Q4; Q5 (events) is new. Dropped from the pool for this block, by the rule that a generic build carries assumptions rather than questions and that the check asks what the build needs: who decides and the spend route (items 5, 10; sales material, v2), hours per week (item 4; no build depends on it), chairs' access and permitted member data (item 12; assumptions 9 and 13), and which monday account (item 13; under A21 the proof of concept goes into the user's own account, so the question is about adoption later, not about where to build).

## 5. Left as it is, and flagged

`should_plugin_propose_a_build: false`, the "do not propose a blueprint or build" trap, the matching `accepted_behaviours` lines and `expected_structures.notes` ("Nothing is to be built from this call") all follow the key's v2 verdict, which the brief says stays untouched. The readiness block says `build-generic`. The two statements are about different checks: the sales verdict asks whether the client is ready to buy; the readiness check asks what the plugin needs to build, and the user decided that thin input never blocks a build. I left the v2 fields alone rather than half-rewrite a key whose verdict I may not touch. The same tension exists in s2 and s10, the other no-build keys. **For the planner:** one decision for all three, whether `should_plugin_propose_a_build` becomes a v2 field in the record map or is flipped with a note. Not done here, so it is not done three different ways.

## 6. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 11 |
| signals | 7 |
| entities | 15 (9 with a parent, all with `moves_independently`) |
| leanings | 5 |
| element_per_pain | 11 |
| incumbents | 7 |
| assumptions | 15 |
| unmet needs | 4 |
| AI opportunities | 3 |
| existing fields corrected | 3 (all in `vocabulary`) |
| transcript edits | 0 |
| key size | 1,273 lines, from 666 |

## 7. Verifier output

`python3 verify_quotes.py ~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s5-intro-thin`, run after the edit:

```
Fixture: s5-intro-thin
Sources: transcript.txt (transcript/line-bracket, 75 units)

pairs found      88
verified         88  (of which presence only, no location cited: 16)
skipped          2  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

Exit code 0. An independent walk in the edit script found 72 structured quote-and-location pairs with no misses and proved the eleven `outcome` strings verbatim at 00:06:45; the shared verifier's higher count includes the presence-only quotes in `objections`, `commitments_and_next_steps` and `account_context`.

## 8. What the exemplar teaches

Three judgment calls every editor will meet on thin input, and how this one went.

1. **`build-generic`, not `none`, and the old verdict stays.** The pull on a thin fixture is to read the key's "Not ready" and clear nothing. The readiness check asks a different question. s5 has stated pains, named entities and one wanted outcome in the client's words, so it clears `build-generic`, and the thinness goes into fifteen assumptions, not into a refusal. The v2 verdict fields stay as they are, and the tension is written down for the planner rather than patched in one key. Clear what the record supports; move the doubt into the assumptions list; never silently rewrite the v2 side.

2. **Five questions means choosing, and the assumptions carry the rest.** Thirteen pool questions became five. The test for each: does a build element change depending on the answer, and is there a client signal to read back? Questions about who decides, the budget and the hours went out, because no element depends on them. The "which monday account" question went out because under A21 the proof of concept goes into the user's own account; the client's dormant setup is an adoption question, not a target. Everything that fell out of the five is still in the record as an assumption with its question, so nothing is lost and the user never asks for what the record holds.

3. **The sweep must be allowed to find nothing.** Four of the seven patterns had no hit here, and one pattern's nearest candidate (volunteers as a shared resource) was declined because the call never says it. Writing "no hit" with the candidate named is a result; forcing a leaning to fill a pattern would be our framing labelled as the client's, which is pattern four. The two real hits (committees as one row, the renewal tracker as a stale mirror) are where the structure actually moves, and both were also corrected in `vocabulary` so the key does not contradict its own block.
