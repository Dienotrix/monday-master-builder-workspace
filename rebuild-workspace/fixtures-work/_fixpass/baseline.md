# Quote baseline for the 25 fixtures

Written 2026-10-13 in the first step of the fix pass, with `verify_quotes.py`. It records what `verify_quotes.py` reports on the twenty-five keys as they stood before any editor touched a transcript or a quote. No key was fixed, no fixture file was edited, and no quote was changed to make a count come out.

## Result in one paragraph

Every structured quote in every key is verbatim at its cited location. The script finds 3,818 quote strings in the twenty-five keys, verifies 3,812 of them, and reports no miss and no near-miss. The six that are not verified are not failures: three are bare location pointers in s21, two are descriptions about a quote in s22, and one is the label of a figure image in s25 that this script cannot read. Eleven more values are null and are counted as skipped. The reason there is nothing to fix is that the earlier builders checked each key against its transcript with their own scripts, and this script reaches the same answer by a separate route. The proof that the script is not simply agreeing with everything is in the section on how it was tested.

## How the baseline was taken

- Command: `python3 verify_quotes.py <fixture folder>`, once per folder, with `--json --spans` as well to collect the unit and span counts. Exit status was 0 for all twenty-five.
- The first complete run over all twenty-five folders was made before the editors' changes began to land, and the pair counts below match it exactly.
- While this step was running, other fix-pass agents had already started on s1 and s5 and had added their `readiness` blocks to those two keys. To keep the baseline unedited, the figures for every fixture come from a copy of the fixtures folder taken after that first run, with the `readiness` field removed from the copies of the s1 and s5 keys. Their counts (175 and 62 pairs) equal the counts of the first run, so nothing else in those two keys had moved. Running the script on the live s1 and s5 folders now reports more pairs, because the new block carries quotes of its own; those verified too.
- Definitions. A pair is a string value under a key whose name carries the word quote, together with its location. `pairs` counts every non-null quote string, including the three pointers. `skipped` is the null or empty values plus the pointers. `presence only` is the part of `verified` that has no location in the key at all, so it was checked for presence in the fixture's files and not at a place. `units parsed` is the number of speech units read from the fixture's transcript and chat files; it matches the README of every fixture that states a unit count (s11 82, s12 214 plus 11 chat messages, s14 415, s15 487, s16 298). `units protected` and `spans` come from `--spans`: the transcript units that hold at least one quoted span the key protects, and the number of merged spans in them.

## Table

