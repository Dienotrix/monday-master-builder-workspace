#!/usr/bin/env python3
"""Rewrite the s4 answer key: add the four new fields, apply the v1 product scope
(Service IS in v1, dev is NOT), and standardise objection types and decision roles."""
import json
from collections import OrderedDict

KEY = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s4-discovery-software/answer-key.json"
k = json.load(open(KEY, encoding="utf-8"))

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]

# ---------------------------------------------------------------- purpose
k["purpose_of_this_fixture"] = (
    "Tests a strong discovery call at a B2B software company of about 200 people, delivered as a WebVTT "
    "auto-transcript, where the engagement falls on both sides of the v1 scope line: monday service is in v1 and "
    "covers a real part of what they need, while monday dev, the best fit for the engineering half, is not. The "
    "plugin should: (1) Propose a monday service build for the request-and-ticket work, which is the "
    "support-to-engineering escalation intake and/or IT's access requests, laptops and offboarding, and build it on "
    "the account's NATIVE Service template boards (Tickets and its native companions), never look-alike boards, and "
    "only after preflight has confirmed Service is provisioned and recorded those board ids. Service extras stay "
    "out of v1: no customer portal, no email-to-ticket channel, no SLA policy setup. (2) Name monday dev as the best "
    "fit for the engineering half (two-week sprints, three for Mobile, epics, the release train and release notes, "
    "and above all PR-to-work-item linking through GitHub, which is the heart of the SOC 2 change-management "
    "problem), say plainly that it is outside v1, and then EITHER offer a clearly labelled Work Management approach "
    "for that half, with its limits and the risk of a second migration, OR recommend waiting on that part. Either "
    "passes. Building dev structures as if supported, or presenting Work Management as the right fit for sprints and "
    "epics, fails. A single undifferentiated 'we'll do it all in Work Management' also fails: the answer has to "
    "separate the in-scope Service build from the out-of-scope engineering half. (3) Not be steered by the loose "
    "word 'projects' or the VP's 'portfolio view': these mean epics and initiatives, not a project-management need, "
    "and not a monday portfolio. The account tier is never stated, so the Enterprise portfolio default cannot fire "
    "here. (4) Not propose monday CRM: the consultant's CRM pitch was politely turned down, and the account "
    "managers' wish to see escalation status is a view on escalation data, not an Accounts board. (5) Grade the "
    "rubric as follows. Met: R2, R3, R6, R7, R8, R9, R10. Partial: R1, R4, R5, R12. Missing: R11. Per pain: P1 "
    "(escalations) is Met on all six checks, so it is excavated; P2 (SOC 2 change evidence) is Met on all checks "
    "except Workaround, which is Partial. Verdict 'Nearly ready', because R4 is Partial: the client gave hours but "
    "no cost, and the consultant's $120/hour placeholder was not confirmed. The blueprint gate is met; the "
    "pricing/proposal and v1.0 sign-off gates are not. (6) Capture the why-now (first SOC 2 audit, fieldwork in the "
    "second week of January, about four months out, required by a large prospect) and the SOC 2 signals: "
    "change-management evidence, incident records, access approvals, audit logs, SSO, a vendor security review, and "
    "no customer PII in engineering tools. (7) Treat GitHub and Slack as must-have integrations and Zendesk as "
    "staying until at least its March renewal, so the Service tickets built here are internal escalation and request "
    "records that link to the Zendesk ticket. (8) Parse WebVTT cues and see through speech-recognition errors "
    "('sock two', 'Zen desk', 'Monday's' meaning monday.com's). should_plugin_propose_a_build is true, and unlike "
    "earlier versions of this fixture it is now true without qualification on the Service side: there is a real "
    "in-scope build to propose on native Service boards, plus either a clearly labelled Work Management approach or "
    "a recommendation to wait for the engineering half."
)

# ---------------------------------------------------------------- attendees: spec decision roles
ROLES = {
    "Consultant": "not applicable",
    "Tomasz Wirth": "approver (decides on the tool: 'It's my call on the tool.'; spend over $50k a year goes to the "
                    "CFO for sign-off, and she was not on the call)",
    "Colleen Brask": "influencer and end user (owns the escalation process day to day; would be the main user of an "
                     "escalation queue)",
    "Devin Marchetti": "influencer and end user (product manager; would use the epics roll-up and the release notes)",
}
for a in k["attendees"]:
    a["decision_role"] = ROLES[a["name"]]

