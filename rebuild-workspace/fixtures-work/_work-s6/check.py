#!/usr/bin/env python3
"""Validity, field-order, shape and quote check for the s6 answer key.

Checks: JSON validity; the 25-field set complete and in the required order;
nested shapes and key order; method-spec vocabulary for objection types and
decision roles; rubric criterion names and statuses; that every quote is an
exact substring of transcript.txt sitting on exactly one line, with a location
that matches that line; that Met rubric rows rest on client-side evidence; and
transcript/key hygiene. Exits non-zero on any failure.
"""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s6-discovery-crm-sales/"
T = open(BASE + "transcript.txt", encoding="utf-8").read()
LINES = [l for l in T.splitlines() if l.strip()]
RAW = open(BASE + "answer-key.json", encoding="utf-8").read()

fails = []


def fail(msg):
    fails.append(msg)
    print("FAIL:", msg)


try:
    k = json.loads(RAW)
    print("JSON valid")
except Exception as e:
    print("FAIL: JSON INVALID", e)
    sys.exit(1)

# ------------------------------------------------------------ field set/order
ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company",
         "attendees", "expected_monday_products", "rubric", "pains", "numbers", "vocabulary",
         "entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
         "objections", "commitments_and_next_steps", "traps", "requested_changes",
         "should_plugin_propose_a_build", "expected_questions_before_building", "expected_verdict",
         "account_context", "expected_structures", "accepted_behaviours", "expected_leak_blocklist"]
actual = list(k)
if [x for x in ORDER if x not in k]:
    fail(f"missing fields: {[x for x in ORDER if x not in k]}")
if [x for x in k if x not in ORDER]:
    fail(f"unexpected fields: {[x for x in k if x not in ORDER]}")
if actual != ORDER:
    fail(f"field order wrong:\n  expected {ORDER}\n  actual   {actual}")
else:
    print(f"field set complete and in order ({len(actual)} fields)")

# ---------------------------------------------------------------- sub-shapes
if list(k["company"]) != ["name", "industry", "size", "locations", "current_tools"]:
    fail(f"company keys/order: {list(k['company'])}")
if not isinstance(k["company"]["current_tools"], list) or not k["company"]["current_tools"]:
    fail("company.current_tools must be a non-empty list")
for a in k["attendees"]:
    if list(a) != ["name", "role", "side", "decision_role"]:
        fail(f"attendee keys/order: {list(a)}")
    if a["side"] not in ("client", "consultant"):
        fail(f"attendee side: {a['side']}")
for p in k["expected_monday_products"]:
    if list(p) != ["kind", "why"]:
        fail(f"expected_monday_products keys/order: {list(p)}")
    if p["kind"] not in ("core", "crm", "service", "dev"):
        fail(f"unknown product kind: {p['kind']}")
    if p["kind"] == "dev":
        fail("dev proposed, which is outside v1 scope")
if list(k["numbers"]) != ["bleed", "upside"]:
    fail("numbers keys/order")
for side in ("bleed", "upside"):
    if list(k["numbers"][side]) != ["value", "quote", "status"]:
        fail(f"numbers.{side} keys/order")
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        fail(f"numbers.{side} status: {k['numbers'][side]['status']}")
for i, v in enumerate(k["vocabulary"]):
    if list(v) != ["their_term", "meaning", "likely_monday_object"]:
        fail(f"vocabulary[{i}] keys/order: {list(v)}")
for i, p in enumerate(k["pains"]):
    if list(p) != ["quote", "location", "theme"]:
        fail(f"pains[{i}] keys/order: {list(p)}")
for i, o in enumerate(k["objections"]):
    if list(o) != ["quote", "type"]:
        fail(f"objections[{i}] keys/order: {list(o)}")
for i, c in enumerate(k["commitments_and_next_steps"]):
    if list(c) != ["quote", "what", "owner", "date"]:
        fail(f"commitments[{i}] keys/order: {list(c)}")
for i, c in enumerate(k["requested_changes"]):
    if list(c) != ["type", "description", "quote"]:
        fail(f"requested_changes[{i}] keys/order: {list(c)}")
    if c["type"] not in ("add", "change", "remove"):
        fail(f"bad requested change type: {c['type']}")
