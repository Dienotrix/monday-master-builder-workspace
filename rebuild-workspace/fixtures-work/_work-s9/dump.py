import re,sys
p='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s9-followup-no-portfolio-unlabelled/transcript.txt'
t=open(p,encoding='utf-8').read()
paras=[x for x in t.split('\n\n') if x.strip()]
words=len(t.split())
print("PARAGRAPHS:",len(paras),"WORDS:",words)
print("ASCII-only:", all(ord(c)<128 for c in t))
print("Non-ascii chars:", sorted({c for c in t if ord(c)>=128}))
print("Any line with a colon-style label?:", bool(re.search(r'^[A-Z][a-z]+ [A-Z][a-z]+ ?\(?.*?\)?:',t,re.M)))
print()
for i,x in enumerate(paras,1):
    ts=re.match(r'\[(\d\d:\d\d:\d\d)\]',x)
    print(f"--- P{i} {'['+ts.group(1)+']' if ts else ''} ({len(x.split())}w)")
    print(x)
