"""Render fixtures/s20-large-group/transcript.txt from turns1-3 and report measurements.

Authoring scratch, deterministic. Writes the transcript and locations.json (tag -> location, line).
Do not re-run after review edits to the transcript: it overwrites the fixture file.
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from turns1 import TURNS1  # noqa: E402
from turns2 import TURNS2  # noqa: E402
from turns3 import TURNS3  # noqa: E402

OUT_DIR = os.path.join(HERE, "..", "..", "fixtures", "s20-large-group")
TRANSCRIPT = os.path.join(OUT_DIR, "transcript.txt")
LOCATIONS = os.path.join(HERE, "locations.json")

NAMES = {
    "Con": ("Consultant", None, "consultant"),
    "Del": ("Delphine Castellane", "Operations Director", "client"),
    "Bro": ("Bronwyn Tsai", "Finance Controller", "client"),
    "Fer": ("Fergus Lindqvist", "Sales Manager", "client"),
    "Ros": ("Rosalind Achebe", "Production Manager", "client"),
    "Eme": ("Emeric Sandoval", "Design Studio Lead", "client"),
    "Hen": ("Henrike Solano", "Customer Service Lead", "client"),
    "Cal": ("Calum Fairweather", "Install Scheduler", "client"),
    "Yol": ("Yolanda Brekke", "Flint Branch Manager", "client"),
    "Kwa": ("Kwame Oduya", "Account Manager", "client"),
}
SILENT = ["Gideon Ashworth-Pell", "Anton Petrakis", "Saoirse Nakamura", "Lettie Havlicek"]
ROSTER = [
    "Consultant", "Delphine Castellane", "Gideon Ashworth-Pell", "Bronwyn Tsai", "Fergus Lindqvist",
    "Rosalind Achebe", "Emeric Sandoval", "Henrike Solano", "Calum Fairweather", "Yolanda Brekke",
    "Kwame Oduya", "Anton Petrakis", "Saoirse Nakamura", "Lettie Havlicek",
]

rng = random.Random(20261006)


def fmt(t):
    t = int(round(t))
    return "%02d:%02d:%02d" % (t // 3600, (t % 3600) // 60, t % 60)


def parse(ts):
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


turns = TURNS1 + TURNS2 + TURNS3
t = 3.0
rendered = []
locs = {}
header = [
    "Ostlerby Signs - operations discovery",
    "Participants (14): " + ", ".join(ROSTER),
    "",
]
for entry in turns:
    key, text = entry[0], entry[1]
    tag = entry[2] if len(entry) > 2 else None
    pin = entry[3] if len(entry) > 3 else None
    if pin:
        pt = parse(pin)
        if pt < t:
            print("WARNING: pin %s for %s is earlier than natural time %s" % (pin, tag, fmt(t)))
        t = max(t, pt)
    name, role, side = NAMES[key]
    ts = fmt(t)
    line = "[%s] %s: %s" % (ts, name, text)
    rendered.append({"ts": ts, "key": key, "name": name, "role": role, "side": side, "text": text,
                     "words": len(text.split()), "line": len(header) + len(rendered) + 1, "tag": tag})
    if tag:
        loc = "%s %s" % (ts, name) if role is None else "%s %s (%s)" % (ts, name, role)
        locs[tag] = {"location": loc, "line": rendered[-1]["line"], "speaker": name, "text": text}
    # duration: speaking pace plus a pause; the last long turns of the call run a little quicker
    t += rendered[-1]["words"] * 0.43 + rng.uniform(0.8, 2.6)

os.makedirs(OUT_DIR, exist_ok=True)
with open(TRANSCRIPT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(header + [ "[%s] %s: %s" % (r["ts"], r["name"], r["text"]) for r in rendered]) + "\n")
with open(LOCATIONS, "w", encoding="utf-8") as f:
    json.dump(locs, f, indent=1)

# ---- measurements ----
total_words = sum(r["words"] for r in rendered)
by_name = {}
for r in rendered:
    by_name[r["name"]] = by_name.get(r["name"], 0) + r["words"]
client_words = sum(v for k, v in by_name.items() if k != "Consultant")
print("turns:", len(rendered), " lines incl header:", len(header) + len(rendered), " words:", total_words,
      " end:", rendered[-1]["ts"])
print("client share: %.1f%%  consultant: %.1f%%" % (100.0 * client_words / total_words, 100.0 * by_name["Consultant"] / total_words))
for k, v in sorted(by_name.items(), key=lambda kv: -kv[1]):
    print("  %-22s %5d words  %5.1f%% of all  %5.1f%% of client" % (k, v, 100.0 * v / total_words,
          (100.0 * v / client_words) if k != "Consultant" else 0.0))
spoke = set(by_name)
print("spoke:", len(spoke), " silent on roster:", [n for n in ROSTER if n not in spoke])
# longest own-side stretch without a client word (consecutive Consultant turns)
best = (0, None)
run = 0
start = None
for r in rendered:
    if r["name"] == "Consultant":
        if run == 0:
            start = r["ts"]
        run += r["words"]
        if run > best[0]:
            best = (run, start)
    else:
        run = 0
print("longest consultant stretch: %d words from %s" % best)
longest_turn = max(rendered, key=lambda r: r["words"])
print("longest single turn: %s, %d words at %s" % (longest_turn["name"], longest_turn["words"], longest_turn["ts"]))
last_spoke = {}
for r in rendered:
    last_spoke[r["name"]] = r["ts"]
print("last spoke:", last_spoke)
print("non-ascii lines:", sum(1 for r in rendered if any(ord(c) > 127 for c in r["text"])))
print("tags:", len(locs))
