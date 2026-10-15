import sys
P = "/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s16-shred-cue/README.md"
t = open(P, encoding="utf-8").read()
R = [
 ("22.7 minutes, about 3,173 spoken words, client share 75% by words and 75% by seconds. 1,193 lines. |",
  "22.7 minutes, about 3,195 spoken words, client share about 75% by words (74.9) and by seconds (74.6). 1,193 lines. |"),
 ("| `answer-key.json` | The 25 fields in the s1 to s10 order, plus an `intake` block. 376 lines. |",
  "| `answer-key.json` | The 25 fields in the s1 to s10 order, plus an `intake` block and, last, a `readiness` block (`readiness/1`, added in the fix pass). 537 lines. |"),
 ("- Products: Work Management (jobs with the six stations, permits on the job with an expiry warning keyed to the install date, a full-screen shop view) plus CRM for quotes, third in the client's own order.",
  "- Products: Work Management (the production flow through the six stations, permits with an expiry warning keyed to the install date, a change request on the job, a full-screen shop view; the item grain is open with a leaning: job as parent, signs or sign packages as child rows through the stations, permits as their own rows linked to the job or building) plus CRM for quotes, third in the client's own order."),
 ("- Quotes: 124 checked strings: 78 with a cue or cue-range location, 20 quote-only (numbers, objections, commitments, requested changes, `account_context.evidence_quote_or_null`), 22 `asked_quote` strings and 4 type-header signal quotes in the intake block; all verified verbatim against the cited cue or merged run, with every merged-run quote confirmed to span its range under one label.",
  "- Quotes: 162 checked strings: 78 with a cue or cue-range location in the 25 fields, 20 quote-only (numbers, objections, commitments, requested changes, `account_context.evidence_quote_or_null`), 22 `asked_quote` strings and 4 type-header signal quotes in the intake block, and 38 in the readiness block (10 pains, 7 signals, 21 under leanings); all verified verbatim against the cited cue or merged run (`verify_quotes.py`, 162 of 162, no miss or near-miss), with every merged-run quote confirmed to span its range under one label."),
 ("298 units, 3,173 words,", "298 units, 3,195 words,"),
 ("talk share 75.4% client by words and 74.6% by seconds", "talk share 74.9% client by words and 74.6% by seconds"),
 ("alias map 2 entries (`R` = Ruairi, `Dad` = the founder); 1 unresolved mention (name-shaped noise); 6 people mentioned and not present; 1 second-hand figure; 1 unit-unresolved figure; 0 composite blocks; silence 159.5 s (11.7% of the span) with 1 gap over three seconds; talk share 74.9% client by words and 74.6% by seconds; package order not applicable.",
  "alias map 2 entries (`R` = Ruairi, `Dad` = the founder); 1 unresolved mention (name-shaped noise); 6 people mentioned and not present; 1 second-hand figure; 1 unit-unresolved figure; 0 composite blocks; silence 159.5 s (11.7% of the span) with 1 gap over three seconds; talk share 74.9% client by words and 74.6% by seconds; package order not applicable; type header field `direction` (renamed from `direction_of_show` in the fix pass).\n- Readiness block: 10 pains (P1.1 to P1.3, P2.1 to P2.4, P3.1, P4.1, P5.1, one per `pains` entry), 7 signals, 26 entities (17 with a parent), 8 leanings, 10 element-per-pain rows (7 fixes, 2 copies-today's-tool, 1 none), 8 incumbents, 16 assumptions, 8 unmet needs, 5 AI opportunities (all round 2), 5 questions (2 read-backs, 3 discovery); cleared for build; build target own-account (A21), workspaces `Tallgrass – Ops` and `Tallgrass – CRM`."),
 ("- To stay under the 400-line budget, every list entry (a rubric row, a pain, an objection, an intake entry) is printed on one line. The field set and order are unchanged from s1 to s10.",
  "- Every list entry (a rubric row, a pain, an objection, an intake entry, a readiness entry) is printed on one line, the stage-1 convention that kept the key under 400 lines; the fix pass's `readiness` block takes the file to 537 lines with the same convention. The field set and order of the 25 fields are unchanged from s1 to s10; `intake` and `readiness` follow them. The key is UTF-8 since the fix pass (the en dash in the workspace names); the transcript stays ASCII."),
 ("Not yet reviewed by the user; the COVERAGE.md row is written at the acceptance stage from the counts above.",
  "Reviewed by the user on 2026-10-12 (FEEDBACK.md, s16 entry: keep the intake and the pains, two changes to the build model); the COVERAGE.md row is written at the acceptance stage from the counts above."),
 ("no quote, location, grade or count changed.",
  "no quote, location, grade or count changed. Fix pass applied 2026-10-13: the user's review changes of 2026-10-12 applied (the item grain stated as open with a leaning, and a change-request element added to the build), `direction_of_show` renamed `direction`, the seven-pattern sweep run (eight leanings), the no-write claims about the accounting system traced to cues 236 and 237 and labelled, the five commitments reworded as committed and not yet done, a mess pass on five uncited Consultant cues (52, 182, 207, 266, 280; 3,195 words, no unit, numbering or timing line changed), and the `readiness` block added as the last field; every quote re-verified afterwards (162 of 162)."),
]
for old, new in R:
    n = t.count(old)
    assert n == 1, f"{n} occurrences: {old[:70]!r}"
    t = t.replace(old, new)
open(P, "w", encoding="utf-8").write(t)
print("README edited:", len(R), "replacements;", len(t.splitlines()), "lines")
