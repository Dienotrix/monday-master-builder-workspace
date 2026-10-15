import sys; sys.path.insert(0,'.')
import keyfmt
K='/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s11-demo-composite/answer-key.json'
k=keyfmt.load(K)
log=[]
def rep(obj,key,old,new,where):
    s=obj[key]; assert old in s,(where,old[:50]); obj[key]=s.replace(old,new); log.append(where)

# ---- 1. counts and transcript-derived fields (after the three transcript steps)
rep(k,'purpose_of_this_fixture',"opens with a 1,416-word tour of six boards, and runs three more turns of 400 to 500 words.",
    "opens with a tour of six boards that runs 1,077 words before the warehouse manager interrupts it with a question and 416 more after, and runs four more turns of 400 to 540 words.","purpose: tour counts")
rep(k,'purpose_of_this_fixture',"the tour is an own-side stretch,","the tour is two own-side stretches split by one client interruption,","purpose: stretches")
k['transcript_format']=("Plain text, 257 lines, 86 speaker turns. Each turn is a label line '[MM:SS] Speaker Name' followed by one text line, with a blank line between turns; the timestamp is the turn start in elapsed minutes and seconds, unpadded past the hour ('[61:47]'), start-only, no end times, no participant header, no call date. Four labels: 'Consultant', 'Anjali Venkataraman' (General Manager), 'Hattie Szabo' (Sales Manager), 'Desmond Farrow' (Warehouse and Dispatch Manager). About 9,006 spoken words. By label the Consultant carries 81.7% and the client side 18.3% (Anjali 12.9%, Hattie 3.5%, Desmond 1.9%), but the [28:05] block (878 words, 9.7% of the file) is labelled Anjali and is composite, so the by-label figures are not a talk share; see intake.talk_share. Longest turn 1,077 words at [04:19] (the tour up to the warehouse manager's interruption at 10:39, 6 minutes 20 seconds; the tour resumes at 10:45 for 416 words to 13:12); the block is the second longest. Non-verbal and transcriber cues in square brackets ([laughs], and one [inaudible] at 01:10 where the warehouse manager is still walking in from the dock); restarts and self-corrections use ' -- ' (sixteen, in thirteen turns); the Consultant's long turns carry false starts, screen-navigation filler, one explanation repeated from an earlier turn (the one set of lines, 13:22 and again at 19:11) and two clauses that never finish (04:19, 26:26); the reply to the sales manager's correction at 25:23 takes two attempts (a wrong first answer at 25:39, her correction at 25:55, the restatement at 26:03). ASCII only, LF line endings. Date clues: the next meeting is 'Thursday the eighth', October is still ahead ('What happens in October?'), so the call sits in late September 2026; 'it's Wednesday' appears only inside the composite block and must not fix the date. Every location in this key is 'MM:SS Speaker Name (role)' from the label line the quote sits under, 'MM:SS Consultant' for our side, and for the composite block '28:05 block, segment N, a participant on the client side (speaker not resolvable)' or '28:05 block, segment N, our side (speaker not resolvable by label)', segments numbered 1 to 9 in order as listed in intake.composite_blocks.")
log.append('transcript_format rewritten with the new counts')
tr=k['traps']
i=[n for n,t in enumerate(tr) if t.startswith("The [04:19] tour is one own-side stretch")][0]
tr[i]=("The tour is two own-side stretches, not one: 1,077 words and 6 minutes 20 seconds from the last client word ('Yep.' at 04:16) to Desmond's interruption at 10:39, then 416 words and 2 minutes 27 seconds from 10:45 to Hattie at 13:12, with one check-in at its end. The interruption is a client word and splits the stretch; it is a question about the mechanism ('Who's actually typing it in?'), not a confirmation of anything, and the presenter picked the tour back up after answering it. The 19:11 and 22:53 turns are two stretches, not one: Anjali's 22:46 is a client word between them.")
log.append('traps[%d]: tour stretch rewritten'%i)
ab=k['accepted_behaviours']
j=[n for n,t in enumerate(ab) if "Reporting 18.4%" in t][0]
rep(ab,j,"Reporting 18.4% as the client share","Reporting 18.3% as the client share","accepted_behaviours: by-label share")
lb=k['expected_leak_blocklist']
j=[n for n,t in enumerate(lb) if "'18.4%'" in t][0]
rep(lb,j,"'18.4%'","'18.3%'","leak blocklist: by-label share")
it=k['intake']
ef=it['export_family']
ef.update({"units":86,"words":9006,"max_unit_words":1077,"second_longest_unit_words":878,
  "max_unit_seconds":"not measurable (start-only); the tour's first part spans 380 seconds to the interruption, the block 379",
  "note":"Measured before any content is read. The unit-length distribution has two outliers far above the file's own percentile (the first part of the tour and the block; the next unit is 536 words), which is what gates the composite splitter on a file with no end times."})