# ---------------------------------------------------------------- products
k["expected_monday_products"] = [
    {
        "kind": "service",
        "why": "IN v1, and the part of this engagement the plugin can actually build. Two candidate scopes. First, "
               "the support-to-engineering escalation intake: an escalation record with an owner, a status support "
               "can see, a severity, and a link back to the Zendesk ticket, so Colleen stops rebuilding her "
               "spreadsheet and account managers can see status for their accounts. Second, IT's service desk: "
               "access requests, laptops and offboarding, which arrive as Slack DMs or a Google Form today, and "
               "which SOC 2 needs an approval and a clean leaver record for. Both must be built on the account's "
               "NATIVE Service template boards (Tickets, plus native companions such as Incidents, Asset management "
               "and Employee lifecycle where those entities are in scope), never on look-alike boards, with the "
               "board ids detected and recorded in preflight first. Service extras are deferred: no customer "
               "portal, no email-to-ticket channel, no SLA policy setup. Zendesk stays as the customer helpdesk "
               "until at least the March renewal, so these tickets are internal records that link to the Zendesk "
               "ticket rather than replacing it."
    },
    {
        "kind": "software",
        "why": "Best fit for the engineering half, but OUT of v1; the plugin must say so plainly and must not build "
               "it. monday dev would replace Redmine for sprints (two weeks for most squads, three for Mobile), "
               "epics, bugs and escalation work items, and releases and release notes. Linking PRs to work items "
               "through GitHub is the heart of the SOC 2 change-management problem, and Slack is a must-have. The "
               "'portfolio view of projects' the VP wants is a roll-up of epics and sprints across squads, which is "
               "also dev. Name it as the fit, not as something being built, and do not quietly rebuild its "
               "structures under another product's name."
    },
    {
        "kind": "core",
        "why": "Acceptable only as a clearly labelled approach for the engineering half, because dev is outside v1; "
               "never as the recommended fit for sprints and epics, and never chosen because the client says "
               "'projects' or 'portfolio view'. Recommending waiting on that half instead also passes. If offered, "
               "the plugin must say what it does not replicate compared with monday dev, must not promise GitHub "
               "behaviour it has not verified, and should note the risk of a second migration later (the CFO does "
               "not want to pay for two things, and the last move off Redmine failed halfway). Plausible pieces: an "
               "epics roll-up, an audit evidence (PBC) board, a change record linking ticket to PR to release, an "
               "on-call handoff and incident log, and a releases board. No portfolio by default: the tier is never "
               "stated and the 'portfolio view' means epics (see expected_structures). monday CRM is not expected "
               "at all: the pitch was turned down, and the account-manager need is a view or dashboard on "
               "escalation data."
    },
]

# ---------------------------------------------------------------- R1 note: Service provisioning now gates the build
for r in k["rubric"]:
    if r["criterion"] == "R1 Current state mapped":
        r["note"] = (
            r["note"]
            + " Because monday service is in v1, two of those gaps now gate the buildable part: who approves an "
              "access grant today is never said, and the account's own monday setup (tier, which products are "
              "provisioned, whether Service exists at all, who administers it) is unknown, so the native Service "
              "board ids cannot be assumed and must be detected in preflight."
        )

# ---------------------------------------------------------------- vocabulary: Service is in v1 now
VOCAB = {
    "eng escalations / escalation":
        "item on the account's native Service Tickets board (monday service is in v1); the engineering work item it "
        "links to would be a dev item, which is outside v1, so in a Work Management approach that becomes a clearly "
        "labelled task",
    "the escalation tracker":
        "replaced by the native Service Tickets board and its columns, plus a saved view for support ops; not a new "
        "look-alike tracker board",
    "access requests / access reviews":
        "ticket on the account's native Service Tickets board (IT service desk install) with an approval status and "
        "an audit trail; quarterly access reviews as recurring items. monday service is in v1, so this is buildable",
    "service desk (IT)":
        "monday service on the account's native Tickets board, with native companions where the entity is in scope "
        "(Incidents, Asset management for laptops, Employee lifecycle for offboarding); the customer portal, "
        "email-to-ticket and SLA policies are deferred beyond v1",
    "incident / postmortem":
        "either the native Service Incidents companion, if incidents live in Service, or a clearly labelled Work "
        "Management item on the engineering side; decide which and say so, rather than creating a look-alike "
        "Incidents board",
    "tickets":
        "linked Zendesk ticket ID or link column on the Service ticket; Zendesk stays the customer helpdesk, so a "
        "monday Service ticket here is the internal escalation or request record, not a copy of the customer ticket",
}
for v in k["vocabulary"]:
    if v["their_term"] in VOCAB:
        v["likely_monday_object"] = VOCAB[v["their_term"]]