| fixture | pairs | verified | skipped | unparsed prose | near-misses | misses | unsupported forms | presence only | units parsed | units protected | spans |
|---|---|---|---|---|---|---|---|---|---|---|---|
| s1-discovery-strong | 175 | 175 | 0 | 0 | 0 | 0 | 0 | 25 | 93 | 135 |
| s2-discovery-gaps | 98 | 98 | 0 | 0 | 0 | 0 | 0 | 25 | 56 | 68 |
| s3-followup-demo-feedback | 142 | 142 | 0 | 0 | 0 | 0 | 0 | 41 | 71 | 100 |
| s4-discovery-software | 121 | 121 | 0 | 0 | 0 | 0 | 0 | 19 | 83 | 90 |
| s5-intro-thin | 62 | 62 | 2 | 0 | 0 | 0 | 0 | 16 | 25 | 40 |
| s6-discovery-crm-sales | 147 | 147 | 0 | 0 | 0 | 0 | 0 | 25 | 96 | 99 |
| s7-discovery-service-desk | 145 | 145 | 0 | 0 | 0 | 0 | 0 | 29 | 101 | 101 |
| s8-discovery-enterprise-pmo | 222 | 222 | 0 | 0 | 0 | 0 | 0 | 25 | 134 | 167 |
| s9-followup-no-portfolio-unlabelled | 121 | 121 | 0 | 0 | 0 | 0 | 0 | 36 | 48 | 70 |
| s10-support-checkin | 61 | 61 | 2 | 0 | 0 | 0 | 0 | 9 | 35 | 49 |
| s11-demo-composite | 120 | 120 | 0 | 0 | 0 | 0 | 0 | 25 | 47 | 64 |
| s12-header-present | 158 | 158 | 3 | 0 | 0 | 0 | 0 | 32 | 107 | 120 |
| s13-header-absent | 165 | 165 | 0 | 0 | 0 | 0 | 0 | 28 | 113 | 128 |
| s14-shred-block | 154 | 154 | 0 | 0 | 0 | 0 | 0 | 34 | 117 | 117 |
| s15-shred-dense | 166 | 166 | 0 | 0 | 0 | 0 | 0 | 30 | 144 | 147 |
| s16-shred-cue | 124 | 124 | 0 | 0 | 0 | 0 | 0 | 24 | 110 | 110 |
| s17-no-markers | 122 | 122 | 0 | 0 | 0 | 0 | 0 | 32 | 80 | 100 |
| s18-identity-collapse | 146 | 146 | 0 | 0 | 0 | 0 | 0 | 31 | 115 | 127 |
| s19-reverse-demo | 188 | 188 | 1 | 0 | 0 | 0 | 0 | 26 | 132 | 132 |
| s20-large-group | 224 | 224 | 0 | 0 | 0 | 0 | 0 | 28 | 149 | 174 |
| s21-existing-account | 165 | 162 | 3 | 0 | 0 | 0 | 0 | 24 | 119 | 120 |
| s22-degrading-commitment | 233 | 231 | 1 | 2 | 0 | 0 | 0 | 27 | 165 | 176 |
| s23-symmetric-shred | 166 | 166 | 0 | 0 | 0 | 0 | 0 | 25 | 112 | 119 |
| s24-package | 262 | 262 | 0 | 0 | 0 | 0 | 0 | 37 | 206 | 218 |
| s25-client-documents | 131 | 130 | 2 | 0 | 0 | 0 | 1 | 11 | 56 | 71 |
| **total** | **3818** | **3812** | **14** | **2** | **0** | **0** | **1** | **664** | **2514** | **2842** |

The rows add up as pairs = verified + unparsed prose + near-misses + misses + unsupported forms + pointers (the pointers are the 3 skipped values of s21). The other skipped values are null and are not pairs.

## Remaining misses and near-misses

None. The list the editors were told to expect is empty.

What the script did report that is not a miss, each with its place so no one has to look for it:

| fixture | kind | where | what it is |
|---|---|---|---|
| s21 | skipped, location pointer | `intake.current_state_met_early.from_quotes[0..2]` | Three strings that are locations only (`00:03:20 ...`, `00:04:25 ...`, `00:05:08 ...`). There is no quote text to compare. The script checks that each resolves to a real unit, and all three do. |
| s22 | unparsed prose | `intake.second_hand[0].figure_as_requoted` | A description of the figure the Consultant re-quoted ("about twenty a week, hedged"). It is not a quotation. |
| s22 | unparsed prose | `intake.second_hand[1].contrast_with_the_wrong_requote` | A sentence of explanation. The two key names carry the word quote but hold prose, so the script names them in a short list and does not fail them. |
| s25 | unsupported form | `rubric[0].evidence[4].quote`, location `figure 1 p.1`, quote "Log in sample register" | The quote is a label inside the figure image `QP-07-F1-sample-flow.png`. An image cannot be read with the standard library alone, so the script skips it and says so. |
| s5 | skipped null | `numbers.bleed.quote`, `numbers.upside.quote` | Null in the key. |
| s10 | skipped null | `numbers.bleed.quote`, `numbers.upside.quote` | Null in the key. |
| s12 | skipped null | `intake.second_hand[1..3].true_source.quote` | Null in the key. |
| s19 | skipped null | `numbers.upside.quote` | Null in the key. |
| s22 | skipped null | `intake.claims_by_our_side[0].quote` | Null in the key. |
| s25 | skipped null | `numbers.upside.quote`, `intake.second_hand[1].true_source.quote` | Null in the key. |

