from pathlib import Path
import re
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');p=B/'chapters/01-authority-viste-dal-candidato.md';s=p.read_text(encoding='utf8')
s=s.replace('Profilo premium cross-authority.','Profilo che integra diritto ed economia della regolazione.').replace('il percorso premium','il percorso giuridico-economico')
s=s.replace('Il VOL-05 è complementare ai capitoli del  su , , , , ,  e .','Il VOL-05 è complementare al VOL-01: capitolo 4, [[books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato|Costituzione e ordinamento dello Stato]]; 5, [[books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati|Diritto amministrativo operativo]]; 6, [[books/il-metodo-bando/chapters/pubblico-impiego-e-organizzazione-pa|Pubblico impiego e organizzazione della PA]]; 7, [[books/il-metodo-bando/chapters/trasparenza-anticorruzione-privacy|Trasparenza, anticorruzione e privacy]]; 8, [[books/il-metodo-bando/chapters/contabilita-pubblica-essenziale|Contabilità pubblica essenziale]]; 10, [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali|Informatica, PA digitale e competenze digitali]]; 11, [[books/il-metodo-bando/chapters/inglese-concorsuale-essenziale|Inglese concorsuale essenziale]]. Per gli appalti ANAC si aggiunge il capitolo 9, [[books/il-metodo-bando/chapters/contratti-pubblici-essenziali|Contratti pubblici essenziali]].')
s=s.replace('Il percorso corretto è E: ripasso selettivo dei capitoli del VOL-01 su ,  e ;  per il ciclo regolatorio e  per l\'economia;  per ARERA;  su consultazione e analisi tariffaria.','Il percorso corretto è E: nel VOL-01 ripasso selettivo dei capitoli 5, 8 e 11, rispettivamente diritto amministrativo, contabilità pubblica e inglese; in questo volume studio dei capitoli 4 per il ciclo regolatorio, 7 per economia e dati, 9 per ARERA e 15 per le simulazioni su consultazione e analisi tariffaria.')
start=s.index('### Laboratorio di qualificazione');s=s[:start]+'''### Un Decoder compilato e tre calendari alternativi

**Esempio interamente fittizio.** Bando Alfa, profilo economico-regolatorio E; domanda entro il 20 ottobre 2026, ore 12:00; scritto il 3 dicembre, durata 90 minuti, due quesiti e un'analisi numerica; orale e inglese secondo il programma. Requisiti dichiarati nella traccia: laurea economica ammessa, nessuna esperienza obbligatoria. Il candidato possiede il titolo richiesto, deve inviare la domanda e annotare la ricevuta. Le date e le prove non descrivono un concorso reale.

| Campo del Decoder | Compilazione del caso Alfa |
| --- | --- |
| Fonte e versione | Bando fittizio Alfa, allegato programma versione 1; controllare eventuali rettifiche ogni settimana |
| Priorità | Capitoli 4, 7 e 9; fondamenti 2–3; laboratorio 15; ripasso base 5, 8 e 11 del VOL-01 |
| Prerequisiti da colmare | Percentuali, lettura di tabelle, ricavo/costo, procedimento amministrativo |
| Output settimanali | Un calcolo commentato, una mini-AIR, una risposta inglese; ogni due settimane simulazione cronometrata |
| Errore iniziale | Confondere variazione percentuale e punti percentuali |
| Controllo documentale | Domanda inviata, ricevuta salvata, requisiti e documento verificati; aggiornamento convocazione nello scadenziario |

I calendari sono **alternative**, non tre fasi da sommare. Il piano da 30 giorni richiede prerequisiti già solidi; con lacune profonde si usano 60 o 90 giorni, oppure si restringe il bando target senza saltare le sue materie obbligatorie.

| Orizzonte e carico didattico | Distribuzione del lavoro | Prove e recupero |
| --- | --- | --- |
| 30 giorni, 2 ore al giorno: 60 ore | 12 ore fondamenti, 24 verticale dell'ente, 12 esercizi integrati, 12 prove/ripasso | Giorni 7, 14 e 21: verifica; giorni 26 e 29: simulazione. Recupero nelle ultime 12 ore |
| 60 giorni, 90 minuti al giorno: 90 ore | 20 ore prerequisiti/fondamenti, 35 verticale, 20 esercizi integrati, 15 prove/ripasso | Una verifica ogni settimana; quattro simulazioni negli ultimi 20 giorni |
| 90 giorni, 1 ora al giorno: 90 ore | 25 ore prerequisiti/fondamenti, 30 verticale, 20 esercizi integrati, 15 prove/ripasso | Richiamo a 1, 7 e 21 giorni dai nuclei nuovi; quattro simulazioni finali |

Per **G**, le ore verticali vanno soprattutto a fattispecie, procedimenti, garanzie e rimedi; l'output è una soluzione motivata con fonte e giudice. Per **E**, si concentrano su mercato, costi, tariffe, dati e interpretazione dei risultati; l'output deve mostrare calcolo, ipotesi e limite. Per **P — giuridico-economico**, si divide il lavoro fra fonte/potere e analisi economica, per concludere con una decisione motivata e un memo. Il profilo P richiede le basi di G ed E: non equivale a studiare tutte le authority con identica profondità.

I profili prudenziali e assicurativi trovano il nucleo specialistico nei capitoli 11–12. Le nozioni di privato, commerciale e antiriciclaggio necessarie ai casi finanziari sono raccordate nel capitolo 12: non sono attribuite senza riscontro al VOL-01. Per i profili informatico-tecnologici il percorso comprende il VOL-08 e il programma tecnico del bando: questo volume sviluppa poteri e contesto regolatorio, non sostituisce il manuale informatico.

## N-MF05-01-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Un programma insiste su energia, tariffe e analisi quantitativa. Quale percorso scegliere e quali capitoli privilegiare?

**Risposta corretta:** E; capitoli 4, 7 e 9, con le simulazioni del 15. Diritto amministrativo e inglese restano prerequisiti, ma studiarli da soli non copre le prestazioni quantitative richieste.

**Quesito 2.** Un'esposizione identifica ARERA come gestore della rete e CONSOB come banca del cliente. Qual è l'errore comune?

**Risposta corretta:** confonde regolazione o vigilanza con gestione del servizio. L'impresa eroga o gestisce; l'autorità esercita i poteri attribuiti dalla fonte. Occorre poi distinguere regolazione, controllo e rimedio individuale nel settore.

**Quesito 3.** Il bando fittizio Alfa scade il 20 ottobre alle 12:00. Il candidato ha completato lo studio ma non conserva una ricevuta. Il Decoder è completo?

**Risposta corretta:** no. La preparazione non prova l'invio della domanda. Va verificato l'adempimento sul canale previsto e conservata la ricevuta, senza assumere che il piano di studio includa automaticamente gli adempimenti della selezione.

**Quesito 4.** Quanto tempo prevede il piano da 60 giorni e perché non va aggiunto a quello da 30?

**Risposta corretta:** 90 ore: 60 × 1,5. I piani sono alternative calibrate sui prerequisiti; sommarli produrrebbe un calendario diverso da quello scelto. Le ore comprendono esercizi e recupero, non solo lettura.

**Quesito 5.** Quale output distingue il percorso P dalla semplice giustapposizione di un tema giuridico e di un calcolo?

**Risposta corretta:** una decisione integrata: fonte e competenza delimitano le opzioni; il dato misura gli effetti; la motivazione spiega scelta, garanzie e limiti. Il capitolo 15 propone prove e memo per allenare questa integrazione.

**Quesito 6.** Il bando tecnico del Garante richiede reti, sistemi e sicurezza. Bastano il capitolo privacy e l'informatica di base?

**Risposta corretta:** no. Si aggiungono i nuclei tecnici del VOL-08 e si confrontano con il programma. La materia privacy individua obblighi e poteri; non insegna da sola progettazione delle reti o amministrazione dei sistemi.

### Caso ragionato di chiusura

**Fatti.** Sara dispone di 60 giorni e 90 minuti quotidiani. Per Alfa ha programmato 70 ore di sola lettura giuridica e 20 di economia, nessuna simulazione. Sa calcolare percentuali ma confonde tariffa e tributo. Correggi il piano senza aumentare il tempo disponibile.

**Soluzione.** Il monte ore è 90. Sara assegna 20 ore a fondamenti e prerequisiti, 35 a economia e verticale ARERA, 20 a esercizi integrati e 15 a prove/ripasso. Fra i primi esercizi distingue tariffa del servizio e prelievo tributario; ogni settimana svolge un calcolo commentato e una mini-AIR. Negli ultimi 20 giorni completa quattro simulazioni, registrando gli errori. La correzione mantiene il programma e introduce prestazioni verificabili: non presume che la quantità di lettura equivalga a preparazione.

**Soglia didattica di controllo:** almeno cinque risposte corrette su sei e una soluzione che rispetti il monte ore; non è la soglia di ammissione di un concorso. Nel Diario annota errore, correzione e data del richiamo.

**Riferimenti e strumenti.** Il bando target, il programma allegato e le rettifiche sono le fonti della selezione. Il corpus storico comprende, fra gli altri, [AGCM 2024, funzionari giuristi](https://www.agcm.it/dotcmsdoc/concorsi-e-praticantato/2024F6G_Bando_Funzionari_giuristi.pdf) e [Banca d'Italia 2025, 60 laureati con orientamento giuridico](https://www.bancaditalia.it/chi-siamo/lavorare-bi/informazioni-concorsi/2025/bando-60-giuristi/index.html): sono esempi datati, non bandi aperti promessi al lettore. Per organi e fonti istitutive usa il repertorio del capitolo 2; per prove complete il capitolo 15.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true');p.write_text(s,encoding='utf8')
print('Chapter 1: links, profiles, calendars, six questions and solved case applied.')
