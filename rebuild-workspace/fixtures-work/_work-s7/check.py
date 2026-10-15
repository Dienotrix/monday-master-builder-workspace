#!/usr/bin/env python3
"""Validity, field-order, shape, quote and location check for the s7 answer key (SRT transcript)."""
import json
import re
import sys

BASE = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s7-discovery-service-desk/"
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
    if p["kind"] not in ("core", "crm", "service", "software"):
        bad(f"expected_monday_products[{i}] kind: {p['kind']}")
for i, r in enumerate(k["rubric"]):
    if set(r) != {"criterion", "status", "evidence", "note"}:
        bad(f"rubric[{i}] keys: {list(r)}")
for i, p in enumerate(k["pains"]):
    if set(p) != {"quote", "location", "theme"}:
        bad(f"pains[{i}] keys: {list(p)}")
for i, v in enumerate(k["vocabulary"]):
    if set(v) != {"their_term", "meaning", "likely_monday_object"}:
        bad(f"vocabulary[{i}] keys: {list(v)}")
for i, o in enumerate(k["objections"]):
    if set(o) != {"quote", "type"}:
        bad(f"objections[{i}] keys: {list(o)}")
for i, c in enumerate(k["commitments_and_next_steps"]):
    if set(c) != {"quote", "what", "owner", "date"}:
        bad(f"commitments[{i}] keys: {list(c)}")
for i, c in enumerate(k["requested_changes"]):
    if set(c) != {"type", "description", "quote"}:
        bad(f"requested_changes[{i}] keys: {list(c)}")
    if c["type"] not in ("add", "change", "remove"):
        bad(f"bad change type: {c['type']}")
if set(k["numbers"]) != {"bleed", "upside"}:
    bad("numbers keys")
for side in ("bleed", "upside"):
    if set(k["numbers"][side]) != {"value", "quote", "status"}:
        bad(f"numbers.{side} keys: {list(k['numbers'][side])}")
    if k["numbers"][side]["status"] not in ("met", "partial", "missing"):
        bad(f"bad numbers status {side}")
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
if not isinstance(k["should_plugin_propose_a_build"], bool):
    bad("should_plugin_propose_a_build is not a boolean")
for f in ("accepted_behaviours", "expected_leak_blocklist", "traps",
          "expected_questions_before_building", "entities_and_workflows", "integrations_mentioned",
          "compliance_or_security_signals"):
    if not (isinstance(k[f], list) and k[f] and all(isinstance(x, str) and x.strip() for x in k[f])):
        bad(f"{f} is not a non-empty list of non-empty strings")
print("scenario id ok:", k["scenario_id"] == "s7-discovery-service-desk")
print("call_type ok:", k["call_type"] == "discovery")
print("build flag:", k["should_plugin_propose_a_build"])
print("portfolio_expected:", k["expected_structures"]["portfolio_expected"])
print("counts: traps", len(k["traps"]), "| questions", len(k["expected_questions_before_building"]),
      "| accepted_behaviours", len(k["accepted_behaviours"]),
      "| leak_blocklist", len(k["expected_leak_blocklist"]),
      "| objections", len(k["objections"]), "| pains", len(k["pains"]),
      "| vocabulary", len(k["vocabulary"]),
      "| native_boards", len(k["expected_structures"]["native_boards_required"]),
      "| lookalike_traps", len(k["expected_structures"]["lookalike_traps"]),
      "| commitments", len(k["commitments_and_next_steps"]),
      "| requested_changes", len(k["requested_changes"]))

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
    if not r["note"].strip():
        bad(f"empty note: {r['criterion']}")
# per-pain blocks complete and in order
pain_rows = [n for n in names[12:]]
pains_seen = []
for n in pain_rows:
    pid = n.split()[0]
    if pid not in pains_seen:
        pains_seen.append(pid)
for pid in pains_seen:
    got = [n.split(" ", 1)[1] for n in pain_rows if n.startswith(pid + " ")]
    if got != P:
        bad(f"{pid} per-pain checks not the six in order: {got}")
