import json,re
from pathlib import Path

base=Path('wiki/books/moduli/m-sa01-sanita-amministrativa/chapters')
for num in ['04','06','09','10']:
 p=next(base.glob(num+'-*'));s=p.read_text(encoding='utf8')
 s=re.sub(r'(?m)^updated_at:.*$', 'updated_at: 2026-10-02',s)
 s=re.sub(r'(?m)^review_required:.*$', 'review_required: true',s)
 s=re.sub(r'(?m)^draft_stage:.*$', 'draft_stage: revision-in-progress',s)
 p.write_text(s,encoding='utf8')
src=Path('wiki/sources/procurement-farmaci-dispositivi-flussi-nsis.md')
s=src.read_text(encoding='utf8').replace('Per i dispositivi restano utilizzabili soltanto i passaggi generali di procurement e controllo interno; il delta settoriale richiede una fonte ufficiale valida ulteriore.','Per definizione e regime dei dispositivi si usa il raccordo MDR/IVDR aggiornato sotto; i claim sui relativi flussi NSIS restano esclusi finché non sostenuti da una fonte valida.')
s=re.sub(r'(?m)^updated_at:.*$','updated_at: 2026-10-02',s)
src.write_text(s,encoding='utf8')
descriptions={7:'Titolo e apertura raccordati a SSN, LEA, organi, accreditamento, atti e flussi; conservate integrazioni INT.',8:'Errori critici di riservatezza, accesso e competenza rendono insufficiente la risposta indipendentemente dal totale.',9:'Riscrittura completa con delega, sportello, portale e pratica esplicitamente fittizi.',10:'Variazione del costo medio corretta a −4,44% senza arrotondamenti intermedi, in entrambe le occorrenze.',11:'Documenti di bilancio, adozione, approvazione e consolidato; esempio risolto di ammortamento e contributo.',12:'AIC e classi A/H/C, raccordo MDR/IVDR, centralizzazione e NSO con esempio.',13:'FEFO, segregazione e catena del freddo; punto di riordino e caso risolti.'}
audit=json.loads(Path('artifacts/review-integrale-2026-10-02/VOL-07-ledger.json').read_text(encoding='utf8'))['findingsDetails']
batch={}
for n,desc in descriptions.items():
 f=next(x for x in audit if x['id']==f'V07-{n:02}')
 files=[f['path']]
 if n==11:files+=['wiki/sources/contabilita-budget-aziende-sanitarie.md']
 if n in (12,13):files+=[str(src).replace('\\','/')]
 batch[f['id']]={'change':desc,'files':files,'evidence':'Delta riletto e calcoli risolti; fonti ufficiali consolidate nelle source. Audit specialistico di modulo e PDF ancora pendenti.','status':'applicato'}
Path('artifacts/correzioni-collana-2026-10-02/VOL-07-batch02.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8')
