#!/usr/bin/env python3
"""Truth-to-transcript checks for the s8 answer key, added at review time.

check.py proves every quote is an exact substring sitting in one cue and that the shapes
and locations are right. This script checks the claims the key makes ABOUT the transcript,
which quote-matching cannot catch:

  1. Every vocabulary 'their_term' is a term the client actually says (word-boundary match),
     so the key never puts an abbreviation in their mouths (caught 'ILSM', 'MSA', 'PE').
  2. No gendered pronoun is ever attached to the Consultant (neutrality rule).
  3. The transcript_format claims match the transcript: cue count, first and last timings,
     spoken word count, per-speaker talk share, the longest unbroken Consultant stretch,
     the Speaker 2 cues, the duplicated cue, the overlapping cue pair, and the claim about
     where cue boundaries fall.
  4. The bleed arithmetic in numbers.bleed adds up to the total the client confirms.
"""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo/"
t = open(BASE + "transcript.txt", encoding="utf-8").read()
raw = open(BASE + "answer-key.json", encoding="utf-8").read()
k = json.loads(raw)

fail = []


def bad(msg):
    fail.append(msg)
    print("FAIL:", msg)


# ---------------------------------------------------------------- parse cues
cues = {}
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        start, end = [x.strip() for x in lines[1].split("-->")]
        m = re.match(r"^<v ([^>]+)>(.*)$", " ".join(lines[2:]))
        cues[int(lines[0])] = (start, end, m.group(1), m.group(2).strip())
nums = sorted(cues)


def secs(ts):
    h, m, rest = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(rest)


# ---------------------------------------------------------------- 1. vocabulary terms
print("--- vocabulary their_term said on the call ---")
low = t.lower()
for v in k["vocabulary"]:
    for part in [p.strip() for p in v["their_term"].split("/")]:
        # word-boundary match so 'PE' does not match inside 'open' or 'people'; a trailing
        # plural 's' is allowed because the key lists terms in the singular ('equipment job',
        # 'project engineer') where the call says them in the plural
        if not re.search(r"\b" + re.escape(part.lower()) + r"s?\b", low):
            bad(f"vocabulary their_term not said in the transcript: {part!r}")
print(f"  {len(k['vocabulary'])} terms checked")

# ---------------------------------------------------------------- 2. neutrality
print("--- Consultant neutrality ---")
GENDERED = r"\b(he|him|his|she|her|hers)\b"
for m in re.finditer(r'[^.?!"]*Consultant[^.?!"]*[.?!]', raw):
    s = m.group(0)
    # only flag a pronoun that could attach to the Consultant: no other named person
    # in the same sentence to own it
    if re.search(GENDERED, s, re.I) and not re.search(
            r"Marisol|Warren|Ines|Bridget|Curt|Corinne|Stefan|Roland|Kyle|Dwayne|Lonnie|"
            r"client|approver|director|PM\b|she would|health system", s):
        bad(f"possible gendered pronoun for the Consultant: {s.strip()[:150]}")
for w in ("Consultant himself", "Consultant herself"):
    if w in raw:
        bad(f"gendered Consultant phrasing: {w!r}")
print("  checked")

# ---------------------------------------------------------------- 2b. no invented people
# The key must not give a person a name the transcript never uses. Sibling fixtures name
# offstage people exactly as the call does; s8 had invented six surnames for them.
print("--- person names in the key exist in the transcript ---")
FIRST = ["Marisol", "Warren", "Ines", "Bridget", "Curt", "Corinne", "Stefan", "Roland",
         "Kyle", "Dwayne", "Lonnie", "Junie"]
for m in re.finditer(r"\b(" + "|".join(FIRST) + r")\s+([A-Z][a-z]{2,})\b", raw):
    if m.group(0) not in t:
        bad(f"key invents a person name the transcript never uses: {m.group(0)!r}")
for nm in FIRST:
    if nm not in t:
        bad(f"key-side first name not in the transcript at all: {nm!r}")
print(f"  {len(FIRST)} first names checked for invented surnames")

# ---------------------------------------------------------------- 3. transcript_format claims
print("--- transcript_format claims ---")
fmt = k["transcript_format"]
spoken = sum(len(c[3].split()) for c in cues.values())
share = {}
for _, _, sp, txt in cues.values():
    share[sp] = share.get(sp, 0) + len(txt.split())

if f"{len(cues)} cues" not in fmt:
    bad(f"cue count not stated as {len(cues)}")
if cues[nums[0]][0] not in fmt:
    bad(f"first cue start {cues[nums[0]][0]} not in transcript_format")
if cues[nums[-1]][1] not in fmt:
    bad(f"last cue end {cues[nums[-1]][1]} not in transcript_format")
