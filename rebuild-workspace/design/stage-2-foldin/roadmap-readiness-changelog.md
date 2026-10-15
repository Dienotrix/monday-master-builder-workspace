# ROADMAP.md, readiness spec and SPEC.md fold-in of A24 to A28: changelog

Editor: the roadmap and readiness editor of stage 2's first task, 2026-10-14. Source of truth: `AMENDMENTS.md` A24 to A28 with every "Answered 2026-10-14" line. Line ranges are after editing, at the moment each entry was written; later entries above a passage may shift it by a few lines.

Status: complete (see the end of this file).

## Entries

### ROADMAP.md, opening (L3)
- L3, A24 to A28: the revision note names A17 to A23 for 2026-10-13 and says the document was re-cut 2026-10-14 under A24 to A28; "on the Mac" becomes "on the user's machine, Windows or Mac, with identical behaviour on both".

### ROADMAP.md, v1 "Take in whatever arrived" (L10 to L15)
- L15, A27: new bullet: the call type is a best guess with its signals, marked assumed; intake carries on and tells the user, a correction re-runs what depended on it, and it stops only when it cannot tell.

### ROADMAP.md, v1 "Decide what to build" (L17 to L22)
- L18, A27: the readiness bullet opens with goals and pains, lists the nine parts in SPEC's order, and adds that thin input still gets a generic build because a basic demo beats nothing, with the plugin asking before the card only what it cannot infer.
- L19, A24, A26: the walkthrough creates the home tree itself (`monday-builder` under the home on either system), asks the firm name, the default account, optionally the never-shown workspaces, and one optional local-or-GitHub archive question; it checks Python and the connector on the running system, and the GitHub tool only when GitHub is picked. `gh` as a default check is gone.
- L20, A26: "the archive account" leaves the default settings list; a GitHub account is stored only when the user chose the GitHub archive.

### ROADMAP.md, v1 "Design the structure" (L24 to L29)
- L27, A25: "forks left open rather than guessed" becomes: a fork or open structural question is built on its leaning with the user's yes, marked assumed, the card saying what a later switch would and would not keep, the user's blocking flag stopping that part.
- L28, A25: new bullet for the narrowed read-back: the automation conditions and a general overview of the board architecture are listed as assumed on the card when the client cannot be reached, and checked at the next contact; column names and status labels are shown, not confirmed separately; the user is always the one who confirms.
- L29, A28: the approval card opens with what the build rests on; one yes covers the whole revision on an own-account proof of concept, lists and irreversible steps included; a yes per list and the execution-time confirmation stay for a client's account and for lists that notify real people.

### ROADMAP.md, v1 "Build it in the user's own account" (L31 to L45)
- L34, A28: new bullet on sample rows for realism over the hour: dozens per board where dashboards and roll-ups need numbers, a handful elsewhere, plausible invented values minus the exclusion list, every value marked sample.
- L35 to L36, A28: workflow publication and agent activation are their own yes in a client's account and within the card's yes on an own-account proof of concept; the read-back and deactivation-until-verified rules are unchanged.
- L41, A25: the build notes gain a short paragraph per open item: what was assumed, why, what the client needs to clarify.
- L42, A27, A28: round two is an order of work, not a wait; with the usual one to three days it is built and audited before the first showing; separate yeses for activation and publication hold in a client's account only.
- L43, A27: new bullet: the first hour is the floor, the usual case is one to three days, and the plugin proposes the cadence while the user sets it.
- L44, A25: new bullet: versions carry their purpose, proof of concept (`v0.x`) until sign-off and working solution from `v1.0`; recording `signed-off` warns and does not block.
- L45, A24, A26: close-out defaults to a local copy-and-compare and a move into `archive/` under the home, the user deleting by hand on either system, no Trash or Recycle Bin; the private repository and clone-and-verify stay for the GitHub option only.

### ROADMAP.md, v1 "On either system" (L47 to L48)
- L47 to L48, A24: new group with one bullet: identical behaviour on Windows and Mac, Python 3.9+ standard-library scripts and hooks, home-directory paths with no fixed separator, either line ending, Python release tooling, and release checks (unit tests and the six end-to-end tests) on both systems, the GitHub archive too where set up.

### ROADMAP.md, v1 "Safety throughout" (L50 to L51)
- L51, A25: the safety bullet adds that assumptions stay visible in the record, on the card and in the build notes, never as text in the client's workspace, never turned into fact.

### ROADMAP.md, v2 or v3 (L60 to L61)
- L61, A25 (answered 2026-10-14) and the user's direction of the same day: the SOP line adds the master document the plugin generates for the client, the solution and why, with diagrams, how to use it and the SOPs, seeded by the build notes; nothing of it is v1.

