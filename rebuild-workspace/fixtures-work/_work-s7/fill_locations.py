#!/usr/bin/env python3
"""Fill every "location": "AUTO" in the s7 key from the cue that contains the sibling quote.

Authoring aid only. check.py re-derives every location independently and fails on any mismatch.
"""
import json
import re

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s7-discovery-service-desk/"
t = open(BASE + "transcript.txt", encoding="utf-8").read()

cues = []
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        num = int(lines[0])
        start = lines[1].split("-->")[0].strip()
        text = " ".join(lines[2:])
        speaker = text.split(":", 1)[0]
        cues.append((num, start, speaker, text))

key = json.load(open(BASE + "answer-key.json", encoding="utf-8"))
filled = problems = 0


def loc_for(q):
    hits = [c for c in cues if q in c[3]]
    if len(hits) != 1:
        return None, hits
    num, start, speaker, _ = hits[0]
    return f"cue {num}, {start}, {speaker}", hits


def walk(o, path):
    global filled, problems
    if isinstance(o, dict):
        if o.get("location") == "AUTO" and isinstance(o.get("quote"), str):
            loc, hits = loc_for(o["quote"])
            if loc is None:
                problems += 1
                print(f"UNRESOLVED ({len(hits)} cue matches) {path}: {o['quote'][:70]!r}")
                if hits:
                    print("    candidates:", [h[0] for h in hits])
            else:
                o["location"] = loc
                filled += 1
        for k, v in o.items():
            walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(key, "")
json.dump(key, open(BASE + "answer-key.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
open(BASE + "answer-key.json", "a", encoding="utf-8").write("\n")
print(f"locations filled: {filled}, unresolved: {problems}")
