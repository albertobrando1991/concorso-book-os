# VOL-07 — Disegno del completamento editoriale

Data: 2026-07-31
Stato: approvato in conversazione, da sottoporre a verifica sul file
Volume: `VOL-07`
Moduli: `M-SA01`, `M-SA02`, `M-SA03`, `M-SA04`

## 1. Decisione

VOL-07 viene esteso dal run configurato iniziale a un volume didattico completo di 25 capitoli. Il volume deve preparare candidati ai concorsi pubblici sanitari senza presupporre l'accesso alle note interne del progetto.

Il perimetro scelto è:

- quadro comune completo per ciascuna famiglia concorsuale;
- verticali professionali autonomi e tracciabili;
- contenuti clinici e tecnici applicati in forma didattica e non esecutiva;
- revisione umana specialistica mantenuta come ultimo gate reale prima del congelamento;
- nessuna accettazione artificiale dei gate non automatizzati.

## 2. Obiettivi

1. Trasformare tutti i nuclei `completo` delle matrici M-SA02, M-SA03 e M-SA04 in capitoli effettivi.
2. Conservare e integrare i capitoli M-SA01 e M-SA02 già completati.
3. Applicare a ogni nuovo capitolo il contratto didattico orientato allo studente.
4. Rendere indice, dashboard e anteprima coerenti con i 25 capitoli.
5. Eseguire la pipeline canonica fino alla predisposizione dello step 15.
6. Consegnare pacchetti di review umana puntuali e utilizzabili dallo staff.

## 3. Non obiettivi

- Non produrre protocolli clinici o tecnici universalmente esecutivi.
- Non sostituire procedure aziendali, manuali del dispositivo o protocolli del setting.
- Non inventare firme, esiti o nulla osta specialistici.
- Non congelare il testo e non chiudere gli step 16-23 prima del completamento dello step 15.
- Non rinumerare o riscrivere la storia degli step già completati nel `run-state`.
- Non pubblicare, distribuire o eseguire push senza una richiesta esplicita.

## 4. Architettura editoriale

La struttura bilanciata comprende 25 capitoli. Gli ID tecnici già versionati restano stabili; l'indice rivolto al lettore applica un ordinamento editoriale continuo da 1 a 25.

### 4.1 M-SA01 — Sanità amministrativa

| Ordine volume | ID tecnico | Titolo |
| ---: | ---: | --- |
| 1 | 04 | Atti, procedimenti e flussi informativi nelle aziende sanitarie |
| 2 | 05 | Documentazione sanitaria, accesso, privacy e conservazione |
| 3 | 06 | Front office e comunicazione con l'utenza |
| 4 | 09 | Contabilità, budget e controllo di gestione |
| 5 | 10 | Procurement, farmaci, dispositivi e magazzino |

Questi cinque capitoli hanno già completato gli step 08-12. Non vanno rinumerati nel filesystem o nel run-state.

### 4.2 M-SA02 — Professioni sanitarie

| Ordine volume | ID tecnico | Target |
| ---: | ---: | --- |
| 6 | 01 | `chapters/01-mappa-profili-e-prove.md` |
| 7 | 03 | `chapters/03-discipline-professionali-autonomia-responsabilita.md` |
| 8 | 04 | `chapters/04-assistenza-infermieristica-tecniche-assistenziali-oss.md` |
| 9 | 05 | `chapters/05-valutazione-clinica-triage-urgenza-emergenza.md` |
| 10 | 06 | `chapters/06-prevenzione-continuita-presa-in-carico.md` |
| 11 | 07 | `chapters/07-evidenze-pico-grade-applicabilita.md` |
| 12 | 08 | `chapters/08-igiene-pubblica-epidemiologia-screening.md` |
| 13 | 09 | `chapters/09-controlli-tpall-verbalizzazione-campionamento-sanzioni.md` |
| 14 | 10 | `chapters/10-prova-pratica-casi-professionali.md` |

Titoli editoriali dei nuovi capitoli:

- 04 — Assistenza infermieristica, tecniche assistenziali e supporto OSS;
- 05 — Valutazione clinica, triage, urgenza ed emergenza;
- 06 — Prevenzione, continuità assistenziale e presa in carico;
- 07 — Evidenze scientifiche, PICO, GRADE e applicabilità;
- 08 — Igiene pubblica, epidemiologia, sorveglianza e screening;
- 09 — Controlli TPALL, verbalizzazione, campionamento e sanzioni;
- 10 — Prova pratica e casi professionali.

