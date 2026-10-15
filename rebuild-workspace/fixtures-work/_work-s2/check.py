#!/usr/bin/env python3
"""Structure, order and quote check for the s2 answer key (locations are 'L<line>, Speaker')."""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s2-discovery-gaps/"
t = open(BASE + "transcript.txt", encoding="utf-8").read()
lines = t.splitlines()
raw = open(BASE + "answer-key.json", encoding="utf-8").read()

fail = 0


def bad(*a):
    global fail
    fail += 1
    print("FAIL:", *a)


try:
    k = json.loads(raw, object_pairs_hook=lambda p: __import__("collections").OrderedDict(p))
    print("JSON valid")
except Exception as e:
    print("JSON INVALID", e)
    sys.exit(1)

ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
got = list(k.keys())
print("field count:", len(got), "expected:", len(ORDER))
if got != ORDER:
    bad("field set/order wrong")
    print("  missing:", [x for x in ORDER if x not in got])
    print("  extra:", [x for x in got if x not in ORDER])
    print("  order got:", got)
else:
    print("field set complete and in order: True")

# nested shapes
if set(k["company"]) != {"name", "industry", "size", "locations", "current_tools"}:
    bad("company keys")
if set(k["expected_verdict"]) != {"verdict", "gates_met", "gates_not_met", "note"}:
    bad("expected_verdict keys")
if list(k["account_context"]) != ["tier", "products_enabled", "existing_monday_setup",
                                 "evidence_quote_or_null"]:
    bad("account_context keys/order", list(k["account_context"]))
if list(k["expected_structures"]) != ["native_boards_required", "portfolio_expected",
                                      "portfolio_reason", "lookalike_traps", "notes"]:
    bad("expected_structures keys/order", list(k["expected_structures"]))
for nb in k["expected_structures"]["native_boards_required"]:
    if list(nb) != ["product", "entity", "why"]:
        bad("native_boards_required item keys", list(nb))
if not isinstance(k["expected_structures"]["portfolio_expected"], bool):
    bad("portfolio_expected not bool")
for f in ("accepted_behaviours", "expected_leak_blocklist", "traps",
          "expected_questions_before_building"):
    if not (isinstance(k[f], list) and all(isinstance(x, str) and x for x in k[f])):
        bad(f + " not a list of non-empty strings")
for f in ("numbers",):
    for side in ("bleed", "upside"):
        if list(k[f][side]) != ["value", "quote", "status"]:
            bad("numbers." + side + " keys")
        if k[f][side]["status"] not in ("met", "partial", "missing"):
            bad("numbers." + side + " status")
for a in k["attendees"]:
    if list(a) != ["name", "role", "side", "decision_role"]:
        bad("attendee keys", a.get("name"))
for p in k["expected_monday_products"]:
    if list(p) != ["kind", "why"]:
        bad("product keys", p)
for o in k["objections"]:
    if list(o) != ["quote", "type"]:
        bad("objection keys", o)
for c in k["commitments_and_next_steps"]:
    if list(c) != ["quote", "what", "owner", "date"]:
        bad("commitment keys", c)

print("scenario id ok:", k["scenario_id"] == "s2-discovery-gaps")
print("call_type ok:", k["call_type"] == "discovery")
print("should_plugin_propose_a_build is False:", k["should_plugin_propose_a_build"] is False)
print("portfolio_expected is False:", k["expected_structures"]["portfolio_expected"] is False)
print("products_enabled empty:", k["account_context"]["products_enabled"] == [])
nonascii = sorted({c for c in raw if ord(c) > 127})
print("non-ascii in key:", nonascii)
if nonascii:
    bad("non-ascii present")

# ---- method-spec vocabulary: decision roles and objection names
SPEC_ROLES = {"approver", "influencer", "admin/owner", "end user", "not applicable"}
for a in k["attendees"]:
    if a["decision_role"].split(" (")[0].strip() not in SPEC_ROLES:
        bad("decision_role not spec vocabulary:", a["name"], repr(a["decision_role"]))
SPEC_OBJ = ["Price feels high", "Needs to think it over", "Must check with someone",
            "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
            "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it",
            "Outside the map"]
counts = {}
for o in k["objections"]:
    head = next((s for s in SPEC_OBJ if o["type"].startswith(s)), None)
    if head is None:
        bad("objection type not a spec name:", repr(o["type"][:60]))
    else:
        counts[head] = counts.get(head, 0) + 1
print("objection types by spec name:", counts, "total", len(k["objections"]))

# ---- rubric
R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
names = [r["criterion"] for r in k["rubric"]]
print("R1-R12 present in order:", names[:12] == expected_r)
if names[:12] != expected_r:
    bad("rubric R rows")
