import io
P='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s11-demo-composite/transcript.txt'
t=open(P,encoding='utf-8').read()
edits=[
 # 01:49 opening: a false start
 ("Okay. So let me say how I'd like to use the time, and you tell me if it's wrong.",
  "Okay. So. Let me -- let me say how I'd like to use the time, and you tell me if it's wrong."),
 # 04:19 tour: false start and an unfinished clause
 ("the event date, the venue, the salesperson, the value, and the stage, which is this coloured column here.",
  "the event date, the venue, the salesperson, which is going to be, well, mostly it'll be -- anyway. The value, and the stage, which is this coloured column here."),
 # 04:19 tour: navigation filler
 ("Now the Clients board. Sorry, wrong tab. There. One row per client organisation.",
  "Now the -- where's it gone. Now the Clients board. Sorry, wrong tab, that's the filter. There. One row per client organisation."),
 ("Third board, Events. This is the one Anjali liked most last week, so I'll go a bit slower.",
  "Third board, Events. Hang on, can you still see this? Desmond? The small screen. Okay. Events. This is the one Anjali liked most last week, so I'll go a bit slower."),
 # 13:22: navigation filler before the walk-through
 ("We can, and I was going to. So, Hattie. On our first call, two weeks ago,",
  "We can, and I was going to. So, Hattie. Let me just get -- no, that's the event, I want the quote. There. On our first call, two weeks ago,"),
 # 19:11: the repeated explanation (the one-set-of-lines point from 13:22, said again)
 ("this column, which I've called Committed. For every item, it adds up what's on every event that weekend.",
  "this column, which I've called Committed. For every item, and the items here are the lines, the same lines, I said this on the quote, the quote's lines are the event's lines, it's one set, so I won't say it a third time -- for every item, it adds up what's on every event that weekend."),
 # 22:53: navigation filler after the protected first sentence
 ("so if I flip over to the crew board and turn the workload view round, trucks down the side,",
  "so if I flip over to the crew board, hang on, it's -- there, and turn the workload view round, trucks down the side,"),
 # 26:17 crew board: a filler and an unfinished clause
 ("and a status that goes from planned to on the road to done, which the crew lead flips from the phone,",
  "and a status that goes from, um, planned to on the road to done, which the crew lead flips from the phone,"),
 ("and the crew one is just today, just their truck, and nothing else. And the workload view,",
  "and the crew one is just today, just their truck, and nothing else, because the last thing a crew lead wants at six in the morning is -- well. Nothing else. And the workload view,"),
 # 38:46: navigation filler after the protected restatement
 ("never get raised. So. Count-in board. Every event that's come back has a row,",
  "never get raised. So. Count-in board. Which is -- no, that's Items, sorry, they sit next to each other. Count-in. Every event that's come back has a row,"),
 # 47:34: a false start after the protected first sentence
 ("So let me answer it properly instead of nodding. The boards work on a phone through the mobile app,",
  "So let me answer it properly instead of nodding. The way it -- so, the boards work on a phone through the mobile app,"),
]
for old,new in edits:
    assert t.count(old)==1, old[:60]
    t=t.replace(old,new)
open(P,'w',encoding='utf-8').write(t)
print("B1 applied:",len(edits),"edits")
