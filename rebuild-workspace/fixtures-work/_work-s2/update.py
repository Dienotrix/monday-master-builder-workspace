#!/usr/bin/env python3
"""Apply the v1-scope revision to the s2 answer key.

Rebuilds the key in the canonical 25-field order, replacing only the fields the
revision touches. Everything else is carried through untouched.
"""
import json
from collections import OrderedDict

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s2-discovery-gaps/"
k = json.load(open(BASE + "answer-key.json", encoding="utf-8"))

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]

# ---------------------------------------------------------------- purpose
k["purpose_of_this_fixture"] = (
    "Tests gap detection on a weak discovery call at a residential pest control and lawn care company "
    "(about 60 technicians, two branches). Attending: a customer service lead and a dispatcher. The owner, "
    "Gary, is the real decision maker and is only mentioned. The consultant pitches before listening, offers "
    "fixes while the client is still describing pains, never works out a cost, accepts a vague why-now, "
    "pitches an unrequested customer self-service form that draws a polite hedge ('Oh. Huh. That sounds "
    "interesting.'), promises rough pricing, and ends with 'I'll send something over' and no date, time or "
    "owner. Expected behaviour: (1) Rubric: Partial for R1 to R9; Missing for R10, R11 and R12; nothing Met. "
    "R2 is Partial because no pain is excavated: P1 and P2 each have Stated and Concrete Met, but both clients "
    "defend their workaround ('the sheet's fine', 'the board works') and are cut off before saying why it "
    "cannot continue. R4 is Partial on a single hours figure (about two hours every morning) with no cost. "
    "(2) Record that hours figure as a cost input without inventing a wage, season length, weekly total or "
    "yearly bleed. (3) Verdict 'Nearly ready' by the section 2.4 rule, but the blueprint gate fails (R2 not "
    "Met) and pricing prep is held (R4, R7, R12 not Met). The plugin must not propose a blueprint, build or "
    "pricing. It produces a discovery prep with at most five gap questions, core criteria first, and a recap "
    "draft that proposes a specific time with Gary invited. (4) Product fit under v1 scope, which is Work "
    "Management plus CRM plus Service: Work Management is the build target for dispatch exceptions, lawn "
    "rounds and add-on requests, and monday Service is the build target for the intake the consultant kept "
    "pitching (re-treats, callbacks and complaints), because Service is in v1 at the same depth as CRM. The "
    "Service work must land on the account's NATIVE Service Tickets board, never a look-alike request board "
    "in Work Management and never the client's own 'service ticket', which is the visit record in their legacy "
    "software. The Service extras the consultant pitched hardest -- email-to-ticket intake, a customer "
    "self-service portal form and response targets that turn a complaint red -- are deferred beyond v1 and "
    "must not be named as deliverables. Do not choose monday CRM after Marisol deflected that pitch. Service "
    "being in scope does not open the blueprint gate: still no build. (5) Treat pitched features that drew "
    "hedging as backlog, not needs. (6) Flag delivery issues: client talk share about 56% (under the 60% "
    "target), one consultant turn of about 245 words with no question (the opening product tour) and another "
    "of about 170 words (the routes-board pitch), fixes offered mid-description, and no commitment question. "
    "expected_questions_before_building is the full pool in priority order, not a list to ask in one meeting. "
    "account_context, expected_structures, accepted_behaviours and expected_leak_blocklist carry the "
    "account-shape, native-board, grader-tolerance and leak-check expectations."
)

