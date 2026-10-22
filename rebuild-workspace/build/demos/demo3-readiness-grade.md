# Demo 3: readiness graded against the s6 key

Graded: the readiness check for the sales pipeline strand and the call summary it was built from, against the `readiness` block of the s6 answer key. The key has no separate intake block; its call type and attendee list were used for the call-type check. Sales-grading fields were ignored.

## 1. Result

- Clearance: cleared to build, the same as the key (cleared for build). Match.
- Counts, found / partly / missed / extra. Goals: 4 / 0 / 0 / 4. Pains (21 in the key): 11 / 4 / 6 / 3. Entities (30 in the key): 9 / 16 / 5 / 0.
- Call type: discovery, every header field marked proposed; the key says discovery. Match. The three client speakers and their roles are right (the sales leader is correctly read as the approver who holds the budget).

## 2. Goals, pains, entities

### Goals

| Key goal | Result | Readiness line |
|---|---|---|
| One screen on Monday: out there, stuck, closed | found | G1 |
| January forecast within ten percent | found | G2 |
| Know who has been in front of a customer without asking | found | G3 |
| Four new reps productive without the manager travelling | found | G4 |

Extras: G5 (the summary builds itself) is extra, sound; it is the analyst's stated outcome in the key's pain list. G6 (one record per company) is extra, sound. G7 (margin seen only by those entitled) is extra, sound; the key carries it as an unmet need. G8 (the agreed five-item scope) is extra, sound, though it is a scope statement more than a goal.

### Pains

| Key pain | Result | Readiness line |
|---|---|---|
| P1.1 cannot say what will close | found | P2.1 |
| P1.2 the forecast is a guess | found | P2.2 (adding up hopes) |
| P1.3 retyping the workbook | found | P3.1, P3.2 |
| P1.4 the manager's pipeline is a legal pad | missed | none |
| P1.5 the workbook is stale within days | missed | none |
| P1.6 the legal pad will not survive four more reps | missed | none; G4 carries the wish but no pain |
| P2.1 stocking quote idle five weeks | found | P1.1 |
| P2.2 thirty-eight percent of quotes with no activity | found | P1.2 |
| P2.3 no follow-up step exists | found | P1.3 |
| P2.4 the ERP shows open quotes but prompts nobody | missed | none; the ERP expiry point appears only as an entity note |
| P3.1 a leaver took the account history | found | P4.1 |
| P3.2 duplicate call on one customer, and a price given away | found | P4.2 (the price giveaway is dropped) |
| P3.3 no buyer preferences survive a handover | found | P4.3 |
| P3.4 reps cannot be made to write things down | missed | none; P7 (adoption) is adjacent but a different pain |
| P4.1 visit coverage planned from memory | found | P5.2 |
| P4.2 the earlier call-report emails died | missed | none |
| P4.3 cannot tell the president whether anyone visited a region | found | P5.3 |
| P5 house accounts unworked | partly | signal only, and an unmet need; no pain line |
| P6 no win-loss on city bids | partly | unmet needs only |
| P7 the bid calendar is a loose spreadsheet | partly | unmet needs only |
| P8 nothing to hand four new reps | partly | G4 and an unmet need; no pain line |

