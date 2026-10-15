#!/usr/bin/env python3
"""Checker for the s9 fixture: exact-substring quotes + complete, ordered field set."""
import json, sys, re, os

BASE = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s9-followup-no-portfolio-unlabelled'
TRANSCRIPT = os.path.join(BASE, 'transcript.txt')
KEY = os.path.join(BASE, 'answer-key.json')

REQUIRED_ORDER = [
    "scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format",
    "company", "attendees", "expected_monday_products", "rubric", "pains",
    "numbers", "vocabulary", "entities_and_workflows", "integrations_mentioned",
    "compliance_or_security_signals", "objections", "commitments_and_next_steps",
    "traps", "requested_changes", "should_plugin_propose_a_build",
    "expected_questions_before_building", "expected_verdict", "account_context",
    "expected_structures", "accepted_behaviours", "expected_leak_blocklist",
]

GATE_STAGES = ["Solution blueprint", "Build", "First demo (v0.1)",
               "Pricing or proposal prep", "v1.0 sign-off"]

errors, warnings = [], []

def err(m): errors.append(m)
def warn(m): warnings.append(m)

# ---------- load ----------
raw_key = open(KEY, encoding='utf-8').read()
try:
    key = json.loads(raw_key)
    json_valid = True
except Exception as e:
    print("FATAL: answer-key.json is not valid JSON:", e)
    sys.exit(1)

transcript = open(TRANSCRIPT, encoding='utf-8').read()
paragraphs = [p for p in transcript.split('\n\n') if p.strip()]

# ---------- ascii ----------
for name, text in (("transcript.txt", transcript), ("answer-key.json", raw_key)):
    bad = sorted({c for c in text if ord(c) >= 128})
    if bad:
        err(f"{name} contains non-ASCII characters: {bad}")

# ---------- field set complete and in order ----------
actual = list(key.keys())
if actual != REQUIRED_ORDER:
    missing = [f for f in REQUIRED_ORDER if f not in actual]
    extra = [f for f in actual if f not in REQUIRED_ORDER]
    if missing: err(f"MISSING fields: {missing}")
    if extra: err(f"UNEXPECTED fields: {extra}")
    if not missing and not extra:
        err("Fields present but in the WRONG ORDER.")
        for i, (a, b) in enumerate(zip(actual, REQUIRED_ORDER)):
            if a != b:
                err(f"  position {i}: found '{a}', expected '{b}'")
                break

# ---------- no speaker labels in transcript (format trap) ----------
if re.search(r'^(Consultant|Marisol|Warren|Ines|Speaker \d+|[A-Z][a-z]+ [A-Z][a-z]+)\s*(\(\d{2}:\d{2}:\d{2}\))?\s*:', transcript, re.M):
    err("transcript.txt appears to contain speaker labels; this fixture must have none.")
if '<v ' in transcript:
    err("transcript.txt contains WebVTT voice tags; this fixture must have none.")