# ---------------------------------------------------- expected_monday_products
k["expected_monday_products"] = [
    {
        "kind": "core",
        "why": (
            "monday Work Management: build target once the blueprint gate is met or the consultant overrides "
            "it. It covers the work that is not request intake: daily dispatch exceptions by technician "
            "(call-outs, trucks down, re-treats to slot in, rain-day pushes), lawn plans and rounds with a "
            "timeline view and dependencies for the rain pushes, the notify-list call before spraying, skips "
            "that quietly become cancels, and add-on requests technicians flag on tickets. These are ordinary "
            "boards, so the native-board rule (A5) does not apply to them, and no portfolio is expected "
            "(see expected_structures). It sits next to 'the system', which stays the record for customers, "
            "plans, routes and state application records unless Gary decides otherwise."
        )
    },
    {
        "kind": "service",
        "why": (
            "monday Service: also a build target, because Service is in v1 at the same depth as CRM. The "
            "intake the consultant pitched repeatedly is a real fit -- re-treat and callback calls that "
            "currently stall between the callback sheet and the whiteboard, and complaints arriving from the "
            "phones, the office inbox, the website, online reviews and the owner's cell. These become items "
            "on the account's NATIVE Service Tickets board (A5), never a look-alike request board built in "
            "Work Management. Two hard limits. First, the deferred extras: the customer self-service portal "
            "form, email-to-ticket channels and SLA or response-target setup are out of v1, which strips out "
            "most of what the consultant actually demonstrated in words ('You could put a form right on your "
            "website', 'So all of that, the email, the phone, the website, it all lands in one place as "
            "tickets.', 'so if a complaint hasn't been touched by end of day it goes red'); requests still "
            "get in by manual entry or a plain monday form, and ageing is a status and a view rather than an "
            "SLA policy. Second, the vocabulary clash: Marisol corrected the consultant that 'a service "
            "ticket for us is the actual visit. That's in the system.', so native Tickets items are their "
            "call-ins, not their visits. Nothing is built yet: the blueprint gate is shut."
        )
    }
]

# ---------------------------------------------------------------- objections
OBJ = [
    ("We tried a scheduling thing, like, three years ago? Some app. Gary bought it. Nobody used it.",
     "Team won't adopt it (past failed rollout; brushed off by the consultant, not explored)"),
    ("I've got guys who still want the paper sheet.",
     "Team won't adopt it (technicians prefer paper)"),
    ("Oh, the guys are gonna love that.",
     "Team won't adopt it (sarcasm about per-technician complaint reporting)"),
    ("Because Gary's going to ask what it costs.",
     "Price feels high (anticipated on behalf of the absent owner; the skipped step is R4)"),
    ("do they each need, like, a login? Because it's sixty guys.",
     "Price feels high (seat cost for about 60 technicians plus seasonal hires; answered with unverified "
     "licensing advice)"),
    ("Well, Gary would have to see it.",
     "Must check with someone (the approver was not on the call)"),
    ("Just not in the spring.",
     "Wrong time, next quarter (busy season, March to June)"),
    ("Oh, I don't think Gary's getting rid of the system.",
     "Outside the map: the existing system stays (scope and integration concern). Not 'monday itself is the "
     "problem': they are defending their own legacy software, not criticising monday"),
    ("I mean, it has to be in the system, though.",
     "Outside the map: compliance and data location (state application records must stay in the legacy system)"),
    ("Oh. Huh. That sounds interesting.",
     "Outside the map: polite hedge after an unrequested feature pitch (customer self-service re-treat form, "
     "itself a deferred Service extra); hesitation, not interest"),
    ("Our customers are, like, seventy.",
     "Outside the map: fit of a pitched feature (customer self-service request form)"),
    ("Yeah. No, maybe.",
     "Outside the map: polite hedge (same self-service form pitch, after the consultant pressed on)"),
    ("Hm. Maybe. That's more Gary's side.",
     "Outside the map: deflection of the monday CRM pipeline pitch (not their decision)"),
    ("honestly the board works. It works.",
     "Outside the map: status quo defended right after the routes-board pitch (the skipped step is the "
     "workaround check)"),
    ("He's not really a dashboard guy.",
     "Outside the map: fit of a pitched feature (owner dashboard)"),
    ("That's a lot of boards.",
     "Outside the map: complexity concern (hedge on the proposed structure)"),
]
k["objections"] = [{"quote": q, "type": t} for q, t in OBJ]

# ---------------------------------------------------------------------- traps
traps = list(k["traps"])


def replace_trap(startswith, new):
    for i, t in enumerate(traps):
        if t.startswith(startswith):
            traps[i] = new
            return
    raise SystemExit("trap not found: " + startswith)


