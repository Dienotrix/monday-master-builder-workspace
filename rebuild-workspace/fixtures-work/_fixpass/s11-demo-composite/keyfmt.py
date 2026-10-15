"""Serializer that reproduces the hand layout of s11's answer-key.json.
Rules inferred from the file: one space per indent level; a dict inside a list prints on one
line; a dict elsewhere prints on one line only when every value is a scalar; a list of scalars
prints inline when its inline form is short, else one element per line; lists of containers
print one element per line. Proven by a byte-for-byte round trip before any edit."""
import json

INLINE_LIST_MAX = 120

def _scalar(v):
    return json.dumps(v, ensure_ascii=False)

def _is_scalar(v):
    return not isinstance(v, (dict, list))

def _one_line(v):
    if isinstance(v, dict):
        return "{" + ", ".join(_scalar(k) + ": " + _one_line(x) for k, x in v.items()) + "}"
    if isinstance(v, list):
        return "[" + ", ".join(_one_line(x) for x in v) + "]"
    return _scalar(v)

def _fmt(v, depth, in_list):
    pad = " " * depth
    pad1 = " " * (depth + 1)
    if isinstance(v, dict):
        if in_list or all(_is_scalar(x) for x in v.values()):
            return _one_line(v)
        parts = [pad1 + _scalar(k) + ": " + _fmt(x, depth + 1, False) for k, x in v.items()]
        return "{\n" + ",\n".join(parts) + "\n" + pad + "}"
    if isinstance(v, list):
        if not v:
            return "[]"
        if all(_is_scalar(x) for x in v):
            s = _one_line(v)
            if len(s) <= INLINE_LIST_MAX:
                return s
        parts = [pad1 + _fmt(x, depth + 1, True) for x in v]
        return "[\n" + ",\n".join(parts) + "\n" + pad + "]"
    return _scalar(v)

def dumps(obj):
    return _fmt(obj, 0, False) + "\n"

def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(dumps(obj))

if __name__ == "__main__":
    import sys
    p = sys.argv[1]
    raw = open(p, encoding="utf-8").read()
    out = dumps(json.loads(raw))
    if out == raw:
        print("round trip: identical")
    else:
        import difflib
        d = list(difflib.unified_diff(raw.split("\n"), out.split("\n"), lineterm="", n=0))
        print("round trip differs; %d diff lines" % len(d))
        for l in d[:40]:
            print(l[:200])
