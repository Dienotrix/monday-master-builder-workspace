#!/usr/bin/env python3
"""Build the s8 answer key. Evidence locations are filled from the generated transcript,
so 'cue N, start, speaker' can never drift from the actual cues."""
import json
import re
import sys
from collections import OrderedDict

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo/"
t = open(BASE + "transcript.txt", encoding="utf-8").read()

# ---------------------------------------------------------------- cue index
CUES = {}
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        m = re.match(r"^<v ([^>]+)>(.*)$", " ".join(lines[2:]))
        CUES[int(lines[0])] = (lines[1].split("-->")[0].strip(), m.group(1), m.group(2))

PROBLEMS = []


def E(quote):
    """Evidence dict with the location filled in from the transcript."""
    hits = [n for n, (s, sp, txt) in CUES.items() if quote in txt]
    if not hits:
        PROBLEMS.append(f"NOT IN ANY CUE: {quote!r}")
        return {"quote": quote, "location": "UNRESOLVED"}
    if len(hits) > 1:
        PROBLEMS.append(f"AMBIGUOUS ({len(hits)} cues {hits}): {quote!r}")
    s, sp, _ = CUES[hits[0]]
    return {"quote": quote, "location": f"cue {hits[0]}, {s}, {sp}"}


def P(quote, theme):
    e = E(quote)
    return {"quote": quote, "location": e["location"], "theme": theme}


def R(criterion, status, quotes, note):
    return {"criterion": criterion, "status": status,
            "evidence": [E(q) for q in quotes], "note": note}


k = OrderedDict()
k["scenario_id"] = "s8-discovery-enterprise-pmo"
k["call_type"] = "discovery"

k["purpose_of_this_fixture"] = (
    "Tests a strong, hour-long discovery call with the PMO of a 400-person healthcare construction and renovation "
    "firm, delivered as a WebVTT transcript with '<v Speaker Name>' voice tags, where the account tier is stated "
    "plainly and therefore the Enterprise portfolio default fires. The plugin should: (1) Read 'We're on the "
    "enterprise plan, work management, about two hundred and twenty seats.' as the trigger for amendment A6 and "
    "include a portfolio with connected projects BY DEFAULT, recording the reason. This is the first fixture in the "
    "set where that default actually applies, and the client's own stated need agrees with it: a portfolio view "
    "across roughly forty active projects showing health, budget burn and the next owner milestone. It must be built "
    "with monday's portfolio and project tools, not plain boards dressed up as projects, with the projects connected "
    "and the roll-ups checked after creation. (2) Not quietly decide the portfolio's shape. The client uses "
    "'portfolio' for the whole book of active work and 'program' for one health system's work under a master "
    "agreement ('A program is one health system's work under a master agreement.'), a job sits in both at once, and "
    "Cumberland's vice president of facilities wants the program as one thing. Whether that is one portfolio with a "
    "program grouping, or a portfolio per program, is a question for the consultant and the client, not an "
    "assumption. (3) Treat the account as an existing Enterprise account with a real setup to audit and extend, not "
    "a greenfield: preconstruction has a bid board whose builder left the company, safety has an incident board in "
    "daily use, the IT director owns the contract and a preconstruction power user builds things. Ask where the "
    "build goes and who administers it before writing anything. (4) Recognise that the 'we already have monday and "
    "nobody uses it' objection is a setup problem, not a tool problem, and say so from the evidence in the call "
    "(one board with a departed owner, one board with a present owner and daily use). (5) Grade the rubric: Met for "
    "R1-R10 and R12, Missing for R11 (no demo has happened), verdict 'Discovery complete'. This is the first fixture "
    "where R4, R7 and R12 are all Met, so the method's pricing-or-proposal gate OPENS. Pricing and proposal prep are "
    "deferred beyond v1, so the correct behaviour is to say plainly that the gate is open and that this version does "
    "not produce pricing or a proposal, and hand the client's explicit request ('Send me a scope and a number I can "
    "put against my line before the budget lock in November.') to the consultant as a to-do with its date. Silently "
    "drafting a price or a proposal fails; silently ignoring the request also fails. (6) Keep the bleed at the "
    "client's own confirmed $432,080 a year, with the collision component taken at the low end and shown as a range, "
    "and leave the $480,000 Cumberland West overrun out of the total as unquantified, because the client explicitly "
    "would not say how much of it was avoidable. The upside is a $150,000 deferred PM hire plus about $280,000 of "
    "fee from one more staffable job a year, with the deferred hire flagged as coming out of the same freed hours as "
    "the bleed's reporting time, so it is not added on top. (7) Grade pains with real gaps: P1 (no trustworthy "
    "portfolio view) and P2 (resource collisions) are excavated on all six checks; P3 (budget burn seen six weeks "
    "late) has Cost inputs and Trajectory Partial; P4 (every PM starts a job differently) has Concrete Partial and "
    "Cost inputs and Trajectory Missing; P5 (warranty calls after turnover) has Concrete and Workaround Partial and "
    "Reach, Cost inputs and Trajectory Missing, and the client parks it herself ('It's not this year's mess.'). (8) "
    "Keep CRM and Service out of this build while handling both correctly: the warranty inbox is ticket-shaped and "
    "Service is in v1, but it is out of the agreed scope, so it is a question and a backlog seed, never a hand-built "
    "'Warranty Requests' board; the health systems and their pursuits are CRM-shaped and partly live on "
    "preconstruction's existing board, so they are also a question. If either is ever built, it goes on the "
    "account's native template boards, and Service extras (customer portal, email-to-ticket, SLA policy setup) stay "
    "deferred. monday dev is out of v1 and nothing here calls for it. (9) Honour the client's own words and their "
    "homonyms: 'the board' is the executive committee, 'health' is a red-amber-green project status rather than "
    "anything clinical, 'the grid' is the resource workbook, 'the deck' is the monthly report, 'the owner' is the "
    "health system, and 'program' is not a monday portfolio by definition. (10) Respect the compliance line: no "
    "patient information and no photographs containing patients or whiteboards, field staff immunization and "
    "background records stay with HR, ICRA permits expire and must be tracked with their dates, loaded rates and "
    "cross-job margin are restricted, and changes to a health status or a milestone date need an audit trail with "
    "the previous date retained. (11) Design for the field as described: superintendents on phones with one bar, two "
    "things a week, and no eight-field form; field crew scheduling is explicitly excluded at the client's request. "
    "(12) Read WebVTT voice tags, treat the two cues tagged '<v Speaker 2>' as speaker unclear so they corroborate "
    "but never carry a Met on their own, and not be confused by one duplicated cue or one overlapping crosstalk "
    "pair. Automations are put forward as a single approval list. should_plugin_propose_a_build is true."
)

k["transcript_format"] = (
    "WebVTT from a video meeting, using voice tags: a 'WEBVTT' header, then numbered cues, a timing line "
    "'HH:MM:SS.mmm --> HH:MM:SS.mmm', and cue text in the form '<v Speaker Name>text'. There are 417 cues running "
    "from 00:00:02.714 to 00:59:44.000, about 6,400 spoken words, for a call of about 60 minutes. Client talk share "
    "is about 68 percent (Marisol Bettencourt 48 percent, Warren Tibbetts 12 percent, Ines Kovalenko 8 percent, the "
    "unlabelled 'Speaker 2' cues under 1 percent); the Consultant has about 32 percent and his longest unbroken "
    "stretch is 110 words over 54 seconds from 00:54:10.284, which is under the spec's 90-second threshold, so "
    "delivery notes should report no long stretch. Long turns are split across consecutive cues by the same speaker; "
    "cue boundaries fall at sentence ends except for two deliberate mid-sentence splits. Three transcript artefacts "
    "are present on purpose: cues 147 and 149 are tagged '<v Speaker 2>' because the tagging failed on two of Ines "
    "Kovalenko's lines (context makes the speaker obvious, but the method requires them to be marked speaker "
    "unclear); cue 184 is a duplicate of cue 183, the same Consultant line emitted twice; and cue 90 starts before "
    "cue 89 ends, which is genuine crosstalk. Every location in this key gives the cue number, cue start time and "
    "speaker, for example 'cue 268, 00:37:30.906, Marisol Bettencourt'. ASCII only. The call date is not in the "
    "transcript; the weekday-date pairs mentioned (Wednesday the twenty-third, the second Tuesday, January "
    "fifteenth) fit a call in September 2026."
)

k["company"] = OrderedDict([
    ("name", "Bellamy Ridge Construction Group"),
    ("industry",
     "Healthcare facilities construction and renovation, exclusively: hospitals, medical office buildings, "
     "outpatient clinics and imaging suites, with a large share of renovation inside occupied buildings. Their "
     "differentiator is working in live clinical space ('Not everybody can do a cath lab renovation on the second "
     "floor while the first floor is doing surgery.'). Work arrives through health-system clients, increasingly "
     "under multi-year master agreements."),
    ("size",
     "About 400 people: roughly 95 salaried office staff and about 300 field staff. Fourteen project managers report "
     "up through the PMO, plus one PMO analyst (Bridget Ahn, on parental leave from November) and one resource "
     "manager. Only four superintendents are qualified for occupied-building work. Thirty-eight to forty active "
     "projects ('Thirty-eight. Forty, depending on how you count the equipment jobs.'), heading for about fifty-five "
     "next year."),
    ("locations", "Knoxville, Tennessee (headquarters), Chattanooga, and Huntsville, Alabama"),
    ("current_tools", [
        "Procore (drawings, RFIs, submittals, daily reports; the system of record for the job itself and explicitly "
        "staying: 'Procore is the job.')",
        "Sage 300 (accounting and job cost; the book of record for anything with a dollar sign, actuals land around "
        "the tenth to twelfth of the following month; controlled by Roland Pace, the controller)",
        "Excel: the resource workbook they call 'the grid' (a tab per office), the 60-something-line project startup "
        "checklist, fourteen different PM cost-to-complete forecasts, and Cumberland's reporting template",
        "Microsoft 365, Teams (how staffing requests reach the resource manager) and the Microsoft tenant used for "
        "single sign-on",
        "The monthly executive deck: about 40 pages plus a 40-row summary page, assembled by hand by the PMO analyst",
        "monday.com, already in use: Enterprise plan, Work Management, about 220 seats. A preconstruction bid board "
        "built by Dwayne Ferris, who left in February, and a safety incident board owned by Lonnie Hatch that is "
        "used daily. The IT director owns the contract; Kyle in preconstruction is the only person who builds in it",
        "Smartsheet (abandoned pilot in 2023, died of double entry)",
        "Power BI (proposed by the IT director's team as a way to build the reporting themselves; not built)",
        "A shared warranty inbox for post-turnover calls",
    ]),
])

