from pathlib import Path
import re,json
module=Path('wiki/books/moduli/m-fl02-regioni-province-citta-metropolitane')
p=module/'chapters/03-funzioni-regionali-rapporti-stato-enti-locali.md';t=p.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,count=1,flags=re.M)
for key,entry in [('source_refs','sources/vol-02-regioni-statuti-competenze-verifica-2026-10-03.md'),('topics','topics/vol-02-statuti-organi-regionali-casi.md')]:
 t=re.sub(r'^'+key+r': \[(.*)\]$',lambda m:key+': ['+m[1]+', "'+entry+'"]',t,count=1,flags=re.M)
p.write_text(t,encoding='utf8')
statepath=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');state=json.loads(statepath.read_text(encoding='utf8'))
state['changes']['V02-22']={'files':[str(p).replace('\\','/')],'change':'Esemplificato art117; presupposti/soggetto120 e procedimento8L131; completata Stato-città e composizione delle tre conferenze, distinta da conferenza di servizi.','evidence':'L131art8 e D281art8/9 scaricati e letti integralmente; PDFQuirinale117/120, sitoPCMcomposizione, Corte210/2024 e76/2009. Casi salute/reato e tutela/valorizzazione risolti.','status':'Applicato; audit specialistico M-FL02 ancora aperto'}
statepath.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
manifest=Path('artifacts/correzioni-collana-2026-10-02/normattiva-fl02/manifest.json');rows=json.loads(manifest.read_text(encoding='utf8'))
for x in rows:
 if x['name'] in ['l131-art8','d281-art8','d281-art9']:x['readComplete']=True
manifest.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
matrix=module/'planning/02-matrice-copertura-didattica.md';t=matrix.read_text(encoding='utf8').replace('review_required: false','review_required: true',1)
t+='\n## Correzioni autorizzate, 3 ottobre 2026\n\n| ID | Capitolo/nucleo | Teoria e applicazione aggiunte | Verifica | Stato |\n| --- | --- | --- | --- | --- |\n| V02-21 | 02, nuclei01/03 | Statuto123, elezione122, cessazione126; casi31componenti e sfiducia | Due quiz aggiuntivi7C/8D e soluzioni | Applicato, audit15 aperto |\n| V02-22 | 03, nuclei02/04/06 | Materie117 esemplificate, conferenze, sostituzione120/L131 | Confronti salute/reato, tutela/valorizzazione e caso LEP | Applicato, audit15 aperto |\n'
matrix.write_text(t,encoding='utf8')
print('V02-22 registrato; fonti lette e matrice aggiornate')
