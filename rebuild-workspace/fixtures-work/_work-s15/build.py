"""Render s15-shred-dense/transcript.txt from turns.py and report its measurements.

Authoring scratch. Deterministic (seeded). Writes:
  fixtures/s15-shred-dense/transcript.txt
  fixtures-work/_work-s15/index.tsv          one row per rendered unit
  fixtures-work/_work-s15/locations.json     tag -> rendered unit(s), used by key.py
"""
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from turns import TURNS, SPEAKERS, ROLES  # noqa: E402

OUT_DIR = os.path.join(HERE, "..", "..", "fixtures", "s15-shred-dense")
TRANSCRIPT = os.path.join(OUT_DIR, "transcript.txt")

SHAPE_WEIGHTS = {
    "C": [0.62, 0.20, 0.18],
    "P": [0.55, 0.15, 0.18, 0.12],
    "O": [0.55, 0.15, 0.18, 0.12],
    "D": [0.55, 0.15, 0.18, 0.12],
    "B": [0.55, 0.15, 0.18, 0.12],
}

rng = random.Random(20260915)


def words(text):
    return len(text.split())


def fmt(t):
    t = int(t)
    return "%02d:%02d:%02d" % (t // 3600, (t % 3600) // 60, t % 60)


def pick_label(labelled, prev_label):
    shapes = SPEAKERS[labelled][1]
    weights = SHAPE_WEIGHTS[labelled]
    for _ in range(50):
        lab = rng.choices(shapes, weights)[0]
        if lab != prev_label:
            return lab
    for lab in shapes:  # deterministic fallback
        if lab != prev_label:
            return lab
    raise RuntimeError("no distinct label available")


units = []  # rendered units in order
t = 3.0
prev_label = None
for idx, entry in enumerate(TURNS):
    speaker, text = entry[0], entry[1]
    tag = entry[2] if len(entry) > 2 else None
    frags = text.split("|")
    for k, frag in enumerate(frags):
        frag = frag.strip()
        labelled = speaker
        m = re.match(r"^@([A-Z]) (.*)$", frag)
        if m:
            labelled = m.group(1)
            frag = m.group(2)
        lab = pick_label(labelled, prev_label)
        prev_label = lab
        w = words(frag)
        unit = {
            "id": "T%d.%d" % (idx, k),
            "src": idx,
            "frag": k,
            "nfrags": len(frags),
            "tag": tag,
            "ts": fmt(t),
            "label": lab,
            "labelled": labelled,
            "owner": speaker,
            "text": frag,
            "words": w,
            "line": len(units) + 1,
        }
        units.append(unit)
        t += 0.33 * w + 0.4
        t += 0.1 if k < len(frags) - 1 else rng.uniform(0.2, 1.2)

lines = ["%s %s: %s" % (u["ts"], u["label"], u["text"]) for u in units]
os.makedirs(OUT_DIR, exist_ok=True)
with open(TRANSCRIPT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")

# ---- measurements ----
n = len(units)
total_words = sum(u["words"] for u in units)
short = [u for u in units if u["words"] < 5]
adjacent_same = sum(1 for a, b in zip(units, units[1:]) if a["label"] == b["label"])
ellipses = sum(l.count("...") + l.count("…") for l in lines)
lower_initial = sum(1 for u in units if u["text"][:1].islower())
no_terminal = sum(1 for u in units if u["text"][-1:] not in ".?!\"'")
collide = sum(1 for a, b in zip(units, units[1:]) if a["ts"] == b["ts"])
shapes_used = {}
for u in units:
    shapes_used.setdefault(u["labelled"], set()).add(u["label"])
by_owner = {}
for u in units:
    by_owner[u["owner"]] = by_owner.get(u["owner"], 0) + u["words"]
client_words = sum(v for k, v in by_owner.items() if k != "C")
longest_c = max((u["words"], u["ts"]) for u in units if u["owner"] == "C")
misattributed = [u for u in units if u["labelled"] != u["owner"]]
frag_units = [u for u in units if u["nfrags"] > 1]
non_ascii = [l for l in lines if any(ord(ch) > 127 for ch in l)]

print("units:", n, " lines:", len(lines), " words:", total_words, " duration:", units[-1]["ts"])
print("short (<5 words):", len(short), " share: %.1f%%" % (100.0 * len(short) / n))
print("adjacent same-label pairs:", adjacent_same, " ellipses:", ellipses, " non-ascii lines:", len(non_ascii))
print("lowercase-initial:", lower_initial, " no terminal punct:", no_terminal, " same-second adjacent stamps:", collide)
print("label shapes used:", {k: len(v) for k, v in shapes_used.items()})
print("words by owner:", by_owner, " client share: %.1f%%" % (100.0 * client_words / total_words))
print("longest Consultant unit (words, ts):", longest_c)
print("shred units (from split turns):", len(frag_units), " mis-attributed units:", len(misattributed))
print("tags:", sum(1 for u in units if u["tag"] and u["frag"] == 0))

with open(os.path.join(HERE, "index.tsv"), "w", encoding="utf-8") as f:
    f.write("line\tid\ttag\tts\tlabel\tlabelled\towner\twords\ttext\n")
    for u in units:
        f.write("%d\t%s\t%s\t%s\t%s\t%s\t%s\t%d\t%s\n" % (
            u["line"], u["id"], u["tag"] or "", u["ts"], u["label"], u["labelled"], u["owner"], u["words"], u["text"]))

locs = {}
for u in units:
    if u["tag"]:
        locs.setdefault(u["tag"], []).append(u)
with open(os.path.join(HERE, "locations.json"), "w", encoding="utf-8") as f:
    json.dump({"units": units, "tags": locs}, f, indent=1)
