#!/usr/bin/env python3
"""Validity, field-order, shape and quote check for the s8 answer key.

Transcript is WebVTT with '<v Speaker Name>' voice tags. Every quote in the key must be an
exact substring of transcript.txt and must sit inside a single cue, and every 'location' must
name that cue's number, start time and speaker.
"""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s8-discovery-enterprise-pmo/"
t = open(BASE + "transcript.txt", encoding="utf-8").read()
raw = open(BASE + "answer-key.json", encoding="utf-8").read()

fail = []


def bad(msg):
    fail.append(msg)
    print("FAIL:", msg)


try:
    k = json.loads(raw)
    print("JSON valid")
except Exception as e:
    print("FAIL: JSON INVALID", e)
    sys.exit(1)

# ---------------------------------------------------------------- field set and order
ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
actual = list(k.keys())
missing = [f for f in ORDER if f not in actual]
extra = [f for f in actual if f not in ORDER]
if missing:
    bad(f"missing fields: {missing}")
if extra:
    bad(f"unexpected fields: {extra}")
print("field set complete:", not missing and not extra)
if actual == ORDER:
    print("field order matches the required order")
else:
    bad(f"field order differs; got {actual}")

# ---------------------------------------------------------------- sub-shapes
if set(k["company"]) != {"name", "industry", "size", "locations", "current_tools"}:
    bad("company keys")
for i, a in enumerate(k["attendees"]):
    if set(a) != {"name", "role", "side", "decision_role"}:
        bad(f"attendees[{i}] keys: {list(a)}")
for i, p in enumerate(k["expected_monday_products"]):
    if set(p) != {"kind", "why"}:
        bad(f"expected_monday_products[{i}] keys: {list(p)}")
for i, r in enumerate(k["rubric"]):
    if set(r) != {"criterion", "status", "evidence", "note"}:
        bad(f"rubric[{i}] keys: {list(r)}")
    for j, e in enumerate(r["evidence"]):
        if set(e) != {"quote", "location"}:
            bad(f"rubric[{i}].evidence[{j}] keys: {list(e)}")
for i, p in enumerate(k["pains"]):
    if set(p) != {"quote", "location", "theme"}:
        bad(f"pains[{i}] keys: {list(p)}")
if set(k["numbers"]) != {"bleed", "upside"}:
    bad("numbers keys")
for side in ("bleed", "upside"):
    if set(k["numbers"][side]) != {"value", "quote", "status"}:
        bad(f"numbers.{side} keys: {list(k['numbers'][side])}")
for i, v in enumerate(k["vocabulary"]):
    if set(v) != {"their_term", "meaning", "likely_monday_object"}:
        bad(f"vocabulary[{i}] keys: {list(v)}")
for i, o in enumerate(k["objections"]):
    if set(o) != {"quote", "type"}:
        bad(f"objections[{i}] keys: {list(o)}")
for i, c in enumerate(k["commitments_and_next_steps"]):
    if set(c) != {"quote", "what", "owner", "date"}:
        bad(f"commitments_and_next_steps[{i}] keys: {list(c)}")
for i, c in enumerate(k["requested_changes"]):
    if set(c) != {"type", "description", "quote"}:
        bad(f"requested_changes[{i}] keys: {list(c)}")
    if c["type"] not in ("add", "change", "remove"):
        bad(f"bad change type {c['type']}")
if set(k["expected_verdict"]) != {"verdict", "gates_met", "gates_not_met", "note"}:
    bad("expected_verdict keys")
if set(k["account_context"]) != {"tier", "products_enabled", "existing_monday_setup",
                                "evidence_quote_or_null"}:
    bad(f"account_context keys: {list(k['account_context'])}")
if set(k["expected_structures"]) != {"native_boards_required", "portfolio_expected",
                                     "portfolio_reason", "lookalike_traps", "notes"}:
    bad(f"expected_structures keys: {list(k['expected_structures'])}")
for i, nb in enumerate(k["expected_structures"]["native_boards_required"]):
    if set(nb) != {"product", "entity", "why"}:
        bad(f"native_boards_required[{i}] keys: {list(nb)}")
    if nb.get("product") not in ("crm", "service"):
        bad(f"native_boards_required[{i}] product not crm/service: {nb.get('product')}")
