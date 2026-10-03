from pathlib import Path
import re,json,hashlib
A=Path(__file__).parent;root=A.parent.parent;changes=[]
def edit(module,filename,replacements,volume):
 p=root/'wiki/books/moduli'/module/'chapters'/filename;s=p.read_text(encoding='utf8');before=hashlib.sha256(p.read_bytes()).hexdigest()
 for old,new in replacements.items():
  assert old in s,(p,old);s=s.replace(old,new)
 p.write_text(s,encoding='utf8',newline='\n');changes.append({'volume':volume,'module':module[:6].upper(),'path':p.relative_to(root).as_posix(),'beforeSHA256':before,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'change':'Rinvii locali sostituiti da titoli canonici per rendere univoca la consultazione del volume e del modulo.'})
edit('m-ir02-universita-afam','12-laboratorio-quattro-profili.md',{'Fonti dei capitoli 02–11.':'Fonti dei capitoli precedenti del modulo Università e AFAM.'},'VOL-06')
edit('m-ir03-enti-ricerca','12-laboratorio-quattro-profili.md',{'capitolo 8:':'capitolo «Tecnologo, laboratori e infrastrutture»:'},'VOL-06')
edit('m-ir04-cultura-beni-culturali','01-mic-quattro-profili.md',{'capitolo 7,':'capitolo «Archivistica e archivi»,','capitolo 5':'capitolo «Procedimenti, vincoli e circolazione»','capitolo 2.':'capitolo «Organizzazione centrale e periferica».'},'VOL-06')
edit('m-sa01-sanita-amministrativa','06-front-office-comunicazione-utenza.md',{'modulo M-SA02, capitolo 10.':'modulo M-SA02, capitolo «Prova pratica e casi professionali».'},'VOL-07')
edit('m-sa01-sanita-amministrativa','10-procurement-farmaci-dispositivi-magazzino.md',{'modulo M-SA04, capitolo 4 — Tecnologie, dispositivi, apparecchiature e rischio':'modulo M-SA04, capitolo «Tecnologie, dispositivi, apparecchiature e rischio tecnologico»'},'VOL-07')
edit('m-sa02-professioni-sanitarie','03-discipline-professionali-autonomia-responsabilita.md',{'capitolo 6 — Prevenzione, continuità e presa in carico':'capitolo «Prevenzione, continuità assistenziale e presa in carico»'},'VOL-07')
module='m-sp02-vigili-fuoco';d=root/'wiki/books/moduli'/module/'chapters';titles={int(p.name[:2]):re.search(r'^title: (.*)$',p.read_text(encoding='utf8'),re.M)[1].strip('\"\'') for p in d.glob('*.md')}
for p in d.glob('*.md'):
 s=p.read_text(encoding='utf8');fm,body=s.split('\n---\n',1);replacements={m[0]:'capitolo «'+titles[int(m[1])]+'»' for m in re.finditer(r'capitolo ([2-6])\b',body)}
 if replacements:edit(module,p.name,replacements,'VOL-12')
edit('m-sp04-prefettizia-diplomatica','01-mappa-scelta-bando-decoder.md',{'capitolo 3,':'capitolo «Carriera diplomatica: prove, materie e ordinamento»,'},'VOL-12')
for module in sorted({r['module'] for r in changes}):
 p=A/(module+'-freeze.json');data=json.loads(p.read_text(encoding='utf8'));controlled=data.setdefault('controlledPrintCorrections',{'date':'2026-10-03','files':[]});controlled.setdefault('referenceCorrections',[]).extend(r for r in changes if r['module']==module);controlled['referenceVerification']='Destinazioni riscontrate nei titoli canonici; nuova prova PDF necessaria.';p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
(A/'VOL-06-07-12-production-reference-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(changes,ensure_ascii=False))
