#!/usr/bin/env python3
"""Build fixtures/s6-discovery-crm-sales/answer-key.json.

Quotes are written once, here. Locations are filled in by searching the
transcript, so a location can never disagree with the line it points at.
Aborts if any quote is missing, spans lines, or matches more than one line.
"""
import json
import re
import sys
from collections import OrderedDict

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s6-discovery-crm-sales/"
T = open(BASE + "transcript.txt", encoding="utf-8").read()
LINES = [l for l in T.splitlines() if l.strip()]
ROLES = {
    "Marcus Thibault": "VP of Sales",
    "Delia Ostrowski": "Sales Operations Analyst",
    "Wes Kubiak": "Regional Sales Manager",
    "Consultant": None,
}
errors = []


def loc(q):
    """Return '[MM:SS] Speaker (role)' for the single line containing q."""
    hits = [l for l in LINES if q in l]
    if len(hits) != 1:
        errors.append(f"{len(hits)} hits for {q[:70]!r}")
        return "UNRESOLVED"
    m = re.match(r"^(\[\d\d:\d\d\]) ([^:]+):", hits[0])
    stamp, sp = m.group(1), m.group(2)
    role = ROLES.get(sp, "UNKNOWN SPEAKER")
    return f"{stamp} {sp} ({role})" if role else f"{stamp} {sp}"


def ev(*quotes):
    return [OrderedDict([("quote", q), ("location", loc(q))]) for q in quotes]


def pain(q, theme):
    return OrderedDict([("quote", q), ("location", loc(q)), ("theme", theme)])


def row(criterion, status, quotes, note):
    return OrderedDict([("criterion", criterion), ("status", status),
                        ("evidence", ev(*quotes)), ("note", note)])


# --------------------------------------------------------------------- rubric
rubric = [
    row("R1 Current state mapped", "met", [
        "Tuesday morning I pull every open quote out of P twenty-one, that's our ERP, Prophet twenty-one, and I paste them into the workbook.",
        "Every rep keeps their own tab, and the columns are different in almost every one, because they set them up themselves back in twenty-nineteen and nobody ever standardised it.",
        "The quote lives in P twenty-one, the pricing lives in P twenty-one, the stock lives in P twenty-one, and everything about whether anybody's actually going to buy it lives in somebody's head.",
        "Then it depends entirely on the rep. It goes in his phone, or on a sticky note, or in his tab in the workbook if he's one of the organised ones.",
        "My Monday morning call is a bunch of people telling me what they think they're going to close and me writing it on a legal pad.",
        "Nobody has opened it since, what, twenty-twenty-three?",
        "We bought monday about nine months ago for the operations side.",
        "It says Pro when I log in. And there's a whole sales CRM section in there with nothing in it, which I've clicked into maybe twice.",
    ],
        "Mapped end to end and unusually well for a first call: the four intake routes, qualification by visit, who builds the quote and why (pricing matrices), the P21 quote as the document of record, Delia's Tuesday pull and Friday forecast, the 22-tab workbook with per-rep columns, Wes's Monday call and legal pad, the dead GoldMine install, and the existing monday use with the tier stated. People and time are attached to each step (Delia 6 h/wk, reps 3 h/wk, managers 4 h/wk). Gaps that remain and should be confirmed rather than assumed: inside sales only surfaced in the last five minutes and their part in the flow is undescribed ('Inside sales takes maybe a third of the orders'); how the website form's shared inbox is triaged today, and by whom; who approves a stocking agreement or contract pricing; the structure, seat count and administrator of the existing monday boards, which the Consultant has said will be inspected before building; and whether the CRM product workspace holds a native install at all, which the transcript cannot answer ('a whole sales CRM section in there with nothing in it'). The bid calendar was described and then deliberately excluded."),
    row("R2 Pain made concrete", "met", [
        "We had a sixty-two thousand dollar stocking quote sitting at Brightline for five weeks and nobody touched it.",
        "Of the quotes over five thousand dollars we sent out last year, thirty-eight percent had no activity after the day they went out.",
        "Nothing. There's no follow-up step. It's whether the rep remembers, and some of them are excellent and some of them are not.",
        "I cannot tell you today what's going to close this month. I can tell you what twenty-two people told me they hope will close, which is not the same thing.",
    ],
        "P1 (no shared pipeline) and P2 (quotes going unfollowed) are both excavated: stated, a specific recent occurrence, and a named workaround the client rejects. P3 (history leaves with the rep) is excavated as well on the three required checks. P4 (visit activity invisible) has a Partial workaround. P5 to P7, listed under pains, are real but thinner: the house accounts nobody works, win-loss on the city bids, and new-rep onboarding, all of which the client put outside the agreed scope for now."),
    row("R3 Why now", "met", [
        "We're launching western Pennsylvania on January fifth. Four reps, two already signed, and the first one starts December first.",
        "It's real. The two signed reps start December first and January fifth, and their guarantee period starts when they start.",
        "Gene wants a rolling ninety-day forecast on his desk every month starting in January.",
        "because we picked up the Northgate abrasives line for that geography in June",
    ],
        "Three separate triggers with dates: the territory launch on 5 January with the first rep starting 1 December, the president's monthly rolling 90-day forecast from January (asked for in August, after the Brightline loss), and the new abrasives line for that geography picked up in June. The December date is a real constraint on the build, not a preference: 'If it's not working before December first, it's not worth doing for this launch.'"),
    row("R4 Bleed number", "met", [
        "Tuesday morning and Friday morning. So call it six hours a week, and that's a quiet week.",
        "Delia loaded is about thirty-five an hour. That's close enough.",
        "Three hours a week, easy. Some of them more. And a chunk of that is calling Fort Wayne to ask a question they could have looked up if it was written anywhere.",
        "With the truck, the phone, benefits, all of it, about sixty an hour.",
        "Four hours. The Monday call is an hour and a half of it and then I'm calling people all week to fill in what they didn't say on the call. And there's three of us doing that.",
        "Call a manager seventy an hour loaded.",
        "Managers, four hours each, three of you, that's twelve hours a week at seventy, times fifty-two, forty-three thousand six hundred and eighty. So on time alone that's two hundred and sixty thousand five hundred and twenty.",
        "Average quote over five thousand is about eight thousand. We make about twenty-five points on that kind of work.",
        "If I'm honest, one in twenty of the ones we didn't chase. Some of them were never real. So twenty-three orders. Twenty-three times two thousand, that's forty-six thousand.",
        "Two hundred and sixty thousand five hundred and twenty plus forty-six thousand. Three hundred and six thousand five hundred and twenty.",
        "Three hundred and six thousand a year.",
        "It feels low, if anything. It doesn't have my time in it, and it doesn't have the house accounts nobody's calling.",
    ],
        "Every input is client-supplied, the arithmetic is done out loud by the client's own analyst, and the VP confirms the total and says it feels low. Note the discipline test in the middle: the Consultant floated 'something like four hundred and seventy thousand in margin' off a half-of-them assumption and was refused ('No. Nowhere near half.'); the client then supplied one in twenty, 23 orders and $46,000. The key's figure is the client's $306,520, never the Consultant's. Excluded on purpose and named as excluded: the Brightline $62,000 (a one-off), the VP's own time, and the unworked house accounts."),
    row("R5 Upside number", "met", [
        "About two point two million a year in revenue, at roughly the same twenty-five points.",
        "Nine months, historically. That's what the last three hires took to get to a normal book.",
        "Six. I'd say six, and I'd be annoyed if it wasn't.",
        "A ramping rep isn't doing full rate, so say half. Half of two point two is one point one, so a quarter of that is two hundred and seventy-five thousand each in that quarter. Four reps, that's one point one million in revenue.",
        "And a quarter of that is margin, so two hundred and seventy-five thousand. In the launch year.",
        "If I weren't rebuilding that workbook twice a week I'd be doing win-loss on the city bids. Nobody has ever looked at why we lose those.",
        "House accounts. Two hundred-odd companies that buy from us when they happen to call. Nobody's ever worked that list and I've asked for somebody to work it for three years.",
    ],
        "Met, with the client doing the conversion and the 'what would you do with it' answers coming from two different people. Two properties of this number matter for any later use: it is a launch-year figure, not an annual one, and the client agreed that out loud ('Once they're ramped they're ramped.'); and it does not overlap the bleed, which is time and unchased quotes rather than ramp revenue, so the two must never be added together. The capacity answers (win-loss analysis on the city bids, working the house accounts) are wants the client cannot reach today, not requirements, and both were placed outside the agreed scope."),
    row("R6 Desired outcome", "met", [
        "A normal week is: I open one screen on Monday morning and I know what's out there, what's stuck, and what closed. I don't ask twenty-two people and I don't wait for Friday.",
        "If the forecast I give him in January is within ten percent. That's it. That's his whole test. He's a numbers guy and he doesn't care how it's made.",
        "Knowing who's been in front of a customer without asking anybody. And the new four getting to productive without me living in Pennsylvania.",
        "Not retyping. Genuinely, that's my answer. If the summary builds itself I don't care what it looks like.",
    ],
        "A picture of solved from each of the three attendees, plus the approver's own test stated as a number: a January forecast within ten percent. These become draft success criteria marked proposed, not agreed, so the v1.0 sign-off gate stays shut until they are confirmed. 'one screen on Monday morning' is the outcome, not a specification of a dashboard; do not turn a figure of speech into a design commitment."),
    row("R7 Decision process mapped", "met", [
        "This is my call. I've got a line in the sales budget and I don't need Gene's signature under forty thousand a year. Gene wants to be told, not asked.",
        "Then it's a conversation with him and probably with our accountant, and it gets slower. I'd rather stay under it.",
        "We don't have an IT department, we have Halbrook Technology, and Ravi over there has to bless anything that touches P twenty-one.",
        "A week or two if you ask him nicely and give him a document. Longer if it sounds like it writes anything back into P twenty-one.",
        "Delia. She's the one who'd have to keep it alive, which is the part I want to ask about actually.",
        "We paid for GoldMine for six years and used it for about one. I'm not doing that again.",
    ],
        "Fully mapped, and the approver is in the room, which no other fixture in this set has: the VP decides, holds the budget line and needs no signature under $40k a year; the president is informed rather than consulted; the outsourced MSP gatekeeps anything touching the ERP, with a stated turnaround of one to two weeks and a longer one if writes are involved; Delia is the named day-to-day owner and the adoption risk sits with the reps. Prior budgeting experience is explicit and negative: six years of paying for a CRM they used for one."),
    row("R8 Priority and timing", "met", [
        "Top of the list. This is a now thing. If it's not working before December first, it's not worth doing for this launch, and then I'd rather wait until after the spring.",
        "Don't try to train anybody the week of Thanksgiving. Nothing happens that week, nobody's here.",
        "And the first week of the month is order entry, so the reps are useless for anything else Monday and Tuesday.",
    ],
        "Placed at the top of the list with a hard date and an explicit fallback (wait until after the spring) if December is missed, which is a fit risk to keep visible rather than a soft preference. Two calendar constraints to design around: no training in Thanksgiving week, and reps unavailable the first Monday and Tuesday of each month for order entry."),
    row("R9 Blockers surfaced", "met", [
        "The reps. That's the whole risk. If it's one more thing to update, they won't, and then I've paid for GoldMine twice.",
        "And if it's slow on a phone in a parking lot, forget it. My guys are not sitting down at a desk. If logging a visit takes more than about a minute in a truck, it won't happen.",
        "And me getting pulled onto the inventory count again in October. That's a real risk, it happens every year.",
    ],
        "Three named blockers, one per attendee, and all three are design inputs rather than sales problems: rep adoption with GoldMine as the precedent, phone usability in a truck with a one-minute ceiling on logging a visit, and the owner's own availability being taken by the October inventory count."),
    row("R10 Next step committed", "met", [
        "Twenty-third works. Two o'clock. I'm in Toledo that day.",
        "I'm free.",
        "Yep, put it in.",
    ],
        "Date, time, length, attendees and purpose all agreed on the call: Wednesday the 23rd at 2:00 pm Eastern, 45 minutes, all three attendees, to react to a first version built in their own account. The Consultant owns the invite and said it would go out at the end of the call, so it stays a to-do until confirmed sent."),
    row("R11 Solution confirmed", "missing", [],
        "Missing by definition: this is the first call and nothing has been shown, so no pain has been confirmed solved in a demo. R11 is graded from demo transcripts only, and it blocks the v1.0 sign-off gate until the 23rd at the earliest."),
    row("R12 Scope agreed verbally", "met", [
        "No. That's the scope. All five, nothing else for now. New rep onboarding, the bid calendar, the house account campaign, all of that can wait until this is alive.",
        "Agreed. I'd add, whatever we do with my Prospects board, don't leave two of them.",
        "Works for me. Five is enough.",
        "Yes. And the quote itself stays in P twenty-one. You're not rebuilding our quoting.",
    ],
        "Met, and this is the first fixture in the set where it is. The Consultant played back five bullets and the approver agreed them out loud, named what is excluded for now, and both other attendees agreed separately. The scope is: (1) prospects with intake from the website form and trade show lists, owned with a next step; (2) accounts and contacts with the history staying when a person leaves; (3) the opportunity pipeline through quoted, verbal, won or lost, carrying the P21 quote number and a follow-up step; (4) logged calls and visits, fast from a truck, with a sortable coverage view for the manager; (5) a forecast view for the VP and the president that builds itself, replacing the workbook. Because R4, R7 and R12 are all Met, the method's pricing-or-proposal gate is open here; what holds a proposal back is the v1 product scope, not the method."),
]

