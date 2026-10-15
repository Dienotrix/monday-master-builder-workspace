# Revision notes 2 — 2026-09-12

A plain record of what the second revision round changed in the design, why, what it reversed from the
first round, what it deferred, what is still open, and whether building can start. It follows
`REVISION-NOTES.md`, which records the first round (A1 to A11 and the live tests), and does not repeat it.

**What drove the round.** Three things arrived after the first round: the user's amendments A12 to A16
(`AMENDMENTS.md`) — no personal names, bespoke work recorded and handed off, one record per client with
strands inside it, a package of calls taken in as a set, and client documents as an input class; the
calibration against four real calls, 125 changes C1 to C125 in `REAL-CALL-LESSONS.md`, fifty of them
revised in the second pair of calls and several reversing a rule the first pair had induced; and, once the
revision passes had landed, three checks over the result — coverage, consistency and buildability — plus a
third leak lint. This file covers all of it: the revision passes (`revision-2-arch-pass1.md`,
`revision-2-arch-pass2.md`, `revision-2-build-plan.md`, `revision-2-spec.md`, `revision-2-method.md`) and
the fix pass that answered the checks (`revision-2-coverage.md`, `revision-2-consistency.md`,
`revision-2-buildability.md`; the leak-lint reports lived with the calibration folder and were deleted with it).

**Authority order, unchanged.** `AMENDMENTS.md` overrides `ARCHITECTURE.md`, which overrides
`BUILD-PLAN.md`; `SPEC.md` describes the product and defers to the same order; the method spec defers to
the amendments. Every document's header now reads A1 to A16.

---

## 1. What changed in each document

### SPEC.md

Grew from 2,359 to about 3,400 words, all of it where the amendments land.

- **One record per client, strands inside** in the opening, the lifecycle (six of twelve steps), the
  scope and the success criteria; the day-in-the-life narrative now has two strands, one of them
  non-platform, and every version and command is qualified (`001/v0.2`).
- **Every call is typed and routed by type**, in plain words rather than as a taxonomy.
- **Non-platform work is recorded and handed off** — no build, audit or demo — as a bullet, a lifecycle
  clause and an out-of-scope line that says deferred rather than rejected.
- **A package is taken in as a set and a client document goes through the same intake**, one sentence
  each in step 3, with the document fixture added to the discovery-grading criterion.
- **The next-step rule as scoped**: date, time and owner still required on a discovery or demo call; a
  mechanism with a named owner on a working session or an expansion.
- **One build at a time** as a safety bullet: one lease per record, a sibling told who holds it, local work
  unblocked — including, after this round's decision, a run-sheet for the sibling's own audited version.
- **The correction loop** in step 9: a run-sheet opens with what was said unsourced last time.
- **Open decisions** asked once per client where client-specific, possibly during a later strand, and
  never at new-client setup; retention covers documents.

### ARCHITECTURE.md

Two revision passes and one fix pass. No section was renumbered; 3.12, 7.7 to 7.10, 9.11, 9.12 and 12.7
are new and sit at the end of their sections, so every anchor the plan and the method cite still resolves.

- **Section 7 rebuilt around the per-client record** (pass 1): the `strands/` level with a record-level and
  a strand-level file map, `client/2` with the strand index and `prior_builds`, `account.json` beside a
  `build/2` ledger per strand, versioning moved to the strand with qualified references outside it,
  `STRAND.md` and `SUMMARY.md`, the live map with its three constraints, migration from `client/1`, and the
  reading contract that bounds what a fresh chat reads to summaries rather than history.
- **The contended lease** (9.8, pass 1; chat identity and the fence completed in the fix pass): one
  `build` lease per record in `lock/2`, an epoch fence, holder discovery in the briefing, the door and the
  hook, release on a clean stop, no expiry, a five-condition break with classify-only recovery over the
  holder and a resume-or-park choice.