print("per-pain blocks:", pains_seen, "each with all six checks in order")
excavated = []
for pid in pains_seen:
    st = {r["criterion"].split(" ", 1)[1]: r["status"] for r in k["rubric"]
          if r["criterion"].startswith(pid + " ")}
    if all(st.get(c) == "met" for c in ("Stated", "Concrete", "Workaround")):
        excavated.append(pid)
print("excavated pains (S+C+W met):", excavated)
r2 = [r["status"] for r in k["rubric"] if r["criterion"] == "R2 Pain made concrete"][0]
if excavated and r2 != "met":
    bad(f"a pain is excavated but R2 is {r2}")
if not excavated and r2 == "met":
    bad("R2 met but no pain is excavated")

# ---------------------------------------------------------------- verdict and gates
core = {r["criterion"]: r["status"] for r in k["rubric"]}
vals = [core["R2 Pain made concrete"], core["R3 Why now"], core["R4 Bleed number"],
        core["R7 Decision process mapped"]]
want = "Not ready" if "missing" in vals else ("Nearly ready" if "partial" in vals else "Discovery complete")
print("verdict rule:", want, "| key says:", k["expected_verdict"]["verdict"], "| R2/R3/R4/R7 =", vals)
if want != k["expected_verdict"]["verdict"]:
    bad(f"verdict {k['expected_verdict']['verdict']!r} does not match the rule ({want})")
STAGES = ["Solution blueprint", "Build", "First demo (v0.1)", "Pricing or proposal prep",
          "v1.0 sign-off"]
entries = k["expected_verdict"]["gates_met"] + k["expected_verdict"]["gates_not_met"]
for s in STAGES:
    n = sum(1 for e in entries if e.startswith(s))
    if n != 1:
        bad(f"stage {s!r} appears {n} times across gates_met/gates_not_met")
if len(entries) != 5:
    bad(f"gates list has {len(entries)} entries, expected 5")
print("all five stage gates present exactly once:",
      all(sum(1 for e in entries if e.startswith(s)) == 1 for s in STAGES))

# ---------------------------------------------------------------- spec vocabularies
SPEC_OBJECTIONS = ["Price feels high", "Needs to think it over", "Must check with someone",
                   "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
                   "Just send a proposal or pricing", "monday itself is the problem",
                   "Team won't adopt it"]
for o in k["objections"]:
    if not any(o["type"].startswith(s) for s in SPEC_OBJECTIONS):
        bad(f"objection type not a spec name: {o['type'][:70]}")
print("objection types all spec names:",
      all(any(o["type"].startswith(s) for s in SPEC_OBJECTIONS) for o in k["objections"]))
SPEC_ROLES = ["approver", "influencer", "admin/owner", "end user", "not applicable"]
for a in k["attendees"]:
    if not any(a["decision_role"].startswith(s) for s in SPEC_ROLES):
        bad(f"decision_role not spec vocabulary: {a['name']}: {a['decision_role'][:60]}")
print("decision roles all spec vocabulary:",
      all(any(a["decision_role"].startswith(s) for s in SPEC_ROLES) for a in k["attendees"]))
for a in k["attendees"]:
    if a["side"] not in ("client", "consultant"):
        bad(f"bad side for {a['name']}: {a['side']}")

# ---------------------------------------------------------------- parse SRT
cues = {}
order = []
for chunk in re.split(r"\n\s*\n", t):
    lines = [l for l in chunk.splitlines() if l.strip()]
    if not lines:
        continue
    if len(lines) >= 3 and re.match(r"^\d+$", lines[0]) and "-->" in lines[1]:
        num = int(lines[0])
        tl = lines[1]
        if not re.match(r"^\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}$", tl):
            bad(f"cue {num}: malformed timing line {tl!r}")
        start, end = [x.strip() for x in tl.split("-->")]
        text = " ".join(lines[2:])
        if ":" not in text:
            bad(f"cue {num}: no speaker label in cue text")
        cues[num] = (start, end, text.split(":", 1)[0], text)
        order.append(num)
    else:
        bad(f"unparsable block: {lines[0][:50]!r}")
print("cues parsed:", len(cues), "| numbering contiguous from 1:", order == list(range(1, len(cues) + 1)))


