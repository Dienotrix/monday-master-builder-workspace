"""Mess pass for s17 (brief section 5; s11 rule). Edits inside existing units only, by physical
line, each anchored on the exact old text; never inside a protected span. Words and commas only:
no bracket, ellipsis, dash or parenthesis, because the fixture's point is zero markers."""
import sys
P = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s17-no-markers/transcript.txt"
EDITS = {
  # our side
  26: ("Before we get into it, let me say how I'd like to use the time.",
       "Before we get into it, let me, let me just say how I'd like to use the time, how I'd like to use the hour."),
  269: ("afternoon. Park it for now, we'll see whether we need it.",
        "afternoon. Park it for now, park it, we'll see whether we need it."),
  299: ("because I've heard the sales side of this.",
        "because I've heard, I've now heard the sales side of this."),
  380: ("That's a really useful thing to have said. The wrong number",
        "That's a really useful thing to have said, hang on, I want to write that down. The wrong number"),
  557: ("The quotes, then. Forty live at a time,",
        "The quotes, then. Sorry, I said I'd come back to the quotes. Forty live at a time,"),
  611: ("and the list comes out of that. Then orders against it.",
        "and the list comes out of that, the list just comes out of that. Then orders against it."),
  692: ("Availability first: bed counts entered from a phone in the tunnel by the leads, by bed, rolled up by product and size, so the list is true the moment the count is.",
        "Availability first, so, availability first: bed counts entered from a phone in the tunnel by the leads, by bed, and rolled up, rolled up by product and size, so the list is true the moment the count is, the moment the count goes in."),
  734: ("Two things I'd ask for before then, if you can. Ilse,",
        "Two things I'd ask for before then, if you can, two small things. Ilse,"),
  # client side
  53: ("Gunnar started it with his brother and bought him out, and he's still the owner.",
       "Gunnar started it with his brother and bought him out, bought him out years ago, and he's still the owner."),
  125: ("the parks departments pay list because they have to. And that's",
        "the parks departments pay list because they have to, they've got no choice. And that's"),
  596: ("I currently say let me check to, and some of those",
        "I currently say let me check to, let me check and I'll ring you back, and some of those"),
}
lines = open(P, encoding="utf-8").read().split("\n")
added = 0
for ln, (old, new) in sorted(EDITS.items()):
    i = ln - 1
    assert old in lines[i], (ln, lines[i][:80])
    assert lines[i].count(old) == 1, ln
    before = len(lines[i].split())
    lines[i] = lines[i].replace(old, new)
    for bad in ("[", "]", "(", ")", "...", "--"):
        assert bad not in lines[i], (ln, bad)
    added += len(lines[i].split()) - before
    print(f"L{ln} turn {(ln+1)//3}: +{len(new.split())-len(old.split())} words")
open(P, "w", encoding="utf-8").write("\n".join(lines))
print("words added:", added)