k["attendees"] = [
    OrderedDict([("name", "Consultant"),
                 ("role", "monday.com consultant running the discovery call"),
                 ("side", "consultant"), ("decision_role", "not applicable")]),
    OrderedDict([("name", "Marisol Bettencourt"),
                 ("role", "Director of the Project Management Office; owns project controls, scheduling standards, "
                          "leadership reporting and the process. Fourteen PMs and the resource manager sit under "
                          "her; she reports to Curt Mabry, VP of Operations"),
                 ("side", "client"),
                 ("decision_role", "approver (decides and funds it from her own line: 'It's my budget.'; only spend "
                                   "over $150k a year goes to the CFO and the executive committee, and she says "
                                   "this is not that)")]),
    OrderedDict([("name", "Warren Tibbetts"),
                 ("role", "Senior Project Manager, 18 years with the firm; runs the Cumberland bed tower (about "
                          "$48M) plus two Waverly renovations"),
                 ("side", "client"),
                 ("decision_role", "influencer and end user (the loudest voice on adoption and on single entry: 'I "
                                   "enter my numbers once.'; his forecast spreadsheet is the model for burn)")]),
    OrderedDict([("name", "Ines Kovalenko"),
                 ("role", "Resource Manager; maintains the allocation workbook ('the grid') for project managers, "
                          "superintendents and project engineers across all three offices"),
                 ("side", "client"),
                 ("decision_role", "influencer and end user (and the natural day-to-day owner of whatever replaces "
                                   "the grid, so an admin/owner audience for the demo as well)")]),
]

k["expected_monday_products"] = [
    OrderedDict([("kind", "core"), ("why",
     "monday Work Management, with a portfolio and connected projects, is the whole of this build. The account is "
     "Enterprise with Work Management enabled and stated plainly, so amendment A6's portfolio default applies and "
     "the client's stated need matches it: one view of every active project with a health status, budget burn "
     "against plan, and the next owner milestone and its date (P1, P3). Underneath it, projects built from standard "
     "project templates, one per project type rather than one template for all three (ground-up, occupied "
     "renovation, and short permit-heavy equipment jobs), with ICRA permits carried as tracked dates that expire "
     "(P4). Alongside, allocation for project managers, superintendents and project engineers, including who is "
     "qualified for occupied work, visible to the PMs without asking the resource manager, and explicitly excluding "
     "field crews (P2). On top, a view for the executive committee and something that can be put in front of "
     "Cumberland's program review in January (R6). Build it with monday's portfolio and project tools, connect the "
     "projects, and verify the roll-ups fill in; plain boards named 'Portfolio' would fail the rule. monday dev is "
     "out of v1 and nothing in this call calls for it.")]),
    OrderedDict([("kind", "service"), ("why",
     "Not in this build, and correctly so, but it must be handled rather than ignored. Post-turnover warranty calls "
     "arrive in a shared inbox and go missing ('We lost one for three weeks.'), which is ticket-shaped work that "
     "monday Service covers and that IS inside v1. The client parked it herself ('Different conversation. I know "
     "it's a mess. It's not this year's mess.'), so the right behaviour is a backlog seed and a question for later, "
     "never a hand-built warranty board smuggled into this scope. If it is ever built, it goes on the account's "
     "native Service Tickets board and companions, detected first, and Service extras (customer portal, "
     "email-to-ticket, SLA policy setup) stay deferred beyond v1.")]),
    OrderedDict([("kind", "crm"), ("why",
     "Not in this build. The health systems are accounts and their capital work arrives as pursuits, and "
     "preconstruction already tracks bids on an existing monday board built by someone who has left. Nobody asked "
     "for a pipeline, preconstruction is not this client's group ('That's not my group.'), and the portfolio need is "
     "about work already won. So CRM is a question about the existing board's future, not a proposal. If pursuits or "
     "health-system accounts ever come into scope, they must land on the account's native CRM boards (Leads, "
     "Contacts, Accounts, Deals/Opportunities, Activities), never on a look-alike 'Owners' or 'Pursuits' board.")]),
]