per_pain = [
    row("P1 Stated", "met", [
        "I cannot tell you today what's going to close this month. I can tell you what twenty-two people told me they hope will close, which is not the same thing.",
        "A rep says a quote is hot because he remembers the visit, not because anything happened this week.",
    ], "P1 is the VP's own framing: the pipeline exists only as twenty-two people's recollections, so the forecast is a guess."),
    row("P1 Concrete", "met", [
        "We had a sixty-two thousand dollar stocking quote sitting at Brightline for five weeks and nobody touched it.",
        "Retyping. Honestly. Some of them put the customer in one column, some of them put customer and city together, one guy puts the quote number in the notes field. I copy it into the shape the summary needs.",
    ], "A specific recent loss and a day-to-day description of what the workaround costs, with the mechanics of the retyping named."),
    row("P1 Workaround", "met", [
        "My Monday morning call is a bunch of people telling me what they think they're going to close and me writing it on a legal pad.",
        "A legal pad. I have a drawer of them. If you want to know what happened in March you can go read March.",
        "With four more reps and a territory we've never sold into, the legal pad stops working. It barely works now. I've got seven and I'm at the edge of it.",
    ], "The workaround is named precisely (the 22-tab workbook, the Monday call, the legal pad) and the client says plainly why carrying on is not acceptable."),
    row("P1 Reach", "met", [
        "And it's not just Marcus who can't see it. I don't know what my own seven guys have out there unless I call them and ask.",
        "It matters when I'm asked why a region is down and the honest answer is I don't know if anybody went out there. Gene asked me that in June about Fort Wayne and I didn't have an answer.",
    ], "Reaches the VP, all three regional managers, the analyst who rebuilds the workbook and the president who asks questions nobody can answer."),
    row("P1 Cost inputs", "met", [
        "Tuesday morning and Friday morning. So call it six hours a week, and that's a quiet week.",
        "Three hours a week, easy. Some of them more. And a chunk of that is calling Fort Wayne to ask a question they could have looked up if it was written anywhere.",
        "Four hours. The Monday call is an hour and a half of it and then I'm calling people all week to fill in what they didn't say on the call. And there's three of us doing that.",
    ], "Hours from all three levels plus client-supplied loaded costs, which is what makes R4 computable."),
    row("P1 Trajectory", "met", [
        "Twenty-six tabs instead of twenty-two. And four tabs from people who don't know how we do it, so I'd be building those columns for them. It's worse than linear, honestly, because new people ask more questions.",
        "Four new people with no history, no account records, nothing to hand them except a list out of P twenty-one of who bought what. And Wes managing seven plus four across two states off a legal pad.",
    ], "Both the analyst and the VP describe the launch making it worse, and the analyst says the growth is worse than linear."),
    row("P2 Stated", "met", [
        "Of the quotes over five thousand dollars we sent out last year, thirty-eight percent had no activity after the day they went out.",
        "Thirty-eight percent. That number made me feel sick, honestly. I've been carrying it around since August.",
    ], "Stated with a measured figure the client produced themselves before the call."),
    row("P2 Concrete", "met", [
        "There were four hundred and seventy-one of them over five thousand.",
        "Somebody was supposed to call them. That's it. That's the whole thing. There was no fight, we didn't get beaten on price, we just went quiet on a sixty-two thousand dollar quote.",
    ], "A count and a named recent instance, with the mechanism of the loss described rather than guessed at."),
    row("P2 Workaround", "met", [
        "Nothing. There's no follow-up step. It's whether the rep remembers, and some of them are excellent and some of them are not.",
        "P twenty-one will show me an open quote until it expires, but it won't tell anybody to do anything about it, and nobody's looking at that list except me on Tuesday.",
    ], "The workaround is explicitly nothing, and the client explains why the ERP does not fill the gap."),
    row("P2 Reach", "met", [
        "Me, eventually, because it shows up as a month that missed. Wes gets it first.",
        "It confuses me on Tuesdays. A rep will say the quote's dead and mean the whole thing is dead, or mean he requoted it with different pricing and there's a new number.",
    ], "Reaches the rep, the manager, the VP through the monthly number, and the analyst who has to interpret what 'dead' means."),
    row("P2 Cost inputs", "met", [
        "Average quote over five thousand is about eight thousand. We make about twenty-five points on that kind of work.",
        "If I'm honest, one in twenty of the ones we didn't chase. Some of them were never real. So twenty-three orders. Twenty-three times two thousand, that's forty-six thousand.",
    ], "Volume, average value, margin percentage and a conversion assumption, all client-supplied, and the client corrected the Consultant's more flattering assumption on the way."),
    row("P2 Trajectory", "partial", [
        "It feels low, if anything. It doesn't have my time in it, and it doesn't have the house accounts nobody's calling.",
    ], "Partial. The client says the current figure understates today, and the launch clearly adds quoting volume into a territory with no coverage, but nobody states what happens to the follow-up gap itself over the next year. The gap question is: with four more reps quoting into a new territory, what happens to the thirty-eight percent?"),
    row("P3 Stated", "met", [
        "When Rudy left in March he took his notebook with him. And that was the account history for about ninety customers. A paper notebook that walked out the door.",
        "But there's no notes, no, this guy only buys in July, no, don't call before ten. That's all gone.",
    ], "Stated by the manager and confirmed independently by the analyst, who receives what little is left."),
    row("P3 Concrete", "met", [
        "Practically? Two of my guys called Kestrel Fabrication in the same week and neither knew the other had been there, and the buyer told the second one, your company already came in on Tuesday, are you not talking to each other. That was embarrassing. And then we gave away a price on a repeat order because the new guy didn't know what we'd quoted the year before.",
    ], "Two distinct consequences in one named recent instance: the duplicate call the customer noticed, and a price given away on a repeat order. They are separate incidents from the Brightline loss and must not be merged with it."),
    row("P3 Workaround", "met", [
        "I tell people to write things down. That's it. That's my whole system. And I can't make a rep write things down, I've tried.",
        "I get the tab. I get their tab in the workbook, which is usually about a third filled in. And I'll pull their quote history out of P twenty-one for whoever takes over.",
    ], "Both halves of the workaround are named, and the manager says why it cannot hold."),
    row("P3 Reach", "met", [
        "Not exactly. A few hundred dollars of margin on that order. But the Kestrel thing, I mean, they're a good customer, and we looked like a mess.",
        "I'd want it to become the account. We shouldn't have the same company twice, that's half of what's wrong with GoldMine.",
    ], "Reaches the incoming rep, the manager, the analyst, and the customer, who saw the duplication."),
    row("P3 Cost inputs", "partial", [
        "Not exactly. A few hundred dollars of margin on that order. But the Kestrel thing, I mean, they're a good customer, and we looked like a mess.",
    ], "Partial. A few hundred dollars on one order is the only figure, and it is explicitly approximate. Ninety accounts lost their history and one rep's departure triggered it, but no hours, frequency or yearly value is attached, so nothing from P3 enters the bleed. The gap question is what a rep's departure costs in lost orders or discounts across a year, and how often it happens."),
    row("P3 Trajectory", "met", [
        "Four new people with no history, no account records, nothing to hand them except a list out of P twenty-one of who bought what. And Wes managing seven plus four across two states off a legal pad.",
    ], "The VP describes the launch running straight into this pain: four people with nothing to inherit."),
    row("P4 Stated", "met", [
        "I don't. I plan ride-alongs off memory. I couldn't tell you who's actually been in front of a customer in the last ninety days, and that's the part that keeps me up, honestly, because with the new territory I'm going to have four people I've never managed.",
    ], "Stated by the person it affects most, with the ninety-day window in his own words."),
    row("P4 Concrete", "met", [
        "Call reports were a thing we did for about six months in twenty-twenty-one. It was an email at the end of the day. It died because nobody read them, including me.",
        "It matters when I'm asked why a region is down and the honest answer is I don't know if anybody went out there. Gene asked me that in June about Fort Wayne and I didn't have an answer.",
    ], "A previous attempt with dates and the reason it died, plus a specific occasion in June when the gap surfaced."),
    row("P4 Workaround", "partial", [
        "If it was a list I could sort. Not twenty-two emails.",
    ], "Partial. What they do today is ask on the Monday call and remember, and the abandoned call reports are described, but nobody says why continuing to manage visits from memory is unacceptable beyond the new territory arriving. The gap question is what carrying on as-is would mean once he is managing eleven reps across two states."),
    row("P4 Reach", "met", [
        "And if it's slow on a phone in a parking lot, forget it. My guys are not sitting down at a desk. If logging a visit takes more than about a minute in a truck, it won't happen.",
        "It matters when I'm asked why a region is down and the honest answer is I don't know if anybody went out there. Gene asked me that in June about Fort Wayne and I didn't have an answer.",
    ], "Reaches the manager, the reps who would do the logging, the VP answering for a region, and the four incoming reps."),
    row("P4 Cost inputs", "partial", [
        "Four hours. The Monday call is an hour and a half of it and then I'm calling people all week to fill in what they didn't say on the call. And there's three of us doing that.",
    ], "Partial. The manager's four hours a week covers chasing updates generally, not visit coverage specifically, and it is already counted once in the bleed. No separate cost is attached to not knowing who has been visited, and none should be invented. The gap question is what a missed or duplicated visit costs, and how often coverage gaps are found after the fact."),
    row("P4 Trajectory", "met", [
        "and that's the part that keeps me up, honestly, because with the new territory I'm going to have four people I've never managed",
    ], "Forward-looking and specific: eleven reps across two states, four of them new to him, from January."),
]
rubric += per_pain

