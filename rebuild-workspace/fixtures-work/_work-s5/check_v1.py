#!/usr/bin/env python3
"""Structure, order and quote check for the s5 answer key (with the four new fields).

Transcript format: '[HH:MM:SS] Speaker Name: text', one turn per line.
"""
import json
import re
import sys

base = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s5-intro-thin/"
t = open(base + "transcript.txt", encoding="utf-8").read()
lines = t.splitlines()
raw = open(base + "answer-key.json", encoding="utf-8").read()
fail = []

try:
    k = json.loads(raw)
    print("JSON valid: True")
except Exception as e:
    print("JSON INVALID", e)
    sys.exit(1)

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]

print("missing fields:", [x for x in ORDER if x not in k])
print("extra fields:", [x for x in k if x not in ORDER])
print("field order exact:", list(k) == ORDER)
if list(k) != ORDER:
    fail.append("field order")

SUB = {
    "company": {"name", "industry", "size", "locations", "current_tools"},
    "expected_verdict": {"verdict", "gates_met", "gates_not_met", "note"},
    "account_context": {"tier", "products_enabled", "existing_monday_setup", "evidence_quote_or_null"},
    "expected_structures": {"native_boards_required", "portfolio_expected", "portfolio_reason",
                            "lookalike_traps", "notes"},
    "numbers": {"bleed", "upside"},
}
for f, want in SUB.items():
    ok = set(k[f]) == want
    print(f"{f} sub-keys ok:", ok, "" if ok else (set(k[f]) ^ want))
    if not ok:
        fail.append(f + " sub-keys")

# account_context / expected_structures order within the object
print("account_context order ok:", list(k["account_context"]) ==
      ["tier", "products_enabled", "existing_monday_setup", "evidence_quote_or_null"])
print("expected_structures order ok:", list(k["expected_structures"]) ==
      ["native_boards_required", "portfolio_expected", "portfolio_reason", "lookalike_traps", "notes"])

print("scenario id ok:", k["scenario_id"] == "s5-intro-thin")
print("call_type ok:", k["call_type"] in ("discovery", "follow-up-demo-feedback", "intro", "support-checkin"))
print("build flag False:", k["should_plugin_propose_a_build"] is False)
print("portfolio_expected False:", k["expected_structures"]["portfolio_expected"] is False)
print("native_boards_required empty:", k["expected_structures"]["native_boards_required"] == [])
print("non-ascii in key:", sorted({c for c in raw if ord(c) > 127}))
print("non-ascii in transcript:", sorted({c for c in t if ord(c) > 127}))

for f in ("accepted_behaviours", "expected_leak_blocklist", "traps", "entities_and_workflows",
          "integrations_mentioned", "compliance_or_security_signals", "expected_questions_before_building"):
    bad = [x for x in k[f] if not isinstance(x, str) or not x.strip()]
    print(f"{f}: {len(k[f])} items, all non-empty strings:", not bad)
    if bad or not k[f]:
        fail.append(f)
for f in ("lookalike_traps", "products_enabled"):
    src = k["expected_structures"] if f == "lookalike_traps" else k["account_context"]
    print(f"{f}: {len(src[f])} items, all strings:", all(isinstance(x, str) and x.strip() for x in src[f]))

# --- rubric -----------------------------------------------------------------
R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
names = [r["criterion"] for r in k["rubric"]]
print("R1-R12 present in order:", names[:12] == expected_r)
for r in k["rubric"]:
    if set(r) != {"criterion", "status", "evidence", "note"}:
        print("bad rubric row keys:", r["criterion"], set(r))
        fail.append("rubric keys")
    if r["status"] not in ("met", "partial", "missing"):
        print("bad status:", r["criterion"], r["status"])
        fail.append("rubric status")
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        print("bad per-pain check name:", r["criterion"])
        fail.append("per-pain name")
    if not m and r["criterion"] not in expected_r:
        print("bad criterion name:", r["criterion"])
        fail.append("criterion name")
    if r["status"] != "missing" and not r["evidence"]:
        print("no evidence but not missing:", r["criterion"])
        fail.append("evidence")
