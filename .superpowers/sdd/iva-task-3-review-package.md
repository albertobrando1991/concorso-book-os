# IVA Task 3 review package post-fix-2

## Git status
```text
 M wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
 M wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
```

## Diffstat
```text
 .../04-diritto-tributario-teoria-imposta.md        |   2 +-
 ...dempimenti-fiscali-redditi-iva-dichiarazioni.md | 173 ++++++++++++++++-----
 2 files changed, 132 insertions(+), 43 deletions(-)
```

## Task 3 report
# Task 3 report â€” M-FC02 capitolo 6 IVA e adempimenti

## Status

DONE

## Baseline, perimetro e hash

- File editoriale: `wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md`.
- SHA-256 baseline: `7ADEA78E0C1E4EEF241A006E3595A25F9917224F870AC8BC2DC3F727E498F810`.
- SHA-256 dopo fix loop: `F03B8D680914136CE2B37D3EC61D0795C1C4E5209099B81D309C42A8A1101EA3`.
- Hash IRPEF/IRES HEAD: `F08C429FE23837D4760C8677E3F39909D0D35B758C83DEE6C170A03EA2F7C92A`.
- Hash IRPEF/IRES finale: `F08C429FE23837D4760C8677E3F39909D0D35B758C83DEE6C170A03EA2F7C92A`: preservazione confermata.
- `updated_at` preservato a `2026-07-20T00:00:00+02:00`.
- Il diff finale comprende anche una modifica di integrazione di una riga nel capitolo 4, necessaria a ripristinare il link/anchor verso il capitolo 6; Ã¨ uno scope coordinato e giustificato dal collegamento rotto. Nessun commit.

## Fix reviewer

| ID | Correzione | Evidenza | Esito |
| --- | --- | --- | --- |
| C1 | SoggettivitÃ  e territorialitÃ  L3 | beni/servizi, mappa B2B/B2C, eccezioni come gate, esempio ed errore | PASS |
| C2 | Catena documentale | fattura, registri vendite/acquisti, debito/detrazione, liquidazione ed errore risolto | PASS |
| I2 | Credito IVA | riporto, compensazione, rimborso e percorso prudente | PASS |
| I3 | Caso IVA determinato | Alfa/Beta/Gamma, luoghi, data, documenti, base `4.200 Ã— t`, rivalsa, detrazione e saldo | PASS |
| I4 | Dichiarazioni | originaria, correttiva legata alle istruzioni, tardiva valida, omessa, integrative a favore/sfavore e quattro casi | PASS |
| M1 | Compensazione | sei gate: esistenza, spettanza, disponibilitÃ , perimetro, ostacoli, controlli; due scenari | PASS |
| M2 | Dato temporale | vigenza D.Lgs. 241/1997 artt. 17-20 e disposizioni pertinenti al 20/07/2026; art. 24 transitorio/non fondativo di F24; futuro D.Lgs. 33/2025 dal 01/01/2027 | PASS |
| Refusi | Citazione Â«tutte senza IVAÂ» e definizione della detrazione nel quiz | testo corretto | PASS |

## Test specifici e output

- `rg -c '^## Operazioni IVA e ciclo degli adempimenti$' <capitolo>` â†’ `1`.
- `rg -c '^\*\*Scenario risolto [AB]' <capitolo>` â†’ `2`.
- Ricerca mirata B2B/B2C, registri, casi dichiarativi, sei gate, riporto/compensazione/rimborso e frase datata â†’ tutte le evidenze presenti.
- Ricerca `?tutte` â†’ 0 occorrenze.
- `updated_at` â†’ `2026-07-20T00:00:00+02:00`.
- Sequenza â€œDa sapere in 5 righeâ€ â†’ fattispecie/qualificazione, documentazione, registrazione, liquidazione, dichiarazione, versamento/compensazione, controllo, correzione nello stesso ordine â€” PASS.
- Caso Alfa/Beta/Gamma â†’ la fattura del 12 marzo anticipa lâ€™effettuazione per lâ€™importo fatturato; la sola ultimazione non basta nella regola generale della prestazione ordinaria nazionale â€” PASS.
- Fonte F24 â†’ artt. 17-20 e disposizioni pertinenti; art. 24 qualificato come transitorio e non fondativo â€” PASS.
- Hash IRPEF/IRES HEAD/finale identici â†’ PASS.
- `git diff --check -- <capitolo>` â†’ output vuoto, PASS.
- SPEC COMPLIANCE: PASS.
- QUALITY: PASS.

## Diffstat

Diff coordinato dei capitoli 4 e 6: `2 files changed, 132 insertions(+), 43 deletions(-)`. Dettaglio: capitolo 4 `1+/1-` (una riga di integrazione per il link/anchor); capitolo 6 `131+/42-`. Il report Ã¨ un file nuovo. Nessun commit eseguito.

## Note tecniche pregresse

`apply_patch` era stato bloccato dal wrapper Windows; il fallback Ã¨ rimasto chirurgico e circoscritto agli heading IVA/adempimenti. Il richiamo `LocalAgentMemory` era stato bloccato dall'assenza del runner `tsx` (`ENOTCACHED`); non Ã¨ stata creata memoria parallela.


