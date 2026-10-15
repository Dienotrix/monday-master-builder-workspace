#!/usr/bin/env python3
"""Apply the v1-scope amendments to the s1 answer key.

Adds account_context, expected_structures, accepted_behaviours and
expected_leak_blocklist; applies the v1 product scope; standardizes objection
types and decision roles to the method spec's vocabulary.
"""
import json
from collections import OrderedDict

KEY = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s1-discovery-strong/answer-key.json"

FIELD_ORDER = [
    "scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
    "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
    "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
    "objections", "commitments_and_next_steps", "traps", "requested_changes",
    "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
    "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist",
]

with open(KEY, encoding="utf-8") as f:
    k = json.load(f, object_pairs_hook=OrderedDict)

# ---------------------------------------------------------------- 3. vocabulary
# Objection types and decision roles use the method spec's vocabulary.
OBJECTION_TYPES = {
    "Honestly? The PMs. We tried a project management tool, I want to say four years ago, and it was dead in about two months.": "Team won't adopt it",
    "Double entry. You had to put your stuff in there and still do everything else you were already doing.": "Team won't adopt it",
    "And nobody asked the PMs what they wanted before we bought it.": "Team won't adopt it",
    "We've got four CD sets going out in October. Nobody's going to want training in October.": "Wrong time, next quarter",
    "And if Bev decides this is going to mess with Ajera, that's a hard stop.": "Must check with someone",
    "So I own the operations systems budget. But anything over twenty-five thousand, Gordon signs.": "Must check with someone",
    "Ideally the whole thing's live before Des Moines opens. But, I mean, I don't want to hold anyone to that. Let's see what it looks like first.": "Needs to think it over",
}
for o in k["objections"]:
    o["type"] = OBJECTION_TYPES[o["quote"]]

DECISION_ROLES = {"Tess Kowalczyk": "approver", "Jordan Pruitt": "influencer"}
for a in k["attendees"]:
    if a["name"] in DECISION_ROLES:
        a["decision_role"] = DECISION_ROLES[a["name"]]
for a in k["attendees"]:
    if a["name"] == "Tess Kowalczyk":
        a["role"] = ("COO. Finance, IT, HR and operations report to her. She approves the operations "
                     "systems budget, but spend over $25k needs the managing partner (Gordon, not on "
                     "the call), and she wants him on board either way. She and Jordan would own the "
                     "rollout.")

# Native-board wording in the vocabulary, so the key does not describe look-alike boards.
VOCAB_OBJECTS = {
    "pursuit": "item on the native CRM Deals/Opportunities board, relabelled to the client's word 'pursuit' (not a look-alike Pursuits board)",
    "pursuit log": "the native CRM Deals/Opportunities board with its pipeline stages (not a new look-alike board)",
    "owner": "item on the native CRM Accounts board, connected to pursuits and jobs (the client's 'owner', not a monday item owner)",
}
for v in k["vocabulary"]:
    if v["their_term"] in VOCAB_OBJECTS:
        v["likely_monday_object"] = VOCAB_OBJECTS[v["their_term"]]

# ------------------------------------------------- 2. v1 scope on the products
for p in k["expected_monday_products"]:
    if p["kind"] == "crm":
        p["why"] += (" CRM is in v1 scope and must be built on the account's own native CRM template "
                     "boards (Leads, Contacts, Accounts, Deals/Opportunities, Activities), detected in "
                     "the account first and relabelled to the client's words where that helps, never "
                     "re-created as look-alike boards.")
    if p["kind"] == "core":
        p["why"] += (" Work Management is in v1 scope. Whether it also gets a portfolio with connected "
                     "projects depends on the account tier, which the call never states, so that is a "
                     "question rather than an assumption. monday Service and monday Dev are not "
                     "proposed: no ticket or request desk and no software development work were "
                     "described, Dev is out of v1 in any case, and the basic submittal log the client "
                     "asked for stays in Work Management next to the jobs.")

