from pathlib import Path
import shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/06-materie-riuso-specialistiche.md');t=p.read_text(encoding='utf-8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-06.md');assert not a.exists();shutil.copyfile(p,a)
t=t.replace('**Apertura editoriale.** ','').replace('nel usare','nell’usare')
t=t.replace('> **Doppio binario.** Verifica sempre se la sezione riguarda il livello base, quello ispettivo o entrambi; non trasferire automaticamente regole e dati da un corpo o da un binario all’altro.\n\n','')
pos=t.index('## Obiettivo del capitolo')
t=t[:pos]+'''Questo capitolo è una guida alla distribuzione delle materie e alle distinzioni essenziali fra funzioni. Non è un corso completo di diritto penale o procedura penale: se il programma richiede quelle discipline, la mappa serve a organizzarne lo studio sistematico e a controllare la copertura, non a sostituirla. Le destinazioni qui indicate hanno un oggetto preciso; nessuna singola introduzione agli atti di polizia giudiziaria copre l’intero codice.

''' +t[pos:]
pos=t.index('La conseguenza pratica è che il bando non va studiato per righe isolate.')
t=t[:pos]+'''### Destinazioni di studio e limiti del riuso

- Per organizzare banca e ripassi: [[books/il-metodo-bando/chapters/banca-dati-ufficiale-studiarla-senza-memorizzare-male#Il protocollo in quattro fasi|VOL-01, Banca dati ufficiale: protocollo in quattro fasi]]. Il rinvio copre mappatura, classificazione, ripetizione e simulazione, non le materie giuridiche dei quesiti.
- Per la sequenza amministrativa: [[books/il-metodo-bando/chapters/diritto-amministrativo-per-candidati#3. Procedimento amministrativo|VOL-01, Diritto amministrativo: procedimento]]. Copre avvio, istruttoria, decisione e termini generali; i poteri settoriali richiedono la propria disciplina.
- Per la costruzione della notizia di reato: [[books/moduli/m-fl04-polizia-locale/chapters/07-polizia-giudiziaria-atti-essenziali#N-FL04-07-02 · Notizia di reato e comunicazione al pubblico ministero|VOL-02, Polizia giudiziaria: comunicazione al pubblico ministero]]. Riusa la sequenza fatto, fonti, attività, soggetti e destinatario; non trasferire i limiti delle qualifiche della Polizia locale ai corpi statali.
- Per distinguere titolo, controllo e autorità: [[books/moduli/m-fl04-polizia-locale/chapters/08-tulps-pubblica-sicurezza-immigrazione#N-FL04-08-01 · TULPS, titoli e polizia amministrativa|VOL-02, TULPS: titoli e polizia amministrativa]]. Gli esempi locali vanno ricondotti alla competenza del proprio corpo.

Per il programma PS 1.000 vice ispettori 2026, articoli 8–9, la banca comprende penale, procedura penale e costituzionale; all’orale si aggiungono amministrativo e parti di civile. La presente mappa non consente di segnare «penale completo» dopo aver letto il solo nucleo sulla notizia di reato. Nel diario assegna a ogni istituto richiesto una spiegazione, un caso e una verifica; una casella senza destinazione resta un’attività di studio da completare.

''' +t[pos:]
t=t.replace('dalle materie specialistiche, che studia nel modulo M-SP01','dalle materie specialistiche, di cui usa qui la mappa e le destinazioni delimitate, integrando lo studio sistematico richiesto dal programma')
pos=t.index('La distinzione più importante è tra appartenenza al corpo')
t=t[:pos]+'''### Mappa essenziale dei tre corpi

| Corpo | Natura e funzione caratteristica | Fonti di orientamento |
| --- | --- | --- |
| Polizia di Stato | Ordinamento civile; funzioni di ordine e sicurezza pubblica nel sistema coordinato dal Ministero dell’Interno | Legge 121/1981; D.P.R. 335/1982 per il personale che espleta funzioni di polizia |
| Arma dei Carabinieri | Forza armata e forza di polizia a competenza generale; le funzioni di sicurezza non ne cancellano la natura militare | D.Lgs. 66/2010 e D.P.R. 90/2010; legge 121/1981 per il sistema di pubblica sicurezza |
| Guardia di finanza | Ordinamento militare; tutela economico-finanziaria e concorso ai compiti di sicurezza previsti dall’ordinamento | Legge 189/1959; D.Lgs. 199/1995 per personale non direttivo e non dirigente |

Il coordinamento funzionale non equivale alla fusione delle carriere. La qualifica di maresciallo nell’Arma o nella GdF non permette di importare automaticamente disciplina di reclutamento, titoli o ruoli dell’altro corpo. Allo stesso modo, funzioni di polizia giudiziaria e dipendenza nell’organizzazione sono piani diversi: nello svolgimento della funzione giudiziaria conta il rapporto stabilito dal codice con l’autorità giudiziaria, mentre l’appartenenza conserva il proprio ordinamento.

''' +t[pos:]
t=t.replace('autorizzazioni, prescrizioni e regole di pubblica sicurezza vanno trattate sul piano amministrativo.','autorizzazioni e prescrizioni richiedono l’individuazione della disposizione violata e della sua conseguenza. Un’irregolarità del titolo non è necessariamente soltanto amministrativa: la norma può prevedere una sanzione amministrativa o una fattispecie penale. Senza quei dati la classificazione resta da verificare.')
t=t.replace('Se una colonna resta vuota senza motivo, la risposta è incompleta.','Una colonna può indicare «non pertinente» motivandolo: non occorre inventare un reato per riempire tutte le caselle.')
t=t.replace('Ordinamento del corpo, pubblica sicurezza, TULPS, polizia amministrativa, diritto e procedura penale con funzione di polizia giudiziaria appartengono al modulo M-SP01.','Ordinamento, pubblica sicurezza e distinzione delle funzioni appartengono alla mappa di questo capitolo; diritto e procedura penale richiedono lo sviluppo sistematico previsto dal programma, oltre ai rinvii introduttivi già indicati.')
t=t.replace('Le materie come ordinamento del corpo, pubblica sicurezza, polizia amministrativa, diritto e procedura penale con polizia giudiziaria appartengono invece al modulo M-SP01.','Qui uso la mappa di ordinamento, pubblica sicurezza e funzioni; non confondo l’introduzione alla polizia giudiziaria con l’intero programma penale.')
t=t.replace('Esempio: “procedura penale” → “M-SP01”, perché riguarda l’accertamento dei reati e la funzione di polizia giudiziaria.','Esempio: “procedura penale” → “studio specialistico del programma”; per notizia di reato uso il rinvio preciso sopra, senza dichiarare così coperto l’intero codice.')
t=t.replace('- Architettura ConcorsoBook: materia comune nel VOL-01, materia di famiglia nel modulo specialistico corretto, materia di sottoprofilo in appendice o verticale quando la specializzazione è reale.','- D.Lgs. 66/2010 e D.P.R. 90/2010 per l’Arma; legge 189/1959 e D.Lgs. 199/1995 per la Guardia di finanza.')
p.write_text(t,encoding='utf-8');print('SP01/06: limite strategico, funzioni, rinvii verificati, caso autorizzativo')