replace_trap(
    "monday service is a natural fit",
    "Service is in v1, so the intake the consultant pitched is genuinely in scope -- but it must go on the "
    "account's native Service Tickets board, not a look-alike. The tempting wrong move is a Work Management "
    "board called Tickets, Requests or Callbacks, built because today's intake lives on a Google Sheet. See "
    "expected_structures.lookalike_traps. In-scope does not mean build: the blueprint gate is still shut, so "
    "Service appears as the intended target, not as created objects."
)
replace_trap(
    "'Service ticket' is a scheduled visit",
    "'Service ticket' is a scheduled visit in the system, not a customer request. Marisol corrected the "
    "consultant's 'that call becomes a ticket'. This collides with monday Service, whose native items are "
    "called tickets: their call-ins are the native Tickets items, their visits are not. Do not rename the "
    "native Tickets board to their meaning, do not map visit records onto it, and expect to need a different "
    "word for one of the two in anything client-facing."
)
traps += [
    "The deferred Service extras are exactly what the consultant demonstrated most vividly: a customer "
    "self-service form on the website, everything landing as tickets from the email inbox, and response "
    "targets that turn an untouched complaint red. All three are out of v1 (portal, email-to-ticket, SLA "
    "setup), and the form was hedged anyway. Intake starts as manual entry or a plain monday form, and "
    "ageing is a status plus a view, not an SLA policy. Naming any of them as a v1 deliverable is the trap.",
    "The AI pitch (reading email, tagging complaint versus re-treat versus billing, sentiment, draft replies) "
    "hangs off the deferred email intake and was never requested. Backlog, not blueprint.",
    "No monday account exists ('No. I've seen the ads.'), so native-board detection (A5 layer 1) has nothing "
    "to run against and no board ids can be recorded yet. Do not claim boards were detected, and do not "
    "assume which Service template family a future account will have.",
    "No account tier was discussed, so the Enterprise portfolio default (A6) does not apply. Do not infer "
    "Enterprise from about 60 technicians or two branches, and do not read the consultant's suggestion that "
    "North could get a copy of the same setup as a portfolio of connected projects. Their work is recurring "
    "plans, rounds and routes, not projects.",
    "The consultant's multi-board sketch ('you'd have a customers board, a plans board with every plan and "
    "what round they're on, a routes board for Travis') drew 'That's a lot of boards.' A board named Contacts "
    "or Accounts would also sit on native CRM entity names while CRM is deliberately out of scope. Use their "
    "vocabulary, keep customer records where they said they live (the system), and ask before creating a "
    "customer board at all.",
]
k["traps"] = traps

# -------------------------------------------------------------- verdict note
k["expected_verdict"]["note"] = (
    "By section 2.4, R2, R3, R4 and R7 are all Partial and none is Missing, so the verdict is 'Nearly ready'. "
    "One-line reason: pains are named but not excavated, the why-now is vague, there is one hours figure with "
    "no cost, and the owner who decides was not on the call. This is not permission to build or price. The "
    "plugin should offer a discovery prep (at most five gap questions, core first), flag R10 Missing, and have "
    "the recap draft propose a specific time with Gary invited. If the consultant overrides the blueprint "
    "gate, the override is logged and the blueprint targets Work Management for dispatch, rounds and add-on "
    "requests plus monday Service for re-treat, callback and complaint intake on the account's native Tickets "
    "board, with the portal form, email-to-ticket and response-target extras listed as deferred beyond v1 and "
    "automations presented as one list for a single approval. A grader who reads R3 as Missing gets 'Not "
    "ready'; the gates and expected actions are the same either way."
)