# ---------------------------------------------------------------------- pains
pains = [
    pain("I cannot tell you today what's going to close this month. I can tell you what twenty-two people told me they hope will close, which is not the same thing.",
         "P1 No shared pipeline: the VP cannot see what will close"),
    pain("A guess. I'll be straight with you.",
         "P1 No shared pipeline: the Friday forecast is a guess"),
    pain("Retyping. Honestly.",
         "P1 No shared pipeline: the analyst re-keys twenty-two differently shaped tabs"),
    pain("A legal pad. I have a drawer of them. If you want to know what happened in March you can go read March.",
         "P1 No shared pipeline: the manager's pipeline is paper"),
    pain("Or in the workbook, for about four days after I ask.",
         "P1 No shared pipeline: the data is stale almost immediately"),
    pain("With four more reps and a territory we've never sold into, the legal pad stops working. It barely works now. I've got seven and I'm at the edge of it.",
         "P1 No shared pipeline: the current method will not survive the launch"),
    pain("We had a sixty-two thousand dollar stocking quote sitting at Brightline for five weeks and nobody touched it.",
         "P2 Quotes go quiet: a named loss after five weeks of silence"),
    pain("Of the quotes over five thousand dollars we sent out last year, thirty-eight percent had no activity after the day they went out.",
         "P2 Quotes go quiet: measured at thirty-eight percent of quotes over five thousand"),
    pain("Nothing. There's no follow-up step. It's whether the rep remembers, and some of them are excellent and some of them are not.",
         "P2 Quotes go quiet: no follow-up step exists at all"),
    pain("P twenty-one will show me an open quote until it expires, but it won't tell anybody to do anything about it, and nobody's looking at that list except me on Tuesday.",
         "P2 Quotes go quiet: the ERP records quotes but prompts nobody"),
    pain("When Rudy left in March he took his notebook with him. And that was the account history for about ninety customers. A paper notebook that walked out the door.",
         "P3 History walks out the door: account knowledge held personally"),
    pain("Practically? Two of my guys called Kestrel Fabrication in the same week and neither knew the other had been there, and the buyer told the second one, your company already came in on Tuesday, are you not talking to each other. That was embarrassing. And then we gave away a price on a repeat order because the new guy didn't know what we'd quoted the year before.",
         "P3 History walks out the door: duplicate call in front of a customer, and a price given away"),
    pain("But there's no notes, no, this guy only buys in July, no, don't call before ten. That's all gone.",
         "P3 History walks out the door: no account preferences survive a handover"),
    pain("I tell people to write things down. That's it. That's my whole system. And I can't make a rep write things down, I've tried.",
         "P3 History walks out the door: the workaround is exhortation"),
    pain("I don't. I plan ride-alongs off memory. I couldn't tell you who's actually been in front of a customer in the last ninety days, and that's the part that keeps me up, honestly, because with the new territory I'm going to have four people I've never managed.",
         "P4 Visit activity invisible: coverage is managed from memory"),
    pain("Call reports were a thing we did for about six months in twenty-twenty-one. It was an email at the end of the day. It died because nobody read them, including me.",
         "P4 Visit activity invisible: the previous attempt died"),
    pain("It matters when I'm asked why a region is down and the honest answer is I don't know if anybody went out there. Gene asked me that in June about Fort Wayne and I didn't have an answer.",
         "P4 Visit activity invisible: the VP cannot answer the president"),
    pain("House accounts. Two hundred-odd companies that buy from us when they happen to call. Nobody's ever worked that list and I've asked for somebody to work it for three years.",
         "P5 House accounts unworked (named, outside the agreed scope for now)"),
    pain("If I weren't rebuilding that workbook twice a week I'd be doing win-loss on the city bids. Nobody has ever looked at why we lose those.",
         "P6 No win-loss analysis on the city bids (named, outside the agreed scope for now)"),
    pain("A spreadsheet. A different spreadsheet. With due dates I update when I remember.",
         "P7 The bid calendar is tracked badly (named and explicitly excluded: 'Separate. Let's not boil the ocean.')"),
    pain("Four new people with no history, no account records, nothing to hand them except a list out of P twenty-one of who bought what. And Wes managing seven plus four across two states off a legal pad.",
         "P8 Nothing to hand a new rep (drives the why-now; onboarding itself was deferred)"),
]

# -------------------------------------------------------------------- numbers
numbers = OrderedDict([
    ("bleed", OrderedDict([
        ("value", "$306,520 a year, built from the client's own inputs and confirmed by the approver. Analyst time: 6 h/wk x $35 loaded x 52 = $10,920. Reps: 22 x 3 h/wk = 66 h/wk x $60 loaded x 52 = $205,920. Managers: 3 x 4 h/wk = 12 h/wk x $70 loaded x 52 = $43,680. Time subtotal $260,520. Unchased quotes: 471 quotes over $5,000 with no activity after issue (38 percent of that year's quotes over $5,000), at the client's own 1-in-20 recovery rate = 23 orders x $2,000 margin (about $8,000 average quote at about 25 points) = $46,000. Total $306,520. The client says it feels low and names what is deliberately left out: his own time and the unworked house accounts. Excluded as a one-off: the $62,000 Brightline stocking quote. The Consultant's larger figure, floated from a half-of-them assumption, was refused and must not appear anywhere."),
        ("quote", "Three hundred and six thousand a year."),
        ("status", "met"),
    ])),
    ("upside", OrderedDict([
        ("value", "About $275,000 of gross margin in the launch year, on about $1.1M of revenue: ramp cut from 9 months to 6 for 4 new reps, each billing at roughly half of a full-ramp $2.2M a year during the quarter gained, so 4 x $275,000 = $1.1M revenue at about 25 points. The client agreed out loud that this is a launch-year figure rather than a recurring one. It does not overlap the bleed and must never be added to it. Two capacity wants named but not quantified: win-loss analysis on the city bids, and working the roughly 200 house accounts nobody calls."),
        ("quote", "And a quarter of that is margin, so two hundred and seventy-five thousand. In the launch year."),
        ("status", "met"),
    ])),
])

# ----------------------------------------------------------------- vocabulary
def v(term, meaning, obj):
    return OrderedDict([("their_term", term), ("meaning", meaning), ("likely_monday_object", obj)])


