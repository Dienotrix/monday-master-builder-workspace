"""Build fixtures/s20-large-group/answer-key.json from locations.json (written by build.py).

Every quote is pulled through Q(tag, text), which asserts the text is a verbatim substring of the
tagged transcript line and returns the s1-style location "HH:MM:SS Speaker Name (role)".
Authoring scratch; read-only against the transcript.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "fixtures", "s20-large-group", "answer-key.json")
LOCS = json.load(open(os.path.join(HERE, "locations.json")))


def Q(tag, text):
    rec = LOCS[tag]
    assert text in rec["text"], "quote not verbatim at %s: %r" % (tag, text)
    return {"quote": text, "location": rec["location"]}


def L(tag):
    return LOCS[tag]["location"]


def T(tag):
    return LOCS[tag]["location"].split(" ")[0]


def row(criterion, status, asked, evidence, note, asked_quote=None):
    r = {"criterion": criterion, "status": status, "asked": asked}
    r["asked_quote"] = asked_quote
    r["evidence"] = evidence
    r["note"] = note
    return r


CONS = "Consultant"
D = "Delphine Castellane (Operations Director)"

key = {}
key["scenario_id"] = "s20-large-group"
key["call_type"] = "discovery"
key["purpose_of_this_fixture"] = (
    "Calibration fixture for the large-group case (REAL-CALL-LESSONS.md C63; BUILD-PLAN.md 4.2 row s20; headless runs H46, H52, H53). "
    "A fourteen-name discovery call with a sign manufacturer: thirteen client attendees listed in the export header, nine of whom speak and four of whom never do, "
    "including the managing director who signs anything over the operations budget threshold and is never addressed by our side. It plants one cross-speaker conflict "
    "(the sales manager says one job in ten is remade, the production manager says closer to one in four, and the room agrees it has never been measured), one self-contradicting "
    "turn (the convener says the existing monday account is on Pro, then corrects herself to Standard inside the same turn), and three mid-call departures that exist only in speech: "
    "the finance controller announces hers, the sales manager's is reported by a colleague, and an account manager leaves with him; a fourth person simply stops speaking and a colleague "
    "guesses he may have gone, which is not a departure record. The key asserts the repair: voices heard and voices missing built from the roster; the silent decision-shaped attendee "
    "promoted to a named risk row recording that our side never addressed him; talk share by side with the loudest and quietest client speaker; the conflict kept as both statements, "
    "marked unresolved, raised as a gap question naming the remake log, and never resolved in favour of the later speaker (reversal R6); the tier correction logged as superseded because "
    "and only because it is the same speaker, the same proposition and the same turn; a budget line and an actual write-off from one speaker kept as two items with no arithmetic between them; "
    "a trajectory question graded not obtainable from this room because the role that could answer it had already left; the approver's priorities and his nod, both relayed by the convener, "
    "never attributed to him; and a prep sheet that ranks the silent attendees by stake. Grading otherwise follows the method: four excavated pains, a client-built bleed that excludes the "
    "contested remake labour, R1 and R7 met-with-residual, R12 Partial because the approver's assent is relayed, verdict Discovery complete with the pricing gate shut, and a build proposed in "
    "Work Management only, with quoting left in the estimating tool and the job number left with the accounting system. should_plugin_propose_a_build is true."
)
key["transcript_format"] = (
    "Plain text export from a video meeting. Two header lines (a meeting title and 'Participants (14): ...', display names only, no roles, no date), a blank line, then 256 speaker turns, "
    "one per line, in the form '[HH:MM:SS] Speaker Name: text'. Timestamps are turn start times from [00:00:03] to [00:48:51]; there are no end times and no join or leave events, so every "
    "presence change is inferable only from speech. The participant header lists thirteen client names and 'Consultant'; ten labels speak (nine client, plus the Consultant) and four listed "
    "names never do. About 5,830 spoken words. Client talk share is about 71.9 percent by words (Delphine Castellane 25.4 percent of all words, Rosalind Achebe 12.3, Henrike Solano 8.0, "
    "Bronwyn Tsai 6.6, Calum Fairweather 4.4, Fergus Lindqvist 4.2, Emeric Sandoval 4.1, Kwame Oduya 3.8, Yolanda Brekke 3.1); the Consultant has 28.1 percent and the longest unbroken "
    "Consultant stretch is 179 words at [00:44:24], under the 225-word proxy. Artefacts: '[inaudible]' inside two lines (00:07:44, 00:12:08), a '[crosstalk]' pair at 00:27:56 and 00:28:03, "
    "'[laughs]' twice, an ellipsis in one arithmetic line and ' -- ' in one crosstalk line. ASCII only. The call date is not stated; the weekday-date pair 'Wednesday the twenty-first' and "
    "the rollout starting 'the week of February ninth' fit a call on a Tuesday in early October 2026 with the walkthrough on Wednesday 21 October. Every location in this key is "
    "'HH:MM:SS Speaker Name (role)' taken from the line the quote is on, with 'HH:MM:SS Consultant' for our side; header lines are never cited."
)
key["company"] = {
    "name": "Ostlerby Signs",
    "industry": "Sign manufacturer and installer: wayfinding packages, exterior fascia signs and counter sets for hospitals, universities, hotels and retail rollouts. Design, print, CNC routing, fabrication, paint and installation are all in-house.",
    "size": "About 95 people. Six customer-service coordinators including their lead, five designers, a production floor with two leads, six two-person install crews (five at the main plant, one at the branch), sales (a sales manager and account managers), finance and an outsourced IT provider. Live jobs 'more like two hundred and something' (Rosalind), 'Two-forty was the number I had in August. It's gone up.' (Delphine); 110-115 on the production floor board.",
    "locations": "Main plant in Saginaw, Michigan; a twelve-person branch with its own install crew in Flint. Installs across the region (a wasted trip to Traverse City is the P3 instance); the pharmacy rollout covers 140 stores in five states.",
    "current_tools": [
        "An estimating tool for quotes (Fergus's team; the client says it works and must stay)",
        "The job sheet: one spreadsheet, one row per job, about forty columns, on the shared drive; the branch keeps its own separate copy ('the Flint sheet')",
        "Email for the sales-to-coordinator handover, customer proof approvals ('that email is the record') and change orders",
        "A design tool in the studio; proofs are files named by version",
        "The floor board: a twelve-foot physical whiteboard with printed job tickets in sleeves, moved by hand through print, cut, fab, paint, assembly, ready",
        "A paper remake log by the router; paper survey forms and phone photos",
        "An accounting system that issues the job number and raises invoices; frozen to any connection until November because of an audit",
        "A spreadsheet for install crew scheduling, a week at a time",
        "monday: one existing account used only by marketing for a content calendar, 25 seats, stated as Standard after a same-turn correction from Pro; who set it up is unknown",
    ],
}
key["attendees"] = [
    {"name": "Consultant", "role": "monday.com consultant running the discovery call", "side": "consultant", "decision_role": "not applicable"},
    {"name": "Delphine Castellane", "role": "Operations Director; convener; owns operations systems and signs up to $20,000 a year; loudest client voice; relays the managing director's views and his nod", "side": "client", "decision_role": "approver (up to $20,000; above that the managing director signs) and admin/owner of the rollout"},
    {"name": "Gideon Ashworth-Pell", "role": "Managing Director; 'here to listen' per the convener; signs anything over $20,000; NEVER SPOKE and was never addressed by our side; presence after the roster is claimed by the header only", "side": "client", "decision_role": "approver (by role, relayed by the convener; unheard; named risk row)"},
    {"name": "Bronwyn Tsai", "role": "Finance Controller; issues job numbers and invoices; supplied the loaded rates and the remake write-off; announced a hard stop and left at 00:31:20", "side": "client", "decision_role": "influencer (raises the purchase order after a yes; owns the audit freeze on the accounting system)"},
    {"name": "Fergus Lindqvist", "role": "Sales Manager; quotes in the estimating tool; states the one-in-ten remake rate; departure reported by the convener at 00:38:15", "side": "client", "decision_role": "influencer"},
    {"name": "Rosalind Achebe", "role": "Production Manager; runs the floor board and the paper remake log; states the one-in-four remake rate; second loudest client voice", "side": "client", "decision_role": "influencer and end user (owner of the floor's screen-on-the-wall requirement)"},
    {"name": "Emeric Sandoval", "role": "Design Studio Lead, five designers; proofs and approval versions; last spoke at 00:17:17 with no stated departure (a colleague's later guess that he 'may have dropped' is not a record of one)", "side": "client", "decision_role": "end user (presence after 00:17:17 unknown)"},
    {"name": "Henrike Solano", "role": "Customer Service Lead; six coordinators including her own the job from won to installed and retype the quote into the job sheet; supplied the coordinator hours", "side": "client", "decision_role": "end user and admin/owner (would roll it out with the convener)"},
    {"name": "Calum Fairweather", "role": "Install Scheduler for six two-person crews; silent until the room-wide open check-in at 00:32:19, then supplied P3 whole", "side": "client", "decision_role": "end user"},
    {"name": "Yolanda Brekke", "role": "Flint Branch Manager, twelve people and one crew; joined late at 00:07:44; keeps the branch's own copy of the job sheet", "side": "client", "decision_role": "influencer and end user (branch)"},
    {"name": "Kwame Oduya", "role": "Account Manager under the sales manager; change orders; asked the per-seat cost question our side deferred; left with the sales manager at 00:38:26", "side": "client", "decision_role": "end user"},
    {"name": "Anton Petrakis", "role": "From the client's outsourced IT provider, attending as a guest ('so nobody promises anything about passwords'); NEVER SPOKE; his firm's security checklist is promised by the convener", "side": "client", "decision_role": "influencer (access and security; unheard)"},
    {"name": "Saoirse Nakamura", "role": "HR and Training Coordinator; 'whatever we pick, the training lands on her'; NEVER SPOKE", "side": "client", "decision_role": "end user (training owner; unheard)"},
    {"name": "Lettie Havlicek", "role": "Production Administrator; prints the job tickets from the job sheet for the floor; NEVER SPOKE, and every statement about her work comes from colleagues", "side": "client", "decision_role": "end user (unheard)"},
]
key["expected_monday_products"] = [
    {"kind": "core", "why": "monday Work Management for the job from won quote to invoiced: one job board for both sites with a site column, stages in the client's words (proofing, production, ready, installed, invoiced), the approved proof and its approval held on the job with a change after sign-off visible as a change, the job ticket printed from the job so it reprints when the job changes, install scheduling for the six crews off the same jobs so a job back in paint cannot show as ready, an installed flag that reaches finance, and a weekly rollout status view the pharmacy customer's project manager asked for. Quoting stays in the estimating tool and the job number keeps coming from the accounting system (no connection before November). The account is stated as Standard, so no portfolio is proposed and plan limits are a preflight question. The floor's requirement is a screen on the wall and a printed ticket, not tablets."},
    {"kind": "not proposed", "why": "CRM is not proposed: the client said the estimating tool works and must stay ('The estimating tool stays.'), nobody asked for a pipeline, and 'quote' here is a priced document, not a deal stage. Service is not proposed: change orders and remakes look ticket-shaped but the client described them as events on a job, no queue or desk was asked for, and Service extras are deferred beyond v1 in any case. Dev is out of v1 and nothing calls for it. If CRM or Service were ever added they would land on the account's native template boards, detected first."},
]

# ---- rubric ----
R = []
R.append(row("R1 Current state mapped", "met-with-residual", True, [
    Q("fer_quote_process", "Then we build the quote in the estimating tool."),
    Q("hen_jobsheet", "The first thing we do is open the job in the job sheet. The job sheet is a spreadsheet."),
    Q("hen_retype", "We type it again, because the quote lives in the estimating tool and the floor can't see the estimating tool."),
    Q("eme_approval", "And the customer signs it off by email. That's the whole approval system."),
    Q("ros_floorboard", "The floor board is a whiteboard, twelve feet of it, columns for print, cut, fab, paint, assembly, ready."),
    Q("bro_p4_stated", "Nobody tells finance a job is on the wall."),
    Q("yol_own_sheet", "We keep our own copy of the job sheet."),
    Q("hen_hours", "Six each, and there are six of us."),
    Q("tier_turn", "Who set it up originally I genuinely couldn't tell you, it predates me."),
], "Graded element by element. Process end to end: Met (quote, handover by email, job sheet, job number, proof and approval, ticket and floor board, install, invoice, with the branch's parallel sheet). Tools and how they connect: Met (nothing connects; every step is a retype, an email or a phone call). Who touches it: Met (each role took its own part; the four silent attendees' parts are described by colleagues). Time on their own process: Met (six coordinators at six hours a week; two production leads at eight hours a week). Time maintaining a platform: not applicable, nothing is maintained. What monday does today and who built it: the first half is Met (marketing's content calendar, 25 seats, Standard after the same-turn correction) and the second half is not ('it predates me'), so the criterion is met-with-residual and the residual is a gap question routed to the convener, who took it as an action at " + T("del_admin_commit") + ". Install was deferred by our side at " + T("con_install_deferred") + " and only recovered by the open check-in at " + T("con_open_checkin") + ".",
    Q("con_walk", "Let's walk a job, then, from the first phone call to the invoice, and I'd like each of you to take your own part.")))
R.append(row("R2 Pain made concrete", "met", True, [
    Q("quarrington_concrete", "eleven of the twenty-two were the wrong size"),
    Q("eme_concrete", "We printed twenty-two arrows pointing the wrong way."),
    Q("cal_p3_concrete", "Crew drove up, hung three, drove home, drove up again the following Tuesday for one panel."),
    Q("bro_p4_concrete", "Average from install to invoice, forty-one days."),
], "Four pains are excavated (Stated, Concrete and Workaround all Met): P1 the quote retyped into the ticket and the ticket going stale, P2 the approved proof version not being the one the floor builds from, P3 crews sent to jobs that are not ready, P4 finance not told a job is installed. Each has a dated or countable instance. Ungraded themes in the pains list: change orders reaching the floor late (Kwame, figure withdrawn), the branch's duplicate sheet, the coordinators' status calls, and the weekly rollout status the customer asked for.",
    Q("con_concrete_q", "When did that last happen?")))
R.append(row("R3 Why now", "met", True, [
    Q("whynow_rollout", "The first is we won a rollout. A pharmacy chain, a hundred and forty stores"),
    Q("whynow_rollout", "First stores go in the week of February ninth and it runs through to June."),
    Q("del_quarrington_trigger", "The second thing is Quarrington."),
    Q("del_august", "August. The remake shipped the first week of September."),
], "All three client-side elements. Change: the 140-store rollout, a third again on current volume and 'a hundred and forty of nearly the same job'. Trigger: the Quarrington lobby remake in August with the customer's regional director watching the second install. Clock: first stores the week of February ninth, so the convener wants the building live in January. No date or trigger came from our side; the customer's name is withheld by the client until countersignature and must stay withheld.",
    Q("con_whynow_q", "What's made this matter this autumn rather than last year?")))
R.append(row("R4 Bleed number", "met", True, [
    Q("hen_hours", "six hours a week each on things that only exist because the quote and the ticket and the proof don't talk to each other. Six each, and there are six of us."),
    Q("bro_rates", "Thirty-eight an hour loaded, give or take. Production leads are fifty-two."),
    Q("ros_wait_hours", "Eight hours a week, easily."),
    Q("bro_writeoff", "Last year we actually wrote off, I want to say fifty-five. Fifty-five, fifty-six, on remake materials."),
    Q("del_math_coord", "Thirty-six times thirty-eight is... thirteen sixty-eight a week. Times fifty-two. Seventy-one thousand and change."),
    Q("del_math_leads", "Four-sixteen a week. Times fifty-two. Twenty-one, twenty-two thousand."),
    Q("del_bleed_total", "So seventy-one, plus twenty-two, plus fifty-five. A hundred and forty-eight thousand, near enough. A year."),
    Q("bro_bleed_confirm", "That's about right, and it's light."),
], "Client inputs, client arithmetic, client confirmation: coordinators 6 x 6 h/wk = 36 h x $38 loaded x 52 = $71,136; production leads 8 h/wk x $52 x 52 = $21,632; remake materials written off last year $55,000 (spoken hedged as 'fifty-five, fifty-six', the hedge kept); exact sum $147,768, stated as 'a hundred and forty-eight thousand, near enough' and confirmed by the controller as about right and light before she left. Excluded and listed as unquantified: remake labour (the rate is in cross-speaker conflict and nobody counted the hours), install wasted trips (sixteen crew hours a month with the rate pending), the invoicing lag (cash timing, not a cost), and design churn. The $90,000 remake budget line is a different item from the $55,000 actual and never enters the total. Per-pain cost checks are reported apart from this engagement total.",
    Q("con_arith", "Let me do the arithmetic out loud and you stop me.")))
R.append(row("R5 Upside number", "partial", True, [
    Q("hen_upside", "Answer the phone."),
    Q("fer_upside_hedge", "Maybe two a month, I'd guess, maybe, where the customer gets bored and goes to someone quicker."),
    Q("fer_upside_hedge", "I couldn't put a value on that, it's a guess."),
    Q("del_upside_target", "The hospital framework."),
    Q("del_upside_target", "I'm not putting a number on it either."),
], "Freed capacity is named (coordinators answering the phone) but not valued. The sales manager's 'maybe two a month' lost jobs is a hedged guess with no value and stays a guess. The 'what would you go after' answer is explicit, a regional health system's five-year framework, with no figure, and the convener refuses to put one on it. Present but short of a number: Partial. No figure may be inferred from the thirty-six coordinator hours.",
    Q("con_upside_q", "If the retyping and the chasing went away, the thirty-six hours a week, what would the coordinators do with it?")))
R.append(row("R6 Desired outcome", "met", True, [
    Q("del_outcome", "I open one thing and I can see every live job, where it is, who's got it, and what's late. One screen."),
    Q("del_outcome", "And when a customer changes a panel, the floor knows before the panel's cut, not after."),
    Q("ros_outcome", "For me, the ticket is never wrong. Whatever the floor is looking at is the same thing the customer signed."),
    Q("hen_outcome", "And I stop being a switchboard."),
    Q("del_gideon_relay", "he wants the rollout to go in without a Quarrington, and he wants the cash position to stop being a surprise"),
], "Day to day from three roles who live it, and the branch adding that it must see the same screen. The leadership win is relayed by the convener from the managing director, who was present and silent; our side said aloud it would record it as hers until it is his (" + T("con_yours_until_his") + "). Draft success criteria stay proposed, not agreed, and the approver's own criterion is a gap question to him by name.",
    Q("con_outcome_q", "It's a normal Tuesday in March. What's different?")))
R.append(row("R7 Decision process mapped", "met-with-residual", True, [
    Q("del_decision", "Up to twenty thousand a year I can sign it, and I'd still tell Gideon. Over twenty it's Gideon, full stop."),
    Q("del_after_yes", "Bronwyn raises a purchase order, or if it's a subscription it goes on the company card and she'd rather it didn't."),
    Q("del_after_yes", "Anton's firm will have a security checklist, they always do, and I'll get that to you rather than make you guess."),
    Q("del_prior_purchase", "I did a one-page case, what it cost and what it saved, and he signed it inside a fortnight."),
    Q("del_gideon_cares", "The rollout. That we can run a hundred and forty stores without me living in the job sheet. And the cash thing, Bronwyn's forty-one days."),
    Q("gideon_intro", "Gideon's our MD, he said he's here to listen, so don't expect a lot out of him."),
], "Who is involved, the threshold, what happens after a yes, the IT checklist, the rollout owners and prior budgeting experience are all Met from the convener. The element 'what each cares about' is Met for the convener and the controller and relayed for the approver: he was on the call, never spoke, and our side never addressed him, asking the convener instead at " + T("con_asks_delphine_about_gideon") + ". A proposition about a present client speaker supplied by another client speaker, with no token from him, cannot make that element Met, so the criterion is met-with-residual, the residual is a gap question to the managing director by name, and the silent-attendee risk row in the intake block records that he was never addressed. The delegation graph: the convener runs it, the managing director is the gate-holder over $20,000 and is wanted in either way, the controller raises the order and holds the audit freeze, the IT provider supplies a checklist.",
    Q("con_decision_q", "Delphine, if you decided this was worth doing, what actually happens?")))
R.append(row("R8 Priority and timing", "met", True, [
    Q("del_priority", "Before the rollout. The first stores go in the week of February ninth, and I want the building running on it in January, not learning it in February."),
    Q("del_priority", "So, this quarter to build, January to be live. If it slips into February we've missed the point."),
], "Now rather than later, with a real deadline: live in January ahead of stores going in the week of February ninth. The build window is this quarter.",
    Q("con_priority_q", "Is this a fix for this quarter, or later on?")))
R.append(row("R9 Blockers surfaced", "met", True, [
    Q("ros_blocker", "The floor won't touch a tablet with gloves on."),
    Q("yol_blocker", "And Flint runs its own sheet and, honestly, we like it that way."),
    Q("del_blocker", "If it's another thing to keep up to date, it's dead."),
    Q("bro_audit", "Nothing touches the accounting system before November."),
], "Four blockers in client words: the floor rejects tablets and wants screens on the wall with a printed ticket; the branch wants to keep its own sheet and says it will quietly do so; double entry killed a job-tracking app two years ago inside a quarter; and the audit freezes any connection to the accounting system until November. The studio's view was asked for by the convener and not answered because the design lead had apparently gone.",
    Q("con_blockers_q", "What could get in the way of this going ahead? Anyone.")))
R.append(row("R10 Next step committed", "met", True, [
    Q("del_nextstep", "Wednesday the twenty-first at two works. Same room, or as much of it as I can get. I'll ask Gideon."),
    Q("con_invite", "Wednesday the twenty-first, two o'clock Eastern. I'll send the invite to you today and you forward it to whoever should be there."),
    Q("del_send_sheets", "I'll forward it today."),
], "Discovery call, so the date rule applies: Wednesday the 21st, 2:00 pm Eastern, 45 minutes, the Consultant hosts and builds the first version, the convener forwards the invite the same day and will ask the managing director. The Consultant's line is the proposal; the convener's acceptance is the client-side evidence. The call closed with a commitment question and a yes ('Show me something.').",
    Q("con_propose_next", "Forty-five minutes. Wednesday the twenty-first, two o'clock Eastern?")))
R.append(row("R11 Solution confirmed", "missing", False, [],
    "Discovery call; nothing has been shown. Expected at this stage and not a defect. Blocks only the v1.0 sign-off gate.", None))
R.append(row("R12 Scope agreed verbally", "partial", True, [
    Q("con_scope_playback", "Is that the right shape?"),
    Q("del_scope_agree", "That's the right shape. Two things. Don't build the quoting in it, ever, Fergus will never forgive me. The estimating tool stays."),
    Q("del_relayed_nod", "He's nodding. Take that as a yes. He's not going to say anything on a call with fourteen people on it, he never does."),
    Q("del_commitment", "Yes. Show me something. I don't want a proposal, I don't want a price, I want to see it run a job."),
], "The convener agreed a five-item first version out loud, with two exclusions (quoting stays in the estimating tool; the job number comes from the accounting system) and two requirements from colleagues (screen on the wall; job number never typed). But the approver's assent exists only as a relayed nod, which is not evidence, the branch's exclusion of its own sheet is unresolved, and our side played the scope back 'not to sign anything'. Enough to build a v0.1, not an agreed scope: Partial, pricing gate shut, and the client asked for no proposal or price in any case.",
    Q("con_scope_playback", "Let me play back what I'd put in a first version, just so you can hear it, not to sign anything.")))
# per-pain checks
R.append(row("P1 Stated", "met", True, [
    Q("hen_retype", "We type it again, because the quote lives in the estimating tool and the floor can't see the estimating tool."),
    Q("ros_stale_ticket", "Then the ticket's wrong and nobody knows. That's Quarrington in one sentence. That's most of our remakes in one sentence."),
], "P1: the quote is retyped into the job sheet and ticket by hand, and a ticket that goes stale builds the wrong thing. Stated by the coordinator lead and the production manager, who work in the same process.", Q("con_walk", "Fergus, it starts with you.")))
R.append(row("P1 Concrete", "met", True, [
    Q("quarrington_concrete", "eleven of the twenty-two were the wrong size. Not by a lot. By about an inch and a half on the width, which on a routed panel is the whole panel."),
    Q("ros_quarrington_cause", "The dimensions on the job ticket were the survey dimensions, not the approved drawing dimensions. Somebody typed the wrong column into the ticket."),
], "Quarrington Hotels, August: eleven of twenty-two routed panels remade because the ticket carried survey dimensions instead of the approved drawing's. A coordinator owned the error on the call; that admission is internal only.", Q("con_whynow_q", "What's made this matter this autumn rather than last year?")))
R.append(row("P1 Workaround", "met", True, [
    Q("hen_p1_workaround", "A coordinator rings the floor and reads the ticket back against the quote, on the big ones. On the small ones we don't, there isn't time, and the small ones are where it goes wrong."),
    Q("hen_p1_why_not", "I can't read a hundred and forty tickets down the phone. And it depends on who's in. When I'm off, nobody reads anything back."),
], "Today: a phone read-back on big jobs only. Why it will not do: it skips the small jobs where errors happen, depends on one person being in, and cannot scale to 140 stores.", Q("con_p1_workaround_q", "And today, how do you stop a wrong ticket getting to the floor?")))
R.append(row("P1 Reach", "met", True, [
    Q("ros_p1_reach", "My leads, who wait. Calum's crew, who go back out. Kwame, who explains it to the customer. And Bronwyn, who writes it off. It's everybody."),
    Q("quarrington_reach", "the customer's regional director was standing in the lobby when the second set went up"),
], "Production leads, the install crew, the account manager, finance and the customer.", Q("con_p1_reach_q", "Who else ends up dealing with a wrong ticket?")))
R.append(row("P1 Cost inputs", "met", True, [
    Q("hen_hours", "Six each, and there are six of us."),
    Q("bro_rates", "Thirty-eight an hour loaded, give or take."),
    Q("ros_wait_hours", "Call it eight hours a week between the two of them standing at the board with a ticket in one hand and a phone in the other"),
    Q("bro_writeoff", "That's the actual, and it's materials, it doesn't have the hours in it."),
], "Hours, headcount and a materials write-off from the people who carry them. Remake labour has no input: its frequency is in cross-speaker conflict and nobody counted the hours, so it stays unquantified until the remake log is counted. The $90,000 budget line is not a cost input.", Q("con_p1_cost_q", "Across the six of you, roughly how many hours a week go into retyping and chasing?")))
R.append(row("P1 Trajectory", "met", False, [
    Q("hen_p1_why_not", "A hundred and forty stores."),
    Q("del_140_anything", "We don't do a hundred and forty of anything."),
], "Volunteered inside the workaround answer rather than asked: the rollout multiplies the retyping and the read-back cannot follow it. Ask-only in the method, so the flag is recorded as not asked and the grade stands on the volunteered quote.", None))
R.append(row("P2 Stated", "met", True, [
    Q("eme_versions", "Every one is a file. We name them, we're disciplined about it, but the approval is a reply to one of them and you have to find which one."),
], "P2: the approved proof version and the version the floor builds from can differ, because the approval is an email reply to one of several files.", Q("con_p2_workaround_q", "So today, if I'm on the floor and I want to know which proof is approved, what do I do?")))
R.append(row("P2 Concrete", "met", True, [
    Q("eme_concrete", "The university library job went to print on version four. The customer had approved version five."),
], "A university library directory printed from the wrong version; nineteen arrows pointed the wrong way (the design lead said twenty-two, the production manager corrected it to nineteen on the call).", Q("con_p2_concrete_q", "Has that gone wrong recently?")))
R.append(row("P2 Workaround", "met", True, [
    Q("eme_workaround", "You ask me. Or you ask a coordinator, who asks me. I'm the one who can find the reply. If I'm off, you wait, or you guess."),
    Q("eme_why_not", "Me being off. And a hundred and forty stores, which will each have their own proof, and I have five designers."),
], "Today: ask the design lead. Why it will not do: it depends on him being in, and the rollout multiplies proofs across five designers.", Q("con_p2_workaround_q", "So today, if I'm on the floor and I want to know which proof is approved, what do I do?")))
R.append(row("P2 Reach", "partial", False, [
    Q("eme_reach", "The floor built what it was handed, and what it was handed was wrong."),
], "Only the floor is named, by implication; the customer and the crew are not, and nobody asked. Gap question to the design lead or the coordinator lead: who else ends up dealing with a proof built from the wrong version?", None))
R.append(row("P2 Cost inputs", "missing", False, [],
    "Never asked. The design lead was in the room when the pain was discussed and last spoke at " + T("eme_reach").split(" ")[0] + " at " + T("eme_why_not") + "; no hours, counts or rework figures exist for proof churn. Ask-only; a targeted question to him, not a group question.", None))
R.append(row("P2 Trajectory", "met", False, [
    Q("eme_why_not", "And a hundred and forty stores, which will each have their own proof, and I have five designers."),
], "Volunteered in the workaround answer, not asked: 140 proofs across five designers. Recorded as not asked.", None))
R.append(row("P3 Stated", "met", True, [
    Q("cal_p3_stated", "And the thing nobody's said is that a crew turns up to a site and the job isn't ready. The sign's still in paint, or the permit's not through, or the site's not ready for us, and two people have driven two hours for nothing."),
], "P3: install crews sent to jobs that are not ready. Stated by the scheduler only after the room-wide open check-in at " + T("con_open_checkin") + "; our side had deferred install at " + T("con_install_deferred") + ".", Q("con_open_checkin", "Is there a part of how a job moves through this building that hasn't come up yet? Anyone. I'm happy with silence.")))
R.append(row("P3 Concrete", "met", True, [
    Q("cal_p3_concrete", "Traverse City, three weeks ago. Retail unit, four panels. The ticket said ready. The board said ready. One panel was in paint because it had been remade, and nobody moved the ticket back."),
], "Three weeks before the call: one remade panel still in paint while the ticket and the board both said ready; the crew went twice.", Q("con_concrete_q", "When did that last happen?")))
R.append(row("P3 Workaround", "met", True, [
    Q("cal_p3_workaround", "I ring the floor every morning. I walk it if I'm in. I ring Yolanda for hers. And I ring the site the day before, if I remember, and I don't always remember because I've got six crews and one of me."),
    Q("cal_p3_trajectory", "I can't ring five states every morning. I can barely ring Flint."),
], "Today: a morning phone round and a walk of the floor. Why it will not do: one scheduler, six crews, and a rollout in five states.", Q("con_p3_workaround_q", "And what stops you carrying on ringing?")))
R.append(row("P3 Reach", "met", True, [
    Q("cal_p3_reach", "The crew, because it's overtime nobody planned. The customer, because we've turned up twice. And the next job, because that crew was supposed to be somewhere else the day they go back."),
], "Crews (unplanned overtime), the customer, and the next job's schedule.", Q("con_p3_reach_q", "Who else feels a wasted trip?")))
R.append(row("P3 Cost inputs", "partial", True, [
    Q("cal_p3_cost", "Two a month. Some months three. Call it two. Four hours each, two people, so sixteen hours a month of crew time, before the fuel."),
    Q("del_crew_rate_gone", "That's a Bronwyn number and she's gone. Put it on her list."),
], "Effort-quantified, rate pending: two wasted trips a month at four hours for two people is sixteen crew hours a month, plus fuel; the crew's loaded rate is the controller's number and she had left at " + T("bro_leaves") + ". One targeted question on her list, not a re-planned conversation. No rate may be assumed from the coordinator or lead rates.", Q("con_p3_cost_q", "How often does a wasted trip happen?")))
R.append(row("P3 Trajectory", "met", False, [
    Q("cal_p3_trajectory", "The rollout. Eight crews on the road instead of six, if we hire, in five states."),
], "Volunteered in the workaround answer: eight crews across five states if they hire for the rollout. Recorded as not asked.", None))
R.append(row("P4 Stated", "met", True, [
    Q("bro_p4_stated", "I don't know it's installed. Nobody tells finance a job is on the wall."),
], "P4: finance is not told a job is installed, so the invoice waits. Stated by the controller, who lives it.", Q("con_install_deferred", "Bronwyn, I promised you early. Where does finance touch a job?")))
R.append(row("P4 Concrete", "met", True, [
    Q("bro_p4_concrete", "Average from install to invoice, forty-one days. Forty-one. For work we've already done and already paid the crew for."),
], "A measured average the controller pulled before the call: 41 days from install to invoice.", Q("con_p4_concrete_q", "How late does that make the invoice?")))
R.append(row("P4 Workaround", "met", True, [
    Q("bro_p4_stated", "I find out because a coordinator mentions it, or a customer rings about something else, or I walk the floor on a Friday and ask."),
    Q("bro_p4_workaround", "It doesn't scale. I can walk the Saginaw floor. I can't walk Flint, and I certainly can't walk a hundred and forty pharmacies."),
], "Today: hearsay and a Friday walk of the floor. Why it will not do: it cannot reach the branch or the rollout. The branch manager emails installs 'mostly'.", Q("con_p4_workaround_q", "What stops you carrying on that way?")))
R.append(row("P4 Reach", "met", True, [
    Q("bro_p4_reach", "Me, and the line of credit. There's about a million two sitting installed and not invoiced at any moment."),
], "The controller, the line of credit and the managing director, who sees the cash position. The 'about a million two' is scale, not a cost.", Q("con_p4_reach_q", "Who feels that?")))
R.append(row("P4 Cost inputs", "partial", False, [
    Q("bro_p4_reach", "There's about a million two sitting installed and not invoiced at any moment."),
], "Volume and delay exist (41 days, about $1.2M installed and uninvoiced at any time) but no cost of carrying it was given or asked, so it is cash timing and not a bleed input. The rate slot is empty: [unpriced]. On the controller's list.", None))
R.append(row("P4 Trajectory", "not-obtainable", True, [
    Q("del_p4_traj_gone", "That's a Bronwyn question and she's gone. I'd be guessing. Put it on her list."),
], "Asked at " + T("con_p4_traj_q") + ", after the controller had left at " + T("bro_leaves") + " (a departure inferable only from her own words). Nothing in the inputs, and the role that could supply it, the Finance Controller, was no longer in the room, so the grade is not obtainable from this room and routes to her list rather than to the same question again in a group.", Q("con_p4_traj_q", "Say nothing changes. What does that look like a year from now, with the rollout on top?")))
key["rubric"] = R

key["pains"] = [
    dict(Q("hen_retype", "We type it again, because the quote lives in the estimating tool and the floor can't see the estimating tool."), theme="P1 Quote retyped by hand into the job sheet and ticket"),
    dict(Q("ros_stale_ticket", "Then the ticket's wrong and nobody knows."), theme="P1 Ticket goes stale after printing; remakes follow"),
    dict(Q("hen_calls", "Thirty-one calls asking where a job is. Thirty-one."), theme="P1 Coordinators as a switchboard for job status (ungraded sub-theme)"),
    dict(Q("eme_versions", "the approval is a reply to one of them and you have to find which one"), theme="P2 Approved proof version lives in an email reply"),
    dict(Q("eme_concrete", "We printed twenty-two arrows pointing the wrong way."), theme="P2 Wrong version built"),
    dict(Q("cal_p3_stated", "a crew turns up to a site and the job isn't ready"), theme="P3 Crews sent to jobs that are not ready"),
    dict(Q("ros_ready", "Which usually means it's ready. Usually."), theme="P3 'Ready' on the floor board is not trustworthy"),
    dict(Q("bro_p4_stated", "Nobody tells finance a job is on the wall."), theme="P4 Finance not told a job is installed"),
    dict(Q("bro_p4_concrete", "Average from install to invoice, forty-one days."), theme="P4 Invoices 41 days late on average"),
    dict(Q("kwa_changeorder", "Whether that reaches the floor before the panel's cut is a coin flip, and I'm not exaggerating, it's about half."), theme="Change orders reach the floor late (ungraded; the 'half' was withdrawn to 'a lot')"),
    dict(Q("yol_own_sheet", "The Saginaw one is unusable by Wednesday, there are two hundred rows and half the filters are somebody's leftovers."), theme="Branch keeps its own copy of the job sheet (ungraded)"),
    dict(Q("rollout_shape", "their project manager wants a weekly status on all hundred and forty, which today would mean Henrike building it by hand every Friday"), theme="Weekly rollout status would be built by hand (ungraded; a reporting need)"),
    dict(Q("kwa_survey", "And then the original stays in the van, or in a drawer, or in Kwame's car"), theme="Paper surveys go missing (ungraded)"),
]
key["numbers"] = {
    "bleed": {"value": "$147,768 per year (spoken as 'A hundred and forty-eight thousand, near enough. A year.'), built and confirmed by the client and called light. Coordinators 6 x 6 h/wk = 36 h x $38 loaded x 52 = $71,136; production leads 8 h/wk x $52 loaded x 52 = $21,632; remake materials actually written off last year $55,000 (hedged 'fifty-five, fifty-six'; hedge kept). Unquantified and excluded: remake labour (rate in conflict, hours uncounted), install wasted trips (16 crew h/month, rate pending), the 41-day invoicing lag (cash timing), proof churn. The $90,000 remake budget line is not a bleed input.", "quote": "So seventy-one, plus twenty-two, plus fifty-five. A hundred and forty-eight thousand, near enough. A year.", "status": "met"},
    "upside": {"value": "No figure. Freed capacity named (coordinators answer the phone; a faster quote-to-proof lag) but not valued; 'maybe two a month' lost jobs is a stated guess with no value; the target they cannot pursue today is a regional health system's five-year signage framework, with no number offered and one refused. Nothing may be derived from the 36 coordinator hours.", "quote": "I couldn't put a value on that, it's a guess.", "status": "partial"},
}
key["vocabulary"] = [
    {"their_term": "job", "meaning": "A won quote from handover to invoice; 'live' means sold and not invoiced (about 240), 'on the floor' means in production (110-115)", "likely_monday_object": "item on a Jobs board (one board, both sites)"},
    {"their_term": "job sheet", "meaning": "The master spreadsheet, one row per job, about forty columns; the branch keeps its own copy, 'the Flint sheet'", "likely_monday_object": "the Jobs board itself, replacing both copies, with a site column"},
    {"their_term": "job ticket", "meaning": "The printed traveller in a sleeve on the floor board, printed from the job sheet by the production administrator", "likely_monday_object": "a printable item view or doc generated from the job; reprints on change"},
    {"their_term": "the floor board", "meaning": "A twelve-foot physical whiteboard with columns print, cut, fab, paint, assembly, ready; tickets move along it by hand", "likely_monday_object": "production status column and a wall-screen board view (not tablets)"},
    {"their_term": "ready", "meaning": "The last column on the floor board; 'usually means it's ready'", "likely_monday_object": "status label that install scheduling depends on; a remade panel must pull it back"},
    {"their_term": "proof", "meaning": "The drawing the customer signs off: sizes, layout, colours, mounting; versioned files", "likely_monday_object": "file column plus a version and an approval status on the job"},
    {"their_term": "sign-off", "meaning": "The customer's approval of a proof, today an email reply", "likely_monday_object": "status column with the approved version and date; not a monday approval feature by default"},
    {"their_term": "remake", "meaning": "A panel built a second time (reprint, or a new blank, router, paint, cure, re-install); logged in a paper book by the router", "likely_monday_object": "subitem or a remake flag with reason; counts feed the conflict question"},
    {"their_term": "change order", "meaning": "A customer change after sign-off, charged if big enough, absorbed if small", "likely_monday_object": "subitem or update with a visible flag on the job; not a Service ticket"},
    {"their_term": "panel", "meaning": "One sign face within a job (a lobby package has 22)", "likely_monday_object": "subitem, or a count column where subitems are too heavy"},
    {"their_term": "survey", "meaning": "Site measurement on a paper form with phone photos; dimensions, wall type, power, access, lift", "likely_monday_object": "file column and survey fields on the job"},
    {"their_term": "crew", "meaning": "A two-person install team; six crews, five in Saginaw and one in Flint", "likely_monday_object": "people or dropdown column on the install schedule"},
    {"their_term": "rollout", "meaning": "A multi-site programme of near-identical jobs; the pharmacy chain's 140 stores", "likely_monday_object": "group or a rollout field on the Jobs board with a weekly status view"},
    {"their_term": "job number", "meaning": "Issued by the accounting system when the controller opens the job", "likely_monday_object": "text column, never typed by a coordinator; sourced later from the accounting system"},
    {"their_term": "wayfinding package", "meaning": "The set of interior panels for one site (eight to twelve per store)", "likely_monday_object": "job type dropdown"},
    {"their_term": "install pack", "meaning": "Not used by the client; the Consultant's term. Permits and drawings travel with the job informally", "likely_monday_object": "none until the client names it"},
]
key["entities_and_workflows"] = [
    "Quote: a request from a customer, contractor or architect; a site survey by an account manager or a local crew; the quote built in the estimating tool; 60-70 quotes a week, about a third won",
    "Handover: a won quote becomes an email from sales to the coordinator lead, or the coordinators find out when the customer rings",
    "Job setup: a coordinator opens a row in the job sheet and retypes the quote (customer, site, panel count, sizes, materials, finishes, due date); the controller issues the job number from the accounting system",
    "Proofing: the studio draws the proof; the customer approves by email reply; hospital proofs go round four or five versions",
    "Production: the production administrator prints the job ticket from the job sheet; the ticket moves across the physical floor board through print, cut, fab, paint, assembly, ready; a stale ticket builds the wrong thing",
    "Change orders: a customer change after sign-off reaches the coordinator by email and the floor sometimes; charged if big, absorbed if small",
    "Remakes: logged in a paper book by the router; frequency contested (one in ten vs one in four); materials written off about $55,000 last year against a $90,000 budget line",
    "Install: six two-person crews scheduled on a spreadsheet a week at a time; the scheduler rings the floor each morning; wasted trips about two a month",
    "Invoicing: the controller invoices when she learns a job is installed, by hearsay or a Friday walk; average 41 days from install to invoice; about $1.2M installed and uninvoiced at any time",
    "Branch: Flint (12 people, one crew) quotes through Saginaw but keeps its own copy of the job sheet and emails installs to finance 'mostly'",
    "Pharmacy rollout: 140 stores, five states, phased by region from the week of February ninth to June; three sign types per store; the customer's project manager wants a weekly status on all 140",
    "Buying process: the Operations Director signs up to $20,000 a year and tells the MD; over $20,000 the MD signs; a one-page cost-and-saving case got the CNC router signed inside a fortnight; after a yes the controller raises a PO; the IT provider supplies a security checklist; the Operations Director, the coordinator lead and HR roll it out",
    "People mentioned but not on the call: Ottoline (marketing manager whose team uses the existing monday account), the pharmacy chain's project manager, Quarrington's regional director, the auditors",
]
key["integrations_mentioned"] = [
    "The estimating tool: stays ('The estimating tool stays.'); a won quote's fields would ideally flow to the job rather than be retyped, but no export or API was discussed, so that is a question, not a plan",
    "The accounting system: source of the job number and of invoices; no connection of any kind before November because of the audit; after that a one-way feed of the job number is the client's stated wish",
    "Email: the handover, proof approvals and change orders live here today; the design is to make the approval and the change visible on the job instead, not to integrate a mailbox",
    "The design tool: stays; proofs are files, so a file column and a version field, not an integration",
    "The shared drive: holds the job sheet; the job sheet is what the build replaces",
    "The existing monday account: marketing's content calendar, 25 seats, Standard (self-corrected from Pro), administrator unknown; the build's home or a separate workspace is a question",
]
key["compliance_or_security_signals"] = [
    "Audit freeze: nothing connects to the accounting system before November (the controller, on the record at " + T("bro_audit") + ")",
    "The IT provider's security checklist is promised by the convener; its contents are unknown and its author, Anton, never spoke, so access, sign-on and password policy are open and never to be answered by us",
    "The pharmacy customer cannot be named until the contract is countersigned; nothing in the record, seed data or client-facing text may carry or guess the name",
    "Customer artwork and proofs are customer property; seed data must not reuse real customer proofs or names (Quarrington, the university library)",
    "Loaded rates ($38, $52) and the remake write-off are finance figures; not for boards, seed data or client-facing material",
    "Seat cost was raised as a concern (crews and floor staff who would open it twice a month); plan limits on Standard and who needs a seat are preflight questions",
]
key["objections"] = [
    {"quote": "If it's another thing to keep up to date, it's dead.", "type": "Team won't adopt it (raised by the convener as the blocker she always names; a job-tracking app died inside a quarter two years ago from double entry)"},
    {"quote": "The floor won't touch a tablet with gloves on.", "type": "Team won't adopt it (embedded: a fact about the floor from the person who runs it, with the cause given; the design answer is a wall screen and a printed ticket)"},
    {"quote": "And Flint runs its own sheet and, honestly, we like it that way.", "type": "We'll build it ourselves (the branch maintains its own copy of the current setup and says it will quietly keep it; partly softened later by 'And Flint sees the same screen as Saginaw.')"},
    {"quote": "Over twenty it's Gideon, full stop.", "type": "Must check with someone (the approver was on the call, silent, never addressed by our side, and his assent was relayed as a nod)"},
    {"quote": "Nothing touches the accounting system before November.", "type": "Wrong time, next quarter (scoped to the integration only; the build itself is wanted in January)"},
    {"quote": "Are we going to end up paying per head for people who'd open it twice a month?", "type": "Price feels high (anticipated from a seat-count question; our side deferred the answer and owes it in the recap)"},
    {"quote": "Shouldn't Ottoline be on this? If it's her account we'd be going into.", "type": "Must check with someone (a client asking why a person is not in the room; the convener took the action to bring her in)"},
]
key["commitments_and_next_steps"] = [
    dict(Q("del_nextstep", "Wednesday the twenty-first at two works."), what="First-version walkthrough, 45 minutes, same room or as much of it as the convener can get; she will ask the managing director", owner="Consultant (hosts and builds); Delphine Castellane confirms attendance", date="2026-10-21 14:00 Eastern (Wednesday the 21st; month and year inferred from the February ninth rollout and the October audit)"),
    dict(Q("con_invite", "I'll send the invite to you today and you forward it to whoever should be there."), what="Send the calendar invite; the convener forwards it the same day", owner="Consultant, then Delphine Castellane", date="Day of the call (date not stated)"),
    dict(Q("del_send_sheets", "And I'll send you the job sheet by Friday, both of them, so you can see what forty columns looks like. Names off, if that's all right."), what="Send both job sheets with names removed", owner="Delphine Castellane", date="Friday of the call week (date not stated)"),
    dict(Q("ros_log_commit", "In a week. I'll count it myself so it's counted the same way all the way through."), what="Count the paper remake log for the last quarter, the mechanism that settles the one-in-ten versus one-in-four conflict", owner="Rosalind Achebe", date="One week after the call"),
    dict(Q("bro_leaves", "Send me the list of what you need and I'll get you the numbers by end of week, the write-off figure properly and whatever else."), what="Supply the crew loaded rate, the remake write-off from the books and the invoicing trajectory; the Consultant sends the list tonight", owner="Bronwyn Tsai (answers); Consultant (sends the list); Delphine Castellane chases", date="End of the call week"),
    dict(Q("del_ottoline_commit", "She should. That's on me. I'll bring her in for the next one."), what="Bring the marketing manager who owns the existing account into the next meeting", owner="Delphine Castellane", date="Before the 21st"),
    dict(Q("del_admin_commit", "I'll find out who the admin is. And I'll get Anton's list."), what="Identify the existing account's administrator and obtain the IT provider's security checklist", owner="Delphine Castellane", date="Not set"),
    dict(Q("con_deferred_seats", "I'll put it in the recap with a straight answer."), what="Answer the per-seat cost question our side deferred on the call (a deferred answer, converted to an owned commitment)", owner="Consultant", date="With the recap, end of the day after the call"),
    dict(Q("con_recap", "And I'll send a short recap by end of day tomorrow, what I heard and the next steps, so you can correct anything I've got wrong."), what="Send the recap for correction", owner="Consultant", date="End of the day after the call"),
    dict(Q("con_propose_next", "I put a first version together with those five pieces, in your words, jobs, tickets, proofs, crews, installed, on made-up jobs unless you'd rather I used real ones"), what="Build the five-item first version; whether seed jobs are made up or real is open", owner="Consultant", date="Before 2026-10-21"),
]
key["traps"] = [
    "The roster is claimed, not observed: the export header lists fourteen display names with no roles. Roles come from the convener's narration; voices heard is nine of thirteen client attendees, voices missing is four named people, and the line must never read 'none'.",
    "Gideon Ashworth-Pell is the decision-shaped silent attendee: introduced as the MD who is 'here to listen', the signer over $20,000, never spoke, never addressed by our side (the Consultant asked Delphine about his view at " + T("con_asks_delphine_about_gideon") + " rather than asking him). He is a named risk row, not a stakeholder with recorded views, and nothing he is reported to want is his evidence.",
    "'He's nodding. Take that as a yes.' is a relayed nod from a colleague and counts for nothing on R12 or R7; the Consultant's own 'I can see a few nods' is correctly disclaimed as not an answer. No nonverbal read stands in for a commitment.",
    "The cross-speaker conflict on the remake rate (one in ten at " + T("fer_remake_rate") + ", closer to one in four at " + T("ros_remake_rate") + ") is kept as both statements with speaker and location, marked unresolved, logged as a conflict and raised as the gap question the remake log count answers. The later statement does not win, and the two may even have different denominators ('I count what the customer sees' vs 'what the shop builds twice'). No remake-labour cost is computed from either figure.",
    "The self-contradicting turn at " + T("tier_turn") + " (Pro, then Standard, same speaker, same proposition, same turn) is the one place the recency rule applies: Standard is recorded as the client-stated tier, 'Pro' goes to the log as superseded, and no conflict is raised. It is still unverified and confirmed at preflight.",
    "The controller's two figures at " + T("bro_writeoff") + " ($90,000 budgeted for remake materials; about $55,000 actually written off) are two different items, as she says herself: neither supersedes the other, no arithmetic runs between them, and only the actual is a bleed input, with its 'fifty-five, fifty-six' hedge kept.",
    "Departures exist only in speech: the controller announces hers (" + T("bro_leaves") + "), the sales manager's is reported by the convener (" + T("fer_departure_reported") + "), the account manager announces his own (" + T("kwa_departure") + "). The design lead's silence after " + T("eme_why_not") + " plus a colleague's 'He may have dropped' is NOT a departure: record presence unknown with the hedge quoted. The managing director's presence at any moment after the roster is the header's claim only.",
    "Who was present when each commercial figure was stated matters: the tier and seat count with the whole room; the $20,000 threshold after the controller, the sales manager and the account manager had gone; the per-seat question with everyone present and deferred by our side.",
    "P4 Trajectory is 'not obtainable from this room', not Missing: it was asked at " + T("con_p4_traj_q") + " after the only person who could answer had left; it routes to her list, not to the next group meeting.",
    "P3 Cost inputs are effort-quantified with the rate pending (sixteen crew hours a month, crew rate on the controller's list). No rate may be borrowed from the $38 or $52 figures.",
    "The bleed is the client's own $147,768 ('a hundred and forty-eight thousand, near enough'), excluding remake labour, install trips, the invoicing lag and proof churn. Do not add the upside, the $90,000 budget line, the $1.2M uninvoiced balance or any remake-rate arithmetic to it.",
    "Kwame's 'about half' for change orders reaching the floor late was withdrawn by its own speaker ('It's a lot.') after Henrike's 'It's not half': a disagreement settled in the room by withdrawal, recorded as 'a lot' with no figure and no conflict entry.",
    "'Two hundred and something' (Rosalind) and 'Two-forty' (Delphine) live jobs agree; a vague and a specific figure are not a conflict. The floor's 110-115 is a different count (in production).",
    "The per-seat cost question at " + T("kwa_seat_question") + " was answered with a deferral at " + T("con_deferred_seats") + ": it goes in the deferred-answers register as an owned commitment due with the recap, and no seat price is invented.",
    "The room-wide open check-in at " + T("con_open_checkin") + " is what produced P3 from a previously silent attendee whose stake our side did not know; it is a legitimate discovery instrument on a large call, and named check-ins remain the only kind that confirm a pain. The next run-sheet carries one open check-in per phase boundary because the room holds attendees whose stake is not in the record.",
    "Install was deferred by our side at " + T("con_install_deferred") + " ('We'll come to install.') and not returned to for fourteen minutes; a delivery note, not a grading change.",
    "Tool references are category words on purpose (an estimating tool, a design tool, an accounting system, a spreadsheet, email); no product name may be inferred or inserted, and a sentence in any client-facing text names at most one such category.",
    "The pharmacy chain is deliberately unnamed ('I can't name them until the contract's countersigned'); never guess or infer it. Quarrington Hotels is named and its story is a failure narrative that stays internal.",
    "The account tier is Standard by the client's own correction, so no portfolio is proposed; seats and plan limits (25 seats, marketing's) are preflight questions, and the build's home in an account that already has marketing in it is a question, with the administrator unknown (R1's residual).",
    "Quoting stays in the estimating tool and the job number comes from the accounting system, by the client's explicit exclusion; no CRM pipeline is proposed because 'quote' is a priced document here, and no Service desk is proposed because change orders and remakes are events on a job.",
    "Statements about the silent production administrator's work ('Lettie prints it off the job sheet') come from colleagues and describe her task; they are current-state evidence about the process, not evidence from her, and a question about her hours goes to her by name.",
    "Yolanda's join at " + T("yol_join") + " is a late join inferable only from speech; the line carries an '[inaudible]' and is quoted only around it. The two '[crosstalk]' turns are complete sentences under their own labels and are not re-joined.",
    "Internal only: a coordinator owning the Quarrington error ('It was one of mine.'), the design lead's possible absence, the sales manager's remake figure being contradicted by the floor, 'Fergus will never forgive me', 'she'd rather it didn't' about the company card, and every remark about the managing director's silence.",
    "Pricing and proposal prep are out of v1 and the pricing gate is shut (R12 Partial, R7 residual); the client asked for neither. Produce no price, proposal or seat-cost estimate beyond the promised straight answer routed to the user.",
]
key["requested_changes"] = [
    {"type": "remove", "description": "Pre-build exclusion: quoting is never built in monday; the estimating tool stays.", "quote": "Don't build the quoting in it, ever, Fergus will never forgive me. The estimating tool stays."},
    {"type": "change", "description": "Pre-build requirement: the job number is never typed by a coordinator; it comes from the accounting system (no connection before November, so the first version carries it as a field sourced later).", "quote": "The job number has to come from the accounting system. That's mine as well."},
    {"type": "change", "description": "Pre-build requirement from the floor: a screen on the wall and a printed ticket, not tablets.", "quote": "And the floor gets a screen on the wall, not tablets. I said it, I'll say it again so it's written down."},
    {"type": "change", "description": "Both sites on one board with a site column, and the branch sees the same screen; stated by the branch manager after her earlier blocker, so it is a requirement with an unresolved objection behind it.", "quote": "And Flint sees the same screen as Saginaw."},
]
key["should_plugin_propose_a_build"] = True
key["expected_questions_before_building"] = [
    "To Gideon Ashworth-Pell by name, before the close of the next meeting: what would he count as a win, and what does he want to see on the 21st (R7 residual; R6 leadership criterion; the only silent attendee with a decision-shaped role)?",
    "To Rosalind Achebe: the remake log count for the last quarter, with the denominator stated (jobs with any panel through twice, or jobs the customer saw remade), which settles the one-in-ten versus one-in-four conflict.",
    "To Bronwyn Tsai, on her list: the crew loaded rate (P3 cost), the remake write-off from the books, and what the 41-day lag looks like a year from now with the rollout (P4 trajectory).",
    "To Delphine Castellane: who administers the existing monday account, and does the build live in that account beside marketing's workspace or elsewhere (R1 residual)?",
    "Verify at preflight: the plan is Standard and the seat count is 25, and which plan limits on Standard bear on a wall-screen view, automations and a printable ticket.",
    "Who needs a seat: crews and floor staff who would open it rarely, against the per-seat concern raised and deferred; the straight answer promised in the recap.",
    "Anton Petrakis's security checklist, through the convener: sign-on, password policy and guest access for the IT provider's own people; never answered by us.",
    "How should a proof approval be recorded when the customer's approval is an email reply today: who marks it approved, and which version string is the one the floor sees?",
    "Should the branch's own sheet be retired on day one, or run alongside for a period, given the branch manager's stated intent to keep it?",
    "Made-up or real jobs in the first version, and if real, the names-off sheets due Friday as the source; nothing from the pharmacy customer by name.",
    "What does 'ready' need to mean so that a remade panel pulls a job back out of it, and who moves it?",
]
key["expected_verdict"] = {
    "verdict": "Discovery complete",
    "gates_met": [
        "Solution blueprint (R1 met-with-residual, R2 Met; the residual, who administers the existing account, is a gap question and not a gate failure)",
        "Build (no extra method gate; still needs the user's approval at the approval stop)",
        "First demo (v0.1): nothing extra needed; booked for Wednesday the 21st, 2:00 pm Eastern",
    ],
    "gates_not_met": [
        "Pricing or proposal prep (R4 Met, but R7 met-with-residual on the approver's own priorities and R12 Partial with the approver's assent relayed; the client asked for no proposal or price in any case)",
        "v1.0 sign-off (R11 Missing, no demo yet; R6 criteria proposed, and the approver's criterion relayed rather than his)",
    ],
    "note": "R2, R3 and R4 are Met from client-side quotes and R7 is met-with-residual, which is a Met grade whose missing element (what the approver himself cares about) becomes a gap question rather than a demotion, so the verdict is Discovery complete. Gap questions for the 21st, capped per audience: the approver's own win condition (to him by name), the remake log count (conflict), the controller's list (crew rate, write-off, P4 trajectory), the account administrator, and the branch's sheet. The readiness section carries the voices line (nine of thirteen client attendees heard; four missing by name), the named risk row for the silent managing director, and the delivery note that our side never addressed him and deferred install until an open check-in recovered it. The pricing gate stays shut, and pricing is out of v1 regardless. The type header resolved on every dimension, so no criterion is advisory.",
}
key["account_context"] = {
    "tier": "Standard, stated by the client after correcting herself in the same turn from Pro ('We dropped to Standard in January when we trimmed the seats, I signed the renewal myself. Standard.'); the earlier value is logged as superseded, and the tier is unverified until preflight reads it",
    "products_enabled": [
        "Work Management: an existing account with 25 seats used only by marketing for a content calendar",
        "CRM: never mentioned; unknown and not needed",
        "Service: never mentioned; unknown and not needed",
        "dev: not mentioned and out of v1",
    ],
    "existing_monday_setup": "One live account owned in practice by marketing (Ottoline's team, not on the call) running a content calendar on 25 seats; nobody outside marketing uses it ('I've logged in twice.'), the sales manager has only seen it over a colleague's shoulder, and who set it up is unknown ('it predates me'). Nothing operational is inherited, but the account has people in it, so the administrator, the workspace the build goes into, seat allocation and permissions are live questions before anything is written, and marketing's board must not be disturbed. The convener took the action to find the administrator and to bring the marketing manager into the next meeting.",
    "evidence_quote_or_null": "We dropped to Standard in January when we trimmed the seats, I signed the renewal myself. Standard. Twenty-five seats on Standard.",
}
key["expected_structures"] = {
    "native_boards_required": [],
    "portfolio_expected": False,
    "portfolio_reason": "The client states Standard (after a same-turn correction from Pro), so the Enterprise default does not apply and no portfolio is proposed; if preflight reads Enterprise instead, the question is reopened and the reason recorded either way. The rollout's 140 near-identical jobs are handled as a group or a rollout field with a weekly status view on the one Jobs board, not as connected projects.",
    "lookalike_traps": [
        "Building a Quotes or Pipeline board because the client says 'quote' sixty times: quoting stays in the estimating tool by explicit exclusion, and 'quote' is a priced document, not a deal.",
        "Building a Change Orders or Remakes ticket board that imitates a native Service Tickets board: both are events on a job and belong on it as subitems, flags or updates.",
        "Rebuilding the forty-column job sheet column for column, or building a second Jobs board for the branch, when the client's own outcome is one screen for both sites with a site column.",
        "Treating marketing's content calendar as a starting point or a template for the Jobs board.",
        "Proposing tablets on the floor or a mobile-first view when the floor's requirement is a wall screen and a printed ticket.",
    ],
    "notes": "One product, Work Management, and no native-board requirement because neither CRM nor Service is in scope. The build is judged on: one Jobs board for both sites; the approved proof version and approval status on the job; a printable ticket that reflects the job as it is now; an install schedule that reads the job's real status so 'ready' means ready; an installed flag finance can see; a weekly rollout status view. Constraints that must survive: no quoting in monday; the job number never typed by a coordinator and sourced from the accounting system only after November; no connection to the accounting system before then; a wall screen and printed ticket for the floor. Automations arrive as one approval list with recipients named, and the recipients cannot include people who were never heard without the convener confirming their part.",
}
key["accepted_behaviours"] = [
    "Building the voices line from the export header against who spoke, in any wording, as long as it names the four silent attendees and never reports zero; reporting the header as claimed, with roles taken from the convener's narration.",
    "Promoting Gideon Ashworth-Pell alone to the named risk row (decision-shaped, silent, never addressed), while listing Anton, Saoirse and Lettie as silent attendees ranked by stake in the prep; treating any of the three as an additional risk row is acceptable if labelled by stake and not as decision-shaped.",
    "Reporting talk share by side with the loudest and quietest client speaker and the count of contributing client speakers, in words only (no end times exist); any figure within a point of the key's is fine, and the share is never presented as a quality measure.",
    "Recording the remake-rate conflict as both statements with speaker and location, kind conflict, unresolved, with a gap question naming the remake log; wording is free, but neither figure may be chosen, averaged or used in arithmetic.",
    "Logging the tier as superseded (Pro to Standard) with the earlier value kept in the log, or recording Standard with the correction noted inline, as long as no conflict entry is raised for it and preflight is told to verify.",
    "Keeping the $90,000 budget line and the $55,000 actual as two items in any layout, provided no sum, difference or supersession runs between them and only the actual enters the bleed.",
    "Grading R1 and R7 as met-with-residual with the residual named, or as Met with the same residual carried as a gap question, as long as the verdict is Discovery complete and the approver's relayed priorities never become his evidence; grading R7 Partial (verdict Nearly ready) is not accepted because every element is Met from the convener except the one that only the approver can supply, which the residual records.",
    "Grading P4 Trajectory as not-obtainable naming the Finance Controller, or as Missing with the same routing note; the gap must go to her list and not to the group.",
    "Recording the three departures and the late join from the quoted lines, and the design lead as presence unknown with the colleague's hedge quoted; recording him as departed is not accepted.",
    "Stating the bleed as $147,768 or 'about $148,000 a year' with the exclusions listed; the hedge on the materials line may be shown as $55,000-$56,000.",
    "Proposing a Work Management build with the five agreed pieces in either order and with either label ('core' or 'Work Management'), keeping quoting and the job number out by the client's exclusion, and asking the pre-build questions or listing them as assumptions to confirm on the 21st.",
    "Writing the next run-sheet with one room-wide open check-in per phase boundary and named check-ins as the only confirmations, listing the silent attendees ranked by stake with one direct question by name before the close; a sheet that directs every check-in to the convener fails.",
    "Presenting automations as one approval list with recipients named; running the change check before any build; working in English only.",
]
key["expected_leak_blocklist"] = [
    "Bleed total in every form: 147768, 147,768, $147,768, 148k, $148k, 'a hundred and forty-eight thousand', 'about a hundred and fifty thousand a year'.",
    "Bleed components: 71136, 71,136, $71,136, 'seventy-one thousand and change', 'thirteen sixty-eight a week'; 21632, 21,632, $21,632, 'four-sixteen a week', 'twenty-one, twenty-two thousand'; 55000, $55k, 'fifty-five, fifty-six', 56000; and the remake budget line 90000, $90k, 'ninety a year'.",
    "Loaded rates and cost inputs: 38, $38, 'thirty-eight an hour loaded'; 52, $52, 'fifty-two'; six hours a week, thirty-six hours, eight hours a week, sixteen hours a month, x52, and any phrase pairing hours with a rate or a yearly total; the crew rate once supplied.",
    "The remake-rate conflict and its speakers: 'one in ten', 'one in four', 'I would put money on that', 'we've never measured it', and any note that the sales manager and the production manager disagree.",
    "The invoicing figures as a failure: 'forty-one days', 41 days, 'a million two', $1.2M installed and uninvoiced, 'the line of credit', 'the cash position'; the 41-day average may appear only as a process fact in an SOP if the user allows it.",
    "The Quarrington and university library stories as failure narratives: 'eleven of the twenty-two were the wrong size', 'twenty-two arrows pointing the wrong way', 'nineteen backwards arrows', the regional director in the lobby, and 'It was one of mine.'; the customers may be named as jobs, not as self-inflicted losses.",
    "Stakeholder assessments and decision power: 'Over twenty it's Gideon, full stop', the $20,000 threshold, 20000, $20k; 'here to listen', 'don't expect a lot out of him', 'He's nodding', 'he never does'; 'If the numbers are on one page, he's fast'; 'Fergus will never forgive me'; 'she'd rather it didn't'.",
    "Remarks about colleagues and silence: the coordinator who owned the error, 'Fergus is' style characterisations, the design lead having possibly dropped, the branch's 'we'll quietly keep ours', 'Mostly.', 'It was in my car.', and any statement that a named person never spoke or was not addressed.",
    "Objection text and planned responses: 'The floor won't touch a tablet with gloves on', 'it's dead by the second week', 'another thing to keep up to date', 'we like it that way', 'Nothing touches the accounting system before November', and the objection names themselves.",
    "Readiness and gate language: R1-R12 and their names, met-with-residual, not-obtainable, advisory, 'Discovery complete', 'Nearly ready', 'Not ready', excavated, gate, gap question, voices heard, voices missing, risk row.",
    "Method vocabulary and markers: bleed, upside, callback, exit ramp, seed data, readiness, pain IDs (P1-P4), conflict, superseded, the asked flag, and the [Q], [Q?], [Q/side], [I], [X] markers.",
    "Internal artefacts: the intake report, the call summary, the raw transcript and its timestamps, the record and log, the deferred-answers register, and any 'if asked' note.",
    "Pricing material of any kind, including a per-seat figure: the promised straight answer on seats is routed to the user and never drafted as a price.",
    "The pharmacy customer's identity in any form, including guesses; the auditors; the unnamed regional health system framework as a sales target.",
    "Consulting brand and product names: the consultant appears as 'Consultant' only; no plugin, tool or brand name of the Consultant's in the account or client-facing text; client tools stay as category words.",
    "Flag, do not remove (volume and process facts legitimate in an SOP, worth checking first): about 95 people; six coordinators, five designers, two production leads, six crews; 60-70 quotes a week and about a third won; 240-ish live jobs and 110-115 on the floor; the floor board columns print, cut, fab, paint, assembly, ready; 140 stores, five states, the week of February ninth to June; three sign types per store; the weekly status; Wednesday the 21st.",
]

# ---- intake block (calibration) ----
spoke = ["Consultant", "Delphine Castellane", "Rosalind Achebe", "Henrike Solano", "Bronwyn Tsai", "Calum Fairweather", "Fergus Lindqvist", "Emeric Sandoval", "Kwame Oduya", "Yolanda Brekke"]
silent = ["Gideon Ashworth-Pell", "Anton Petrakis", "Saoirse Nakamura", "Lettie Havlicek"]
key["intake"] = {
    "fixture_class": "calibration fixture (WP18): REAL-CALL-LESSONS.md C63 large-group; BUILD-PLAN.md 4.2 row s20; guards reversal R6 (a cross-speaker conflict is never resolved by recency; only same speaker, same proposition, one call is superseded); scored by H46, H52 and H53",
    "export_family": "block export: '[HH:MM:SS] Name: text', one whole turn per line, start-only zero-padded stamps, strictly increasing, no end times, no join or leave events, a two-line participant header of display names with no roles; label shape uniform; two '[inaudible]' and two '[crosstalk]' markers, no ellipsis except one arithmetic pause; no composite block is structurally present and no shred is present, so both detectors run and neither fires",
    "type_header": {
        "proposed": "discovery; seat partner-led; relationship new logo; direction of show nobody shows; output class configured structure; room shape large group (13 client attendees listed, 9 spoke); money live in the room: yes, the approver listed and silent, seat count and tier stated, the spend threshold stated after three people had left",
        "signals": [
            dict(Q("con_walk", "Let's walk a job, then, from the first phone call to the invoice, and I'd like each of you to take your own part."), dimension="agenda sentence, accepted by the client's next turns: discovery"),
            dict(Q("del_scope_agree", "That's the right shape."), dimension="output class: boards, views and a printed ticket accepted; no code, module or renderer mentioned by the client: configured structure"),
            dict(Q("tier_turn", "Standard. Twenty-five seats on Standard."), dimension="commercial marker: tier and seat count, speaker the convener, hedge state self-corrected in the turn"),
            dict(Q("del_decision", "Over twenty it's Gideon, full stop."), dimension="commercial marker: who approves spend, stated with the approver present and silent"),
        ],
        "note": "Proposed with quotes, never decided; every dimension resolved, so no criterion is advisory. No screen was shared and nothing is quarantined as [X].",
    },
    "roster": {
        "source": "export header, claimed not observed; roles from the convener's narration at " + T("gideon_intro") + " and " + T("roster_roles") + ", recorded observed-but-partial",
        "listed": 14, "client_listed": 13, "spoke": spoke, "client_spoke": 9, "silent": silent, "unlisted_speakers": [],
        "voices_line": "voices heard: 9 of 13 client attendees; voices missing: Gideon Ashworth-Pell, Anton Petrakis, Saoirse Nakamura, Lettie Havlicek (never 'none')",
        "role_evidence": [
            dict(Q("gideon_intro", "Gideon's our MD, he said he's here to listen, so don't expect a lot out of him."), name="Gideon Ashworth-Pell", titled="Managing Director, behaves as silent listener"),
            dict(Q("roster_roles", "Anton's from our IT provider, so nobody promises anything about passwords."), name="Anton Petrakis", titled="IT provider (guest)"),
            dict(Q("roster_roles", "Saoirse's here from HR because whatever we pick, the training lands on her."), name="Saoirse Nakamura", titled="HR and training"),
            dict(Q("roster_roles", "And Lettie, who does the job tickets for the floor, so she lives this more than any of us."), name="Lettie Havlicek", titled="Production administrator"),
        ],
    },
    "silent_attendee_risk_rows": [
        {"name": "Gideon Ashworth-Pell", "titled": "Managing Director", "decision_shaped": True, "addressed_by_our_side": False, "our_side_asked_a_colleague_instead": L("con_asks_delphine_about_gideon"), "relayed_statements": [L("del_gideon_relay"), L("del_gideon_cares"), L("del_relayed_nod")], "repair": "named risk row in the readiness section; one direct question by name before the close of the next meeting; nothing relayed is attributed to him"},
    ],
    "silent_attendees_ranked_by_stake_for_the_prep": [
        "1. Gideon Ashworth-Pell: signs over $20,000; the only decision-shaped silent attendee; offered a direct question by name",
        "2. Anton Petrakis: access and security checklist; routed through the convener, never answered by us",
        "3. Saoirse Nakamura: training lands on her; routed through the convener",
        "4. Lettie Havlicek: prints the tickets, lives P1; a targeted question on her hours, through the convener",
    ],
    "talk_share": {
        "method": "by words only (no end times); the family emits whole turns so no merge, split or re-join preceded the count; shred index zero",
        "by_side": {"client": 71.9, "our_side": 28.1}, "client_speakers_contributing": 9,
        "loudest_client": "Delphine Castellane, 25.4 percent of all words (35.3 percent of client words)",
        "quietest_client_contributor": "Yolanda Brekke, 3.1 percent of all words (4.2 percent of client words)",
        "per_speaker_percent_of_all_words": {"Consultant": 28.1, "Delphine Castellane": 25.4, "Rosalind Achebe": 12.3, "Henrike Solano": 8.0, "Bronwyn Tsai": 6.6, "Calum Fairweather": 4.4, "Fergus Lindqvist": 4.2, "Emeric Sandoval": 4.1, "Kwame Oduya": 3.8, "Yolanda Brekke": 3.1},
        "longest_own_side_stretch": "179 words at " + T("con_scope_playback") + " (scope playback), under the 225-word proxy; no stretch over it",
        "client_interviewer": "none (the convener directs colleagues by name but her turns are not majority interrogative)",
        "standing_note": "share is never read as a quality proxy and has not tracked grading outcome in the calls seen so far",
    },
    "presence_changes_inferable_from_speech": [
        dict(Q("yol_join", "Sorry, sorry. The highway was shut at the river."), who="Yolanda Brekke", kind="late join, announced by the speaker"),
        dict(Q("bro_leaves", "That's me, I'm afraid. Auditors."), who="Bronwyn Tsai", kind="departure, announced by the speaker (hard stop stated at " + T("bron_hardstop") + "); last spoke " + T("bro_leaves")),
        dict(Q("fer_departure_reported", "Fergus has had to drop, by the way, he's got the Quarrington call at three."), who="Fergus Lindqvist", kind="departure, reported by a colleague; last spoke " + T("fer_withdraw_marker") if "fer_withdraw_marker" in LOCS else "departure, reported by a colleague; last spoke 00:32:04"),
        dict(Q("kwa_departure", "And I'm going with him, I'm on the same call."), who="Kwame Oduya", kind="departure, announced by the speaker"),
        dict(Q("eme_maybe_gone", "He may have dropped. He had a four o'clock print deadline. I'll ask him."), who="Emeric Sandoval", kind="NOT a departure: last spoke " + T("eme_why_not") + "; a colleague's hedged guess; recorded as presence unknown with the hedge quoted"),
        {"who": "Gideon Ashworth-Pell, Anton Petrakis, Saoirse Nakamura, Lettie Havlicek", "kind": "presence at any moment is the header's claim only; nothing in speech confirms or denies it"},
    ],
    "commercial_figures_and_who_was_present": [
        {"figure": "25 seats, Standard (self-corrected from Pro)", "location": L("tier_turn"), "present": "every listed attendee (the branch manager had joined at " + T("yol_join") + "); the four silent attendees by the header's claim"},
        {"figure": "per-seat cost question, deferred by our side", "location": L("kwa_seat_question"), "present": "every listed attendee; our answer at " + T("con_deferred_seats") + " is a deferral, converted to an owned commitment"},
        {"figure": "$20,000 approval threshold", "location": L("del_decision"), "present": "listed attendees minus Bronwyn Tsai, Fergus Lindqvist and Kwame Oduya; Emeric Sandoval unknown; the approver by the header's claim"},
    ],
    "conflicts": [
        {"kind": "conflict", "proposition": "share of jobs remade",
         "statements": [Q("fer_remake_rate", "Honestly? One in ten. One in ten jobs has something remade."), Q("ros_remake_rate", "It is not one in ten. From where I stand it's closer to one in four.")],
         "possibly_different_denominators": [Q("fer_remake_rate", "I say that as the person who has to explain it to the customer"), Q("ros_crosstalk", "It depends whether you count the ones we catch before they ship.")],
         "acknowledged_unmeasured": Q("del_never_measured", "We've never measured it. That's the honest answer."),
         "repair": "both statements kept with speaker and location in open-questions.md as kind conflict, marked unresolved, a conflict log entry, no superseded entry, no recency, no arithmetic on either figure; gap question: the remake log count for the last quarter with its denominator (owner Rosalind Achebe, one week); remake labour stays unquantified in the bleed"},
    ],
    "superseded": [
        {"speaker": "Delphine Castellane", "proposition": "monday plan tier", "location": L("tier_turn"), "earlier": "Pro ('we're on the Pro plan')", "later": "Standard ('We dropped to Standard in January when we trimmed the seats, I signed the renewal myself. Standard.')",
         "why_superseded": "same speaker, same proposition, one turn, one call: the only case the recency rule covers", "recorded_value": "Standard, client-stated, unverified until preflight", "log_entry": "superseded, with the earlier value and the turn; no conflict entry"},
    ],
    "unresolved_figure_pairs": [
        {"speaker": "Bronwyn Tsai", "location": L("bro_writeoff"), "figures": ["$90,000 a year budgeted for remake materials", "about $55,000-$56,000 actually written off on remake materials last year (hedged)"], "relationship": "two different items, budget and actual, stated so by the speaker ('Don't add them together, they're not the same thing.'); neither supersedes the other, no arithmetic between them, only the actual is a bleed input"},
    ],
    "not_conflicts": [
        {"pair": "Kwame Oduya 'it's about half' vs Henrike Solano 'It's not half'", "locations": [L("kwa_changeorder"), L("hen_not_half")], "handling": "the figure was withdrawn by its own speaker in the room (" + L("kwa_withdraws") + "); recorded as 'a lot' with no figure; no conflict entry"},
        {"pair": "Rosalind Achebe 'two hundred and something' vs Delphine Castellane 'Two-forty'", "locations": [L("ros_live_jobs"), L("del_240")], "handling": "a vague and a specific figure that agree; the floor's 110-115 is a different count; no conflict entry"},
    ],
    "deferred_answers_register": [
        {"question": Q("kwa_seat_question", "Are we going to end up paying per head for people who'd open it twice a month?"), "our_answer": Q("con_deferred_seats", "I'll put it in the recap with a straight answer."), "commitment": "owner the user; due with the recap, end of the day after the call; no figure drafted in the record; collides with no recorded blocker, so not escalated"},
    ],
    "second_hand_statements": [
        {"about": "Gideon Ashworth-Pell", "by": "Delphine Castellane", "locations": [L("del_gideon_relay"), L("del_gideon_cares"), L("del_relayed_nod")], "status": "relayed; recorded as the convener's words about him; never attributed to him, never evidence for R7's approver element, R6's leadership criterion or R12; no figure carried"},
    ],
    "composite_blocks": "none: end times absent and every unit is a whole labelled turn well under the wall-clock plausibility bound; the detector ran and did not fire",
    "wedges": "none: the family cannot produce them",
    "rejoined_sentences": "none: the two '[crosstalk]' turns are complete under their own labels and are quoted as such, never merged",
    "alias_map": [
        {"canonical": "Gideon Ashworth-Pell", "forms": ["Gideon", "our MD", "the MD", "he (in the convener's relayed statements)"]},
        {"canonical": "Anton Petrakis", "forms": ["Anton", "our IT provider (his firm, not him)", "Anton's firm"]},
        {"canonical": "Bronwyn Tsai", "forms": ["Bronwyn", "finance", "a Bronwyn number"]},
        {"canonical": "Yolanda Brekke", "forms": ["Yolanda", "Flint (as in 'She runs Flint', 'I ring Yolanda for hers')"]},
        {"canonical": "Ottoline (not on the call)", "forms": ["Ottoline", "Ottoline's team", "marketing"]},
    ],
    "confidence_per_unit": {"certain": 252, "probable": 4, "uncertain": 0, "unattributable": 0, "probable_lines": [L("yol_join"), L("fer_volume"), L("fer_crosstalk"), L("ros_crosstalk")], "rule": "the worst state travels to anything derived from the unit; nothing load-bearing rests on a probable unit"},
    "package_order": "not applicable: a single first-hand call",
    "second_hand_figure": "none: no figure was re-quoted from another call or seller; the relayed statements above carry no figure",
    "check_in_expectations_for_the_next_run_sheet": {
        "why": "the room holds attendees whose stake is not in the record (the managing director, the IT provider, HR, the production administrator), so the room-wide open check-in is permitted",
        "rule": "one room-wide open check-in per phase boundary, naming the topic and tolerating silence, from whoever is not driving the screen; named check-ins are the only confirmations; a sheet that directs every check-in to the convener fails (H52)",
        "precedent_on_this_call": L("con_open_checkin") + " produced P3 from a silent attendee whose stake our side had deferred at " + T("con_install_deferred"),
    },
}

# ---- serializer: depth-limited pretty printing so the key stays under 400 lines ----
def dumps(o):
    return json.dumps(o, ensure_ascii=True)


def render(obj, path=()):
    depth = len(path)
    ind = " " * (depth + 1)
    if isinstance(obj, dict):
        expand = depth == 0 or (path[0] in ("company", "numbers", "expected_verdict", "account_context", "expected_structures") and depth == 1) \
            or (path[0] == "rubric" and depth == 2) or (path[0] == "intake" and depth in (1, 2))
        if not expand:
            return dumps(obj)
        parts = []
        for k, v in obj.items():
            parts.append("%s%s: %s" % (ind, dumps(k), render(v, path + (k,))))
        return "{\n" + ",\n".join(parts) + "\n" + " " * depth + "}"
    if isinstance(obj, list):
        expand = depth == 1 or (path[0] == "rubric" and depth == 3) or (path[0] in ("company", "expected_verdict", "account_context", "expected_structures") and depth == 2) \
            or (path[0] == "intake" and depth == 2 and obj and isinstance(obj[0], (dict, str)) and path[-1] not in ("spoke", "silent", "unlisted_speakers", "probable_lines", "relayed_statements", "locations"))
        if not expand or not obj:
            return dumps(obj)
        parts = ["%s%s" % (ind, render(v, path + (i,))) for i, v in enumerate(obj)]
        return "[\n" + ",\n".join(parts) + "\n" + " " * depth + "]"
    return dumps(obj)


text = render(key)
json.loads(text)  # must be valid JSON
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(text + "\n")
print("fields:", list(key.keys()) == ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company", "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary", "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals", "objections", "commitments_and_next_steps", "traps", "requested_changes", "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict", "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist", "intake"])
print("lines:", text.count("\n") + 1, " rubric rows:", len(R))
