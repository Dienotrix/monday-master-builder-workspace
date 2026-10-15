# SPEC edits from the review interview of 2026-10-13

One line per edit to `rebuild-workspace/design/SPEC.md`, applied in one pass from `for-review/SPEC-REVIEW-2026-10-13.md` and amendments A21 to A28. Every "Keep. No edit." round was left alone. Edits 51 to 54 came from the closing re-read, which looks for sentences the pass had put in contradiction with each other.

1. Header: re-cut under A1 to A28 and reviewed with the user by interview the same day; the manifest sentence kept. Interview outcome.
2. Who it is for, One surface: Claude Code on Windows or Mac with identical behaviour, every operation OS-independent or with a tested per-system implementation, the archive running wherever the user is; Mac-only phrasing and the `gh` mention removed. Round 1, A24; A26.
3. Who it is for, home folder: generic default under the home directory on either system, created by the plugin; `archive/` added as the holding folder; the settings lose the GitHub account; the never-shown workspaces become optional. Round 1 restart, A26; A24.
4. Who it is for, walkthrough: two questions and one offer, creates the tree, checks Python and the connector on the system it runs on, keeps the `CLAUDE.md` warning; asks for no GitHub account and checks for no GitHub tool. Round 1 restart, A26; A24.
5. Who it is for, sessions: the nudge is a suggestion and the user decides. Round 1 restart, kept as decided, one clarifying clause.
6. What it does, intake: call type a best guess, recorded as assumed with its signals, intake continues and tells the user, stops only when it cannot tell. Round 2, A27.
7. What it does, readiness: nine parts opening with goals and pains; thin input never blocks because a basic demo beats nothing; user-approved assumptions may carry a proof of concept while visibly unconfirmed. Round 2, A27; A25.
8. What it does, blueprint: unconfirmable client terms go on the card as assumed terms and are read back at the next contact; a fork or structural question is built on its leaning with the user's yes and marked assumed, the card saying what a switch would and would not restore; the blocking flag stays the one stop. A25.
9. What it does, approval card: opens with assumptions, assumed terms and fork leanings; one yes for the whole revision on an own-account proof of concept, lists and irreversible steps included; per-list yes and execution-time confirmation kept for client accounts and anything notifying real people. Rounds 3 and 6, A28; A25.
10. What it does, build: sample rows go for realism over the hour, dozens where dashboards and roll-ups need numbers, plausible invented names and figures allowed minus the exclusion list, every value marked as sample. Round 3, A28.
11. What it does, audit and build notes: the presentation checklist lists the views the API cannot create with their board and settings, for the user to add when they choose. Round 9, A23.
12. What it does, round two: the two rounds are an order of work, not a wait; with the usual preparation time round two is built and audited before the first showing. Round 8, A27.
13. What it does, iterate or fresh: the plugin proposes with its reason and the user confirms, never fresh on its own; new bullet "Versions carry their purpose", with sign-off requiring the structural assumptions confirmed or explicitly accepted. Round 4, A21; A25.
14. What it does, research: the deep dive runs before the first build when the usual one to three days exist, after round one when they do not. Round 8, A27.
15. What it does, close-out: the record close archives locally into `archive/` under the home, the holding folder, with deletion by hand on either system; no repository, clone or Trash. Round 1 restart, A26; A24.
16. Lifecycle step 2: call type proposed as a best guess and recorded as assumed with its signals. Round 2, A27.
17. Lifecycle step 3: readiness opens with goals and pains; thin input is `cleared to build, generic` with the assumptions listed; `not yet` unchanged. Round 2, A27; A25.
18. Lifecycle step 5: the blueprint carries the assumed terms and fork leanings with what a later switch would and would not restore. A25.
19. Lifecycle step 6: one yes on an own-account proof of concept; per-list yes in a client's account and for real-people notifications. Round 3, A28.
20. Lifecycle step 7: execution-time confirmation and per-list confirmation only in a client's account; sample rows per the realism rule. Rounds 3 and 6, A28.
21. Lifecycle step 9: the deep dive before the first build when time exists; round two before the first showing when time allows; publication and activation yeses own only in a client's account. Round 8, A27; A28.
22. Lifecycle step 10: the plugin proposes iterate or fresh with its reason, the user confirms. Round 4, A21.
23. Lifecycle step 11: versions carry their purpose; `signed-off` requires every structural assumption confirmed or explicitly accepted, recorded in the record. A25.
24. Lifecycle step 12: local archive as a verified copy-and-compare, the folder moved into `archive/` on the user's confirmation, deletion by hand on either system; no repository, clone, Trash or Recycle Bin. Round 1, A24; A26.
25. Lifecycle, first-hour paragraph split in two: the hour is the floor, measured and recorded with no ceiling, realism winning when it takes longer; the usual case is one to three days with deep research before the first build and round two before the first showing, the plugin proposing the cadence and the user deciding. Rounds 3, 7 and 8, A27; A28.
26. v1 scope, in scope: the record close with its local archive. A26.
27. v1 scope, out of scope: no `delete_*` call in any account, the user's own included; deletion by hand. Round 5.
28. Safety, approval stops: each list approved as a whole, with its own yes in a client's account or where rows notify real people, within the card's one yes on an own-account proof of concept. Round 3, A28.
29. Safety, irreversible steps: execution-time confirmation only in a client's account; "removing a dashboard" dropped from the list because the plugin now deletes nothing anywhere; the no-delete rule stated. Round 6, A28; round 5.
30. Safety, new bullet "Assumptions stay visible": in the record, on the card and in the build notes, never inside the client's workspace, never turned into facts; sign-off refused while a structural assumption is unconfirmed. A25; A28.
31. Safety, record hygiene: the archive and cleanup line, local, on either system, deletion by hand. A26; A24.
32. Safety, never-demo: "when named in local settings", since the question is now optional. A26.
33. Success criteria, Record row: a record close leaves a verified copy in `archive/` and sends nothing to any repository. Round 1 restart, A26.
34. Success criteria, Platform row: install, intake, build, interruption recovery, audit and archive proven on both Windows and macOS. A24.
35. Success criteria, Daily use row: a working home on either system with no GitHub step. A24; A26.
36. Success criteria, First hour row: the floor, measured and recorded, no ceiling; new Assumptions row. Round 7; A25.
37. Worked day, 9:10: the call type stated as a best guess that the user lets stand. Round 2, A27.
38. Worked day, 9:25: goals and pains first in the readiness output. Round 2, A27.
39. Worked day, 9:25: the fee stage names go on the card as assumed terms to read back at the next contact. A25.
40. Worked day, 9:40: the card opens with the assumptions and the assumed terms. A25.
41. Worked day, 9:40: one yes covers the whole card, the two workspaces and the automations list included. Round 3, A28.
42. Worked day, 9:50: the workspaces created without a second ask; about 60 plausible sample rows marked as sample; the automations created under the same yes. Rounds 3 and 6, A28.
43. Worked day, 9:50: `cleared to show` at 10:20, the build notes' checklist naming the Kanban and Gantt views to add by hand with their board and settings. Round 9, A23; A28.
44. Worked day, Thursday: the stage names corrected when read back as assumed terms. A25.
45. Worked day, Thursday: one yes for revision 2, the agent's activation included. Round 6, A28.
46. Worked day, Thursday: the agent activated last under the card's yes instead of a separate ask. Round 6, A28.
47. Worked day, new closing paragraph: the day is the floor; with the usual one to three days the deep research and round two come before the showing. Round 8, A27.
48. Live testing, views: the enum re-checked on the live schema on 2026-10-13, four creatable kinds, the hand-made views on the checklist, a probe noted for the app kind with a built-in view's feature id. Rounds 8 and 9, A23.
49. Live testing, Vibe apps: the delete finding kept as a finding, with v1 sending no delete call, so removal is a by-hand close-out step. Round 5.
50. Open decisions, A11-1: the test workspace is named when the first live probe asks. Round 9.
51. Re-read fix, What it does, research: "when time allows" restored for the quick brief to match lifecycle step 4.
52. Re-read fix, What it does, build: sample data "invented ... as the call and the brief describe it", so the sentence no longer says both invented and drawn from. A28.
53. Re-read fix, Lifecycle, first-hour paragraph: one sentence re-punctuated.
54. Re-read fix, Live testing, workflows: the activate-or-not choice is its own yes in a client's account and within the card's yes on an own-account proof of concept, matching the approval rule. A28.