for r in k["rubric"]:
    if list(r) != ["criterion", "status", "evidence", "note"]:
        bad("rubric row keys", r["criterion"])
    if r["status"] not in ("met", "partial", "missing"):
        bad("rubric status", r["criterion"])
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        bad("per-pain check name", r["criterion"])
    if not m and r["criterion"] not in expected_r:
        bad("criterion name", r["criterion"])
    if r["status"] == "missing" and r["evidence"]:
        # A Missing row may cite Consultant-side lines to evidence the gap itself
        # (R10 does this on purpose, and its note says so). It must never cite
        # client-side evidence, which would contradict the grade.
        spk = [e.get("location", "").split(", ")[-1] for e in r["evidence"]]
        if set(spk) != {"Consultant"}:
            bad("missing but has client-side evidence", r["criterion"], spk)
        else:
            print("  note missing-with-consultant-evidence (allowed):", r["criterion"])
    if r["status"] != "missing" and not r["evidence"]:
        bad("no evidence", r["criterion"])
    for e in r["evidence"]:
        if list(e) != ["quote", "location"]:
            bad("evidence keys", r["criterion"])
if any(r["status"] == "met" for r in k["rubric"] if r["criterion"].startswith("R")):
    bad("an R row is Met (fixture expects nothing Met)")

# ---- every quote is an exact substring, on one line, with a matching location
quotes = []


def walk(o, path):
    if isinstance(o, dict):
        for kk, v in o.items():
            if kk == "quote":
                quotes.append((path, v, o.get("location")))
            else:
                walk(v, path + "." + kk)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, f"{path}[{i}]")


walk(k, "")
n = 0
for path, q, loc in quotes:
    if q is None:
        continue
    if not isinstance(q, str):
        bad("quote not a string", path, repr(q))
        continue
    n += 1
    if q not in t:
        bad("NOT FOUND", path, repr(q))
        continue
    hits = [i for i, l in enumerate(lines) if q in l]
    if not hits:
        bad("SPANS LINES", path, repr(q))
        continue
    if len(hits) > 1:
        print("  note MULTI-HIT", len(hits), path, repr(q[:40]))
    if loc:
        m = re.match(r"^L(\d+), (.+)$", loc)
        if not m:
            bad("location format", path, repr(loc))
        else:
            ln, spk = int(m.group(1)), m.group(2)
            if ln - 1 not in hits:
                bad("LOC LINE MISMATCH", path, repr(q[:40]), "key:", loc, "actual lines:",
                    [h + 1 for h in hits])
            elif not lines[ln - 1].startswith(spk + ":"):
                bad("LOC SPEAKER MISMATCH", path, repr(q[:40]), "key:", loc,
                    "actual:", lines[ln - 1].split(":")[0])
print("quotes checked:", n)

# ---- verbatim fragments embedded in prose in the new/edited fields
FRAGMENTS = [
    "No. I've seen the ads.",
    "Kelsey said she used it at her old job, maybe? Or it was a different one.",
    "it's priced by seat, but there's some ways around that, like forms, guest access",
    "Everywhere. The phones, the office inbox, the website.",
    "a service ticket for us is the actual visit. That's in the system.",
    "You could put a form right on your website",
    "So all of that, the email, the phone, the website, it all lands in one place as tickets.",
    "so if a complaint hasn't been touched by end of day it goes red",
    "that's supposed to come to us as a lead, so we can call them.",
    "you'd have a customers board, a plans board with every plan and what round they're on, a routes board for Travis",
    "That's a lot of boards.",
    "she wasn't crying, but she was upset",
    "And then she's asking for Gary. And then Gary's asking me.",
    "Gary took that pretty hard",
    "He printed one out",
    "Kind of in a mean way.",
    "My step count's great, though.",
    "Hector will die before he gives up the paper",
    "Hector's gonna be buried with a clipboard",
    "He knows the dogs better than the customers.",
    "The ticket's under the seat with a gas station burrito wrapper.",
    "I have no idea how billing works.",
    "she has her own spreadsheet",
    "It's a different everything up there.",
    "I'll put some ballpark numbers in there for him.",
    "in monday that basically can't happen",
    "monday connects to pretty much everything.",
    "Most people pick it up in a day, honestly.",
    "Fifteen, twenty a week, maybe?",
    "Summer's like double",
    "the sheet's fine",
    "the board works",
    "I'll send something over",
    "Oh. Huh. That sounds interesting.",
    "that call becomes a ticket",
]
for frag in FRAGMENTS:
    if frag not in t:
        bad("prose fragment not verbatim in transcript:", repr(frag))
print("prose fragments checked:", len(FRAGMENTS))

print("\nRESULT:", "PASS" if not fail else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
