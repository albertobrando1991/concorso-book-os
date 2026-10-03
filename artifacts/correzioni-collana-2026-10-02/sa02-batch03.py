import json,re
from pathlib import Path

base=Path('wiki/books/moduli/m-sa02-professioni-sanitarie/chapters')
for num in ['03','04','05']:
 p=next(base.glob(num+'-*'));s=p.read_text(encoding='utf8')
 s=re.sub(r'(?m)^updated_at:.*$', 'updated_at: 2026-10-03',s)
 s=re.sub(r'(?m)^review_required:.*$', 'review_required: true',s)
 s=re.sub(r'(?m)^draft_stage:.*$', 'draft_stage: revision-in-progress',s)
 if num=='04':
  s=s.replace('### Obiettivi, interventi e indicatori\n\n### Diagnosi infermieristica','### Diagnosi infermieristica')
  s=s.replace('### Sicurezza del processo della terapia\n\n### Igiene delle mani','### Igiene delle mani')
 p.write_text(s,encoding='utf8')
sources=['sicurezza-cure-responsabilita-consenso-leggi-24-219','sicurezza-cure-ica-sorveglianza-epidemiologica-prevenzione','deterioramento-clinico-news2-sepsi-regioni','sicurezza-terapia-triage-assistenza-infermieristica-ministero']
for name in sources:
 p=Path('wiki/sources',name+'.md');s=p.read_text(encoding='utf8');s=re.sub(r'(?m)^updated_at:.*$', 'updated_at: 2026-10-03',s);p.write_text(s,encoding='utf8')
descriptions={14:'Uniformati gli imperativi in SA01/10 e SA02/05.',15:'Responsabilità civile/penale e assicurazione, limite temporaneo 2026, consenso/DAT/pianificazione/minori con casi risolti.',16:'Diagnosi infermieristica distinta da medica, scale, cinque momenti, precauzioni e prevenzione catetere; esempi e verifica.',17:'Scala 2 NEWS2 circoscritta a insufficienza respiratoria ipercapnica confermata e decisione documentata, non BPCO isolata.',18:'Esclusioni NEWS2 per minori di 16 anni e gravidanza, senza estensione dai contenuti ostetrici del capitolo.',19:'Cinque priorità nazionali di triage con tempi, rivalutazione e caso risolto; nuovo dato operativo tracciato.'}
audit=json.loads(Path('artifacts/review-integrale-2026-10-02/VOL-07-ledger.json').read_text(encoding='utf8'))['findingsDetails'];batch={}
for n,desc in descriptions.items():
 f=next(x for x in audit if x['id']==f'V07-{n:02}');files=[f['path']]
 if n==14: files += [str(next(base.glob('05-*'))).replace('\\','/')]
 else:files+=['wiki/sources/'+sources[{15:0,16:1,17:2,18:2,19:3}[n]]+'.md']
 batch[f['id']]={'change':desc,'files':files,'evidence':'Fonte primaria e passaggi pertinenti ricontrollati; casi risolti, limiti esplicitati. Step 15 e nuovo PDF ancora da concludere.','status':'applicato'}
Path('artifacts/correzioni-collana-2026-10-02/VOL-07-batch03.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8')
print('SA02 metadata e batch aggiornati.')
