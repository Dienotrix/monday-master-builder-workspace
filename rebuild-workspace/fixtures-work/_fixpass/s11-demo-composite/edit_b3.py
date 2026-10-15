P='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s11-demo-composite/transcript.txt'
t=open(P,encoding='utf-8').read()
old_principle="[25:39] Consultant\nThen those are the items that get the committed column first, and chairs can wait. The two tents and the dance floor sections, and anything else there's only one or two of, which you'll know and I won't. That's a better version than the one I built, because it's smaller, and it's the version I'd have built if I'd asked you instead of Anjali. I'll list it that way tonight.\n\n[26:09] Anjali Venkataraman\nFine. Do the crew board. That's the one Des needs to see.\n\n[26:17] Consultant\n"
assert t.count(old_principle)==1
fumble="Right. So -- so what I'd do with that is, um, I'd put a flag on the tent, a sort of warning on the tent rows, so when the ten-by-twenty goes on a quote it -- no. Hang on. That's the same column wearing a different hat."
correct="I don't want a warning. I want to know which wedding the tent's already on. The tent and the floor. Not the chairs."
principle="Then those are the items that get the committed column first, and chairs can wait. The two tents and the dance floor sections, and anything else there's only one or two of, which you'll know and I won't. That's a better version than the one I built, because it's smaller. I'll list it that way tonight."
anjali="Fine. Do the crew board. That's the one Des needs to see."
# the crew-board turn text, as edited in B1
cb_start=t.index(old_principle)+len(old_principle)
cb_end=t.index("\n\n[28:05]")
crew=t[cb_start:cb_end]
wf,wc_,wp,wa,wcrew=[len(x.split()) for x in (fumble,correct,principle,anjali,crew)]
# window 25:39 (1539 s) to 28:05 (1685 s) = 146 s for all five turns; one rate throughout
rate=(wf+wc_+wp+wa+wcrew)/146.0
t0=1539
t1=t0+round(wf/rate); t2=t1+round(wc_/rate); t3=t2+round(wp/rate); t4=t3+round(wa/rate)
st=lambda s:"%02d:%02d"%divmod(s,60)
print("words",wf,wc_,wp,wa,wcrew,"rate wpm",round(60*rate,1))
print("stamps fumble 25:39, correction",st(t1),"principle",st(t2),"anjali",st(t3),"crew board",st(t4),"crew-board wpm",round(60*wcrew/(1685-t4),1))
new="[25:39] Consultant\n"+fumble+"\n\n["+st(t1)+"] Hattie Szabo\n"+correct+"\n\n["+st(t2)+"] Consultant\n"+principle+"\n\n["+st(t3)+"] Anjali Venkataraman\n"+anjali+"\n\n["+st(t4)+"] Consultant\n"
t=t.replace(old_principle,new)
open(P,'w',encoding='utf-8').write(t)
open('b3_stamps.txt','w').write("anjali %s\ncrew %s\ncorrection %s\nprinciple %s\n"%(st(t3),st(t4),st(t1),st(t2)))
print("B3 applied")
