"""Fix 1 of verify.md (2026-10-13): `intake.conflicts[0]` gains a `leaning` carrying the same
leaning as `readiness.structure.leanings[2]` (option and condition, copied from that entry), after
the entry's existing fields. Load, change, dump with the editor's renderer; round trip asserted first."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render  # noqa: E402

KEY = os.path.join(HERE, '..', '..', '..', 'fixtures', 's25-client-documents', 'answer-key.json')
KEY = os.path.normpath(KEY)

raw = open(KEY, encoding='utf-8').read()
d = json.loads(raw)
expanded = render.layout(raw)
assert render.dumps(d, expanded) == raw, 'round trip failed before any change'

conflict = d['intake']['conflicts'][0]
assert conflict['proposition'].startswith('whether a priority request is approved by the Laboratory Manager')
assert 'leaning' not in conflict, 'already applied'
fork = d['readiness']['structure']['leanings'][2]
assert fork['pattern'] == 'fork'

conflict['leaning'] = {'option': fork['option'], 'condition': fork['condition']}
assert list(conflict.keys())[-1] == 'leaning'
assert list(d.keys())[-1] == 'readiness' and list(d.keys())[-2] == 'intake'

out = render.dumps(d, expanded)
assert json.loads(out) == d
open(KEY, 'w', encoding='utf-8').write(out)
print('lines before', raw.count('\n'), 'after', out.count('\n'))
