"""Builds fixtures/s18-identity-collapse/answer-key.json.

Every location is looked up from the transcript; every quote must be a unique single-line substring.
Do not re-run after review: it overwrites the reviewed key. check.py is the read-only checker.
"""
import json, re, sys
from collections import OrderedDict, Counter

DIR = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s18-identity-collapse/"
tx = open(DIR + "transcript.txt").read()
LINES = tx.split("\n")
PAT = re.compile(r"^\[(\d\d:\d\d:\d\d)\] ([A-Za-z ]+): (.*)$")
TURNS = [(m.group(1), m.group(2), m.group(3)) for m in (PAT.match(l) for l in LINES) if m]
BY_STAMP = {t[0]: t for t in TURNS}
LABELS = ["Consultant", "Tadhg Devlin", "Jon Ashby", "John Rudge", "Maxine Bassett"]


def find(sub):
    hits = [t for t in TURNS if sub in t[2]]
    if len(hits) != 1:
        sys.exit("quote not unique (%d hits): %r" % (len(hits), sub[:80]))
    return hits[0]


def q(sub, stamp=None):
    st, lab, _ = find(sub)
    if stamp and stamp != st:
        sys.exit("stamp mismatch for %r: %s != %s" % (sub[:60], st, stamp))
    return OrderedDict([("quote", sub), ("location", "%s %s" % (st, lab))])


def qo(sub):
    find(sub)
    return sub


def stamp_of(sub):
    return find(sub)[0]


def row(criterion, status, evidence, note, asked, asked_q=None):
    r = OrderedDict([("criterion", criterion), ("status", status), ("evidence", evidence), ("note", note), ("asked", asked)])
    if asked and asked_q:
        r["asked_quote"] = q(asked_q)
    return r


# measurements
words_by = Counter()
for st, lab, text in TURNS:
    words_by[lab] += len(text.split())
TOT = sum(words_by.values())
client_words = TOT - words_by["Consultant"]
short = sum(1 for t in TURNS if len(t[2].split()) <= 4)
lower = sum(1 for t in TURNS if t[2][0].islower())
unterm = sum(1 for t in TURNS if t[2].rstrip()[-1] not in ".?!\"")
longest = max(TURNS, key=lambda t: len(t[2].split()))
same_pairs = sum(1 for a, b in zip(TURNS, TURNS[1:]) if a[1] == b[1])
turns_by = Counter(t[1] for t in TURNS)


def secs(s):
    h, m, ss = s.split(":")
    return int(h) * 3600 + int(m) * 60 + int(ss)


gaps = [secs(b[0]) - secs(a[0]) for a, b in zip(TURNS, TURNS[1:])]
markers = Counter(re.findall(r"\[(laughs|crosstalk|inaudible|dog barks)\]", tx))

K = OrderedDict()
K["scenario_id"] = "s18-identity-collapse"
K["call_type"] = "discovery"
K["purpose_of_this_fixture"] = (
    "Calibration fixture for the identity-collapse case (REAL-CALL-LESSONS C60; BUILD-PLAN 4.2 row s18; headless run H44). A first-hand discovery call with a marina and boatyard, exported as a plain block transcript whose labels are structurally clean and whose spoken names are not. The general manager is labelled 'Tadhg Devlin' and is never once rendered that way in speech: the export gives him Tige, Tyge, Teague and Tighe, 'Tige Devlin' in his own introduction, 'Tige Devon' in our read-back, Devlin as a possessive, the ordinary English words tie, tag and tide in three vocative slots, a family nickname (Thady) that matches no roster entry on any string basis, and the role forms 'the GM' and 'general manager': thirteen surface forms for one person. The workshop manager speaks every one of her turns under the label 'Maxine Bassett', the absent office administrator whose laptop she borrowed, and is only ever called Bernie, Bernie Locke or Bernadette. The marina manager 'Jon Ashby' and the finance manager 'John Rudge' are both rendered 'John' in all twenty-one spoken mentions, and the humans confuse them twice. "
    "The key carries the alias map and asserts the repair: every form binds by adjacency pair first, then by phonetic key and edit distance against the roster; a coerced ordinary word passes the vocative-slot test and is logged, while the sixteen ordinary uses of the same three words are left alone; the nickname binds only by its answered adjacency pair; the borrowed label resolves to the person who spoke under it without anyone being invented from the label; the shared 'John' token is resolved occurrence by occurrence, one occurrence is left honestly ambiguous, and the two colleagues are never merged; the alias table is proposed once for the user's confirmation; and no person is created for Tige, Tyge, Teague, Tighe, Devon, Thady, the three words, the dog, a second Bernie, a third John or a speaking Maxine. Beside the intake assertions the 25 fields grade the call itself: Discovery complete with R1 and R4 met-with-residual, R5 and R12 partial, R11 missing and P4 Cost inputs not obtainable from this room; two excavated pains; a client-built bleed of ninety-six and a half thousand a year in pounds; and a Work Management build for the lift-out list with tide-windowed hoist slots and the job card, with the client's two systems of record left exactly as they are."
)
K["transcript_format"] = (
    "Plain text, %d lines: a three-line human-readable export header (a title line, 'Recording length: 00:45:02', and 'Participants (5): Consultant, Tadhg Devlin, Jon Ashby, John Rudge, Maxine Bassett'), a blank line, then %d turns, one per line, in the form '[HH:MM:SS] Label: text'. Stamps are start times at one-second resolution from [00:00:03] to [00:44:57], strictly increasing, no collisions, no end times, no call date. Five labels, all as the platform saw them: 'Consultant', 'Tadhg Devlin', 'Jon Ashby', 'John Rudge' and 'Maxine Bassett', the last a borrowed laptop under which Bernie Locke speaks throughout. About %s spoken words; client share about %d percent by words (Tadhg Devlin %.1f, Jon Ashby %.1f, John Rudge %.1f, the borrowed label %.1f). Longest unit %d words, our side, the first-cut play-back at 00:38:40. No adjacent same-label pair. Two units begin lowercase, both of them coerced vocatives (tag at 00:05:49, tide at 00:15:03; the third, tie at 00:11:11, sits after 'Right,'); every unit ends in terminal punctuation; %d units are four words or fewer. Bracketed cues: [laughs] %d, [crosstalk] %d, [inaudible] %d, [dog barks] %d. Currency is pounds. Every location in this key is 'HH:MM:SS Label' with the label exactly as printed, so Bernie's turns are located under 'Maxine Bassett'; the attendees field and the intake block carry the resolution. Every quote sits inside exactly one line. Weekday clues (three weeks on Monday is the twelfth, Monday the fifth, the fourteenth of October, back on the twenty-eighth) fit a call in the week of 21 September 2026; the date is not stated."
    % (len(LINES) - 1, len(TURNS), "{:,}".format(TOT), round(100.0 * client_words / TOT), 100.0 * words_by["Tadhg Devlin"] / TOT, 100.0 * words_by["Jon Ashby"] / TOT, 100.0 * words_by["John Rudge"] / TOT, 100.0 * words_by["Maxine Bassett"] / TOT, len(longest[2].split()), short, markers["laughs"], markers["crosstalk"], markers["inaudible"], markers["dog barks"])
)
K["company"] = OrderedDict([
    ("name", "Brindlehaven Marina"),
    ("industry", "Marina and boatyard: annual berthing on pontoons and swinging moorings, a fuel berth and chandlery, and a yard that lifts about three hundred and forty boats out each autumn and back in each spring with a fifty-tonne hoist, storing them on hardstanding and doing workshop jobs (antifoul, anodes, engine services) while they are out. Customers are private boat owners, called owners; a small number of visitor lifts for surveys."),
    ("size", "Forty-six staff, nearer sixty in summer with seasonal yard crew; nine workshop engineers; four hundred and twenty berths and about a hundred and eighty moorings; sixty more berths on C pontoon from March."),
    ("locations", "One site on a tidal river: the yard office (the general manager, the dog), the marina office at the pontoon end (the marina manager), an upstairs office (finance), a workshop with a mezzanine, three acres of hardstanding without Wi-Fi, and the hoist dock, which dries out, so lifts happen two hours either side of high water. A competitor marina sits across the water."),
    ("current_tools", [
        "The book: the office administrator's spreadsheet with a lift-out tab and a launches tab, one line per boat; twenty years old, colour-coded, and touched by nobody else",
        "The hoist board: a whiteboard in the yard office with a column per day, filled on Fridays from the book; the yard crew work from a printed sheet off it each morning",
        "The job card: a triplicate paper pad written off the book; top copy to the workshop wall (a whiteboard with hooks), second copy in the office, third copy cable-tied to the boat",
        "The berthing system: contracts, direct debits, berth allocation and the waiting list; the book of record for berths and never to be moved or written to",
        "The accounts package: invoices typed from signed job cards, six to eight weeks late in April",
        "Phone and email for bookings and owner calls. The tide tables for the hoist window. A task app tried on a free trial two summers ago and abandoned",
    ]),
])
K["attendees"] = [
    OrderedDict([("name", "Tadhg Devlin (labelled 'Tadhg Devlin'; rendered in speech as Tige, Tyge, Teague, Tighe, Tige Devlin, Tige Devon, Devlin, tie, tag, tide, Thady and 'the GM')"), ("role", "General manager, fourteen years at the marina and six in the role; everything between the water and the yard is his; approves operational spend up to twenty thousand; walks the launch list every April morning."), ("side", "client"), ("decision_role", "approver (up to twenty thousand; the chairman and the family board sign above it and were not on the call)")]),
    OrderedDict([("name", "Jon Ashby (labelled 'Jon Ashby'; rendered 'John' in speech, also Jonny, Ashby, 'the wet John')"), ("role", "Marina manager: berths, moorings, the hoist and its slots, the yard crew; builds the hoist board from the book each Friday and rings the office at half six each morning."), ("side", "client"), ("decision_role", "influencer (and end user; speaks for the hoist driver and the yard crew)")]),
    OrderedDict([("name", "John Rudge (labelled 'John Rudge'; rendered 'John' in speech, also Rudge, 'the dry John')"), ("role", "Finance and admin manager: invoices from job cards, credits, the loaded rates, the budget line; the office administrator reports to him; holds the veto on anything touching the berthing system."), ("side", "client"), ("decision_role", "influencer (gate-holder on both systems of record: berths and invoicing)")]),
    OrderedDict([("name", "Bernie Locke (labelled 'Maxine Bassett' throughout, the absent office administrator's laptop; spoken as Bernie, Bernie Locke, Bernadette)"), ("role", "Workshop manager: assigns the nine engineers from a whiteboard wall, chases hours on Fridays, orders parts, signs cards; the person who found the card in the skip."), ("side", "client"), ("decision_role", "end user (and the likely admin/owner of the workshop side; wants the wall to become a view she runs)")]),
    OrderedDict([("name", "Consultant"), ("role", "monday.com consultant running the discovery call"), ("side", "consultant"), ("decision_role", "not applicable")]),
]
K["expected_monday_products"] = [OrderedDict([("kind", "core"), ("why", "Work Management for the two pieces played back and accepted as a first cut: the lift-out list (one line a boat, the hoist slot and the tide window on it, a printed sheet each morning) and the job card (hours, parts as fields, the launch date red inside a fortnight, the insurance yes/no and the lift record), with the workshop wall becoming a view. Owner notification is a later piece. The berthing system stays the book of record for berths and is never written to. The accounts package is never written to either. Parts ordering and the shop are out. No CRM: nothing here is a pipeline and berth contracts stay where they are. No Service: an owner request is a line on a card, not a ticket, and owners do not type in the first go. Dev is out of v1 and nothing here is software work. There is no account and no tier, so no portfolio is assumed.")])]