- **The intake pipeline rewritten as measure-first** (5.4, pass 2): export family before parsing, the
  eight phases with merge first, both detectors on every file, identity by adjacency pair, four confidence
  states, thresholds from the file's own distribution; in the fix pass the script was split in two around
  the intake report, the permitted constants were enumerated and the short-file case defined.
- **Call typing and routing** (8.3 step 5 and 7, 3.3): four dimensions, two modifiers, five signals, a
  conservative fallback per dimension, per-segment typing, and — from the fix pass — one list of thirteen
  labels with a route for each, and `advisory` as a fourth grade status.
- **The grading rules** (3.3): cross-speaker composition, element-by-element grading, the non-evidence list
  with its carve-outs, the narrowed conflict rule, the three bleed states, the asked flag, not obtainable
  from this room, expansion mode, consumption as a design input, and the document rules of A16.
- **The demo run-sheet** (3.5): routing by type, the stop conditions, the skeleton, the countable budgets
  over planned showings, two check-ins with different jobs, the prep block with every field the calibration
  asked for, the close per type, numbers and claims; the corrections-from-last-meeting block from the fix
  pass.
- **Claims discipline as mechanism** (9.12) and **delivery-side confidentiality** (9.11): the store outside
  the record, the prep read, refusal never a range, the if-asked list, the correction loop, never the
  operational account on a screen, one access-request shape, credentials never named.
- **The voice specification** (3.12) with its regeneration path settled as a release step.
- **Non-platform strands** (7.9) and **hybrid strands** (7.7) as a structural boundary.
- **A16 in full** (fix pass): `inputs/` at record level under the open retention question,
  `record.py add-document`, `transcript_prep.py document`, the `document-summary.md` template, the
  `documented` source marker, the `[Q/doc]` marker and its tier, the grading rules, the intake paragraph with
  the one-path rule, the document-versus-call conflict, and the SOP started from the client's own.
- **The decision log**: 12.4 rows for A12 to A16 with the two decisions this round took recorded in A14
  and A15; 12.7 new, the eleven calibration reversals and the five rules deliberately not written; 13 with
  the lessons decisions 14 to 18 and the provisional-rules caveat; 14 with seven new risk rows.

### BUILD-PLAN.md

- **An eighteenth package.** WP18 writes the fourteen calibration fixtures and the document fixture in
  stage 1, because WP1 pins against their keys, WP5 is accepted on nine of them and WP14 grades them; left
  in stage 5 they would have been written unreviewed by whoever needed a green run.
- **Stage 1 pins every interface**, not only every schema: the intake report (`intake-report/1`), the
  `status --json` output, the strand-index row, the lock history entry, the permitted-constants table, the
  label list, and the A16 markers reserved now.
- **WP2 owns a unit-level record fixture**, so stage-2 tests have a record before templates or seed records
  exist; `init` is accepted with WP7.
- **WP3 names its raw-read sources**: two structure files cover 58 of the 67 boards, and the nine others are
  re-captured live before the ring rolls.
- **WP5 is two scripts** with an acceptance a builder can implement: enumerated constants, a
  moves-with-the-distribution test, the short-file rule, `set` ordering split between script and skill, and
  the `document` subcommand.
- **WP13 gets a hook script** with a unit test, and an acceptance rewritten to what a hook can read.
- **The correction loop is built**: the block in the template (WP7), the gate check (WP17), the writer and
  reader named (WP8, WP12), a planted deferred answer in r7 asserted in H16 (WP14).
- **Fifty-two headless rows** (H01 to H56 with H02 to H06 sharing one) and twenty-three sandbox scenarios;
  every reversal carries a test in both directions; H56 is the document run; H50 gains the unresolvable
  fragment; H37, H40 and H50 assert the quarantine in both directions; H35 and H36 carry the parked-strand
  path; the runner sets `MMB_HOME` to a temporary home.
