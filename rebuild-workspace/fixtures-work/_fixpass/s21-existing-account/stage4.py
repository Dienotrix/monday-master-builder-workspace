import json, re, sys
from collections import Counter
sys.path.insert(0, '.')
from render import dump
F = '/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s21-existing-account/'
def rep(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:70]); return s.replace(old, new)

# ---- transcript: mess pass inside six unquoted Consultant turns (s11 rule, brief section 5)
t = open(F + 'transcript.txt', encoding='utf-8').read()
edits = [
 ("[00:04:55] Consultant: That's on both of us, and I'd rather own my half of it. And the Studies board, who changes things on it now? Labels, columns, that sort of thing.",
  "[00:04:55] Consultant: That's on both of us, and I'd rather -- I'd rather own my half of it. And the Studies board, who changes things on it now? Labels, columns, um, that sort of thing."),
 ("[00:05:44] Consultant: We'll check that rather than guess it. It's one of the things I'd want to leave different this time, so it's yours to change.",
  "[00:05:44] Consultant: We'll check that rather than guess it. It's one of the things I'd want to, er, to leave different this time, so it's yours to change."),
 ("[00:20:40] Consultant: That's their call, not mine. Ask them and tell me what they say, and I'll do it whichever way they want.",
  "[00:20:40] Consultant: That's their call, not mine. Ask them and tell me what they say, and I'll do it whichever way they, whichever way they want."),
 ("[00:21:36] Consultant: Thanks, that was useful. Genuinely, that's most of the work already done, and it's done in your words, which is the part I can't do.",
  "[00:21:36] Consultant: Thanks, that was useful. Genuinely, that's -- that's most of the work already done, and it's done in your words, which is the part I can't do, so."),
 ("[00:25:42] Consultant: Right. And the recruiters themselves. Last time it was the board, they went back to the sheet, we've said that. What's different this time?",
  "[00:25:42] Consultant: Right. And the recruiters themselves. Last time it was the board, they went back to the sheet, we've said that. So what's, what's different this time?"),
 ("[00:27:05] Consultant: One thing I want to ask while we're here. The recruiters have respondent details somewhere. Where do those live?",
  "[00:27:05] Consultant: One thing I want to ask while we're here, um, before I forget. The recruiters have respondent details somewhere. Where do those live?"),
]
for o, n in edits: t = rep(t, o + '\n', n + '\n')
open(F + 'transcript.txt', 'w', encoding='utf-8').write(t)

# ---- recount under the README's definition
c = Counter(); mx = (0, None); short = 0; same = 0; prev = None; units = 0
for line in t.splitlines():
    m = re.match(r'\[(\d\d:\d\d:\d\d)\] ([^:]+): (.*)$', line); assert m, line
    units += 1; ts, sp, txt = m.groups()
    toks = [x for x in txt.split() if x != '--' and not re.fullmatch(r'\[[^\]]*\]', x)]
    n = len(toks); c[sp] += n
    if n > mx[0]: mx = (n, ts + ' ' + sp)
    if n <= 4: short += 1
    if prev == sp: same += 1
    prev = sp
tot = sum(c.values()); cl = tot - c['Consultant']
pct = lambda n: round(100 * n / tot)
assert units == 262 and mx == (83, '00:33:57 Consultant') and short == 24 and same == 20
B, Hh, Id, CL = pct(c['Bethan Tull']), pct(c['Henrietta Weyland']), pct(c['Idris Machado']), pct(cl)
print('words', tot, 'client', CL, 'Bethan', B, 'Henrietta', Hh, 'Idris', Id, 'max', mx, 'short', short, 'same', same)

# ---- key count fields
P = F + 'answer-key.json'; k = json.load(open(P, encoding='utf-8'))
k['transcript_format'] = rep(k['transcript_format'], "About 4,770 spoken words", f"About {tot:,} spoken words")
k['transcript_format'] = rep(k['transcript_format'], "client share about 67% (Bethan 27%, Henrietta 27%, Idris 13%)", f"client share about {CL}% (Bethan {B}%, Henrietta {Hh}%, Idris {Id}%)")
assert k['intake']['format']['words_spoken'] == 4769; k['intake']['format']['words_spoken'] = tot
dump(k, P)
lines = sum(1 for _ in open(P, encoding='utf-8'))

