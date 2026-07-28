# VOL-08 ICT, digitale, cybersecurity e dati — Specifica editoriale

## Obiettivo

Portare `VOL-08` dallo stato di scaffold a volume specialistico source-ready, usando il dossier esterno `Modulo M-TR01 – ICT, digitale, cybe.txt` come riferimento di pianificazione consolidato e applicando il protocollo editoriale governato dal CLI di pipeline.

## Decisioni approvate

- Codice volume: `VOL-08`.
- Titolo: `ICT, digitale, cybersecurity e dati`.
- Data di chiusura delle fonti: `2026-07-28`.
- Responsabile normativo: `Alberto Brando`.
- Responsabile editoriale: `Alberto Brando`.
- Provider di scrittura: `codex`.
- Il volume è monomodulo e contiene `M-TR01`.
- Target indicativo: 32.000–34.000 parole e 90–115 pagine equivalenti.
- Il volume sviluppa il delta specialistico ICT e non duplica il nucleo comune di `VOL-01`.

## Confine editoriale

Restano nel volume base e sono richiamati mediante destinazioni precise:

- contratti pubblici essenziali;
- privacy, CAD, trasparenza digitale, PEC, firma e identità digitale di base;
- informatica generale, Office e sicurezza elementare;
- inglese, logica, situazionali e casi amministrativi di base.

`VOL-08` insegna invece programmazione, algoritmi, basi dati, reti, sistemi, ingegneria del software, API, interoperabilità, cloud, DevOps, cybersecurity specialistica, IAM, crittografia, logging, incident response, data governance, AI/ML e procurement ICT applicativo.

I contenuti avanzati appartenenti ad altre famiglie sono rinviati a `VOL-09`, `VOL-10`, `VOL-11` o `VOL-12`, senza duplicazioni.

## Flusso della conoscenza

1. Copiare il dossier in `wiki/raw/` come evidenza immutabile.
2. Creare una source note in `wiki/sources/` con limiti, attendibilità e riferimenti.
3. Creare o aggiornare topic ed entity page pertinenti.
4. Collegare fonte, topic, modulo e volume.
5. Aggiornare `wiki/index.md` e appendere un evento a `wiki/log.md`.
6. Generare l’outline e la matrice solo dalla conoscenza consolidata.
7. Usare le fonti raw esclusivamente per audit, mai come fonte diretta del testo finale.

Le fonti normative e i bandi indicati nel dossier come `[DA VERIFICARE]` rimangono tali finché non vengono acquisiti da fonti ufficiali e consolidati nel wiki.

## Architettura del volume

### Front matter

Il volume adotta il front matter canonico dei volumi specialistici:

1. servizi digitali;
2. frontespizio;
3. copyright e note;
4. sommario;
5. premessa;
6. indice.

L’indice usa `front_matter_layout: analytical-index` e `index_detail: chapters-only`. La numerazione vive in `outline_section`; titoli e H1 non contengono numeri.

### Modulo M-TR01

Il solo modulo del volume è articolato in cinque parti.

#### Parte I — Profilo e fondamenta specialistiche

1. Lavorare come ICT nella PA: ruoli, enti e prove.
2. Informatica specialistica: cosa serve oltre il VOL-01.

#### Parte II — Sviluppo, dati e infrastrutture

3. Programmazione, algoritmi e strutture dati.
4. Basi dati, SQL/NoSQL e qualità del dato.
5. Reti, sistemi operativi e infrastrutture.
6. Ingegneria software, API e interoperabilità della PA.
7. Cloud PA, virtualizzazione, container e DevOps.

#### Parte III — Cybersecurity e resilienza

8. Cybersecurity operativa: rischio, controlli e vulnerabilità.
9. IAM, crittografia, logging e incident response.

#### Parte IV — Dati, intelligenza artificiale e fornitori

10. Data governance, open data, interoperabilità e qualità.
11. AI/ML nella PA: modelli, rischi e compliance.
12. Procurement ICT e gestione dei fornitori.

#### Parte V — Allenamento

13. Laboratorio prove ICT: quiz, scritto tecnico, orale e casi.

### Appendici

- A. Glossario ICT, cyber e dati per concorsi PA.
- B. ISO 27001, NIST CSF, ITIL e COBIT in chiave concorsuale.
- C. NIS2 e incident response.
- D. Cloud PA e DevOps: checklist operativa.
- E. Data e AI compliance.
- F. Piano 30/60/90 giorni per profili ICT.

## Matrice di copertura

La matrice registra, per ciascun nucleo:

- materia e concetti;
- profili destinatari;
- fonti consolidate;
- capitolo o appendice;
- copertura teorica;
- applicazione e output;
- verifica dell’apprendimento;
- stato (`completo`, `parziale`, `solo-nominato`, `rinviato`, `mancante`);
- necessità di review normativa.

`solo-nominato`, `mancante` e `parziale` bloccano la pubblicazione. `rinviato` è valido solo con una destinazione precisa, completa e verificata.

## Pipeline

La scheda del volume dichiara le fasi `A`–`G`, così l’intero protocollo dei 25 prompt resta governato dal CLI. Il ciclo operativo è:

1. `doctor --json`;
2. `init VOL-08 --json`;
3. `status VOL-08 --json`;
4. `next VOL-08 --json`;
5. esecuzione esatta del prompt materializzato;
6. `complete ... --json`;
7. correzione e ripetizione quando il gate blocca.

I gate non automatizzati vengono chiusi con `--accept --note` soltanto dopo una verifica manuale effettivamente svolta. Nessuno step a valle viene anticipato e `pipeline/VOL-08/run-state.json` non viene modificato manualmente.

## Verifiche e gestione degli errori

- Il CLI deve riconoscere scheda, modulo, capitoli e matrici.
- Ogni file editoriale deve avere frontmatter valido e link coerenti.
- I riferimenti non verificati devono restare esplicitamente marcati.
- L’ingest deve essere tracciato in `wiki/log.md` e nella memoria locale.
- L’indice deve coincidere con i file capitolo e con l’ordine dichiarato nella scheda.
- I gate automatici devono essere letti dal JSON, non dal testo formattato.
- Un errore di famiglia, una duplicazione del nucleo B-PA o una lacuna su materie ricorrenti blocca la lavorazione.

## Criterio di completamento

Il lavoro è completo quando:

- il dossier è acquisito e consolidato nel wiki;
- VOL-08 e M-TR01 hanno struttura, indice, front matter, matrice e scheda pipeline coerenti;
- il CLI ha inizializzato il run-state;
- tutti gli step eseguibili con le fonti disponibili sono stati lavorati e chiusi tramite gate;
- ogni blocco residuo è documentato con la precisa verifica umana o fonte ufficiale mancante;
- la memoria locale contiene una traccia sintetica del flusso.
