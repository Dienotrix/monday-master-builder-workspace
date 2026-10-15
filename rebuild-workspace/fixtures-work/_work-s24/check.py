"""Read-only check of fixtures/s24-package: field order, every quote verbatim at its
cited location, quote-only strings and single-quoted prose spans inside one turn's text line,
counts for the README. Never writes.

Stricter than the first version: matches at word boundaries, refuses a quote-only string
that sits only in a header or Highlights line, scans single-quoted spans of three or more
words inside prose fields, and checks an inline '(rec-NNNN mm:ss)' citation that follows
such a span. Format descriptions, Highlights wording, objection type names and design
vocabulary are listed, not counted as failures; the leak block list is matched
case-insensitively because its entries are patterns."""
import json
import os
import re
import sys
from collections import Counter, defaultdict

F = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s24-package"
ORDER = ["scenario_id", "call_type", "purpose_of_this_fixture", "transcript_format", "company", "attendees",
         "expected_monday_products", "rubric", "pains", "numbers", "vocabulary", "entities_and_workflows",
         "integrations_mentioned", "compliance_or_security_signals", "objections", "commitments_and_next_steps",
         "traps", "requested_changes", "should_plugin_propose_a_build", "expected_questions_before_building",
         "expected_verdict", "account_context", "expected_structures", "accepted_behaviours",
         "expected_leak_blocklist"]
key = json.load(open(os.path.join(F, "answer-key.json"), encoding="utf-8"))
keys = list(key.keys())
print("field order ok:", keys[:25] == ORDER, "| extra:", keys[25:])

files = {}
label = re.compile(r"^(.+?) · (\d\d:\d\d)$")
for name in sorted(os.listdir(F)):
    if name.startswith("rec-") and name.endswith(".txt"):
        rid = name[:8]
        lines = open(os.path.join(F, name), encoding="utf-8").read().split("\n")
        turns = {}
        textlines = {}
        for i, ln in enumerate(lines[:-1]):
            m = label.match(ln)
            if m:
                turns[(m.group(1), m.group(2))] = (lines[i + 1], i + 2)
                textlines[i + 2] = (m.group(1), m.group(2), lines[i + 1])
        files[rid] = {"name": name, "lines": lines, "turns": turns, "textlines": textlines}
print("files:", {k: v["name"] for k, v in files.items()})

locre = re.compile(r"^(rec-\d{4}), (\d\d:\d\d) (.+?)(?: \(([^()]*)\))?$")
# quoted spans in prose that are not transcript turns, by design
NOT_TURNS = {"Speaker Name · mm:ss", "Notetaker (recording assistant)", "automatic, en-US; speaker labels from meeting accounts",
             "── Title ──", "rec-NNNN, mm:ss Speaker Name (role)", "listed, silent, presence unconfirmed", "turn off in monday",
             "Price feels high", "do not show"}


def wb(q, t, ci=False):
    """q occurs in t verbatim (case-insensitively when ci) at word boundaries."""
    if ci:
        q, t = q.lower(), t.lower()
    i = t.find(q)
    while i != -1:
        before = t[i - 1] if i > 0 else " "
        after = t[i + len(q)] if i + len(q) < len(t) else " "
        if not (before.isalnum() and q[0].isalnum()) and not (after.isalnum() and q[-1].isalnum()):
            return True
        i = t.find(q, i + 1)
    return False


def find_in_turns(q, ci=False):
    return [(rid, lno, who, ts) for rid, f in files.items() for lno, (who, ts, txt) in f["textlines"].items() if wb(q, txt, ci)]


def in_header(q):
    return [(rid, i + 1) for rid, f in files.items() for i, ln in enumerate(f["lines"]) if q in ln and (i + 1) not in f["textlines"]]


bad = []
listed = []
n_loc = n_only = 0
cited = defaultdict(set)


def walk(o, path):
    global n_loc, n_only
    if isinstance(o, dict):
        if "quote" in o and isinstance(o["quote"], str):
            q = o["quote"]
            if "location" in o and isinstance(o["location"], str):
                n_loc += 1
                m = locre.match(o["location"])
                if not m:
                    bad.append((path, "bad location form", o["location"]))
                else:
                    rid, ts, who, role = m.groups()
                    hit = files.get(rid, {}).get("turns", {}).get((who, ts))
                    if hit is None:
                        bad.append((path, "no such turn", o["location"]))
                    elif not wb(q, hit[0]):
                        bad.append((path, "quote not at location", o["location"], q[:70]))
                    else:
                        cited[rid].add(hit[1])
            else:
                n_only += 1
                hits = find_in_turns(q)
                if not hits:
                    bad.append((path, "quote-only string not in any turn text line", q[:70], in_header(q)))
                for rid, lno, who, ts in hits:
                    cited[rid].add(lno)
        for k, v in o.items():
            if k != "quote":
                walk(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, path + f"[{i}]")


walk(key, "")
eq = key["account_context"].get("evidence_quote_or_null")
if isinstance(eq, str):
    n_only += 1
    if not find_in_turns(eq):
        bad.append(("account_context/evidence_quote_or_null", "not in any turn", eq[:60]))

