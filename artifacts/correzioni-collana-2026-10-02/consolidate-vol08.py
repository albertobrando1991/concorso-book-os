from pathlib import Path
import re,json,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale')
changes=[]
replacements={
7:{
'DevOps mette in relazione sviluppo, rilascio ed esercizio. Il suo risultato atteso è una modifica identificabile, verificata e recuperabile, non una sequenza più veloce di passaggi non controllati.':'',
"L'Infrastructure as Code applica lo stesso principio alla configurazione. Una modifica a rete, capacità o ambiente non resta in una console amministrativa priva di storia: viene proposta, letta, testata e applicata con un identificativo. Il vantaggio non è l'assenza di errori, ma la possibilità di confrontare lo stato previsto con quello reale e di riprodurre un ambiente. Gli elementi sensibili, come segreti e credenziali, non vanno copiati nei file ordinari: richiedono gestione separata e accessi controllati. Dopo un rilascio il lavoro continua con la verifica delle funzioni, delle prestazioni e degli effetti sui dati.":'Dopo il rilascio si verificano funzioni, prestazioni ed effetti sui dati; la configurazione versionata conserva il collegamento tra modifica ed esito.',
'Un servizio governato produce segnali leggibili e li collega a decisioni. Osservare non significa accumulare dati: significa poter spiegare un degrado, decidere una priorità e verificare se l\'intervento ha funzionato.':''},
12:{"La scelta resta quindi un atto di governo: documentare assunzioni, alternative scartate, dipendenze e criterio di verifica rende la decisione esaminabile anche quando cambiano persone o fornitori. Il costo iniziale non esaurisce la valutazione: migrazione, formazione, integrazioni, manutenzione, crescita dei volumi e uscita possono modificare il costo effettivo del servizio. Una risposta concorsuale completa esplicita questo ciclo e non presenta make, buy o reuse come formule automatiche.":'Conserva motivazione e alternative scartate: chi subentra deve poter riesaminare la decisione se cambiano fabbisogno o costi.'},
13:{"Rileggi il testo cercando la catena requisito, scelta, rischio, controllo, evidenza. Se un paragrafo non entra nella catena, chiediti se è davvero pertinente. Se una scelta non ha un limite, un rischio o una verifica, probabilmente è ancora un'affermazione astratta. Questo controllo evita sia l'elenco di prodotti sia l'architettura universale immaginaria.":''}
}
for n,pairs in replacements.items():
 p=next((B/'chapters').glob(f'{n:02}-*.md'));s=p.read_text(encoding='utf8')
 for old,new in pairs.items():
  assert old in s,(n,old[:40]);s=s.replace(old,new,1);changes.append({'chapter':n,'old':old,'new':new,'reason':'concetto già sviluppato nel nucleo; preservati passaggi non ripetuti'})
 s=re.sub(r'\n{4,}','\n\n\n',s);p.write_text(s,encoding='utf8')