The key's own refusals are not checked, on purpose. `intake.refused_quotes` lists spans the key declines to cite because they cross a label: s14 has 8, s16 has 6, s17 has 6, s23 has 10. They are examples of text that must not be quoted, so they are expected not to verify.

No pair carries a location note either. A location note appears when the line, cue, turn or paragraph number in a citation points at a unit whose stamp or label disagrees with the rest of the citation. There are none in the baseline, which means the stamps and labels in all 3,812 verified citations also agree with the units they point at. The script reads two more things that never came up: a merged run that crosses a change of speaker, and a quote cited to one segment of a composite block while it sits in another. Both are checked, and the segment check ran on 28 citations in s11 and s17 and passed on all of them.

## How the script was tested

A script that reports no misses has to be shown able to report one. From the baseline copies I took, per fixture, up to twenty verified located quotes (500 in all) and changed one thing at a time, in memory, never in a file:

| change | tried | reported correctly |
|---|---|---|
| one word of the quote altered | 500 | 500 as a miss |
| the first letter's case swapped | 500 | 500 as a near-miss |
| the first comma, full stop or question mark removed | 482 | 395 as a near-miss; the other 87 removed only the final stop, which leaves a true substring of the unit, so verified is right |
| the line, cue or stamp of the citation moved | 480 | 459 as a miss that names where the quote is found; the other 21 (20 in s17, 1 in s9) moved only the stamp while the turn or paragraph number stayed right, which is a location note and not a miss, by design |

A mutated copy of s14 also showed the layout of the report: a typo in the quote, a citation moved two lines, a changed final stop and a quote that appears nowhere each produced a readable entry with the quote, the cited location, where it was found instead and the nearest text.

## Location grammars the script reads

The grammar per fixture, taken from the fixture's own files and README. All of them parsed on the first full run, so no form had to be added to reach zero.

| fixture | unit format and location form |
|---|---|
| s1 | `[HH:MM:SS] Name: text`; location `HH:MM:SS Name (role)` |
| s2 | `Name: text`, no stamps; location `L<n>, Name` (physical line) |
| s3 | `Name (HH:MM:SS): text`; `HH:MM:SS Name (role)` |
| s4 | WebVTT, `Name: text` in the cue; `cue N, HH:MM:SS.mmm, Name` |
| s5 | `[HH:MM:SS] Name: text`; `HH:MM:SS Name` |
| s6 | `[MM:SS] Name: text`; `[MM:SS] Name (role)` |
| s7 | SRT; `cue N, HH:MM:SS,mmm, Name` |
| s8 | WebVTT with `<v Name>`; `cue N, HH:MM:SS.mmm, Name` |
| s9 | blank-line separated paragraphs, optional `[HH:MM:SS]`; `paragraph N` (with an optional stamp), no labels |
| s10 | `Name: text`, no stamps; `L<n>, Name (role)` |
| s11 | label line `[MM:SS] Name` then text; `MM:SS Name (role)` and `MM:SS block, segment N, ...` |
| s12 | header block, then `Name   HH:MM:SS` and a text line; chat file `HH:MM:SS   Name` and a text line; `HH:MM:SS Name (role)` and `chat HH:MM:SS Name` |
| s13 | preamble, then `Name  MM:SS` and a text line; `MM:SS Name` |
| s14 | `M:SS Label: text`; `L<n>, M:SS Name` |
| s15 | `M:SS Label: text` (label shapes vary); `L<n>, M:SS, Label` and `L<a>-<b>, M:SS, Name (merged run)` |
| s16 | WebVTT, `Name: text`; `cue N, ...` and `cues N-M, ...` (merged run) |
| s17 | `Name MM:SS` and a text line; `turn N, MM:SS, Name` and `turn N, MM:SS, labelled Name, segment k (side-only)` |
| s18 | `[HH:MM:SS] Name: text`; `HH:MM:SS Name` |
| s19 | `[HH:MM:SS] Name: text`; `HH:MM:SS Name (role)` |
| s20 | `[HH:MM:SS] Name: text`; `HH:MM:SS Name (role)` |
| s21 | `[HH:MM:SS] Name: text`; `HH:MM:SS Name (role)` |
| s22 | call 1 `[HH:MM:SS] Name: text`, call 2 `Name (HH:MM:SS): text`; `call N, HH:MM:SS Name (role)` |
| s23 | `HH:MM:SS Name: text`; `L<n>, HH:MM:SS Name` |
| s24 | metadata block, topic dividers, `Name · mm:ss` and a text line, five files; `rec-NNNN, mm:ss Name (role)` |
| s25 | `[HH:MM:SS] Name: text`, plus a .docx, a PDF and a PNG; `HH:MM:SS Name (role)`, `QP-07 section N.N`, `write-up p.N section N, W-n`, `figure 1 p.1` |

