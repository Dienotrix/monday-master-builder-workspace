# DelOps Method Spec (for monday Master Builder)

Research dossier, 2026-09-10; revised 2026-09-12 against the real-call calibration (`design/REAL-CALL-LESSONS.md`, C1-C125) and amendments A12 to A16 (`design/AMENDMENTS.md`, which overrides this file wherever they conflict). Input for the plugin's method skill, templates, and checks. Written fresh; nothing here is copied from the source documents or from any earlier plugin. Section numbers are cited by the lessons file and by `design/ARCHITECTURE.md` and do not change; new material is appended inside its section (2.6, 4.11, 4.12, 6.6, 7.1). Where the written method and observed practice disagree, the text says which wins and why. Nothing here settles an A11 decision.

## 0. Basis and ground rules

- **Source.** the user's own sales playbook (v1) and master call checklist, written for a previous employer, distilled and rebranded for DelOps. Removed: the previous company name, its hourly rate and deal-size figures, client-count and track-record claims, team-management material (manager reviews, peer comparisons, rep development cadence), and references to a CRM and a call-recording product. The client record replaces the CRM.
- **Influence.** The question-led approach draws on NEPQ, a published question-led sales method. Credit the method as an influence only (for example one line in the README), never by its author's name. Plugin text must not reproduce its stage names, tone lists, scripts, or terminology.
- **No scripts.** Plugin text holds principles, checks, and short example phrasings. No long scripts or dialogues. The phrasings in this spec are original and meant to be adapted to the user's voice (4.12).
- **No claims.** Plugin text and generated material make no claims about DelOps — client counts, success rates, case studies, other-client anecdotes, sector-experience claims ("we have worked with many companies in your sector"), or demand statistics about our own book ("that is one of our most requested things") — unless the user supplies and approves them. The ban covers the self-introduction, which is where such a claim lands by default in every generated opening; none of these shapes names a client, so a proper-noun blocklist passes all of them and the rule has to be authored in. The substitute, in a room where our side is a stranger, is one verifiable credential: a certification, a listed status, a named reference the client may contact. What substitutes in a seat where no third party can vouch is open (11).
- **Tone of skill text.** The source documents are emphatic (capitals, "mandatory", "non-negotiable"). Translate every rule into a calm, specific statement.
- **Internal vocabulary** used below (never client-facing):
  - *Pain (P#)*: a problem the client described in their own words.
  - *Bleed*: the yearly cost of keeping the current state, worked out with the client.
  - *Upside*: what fixing it would unlock, in the client's own figures.
  - *Callback*: opening a demo segment by pointing back to a stated pain.
  - *Exit ramp*: the point where the user stops showing and moves to the close.
  - *Named check-in / open check-in*: the two check-in instruments (4.3, step 4). Only the first is recordable as a confirmation.
  - *Confirmation ledger*: the per-pain record of client ties confirmed back by the presenter during a demo (4.3), read by the close and by R11.
  - *Mechanism*: a next step delivered as a booking mechanism with a named owner, as distinct from a promise to find times.
  - *Structure inventory*: the record of what a client showed us of their own build (2.6).
  - *Strand*: one piece of work inside a client's record (A14). *Set*: a package of calls taken in together (A15).
  - *[found] / [inferred]*: taken from a transcript vs inferred from research or reasoning. These are this document's names for the record's `[Q]` and `[I]` markers; the full marker set, including `[Q?]` unclear speaker, `[Q/side]` side-only, `[Q/recon]` reconstruction and `[X]` quarantined, is the architecture's (§7.5).

## 1. Core principles

1. **Diagnose before prescribing.** No demo before discovery, no price before a bleed number, no proposal before the client has agreed the scope out loud.
2. **The client's words make the case.** Their statements and numbers outweigh anything the user or Claude asserts. Quotes are recorded verbatim.
3. **Ask, listen, stay with the problem.** In discovery the client does most of the talking (target 60% or more). When they describe a pain, explore it further before offering a fix. Pressure creates resistance. This holds while the client walks their current state; when they walk a candidate solution they built themselves, interrogating it hard is the work and silence is the defect (2.5).
4. **Put a price on doing nothing.** Work out the bleed together; where it fits, also the upside.
5. **Everything shown or built traces to a stated pain.** Anything else goes to the backlog, not the demo.
6. **A demo is a conversation.** Short showings, a check-in after each, stop once they are convinced, end with a commitment question rather than a summary. The close is a separate discipline that good delivery does not produce on its own (4.6).
7. **Most objections are a skipped step.** Prevent them by running the step early; when one surfaces anyway, stay curious and never defensive.
8. **Trusted expert, not order taker.** Guide the conversation, and say so when the current setup only needs a small fix.
9. **Every meeting ends with a next step the client assented to.** A date, time and owner where the room can fix one; on a working session or an expansion call, a booking mechanism with a named owner and a stated purpose counts (2.3, R10). A promise to send something over is neither. Every support call ends with one forward-looking question about what is still manual.
10. **Internal sales thinking never reaches client-facing material** — or a shared screen (7).
11. **What is said aloud is held to the rule for what is written.** No figure without a source, no capability without a probe, no estimate for work nobody has read, and a correction made in the next meeting for anything said wrong (7.1).

## 2. Discovery readiness rubric

### 2.1 Grading rules

- **Input:** every call the strand serves — transcripts and summaries live at record level in `calls/`, while `discovery.md` is per strand (A14) — any client document taken in as an input (A16), and the previous `discovery.md`. `research/` supplies context only. A package of calls handed over at once is graded once, as a set, after the whole set is in the record (6.6); one call alone is the common case, and nothing here waits for a second.
- **Scope:** graded per pain (2.2), for the engagement as a whole (2.3), and per typed segment where a call changed type part-way (2.6): the last third of a demo that turned into discovery is harvested as discovery, not as demo reactions. An account running two discovery threads in parallel — two sponsors, two pieces of work — is graded per thread, each thread a strand, and the record shows the threads side by side rather than one verdict averaging them (architecture §3.3). Each run records which calls and documents it covered, by sequence rather than by file name.
- **Status values:**
  - *Met*: at least one client-side verbatim quote satisfies the definition.
  - *Met-with-residual*: a compound criterion whose elements are Met except one; the missing element becomes a gap question instead of vanishing into a one-word grade. Every compound criterion is graded element by element, the elements are shown, and the weakest is reported.
  - *Partial*: present but short of the definition (vague, an unconfirmed range, a figure our side proposed that the client did not clearly confirm, speaker unclear, side-only evidence).
  - *Missing*: nothing in the inputs.
  - *Not obtainable from this room*: nothing in the inputs, and the role that could supply it was not present; the grade names that role (2.3, obtainability map) and routes to a room change rather than to the same question again.
  - *Advisory*: a type-specific criterion on a call whose type could not be resolved (2.6). It carries its question, counts for nothing in the verdict or any gate, and is regraded once the user confirms the type.
  - *Not applicable*: the user marks it with a reason; the reason goes to `log.md`.
- **Asked? flag:** every criterion and every per-pain check records whether our side asked, with the attempted question quoted where one exists. "We never asked" and "they would not say" grade the same and need different prep: a dodged item needs a different room, person or framing, not the same question twice. Cost inputs and trajectory are marked ask-only — they are volunteered when the person who does the work is in the room and otherwise arrive only when asked.
- **Evidence format:** quote, speaker (name, role, side), the check or element it satisfies, file, location (timestamp or cue range if present, otherwise line range), marker, intake confidence. Example:
  `"She loses most of Friday rebuilding that report." (operations lead, client side) calls/2026-09-03-discovery.transcript.txt L142-L144 [found] certain`
  Intake assigns each utterance one of four confidence states (certain, probable, uncertain, unattributable) and the worst state travels to any pain, number or requirement derived from it. Material the client sent before a call — a document, a deck, a prototype link — is cited `[pre-read]` with who sent it and whether our side acknowledged it on the call (provisional, one observation). A client document taken in as an input is cited by document and section or page, never by speaker, with its author, date and status (draft, approved, current practice, desired state) recorded and each marked unknown when the document does not say; where the author is unknown the tier is "the client's document", one step below an attributed quote (A16).
- Only **[found] client-side** evidence, or a client document that states the thing explicitly, can make an item Met. [inferred] items are shown but count as Missing for gates; they can shape questions. Side-only evidence — "a participant on the client side", where the speaker cannot be resolved — grades Partial and never Missing.
- **Non-evidence.** None of the following counts, for any criterion: our own framing and recaps; backchannel tokens ("right", "mm"); agreement that answers a meeting proposal rather than a substantive claim; a feature request phrased as a question; any date or figure our side supplied, including a figure elicited by our own leading band ("it shouldn't be more than that, though?"), which is our figure and not a client input; a client figure re-quoted second-hand by a seller who handed the package over (A15); and a client assent swallowed inside our own turn, which is permanently unprovable and is re-asked in the next call, naming the person. For R11 and R12 a backchannel counts as nothing rather than Partial, and the evidence quote is paired with the line it answers so an agreement cannot float free of its antecedent. Two carve-outs, stated here so a grader does not have to find them: a closed factual yes or no answering our own leading question is evidence *of the fact* but not *of their framing*, and is recorded with the question it answers; and R10 is asymmetric — the date or mechanism we proposed and the client assented to is the one admissible piece of our-side evidence there is.
- **Several client voices.** A pain may be excavated across speakers — one states it, another prices the effort, a third quantifies the workaround's failure — provided they work in the same process, with the speaker recorded per check rather than per pain. Where a criterion is about behaviour or attitude, quote the whole turn. A proposition about one client speaker's work, supplied by a different client speaker and confirmed only with a token, is capped at Partial and records both speakers (provisional).
- **Conflicts.** The most recent client statement wins only for a factual conflict about the same proposition, from the same speaker, inside one call; then the superseded value and date go to `log.md`. Every other pair is kept as both statements with call, speaker and location, marked unresolved, and raised as a gap question: two speakers on one call; the same speaker giving two accounts of one fact — restricted to assertion classes a follow-up message would repeat back (who attended a prior meeting, a plan or tier, a figure stated two ways, an owner named two ways), never time-of-day remarks, which surface transcription noise and train the user to ignore the list; two calls, where no recency rule applies (A15); and a document against a call, which is a finding in its own right and often the best callback material there is (A16). Two figures minutes apart that may price different line items are recorded as a pair with the relationship unresolved and no arithmetic between them. Two speakers who agree on the facts but need different structures are not in conflict: that is a **fork**, carried as an open option in the blueprint (architecture §3.4), and recency must not resolve it. A requirement re-engineered by consensus inside one call is not a conflict either; its mechanism history is kept (2.3, R1).
- **No or unreliable speaker labels:** mark evidence "speaker unclear", grade Partial until the user confirms. Grading is per turn, not per file: one repaired block caps its own evidence at Partial until a human confirms the speaker and does not down-grade the whole transcript. Absence of artifact markers is not evidence of a clean file — zero markers together with shred or composite signals *raises* the doubt level, because the clean-looking export is the one that assigns a confident label to every fragment.

### 2.2 Per-pain checks (run for every pain P#)

| Check | Met when the client... | If missing or partial, add to next prep (example phrasing) |
|---|---|---|
| Stated | describes the problem in their own words | (defines the pain; no P# without it) |
| Concrete | gives a specific recent occurrence, or describes what it looks like day to day (what, who, how often) | "When did that last come up? What happened?" |
| Workaround | names what they do today and why carrying on that way is not acceptable | "What stops you from carrying on with the current workaround?" |
| Reach | says who else it affects and how | "Who else ends up dealing with this?" |
| Cost inputs (ask-only) | attaches hours, headcount, frequency, errors, or lost revenue | "Across everyone involved, roughly how many hours a week go into this?" — to the person who does the work |
| Trajectory (ask-only) | says what happens to it in a year, or as they grow, if nothing changes | "Say this stays as it is. What does next year look like?" |

A pain with Stated, Concrete and Workaround all Met counts as **excavated**; the three may come from different client speakers in the same process (2.1). The method runs the full sequence on every pain, but only one excavated pain is required for R2.

A figure the client scopes to the pain in the same clause needs no separate attribution quote where the referent is explicit. Where the referent is a pointer — "that", "this one", "the thing we showed you" — record what it resolves to and how, and the check cannot exceed Partial until confirmed with the person who performs the work; otherwise the pronoun resolves to the wrong noun and the bleed is built on the cost of doing the work rather than the cost of the pain. A total-effort or total-spend figure is never a cost input unless the client attributes a portion of it to the pain, and that quote is required. Cost inputs are obtained in proportion to how narrow and countable the unit of work is: on a working session with the operator present they arrive as a by-product of the scoping argument, with no cost question asked.

### 2.3 Engagement criteria

| ID | Criterion | Met when | Evidence to record | If missing or partial | Weight |
|---|---|---|---|---|---|
| R1 | Current state mapped | Client has described the process end to end, the tools and how they connect (or don't), who touches it, time spent on their own process and time spent maintaining the platform (two elements, Met on either, the record showing which), what monday does today and who built it | Quotes per element; `[pre-read]` material and client documents can satisfy elements; where the client showed us their build, the structure inventory (2.6) with observed-only rows recorded as unconfirmed; research adds [inferred] context; a requirement re-engineered by consensus on a call keeps its mechanism history | Walkthrough question for the unmapped element; blueprint lists assumptions to confirm | Gate: blueprint |
| R2 | Pain made concrete | At least one pain is excavated (2.2) | Pain IDs and quotes, speaker per check | Per-pain questions for the top pain | Core |
| R3 | Why now | Three client-side elements — what changed, a trigger event, a clock. Met on change plus at least one other. A date our side supplied and a trigger event our side initiated (our own outreach) are excluded: a prospect who merely answered a call would otherwise grade Met with no urgency at all | Quote per element, dates. Our own commercial clock — a renewal, a quarter end, any constraint on our side — is recorded and front-paged separately as an owned to-do, never as client hesitancy, and excluded from the grade | "What's made this matter now rather than last year?" Anticipate timing and think-it-over objections | Core |
| R4 | Bleed number | Yearly (or monthly) cost of the current state, built from client-supplied inputs, math written out, total confirmed by the client. Three states sit below Met: `[unpriced]` (volume and frequency in place, the rate slot empty), "cost not measurable from their record" (the client says their own tracking data is untrue), and "effort-quantified, rate pending" (volume, frequency and an effort rate exist; a multiplier and an internal rate are missing). Scale is reported as a filled section even when the bleed is Missing, naming the missing multiplier, so the verdict can read "scale established, cost not priced" rather than an unqualified Missing on a rich call | Input quotes, math, confirmation quote; the per-pain cost check reported apart from the engagement-level bleed, since the two diverge routinely | Missing inputs become one targeted question to the person who does the work, not a re-planned conversation; pricing prep is held; anticipate the price objection | Core |
| R5 | Upside number | Freed capacity converted to value with the client's figures, and the client names something they want to do but cannot today | Quotes, math | Where it fits: "If that time went into selling, what would it add up to in a month?" then "Is there something you'd go after if capacity weren't the limit?" | Advisory |
| R6 | Desired outcome | Client describes what solved looks like day to day and what their leadership would count as a win | Quotes, turned into draft success criteria | "Imagine this is running well by spring. What's different in a normal week?" Blueprint marks success criteria as proposed | Gate: v1.0 |
| R7 | Decision process mapped | Who is involved, their roles, what each cares about, who approves spend, what happens after a yes, prior budgeting experience — recorded as a delegation graph where the room described one: delegate, gate-holder, gate condition, re-entry trigger, standing conditions. "Run it, but I want to be in on the approvals" is one sentence and the whole decision structure of an engagement, and a flat role list cannot hold it | Per-stakeholder quotes; the graph | "Who else has a say, and what will they want to see?" Recommend inviting the approver; anticipate the check-with-someone objection | Core |
| R8 | Priority and timing | Client places it on a now-versus-later scale and names a target date or real deadline | Quote | "Is this something to fix this quarter, or later on?" A "later" answer is flagged to the user as a fit risk | Advisory |
| R9 | Blockers surfaced | Client has said what could stop this going ahead | Quote | "What could get in the way of this going ahead?" near the close of the next meeting | Advisory |
| R10 | Next step committed | On a discovery or demo call: the call ended with a specific date, time, and owner. On a working session or an expansion call (expansion mode, below): a date, **or** a booking mechanism delivered during the call with a named owner, a stated purpose and the client's assent; scheduling handed off to a named owner without that assent grades Partial-plus and always emits a same-day date-proposal to-do; an offer to find some times is neither. Nothing is keyed on post-call calendar state, which a transcript cannot show | Quote | Flag in the call summary; recap draft proposes a concrete time; unowned commitments flagged | Every call |
| R11 | Solution confirmed | For each in-scope pain, the client said during a demo that what they saw addresses it, and the presenter confirmed the tie back in their words — read from the confirmation ledger (4.3). A client agreeing to a described mechanism with nothing on screen is *mechanism-confirmed*: weaker, and re-confirmed against the built artefact before sign-off | Quote per pain from a demo transcript, paired with the line it answers | Re-check unconfirmed and mechanism-confirmed pains in the next demo | Gate: v1.0 |
| R12 | Scope agreed verbally | Client agreed a short scope (five bullets or fewer) out loud. Where the client built part of the thing themselves, the scope is a delta in four parts — inherited, in scope, client-side change, access unlock — each confirmed with the person who owns it; without that, both sides price different objects while believing they agree, and the anchor becomes a completion figure guessed aloud | Quote | No proposal draft; scope-confirmation step added to next prep | Gate: proposal |

**On R10, where practice and the method disagree.** Across the whole evidence base no new date was fixed during any call; the only date that appears pre-existed and was named by our side. What separated a good close from a bad one was a *mechanism* with a named owner, not a date. The method keeps the date rule for discovery and demo calls, because a date in the room is attainable there, the close (4.6) is written to obtain it, and a fixture key already grades "I'll send something over" as Missing; the mechanism state applies to working sessions and expansion calls, where the honest best outcome is often a booking mechanism handed to a named owner with the client's assent. The written rule wins on grading; the observed practice wins on how the close is built.

**Which role can supply what.** A Missing grade is only actionable once it is known who could have answered. The map below is what turns "Missing" into "not obtainable from this room" and routes it to a room change; each gap question (2.5) names the role.

| Criterion or check | Usually supplied by |
|---|---|
| Current state, workaround, concrete instance | the operator who does the work; the admin or builder for what the platform does today |
| Cost inputs, effort per unit | the operator who does the work (volunteered when present); the department head for the aggregate |
| Volume, headcount, frequency | the department head |
| Why now, the clock, priority | the executive or budget holder |
| Decision process, blockers, procurement | the gate-holder, in their own words |
| Access, policy, security questions | the client's IT or security owner — never answered by us |
| Scope of a client-built artefact | its author |

**Expansion and renewal mode.** One mode, not two. It applies when the client is an existing account of ours or has a live build already, and it carries a working-session sub-trigger — technical work performed in the meeting, or a client-built artefact present — rather than a second mode, because two modes firing on one call with different criterion sets and no precedence rule is worse than one imperfect mode, and the existing-account working session is their exact intersection. In this mode current state is expected Met early; why-now, bleed and decision process are the scarce criteria (the claim about decision process is provisional and confounded with room composition). Three record fields (3, field 16): *current wins to preserve* — quote, object, owner, authorship (built by us, by them, by a third party), the burden of keeping it and its change path, since what we built is at once the trust asset and the latent objection; *prior attempts* — what was built, by whom, when, its status and who paid, in their words, presuming neither failure nor lapse; and *incumbent friction* — anything the client has said about the cost or difficulty of changing what we previously built, recorded either way including "nothing said". An advisory rubric item documents what already works. What we built and is still live — the objects, the allowance they consume, the change-cost expectation the client has formed, the do-not-disturb list — lives at record level in `prior_builds` and the live map (architecture §7.2, §7.8) and is not duplicated here.

**Client-built assets and inherited-build risk.** Where the client has built something themselves — a prototype, a script, a partial solution — the record holds it in its own section (3, field 15) with the blocker in their own words, which is usually the actual scope rather than the pain list. Before any commitment, establish authorship, whether we can read it, the cost of discarding it and who owns it after handover. No completion, effort or duration figure is quoted for work on a client-built artefact until we can read it; the replacement is what has been seen, what still needs looking at, and the artefact required first (7.1). A separately priced review step is a recommendation to the user, never a rule the product enforces: a transcript cannot license a commercial policy, and on a small job a forced review in front of someone who has built most of it reads as padding.

**Bleed and upside math rules**
- Bleed: hours per week x loaded hourly cost x 52 (or monthly x 12), per pain, then summed. Errors, rework, and lost deals are added only when the client gives a figure; otherwise listed as unquantified.
- Upside: freed hours, then extra output (deals, jobs, clients) x the client's average value, per month; then the "what would you do with it" question.
- Use the client's figures. Show ranges as ranges, never round up, never fill a missing input with an outside average. Any Claude estimate is [inferred] and kept apart from the client's number. A figure whose unit was abandoned mid-sentence — a per-item rate, then a package size, then trailing off — is stored *unit-unresolved*, neither a range nor a hedge, and is never given the nearest unit in the sentence. A hedged number keeps its hedge and is never promoted to confirmed. A figure that entered the call from outside it — a colleague's message, a lookup mid-call — is recorded as off-transcript and never promoted to confirmed. Between two figures whose relationship is unresolved (2.1) no arithmetic runs.
- Time saved converts to money; where it fits, ask what the time back would mean to them personally. Personal motives are internal notes.
- If the bleed looks smaller than the likely engagement cost, flag it to the user as a fit question, not a pricing problem.
- **Platform consumption is a design input, not a bleed input.** Where any component the solution will use is metered, record the allowance the account holds, what already consumes it and by what, whether charging is per run or per publication, expiry and reset behaviour, and a measurement plan (3, field 17). It changes the run-volume design and the number of human-in-the-loop steps, which is why it moved inside scope while pricing, proposals and ROI stay out (SPEC). It is cross-linked to the bleed frame; whether it belongs inside that frame or beside it is open (11).

### 2.4 Verdict and stage gates

**Verdict** (source exit criteria for discovery: concrete pain, why now, money figure, decision process):
- *Discovery complete*: R2, R3, R4, R7 all Met.
- *Nearly ready*: none of those Missing, at least one Partial.
- *Not ready*: any of those Missing.

The verdict and a one-line reason appear in `discovery.md` and `STRAND.md`, and in the strand index on `CLIENT.md` (A14). The reason line names the missing multiplier where scale is established and the cost is not priced, any open question that blocks a gate with its owner, and a commercial-date collision (below).

**Readiness section, beyond the grades.** A *voices heard / voices missing* line, built from the attendee list against who actually spoke. Where no roster exists the line reads "unknown", never "none": a format that records only speech cannot show a silent attendee, and reporting zero silently defeats the rule in the format where it is least reliable. Attendees who never spoke and hold a decision-shaped role are promoted to a named risk row that records whether our side ever addressed them. Criteria met only by the people who already like the tool are discounted in the reason line. The asked? flags (2.1) are shown beside the grades.

**Stage gates** (proposal for the user to confirm):

| Step | Needs | If not met |
|---|---|---|
| Solution blueprint | R1 at least Partial, R2 Met; where a structure inventory exists (2.6), its graded read-back | Explain the gap, offer a discovery prep; the user may override |
| Scope record and hand-off (a `non-platform` strand, or the non-platform half of a `hybrid` one) | The strand's scope, open questions, dependencies, access needed and next steps recorded | There is no build, demo or audit for such a strand; the design step ends with the plain statement that building happens outside the product (A13) |
| Build | the user's approval at the existing approval stop | (no extra method gate) |
| First demo (v0.1) | Nothing extra; the version audited | Gaps become demo questions. A strand with nothing built inside the product cannot be demonstrated (A13, 4) |
| Pricing or proposal prep | For a figure: R4, R7, R12 Met. Disclosing that a component is consumption-priced is not gated (4.10) | Prepare the missing step instead |
| v1.0 sign-off | R6 success criteria agreed; R11 Met for every in-scope pain, mechanism-confirmed pains re-confirmed on screen | Add re-checks to the sign-off demo |

**A commercial date against a closed gate.** When a commercial date exists — on the client's side or ours — and the pricing gate is closed, schedule the missing steps backwards from that date and show the collision on the front page, rather than waiting for an override nobody wants to give.

Overrides are the user's call. The product records the override and its reason in `log.md` and keeps the gap visible in `STRAND.md`.

### 2.5 Turning gaps into meeting prep

- Each Missing or Partial item yields one short, conversational question tied to its P# or R#, stored in the strand's open-questions register (3, field 14) and pulled into the next meeting's prep, together with the person who can answer it (2.3, obtainability map).
- Show what is already known next to each question, so nothing gets asked twice. Remove questions once answered.
- At most five gap questions per meeting, counted per audience — the people who will actually be in the room — and per kind (conflict, technical, access, commercial, policy, ask), which is the same cap the open-questions register applies from the other side. Order: core criteria, then gates for the upcoming step, then advisory items.
- In a demo, attach each gap question to the segment it follows naturally (4.4).
- When a gap cannot be closed by asking (the approver never attends; the role that could answer was not in the room), propose an action instead: invite them, or offer to join their internal conversation. A question that was asked and dodged is not repeated as written; it goes to a different person, room or framing.
- **Discovery-meeting prep order:** brief connection question and let them talk first; set the frame that this is a conversation; honest-expert line where it fits ("If a small fix is all you need, I'll tell you."); current state; per pain (concrete, workaround, reach); why now; cost and confirmation; upside; outcome; decision, priority, blockers; commitment question and a specific next step.
- **Group discovery, prep order:** let the senior person set the frame; take each role in turn, by name, with the reason they own the question (4.12); then have them demonstrate. The prep lists attendees with a stated stake and no contribution, ranked by stake; at least one gets a direct question by name before the close and the rest are handed to the convener to route. Never every silent attendee put on the spot — in a large mixed room that is a plausible way to make a meeting worse.
- **When the client is showing.** Two disciplines, and the difference is *what* they are showing. When the client walks their **current state** — a reverse demo — the rule mirrors "a demo is a conversation": stop selling while they are showing. Our questions crowd out their narration, and a fix proposed across it is what flattens the requirement that was about to be said; questions go to the inventory (what is this, who owns it, where does the value come from) and nothing else. When the client walks a **candidate solution they built themselves** — a prototype review — sustained interrogation of the artefact is the work and silence is the defect: probe the data source, the formats, the identifiers, the failure cases, what breaks it. Interrogating the artefact is not selling; what the rule targets is our side proposing a solution across their narration. The method as first written stated only the first half, as if universal; that version would have graded the best-run call in the evidence base as a violation, so the scoped rule wins. The delivery-note check (6.5) fires only on the current-state case. In either case, ask for the *shape* of a thing rather than choosing an item for them to open (architecture §9.11); that is etiquette, not a limit on the inventory probing the reverse demo requires.

### 2.6 Call type, and what it switches

A call's type is not one label but four dimensions, each of which changes which criteria apply and at what threshold: **seat** (who owns the room and the question order — partner-led, co-sell, vendor-led, client-led), **relationship** (new logo, existing client of ours, a third party's account where we are the stranger), **direction of show** (we show; they show their current state; they show a candidate solution they built; nobody shows), and **output class** (configured structure, bespoke code, hybrid — where a hybrid is two work items with two gate sets, never a blend). Two modifiers change thresholds without changing structure: room shape, and whether money is live in the room. Intake proposes the type as a header on the call summary with the quote that produced it and never decides it; the user dismisses or confirms (architecture §8.3, step 5). Only the cells the evidence covers are specified, and no behaviour is invented for an unseen cell.

- **Type per segment.** A call is not one type throughout: when the screen stops, client share and the rate of substantive client turns jump, and everything decision-relevant may arrive after that boundary. The summary carries the primary type plus the segment boundaries with the event that caused each, and grading, evidence harvesting and delivery notes (6.5) run per segment.
- **Unresolved type.** Where a dimension cannot be resolved, the fallback is the value that grants us the fewest rights and demands the most evidence, and every type-specific rubric rule drops to advisory: it may raise a question but never produces a Missing verdict or a failed gate. That demotion stops at the rubric. The strand's kind and output class, which the user sets when the strand opens, still govern the build, audit and demo doors, so nothing is claimed buildable on an unresolved output class and no door goes advisory (architecture §12.3, D26). A client document has no call type at all (A16): a document-only record is graded under the document rules of 2.1 alone, every criterion against its definition, and nothing drops to advisory for a header it does not carry; beside a call, the call's type scopes the criteria and the document's extracts are admitted under the same rules.
- **Reverse demo** (they show their current state) and **prototype review** (they show a candidate solution they built) produce the **structure inventory**: boards, groups, columns, statuses, views and dashboards, each row marked *spoken*, *observed* or — from a client document or diagram — *documented* (A16), each with an owner and a class (current state, current manual artefact, client-built prototype), so current state can be satisfied without the prototype rows. Two further states: *proposed-and-displaced*, with the displacing quote, and *compound show*. Its graded read-back — the current-state analogue of R11 — sits in front of the blueprint gate; current state can be Met by observation plus narration, with observed-only rows recorded as unconfirmed. A prototype review additionally records the inheritance: which tool, what works, the named gap in their words, who owns the code, what access we need, what must not break, and their own assessment of completeness (provisional: the type switches no rule off on its own until a second observation arrives). Fork detection does not live in the inventory; it belongs wherever client speakers narrate their current state, in any call type, because the fork that mattered most surfaced during a demo of ours.
- **Scoping and working-session calls** are routed, not dropped, and not graded first: the open questions with their owners, the dependency chain, and the strand kind the call implies (`non-platform` or `hybrid` where the deliverable is not platform structure) are recorded before anything else, so the next step is the scope path and never a blueprint or a door (architecture §8.3, step 7). Grading, when the user asks for it, runs under expansion mode's working-session sub-trigger (2.3). A bespoke-code strand has no structure read-back, no automation list and no demo; "the thing cannot be demonstrated yet" is a stated stop, not a silent failure (A13).
- **A seat we do not own.** Next step and scope are graded against the thread rather than against us; the commercial answers have one named owner (4.11).

## 3. discovery.md fields

A **current** file per strand (A14), rewritten on each update: the consolidated view across every call and document the strand serves. Per-call detail lives in call summaries at record level; a later strand reads the closed strand's `SUMMARY.md`, never this file. Every line carries [found] with a source, or [inferred] with its basis.

**Header:** client and strand, last updated, calls covered (by sequence and provenance — first-hand or handed over, A15) and documents covered (A16), current stage, verdict with one-line reason, the call-type header of the latest call (2.6).

| # | Section | Fields |
|---|---|---|
| 1 | Readiness | Per-pain checks and R1-R12: status, elements where compound, asked? flag with the attempted question, speaker per check, evidence pointer, next action and the role that can supply it; voices heard / voices missing (2.4) |
| 2 | Current state | Process walkthrough, tools and connections, people and time spent (on their process; on platform upkeep), monday today, who built it; `[pre-read]` and documented sources marked; pointer to the structure inventory where the client showed us their build (2.6) |
| 3 | Pains (P#) | Title in their words; 1-3 verbatim quotes with source and speaker per check; concrete instance; workaround and why it falls short; who else; cost inputs (link N#); trajectory; client's priority rank; linked blueprint elements; status (open, in build vX, mechanism-confirmed, confirmed solved with quote) |
| 4 | Numbers (N#) | Type (bleed, upside, volume, cost input); value, unit, period, or *unit-unresolved*; inputs with quotes; math; client confirmation quote or "unconfirmed"; hedge kept; linked pain. Bleed and upside totals at the top with the bleed state (Met, effort-quantified rate pending, `[unpriced]`, not measurable from their record); the per-pain cost check apart from the engagement bleed; scale reported even when the bleed is Missing; unresolved pairs shown as pairs. All internal-only |
| 5 | Why now | The three client-side elements — change, trigger, clock — with quotes and dates; separately, our own commercial clock and constraints, marked excluded from the grade and listed as owned to-dos |
| 6 | Outcome and success criteria | Client's picture of solved (quote); leadership's win condition; draft criteria marked proposed or agreed |
| 7 | Stakeholders (S#) | Name, role as titled and as behaved, side, decision role — and where the room described one, the delegation graph (delegate, gate-holder, gate condition, re-entry trigger, standing conditions) — what they care about, calls attended, spoke or silent, demo audience type, open questions for them. A client-side interviewer (a client speaker whose turns mostly interrogate a named colleague) is reported here and never changes a grade (provisional) |
| 8 | Decision and timing | Steps after a yes, approver, budget process, procurement or legal, priority, target go-live, blockers named; commercial dates on either side, checked against the gates (2.4) |
| 9 | Objections (O#) | Status (anticipated, raised, resolved, recurring, **embedded** — surfaced as a fact about today by the person who lives it, rather than raised as a deal objection); their words and source, or the signal if anticipated; underlying concern; client-attributed cause; skipped step; response used or planned; outcome |
| 10 | Commitments (C#) | Who (client or the user), what, due date, source, status (open, done, overdue); includes every question our side answered with a deferral or an unverified hedge, converted to an owned, dated commitment (6.1) |
| 11 | Next step | Date, time, owner, purpose, calendar invite sent (yes or no); or the booking mechanism, its owner and the client's assent, with the same-day date-proposal to-do (R10) |
| 12 | Client vocabulary | Their terms for work items, stages, roles, documents, and the incumbent tool's mechanism words. The per-file alias table confirmed by the user at intake. One word used for two levels of their model is flagged "confirm before naming anything"; a term that looks like a hierarchy level but denotes a staff grade or a skill tier is never modelled as hierarchy. Reused in board and column names, demo script, and SOP |
| 13 | Alternatives in play | Other partners, vendors, in-house build ideas, platform-switch talk |
| 14 | Open questions | The gap questions for the next meeting, drawn from the strand's open-questions register (`solution/open-questions.md`: one block per question with kind, what it blocks, owner, best answer so far with its confidence, how it gets settled, and a `bypassed` state for a question a design change routed around), each with target person |
| 15 | Client-built assets | What they built and why, the mechanism, the author, what it does and how we know, the blocker in their own words, access state with the unlock's owner and cost, our completeness note, disposition, post-handover ownership. The blocker is one field here, not a second object. Usually the actual scope (2.3) |
| 16 | Current wins, prior attempts, incumbent friction | Expansion mode's three fields (2.3): wins to preserve with authorship, burden and change path; prior attempts with status and payer; incumbent friction, recorded either way |
| 17 | Platform consumption | Allowance held, what consumes it and by what, per run or per publication, expiry and reset, measurement plan (2.3). A design input; not pricing |

Expansion seeds live in `solution/backlog.md`; `discovery.md` only links to them. Asks made in a demo live in `solution/gaps.md` (4.6).

**Condensing at each version:** keep current numbers only (a value superseded in the narrow case 2.1 allows moves to `log.md` with date; an unresolved pair stays a pair); collapse resolved objections to one line; move done commitments to `log.md`; keep the strongest 1-3 quotes per pain. At strand close the strand's `SUMMARY.md` is what later work reads (A14).

## 4. Demo script

Internal file, `strands/<id>/versions/<version>/demo-script.md`. Generated from `discovery.md`, `solution/blueprint.md`, and `solution/build.json` after read-back verification and the auditor pass, in the voice of 4.12.

The run-sheet below is gated on **we show**. Where the client shows, or nobody shows — a scoping or working session, a reverse demo, a prototype review — the artifact is a **scoping run-sheet** instead: the artefact to be walked, the dependency questions in order, the mechanism proposals to be named, and a scope read-back; and before any mechanism is proposed, where each input lives today, in what format and who puts it there. A `non-platform` strand, and the non-platform half of a `hybrid` one, cannot be demonstrated: nothing has been built inside the product, and the generator stops with that statement rather than failing silently (A13). An audience meeting the product for the first time gets the orientation pattern (4.3) beside the callback-led one.

### 4.1 Prep block fields

- **Meeting:** date, time, length (10, 20, or 30 minutes), version shown, type (first demo, iteration, sign-off, expansion) and the call-type header (2.6). Where the client stated a duration constraint in their own words, it is converted to a number here and the run-sheet is checked against it: a request for a brief look that becomes most of an hour of screen is a failure nobody converted.
- **Attendees:** name, role, audience type, decision role; whether the approver attends, and the plan if not; both sides' hard stops, so the close lands before either; attendees with a stated stake and no prior contribution, ranked by stake, one of whom is offered a question by name before the close; where the list gains people who have not seen the product, which of the three choices prep made — protect the type with an opening contract, budget an orientation block, or split the meeting (provisional). In a co-sell seat, the driver/fronter split (4.11).
- **One goal** for this meeting (for example: confirm direction on P1-P3; get verbal scope agreement; sign-off).
- **Already known:** top pains in their words, why now, desired outcome, and what the pre-read told us — proof of preparation opens the meeting (4.12).
- **Callbacks ready:** 2-3 pains, each with a verbatim quote and source. A callback from a call the presenter did not attend is marked second-hand.
- **Buying criteria, verbatim:** what the client has said would make them say yes. The precondition for the recovery block (4.3).
- **Numbers, sourced:** bleed and upside with the client's inputs, spoken only if it fits and never on screen; every other figure in the pack read live at prep with its date, or supplied and approved by the user — anything else removed, not hedged. Beside them the **numbers we do not have** card: one line per category with no sourced figure for this account, each paired with the sentence to say instead and the person who can source it, so it reads as what to say rather than as a list of things not to sell. The client's plan tier and product mix, with their date and source: absent a recorded plan, any plan-gated answer is "it depends on your tier, and I'll confirm which side of the line you're on".
- **Capabilities on the ladder:** each capability the pack may claim marked *shown* (built, verified, on screen, with the account and plan it was shown on), *buildable* (verified in our own testing, not yet built here) or *unverified*; only the first two are stated as capability, and the account-and-plan difference is said aloud only where the capability is plan-gated or the client stated a plan constraint, because a caveat on every screen turns a demo into hedging. The unverified go to the **if-asked list** with their answer ("I'd want to check that before I promise it") and the positive continuation: build the smallest working version, run it once, measure, multiply by their own volume.
- **Artefacts to request before the call:** any question whose answer could be read off a document — an interface specification, an export, a process map — is an artefact request, not a demo question (4.4).
- **Gap questions:** from the rubric, capped per audience and kind (2.5), each attached to a segment and routed to a named person.
- **Likely objections:** at most three (5.3), each with prevention question and response approach.
- **Environment check:** read-back and audit dates; the demo account named by id and asserted clean of rates, margins, staff cost and client lists, with a do-not-open list headed by our own commercial boards and the environment's capability gaps listed by name so a foreseeable question does not send anyone to a live account for an example (architecture §9.11 — our own live operational account is never shown); objects to open in order (build.json keys and URLs); sample items to click; unfinished areas to avoid; seed data realistic and free of internal notes (whether sample rows may sit in a live client account is a separate, open question [A11-2]). A **data-provenance line per screen**: for every visible field, where it comes from in their world today and what is seeded for illustration, required even when no screen depends on client data, with the environment as part of the line. A **dead-screen contingency**: the non-driving presenter holds a question for the gap rather than hoping the room fills it. Any connection shown says aloud what it is not allowed to change.
- **Planned close:** commitment question, fallback question, the per-pain confirmations expected, the gap-and-backlog line, the proposed next step as a mechanism with a named owner (4.6).
- **Opening frame:** three sentences (4.2).
- **Delivery reminder:** one line (greet as the host expert rather than thanking them for their time; pause after questions).

### 4.2 Opening (1-3 minutes)

- Greet, ask a short connection question, let them talk first. Open with who you are, who is with you and why, and what you already know from the pre-read (4.12).
- Set the frame in three sentences: what each piece shown links back to ("Each piece I show links to something you told me. Interrupt whenever you like."), the plan boundary (what their tier includes and what is shown from another), and the seeded-data boundary (what on screen is theirs and what is illustration).
- Check priorities with a question, not a recap: "Has anything shifted since we last spoke?"
- Where the client's current structure and the proposed one differ, take a two-minute translation beat before the first screen: read the structure mapping back in their words — "today this is one container per X with each Y inside it; here the Y becomes this and the container becomes this" — and where two shapes are genuinely possible, offer both aloud and let them choose. This is a conversational move, paired with the blueprint's mapping section (architecture §3.4) and distinct from the modelling rule that both shapes are supported. Skipping it is how a client maps silently and concludes the demo solved the wrong layer.
- For a room meeting the product for the first time, define the platform once, in one plain sentence, with the jargon dissolved on the spot.
- An agenda fork ("we can go through the build, or spend the time on the open questions") is offered only where every branch has a prepared run-sheet, and the chosen branch's scope is restated as a numbered budget before the first screen. It is a second-meeting move; a first demo never generates one.

### 4.3 Segment pattern (one per pain)

| Step | Content | Guidance |
|---|---|---|
| 1. Callback | Pain ID and the client's own words | One sentence: "Last time you said [their words]." One callback per segment, verbatim — never one aggregated paraphrase spent before the first screen. A second-hand callback is said as such and is never self-confirmed |
| 2. Show | Object(s) from build.json, click path, sample item | Under two minutes. Only what serves this pain; list neighbouring features not to show |
| 3. Value | The outcome in their vocabulary | The effect on their week, not the feature name; optional spoken tie to their number |
| 4. Check-in | The **named** check-in: one open question to the person whose pain it is, inviting correction | "How close is this to what you had in mind?" — to them by name. The only kind of check-in recordable as a confirmation. At a phase boundary, and only where the room holds people whose stake the record does not know, one **room-wide open** check-in in addition, naming the topic and tolerating silence, preferably from whoever is not driving; it is for discovering a stake, never for confirming one. A closed comprehension check ("does that make sense?") may open the floor and is never evidence |
| Listen for | Yes signals, gaps, objection signals, the client tying the screen to their own pain | Yes: exit-ramp check. Gap: note for `gaps.md` or the blueprint. Objection: link O#. A client tie: confirm it back in their words on the next sentence and log it in the confirmation ledger |
| Optional | One gap question tied to this pain | From 2.5 |

**The two check-ins.** The method as first written had one check-in and one rule, and its round-one tightening — every check-in to one named person, never to the room — would have deleted the two devices that made the strongest demo in the evidence base work: a room-wide open check-in was the only reason a silent attendee spoke at all, from a stake our side did not know existed and so could not have named, and a closed comprehension check opened the floor to two substantive questions. The distinction is between a check-in's turn-yielding function and its evidentiary function: the named check-in confirms, the open one discovers, and only the first is recorded as a confirmation. In a small room where every stakeholder's pain is already recorded, the named rule stands alone.

**Client ties and the confirmation ledger.** When a client says out loud that a screen solves their own stated problem, that is what an interactive demo *produces*, not a symptom of a missing callback — the round-one reading of client tying as a defect signal is refuted and is not written anywhere. The defect is a tie nobody confirms. The presenter's next sentence confirms the tie in their words, and it is logged as a per-pain confirmation; the ledger is capped at ties that map to a named pain in the record, so an interactive stretch does not become a parroting loop. The close reads the ledger back (4.6); R11 reads it after the call.

Segment rules:
- Order: the pain tied to why now first, then by the client's own emphasis.
- Never more **planned** segments than stated pains. Features with no pain go to the backlog. Showings generated live in answer to a client question are exempt from the cap and counted separately in the delivery notes: many one-minute answers are not worse than a few long lectures, and the cap exists so the generator does not simply emit more.
- If our side has spoken for about 90 seconds without a client word — counted from the last client word, across both presenters, with a one-turn hand-off exemption — the next line in the script is a routed question (4.12). With two presenters the monologue becomes a duet, and a per-speaker clock passes it.
- When the client reacts strongly ("this would halve my week"), match the energy and convert: what that is worth to them, what they would do with the time. Record the quote.
- If they ask for something not built, confirm what they mean, note it in `gaps.md` for the next version or backlog, and carry on. An ask repeated across meetings and people is a build item, not a talking point — including one answered satisfactorily in words every time, which is what hides it. Designing a mechanism live off their answer counts as addressed only if it ends in a named artefact request or a build commitment with an owner and a date.
- **Recovery block.** When a live failure is fixable on screen in under a minute: fix it live, narrating each step, and have the non-driving presenter tie the fix to a buying criterion the client stated earlier, read from the prep block. It is a block to have ready, not a graded rule.
- **Orientation pattern** (first exposure; provisional): name the primitive, show one live instance, state what composes on top of it, confirm comprehension, route a discovery question. Audiences who have already seen the product get the callback-led pattern.
- Where the portfolio default applies (AMENDMENTS A6), the demo carries a job-level segment addressed to the person who works at that level.

### 4.4 Discovery during the demo

- The demo continues discovery. The cap is on **questions whose answers cannot change the next two minutes**, not on the number of questions: the earlier cap of one per segment and three or four in total is lifted because on a well-run demo mid-showing discovery produced the call's best pain statement and stopping eighteen times worked. The override is argued rather than slipped in, and it is provisional as a general licence: the driver could run mid-demo discovery without losing the room because a second presenter held the frame, and a single presenter who stops ten times has nobody covering the floor.
- Any question whose answer could be read off a document is an artefact request made before the call (4.1), never a question that interrogates one person in front of the room.
- Current-state data questions are asked before any screen that presupposes data ("where does this list live today, and who keeps it?"), which pre-empts the question that otherwise gets asked and deferred four times.
- Rubric gaps come first. Otherwise use standing questions such as:
  - "Who would have this open every morning?"
  - "How would [named colleague] react to this?"
  - "What would it take for your team to say yes without hesitation?"
  - "Which part of the week would feel different first?"
- Answers go into the demo call summary and update `discovery.md`.

### 4.5 Exit ramps

Written as literal sentences to listen for, gated on we-show.

- **Buying signals:** explicit confirmation ("that's exactly it"), questions about timing, cost, rollout or next steps, talking about using it in the future tense, asking who else should see it. The strongest of all: a client building their own scenario in the tool, unprompted and in the future tense ("so when a job comes in we'd..."); it ends the showing.
- **Action:** finish the current point, skip the remaining segments (kept under "if asked"), go to the close.
- The urge to add "it can also do..." is the cue for the commitment question.
- **Hesitation signals** (quiet, vague answers; three or more hedges in one turn — "I suppose", "maybe", "we'd have to see"): stop and add nothing. Slow down and ask what is on their mind. Do not add features or information.
- **An explicit redirect** ("can we move on to...", "the thing I actually wanted to see is...") outranks every hedge and ends our side's elaboration on the next sentence. It does not end client-initiated questions; where the redirecting speaker yields the floor to a colleague first, the segment clock starts when that thread closes, and overrun is measured from the end of the client thread, not from the redirect.
- **A client vouching for an unshown capability** ("your colleague said it can do that") sourced to a meeting we were not on is a buying signal and an unverified claim at once, now with a client champion attached; the presenter's next sentence confirms the scope or qualifies it, and the claim goes to the correction list (7.1).
- Each segment carries a one-line ramp note naming which remaining segments can be skipped.

### 4.6 Close (2-4 minutes)

The close is a separate discipline that delivery quality does not produce: on the evidence, a demo that beat a weak one on every structural measure ended exactly the same way — no commitment question, no per-pain confirmation, no date, and a read of the room standing in for all three. So the close is generated in full, in this order.

- **Commitment question, not a summary:** "From what you've seen, does this deal with the problem you described?" then "Where would you like to go from here?" Never "how does this resonate?", which asks for an opinion and gets a review.
- **Per-pain confirmation from the person who raised each pain**, read back from the confirmation ledger (4.3) rather than asked cold: "[Name], you said the intake screen takes the Friday rebuild off your desk — is that right?" A pain with no ledger entry is asked of its owner by name, once.
- **The direction question**, then the **gap-and-backlog line**, spoken: what was asked for and not shown, what goes to the next version and what to the backlog, in their words. It is read from `gaps.md`, where every ask sits as shown, promised, answered-in-words, deferred or unaddressed with its repeat count across meetings and people — and unaddressed names people as well as items.
- If hesitation is in the air: "What could get in the way?"
- **The next step is a mechanism, not a promise.** The invite sent while everyone is still on the call is the mechanism that fixes the date, and the close aims at it. Where the room cannot fix one, the close hands scheduling to a named owner through a named mechanism — their assistant, a booking link, a slot the convener will confirm by a stated day — and takes the client's assent to it; "I'll send something over" is not a mechanism. On a discovery or demo call R10 still needs the date (2.3); the close is written around the mechanism because that is what separated the good closes from the bad ones, and the rubric holds the line so the run-sheet keeps aiming at a date.
- **Never in the close:** reading the room. No nonverbal read, enthusiasm read or self-assessment of fit stands in for the commitment question; it is worse than the banned opinion question, which at least yields a quotable client sentence, and the nods being read may come from a room in which several people never spoke.
- A proposal is offered only after verbal scope agreement (R12).
- Commitment by version: v0.1 confirm direction and gaps; v0.x confirm the changes; v1.0 sign-off; v1.x go-ahead for the next item.
- **Close variant per call type.** A scoping session closes with a scope read-back in five bullets, each confirmed with the person who owns it (the four-part delta where the client built part of it, R12), then the paid-next-step question, then the booking mechanism. The commitment question there is about proceeding, not about whether a screen solved a pain.

### 4.7 Timing variants (estimates; roughly 3-4 minutes per segment)

| Length | Structure (minutes) | Segments | Gap questions | Typical use |
|---|---|---|---|---|
| 10 min | Open 1, segments 7, close 2 | 1-2 top pains | At most 1 | Executive check-in, follow-up |
| 20 min | Open 2, segments 14, close 3-4 | 3-4 | 2-3 | Standard demo |
| 30 min | Open 3, segments 17, open conversation 5, close 4-5 | 4-5 | 3-4 | First demo, sign-off, mixed audience |

Cut segments rather than rushing the showing. Unshown segments stay listed under "if asked". The open-conversation block sits **before** the close and may grow at the expense of segments, never of the close: the best material in the evidence base came from a long open-question tail, but that tail carried no commitment question and no confirmation, so it was extended Q&A rather than a close. The close keeps its two to four minutes; a run-sheet that protects a long open phase flags the tension with this table rather than lengthening the close quietly. Whoever controls the screen — ours or theirs — stays to the close, so the meeting ends well before either side's hard stop; where the driver leaves early the close becomes a drift, and the largest ask of the hour tends to arrive inside the overrun.

### 4.8 Audience variants

| Audience | Callbacks chosen | What to show | Value framed as | Check-in example | Commitment |
|---|---|---|---|---|---|
| Executive | Pains tied to why now, risk, visibility, cost | Dashboards and summaries, few clicks | Outcomes, risk removed, their numbers (spoken) | "Is this the view you'd want before your board meeting?" | Decision and next step on their side |
| Admin / owner | Maintenance, data quality, handoffs | Structure, automations, permissions, how to change things | Less upkeep, fewer breakages, control | "Could you adjust this yourself when things change?" | Rollout ownership, access, handoff and SOP |
| End user | Their daily friction | Their board or view, item page, forms, notifications, one real task end to end | Fewer steps, no re-entry, clarity | "Would this replace what you do today?" | Pilot or feedback date |

Mixed audience: approver's segment first, at least one segment per role, and after each segment a **named** check-in to the person whose pain it is — the only check-in recordable as a confirmation. Where the room holds attendees whose stake the record does not know, one **room-wide open** check-in per phase boundary is permitted (4.3); in a small room where every stakeholder's pain is recorded, the named rule stands alone. Where the portfolio default applies, a job-level segment goes to the person who works at that level, because two independent rooms rejected the portfolio shape at the job level. Larger rooms: 4.11.

### 4.9 Version variants

- **v0.1:** confirm direction, heavy on gap questions, expect changes.
- **v0.x:** callbacks point to the client's feedback from the previous demo; the correction list from the previous meeting (7.1) is read before the first segment.
- **v1.0 sign-off:** one segment per in-scope pain against agreed success criteria; confirmation per pain (R11), with mechanism-confirmed pains re-confirmed on screen; commitment is sign-off.
- **v1.x expansion:** callbacks come from backlog seeds the client raised; expansion mode's fields (2.3) shape the prep.

### 4.10 Pricing conversation guard (internal; only when the user asks)

- **Two halves, gated differently.** Disclosing that a component is *consumption-priced* is a risk disclosure: allowed and encouraged early, and mandatory wherever any component the solution will use is metered, because a client with a painful precedent on a metered tool will ask for the model before any scope exists and deserves the answer. Naming a *figure* stays gated: preconditions R4, R7, R12 Met; otherwise prepare the missing step. The method's original ordering was wrong on the first half.
- Prep order for a figure: restate their bleed in their words; restate what they said solving it would be worth; scope in five bullets or fewer; the price stated once; a pause; if they react, a calm comparison with their bleed; commitment question.
- No unprompted discounts, no justifying the rate, no filling the silence.
- Price sensitivity is answered with fuller cost discovery earlier, not discounts.
- **Never a leading price question** ("it shouldn't be more than that, though, right?"): its answer would later be quoted as a client input, and it is not one (2.1). Never reason from one vendor's pricing to another's. Provisional, one observation.
- **Audience and role.** No price, rate, entitlement or account-status figure is stated after the person who owns approval has left the call, and none is placed in a group-facing recap or a summary addressed to a mixed audience; the product never generates a sentence that makes a non-approver the messenger for a figure. Where one is spoken anyway, it becomes an owned, dated to-do addressed to the approver and is raised in the summary. Trigger: only where a gate-holder has been identified and was present earlier in the same call — otherwise every first meeting would escalate a to-do to a person the record has not met. The user may override it, and the override is recorded, because a budget holder who asks for the number in front of their team should not meet a product that refuses to write it. This rule lives here once; the rubric and the summary rules apply it from here (provisional, one observation). In a co-sell seat one named person owns commercial answers (4.11).
- A commitment to check something carries no figure in the same turn, and an unsourced figure is refused rather than ranged (7.1). Check entitlement before quoting; anchor money against a spend they already make.
- The plugin holds no rate. Figures come from the user; every plan-limit, quota and entitlement figure is read live at prep with its date and kept, user-approved, in the claims store outside the record (architecture §9.12).

### 4.11 Group calls and several stakeholders

The method as first written assumed one or two client voices. Rooms of nine or more, with several attendees who never speak, are ordinary, and the guidance below is what such a room needs.

- **Know who is there.** A participant header is claimed, not observed: intake reports listed-but-silent and speaking-but-unlisted, assigns side from behaviour, and where no header exists reads the roster from the introductions and records voices-missing as "unknown" (2.4). The prep lists attendees with a stated stake and no contribution, ranked by stake; one is offered a direct question by name before the close and the rest are handed to the convener to route. Never every silent attendee put on the spot.
- **Route by name, with the reason.** Every question goes to a named person with the reason they own it (4.12). The same architecture question is asked twice: once of whoever knows what is possible, once of whoever knows what is needed. A client-side interviewer — one client speaker interrogating a colleague by name — is reported in the delivery notes and changes no grade.
- **Two check-ins** (4.3): named to confirm, room-wide open to discover, closed comprehension checks never as evidence.
- **New attendees evict the planned meeting type** unless prep protects it: an opening contract, a budgeted orientation block, or a split meeting (provisional; the client stated the mechanism themselves).
- **Whoever drives the screen stays to the close**, and the run-sheet respects both sides' hard stops (4.7).
- **Commercial statements are routed by who is in the room** (4.10): none after the approval owner leaves, none in a group recap, one named owner for commercial answers.
- **Co-sell seat** — a third party fronts the meeting and the user drives the screen: the prep block carries the driver/fronter split (who opens, who drives, who closes, who answers commercial questions) and the agreed hand-back sentence. One named person owns each topic; the non-owner routes rather than answers, and two people never answer one question at once, because a single commercial question otherwise takes several exchanges to settle in front of the room. Every claim the other party makes in our presence is recorded verbatim, attributed and dated, so the follow-up can cite it rather than repeat it; any statement they make about our own services or scope is explicitly reclaimed as ours; and routing a question to them does not make the answer sourced.
- **A client asking why some group is not in the room** is an objection signal (5.3), not small talk.
- **Gap questions are capped per audience** (2.5), and a Missing that the room could not have supplied names the role that could (2.3).
- **The close reads no room.** Nods from a room where several people never spoke are not a commitment (4.6).

### 4.12 Voice: how the practitioner works

This is the register a script generator follows for every run-sheet, scoping run-sheet, recap and client-facing reply; the plugin ships it as `shared/house-style.md` (architecture §3.12) and the shapes below are its source. The measured register is assertive rather than hedged and mechanism-first, with hedging done explicitly and structurally — "I'd want to check that" — rather than atmospherically. Profiles are per speaker and per seat, never pooled across our side: a pooled profile puts a colleague's habits in the user's mouth, and the corpus measured one colleague's hedging tic at many times the user's rate. Shapes carry placeholders in brackets; every phrasing is original and is adapted, not read.

**Framing.** Open with who you are, who is with you and why, and what you already know from the pre-read: proof of preparation beats a capability list. "I'm [role]; [colleague] is here because [reason]. From what you sent over I know [two facts]. Tell me where that's already wrong." Define the platform once, in one plain sentence, whenever anyone present has not seen it, and dissolve each term of art the moment it is used: "a [term] is just [plain word]". Anchor every new construct to whatever they already use: "this is your [their thing], with [difference]". Prefer building live on screen to describing.

**Routing a question to the right person.** Every question goes to a named person with the reason they own it: "[Name], this one is yours because you run [thing]: [question]?" Ask the same architecture question twice, of two people: "[Name], is that possible today?" then "[Name], is that what you actually need?" Stop before a dependency and ask rather than assume a fact about the client: "Before I go further — where does [input] live today, and who puts it there?" Never run past a couple of minutes without a routed question, and never let a client have to apologise for interrupting.

**Converting a client statement into a proposed mechanism.** Mark the load-bearing primitive and confirm it before composing on it: "Everything hangs off [primitive]; if that's wrong, nothing after it holds — is it right?" Then convert: "What you just described — [their words] — I'd call [mechanism name]: [one plain sentence]. In your world that means [restated in their nouns and verbs]." Close each proposed mechanism with a correctability question, which invites the missing case rather than an opinion: "What case does that miss?" — not "does that sound good?" Where two shapes are possible, name both aloud and let them choose (4.2). Deflate scope when it is genuinely small: "That part is small; I'd do it in the session rather than write it up."

**Not knowing, not being able, and self-correcting.** Admit unfamiliarity and make the admission the reason for the question: "I haven't seen your [system]; that's why I'm asking what a [record] looks like." A commitment to check carries no figure: "I'd want to check that before I promise it — [name] confirms by [day]." An unsourced figure is refused, never ranged (7.1). Narrate fumbles and say why a screen is messy rather than hoping nobody noticed. Retract explicitly and attribute the correction: "Earlier I said [X]; that was wrong — [Y] is right, and [name] caught it." Anchor money against a spend they already make, and check entitlement before quoting. Ask for their example artefact before offering ours: "Send me one of yours first."

**The DON'Ts** are the second-person statement of the claims rules in 7.1 and 4.10 and of the delivery-confidentiality rules (architecture §9.11); they are linked, not restated. Scope caveat: the bank rests on a large sample in one seat and a much smaller one in another; the framing, mechanism and commercial shapes drawn from the smaller sample are provisional and are regenerated when a second call in that seat arrives.

## 5. Objection handling

### 5.1 Generic pattern

1. **Pause.** Calm and curious; do not argue, defend, or discount.
2. **Ask what they mean, using their exact words.** "Say more about that. What part feels like a lot?"
3. **Find the real concern** under the stated one: cost, timing, confidence it will work, someone else's view, trust.
4. **Run the skipped step now** (5.2), for example working out the cost together.
5. **Let them propose the resolution.** "What would you need to see to feel comfortable with that?"
6. **Record it:** their words, the real concern, what resolved it, status.

Responses never include invented claims — client counts, success rates, case studies, sector-experience claims, demand statistics about our own book (0). An objection raised on two or more calls is marked recurring and gets a prepared response in the next prep. A concern restated three or more times inside a minute by one speaker, each restatement stronger, with only agreement tokens from our side in between, is a **restated-and-unanswered** objection: intake's delivery measures flag the candidate window (one client speaker, three or more substantive turns inside a minute, only our agreement tokens between — architecture §5.4), the summariser judges whether the turns restate one concern, and the summary raises it with all three quotes (provisional). Objections and responses are internal-only.

### 5.2 Skipped-step map

| Objection (paraphrased) | Usually means this was skipped | Prevent with | If it surfaces anyway |
|---|---|---|---|
| Price feels high | R4 bleed | Cost questions before any price | Compare with their bleed; if there is none, offer to work it out together now |
| Needs to think it over | R3 why now, pain trajectory | Urgency and trajectory questions | "Sure. Which part are you still weighing?" then address that part |
| Must check with someone | R7 decision process | Decision questions; invite the approver | Ask what that person will care about most; offer to join that conversation |
| Wrong time, next quarter | R3, R8 | Why-now and priority questions | "What will be different next quarter?"; cost of waiting from their monthly bleed; tie to their real deadline |
| We'll build it ourselves (they maintain the current setup) | Workaround check | Workaround questions | "What has held it up so far, and whose time would it use?" |
| We built most of it and hit a wall (they name the wall) | Nothing skipped: the strongest buying signal there is, with the ask already scoped by them | Ask for the artefact before the call (4.1) | Credit the work explicitly, then name the missing piece precisely; scope as a delta (R12); quote no figure until the artefact has been read (7.1) |
| Talking to other partners | R6 outcome, buying criteria | Outcome questions | Welcome it; "What have you seen so far, and what would make the choice clear?" |
| Just send a proposal or pricing | R12 scope | Scope confirmation before offering a document | "Happy to. Let's agree what it covers first, so the numbers mean something." |
| monday itself is the problem | R1 current state | Current-state walkthrough | Ask what it fails to do; offer to check whether the setup or the tool is the cause before a costly switch |
| Team won't adopt it (added; not in source) | End users not heard | End-user conversation, end-user demo segment | Ask who would resist and why; plan an end-user session. Never a maintenance promise ("set it and forget it"): the answer to an adoption objection is running the skipped step, not a claim about upkeep |
| Changing what you built for us costs us (added; provisional) | A self-service handover and a stated change path at build time | Hand over what they can change themselves; say at build time what changing each part will take | Ask what they most often need to change, then price or productise that path. The one objection class that is about us |

### 5.3 Anticipating objections from the record

Before each meeting prep, scan `research/`, `calls/`, and `discovery.md` for signals. List at most three likely objections in the prep block, and record each in `discovery.md` Objections with status *anticipated*: the signal (quote and source, or [inferred] and basis), the skipped step, prevention questions (merged into the gap questions), and the response approach. An objection that surfaces as a fact about today, from the person who lives it, is recorded with status *embedded* and a client-attributed cause (3, field 9) rather than as a deal objection.

| Signal in the record | Likely objection |
|---|---|
| R4 Missing, bleed small against likely scope, budget freeze or cost cutting mentioned | Price |
| R3 Missing, priority "later", no deadline, a peak period or year-end ahead | Think it over, wrong time |
| Approver never on a call, new names appearing, "I'll need to run it by..." | Check with someone |
| A client asks why some group or person is not in the room | Check with someone; a missing role for a criterion (2.3) |
| In-house admin or developer who maintains the current setup, earlier DIY attempts | Build it ourselves |
| In-house builder who built a prototype, hit a wall and named the wall | Not an objection: a buying signal with the scope already named (5.2) |
| Other quotes, partners, or vendors mentioned; research shows a tender | Other partners |
| Early requests for pricing or a document | Send a proposal |
| Frustration with monday itself, other tools being evaluated | Platform is the problem |
| Past failed rollout, low usage, complaints about team habits | Adoption |
| The client names a cost or difficulty of changing what we previously built | Changing what you built costs us |
| The same concern restated three times in a minute with only our agreement tokens between | Restated and unanswered (5.1) |
| The attendee list gains people who have not seen the product | The planned meeting type will be evicted (4.11); not an objection, but prep chooses a protection |

## 6. Post-call recap and follow-up

**Meeting loop** (chats break on units of work, not per meeting — A10: a new chat when switching clients, a fresh chat for a build or an audit, otherwise the same chat across several meetings until it slows):
- *Before:* read `CLIENT.md`, `STRAND.md`, the strand's `discovery.md`, `meetings.md`, the last call summary, open commitments and the open-questions register; produce the prep (discovery prep or demo script).
- *After:* the user provides the plain-text transcript, or a package of them (6.6), or a client document (A16). Once the open transcript question has been answered for this client [A11-3], Claude saves each transcript unchanged to `calls/`, writes the call summary, updates `discovery.md`, `STRAND.md`, `CLIENT.md` and `meetings.md`, appends to `log.md`, drafts the client recap, and lists the user's own to-dos (send recap, send invite, the owned commitments from deferred answers).

### 6.1 Internal call summary (`calls/<date>-<type>.md`, history)

- Meeting: date, type — one of the thirteen labels the architecture pins in `record-map.md` (§7.1: intro, discovery, reverse demo, prototype review, demo, scoping, working session, pricing, call review, expansion, sign-off, check-in, support; that list is the home and this is a citation of it) — the call-type header (2.6) and, where the type changed mid-call, the segment boundaries with the event at each; sequence in the client's meeting order and provenance — first-hand or handed over, and by whom as a role (A15); duration; attendees (name, role as titled and as behaved, side, spoke or silent); the strand or strands it serves; recording link (link only); transcript file.
- Goal for the call and whether it was achieved (yes, partly, no).
- New or changed: pains, numbers, why now, outcome, stakeholders, decision information; each with quote, speaker per check and location.
- Demo reactions per segment (confirmed, lukewarm, wanted something else) with quote, and the per-pain confirmation ledger — each client tie with the presenter's confirming sentence (4.3), which intake writes into the version's reactions block for the close and R11 to read.
- Objections raised: verbatim, location, how handled, status (including embedded and restated-and-unanswered).
- Commitments on both sides, with due dates.
- **Deferred and hedged answers:** every client question our side answered with "let me check" or an unverified hedge, each converted to an owned, dated commitment. Escalated in the summary only where the question collides with a recorded blocker; otherwise every "let me check" in a technical session escalates and the summary stops being readable.
- Claims made in our presence by a third party, verbatim, attributed and dated, never restated as ours (7.1).
- Next step (date, time, owner), or the mechanism with its owner and the client's assent, or a "not set" flag.
- Seeds and out-of-scope asks (copied to `backlog.md`); on a demo, every ask into `gaps.md` with its state and repeat count.
- **What the transcript cannot see:** silence measured where the export carries end times, presence changes inferable only from speech (late joins, hard stops, someone leaving mid-call), decisions and figure corrections that arrived off-transcript, and who was present when any commercial figure was stated (4.10).
- On a demo: the account it ran in and its intended state, and what was changed live on screen — object, change, whether it is kept — without a count, since a transcript cannot separate a described change from a performed one.
- Readiness changes: which criteria moved, and to what.
- Questions carried forward, into the open-questions register with owners.
- Delivery notes (optional, 6.5).

### 6.2 Client recap draft (`drafts/<date>-recap.md` in the strand, client-facing)

- What we heard: 2-4 bullets on their goals and problems, neutral wording, their vocabulary; no figures, no emotional detail, no remarks about colleagues.
- What we agreed: decisions and agreed scope items.
- Next step: date, time, who — or the mechanism and its owner.
- What we need from you: client commitments with dates.
- What you'll get from me: The user's commitments with dates, including every deferred answer now owned.
- Short and plain, in the user's voice (4.12). No price, rate, entitlement or account-status figure in a recap addressed to a group or a mixed audience (4.10). A third party's claim is never restated as ours; the recap points at the vendor's published documentation instead. Leak-checked (7).

### 6.3 Follow-up rules

1. Process the transcript the same day, ideally within an hour of the call; the meeting chat prompts for it.
2. No meeting closes without a next step the client assented to: a specific date, time and owner, or — on a working session or expansion call — a booking mechanism with a named owner (R10). If missing, the summary flags it and the recap draft proposes a concrete time; a mechanism without a date emits a same-day date-proposal to-do.
3. The recap is a draft. The user reviews and sends it; the plugin does not send messages or calendar invites unless the user asks at that moment.
4. The calendar invite for the next step stays a to-do until the user confirms it was sent.
5. Commitments carry an owner and due date in `discovery.md` and `log.md`. Open and overdue items are shown at the start of the next meeting chat. Every deferred or hedged answer (6.1) is one of them.
6. No proposal or SOW draft without R12 evidence.
7. Objections go to `discovery.md`; recurring ones get a prepared response.
8. Seeds and out-of-scope asks go to `solution/backlog.md` with the client's words and source; demo asks go to `solution/gaps.md` with their state.
9. Pains confirmed in a demo are marked with the quote and the presenter's confirming sentence (R11); mechanism-confirmed pains are marked as such. Rejected or reshaped features update `blueprint.md` and the version notes.
10. Answered questions leave the open list, so nothing gets asked twice.
11. **The correction loop.** Anything said wrong or unsourced on the call — an unsourced figure, an unverified capability, a hedged answer, a second-hand promise — becomes an entry on the next meeting's correction list, which the next run-sheet places before its first segment, so the correction is made in the room, attributed to us, and logged (7.1).

### 6.4 Support and check-in calls (short version)

Graded against five items; missing ones become reminders in the next check-in prep:
- Solved their issue first.
- Named what the fix prevents, in plain terms.
- Asked one forward-looking question before ending ("With this sorted, what's still being done by hand?").
- Logged the answer to `backlog.md` as a seed.
- Closed with a short note on what is worth keeping an eye on.

### 6.5 Optional delivery notes (internal; speaker-labelled transcripts only)

Every measure below is computed after intake has merged, split and re-joined the transcript, never on raw units, and each is scoped to the call type and reported per typed segment (2.6) as well as whole-call.

- **Client talk share** by word count and, where the export carries end times, by speaking seconds, as two measurements with no confidence claim drawn from their agreement. Discovery target: 60% or more. Demo band: client 30-40%, measured over the **showing window** and reported per phase as well as whole-call, because a whole-call figure launders a monologue — a demo can sit inside the band overall while its showing window sits at a fifth. The band is attainable and it is not sufficient. Beside the ratio, a **shred index** for the file, and the standing rule that the ratio is never read as a proxy for transcript quality: aggregate share is robust to shredding and nothing else is, so a healthy figure says nothing about whether individual attribution is right. Not reported when composite blocks exceed a few percent of words. Report the share and state plainly that it has not tracked grading outcome in the calls seen so far, with the n — an observation, not a finding.
- **What else must be measured**, because an aggregate can look healthy while the interaction is poor: the number of check-ins and stops, and which kind (4.3); showings inside the two-minute cap against the total; per-segment callbacks; exit ramps taken against buying signals heard; whether the driver stayed to the close; and the per-phase share.
- **Group calls** (more than two client attendees): share by side; the number of client speakers who contributed at all; the loudest and quietest client speaker; attendees who never spoke, with decision-shaped roles flagged (2.4); and, where one client speaker is interrogating another, client share decomposed into *client-interviewer* and *client-describing*. A client-side interviewer is reported, never grade-changing (provisional). A healthy group call and one person monologuing while the rest stay silent produce the same overall figure, which is why one number is never enough.
- **Own-side stretches without a client word:** over 90 seconds with timestamps, roughly 225 words as a proxy without them, counted from the last **client** word across both presenters with a one-turn hand-off exemption — not per speaker, since a two-presenter duet passes every per-speaker instrument while the client says nothing for minutes. Long single turns are still listed.
- Whether a fix was offered while the client was still describing a pain — checked only where the client was walking their **current state**. Where they walked a candidate solution they built, interrogating it is the work, and the check does not fire (2.5).
- Whether the call ended with a commitment question, per-pain confirmations, a gap-and-backlog line and a next step that was a date or a mechanism (4.6).
- Showings generated live in answer to a client question, counted separately from planned segments (4.3).
- Anything said before the client joined the recording.
- One takeaway, only one.
- Tone and energy cannot be judged from plain text; do not attempt it.

### 6.6 Taking over a package from another seller (A15)

Sometimes the record starts from a package: discovery, one or more demos, a call review, a pricing call, handed over by another seller or sales engineer as downloaded files or pasted text, often in yet another export grammar. One call remains the common case and the default; a package is the same flow with more inputs, never a separate mode, and nothing waits for a second call.

- **Take it in as a set.** Type each call (2.6) and order them: the script orders by date and flags ties, intake proposes the internal-evidence adjustments — who refers back to what, which build a later call reacts to — with their quotes, the user confirms, and file names count for nothing. Record who was in each. Build one record from all of them before grading anything.
- **Second-hand is second-hand.** A client figure the handing-over seller re-quotes is not fresh client evidence (2.1). A commitment or capability promise a client reports our colleague having made in a meeting we did not attend is recorded "reported, unverified", with the reporting client's quote, the colleague named, and an action to confirm before the next session; the room accepting it as settled does not make it so. A figure relayed from an absent colleague during a call travels with its hedge. Every claim the previous seller made about the platform, its price or its limits goes to the claims store and onto the first meeting's correction list (7.1), so the user corrects rather than compounds it.
- **Cross-call conflicts are kept, not resolved.** Both statements, each with its call and speaker; no "most recent wins" across calls. Unresolved conflicts become gap questions for the next meeting, routed to the person who can settle them.
- **Grade and blueprint once**, against the synthesized record, so the first build is a proof of concept assembled from the whole package rather than from its last call. The most-repeated ask is counted across the whole package and across people (4.3).
- **Afterwards, every new meeting is one more call into the same record** and a new strand version that builds only the difference from the version before — whether the change is to something we built or to something that already existed in the client's account (architecture §8.9).
- **The first recap after a handover** names what the user knows from the package in the client's own words, commits to nothing the previous seller promised until it is verified, and takes the client's correction as the opening question of the first meeting (4.12, framing).

## 7. Never in client-facing material

**Client-facing means:** `sop/` (SOP.md, diagrams), `deliverables/` (recaps, handoff documents, future slide decks), anything written into the client's monday account (workspace, board and column names, descriptions, docs, item names, seed data, updates, dashboards, forms), any message the user will send — and anything on a shared screen, which no lint can see (architecture §9.11).

**Never include:**
1. Bleed and upside numbers, their inputs (hours, loaded hourly costs, salaries), and the math.
2. Emotional or personal stakes (embarrassment, credibility, burnout, personal reasons for wanting time back).
3. Objections, raised or anticipated, and planned responses.
4. Readiness grades, gaps, gap questions, gate status.
5. Stakeholder assessments: decision power, what each person cares about, attitudes, politics, who is a risk.
6. Closing tactics: deadline anchors, cost-of-waiting math, planned commitment questions, exit-ramp notes.
7. Pricing strategy, rates, margins, discount thinking.
8. Alternatives in play and what the client said about them.
9. Research inferences about the company or individuals, and [found]/[inferred] markers.
10. Demo scripts, prep blocks, call summaries, raw transcripts, recording links, `log.md` content.
11. Remarks by client staff about colleagues.
12. Other clients' names, data, or examples.
13. Method vocabulary: bleed, upside, callback, exit ramp, seed, readiness, pain IDs.
14. Backlog items framed as sales opportunities. A neutral "possible next improvements" list is fine when the user asks for it.
15. Maintenance promises — "set it and forget it" and every equivalent — and any automation described as maintenance-free.
16. Usage statistics, adoption percentages, client counts, other-client anecdotes, sector-experience claims and demand statistics about our own book, including in a self-introduction (0).
17. A vendor's data-handling, training, retention or compliance position asserted as ours; and a third party's such claim restated as ours. Point at the vendor's published documentation and let the client's security review own the question.
18. Our own operational data — engagement names, staff, hours, billable flags, rates or where they sit — on any screen or in any file (architecture §9.11).
19. A client's personal login as an access option, including as a hypothetical and including while naming the risk; the only access request is a named seat in the name of the person doing the work at the lowest level that can perform it (architecture §9.11).
20. A permission described as verified when the audit could only record it as not checkable; it is described as configured.

**May contain:** agreed goals and requirements in neutral wording and the client's vocabulary; the solution as built; how-to steps and process diagrams; agreed success criteria without money figures; agreed next steps, dates, and owners; the client's own SOP as the starting point for ours, reusing its vocabulary and structure and showing what changed (A16).

**Leak check** (before writing any client-facing file or writing into monday):
- Build a block list from the record: bleed, upside, and cost-input values from `discovery.md` Numbers in common formats (45000, 45,000, 45k, $45k) and in split renderings; objection text; stakeholder assessment text; names of alternatives in play; method vocabulary; pain IDs; evidence markers.
- Volume numbers (for example "12 projects a month") may be legitimate in an SOP: flag them for the user rather than removing them.
- Scan the draft, remove hits, tell the user what was removed. A small script is preferred where the environment can run one (node and python3 exist on the user's Mac); otherwise an explicit review step.
- **An authoring rule the lint cannot enforce:** outside a call folder, tool references are category words, and no more than one category is named per sentence. The combination of a client's tools identifies them even with every proper noun removed; the lint reaches only the three-in-one-sentence case.

### 7.1 Claims discipline in live speech

The rules above were written for generated text, and the most damaging claims in the evidence base were improvised answers to live questions, which no lint can reach: two prices for one purchase minutes apart, entitlement and scale answers guessed aloud, a completion figure spoken before any sight of the artefact. So the discipline reaches speech, through the prep pack, the register (4.12) and the correction loop.

- **No figure without a source.** Every figure spoken was read live at prep with its date or came from the user; an unsourced figure is answered with a refusal, never a range, because a range spoken aloud becomes the remembered price. The prep pack's "numbers we do not have" card names each category with no sourced figure and the sentence to say instead (4.1).
- **A commitment to check is exclusive of a figure in the same turn.** If the answer says we will confirm something, it carries no number, and the commitment is emitted as an owned to-do with a name and a date.
- **"It can" is not "I have."** Only *shown* and *buildable* capabilities are stated as capability (4.1); *unverified* is "I'd want to check that before I promise it", followed by the offer to build the smallest working version, run it once and measure. A plan-gated answer carries its gate.
- **No estimate for unbuilt or unread work** — no effort, duration or completion figure ("you're most of the way there", "that's a ten-minute setup") before scoping, in front of the person who will price the work, on any call where that person is present. The replacement is what has been seen so far, what still needs looking at before a number is put on it, and the artefact required first. No figure at all for work on a client-built artefact until we can read it (2.3).
- **No capability claim about a system nobody on our side has read.** Record what the client's own systems owner said, quoted and attributed; generate no capability, limit or flexibility statement of our own until the documentation has been read.
- **Never "we can change it later" unqualified.** Say what a conversion does and does not restore, grounded in our own probes.
- **Commercial and account-status statements are routed by who is in the room** (4.10): none after the approval owner has left, none in a group recap, one named owner in a co-sell seat.
- **No leading price question** (4.10), and no reasoning from one vendor's pricing to another's.
- **A figure or promise inherited from a colleague's earlier meeting** is verified with that colleague before it is repeated. A third party's claim made beside us is recorded verbatim, attributed and dated, never restated as ours, and the follow-up points at the published documentation so the client's review chases the right party.
- **The never-say list** the plugin keeps beside its platform gotchas (architecture §10.2) — multi-object asynchronous setup as a one-time mapping, a dashboard promised as working when widgets cannot be read back, a bulk action at a scale we have not run, a cascade edit answered with an unqualified yes, a permissions question answered with a views answer, file limits, metered-allowance behaviour, roadmap statements that a limit will rise — is read at prep and applied in the room.
- **The correction loop.** After the call, the delivery notes and the deferred-answer register (6.1) flag every unsourced figure, unverified capability, hedged answer and second-hand promise that was spoken. Each becomes an owned to-do or an entry on the next meeting's correction list, which the next run-sheet places before its first segment, so the correction is made in the room, attributed to us, and logged. The per-account claims store outside the record (architecture §9.12) catches contradictions across calls at prep; contradictions minutes apart inside one call are caught only by the rules above.

## 8. Method-to-record mapping

Paths are inside `~/DelOps/monday-master-builder-dev/clients/<slug>/`; strand-level paths are inside `strands/<id>/` (A14).

| Method element | File | Current or history | Notes |
|---|---|---|---|
| Pre-meeting research and hypotheses | `research/` | Current | [inferred] by default; never counts as rubric evidence; feeds objection anticipation |
| Raw transcripts | `calls/<date>-<type>.transcript.txt` | History, never edited | Recordings as links only. Saved only once the open transcript question is answered for this client; kept and archived per `transcripts_at_close`, which is open with no default [A11-3] |
| Client documents (A16) | `inputs/<date>-<title>.<ext>`, with its summary beside it as `inputs/<date>-<title>.md` | Raw, never edited; the summary a snapshot | Record level. Same lint, naming and retention rules as transcripts; the open A11 retention question covers them too [A11-3]. Author, date and status recorded, `unknown` where unstated; cited by document and section or page (architecture §7.5) |
| Per-call summary, type header, confirmation ledger entries, delivery notes | `calls/<date>-<type>.md` | History | 6.1; sequence, provenance and the strands served in its front matter |
| Meeting register: every meeting including ones never ingested, our presenter, the environment, who has seen what, the package block | `meetings.md` | History | Record level; predates any version |
| Readiness grades and gate status | `discovery.md` section 1; verdict line in `STRAND.md`; strand index in `CLIENT.md` | Current | 2.3-2.4 |
| Pains, numbers, why now, outcome, stakeholders, decision, objections, commitments, next step, vocabulary, client-built assets, expansion fields, consumption | `discovery.md` | Current | Changes noted in `log.md` |
| Front page: stage, top pains, why now, verdict, next step, open commitments, open overrides | `STRAND.md` | Current | Internal; `CLIENT.md` carries the client, the strand index, stakeholders and `prior_builds` |
| Open questions with kind, owner, what they block, best answer, how settled, bypassed | `solution/open-questions.md` | Current | Written by discovery-check; intake inserts; the blueprint marks bypassed. Source of the gap questions (2.5) |
| Gap questions for the next meeting | `discovery.md` Open questions, pulled into prep | Current | 2.5 |
| Discovery-meeting prep sheet | `calls/<date>-<type>-prep.md` | History | Written by discovery-check |
| Structure inventory and prototype inheritance record | `solution/structure-inventory.md` | Current | 2.6; written at intake after a reverse demo or prototype review; its read-back graded before the blueprint gate |
| Success criteria | `discovery.md` then `solution/blueprint.md` then v1.0 sign-off then `sop/SOP.md` (neutral wording) | Current | R6 |
| Pain-to-solution trace, structure mapping, forks, field authority | `solution/blueprint.md` | Current | Every element names its pain ID; untraced items move to the backlog; absent on a `non-platform` strand |
| Scope, open technical questions, dependencies, access needed, next steps, hand-off statement for non-platform work | `solution/scope.md` | Current | A13; on `non-platform` and `hybrid` strands only; ends with the statement that building happens outside the product |
| External dependencies with direction, latency, access and claims | `solution/dependencies.md` | Current | Provisional |
| Demo navigation targets | `solution/build.json` | Current | Demo script references keys and URLs from it |
| Seeds, out-of-scope asks, features with no pain | `solution/backlog.md` | Current | Source of v1.x callbacks; repeat counts across meetings and people |
| Demo asks in five states with repeat counts and verbatim answers | `solution/gaps.md` | Current | 4.6; feeds the spoken gap line and the most-repeated-ask refusal |
| Demo script (prep, segments, close) or scoping run-sheet | `versions/<version>/demo-script.md` | Frozen once used | Internal |
| Demo reactions and per-pain confirmations | `calls/<date>-demo.md`, then the version's reactions block in `versions/<version>/version.md` (the confirmation ledger), then pain status in `discovery.md` | History, then current | R11, 4.3 |
| Version changes and client feedback | `versions/<version>/` | History | Condense `discovery.md` at each version |
| Client recap draft | `drafts/<date>-recap.md` | History | Client-facing; leak-checked |
| Commitments, decisions, gate overrides, superseded numbers, conflicts, resolved objections, scope entries | `log.md` | History | Record level, one per client; every entry carries a strand field |
| Deferred and hedged answers, converted to commitments | `calls/<date>-<type>.md`, then `discovery.md` Commitments | History, then current | 6.1 |
| SOP and process diagrams | `sop/SOP.md`, `sop/diagrams/` | Current, grows progressively | Client-facing; leak-checked; starts from the client's own SOP where one exists (A16) |
| What is live in the account and what must not break | `live/live-map.md` | Current | Record level; read by every later strand (A14) |
| What a later strand reads of a closed one | `SUMMARY.md` | Current | At most 80 lines; the bloat control of A14 |
| Strand close-out; client card at record close | `close-out.md`; `client-card.md` | Snapshot; current | A14: a strand closes and the record stays open; the record close triggers the archive |
| Rate, approved claims, pricing inputs, plan-limit and quota figures read live | `~/DelOps/claims/<slug>.md`, outside the record | Current | The claims store (architecture §9.12); user-approved entries only |
| Voice: register, DO and DON'T lists, sentence shapes | `shared/house-style.md` in the plugin | n/a | 4.12; per speaker and per seat |
| Cross-client objection library | Outside client folders, anonymised | Grows | Optional; to confirm |

## 9. Scenario tests for the method

| # | Setup | Expected behaviour |
|---|---|---|
| 1 | Transcript with only a vague pain ("we want to be more efficient") | P1 Stated only; R2 Missing; verdict Not ready; next prep has concreteness and workaround questions |
| 2 | the user computes a yearly figure; client replies "mm" | R4 Partial; prep includes a confirmation question; pricing prep held |
| 3 | Client supplies hours and rate and says "probably more than that" | R4 Met with inputs, math, confirmation quote and location |
| 4 | Research suggests a pain the client never mentioned | Shown as [inferred]; no P# Met; appears only as a question |
| 5 | Transcript without speaker labels | Evidence "speaker unclear"; affected items Partial; no talk-share estimate |
| 6 | Later call contradicts an earlier number | Both statements kept with their call and speaker as an unresolved conflict; no arithmetic between them; a gap question for the next meeting. Only the same speaker correcting the same commitment inside one call sends the old value to `log.md` |
| 7 | 10-minute executive demo with five confirmed pains | Two segments (why-now pain first), others under "if asked", at most one gap question, commitment close |
| 8 | Client signals "that's exactly it" after segment 2 of 5 | Script's ramp note skips to the close; no further segments |
| 9 | In-house developer and earlier DIY attempt in the record | "Build it ourselves" listed as anticipated with signal, skipped step, prevention question |
| 10 | the user asks for a proposal, no verbal scope agreement in transcripts | No proposal draft; scope-confirmation step added to next prep; the user may override, logged |
| 11 | SOP and recap generated from a record full of bleed figures, objections, stakeholder notes | None of them appear; leak check reports clean or lists what it removed |
| 12 | Seed data for the monday build drafted from pains | Neutral, realistic names; no figures, emotional quotes, or internal notes |
| 13 | Call ends with "I'll follow up" | R10 Missing flagged; recap draft proposes a specific time; to-do for the invite |
| 14 | Support call without a forward-looking question | Short-version grade shows it missing; reminder in next check-in prep |
| 15 | Client quote with grammar slips or filler | Stored verbatim, not tidied |
| 16 | A package of four calls handed over by another seller, in a new export grammar, with a figure the seller re-quotes and two calls that contradict each other on a plan tier | Taken in as a set; ordered by date and internal evidence; the re-quoted figure recorded second-hand and not client evidence; the tier conflict kept as both statements with a gap question; graded and blueprinted once over the set |
| 17 | The client walks a prototype they built, and our side questions it hard for ten minutes | The fix-offered-mid-pain check does not fire; the structure inventory carries the prototype rows in their own class; current state is graded without them; the blocker in their words goes to client-built assets; no completion figure is quoted before the artefact is read |
| 18 | A demo to a room of ten in which three never speak; the presenter asks the room "anyone else?" at the end of a phase and a silent attendee raises a stake nobody knew | The open check-in is permitted and recorded as a discovered stake, not a confirmation; voices-missing lists the other two with their roles; nothing in the close reads the room |
| 19 | A working session ends with "book it through my assistant, this week, for the data walk-through" and the client says yes; a demo ends the same way | Working session: R10 Met on the mechanism with owner, purpose and assent. Demo: R10 not Met; the summary flags it and the recap proposes a time |
| 20 | Mid-demo the client asks how many rows a board can hold; no figure was read at prep | The prep pack's card supplies the refusal and the sentence to say instead; the answer carries no number; an owned to-do to read the live limit, with a name and date, goes to the summary; the answer is on the next meeting's correction list |
| 21 | A strand whose deliverable is a script against a third-party system | Scope, open questions, dependencies, access and next steps recorded in `scope.md`; the file ends with the hand-off statement; no blueprint, build, demo or audit is offered |
| 22 | The client's SOP says approvals go through one desk; on the call the operator says nobody uses that step | Both recorded with their sources as a conflict and a callback candidate; the current-state picture carries the lived version, the document is cited by section, and neither is discarded |
| 23 | A client document arrives before any call | Chained to the discovery check as a discovery call would be, and graded on its own under the document rules, with no call type proposed and nothing dropped to advisory for the header it does not carry: current-state and requirements criteria may be Met from it, cost, why-now, decision and next step stay Missing unless stated explicitly; every gap it cannot fill is shown |

## 10. Adapted or dropped from the sources

- **Adapted:** CRM updates became client-record updates; team handoffs dropped for a solo consultant (revisit when folders are shared with teammates); objection library feeding the playbook became recurring-objection prep, with a cross-client library as an option; monthly self-review became optional per-call delivery notes with one takeaway.
- **Dropped:** tone-of-voice coaching (plain text cannot carry it), manager reviews, peer cadence comparisons, weekly and monthly rep progression, the influence's question-stage names and tone taxonomy, all long example dialogues, the previous company's rate, deal sizes, and client-count claims.
- **Added (not in sources):** the adoption objection, stage gates and verdict thresholds, the leak check, timing budgets per segment, version variants for demos.
- **Added from the real-call calibration (2026-09-12):** the two check-ins, the confirmation ledger, the scoped reverse-demo discipline, the close as a discipline of its own with the mechanism next step, call type and per-segment grading, expansion mode, the obtainability map, the bleed states below Met, group-call and co-sell guidance, claims discipline in speech with the correction loop, and the voice section. Roughly twenty of the underlying rules rest on a single observation and are marked provisional here as they are in the lessons file; they are hypotheses until the second observation arrives, and none has been laundered into a rule.

## 11. Open questions for the user

1. Should a "Not ready" verdict block the blueprint, or only warn with a logged override? (Proposed: warn, but require R1 Partial and R2 Met.)
2. Pricing, proposals and ROI documents stay out of v1 (SPEC); metered consumption is in, as a design input (2.3). The rate, approved credentials and claims live in the claims store outside the record (architecture §9.12, D27). Still open: where consumption sits relative to the bleed frame — inside it or in a section of its own — since a budget holder asks about both in one breath.
3. Does the user want a cross-client objection library, and where (anonymised, outside client folders)?
4. May any client-facing document, such as a proposal or ROI summary, ever show the client's own cost figure, or is the exclusion absolute?
5. File locations are now settled by the architecture (8); no longer open.
6. Is R5 (upside) advisory for every engagement, or core for some (for example sales-team buyers)?
7. Transcript sources: intake now measures every file before reading it and classifies by shape, so no fixed list of sources is needed; delivery notes run wherever speakers are labelled. What remains open is the transcript redaction and retention policy, asked before the first real client transcript is saved [A11-3].
8. Delivery notes ship in v1 as scoped in 6.5; whether the group-call decomposition earns its place is judged after the first real group call.
9. Should the recap draft be produced after every call automatically, or only on request?
10. When folders are shared with teammates later, may internal notes (stakeholder assessments, objections) be visible to them?
11. In a partner-led seat with no third party to vouch, what credential substitutes for the banned client-count claim (0)? The user's call.
12. May the user hold to a date-on-the-call rule for working sessions too, or is the mechanism state the permanent standard there? The evidence says no call fixed a new date; the method holds the date for discovery and demo calls (2.3) and asks whether the user wants to raise the bar elsewhere.