# --------------------------------------------------------- 2. v1 scope: traps
k["traps"] += [
    "The account tier is never stated on the call, so it is 'unknown' and has to be asked. Do not assume Enterprise and do not add a portfolio by default. If the account turns out to be Enterprise with Work Management in scope, a portfolio with connected projects is the default shape, and the reason for including or leaving it out is recorded either way.",
    "CRM has to be built on the account's native CRM template boards. 'Pursuits' and 'owners' are the client's labels for deals and accounts, not a reason to create new look-alike boards; find the native boards in the account first and map pursuits, owners and their contacts onto them.",
    "There is no usable monday account to build on yet: Anneke's free board lapsed ('It kind of fizzled when the trial ended and nobody was paying for it.') and even its survival is a guess ('Probably? I'd have to ask her.'). Which account, workspace and products exist is unknown, so native-board detection and the account question come before any build.",
    "Submittals look like a ticket queue with an SLA ('most of our contracts say ten business days. Some say fourteen calendar days.', plus a GC's delay letter), but the client asked for a basic submittal log kept light and alongside the jobs. Service extras (customer portal, email-to-ticket, SLA policy setup) are deferred beyond v1, so do not offer them here.",
    "Automations are approved once as a single list, with each row naming its trigger, conditions, action and exact recipients. Automations created through the API cannot be switched off through the API, so the list has to say so and the handoff needs a 'turn off in monday' step for each one.",
    "Objection status: all seven entries are anticipated or raised as blockers, and none was resolved on the call. The three PM-adoption lines are one recurring concern in three quotes, not three separate objections, and Tess's go-live line is a soft hedge rather than a stated refusal.",
    "Pricing and proposal prep are out of v1, and R12 is Partial in any case, so produce neither: no price, no proposal, no ROI sheet, even though the client has a budget date on October 1 and Gordon 'signed it in about a week' last time when the numbers were clear.",
]

# --------------------------------------------------------------- 1. new fields
k["account_context"] = OrderedDict([
    ("tier", "unknown"),
    ("products_enabled", [
        "unknown: nothing in the call says which monday products or seats the firm has today",
        "No paid subscription at the time of the call. The only monday use was one free board that lapsed when its trial ended, so treat Work Management and CRM as products to be provisioned, not found",
        "Whether the old free account or workspace still exists at all is unconfirmed ('Probably? I'd have to ask her.')",
    ]),
    ("existing_monday_setup", "Effectively none. Anneke (interiors, half PM and half designer) built one free monday board last year to track FF and E (furniture, fixtures and equipment) selections on a couple of jobs. She liked it, nobody else ever touched it, and it fizzled when the trial ended. Jordan thinks it probably still exists but would have to ask her, and says there is nothing in it the firm would need. FF and E is not in scope, so nothing is inherited: no boards, columns, automations, users, permissions or data to audit, extend or migrate. Tess treats the board only as evidence that a non-technical person could build something herself ('Anneke is not a tech person and she built that herself in an afternoon.'). The plugin should ask which account the build goes into, who administers it, and which products and seats are being bought, before designing anything that depends on the answer."),
    ("evidence_quote_or_null", "It kind of fizzled when the trial ended and nobody was paying for it."),
])

