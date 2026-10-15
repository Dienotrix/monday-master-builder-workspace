#!/usr/bin/env python3
"""Fixture checker for s10-support-checkin (and a cross-check for the other keys).

Checks:
  1. answer-key.json is valid JSON and ASCII-only; transcript.txt is ASCII-only.
  2. The 25 top-level fields are all present, in the required order, with no extras.
  3. Nested shapes: exact key sets for every object in every list/dict field.
  4. Every "quote" anywhere in the key is an exact substring of transcript.txt,
     occurs exactly once, and sits on exactly one line. Nulls are skipped.
  5. For keys whose locations are "L<n>, Name (role)": the line number matches the
     line the quote is on, and the speaker in the location matches that line's speaker.
  6. rubric statuses are lowercase met / partial / missing.
  7. expected_verdict lists all five spec stage names exactly once across
     gates_met + gates_not_met.

Usage:
  python3 check.py                # checks s10 (strict, including locations)
  python3 check.py --all          # also quote/order-checks s1, s2, s3, s4, s5
"""
import json
import os
import re
import sys

FIXTURES = "/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"

FIELD_ORDER = [
    "scenario_id",
    "call_type",
    "purpose_of_this_fixture",
    "transcript_format",
    "company",
    "attendees",
    "expected_monday_products",
    "rubric",
    "pains",
    "numbers",
    "vocabulary",
    "entities_and_workflows",
    "integrations_mentioned",
    "compliance_or_security_signals",
    "objections",
    "commitments_and_next_steps",
    "traps",
    "requested_changes",
    "should_plugin_propose_a_build",
    "expected_questions_before_building",
    "expected_verdict",
    "account_context",
    "expected_structures",
    "accepted_behaviours",
    "expected_leak_blocklist",
]

CALL_TYPES = {"discovery", "follow-up-demo-feedback", "intro", "support-checkin"}
STATUSES = {"met", "partial", "missing"}
GATES = [
    "Solution blueprint",
    "Build",
    "First demo (v0.1)",
    "Pricing or proposal prep",
    "v1.0 sign-off",
]

SHAPES = {
    "company": {"name", "industry", "size", "locations", "current_tools"},
    "attendees": {"name", "role", "side", "decision_role"},
    "expected_monday_products": {"kind", "why"},
    "rubric": {"criterion", "status", "evidence", "note"},
    "evidence": {"quote", "location"},
    "pains": {"quote", "location", "theme"},
    "vocabulary": {"their_term", "meaning", "likely_monday_object"},
    "objections": {"quote", "type"},
    "commitments_and_next_steps": {"quote", "what", "owner", "date"},
    "requested_changes": {"type", "description", "quote"},
    "expected_verdict": {"verdict", "gates_met", "gates_not_met", "note"},
    "account_context": {"tier", "products_enabled", "existing_monday_setup",
                        "evidence_quote_or_null"},
    "expected_structures": {"native_boards_required", "portfolio_expected",
                            "portfolio_reason", "lookalike_traps", "notes"},
    "native_boards_required": {"product", "entity", "why"},
    "numbers_entry": {"value", "quote", "status"},
}

errors = []
notes = []


def err(msg):
    errors.append(msg)


def check_shape(label, obj, expected):
    if not isinstance(obj, dict):
        err("%s: expected an object, got %s" % (label, type(obj).__name__))
        return
    got = set(obj.keys())
    if got != expected:
        missing = sorted(expected - got)
        extra = sorted(got - expected)
        if missing:
            err("%s: missing keys %s" % (label, missing))
        if extra:
            err("%s: unexpected keys %s" % (label, extra))


