#!/usr/bin/env python3
"""Writes fixtures/s21-existing-account/transcript.txt from turns.py.

One turn per line: "[HH:MM:SS] Speaker Name: text". Timestamps are turn start
times generated from word counts (about 2.4 words a second plus a short gap),
with a longer pause where the screen share starts and stops.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from turns import TURNS  # noqa: E402

OUT = os.path.join(HERE, "..", "..", "fixtures", "s21-existing-account", "transcript.txt")

NAMES = {
    "C": "Consultant",
    "O": "Henrietta Weyland",
    "B": "Bethan Tull",
    "I": "Idris Machado",
}

PAUSE_AFTER = {
    "Can I share my screen? It's easier if you just see it.": 14.0,
    "Let me stop sharing. Hang on.": 6.0,
    "I can hear you. Hang on, I'm going to move rooms, someone's booked the one I'm in. Give me thirty seconds.": 28.0,
    "Take your time.": 4.0,
}


def stamp(t):
    t = int(round(t))
    return "%02d:%02d:%02d" % (t // 3600, (t % 3600) // 60, t % 60)


def main():
    t = 3.0
    lines = []
    for spk, text in TURNS:
        lines.append("[%s] %s: %s" % (stamp(t), NAMES[spk], text))
        words = len(text.split())
        t += 0.9 + words / 2.4
        t += PAUSE_AFTER.get(text, 0.0)
    with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    total_words = sum(len(x.split()) for _, x in TURNS)
    by = {}
    for spk, text in TURNS:
        by[spk] = by.get(spk, 0) + len(text.split())
    print("turns", len(TURNS), "words", total_words, "end", stamp(t))
    for k, v in by.items():
        print(" ", NAMES[k], v, "%.0f%%" % (100.0 * v / total_words))
    client = sum(v for k, v in by.items() if k != "C")
    print("  client share %.0f%%" % (100.0 * client / total_words))
    longest = max(((len(x.split()), x) for s, x in TURNS if s == "C"))
    print("  longest consultant turn", longest[0], "words")


if __name__ == "__main__":
    main()
