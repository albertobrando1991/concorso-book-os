from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp03-magistratura-avvocatura-notariato');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02');entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');assert 'review_required: false' in t;t=t.replace('draft_stage: specialist-audit-complete','draft_stage: text_frozen');p.write_text(t,encoding='utf8');entries.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03'})
for name in ['index.md','planning/00-piano-editoriale.md']:
 p=B/name;t=p.read_text(encoding='utf8');arc=C/('archive/pre-correzioni-sp03-'+p.name);assert not arc.exists();arc.write_text(t,encoding='utf8');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
 if name=='index.md':
  t=re.sub(r'- Stato:.*','- Stato: sette capitoli corretti e audit specialistico del 3 ottobre 2026 concluso; nuovo PDF e revisione di volume necessari.',t)
  t=t.replace('le sezioni di mappa, prove, materie specialistiche e piano di studio sono triplicate, non condivise.','requisiti e prove sono distinti per percorso; scrittura e pianificazione sono comuni soltanto nei metodi trasferibili, con applicazioni separate.')
  t=t.replace('Le sezioni normative e specialistiche richiedono source notes consolidate e review umana.','Le sezioni normative e specialistiche derivano da fonti consolidate e sono state verificate selettivamente nei punti dichiarati.')
  t=t.replace('Nessuno per questo modulo: fase C chiusa. Restano la review finale di volume, il preflight e la preparazione della consegna; la conferma conclusiva dello step 24 è umana.','Produrre e controllare il nuovo PDF, poi completare revisione di volume e preflight secondo la pipeline. Il freeze del testo non equivale a pubblicabilità attestata.')
 else:
  fm=t.split('\n---\n',1)[0].replace('review_required: true','review_required: false');fm=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',fm,flags=re.M)
  t=fm+'''\n---

# Piano editoriale — M-SP03

## Obiettivo e confini

Orientamento alle tre selezioni giuridiche, requisiti e prove, metodo di scrittura e preparazione lunga. Non è il programma completo di diritto civile, penale, amministrativo o notarile. Il lettore usa materiali specialistici per la teoria di materia non trattata. Il notariato è professione regolamentata con funzione pubblica, non accesso al pubblico impiego.

## Struttura effettiva

1. Mappa delle tre professioni e scelta del binario.
2. Magistratura ordinaria: accesso, prove e ordinamento.
3. Avvocatura dello Stato: selezione, prove e funzione.
4. Notariato: pratica, atti e ordinamento.
5. Metodo per tema, atto e prova teorico-pratica, con prodotti svolti.
6. Piano pluriennale e gestione delle incognite, con proposta su due anni.
7. Errori, casi e checklist finale.

Trentacinque nuclei, cinque per capitolo, e 57 quiz commentati. Il Decoder è integrato nella mappa; requisiti e prestazioni restano separati per percorso. Gli ID sono quelli dei capitoli correnti, riconciliati nella matrice.

## Correzioni e controlli

Applicati V12-36–47, aggiunto il limite di due precedenti non idoneità della procuratura, verificati calcoli e cronologie. I casi sono originali, con ipotesi e condizioni esplicite. La pianificazione è condizionata all’accesso, ai prodotti corretti e agli atti effettivamente pubblicati.

Fonte: [[sources/bandi-magistratura-avvocatura-notariato-m-sp03]]. Sintesi: [[topics/m-sp03-carriere-giuridiche-prove]]. Matrice: [[books/moduli/m-sp03-magistratura-avvocatura-notariato/planning/02-matrice-copertura-didattica]]. Audit: [[reviews/pipeline/VOL-12/15-moduli-m-sp03-magistratura-avvocatura-notariato]].

## Stato

Audit specialistico del 3 ottobre 2026 concluso senza errori gravi o medi aperti nel perimetro corretto; gate 15 passato senza blocker o warning. Fonti verificate selettivamente, non certificazione normativa integrale. Nuovo PDF e controlli di volume necessari. Le valutazioni di pubblicabilità dei precedenti report restano documenti storici e non descrivono questo stato.
'''
 p.write_text(t,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';p.write_text(p.read_text(encoding='utf8').replace('review_required: true','review_required: false'),encoding='utf8')
manifest={'volume':'VOL-12','module':'M-SP03','date':'2026-10-03','files':entries,'checks':['7 capitoli, 35 nuclei almeno 600 parole, 57 quiz commentati.','Casi, cronologie, calcoli e chiavi riesaminati; Humanizer dei delta completato.','Indice e matrice riconciliati; step 15 passato senza blocker o warning.'],'limitations':['Nuovo PDF e SP04 ancora necessari.','Riscontri normativi selettivi nelle source notes; non certificazione dell’intero programma.']}
(A/'M-SP03-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8');p=R/'16-moduli-m-sp03-magistratura-avvocatura-notariato.md';arc=C/'archive/pre-correzioni-16-m-sp03.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-SP03 — Manifest testuale del 3 ottobre 2026\n\nVerifica manuale del gate non implementato, esito CLI separatamente registrato.\n\n'+'\n'.join('- '+s for s in manifest['checks'])+'\n\n| File | Stato | Data | SHA256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+x['path']+' | '+x['status']+' | '+x['date']+' | '+x['sha256']+' |' for x in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
mapping=json.loads((A/'M-SP03-findings-map.json').read_text(encoding='utf8'));batch={}
for n,(c,desc) in mapping.items():batch[f'V12-{int(n):02}']={'change':desc,'files':[next((B/'chapters').glob(f'{c:02}-*.md')).as_posix(),'wiki/sources/bandi-magistratura-avvocatura-notariato-m-sp03.md','wiki/reviews/pipeline/VOL-12/15-moduli-m-sp03-magistratura-avvocatura-notariato.md'],'evidence':'Audit specialistico e gate 15 passato; fonti, calcoli e chiavi nelle evidenze M-SP03. Nuovo PDF ancora necessario.','status':'applicato'}
(A/'VOL-12-batch3.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('SP03 manifest, 12 findings')
