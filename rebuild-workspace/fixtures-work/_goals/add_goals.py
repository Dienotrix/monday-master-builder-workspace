#!/usr/bin/env python3
"""add_goals.py - apply the goals pass to one fixture answer key, touching nothing else.

Usage
    python3 add_goals.py <fixture folder> <plan.json> [--dry-run]

plan.json
    {
      "goals": [ {"id": "G1", "goal": "...", "quote": "...", "location": "...",
                  "speaker_role": "...", "pains": ["P1"]} , ... ],
      "assumption_kinds": ["gap", "board-architecture", ...],   one per readiness.assumptions entry, in order
      "note_add": null or "one sentence appended to readiness.note (required when goals is empty)"
    }

What it does
    Inserts readiness.goals just before readiness.pains, adds "kind" and "state": "assumed" to every
    readiness.assumptions entry, moves readiness.verdict.cleared_for "none" to "not-yet", and appends
    note_add to readiness.note. Edits are textual, so the key keeps its own formatting. Afterwards it
    re-parses the key and proves that, with those additions taken back out, the key equals the original.
    Refuses a key that already has readiness.goals. Standard library only; Python 3.9 or later.
"""
import json
import sys

KINDS = {"gap", "call-type", "automation-condition", "board-architecture", "leaning"}
GOAL_FIELDS = ["id", "goal", "quote", "location", "speaker_role", "pains"]


def fail(msg):
    print("add_goals: " + msg, file=sys.stderr)
    sys.exit(1)


def find_key(text, key, start, end):
    """Index of '"key"' followed by ':' at the shallowest depth inside text[start:end]."""
    needle = json.dumps(key)
    depth, i, in_str = 0, start, False
    best = None
    while i < end:
        c = text[i]
        if in_str:
            if c == "\\":
                i += 2
                continue
            if c == '"':
                in_str = False
        else:
            if c == '"':
                if depth == 1 and text.startswith(needle, i):
                    j = i + len(needle)
                    while text[j] in " \t\r\n":
                        j += 1
                    if text[j] == ":":
                        best = i
                        break
                in_str = True
            elif c in "{[":
                depth += 1
            elif c in "}]":
                depth -= 1
        i += 1
    return best


def value_span(text, key_pos):
    """(start, end) of the JSON value that follows the key at key_pos."""
    j = text.index(":", key_pos) + 1
    while text[j] in " \t\r\n":
        j += 1
    _, end = json.JSONDecoder().raw_decode(text, j)
    return j, end