# ---------------------------------------------------------------- objections: spec vocabulary
k["objections"] = [
    {
        "quote": "Part of me wonders if switching tools right before an audit is insane.",
        "type": "Wrong time, next quarter (raised by the PM as the risk of switching mid-audit, and answered on the "
                "call by the VP: 'Redmine is the finding'; prevention is R3 and R8, both Met)"
    },
    {
        "quote": "If engineers hate it, if it feels like more work than Redmine, they'll revolt, and I'm back on Redmine by March with egg on my face.",
        "type": "Team won't adopt it (raised as the main blocker, with scar tissue from a migration that failed "
                "halfway two years ago; plan an end-user session and the Dispatch pilot)"
    },
    {
        "quote": "She'll ask what happened last time.",
        "type": "Must check with someone (the CFO signs above $50k a year, was not on the call, and will ask about "
                "the failed migration; ask what she will care about and offer to join that conversation)"
    },
    {
        "quote": "I'm not going to put a dollar figure on it on this call.",
        "type": "Price feels high (anticipated, not raised: the cost-discovery step was deflected to the CFO, which "
                "is the spec's R4-Missing signal; R4 stays Partial and pricing prep is held)"
    },
    {
        "quote": "Which, with this timeline, yeah, I'm a little worried about.",
        "type": "Wrong time, next quarter (anticipated: a four-to-six-week vendor security review against an "
                "end-of-November target)"
    },
    {
        "quote": "I'm not ripping out Zendesk four months before an audit.",
        "type": "Wrong time, next quarter (helpdesk replacement only: Zendesk stays at least until the March "
                "renewal. It does not block the in-scope Service build, which links to Zendesk instead of "
                "replacing it)"
    },
    {
        "quote": "Sales has their CRM, it's a whole different budget, a whole different VP, and I would like to keep my friends in sales. Let's keep this to engineering and support.",
        "type": "Must check with someone (not this buyer's decision: sales has its own CRM, budget and VP. Treat it "
                "as a scope refusal after an unrequested pitch, not as interest to follow up)"
    },
]