if list(k["expected_verdict"]) != ["verdict", "gates_met", "gates_not_met", "note"]:
    fail("expected_verdict keys/order")
if list(k["account_context"]) != ["tier", "products_enabled", "existing_monday_setup",
                                  "evidence_quote_or_null"]:
    fail("account_context keys/order")
if not isinstance(k["account_context"]["products_enabled"], list) or \
        not k["account_context"]["products_enabled"]:
    fail("account_context.products_enabled must be a non-empty list")
if list(k["expected_structures"]) != ["native_boards_required", "portfolio_expected",
                                      "portfolio_reason", "lookalike_traps", "notes"]:
    fail("expected_structures keys/order")
for i, nb in enumerate(k["expected_structures"]["native_boards_required"]):
    if list(nb) != ["product", "entity", "why"]:
        fail(f"native_boards_required[{i}] keys/order: {list(nb)}")
    if nb["product"] not in ("crm", "service"):
        fail(f"native_boards_required[{i}] product not crm/service: {nb['product']}")
if k["expected_structures"]["portfolio_expected"] is not None and \
        not isinstance(k["expected_structures"]["portfolio_expected"], bool):
    fail("portfolio_expected must be true, false or null")
for f in ("entities_and_workflows", "integrations_mentioned", "compliance_or_security_signals",
          "traps", "expected_questions_before_building", "accepted_behaviours",
          "expected_leak_blocklist"):
    if not (isinstance(k[f], list) and k[f] and all(isinstance(x, str) and x.strip() for x in k[f])):
        fail(f"{f} must be a non-empty list of non-empty strings")
if not (isinstance(k["expected_structures"]["lookalike_traps"], list)
        and k["expected_structures"]["lookalike_traps"]):
    fail("lookalike_traps must be a non-empty list")
print("scenario id ok:", k["scenario_id"] == "s6-discovery-crm-sales")
print("call_type ok:", k["call_type"] in ("discovery", "follow-up-demo-feedback", "intro",
                                          "support-checkin"))
print("build flag:", k["should_plugin_propose_a_build"])
print("portfolio_expected:", k["expected_structures"]["portfolio_expected"])

# --------------------------------------------------------- spec vocabularies
SPEC_OBJECTIONS = ["Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves",
                   "Talking to other partners", "Just send a proposal or pricing",
                   "monday itself is the problem", "Team won't adopt it"]
for o in k["objections"]:
    if not any(o["type"].startswith(s) for s in SPEC_OBJECTIONS):
        fail(f"objection type not a spec name: {o['type'][:70]}")
print("objection types all spec names:",
      all(any(o["type"].startswith(s) for s in SPEC_OBJECTIONS) for o in k["objections"]),
      "|", len(k["objections"]), "objections")
SPEC_ROLES = ["approver", "influencer", "admin/owner", "end user", "not applicable"]
for a in k["attendees"]:
    if not any(a["decision_role"].startswith(s) for s in SPEC_ROLES):
        fail(f"decision_role not spec vocabulary: {a['name']}: {a['decision_role'][:60]}")
    if a["side"] == "consultant" and a["decision_role"] != "not applicable":
        fail(f"consultant carries a client decision role: {a['decision_role']!r}")
print("decision roles all spec vocabulary:",
      all(any(a["decision_role"].startswith(s) for s in SPEC_ROLES) for a in k["attendees"]))

# ------------------------------------------------------------------- rubric
R = ["Current state mapped", "Pain made concrete", "Why now", "Bleed number", "Upside number",
     "Desired outcome", "Decision process mapped", "Priority and timing", "Blockers surfaced",
     "Next step committed", "Solution confirmed", "Scope agreed verbally"]
P = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
expected_r = [f"R{i+1} {n}" for i, n in enumerate(R)]
names = [r["criterion"] for r in k["rubric"]]
if names[:12] != expected_r:
    fail("R1-R12 not present, in order, at the head of the rubric")
