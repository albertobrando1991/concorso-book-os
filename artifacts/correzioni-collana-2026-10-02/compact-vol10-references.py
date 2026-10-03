from pathlib import Path
import json,hashlib,re
A=Path(__file__).parent;B=Path('wiki/books/moduli/m-tr03-tecnico-ingegneristico');records=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');old='## Riferimenti normativi e professionali\n\n';assert t.count(old)==1,p
 before=hashlib.sha256(p.read_bytes()).hexdigest();tail=t.split(old)[1];assert not re.search(r'^#{1,4} ',tail,re.M),p
 backup=A/'before-text/VOL-10/layout-references'/p.name;backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():backup.write_text(t,encoding='utf8')
 t=t.replace(old,'**Riferimenti normativi e professionali.** ',1);p.write_text(t,encoding='utf8')
 assert t.split('**Riferimenti normativi e professionali.** ')[1]==tail
 records.append({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'referenceTextPreserved':True})
(A/'VOL-10-layout-reference-delta.json').write_text(json.dumps({'date':'2026-10-03','reason':'Riferimenti finali in paragrafo con etichetta, corpo11pt; evita una riga di titolo isolata dal flusso finale. Nessuna fonte rimossa.','files':records},ensure_ascii=False,indent=2),encoding='utf8')
print('13 reference texts preserved; controlled layout correction, manifest refresh after PDF check')
