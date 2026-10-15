"""Renderer that reproduces the s21 key's own layout: top-level keys on their own lines,
each direct child of a top-level container on one compact line, and (added for the fix pass)
the readiness block printed one level deeper so its entries are one per line."""
import json

def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(', ', ': '))

def render(v, depth, under_readiness, ind):
    limit = 4 if under_readiness else 2
    if isinstance(v, dict) and v and depth < limit:
        parts = []
        for k, val in v.items():
            parts.append(' ' * (ind + 2) + json.dumps(k, ensure_ascii=False) + ': ' +
                         render(val, depth + 1, under_readiness or k == 'readiness', ind + 2))
        return '{\n' + ',\n'.join(parts) + '\n' + ' ' * ind + '}'
    if isinstance(v, list) and v and depth < limit:
        parts = [' ' * (ind + 2) + render(x, depth + 1, under_readiness, ind + 2) for x in v]
        return '[\n' + ',\n'.join(parts) + '\n' + ' ' * ind + ']'
    return compact(v)

def dump(obj, path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(render(obj, 0, False, 0) + '\n')

if __name__ == '__main__':
    import sys
    src = sys.argv[1]
    raw = open(src, encoding='utf-8').read()
    obj = json.load(open(src, encoding='utf-8'))
    out = render(obj, 0, False, 0) + '\n'
    print('round trip identical:', out == raw, '| non-ascii in source:', any(ord(c) > 127 for c in raw))
    if out != raw:
        a = raw.splitlines(); b = out.splitlines()
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print('first diff at line', i + 1); print(repr(x[:160])); print(repr(y[:160])); break
        print(len(a), len(b))
