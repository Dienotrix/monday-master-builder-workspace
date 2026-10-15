"""Read-only checks for s17-no-markers: field order, quote validity per turn, counts. Never writes."""
import json, re, sys
F = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s17-no-markers/"
ORDER = ["scenario_id","call_type","purpose_of_this_fixture","transcript_format","company","attendees","expected_monday_products","rubric","pains","numbers","vocabulary","entities_and_workflows","integrations_mentioned","compliance_or_security_signals","objections","commitments_and_next_steps","traps","requested_changes","should_plugin_propose_a_build","expected_questions_before_building","expected_verdict","account_context","expected_structures","accepted_behaviours","expected_leak_blocklist"]
k = json.load(open(F+"answer-key.json"))
keys = list(k.keys())
print("field order ok:", keys[:25]==ORDER, "| extra:", keys[25:])
print("key lines:", len(open(F+"answer-key.json").read().split("\n")))
txt = open(F+"transcript.txt").read(); lines = txt.split("\n")
hdr = re.compile(r'^(.+?) (\d\d:\d\d)$'); turns=[]; i=0
while i < len(lines):
    m = hdr.match(lines[i])
    if m: turns.append(dict(n=len(turns)+1, label=m.group(1), stamp=m.group(2), text=lines[i+1])); i+=2
    else: i+=1
byn = {t['n']:t for t in turns}
loc = re.compile(r'^turn (\d+), (\d\d:\d\d), (.+)$')
bad=0; n_loc=0; n_qonly=0
def walk(o, path=""):
    if isinstance(o, dict):
        if "quote" in o and isinstance(o["quote"], str):
            yield path, o["quote"], o.get("location")
        for kk,v in o.items():
            if kk in ("quote","location"): continue
            yield from walk(v, path+"/"+kk)
    elif isinstance(o, list):
        for j,v in enumerate(o): yield from walk(v, f"{path}[{j}]")
for path,q,l in walk({kk:v for kk,v in k.items() if kk!="intake"}):
    if l:
        n_loc+=1
        m = loc.match(l)
        if not m: print("BAD LOC FORMAT", path, l); bad+=1; continue
        n=int(m.group(1)); st=m.group(2); lab=m.group(3)
        t=byn.get(n)
        if not t: print("NO TURN", path, l); bad+=1; continue
        if t['stamp']!=st: print("STAMP MISMATCH", path, l, t['stamp']); bad+=1
        seg = lab.startswith("labelled ")
        want = lab.split(",")[0].replace("labelled ","") if seg else lab
        if t['label']!=want: print("LABEL MISMATCH", path, l, t['label']); bad+=1
        if q not in t['text']: print("QUOTE NOT IN TURN", path, repr(q[:60]), l); bad+=1
        if seg and n!=183: print("SEG LOC NOT 183", path, l); bad+=1
    else:
        n_qonly+=1
        if not any(q in ln for ln in lines): print("QUOTE-ONLY NOT FOUND", path, repr(q[:70])); bad+=1
eq = k["account_context"]["evidence_quote_or_null"]
if eq and not any(eq in ln for ln in lines): print("EVIDENCE QUOTE NOT FOUND"); bad+=1
# intake quotes
for path,q,l in walk(k["intake"]):
    if not any(q in ln for ln in lines): print("INTAKE QUOTE NOT FOUND", path, repr(q[:70])); bad+=1
# segments spans inside turn 183
blk = byn[183]['text']
for s in k["intake"]["composite_blocks"][0]["segments"]:
    a=blk.find(s["from"]); b=blk.find(s["to"])
    if a<0 or b<0 or b<a: print("SEGMENT SPAN BAD", s["k"], a, b); bad+=1
# segment-cited quotes fall inside their segment span
segs = {s["k"]:(blk.find(s["from"]), blk.find(s["to"])+len(s["to"])) for s in k["intake"]["composite_blocks"][0]["segments"]}
for path,q,l in walk({kk:v for kk,v in k.items() if kk!="intake"}):
    if l and "segment" in l:
        kk_=int(re.search(r'segment (\d)',l).group(1)); p=blk.find(q)
        if not (segs[kk_][0] <= p and p+len(q) <= segs[kk_][1]): print("QUOTE OUTSIDE SEGMENT", path, kk_, p, segs[kk_]); bad+=1
# rejoined list vs transcript
rj = k["intake"]["rejoined_sentences"]
for r in rj:
    t=byn[r["fragment_turn"]]
    if t['label']!=r["under_label"]: print("REJOIN LABEL", r); bad+=1
    frag=r["fragment"]
    if not (t['text'].startswith(frag) or t['text'].endswith(frag) or t['text']==frag): print("REJOIN FRAG", r["fragment_turn"], repr(frag), repr(t['text'][:40])); bad+=1
print("rejoined entries:", len(rj), "| cross-label:", sum(1 for r in rj if r["owner"]!="unresolved"), "| unresolved:", sum(1 for r in rj if r["owner"]=="unresolved"))
# counts
rub=k["rubric"]; from collections import Counter
print("rubric rows:", len(rub), dict(Counter(r["status"] for r in rub)), "asked true:", sum(1 for r in rub if r.get("asked")), "asked false:", sum(1 for r in rub if r.get("asked") is False))
print("pains:", len(k["pains"]), "objections:", len(k["objections"]), "traps:", len(k["traps"]), "blocklist:", len(k["expected_leak_blocklist"]), "requested:", Counter(r["type"] for r in k["requested_changes"]), "lookalikes:", len(k["expected_structures"]["lookalike_traps"]), "vocab:", len(k["vocabulary"]), "commitments:", len(k["commitments_and_next_steps"]), "questions:", len(k["expected_questions_before_building"]), "accepted:", len(k["accepted_behaviours"]))
print("objection types:", Counter(o["type"].split(" (")[0] for o in k["objections"]))
print("quotes with location:", n_loc, "quote-only:", n_qonly, "| BAD:", bad)
# stats claimed
words=sum(len(t['text'].split()) for t in turns)
print("turns", len(turns), "words", words, "block words", len(blk.split()), "share", round(len(blk.split())/words,3))
print("short<=4", sum(1 for t in turns if len(t['text'].split())<=4), "lower", sum(1 for t in turns if t['text'][0].islower()), "noterm", sum(1 for t in turns if t['text'][-1] not in '.?!'), "same-label pairs", sum(1 for a,b in zip(turns,turns[1:]) if a['label']==b['label']))
print("markers:", txt.count('['), txt.count('...'), txt.count('--'), txt.count('('))