## Cap. 4 integration diff
```diff
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
index a807f0b..9f204ba 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
@@ -449,21 +449,21 @@ La diretta applicabilita del regolamento, l'attuazione della direttiva e l'event
 | Termine di attuazione | Il termine assegnato allo Stato e' scaduto e la direttiva non e' stata attuata, oppure e' stata attuata in modo inadeguato rispetto alla disposizione considerata? |
 | Dimensione verticale | La disposizione e' invocata nei confronti dello Stato o di un soggetto riconducibile allo Stato secondo i criteri del diritto UE? |
 | Limite orizzontale | La direttiva, da sola, non puo' imporre obblighi a un altro soggetto privato in una controversia tra privati. |
 
 Queste condizioni non autorizzano automatismi. Occorre identificare la disposizione, il destinatario della pretesa e il rapporto concreto; vanno inoltre considerati primato e interpretazione conforme. Prima della pubblicazione o dell'uso su una fattispecie reale resta necessaria una review giuridica specifica.
 
 ### IVA armonizzata: direttiva europea e D.P.R. 633/1972
 
 La direttiva 2006/112/CE costruisce il sistema comune dell'IVA: operazioni rilevanti, soggetti passivi, fatto generatore, esigibilita, base imponibile, detrazione, obblighi e regimi speciali appartengono a un'architettura armonizzata. Il D.P.R. 633/1972 resta la disciplina nazionale di attuazione da applicare nel quadro della direttiva. Non e' una fonte isolata dal diritto UE, ma neppure una semplice copia che il candidato possa ignorare.
 
-Il metodo corretto e' tripartito: individua l'istituto armonizzato, ricerca la disposizione unionale pertinente, poi verifica la norma nazionale che lo attua. Per presupposti, operazioni, rivalsa, detrazione e liquidazione prosegui con [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#IVA: la mappa essenziale]].
+Il metodo corretto e' tripartito: individua l'istituto armonizzato, ricerca la disposizione unionale pertinente, poi verifica la norma nazionale che lo attua. Per presupposti, operazioni, rivalsa, detrazione e liquidazione prosegui con [[books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni#Operazioni IVA e ciclo degli adempimenti]].
 
 ### Il sistema doganale multilivello
 
 Il Regolamento (UE) n. 952/2013 istituisce il Codice doganale dell'Unione e fissa il quadro generale su merci, soggetti, decisioni, dichiarazioni, controlli, classificazione, origine, valore, obbligazione doganale e regimi. Il Regolamento delegato (UE) 2015/2446 integra il CDU nei limiti della delega; il Regolamento di esecuzione (UE) 2015/2447 stabilisce condizioni uniformi di applicazione. I tre atti formano un sistema, ma svolgono funzioni differenti.
 
 Il diritto nazionale, compreso il D.Lgs. 141/2024, disciplina i profili rimessi allo Stato e completa il quadro negli spazi consentiti: non sostituisce il CDU e non puo' contraddirlo. Per la sequenza operativa delle procedure doganali rinvia a [[books/moduli/m-fc02-agenzie-fiscali/chapters/08-dogane-procedure-doganali-adm#1. Le fonti: prima l'Unione, poi il complemento nazionale]].
 
 ### Metodo del caso: importazione e vendita interna
 
 Una societa importa una merce da un Paese terzo e poi la vende in Italia. Il caso contiene due sequenze da tenere separate.

```

