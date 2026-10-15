#!/usr/bin/env python3
"""Quote, field-set and vocabulary check for the s1 answer key.

Checks: JSON validity; the 25-field set complete and in order; nested shapes;
method-spec vocabulary for objection types and decision roles; and every quote
(including account_context.evidence_quote_or_null) an exact substring of the
transcript, on exactly one line, with a matching location.
Exits non-zero on any failure.
"""
import json
import re
import sys

base = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s1-discovery-strong/"
t = open(base + "transcript.txt", encoding="utf-8").read()
lines = t.splitlines()
raw = open(base + "answer-key.json", encoding="utf-8").read()

fails = []


def fail(msg):
    fails.append(msg)
    print("FAIL:", msg)


try:
    k = json.loads(raw)
    print("JSON valid")
except Exception as e:
    print("FAIL: JSON INVALID", e)
    sys.exit(1)

required = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
            "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
            "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
            "objections", "commitments_and_next_steps", "traps", "requested_changes",
            "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
            "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
actual = list(k)
if [x for x in required if x not in k]:
    fail(f"missing keys: {[x for x in required if x not in k]}")
if [x for x in k if x not in required]:
    fail(f"extra keys: {[x for x in k if x not in required]}")
if actual != required:
    fail(f"field order wrong:\n  expected {required}\n  actual   {actual}")
else:
    print(f"field set complete and in order ({len(actual)} fields)")

# nested shapes
if set(k["company"]) != {"name", "industry", "size", "locations", "current_tools"}:
    fail("company keys")
if set(k["expected_verdict"]) != {"verdict", "gates_met", "gates_not_met", "note"}:
    fail("expected_verdict keys")
if set(k["numbers"]) != {"bleed", "upside"}:
    fail("numbers keys")
for side in ("bleed", "upside"):
    if set(k["numbers"][side]) != {"value", "quote", "status"}:
        fail(f"numbers.{side} keys")
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        fail(f"numbers.{side} status")
if set(k["account_context"]) != {"tier", "products_enabled", "existing_monday_setup",
                                 "evidence_quote_or_null"}:
    fail("account_context keys")
if list(k["account_context"]) != ["tier", "products_enabled", "existing_monday_setup",
                                  "evidence_quote_or_null"]:
    fail("account_context key order")
if not isinstance(k["account_context"]["products_enabled"], list) or \
        not k["account_context"]["products_enabled"]:
    fail("account_context.products_enabled must be a non-empty list")
if set(k["expected_structures"]) != {"native_boards_required", "portfolio_expected",
                                     "portfolio_reason", "lookalike_traps", "notes"}:
    fail("expected_structures keys")
if list(k["expected_structures"]) != ["native_boards_required", "portfolio_expected",
                                      "portfolio_reason", "lookalike_traps", "notes"]:
    fail("expected_structures key order")
for i, nb in enumerate(k["expected_structures"]["native_boards_required"]):
    if list(nb) != ["product", "entity", "why"]:
        fail(f"native_boards_required[{i}] keys/order: {list(nb)}")
    if nb["product"] not in ("core", "crm", "service", "dev"):
        fail(f"native_boards_required[{i}] product not a monday product kind: {nb['product']}")
    if nb["product"] == "dev":
        fail(f"native_boards_required[{i}] proposes dev, which is out of v1 scope")
if k["expected_structures"]["portfolio_expected"] is not None and \
        not isinstance(k["expected_structures"]["portfolio_expected"], bool):
    fail("portfolio_expected must be true, false or null")
if not isinstance(k["expected_structures"]["lookalike_traps"], list) or \
        not k["expected_structures"]["lookalike_traps"]:
    fail("lookalike_traps must be a non-empty list")
for f in ("accepted_behaviours", "expected_leak_blocklist"):
    if not isinstance(k[f], list) or not k[f] or not all(isinstance(x, str) and x for x in k[f]):
        fail(f"{f} must be a non-empty list of non-empty strings")
for a in k["attendees"]:
    if list(a) != ["name", "role", "side", "decision_role"]:
        fail(f"attendee keys/order: {list(a)}")
