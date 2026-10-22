"""Regenerate leak_lint.py's shared-words region from the shipped shared/ folder, as test_G01 reads it.

python regen_shared.py <leak_lint.py> <committed leak_lint.py> [--phrases]

Development only, never shipped. Run it after a reviewed change under shared/, and only once `leak_lint.py terms`
over shared/ passes against an empty home (a scratch MMB_HOME holding only local/settings.json). Make the committed
copy with `git show HEAD:plugins/monday-master-builder/scripts/leak_lint.py > <file>` from the plugin root.

SHARED_WORDS becomes shared_vocabulary() less "pdftotext", which check L05 bars from the script's text (test_G01
leaves it out the same way). SHARED_PHRASES is copied back from the committed copy when shared_phrases() still
matches it, so the region keeps the layout test_R41 relies on; if the phrases changed, it stops unless --phrases is
given, and then rewraps between phrases only, with the last phrase on a line of its own, as test_R41 expects.
"""
import importlib.util
import sys
import textwrap
from pathlib import Path

sys.dont_write_bytecode = True
script, committed = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(script.parent))
spec = importlib.util.spec_from_file_location("leak_lint_regen", script)
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

W_HEAD, W_TAIL = 'SHARED_WORDS = frozenset("""\n', '\n""".split())'
P_HEAD, P_TAIL = 'SHARED_PHRASES = frozenset(p.strip() for p in """\n', '\n""".split(",") if p.strip())'


def bounds(text, head, tail):
    start = text.index(head) + len(head)
    return start, text.index(tail, start)


text = script.read_text(encoding="utf-8")
old = committed.read_text(encoding="utf-8-sig")
words = sorted(lint.shared_vocabulary() - {"pdftotext"})
start, end = bounds(text, W_HEAD, W_TAIL)
text = text[:start] + textwrap.fill(" ".join(words), width=120, break_on_hyphens=False) + text[end:]

o_start, o_end = bounds(old, P_HEAD, P_TAIL)
committed_phrases = {p.strip() for p in old[o_start:o_end].split(",") if p.strip()}
phrases = sorted(lint.shared_phrases())
start, end = bounds(text, P_HEAD, P_TAIL)
if set(phrases) == committed_phrases:
    text = text[:start] + old[o_start:o_end] + text[end:]
elif "--phrases" in sys.argv:
    # Reviewed: wrap between phrases only, and keep the last phrase on a line of its own, as test_R41 expects.
    lines, line = [], ""
    for phrase in phrases[:-1]:
        piece = phrase + ","
        if line and len(line) + 1 + len(piece) > 120:
            lines.append(line)
            line = piece
        else:
            line = (line + " " + piece) if line else piece
    lines += [line, phrases[-1] + ","] if line else [phrases[-1] + ","]
    text = text[:start] + "\n".join(lines) + text[end:]
    print("phrases: added %s; removed %s" % (sorted(set(phrases) - committed_phrases),
                                             sorted(committed_phrases - set(phrases))))
else:
    raise SystemExit("shared_phrases() differs from the committed region: review it, then run again with --phrases")
script.write_bytes(text.encode("utf-8"))
c_start, c_end = bounds(old, W_HEAD, W_TAIL)
before = set(old[c_start:c_end].split())
print("words: %d; added %s; removed %s" % (len(words), sorted(set(words) - before), sorted(before - set(words))))