# ------------------------------------------------------------ account_context
k["account_context"] = {
    "tier": (
        "unknown. No plan, tier or seat count was discussed. The only pricing exchange was Travis asking "
        "whether about 60 technicians each need a login and the consultant answering that 'it's priced by "
        "seat, but there's some ways around that, like forms, guest access'. Do not infer Enterprise, and do "
        "not infer a tier from headcount or from two branches."
    ),
    "products_enabled": [],
    "existing_monday_setup": (
        "None. Quillmoor has no monday account, workspace, board or earlier build, and nobody on the call has "
        "used monday: Marisol has seen advertising and is unsure whether Kelsey, the owner's daughter, used it "
        "at a previous employer ('Kelsey said she used it at her old job, maybe? Or it was a different one.'). "
        "Consequences for the plugin: there is nothing to audit or extend; native-board detection (A5 layer 1) "
        "cannot run and no board ids can be recorded, so for Service the blueprint names the native Tickets "
        "entity and defers id capture to a preflight once an account exists; the account tier that drives the "
        "portfolio default (A6) is likewise unknown. Kelsey's possible monday experience and her ownership of "
        "the callback sheet and the website make her an unknown stakeholder worth asking about."
    ),
    "evidence_quote_or_null": "No. I've seen the ads."
}

# --------------------------------------------------------- expected_structures
k["expected_structures"] = {
    "native_boards_required": [
        {
            "product": "service",
            "entity": "Tickets",
            "why": (
                "Re-treat and callback call-ins and complaints are one intake queue, and that is the Service "
                "Tickets entity. Today they are split across the Google Sheet callback sheet, the dispatch "
                "whiteboard, Marisol's email folder and the owner's cell ('Everywhere. The phones, the office "
                "inbox, the website.'). Under A5 these items must live on the account's native Service Tickets "
                "board, found by the detection rules and recorded by id -- which cannot happen until an "
                "account exists. Native Tickets items are their call-ins, not their 'service ticket' visits."
            )
        }
    ],
    "portfolio_expected": False,
    "portfolio_reason": (
        "A6 applies only when the account tier is Enterprise and Work Management is in scope. There is no "
        "monday account and no tier was discussed, so the Enterprise condition is not met and the default does "
        "not apply; record that reason rather than treating it as a silent skip. Nothing in the transcript "
        "asks for a portfolio either: the two branches are a single distinction on items (main branch on "
        "Tolliver Road, North), the consultant's suggestion that North could get a copy of the same setup is "
        "duplication rather than connected projects, and the work itself is recurring plans, rounds and routes "
        "rather than projects. Revisit if Gary turns out to be on Enterprise and Work Management is built. No "
        "build is proposed at this stage in any case."
    ),
    "lookalike_traps": [
        "A Work Management board named Tickets, Requests, Callbacks or Re-treats holding the call-ins and "
        "complaints. This is the central look-alike trap of this fixture: it is the natural move, because "
        "intake lives on a spreadsheet today and Work Management is the other in-scope product, and A5 "
        "forbids it now that Service is in v1.",
        "Rebuilding the callback sheet column-for-column as its own plain board (customer, address, what's "
        "going on, plan, which tech was out last) instead of as columns on native Tickets.",
        "Splitting complaints onto a second look-alike board because they arrive through different channels. "
        "One native Tickets board with a request-type label covers re-treats, callbacks, billing questions "
        "and complaints; their own words already distinguish these.",
        "Duplicating the native Tickets board per branch or per request type. A duplicate of a native board "
        "still trips the A5 guard; use groups, views and a branch column instead.",
        "Naming a Work Management board Contacts or Accounts for the customers board the consultant sketched. "
        "Those are native CRM entity names, and CRM is deliberately out of scope here after Marisol deflected "
        "the pitch, so such a board is both a look-alike and unrequested. Their customer record stays in the "
        "system unless Gary says otherwise.",
        "Creating a look-alike Activities or Leads board for the add-on requests technicians write on tickets "
        "('that's supposed to come to us as a lead, so we can call them.'). Marisol handed the sales side to "
        "Gary, so this is a simple Work Management item, not a CRM entity."
    ],
    "notes": (
        "Nothing here is a build instruction for this fixture: the blueprint gate is shut (R2 Partial), so "
        "expected_structures describes what a correct blueprint would have to respect if the consultant "
        "overrides the gate later, and what a wrong one would look like. The Work Management pieces (dispatch "
        "exceptions, plans and rounds, skips, add-on requests) are ordinary boards, so A5 does not apply to "
        "them and no native template is required. For Service, only the Tickets entity is required; the native "
        "companions that ship with the Service templates (Contacts, CSAT Survey, and the IT-flavoured "
        "Incidents, Asset management and directory boards) are not required here -- customer records stay in "
        "the system, satisfaction surveying never came up, and the IT families do not fit a home-services "
        "business. If the client later wants customer records in monday, that is a scope question for Gary, "
        "not a board to add quietly. Automations across both products are presented as one list for a single "
        "approval, each row naming trigger, conditions, action and exact recipients, with the note that "
        "API-created automations cannot be switched off through the API."
    )
}

