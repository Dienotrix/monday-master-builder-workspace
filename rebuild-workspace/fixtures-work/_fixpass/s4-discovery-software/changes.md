# s4-discovery-software — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s4-discovery-software/answer-key.json` only. `transcript.txt` is unchanged (263 cues, WebVTT; the mess pass of the s11 rule applies to s12 to s25, and no FEEDBACK entry asks for a transcript change here). There is no README for s4. The key was loaded, changed and dumped by script (`indent=2`, `ensure_ascii=False`, trailing newline) after a round trip without changes had reproduced the file byte for byte. The file was already UTF-8 before the pass (Kraków), so the en dash in the workspace names changes nothing about its encoding. The 25 fields keep their order; `readiness` is the 26th and last. A field-by-field diff against the untouched copy shows five changed strings outside the new block, all logged below, and `rubric`, `expected_verdict`, `numbers` and `pains` identical.

FEEDBACK.md has no entry for s4 (its fixture entries cover s11 to s25), so the pass here is the sweep, the never-written rule, the standing lines and the readiness block. The `direction` rename does not apply: the key has no `intake` field and `direction_of_show` appears nowhere in it.

## 1. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit becomes a `structure.leanings` entry; a field is corrected only where a builder reading it alone would build the flaw (exemplar rule), otherwise the leaning carries the addition and the field stands.

**One row where the call describes many.** Three hits, one of them conditional.
- Access grants under one request. The auditor wants "an approval on every access grant and a clean record when someone leaves" (cue 148) and quarterly reviews of "Who has access to what, who approved it" (cue 133). One ticket with one approval cell would carry one value for several systems, and the leaver record and the review need the grant, not the request. Leaning 1: grants as child rows with their own approver, date and revoked date. **Field corrected:** `vocabulary["access requests / access reviews"].likely_monday_object`, which read only "with an approval status and an audit trail"; it now says where one request names several systems each grant is a child row, pointing at the leaning. Settling condition: whether a request today names one system or several, and what the auditor samples.
- The escalation and the engineering work item. "Or there's two Redmine issues for the same thing because two people grabbed it. Or zero." (cue 83) and the June export change, "Like fifteen tickets in the first hour" (cue 170), show the two move independently: one escalation per Zendesk ticket, zero or several escalations per work item. Leaning 2 keeps them apart and says that in v0.1 the work-item reference is a link or text, because the work item is monday dev. No field corrected: the vocabulary entry for escalations already separates the Service ticket from the dev item.
- The VP's "project" as one row, conditional on a Work Management approach for the engineering half. "those are epics technically, I guess. Or a bunch of epics." (cue 58); the typed status would be Devin's roadmap sheet again (cue 55). Leaning 7: initiative as parent, epics as child rows, status rolled up. No field corrected: `vocabulary["projects (the big stuff...)"]` already says "epic item with a roll-up (roadmap) view".