## Cap. 6 full diff
```diff
diff --git a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
index 1eab7a2..d5b07d8 100644
--- a/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
+++ b/wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/06-adempimenti-fiscali-redditi-iva-dichiarazioni.md
@@ -1,35 +1,37 @@
 ---
 id: chapter-m-fc02-adempimenti-fiscali-redditi-iva-dichiarazioni
 type: book_chapter
 title: "Adempimenti fiscali: redditi, IVA, dichiarazioni"
 status: draft
 domain: "concorsi pubblici italiani"
 topics: ["adempimenti fiscali","IRPEF","IRES","categorie reddituali","reddito d'impresa","iva","dichiarazioni fiscali","versamenti"]
 entities: ["Agenzia delle Entrate"]
-source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/adempimenti-contabilita-civile-commerciale-m-fc02.md"]
+source_refs: ["sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md","sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md","sources/adempimenti-contabilita-civile-commerciale-m-fc02.md","sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md","sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md"]
 book_refs: ["m-fc02-agenzie-fiscali"]
 confidence: 0.84
 updated_at: 2026-07-20T00:00:00+02:00
 created_at: 2026-07-01T21:00:00+02:00
 review_required: true
 canonical: true
 tags: ["book-chapter","module-code-m-fc02","professional-draft"]
 book_id: m-fc02-agenzie-fiscali
 outline_section: 6
 draft_stage: professional-draft
 module_code: M-FC02
 module_family: funzioni-centrali
 last_compiled_from:
   - wiki/sources/normativa-tributaria-tuir-iva-accertamento-m-fc02.md
   - wiki/sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18.md
   - wiki/sources/adempimenti-contabilita-civile-commerciale-m-fc02.md
+  - wiki/sources/iva-dpr-633-1972-aggiornamento-2026-07-20.md
+  - wiki/sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20.md
   - wiki/topics/diritto-tributario-concorsi-agenzie-fiscali.md
   - wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta.md
   - wiki/books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco.md
 ---
 
 # Adempimenti fiscali: redditi, IVA, dichiarazioni
 
 ## Specifica struttura madre
 
 ### Obiettivo
@@ -313,108 +315,193 @@ Classifica l'effetto, senza usare importi vigenti:
 ### Trappole e checklist operativa sui redditi
 
 - Non classificare un provento dal nome usato dalle parti: ricostruisci fonte e rapporto effettivo.
 - Non usare «occasionale» come sinonimo universale di reddito diverso.
 - Non confondere reddito di capitale e guadagno finanziario tipizzato nei redditi diversi.
 - Non equiparare utile, imponibile, incasso e liquidità.
 - Non dedurre un costo soltanto perché è contabilizzato o collegato genericamente all'impresa.
 - Non descrivere la sintesi interpretativa dell'inerenza come testo letterale dell'art. 109.
 - Verifica sempre soggetto, residenza, categoria, periodo, determinazione, regimi speciali, dichiarazione e versamento.
 
-## IVA: la mappa essenziale
+## Operazioni IVA e ciclo degli adempimenti
 
-Nell'IVA il centro è l'operazione inserita in un meccanismo documentale e contabile:
+Il [[books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta#IVA: operazioni, soggetti, detrazione e adempimenti|capitolo 4]] presenta l'IVA come imposta armonizzata sui consumi e spiega la catena rivalsa, detrazione e liquidazione. Qui quella struttura diventa un metodo per trattare la singola operazione e seguirla fino all'eventuale correzione:
 
 ```text
