"""Dump a key in the s15 style: dicts pretty at depth 0 and 1, lists one entry per line,
objects inside lists compact on one line, dicts at depth 2 and below compact.
`deep` names top-level keys whose dicts stay pretty one level further (used for `readiness`)."""
import json

def _compact(o):
    return json.dumps(o, ensure_ascii=False, separators=(", ", ": "))

def dumps(o, deep=()):
    out = []
    def emit(v, depth, ind, pretty_limit):
        pad = "  " * ind
        if isinstance(v, dict):
            if not v:
                out.append("{}"); return
            if depth < pretty_limit:
                out.append("{\n")
                items = list(v.items())
                for i, (kk, vv) in enumerate(items):
                    out.append(pad + "  " + json.dumps(kk, ensure_ascii=False) + ": ")
                    emit(vv, depth + 1, ind + 1, pretty_limit)
                    out.append(",\n" if i < len(items) - 1 else "\n")
                out.append(pad + "}")
            else:
                out.append(_compact(v))
        elif isinstance(v, list):
            if not v:
                out.append("[]"); return
            out.append("[\n")
            for i, vv in enumerate(v):
                out.append(pad + "  ")
                if isinstance(vv, (dict, list)):
                    out.append(_compact(vv))
                else:
                    out.append(_compact(vv))
                out.append(",\n" if i < len(v) - 1 else "\n")
            out.append(pad + "]")
        else:
            out.append(_compact(v))
    # top level
    out.append("{\n")
    items = list(o.items())
    for i, (kk, vv) in enumerate(items):
        out.append("  " + json.dumps(kk, ensure_ascii=False) + ": ")
        limit = 3 if kk in deep else 2
        emit(vv, 1, 1, limit)
        out.append(",\n" if i < len(items) - 1 else "\n")
    out.append("}\n")
    return "".join(out)
