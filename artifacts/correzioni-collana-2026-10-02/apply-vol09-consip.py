from pathlib import Path
import importlib.util
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-consip-strumenti-obblighi-2026-10-03.md'
slug='07-consip-mepa-aq-sdapa-asp';t=u.read(slug)
t=u.replace(t,'Serve per acquisti di beni, servizi e, nei casi previsti, lavori di manutenzione entro il perimetro consentito dalla disciplina vigente e dalle categorie abilitate.','Serve per acquisti di beni, servizi e lavori sotto la soglia europea, entro le categorie abilitate: il suo perimetro non è limitato ai soli lavori di manutenzione.')
anchor='### Convenzioni: adesione a condizioni già definite\n'
t=u.replace(t,anchor,'''### Obblighi e facoltà: partire dall’ente, dalla categoria e dal valore

La scelta non dipende soltanto dalla convenienza del catalogo. Le norme sulla razionalizzazione degli acquisti pongono obblighi diversi secondo **amministrazione, merceologia e valore**. Il regime va letto insieme al Codice: art. 62 per la qualificazione, art. 50 o altre disposizioni per la procedura, artt. 21–28 per il ciclo digitale. La soglia di 5.000 euro del mercato elettronico non è quella dell’affidamento diretto, né quella della qualificazione.

| Ambito | Regola di partenza | Fonte e controllo |
| --- | --- | --- |
| Amministrazioni statali, scuole e università | Convenzioni quadro Consip; completamento con AQ/SDAPA secondo il regime applicabile | L.296/2006, art.1,c.449; L.160/2019, art.1,c.583; verificare eccezioni specifiche, anche per ricerca e didattica universitaria |
| Enti nazionali di previdenza/assistenza e agenzie fiscali | Obblighi specifici di approvvigionamento centralizzato; non equipararli senza verifica a un Comune | Commi449–450 e583, secondo soggetto e acquisto |
| Enti territoriali e altre PA, acquisti ordinari | Convenzioni generalmente facoltative con rispetto dei parametri prezzo/qualità; restano obblighi per categorie particolari | L.296/2006,c.449; art.26 L.488/1999, con le eccezioni previste |
| Beni/servizi da5.000 euro e sottoUE | Mercato elettronico o strumenti alternativi consentiti dal comma450 secondo il tipo di amministrazione | L.296/2006,c.450; per le altre PA MePA, altri mercati elettronici o sistema telematico della centrale regionale |
| Enti del SSN | Convenzioni regionali o, in mancanza, Consip; acquisti telematici secondo disciplina sanitaria | L.296/2006,c.449; DL95/2012,art.15,c.13,d; esenzione da quest’ultimo obbligo sotto1.000 euro |
| Informatica e connettività delle amministrazioni e società incluse nel conto consolidato ISTAT | Strumenti di acquisto/negoziazione Consip o soggetti aggregatori per beni e servizi disponibili | L.208/2015,c.512; eventuale deroga specifica del c.516 |

La tabella è una mappa normativa: non annulla discipline di settore, regionali o quelle delle singole categorie. Per energia, gas, carburanti, combustibili, telefonia e ulteriori categorie previste opera anche l’art. 1, comma 7, del DL95/2012. Per gli acquisti rientranti nell’art. 9, comma 3, del DL66/2014 si applica il decreto sulle categorie dei soggetti aggregatori.

### Categorie dei soggetti aggregatori: aggiornamento 2026

Il **DPCM11 febbraio2026**, pubblicato nella Gazzetta Ufficiale del16 aprile2026, sostituisce gli obblighi del DPCM11 luglio2018 dalla pubblicazione. Individua trenta categorie. Per ricordarle, separa due fasce, senza confonderle con i limiti dell’art.50:

| Soglia del decreto | Categorie da riconoscere |
| --- | --- |
| 40.000 euro | Farmaci, vaccini, ausili per incontinenza, medicazioni generali e speciali, aghi/siringhe, gestione apparecchiature elettromedicali, pulizia/ristorazione/lavanderia SSN, rifiuti sanitari, vigilanza armata, guardiania, guanti, suture, trasporto scolastico, arredi |
| Soglia UE subcentrale servizi/forniture:216.000 nel2026–2027 | Stent, protesi d’anca e ginocchio, defibrillatori, pacemaker, facility management, pulizia immobili, manutenzione immobili/impianti, ossigenoterapia, diabetologia territoriale, manutenzione strade come servizi/forniture, suturatrici, gestione/manutenzione aree verdi |

Le soglie riguardano il massimo annuo a base d’asta negoziabile autonomamente per categoria; **per una gara pluriennale si considera la base d’asta dell’intero periodo**. L’ambito soggettivo è quello dell’art.9,c.3: amministrazioni statali interessate, regioni ed enti regionali, enti locali e loro consorzi/associazioni, SSN, con le esclusioni previste per scuole e università da questo specifico regime. Queste esclusioni non cancellano gli altri obblighi Consip.

Per le categorie individuate, il blocco del rilascio del CIG alle stazioni che non ricorrono a Consip o aggregatore opera dalla data di attivazione del relativo contratto, secondo l’art.1,c.3 del decreto. Non basta trovare il nome di una categoria: occorre identificare l’iniziativa attiva pertinente. **Caso:** trasporto scolastico da30.000 euro annui per tre anni ha base90.000; non si confrontano solo30.000 con40.000 per evitare il regime aggregato.

### Quando lo strumento obbligatorio non è idoneo o disponibile

L’assenza di una convenzione non rende automaticamente libero ogni acquisto. Vanno verificati altri strumenti obbligatori e le condizioni della deroga. Per convenzione non idonea per mancanza di caratteristiche essenziali, il comma510 della L.208/2015 richiede autorizzazione specificamente motivata dell’organo di vertice amministrativo, trasmessa alla Corte dei conti. Per convenzione indisponibile e motivata urgenza, l’art.1,c.3 del DL95/2012 consente contratti limitati a durata e misura necessarie, con condizione risolutiva per sopravvenuta disponibilità.

Per **ICT**, il comma516 consente procedere autonomamente in caso di indisponibilità o inidoneità rispetto allo specifico bisogno, oppure necessità e urgenza per continuità amministrativa, previa autorizzazione motivata del vertice e comunicazione ad ANAC e AGID. Il fascicolo deve documentare il bisogno essenziale e il confronto con gli strumenti disponibili. “Il fornitore abituale è più comodo” non dimostra l’inidoneità.

**Tre decisioni risolte.** Un Comune compra cancelleria ordinaria per8.000 euro: diretto consentito per valore, ma deve rispettare il comma450 e gli obblighi digitali. Lo stesso Comune compra cancelleria per4.000 euro: l’esenzione specifica dal mercato elettronico non lo esenta da CIG, motivazione e ciclo digitale. Per software da4.000 euro non può usare automaticamente la stessa conclusione: deve considerare anche il comma512 relativo all’ICT. Importo e oggetto vanno letti insieme.

''' + anchor)
anchor='MEPA: catalogo, ordine e negoziazione\n'
t=u.replace(t,anchor,'''### Accordo quadro: applicare l’art.59

Nei settori ordinari la durata dell’accordo quadro non supera **quattro anni**, salvo casi eccezionali motivati. Stazioni ammesse e operatori sono quelli individuati dalla procedura istitutiva; il contratto attuativo non può cambiare sostanzialmente le condizioni né uscire dal tipo di prestazioni previste.

Con un solo operatore, si applicano le condizioni dell’accordo e si può chiedere per iscritto di completare l’offerta se necessario. Con più operatori, si distinguono tre assetti: tutti i termini e i criteri oggettivi di assegnazione già stabiliti, quindi nessun nuovo confronto; termini incompleti, quindi riapertura; modalità mista, solo se prevista nei documenti iniziali con criteri oggettivi. Nel confronto si consultano per iscritto gli operatori dell’accordo in grado di eseguire, si concede un termine adeguato e si valutano offerte secondo criteri già fissati.

**Caso:** un AQ multioperatore assegna le richieste per area geografica e percentuali prestabilite. L’ente non può scegliere liberamente l’impresa preferita. Se invece l’AQ prevede un rilancio per definire un progetto specifico, non può sostituirlo con un ordine senza confronto. La decisione spiega quale delle modalità previste si applica e con quali dati; non inventa una regola dopo l’aggiudicazione dell’accordo.

''' + anchor)
anchor='Gare in ASP: piattaforma e procedura telematica\n'
t=u.replace(t,anchor,'''### SDAPA: apertura continua e appalti specifici

L’art.32 disciplina un procedimento interamente elettronico per acquisti di uso corrente, con caratteristiche disponibili sul mercato. Si applicano le regole della procedura ristretta con adattamenti: **tutti gli operatori idonei sono ammessi**, senza limitarne il numero; possono chiedere ammissione per l’intera durata del sistema. Il bando ne indica il periodo di validità: non si applica automaticamente il limite quadriennale dell’accordo quadro.

Per ogni appalto specifico sono invitati tutti gli ammessi al sistema o alla categoria corrispondente. Nei settori ordinari, termine iniziale per le domande almeno30 giorni dalla trasmissione del bando; offerte almeno10 giorni dall’invito, fatto salvo il regime dell’art.72,c.5. La valutazione delle nuove domande avviene entro10 giorni lavorativi, estendibili a15 nei casi motivati previsti; particolari condizioni valgono prima del primo invito. Il DGUE può essere richiesto aggiornato entro5 giorni lavorativi. Non si impongono contributi amministrativi agli operatori per partecipare al sistema.

**Caso:** al sistema sono ammessi40 operatori della categoria richiesta. La stazione non può sceglierne soltanto5 applicando meccanicamente il minimo della negoziata sotto soglia: deve invitare tutti gli ammessi alla categoria. Se un operatore si abilita successivamente, l’apertura del sistema gli permette di concorrere agli appalti successivi secondo le regole; non riapre da sola una competizione già conclusa.

''' + anchor)
t=u.replace(t,'Le gare in ASP riguardano l\'uso di un ambiente telematico per gestire procedure di gara.','Le gare in ASP (Application Service Provider) utilizzano gratuitamente la piattaforma telematica con supporto Consip per procedure gestite dall’amministrazione, riguardanti beni, servizi, lavori e concessioni di servizi.')
u.save(slug,t,['V09-17','V09-18','V09-19'],u.REF)
slug='04-progettazione-gara-documenti';t=u.read(slug)
t=u.replace(t,'si assume che non si tratti di un progetto di investimento pubblico e che non siano attive convenzioni obbligatorie pertinenti.','si assume che non si tratti di un progetto di investimento pubblico. L’istruttoria documenta l’assenza, negli strumenti Consip e degli aggregatori, di una soluzione idonea alle interfacce essenziali già descritte; il vertice amministrativo ha autorizzato motivatamente la deroga ICT del comma516 della L.208/2015, con comunicazione ad ANAC e AGID. Questa è una condizione espressa del caso: la sola assenza di convenzioni non basterebbe, come spiega il capitolo7.')
u.save(slug,t,['V09-17'],u.REF);u.record()
p=Path('wiki/topics/vol-09-appalti-pnrr-procurement.md');p.write_text(p.read_text(encoding='utf8')+'\n- Strumenti e obblighi Consip, nuovo DPCM2026: [[sources/vol-09-consip-strumenti-obblighi-2026-10-03]].\n',encoding='utf8')
