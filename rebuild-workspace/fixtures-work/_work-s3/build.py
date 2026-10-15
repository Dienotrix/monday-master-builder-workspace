#!/usr/bin/env python3
"""Build s3 transcript.txt from draft.txt with turn start timestamps.

Draft line: Speaker|text or Speaker|text|+N (N extra seconds of pause before the turn).
Output line: Speaker (HH:MM:SS): text
"""
import sys

WORK = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/_work-s3/"
OUT = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s3-followup-demo-feedback/transcript.txt"
TARGET_LAST_START = float(sys.argv[1]) if len(sys.argv) > 1 else 1805.0

rows = []
for raw in open(WORK + "draft.txt", encoding="utf-8").read().splitlines():
    if not raw.strip():
        continue
    parts = raw.split("|")
    speaker, text = parts[0], parts[1]
    extra = float(parts[2][1:]) if len(parts) > 2 else 0.0
    rows.append((speaker, text, extra))

# raw durations: speech at about 2.6 words per second plus a short gap
starts = []
t = 0.0
prev_words = 0
for i, (speaker, text, extra) in enumerate(rows):
    if i == 0:
        t = 0.0
    else:
        gap = 1.4 + (0.6 if len(rows[i - 1][1].split()) > 40 else 0.0)
        t += prev_words / 2.6 + gap + extra
    starts.append(t)
    prev_words = len(text.split())

first_offset = 3.0
scale = (TARGET_LAST_START - first_offset) / starts[-1]
out = []
last = -1
for (speaker, text, extra), s in zip(rows, starts):
    sec = int(round(first_offset + s * scale))
    if sec <= last:
        sec = last + 1
    last = sec
    hh, rem = divmod(sec, 3600)
    mm, ss = divmod(rem, 60)
    out.append(f"{speaker} ({hh:02d}:{mm:02d}:{ss:02d}): {text}")

open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
words = sum(len(r[1].split()) for r in rows)
print("turns:", len(rows), "spoken words:", words, "scale:", round(scale, 3))
print(out[0])
print(out[-1])