# ---------------------------------------------------------------- traps
k["traps"] = [
    "The engagement straddles the v1 scope line, and the plugin has to split it. monday service IS in v1: the "
    "escalation intake and IT's access requests, laptops and offboarding can be blueprinted, built and audited, at "
    "the same depth as CRM. monday dev is NOT: sprints, epics, the release train and PR-to-work-item linking are the "
    "best fit for the engineering half and cannot be built. Passing: propose the Service build, name dev as the fit "
    "for the rest, and either offer a clearly labelled Work Management approach for it or recommend waiting. "
    "Failing: building dev structures as if supported, presenting Work Management as the right fit for sprints and "
    "epics, or answering with one undifferentiated build that hides which half is out of scope.",
    "Service must be built on the account's NATIVE Service template boards. A hand-built 'Escalations', 'Support "
    "Tickets', 'IT Requests' or 'Access Requests' board is a look-alike and fails even if its columns are right. "
    "The native boards are found by detection (template lineage walked as a chain, template view ids, or the "
    "reserved Tickets column fingerprint), and their ids are recorded per entity in the client record before any "
    "write. Renaming a native board to the client's vocabulary is fine, because board names prove nothing; "
    "recreating the entity beside it is not.",
    "Service extras are deferred beyond v1 even though this call invites all three: no customer portal (the account "
    "managers get a view or dashboard, not a portal), no email-to-ticket channel (the Zendesk hop is a link plus an "
    "automation, not an inbound mail channel), and no SLA policy setup (the Sev 1-4 scale and 'when we last told "
    "the customer something' both tempt it). Naming them as later work is fine; building them fails.",
    "Whether the account even has Service provisioned is unknown. The only monday use described is Marketing's "
    "campaign boards plus a webinar calendar, with plan, seats and admin unknown, and engineering has never touched "
    "it. If Service is not enabled there is no native Tickets board to build on: ask, and do not hand-build a "
    "look-alike in its place.",
    "The Enterprise portfolio default does not fire here. The tier is never stated ('I have no idea what plan "
    "they're on or how many seats'), and the transcript says otherwise anyway: the VP's 'portfolio view' of 'all our "
    "projects' means a roll-up of epics across squads. Record the reason for not proposing one. If preflight later "
    "finds an Enterprise account and a Work Management approach is agreed for the engineering half, the default then "
    "applies and should be built with monday's portfolio and project tools, not plain boards.",
    "'Projects' is used loosely. Redmine 'projects' are containers, roughly one per product area (eleven, including "
    "Support Escalations and Misc), and 'the Dispatch project' in Devin's commitment is one of them. The VP's "
    "'portfolio view' of 'all our projects' means epics and initiatives across squads (he says 'those are epics "
    "technically, I guess'), with the non-code 'SOC two project' mixed in. The word does not signal a "
    "project-management need, a monday portfolio, or a reason to choose Work Management; map it to epics and a "
    "roll-up view, and ask whether the non-code audit work belongs in the same view.",
    "The consultant's CRM pitch was politely turned down ('Please don't open that can.'). Do not add monday CRM, and "
    "do not treat the Granite deal as a pipeline need. The account managers' wish to see escalation status calls for "
    "a view or dashboard on escalation data, not an Accounts, Customers or Deals board, and certainly not a "
    "hand-built look-alike of one.",
    "The consultant's $120/hour placeholder is not client evidence. Tomasz answered 'Mm. I don't know. Maybe?' and "
    "deferred to the CFO, so R4 stays Partial. His earlier 'that's about right' confirms only the hours framing "
    "(about one engineer per sprint). Do not present a computed bleed total as confirmed.",
    "Engineering hours are a loose range: 'forty-ish' per sprint and 'more like fifty' on a bad sprint; Tomasz chose "
    "forty. Keep the range and do not round up.",
    "The consultant promised 'a first look' for the next call. That promise does not override the v1 scope line. The "
    "Service part can be shown as a real build; anything covering sprints, epics, releases or PR linking is either a "
    "clearly labelled approximation framed as a direction check, or left out with the reason given.",
    "Zendesk stays until at least the March renewal ('I'd look at it then. Maybe.'). Do not plan a helpdesk "
    "migration, and do not read Service being in v1 as permission to replace Zendesk. The escalation flow still has "
    "to connect to it, and the connection must not be described as email-to-ticket, which is deferred.",
    "Sprint lengths differ: two weeks for most squads, three weeks for Mobile.",
    "Five squads, but only four are named (Dispatch, Billing, Mobile, Platform). Ask for the fifth; do not invent it.",
    "The Redmine migration scope is disputed. Tomasz wants only open issues and epics; Devin wants at least the last "
    "year of history for the audit ('We can argue about that later.').",
    "monday is already in use: Marketing (and Customer Education) use boards Jess built, with unknown plan and "
    "seats. Ask whether to build in that account or a separate one, and who administers it.",
    "Speech-recognition errors: 'sock two' is SOC 2 and 'Zen desk' is Zendesk. 'Monday's security and compliance "
    "documentation' means monday.com's, while 'By Monday' in Tomasz's commitment is the weekday.",
    "Oren's attendance at the next call is tentative ('no promises'); do not list him as a confirmed attendee.",
    "The timeline is tight: a 4 to 6 week security review, a one-sprint pilot and a big release at the end of "
    "October, against 'off Redmine by end of November'. Flag feasibility; ask whether the review and pilot can "
    "overlap. Note that the Service build does not depend on the Redmine cutover, so it can be sequenced first.",
    "Customer PII must not appear in the build or seed data (homeowner names, phone numbers, addresses). Escalation "
    "items link to the Zendesk ticket instead of copying it: 'Link to the ticket, sure. Copy the ticket, no.'",
    "The consultant started describing a monday dev GitHub integration while the client was still describing pains, "
    "then stopped mid-sentence. No product claim was completed and nothing was agreed; it is a delivery note, not a "
    "commitment, not client interest, and not licence to treat dev as in scope.",
    "The scope agreement covers only the first demo and is hedged ('Don't hold me to that being the whole list.'). "
    "R12 is not Met: no proposal.",
    "The production deploy and approval process was never described, and neither was who approves an access grant "
    "today. Do not assume where approvals happen (GitHub review, a release sign-off, a status on a ticket); for the "
    "Service build this matters, because the approval record is the audit evidence.",
    "There are two different invoice incidents: the May 'invoice PDF thing' (the same bug fixed twice by two squads) "
    "and the June invoice CSV export change (support not told). Do not merge them.",
    "The call date is not in the transcript. 'Friday', 'by Monday', 'early next week' and 'Tuesday the twenty-second' "
    "are relative.",
]

