import json,os,re
F="/Users/caramelm4/DelOps/monday-master-builder-dev/rebuild-workspace/fixtures"
A=["s1-discovery-strong","s3-followup-demo-feedback","s10-support-checkin"]
B=["s8-discovery-enterprise-pmo","s9-followup-no-portfolio-unlabelled"]
def load(s):
    t=open(os.path.join(F,s,"transcript.txt")).read()
    k=open(os.path.join(F,s,"answer-key.json")).read()
    c=""
    p=os.path.join(F,s,"context-v0.1.md")
    if os.path.exists(p): c=open(p).read()
    return t,k,c
def show(chain,tokens,label):
    print(f"\n===== CHAIN {label}: token presence (transcript / key / context) =====")
    data={s:load(s) for s in chain}
    for tok in tokens:
        row=[]
        for s in chain:
            t,k,c=data[s]
            row.append(f"{s.split('-')[0]}:T{t.count(tok)}/K{k.count(tok)}/C{c.count(tok)}")
        print(f"  {tok:34} "+"  ".join(row))
    print(f"\n----- money figures per file ({label}) -----")
    for s in chain:
        t,k,c=data[s]
        print(f"  {s}")
        print("    transcript $:",sorted(set(re.findall(r"\$[\d,]+(?:\.\d+)?[km]?",t)))[:20])
        print("    key $       :",sorted(set(re.findall(r"\$[\d,]+(?:\.\d+)?[km]?",k)))[:25])
show(A,["Brackenholt","Tess","Kowalczyk","Jordan","Pruitt","Bev","Halvorsen","Gordon","Hallie","Karen","Anneke","Ajera","Bluebeam","Procore","Harwood","Oak Street","Des Moines","Madison","Milwaukee","Rockford","the Wall","Staff allocation","504,920","25,000","$25k","enterprise","Enterprise","pursuit","Pursuits","submittal","Microsoft"],"A (s1/s3/s10)")
show(B,["Bellamy Ridge","Marisol","Bettencourt","Warren","Tibbetts","Ines","Kovalenko","Stefan","Junie","Rasco","Cumberland","Waverly","Pellham","Knoxville","Chattanooga","Huntsville","Sage 300","Procore","Smartsheet","432,080","150,000","220","enterprise","Enterprise","portfolio","Portfolio","ICRA","superintendent"],"B (s8/s9)")