print("R1-R12 present in order:", names[:12] == expected_r, "| rubric rows:", len(k["rubric"]))
for r in k["rubric"]:
    if list(r) != ["criterion", "status", "evidence", "note"]:
        fail(f"rubric keys/order for {r.get('criterion')}: {list(r)}")
    if r["status"] not in ("met", "partial", "missing"):
        fail(f"bad status: {r['criterion']} -> {r['status']}")
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m and m.group(2) not in P:
        fail(f"bad per-pain check name: {r['criterion']}")
    if not m and r["criterion"] not in expected_r:
        fail(f"bad criterion name: {r['criterion']}")
    if r["status"] == "missing" and r["evidence"]:
        fail(f"missing but has evidence: {r['criterion']}")
    if r["status"] != "missing" and not r["evidence"]:
        fail(f"no evidence: {r['criterion']}")
    if not r["note"].strip():
        fail(f"empty note: {r['criterion']}")
# per-pain blocks must be complete: six checks per graded pain
pp = {}
for r in k["rubric"]:
    m = re.match(r"^(P\d) (.+)$", r["criterion"])
    if m:
        pp.setdefault(m.group(1), []).append(m.group(2))
for pid, checks in pp.items():
    if checks != P:
        fail(f"{pid} per-pain checks incomplete or out of order: {checks}")
print("per-pain blocks graded:", sorted(pp), "each with all six checks:",
      all(v == P for v in pp.values()))
# gates: each spec stage named exactly once across gates_met / gates_not_met
STAGES = ["Solution blueprint", "Build", "First demo (v0.1)", "Pricing or proposal prep",
          "v1.0 sign-off"]
gates = k["expected_verdict"]["gates_met"] + k["expected_verdict"]["gates_not_met"]
for s in STAGES:
    n = sum(1 for g in gates if g.startswith(s))
    if n != 1:
        fail(f"stage {s!r} appears {n} times across gates_met/gates_not_met")
if len(gates) != len(STAGES):
    fail(f"{len(gates)} gate entries for {len(STAGES)} spec stages")
print("all five spec stages named exactly once across the gates:",
      all(sum(1 for g in gates if g.startswith(s)) == 1 for s in STAGES))
if k["expected_verdict"]["verdict"] not in ("Discovery complete", "Nearly ready", "Not ready"):
    fail(f"verdict not a spec value: {k['expected_verdict']['verdict']}")
print("verdict:", k["expected_verdict"]["verdict"])

# ------------------------------------------------- internal cross-references
# Every P# the prose refers to must exist as a graded pain in `pains` (a note
# that says "P5 to P7" when the pains run P5 to P8 is a real defect).
# Pain ids are single-digit (P1-P9); 'P21' in this key is the ERP, Prophet 21.
pain_ids = {p["theme"].split()[0] for p in k["pains"]}
if not all(re.fullmatch(r"P[1-9]", p) for p in pain_ids):
    fail(f"pains themes must start with a pain id P1-P9: {sorted(pain_ids)}")
referenced = set()


def refs(o, key=None):
    if isinstance(o, str):
        if key != "criterion":
            referenced.update(re.findall(r"\bP[1-9]\b", o))
    elif isinstance(o, dict):
        for kk, v in o.items():
            refs(v, kk)
    elif isinstance(o, list):
        for v in o:
            refs(v, key)


refs(k)
dangling = sorted(referenced - pain_ids, key=lambda s: int(s[1:]))
if dangling:
    fail(f"prose refers to pain ids that are not in `pains`: {dangling}")
missing_range = sorted(pain_ids - referenced, key=lambda s: int(s[1:]))
if missing_range:
    fail(f"pains never referred to anywhere in the prose: {missing_range}")
print(f"pain ids consistent: {len(pain_ids)} in `pains`, all referenced, none dangling")

# The self-description must match the transcript it describes.
last = re.match(r"^\[(\d\d):(\d\d)\]", LINES[-1]).groups()
first = re.match(r"^\[(\d\d):(\d\d)\]", LINES[0]).groups()
fmt = k["transcript_format"]
for label, token in (("turn count", f"{len(LINES)} turns"),
                     ("first timestamp", f"[{first[0]}:{first[1]}]"),
                     ("last timestamp", f"[{last[0]}:{last[1]}]")):
    if token not in fmt:
        fail(f"transcript_format {label} does not match the transcript: expected {token!r}")