### ROADMAP.md, build stages (L66 to L81)
- L66: the heading reads "re-cut 2026-10-13, updated 2026-10-14".
- L70, A24: stage 0 is complete for v1 on macOS; the Windows re-run with its short list (hook launch, plugin root spelling, GitHub tool presence where the GitHub archive is chosen) belongs to WP-S0 and waits until before the first release.
- L72, stale state: stage 1b reads "complete 2026-10-13, with its consistency check and fix".
- L73, stale state: the fixture fix pass reads "complete 2026-10-13".
- L74, A24, A27, stale state: stage 2 is current; its first task is the fold-in of A24 to A28, then the goals pass on the 25 keys and the record-map pin, then WP2 in Python 3.9 or later.
- L78, A24, A27: stage 5's release tooling is Python, the release checks run on Windows and macOS, and the end-to-end proof of concept is where the first-hour floor is measured and recorded with its figure.
- L79, A25: the v2 / v3 row names the master document beside the SOP layer.
- L81, A24: "Waiting on the user" adds the user's Windows machine for the stage-0 re-run before the first release.
- Counts: ROADMAP carries no file, template or test count, so none was re-totalled. The six end-to-end tests are the user's named six, unchanged.

### Readiness spec, title and status (L1, L3)
- L1, stale state: the title drops "for the stage 1b re-cut".
- L3, A24 to A28, stale state: the status line says the spec was folded on 2026-10-13 into SPEC and ARCHITECTURE section 3.3 and re-cut 2026-10-14 under A24 to A28; "Status: proposed" is gone.

### Readiness spec, section 1 (L9)
- L9, A27, A25: thin input gets a generic workspace built and shown because a basic demo beats nothing; user-approved assumptions may carry a proof of concept while visibly unconfirmed, and a working solution needs its structural assumptions confirmed or accepted.

### Readiness spec, section 2, the nine parts (L13 to L27)
- L15, A27: part 1 becomes "Goals and pains": the client's stated goals first, in their own words with quote, location and speaker role, then the pains with their wanted outcomes; the unconfirmed signals stay beside them. No part renumbers, so the count stays nine and every part cross-reference ("part 3", "part 9") still holds.
- L17, A25: part 3 says an open structural question does not by itself stop a proof of concept: the build rests on its leaning with the user's yes, marked assumed, the card saying what a later switch would and would not keep; the blocking flag stops that part.
- L19, A25, A27: part 5 widens to the call type when only guessed, the automation conditions and board-architecture overview when the client cannot be reached, and fork leanings; column names and status labels show on the card and are not confirmed one by one; assumptions live in the record, the card and the build notes with a short paragraph per open item, never as text in monday; the user is the one who confirms.
- L22 to L26, A27, stale term: part 8 is now "Clearance", SPEC's word, with a note that the record keeps it in the pinned field `verdict`; `cleared to build, generic` is built and shown with its assumptions rather than held for better inputs.
- L27, A27, A25: part 9's questions are for the user to ask at the next contact, not a stop; before the card the plugin asks only what it cannot infer; a fork's leaning carries the build with the user's yes.

### Readiness spec, section 3 (L32)
- L32, A27: the call-type sentence adds that the type is intake's best guess, marked assumed, and a correction re-runs the check.

### Readiness spec, section 5 (L40 to L44)
- L40, A27: the heading adds "and in the usual one to three days".
- L42, A28: the one approval stop is one yes for the whole revision on an own-account proof of concept, a yes per list in a client's account or where rows notify real people; sample rows follow realism over the hour, every value marked sample.
- L44, A27: new paragraph: the hour is the floor; with the usual one to three days the deep research runs before the first build, sample data is refined, round two is built and audited before the first showing; the plugin proposes the cadence and the user sets it.

### Readiness spec, section 6 (L48)
- L48, A27, stale state: past tense for the completed fix pass (2026-10-13); the keys receive `goals` in a small follow-up pass with the record-map pin; a third grader check (every goal carries its quote at its location) may join. Grader-check count stays two now, three only if the user nods.