def walk_quotes(node, path, out):
    """Collect (path, quote, location_or_None) for every dict carrying a 'quote'."""
    if isinstance(node, dict):
        if "quote" in node:
            out.append((path, node["quote"], node.get("location")))
        for k, v in node.items():
            walk_quotes(v, "%s.%s" % (path, k), out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_quotes(v, "%s[%d]" % (path, i), out)


def check_fixture(folder, strict_locations):
    global errors
    kp = os.path.join(FIXTURES, folder, "answer-key.json")
    tp = os.path.join(FIXTURES, folder, "transcript.txt")
    print("\n=== %s ===" % folder)

    raw_key = open(kp, encoding="utf-8").read()
    transcript = open(tp, encoding="utf-8").read()

    for label, text in (("answer-key.json", raw_key), ("transcript.txt", transcript)):
        bad = sorted({c for c in text if ord(c) > 127})
        if bad:
            msg = "%s/%s: non-ASCII characters %r" % (folder, label, bad)
            if folder == "s4-discovery-software":
                # COVERAGE.md documents s4 as deliberately UTF-8 ("Krakow" with an accent).
                notes.append(msg + " -- documented as intentional in COVERAGE.md, not a failure")
            else:
                err(msg)

    try:
        key = json.loads(raw_key)
    except Exception as e:
        err("answer-key.json: invalid JSON: %s" % e)
        return
    print("JSON valid: yes")

    # --- field set and order ---
    got = list(key.keys())
    if got != FIELD_ORDER:
        missing = [f for f in FIELD_ORDER if f not in got]
        extra = [f for f in got if f not in FIELD_ORDER]
        if missing:
            err("top level: missing fields %s" % missing)
        if extra:
            err("top level: unexpected fields %s" % extra)
        if not missing and not extra:
            err("top level: fields present but out of order:\n  got      %s\n  expected %s"
                % (got, FIELD_ORDER))
    else:
        print("Field set and order: all %d fields correct" % len(FIELD_ORDER))

    if key.get("call_type") not in CALL_TYPES:
        err("call_type: %r is not one of %s" % (key.get("call_type"), sorted(CALL_TYPES)))
    if not isinstance(key.get("should_plugin_propose_a_build"), bool):
        err("should_plugin_propose_a_build: must be a boolean")

    # --- nested shapes ---
    check_shape("company", key.get("company"), SHAPES["company"])
    for i, a in enumerate(key.get("attendees", [])):
        check_shape("attendees[%d]" % i, a, SHAPES["attendees"])
    for i, p in enumerate(key.get("expected_monday_products", [])):
        check_shape("expected_monday_products[%d]" % i, p, SHAPES["expected_monday_products"])
    for i, r in enumerate(key.get("rubric", [])):
        check_shape("rubric[%d]" % i, r, SHAPES["rubric"])
        if isinstance(r, dict):
            if r.get("status") not in STATUSES:
                err("rubric[%d] (%s): status %r not in %s"
                    % (i, r.get("criterion"), r.get("status"), sorted(STATUSES)))
            for j, e in enumerate(r.get("evidence", [])):
                check_shape("rubric[%d].evidence[%d]" % (i, j), e, SHAPES["evidence"])
    for i, p in enumerate(key.get("pains", [])):
        check_shape("pains[%d]" % i, p, SHAPES["pains"])
    nums = key.get("numbers", {})
    if set(nums.keys()) != {"bleed", "upside"}:
        err("numbers: expected exactly bleed and upside, got %s" % sorted(nums.keys()))
    for k in ("bleed", "upside"):
        if k in nums:
            check_shape("numbers.%s" % k, nums[k], SHAPES["numbers_entry"])
            if nums[k].get("status") not in STATUSES:
                err("numbers.%s: status %r not in %s" % (k, nums[k].get("status"), sorted(STATUSES)))
    for i, v in enumerate(key.get("vocabulary", [])):
        check_shape("vocabulary[%d]" % i, v, SHAPES["vocabulary"])
    for i, o in enumerate(key.get("objections", [])):
        check_shape("objections[%d]" % i, o, SHAPES["objections"])
    for i, c in enumerate(key.get("commitments_and_next_steps", [])):
        check_shape("commitments_and_next_steps[%d]" % i, c, SHAPES["commitments_and_next_steps"])
    for i, c in enumerate(key.get("requested_changes", [])):
        check_shape("requested_changes[%d]" % i, c, SHAPES["requested_changes"])
        if isinstance(c, dict) and c.get("type") not in {"add", "change", "remove"}:
            err("requested_changes[%d]: type %r not add/change/remove" % (i, c.get("type")))
    check_shape("expected_verdict", key.get("expected_verdict"), SHAPES["expected_verdict"])
    check_shape("account_context", key.get("account_context"), SHAPES["account_context"])
    es = key.get("expected_structures", {})
    check_shape("expected_structures", es, SHAPES["expected_structures"])
    for i, b in enumerate(es.get("native_boards_required", [])):
        check_shape("expected_structures.native_boards_required[%d]" % i, b,
                    SHAPES["native_boards_required"])

    for f in ("entities_and_workflows", "integrations_mentioned",
              "compliance_or_security_signals", "traps",
              "expected_questions_before_building", "accepted_behaviours",
              "expected_leak_blocklist"):
        v = key.get(f)
        if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
            err("%s: must be a list of strings" % f)

    # --- gates ---
    ev = key.get("expected_verdict", {})
    if isinstance(ev, dict):
        gates = list(ev.get("gates_met", [])) + list(ev.get("gates_not_met", []))
        for g in GATES:
            hits = [x for x in gates if x.startswith(g)]
            if len(hits) != 1:
                err("expected_verdict: stage %r appears %d times across gates_met/gates_not_met"
                    % (g, len(hits)))
        for x in gates:
            if not any(x.startswith(g) for g in GATES):
                err("expected_verdict: gate entry does not start with a spec stage name: %r" % x)

    # --- quotes ---
    lines = transcript.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    found = []
    walk_quotes(key, "key", found)
    checked = 0
    skipped = 0
    for path, quote, location in found:
        if quote is None:
            skipped += 1
            continue
        if not isinstance(quote, str) or not quote:
            err("%s: quote is not a non-empty string" % path)
            continue
        count = transcript.count(quote)
        if count == 0:
            err("%s: quote NOT FOUND in transcript: %r" % (path, quote[:90]))
            continue
        if count > 1:
            err("%s: quote occurs %d times (must be unique): %r" % (path, count, quote[:90]))
        hits = [n for n, line in enumerate(lines, 1) if quote in line]
        if not hits:
            err("%s: quote spans more than one line: %r" % (path, quote[:90]))
            continue
        if len(hits) > 1:
            err("%s: quote appears on lines %s" % (path, hits))
        checked += 1
        if strict_locations and location is not None:
            m = re.match(r"^L(\d+), (.+)$", location)
            if not m:
                err("%s: location %r does not match 'L<n>, Name (role)'" % (path, location))
                continue
            n, who = int(m.group(1)), m.group(2)
            if n != hits[0]:
                err("%s: location says L%d but the quote is on line %d" % (path, n, hits[0]))
            speaker = lines[hits[0] - 1].split(":", 1)[0]
            if not who.startswith(speaker):
                err("%s: location speaker %r does not match line speaker %r"
                    % (path, who, speaker))
    print("Quotes checked: %d exact-substring hits (%d nulls skipped)" % (checked, skipped))
    if strict_locations:
        print("Locations checked: line number + speaker for every quote that has one")
    return checked


def main():
    do_all = "--all" in sys.argv
    total = check_fixture("s10-support-checkin", strict_locations=True)
    if do_all:
        for f in ("s1-discovery-strong", "s2-discovery-gaps",
                  "s3-followup-demo-feedback", "s4-discovery-software", "s5-intro-thin"):
            if os.path.isdir(os.path.join(FIXTURES, f)):
                check_fixture(f, strict_locations=False)
    print("\n" + "=" * 60)
    if errors:
        print("FAILED: %d problem(s)" % len(errors))
        for e in errors:
            print("  - %s" % e)
        sys.exit(1)
    print("ALL CHECKS PASSED (s10 quotes verified: %s)" % total)
    for n in notes:
        print("  note: %s" % n)


if __name__ == "__main__":
    main()