mins = int(last[0]) + (1 if int(last[1]) >= 30 else 0)
for field in ("purpose_of_this_fixture", "transcript_format"):
    for claim in re.findall(r"(\d+)-minute (?:discovery )?call", k[field]):
        if abs(int(claim) - mins) > 1:
            fail(f"{field} calls this a {claim}-minute call; the transcript ends at "
                 f"{last[0]}:{last[1]}")
print(f"self-description matches transcript: {len(LINES)} turns, [{first[0]}:{first[1]}]-"
      f"[{last[0]}:{last[1]}]")

# -------------------------------------------------------------------- quotes
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
CONSULTANT_EVIDENCE = []
for path, q, l in quotes:
    if q is None:
        continue
    if not isinstance(q, str):
        fail(f"quote not a string: {path} {q!r}")
        bad += 1
        continue
    n += 1
    if q not in T:
        fail(f"QUOTE NOT FOUND: {path} {q!r}")
        bad += 1
        continue
    hits = [line for line in LINES if q in line]
    if not hits:
        fail(f"QUOTE SPANS LINES: {path} {q!r}")
        bad += 1
        continue
    if len(hits) > 1:
        fail(f"MULTI-LINE MATCH ({len(hits)}): {path} {q[:50]!r}")
        bad += 1
        continue
    m = re.match(r"^(\[\d\d:\d\d\]) ([^:]+):", hits[0])
    if not m:
        fail(f"host line not in '[MM:SS] Speaker: text' form: {hits[0][:60]!r}")
        continue
    stamp, sp = m.group(1), m.group(2)
    if l:
        if stamp not in l or sp not in l:
            fail(f"LOC MISMATCH: {path} {q[:45]!r} key={l!r} actual={stamp} {sp}")
    if path.startswith(".rubric") and sp == "Consultant":
        CONSULTANT_EVIDENCE.append((path, q[:50]))
print(f"quotes checked: {n}, not found or invalid: {bad}")

# Met/Partial rubric rows must rest on client-side evidence (spec 2.1)
if CONSULTANT_EVIDENCE:
    for path, q in CONSULTANT_EVIDENCE:
        fail(f"rubric evidence is consultant-side: {path} {q!r}")
print("all rubric evidence is client-side:", not CONSULTANT_EVIDENCE)

# ---------------------------------------------- fragments quoted inside prose
VERBATIM = ["It says Pro when I log in", "a whole sales CRM section in there with nothing in it",
            "don't leave two of them", "You're not rebuilding our quoting",
            "I was copying the workbook columns onto a board, which I don't think was right",
            "I didn't really know how it should be built", "No. Nowhere near half.",
            "Three hundred and six thousand a year", "Once they're ramped they're ramped",
            "It feels low, if anything", "This is my call", "Gene wants to be told, not asked",
            "reasonable but he's slow", "probably that's us", "The boards purchasing built are a mess",
            "Is that monday, or is that us?", "What am I paying for?",
            "I've paid for GoldMine twice", "some of them are excellent and some of them are not",
            "That number made me feel sick, honestly", "that's the part that keeps me up",
            "That was embarrassing", "we looked like a mess",
            "I'll get excited and then I'll be wrong in front of Gene",
            "the reps are useless for anything else Monday and Tuesday",
            "Separate. Let's not boil the ocean.", "mentioned it at a golf thing",
            "A few hundred dollars of margin on that order",
            "If a rep can see what we give another customer on the same part, I'll have a problem within a week",
            "Inside sales takes maybe a third of the orders",
            "no notes, no, this guy only buys in July, no, don't call before ten. That's all gone",
            "An account. Or a customer, same thing", "Blanket order, same idea",
            "calling Fort Wayne to ask a question", "I've got a quote out at Brightline",
            "the legal pad stops working", "If it's not working before December first",
            "I'd rather stay under it", "We paid for GoldMine for six years and used it for about one",
            "A guess. I'll be straight with you", "twenty-five points",
            "It'll be a photo of the legal pad", "I'll send the invite when we hang up",
            "something like four hundred and seventy thousand in margin",
            "I'll look at those boards before I build anything",
            "That's a good catch and I'll come back to you about where they fit",
            "It's either the base for this or it gets cleaned up"]