log.append('intake.export_family counts')
rep(it['detectors'],'composite_splitter',"does not flag the [04:19] tour or the other long Consultant turns","does not flag the [04:19] and [10:45] tour turns or the other long Consultant turns","intake.detectors")
cb=it['composite_blocks']['28:05']
rep(cb,'not_composite',"The [04:19] tour (1,416 words) and the 13:22, 19:11, 22:53, 38:46 and 47:34 turns","The [04:19] tour (1,077 words to the interruption at 10:39, and 416 more at 10:45) and the 13:22, 19:11, 22:53, 26:26, 38:46 and 47:34 turns","composite_blocks.not_composite")
it['rejoined_sentences']=("none needed: no sentence is split across turns; the sixteen ' -- ' restarts (00:52, 01:49, 04:19 twice, 13:12, 13:22, 19:11, 22:53, 25:39 twice, 26:26, 28:05 twice inside the block, 38:46, 47:34, 54:43) stay inside their own units, and the two clauses that never finish ('mostly it'll be -- anyway' at 04:19, 'is -- well' at 26:26) are abandoned by the speaker, not cut by the export, so nothing is re-joined")
log.append('intake.rejoined_sentences')
oss=it['own_side_stretches']
oss[0:1]=[{"from":"04:16 (last client word, 'Yep.')","to":"10:39 (Desmond)","words":1077,"seconds":380,"note":"the tour to the interruption; every showing inside it exceeds the per-showing cap; the one client word inside the tour is a question about who types the count, not a check-in"},
          {"from":"10:45 (the tour resumes)","to":"13:12 (Hattie)","words":416,"seconds":147,"note":"the rest of the tour, the count-in notifications and the weekend page; one check-in at its end"}]
oss[2].update({"words":536}); rep(oss[2],'note',"22:53 to 25:16 (397 words)","22:53 to 25:16 (402 words)","own_side_stretches[2]")
oss[3].update({"words":470})
log.append('intake.own_side_stretches: tour split in two, word counts refreshed')
ts=it['talk_share']
ts['by_label_whole_call']={"client":18.3,"our_side":81.7,"warning":"not a talk share: the [28:05] block (878 words, 9.7% of the file) is composite and above the few-percent cutoff"}
ts['attributable_only']={"client_words":769,"our_side_words":7359,"unattributable_words":878,"client_share_of_attributable":9.5}
ts['if_segments_confirmed']={"client":17.2,"note":"782 of the block's words are client side; this is the figure C56 calls roughly 17%"}
ts['per_phase_by_label']=[
 {"phase":"before the share, 00:03 to 03:07","words":387,"client":35.1},
 {"phase":"the tour, 03:12 to 13:12","words":1680,"client":2.4,"note":"the client words are 'We see it.', 'Yep.' and the warehouse manager's interruption at 10:39"},
 {"phase":"pain by pain, 13:22 to 46:10","words":4774,"client":25.7,"note":"includes the 878 unattributable words of the block; attributable client share of this phase is 8.9%"},
 {"phase":"after the share, 46:19 to 61:47","words":2165,"client":11.3}]
ts['showing_window'].update({"words":6454,"client_by_label":19.6})
log.append('intake.talk_share recomputed')
dn=it['delivery_notes']
dn[0]="Client share by label 18.3% whole-call, 19.6% over the showing window, 2.4% during the tour; the block makes the whole-call figure unreliable and the attributable client share is 9.5%. Below the 30 to 40% band everywhere but the first three minutes."
dn[1]="Defect: the tour ran 1,077 words and 6 minutes 20 seconds before a client spoke, and the client word was an interruption rather than a check-in; the presenter announced it, still ran it, answered the interruption and ran 416 more words to one check-in at the end, and every showing in it is over the cap. Defect: three client ties answered with 'It can also' (22:53, 42:29, 44:36) instead of a one-sentence confirmation; the cascades are the exit-ramp cue and were missed each time."
rep(dn,3,"the current-state question asked before the red bit was shown;","the current-state question asked before the red bit was shown; a wrong first answer to the sales manager (25:39) corrected by her (25:55) before the smaller version was stated (26:03);","delivery_notes[3]")
log.append('intake.delivery_notes[0], [1] recomputed; [3] gains the two-turn reply')

