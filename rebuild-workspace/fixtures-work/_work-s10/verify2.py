#!/usr/bin/env python3
"""Second, independent verification pass for s10-support-checkin.

Deliberately written separately from check.py, with the field list re-typed from
the brief and different quote-matching logic, so a mistake in one is unlikely to
be repeated in the other. Adds checks check.py does not make:

  * every HH:MM:SS timestamp cited in a note exists in the s1 or s3 transcript
    (the carried-forward citations);
  * rubric criterion names match the method spec exactly (R names, per-pain
    check names, support-call rows);
  * objection "type" values are spec objection names;
  * "decision_role" values are spec role vocabulary;
  * every met/partial row either carries evidence or explains itself;
  * quotes are attributed to the speaker who actually said them.
"""
import json
import re
import sys

S10 = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s10-support-checkin"
S1T = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s1-discovery-strong/transcript.txt"
S3T = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s3-followup-demo-feedback/transcript.txt"

# Re-typed from the brief, not imported from check.py.
EXPECTED_FIELDS = """scenario_id call_type purpose_of_this_fixture transcript_format company
attendees expected_monday_products rubric pains numbers vocabulary entities_and_workflows
integrations_mentioned compliance_or_security_signals objections commitments_and_next_steps
traps requested_changes should_plugin_propose_a_build expected_questions_before_building
expected_verdict account_context expected_structures accepted_behaviours
expected_leak_blocklist""".split()

R_NAMES = [
    "R1 Current state mapped", "R2 Pain made concrete", "R3 Why now", "R4 Bleed number",
    "R5 Upside number", "R6 Desired outcome", "R7 Decision process mapped",
    "R8 Priority and timing", "R9 Blockers surfaced", "R10 Next step committed",
    "R11 Solution confirmed", "R12 Scope agreed verbally",
]
PAIN_CHECKS = ["Stated", "Concrete", "Workaround", "Reach", "Cost inputs", "Trajectory"]
OBJECTION_NAMES = {
    "Price feels high", "Needs to think it over", "Must check with someone",
    "Wrong time, next quarter", "We'll build it ourselves", "Talking to other partners",
    "Just send a proposal or pricing", "monday itself is the problem", "Team won't adopt it",
}
DECISION_ROLES = {"approver", "influencer", "admin/owner", "end user", "not applicable"}

fails = []


def bad(m):
    fails.append(m)


key = json.load(open(S10 + "/answer-key.json", encoding="utf-8"))
tlines = open(S10 + "/transcript.txt", encoding="utf-8").read().rstrip("\n").split("\n")
s1 = open(S1T, encoding="utf-8").read()
s3 = open(S3T, encoding="utf-8").read()

# 1. field set and order, re-derived
if list(key) != EXPECTED_FIELDS:
    bad("field order mismatch:\n  got      %s\n  expected %s" % (list(key), EXPECTED_FIELDS))
print("fields: %d, order %s" % (len(key), "OK" if list(key) == EXPECTED_FIELDS else "WRONG"))

# 2. build a line index the other way round: speaker + text per line
parsed = []
for i, line in enumerate(tlines, 1):
    if ": " not in line:
        bad("L%d has no 'Speaker: text' separator" % i)
        parsed.append((i, "", ""))
        continue
    sp, txt = line.split(": ", 1)
    parsed.append((i, sp, txt))
print("transcript lines: %d, speakers: %s" % (len(parsed), sorted({p[1] for p in parsed})))

# 3. every quote, matched against the spoken text only (not the speaker label)
quotes = []


def collect(node, path):
    if isinstance(node, dict):
        if "quote" in node:
            quotes.append((path, node["quote"], node.get("location")))
        for k, v in node.items():
            collect(v, path + "." + k)
    elif isinstance(node, list):
        for n, v in enumerate(node):
            collect(v, "%s[%d]" % (path, n))


collect(key, "key")
ok = nulls = 0
for path, q, loc in quotes:
    if q is None:
        nulls += 1
        continue
    owners = [(i, sp) for i, sp, txt in parsed if q in txt]
    if len(owners) != 1:
        bad("%s: quote matches %d spoken lines: %r" % (path, len(owners), q[:80]))
        continue
    line_no, speaker = owners[0]
    ok += 1
    if loc is None:
        continue
    m = re.fullmatch(r"L(\d+), (Consultant|Jordan Pruitt \(Operations Manager\))", loc)
    if not m:
        bad("%s: malformed location %r" % (path, loc))
        continue
    if int(m.group(1)) != line_no:
        bad("%s: location L%s but quote is on L%d" % (path, m.group(1), line_no))
    if not m.group(2).startswith(speaker):
        bad("%s: location attributes to %r, line spoken by %r" % (path, m.group(2), speaker))
