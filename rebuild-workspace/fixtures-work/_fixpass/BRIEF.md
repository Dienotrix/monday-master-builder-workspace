# Fixture fix pass — the common brief

Written 2026-10-13 by the planner. Every agent in the fix pass reads this file first. It fixes the field names of the `readiness` block, the editing rules and the output files, so twenty-five keys come out the same shape. The authority behind it: `for-review/FEEDBACK.md` (the user's review findings and their dispositions, including the agreed order, the sign-off scope at the top, the cross-fixture patterns near the end and the standing lines inside the s11, s14, s21 and s22 entries), `rebuild-workspace/design/stage-1b/build-readiness-spec.md` (the check the block mirrors), `rebuild-workspace/design/stage-1b/PLAN.md` section 7 (what the fix pass does), and amendments A16, A21 and A23 in `rebuild-workspace/design/AMENDMENTS.md`.

## 1. Where things are

- Fixtures: `rebuild-workspace/fixtures/s<N>-<name>/` with `answer-key.json`, one or more transcript or input files, and for s11 to s25 a `README.md`. `rebuild-workspace/fixtures/COVERAGE.md` holds one row per fixture.
- Work files for this pass: `rebuild-workspace/fixtures-work/_fixpass/<fixture-id>/` (create it): `changes.md` (the editor's log), `coverage-row.md` (the fixture's new COVERAGE row, one line, same columns as the existing row), `verify.md` (the verifier's report). Nobody edits `COVERAGE.md` directly during the pass; a merge step does it at the end.
- The quote verifier: `rebuild-workspace/fixtures-work/_fixpass/verify_quotes.py` (written in the first step). `python3 verify_quotes.py <fixture folder>` checks every structured quote in the key at its cited location and reports misses; `--spans` lists the quoted spans per transcript unit. Editors run it before handing over; verifiers run it again.

## 2. Rules that apply to every file

- Fictional only. The fixtures name no real person, firm or account; keep every name as it is or invent in the same register. "The user" for the consultant; "the Consultant" is the fixture's own speaker label and stays.
- No sales vocabulary enters the `readiness` block: no R-numbers, grades, gate names or verdict words. The key's existing `rubric`, `expected_verdict` and `numbers` fields stay untouched; they are v2 material.
- JSON stays valid, UTF-8, with the file's existing indentation; field order is kept (the 25 fields in the s1 to s10 order, then `intake` where it exists, then `readiness` last). Load, change, dump; never hand-edit a large JSON file with string replacement.
- A quote cited anywhere in the key is verbatim at its location. Any new quote the block introduces is copied from the transcript, not retyped from memory, and carries a location in the file's own grammar.
- Calm prose, short sentences with reasons, in every Markdown file you write.

## 3. The `readiness` block, field by field

Add `readiness` as the last top-level field of every key. Field names are final; the record map pins them in this pass.

```
"readiness": {
  "schema": "readiness/1",
  "note": "Derived from this key's pains, entities, products, structure, forks and questions in the fixture fix pass of 2026-10-13. Structure assertions stay provisional until the user has seen a real build (FEEDBACK, top).",
  "pains": [ {"id": "P1", "quote": "…", "location": "…", "speaker_role": "…", "stated_or_excavated": "stated|excavated", "outcome": "the wanted outcome in the client's words, or null"} ],
  "signals": [ {"quote": "…", "location": "…", "pain": "P2", "not_confirmed": "what our side never confirmed"} ],
  "entities": [ {"name": "…", "parent": "… or null", "moves_independently": "yes|no|unknown", "shared_resource": true|false, "goes_stale": true|false, "source": "spoken|observed|documented|assumed", "evidence": "location or null"} ],
  "structure": {
    "products": ["Work Management", "CRM", "Service"],
    "build_target": "own-account|client-account",
    "build_target_reason": "prospect, so the user's own account by default (A21) | existing customer with a live account of their own (A21)",
    "workspaces": ["<Client> – Ops", "<Client> – CRM"],
    "native_reuse": "which native boards, or 'none: no CRM or Service entity'",
    "leanings": [ {"question": "…", "option": "…", "quotes": ["…"], "locations": ["…"], "condition": "the live condition that settles it", "pattern": "one of the seven sweep patterns, or 'fork' for a disagreement between two client speakers"} ],
    "patterns": ["parent-row-with-roll-up: <parent> with <children> as child rows, <roll-up> on the parent"],
    "element_per_pain": [ {"pain": "P1", "element": "…", "verdict": "fixes|copies-today's-tool|none"} ]
  },
  "existing": {"account": "what the key's account_context and the record say exists, or 'unknown, no account bound'", "incumbents": [ {"system": "…", "authority": "stays system of record for: … ; follower for: …", "evidence": "location or null"} ]},
  "assumptions": [ {"statement": "…", "question": "the question that would replace it"} ],
  "unmet_needs": [ {"need": "…", "clock": "… or null", "why_not_met": "…"} ],
  "ai_opportunities": [ {"pain_or_need": "P3", "kind": "agent|ai_column|workflow|vibe_app|sequence", "round": 1|2, "probe_basis": "P-19|P-20|P-21|unprobed", "idea": "one sentence"} ],
  "verdict": {"cleared_for": "build|build-generic|none", "conditions": ["approval stop", "A11-2 asked first (client-account target)", "…"], "reason": "one sentence"},
  "questions": [ {"text": "…", "kind": "read-back|discovery", "role": "who can answer", "known": "what the record already holds"} ]
}
```

Rules for filling it:
- `pains` reuses the key's own `pains` entries (the same quotes and locations) so nothing new needs verifying; `id` follows the key's P-numbering.
- `signals` holds client ties our side never confirmed; they are carried forward, never counted as evidence.
- `entities` answers "what moves independently of what?" for every entity in `entities_and_workflows` and any the pains name. `shared_resource` is true for anything booked or reused across jobs; `goes_stale` is true for anything produced from data that later changes.
- `structure.element_per_pain` answers "does this structure fix the pain, or copy today's tool?" for every pain. A pain with `none` is a finding and stays visible.
- `structure.leanings` is where every sweep hit and every fork lands: the question, the leaning, the quotes it rests on, the condition that settles it. A fork keeps its existing entry elsewhere in the key and gains the same `leaning` there.
- `build_target`: `own-account` for a prospect; `client-account` only where the fixture is an existing customer with their own live account (A21). `workspaces` follow the A21 rule, one per product, named after the fictional client.
- `verdict.cleared_for`: `build` when at least one pain has an entity and a wanted outcome, the product is chosen, the structure is stated with its leanings and the build target is named; `build-generic` when the structure rests mostly on assumptions (the thin case); `none` when no pain or entity is firm enough. `conditions` always lists the approval stop, and the A11 question that first matters where one does.
- `questions`: at most five, ordered, each a `read-back` where a signal exists and a `discovery` question otherwise, each routed to a role, each saying what is already known. Reuse the key's `expected_questions_before_building` where they fit, reworded in build terms.
- `ai_opportunities`: at least one where any pain admits an AI element; `round` is 1 only when the client asked for AI or workflows on the call.

## 4. The other changes

- **`direction` rename (s11 to s25):** `intake.type_header.direction_of_show` becomes `direction` wherever it appears in the key, including inside `intake.files[]` headers of a package. The README's prose follows if it names the field.
- **The seven-pattern sweep (every key):** one row where the call describes many; a pain with no element that fixes it; an alias-map entry that names more than one entity; our framing labelled as the client's; a shared resource with no reservation tracking; an artefact that can go stale with nothing to flag it; an expected output the input cannot support. Each hit becomes a `structure.leanings` entry, never a silent restructure; where the hit is in an existing field (a stage list, an alias entry, an expected output), that field is corrected too and the change logged.
- **The "never written to" rule (every key):** every claim that a client system is never written to, not written back to or never touched must trace to a client quote; where it traces only to "stays the book of record" or to our own sentence, it becomes "writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the system is our safe default, labelled as ours". Log each occurrence.
- **Standing lines, applied where they bite:** a board status set by a person is a claim, never evidence that the source system changed (s22); a commitment made on a call is `committed`, with owner, purpose and when, and becomes done only on evidence (s21); inference targets questions and never fills evidence (s11); a product limit never deletes a client need (s15).
- **The fixture's own entry in FEEDBACK.md:** apply every change it records, exactly as recorded, including the quotes and line references it gives. s17 and s25 have no fixture changes.

## 5. Transcript edits

- Only two kinds: the changes a FEEDBACK entry asks for, and the mess pass of the s11 rule ("our side's speech gets the same mess pass as the client's"), applied with judgment to s12 to s25 where the user's side speaks in writer-clean paragraphs.
- The mess pass edits inside existing units only: false starts, navigation filler, a repeated half-explanation, an unfinished clause, added to turns that are not quoted or added around a quoted span, never inside one. The number of units, their numbering and their timing lines do not change. Only word counts move; the README and the coverage row are updated for them.
- s11 is the one exception: its review asks for a mid-tour interruption and a two-turn version of the "instant principle" reply, which means new turns. After them every location in the key, the README and the coverage row is re-cited with the verifier's help, and the whole key is re-verified.
- Run `verify_quotes.py` after any transcript edit; zero misses before handing over.

## 6. What the editor hands over

`changes.md`: every change by file and field, with the FEEDBACK item, sweep pattern or rule it answers; the verifier's output pasted at the end; a count of readiness questions, pains, entities, leanings. `coverage-row.md`: the fixture's full COVERAGE row with every count true of the edited files, the Review column reading `reviewed 2026-10-13; fix pass applied 2026-10-13`. For s1 to s10, whose rows sit in the first table of COVERAGE.md with three columns, the row keeps its three columns and the fourth column is not added.

## 7. What the verifier checks

JSON validity and field order; `readiness` present and complete in the shape above; `direction` renamed and `direction_of_show` absent; every pain of the key present in `readiness.pains` and in `element_per_pain`; every entity with a parent carrying `moves_independently`; at most five questions; a valid `cleared_for`; no sales word in the block; the "never written to" rule applied; the FEEDBACK items of the fixture applied as recorded; `verify_quotes.py` clean; README counts and the coverage row true of the files; transcript edits inside existing units with unchanged unit counts (except s11). The report lists each check as pass or fail with the evidence, and ends PASS or FAIL.

## 8. Settled after the exemplars (2026-10-13)

The two exemplars, `_fixpass/s1-discovery-strong/changes.md` (strong case) and `_fixpass/s5-intro-thin/changes.md` (thin case), are the worked examples. Read both before editing; their "What the exemplar teaches" sections are now rules:

- **The old verdict fields stay, and the block says so when they disagree.** `should_plugin_propose_a_build`, `expected_verdict`, the "do not build" traps and the matching `accepted_behaviours` lines answer the v2 sales question and are not edited. The readiness block answers the v1 question by the brief's own definitions. Where the two disagree (s5 says `false` and `build-generic`; s2 and s10 may too), the block's `note` gains one sentence: "The key's `should_plugin_propose_a_build: false` and its verdict answer the v2 sales question; under A19 and the user's decision of 2026-10-13, thin input clears a generic build with its assumptions listed." Never flip the old field.
- **Pain ids.** Keep every pain entry the key holds, with its own quote and location. Where the key groups several quotes under one theme, number them `P1.1`, `P1.2` and so on, and give an unnumbered pain the next free number, saying so in `changes.md`. Every entry gets its own `element_per_pain` row.
- **`copies-today's-tool` is the honest verdict** when a structure fixes the pain only once an integration or a data feed exists that v0.1 does not have; the leaning and a question carry the dependency.
- **Correcting a field versus adding a leaning.** A sweep hit corrects an existing field when a builder reading that field alone would build the flaw; when the field is only incomplete, the leaning carries the addition and the field stands.
- **A sweep that finds nothing is a result.** Write "no hit" for the pattern with the nearest candidate named and why it was declined. Never force a leaning to fill a pattern; that would be our framing labelled as the client's.
- **Choosing the five questions.** Keep a question when a build element changes with its answer or a client signal exists to read back; everything that falls out stays in the record as an assumption with its question. Under A21 the "which monday account" question is not one of the five for a prospect.
- **Workspace names** use the en dash as the brief shows, which makes a formerly ASCII key UTF-8; that is fine.
- **Verifier discipline.** Run `verify_quotes.py` after every change to a key or a transcript, not only at the end. When units are renumbered (s11), read the location notes as well as the misses: a citation whose index still points at a unit with a different stamp is a note, not a miss, and still has to be re-cited.
- **Package and multi-file fixtures** (s22, s24, s25): the mess pass touches transcripts only, inside existing units; documents, images and chat files are not edited.
