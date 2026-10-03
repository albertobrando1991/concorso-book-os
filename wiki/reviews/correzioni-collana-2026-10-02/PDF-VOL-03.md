# Revisione dell’impaginato corrente — VOL-03

## 1. Sintesi

Prova interna del 3 ottobre 2026: **813 pagine**, 50 capitoli/appendici, 3 moduli, 144 nuclei e 194 voci d’indice. I 70 diagrammi testuali raster sono stati sostituiti da schemi nativi leggibili e corretti nel significato. Il PDF è un candidato tecnico revisionato: rimangono aperte le dipendenze comuni sui servizi digitali e sui dati editoriali. Nessun via libera step 24.

SHA-256 PDF: `32e25d31b712ca18af78053e7f62daab47ea266106ca52dae16cd8407eff718c`.

## 2. Punti di forza

Progressione Ministeri, Agenzie fiscali, EPNE; casi e quiz preservati rispetto al freeze testuale. Le tabelle mantengono confronti e alternative senza false frecce di sequenza. I workbook più densi hanno spazio di compilazione verticale. Indice e rinvii usano la numerazione globale del volume.

## 3. Interventi verificati

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|---|---|---|---|---|---|---|
| P03-01 | Indice, pp. 6–11 | Tipografia | grave | Indice precedente a 6,75 pt. | Indice corrente a 9,5 pt; 194 destinazioni verificate direttamente nel PDF. | Corretto e verificato |
| P03-02 | Capitoli 13, 14 e 31; tre workbook | Usabilità | grave | Otto/dieci colonne spezzavano le parole e riducevano lo spazio di scrittura. | Tre schede verticali a due colonne; campi vuoti con due righe; contenuti originali conservati. | Corretto e verificato |
| P03-03 | Capitoli 30–31; mappe, appendici e rinvii | Layout e navigazione | medio | Riga Output isolata, schemi ridondanti illeggibili e slug visibili. | Mappa BANDO a due colonne; schemi nativi; etichette umane per 126 link e allineamento di 113 righe di rinvii. | Corretto e verificato |
| P03-04 | Sequenza capitoli fiscali 20–23 | Struttura | grave | 05a e 05b erano collocati dopo le appendici. | Ordine 05,05a,05b,06; indice globale 20,21,22,23 e riscontro dei titoli fisici. | Corretto e verificato |
| P03-05 | Schemi 30.1,31.1,31.2,31.5 | Correttezza didattica | grave | Espansione BANDO e mappa delle appendici non corrispondevano al testo. | Bando/Aree/Nuclei/Diario/Output; appendici A–H corrispondenti ai contenuti effettivi. | Corretto e verificato |
| P03-06 | Schemi 20.2,23.3,24.3,25.4,29.3,30.3 | Correttezza didattica | grave | Frecce trasformavano alternative, tempi diversi e contesti distinti in fasi obbligatorie. | Tabelle native distinguono esiti del controllo, dichiarazione/liquidazione/versamento, titoli della riscossione, AEO e casi per ente. | Corretto e verificato |
| P03-07 | Schemi 18.2 e 31.5 | Correttezza istituzionale | grave | Profili come quarto ente; EORI confuso con AEO. | Profili come criterio di studio; enti e relazioni corretti; EORI identificazione, AEO status autorizzato. | Corretto e verificato |
| P03-08 | FC03 appendice E, §49.3 | Rinvii errati | medio | Cybersecurity, Consip e authority indicavano altri volumi; capitoli locali ambigui. | Master corretto: VOL-08, VOL-09, VOL-05; ricerca e fisco rinviati al modulo e titolo effettivi. Gate 14/15/16 rieseguiti. | Corretto e verificato |

## 4. Macrostruttura e completezza