print("quotes: %d verified against spoken text, %d nulls" % (ok, nulls))

# 4. carried-forward citations must exist in the s1 or s3 transcripts
cited = set()
for m in re.finditer(r"\b(\d{2}:\d{2}:\d{2})\b", json.dumps(key)):
    cited.add(m.group(1))
for ts in sorted(cited):
    if ("[%s]" % ts) not in s1 and ("(%s)" % ts) not in s3:
        bad("cited timestamp %s is in neither the s1 nor the s3 transcript" % ts)
print("cross-fixture timestamps cited: %d, all resolvable: %s"
      % (len(cited), "yes" if not any("timestamp" in f for f in fails) else "NO"))

# 5. rubric naming, statuses, evidence discipline
support = [r for r in key["rubric"] if r["criterion"].startswith("Support check")]
rrows = [r for r in key["rubric"] if re.match(r"^R\d+ ", r["criterion"])]
prows = [r for r in key["rubric"] if re.match(r"^P\d+ ", r["criterion"])]
if len(support) != 5:
    bad("expected 5 support-call rows, found %d" % len(support))
for n, r in enumerate(support, 1):
    if not r["criterion"].startswith("Support check %d " % n):
        bad("support row %d misnamed: %r" % (n, r["criterion"]))
if [r["criterion"] for r in rrows] != R_NAMES:
    bad("R rows do not match the spec names in order: %s" % [r["criterion"] for r in rrows])
for r in prows:
    m = re.fullmatch(r"(P\d+) (.+)", r["criterion"])
    if not m or m.group(2) not in PAIN_CHECKS:
        bad("per-pain row misnamed: %r" % r["criterion"])
if len(prows) != 6:
    bad("expected 6 per-pain rows for the one new pain, found %d" % len(prows))
for r in key["rubric"]:
    if r["status"] not in {"met", "partial", "missing"}:
        bad("%s: bad status %r" % (r["criterion"], r["status"]))
    if r["status"] in {"met", "partial"} and not r["evidence"]:
        if not re.match(r"^(Carried forward|Met since|Carried)", r["note"]):
            bad("%s: %s with no evidence and no carried-forward note" % (r["criterion"], r["status"]))
    if r["status"] == "missing" and r["evidence"]:
        bad("%s: missing but carries evidence" % r["criterion"])
print("rubric rows: %d (%d support, %d R, %d per-pain)"
      % (len(key["rubric"]), len(support), len(rrows), len(prows)))

# 6. vocabularies
for o in key["objections"]:
    if o["type"] not in OBJECTION_NAMES:
        bad("objection type not a spec name: %r" % o["type"])
for a in key["attendees"]:
    if a["decision_role"] not in DECISION_ROLES:
        bad("decision_role not spec vocabulary: %r" % a["decision_role"])
    if a["side"] not in {"client", "consultant"}:
        bad("bad side: %r" % a["side"])

# 7. the scenario's own invariants
if key["call_type"] != "support-checkin":
    bad("call_type should be support-checkin")
if key["should_plugin_propose_a_build"] is not False:
    bad("should_plugin_propose_a_build must be false for this scenario")
if key["requested_changes"] != []:
    bad("requested_changes must be empty: the issue was user error")
if key["expected_structures"]["portfolio_expected"] is not False:
    bad("portfolio_expected must be false")
for k in ("bleed", "upside"):
    if key["numbers"][k]["status"] != "met" or key["numbers"][k]["quote"] is not None:
        bad("numbers.%s should be met with a null quote (carried from s1)" % k)
gates = key["expected_verdict"]["gates_met"] + key["expected_verdict"]["gates_not_met"]
for stage in ("Solution blueprint", "Build", "First demo (v0.1)",
              "Pricing or proposal prep", "v1.0 sign-off"):
    if sum(1 for g in gates if g.startswith(stage)) != 1:
        bad("stage %r not listed exactly once" % stage)
if any(ord(c) > 127 for c in json.dumps(key, ensure_ascii=False)):
    bad("answer key contains non-ASCII characters")

print("\n" + "=" * 58)
if fails:
    print("SECOND PASS FAILED: %d problem(s)" % len(fails))
    for f in fails:
        print("  - %s" % f)
    sys.exit(1)
print("SECOND PASS CLEAN: %d quotes, %d rubric rows, %d cited timestamps resolved"
      % (ok, len(key["rubric"]), len(cited)))