# ---- 2. direction rename (s11 to s25)
th=it['type_header']; new={}
for key,v in th.items():
    nk={'direction_of_show':'direction','direction_of_show_note':'direction_note'}.get(key,key); new[nk]=v
it['type_header']=new; log.append('intake.type_header: direction_of_show -> direction, direction_of_show_note -> direction_note')
j=[n for n,t in enumerate(ab) if "direction of show changes" in t][0]
rep(ab,j,"where direction of show changes from we show to nobody shows","where the direction changes from we show to nobody shows","accepted_behaviours: prose follows the rename")

# ---- 3. sweep corrections (pattern 4: our framing labelled as the client's)
v=k['vocabulary']
e=[x for x in v if x['their_term']=="short / damaged"][0]
e['their_term']="shortage (the client's word); short / damaged (the Consultant's labels)"
e['meaning']="A line that came back missing or broken and should raise a charge. The client says 'shortage' (44:26), 'eight chairs' and 'cigarette burns' (41:57); 'short' and 'damaged' are the Consultant's status labels, unchallenged on the call and read back before v0.2"
log.append("vocabulary['short / damaged']: relabelled as the Consultant's words")
e=[x for x in v if x['their_term']=="count sheet / count-in"][0]
e['meaning']="The paper record of what came back is the client's 'count sheet' (41:57); 'count-in' is the Consultant's word for the act and the board, unchallenged but not the client's"
log.append("vocabulary['count sheet / count-in']: 'count-in' labelled as ours")
e=[x for x in v if x['their_term']=="the Thursday board / the whiteboard"][0]
e['meaning']="The weekly dispatch plan on a whiteboard with magnets, redone as venues move. 'The whiteboard' is attributed (51:23); 'the Thursday board' is spoken only inside the composite block, side-only"
e['likely_monday_object']="the Crew schedule board and its by-truck workload view; 'the Thursday board' is heard only inside the block, so it is confirmed by name before it names anything"
log.append("vocabulary['the Thursday board / the whiteboard']: side-only status stated")
j=[n for n,t in enumerate(lb) if t.startswith("CAUTION:")][0]
lb[j]="CAUTION: 'dead', 'sent back', 'shortage', 'the whiteboard', 'the yard', 'crew lead', 'truck three' are the client's own vocabulary and must survive in client-facing output; 'short', 'damaged' and 'count-in' are the Consultant's labels and 'the Thursday board' is heard only inside the composite block, so each is kept until read back and replaced if the client's word differs; only the narratives around them are blocked."
log.append('leak blocklist CAUTION line: the three Consultant labels and the side-only term no longer called the client\'s')
im=k['integrations_mentioned']
rep(im,4,"the current source of the Thursday board (side-only), replaced by the Events board.","the current source of the Thursday board (side-only); to be replaced by the Events board on the assumption that it holds nothing that does not start as a quote, which the sales administrator, who was not in the room, is asked (readiness leaning 9).","integrations_mentioned[4]: replacement labelled an assumption")

# ---- 4. the never-written rule (weaker form, labelled ours)
rep(im,0,"Not in scope.","Not in scope. Writeback and integration direction unresolved; v0.1 does not depend on either; staying clear of the accounting system is our safe default, labelled as ours.","integrations_mentioned[0]: never-written wording")

# ---- 5. standing lines
c=k['commitments_and_next_steps'][0]
rep(c,'owner',"the invite to the three attendees was sent during the call at 60:49","the Consultant said at 60:49 that the invite to the three attendees was being sent while on the call: committed, not evidenced as received","commitments[0].owner (s21)")
rep(dn,3,"the invite sent on the call;","the invite committed on the call, by the Consultant's own word at 60:49;","delivery_notes[3] (s21)")
ncl=it['next_close_list']
rep(ncl,4,"then the next step with the invite sent on the call","then the next step, with the invite confirmed as received rather than taken as sent","next_close_list[4] (s21)")
keyfmt.save(k,K)
print("\n".join(log))
