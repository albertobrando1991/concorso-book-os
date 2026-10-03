from pathlib import Path
import json,hashlib
A=Path(__file__).parent;p=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico/chapters/04-ntc-sismica-geotecnica-sicurezza-strutturale.md')
t=p.read_text(encoding='utf8');label='**Riferimenti normativi e professionali.** ';assert t.count(label)==1
head,refs=t.split(label);assert '## ' not in refs
anchor='## Obiettivo';assert anchor in head
t=head.rstrip()+'\n';t=t.replace(anchor,label+refs.strip()+'\n\n'+anchor,1);p.write_text(t,encoding='utf8')
q=A/'VOL-10-layout-reference-delta.json';d=json.loads(q.read_text(encoding='utf8'))
for r in d['files']:
 if r['path']==p.as_posix():r['after']=hashlib.sha256(p.read_bytes()).hexdigest();r['placement']='Riferimenti NTC integrati nell’apertura, prima degli obiettivi; testo conservato integralmente.'
q.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('NTC references moved into opening, no text removed')
