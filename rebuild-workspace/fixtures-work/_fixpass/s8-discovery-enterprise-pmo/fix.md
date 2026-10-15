# s8-discovery-enterprise-pmo — fix pass, second round

Fixer's log, 2026-10-13. Everything here is fictional and stays fictional. The verifier's first pass (`verify.md`) ended FAIL on two findings. Both are applied below; nothing else in the fixture moved.

Files touched: `fixtures/s8-discovery-enterprise-pmo/answer-key.json` (one string) and `_fixpass/s8-discovery-enterprise-pmo/coverage-row.md` (one sentence). `transcript.txt` and `changes.md` are unchanged. The key was loaded, changed and dumped by script after a no-change round trip had reproduced the file byte for byte, so the diff is the one string.

## Fixes

1. **Spliced quote in `readiness.questions[2].text`.** The opening sentence quoted 'confirmed, verbally, in the hall', which joined Warren's words at cue 155 with Ines's at cue 156 and matched neither. Replaced the sentence with "Ines, on the June collision you said 'Verbally, in the hall, which is the problem'." The quoted span is Ines's own line at cue 156 (00:21:35.701) and was proven verbatim in the transcript by the edit script before the file was written. The rest of the question (the allocation row, the preconstruction names, the four qualified superintendents) and its `kind`, `role` and `known` fields are as they were. The inline-quote check was re-run over the whole block: four single-quoted spans of three words or more, all present in the transcript, none missing.
2. **Coverage row's claim about the review line.** The last paragraph of `coverage-row.md` said the line `reviewed 2026-10-13; fix pass applied 2026-10-13` lives in `changes.md`; it did not, and the s1 exemplar's coverage-row.md carries no such sentence either. Reworded so the paragraph states the review line itself and says plainly that it is here and not in `changes.md`, leaving the merge step to record it in whatever form the first table adopts. `changes.md` was not edited, since the editor's log is a record of what was done rather than a place to park the row's review line.

## Verifier output

`python3 -I fixtures-work/_fixpass/verify_quotes.py fixtures/s8-discovery-enterprise-pmo`, run after both fixes, exit code 0:

```
Fixture: s8-discovery-enterprise-pmo
Sources: transcript.txt (transcript/vtt, 417 units)

pairs found      283
verified         283  (of which presence only, no location cited: 25)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
```

The pair count is unchanged from the first verification (283 found, 283 verified, 25 presence-only), which is expected: the replaced span sat in a prose field the structured verifier does not parse, and no structured quote or location moved.