# -------------------------------------------------------- accepted_behaviours
k["accepted_behaviours"] = [
    "Grading R3 as Missing instead of Partial, which yields 'Not ready' instead of 'Nearly ready'. The gates, "
    "the held pricing and every expected action are identical either way, so both readings pass.",
    "Grading R5 as Missing instead of Partial. R5 is advisory and changes no verdict or gate.",
    "Grading P1 Workaround and P2 Workaround as Missing instead of Partial. What matters is that neither is "
    "Met, so no pain is excavated and R2 stays Partial.",
    "Either naming monday Service as the intake target outright, or naming it while asking first whether "
    "re-treats and callbacks should live in monday at all given that 'the system' generates the visits. Both "
    "are correct; silently designing intake in Work Management is not.",
    "Sketching the intended shape (native Tickets for call-ins and complaints, Work Management for dispatch "
    "exceptions, rounds and add-on requests) as a clearly labelled proposal pending the gate, rather than "
    "withholding all structural thinking. What must not happen is a blueprint presented as approved, a build, "
    "or any created object.",
    "Listing the deferred Service extras explicitly as deferred, or leaving them out entirely. Both keep them "
    "out of v1; presenting any of them as a deliverable does not.",
    "Using the client's vocabulary instead of monday's for the intake items (a request, a callback, a "
    "call-in), as long as the underlying board is the native Service Tickets board. Their 'service ticket' "
    "must not be the label for it.",
    "Fewer than five gap questions, or a different subset of expected_questions_before_building, as long as "
    "core criteria (R2, R3, R4, R7) come before gate and advisory items and the pool is not exceeded.",
    "Delivery-note figures within a couple of points or tens of words of the key's estimates (client share "
    "about 56%, a 245-word and a 170-word consultant turn). These are word-count estimates on an untimed "
    "transcript, not exact measurements, and a plugin that declines to estimate talk share at all while "
    "noting the long unbroken turns is also acceptable.",
    "Recording the two-hours figure as a cost input, or as an unquantified volume note. Either is fine; "
    "multiplying it into a weekly or yearly bleed is not.",
    "Naming Kelsey, Lorna, Gary or Rhonda as stakeholders with unknown or unconfirmed roles, or listing them "
    "as open questions instead. Asserting a decision role for any of them is not acceptable.",
    "Either treating the North branch as out of scope for now or listing it as an open scope question. "
    "Assuming it is included, as the consultant did, is not."
]