RUB = []
RUB.append(row("R1 Current state mapped", "met-with-residual", [
    q("They ring the office. Or they email the office, or they catch me on the pontoon and I write it on my hand. Most of them ring. Maxine takes it. She puts it in the book."),
    q("Then, on the Friday, I print the next week out of the book and I put the boats onto the hoist board, which is a whiteboard in the yard office, a column a day, and the lads work off a printed sheet from that each morning."),
    q("When she takes the booking she writes a card off the book. Triplicate pad."),
    q("In theory the top copy comes to me and I put it on my wall, which is a whiteboard with hooks on it, one hook a boat, and I give it to an engineer, and he takes it to the boat and writes his hours on it, and when the job's done it comes back to me and I sign it and it goes upstairs to John."),
    q("I type it into the accounts package. Boat, owner, hours times the rate, parts off the card, and it goes out to the owner."),
    q("And then in February half of them ring and move it, and the new date goes in the book, and the card on the boat still says the old date."),
    q("The berthing system. Contracts, direct debits, who's on which berth, the waiting list."),
], "The client walks a boat end to end: the booking by phone, the book, the Friday transfer to the hoist board and the printed sheet, the tide window, the card written off the book in triplicate, the workshop wall, hours on the card or not, the signed card upstairs, the invoice, the launches tab and the February date changes, the berthing system beside it all. The residual: the office steps (how a booking is keyed, the colours in the book, the launches tab, the weights held in the administrator's head) are described second-hand because the office administrator is on leave ('So we're describing her bit second-hand, which she'd hate.' 00:08:32), and are carried as questions for the twenty-eighth. Met-with-residual, not partial: the map is complete, one owner of it was not in the room.", True, "Okay. Let's walk it. Start me at the beginning. A boat's in the water, it's September, the owner wants it out for the winter. What happens?"))
RUB.append(row("R2 Pain made concrete", "met", [
    q("And this April, forty-one of them weren't ready on their date."),
    q("Saturday the eighteenth of April. Nineteen launches booked. Six ready."),
    q("I know it was twenty-six because Lorcan and I did most of it ourselves. The card said fourteen because that's what was on it when I fished it out."),
    q("And a forty-two-foot boat hanging in the slings for forty minutes while three of us argued about whose was next, with the tide going out under it."),
], "Two pains are excavated: P1 (boats miss their launch date because the card and the book disagree) and P2 (workshop hours never reach the card). P3 (the hoist double-booked from three sources) is concrete with a partial workaround; P4 (owners chase status by phone) is stated with no count. Every load-bearing quote is a single clean unit under a clean label.", True, "Tell me about April."))
RUB.append(row("R3 Why now", "met", [
    q("April. And the pontoon. They're the same thing, really."),
    q("eleven owners didn't renew. Eleven annual berths walked across the water to the place opposite."),
    q("C pontoon. Sixty new berths, built, in the water in March."),
    q("So that's the why now."),
], "A client-side event (forty-one boats late in April, eleven berths lost), a client-side change (sixty more berths from March) and the chairman's ultimatum in May. The ultimatum is relayed by the general manager ('and I'm quoting') and is recorded as his account of it, never as the chairman's statement; the why-now stands on the two client-side facts without it.", True, "Tyge, what made you pick up the phone now, rather than a year ago?"))
RUB.append(row("R4 Bleed number", "met-with-residual", [
    q("Three, nine engineers, that's twenty-seven hours a week. We charge fifty-eight an hour. Forty-six weeks, because the workshop's dead over Christmas and half of August."),
    q("Nine thousand four hundred and twelve, in goodwill credits, April and May, all of it launch dates."),
    q("Nineteen an hour loaded, forty-eight weeks. Eleven thousand, near enough. That one's my estimate, not Maxine's, so it's soft."),
    q("Seventy-two, plus eleven, plus thirteen and a half. Ninety-six and a half thousand. A year."),
    q("Ninety-six and a half. I'd sign that. It's light, but I'd sign it."),
], "Client-built and confirmed by the approver: unbilled workshop hours (27 h/wk x 58 x 46 = 72,036), office retyping (12 h/wk x 19 loaded x 48 = 10,944) and credits plus uncharged re-lifts (9,412 + 23 x 180 = 13,552), which the finance manager rounds aloud to ninety-six and a half thousand. The residual, carried as one gap question: the hours are hedged three to four and the client chose three ('Say three, so John doesn't accuse me of making it up.' 00:27:53); the office line is the finance manager's estimate for an absent colleague and he calls it soft. Set aside by the client and kept beside the number, never in it: the eleven lost berths at forty-six thousand two hundred a year (00:29:28), the workshop manager's own time, parts written off and the hoist driver's overtime (00:29:52).", True, "We're about to do the money, and I want yours, not mine. Rudge, you've got the credits."))
RUB.append(row("R5 Upside number", "partial", [
    q("Sixty at four thousand two hundred is two hundred and fifty-two thousand a year in berthing"),
    q("I can't split that for you. All of it if April happens again. None of it if it doesn't. It's not a number I can give you honestly."),
], "A figure exists, but it is the new pontoon's berthing revenue, and the general manager declines to attribute any share of it to this work. Recorded as the pontoon's number with a dependency on this project, as our side proposed at 00:30:52, not as this project's upside. Partial, not not-obtainable: the room could and did give a number; it is the link that is unquantified.", True, "If this worked, what's the upside, in money? Not the pain going away, the thing you'd win."))
RUB.append(row("R6 Desired outcome", "met", [
    q("One list. A boat comes out, and everything about it, the jobs, the parts, the launch date, who's on it, is in one place, and on a Monday morning I can see which ones won't make their date, and the owner's been told a week before, not on the day."),
    q("Write fewer than five. I'm not a fool. Five, and every one of them warned."),
    q("And the hours. Every hour on a card by Friday. That one's mine."),
], "Stated in the client's words with two measures the client set: fewer than five late launches next spring, every one warned a week before, and every hour on a card by the Friday. Our side proposed a stricter wording (00:31:37) and the client corrected it; the client's version is the one recorded.", True, "Say it worked. Say it's next April. What's different, in a sentence?"))
RUB.append(row("R7 Decision process mapped", "met", [
    q("Mine, up to twenty thousand on anything operational. Above that it's Aubrey and the board, which is the family, four of them, and they meet on the fourteenth of October."),
    q("The fourteenth if it's above twenty. Before that if it isn't. But I'd want him to see it regardless, so plan for the fourteenth."),
    q("There's a line called yard systems that's had nothing in it for three years. Aubrey hates anything monthly."),
], "Approver, threshold, the body above it, its date and its temperament are all stated by the client. The chairman was not on the call; the general manager will ask him to the fifth (00:43:10) and expects him not to come.", True, "Who decides? If this goes ahead, whose yes is it?"))
RUB.append(row("R8 Priority and timing", "met", [
    q("The honest answer is the launch season. March. If the boats go in on their dates next spring, we've done it."),
    q("But if you could get the lift-out list, just the list and the slots, in front of John before the twelfth, I'd take that and say thank you."),
    q("Three weeks on Monday. The twelfth."),
    q("Then fine."),
], "The need is the launch season (March); the twelfth of October is a hope for the lift-out list alone. Our side pushed back honestly on three weeks and the marina manager accepted a rule: if it is not ready and quiet by the fifth, it waits until December and the launch side comes first (00:34:29, 00:34:41). 'John' at 00:33:33 is the marina manager, resolved from the hoist slots being his and from his reply at 00:34:16.", True, "When does it need to be real?"))
RUB.append(row("R9 Blockers surfaced", "met", [
    q("The engineers. If it needs typing, they won't. Not won't. Can't. Phone in a drawer, gloves on, forty foot up a ladder."),
    q("The signal. Wi-Fi doesn't reach the hardstanding."),
    q("It has to be learnable in a morning by someone who won't be here in six months."),
    q("The berthing system stays."),
    q("Maxine is the only person who knows the book, and if she thinks this is replacing her she'll dig in, and she'd be right to."),
    q("The family don't like subscriptions."),
], "Six blockers from three client speakers, each with an answer or a route: no engineer logins and a printed sheet (00:36:51); nothing writes to the berthing system (00:36:02); the office administrator's conversation is the client's to have (00:36:27); the subscription question is for the fourteenth (00:32:59). The outside IT company is a dependency for any login.", True, "What stops this? Not the money. The things you already know will get in the way."))
RUB.append(row("R10 Next step committed", "met", [
    q("Monday the fifth. Morning. Half nine, before the yard gets loud. Here, not on a screen, if you can manage it."),
    q("Bernie, John, John, all of you. And I'll ask Aubrey. He won't come but I'll ask, and then he can't say he wasn't asked."),
    q("I'll send an invite today for half nine on the fifth, with a note of what we've agreed and the questions I've got for Maxine when she's back on the twenty-eighth."),
], "Day, time, place (the yard office, in person), attendees and the invite are all fixed. The third quote is our own utterance, cited because the invite is by nature ours to send; the commitment rests on the client's first two lines. 'John, John' names both managers; neither is a third person.", True, "Dates, then. I'd like to show you a first cut in about ten days. Monday the fifth?"))
RUB.append(row("R11 Solution confirmed", "missing", [], "Discovery call; nothing has been shown. Expected at this stage and not a defect. Blocks only the v1.0 sign-off gate.", False))
RUB.append(row("R12 Scope agreed verbally", "partial", [
    q("That's it. That's the first go. Not the owners typing in, though."),
    q("You can say I've agreed to look at it. I haven't agreed to buy it, and Aubrey hasn't seen it, so don't write agreed anywhere he'll read it."),
], "A first cut is agreed to be shown, with five corrections from the room, and the general manager draws the line himself: agreed to look, not to buy, and the chairman has not seen it. Write 'first cut, agreed to be shown' (00:41:52) and nothing stronger in anything the chairman reads.", True, "So can I say we've agreed a first cut. The lift-out list with slots and the tide, and the job card with hours and the launch date. Shown to you, not sold to you."))
# P1
RUB.append(row("P1 Stated", "met", [q("Forty-one boats sat on the hardstanding with an owner stood next to them, on the day they'd booked, with the antifoul not done or the anodes not on or, in two cases, the engine in bits on the floor of the workshop.")], "Boats miss their launch date because the card and the book disagree, in the general manager's own words.", True, "Tell me about April."))
RUB.append(row("P1 Concrete", "met", [q("Because the job card was in the wrong pile, or in a van, or in one case, in the skip."), q("And a man in a deckchair next to his boat with a flask, from eight in the morning, because he'd driven three hours and he'd been told, by Maxine, in good faith, that it was done.")], "A specific Saturday (the eighteenth of April), nineteen booked and six ready, one named boat's card in the skip, one owner in a deckchair until four.", True, "Forty-one."))
RUB.append(row("P1 Workaround", "met", [q("Forty boats, an hour and a half, every morning for eight weeks. And I still missed forty-one, because ready isn't a thing you can see."), q("Bernie's wall doesn't have dates on it. It has boats on it.")], "The workaround is the general manager's seven o'clock walk; why it fails is stated: readiness is not visible and the wall carries no dates.", True, "Tighe, you said earlier you walk the yard too. Is that the same walk?"))
RUB.append(row("P1 Reach", "met", [q("Two owners rang Aubrey. Not me, Aubrey."), q("is not in a mood to pay an invoice in June for work he can't remember.")], "Reaches the owners, the chairman, the finance manager's invoices and the yard; volunteered, not asked.", False))
RUB.append(row("P1 Cost inputs", "met", [q("And twenty-three re-lifts we didn't charge for, which is a hundred and eighty each, so four thousand one hundred and forty."), q("Forty-six thousand two hundred a year of berthing. Eleven at four thousand two hundred.")], "Credits, uncharged re-lifts and the lost berths are all figured by the finance manager; the berth loss is set aside from the bleed by the client's own choice.", True, "And the eleven berths? The forty-six thousand?"))
RUB.append(row("P1 Trajectory", "met", [q("Which is sixty more boats coming out next autumn and sixty more going back in the spring after."), q("But it's not a one-off, it's a curve, and the curve's going the wrong way.")], "Sixty more boats from March and a worsening credit curve.", True, "And the pontoon?"))
# P2
RUB.append(row("P2 Stated", "met", [q("Don't get billed. John can only invoice what's on the card.")], "Hours that never reach the card are never invoiced; 'John' here is the finance manager, confirmed by his restatement at 00:13:53.", True, "And the hours that don't get written down?"))
RUB.append(row("P2 Concrete", "met", [q("The Kittiwake. The one in the skip. I know it was twenty-six because Lorcan and I did most of it ourselves.")], "One named job: fourteen hours on the card, twenty-six worked.", True, "Was there a job where it was twenty-six?"))
RUB.append(row("P2 Workaround", "met", [q("and on the Friday I go round with a pen and ask everyone what they did all week. And they tell me, roughly.")], "The Friday round with a pen, and why it fails: roughly.", True, "And in practice?"))
RUB.append(row("P2 Reach", "met", [q("Which, in April, was six to eight weeks after the boat went back in the water, because the cards come up in a heap when Bernie clears her wall, not when the job's done.")], "Reaches invoicing timing and the owner's willingness to pay; volunteered.", False))
RUB.append(row("P2 Cost inputs", "met-with-residual", [q("I'd say three, four hours a week, each engineer, that never make it onto a card."), q("We charge fifty-eight an hour.")], "Hours per engineer, headcount, charge rate and weeks are all client-supplied; the residual is the hedge (three to four), resolved by the client's own choice of three. A run that uses four, or averages, is wrong.", True, "Bernie, the hours. Three or four a week per engineer."))
RUB.append(row("P2 Trajectory", "partial", [q("It got worse this year, because the two new lads started in March and they don't know yet that I'll come round on the Friday.")], "A direction (worse this year, two new engineers) with no rate; partial.", True, "Has it always been like that, or is it getting worse?"))
# P3
RUB.append(row("P3 Stated", "met", [q("Because I'm the one stood at the hoist at seven in the morning with two boats booked into the same slot and an owner on the phone.")], "The hoist double-booked, in the marina manager's words.", True, "Ashby, same question to you. What made it worth an hour of your morning?"))
RUB.append(row("P3 Concrete", "met", [q("The board said four boats. The book said five, because Maxine had taken a fifth on the Thursday and it hadn't got to the board."), q("That was me. Twice a week. Three, some weeks.")], "One day in the second week of last October, three sources, a boat in the slings for forty minutes; twice a week, three some weeks. The frequency is the marina manager's, claimed at 00:22:16 after our side addressed the wrong John.", True, "Okay. Ashby, the double booking. Tell me about a day it happened."))
RUB.append(row("P3 Workaround", "partial", [q("I ring the office at half six every morning and ask Maxine what came in yesterday. And I walk round the yard with the sheet before the lads start. That's the system. Me, walking."), q("Then there isn't a system.")], "The half-six call and the walk cover the book-versus-board gap and fail when the office administrator is away. What is done about the third source, a relaunch that lives only on the workshop wall, is never stated; partial.", True, "What do you do about it now?"))
RUB.append(row("P3 Reach", "met", [q("and two of our own lifts went to the next day."), q("One-eighty. Same as a visitor lift. We could charge it. We don't, because it's our fault, mostly.")], "Reaches other owners' lifts, the hoist driver, the re-lift fee that is waived; volunteered.", False))
RUB.append(row("P3 Cost inputs", "partial", [q("Don't. I'd be guessing and you'd be quoting me.")], "The re-lift fee is figured under P1; the hoist driver's overtime and the hours a boat hangs in the slings are declined rather than guessed. Partial: one input figured, the rest refused honestly.", True, "And Bernie's own time, the parts written off, Wojtek's overtime?"))
RUB.append(row("P3 Trajectory", "met", [q("Spring's worse, because the launches are all on dates the owner picked back in October, and then the weather has opinions.")], "Volunteered: spring is worse than autumn, and sixty more boats are coming.", False))
# P4
RUB.append(row("P4 Stated", "met", [q("They ring. In April the office phone doesn't stop. Is my boat in, is it done, why isn't it done.")], "Owners chase status by phone because nobody tells them when a boat is ready.", True, "And the owners, generally. While all this is going on, how do they find out?"))
RUB.append(row("P4 Concrete", "partial", [q("Dozens a day. I couldn't tell you. Maxine could.")], "No count and no named occurrence beyond the two-calls afternoon at 00:18:40; 'dozens a day' is not a figure.", True, "How many calls?"))
RUB.append(row("P4 Workaround", "partial", [q("Nobody, formally. If Bernie's happy with it she rings Maxine and Maxine rings the owner."), q("Which they don't believe, so they ring.")], "An answerphone message and an informal chain; why it fails is stated for the message and not for the chain; partial.", True, "And who tells the owner it's ready? When it is ready."))
RUB.append(row("P4 Reach", "met", [q("Twice in one afternoon, once. He thought we'd lost the boat.")], "Reaches the owner, the office and the workshop manager; volunteered.", False))
RUB.append(row("P4 Cost inputs", "not-obtainable", [q("There isn't, and I'm not going to invent one. That's a Maxine number.")], "Asked directly and declined honestly by the finance manager, who names the person who could supply it. Graded not obtainable from this room, with the role named: the office administrator, back on the twenty-eighth. No figure is invented and 'dozens a day' is not multiplied by anything.", True, "Rudge, is there a number on what that costs? Maxine's time on those calls, say?"))
RUB.append(row("P4 Trajectory", "missing", [], "Nothing is said about whether the calls are growing, and nobody asked.", False))
K["rubric"] = RUB