if nums != list(range(1, len(cues) + 1)):
    bad("cue numbering is not contiguous from 1")

# word count claim, e.g. 'about 6,400 spoken words'
m = re.search(r"about ([\d,]+) spoken words", fmt)
if not m:
    bad("no 'about N spoken words' claim found")
elif abs(int(m.group(1).replace(",", "")) - spoken) > 100:
    bad(f"spoken word claim {m.group(1)} vs actual {spoken}")

client = sum(n for sp, n in share.items() if sp != "Consultant")
claims = [("Client talk share is about (\\d+) percent", client / spoken * 100),
          ("Marisol Bettencourt (\\d+) percent", share["Marisol Bettencourt"] / spoken * 100),
          ("Warren Tibbetts (\\d+) percent", share["Warren Tibbetts"] / spoken * 100),
          ("Ines Kovalenko (\\d+) percent", share["Ines Kovalenko"] / spoken * 100),
          ("Consultant has about (\\d+) percent", share["Consultant"] / spoken * 100)]
for pat, actual in claims:
    m = re.search(pat, fmt)
    if not m:
        bad(f"claim missing from transcript_format: {pat}")
    elif abs(int(m.group(1)) - actual) > 1.0:
        bad(f"{pat} claims {m.group(1)} but actual is {actual:.1f}")
if share.get("Speaker 2", 0) / spoken * 100 >= 1.0:
    bad("Speaker 2 share is not under 1 percent as claimed")

# longest unbroken Consultant stretch
runs, cur = [], []
for i in nums:
    if cues[i][2] == "Consultant":
        cur.append(i)
    else:
        if cur:
            runs.append(cur)
        cur = []
if cur:
    runs.append(cur)
best = max(runs, key=lambda r: sum(len(cues[i][3].split()) for i in r))
words = sum(len(cues[i][3].split()) for i in best)
dur = secs(cues[best[-1]][1]) - secs(cues[best[0]][0])
print(f"  longest Consultant stretch: {words} words, {dur:.0f}s, from {cues[best[0]][0]}")
for piece in (f"{words} words", f"{round(dur)} seconds", cues[best[0]][0]):
    if piece not in fmt:
        bad(f"longest-stretch claim missing or wrong: {piece!r}")
if dur > 90:
    bad("the longest Consultant stretch exceeds the spec's 90-second threshold")

# artefacts
sp2 = [i for i in nums if cues[i][2] == "Speaker 2"]
if sp2 != [147, 149]:
    bad(f"Speaker 2 cues are {sp2}, key claims 147 and 149")
dupes = [i for i in nums if i + 1 in cues and cues[i][3] == cues[i + 1][3]
         and cues[i][2] == cues[i + 1][2]]
if dupes != [183]:
    bad(f"duplicate cue pairs start at {dupes}, key claims 183/184")
overlaps = [i for i in nums if i + 1 in cues and secs(cues[i + 1][0]) < secs(cues[i][1])]
# crosstalk = an overlap between two DIFFERENT speakers; the duplicated 183/184 pair also
# overlaps, but it is the same speaker twice and the key describes it as the duplicate
crosstalk = [i for i in overlaps if cues[i][2] != cues[i + 1][2]]
same_speaker = [i for i in overlaps if i not in crosstalk]
if crosstalk != [89]:
    bad(f"crosstalk (different-speaker) overlaps start at {crosstalk}, key claims 89/90")
if same_speaker != [183]:
    bad(f"same-speaker overlaps start at {same_speaker}, key claims only the duplicate 183/184")

# cue-boundary claim: no cue may end mid-sentence if the key says boundaries are sentence ends
midsent = [i for i in nums if cues[i][3] and cues[i][3][-1] not in '.?!"']
if "every cue boundary falls at a sentence end" in fmt and midsent:
    bad(f"key claims every boundary is a sentence end, but these cues end mid-sentence: {midsent}")
print(f"  cues ending mid-sentence: {len(midsent)}")

# ---------------------------------------------------------------- 4. bleed arithmetic
print("--- bleed arithmetic ---")
total = 14 * 4 * 52 * 95 + 10 * 52 * 72 + (16 * 65 + 4 * 115) * 12 + 2 * 50000
if total != 432080:
    bad(f"recomputed bleed {total} != 432080")
if "$432,080" not in k["numbers"]["bleed"]["value"]:
    bad("bleed value does not state $432,080")
if "432,080" not in raw.replace("$432,080", "432,080"):
    bad("bleed total missing from the key")
print(f"  components sum to ${total:,} and the client confirms "
      f"{k['numbers']['bleed']['quote']!r}")

print("\nRESULT:", "PASS" if not fail else f"{len(fail)} FAILURE(S)")
sys.exit(1 if fail else 0)