k["expected_structures"] = OrderedDict([
    ("native_boards_required", [
        OrderedDict([
            ("product", "crm"),
            ("entity", "Deals/Opportunities"),
            ("why", "Pursuits are the agreed first scope item and are a deal pipeline: intake, go/no-go, PIC and PM assignment, fee proposal and Gordon's fee sign-off, due date and addenda, submission, short list, interview, won or lost. This has to be the account's native Deals (Opportunities) board relabelled to 'Pursuits', not a new board that looks like one."),
        ]),
        OrderedDict([
            ("product", "crm"),
            ("entity", "Accounts"),
            ("why", "The client's 'owner' is the buying organisation: a city, a school district or a county ('The owner is the building owner, the client. The city, the school district, whoever.'). Larkspur Falls School District, the Rockford clinic owner and the county behind the jail addition are all accounts, and both pursuits and jobs hang off them, including repeat work such as the facilities study that preceded the Larkspur Falls RFP. Use the native Accounts board, not an 'Owners' look-alike."),
        ]),
        OrderedDict([
            ("product", "crm"),
            ("entity", "Contacts"),
            ("why", "Named people on the owner's side appear in the call (a facilities director who gave feedback after the loss, a school board that later disputes an approval, GC contacts during CA), and PICs win work through those relationships. Where such contacts are kept today was never discussed, so this is a scope question first; if contacts are in the build, they go on the native Contacts board."),
        ]),
        OrderedDict([
            ("product", "crm"),
            ("entity", "Leads"),
            ("why", "Only if the client wants a stage before go/no-go. Intake here is an RFP or RFQ from a bid portal or a PIC's call, not a person-shaped lead, so it may belong as an early stage on the pursuit itself instead of a separate Leads record. Ask; if Leads are used, use the native Leads board and its native convert path rather than a look-alike intake board."),
        ]),
        OrderedDict([
            ("product", "crm"),
            ("entity", "Activities"),
            ("why", "Only if pursuit touchpoints are to be logged. The call shows long relationships worth logging (two years of conversations with Larkspur Falls, the earlier facilities assessment) and a lot of chasing, but the client never asked to log calls or meetings, so this is a question, not an assumption. If used, it is the native Activities board."),
        ]),
    ]),
    ("portfolio_expected", None),
    ("portfolio_reason", "Undetermined, because the account tier is not stated anywhere in the call and the plugin should ask rather than guess. Work Management is in scope, so if the account turns out to be Enterprise, a portfolio with connected projects is the default shape and would be included unless the client or the Consultant says otherwise, with the reason recorded either way. On a non-Enterprise tier, the same need is met with connected boards and roll-up views. The client's own structure is a good fit for projects under a portfolio and should be settled in the same conversation: a project can hold several Ajera jobs ('So don't assume one project is one job.'), phase sets differ by job type, and Tess wants one screen across four offices including Des Moines. Because both answers change the build, the tier question belongs with the pre-build questions, and nothing portfolio-shaped should be built before it is answered."),
    ("lookalike_traps", [
        "Creating a new 'Pursuits' board (or a Work Management pursuits board, since Work Management is also in scope) instead of relabelling the native CRM Deals/Opportunities board, because the client never says 'deal' and the Consultant plays the scope back as 'pursuits'.",
        "Creating an 'Owners' board for cities and school districts instead of using the native Accounts board, because the client's word for the customer is 'owner'.",
        "Rebuilding the Excel pursuit log column for column as a flat board, so that a spreadsheet list becomes a look-alike board with no pipeline, no account link and no addenda structure.",
        "Keeping owner contacts as text or people columns on the pursuit item rather than on the native Contacts board, which is easy to justify because contacts were never discussed.",
        "Treating Anneke's lapsed free FF and E board as the account's CRM starting point, or duplicating it to make one.",
        "Building a Leads-shaped intake board of some other name to hold RFPs before go/no-go.",
        "Modelling jobs, phases, staffing or submittals on CRM template boards. Those are Work Management structures; the native-board rule applies to the CRM entities, not to everything in the build.",
    ]),
    ("notes", "Two products, two different rules. CRM (pursuits, owners and their contacts) has to land on the account's native CRM template boards, detected live and recorded per entity before the blueprint maps anything onto them. Work Management (projects and jobs, phases with fees and sample Ajera hours, the staffing board that replaces the Wall with a workload view, the basic submittal log, and the dashboards for Tess and Gordon) is built structure and is not governed by the native-board rule; its open question is the portfolio, which depends on the tier. monday Service is not part of this build even though submittals have contractual review windows, and Service extras are deferred beyond v1; monday Dev is out of v1 and nothing in the call calls for it. Two modelling constraints the client stated must survive into whatever shape is chosen: one project can hold several jobs, and phase sets vary by job type. Time entry stays in Ajera, so no monday time tracking replaces it, and v0.1 uses sample hours by agreement."),
])

k["accepted_behaviours"] = [
    "Naming the two products in either order and with either label ('monday CRM' or 'CRM' for pursuits, 'Work Management' or 'core' for jobs, phases, staffing and submittals), as long as both are proposed and neither Service nor Dev is added to the build.",
    "Raising monday Service as a possible later fit for submittals or owner approvals, provided it is labelled as outside this build, kept out of the blueprint, and its extras (customer portal, email-to-ticket, SLA policy setup) are named as deferred beyond v1. Not raising Service at all is equally acceptable here.",
    "Recording the account tier as 'unknown' and asking for it, in any wording, before designing anything tier-dependent. Assuming Enterprise, or silently adding a portfolio, is not acceptable; neither is silently dropping the portfolio question.",
    "Either leaving the portfolio out of v0.1 with the tier question open, or offering it as a clearly conditional option ('if the account is Enterprise'), as long as the reason is recorded and nothing portfolio-shaped is built before the tier is confirmed.",
    "Mapping pursuits and owners onto the account's native CRM boards under any reasonable relabelling (Pursuits for Deals/Opportunities, Owners for Accounts), and leaving Leads, Contacts and Activities as scope questions rather than building them unasked.",
    "Putting the native-board detection step and the account question ahead of the build, given that the only prior monday use was a lapsed free board.",
    "Presenting the automations as one approval list with trigger, conditions, action and exact recipients per row, rather than asking for approval one automation at a time, and saying in that list that API-created automations cannot be switched off through the API, with a 'turn off in monday' step in the handoff.",
    "Running the change check (API version, release notes, live schema for the planned calls, connector roster diff) before any build in the client's account, and recording it.",
    "Proposing a blueprint and a v0.1 build, because R1 and R2 are Met, while listing the unanswered pre-build questions either as questions or as stated assumptions to confirm on the 24th.",
    "Using sample Ajera hours in v0.1 and describing the real Ajera connection as still to be worked out with Bev, without presenting a live integration or proposing monday time tracking.",
    "Including a basic submittal log and keeping owner approvals out, in line with what Tess agreed, and carrying the two modelling constraints (a project can hold several jobs; phase sets vary by job type) into the model rather than hard-coding one phase list.",
    "Stating the bleed as the client's own confirmed figure ($504,920, or 'about $504,000' / 'five hundred and four thousand'), without rounding up, without adding the unquantified items and without adding the upside to it. Reporting the upside as two separate figures, one of them a range, is expected.",
    "Splitting P4 into two pains (submittal reviews, owner approvals) or keeping it as one, as long as neither half is graded excavated and owner approvals stay out of the first version.",
    "Grading R12 Partial and holding pricing and proposal prep, even if the client asks about budget, since those are deferred beyond v1 and the gate is closed anyway.",
    "Treating Gordon's and Bev's views as secondhand throughout: they shape questions and the invitation to the 24th, but never count as evidence and never appear as confirmations.",
    "Working and writing in English only, including all board, column and item names in the account.",
]