# ---------------------------------------------------- expected_leak_blocklist
k["expected_leak_blocklist"] = [
    "Cost inputs and any figure derived from them: 'two hours', '2 hours', 'two hours every morning', 'two "
    "hours a day', and any weekly, seasonal or yearly total or money value built from them (10-12 hours a "
    "week, 500 hours a year, a dollar bleed). None of this reaches a recap, an SOP, seed data or the monday "
    "account. There is no confirmed bleed or upside total in this record to block, which is itself the point: "
    "if a figure appears in a draft, it was invented.",
    "Any hourly rate, wage or loaded cost. None was ever given, so any such number is fabricated as well as "
    "internal.",
    "Method vocabulary: bleed, upside, exit ramp, callback in its method sense (opening a demo segment by "
    "pointing at a stated pain), seed or seed data, readiness, excavated, gate or gate status, verdict, "
    "'Nearly ready', 'Not ready', 'Discovery complete'.",
    "CAUTION, do not strip: 'callback', 'callback sheet' and 'callbacks' are this client's own words for a "
    "real work item and belong in board names, an SOP and the recap. Only the method's sense of the word is "
    "blocked, and it never appears in client-facing text anyway. A naive block list that removes the client's "
    "term breaks the deliverable.",
    "Identifiers and markers: P1 to P7, R1 to R12, N# number ids, S# stakeholder ids, O# objection ids, C# "
    "commitment ids, '[found]', '[inferred]', 'Partial', 'Met' and 'Missing' as grades.",
    "Objection text and the fact that anything was treated as an objection: 'Because Gary's going to ask what "
    "it costs.', 'Well, Gary would have to see it.', 'Just not in the spring.', 'That's a lot of boards.', "
    "'Our customers are, like, seventy.', 'Hm. Maybe. That's more Gary's side.', 'He's not really a dashboard "
    "guy.', 'Oh, I don't think Gary's getting rid of the system.', 'We tried a scheduling thing, like, three "
    "years ago? Some app. Gary bought it. Nobody used it.', 'I've got guys who still want the paper sheet.', "
    "'Oh, the guys are gonna love that.', plus the anticipated-objection labels and planned responses.",
    "Stakeholder assessments: that Gary is the approver or decision maker, that Marisol is an influencer, that "
    "Travis is an end user, that the person who decides was absent, that Kelsey or Lorna are unknown "
    "stakeholders, and anything about what Gary cares about or how he buys.",
    "Emotional and personal stakes: 'she wasn't crying, but she was upset', 'And then she's asking for Gary. "
    "And then Gary's asking me.', 'Gary took that pretty hard', 'He printed one out', 'Kind of in a mean "
    "way.', 'My step count's great, though.'",
    "Remarks by staff about colleagues: 'Hector will die before he gives up the paper', 'Hector's gonna be "
    "buried with a clipboard', 'He knows the dogs better than the customers.', 'The ticket's under the seat "
    "with a gas station burrito wrapper.', 'I have no idea how billing works.', 'she has her own spreadsheet', "
    "'It's a different everything up there.', and the North-branch comparisons generally.",
    "Closing and pricing thinking: the held pricing prep, the promise 'I'll put some ballpark numbers in there "
    "for him.', seat-count sizing, cost-of-waiting framing, the planned commitment question, and the note "
    "that the spring blackout is a scheduling lever.",
    "Consultant claims repeated as fact: 'in monday that basically can't happen', 'monday connects to pretty "
    "much everything.', 'Most people pick it up in a day, honestly.', 'it's priced by seat, but there's some "
    "ways around that, like forms, guest access'. Not internal exactly, but unverified, so they must not "
    "appear as commitments in a recap, an SOP or a board description.",
    "Backlog framed as an upsell: the customer self-service form, AI tagging and draft replies, the owner "
    "dashboard, the CRM pipeline for add-ons, the map view, per-technician complaint reporting. A neutral "
    "'possible next improvements' list is fine if the consultant asks for one.",
    "FLAG, do not remove automatically: volume figures that could legitimately belong in an SOP -- 'Fifteen, "
    "twenty a week, maybe?' and 'Summer's like double' for re-treat calls, about 60 technicians, six or seven "
    "lawn rounds a year, the thirty-day one-time re-treat window, six rounds, quarterly plans. Show these to "
    "the consultant rather than stripping them, and keep the hedging if they stay.",
    "Sensitive operational detail that must not land in seed data or examples even though it is the client's "
    "own: the Pheasant Run customer who called three times, real gate codes, lockbox codes, dog notes, "
    "notify-list medical reasons, and the owner's personal cell as a channel. Seed data uses invented "
    "addresses and no access codes.",
    "There are no alternatives in play in this record -- no other partners, vendors or in-house build plans "
    "were mentioned -- so that category of the block list is empty by design. The abandoned scheduling app is "
    "a past failure and an adoption signal, not an alternative, and stays internal on those grounds."
]

out = OrderedDict((f, k[f]) for f in ORDER)
assert set(out) == set(k), (set(k) - set(out), set(out) - set(k))
with open(BASE + "answer-key.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("written; fields:", len(out))