# ---- README
R = F + 'README.md'; r = open(R, encoding='utf-8').read()
r = rep(r, "262 lines, 37.6 minutes, 4,769 spoken words (whitespace tokens after the speaker label, bracket tags and bare `--` excluded), client share 67% (Bethan 27%, Henrietta 27%, Idris 13%), longest turn 83 words, the Consultant's at 00:33:57.",
    f"262 lines, 37.6 minutes, {tot:,} spoken words (whitespace tokens after the speaker label, bracket tags and bare `--` excluded), client share {CL}% (Bethan {B}%, Henrietta {Hh}%, Idris {Id}%), longest turn 83 words, the Consultant's at 00:33:57.")
r = rep(r, "The 25 fields in the s1 to s10 order, plus an `intake` block. 274 lines.",
    f"The 25 fields in the s1 to s10 order, plus an `intake` block and, since the fix pass, a `readiness` block last. {lines} lines.")
r = rep(r, "R10 Met in expansion mode on a booking mechanism delivered on the call with a named owner, a stated purpose and client assent;",
    "R10 Met in expansion mode on a booking mechanism committed on the call (evidence state: the booking link committed to send today, with its owner and purpose; not sent, done only on evidence);")
r = rep(r, "Requested changes: 1 add, 2 change, 1 remove (changes to live objects of ours with the approver's yes; the recruiter week view conditional).",
    "Requested changes: 1 add, 3 change, 1 remove (the costing delta first, as the main build; the label handover with the approver's yes; the rota archive proposed and accepted by Idris, with the approver's yes still required; the recruiter week view conditional).")
r = rep(r, "all verified verbatim against the cited line by a checker that matches on timestamp and speaker and follows nested quote objects.",
    "all verified verbatim against the cited line by a checker that matches on timestamp and speaker and follows nested quote objects. After the fix pass the shared verifier (`fixtures-work/_fixpass/verify_quotes.py`) reports 194 quote strings, 191 verified (25 of them by presence only, with no location cited) and 3 bare location pointers skipped; 0 near-misses, 0 misses.")
r = rep(r, "`label`, `seat`, `relationship`, `direction_of_show`, `output_class`", "`label`, `seat`, `relationship`, `direction`, `output_class`")
r = rep(r, "`direction_of_show` carries one of the four tokens, `no-show`, the dominant one; a `direction_of_show_note` beside it",
    "`direction` (named `direction_of_show` before the fix pass) carries one of the four tokens, `no-show`, the dominant one; a `direction_note` beside it")
r = rep(r, "To stay under the 400-line budget, every list entry and every second-level key is printed on one line. The field set and order are unchanged from s1 to s10.",
    f"Every list entry and every second-level key of the 26 original fields is printed on one line; the `readiness` block added in the fix pass prints its entries one per line, two levels deeper, which is why the file is now {lines} lines. The field set and order of the 25 fields are unchanged from s1 to s10; `intake` and `readiness` follow them.")
r = rep(r, "The composite `direction_of_show` value was replaced with the bare value", "The composite direction-of-show value was replaced with the bare value")
r = rep(r, "## Review status\n\nWritten to its row in BUILD-PLAN.md section 4.2 and to C64 in REAL-CALL-LESSONS.md section 6, and to nothing else. Not yet reviewed by the user; the COVERAGE.md row is written at the acceptance stage from the counts above.",
    "Fix pass applied 2026-10-13: the three changes of the user's review (the costing delta added to `requested_changes` as the main build, the rota archive reworded as proposed and accepted by Idris with Henrietta's approval still required, the booking link as committed to send today with owner and purpose), the `direction` rename, the seven-pattern sweep (six leanings, with the agency value, the session row and the Farraday alias corrected in their fields), the `readiness` block as the 27th field, and a light mess pass on six unquoted Consultant turns (00:04:55, 00:05:44, 00:20:40, 00:21:36, 00:25:42, 00:27:05; sixteen words, no unit, stamp or quoted span changed), with every count above re-derived; the log is `fixtures-work/_fixpass/s21-existing-account/changes.md`.\n\n## Review status\n\nWritten to its row in BUILD-PLAN.md section 4.2 and to C64 in REAL-CALL-LESSONS.md section 6, and to nothing else. Reviewed by the user on 2026-10-11 (FEEDBACK.md, s21 entry: keep, with three changes, all applied in the fix pass of 2026-10-13); the COVERAGE.md row is updated from the counts above by the merge step.")
open(R, 'w', encoding='utf-8').write(r)
print('key lines', lines, '| README stale checks:', [s for s in ['4,769', '274 lines', 'direction_of_show`', 'Henrietta 27%', '2 change'] if s in r])
