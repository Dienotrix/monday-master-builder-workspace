# Reviewing the calibration fixtures s11–s25

Fix pass applied 2026-10-13. Each folder now carries CHANGES.md, the editor's log of what changed and why, and the key carries a readiness block, the v1 half the plugin is graded on; the sales fields stay for v2.

These fifteen fixtures are the specification the intake code will be graded against. Each folder holds a `README.md` (what it proves, its counts, the planted defects and where they are), the input files (a transcript in some export format; s24 is a package of five; s25 is a Word file, a PDF, a flowchart image and a short call), and `answer-key.json` (what the plugin must conclude — the 25 fields the reviewed fixtures s1–s10 use, plus an `intake` block asserting the repair).

Every fixture was written from generic parameters, then adversarially reviewed: every cited quote verified at its location (2,074 in all), every planted defect confirmed, counts re-checked, no real-client content. All fifteen came back "ready for user review".

**What to do per fixture (10 minutes each is plenty):**
1. Read the README's first section: does the scenario make sense as something the plugin will meet?
2. Skim the transcript: does it read like a real call, mess included? Anything that reads like a real client you know? (There should be none.)
3. Open `answer-key.json` and spot-check three things: the pains it lists, what it says is buildable, and one planted defect's repair in the `intake` block. Is that what you would want the plugin to conclude?
4. Reply with the fixture id and either "keep", or "wrong / missing / unclear" plus the line or quote and the reason.

Three things to know: the type-header fields carry short machine tokens (for example `new-logo`, `small-group`) with the authors' prose kept in a `_note` field beside each; a two-attendee call is currently typed `small-group`, which the build will settle; and the reviewers flagged a few real place names used as invented ones (the s1–s10 practice) — say if you want them changed.

| Fixture | What it proves |
|---|---|
| s11-demo-composite | a demo transcript with one long block that hides several speakers; nothing in it is attributed to the labelled name |
| s12-header-present | a big export roster that lies (bots, silent listed people, unlisted speakers, wrong org sections) |
| s13-header-absent | no roster at all; the attendees are narrated aloud across two turns |
| s14-shred-block | sentences shredded across turns and speakers; a headline figure split three ways |
| s15-shred-dense | a third of turns under five words, four label shapes in one file, no ellipses |
| s16-shred-cue | a cue-timed export with one speaker's words wedged inside another's; quotes never cross a speaker |
| s17-no-markers | zero artifact markers plus heavy shred: intake raises doubt instead of trusting the clean look |
| s18-identity-collapse | one person under a dozen surface forms; no person invented |
| s19-reverse-demo | the client shares their screen; the structure inventory with spoken / observed marks |
| s20-large-group | double-digit attendance, silent decision-makers, a cross-speaker conflict kept as both statements |
| s21-existing-account | an existing client with a lapsed rollout and an internal prototype; expansion mode |
| s22-degrading-commitment | two calls where our side re-quotes a client figure second-hand; the re-quote is not evidence |
| s23-symmetric-shred | balanced shredding that hides per-speaker error behind a healthy aggregate |
| s24-package | five handed-over calls in a new export grammar, out of order, with a re-quoted figure and a cross-call conflict |
| s25-client-documents | a client SOP (Word), a flowchart (image), a requirements write-up (PDF) and a short call that contradicts the SOP |
