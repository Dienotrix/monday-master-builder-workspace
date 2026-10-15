# s14-shred-block — fix pass changes

Editor's log, 2026-10-13. Everything here is fictional and stays fictional.

Files touched: `fixtures/s14-shred-block/answer-key.json` and `fixtures/s14-shred-block/README.md`. `transcript.txt` is unchanged (415 units on 829 lines; see section 8). The key was loaded, changed and dumped by script. The file keeps a compact style (top-level fields and their direct children expanded, inner objects one per line), which `json.dump` would have reflowed, so the script carries a serializer that reproduced the untouched file byte for byte before any change; the diff outside the new block is 17 lines, the 18 field edits logged below (two land on the same `expected_structures.notes` line). The 25 fields keep their order, `intake` stays 26th and `readiness` is the 27th and last. Every quote the block introduces was copied from the transcript and proven verbatim at its cited line inside the script before the file was written (34 proofs), and the ten pain quotes were re-proven at their lines as well. The key is UTF-8 now (one en dash in the workspace name); the transcript stays ASCII.

Authority order followed: the s14 entry of `for-review/FEEDBACK.md` (lines 95 to 107) for the fixture's own changes; the cross-fixture patterns and the standing lines of s11, s14, s21 and s22 for the sweep and the rules; the brief and its section 8 for the block's shape and the judgment calls; the spec's sections 2, 7, 8 and 9 for what the block answers.

## 1. The review entry's changes, exactly as recorded

