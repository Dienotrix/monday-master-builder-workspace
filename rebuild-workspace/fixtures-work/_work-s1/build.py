#!/usr/bin/env python3
"""Assign realistic timestamps to the s1 draft and write transcript.txt."""
import random
import sys

BASE = "<scratch>/scratchpad/rebuild/fixtures"
DRAFT = BASE + "/_work-s1/draft.txt"
OUT = BASE + "/s1-discovery-strong/transcript.txt"

SPEAKERS = {"C": "Consultant", "T": "Tess Kowalczyk", "J": "Jordan Pruitt"}
TARGET_LAST_START = 45 * 60 + 2  # last turn starts around 00:45:02

company = sys.argv[1] if len(sys.argv) > 1 else "{CO}"

random.seed(20260910)
turns = []
for raw in open(DRAFT, encoding="utf-8"):
    raw = raw.rstrip("\n")
    if not raw.strip():
        continue
    key, text = raw.split(": ", 1)
    text = text.replace("{CO}", company)
    turns.append((SPEAKERS[key], text))

# raw timing model
t = 4.0
starts = []
for name, text in turns:
    starts.append(t)
    words = len(text.split())
    secs = words * (60.0 / 162.0) * random.uniform(0.9, 1.1)
    gap = random.uniform(0.6, 2.2)
    if "calculator" in text or "..." in text:
        gap += random.uniform(2.5, 4.5)
    if "[muffled]" in text:
        gap += 7
    t += max(secs, 0.8) + gap

scale = (TARGET_LAST_START - 4.0) / (starts[-1] - 4.0)
lines = []
for (name, text), s in zip(turns, starts):
    ts = int(round(4.0 + (s - 4.0) * scale))
    hh, rem = divmod(ts, 3600)
    mm, ss = divmod(rem, 60)
    lines.append(f"[{hh:02d}:{mm:02d}:{ss:02d}] {name}: {text}")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")

total = sum(len(x.split()) for _, x in turns)
by = {}
for name, text in turns:
    by[name] = by.get(name, 0) + len(text.split())
client = total - by.get("Consultant", 0)
longest = max(len(x.split()) for n, x in turns if n == "Consultant")
print(f"turns={len(turns)} words={total} scale={scale:.3f}")
for k, v in by.items():
    print(f"  {k}: {v} ({v/total:.1%})")
print(f"client share={client/total:.1%}; longest consultant turn={longest} words")
print("last line:", lines[-1][:60])
