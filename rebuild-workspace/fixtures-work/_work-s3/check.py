#!/usr/bin/env python3
"""Quote, field-set and vocabulary check for the s3 answer key.

Transcript format: 'Name (HH:MM:SS): text'.
Checks: JSON validity; the 25 top-level fields present, in order, nothing extra;
nested shapes; rubric/per-pain names and statuses; every "quote" and the
account_context evidence quote an exact substring of the transcript; every
'single-quoted' fragment inside the four newest fields an exact substring too;
objection types and decision roles drawn from the method spec's vocabulary.
"""
import json
import re
import sys

base = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s3-followup-demo-feedback/"
t = open(base + "transcript.txt", encoding="utf-8").read()
lines = t.splitlines()
raw = open(base + "answer-key.json", encoding="utf-8").read()
fail = []
try:
    k = json.loads(raw)
    print("JSON valid")
except Exception as e:
    print("JSON INVALID", e)
    sys.exit(1)

required = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
            "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
            "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
            "objections", "commitments_and_next_steps", "traps", "requested_changes",
            "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
            "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
missing = [x for x in required if x not in k]
extra = [x for x in k if x not in required]
print("missing keys:", missing)
print("extra keys:", extra)
print("field order exact:", list(k) == required)
if missing or extra or list(k) != required:
    fail.append("top-level field set or order")
print("company keys ok:", set(k["company"]) == {"name", "industry", "size", "locations", "current_tools"})
print("verdict keys ok:", set(k["expected_verdict"]) == {"verdict", "gates_met", "gates_not_met", "note"})
print("scenario id ok:", k["scenario_id"] == "s3-followup-demo-feedback")
print("call_type ok:", k["call_type"] == "follow-up-demo-feedback")
print("build flag true:", k["should_plugin_propose_a_build"] is True)
print("AUTO/NOT FOUND left in key:", '"AUTO"' in raw or "NOT FOUND" in raw)
print("non-ascii in key:", sorted({c for c in raw if ord(c) > 127}))
print("non-ascii in transcript:", sorted({c for c in t if ord(c) > 127}))
ctx = open(base + "context-v0.1.md", encoding="utf-8").read()
print("non-ascii in context:", sorted({c for c in ctx if ord(c) > 127}))

# ---- new fields: shapes -------------------------------------------------
ac = k["account_context"]
ok = list(ac) == ["tier", "products_enabled", "existing_monday_setup", "evidence_quote_or_null"]
print("account_context keys ok:", ok)
if not ok:
    fail.append("account_context keys")
es = k["expected_structures"]
ok = list(es) == ["native_boards_required", "portfolio_expected", "portfolio_reason",
                  "lookalike_traps", "notes"]
print("expected_structures keys ok:", ok)
if not ok:
    fail.append("expected_structures keys")
for b in es["native_boards_required"]:
    if list(b) != ["product", "entity", "why"]:
        print("bad native board entry keys:", b)
        fail.append("native board entry keys")
    if b["product"] not in ("core", "crm", "service", "dev"):
        print("bad native board product:", b["product"])
        fail.append("native board product")
if not isinstance(es["portfolio_expected"], bool):
    print("portfolio_expected not a bool")
    fail.append("portfolio_expected type")
for name in ("accepted_behaviours", "expected_leak_blocklist"):
    v = k[name]
    if not (isinstance(v, list) and v and all(isinstance(x, str) and x.strip() for x in v)):
        print("bad", name)
        fail.append(name)
if not all(isinstance(x, str) and x.strip() for x in es["lookalike_traps"]):
    print("bad lookalike_traps")
    fail.append("lookalike_traps")
print("counts: native_boards_required %d, lookalike_traps %d, accepted_behaviours %d, leak_blocklist %d"
      % (len(es["native_boards_required"]), len(es["lookalike_traps"]),
         len(k["accepted_behaviours"]), len(k["expected_leak_blocklist"])))

# ---- vocabulary from the method spec ------------------------------------
OBJ = ["Price feels high", "Needs to think it over", "Must check with someone",
       "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
       "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it",
       "Outside the map"]
ROLES = ["approver", "influencer", "admin/owner", "end user", "not applicable"]
for o in k["objections"]:
    if not any(o["type"].startswith(x) for x in OBJ):
        print("objection type outside spec vocabulary:", o["type"])
        fail.append("objection type")
for a in k["attendees"]:
    if not any(a["decision_role"].startswith(x) for x in ROLES):
        print("decision_role outside spec vocabulary:", a["name"], a["decision_role"])
        fail.append("decision_role")
