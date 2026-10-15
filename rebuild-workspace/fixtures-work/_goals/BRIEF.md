# The goals pass — brief for each batch agent

Written 2026-10-14. You add the readiness `goals` list to a batch of fixture answer keys and classify each readiness assumption. You change nothing else in any key.

## Paths
- Fixtures: `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/<fixture>/` — `answer-key.json`, the transcript or transcripts (`.txt`), sometimes documents, and a `README.md` on s11 to s25.
- Helper: `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_goals/add_goals.py` (read its docstring).
- Verifier: `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_fixpass/verify_quotes.py <fixture folder> --json` (its docstring explains statuses and the location grammars).
- Your plans: `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_goals/plans/<fixture>.json`.
- The log: `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_goals/log.md` (append; create with a title line if missing).
- Baseline verifier results (before this pass, all zero misses): `~/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures-work/_goals/baseline/<fixture>.json`.
- The shape, pinned: `~/DelOps/monday-master-builder-dev/monday-master-builder/plugins/monday-master-builder/shared/record-map.md`, section "Pinned: readiness", rows `goals[]` and `assumptions[]`. The design reason: `~/DelOps/monday-master-builder-dev/rebuild-workspace/design/AMENDMENTS.md`, A27 (readiness opens with goals and pains, so the user sees what the client wants before what hurts).

## Per fixture, in order
1. If the key's `readiness` already has `goals`, or `plans/<fixture>.json` exists and the log has a line for it, skip it (the pass is resumable).
2. Read the key's `readiness` block (note, pains, assumptions, structure.leanings) and enough of the key's other fields (`company`, `attendees`, `pains`, `call_type`) to know who is on the client side. Read the transcript(s) and documents in full; goals are often said early or late in a call, not where the pains are.
3. Find the client's stated goals (rules below). Write the plan file: `{"goals": [...], "assumption_kinds": [...], "note_add": null}`; goal fields exactly `id, goal, quote, location, speaker_role, pains`, ids `G1`, `G2`, … in the order the record first shows them.
4. Apply to a scratch copy first: copy the whole fixture folder to `/private/tmp/claude-501/-Users-caramelm4-DelOps/66f8eb44-eca9-44b9-8727-28498c028b8a/scratchpad/goals-try/<fixture>/`, run the helper on the copy, run the verifier on the copy. Every goal quote must come back `verified` (not near-miss, not miss), and the totals must be the baseline's plus your goals. Fix the plan and retry on a fresh copy until clean.
5. Apply the same plan to the real fixture folder, run the verifier on it, and confirm the same counts.
6. Append one log line: fixture, goals count, the goal ids with their pain links, assumption kinds tally, verifier pairs/verified/misses/near-misses before and after, and any judgment call worth the user's nod in one sentence.

## What counts as a goal
- A goal is what the client wants to achieve or to be true: an aim, a target, a state of affairs they are working towards ("one place where we can see…", "the audit finding closed before the renewal", "stop chasing people for…", "grow to…"). A pain is what hurts today; a goal is where they want to get. They often relate: link a goal to the pains it answers through `pains` (ids from that key's `readiness.pains`; an empty list is allowed).
- Said by a client-side speaker, in their own words. Our side's framing, recaps, playbacks and demo narration never count, even when the client agreed with them ("yes, exactly" to our sentence is not their goal in their words). In a handed-over package, a figure or aim the handing-over seller re-quotes is second-hand and does not count. In a client document, a stated objective counts, cited in the document grammar the key's own quotes use.
- Prefer few, strong goals: usually one to four. A thin input may have one or none. Do not restate every pain's wanted outcome as a goal; a goal is broader than a single pain's outcome, or is stated as an aim in its own right.
- `goal` is a short paraphrase (at most fifteen words) that keeps the client's vocabulary; no product terms, no monday jargon.
- `quote` is verbatim: one clause or one sentence, an exact substring of the cited unit (the verifier normalises whitespace, straight and curly quotes, and ellipses only). `location` uses the same grammar the key's existing quotes use for that transcript or document; copy the form of a nearby pain's location. `speaker_role` follows the style the key's pains use for that speaker.
- No goal stated anywhere: `"goals": []` and `note_add` with one sentence saying the input states no goal and the questions carry it.
- Name no one who is not already in the fixture. The fixtures are fictional; their characters' names may appear in locations as the key already writes them.

## Assumption kinds
One per entry of `readiness.assumptions`, in order (the helper adds `"state": "assumed"` to all):
- `board-architecture`: what is a board, a group, an item or a subitem; how boards relate, connect, mirror or roll up; which workspace or product something lives in.
- `automation-condition`: a trigger, condition, threshold or recipient of an automation, workflow, sequence or notification.
- `call-type`: what kind of call or input this is, or who was presenting.
- `leaning`: the assumption restates or depends on an open structural question or fork recorded in `structure.leanings`.
- `gap`: anything else the build fills by assumption (a fact, a figure, a label, an owner, a process step).
Pick the most specific that fits; when torn between `gap` and another, choose the other only if the assumption would change the build's structure or an automation.

## Rules
- Change nothing in a key except through the helper. Do not edit the transcripts, documents, READMEs or any other file outside `_goals/plans/`, `_goals/log.md` and the scratch folder.
- Calm, plain prose in the log. Name no real person, firm or account.
- Return only: the fixtures done, the total goals added, and any fixture you could not finish with the reason. Two or three lines.
