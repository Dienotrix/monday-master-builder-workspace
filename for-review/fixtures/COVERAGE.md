# Fixture set: coverage

Ten call-transcript fixtures for a plugin that helps a solo monday.com consultant run client engagements. The plugin reads the inputs, checks build-readiness, proposes a monday blueprint, builds it in the client's account, and writes demo scripts and SOPs.

Version 1 covers **monday Work Management, CRM and Service**, in English. Dev is out. The design amendments that shape these fixtures are in `design/AMENDMENTS.md`; the ones the keys lean on most are A1 (automations approved as one list), A5 (CRM and Service must use the account's native template boards), A6 (Enterprise plus Work Management gets a portfolio with connected projects by default) and A7 (v1 product scope, with Service extras and pricing/proposal prep deferred).

Fifteen further fixtures, the calibration fixtures s11 to s24 and the document fixture s25, were written at stage 1 (BUILD-PLAN.md WP18) and are listed in the section *Calibration fixtures and the document fixture* below. The user's review of all fifteen closed on 2026-10-13 and the fix pass was applied the same day; the reviewed-set totals in this file are stated as before and the calibration counts are kept beside them.

## README

### What is in each folder

| Folder | Files | Call |
|---|---|---|
| `s1-discovery-strong/` | `transcript.txt`, `answer-key.json` | Strong discovery, architecture and engineering firm |
| `s2-discovery-gaps/` | `transcript.txt`, `answer-key.json` | Weak discovery, pest control and lawn care company |
| `s3-followup-demo-feedback/` | `transcript.txt`, `answer-key.json`, `context-v0.1.md` | v0.1 feedback from the s1 client, one day after the walkthrough |
| `s4-discovery-software/` | `transcript.txt` (WebVTT), `answer-key.json` | Strong discovery that straddles the v1 scope line |
| `s5-intro-thin/` | `transcript.txt`, `answer-key.json` | Thin 12-minute intro call, membership association |
| `s6-discovery-crm-sales/` | `transcript.txt`, `answer-key.json` | Classic sales-team CRM discovery, industrial distributor |
| `s7-discovery-service-desk/` | `transcript.txt` (SRT), `answer-key.json` | Service-desk discovery, facilities maintenance company |
| `s8-discovery-enterprise-pmo/` | `transcript.txt` (WebVTT `<v>`), `answer-key.json` | Enterprise PMO discovery; the portfolio default fires |
| `s9-followup-no-portfolio-unlabelled/` | `transcript.txt`, `answer-key.json`, `context-v0.1.md` | v0.1 feedback from the s8 client; the portfolio default is overridden; no speaker labels |
| `s10-support-checkin/` | `transcript.txt`, `answer-key.json` | Support and check-in call with the s1/s3 client, post sign-off |

`fixtures-work/_work-s1/` ... `_work-s10/` hold per-fixture authoring scratch (drafts, build scripts, per-fixture `check.py`). `fixtures-work/_critic/` holds the set-level audit scripts: `audit.py` (field order, quote validity, objection and role vocabulary), `names3.py` (cross-scenario name-collision scan), `tally.py`, `digest.py`. None of these are fixtures; leave them out of test globs.

**Do not re-run the scratch build scripts.** They write straight to the fixture files from drafts that predate review (`_work-s3/build.py` is the known-bad case: 38 of 187 lines differ), so re-running one silently undoes reviewed fixes and breaks the key's quotes and locations. Use the `check.py` scripts, which are read-only.

### How to use a fixture

Give the plugin `transcript.txt`, then compare its output with `answer-key.json`. Three fixtures are graded cumulatively and need their earlier calls as well:

- **s3** needs the s1 transcript and `context-v0.1.md`.
- **s9** needs the s8 transcript and `context-v0.1.md`.
- **s10** needs the s1 and s3 transcripts. There is no context file for the signed-off v1.0 build; `account_context.existing_monday_setup` describes what exists instead.

### Grader conventions

**Field set.** Every key has the same **25 top-level fields in the same order**, and the same nested shapes:

`scenario_id`, `call_type`, `purpose_of_this_fixture`, `transcript_format`, `company`, `attendees`, `expected_monday_products`, `rubric`, `pains`, `numbers`, `vocabulary`, `entities_and_workflows`, `integrations_mentioned`, `compliance_or_security_signals`, `objections`, `commitments_and_next_steps`, `traps`, `requested_changes`, `should_plugin_propose_a_build`, `expected_questions_before_building`, `expected_verdict`, `account_context`, `expected_structures`, `accepted_behaviours`, `expected_leak_blocklist`. A calibration key (s11 to s25) carries the same 25 in the same order and adds a 26th field, `intake`, after them.

**Quotes.** Every `quote` is an exact substring of that folder's `transcript.txt`, and each sits inside exactly one line, cue or paragraph. **1,294 checked strings**: 1,284 `quote` fields plus 10 `account_context.evidence_quote_or_null`. The calibration set adds 3,073 quote strings on the same basis (recounted after the fix pass of 2026-10-13, readiness blocks included) (every `quote`, `asked_quote` and `evidence_quote_or_null` string, intake block included), each verified at its cited location at stage-1 acceptance; reviewed 2026-10-13.

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|---|---|---|---|---|
| `quote` fields | 174 | 97 | 141 | 120 | 61 | 146 | 144 | 221 | 120 | 60 |

**Locations** follow each transcript's own format:

| Scenario | Location format | Example |
|---|---|---|
| s1, s3 | `HH:MM:SS Speaker Name (role)` | `00:08:56 Jordan Pruitt (Operations Manager)` |
| s2 | `L<line>, Speaker` | `L147, Travis` |
| s4 | `cue N, HH:MM:SS.mmm, Speaker Name` | `cue 79, 00:12:27.888, Colleen Brask` |
| s5 | `HH:MM:SS Speaker Name` | `00:04:04 Jolene Varga` |
| s6 | `[MM:SS] Speaker Name (role)` | `[12:20] Delia Ostrowski (Sales Operations Analyst)` |
| s7 | `cue N, HH:MM:SS,mmm, Speaker Name` (SRT comma) | `cue 20, 00:02:12,520, Tansy Whitlock` |
| s8 | `cue N, HH:MM:SS.mmm, Speaker Name` | `cue 56, 00:07:48.245, Marisol Bettencourt` |
| s9 | `paragraph N, inferred Speaker Name (speaker unclear)` | `paragraph 75, inferred Marisol Bettencourt (speaker unclear)` |
| s10 | `L<line>, Speaker Name (role)` | `L58, Jordan Pruitt (Operations Manager)` |

**Rubric rows.** `criterion` uses the spec names exactly (`R1 Current state mapped` ... `R12 Scope agreed verbally`, and per pain `P# Stated`, `Concrete`, `Workaround`, `Reach`, `Cost inputs`, `Trajectory`). `status` is lowercase `met`, `partial` or `missing`. 323 rows across the set: 229 met, 60 partial, 34 missing. The calibration set adds 468 rows (317 met, 85 partial, 28 missing, 26 met-with-residual, 12 not-obtainable), reviewed 2026-10-13; the two added statuses and the per-row `asked` flag appear in no reviewed key. s10 additionally carries five `Support check 1-5 <spec 6.4 wording>` rows, the only fixture graded with the short support-call instrument.

**Per-pain rows exist only for the pains a key grades**, and the `pains` array is usually longer than the graded set (the ungraded ones are discussed in the R2 note). Graded: s1 P1-P4, s2 P1-P2, s3 P1-P5, s4 P1-P2, s5 P1, s6 P1-P4, s7 P1-P5, s8 P1-P5, s9 P1-P4, s10 P6 (the expansion seed). 33 graded pains, 21 excavated. The calibration set adds 48 graded pains, 37 excavated, reviewed on 2026-10-13.

**Gates.** Each `expected_verdict` names all five spec stages exactly once across `gates_met` and `gates_not_met`, each entry starting with the stage name: `Solution blueprint`, `Build`, `First demo (v0.1)`, `Pricing or proposal prep`, `v1.0 sign-off`. Build and First demo count as met only when the blueprint gate is met, since they add no method requirement of their own.

**Objection `type`** leads with a section 5.2 name, optionally followed by a parenthetical nuance: `Must check with someone (the approver was not on the call)`. Objections with no home in the map are prefixed `Outside the map: `. This is now uniform across all ten keys; the mapping table below counts the leading spec name.

**`decision_role`** uses the spec's role vocabulary (`approver`, `influencer`, `admin/owner`, `end user`), alone or combined, optionally with a parenthetical nuance. Two non-values are used deliberately: `not applicable` for the Consultant in all ten keys, and `unknown` for s5's five-second unidentified interrupter.

**Null quotes.** `numbers.bleed.quote` and `numbers.upside.quote` are null in s5 (both statuses `missing`, no client line applies) and in s10 (both statuses `met`, carried unchanged from s1 with no line on this call restating them). Checkers should skip nulls rather than assume a status from them.

**Consultant-side evidence.** Client-side quotes are what grade a criterion. A handful of rows deliberately cite Consultant lines and say so in the note: s2 R10 (the gap itself), s7/s9/s10 R10 and R12 (a next step or a read-back is the Consultant's own utterance by nature). Never for a Met row resting on disclosure.

**Dates.** No transcript states its own date; all relative dates fit September-December 2026. Chain A: s1 discovery in early September, v0.1 walkthrough Thursday 24 September, s3 on Friday 25 September, scoping Tuesday 29 September, partner meeting Thursday 1 October, v1.0 sign-off Thursday 22 October, s10 on Tuesday 8 December. s4 books Tuesday the 22nd at 1:00 pm Eastern, s5 Tuesday the 22nd at 10:30 Eastern, s6 Wednesday the 23rd at 2:00 pm Eastern, s7 Wednesday the 23rd (time deliberately unfixed), s8 Wednesday the 23rd at 2:00 pm Eastern, s9 around Tuesday 6 October with the next session Thursday 15 October. See the note on the s6/s8 overlap under remaining gaps.

**Naming and fiction.** Client organisations, people, jobs, deals and incidents are fictional. Person and organisation names are **unique across unrelated scenarios**; only the two client chains reuse names on purpose (s1/s3/s10 share Brackenholt and its people, s8/s9 share Bellamy Ridge and its people). `_critic/names3.py` re-checks this. The consultant appears only as `Consultant`, with no personal name, business name or gendered pronoun, and no consulting brand or plugin name appears anywhere. Real places, and real software products used as client tools, are named on purpose so integration detection can be tested: monday.com, Ajera, Bluebeam, Procore, Microsoft 365, Google Workspace, QuickBooks, Redmine, Zendesk, GitHub, Slack, Eventbrite, Trello, Epicor Prophet 21, GoldMine, Sage 300, ServiceChannel, Smartsheet, Power BI.

## What each scenario tests

**s1-discovery-strong -  the positive baseline.** 45-minute discovery with the COO and operations manager of a 120-person A&E firm opening a fourth office. The managing partner, who signs over $25k, is absent. Tests R1-R10 Met from client quotes with R11 Missing and R12 Partial; realistic per-pain gaps (P1-P3 excavated, P4 not); the client's own confirmed $504,920 bleed with unquantified items left out and the overlapping upside never added; client vocabulary (pursuits, jobs, phases, the Wall, owner); Ajera as a must-have whose unknowns become questions; and a CRM-plus-Work-Management blueprint. Account facts are absent on purpose: tier unknown, no usable account, so the portfolio question stays open and CRM must land on native boards once detected.

**s2-discovery-gaps -  the weak discovery.** The consultant pitches before listening, never works out a cost, accepts a vague why-now and closes with "I'll send something over". Tests gap detection (R1-R9 Partial, R10-R12 Missing, nothing Met), inventing no bleed from a single hours figure, and reaching "Nearly ready" while the blueprint gate stays shut so no build or pricing is proposed. Product handling is the v1 test: Work Management for dispatch and rounds, native Service **Tickets** for the intake the consultant kept pitching, with the portal form, email-to-ticket and response targets named as deferred extras, and no CRM after that pitch was deflected.

**s3-followup-demo-feedback -  the iteration call.** The s1 client reacts to v0.1 the day after the walkthrough and the controller joins for the first time. Tests cumulative grading (R11 Partial per pain, P3 and P4 checks closing, a new excavated P5 that leaves the bleed unchanged), a precise 15-item v0.2 change list that keeps backlog asks and non-requests out, the client's exact labels including the "Staff allocation" exception, relayed approver remarks excluded as evidence, a recurring objection and an alternative in play kept internal, and a pricing request held until scope is agreed.

**s4-discovery-software -  the scope line.** Strong discovery at a 200-person B2B SaaS company, as a WebVTT auto-transcript, where the engagement falls on both sides of v1. Tests naming monday Service as in-scope and buildable on native boards, naming monday dev as the best fit for the engineering half and plainly out of v1 (then either a clearly labelled Work Management approximation or a recommendation to wait), not being steered by "projects" or "portfolio view", not proposing CRM after a deflected pitch, R4 Partial on an unconfirmed Consultant rate, and parsing speech-recognition errors.

**s5-intro-thin -  restraint.** A 12-minute intro with a membership coordinator exploring options for an absent executive director. Tests "Not ready" with no gate met, no blueprint or build or pricing, no numbers invented from hedged volumes or idioms, honesty about fit (a better spreadsheet might do), preparation aimed at the real decision maker, and parsing a rough lowercase caption export with an unlabelled interrupter and `[inaudible]` gaps.

**s6-discovery-crm-sales -  the classic CRM engagement.** 42-minute discovery with an 85-person industrial distributor running its pipeline on a 22-tab Excel workbook. The centre of the fixture is vocabulary: they say "prospects" for leads and "opportunities" or "quotes" for deals, and "quote" carries two confirmed meanings. The right answer relabels the account's **native CRM boards**; an abandoned hand-built Prospects board makes the wrong answer feel available. Account facts are stated for the first time in the set (Pro tier, CRM enabled and empty), so the portfolio default must not fire and an enabled product must not be mistaken for an installed native board set. R12 Met opens the pricing gate while v1 keeps pricing out.

**s7-discovery-service-desk -  Service on native boards, extras deferred.** SRT transcript from a 140-person facilities maintenance company on a performance plan with its largest client. They call tickets "work orders" and the IT admin's abandoned monday "work order tracker" is still in the account, so the build is the **native Tickets board relabelled**, never a new look-alike. All three things they most want (customer portal, email-to-ticket, SLA policy setup) are deferred extras the plugin must name as later work while designing a v1 that works without them. Tier is loosely "Standard" and unverified, making plan limits and whether Service is provisioned live preflight questions.

**s8-discovery-enterprise-pmo -  the portfolio default fires.** Hour-long WebVTT call with the PMO of a 400-person healthcare construction firm. "We're on the enterprise plan, work management, about two hundred and twenty seats" is the A6 trigger, so a portfolio with connected projects is included by default, built with the portfolio and project tools rather than plain boards. Tests not quietly deciding the portfolio's shape (portfolio vs programme is a question), an existing account that must be audited rather than assumed away, and the pricing gate opening (R4, R7 and R12 all Met) while the product's own scope keeps pricing out.

**s9-followup-no-portfolio-unlabelled -  the override, and no speaker labels.** Follow-up with the s8 client about ten days after the v0.1 walkthrough. The PMO director takes the portfolio layer back out ("leadership isn't ready"), which is A6's own exception: honour it, remove the layer, keep the projects as real monday projects, and record why with the named revisit condition. A second thread contradicts an earlier number (the PM's four hours a week becomes a measured two and a half), so the bleed falls to unconfirmed and the pricing gate that opened in s8 closes again. The transcript has **no speaker labels at all**, which is what drives R10, R11 and R12 to Partial.

**s10-support-checkin -  after sign-off.** A short two-speaker support call seven weeks after v1.0 sign-off. The reported problem is user error, not a defect or a change request, and the correct handling is diagnosis, explanation and no build. A new need surfaces in passing and must be logged as an expansion seed rather than scoped or priced. Graded with the short support-call instrument; the only fixture where R11 and R12 are Met and all five gates are open, and the only one where the A6 portfolio exception appears as a decision already recorded at scoping.

## Coverage matrices

### Call shape and transcript format

| | s1 | s2 | s3 | s4 | s5 |
|---|---|---|---|---|---|
| `call_type` | discovery | discovery | follow-up-demo-feedback | discovery | intro |
| Client | A&E firm, ~120 staff | Pest and lawn, ~60 techs | Same firm as s1 | B2B SaaS, ~200 staff | Nonprofit association, ~15 staff |
| Client attendees | COO, Ops Manager | CS lead, dispatcher | COO, Ops Mgr, Controller (new) | VP Eng, Support Ops Mgr, PM | Membership coordinator (+ interruption) |
| Approver present | No | No | No (relayed only) | Partly (CFO absent) | No |
| Format | `[HH:MM:SS] Name: text` | `Name: text` paragraphs, no timestamps | `Name (HH:MM:SS): text` | WebVTT cues | lowercase caption export |
| Length | 45 min, 242 turns, ~5,730 words | ~28-30 min, 179 turns, ~3,730 words | 30.5 min, 187 lines, ~3,970 words | 40.6 min, 263 cues, ~5,140 words | 12 min, 75 lines, ~1,640 words |
| Client talk share | 74% | 56% (below target) | 62% | 72% | 66% |
| Longest Consultant stretch | 89 words | 245 words (over proxy) | 103 words | ~100 words over cues | ~52 words |
| Artefacts | `[laughs]`, `[muffled]`, a freeze | `[crosstalk]` x2, `[radio chatter]`, `[inaudible]` | `[laughs]`, `[sighs]` | recognition errors, split cues, `Kraków` | `[inaudible]` x3, "event bright", `Speaker 3` |

| | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|
| `call_type` | discovery | discovery | discovery | follow-up-demo-feedback | support-checkin |
| Client | Industrial distributor, ~85 staff | Facilities maintenance, ~140 staff | Healthcare construction, ~400 staff | Same firm as s8 | Same firm as s1/s3 |
| Client attendees | VP Sales, Sales Ops Analyst, Regional Mgr | Director Client Services, Help Desk Lead, IT Admin | PMO Director, Senior PM, Resource Mgr | Same three as s8 | Ops Manager only |
| Approver present | Yes (holds budget) | Yes for tool, not for money | Yes (holds budget) | Yes | n/a (post sign-off) |
| Format | `[MM:SS] Name: text` | SRT cues (`,mmm`) | WebVTT `<v Name>` voice tags | unlabelled notetaker paragraphs | `Name: text`, no timestamps |
| Length | 42 min, 270 turns, ~5,390 words | 41.5 min, 267 cues, ~5,401 words | ~60 min, 417 cues, ~6,400 words | ~25 min, 119 paragraphs, ~3,485 words | 80 lines, ~1,834 words |
| Client talk share | 67% | 62% | 68% | not computable (no labels) | 63% |
| Longest Consultant stretch | within proxy | 89 words (cue 217) | 110 words / 54 s | not attributable | 56 words |
| Artefacts | `[laughs]` x2, "P twenty-one", weekday vs product | duplicate cue pair 13/14, mis-attributed cue 33, `[inaudible]` | `<v Speaker 2>` x2, duplicate cue 184, overlap 89/90 | no labels at all; run-together paragraphs 55, 60 | `[laughs]`, ` -- ` self-corrections |

### Rubric criteria (R1-R12)

| Criterion | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 | Never reached |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 Current state mapped | Met | Part | Met | Part | Part | Met | Met | Met | Met | Met | missing |
| R2 Pain made concrete | Met | Part | Met | Met | **Miss** | Met | Met | Met | Met | Met | -  |
| R3 Why now | Met | Part | Met | Met | Part | Met | Met | Met | Met | Met | missing |
| R4 Bleed number | Met | Part | Met | Part | **Miss** | Met | Part | Met | Part | Met | -  |
| R5 Upside number | Met | Part | Met | Part | **Miss** | Met | Part | Met | Met | Met | -  |
| R6 Desired outcome | Met | Part | Met | Met | Part | Met | Met | Met | Met | Met | missing |
| R7 Decision process mapped | Met | Part | Met | Met | **Miss** | Met | Met | Met | Met | Met | -  |
| R8 Priority and timing | Met | Part | Met | Met | Part | Met | Met | Met | Met | Met | missing |
| R9 Blockers surfaced | Met | Part | Met | Met | Part | Met | Met | Met | Met | Met | missing |
| R10 Next step committed | Met | **Miss** | Met | Met | Met | Met | Part | Met | Part | Part | -  |
| R11 Solution confirmed | Miss | Miss | Part | Miss | Miss | Miss | Miss | Miss | Part | **Met** | -  |
| R12 Scope agreed verbally | Part | Miss | Part | Part | Miss | **Met** | Part | **Met** | Part | **Met** | -  |

### Per-pain checks

S = Stated, C = Concrete, W = Workaround, R = Reach, $ = Cost inputs, T = Trajectory. A pain is excavated when S, C and W are all Met. 33 graded pains, 21 excavated.

| Pain | S | C | W | R | $ | T | Excavated |
|---|---|---|---|---|---|---|---|
| s1 P1 missed pursuit deadline cost a fee | Met | Met | Met | Met | Met | Met | yes |
| s1 P2 staffing on the Wall | Met | Met | Met | Met | Met | Met | yes |
| s1 P3 fee burn seen too late | Met | Met | Met | Part | Met | Miss | yes |
| s1 P4 submittal reviews slip past contract windows | Met | Met | Part | Met | Part | Miss | no |
| s2 P1 re-treat and callback requests stall | Met | Met | Part | Met | Part | Miss | no |
| s2 P2 dispatcher rebuilds routes | Met | Met | Part | Part | Met | Miss | no |
| s3 P1-P3 (carried from s1; P3's open checks close) | Met | Met | Met | Met | Met | Met | yes |
| s3 P4 (Workaround and Trajectory close) | Met | Met | Met | Met | Part | Met | yes |
| s3 P5 invoice milestones found late (new) | Met | Met | Met | Met | Met | Met | yes |
| s4 P1 escalations | Met | Met | Met | Met | Met | Met | yes |
| s4 P2 SOC 2 change evidence | Met | Met | Part | Met | Met | Met | no |
| s5 P1 general disorganisation | Met | **Miss** | Part | Part | **Miss** | Miss | no |
| s6 P1 no shared pipeline | Met | Met | Met | Met | Met | Met | yes |
| s6 P2 quotes go quiet after five weeks | Met | Met | Met | Met | Met | **Part** | yes |
| s6 P3 account history held personally | Met | Met | Met | Met | Part | Met | yes |
| s6 P4 visit coverage managed from memory | Met | Met | Part | Met | Part | Met | no |
| s7 P1 missed response times | Met | Met | Met | Met | Met | Met | yes |
| s7 P2 monthly service-level report rebuilt by hand | Met | Met | Met | Met | Met | Part | yes |
| s7 P3 escalation is a phone call from the director | Met | Met | Met | Met | Met | Miss | yes |
| s7 P4 double entry with client-owned portals | Met | Met | Part | Met | Met | Miss | no |
| s7 P5 operational knowledge sits with the help desk lead | Met | **Part** | Met | **Miss** | Miss | Miss | no |
| s8 P1 no trustworthy portfolio view | Met | Met | Met | Met | Met | Met | yes |
| s8 P2 resource collisions | Met | Met | Met | Met | Met | Met | yes |
| s8 P3 budget burn seen late | Met | Met | Met | Met | Part | Part | yes |
| s8 P4 no standard project start | Met | Part | Met | Met | Miss | Miss | no |
| s8 P5 warranty calls after turnover | Met | Part | Part | **Miss** | Miss | Miss | no |
| s9 P1 portfolio view (its cost input is contradicted here) | Met | Met | Met | Met | Part | Met | yes |
| s9 P2 request vs commitment on allocation | Met | Met | Met | Met | Met | Met | yes |
| s9 P3 burn unconfirmable (Sage not connected) | Met | Met | Met | Met | Part | Part | yes |
| s9 P4 no standard project start | Met | Part | Met | Met | Miss | Miss | no |
| s10 P6 outside consultant fees (seed) | Met | Met | Part | Part | Part | Miss | no |

Statuses reached per check: **Stated** Met only. **Concrete**, **Reach**, **Cost inputs** and **Trajectory** reach all three. **Workaround** reaches Met and Partial, never Missing.

### Numbers and next step

| | Bleed | Upside | Next step (R10) |
|---|---|---|---|
| s1 | Met: $504,920/yr, client-built and confirmed | Met: ~$283,140/yr billable (overlaps bleed) + $800k-$1.2M fee | Thu 24th, 10:00 Central walkthrough |
| s2 | Partial: one hours input, no cost | Partial: add-on leads, no figure | **Missing** ("I'll send something over") |
| s3 | Met: carried from s1; P5 cash timing excluded | Met: carried from s1 | Tue 29th, 9:30-10:30 Central scoping |
| s4 | Partial: hours only; $120/h placeholder unconfirmed | Partial: offline mode; deal value withheld | Tue 22nd, 1:00 pm Eastern |
| s5 | Missing (`quote` null) | Missing (`quote` null) | Tue 22nd, 10:30 Eastern discovery |
| s6 | Met: $306,520/yr, client-built; Consultant's larger figure refused | Met: ~$275,000 launch-year margin, never added to bleed | Wed 23rd, 2:00 pm Eastern |
| s7 | Partial: 65 h/wk confirmed, rate withdrawn pending CFO | Partial: county contract and freed staff, unvalued | **Partial**: Wed 23rd, no time fixed |
| s8 | Met: $432,080/yr confirmed; $480k overrun excluded | Met: ~$430,000 in two client-figured parts | Wed 23rd, 2:00 pm Eastern |
| s9 | **Partial: contradicted** (4 h/wk -> measured 2.5), now unconfirmed | Met: unchanged, but now carries a dependency | Partial: Thu 15th, 11:30 Eastern |
| s10 | Met: $504,920 carried, `quote` null | Met: carried, `quote` null | Partial: window and owner, no date |

### Verdicts and gates

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Verdict | Discovery complete | Nearly ready | Discovery complete | Nearly ready | Not ready | Discovery complete | Nearly ready | Discovery complete | Nearly ready | Discovery complete |
| Solution blueprint | met | not met | met | met | not met | met | met | met | met | met |
| Build | met | not met | met | met (labelled) | not met | met | met | met | met | met |
| First demo (v0.1) | met | not met | met | met | not met | met | met | met | met | met |
| Pricing or proposal prep | not met | not met | not met | not met | not met | **met** | not met | **met** | **re-closed** | **met** |
| v1.0 sign-off | not met | not met | not met | not met | not met | not met | not met | not met | not met | **met** |
| `should_plugin_propose_a_build` | true | false | true | true | false | true | true | true | true | false |
| Expected main output | Blueprint + v0.1 | Discovery prep; recap with a real time | v0.2 change list; scoping prep | Scope split: Service build, dev named | Discovery prep for the 22nd | CRM blueprint on native boards | Service blueprint, extras on backlog | WM build with portfolio | Revised build, portfolio removed | Explanation, seed logged, no build |

The pricing/proposal gate opens on method grounds in s6, s8 and s10, and closes again in s9. In every case pricing and proposal prep are **still** deferred beyond v1, so the expected behaviour is to say the gate is open, decline to produce a figure or a document, and hand the request to the consultant. s10 is the only fixture where the v1.0 sign-off gate is met.

### monday products and v1 scope

| Product | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Work Management (core) | build | build once gate opens | v0.2 | labelled approximation or wait | tentative | present, out of scope | secondary, confirm | **whole build** | **whole build** | built, live |
| CRM | build (native) | not expected (deflected) | v0.2 (native) | not expected (turned down) | tentative | **whole build** (native) | not expected | conditional, out | conditional, out | built, live (native) |
| Service | -  | **build** (native Tickets) | -  | **build** (native Tickets) | not indicated | not in scope | **whole build** (native Tickets) | parked by client | parked, stays parked | -  |
| Dev | -  | -  | -  | named, **out of v1** | out of v1 | -  | -  | -  | -  | -  |

Deferred items named across the set: **Service extras** (customer portal, email-to-ticket, SLA policy setup) in s2, s4 and s7, with s7 the case where the client pushes back on the deferral; **pricing and proposal prep** in every key; **Dev** in s4 and s5; the **portfolio layer** in s9 (client override) and s10 (left out at scoping, reason recorded).

### Account tier, native boards and the portfolio default

| | Tier | `portfolio_expected` | Native boards required | Look-alike traps |
|---|---|---|---|---|
| s1 | unknown | `null` (undetermined; ask) | 5 CRM: Deals/Opportunities, Accounts, Contacts, Leads, Activities | 7 |
| s2 | unknown | false (no account, no tier) | 1 Service: Tickets | 6 |
| s3 | unknown | false (tier unknown) | 2 CRM: Deals/Opportunities, Accounts | 7 |
| s4 | unknown | false (tier never stated) | 5 Service: two Tickets installs + Incidents, Employee lifecycle, Asset management (conditional) | 6 |
| s5 | unknown | false (no build at all) | none (conditional mapping in notes) | 4 |
| s6 | **Pro** (stated) | false (stated, not Enterprise) | 7 CRM incl. Quotes & Invoices and Products & Services (conditional) | 11 |
| s7 | **Standard** (loose, unverified) | false (tier unverified; WM secondary) | 4 Service incl. Tickets relabelled "Work Orders"; CRM conditional | 12 |
| s8 | **Enterprise** (stated) | **true** (A6 fires) | 2 conditional, both out of this build | 10 |
| s9 | **Enterprise** (re-evidenced) | false (**client override**, reason recorded) | 2 conditional, both out of this build | 12 |
| s10 | **Enterprise** | false (documented exception from scoping) | 3 CRM, already built and live | 6 |

s8 is the only fixture where the A6 default fires. s9 is the only fixture that exercises its exception. s1 is the only key where `portfolio_expected` is `null` rather than a boolean, because the tier is genuinely undetermined and the plugin is expected to ask.

### Objections, by the spec's section 5.2 names

| Spec objection | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Price feels high | - | 2 | - | 1 | 1 | 1 | 1 | - | - | - |
| Needs to think it over | 1 | - | - | - | - | - | - | - | - | - |
| Must check with someone | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 2 | 1 | - |
| Wrong time, next quarter | 1 | 1 | 1 | 3 | 1 | - | 1 | - | 1 | 1 |
| We'll build it ourselves | - | - | - | - | - | 2 | 1 | 1 | - | - |
| Talking to other partners | - | - | 2 | - | 1 | - | 1 | 1 | 1 | - |
| Just send a proposal or pricing | - | - | 1 | - | 1 | 1 | 1 | 1 | 1 | - |
| monday itself is the problem | - | - | - | - | - | 1 | 2 | 1 | 1 | - |
| Team won't adopt it | 3 | 3 | - | 1 | 1 | 1 | 2 | 2 | 2 | 1 |
| Outside the map | - | 9 | 2 | - | 2 | - | - | - | 1 | - |
| **Total** | **7** | **16** | **8** | **7** | **8** | **7** | **10** | **8** | **8** | **2** |

81 objections in all. The calibration set adds 131, reviewed. Statuses covered: anticipated (s1, s2, s4, s5, s6), raised, answered on the call (s4, s6, s7, s8, s9), resolved from the client's own evidence (s6, s8), and recurring (s3, s9).

### Traps (281)

Exact counts per key:

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `traps` | 33 | 27 | 29 | 24 | 24 | 26 | 35 | 31 | 31 | 21 | **281** |

The calibration set adds 432 traps, 95 of them look-alike traps, reviewed.

The recurring themes, with examples of where they are exercised (not an exhaustive index):

- **Client vocabulary and ambiguous terms** -  "owner" is the building owner (s1); "callback" and "service ticket" mean two things (s2); "prospect"/"quote" are leads and deals (s6); "work order" is a ticket and "PM" is preventive maintenance (s7); "portfolio" vs "program", "the board" is the executive committee (s8, s9); "consultants" are outside engineering firms (s10).
- **Native-board and look-alike enforcement** -  81 look-alike traps across the set; the sharpest are an abandoned hand-built Prospects board (s6) and an abandoned "work order tracker" (s7) that both make the wrong answer feel available.
- **Portfolio default and its exceptions** -  every key records why a portfolio is or is not expected: tier unknown (s1-s5), stated non-Enterprise (s6, s7), the default firing (s8), a client override (s9), a documented scoping exception (s10).
- **Deferred scope** -  Service extras that the client actively wants (s2, s4, s7); Dev named but not built (s4); pricing and proposal prep held even when the gate is open (s6, s8, s10).
- **Bleed and upside discipline** -  loaded vs bill rates and no adding overlapping upside (s1); no bleed from one hours figure (s2); unconfirmed Consultant rate (s4, s7); a launch-year figure that is not annual (s6); a contradicted input that must supersede rather than merge (s9).
- **Loose, hedged or self-corrected numbers** -  "forty-ish" vs "more like fifty" (s4); "a couple thousand members" (s5); "thirty-eight, forty depending on how you count" (s8).
- **Consultant words are not evidence** -  the $120/h placeholder (s4), platform claims (s2), the four-part first cut being the Consultant's framing (s7), arithmetic spoken aloud over client-supplied inputs (s8).
- **Integrations and systems of record** -  Ajera one-way and read-only (s1, s3, s10); "the system" stays (s2); Zendesk stays (s4); Prophet 21 gated by an outsourced IT provider (s6); Procore and Sage 300 stay (s8, s9).
- **Data modelling** -  one project with several jobs and phases that vary by job type (s1); several milestones per phase (s3); a work order belongs to a building, not a client (s7); three project templates, not one (s8).
- **Grading boundaries and gate discipline** -  R12 Partial despite "the right first cut" (s1); R10 Partial with a day but no time (s7); the gate that opens then closes (s8 -> s9).
- **Absent, tentative or secondhand stakeholders** -  relayed approver remarks (s3); an absent CFO (s4, s7); the executive director known only secondhand (s5); and the inverse case where the approver is present and holds the budget (s6, s8).
- **Dates and relative timing** -  no transcript states its own date; two different fifteenths (s9); "next quarter" must not be resolved into a date (s9).
- **Internal-only, privacy, PII and security** -  remarks about colleagues in every key; customer PII (s4); no patient information (s7, s8); restricted rates and margins (s1, s3, s6, s8).
- **Transcript artefacts and attribution** -  recognition errors (s4); `Speaker 3` (s5); duplicated and mis-attributed cues (s7, s8); no speaker labels at all (s9).
- **Change-request precision** -  keeping backlog asks, open questions and non-requests out of the change list (s3, s9).
- **Automations as one approval list** -  A1, with the caveat that API-created automations cannot be switched off through the API, appears in s1, s2, s3, s5, s7, s8 and s9.

### Requested changes

| | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 | s9 | s10 |
|---|---|---|---|---|---|---|---|---|---|---|
| add / change / remove | 1/2/0 | 0/0/0 | 7/6/2 | 2/0/0 | 0/0/0 | 2/4/0 | 2/4/0 | 2/2/1 | 8/4/2 | 0/0/0 |
| Nature | pre-build requirements | none (hedges are not requests) | v0.2 change list | first-demo asks | none (no build) | pre-build requirements | pre-build and sequencing requirements | pre-build requirements and one exclusion | the portfolio override plus v0.2 revisions | none (client housekeeping only) |

51 requested changes in all. The calibration set adds 80 (31 add, 42 change, 7 remove), reviewed. The two follow-up calls (s3, s9) carry 29 of them; the three fixtures with no build (s2, s5, s10) carry none by design.

### Leak-check block lists

Every key carries `expected_leak_blocklist` (158 entries: 21, 15, 14, 15, 10, 19, 14, 16, 15, 19). The calibration set adds 242 entries, reviewed. The recurring classes are bleed and upside totals and components in numeric, comma, `$`, `k` and spoken-word forms; loaded rates and cost inputs; write-off, loss and threshold amounts; objection text; stakeholder assessments; remarks about colleagues; failure narratives; alternatives in play; method vocabulary, pain IDs and evidence markers; and customer or member PII.

Two deliberate non-removals recur and are worth grading for: **flag, do not remove** groups for legitimate volume and process facts that belong in an SOP (s1, s5, s6, s10), and **CAUTION** entries where a blocked word is also the client's own vocabulary and must survive (s2's "callback"). s5's list is the inverse case: no figure exists, so any figure is by definition invented.

### Integrations and compliance signals

| | Integrations | Compliance and security |
|---|---|---|
| s1 | Ajera must-have (hosting, API unknown); Procore via GCs; bid portals | Microsoft SSO; rates confidential; justice-job access limits; public records requests |
| s2 | "the system" (name unknown), QuickBooks, Google Sheet, owner's cell | State pesticide application records; medical notify list; gate and lockbox codes |
| s3 | Ajera one-way, read-only, in writing; API unconfirmed | Milestone amounts restricted; burn at billing rates; IT provider gate |
| s4 | GitHub and Slack must-have; Zendesk link; Redmine migration | SOC 2, audit logs, vendor review, DPA, customer PII, Google SSO |
| s5 | Membership database (name inaudible), Eventbrite, web form | Member personal data; licence and CE credit data; nonprofit board approval |
| s6 | Epicor Prophet 21 must-have, gated by outsourced IT; GoldMine legacy | Contract pricing and cross-customer margin confidential; pricing matrix stays in the ERP |
| s7 | Microsoft 365; ServiceChannel and a second client portal; Sage 300 | Healthcare site badging, nothing about patients in notes; contract terms confidential |
| s8 | Procore stays; Sage 300 gated by the controller; Microsoft SSO | No patient information or photos; immunization records with HR; ICRA expiry; audit trail |
| s9 | Sage 300 answered: no live connection this year, monthly upload | Security questionnaire half done; nothing in the client tenant yet; health-status audit trail |
| s10 | Ajera weekly one-way import live; nothing writes back | Milestone amounts restricted; Microsoft sign-in on the Enterprise plan |

## Calibration fixtures and the document fixture (s11 to s25)

Fifteen further fixtures, written at stage 1 by WP18 to the rows of BUILD-PLAN.md section 4.2 and the parameters of REAL-CALL-LESSONS.md section 6, each in its own folder with a `README.md` that states what it plants, its counts and its review history. Fourteen are calibration fixtures: each is written to its section 4.2 row and its lessons row and to nothing else, and its key asserts the repair, not only the reading. The fifteenth, s25, is the document fixture of A16: three client documents and one short call. Every key carries the 25 reviewed fields in the s1 order and a 26th, `intake`, asserting the repair. The counts on each row are the README's, re-measured from the key at stage-1 acceptance (`tests/stage1-acceptance-fixtures.md` in the repo) with no difference found; they are to be checked against the grader's totals when WP14 lands. The user's review of all fifteen closed on 2026-10-13; the fix pass was applied the same day, and each folder's README records what changed.

| Fixture | Label | Files | Lessons row | Reversal guarded | Rubric rows (met / partial / missing / met-with-residual / not-obtainable) | Pains graded (excavated) | Objections | Traps (look-alike) | Leak entries | Requested changes (add / change / remove) | Quote strings | Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `s11-demo-composite/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C56 | R19 | 24 (9 / 13 / 1 / 1 / 0) | 2 (1) | 8 | 22 (4) | 13 | 5 (1 / 3 / 1) | 151 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s12-header-present/` | calibration fixture | `transcript.txt`, `meeting-chat.txt`, `answer-key.json`, `README.md` | C57 (a) | none | 36 (24 / 6 / 3 / 2 / 1) | 4 (3) | 9 | 32 (6) | 16 | 4 (2 / 2 / 0) | 199 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s13-header-absent/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C57 (b) | none | 30 (22 / 4 / 2 / 1 / 1) | 3 (2) | 8 | 29 (6) | 16 | 5 (3 / 1 / 1) | 195 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s14-shred-block/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C58 (a) | none | 36 (27 / 3 / 3 / 2 / 1) | 4 (3) | 12 | 30 (7) | 15 | 7 (2 / 4 / 1) | 191 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s15-shred-dense/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C58 (b) | R8 | 24 (18 / 2 / 1 / 2 / 1) | 2 (2) | 8 | 30 (6) | 16 | 5 (1 / 4 / 0) | 209 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s16-shred-cue/` | calibration fixture | `transcript.txt` (WebVTT), `answer-key.json`, `README.md` | C58 (c) | R2 | 24 (18 / 2 / 2 / 1 / 1) | 2 (2) | 7 | 26 (6) | 14 | 4 (1 / 3 / 0) | 162 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s17-no-markers/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C59 | none | 30 (21 / 6 / 2 / 1 / 0) | 3 (2) | 8 | 27 (6) | 14 | 5 (2 / 3 / 0) | 160 | reviewed 2026-10-10; fix pass applied 2026-10-13 |
| `s18-identity-collapse/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C60 | none | 36 (23 / 7 / 2 / 3 / 1) | 4 (2) | 12 | 28 (7) | 15 | 6 (3 / 2 / 1) | 163 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s19-reverse-demo/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C62 | R3, R14 | 36 (22 / 7 / 3 / 3 / 1) | 4 (3) | 8 | 26 (9) | 15 | 7 (4 / 2 / 1) | 233 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s20-large-group/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C63 | R6 | 36 (27 / 5 / 1 / 2 / 1) | 4 (4) | 9 | 28 (6) | 19 | 3 (1 / 2 / 0) | 278 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s21-existing-account/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C64 | R4, R9 | 24 (16 / 6 / 0 / 1 / 1) | 2 (2) | 7 | 30 (5) | 19 | 5 (1 / 3 / 1) | 191 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s22-degrading-commitment/` | calibration fixture | `transcript-1.txt`, `transcript-2.txt`, `answer-key.json`, `README.md` | C65 | none | 36 (27 / 5 / 2 / 1 / 1) | 4 (3) | 8 | 30 (6) | 18 | 4 (2 / 2 / 0) | 263 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s23-symmetric-shred/` | calibration fixture | `transcript.txt`, `answer-key.json`, `README.md` | C104 | R5's companion measure | 36 (27 / 4 / 3 / 1 / 1) | 4 (3) | 8 | 28 (7) | 15 | 6 (2 / 4 / 0) | 198 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s24-package/` | calibration fixture | `rec-4397-production-walkthrough.txt`, `rec-4402-first-look.txt`, `rec-4409-pricing.txt`, `rec-4418-discovery.txt`, `rec-4431-internal-review.txt`, `answer-key.json`, `README.md` | A15 (no lessons row) | R6, R7 | 36 (25 / 7 / 2 / 2 / 0) | 4 (3) | 12 | 30 (8) | 19 | 9 (3 / 5 / 1) | 313 | reviewed 2026-10-13; fix pass applied 2026-10-13 |
| `s25-client-documents/` | the document fixture | `QP-07-sample-receipt-testing-certification-v3.2.docx`, `QP-07-F1-sample-flow.png`, `sample-tracking-what-we-need.pdf`, `transcript.txt`, `answer-key.json`, `README.md` | A16 (no lessons row) | none | 24 (11 / 8 / 1 / 3 / 1) | 2 (2) | 7 | 36 (6) | 18 | 5 (3 / 2 / 0) | 167 | reviewed 2026-10-13; fix pass applied 2026-10-13 |

Calibration set totals after the user's review and the fix pass of 2026-10-13: 468 rubric rows (317 met, 85 partial, 28 missing, 26 met-with-residual, 12 not-obtainable; the rubric is v2 and was not edited); 48 graded pains, 37 excavated; 131 objections; 432 traps, 95 of them look-alike traps; 242 leak-blocklist entries; 80 requested changes (31 add, 42 change, 7 remove); 3,073 quote strings, the readiness blocks included. Quote strings are counted on one basis for every key: every non-null `quote`, `asked_quote` and `account_context.evidence_quote_or_null` string, the intake block included, which is why a row can differ by a few from the README's own count, whose basis the README states.

**How to use them.** Every fixture is graded once, on its own, except where its README says otherwise: s12 takes `transcript.txt` and `meeting-chat.txt` as one meeting; s22 takes its two transcripts as a pair, in the order internal evidence gives (call 1 then call 2); s24 takes its five recordings as a package, ordered by the dates inside the files and never by their names, with the same-day pair broken by internal evidence; s25 takes its three documents and its call as one client's inputs and is run twice, documents first and call first, to the same end state (H56). The `fixtures-work/_work-sNN/` scratch folders some READMEs mention are authoring scratch, as for s1 to s10: never re-run, never in test globs.

**Location formats** follow each file's own grammar and are stated in each README: a stamp plus speaker (`MM:SS Speaker Name (role)` in s11; `HH:MM:SS Speaker Name (role)` in s12, s18 to s21 and s25's call; `MM:SS Speaker Name` in s13); a line reference (`L<line>, M:SS Label` in s14; `L<n>, M:SS, <label>` or `L<a>-<b>, M:SS, <person> (merged run)` in s15; `L<line>, HH:MM:SS Label` in s23); a unit reference (`cue N, HH:MM:SS.mmm, Label` or `cues N-M, ...` in s16; `turn N, MM:SS, Speaker Name` in s17); a file prefix (`chat HH:MM:SS Name` in s12; `call N, HH:MM:SS Speaker Name (role)` in s22; `rec-NNNN, mm:ss Speaker Name (role)` in s24); and a document reference in s25 (`QP-07 section N.N`, `QP-07 front page`, `write-up p.N section N`, `figure 1 p.1`), never a speaker.