vocabulary = [
    v("prospect", "A company nobody has sold to yet, arriving from a trade show list, the website form, a rep stopping in, or a buyer moving to a new company",
      "Native CRM Leads board, relabelled to Prospects (board name and item terminology), never a new look-alike 'Prospects' board. Note the account already contains a hand-built Prospects board that must be resolved, not extended"),
    v("opportunity", "An active quote pursuit, used interchangeably with 'quote' for the deal itself",
      "Native CRM Deals/Opportunities board, item terminology relabelled to Opportunity or Quote in their words"),
    v("quote", "Two meanings: the priced document in the ERP, and the deal itself ('I've got a quote out at Brightline'). The client confirmed both uses",
      "The deal is the native Deals item; the document stays in Prophet 21 and is referenced by its quote number. Optionally the native Quotes & Invoices board if they want a document record, which must be asked, not assumed"),
    v("account / customer", "An existing buying company; about 1,100 bought in the last two years, about 400 buy monthly",
      "Native CRM Accounts board (may be relabelled Customers). Never a hand-built 'Customers' board"),
    v("house accounts", "The couple of hundred small accounts with no assigned rep, served by inside sales when they call",
      "A segment or ownership state on the native Accounts board (status or owner field, plus a view), not a separate board and not a separate product"),
    v("stocking agreement", "An agreement to hold a customer's fasteners on the shelf against a year's committed buying; the sticky, high-value deals",
      "A deal type on the native Deals board, with its own stage path or type field; the Brightline loss was one of these"),
    v("blanket order", "Same idea as a stocking agreement in the client's usage ('Blanket order, same idea')",
      "Same deal type as stocking agreement; do not model as a second entity"),
    v("line card", "The set of manufacturer lines they are authorised to distribute, such as the Northgate abrasives line",
      "Possibly the native Products & Services board later, but nobody asked for it; keep as a backlog item in Wes's words"),
    v("the workbook", "The Excel file on SharePoint with a tab per rep plus a formula summary tab; the current pipeline and forecast",
      "Replaced by the native Deals board plus views and a forecast dashboard. Migrate its substance, never its columns"),
    v("the tab", "One rep's sheet inside the workbook, with columns that rep invented in 2019",
      "A per-owner filtered view of the native Deals board, not a board or group per rep"),
    v("P twenty-one / Prophet twenty-one", "Epicor Prophet 21, the ERP: orders, inventory, contract pricing, quoting, invoicing. Explicitly staying",
      "Integration and system of record, not a monday object. The quote number and status live on the deal; the document and pricing stay in the ERP"),
    v("GoldMine", "The legacy CRM, still installed on a Toledo server, last used around 2022 to 2023",
      "Not a monday object. At most a one-time import of the account list, which the client says is the only part worth keeping, and only if asked"),
    v("the branch", "A warehouse, used for Fort Wayne in particular ('calling Fort Wayne to ask a question')",
      "A location field on accounts or deals; the two warehouses are not boards"),
    v("ride-along", "A manager accompanying a rep on customer visits, planned today from memory",
      "An activity type on the native Activities board, plus a coverage view for the manager"),
    v("call report", "The abandoned 2021 practice of emailing a summary of the day's calls",
      "A logged activity on the native Activities board; the client's requirement is that it be a sortable list rather than emails"),
    v("the Monday morning call", "Wes's weekly call where seven reps say what they expect to close and he writes it on a legal pad. 'Monday' here is the weekday, not the product",
      "A saved view or dashboard used live in that meeting; do not read this as a reference to monday.com"),
    v("the forecast", "Delia's Friday roll-up emailed to the VP and the president; from January the president wants a rolling 90-day version monthly",
      "A dashboard or saved view over the native Deals board, with a rolling 90-day window"),
    v("contract pricing / the pricing matrix", "Negotiated customer-specific pricing held in the ERP, confidential across reps",
      "Stays in Prophet 21. Nothing in monday should replicate it, and margin visibility must be restricted"),
    v("points", "Gross margin percentage ('we make about twenty-five points')",
      "A margin percentage field on the deal, visible only to owner, manager, analyst, VP and president"),
    v("requote", "Reissuing a quote at different pricing, which creates a new ERP number for the same pursuit",
      "A new quote number on the same deal, or a linked quote record; not a new deal, and a known source of confusion in the current workbook"),
    v("verbal", "A stage the client uses for a pursuit the customer has committed to informally before the order lands",
      "A stage on the native Deals pipeline, between quoted and won"),
    v("the city bids", "Public-sector bids, such as the City of Hollandale water department, tracked in a separate spreadsheet and a public record",
      "Out of the agreed scope; a backlog item. If built later, note the public-records constraint on what gets written"),
    v("inside sales / counter", "The five people who take orders that come in, and who handle house accounts; surfaced only at the end of the call",
      "Likely users of the same native boards; where they fit is an open question the client raised themselves"),
    v("the launch / western Pennsylvania", "The new territory opening 5 January with four reps, run out of Toledo, about four hours away",
      "A territory or region field and views, not a separate set of boards and not a third warehouse"),
    v("guarantee period", "The new reps' guaranteed compensation window, starting on their start dates",
      "Not a monday object; it is why the January date is a real deadline"),
    v("the inventory count", "The annual physical inventory that takes Delia away from everything else, usually in October",
      "Not a monday object; a scheduling risk for the build and the handover"),
    v("Gene", "The president and second-generation owner, not on the call, informed rather than consulted, wants the monthly forecast",
      "Audience for the forecast dashboard; internally an approver-adjacent stakeholder who must be told"),
    v("Halbrook / Ravi", "The outsourced IT provider and its engineer, who must approve anything touching the ERP",
      "Not a monday object; a gate on the Prophet 21 integration with a one-to-two-week turnaround"),
]

# -------------------------------------------------- entities and workflows
entities = [
    "Prospect intake by four routes: trade show badge-scan spreadsheets, the website form landing in a shared inbox, a rep stopping in at an unfamiliar shop, and a known buyer moving to a new company. Today each lands in the rep's phone, a sticky note, or his tab in the workbook.",
    "Qualification by visit: the rep visits, learns what they buy today and from whom, then asks for a chance to quote.",
    "Quote creation: mostly by the analyst or inside sales in Prophet 21 because of the pricing matrices; contract pricing and stocking agreements always come to the analyst.",
    "Quote follow-up: no step exists. Prophet 21 holds the open quote until it expires and prompts nobody; 38 percent of quotes over $5,000 got no activity after the day they went out.",
    "The pipeline workbook: an Excel file on SharePoint, one tab per rep with rep-invented columns, plus a formula summary tab that breaks about monthly. The analyst pulls open quotes from the ERP each Tuesday, pastes and re-keys them, then chases reps for what is alive.",
    "The Friday forecast: the analyst makes the summary add up and emails it to the VP and the president. From January the president wants a rolling 90-day forecast monthly.",
    "The Monday morning manager call: reps state what they expect to close; the manager records it on a legal pad and spends the rest of the week filling in what was not said.",
    "Order and delivery: orders, inventory, contract pricing and invoicing all run in Prophet 21, which is explicitly staying.",
    "Account ownership and house accounts: most of about 1,100 active accounts are assigned to a rep; a couple of hundred small ones sit unassigned and are served by inside sales when they call.",
    "Rep departure and handover: the leaver's workbook tab (about a third filled in) and an ERP quote history go to the successor; notes, preferences and relationship history do not survive. One departure in March took a paper notebook covering about ninety accounts.",
    "Visit and ride-along planning: done from memory, with no record of who has been in front of a customer in the last ninety days. Call reports existed for six months in 2021 and died because nobody read them.",
    "New territory launch: western Pennsylvania from 5 January, four reps (two signed), first start date 1 December, run out of Toledo about four hours away, on the back of a new abrasives line picked up in June.",
    "New rep onboarding and ramp: historically nine months to a normal book, with nothing to hand a new rep except an ERP list of who bought what. Named as a later item, not in the agreed scope.",
    "Municipal bidding: submissions to bodies such as the City of Hollandale water department, tracked in a separate spreadsheet with due dates updated from memory, and a public record once submitted. Explicitly excluded from this scope.",
    "Existing monday use on the operations side: purchasing runs vendor returns and the Fort Wayne racking project, and there is believed to be a safety audit board. Structure, seats and administrator all unknown.",
    "An abandoned CRM attempt inside the account: the analyst built a Prospects board in April by copying workbook columns, got pulled onto the inventory count, and left about forty rows including test rows with her own name on them.",
]

integrations = [
    "Epicor Prophet 21 (the ERP; must-have connection and explicitly staying: quote number and status to monday, document and pricing staying in the ERP. Version and whether an API or database connection exists are unknown and were made an action for the client)",
    "Halbrook Technology, the outsourced IT provider (gate on anything touching Prophet 21; one to two weeks with a document, longer if anything writes back)",
    "GoldMine (legacy CRM, still installed; only the account list is considered worth keeping, and the activity history is explicitly not trusted)",
    "Microsoft 365: Outlook and Teams (email, calendar and internal chat; the likely route for logging emails and for sign-in)",
    "SharePoint (the pipeline workbook and quote PDFs live here; the workbook is a migration source)",
    "Excel (the workbook itself, plus the separate bid-calendar spreadsheet and the trade show badge-scan exports)",
    "The website enquiry form, which currently dumps into a shared inbox (candidate for a native form or an intake automation into Leads)",
    "Trade show badge scans, arriving as a spreadsheet from whoever ran the booth (a recurring import, not a live integration)",
    "monday.com itself, already in use on the operations side on a Pro plan, with the CRM product present and unused",
]

compliance = [
    "Contract pricing and cross-customer margin are confidential between reps: 'If a rep can see what we give another customer on the same part, I'll have a problem within a week.' Margin visibility is limited to the deal owner, their manager, the analyst, the VP and the president.",
    "The pricing matrix for the whole line card must not be exposed to reps, which is an argument for leaving pricing in the ERP rather than mirroring it into monday.",
    "Municipal bid submissions are public records, so what gets written on those records is constrained. The bid work is outside this scope, but the constraint should be recorded.",
    "Customer contact data (named buyers, their numbers and preferences) would move from personal notebooks and spreadsheets into a shared system, which is the point of the engagement but also makes access permissions part of the design.",
    "Departing-employee risk is a stated driver: account history currently leaves with the person, and the client wants records that stay with the company.",
    "The legacy GoldMine server cannot be switched off for a stated licensing reason, so old customer data continues to sit on an unused internal server.",
    "Microsoft 365 is the identity source and the MSP administers it, so sign-in and provisioning for 22 reps plus inside sales run through Halbrook rather than an internal admin.",
    "Any Prophet 21 connection must be described to the MSP before it is approved, and a connection that writes back to the ERP will face more scrutiny than one that reads.",
]

