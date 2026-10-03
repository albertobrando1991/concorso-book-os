from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-ir02-universita-afam/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
blocks={
(6,2):'''**Tre assestamenti, tre effetti diversi.** I dati seguenti sono ipotesi di esercizio. Un'attrezzatura ordinaria da 60.000 euro, pagata e disponibile dal 1° gennaio, ha vita utile di cinque anni e valore residuo nullo. Con quota costante, l'ammortamento annuo è 60.000 / 5 = **12.000 euro**: il pagamento è 60.000, il costo annuo 12.000, il valore netto dopo il primo anno 48.000. L'ammortamento distribuisce il costo lungo l'utilità; non è un fondo di denaro accantonato. L'esempio non riguarda beni culturali, per i quali il D.I. 34/2025 esclude l'ammortamento ordinario.

Un canone annuale di 12.000 euro è pagato il 1° ottobre per il periodo ottobre-settembre. Al 31 dicembre sono maturati tre mesi: costo dell'esercizio **3.000**, risconto attivo **9.000**. Il risconto rinvia al futuro la quota già pagata che non appartiene all'esercizio. Se invece interessi di 1.200 euro per ottobre-marzo saranno pagati a marzo, al 31 dicembre si rilevano **600 euro di costo e 600 di rateo passivo**. Il rateo anticipa la rilevazione della quota maturata, con pagamento futuro. Per semplicità si assumono quote mensili uniformi e si escludono imposte, contributi e altre operazioni.

La distinzione si può ricordare chiedendosi che cosa viene prima: nel risconto viene prima il movimento monetario; nel rateo viene prima la competenza economica della quota. Non ogni debito è un rateo: questi assestamenti riguardano componenti comuni a più esercizi il cui importo varia in ragione del tempo.
''',
(6,3):'''L'art. 1 del D.Lgs. 18/2012 permette di riconoscere i documenti senza confondere bilancio unico e bilancio consolidato:

| Documento | Componenti e funzione |
| --- | --- |
| Bilancio unico annuale di previsione autorizzatorio | Budget economico e budget degli investimenti: programma e autorizza la gestione |
| Bilancio unico triennale | Budget economico e degli investimenti sul periodo pluriennale: verifica sostenibilità e indirizzi |
| Bilancio unico di esercizio | Stato patrimoniale, conto economico, rendiconto finanziario e nota integrativa; è corredato dalla relazione sulla gestione |
| Bilancio consolidato | Rappresenta il gruppo secondo il perimetro applicabile; non è sinonimo di bilancio unico dell'ateneo |

Per gli atenei ricompresi nelle amministrazioni pubbliche sono previsti anche preventivo finanziario non autorizzatorio e rendiconto finanziario destinati al raccordo con il consolidamento dei conti pubblici. L'aggettivo «non autorizzatorio» impedisce di attribuire al preventivo finanziario la funzione propria del budget autorizzatorio.

I principi e gli schemi aggiornati sono contenuti nel **D.I. MUR-MEF 34/2025**. I precedenti D.I. 19/2014, 394/2017 e 925/2015 sono stati abrogati: un quesito storico può richiamarli, mentre una risposta sul quadro corrente deve partire dal decreto del 2025. Il manuale di contabilità dell'ateneo specifica l'applicazione senza sostituire i principi nazionali.
''',
(6,5):'''**Laboratorio numerico: chiudere un prospetto semplificato.** Tempo: 20 minuti. All'inizio dell'esercizio l'ateneo presenta, limitatamente al perimetro simulato, cassa 200.000 e patrimonio netto 200.000, senza altre poste. Nell'anno incassa proventi correnti interamente di competenza per 100.000; paga personale per 70.000, l'attrezzatura da 60.000 e il canone anticipato da 12.000 descritti nel secondo nucleo. A fine anno matura il rateo passivo di 600. Non vi sono altri fatti, imposte, crediti o contributi da riscontare. Redigi un conto economico sintetico, un prospetto patrimoniale e un raccordo con la cassa.

**Soluzione.** Il conto economico espone proventi 100.000 e costi per personale 70.000, ammortamento 12.000, canone 3.000, interessi 600: risultato economico **14.400**. La cassa finale è 200.000 + 100.000 − 70.000 − 60.000 − 12.000 = **158.000**. Le attività finali sono cassa 158.000, attrezzatura netta 48.000 e risconto attivo 9.000: totale **215.000**. Il lato passivo comprende rateo passivo 600 e patrimonio netto 214.400, dato da 200.000 iniziali più il risultato di 14.400. Totale passività e patrimonio netto: **215.000**.

Il saldo monetario dell'anno è negativo per 42.000, ma il risultato economico è positivo per 14.400: l'acquisto dell'attrezzatura e il canone anticipato spiegano gran parte della differenza. Non si può dichiarare perdita soltanto perché la cassa diminuisce. Il prospetto è un esercizio di raccordo, non lo schema ministeriale completo né una registrazione pronta per qualsiasi piano dei conti.

**Valutazione, 10 punti:** 3 per competenza e assestamenti, 3 per risultato economico, 2 per cassa, 2 per quadratura patrimoniale. Attribuire tutti i 60.000 al costo dell'anno richiede di riprendere la distinzione fra investimento e costo prima di considerare superata la prova.
''',
(7,4):'''La forma del finanziamento determina che cosa occorre dimostrare. Nei grant europei possono convivere modalità diverse; la scelta è stabilita dal contratto e dai suoi allegati, non dal beneficiario dopo la spesa.

| Forma | Calcolo e controllo essenziale |
| --- | --- |
| Costi effettivi | Costi realmente sostenuti e ammissibili, riconciliabili con contabilità e giustificativi |
| Costi unitari | Unità effettive ammissibili × importo unitario; occorre provare le unità utilizzate o prodotte |
| Tasso forfettario | Percentuale × base ammissibile prevista; le esclusioni dalla base contano quanto la percentuale |
| Somma forfettaria, o lump sum | Importo definito per attività e risultati contrattuali: la verifica riguarda la loro realizzazione, secondo il grant |

**Esercizio originale.** Un avviso ipotetico riconosce 80 euro per ogni unità documentata. Su 45 unità dichiarate soltanto 42 risultano realizzate e ammissibili: 42 × 80 = **3.360 euro**, non 3.600. Un'altra categoria applica il 10% a una base definita dal contratto: di 24.000 euro complessivi, 4.000 appartengono a categorie escluse. La base è 20.000 e il forfait **2.000**, non 2.400. Percentuali e importi sono dati dell'esercizio, non tariffe universali di Horizon o PRIN.

Per una lump sum di 30.000 euro assegnata a un pacchetto di lavoro, fatture per 29.000 non dimostrano da sole che il pacchetto sia completato. Si verificano attività, risultati e condizioni contrattuali di accettazione. Un risparmio rispetto alla stima non produce automaticamente il medesimo taglio previsto per costi effettivi; restano gli obblighi etici, di integrità, documentazione e corretta attuazione. La semplificazione della rendicontazione finanziaria non elimina i controlli.

**Domanda-trappola.** È sempre necessario presentare ogni fattura per ottenere il contributo? No: dipende dalla forma di finanziamento. È però altrettanto errato rispondere che un forfait non richiede evidenze: devono essere provate almeno le condizioni e la base o le unità pertinenti. La contabilità ordinaria dell'ente continua comunque a registrare le operazioni secondo le proprie regole.
''',
(7,5):'''Una spesa non prevista nella ripartizione iniziale non è automaticamente esclusa né automaticamente ammissibile. Nel modello europeo, l'art. 5.5 del grant disciplina la flessibilità: taluni trasferimenti fra categorie o partecipanti sono ammessi senza amendment se non modificano sostanzialmente l'azione; altri cambiamenti richiedono modifica formale o approvazione specifica. Il massimo del contributo non aumenta per effetto di un trasferimento interno. Prima di decidere si leggono descrizione dell'azione, categorie, limiti e condizioni del contratto concreto.

**Decisione su dati chiusi.** Il contratto del caso consente trasferimenti fra due categorie senza modifica formale soltanto se le attività restano identiche. Il responsabile propone di spostare 5.000 euro per acquistare un'attrezzatura necessaria al lavoro già approvato; nessun limite o categoria speciale è coinvolto. L'ufficio verifica e documenta questi presupposti, la disponibilità e la regolarità della procedura, senza dedurre l'inammissibilità dalla sola assenza nella ripartizione iniziale. Se invece la stessa somma finanzia un nuovo pacchetto di attività fuori dalla descrizione approvata, il presupposto viene meno: occorre attivare il percorso di modifica e non rendicontare il nuovo lavoro come già autorizzato.
''',
(8,4):'''Una **milestone** è un traguardo qualitativo, come l'adozione di un atto o l'attivazione verificabile di un servizio; un **target** è un obiettivo quantitativo, come un numero definito di posti o risultati. L'evidenza deve corrispondere alla formulazione approvata. «È stato pagato il fornitore» non prova, da solo, che un laboratorio sia operativo o che gli utenti previsti abbiano ricevuto il servizio.

Nel dispositivo per la ripresa e la resilienza il rispetto del **DNSH è obbligatorio**: varia il modo di dimostrarlo per la misura e l'intervento, non la facoltà di ignorarlo. Si individuano requisiti pertinenti, momento della verifica ed evidenze richieste dalle istruzioni applicabili. Una dichiarazione finale generica non sostituisce controlli che dovevano accompagnare progetto, affidamento ed esecuzione.

**Fascicolo simulato.** La traccia richiede entro il 30 giugno l'attivazione di un servizio e 120 utenti distinti formati. Sono disponibili un verbale di attivazione del 28 giugno, un pagamento, un elenco di 125 registrazioni e le prove di frequenza. L'elenco contiene cinque duplicati e otto persone, diverse dalle cinque ripetute, prive della frequenza minima. Il verbale può sostenere la milestone, purché attesti le condizioni previste; per il target si contano **125 − 5 − 8 = 112** utenti verificabili. Mancano otto utenti per raggiungere 120. Il pagamento non colma la differenza.

**Nota di esito attesa.** «L'attivazione risulta documentata dal verbale, da confrontare con le condizioni della misura. Il target quantitativo non risulta raggiunto: gli utenti ammissibili documentati sono 112 su 120. Si rettifica il dato proposto, si conserva l'elenco di riconciliazione e si informa il responsabile per il seguito previsto. Non si certificano utenti privi di evidenza e non si retrodatano attività». Il mancato raggiungimento e le conseguenze finanziarie vanno gestiti secondo gli atti della misura; l'operatore non può inventare una proroga.
'''}
for cap in [6,7,8]:
 p=next(B.glob(f'{cap:02}-*.md'));t=p.read_text(encoding='utf8')
 for (c,n),block in blocks.items():
  if c==cap:t=re.sub(rf'(^### N-IR02-{cap:02}-{n:02}[^\n]*\n)',lambda m:m[1]+'\n'+block+'\n',t,count=1,flags=re.M)
 t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);t=t.replace('draft_stage: text_frozen','draft_stage: correction-in-progress').replace('review_required: false','review_required: true');p.write_text(t,encoding='utf8')
(A/'V06-10-progress.json').write_text(json.dumps({'status':'parziale','completed':['M-IR02/06','M-IR02/07','M-IR02/08'],'pending':['M-IR03/04','M-IR03/11'],'numericalChecks':{'amortization':12000,'prepaid':9000,'accrual':600,'profit':14400,'cash':158000,'balance':215000,'unitCost':3360,'flatRate':2000,'targetActual':112}},ensure_ascii=False,indent=2),encoding='utf8')
print('V06-10: quota IR02 applicata; IR03 ancora pendente')