def to_ms(s):
    h, m, rest = s.split(":")
    sec, ms = rest.split(",")
    return ((int(h) * 60 + int(m)) * 60 + int(sec)) * 1000 + int(ms)


mono = True
prev_end = -1
for num in order:
    s, e, _, _ = cues[num]
    if to_ms(s) < prev_end or to_ms(e) <= to_ms(s):
        mono = False
        bad(f"cue {num}: timings not monotonic / non-positive duration")
    prev_end = to_ms(e)
print("timings monotonic and positive:", mono)
print("duration:", cues[order[-1]][1] if order else "n/a")
SPEAKERS = {"Consultant", "Yvette Carnahan", "Tansy Whitlock", "Curtis Vandergrift"}
unknown = {cues[n][2] for n in order} - SPEAKERS
if unknown:
    bad(f"unexpected speaker labels: {unknown}")

words = sum(len(re.findall(r"[A-Za-z0-9']+", cues[n][3].split(":", 1)[1])) for n in order)
cw = sum(len(re.findall(r"[A-Za-z0-9']+", cues[n][3].split(":", 1)[1])) for n in order
         if cues[n][2] != "Consultant")
print(f"spoken words: {words} | client talk share: {100.0*cw/words:.1f}%")

# ---------------------------------------------------------------- quotes and locations
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
n = bad_q = multi = 0
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
    hits = [num for num in order if q in cues[num][3]]
    if not hits:
        bad(f"spans cues (not inside one cue): {path} {q!r}")
        bad_q += 1
        continue
    if len(hits) > 1:
        multi += 1
        print("note: quote matches several cues", hits, path, repr(q[:50]))
    if loc is not None:
        start, _, sp, _ = cues[hits[0]]
        want_loc = f"cue {hits[0]}, {start}, {sp}"
        if loc != want_loc:
            bad(f"LOC MISMATCH: {path} {q[:40]!r} key={loc!r} actual={want_loc!r}")
print(f"quotes checked: {n}, not found or invalid: {bad_q}, multi-cue: {multi}")

# quotes that need a location must have one
for path, q, loc in quotes:
    if isinstance(q, str) and loc is None and ".evidence[" in path:
        bad(f"evidence quote without a location: {path}")