k["rubric"] = [
    R("R1 Current state mapped", "met", [
        "Preconstruction wins it.",
        "Roland sets up the job number in Sage.",
        "The PM sets up the project in Procore, which is where the drawings and RFIs and submittals live.",
        "Insurance certificates, notice to proceed, preconstruction meeting, ICRA, badging, the submittal log setup, "
        "the schedule baseline.",
        "Every Monday the PMs are supposed to send me a status.",
        "It's an email, or a tab in a spreadsheet, or in two cases a text message, and it has percent complete, any "
        "schedule slip, any budget exposure, and a color.",
        "Bridget, my analyst, pulls all of it into the monthly deck for the executive committee.",
        "Two full days a month, and that's if people answer her.",
        "I keep a forecast in Excel.",
        "Because Sage gives me actuals after the month closes, and that's too late to do anything with, so I carry "
        "my own.",
        "We call it the grid.",
        "A tab per office, every person down the left, weeks across the top, and a percentage in each cell.",
        "Preconstruction has a board in monday for tracking bids.",
        "Safety has one too, Lonnie's incident board, and that one's actually used every day.",
        "We're on the enterprise plan, work management, about two hundred and twenty seats.",
        "Stefan owns the contract and Kyle in preconstruction is the one who actually builds things in it.",
    ], "Walked end to end: award from preconstruction, job number in Sage, project set up in Procore, the "
       "60-something-line Excel startup checklist including ICRA, then the running job (weekly OAC meeting, "
       "schedule updated Thursday, superintendent daily reports in Procore, the PM's Friday forecast), then Monday "
       "status emails to the PMO, the analyst's monthly 40-page deck and 40-row summary page, the executive "
       "committee on the second Tuesday, Cumberland's own report in their template, and closeout, turnover and a "
       "year of warranty. Tools and their disconnections are named: Procore for the job, Sage for cost with actuals "
       "around the tenth to twelfth, Excel for the grid and fourteen different PM forecasts, Teams for staffing "
       "requests. People and time are given: 14 PMs at about 4 hours a week assembling, the resource manager at 10 "
       "hours a week, the analyst 2 days a month, the director half a day a month. monday today is fully described, "
       "including who built each board and that one builder has left, plus the plan, product and seat count, which "
       "makes this the first fixture where the tier is known from the transcript."),
    R("R2 Pain made concrete", "met", [
        "Curt asked me a question I could not answer, which was, of these forty, which ones are actually in trouble.",
        "Five weeks late.",
        "It's not wrong on purpose.",
        "Once you find out a green row was five weeks late, you can't unsee that.",
    ], "P1 is excavated: Stated, Concrete and Workaround are all Met, and in fact all six per-pain checks are Met "
       "for both P1 and P2. The August executive committee meeting is a specific, recent, dated-by-month occurrence "
       "with a named consequence."),
    R("R3 Why now", "met", [
        "We signed a four-year master agreement with Cumberland Health in August.",
        "That takes us from forty active projects to something like fifty-five next year, with the same fourteen PMs "
        "and the same one analyst.",
        "Reporting, their PMO has a quarterly program review and the first one is January fifteenth, and I have to "
        "stand up in front of their vice president of facilities and show program-level health, budget and "
        "milestones across every job we're doing for them.",
        "And Bridget goes out on parental leave in November.",
        "Next year's budget locks in November.",
    ], "Four independent triggers, three of them dated: the master agreement signed in August, the first quarterly "
       "program review on January fifteenth with an external audience, the analyst who builds the report going on "
       "leave in November, and the budget lock in November. The client also contrasts now with earlier in the year "
       "('If you'd called me in March I'd have been polite and slow.'), which is the cleanest possible why-now "
       "signal."),
    R("R4 Bleed number", "met", [
        "Fourteen project managers report up through me, and Ines sits in my group.",
        "Call it four hours a week, easily.",
        "Four is fair.",
        "About ninety-five an hour.",
        "Ten, and that's a good week.",
        "Call it seventy-two.",
        "She's at about sixty-five loaded.",
        "Half a day a month, reviewing and rewriting the summary page.",
        "About fifty thousand in overtime and acceleration.",
        "Two a year. Maybe three.",
        "That's what June cost.",
        "Four hundred and thirty-two thousand.",
        "That number is low, if anything.",
        "About right and also horrible.",
    ], "$432,080 a year, every input client-supplied and the total confirmed out loud. Math: PM assembling 14 x 4 "
       "h/wk x 52 x $95 = $276,640; the grid 10 h/wk x 52 x $72 = $37,440; the monthly deck (16 h x $65 = $1,040 "
       "plus 4 h x $115 = $460) x 12 = $18,000; resource collisions 2 x $50,000 = $100,000, taken at the low end of "
       "the client's own 'two a year, maybe three' and shown as a $100,000-$150,000 range. The client confirms the "
       "figure twice, once numerically and once qualitatively, and volunteers that it is understated. Deliberately "
       "excluded and listed separately as unquantified: the $480,000 Cumberland West overrun, because she would not "
       "say how much was avoidable ('Some. Maybe half of it, if I'm honest, and I'm not going to pretend I know "
       "which half.'). The Consultant does the arithmetic aloud, but every input and the confirmation come from the "
       "client, so this is Met rather than Partial."),
    R("R5 Upside number", "met", [
        "I've got two PMs in next year's budget request, at about a hundred and fifty thousand each all in.",
        "I'd hold one.",
        "We turned down two invitations last year because we couldn't staff them.",
        "Eight to twelve million in revenue, and we make about three and a half points on that kind of work.",
        "One is realistic.",
        "Waverly wants one partner for their whole outpatient program.",
        "And I can't credibly say yes, because I cannot show them how we'd run twenty of their jobs at once when I "
        "can't show anybody how we run forty now.",
    ], "Two client-figured components plus the 'what would you go after' answer. Deferred hire: one of two budgeted "
       "PMs at about $150,000 all in, held rather than hired, and she refuses to claim both, which is a credibility "
       "signal worth keeping. Capacity to bid: two invitations were no-bid last year for lack of a superintendent; a "
       "job is $8M-$12M at about 3.5 points, so one more a year is about $280,000 of fee at the low end. The "
       "ambition is explicit and unprompted: Waverly's whole outpatient programme, which she cannot credibly pitch "
       "while she cannot show how forty jobs run today. Discipline note: the $150,000 comes out of the same freed "
       "reporting hours already counted in the bleed, so it must not be added to the bleed total."),
    R("R6 Desired outcome", "met", [
        "I open one screen on Monday morning and I see forty projects, with a color and a number, and I believe it.",
        "And I stop emailing people for it.",
        "If I want to know which ones are in trouble I look, I don't ask.",
        "Budget.",
        "He wants to walk into the second Tuesday and not be surprised.",
        "If I can pull their program up on a screen in front of their VP of facilities and it's current, that's the "
        "win.",
        "I enter my numbers once.",
        "And I'd like somebody to be able to answer Warren without me.",
    ], "A day-to-day picture from all three people and a leadership win condition in two forms: the VP of Operations "
       "not being surprised at the second Tuesday meeting, and the Cumberland program review in January going well. "
       "Turn these into draft success criteria marked proposed, not agreed: they were described, not signed off, "
       "which is why the v1.0 sign-off gate stays closed."),
    R("R7 Decision process mapped", "met", [
        "It's my budget.",
        "Anything over a hundred and fifty thousand a year goes to Corinne and then the executive committee.",
        "So practically, I decide, Corinne's team raises the PO, and Stefan does his security review.",
        "And he will have a questionnaire.",
        "Two to three weeks, and he's thorough.",
        "Nothing touches Sage without Roland, and he is protective of Sage, and I'd say rightly.",
        "Procore, three years ago.",
        "Security review, a pilot, then a rollout with training.",
    ], "Fully mapped, and the approver is on the call, which is unusual for this fixture set. She decides and funds "
       "it from the PMO line; the $150k-a-year threshold that would pull in the CFO and the executive committee is "
       "named and she says this is below it; the sequence after a yes is stated (she decides, the CFO's team raises "
       "the PO, the IT director runs a two-to-three-week security review with a questionnaire and SSO questions); "
       "the controller is a gate on anything touching Sage; and there is prior budgeting experience with the same "
       "pattern from buying Procore three years ago. What each person cares about is also given: the VP of "
       "Operations wants no surprises, the IT director wants SSO, data location and export control, the controller "
       "protects Sage."),
    R("R8 Priority and timing", "met", [
        "This is the thing I'm working on.",
        "If you'd called me in March I'd have been polite and slow.",
        "I'd want something real running on a handful of jobs by the middle of November, so we've shaken it out "
        "before the holidays, and everything on it in time for January fifteenth.",
        "Warren's three, and three of the Chattanooga ones so it's not all one office.",
    ], "Placed firmly on the now side with a reason, and given real dates: a pilot on six projects by mid-November, "
       "everything on it for January fifteenth. The pilot selection is even specified, deliberately spanning two "
       "offices."),
    R("R9 Blockers surfaced", "met", [
        "Adoption.",
        "We tried Smartsheet in twenty twenty-three and it lasted about a quarter.",
        "So it became another thing to update, and the PMs smiled at me and quietly didn't.",
        "If it's another thing to update, it's dead.",
        "And if the supers have to log in, it's dead twice, because they're on a phone in a trailer with one bar.",
        "Stefan's guy told him he could build this in Power BI in a couple of weeks.",
        "I should tell you we're also talking to another partner.",
        "And half our sites have no signal inside the building.",
    ], "Named without being asked twice: adoption with a specific prior failure and its cause (double entry, the old "
       "thing never removed), field connectivity, an in-house Power BI alternative, the security review, the "
       "controller's protection of Sage, and a competing partner. Each maps to a prevention step rather than a "
       "rebuttal."),
    R("R10 Next step committed", "met", [
        "After one, I've got an OAC at eleven.",
        "Two o'clock Eastern on the twenty-third, then.",
        "Works.",
        "Two o'clock Eastern, Wednesday the twenty-third, forty-five minutes.",
    ], "Date, time, length, attendees and owner all settled on the call, with the client naming the time herself and "
       "both other attendees confirming. The Consultant commits to sending the invite the same afternoon, so R10 is "
       "Met rather than the common 'I'll follow up' failure."),
    R("R11 Solution confirmed", "missing", [],
      "No demo has happened, so no pain has been confirmed against something shown. This closes the v1.0 sign-off "
      "gate and becomes the goal of the first walkthrough on the twenty-third."),
    R("R12 Scope agreed verbally", "met", [
        "Yes. Those five. That's what I'd sign up for.",
        "I'd add that Warren enters his numbers once, but that's inside number one.",
        "And field crews stay out.",
        "Go.",
    ], "The Consultant plays back a five-item scope and the approver agrees to it out loud, unhedged, then adds one "
       "clarification inside item one and the resource manager adds one explicit exclusion. This is the first "
       "fixture in the set where R12 is Met, which opens the pricing-or-proposal gate for the first time. The "
       "agreed five: the portfolio view with health, burn and the next owner milestone; a standard project template "
       "per project type with ICRA expiry tracked; allocation for PMs, superintendents and project engineers "
       "including occupied-work qualification and excluding field crews; a view for the executive committee plus "
       "something for Cumberland in January; and a pilot on six projects by mid-November before the rest."),

    # ---------------- P1: no trustworthy portfolio view
    R("P1 Stated", "met", [
        "I have forty projects and I could not put that slide together in less than a week.",
        "The summary page.",
        "Because it's wrong.",
        "It's not wrong on purpose.",
    ], "Stated twice, in her own words, first as envy at a conference and then as the specific artefact she does not "
       "trust."),
    R("P1 Concrete", "met", [
        "The August meeting.",
        "And he says, didn't you tell me last month that one was waiting on a switchgear delivery?",
        "Five weeks late.",
        "Curt asked me a question I could not answer, which was, of these forty, which ones are actually in trouble.",
    ], "A specific recent occurrence with month, room, participant, the exact question asked and the real state of "
       "the project behind the green row."),
    R("P1 Workaround", "met", [
        "Open the deck from the tenth, which is a month old.",
        "Half a day, and I still wouldn't swear to it.",
        "The second is that I don't believe it anymore.",
        "Once you find out a green row was five weeks late, you can't unsee that.",
    ], "Names today's method (a month-old deck, her email, calling six PMs, half a day) and why carrying on is not "
       "acceptable: even the output of that half day would not be trustworthy, and trust in every green row is now "
       "gone."),
    R("P1 Reach", "met", [
        "The PMs, because they're the ones being chased.",
        "They don't answer her.",
        "It reaches Cumberland.",
        "Their PMO wants a monthly report per project in their format, and under the new agreement they want it at "
        "program level too.",
        "Same facts, four formats.",
    ], "Reaches the fourteen PMs, the analyst, the director, the executive committee and the client's own customer. "
       "Warren's 'same facts, four formats' quantifies the duplication: the PMO status, his forecast, the owner's "
       "OAC agenda and staffing."),
    R("P1 Cost inputs", "met", [
        "Call it four hours a week, easily.",
        "Four is fair.",
        "About ninety-five an hour.",
        "Two full days a month, and that's if people answer her.",
        "She's at about sixty-five loaded.",
        "Half a day a month, reviewing and rewriting the summary page.",
    ], "Hours, headcount, frequency and loaded costs for all three roles involved, all client-supplied."),
    R("P1 Trajectory", "met", [
        "Worse, and I can be specific about why.",
        "That takes us from forty active projects to something like fifty-five next year, with the same fourteen PMs "
        "and the same one analyst.",
        "Is gone from November.",
        "And I don't have a second Bridget.",
    ], "A year out is quantified rather than gestured at: about 37 percent more projects on the same headcount, and "
       "the one person who assembles the report leaves the picture in November."),

    # ---------------- P2: resource collisions
    R("P2 Stated", "met", [
        "When a superintendent calls me from the wrong job site.",
        "The grid tells you who's busy.",
        "It does not tell you who's the right person.",
    ], "Stated by the person who owns the process, plus the sharper second half from her director: the workbook "
       "holds availability but not capability, and capability lives in one person's head."),
    R("P2 Concrete", "met", [
        "June. Junie Rasco.",
        "Warren had him penciled for the Waverly cath lab, and preconstruction had promised him to the Pellham "
        "fit-out, and both started the same week.",
        "I did not pencil him. I had him confirmed. Verbally.",
        "We moved Junie to Waverly because that one had a hard date with the owner, and then Pellham started with an "
        "assistant super and we ran overtime for six weeks to hold the date.",
    ], "A dated, named, fully traced instance, including the disagreement about whether the superintendent was "
       "penciled or confirmed, which is itself the evidence that the commitment lived in a hallway rather than a "
       "system."),
    R("P2 Workaround", "met", [
        "By me. Every week. Monday and Tuesday morning are the grid.",
        "Ten, and that's a good week.",
        "Teams messages, mostly.",
        "It's just that it lives on my laptop and in my head, and nobody can see it.",
        "And if I'm on holiday, nobody can answer him at all.",
    ], "The workaround works, and she says so, which is the honest version: the objection to it is not that it "
       "fails but that it is invisible to everyone else and stops entirely when she does."),
    R("P2 Reach", "met", [
        "The supers, first.",
        "They're the ones told on a Friday that Monday changed.",
        "And the owner finds out when a date moves, which is the one that actually costs us, because some of those "
        "dates have LDs behind them.",
        "Right. On the bed tower there's a date for first patient day and there's money behind it.",
    ], "Superintendents, PMs whose schedules assumed a person, the director, and the client's own customer, with "
       "liquidated damages behind some owner dates, which is where it turns into money."),
    R("P2 Cost inputs", "met", [
        "Ten, and that's a good week.",
        "Call it seventy-two.",
        "About fifty thousand in overtime and acceleration.",
        "Two a year. Maybe three.",
        "That's what June cost.",
    ], "Both a recurring labour cost and an event cost with a frequency, all from the client. The frequency is a "
       "range, so the low end is used and the range is shown."),
    R("P2 Trajectory", "met", [
        "All of Cumberland's work is in occupied buildings.",
        "So the same four names.",
        "Occupied-renovation supers, there are four.",
    ], "The constraint gets tighter rather than looser: the growth is all occupied-building work, which only four "
       "superintendents can run."),

    # ---------------- P3: budget burn seen too late
    R("P3 Stated", "met", [
        "So on the twelfth of September I find out what August really cost me.",
        "We were four hundred and eighty thousand over on the mechanical buyout and we found out six weeks after it "
        "happened.",
        "There's no such thing as a portfolio number for us.",
    ], "Stated from both ends: the PM's lag between spend and actuals, and the director's inability to add fourteen "
       "different forecasts into one number."),
    R("P3 Concrete", "met", [
        "Cumberland West.",
        "Roland closed the month and called me.",
        "Which is not how I want to learn things.",
        "The buyout came in high, the PM knew the buyout came in high, and he was working a change order with the "
        "owner to cover part of it.",
    ], "A named project, a named amount, how it surfaced, and the mechanism: the PM was managing it honestly, but it "
       "never reached a number the PMO could see before the next phases were committed."),
    R("P3 Workaround", "met", [
        "I keep a forecast in Excel.",
        "The problem is that I have fourteen of these and no two are built the same, so I cannot add them up.",
        "There's fourteen spreadsheets.",
        "Mine's good.",
    ], "Fourteen private forecasts of varying quality, explicitly not addable, and the good one is not the problem, "
       "which is the argument for a standard rather than for policing."),
    R("P3 Reach", "met", [
        "Roland, because he's the one making the call.",
        "Corinne, because she's forecasting cash off it.",
        "And the owner, honestly, because a change order conversation in week eight looks like we weren't watching.",
    ], "The controller, the CFO's cash forecast, and the client's own credibility with the owner during a change "
       "order conversation."),
    R("P3 Cost inputs", "partial", [
        "We were four hundred and eighty thousand over on the mechanical buyout and we found out six weeks after it "
        "happened.",
        "Some. Maybe half of it, if I'm honest, and I'm not going to pretend I know which half.",
    ], "Partial on purpose. There is one large one-off figure and an explicit refusal to say how much was "
       "avoidable, and no recurring rate (how often overruns surface late, or the typical size). So the $480,000 "
       "sits beside the bleed as unquantified rather than inside it, and the next prep asks for frequency and "
       "typical size instead. Treating it as a $240,000-a-year saving would be inventing the client's number for "
       "her."),
    R("P3 Trajectory", "partial", [
        "It doesn't get better.",
        "I don't have a number for that one, it just doesn't get better.",
    ], "Partial: she says it will not improve but gives no year-out picture and no figure, and unlike P1 she does "
       "not tie it to the volume increase. A trajectory question for the next conversation, worth asking because "
       "fifty-five projects means fifty-five forecasts."),

    # ---------------- P4: no standard project start
    R("P4 Stated", "met", [
        "That's the honest answer, yes. Every PM starts a job their own way.",
        "In practice everybody has their own version.",
        "Consistency.",
    ], "Stated by the director and corroborated immediately by her senior PM, who admits his own version has extra "
       "lines on it."),
    R("P4 Concrete", "partial", [
        "And I can't point you at one job and say, here, this went wrong.",
        "Somebody's baseline schedule is in the system, somebody's is in their drawer.",
        "Somebody's ICRA is tracked with an expiry date, somebody's is a PDF in a folder.",
        "I've seen it happen. Not to me.",
    ], "Partial by the spec's definition: she describes what it looks like day to day, which the check allows, but "
       "explicitly cannot give a specific recent occurrence, and the one vivid consequence (an ICRA permit lapsing "
       "and the job being shut down for a day) is secondhand and undated. A concreteness question for the next "
       "conversation, and a reason to ask for the last three project startups rather than a story."),
    R("P4 Workaround", "met", [
        "An Excel file.",
        "Sixty-something lines.",
        "In theory.",
        "Mine's got things on it the master doesn't, because I've been burned.",
    ], "The workaround is a 60-something-line Excel checklist that exists but is not followed, and the private "
       "variants are the evidence that it does not hold."),
    R("P4 Reach", "met", [
        "The project engineers, because they're the ones actually doing the steps.",
        "The admin who does badging.",
        "And the new PMs suffer most.",
        "And the owner sees it, because their first impression of us is whether the first three weeks are organized.",
    ], "Project engineers, the badging admin, the safety director, new hires without healthcare experience, and the "
       "owner's first impression."),
    R("P4 Cost inputs", "missing", [],
      "No hours, frequency or cost were attached to inconsistent startups. A cost question for the next "
      "conversation, and the reason P4 is not excavated."),
    R("P4 Trajectory", "missing", [],
      "Nothing was said about what inconsistent startups look like at fifty-five projects a year with new PMs, "
      "which is the obvious follow-up given the growth."),

    # ---------------- P5: warranty calls after turnover
    R("P5 Stated", "met", [
        "An inbox.",
        "Turnover, punch list, closeout documents, and then warranty for a year.",
    ], "Stated plainly: a year of warranty obligation managed out of a shared inbox."),
    R("P5 Concrete", "partial", [
        "We lost one for three weeks.",
        "A door closer at Waverly.",
        "Which is a small thing, except the person who called it in was their facilities director, who decides who "
        "gets the next fit-out.",
    ], "Partial: there is one instance with a consequence that matters commercially, but no date, no frequency and "
       "no description of how it normally runs."),
    R("P5 Workaround", "partial", [
        "Somebody watches it, mostly.",
        "Different conversation.",
    ], "Partial: what they do today is named, but not why carrying on that way is unacceptable. The opposite, in "
       "fact, is stated: the client parks the problem for this year, so the workaround stands by her own choice."),
    R("P5 Reach", "missing", [],
      "Nobody said who else the warranty inbox affects, beyond the one facilities director in the single story. The "
      "only per-pain check in this fixture graded Missing on Reach."),
    R("P5 Cost inputs", "missing", [], "No hours, volume or cost for warranty calls."),
    R("P5 Trajectory", "missing", [],
      "Nothing about what a year of warranty on fifty-five projects looks like. Out of scope by the client's own "
      "decision, so this stays a backlog seed rather than a gap to chase."),
]

