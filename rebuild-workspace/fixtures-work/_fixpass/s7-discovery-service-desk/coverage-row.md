# s7-discovery-service-desk — COVERAGE row after the fix pass

The row for the first table of `fixtures/COVERAGE.md` (three columns: Folder, Files, Call). Per the brief, s1 to s10 keep their three columns and no fourth column is added.

| `s7-discovery-service-desk/` | `transcript.txt` (SRT), `answer-key.json` | Service-desk discovery, facilities maintenance company |

Note for the merge step (not part of the row): the row carries no counts and is unchanged in form and content. The transcript is untouched (267 cues, about 5,401 spoken words). The counts COVERAGE tracks for s7 elsewhere are unchanged by this pass: traps 35, pains 18, vocabulary 16, expected questions 15, entities_and_workflows 16, commitments 10, requested changes 2/4/0, look-alike traps 12. One count moves: `quote` fields in the second table from 144 to 192, because the `readiness` block adds 18 pain quotes, 6 signal quotes and 24 leaning quotes (the verifier's 193 pairs include `account_context.evidence_quote_or_null`). The key grew from 1,273 to 2,271 lines with `readiness` as its 26th field and is UTF-8 now (the en dash in the workspace name). Review line for whatever form the first table adopts: `reviewed 2026-10-13; fix pass applied 2026-10-13`.
