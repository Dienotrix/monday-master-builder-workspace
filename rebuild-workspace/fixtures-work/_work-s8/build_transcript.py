#!/usr/bin/env python3
"""Build the s8 WebVTT transcript (<v Speaker> voice tags) from the turn drafts.

Cue rule: a cue is one or more whole sentences from a single turn, except where the
draft carries an explicit '||' marker, which forces a mid-sentence split. That keeps
every single sentence inside exactly one cue, so answer-key quotes never span cues.

Markers in the draft text:
  ||           forced mid-sentence cue split (the earlier cue ends without punctuation)
  [[DUP]]      the transcription repeats this turn's first cue as the next cue
  [[OVERLAP]]  this turn's first cue starts before the previous cue ends (crosstalk)
"""
import re
import sys

WORK = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures-work/_work-s8/"
OUT = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo/transcript.txt"

SPEAKERS = {"Consultant", "Marisol Bettencourt", "Warren Tibbetts", "Ines Kovalenko", "Speaker 2"}
MAX_CUE_WORDS = 32
TARGET_END = 59 * 60 + 44.0  # last cue ends just under the hour

# ---------------------------------------------------------------- read turns
turns = []
for fn in ("draft_a.txt", "draft_b.txt"):
    for ln, line in enumerate(open(WORK + fn, encoding="utf-8"), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ": " not in line:
            sys.exit(f"{fn}:{ln}: no speaker separator: {line[:60]}")
        sp, text = line.split(": ", 1)
        if sp not in SPEAKERS:
            sys.exit(f"{fn}:{ln}: unknown speaker {sp!r}")
        dup = overlap = False
        while True:
            if text.startswith("[[DUP]] "):
                dup, text = True, text[8:]
            elif text.startswith("[[OVERLAP]] "):
                overlap, text = True, text[12:]
            else:
                break
        turns.append({"speaker": sp, "text": text.strip(), "dup": dup, "overlap": overlap})

# ---------------------------------------------------------------- split into cue texts
def split_sentences(chunk):
    """Whole sentences, keeping their punctuation."""
    parts = re.split(r"(?<=[.?!])\s+", chunk.strip())
    return [p.strip() for p in parts if p.strip()]


def cue_texts(text):
    """Cue texts for one turn: groups of whole sentences, honouring || hard breaks."""
    out = []
    for segment in text.split("||"):
        segment = segment.strip()
        if not segment:
            continue
        group, count = [], 0
        for sent in split_sentences(segment):
            n = len(sent.split())
            if group and count + n > MAX_CUE_WORDS:
                out.append(" ".join(group))
                group, count = [sent], n
            else:
                group.append(sent)
                count += n
        if group:
            out.append(" ".join(group))
    return out


# ---------------------------------------------------------------- lay out cues on a timeline
def jitter(i, lo, hi):
    """Deterministic pseudo-random gap, so reruns are identical."""
    return lo + ((i * 7919) % 1000) / 1000.0 * (hi - lo)


cues = []  # (speaker, text, start, end)
t = 2.1
for ti, turn in enumerate(turns):
    texts = cue_texts(turn["text"])
    if not texts:
        continue
    t += jitter(ti, 0.30, 0.95)  # inter-turn gap
    for ci, ct in enumerate(texts):
        words = len(ct.split())
        dur = max(1.45, words * 0.40 + 0.65)
        start = t
        if ci == 0 and turn["overlap"] and cues:
            prev = cues[-1]
            start = prev[2] + (prev[3] - prev[2]) * 0.55
        end = start + dur
        cues.append([turn["speaker"], ct, start, end])
        if ci == 0 and turn["dup"]:
            cues.append([turn["speaker"], ct, start + 0.12, end + 0.12])
        t = max(t, end) + jitter(ti * 13 + ci, 0.12, 0.48)

# scale the whole timeline so the last cue ends at TARGET_END
scale = TARGET_END / cues[-1][3]
for c in cues:
    c[2] *= scale
    c[3] *= scale


def stamp(s):
    h = int(s // 3600)
    m = int((s % 3600) // 60)
    sec = s % 60
    return f"{h:02d}:{m:02d}:{sec:06.3f}"


# ---------------------------------------------------------------- write
lines = ["WEBVTT", ""]
for i, (sp, txt, s, e) in enumerate(cues, 1):
    lines += [str(i), f"{stamp(s)} --> {stamp(e)}", f"<v {sp}>{txt}", ""]
out = "\n".join(lines)
non_ascii = sorted({c for c in out if ord(c) > 127})
if non_ascii:
    sys.exit(f"non-ascii in transcript: {non_ascii}")
open(OUT, "w", encoding="utf-8").write(out)

# cue index for answer-key authoring
with open(WORK + "cues.txt", "w", encoding="utf-8") as fh:
    for i, (sp, txt, s, e) in enumerate(cues, 1):
        fh.write(f"{i}\t{stamp(s)}\t{sp}\t{txt}\n")

# ---------------------------------------------------------------- stats
spoken = sum(len(txt.split()) for _, txt, _, _ in cues)
by_sp = {}
for sp, txt, _, _ in cues:
    by_sp[sp] = by_sp.get(sp, 0) + len(txt.split())
client = sum(v for k, v in by_sp.items() if k != "Consultant")
print(f"cues: {len(cues)}  spoken words: {spoken}  ends: {stamp(cues[-1][3])}")
print(f"client share: {client / spoken * 100:.1f}%")
for k, v in sorted(by_sp.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v} words ({v / spoken * 100:.1f}%)")
longest = max(len(txt.split()) for _, txt, _, _ in cues)
print("longest cue (words):", longest)
# longest consultant stretch without a client turn, in words and seconds
run_w = run_start = 0
best = (0, 0, 0)
for sp, txt, s, e in cues:
    if sp == "Consultant":
        if run_w == 0:
            run_start = s
        run_w += len(txt.split())
        if run_w > best[0]:
            best = (run_w, run_start, e)
    else:
        run_w = 0
print(f"longest Consultant stretch: {best[0]} words, {best[2] - best[1]:.0f}s from {stamp(best[1])}")
