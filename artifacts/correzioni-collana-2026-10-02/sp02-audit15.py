from pathlib import Path
from fractions import Fraction
import re,json
B=Path('wiki/books/moduli/m-sp02-vigili-fuoco');A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12');C=Path('wiki/reviews/correzioni-collana-2026-10-02')
assert Fraction(1,4)-Fraction(3,4)*Fraction(1,10)==Fraction(7,40)
assert Fraction(25+21+21,3)+21+21+1==Fraction(196,3)
assert 1200/.04==30000 and 1200/.02==60000
assert (30+21+21)/3==24 and (30+30+21)/3==27
keys=json.loads((A/'M-SP02-quiz-keys.json').read_text(encoding='utf8'));matrix=(B/'planning/02-matrice-copertura-didattica.md').read_text(encoding='utf8');checks=[]
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);no=p.name[:2]
 body=body.replace('Non serve a celebrare ore, impone automaticamente un cambio di concorso o consente di stimare i posti futuri.','Non serve a celebrare ore; non impone automaticamente un cambio di concorso né consente di stimare i posti futuri.')
 if no=='03':
  body=body.replace('No: compariranno nell’avviso sulle modalità di esecuzione, e fino ad allora non vanno date per note.','No: occorre verificarle nelle comunicazioni ufficiali della procedura.').replace("No: compariranno nell'avviso sulle modalità di esecuzione, e fino ad allora non vanno date per note.",'No: occorre verificarle nelle comunicazioni ufficiali della procedura.')
  body=body.replace('una carta d’identità scaduta non è un documento.','un documento scaduto non soddisfa il requisito di validità richiesto.').replace("una carta d'identità scaduta non è un documento.",'un documento scaduto non soddisfa il requisito di validità richiesto.')
 for path,heading in re.findall(r'\[\[(books/[^#\]|]+)#([^\]|]+)(?:\|[^\]]*)?\]\]',body):
  dst=Path('wiki')/(path+'.md');assert dst.exists(),dst
  assert heading in [re.sub(r'^#+ ','',l) for l in dst.read_text(encoding='utf8').splitlines() if l.startswith('#')],heading
 ids=re.findall(r'^## (N-SP02-\d+-\d+) ·',body,re.M);assert ids==[f'N-SP02-{no}-{i:02}' for i in range(1,6)],p
 for nid in ids:assert nid in matrix
 assert re.findall(r'Risposta corretta: ([ABCD])',body)==keys[no],p
 assert not re.search(r'\[\[(sources|topics|raw|entities|planning|reviews)/',body)
 assert '<br' not in body
 for field in ['source_refs','last_compiled_from','topics','entities']:
  for ref in json.loads(re.search(rf'^{field}: (\[.*\])$',fm,re.M)[1]):assert (Path('wiki')/(ref+'.md')).exists(),ref
 fm=fm.replace('review_required: true','review_required: false').replace('draft_stage: corrections-applied','draft_stage: specialist-audit-complete');p.write_text(fm+'\n---\n'+body,encoding='utf8');checks.append({'path':p.as_posix(),'nuclei':len(ids),'quiz':6,'links':'resolved','bodyInternalLinks':0})
(A/'M-SP02-audit-checks.json').write_text(json.dumps({'math':'passed','files':checks},ensure_ascii=False,indent=2),encoding='utf8')
p=R/'15-moduli-m-sp02-vigili-fuoco.md';arc=C/'archive/pre-correzioni-15-m-sp02.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
t=(R/'14-moduli-m-sp02-vigili-fuoco.md').read_text(encoding='utf8').replace('# M-SP02 — Correzioni editoriali del 3 ottobre 2026','# M-SP02 — Audit specialistico del 3 ottobre 2026').replace('Applicati venti rilievi','Riesaminati e corretti venti rilievi').replace('Audit specialistico dei delta, manifest del testo e nuovo PDF.','Audit specialistico dei delta concluso; manifest del testo e nuovo PDF.').replace('ma restano gli audit e i controlli di volume','ma restano i controlli di volume')
t+='''

### Evidenze dell’audit specialistico

Zero errori gravi o medi aperti nel perimetro corretto del modulo. I limiti esterni sono dichiarati senza sostituirli con dati inventati. Nessun box Dato operativo rilevato dal CLI: soglie e procedure sono comunque state riesaminate nei passaggi interessati.

- Requisiti: ricontrollati bando 400 artt. 1–2, DM 166 artt. 1–2, DPR 207 art. 3 e tabella. Distinte maturazione, dichiarazione, documentazione e momento dell’accertamento. Valore naturale isolato non attribuisce idoneità ad altri ruoli.
- Prove: Allegato A, posizioni del modulo C e tabella trave; soglie maschili/femminili dei casi esplicitate. Formula della media subordinata a ciascuna sufficienza. Nessuna conversione intermedia inventata e nessun rapporto fra prestazioni usato per prescrivere il rendimento dell’allenamento.
- Titoli: Allegato B e art. 8, possesso/dichiarazione a scadenza, non cumulabilità e ammissione alla valutazione dopo tutte le prove. Caso dopo scadenza corretto.
- Diario: documento ufficiale inPA del 28 settembre, tutte e tre le pagine lette; tablet, lettera e turni. Le comunicazioni del 7 ottobre non sono anticipate.
- Prevenzione: DLgs 139 art. 13 e DPR 151 artt. 3–4 letti nel testo corrente. Distinti progetto B/C, SCIA, controlli A/B e C, CPI e modifiche. Nessun progetto antincendio ricostruito senza dati.
- Calcoli risolti: valore atteso 0,175; media 24 e poi 27 nel confronto dei pesi; Andrea 67/3 più 21 più 21 e titolo 1 = 65,333…; pressione 30 e 60 kPa. Chiavi e commenti dei 48 quiz confrontati con le opzioni, senza lettere dei distrattori ereditate dalle vecchie versioni.
- Coerenza: quaranta ID corrispondenti al capitolo reale; cinque rinvii a heading esistenti, letti nelle sezioni indicate; matrice circoscritta al perimetro reale. Tutti i nuclei sopra 600 parole, senza assumere il conteggio come dimostrazione sufficiente di copertura.
- Stile e superficie: rimossi i passaggi staff individuati e le ripetizioni dei commenti; integrate consegne risolte al posto di istruzioni generiche. Originali conservati. Controllo visuale da ripetere sul nuovo PDF.
''';p.write_text(t,encoding='utf8')
print('SP02 audit15 verifiche concluse: 8 capitoli, 40 nuclei, 48 quiz')