**Statuses.** Every calibration key uses `met-with-residual` and the per-row `asked` flag (with an `asked_quote` where it is true; s15 leaves the flag off six rows on purpose), and twelve use `not-obtainable`. No key carries a positive `advisory` row: every call type in the set resolves, as BUILD-PLAN.md section 4.3 (item 8) states, so the value's positive case is that section's constructed unresolvable fragment (H50) and not a fixture; s25 asserts the value's absence in a document-only pass. The READMEs that said another calibration fixture carries the case were corrected at stage-1 acceptance.

**Type headers.** Every calibration key's `intake.type_header` (per file in s24, per call in s22) carries the tokens `shared/record-map.md` pins for the four dimensions and the two modifiers (`partner-led`, `new-logo`, `no-show`, `configured-structure`, `small-group`, `not-live` and the rest), with the fixture's reasoning in a `_note` beside each field; the segment values use the same tokens. They were re-spelled from the ARCHITECTURE.md 8.3 step 5 prose at stage-1 acceptance, because `record-map.md` is the pinned home of the vocabulary and `transcript_prep.py` embeds those tokens.

## Remaining gaps

**Statuses never reached.** R1, R3, R6, R8 and R9 are never Missing. Per pain, **Stated** is always Met and **Workaround** is never Missing. No bleed is built from a range and then confirmed.