objections = [
    OrderedDict([("quote", "Honestly, part of me thinks Delia could just build this herself in monday and we keep the money. We've already got the licences. What am I paying for?"),
                 ("type", "We'll build it ourselves (raised by the approver; the spec's skipped step is the workaround check, and the Consultant ran it on the call by asking what had held it up and whose time it would use. The answer was the abandoned Prospects board, the inventory count, and 'live in June' against a December deadline)")]),
    OrderedDict([("quote", "I built a Prospects board in April and it died in three weeks, because I got pulled onto the physical inventory count and never went back."),
                 ("type", "We'll build it ourselves (the same objection, resolved by the client's own evidence: a real DIY attempt that stalled, plus 'I didn't really know how it should be built.' Record the resolution, and do not treat the abandoned board as a starting point without asking)")]),
    OrderedDict([("quote", "The reps. That's the whole risk. If it's one more thing to update, they won't, and then I've paid for GoldMine twice."),
                 ("type", "Team won't adopt it (raised as the main blocker, with six years of unused GoldMine as the precedent. Prevention is an end-user conversation and an end-user demo segment; the design constraints are the one-minute visit log and phone usability)")]),
    OrderedDict([("quote", "The boards purchasing built are a mess, honestly. Things in the wrong place, columns nobody fills in. Is that monday, or is that us?"),
                 ("type", "monday itself is the problem (raised mildly and answered on the call by asking what it fails to do; the client concluded 'probably that's us'. The Consultant committed to reviewing those boards before building rather than proposing a replacement)")]),
    OrderedDict([("quote", "And send me a proposal with a number by the end of next week, would you?"),
                 ("type", "Just send a proposal or pricing (raised, but after scope agreement rather than before it, so the method's precondition is satisfied. What holds the document back is that pricing and proposal prep are outside v1, which the plugin must say plainly and hand to the Consultant)")]),
    OrderedDict([("quote", "We don't have an IT department, we have Halbrook Technology, and Ravi over there has to bless anything that touches P twenty-one."),
                 ("type", "Must check with someone (not about the purchase, which is the VP's own call, but about the ERP connection; ask what Ravi will care about and offer to write the document he will want)")]),
    OrderedDict([("quote", "Then it's a conversation with him and probably with our accountant, and it gets slower. I'd rather stay under it."),
                 ("type", "Price feels high (anticipated, not raised: a stated $40k-a-year signature threshold the client wants to stay under, plus 'We paid for GoldMine for six years and used it for about one.' The bleed is confirmed at $306,520, so the cost-discovery step is already done)")]),
]

commitments = [
    OrderedDict([("quote", "Twenty-third works. Two o'clock. I'm in Toledo that day."),
                 ("what", "Next call: a first version built in the client's own account, 45 minutes, with all three attendees, early enough that changes still fit before December"),
                 ("owner", "Consultant (runs it); all three client attendees confirmed"),
                 ("date", "Wednesday the 23rd, 2:00 pm Eastern (month not stated; the 23rd is a Wednesday in September 2026)")]),
    OrderedDict([("quote", "I'll send the invite when we hang up."),
                 ("what", "Send the calendar invite for the 23rd to the three client attendees"),
                 ("owner", "Consultant"),
                 ("date", "Immediately after the call; stays a to-do until confirmed sent")]),
    OrderedDict([("quote", "Yes. I'll scrub it and send it. Friday?"),
                 ("what", "Send a copy of the pipeline workbook with customer names removed"),
                 ("owner", "Delia Ostrowski"),
                 ("date", "Friday of the week of the call")]),
    OrderedDict([("quote", "I'll email him this week. He'll ask you for a document, I'll warn you now."),
                 ("what", "Ask Halbrook (Ravi) which version of Prophet 21 they run and whether an API or database connection is available"),
                 ("owner", "Marcus Thibault"),
                 ("date", "The week of the call")]),
    OrderedDict([("quote", "[laughs] It'll be a photo of the legal pad. I'll send it tonight."),
                 ("what", "Send whatever exists on visit coverage, expected to be a photograph of the legal pad"),
                 ("owner", "Wes Kubiak"),
                 ("date", "The evening of the call")]),
    OrderedDict([("quote", "I'll look at those boards before I build anything so we're not repeating whatever happened there."),
                 ("what", "Review the existing operations boards in the account before building anything"),
                 ("owner", "Consultant"),
                 ("date", "Before the 23rd")]),
    OrderedDict([("quote", "We won't. It's either the base for this or it gets cleaned up, and I'll come back to you with which."),
                 ("what", "Decide and report back what happens to the abandoned Prospects board, so the account does not end up with two"),
                 ("owner", "Consultant"),
                 ("date", "By the 23rd")]),
    OrderedDict([("quote", "That's a good catch and I'll come back to you about where they fit."),
                 ("what", "Come back on where the five inside sales people fit in the design"),
                 ("owner", "Consultant"),
                 ("date", "By the 23rd")]),
]

traps = [
    "The vocabulary trap is the centre of this fixture. 'Prospects' means leads and 'opportunities' or 'quotes' means deals, and nobody on the call ever says 'lead' or 'deal'. The correct answer maps their words onto the account's native CRM boards by relabelling the board name and item terminology (and the views), not by building boards called Prospects and Quotes beside the native ones. Board names and item terminology prove nothing about nativeness, so renaming is free; recreating the entity is a failure even when every column is right.",
    "'Quote' has two meanings in this account and the client confirmed both: the priced document in Prophet 21, and the pursuit itself. The deal record is the pursuit; the document and the pricing stay in the ERP, referenced by quote number. Building a quoting engine in monday contradicts an explicit instruction ('You're not rebuilding our quoting') and rebuilding the pricing matrix would breach the margin-confidentiality rule as well.",
    "A hand-built Prospects board already exists in the account, created by the sales ops analyst in April and abandoned after three weeks with about forty rows, half of them test rows carrying her own name. It is a look-alike, it is not a starting point, and the client asked that the account not end up with two ('don't leave two of them'). It is also the evidence that resolved the DIY objection. Do not extend it, duplicate it, or seed a demo from its test rows.",
    "The CRM product is present but unused ('a whole sales CRM section in there with nothing in it'), which is not the same as native boards existing. Preflight has to look: if the CRM workspace holds a native install, detect it and record the board ids per entity; if it holds nothing, install monday's native CRM template set rather than hand-building the five entities, and say which was done. Assuming the natives are there because the product is enabled is as wrong as hand-building them.",
    "The tier is stated as Pro, so the Enterprise portfolio default does not fire. Record the tier and the reason no portfolio is proposed. Nothing in this engagement is portfolio-shaped anyway: there are no projects, and the two warehouses and three territories are fields and views.",
    "Twenty-two reps, three territories and two warehouses invite a board per rep, per territory or per branch. The client's own diagnosis of the workbook is that per-rep containers with per-rep columns are the problem. Territory, branch and owner are fields with views over single native boards.",
    "The workbook must not be rebuilt column for column. That is exactly what the analyst did in her abandoned attempt ('I was copying the workbook columns onto a board, which I don't think was right'). Migrate the substance of the pipeline into the native Deals structure; the twenty-two differently shaped tabs are an artefact to retire, not a schema.",
    "'Accounts' is the client's word for existing customers, so the native Accounts board fits with no translation. Do not create a 'Customers' board because the client also says customer, and do not model house accounts as a separate board: they are unassigned accounts, a segment and a view.",
    "The bleed is the client's own $306,520, built from their inputs and confirmed. The Consultant's larger figure, floated from an assumption that half the unchased quotes would have closed, was explicitly refused and is not evidence. Any key or output that carries the Consultant's number instead of the client's has failed the method.",
    "Bleed and upside must not be added together, and the upside is a launch-year figure, not an annual one, which the client agreed out loud. The $62,000 Brightline quote is a one-off and stays out of the yearly figure, as the client said himself.",
    "The 38 percent and the 471 quotes are volume measures that can legitimately appear in an SOP, so they are flagged for the Consultant rather than stripped. The derived margin figures, the loaded hourly costs ($35, $60, $70), the hour inputs and the $306,520 total are bleed material and never appear in anything client-facing.",
    "R12 is Met and R4 and R7 are Met, so the method's pricing-or-proposal gate is open for the first time in this fixture set, and the client asked for a proposal with a number. Pricing and proposal prep are deferred beyond v1, so the correct behaviour is to say plainly that this version does not produce the proposal or the number, hand it to the Consultant with the agreed five-bullet scope in the client's words, and not draft a priced document. Refusing on the grounds that the gate is closed would be wrong; the gate is open.",
    "Service is not in scope and nothing in the call describes a ticket desk. The vendor returns board on the operations side is purchasing's existing work, not a Service opportunity, and Service extras are deferred beyond v1 in any case. Dev is outside v1 and nothing calls for it.",
    "The client named three things as later items in the same breath as agreeing scope: new rep onboarding, the bid calendar and the house account campaign. Plus two capacity wants (win-loss on the city bids, working the house accounts) and one eventual want (line card gap analysis, in Wes's words). All are backlog seeds, and none may quietly enter the first build.",
    "Inside sales surfaced in the last five minutes, raised by the client as something the Consultant had not asked about. Five people who take about a third of the orders are potential users of the same boards, and where they fit is an open question, not an assumption in either direction.",
    "The Brightline Metalworks loss and the Kestrel Fabrication duplicate call are two separate incidents with different causes. Do not merge them, and do not attach the Kestrel price giveaway to the Brightline number.",
    "Two figures about reps must not be confused: twenty-two reps today, twenty-six after the launch. The company is eighty-five people. The launch adds four reps, not a third warehouse and not a new branch.",
    "'one screen on Monday morning' is the outcome the VP described, and 'Monday morning call' is the manager's weekly meeting. Neither is a reference to monday.com, and neither is a dashboard specification.",
    "Success criteria are proposed, not agreed. The president's 'within ten percent' test came secondhand from the VP, and the president was not on the call, so it is recorded as the approver's report of the president's test rather than as an agreed criterion.",
    "The ERP connection is unverified. Nobody knows the Prophet 21 version or whether an API exists; the client took that away as an action. Do not promise a sync, and expect the MSP to take one to two weeks, longer if anything writes back into the ERP.",
    "GoldMine is a migration trap. The client trusts nothing in it except possibly the account list, precisely because some of those companies never bought and so are absent from the ERP. Wholesale import of three-year-old activity history would reintroduce the data everyone distrusts.",
    "Margin and pricing permissions are a hard requirement, not a preference: owner, their manager, the analyst, the VP and the president, never other reps. Any demo seed data and any view has to respect that, and the pricing matrix stays out of monday entirely.",
    "The one-minute rule is a real design constraint from the person whose team must comply: logging a visit from a truck has to be quicker than a minute or it will not happen. A long form on the Activities board fails this even if the field list is correct.",
    "Dates are relative and no call date is stated. The next call is Wednesday the 23rd at 2:00 pm Eastern; the first new rep starts 1 December; the territory launches 5 January; the president's forecast starts in January; Thanksgiving week is unusable for training; the first Monday and Tuesday of each month are order entry. Relative dates fit September 2026.",
    "The abrasives line was picked up in June and the competitor's people are unhappy after an acquisition. Those are why-now context, not requirements, and the competitor should not appear in client-facing material.",
    "Remarks about colleagues and internal candour stay internal: the departed rep taking his notebook, 'some of them are excellent and some of them are not', 'we looked like a mess', the reps treating the old CRM as surveillance, and the analyst's test rows with her own name on them.",
]