K["pains"] = [
    q("And this April, forty-one of them weren't ready on their date."),
    q("Because the job card was in the wrong pile, or in a van, or in one case, in the skip."),
    q("The date changes and the card doesn't. Or the card changes because Bernie heard about it, and the book doesn't. Either way there's two dates and one of them's wrong."),
    q("It's the walk back to the van, it's the second job they did while they were up the ladder, it's the snag they fixed because it was there."),
    q("If the card says fourteen hours, it's fourteen hours. I've no way of knowing it was twenty-six."),
    q("Three places. And a forty-two-foot boat hanging in the slings for forty minutes while three of us argued about whose was next, with the tide going out under it."),
    q("The book doesn't know about the tide."),
    q("Maxine's answerphone message in April actually says, if you're ringing about your launch date we'll ring you. Which they don't believe, so they ring."),
    q("A lift with no card, no line, and a surveyor tapping his watch."),
    q("We've got the weights for maybe two thirds of the regulars. In Maxine's head, mostly. Some on the sheet."),
]
themes = ["P1 Boats miss their launch date because the card and the book disagree (excavated)", "P1 The card itself goes missing", "P1 Two dates, one wrong: the launches tab and the card", "P2 Workshop hours never reach the card (excavated)", "P2 The invoice can only be what the card says", "P3 The hoist double-booked from three sources", "P3 The book does not know the tide window", "P4 Owners chase status by phone; nobody tells them", "Visitor lifts arrive with no card and no line (folded into P3)", "Boat weights live in one head or nowhere (not graded; a data question)"]
for p, th in zip(K["pains"], themes):
    p["theme"] = th

K["numbers"] = OrderedDict([
    ("bleed", OrderedDict([("value", "Ninety-six and a half thousand pounds a year, client-built and confirmed by the approver. Unbilled workshop hours: 3 h/wk x 9 engineers x 46 weeks x 58 charge rate = 72,036 ('seventy-two thousand and some'). Office retyping: 12 h/wk x 19 loaded x 48 = 10,944 ('eleven thousand, near enough', the finance manager's own estimate, called soft). Credits plus uncharged re-lifts: 9,412 + 23 x 180 = 13,552 ('thirteen and a half thousand'). The arithmetic gives 96,532; keep the client's own rounding. Met-with-residual: the hours are hedged three to four with three chosen by the client, and the office line is an estimate for an absent colleague; both carried as one gap question. Set aside by the client and kept beside the number: the eleven lost berths at 46,200 a year, the workshop manager's time, parts written off, the hoist driver's overtime."), ("quote", qo("Seventy-two, plus eleven, plus thirteen and a half. Ninety-six and a half thousand. A year.")), ("status", "met-with-residual")])),
    ("upside", OrderedDict([("value", "Two hundred and fifty-two thousand a year in berthing from the sixty C pontoon berths (60 x 4,200), plus a lift, a launch and a workshop job per boat, unvalued. The general manager declines to say what share depends on this work ('All of it if April happens again. None of it if it doesn't.'), so it is recorded as the pontoon's figure with a dependency on this project, never added to the bleed and never claimed as this project's upside. Partial."), ("quote", qo("Sixty at four thousand two hundred is two hundred and fifty-two thousand a year in berthing")), ("status", "partial")])),
])