### Readiness spec, section 7 (L50 to L52)
- L50, stale state: the heading reads "Shape, pinned in the record map".
- L52, A27, A25: the proposed `goals[]` shape comes first: `id`, `goal` (the client's words), `quote`, `location`, `speaker_role`, `pains[]` (ids of the pains it relates to); `assumptions[]` gains `kind` (gap, call type, automation condition, board architecture or leaning) and `state` (assumed or accepted); the closing sentence says the fix pass pinned the rest in `shared/record-map.md` and `goals[]` with the two new fields are pinned there in the follow-up keys pass. The field `verdict` keeps its pinned name.

### Readiness spec, section 8 (L54 to L60)
- L54: the heading adds 2026-10-14.
- L57, A28: the generic-build bullet adds that on an own-account proof of concept the same yes covers the whole revision.
- L58 to L60, A27, A25: three new bullets: goals and pains open the check; the call type is a best guess; assumptions may carry a proof of concept, open structural questions are built on their leaning, and `signed-off` warns rather than blocks. The first item stays the five-question ceiling, so section 9's "first item" reference holds.

### Readiness spec, section 9 (L66 to L67)
- L66, cross-reference fix: "(part 8, first item)" becomes "(section 8, first item)"; part 8 of the check is the clearance, and the ceiling lives in section 8.
- L67, A27, stale state: the pin was made in the fix pass (past tense), and `goals[]` joins it in the follow-up keys pass.

### SPEC.md, brought in line with the answered lines of 2026-10-14 only
- L3, A24 to A28: the revision note adds that SPEC was re-cut 2026-10-14 under A24 to A28 for that day's answers.
- L12, A26: "There is no GitHub account anywhere in it" becomes: a GitHub account is stored in `local/` only when the user picks the GitHub archive; the default local archive needs none.
- L13, A26: the walkthrough offers two optional questions, the never-shown workspaces and local-or-GitHub archive (local the default); it checks the GitHub tool and stores an account only when GitHub is picked.
- L22, A25: the term read-back narrows to the automation conditions and a general overview of the board architecture, confirmed by the user as solution architect; column names and status labels show on the card, not confirmed separately; when the client cannot be reached they go on the card marked assumed; a fork's card text says what a later switch would and would not "keep" (was "restore"), and the build notes carry a short paragraph on why it is open.
- L23, A25: assumed items stay marked until the user confirms them, passing on what the client said; the plugin never deals with the client.
- L28, A25: sign-off warns, listing every structural assumption not yet confirmed or accepted, and does not block (was "requires").
- L31, A26: close-out keeps the local archive as the default and adds the GitHub archive with a private repository and clone-and-verify for a user who picked it.
- L39, A25: the blueprint step lists the assumed automation conditions, board overview and fork leanings, each fork with what a switch would and would not keep.
- L45, A25: `signed-off` warns and does not block (was "requires").
- L46, A26: the record close adds the GitHub path for a user who picked it.
- L58, A26: in-scope line adds "or a GitHub archive where the user chose it".
- L83, A25: `signed-off` "is refused" becomes "warns ... without blocking".
- L86, A26: record hygiene names the GitHub archive with a verified clone as the option beside the default local copy.
- L104 to L106, A26: the Record criterion's "sends nothing to any repository" applies to the default local path; Platform tests the local archive on both systems and the GitHub archive on both wherever set up; Daily use has no GitHub step unless the user picks it.
- L108, A25: the Assumptions criterion lists unconfirmed structural assumptions as a warning at `signed-off` (was "refused").
- L116, L118, L122, A25: the worked day follows the narrowed read-back: the assumed item is the won-pursuit automation condition beside the board overview, the fee stage names only show on the card, and on Thursday the user passes on the client's confirmation and the stage-name correction. Nothing else in SPEC was touched.

## Worth the user's nod

- **The `goals[]` shape (readiness spec section 7).** Proposed as `id`, `goal` (the client's words), `quote`, `location`, `speaker_role`, and `pains[]` (the ids of the pains the goal relates to). The link runs from goal to pains only; pains gain no goal field. It is pinned in `shared/record-map.md` in the follow-up keys pass, not in this run.
- **Two new `assumptions[]` fields (readiness spec section 7).** `kind` (gap, call type, automation condition, board architecture or leaning) so the card and the sign-off warning can tell structural assumptions apart, and `state` (assumed or accepted), with a confirmed assumption becoming evidence and leaving the list. Including the call type as a kind follows from A27's "everything else is assumed, labelled and shown on the card"; the map called the kind field optional. Pinned in the same follow-up pass if nodded.
- **"Clearance" in the readiness spec, field still `verdict`.** Part 8 now uses SPEC's word, "clearance"; the record map pins the field as `verdict` with `cleared_for`, so the field name was left as pinned rather than renamed.
- **A third grader check may join (readiness spec section 6):** every goal carries its verbatim quote at its location. Left as "may join"; the grader count stays two until the user says yes.
- **SPEC's worked day.** The fee stage names stopped being an assumed term under the narrowed read-back, so the example's assumed item became the won-pursuit automation condition beside the board overview. This is an illustrative choice, not a rule.
- **GitHub close-out wording.** SPEC and ROADMAP describe the GitHub path as a private repository with a clone-and-verify close-out, the wording of the original A26 consequence that the answered line keeps "for that path only".
- **ROADMAP grouping.** The A24 platform rules sit in a new v1 group, "On either system", rather than inside "Safety throughout"; the stage-0 Windows re-run is named as part of WP-S0, as directed, not a new row.

Status: complete. Files edited: `ROADMAP.md` (81 lines), `stage-1b/build-readiness-spec.md` (67 lines), `SPEC.md` (148 lines, line count unchanged). No file, template or test count in the three files changed; the nine readiness parts, the 25 answer keys, the two grader checks and the six end-to-end tests stand as they were. No part renumbered, and the one part-number cross-reference that was wrong ("part 8, first item") now reads "section 8, first item". The three A11 decisions stay open; no AI credit is priced.