requested_changes = [
    OrderedDict([("type", "change"),
                 ("description", "Pre-build requirement: the quote document and the pricing stay in Prophet 21. monday carries the quote number and the pipeline status, and does not become a quoting tool."),
                 ("quote", "Yes. And the quote itself stays in P twenty-one. You're not rebuilding our quoting.")]),
    OrderedDict([("type", "change"),
                 ("description", "Pre-build requirement: one record per company. A prospect that starts buying becomes the account rather than existing twice."),
                 ("quote", "I'd want it to become the account. We shouldn't have the same company twice, that's half of what's wrong with GoldMine.")]),
    OrderedDict([("type", "change"),
                 ("description", "Pre-build requirement: margin on a deal is visible to the owner, their manager, the analyst, the VP and the president only, never to other reps."),
                 ("quote", "Owner, their manager, Delia, me, Gene. Not other reps. Ever.")]),
    OrderedDict([("type", "add"),
                 ("description", "Pre-build requirement: logging a visit must be doable from a phone in a truck in under about a minute."),
                 ("quote", "If logging a visit takes more than about a minute in a truck, it won't happen.")]),
    OrderedDict([("type", "add"),
                 ("description", "Pre-build requirement: visit coverage has to be a sortable list for the manager rather than a stream of emails."),
                 ("quote", "Sortable. Not emails.")]),
    OrderedDict([("type", "change"),
                 ("description", "Pre-build requirement: resolve the abandoned Prospects board so the account does not end up with two prospect lists."),
                 ("quote", "Agreed. I'd add, whatever we do with my Prospects board, don't leave two of them.")]),
]

questions = [
    "Does the CRM product workspace hold a native CRM install already, and where are its Leads, Contacts, Accounts, Deals/Opportunities and Activities boards? If it is genuinely empty, do you want the native CRM template set installed there, or should this live in its own workspace?",
    "What should happen to the Prospects board you started in April: is it retired once the native Leads board is in place, and can its forty rows (minus the test rows) be migrated?",
    "Who administers your monday account today, and how many seats do you have? Twenty-two reps plus five inside sales plus managers is a bigger seat question than the operations boards needed.",
    "Which version of Prophet 21 are you on, and does it expose an API or a reportable database? Until Ravi answers, the quote number and status may have to be entered by hand or imported on a schedule rather than synced.",
    "Should the quote step be a record of its own on the native Quotes & Invoices board, or just the quote number, value and status as fields on the opportunity? Either works; the document and pricing stay in Prophet 21 regardless.",
    "What exactly are the pipeline stages, in your words? The call gave prospect, quoted, verbal, won and lost, and a stalled or no-decision state is implied by the five-week silence but was never named.",
    "How should territory and branch be represented: fields and views over one set of boards, which is what I would recommend, or something else? And does western Pennsylvania need its own view from day one?",
    "Where do the five inside sales people fit? They take about a third of the orders and serve the house accounts, and you raised them yourself at the end of the call.",
    "Do stocking agreements and blanket orders need their own stage path or renewal date on the opportunity, given they are the sticky deals and the Brightline loss was one?",
    "Do you want the GoldMine account list imported, and if so just the companies that never bought and so are missing from Prophet 21? Nothing else from GoldMine, on your own read of it.",
    "What counts as a follow-up for a quote that has gone quiet, and after how many days should it be flagged? Five weeks is clearly too long; the threshold should be yours.",
    "Who should receive the follow-up prompts and the stalled-quote notifications: the rep only, the rep and their manager, or a queue Delia works? This decides the automation recipients.",
    "How should the website form enquiries and the trade show badge-scan spreadsheets arrive: a native form on the Leads board, an import, or an automation from the shared inbox?",
    "The president's 'within ten percent' forecast test came through you. Can we confirm it with him, or at least confirm the reporting shape he wants, before it becomes a success criterion?",
]

verdict = OrderedDict([
    ("verdict", "Discovery complete"),
    ("gates_met", [
        "Solution blueprint: R1 Met and R2 Met, so the blueprint gate is open. The blueprint must map the client's vocabulary onto the account's native CRM boards and record the board ids per entity from preflight first.",
        "Build: no extra method gate beyond the Consultant's approval at the approval stop. There is a real v0.1 to build here, in CRM, once the account questions are answered or listed as assumptions.",
        "First demo (v0.1): nothing extra required. It is already booked for Wednesday the 23rd at 2:00 pm Eastern, framed as a working first version to react to.",
        "Pricing or proposal prep: R4, R7 and R12 are all Met, so the method gate is open, and the client asked for a proposal with a number. This is the first fixture in the set where this gate opens. The v1 product scope still defers pricing and proposal prep, so the correct behaviour is to say that plainly, hand the agreed five-bullet scope to the Consultant in the client's own words, and not draft a priced document.",
    ]),
    ("gates_not_met", [
        "v1.0 sign-off: needs agreed R6 success criteria and R11 Met for every in-scope pain. R11 is Missing because nothing has been shown yet, and the success criteria (one screen on Monday morning, a January forecast within ten percent, knowing who has been visited, no more retyping) are proposed rather than agreed, with the president's test reported secondhand.",
    ]),
    ("note", "R2, R3, R4 and R7 are all Met from client-side quotes, so the verdict is Discovery complete. Two things make this fixture unusual in the set: the approver is in the room and holds the budget, and R12 is Met, so the pricing-or-proposal gate opens on the method while remaining outside v1 as a capability. The gap questions for the 23rd are few and specific: P2 trajectory (what the launch does to the 38 percent), P3 and P4 cost inputs, the P4 workaround, and confirmation of the president's forecast test. The build questions matter more than the grading gaps here, and they are mostly account questions: whether the CRM product workspace holds a native install, what happens to the abandoned Prospects board, seats and administrator, and the Prophet 21 connection the MSP has to approve. The tier is stated as Pro, so no portfolio is proposed and the reason is recorded."),
])

account_context = OrderedDict([
    ("tier", "Pro, stated by the client: 'It says Pro when I log in.' Because the tier is stated and is not Enterprise, the portfolio-by-default rule does not apply and the reason is recorded. Preflight should still confirm the tier and the seat count through the API before building, since a plan change or a per-product tier difference would change the answer."),
    ("products_enabled", [
        "Work Management (core): in use on the operations side. Purchasing runs vendor returns and the Fort Wayne racking project, and there is believed to be a safety audit board.",
        "CRM: present and stated by the client, and essentially unused ('a whole sales CRM section in there with nothing in it, which I've clicked into maybe twice'). This is the product the engagement is built in. Whether its workspace holds a native CRM board install is unknown from the transcript and must be detected in preflight; an enabled product does not imply installed native boards.",
        "Service: never mentioned, and not needed. No ticket or request desk was described, and Service extras are deferred beyond v1 in any case.",
        "dev (software): never mentioned, not needed, and outside v1.",
    ]),
    ("existing_monday_setup", "Bought about nine months before the call for operations. Purchasing uses it for vendor returns and the Fort Wayne racking project, and the VP thinks there is a safety audit board too. Nobody on the call could describe how those boards are structured, who administers the account, or how many seats exist. The sales side has one artefact: a Prospects board the sales ops analyst built in April by copying the workbook's columns, abandoned after three weeks when the physical inventory count took her away, still holding about forty rows of which roughly half are test rows carrying her own name. The regional manager volunteered that the purchasing boards 'are a mess' and asked whether that was monday's fault; the Consultant committed to reviewing them before building. So there is a live account with real but unrelated content, one look-alike sales board to resolve, and an empty CRM product waiting to be set up properly."),
    ("evidence_quote_or_null", "It says Pro when I log in. And there's a whole sales CRM section in there with nothing in it, which I've clicked into maybe twice."),
])

def nb(entity, why):
    return OrderedDict([("product", "crm"), ("entity", entity), ("why", why)])


