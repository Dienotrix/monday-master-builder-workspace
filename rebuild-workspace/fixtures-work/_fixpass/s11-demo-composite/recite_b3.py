import sys; sys.path.insert(0,'.')
import keyfmt
K='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s11-demo-composite/answer-key.json'
k=keyfmt.load(K)
# R8 evidence location
ev=k['rubric'][7]['evidence'][2]
assert ev['location']=="26:09 Anjali Venkataraman (General Manager)"
ev['location']="26:22 Anjali Venkataraman (General Manager)"
# R1 note: the Consultant's restatement at 26:17 is now at 26:26
n=k['rubric'][0]['note']; assert "13:22, 19:11, 26:17 and 38:46" in n
k['rubric'][0]['note']=n.replace("13:22, 19:11, 26:17 and 38:46","13:22, 19:11, 26:26 and 38:46")
# quarantine not_quarantined list of client turns inside the share
q=k['intake']['quarantine']["03:12 to 46:19, the Consultant's screen share"]
s=q['not_quarantined']; assert "25:23, 26:09, 37:02" in s
q['not_quarantined']=s.replace("25:23, 26:09, 37:02","25:23, 25:55, 26:22, 37:02")
keyfmt.save(k,K)
print("re-cited: R8 evidence 26:09 -> 26:22; R1 note 26:17 -> 26:26; not_quarantined list adds 25:55 and moves 26:09 -> 26:22")
