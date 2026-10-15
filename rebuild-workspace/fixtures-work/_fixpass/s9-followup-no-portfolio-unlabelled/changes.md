# s9-followup-no-portfolio-unlabelled — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s9-followup-no-portfolio-unlabelled/answer-key.json` only. `transcript.txt` is unchanged (119 paragraphs, no edit asked for; the mess pass applies to s12 to s25). `context-v0.1.md` is not edited, as the task set; the readiness block reads it as what already exists. There is no README. The key was loaded, changed and dumped by script (`edit_key.py` in this folder: `indent=2`, `ensure_ascii=False`, trailing newline) after a round trip without changes had reproduced the file byte for byte. The 25 fields keep their order; `readiness` is the 26th and last. The key stays ASCII: the one workspace name is the existing v0.1 workspace, which carries no en dash.

FEEDBACK.md has no entry for s9 (its fixture entries cover s11 to s25), so the only FEEDBACK material applied is the cross-fixture sweep, the fix-pass rule from s14 and the standing lines from s11, s21 and s22. The `direction` rename does not apply: this key has no `intake` field and `direction_of_show` appears nowhere in it.

## 1. The seven-pattern sweep over the key

Each hit became a `readiness.structure.leanings` entry. Where the hit sat in an existing field and a builder reading that field alone would build the flaw, the field was corrected too; where the field was only incomplete, the leaning carries the addition and the field stands.

**One row where the call describes many.** Two hits, both already corrected in the key's own fields by the call itself, so no field was changed.
- Milestones. v0.1 holds a baseline and a current date; the senior PM says the owner wants the history ("They want the history.", paragraph 45; "First patient day has moved twice on the tower.", paragraph 45) with a typed reason (paragraph 47). `vocabulary["milestone"]` already says "each change, its date, and a typed free-text reason", so it stands. Leaning 1 states the shape (date changes as child entries under the milestone) and leaves the mechanism (subitem or dated update) as the condition.
- Templates. One occupied-renovation template for three project types, when "The equipment one is shorter and it's a completely different list." (paragraph 70). The key's `lookalike_traps` and `requested_changes` already carry this. Leaning 6 states one template per type with its own startup list, conditioned on the two checklists arriving.
- Considered, not a hit: allocation rows. "Everything in there is a commitment." (paragraph 59) is a missing state on the row, not one row standing for many; it lands under pattern 5.

**A pain with no element that fixes it.** One hit and two dependency verdicts, all visible in `element_per_pain`.
- P1.1 (the roll-up is only as good as the fourteen spreadsheets) has no element in this version: the leadership roll-up is deferred by the client's own decision, and the PMO director's view over the three projects is her own screen, not a portfolio. Marked `none`, with the reason that the trust is addressed at the inputs (P1.2 to P1.6) and the roll-up waits on the two revisit conditions (leaning 9). This is the client's choice, recorded as hers; it stays a finding because the pain stays unmet.
- P3.1 and P3.2 (burn) are `copies-today's-tool`: until the first Sage report is uploaded the burn column holds sample money, which is the senior PM's exact complaint ("It's a good-looking screen with made-up money on it.", paragraph 73), and the upload is a monthly manual feed v0.1 does not have. Leaning 4 and question 3 carry the dependency.

**An alias-map entry that names more than one entity.** No hit. s9 has no alias map. The nearest candidates: `vocabulary["the OAC"]` carries two senses (the meeting and the preparation for it), which is one term with two meanings, not two entities merged; "the board" is the executive committee only; the pronoun "her" in "copy her" (paragraph 83) and "her and not a PM" (paragraph 63) resolves to the PMO director by the next turn (paragraph 64). Each absent colleague (Curt, Roland, Stefan, Kyle, Junie, Nadine, Ruben) is one person. Nothing split.

**Our framing labelled as the client's.** One hit in two fields, and one wording.
- "A permission, not a preference" is the Consultant's phrase (paragraph 65: "I'll write that down as a permission rather than a preference"). The client's words are "I want to be the one who does it" (paragraph 62) and "her and not a PM" (paragraph 63). `compliance_or_security_signals[4]` said "This is a permission, not a preference, and was recorded as such on the call"; `requested_changes[8].description` said "Recorded as a permission, not a preference." Both corrected to say whose framing it is and that the client did not object; the substance (only the resource manager confirms; the director substitutes) is the client's and stands.
- `entities_and_workflows[1]` said the revisit conditions "double as success criteria". The client gave them as the test for revisiting ("Two things have to be true", paragraph 19); treating them as success criteria is our proposal. Corrected to say so. The same framing in `objections[3].type` and `expected_verdict.gates_not_met[1]` sits in v2 fields and is left.
- Checked and left: "real projects, not boards dressed up to look like projects" is the Consultant's (paragraph 30) and the key says so; the closing list (paragraph 110) is the Consultant's summary, confirmed by the client with "That's the list." (paragraph 111); the eighteen-item list is the Consultant's trim, which the client grades ("Mostly", "eighteen is about right for a renovation", paragraph 70).

