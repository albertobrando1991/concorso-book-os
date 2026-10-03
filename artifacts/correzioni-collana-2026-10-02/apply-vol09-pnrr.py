from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-pnrr-architettura-chiusura-regis-2026-10-03.md'
slug='10-pnrr-milestone-target-regis';t=u.read(slug)
t=t.replace('## N-TR02-10-01 · Mappa BANDO','## N-TR02-10-01 · Architettura del piano e responsabilità')
t=t.replace('## N-TR02-10-02 · Strumenti e applicazioni','## N-TR02-10-02 · Risultati, indicatori e identificativi')
t=t.replace('## N-TR02-10-03 · Gestione operativa','## N-TR02-10-03 · ReGiS, dati e validazione')
t=t.replace('## N-TR02-10-04 · ▣ Verifica 2 - Dati, ReGiS e rendicontazione','## N-TR02-10-04 · Controlli, ritardi e chiusura 2026')
t=t.replace('La milestone è una tappa verificabile; il target è un risultato misurabile.','La milestone è un traguardo qualitativo; il target è un obiettivo quantitativo.')
t=t.replace('Per lo studio concorsuale non serve memorizzare elenchi mutevoli di misure. Serve capire la logica amministrativa:', 'Per lo studio concorsuale occorre conoscere la struttura delle missioni e saper leggere la singola misura. La logica amministrativa è questa:')
t=t.replace("La milestone è una tappa, un evento o una condizione verificabile nel percorso di attuazione. Il target è un risultato misurabile da raggiungere secondo la misura.","Ai sensi dell’articolo 2 del regolamento (UE) 2021/241, milestone, o traguardo, esprime un risultato qualitativo; target, o obiettivo, un risultato quantitativo. Entrambi misurano l’avanzamento di riforme e investimenti. Una scadenza interna di lavoro non è automaticamente una milestone PNRR.")
t=t.replace('La milestone è una tappa o condizione verificabile. Può avere natura procedurale, amministrativa o tecnica, secondo quanto prevede la misura. Il risultato numerico è più vicino alla logica del target, ma anche qui conta la definizione ufficiale del singolo intervento.','La milestone esprime un risultato qualitativo, per esempio l’entrata in vigore di una riforma prevista negli atti del piano. Il target è quantitativo, per esempio il numero di strutture realizzate con caratteristiche definite. Entrambi richiedono evidenze e rispetto della scadenza applicabile.')
t=t.replace('La milestone può essere il completamento di una fase verificabile, come l’aggiudicazione, l’avvio, il collaudo o altra condizione prevista dalla misura.','La milestone può essere il completamento di una fase verificabile soltanto se quella condizione è prevista dagli atti della misura.')
t=t.replace("La milestone può essere il completamento di una fase verificabile, come l'aggiudicazione, l'avvio, il collaudo o altra condizione prevista dalla misura.","La milestone può essere il completamento di una fase verificabile soltanto se quella condizione è prevista dagli atti della misura.")
t=t.replace('Le definizioni operative cambiano in base al progetto.','La distinzione giuridica qualitativo/quantitativo resta ferma; cambiano il contenuto concreto del risultato e le prove richieste.')
anchor='### Milestone, target, output e risultato'
t=u.replace(t,anchor,'''### Dalle missioni alla singola operazione

Il **Recovery and Resilience Facility**, RRF, è il dispositivo europeo per la ripresa e la resilienza; il PNRR è il piano italiano attuato nel suo quadro. I sei pilastri tematici del regolamento europeo non coincidono con la ripartizione italiana in missioni. Dopo l’inserimento del capitolo REPowerEU, le missioni italiane sono sette.

| Missione | Ambito da riconoscere |
| --- | --- |
| M1 | Digitalizzazione, innovazione, competitività, cultura e turismo |
| M2 | Rivoluzione verde e transizione ecologica |
| M3 | Infrastrutture per una mobilità sostenibile |
| M4 | Istruzione e ricerca |
| M5 | Inclusione e coesione |
| M6 | Salute |
| M7 | REPowerEU: sicurezza energetica e transizione dell’energia |

La **componente** raggruppa interventi coerenti all’interno di una missione; riforme e investimenti sono le misure attraverso cui il piano agisce. Il **progetto** è l’operazione concreta attuata da un soggetto. Non tutti i livelli hanno la stessa articolazione: il capitolo REPowerEU non va forzato nello schema in componenti delle prime sei missioni.

Per leggere un codice, scomponilo. In M4C1I1.1, M4 indica la missione istruzione e ricerca, C1 la componente, I1.1 l’investimento. Il CUP di un singolo intervento è un altro identificativo: non coincide con il codice della misura. Più progetti possono concorrere a un obiettivo della stessa misura; il risultato europeo può quindi essere aggregato, mentre il soggetto attuatore deve dimostrare il proprio contributo secondo gli atti che lo finanziano.

Una **riforma** modifica regole, istituzioni o processi; un **investimento** impiega risorse per ottenere capacità, infrastrutture, servizi o altri risultati previsti. Non ogni riforma comporta un appalto e non ogni investimento coincide con un unico contratto. Questa distinzione impedisce di ridurre il PNRR a una lista di gare.

### CID, accordi operativi e obblighi dell’ente

La Commissione valuta il piano; il Consiglio dell’Unione europea, su proposta della Commissione, approva tale valutazione con una **decisione di esecuzione**, spesso abbreviata CID. Il suo allegato contiene la descrizione di riforme e investimenti, risultati e scadenze. Gli **Operational Arrangements**, o accordi operativi fra Commissione e Stato, precisano monitoraggio, indicatori, meccanismi di verifica e accesso ai dati. Il decreto di finanziamento, l’avviso e la convenzione trasferiscono al soggetto attuatore gli obblighi della sua operazione.

L’ordine di lettura è dunque: decisione e allegato applicabili → accordi operativi → disciplina della misura → atto di finanziamento del progetto. Una presentazione divulgativa aiuta a orientarsi, ma non sostituisce la formulazione dell’obiettivo. Una proposta della Commissione di revisione non equivale ancora alla decisione del Consiglio; neppure il nuovo Gantt dell’ente modifica da solo una scadenza del piano.

Il coordinamento nazionale tiene insieme amministrazioni titolari, monitoraggio e rapporto con l’Unione. Nel lavoro sul progetto, la distinzione decisiva è fra **amministrazione titolare**, responsabile del presidio della misura e della validazione nel proprio perimetro, e **soggetto attuatore**, che realizza l’intervento, alimenta i dati e conserva le prove. La stazione appaltante può coincidere con quest’ultimo, ma il ruolo contrattuale non esaurisce gli obblighi del finanziamento. Il fornitore resta tenuto alle prestazioni e alla documentazione previste dal contratto.

### Perché una fattura non determina la rata europea

Il dispositivo è basato sul conseguimento dei risultati: le rate allo Stato seguono la valutazione soddisfacente di milestone e target, secondo l’articolo 24 del regolamento. Non sono la somma automaticamente rimborsata delle fatture trasmesse dai singoli comuni. Ciò non elimina i controlli sulla spesa: restano regolarità delle procedure, tutela degli interessi finanziari, prevenzione di frodi, conflitti di interessi e doppio finanziamento, oltre alle regole della misura.

In prova, tieni distinti i due circuiti. Nel rapporto Stato–Unione si dimostrano i risultati concordati e gli obblighi di controllo; nel rapporto amministrazione titolare–attuatore si applicano condizioni di finanziamento, trasferimento e rendicontazione dell’operazione. Un progetto può avere un avanzamento finanziario elevato e una performance insufficiente. Può anche avere completato la prestazione ma dover ancora completare il fascicolo di spesa.

'''+anchor)
anchor='### Monitoraggio, rendicontazione e controllo'
t=u.replace(t,anchor,'''### Alimentazione, prevalidazione e validazione

Il soggetto attuatore alimenta i dati di propria competenza sulla base di atti ed evidenze. La **prevalidazione** esegue controlli automatici e consente di vedere anomalie prima del consolidamento. L’amministrazione titolare effettua la **validazione** periodica delle informazioni nel suo perimetro. Il significato dei passaggi è diverso: un campo formalmente corretto può contenere un dato sostanzialmente falso; un controllo informatico superato non certifica da solo ammissibilità della spesa o raggiungimento del target.

Un flusso completo comprende cinque operazioni: riconciliare fascicolo e dati; aggiornare avanzamento fisico, procedurale e finanziario; eseguire prevalidazione; risolvere o motivare le anomalie secondo le istruzioni; sottoporre i dati al consolidamento previsto. Dopo la validazione, rettifiche e aggiornamenti devono restare tracciabili. Non si cancella la storia di un progetto per far scomparire un ritardo.

**Esempio documentato di calendario.** Le linee guida del Dipartimento per le pari opportunità, versione 3.0 del 20 giugno 2025, per M5C1 investimento 1.3 prevedono trasmissione degli esiti di prevalidazione entro il 5 del mese, aggiornamento e prevalidazione del soggetto attuatore entro il 10, validazione dell’amministrazione titolare entro il 20. Gli esiti negativi o con riserva attivano il ciclo di correzione descritto nella guida. È un esempio attribuito a quella misura e versione: le istruzioni della propria amministrazione titolare governano il calendario concreto, soprattutto nella fase finale del 2026.

### Caso di qualità del dato: cento consegnati, novantadue verificati

Assumiamo, per questo esercizio, che l’atto di finanziamento richieda **100 dispositivi installati, configurati e funzionanti**, provati da verbali nominativi. Il fornitore consegna 100 dispositivi; 92 superano la verifica, otto sono ancora da configurare. La fattura riguarda l’intera consegna. Un operatore inserisce 100 come valore realizzato perché il numero coincide con il documento di trasporto.

La registrazione è errata: l’indicatore del caso richiede tre condizioni congiunte, non la sola consegna. La situazione dimostrata è 92 dispositivi su 100, cioè il 92%; l’output contrattuale consegnato e quello verificato vanno registrati distintamente. La fattura non completa gli otto dispositivi mancanti. Occorre rettificare il dato, collegare i verbali, assegnare il completamento al responsabile competente e valutare l’effetto sulla scadenza.

| Dato | Evidenza | Decisione corretta |
| --- | --- | --- |
| 100 consegnati | Documento di trasporto | Registrare la consegna |
| 92 funzionanti | Verbali di verifica | Rappresentare il valore dimostrato |
| 8 da configurare | Elenco anomalie | Completare e verificare, senza anticipare l’esito |
| Fattura ricevuta | Documento fiscale | Avviare i controlli di competenza; non dichiarare per questo il target |

Se la prevalidazione non segnala errori, la conclusione non cambia: la piattaforma può non conoscere il contenuto dei verbali. Il controllo sostanziale confronta definizione dell’indicatore, unità di misura, popolazione considerata, data di osservazione e documenti. Il numeratore deve contare soltanto gli elementi che rispettano la definizione; il denominatore deve essere quello dell’obiettivo, senza ridurlo per migliorare la percentuale.

Un secondo errore possibile è l’associazione a un CUP diverso. Non si cambia il codice per eliminare un messaggio di errore: si ricostruisce quale atto finanzia la prestazione, quali procedure vi sono collegate e quale identificativo è corretto. La correzione deve seguire il flusso autorizzato e lasciare traccia della riconciliazione. Una risposta d’esame solida indica dato sbagliato, fonte corretta, ruolo responsabile e azione, senza inventare pulsanti o schermate.

'''+anchor)
anchor='### Caso ragionato: milestone a rischio'
t=u.replace(t,anchor,'''### Il calendario di chiusura 2026

**Quadro verificato al 3 ottobre 2026.** I termini di agosto e settembre riportati qui sono già trascorsi alla data di questa edizione. Servono a interpretare il ciclo conclusivo e le responsabilità; non indicano nuove finestre disponibili.

| Termine | Livello e funzione |
| --- | --- |
| 31 agosto 2026 | Termine finale UE per il completamento di milestone e target |
| 30 settembre 2026 | Termine per le ultime richieste statali di pagamento alla Commissione, con le prove richieste |
| 31 dicembre 2026 | Termine dei pagamenti del dispositivo dalla Commissione agli Stati |

La comunicazione della Commissione *NextGenerationEU – La strada verso il 2026*, COM(2025) 310, chiarisce questa sequenza. **Dicembre non proroga il termine per realizzare i risultati.** Il periodo di valutazione della richiesta non permette di completare a ottobre una prestazione che doveva essere conclusa entro agosto. L’eventuale mancato raggiungimento va rappresentato e trattato secondo gli atti applicabili; non si retrodatano certificati o avanzamenti.

Accanto ai termini UE esistono quelli del progetto e della misura, che possono essere anteriori. Le linee guida PCM–MEF/RGS del 16 aprile 2026, per gli interventi ricompresi nel loro ambito, precisano la documentazione di conclusione e il riferimento al secondo trimestre 2026, ossia **30 giugno**. Prevedono specifici casi con completamento entro il 31 agosto e limitate eccezioni gestite dall’amministrazione titolare: non sono una proroga automatica concessa a qualunque soggetto attuatore.

Per applicarle, si verifica anzitutto se l’intervento appartiene all’allegato pertinente o se l’amministrazione titolare ne ha disposto l’applicazione nel perimetro consentito. Poi si controllano CID, atto di finanziamento e istruzioni della misura. L’ordine evita due errori opposti: attribuire a tutti i progetti una scadenza intermedia prevista per alcuni, oppure ignorare una scadenza anteriore perché esiste il limite UE di agosto.

### Quale evidenza chiude la performance

Per i lavori, le linee guida disciplinano il certificato di ultimazione; per servizi e forniture, la certificazione di regolare esecuzione o la verifica di conformità pertinente. Il documento deve rendere identificabili misura, intervento, CUP, CIG, importo, soggetti e data, collegando ciò che è stato eseguito alla descrizione della misura. **La data di emissione della certificazione è rilevante**: una semplice affermazione retrospettiva non sostituisce la prova richiesta nei termini.

Se è già disponibile un collaudo o un certificato di regolare esecuzione avente valore probatorio superiore, non occorre produrre inutilmente un documento meno avanzato per duplicare la stessa dimostrazione. Restano necessari gli elementi richiesti e l’eventuale integrazione delle informazioni mancanti. Il certificato lavori è sottoscritto dai soggetti previsti, con il visto del RUP; i modelli per servizi e forniture distinguono DEC/RUP, impresa e soggetto della stazione appaltante abilitato alla stipula.

Le lavorazioni marginali ammesse entro un termine assegnato, comunque non superiore a 60 giorni nei presupposti previsti, non possono incidere sull’uso e sulla funzionalità dell’intervento. La regola non consente di chiamare “ultimata” un’opera cui manchi una parte indispensabile per funzionare. Nel caso dei dispositivi, otto unità non configurate e non funzionanti non diventano complete grazie a una generica annotazione “finiture residue”.

Nel flusso delle linee guida, l’evidenza di completamento è normalmente caricata entro cinque giorni dal completamento; la documentazione integrativa dei controlli segue entro quindici giorni. Questi adempimenti vanno letti nel loro specifico ambito e insieme alle istruzioni dell’amministrazione titolare. La data di caricamento e la data in cui la prestazione è stata effettivamente completata sono informazioni distinte: correggere un dato non modifica il fatto storico.

### Performance, spesa e strumenti finanziari

La rendicontazione della performance può precedere quella della spesa, che segue le istruzioni finanziarie e i controlli applicabili. Non si deduce dal 31 agosto l’obbligo indistinto che ogni pagamento locale debba essere effettuato quel giorno; non si deduce dal 31 dicembre la libertà di completare qualsiasi opera entro fine anno. L’esercizio corretto è individuare per ciascun obbligo **soggetto, oggetto, scadenza ed evidenza**.

Alcune misure attuate tramite strumenti finanziari o strutture di investimento hanno risultati formulati in termini di trasferimento di risorse e stipula di contratti vincolanti con beneficiari, con condizioni specifiche. L’eventuale prosecuzione a valle delle attività non crea un’eccezione generale per tutti i cantieri o acquisti. Prima di invocare questa disciplina occorre dimostrare che il progetto appartiene a quella misura e che il risultato previsto è proprio quello, non un’opera fisica ancora incompleta.

**Verifica applicata.** Un ente afferma: «Abbiamo tempo fino al 31 dicembre perché l’Unione paga entro quella data». La risposta è errata: confonde il pagamento Commissione–Stato con il completamento dei risultati e con le scadenze dell’operazione. La correzione identifica il termine della misura, la prova richiesta e l’eventuale scostamento, senza spostare il calendario con una decisione unilaterale.

'''+anchor)
t=t.replace('Risposta: la milestone è una tappa o condizione verificabile del percorso di attuazione. Il target è un risultato misurabile da raggiungere secondo l’indicatore previsto.','Risposta: la milestone è un traguardo qualitativo; il target è un obiettivo quantitativo, entrambi definiti negli atti del piano.')
t=t.replace("Risposta: la milestone è una tappa o condizione verificabile del percorso di attuazione. Il target è un risultato misurabile da raggiungere secondo l'indicatore previsto.","Risposta: la milestone è un traguardo qualitativo; il target è un obiettivo quantitativo, entrambi definiti negli atti del piano.")
t+='\n### Riferimenti normativi e operativi\n\nRegolamento (UE) 2021/241, artt. 2, 3, 20, 22 e 24; Commissione europea, COM(2025) 310 final, *NextGenerationEU – La strada verso il 2026*; PCM–MEF/RGS, linee guida del 16 aprile 2026 sulla conclusione degli interventi PNRR, con allegati; Dipartimento per le pari opportunità, linee guida di monitoraggio, rendicontazione e controllo, versione 3.0 del 20 giugno 2025, utilizzate per l’esempio espressamente indicato. Per la singola operazione si leggono inoltre CID, accordi operativi e atti della misura pertinenti.\n'
u.save(slug,t,['V09-26','V09-27'],u.REF);u.record()