**Item 1: "two hundred colliding lines", our number promoted to a client fact.** The figure is the Consultant's ("Two hundred lines, not two thousand.", L721, 51:32) and Aileen answers with her capacity ("I could do two hundred lines in a day and a half.", L723, 51:49). The client's rule for finding the kit is at L293 ("It's whatever we only have a few of."). Every place the key treated the figure as known now says the first step is to identify the scarce, collision-prone kit by that rule and count it from the data, with about two hundred recorded as our proposed clean-up size, not a client count:
- `rubric[R9 Blockers surfaced].note` (the entry's key line 38): "the two hundred colliding kit lines fixed first" became "the scarce, collision-prone kit identified by Aileen's rule and fixed first (about two hundred lines is our proposed clean-up size, not a client count)".
- `rubric[P4 Concrete].note` (key line 61): "the colliding kit is about two hundred lines" became the rule, the count from the data, the Consultant's figure labelled as ours, and Aileen's day and a half named as her capacity against that figure.
- `rubric[P4 Workaround].note` (key line 62): "a day and a half for the two hundred lines that collide" became "a day and a half for the scarce kit, against our proposed size of about two hundred lines".
- `rubric[P4 Cost inputs].note`: the same phrase, same correction (not cited by the entry; same pattern, so logged).
- `vocabulary["walls / racks / desks"].likely_monday_object`: "the first two hundred lines to load" became the rule, the count, and the figure labelled as ours.
- `commitments_and_next_steps[7].what`: "a day and a half for the two hundred colliding lines" now names the Consultant's figure at L721 and Aileen's capacity at L723.
- `expected_questions_before_building[1]`: the question now asks which kit is scarce by the client's rule and how many lines it is once counted, with the figure labelled as ours.
- `expected_structures.notes`: "the two hundred colliding lines are the first data in" became the identified-and-counted kit as the first data in, with the figure labelled as ours.
The rubric edits are to `note` fields only. The brief keeps `rubric` untouched as v2 material, but the review entry names these lines by number and the brief says to apply its changes exactly as recorded, and FEEDBACK sits above the brief in the authority order; no grade, quote or location in the rubric changed. The pain quotes at L293 and L723 stay as they are; they are client words and the entry does not change them.

**Item 2: "the hire system is never written to", unsupported.** The book-of-record sentence is ours (L715) and the client's yes is at L717; nothing on the call establishes a no-write rule. Each of the four occurrences the entry names became the entry's wording, and where the field kept other content it was kept:
- `vocabulary["the hire system"].likely_monday_object` (key line 93): "nothing written back" became "Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the hire system is our safe default, labelled as ours".
- `integrations_mentioned[0]` (key line 117): "Nothing is written back; whether a booking reference or a kit export can be read from it is a question, not a promise" became the unresolved wording followed by the same question sentence.
- `expected_questions_before_building[3]` (key line 204): "Nothing is written back either way." became "Writeback and integration direction unresolved; v0.1 does not depend on either."
- `expected_structures.notes` (key line 247): "the hire system is never written to and never duplicated" became "the hire system is not duplicated (the managing director's first question, relayed by Meera at L557); writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the hire system is our safe default, labelled as ours". "Not duplicated" stays because it traces to a client line (L557, relayed, and L561 "If he thinks this is a second hire system, it stops there.").
The entry's rule applies to every key, so the rest of the key was searched too; section 3 has the result.

**Item 3: wedge detector, "not evaluable", not "found nothing".**
- `accepted_behaviours[6]`: the acceptable answer is now "ran; not evaluable, no end times" in any wording that gives the reason; "did not run" stays unacceptable, and "found nothing" without the reason is unacceptable too, with the entry's reason (negative evidence against missing observability) written in.
- `traps[5]`: "it runs, reports nothing, and says why" became "it runs and reports that it is not evaluable because no end times exist, and says so", with the "found nothing" trap added.
- `intake.detectors.wedge_flagger`: "reports nothing and says why" became "ran; not evaluable, no end times", with the same reason.
- README, defects table: "wedge flagger runs, reports nothing (no end times), says why" became "wedge flagger ran; not evaluable, no end times (missing observability, never 'found nothing')".
`intake.wedges` stays an empty list and the README's "0 wedges" count stays: no wedge was detected, and the block now says why that is not the same as none being present.

**Left as is, by the user's call:** the cross-speaker reconstruction of the headline figure; the key cites L469 alone for the grade and stores the reconstruction as a `[Q/recon]`, so nothing changed there.

## 2. The direction rename

`intake.type_header.direction_of_show` became `direction`, in place, key order kept (the value `no-show` is unchanged). No other occurrence exists in the key; the signal named "same-side screen direction" is a signal label, not the field, and stands. The README never names the field, so its prose did not move. A search of the written file for `direction_of_show` finds nothing.

## 3. The "never written to" rule across the key

A search for "written to", "written back", "write back", "writeback", "never touch", "read-only", "one way", "writes nothing" and "not written" found exactly the four occurrences the review entry names (section 1, item 2), all reworded. Checked and left, because each traces to a client line: "sub-hires are recorded on the show and never ordered from it" in `vocabulary`, `traps[18]`, `requested_changes[3]` and the products entry, which rests on Meera's "Agreed. The hire system raises those." (L713); "the hire system stays the book of record" wherever it appears, which rests on the client's yes at L717 to our sentence at L715, and the key already labels whose sentence is whose. The new block uses the rule's wording in `existing.incumbents[0]`, leaning 3, assumption 7, question 3 and a verdict condition; no client line on this call says anything about writing to the hire system, so no stronger statement is available.

## 4. The seven-pattern sweep

Each pattern was checked against the transcript and the key. A hit became a `structure.leanings` entry; an existing field was corrected only where a builder reading it alone would build the flaw (brief, section 8, fourth rule).

1. **One row where the call describes many.** Two hits.
   - Crew. The grid is shows by days by names, pencil until confirmed (L175), and the need is counted in bodies and trades (L171). One people column on a show would carry one value for many people with their own trade, day, call time and confirmed state. Leaning 2: assignment rows under the show with needed-against-confirmed rolling up. `vocabulary["the grid"]` already says "people or crew items assigned by day", so it stands.
   - Kit. One line per kit item per show with a quantity and a hold window, rolled up per item per date; this is also the pattern 5 hit and is leaning 1. `vocabulary["kit / kit list"]` says "connected items or subitems on the show ... the collision view across shows", which is incomplete, not wrong; it stands and the leaning carries the roll-up.
   - Considered and declined: the show's phases as a single status. The key already gives dates per phase (`vocabulary` prep and load-in entries) and a per-case checked-in state, so one status is not the whole shape; the phase list is handled under pattern 4 instead.
2. **A pain with no element that fixes it.** Three hits, kept visible in `element_per_pain`.
   - P4.1 (asset records a fifth wrong, Dunmere outside the system): nothing in the build touches the hire system's records; the fix is Aileen's clean-up, a client task. `none`, with leanings 4 and 8 and an unmet need.
   - P6.1 (crew chiefs get told): no board element gives them a say; the Wednesday call is a commitment. `none`, with leaning 9 and an unmet need.
   - P3.1 (the hire system thinks kit is still out): check-in rows in monday are Aileen's claim that a case is back and the hire system is still typed separately, so until integration direction is resolved this is a second place to record a return. `copies-today's-tool`, with leaning 3; the honest verdict under the brief's section 8, third rule.
3. **An alias-map entry that names more than one entity.** No hit in the pattern's sense (distinct people collapsed into one person). The nearest candidate is "the lads", which resolves to Aileen's two unnamed warehouse staff. Splitting it would invent two people with no names, which the entry's own method forbids. **Field tightened:** `intake.roster.alias_map[1].state` now says it is a group label for two people, neither resolved individually, and that no user or crew record is made from it. "Ferris" resolves to one person and stands.
4. **Our framing labelled as the client's.** One hit (the review entry's item 1, the two hundred lines; leaning 4) and one soft hit. The five-phase list (prep, load-in, show days, load-out, check-in) is the Consultant's enumeration at L699, accepted by Dermot's "It isn't. That's right." (L701); the client used four of the five words themselves across the call, and "show days" is ours. **Field corrected:** `vocabulary["show"].likely_monday_object` now says whose list it is and gives a date per phase; leaning 5 carries the question with the key's own question 5 as its condition. Checked and left, because already labelled: the December switchover window (ours at L581, adjusted by the client at L583), the book-of-record sentence (ours at L715), "the four or five of you who plan" (ours at L611; now also assumption 5), and the four-piece first cut (played back by us and agreed by Meera at L735 "subject to Ferris hearing it").
5. **A shared resource with no reservation tracking.** Two hits.
   - Kit across shows, the centre of the fixture: "On paper both shows owned them." (L103) and "they were never coming back in time" (L99). The key's "collision view" names the symptom without the reservation. Leaning 1: kit lines with a hold window from the prep day to check-in, rolled up per kit item per date against the owned quantity; the condition is the one-show kit list Aileen is sending and her confirmation of the hold window.
   - Vehicles: "what vehicle" (L47) and "The vehicle plan" (L385) are per show and change when a show moves, and nothing in the key tracks them. Leaning 6: a vehicle field and a transport-company-booked flag on the show in v0.1, rows of their own only if Dermot says two shows ever want the same van; the condition is his answer. Not forced further: nobody said a van was double-booked.
   - Freelancers across shows: the pencilled grid is their reservation today and leaning 2 keeps it as assignment rows; nobody said one freelancer is ever pencilled on two shows, so that is the leaning's condition, not a claim.
6. **An artefact that can go stale with nothing to flag it.** Three hits.
   - The kit list spreadsheet: it changes twice more before a show (L311) and the typed copy in the hire system is a week out or never (L161). Leaning 7: the kit lines on the show are the single list, the one-show spreadsheet is imported as sample data with its import date shown, and the spreadsheet is not kept in parallel; the condition is Moira, who was not on the call.
   - Check-in and the hire system's picture ("a picture of about two weeks ago", L297): leaning 3 puts who and when on every check-in row and says the board state is a claim (s22).
   - The Kit board's own lines: kit sold or bought goes stale on the board as it did in the hire system (L589). Leaning 8: a last-verified date and a verified-by per scarce-kit line, editable by Aileen herself (L745).
   No existing field was wrong on this pattern; `vocabulary["check-in"]` and `["kit / kit list"]` are incomplete and stand.
7. **An expected output the input cannot support.** No hit, after re-measuring. Every statistic the key and the README assert was recounted from the file: 415 units on 829 lines, 6,448 spoken words with bracketed cues excluded, client share 0.603 by words (Meera 28.5, Dermot 17.5, Aileen 14.3 percent), 172 Consultant turns, 40 lowercase-initial, 32 unterminated and 57 short units, five collisions at L119/L121, L243/L245, L277/L279, L367/L369, L463/L465, one inversion at L449/L451, one adjacent same-label pair at L751/L753, the 174-word block at L205, the longest own-side unit 72 words at L21, four `[laughs]` and one `[crosstalk]`, no ellipsis, ASCII, LF. All true. The dates were checked against the s15 standing point (never pin a month from a weekday alone): here two weekday-date pairs (Friday the second, Tuesday the sixth) plus the season words fix the month, and the key already labels the year as inferred and the call date as unstated, so the commitment date stands. The bleed and upside figures are the client's own words with the arithmetic labelled ours.

## 5. Standing lines, where they bite

- **s22 (a board status set by a person is a claim, never evidence that the source system changed).** Bites hardest here, on check-in. Leaning 3, `element_per_pain` P3.1, `existing.incumbents[0]`, unmet need 1 and a verdict condition all say that a checked-in state on the board is Aileen's claim that a case is back, that marking it back in the hire system stays a separate typed step, and that the walkthrough shows the queue and says what it does not show. The same applies to the kit list typed into the hire system a week out (incumbent 2).
- **s21 (a commitment is `committed`, with owner, purpose and when; done only on evidence).** Three commitments bite on the build and are verdict conditions in that state: Aileen's kit list and grid photograph ("I'll do it today and then it's done.", committed, not received), Dermot's crew-chief call (Wednesday afternoon, committed, not done), Meera's ask to the finance manager (Thursday, committed, not done, carried and not a build dependency). The key's eight `commitments_and_next_steps` entries each carry owner, purpose and a date or "date not stated" and none is recorded as done; the invite entry says "Sending it now." and not "sent", so it stands. The R10 note's "The invite is sent during the call" sits in `rubric`, which this pass does not grade-edit; noted for the v2 pass. No status field was added, since that would change the shared shape; one decision for all twenty-five keys if the planner wants it.
- **s11 (inference targets questions; it never fills evidence).** Six unconfirmed client ties are in `signals`, each naming what was never confirmed, and two of the five questions are read-backs of them (Q1 reads back L705 and L293; Q4 reads back L545 and L557). The composite block's "I build the show list off the design" is a signal with its side-only location and drives question 5, never an entity's evidence. The entities whose shape is inferred (the hold window, the quantity, the trades) are assumptions with their questions, not entities with locations.
- **s15 (a product limit never deletes a client need).** Seven `unmet_needs` keep what the build does not meet, with the client's clocks where given: the hire system becoming true on check-in; a change reaching freelancers and the transport company (January); a say for the crew chiefs (December); the asset records and Dunmere (December; February); the finance manager's figures (Thursday); the one page for the managing director (before the November budget round); loss traced below the case (no clock).

## 6. The readiness block, field by field

- `pains`: the key's ten `pains` entries in array order, same quotes and locations, numbered theme first and running number after the dot (brief, section 8, second rule): P1.1 to P1.3, P2.1 and P2.2, P3.1 and P3.2, P4.1, and the two unnumbered entries as P5.1 (the wall-of-colour impression, which the key calls a constraint, not a pain) and P6.1 (crew chiefs get told). P1 to P3 are excavated as the R2 note says; P4, P5 and P6 are stated. `outcome` is verbatim from the client: Meera's whole ask at L533 for P1.1 and P1.2, her "I'd settle for taking the double-booking part out of it" (L545) for P1.3, Dermot's L535 for P2.x, Aileen's L537 for P3.x, her "You could give me the two weeks in December." (L597) for P4.1, "Don't make me look at a wall of colour." (L749) for P5.1, and null for P6.1, where no outcome words exist.
- `signals`: six (section 5, s11).
- `entities`: twenty-four, answering what moves independently of what. Kit lines, crew assignments, sub-hires, check-in and call times move independently of the show; the kit item, the freelancer, the crew chief, the project manager and the vehicle plan are shared across shows; the kit list spreadsheet, the hire-system booking, the asset records, the Kit board's scarce flag and the grid go stale. Every entity with a parent carries `moves_independently`; all are `spoken` with a location, because every one was named on the call.
- `structure`: Work Management only; `own-account` because the firm is a prospect with no account of any kind (A21); one workspace, "Norhaven – Ops", named for the fictional client with the brief's en dash; native reuse none, no CRM or Service entity; nine leanings (sections 4 and 5); three parent-row-with-roll-up patterns (kit lines, crew assignments, check-in rows); ten `element_per_pain` rows (seven `fixes`, one `copies-today's-tool`, two `none`).
- `existing`: "unknown, no account bound" with the client's own words at L275 and the A21 point that the user's own account is read at preflight; six incumbents with what each stays the record for, the hire system carrying the unresolved writeback wording.
- `assumptions`: fourteen, each with the question that would replace it; one is routed to the user (which realistic values may appear in sample rows).
- `unmet_needs`: seven (section 5, s15).
- `ai_opportunities`: four, all round 2, because the client never asked for AI or workflows; the workflow cites P-21, the agent P-19, the Vibe app P-20, and the AI column is `unprobed`.
- `verdict`: `build`. Three excavated pains carry entities and wanted outcomes in the client's words, the product is chosen, the shape is stated with its leanings and the target is named. Nine conditions, starting with the approval stop and the A11 point (no A11 question first matters for an own-account build; the three decisions stay open), then the count of the scarce kit, the three commitments in their committed state, the open ordering for the sixth, the unresolved hire-system direction and the sample-data rule.
- `questions`: five, the ceiling. Q1 and Q4 are read-backs because signals exist; Q2, Q3 and Q5 are discovery. Each is routed and says what is known. Reused from the key's pool of ten: item 2 (Q1 and Q2), items 4 and 8 (Q3), items 3, 6 and 7 (Q5). Dropped from the five and left in the record: which monday account (item 1; under A21 the proof of concept goes into the user's own account, so it moves to handover and sits in `existing.account`), the phase list (item 5; assumption 4 and leaning 5), the sub-hire fields (item 9; assumption 8), and the ordering on the sixth (item 10; a verdict condition, not a structure question).
- No R-number, grade, gate name or verdict word is in the block; the script searched for them before writing. `rubric`, `expected_verdict` and `numbers` are untouched except for the four `note` fields the review entry names (section 1). `should_plugin_propose_a_build` is `true` and the block agrees, so the section 8 disagreement sentence is not needed.