(A/'VOL-08-style-deltas.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf8')
p=B/'index.md';s=p.read_text(encoding='utf8').replace('publication-ready','revision-in-progress').replace('M-TR01 - ICT','M-TR01 — ICT')
s=s.replace('[[books/moduli/m-tr02-appalti-pnrr-fondi-ue/index#Perimetro|M-TR02]] è solo un instradamento di catalogo finché resta incompleto.', '[[books/moduli/m-tr02-appalti-pnrr-fondi-ue/index|M-TR02, nel VOL-09]], sviluppa procedure e gestione contrattuale: usa l’indice per selezionare il capitolo pertinente al bando.')
s=re.sub(r'I capitoli 01-13 hanno completato.*?(?=\n\n)', 'I tredici capitoli sono in revisione dei rilievi dell’audit integrale del 2 ottobre 2026. Il testo aggiornato al 3 ottobre integra fonti, teoria, esempi e soluzioni; riesame specialistico e congelamento sono gestiti dal CLI. La pubblicabilità richiede anche la verifica delle figure e dell’esportazione PDF aggiornata e i gate finali del volume.',s)
s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M).replace('source_refs: [','source_refs: ["sources/ict-rettifiche-specialistiche-2026-10-03", ',1)
p.write_text(s,encoding='utf8')
p=B/'planning/02-matrice-copertura-didattica.md';s=p.read_text(encoding='utf8').replace('updated_at: 2026-08-10','updated_at: 2026-10-03').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/ict-rettifiche-specialistiche-2026-10-03", ',1)
s+='''\n## Rettifiche dell’audit integrale — 3 ottobre 2026

Le righe e i nuclei sopra descrivono la copertura strutturale; i seguenti delta precisano il contenuto corrente e superano i precedenti rinvii generici a verifiche future. Fonte comune: [[sources/ict-rettifiche-specialistiche-2026-10-03]], con [[topics/ict-rettifiche-specialistiche-2026]].

| Capitoli | Teoria ed evidenza aggiunte | Verifica e limiti |
| --- | --- | --- |
| 02–03 | Complemento a due, significando/esponente, spazio totale/ausiliario, O e Theta | Calcoli 8 bit, interpretazione dell’overflow, quiz 5 e fonte Morin |
| 04–06 | FK obbligatoria, quattro isolamenti e PostgreSQL 18, versioni HTTP, test, REST e PDND | Sequenza T1/T2, requisito numerico, richiesta/risposta API e permessi |
| 07–08 | Classificazione/qualificazione cloud, STRIDE tradotto e casi | Tre impatti, sei minacce/controlli, due aperte risolte |
| 09 | NIS2 essenziali/importanti, governance, notifiche e coorti ACN, legge 90 e GDPR, crittografia/PKI | Timeline 24/72/mese e sei quiz a scelta multipla con commenti; allegati tecnici ACN non riprodotti |
| 10 | Requisiti cumulativi CAD e HVD, definizioni prima delle applicazioni | Sei quiz nuovi, casi di governance e percorso PDND nel cap. 06 |
| 11 | Ruoli/rischi AI, legge 132 art. 14 e modifica UE 1744/2026; due algoritmi e metriche | Albero, k-means, matrice di confusione, precision/recall/F1; date distinte dai transitori |
| 12 | CAD 68–69, legge 208 commi 512 e seguenti, funzione DEC e DPO | Confronto TCO e SLA numerico; ruoli senza inventare poteri di approvazione |
| 13 | Elaborato completo, soluzione del caso autonomo e prova pratica aggiuntiva | SQL con output, massimo/caso vuoto, metriche e rubrica; dati originali didattici |

La verifica periodica di una fonte mobile rimane un dovere operativo e non una lacuna didattica: le regole datate pertinenti sono spiegate nel testo. Le matrici storiche non certificano pubblicabilità PDF.
''';p.write_text(s,encoding='utf8')
topic=Path('wiki/topics/ict-rettifiche-specialistiche-2026.md')
topic.write_text('''---
id: topic-ict-rettifiche-specialistiche-2026
type: topic
title: "ICT: fondamenti, sicurezza, dati, AI e acquisti — rettifiche 2026"
status: consolidated
domain: concorsi pubblici italiani
topics: ["ICT", "cybersecurity", "AI", "dati"]
entities: ["ACN", "AgID", "Unione europea"]
source_refs: ["sources/ict-rettifiche-specialistiche-2026-10-03"]
book_refs: ["m-tr01-ict-trasformazione-digitale"]
parent_topics: []
child_topics: []
chapter_refs: ["books/moduli/m-tr01-ict-trasformazione-digitale/index"]
confidence: 0.95
created_at: 2026-10-03
updated_at: 2026-10-03
review_required: true
canonical: true
tags: ["VOL-08", "rettifiche-audit"]
---

# ICT: rettifiche specialistiche 2026

La [[sources/ict-rettifiche-specialistiche-2026-10-03|fonte consolidata]] raccoglie i riscontri primari e i limiti delle acquisizioni. Il [[books/moduli/m-tr01-ict-trasformazione-digitale/index|modulo M-TR01]] applica le regole a casi e prove tecniche.

## Fondamenti e servizio

Distinguere rappresentazione numerica e comportamento del linguaggio, costo totale e ausiliario, limite O e ordine Theta. Isolamento SQL e implementazione concreta hanno garanzie differenti. HTTP/3 non usa TCP; regressione è una finalità, non un livello di test. REST richiede vincoli architetturali; una API JSON non li dimostra da sola. PDND supporta scambi autorizzati e non crea la base giuridica.

## Sicurezza e notifiche

Classificazione dei dati/servizi e qualificazione del cloud sono controlli distinti. Nel NIS si verifica prima il campo soggettivo, poi categoria, misure, significatività e coorte ACN. Pre-notifica 24 ore e notifica ordinaria 72 ore decorrono dalla stessa conoscenza; relazione finale dal momento indicato dalla norma. Legge 90 e GDPR mantengono presupposti propri. Hash, firma, cifratura e MAC offrono proprietà differenti; certificato, fiducia, revoca e autorizzazione non sono sinonimi.

## Dati e AI

Gli open data richiedono cumulativamente condizioni di riuso, formati/metadati e regime economico CAD. Gli HVD hanno obblighi API e formati, con bulk secondo allegato. Per AI si verificano ruoli, uso e rischio prima del calendario, modificato dal regolamento 1744/2026. La legge 132, articolo 14, conserva decisione e responsabilità umane nella PA. Addestramento, test e metriche devono rendere visibili errori e limiti: l’accuracy può nascondere omissioni gravi.

## Acquisti e prove

CAD 68–69 guida valutazione e riuso; legge 208/2015 aggiunge vincoli sul canale di approvvigionamento ICT. La direzione dell’esecuzione è una funzione necessaria, con DEC separato nei casi previsti. Il DPO consiglia e sorveglia senza approvare al posto del titolare. TCO e SLA richiedono dati, denominatori e condizioni dichiarati. Le prove del capitolo 13 producono un elaborato, una diagnosi e risultati numerici autocorreggibili.

## Limiti

Aggiornamento mirato al 3 ottobre 2026, non certificazione di ogni fonte storica né esaustività di qualunque bando ICT. Le fonti precedenti sono conservate; questo consolidamento prevale per i claim espressamente rettificati. Figure e PDF richiedono controllo sulla versione aggiornata.
''',encoding='utf8')
p=Path('wiki/sources/ict-rettifiche-specialistiche-2026-10-03.md');s=p.read_text(encoding='utf8').replace('## Collegamenti e limiti\n\n','').replace('e verrà completata con gli ulteriori riscontri','al 3 ottobre 2026');s+='\nVerificato nuovamente il testo integrale dell’articolo 14 della legge 132/2025 sulla Gazzetta ufficiale: quattro commi, nessuna delega della decisione provvedimentale al sistema. Esempi di albero, k-means, metriche, TCO e SLA ricalcolati con dati didattici originali.\n';p.write_text(s,encoding='utf8')
# Immutable acquisitions: report invalid response explicitly without changing raw.
raw=Path('wiki/raw/correzioni-vol08-2026-10-03');manifest=[]
for p in raw.iterdir():
 if p.is_file():manifest.append({'path':p.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'validPdf':p.read_bytes().startswith(b'%PDF'),'limitation':'ANAC download returned error body, not normative PDF' if p.name=='anac-dec.pdf' else ''})
(A/'VOL-08-raw-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('Indice, matrice, topic, fonte, manifest raw e condensazione editoriale aggiornati.')
