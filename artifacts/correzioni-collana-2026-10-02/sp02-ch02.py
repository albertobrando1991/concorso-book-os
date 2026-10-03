from pathlib import Path
import re
p=Path('wiki/books/moduli/m-sp02-vigili-fuoco/chapters/02-la-tua-posizione-prima-della-domanda.md');t=p.read_text(encoding='utf8')
arc=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp02-02.md')
if not arc.exists():arc.write_text(t,encoding='utf8')
def rep(a,b):
 global t
 assert a in t,a[:100]
 t=t.replace(a,b)
def span(a,b,v):
 global t
 i=t.index(a);j=t.index(b,i);t=t[:i]+v+'\n\n'+t[j:]
rep('Non serve a studiare: serve a rispondere, prima di investire mesi, a due domande diverse che il candidato tende a confondere.','Insegna a distinguere, prima di investire mesi, due domande che richiedono verifiche diverse.')
rep('La seconda è **contro chi concorri**: in quale quota rientri, e quanti posti ha quella quota.','La seconda riguarda **le riserve**: quale beneficio puoi dichiarare e come si combina con la graduatoria di merito.')
rep('Sono due verifiche distinte, e sbagliare la seconda costa quanto sbagliare la prima. Cominciamo da lì, perché è quella che quasi nessuno fa.','L’assenza di una riserva non equivale alla mancanza di un requisito di ammissione. Partiamo dalle quote per separare subito i due piani.')
rep('**misurare in autonomia** i parametri che puoi misurare — forza di presa, composizione corporea, visus, udito — prima di investire mesi di preparazione.','comprendere unità, soglie e limiti delle misurazioni di forza di presa, composizione corporea, visus e udito, distinguendo la valutazione preliminare dall’accertamento concorsuale.')
rep('quale dei tre regimi di idoneità','quale regime di idoneità')
rep('In questo capitolo il metodo BANDO serve a produrre una decisione, non una conoscenza: alla fine devi avere un foglio con date e numeri tuoi.','La conoscenza delle regole deve tradursi in una scheda con condizioni, termini e documenti; le informazioni sanitarie restano affidate agli accertamenti competenti.')
rep('Su quattrocento posti, significa centottanta, centoquaranta e sessanta. Al candidato che non possiede nessuno dei tre titoli restano **venti posti**.','Su quattrocento posti, le quote nominali valgono centottanta, centoquaranta e sessanta: il residuo è **venti posti non riservati**. Non sono venti posti garantiti esclusivamente a chi non possiede riserve: anche un riservatario può collocarsi utilmente per merito.')
span('Non è un\'ipotesi teorica.','**Seconda: la riserva va dichiarata.**','''Le quote non sono tre concorsi chiusi con probabilità ricavabili dividendo i posti per la percentuale. Il risultato dipende da idonei, punteggi, appartenenza alle categorie e applicazione delle riserve. Conoscere soltanto il numero delle domande non permette di prevedere quanti posti saranno devoluti.

Un esempio aritmetico chiarisce il meccanismo senza simulare una graduatoria completa: se dieci dei centoquaranta posti della riserva del 35% non sono coperti, quei dieci sono attribuiti agli altri idonei secondo l’ordine di graduatoria. Il residuo nominale iniziale di venti aumenta di dieci posti non più vincolati a quella riserva. Non segue che trenta candidati privi di ogni riserva saranno necessariamente assunti: l’attribuzione concreta richiede la graduatoria e le regole applicabili.

La conseguenza utile è duplice. Non rinunciare per il solo dato del 95%; non trasformare il residuo in una promessa di assunzione. Il punteggio e il superamento di tutte le fasi rimangono essenziali anche quando possiedi un titolo di riserva.''')
rep('concorre nella quota libera, cioè contro il numero più piccolo.','non può fondare il beneficio sulla sola esistenza del titolo. Possesso e dichiarazione tempestiva vanno verificati separatamente.')
rep('**i parametri e le soglie sono differenziati per sesso** in tutte le prove motorio-attitudinali e nei parametri fisici del d.P.R. 207/2015.','**diversi parametri e soglie sono differenziati per sesso**, fra cui quelli del d.P.R. 207/2015 e quelli di corsa e nuoto; non ogni modulo ha una distinzione, come mostra la trave.')
rep('Per un civile che scopre il concorso a ventidue o ventitré anni, questa via è di fatto impraticabile: dodici mesi di servizio effettivo più i tempi di arruolamento non stanno dentro la finestra residua.','A ventidue o ventitré anni non si può dichiarare la via impraticabile per semplice sottrazione: dodici mesi possono maturare prima del venticinquesimo compleanno. Occorre però aggiungere i tempi effettivi di selezione e arruolamento e confrontarli con la scadenza del bando VVF. Un progetto futuro non costituisce il titolo da dichiarare nella domanda attuale.')
rep('Mettendo insieme i due dati si ottiene una conclusione che non è scritta in nessuna pagina del bando: **per chi ha superato i ventisei anni, il volontariato nel Corpo non è una scorciatoia, è spesso l\'unica porta rimasta**. E per chi ne ha venti, è un investimento che apre una quota del trentacinque per cento invece del cinque.','I due benefici sono distinti: **un anno di iscrizione** rileva per il limite di età; **tre anni e 120 giorni** per la riserva. Per chi ha compiuto ventisei anni va verificata anche l’elevazione per servizio militare effettivo, fino a tre anni. Non esiste una conclusione valida per tutti basata sulla sola età.')
rep('È la quota più piccola delle tre, ed è anche **la più accessibile a un civile che parte da zero**.','È la quota nominale più piccola delle tre. Accessibilità e tempi dipendono dal percorso di servizio e non si deducono dalla percentuale.')
rep('Sessanta posti su quattrocento, contro i venti della quota libera.','La quota nominale è di sessanta posti su quattrocento; non è un confronto fra probabilità individuali di successo.')
span('> **Attenzione.** Nessuna delle tre vie','### Caso guidato:','''> **Attenzione.** Le condizioni devono maturare entro la scadenza pertinente, non necessariamente prima della pubblicazione. Un servizio già in corso può concludersi mentre il bando è aperto. Una promessa di conclusione successiva alla scadenza non vale come requisito già posseduto.

### Tre date da mettere sul calendario

Per ogni percorso annota la data di inizio, la data di maturazione della condizione e la scadenza concorsuale. Aggiungi il compleanno rilevante quando è previsto un limite anagrafico. Il calcolo non può partire dalla sola età espressa in anni interi.

| Situazione | Verifica decisiva |
| --- | --- |
| Ferma prefissata in corso | Dodici mesi conclusi e meno di 25 anni entro la scadenza della riserva. |
| Volontario VVF da un anno | Limite speciale di età; non ancora riserva del 35% per il solo anno. |
| Volontario VVF da tre anni | Verificare anche almeno 120 giorni di servizio e dichiarazione. |
| Servizio civile in corso | Conclusione senza demerito entro la scadenza, non semplice avvio. |
| Età oltre il limite ordinario | Verificare effettivo servizio militare e limite speciale VVF; nessuna deroga si presume. |

Esempio didattico: il termine è il 3 agosto; il servizio civile termina il 20 luglio. La condizione può maturare durante l’apertura della procedura, se il servizio si conclude senza demerito e viene dichiarato correttamente. Se termina il 20 agosto, non è posseduta entro quel termine. Per il volontario VVF, due anni e undici mesi di iscrizione al giorno della scadenza non diventano tre anni perché la prova si terrà più avanti. Il termine del titolo di riserva e il calendario della prova assolvono funzioni differenti.

Conserva il documento da cui ricavi ogni data. Una scheda con «riserva sì» senza indicazione della condizione e della sua maturazione non è ancora una verifica.''')
span('### Caso guidato:','## N-SP02-03-01','''### Caso guidato: ventinove anni e un dato sul visus

Marco ha ventinove anni, un diploma, nessun servizio militare e nessuna iscrizione come volontario VVF. Il suo visus naturale, misurato l’anno scorso, era 12/10 complessivi. Il bando chiude fra tre settimane.

La prima conclusione è documentale: non rientra nel limite ordinario e non possiede le condizioni per le elevazioni descritte. Iscriversi adesso agli elenchi non fa maturare un anno entro tre settimane. Non deve dichiarare come posseduto un requisito futuro.

Per un’eventuale tornata successiva, l’iscrizione e la sua durata andrebbero valutate secondo le regole allora vigenti, insieme agli altri requisiti. Non è garantito che un futuro bando ripeta le stesse condizioni o che Marco acquisisca l’idoneità necessaria.

Il dato di 12/10 naturali è inferiore alla somma richiesta per vigile, ma non autorizza una prognosi permanente. Non dimostra neppure idoneità a ispettore antincendi o vice direttore: per questi ruoli la correzione è ammessa entro limiti specifici e vanno accertati anche il valore dell’occhio peggiore, campo visivo, visione binoculare, motilità e gli altri requisiti. La scelta di un corso di laurea non va fondata sulla presunta equivalenza «occhiali ammessi, quindi idoneo».

L’output corretto è una scheda con tre esiti distinti: requisito anagrafico non soddisfatto per il bando attuale; eventuale percorso futuro da verificare; situazione sanitaria da approfondire con il professionista e poi con l’accertamento concorsuale. Il libro non attribuisce un costo standard alla visita né la usa come sostituto del giudizio della commissione.''')
rep('I requisiti documentali si verificano una volta e si archiviano. L\'idoneità si mantiene.','I documenti attestano condizioni riferite a termini precisi e vanno conservati; variazioni successive rilevanti non si ignorano. L’idoneità segue gli accertamenti e la permanenza prescritti.')
rep('Per chi ha passato i ventisei anni, spesso è l\'unica strada che resta aperta.','La verifica deve comunque considerare anche l’effettivo servizio militare, senza confondere il limite speciale con una riserva di posti.')
span('Nota la formulazione della seconda voce:','## N-SP02-03-02','''La seconda voce richiede una sentenza irrevocabile per delitto non colposo: un procedimento pendente non è automaticamente quella specifica causa. Ma sarebbe sbagliato ridurre tutto l’accertamento a questa domanda. Restano le altre cause elencate e il distinto requisito delle qualità morali e di condotta. Un caso dubbio richiede l’esame della situazione concreta e della disciplina applicabile; non una risposta automatica ricavata da una sola casella.

### Caso sui termini: diploma e riserva

Sara presenta domanda il 10 luglio, conclude il servizio civile senza demerito il 20 luglio e consegue il diploma il 30 settembre. Ipotizziamo una scadenza il 3 agosto e una preselettiva il 14 ottobre. Il titolo di riserva può maturare entro il termine di domanda; il diploma segue l’eccezione espressa e può essere conseguito entro la preselettiva. Sara deve rendere le dichiarazioni nella forma e nei termini previsti, aggiornando o ripresentando la domanda se necessario secondo la procedura consentita. Non può indicare il 10 luglio come già concluso un servizio ancora in corso.

Cambia un solo dato: il servizio civile termina il 20 agosto. Il diploma resta compatibile con la deroga ipotizzata, ma la riserva non è maturata alla scadenza. L’ammissibilità e il beneficio non hanno lo stesso esito. Cambia invece la data del diploma al 20 ottobre: la deroga non basta più per quella preselettiva. Questa lettura per condizioni evita di estendere un’eccezione da un requisito all’altro.

Per il controllo finale usa quattro righe: condizione richiesta; documento o dichiarazione che la prova; data di maturazione; termine da rispettare. Alla voce sanitaria non inserire «certificato uguale a idoneità»: annota gli accertamenti previsti e la competenza della commissione. Alla voce condotta non scrivere soltanto «nessuna condanna»: controlla separatamente l’intero elenco delle cause ostative e il requisito generale richiamato dal bando.''')
rep('Qui arriva la parte che quasi nessun candidato verifica prima, e che invece è la più facile da verificare.','I valori numerici aiutano a leggere il requisito; non trasformano la valutazione medico-legale in un’autocertificazione.')
rep('| **forza muscolare** | **40** | **20** |','| **forza muscolare** | **≥ 40 kg** | **≥ 20 kg** |')
rep('| **composizione corporea** | **fra 7 e 22** | **fra 12 e 30** |','| **composizione corporea** | **≥ 7% e ≤ 22%** | **≥ 12% e ≤ 30%** |')
rep('| **massa metabolicamente attiva** | **40** | **28** |','| **massa metabolicamente attiva** | **≥ 40%** | **≥ 28%** |')
span('Fermati su una cosa:','E la composizione corporea','''L’articolo 3, comma 2, del d.P.R. 207/2015 ammette un adeguamento dei valori strumentali fino al 10% rispetto ai limiti, in relazione a condizioni tecniche o individuali. Non è un bonus automatico né significa dieci punti percentuali aggiunti o sottratti liberamente. Applicazione, strumenti e accertamento seguono le direttive e la procedura competente. Una misura preliminare può orientare un confronto professionale; non sostituisce il risultato concorsuale.

Tieni distinti unità e verso della soglia: 40 kg è una forza di presa minima; 40% è un rapporto percentuale per una diversa grandezza. Per la massa grassa esistono sia un limite inferiore sia uno superiore. Una misura con apparecchio non equivalente, o senza condizioni controllate, non consente un confronto conclusivo.''')
rep('| **ispettore antincendi** e **vice direttore** | stessi valori | **ammessa** |','| **ispettore antincendi** e **vice direttore** | stessi valori | **ammessa nei limiti specifici dell’art. 1** |')
span('Stessi numeri, regola opposta.','Il decreto richiede inoltre','''La differenza riguarda la correzione, non l’automatica idoneità a un altro ruolo. Per le qualifiche in cui è consentita, l’articolo 1 pone limiti diottrici e richiede ulteriori condizioni oculari. La sola somma dei decimi non descrive l’occhio peggiore, la visione binoculare, il campo visivo o la motilità. Né il dato di oggi autorizza una previsione definitiva della situazione futura.

Perciò una valutazione oculistica preliminare può chiarire il quadro personale e il confronto con la disciplina, ma non certifica da sola l’ammissione al concorso. La verifica del titolo di studio per un diverso ruolo resta autonoma dalla verifica sanitaria.''')
rep('calcolata come media delle frequenze 500, 1000, 2000 e 3000 Hz;','calcolata come media delle frequenze 500, 1000, 2000 e 3000 Hz, e non superiore a **45 decibel** sulle frequenze 4000, 6000 e 8000 Hz; non sono ammesse protesi acustiche;')
rep('I tre regimi del d.m. 166/2019','I regimi del d.m. 166/2019')
rep('**Il criterio è funzionale e relativo alla qualifica**, non assoluto e uniforme.','**Il criterio è funzionale e relativo alla qualifica**. Non equivale ad assenza di requisiti sanitari.')
rep('un candidato escluso dai ruoli operativi per un parametro numerico può essere pienamente idoneo per un ruolo tecnico-professionale, perché quel parametro semplicemente non gli si applica.','un parametro previsto per un ruolo non si trasferisce automaticamente agli altri. L’eventuale idoneità tecnico-professionale richiede comunque la propria valutazione medico-legale, non si ricava dall’esclusione dal ruolo operativo.')
rep('È l\'unica lettura che ha senso.','Il confronto serve a comprendere il caso, mantenendo distinta la valutazione clinica dall’accertamento concorsuale.')
span('### La sequenza giusta delle verifiche','## Errori tipici','''### Una sequenza che mantiene aperti i controlli necessari

Comincia dalla scadenza e dal ruolo: sono le coordinate che stabiliscono quali condizioni verificare. Controlla subito età, titolo di studio e cause ostative; nello stesso periodo organizza gli approfondimenti sanitari pertinenti. Non esiste una regola per cui visus e udito siano sempre definitivi o si chiariscano necessariamente in un pomeriggio.

La riserva si verifica in parallelo: titolo posseduto, termine di maturazione e dichiarazione. Non attendere la visita per scoprire che manca una dichiarazione entro la scadenza, e non attendere la graduatoria per chiarire una condizione sanitaria già nota. Un elemento mancante richiede un’azione precisa e una data, non l’etichetta generica «da vedere».

Per i parametri corporei evita la formula «fuori soglia ma risolvibile». Modificabilità, tempi e sicurezza non si deducono dal numero. Un percorso personale va valutato con professionisti competenti, senza prescrizioni di dimagrimento o allenamento ricavate dalla tabella concorsuale. Il candidato deve arrivare informato agli accertamenti, non sostituirsi alla commissione.

### Scheda di controllo del caso

Scrivi su righe separate: ruolo richiesto; norma sanitaria applicabile; condizioni documentali già verificate; informazioni da approfondire; termine della domanda; documentazione richiesta per le successive convocazioni. Per ciascuna informazione sanitaria indica la data della valutazione e chi la ha eseguita. Il foglio non è un certificato: aiuta a non perdere il collegamento fra regola e passaggio successivo.

Considera due candidati con lo stesso visus naturale complessivo. Uno domanda l’accesso a vigile, l’altro a un ruolo tecnico-professionale dell’articolo 2. Sarebbe errato applicare indistintamente la tabella del primo al secondo. Sarebbe altrettanto errato dichiarare il secondo idoneo senza valutarne la capacità funzionale e le eventuali infermità rilevanti. La domanda corretta non è «questo numero basta?», ma «quale disciplina governa questo ruolo e chi deve accertare l’insieme delle condizioni?».

La stessa distinzione vale per un certificato richiesto per partecipare alla prova motoria. Quel documento consente il passaggio procedurale secondo il bando; non coincide con tutti gli accertamenti per l’accesso al ruolo. Leggi oggetto, validità e forma del certificato, senza estendere il suo effetto a ciò che non attesta.''')
span('## Errori tipici','## ▣ Verifica 02.A','''## Errori tipici

**«Venti posti sono garantiti a chi non ha riserve».** Sono il residuo nominale non riservato, da coordinare con merito e devoluzione: non una garanzia per una categoria separata.

**«Basta iscriversi come volontario».** Un anno rileva per il limite speciale di età; per la riserva occorrono tre anni e 120 giorni. Possesso e dichiarazione sono passaggi distinti.

**«Alla pubblicazione è già tutto deciso».** Una condizione può maturare mentre il bando è aperto, purché entro il termine pertinente. La data della prova non sana un requisito richiesto prima.

**«Gli occhiali mi rendono idoneo a un altro ruolo».** La correzione ammessa non esaurisce l’accertamento e non elimina i suoi limiti specifici.

**«Essere sotto il massimo basta».** Per la massa grassa esiste anche un minimo. Un risultato isolato non certifica l’idoneità complessiva.

**«Nessuna condanna irrevocabile significa condotta sicuramente conforme».** Quella è una specifica causa ostativa; vanno controllate anche le altre e il requisito generale.''')
span('## ▣ Verifica 02.A','## ▣ Verifica 02.B','''## ▣ Verifica 02.A · Quiz ragionati

**1. Quale affermazione sui venti posti nominalmente non riservati è corretta?**

A. Sono garantiti ai soli candidati privi di ogni riserva.
B. Costituiscono un residuo da coordinare con graduatoria di merito e devoluzione.
C. Sono attribuiti per sorteggio.
D. Sono sottratti al concorso se le riserve risultano coperte.

**Risposta corretta: B.** Le percentuali non creano una garanzia esclusiva per i non riservatari; A confonde quota non riservata e categoria di beneficiari. C e D introducono meccanismi non previsti.

**2. Il servizio civile si conclude senza demerito durante l’apertura del bando, prima della scadenza. Quale controllo serve?**

A. Verificare maturazione entro il termine e corretta dichiarazione.
B. Escludere il titolo perché successivo alla pubblicazione.
C. Attendere la graduatoria per dichiararlo.
D. Considerarlo acquisito già all’inizio del servizio.

**Risposta corretta: A.** Conta il termine richiesto e la dichiarazione prevista. B anticipa indebitamente il termine; C lo sposta in avanti; D scambia avvio e conclusione.

**3. Quale coppia distingue correttamente i benefici per il volontario VVF?**

A. Riserva dopo un anno, limite speciale dopo tre.
B. Entrambi alla prima iscrizione.
C. Entrambi dopo dodici mesi di servizio effettivo.
D. Limite speciale dopo un anno di iscrizione; riserva dopo tre anni e 120 giorni di servizio.

**Risposta corretta: D.** Le due condizioni hanno oggetto e tempi diversi. A le inverte, B elimina i tempi e C sostituisce requisiti non corrispondenti.

**4. Un valore di massa grassa maschile del 5%, confrontato con la tabella nominale del d.P.R. 207/2015:**

A. Soddisfa il requisito perché inferiore al 22%.
B. Diventa conforme grazie a un buon handgrip.
C. È inferiore al minimo nominale del 7%; il giudizio complessivo resta distinto.
D. Dimostra da solo la condizione sanitaria futura.

**Risposta corretta: C.** L’intervallo ha due estremi; le grandezze non si compensano. A ignora il minimo, B inventa una compensazione, D trasforma una misura in prognosi. Gli adeguamenti strumentali non sono un’autovalutazione libera.

**5. Di un candidato è noto soltanto un visus naturale complessivo di 12/10. Che cosa si può concludere?**

A. È idoneo a tutti i ruoli con gli occhiali.
B. È sotto la somma naturale richiesta per vigile; non è dimostrata l’idoneità ad altri ruoli.
C. È definitivamente escluso da ogni futura procedura.
D. È idoneo a vigile se l’occhio peggiore ha 6/10.

**Risposta corretta: B.** Il dato non soddisfa la somma richiesta, ma non descrive tutto l’accertamento. A presume l’idoneità, C una prognosi permanente e D ignora che le soglie per somma e occhio peggiore devono entrambe essere rispettate.

**6. Per un ruolo tecnico-professionale disciplinato dall’articolo 2 del D.M. 166/2019:**

A. Serve la valutazione funzionale e medico-legale propria del ruolo.
B. Non esistono requisiti sanitari.
C. Si trasferiscono automaticamente tutte le soglie dell’articolo 1.
D. L’esclusione da un ruolo operativo prova l’idoneità.

**Risposta corretta: A.** L’assenza di quella specifica tabella non elimina l’accertamento. B lo cancella, C confonde gli ambiti e D ricava un esito positivo da un dato che non lo dimostra.''')
span('## ▣ Verifica 02.B','## In sintesi','''## ▣ Verifica 02.B · Domande aperte e criteri di risposta

**1.** Calcola il residuo nominale delle riserve e spiega perché non è una promessa ai non riservatari. **Riscontro:** 400 − 180 − 140 − 60 = 20; graduatoria di merito e devoluzione impediscono di trattarlo come contingente esclusivo garantito.

**2.** A ventisette anni quali informazioni mancano per valutare l’età? **Riscontro:** data di nascita e scadenza, servizio militare effettivo, iscrizione VVF e sua durata; l’assenza di una riserva non esclude ogni elevazione.

**3.** Distingui un anno di iscrizione da tre anni e 120 giorni. **Riscontro:** il primo riguarda il limite speciale, i secondi la riserva del 35%; non sono benefici equivalenti.

**4.** Il titolo di riserva esiste ma non è dichiarato: basta il documento conservato? **Riscontro:** no, occorre anche la dichiarazione prevista entro il termine, senza presumere un recupero successivo.

**5.** Perché 12/10 naturali non dimostrano idoneità a ispettore? **Riscontro:** mancano correzione nei limiti ammessi, altri parametri oculari e restante accertamento; il titolo di studio è un ulteriore piano distinto.

**6.** Che cosa significa un intervallo 7–22%? **Riscontro:** due estremi nominali inclusi, non soltanto un massimo. La misura non è da sola un giudizio complessivo.

**7.** Distingui kg e percentuali nella tabella. **Riscontro:** forza di presa in kg; composizione e massa metabolicamente attiva espresse come percentuali delle rispettive grandezze previste.

**8.** L’articolo 2 elimina ogni verifica sanitaria? **Riscontro:** no, richiede idoneità funzionale e valutazione delle condizioni rilevanti per la qualifica.

**9.** A che cosa serve consultare il D.M. 166/2019 con il professionista? **Riscontro:** chiarire disciplina e situazione personale; non sostituire la commissione o ricavare una diagnosi da una lista.

**10.** Organizza un controllo che non faccia scadere la domanda durante un approfondimento sanitario. **Riscontro:** calendario documentale e dichiarazioni in parallelo agli approfondimenti pertinenti; nessuna autocertificazione di requisiti mancanti o presunta idoneità.''')
span('## In sintesi','*Fonti:','''## In sintesi

Riserve, requisiti di ammissione e idoneità sanitaria sono piani distinti. Le condizioni vanno riferite al termine corretto; diploma e accertamenti sanitari seguono le eccezioni previste. Un valore numerico preliminare aiuta a porre la domanda corretta, ma non attribuisce idoneità, non compensa altri requisiti e non autorizza prognosi permanenti.''')
t=t.replace('Dati verificati al 10 agosto 2026.','Dati del bando campione ricontrollati il 3 ottobre 2026.')
for old,new in [('N-SP02-03-01','N-SP02-02-03'),('N-SP02-03-02','N-SP02-02-04'),('N-SP02-03-03','N-SP02-02-05')]:t=t.replace(old,new)
t=re.sub(r'^review_required:.*$','review_required: true',t,flags=re.M);t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M)
p.write_text(t,encoding='utf8');print('SP02/02 corretto; originale archiviato')