# ---------------------------------------------------------------- questions
k["expected_questions_before_building"] = [
    "(For the consultant, before any blueprint) The request-and-ticket half is buildable now: monday service covers "
    "the escalation intake and IT's access requests, on your account's native Tickets boards. The engineering half "
    "(sprints, epics, releases, PR-to-ticket linking) is monday dev, which this version does not build. Do you want "
    "a clearly labelled Work Management approach for that half in the first look on the 22nd, or should we wait on "
    "it and show the Service part only?",
    "Does the account have Service provisioned, and where are its native Tickets boards? Which products and tier is "
    "the account on, who administers the boards Marketing uses, and should this be built in that account or a "
    "separate one?",
    "Which Service scope comes first: the support-to-engineering escalation intake, IT's access requests, laptops "
    "and offboarding, or both? If both, should they share one Tickets board with separate groups and views, or two "
    "native installs?",
    "The customer portal, email-to-ticket and SLA policies are out of this version. Is a link from the Zendesk "
    "ticket plus an automation enough for the escalation hop for now, and do you want response-time expectations "
    "recorded as a plain status rather than an SLA policy?",
    "When you say a portfolio view of all your projects, do you mean a roll-up of epics across the squads? Should "
    "non-code work like the SOC 2 evidence tracking sit in the same view?",
    "What is the fifth squad called? Does Mobile keep its three-week sprints while the others run two weeks, and "
    "which day do sprints start?",
    "How does a production change get approved and deployed today, and where should that approval be recorded so it "
    "counts as audit evidence?",
    "Who approves an access grant today, and what has to be on the record for the auditor: the approver, the date, "
    "the systems granted, and the quarterly review?",
    "Which fields does tier two need when escalating, and how should the Zendesk ticket be linked so no customer "
    "personal details are copied?",
    "Which Redmine data should come across: only open issues and epics, or the last year of history too?",
    "Which GitHub organisation and repositories, and which Slack channels and notifications, need connecting?",
    "What must an on-call handoff record contain, and where should incidents and postmortems live: on the native "
    "Service Incidents board, or with the engineering work?",
    "What should account managers see about escalations on their accounts, and do they need to change anything or "
    "only view it?",
]

# ---------------------------------------------------------------- verdict
k["expected_verdict"]["gates_met"] = [
    "Solution blueprint: R1 is Partial and R2 is Met",
    "Build: no extra method gate beyond the consultant's approval at the approval stop. Within v1 there is a real "
    "build to propose: monday service for the escalation intake and/or IT's service desk, on the account's native "
    "Tickets board and its native companions, with Service extras (portal, email-to-ticket, SLA policies) excluded. "
    "The engineering half is either a clearly labelled Work Management approach or a recommendation to wait.",
    "First demo (v0.1): nothing extra required",
]
k["expected_verdict"]["note"] = (
    "Verdict criteria: R2 Met (P1 escalations excavated), R3 Met (first SOC 2 audit, fieldwork in the second week of "
    "January, required by the Granite prospect), R7 Met (the VP decides, the CFO signs above $50k a year, a 4 to 6 "
    "week security review, then a one-squad pilot), R4 Partial. None Missing and one Partial, so 'Nearly ready', not "
    "'Discovery complete'. On scope: monday service is in v1, so the escalation intake and IT's access requests are "
    "a genuine build target, on the account's native Service boards, with Service extras deferred. monday dev is "
    "not in v1, so the engineering half (sprints, epics, releases, PR-to-work-item linking) is named as the fit and "
    "then either approximated in Work Management with clear labelling or deferred, with the reason given. Next prep "
    "should close R4 (loaded hourly cost via the CFO, then a yearly figure the client confirms) and R12 (a short "
    "scope agreed out loud), and settle the account questions the build depends on: tier, provisioned products, and "
    "the native Service board ids."
)

# ---------------------------------------------------------------- new field: account_context
k["account_context"] = {
    "tier": "unknown. The tier is never stated. The only monday use described belongs to Marketing, and the VP says "
            "plainly that he does not know the plan or the seat count, so the Enterprise-only portfolio default "
            "cannot be applied from this transcript. Preflight must establish it.",
    "products_enabled": [
        "unknown overall: nothing in the transcript names a monday product, and the plugin must detect this in "
        "preflight rather than assume it.",
        "Work Management: implied but not confirmed. Marketing has campaign boards built by their ops person, and "
        "Customer Education uses one of those boards for a webinar calendar.",
        "Service: unknown, and this is the gating unknown for the buildable part of the engagement. If Service is "
        "not provisioned there are no native Tickets boards to build the escalation intake or the IT service desk "
        "on, and the answer is to ask, not to hand-build a look-alike.",
        "CRM: unknown, and not needed. The CRM pitch was turned down.",
        "dev: unknown, and outside v1 either way.",
    ],
    "existing_monday_setup": "Marketing uses monday for campaign boards, set up by Jess, their marketing ops person. "
                             "Customer Education uses one of those boards for the webinar calendar. Engineering, "
                             "support and IT have never used it, and none of the three people on the call knows the "
                             "plan, the seat count or who administers it. There is no existing setup to audit or "
                             "extend for this engagement, so the question of whether to build in that account or a "
                             "separate one is open.",
    "evidence_quote_or_null": "I have no idea what plan they're on or how many seats.",
}