V = lambda t, m, o: OrderedDict([("their_term", t), ("meaning", m), ("likely_monday_object", o)])
K["vocabulary"] = [
    V("owner", "The boat's owner, the customer; never the business owners, who are 'the family' or 'the board'", "a person field or a text field on the lift and on the job card; no Contacts board in v1"),
    V("the family / the board", "The Threlfalls, four of them, who own the marina and meet monthly; the chairman is Aubrey", "not a monday object; the approver above twenty thousand in the record"),
    V("lift / lift-out", "Taking a boat out of the water on the hoist; about three hundred and forty each autumn", "item on the lift-out list, with a date, a slot and a cradle"),
    V("launch / relaunch", "Putting a boat back in; the spring season, March to April, on a date the owner booked when it came out", "a launch date on the job card, red inside a fortnight; a launches view of the same list"),
    V("the hoist", "The fifty-tonne travel lift at the hoist dock, driven by one person; the dock dries out", "the resource the slot belongs to; no separate board"),
    V("the slot / the window", "A hoist slot inside the tidal window, two hours either side of high water; two to six per day", "a slot with a date, a time and the tide window on the lift"),
    V("the book", "The office administrator's lift-out and launches spreadsheet; twenty years old; nobody else touches it", "replaced by the lift-out list; never 'book of record', which is the berthing system"),
    V("the board", "Two meanings: the hoist whiteboard in the yard office (00:21:08) and the family board (00:32:11)", "the first becomes the daily view and the printed sheet; the second is not an object"),
    V("job card", "The triplicate paper card for the work on a boat while it is out; hours and parts written on it", "item on the job card list, linked to the lift; hours, parts as fields, launch date, insurance yes/no, lift record"),
    V("the wall", "The workshop manager's whiteboard with a hook per boat, where cards hang", "a view of the job cards by engineer; not a separate board"),
    V("the sheet", "The printed daily sheet the yard crew work from, off the hoist board", "a printable view of the lift-out list: boat, length, weight, berth, cradle tag, owner phone, who drove"),
    V("cradle", "The steel stand a boat sits on ashore; each has a numbered tag", "a field on the lift; the tag number is data, not a person"),
    V("berth holder", "An owner with an annual berth contract in the berthing system", "stays in the berthing system; a read-only list later, at most"),
    V("visitor lift", "A same-day lift for a boat from elsewhere, usually for a survey; no card, often no line", "a lift on the list with no job card; flagged as visitor"),
    V("re-lift", "Lifting a boat a second time because it went in unready; one-eighty, not charged", "a count on the record, not a fee in the tool"),
]
K["entities_and_workflows"] = [
    "Lift-out booking: the owner rings (or emails, or catches the marina manager on the pontoon); the office administrator puts a line in the book's lift-out tab with boat, owner, length, date and the work wanted",
    "Hoist scheduling: each Friday the marina manager prints the next week from the book onto the hoist whiteboard, one column a day, and fits the boats into the tidal window (two hours either side of high water, two to six boats a day depending on the tide)",
    "The daily sheet: printed off the whiteboard each morning for the yard crew, with boat, length, weight, berth, cradle tag number, owner's phone and a box for who drove",
    "The lift: the hoist driver lifts, the yard foreman and crew chock and tie the boat into a numbered cradle on the hardstanding",
    "Job card: written in triplicate off the book by the office administrator; top copy to the workshop wall, second to the office, third cable-tied to the boat",
    "Workshop assignment: the workshop manager hangs the card on a hook and gives it to an engineer by proximity and skill (two engine specialists; GRP and antifoul to whoever has a roller)",
    "Hours and parts: written on the card by the engineer, or reconstructed roughly on Friday; the workshop manager signs, the general manager signs anything over five hundred in parts",
    "Invoicing: the signed card goes upstairs; the finance manager types it into the accounts package; in April six to eight weeks after launch",
    "Launch booking: the launch date is taken when the boat comes out and written in the launches tab; changes arrive by phone in February and reach the book or the card but rarely both",
    "Owner notification: nobody formally; the workshop manager rings the office or the owner; the owner usually rings first",
    "Visitor lifts: twenty to thirty a year, same day, for surveys; no card, often no line in the book; they collide with booked slots",
    "Insurance and lift records: the owner's insurance certificate is meant to be on file before a lift and a lift record (who drove, weight, date) after; both on the card, sometimes; inspected by the insurer in January; berthing itself stays in its own system, untouched",
]
K["integrations_mentioned"] = [
    "The berthing system (contracts, direct debits, berth allocation, waiting list): stays, is never written to; a read-only berth holder list is a possible later read (00:36:02), a question and not a design; the vendor's yard module is an alternative in play, not an integration",
    "The accounts package: the finance manager invoices from signed cards; nothing writes to it; whether hours could be exported to it is not discussed and not proposed",
    "Email and phone: how bookings and owner calls arrive; the office keys them; no email-to-item intake in the first go because owners do not type",
    "The tide tables: the source of the daily window; how the window reaches the slot (typed by the marina manager, or otherwise) is a pre-build question",
    "The chairman's other business uses an unnamed tool with coloured boards for a rota; whether it is monday is unknown and must be asked, because it decides which account the build goes in",
]
K["compliance_or_security_signals"] = [
    "Owner personal data: the insurance certificate carries the owner's address and the finance manager will not have it on a screen in the yard; the record holds a yes/no and a date, never the document (00:41:11)",
    "Owner phone numbers are already on the printed sheet in the yard; whether they stay there is a question for the fifth, not an assumption",
    "The insurer requires an insurance certificate on file before a lift and a lift record (who drove, weight, date) after; the January inspection 'was a conversation' last year (00:40:27)",
    "Direct debits and contracts live in the berthing system and nothing else touches them",
    "Boat names identify owners; the Kittiwake and the deckchair owner are customer stories and stay internal",
]
O = lambda quote, typ: OrderedDict([("quote", qo(quote)), ("type", typ)])
K["objections"] = [
    O("They can rebuild a gearbox in the rain but they will not write down that they did it.", "Team won't adopt it (the engineers will not write; raised)"),
    O("The engineers. If it needs typing, they won't. Not won't. Can't. Phone in a drawer, gloves on, forty foot up a ladder.", "Team won't adopt it (raised as a blocker; answered on the call with no engineer logins and a printed sheet)"),
    O("I tried one of those task apps two summers ago. Free trial. It was me and Lorcan for a month, and then it was me, and then it was nobody.", "Team won't adopt it (a free task app tried and abandoned; raised)"),
    O("I haven't agreed to buy it, and Aubrey hasn't seen it, so don't write agreed anywhere he'll read it.", "Must check with someone (the chairman and the family board were not on the call; raised)"),
    O("We're three weeks from the busiest eight weeks of the year. I'm not learning a new thing on the twelfth of October with a boat in the slings.", "Wrong time, next quarter (the lift-out season starts in three weeks; raised, answered on the call with the December rule, accepted)"),
    O("And I could build the lift list in a spreadsheet with the tide in it in a weekend. Honestly. Why don't I?", "We'll build it ourselves (raised; answered by the general manager, not by our side)"),
    O("The berthing system people have a yard module. They pitched it in June.", "Talking to other partners (the berthing system vendor's yard module at three thousand six hundred a year; raised; our side declined to judge it unseen)"),
    O("And isn't this just another place to type things? Genuine question. Not a dig.", "monday itself is the problem (another place to type; raised, answered on the call)"),
    O("What does something like this cost? Roughly. So I can warn Aubrey before the fourteenth.", "Just send a proposal or pricing (raised; deferred with a sequence and a date, no figure)"),
    O("Aubrey hates anything monthly. He'll ask why it isn't a one-off, and you should have an answer.", "Price feels high (anticipated from the chairman, who dislikes subscriptions)"),
    O("The signal. Wi-Fi doesn't reach the hardstanding.", "Outside the map: no signal on the hardstanding (raised; answered by the printed sheet and no yard logins)"),
    O("Half the yard's seasonal, they come in April and they're gone in October, so whoever learns it in the spring isn't here in the autumn.", "Outside the map: seasonal crew turnover (raised; a design constraint, learnable in a morning)"),
]
CM = lambda quote, what, owner, date: OrderedDict([("quote", qo(quote)), ("what", what), ("owner", owner), ("date", date)])
K["commitments_and_next_steps"] = [
    CM("Monday the fifth. Morning. Half nine, before the yard gets loud. Here, not on a screen, if you can manage it.", "Walkthrough of a first cut (the lift-out list with slots and the tide window; the job card with hours and launch date) in person at the yard office on the big screen; general manager, marina manager, finance manager and workshop manager attend; the chairman invited by the general manager and expected not to come", "Consultant (hosts); Tadhg Devlin, Jon Ashby, John Rudge and Bernie Locke attend", "2026-10-05 09:30 local (Monday the fifth; month and year inferred from 'three weeks on Monday, the twelfth' and the fourteenth of October)"),
    CM("I'll send an invite today for half nine on the fifth, with a note of what we've agreed and the questions I've got for Maxine when she's back on the twenty-eighth.", "Invite plus a note of the first cut as 'agreed to be shown' and the list of questions for the office administrator", "Consultant", "the day of the call (unstated; week of 21 September 2026)"),
    CM("And I'll ask Aubrey. He won't come but I'll ask, and then he can't say he wasn't asked.", "Ask the chairman to the fifth", "Tadhg Devlin", "before 2026-10-05"),
    CM("Done. He'll hate it before and like it after. That's Lorcan.", "Walk the yard foreman through the first cut before the fifth, not after", "Tadhg Devlin", "before 2026-10-05"),
    CM("I'll put a proper figure in front of you before the fourteenth, in writing, with what it covers.", "A written figure with its coverage after the walkthrough and before the family board; a deferred answer with a date, entered in the deferred-answer register and held until R12 is met; pricing itself is outside v1", "Consultant", "before 2026-10-14"),
    CM("Fair. I'd rather have nothing than a guess. It goes on the list for the twenty-eighth.", "Questions for the office administrator on her return: how bookings are keyed, the colours in the book, the launches tab, the boat weights, her share of April on the phone", "Consultant drafts; Tadhg Devlin asks", "2026-09-28 (Monday the twenty-eighth)"),
]
K["traps"] = [
    "The header's 'Participants (5)' line lists Maxine Bassett; she is on leave and never speaks. The forty-six turns under that label are Bernie Locke's (00:00:52, 00:01:11). Do not list Maxine as an attendee, do not invent Bernie as an unlisted sixth person, and do not treat the header as an observed roster.",
    "'Tige Devon' (00:04:01) is our own read-back rendered wrong and corrected in the next turn; it is not a second surname and not a person. 'Devlin's rule' (00:09:48, 00:34:45) is the general manager's rule, evidence of his authority, not a separate person named Devlin.",
    "'Write Tige' (00:43:53) is the export's rendering of the general manager saying his own name. Client-facing text spells him as the label and the invite do, Tadhg Devlin, never as any rendering; and spells the workshop manager as Bernie Locke, never as the label.",
    "Thady (00:24:01, 00:43:32, 00:43:41) is a family nickname that matches nothing by string; it binds only by the answered adjacency pair at 00:24:01 to 00:24:04, and 00:43:41 is corroboration, not the method. Never a second person.",
    "tag (00:05:49), tie (00:11:11) and tide (00:15:03) are vocatives, each answered by the general manager in the next turn; the other sixteen uses of the same three words (a tag on the cradle, tie it into the cradle, tie up a dinghy, the tide thirteen times) are ordinary words and stay ordinary. Coerce three, log three, leave sixteen.",
    "Every spoken 'John' is the export's rendering of two different names. An exact string match to the label 'John Rudge' is wrong for ten of twenty-one occurrences and unsafe for one more; resolve each by adjacency pair or content, as the intake block lists.",
    "At 00:22:03 our side addressed 'John' with a fact that was the marina manager's; the finance manager's 'Not me' (00:22:08) is a disclaimer, not an answer, and 'That was me' (00:22:16) claims it. The twice-a-week figure stays with Jon Ashby; the error is a delivery note, not a re-attribution.",
    "'Tyge's list is getting long, as John will tell you' (00:26:00) is genuinely ambiguous between the two managers, with no adjacency pair either way. Leave it unbound, say so, and let nothing rest on it. A run that binds it to the exact-match label fails.",
    "Biscuit (00:00:23, 00:13:20) is a dog. Not a person, not a mentioned stakeholder, not name-shaped noise worth an open question.",
    "'Owner' is the boat's owner, the customer (00:07:01). 'The family' and 'the board' at 00:32:11 are the four Threlfalls; the chairman is Aubrey and is never 'the owner'. 'The board' at 00:21:08 is the hoist whiteboard: two meanings, one word.",
    "'The book' is the office administrator's spreadsheet, not the accounts and not a book of record. The book of record for berths is the berthing system (00:19:17), which is never written to.",
    "The chairman's ultimatum (00:06:29) is relayed by the general manager with 'and I'm quoting'; record it as his account, never as the chairman's statement, and let the why-now stand on the April facts and the pontoon without it.",
    "The eleven lost berths (46,200 a year) are set aside by the finance manager (00:29:28); keep them beside the bleed and never in it, and never annualise a loss the client hopes is not annual.",
    "The bleed's hours are hedged three to four and the client chose three (00:27:53); use three, do not use four, do not average, and carry the hedge as the residual. The office line is the finance manager's own estimate for an absent colleague and is called soft; it stays in the number with its softness recorded.",
    "The credits (9,412, cash) and the re-lifts (4,140, revenue not charged) are summed by the client and rounded to thirteen and a half; write the client's rounding and the arithmetic beside it. The finance manager chose this year's figure over last year's half (00:27:41); do not build a range he did not ask for.",
    "The pontoon's 252,000 (00:30:05) is not this project's upside; the general manager refuses to split it (00:30:40). R5 is partial, the figure is recorded as a dependency, and it is never added to the bleed.",
    "The vendor's yard module at three thousand six hundred a year (00:37:02) is an alternative in play relayed by the client; our side declined to judge it unseen (00:37:30). Do not evaluate it, do not net its price against anything, and record it as an alternative with an open question about who is looking at it.",
    "'Nothing new in a lift-out week' (00:34:45) is a client rule: the lift-out list ships for the twelfth only if it is ready and quiet by the fifth, otherwise it waits until December and the launch side comes first (00:34:29). Sequence the build to that rule rather than to the twelfth.",
    "R8: March is the need, the twelfth is a hope (00:33:33). Do not plan the whole build for October, and do not let the hope become a commitment in the note.",
    "R10 is in person at the yard office (00:42:46), not a video call; the invite goes to the finance manager to forward (00:43:32). Write the place as the client stated it.",
    "R12 is partial in the client's own words (00:41:40): write 'first cut, agreed to be shown' (00:41:52) and put 'agreed' in nothing the chairman reads.",
    "The pricing request (00:42:00) was refused with a reason and a sequence (00:42:06); produce no figure and no proposal. The gate is closed on R12 in any case, and pricing is outside v1; the promise of a figure before the fourteenth is a deferred answer with a date, held until scope is agreed.",
    "The insurance certificate carries the owner's address (00:41:11): the card holds a yes/no and a date, never the document, and nothing puts an address on a yard screen.",
    "Parts ordering is out of the first cut by the workshop manager's own request (00:40:06); parts remain as fields on the card. The shop is out (00:19:47). Visitor lifts are in, as lifts with no card and no line (00:20:01).",
    "The yard crew get no logins in the first go (00:36:51); the office types and the sheet prints (00:39:46). Do not design a mobile engineer app for people with gloves on and no signal.",
    "Owners do not type in the first go (00:39:24); no owner portal, no request form in v1. Owner notification is the third piece, later.",
    "There is no monday account (00:33:05). The chairman's other business uses an unnamed board tool; do not assume it is monday, ask (00:33:21), because the answer decides which account the build goes in.",
    "The workshop manager's brief absence (00:26:07) is a presence change inferable only from speech; nothing said in her absence is hers, and the gap is not measurable without end times.",
]
RC = lambda typ, desc, quote: OrderedDict([("type", typ), ("description", desc), ("quote", qo(quote))])
K["requested_changes"] = [
    RC("add", "Pre-build requirement (no build exists yet): whatever it is, it prints; the yard crew read paper.", "And it prints. Whatever it is, it prints, because the lads read paper and they will read paper until they retire."),
    RC("add", "Pre-build requirement: the launch date on every job card, red inside a fortnight.", "And the launch date on every card. In red if it's inside a fortnight. That's the one thing I'd have wanted in April."),
    RC("add", "Pre-build requirement: the card carries whether the owner's insurance certificate is on file (yes/no and a date, never the document) and the lift record (who drove, weight, date).", "Not the certificate itself. Whether we've got it. The certificate has the owner's address on it and I'm not having that on a screen in the yard."),
    RC("change", "Our play-back had owners eventually entering requests; the client removes owners from typing in the first go. The office types.", "Not the owners typing in, though. I know that's where these things go. Not in the first go. The office types it."),
    RC("change", "The hoist slot must carry the tide window, not just a date.", "And the tide window on the slot. If it doesn't know about the tide, it's the book again with a nicer font."),
    RC("remove", "Parts ordering, mentioned in our play-back as staying with the suppliers, is taken out of the first cut altogether at the workshop manager's request; parts stay as fields on the card.", "And leave parts out. I'll do parts my way until you've seen how bad my way is, and then we'll talk."),
]
K["should_plugin_propose_a_build"] = True
K["expected_questions_before_building"] = [
    "Which monday account does this go in, who administers it, and which products and seats are being bought? The chairman's other business uses an unnamed board tool (00:33:05): is it monday, and if so is this the same account or a new one?",
    "For the office administrator on the twenty-eighth: how a booking is keyed today, what the colours in the book mean, how the launches tab is kept, where the boat weights live, and her share of April on the phone (P4 cost input).",
    "The slot model: how many slots per day inside the window (two to six), who enters the tidal window each day and from what, and whether a slot is a time or a position in the window.",
    "Who types: the office administrator and her number two, the general manager, the marina manager, the workshop manager; confirm five seats and no engineer or yard-crew logins in the first go.",
    "The printed sheet: confirm its fields (boat, length, weight, berth, cradle tag, owner phone, who drove) and whether the owner's phone number stays on a sheet that lives in the yard.",
    "The job card fields: hours by engineer, parts as text or lines, the launch date, insurance on file yes/no with a date, the lift record; and whether the nine engineers appear as names on a card without being users.",
    "Visitor lifts: how one enters the list when it was arranged on the pontoon, and what marks it as a lift with no card.",
    "The berth holder list: is a read-only export from the berthing system wanted later, in what form, from whom, how often; confirm nothing writes back.",
    "The vendor's yard module (00:37:02): is anyone evaluating it in parallel before the fifth, and does the lift list need to be shaped so it could be replaced by it without touching the job cards?",
    "Owner notification (the third piece, later): by whom and how, given owners do not type and one writes letters; nothing is built for it in the first cut.",
]
K["expected_verdict"] = OrderedDict([
    ("verdict", "Discovery complete"),
    ("gates_met", [
        "Solution blueprint (R1 Met-with-residual, R2 Met with two excavated pains)",
        "Build (no extra method gate; still needs the user's approval at the approval stop and the change check; nothing tier-dependent until an account exists)",
        "First demo (v0.1): nothing extra needed; the walkthrough on the fifth is in person at the yard office and the lift-out list goes first",
    ]),
    ("gates_not_met", [
        "Pricing or proposal prep (R4 Met-with-residual and R7 Met, but R12 Partial: agreed to be shown, not to buy, and the chairman has not seen it)",
        "v1.0 sign-off (R11 Missing because nothing has been shown; R5 Partial)",
    ]),
    ("note", "R2, R3, R6, R7, R8, R9 and R10 are Met and R1 and R4 are Met-with-residual from client-side quotes, so the verdict is Discovery complete with the residuals carried as gap questions. Gap questions for the fifth (at most five): the office administrator's answers on the twenty-eighth (R1 residual, P4 cost), the hedge on hours (R4 residual), the vendor module's status, the slot model, and the printed sheet's fields. Propose the blueprint and a v0.1 build once the pre-build questions are answered or listed as assumptions, sequenced to the client's lift-out-week rule. The intake block is graded separately by the intake grader; the 25-field grader ignores it."),
])
K["account_context"] = OrderedDict([
    ("tier", "unknown"),
    ("products_enabled", [
        "none: there is no monday account ('No. Nothing.')",
        "Work Management is the product to be provisioned, not found; the tier is never stated",
        "The chairman's other business uses an unnamed tool with coloured boards for a rota; whether it is monday, and whether this build would share its account, is unknown and is a question before anything is bought",
    ]),
    ("existing_monday_setup", "None. The general manager has seen the chairman's rota tool on a phone and cannot name it; the workshop manager tried a free task app two summers ago with the yard foreman and it died within a month, which is a design constraint (learnable in a morning, nothing to type in the yard) and not an existing setup. No boards, users, automations or data to audit, extend or migrate. The plugin should ask which account the build goes into, who administers it and which products and seats are being bought before designing anything that depends on the answer."),
    ("evidence_quote_or_null", qo("No. Nothing. Aubrey's other business, the holiday park, uses something with coloured boards for the housekeeping rota, I've seen it on his phone, I couldn't tell you what it is.")),
])
K["expected_structures"] = OrderedDict([
    ("native_boards_required", []),
    ("portfolio_expected", False),
    ("portfolio_reason", "There is no account and the tier is never stated, so the Enterprise default cannot fire and nothing tier-dependent is built. Work Management is the whole scope: a lift-out list and a job card list, connected, with a printable daily view and a wall view by engineer. Three hundred and forty lifts a year is volume, not a portfolio. If the account turns out to be Enterprise the portfolio question is reopened and the reason recorded either way."),
    ("lookalike_traps", [
        "A 'Berths' or 'Berth holders' board that carries contracts or direct debits, which is the second berthing system the finance manager will stop.",
        "An 'Owners' board on the native CRM Contacts or Accounts boards, or a pipeline of bookings on Deals, when no selling and no pipeline pain exists; CRM is not part of this build.",
        "Treating owner requests as Service tickets with an owner portal, when owners do not type in the first go and Service extras are out of v1.",
        "A 'Parts orders' board that orders from suppliers, when parts ordering was taken out by name and parts are fields on the card.",
        "Rebuilding the book tab for tab, or the hoist whiteboard as a grid of days, so the slot still does not know the tide.",
        "An engineer app with a login per engineer and time entry in the yard, which repeats the task app that died and ignores the gloves, the drawer and the signal.",
        "A 'Shop' or chandlery board in the first version, when the shop was put out by name.",
    ]),
    ("notes", "One product, one rule. Work Management carries the lift-out list (boat, owner, length, weight, berth, cradle tag, the slot with its tide window, visitor flag, lift record) with a printable daily view, and the job card list (linked to the lift; hours by engineer, parts as fields, the launch date red inside a fortnight, insurance on file yes/no and date) with a wall view by engineer and a Monday view of launches inside a fortnight; it is built structure, not governed by the native-board rule, and no CRM or Service entity is in scope, so native_boards_required is empty by design. Constraints that survive into any shape. Nothing writes to the berthing system. Nothing writes to the accounts package. No engineer or yard-crew logins; the sheet prints; owners do not type; the shop and parts ordering are out; learnable in a morning; the office administrator runs it when she is back."),
])
K["accepted_behaviours"] = [
    "Naming the product as 'Work Management' or 'core', as long as neither CRM, Service nor Dev is added to the build.",
    "Any structure that carries lifts with tide-windowed slots and job cards with hours and a launch date: two connected boards, one board with two groups, or a board with views, as long as the daily sheet prints and the workshop wall becomes a view.",
    "Recording the alias table label-first or canonical-first, as long as the thirteen forms bind to one person, each entry names its method, and every state is 'proposed' until the user confirms.",
    "Locating Bernie Locke's turns under the label 'Maxine Bassett' exactly as printed, with or without an appended gloss such as '(Bernie Locke)', as long as the attendees field and the alias table carry the resolution.",
    "Resolving 00:26:00 as ambiguous, or as probable-either with no binding, but never as bound to either manager.",
    "Grading R1 met-with-residual, or met with the office steps named as second-hand in the note and carried as questions; not partial.",
    "Writing the bleed as the client's own words (ninety-six and a half thousand) or as 96,532 from the client's own components, either way naming the residual.",
    "Recording the pontoon figure under upside with status partial and a dependency, in either order of words.",
    "Logging our side's 00:22:03 error as a delivery defect or as an observation, as long as the twice-a-week fact stays with Jon Ashby and no re-attribution happens.",
    "Listing Biscuit nowhere, or once in an audit note as a non-person token; never in a roster or an open question.",
    "Calling the ordinary-word repair 'coerced', 'bound' or 'promoted', as long as each of the three carries its vocative-slot licence and the sixteen ordinary uses are untouched.",
    "Treating the farewell 'Teague' (00:44:39) as an unanswered vocative bound by the already-confirmed alias, or as unbound corroboration; neither adds a person.",
    "Writing the next step as 09:30 on Monday 5 October 2026 with the year inferred, or as 'Monday the fifth, half nine, the yard office' with the month inferred from the twelfth and the fourteenth.",
]
K["expected_leak_blocklist"] = [
    "Bleed total in every form: 96,532, 96532, 96,520, 96.5k, 'ninety-six and a half thousand', 'ninety-six and a half', 'ninety-six thousand', 'ninety-six five'.",
    "Bleed components and inputs: 72,036, 'seventy-two thousand', 1,566, 'twenty-seven hours a week', 10,944, 'eleven thousand', 13,552, 'thirteen and a half thousand', 'three or four hours a week' as a loss.",
    "Rates: 58 or 'fifty-eight an hour' (the workshop charge rate), 19 or 'nineteen an hour loaded'.",
    "Credits and re-lifts: 9,412, 'nine thousand four hundred and twelve', 'nine and a half thousand in goodwill credits', 4,140, 'twenty-three re-lifts', 'last year was maybe half that'. CAUTION: 'one-eighty' is also the published visitor lift fee and may survive as a price in an SOP; the waiver and the count do not.",
    "The lost berths: 'eleven owners didn't renew', 'eleven annual berths', 46,200, 'forty-six thousand two hundred', 'walked across the water', 'the place opposite'. CAUTION: 4,200 is the annual berth fee and is a published price; the eleven and their total are the confidential part.",
    "The upside and its dependency: 252,000, 'two hundred and fifty-two thousand', 'All of it if April happens again'.",
    "Decision process detail and the chairman's words: 'up to twenty thousand', 20,000, 'the fourteenth of October' as an approval date, 'yard systems' budget line, 'Aubrey hates anything monthly', 'He won't come but I'll ask', 'I'm not paying for a pontoon so you can lose the boats off it', 'counted the boats himself, on a Sunday, with a clipboard'.",
    "Alternatives in play: the vendor's 'yard module', 3,600 or 'three thousand six hundred a year', 'build the lift list in a weekend', the abandoned free trial.",
    "Objection text: 'another place to type things', 'not learning a new thing on the twelfth', 'hands like shovels', 'phones live in a drawer', 'look at their boots'.",
    "Remarks about colleagues: 'twenty years of Maxine in it', 'she'll dig in', 'Thady's inbox is a disgrace', 'He'll hate it before and like it after', 'the wet John and the dry John', 'doesn't like the dog', 'She's being polite because you're new'.",
    "The April failure narrative: 'forty-one', 'in the skip', the deckchair and the flask, 'He was there till four', 'forty minutes in the slings', 'the mud in the slings', 'Two owners rang Aubrey'.",
    "Customer PII and stories: the Kittiwake and its owner, the deckchair owner, the letter-writer, 'fourteen hours' versus 'twenty-six', any owner's address or phone number, the insurance certificate's contents.",
    "Identity and transcript artefacts: Tige, Tyge, Teague, Tighe, Devon, Thady, 'Write Tige', 'the label says Maxine', 'Other John', alias tables, coercion logs; client-facing text uses Tadhg Devlin, Bernie Locke, Jon Ashby and John Rudge as the labels and the invite spell them.",
    "Method vocabulary, pain IDs (P1 to P4), R-numbers, gate names, 'excavated', 'met-with-residual', 'not obtainable from this room', 'seed', 'blocklist'.",
    "Flag, do not remove: three hundred and forty lifts, sixty new berths, 'two hours either side of high water', 'two boats on a neap', four to five boats a day, the insurer's fields (who drove, weight, date), 'learnable in a morning', 'it prints'; these are volume and process facts that belong in an SOP.",
]