if not isinstance(k["expected_structures"]["portfolio_expected"], bool):
    bad("portfolio_expected is not a boolean")
for f in ("accepted_behaviours", "expected_leak_blocklist", "traps",
          "expected_questions_before_building", "entities_and_workflows", "integrations_mentioned",
          "compliance_or_security_signals"):
    if not (isinstance(k[f], list) and k[f] and all(isinstance(x, str) and x.strip() for x in k[f])):
        bad(f"{f} is not a non-empty list of non-empty strings")
if not isinstance(k["account_context"]["products_enabled"], list):
    bad("products_enabled is not a list")
print("scenario id ok:", k["scenario_id"] == "s8-discovery-enterprise-pmo")
print("call_type ok:", k["call_type"] in ("discovery", "follow-up-demo-feedback", "intro",
                                         "support-checkin"), k["call_type"])
print("build flag:", k["should_plugin_propose_a_build"])
print("portfolio_expected:", k["expected_structures"]["portfolio_expected"])
print("counts: traps", len(k["traps"]), "| questions", len(k["expected_questions_before_building"]),
      "| accepted_behaviours", len(k["accepted_behaviours"]),
      "| leak_blocklist", len(k["expected_leak_blocklist"]),
      "| native_boards", len(k["expected_structures"]["native_boards_required"]),
      "| lookalike_traps", len(k["expected_structures"]["lookalike_traps"]),
      "| vocabulary", len(k["vocabulary"]), "| pains", len(k["pains"]))

# ---------------------------------------------------------------- rubric names and statuses
R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
expected_r = [f"R{i + 1} {n}" for i, n in enumerate(R)]
names = [r["criterion"] for r in k["rubric"]]
if names[:12] != expected_r:
    bad("R1-R12 not present in order")
print("R1-R12 present in order:", names[:12] == expected_r)
for r in k["rubric"]:
    if r["status"] not in ("met", "partial", "missing"):
        bad(f"bad status {r['criterion']}")
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        bad(f"bad per-pain check name: {r['criterion']}")
    if not m and r["criterion"] not in expected_r:
        bad(f"bad criterion name: {r['criterion']}")
    if r["status"] == "missing" and r["evidence"]:
        bad(f"missing but has evidence: {r['criterion']}")
    if r["status"] != "missing" and not r["evidence"]:
        bad(f"no evidence: {r['criterion']}")
# every per-pain block must carry all six checks
pain_ids = sorted({m.group(1) for m in (re.match(r"^(P\d) ", n) for n in names) if m})
for pid in pain_ids:
    got = [n.split(" ", 1)[1] for n in names if n.startswith(pid + " ")]
    if got != P:
        bad(f"{pid} per-pain checks not the six in order: {got}")
print("per-pain blocks:", pain_ids)
for side in ("bleed", "upside"):
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        bad(f"bad numbers status {side}")

# ---------------------------------------------------------------- spec vocabularies
SPEC_OBJECTIONS = ["Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
                   "Just send a proposal or pricing", "monday itself is the problem",
                   "Team won't adopt it"]
for o in k["objections"]:
    if not any(o["type"].startswith(s) for s in SPEC_OBJECTIONS):
        bad(f"objection type not a spec name: {o['type'][:70]}")
print("objection types all spec names:",
      all(any(o["type"].startswith(s) for s in SPEC_OBJECTIONS) for o in k["objections"]),
      "|", len(k["objections"]), "objections")
SPEC_ROLES = ["approver", "influencer", "admin/owner", "end user", "not applicable"]
for a in k["attendees"]:
    if not any(a["decision_role"].startswith(s) for s in SPEC_ROLES):
        bad(f"decision_role not spec vocabulary: {a['name']}: {a['decision_role'][:60]}")
print("decision roles all spec vocabulary:",
      all(any(a["decision_role"].startswith(s) for s in SPEC_ROLES) for a in k["attendees"]))
for a in k["attendees"]:
    if a["side"] not in ("client", "consultant"):
        bad(f"bad side for {a['name']}: {a['side']}")

# ---------------------------------------------------------------- parse WebVTT cues with <v> tags
if not t.startswith("WEBVTT\n"):
    bad("transcript does not start with a WEBVTT header")
