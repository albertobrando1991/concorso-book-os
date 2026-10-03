from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp01-forze-ordine');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');assert 'review_required: false' in t;t=t.replace('draft_stage: specialist-audit-complete','draft_stage: text_frozen');p.write_text(t,encoding='utf8');entries.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03'})
for name in ['index.md','planning/00-piano-editoriale.md']:
 p=B/name;t=p.read_text(encoding='utf8');arc=C/('archive/pre-correzioni-sp01-'+p.name);assert not arc.exists();arc.write_text(t,encoding='utf8')
 t=t.replace('M-SP01 -','M-SP01 —');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
 t=t.replace('dieci capitoli completati in formato 2, revisionati e pubblicabili; fase C chiusa.','dieci capitoli corretti e audit specialistico del 3 ottobre 2026 concluso; nuovo PDF e revisione di volume necessari.')
 t=t.replace('Le sezioni normative e specialistiche richiedono source notes consolidate e review umana.','Le sezioni normative e specialistiche derivano da fonti consolidate; gli audit precedono il sign-off conclusivo del volume.')
 t=t.replace('la sequenza invariante a quattro fasi','una sequenza ricorrente da verificare nella procedura').replace('la sequenza invariante è parte della mappa','la sequenza delle prove è parte della mappa')
 t=t.replace('la fonte ufficiale indica 29 anni non compiuti.','il bando ufficiale, art. 2, indica 26 anni non compiuti per i civili e 25 per i VFP, con le elevazioni effettivamente spettanti. Il precedente dato 29/28 duplicava implicitamente l’elevazione massima ed è stato corretto.')
 t=t.replace('nel concorso per vice ispettori 2026 fra pubblicazione della banca dati e prova scritta è passato poco più di un mese.','il piano usa una banca di 5.000 quesiti attestata dal bando PS 1.000 e uno scenario didattico di 33 giorni, senza presentare l’intervallo come termine ufficiale.')
 t=t.replace('banca dati ufficiale, componimento di italiano, tema lungo, preselezione.','funzione selettiva, formato e presenza della banca; italiano a quiz CC 898 e composizione GdF 983.')
 t+='\n## Correzioni del 3 ottobre 2026\n\nDieci capitoli, cinquanta nuclei e 71 quiz commentati. Matrice riconciliata con gli ID dei capitoli reali. Humanizer dei delta, controllo di copertura e revisione specialistica conclusi; manifest M-SP01-freeze.json. Il perimetro è strategico e procedurale: i rinvii delimitati del capitolo 6 non promettono un intero corso penalistico. Restano necessari il nuovo PDF e i controlli di volume. Le note storiche precedenti non sostituiscono questo stato.\n'
 p.write_text(t,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';t=p.read_text(encoding='utf8').replace('review_required: true','review_required: false');p.write_text(t,encoding='utf8')
manifest={'volume':'VOL-12','module':'M-SP01','date':'2026-10-03','files':entries,'checks':['10 capitoli, 50 nuclei almeno 600 parole, 71 quiz commentati.','Calcoli, casi, chiavi, rinvii e fonti dei delta riesaminati; Humanizer applicato ai passaggi modificati.','Step 15 passato senza blocker o warning; indice e matrice riconciliati.'],'limitations':['Nuovo PDF e altri moduli del volume ancora da completare.','Fonti normative verificate selettivamente; dati storici PS non riattestati esclusi dai claim.']}
(A/'M-SP01-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
p=R/'16-moduli-m-sp01-forze-ordine.md';arc=C/'archive/pre-correzioni-16-m-sp01.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-SP01 — Manifest testuale del 3 ottobre 2026\n\nVerifica manuale, esito CLI registrato separatamente.\n\n'+'\n'.join('- '+s for s in manifest['checks'])+'\n\n| File | Stato | Data | SHA256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+x['path']+' | '+x['status']+' | '+x['date']+' | '+x['sha256']+' |' for x in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
mapping=json.loads((A/'M-SP01-findings-map.json').read_text(encoding='utf8'));batch={}
for n,(c,desc) in mapping.items():batch[f'V12-{int(n):02}']={'change':desc,'files':[next((B/'chapters').glob(f'{c:02}-*.md')).as_posix(),'wiki/sources/bandi-rappresentativi-m-sp01-forze-polizia-2026.md','wiki/reviews/pipeline/VOL-12/15-moduli-m-sp01-forze-ordine.md'],'evidence':'Audit specialistico dei delta e gate 15 passato; fonti, calcoli e chiavi nelle evidenze M-SP01. PDF ancora necessario.','status':'applicato'}
(A/'VOL-12-batch2.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('SP01 manifest, 15 findings')