# ---------------- intake block ----------------
def st(sub):
    return stamp_of(sub)

I = OrderedDict()
I["export_family"] = OrderedDict([
    ("family", "block export"),
    ("dialect", "plain text; one turn per line as '[HH:MM:SS] Label: text'; start-only stamps at one-second resolution; a three-line human-readable export header ending in a 'Participants (5)' line, then a blank line; line endings LF"),
    ("end_times", False),
    ("participant_header", "present and claimed: five labels as the platform saw them, one of them a borrowed laptop"),
    ("label_position", "line prefix, uniform shape; four full-name labels and 'Consultant'; no initials, no device names, no bots"),
    ("units", len(TURNS)), ("words", TOT),
    ("max_unit_words", len(longest[2].split())),
    ("max_unit_seconds", "not measurable (start-only); %d s from 00:38:40 to the next stamp" % (secs("00:39:24") - secs("00:38:40"))),
    ("adjacent_same_label_pairs", same_pairs),
    ("shred_counts", OrderedDict([("lowercase_initial_units", lower), ("units_without_terminal_punctuation", unterm), ("units_at_or_under_four_words", short)])),
    ("timestamp_order", "strictly increasing; 0 collisions, 0 inversions"),
    ("gap_distribution", "start-to-start %d to %d s, proportional to unit length; mode %d s; no gap is measurable as silence without end times" % (min(gaps), max(gaps), Counter(gaps).most_common(1)[0][0])),
    ("markers", OrderedDict([("laughs", markers["laughs"]), ("crosstalk", markers["crosstalk"]), ("inaudible", markers["inaudible"]), ("dog barks", markers["dog barks"])])),
    ("defect_density", "%.1f percent short, %.1f percent lowercase-initial (both are coerced vocatives, not shred), %.1f percent unterminated, 0 collisions, 0 same-label pairs; thresholds derive from this file's own distribution; the file is structurally clean by design so that the identity behaviour is isolated, and a clean structure is not evidence of clean names" % (100.0 * short / len(TURNS), 100.0 * lower / len(TURNS), 100.0 * unterm / len(TURNS))),
])
I["detectors"] = OrderedDict([
    ("composite_splitter", "runs; reports that no unit qualified: the longest unit is 118 words on our side (00:38:40), a play-back with no second-person address to its own label and no interview move inside it; no end times to test a rate against; composite_blocks is empty"),
    ("wedge_flagger", "runs; no end times, so no boundary gap is measurable; reports nothing to flag and says why"),
    ("rule", "both detectors run on every file and only one may fire; here neither does, and the report says so for each"),
])
I["type_header"] = OrderedDict([
    ("label", "discovery"), ("seat", "partner-led"), ("relationship", "new logo"), ("direction_of_show", "nobody shows"), ("output_class", "configured structure"),
    ("room_shape", "small group: four client speakers in four rooms on one site (the yard office, the marina office, the upstairs office, the workshop mezzanine), one of them under a borrowed label; one on our side; one brief absence"),
    ("money_live", "live in the room with the approver absent: a charge rate and a loaded rate from the finance manager (00:27:59, 00:28:33), the twenty-thousand threshold from the general manager (00:32:11, unhedged), the vendor's price relayed (00:37:02), and a cost question (00:42:00) refused by our side with a sequence and no figure (00:42:06); the chairman was not present"),
    ("signals", [
        OrderedDict([("signal", "screen-control deixis"), ("result", "none; our side states no screen"), ("quote", qo("I'm not going to show you anything today."))]),
        OrderedDict([("signal", "same-side screen direction"), ("result", "none (provisional signal, nothing to record)")]),
        OrderedDict([("signal", "agenda sentence and the client's answer"), ("result", "discovery: the agenda sentence at 00:01:56 and the client's acceptance at 00:02:30"), ("quote", qo("Good. That's what I told Aubrey we'd do. Ask away."))]),
        OrderedDict([("signal", "output-class markers"), ("result", "configured structure: one list, a card, a view of the wall, a printed sheet; the one client-side 'module' (00:37:02) is the vendor's product and not a bespoke-code marker"), ("quote", qo("One list. A boat comes out, and everything about it, the jobs, the parts, the launch date, who's on it, is in one place"))]),
        OrderedDict([("signal", "commercial markers"), ("result", "who approves spend and the threshold (00:32:11, unhedged); rates (00:27:59 'we charge', 00:28:33 'I'd say'); the vendor price (00:37:02, relayed); the pricing request (00:42:00) and the refusal (00:42:06)"), ("quote", qo("Mine, up to twenty thousand on anything operational."))]),
    ]),
    ("proposal", "one-line dismissible header with the agenda quote; detection proposes, the user decides; no dimension unresolved, so nothing grades advisory"),
])
I["roster"] = OrderedDict([
    ("header_claimed", LABELS),
    ("observed_labels", LABELS),
    ("turns_by_label", OrderedDict((l, turns_by[l]) for l in LABELS)),
    ("borrowed_labels", [OrderedDict([("label", "Maxine Bassett"), ("what", "the absent office administrator's laptop, used by the workshop manager; stated by the speaker at 00:00:52 and named in full at 00:01:11"), ("resolves_to", "Bernie Locke, Workshop Manager"), ("turns", turns_by["Maxine Bassett"])])]),
    ("speaking_but_unlisted", ["Bernie Locke: every turn under the label 'Maxine Bassett'; absent from the header; introduced in full at 00:01:11 ('Bernie Locke, I run the workshop')"]),
    ("listed_but_silent", ["Maxine Bassett: listed in the header; never speaks; on leave until the twenty-eighth (00:00:52); mentioned thirty-six times"]),
    ("voices_missing", "none against the header once the borrowed label is resolved; the header is claimed, not observed, so whether anyone else sat in the yard office or the marina office is unknown"),
    ("mentioned_not_present", ["Maxine Bassett (office administrator; keeps the book)", "Aubrey Threlfall (chairman; one of the four family board members)", "the other three family board members (unnamed)", "Lorcan (yard foreman)", "Wojtek (hoist driver)", "the office administrator's number two (unnamed)", "the nine engineers, two of them new in March (unnamed)", "the outside IT company", "the berthing system vendor", "the insurer", "a surveyor (August)", "boat owners: the Kittiwake's, the deckchair owner, the letter-writer", "the competitor marina across the water"]),
    ("presence_changes", "the workshop manager leaves the mezzanine briefly and returns ('Sorry, I had to go down for a second.' 00:26:07); the gap is not measurable without end times; nobody else joins or leaves; the three locations plus the mezzanine are stated in speech, not in the header"),
])

