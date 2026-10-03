from pathlib import Path
import json,re
B=Path('wiki/books/moduli/m-ir01-scuola/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
def add(n,txt):
 p=next(B.glob(f'{n:02}-*.md'));t=p.read_text(encoding='utf8');a=t.index('\n## Il Bando Decoder');t=t[:a]+'\n'+txt.strip()+'\n'+t[a:];t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8');return str(p).replace('\\','/')
files=[]
files.append(add(7,'''## Le regole del D.I. 129/2018: dal programma al pagamento

L’esercizio finanziario coincide con l’anno solare, non con l’anno scolastico. Il **programma annuale** segue la competenza finanziaria e distingue entrate per fonte e spese per destinazione: attività, progetti e gestioni separate. Le spese complessive non possono superare le entrate; a ciascuna destinazione si collega la scheda illustrativa finanziaria predisposta dal DSGA. Avere denaro in cassa non autorizza una spesa estranea agli stanziamenti e ai vincoli.

Nella procedura ordinaria dell’art. 5, il DS predispone il programma con la collaborazione del DSGA per la parte economico-finanziaria; la giunta esecutiva lo propone al consiglio entro il **30 novembre** dell’anno precedente. Entro la stessa data è sottoposto ai revisori, che rendono di regola il parere entro il **31 dicembre**. Il consiglio approva entro il **31 dicembre**, anche se il parere non è ancora pervenuto; un parere negativo richiede considerazione dei rilievi ed eventuale motivazione del mancato recepimento. Questi sono termini ordinari: una proroga comunicata per un esercizio non diventa la regola permanente.

| Passaggio | Contenuto | Competenza ed evidenza |
| --- | --- | --- |
| Accertamento | Verificare ragione del credito, debitore e somma sulla base di documenti idonei | DSGA; registrazione riferita alla fonte di finanziamento |
| Riscossione | Incassare l’entrata | Istituto cassiere; reversale e riscontro dell’incasso |
| Impegno | Vincolare lo stanziamento per un’obbligazione giuridicamente perfezionata | DS assume, DSGA registra; titolo e disponibilità |
| Liquidazione | Determinare esatto importo dovuto e creditore, verificata regolarità della prestazione | DSGA; documenti giustificativi, fattura e riscontro della fornitura |
| Ordinazione | Disporre il pagamento con mandato | Mandato firmato da DS e DSGA, corredato dalle evidenze |
| Pagamento | Eseguire l’uscita | Istituto cassiere; quietanza e riconciliazione |

L’**impegno** non è il preventivo del fornitore: richiede un’obbligazione perfezionata e non può eccedere lo stanziamento pertinente. La **liquidazione** non coincide con l’arrivo della fattura: per beni, servizi o lavori occorre verificare regolare fornitura o esecuzione. L’**ordinazione** non prova da sola l’avvenuto pagamento. Questa distinzione consente di localizzare una pratica bloccata e di chiedere il documento necessario, senza alterare artificialmente i dati.

A fine esercizio, entrate accertate e non riscosse sono **residui attivi**; spese impegnate e non pagate sono **residui passivi**. Non sono automaticamente errori: rappresentano crediti e debiti ancora da regolare. Devono però mantenere un titolo e una consistenza corretti. Una previsione di entrata mai accertata non diventa residuo attivo solo per aumentare il risultato.

Il **conto consuntivo** comprende conto finanziario e conto del patrimonio con gli allegati previsti. Nella sequenza ordinaria dell’art. 23, il DSGA lo predispone entro il **15 marzo** dell’anno successivo; il DS lo sottopone ai revisori entro la stessa data; il parere è reso entro il **15 aprile**; il consiglio approva entro il **30 aprile**. Il rendiconto rende verificabili gestione e risultato, mentre la relazione spiega il rapporto con gli obiettivi. Non sana automaticamente atti irregolari compiuti durante l’anno.

### Riconciliazione numerica risolta

**Dati originali.** Fondo di cassa iniziale 20.000 euro. Nell’anno: entrate accertate 100.000, riscosse 90.000; spese impegnate 95.000, pagate 80.000. Per semplificare, non esistono residui iniziali né altre operazioni.

- Cassa finale: 20.000 + 90.000 − 80.000 = **30.000 euro**.
- Residui attivi: 100.000 − 90.000 = **10.000 euro**.
- Residui passivi: 95.000 − 80.000 = **15.000 euro**.
- Risultato di amministrazione nel caso: 30.000 + 10.000 − 15.000 = **25.000 euro**.

La verifica alternativa usa il risultato iniziale 20.000 più la differenza di competenza 100.000 − 95.000 = 5.000: totale 25.000. La cassa è invece 30.000, perché una parte serve ancora a pagare debiti. Se 8.000 euro del risultato hanno destinazione vincolata, non sono liberamente destinabili: il risultato complessivo non coincide con la quota disponibile per nuove scelte.

**Domanda.** Si può pagare una fattura di 4.000 euro perché la cassa finale è positiva, anche se l’impegno manca? No: liquidità e legittimità della spesa sono controlli diversi. Occorre ricostruire titolo, stanziamento, assunzione dell’obbligazione e prestazione; il pagamento non può essere usato per occultare il passaggio mancante.'''))
files.append(add(8,'''## Inventario: consegnatario, ricognizione e scarico

Il D.I. 129/2018 attribuisce al **DSGA le funzioni di consegnatario**, ferme le responsabilità del DS. Il consegnatario conserva e gestisce i beni, vigila sul loro uso, cura le scorte e gli adempimenti assegnati. In istituti complessi o distribuiti su più plessi il DS può nominare sub-consegnatari, responsabili dei beni loro affidati. Un docente che utilizza un laboratorio non diventa automaticamente consegnatario generale.

Gli inventari distinguono beni mobili, beni storico-artistici, libri e materiale bibliografico, valori mobiliari, veicoli e natanti, immobili. I beni di terzi concessi in uso sono registrati separatamente con proprietario, titolo e condizioni: possesso materiale e proprietà non coincidono. Per i mobili si annotano almeno provenienza, collocazione, quantità, stato e valore, con numero progressivo. Non si inventariano gli oggetti di facile consumo e, in via generale, i beni mobili fino a 200 euro IVA compresa, salvo che siano elementi di un’universalità di beni di valore superiore alla soglia; sono previste specifiche esclusioni per periodici e libri delle biblioteche di classe.

La **ricognizione** accerta materialmente esistenza, ubicazione e stato dei beni: deve avvenire almeno ogni cinque anni. Il **rinnovo degli inventari e la rivalutazione** almeno ogni dieci anni. Non sono operazioni equivalenti: il controllo fisico può trovare un bene funzionante in un luogo diverso, una perdita o un bene divenuto inutilizzabile, che richiedono trattamenti distinti. Una ricognizione annuale locale più frequente non contraddice il termine massimo della disciplina nazionale.

Lo **scarico** per furto, forza maggiore o inservibilità non consiste nel premere «elimina» nel gestionale. L’art. 33 richiede un provvedimento del DS con motivazione sull’eventuale reintegro a carico dei responsabili o sull’assenza di responsabilità amministrativa. Per il furto si allegano denuncia e relazione del DSGA; per l’inservibilità il verbale della commissione pertinente. Anche l’uscita materiale e il trattamento del rifiuto seguono la disciplina applicabile. Non consegnare un’apparecchiatura dismessa a un privato senza il percorso previsto.

**Scheda compilata originale.** Bene: computer portatile; numero inventario 245; provenienza: acquisto con fattura 18; valore iniziale: 900 euro IVA compresa; collocazione: laboratorio linguistico, plesso A; utilizzatore: docente responsabile del laboratorio; stato: funzionante; documento di presa in carico: verbale 7. Durante la ricognizione il portatile è nel plesso B. Prima si verifica l’assegnazione e si aggiorna la collocazione sulla base del trasferimento documentato: non si presume un furto né si crea una seconda scheda come se fosse un nuovo bene.

**Secondo esito.** Lo stesso bene non viene rinvenuto e risulta una segnalazione di sottrazione. Si ricostruiscono affidamento e circostanze, si attivano denuncia e comunicazioni pertinenti e si forma la documentazione per il provvedimento del DS. Il numero inventariale consente di identificare l’oggetto; non prova, da solo, la colpa dell’ultimo utilizzatore.

### DNSH: vincolo generale, evidenze pertinenti alla misura

Il principio **Do No Significant Harm (DNSH)**, «non arrecare un danno significativo», vincola le misure finanziate dal dispositivo europeo per la ripresa e la resilienza. Nel PNRR non è facoltativo per il solo fatto che la traccia non nomini una scheda ambientale. Cambiano la valutazione, le condizioni, le schede e le evidenze richieste secondo attività e misura; non il vincolo orizzontale.

In un acquisto scolastico finanziato, l’ufficio collega codice del progetto, oggetto, requisiti ambientali pertinenti, documenti del fornitore e verifica dell’esecuzione. Un’attestazione generica priva di riferimento al bene non dimostra il rispetto dei requisiti. La piattaforma ministeriale di gestione del progetto e il sistema ReGiS svolgono funzioni nel flusso di monitoraggio: non presumere che ogni scuola inserisca direttamente ogni dato in ogni sistema. Si seguono le istruzioni della specifica amministrazione titolare, mantenendo il collegamento fra dati caricati e documenti conservati.'''))
files.append(add(9,'''## Il ruolo giuridico del dirigente scolastico

L’art. 25 del D.Lgs. 165/2001 attribuisce al **dirigente scolastico (DS)** gestione unitaria dell’istituzione, legale rappresentanza, responsabilità delle risorse finanziarie e strumentali e dei risultati del servizio. Il DS esercita poteri di direzione, coordinamento e valorizzazione delle risorse umane nel rispetto delle competenze degli organi collegiali. Organizza l’attività secondo efficacia ed efficienza formative ed è titolare delle relazioni sindacali.

La **gestione unitaria** evita che attività didattiche, uffici e servizi procedano come organizzazioni separate. Non significa che tutte le decisioni spettino al DS. Il collegio elabora il PTOF e il consiglio lo approva; il DS definisce gli indirizzi e assume i provvedimenti gestionali di competenza. La libertà di insegnamento non elimina la programmazione collegiale; la direzione non autorizza a imporre ogni scelta metodologica individuale indipendentemente dalle attribuzioni professionali.

Il DS può individuare docenti collaboratori e delegare specifici compiti. Deve restare riconoscibile oggetto e limite della delega: una generica collaborazione non trasferisce automaticamente ogni potere del dirigente. Il DSGA lo coadiuva, sovrintendendo con autonomia operativa ai servizi amministrativi e generali nel quadro delle direttive di massima e degli obiettivi assegnati. Il rapporto non è quello fra decisore assoluto e semplice esecutore: la legge distribuisce attribuzioni e responsabilità proprie.

Il DS presenta periodicamente al consiglio una relazione motivata sulla direzione e sul coordinamento dell’attività formativa, organizzativa e amministrativa. Rendere conto significa spiegare risultati, criticità e scelte rispetto a risorse e obiettivi. Il sistema di valutazione dei risultati dirigenziali ha una disciplina nazionale specifica: non va confuso con la valutazione del singolo docente o con il RAV della scuola.

**Caso originale.** Il PTOF approvato prevede un laboratorio pomeridiano; non sono ancora definite copertura dei servizi, accesso agli spazi e risorse. Il DS verifica la fattibilità e coordina gli atti necessari. Il collegio definisce la progettazione didattica nel proprio ambito; il DSGA predispone l’organizzazione ATA e gli elementi contabili; il consiglio interviene negli atti di competenza, comprese le eventuali variazioni richieste. Il responsabile della sicurezza collabora alle verifiche preventive secondo ruolo. Il fatto che il progetto sia nel PTOF non equivale a ordine di acquisto, autorizzazione allo straordinario o valutazione positiva di ogni rischio.

**Output richiesto.** Una nota di dieci righe deve indicare obiettivo, vincoli, soggetti, atti e controllo finale. Soluzione essenziale: «Attivare il laboratorio dopo verifica di personale, spazi, sicurezza e copertura; incaricare gli uffici delle istruttorie; rispettare le competenze collegiali e le relazioni sindacali pertinenti; formalizzare i provvedimenti; monitorare presenze, attività svolte e risultati attesi». L’efficacia formativa si misura anche sul risultato degli alunni, non sul solo numero di ore pagate.'''))
files.append(add(10,'''## Informazione, confronto e contrattazione: tre esiti diversi

Il CCNL Comparto Istruzione e ricerca 2022–2024, sottoscritto il **23 dicembre 2025**, disciplina le relazioni sindacali con gli artt. 5, 6, 8 e 11. A livello d’istituto, il DS rappresenta la parte pubblica; la parte sindacale comprende la **Rappresentanza sindacale unitaria (RSU)** e le rappresentanze territoriali delle organizzazioni sindacali aventi titolo. Il DSGA fornisce il supporto tecnico di competenza, senza diventare per questo titolare della delegazione pubblica.

L’**informazione** trasmette preventivamente per iscritto dati ed elementi utili a valutare le misure, ed è presupposto per confronto e contrattazione nelle materie previste. Il **confronto** instaura un dialogo approfondito e si conclude con una sintesi delle posizioni: non richiede necessariamente la stipula di un accordo. La **contrattazione integrativa** mira invece a un contratto sulle materie demandate, entro legge, CCNL e risorse. Non può spostare agli interlocutori sindacali attribuzioni che la legge riserva agli organi della scuola.

| Questione d’istituto | Relazione da riconoscere nel CCNL |
| --- | --- |
| Articolazione dell’orario di lavoro | Confronto, art. 11, comma 9, lett. b1 |
| Criteri di assegnazione del personale alle sedi dell’istituto | Confronto, art. 11, comma 9, lett. b2 |
| Ripartizione delle risorse del fondo e determinazione dei compensi | Contrattazione, art. 11, comma 4, lett. c2 |
| Criteri delle fasce di flessibilità in entrata/uscita ATA | Contrattazione, art. 11, comma 4, lett. c6 |

La differenza fra articolazione dell’orario e criteri delle fasce flessibili mostra perché una sola parola non basta per classificare la materia. Non è corretto rispondere «tutto ciò che riguarda l’orario va contrattato». La sessione d’istituto e le procedure rispettano i termini contrattuali; il confronto non può essere simulato con una comunicazione quando la scelta è già irreversibile.

## Sicurezza: responsabilità scolastiche e responsabilità edilizie

Il DS, quale datore di lavoro nel contesto scolastico, organizza prevenzione, valutazione dei rischi, formazione e gestione delle emergenze secondo il D.Lgs. 81/2008. Il **Responsabile del servizio di prevenzione e protezione (RSPP)** offre il supporto tecnico del servizio: non sostituisce il datore di lavoro nelle decisioni che la legge gli attribuisce. Il **Rappresentante dei lavoratori per la sicurezza (RLS)** svolge funzioni partecipative, di consultazione e segnalazione; non è il soggetto che certifica la sicurezza dell’edificio. Addetti alle emergenze e personale devono conoscere compiti e istruzioni del piano locale.

L’amministrazione tenuta a fornire e mantenere l’edificio conserva le competenze sugli interventi strutturali e di manutenzione. I commi 3.1–3.3 dell’art. 18 distinguono questo piano dalle misure gestionali della scuola. L’esenzione di responsabilità del DS prevista dal comma 3.1 è condizionata alla richiesta tempestiva degli interventi e all’adozione delle misure gestionali di competenza nei limiti indicati: una semplice lettera all’ente non giustifica lasciare persone esposte a un pericolo riconosciuto.

Quando rileva un **pericolo grave e immediato**, il DS può interdire in parte o totalmente l’uso dei locali e ordinarne l’evacuazione, con le comunicazioni all’amministrazione competente e all’autorità di pubblica sicurezza previste dall’art. 18. La valutazione dei rischi strutturali e il documento congiunto seguono il quadro nazionale; questo non autorizza un assistente amministrativo a certificare portanza, impianti o agibilità. La scuola attiva chi ha competenza tecnica e, nell’attesa, gestisce l’esposizione al rischio.

**Scenario chiuso.** Durante le lezioni cadono frammenti dal soffitto di un corridoio. Il personale allontana le persone dalla zona pericolosa secondo formazione e piano, impedisce l’accesso senza esporsi e avvisa immediatamente i responsabili; se occorre, attiva i soccorsi. Il DS dispone le misure gestionali urgenti e le comunicazioni, richiede l’intervento all’ente competente e si raccorda con il RSPP. La segreteria registra tempi, segnalazioni e atti dopo l’attivazione della protezione, senza ritardarla per completare il protocollo. La riapertura non deriva dall’assenza di nuove cadute per mezz’ora, ma dai riscontri e dalle decisioni competenti.

**Verifica.** La prima azione è individuare chi ha colpa? No: prima si protegge chi è esposto e si attiva il piano; in parallelo o dopo si documentano fatti e responsabilità. La prevenzione urgente non è una sanzione e non richiede di avere già concluso l’accertamento della causa.'''))
p=next(B.glob('08-*.md'));t=p.read_text(encoding='utf8');t=t.replace('DNSH, quando applicabile','DNSH, con le evidenze pertinenti alla misura').replace('DNSH quando applicabile','DNSH con le evidenze pertinenti alla misura');p.write_text(t,encoding='utf8')
p=next(B.glob('10-*.md'));t=p.read_text(encoding='utf8');t=t.replace('1. registra la segnalazione e separa fatti descritti, dati disponibili e aspetti da verificare;','1. in caso di pericolo grave e immediato, attiva anzitutto la protezione delle persone e il piano locale nel proprio ruolo; registra quindi la segnalazione e distingue i fatti dagli aspetti da verificare;');t=t.replace('1. registra la segnalazione e raccoglie gli elementi utili per distinguere fatto, possibile rischio e problema organizzativo;','1. se emerge un pericolo grave e immediato, attiva prima le misure urgenti di protezione previste dal ruolo e dal piano; raccoglie quindi gli elementi utili a distinguere fatto, rischio e problema organizzativo;');t=t.replace("No. Deve prima raccogliere fatti, verificare il rischio, i documenti, le competenze e i soggetti previsti, quindi attivare il passaggio applicabile.","No. Se vi è pericolo grave e immediato, deve anzitutto proteggere le persone e attivare il piano nel proprio ruolo; la raccolta ordinaria dei documenti non deve ritardare la protezione. Successivamente ricostruisce fatti, competenze e passaggi applicabili.");t=t.replace('**segnalazione -> fatti -> rischio -> fonte e competenza -> raccordo -> evidenza -> verifica**','**protezione urgente, se necessaria → segnalazione → fatti e rischio → competenza → azione → verifica**');p.write_text(t,encoding='utf8')
batch={'V06-06':{'change':'Inseriti programma annuale e consuntivo con ruoli/termini ordinari, fasi entrata/spesa, residui, riconciliazione numerica e inventario con consegnatario/ricognizione/scarico.','files':files[:2],'evidence':'D.I.129 artt.5/23 su GU e12/13/15/16/17/30/31/33 consolidati; caso 30.000+10.000−15.000=25.000 risolto.','status':'applicato'},'V06-07':{'change':'Esposti art.25 D.Lgs.165, relazioni del CCNL23dicembre2025 e ruoli sicurezza/ente edilizio; protezione urgente anteposta alla documentazione nello scenario e nella domanda-trappola.','files':files[2:],'evidence':'Art.25 e art.18, commi3.1–3.3, consolidati; ARAN artt.5/6/11; scenario soffitto risolto rispettando i confini tecnici.','status':'applicato'}}
(A/'VOL-06-batch03.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('IR01 capitoli 07–10 integrati; quota scolastica V06-23 corretta, IR03 ancora da fare.')