-operazione -> soggetto -> disciplina applicabile -> documentazione
-          -> rivalsa/detrazione -> liquidazione -> dichiarazione -> controllo
+fattispecie -> documentazione -> registrazione -> liquidazione -> dichiarazione
+-> versamento o compensazione -> controllo -> eventuale correzione
 ```
 
-L'IVA non è soltanto una percentuale sul prezzo. Occorre capire chi effettua l'operazione, in quale veste, quale trattamento si applica, come l'operazione viene documentata e come concorre alla liquidazione.
+La sequenza ordina il ragionamento, ma non rende identiche tutte le fattispecie. Regole speciali, limiti alla detrazione, inversione contabile e regimi particolari richiedono sempre la verifica della disciplina applicabile.
 
-### Presupposti e operazioni
+### 1. Cessione o prestazione: qualificare il profilo oggettivo
 
-Le domande guida sono:
+La cessione trasferisce, di regola, la proprietà o un diritto reale su un bene; la prestazione deriva da un'obbligazione di fare, non fare o permettere. Le assimilazioni e le esclusioni previste dalla legge impediscono di classificare l'operazione soltanto dal nome del contratto.
 
-- che cosa è avvenuto: cessione, prestazione, acquisto o altra operazione?;
-- chi ha effettuato l'operazione e nell'esercizio di quale attività?;
-- dove si considera effettuata secondo le regole pertinenti?;
-- l'operazione è imponibile o riceve un trattamento diverso?;
-- quale documento e quale registrazione rendono il dato conoscibile?
+**Conseguenza operativa.** La qualificazione seleziona le regole su territorialità, effettuazione e documentazione. **Esempio:** vendita di un bene e consulenza verso corrispettivo appartengono a famiglie diverse. **Errore:** chiamare prestazione qualunque fattura. **Verifica:** quale fatto economico e quale disposizione di inclusione o esclusione sostengono la qualifica?
 
-È importante distinguere un'operazione estranea al campo applicativo da un'operazione che vi rientra ma riceve un particolare trattamento. Dire genericamente che «non si paga l'IVA» cancella differenze che possono produrre conseguenze sostanziali e documentali diverse.
+### 2. Soggettività e territorialità
 
-### Rivalsa, detrazione e neutralità
+La soggettività risponde a una domanda preliminare: chi compie l'operazione agisce come soggetto passivo? Rilevano l'esercizio abituale di impresa, arte o professione e, nella nozione unionale, l'attività economica indipendente. Una vendita privata occasionale non diventa operazione IVA soltanto perché ha un prezzo; per società ed enti occorre comunque verificare la sfera in cui agiscono.
 
-In termini essenziali, il soggetto che effettua un'operazione imponibile addebita l'imposta secondo il meccanismo applicabile; chi acquista, quando ricorrono i presupposti, può detrarre l'imposta assolta sugli acquisti. La liquidazione confronta le grandezze rilevanti:
+La territorialità localizza la singola operazione. Per i **beni** si guarda alla regola pertinente alla cessione: luogo del bene e, se vi è trasporto, partenza, arrivo e specifica fattispecie. Per i **servizi** la mappa essenziale distingue:
 
-```text
-IVA sulle operazioni attive
-- IVA detraibile sugli acquisti ammessi
-= risultato della liquidazione
-```
+| Prestazione | Regola-guida da verificare | Domanda operativa |
+| --- | --- | --- |
+| B2B, verso soggetto passivo | In via generale rileva il luogo del committente. | Il cliente agisce come soggetto passivo e dove è stabilito? |
+| B2C, verso consumatore | In via generale rileva il luogo del prestatore. | Il cliente agisce da privato e dove è stabilito il prestatore? |
 
-Lo schema non sostituisce le regole su detraibilità, rettifiche, operazioni particolari o regimi speciali. Dire che l'IVA è sempre neutrale per chiunque sarebbe inesatto: la detrazione richiede condizioni e può essere limitata o esclusa.
+Le regole generali non chiudono il caso. Immobili, trasporti, accesso a eventi, ristorazione, servizi elettronici e altre fattispecie possono seguire criteri speciali. Le eccezioni vanno usate come **controllo**: prima si classifica bene o servizio e B2B o B2C; poi si domanda se la natura concreta attiva una deroga, senza imparare un repertorio scollegato.
 
-Fattura, registrazione, liquidazione e dichiarazione svolgono funzioni differenti. La fattura documenta l'operazione; la registrazione la inserisce nel sistema contabile-fiscale; la liquidazione determina il risultato periodico; la dichiarazione rappresenta i dati del periodo.
+**Conseguenza operativa.** Territorialità italiana significa applicare la disciplina interna pertinente; territorialità estera impone di verificare obblighi e debitore senza concludere automaticamente «nessun adempimento». **Esempio:** consulenza resa da un'impresa italiana a un'impresa francese che agisce come soggetto passivo: la regola-guida B2B orienta verso il luogo del committente, salva verifica di qualificazione, stabilimento ed eccezioni. **Errore:** localizzare dal domicilio di una parte o dal luogo materiale in cui il consulente scrive il parere. **Verifica:** è bene o servizio, il cliente agisce B2B o B2C, qual è la regola generale e ricorre un'eccezione?
+
+### 3. Le quattro classi di operazioni
+
+| Classe | Inquadramento | Conseguenza essenziale |
+| --- | --- | --- |
+| Imponibile | Ricorrono i presupposti e si applica il regime ordinario. | L'imposta è addebitata secondo le regole applicabili e confluisce nella liquidazione. |
+| Non imponibile | L'operazione è nel sistema IVA, ma la legge non applica l'imposta, spesso secondo la logica della destinazione. | In linea generale conserva il diritto a detrazione, da verificare sulla fattispecie. |
+| Esente | L'operazione rientra nel campo IVA e beneficia di un'esenzione tipizzata. | Può limitare la detrazione sugli acquisti; non equivale a non imponibilità. |
+| Esclusa o fuori campo | Manca un presupposto oppure una norma sottrae la fattispecie al campo applicativo. | Non va trattata come operazione esente; restano da verificare gli obblighi propri del caso. |
 
-## Dichiarazione, liquidazione e versamento
+Le somme escluse dal computo della base imponibile non costituiscono automaticamente una quinta classe. **Errore comune:** dire soltanto «senza IVA». **Verifica:** l'operazione è dentro o fuori dal campo e, se è dentro, quale trattamento riceve?
 
-### Dichiarazione e documentazione
+### 4. Effettuazione ed esigibilità
 
-La dichiarazione fiscale rappresenta dati, elementi e risultati rilevanti secondo la disciplina del tributo. Non crea necessariamente il fatto imponibile, che trova fondamento nella legge; rende però la posizione conoscibile e consente i meccanismi di liquidazione e controllo.
+Il momento di effettuazione colloca l'operazione nel tempo secondo regole differenziate; fatturazione o pagamento possono assumere rilievo anticipato nei casi previsti. L'esigibilità indica quando l'Erario può pretendere l'imposta. I concetti sono collegati, ma non sovrapponibili.
 
-La documentazione sostiene ciò che viene rappresentato. Scritture, fatture, certificazioni e altri documenti collegano il dato alla sua origine. Un dato fiscale affidabile deve poter essere ricostruito.
+**Conseguenza operativa.** Il momento rilevante governa documentazione e periodo di liquidazione. **Esempio:** non si estende automaticamente a una prestazione la regola temporale propria di una cessione. **Errore:** assumere che data del contratto, consegna, fattura, pagamento ed esigibilità coincidano sempre. **Verifica:** quale evento rende effettuata la specifica operazione e quando diviene esigibile l'imposta?
 
-La dichiarazione non prova, da sola, che ogni importo sia corretto o pagato. Allo stesso modo, un versamento non dimostra che ogni obbligo dichiarativo sia stato assolto.
+### 5. Base imponibile e aliquota
 
-### Liquidazione e versamento
+La base imponibile muove dal corrispettivo complessivo e comprende gli elementi accessori indicati dalla disciplina. Le somme escluse dal computo devono ricadere in una previsione pertinente. L'aliquota è la misura applicata alla base, non il punto di partenza del caso.
 
-Liquidare significa determinare il risultato applicando le regole ai dati. Non significa svolgere un accertamento sostanziale. Il versamento è invece l'esecuzione monetaria dell'obbligazione e può riferirsi a saldo, acconti, ritenute o altri titoli previsti.
+**Conseguenza operativa.** Prima si ricostruiscono corrispettivo, accessori ed esclusioni; soltanto dopo si individua l'aliquota vigente. **Esempio:** una spesa accessoria non sparisce dalla base perché esposta separatamente. **Errore:** applicare una percentuale a un importo non qualificato. **Verifica:** quali componenti formano la base e quale fonte vigente sostiene l'aliquota?
+
+### 6. Rivalsa, detrazione e liquidazione
+
+La rivalsa riguarda l'addebito dell'imposta al cliente; la detrazione riguarda l'imposta dovuta o assolta sugli acquisti. La detrazione richiede attività economica, destinazione a operazioni che attribuiscono il diritto, documento e registrazione richiesti e assenza di limiti specifici. Non è un rimborso né una compensazione automatica.
+
+```text
+IVA sulle operazioni attive - IVA detraibile sugli acquisti ammessi
+= debito o eccedenza della liquidazione
+```
 
-Per risolvere un caso chiediti quale somma è dovuta, chi deve pagarla, a quale periodo si riferisce e se il dato è coerente con dichiarazione e documentazione. Versare non corregge automaticamente un dato dichiarativo errato; dichiarare non equivale a pagare.
+**Esempio pedagogico:** IVA attiva 1.200 e IVA detraibile 700 producono un saldo di 500; i valori allenano il calcolo e non rappresentano aliquote, soglie o parametri vigenti. **Errore:** sottrarre tutta l'IVA sugli acquisti senza verificarne il diritto. **Verifica:** quali acquisti sono documentati, inerenti e destinati a operazioni con diritto a detrazione?
 
-### Compensazione e correzione degli errori
+### 7. Documento, registri e liquidazione
 
-La compensazione consente, nel perimetro stabilito dalla legge, di utilizzare crediti per assolvere debiti. Non è una cancellazione informale: richiede esistenza e utilizzabilità del credito, corretta individuazione del debito e rispetto delle modalità applicabili.
+La fattura o il documento previsto descrive l'operazione e consente di collegare parti, oggetto, momento, base e imposta. Le operazioni attive documentate alimentano il **registro delle fatture emesse** o, quando applicabile, quello dei corrispettivi: l'imposta esigibile concorre al debito del periodo. Le fatture di acquisto confluiscono nel **registro degli acquisti**: l'imposta non diventa detraibile per la sola annotazione, ma soltanto se esistono diritto, documento e condizioni di esercizio.
 
-Gli errori possono riguardare dato, qualificazione, calcolo, omissione o pagamento. Lo strumento di correzione dipende dal tipo di errore, dal momento in cui viene rilevato e dalla disciplina vigente:
+Alla chiusura del periodo, la liquidazione riconcilia registri e documenti:
 
 ```text