## 7. README

`README.md` was brought in line: the files table now names the `readiness` block, the key's 503 lines and its UTF-8 encoding; the defects table carries the wedge wording of item 3; a readiness paragraph joins the counts with the figures above; the checks paragraph records the verifier's 191 pairs; and the review-history sentence closes the file ("Reviewed by the user 2026-10-11 ...; fix pass applied 2026-10-13: ..."). No other README count moved, because no transcript count, rubric count, pain count or trap count changed.

## 8. Transcript

No edit. The review entry asks for none, and the README records that a mess pass already covered the Consultant's side at review ("fifteen fillers, false starts and repeats across both sides at the second, because a consultant with no disfluency in 172 turns is a writer's artefact"); the file bears it out (L9 "from, from stranger places", L135 "to the, to the money", L319 "who else, who else", L391 "the, the working out", L551 "you know, gets made", L653 "Erm,", L677 "who, who needs to know"). Adding more would be a second mess pass on a file that already had one, with the renumbering risk and no gain, so the s11 rule is judged already met. Unit count, numbering and timing lines are unchanged.

## 9. Counts

| item | count |
| --- | --- |
| readiness questions | 5 (2 read-back, 3 discovery) |
| pains | 10 (P1.1 to P6.1) |
| signals | 6 |
| entities | 24 (18 with a parent, all with `moves_independently`) |
| leanings | 9 |
| patterns | 3 |
| element_per_pain | 10 (7 fixes, 1 copies-today's-tool, 2 none) |
| incumbents | 6 |
| assumptions | 14 |
| unmet needs | 7 |
| AI opportunities | 4 (all round 2) |
| verdict conditions | 9 |
| existing fields edited | 18 (4 rubric notes, 3 vocabulary, 1 commitment, 2 expected questions, 1 integrations entry, 1 expected_structures.notes twice, 1 accepted behaviour, 1 trap, 1 detector, 1 rename, 1 alias state) |
| transcript edits | 0 |
| key size | 503 lines, from 350; 27 top-level fields |
| verifier pairs | 191, from 154 |

## 10. Verifier output

`python3 -I fixtures-work/_fixpass/verify_quotes.py fixtures/s14-shred-block`, run after the last edit to the key (the README and coverage files touch no quote; a re-run after them reproduced this output), exit code 0:

```
Fixture: s14-shred-block
Sources: transcript.txt (transcript/line-time-first, 415 units)

pairs found      191
verified         191  (of which presence only, no location cited: 34)
skipped          0  (null, empty or a bare location pointer)
unparsed prose   0
near-misses      0
misses           0
unsupported      0
refused_quotes   8 entries in 1 list(s) are the key's own refusals and are not checked
```

No location notes were reported. The edit script's own walk proved 34 new quote-and-location pairs and the ten pain quotes at their lines before writing; the shared verifier's higher count includes the key's presence-only quotes in `objections`, `commitments_and_next_steps`, `requested_changes`, `numbers` and `account_context`.

## 10. The goals pass (2026-10-14)

Under A27 the readiness block now opens with the client's stated goals, in their own words, before the pains. This pass added `readiness.goals` and gave every readiness assumption a `kind` and a `state` (all `assumed`), the shape pinned in `shared/record-map.md`. Nothing else in the key changed; a script proved it by taking the additions back out and comparing with the key as it stood before.

| Goal | In short | Said at | Pains |
|---|---|---|---|
| G1 | Take on the framework's extra shows from January without hiring | L505, 35:12 Dermot Shanley | P2.1, P2.2, P3.2 |
| G2 | One thing showing every show for six weeks, its kit, and whether they have it | L533, 37:19 Meera Ganguly | P1.1, P1.2, P1.3 |
| G3 | The grid off the wall, so a show moving reaches the people it affects | L535, 37:34 Dermot Shanley | P2.1, P2.2 |
| G4 | Know on the Monday what's coming back and what hasn't been checked in | L537, 37:48 Aileen Rusnak | P3.1, P3.2 |

Assumption kinds: gap 7, leaning 6, automation-condition 1.

Verifier: 191 pairs, 191 verified, 0 misses and 0 near-misses before; 195 pairs, 195 verified, 0 misses and 0 near-misses after (the difference is the goal quotes).

Judgment calls for your nod:
- G1 is the crew and logistics lead's short answer at L505, which the operations director endorses at L507 and the key already cites for R5, and every goal quote is one whole unit, none inside the L205 composite block or across a shredded span; G2 to G4 are the "next March" answers the key also uses as the P1, P2 and P3 outcomes, kept because each covers a whole pain group, and the sub-hire target (halved, or the hundred and twenty-five taken out) was left out because the operations director says it is still to be settled with the managing director.
