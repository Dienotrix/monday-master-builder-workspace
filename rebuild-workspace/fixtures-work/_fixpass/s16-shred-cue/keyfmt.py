"""Serializer that reproduces the s16 key's hybrid style: two-space indent; array elements compact on
one line; objects whose values are all scalars compact; arrays of scalars one per line; everything else
expanded. Tested byte for byte against the untouched file before any change."""
import json
def _compact(v): return json.dumps(v, ensure_ascii=False)
def _is_scalar(v): return not isinstance(v, (dict, list))
def dump(v, ind=0):
    pad = "  " * ind; pad1 = "  " * (ind + 1)
    if isinstance(v, dict):
        if not v: return "{}"
        if all(_is_scalar(x) for x in v.values()) and ind > 0: return _compact(v)
        items = [f'{pad1}{_compact(k)}: {dump(x, ind + 1)}' for k, x in v.items()]
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    if isinstance(v, list):
        if not v: return "[]"
        items = [f'{pad1}{_compact(x)}' for x in v]
        return "[\n" + ",\n".join(items) + "\n" + pad + "]"
    return _compact(v)
def dumps(obj): return dump(obj, 0) + "\n"
if __name__ == "__main__":
    import sys
    p = sys.argv[1]; raw = open(p, encoding="utf-8").read()
    out = dumps(json.loads(raw))
    print("byte-identical:", out == raw)
    if out != raw:
        a = raw.split("\n"); b = out.split("\n")
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y: print("first diff at line", i + 1); print(" file:", x[:160]); print(" mine:", y[:160]); break
        print(len(a), len(b))