expected_structures = OrderedDict([
    ("native_boards_required", [
        nb("Leads", "Required. 'Prospect' is their word for a company nobody has sold to yet, arriving from trade show lists, the website form, a rep stopping in, or a buyer moving firms. This is the native Leads board, relabelled to Prospects in the board name and item terminology, with the native convert path to Accounts, Contacts and an opportunity. It is not a new 'Prospects' board, and the abandoned hand-built Prospects board in the account is not an acceptable substitute or starting point. Detection caveat from the live rules: nativeness comes from template lineage walked as a chain, a template view id, or the reserved lead_* column ids, never from the board name."),
        nb("Contacts", "Required. Named buyers and their preferences are the history the client wants to stop losing when a rep leaves ('no notes, no, this guy only buys in July, no, don't call before ten. That's all gone.'). Contacts belong on the native Contacts board, linked to their account, not as people or text columns on the deal. Reserved contact_* ids and lineage identify it."),
        nb("Accounts", "Required, and the vocabulary already matches: 'An account. Or a customer, same thing', about 1,100 active and about 400 buying monthly. House accounts are unassigned accounts on the same board, expressed as an owner state or segment plus a view, not a second board. Renaming to Customers is acceptable; a hand-built Customers board is not."),
        nb("Deals/Opportunities", "Required, and the heart of the build. 'Opportunity' and 'quote' both mean this record: from prospect through quoted, verbal, won or lost, carrying the Prophet 21 quote number, the value, the margin points with restricted visibility, a stocking-agreement or blanket-order type, and a follow-up step so nothing repeats the five-week silence that lost Brightline. Relabel to their word; do not create a 'Quotes' or 'Pipeline' board beside the native one, and do not build one board per rep, territory or branch."),
        nb("Activities", "Required. Logged calls and visits, including ride-alongs, are one of the five agreed scope items, and the manager's requirement is a sortable coverage view rather than emails. These are native Activities records linked to the account, contact and deal, not a hand-built 'Call reports' or 'Visit log' board. Two constraints ride along: logging must take under about a minute from a phone in a truck, and the native Activities board's item terminology in the CRM core template is 'Activity ' with a trailing space, which is a detection quirk to expect rather than to fix."),
        nb("Quotes & Invoices", "Conditional, and a question rather than an assumption. If the client wants a record per quote document (useful because a requote creates a new ERP number for the same pursuit), it belongs on the native Quotes & Invoices board with its line-item subitem board, not on a hand-built 'Quotes' board. The alternative, which is lighter and may be enough, is the quote number, value and status as fields on the opportunity. Either way the document and the pricing stay in Prophet 21."),
        nb("Products & Services", "Conditional and not asked for. The line card was mentioned, and the manager named line-gap analysis as something he would want eventually, explicitly not for December. If that is built later it is the native Products & Services board; do not add it now because the family ships it. Detection note: this board's item terminology is the default 'item', so only the product_and_service_* ids find it."),
    ]),
    ("portfolio_expected", False),
    ("portfolio_reason", "The portfolio-by-default rule applies to Enterprise accounts with Work Management in scope, and neither condition holds. The tier is stated as Pro ('It says Pro when I log in'), and the agreed scope is a CRM engagement: prospects, accounts and contacts, an opportunity pipeline, logged activity and a forecast view. There are no projects to roll up, and the structures that might tempt a portfolio shape are not projects: two warehouses, three regions and a new territory are fields and views over single native boards, and twenty-two reps are owners, not projects. Record the tier and this reason either way. If preflight found an Enterprise tier instead, the rule would apply only to whatever Work Management work came into scope, which today is none."),
    ("lookalike_traps", [
        "Extending, duplicating or demoing from the hand-built Prospects board already in the account, instead of using the native Leads board and resolving that board as the client asked.",
        "Creating a new 'Prospects' board because the client never says 'lead'. The native Leads board relabelled to Prospects is the answer; the word is a label, not a schema.",
        "Creating a 'Quotes', 'Opportunities' or 'Pipeline' board rather than relabelling the native Deals/Opportunities board, which is the easiest mistake to make here because 'quote' is the client's dominant word.",
        "Creating a 'Customers' board for the eleven hundred accounts instead of using the native Accounts board.",
        "Creating a 'House accounts' board for the couple of hundred unassigned accounts, rather than a segment or owner state and a view on Accounts.",
        "Creating a 'Call reports' or 'Visit log' board for logged calls and visits instead of the native Activities board, which the 2021 email-based call reports make tempting to model as its own thing.",
        "Keeping buyers as people or text columns on the opportunity instead of on the native Contacts board, since contacts were discussed mostly as lost notes rather than as records.",
        "Rebuilding the twenty-two-tab workbook as a flat board, column for column, which is exactly the abandoned attempt the analyst described and rejected herself.",
        "One board per rep, per territory or per warehouse, driven by the workbook's per-rep tabs, the three regions and the January territory launch.",
        "Hand-building the five CRM entities in a Work Management workspace because the CRM product workspace looked empty, instead of detecting the native install or installing monday's native CRM template set.",
        "Building a 'Bids' board inside the CRM setup for the city bids, which are both outside the agreed scope and subject to public-records constraints.",
    ]),
    ("notes", "This is a single-product build: monday CRM, on the account's native CRM boards, for all five agreed scope items. Every CRM entity here is governed by the native-board rule, and preflight must detect and record the board ids per entity before the blueprint maps anything onto them; where the CRM workspace turns out to hold no native install, the answer is to install monday's native CRM template set and say so, never to hand-build the entities. The client's vocabulary is carried by relabelling boards, item terminology and views (Prospects, Opportunities or Quotes, Customers or Accounts, visits and ride-alongs), which is free and proves nothing about nativeness either way. Work Management already exists in the account on the operations side and stays outside this scope, though the Consultant committed to reviewing those boards before building; the deferred items (new rep onboarding, the bid calendar, the house account campaign, line-card gap analysis) may land in either product later and belong in the backlog for now. Service and dev are not part of this build and nothing in the call calls for them. Three non-negotiables from the client shape the structure: Prophet 21 keeps the quote document and all pricing, margin is visible only to owner, manager, analyst, VP and president, and a visit must be loggable from a phone in under about a minute. The portfolio question is settled and closed: Pro tier, no projects, reason recorded."),
])

accepted_behaviours = [
    "Proposing a monday CRM build on the account's native CRM boards for all five agreed scope items, with the client's words carried by relabelling board names, item terminology and views rather than by new boards. Any reasonable relabelling passes (Prospects for Leads, Opportunities or Quotes for Deals, Customers for Accounts, visits or call reports for Activities).",
    "Running preflight before any write: confirming the tier and products through the API, detecting the native CRM boards and recording their ids per entity in the client record, and recording the change check. Stopping to ask when the CRM workspace holds no native install, or when detection is ambiguous, is correct behaviour rather than a failure to deliver.",
    "Either resolution of an empty CRM workspace passes: installing monday's native CRM template set and saying so, or asking the Consultant first. Hand-building the five entities does not pass in either case.",
    "Either treatment of the quote step passes, provided it is asked rather than assumed: the native Quotes & Invoices board with its line-item subitems, or the quote number, value and status as fields on the opportunity. What fails is a hand-built Quotes board or anything that reproduces ERP pricing in monday.",
    "Recording the tier as Pro and proposing no portfolio, with the reason recorded. Raising the portfolio only to rule it out is fine; silently dropping the question, or proposing one anyway, is not.",
    "Dealing with the abandoned Prospects board explicitly: migrating its real rows onto the native Leads board and retiring it, or proposing to archive it, and saying which. Leaving two prospect lists, or seeding a demo from its test rows, fails.",
    "Not proposing monday Service or dev, and not reading purchasing's vendor returns board as a Service opportunity.",
    "Stating the bleed as the client's own confirmed $306,520 a year (or 'Three hundred and six thousand'), without rounding up, without the Consultant's rejected larger figure, without the one-off Brightline $62,000, and without adding the upside to it. Reporting the upside separately and as a launch-year figure passes; presenting it as recurring does not.",
    "Grading the verdict Discovery complete and saying plainly that the pricing-or-proposal gate is open on the method (R4, R7 and R12 all Met) while pricing and proposal prep are outside this version, so the number and the document are the Consultant's to produce. Handing over the agreed five-bullet scope in the client's words is the useful output here.",
    "Treating the 'build it ourselves' objection the way the call did: the workaround question rather than a defence, the client's own stalled attempt and December deadline as the answer, and no invented claims. Conceding that some of it could be built in-house, as the Consultant did, is acceptable and in character for the method.",
    "Treating the 'is monday the problem' question as a current-state question, and reviewing the existing operations boards before building rather than proposing to replace them.",
    "Carrying the three client-stated non-negotiables into the design: Prophet 21 keeps quoting and pricing, margin visibility is restricted to owner, manager, analyst, VP and president, and logging a visit from a truck stays under about a minute.",
    "Turning the Prophet 21 connection into a question and a document for the MSP rather than a promised sync, and planning for one to two weeks of approval, longer if anything writes back to the ERP.",
    "Keeping the deferred items in the backlog in the client's words (new rep onboarding, the bid calendar, the house account campaign, win-loss on the city bids, line-card gap analysis) and out of the first build.",
    "Presenting the automations, including the quote follow-up prompts and stalled-quote notifications, as one approval list with trigger, conditions, action and exact recipients per row, noting that automations created through the API cannot be switched off through the API, with a 'turn off in monday' step in the handoff. Asking who receives the follow-up prompts rather than assuming is part of this.",
    "Designing around the client's calendar: usable before 1 December, no training in Thanksgiving week, and reps unavailable the first Monday and Tuesday of each month.",
    "Marking the success criteria as proposed rather than agreed, and flagging that the president's 'within ten percent' test came secondhand from the VP.",
]

leak_blocklist = [
    "The bleed total in every form: 306520, 306,520, $306,520, '$306k', 'three hundred and six thousand', 'three hundred and six thousand five hundred and twenty'.",
    "Bleed components and subtotals: 260520, 260,520, '$260,520', 'two hundred and sixty thousand five hundred and twenty'; 205920, 205,920, '$205,920', 'two hundred and five thousand nine hundred and twenty'; 43680, 43,680, '$43,680', 'forty-three thousand six hundred and eighty'; 10920, 10,920, '$10,920', 'ten thousand nine hundred and twenty'; 46000, '$46,000', 'forty-six thousand'.",
    "Loaded hourly costs and the words around them: 35, '$35', 'thirty-five an hour', 'Delia loaded'; 60, '$60', 'sixty an hour'; 70, '$70', 'seventy an hour loaded'; and any phrase pairing hours with a rate or a yearly total.",
    "Hour inputs behind the math: 'six hours a week', 'three hours a week', 'four hours', 'sixty-six hours', 'twelve hours a week', 'times fifty-two', and the derived per-week figures.",
    "The Consultant's rejected figure and the assumption behind it: 'four hundred and seventy thousand', 'half of those', and any total built from a half-of-them recovery rate.",
    "Upside figures and their inputs: 275000, 275,000, '$275,000', 'two hundred and seventy-five thousand'; 'one point one million'; 'two point two million' as a per-rep revenue figure; the nine-to-six-month ramp comparison; 'a quarter of that is margin'.",
    "Margin percentages and their shorthand next to any figure: 'twenty-five points', '25 percent margin', 'two thousand a quote', 'about eight thousand' as an average quote value.",
    "The one-off loss amounts: 62000, '$62,000', 'sixty-two thousand', 'the Brightline sixty-two', and 'A few hundred dollars of margin on that order'.",
    "Budget mechanics and the spend threshold: 'forty thousand a year', '$40k', who signs above it, 'I'd rather stay under it', and the expectation of staying below the president's signature line.",
    "Stakeholder assessments: that the VP is the approver and the president is informed rather than consulted, that the analyst is the single point of failure and the named day-to-day owner, that the MSP engineer is 'reasonable but he's slow', and that the reps are the adoption risk.",
    "Objection text and planned responses, raised or anticipated: 'What am I paying for?', 'I've paid for GoldMine twice', 'The boards purchasing built are a mess', 'Is that monday, or is that us?', and anything about how the build-it-ourselves question was handled.",
    "The stalled DIY attempt as an argument: that the analyst's Prospects board died in three weeks, that she 'didn't really know how it should be built', and the reading that in-house delivery would land in June. The board itself may be discussed neutrally in a handover note as data to migrate or archive.",
    "Emotional and personal stakes: 'That number made me feel sick, honestly', 'that's the part that keeps me up', 'That was embarrassing', 'we looked like a mess', and 'I'll get excited and then I'll be wrong in front of Gene'.",
    "Remarks by client staff about colleagues: 'some of them are excellent and some of them are not', the reps deciding the old CRM was a surveillance tool, 'the reps are useless for anything else Monday and Tuesday', that a departing rep took his notebook, and the test rows carrying the analyst's own name.",
    "Readiness and method vocabulary: bleed, upside, callback, exit ramp, seed, readiness, gate status, P1 to P8, R1 to R12, [found] and [inferred] markers, verdict wording such as 'Discovery complete'.",
    "Competitive and relationship context: that Vantage Industrial won the Brightline order, that a competitor in the new territory was sold to a national and their people are unhappy, and how the loss was discovered ('mentioned it at a golf thing').",
    "Named customers attached to failures, in any client-facing document that is not for the people involved: Brightline Metalworks as a loss, Kestrel Fabrication as the duplicate-call incident, and the departed rep's name.",
    "Pricing strategy of any kind for the engagement itself, including the proposal the client asked for, any rate, and any comparison between the engagement cost and the bleed. Pricing and proposal prep are outside this version, and the figures stay with the Consultant.",
    "Volume numbers are a flag for the Consultant rather than an automatic removal, because they can be legitimate in an SOP: 'thirty-eight percent', 'four hundred and seventy-one' quotes, about 1,100 accounts, about 400 monthly buyers, a couple of hundred house accounts, 22 reps, 26 reps after the launch, 85 employees, and about 90 accounts on the departed rep's notebook.",
]

