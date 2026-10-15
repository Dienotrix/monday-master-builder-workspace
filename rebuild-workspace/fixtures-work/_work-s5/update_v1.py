#!/usr/bin/env python3
"""Add the four new fields to the s5 answer key and apply the v1 scope.

Rebuilds the key in the required field order, rewrites objection types to the
method spec's names, appends v1-scope traps, and writes the file back.
"""
import json

KEY = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s5-intro-thin/answer-key.json"

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]

k = json.load(open(KEY, encoding="utf-8"))

# --- expected_monday_products: v1 scope stated explicitly -------------------
k["expected_monday_products"] = [
    {
        "kind": "core",
        "why": ("Tentative only, and inside v1 scope. If monday fits at all, Work Management could carry "
                "event planning, volunteer committee tracking and one shared view for the executive director. "
                "Nothing is confirmed: no pain is excavated, the account tier and any existing monday account "
                "are unknown, and a dedicated association management system or a better spreadsheet may fit "
                "better. Name it as a possibility, never a recommendation, and do not attach a portfolio "
                "(see expected_structures)."),
    },
    {
        "kind": "crm",
        "why": ("Possible but unconfirmed, and inside v1 scope. Member renewals and lapsed-member follow-up "
                "could run as a pipeline, but the existing membership database ('the portal') may stay the "
                "system of record and an association management system is also in play. Raise it as a "
                "question; do not assume it. If CRM is ever confirmed, it must be built on the account's "
                "native CRM boards (Leads, Contacts, Accounts, Deals/Opportunities, Activities), never on "
                "look-alike member or renewal boards."),
    },
]

# --- objections: types standardized to the spec's objection map (5.2) -------
OBJ = [
    ("and honestly i don't want to waste your time, i'm not even sure we're the kind of place that needs a whole system",
     "Outside the map: doubt that they need a whole system"),
    ("well we're a nonprofit so budget's always a thing", "Price feels high"),
    ("one of our board members apparently uses some association software at the other group he's on",
     "Talking to other partners"),
    ("honestly that's above my pay grade", "Must check with someone"),
    ("no rush really", "Wrong time, next quarter"),
    ("do you have like a demo or a price sheet or something i could send denise though? she's going to ask",
     "Just send a proposal or pricing"),
    ("somebody set something up and then nobody used it", "Team won't adopt it"),
    ("is monday like a project management thing? i thought it was for marketing agencies",
     "Outside the map: monday seen as a marketing-agency tool"),
]
old_quotes = [o["quote"] for o in k["objections"]]
assert old_quotes == [q for q, _ in OBJ], old_quotes
k["objections"] = [{"quote": q, "type": t} for q, t in OBJ]

# --- traps: v1 scope, plus the objection context the type field no longer holds
k["traps"] += [
    ("Do not propose a portfolio with connected projects. The Enterprise-plus-Work-Management default cannot "
     "apply here: the account tier is unknown, no monday account is confirmed, and no build is proposed."),
    ("If CRM is later confirmed for members and renewals, it must reuse the account's native CRM boards "
     "(Leads, Contacts, Accounts, Deals/Opportunities, Activities). A 'Members' or 'Renewals' board built "
     "from scratch would be a look-alike. At this stage that is a question, not a plan."),
    ("Nothing in the call indicates Service, and Dev is outside v1. The website registration form and the "
     "committee email chains are not an email-to-ticket or ticketing requirement, and the Service extras "
     "(customer portal, email-to-ticket, SLA policy setup) are deferred beyond v1 in any case."),
    ("No automations list arises. Automations are approved as one list against a blueprint, and there is no "
     "blueprint, so proposing automations from this call would be inventing scope."),
    ("All eight objections are anticipated signals, not objections raised against a proposal: nothing was "
     "pitched and no price was named. Record each with status anticipated, its signal quote and the skipped "
     "step (price to R4, check with someone to R7, wrong time to R3 and R8, send a proposal or pricing to "
     "R12, adoption to the abandoned committee tool, other partners to R6 buying criteria)."),
]

# --- one more pre-build question, for the account itself --------------------
k["expected_questions_before_building"].append(
    "(Account) If this goes ahead, which monday account, plan tier and products would we be working in, who "
    "is the admin, and how many staff and volunteer chairs would need access?"
)