# ---------------------------------------------------------------- verbatim fragments cited in prose
VERBATIM = [
    "work order", "request", "PM", "preventive maintenance", "the whiteboard is the truth",
    "ServiceChannel", "Fairlane", "Brightmoor", "Sage 300", "the service inbox", "legal pad",
    "Standard, I think? Whatever the middle one is", "we tried monday two years ago and it didn't stick",
    "It'll be full of dead work orders from back then", "just under a fifth of our book",
    "six clinics", "sixty-six hours", "ninety-day performance plan", "second week of December",
    "renews in January", "Three hours each", "an hour a day each", "Seven, with me",
    "I'd guess thirty-five all in", "a hundred and eighteen thousand", "two hundred and forty hours",
    "Let me get the real one from him", "eleven buildings", "monthly response-time reporting",
    "I'm not going to invent one for you", "ugly and working in December",
    "Wednesday's usually clear for me. The twenty-third", "three times to choose from",
    "over ten thousand he signs", "he'll want that second part in writing",
    "I could probably put most of this together myself", "don't design it for a desk",
    "Dewey", "badging", "anything about patients or which room", "outside vendors",
    "add a column without calling a consultant", "they'll go back to the spreadsheet",
    "Microsoft sign-in", "half of them haven't got a company email address",
    "the portal work isn't optional", "we don't get paid", "four hundred-ish a week",
    "That's not counting PMs", "About half and half", "Roanoke came in through an acquisition",
    "four months", "the binder", "Corinne", "I don't want to guess at it",
    "That's the first cut, yeah", "Don't hold me to the wording until Pete's heard it",
    "I never know if you've got it", "ninety-four percent", "seventy-eight on theirs",
    "Call it twenty", "It's just always there", "Pete Odugbemi", "Hollis", "Rosalie", "Junie",
    "Delia", "Rob's got an inspections board", "estimating keeps a bid board",
    "I decide the tool", "answering service", "six-month implementation",
    "Don't hold me to that", "I'm not going to put a number on my own time",
    "a different animal from a call", "And the knowledge thing. Not first. But I'd want it.",
    "If we don't close it in their system, we don't get paid.",
    "it'll die the same way it died last time", "he has mentioned that to me more than once since",
    "I just can't do it this year", "they'll go back to the spreadsheet and I won't be able to stop them",
    "I could probably put most of this together myself, honestly",
    "Dewey is excellent, and Dewey does not answer his phone", "Rosalie hates it",
    "The girl before Rosalie quit, and she said the portal was part of why",
    "I don't think anybody's opened that since Corinne made it", "That was me on a Saturday",
    "I didn't know it existed for about a month",
    "The whiteboard is the truth. The spreadsheet is what we tell people.",
    "I couldn't defend either number in the room", "That's worse than being wrong",
    "the one that hurt", "a slide with our response times on it", "the request is the phone call",
    "Standard, I think? Whatever the middle one is. I'd have to look.",
    "Rob's got an inspections board he likes", "fifteen or twenty escalations a day",
    "Both go on the list, and I'll show you the list rather than keep it to myself.",
    "What I'll send you is a short recap of what I heard today in plain language",
    "Talk to Dewey. And don't design it for a desk.",
    "Take the footer off and take the name off and it's fine.", "I can get all that today.",
    "I'll ask him tomorrow.", "Yes. I'll come back to you tomorrow or Thursday.",
    "Can it be ugly and working in December and pretty afterwards?",
    "Not typing the client and the building and the contact every single time",
    "Yeah. I'd want Microsoft sign-in.", "the dispatcher hasn't got a ServiceChannel login",
    "every little change is a ticket to me", "nobody asked the help desk",
    "Nobody used it after about six weeks", "half eleven",
]
cited_bad = 0
raw_l, t_l = raw.lower(), t.lower()
for f in [x.lower() for x in VERBATIM]:
    if f in raw_l and f not in t_l:
        bad(f"prose cites a fragment that is NOT in the transcript: {f!r}")
        cited_bad += 1
print(f"verbatim fragments cited in prose: {sum(1 for f in VERBATIM if f in raw)} cited, {cited_bad} wrong")

# ---------------------------------------------------------------- misc hygiene
for tok in ('"AUTO"', "NOT FOUND", "TODO", "FIXME"):
    if tok in raw:
        bad(f"placeholder left in key: {tok}")
print("non-ascii in key:", sorted({c for c in raw if ord(c) > 127}))
print("non-ascii in transcript:", sorted({c for c in t if ord(c) > 127}))
for w in ("DelOps", "the user", "monday-master-builder"):
    if w in raw:
        bad(f"neutrality: {w!r} appears in the key")
    if w in t:
        bad(f"neutrality: {w!r} appears in the transcript")
if "|||" in t:
    bad("cue-split marker ||| left in the transcript")
def need(cond, msg):
    if not cond:
        bad(msg)


# ------------------------------------------------- client vocabulary must really be the client's
# Every their_term variant has to appear in the transcript, unless the entry itself says the term
# was never named on the call. This is the check that catches invented client vocabulary, such as
# a 'P1, P2, P3' priority-code scheme the client never used.
vocab_bad = 0
for v in k["vocabulary"]:
    if "never named as a term on this call" in v["meaning"].lower():
        continue
    for variant in v["their_term"].split("/"):
        var = variant.strip()
        for art in ("the ", "a ", "an "):
            if var.lower().startswith(art):
                var = var[len(art):]
        if var and var.lower() not in t_l:
            bad(f"vocabulary term claimed as the client's own is NOT in the transcript: {var!r} "
                f"(entry {v['their_term']!r})")
            vocab_bad += 1
print("client vocabulary terms all present in transcript:", vocab_bad == 0)

