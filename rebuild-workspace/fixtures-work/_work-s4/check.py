#!/usr/bin/env python3
"""Validity, field-order, shape and quote check for the s4 answer key (WebVTT transcript)."""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s4-discovery-software/"
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
if set(k["expected_verdict"]) != {"verdict", "gates_met", "gates_not_met", "note"}:
    bad("expected_verdict keys")
if set(k["account_context"]) != {"tier", "products_enabled", "existing_monday_setup", "evidence_quote_or_null"}:
    bad(f"account_context keys: {list(k['account_context'])}")
if set(k["expected_structures"]) != {"native_boards_required", "portfolio_expected", "portfolio_reason",
                                     "lookalike_traps", "notes"}:
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
print("scenario id ok:", k["scenario_id"] == "s4-discovery-software")
print("call_type ok:", k["call_type"] == "discovery")
print("build flag true:", k["should_plugin_propose_a_build"] is True)
print("portfolio_expected:", k["expected_structures"]["portfolio_expected"])
print("counts: traps", len(k["traps"]), "| questions", len(k["expected_questions_before_building"]),
      "| accepted_behaviours", len(k["accepted_behaviours"]),
      "| leak_blocklist", len(k["expected_leak_blocklist"]),
      "| native_boards", len(k["expected_structures"]["native_boards_required"]),
      "| lookalike_traps", len(k["expected_structures"]["lookalike_traps"]))

# ---------------------------------------------------------------- rubric
R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
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
for side in ("bleed", "upside"):
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        bad(f"bad numbers status {side}")
for c in k["requested_changes"]:
    if c["type"] not in ("add", "change", "remove"):
        bad(f"bad change type {c}")

# ---------------------------------------------------------------- spec vocabularies
SPEC_OBJECTIONS = ["Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
                   "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it"]
for o in k["objections"]:
    if not any(o["type"].startswith(s) for s in SPEC_OBJECTIONS):
        bad(f"objection type not a spec name: {o['type'][:70]}")
print("objection types all spec names:", all(any(o["type"].startswith(s) for s in SPEC_OBJECTIONS)
                                             for o in k["objections"]),
      "|", len(k["objections"]), "objections")
SPEC_ROLES = ["approver", "influencer", "admin/owner", "end user", "not applicable"]
for a in k["attendees"]:
    if not any(a["decision_role"].startswith(s) for s in SPEC_ROLES):
        bad(f"decision_role not spec vocabulary: {a['name']}: {a['decision_role'][:60]}")
print("decision roles all spec vocabulary:",
      all(any(a["decision_role"].startswith(s) for s in SPEC_ROLES) for a in k["attendees"]))

# ---------------------------------------------------------------- parse WebVTT cues
cues = {}  # cue number -> (start, speaker, text)
block = []
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        num = int(lines[0])
        start = lines[1].split("-->")[0].strip()
        text = " ".join(lines[2:])
        sp = text.split(":", 1)[0] if ":" in text else "?"
        cues[num] = (start, sp, text)
        block.append(num)
print("cues parsed:", len(cues), "| numbering contiguous from 1:", block == list(range(1, len(cues) + 1)))
if not cues:
    bad("no cues parsed")

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
        want_cue = f"cue {hits[0]}"
        if want_cue not in loc or start not in loc or sp not in loc:
            bad(f"LOC MISMATCH: {path} {q[:45]!r} key={loc!r} actual={want_cue}, {start}, {sp}")
print(f"quotes checked: {n}, not found or invalid: {bad_q}")

# ---------------------------------------------------------------- verbatim fragments cited in prose
VERBATIM = ["egg on my face", "I groveled a lot", "We look stupid", "about had a heart attack",
            "they'll revolt", "Engineers hate clicking", "shelfware", "scar tissue",
            "did not sign up to be the Redmine guy", "God help them",
            "Engineering thinks everything's a Sev 3", "Please don't open that can",
            "a whole different VP", "keep my friends in sales", "whose team was the problem",
            "whole job is being confused", "two months free", "evaluating other options",
            "forty-some trucks", "out in Denver", "hundred and twenty an hour", "fifty thousand",
            "forty-ish hours a sprint", "an hour a day each", "Three full weekends",
            "most of a day every release", "more like fifty",
            "homeowner names and phone numbers and addresses", "fifteen hundred technicians",
            "biggest customer by a lot", "the Granite deal", "compliance automation platforms",
            "another tracker", "Sixty is generous", "those are epics technically, I guess",
            "I have no idea what plan they're on or how many seats", "I'd look at it then. Maybe.",
            "Don't hold me to that being the whole list.", "no promises",
            "We can argue about that later.", "I'm not ripping out Zendesk",
            "Part of me wonders if switching tools right before an audit is insane",
            "Mm. I don't know. Maybe?", "that's about right", "it probably will be",
            "Link to the ticket, sure. Copy the ticket, no.", "Redmine is the finding",
            "IT is two people and they report to me", "Laptops, access, offboarding, it's all DMs",
            "the doc is, let's say, aspirational", "Slack is where everything happens and then dies",
            "It's my call on the tool."]
cited_bad = 0
for f in VERBATIM:
    in_key = f in raw
    in_tr = f in t
    if in_key and not in_tr:
        bad(f"prose cites a fragment that is NOT in the transcript: {f!r}")
        cited_bad += 1
print(f"verbatim fragments cited in prose: {sum(1 for f in VERBATIM if f in raw)} cited, {cited_bad} wrong")

# ---------------------------------------------------------------- misc hygiene
print("AUTO/NOT FOUND/TODO left in key:", '"AUTO"' in raw or "NOT FOUND" in raw or "TODO" in raw)
print("non-ascii in key:", sorted({c for c in raw if ord(c) > 127}))
print("non-ascii in transcript:", sorted({c for c in t if ord(c) > 127}))
for w in ("DelOps", "the user"):
    if w in raw:
        bad(f"neutrality: {w!r} appears in the key")
print("\nRESULT:", "PASS" if not fail else f"{len(fail)} FAILURE(S)")
sys.exit(1 if fail else 0)