**A pain with no element that fixes it.** Ten `none` rows and two `copies-today's-tool` rows in `element_per_pain`, all kept visible. Nine of the ten have one cause: their fix is monday dev, outside v1 (P2.1 PR linking, P2.4, P3.1 and P3.2 release notes, P5.1 to P5.3 Redmine, P6.1 and P6.2 the cross-squad roll-up), so they share leaning 5, which states the user's choice between a clearly labelled Work Management approach and waiting, and they land in `unmet_needs` with the end-of-November clock. P1.7 (the same bug fixed twice in two squads) is `none` too: duplicates are caught in the engineering tracker and code review, which the Service build does not reach. P2.2 and P2.3 (three weekends; the scavenger hunt) are `copies-today's-tool`: a PBC request board with linked evidence is the Drive folder with an index, which tracks the request and not the trace from ticket to approval to PR to release (leaning 6). No field corrected: the key's `expected_monday_products` and `traps` already say the engineering half is not built.

**An alias-map entry that names more than one entity.** No hit. s4 has no alias map. `vocabulary` was read as the nearest thing. "squads (Dispatch, Billing, Mobile, Platform, plus one unnamed)" and "the tech app / the web app" name values of one column, not things that move independently. "on-call / handoff doc" pairs a rotation with its artefact and "incident / postmortem" an event with its write-up; both are a term and its derivative, like the s1 glossary pairs, and stand. The `entities` list does separate the on-call week, the handoff record and the pending item, because they go stale differently.

**Our framing labelled as the client's.** No hit. Checked: the three-item first look is the Consultant's list (cues 238 to 239), but Tomasz confirmed it out loud, "Yeah. Those three." (cue 240), added on-call handoffs, and Colleen added the account manager view, so the key's "agreed, hedged" is right. The $120 placeholder, the "one full engineer" framing and the proposed success criteria are already labelled as the Consultant's. The IT service desk scope was volunteered by Tomasz (cues 147 to 149) in answer to a question, not proposed. The PII rule, "an escalation needs to carry enough to reproduce the problem, but not the customer's personal details" (Consultant, cue 124), was confirmed by Colleen in her own words (cue 125), which is the quote the key uses. The one soft candidate, the status label "acknowledged" in `vocabulary["put eyes on it"]`, is a label suggestion marked "such as", not a client term, and stands.

**A shared resource with no reservation tracking.** No hit. Nothing on the call is booked across jobs in the sense the pattern means. Two candidates were considered and declined. The on-call engineer is a person booked for a week, but the rotation lives in SRE's on-call tooling (cue 46), which the build does not replace; the entity carries `shared_resource: true` and the incumbent line says so. Laptops are named once, as a request type ("Laptops, access, offboarding, it's all DMs", cue 149), and the key already says not to add Asset management unasked; the laptop entity carries `shared_resource: true` and an assumption carries the question. Forcing a holder-and-return structure from one word would be our framing.

**An artefact that can go stale with nothing to flag it.** Two hits, plus two entities marked without a leaning.
- The escalation tracker, "wrong by lunch" (cue 89). The ticket replaces it, but the sheet's columns are of two kinds: Colleen's own (owner, status) and copies of other systems (the Zendesk state, "when we last told the customer something", the Redmine number). Leaning 3 says which values are the record and which are claims, with who set them and when; this is also where the s22 line bites (section 3). No field corrected: `vocabulary["the escalation tracker"]` says the sheet is replaced by the native Tickets board and a saved view, which is true and merely silent on the mirrored columns; the leaning carries them.
- The on-call handoff doc, "aspirational" (cue 140), which dropped the Monday hotfix (cue 143). Leaning 4: a handoff board with pending items as child rows that stay open until closed. **Field corrected:** `vocabulary["on-call / handoff doc"].likely_monday_object`, which offered "item per week or doc"; a builder choosing the doc would rebuild today's artefact, so the "or doc" is gone and the entry points at the leaning.
- Release notes and Devin's roadmap sheet carry `goes_stale: true` in `entities` without a leaning of their own: both belong to the engineering half (leaning 5).

**An expected output the input cannot support.** One small hit, corrected. The key stated Redmine has "eleven" projects "including Support Escalations and Misc"; Devin said "I think, eleven projects? Roughly one per product area" and then named the Support Escalations and Misc projects separately (cues 51 to 52), so the count is hedged and whether it includes those two is not said. **Fields corrected:** `vocabulary["projects (in Redmine)"].meaning` and `traps[5]`, both now carrying the hedge and the quote. Checked and left: the transcript statistics in `transcript_format` (recounted from the file: 263 cues, 00:40:34 end, 5,139 spoken words against "about 5,140", client share 71.7 percent against "about 72 percent"; all true); the dates (the month is held open, "the 22nd is a Tuesday in September 2026" is labelled an inference); the fifth squad (the key says ask, do not invent); the loose counts ("about 14 of 40", "about 40 escalations a month last year (loose)") all keep their hedges.

## 2. The "never written to" rule

s4 is not among the eleven keys FEEDBACK lists. A search of the key for "written to", "write back", "writeback", "written back", "never touch", "not written", "read-only" and "one way" finds no no-write claim about a client system. The two "stays the" phrasings, "Zendesk stays the customer helpdesk" in `vocabulary["tickets"]` and `expected_monday_products[0]`, trace to Colleen's own words, "I'm not ripping out Zendesk four months before an audit" (cue 207), and say nothing about writing, so they stand. "Everything else we archive read-only" is Tomasz's sentence about Redmine (cue 210), quoted as his. Nothing was reworded.

The new `existing.incumbents` lines use the rule's wording from the start. For Zendesk the client did ask for something to flow back, "having the status come back, that has to connect to Zendesk somehow" (cue 208), so the line says: how, and in which direction, is unresolved; v0.1 does not depend on it; a link column is our safe default, labelled as ours, and it is not an email-to-ticket channel. Redmine: v0.1 writes nothing into it and migrates nothing. GitHub: the PR link is the client's must-have and is dev; no GitHub behaviour promised unverified. The same unresolved state is signal 6 and part of question 2.

## 3. Standing lines where they bite

- **s22 (a board status set by a person is a claim, never evidence the source system changed).** Bites on the escalation ticket, where leaning 3 and the P1.3 element say owner, severity, acknowledged and status are events on the ticket, while "last customer update" is a claim about Zendesk and "released" a claim about GitHub and the release train until a connection exists, each shown with who set it and when. It bites on access too: the approval recorded by the approver happens in monday, so there it is the event rather than a claim (like the s1 fee sign-off), but whether monday's log satisfies "who changed an approval and when, and that it can't just be quietly edited" (cue 216) is unverified and sits in `assumptions` and `unmet_needs` for Oren. A verdict condition says every mirrored value is labelled a claim.
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Checked; no field needed correcting. The seven `commitments_and_next_steps` entries carry owner, purpose and a date or a loose one, none is recorded as done, and Oren's attendance keeps its "no promises". The verdict's last condition restates the state: the invite is committed, not sent; the tracker, the Dispatch CSV and the control-list sections are committed inputs, not received. The R10 note's "The consultant sends the invite right after the call; Tomasz forwards it to Oren" sits in `rubric`, which this pass does not touch; noted for the v2 pass. No `status` sub-field was added to the commitments array, which would change the shared s1 to s10 shape.
- **s11 (inference targets questions; it never fills evidence).** Seven unconfirmed client ties are in `signals`, each naming what our side never confirmed, and three drive the two read-back questions (Q2 and Q4). None appears as evidence or in an element. The approval of a production change, which nobody described, is an entity with `source: assumed` and `evidence: null` rather than a guessed location.
- **s15 (a product limit never deletes a client need).** Eight entries in `unmet_needs`: the whole engineering half (PR linking, sprints and epics, release notes, leaving Redmine) with its clocks, the status back to Zendesk, SSO and the unalterable approval record (which cannot be shown in the user's own account), the deferred Service extras, and quarterly access reviews as evidence. The key's existing "deferred beyond v1" wording for the portal, email-to-ticket and SLA policies was checked against the s15 shape: the client asked for none of the three, so no need is being deleted, and the entry says what tempts them.

## 4. The readiness block, field by field

- `pains`: the key's 25 entries in array order, same quotes and locations, numbered by theme as the exemplar rule asks: P1.1 to P1.7 (escalations), P2.1 to P2.4 (SOC 2 change evidence), P3.1 and P3.2 (release notes), P4.1 and P4.2 (on-call), P5.1 to P5.3 (Redmine), P6.1 and P6.2 (roadmap), P7.1 and P7.2 (customer PII), P8.1 and P8.2 (access requests), and the unnumbered cross-cutting Slack pain as P9.1, the next free number. P1 entries are `excavated` (the key grades all six checks Met); every other entry is `stated`, including P2, whose Workaround check is Partial. `outcome` is verbatim from the February-week answers at cues 198 to 200 (Colleen's escalation and PTO sentences; Tomasz's click-through; Devin's release notes and roadmap), Colleen's cue 258 for the tracker pain, Tomasz's cue 233 for the Redmine pains, Colleen's cue 125 for the PII pains, and Tomasz's own cue 56 sentence for P6.2; P1.6, P1.7, P3.2, P4.x, P5.3, P8.x and P9.1 carry null because no outcome words aim at them.
- `signals`: seven, listed in section 3.
- `entities`: thirty, answering "what moves independently of what?". Twelve have a parent and all carry `moves_independently`. The escalation moves independently of the Zendesk ticket and of the engineering work item; a customer update is many per escalation; the access grant moves independently of the request that created it (reviewed quarterly, revoked at leaving); the pending handoff item outlives the handoff; release notes, the handoff record, the evidence screenshot, the tracker and the roadmap sheet go stale. The on-call week and the laptop are the two `shared_resource: true` entries.
- `structure`: Service and Work Management; `own-account`, "prospect, so the user's own account by default (A21)"; "Tollgrove – Service" and "Tollgrove – Ops"; native reuse names the IT-service-desk install, the base Tickets family, the conditional Incidents and Employee lifecycle companions, no CRM, and ordinary labelled boards for handoffs and PBC requests; eight leanings (three one-row-many, two stale-artefact, two no-element, one fork); four patterns; 25 `element_per_pain` rows (13 `fixes`, 10 `none`, 2 `copies-today's-tool`).
- `existing`: "unknown, no account bound", with the A21 point that the client's account question moves to handover and that preflight must find Service in the user's own account; twelve incumbents.
- `assumptions`: fifteen, each with the question that would replace it.
- `unmet_needs`: eight (section 3).
- `ai_opportunities`: four, all round 2. The client never asked for AI or workflows: "If PRs don't link to the work item automatically" (cue 204) asks for an integration, and "Release notes that basically write themselves" (cue 200) is a wish about generation from shipped items, which is dev; neither is a request for an AI element. The two workflows cite P-21; the two AI columns are `unprobed`.
- `verdict`: `build`. Nine conditions, starting with the approval stop and the A11 point (none bites for an own-account target; the three decisions stay open), then the workspaces, the Service detection rule, the scope choice, the engineering-half labelling, the Service extras, sample data, and the committed-not-done items.
- `questions`: five, the ceiling. Q2 and Q4 are read-backs because signals exist (the link-not-copy rule and "come back", and the epics and SOC 2 project answers); Q1, Q3 and Q5 are discovery. Reused from the key's pool of thirteen: item 3 in Q1, items 9 and 13 in part in Q2, item 8 in Q3, items 1 and 5 in Q4, item 12 in Q5. Left to the record as assumptions with their question: the fifth squad and sprint days (item 6; a dropdown placeholder), GitHub and Slack details (item 11; nothing is connected in v0.1), the account manager view (item 13; Devin and Colleen confirmed it is view-only), the Zendesk link and SLA wording (item 4; A7 settles it), the production change approval (item 7; the engineering half), the Redmine history (item 10; a fork, leaning 8). Item 2, which account and which tier, is not one of the five under A21: the proof of concept goes into the user's own account, and the client's account becomes a handover question; `existing.account` says so. The key's own list of thirteen questions is left as it is.