def line_indent(text, pos):
    ls = text.rfind("\n", 0, pos) + 1
    k = ls
    while text[k] in " \t":
        k += 1
    return text[ls:k]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if len(args) != 2:
        fail("usage: add_goals.py <fixture folder> <plan.json> [--dry-run]")
    key_path = args[0].rstrip("/") + "/answer-key.json"
    with open(key_path, encoding="utf-8") as fh:
        text = fh.read()
    with open(args[1], encoding="utf-8") as fh:
        plan = json.load(fh)
    original = json.loads(text)
    r = original.get("readiness")
    if not isinstance(r, dict):
        fail("no readiness block")
    if "goals" in r:
        fail("readiness.goals already present; refusing to apply twice")

    goals = plan.get("goals")
    kinds = plan.get("assumption_kinds")
    note_add = plan.get("note_add")
    if not isinstance(goals, list) or not isinstance(kinds, list):
        fail("plan needs goals[] and assumption_kinds[]")
    pain_ids = {p.get("id") for p in r.get("pains", [])}
    for n, g in enumerate(goals, 1):
        if list(g.keys()) != GOAL_FIELDS:
            fail("goal %d fields must be exactly %s in that order" % (n, GOAL_FIELDS))
        if g["id"] != "G%d" % n:
            fail("goal %d must have id G%d" % (n, n))
        for f in ("goal", "quote", "location", "speaker_role"):
            if not isinstance(g[f], str) or not g[f].strip():
                fail("goal %s: %s must be a non-empty string" % (g["id"], f))
        if not isinstance(g["pains"], list) or not set(g["pains"]) <= pain_ids:
            fail("goal %s: pains must be ids from readiness.pains (%s)" % (g["id"], sorted(pain_ids)))
    if not goals and not note_add:
        fail("an empty goals list needs note_add saying why")
    assumptions = r.get("assumptions", [])
    if len(kinds) != len(assumptions):
        fail("assumption_kinds has %d entries; readiness.assumptions has %d" % (len(kinds), len(assumptions)))
    bad = [k for k in kinds if k not in KINDS]
    if bad:
        fail("unknown assumption kinds %s; allowed %s" % (bad, sorted(KINDS)))

    # Locate the readiness object.
    rk = find_key(text, "readiness", 0, len(text))
    r_start, r_end = value_span(text, rk)
    edits = []  # (position, old_len, new_text), applied from the end backwards

    # 1. cleared_for none -> not-yet
    vk = find_key(text, "verdict", r_start, r_end)
    v_start, v_end = value_span(text, vk)
    if r["verdict"].get("cleared_for") == "none":
        ck = find_key(text, "cleared_for", v_start, v_end)
        c_start, c_end = value_span(text, ck)
        edits.append((c_start, c_end - c_start, '"not-yet"'))

    # 2. kind and state on each assumption
    ak = find_key(text, "assumptions", r_start, r_end)
    a_start, a_end = value_span(text, ak)
    dec = json.JSONDecoder()
    i = a_start + 1
    for n in range(len(assumptions)):
        while text[i] in " \t\r\n,":
            i += 1
        _, o_end = dec.raw_decode(text, i)
        close = o_end - 1
        body = text[i:o_end]
        add_kind = json.dumps(kinds[n])
        if "\n" in body:
            qk = find_key(text, "question", i, o_end)
            ind = line_indent(text, qk)
            j = close
            while text[j - 1] in " \t\r\n":
                j -= 1
            new = ',\n%s"kind": %s,\n%s"state": "assumed"' % (ind, add_kind, ind)
            edits.append((j, 0, new))
        else:
            edits.append((close, 0, ', "kind": %s, "state": "assumed"' % add_kind))
        i = o_end

    # 3. goals before pains
    pk = find_key(text, "pains", r_start, r_end)
    ind = line_indent(text, pk)
    rows = [json.dumps(g, ensure_ascii=False) for g in goals]
    if rows:
        inner = ",\n".join(ind + "  " + row for row in rows)
        goals_text = '"goals": [\n%s\n%s],\n%s' % (inner, ind, ind)
    else:
        goals_text = '"goals": [],\n%s' % ind
    edits.append((pk, 0, goals_text))

    # 4. note
    if note_add:
        nk = find_key(text, "note", r_start, r_end)
        n_start, n_end = value_span(text, nk)
        new_note = r["note"].rstrip() + " " + note_add.strip()
        edits.append((n_start, n_end - n_start, json.dumps(new_note, ensure_ascii=False)))

    for pos, old_len, new in sorted(edits, key=lambda e: e[0], reverse=True):
        text = text[:pos] + new + text[pos + old_len:]

    # Prove nothing else changed.
    after = json.loads(text)
    ra = after["readiness"]
    if list(ra.keys())[:3] != ["schema", "note", "goals"] or ra["goals"] != goals:
        fail("goals did not land as the third field of readiness")
    back = json.loads(json.dumps(after))
    rb = back["readiness"]
    del rb["goals"]
    for a in rb["assumptions"]:
        a.pop("kind")
        a.pop("state")
    if r["verdict"].get("cleared_for") == "none":
        rb["verdict"]["cleared_for"] = "none"
    if note_add:
        rb["note"] = r["note"]
    if back != original:
        fail("self-check failed: something besides the planned additions changed; nothing written")

    if dry:
        print("add_goals: dry run ok for %s (%d goals, %d assumptions)" % (key_path, len(goals), len(kinds)))
        return
    with open(key_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print("add_goals: wrote %s (%d goals, %d assumptions kinded)" % (key_path, len(goals), len(kinds)))


if __name__ == "__main__":
    main()
