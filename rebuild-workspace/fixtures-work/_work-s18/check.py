"""Read-only checks for s18-identity-collapse: field order, quote validity, stamp references, alias forms, counts, name collisions."""
import json, re, os, glob, sys
from collections import Counter, OrderedDict

DIR = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s18-identity-collapse/"
FIX = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/"
ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company", "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary", "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals", "objections", "commitments_and_next_steps", "traps", "requested_changes", "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict", "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
k = json.load(open(DIR + "answer-key.json"), object_pairs_hook=OrderedDict)
tx = open(DIR + "transcript.txt").read()
lines = tx.split("\n")
PAT = re.compile(r"^\[(\d\d:\d\d:\d\d)\] ([A-Za-z ]+): (.*)$")
turns = [(m.group(1), m.group(2), m.group(3)) for m in (PAT.match(l) for l in lines) if m]
stamps = {t[0]: t for t in turns}
bad = 0

keys = list(k.keys())
print("field order ok:", keys[:25] == ORDER, "| extra:", keys[25:], "| key lines:", open(DIR + "answer-key.json").read().count("\n"))


def walk(o, path=""):
    out = []
    if isinstance(o, dict):
        for kk, v in o.items():
            if kk in ("quote", "evidence_quote_or_null") and isinstance(v, str):
                out.append((path + "/" + kk, v, o.get("location")))
            else:
                out += walk(v, path + "/" + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            out += walk(v, path + "[%d]" % i)
    return out


qs = walk(k)
with_loc = 0
for p, q, loc in qs:
    hits = [t for t in turns if q in t[2]]
    if len(hits) != 1:
        bad += 1
        print("  BAD QUOTE (%d hits) %s: %r" % (len(hits), p, q[:70]))
        continue
    if loc:
        with_loc += 1
        want = "%s %s" % (hits[0][0], hits[0][1])
        if loc != want:
            bad += 1
            print("  BAD LOCATION %s: %r != %r" % (p, loc, want))
print("quotes checked:", len(qs), "with location:", with_loc, "bad:", bad)

txt = json.dumps(k)
reclen = re.search(r"Recording length: (\d\d:\d\d:\d\d)", tx).group(1)
refs = sorted(set(re.findall(r"\b(\d\d:\d\d:\d\d)\b", txt)) - {reclen})
missing = [r for r in refs if r not in stamps]
print("stamps referenced:", len(refs), "missing:", missing)

# alias-map forms: each plainly listed stamp must contain the form (word boundary, case-sensitive)
I = k["intake"]
formbad = 0
for ent in I["alias_map"]:
    for f in ent["forms"]:
        alts = [a.strip() for a in f["form"].split(" / ")]
        if alts[0] in ("Tadhg Devlin", "Maxine Bassett", "Jon Ashby", "John Rudge", "the owner (refused)", "the family", "Maxine's number two", "the wet John", "the dry John", "Aubrey"):
            continue
        for loc in f["locations"]:
            st = loc.split(" ")[0]
            if st not in stamps:
                continue
            cands = alts + [a.replace("the ", "") for a in alts]
            if not any(re.search(r"(?<![A-Za-z])" + re.escape(a) + r"(?![A-Za-z])", stamps[st][2]) for a in cands):
                formbad += 1
                print("  FORM NOT AT STAMP:", alts, st)
print("alias forms checked; bad:", formbad)

# rubric counts
rub = k["rubric"]
print("rubric rows:", len(rub), dict(Counter(r["status"] for r in rub)))
print("asked:", dict(Counter(r.get("asked") for r in rub)), "asked_quote:", sum(1 for r in rub if "asked_quote" in r))
crit = [r["criterion"] for r in rub]
RN = ["R1 Current state mapped", "R2 Pain made concrete", "R3 Why now", "R4 Bleed number", "R5 Upside number", "R6 Desired outcome", "R7 Decision process mapped", "R8 Priority and timing", "R9 Blockers surfaced", "R10 Next step committed", "R11 Solution confirmed", "R12 Scope agreed verbally"]
print("R names ok:", crit[:12] == RN, "| pain checks ok:", all(c.split(" ", 1)[1] in ("Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory") for c in crit[12:]))
GATES = ["Solution blueprint", "Build", "First demo (v0.1)", "Pricing or proposal prep", "v1.0 sign-off"]
gl = k["expected_verdict"]["gates_met"] + k["expected_verdict"]["gates_not_met"]
print("gates ok:", [sum(1 for g in gl if g.startswith(x)) for x in GATES] == [1] * 5)
graded = sorted(set(c.split()[0] for c in crit if c.startswith("P")))
exc = [p for p in graded if all(next(r["status"] for r in rub if r["criterion"] == p + " " + x) == "met" for x in ("Stated", "Concrete", "Workaround"))]
print("graded pains:", graded, "excavated:", exc, "pains array:", len(k["pains"]))
SPEC = {"Price feels high", "Needs to think it over", "Must check with someone", "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners", "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it"}
ob = Counter(o["type"].split(" (")[0] for o in k["objections"])
print("objections:", len(k["objections"]), dict(ob), "| all named:", all(t in SPEC or t.startswith("Outside the map") for t in ob))
print("traps:", len(k["traps"]), "lookalike:", len(k["expected_structures"]["lookalike_traps"]), "blocklist:", len(k["expected_leak_blocklist"]), "requested:", dict(Counter(r["type"] for r in k["requested_changes"])), "questions:", len(k["expected_questions_before_building"]), "accepted:", len(k["accepted_behaviours"]), "vocab:", len(k["vocabulary"]), "commitments:", len(k["commitments_and_next_steps"]), "entities:", len(k["entities_and_workflows"]), "integrations:", len(k["integrations_mentioned"]), "compliance:", len(k["compliance_or_security_signals"]))
print("decision roles:", [a["decision_role"].split(" (")[0] for a in k["attendees"]])
print("intake keys:", list(I.keys()))

# measurements the key states
wc = Counter()
for st, lab, text in turns:
    wc[lab] += len(text.split())
tot = sum(wc.values())
print("units", len(turns), "words", tot, "client share %.1f" % (100.0 * (tot - wc["Consultant"]) / tot), {l: round(100.0 * w / tot, 1) for l, w in wc.items()})
print("lowercase-initial:", [t[0] for t in turns if t[2][0].islower()], "| short:", sum(1 for t in turns if len(t[2].split()) <= 4), "| same-label pairs:", sum(1 for a, b in zip(turns, turns[1:]) if a[1] == b[1]))
print("John occurrences:", sum(len(re.findall(r"\bJohn\b", t[2])) for t in turns), "| Maxine:", sum(len(re.findall(r"Maxine", t[2])) for t in turns), "| Aubrey:", sum(len(re.findall(r"Aubrey", t[2])) for t in turns))
for w in ("tie", "tag", "tide"):
    print("  %s: %d uses in %d units" % (w, sum(len(re.findall(r"\b%s\b" % w, t[2])) for t in turns), sum(1 for t in turns if re.search(r"\b%s\b" % w, t[2]))))

def strings(o):
    if isinstance(o, dict):
        for v in o.values():
            for s in strings(v):
                yield s
    elif isinstance(o, list):
        for v in o:
            for s in strings(v):
                yield s
    elif isinstance(o, str):
        yield o


# the Consultant never gets a gendered pronoun: any sentence naming the Consultant that also carries he/she/his/him
gp = 0
for s in list(strings(k)) + [t[2] for t in turns]:
    for sent in re.split(r"(?<=[.?!])\s+", s):
        if "Consultant" in sent and re.search(r"\b(he|she|his|him)\b", sent):
            gp += 1
            print("  PRONOUN NEAR CONSULTANT:", sent[:140])
print("gendered pronoun near 'Consultant':", gp)

# tool categories per sentence (heuristic), per string value
CATS = ["spreadsheet", "berthing system", "accounts package", "email", "task app", "tide tables", "calendar", "messaging", "text message", "portal", "monday"]
multi = 0
for src, items in (("transcript", [t[2] for t in turns]), ("key", list(strings(k)))):
    for s in items:
        for sent in re.split(r"(?<=[.?!])\s+", s):
            h = {c for c in CATS if c in sent.lower()}
            if len(h) > 1:
                multi += 1
                print("  MULTI-CATEGORY (%s): %s -> %s" % (src, sent[:110], sorted(h)))
print("multi-category sentences:", multi)

# name collisions against every other fixture folder
names = Counter()
for f in (DIR + "transcript.txt", DIR + "answer-key.json"):
    for m in re.finditer(r"\b[A-Z][a-z]{2,}\b", open(f).read()):
        names[m.group(0)] += 1
OURS = ["Tadhg", "Devlin", "Tige", "Tyge", "Teague", "Tighe", "Thady", "Bernie", "Bernadette", "Locke", "Maxine", "Bassett", "Ashby", "Rudge", "Jonny", "Aubrey", "Threlfall", "Lorcan", "Wojtek", "Biscuit", "Kittiwake", "Brindlehaven"]
coll = {}
for d in sorted(glob.glob(FIX + "s*/")):
    if d.rstrip("/").endswith("s18-identity-collapse"):
        continue
    blob = ""
    for f in glob.glob(d + "*"):
        if os.path.isfile(f):
            try:
                blob += open(f, errors="ignore").read()
            except Exception:
                pass
    for n in OURS:
        if re.search(r"\b" + n + r"\b", blob):
            coll.setdefault(n, []).append(os.path.basename(d.rstrip("/")))
print("name collisions with other fixtures:", coll or "none")
print("RESULT:", "OK" if bad == 0 and not missing and formbad == 0 else "PROBLEMS")