Il salto tecnico tra `01` e `03` viene conservato perché `03` è già scritto, revisionato e registrato nel run-state. La continuità per il lettore è ottenuta tramite l'ordine editoriale, non alterando gli identificativi storici.

### 4.3 M-SA03 — Dirigenza medica e sanitaria

| Ordine volume | ID tecnico | Target |
| ---: | ---: | --- |
| 15 | 01 | `chapters/01-profili-requisiti-prove-dirigenza-sanitaria.md` |
| 16 | 02 | `chapters/02-programmazione-sanitaria-organizzazione-servizi.md` |
| 17 | 03 | `chapters/03-linee-guida-appropriatezza-decisioni-cliniche.md` |
| 18 | 04 | `chapters/04-governo-clinico-hta-qualita-accreditamento-rischio.md` |
| 19 | 05 | `chapters/05-epidemiologia-sanita-pubblica-dirigenza.md` |
| 20 | 06 | `chapters/06-dirigenza-medica-discipline-casi.md` |
| 21 | 07 | `chapters/07-dirigenza-sanitaria-non-medica-discipline-casi.md` |

I capitoli 06 e 07 sono verticali distinti. Il primo insegna come affrontare la disciplina e i casi della dirigenza medica senza fingere di sostituire i manuali delle singole specializzazioni. Il secondo tratta i profili della dirigenza sanitaria non medica secondo requisiti, fonti e responsabilità propri.

### 4.4 M-SA04 — Tecnici sanitari e prevenzione

| Ordine volume | ID tecnico | Target |
| ---: | ---: | --- |
| 22 | 01 | `chapters/01-profili-tslb-tsrm-requisiti-prove-responsabilita.md` |
| 23 | 02 | `chapters/02-tslb-processo-laboratorio-qualita-biosicurezza.md` |
| 24 | 03 | `chapters/03-tsrm-imaging-dosimetria-radioprotezione.md` |
| 25 | 04 | `chapters/04-tecnologie-dispositivi-apparecchiature-rischio.md` |

TSLB e TSRM restano verticali autonomi. Il capitolo 04 tratta soltanto il quadro trasversale di tecnologie, dispositivi, apparecchiature, qualità e rischio tecnologico.

## 5. Contratto didattico del capitolo

Ogni capitolo deve poter essere studiato senza consultare il wiki interno. La struttura minima comprende:

1. obiettivi di apprendimento e perimetro concorsuale;
2. spiegazione progressiva dei concetti;
3. collegamento fra norma, principio e applicazione;
4. esempi e casi ragionati;
5. output richiesti nelle prove scritte, pratiche o orali;
6. errori frequenti e distinzioni da ricordare;
7. sintesi operativa;
8. domande, quiz o esercizi con criteri di autoverifica;
9. fonti ufficiali realmente utili al lettore;
10. dati mobili, limiti e data di cut-off chiaramente segnalati.

Sono vietati nel testo rivolto allo studente:

- rinvii a “fonti consolidate”, “source note”, “matrice”, “pacchetto” o altri artefatti interni;
- affermazioni che presuppongono accesso alle note di lavorazione;
- istruzioni cliniche o tecniche esecutive prive di validazione;
- estensioni universali ricavate da procedure locali o da un singolo dispositivo;
- citazioni ornamentali che non aiutano comprensione o verifica.

Le note interne restano strumenti di provenienza per lo staff. Nel capitolo si citano direttamente la fonte ufficiale, l'atto, la linea guida o il documento pubblico pertinente.

## 6. Pipeline

La scheda canonica di VOL-07 deve dichiarare:

- fasi del volume `A-F`;
- tutti e quattro i moduli nelle fasi pertinenti;
- i 25 target della fase C;
- fasi D per la review di modulo;
- fasi E-F a livello di volume, presenti ma bloccate finché lo step 15 non passa.

La migrazione si esegue esclusivamente con:

```text
npm run pipeline -- sync VOL-07 --json
```

La sincronizzazione deve preservare gli step già completati e aggiungere soltanto i nuovi target. `pipeline/VOL-07/run-state.json` non viene modificato a mano.

Per ciascun capitolo nuovo si eseguono in ordine:

