import json,re,sys
BASE='/Users/caramelm4/DelOps/rebuild-workspace/fixtures/s9-followup-no-portfolio-unlabelled'
t=open(BASE+'/transcript.txt',encoding='utf-8').read()
paras=[p for p in t.split('\n\n') if p.strip()]
key=json.load(open(BASE+'/answer-key.json',encoding='utf-8'))
rows=[]
def walk(n,path):
    if isinstance(n,dict):
        if 'quote' in n and isinstance(n['quote'],str) and 'location' in n:
            rows.append((n['quote'],n['location'],path))
        for k,v in n.items(): walk(v,path+'.'+k)
    elif isinstance(n,list):
        for i,v in enumerate(n): walk(v,'%s[%d]'%(path,i))
walk(key,'key')
bad=0; spk={}
for q,loc,path in rows:
    hits=[i+1 for i,p in enumerate(paras) if q in p]
    m=re.search(r'paragraph (\d+)',loc)
    stated=int(m.group(1)) if m else None
    if hits!=[stated]:
        bad+=1; print('MISMATCH %s stated=%s actual=%s q=%r'%(path,stated,hits,q[:60]))
    s=re.search(r'inferred ([A-Za-z ]+?) \(speaker unclear\)',loc)
    if s and stated: spk.setdefault(stated,set()).add(s.group(1).strip())
    if not s: print('NO INFERRED SPEAKER in location: %s -> %s'%(path,loc))
print('rows with location:',len(rows),'mismatches:',bad)
print('--- paragraphs attributed to >1 speaker ---')
for p,v in sorted(spk.items()):
    if len(v)>1: print(' P%d:'%p, sorted(v))
print('--- attribution map ---')
for p,v in sorted(spk.items()): print(' P%-4d %s'%(p,'/'.join(sorted(v))))