# ---------------------------------------------------------------- new field: expected_structures
k["expected_structures"] = {
    "native_boards_required": [
        {
            "product": "service",
            "entity": "Tickets (native Service template install: the base Tickets family or the customer-service "
                      "family)",
            "why": "Required if the support-to-engineering escalation intake is built. Every escalation record must "
                   "live on the account's native Tickets board, found in preflight by template lineage walked as a "
                   "chain, by a template view id, or by the reserved Tickets column fingerprint, and the board id "
                   "recorded per entity in the client record. A new 'Escalations' or 'Support Tickets' board would "
                   "be a look-alike and fails the rule. Renaming the native board to their vocabulary is fine."
        },
        {
            "product": "service",
            "entity": "Tickets (native Service IT-service-desk install)",
            "why": "Required if IT's requests are built: access requests, laptops and offboarding, which arrive as "
                   "Slack DMs or a Google Form today and which SOC 2 needs an approval and a clean leaver record "
                   "for. Use the account's native install rather than a hand-built 'Access Requests' board. If both "
                   "this and the escalation intake are in scope, state plainly whether they share one Tickets board "
                   "with separate groups and views or use two native installs, and ask."
        },
        {
            "product": "service",
            "entity": "Incidents (native IT-service-desk companion)",
            "why": "Conditional. If production incident logging and postmortems go into Service, they belong on the "
                   "native Incidents companion, not on a new 'Incidents' or 'Postmortems' board. If they stay with "
                   "the engineering work instead, say so and record the choice. Detection caveat: the native "
                   "Incidents board's column ids are all monday defaults, so a copy with broken lineage cannot be "
                   "told from an ordinary board by columns alone; it needs lineage or a template view id, and a "
                   "weak match is a question for the consultant, not a reason to build a new board."
        },
        {
            "product": "service",
            "entity": "Employee lifecycle (native IT-service-desk companion)",
            "why": "Conditional on offboarding being in scope: 'Laptops, access, offboarding, it's all DMs' and the "
                   "auditor wants a clean record when someone leaves. If offboarding is built, use this native "
                   "companion rather than a new leavers board."
        },
        {
            "product": "service",
            "entity": "Asset management (native IT-service-desk companion)",
            "why": "Conditional on laptop and asset tracking being asked for. It is part of the native IT "
                   "service-desk family, so if assets are in scope it is the board to use, but do not add it "
                   "unasked just because the family ships it."
        },
    ],
    "portfolio_expected": False,
    "portfolio_reason": "The portfolio-by-default rule applies to Enterprise accounts with Work Management in scope, "
                        "and neither condition is established here. The tier is never stated ('I have no idea what "
                        "plan they're on or how many seats'), and the transcript says otherwise in any case: the "
                        "VP's 'portfolio view' of 'all our projects' means a roll-up of epics and initiatives across "
                        "squads, which he half-concedes himself ('those are epics technically, I guess'), and that "
                        "is monday dev, outside v1. The reason is recorded either way. If preflight finds an "
                        "Enterprise account AND the consultant agrees a Work Management approach for the engineering "
                        "half, the default then applies: build it with monday's portfolio and project tools rather "
                        "than plain boards, connect the projects, check the roll-ups fill in, and record that "
                        "decision too.",
    "lookalike_traps": [
        "A hand-built 'Escalations' or 'Support Tickets' board for the escalation intake while Service is in scope. "
        "It fails even with the right columns, severity and owner: the entity belongs on the account's native "
        "Tickets board.",
        "A hand-built 'Access Requests', 'IT Requests' or 'Service Desk' board for IT's queue, instead of the native "
        "IT-service-desk Tickets install.",
        "A hand-built 'Incidents' or 'Postmortems' board sitting inside the Service setup beside a native Incidents "
        "companion.",
        "A CRM look-alike for the account-manager need: an 'Accounts', 'Customers' or 'Clients' board, or a deals or "
        "pipeline board for the Granite deal. CRM is out of scope here entirely, and the need is a view or "
        "dashboard on escalation data. If an account entity were ever required it would have to be the native CRM "
        "Accounts board.",
        "Treating a duplicate of a native Tickets board as 'not native' and building a parallel board beside it. A "
        "duplicate keeps the column fingerprint and is still the native entity; an ambiguous detection result is a "
        "question for the consultant, not licence to create another board.",
        "Naming an ordinary Work Management board 'Tickets', 'Sprints', 'Epics' or 'Releases' and presenting it as "
        "the Service or dev equivalent. The name is not the problem; presenting it as the product is, and in a Work "
        "Management approach every board is an ordinary board and must be labelled as an approximation.",
    ],
    "notes": "Service extras stay out of v1, which shapes the structures: no customer portal object, no "
             "email-to-ticket channel, and no SLA policy setup, so where the account's native Tickets board already "
             "carries SLA helper columns they are left alone and no response-time promises enter the blueprint. Do "
             "not add native companions the client never asked for (CSAT Survey, Contacts) merely because the "
             "template family includes them. Zendesk stays the customer helpdesk until at least the March renewal, "
             "so a monday Service ticket here is an internal escalation or request record that links to the Zendesk "
             "ticket, with no customer PII copied across: 'Link to the ticket, sure. Copy the ticket, no.' The "
             "engineering half carries no native-board requirement because monday dev is outside v1; if a Work "
             "Management approach is built for it, every board is an ordinary board, labelled as an approximation, "
             "with the second-migration risk stated. Preflight records the native board ids per entity in the client "
             "record before any write, and the post-build audit verifies that every Service entity in the blueprint "
             "sits on its native board.",
}

