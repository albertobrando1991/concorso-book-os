from pathlib import Path
import re,json,shutil,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia/chapters')
p=next(B.glob('05-*.md'));t=p.read_text('utf-8');b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
before=hashlib.sha256(p.read_bytes()).hexdigest()
t=t.replace("c'e tra due istituti","c'è tra due istituti")
addition='''### Dossier completo: preparare una causa contrattuale

Il dossier seguente è interamente fittizio; nomi, numero di ruolo e documenti sono creati per l'esercizio. Le regole processuali richiamate sono quelle spiegate nel capitolo 6. L'incarico è preparare la prima udienza, senza redigere una decisione.

**Identificazione.** Tribunale ordinario di Bologna, sezione civile, fascicolo didattico RG 1250/2026; attrice Alfa Arredi s.r.l., convenuta Beta Servizi s.r.l.; cognizione ordinaria. La citazione notificata il 16 febbraio 2026 indica l'udienza del 29 giugno 2026. Con decreto del 4 maggio il giudice conferma tale data dopo le verifiche preliminari; la cancelleria lo comunica il 5 maggio. Si assume regolare il contraddittorio e non si applicano sospensioni nel periodo del caso.

**Documenti disponibili.** Queste sintesi costituiscono il materiale da usare; non aggiungere fatti mancanti.

| Documento didattico | Contenuto fornito |
|---|---|
| D1 — Contratto, 10 dicembre 2025 | Fornitura di arredi per euro 12.000; consegna pattuita entro 12 gennaio 2026; pagamento entro 31 gennaio. Nessuna clausola su penali è riportata nel dossier. |
| D2 — Documento di consegna, 12 gennaio | Indica sei colli consegnati presso Beta e una firma del ricevente; non riporta descrizione analitica dello stato di ogni arredo. |
| D3 — Email di Beta, 15 gennaio | Beta dichiara che due pannelli sono danneggiati e chiede un sopralluogo. Non sono allegati fotografia o verbale tecnico. |
| D4 — Contabile bancaria, 30 gennaio | Indica ordine di bonifico di euro 3.000 da Beta ad Alfa con causale riferita alla fornitura; non contiene attestazione dell'accredito sul conto beneficiario. |
| D5 — Citazione, notificata 16 febbraio | Alfa chiede euro 12.000 e sostiene che la fornitura sia stata eseguita correttamente. Si costituisce il 24 febbraio. |
| D6 — Comparsa di Beta, 17 aprile | Beta allega il pagamento di euro 3.000 e contesta la qualità di parte della fornitura, opponendosi alla richiesta residua. Produce D3 e D4; non formula nel dossier una domanda riconvenzionale. |
| D7 — Decreto, 4 maggio | Conferma udienza 29 giugno dopo le verifiche preliminari; comunicazione 5 maggio. |
| D8 — Memorie | Prime memorie depositate il 20 maggio; memoria istruttoria di Alfa depositata il 9 giugno; memoria istruttoria di Beta depositata il 10 giugno. Nessuna istanza di rimessione in termini risulta nel materiale. |

**Consegna.** Prepara cronologia, scheda causa, nota di ricerca sulla memoria del 10 giugno e promemoria per l'udienza. Distingui ciò che risulta da un documento, ciò che una parte sostiene e ciò che il magistrato deve valutare. Tempo suggerito: 35 minuti.

### Soluzione: cronologia e scheda causa compilate

| Data | Evento e riferimento | Rilevanza da registrare |
|---|---|---|
| 10 dicembre 2025 | Contratto D1 | Oggetto, prezzo e scadenze pattuite. |
| 12–15 gennaio 2026 | Consegna D2 ed email D3 | Presenza di un documento di ricezione; contestazione successiva della qualità. |
| 30 gennaio | Ordine di bonifico D4 | Supporta l'allegazione del versamento, ma il dossier non documenta l'accredito. |
| 16–24 febbraio | Notifica e costituzione Alfa, D5 | Avvio della causa; costituzione entro dieci giorni dalla notifica. |
| 17 aprile | Comparsa D6 | Prima del termine del 20 aprile; difese e allegati di Beta. |
| 4–5 maggio | Decreto e comunicazione D7 | Udienza confermata e presupposto per lo scadenzario delle memorie. |
| 20 maggio | Prime memorie D8 | Termine dei quaranta giorni. |
| 9–10 giugno | Memorie istruttorie D8 | Termine dei venti giorni al 9 giugno; deposito Beta del giorno successivo da segnalare. |
| 29 giugno | Udienza confermata D7 | Preparazione delle questioni processuali e delle richieste istruttorie. |

**Scheda causa — redatta il 12 giugno 2026, materiale preparatorio.** Oggetto: domanda di pagamento del prezzo di una fornitura, euro 12.000; Beta deduce un versamento di euro 3.000 e difetti di parte dei beni. Stato: fase precedente alla prima udienza, dopo deposito delle memorie istruttorie. Prossima scadenza ordinaria: 19 giugno per la terza memoria; udienza 29 giugno.

**Fatti e allegazioni.** D1 documenta il contenuto contrattuale riportato nel dossier. D2 documenta una consegna di sei colli e la presenza di una firma, non da solo la conformità di ogni bene. D3 prova che Beta ha formulato quella contestazione, non che i pannelli fossero effettivamente danneggiati. D4 documenta l'ordine bancario descritto, non consente da solo di affermare l'avvenuto accredito. Non si deve scrivere «debito residuo accertato: euro 9.000»: è un risultato aritmetico possibile se il pagamento viene riconosciuto, non una decisione già presa.

**Questioni per il magistrato.** Verifica del pagamento allegato e della contestazione qualitativa; individuazione dei fatti controversi e delle prove richieste; tempestività ed effetti delle produzioni contenute nella memoria Beta del 10 giugno. Non risultano dal dossier perizia, fotografie, quietanza o riconoscimento di Alfa sul pagamento: annotare l'assenza, senza creare documenti o presumere il loro contenuto.

**Atti da consultare in priorità.** D5 e D6 per domande e difese; D1–D4 per il supporto documentale; D7 per la data dell'udienza; ricevute e contenuti delle memorie D8 per la questione processuale. La scheda non sostituisce la lettura diretta di questi atti.

### Soluzione: nota di ricerca realmente compilata

**Quesito:** rispetto all'udienza del 29 giugno, confermata con decreto del 4 maggio, quale termine ordinario si applica alla memoria istruttoria ex art. 171-ter, numero 2, depositata da Beta il 10 giugno?

**Fonti pertinenti:** artt. 155, 171-bis e 171-ter c.p.c., testo vigente considerato nel capitolo 6. Il decreto previsto dal 171-bis è presente; il termine di venti giorni prima dell'udienza conduce al 9 giugno 2026, martedì. Non ricorrono nel caso festività finali o sospensione feriale.

**Applicazione:** la data documentata del 10 giugno è successiva di un giorno alla scadenza ordinaria. Segnalare il deposito, la data rilevante risultante dalle ricevute e quali produzioni o richieste contiene. Non limitarsi alla data visualizzata nel registro se differisce dall'evento che perfeziona il deposito.

**Conclusione preparatoria e limiti:** esiste una criticità di tempestività da sottoporre al magistrato. La nota non dispone lo stralcio della memoria, non cancella il deposito e non decide quali attività siano precluse; tali valutazioni richiedono esame del contenuto, delle richieste e di eventuali ulteriori circostanze. Nessuna istanza di rimessione in termini è fornita nel dossier. Non occorre aggiungere una sentenza generica soltanto per rendere più lunga la ricerca: la questione assegnata trova anzitutto risposta nelle disposizioni indicate.

### Soluzione: promemoria d'udienza e seguito

**Udienza 29 giugno 2026 — RG didattico 1250/2026.** Verificare presenza delle parti; avere disponibili contratto, documento di consegna, email e contabile; distinguere domanda di Alfa, contestazioni di Beta e prova dell'accredito mancante. Portare all'attenzione del magistrato la sequenza delle memorie, con scadenza del 9 giugno e deposito Beta del 10. Preparare l'elenco delle richieste istruttorie risultanti dagli atti, senza anticiparne ammissione o rigetto. Aggiornare la scheda con gli eventuali depositi successivi al 12 giugno prima di usarla in udienza.

**Variante post-udienza, dato aggiuntivo dell'esercizio:** il verbale del 29 giugno dispone un'udienza istruttoria il 14 settembre e riserva la decisione sulle questioni indicate; il testo integrale è nel fascicolo. L'aggiornamento corretto annota provvedimento, nuova data e attività espressamente disposte; non trasforma una riserva in rigetto o accoglimento. La cancelleria cura gli adempimenti di competenza, l'UPP aggiorna il materiale preparatorio e il monitoraggio. Non si inviano alle parti interpretazioni informali sull'esito.

### Esercizio autonomo con soluzione

Rileggi questa frase e correggila: «Beta ha pagato 3.000 euro, i mobili sono difettosi e la memoria tardiva deve essere eliminata; il giudice condannerà al pagamento di 9.000 euro».

**Soluzione modello:** «Beta allega un pagamento di 3.000 euro, documentato nel dossier da un ordine di bonifico senza prova dell'accredito, e lamenta difetti attraverso l'email del 15 gennaio. La memoria del 10 giugno risulta successiva alla scadenza ordinaria del 9 giugno: la criticità e il contenuto dell'atto vanno sottoposti al magistrato. Restano da valutare pagamento, conformità e conseguenze processuali; nessuna decisione è stata adottata».

**Autovalutazione, 10 punti:** due per fonti documentali identificabili; due per distinzione tra fatti e allegazioni; due per calendario corretto; due per questione giuridica pertinente; due per rispetto del ruolo. Assegna un punto, anziché due, quando l'elemento è presente ma impreciso; zero se manca o è errato. Una scheda che inventa il provvedimento o altera il fascicolo va rifatta anche se ottiene punti nelle altre voci.

'''
t=t.replace('### Caso guidato: fascicolo assegnato prima dell’udienza',addition+'### Caso guidato: fascicolo assegnato prima dell’udienza') if '### Caso guidato: fascicolo assegnato prima dell’udienza' in t else t.replace("### Caso guidato: fascicolo assegnato prima dell'udienza",addition+"### Caso guidato: fascicolo assegnato prima dell'udienza",1)
t=re.sub(r'### Quiz commentato\n.*?(?=### Checklist di ripasso)', '''### Quiz commentato

1. **Nel dossier, l'email di Beta sui pannelli danneggiati consente anzitutto di affermare che:**
   - A. il difetto è già accertato dal giudice.
   - B. Alfa ha riconosciuto la propria responsabilità.
   - C. Beta ha formulato una contestazione, da distinguere dalla prova del difetto.
   **Risposta corretta: C.** La scheda deve attribuire l'affermazione al suo autore e indicarne la fonte, senza trasformarla in fatto accertato.

2. **La contabile D4 riporta un ordine di bonifico ma non l'accredito. Quale annotazione è corretta?**
   - A. Ordine di euro 3.000 documentato; accredito non dimostrato dal materiale fornito.
   - B. Pagamento definitivamente accertato con effetti già decisi.
   - C. Documento irrilevante da eliminare dal fascicolo.
   **Risposta corretta: A.** Si descrive ciò che il documento contiene e ciò che manca; la valutazione finale non spetta all'addetto.

3. **Quale ricerca risponde al compito assegnato nel caso?**
   - A. Raccogliere tutti i precedenti sulla responsabilità contrattuale senza selezione.
   - B. Verificare decreto, udienza e termine della memoria istruttoria del 10 giugno.
   - C. Cercare soltanto una massima favorevole alla richiesta dell'attrice.
   **Risposta corretta: B.** Quesito, norma ed eventi documentati devono essere collegati; la ricerca non è una raccolta orientata a favorire una parte.

4. **Il deposito di Beta risulta successivo alla scadenza ordinaria. Che cosa fa l'AUPP?**
   - A. Cancella l'atto dal fascicolo informatico.
   - B. Comunica alla parte che ogni sua difesa è respinta.
   - C. Segnala date, ricevute e contenuto al magistrato per la valutazione pertinente.
   **Risposta corretta: C.** Il supporto documenta la criticità e non adotta autonomamente una decisione processuale.

5. **Quale elemento rende verificabile una cronologia?**
   - A. La valutazione personale dell'estensore al posto degli atti.
   - B. Data, evento e riferimento al documento da cui risulta.
   - C. Il solo ordine di caricamento dei file, anche se diverso dalle date processuali.
   **Risposta corretta: B.** Un evento deve poter essere ricondotto alla sua fonte; ordine informatico e sequenza giuridica possono non coincidere.

6. **Il verbale contiene una riserva del giudice. Come va aggiornata la scheda?**
   - A. Riportando la riserva e le attività effettivamente disposte.
   - B. Registrando un rigetto, perché la decisione è rinviata.
   - C. Registrando un accoglimento provvisorio della domanda.
   **Risposta corretta: A.** La riserva non equivale né a rigetto né ad accoglimento: l'aggiornamento deve seguire il testo del provvedimento.

''',t,flags=re.S)
for s in ['vol-04-organizzazione-upp-verifica-2026-10-03','vol-04-processo-civile-verifica-2026-10-03']:
 t=t.replace('source_refs: [',f'source_refs: [\n  "sources/{s}.md",',1).replace('last_compiled_from: [',f'last_compiled_from: [\n  "wiki/sources/{s}.md",',1)
t=re.sub(r'updated_at:.*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true')
p.write_text(t,'utf-8')
(A/'VOL-04-fascicolo-delta.json').write_text(json.dumps({'path':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'dossierDocuments':8,'outputs':['cronologia','scheda causa','nota ricerca','promemoria udienza','seguito','esercizio corretto'],'quiz':6},ensure_ascii=False,indent=2),'utf-8')
print('Capitolo05: dossier, quattro output, seguito, esercizio e quiz applicati')
