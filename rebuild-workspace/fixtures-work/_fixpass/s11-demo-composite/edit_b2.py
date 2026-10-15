import re
P='/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures/s11-demo-composite/transcript.txt'
t=open(P,encoding='utf-8').read()
split_after="and the crew lead marks eight short and two damaged, and that's it, their job is done, they go home. "
resume_old="The second it's marked, and this is the first of the two automatic things I've built, sales get told."
assert t.count(split_after)==1 and t.count(resume_old)==1
# words of the tour before and after the split
tour_start=t.index("[04:19] Consultant\n")+len("[04:19] Consultant\n")
tour_end=t.index("\n\n[13:12]")
tour=t[tour_start:tour_end]
i=tour.index(split_after)+len(split_after)
w1=len(tour[:i].split()); w2=len(tour[i:].split())
desmond="Sorry. Hang on. Who's marking that? In the story. Who's actually typing it in?"
cons_pre="The crew lead. On a phone, at the dock, in the story. I'll show you that properly when we get to Hattie's charges, because it's the bit I most want you to pull apart, so hold the thought. Where was I. Short, damaged. Yes. "
wd=len(desmond.split()); wc=len(cons_pre.split())
total=259+533  # 04:19 to 13:12
# budget: 533 s for w1 + wd + wc + w2 words; give Desmond 6 s, split the rest by words
rest=533-6
rate=(w1+wc+w2)/rest  # words per second
t1=259+round(w1/rate)
t2=t1+6
print("w1",w1,"w2",w2,"desmond",wd,"cons",wc)
print("part1 rate wpm",round(60*w1/(t1-259),1),"part2 rate wpm",round(60*(wc+w2)/(792-t2),1))
s1="%02d:%02d"%divmod(t1,60); s2="%02d:%02d"%divmod(t2,60)
print("stamps",s1,s2)
new=split_after.rstrip()+"\n\n["+s1+"] Desmond Farrow\n"+desmond+"\n\n["+s2+"] Consultant\n"+cons_pre+resume_old
t=t.replace(split_after+resume_old,new)
open(P,'w',encoding='utf-8').write(t)
print("B2 applied")