k["pains"] = [
    P("I have forty projects and I could not put that slide together in less than a week.",
      "P1 No trustworthy portfolio view: the director cannot produce a single picture of her own projects"),
    P("Because it's wrong.",
      "P1 The monthly summary page is not believed by the person who produces it"),
    P("It's not wrong on purpose.",
      "P1 The report is assembled from forty people's varying inputs rather than being wrong deliberately"),
    P("Curt asked me a question I could not answer, which was, of these forty, which ones are actually in trouble.",
      "P1 The concrete instance: the August executive committee meeting"),
    P("Five weeks late.",
      "P1 A project showing green was five weeks late"),
    P("Once you find out a green row was five weeks late, you can't unsee that.",
      "P1 Trust in the status colours is gone, which is why the workaround cannot continue"),
    P("Half a day, and I still wouldn't swear to it.",
      "P1 Answering a basic portfolio question today costs half a day and still is not reliable"),
    P("Same facts, four formats.",
      "P1 PMs re-assemble the same information for four audiences"),
    P("And I don't have a second Bridget.",
      "P1 Trajectory: the one person who assembles the report goes on leave in November"),
    P("When a superintendent calls me from the wrong job site.",
      "P2 Resource collisions: conflicts surface at the job site, not in planning"),
    P("Warren had him penciled for the Waverly cath lab, and preconstruction had promised him to the Pellham "
      "fit-out, and both started the same week.",
      "P2 The concrete instance: one superintendent promised to two jobs starting the same week in June"),
    P("I did not pencil him. I had him confirmed. Verbally.",
      "P2 Commitments live in hallway conversations, so two people can both believe they have the same person"),
    P("It's just that it lives on my laptop and in my head, and nobody can see it.",
      "P2 The allocation workbook is invisible to everyone but its owner"),
    P("It does not tell you who's the right person.",
      "P2 Availability is tracked, capability for occupied-building work is not"),
    P("And then somebody reshuffles it in a meeting I'm not in, and I find out when the grid doesn't match the job "
      "site.",
      "P2 Corroboration only: this cue is tagged '<v Speaker 2>', so the speaker must be recorded as unclear (it is "
      "Ines Kovalenko by context) and it cannot carry a Met on its own"),
    P("So on the twelfth of September I find out what August really cost me.",
      "P3 Budget burn: actuals arrive up to six weeks after the spend"),
    P("We were four hundred and eighty thousand over on the mechanical buyout and we found out six weeks after it "
      "happened.",
      "P3 The concrete instance: the Cumberland West overrun, found six weeks late"),
    P("The problem is that I have fourteen of these and no two are built the same, so I cannot add them up.",
      "P3 Fourteen private PM forecasts cannot be rolled up into a portfolio number"),
    P("And the owner, honestly, because a change order conversation in week eight looks like we weren't watching.",
      "P3 Reach: late visibility damages credibility with the health system during change orders"),
    P("That's the honest answer, yes. Every PM starts a job their own way.",
      "P4 No standard project start: every PM runs their own version of the startup checklist"),
    P("Somebody's ICRA is tracked with an expiry date, somebody's is a PDF in a folder.",
      "P4 Infection-control permits, which expire, are tracked inconsistently"),
    P("And the new PMs suffer most.",
      "P4 Reach: PMs hired from outside healthcare do not know what they do not know"),
    P("An inbox.",
      "P5 Warranty calls after turnover are managed out of a shared inbox"),
    P("We lost one for three weeks.",
      "P5 A warranty call went unanswered for three weeks; ticket-shaped work, parked by the client for this year"),
]

k["numbers"] = OrderedDict([
    ("bleed", OrderedDict([
        ("value",
         "$432,080 per year, confirmed by the client. Components: PM status assembling 14 PMs x 4 h/wk x 52 x $95 "
         "loaded = $276,640; the resource grid 10 h/wk x 52 x $72 = $37,440; the monthly deck (16 h x $65 = $1,040 "
         "for the analyst, plus 4 h x $115 = $460 for the director) x 12 = $18,000; resource collisions at 2 a year "
         "x about $50,000 = $100,000, taken at the low end of the client's 'Two a year. Maybe three.' and shown as "
         "a range of $100,000-$150,000. Excluded and listed separately as unquantified: the $480,000 Cumberland West "
         "mechanical buyout overrun, because the client explicitly would not say how much of it was avoidable, and "
         "there is no frequency for late-surfacing overruns. The client volunteered that the total is understated."),
        ("quote", "Four hundred and thirty-two thousand."),
        ("status", "met"),
    ])),
    ("upside", OrderedDict([
        ("value",
         "About $430,000 a year in two client-figured parts, kept separate from the bleed. First, $150,000 of "
         "deferred hiring: two PMs are in next year's budget at about $150,000 all in each, and she would hold one "
         "(not both) if the existing fourteen could carry their jobs. This comes out of the same freed reporting "
         "hours already counted in the bleed, so it must never be added to the bleed total. Second, about $280,000 "
         "of fee from one more staffable job a year: two invitations were no-bid last year for lack of a "
         "superintendent, such jobs run $8M-$12M in revenue at about 3.5 points, and she calls one more a year "
         "realistic while refusing two. The 'what would you go after' answer is explicit: Waverly's entire "
         "outpatient programme, which she cannot credibly pursue while she cannot show how forty jobs run today."),
        ("quote", "I've got two PMs in next year's budget request, at about a hundred and fifty thousand each all "
                  "in."),
        ("status", "met"),
    ])),
])