F = lambda form, slot, locs, method, state: OrderedDict([("form", form), ("slot", slot), ("locations", locs), ("method", method), ("state", state)])
I["alias_map"] = [
    OrderedDict([("canonical", "Tadhg Devlin"), ("side", "client"), ("label", "Tadhg Devlin"), ("form_count", 13), ("forms", [
        F("Tadhg Devlin", "label and header", ["every turn under the label; header line 3"], "the roster entry itself; never rendered this way in speech", "confirmed by the label"),
        F("Tige", "self-reference (four), vocative (one), subject (two)", ["00:00:23", "00:01:25", "00:03:19", "00:04:10", "00:15:56", "00:29:18", "00:43:53"], "first person under his own label at 00:00:23 ('Tige here'), 00:03:19 and 00:04:10 binds the rendering; the vocative at 00:01:25 is answered at 00:01:33; 00:15:56 and 00:29:18 are colleagues' subject uses matching the bound form; phonetic key and edit distance against 'Tadhg' fail, because the spelling does not encode the sound", "proposed once for the user's confirmation"),
        F("Tige Devlin", "first-person self-introduction and self-correction", ["00:03:19", "00:04:10"], "surname exact match plus first person under the label; the strongest single basis for the whole cluster", "proposed once for the user's confirmation"),
        F("Tige Devon", "our read-back, rendered", ["00:04:01"], "corrected by the labelled speaker at 00:04:10 ('Devlin. Tige Devlin.'); edit distance 2 on the surname; bound by the correction, never a second surname", "proposed; logged as a recognition error"),
        F("Tyge", "vocative (two), self-reference in the third person (one)", ["00:04:17", "00:20:32", "00:26:00"], "adjacency pair: 00:04:17 answered at 00:04:26, 00:20:32 answered at 00:20:42; 00:26:00 is under his own label ('Tyge's list'); phonetic key agrees with Tige", "proposed once for the user's confirmation"),
        F("Teague", "vocative (two)", ["00:06:06", "00:44:39"], "adjacency pair: 00:06:06 answered at 00:06:14; 00:44:39 is a farewell followed by his 00:44:45 and binds by the confirmed cluster; phonetic key agrees with Tige", "proposed once for the user's confirmation"),
        F("Tighe", "vocative (one)", ["00:23:11"], "adjacency pair: answered at 00:23:18; phonetic key agrees with Tige", "proposed once for the user's confirmation"),
        F("Devlin", "possessive (two), surname alone (two)", ["00:04:10", "00:04:17", "00:09:48", "00:34:45"], "surname exact match to the label; 'Devlin's rule' is his rule, not a person", "confirmed by exact match"),
        F("tie", "vocative (one), coerced", ["00:11:11"], "vocative-slot test passed (see vocative_slot_tests); adjacency pair: answered at 00:11:17; coercion logged", "proposed once for the user's confirmation"),
        F("tag", "vocative (one), coerced", ["00:05:49"], "vocative-slot test passed; adjacency pair: answered at 00:05:55; coercion logged", "proposed once for the user's confirmation"),
        F("tide", "vocative (one), coerced", ["00:15:03"], "vocative-slot test passed; adjacency pair: answered at 00:15:16; coercion logged", "proposed once for the user's confirmation"),
        F("Thady", "vocative (one), possessive (one), subject (one)", ["00:24:01", "00:43:32", "00:43:41"], "matches no roster entry by exact match, phonetic key or edit distance; binds only by the adjacency pair 00:24:01 to 00:24:04; 00:43:41 ('Thady's what his mother calls him') and his 00:43:53 are corroboration, not the method; never a person", "proposed once for the user's confirmation"),
        F("the GM / general manager", "role form", ["00:03:19", "00:04:01", "00:15:56"], "self-description at 00:03:19; 00:15:56 states the identity in the same breath ('the GM signs, which is Tige')", "proposed once for the user's confirmation"),
    ])]),
    OrderedDict([("canonical", "Bernie Locke"), ("side", "client"), ("label", "Maxine Bassett (borrowed)"), ("form_count", 4), ("forms", [
        F("Maxine Bassett", "label and header", ["every turn under the label; header line 3"], "the label is the absent administrator's device; the speaker says so at 00:00:52; every turn under it is Bernie Locke's; the label binds to nobody named Maxine", "proposed once for the user's confirmation"),
        F("Bernie", "vocative and subject", ["00:00:52", "00:01:06", "00:01:11", "00:03:19", "00:05:29", "00:11:34", "00:11:57", "00:14:58", "00:15:21", "00:15:48", "00:16:20", "00:18:10", "00:18:28", "00:21:08", "00:24:39", "00:27:47", "00:28:56", "00:29:44", "00:38:40", "00:43:10", "00:44:39"], "first person under the borrowed label at 00:00:52 ('it's Bernie'); vocatives at 00:11:57 and 00:27:47 answered under that label at 00:12:00 and 00:27:53", "proposed once for the user's confirmation"),
        F("Bernie Locke", "self-introduction", ["00:01:11"], "first person under the borrowed label", "proposed once for the user's confirmation"),
        F("Bernadette", "subject", ["00:16:06"], "answered under the borrowed label at 00:16:12 ('Don't.'); a long form of the bound name", "proposed once for the user's confirmation"),
    ])]),
    OrderedDict([("canonical", "Jon Ashby"), ("side", "client"), ("label", "Jon Ashby"), ("form_count", 5), ("forms", [
        F("Jon Ashby", "label and header", ["every turn under the label; header line 3"], "the roster entry; the first name is never rendered 'Jon' in speech", "confirmed by the label"),
        F("John", "subject, vocative and object; ten of twenty-one occurrences resolve here", ["00:00:23 (first)", "00:01:50", "00:03:19 (first)", "00:03:44 ('the wet John')", "00:22:03", "00:33:33", "00:40:53", "00:43:10 (one of two)", "00:44:06 (both)"], "resolved occurrence by occurrence: adjacency pair (00:01:50 follows his 00:01:45; 00:22:03 is claimed at 00:22:16 after the other manager's disclaimer) or content (the marina office, the hoist, the slots, the sheet); phonetic key ties on both labels and decides nothing", "proposed once for the user's confirmation"),
        F("Jonny", "vocative", ["00:22:57"], "adjacency pair: answered at 00:23:03; edit distance 2 from the label's first name", "proposed once for the user's confirmation"),
        F("Ashby", "self-description and vocative", ["00:03:44", "00:04:01", "00:07:12", "00:21:01", "00:22:28", "00:34:45", "00:44:39"], "surname exact match; vocatives answered at 00:07:21, 00:21:08 and 00:22:33", "confirmed by exact match"),
        F("the wet John", "nickname, once", ["00:03:44"], "assigned in the same sentence as 'I'm Rudge'; not reused", "proposed; corroboration only"),
    ])]),
    OrderedDict([("canonical", "John Rudge"), ("side", "client"), ("label", "John Rudge"), ("form_count", 4), ("forms", [
        F("John Rudge", "label and header", ["every turn under the label; header line 3"], "the roster entry", "confirmed by the label"),
        F("John", "subject, vocative and object; ten of twenty-one occurrences resolve here", ["00:00:23 (second)", "00:03:19 (second)", "00:03:44 ('the dry John')", "00:12:00", "00:13:46", "00:15:03", "00:26:26", "00:26:32", "00:27:53", "00:43:10 (one of two)"], "resolved occurrence by occurrence: adjacency pair (00:13:46 restated by him at 00:13:53; 00:26:26 disclaimed by the other manager at 00:26:32 and answered by him at 00:26:38; 00:27:53 answered at 00:27:59) or content (upstairs, invoices, the numbers); the exact string match to this label is not the method and is wrong for the other ten", "proposed once for the user's confirmation"),
        F("Rudge", "self-description and vocative", ["00:03:44", "00:04:01", "00:16:15", "00:25:31", "00:26:17", "00:26:32", "00:38:31", "00:44:39"], "surname exact match; vocatives answered at 00:16:20, 00:25:38 and 00:38:36", "confirmed by exact match"),
        F("the dry John", "nickname, once", ["00:03:44"], "self-assigned; not reused", "proposed; corroboration only"),
    ])]),
    OrderedDict([("canonical", "Maxine Bassett"), ("side", "client, absent"), ("label", "none of her own; her name is a borrowed label"), ("form_count", 2), ("forms", [
        F("Maxine", "subject, possessive and one self-corrected vocative", ["thirty-six occurrences between 00:00:45 and 00:44:22"], "every occurrence is the absent administrator; the vocative at 00:15:48 ('Maxine, sorry, Bernie') is corrected inside the same turn and the answer at 00:15:56 binds to Bernie, so no adjacency pair ever supports a present Maxine", "proposed once for the user's confirmation"),
        F("Maxine's number two", "role phrase", ["00:28:33"], "an unnamed second office person; not a name, not a person created", "not a person"),
    ])]),
    OrderedDict([("canonical", "Aubrey Threlfall"), ("side", "client, absent"), ("label", "none"), ("form_count", 3), ("forms", [
        F("Aubrey", "subject and object, seventeen occurrences", ["00:02:30 to 00:43:10"], "spoken in full at 00:06:29 ('Aubrey, who's the chairman, Aubrey Threlfall'); 'the chairman' and 'him' in the decision passages are the same person", "proposed"),
        F("the family / the board / the Threlfalls", "collective", ["00:02:43", "00:06:29", "00:07:01", "00:32:11", "00:36:36"], "four people including the chairman; the three others are unnamed; not one person", "proposed"),
        F("the owner (refused)", "not a form", ["00:07:01"], "'Nobody calls Aubrey the owner'; owner always means the customer", "not applicable"),
    ])]),
]
I["cross_confusion"] = OrderedDict([
    ("token", "John"),
    ("referents", ["Jon Ashby", "John Rudge"]),
    ("occurrences", 21),
    ("rule", "resolved occurrence by occurrence, adjacency pair first, then content; ten to each manager and one left ambiguous; the two labels stay two people; no occurrence is bound to the label that merely matches the spelling"),
    ("human_confusion_1", "00:22:03 our side addressed 'John' with the marina manager's fact; the finance manager disclaimed it ('Not me.' 00:22:08) and the marina manager claimed it ('That was me.' 00:22:16); our side corrected to the surname at 00:22:28. The vocative binds to Jon Ashby by the claim; the disclaimer is not an answer; recorded as a delivery note, with the figure kept on Jon Ashby"),
    ("human_confusion_2", "00:26:26 the general manager said 'John's got the actual credits number'; the marina manager began to answer, stopped and named the other ('Oh. Other John. Rudge.' 00:26:32); the finance manager supplied the figure at 00:26:38. Binds to John Rudge; 'Other John' is not a third person"),
    ("ambiguous", "00:26:00 'as John will tell you': no adjacency pair, both plausible; left unbound and noted; nothing rests on it"),
    ("not_merged", "the two labels carry different roles (the hoist and berths; invoices and the numbers), different rooms (the marina office; upstairs), different sites of evidence, and address and correct each other (00:03:44, 00:26:32); a merge would put the credits figure in the mouth of the person who waives the re-lift fee"),
])
I["vocative_slot_tests"] = [
    OrderedDict([("token", "tag"), ("coerced_at", "00:05:49"), ("licence", "sentence-initial and lowercase by position, set off by a comma, followed by a second-person imperative ('before you go on'), and the previous different speaker (the general manager) answers in the next turn ('Say it, you've got it.')"), ("not_coerced_at", ["00:10:10"]), ("reason", "'a tag on it with a number' is a noun in an ordinary slot; the cradle tag is data")]),
    OrderedDict([("token", "tie"), ("coerced_at", "00:11:11"), ("licence", "after 'Right,', set off by commas, followed by a second-person hand-off ('your go'), answered by the general manager at 00:11:17"), ("not_coerced_at", ["00:11:17", "00:30:05"]), ("reason", "'tie it into the cradle' and 'tie up a dinghy' are verbs in ordinary slots, one of them inside the very answer that binds the vocative")]),
    OrderedDict([("token", "tide"), ("coerced_at", "00:15:03"), ("licence", "sentence-initial, set off by a comma, followed by 'hang on, that's not what I said', a correction addressed to the previous speaker, who answers at 00:15:16 ('Three or four hours a week. Sorry.')"), ("not_coerced_at", ["00:08:49", "00:09:24", "00:21:50", "00:33:52", "00:37:02", "00:38:21", "00:38:40", "00:39:35", "00:40:17", "00:41:22"]), ("reason", "thirteen ordinary uses of 'the tide', 'the tide window', 'the tide tables' across ten units; the marina's whole scheduling rule is the tide, and a run that turns any of them into a name has broken the SOP")]),
]
I["not_invented"] = ["Tige", "Tyge", "Teague", "Tighe", "Tige Devon or Devon", "Thady", "tie, tag and tide as people", "a person named Devlin distinct from the general manager", "Maxine Bassett as a speaker or an attendee", "a second Bernie, or a Bernadette distinct from Bernie", "a third John from 'the wet John', 'the dry John', 'Other John' or 'John, John'", "Biscuit (a dog)", "'Maxine's number two' as a named person", "a fourth Threlfall by name"]
I["stakeholders_asserted"] = ["Tadhg Devlin (General Manager)", "Jon Ashby (Marina Manager)", "John Rudge (Finance and Admin Manager)", "Bernie Locke (Workshop Manager)", "Consultant", "and, mentioned only: Maxine Bassett, Aubrey Threlfall and the family board, Lorcan, Wojtek, the office administrator's number two, the engineers, the IT company, the berthing system vendor, the insurer, the surveyor, the boat owners, the competitor marina"]
I["unresolved_mentions"] = [OrderedDict([("location", "00:26:00"), ("token", "John"), ("state", "ambiguous between two resolved people"), ("basis", "no adjacency pair; both readings plausible; occurs inside the general manager's aside about his own list"), ("repair", "left unbound; recorded; no evidence and no stakeholder rests on it; one line in the audit log, not an open question")])]
I["confidence"] = OrderedDict([
    ("default", "certain"),
    ("probable", "the %d units under 'Maxine Bassett' until the alias table is confirmed, then certain; and every mention resolution of a rendered form (each Tige, Tyge, Teague, Tighe, Devon, Thady, each of the twenty resolved 'John' occurrences, the three coerced words) until confirmed" % turns_by["Maxine Bassett"]),
    ("uncertain", "the 'John' at 00:26:00 (ambiguous); nothing else, since no unit's speaker is in doubt"),
    ("unattributable", "none; no composite block exists"),
    ("propagation", "the worst state travels to anything derived: P2 Stated, P2 Workaround and every quote located under 'Maxine Bassett' are probable until the table is confirmed; P3 Concrete's frequency rests on 00:22:16 (certain, Jon Ashby's own claim) and not on the vocative at 00:22:03; nothing rests on a coerced word alone"),
])
I["recognition_errors"] = "the first name under the label 'Tadhg Devlin' is never rendered as spelled: Tige (8), Tyge (3), Teague (2), Tighe (1), and once the surname as Devon; 'Jon' is rendered 'John' in every spoken mention; all are in the alias map and none sits in a term slot"
I["composite_blocks"] = []
I["wedges"] = []
I["boundary_duplication"] = []
I["rejoined_sentences"] = []
I["second_hand"] = [
    OrderedDict([("location", "00:06:29"), ("what", "the chairman's ultimatum, quoted by the general manager"), ("state", "relayed; recorded as the general manager's account of it, never as the chairman's statement; the why-now stands without it")]),
    OrderedDict([("location", "00:37:02"), ("what", "the vendor's yard module and its price"), ("state", "a third-party claim relayed by the client; recorded as an alternative in play; not evaluated; the price is never netted against anything")]),
    OrderedDict([("location", "00:28:33"), ("what", "the office hours figure"), ("state", "the finance manager's estimate for an absent colleague, called soft by him; in the bleed with its softness recorded as the residual")]),
]
I["unit_unresolved_figures"] = ["'twenty years of Maxine in it' (00:08:20): an idiom for the book's age, not a duration to store", "'Dozens a day' (00:25:26): no count and no unit; not a figure, not multiplied", "'Seventy-two thousand and some' (00:27:59): the 'and some' is the client's own rounding of 72,036 and is kept as such"]
I["off_transcript"] = "none: no decision or figure correction arrived from outside the call; the credits figure was pulled the day before the call by the finance manager (00:26:26) and is the client's own"
I["quarantine"] = "not applicable: no screen shared and no demonstration frame of ours; the client's hypotheticals ('If April happens again', 'Say it's next April') are requirements evidence, not [X]"
I["package_order"] = "not applicable: one call"
I["silence"] = "not measurable: start-only stamps and no end times; the report says so rather than estimating"
I["talk_share"] = OrderedDict([
    ("client_by_words", round(client_words / TOT, 3)),
    ("client_by_seconds", "not computable (no end times)"),
    ("by_speaker_words", OrderedDict([("Tadhg Devlin", round(words_by["Tadhg Devlin"] / TOT, 3)), ("Jon Ashby", round(words_by["Jon Ashby"] / TOT, 3)), ("John Rudge", round(words_by["John Rudge"] / TOT, 3)), ("Maxine Bassett (Bernie Locke)", round(words_by["Maxine Bassett"] / TOT, 3)), ("Consultant", round(words_by["Consultant"] / TOT, 3))])),
    ("note", "computed on merged units after repair; nothing to merge or repair in this file; the ratio is never read as a proxy for name quality"),
])
I["delivery_notes"] = [
    "Client share about %d percent by words; our longest turn is %d words at 00:38:40, the first-cut play-back; no own-side stretch longer than one turn." % (round(100.0 * client_words / TOT), len(longest[2].split())),
    "Defect: at 00:22:03 our side attributed the marina manager's twice-a-week figure to the finance manager by first name; corrected by the room within two turns and by our side at 00:22:28 ('Sorry. Ashby.').",
    "Good practice: our side proposed surnames when the room offered them (00:04:01) and used them from then on; asked which square was Maxine (00:00:45) and accepted the answer; self-corrected 'Maxine, sorry, Bernie' at 00:15:48; refused a guess on the office cost (00:25:53), refused to judge the vendor module unseen (00:37:30), refused the pricing request with a sequence (00:42:06), and pushed back on the twelfth honestly (00:33:52).",
    "Small talk dropped at intake: the dog, the kids, the wellies; 'I don't see my kids' plus a first name is re-identifying and carries nothing.",
]
K["intake"] = I


