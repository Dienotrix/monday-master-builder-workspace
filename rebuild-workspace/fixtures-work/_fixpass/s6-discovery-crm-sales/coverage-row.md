# s6-discovery-crm-sales — COVERAGE row after the fix pass

The row for the first table of `fixtures/COVERAGE.md` (three columns: Folder, Files, Call). Per the brief, s1 to s10 keep their three columns and no fourth column is added.

| `s6-discovery-crm-sales/` | `transcript.txt`, `answer-key.json` | Classic sales-team CRM discovery, industrial distributor |

Note for the merge step (not part of the row): the row carries no counts and is unchanged in form and content. The transcript is untouched (270 units, 5,390 spoken words, client talk share 67.2 percent, as the key's `transcript_format` states). The counts COVERAGE tracks for s6 elsewhere are unchanged by this pass: traps 26, pains 21, vocabulary 28 (two entries reworded, none added or removed), expected questions 14, entities_and_workflows 16, commitments 9, objections 7, `quote` fields verified by the shared verifier 190 (147 before the block). The key grew from 1,299 to 2,260 lines with `readiness` as its 26th and last field, and is UTF-8 now (an en dash in the workspace name). The review line is `reviewed 2026-10-13; fix pass applied 2026-10-13`; the fix-pass facts live in `changes.md` beside this file.