print("objection types checked:", len(k["objections"]), "| decision roles checked:", len(k["attendees"]))

# ---- transcript form ----------------------------------------------------
bad_fmt = [i + 1 for i, l in enumerate(lines) if not re.match(r"^[A-Z][A-Za-z ]+ \(\d\d:\d\d:\d\d\): \S", l)]
print("lines not in 'Name (HH:MM:SS): text' form:", bad_fmt)
stamps = [re.match(r"^.+? \((\d\d):(\d\d):(\d\d)\): ", l).groups() for l in lines]
secs = [int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in stamps]
print("timestamps strictly increasing:", all(b > a for a, b in zip(secs, secs[1:])))
speakers = {re.match(r"^(.+?) \(", l).group(1) for l in lines}
print("speakers:", sorted(speakers))

R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
names = [r["criterion"] for r in k["rubric"]]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
print("R1-R12 present in order:", names[:12] == expected_r)
for r in k["rubric"]:
    if r["status"] not in ("met", "partial", "missing"):
        print("bad status", r["criterion"])
        fail.append("rubric status")
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        print("bad per-pain check name:", r["criterion"])
        fail.append("per-pain name")
    if not m and r["criterion"] not in expected_r:
        print("bad criterion name:", r["criterion"])
        fail.append("criterion name")
    if r["status"] == "missing" and r["evidence"]:
        print("missing but has evidence:", r["criterion"])
        fail.append("evidence on missing")
    if r["status"] != "missing" and not r["evidence"]:
        if not r["note"].startswith("Carried forward from s1"):
            print("no evidence and not marked carried forward:", r["criterion"])
            fail.append("unmarked empty evidence")
for side in ("bleed", "upside"):
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        print("bad numbers status", side)
        fail.append("numbers status")
for c in k["requested_changes"]:
    if c["type"] not in ("add", "change", "remove"):
        print("bad change type", c)
        fail.append("change type")

# ---- quotes -------------------------------------------------------------
quotes = []


def walk(o, path):
    if isinstance(o, dict):
        for kk, v in o.items():
            if kk in ("quote", "evidence_quote_or_null"):
                if v is not None:
                    quotes.append((path + "." + kk, v, o.get("location")))
            else:
                walk(v, path + "." + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(k, "")
n = bad = 0
for path, q, loc in quotes:
    if not isinstance(q, str):
        print("QUOTE NOT A STRING:", path, repr(q))
        bad += 1
        continue
    n += 1
    if q not in t:
        bad += 1
        print("NOT FOUND:", path, repr(q))
        continue
    hits = [i for i, l in enumerate(lines) if q in l]
    if not hits:
        print("SPANS LINES:", path, repr(q))
        bad += 1
        continue
    if len(hits) > 1 and not path.endswith("evidence_quote_or_null"):
        print("MULTI-HIT (", len(hits), "):", path, repr(q), [lines[h][:30] for h in hits])
    if loc:
        ts = re.match(r"^(.+?) \((\d\d:\d\d:\d\d)\): ", lines[hits[0]])
        if ts and (ts.group(2) not in loc or ts.group(1) not in loc):
            print("LOC MISMATCH:", path, repr(q), "key:", loc, "actual:", ts.group(2), ts.group(1))
            bad += 1
print(f"quotes checked: {n}, not found or invalid: {bad}")
if bad:
    fail.append("quotes")

# ---- 'single-quoted' fragments inside the four newest fields ------------
# An opening quote follows start, whitespace or an opening bracket; a closing
# quote is not followed by a lowercase letter, so apostrophes inside words
# (job's, don't, that's) are not mistaken for delimiters.
FRAG = re.compile(r"(?:(?<=^)|(?<=[\s(\[]))'(.+?)'(?![a-z])", re.S)


def strings(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values():
            yield from strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from strings(v)


frag_n = frag_bad = 0
for field in ("account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"):
    for s in strings(k[field]):
        for m in FRAG.finditer(s):
            frag = m.group(1)
            frag_n += 1
            if frag not in t:
                frag_bad += 1
                print("FRAGMENT NOT IN TRANSCRIPT:", field, repr(frag))
print(f"quoted fragments in new fields checked: {frag_n}, not found: {frag_bad}")
if frag_bad:
    fail.append("fragments")

print("\nRESULT:", "PASS" if not fail else "FAIL " + "; ".join(sorted(set(fail))))