# ---------------- emitter: top-level pretty, entries one per line ----------------
def dumps(v):
    return json.dumps(v, ensure_ascii=False)


COMPACT_KEYS = {"bleed", "upside", "markers", "shred_counts", "turns_by_label", "by_speaker_words", "gates_met", "gates_not_met", "products_enabled", "borrowed_labels", "not_invented", "stakeholders_asserted", "detectors", "unit_unresolved_figures", "second_hand", "unresolved_mentions"}


def render(v, depth, ind, key=None):
    pad = "  " * ind
    pad1 = "  " * (ind + 1)
    if isinstance(v, dict):
        if depth > 3 or not v or key in COMPACT_KEYS:
            return dumps(v)
        parts = []
        for k, vv in v.items():
            parts.append('%s"%s": %s' % (pad1, k, render(vv, depth + 1, ind + 1, k)))
        return "{\n" + ",\n".join(parts) + "\n" + pad + "}"
    if isinstance(v, list):
        if depth > 3 or not v or key in COMPACT_KEYS:
            return dumps(v)
        parts = []
        for e in v:
            if key == "alias_map" and isinstance(e, dict) and any(isinstance(x, list) and len(x) > 6 for x in e.values()):
                parts.append(pad1 + render_entry(e, ind + 1))
            else:
                parts.append(pad1 + dumps(e))
        return "[\n" + ",\n".join(parts) + "\n" + pad + "]"
    return dumps(v)


