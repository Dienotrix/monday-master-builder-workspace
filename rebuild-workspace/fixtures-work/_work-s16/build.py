#!/usr/bin/env python3
"""Authoring script for fixture s16-shred-cue (WP18, C58c, guards R2).

Generates transcript.txt (WebVTT, numbered cues, end times, 'Label: text'
payload) and answer-key.json. Cue numbers and timestamps in the key are
looked up from the generated transcript, never typed by hand.

Refuses to overwrite an existing fixture unless --force is given, because
re-running a build script silently undoes reviewed fixes (see COVERAGE.md).
Standard library only; runs on Python 3.9.
"""
import json
import os
import random
import re
import sys

OUT = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s16-shred-cue"

C = "Consultant"
I = "Ingrid Falkenrath"
S = "Sunniva Okonkwo-Reyes"
D = "D"

# (label, text[, flag]) ; flag "W" = wedge (0-1 ms gap both sides),
# "S" = shred fragment (tight gap after a different label)
E = [
    (C, "Hi Ingrid, can you hear me all right?"),
    (I, "I can, yes. Hi. Give me one second, I'm letting the others in."),
    (C, "No rush at all."),
    (I, "Okay. Right. So it's me, and Dorian, who runs the desk, the desk is our intake team,"),
    (I, "and Sunniva is here, she looks after the linguists, all the freelancers,"),
    (S, "Hi. Sorry, I'm on a laptop in the kitchen, they're painting the office this week."),
    (C, "Hi Sunniva. The kitchen's fine, I've had worse."),
    (I, "and Desmond, from finance, said he'd try to join at the half hour, he's got a client thing first."),
    (I, "Rowan couldn't make it. Rowan's our managing director, you'll meet Rowan next time."),
    (C, "Okay, that's helpful. Dorian, you're the one on the desk day to day, is that right?"),
    (D, "That's me, yeah."),
    (C, "Great. And how's the week going so far?"),
    (D, "It's Tuesday, so it's the day after Monday."),
    (I, "Every week is a busy one. That's kind of why we're talking to you."),
    (C, "Fair enough. So let me say what I'd like to do with the time, and you tell me if it's the wrong shape."),
    (C, "I'd like to spend most of it on how work comes in and moves through today, where it hurts,"),
    (C, "and what that's costing you, and only at the end say what a first version might look like."),
    (C, "I'm not going to show you anything today. Does that work?"),
    (I, "That works. Honestly I'd rather you heard it from Dorian and Sunniva than from me, I get the polished version."),
    (C, "Okay. Ingrid, can you give me the thirty-second version of the company first, for my notes?"),
    (I, "Sure. Quillbrook is a translation and localisation agency, we're in Providence. Forty-four people on payroll,"),
    (I, "forty-five on Monday, we've got a new project manager starting."),
    (I, "Most of the actual translation is done by freelancers. We call them linguists, everybody does."),
    (I, "Sunniva can tell you how many, I always get it wrong."),
    (S, "About three hundred on the bench. Two-eighty active, if active means they took a job this year."),
    (C, "And the bench is?"),
    (S, "The bench is my list of who's available, what languages they do, what they charge, and whether they're any good."),
    (S, "It's a spreadsheet. A big one. It's been a spreadsheet for eleven years."),
    (C, "Okay. And the kind of work?"),
    (I, "Three lines, roughly. Legal, so contracts and filings. Life sciences, which is mostly regulatory submissions,"),
    (I, "and that's the one that's growing. And marketing localisation, websites, campaigns, that sort of thing."),
    (I, "Regulatory is where the money is and also where the deadlines are, are the scary ones."),
    (I, "Marketing is the easy one. Nobody dies if a brochure is a day late."),
    (C, "And is any of this in monday today, or anything like it?"),
    (I, "No. Sunniva did a trial two years ago, for the bench, and it lapsed."),
    (S, "It lapsed because I was the only person in it. It was me talking to myself."),
    (I, "So no account. Nothing to inherit, which is probably a good thing."),
    (C, "Got it. So walk me through it. A request comes in. What actually happens, start to finish?"),
    (D, "Okay so. Everything lands in the box."),
    (D, "The box is a shared inbox, requests at our domain, everybody on the desk can see it."),
    (D, "A client sends a file, or a link, or sometimes just a note that says can you quote this,"),
    (D, "and no file, which is its own problem."),
    (C, "Mm-hm.", "W"),
    (D, "so somebody on the desk, usually me, opens it, works out what it is, what languages, what it's for,"),
    (D, "and puts it in the tracker."),
    (C, "The tracker being?"),
    (D, "A spreadsheet. One row per request. Date in, client, language pair, word count if we have it, who's quoting it, status."),
    (D, "Status is a column I type into. There's no list, it's whatever I type that day."),
    (C, "And who does the quote?"),
    (D, "Depends. If it's a straightforward document, the desk does it. We run the file through the TM,"),
    (D, "the TM being our translation-memory tool, it tells us the word count and how much of it is a repeat,"),
    (D, "and we price off that, per word, by language pair. If it's a big regulatory thing, a PM quotes it,"),
    (D, "because they need to know who's going to do it before they promise a date."),
    (C, "And how many of those requests come in a week, roughly, would you say"),
    (D, "Forty.", "W"),
    (C, "forty a week, okay, and of those how many turn into a job, roughly?"),
    (D, "Maybe twenty-five. Thirty in a good week."),
    (I, "It's more like forty-five now, Dorian, since the summer. Not forty."),
    (D, "Since the summer, yeah, okay, forty-five. It was forty in the spring, it's forty-five now."),
    (C, "Okay. And once it's a job?"),
    (D, "Then it gets a job number, which is also just the next row, in a different tab,"),
    (D, "and the PM picks a linguist, and it goes. Translate, edit, proof, we say TEP."),
    (D, "Three linguists on a regulatory job, two on most other things."),
    (D, "The PM chases each stage themselves, however they chase it, and when it's delivered"),
    (D, "they fill in the job sh"),
    (D, "sheet, which is a form, and the job sheet goes to Desmond, and Desmond bills from it."),
    (D, "And if the job sheet's wrong the invoice is wrong, and then it's Desmond in my box."),
    (S, "Picks a linguist from the bench. In theory."),
    (D, "In theory."),
    (C, "We'll come back to in theory. And after delivery, does the client ever come back with changes?"),
    (S, "Regulatory always comes back. The reviewer at the client flags things, the PM sends it back to the editor,"),
    (S, "and none of that is anywhere except the PM's own notes. If the PM's on holiday, good luck."),
    (I, "That's a whole other conversation. Park it."),
    (C, "Parked. Can I check I've got the shape right? Requests in the box, into the tracker, a quote from the TM or from a PM,"),
    (C, "then a job, a linguist from the bench, TEP, and a job sheet to Desmond."),
    (I, "That's it. That's the whole company on one line."),
    (C, "Okay. Ingrid, you said every week is busy. Where does this actually hurt?"),
    (I, "Two places. The first one is the box."),
    (I, "Things sit in it. Not for long, usually, but long enough, and the ones that sit are the ones that"),
    (I, "that matter, because a regulatory request is never small, and it's never patient."),
    (I, "A request comes in and then the whole thing sits in the box until somebody"),
    (D, "picks it up.", "S"),
    (D, "Which is usually me, on a Thursday."),
    (C, "Can you give me one? A specific time it sat."),
    (I, "Dorian, tell them about the Thursday thing."),
    (D, "Okay so, the Thursday thing."),
    (D, "In April, a regulatory client, one of our bigger ones, sent a request on a Monday afternoon."),
    (D, "Forty thousand words, a submission dossier, six languages, they needed a quote by the Wednesday."),
    (D, "It landed in the box at about four o'clock, and I was out on the Tuesday, and the person covering the box"),
    (D, "the box only does the flagged ones, and it wasn't flagged, because nobody flags things,"),
    (D, "so I found it on the Thursday, when I did the sweep."),
    (C, "The sweep being?"),
    (D, "Thursday afternoon I go through everything in the box that hasn't been moved to a folder and check it against the tracker."),
    (D, "Takes the whole afternoon. Sometimes it runs into Friday morning."),
    (C, "And the request?"),
    (D, "They'd gone with somebody else by then. They told us on the Friday. Politely."),
    (I, "That was a hundred and ten thousand dollar job, that one, if we'd priced it the way we usually do."),
    (I, "And they haven't sent us a regulatory job since. They still send us the marketing stuff. Small stuff."),
    (I, "We'd had that client six years."),
    (C, "Was that the only one?"),
    (I, "No. How many did we lose in the spring, Dorian, two?"),
    (D, "Two.", "W"),
    (I, "two in the spring, that we know about. The ones that just quietly don't come back, you don't know about."),
    (C, "What was the other one?"),
    (I, "Marketing client. Smaller. A brochure set, they asked twice and we answered the second time."),
    (I, "That one came back, actually, so maybe it's one and a half. Call it two, it felt like two."),
    (C, "And why doesn't the current way work? You've got the sweep, you've got someone on the box every day."),
    (D, "Because the sweep is once a week and the box is forty-five a week. Sorry, forty-five requests a week."),
    (D, "And because it's me. If I'm out, it's whoever's covering, and covering means answering the flagged ones."),
    (I, "And because it doesn't scale. If the January thing lands the way Rowan thinks it will,"),
    (I, "we're not at forty-five a week, we're at seventy, eighty, and the sweep is a whole day, and Dorian's already"),
    (I, "already doing ten hours a week on it."),
    (C, "Okay, hold that ten hours, I'm going to come back to it. Who else feels it when a request sits?"),
    (I, "The client, obviously. The PM who ends up quoting it in a panic on the Thursday night."),
    (I, "Rowan, because Rowan hears about it from the client. And me, because I hear about it from Rowan."),
    (S, "And the linguists, because a panic quote turns into a panic job, and a panic job means I'm calling people on a Sunday."),
    (C, "And if nothing changes, what does next year look like on the box?"),
    (I, "Like this year but with the January account on top. Which is the part that keeps me up, honestly."),
    (I, "Twice the regulatory volume through a box that already loses things."),
    (C, "Okay. Second place it hurts. You said two."),
    (I, "The bench. Sunniva, you tell it, it's yours."),
    (S, "So the bench, like I said, is my list. When a job comes in, the PM is supposed to ask me who's free,"),
    (S, "and I look at the bench and I say, use this person, they're free that week, they've done this client before,"),
    (S, "and then I mark them as booked. That's the idea."),
    (C, "Right.", "W"),
    (S, "What actually happens is the PMs have their own favourites, and they message them directly,"),
    (S, "and the linguist says yes, because linguists say yes to everything,"),
    (S, "and I find out when the linguist writes to me asking why they've been booked for two"),
    (D, "two jobs in the same week.", "S"),
    (D, "Yeah. That happened."),
    (C, "How does a PM see the bench today?"),
    (S, "They don't. They ask me. Or they don't ask me, which is the problem."),
    (D, "We always check the bench first though, on the desk."),
    (S, "Not always.", "W"),
    (D, "well. Mostly. The desk does."),
    (S, "The desk does. The PMs don't."),
    (C, "Can you give me a specific one?"),
    (S, "June. Hang on, let me find the actual week."),
    (S, "Kirsten."),
    (S, "No, sorry, wrong tab. Second week of June."),
    (S, "We had a linguist, German medical, one of maybe four we trust on regulatory,"),
    (S, "booked by me on a submission for one client, and booked by Bastian, one of the PMs, on a different submission,"),
    (I, "That's the one.", "W"),
    (S, "same week, and she said yes to both, and she did both, and both were late."),
    (S, "And we paid a second linguist a rush premium on the second one to catch up the review."),
    (C, "What did that cost?"),
    (S, "The rush premium? I don't know the total for the year. Desmond has the actual number, I only see the ones I approve."),
    (I, "I'd guess, but I'd rather Desmond told you. It's not nothing. It's a few thousand a year, at least."),
    (C, "Okay, that's fine, we'll get it from Desmond. Sunni, what was the linguist's rate on that one?"),
    (S, "Doesn't matter, and I'm not saying it on a call. Rates stay on the bench."),
    (C, "Fair. And who gets hurt when that happens?"),
    (S, "The linguist, first. She was working nights. The two PMs, who both think the other one stole her."),
    (S, "The client whose review was late. And me, because I'm the one apologising to all of them."),
    (C, "And what happens to the bench in twelve months if nothing changes?"),
    (S, "It gets worse, because regulatory doubles and I've got four German medical people, not eight."),
    (S, "And the new PM starts Monday, and the new PM doesn't know who's on the bench, so they'll just ask Bastian."),
    (S, "And Bastian will give them his favourites, and his favourites are already booked."),
    (C, "Okay. Let me ask about time. Dorian, you said ten hours a week on the sweep."),
    (D, "Ten on the sweep and the checking. Then the tracker itself, the typing, maybe another"),
    (D, "another five. Call it fifteen a week for me."),
    (C, "And is it only you?"),
    (D, "Mostly me. Priya covers when I'm out, and she does the flagged ones every day anyway, so, five or six hours of hers?"),
    (I, "Say six."),
    (C, "So twenty-one hours a week between the two of them. What does that cost you, loaded?"),
    (I, "Loaded. Um."),
    (I, "Dorian's about forty-eight an hour, loaded, I think. I'd have to check that with Desmond."),
    (I, "Priya's less. Call them both forty-five and I'm probably close."),
    (C, "Do you want to do the math, or should I?"),
    (I, "I'll do it. Twenty-one times forty-five is, nine hundred and forty-five a week."),
    (I, "Times fifty-two. Forty-nine thousand, one hundred and forty."),
    (I, "So call it forty-nine thousand a year on the desk, just on the sweep and the tracker."),
    (C, "Does that feel right?"),
    (I, "It feels light. It doesn't have the rush premiums in it, and it doesn't have the PMs quoting at midnight."),
    (I, "And it doesn't have the hundred and ten thousand dollar job we didn't get. But it's the number I can stand behind today."),
    (C, "Okay. Forty-nine thousand a year, your number, rush premiums to come from Desmond. I'll keep the lost job separate."),
    (I, "Yes. Keep it separate. Rowan will want to see it, but it's not a cost, it's a job we didn't get."),
    (C, "And the January account. What is it, if you can say?"),
    (I, "I can say what it is, I can't say who. A pharmaceutical company, a big one, regulatory submissions, multi-language,"),
    (I, "starts the fifth of January. It's roughly double our current regulatory volume, on its own."),
    (C, "And what's it worth?"),
    (I, "I'd rather not say the number on this call. That's Rowan's to share. It's the biggest contract we've signed."),
    (C, "That's fine, I won't guess at it. What would you do with the desk time, if you got it back?"),
    (I, "Not hire. That's the honest answer. We've budgeted another coordinator for January because of the account,"),
    (I, "and that's a fifty-five thousand dollar salary, more with everything on top,"),
    (I, "and if the desk could handle eighty a week without the sweep, I'd rather spend that on a PM."),
    (C, "So the upside you'd claim is the coordinator you don't hire."),
    (I, "Yes. Fifty-five thousand, and honestly I'd take that to Rowan tomorrow."),
    (C, "Okay. Sunniva, anything on the upside from your side?"),
    (S, "Fewer Sundays. I don't know how to put a number on that, and I'd rather you didn't."),
    (C, "I won't."),
    (I, "Sorry, one second. Desmond's just messaged, he's not going to make it. Client thing overran."),
    (C, "No problem. We'll get his numbers after."),
    (C, "Let me ask the picture question. Say it's March. It's working. What does a Tuesday morning look like for each of you?"),
    (I, "One screen. Every request that came in this week, who's quoting it, and whether it's out the door."),
    (I, "And if something's been sitting more than a day, it's red, and I don't have to ask Dorian."),
    (D, "I stop doing the sweep. That's mine. Things get flagged when they come in, not on a Thursday."),
    (S, "The PMs can see the bench without asking me, and they can't book someone I've already booked."),
    (S, "Or they can, but it shouts at them. And they see language pairs, not just languages."),
    (C, "And for Rowan? What does Rowan want out of this?"),
    (I, "Rowan said, at the offsite, no more losing jobs we never quoted. That's the line."),
    (I, "I'm paraphrasing, but that's the line. I'd want Rowan to say it to you, not me."),
    (C, "Understood, I'll hold it as yours until then. Let me ask how a decision like this gets made here."),
    (I, "So I own the operations budget. Anything under fifteen thousand a year I can sign"),
    (I, "sign myself. Over that, Rowan signs."),
    (I, "And honestly Rowan would want to see it either way, because Rowan's the one who gets the phone calls."),
    (C, "And Desmond?"),
    (I, "Desmond cares about two things. That it doesn't touch the books without him knowing,"),
    (I, "the books being our accounting system, and that we're not paying for seats nobody uses."),
    (I, "He doesn't sign, but he can slow it down a lot."),
    (C, "Anyone on the IT side?"),
    (I, "We use an outside provider. They have a checklist. Single sign-on, where the data sits, that sort of thing."),
    (I, "It's a checklist, not a person with an opinion."),
    (C, "And what would Rowan need to see to say yes?"),
    (I, "The desk. Requests coming in and going out, and nothing sitting. Rowan is not going to care about the bench."),
    (S, "Rowan will care about the bench the next time we pay a rush premium."),
    (I, "Fair."),
    (C, "When did you last buy something like this, and how did that go?"),
    (I, "The TM tool, three years ago. I did a one-page thing, cost and what it saved, and Rowan signed it in a week."),
    (I, "Rowan's fast when the numbers are clear. Slow when they're not."),
    (I, "So if you can send me something Rowan can read in five minutes, what it costs and what it saves, that's the way in."),
    (C, "I'll send a recap of what I heard, not a price. We're not at a price yet, and I'd rather not guess at one."),
    (I, "That's fine. I just want you to know the shape of what works here."),
    (C, "Okay. Timing. When does this need to be working?"),
    (I, "Before the account starts. The fifth of January."),
    (C, "Okay.", "W"),
    (I, "Which really means the first week of December,"),
    (I, "because nobody's learning anything in December, December is our worst month, everyone's shipping year-end."),
    (C, "So the desk part, requests in and out, live in the first week of December."),
    (I, "The desk part. The bench I'd love, but if it's January that's"),
    (S, "Fine.", "S"),
    (S, "I'd rather not live with it till January, for the record."),
    (I, "Noted."),
    (C, "What could stop this? What gets in the way?"),
    (I, "The PMs. If it's another thing they have to type into, they'll message Bastian's favourite linguist and carry on."),
    (D, "And the desk can't be typing things twice. If it's the tracker and this, I'm not doing both."),
    (S, "And the linguists are not going to log into anything. They're freelancers, they've got twenty agencies each."),
    (S, "So whatever this is, the bench has to work without the linguists touching it."),
    (I, "And the IT checklist. It's never stopped anything, but it's slowed a couple of things down by a month."),
    (C, "Okay. Four things. PMs, double entry, linguists staying out, and the checklist."),
    (I, "And December. Don't ask anyone to learn anything in December."),
    (C, "Five. Let me play back what I'd put in a first version, just to see if it's the right shape, not to agree anything."),
    (C, "One, requests. Everything from the box lands as a request with a date, a client, a language pair, a status you pick from a list,"),
    (C, "and a flag when it's been sitting more than a day. Two, quotes to jobs. A request that's won becomes a job with a"),
    (C, "a number, and the stages, translate, edit, proof, on it. Three, the bench. Linguists as a list with language pairs and availability,"),
    (C, "and a PM booking someone shows up against their week, so a double booking shouts."),
    (C, "Linguists don't log in. And the books stay where they are, we don't touch the accounting system in a first version."),
    (I, "That's the right shape. Two things."),
    (I, "The bench needs language pairs, not languages. German into English is not English into German."),
    (S, "And direction matters most on regulatory, some people only do one way."),
    (I, "And I don't want linguists as users, ever, not just in the first version."),
    (C, "Both fine. Anything else?"),
    (D, "The status list. If you make me a list, let me add to it. I'll need a status you haven't thought of by Wednesday."),
    (C, "That's fair, I'll make it editable. And the accounting side?"),
    (I, "Leave it. Desmond will want to talk about it, and that's a later conversation, with him in the room."),
    (C, "Okay. Is this something you want to take forward?"),
    (I, "Yes. I want to see it. Rowan will want to see it before we call it a scope, though, so don't take my yes as the yes."),
    (C, "Understood. Can we put a time in for me to walk the three of you through a first version? Rowan too, if you can get him."),
    (I, "Monday the twenty-eighth is good for me. Morning."),
    (D, "I'm good Monday."),
    (S, "Monday's fine if it's before noon, I've got linguists at noon."),
    (C, "Eleven Eastern, forty-five minutes?"),
    (I, "Eleven works. I'll ask Rowan, but don't wait on him."),
    (C, "I'll send the invite before we hang up. Dorian, could you send me the tracker, with the client names taken out if you need to?"),
    (D, "Yeah. I can do that today. Names out is easy, it's a column."),
    (C, "And Ingrid, the rush premium total and the loaded rates from Desmond, whenever he can."),
    (I, "I'll ask him this afternoon. He was supposed to be here. He'll have it by Friday."),
    (C, "And I'll send a short recap tomorrow, what I heard and what's next, and you tell me where I got it wrong."),
    (I, "Perfect."),
    (C, "One last thing. Anything I should not write down?"),
    (I, "Client names. And rates, any rates. Everything else is fine."),
    (C, "Understood. Thanks, all three of you. Sunniva, enjoy the kitchen."),
    (S, "Ha. Bye."),
    (D, "Bye."),
    (I, "Thanks. Bye."),
]