-qual è l'errore? -> dove produce effetto? -> quando viene rilevato?
--> quale strumento prevede la disciplina vigente?
+imposta esigibile dalle operazioni attive registrate
+- imposta sugli acquisti ammessa in detrazione
+= debito da versare oppure eccedenza da gestire
 ```
 
-In prova è preferibile spiegare questa logica senza improvvisare termini, sanzioni o scadenze.
+**Esempio proprio, con valori pedagogici.** Il registro vendite espone imposta esigibile per 900; il registro acquisti espone 500, ma 80 riguardano un acquisto per il quale, nell'ipotesi, manca il diritto a detrazione. La detrazione ammessa è 420 e la liquidazione produce un debito di 480. Sottrarre tutti i 500 genererebbe un errore di detrazione; omettere una fattura attiva ridurrebbe invece il debito in modo indebito.
+
+**Percorso di soluzione.** Per ogni scostamento: risalire dal registro al documento; verificare momento ed esigibilità; correggere l'annotazione secondo la disciplina; riliquidare; valutare gli effetti su comunicazione, dichiarazione e pagamento. **Errore:** credere che fattura, registro e liquidazione siano duplicati dello stesso atto. **Verifica:** quale registro alimenta il debito, quale annotazione sostiene la detrazione e il saldo si riconcilia con i documenti?
+
+### Caso IVA completo
+
+**Fatti determinati.** Alfa S.r.l., stabilita a Bologna, presta a Beta S.p.A., soggetto passivo stabilito a Milano, un servizio ordinario di consulenza utilizzato nell'impresa. Il lavoro è ultimato il 12 marzo; Alfa emette fattura lo stesso giorno. Il corrispettivo pattuito è 4.000, oltre a 200 per spese accessorie contrattualmente addebitate. Per evitare dati mobili, si indica con **t** l'aliquota vigente da verificare alla data dell'operazione. Nel medesimo periodo Alfa riceve da Gamma S.r.l. una fattura per un acquisto inerente di 1.500 più imposta pedagogica di 300; documento e registrazione sono regolari e si assume, ai soli fini dell'esercizio, che l'imposta sia integralmente detraibile. Le altre operazioni del periodo generano imposta a debito pedagogica di 700.
+
+**Soluzione applicata.** (1) Alfa e Beta agiscono come soggetti passivi; si tratta di servizio B2B. (2) La regola-guida localizza la prestazione presso il committente: Milano, quindi Italia, non emergendo eccezioni dai fatti. (3) La prestazione è imponibile nell'ipotesi. (4) Per la prestazione ordinaria nazionale, la sola ultimazione del 12 marzo non basterebbe, secondo la regola generale, a determinare l’effettuazione: la fattura emessa nello stesso giorno anticipa invece il momento di effettuazione per l’importo fatturato. Su questa base si collocano operazione ed esigibilità nel periodo, ferma la verifica di eventuali regole speciali. (5) La base pedagogica è 4.200, perché le spese accessorie addebitate partecipano al corrispettivo; l'imposta è **4.200 × t**, senza attribuire a **t** un valore mobile. (6) Alfa esercita la rivalsa in fattura e registra l'operazione tra le vendite, alimentando il debito. (7) La fattura Gamma, registrata e relativa all'acquisto inerente, alimenta la detrazione per 300 nell'ipotesi. (8) La liquidazione pedagogica è **700 + (4.200 × t) - 300**. Il risultato positivo è debito; se fosse negativo sarebbe eccedenza, non rimborso automatico.
+
+**Controllo finale.** Se Alfa omettesse la fattura dal registro vendite, dovrebbe riallineare documento, registrazione, liquidazione, eventuale comunicazione/dichiarazione e pagamento con gli strumenti vigenti. Il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale#Dal dato al controllo|capitolo 5]] tratta il controllo; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05a-sanzioni-amministrative-reati-tributari|capitolo 5A]] le sanzioni; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/05b-tutela-processo-tributario|capitolo 5B]] la tutela; il [[books/moduli/m-fc02-agenzie-fiscali/chapters/07-riscossione-nazionale-lavoro-ader#2. Accertamento e riscossione: la separazione essenziale|capitolo 7]] la riscossione.
+
+### Caso comparativo: quattro operazioni, quattro esiti
+
+Classifica: vendita interna imponibile; esportazione che soddisfa i requisiti di non imponibilità; prestazione sanitaria compresa nell'esenzione tipizzata; prestazione priva di territorialità italiana. La soluzione non è «tutte senza IVA»: la prima applica l'imposta; la seconda resta nel sistema e, in linea generale, conserva la detrazione; la terza può limitarla; la quarta è fuori dal campo territoriale italiano. Requisiti e documenti vanno verificati nel caso concreto.
+
+## Dichiarazioni, versamenti e compensazioni
+
+### Dichiarazione originaria, correttiva, integrativa e omessa
+
+L'**originaria** è la prima dichiarazione validamente presentata per il periodo. Se ne viene trasmessa un'altra entro il termine ordinario, la qualificazione come **correttiva nei termini** e le modalità di sostituzione dipendono anche dalle istruzioni del modello vigente: non basta il nome scelto dal contribuente. Dopo il termine ordinario, l'**integrativa** corregge errori od omissioni nei limiti temporali, sostanziali e procedurali di legge.
+
+Una dichiarazione inviata entro la finestra che la legge considera **tardiva ma valida** resta dichiarazione presentata, ferma la disciplina della tardività. Oltre quella finestra è **omessa**; l'invio successivo può rilevare per gli effetti espressamente previsti, ma non converte automaticamente l'omissione in presentazione tempestiva o tardiva valida.
+
+La correzione può essere **a sfavore** del contribuente, quando emerge maggiore debito o minore credito, oppure **a favore**, quando emerge minore debito o maggiore credito. In entrambi i casi vanno verificati termini, prova, utilizzabilità del credito, effetti sui versamenti e strumento vigente: «integrativa» non significa credito immediatamente spendibile.
+
+**Caso 1.** Alfa scopre un ricavo omesso quando il termine ordinario è ancora aperto: consulta le istruzioni del modello e presenta la dichiarazione sostitutiva qualificata come correttiva, poi riallinea il pagamento. **Caso 2.** Lo stesso errore emerge dopo il termine: valuta un'integrativa a sfavore e la regolarizzazione. **Caso 3.** Un costo è stato duplicato e ha prodotto un credito apparente: anche se la correzione elimina il credito, occorre verificare se esso sia già stato usato. **Caso 4.** Un costo spettante era stato omesso: l'integrativa a favore non rende automatici compensazione o rimborso.
+
+### Versamento unitario e quadro temporale
+
+Il versamento unitario consente mediante F24 pagamenti e compensazioni riferiti ai tributi e contributi ammessi. Il modello organizza debiti, crediti e saldo; non crea il credito e non prova da solo la correttezza della dichiarazione. **Al 20 luglio 2026, per il percorso descritto sono vigenti gli artt. 17-20 e le altre disposizioni pertinenti del D.Lgs. 241/1997; l’art. 24 ha natura transitoria e non costituisce il fondamento del modello F24. Il D.Lgs. 33/2025 costituisce il futuro testo unico applicabile dal 1° gennaio 2027.** Codici, canali e specifiche restano dati mobili da verificare.
+
+### Compensazione: gate in sei controlli
+
+Prima di utilizzare un credito si verificano nell'ordine: **esistenza**, cioè formazione documentabile; **spettanza**, cioè fondamento sostanziale; **disponibilità**, cioè maturazione e possibilità di utilizzo; **perimetro**, verticale nello stesso tributo oppure orizzontale tra debiti e crediti ammessi; **cause ostative**, limiti o blocchi riferiti al contribuente e al credito; **controlli e modalità**, inclusi, quando richiesti, dichiarazione preventiva, visto, canale telematico e presentazione dell'F24. Un credito esposto non supera da solo questi gate.
+
+**Scenario risolto A — verticale.** Debito IVA pedagogico 900 e credito IVA disponibile 600: verificati i sei gate, 600 sono usati nello stesso tributo e resta 300. Se il credito è soltanto contabilizzato ma non disponibile, il calcolo è aritmeticamente possibile ma l'uso non è ammesso.
+
+**Scenario risolto B — orizzontale.** Credito IVA pedagogico 600 e debito contributivo ammesso 400: l'uso di 400 è orizzontale solo dopo verifica di spettanza, disponibilità, limiti, cause ostative e canale; residuano 200. Se manca un adempimento preventivo richiesto, non si procede confidando nella successiva correzione.
+
+### Credito IVA: riporto, compensazione e rimborso
+
+Un'eccedenza detraibile può essere **riportata** ai periodi successivi secondo le regole, mantenendola nel circuito IVA; può essere **compensata**, verticalmente o orizzontalmente, se esistente, spettante, disponibile e utilizzabile; può essere chiesta a **rimborso** soltanto nei casi e alle condizioni previsti, mediante il relativo percorso dichiarativo e di controllo. Sono tre destinazioni diverse: il saldo a credito non genera automaticamente denaro né libertà di scelta illimitata.
+
+**Percorso prudente.** Riconciliare origine e dichiarazione del credito; verificare presupposti della destinazione scelta; controllare limiti, garanzie, visto e cause ostative eventualmente applicabili; usare il canale vigente; conservare la prova; monitorare controlli ed eventuali rettifiche.
+
+### Errore e correzione
+
+Si identifica il fatto, si localizza l'effetto in documento, registro, liquidazione, dichiarazione o pagamento, si stabilisce quando emerge e si sceglie lo strumento vigente. Un versamento carente può richiedere pagamento e regolarizzazione; un versamento eccedente non produce automaticamente rimborso. Correzione dichiarativa, recupero del credito e regolarizzazione del pagamento sono percorsi coordinati ma distinti.
+
+### Quiz ragionati e risposta alla commissione
+
+**1. Un'operazione esente è fuori campo?** No: rientra nel campo IVA ma riceve un'esenzione tipizzata.
+**2. Rivalsa e detrazione coincidono?** No: la prima è addebito al cliente, la seconda è il diritto, esercitato alle condizioni di legge, di sottrarre dall'imposta dovuta quella assolta o dovuta sugli acquisti ammessi.
+**3. La correttiva è sempre un'integrativa?** No: conta se il termine ordinario è ancora aperto.
+**4. Un credito dichiarato è sempre compensabile?** No: vanno verificati esistenza, disponibilità, limiti e modalità.
+
+**Domanda.** Descriva il ciclo degli adempimenti IVA e il raccordo con dichiarazione e pagamento.
+**Risposta modello.** Si qualifica la fattispecie verificando operazione, soggetto, territorialità e trattamento; si individuano effettuazione, esigibilità, base e aliquota; quindi si documenta e registra. La liquidazione confronta imposta a debito e detraibile. La dichiarazione rappresenta annualmente dati e risultanze, mentre versamento, compensazione o rimborso seguono presupposti propri. Controllo, sanzione, tutela e riscossione appartengono a fasi successive e a sedi distinte.
+
+### Domande-trappola, errori e checklist
+
+- «Non imponibile» ed «esente» significano la stessa cosa? No.
+- Un F24 a saldo zero è irrilevante? No: modalità e obblighi di presentazione vanno verificati.
+- Pagare corregge automaticamente la dichiarazione? No.
+- Una dichiarazione oltre il termine ordinario è sempre integrativa valida? No.
+
+**Errori frequenti:** partire dall'aliquota; confondere art. 15 e operazione fuori campo; considerare neutrale l'IVA in assoluto; detrarre senza condizioni; confondere credito IVA, rimborso e compensazione; scegliere la correzione senza verificare la data.
+
+**Checklist:** ho qualificato operazione, soggetto e territorio; distinto le quattro classi; verificato effettuazione, esigibilità, base e aliquota; separato rivalsa e detrazione; riconciliato documento, registro, liquidazione e dichiarazione; qualificato la dichiarazione; verificato credito, debito e modalità; instradato controllo, sanzione, tutela e riscossione ai capitoli responsabili.
+
+**Diario degli errori:** registra in quattro colonne: fatto; passaggio saltato; regola corretta; prova di recupero. Una voce utile è «ho detto esente invece di fuori campo; non ho verificato i presupposti; ripasso le quattro classi; riclassifico quattro casi senza appunti».
 
 ## Servizi fiscali e rapporto con il contribuente
 
 Gli adempimenti sono anche un problema di servizio pubblico. I servizi fiscali consentono di consultare dati, trasmettere dichiarazioni e istanze, ricevere comunicazioni e correggere anomalie attraverso i canali previsti.
 
 Il funzionario deve identificare la richiesta, verificare competenza e identità, spiegare il percorso, indicare i documenti necessari e lasciare traccia dell'attività quando previsto. Non può sostituirsi al contribuente nelle scelte che non competono all'ufficio o anticipare l'esito di un controllo.
 
 | Situazione | Condotta corretta | Rischio da evitare |
 | --- | --- | --- |
 | Dichiarazione confusa con pagamento | Verificare separatamente i due adempimenti. | Rispondere soltanto «risulta pagato». |
 | Documento mancante | Spiegare quale dato deve essere comprovato. | Anticipare l'esito del controllo. |
 | Anomalia nei dati | Identificare fonte, periodo e percorso di chiarimento. | Trattarla come evasione provata. |
 | Richiesta sulla riscossione | Distinguere la fase e indirizzare correttamente. | Confondere Agenzia delle Entrate e AdER. |
 
 Assistenza e controllo non sono alternativi: una comunicazione chiara favorisce l'adempimento spontaneo, mentre legalità e imparzialità assicurano il corretto trattamento delle posizioni.
 
 ## Da sapere in 5 righe
 
-1. L'adempimento fiscale è una sequenza di qualificazione, documentazione, dichiarazione, liquidazione e pagamento.
-2. Le imposte sui redditi partono da soggetto, categoria, periodo e regole di determinazione.
-3. L'IVA si studia attraverso operazione, soggetto, rivalsa, detrazione e liquidazione.
-4. Dichiarazione, versamento, controllo e riscossione sono momenti distinti.
-5. Compensazione e correzione degli errori richiedono presupposti e regole vigenti.
+1. Si parte dalla fattispecie e dalla sua qualificazione: fatto, soggetto, tributo e trattamento applicabile.
+2. La fattispecie qualificata conduce alla documentazione e poi alla registrazione nei registri pertinenti.
+3. Dai registri si passa alla liquidazione e, successivamente, alla dichiarazione dei dati e delle risultanze.
+4. Il saldo conduce al versamento oppure, quando ne ricorrono i presupposti, alla compensazione.
+5. Seguono il controllo e, se emerge un errore, l'eventuale correzione con lo strumento vigente.
 
 ## Caso guidato
 
 Una piccola società presta servizi e riceve fatture per acquisti inerenti all'attività. Al termine del periodo emergono tre problemi: una fattura attiva non è stata inserita correttamente nella liquidazione IVA; un costo è stato classificato senza verificarne il trattamento ai fini del reddito; il versamento non coincide con il risultato ricostruito.
 
 **Primo:** separare i tributi. L'operazione attiva entra nel circuito IVA: soggetto, operazione, documento, registrazione e liquidazione. Il costo entra nel circuito delle imposte sui redditi: natura del componente, periodo, regola di determinazione e incidenza sulla base imponibile.
 
 **Secondo:** ricostruire i dati dai documenti. Non si parte dalla somma versata per dedurre ciò che avrebbe dovuto essere dichiarato.
 
 **Terzo:** ricalcolare. Per l'IVA si ricostruiscono le operazioni e il risultato della liquidazione; per il reddito si verifica il trattamento del componente. Solo dopo si confrontano dichiarazione e versamenti.
@@ -504,20 +591,22 @@ Trasforma la tabella in una risposta orale usando i verbi qualificare, documenta
 - Distinguo dichiarazione e versamento.
 - So spiegare compensazione e correzione senza presentarle come automatiche.
 - Non confondo controllo, accertamento e riscossione.
 - Ho svolto caso, esercizio e quiz.
 
 ## Riferimenti consolidati
 
 - [[sources/normativa-tributaria-tuir-iva-accertamento-m-fc02]]
 - [[sources/irpef-ires-categorie-reddito-impresa-aggiornamento-2026-07-18]]
 - [[sources/adempimenti-contabilita-civile-commerciale-m-fc02]]
+- [[sources/iva-dpr-633-1972-aggiornamento-2026-07-20]]
+- [[sources/dichiarazioni-versamenti-compensazioni-aggiornamento-2026-07-20]]
 - [[topics/diritto-tributario-concorsi-agenzie-fiscali]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/04-diritto-tributario-teoria-imposta]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/11-contabilita-aziendale-economia-impresa-fisco]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/05-accertamento-controlli-compliance-fiscale]]
 - [[books/moduli/m-fc02-agenzie-fiscali/chapters/07-riscossione-nazionale-lavoro-ader]]
 
 ## Note di review
 
 - Sottoporre a review normativa articolo per articolo la trattazione IRPEF/IRES, con particolare attenzione a regimi speciali, derivazione rafforzata, imputazione e singole deducibilità.
 - I numeri del caso IRES sono esclusivamente pedagogici e non rappresentano aliquote, soglie, limiti o parametri vigenti.

```