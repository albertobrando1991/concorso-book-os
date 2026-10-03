from pathlib import Path
import json,re,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale');R=Path('wiki/reviews/pipeline/VOL-08');R.mkdir(exist_ok=True)
applied={1:'Indice e matrice riconciliati: nessuna pubblicabilità anticipata; M-TR02 è un rinvio effettivo al VOL-09.',2:'Bando, Aree, Nuclei, Diario, Output ripristinati nei capitoli 10–12.',3:'Tutte le 13 tabelle staff spostate in planning/verifiche; audit conserva controllo atomico dei target reali.',4:'Complemento a due su otto bit, intervalli, overflow e modello segno/esponente/significando con 1,5.',5:'Spazio totale e ausiliario distinti; scansione con contatore e modello dichiarato.',6:'Limite O distinto da Theta; quiz 5 usa funzioni dominanti esplicite e calcolo del raddoppio.',7:'Fonte bibliografica identificata: Pat Morin, Open Data Structures, versione Python, § 1.3.',8:'FK obbligatoria NOT NULL e id_ufficio esplicitato nello schema Assegnazione.',9:'Quattro livelli SQL, anomalie, specificità PostgreSQL 18 e sequenza concorrente risolta.',10:'Esempio circoscritto a HTTP/1.1; HTTP/2 TCP e HTTP/3 QUIC distinti.',11:'Regressione descritta come finalità trasversale ai livelli di test.',12:'Requisito risolto: utenti, dati, percentile, durata, latenza e tasso di errore.',13:'Vincoli REST, richiesta/risposta API, autorizzazione per oggetto, stati ed errori.',14:'Classificazione ordinario/critico/strategico e impatti; regolamento ACN 21007/24 e qualificazione distinta.',15:'Sei categorie STRIDE tradotte con minaccia, esempio e controllo.',16:'Due aperte cybersecurity risolte sul caso dei fascicoli e sui controlli temporanei.',17:'NIS2 artt. 6 e 23–25, governance, coorti ACN 2025/2026, timeline e raccordo legge 90/GDPR.',18:'Simmetrica/asimmetrica, firme, hash, MAC, password, certificati, catena, revoca e TLS.',19:'Dodici quiz riscritti nei capitoli 9–10, tre chiavi per lettera e commenti corrispondenti.',20:'Refuso “nell’ignorare” corretto.',21:'Tre requisiti cumulativi della definizione CAD di dati di tipo aperto.',22:'HVD: API e formati obbligatori, bulk dove previsto; licenze, metadati e documentazione.',23:'Rinvio PDND delimitato e destinazione cap. 06 integrata con flusso, ruoli, voucher e caso.',24:'Refuso “uso interno” corretto.',25:'Ruoli e rischio AI, obblighi PA e legge 132 art. 14; calendario modificato dal regolamento 1744/2026 e transitori distinti.',26:'Albero decisionale, k-means, matrice di confusione, precision/recall/F1 e baseline calcolati.',27:'CAD 68–69, confronto TCO, riuso e legge 208/2015 commi 512 e seguenti.',28:'SLA su 43.200 minuti: 90 di fermo, 99,7917%, scostamento e limite di penali/esclusioni.',29:'Funzione della direzione dell’esecuzione distinta dalla nomina di un DEC separato.',30:'Decisione al titolare; DPO consiglia e sorveglia, senza approvazione sostitutiva.',31:'Elaborato completo, diagnosi con tre ipotesi e prova SQL/algoritmo/metriche con risultati e rubrica.',32:'Definizioni prima delle applicazioni nel cap. 10; riprese condensate in 7/12/13; spazio usato per esempi e soluzioni.'}
rows=[]
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-08.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\| V08-\d\d \|',line):
  c=[x.strip() for x in line.strip('|').split('|')];n=int(c[0][-2:]);rows.append({'id':c[0],'position':c[1],'category':c[2],'severity':c[3],'diagnosis':c[4],'correction':applied[n],'status':'Applicato; riesame specialistico corrente'})
