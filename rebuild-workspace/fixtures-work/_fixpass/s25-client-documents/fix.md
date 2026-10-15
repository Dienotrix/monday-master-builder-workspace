# s25-client-documents — fixes after the first verification

Fixer's log, 2026-10-13. Everything here is fictional and stays fictional. Both numbered fixes in `verify.md` are applied. Files touched: `fixtures/s25-client-documents/answer-key.json` (one entry), `fixtures/s25-client-documents/README.md` (one sentence on the fix-pass line) and `changes.md` here (four lines). The transcript, the Word file, the PDF, the PNG and `coverage-row.md` are unchanged; no count they carry moved. The edit script is `fix.py` beside this file; it imports the editor's `render.py`, asserted a byte-for-byte round trip of the shipped key before changing it, and was run once.

## Fixes

1. **`intake.conflicts[0]` gains a `leaning`.** The entry for "whether a priority request is approved by the Laboratory Manager before allocation" now ends with a `leaning` field after `callback`, holding `option` and `condition` copied word for word from `readiness.structure.leanings[2]` (the priority flag with a notification built, the approval step built neither way; settled by the Quality Manager and the Laboratory Manager together on the 9th). The entry's quotes are unchanged and the leaning repeats none of them, because the entry already holds them under `document`, `dependent_requirement` and `call`; the verifier's pair count therefore stays at 167. The shape follows the s24 fork's `leaning` without its `status` line. The key stays 551 lines and 27 fields in order, with `intake` 26th and `readiness` last; a line diff against the pre-fix copy shows that one line and nothing else. Logged in `changes.md` (the method paragraph's diff sentence, section 3's fork sentence and section 10's corrected-fields row) and on the README's fix-pass line.
2. **`changes.md` section 10, the `entities` row.** "21 (10 with a parent, all with `moves_independently`)" is now "21 (11 with a parent, all with `moves_independently`)", which is what the key holds (recounted: 11 of 21 entities carry a parent).

## Verifier output

`python3 -I fixtures-work/_fixpass/verify_quotes.py /Users/caramelm4/DelOps/rebuild-workspace/fixtures/s25-client-documents`, run after the key edit and again after the Markdown edits, identical both times, exit code 0:

```
Fixture: s25-client-documents
Sources: QP-07-F1-sample-flow.png (image, 0 units); QP-07-sample-receipt-testing-certification-v3.2.docx (docx, 33 units); sample-tracking-what-we-need.pdf (pdf, 6 units); transcript.txt (transcript/line-bracket, 88 units)

pairs found      167
verified         166  (of which presence only, no location cited: 11)
skipped          2  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      1

UNPARSED PROSE AND UNSUPPORTED FORMS
- /rubric[0]/evidence[4]/quote [unsupported] image: not checkable here, skipped | Log in sample register
```

The one unsupported form is the figure label in the PNG, which the baseline already lists and which no reader of an image can check here. Zero misses.
