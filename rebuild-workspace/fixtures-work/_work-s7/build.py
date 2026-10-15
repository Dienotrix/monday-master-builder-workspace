#!/usr/bin/env python3
"""Build the s7 SRT transcript from draft turns, and emit a cue index for key authoring."""
import os
import re

WORK = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_work-s7/"
OUT = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s7-discovery-service-desk/"
os.makedirs(OUT, exist_ok=True)

turns = []
for part in ("turnsA.txt", "turnsB.txt"):
    p = WORK + part
    if not os.path.exists(p):
        continue
    for line in open(p, encoding="utf-8").read().splitlines():
        line = line.strip()
        if not line:
            continue
        turns.append(line)

# split turns into cues on the explicit ||| marker
SPEAKERS = {"Consultant", "Yvette Carnahan", "Tansy Whitlock", "Curtis Vandergrift"}

cues = []  # list of (speaker, text)
for t in turns:
    speaker = t.split(":", 1)[0]
    if speaker not in SPEAKERS:
        raise SystemExit("turn without a known speaker label: " + t[:60])
    pieces = [p.strip() for p in t.split("|||") if p.strip()]
    for j, piece in enumerate(pieces):
        # a turn continued into another cue repeats the speaker label, so every
        # cue's text starts with its speaker
        cues.append((speaker, piece if j == 0 else f"{speaker}: {piece}"))


def words(s):
    head, sep, rest = s.partition(":")
    body = rest if head in SPEAKERS else s
    return len(re.findall(r"[A-Za-z0-9']+", body))


SEC_PER_WORD = 0.42
MIN_DUR = 1.3
clock = 3.0  # first cue starts at 00:00:03
rows = []
for i, (sp, text) in enumerate(cues):
    n = words(text)
    dur = max(MIN_DUR, n * SEC_PER_WORD)
    start = clock
    end = start + dur
    # deterministic, varied gap; longer pauses where the topic turns
    gap = 0.25 + ((i * 37) % 11) * 0.06
    if i and cues[i - 1][0] != sp:
        gap += 0.25
    clock = end + gap
    rows.append((i + 1, start, end, sp, text))


def ts(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


srt = []
for num, start, end, sp, text in rows:
    srt.append(f"{num}\n{ts(start)} --> {ts(end)}\n{text}\n")
open(OUT + "transcript.txt", "w", encoding="utf-8").write("\n".join(srt))

with open(WORK + "index.tsv", "w", encoding="utf-8") as f:
    for num, start, end, sp, text in rows:
        f.write(f"{num}\t{ts(start)}\t{sp}\t{text}\n")

total_words = sum(words(t) for _, t in cues)
client_words = sum(words(t) for sp, t in cues if sp != "Consultant")
print("cues:", len(rows))
print("duration:", ts(rows[-1][2]))
print("spoken words:", total_words)
print("client talk share: %.1f%%" % (100.0 * client_words / total_words))
longest = max(((words(t), i + 1) for i, (sp, t) in enumerate(cues) if sp == "Consultant"))
print("longest Consultant cue: %d words (cue %d)" % longest)
speakers = {}
for sp, t in cues:
    speakers[sp] = speakers.get(sp, 0) + words(t)
for sp, w in sorted(speakers.items(), key=lambda x: -x[1]):
    print("  %-20s %5d words" % (sp, w))