- **Section 6** closes every live conflict: rows 12 to 16 are folded into the architecture and row 17
  records this round's counts. **115 rows, 111 installed files, ten scripts, 43 templates**, re-added.

### research-delops-method.md

- Five subsections appended (2.6 call type, 4.11 group calls, 4.12 voice, 6.6 handover, 7.1 claims in
  speech); every existing section number kept.
- The grading rules, the demo sections and the never-list carry the calibration's changes in their scoped
  form, with the table in `revision-2-method.md` recording where practice and the written method disagreed
  and which won.
- A16 in 2.1, 2.6, 3, 6, 7, 8 and scenarios 22 and 23; `advisory` as a status; parallel threads graded per
  thread; the restated-and-unanswered detector tied to the intake measures; the label list cited from the
  architecture; the set ordering split; the document row given its real path.

---

## 2. The structural changes

**The per-client record with strands.** The record is keyed to the client. Each piece of work is a strand
with its own versions, blueprint, ledger, audits, SOP and close-out; calls, research, the meeting register,
the account binding and the live map stay at record level. A later strand reads an earlier strand's 80-line
summary, never its history, and every reference that leaves a strand folder is qualified. Close-out is
two-level: a strand closes and archives nothing; the record closes when the relationship ends and that is
what triggers the archive and the cleanup — and it now refuses over a `paused` strand, whose parked run is
resumed first.

**The contended lease.** One `build` lease per record, held by one strand for a live run or a doc copy,
never by record-only work. A sibling is told who holds it, since when, what it may still do locally, and the
three ways forward. The take mints the chat label; the fence checks epoch, label and run id on every
account-affecting write, so a chat presumed dead cannot write even after a resume-first break has put a new
epoch into its own strand's ledger; the epoch and label are held in the chat and never re-read from disk.
The lock file and its two mirrors have exactly one writer, the primitives in `mmb_common.py`. A stale line
from another client warns and asks rather than refusing, because it has no break path from here.

**The call-type router.** Four dimensions, two modifiers, five priority-ordered signals each recording its
quote, typing per call and per segment, a proposal the user confirms and never a decision. Thirteen labels
with a route each — a pricing call under the audience rule, a call review carrying no client evidence, a
scoping call to the scope path. Where a dimension cannot be resolved the fallback is the value granting the
fewest rights; type-specific rules grade `advisory` and touch neither the verdict nor the gates; the doors
read the strand's kind and output class, which the user set, so nothing is claimed buildable on an
unresolved class and no door goes advisory (D26).

