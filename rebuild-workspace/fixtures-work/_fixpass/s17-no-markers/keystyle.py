"""Dump the s17 key in its own style: dicts pretty at depth 0 and 1, and deeper dicts pretty only
when one of their direct values is a list; every other dict compact on one line; lists one entry
per line with each entry compact, except a list of scalars at depth 3 or deeper, which is inline;
objects inside lists always compact. Reproduces the untouched
file byte for byte (checked before any edit)."""
import json

def _compact(o):
    return json.dumps(o, ensure_ascii=False, separators=(", ", ": "))

def dumps(o):
    out = []
    def emit(v, depth, ind):
        pad = "  " * ind
        if isinstance(v, dict):
            if not v:
                out.append("{}"); return
            pretty = depth <= 1 or any(isinstance(x, list) for x in v.values())
            if pretty:
                out.append("{\n")
                items = list(v.items())
                for i, (kk, vv) in enumerate(items):
                    out.append(pad + "  " + json.dumps(kk, ensure_ascii=False) + ": ")
                    emit(vv, depth + 1, ind + 1)
                    out.append(",\n" if i < len(items) - 1 else "\n")
                out.append(pad + "}")
            else:
                out.append(_compact(v))
        elif isinstance(v, list):
            if not v:
                out.append("[]"); return
            if depth >= 3 and not any(isinstance(x, (dict, list)) for x in v):
                out.append(_compact(v)); return
            out.append("[\n")
            for i, vv in enumerate(v):
                out.append(pad + "  " + _compact(vv))
                out.append(",\n" if i < len(v) - 1 else "\n")
            out.append(pad + "]")
        else:
            out.append(_compact(v))
    emit(o, 0, 0)
    out.append("\n")
    return "".join(out)