def render_entry(e, ind):
    # an alias-map entry: scalar keys one per line, its long list one item per line
    pad = "  " * ind
    pad1 = "  " * (ind + 1)
    pad2 = "  " * (ind + 2)
    parts = []
    for k, vv in e.items():
        if isinstance(vv, list) and len(vv) > 6:
            parts.append('%s"%s": [\n%s\n%s]' % (pad1, k, ",\n".join(pad2 + dumps(x) for x in vv), pad1))
        else:
            parts.append('%s"%s": %s' % (pad1, k, dumps(vv)))
    return "{\n" + ",\n".join(parts) + "\n" + pad + "}"


out = render(K, 1, 0) + "\n"
json.loads(out)  # must be valid JSON
open(DIR + "answer-key.json", "w").write(out)
print("key lines:", out.count("\n"))
print("rubric:", len(RUB), dict(Counter(r["status"] for r in RUB)))
print("asked true:", sum(1 for r in RUB if r["asked"]), "false:", sum(1 for r in RUB if not r["asked"]))
print("pains:", len(K["pains"]), "objections:", len(K["objections"]), "traps:", len(K["traps"]), "blocklist:", len(K["expected_leak_blocklist"]))
print("requested:", dict(Counter(r["type"] for r in K["requested_changes"])), "questions:", len(K["expected_questions_before_building"]), "accepted:", len(K["accepted_behaviours"]), "vocab:", len(K["vocabulary"]), "commitments:", len(K["commitments_and_next_steps"]))
print("measure: units", len(TURNS), "words", TOT, "short", short, "lower", lower, "unterm", unterm, "same_pairs", same_pairs, "gaps", min(gaps), max(gaps), "turns_by", dict(turns_by), "markers", dict(markers))