cues = {}
order = []
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        num = int(lines[0])
        start = lines[1].split("-->")[0].strip()
        body = " ".join(lines[2:])
        m = re.match(r"^<v ([^>]+)>(.*)$", body)
        if not m:
            bad(f"cue {num} has no <v Speaker> voice tag: {body[:60]}")
            continue
        cues[num] = (start, m.group(1), m.group(2))
        order.append(num)
print("cues parsed:", len(cues), "| numbering contiguous from 1:",
      order == list(range(1, len(cues) + 1)))
if not cues:
    bad("no cues parsed")
speakers = sorted({sp for _, sp, _ in cues.values()})
print("speakers:", speakers)
spoken = sum(len(txt.split()) for _, _, txt in cues.values())
client = sum(len(txt.split()) for _, sp, txt in cues.values() if sp != "Consultant")
print(f"spoken words: {spoken} | client share: {client / spoken * 100:.1f}% | last cue starts "
      f"{cues[order[-1]][0]}")

# ---------------------------------------------------------------- quotes
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
n = bad_q = 0
for path, q, loc in quotes:
    if q is None:
        continue
    if not isinstance(q, str):
        bad(f"quote not a string: {path} {q!r}")
        bad_q += 1
        continue
    n += 1
    if q not in t:
        bad(f"NOT FOUND in transcript: {path} {q!r}")
        bad_q += 1
        continue
    hits = [num for num, (s, sp, txt) in cues.items() if q in txt]
    if not hits:
        bad(f"spans cues (not inside one cue): {path} {q!r}")
        continue
    if len(hits) > 1:
        print("note: multi-cue match", hits, path, repr(q[:50]))
    if loc:
        start, sp, _ = cues[hits[0]]
        if f"cue {hits[0]}" not in loc or start not in loc or sp not in loc:
            bad(f"LOC MISMATCH: {path} {q[:45]!r} key={loc!r} actual=cue {hits[0]}, {start}, {sp}")
print(f"quotes checked: {n}, not found or invalid: {bad_q}")

# ---------------------------------------------------------------- fragments quoted inside prose
VERBATIM = ["four hundred and thirty-two thousand", "That number is low, if anything",
            "we're also talking to another partner", "We're on the enterprise plan",
            "Every PM starts a job their own way", "which ones are actually in trouble",
            "It's not wrong on purpose", "a color and a number", "the second Tuesday",
            "nobody trusts what's in it", "Dwayne set that up", "another thing to update",
            "it's dead twice", "Power BI", "Procore is the job", "No patient information",
            "immunization records", "Loaded rates", "Those five", "the twenty-third",
            "Junie Rasco", "two hundred and twenty seats", "ninety-five an hour",
            "seventy-two", "sixty-five loaded", "a hundred and fifteen",
            "four hundred and eighty thousand", "a hundred and fifty thousand each",
            "three and a half points", "Eight to twelve million", "fifty-five",
            "January fifteenth", "middle of November", "Bridget goes out on parental leave",
            "Speaker 2", "first patient day", "Several per phase",
            "That's my portfolio", "A program is one health system's work under a master agreement",
            "field crews stay out", "use real names", "Ugly and true"]
cited_bad = 0
for f in VERBATIM:
    if f in raw and f not in t and f != "Speaker 2":
        bad(f"prose cites a fragment that is NOT in the transcript: {f!r}")
        cited_bad += 1
print(f"verbatim fragments cited in prose: {sum(1 for f in VERBATIM if f in raw)} cited, "
      f"{cited_bad} wrong")

# ---------------------------------------------------------------- misc hygiene
print("AUTO/NOT FOUND/TODO left in key:", '"AUTO"' in raw or "NOT FOUND" in raw or "TODO" in raw)
print("non-ascii in key:", sorted({c for c in raw if ord(c) > 127}))
print("non-ascii in transcript:", sorted({c for c in t if ord(c) > 127}))
for w in ("DelOps", "the user", "monday-master-builder"):
    if w in raw:
        bad(f"neutrality: {w!r} appears in the key")
    if w in t:
        bad(f"neutrality: {w!r} appears in the transcript")
print("\nRESULT:", "PASS" if not fail else f"{len(fail)} FAILURE(S)")
sys.exit(1 if fail else 0)