# ---------------------------------------------------------------- new field: accepted_behaviours
k["accepted_behaviours"] = [
    "Splitting the answer along the v1 scope line: a real monday service build for the escalation intake and/or "
    "IT's requests, and the engineering half named as monday dev, out of scope, then either approximated with clear "
    "labelling or deferred. Both halves have to be visible in the answer.",
    "For the engineering half, either option passes: a clearly labelled Work Management approximation with its "
    "limits, what it does not replicate compared with monday dev, and the risk of a second migration; or a "
    "recommendation to wait on that part, with the same explanation. What fails is presenting Work Management as the "
    "right fit for sprints and epics, or building dev structures as if supported.",
    "On the Service side, either sequencing passes: proposing the escalation intake now, or proposing IT's access "
    "requests and offboarding first as the safer opening build (nothing depends on the Redmine cutover and Zendesk "
    "stays) and asking about the escalation intake. What fails is a hand-built look-alike ticket board in either "
    "case.",
    "Running preflight before any write: confirming Service is provisioned, detecting the native Tickets board and "
    "any native companions, recording their ids per entity in the client record, and recording the change check. "
    "Stopping to ask when Service turns out not to be provisioned, or when detection is ambiguous, is correct "
    "behaviour rather than a failure to deliver.",
    "Asking about the account before assuming structures: tier, which products are provisioned, who administers the "
    "boards Marketing uses, and whether to build in that account or a separate one.",
    "Not proposing a portfolio here, and recording why (tier unknown; 'portfolio view' means epics). Proposing one "
    "later, after preflight finds an Enterprise account and a Work Management approach for the engineering half is "
    "agreed, also passes, provided it uses monday's portfolio and project tools and the reason is recorded.",
    "Keeping Service extras out while naming them as later work: no customer portal, no email-to-ticket channel, no "
    "SLA policy setup. Describing the Zendesk hop as a link plus an automation rather than an inbound mail channel.",
    "Not proposing monday CRM, and meeting the account-manager need with a view or dashboard on escalation data.",
    "Presenting the automations as one list for a single approval, each row naming trigger, conditions, action and "
    "exact recipients, with the note that automations created through the API cannot be switched off through the "
    "API, and a 'turn off in monday' step per automation in the handoff.",
    "Keeping the hours as a range ('forty-ish', 'more like fifty') and not presenting a computed bleed as "
    "confirmed; holding pricing and proposal prep because R4 and R12 are Partial.",
    "Using the client's vocabulary for names and labels (squads, epics, escalations, Sev 1-4, release train, "
    "hotfix, PBC list) while keeping internal method vocabulary and the cost figures out of anything client-facing.",
    "Seed data and item names that carry no customer PII, no real customer identity from the July incident, and no "
    "internal notes; escalation examples link to a ticket reference rather than copying ticket content.",
    "Flagging the timeline honestly: a 4 to 6 week security review, a one-sprint pilot and an end-of-October release "
    "against 'off Redmine by end of November', and noting that the Service build can be sequenced ahead of the "
    "Redmine cutover.",
    "All output in English, including anything the Kraków half of engineering will read; v1 is English only, so "
    "offering a translated SOP is out of scope.",
    "Treating the consultant's unfinished monday dev GitHub remark and the $120/hour placeholder as non-evidence, "
    "and treating the CRM exchange as a refusal rather than a lead.",
]