key = OrderedDict([
    ("scenario_id", "s6-discovery-crm-sales"),
    ("call_type", "discovery"),
    ("purpose_of_this_fixture",
     "Tests the classic sales-team CRM engagement the fixture set was missing: a strong 45-minute discovery call with a B2B industrial supplies distributor of about 85 people (22 outside reps, 2 warehouses) that runs its pipeline on a 22-tab Excel workbook plus a legacy CRM nobody has opened since 2023. Four things are under test. (1) The vocabulary trap. They say 'prospects' for leads and 'opportunities' or 'quotes' for deals, and never say lead or deal. The right answer maps those words onto the account's NATIVE CRM template boards (Leads, Contacts, Accounts, Deals/Opportunities, Activities) by relabelling board names, item terminology and views, never by building look-alike boards called Prospects and Quotes. A hand-built Prospects board already sits abandoned in the account, which makes the wrong answer feel available; the client also asked not to end up with two. (2) Account facts that are stated rather than unknown for once: the tier is Pro and the CRM product is enabled and empty. So the Enterprise portfolio default must NOT fire, the reason must be recorded, and the plugin must not confuse an enabled product with an installed native board set: preflight has to look, and install monday's native CRM template set if the workspace is bare. (3) Grading. R1 to R10 and R12 all Met, R11 Missing, verdict 'Discovery complete'. Per pain: P1, P2 and P3 excavated; P2 Trajectory Partial; P3 Cost inputs Partial; P4 Workaround and Cost inputs Partial. The bleed is the client's own $306,520 a year, built out loud by their analyst and confirmed by the VP, after the VP refused the Consultant's larger figure; the upside is a $275,000 launch-year margin figure that must not be added to the bleed. (4) The gate that has never opened in this set. R4, R7 and R12 are all Met and the client asks for a proposal with a number, so the method's pricing-or-proposal gate is open. Pricing and proposal prep are deferred beyond v1, so the plugin must say that plainly, hand the agreed five-bullet scope to the Consultant in the client's words, and not draft a priced document. The objection 'we'll just build it ourselves' is raised by the approver and answered with the workaround question. A milder 'monday itself is the problem' is raised about the existing operations boards and resolved on the call."),
    ("transcript_format",
     "Plain text, one line per turn, in the form '[MM:SS] Speaker Name: text', with no blank lines between turns. 270 turns from [00:03] to [42:22], about 5,390 spoken words, client talk share about 67 percent. The consultant is labelled 'Consultant' with no name, role or gendered pronoun. Timestamps are minutes and seconds only, so locations in this key are written '[MM:SS] Speaker Name (role)', for example '[12:20] Delia Ostrowski (Sales Operations Analyst)', and '[13:38] Consultant' style without a role for the consultant. Speech is lightly disfluent and carries '[laughs]' twice; nothing is tidied. The call date is not stated anywhere; relative dates fit September 2026, with the next call on Wednesday the 23rd. Note two transcript artefacts: 'Monday' appears as a weekday ('the Monday morning call') as well as the product name 'monday', and the ERP is spoken as 'P twenty-one' and 'Prophet twenty-one' rather than written as P21."),
    ("company", OrderedDict([
        ("name", "Calderwood Industrial Supply"),
        ("industry", "B2B industrial supplies distribution: fasteners, abrasives, cutting tools, safety equipment and general MRO consumables, sold to fabricators, machine shops, food plants and municipalities"),
        ("size", "About 85 employees: 22 outside sales reps, 5 inside sales and counter staff, 3 regional sales managers, and one sales operations analyst. Four more reps join for the new territory, taking outside sales to 26."),
        ("locations", "Two warehouses: Toledo, Ohio (main site, where the VP of Sales sits) and Fort Wayne, Indiana. A new sales territory in western Pennsylvania launches 5 January, served out of Toledo, about four hours away."),
        ("current_tools", [
            "Epicor Prophet 21 ('P twenty-one'), the ERP: orders, inventory, contract pricing, quoting and invoicing. Explicitly staying.",
            "Excel on SharePoint: the pipeline workbook, one tab per rep plus a formula summary tab, and a separate bid-calendar spreadsheet.",
            "GoldMine, the legacy CRM, still installed on a Toledo server and unopened since about 2023.",
            "Microsoft 365: Outlook and Teams.",
            "SharePoint (the workbook and quote PDFs).",
            "monday.com: Pro plan, about nine months old, used by purchasing for vendor returns and the Fort Wayne racking project, plus a believed safety audit board, and one abandoned Prospects board built by the sales ops analyst.",
            "A website enquiry form that lands in a shared inbox.",
            "Trade show badge scans, returned as a spreadsheet.",
            "Halbrook Technology, the outsourced IT provider, which administers Microsoft 365 and gatekeeps the ERP.",
        ]),
    ])),
    ("attendees", [
        OrderedDict([("name", "Consultant"), ("role", "monday.com consultant running the discovery call"),
                     ("side", "consultant"), ("decision_role", "not applicable")]),
        OrderedDict([("name", "Marcus Thibault"), ("role", "VP of Sales"), ("side", "client"),
                     ("decision_role", "approver (decides and holds the budget line: 'This is my call.' No signature needed from the president under $40k a year, and the president is told rather than asked)")]),
        OrderedDict([("name", "Delia Ostrowski"), ("role", "Sales Operations Analyst (the only sales ops person)"),
                     ("side", "client"),
                     ("decision_role", "admin/owner (named as the day-to-day owner of whatever is built, and the person who would have to keep it alive; also the heaviest end user and the author of the abandoned Prospects board)")]),
        OrderedDict([("name", "Wes Kubiak"), ("role", "Regional Sales Manager (Fort Wayne and west, seven reps, and the new western Pennsylvania territory from January)"),
                     ("side", "client"),
                     ("decision_role", "influencer and end user (owns the weekly pipeline call and visit coverage; his team's adoption is the stated risk)")]),
    ]),
    ("expected_monday_products", [
        OrderedDict([("kind", "crm"), ("why", "The build, and the whole of it. All five agreed scope items are CRM entities: prospects (native Leads, relabelled), accounts and contacts with history that survives a departure (native Accounts and Contacts), the opportunity pipeline carrying the Prophet 21 quote number with a follow-up step (native Deals/Opportunities), logged calls and visits including ride-alongs with a sortable coverage view (native Activities), and a forecast view for the VP and the president that replaces the Friday workbook. CRM is in v1 scope and must be built on the account's own native CRM template boards, detected and recorded per entity in preflight first, relabelled to the client's vocabulary where that helps, and never re-created as look-alike boards. The CRM product is enabled and empty, so if the workspace holds no native install the native template set is installed rather than hand-built. Optional and to be asked: the native Quotes & Invoices board for a per-document record, since a requote creates a new ERP number for the same pursuit.")]),
        OrderedDict([("kind", "core"), ("why", "Already present and deliberately out of this scope. Purchasing runs vendor returns and the Fort Wayne racking project on Work Management boards, and there is believed to be a safety audit board; the Consultant committed to reviewing those before building, because the manager asked whether their messiness was monday's fault. Nothing in the agreed five belongs there, and no sales entity may be modelled on a Work Management board because the CRM workspace looked empty. The deferred items could land here later (new rep onboarding checklists, the bid calendar) and stay in the backlog until asked for. monday Service and dev are not proposed at all: no ticket or request desk was described, the vendor returns board is purchasing's existing work rather than a Service opportunity, Service extras are deferred beyond v1, and dev is outside v1 with nothing in the call calling for it.")]),
    ]),
    ("rubric", rubric),
    ("pains", pains),
    ("numbers", numbers),
    ("vocabulary", vocabulary),
    ("entities_and_workflows", entities),
    ("integrations_mentioned", integrations),
    ("compliance_or_security_signals", compliance),
    ("objections", objections),
    ("commitments_and_next_steps", commitments),
    ("traps", traps),
    ("requested_changes", requested_changes),
    ("should_plugin_propose_a_build", True),
    ("expected_questions_before_building", questions),
    ("expected_verdict", verdict),
    ("account_context", account_context),
    ("expected_structures", expected_structures),
    ("accepted_behaviours", accepted_behaviours),
    ("expected_leak_blocklist", leak_blocklist),
])

if errors:
    print("QUOTE RESOLUTION FAILURES:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

out = BASE + "answer-key.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(key, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("wrote", out)
print("rubric rows:", len(rubric), "| pains:", len(pains), "| vocabulary:", len(vocabulary),
      "| traps:", len(traps), "| questions:", len(questions))
