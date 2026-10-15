"""Render the five s24 transcript files from turns.py.

Read-write: writes fixtures/s24-package/rec-*.txt. Run once; the key
generator and check.py read the rendered files.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import turns  # noqa: E402

OUT = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s24-package"

NAMES = {
    "M": "Clodagh Rennard",
    "K": "Kofi Danquah",
    "D": "Wade Strickler",
    "G": "Gwen Tarrant",
    "T": "Jesse Corrigan",
    "L": "Lupe Arrieta",
}
SELLER = {"M", "K"}

RULE = "═" * 64

FILES = [
    dict(
        stem="rec-4418-discovery",
        title="Discovery - Penhallow Print and Sign",
        rid="rec-4418",
        date="2026-07-14",
        src=turns.DISCOVERY,
        start=6,
        participants="Clodagh Rennard (host); Kofi Danquah; Wade Strickler; Gwen Tarrant; Jesse Corrigan; Notetaker (recording assistant)",
        highlights=[
            "The client estimates reprint costs at $40,000 per year and six to seven reprints per week.",
            "Deadline: fourteen credit union branches by November 30.",
            "Next step: demo on July 23 at 10:00.",
        ],
    ),
    dict(
        stem="rec-4402-first-look",
        title="First look - Penhallow",
        rid="rec-4402",
        date="2026-07-23",
        src=turns.DEMO1,
        start=4,
        participants="Clodagh Rennard (host); Kofi Danquah; Wade Strickler; Gwen Tarrant; Jesse Corrigan; Lupe Arrieta; Notetaker (recording assistant)",
        highlights=[
            "Two options were discussed for tracking production pieces (sub-items or a separate board).",
            "Customer proof approval from email without login was demonstrated.",
            "Follow-up session scheduled for August 6 at 10:00.",
        ],
    ),
    dict(
        stem="rec-4431-internal-review",
        title="Internal - Penhallow debrief",
        rid="rec-4431",
        date="2026-07-23",
        src=turns.REVIEW,
        start=3,
        participants="Clodagh Rennard (host); Kofi Danquah; Notetaker (recording assistant)",
        highlights=[
            "The team agreed to lead with sub-items in the next demo.",
            "Proposal to be priced at $18,500 plus eight seats on the Pro plan.",
            "Open items: the estimating system export, file locking, the approval flow.",
        ],
    ),
    dict(
        stem="rec-4397-production-walkthrough",
        title="Production walkthrough - Penhallow",
        rid="rec-4397",
        date="2026-08-06",
        src=turns.DEMO2,
        start=5,
        participants="Clodagh Rennard (host); Kofi Danquah; Wade Strickler; Gwendolyn Tarrant; Jesse Corrigan; Guadalupe Arrieta; Notetaker (recording assistant)",
        highlights=[
            "Reprint volume clarified as two to three per week.",
            "Install permits, phone access and a late-jobs list were reviewed.",
            "Pricing discussion scheduled for August 19 at 2:00 PM.",
        ],
    ),
    dict(
        stem="rec-4409-pricing",
        title="Pricing - Penhallow",
        rid="rec-4409",
        date="2026-08-19",
        src=turns.PRICING,
        start=4,
        participants="Clodagh Rennard (host); Wade Strickler; Guadalupe Arrieta; Notetaker (recording assistant)",
        highlights=[
            "Annual cost of the current process estimated at $96,500.",
            "Proposal: $18,500 build plus eight Pro seats.",
            "Follow-up on August 27 at 9:00 AM pending owner approval.",
        ],
    ),
]


def parse(src):
    items = []
    for raw in src.strip().split("\n"):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("## "):
            items.append(("TOPIC", line[3:].strip()))
            continue
        code, text = line.split(":", 1)
        items.append((code.strip(), text.strip()))
    return items


def words(text):
    return len(re.findall(r"[A-Za-z0-9'][A-Za-z0-9'\-]*", text))


def mmss(sec):
    return "%02d:%02d" % (sec // 60, sec % 60)


def render(spec):
    items = parse(spec["src"])
    t = spec["start"]
    body = []
    stats = {"turns": 0, "words": {}, "max_turn": (0, None), "topics": 0}
    for kind, text in items:
        if kind == "TOPIC":
            body.append("")
            body.append("── %s ──" % text)
            body.append("")
            stats["topics"] += 1
            t += 2
            continue
        name = NAMES[kind]
        body.append("%s · %s" % (name, mmss(t)))
        body.append(text)
        w = words(text)
        stats["turns"] += 1
        stats["words"][name] = stats["words"].get(name, 0) + w
        if w > stats["max_turn"][0]:
            stats["max_turn"] = (w, name + " " + mmss(t))
        # pacing: about 150 words a minute plus a short gap, a little
        # slower for long turns
        t += int(round(w * 0.48 + 1.6 + (0.6 if w > 60 else 0)))
    duration = t + 5
    head = [
        RULE,
        "Recording       %s" % spec["title"],
        "Recording ID    %s" % spec["rid"],
        "Date            %s" % spec["date"],
        "Duration        %s" % mmss(duration),
        "Host            Clodagh Rennard",
        "Participants    %s" % spec["participants"],
        "Transcript      automatic, en-US; speaker labels from meeting accounts",
    ]
    for i, h in enumerate(spec["highlights"]):
        head.append(("Highlights      - %s" if i == 0 else "                - %s") % h)
    head.append(RULE)
    text = "\n".join(head + body).rstrip("\n") + "\n"
    stats["duration"] = mmss(duration)
    stats["lines"] = text.count("\n")
    return text, stats


def main():
    os.makedirs(OUT, exist_ok=True)
    total_lines = 0
    for spec in FILES:
        text, st = render(spec)
        path = os.path.join(OUT, spec["stem"] + ".txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        total_lines += st["lines"]
        allw = sum(st["words"].values())
        client = sum(v for k, v in st["words"].items() if k not in {NAMES["M"], NAMES["K"]})
        print("%s: %d turns, %d topics, %d words, duration %s, %d lines, client share %.0f%%, longest turn %d words (%s)" % (
            spec["stem"], st["turns"], st["topics"], allw, st["duration"], st["lines"],
            100.0 * client / allw if allw else 0, st["max_turn"][0], st["max_turn"][1]))
        for k, v in sorted(st["words"].items(), key=lambda x: -x[1]):
            print("    %-22s %5d  %4.0f%%" % (k, v, 100.0 * v / allw))
    print("total transcript lines:", total_lines)


if __name__ == "__main__":
    main()
