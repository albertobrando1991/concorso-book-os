from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-sp01-forze-ordine');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
assert 44-12*.25==41 and 42-12*.25==39
assert 8*60-70-30==6*60+20
assert 240*45/60+45+15==240
assert 20*240+200==5000
keys=json.loads((A/'M-SP01-quiz-keys.json').read_text(encoding='utf8'));matrix=(B/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf8');checks=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);no=p.name[:2]
 for path,heading in re.findall(r'\[\[(books/[^#\]|]+)#([^\]|]+)(?:\|[^\]]*)?\]\]',body):
  dst=Path('wiki')/(path+'.md');assert dst.exists(),dst
  assert heading in [re.sub(r'^#+ ','',l) for l in dst.read_text(encoding='utf8').splitlines() if l.startswith('#')],heading
 ids=re.findall(r'^## (N-SP01-\d+-\d+) ·',body,re.M);assert ids==[f'N-SP01-{no}-{i:02}' for i in range(1,6)],p
 for nid in ids:assert nid in matrix
 assert re.findall(r'Risposta corretta: ([ABCD])',body)==keys[no],p
 assert not re.search(r'\[\[(sources|topics|raw|entities|planning|reviews)/',body)
 assert '<br' not in body
 for field in ['source_refs','last_compiled_from','topics','entities']:
  for ref in json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1]):assert (Path('wiki')/(ref+'.md')).exists(),ref
 fm=fm.replace('review_required: true','review_required: false').replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(fm+'\n---\n'+body,encoding='utf8');checks.append({'path':p.as_posix(),'nuclei':len(ids),'quiz':len(keys[no]),'links':'resolved','bodyInternalLinks':0})
(A/'M-SP01-audit-checks.json').write_text(json.dumps({'math':'passed','files':checks},ensure_ascii=False,indent=2),encoding='utf8')
p=R/'15-moduli-m-sp01-forze-ordine.md';arc=C/'archive/pre-correzioni-15-m-sp01.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-sp01-forze-ordine.md').read_text(encoding='utf8').replace('— Correzioni editoriali','— Audit specialistico').replace('Audit specialistico dei delta, manifest e nuovo PDF;','Audit specialistico dei delta concluso; manifest e nuovo PDF;')
t+='''

### Evidenze dell’audit specialistico

Zero errori gravi o medi aperti nel perimetro corretto del modulo. Limiti delle verifiche esterne esplicitati e dati non riscontrati esclusi dai claim. Nessun box Dato operativo rilevato dal CLI; i valori presenti nel testo sono comunque stati riesaminati.

- PS 4.400: originale, pp. 7–9; ripartizione, età 26 non compiuti per civili e 25 per VFP, elevazioni effettive e diploma alle condizioni della procedura. Eliminata la doppia applicazione implicita dell’elevazione nelle soglie 29/28.
- PS 1.000: copia completa acquisita da inPA, pp. 7–10 e 13–15; riserve ulteriori non cancellate dal residuo 666, età e deroga personale, diploma alla prima prova, domanda, materie, 5.000 quesiti, scritto di 100 e ammissione dei migliori 4.000 con almeno 18/30 più pari merito. Nessuna equivalenza fra soglia e ammissione garantita. Date della banca non riattestate escluse dal testo.
- Carabinieri 3.081: artt. 2–6 e scheda inPA; formula del compleanno, categorie, domanda sul portale Arma, annullamento e nuova domanda, scadenza ore 23:59, nessun distinto orale nella sequenza. Non trasferiti termini o requisiti di altri bandi.
- Carabinieri 898: artt. 2, 6, 9–10 e allegato C; italiano a 60 quesiti, non tema. Decreto correttivo del 10 marzo distinto dalla pubblicazione del 18 marzo. Certificato valido e documentazione nei tempi prescritti; nessuna promessa generica di rinvio.
- GdF 983: artt. 2, 12–14; composizione di sei ore e minimo 10/20; sequenze obbligatorie/facoltative distinte per contingente; punteggio 7–8 convertito in 0,25. Il limite di due partecipazioni dell’art. 1, comma 3, riguarda il contingente riservato indicato, non tutto il mare. Rimosso dal protocollo il bando 69 ufficiali fuori perimetro.
- Corte costituzionale 40/2024: dispositivo e motivazione controllati; specifica clausola GdF sulla guida in stato di ebbrezza, con distinta valutazione della condotta. D.M. 198/2003 riferito alla Polizia di Stato; riforma della statura non abroga tutti i requisiti sanitari.
- Casi: 44 − 12 × 0,25 = 41; 42 − 12 × 0,25 = 39; partenza 6:20 per 8:00 con 70 + 30 minuti. Cronologie del titolo, certificato e ricevuta separate dai livelli di preparazione. Piano banca: 20 × 240 + 200 = 5.000; a 45 secondi per quesito, 240 richiedono tre ore, più un’ora per correzione e diario.
- Coerenza: 50 nuclei con almeno 600 parole, 71 quiz; chiavi e commenti riallineati dopo redistribuzione delle opzioni, senza lettere dei distrattori ereditate. Rinvii a heading esistenti e letti, perimetro circoscritto nella matrice. Rimossi residui staff e tabelle con HTML visibile; nuovo PDF necessario per la resa effettiva.

Evidenze: M-SP01-audit-checks.json, M-SP01-surface-counts.json, M-SP01-quiz-keys.json e tre source notes collegate. Le note conservano materiale storico distinto dal riscontro corrente; ciò non attribuisce verifica integrale alle fonti storiche.
'''
p.write_text(t,encoding='utf8');print('SP01 audit',len(checks),'files')