# --- expected_verdict note: v1 scope ---------------------------------------
k["expected_verdict"]["note"] += (
    " v1 scope: Work Management and CRM are both in v1, but the fit itself is unconfirmed, so the expected "
    "output names possibilities and questions rather than a blueprint. No portfolio (tier unknown, no build), "
    "no native-board mapping yet (no CRM commitment and no bound account), no automations list (that is "
    "approved as one list against a blueprint) and no pricing or proposal prep. English only."
)

# --- new field 1: account_context ------------------------------------------
k["account_context"] = {
    "tier": "unknown",
    "products_enabled": [
        "unknown - no monday product, plan tier, seat count or admin was named, and it is not established "
        "that the society has a monday account at all"
    ],
    "existing_monday_setup": (
        "unknown. The conference committee set something up 'a while back' that nobody used, and Jolene does "
        "not remember whether it was Trello or monday; Wendell would know and she agreed to ask. So a dormant "
        "monday account may or may not exist, and its owner, contents and state are all unconfirmed. Everything "
        "else runs outside monday: the membership database they call 'the portal' (name inaudible), Excel "
        "trackers, a separate CE/PDH spreadsheet, Eventbrite, a website form, Google Docs, email and phone "
        "calls. No account can be bound and no preflight, native-board detection or change check can run until "
        "the account question is answered."
    ),
    "evidence_quote_or_null": (
        "the conference committee tried trello a while back i think? or it might have been monday actually. "
        "i really don't remember"
    ),
}

# --- new field 2: expected_structures --------------------------------------
k["expected_structures"] = {
    "native_boards_required": [],
    "portfolio_expected": False,
    "portfolio_reason": (
        "No build is proposed, so no portfolio. The default (Enterprise tier plus Work Management in scope "
        "gives a portfolio with connected projects) cannot even be evaluated here: the account tier is "
        "unknown, no monday account is confirmed, and Work Management is only a possibility. A nonprofit with "
        "about 15 staff is unlikely to be on Enterprise [inferred], but that has to be read from the account "
        "at preflight, never assumed from the company size. Tier and existing account are questions for the "
        "discovery call."
    ),
    "lookalike_traps": [
        "A 'Members' or 'Contacts' board built from scratch in Work Management would be a look-alike of the "
        "native CRM Contacts board, and a 'Renewals' pipeline a look-alike of native Leads or "
        "Deals/Opportunities. If CRM is ever confirmed, detect and reuse the native boards instead.",
        "Lapsed-member follow-up and the bookkeeper's payment checks would be look-alikes of the native CRM "
        "Activities board if modelled as new boards of their own.",
        "'the board', 'board retreat' and 'board members' mean the society's board of directors. No monday "
        "board may be created from those mentions.",
        "The possible dormant Trello or monday setup must be identified before anything is created, so a new "
        "board is not stood up beside an existing one.",
    ],
    "notes": (
        "Nothing is to be built from this call, so native_boards_required is empty and no entity is mapped "
        "yet. Conditional, for the discovery call onwards: if CRM is confirmed for membership, members map to "
        "native Contacts, member firms to native Accounts, new-member intake to native Leads, renewals to "
        "native Deals/Opportunities, and renewal or lapsed follow-up to native Activities - each on the "
        "account's native CRM board, found by detection and recorded by id, never rebuilt. If Work Management "
        "is confirmed, events, committees and the annual conference are ordinary boards, and only an "
        "Enterprise tier read live at preflight would add a portfolio with connected projects. Service is not "
        "indicated and its extras are deferred beyond v1; Dev is out of v1 entirely. Open structural "
        "questions: the account, tier and products; whether 'the portal' stays the member system of record and "
        "whether it can export or connect; whether volunteer committee chairs need guest or limited access; "
        "and which member data (addresses, license numbers, CE/PDH credits) may be stored in a new tool."
    ),
}

