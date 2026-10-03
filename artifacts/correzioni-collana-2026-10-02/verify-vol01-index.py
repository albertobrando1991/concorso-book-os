from pathlib import Path
import pymupdf,json,re,unicodedata
A=Path(__file__).parent;d=pymupdf.open(A/'vol-01-stable-release-20261003-proof.pdf');dom=json.loads((A/'vol-01-stable-release-20261003-proof-metrics.json').read_text('utf-8'))
def norm(s):return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',s)).lower()
rows=[]
for i in range(6,17):
 s=d[i].get_text();s=s[s.index('Indice'):] if i==6 else s[s.index('CAPITALE PERSONALE')+len('CAPITALE PERSONALE'):]
 for m in re.finditer(r'(?m)^(\d+\.\d+|[A-F]\.\d+|[1-7])\s*\n([^\d\n].*?)\n(\d+)\s*(?=\n|$)',s,re.S):
  title=' '.join(m[2].split());target=int(m[3]);rows.append(dict(kind='section',number=m[1],title=title,indexPage=i+1,targetPage=target,match=norm(title) in norm(d[target-1].get_text())))
 for m in re.finditer(r'(?m)^Capitolo (\d+)(.*?)\n(\d+)\s*(?=\n|$)',s,re.S):
  title=' '.join(m[2].split());target=int(m[3]);rows.append(dict(kind='chapter',number=m[1],title=title,indexPage=i+1,targetPage=target,match=norm(title) in norm(d[target-1].get_text())))
 for m in re.finditer(r'(?m)^(Introduzione|Conclusione|Appendice [A-F])(.*?)\n(\d+)\s*(?=\n|$)',s,re.S):
  title=' '.join(m[2].split()).lstrip(' -–—');target=int(m[3]);rows.append(dict(kind='apparatus',number=m[1],title=title,indexPage=i+1,targetPage=target,match=norm(title) in norm(d[target-1].get_text())))
chapters=[r for r in rows if r['kind']=='chapter'];assert len(chapters)==24
apparati=[r for r in rows if r['kind']=='apparatus'];assert len(apparati)==8,apparati
sections=[r for r in rows if r['kind']=='section'];assert len(sections)==405,len(sections)
out=dict(pdf=d.name,entries=rows,chapters=len(chapters),apparatus=len(apparati),sections=len(sections),mismatches=[r for r in rows if not r['match']])
(A/'VOL-01-index-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),'utf-8');print(json.dumps({k:v for k,v in out.items() if k not in ['entries','pdf']},ensure_ascii=False))
