"""Renderer that reproduces the s25 key's own layout exactly. The key prints most list entries and
nested dicts on one line, with a few containers expanded (the top level, each top-level container,
`intake.files`, `intake.grading_passes` and its two passes, and so on). Rather than guess the rule,
`layout(raw)` reads which container paths the shipped file expands and `render` follows that set;
any container not in the set is printed compact. For the new `readiness` block (added in the fix
pass) a container expands when it holds another container, so every pain, entity, leaning and
question sits on its own line."""
import json
import re

_KEY = re.compile(r'^\s*"((?:[^"\\]|\\.)*)":\s*([\[{])$')


def layout(raw):
    """The set of container paths (tuples of keys and indices) the raw text prints expanded."""
    expanded = set()
    stack = []          # entries: [path, kind, child_count]
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if s in ('}', ']', '},', '],'):
            stack.pop()
            continue
        if stack:
            parent = stack[-1]
            if parent[1] == '{':
                m = _KEY.match(line)
                if m:
                    path = parent[0] + (json.loads('"' + m.group(1) + '"'),)
                    expanded.add(path)
                    stack.append([path, m.group(2), 0])
                continue
            idx = parent[2]
            parent[2] += 1
            if s in ('{', '['):
                path = parent[0] + (idx,)
                expanded.add(path)
                stack.append([path, s, 0])
            continue
        if s in ('{', '['):
            expanded.add(())
            stack.append([(), s, 0])
    return expanded


def compact(v):
    return json.dumps(v, ensure_ascii=False, separators=(', ', ': '))


def has_container(v):
    vals = v.values() if isinstance(v, dict) else v
    return any(isinstance(x, (dict, list)) and x for x in vals)


def render(v, path, ind, expanded):
    if not (isinstance(v, (dict, list)) and v):
        return compact(v)
    if path[:1] == ('readiness',):
        expand = len(path) == 1 or has_container(v)
    else:
        expand = path in expanded
    if not expand:
        return compact(v)
    if isinstance(v, dict):
        parts = [' ' * (ind + 2) + json.dumps(k, ensure_ascii=False) + ': ' + render(val, path + (k,), ind + 2, expanded)
                 for k, val in v.items()]
        return '{\n' + ',\n'.join(parts) + '\n' + ' ' * ind + '}'
    parts = [' ' * (ind + 2) + render(x, path + (i,), ind + 2, expanded) for i, x in enumerate(v)]
    return '[\n' + ',\n'.join(parts) + '\n' + ' ' * ind + ']'


def dumps(obj, expanded):
    return render(obj, (), 0, expanded) + '\n'


if __name__ == '__main__':
    import sys
    src = sys.argv[1]
    raw = open(src, encoding='utf-8').read()
    obj = json.load(open(src, encoding='utf-8'))
    exp = layout(raw)
    out = dumps(obj, exp)
    print('round trip identical:', out == raw, '| non-ascii in source:', any(ord(c) > 127 for c in raw))
    print('expanded paths:', sorted(p for p in exp if len(p) >= 2 and p[0] == 'intake'))
    if out != raw:
        a = raw.splitlines(); b = out.splitlines()
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y:
                print('first diff at line', i + 1); print(repr(x[:160])); print(repr(y[:160])); break
        print(len(a), len(b))
