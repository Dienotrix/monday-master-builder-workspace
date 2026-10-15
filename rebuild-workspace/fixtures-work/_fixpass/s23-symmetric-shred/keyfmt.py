"""Serializer that reproduces the s23 key's layout: dicts pretty at indent 2, lists one
element per line with each element compact, dicts two levels down inside `intake` compact."""
import json

def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(', ', ': '))

def render(v, depth, in_intake, key=None):
    pad = '  ' * depth
    pad1 = '  ' * (depth + 1)
    if isinstance(v, dict):
        if (in_intake and depth >= 2) or not v:
            return compact(v)
        parts = []
        for k, x in v.items():
            parts.append(pad1 + json.dumps(k, ensure_ascii=False) + ': ' + render(x, depth + 1, in_intake or (depth == 0 and k == 'intake'), k))
        return '{\n' + ',\n'.join(parts) + '\n' + pad + '}'
    if isinstance(v, list):
        if not v:
            return '[]'
        return '[\n' + ',\n'.join(pad1 + compact(x) for x in v) + '\n' + pad + ']'
    return compact(v)

def dumps(key):
    return render(key, 0, False) + '\n'

if __name__ == '__main__':
    import sys
    src = sys.argv[1]
    raw = open(src, encoding='utf-8').read()
    key = json.loads(raw)
    out = dumps(key)
    print('round trip identical:', out == raw)
    if out != raw:
        a = raw.split('\n'); b = out.split('\n')
        for i, (x, y) in enumerate(zip(a, b), 1):
            if x != y:
                print('first diff at line', i); print(' file:', x[:160]); print(' mine:', y[:160]); break
        print('lines', len(a), len(b))