miscited = 0
for frag in VERBATIM:
    if frag in RAW and frag not in T:
        fail(f"prose cites a fragment that is NOT in the transcript: {frag!r}")
        miscited += 1
print(f"prose fragments cross-checked: {sum(1 for f in VERBATIM if f in RAW)} cited, {miscited} wrong")

# Generalised version of the same check: any long, sentence-looking span the key
# wraps in single quotes should be real transcript text. A span ends at the next
# apostrophe, so contractions truncate it to a prefix, which is still a valid
# substring test. Spans that are deliberately not transcript text go in ALLOW.
ALLOW = {
    "Activity ' with a trailing space",
    # Method-spec wording, quoted as method vocabulary rather than as client speech.
    "monday itself is the problem",
    "what would you do with it",
}
strings = []


def collect(o):
    if isinstance(o, str):
        strings.append(o)
    elif isinstance(o, dict):
        for v in o.values():
            collect(v)
    elif isinstance(o, list):
        for v in o:
            collect(v)


# expected_leak_blocklist is exempt: its entries are match patterns for a leak
# scanner (spoken forms, lower case, digit and $ variants), not quotations.
collect({kk: v for kk, v in k.items() if kk != "expected_leak_blocklist"})
scanned = loose = 0
# Capitalised spans, and lower-case spans that open right after a space so that
# possessives and contractions elsewhere in the sentence are not mistaken for
# the start of a citation.
PATTERNS = (r"'([A-Z][^']{19,})'", r"(?<= ')([a-z][^']{24,})'")
for s in strings:
    for pat in PATTERNS:
        for frag in re.findall(pat, s):
            if frag in ALLOW:
                continue
            scanned += 1
            if frag not in T:
                fail(f"prose quotes text that is not in the transcript: {frag!r}")
                loose += 1
print(f"quoted spans auto-scanned in prose: {scanned}, not in transcript: {loose}")

# ------------------------------------------------------------------ hygiene
for bad_token in ('"AUTO"', "UNRESOLVED", "NOT FOUND", "TODO", "PLACEHOLDER", "{CO}"):
    if bad_token in RAW:
        fail(f"placeholder left in key: {bad_token}")
if "PLACEHOLDER" in T or "{CO}" in T:
    fail("placeholder left in transcript")
na_key = sorted({c for c in RAW if ord(c) > 127})
na_tr = sorted({c for c in T if ord(c) > 127})
if na_key:
    fail(f"non-ascii in key: {na_key}")
if na_tr:
    fail(f"non-ascii in transcript: {na_tr}")
for w in ("DelOps", "the user"):
    if w in RAW:
        fail(f"neutrality: {w!r} appears in the key")
    if w in T:
        fail(f"neutrality: {w!r} appears in the transcript")
# transcript shape
prev = -1
for i, line in enumerate(LINES):
    m = re.match(r"^\[(\d\d):(\d\d)\] ([^:]+): (.+)$", line)
    if not m:
        fail(f"malformed transcript line {i+1}: {line[:60]!r}")
        continue
    sec = int(m.group(1)) * 60 + int(m.group(2))
    if sec < prev:
        fail(f"timestamp goes backwards at line {i+1}: {line[:40]!r}")
    prev = sec
if len(set(LINES)) != len(LINES):
    fail("duplicate transcript lines (would make quotes ambiguous)")
words = sum(len(re.match(r"^\[\d\d:\d\d\] [^:]+: (.+)$", l).group(1).split()) for l in LINES)
cons = sum(len(re.match(r"^\[\d\d:\d\d\] [^:]+: (.+)$", l).group(1).split())
           for l in LINES if l.startswith("[") and "] Consultant:" in l)
print(f"transcript: {len(LINES)} turns, {words} spoken words, client share "
      f"{100*(words-cons)/words:.1f}%")

print("-" * 62)
if fails:
    print(f"{len(fails)} FAILURE(S)")
    sys.exit(1)
print("ALL CHECKS PASSED")