k["vocabulary"] = [
    {"their_term": "portfolio", "meaning": "Every active job across all three offices, about forty of them; her own "
     "word, used before the Consultant used it",
     "likely_monday_object": "a monday portfolio with the active projects connected to it (Enterprise plus Work "
     "Management, so the A6 default applies)"},
    {"their_term": "program", "meaning": "All of one health system's work under a master agreement, twelve to "
     "fifteen jobs at a time; Cumberland is a program and Waverly would become a second one",
     "likely_monday_object": "open question, and one to ask rather than assume: a grouping or view inside one "
     "portfolio, or a portfolio per program. A job belongs to the portfolio and a program at the same time"},
    {"their_term": "the board", "meaning": "The executive committee (VP of Operations, CFO, two principals) that "
     "meets the second Tuesday. The firm is privately held and has no actual board",
     "likely_monday_object": "nothing; a homonym trap. It is an audience for a dashboard, not a monday board"},
    {"their_term": "health", "meaning": "A project's red-amber-green status, set by its PM",
     "likely_monday_object": "status column on the project, rolled up to the portfolio; nothing clinical is meant "
     "by the word"},
    {"their_term": "burn", "meaning": "Cost spent against plan on a job",
     "likely_monday_object": "numbers or formula columns on the project, mirrored up to the portfolio; the actuals "
     "come from Sage, which stays the book of record"},
    {"their_term": "the grid", "meaning": "Ines's Excel allocation workbook: a tab per office, people down the "
     "left, weeks across the top, percentages in the cells",
     "likely_monday_object": "a resource or allocation board with a workload view, owned by the resource manager"},
    {"their_term": "the deck", "meaning": "The monthly 40-page executive report plus its 40-row summary page, "
     "assembled by the PMO analyst",
     "likely_monday_object": "portfolio dashboard plus an exportable summary view; the deck itself is the artefact "
     "to replace"},
    {"their_term": "the owner", "meaning": "The health system that owns the building and pays for the work",
     "likely_monday_object": "the client's own customer, not a monday item owner or People column; if ever "
     "tracked as records, health systems belong on the native CRM Accounts board"},
    {"their_term": "job / project", "meaning": "Used interchangeably for one construction project; 'equipment job' "
     "is a short project of the same shape",
     "likely_monday_object": "a monday project connected to the portfolio, including the equipment jobs"},
    {"their_term": "equipment job", "meaning": "A six-week, roughly $1.5M scope such as an MRI replacement or a "
     "linear accelerator swap, with all the same steps as a large job",
     "likely_monday_object": "a project from the equipment-job template, connected to the portfolio like any other"},
    {"their_term": "occupied renovation", "meaning": "Work inside a live clinical building, which is most of what "
     "they do and what only four superintendents are qualified to run",
     "likely_monday_object": "project type on the project template, plus a qualification attribute on people in "
     "the allocation board"},
    {"their_term": "ICRA", "meaning": "Infection control risk assessment: a permit per work area, signed by the "
     "hospital's infection control nurse, which expires and can shut the job down if it lapses",
     "likely_monday_object": "a dated, expiring item or date column inside the occupied-renovation project "
     "template, with a reminder automation"},
    {"their_term": "ILSM", "meaning": "Interim life safety measures required while working in an occupied "
     "healthcare building",
     "likely_monday_object": "template steps inside the occupied-renovation project type"},
    {"their_term": "super", "meaning": "Superintendent, the field leader of a job",
     "likely_monday_object": "person record in the allocation board, with an occupied-work qualification"},
    {"their_term": "PE", "meaning": "Project engineer, who does many of the startup steps",
     "likely_monday_object": "person record in the allocation board; an end user of the project template"},
    {"their_term": "milestone", "meaning": "An owner-facing contractual date; eleven or twelve per large job, "
     "several per phase, some with money behind them",
     "likely_monday_object": "milestone items under the project, not a single date column; the next one rolls up "
     "to the portfolio with its date"},
    {"their_term": "first patient day", "meaning": "The date the owner starts using the space, with liquidated "
     "damages behind it on the bed tower",
     "likely_monday_object": "a milestone item with a flag for contractual exposure"},
    {"their_term": "LDs", "meaning": "Liquidated damages behind certain owner dates",
     "likely_monday_object": "an attribute on milestone items; the amounts themselves are commercially sensitive"},
    {"their_term": "buyout", "meaning": "Awarding a trade package; where the Cumberland West overrun appeared",
     "likely_monday_object": "a cost or commitment stage on the project, reported as burn rather than rebuilt as "
     "accounting"},
    {"their_term": "turnover, punch list, closeout", "meaning": "The end-of-job sequence, followed by a year of "
     "warranty",
     "likely_monday_object": "closing phases in the project template; warranty is out of this scope"},
    {"their_term": "OAC meeting", "meaning": "The weekly owner-architect-contractor meeting",
     "likely_monday_object": "a recurring meeting the project data should serve; one of the four formats PMs "
     "currently rebuild by hand"},
    {"their_term": "no-bid", "meaning": "Declining an invitation to bid, in their case for lack of a "
     "superintendent",
     "likely_monday_object": "nothing in this build; it belongs to preconstruction's existing bid board and is "
     "part of the upside story"},
    {"their_term": "master agreement / MSA", "meaning": "A multi-year agreement under which all of a health "
     "system's capital work flows to them; the Cumberland one was signed in August",
     "likely_monday_object": "the thing a 'program' hangs off; a question for the portfolio shape"},
    {"their_term": "the summary page", "meaning": "The 40-row, four-column front page of the deck that leadership "
     "actually reads",
     "likely_monday_object": "the portfolio view itself; the client should be able to open it rather than receive "
     "it"},
]

k["entities_and_workflows"] = [
    "Award handover: preconstruction wins the work and hands it to the PMO, which assigns a project manager and a "
    "superintendent. Preconstruction is explicitly not this client's group.",
    "Project setup: the controller opens a job number in Sage 300, the PM sets up the project in Procore for "
    "drawings, RFIs and submittals, and the PM works through a 60-something-line Excel startup checklist "
    "(insurance certificates, notice to proceed, preconstruction meeting, ICRA, badging, submittal log, schedule "
    "baseline). Every PM has their own variant of the checklist.",
    "Infection control: an ICRA permit per work area, signed by the hospital's infection control nurse, specifying "
    "barriers, negative air and cart routes. It expires, and a lapse means being shut down that day. Interim life "
    "safety measures apply alongside it in occupied buildings.",
    "Project types with different templates and milestone sets: ground-up, occupied renovation (where infection "
    "control and life safety live), and short permit-heavy equipment jobs such as an MRI or linear accelerator "
    "replacement.",
    "Running a job week to week: a weekly OAC meeting with owner and architect, the schedule updated Thursday "
    "night, superintendent daily reports in Procore, and the PM's Friday cost-to-complete forecast in a private "
    "Excel file.",
    "Owner milestones: eleven or twelve per large job that the owner cares about (permit issued, steel topped out, "
    "dry-in, first energization, imaging equipment delivery, substantial completion, first patient day), several "
    "per phase, some with liquidated damages, and when one moves the owner wants the previous date to still exist.",
    "Weekly PMO status: each PM sends the director percent complete, schedule slip, budget exposure and a "
    "red-amber-green colour, by email, spreadsheet tab or text message. The PM sets the colour.",
    "Monthly reporting: the PMO analyst assembles a 40-page deck plus a 40-row summary page, chasing PMs for "
    "inputs, and it goes out around the tenth for the executive committee's second-Tuesday meeting.",
    "Owner-side reporting: Cumberland's PMO wants a monthly report per project in their own template, and under the "
    "new master agreement wants it at program level, with a quarterly program review starting January fifteenth.",
    "Cost reporting: Sage job cost reports land around the tenth to twelfth of the following month, so a PM learns "
    "August's real cost in mid-September; overruns can surface after the next phases are committed.",
    "Resource allocation: the resource manager maintains the grid weekly (Monday and Tuesday morning), requests "
    "arrive as Teams messages or hallway conversations, and conflicts surface when a superintendent turns up at the "
    "wrong job. Only four superintendents can run occupied work. Field crew scheduling belongs to the "
    "superintendents and is explicitly out of scope.",
    "Turnover and closeout: turnover, punch list, closeout documents, then a year of warranty.",
    "Warranty: post-turnover calls arrive in a shared inbox that somebody watches 'mostly'; one was lost for three "
    "weeks. Ticket-shaped, in v1 as Service, but parked by the client for this year.",
    "Buying process: the PMO director decides and funds from her own line, the CFO's team raises the PO, the IT "
    "director runs a two-to-three-week security review with a questionnaire, the controller gates anything touching "
    "Sage, then a pilot and a rollout with training, as they did with Procore three years ago.",
]

k["integrations_mentioned"] = [
    "Procore: stays as the system of record for drawings, RFIs, submittals and daily reports, and is explicitly not "
    "being replaced ('Procore is the job.'). The boundary must be stated, not blurred; nobody asked to duplicate "
    "RFIs.",
    "Sage 300: the source of cost actuals for budget burn and the book of record for anything with a dollar sign. "
    "Access is gated by the controller, and the transcript never says whether an API, export or report feed is "
    "available, so this is the biggest open integration question of the build.",
    "Microsoft 365 and Teams: where staffing requests happen today; Teams is a realistic notification target.",
    "Microsoft single sign-on: the IT director will require it, along with questions about where the data sits and "
    "who can export it.",
    "Excel: the grid, the startup checklist, fourteen PM forecasts and Cumberland's report template; the template "
    "is being sent as an input, so an export or view shaped like it is in scope.",
    "monday.com already in the account: preconstruction's bid board (builder has left) and safety's incident board "
    "(owned and used daily). Both must be audited rather than duplicated or disturbed.",
    "Power BI: proposed inside the client's IT team as a do-it-ourselves alternative; relevant because it answers "
    "reporting but not data capture.",
    "Smartsheet: an abandoned 2023 pilot, relevant as adoption history rather than as an integration.",
    "A shared warranty inbox: email-shaped intake, and the natural home of a later Service conversation. "
    "Email-to-ticket is deferred beyond v1, so it must not be promised.",
]

k["compliance_or_security_signals"] = [
    "No patient information in any of their systems, stated as non-negotiable, and no photographs containing a "
    "patient or a whiteboard with names on it. Crews work in occupied clinical units carrying phones, and the "
    "client's customers run walk-throughs, so any photo or update field has to be designed with this in mind and "
    "seed data must never imply patient data.",
    "Field staff immunization records and background checks stay with HR and must not go into a project system; the "
    "client has already refused this request internally.",
    "ICRA permits: per work area, signed by the hospital's infection control practitioner, with an expiry that can "
    "shut the job down if it lapses.",
    "Interim life safety measures while working in occupied healthcare buildings.",
    "Badging for field staff at client sites, handled by an admin as part of project startup.",
    "Loaded rates are restricted: PMs see hours, not each other's rates, and not the cost figures worked out on "
    "this call.",
    "Cross-job margin is restricted: a PM seeing their own job's cost is fine, a PM seeing every job's margin is "
    "not, and the client wants to think about the boundary.",
    "Audit trail on status changes: if a PM moves a health status from yellow to green, she wants to know who did "
    "it and when.",
    "Milestone date history: when a date moves, the previous date must still exist somewhere, for the owner's "
    "benefit as well as hers.",
    "Microsoft single sign-on, plus an IT security questionnaire covering where data sits and who can export it, "
    "run by the IT director over two to three weeks.",
    "Sage is the book of record for anything with a dollar sign, and the controller gates access to it.",
    "Liquidated damages behind certain owner dates make contractual exposure commercially sensitive.",
]

k["objections"] = [
    {"quote": "I should tell you we're also talking to another partner.",
     "type": "Talking to other partners (raised, and volunteered by the approver: a Nashville firm that did "
             "Waverly's rollout, coming in next week, surfaced because the VP of Operations asked around. The spec's "
             "response is to welcome it and ask what they have seen and what would make the choice clear, which the "
             "Consultant does; her answer is a concrete buying criterion, so R6 is being used as prevention. "
             "Internal only: the partner and this exchange must never appear in client-facing material)"},
    {"quote": "We tried Smartsheet in twenty twenty-three and it lasted about a quarter.",
     "type": "Team won't adopt it (raised as the first-named blocker, with the cause given: double entry and the old "
             "process never being removed. Prevention is an end-user conversation and an end-user demo segment, plus "
             "a plan for what stops being done)"},
    {"quote": "If it's another thing to update, it's dead.",
     "type": "Team won't adopt it (the senior PM's blunter version, extended to the field: superintendents on a "
             "phone with one bar, so the design must ask them for two things a week, not eight fields)"},
    {"quote": "Half the columns are empty and nobody trusts what's in it.",
     "type": "monday itself is the problem (raised about their existing preconstruction board. The spec's response "
             "is to ask what it fails to do and check whether the setup or the tool is the cause, and the call "
             "supplies the answer: the builder left in February and nobody took it over, while the safety board with "
             "a present owner is used daily. R1 evidence resolves this rather than a rebuttal)"},
    {"quote": "Stefan's guy told him he could build this in Power BI in a couple of weeks.",
     "type": "We'll build it ourselves (raised pre-emptively by the approver, who also answers it herself: a report "
             "is the easy half and the data capture is the problem. The prevention is the workaround question; the "
             "response is to agree that a dashboard is the easy half rather than to argue)"},
    {"quote": "Nothing touches Sage without Roland, and he is protective of Sage, and I'd say rightly.",
     "type": "Must check with someone (the controller is a real gate on the integration that the budget-burn half of "
             "the build depends on. Prevention is mapping the decision process, which is done; the action is to ask "
             "what he will care about and offer to join that conversation)"},
    {"quote": "Two to three weeks, and he's thorough.",
     "type": "Must check with someone (the IT director's security review, with a questionnaire, SSO and data "
             "questions. It is the longest pole against a mid-November pilot, which is why the Consultant asks to "
             "start it now)"},
    {"quote": "Send me a scope and a number I can put against my line before the budget lock in November.",
     "type": "Just send a proposal or pricing (raised by the approver with a real deadline behind it. The spec's "
             "prevention, agreeing the scope first, has already happened in this call, so R12 is Met and the gate is "
             "open. The v1 constraint is what binds instead: pricing and proposal prep are deferred beyond v1, so "
             "the plugin must record the request with its date and hand it to the consultant, not draft a figure)"},
]

