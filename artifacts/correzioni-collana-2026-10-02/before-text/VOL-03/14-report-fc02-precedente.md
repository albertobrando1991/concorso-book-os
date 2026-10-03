# Report editoriale — Correzioni M-FC02 Agenzie fiscali

## 1. Sintesi editoriale
- Genere editoriale: manuale-workbook specialistico per concorsi nelle Agenzie fiscali.
- Pubblico target: candidati AE, ADM, AdER, Territorio/SPI e profili amministrativo-contabili collegati.
- Perimetro di questa revisione: applicazione delle correzioni obbligatorie M01-M07 del report trasversale dello step 13.
- Stato generale in una frase: tutte le correzioni obbligatorie sono state applicate; review specialistiche e preflight KDP restano correttamente aperti.

## 2. Punti applicati della checklist
Applicati i controlli pertinenti: struttura e indice; coerenza tra capitoli; gerarchia dei titoli; metadati; ortografia; apparato iconografico; asset dichiarati e incorporati; link e anchor; copertura didattica; frontmatter; leggibilità markdown; integrità tecnica. Il controllo sul PDF non è applicabile in questo step. Non sono state rieseguite review normative esterne.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| G01 | Cap. 9 e matrice | Copertura didattica | Grave | Promessa sul monopolio fiscale già corretta nello step 13. | Verificare permanenza della spiegazione e della riga di matrice. | Corretto |
| M01 | index.md | Coerenza globale | Media | Stato e prossimo passo obsoleti. | Allineare indice ai totali della matrice. | Corretto |
| M02 | Capp. 1-14, 5A e 5B | Ortografia | Media | Alternanza tra accenti e grafie ASCII. | Normalizzare il corpo preservando metadati e percorsi. | Corretto |
| M03 | Capp. 5-7 | Apparato visivo | Media | Quindici asset dichiarati ma non incorporati. | Inserire figure e didascalie nelle sezioni pertinenti. | Corretto |
| M04 | Cap. 3 | Coerenza testo-apparato | Media | Figure collocate sotto sezioni non corrispondenti. | Ricollocare le figure 3.2-3.4. | Corretto |
| M05 | Cap. 8 | Gerarchia visiva | Media | Ordine figure non progressivo. | Ripristinare l'ordine 8.1-8.5. | Corretto |
| M06 | Cap. 4 e matrice | Gerarchia titoli | Media | Livello 3 senza livelli 1 e 2. | Rinominare il titolo e aggiornare il riferimento. | Corretto |
| M07 | Capp. 1-3 | Metadati | Media | Campo companion_to mancante. | Aggiungere il campo canonico. | Corretto |
| L01 | Cap. 14 | Layout | Lieve | Figure 14.4-14.5 consecutive. | Valutare durante il preflight KDP. | Aperto per preflight |

### Registro delle correzioni applicate
| ID | File modificato | Correzione | Fonte/evidenza | Stato finale |
| --- | --- | --- | --- | --- |
| G01 | Nessuna modifica nello step 14 | Verificata la correzione già registrata nello step 13 e la riga coerente nella matrice. | Report step 13 e matrice. | Corretto |
| M01 | index.md | Rimossi il riferimento ai 18 blocker e il prossimo passo obsoleto; dichiarati 80 nuclei completi, review e preflight aperti. | Totali della matrice: 80 completo, zero blocker. | Corretto |
| M02 | 16 file in chapters/ | Normalizzate 1.717 grafie ASCII nel solo corpo editoriale, preservando frontmatter, slug e percorsi. | Ricerca PCRE2 senza residui nel corpo; diff-check e test. | Corretto |
| M03 | Capitoli 5, 6 e 7 | Incorporati nel corpo i 15 asset già dichiarati, con didascalie e collocazione pertinente. | Cinque figure ordinate per capitolo; PNG esistenti. | Corretto |
| M04 | Capitolo 3 | Ricollocate le figure 3.2, 3.3 e 3.4 nelle sezioni su MEF, tre funzioni e rete territoriale. | Ordine 3.1-3.5 e corrispondenza didascalia-sezione. | Corretto |
| M05 | Capitolo 8 | Spostata la figura 8.5 dopo la 8.4, ripristinando l'ordine numerico. | Ricerca delle didascalie nel file. | Corretto |
| M06 | Capitolo 4 e matrice | Rinominato il titolo in Quadro UE fiscale, IVA e dogane e aggiornato il riferimento nella matrice. | Nessun residuo di Livello 3 - Quadro UE. | Corretto |
| M07 | Capitoli 1, 2 e 3 | Aggiunto companion_to: il-metodo-bando senza modificare gli altri metadati. | Controllo frontmatter e test. | Corretto |
| L01 | Capitolo 14 | Nessuna modifica: osservazione lieve rinviata al preflight. | Non applicare come obbligatori i suggerimenti facoltativi. | Aperto per preflight |

## 4. Osservazioni per capitolo
### Capitoli 1-3
- Punti di forza: metadati coerenti; figure del capitolo 3 collocate accanto ai concetti descritti.
- Criticità: review organizzativa ufficiale ancora richiesta.

### Capitolo 4
- Punti di forza: gerarchia UE coerente e matrice riallineata.
- Criticità: vigenza tributaria e fonti UE restano da review umana.

### Capitoli 5-7
- Punti di forza: i quindici asset dichiarati sono ora visibili nel percorso didattico.
- Criticità: resa in pagina da verificare nel preflight KDP.

### Capitolo 8
- Punti di forza: sequenza delle figure ripristinata.
- Criticità: CDU, TARIC e sistemi telematici restano soggetti a verifica specialistica.

### Capitoli 9-14
- Punti di forza: ortografia uniformata senza modifiche sostanziali alla copertura.
- Criticità: restano le review specialistiche; L01 resta al preflight.

## 5. Coerenza globale
- Terminologia: normalizzata nel corpo editoriale senza alterare i percorsi tecnici.
- Struttura vs indice: coerente con 14 capitoli numerati, due intercalari e 80 nuclei completi.
- Promesse dell'introduzione mantenute: sì sul piano didattico; pubblicabilità subordinata a review e preflight.

## 6. Contenuto da verificare
- Vigenza di norme, procedure, soglie, termini, modelli e sistemi indicati nella matrice.
- Review tributarie, doganali, catastali, contabili, civilistiche, penal-tributarie, processuali, organizzative e privacy.
- Resa KDP delle 70 figure incorporate, delle tabelle, dei canvas e delle figure 14.4-14.5.

## 7. Suggerimenti facoltativi (non errori)
- Valutare nel text freeze l'uniformità tipografica dei box ricorrenti.
- Valutare una tabella iniziale profilo-capitoli solo come scelta autoriale.
- Decidere nel preflight se separare le figure 14.4 e 14.5.

## 8. Priorità degli interventi
1. Eseguire la review umana specialistica prevista dallo step 15.
2. Congelare il testo soltanto dopo la chiusura delle review richieste.
3. Eseguire il preflight KDP e risolvere L01 sulla base della resa reale.

## 9. Giudizio di pubblicabilità
Pubblicabile dopo intervento medio.

Motivazione: M01-M07 sono chiusi e la copertura didattica resta completa. Le verifiche normative specialistiche e il preflight KDP non sono stati anticipati né dichiarati conclusi.

## 10. Limiti di questa revisione
La revisione ha verificato markdown, frontmatter, matrice, ordine e presenza delle figure, residui ortografici selezionati, integrità del diff e test automatici. Non ha esaminato un PDF impaginato e non ha aggiornato la vigenza normativa tramite fonti esterne.