## 5. Left as it is, and noted

`should_plugin_propose_a_build: true` and the readiness verdict `build` agree, so the block's `note` gains no second sentence. `rubric`, `expected_verdict` and `numbers` are untouched. The key's R6 note calls the success criteria "proposed, not yet agreed", which the block respects by giving each pain the client's own outcome sentence rather than a criterion. The fork on Redmine history keeps its existing entry in `traps[13]` and gains the same leaning there, as the brief asks; it is the only fork on the call.

## 6. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 25 |
| signals | 7 |
| entities | 30 (12 with a parent, all with `moves_independently`) |
| leanings | 8 |
| element_per_pain | 25 (13 fixes, 10 none, 2 copies-today's-tool) |
| incumbents | 12 |
| assumptions | 15 |
| unmet needs | 8 |
| AI opportunities | 4 |
| existing fields corrected | 5 (three in `vocabulary`, two in `traps`) |
| transcript edits | 0 |
| key size | 2,106 lines, from 1,079; 26 top-level fields |

## 7. Verifier output

`python3 -I verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s4-discovery-software`, run after all edits (and once before them, when it read 121 pairs clean), exit code 0:

```
Fixture: s4-discovery-software
Sources: transcript.txt (transcript/vtt, 263 units)

pairs found      169
verified         169  (of which presence only, no location cited: 19)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

No location notes were raised (no units were renumbered). The build script proved 38 quote strings against their cues before writing, among them the nine `outcome` strings and the six quoted fragments inside question texts, which the shared verifier does not check because they sit under keys without the word "quote"; it also asserted the speaker on every entity and incumbent `evidence` cue.