# ---------- collect and check every quote ----------
quotes = []
def walk(node, path):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'quote' and isinstance(v, str):
                quotes.append((v, f"{path}.{k}"))
            elif k == 'quote' and v is None:
                warn(f"{path}.quote is null")
            else:
                walk(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{path}[{i}]")
walk(key, 'key')

for q, path in quotes:
    if q not in transcript:
        err(f"QUOTE NOT AN EXACT SUBSTRING at {path}: {q!r}")
        continue
    hits = [i + 1 for i, p in enumerate(paragraphs) if q in p]
    if not hits:
        err(f"QUOTE SPANS A PARAGRAPH BREAK at {path}: {q!r}")
    elif len(hits) > 1:
        warn(f"quote appears in {len(hits)} paragraphs {hits} at {path}: {q!r}")
    if transcript.count(q) > 1:
        warn(f"quote occurs {transcript.count(q)}x in transcript at {path}: {q!r}")

# ---------- stated paragraph number must match the real one ----------
# Locations in this key are 'paragraph N, [ts,] inferred Name (speaker unclear)'.
located = []
def walk_loc(node, path):
    if isinstance(node, dict):
        if isinstance(node.get('quote'), str) and isinstance(node.get('location'), str):
            located.append((node['quote'], node['location'], path))
        for k, v in node.items():
            walk_loc(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_loc(v, f"{path}[{i}]")
walk_loc(key, 'key')

speakers_by_para = {}
for q, loc, path in located:
    m = re.search(r'paragraph (\d+)', loc)
    if not m:
        err(f"location has no paragraph number at {path}: {loc!r}")
        continue
    stated = int(m.group(1))
    para_hits = [i + 1 for i, p in enumerate(paragraphs) if q in p]
    if para_hits != [stated]:
        err(f"LOCATION PARAGRAPH WRONG at {path}: says paragraph {stated}, "
            f"quote is in {para_hits}: {q!r}")
    ts = re.match(r'\[(\d\d:\d\d:\d\d)\]', paragraphs[stated - 1]) if 1 <= stated <= len(paragraphs) else None
    if ts and ts.group(1) not in loc:
        warn(f"paragraph {stated} carries timestamp [{ts.group(1)}] but the location omits it at {path}")
    if not ts and re.search(r'\[\d\d:\d\d:\d\d\]', loc):
        err(f"location cites a timestamp but paragraph {stated} has none at {path}")
    sm = re.search(r'inferred ([A-Za-z ]+?) \(speaker unclear\)', loc)
    if not sm:
        err(f"location lacks an inferred speaker marked '(speaker unclear)' at {path}: {loc!r}")
    else:
        speakers_by_para.setdefault(stated, set()).add(sm.group(1).strip())

# Only the two run-together notetaker paragraphs may hold more than one speaker.
RUN_TOGETHER = {55, 60}
for para, names in sorted(speakers_by_para.items()):
    if len(names) > 1 and para not in RUN_TOGETHER:
        err(f"paragraph {para} is attributed to several speakers {sorted(names)}; "
            f"only paragraphs {sorted(RUN_TOGETHER)} run two speakers together")

# ---------- rubric shape ----------
valid_status = {"met", "partial", "missing"}
for i, row in enumerate(key.get('rubric', [])):
    for f in ("criterion", "status", "evidence", "note"):
        if f not in row: err(f"rubric[{i}] missing field '{f}'")
    if row.get('status') not in valid_status:
        err(f"rubric[{i}] status {row.get('status')!r} not in {valid_status}")
    for j, ev in enumerate(row.get('evidence', [])):
        if set(ev.keys()) != {"quote", "location"}:
            err(f"rubric[{i}].evidence[{j}] keys {set(ev.keys())} != {{quote, location}}")
    if row.get('status') in ("met", "partial") and not row.get('evidence'):
        note = row.get('note', '')
        if not re.search(r'[Cc]arried forward', note):
            warn(f"rubric[{i}] '{row.get('criterion')}' is {row.get('status')} with no evidence "
                 f"and no 'carried forward' note")

# ---------- other nested shapes ----------
for i, a in enumerate(key.get('attendees', [])):
    if set(a.keys()) != {"name", "role", "side", "decision_role"}:
        err(f"attendees[{i}] keys {set(a.keys())}")
for i, p in enumerate(key.get('pains', [])):
    if set(p.keys()) != {"quote", "location", "theme"}:
        err(f"pains[{i}] keys {set(p.keys())}")
for i, p in enumerate(key.get('expected_monday_products', [])):
    if set(p.keys()) != {"kind", "why"}:
        err(f"expected_monday_products[{i}] keys {set(p.keys())}")
for i, o in enumerate(key.get('objections', [])):
    if set(o.keys()) != {"quote", "type"}:
        err(f"objections[{i}] keys {set(o.keys())}")
for i, c in enumerate(key.get('commitments_and_next_steps', [])):
    if set(c.keys()) != {"quote", "what", "owner", "date"}:
        err(f"commitments_and_next_steps[{i}] keys {set(c.keys())}")
for i, r in enumerate(key.get('requested_changes', [])):
    if set(r.keys()) != {"type", "description", "quote"}:
        err(f"requested_changes[{i}] keys {set(r.keys())}")
for i, v in enumerate(key.get('vocabulary', [])):
    if set(v.keys()) != {"their_term", "meaning", "likely_monday_object"}:
        err(f"vocabulary[{i}] keys {set(v.keys())}")

nums = key.get('numbers', {})
if set(nums.keys()) != {"bleed", "upside"}:
    err(f"numbers keys {set(nums.keys())} != {{bleed, upside}}")
for k2 in ("bleed", "upside"):
    if k2 in nums and set(nums[k2].keys()) != {"value", "quote", "status"}:
        err(f"numbers.{k2} keys {set(nums[k2].keys())}")
    if k2 in nums and nums[k2].get('status') not in valid_status:
        err(f"numbers.{k2}.status invalid")

ac = key.get('account_context', {})
if set(ac.keys()) != {"tier", "products_enabled", "existing_monday_setup", "evidence_quote_or_null"}:
    err(f"account_context keys {set(ac.keys())}")

es = key.get('expected_structures', {})
if set(es.keys()) != {"native_boards_required", "portfolio_expected", "portfolio_reason",
                      "lookalike_traps", "notes"}:
    err(f"expected_structures keys {set(es.keys())}")
for i, nb in enumerate(es.get('native_boards_required', [])):
    if set(nb.keys()) != {"product", "entity", "why"}:
        err(f"expected_structures.native_boards_required[{i}] keys {set(nb.keys())}")

# ---------- verdict gates ----------
ev = key.get('expected_verdict', {})
if set(ev.keys()) != {"verdict", "gates_met", "gates_not_met", "note"}:
    err(f"expected_verdict keys {set(ev.keys())}")
all_gates = ev.get('gates_met', []) + ev.get('gates_not_met', [])
for stage in GATE_STAGES:
    n = sum(1 for g in all_gates if g.startswith(stage))
    if n != 1:
        err(f"gate stage '{stage}' appears {n} times across gates_met/gates_not_met (want 1)")
if len(all_gates) != 5:
    err(f"{len(all_gates)} gate entries total (want exactly 5)")

# ---------- neutrality ----------
for banned in ("DelOps", "Master Builder", "the user"):
    if banned.lower() in transcript.lower():
        err(f"transcript leaks '{banned}'")
    if banned.lower() in raw_key.lower() and banned != "the user":
        warn(f"answer-key mentions '{banned}'")

# ---------- report ----------
print(f"transcript: {len(paragraphs)} paragraphs, {len(transcript.split())} words")
print(f"answer-key: {len(key)} top-level fields, {len(quotes)} quotes checked")
print(f"located quotes with paragraph numbers verified: {len(located)}")
print(f"field set complete and in order: {actual == REQUIRED_ORDER}")
print(f"rubric rows: {len(key.get('rubric', []))}")
print()
if warnings:
    print(f"--- {len(warnings)} warning(s) ---")
    for w in warnings: print("  WARN:", w)
    print()
if errors:
    print(f"--- {len(errors)} ERROR(S) ---")
    for e in errors: print("  ERROR:", e)
    sys.exit(1)
print("ALL CHECKS PASSED")