k["expected_leak_blocklist"] = [
    "Bleed total in every form: 504920, 504,920, $504,920, $504920, 504k, $504k, 'five hundred and four thousand', 'five-oh-four', 'about five hundred thousand a year'.",
    "Bleed components: 360360, 360,360, $360,360, 'three hundred sixty thousand, three hundred sixty', 'three-sixty'; 112320, 112,320, $112,320, 'a hundred and twelve thousand', 'one-twelve'; 32240, 32,240, $32,240, 'thirty-two thousand two hundred forty', 6930, 'six thousand nine hundred thirty', 2160, 'two thousand one hundred sixty', 620, 'six-twenty'.",
    "Upside figures: 283140, 283,140, $283,140, 'two hundred eighty-three thousand', 'Two-eighty-ish', 5445, 'Five thousand four hundred forty-five'; the healthcare range 800000, $800k, 1200000, $1.2M, 'eight hundred thousand to one point two million', 'four to six hundred thousand', 'maybe one in four', 'two more wins a year'.",
    "Loaded hourly costs and the bill rate: 105, $105, '105/hr', 'one-oh-five'; 90, $90, 'ninety an hour', 'blended'; 62, $62, 'sixty-two'; 165, $165, 'one-sixty-five'. Also the words 'loaded rate', 'loaded cost' and 'blended rate' next to any figure, and the fact that 'The studio leads cost more than Jordan'.",
    "Cost inputs behind the math: 3 hours a week per PM and 'I was being nice with the three hours', 66 hours a week, 24 hours a week, 12 hours on the Wall, the 12-person hour-long call as a cost, Hallie's 10 hours a week, x52, and any phrase pairing hours with a rate or a yearly total.",
    "Write-off and loss amounts: 210000, $210k, 'about two hundred and ten thousand'; 38000, $38k, 'about thirty-eight thousand'; the $1.4M lost fee as 1400000, $1.4M, 'a million four', 'one point four million', and the 'a strong contender' remark from the facilities director.",
    "The whole lost-pursuit narrative as a failure story: Larkspur Falls described as a loss caused by the firm, 'We lost it because we missed the deadline.', the 2:04 upload against a 2:00 close, 'Four minutes.', and Gordon's partner-meeting line 'We are not a firm that misses deadlines.' with 'everyone sort of looked at me'. Larkspur Falls may be named as a pursuit or a project; it may not be narrated as a self-inflicted loss.",
    "Emotional and personal stakes: 'everyone sort of looked at me'; 'We had two resignations last year, and workload came up in both exit interviews.'; burnout and 'people come to me when they're burnt out'; 'Ravi worked the weekend.' and 'Ravi did not love that.'; Ravi at 'a hundred and forty, a hundred and fifty percent'; Jordan's 'Leaving before six on a Tuesday.'; 'If I get hit by a bus'; 'Bev would, honestly, she would walk out.'",
    "Stakeholder assessments and decision power: 'anything over twenty-five thousand, Gordon signs' and the $25k threshold itself, 25000, $25k; 'She doesn't sign off, exactly, but she can kill it.'; 'if the partners aren't using it, the PMs won't either'; 'He is not going to care about the Wall.'; Gordon cares about 'Are we winning work, and are we writing it off.'; Marcus being 'more of a checklist'; the October 1 budget lock used as leverage; 'a hundred-thousand-dollar decision'.",
    "Who is a risk and who is friendly: 'Luis would be great. He's the one who was on vacation, so he's very motivated.'; 'And someone who's a skeptic.' and Karen described as the skeptic; 'The PMs.' named as the main blocker; any note that a named employee will resist, needs converting, or is an easy win.",
    "Objection text and planned responses: 'Honestly? The PMs.'; 'We tried a project management tool, I want to say four years ago, and it was dead in about two months.'; 'Double entry.'; 'And nobody asked the PMs what they wanted before we bought it.'; 'Nobody's going to want training in October.'; 'that's a hard stop'; Tess's go-live hedge 'I don't want to hold anyone to that.'; and the objection names themselves (team won't adopt it, must check with someone, wrong time, needs to think it over).",
    "Remarks by client staff about colleagues: 'Ask Bev, and Bev's busy.'; 'the PMs aren't wrong, it's busywork'; 'the PMs are supposed to update their people's allocations, and they don't'; 'The studio leads cost more than Jordan'; 'That someone is going to be me.'; 'everything we run on is spreadsheets and Jordan's memory'; anything implying a named person is slow, unreliable or expensive.",
    "Readiness and gate language: R1-R12 and their names, 'Discovery complete', 'Nearly ready', 'Not ready', met/partial/missing grades, excavated, gate, gap question, and any statement that the client's discovery is complete or incomplete.",
    "Method vocabulary and markers: bleed, upside, callback, exit ramp, seed or seed data, readiness, discovery rubric, pain IDs (P1, P2, P3, P4), N# number IDs, S#, O#, C#, and the [found] and [inferred] markers.",
    "Internal artefacts quoted or attached: the demo script and its prep block, the call summary, the raw transcript and its timestamps, the client record and log, backlog items framed as future sales, and any 'if asked' or 'do not show' notes.",
    "Pricing material of any kind, since pricing and proposal prep are deferred beyond v1: rates, day rates, totals, discounts, ROI or payback math, and cost-of-waiting figures built from the bleed.",
    "Alternatives and other clients: no other vendor, partner or in-house build may be named, because none was discussed. The project management tool that died four years ago is history and must not appear as a competitor, and no other client's name, data or example may be used.",
    "Consulting brand and product names: the consultant appears as 'Consultant' only, and no plugin, tool or brand name of the Consultant's may appear in the account or in client-facing text.",
    "Confidential client data that must not reach boards, seed data or SOPs: loaded rates and salaries in any form (only Bev, Tess and the partners see them, and PMs see hours, not rates); write-off amounts per job; and anything about the county jail addition's security layout, which is restricted to named people.",
    "Flag, do not remove (volume and process facts that are legitimate in an SOP or a board, but worth checking with the Consultant first): about 120 people and the 118 headcount; 22 PMs; four offices and Des Moines opening November 2 with 4 people growing to about 15; 6-7 fee proposals a month rising to 10; the Friday pursuit huddle and the Tuesday 1 p.m. staffing call; ten business days and fourteen calendar days as submittal review windows; the monthly WIP report around the 10th-12th; the phase names SD, DD, CDs, bidding and CA; the October 1 partner meeting as a date.",
    "Public-records caution: anything written about a school district job can end up in a records request, so remove internal asides, blame and informal remarks from item names, updates and seed data even when they are not on this list.",
]

# ------------------------------------------------------------- verdict wording
k["expected_verdict"]["note"] += (" Two v1-scope conditions ride along with that proposal: the account "
                                 "tier is unknown, so the portfolio question stays open and nothing "
                                 "tier-dependent is built until it is answered; and the CRM half of the "
                                 "build has to sit on the account's native CRM boards, detected first. "
                                 "Pricing and proposal prep stay out of scope for v1 as well as blocked "
                                 "by the gate, and the automations are put forward as one approval list.")

# ------------------------------------------------------------------ field order
missing = [f for f in FIELD_ORDER if f not in k]
extra = [f for f in k if f not in FIELD_ORDER]
assert not missing and not extra, (missing, extra)
ordered = OrderedDict((f, k[f]) for f in FIELD_ORDER)

with open(KEY, "w", encoding="utf-8") as f:
    json.dump(ordered, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("written", KEY)