1. step 08 — piano del capitolo;
2. step 09 — scrittura;
3. step 10 — controllo di copertura;
4. step 11 — Humanizer;
5. step 12 — revisione editoriale totale.

Dopo la fase C:

1. step 13 — review complessiva di ciascun modulo;
2. step 14 — correzioni obbligatorie;
3. step 15 — preparazione e compilazione del pacchetto di review specialistica.

L'agente prepara lo step 15, ma non compila gli esiti riservati al revisore. Il run deve arrestarsi onestamente al primo gate umano non soddisfatto.

## 7. Pacchetti di review umana

Per ogni modulo il pacchetto deve elencare:

| Campo | Contenuto |
| --- | --- |
| posizione | file e sezione verificabile |
| affermazione | claim normativo, tecnico o clinico |
| fonte | fonte ufficiale consolidata |
| domanda | quesito preciso al revisore |
| rischio | alto, medio o basso |
| esito | campo vuoto riservato al revisore |
| correzione | campo vuoto o proposta chiaramente distinta |

Le review già previste per M-SA02 (`REV-OSS`, `REV-OST`, `REV-FIS`, `REV-EPI`, `REV-TPA`) vengono conservate e coordinate con i capitoli nuovi. M-SA03 e M-SA04 ricevono pacchetti separati per i rispettivi verticali.

## 8. Indice e dashboard

La dashboard deve:

- mostrare tutti i 25 capitoli nell'ordine editoriale;
- distinguere l'ordine rivolto allo studente dagli ID tecnici;
- usare titoli con accenti e punteggiatura corretti;
- caricare il corpo del capitolo selezionato, non un'anteprima riutilizzata;
- aggiornarsi dalla sorgente canonica senza richiedere copie manuali divergenti;
- indicare lo stato “in attesa di revisione umana specialistica” quando lo step 15 è aperto;
- non presentare il volume come congelato, pronto per KDP o consegnabile.

## 9. Verifiche

L'implementazione deve essere guidata da test che provino almeno:

1. manifest dei 25 capitoli nella scheda pipeline;
2. conservazione degli step già completati dopo `sync`;
3. generazione degli step 08-12 per tutti i target nuovi;
4. generazione degli step 13-15 per tutti i moduli;
5. blocco degli step 16-23 in assenza del nulla osta umano;
6. presenza dei capitoli negli indici;
7. ordine editoriale continuo nella dashboard;
8. anteprima distinta per capitolo;
9. assenza di placeholder e riferimenti interni vietati;
10. controllo di accenti, titoli e link;
11. typecheck;
12. suite completa del repository.

La verifica finale comprende inoltre `pipeline doctor`, `pipeline status VOL-07 --json`, `git diff --check` e un controllo visivo della dashboard.

## 10. Gestione degli errori

- Una fonte insufficiente blocca il capitolo interessato e viene registrata come blocker; non viene colmata per inferenza.
- Un gate non implementato viene verificato manualmente soltanto quando esistono evidenze reali.
- Lo step 15 privo di firma resta aperto.
- Un errore di anteprima viene riprodotto con un test prima della correzione.
- Modifiche sostanziali a capitoli già revisionati riaprono i relativi controlli 10-15.
- File sporchi non pertinenti nel worktree non vengono inclusi nei commit.

## 11. Strategia di commit e consegna

I commit restano piccoli e tematici:

1. specifica e test;
2. configurazione e sincronizzazione;
3. un ciclo editoriale per capitolo o gruppo strettamente correlato;
4. review di modulo;
5. pacchetti step 15;
6. dashboard e verifiche finali.

La consegna è locale. Push, PR, pubblicazione e distribuzione restano fuori perimetro finché non richiesti.

## 12. Criterio di completamento di questa fase

Il lavoro automatico è completato quando:

- tutti i 25 capitoli esistono e i nuovi hanno superato gli step 08-12;
- gli step 13-14 sono chiusi con evidenze;
- tutti i pacchetti dello step 15 sono pronti;
- CLI e dashboard mostrano correttamente il gate umano aperto;
- test, typecheck e controlli di integrità sono verdi;
- nessuno step 16-23 è stato dichiarato completato.

Il volume diventa congelabile e può proseguire verso impaginazione e consegna soltanto dopo l'integrazione dei nulla osta umani.