for p in k["expected_monday_products"]:
    if list(p) != ["kind", "why"]:
        fail(f"expected_monday_products keys/order: {list(p)}")
    if p["kind"] not in ("core", "crm", "service", "dev"):
        fail(f"unknown product kind: {p['kind']}")
    if p["kind"] == "dev":
        fail("dev proposed, which is out of v1 scope")

print("scenario id ok:", k["scenario_id"] == "s1-discovery-strong")
if "PLACEHOLDER" in t or "{CO}" in t:
    fail("placeholder left in transcript")
if '"AUTO"' in raw:
    fail("AUTO left in key")
nonascii = sorted({c for c in raw if ord(c) > 127})
if nonascii:
    fail(f"non-ascii in key: {nonascii}")

# method-spec vocabulary (section 5.2 objection names; section 3 decision roles)
SPEC_OBJECTIONS = {"Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves",
                   "Talking to other partners", "Just send a proposal or pricing",
                   "monday itself is the problem", "Team won't adopt it"}
for o in k["objections"]:
    if list(o) != ["quote", "type"]:
        fail(f"objection keys/order: {list(o)}")
    if o["type"] not in SPEC_OBJECTIONS:
        fail(f"objection type not in the spec's names: {o['type']!r}")
SPEC_ROLES = {"approver", "influencer", "admin/owner", "end user", "not applicable"}
for a in k["attendees"]:
    if a["decision_role"] not in SPEC_ROLES:
        fail(f"decision_role not in the spec's vocabulary: {a['decision_role']!r} ({a['name']})")
    if a["side"] == "consultant" and a["decision_role"] != "not applicable":
        fail(f"consultant should carry no client decision role: {a['decision_role']!r}")
print("objection types and decision roles use the spec's vocabulary:",
      not [f for f in fails if "vocabulary" in f or "spec's names" in f])

R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
names = [r["criterion"] for r in k["rubric"]]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
if names[:12] != expected_r:
    fail("R1-R12 not present in order")
for r in k["rubric"]:
    if r["status"] not in ("met", "partial", "missing"):
        fail(f"bad status {r['criterion']}")
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        fail(f"bad per-pain check name: {r['criterion']}")
    if not m and r["criterion"] not in expected_r:
        fail(f"bad criterion name: {r['criterion']}")
    if r["status"] == "missing" and r["evidence"]:
        fail(f"missing but has evidence: {r['criterion']}")
    if r["status"] != "missing" and not r["evidence"]:
        fail(f"no evidence: {r['criterion']}")
for c in k["requested_changes"]:
    if c["type"] not in ("add", "change", "remove"):
        fail(f"bad change type {c}")

quotes = []


def walk(o, path):
    if isinstance(o, dict):
        for kk, v in o.items():
            if kk in ("quote", "evidence_quote_or_null"):
                quotes.append((path + "." + kk, v, o.get("location")))
            else:
                walk(v, path + "." + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(k, "")
n = bad = 0
for path, q, loc in quotes:
    if q is None:
        continue
    n += 1
    if q not in t:
        bad += 1
        fail(f"QUOTE NOT FOUND: {path} {q!r}")
        continue
    hits = [i for i, l in enumerate(lines) if q in l]
    if not hits:
        fail(f"QUOTE SPANS LINES: {path} {q!r}")
        continue
    if len(hits) > 1:
        fail(f"MULTI-HIT ({len(hits)}): {path} {q!r} {[lines[h][:22] for h in hits]}")
    if loc:
        ts = re.match(r"\[(\d\d:\d\d:\d\d)\] ([^:]+):", lines[hits[0]])
        if ts and (ts.group(1) not in loc or ts.group(2) not in loc):
            fail(f"LOC MISMATCH: {path} {q!r} key: {loc} actual: {ts.group(1)} {ts.group(2)}")
print(f"quotes checked: {n}, not found: {bad}")

print("-" * 60)
if fails:
    print(f"{len(fails)} FAILURE(S)")
    sys.exit(1)
print("ALL CHECKS PASSED")
