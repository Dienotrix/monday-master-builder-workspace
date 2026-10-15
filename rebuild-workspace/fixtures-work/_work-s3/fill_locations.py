#!/usr/bin/env python3
"""Fill "location": "AUTO" entries in the s3 answer key from the transcript line each quote is on."""
import json
import re

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s3-followup-demo-feedback/"
ROLES = {
    "Tess Kowalczyk": "Tess Kowalczyk (COO)",
    "Jordan Pruitt": "Jordan Pruitt (Operations Manager)",
    "Bev Halvorsen": "Bev Halvorsen (Controller)",
    "Consultant": "Consultant",
}
lines = open(BASE + "transcript.txt", encoding="utf-8").read().splitlines()
k = json.load(open(BASE + "answer-key.json", encoding="utf-8"))
problems = []


def loc_for(q):
    hits = [l for l in lines if q in l]
    if not hits:
        problems.append(("NOT FOUND", q))
        return "NOT FOUND"
    if len(hits) > 1:
        problems.append(("MULTI", q))
    m = re.match(r"^(.+?) \((\d\d:\d\d:\d\d)\): ", hits[0])
    return f"{m.group(2)} {ROLES[m.group(1)]}"


def walk(o):
    if isinstance(o, dict):
        if "quote" in o and o.get("location") == "AUTO":
            o["location"] = loc_for(o["quote"])
        for v in o.values():
            walk(v)
    elif isinstance(o, list):
        for v in o:
            walk(v)


walk(k)
open(BASE + "answer-key.json", "w", encoding="ascii").write(json.dumps(k, indent=2, ensure_ascii=True) + "\n")
for p in problems:
    print(p)
print("filled; problems:", len(problems))