# --- new field 3: accepted_behaviours --------------------------------------
k["accepted_behaviours"] = [
    "Naming Work Management as a possibility with CRM as an open question, or naming no product at all and "
    "asking about fit first. Both are acceptable; recommending a build is not.",
    "Saying plainly that a dedicated association management system, or a better spreadsheet and a couple of "
    "habits, may suit the society better, as the Consultant did on the call.",
    "Grading R2 or R7 Partial rather than Missing. The verdict stays Not ready because R4 is Missing, and the "
    "blueprint gate stays shut because R2 is not Met.",
    "Grading R9 Met, since she answered a direct question about blockers. It is advisory and changes no gate.",
    "Splitting renewals out as a second pain with Concrete Partial, as long as no pain is called excavated.",
    "Recording Jolene as end user rather than influencer, and leaving Wendell out of the attendee list "
    "altogether or holding his decision role as unknown.",
    "Recording the account, tier and products as unknown and asking, rather than assuming Enterprise, "
    "assuming no account exists, or inferring a tier from the staff count.",
    "Asking fewer than five gap questions, or reordering them, provided the core criteria (R2, R3, R4, R7) "
    "come first and the questions that belong to Denise are marked for her. "
    "expected_questions_before_building is the full pool in priority order, not one meeting's agenda.",
    "Leaving the month of Tuesday the 22nd unresolved, or asking the Consultant for it, rather than guessing.",
    "Declining to produce a blueprint, a build, an automations list, a portfolio plan, a native-entity map, a "
    "demo script, seed data, pricing or a proposal. None of those are reachable from this call.",
    "Producing only the light outputs: the Not ready verdict with a one-line reason, a call summary, discovery "
    "prep for the 22nd, a client recap draft that proposes the booked time, and the Consultant's own to-dos "
    "(send the invite with a short agenda).",
    "Flagging the hedged figures ('a couple thousand' members, 'fifteen-ish' staff) as unconfirmed volumes to "
    "check, rather than using them as volumes or turning them into any bleed or upside number.",
    "Carrying the abandoned committee tool as an anticipated adoption objection and a question about what "
    "happened, rather than as a stated pain.",
    "Leaving the monday change check and preflight for build time. Neither is due on an intro call, but "
    "neither may be skipped later if a build is ever approved.",
    "Working in English throughout.",
]

# --- new field 4: expected_leak_blocklist ----------------------------------
k["expected_leak_blocklist"] = [
    "No bleed or upside figures exist in this record, so there are none to block. Any money figure, hours "
    "figure or yearly cost attributed to the society would be invented, and must appear in no file at all, "
    "internal or client-facing.",
    "Method vocabulary: bleed, upside, callback, exit ramp, seed, readiness, excavated, gap question, fit "
    "risk, pain ids such as P1, criterion ids such as R2 or R4, gate and verdict wording such as Not ready, "
    "and the [found] and [inferred] markers.",
    "Objection text and the fact that objections were anticipated at all: \"well we're a nonprofit so "
    "budget's always a thing\", \"honestly that's above my pay grade\", \"i'm not even sure we're the kind of "
    "place that needs a whole system\", \"no rush really\", \"somebody set something up and then nobody used "
    "it\", \"is monday like a project management thing? i thought it was for marketing agencies\".",
    "Stakeholder assessments: \"i'm not the one who'd decide anything\", the note that the approver is "
    "unknown and may be the board, that Denise is the real decision maker to aim the next call at, and "
    "\"she might only be able to do half\".",
    "Remarks by staff about colleagues or their tools: \"sixteen if you count our part time bookkeeper i "
    "never know if she counts\", \"one of the chairs just likes to call people\", \"i don't totally trust "
    "it\", and \"each one kind of runs however their chair wants to run it\".",
    "Alternatives in play: the unnamed association management software and the suggestion that Denise may be "
    "looking at it - \"one of our board members apparently uses some association software at the other group "
    "he's on\".",
    "The internal fit judgement: that the engagement may not be a fit, that priority leans towards later, and "
    "that the society may only need a better spreadsheet. The honest-expert version may be said to the "
    "client, but the internal assessment and the words fit risk stay out of every written deliverable.",
    "Member personal data: \"addresses license numbers\" and anything from the renewal tracker. None of it "
    "may reach monday, seed data, or any client-facing file, and only a blank copy with column headers was "
    "requested.",
    "Raw transcript material: quoted lines with their timestamps and locations, the [inaudible] markers, the "
    "Speaker 3 label, and the call summary and prep sheet themselves.",
    "Volume figures to flag rather than delete, per the leak-check rule: \"a couple thousand members? don't "
    "quote me on that\" and \"fifteen-ish\". Both are hedged, so if a volume is ever needed in an SOP it must "
    "be confirmed first and shown to the Consultant, not silently reused.",
]

out = {key: k[key] for key in ORDER}
assert set(out) == set(k), (set(k) - set(out), set(out) - set(k))
with open(KEY, "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("written:", KEY, "fields:", len(out))