**A shared resource with no reservation tracking.** One hit. People across jobs: the allocation board is the reservation, and v0.1's rows carry no requested-or-confirmed state and no rule about who confirms (context-v0.1.md; "Everything in there is a commitment.", paragraph 59). The key's `requested_changes[8]` has the change. Leaning 3 adds what the key leaves open: whether a requested row shows in the Who's over workload at all, whether it counts toward over-capacity, and what a refused request becomes; the condition includes a preflight check that the build account's tier supports a column permission limited to two named people. Question 1 is this.

**An artefact that can go stale with nothing to flag it.** Four hits.
- The roll-up itself, named by the client ("a roll-up is only as good as the forty things underneath it", paragraph 13). Leaning 9 records the deferral, the projects staying real projects, the director's own view and the two revisit conditions.
- Burn actuals from the monthly upload. `vocabulary["burn"]` and `requested_changes[11]` name the upload but not how its age shows. Leaning 4: two columns (actuals with their report month and uploader; the PM's forecast, PM-owned), burn computed from both and labelled with the actuals' month; every actual a sample until the first upload. Field left, since it is incomplete rather than wrong.
- Health colour. A colour set by a PM is a claim (s22). Leaning 2: last-changed-by and last-changed-at on the item with the column history behind it.
- Projects already created from a template when the startup list changes, which it is still doing (paragraph 70). Leaning 8: changes applied to live projects by hand as a listed step. This is a build mechanic for the user, not a client ask, and the leaning says so.

**An expected output the input cannot support.** Two hits in the build sense; none in the fixture-ground-truth sense.
- The ICRA reminder's corrected recipients need a project engineer, and v0.1 names a PM and a superintendent on the project and no project engineer (context-v0.1.md). `requested_changes[12]` says the change "edits a row on the single automation approval list", which is incomplete rather than wrong. Leaning 7: a Project engineer people column on the project, or on the ICRA item if engineers differ per work area. Question 4 asks which.
- A program total for Cumberland's January review. The client chose a filtered list with no total and took the risk ("He's a milestones man more than a totals man. But he might.", paragraph 29). Leaning 5 records that nothing total-shaped is built and the risk is hers.
- Checked: `transcript_format` counts (recounted: 119 paragraphs, 3,485 words with the stamps, eleven stamps at paragraphs 1, 4, 11, 19, 33, 54, 72, 79, 86, 98 and 112, paragraphs 55 and 60 running two speakers together, paragraphs 52 and 53 and 62 and 63 as the same speaker, one `[inaudible]` in paragraph 40); all true. The call date stays an inference offered as one.

## 2. The "never written to" rule

s9 is not among the eleven keys FEEDBACK lists. A walk of the whole key for "never written", "written to", "written back", "write back", "writeback", "never touch", "not written", "read-only", "one way", "stays the", "book of record" and "system of record" found no claim that Sage, Procore or any client system is never written to. One occurrence of the weaker form was found and reworded:
- `integrations_mentioned[0]` ended "Sage stays the book of record and must not be rebuilt in monday." Nothing on this call says "book of record"; the client's words fix only the read direction ("he already produces a job cost report on the eleventh or twelfth and he doesn't much care if somebody uploads it somewhere", paragraph 75). Now: "The call fixes only the read direction, a monthly upload of the controller's report (paragraph 75); writeback and integration direction beyond that upload are unresolved; v0.1 does not depend on either; keeping job cost in Sage and not rebuilding it in monday is our safe default, labelled as ours."

Checked and left, because each traces to a client line or is not a no-write claim: "Nothing real may be written into the client's tenant until the security review clears" (`integrations_mentioned[3]`, `compliance_or_security_signals[1]`, `traps[21]`, `account_context`) traces to the Consultant's proposal in paragraph 80 and the client's "That's how it has to be. He'd find out." in paragraph 81; "that's Procore's job" (paragraph 40) is the senior PM's; "no live connection this year" (paragraph 75) is the client's. `traps[20]`, `expected_structures.lookalike_traps[8]` and `accepted_behaviours[15]` say a job-cost board must not become "a second book of record", which is a no-duplicate rule resting on the client's refusal to endorse made-up money and the controller's relayed position, not a no-write claim; left. The readiness block's `existing.incumbents` entry for Sage carries the unresolved wording from the start.

## 3. Standing lines where they bite

- **s21 (a commitment is `committed`, done only on evidence).** Bites on the two startup checklists. Three fields said they "are being sent" (`requested_changes[10].description`, `entities_and_workflows[7]`, `integrations_mentioned[4]`); the call has "I'll send you my master version and Warren's version" (paragraph 71) and nothing sent. All three now say the PMO director committed on the call to send them and neither has been received. The invite ("I'll send the invite this afternoon.", paragraph 115), the two further PMs' hours (paragraph 117) and the retirement of the Monday status email (paragraph 109) are already written as commitments in `commitments_and_next_steps`; they are listed in the block's verdict conditions as committed, not done. No `status` field was added to the commitments array, since that would change the shared s1 to s10 shape. `expected_verdict.gates_met[2]` ("The next showing is booked for Thursday the fifteenth") is v2 material and untouched.
- **s22 (a board status set by a person is a claim).** Bites on health and on burn. Leaning 2 and the P1.3 to P1.5 element rows say the colour is the PM's claim and the audit shows who claimed it, never that the job is green. Leaning 4 says every actual is a sample until the first upload and then a copy of Sage as of its report month. The confirmed allocation state is the resource manager's own act in monday, so there it is the event and not a claim about another system.
- **s11 (inference targets questions, never fills evidence).** Seven unconfirmed ties are in `signals` (the VP of Operations' two relayed remarks, Cumberland's VP, the resource manager's and the senior PM's ties of the workload view to the collision pain, the controller's position, the IT director's questions); four of the five questions are read-backs; none appears as evidence or in an element. The project engineer on a project carries `source: assumed` and `evidence: null`.
- **s15 (a product limit never deletes a client need).** Single sign-on and permissions inside the client's tenant cannot be shown in the user's own account and stay in `unmet_needs`; so do the live Sage connection, the leadership roll-up, the Cumberland total, the pipeline view and the parked warranty inbox, each with its clock where the client gave one.

## 4. The readiness block

Built from the key's own content in the brief's exact shape. Counts: pains 15 (the key's 15 entries in array order, same quotes and locations), signals 7, entities 29 (18 with a parent, all with `moves_independently`), leanings 9, element_per_pain 15 (one per pain id; one `none`, two `copies-today's-tool`, twelve `fixes`), incumbents 9, assumptions 17, unmet_needs 8, ai_opportunities 5 (all round 2: the client never asked for AI or workflows; three workflows on P-21, one agent on P-19, one AI column unprobed), questions 5 (four read-backs, one discovery), verdict `build`.

- **Pain ids.** The key numbers its 15 entries under four themes, two of them under two themes at once. Each entry keeps its own id, theme number first and running number after the dot, in array order: P1.1 to P1.5, P2.1 to P2.3, P3.1 to P3.2, P3.3 (the key's "P3 and P1" entry, filed under its first-named theme), P4.1 to P4.3, and P1.6 (the key's "P1 and P4" entry, filed under its first-named theme). All `stated`: this is a feedback call and the client raises every one; the nearest candidate for `excavated`, "Because it's a number I make up." (paragraph 42), answers "Tell me why" about a removal the senior PM had already asked for. `speaker_role` carries the inferred role with "(inferred, speaker unclear)", because the transcript has no labels. Every `outcome` is a client sentence proven verbatim at its paragraph by the script.
- **Speakers.** Every location keeps the key's grammar, "paragraph N, inferred Name (speaker unclear)", with the stamp where the paragraph has one. Two attributions the block introduces are the least certain and are flagged for the user: paragraph 51 ("And put it on the item, not in a log somewhere.") and paragraph 77 ("The actuals are history. My forecast is the job."), both given to the senior PM as the end-user voice. The verifier ignores the name for the paragraph grammar, so neither can mask a miss.
- **Structure.** Work Management only. `build_target` is `own-account`, reason "prospect, so the user's own account by default (A21)", with the fixture's own fact added: v0.1 already lives there and the client's own account is closed to anything real until the security review clears. `workspaces` names the existing v0.1 workspace from context-v0.1.md under A21's continuation clause (a change to v0.1 after the client's feedback on a demo), so no new workspace and no second one; this is the one key where that clause, not the "<client> – product" rule, applies. `native_reuse` is "none: no CRM or Service entity in this build". Four parent-row-with-roll-up patterns (milestones and their date changes; phases and burn; people and allocation rows; startup items).
- **Existing.** `existing.account` lists what v0.1 holds in the user's own account (the portfolio, three projects, the allocation board and its workload view, the dashboard, one automation, sample data only, read-only access for the three attendees) and that the client's Enterprise account is bound to nothing; its migration is a handover question. Nine incumbents with what each stays the record for.
- **Verdict.** `build`: five pain themes have entities and outcomes in the client's own words, the one product is chosen, the structure is a change to v0.1 stated with nine leanings, and the target is named. Nine conditions, starting with the approval stop and the A11 point (none bites for an own-account build; the three A11 decisions stay open), then the continuation workspace, the closed client tenant, the sample burn figures, the unreceived checklists, the three commitments, the inferred speakers and the unbuilt portfolio.
- **Questions.** Five, the ceiling. Reused from the key's pool of fourteen: item 9 (allocation states) is Q1; items 5 and 6 (audit and milestone history) are Q2; item 8 (the Sage upload) is Q3; item 7 (templates) is Q5; Q4 (the project engineer) is new, from leaning 7. Dropped from the five and kept as assumptions with their questions: item 1 (confirm the speakers; routed to the user), items 2 and 3 (the revisit and the director's view), item 4 (the Cumberland view, which the client has answered for now), items 10 and 11 (which account and the IT director's two questions; under A21 the next version stays in the user's own account and the migration moves to handover), item 12 (go-live and the email), item 14 (out-of-scope items). Item 13 (what inconsistent startups cost) is sales material and is left to the key's own list.
- **Left as it is.** `should_plugin_propose_a_build` is `true` and `expected_verdict` is "Nearly ready", which answer the v2 sales question and agree with the block's `build` in direction, so the `note` needs no second sentence. `rubric`, `expected_verdict` and `numbers` are untouched; the contradicted hours and the range stay there as v2 material, and no readiness question spends a slot on them. No R-number, grade, gate name or verdict word is in the block (the script searched for them before writing; the one hit, "a backlog seed", was reworded because the key's own leak list names "seed" as apparatus vocabulary).

## 5. Fields corrected, by field

| field | change | answers |
| --- | --- | --- |
| `integrations_mentioned[0]` | "Sage stays the book of record and must not be rebuilt in monday" reworded to the unresolved-direction wording with our default labelled as ours | never-written rule, weaker form |
| `compliance_or_security_signals[4]` | permission wording attributed to the Consultant, client's words quoted | sweep pattern 4 |
| `requested_changes[8].description` | same | sweep pattern 4 |
| `entities_and_workflows[1]` | "double as success criteria" attributed to our side; the client's test cited | sweep pattern 4 |
| `requested_changes[10].description` | "are being sent" to "committed on the call ... neither has been received" | s21 line |
| `entities_and_workflows[7]` | same | s21 line |
| `integrations_mentioned[4]` | same | s21 line |
| `readiness` | added as the 26th and last field | the brief |

Transcript edits: 0. Key size: 2,021 lines, from 1,104.

## 6. Counts

| item | count |
| --- | --- |
| readiness questions | 5 |
| pains | 15 |
| signals | 7 |
| entities | 29 (18 with a parent, all with `moves_independently`) |
| leanings | 9 |
| element_per_pain | 15 |
| incumbents | 9 |
| assumptions | 17 |
| unmet needs | 8 |
| AI opportunities | 5 |
| verdict conditions | 9 |
| existing fields corrected | 7 |
| transcript edits | 0 |

## 7. Verifier output

`python3 -I fixtures-work/_fixpass/verify_quotes.py fixtures/s9-followup-no-portfolio-unlabelled`, run after the last edit, exit code 0 (the baseline before any edit was 121 pairs, 121 verified, 0 misses):

```
Fixture: s9-followup-no-portfolio-unlabelled
Sources: context-v0.1.md (context, 41 units); transcript.txt (transcript/paragraph, 119 units)

pairs found      169
verified         169  (of which presence only, no location cited: 36)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

The `--json` run lists no location notes. The edit script independently proved 82 quote-at-paragraph pairs (59 distinct) before writing, including the fifteen `outcome` strings and the four read-back quotes inside the question texts, which the shared verifier does not read as quote fields.