for side in ("bleed", "upside"):
    if set(k["numbers"][side]) != {"value", "quote", "status"}:
        print("bad numbers keys:", side)
        fail.append("numbers keys")
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        print("bad numbers status:", side)
        fail.append("numbers status")

# --- vocabulary from the method spec ---------------------------------------
SPEC_OBJECTIONS = {"Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
                   "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it"}
for o in k["objections"]:
    if set(o) != {"quote", "type"}:
        print("bad objection keys:", set(o))
        fail.append("objection keys")
    ty = o["type"]
    if ty not in SPEC_OBJECTIONS and not ty.startswith("Outside the map: "):
        print("objection type not in spec vocabulary:", repr(ty))
        fail.append("objection type")
print("objection types:", sorted({o["type"] for o in k["objections"]}))
print("objections outside the map:", sum(1 for o in k["objections"] if o["type"].startswith("Outside the map")))

SPEC_ROLES = {"approver", "influencer", "admin/owner", "end user", "unknown", "not applicable"}
for a in k["attendees"]:
    if set(a) != {"name", "role", "side", "decision_role"}:
        print("bad attendee keys:", set(a))
        fail.append("attendee keys")
    if a["decision_role"] not in SPEC_ROLES:
        print("decision_role not in spec vocabulary:", repr(a["decision_role"]))
        fail.append("decision_role")
    if a["side"] not in ("client", "consultant"):
        print("bad side:", a["side"])
print("decision roles:", [a["decision_role"] for a in k["attendees"]])

for c in k["requested_changes"]:
    if c["type"] not in ("add", "change", "remove"):
        print("bad change type:", c)
        fail.append("change type")
for p in k["expected_monday_products"]:
    if set(p) != {"kind", "why"} or p["kind"] not in ("core", "crm", "service", "software"):
        print("bad product row:", p)
        fail.append("product row")
print("products:", [p["kind"] for p in k["expected_monday_products"]])

# --- quotes -----------------------------------------------------------------
quotes = []


def walk(o, path):
    if isinstance(o, dict):
        for kk, v in o.items():
            if kk == "quote":
                quotes.append((path + ".quote", v, o.get("location")))
            else:
                walk(v, path + "." + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(k, "")
quotes.append(("account_context.evidence_quote_or_null",
               k["account_context"]["evidence_quote_or_null"], None))

n = bad = nulls = 0
for path, q, loc in quotes:
    if q is None:
        nulls += 1
        continue
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
        fail.append("spans lines")
        continue
    if len(hits) > 1:
        print("MULTI-HIT (", len(hits), "):", path, repr(q), [lines[h][:24] for h in hits])
    if loc:
        mm = re.match(r"\[(\d\d:\d\d:\d\d)\] ([^:]+):", lines[hits[0]])
        if mm and (mm.group(1) not in loc or mm.group(2) not in loc):
            print("LOC MISMATCH:", path, repr(q), "key:", loc, "actual:", mm.group(1), mm.group(2))
            fail.append("location")
print(f"quotes checked: {n}, null (allowed): {nulls}, not found or invalid: {bad}")
if bad:
    fail.append("quotes")

# --- verbatim spans inside the leak block list must also be exact -----------
spans = 0
for i, item in enumerate(k["expected_leak_blocklist"]):
    for sp in re.findall(r'"([^"]+)"', item):
        spans += 1
        if sp not in t:
            print("BLOCKLIST SPAN NOT IN TRANSCRIPT:", i, repr(sp))
            fail.append("blocklist span")
print(f"blocklist verbatim spans checked: {spans}")

print()
print("RESULT:", "PASS" if not fail else "FAIL " + str(sorted(set(fail))))
