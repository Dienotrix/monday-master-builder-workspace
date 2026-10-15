import json, re, sys
base = "<scratch>/scratchpad/rebuild/fixtures/s5-intro-thin/"
t = open(base + "transcript.txt", encoding="utf-8").read()
lines = t.splitlines()
try:
    k = json.load(open(base + "answer-key.json", encoding="utf-8"))
    print("JSON valid")
except Exception as e:
    print("JSON INVALID", e); sys.exit(1)

required = ["scenario_id","call_type","purpose_of_this_fixture","transcript_format","company","attendees","expected_monday_products","rubric","pains","numbers","vocabulary","entities_and_workflows","integrations_mentioned","compliance_or_security_signals","objections","commitments_and_next_steps","traps","requested_changes","should_plugin_propose_a_build","expected_questions_before_building"]
print("missing keys:", [x for x in required if x not in k])
print("extra keys:", [x for x in k if x not in required])
for r in k["rubric"]:
    if r["status"] not in ("met","partial","missing"): print("bad status", r)

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
n = 0; bad = 0
for path, q, loc in quotes:
    if q is None: continue
    n += 1
    if q not in t:
        bad += 1; print("NOT FOUND:", path, repr(q)); continue
    hits = [i for i, l in enumerate(lines) if q in l]
    if not hits:
        print("SPANS LINES:", path, repr(q)); continue
    if len(hits) > 1:
        print("MULTI-HIT (", len(hits), "):", path, repr(q), [lines[h][:22] for h in hits])
    if loc:
        ts = re.match(r"\[(\d\d:\d\d:\d\d)\]", lines[hits[0]])
        if ts and ts.group(1) not in loc:
            print("LOC MISMATCH:", path, repr(q), "key:", loc, "actual:", ts.group(1))
print(f"quotes checked: {n}, not found: {bad}")
