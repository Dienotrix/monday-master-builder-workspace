#!/usr/bin/env python3
"""Re-measure the s16 transcript statistics the key and README assert."""
import re, sys, json, datetime
path = sys.argv[1] if len(sys.argv) > 1 else "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s16-shred-cue/transcript.txt"
txt = open(path, encoding="utf-8").read()
blocks = [b for b in txt.split("\n\n") if b.strip() and not b.startswith("WEBVTT")]
cues = []
def ts(s):
    h, m, rest = s.split(":"); return int(h)*3600 + int(m)*60 + float(rest)
for b in blocks:
    lines = b.strip().split("\n")
    n = int(lines[0]); start, end = lines[1].split(" --> ")
    label, text = lines[2].split(": ", 1)
    cues.append(dict(n=n, start=ts(start), end=ts(end), label=label, text=text, start_s=start))
assert [c["n"] for c in cues] == list(range(1, len(cues)+1))
def words(t):
    toks = [w for w in t.split() if not re.fullmatch(r"\[[a-z]+\]", w)]
    return len(toks)
total = sum(words(c["text"]) for c in cues)
by_label = {}
secs = {}
for c in cues:
    by_label[c["label"]] = by_label.get(c["label"], 0) + words(c["text"])
    secs[c["label"]] = secs.get(c["label"], 0) + (c["end"] - c["start"])
client_w = sum(v for k, v in by_label.items() if k != "Consultant")
client_s = sum(v for k, v in secs.items() if k != "Consultant")
same = sum(1 for a, b in zip(cues, cues[1:]) if a["label"] == b["label"])
mx = max(cues, key=lambda c: words(c["text"]))
mxs = max(cues, key=lambda c: c["end"] - c["start"])
lower = sum(1 for c in cues if re.sub(r"\[[a-z]+\]\s*", "", c["text"])[:1].islower())
def strip_br(t): return re.sub(r"\s*\[[a-z]+\]\s*", " ", t).strip()
noterm = sum(1 for c in cues if strip_br(c["text"]) and strip_br(c["text"])[-1] not in ".?!")
short = sum(1 for c in cues if words(c["text"]) <= 4)
span = cues[-1]["end"] - cues[0]["start"]
talk = sum(c["end"] - c["start"] for c in cues)
gaps = [(b["n"], round(b["start"] - a["end"], 3)) for a, b in zip(cues, cues[1:])]
zero = [n for n, g in gaps if abs(g) < 0.0005]
big = [(n, g) for n, g in gaps if g > 3]
own = sum(words(c["text"]) for c in cues if 21 <= c["n"] <= 23)
print(json.dumps(dict(units=len(cues), words=total, by_label=by_label, client_by_words=round(client_w/total, 3),
    client_by_seconds=round(client_s/talk, 3), same_label_pairs=same, same_label_share=round(same/(len(cues)-1), 3),
    longest_words=(mx["n"], words(mx["text"])), longest_seconds=(mxs["n"], round(mxs["end"]-mxs["start"], 1)),
    lowercase_initial=lower, no_terminal_punct=noterm, le4_words=short,
    unlabelled_seconds=round(span - talk + cues[0]["start"], 1), share_unlabelled=round((span - talk + cues[0]["start"]) / (cues[-1]["end"]), 3),
    zero_gap_after=zero, gaps_over_3s=big, own_side_21_23=own, span_min=round(cues[-1]["end"]/60, 1),
    oct8_2026=datetime.date(2026, 10, 8).strftime("%A"), sep8_2026=datetime.date(2026, 9, 8).strftime("%A")), indent=1))
if "--cues" in sys.argv:
    for c in cues:
        if c["label"] == "Consultant": print(c["n"], words(c["text"]), c["text"])