# ---------------------------------------------------------------- new field: expected_leak_blocklist
k["expected_leak_blocklist"] = [
    "The unconfirmed loaded-rate placeholder in every format: '120', '$120', 'a hundred and twenty an hour', and any "
    "yearly or per-sprint total computed from it.",
    "Cost inputs and the hours behind them: 'forty-ish hours a sprint', 'forty hours', 'more like fifty', 'an hour a "
    "day each', Colleen's hour on the tracker, 'most of a day every release', 'Three full weekends'. Volume numbers "
    "(about 1,100 tickets a month, 60 to 70 escalations, about 40 last year) are flagged for the consultant rather "
    "than removed, because they can be legitimate in an SOP.",
    "The spend threshold and budget mechanics: 'fifty thousand', '$50k', who signs above it, and the expectation "
    "that this deal will cross it ('it probably will be').",
    "Stakeholder assessments: that the CFO is the spend approver who will ask about the failed migration, that the "
    "security lead is the long pole on the timeline, that 'IT is two people and they report to me', and that Bartek "
    "'did not sign up to be the Redmine guy'.",
    "Objection text and the adoption risk, raised or anticipated: 'they'll revolt', 'egg on my face', 'shelfware', "
    "'scar tissue', 'Engineers hate clicking', 'Part of me wonders if switching tools right before an audit is "
    "insane', 'I'm not ripping out Zendesk', and any planned response to them.",
    "Emotional and personal stakes: 'I groveled a lot', 'We look stupid', 'about had a heart attack', 'whose team "
    "was the problem', 'whole job is being confused', and the readiness-assessment embarrassment in engineering.",
    "Remarks by client staff about colleagues or other teams: 'Engineering thinks everything's a Sev 3', 'Engineers "
    "hate clicking', 'God help them', the nagging line, and the sales-politics asides ('a whole different VP', "
    "'keep my friends in sales', 'Please don't open that can').",
    "Sales context that must not reach engineering tools or client-facing documents: the internal deal codename 'the "
    "Granite deal', the prospect's identity as a national facilities group, 'biggest customer by a lot', 'fifteen "
    "hundred technicians', and the fact that the deal slides without a clean report. The audit deadline itself may "
    "be stated neutrally.",
    "Customer identity and the concession from the July escalation: 'out in Denver', 'forty-some trucks', "
    "'evaluating other options', 'two months free', and the owner calling the CEO. None of it belongs in seed data "
    "either.",
    "Customer PII of any kind, which is also the client's own rule: 'homeowner names and phone numbers and "
    "addresses' must never appear in board names, item names, descriptions, updates, docs or seed data. Link to the "
    "ticket instead: 'Link to the ticket, sure. Copy the ticket, no.'",
    "Alternatives in play and what was said about them: the 'compliance automation platforms' purchase in "
    "procurement, and the move to 'another tracker' two years ago that failed halfway.",
    "Reliability judgements about their current process that read as criticism of named people: 'Sixty is generous', "
    "'the doc is, let's say, aspirational', and 'Slack is where everything happens and then dies'.",
    "Method vocabulary and internal grading: bleed, upside, callback, exit ramp, seed, readiness, excavated, pain "
    "IDs such as P1 and P2, criterion IDs such as R4 and R12, gate names, the verdict wording 'Nearly ready', and "
    "the [found] and [inferred] markers.",
    "Internal artefacts in full: the demo script and its prep block, call summaries, the raw transcript and cue "
    "locations, gap questions, and anything from the change log.",
    "The scope-limit reasoning as an internal note: phrasing such as 'outside v1' or product-roadmap language "
    "belongs in the consultant's record, while client-facing material says plainly and neutrally what is being "
    "built now and what is deferred.",
]

# ---------------------------------------------------------------- write, ordered
out = OrderedDict((f, k[f]) for f in ORDER)
extra = [f for f in k if f not in ORDER]
assert not extra, f"unexpected fields: {extra}"
with open(KEY, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("written:", KEY, "fields:", len(out))
