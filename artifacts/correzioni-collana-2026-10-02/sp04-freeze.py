from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02');entries=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');assert 'review_required: false' in t;t=t.replace('draft_stage: specialist-audit-complete','draft_stage: text_frozen');p.write_text(t,encoding='utf8');entries.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'status':'text-freeze','date':'2026-10-03'})
for name in ['index.md','planning/00-piano-editoriale.md']:
 p=B/name;t=p.read_text(encoding='utf8');arc=C/('archive/pre-correzioni-sp04-'+p.name);assert not arc.exists() or arc.read_text(encoding='utf8')==t;arc.write_text(t,encoding='utf8');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
 if name=='index.md':
  t=t.replace('due carriere ad accesso diretto in qualifica dirigenziale','due carriere speciali con accesso alle rispettive qualifiche iniziali')
  t=re.sub(r'- Stato:.*','- Stato: sette capitoli corretti e audit specialistico del 3 ottobre 2026 concluso; nuovo PDF e revisione di volume necessari.',t)
  t=t.replace('Le sezioni normative e specialistiche richiedono source notes consolidate e review umana.','Le sezioni normative e specialistiche derivano da fonti consolidate, con riscontri selettivi e limiti temporali dichiarati.')
  t=t.replace('La matrice contiene 37 nuclei completi; i due accorpamenti rispetto ai nove titoli nominali sono motivati nel piano editoriale.','La matrice contiene 37 nuclei nel perimetro di orientamento, requisiti, prove e metodo; non dichiara coperto l’intero programma teorico delle materie.')
  s=t.find('## Un pattern che attraversa il volume');t=(t[:s] if s>=0 else t)+'''\n## Riuso del metodo della banca dati

Il protocollo del volume base si applica soltanto a una raccolta ufficiale effettivamente pubblicata e identificata per versione. L’annuncio non certifica che il file sia disponibile. Stato della pubblicazione, rettifiche e calendario vanno controllati sul portale della procedura.

Fonte specialistica: [[sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04]]. Sintesi: [[topics/m-sp04-prefettizia-diplomatica-prove]]. Audit: [[reviews/pipeline/VOL-12/15-moduli-m-sp04-prefettizia-diplomatica]].
'''
  t=t.replace('\n.\n','\n')
 else:
  fm=t.split('\n---\n',1)[0].replace('review_required: true','review_required: false');fm=re.sub(r'^draft_stage:.*$','draft_stage: text_frozen',fm,flags=re.M)
  t=fm+'''\n---

# Piano editoriale — M-SP04

## Obiettivo e confini

Orientamento e metodo per prefettizia e diplomatica, con requisiti, prove, ordinamento essenziale e applicazioni. Non sostituisce i programmi completi di diritto, storia, economia o corsi di lingua. Le tornate di riferimento sono prefettizia 2025 e diplomatica 2026: il riuso richiede confronto con il nuovo bando.

## Struttura effettiva

1. Mappa, scelta del binario e Bando Decoder.
2. Carriera prefettizia: prove, materie e ordinamento.
3. Carriera diplomatica: prove, materie e ordinamento.
4. Lingue straniere: diagnosi, scelta, laboratorio e manutenzione.
5. Orale e postura professionale, dossier e prova informatica.
6. Piano di preparazione: settimane da 12/20 ore e orizzonte condizionato.
7. Errori, casi e checklist.

Sette capitoli, 37 nuclei e 43 quiz. Cinque nuclei per capitolo, sette per il capitolo 3; numerazione coerente con i file e la matrice. Gli accorpamenti storici sono documentati negli snapshot interni, senza note di produzione nel libro.

## Correzioni e verifiche

Applicati V12-48–62 e quota SP04 dei rilievi trasversali V12-63–66. Aggiunta la correzione della scadenza diplomatica al 27 aprile 2026 ore 12. Fonti, calcoli, casi e chiavi verificati nel perimetro dichiarato; linguaggio e ripetizioni riesaminati sui delta.

Fonte: [[sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04]]. Topic: [[topics/m-sp04-prefettizia-diplomatica-prove]]. Matrice: [[books/moduli/m-sp04-prefettizia-diplomatica/planning/02-matrice-copertura-didattica]]. Audit: [[reviews/pipeline/VOL-12/15-moduli-m-sp04-prefettizia-diplomatica]].

## Stato

Audit specialistico del 3 ottobre 2026 concluso senza errori gravi o medi aperti nel perimetro corretto; gate 15 passato senza blocker o warning. Riscontri normativi selettivi, non certificazione dell’intero ordinamento. Nuovo PDF e gate di volume necessari; il freeze testuale non attesta pubblicabilità.
'''
 p.write_text(t,encoding='utf8')
manifest={'volume':'VOL-12','module':'M-SP04','date':'2026-10-03','files':entries,'checks':['7 capitoli, 37 nuclei almeno 600 parole, 43 quiz commentati.','Bandi, casi, cronologie, calcoli e chiavi riesaminati; Humanizer dei delta completato.','Indice e matrice riconciliati; step 15 passato senza blocker o warning.'],'limitations':['Nuovo PDF e revisione di volume necessari.','Riscontri normativi selettivi nelle source notes; non certificazione dell’intero programma.']}
(A/'M-SP04-freeze.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8');p=R/'16-moduli-m-sp04-prefettizia-diplomatica.md';arc=C/'archive/pre-correzioni-16-m-sp04.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text('# M-SP04 — Manifest testuale del 3 ottobre 2026\n\nVerifica manuale del gate non implementato; esito CLI registrato separatamente.\n\n'+'\n'.join('- '+s for s in manifest['checks'])+'\n\n| File | Stato | Data | SHA256 |\n| --- | --- | --- | --- |\n'+'\n'.join('| '+x['path']+' | '+x['status']+' | '+x['date']+' | '+x['sha256']+' |' for x in entries)+'\n\n'+' '.join(manifest['limitations'])+'\n',encoding='utf8')
mapping=json.loads((A/'M-SP04-findings-map.json').read_text(encoding='utf8'));batch={}
for n,(c,desc) in mapping.items():
 files=[next((B/'chapters').glob(f'{c:02}-*.md')).as_posix(),'wiki/sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04.md','wiki/reviews/pipeline/VOL-12/15-moduli-m-sp04-prefettizia-diplomatica.md']
 if int(n)>=63:files+=['wiki/reviews/pipeline/VOL-12/15-moduli-'+x+'.md' for x in ['m-sp01-forze-ordine','m-sp02-vigili-fuoco','m-sp03-magistratura-avvocatura-notariato']]
 batch[f'V12-{int(n):02}']={'change':desc,'files':files,'evidence':'Audit specialistici dei quattro moduli e gate 15 passati; evidenze di fonti, calcoli e chiavi nei manifest. Nuovo PDF ancora necessario.','status':'applicato'}
(A/'VOL-12-batch4.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('SP04 manifest, 19 findings')