Sono presenti tutti i 50 master previsti dal catalogo e tutti i 144 nuclei. Hash correnti confrontati con le sorgenti usate nell’export: zero difformità. La revisione testuale integrale del 2 ottobre e le correzioni testuali registrate il 3 ottobre restano documentate nei rispettivi audit; questo rapporto non dichiara una nuova rilettura integrale parola per parola. Il delta di produzione comprende 70 schemi, un passaggio IVA e cinque destinazioni della tabella EPNE, con confronto inverso e snapshot. I quiz e i casi non sono stati riscritti da questa lavorazione grafica.

## 5. Contenuto, fonti e rinvii

I 70 schemi originali sono stati esaminati e confrontati semanticamente con le nuove tavole. Fonti e limiti sono nella nota `wiki/sources/vol-03-schemi-fiscali-verifica-2026-10-03.md`; per EORI/AEO sono state ricontrollate le pagine ufficiali della Commissione. Le correzioni sostanziali precedenti conservano le loro source notes. Non viene attribuita alla verifica grafica una nuova certificazione di ogni norma. L’allineamento dei 113 riferimenti numerati e delle 126 etichette è registrato con prima/dopo nel manifest della proiezione. I rinvii esterni indicano moduli e titoli reali; quelli interni sono coerenti con l’indice.

## 6. Tipografia e geometria

Formato 6,69×9,61 pollici, 481.92×691.92 pt. Testo principale Garamond circa 11 pt; tabelle circa 9,5 pt; indice minimo 9,5 pt. Font incorporati, inclusi i glifi Type3 con CharProcs. Zero overflow DOM rispetto al piè di pagina, zero testo fuori pagina nella scansione geometrica. Nessuna figura raster residua nel PDF; i PNG originali restano archiviati nel repository. Il rispetto geometrico non equivale a una prova fisica di stampa.

## 7. Secondo controllo e copertura visiva

Visionate tutte le 51 tavole contatto del candidato corrente (813 pagine), più 22 pagine ingrandite, elencate nel registro visuale. Le tavole contatto consentono il controllo di struttura, ritmo, vuoti, salti e densità; non sono una lettura integrale del testo minuto a piena risoluzione. L’indice è stato verificato anche con estrazione diretta del PDF: 194/194 destinazioni corrette. La modalità stampa è stabilizzata e il DOM congelato prima dell’esportazione: conteggi DOM e PDF coincidenti. Sono ammesse continuazioni di tabelle con intestazione ripetuta; non sono state trovate perdite di righe.

## 8. Giudizio finale

**Non pubblicabile allo stato attuale per dipendenze editoriali comuni ancora aperte.** Il candidato interno ha superato le verifiche locali qui descritte. La promessa dei servizi digitali di pagina 1 non è stata verificata; dati editoriali commerciali, copertina, prova fisica e accettazione KDP non sono attestati. Step 21 resta in corso; 22, 23, 24 non chiusi da questo rapporto.

## 9. Produzione e artefatti

La [specifica KDP](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6), verificata nel fascicolo di produzione VOL-02 il 3 ottobre, consente fino a 828 pagine per questo formato con nero e carta bianca. Il candidato di 813 pagine rientra in tale limite; supera invece 776 pagine e non è candidato alla carta crema. Non occorre comprimere il carattere né dividere questo interno. Margini, dorso, copertina e pagine eventualmente aggiunte dal servizio vanno verificati nel successivo passaggio reale di produzione.

Pacchetto: `delivery/VOL-03/candidate-2026-10-03/README.md`. Prova, manifest, registri di geometria e indice, tavole contatto, ingrandimenti mirati, payload congelato e snapshot dei 50 master sono inclusi. Le prove intermedie precedenti sono superate e non vanno consegnate.

## 10. Priorità residue

Confermare l’offerta digitale e i dati editoriali comuni; applicare gli eventuali delta di front matter; rigenerare e ricontrollare il PDF interessato; completare i gate nell’ordine del CLI; preparare copertina e prova fisica. Non sono stati effettuati upload, pubblicazione o signoff finale. Il lavoro locale non chiude automaticamente i rilievi comuni di collana.