k["commitments_and_next_steps"] = [
    {"quote": "Two o'clock Eastern on the twenty-third, then.",
     "what": "Next meeting: a first-cut walkthrough built on six of their real jobs with their real project names, "
             "45 minutes, with Marisol, Warren and Ines",
     "owner": "Consultant (hosts and builds it); all three client attendees confirmed on the call",
     "date": "Wednesday the 23rd, 2:00 pm Eastern (month not stated; the 23rd is a Wednesday in September 2026)"},
    {"quote": "I'll send the invite this afternoon.",
     "what": "Send the calendar invite for the 23rd to the three client attendees",
     "owner": "Consultant", "date": "The afternoon of the call"},
    {"quote": "And I'll send you Cumberland's template and the summary page from August so you can see the shape of "
              "it.",
     "what": "Send the owner's reporting template and August's 40-row summary page as build inputs",
     "owner": "Marisol Bettencourt", "date": "Not dated; before the 23rd by implication"},
    {"quote": "I can send it today.",
     "what": "Send two tabs of the resource grid, checked for any rates and scrubbed if present",
     "owner": "Ines Kovalenko", "date": "Day of the call"},
    {"quote": "You can have it.",
     "what": "Send the senior PM's cost-to-complete forecast spreadsheet, the model for how burn should work",
     "owner": "Warren Tibbetts", "date": "Not dated"},
    {"quote": "I'll email him today and tell him it's coming.",
     "what": "Start the IT director's security review now rather than in three weeks, because it is the longest pole "
             "against a mid-November pilot",
     "owner": "Marisol Bettencourt", "date": "Day of the call"},
    {"quote": "I'll send what he needs with the invite.",
     "what": "Send the security and compliance documentation the IT director will want, with the invite",
     "owner": "Consultant", "date": "The afternoon of the call"},
    {"quote": "You'll get both.",
     "what": "Send a written scope and a figure the client can put against her budget line. Note for the plugin: "
             "this is the consultant's own commitment and pricing and proposal prep are deferred beyond v1, so it "
             "is recorded as a consultant to-do with its November deadline, not drafted by the plugin",
     "owner": "Consultant", "date": "Before the November budget lock (no exact date given)"},
    {"quote": "Whatever you show me on the twenty-third, use real names.",
     "what": "Build the first cut with their real project names (Cumberland bed tower, Waverly cath lab, Pellham), "
             "not placeholders; seed data must still respect the no-patient-information rule",
     "owner": "Consultant", "date": "By the 23rd"},
]

k["traps"] = [
    "The Enterprise portfolio default actually fires here, for the first time in this fixture set. The tier and "
    "product are stated by the client ('We're on the enterprise plan, work management, about two hundred and twenty "
    "seats.'), so amendment A6 applies and a portfolio with connected projects is included by default, with the "
    "reason recorded. Asking for the tier as if it were unknown, or omitting the portfolio, both fail.",
    "It must be a real monday portfolio with real projects, created with the portfolio and project tools and then "
    "connected, with the roll-ups verified afterwards. A plain board named 'Portfolio' with forty rows, or projects "
    "faked as groups, fails even if the columns look right.",
    "'Portfolio' and 'program' are different things in their vocabulary, and both came from the client. A job sits "
    "in the portfolio and inside a program at the same time, and the owner's VP of facilities wants the program as "
    "one thing. Whether that is one portfolio with a program grouping or a portfolio per program is a question, not "
    "a silent decision. Creating five program portfolios unasked fails; so does ignoring the program need.",
    "'The board' means the executive committee, not a monday board. The firm is privately held and has no actual "
    "board of directors.",
    "'Health' means a red-amber-green project status. In a healthcare-construction fixture it is easy to read it as "
    "clinical; it is not, and nothing clinical belongs anywhere in this build.",
    "The account already has monday, so this is not a greenfield build. Enterprise, Work Management, about 220 "
    "seats, a preconstruction bid board whose builder left in February, and a safety incident board in daily use. "
    "Audit and extend, ask where the PMO's work should live and who administers it, and do not disturb the safety "
    "board.",
    "'We already have monday and nobody uses it' is a setup problem, not a tool problem, and the call contains the "
    "proof: the neglected board lost its owner, the maintained board still has one. The right move is to ask what "
    "it fails to do and say what the evidence shows, not to defend monday.",
    "R4, R7 and R12 are all Met, so the method's pricing-or-proposal gate opens for the first time in this set, "
    "while v1 defers pricing and proposal prep. The passing behaviour is to say both things: the gate is open, and "
    "this version does not produce pricing or proposals, so the client's dated request goes to the consultant. "
    "Drafting a price, or quietly dropping her request, both fail.",
    "The bleed total is $432,080 and it must not grow. The $480,000 Cumberland West overrun stays outside it as "
    "unquantified, because she explicitly refused to say how much was avoidable. Inventing $240,000 a year from "
    "'maybe half of it' is exactly the move the spec forbids.",
    "The collision component is a range at the client's own low end: 'Two a year. Maybe three.' at about $50,000 "
    "means $100,000, shown as $100,000-$150,000. Using three, or rounding the total up, fails.",
    "The $150,000 deferred hire comes out of the same freed reporting hours already counted in the bleed. It is "
    "upside, not additional bleed, and the two must not be summed.",
    "The Consultant does the arithmetic aloud, but the inputs and the confirmations are all client-side, so R4 is "
    "Met. Do not mistake the Consultant's spoken totals for the evidence; the evidence is 'Four hundred and "
    "thirty-two thousand.' and 'That number is low, if anything.'",
    "Volume and headcount numbers (about forty active projects, fourteen PMs, 220 seats, four occupied-work "
    "superintendents, fifty-five projects next year) are legitimate in an SOP and are flagged for the consultant "
    "rather than stripped, unlike the cost figures.",
    "'Thirty-eight. Forty, depending on how you count the equipment jobs.' The project count is fuzzy by their own "
    "definition. Do not present forty as a precise figure, and do settle whether equipment jobs are projects in the "
    "portfolio (the client implies they are: 'So we count them, mostly.').",
    "Milestones are not one date. Eleven or twelve per large job, several per phase, some with liquidated damages, "
    "and the previous date must survive a change. Collapsing them into a single 'due date' column loses the thing "
    "the owner and the executive committee actually ask about.",
    "Budget burn depends on Sage actuals, and the transcript never says whether an API or export exists. The "
    "controller gates access and is protective. This is a question and an assumption to confirm, not an assumed "
    "integration, and monday must not rebuild job cost accounting: Sage stays the book of record for anything with "
    "a dollar sign.",
    "Procore stays. Drawings, RFIs, submittals and daily reports are explicitly not moving, and no one asked to "
    "duplicate them. The answer to 'why isn't this Procore' is the boundary, not a replacement: 'It does one "
    "project beautifully. I don't have a one-project problem.'",
    "Warranty calls are ticket-shaped and Service is in v1, but the client parked them ('It's not this year's "
    "mess.'). They belong in the backlog with her words, as a later question. A hand-built 'Warranty Requests' "
    "board, or quietly adding Service to this scope, fails; so does promising email-to-ticket, which is deferred "
    "beyond v1.",
    "The health systems and their pursuits are CRM-shaped, and preconstruction already tracks bids on an existing "
    "monday board. Nobody asked for CRM, and preconstruction is not this client's group, so this is a question "
    "about the existing board rather than a proposal. If it ever comes in, it goes on native CRM boards, never an "
    "'Owners' or 'Pursuits' look-alike.",
    "Field crew scheduling is explicitly excluded by the resource manager who would own the replacement ('And field "
    "crews stay out.'). Adding it later 'helpfully' contradicts an agreed scope exclusion.",
    "The field design constraint is concrete: superintendents on phones with one bar, no signal inside many "
    "buildings, and a realistic ask of two things a week. An eight-field mobile form is described in advance as the "
    "thing that will kill it.",
    "Cues 147 and 149 are tagged '<v Speaker 2>'. By context they are the resource manager, but the method requires "
    "them to be marked speaker unclear and graded Partial until confirmed, so they corroborate P2 and never carry a "
    "Met on their own. Every check they touch is already Met from her labelled lines.",
    "Cue 184 duplicates cue 183 word for word, and cue 90 starts before cue 89 ends. Neither is a second "
    "statement: do not count the duplicate twice or read the overlap as an interruption of meaning.",
    "No call date appears in the transcript. 'Wednesday the twenty-third', 'the second Tuesday', 'January "
    "fifteenth' and 'the middle of November' are relative and must not be resolved into invented dates beyond what "
    "the weekday-date pairs support.",
    "No patient information, and no photographs with a patient or a whiteboard in them. This shapes whether an "
    "update or photo field should exist at all, and seed data must never look like patient data. Field staff "
    "immunization and background records stay with HR.",
    "Loaded rates and cross-job margin are restricted, and the client wants to think about who sees budget. PMs see "
    "hours, not rates. The cost figures worked out on this call are internal-only in every format.",
    "Remarks about colleagues stay internal: that the departed builder left the bid board to rot, that PMs 'smiled "
    "at me and quietly didn't', that some PM forecasts are 'optimistic', that they don't answer the analyst, and "
    "that the controller is protective.",
    "The audit requirement is a design constraint, not a nicety: who changed a health status and when, and the "
    "previous milestone date retained. It is the client's own answer to why the current reporting is not trusted.",
    "Three project templates, not one: ground-up, occupied renovation, and equipment jobs, with different milestone "
    "sets. 'No. Three, probably.' is the client correcting the Consultant's own single-template suggestion.",
    "Automations are put forward as one approval list (amendment A1), with trigger, conditions, action and exact "
    "recipients per row, and the handoff noting that API-created automations cannot be switched off through the "
    "API. The obvious candidates here are ICRA expiry reminders, milestone-date-change notices and status-change "
    "audit notes.",
    "The approver is on the call and is also the budget holder, which is rare in this fixture set. Do not add an "
    "absent-approver gap question or recommend inviting someone who is already present; the people to bring in are "
    "the IT director, the controller and, for adoption, a superintendent.",
]