def fmt(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return "%02d:%02d:%02d.%03d" % (h, m, s, ms)


def build_cues():
    rng = random.Random(1616)
    cues = []
    t = 2.310
    prev_label = None
    prev_wedge = False
    for i, e in enumerate(E):
        label, text = e[0], e[1]
        flag = e[2] if len(e) > 2 else ""
        words = len(text.split())
        rate = rng.uniform(2.2, 3.0)
        dur = max(0.7, words / rate + rng.uniform(0.15, 0.6))
        if flag == "W" or prev_wedge:
            gap = rng.choice([0.0, 0.001])
        elif flag == "S":
            gap = rng.uniform(0.02, 0.07)
        elif label == prev_label:
            gap = rng.uniform(0.04, 0.35)
        else:
            gap = rng.uniform(0.25, 0.95)
        start = t + gap
        end = start + dur
        cues.append({"n": i + 1, "label": label, "text": text, "flag": flag,
                     "start": start, "end": end, "gap": gap})
        t = end
        prev_label = label
        prev_wedge = (flag == "W")
    return cues


def render_vtt(cues):
    out = ["WEBVTT", ""]
    for c in cues:
        out.append(str(c["n"]))
        out.append("%s --> %s" % (fmt(c["start"]), fmt(c["end"])))
        out.append("%s: %s" % (c["label"], c["text"]))
        out.append("")
    return "\n".join(out)


CUES = build_cues()
BY_N = {c["n"]: c for c in CUES}


def find(sub, label=None, nth=None):
    hits = [c for c in CUES if sub in c["text"] and (label is None or c["label"] == label)]
    if nth is not None:
        hits = [hits[nth]]
    if len(hits) != 1:
        raise SystemExit("find(%r): %d hits" % (sub, len(hits)))
    return hits[0]


def loc(sub, label=None, nth=None):
    c = find(sub, label, nth)
    return "cue %d, %s, %s" % (c["n"], fmt(c["start"]), c["label"])


def q(sub, label=None, nth=None):
    return {"quote": sub, "location": loc(sub, label, nth)}


def n(sub, label=None, nth=None):
    return find(sub, label, nth)["n"]


def rng_(a, b):
    return "cues %d-%d" % (a, b)


def stats():
    words = {}
    total = 0
    for c in CUES:
        w = len(c["text"].split())
        words[c["label"]] = words.get(c["label"], 0) + w
        total += w
    same = sum(1 for a, b in zip(CUES, CUES[1:]) if a["label"] == b["label"])
    lower = sum(1 for c in CUES if c["text"][0].islower())
    term = sum(1 for c in CUES if c["text"].rstrip()[-1] in ".?!")
    maxw = max(len(c["text"].split()) for c in CUES)
    maxs = max(c["end"] - c["start"] for c in CUES)
    return {"words": words, "total": total, "same": same, "pairs": len(CUES) - 1,
            "lower": lower, "term": term, "maxw": maxw, "maxs": maxs,
            "end": CUES[-1]["end"], "n": len(CUES)}


ST = stats()
client_words = ST["total"] - ST["words"][C]
share = lambda k: round(100.0 * ST["words"][k] / ST["total"])
same_share = round(100.0 * ST["same"] / ST["pairs"])
minutes = round(ST["end"] / 60.0, 1)
lower_share = round(100.0 * ST["lower"] / ST["n"])
term_share = round(100.0 * ST["term"] / ST["n"])

# ---- anchors used by the key ----
RA = find("Dorian, you're the one on the desk")["n"]; RB = find("That's me, yeah.")["n"]
RC = find("Dorian, tell them about the Thursday thing.")["n"]; RD = find("Okay so, the Thursday thing.")["n"]
ROS1 = find("So it's me, and Dorian")["n"]; ROS2 = find("and Sunniva is here")["n"]
ROS3 = find("I'm on a laptop in the kitchen")["n"]; ROS4 = find("and Desmond, from finance")["n"]; ROS5 = find("Rowan couldn't make it.")["n"]
W1 = find("Mm-hm.")["n"]; W2 = find("Forty.")["n"]; W3 = find("Two.", D)["n"]; W4 = find("Right.", C)["n"]
W5 = find("Not always.")["n"]; W6 = find("That's the one.")["n"]; W7 = find("Okay.", C, 0)["n"]
SH1a = find("sits in the box until somebody")["n"]; SH1b = find("picks it up.")["n"]; SH1c = find("Which is usually me, on a Thursday.")["n"]
SH2a = find("asking why they've been booked for two")["n"]; SH2b = find("two jobs in the same week.")["n"]; SH2c = find("Yeah. That happened.")["n"]
SH3a = find("if it's January that's")["n"]; SH3b = find("Fine.", S)["n"]; SH3c = find("I'd rather not live with it")["n"]
DUP1 = (find("the ones that sit are the ones that")["n"], find("that matter, because")["n"])
DUP2 = (find("the person covering the box")["n"], find("the box only does the flagged ones")["n"])
DUP3 = (find("and Dorian's already")["n"], find("already doing ten hours")["n"])
DUP4 = (find("maybe another")["n"], find("another five.")["n"])
DUP5 = (find("I can sign")["n"], find("sign myself.")["n"])
DUP6 = (find("becomes a job with a")["n"], find("a number, and the stages")["n"])
TR = (find("they fill in the job sh")["n"], find("sheet, which is a form")["n"])
KIR = find("Kirsten.")["n"]
SUNNI = find("Sunni, what was the linguist's rate")["n"]; SUNNI2 = find("Doesn't matter, and I'm not saying it on a call.")["n"]
QA1 = find("how many of those requests come in a week")["n"]
SUP = find("Since the summer, yeah, okay, forty-five.")["n"]; SUPI = find("It's more like forty-five now, Dorian")["n"]
QA2 = find("How many did we lose in the spring, Dorian, two?")["n"]; QA2b = find("two in the spring, that we know about.")["n"]
QA3a = find("We always check the bench first though")["n"]; QA3b = find("well. Mostly. The desk does.")["n"]
QA4a = find("and booked by Bastian")["n"]; QA4b = find("same week, and she said yes to both")["n"]
BL1 = find("I'll do it. Twenty-one times forty-five")["n"]; BL3 = find("So call it forty-nine thousand a year on the desk")["n"]
TH1 = find("It landed in the box at about four o'clock")["n"]; TH3 = find("so I found it on the Thursday, when I did the sweep.")["n"]
TJ1 = find("And because it doesn't scale.")["n"]
SIT1 = find("Things sit in it.")["n"]
DT1 = find("Ten on the sweep and the checking.")["n"]
DES = find("Desmond's just messaged")["n"]
AG1 = find("So let me say what I'd like to do with the time")["n"]; AG2 = find("That works. Honestly I'd rather you heard it")["n"]
NOSHOW = find("I'm not going to show you anything today.")["n"]
SMALL = [find("I'm on a laptop in the kitchen")["n"], find("The kitchen's fine")["n"], find("It's Tuesday, so it's the day after Monday.")["n"], find("Sunniva, enjoy the kitchen.")["n"]]
ONEHALF = find("so maybe it's one and a half")["n"]

MR1 = "I'll do it. Twenty-one times forty-five is, nine hundred and forty-five a week. Times fifty-two. Forty-nine thousand, one hundred and forty. So call it forty-nine thousand a year on the desk, just on the sweep and the tracker."
MR2 = "It landed in the box at about four o'clock, and I was out on the Tuesday, and the person covering the box only does the flagged ones, and it wasn't flagged, because nobody flags things, so I found it on the Thursday, when I did the sweep."
MR3 = "And because it doesn't scale. If the January thing lands the way Rowan thinks it will, we're not at forty-five a week, we're at seventy, eighty, and the sweep is a whole day, and Dorian's already doing ten hours a week on it."
MR4 = "Things sit in it. Not for long, usually, but long enough, and the ones that sit are the ones that matter, because a regulatory request is never small, and it's never patient."
MR5 = "Ten on the sweep and the checking. Then the tracker itself, the typing, maybe another five. Call it fifteen a week for me."

KEY = {}
KEY["scenario_id"] = "s16-shred-cue"
KEY["call_type"] = "discovery"
KEY["purpose_of_this_fixture"] = (
    "Calibration fixture (REAL-CALL-LESSONS.md C58c; guards reversal R2, the speaker boundary rather than the turn boundary). "
    "A cue-export discovery call: every unit is individually timed with a start and an end, a unit is a breath rather than a turn, and a sentence routinely spans two to four units of the same speaker, so roughly two fifths of adjacent units share a label. "
    "Planted on purpose: (1) seven tight wedges, one speaker's short unit inside another speaker's run at a 0 or 1 ms gap on both sides, four of them genuine client speech and three of them our own backchannels, none of which may be absorbed into the surrounding run; "
    "(2) six boundary-word duplications, where the last word or two of a unit is re-emitted as the first of the next same-speaker unit, plus one sub-word truncation, each removed only in derived text and never inside quotation marks; "
    "(3) three cross-label shreds, where the tail of one speaker's sentence sits under the next speaker's label, one of which could stand alone as a backchannel and is therefore 'boundary artifact, owner unresolved' rather than a re-attribution; "
    "(4) a single-initial label, 'D', that phonetic and edit-distance tests cannot resolve and first-letter matching cannot either, because the narrated roster holds two people whose names begin with D, so only the adjacency pairs resolve it to Dorian; "
    "(5) a vocative matching nobody, 'Kirsten.', the whole content of a very short unit, occurring once with no adjacency-pair support, which is name-shaped noise kept out of the stakeholder list and surfaced as an open question; "
    "(6) a roster narrated aloud across two client turns split by a colleague's interruption, listing one attendee, the finance lead, who never joins, so the figures only that role could supply are 'not obtainable from this room'. "
    "It tests that intake runs both detectors and only the wedge flagger fires; that a quote across same-speaker units is a merged run cited as 'cues N-M' at [Q/recon] after de-duplication; that a quote whose first or last word sits under another speaker's label is refused while the units either side stay quotable; that the answer half of an adjacent question-answer pair is kept as an utterance with both unit numbers even when it is one word; and that grading still lands on the client's own confirmed figures with the residual and the unobtainable element named as gap questions rather than vanishing. "
    "Method content is deliberately ordinary: a strong discovery at a translation agency, Discovery complete, one build to propose, so nothing about the grading distracts from the intake repair.")
KEY["transcript_format"] = (
    "WebVTT from a video meeting: a 'WEBVTT' header line, then numbered cues from 1 to %d, each with a timing line 'HH:MM:SS.mmm --> HH:MM:SS.mmm' (zero-padded, millisecond precision, strictly monotonic, no overlaps, no collisions) and one payload line 'Label: text'. "
    "Labels are display names as the export emitted them: 'Consultant', 'Ingrid Falkenrath', 'Sunniva Okonkwo-Reyes' and the bare initial 'D'. No participant header, no artifact markers, no call date; ASCII only. "
    "%d cues, about %d spoken words, running %s minutes to %s. Units are short (longest %d words, %.1f seconds); a sentence often spans two to four units of one speaker, so %d of %d adjacent cue pairs (%d percent) share a label, %d percent of cues begin lowercase and only %d percent end in terminal punctuation. "
    "Wedges sit at 0-1 ms gaps; ordinary speaker changes at 250-950 ms; same-speaker continuations at 40-350 ms; shred fragments at 20-70 ms. "
    "Talk share by words: Ingrid Falkenrath %d percent, Sunniva Okonkwo-Reyes %d percent, D %d percent, Consultant %d percent (client %d percent). "
    "Every location in this key is 'cue N, HH:MM:SS.mmm, Label' with the label exactly as printed, so Dorian's cues are cited as 'D'; a merged run is cited as 'cues N-M'. "
    "The weekday and date pairs (a Tuesday call, 'Monday the twenty-eighth', a contract starting 'the fifth of January') fit a call on Tuesday 22 September 2026 with the walkthrough on Monday 28 September and the contract on Tuesday 5 January 2027; the date is not stated."
    % (ST["n"], ST["n"], ST["total"], minutes, fmt(ST["end"]), ST["maxw"], ST["maxs"], ST["same"], ST["pairs"], same_share, lower_share, term_share,
       share(I), share(S), share(D), share(C), 100 - share(C)))
KEY["company"] = {
    "name": "Quillbrook (Quillbrook Language Services; the client says 'Quillbrook')",
    "industry": "Translation and localisation agency. Three lines: legal (contracts and filings), life sciences (mostly regulatory submissions, the growing line) and marketing localisation (websites, campaigns). Regulatory work is 'where the money is' and where the deadlines bite.",
    "size": "Forty-four people on payroll, forty-five from the following Monday (a new project manager). About three hundred freelance linguists on the bench, two hundred and eighty active this year.",
    "locations": "Providence, Rhode Island. Linguists are remote freelancers.",
    "current_tools": [
        "The box: a shared inbox where every request lands, visible to the whole desk.",
        "The tracker: a spreadsheet with one row per request (date in, client, language pair, word count, who is quoting, a free-typed status) and a second tab for jobs.",
        "The bench: a spreadsheet of linguists kept by the vendor manager for eleven years, with languages, rates, availability and quality notes.",
        "The TM: a translation-memory tool that gives the word count and the repeat share for quoting.",
        "The books: an accounting system the finance lead bills from, fed by a job sheet the PM fills in at delivery.",
        "Direct messages from PMs to favoured linguists, outside the bench (channel not named).",
        "monday.com: none. A trial for the bench two years ago lapsed because only one person used it."
    ]
}
KEY["attendees"] = [
    {"name": "Ingrid Falkenrath", "role": "Operations Director. Owns the operations budget and signs anything under fifteen thousand dollars a year; above that the managing director signs, and she wants him to see it either way.", "side": "client", "decision_role": "approver (under the fifteen-thousand-dollar threshold; the managing director above it)"},
    {"name": "Dorian (surname not stated; export label 'D')", "role": "Runs the desk, the intake team: opens the box, keeps the tracker, quotes straightforward documents, does the Thursday sweep.", "side": "client", "decision_role": "influencer and end user"},
    {"name": "Sunniva Okonkwo-Reyes", "role": "Vendor manager. Keeps the bench, books linguists, approves rush premiums she sees, apologises when a linguist is double-booked.", "side": "client", "decision_role": "influencer and end user"},
    {"name": "Desmond (surname not stated)", "role": "Finance lead. Named in the narrated roster as trying to join at the half hour; a message reported at cue %d says he is not coming. Never speaks. Holds the rush premium total and the loaded rates, and cares that nothing touches the books without him." % DES, "side": "client", "decision_role": "influencer (listed, never joined; can slow a purchase down but does not sign)"},
    {"name": "Consultant", "role": "monday.com consultant running the discovery call", "side": "consultant", "decision_role": "not applicable"}
]
KEY["expected_monday_products"] = [
    {"kind": "core", "why": "monday Work Management for the desk and the bench. Requests from the box become items with a date in, client, language pair, a status picked from an editable list and a flag after a day of sitting; a won request becomes a job with a number and the TEP stages; the bench becomes a linguist list with language pairs and availability, with PM bookings shown against each linguist's week so a double booking shouts; a dashboard gives Ingrid her one screen. Linguists are never users. Traces to P1 (requests sitting in the box) and P2 (double-booked linguists). Tier is never stated and there is no account, so no portfolio is assumed."},
    {"kind": "crm", "why": "Conditional, as a question. Requests and quotes are deal-shaped and the clients are account-shaped, so if the client wants quoting run as a pipeline with client records rather than as a queue, that half must sit on the account's native CRM template boards (Deals/Opportunities, Accounts), detected first and relabelled to 'requests' and 'clients', never rebuilt as look-alikes. The call asked for a queue with a flag, not a pipeline, so this is asked before building, not assumed. Service is not indicated (the box is an intake queue for quotes, not a ticket desk) and Dev is out of v1."}
]

def row(crit, status, asked, ev, note):
    return {"criterion": crit, "status": status, "asked": asked, "evidence": ev, "note": note}

KEY["rubric"] = [
    row("R1 Current state mapped", "met", True, [q("Everything lands in the box."), q("A spreadsheet. One row per request. Date in, client, language pair, word count if we have it, who's quoting it, status."), q("The bench is my list of who's available, what languages they do, what they charge, and whether they're any good.")],
        "Intake (the box), the tracker, quoting (the TM or a PM), jobs with TEP, the bench, the job sheet to finance, and no monday account. The Consultant's one-line shape check is confirmed by Ingrid ('That's it. That's the whole company on one line.'). Thin: how the box is covered day to day beyond the flagged ones, and how PMs chase stages ('however they chase it')."),
    row("R2 Pain made concrete", "met", True, [q("They'd gone with somebody else by then. They told us on the Friday. Politely."), q("same week, and she said yes to both, and she did both, and both were late.")],
        "P1 and P2 are both excavated: Stated, Concrete and Workaround Met, with a dated instance each (the April request that sat until the Thursday sweep; the June German medical double booking)."),
    row("R3 Why now", "met", True, [q("starts the fifth of January. It's roughly double our current regulatory volume, on its own."), q("And they haven't sent us a regulatory job since. They still send us the marketing stuff. Small stuff.")],
        "Client-side change (a pharmaceutical account doubling regulatory volume), client-side trigger (accounts lost in the spring) and a client-side clock (the fifth of January, then the first week of December). Our side supplied no date."),
    row("R4 Bleed number", "met-with-residual", True, [q("So call it forty-nine thousand a year on the desk, just on the sweep and the tracker."), q("It feels light. It doesn't have the rush premiums in it, and it doesn't have the PMs quoting at midnight."), q("Dorian's about forty-eight an hour, loaded, I think. I'd have to check that with Desmond.")],
        "Client-built and confirmed: 21 h/wk (Dorian 15, Priya 6) x $45 loaded x 52 = $49,140, spoken as 'call it forty-nine thousand'. Elements: volume Met, frequency Met, rate Met on a hedge, confirmation Met. Residual, as gap questions rather than a downgrade: the loaded rate is 'about forty-eight ... I'd have to check that with Desmond' and rush premiums are excluded because only the finance lead has the total (see P2 Cost inputs). The $110,000 job is revenue not won, kept out."),
    row("R5 Upside number", "met", True, [q("and that's a fifty-five thousand dollar salary, more with everything on top,"), q("Yes. Fifty-five thousand, and honestly I'd take that to Rowan tomorrow.")],
        "The coordinator hire budgeted for January and not made: $55,000 salary, 'more with everything on top', client-figured. The contract's value is withheld ('That's Rowan's to share') and Sunniva's 'Fewer Sundays' is unvalued at her request; neither is estimated."),
    row("R6 Desired outcome", "met", True, [q("One screen. Every request that came in this week, who's quoting it, and whether it's out the door."), q("I stop doing the sweep. That's mine. Things get flagged when they come in, not on a Thursday."), q("The PMs can see the bench without asking me, and they can't book someone I've already booked.")],
        "Day to day for all three speakers. The leadership line ('no more losing jobs we never quoted') is Ingrid paraphrasing the managing director and she says so; it shapes a question for him and is not his evidence."),
    row("R7 Decision process mapped", "met", True, [q("So I own the operations budget. Anything under fifteen thousand a year I can sign"), q("He doesn't sign, but he can slow it down a lot."), q("The TM tool, three years ago. I did a one-page thing, cost and what it saved, and Rowan signed it in a week.")],
        "Ingrid signs under $15,000 a year; Rowan (managing director, absent) above, and sees it either way; Desmond (finance, absent) does not sign but can slow it; an outside IT provider has a checklist (single sign-on, data location). Prior purchase: the TM tool, one page, signed in a week. Delegation shape: Ingrid runs it, Rowan holds the gate, Desmond holds the books."),
    row("R8 Priority and timing", "met", True, [q("Before the account starts. The fifth of January."), q("The desk part. The bench I'd love, but if it's January that's")],
        "The desk part live in the first week of December, because nothing is learned in December; the bench may slip to January (Sunniva objects, for the record). The client's clock, not ours."),
    row("R9 Blockers surfaced", "met", True, [q("The PMs. If it's another thing they have to type into, they'll message Bastian's favourite linguist and carry on."), q("And the desk can't be typing things twice. If it's the tracker and this, I'm not doing both."), q("And the linguists are not going to log into anything. They're freelancers, they've got twenty agencies each.")],
        "Five, in the client's words: PM adoption, double entry on the desk, linguists never logging in, the IT provider's checklist, and December."),
    row("R10 Next step committed", "met", True, [q("Monday the twenty-eighth is good for me. Morning."), q("Eleven works. I'll ask Rowan, but don't wait on him."), q("I'll send the invite before we hang up. Dorian, could you send me the tracker, with the client names taken out if you need to?")],
        "Monday the 28th, 11:00 Eastern, 45 minutes, a first-version walkthrough for the three of them, with the invite sent on the call; the managing director invited but not waited on. Discovery call, so the date-time-owner reading applies; the Consultant's invite line is the one admissible our-side next-step evidence and the client assents to it."),
    row("R11 Solution confirmed", "missing", False, [], "No demo yet; expected at this stage. Blocks only the v1.0 sign-off gate."),
    row("R12 Scope agreed verbally", "partial", True, [q("That's the right shape. Two things."), q("Yes. I want to see it. Rowan will want to see it before we call it a scope, though, so don't take my yes as the yes.")],
        "A first cut in four parts is played back 'not to agree anything' and Ingrid accepts its shape with two changes and one exclusion, then says the scope is the managing director's to call. Enough for a v0.1, not for a proposal."),
    row("P1 Stated", "met", True, [q("Things sit in it."), q("Which is usually me, on a Thursday.")], "P1: requests sit in the box until one person's weekly sweep finds them."),
    row("P1 Concrete", "met", True, [q("Forty thousand words, a submission dossier, six languages, they needed a quote by the Wednesday."), q("They'd gone with somebody else by then. They told us on the Friday. Politely.")], "April: a regulatory client's 40,000-word, six-language dossier landed on a Monday at about four, sat unflagged while Dorian was out, and was found on the Thursday sweep; the client had gone elsewhere. A six-year client that has sent no regulatory work since."),
    row("P1 Workaround", "met", True, [q("Thursday afternoon I go through everything in the box that hasn't been moved to a folder and check it against the tracker."), q("Because the sweep is once a week and the box is forty-five a week. Sorry, forty-five requests a week."), q("And because it's me. If I'm out, it's whoever's covering, and covering means answering the flagged ones.")], "Today: the Thursday sweep plus whoever covers the flagged ones. Why it will not do: once a week against forty-five requests a week, dependent on one person, and it does not scale to the January volume."),
    row("P1 Reach", "met", True, [q("The client, obviously. The PM who ends up quoting it in a panic on the Thursday night."), q("And the linguists, because a panic quote turns into a panic job, and a panic job means I'm calling people on a Sunday.")], "Client, PMs, the managing director, Ingrid, and linguists via panic jobs."),
    row("P1 Cost inputs", "met", True, [q("another five. Call it fifteen a week for me."), q("Priya's less. Call them both forty-five and I'm probably close.")], "Dorian 15 h/wk (10 sweep and checking, 5 tracker), Priya 6 h/wk ('five or six', Ingrid: 'Say six'), $45 loaded blended, hedged from 'about forty-eight' for Dorian. The lost $110,000 job is a stake, not a cost input."),
    row("P1 Trajectory", "met", True, [q("we're not at forty-five a week, we're at seventy, eighty, and the sweep is a whole day, and Dorian's already"), q("Twice the regulatory volume through a box that already loses things.")], "Seventy to eighty requests a week with the January account; the sweep becomes a whole day."),
    row("P2 Stated", "met", True, [q("What actually happens is the PMs have their own favourites, and they message them directly,"), q("The desk does. The PMs don't.")], "P2: PMs book linguists outside the bench, so linguists get double-booked. Dorian's 'We always check the bench first' is qualified at once by Sunniva's wedged 'Not always.' and his own 'well. Mostly.'"),
    row("P2 Concrete", "met", True, [q("We had a linguist, German medical, one of maybe four we trust on regulatory,"), q("And we paid a second linguist a rush premium on the second one to catch up the review.")], "Second week of June: one of about four trusted German medical linguists booked by Sunniva and by a PM on two submissions the same week; both late, a rush premium paid. 'Kirsten.' at cue %d is not her name; see the intake block." % KIR),
    row("P2 Workaround", "met", True, [q("and then I mark them as booked. That's the idea."), q("They don't. They ask me. Or they don't ask me, which is the problem.")], "Today: ask Sunniva, she reads the bench and marks the booking. Why it will not do: PMs cannot see the bench, so they bypass it, and she learns of a clash from the linguist."),
    row("P2 Reach", "met", True, [q("The linguist, first. She was working nights. The two PMs, who both think the other one stole her."), q("The client whose review was late. And me, because I'm the one apologising to all of them.")], "Linguist, both PMs, the client, Sunniva."),
    row("P2 Cost inputs", "not-obtainable", True, [q("The rush premium? I don't know the total for the year. Desmond has the actual number, I only see the ones I approve."), q("I'd guess, but I'd rather Desmond told you. It's not nothing. It's a few thousand a year, at least.")], "Asked, and not obtainable from this room: the rush premium total sits with the finance lead, who was listed and never joined. Role that can supply it: finance lead. 'A few thousand a year, at least' is a hedge and enters no total; Ingrid commits to getting the figure by Friday."),
    row("P2 Trajectory", "met", True, [q("It gets worse, because regulatory doubles and I've got four German medical people, not eight."), q("And the new PM starts Monday, and the new PM doesn't know who's on the bench, so they'll just ask Bastian.")], "Regulatory volume doubles against the same four trusted linguists, and a new PM inherits the bypass."),
]
KEY["pains"] = [
    {"quote": "Things sit in it.", "location": loc("Things sit in it."), "theme": "P1 Requests sit in the box until the weekly sweep"},
    {"quote": "And because it's me. If I'm out, it's whoever's covering, and covering means answering the flagged ones.", "location": loc("And because it's me."), "theme": "P1 Intake depends on one person"},
    {"quote": "Status is a column I type into. There's no list, it's whatever I type that day.", "location": loc("Status is a column I type into."), "theme": "P1 No shared status on a request"},
    {"quote": "What actually happens is the PMs have their own favourites, and they message them directly,", "location": loc("What actually happens is the PMs have their own favourites"), "theme": "P2 PMs book linguists outside the bench"},
    {"quote": "They don't. They ask me. Or they don't ask me, which is the problem.", "location": loc("They don't. They ask me."), "theme": "P2 PMs cannot see the bench"},
    {"quote": "And the new PM starts Monday, and the new PM doesn't know who's on the bench, so they'll just ask Bastian.", "location": loc("And the new PM starts Monday"), "theme": "P2 The bypass is inherited by new PMs"},
    {"quote": "and none of that is anywhere except the PM's own notes. If the PM's on holiday, good luck.", "location": loc("and none of that is anywhere except the PM's own notes."), "theme": "P3 Post-delivery client revisions live in PMs' notes (parked by the client; not graded)"}
]
KEY["numbers"] = {
    "bleed": {"value": "$49,140 per year, spoken as 'call it forty-nine thousand', client-built and confirmed: 21 h/wk (Dorian 15, Priya 6) x $45 loaded x 52. Ingrid says it feels light. Excluded: rush premiums (finance lead's figure, due Friday), PMs quoting at night, and the $110,000 job not won (revenue, one-off).", "quote": "So call it forty-nine thousand a year on the desk, just on the sweep and the tracker.", "status": "met-with-residual"},
    "upside": {"value": "$55,000 per year: the January coordinator hire not made ('more with everything on top', unquantified). The pharmaceutical contract's value is withheld and Sunniva's Sundays are unvalued; neither is estimated. Not added to the bleed.", "quote": "Yes. Fifty-five thousand, and honestly I'd take that to Rowan tomorrow.", "status": "met"}
}
KEY["vocabulary"] = [
    {"their_term": "the box", "meaning": "The shared inbox every request lands in", "likely_monday_object": "none; the source of items on a Requests board (not a board itself)"},
    {"their_term": "request", "meaning": "A client asking for a quote; forty-five a week", "likely_monday_object": "item on a Requests board, or the native CRM Deals/Opportunities board if quoting is run as a pipeline (ask)"},
    {"their_term": "the desk", "meaning": "The intake team Dorian runs (Dorian plus Priya covering)", "likely_monday_object": "people column or team"},
    {"their_term": "the tracker", "meaning": "The request spreadsheet, one row per request, jobs on a second tab", "likely_monday_object": "the Requests and Jobs boards it is replaced by"},
    {"their_term": "flagged", "meaning": "A request someone marked as needing attention; unflagged ones wait for the sweep", "likely_monday_object": "status label plus an automation after a day of sitting"},
    {"their_term": "the sweep", "meaning": "Dorian's Thursday-afternoon pass through the box against the tracker", "likely_monday_object": "none; the thing the build removes"},
    {"their_term": "quote", "meaning": "The price for a request, per word by language pair, from the TM count or a PM", "likely_monday_object": "number and status columns on the request"},
    {"their_term": "the TM", "meaning": "The translation-memory tool giving word count and repeat share", "likely_monday_object": "number columns (word count, repeat share); no integration asked for"},
    {"their_term": "job / job number", "meaning": "A won request; today the next row on the jobs tab", "likely_monday_object": "item on a Jobs board with an auto-number or ID"},
    {"their_term": "TEP", "meaning": "Translate, edit, proof: the three stages of a job, two or three linguists", "likely_monday_object": "status column or subitems per stage"},
    {"their_term": "linguist", "meaning": "A freelance translator, editor or proofreader; never a system user", "likely_monday_object": "item on a Linguists (bench) board; not a people column"},
    {"their_term": "the bench", "meaning": "Sunniva's spreadsheet of linguists with languages, rates, availability, quality", "likely_monday_object": "Linguists board with a bookings view; rates restricted or left off"},
    {"their_term": "language pair", "meaning": "Source into target, directional ('German into English is not English into German')", "likely_monday_object": "dropdown column of pairs, not of languages"},
    {"their_term": "rush premium", "meaning": "Extra paid to a linguist to catch up a late job", "likely_monday_object": "number column (restricted); total held by finance"},
    {"their_term": "job sheet", "meaning": "The form a PM fills in at delivery that finance bills from", "likely_monday_object": "board form or doc on the job; the books stay untouched"},
    {"their_term": "the books", "meaning": "The accounting system the finance lead bills from", "likely_monday_object": "none in the first version"},
    {"their_term": "the January account", "meaning": "An unannounced pharmaceutical client starting 5 January, doubling regulatory volume", "likely_monday_object": "dropdown label (client), name withheld until announced"}
]
KEY["entities_and_workflows"] = [
    "Request intake: a client sends a file, a link or a note to the box; someone on the desk (usually Dorian) opens it, works out language pair and purpose, and adds a row to the tracker with a free-typed status",
    "Quoting: straightforward documents are quoted by the desk from the TM's word count and repeat share, per word by language pair; big regulatory requests are quoted by a PM who first works out who will do the work",
    "Volume: forty-five requests a week since the summer (forty in the spring); twenty-five to thirty become jobs; seventy to eighty a week expected with the January account",
    "Job: a won request gets a job number on the jobs tab; the PM picks a linguist; stages are translate, edit, proof (TEP) with three linguists on regulatory and two elsewhere; the PM chases stages their own way",
    "Delivery and billing: the PM fills in the job sheet; the job sheet goes to the finance lead, who bills from the books; a wrong job sheet means a wrong invoice",
    "Post-delivery revisions on regulatory work live in the PM's own notes (parked by the client)",
    "The bench: PMs are meant to ask Sunniva, who reads the bench and marks the booking; PMs message favoured linguists directly; the June double booking of a German medical linguist across two submissions",
    "Buying process: Ingrid signs under $15,000 a year; the managing director above and sees it either way; the finance lead must know before anything touches the books; the outside IT provider runs a checklist; the TM tool was bought from a one-page case in a week",
    "People mentioned but not on the call: Rowan (managing director), Desmond (finance lead, listed, never joined), Priya (desk, covers Dorian), Bastian (PM who books his favourites), the new PM starting Monday"
]
KEY["integrations_mentioned"] = [
    "A shared inbox (the box): the source of requests; how requests reach the build (forwarding, a form, or retyping) is a question, not an integration asked for.",
    "A spreadsheet (the tracker, and separately the bench): the current data sources; Dorian sends the tracker with client names removed.",
    "A translation-memory tool (the TM): word counts and repeat share for quoting; no connection requested.",
    "An accounting system (the books): explicitly out of the first version; any later link needs the finance lead in the room.",
    "Single sign-on and data location: items on the outside IT provider's checklist."
]
KEY["compliance_or_security_signals"] = [
    "Linguist rates are confidential: 'Rates stay on the bench.' and 'And rates, any rates.' Never in seed data, item names or client-facing material.",
    "Client names are to be scrubbed from the tracker export and left out of notes ('Client names.').",
    "The January account is unannounced; the client will say what it is but not who, and the contract value is the managing director's to share.",
    "Regulatory submission dossiers are client-confidential documents; the build holds requests and jobs, not the files.",
    "The outside IT provider's checklist: single sign-on and where the data sits."
]
KEY["objections"] = [
    {"quote": "The PMs. If it's another thing they have to type into, they'll message Bastian's favourite linguist and carry on.", "type": "Team won't adopt it"},
    {"quote": "And the desk can't be typing things twice. If it's the tracker and this, I'm not doing both.", "type": "Team won't adopt it (double entry)"},
    {"quote": "Yes. I want to see it. Rowan will want to see it before we call it a scope, though, so don't take my yes as the yes.", "type": "Must check with someone (the managing director was not on the call)"},
    {"quote": "Leave it. Desmond will want to talk about it, and that's a later conversation, with him in the room.", "type": "Must check with someone (the finance lead, on anything touching the books)"},
    {"quote": "And December. Don't ask anyone to learn anything in December.", "type": "Wrong time, next quarter (December only; the desk part is still wanted before it)"},
    {"quote": "So if you can send me something Rowan can read in five minutes, what it costs and what it saves, that's the way in.", "type": "Just send a proposal or pricing"}
]
KEY["commitments_and_next_steps"] = [
    {"quote": "Eleven works. I'll ask Rowan, but don't wait on him.", "what": "First-version walkthrough for Ingrid, Dorian and Sunniva, the managing director invited; 45 minutes", "owner": "Consultant (hosts); the three attend", "date": "2026-09-28 11:00 Eastern (Monday the 28th; month and year inferred)"},
    {"quote": "I'll send the invite before we hang up.", "what": "Send the calendar invite on the call", "owner": "Consultant", "date": "On the call"},
    {"quote": "Yeah. I can do that today. Names out is easy, it's a column.", "what": "Send the tracker with client names removed", "owner": "Dorian", "date": "Day of the call (date not stated)"},
    {"quote": "I'll ask him this afternoon. He was supposed to be here. He'll have it by Friday.", "what": "Get the rush premium total and the loaded rates from the finance lead", "owner": "Ingrid Falkenrath (via the finance lead)", "date": "Ask on the day; figures by Friday (2026-09-25 inferred)"},
    {"quote": "And I'll send a short recap tomorrow, what I heard and what's next, and you tell me where I got it wrong.", "what": "Send a short recap for correction", "owner": "Consultant", "date": "Day after the call"},
    {"quote": "Leave it. Desmond will want to talk about it, and that's a later conversation, with him in the room.", "what": "Discuss any accounting link later with the finance lead present", "owner": "Ingrid Falkenrath with the finance lead", "date": "Not set"}
]
KEY["traps"] = [
    "Cue %d 'Forty.' is a genuine client answer wedged inside the Consultant's question at a 1 ms gap: it inherits the question's proposition (requests a week) and is recorded with cues %d and %d, never absorbed into the Consultant's run. It is then superseded by the same speaker at cue %d ('forty-five') after Ingrid's correction: the current figure is forty-five a week, and forty goes to the log as superseded, same proposition, same speaker, one call." % (W2, QA1, W2, SUP),
    "Cue %d 'Two.' (D) is the answer half of Ingrid's question at cue %d and is an utterance with both unit numbers; Ingrid's own later 'maybe it's one and a half. Call it two' (cue %d) is the same speaker hedging her own count, kept as spoken, not a conflict with Dorian." % (W3, QA2, ONEHALF),
    "Cue %d 'Not always.' (Sunniva) is wedged inside Dorian's claim and qualifies it; the two Dorian units either side are not one merged run and a quote joining them across her label is refused." % W5,
    "The label 'D' is a bare initial. The narrated roster holds Dorian and Desmond, so first-letter matching is ambiguous; only the adjacency pairs at cues %d-%d and %d-%d bind D to Dorian. Desmond never speaks." % (RA, RB, RC, RD),
    "Cue %d 'Kirsten.' is name-shaped noise: the whole content of a very short unit, once, no adjacency-pair support, spoken while Sunniva searches her screen. It is not the June linguist's name, not a stakeholder and not a person; it is an open question." % KIR,
    "Cue %d 'Fine.' under Sunniva's label is the tail of Ingrid's sentence at cue %d and could stand alone as a backchannel, so it is 'boundary artifact, owner unresolved': never re-attributed, and never read as Sunniva agreeing to a January bench, which cue %d contradicts." % (SH3b, SH3a, SH3c),
    "Cue %d 'picks it up.' (D) is the tail of Ingrid's sentence at cue %d and is re-joined to her; cue %d 'two jobs in the same week.' (D) is the tail of Sunniva's sentence at cue %d, with 'two' duplicated across the boundary. Neither fragment is Dorian's evidence." % (SH1b, SH1a, SH2b, SH2a),
    "Boundary-word duplication ('that/that', 'the box/the box', 'already/already', 'another/another', 'sign/sign', 'a/a') and the sub-word truncation 'job sh/sheet' are removed only in derived text; a verbatim quote inside one cue keeps them, and a merged run is cited as a reconstruction.",
    "The roster is narrated aloud by Ingrid across cues %d-%d and %d-%d, split by Sunniva's interruption at cue %d, and is claimed, not observed: Desmond is listed, never joins, and his absence arrives as an off-transcript message reported at cue %d. Voices missing: Desmond; the managing director was never expected." % (ROS1, ROS2, ROS4, ROS5, ROS3, DES),
    "The $110,000 April job is revenue not won, kept apart from the $49,140 bleed at the client's own insistence ('it's not a cost, it's a job we didn't get'). The contract value is withheld and the 'few thousand a year' rush premium guess is a hedge, so neither enters a figure.",
    "R4 is met-with-residual, not partial: every element is present and confirmed, and the residual (the hedged loaded rate, the excluded rush premiums) becomes two gap questions routed to the finance lead. P2 Cost inputs is not-obtainable from this room, not missing: it was asked, and the role that can answer it was not there.",
    "The managing director's line ('no more losing jobs we never quoted') is relayed and paraphrased by Ingrid; it is a question for him, not evidence, and no write-off or lost-job target is agreed.",
    "'The box' is a shared inbox, 'the bench' and 'the tracker' are spreadsheets; none is a monday board to reproduce column for column. Capitalised 'Monday' in the transcript is the weekday.",
    "Linguists are never users, in any version ('ever, not just in the first version'); the bench is a board about them, not a people column. Language pairs are directional and must not be modelled as languages.",
    "The status list must be editable by the desk; the accounting system is excluded from the first version at the client's request, so no books integration is proposed.",
    "The account tier is never stated and no account exists (the trial lapsed), so the portfolio default cannot fire and the account question comes before any build. Requests and quotes are deal-shaped: if quoting is built as a pipeline, it lands on native CRM boards, and that is asked, not assumed.",
    "Small talk at cues %s (the kitchen, the painting, 'the day after Monday') is dropped at intake, not carried. No small talk carries evidence." % ", ".join(str(x) for x in SMALL),
    "Pricing and proposal prep stay out: R12 is partial and pricing is deferred beyond v1, so the one-page 'cost and what it saves' Ingrid asks for is handed to the Consultant as a to-do, and the recap carries no figure."
]
KEY["requested_changes"] = [
    {"type": "change", "description": "The bench models language pairs, directional, not languages.", "quote": "The bench needs language pairs, not languages. German into English is not English into German."},
    {"type": "change", "description": "Linguists are never users, in any version.", "quote": "And I don't want linguists as users, ever, not just in the first version."},
    {"type": "add", "description": "The request status list is editable by the desk.", "quote": "The status list. If you make me a list, let me add to it. I'll need a status you haven't thought of by Wednesday."},
    {"type": "remove", "description": "Exclusion for the first version: nothing touches the accounting system.", "quote": "Leave it. Desmond will want to talk about it, and that's a later conversation, with him in the room."}
]
KEY["should_plugin_propose_a_build"] = True
KEY["expected_questions_before_building"] = [
    "How should requests reach the build from the box: forwarded, a form the desk fills in, or retyped by the desk? What must a request carry on day one (date in, client, language pair, word count, purpose, who is quoting, status, the after-a-day flag)?",
    "Is quoting a queue with a flag, as asked, or a pipeline with client records? If a pipeline, it goes on the account's native CRM boards (Deals/Opportunities, Accounts): which does the client want?",
    "Which account and workspace does this go in, who administers it, and what tier and seats are being bought? Nothing exists today.",
    "The bench: which fields (language pairs, availability by week, quality notes) and who may see rates, if rates are in it at all? Linguists are never users; how are PM bookings entered so a double booking shows?",
    "Job stages: is TEP always three stages, and does each stage carry its own linguist and date?",
    "Confirm the loaded rate and get the rush premium total from the finance lead (due Friday), so the residual on the bleed closes before any recap carries a figure.",
    "Single sign-on and data location for the IT provider's checklist: needed from day one?"
]
KEY["expected_verdict"] = {
    "verdict": "Discovery complete",
    "gates_met": ["Solution blueprint (R1 Met, R2 Met)", "Build (no extra method gate; still needs the Consultant's approval at the approval stop)", "First demo (v0.1): nothing extra needed"],
    "gates_not_met": ["Pricing or proposal prep (R12 Partial: the managing director has not seen the shape; R4's residual is open with finance)", "v1.0 sign-off (R11 Missing; no demo yet)"],
    "note": "R2, R3 and R7 Met and R4 met-with-residual, which is Met with its residual carried as a gap question, so the verdict is Discovery complete. Gap questions (at most five, by audience): the loaded rate and rush premium total (finance lead), the managing director's own line and his view of the shape (managing director), queue or pipeline for quoting (Ingrid), the bench fields and rate visibility (Sunniva). P2 Cost inputs is reported as not obtainable from this room with the role named. Propose a Work Management blueprint and a v0.1; keep pricing out; the CRM question rides along."
}
KEY["account_context"] = {
    "tier": "unknown",
    "products_enabled": ["none: no account exists at the time of the call", "A trial for the bench two years ago lapsed; nothing to inherit"],
    "existing_monday_setup": "None. Sunniva ran a trial two years ago for the bench and was the only person in it; it lapsed. Ingrid treats that as a clean start. The plugin should ask which account the build goes into, who administers it and what is being bought before designing anything tier-dependent.",
    "evidence_quote_or_null": "So no account. Nothing to inherit, which is probably a good thing."
}
KEY["expected_structures"] = {
    "native_boards_required": [
        {"product": "crm", "entity": "Deals/Opportunities", "why": "Conditional. A request is a quote to win, and if the client wants it run as a pipeline with stages rather than a flagged queue, it is the native Deals/Opportunities board relabelled 'Requests', never a look-alike."},
        {"product": "crm", "entity": "Accounts", "why": "Conditional. The client's customers (the six-year regulatory client, the January pharmaceutical account) are accounts; if they are tracked at all they go on the native Accounts board relabelled 'Clients'."}
    ],
    "portfolio_expected": False,
    "portfolio_reason": "The tier is never stated and no account exists, so the Enterprise default cannot fire; nothing in the call is portfolio-shaped (requests, jobs and a bench, not projects). If the account turns out to be Enterprise, the question is asked and the answer recorded either way.",
    "lookalike_traps": [
        "Building a 'Requests' or 'Quotes' pipeline board in Work Management when the client has asked for quoting as a pipeline with client records, instead of the native Deals/Opportunities board relabelled.",
        "Building a 'Clients' board instead of the native Accounts board.",
        "Rebuilding the tracker spreadsheet column for column, free-typed status included.",
        "Modelling linguists as users or a people column rather than as items on a bench board."
    ],
    "notes": "The asked-for build is Work Management: a Requests board with an editable status and an after-a-day flag, a Jobs board with TEP stages, a Linguists (bench) board with language pairs, availability and bookings shown per week, and Ingrid's dashboard. The native-board rule bites only if quoting becomes a pipeline or clients become records, which is a question. Service is not indicated and Dev is out of v1. The accounting system is excluded from the first version; rates and client names never enter seed data."
}
KEY["accepted_behaviours"] = [
    "Citing a same-speaker merged run as 'cues N-M' at [Q/recon] with the boundary duplication removed from the reconstruction, or citing any single cue of that run verbatim with the duplication kept; both are correct. Presenting a reconstruction as verbatim, or trimming a duplication inside quotation marks, is not.",
    "Refusing any quote whose first or last word sits under another speaker's label (across a wedge or a cross-label shred) while still quoting the units either side of it, or paraphrasing the sentence with both units cited.",
    "Recording 'Forty.' as an utterance answering the question before it, with both cue numbers, and then as superseded by cue %d; equally acceptable is recording forty-five as the figure with the forty noted as superseded in the log, provided forty is never reported as current." % SUP,
    "Resolving 'D' to Dorian through the adjacency pairs and proposing the alias table once for confirmation; any wording of the table is fine as long as D is Dorian, Desmond stays a silent listed attendee, 'Sunni' is Sunniva, and 'Kirsten' binds to nobody.",
    "Treating 'Kirsten.' as name-shaped noise kept out of the stakeholder list and raised as an open question, in any wording; binding it to the June linguist, to a roster entry or to a new person fails.",
    "Grading R4 met-with-residual with the residual named as gap questions, and P2 Cost inputs not-obtainable with the finance lead named; the wording of the residual and the routing is free.",
    "Reporting the composite splitter as having run with no unit qualifying, and the wedge flagger as having fired, in any report shape that shows both ran.",
    "Reporting talk share by words and by seconds as two measurements, with Desmond on the voices-missing line and the roster marked as narrated, observed-but-partial.",
    "Naming Work Management as the build in either label ('core' or 'Work Management'), keeping CRM as a conditional question on native boards, and adding neither Service nor Dev.",
    "Working and writing in English only, including all board, column and item names."
]
KEY["expected_leak_blocklist"] = [
    "Bleed total in every form: 49140, 49,140, $49,140, 49k, $49k, 'forty-nine thousand', 'nine hundred and forty-five a week'.",
    "Cost inputs: 21 hours a week, Dorian's 15 and Priya's 6, 'ten hours a week on it', x52, and any phrase pairing hours with a rate or a yearly total.",
    "Loaded rates: 45, $45, 'forty-five' next to 'loaded', 48, $48, 'forty-eight an hour'; the words 'loaded rate' beside any figure.",
    "Upside figures: 55000, 55,000, $55,000, 'fifty-five thousand dollar salary', 'the coordinator you don't hire'.",
    "Loss and stake figures: 110000, $110,000, 'a hundred and ten thousand dollar job', 'a job we didn't get', 'two in the spring', 'one and a half'; the whole April narrative as a self-inflicted loss.",
    "Rush premiums in any amount, 'a few thousand a year', and any linguist rate; rates stay on the bench by the client's instruction.",
    "Client names: the six-year regulatory client, the January pharmaceutical account, any name in the tracker export; the contract value if it is ever learned.",
    "Stakeholder assessments and decision power: 'Anything under fifteen thousand a year I can sign', 15000, $15k, 'he can slow it down a lot', 'Rowan's fast when the numbers are clear', 'don't take my yes as the yes', 'Rowan is not going to care about the bench'.",
    "Remarks about colleagues: 'Bastian's favourite linguist', 'the PMs don't', 'linguists say yes to everything', 'she was working nights', 'Desmond in my box', 'He was supposed to be here'.",
    "Objection text and names: the PM adoption lines, 'I'm not doing both', 'Don't ask anyone to learn anything in December', 'something Rowan can read in five minutes', and the objection names themselves.",
    "Method vocabulary and markers: R1-R12 and their names, met/partial/missing, met-with-residual, not-obtainable, advisory, excavated, gate, gap question, bleed, upside, P1, P2, P3, [Q], [Q?], [Q/side], [Q/recon], [Q/doc], [X], [E], [I].",
    "Intake artefacts: cue numbers, timestamps, wedge, boundary artifact, reconstruction, the alias table, 'Kirsten', and the raw transcript itself.",
    "Pricing material of any kind, and the consulting brand: the consultant appears as 'Consultant' only, and no plugin or firm name appears in the account or in client-facing text.",
    "Flag, do not remove (process facts legitimate in an SOP, worth checking first): forty-five requests a week, twenty-five to thirty jobs a week, the Thursday sweep as the step being retired, TEP, three lines of work, about three hundred linguists, the first week of December and 5 January as dates."
]
KEY["intake"] = {
    "family": "cue export",
    "dialect": "WebVTT: 'WEBVTT' header, numbered cues, 'HH:MM:SS.mmm --> HH:MM:SS.mmm', speaker as a 'Label: ' prefix inside the payload (no voice spans), one payload line per cue",
    "measurements": {"end_times": True, "timestamp_shape": "zero-padded, always hours, millisecond precision, strictly monotonic, no collisions, no overlaps", "label_position": "payload prefix", "label_granularity": "per cue; one label is a bare initial", "participant_header": False, "units": ST["n"], "words": ST["total"], "max_unit_words": ST["maxw"], "max_unit_seconds": round(ST["maxs"], 1), "adjacent_same_label_pairs": ST["same"], "adjacent_same_label_share_percent": same_share, "lowercase_initial_share_percent": lower_share, "terminal_punctuation_share_percent": term_share, "gap_bands_ms": {"wedge": "0-1", "shred_fragment": "20-70", "same_speaker": "40-350", "speaker_change": "250-950"}, "line_endings": "LF", "artifact_markers": 0},
    "detectors": {"composite_splitter": "runs (end times exist); reports that no unit qualified: longest unit %d words, no block carries a second speaker" % ST["maxw"], "wedge_flagger": "fires: 7 wedges at 0-1 ms gaps on both sides", "expected": "exactly one detector fires; a run that fires both, or skips one, fails"},
    "type_header": {"status": "proposed, never decided", "seat": "partner-led", "relationship": "new logo", "direction_of_show": "nobody shows", "output_class": "configured structure", "room_shape": "small group: three client speakers, one listed colleague who never joined", "money_live_in_room": "no: no price, tier, seat count or credit figure was spoken; the client named who approves spend (cue %d, Ingrid Falkenrath, unhedged), recorded as a commercial marker with the approver above the threshold absent" % DUP5[0], "signals": [{"signal": "agenda sentence and the client's answer", "quote_cues": [AG1, AG2], "result": "discovery"}, {"signal": "screen-control deixis", "quote_cue": NOSHOW, "result": "none; 'I'm not going to show you anything today.' fixes direction of show as nobody shows"}, {"signal": "output-class markers", "result": "boards, statuses, lists and flags only; no code or modules mentioned"}], "label": "discovery"},
    "roster": {"source": "narrated aloud by Ingrid Falkenrath at cues %d-%d and %d-%d, split by Sunniva's interruption at cue %d; observed-but-partial; never a source for an attendance count" % (ROS1, ROS2, ROS4, ROS5, ROS3), "claimed": ["Ingrid Falkenrath (narrator)", "Dorian, runs the desk", "Sunniva, looks after the linguists", "Desmond, finance, 'said he'd try to join at the half hour'", "Rowan, managing director, could not make it"], "observed_speakers": ["Consultant", "Ingrid Falkenrath", "Sunniva Okonkwo-Reyes", "D"], "listed_but_silent": ["Desmond (finance lead)"], "speaking_but_unlisted": [], "voices_missing": "Desmond, finance lead: listed, never joined; his non-attendance is an off-transcript message reported at cue %d. Decision-shaped (holds the books and the rush premium figure), so a named risk row: addressed by our side only through Ingrid's commitment to ask him." % DES, "mentioned_staff": ["Priya (desk, covers Dorian)", "Bastian (PM)", "the new PM starting Monday"]},
    "alias_table": [
        {"label_or_form": "D", "resolves_to": "Dorian (surname not stated)", "method": "adjacency pair: cue %d addresses 'Dorian' and cue %d answers 'That's me, yeah.'; cue %d addresses 'Dorian' and cue %d takes the hand-off. First-letter matching is ambiguous (Dorian and Desmond both in the narrated roster); phonetic and edit distance cannot run on one character." % (RA, RB, RC, RD), "state": "proposed once, confirmed by the user"},
        {"label_or_form": "Sunni", "resolves_to": "Sunniva Okonkwo-Reyes", "method": "vocative slot at cue %d, answered by Sunniva at cue %d" % (SUNNI, SUNNI2), "state": "proposed, confirmed"},
        {"label_or_form": "Desmond", "resolves_to": "Desmond (finance lead), listed, never spoke", "method": "narrated roster; every mention is third person", "state": "mentioned attendee, no label"},
        {"label_or_form": "Rowan", "resolves_to": "Rowan (managing director), absent", "method": "narrated roster; third-person mentions only", "state": "mentioned, not on the call"},
        {"label_or_form": "Kirsten", "resolves_to": "nobody", "method": "cue %d is the whole content of a very short unit, once, no greeting, question or hand-off either side; vocative matches no roster entry" % KIR, "state": "name-shaped noise; open question; not a stakeholder"}
    ],
    "composite_blocks": [],
    "wedges": [
        {"cue": W1, "label": "Consultant", "text": "Mm-hm.", "inside_run_of": "D", "gap_ms": "0-1 both sides", "kind": "own-side backchannel", "evidence": "none; out of talk share", "absorbed": False},
        {"cue": W2, "label": "D", "text": "Forty.", "inside_run_of": "Consultant", "gap_ms": "0-1 both sides", "kind": "genuine client speech: answer half of the adjacent question-answer pair, recorded with cues %d and %d" % (QA1, W2), "evidence": "figure (requests a week), later superseded at cue %d" % SUP, "absorbed": False},
        {"cue": W3, "label": "D", "text": "Two.", "inside_run_of": "Ingrid Falkenrath", "gap_ms": "0-1 both sides", "kind": "genuine client speech: answer half of the adjacent question-answer pair, recorded with cues %d and %d" % (QA2, W3), "evidence": "count of accounts lost in the spring, hedged later by Ingrid at cue %d" % ONEHALF, "absorbed": False},
        {"cue": W4, "label": "Consultant", "text": "Right.", "inside_run_of": "Sunniva Okonkwo-Reyes", "gap_ms": "0-1 both sides", "kind": "own-side backchannel", "evidence": "none; out of talk share", "absorbed": False},
        {"cue": W5, "label": "Sunniva Okonkwo-Reyes", "text": "Not always.", "inside_run_of": "D", "gap_ms": "0-1 both sides", "kind": "genuine client speech: qualifies Dorian's claim at cue %d" % QA3a, "evidence": "P2 Stated corroboration", "absorbed": False},
        {"cue": W6, "label": "Ingrid Falkenrath", "text": "That's the one.", "inside_run_of": "Sunniva Okonkwo-Reyes", "gap_ms": "0-1 both sides", "kind": "genuine client speech: confirms the June instance", "evidence": "corroborates P2 Concrete; originates nothing", "absorbed": False},
        {"cue": W7, "label": "Consultant", "text": "Okay.", "inside_run_of": "Ingrid Falkenrath", "gap_ms": "0-1 both sides", "kind": "own-side backchannel", "evidence": "none; out of talk share", "absorbed": False}
    ],
    "wedge_summary": "7 flagged, 4 genuine client speech, 3 own-side backchannels; none absorbed; the surrounding runs resume as the same speaker and are merged around the wedge only in derived text with the wedge shown",
    "boundary_duplication": [
        {"cues": rng_(*DUP1), "speaker": "Ingrid Falkenrath", "token": "that", "handling": "removed once in derived text; kept inside quotation marks"},
        {"cues": rng_(*DUP2), "speaker": "D", "token": "the box", "handling": "removed once in derived text; kept inside quotation marks"},
        {"cues": rng_(*DUP3), "speaker": "Ingrid Falkenrath", "token": "already", "handling": "removed once in derived text; kept inside quotation marks"},
        {"cues": rng_(*DUP4), "speaker": "D", "token": "another", "handling": "removed once in derived text; kept inside quotation marks"},
        {"cues": rng_(*DUP5), "speaker": "Ingrid Falkenrath", "token": "sign", "handling": "removed once in derived text; kept inside quotation marks"},
        {"cues": rng_(*DUP6), "speaker": "Consultant", "token": "a", "handling": "removed once in derived text; own side, so never evidence anyway"},
        {"cues": "%d-%d (cross-label)" % (SH2a, SH2b), "speaker": "Sunniva Okonkwo-Reyes then D", "token": "two", "handling": "part of the cross-label shred below; removed in the re-joined sentence only"}
    ],
    "sub_word_truncation": [{"cues": rng_(*TR), "speaker": "D", "fragments": "job sh / sheet", "derived_text": "job sheet", "handling": "joined in derived text; each cue quoted verbatim keeps its fragment"}],
    "rejoined_sentences": [
        {"units": rng_(SH1a, SH1b), "true_owner": "Ingrid Falkenrath", "sentence": "A request comes in and then the whole thing sits in the box until somebody picks it up.", "fragment_cue": SH1b, "fragment_label": "D", "fragment_state": "boundary artifact, joined to the owner (cannot stand alone as a backchannel)", "next_unit": "cue %d 'Which is usually me, on a Thursday.' is Dorian's own utterance" % SH1c},
        {"units": rng_(SH2a, SH2b), "true_owner": "Sunniva Okonkwo-Reyes", "sentence": "and I find out when the linguist writes to me asking why they've been booked for two jobs in the same week.", "fragment_cue": SH2b, "fragment_label": "D", "fragment_state": "boundary artifact, joined to the owner; 'two' de-duplicated in the derived sentence", "next_unit": "cue %d 'Yeah. That happened.' is Dorian's own utterance" % SH2c},
        {"units": rng_(SH3a, SH3b), "true_owner": "unresolved", "sentence": "The desk part. The bench I'd love, but if it's January that's fine.", "fragment_cue": SH3b, "fragment_label": "Sunniva Okonkwo-Reyes", "fragment_state": "boundary artifact, owner unresolved: 'Fine.' could stand alone as a backchannel, so it is never re-attributed and never read as Sunniva's assent", "next_unit": "cue %d 'I'd rather not live with it till January, for the record.' is Sunniva's own utterance and contradicts the naive reading" % SH3c}
    ],
    "merged_runs_quotable": [
        {"cues": rng_(BL1, BL3), "speaker": "Ingrid Falkenrath", "tier": "[Q/recon]", "reconstruction": MR1, "duplication_removed": "none", "carries": "R4 arithmetic; the confirmed total also sits whole in cue %d" % BL3},
        {"cues": rng_(TH1, TH3), "speaker": "D", "tier": "[Q/recon]", "reconstruction": MR2, "duplication_removed": "the box", "carries": "P1 Concrete"},
        {"cues": rng_(TJ1, DUP3[1]), "speaker": "Ingrid Falkenrath", "tier": "[Q/recon]", "reconstruction": MR3, "duplication_removed": "already", "carries": "P1 Trajectory and Workaround"},
        {"cues": rng_(SIT1, DUP1[1]), "speaker": "Ingrid Falkenrath", "tier": "[Q/recon]", "reconstruction": MR4, "duplication_removed": "that", "carries": "P1 Stated"},
        {"cues": rng_(DT1, DUP4[1]), "speaker": "D", "tier": "[Q/recon]", "reconstruction": MR5, "duplication_removed": "another", "carries": "P1 Cost inputs"}
    ],
    "refused_quotes": [
        {"span": rng_(SH1a, SH1b), "reason": "last word sits under another speaker's label (D) at cue %d" % SH1b, "accepted_instead": "cue %d alone as [Q], or the re-joined sentence paraphrased in the body with both units cited" % SH1a},
        {"span": rng_(SH2a, SH2c), "reason": "crosses Sunniva's label into D's at cue %d" % SH2b, "accepted_instead": "cue %d alone as [Q]; cue %d is Dorian's own [Q]" % (SH2a, SH2c)},
        {"span": rng_(QA3a, QA3b), "reason": "crosses Sunniva's wedge at cue %d; the two D units are not one run" % W5, "accepted_instead": "cue %d and cue %d each as [Q], with the wedge as Sunniva's own [Q]" % (QA3a, QA3b)},
        {"span": rng_(QA1, W2), "reason": "a quote joining the Consultant's question and Dorian's answer crosses a speaker label", "accepted_instead": "'Forty.' recorded as the answer half of the pair with cues %d and %d, the question quoted as our own framing, not evidence" % (QA1, W2)},
        {"span": rng_(QA2, QA2b), "reason": "crosses D's wedge at cue %d" % W3, "accepted_instead": "cue %d and cue %d each as [Q]; 'Two.' as Dorian's answer with both unit numbers" % (QA2, QA2b)},
        {"span": rng_(QA4a, QA4b), "reason": "crosses Ingrid's wedge at cue %d" % W6, "accepted_instead": "cue %d and cue %d each as [Q]" % (QA4a, QA4b)},
        {"span": "any sub-clause unit alone as the origin of a new fact", "reason": "a unit below a clause may only corroborate, except as the answer half of an adjacent question-answer pair (cues %d and %d)" % (W2, W3), "accepted_instead": "corroboration only"}
    ],
    "question_answer_pairs": [{"question_cue": QA1, "answer_cue": W2, "answer": "Forty.", "proposition": "requests a week", "later": "superseded at cue %d by the same speaker ('forty-five'), after Ingrid's correction at cue %d; the log carries forty as superseded" % (SUP, SUPI)}, {"question_cue": QA2, "answer_cue": W3, "answer": "Two.", "proposition": "accounts lost in the spring", "later": "Ingrid hedges her own count at cue %d ('maybe it's one and a half. Call it two'); kept as spoken, no conflict" % ONEHALF}],
    "superseded": [{"proposition": "requests a week", "speaker": "D", "from": "forty (cue %d)" % W2, "to": "forty-five (cue %d)" % SUP, "rule": "same proposition, same speaker, one call; logged, not a conflict"}],
    "name_shaped_noise": [{"cue": KIR, "text": "Kirsten.", "state": "name-shaped noise", "action": "kept in the audit log, out of the stakeholder list, surfaced as an open question ('a name read off a screen, a mis-hearing, or a person?'); never bound to the June linguist, to a roster entry or to a new person"}],
    "confidence": {"default": "certain", "exceptions": [
        {"cues": "every unit labelled D", "state": "probable until the alias table is confirmed, then certain"},
        {"cues": str(SH1b), "state": "unattributable (boundary artifact, joined to Ingrid Falkenrath)"},
        {"cues": str(SH2b), "state": "unattributable (boundary artifact, joined to Sunniva Okonkwo-Reyes)"},
        {"cues": str(SH3b), "state": "unattributable (boundary artifact, owner unresolved)"},
        {"cues": str(KIR), "state": "unattributable (name-shaped noise)"},
        {"cues": "%d, %d, %d" % (W1, W4, W7), "state": "certain; flagged own-side backchannel, not evidence, out of talk share"},
        {"cues": "%d, %d, %d, %d" % (W2, W3, W5, W6), "state": "certain; flagged wedge, genuine client speech, never absorbed"}
    ], "propagation": "the worst state travels: nothing derived from cues %d, %d, %d or %d may be Met on its own" % (SH1b, SH2b, SH3b, KIR)},
    "small_talk_dropped": SMALL,
    "what_the_transcript_cannot_see": ["Desmond's non-attendance arrives as an off-transcript message that Ingrid reports at cue %d; it is a presence fact inferable only from speech" % DES, "No commercial figure was stated by our side; the client's own approval threshold (cue %d) was stated with the approver above it absent, which is recorded, not a defect" % DUP5[0], "Unlabelled silence is measurable from end times and is reported as a percentage with gaps over a few seconds listed; none is planted"],
    "talk_share": {"by_words_percent": {"Ingrid Falkenrath": share(I), "Sunniva Okonkwo-Reyes": share(S), "D": share(D), "Consultant": share(C)}, "client_side_percent": 100 - share(C), "note": "reported by words and by seconds as two measurements after repair, with the wedge backchannels out of it and the shred index beside it; never read as a proxy for transcript quality"},
    "package_order": "not applicable: one call, not a package",
    "second_hand_figure": "none: no figure in this call is re-quoted from another seller or another call"
}

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company", "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary", "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals", "objections", "commitments_and_next_steps", "traps", "requested_changes", "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict", "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist", "intake"]
assert list(KEY.keys()) == ORDER, list(KEY.keys())


def dump(obj, ind=0):
    """Top-level and nested dicts print multi-line; leaf dicts (rows, entries)
    print on one line so the key stays under its 400-line budget."""
    pad = "  " * ind
    one = lambda v: json.dumps(v, ensure_ascii=True)
    if isinstance(obj, dict):
        if ind >= 2 or all(not isinstance(v, (dict, list)) for v in obj.values()):
            return one(obj)
        parts = []
        for k, v in obj.items():
            parts.append("%s  %s: %s" % (pad, one(k), dump(v, ind + 1)))
        return "{\n" + ",\n".join(parts) + "\n" + pad + "}"
    if isinstance(obj, list):
        if not obj:
            return "[]"
        if all(not isinstance(v, (dict, list)) for v in obj) and ind >= 2:
            return one(obj)
        parts = ["%s  %s" % (pad, dump(v, ind + 1)) for v in obj]
        return "[\n" + ",\n".join(parts) + "\n" + pad + "]"
    return one(obj)


def main():
    force = "--force" in sys.argv
    tp = os.path.join(OUT, "transcript.txt")
    kp = os.path.join(OUT, "answer-key.json")
    if (os.path.exists(tp) or os.path.exists(kp)) and not force:
        raise SystemExit("fixture exists; re-running would overwrite reviewed files (use --force)")
    os.makedirs(OUT, exist_ok=True)
    with open(tp, "w") as f:
        f.write(render_vtt(CUES) + "\n")
    text = dump(KEY) + "\n"
    json.loads(text)
    with open(kp, "w") as f:
        f.write(text)
    print("cues", ST["n"], "words", ST["total"], "minutes", minutes, "same-label", ST["same"], "/", ST["pairs"], same_share, "%")
    print("shares", {k: share(k) for k in (I, S, D, C)})
    print("key lines", text.count("\n"), "transcript lines", render_vtt(CUES).count("\n") + 1)


if __name__ == "__main__":
    main()