**The claims store.** `claims/<slug>.md` under `MMB_HOME`, outside the record because the record feeds
client-facing drafting and is archived whole. Created at binding; written by `call-intake` (claims spoken
on a call, a third party's, a deferred answer's figure, a previous seller's at package intake) and by
`demo-script` (figures read live at prep); every entry proposed to the user and counting only once approved.
Read at every prep, reaching cross-call contradictions only; in-call contradictions are the run-sheet's two
speech rules — refusal never a range, and a commitment to check carries no figure — and the correction loop:
the deferred-answer register feeds the next run-sheet's corrections block, which the gate refuses to leave
empty while the register is not.

**The bespoke-strand boundary.** A `non-platform` strand has `scope.md` and nothing that a build path has:
no blueprint, versions, ledger, SOP, lease, element kinds, build stage or audit. `record.py check` blocks
the files, the lease refuses the strand, both doors and the demo script refuse it, and `scope.md` ends with
a fixed sentence the front door repeats. A `hybrid` strand has both files and one written boundary. The
gates the product owns still apply to what such a strand writes. Designing the work is deferred, not
rejected.

**Two more this round produced.** Client documents as an input class beside transcripts, through the same
intake, stopped at the same open retention question, cited by section or page, kept apart from lived
process. And a measure-first intake split into a file-level script that ends in a pinned report and a
record-facing script that reads it, so the widest new interface of the round is a schema rather than an
agreement between two builders.

---

## 3. Rules reversed or scoped from round one, and why

Each row is a round-one rule that the second pair of calls, or a check, overturned or narrowed. The old
text is gone rather than scoped beside the new; 12.7 of the architecture lists the calibration's eleven and
the plan carries a test for each in both directions.

| Round-one rule | Now | Why |
|---|---|---|
| Format detection against a closed list of nine formats | Detection by measurement, family first; the nine shapes are fixture coverage | A third export grammar arrived; every constant was mis-sized in both directions |
| A quote never crosses a turn boundary | Never crosses a **speaker** boundary; a merged run is cited with its unit range | On a cue export two fifths of adjacent units share a label, so the old rule made almost nothing quotable while protecting nothing |
| Stop selling while the client is showing | Scoped to a current-state walk; interrogating a prototype they built is the work | The universal rule would have graded the best-run call as a violation |
| Every check-in to one named person, never to the room | Two instruments: the named one confirms, a room-wide open one discovers, once per phase boundary where the room holds stakes the record lacks | The open check-in was the only reason a silent attendee spoke, from a stake nobody could have named |
| Client tying a screen to a pain is a defect signal | It is what an interactive demo produces; the defect is an unconfirmed tie, and the confirmation ledger is the fix | The strong demo had ten client ties and went well |
| Segments never outnumber stated pains | The cap covers planned showings only; live answers are exempt and counted separately | Eighteen one-minute answers beat eight lectures |
| The latest client statement wins | Only for the same proposition, same speaker, one call; every other pair is a conflict kept as both, and a structural disagreement is a fork | Two figures minutes apart priced different line items; two calls contradicting each other are a gap question, not a merge |
| Next step needs date, time and owner on every call | Kept for discovery and demo; a mechanism with a named owner and client assent on a working session or an expansion | No call in the corpus fixed a new date; the differentiator was a mechanism |
| At most one question per segment, three or four in total | A cap on questions whose answers cannot change the next two minutes; document-answerable questions become artefact requests | Mid-demo discovery produced the call's best pain statement; the override is argued and provisional |
| Numbers stay in reserve and never on screen | No figure a run-sheet cannot source, read live at prep or user-approved; an unsourced figure is refused, never ranged | The worst numbers were spoken, not written; a range becomes the remembered price |
| A hard pre-call gate on screens that presuppose client data | The gate fires on the claim; current-state questions are the non-blocking mitigation; for scoping it inverts into an obligation | The screen was never the problem; the talk track was |
| Say the plan difference on every capability | Only for a plan-gated capability or a client-stated constraint | A caveat on every screen degrades a demo into hedging |
| A member or admin seat on the admin checklist | The lowest named seat that can perform the work; elevated rights separate with reason and duration; a client's login never named even hypothetically | Naming it produced an offer of a broader grant than the work needed |
| Pricing questions routed to "not part of this plugin" | Pricing stays out; metered consumption is a recorded design input | Consumption changes the run-volume design; evidenced in both second-round calls |
| The assistant-to-platform connection as the whole environment rule | Never the live operational account on a screen; every connection shown says what it may not change | The worst exposure in the corpus was our own board on a shared screen |
| Lengthen the close to hold the best material | The close keeps its minutes; a long open-question phase is protected before it | The long tail held no commitment question and no confirmation |
| One approval per automation (A1, first-round leftovers) | One list approved once, one grouped re-confirmation at execution, the switch-off flag retired | A1 settled it; the 3.7 description and the 9.1 row still said card-per-automation and are corrected |
| Retention asked at new-client setup (first-round leftover) | Asked once, before the first real transcript or document, never at setup | A11 says ask at the moment it matters; H01 asserted the opposite and is corrected |
| A demo script refuses while any strand holds the lease (pass 1) | Refuses only while its own strand holds it; a sibling's build is recorded in the prep block | The run-sheet is local work whose link check reads its own protected objects; the waiting message already promised it |
| Fixtures s11 to s24 written in stage 5 (pass 3 of the plan) | Written and reviewed in stage 1 as WP18 | Three earlier packages depended on them |
| One 560-line intake script (pass 2) | Two scripts around a pinned intake report | The budget was not credible and the interface had no schema |
| A hook that checks "this chat's strand" (pass 1) | A hook that checks only what it can read; chat identity is the ledger's fence | A hook has no chat identity |

**Deliberately not written**, on the calibration's evidence: a detector for two incompatible account
facts, a working-session mode beside expansion mode, a lengthened close, the named-only check-in, and
client tying as a defect.

---

## 4. Deferred, and what it waits on

| Deferred | Waits on |
|---|---|
| Designing or building non-platform work (A13) | The first real engagement of this kind; v1 records and hands off |
| Non-platform element kinds in the ledger, and a design-stage flow kind in `sop_tools.py` | The same; the two halves such a kind would reuse already exist, and a promotable design flow would remove a guard |
| Modelling the demo environment as an asset with its own state (decision 17) | A package giving it a state file; recorded per meeting and per run-sheet meanwhile |
| Grouping the live map by strand | An account outgrowing one table; 7.1's blocking budget says when |
| Any call-type cell the calibration did not evidence | Evidence; the scope matrix marks such cells unspecified and no behaviour is invented |
| Regenerating the smaller-seat voice shapes | A second call in that seat; then a release step the user runs on the Mac, never a client chat |
| Promoting any provisional rule (roughly twenty) | The second observation named beside each in the file that carries it; release check 10 confirms none moved |
| The nine boards the raw-read files do not cover | A live re-capture before the ring rolls around 2026-10-01 |
| Service extras, Dev, bulk import, published workflows, AI agents and columns, sequences, webhooks, notifications, doc images from Cowork, non-English | Unchanged from the first round |

---

## 5. Open decisions as they now stand

**The three A11 decisions**, no default assumed, every tag intact (build plan 11 / 10 / 14, method 0 / 1 /
4), each asked at the moment it first matters and recorded as a `decision` so no later chat re-asks.

| Decision | Where it is today | Where it is asked |
|---|---|---|
| Test account for write probes and scenarios | An existing test workspace in the user's account, as the status quo then (superseded: A11-1 keeps the choice open until the user names a workspace) | Before any write probe or scenario outside it, and confirmed before 1.0.0 |
| Sample data inside a live client account | Nothing written as a default; the blueprint carries the section with the choice unmade | At the blueprint the first time a revision in any strand plans sample rows, and again as a stop in the build door; once per client, possibly during a later strand |
| Transcript redaction and retention, now covering documents | `unanswered` in `CLIENT.md`; only fictional fixtures exist; the calibration's own practice recorded as a candidate and not adopted | Before the first real client transcript or document is written to disk, as one three-part question, never at setup; the record close refuses to prepare the archive while it stands |

**Four calibration questions with a default that ships** (`[L14]` to `[L18]` in the plan): whether a
blocking fork may refuse the freeze (default: the freeze proceeds with the fork listed); where consumption
sits relative to the bleed frame (default: its own section, cross-linked); whether the demo environment is
a modelled asset (default: no); what credential substitutes for the banned client-count claim in a
partner-led seat (the user's; the slot ships empty).

**Decisions this round took for the user, worth their nod**, each recorded where it lives: a sibling's held
lease does not stop a run-sheet (12.4 A14); the intake script is split in two and the hook has a script,
so 111 files and ten scripts (§2, §6 row 17); the gotcha budget at 460 and the script budgets in 5.4; the
lease's chat label minted by the take rather than named by the user; the call review typed as carrying no
client evidence when no client was present.

**Two naming items left for the user.** The method's §0 credits a published author of a public sales method
by name; a strict reading of A12 would remove it, and three passes have left it as the user's call. The
GitHub owner handle appears in the spec, the architecture and the plan as an environment fact from A8; a
variable would remove it everywhere but there.

**Also left as written**: four spellings of hand-off across the documents, "engagement" used both for the
front door and for a piece of work, the method's "history" beside the architecture's "snapshot" for the
same file kind, one real product name inside a fictional fixture row, and the amendments file's own paths
to the rules files. None misleads a builder; each is cosmetic or the user's file.

---

## 6. What the checks found, and what was done

| Check | Found | Done |
|---|---|---|
| Coverage (C1 to C125, A15) | 120 landed, 3 partial, 2 deferred by design, 0 missing, 0 contradictions | The three partials closed: the two C6 clauses (trailing backchannel out of talk share; a split number re-joined at the lower confidence), C26's parallel threads graded per thread, and C80's detector given a home in the delivery measures with the summariser judging it |
| Consistency | 9 must-fix, 33 notes | All 9 fixed: A16 in the architecture and the plan; the A1 leftovers in 3.7 and 9.1 and in WP9 and §6; the lease-versus-demo-script contradiction decided; the A11 timing stated once; one label list with routes for the pricing call and the call review; `strand kind` catalogued; the audit scratch path; the second writers of `dependencies.md` and `open-questions.md` named. Eighteen of the notes fixed while the sections were open; the rest are the naming items above |
| Buildability | ready = false; 14 must-fix | All 14 addressed: WP18; the intake report and `status --json` pinned; S0-15 widened with a fallback per path, the store's writers and `MMB_HOME`; WP2's fixtures; WP3's sources; WP5's acceptance rewritten and the script split; chat identity, the carry rule and the three-part fence; the correction loop built end to end; `hooks/guard.py`; the parked-strand hole closed with the interim constraint and `live-map set`; `advisory`, the unresolvable input and the `[X]` assertions; A16 resolved; the voice bank's regeneration path; the catalogue fixes including the hashed name list |
| Leak lint, round 3 | 2 hits in 2 files, both an ordinary noun lifted from a participant | Both fixed by the lint pass; nothing written this round names an organisation, person, product, brand, figure or date from a call, and tool references stay category words |

Forty-six distinct fixes, counting each must-fix once where two checks raised it.

---

## 7. Readiness

**Building can start.** The five documents agree with each other and with the amendments through A16;
every installed file has one owning package with an acceptance check a builder can run; every interface
between packages is a pinned schema rather than prose; the work has a dependency order that begins with the
stage-0 probes, the shared facts and the calibration fixtures; and each new mechanism this round introduced
— the strand model, the contended lease, the router, the store, the boundary, the document flow, the
correction loop — has a test that fails.

**What would block it, and when:**

- Nothing blocks writing the plugin. The open decisions block specific later moments, not the build.
- **The first week is WP18.** The calibration fixtures are the specification of half the intake behaviour
  and are written to the lessons' parameters with no real-call content; until they are reviewed, WP5 cannot
  be accepted, and a builder who writes them to fit the code has encoded the code's behaviour as the answer
  key. That is the one place the plan asks for judgement before mechanism.
- **Nine boards** of the 67-board fixture must be re-captured live before the ring rolls around
  2026-10-01, or WP3's classification test loses part of its evidence.
- **Stage-0 probes** still decide what the README may claim: S0-12 (hooks in Cowork), S0-14 (raw GraphQL
  text in `tool_input`) and S0-15 (the `MMB_HOME` root, path by path). None changes safety; each changes a
  fallback.
- **The first client build** stops until the sample-data question is answered, by design; **the first real
  transcript or document** is not saved until retention is answered; **sandbox runs outside the current
  workspace** wait on the test-account answer; release check 10 re-reads all three before 1.0.0.
- **Three manual steps sit with the user** and have no API path: U-01 (switch the test automation off in
  the UI and record whether its creator could), U-02 (stop the leftover test forms), V-01 (the dashboard
  widget check by eye).

**One honest caveat.** The architecture's script catalogue and skill responsibilities are dense single
paragraphs. Every rule is there and every reference resolves, but a builder reading 5.4 or 3.2 for the
first time should read the plan's acceptance for that package beside it; the plan is where the rules are
turned into things that pass or fail.

---

## 8. Final check

A final verification (`revision-2-final-verify.md`, 2026-09-12) read the five documents after the fix pass against A1 to A16. It found every A16 bullet implemented, A15's one-call default holding everywhere, every re-added count reproducing, A12 holding, and the 46 fixes applied with the old text gone. Three items were must-fix, all small, plus two partials and two notes that fold into them; each is closed below.

- **M1, a document-only record had no grading scope and no hand-back.** 3.3 and 8.4 keyed the criteria on a type header a document snapshot does not carry, and 8.3 step 7 routed by a label a document does not have. Now 3.3, 8.4 and method 2.6 say it in one sentence each: a document carries no type header, its absence demotes nothing, a document-only record is graded under the document rules alone with every criterion against its plain definition and nothing `advisory`, the doors still read the strand's `kind` and `output_class`, and beside a call the call's header scopes the criteria. 8.3's document paragraph now walks the seven steps: 2 and 3 apply as written; steps 1, 4, 5, 6 and 7 differ, including that neither the pipeline nor `type` runs, no `meetings.md` line is added and a `document` log entry stands in for the `call` entry (the note N10), and that after a document-only intake the front door chains `discovery-check` as it does after a discovery call. 3.2, 12.4, the spec's lifecycle and success table, method scenario 23, WP8's `transcripts.md`, `call-types.md` and `rubric.md` acceptance, s25's key and H56 carry the same rule.
- **M2, `transcript_prep.py document` read a raw file inside the half that never reads one.** Moved to `transcript_measure.py`, the file-level half, which is the side the split's own reason puts it on: A§2, both 5.4 rows, 8.3 step 1 and the document paragraph, 12.4 A16, WP5's reason paragraph and `document` bullet, H56 and §6 rows 16 and 17. The document report now carries the extracted text by anchor, so `verify-quotes` checks a `[Q/doc]` extract from the report alone and WP5's reports-only test holds for every `transcript_prep.py` subcommand. Budgets moved with it, total unchanged: `transcript_measure.py` 600 and `transcript_prep.py` 360 (tests 500 and 280) in 5.4, WP5 and §6 row 17 — a size resolution, worth the user's nod like the others in §5.
- **M3, the client's own SOP had no path to a drafter with no file access, and copying its structure failed the copied-run lint.** 3.6 and the `sop_tools.py` row name the path: the skill proposes which document in `inputs/` is the client's SOP from the snapshots' status fields, the user confirms, and `sop_tools.py inputs --from-document <stem>` appends that document's own text and its section headings from the snapshot's section map — never the snapshot's marks, conflicts or markers. 9.6 exempts a run that matches a client document in `inputs/` and the document snapshot's client-safe block (the note N9) from the copied-run rule, since what the client wrote cannot leak to them, and keeps the rest of the snapshot inside it. WP4, WP6 and WP12 test it, and WP12's proved-by row now cites H56 (the note N12).
- **N7, one arrival order tested.** H56 now runs both orders from the same fixture with no new file — documents then the call, and the call then the documents — and asserts the same grades, conflict and `documented` rows; s25's key and the 4.2 paragraph say so. The row count stays at 52.

No count moved except the two script budgets: 111 installed files, ten scripts, 43 templates, 115 ownership rows, 52 headless rows, 23 sandbox scenarios, the `[A11-n]` tags, and the skill descriptions are as §4 of the verification re-counted them. The remaining notes (N1 to N6, N8, N11, N13 to N18) and the four items left as the user's in §5 above are untouched.