assert len(rows)==32
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |\n'+''.join('| '+' | '.join([r['id'],r['position'],r['category'],r['severity'],r['diagnosis'],r['correction'],r['status']])+' |\n' for r in rows)
text='''# VOL-08 — Correzioni integrali del testo, 3 ottobre 2026

## 1. Sintesi

Applicati i 32 rilievi testuali dell’audit integrale. Il lavoro si basa sulla lettura completa dei tredici originali documentata nell’audit precedente, sul riesame dei passaggi modificati, sulla verifica delle soluzioni e sul confronto con fonti primarie. La chiusura riguarda il testo; figure e PDF aggiornato restano da verificare.

## 2. Checklist applicata

Riesaminati i punti testuali 1–26 e 28–30: correttezza, chiarezza, progressione, autonomia, fonti, aggiornamento, ruoli, terminologia, quiz, esempi, rinvii, coerenza con matrice e indice. Punto 27: il precedente audit visuale non vale per il PDF dopo queste modifiche. Nessuna nuova attestazione di lettura integrale dei PDF normativi di 41 pagine o della Gazzetta intera: letti i passaggi pertinenti; i due provvedimenti ACN di cinque e tre pagine sono letti integralmente, senza allegati separati.

## 3. Registro per ID

'''+table+'''
## 4. Fonti ed evidenze

Fonte consolidata `ict-rettifiche-specialistiche-2026-10-03` e topic collegato, con URL ufficiali ACN, Commissione/EUR-Lex, Gazzetta Ufficiale, MEF, AgID, PagoPA, NIST, PostgreSQL, RFC e fonti tecniche originali. La nota distingue acquisizioni valide e riscontri indicizzati. L’errore del download ANAC è esplicitato nel manifest raw e non viene presentato come PDF normativo letto. Le soglie non verificate non sono introdotte. Le raccolte storiche conservano i propri limiti; il nuovo consolidamento prevale sui claim rettificati.

## 5. Copertura e autonomia

Ottantadue nuclei mantengono identità e destinazione. Le verifiche staff sono in planning, non nel prodotto; il controllo atomico confronta ancora i target con unità effettivamente presenti nel testo. Le nuove attestazioni sostituiscono solo citazioni supersedute, senza retrodatare il riesame o attribuirlo ai revisori storici. Capitoli 7–13 includono le integrazioni necessarie senza duplicare il diritto generale di VOL-01/VOL-09.

## 6. Verifiche

Tredici gate di densità/copertura passati senza blocchi o avvisi. Rinvii wikilink del corpo: zero destinazioni e ancore irrisolte. Audit Format 2: 82 nuclei coerenti tra capitoli, matrice e indice, senza duplicati o target mancanti. Dodici quiz nuovi risolti, chiavi A/B/C/D distribuite tre volte ciascuna; aperte cybersecurity con risposte specifiche. Verificati calcoli binari, costo quadratico, isolamento, SLA, TCO, Gini, centroidi, precision/recall/F1, query SQL e caso vuoto. Il test di regressione riproduce prima il mancato supporto ai mapping esterni e controlla che un target presente solo nello staff non basti.

## 7. Suggerimenti facoltativi

Nessuna scelta facoltativa usata per eludere una correzione obbligatoria. L’eventuale spazio ulteriore per esercizi verrà valutato sul PDF senza ridurre corpo tipografico o teoria.

## 8. Priorità residue

Audit specialistico e freeze tramite CLI; poi allineamento figure, esportazione, controllo visivo e preflight del volume. Il calendario AI nelle figure deve distinguere 2027/2028 dai transitori, mentre quello NIS deve distinguere le coorti.

## 9. Giudizio

Le correzioni note sono applicate e controllate nel testo. La pubblicabilità non è ancora dichiarata: occorre il candidato PDF aggiornato e il completamento dei gate di produzione.

## 10. Limiti

Riesame mirato dei claim tecnici/normativi coinvolti, datato 3 ottobre 2026; nessuna promessa di copertura di ogni bando ICT o validazione integrale di ogni documento citato. Esempi e cifre originali sono didattici, non prezzi, soglie normative o benchmark di amministrazioni. Gli hash identificano la versione verificata e non certificano figure/PDF.
'''
for target in [R/'14-moduli-m-tr01-ict-trasformazione-digitale.md',Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-08.md')]:
 if target.exists() and not (A/'before-text/VOL-08'/target.name).exists():shutil.copy2(target,A/'before-text/VOL-08'/target.name)
 target.write_text(text,encoding='utf8')
(A/'VOL-08-applied.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
# Reader references name the exact acts introduced in the text.
refs={7:'- ACN, regolamento 21007/24 del 27 giugno 2024, e catalogo di qualificazione del servizio pertinente.\n',9:'- Legge 90/2024, articolo 1 vigente; determinazioni ACN 379907/2025 e 127434/2026, per decorrenze e coorti.\n',11:'Regolamento (UE) 2026/1744, modifiche all’AI Act e calendario; legge 132/2025, articolo 14. Pat Morin e la documentazione scikit-learn sugli alberi e sul k-means per i metodi, distinti dagli esempi numerici originali.\n',12:'- CAD, articoli 68–69 e linee guida AgID su acquisizione e riuso; legge 208/2015, articolo 1, commi 512 e seguenti.\n'}
for n,ref in refs.items():
 p=next((B/'chapters').glob(f'{n:02}-*.md'));s=p.read_text(encoding='utf8');s=s.rstrip()+'\n\n'+ref;p.write_text(s,encoding='utf8')
# Place the independent prompt immediately before its solution; simulation points to both.
p=next((B/'chapters').glob('13-*.md'));s=p.read_text(encoding='utf8');start=s.index('### Caso autonomo:');end=s.index('Per il confronto, usa',start);block=s[start:end];s=s[:start]+s[end:];s=s.replace('### Soluzione commentata del caso autonomo',block+'### Soluzione commentata del caso autonomo',1);s=s.replace('Per il confronto, usa la soluzione commentata del caso autonomo','Per la simulazione autonoma, usa la traccia, la rubrica e la soluzione commentata del caso autonomo');p.write_text(s,encoding='utf8')
p=Path('wiki/books/volumi/vol-08-ict-digitale-cybersecurity-dati/planning/00-scheda-pipeline.md');s=p.read_text(encoding='utf8').replace('2026-07-28','2026-10-03');p.write_text(s,encoding='utf8')
p=B/'planning/03-bibbia-modulo.md';s=p.read_text(encoding='utf8');s+='\n## Rettifiche del 3 ottobre 2026\n\nI 32 rilievi dell’audit integrale sono applicati. Fonti puntuali e topic sono consolidati; tabelle interne di verifica spostate in `planning/verifiche/`. La pubblicabilità richiede nuovi controlli sulle figure e sul PDF, distinti dal testo. Il CLI possiede l’ordine e lo stato dei gate.\n';s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);p.write_text(s,encoding='utf8')
print('Registro 32 ID, rapporti, riferimenti e apparati aggiornati.')