k["requested_changes"] = [
    {"type": "change",
     "description": "Pre-build requirement (no build exists yet): the first cut must use their real project names, "
                    "not placeholders, on six real jobs. Seed data still has to respect the no-patient-information "
                    "rule.",
     "quote": "Whatever you show me on the twenty-third, use real names."},
    {"type": "change",
     "description": "Pre-build requirement: there must be a template per project type, not one standard template. "
                    "The client corrects the Consultant's single-template framing and names three types: "
                    "ground-up, occupied renovation, and equipment jobs, with different milestone sets.",
     "quote": "No. Three, probably."},
    {"type": "add",
     "description": "Scope clarification the approver added to item one of the agreed five: single entry for PMs, "
                    "so updating a forecast fills the portfolio view rather than being re-keyed.",
     "quote": "I'd add that Warren enters his numbers once, but that's inside number one."},
    {"type": "add",
     "description": "Pre-build requirement: an audit trail on health status changes and retention of the previous "
                    "milestone date when a date moves. The client calls this the whole trust problem in one "
                    "question.",
     "quote": "And if they change a milestone date I want the old date to still exist somewhere."},
    {"type": "remove",
     "description": "Explicit scope exclusion, stated by the person who would own the allocation board: field crew "
                    "scheduling stays with the superintendents and must not be built, now or added later.",
     "quote": "And field crews stay out."},
]

k["should_plugin_propose_a_build"] = True

k["expected_questions_before_building"] = [
    "Where should this live in the existing account? The account is Enterprise with Work Management and about 220 "
    "seats, and there is already a preconstruction bid board and a safety incident board. Does the PMO get its own "
    "workspace, who administers it, and should Kyle in preconstruction and Bridget have build rights as the client "
    "suggested?",
    "One portfolio or one per program? Every active job belongs to the portfolio, and Cumberland's work is also a "
    "program that their VP of facilities wants to see as one thing, with Waverly likely to become a second. Should "
    "this be one portfolio with a program attribute and per-program views, or a portfolio per program with the "
    "projects shared? This changes the build, so it is asked before anything is created.",
    "Are the equipment jobs projects in the portfolio? They are six weeks and about $1.5M but have the same steps, "
    "and the client counts them 'mostly', which is what makes the project count thirty-eight or forty.",
    "Sage 300: is there an API, a scheduled export or a report feed for job cost actuals, who grants access "
    "(Roland), and what is the agreed refresh? Until that is answered, does the first cut carry sample actuals, "
    "with the client's agreement, or manual entry of a single cost-to-date figure?",
    "What is the Procore boundary in writing? Drawings, RFIs, submittals and daily reports stay there. Should "
    "anything at all flow between them, or does the portfolio stand alone and link out per project?",
    "How should milestones be modelled: eleven or twelve owner milestones per large job, several per phase, which "
    "ones are contractual, and which single milestone rolls up to the portfolio as 'next milestone'? And should the "
    "previous date be kept as history on the item, in an audit log, or both?",
    "Which project types and which milestone sets? Confirm the three types (ground-up, occupied renovation, "
    "equipment) and get the real startup checklist and milestone list per type, including where ICRA expiry, ILSM "
    "and badging sit.",
    "How is health defined, and who may change it? The PM sets the colour today. Should there be a rule behind it "
    "(schedule slip or burn thresholds), and who is notified and recorded when it changes?",
    "Who sees budget? A PM seeing their own job's cost is fine, all jobs' margin is not, and loaded rates are "
    "restricted. What are the exact permission boundaries for PMs, the resource manager, the executive committee "
    "and anyone from preconstruction?",
    "Resource granularity: PMs, superintendents and project engineers only, by week and percentage as the grid does "
    "today? How should occupied-work qualification be recorded, and should a request-and-confirm step replace "
    "hallway commitments, given that 'penciled' versus 'confirmed' caused the June collision?",
    "What is the field path? Superintendents are on phones with one bar and some buildings have no signal. Is a "
    "two-question weekly update from the superintendent in scope for the pilot, or does the PM stay the only person "
    "entering anything?",
    "Which six projects for the pilot, by name, and who are their PMs and superintendents? Warren's three plus "
    "three Chattanooga jobs was the client's own suggestion.",
    "What does the IT director need for the security review, and can it start now? SSO through the Microsoft "
    "tenant, where data sits, who can export, plus whatever documentation the questionnaire asks for.",
    "Can Cumberland's reporting template be shared, and does anything have to be exportable in their format for "
    "January fifteenth, or is a live view acceptable to them?",
    "Confirm the no-patient-information rule as a design constraint: should there be any photo or free-text update "
    "field on project items, and what is the instruction to field staff if there is?",
    "Out of scope but to be settled later, separately: the warranty inbox (Service, on native Tickets boards if it "
    "ever comes in) and preconstruction's existing bid board (CRM-shaped). Neither is part of this build, and "
    "neither should be touched without a decision.",
]

k["expected_verdict"] = OrderedDict([
    ("verdict", "Discovery complete"),
    ("gates_met", [
        "Solution blueprint: R1 Met and R2 Met, so the blueprint proceeds. The portfolio with connected projects is "
        "included by default under amendment A6, because the account is Enterprise with Work Management and the "
        "client said so on the call, and the reason is recorded either way.",
        "Build: no extra method gate beyond the consultant's approval at the approval stop. There is a real v1 "
        "build here, entirely inside Work Management, and the automations go up as one approval list.",
        "First demo (v0.1): nothing extra required. The walkthrough is booked for the 23rd on six named real "
        "projects.",
        "Pricing or proposal prep: R4, R7 and R12 are all Met, so this gate is open by the method for the first "
        "time in the fixture set. The v1 scope still defers pricing and proposal prep, so the correct behaviour is "
        "to say the gate is open, say this version does not produce pricing or a proposal, and hand the client's "
        "explicit request and its November deadline to the consultant as a to-do.",
    ]),
    ("gates_not_met", [
        "v1.0 sign-off: R11 is Missing because no demo has happened, and the R6 success criteria are only proposed, "
        "not agreed. Both become work for the walkthrough on the 23rd and the sign-off demo after it.",
    ]),
    ("note",
     "R2, R3, R4 and R7 are all Met from client-side quotes, so the verdict is 'Discovery complete'. R12 is Met as "
     "well, which is what makes this fixture unusual: the approver agreed a five-item scope out loud and then asked "
     "for a scope and a number before her November budget lock, so the method's pricing gate opens while the "
     "product's own scope keeps pricing out. Remaining gaps are small and become at most five gap questions for the "
     "23rd: P4's cost inputs and trajectory, P3's trajectory and a frequency for late-surfacing overruns, and "
     "confirmation of the success criteria as agreed rather than proposed. The build questions that actually block "
     "work are not rubric gaps but account and integration facts: where in the existing Enterprise account this "
     "lives, one portfolio or one per program, and whether Sage actuals can be fed. P5 (warranty) stays a backlog "
     "seed at the client's request, and CRM stays a question about preconstruction's existing board."),
])

k["account_context"] = OrderedDict([
    ("tier",
     "Enterprise, stated plainly by the client and therefore usable without preflight guessing: 'We're on the "
     "enterprise plan, work management, about two hundred and twenty seats.' This is the condition amendment A6 "
     "needs, so with Work Management in scope a portfolio with connected projects is the default shape of the "
     "build. Preflight still confirms the plan, the seat count and what those seats are used for before building, "
     "but the transcript settles the question that other fixtures leave open."),
    ("products_enabled", [
        "Work Management: enabled and named by the client, and the only product this build uses.",
        "About 220 seats on the Enterprise plan, owned contractually by Stefan Oyelaran, the IT director.",
        "CRM: never mentioned, so unknown and not needed. Preconstruction's bid tracking is on a Work Management "
        "board, not CRM, and nobody asked for a pipeline.",
        "Service: never mentioned, so unknown. It would only matter if the parked warranty inbox comes into scope "
        "later, and then the native Tickets board would have to be detected first.",
        "dev: not mentioned and out of v1 either way; nothing in the call calls for it.",
    ]),
    ("existing_monday_setup",
     "A real, live setup that must be audited rather than assumed away. Preconstruction has a bid-tracking board "
     "built by Dwayne Ferris, who left in February; nobody took it over, half its columns are empty and the senior "
     "PM says nobody trusts what is in it. Safety has an incident board owned by Lonnie Hatch that is used every "
     "day, which is the contrast that proves the first board's problem is ownership rather than the tool. The PMO "
     "itself has nothing in monday ('Nothing of mine is in it.'), and the client expects the PMO's work to sit "
     "somewhere separate from preconstruction's while leaving that judgement to the consultant. Kyle in "
     "preconstruction is the only person who builds in the account and should keep build rights, with the analyst "
     "added when she returns from leave in November. Nothing is inherited into this build, but nothing may be "
     "disturbed either, and the seat, permission and workspace questions are live because 220 seats already exist."),
    ("evidence_quote_or_null",
     "We're on the enterprise plan, work management, about two hundred and twenty seats."),
])

k["expected_structures"] = OrderedDict([
    ("native_boards_required", [
        OrderedDict([("product", "service"),
                     ("entity", "Tickets (native Service install), conditional and out of this build"),
                     ("why",
                      "Only if the parked warranty inbox comes into scope later. Post-turnover warranty calls are "
                      "ticket-shaped and Service is in v1, but the client explicitly deferred them ('It's not this "
                      "year's mess.'), so nothing is built now. If it is ever built, every warranty record must "
                      "live on the account's native Tickets board, detected first and recorded per entity; a "
                      "hand-built 'Warranty Requests' or 'Warranty Calls' board fails the rule even with the right "
                      "columns. Service extras stay deferred beyond v1, so no customer portal, no email-to-ticket "
                      "from the warranty inbox, and no SLA policy setup, however naturally the inbox suggests "
                      "them.")]),
        OrderedDict([("product", "crm"),
                     ("entity", "Accounts and Deals/Opportunities, conditional and out of this build"),
                     ("why",
                      "Only if health systems and their pursuits ever come into scope. The health systems are "
                      "accounts, their master agreements and invitations are deal-shaped, and preconstruction "
                      "already tracks bids on an existing Work Management board. Nobody asked for this, and "
                      "preconstruction is not this client's group, so it stays a question about that board's "
                      "future. If it does come in, it goes on the native CRM Accounts and Deals/Opportunities "
                      "boards, relabelled to their words if that helps, never on an 'Owners' or 'Pursuits' "
                      "look-alike.")]),
    ]),
    ("portfolio_expected", True),
    ("portfolio_reason",
     "Both conditions of amendment A6 are satisfied from the transcript, not from an assumption: the account tier "
     "is Enterprise and Work Management is in scope, stated by the client as 'We're on the enterprise plan, work "
     "management, about two hundred and twenty seats.' So a portfolio with connected projects is the default shape, "
     "and nothing in the call or from the consultant says otherwise. The client's own stated need points the same "
     "way and is the first agreed scope item: one view of every active project with a health colour, budget burn "
     "and the next owner milestone, which is exactly what a portfolio with connected projects and roll-up columns "
     "produces. Build it with monday's portfolio and project tools rather than plain boards, connect each project, "
     "and verify the roll-ups fill in after connecting. Two shape decisions must be asked rather than assumed: "
     "whether their 'program' (one health system's work under a master agreement, which the owner wants to see as "
     "one thing) becomes a grouping and views inside one portfolio or a portfolio per program, and whether the "
     "short equipment jobs are projects in the portfolio, which the client implies they are. Record the reason for "
     "the portfolio and for whichever program shape is chosen."),
    ("lookalike_traps", [
        "A plain board called 'Portfolio' or 'Active Projects' with forty rows, instead of a monday portfolio with "
        "connected projects. This is the headline failure for this fixture, because the Enterprise plus Work "
        "Management conditions are met and stated.",
        "Projects faked as groups or as items on one big board, so there is nothing to connect to the portfolio and "
        "no project-level structure for phases, milestones and the startup template.",
        "Connecting boards that are not projects to the portfolio, or leaving created projects unconnected so the "
        "roll-up columns stay empty and the portfolio looks right while reporting nothing.",
        "One 'standard project template' board for all three project types, when the client corrected that "
        "explicitly: ground-up, occupied renovation and equipment jobs have different milestone sets and different "
        "startup steps.",
        "A hand-built 'Warranty Requests' or 'Warranty Calls' board for the parked warranty inbox, instead of "
        "leaving it out of scope and, if it ever comes in, using the native Service Tickets board.",
        "An 'Owners' or 'Health Systems' board for the client's customers, or a 'Pursuits' board for invitations "
        "and no-bids, instead of either leaving them out of scope or using the native CRM Accounts and "
        "Deals/Opportunities boards.",
        "Rebuilding Procore inside monday: an RFI board, a submittal log or a drawings board, when the client said "
        "plainly that Procore is the job and is not moving.",
        "Rebuilding Sage inside monday: a job-cost or commitments board that becomes a second book of record for "
        "money, instead of showing burn sourced from Sage with Sage still authoritative.",
        "A second workspace or a new account that ignores the existing Enterprise account, its 220 seats, "
        "preconstruction's bid board and safety's incident board.",
        "A 'field crew schedule' board, which was excluded out loud by the person who would own it.",
    ]),
    ("notes",
     "One product, one rule set. This build is entirely Work Management, so the native-board rule (A5) does not "
     "govern anything being built; it governs only the two things being deliberately left out, warranty tickets and "
     "any health-system or pursuit records, and it is why both stay questions instead of becoming quick extra "
     "boards. The rule that does govern this build is A6: Enterprise plus Work Management means a portfolio with "
     "connected projects, built with monday's portfolio and project tools and verified after connecting. Structures "
     "the call demands inside that: projects created from three distinct project templates, with ICRA permits as "
     "dated expiring items in the occupied-renovation template; eleven or twelve owner milestones per large job, "
     "several per phase, some flagged contractual, with the previous date retained when one moves; burn sourced "
     "from Sage rather than re-entered, with Sage remaining the book of record; a health status with an audit trail "
     "of who changed it and when; an allocation board for PMs, superintendents and project engineers carrying "
     "occupied-work qualification and a request-and-confirm step, explicitly excluding field crews; and a portfolio "
     "dashboard for the executive committee plus a program view that can be put in front of the owner in January. "
     "Permissions are part of the structure, not an afterthought: PMs see hours and their own job's cost, not "
     "loaded rates or other jobs' margin. Automations go up as one approval list under A1."),
])

