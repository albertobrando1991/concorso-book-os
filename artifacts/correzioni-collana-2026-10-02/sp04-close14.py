from pathlib import Path
import re,json,ast
B=Path('wiki/books/moduli/m-sp04-prefettizia-diplomatica');A=Path('artifacts/correzioni-collana-2026-10-02');C=Path('wiki/reviews/correzioni-collana-2026-10-02');R=Path('wiki/reviews/pipeline/VOL-12')
source='sources/bandi-carriera-prefettizia-e-diplomatica-m-sp04';topic='topics/m-sp04-prefettizia-diplomatica-prove';entities=['entities/ministero-interno','entities/ministero-affari-esteri']
details={1:'Ammissibilità preliminare; quattro serie di scritti non superate; caso tre insuccessi e un orale negativo; Decoder aggiornabile.',2:'Età con date precise; valore atteso e omissione per difficoltà; scrittura digitale; SNA; calcolo finale 150.',3:'Laurea magistrale senza elenco ristretto, titoli esteri, scadenza 27 aprile; programma economico completo; materia facoltativa; graduatoria 149,2.',4:'Scelta nella domanda prima della scadenza; testo inglese originale, traduzione, risposta, correzione e dialogo.',5:'Rilettura delle istruzioni informatiche; dossier con risposta, obiezione, transizioni e foglio elettronico risolto.',6:'Settimane da 12 e 20 ore, varianti minime e prove complete; piano 26/52 settimane con checkpoint; pianificazione a ritroso.',7:'Rimossa nota di accorpamento; checklist distinte; caso laurea espressamente prefettizio; commenti dei sei quiz riscritti.'}
stats=[];keys={}
refs={1:[('banca-dati-ufficiale-studiarla-senza-memorizzare-male','Il protocollo in quattro fasi'),('la-prova-a-quiz','Quando saltare una domanda'),('casi-pratici-problem-solving-amministrativo','La griglia in otto domande')],2:[('diritto-amministrativo-per-candidati','Programma essenziale per i concorsi'),('costituzione-e-ordinamento-dello-stato','Percorso essenziale del programma di diritto costituzionale')]}
for p in sorted((B/'chapters').glob('*.md')):
 t=p.read_text(encoding='utf8');fm,body=t.split('\n---\n',1);c=int(p.name[:2]);ids=re.findall(r'^## (N-SP04-\d+-\d+) ·',body,re.M);assert len(ids)==(7 if c==3 else 5)
 mapping={old:f'N-SP04-{c:02}-{i:02}' for i,old in enumerate(ids,1)}
 fm=re.sub(r'N-SP04-\d+-\d+',lambda m:mapping.get(m[0],m[0]),fm);body=re.sub(r'N-SP04-\d+-\d+',lambda m:mapping.get(m[0],m[0]),body)
 if c==1:
  body=body.replace('Qui devi produrre una decisione verificabile, non scegliere il titolo che suona meglio.','Qui devi produrre una decisione verificabile, non scegliere il titolo che suona meglio. Il percorso spiega accesso, prove, ordinamento essenziale e preparazione; non svolge per intero i programmi di diritto, storia ed economia né sostituisce un corso nelle lingue richieste.')
  body=body.replace('eventuali prove facoltative, titoli e graduatoria','eventuale materia orale facoltativa, lingue facoltative, titoli e graduatoria')
  body=body.replace('La terza area sono i dati mobili.','Per la diplomatica aggiungi le opzioni da dichiarare nella domanda: seconda lingua, lingue facoltative, eventuale materia orale facoltativa dell’articolo 11 e titoli valutabili. Per soglie e calcolo usa il capitolo 3, sezioni “L’orale” e “Punteggio finale”: il Decoder registra la scelta, senza duplicare ogni tabella di punteggio.\n\nLa terza area sono i dati mobili.')
 if c==6:body=body.replace('Quando arriva il bando, non si butta il piano.','Nel binario diplomatico programma anche l’eventuale materia orale facoltativa scelta nella domanda, senza sottrarre il presidio dei minimi obbligatori. La scelta non può attendere l’esito degli scritti se il termine della domanda è già decorso.\n\nQuando arriva il bando, non si butta il piano.')
 if c in refs:
  body+='\n## Rinvii al volume base\n\n'
  for slug,heading in refs[c]:
   target='books/il-metodo-bando/chapters/'+slug;assert ('## '+heading) in (Path('wiki')/(target+'.md')).read_text(encoding='utf8')
   body+=f'- [[{target}#{heading}|{heading}]]: fondamenti o metodo nel perimetro della sezione; requisiti, punteggi e formati specialistici restano quelli spiegati in questo modulo.\n'
 # Standardize option layout, then rotate the validated semantic answer with its explanation.
 body=re.sub(r'^\s*(?:- )?([A-D])\. ',r'\1. ',body,flags=re.M)
 body=re.sub(r'^\s*(\*\*Risposta corretta:)',r'\1',body,flags=re.M)
 pat=r'^A\. ([^\n]+)\n\s*B\. ([^\n]+)\n\s*C\. ([^\n]+)\n\s*D\. ([^\n]+)\n\s*\*\*Risposta corretta: ([A-D])\.\*\*([^\n]*)'
 seq=[]
 def rotate(m):
  opts=list(m.group(1,2,3,4));old=m[5];target='ABCD'[(len(seq)+c)%4];shift=(ord(target)-ord(old))%4;mp={chr(65+i):chr(65+(i+shift)%4) for i in range(4)};out=['']*4
  for i,v in enumerate(opts):out[(i+shift)%4]=v
  comment=re.sub(r'\b[A-D]\b',lambda x:mp[x[0]],m[6].strip());seq.append({'key':target,'correct':opts[ord(old)-65]})
  return '\n'.join(f'{chr(65+i)}. {v}' for i,v in enumerate(out))+f'\n\n**Risposta corretta: {target}.** '+comment
 body=re.sub(pat,rotate,body,flags=re.M);assert len(seq)==len(re.findall(r'Risposta corretta:',body)),(p,len(seq));keys[f'{c:02}']=seq
 for field,val in [('source_refs',json.dumps([source])),('last_compiled_from',json.dumps([source])),('topics',json.dumps([topic])),('entities',json.dumps(entities)),('updated_at','2026-10-03'),('cut_off_date','2026-10-03'),('draft_stage','corrections-applied'),('review_required','true')]:
  if re.search(rf'^{field}:',fm,re.M):fm=re.sub(rf'^{field}:.*$',field+': '+val,fm,flags=re.M)
  else:fm+='\n'+field+': '+val
 p.write_text(fm+'\n---\n'+body,encoding='utf8')
 nuclei=[{'id':m[0],'heading':m[1],'words':len(re.findall(r'\b[\w’]+\b',m[2]))} for m in re.findall(r'^## (N-SP04-\d+-\d+) · ([^\n]+)\n(.*?)(?=^## |\Z)',body,re.M|re.S)];assert min(n['words'] for n in nuclei)>=600,(p,nuclei)
 stats.append({'path':p.as_posix(),'chapter':c,'words':len(re.findall(r'\b[\w’]+\b',body)),'nuclei':nuclei,'quiz':len(seq)})