Extras: P5.1 (managers cannot see their reps' pipeline without calling) is extra, sound. P6 (new companies live wherever the rep puts them) is extra, sound. P7 (reps will not log if it is slow or one more thing) is extra, sound; the key treats it as a blocker and a leaning.

### Entities

| Key entity | Result | Readiness line |
|---|---|---|
| prospect | found | prospect |
| intake route | partly | only in the build elements (website form, trade-show lists) |
| account | found | account (shared resource marked false; the key says true) |
| contact | found | contact (goes stale marked true; the key says false) |
| house account | partly | a signal, not an entity |
| account owner | partly | folded into "rep and region" and the account's independence note |
| opportunity / quote | found | opportunity (goes stale true; the key says false) |
| ERP quote document | found | business-system quote number, with the requote clock |
| pipeline stage | partly | an assumption, not an entity |
| follow-up step | partly | a column in the P1 element, not an entity |
| stocking agreement | partly | a note under opportunity, plus an assumption |
| margin on a deal | partly | goal and unmet need, not an entity |
| activity (call or visit) | found | call or visit |
| ride-along | missed | none |
| outside rep | found | rep and region |
| inside sales | partly | signal and assumption only |
| region / territory | found | rep and region (merged with rep) |
| branch | missed | none |
| pipeline workbook | partly | in Existing, not Entities |
| a rep's tab | missed | none |
| forecast | found | forecast (view, never typed) |
| manager's legal pad | missed | none |
| old CRM account list | partly | in Existing |
| abandoned Prospects board | partly | in Existing, described but not decided |
| contract pricing matrix | partly | under the ERP's authority in Existing |
| city bid | partly | unmet needs |
| bid calendar | partly | unmet needs |
| line card | partly | unmet needs (the view of lines each customer buys) |
| outsourced IT provider | partly | named in assumptions and unmet needs |
| the IT engineer who blesses ERP changes | missed | none |

Extras: none. Every readiness entity maps to a key entity. The independence notes are good and cite the call; the differences are in the flags noted above.

## 3. Product and structure

The readiness check picks CRM only, as the key does, with the native boards: Leads, Accounts, Contacts, Opportunities, Sales Activities. It names no Work Management, Service or Dev entity, which matches the key. Build target is own-account, with the reason that the call offered "your own account"; this matches the key and notes the tension the key flags. The forecast and coverage dashboard matches the key's forecast view. It also correctly keeps the quote document and pricing in the business system and leaves out Quotes & Invoices, which the key treats as optional.

Differences against the key:

- The key relabels native boards to the client's words (Leads as Prospects, Deals as Opportunities) and treats this as the point of the vocabulary trap. The readiness check uses the native names and never proposes relabelling. This is a miss, not an error: it builds no look-alike boards.
- The key says the native boards are found by detection, recorded, or installed from the native template set if the workspace is bare. The readiness check does not say this. Its verdict condition ("the CRM workspace is not yet in the record, no account bound") reads as if the build were waiting on a client account, which the key says it is not.
- The key's leaning for requotes is the opportunity as parent with each quote document as a child row and a roll-up. The readiness leaning keeps one opportunity with earlier numbers in its updates. The key's own condition (how often requotes happen) allows the simpler form, so this is a defensible difference. The readiness roll-up pattern covers accounts only.
- The automation that creates and assigns a lead from a new website enquiry is not in the key and rests on no stated client wish. The key's version is a native form on Leads plus an import for trade-show lists; the readiness check has no import.
- The key adds a stalled flag derived from days since last activity, and an "ERP status as of" date for the hand-keyed number. The readiness check has the flag as an automation but no as-of date.
- Nothing is built that the key forbids: no Prospects or Quotes look-alike board, no ERP write-back, no Work Management modelling.

## 4. Assumptions and questions

### Key assumptions against the readiness check's

| Key assumption (kind) | Result | Readiness match |
|---|---|---|
| Stages are the five played back (leaning) | found, kind differs (gap) | the stages assumption and its question |
| Stalled after a fixed number of days (automation-condition) | found, number differs | seven days, manager at fourteen; the key's provisional figure is fourteen |
| Prompts go to the rep, then the manager | found | same item |
| ERP number keyed by hand, no connection (leaning) | found, kind differs (gap) | the hand-typed quote number; no as-of date; its question asks acceptability, not the ERP version or API |
| Quote document is fields, no per-document record | partly | the requote leaning (same deal, new number); the question about a per-document record is not asked in those words |
| Territory is a field and view, not a workspace (board-architecture) | found, kind differs (gap) | region as a column |
| Inside sales use the same boards, do not own deals | found | same item and a matching question |
| Prospects arrive through a form and an import | partly | the website enquiry automation; no trade-show import |
| Nothing imported from the old CRM | missed | listed as an unmet need "not probed"; no assumption or question |
| The abandoned Prospects board is neither seed nor base | missed | described in Existing; its fate and the client's "don't leave two" are not carried |
| Stocking agreement is a deal type with a term end date | found, partly | a type on the opportunity; no term end date; the question asks about a term or review date |
| Margin visibility is a permission design on sample data | partly | an unmet need and a question, not an assumption |
| Sample rows are invented, no real names | missed | none |
| The president's forecast test needs confirming with him | partly | a forecast formula assumption; confirming with the president is not raised |
| First version in the user's own account despite the offer made | partly | stated in the build-target line, not as an assumption |

Totals: 7 found, 5 partly, 3 missed. The readiness check often labels as "gap" what the key calls a leaning or a board-architecture choice. Its extra assumptions are sound: the client's name, the call-type read, the five-board build, the lead-to-account conversion leaning, and the region-by-location question. The enquiry-assignment automation is extra and thinly supported.

### Key questions against the readiness check's

| Key question | Result | Readiness question |
|---|---|---|
| Requote: second row or replacement, how often | found | question 3 (same deal or new; frequency not asked) |
| Stages in your words, what is stalled, after how many days, who is told | found | questions 1 and 5 together |
| Who owns an account two reps touch, who inherits a leaver's accounts | missed | none |
| What inside sales would type, and whether they own deals | found | question 4 |
| Is a hand-keyed ERP number acceptable, and who keys it | partly | asked in the assumptions list but not in the five questions, and without "who keys it" |

Extra: question 2 (must reps not see other reps' deals at all, or only margin and pricing) is extra, sound. Its role and context are right.

## 5. Quotes

Five checked against the transcript, whose timestamps are minutes and seconds.

1. "I open one screen on Monday morning and I know what's out there, what's stuck, and what closed." at 28:26, the sales leader. Exact.
2. "We had a sixty-two thousand dollar stocking quote sitting at the named customer for five weeks and nobody touched it." at 11:34, the sales leader. Exact (the customer name is replaced here; the readiness text keeps it).
3. "Owner, their manager, Delia, me, Gene. Not other reps. Ever." at 39:01, the sales leader. Exact, with the first names left in the quoted text.
4. "Longer if it sounds like it writes anything back into P twenty-one." at 30:27, sales operations. Exact.
5. "Somebody was supposed to call them. That's it." used in question 1. The wording is exact, but the question's "known" line cites 13:05, which is a different statement by the regional manager; the sales leader's line is at 12:01. Near: right words, location not given for that quote.

Also seen exact: the Prospects-board line at 31:19, the no-follow-up line at 13:05, and the same-company line at 38:47. No drifted or wrong quote was found. The quoted excerpts are cut mid-sentence without an ellipsis in a few places; none changes meaning.

## 6. What the skills should change

1. Pains (misses P1.4, P1.5, P1.6, P2.4, P3.4, P4.2): the summary's pain list takes only the headline statement of each theme. It should also take the workaround-as-pain lines (the legal pad, the stale workbook, the ERP that prompts nobody, "write things down", the abandoned call reports) and the "will not survive the launch" lines. The readiness skill should not drop a pain only because another pain in the same theme is already listed.
2. Deferred pains (P5, P6, P7, P8 listed only as signals or unmet needs): the summary and readiness should list pains the client defers as pains, marked deferred, so they get a pain line and an outcome rather than only an unmet-need row.
3. Entities (10 partly, 5 missed): the summary lists eight entities; the key finds about thirty. Add the children and neighbours that the call names: intake route, house account, account owner, pipeline stage, follow-up step, stocking agreement, margin, inside sales, ride-along, branch, and the artefacts (workbook tabs, legal pad). Apply the independence and stale tests per entity rather than defaulting (account shared resource, opportunity and contact stale flags differ from the key).
4. Structure (vocabulary and preflight): state that native boards are relabelled to the client's words where it helps, and that preflight detects the native set or installs it if the workspace is bare. Reword the verdict condition so an unbound client account does not read as a blocker on an own-account build.
5. Assumptions (missed old-CRM import, Prospects board fate, invented sample data): add an assumption and question for each thing the call raises and leaves open, even when it is only handover work. Use the kinds consistently: a structural choice with a stated condition is a leaning or board-architecture, not a gap.
6. Questions (missed account ownership and leaver inheritance; hand-keyed ERP number only partly): when picking the few questions, prefer one per unresolved structural choice. Ownership of a shared account and who keys the ERP number outrank a second variant of an already-asked question.
7. Invented specifics: the seven-day flag and the enquiry-assignment automation have no basis on the call. Mark such numbers and automations as ours, give the key-style provisional figure for the user to correct, and drop automations the client never asked for.
8. Requote structure and the as-of date: when the call shows one pursuit with several ERP documents, offer the parent-with-child-rows leaning with its condition, and add an "ERP status as of" field to any hand-keyed ERP value so staleness shows.
