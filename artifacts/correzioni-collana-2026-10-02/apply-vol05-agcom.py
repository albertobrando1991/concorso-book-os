from pathlib import Path
import json
B=Path('wiki/books/moduli/m-fc05-authority-indipendenti');O=Path('artifacts/correzioni-collana-2026-10-02');note='vol-05-agcom-verifica-2026-10-03'
Path('wiki/sources/'+note+'.md').write_text('''---
id: source-vol-05-agcom-verifica-2026-10-03
type: source
title: "VOL-05 — AGCOM: Codice, controversie, DSA e DMA"
status: consolidated
domain: comunicazioni e servizi digitali
topics: ["comunicazioni elettroniche", "media", "controversie", "DSA", "DMA"]
entities: ["AGCOM", "Corecom", "Commissione europea"]
source_refs: ["sources/agcom-comunicazioni-media-utenti-piattaforme-2026-07-24.md", "sources/regolazione-ue-digitale-e-finanziaria-vol-05.md"]
book_refs: ["m-fc05-authority-indipendenti", "vol-05-authority-regolazione"]
confidence: 0.97
updated_at: 2026-10-03
created_at: 2026-10-03
review_required: false
canonical: true
tags: ["vol-05", "correzioni", "agcom"]
source_type: official_legislation_and_authority
source_date: 2026-10-03
authority_level: primary
---

# Comunicazioni e media

Codice D.Lgs. 259/2003, riforma 207/2021; TUSMA D.Lgs. 208/2021: identificativi confermati nelle definizioni art. 1 del regolamento controversie. [AGCOM, comunicazioni elettroniche](https://www.agcom.it/competenze/comunicazioni-elettroniche?page=2) distingue interventi orizzontali e SMP. [Servizi di accesso](https://www.agcom.it/node/1014/printable/print): letta descrizione degli obblighi, senza assumere vigenti per sempre operatori/mercati del provvedimento 2019. [Servizio universale](https://www.agcom.it/sites/default/files/migration/attachment/Allegato%203-1-2024.pdf), passaggio art. 94 letto nell'indice ufficiale, accesso adeguato a banda larga e voce a prezzo accessibile in postazione fissa; nessuna velocità corrente inserita. [Frequenze](https://www.agcom.it/competenze/comunicazioni-elettroniche/reti/frequenze/frequenze-radio-e-TV), ruoli PNRF MIMIT/PNAF AGCOM. [Pluralismo](https://www.agcom.it/sites/default/files/media/allegato/2024/allegato%20A%20delibera%2066-24-cons.pdf), art. 51 TUSMA e SIC, letto estratto ufficiale introduttivo. Non dichiarata lettura completa dei due codici o degli allegati media.

# Controversie

[Pagina normativa 203/18/CONS](https://www.agcom.it/provvedimenti/delibera-203-18-cons) collega il testo aggiornato 194/23/CONS. PDF acquisito in `wiki/raw/correzioni-vol05-2026-10-03/agcom-controversie.pdf` (26 pagine; URL storico del file non coincide con data del contenuto). Letti integralmente artt. 1–7 e 14–22; non dichiarato completo l'intero regolamento. Punti: art. 3 condizione di procedibilità per comunicazioni elettroniche, soddisfatta comunque dopo 30 giorni dall'istanza; art. 6 comma 3-bis, servizi audiovisivi reclamo e risposta insoddisfacente o 30 giorni, istanza entro quattro mesi; art. 14 definizione entro tre mesi dalla chiusura, partecipazione dell'istante alla conciliazione, non pendenza giudizio stesso oggetto/parti; art. 20 ordine, rimborsi/indennizzi e maggior danno riservato al giudice; art. 22 definizione passaggio operatori e audiovisivi riservata ad AGCOM. Il caso corrente del capitolo aveva attribuzione troppo generica al Corecom per la migrazione: precisata.

# DSA e DMA

Fonti normative ufficiali: [DSA 2022/2065](https://eur-lex.europa.eu/eli/reg/2022/2065/), [DMA 2022/1925](https://eur-lex.europa.eu/legal-content/IT/TXT/?uri=CELEX%3A32022R1925). Acquisizione raw EUR-Lex restituita vuota: non prova testuale; manifest ne conserva esito. Verificati estratti indicizzati ufficiali degli artt. 56 commi 1–3 e 66 DSA e art. 3 commi 1–3 DMA; raccordo con [Commissione, enforcement DSA](https://digital-strategy.ec.europa.eu/en/policies/dsa-enforcement) aggiornato 2 luglio 2026 e [AGCOM, soggetti destinatari](https://www.agcom.it/competenze/piattaforme-online/digital-service-act/soggetti-destinatari). Non lettura integrale dei regolamenti.

DSA: Stato dello stabilimento principale, salvo poteri Commissione; esclusiva Commissione per capo III sezione 5, ma anche poteri sugli altri obblighi delle VLOP/VLOSE. Avvio Commissione esclude l'esercizio nazionale sui medesimi fatti per evitare duplicazione. Obblighi progressivi servizi intermediari, hosting, piattaforme, marketplace, VLOP/VLOSE; esenzioni micro/piccole specifiche, non esenzione generale DSA. Reclami art. 53 al DSC del luogo del destinatario, distinto dall'autorità competente a decidere.

DMA art. 3: tre requisiti qualitativi; presunzioni quantitative 7,5 miliardi fatturato UE in ciascuno di tre esercizi oppure 75 miliardi capitalizzazione media/equo valore nell'ultimo, medesimo servizio in almeno tre Stati; 45 milioni utenti finali mensili e 10.000 commerciali annui nell'ultimo esercizio; persistenza di queste ultime soglie in tre esercizi. Designazione Commissione, possibile anche secondo accertamento qualitativo; non equivalenza VLOP/gatekeeper. [Consiglio UE, pacchetto digitale](https://www.consilium.europa.eu/en/policies/digital-services-package/) e [portale DMA](https://digital-markets-act.ec.europa.eu/index_en) riscontri di contesto.

Collegamenti: [[topics/authority-rettifiche-2026]]; [[books/moduli/m-fc05-authority-indipendenti/chapters/10-agcom-comunicazioni-media-utenti-piattaforme]].
''',encoding='utf8')
t=Path('wiki/topics/authority-rettifiche-2026.md');t.write_text(t.read_text(encoding='utf8')+'\n\n## AGCOM e servizi digitali\n\n[[sources/'+note+']] integra Codice/TUSMA, rimedi e termini delle controversie, progressione obblighi DSA e riparto completo Commissione/DSC, criteri DMA distinti dalla designazione VLOP.\n',encoding='utf8')
p=B/'chapters/10-agcom-comunicazioni-media-utenti-piattaforme.md';s=p.read_text(encoding='utf8')
pos=s.index('## N-MF05-10-02')
s=s[:pos]+'''### Codice e TUSMA: le basi da usare nel caso

Il **Codice delle comunicazioni elettroniche è il D.Lgs. 259/2003**, profondamente riformato dal D.Lgs. **207/2021** in attuazione del Codice europeo. Il **TUSMA è il D.Lgs. 208/2021**. I due numeri consecutivi del 2021 non indicano lo stesso testo: reti e trasporto dei segnali si distinguono dalla responsabilità editoriale sui servizi media.

La regolazione dei mercati può richiedere l'individuazione di un operatore con **significativo potere di mercato (SMP)**, posizione assimilabile alla dominanza. Dopo definizione e analisi del mercato, AGCOM può imporre rimedi proporzionati al problema: accesso alle risorse, trasparenza delle condizioni, non discriminazione, separazione contabile e controllo dei prezzi secondo i presupposti del Codice. Non è la sanzione per un abuso antitrust già provato: la regolazione ex ante affronta un problema strutturale. Altri obblighi sono orizzontali o simmetrici e non richiedono necessariamente un previo accertamento SMP.

**Accesso** significa poter usare risorse o servizi di un altro operatore alle condizioni consentite; **interconnessione** collega reti per permettere agli utenti di comunicare o accedere ai servizi. Se un concorrente chiede accesso a un'infrastruttura, occorrono mercato, titolo dell'obbligo, fattibilità e condizioni; non basta invocare il pluralismo televisivo. Il **servizio universale**, invece, assicura ai consumatori disponibilità e accessibilità economica di un accesso adeguato a internet a banda larga e di comunicazioni vocali in postazione fissa, secondo la disciplina: non promette gratuitamente qualsiasi velocità o tecnologia.

Lo **spettro radio** è una risorsa scarsa: gestione delle interferenze, uso efficiente e accesso richiedono pianificazione e diritti d'uso. Il MIMIT elabora il Piano nazionale di ripartizione delle frequenze, che attribuisce le bande ai servizi; AGCOM elabora i piani di assegnazione di competenza e le regole regolatorie. Non è corretto attribuire ad AGCOM da sola ogni attività ministeriale di rilascio o gestione dei diritti.

Nel TUSMA il **pluralismo esterno** riguarda la pluralità effettiva di fonti e operatori; quello **interno** la possibilità di esprimere differenti orientamenti nel servizio, secondo gli obblighi applicabili. L'articolo 51 considera posizioni di significativo potere lesive del pluralismo nel **Sistema integrato delle comunicazioni (SIC)** e nei mercati che lo compongono. Non è sufficiente contare i canali: controllo comune, accesso alle risorse e incidenza sull'informazione possono ridurre la pluralità sostanziale. Tutela dei minori e comunicazioni commerciali richiedono poi regole proprie, anche per servizi a richiesta e piattaforme di condivisione video nei rispettivi ambiti.

'''+s[pos:]
pos=s.index('![Figura 10.3')
s=s[:pos]+'''### Tre moduli, tre funzioni e termini da distinguere

Nel regolamento **203/18/CONS, aggiornato dalla 194/23/CONS**, la procedura tramite Conciliaweb mantiene passaggi distinti:

| Strumento | Funzione e limite |
| --- | --- |
| UG: conciliazione | Ricerca un accordo; nelle controversie di comunicazioni elettroniche comprese nel regolamento è condizione di procedibilità del giudizio. |
| GU5: misura temporanea | Chiede tutela della continuità del servizio o della numerazione durante conciliazione/definizione; non liquida il maggior danno. |
| GU14: definizione | Dopo mancato accordo, o sui punti residui, chiede una decisione amministrativa nei limiti previsti. |

Ai fini dell'azione giudiziale, la condizione si considera comunque avverata trascorsi **30 giorni dalla presentazione dell'istanza di conciliazione**: non è un termine di prescrizione del diritto e non significa che ogni controversia sia già decisa. L'istanza di definizione deve essere proposta **entro tre mesi dalla conclusione del tentativo**; non è ammissibile se pende un giudizio di merito sullo stesso oggetto tra le stesse parti. Chi ha presentato la conciliazione senza parteciparvi non può poi chiedere la definizione, ferma la tutela giudiziaria. Ripetere il tentativo non fa ripartire il termine.

La definizione può ordinare cessazione della condotta lesiva, **rimborso di somme non dovute e indennizzi** previsti da contratto, carta dei servizi o disciplina. Il maggior danno resta al giudice: non si confonde l'indennizzo parametrato al disservizio con il risarcimento completo di una perdita d'impresa. L'ordine conclusivo è vincolante e la sua inosservanza è sanzionabile; non è una proposta conciliativa.

La competenza è del Corecom delegato nei casi ordinari; la **definizione dei disservizi nel passaggio tra operatori è riservata ad AGCOM**, come quella delle controversie con fornitori di servizi media audiovisivi. Per questi ultimi la conciliazione richiede un previo reclamo e risposta insoddisfacente oppure almeno 30 giorni dall'invio; l'istanza va presentata entro quattro mesi dal reclamo. Non si trasferiscono automaticamente ai servizi audiovisivi tutte le condizioni delle controversie telefoniche.

'''+s[pos:]
pos=s.index('Il candidato deve ricordare soprattutto tre conseguenze.')
s=s[:pos]+'''Il riparto completo dell'**articolo 56 del regolamento UE 2022/2065** aggiunge una precisazione decisiva: la Commissione può vigilare sulle VLOP e VLOSE **anche per gli altri obblighi DSA**, oltre alla sua esclusiva sul capo III, sezione 5. Per questi altri obblighi conserva competenza lo Stato dello stabilimento principale finché non interviene l'avvio del procedimento della Commissione per la medesima violazione; l'articolo 66 evita duplicazioni. Un servizio accessibile in Italia non diventa per questo stabilito in Italia. Il reclamo del destinatario ad AGCOM ai sensi dell'articolo 53 può quindi richiedere trasmissione e cooperazione con il DSC competente.

### Gli obblighi DSA crescono con il servizio

| Categoria | Esempi di obblighi da distinguere |
| --- | --- |
| Servizi intermediari | Punti di contatto, condizioni d'uso trasparenti e obblighi di rendicontazione nei termini previsti. Comprendono semplice trasporto, memorizzazione temporanea e hosting. |
| Hosting | Meccanismi per segnalare contenuti illegali e motivazione di determinate restrizioni; memorizzano informazioni fornite dall'utente. |
| Piattaforme online | Hosting che diffondono informazioni al pubblico; sistemi interni di reclamo, ADR, trasparenza di pubblicità e raccomandazioni, protezione dei minori secondo l'ambito. |
| Marketplace | Per quelli che consentono contratti a distanza consumatore–professionista, anche tracciabilità degli operatori commerciali e progettazione conforme. |
| VLOP e VLOSE designate | Valutazione e attenuazione dei rischi sistemici, revisione indipendente e ulteriori obblighi del capo III, sezione 5. |

Gli articoli 19 e 29 prevedono specifiche esenzioni per microimprese e piccole imprese: non una generale immunità dal DSA. La qualifica di VLOP/VLOSE richiede la designazione della Commissione, sulla base della soglia e delle condizioni regolamentari; non coincide con la designazione di gatekeeper DMA. Il divieto di imporre un obbligo generale di sorveglianza non esonera dagli obblighi specifici di gestione delle segnalazioni.

'''+s[pos:]
s=s.replace('![Figura 10.4 — Distinzioni essenziali: AGCOM: comunicazioni e piattaforme.](../assets/chapter-10/04-distinzioni-agcom-media-piattaforme.png)\n\n## N-MF05-10-03 · Poteri, procedura e conseguenze\n\n*Figura 10.4 — La tavola evidenzia le distinzioni da controllare prima di rispondere.*','![Figura 10.4 — Distinzioni essenziali: AGCOM: comunicazioni e piattaforme.](../assets/chapter-10/04-distinzioni-agcom-media-piattaforme.png)\n\n*Figura 10.4 — La tavola evidenzia le distinzioni da controllare prima di rispondere.*\n\n## N-MF05-10-03 · Poteri, procedura e conseguenze')
pos=s.index('Un\'impresa segnala che una piattaforma combina dati')
s=s[:pos]+'''Nel **regolamento UE 2022/1925 (DMA)** il gatekeeper è un'impresa designata dalla Commissione perché ha un impatto significativo sul mercato interno, offre un servizio di piattaforma di base che è un punto di accesso importante per gli utenti commerciali e possiede una posizione consolidata e duratura, o destinata a diventarlo. I servizi possono comprendere ricerca, intermediazione, social network, sistemi operativi e altri servizi elencati: non ogni sito commerciale.

L'articolo 3 pone presunzioni quantitative, da applicare correttamente:

1. **Impatto:** fatturato UE di almeno 7,5 miliardi in ciascuno degli ultimi tre esercizi **oppure** capitalizzazione media o valore equo equivalente di almeno 75 miliardi nell'ultimo; inoltre lo stesso servizio di piattaforma di base è offerto in almeno tre Stati membri.
2. **Accesso:** per il servizio, nell'ultimo esercizio almeno 45 milioni di utenti finali attivi mensili nell'UE **e** 10.000 utenti commerciali attivi annui stabiliti nell'UE.
3. **Durata:** le soglie del secondo punto sono raggiunte in ciascuno degli ultimi tre esercizi.

Sono presunzioni nel procedimento di designazione, non una sanzione automatica; è possibile anche l'accertamento qualitativo previsto dal regolamento. La sola capitalizzazione elevata non completa la verifica. Una volta designati, i gatekeeper devono rispettare obblighi su equità e contendibilità, per esempio accesso ai dati generati dagli utenti commerciali, divieti di trattamenti preferenziali e condizioni per combinare dati, secondo lo specifico articolo. Il DMA integra, senza sostituire, gli articoli 101–102 TFUE: non occorre dimostrare un abuso antitrust per ogni obbligo ex ante.

'''+s[pos:]
s=s.replace('Il Corecom può essere coinvolto nell\'ambito delle funzioni delegate e della procedura prevista.',"Il Corecom può svolgere la conciliazione nelle funzioni delegate; se il disservizio riguarda il passaggio tra operatori, la successiva definizione è invece di competenza AGCOM ai sensi dell'articolo 22.")
a=s.index('### Laboratorio di qualificazione');s=s[:a]+'''## N-MF05-10-05 · Consolidamento e verifica

### ▣ Verifica ragionata

**Quesito 1.** Un operatore è individuato come SMP. Ogni rimedio di accesso è una sanzione per abuso già accertato?

**Risposta corretta:** no. Il Codice delle comunicazioni elettroniche consente regolazione ex ante proporzionata al problema concorrenziale; la sanzione antitrust richiede una distinta fattispecie. TUSMA 208/2021 e Codice 259/2003 riformato dal 207/2021 non coincidono.

**Quesito 2.** Mancata conciliazione conclusa il 10 febbraio; GU14 proposto il 20 giugno. La definizione è tempestiva perché l'utente ha ripetuto il tentativo a maggio?

**Risposta corretta:** no. Il termine è tre mesi dalla prima conclusione; il tentativo successivo sulla stessa controversia non lo riapre. Resta da valutare la tutela giudiziaria, senza confondere la decadenza dalla procedura con l'estinzione del diritto sostanziale.

**Quesito 3.** Dopo un disservizio di migrazione, il Corecom può sempre decidere il GU14 e liquidare il maggior danno?

**Risposta corretta:** no. La definizione dei disservizi nel passaggio tra operatori compete ad AGCOM. Rimborsi e indennizzi regolatori si distinguono dal maggior danno riservato al giudice.

**Quesito 4.** Per una VLOP la Commissione può intervenire soltanto sui rischi sistemici?

**Risposta corretta:** no. Ha esclusiva sul capo III, sezione 5, e poteri anche sugli altri obblighi DSA. L'avvio del suo procedimento esclude la duplicazione dell'azione nazionale sulla medesima violazione, secondo gli articoli 56 e 66.

**Quesito 5.** Un servizio di cloud hosting, senza diffusione al pubblico, è automaticamente una piattaforma online soggetta a tutti gli obblighi delle VLOP?

**Risposta corretta:** no. Hosting, piattaforma e VLOP sono livelli distinti; diffusione al pubblico e designazione contano. All'hosting si applicano gli obblighi pertinenti, inclusi meccanismi di segnalazione e motivazione nei casi previsti, senza attribuirgli ogni obbligo supplementare.

**Quesito 6.** Un'impresa vale 80 miliardi, ma offre il servizio in un solo Stato e ha 2.000 utenti commerciali annui. Soddisfa tutte le presunzioni quantitative DMA?

**Risposta corretta:** no. Mancano almeno tre Stati e 10.000 utenti commerciali, oltre agli altri controlli richiesti. Non si esclude per ciò solo ogni possibile designazione qualitativa; si esclude la conclusione automatica fondata sul valore di mercato.

### Caso ragionato di chiusura

**Traccia.** Una VLOP con stabilimento principale in un altro Stato UE sospende un account italiano. Lo stesso utente contesta un doppio addebito durante la migrazione telefonica. Chiede al Corecom una decisione unica su entrambe le vicende e 20.000 euro per perdita di affari. Quali documenti e percorsi servono?

**Soluzione.** Per l'account: decisione e motivazione, condizioni d'uso, eventuale reclamo interno e identificazione del servizio; si valutano gli obblighi DSA e il reclamo ad AGCOM quale DSC del destinatario, con cooperazione verso lo Stato di stabilimento e verifica dell'eventuale procedimento Commissione. Per gli addebiti: contratti, fatture, data di migrazione e reclamo; conciliazione e, nei termini, definizione AGCOM per il disservizio nel passaggio tra operatori. La richiesta di 20.000 euro di maggior danno richiede tutela giudiziaria e prova, mentre rimborsi/indennizzi seguono il loro regime. Il Corecom non acquisisce una competenza generale DSA per il fatto di avere ricevuto il reclamo telefonico.

**Autovalutazione:** un punto per la separazione dei fascicoli, uno per stabilimento/Commissione, uno per definizione AGCOM, uno per danno distinto dall'indennizzo.

**Riferimenti normativi e professionali.** Legge 249/1997; D.Lgs. 259/2003, riformato dal D.Lgs. 207/2021; TUSMA, D.Lgs. 208/2021, articolo 51; regolamento controversie 203/18/CONS aggiornato dalla 194/23/CONS, articoli 2–6, 14, 20 e 22; DSA, regolamento UE 2022/2065, articoli 19, 29, 53, 56 e 66; DMA, regolamento UE 2022/1925, articoli 3, 5–7. [AGCOM, regolamento e aggiornamenti](https://www.agcom.it/provvedimenti/delibera-203-18-cons). Verifica al 3 ottobre 2026.
'''
s=s.replace('updated_at: 2026-08-22','updated_at: 2026-10-03').replace('draft_stage: frozen','draft_stage: revision-in-progress').replace('review_required: false','review_required: true').replace('source_refs: [','source_refs: ["sources/'+note+'.md", ',1).replace('last_compiled_from: [','last_compiled_from: ["wiki/sources/'+note+'.md", "wiki/topics/authority-rettifiche-2026.md", ',1);p.write_text(s,encoding='utf8')
f=O/'VOL-05-progress.json';d=json.loads(f.read_text(encoding='utf8'));d['chaptersApplied']=list(range(1,11));d['chaptersReadThisCycle']=list(range(1,11));d['findingsFullyApplied']+=['V05-18','V05-19'];d['findingsPartiallyApplied']['V05-02']='Capitoli 1–10: 60 quesiti e 10 casi specifici';f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
f=O/'VOL-05-reading-checkpoint.json';d=json.loads(f.read_text(encoding='utf8'));d['files'][9]['readComplete']=True;f.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8');print('Applied chapter 10.')