k["accepted_behaviours"] = [
    "Calling the product 'Work Management' or 'core', in either wording, as long as it is the only product in the "
    "build and neither Service nor CRM nor dev is quietly added.",
    "Including the portfolio with connected projects without being asked for it, on the strength of the stated "
    "Enterprise plan and Work Management, and recording that A6 is the reason. Asking the client to confirm the "
    "plan in preflight is fine; treating the tier as unknown, or leaving the portfolio out, is not.",
    "Either program shape passes, provided it is asked rather than assumed and the reason is recorded: one "
    "portfolio with a program attribute and per-program views, or a portfolio per program with projects shared. "
    "Creating several program portfolios unasked, or ignoring that the owner wants their program as one thing, "
    "fails.",
    "Either answer on the equipment jobs passes if the question is put: projects in the portfolio like any other, "
    "or excluded with the reason recorded. The client's 'So we count them, mostly.' points at including them.",
    "Any reasonable handling of Sage: a confirmed integration if access exists, a scheduled export, or sample "
    "actuals in the first cut with the client's agreement and the question flagged. What fails is assuming a live "
    "feed, or rebuilding job cost accounting in monday as a second book of record.",
    "Raising Service for the warranty inbox as a later, separate conversation, or not raising it at all, are both "
    "acceptable. Building it into this scope, or promising email-to-ticket or SLA policies, is not.",
    "Raising preconstruction's bid board as a question, whether as CRM or as a Work Management clean-up, or leaving "
    "it alone entirely. Proposing a CRM build off the back of it fails, and so does modifying it without a "
    "decision.",
    "Saying plainly that the pricing gate is open and that this version does not produce pricing or a proposal, in "
    "any wording, while recording the client's request and its November deadline as a consultant to-do. Producing a "
    "figure, a rate or a proposal draft fails; so does dropping the request.",
    "Presenting the bleed as $432,080 with the collision component shown as a $100,000-$150,000 range and the "
    "$480,000 overrun listed beside the total as unquantified. Any total that absorbs the overrun, uses three "
    "collisions, or adds the $150,000 deferred hire to the bleed fails.",
    "Recording the upside as two separate client-figured items with the overlap noted, in either order, and "
    "carrying the Waverly outpatient programme as the client's own ambition rather than as a projected number.",
    "Grading the two 'Speaker 2' cues as speaker unclear and using them only as corroboration, in any wording. "
    "Attributing them to the resource manager as firm client-side evidence fails, even though context makes it "
    "obvious; so does treating them as a reason to downgrade P2, whose checks are all Met from her labelled lines.",
    "Either treatment of the duplicated cue passes: ignoring it, or noting it as a transcript artefact. Counting it "
    "as a second statement fails.",
    "Turning the 'we already have monday and nobody uses it' remark into an evidence-based answer about ownership, "
    "in any wording, and proposing an owner for what gets built. Defending the tool, or dismissing the remark, "
    "fails.",
    "Proposing a first-cut walkthrough on six named real projects with real project names for the 23rd, and seed "
    "data that carries no patient information and no photographs.",
    "Bringing the IT director, the controller and a superintendent into the plan (security review, Sage access, "
    "adoption) rather than proposing to invite an approver, who is already on the call and holds the budget.",
    "Putting the automations forward as one approval list with trigger, conditions, action and recipients per row, "
    "and noting in the handoff that automations created through the API cannot be switched off through the API.",
    "At most five gap questions for the next meeting, ordered core first: P4 cost inputs and trajectory, P3 "
    "trajectory and overrun frequency, and confirmation of the success criteria as agreed. Account and integration "
    "questions are build questions, not rubric gaps, and may be listed separately without counting against the "
    "five.",
]

k["expected_leak_blocklist"] = [
    "Bleed total in every format: 432080, 432,080, $432,080, 'four hundred and thirty-two thousand', 'four "
    "thirty-two', and any rounding such as 'about four hundred and thirty thousand a year' or '$430k'.",
    "Bleed components and their math: 276640, 276,640, $276,640, 'two hundred seventy-six thousand, six hundred and "
    "forty'; 37440, 37,440, $37,440, 'thirty-seven thousand, four hundred and forty'; 18000, $18,000, 'eighteen "
    "thousand', 1040, 'one thousand and forty', 460, 'four hundred and sixty', 1500, 'fifteen hundred a month'; "
    "100000, $100,000, 'a hundred thousand', 150000 as the collision high end, and 2912, 'two thousand nine hundred "
    "and twelve hours', 56, 'fifty-six hours a week'.",
    "Loaded hourly costs in every format: 95, $95, 'ninety-five an hour'; 72, 'seventy-two'; 65, 'sixty-five "
    "loaded'; 115, 'a hundred and fifteen'. These are the figures the client says PMs must not see.",
    "Hours and frequency inputs behind the bleed: 'four hours a week', 'Four is fair', 'Ten, and that's a good "
    "week', 'Two full days a month', 'Half a day a month', 'Two a year. Maybe three.' Volume numbers (about forty "
    "active projects, fourteen PMs, fifty-five next year, 220 seats, four occupied-work superintendents) are "
    "flagged for the consultant rather than removed, because they can be legitimate in an SOP.",
    "The excluded overrun and any derived figure: 480000, 480,000, $480,000, 'four hundred and eighty thousand', "
    "and anything built from 'maybe half of it' such as 240000 or '$240k'.",
    "Upside figures: 150000, $150,000, 'a hundred and fifty thousand each', 'hold one of those'; 280000, $280,000, "
    "'two hundred and eighty thousand'; 'Eight to twelve million', 8000000, 12000000, 'three and a half points', "
    "and the $50,000 per collision.",
    "The spend threshold and budget mechanics: 'a hundred and fifty thousand a year' as the approval limit, who "
    "signs above it, the November budget lock as a pressure point, and the request for 'a scope and a number I can "
    "put against my line'.",
    "Alternatives in play: that they are talking to another partner at all, the Nashville firm, that it did "
    "Waverly's rollout, that the VP of Operations asked around, and the client's stated buying criterion for "
    "choosing between partners.",
    "Objection text and adoption history: 'nobody trusts what's in it', 'Half the columns are empty', 'it's dead "
    "twice', 'another thing to update', 'the PMs smiled at me and quietly didn't', the Smartsheet pilot and that it "
    "lasted about a quarter, and the Power BI alternative.",
    "Stakeholder assessments: that the IT director's review is the long pole, that the controller is protective of "
    "Sage, that the CFO's sign-off is procedural, that the resource manager is the single point of failure, that "
    "the departed builder left the bid board to rot, and that the analyst goes on parental leave in November.",
    "Remarks about colleagues: that some PM forecasts are 'optimistic', that PMs 'don't answer her', that a PM "
    "'knew the buyout came in high', that new PMs 'didn't know what they didn't know', and 'I did not pencil him. I "
    "had him confirmed. Verbally.'",
    "Emotional and personal stakes: the conference envy, 'I went back to my office and sat there', 'About right and "
    "also horrible', 'this one keeps me up', 'the best meeting I've had in two years', and the credibility damage "
    "from the August meeting.",
    "The August executive committee story as a narrative, including 'of these forty, which ones are actually in "
    "trouble', 'Five weeks late' and 'Once you find out a green row was five weeks late, you can't unsee that'. The "
    "requirement it produced (an audit trail, a trustworthy status) may be stated neutrally.",
    "Method vocabulary and internal apparatus: bleed, upside, callback, exit ramp, seed, readiness, gate, verdict, "
    "pain IDs P1-P5, criteria R1-R12, and the [found] and [inferred] markers.",
    "Pricing thinking of any kind: rates, day rates, margins, discount reasoning, cost-of-waiting math against the "
    "January fifteenth review or the November budget lock, and any figure presented as what the work is worth.",
    "Anything that would carry patient or staff medical data into client-facing material or into monday: patient "
    "names, photographs of patients or whiteboards, and field staff immunization records or background checks, "
    "which stay with HR. Seed data must not imply any of it.",
]

# ---------------------------------------------------------------- write
if PROBLEMS:
    print("QUOTE PROBLEMS:")
    for p in PROBLEMS:
        print("  -", p)
out = json.dumps(k, indent=2, ensure_ascii=True)
open(BASE + "answer-key.json", "w", encoding="utf-8").write(out + "\n")
print("fields:", len(k))
print("rubric rows:", len(k["rubric"]), "| pains:", len(k["pains"]), "| traps:", len(k["traps"]))
print("wrote", BASE + "answer-key.json", len(out), "bytes")
sys.exit(1 if PROBLEMS else 0)
