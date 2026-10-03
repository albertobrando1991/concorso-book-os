from pathlib import Path
from urllib.parse import urlparse
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/books/moduli/m-fc04-giustizia/chapters/17-fonti-riferimenti-essenziali.md');t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest();links=[]
def sub(m):
 label,url=m[1],m[2];domain=urlparse(url).netloc.removeprefix('www.');links.append(dict(label=label,url=url,printDomain=domain));return label+' ('+domain+')'
t=re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)',sub,t)
t=t.replace('I collegamenti sono strumenti di verifica, mentre regole, esempi e soluzioni necessarie alle attività del volume sono spiegati nei capitoli.','Per consultarli, usa i siti indicati cercando titolo, numero e data del documento. Regole, esempi e soluzioni necessarie alle attività del volume sono spiegati nei capitoli.')
p.write_text(t,'utf-8');after=hashlib.sha256(p.read_bytes()).hexdigest()
(A/'VOL-04-bibliography-links.json').write_text(json.dumps(dict(chapter=p.as_posix(),before=before,after=after,links=links,reason='Bibliografia per stampa: titoli e domini leggibili; URL completi preservati nel registro e nelle source notes.'),ensure_ascii=False,indent=2),'utf-8')
for filename,key in [('M-FC04-freeze.json','files'),('VOL-04-text-verifica.json','chapters')]:
 f=A/filename;d=json.loads(f.read_text('utf-8'))
 for row in d[key]:
  if row['path']==p.as_posix():row['sha256']=after
 d['bibliographyPrintDelta']='VOL-04-bibliography-links.json';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
f=Path('wiki/reviews/pipeline/VOL-04/16-moduli-m-fc04-giustizia.md');f.write_text(f.read_text('utf-8').replace(before,after)+'\n\nBibliografia del capitolo17 resa leggibile in stampa: titoli e domini, con URL completi preservati in VOL-04-bibliography-links.json e source notes. Corretto URL non spezzabile fuori pagina nella prima prova. Nessuna variazione delle fonti normative.\n','utf-8')
print('Link convertiti:',len(links))