# ------------------------------------------------- planted elements present and testable
traps_all = " ".join(k["traps"]).lower()
acc_all = " ".join(k["accepted_behaviours"]).lower()
leak_all = " ".join(k["expected_leak_blocklist"]).lower()
notes_all = k["expected_structures"]["notes"].lower()
look_all = " ".join(k["expected_structures"]["lookalike_traps"]).lower()

for term in ("portal", "email-to-ticket", "sla policy setup"):
    need(term in traps_all, f"deferred Service extra {term!r} is not named in traps")
    need(term in acc_all or term in notes_all,
         f"deferred Service extra {term!r} is not named in accepted_behaviours or notes")
need("backlog" in acc_all, "the backlog handling for the deferred extras is not an accepted behaviour")

need("work order" in look_all, "the look-alike 'Work Orders' board trap is not listed")
need("tracker" in look_all, "the abandoned work order tracker is not listed as a look-alike trap")
svc = [b for b in k["expected_structures"]["native_boards_required"]
       if b["product"] == "service" and "ticket" in b["entity"].lower()]
need(len(svc) >= 1, "no native Service Tickets board required in expected_structures")
need(any("work order" in (b["why"] + b["entity"]).lower() for b in svc),
     "the native Tickets board is not tied to the client's 'work order' label")

need(k["expected_structures"]["portfolio_expected"] is False, "portfolio_expected should be False")
need("enterprise" in k["expected_structures"]["portfolio_reason"].lower(),
     "portfolio_reason does not explain why the Enterprise default does not apply")

for name in ("monday itself is the problem", "We'll build it ourselves"):
    need(any(o["type"].startswith(name) for o in k["objections"]),
         f"the planted objection {name!r} is missing")

need(k["account_context"]["tier"].startswith("Standard"), "account tier should read Standard")
need(k["account_context"]["evidence_quote_or_null"] in t, "tier evidence quote is not in transcript")
need("plan" in traps_all and "automation action cap" in traps_all,
     "plan-limit consequences are not carried in traps")

for term in ("35", "65", "118", "240", "bleed", "upside", "objection"):
    need(term in leak_all, f"leak blocklist does not cover {term!r}")

# ------------------------------------------------- format, length and talk share match the brief
total_s = to_ms(cues[order[-1]][1]) / 1000.0
need(32 * 60 <= total_s <= 48 * 60,
     f"duration {total_s/60:.1f} min is outside 20% of the 40-minute brief")
need("srt" in k["transcript_format"].lower(), "transcript_format does not say SRT")
need(100.0 * cw / words >= 60.0, "client talk share is below the method's 60% target")
cons_cues = [(len(re.findall(r"[A-Za-z0-9']+", cues[n][3].split(":", 1)[1])), n)
             for n in order if cues[n][2] == "Consultant"]
longest_w, longest_n = max(cons_cues)
need(longest_w <= 225, f"a Consultant cue is {longest_w} words, over the 225-word proxy")
need(f"{longest_w} words (cue {longest_n})" in raw,
     f"the key's longest-Consultant-cue claim does not match the actual {longest_w} words "
     f"at cue {longest_n}")
print(f"duration: {total_s/60:.1f} min | longest Consultant cue: {longest_w} words (cue {longest_n})")

# ------------------------------------------------- deliberate artefacts still true, and evidence-free
need(cues[13][3] == cues[14][3], "cues 13 and 14 are no longer an identical duplicated pair")
need(cues[33][2] == "Tansy Whitlock", "cue 33 is no longer the mis-attributed cue the key describes")
need(t.count("[inaudible]") == 1 and "[inaudible]" in cues[234][3],
     "the single [inaudible] is no longer at cue 234")
artefact_cues = {13, 14, 33}
artefact_clean = True
for path, q, loc in quotes:
    if isinstance(q, str) and isinstance(loc, str):
        m = re.match(r"cue (\d+),", loc)
        if m and int(m.group(1)) in artefact_cues:
            bad(f"evidence sits on a deliberate transcript artefact: {loc} ({path})")
            artefact_clean = False
print("artefact cues 13, 14 and 33 carry no evidence:", artefact_clean)

print("\nRESULT:", "PASS" if not fail else f"{len(fail)} FAILURE(S)")
sys.exit(1 if fail else 0)