**Call types still missing.** There is no transcript of a **first-demo or sign-off demo** (both exist only as context files or carried notes), no **scoping or pricing call**, no **working session**, and no **v1.x expansion call** that takes a logged seed forward. s10 creates the expansion seed but deliberately stops there.

**Method scenarios not covered.**
- Research or `[inferred]` input feeding objection anticipation.
- A prior `discovery.md` supplied as input rather than reconstructed from transcripts.
- A **Consultant override of a gate actually exercised on a call** (s2 and s9 describe the correct handling of an override in their notes, but no transcript contains one).
- A bleed smaller than the likely engagement cost, which the spec says to flag as a fit question.
- A multi-file call, or two transcripts of the same meeting to reconcile.

**Objection coverage.** "Needs to think it over" appears once (s1, as a soft hedge) and never as a stated objection after a proposal. No price objection follows a stated price -  arguably permanent, since pricing is deferred beyond v1.

**Client-facing output checks.** The keys now carry leak block lists, but no key carries an expected **demo-script, recap or SOP outline** to grade structure against.

**Native-board detection.** No fixture can supply real board ids, because no fixture has a live account to detect against. Every native-board expectation is therefore an entity-level requirement plus a preflight instruction, and the detection step itself stays untested here; a live test is where that belongs.

**Known calendar overlap.** s6, s7 and s8 all book their next meeting on **Wednesday the 23rd**, and s6 and s8 name the identical slot (2:00 pm Eastern). Each is a separate client and no plugin run sees two at once, so nothing inside a fixture is wrong, but the set no longer represents one coherent consultant calendar. Fixing it would mean editing a booked time in two reviewed transcripts and their keys; it is recorded here instead.

**Convention deviations worth knowing.** s1 is the only key, reviewed or calibration, with `portfolio_expected: null`; s24, which also has no account and no tier, carries `false` under the s2 convention with the previous seller's tier proposal held as her claim (changed from `null` at stage-1 acceptance; the user's review kept it). s10 is the only key with null `numbers` quotes at `met` status, and the only one whose rubric carries `Support check` rows. s5 is the only key using `unknown` as a `decision_role`.