inline_re = re.compile(r"(?<![A-Za-z])'((?:[^']|'(?=[a-z]))+?)'(?![A-Za-z])")
cite_re = re.compile(r"^\s*[,;]?\s*\((rec-\d{4}),?((?: ?\d\d:\d\d,?)+)")
n_inline = n_inline_cited = 0


def walk_prose(o, path):
    global n_inline, n_inline_cited
    if isinstance(o, dict):
        for k, v in o.items():
            if k != "quote":
                walk_prose(v, path + "/" + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk_prose(v, path + f"[{i}]")
    elif isinstance(o, str):
        ci = path.startswith("/expected_leak_blocklist")
        for m in inline_re.finditer(o):
            span = m.group(1)
            if len(span.split()) < 3 or "..." in span:
                continue
            n_inline += 1
            if span in NOT_TURNS:
                listed.append((path, "not a turn by design", span[:60]))
                continue
            hits = find_in_turns(span, ci)
            if not hits:
                if in_header(span):
                    listed.append((path, "Highlights or header wording", span[:60]))
                else:
                    bad.append((path, "inline quoted span not in any turn", span[:80]))
                continue
            for rid, lno, who, ts in hits:
                cited[rid].add(lno)
            cm = cite_re.match(o[m.end():m.end() + 40])
            if cm:
                n_inline_cited += 1
                rid = cm.group(1)
                stamps = re.findall(r"\d\d:\d\d", cm.group(2))
                if not any(h[0] == rid and h[3] in stamps for h in hits):
                    bad.append((path, "inline citation does not match the span's turn", span[:60], rid, stamps))


walk_prose(key, "")
print(f"quotes with location: {n_loc}; quote-only: {n_only}; total structured: {n_loc + n_only}; "
      f"inline prose spans: {n_inline} ({n_inline_cited} with a citation); bad: {len(bad)}; listed, not turns: {len(listed)}")
for b in bad:
    print("   BAD", b)
if "--listed" in sys.argv:
    for b in listed:
        print("   listed", b)
if "--lines" in sys.argv:
    for rid, f in files.items():
        uncited = sorted(set(f["textlines"]) - cited[rid])
        print(f"{rid}: {len(f['textlines'])} turns, {len(cited[rid])} cited text lines, uncited: {uncited}")

# counts
rub = key["rubric"]
st = Counter(r["status"] for r in rub)
asked = Counter(bool(r.get("asked")) for r in rub)
has_asked = all("asked" in r for r in rub)
print("rubric rows:", len(rub), dict(st), "asked flags on all rows:", has_asked, "asked true/false:", asked[True], asked[False])
pains = sorted({r["criterion"].split()[0] for r in rub if r["criterion"].startswith("P")})
exc = []
for p in pains:
    s = {r["criterion"].split(" ", 1)[1]: r["status"] for r in rub if r["criterion"].startswith(p + " ")}
    if all(s.get(c) == "met" for c in ("Stated", "Concrete", "Workaround")):
        exc.append(p)
print("graded pains:", pains, "excavated:", exc, "| pains array:", len(key["pains"]))
obj = Counter(o["type"].split(" (")[0].split(":")[0].strip() for o in key["objections"])
print("objections:", len(key["objections"]), dict(obj))
print("traps:", len(key["traps"]), "| lookalike:", len(key["expected_structures"]["lookalike_traps"]),
      "| blocklist:", len(key["expected_leak_blocklist"]))
rc = Counter(r["type"] for r in key["requested_changes"])
print("requested changes:", dict(rc), "| commitments:", len(key["commitments_and_next_steps"]),
      "| questions:", len(key["expected_questions_before_building"]), "| vocab:", len(key["vocabulary"]),
      "| accepted:", len(key["accepted_behaviours"]), "| entities:", len(key["entities_and_workflows"]),
      "| integrations:", len(key["integrations_mentioned"]), "| compliance:", len(key["compliance_or_security_signals"]))
it = key["intake"]
print("intake: files", len(it["files"]), "| order", it["confirmed_order"], "| order evidence", len(it["order_evidence"]),
      "| ties", len(it["ties"]), "| second-hand", len(it["second_hand"]), "| conflicts", len(it["conflicts"]),
      "| forks", len(it["forks"]), "| not-conflicts", len(it["not_conflicts"]), "| relayed", len(it["relayed_statements"]),
      "| claims", len(it["claims_by_the_previous_seller"]), "| quarantine frames", len(it["quarantine"]),
      "| alias", len(it["alias_map"]), "| recognition errors", len(it.get("recognition_errors", [])),
      "| corrections", len(it["corrections_block_for_first_meeting"]), "| delivery notes", len(it["delivery_notes"]))
print("verdict:", key["expected_verdict"]["verdict"], "| build:", key["should_plugin_propose_a_build"],
      "| portfolio:", key["expected_structures"]["portfolio_expected"], "| native:", key["expected_structures"]["native_boards_required"])
raw = open(os.path.join(F, "answer-key.json"), encoding="utf-8").read()
print("key lines:", raw.count("\n"), "| transcript lines:", sum(len(f["lines"]) - 1 for f in files.values()))
low = raw.lower()
for w in ("consultant", "delops"):
    print(f"  word {w!r} in key:", low.count(w))
sys.exit(1 if bad else 0)
