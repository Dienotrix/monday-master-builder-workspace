#!/usr/bin/env python3
"""Fill 'location' fields in the s1 answer key from the transcript line each quote sits on."""
import json
import re

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s1-discovery-strong/"
ROLES = {"Tess Kowalczyk": "COO", "Jordan Pruitt": "Operations Manager"}

lines = open(BASE + "transcript.txt", encoding="utf-8").read().splitlines()
key = json.load(open(BASE + "answer-key.json", encoding="utf-8"))
problems = 0


def walk(o, path):
    global problems
    if isinstance(o, dict):
        q = o.get("quote")
        if q is not None:
            hits = [i for i, l in enumerate(lines) if q in l]
            if not hits:
                print("NOT FOUND:", path, repr(q))
                problems += 1
            else:
                if len(hits) > 1:
                    print("MULTI-HIT:", path, repr(q), [h + 1 for h in hits])
                m = re.match(r"\[(\d\d:\d\d:\d\d)\] ([^:]+): ", lines[hits[0]])
                ts, sp = m.groups()
                if "location" in o:
                    o["location"] = f"{ts} {sp}" + (f" ({ROLES[sp]})" if sp in ROLES else "")
        for kk, v in o.items():
            if kk != "quote":
                walk(v, path + "." + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(key, "")
with open(BASE + "answer-key.json", "w", encoding="utf-8") as fh:
    json.dump(key, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print("problems:", problems)
