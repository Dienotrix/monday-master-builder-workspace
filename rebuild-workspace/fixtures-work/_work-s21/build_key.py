#!/usr/bin/env python3
"""Writes fixtures/s21-existing-account/answer-key.json.

Every quote is resolved against transcript.txt: it must be an exact substring of
exactly one line, and the location is taken from that line. The JSON is printed
compactly (all-scalar objects on one line) to stay inside the 400-line budget.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "..", "..", "fixtures", "s21-existing-account")
TRANSCRIPT = os.path.join(FIX, "transcript.txt")
OUT = os.path.join(FIX, "answer-key.json")

ROLES = {
    "Consultant": None,
    "Henrietta Weyland": "Director of Operations",
    "Bethan Tull": "Fieldwork Manager",
    "Idris Machado": "Recruitment Team Lead",
}

LINE_RE = re.compile(r"^\[(\d\d:\d\d:\d\d)\] ([^:]+): (.*)$")
LINES = open(TRANSCRIPT, encoding="utf-8").read().splitlines()
PARSED = []
for ln in LINES:
    m = LINE_RE.match(ln)
    assert m, ln
    PARSED.append((m.group(1), m.group(2), m.group(3)))

ERRORS = []


def loc(quote, speaker=None):
    if isinstance(quote, tuple):
        quote, speaker = quote
    hits = [(i, p) for i, p in enumerate(PARSED) if quote in p[2] and (speaker is None or p[1] == speaker)]
    if len(hits) != 1:
        ERRORS.append("%d hits for: %s" % (len(hits), quote))
        return "UNRESOLVED"
    ts, name, _ = hits[0][1]
    role = ROLES[name]
    return "%s %s (%s)" % (ts, name, role) if role else "%s %s" % (ts, name)


def E(quote, speaker=None):
    if isinstance(quote, tuple):
        quote, speaker = quote
    return {"quote": quote, "location": loc(quote, speaker)}


def Q(quote):
    """A quote that must exist but is cited without a location field (used inside notes)."""
    loc(quote)
    return quote


# ---------------------------------------------------------------- serializer

def is_scalar(v):
    return v is None or isinstance(v, (str, int, float, bool))


def dumps(obj, ind=0):
    """Top-level keys expanded; every list entry and every second-level dict key on one line."""
    pad = "  " * ind
    if ind >= 2 or is_scalar(obj):
        return json.dumps(obj, ensure_ascii=False)
    if isinstance(obj, dict):
        if not obj:
            return "{}"
        parts = ["%s  %s: %s" % (pad, json.dumps(k, ensure_ascii=False), dumps(v, ind + 1)) for k, v in obj.items()]
        return "{\n" + ",\n".join(parts) + "\n" + pad + "}"
    if isinstance(obj, list):
        if not obj:
            return "[]"
        parts = ["%s  %s" % (pad, dumps(v, ind + 1)) for v in obj]
        return "[\n" + ",\n".join(parts) + "\n" + pad + "]"
    return json.dumps(obj, ensure_ascii=False)


# ---------------------------------------------------------------- rubric helpers

def row(criterion, status, asked, asked_q, evidence, note):
    r = {"criterion": criterion, "status": status}
    r["evidence"] = [E(q) for q in evidence]
    r["note"] = note
    r["asked"] = asked
    if asked_q:
        r["asked_quote"] = E(asked_q)
    return r


C_AGENDA = "So, you emailed saying two things. You want the costing board Bethan's been building to actually get finished, and you want the recruiter side back in some form."
O_AGENDA_ANSWER = "That's it. And the costing piece is the bigger one, by a distance."
C_CLOCK = "The pricing on the renewal quote I sent you is held until the twentieth of November. That's my constraint, not yours, and I'm saying it so it's on the table and not a surprise."
C_MECH = "I'll send Bethan a booking link today, for forty-five minutes, just the two of us, where you walk me through the costing board cell by cell and I try the two approaches on a copy of it. Bethan, you pick the slot."
B_ASSENT = "Yes. Send it. I'll grab something next week, once the wave's started it goes quiet for me."
B_WALL = "But I can't get that number into a formula on the parent, and I can't get the Studies board to read it, and I've tried it four ways."
B_EIGHTY = "I'm, like, eighty percent there. It's the last bit."
B_SHARE = "Can I share my screen? It's easier if you just see it."
B_STOP = "Let me stop sharing. Hang on."
B_FRIDAY = "The costing sheet is my Friday. Every Friday. Four hours, sometimes five, just re-keying cells and checking the sums against each other."
O_RATE = "I don't carry loaded rates around in my head. That's Philippa's, and I'd rather she gave you the real number than I guessed at one."
C_FORTY = "Sure. If we said, I don't know, forty an hour just to --"
O_DONT = "Don't. Get it from Philippa."
O_FRICTION = "The honest thing is every time we wanted a label changed we had to email you and wait, and after a while people stopped asking."
O_CAUSE = "We didn't know how to do it ourselves and I'm not sure anyone was meant to."
O_STUDIES = "The Studies board is the thing that works. Every brief goes on it, the account leads live on it, and the Friday email goes out off it without anybody touching it."
O_FRIDAYMAIL = "Don't touch the Friday email. I mean that. The account leads would notice before I did."
O_INCENT = "Finance runs the Incentives board and Philippa would riot if anyone went near it."
I_DEAD = "The rota board's dead. It's still in there, but nobody's put anything on it in about a year."
I_BACK = "They went back to the sheet inside three months. Leonie was doing it twice, once on the board and once on the sheet, and the sheet won."
O_NODATE = "No. Honestly, no. There's no date. It's just been getting worse and I'm tired of it."
O_CHANGE = "What's changed is we picked up three, no, two new agency clients since the summer, and both of them want a costed brief back inside forty-eight hours. We've never worked like that."
O_LOSE = "If we keep doing it in the sheet we will lose one of them. Not might. Will. They've said so."
B_FARRADAY = "The Farraday one. The incentive line was in there twice, once per cell and once at the bottom, and I didn't catch it, and the number went to the agency doubled up on the incentives and light everywhere else, and we ate it."
O_SIX = "About six thousand, all in."
O_TIPPED = "End of the summer. It was the thing that tipped it, for me."
O_DELEGATE = "Bethan runs it. I am not going to be in the weeds on this one. But anything that touches the Studies board or the Friday email, I want to see it and say yes before it goes live."
O_SPEND = "Spend is mine, up to what Hamish set for systems this year. The renewal plus this is inside that, I think. I'd want to check the number before I say it out loud."
O_YOLANDA = "Philippa has to be fine with anything that goes near the Incentives board. She doesn't sign, but she can stop it."
O_CARD = "We don't do purchase orders for this. It goes on the card, same as the renewal. Then it's Beth's."
O_SHAPE = "That's the shape. The rota is a maybe until I've seen it. The rest, yes."
C_SHAPE = "Inherited. Bethan's costing board as it stands, the form, the cells as subitems, the cell totals."
B_MECH_OK = "Either of those would do it, honestly. The first one. I don't want to lose the form."
C_TWO_WAYS = "There are two ways I'd want to try. One, keep your cells as subitems and get the total onto the parent in a way the Studies board can read through a connection. Two, put the costing onto the Studies board itself and retire the second board."
O_PUT_IN_TOUCH = "I'll put you two in touch. Leave that with me."
O_NOTED = "Noted."
B_ACCESS = "No. It's in my own workspace. I'd have to add you, and I'll need to ask the IT people how you're meant to come in, they have opinions about guests."
B_SPLIT_A = "The other thing I want out of it, and this is the bit Henrietta actually cares about, is a monthly view per agency of what we costed against what --"
C_MMHM = "Mm-hm."
B_SPLIT_B = "-- against what it actually came in at. Costed versus actual. Because right now that's a question I get asked and can't answer."
I_LEONIE_ART = "Leonie's got the sheet down to a fine art, honestly. She'd rather keep it. That's the thing you're up against."
I_DONT_KNOW = "I genuinely don't. It's not something I've timed and I'd be making it up. Ask Leonie."
O_ASK_LEONIE = "Ask Leonie. Don't take a number from us on that."
B_NOT_TOOL = "I did wonder, honestly, whether it's just not the right tool for the costing bit."
O_SAME_SHEET = "When you send the renewal through, can the extra piece be on the same sheet? I'd rather sign one thing."
O_PRO = "We're on Pro, I think it's thirty-something seats, the renewal's got the actual number on it."
B_TEST_ROWS = "Ignore the numbers, those are made up, I put test rows in so the formulas had something to chew on."
O_NOW = "Now. The costing piece, now. I'm not going to put a date on it, we did that with the rota and it just moved."

# ---------------------------------------------------------------- the key

key = {}
key["scenario_id"] = "s21-existing-account"
key["call_type"] = "expansion"
key["purpose_of_this_fixture"] = (
    "Calibration fixture for C64: a renewal-shaped call with an existing client of ours. What we built about two years ago is partly live and loved (the Studies board with its Friday digest, the Incentives board that finance now owns) and partly lapsed (a recruiter rota board the recruiters abandoned inside three months for a spreadsheet). The client's fieldwork manager has built her own study-costing board with a form and subitem cells, hit a wall she names precisely (the subitem total cannot reach a formula on the parent or the live Studies board), guesses aloud that she is 'eighty percent there', and walks it on a shared screen mid-call. The only clock in the call is ours: the Consultant says the renewal quote's pricing is held until 20 November and the client answers 'Noted.' and moves on. It tests that the plugin (1) proposes the type header as expansion (seat partner-led, relationship existing client of ours, output class configured structure) with a working-session sub-trigger for the screen-share segment and applies no second mode and no working-session, prototype-review or scoping label, so the call chains discovery-check rather than the scope path (R9); (2) grades R1 Met early from the first minutes, as expansion mode expects, and records current wins to preserve with authorship, prior attempts with status and payer, incumbent friction with its client-attributed cause, and the client-built asset with the blocker in her words; (3) grades R3 met-with-residual on client-side change plus trigger with the missing client clock as a gap question, records the 20 November date as our own commercial clock, front-paged and owned, excluded from why-now and never read as client hesitancy; (4) reports the collision between that date and the closed pricing gate (R4 Partial, R12 Partial) with the missing steps scheduled back from it, while pricing itself stays outside the plugin; (5) grades R10 Met on a booking mechanism delivered on the call with a named owner, a stated purpose and the client's assent, while the same close in discovery or demo mode would be Partial and s2's 'I'll send something over' stays Missing (R4 of the reversal map); (6) keeps the bleed at effort-quantified, rate pending, refuses the Consultant's withdrawn 'forty an hour', names the finance controller as the role that holds the rate, and grades P2 Cost inputs not obtainable from this room, naming the recruitment coordinator; (7) files the prototype as the strongest buying signal rather than a build-it-ourselves objection, quotes no completion or effort figure for work on it until it has been read, and treats the screen share as the client's own frame with no [X] quarantine; and (8) proposes a Work Management blueprint as a delta against the client-built board, honouring the live map: the Friday digest and the Incentives board do-not-change, the Studies board change-with-own-yes, the dead rota board archived and never deleted."
)
key["transcript_format"] = (
    "Plain text, 262 lines, one speaker turn per line in the form '[HH:MM:SS] Speaker Name: text'. Timestamps are turn start times from [00:00:03] to [00:37:38]. No header lines, no participant block and no call date. Four speakers: 'Consultant', 'Henrietta Weyland' (Director of Operations), 'Bethan Tull' (Fieldwork Manager) and 'Idris Machado' (Recruitment Team Lead). About 4,730 spoken words; client share about 67% (Bethan 27%, Henrietta 26%, Idris 13%); the Consultant's longest turn is 83 words at [00:33:57]. A block export with no end times: the composite detector cannot qualify (short units, no wall-clock), the wedge detector does not apply, and only the sentence re-join runs. Artefacts: [laughs] three times, [crosstalk] twice (Idris joining, and a phone interruption), one [inaudible] inside an Idris turn, ' -- ' for interruptions and self-corrections, and one Bethan sentence split across two of her own lines by the Consultant's 'Mm-hm.'. The screen share runs from Bethan's 'Can I share my screen?' at [00:14:30] to 'Let me stop sharing.' at [00:21:26]. Two lines follow the goodbyes, recorded before the meeting ended. Relative dates fit late October 2026: 'the twentieth of November' is a Friday, 'next week' and 'the week after next' are relative to the unstated call date. Every location in this key is 'HH:MM:SS Speaker Name (role)', or 'HH:MM:SS Consultant', taken from the line the quote is on."
)
key["company"] = {
    "name": "Kelbrook Field Partners (called 'Kelbrook')",
    "industry": "Market research fieldwork agency: recruits respondents, runs qualitative and quantitative studies and pays incentives for research agencies and, sometimes, brands directly. The commissioning agency is 'the client' or 'the agency'.",
    "size": "About seventy people: 28 recruiters across two centres, five account leads, three fieldwork managers, a small analysis team, finance (one controller with a part-timer) and the office",
    "locations": "A main office (the recruitment room is on the third floor) and a second recruitment centre in Thornbury with six recruiters, opened this year",
    "current_tools": [
        "monday.com Work Management, Pro plan per the client ('thirty-something seats', hedged): the Studies board with a status column and a Friday digest automation to the account leads, the Incentives board run by finance, a dead Recruiter rota board built with the rest about two years ago, and Bethan's own Study costing board (form, one item per brief, cells as subitems, formula columns) in her own workspace",
        "The costing sheet: a spreadsheet copied per brief, one per fieldwork manager, with a separate copy on the finance side",
        "Leonie's recruiter rota sheet, colour-coded and photographed. The photo goes into the recruiters' group chat",
        "The accounting system, where invoices and 'actual' study cost live, run by Philippa",
        "The panel software, where respondent names, numbers and history live and stay",
        "Email, for briefs from agencies and for the Friday digest. The recruitment room's wall screen, which shows the phone queue today"
    ],
}
key["attendees"] = [
    {"name": "Henrietta Weyland", "role": "Director of Operations. Holds the spend for this and the renewal up to a systems figure the owner set (hedged: 'I think'); delegates the run to Bethan and reserves a yes on anything touching the Studies board or the Friday email. Sponsor of the prior build.", "side": "client", "decision_role": "approver (delegates the run; gate-holder on the live Studies board and Friday email; spend up to a hedged threshold, above it the owner)"},
    {"name": "Bethan Tull", "role": "Fieldwork Manager. Costs briefs in the sheet; built the Study costing board herself in her own workspace and named its wall; will run the work day to day and owns the prototype and the access to it.", "side": "client", "decision_role": "admin/owner and influencer (delegate; author of the client-built asset)"},
    {"name": "Idris Machado", "role": "Recruitment Team Lead. Runs the recruiters across both centres; owns the rota problem but not the rota sheet, which Leonie (recruitment coordinator, absent) keeps.", "side": "client", "decision_role": "influencer (end-user voice for the recruiters)"},
    {"name": "Consultant", "role": "monday.com consultant who built the prior rollout and runs the expansion call", "side": "consultant", "decision_role": "not applicable"},
]
key["expected_monday_products"] = [
    {"kind": "core", "why": "Work Management only, as a second strand inside the existing record. The costing piece is a delta against Bethan's own board: the cell total reaching the parent, the live Studies board reading it through a connection, and a per-agency monthly costed-versus-actual view, with the form kept. The recruiter week view is conditional on Henrietta seeing the approach first, is read from the Studies board's field dates, is shown on the recruitment room's screen, and holds sessions and recruiters, never respondents. The live map governs: the Friday digest automation and the Incentives board are do-not-change, the Studies board is change-with-own-yes (Henrietta's yes; read, not typed), and the dead rota board is archived. No CRM: the per-agency view is a view over studies, not a sales pipeline, and no Service: no queue was described. The tier is Pro by the client's statement, so no portfolio."},
]
key["rubric"] = [
    row("R1 Current state mapped", "met", True, "tell me what's actually live from what we did, and what isn't. Don't spare me.",
        [O_STUDIES, O_FRIDAYMAIL, I_DEAD, I_BACK, "Nobody, really.", "It's a board with a form on the front, one item per brief, and the cells are subitems.", "No. Studies, Incentives, the Friday email. The rota's dead, the costing board is Bethan's. That's the estate.", "Every brief gets costed in the sheet, and the sheet is a copy of a copy of a copy.", "Leonie does the sheet, colour codes it, and takes a photo of it. The photo goes in the group chat. That's the system."],
        "Met early, by 00:07:13, as expansion mode expects: the client states the estate in a few turns (what is live, what lapsed, what she built, who administers it, that nobody maintains the platform) and the rest is the two pains' process. Elements: process (brief to costed brief to invoice; rota sheet to photo), tools and connections (sheet, accounting system, panel software, none connected), time on their process (Bethan's Fridays) and time maintaining the platform ('Nobody, really.'), monday today and who built it (our build plus Bethan's board). A structure inventory exists from the screen share: prototype rows (form, item per brief, cells as subitems, cell formula, subitem summary, the failed formula, mirror, number column and dashboard attempts) in class client-built prototype, and spoken rows for the Studies board (status column, seven labels, field dates), the Incentives board and the dead rota board; current state is satisfiable without the prototype rows. Admin membership is hedged ('I think you're still an admin on it') and read live, never assumed."),
    row("R2 Pain made concrete", "met", True, "Noted. And where does it go wrong?",
        [B_FARRADAY, "Three weeks ago we had a Saturday session with two recruiters booked on it and neither of them knew. Twelve respondents turned up to an empty room and the account lead had to ring round apologising."],
        "Two pains excavated: P1 study costing (Stated, Concrete, Workaround Met, all from Bethan) and P2 the recruiter rota (Stated, Concrete, Workaround Met, all from Idris). Bethan's named wall is recorded in the client-built assets section, not as a third pain."),
    row("R3 Why now", "met-with-residual", True, "Fair. Is there anything on your side that puts a date on this? A wave, a contract, a year end?",
        [O_CHANGE, "We've always been a week. A week was fine. It's not fine any more.", O_TIPPED, O_NODATE],
        "Compound criterion graded element by element. Change: Met (two new agency clients since the summer wanting a costed brief inside forty-eight hours; 'three, no, two' is a self-correction, use two). Trigger event: Met (the Farraday study, mis-costed at the end of the summer, 'the thing that tipped it'). Clock: missing on the client side, and the Consultant asked. Met on change plus trigger; the missing clock is the residual and becomes one gap question for Henrietta, not a Partial. The only date in the call, 20 November, is the Consultant's own renewal-pricing hold: recorded in the separate commercial clock (our side) field, front-paged as an owned to-do, and excluded from this criterion. Henrietta's 'Noted.' is a backchannel and evidence of nothing."),
    row("R4 Bleed number", "partial", True, "What's that time worth, roughly? Do you carry a loaded rate for a fieldwork manager?",
        [B_FRIDAY, "Every Friday. And the other two fieldwork managers do the same for theirs, less than me, they've got fewer cells, call it half that each.", "Between the three of us we cost, what, twelve, fifteen briefs a month? Fifteen in a busy month.", O_RATE, O_DONT, I_DONT_KNOW],
        "State: effort-quantified, rate pending. Bethan scopes her hours to the pain in one clause with an explicit referent ('The costing sheet is my Friday'), so no separate attribution quote is needed: 4-5 h/wk for her, about half that for each of the other two fieldwork managers (hedged), over 12-15 briefs a month (12 normal). The rate is not in the room: Henrietta holds no loaded rate and routes it to Philippa, the finance controller, which is the role the obtainability map names; the Consultant's 'forty an hour' was withdrawn on the spot and counts for nothing. The rota side has no hours at all (P2 Cost inputs not obtainable). Scale is reported as filled with the missing multiplier named: the loaded rate. The Farraday loss ('About six thousand, all in', currency not stated) is a one-off, excluded. Every study is costed 'at least twice' (client-interviewer exchange, Henrietta asking Bethan) is a frequency fact, reported and not grade-changing. Verdict consequence: Nearly ready."),
    row("R5 Upside number", "partial", True, "If a costed brief went back in a day instead of a week, what does that do for you?",
        ["We'd stop losing the short-notice ones. I'm not going to put a number on that today, I'd be guessing.", "It's more than I'd like to say out loud without checking."],
        "The upside is named (winning the short-notice briefs, keeping the two new agency clients) and explicitly unvalued; Henrietta declines to guess and the plugin must not fill it. Bethan's 'It's more than you'd think.' is not a figure."),
    row("R6 Desired outcome", "met", True, "Imagine this is running well in the spring. What's different in a normal week?",
        ["A brief comes in, Bethan costs it once, in one place, and the number that goes to the agency is the number Philippa sees. That's it. That's the whole thing.", "Meaning I don't care where, as long as there's one of it. If the number's on Beth's board and the Studies board shows it and Philippa reads it off the same thing, that's one place. If it's three files that agree, that's not.", "And I get my Fridays back.", "And the recruiters can see their week without Leonie retyping it.", "Hamish just wants to stop hearing about the sheet. That's his win condition, if you want one."],
        "Day to day from all three: one costing in one place, the agency's number equals finance's number, Bethan's Fridays back, recruiters seeing their week. Leadership win relayed by Henrietta from Hamish (the owner, absent): 'stop hearing about the sheet'. Draft success criteria stay proposed; nothing was agreed as a measure."),
    row("R7 Decision process mapped", "met", True, "Decision-wise. If we go ahead, who's involved, and who says yes?",
        [O_DELEGATE, O_SPEND, "Then it's a conversation with Hamish, and he'll say yes if it's the sheet. But I don't think it's over.", O_YOLANDA, O_CARD, "Same way. On the card, nobody blinked. The number was small enough that it never went near Hamish, and it won't this time either unless the two of you go mad."],
        "A delegation graph, not a flat list. Delegate: Bethan runs it. Gate-holder: Henrietta, gate condition 'anything that touches the Studies board or the Friday email', re-entry trigger 'before it goes live'. Spend: Henrietta up to the owner's systems figure, hedged ('I think', 'I'd want to check the number'); above it, Hamish (absent, relayed). Second gate-holder: Philippa on anything near the Incentives board ('She doesn't sign, but she can stop it.'). After a yes: on the card, no purchase order, then it is Bethan's; prior budgeting: the rota build went the same way. The approver is present and holds the budget; the check-with-someone objection is anticipated for the threshold only."),
    row("R8 Priority and timing", "partial", True, "I'll take it. Is this something for this quarter, or later on?",
        [O_NOW, "Yes. The costing piece, yes, today. The rota, show me."],
        "Priority is explicit and top ('Now. The costing piece, now.') and timing is explicitly refused ('I'm not going to put a date on it'), so the criterion is present but short of a target date. Do not fill the missing date with the Consultant's 20 November hold: that date is ours. The wave blackout ('the last two weeks of a wave') is a constraint on when work can land, not a client deadline."),
    row("R9 Blockers surfaced", "met", True, "What could stop it? Honestly.",
        ["The recruiters, we've talked about. The IT people and how you get in. And Philippa, if she thinks it touches her board.", ("And the wave.", "Idris Machado"), I_LEONIE_ART, B_ACCESS, "The one thing is recruitment can't take anything new in the last two weeks of a wave, and there's one starting the week after next. So whatever we do, it's not then."],
        "Four blockers named by the client: recruiter adoption after the rota backslide; how the Consultant gets access (the outsourced IT people's guest policy, a client-policy question the plugin never answers itself); Philippa stopping anything near the Incentives board; and the wave blackout. Mitigations raised on the call: Leonie in the room when the rota is built, Henrietta's yes before anything touches Studies, access asked of IT by Bethan."),
    row("R10 Next step committed", "met", True, C_MECH,
        [B_ASSENT, C_MECH, O_PUT_IN_TOUCH, "I'll add you to the board once the IT people come back to me. Might be a few days."],
        "Met under expansion mode on a booking mechanism, not a date: the Consultant delivers the mechanism on the call (a booking link sent today), names the owners (Consultant sends, Bethan picks the slot), states the purpose (walk the costing board cell by cell and try the two approaches on a copy) and Bethan assents ('Yes. Send it.'). No date, no time and no invite exists, and nothing is keyed on post-call calendar state. The same close on a discovery or demo call would grade Partial, and s2's 'I'll send something over' still grades Missing: the mechanism state applies to working-session and expansion modes only. The rate conversation is a separate item: 'I'll put you two in touch' is scheduling handed off to a named owner (Henrietta) without a mechanism, Partial-plus, and emits a same-day date-proposal to-do. The Consultant's line is the one admissible piece of our-side R10 evidence."),
    row("R11 Solution confirmed", "partial", True, C_TWO_WAYS,
        [B_MECH_OK, "Because the account leads will fill in a form. They will not open a board and add an item. I've watched them not do it."],
        "Mechanism-confirmed, not solution-confirmed: nothing built was shown. The Consultant described two approaches with nothing on screen but Bethan's own board, and Bethan chose the first (cells stay subitems, the total reaches the parent, the Studies board reads it through a connection, the form stays). Graded weaker than a screen confirmation and re-confirmed against the built artefact before sign-off; P2 has no confirmation at all (Henrietta: 'show me')."),
    row("R12 Scope agreed verbally", "partial", True, "After, I think, but let me play back what I think the whole shape is, and tell me where I'm wrong.",
        [C_SHAPE, O_SHAPE, "One condition on the Studies board. No new columns the account leads have to fill in. They fill in the form and they read the status, that's all they'll do, and I'm not going to make them do more.", "Yes to that. Show her how and then it's hers.", "Fine. Whatever gets it out of the sidebar."],
        "The scope was read back as a delta in four parts (inherited: Bethan's board, form, cells, cell totals; in scope: parent total, Studies reading it, per-agency monthly costed-versus-actual view, a recruiter week view; client-side change: Bethan adds the Consultant, Idris sends Leonie's columns; access unlock: whatever the IT people say). Henrietta confirmed the costing half with a condition (Studies is read, not typed), left the rota a maybe, and the access unlock is unresolved. Partial: enough to blueprint the costing strand, not enough for a proposal, and no figure until the board has been read. The label self-service ask and the rota archive were agreed as changes to live objects with Henrietta's yes."),
    row("P1 Stated", "met", True, "So, costing. Bethan, walk me through it as it is today, before your board. Where does a brief start?",
        ["And costing it means the sheet. Every brief gets costed in the sheet, and the sheet is a copy of a copy of a copy. There's no version of it that's the real one.", "And the number the client gets is not the number finance sees, because they're two different sheets by then."],
        "P1: briefs are costed in a copied spreadsheet with no single version, and the agency's number diverges from finance's."),
    row("P1 Concrete", "met", True, "Noted. And where does it go wrong?",
        [B_FARRADAY, O_SIX, "Once a study. Nearly every study. The agency comes back with one more audience, or the brand wants a boost sample, and it's a fifth cell."],
        "The Farraday study at the end of the summer: the incentive line counted twice, the number sent doubled on incentives and light elsewhere, about six thousand absorbed (currency not stated), the corrected version done at eleven at night. Day to day: nearly every study gets a late cell and is costed at least twice."),
    row("P1 Workaround", "met", False, None,
        ["I open the brief email. I copy each cell into the sheet, n, incentive, recruit cost, by hand, because the agencies all send it differently.", "And the version of the sheet Philippa has is a different file. It's the same sheet, it's just not the same file.", "Which is partly why I built the costing thing on my own. I didn't want to email and wait.", B_WALL],
        "Volunteered, not asked. Today: the sheet re-keyed by hand from the brief email, checked against last month's copy, the total typed onto Studies and emailed anyway, a different file on the finance side, and Bethan's own board that stops at the roll-up. Why it will not do: three files that do not agree, a doubled line nobody caught, and a board she cannot finish."),
    row("P1 Reach", "met", True, "Okay, twelve to fifteen. And who else is stuck while that's happening?",
        ["The account leads sit on their hands until I'm done, because they can't send a number they haven't got. And then Philippa re-keys the whole thing into the accounting system for the invoice, so it's typed three times before anyone gets paid."],
        "Account leads wait, finance re-keys, the agency gets a late or wrong number, the owner hears about it."),
    row("P1 Cost inputs", "met", True, "How long does the sheet take you, a normal week?",
        [B_FRIDAY, "Between the three of us we cost, what, twelve, fifteen briefs a month? Fifteen in a busy month.", "At least twice. Some of them three times."],
        "Hours attached in one clause by the person who does the work: 4-5 h/wk (Bethan), about half each for two colleagues (hedged), 12-15 briefs a month, each costed at least twice. The rate is pending with finance, which is R4's gap, not this check's."),
    row("P1 Trajectory", "met", True, "And if it stays as it is?",
        [O_LOSE, "In a review. Politely. But yes."],
        "Henrietta: one of the two new agency clients will be lost if costing stays in the sheet; said in a review."),
    row("P2 Stated", "met", True, "Idris, the recruiters. Tell me where it is.",
        ["So the recruiters don't know their week until Leonie's done the sheet, and Leonie doesn't do the sheet until the field dates are in, and the field dates move."],
        "P2: the recruiter rota lives in Leonie's sheet, always late and wrong somewhere, after the board built for it lapsed."),
    row("P2 Concrete", "met", True, "What does wrong look like?",
        ["Three weeks ago we had a Saturday session with two recruiters booked on it and neither of them knew. Twelve respondents turned up to an empty room and the account lead had to ring round apologising.", "The field dates moved on the Wednesday. The Studies board had the new dates, because the account lead changed them, which is right. Leonie's sheet had the old ones, because nobody told her. And the photo in the chat was from the Monday. The two things don't know about each other."],
        "Three weeks before the call: a Saturday session nobody staffed after the field dates moved on Studies and the photographed sheet did not; twelve respondents in an empty room; it reached the owner."),
    row("P2 Workaround", "met", True, "How does the sheet work, day to day?",
        ["Leonie does the sheet, colour codes it, and takes a photo of it. The photo goes in the group chat. That's the system.", "When she was off for a week in the summer nobody could read the colours and we lost two sessions.", "A second copy. For Thornbury. Which is exactly what we said we wouldn't do."],
        "Today: Leonie's colour-coded sheet photographed into the group chat, the recruiters reading the photo, the dead board ignored. Why it will not do: unreadable without Leonie (two sessions lost when she was off), it does not know the Studies board's dates, and Thornbury means a second copy. The '[inaudible]' unit is uncertain and corroborated by the repeat that follows it."),
    row("P2 Reach", "met", True, "Who else ends up dealing with it when it goes wrong?",
        ["The recruiters, obviously. The respondents, who've given up a Saturday. And whichever account lead has to ring the agency and explain.", "That one got to Hamish."],
        "Recruiters, respondents, the account lead who rings the agency, and the owner."),
    row("P2 Cost inputs", "not-obtainable", True, "How long does the sheet take Leonie, do you know?",
        [I_DONT_KNOW, O_ASK_LEONIE],
        "Not obtainable from this room. The Consultant asked; Idris will not guess and Henrietta tells the Consultant not to take a number from them. The role that could supply it is the recruitment coordinator (Leonie), who keeps the sheet and was not on the call. Routes to a room change (Leonie in the rota session), not to the same question again, and nothing is inferred from Idris."),
    row("P2 Trajectory", "partial", True, "I won't. And if nothing changes, a year from now?",
        ["It'll be worse with the second centre, probably. Thornbury's got its own recruiters and they'll want the same sheet. I don't know."],
        "Hedged both ways ('probably', 'I don't know'): a second copy of the sheet for Thornbury is the direction, with no confident forward statement. Keep the hedge."),
]
key["pains"] = [
    {"quote": "There's no version of it that's the real one.", "location": loc("There's no version of it that's the real one."), "theme": "P1 Briefs costed in a copied spreadsheet with no single version"},
    {"quote": B_FARRADAY, "location": loc(B_FARRADAY), "theme": "P1 A mis-costed study absorbed at the firm's cost (the trigger)"},
    {"quote": "And the number the client gets is not the number finance sees, because they're two different sheets by then.", "location": loc("And the number the client gets is not the number finance sees, because they're two different sheets by then."), "theme": "P1 The agency's number and finance's number diverge"},
    {"quote": "Once a study. Nearly every study. The agency comes back with one more audience, or the brand wants a boost sample, and it's a fifth cell.", "location": loc("Once a study. Nearly every study. The agency comes back with one more audience, or the brand wants a boost sample, and it's a fifth cell."), "theme": "P1 Late cells mean every study is costed at least twice"},
    {"quote": B_WALL, "location": loc(B_WALL), "theme": "P1 The client-built costing board stops at the roll-up (the named wall; recorded under client-built assets, not as a separate pain)"},
    {"quote": B_SPLIT_B, "location": loc(B_SPLIT_B), "theme": "P1 No costed-versus-actual view per agency (desired outcome, part of P1's scope)"},
    {"quote": "So it's always late and it's always wrong somewhere.", "location": loc("So it's always late and it's always wrong somewhere."), "theme": "P2 The recruiter rota is late and wrong"},
    {"quote": "And the recruiters look at the photo. Not the board. The board's never had the sessions on it.", "location": loc("And the recruiters look at the photo. Not the board. The board's never had the sessions on it."), "theme": "P2 The rota sheet and the Studies board do not know about each other"},
    {"quote": O_FRICTION, "location": loc(O_FRICTION), "theme": "Changing what we built needs an email to us (incumbent friction; recorded as an embedded objection, not graded as a pain)"},
]
key["numbers"] = {
    "bleed": {
        "value": "Effort-quantified, rate pending (Partial). Volume and frequency: Bethan 4-5 h/wk on the costing sheet, the other two fieldwork managers about half that each (hedged), 12-15 briefs a month (12 normal), each costed at least twice. Rate: none; Henrietta holds no loaded rate and routes it to Philippa, the finance controller. Missing multiplier: the loaded hourly cost. Rota hours: not obtainable from this room (Leonie). Excluded: the roughly six-thousand Farraday loss (one-off; currency not stated), the Consultant's withdrawn 'forty an hour', and any lost-client value (unquantified).",
        "quote": B_FRIDAY,
        "status": "partial",
    },
    "upside": {
        "value": "Named, unvalued (Partial): winning the short-notice briefs and keeping the two new agency clients that want a costed brief inside forty-eight hours. Henrietta refuses to guess a figure and the plugin must not supply one.",
        "quote": "We'd stop losing the short-notice ones. I'm not going to put a number on that today, I'd be guessing.",
        "status": "partial",
    },
}
key["vocabulary"] = [
    {"their_term": "brief", "meaning": "A request for fieldwork from an agency; one item on the Studies board and one item on the costing board. 'Study' is the same thing once it is running; confirm before naming anything", "likely_monday_object": "item on the live Studies board; item on the costing board (inherited)"},
    {"their_term": "cell", "meaning": "An audience group within a study with its own n, incentive, recruit cost and moderation hours. Agencies sometimes say 'quota' for the same thing. Not a spreadsheet cell", "likely_monday_object": "subitem on the costing board (inherited)"},
    {"their_term": "n", "meaning": "Sample size of a cell; comes from the brief and changes when the screener is signed off", "likely_monday_object": "number column on the subitem (inherited)"},
    {"their_term": "incentive / incentive per head", "meaning": "What a respondent is paid; a cost line per cell. Payment itself is finance's, on the Incentives board and in the accounting system", "likely_monday_object": "number column on the subitem (inherited); the Incentives board is do-not-change"},
    {"their_term": "recruit cost per head", "meaning": "Cost of recruiting one respondent for a cell", "likely_monday_object": "number column on the subitem (inherited)"},
    {"their_term": "moderation hours", "meaning": "Qual-only cost line; filled on a quant study by mistake", "likely_monday_object": "number column on the subitem (inherited); a qual/quant type would drive which lines apply"},
    {"their_term": "qual / quant", "meaning": "Qualitative (small n, moderation) and quantitative (large n, no moderation) studies", "likely_monday_object": "status or dropdown column"},
    {"their_term": "costed brief / costing", "meaning": "The priced brief sent back to the agency; today a spreadsheet, tomorrow the parent total", "likely_monday_object": "the parent total on the costing board, read by the Studies board"},
    {"their_term": "costed versus actual", "meaning": "What was costed against what the study came in at; 'actual' lives in the accounting system", "likely_monday_object": "a per-agency monthly view; the actual side is an open question"},
    {"their_term": "the sheet", "meaning": "Two different things: the costing spreadsheet (Bethan) and Leonie's rota spreadsheet (Idris). Confirm which before naming anything", "likely_monday_object": "none (replaced)"},
    {"their_term": "the Studies board", "meaning": "The live board we built: one line per study, the status column the account leads read", "likely_monday_object": "existing board, change-with-own-yes"},
    {"their_term": "the Friday email", "meaning": "The digest automation off the Studies board to the account leads and Henrietta", "likely_monday_object": "existing automation, do-not-change"},
    {"their_term": "the Incentives board", "meaning": "The board finance runs: who is owed what and whether it is paid; no bank details", "likely_monday_object": "existing board, do-not-change"},
    {"their_term": "the rota / the rota board", "meaning": "Leonie's sheet of recruiter sessions, and the dead board built for it", "likely_monday_object": "the dead board archived; a recruiter week view, conditional"},
    {"their_term": "the costing board / the costing thing", "meaning": "Bethan's own board in her own workspace: form, item per brief, cells as subitems", "likely_monday_object": "inherited client-built board; the strand's starting point"},
    {"their_term": "account lead", "meaning": "Owns the agency relationship, puts the brief on Studies, fills in the form, sends the number", "likely_monday_object": "people column"},
    {"their_term": "fieldwork manager", "meaning": "Costs briefs and runs studies; three of them", "likely_monday_object": "people column"},
    {"their_term": "recruiter / recruitment room / the big telly", "meaning": "The 28 recruiters across two centres; the room with the wall screen that shows the phone queue", "likely_monday_object": "a board view on the wall screen (sessions, rooms, recruiters, never respondents)"},
    {"their_term": "session", "meaning": "A fielding slot recruiters staff, such as a Saturday session", "likely_monday_object": "item on a recruiter week view"},
    {"their_term": "wave", "meaning": "A fielding period; recruitment takes nothing new in its last two weeks", "likely_monday_object": "none (a scheduling constraint)"},
    {"their_term": "field dates", "meaning": "When a study is in field; live on the Studies board and moved by the account lead", "likely_monday_object": "existing date or timeline column on Studies"},
    {"their_term": "screener", "meaning": "The recruitment questionnaire; n changes when it is signed off", "likely_monday_object": "none in scope"},
    {"their_term": "client / agency / brand", "meaning": "The commissioning research agency, or a brand direct; never the monday account", "likely_monday_object": "dropdown or text on Studies for the per-agency view; not a CRM Accounts board"},
    {"their_term": "code", "meaning": "The study code used on every board instead of the brand or study title", "likely_monday_object": "text column, typed twice today (form and Studies); the identifier question"},
    {"their_term": "the panel software", "meaning": "Where respondent names, numbers and history live and stay", "likely_monday_object": "none; never connected"},
]
key["entities_and_workflows"] = [
    "Brief intake: an agency emails or calls a brief; the account lead puts it on the Studies board with the study code and field dates",
    "Costing today: one of three fieldwork managers copies each cell (n, incentive per head, recruit cost per head, moderation hours if qual) from the brief email into the sheet by hand, checks the sums against last month's copy, types the total onto Studies and emails the account lead anyway; 12-15 briefs a month",
    "Late cells: nearly every study gains a cell after costing (a fifth audience, a boost sample), so each is costed at least twice",
    "Invoicing: Philippa re-keys the costed brief into the accounting system; 'actual' lives there and nowhere Bethan can see",
    "Bethan's costing board: form on the front filled by the account lead (brief name as the code, agency, field dates, number of cells), one item per brief, cells as subitems with a working cell-total formula, a subitem summary that cannot be read by a parent formula or by the Studies board; four failed attempts (parent formula, mirror, typed number column, dashboard)",
    "The Studies board: one line per study, a status column with about seven labels the five account leads read, field dates moved by account leads, the Friday digest automation to the account leads and Henrietta; admin membership hedged (the Consultant and Hamish 'I think')",
    "The Incentives board: finance's; who is owed what and whether paid; bank details stay in the accounting system",
    "The recruiter rota today: Leonie's colour-coded sheet, photographed. The photo goes into the group chat and the recruiters read it, never the board; the dead rota board has had nothing on it for about a year",
    "Waves and sessions: fielding periods with sessions (some on Saturdays) staffed by recruiters across the main office and the Thornbury centre; no new work in the last two weeks of a wave",
    "Respondent data: names, numbers and history stay in the panel software by agreement with the agencies' compliance people; a recruiter week holds sessions, rooms, recruiters and headcount only",
    "Buying process: Henrietta signs on the card up to the owner's systems figure (hedged); Hamish above it; Philippa can stop anything near the Incentives board; the prior rota build went the same way",
    "People mentioned but not on the call: Hamish (owner; relayed win condition), Philippa (finance controller; holds rates and the accounting system), Leonie (recruitment coordinator; keeps the rota sheet), the outsourced IT people (guest access policy), the two other fieldwork managers, the five account leads",
]
key["integrations_mentioned"] = [
    "The accounting system (finance): 'actual' study cost and invoices live there; no connection today, and any read is a question for Philippa, never assumed",
    "Email: briefs arrive by email; the Friday digest goes out by email (built, do-not-change)",
    "The costing spreadsheet and Leonie's rota spreadsheet: current data sources to be replaced; Idris sends a photo of the rota sheet's columns",
    "The panel software: respondent data; never to be connected or copied",
    "The recruitment room's wall screen: a browser that could show a board view (conditional recruiter week view)",
]
key["compliance_or_security_signals"] = [
    "Respondent personal data (names, numbers, history) stays in the panel software, agreed with the agencies' compliance people; nothing about respondents on any board",
    "Study codes, never the brand or the agency's study title, on every board",
    "Bank details and payment data stay in the accounting system; the Incentives board only says who is owed what and whether it is paid",
    "Guest and access policy belongs to the outsourced IT people: how the Consultant gets into Bethan's workspace is their call, asked by Bethan, never answered by us",
    "Admin and member roles on the account are hedged from memory and must be read live before anything is changed",
]
key["objections"] = [
    {"quote": O_FRICTION, "type": "Changing what you built for us costs us (embedded: stated as a fact about today by the person who lives it; client-attributed cause 'We didn't know how to do it ourselves')"},
    {"quote": I_LEONIE_ART, "type": "We'll build it ourselves (they maintain the current setup: the rota sheet, a risk)"},
    {"quote": B_WALL, "type": "Outside the map: internal builder who built a prototype, hit a wall and named it (a buying signal, not an objection; credit the work and name the missing piece; never filed as We'll build it ourselves)"},
    {"quote": B_NOT_TOOL, "type": "monday itself is the problem (raised, answered on the call by offering to check the setup on her board before saying either way)"},
    {"quote": I_BACK, "type": "Team won't adopt it (the prior backslide; raised as a blocker for the rota half)"},
    {"quote": O_SPEND, "type": "Must check with someone (the spend threshold is hedged and the owner is absent; the approver is present)"},
    {"quote": O_SAME_SHEET, "type": "Just send a proposal or pricing (raised; held: scope first and no figure until the board is read)"},
]
key["commitments_and_next_steps"] = [
    {"quote": C_MECH, "what": "Booking link for a 45-minute working session with Bethan: walk the costing board cell by cell and try the two approaches on a copy (the next step, R10)", "owner": "Consultant sends the link today; Bethan picks the slot", "date": "Link sent on the day of the call (date not stated); session next week, no date or time fixed"},
    {"quote": B_ASSENT, "what": "Book the session from the link", "owner": "Bethan Tull", "date": "Next week, relative to the unstated call date"},
    {"quote": O_PUT_IN_TOUCH, "what": "Put the Consultant in touch with Philippa for the loaded rate (scheduling handed off, no mechanism; same-day date-proposal to-do for the Consultant)", "owner": "Henrietta Weyland", "date": "Not set"},
    {"quote": "I'll send a short recap tomorrow, what I heard and the next steps, so you can correct anything I got wrong. And I'll say plainly in it that there's no number on the costing piece yet.", "what": "Recap draft for correction, stating that no figure exists yet", "owner": "Consultant", "date": "Day after the call (date not stated)"},
    {"quote": "I'll add you to the board once the IT people come back to me. Might be a few days.", "what": "Ask the IT people how the Consultant may be given access, then add the Consultant to the costing board", "owner": "Bethan Tull (policy answer from the IT people)", "date": "A few days; not set"},
    {"quote": "[laughs] A photo is literally how we do it. I'll send one today.", "what": "Send a photo of Leonie's rota sheet columns", "owner": "Idris Machado", "date": "Day of the call (date not stated)"},
    {"quote": "Happy to, once we've agreed what it covers, and I won't put a number on the costing piece until I've read Bethan's board. So it may be two sheets, or one sheet later. I'd rather it was right.", "what": "Renewal and expansion on one sheet, later, once scope is agreed and the board read (pricing itself is outside the plugin; the collision with the 20 November hold is scheduled back)", "owner": "Consultant", "date": "Not set; after the working session and the rate"},
    {"quote": "Yes to that. Show her how and then it's hers.", "what": "Hand over label editing on the Studies board to Bethan (a change to a live object with Henrietta's yes)", "owner": "Consultant, with Henrietta's approval", "date": "Not set"},
    {"quote": "I'd archive it rather than delete it, so it's out of the way and still there if anyone asks.", "what": "Archive the dead rota board (never delete)", "owner": "Consultant, at the approval stop", "date": "Not set"},
    {"quote": "I'd want to check the number before I say it out loud.", "what": "Soft: Henrietta checks the systems figure the renewal plus the expansion must fit inside", "owner": "Henrietta Weyland", "date": "Not set"},
]
key["traps"] = [
    "Type: expansion, proposed with the agenda sentence and Henrietta's answer, never decided by the plugin. The screen share is a working-session sub-trigger (a client-built artefact present and technical work performed on it), not a second mode: no working-session, prototype-review or scoping label, no second criterion set, and the call chains discovery-check rather than the scope path.",
    "Current state is Met early, by 00:07:13, from a few turns about the estate; do not grade R1 Partial for want of a full walkthrough, and do not re-ask what the prior build already established.",
    "The 20 November date is the Consultant's: our commercial clock, front-paged as an owned to-do, excluded from R3, never presented as urgency or client hesitancy in a recap. Henrietta's 'Noted.' is a backchannel and evidence of nothing.",
    "The pricing gate is closed (R4 Partial, R12 Partial; R7 Met) and a commercial date exists, so the front page shows the collision with the missing steps scheduled back from 20 November: the working session, the rate from Philippa, the scope read-back with Henrietta, then pricing prep, which is not part of this plugin.",
    "R10 is Met on a mechanism only because the mode is expansion; the same close in discovery or demo mode grades Partial (no date, no time, no invite), and s2's 'I'll send something over' stays Missing. Do not convert on post-call calendar state.",
    "'I'll put you two in touch' is scheduling handed off to a named owner without a mechanism: Partial-plus, with a same-day date-proposal to-do; it is not Met and not the next step.",
    "'Eighty percent there' is Bethan's own guess about her own board; it is recorded in the client-built assets section and never becomes a completion, effort or duration figure from us. No figure is quoted for work on the board until it has been read; the Consultant's refusal to give one is the expected behaviour.",
    "Bethan's prototype with its named wall is the strongest buying signal, filed as the internal-builder signal row (built a prototype, hit a wall and named it) and answered by crediting the work and naming the missing piece; Leonie's sheet is the build-it-ourselves risk. Do not file the prototype under 'We'll build it ourselves'.",
    "The Consultant's 'forty an hour' was withdrawn and refused ('Don't. Get it from Philippa.'); it counts for nothing. The bleed is effort-quantified, rate pending; the rate's role is the finance controller.",
    "P2 Cost inputs is not obtainable from this room: the recruitment coordinator keeps the sheet and was absent. Do not infer Leonie's hours from Idris or Henrietta, and route the question to a room with Leonie in it.",
    "The roughly six-thousand Farraday loss (currency not stated) is a one-off, not a bleed input; 'we ate it' and the eleven-at-night correction stay internal.",
    "'Cell' is an audience group, not a spreadsheet cell; 'the sheet' is two different spreadsheets (costing, rota); 'client' is the commissioning agency; 'brief' and 'study' are one item at two stages. Confirm before naming anything.",
    "The live map governs: the Friday digest and the Incentives board are do-not-change (quoted from Henrietta), the Studies board is change-with-own-yes (Henrietta's gate: 'read, not typed'), and an element that collides with do-not-change is a fork carried open, never a silent change.",
    "Authorship of the live estate is ours: the Studies board, digest, Incentives board and the lapsed rota board were built by the Consultant, so each current win is both the trust asset and the latent objection; incumbent friction is recorded with its client-attributed cause, and the change path (self-service labels) is a requested change, not a courtesy.",
    "Prior attempts carry a status axis and a payer axis: the rota board lapsed (client paid, still in the account, nothing on it for about a year); the Studies and Incentives boards did not lapse. Nothing else failed.",
    "The dead rota board is archived, never deleted, and never silently reused; a recruiter week view is built only after Henrietta has seen the approach, is read from the Studies board's field dates, and holds sessions, rooms, recruiters and headcount, never respondents.",
    "Bethan's screen share is the client's own frame, so no [X] quarantine applies to what she narrated; her test rows are not client figures either, because she said they are made up.",
    "Two approaches were spoken by the Consultant ('I've built the first before', 'not promising it until I've done it on a copy'): claims to the store as buildable and unverified respectively, never stated as capability in client-facing text, and the choice is Bethan's mechanism-confirmation, not a build.",
    "The delegation graph is the decision structure: Bethan runs it, Henrietta approves anything touching Studies or the Friday email before go-live and holds spend to a hedged threshold, Hamish above it (absent), Philippa can stop anything near Incentives. A flat role list loses this.",
    "Tier is Pro by client statement with a hedged seat count ('thirty-something'); record the source and date, read it live at preflight, and do not read the renewal as an upgrade. No portfolio.",
    "The account is already bound and the record already exists: this is a second strand, not a new client; no new-account question, no native-board detection (no CRM or Service entity), and the blueprint's inventory marks Bethan's board pre-existing and inherited, never ours to overwrite.",
    "The study code is typed twice (form and Studies) and one with a space never lined up: an identifier question for the build, never answered with an 'as long as the names match' claim.",
    "The incentive field was text for a month and the dashboard showed 'a number I didn't trust': read the prototype's field types and formulas live before extending them.",
    "Respondent data stays in the panel software and bank details in the accounting system; nothing about respondents or payments enters any board, view or seed data.",
    "Relayed lines are not evidence of the absent person: Hamish's win condition, 'That one got to Hamish', Philippa 'would riot'. They shape questions and the do-not-change list, never a grade about them.",
    "The Consultant's two-approaches turn during the prototype walk is interrogation of a candidate solution, not a fix offered mid-pain; the delivery note must not flag it. The one client-interviewer moment (Henrietta asking Bethan how often a cell is added late) is reported and never changes a grade.",
    "The sentence split across two Bethan lines by the Consultant's 'Mm-hm.' is one sentence with one owner; cite it as two units or as a reconstruction with both locations, never as a single verbatim quote that crosses the Consultant's label.",
    "Idris's '[inaudible]' unit is uncertain; the requirement it carries (a second copy for Thornbury) is corroborated by his next line and originates nothing on its own. The two lines after the goodbyes (the Farraday invoice) are internal and never reach a recap.",
    "The call date is not in the transcript; 'the twentieth of November' fits Friday 20 November 2026 and 'next week', 'the week after next' and 'three weeks ago' are relative to the unstated late-October date. Self-corrections use the corrected value: 'three, no, two new agency clients'.",
]
key["requested_changes"] = [
    {"type": "change", "description": "Hand over label editing on the live Studies board so Bethan can change a label without emailing the Consultant; a change to a live object, approved by Henrietta on the call, planned as pre-existing-modified with its prior state read live.", "quote": "And I want to be able to change a label on the Studies board without emailing you."},
    {"type": "change", "description": "Condition on the Studies board: nothing new the account leads must type; anything that lands on Studies is read, not typed (the connection to the costing total and the field dates the rota view reads).", "quote": "One condition on the Studies board. No new columns the account leads have to fill in."},
    {"type": "add", "description": "A recruiter week view on the recruitment room's wall screen, conditional on Henrietta seeing the approach first and on Leonie being in the room when it is built; sessions, rooms, recruiters and headcount, never respondents.", "quote": "But if it was on the screen in the recruitment room, the big one, and it was right, they'd use it."},
    {"type": "remove", "description": "Archive the dead Recruiter rota board (never delete; nothing on it has been real for a year), with Henrietta's yes since it is a live object of ours.", "quote": "And bin the old rota board. Nothing on it's been real for a year."},
]
key["should_plugin_propose_a_build"] = True
key["expected_questions_before_building"] = [
    "Access: what did the IT people say about how the Consultant is given access to Bethan's workspace and the costing board, and at what seat level; nothing is built or read until that answer arrives, and the plugin never proposes the policy itself.",
    "The roll-up: on a copy of Bethan's board, does the first approach (cells stay subitems, the total reaches the parent, the Studies board reads it through a connection) work with her form, and what happens when a cell is added after costing or n changes at screener sign-off?",
    "Identifiers: should the study code be typed once (on Studies) and read by the costing board, or the other way round, and what happens to the existing items whose codes do not match?",
    "Actual: where exactly does 'actual' live in the accounting system, will Philippa allow a read or a monthly upload, and is the per-agency monthly view a view over Studies or over the costing board?",
    "The rate: what loaded hourly cost does Philippa use for a fieldwork manager, so the bleed can move from effort-quantified to Met?",
    "Labels: which Studies status labels should change now (two 'mean the same thing'), who may edit them after the handover, and does the Friday digest read any of them?",
    "The rota: what are the columns on Leonie's sheet (photo from Idris), which sessions and rooms exist across both centres, when is the wave blackout, and will Leonie be in the session where the view is built?",
    "Admin and members: who is actually admin on the account today (Bethan thinks the Consultant and Hamish), read live before anything is changed.",
    "Seats and tier: the renewal quote's seat count and whether the Pro plan's limits fit the connection and the view planned, read at preflight with its date.",
]
key["expected_verdict"] = {
    "verdict": "Nearly ready",
    "gates_met": [
        "Solution blueprint (R1 Met, R2 Met; the structure inventory's read-back is graded Partial: the prototype rows were read back in the scope playback and accepted by Henrietta, the observed-only rows stay unconfirmed until the working session, and that grade is recorded in front of the gate)",
        "Build (no extra method gate; the Consultant's approval at the approval stop, after access is granted and the copy has been tried)",
        "First demo (v0.1): nothing extra needed; the demo re-confirms the mechanism-confirmed pain on screen",
    ],
    "gates_not_met": [
        "Pricing or proposal prep (R7 Met, but R4 Partial: effort-quantified, rate pending with Philippa; and R12 Partial: the rota half is a maybe and the access unlock is open). A commercial date exists on our side, 20 November, so the front page shows the collision and the steps scheduled back from it; pricing itself is not part of this plugin",
        "v1.0 sign-off (R11 Partial: mechanism-confirmed only, nothing shown; R6 success criteria proposed, not agreed; P2 unconfirmed)",
    ],
    "note": "R2 Met, R3 met-with-residual (counts as Met for the verdict, with the missing client clock as a gap question), R7 Met and R4 Partial give Nearly ready, with the reason line reading scale established, cost not priced, missing multiplier the loaded rate, and the 20 November collision named. Gap questions for the next meeting (at most five, per audience): the rate (Philippa), the client clock (Henrietta), the rota approach and Leonie's hours (a room with Leonie), the access answer (Bethan via the IT people), the actual side of costed-versus-actual (Philippa). Propose the blueprint as a second strand in the existing record once access exists: a delta against the inherited board, the live map honoured, the rota conditional, the automations as one approval list. No figure, no proposal and no completion estimate until the board has been read.",
}
key["account_context"] = {
    "tier": "Pro (client statement, hedged seat count 'thirty-something'; the renewal quote holds the number, not read on the call; to be read live at preflight with its date)",
    "products_enabled": [
        "Work Management: live, our build from about two years ago (Studies board with the Friday digest automation, Incentives board, a dead Recruiter rota board) plus Bethan's own Study costing board in her own workspace",
        "No CRM and no Service enabled or discussed",
    ],
    "existing_monday_setup": "A bound account with a live prior build of ours and one client-built board. Live and loved: the Studies board (one line per study, a status column with about seven labels that the five account leads read, field dates the account leads move) and its Friday digest automation to the account leads and Henrietta; the Incentives board, run by finance as its own. Lapsed: the Recruiter rota board, abandoned inside three months for Leonie's sheet, still in the account with nothing on it for about a year, to be archived. Client-built: Bethan's costing board (form, item per brief, cells as subitems, working cell-total formula, a subitem summary no parent formula or connection can read), in her own workspace where the Consultant has no access yet. Admin membership is hedged from memory (the Consultant and Hamish 'I think', Bethan a member) and is read live. The record exists already: this call opens a second strand, reads the live map and prior_builds, and touches the Studies board only with Henrietta's yes.",
    "evidence_quote_or_null": O_STUDIES,
}
key["expected_structures"] = {
    "native_boards_required": [],
    "portfolio_expected": False,
    "portfolio_reason": "The client states the Pro plan ('We're on Pro, I think it's thirty-something seats'), so the Enterprise default does not apply; Work Management is the only product and the work is a delta against an inherited board plus a conditional view, none of it portfolio-shaped. The tier is a client statement with a hedged seat count and is re-read at preflight with its date.",
    "lookalike_traps": [
        "Building a new costing board of our own beside Bethan's, or copying hers into a fresh board, instead of extending the inherited board she owns; the form and the cells stay hers.",
        "Creating an 'Agencies' or 'Clients' board to hold the per-agency monthly view, which is a CRM Accounts look-alike in a build with no CRM in scope; the view is a view over studies, keyed by the agency value already on Studies.",
        "Building a new recruiter rota board while the dead one sits in the account, or silently repurposing the dead one; the dead board is archived with Henrietta's yes, and a recruiter week view is built only after she has seen the approach.",
        "Putting the costing onto the Studies board with new columns the account leads must fill in, which breaks the 'read, not typed' condition and Henrietta's gate on the live board.",
        "Touching the Friday digest automation or the Incentives board in any way, including 'improving' them; both are do-not-change, quoted from the client.",
    ],
    "notes": "One product, three classes of object. Inherited (client-built): the costing board, form, cells, cell formula, to be extended after access and a read on a copy, never overwritten. Live and ours: the Studies board (change-with-own-yes; the connection and the label handover with Henrietta's yes), the Friday digest and the Incentives board (do-not-change), the dead rota board (archive). New: the parent total and the connection, the per-agency monthly costed-versus-actual view once 'actual' has a source, the conditional recruiter week view for the wall screen. No CRM, no Service, no portfolio, no time tracking. Respondent data and payment data never enter the account. Every automation, including any change near the digest, goes on one approval list with recipients shown.",
}
key["accepted_behaviours"] = [
    "Proposing the type header in any wording that names expansion as the call type and the screen share as a working-session sub-trigger with its boundaries quoted, provided no second mode or second label is applied and the header is offered with its quote rather than decided.",
    "Grading R1 Met from the estate turns alone, with or without a formal structure inventory, as long as the prototype rows are kept apart from current state and admin membership is marked hedged.",
    "Grading R3 met-with-residual, or Met with the missing client clock listed as a gap question, as long as the 20 November date never appears as why-now evidence and is front-paged as our own owned to-do.",
    "Showing the commercial-date collision in any layout that names the closed gate, the date, and the steps scheduled back from it, while stating that pricing and proposal prep are not part of this plugin.",
    "Grading R10 Met on the booking mechanism, or Met with a note that no date exists yet, provided the grade is tied to expansion mode, the same-day date-proposal to-do is emitted for the Philippa hand-off, and nothing is inferred from the calendar.",
    "Reporting the bleed as effort-quantified, rate pending, or as Partial with the rate named as the missing multiplier and Philippa as its owner; either wording passes, and any figure built from 'forty an hour' fails.",
    "Grading P2 Cost inputs not obtainable from this room naming the recruitment coordinator, or Missing with the same routing note, provided nothing is inferred from Idris or Henrietta.",
    "Filing the prototype either as the internal-builder signal row (built a prototype, hit a wall and named it) or as no objection at all with the client-built assets section carrying the wall; filing it as 'We'll build it ourselves' fails.",
    "Refusing any completion, effort or duration figure for work on the costing board, in the summary, the recap or the blueprint, until access exists and the board has been read; repeating 'eighty percent' as a fact fails.",
    "Proposing the blueprint now as a delta against the inherited board with the access unlock listed as blocking, or holding the blueprint until after the booked working session with that reason stated; either passes, silently building beside her board fails.",
    "Recording the live-map constraints in any equivalent wording: the digest and the Incentives board untouchable, the Studies board changed only with Henrietta's yes and only with read-not-typed elements, the rota board archived rather than deleted.",
    "Naming the tier as Pro from the client's statement, with its hedge and date, and asking for the seat count rather than reading it from the renewal quote, which the plugin has not seen.",
    "Treating everything said about Hamish, Philippa and Leonie as relayed: it shapes the delegation graph, the do-not-change list and the room-change routing, and never counts as their evidence.",
    "Presenting automations, including the archive of the rota board and any connection near the digest, as one approval list with trigger, conditions, action and recipients per row, and running the change check before any write into the client's account.",
]
key["expected_leak_blocklist"] = [
    "Cost inputs and hours: 'Four hours, sometimes five', 4-5 h/wk, 'call it half that each', 'my Friday' as a cost, 'at least twice' and 'three times' as cost multipliers, and any phrase pairing hours with a rate or a yearly total.",
    "The withdrawn rate and any rate: 'forty an hour', 40, $40, 'loaded rate', and any hourly cost attributed to Philippa before she supplies it.",
    "The Farraday loss: 'About six thousand', 6000, $6k, 'we ate it', 'doubled up on the incentives', 'eleven at night', and the narrative of a mis-costed study as the firm's failure; Farraday may be named as an agency, not narrated as a loss.",
    "The client's own completion guess: 'eighty percent there', 80%, and any completion, effort or duration figure for the costing board.",
    "Our commercial clock: 'held until the twentieth of November', 20 November, 'my constraint', the renewal quote and its validity, and any sentence that turns the date into client urgency.",
    "Tier, seats and spend: 'Pro', 'thirty-something seats', the systems figure Hamish set, 'up to what Hamish set', 'on the card', 'nobody blinked', and any threshold or budget remark.",
    "Incumbent friction and stakeholder assessments: 'we had to email you and wait', 'people stopped asking', 'the handover was a call', 'Philippa would riot', 'She doesn't sign, but she can stop it', 'unless the two of you go mad', 'Hamish reads those', 'Hamish on his phone at the weekend'.",
    "Remarks about colleagues and personal stakes: 'Leonie's got the sheet down to a fine art', 'She'd rather keep it', 'nobody could read the colours', 'she was shown it after', 'That's on me', 'Beth did the corrected one at eleven at night', 'I'm tired of it', 'He's got a playlist'.",
    "The backslide and failure narratives: 'They went back to the sheet inside three months', 'the sheet won', 'The rota board's dead', 'Twelve respondents turned up to an empty room', 'That one got to Hamish', 'we lost two sessions'.",
    "Objection text and the objection names: 'whether it's just not the right tool', 'can the extra piece be on the same sheet', 'The rota is a maybe', 'We've been here before', and the map's names (changing what you built costs us, build it ourselves, monday itself is the problem, team won't adopt it, must check with someone, just send a proposal).",
    "Readiness and gate language: R1-R12 and their names, 'Nearly ready', 'met-with-residual', 'not obtainable from this room', excavated, gate, gap question, mechanism-confirmed, the commercial-date collision, and any statement that discovery is complete or incomplete.",
    "Method vocabulary and markers: bleed, upside, effort-quantified, rate pending, callback, exit ramp, seed, expansion mode, working-session sub-trigger, live map, do-not-change, change-with-own-yes, pain ids (P1, P2), N#, S#, O#, C#, and the [Q], [Q/recon], [X], [I] and [found] markers.",
    "Internal artefacts: the call summary, the type header, the delivery notes, the raw transcript and its timestamps, the two lines after the goodbyes about the Farraday invoice, the claims store entries for the two approaches, and any 'if asked' or 'do not show' note.",
    "Pricing material of any kind: rates, totals, discounts, ROI, cost-of-waiting figures, and any number for the costing work, since pricing is outside the plugin and the gate is closed.",
    "Confidential client data: respondent names, numbers or history from the panel software; bank or payment details; brand names or agency study titles in place of study codes; the agencies' compliance arrangements.",
    "Alternatives and other clients: no other vendor, partner or in-house build may be named, because none was discussed; Bethan's own board is inherited work, not a competitor, and no other client's name or example may be used.",
    "Consulting brand and product names: the consultant appears as 'Consultant' only, and no plugin, tool or brand name of the Consultant's may appear in the account or in client-facing text.",
    "Flag, do not remove (process and volume facts that belong in an SOP or a board, checked with the Consultant first): about seventy people, 28 recruiters, five account leads, three fieldwork managers, two centres including Thornbury, 12-15 briefs a month, the Friday digest as a process, the wave blackout, Saturday sessions, qual and quant, cells, the study code convention.",
    "CAUTION: 'cell', 'wave', 'session', 'brief', 'study', 'code' and 'the Friday email' are the client's own vocabulary and must survive in boards and SOPs even where a blocked phrase sits near them.",
]
key["intake"] = {
    "format": {"family": "block export", "dialect": "one turn per line, '[HH:MM:SS] Speaker Name: text'", "end_times": False, "timestamp_shape": "zero-padded HH:MM:SS start only, monotonic, no collisions", "label_position": "prefix in the payload, full name, uniform", "participant_header": False, "line_endings": "LF", "units": 262, "words_spoken": 4729, "max_unit_words": 83, "defect_density": "low: 24 of 262 turns (about 9%) at or below four words, none of them a fragment of a neighbour; no lowercase-initial turns; no colliding stamps; 20 adjacent same-label pairs; the no-action band applies", "roster_source": "observed speakers only; the Consultant's opening names the expected attendees, which is human framing and not a roster"},
    "type_header": {
        "call_type": "expansion",
        "sub_trigger": "working-session (a client-built artefact present and technical work performed on it during the screen share)",
        "labels_not_applied": {"working-session": "the sub-trigger of expansion mode, not a second mode or label (R9)", "prototype-review": "the screen share is a typed segment inside an expansion call, and the prototype-review type switches no rule off on its own", "scoping": "the deliverable is configured structure and the call chains discovery-check, not the scope path"},
        "seat": {"value": "partner-led", "quote": C_AGENDA, "location": loc(C_AGENDA)},
        "relationship": {"value": "existing client of ours", "quote": "Anything of ours that's changed since I last looked?", "location": loc("Anything of ours that's changed since I last looked?")},
        "direction_of_show": {"primary": "nobody shows", "segment": "they show a candidate solution they built", "from": E(B_SHARE), "to": E(B_STOP), "deixis_run": "about seven minutes of client-side screen deixis, so the show is substantive"},
        "output_class": {"value": "configured structure", "quote": "It's a board with a form on the front, one item per brief, and the cells are subitems.", "location": loc("It's a board with a form on the front, one item per brief, and the cells are subitems.")},
        "room_shape": "small: three client attendees who all spoke, one on our side; no roster, so voices missing reads unknown",
        "money_live": {"value": "yes, on our side only: a commercial date spoken by the Consultant with the approver present; the client's own commercial markers are the tier and a hedged seat count", "quote": C_CLOCK, "location": loc(C_CLOCK)},
        "agenda": {"quote": C_AGENDA, "location": loc(C_AGENDA), "client_answer": O_AGENDA_ANSWER, "client_answer_location": loc(O_AGENDA_ANSWER)},
        "proposed_not_decided": True,
    },
    "current_state_met_early": {"by": "00:07:13", "from_quotes": [loc(O_STUDIES), loc(I_DEAD), loc("Nobody, really.")]},
    "current_wins_to_preserve": [
        {"object": "Studies board status column and the Friday digest automation", "quote": O_FRIDAYMAIL, "location": loc(O_FRIDAYMAIL), "owner": "Henrietta Weyland (readers: the five account leads, Hamish)", "authorship": "built by us", "burden": "none stated; runs without anybody touching it", "change_path": "labels: none today (email us and wait); to become self-service for Bethan with Henrietta's yes", "constraint": "digest do-not-change; Studies board change-with-own-yes"},
        {"object": "Incentives board", "quote": O_INCENT, "location": loc(O_INCENT), "owner": "Philippa (finance), absent", "authorship": "built by us, now finance's own", "burden": "none stated", "change_path": "none; Philippa can stop anything near it", "constraint": "do-not-change"},
        {"object": "Bethan's costing board: the form and the cells", "quote": B_MECH_OK, "location": loc(B_MECH_OK), "owner": "Bethan Tull", "authorship": "built by them", "burden": "hers; stops at the roll-up", "change_path": "inherited and extended after access and a read on a copy", "constraint": "inherited; the form stays"},
    ],
    "prior_attempts": [
        {"what": "Recruiter rota board", "by_whom": "us", "when": "about two years ago, with the Studies and Incentives boards", "status": "lapsed: nothing on it for about a year, still in the account", "payer": "the client (on the card, 'nobody blinked')", "why_in_their_words": I_BACK, "location": loc(I_BACK), "disposition": "archive with Henrietta's yes; a recruiter week view only after she has seen the approach and with Leonie in the room"},
    ],
    "incumbent_friction": {"stated": True, "quote": O_FRICTION, "location": loc(O_FRICTION), "client_attributed_cause": O_CAUSE, "cause_location": loc(O_CAUSE), "objection_status": "embedded"},
    "prior_build_by_us_still_live": {"objects": ["Studies board", "Friday digest automation", "Incentives board", "Recruiter rota board (dead)"], "consumes": "unknown: seats and automation runs not stated; read at preflight", "change_cost_expectation": O_FRICTION, "do_not_disturb": [E(O_FRIDAYMAIL), E(O_INCENT)], "handover_lesson": E("That's the thing I'd do differently, honestly. Last time it was built and handed over and the handover was a call. This time I want someone here who can change things.")},
    "client_built_assets": {"what": "Study costing board in Bethan's own workspace", "why": E("Which is partly why I built the costing thing on my own. I didn't want to email and wait."), "mechanism": "form, one item per brief, cells as subitems with a cell-total formula, a subitem summary on the parent", "author": "Bethan Tull", "does": "captures a brief and its cells and totals each cell; observed on her screen and narrated", "blocker_in_their_words": E(B_WALL), "access_state": {"state": "no access; the board is in her workspace", "unlock_owner": "Bethan, subject to the IT people's guest policy", "cost": "unknown; a few days", "quote": B_ACCESS, "location": loc(B_ACCESS)}, "their_own_completeness": {"quote": B_EIGHTY, "location": loc(B_EIGHTY), "treatment": "the client's guess; never a figure of ours"}, "our_completeness_note": "seen: the form and the cells and a working cell formula; not yet looked at: the connection to Studies and late-added cells; no figure until read", "disposition": "inherit and extend, approach one (cells stay subitems, total to the parent, Studies reads it); the form stays", "post_handover_ownership": "Bethan"},
    "commercial_clock_our_side": {"date": "2026-11-20 (Friday; 'the twentieth of November')", "speaker": "Consultant", "quote": C_CLOCK, "location": loc(C_CLOCK), "client_acknowledgement": {"quote": O_NOTED, "location": loc(O_NOTED, "Henrietta Weyland"), "treatment": "backchannel; non-evidence; not hesitancy"}, "front_page": True, "excluded_from_why_now": True, "listed_as_owned_todo": True, "never_client_hesitancy": True, "other_constraints_our_side": [{"constraint": "no figure on the costing piece until the board has been read", "quote": "Happy to, once we've agreed what it covers, and I won't put a number on the costing piece until I've read Bethan's board. So it may be two sheets, or one sheet later. I'd rather it was right.", "location": loc("Happy to, once we've agreed what it covers, and I won't put a number on the costing piece until I've read Bethan's board. So it may be two sheets, or one sheet later. I'd rather it was right."), "owned_todo": "read the board on a copy in the working session, then price"}, {"constraint": "no access to the costing board yet", "owned_todo": "wait for the IT people's answer through Bethan; never propose the policy"}], "collision": {"gate": "Pricing or proposal prep", "closed_by": ["R4 partial (rate pending with Philippa)", "R12 partial (rota a maybe; access unlock open)"], "steps_scheduled_back": [{"step": "working session on a copy of the costing board", "owner": "Consultant with Bethan", "by": "the week after the call"}, {"step": "loaded rate from Philippa", "owner": "Consultant, introduced by Henrietta", "by": "before the scope read-back"}, {"step": "scope read-back with Henrietta: costing confirmed, rota decided, access settled", "owner": "Consultant", "by": "before 2026-11-20"}, {"step": "pricing prep", "owner": "the user, outside the plugin", "by": "2026-11-20"}]}},
    "next_step": {"state": "booking mechanism delivered on the call", "mechanism": "a booking link sent today for a 45-minute working session", "owner_send": "Consultant", "owner_book": "Bethan Tull", "purpose": "walk the costing board cell by cell and try the two approaches on a copy", "assent": E(B_ASSENT), "grade": "met", "grade_in_discovery_or_demo_mode": "partial", "second_item": {"state": "scheduling handed off to a named owner, no mechanism", "owner": "Henrietta Weyland", "quote": O_PUT_IN_TOUCH, "location": loc(O_PUT_IN_TOUCH), "grade": "partial-plus", "todo": "same-day date-proposal to Philippa via Henrietta"}},
    "composite_blocks": [],
    "composite_detector": "ran; cannot qualify on this file (no end times, longest unit 83 words) and says so",
    "wedges": [],
    "wedge_detector": "not applicable: block export without end times",
    "rejoined_sentences": [
        {"owner": "Bethan Tull", "units": [loc(B_SPLIT_A), loc(B_SPLIT_B)], "interior_backchannel": E(C_MMHM), "reconstruction": "The other thing I want out of it, and this is the bit Henrietta actually cares about, is a monthly view per agency of what we costed against what it actually came in at.", "boundary_artifact": "the repeated 'against what' at the join, removed only outside the quotation marks", "citation": "[Q/recon] with both locations, or two [Q] quotes; never one quote across the Consultant's label", "confidence": "probable"},
    ],
    "split_numbers": [],
    "unit_unresolved_figures": [],
    "alias_map": {"Bethan Tull": ["Bethan", "Beth"], "Henrietta Weyland": ["Henrietta"], "Idris Machado": ["Idris"], "Leonie": ["absent: recruitment coordinator, keeps the rota sheet"], "Philippa": ["absent: finance controller, the accounting system, rates"], "Hamish": ["absent: owner, the systems figure"], "Farraday": ["an agency and its study; not a person"], "Thornbury": ["the second recruitment centre; a place, not a person"]},
    "confidence": {"default": "certain", "exceptions": [{"location": loc("It's the same sheet, just [inaudible] for Thornbury."), "state": "uncertain", "reason": "[inaudible] inside the unit; corroborated by the next line and originates nothing"}, {"location": loc("[crosstalk] -- sorry, hi, I'm here. Phones are going but I've shut the door."), "state": "probable", "reason": "crosstalk at the join"}, {"location": loc("Sorry, hang on. [crosstalk] No, tell her I'll ring her back. Sorry. Where was I."), "state": "probable", "reason": "off-call speech inside the turn; not evidence"}, {"location": loc(B_SPLIT_A), "state": "probable", "reason": "fragment tail of the re-joined sentence"}, {"location": loc(B_SPLIT_B), "state": "probable", "reason": "fragment head of the re-joined sentence"}]},
    "package_order": None,
    "package_note": "single call, first-hand; no package, so no order to confirm",
    "second_hand": [],
    "second_hand_note": "none: every figure is first-hand and no figure is re-quoted; the relayed remarks (Hamish's win condition, Philippa's likely reaction, 'That one got to Hamish') carry no figure and are never attributed to the absent person as their statement",
    "quarantine": {"x_applied": False, "reason": "the screen share is the client's own frame (they show a candidate solution they built), so nothing narrated on it is quarantined; Bethan's test rows are excluded as figures on her own statement", "test_rows": E(B_TEST_ROWS)},
    "voices": {"heard": ["Henrietta Weyland", "Bethan Tull", "Idris Machado"], "missing": "unknown: no roster", "decision_shaped_absentees": ["Hamish (owner; spend above the threshold)", "Philippa (finance; can stop anything near Incentives; holds the rate)"], "after_goodbyes": [loc("Beth, hang on a second, I want to go through the Farraday invoice before Philippa sends it."), loc("Yep. Let me end the --")]},
    "delivery_notes": {"client_share": "about 67% by words", "longest_own_side_turn": "83 words", "fix_offered_mid_pain": "none: the two-approaches turn sits inside the prototype walk, where interrogating the artefact is the work", "client_interviewer": E("Beth, how many of those get a cell added after you've costed them? Actually, not roughly."), "commitment_question": E("Before we do next steps. Is this worth taking forward, from where you sit?")},
    "claims_by_our_side": [
        {"claim": "approach one is buildable ('I've built the first before')", "quote": "I've built the first before. I haven't tried it against a form like yours, so I'm not promising it until I've done it on a copy.", "location": loc("I've built the first before. I haven't tried it against a form like yours, so I'm not promising it until I've done it on a copy."), "hedge": "hedged against her form; unverified until tried on a copy", "audience": "approver present"},
        {"claim": "the withdrawn rate", "quote": C_FORTY, "location": loc(C_FORTY), "hedge": "withdrawn on the spot", "audience": "approver present; refused by her"},
    ],
}

if ERRORS:
    for e in ERRORS:
        sys.stderr.write("ERROR " + e + "\n")
    sys.exit(1)

text = dumps(key) + "\n"
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(text)
json.loads(text)
print("wrote", OUT, "lines", text.count("\n"))