Forms the script also accepts although no baseline key uses them yet: a quote list beside a `locations` list (the `readiness` leanings use it), a quote offered with a list of locations, a location at the end of the quote's own string, and an elision in a quote read as ordered fragments.

## What the script does not cover

- Quotes with no location. Each key carries between 9 and 41 of them, usually 25: the `quote` of each `numbers` item and `account_context.evidence_quote_or_null` have no location field. The script checks the text is somewhere in the fixture's files and, in `--spans`, protects every occurrence, but it cannot say the quote is at the right place. In all, 664 of the 3,812 verified pairs are of this kind.
- Quotes and figures inside prose. Phrases in single quotes inside notes, reasons and READMEs, and any number the key states (word counts, shares, unit counts, durations), are not read. Only values under a quote key are checked.
- Whether the quote supports the claim it is attached to, and whether the speaker role in parentheses is right. The role is ignored on purpose; the stamp and the label are matched.
- The key's own refusals (`refused_quotes`), by design, and the description keys named above.
- Index against stamp. Where a citation has an index (cue, turn, paragraph, line), the index picks the unit and a disagreeing stamp is reported as a location note only. An editor who renumbers units must therefore read the location notes as well as the misses.
- A quote that occurs in several units. A location that names the wrong one of two identical short quotes is caught only when the text at the cited unit differs; two identical lines at the right stamp and label cannot be told apart. The README of s21 names two such short quotes.
- Composite-block segments are checked only where the key gives the segment's start and end text (s11 and s17). The s14 block is cited as a unit, not by segment.
- Documents. The .docx is read from `word/document.xml` paragraphs and headings, so tables, headers, footers and tracked changes are not seen. The PDF is read from its plain or Flate text-showing operators in the Latin character set; a scanned, encrypted or font-subset PDF would be reported as unsupported. Images are skipped. The brief expected the PDF to be reported as not checkable; it turned out to be readable, so its eleven citations are verified (write-up p.1 section 1, section 2 with W-2, W-3, W-5, W-6, and p.2 section 3), and only the figure label is left.
- Cross-file consistency of the key and the README (counts, row lines). That belongs to the verifier checklist, not to this script.

## Using it during the pass

`python3 verify_quotes.py <fixture folder>` prints the counts and each miss on its own lines. `--spans` adds, per unit, the text between marks that must not change. `--json` is for scripted use. Exit 0 means every pair is verified, 1 means a miss or near-miss remains, 3 means the folder or key could not be read. Unparsed prose, unsupported forms and location notes do not change the exit status, so read them.

Because the script is the only gate for transcript edits, the s11 editor in particular should run it after every new turn and re-cite from its output: it lists where a quote is found when the old location no longer holds.
