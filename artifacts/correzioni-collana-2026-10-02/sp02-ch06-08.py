from pathlib import Path
import re
B=Path('wiki/books/moduli/m-sp02-vigili-fuoco/chapters');A=Path('wiki/reviews/correzioni-collana-2026-10-02/archive')
for no in ['06','07','08']:
 p=next(B.glob(no+'-*.md'));t=p.read_text(encoding='utf8');a=A/f'pre-correzioni-sp02-{no}.md'
 if not a.exists():a.write_text(t,encoding='utf8')
 if no=='06':
  t=t.replace('la concentrazione delle riserve impone una decisione prima dell\'allenamento. Il candidato civile senza titolo di riserva non deve nascondersi il significato competitivo del cinque per cento residuo, pur considerando la devoluzione dei posti non coperti.','le riserve vanno distinte dai requisiti di ammissione. Il residuo nominale del cinque per cento non è garantito esclusivamente ai non riservatari; occorre considerare graduatoria di merito e devoluzione, senza dedurre probabilità dai soli posti.')
  t=t.replace('Una riga a valle non può essere considerata prioritaria se il passaggio precedente è ancora formalmente aperto. Disegnare questa sequenza rende immediata la criticità.','I requisiti formali critici si verificano subito, ma la preparazione fisica o linguistica può dover iniziare in parallelo: una dipendenza procedurale non impone di attendere il risultato del filtro prima di sviluppare capacità che richiedono tempo.')
  t=t.replace('Il registro viene controllato anche prima della consegna editoriale. Ogni numero nel capitolo deve avere fonte e data; ogni silenzio rilevante deve essere dichiarato. Questo rende il testo aggiornabile senza riscriverlo da zero.','Prima di una simulazione controlla la versione delle istruzioni usate. Ogni numero della tua scheda deve avere fonte e data; ciò che il documento non indica resta una domanda aperta. La revisione evita di confrontare risultati prodotti con regole differenti.')
  t=t.replace('Il controllo viene sempre datato e firmato dal candidato.','Il controllo viene datato e collegato alla copia dei documenti effettivamente consultati, così un cambiamento successivo resta riconoscibile.')
  marker='### Fonte e riuso'
  add='''### Destinazioni di studio nel volume base

I rinvii seguenti hanno un oggetto delimitato. Non sostituiscono l’intero programma specialistico e richiedono una verifica nella forma del nuovo concorso.

- **Condizioni, connettivi e quantificatori:** [[books/il-metodo-bando/chapters/logica-comprensione-ragionamento#Logica essenziale: principi e parole che decidono il risultato]]. Riprendi le distinzioni e risolvi l’esempio sull’inversione del condizionale prima di una serie mista.
- **Sistema operativo e gestione dei file:** [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali#2. Sistema operativo, file e cartelle]]. La sezione spiega percorsi, estensioni, copia e spostamento; esegui il mini-esercizio senza confondere nome e formato.
- **Videoscrittura e fogli elettronici:** [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali#3. Produttività digitale e strumenti Office]]. Il laboratorio di formule e riferimenti consente un controllo concreto; l’area digitale del volume base non è limitata al diritto del documento informatico.
- **Comprensione di testi inglesi:** [[books/il-metodo-bando/chapters/inglese-concorsuale-essenziale#14. Reading comprehension]]. I mini-brani con risposte motivate allenano individuazione del dato e confronto con i distrattori; non attribuiscono un livello linguistico non dichiarato dal bando.
- **Nozioni costituzionali:** [[books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato#1. Stato, Costituzione e ordinamento costituzionale]]. La destinazione spiega caratteri della Costituzione e forme di Stato e governo; non copre da sola la storia d’Italia dal 1861.

Per il direttivo collega inoltre la parte istituzionale alla mappa della prevenzione incendi del capitolo 5 di questo modulo, distinguendo funzione, progetto, SCIA e controlli. La teoria tecnico-progettuale propria della specializzazione non si considera coperta per effetto di questi rinvii comuni.

'''
  t=t.replace(marker,add+marker,1)
  t=t.replace('Nel volume base può essere trattata come amministrazione digitale; nel bando operativo è accertamento dell\'uso delle apparecchiature e delle applicazioni più diffuse.','Il volume base comprende sia amministrazione digitale sia competenze d’uso; nel bando operativo rileva l’uso delle apparecchiature e delle applicazioni più diffuse. Seleziona le sezioni pertinenti indicate sotto.')
  t=t.replace('non coincide con amministrazione digitale |','sezioni su file, produttività e competenze d’uso; non solo amministrazione digitale |')
  t=t.replace('La formula sulle riserve, per esempio, alimenta una valutazione di partecipazione; quella sul filtro limita il tempo di studio dopo il margine.','La formula sulle riserve alimenta una valutazione documentata; quella sul filtro aiuta a distribuire il tempo mantenendo richiami, senza presumere una soglia reale dai risultati personali.')
 if no=='07':
  t=t.replace('cinque risposte orali e una revisione delle fonti','otto risposte orali e una revisione delle fonti').replace('Questa triage','Questo criterio di selezione')
  marker='## N-SP02-12-01'
  add='''### Quando restano soltanto trenta o sessanta giorni

I percorsi abbreviati presuppongono requisiti verificabili e una base già disponibile. Non promettono di creare in poche settimane una capacità fisica mancante. Per la parte motoria le sedute e i recuperi restano definiti con chi segue la preparazione; le ore sotto indicate riguardano studio, controllo e produzione.

**Trenta giorni, operativo — 8 ore di studio settimanali.** Giorni 1–7: due ore di controllo di bando e avvisi, quattro di diagnosi delle aree e due di correzione. Giorni 8–21: quattro ore di recupero mirato, due di serie miste e due di correzione ogni settimana. Giorni 22–30: simulazioni secondo istruzioni effettive, richiami e controllo dei documenti nella stessa quota di tempo. Output: scheda corrente, registro degli errori e almeno due simulazioni corrette; la prova fisica resta un percorso parallelo, non un carico improvvisato dell’ultima settimana.

**Sessanta giorni, operativo — 8 ore settimanali.** Nei primi quindici giorni completa diagnosi e prime correzioni; nei successivi trenta alterna recupero e serie miste con verifica quindicinale; negli ultimi quindici consolida formato ufficiale e logistica. Ripartizione ordinaria: quattro ore di teoria mirata, due di esercizi e due di correzione. Quando una lacuna si chiude, passa al mantenimento e rialloca soltanto il tempo dimostrato eccedente.

**Trenta giorni, direttivo — 12 ore settimanali.** Prima settimana: due ore sul programma e requisiti, quattro su una produzione diagnostica, tre di correzione e tre di orale. Settimane 2–3: sei ore fra elaborato e correzione, quattro sulle lacune emerse e due per otto brevi risposte orali. Ultimi giorni: una simulazione con gli strumenti consentiti, recupero degli errori ricorrenti e cartella documentale. Le durate sono didattiche: la simulazione integrale assume il tempo della prova solo quando questo è pubblicato.

**Sessanta giorni, direttivo — 12 ore settimanali.** Giorni 1–14: diagnosi e quattro sezioni tecniche corrette; giorni 15–42: una produzione completa per settimana con correzione, più otto risposte orali; giorni 43–60: due simulazioni complessive e recupero mirato. La quota settimanale ordinaria resta sei ore di produzione/correzione, quattro di studio mirato e due di orale. Se una traccia richiede più tempo, riduci altre consegne: non far comparire ore inesistenti.

In ciascun percorso il controllo finale confronta consegne effettive e programma. Un output non prodotto resta una lacuna; non si chiude la riga perché sono trascorsi trenta o sessanta giorni.

'''
  t=t.replace(marker,add+marker,1)
  t=t.replace('almeno quattro produzioni tecniche, trenta risposte orali','almeno quattro produzioni tecniche e trenta risposte orali: otto per ciascuna delle prime quattro settimane ne programmano trentadue, con due di margine rispetto all’obiettivo,')
  t=t.replace('con due di margine rispetto all’obiettivo, e un diario','con due di margine rispetto all’obiettivo; inoltre un diario')
 if no=='08':
  t=t.replace('non ho riprodotto elenchi diagnostici né tratto conclusioni autonome','ho distinto la valutazione preliminare dall’accertamento concorsuale').replace('il terzo regime sanitario','il regime sanitario tecnico-professionale')
  t=t.replace('pianificare sul minimo, non sulla media','controllare ogni soglia e calcolare separatamente la media')
  t=t.replace('fermarsi al margine ragionevole e riallocare tempo','mantenere richiami e riallocare tempo sulla base degli errori')
  marker='### La decisione scritta di Andrea'
  add='''### Dati e soluzione del caso operativo

Per chiudere il ragionamento aggiungiamo dati espliciti, riferiti alla tabella maschile del capitolo 4: trave conclusa alla seconda esecuzione nel tempo massimo (**25**), quattro trazioni valide (**21**), diciotto progressioni valide (**21**). La Prova 1 sarebbe superata con media **67/3 = 22,333…**. La corsa in **4'55\"** raggiunge **21**, ma ha margine temporale nullo rispetto alla soglia nominale. Il percorso acquatico non completato rende la terza prova non superata: non si forma un risultato utile sommando soltanto le prime due.

In una successiva rilevazione valida Andrea mantiene quei risultati e completa il percorso acquatico in **35 secondi**, pari a **21**. Il totale delle prove è allora **64,333…**; se la patente B era posseduta e dichiarata entro il termine, il totale con il titolo diventa **65,333…**. Il calcolo è didattico e non predice la posizione in graduatoria. Il recupero del percorso acquatico cambia la validità complessiva; il margine resta nullo in corsa e nuoto e va valutata la ripetibilità con chi segue la preparazione.

La domanda del caso è: «Bastava aumentare le trazioni lasciando incompleto il percorso acquatico?». **No:** avrebbe migliorato soltanto una media interna a una procedura ancora non superata. La seconda domanda è: «Il nuovo totale assicura il posto?». **No:** mancano graduatoria, risultati altrui e applicazione delle riserve. Sono due limiti diversi, da spiegare entrambi.

'''
  t=t.replace(marker,add+marker,1)
  marker='### La settimana di controllo di Francesca'
  add='''### Una consegna tecnica con soluzione e griglia

Francesca riceve una traccia didattica circoscritta: «Una forza costante perpendicolare di 1.200 N agisce uniformemente su una superficie di 0,04 m². Calcola la pressione media e indica che cosa cambia dimezzando l’area, a forza invariata. Distingui il risultato da una verifica strutturale». Non è una traccia ufficiale: serve a controllare la sequenza dati–modello–unità–limiti prima di elaborati più complessi.

La scaletta corretta identifica forza e area, dichiara l’ipotesi di distribuzione uniforme e usa **p = F/A**. Il risultato è **30.000 Pa = 30 kPa**. Con area 0,02 m² la pressione media diventa **60.000 Pa = 60 kPa**. La relazione inversa è controllabile: stessa forza su metà superficie raddoppia il rapporto. Non si conclude però che un elemento strutturale sia sicuro: mancano materiale, geometria, vincoli, azioni pertinenti e criteri di verifica.

La prima risposta di Francesca riportava soltanto «30» e «raddoppia». La seconda scrive unità, ipotesi e limite della conclusione. La correzione assegna un riscontro distinto a cinque criteri: dati completi; modello motivato; operazione e unità corrette; controllo della variazione; conclusione limitata al quesito. Non è un voto della commissione, ma una griglia ripetibile. Una risposta con risultato corretto e unità assente resta da correggere.

All’orale il collega chiede: «Perché non puoi affermare che la struttura resiste?». La risposta attesa distingue una pressione media calcolata da una verifica di sicurezza, che richiede ulteriori dati e il modello pertinente. Una seconda domanda collega funzione e procedura: «La valutazione di un progetto antincendio coincide con la SCIA?». Francesca risponde usando la sequenza del capitolo 5: esame progettuale per i casi previsti, segnalazione prima dell’esercizio, controlli successivi. Non inventa una soluzione progettuale a partire dai soli dati numerici.

'''
  t=t.replace(marker,add+marker,1)
 t=t.replace('review_required: false','review_required: true');t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
print('SP02/06–08 integrati; quiz da rifinire separatamente')