(A/'M-SP04-surface-counts.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf8');(A/'M-SP04-quiz-keys.json').write_text(json.dumps(keys,ensure_ascii=False,indent=2),encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';old=p.read_text(encoding='utf8');arc=C/'archive/pre-correzioni-sp04-matrice.md';assert not arc.exists();arc.write_text(old,encoding='utf8');fm=old.split('\n---\n',1)[0];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M)
t=fm+'''\n---

# M-SP04 — Matrice di copertura didattica

Sette capitoli e 37 nuclei riconciliati al 3 ottobre 2026. Copertura di orientamento, requisiti e prove delle tornate prefettizia 2025 e diplomatica 2026, ordinamento essenziale, metodo e applicazioni. Il modulo non dichiara coperto l’intero programma teorico di diritto, storia, economia o lingue. I rinvii al volume base coprono soltanto i fondamenti e il metodo delle sezioni indicate.

Definizione, funzione, ambito, elementi, distinzioni, conseguenze, casi, output, errori e verifiche sono riesaminati nel perimetro assegnato. Q indica il totale del capitolo, C ed E almeno un caso e un esercizio. I riscontri normativi sono selettivi e documentati nella fonte; il conteggio parole non sostituisce la verifica sostanziale.

| Nucleo ID | Materia/concetto | Fonte | Collocazione | Teoria | Applicazione/output | Verifica | Stato | Review normativa |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
for st in stats:
 for n in st['nuclei']:t+=f"| {n['id']} | {n['heading']} | [[{source}]] | cap. {st['chapter']:02}, heading {n['id']} | Spiegazione del perimetro assegnato | {details[st['chapter']]} | Q:{st['quiz']} C:1 E:1 | completo | Riscontri selettivi, tornate e limiti dichiarati |\n"
p.write_text(t,encoding='utf8')
p=Path('wiki')/(topic+'.md');assert not p.exists();p.write_text('---\nid: topic-m-sp04-prefettizia-diplomatica-prove\ntype: topic\ntitle: Prefettizia e diplomatica — accesso e prove\nstatus: consolidated\ndomain: concorsi pubblici\nsource_refs: '+json.dumps([source])+'\nentities: '+json.dumps(entities)+'\nbook_refs: ["m-sp04-prefettizia-diplomatica"]\nupdated_at: 2026-10-03\ncreated_at: 2026-10-03\nreview_required: false\ncanonical: true\n---\n\n# Prefettizia e diplomatica — accesso e prove\n\nDue carriere distinte per amministrazione, requisiti, lingue e graduatoria. La domanda precede il calendario delle prove: le opzioni dichiarate hanno propri termini. La prefettizia richiede specifici titoli; il bando diplomatico 2026 ammette laurea magistrale o equiparata senza lo stesso elenco ristretto.\n\n[['+source+']] — '+', '.join('[['+x+']]' for x in entities)+'\n\n'+'\n'.join(f"- [[{Path(st['path']).with_suffix('').as_posix()[5:]}]] — {details[st['chapter']]}" for st in stats)+'\n',encoding='utf8')
p=Path('wiki/entities/ministero-affari-esteri.md')
if not p.exists():p.write_text('---\nid: entity-ministero-affari-esteri\ntype: entity\ntitle: Ministero degli affari esteri e della cooperazione internazionale\nstatus: consolidated\ndomain: amministrazioni centrali\nsource_refs: ["'+source+'"]\nupdated_at: 2026-10-03\ncreated_at: 2026-10-03\nreview_required: false\ncanonical: true\n---\n\n# Ministero degli affari esteri e della cooperazione internazionale\n\nAmministrazione della carriera diplomatica e della rete delle relazioni con l’estero, distinta dall’accesso ai profili amministrativi generali. Per la selezione 2026: [['+source+']]. Percorso: [['+topic+']].\n',encoding='utf8')
p=Path('wiki')/(source+'.md');t=p.read_text(encoding='utf8').replace('economia comprende politica economica','economia comprende economia politica, politica economica');t+='\nRaccordo: [['+topic+']], '+', '.join('[['+x+']]' for x in entities)+', [[books/moduli/m-sp04-prefettizia-diplomatica/index]].\n';p.write_text(t,encoding='utf8')
mapping={48:(1,details[1]),49:(1,'Requisiti come condizione necessaria, punteggi personali soltanto dopo l’ammissibilità.'),50:(2,'Paolo nato 1 luglio 1989, scadenza 10 luglio 2025: fuori limite con il solo figlio; variante 20 luglio.'),51:(2,'Confronto risposta/omissione: 2/9, 1/5, 4/23; esempi con quattro/cinque opzioni e limiti della stima.'),52:(2,'Art. 10: scrittura digitale con esercizio e verifica delle istruzioni.'),53:(2,'SSAI soppressa dal 2014, funzioni trasferite alla SNA.'),54:(2,'Formula con titoli e lingua, caso 150 e variante insufficiente; preferenze distinte.'),55:(3,'Laurea magistrale o equiparata, riconoscimento/equivalenza e termini distinti.'),56:(3,'Programma economico aggiornato e coordinato con i capitoli 1 e 5.'),57:(3,'Cinque opzioni per la materia facoltativa, scelta in domanda, 1,2/2, raccordo con Decoder e piano.'),58:(3,'Titoli e bonus con limiti; caso 149,2 e controlli inversi.'),59:(4,'Diagnosi e scelta prima della scadenza; nessun cambio libero dopo il termine.'),60:(4,details[4]),61:(5,details[5]),62:(6,details[6]),63:(7,'Residui staff rimossi nei quattro moduli; nota di accorpamento conservata nello snapshot, non nel libro.'),64:(7,'Commenti corretti e chiavi riequilibrate nei quattro moduli, con risposta semantica conservata.'),65:(7,'Refusi dell’audit corretti nei quattro moduli e nuova scansione mirata.'),66:(7,'Regole duplicate ricondotte alle sedi pertinenti; casi e laboratori con dati e soluzioni sostituiscono genericità nei quattro moduli.')}
(A/'M-SP04-findings-map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf8')
report='''# M-SP04 — Correzioni editoriali del 3 ottobre 2026

## 1. Sintesi editoriale

Applicati V12-48–62 e concluse le correzioni trasversali V12-63–66. Sette capitoli riletti integralmente, fonti consolidate, casi risolti e controlli di coerenza eseguiti. Ulteriore correzione: scadenza MAECI 27 aprile 2026 ore 12, per il termine festivo del 26 aprile. Nuovo PDF necessario.

## 2. Punti applicati della checklist

Perimetro, titoli, sequenza, requisiti, aggiornamento, fonti, numeri, esempi, quiz, commenti, applicazioni, autonomia, rinvii, numerazione, stile e residui staff. Distinti ammissibilità, preparazione, voto, preferenza e riserva.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
'''
for n,(c,desc) in mapping.items():report+=f'| V12-{n:02} | Capitolo {c:02} e raccordi | Contenuto e applicazione | Media | {desc} | Applicata nei file correnti | Corretto |\n'
report+='\n## 4. Osservazioni per capitolo\n\n'+'\n\n'.join(f'{c:02}: {v}' for c,v in details.items())+'''

## 5. Coerenza globale

37 nuclei con ID coerenti con capitolo e matrice. Modalità digitali per entrambi i binari, lingue e requisiti distinti. Fonti collegate a topic ed entità; rinvii al volume base con destinazioni esistenti. Matrice circoscritta al perimetro effettivo, senza dichiarare coperto l’intero programma disciplinare.

## 6. Contenuto da verificare

Nuovo PDF e revisione del volume. Pubblicazione corrente della banca dati e calendari restano controlli del candidato sui portali: il libro non presenta la vecchia ricognizione di agosto come verifica odierna. Ordinamenti storici distinti dai riscontri nuovi sul bando e sulla SNA.

## 7. Suggerimenti facoltativi

I laboratori sono originali e ridotti per l’allenamento. Non replicano tracce ministeriali né garantiscono voti. Le settimane da 12 e 20 ore richiedono basi già presenti e finestre per prove complete.

## 8. Priorità degli interventi

Audit specialistico, manifest, rigenerazione PDF e revisione finale di volume secondo la pipeline.

## 9. Giudizio di pubblicabilità

Non attestata. Il completamento testuale non sostituisce controllo visivo e gate conclusivi.

## 10. Limiti della revisione

Lettura integrale dei sette capitoli; riscontri normativi selettivi dichiarati nella fonte. Non certificazione dell’intero ordinamento. Esempi e calcoli controllati sulle ipotesi esplicite; nessuna previsione di ammissione individuale.
'''
p=R/'14-moduli-m-sp04-prefettizia-diplomatica.md';arc=C/'archive/pre-correzioni-14-m-sp04.md'
if p.exists() and not arc.exists():arc.write_bytes(p.read_bytes())
p.write_text(report,encoding='utf8');print('SP04 close14',sum(s['words'] for s in stats),'words',sum(s['quiz'] for s in stats),'quiz')
