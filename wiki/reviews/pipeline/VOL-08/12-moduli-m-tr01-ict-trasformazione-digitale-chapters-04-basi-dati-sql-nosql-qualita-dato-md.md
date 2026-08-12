# Report editoriale — VOL-08, capitolo 4

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi pubblici.
- Pubblico target: candidati a profili di funzionario ICT, database e Data/AI nella PA.
- Perimetro di questa revisione: capitolo 4, matrice di copertura M-TR01, piano di completamento, rinvio al VOL-01, capitoli di raccordo e fonti consolidate.
- Stato generale in una frase: capitolo autonomo, ben strutturato e didatticamente completo; resta da consolidare la tracciabilità puntuale di tre famiglie NoSQL prima della pubblicazione.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30: coerenza con indice e struttura; progressione; gerarchia; autonomia del capitolo; rapporto con i capitoli adiacenti; terminologia; completezza e accuratezza delle spiegazioni; errori concettuali o fattuali; esempi, query, tabelle e apparato delle fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; layout Markdown; leggibilità e qualità complessiva.

Il punto 27, impaginazione, non è applicabile: non è disponibile un PDF o un file impaginato da ispezionare pagina per pagina.

È stato applicato anche il gate di copertura didattica integrale. I sei nuclei `N-TR01-04-01`–`N-TR01-04-06` sviluppano modello e schema, chiavi e vincoli, normalizzazione, SQL, transazioni, indici, famiglie NoSQL, qualità e sicurezza del dato. Tutti risultano `completo`: nessun concetto è soltanto nominato, parziale, rinviato o mancante. Gli esempi applicano concetti già spiegati. Il rinvio al VOL-01, capitolo 10, § 7, è preciso e limitato ai prerequisiti.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | `N-TR01-04-05` — Famiglie NoSQL | Apparato delle fonti | Media | La source note documenta direttamente il modello documentale, mentre chiave-valore, wide-column e grafo restano classificazioni introduttive non collegate a una fonte neutrale e puntuale per ciascuna famiglia. | Integrare la source note con documentazione primaria o materiale universitario che sostenga definizione, struttura e uso concettuale delle tre famiglie; verificare poi che le formulazioni del nucleo restino coerenti. | Da verificare |
| E02 | `N-TR01-04-01`; checklist finale | Coerenza terminologica | Lieve | Le coppie relazione/tabella, tupla/riga e attributo/colonna sono spiegate correttamente, ma manca ancora una forma principale dichiarata nel glossario finale del volume. | Registrare nel glossario le equivalenze e usare «tabella, riga, colonna» negli esercizi operativi, conservando i termini teorici nella spiegazione del modello. | Proposto |
| E03 | Checklist finale, tabelle e blocchi SQL | Layout | Lieve | Caselle Unicode, codice e tabelle sono leggibili nel Markdown, ma la resa dipende dal font e dalla larghezza utile del formato KDP. | Verificare nel PDF allineamento, ritorni a capo e incorporazione dei glifi; spezzare eventuali tabelle che eccedono la gabbia. | Proposto |

Non sono emersi errori oggettivi gravi, contraddizioni interne, riferimenti normativi da correggere, rinvii generici o nuclei soltanto nominati. Non sono state applicate correzioni dirette al capitolo in questa fase.

## 4. Osservazioni per capitolo

### Capitolo 4 — Basi dati, SQL/NoSQL e qualità del dato

- Punti di forza: uso coerente di un solo caso guida; progressione dai requisiti allo schema e poi alle query; distinzione efficace fra chiave, vincolo e indice; normalizzazione collegata alle anomalie; query spiegate e non soltanto mostrate; confronto SQL/NoSQL prudente; qualità tradotta in dimensioni e controlli; raccordi chiari con cybersecurity e data governance.
- Criticità: la copertura delle famiglie NoSQL è più ampia della granularità attuale delle fonti; glossario e resa KDP restano controlli finali di collana.

## 5. Coerenza globale

- Terminologia: coerente nel capitolo. Le equivalenze teoriche e operative indicate in E02 richiedono soltanto consolidamento nel glossario.
- Struttura vs indice: coerente. L’indice promette modellazione, query, transazioni e controlli; il capitolo sviluppa tali contenuti e aggiunge gli elementi previsti dalla specifica.
- Promesse dell’introduzione mantenute: sì. Ogni competenza dichiarata dispone di spiegazione, esempio o esercizio.
- Confini: rispettati. API e interoperabilità sono rinviate al capitolo 6; rischio, IAM e logging ai capitoli 8-9; governance, metadati e open data al capitolo 10.
- Rinvio al VOL-01: preciso, verificabile e limitato alle nozioni introduttive del capitolo 10, § 7.
- Copertura v4: completa per la riga assegnata al capitolo 4. Non è necessario declassare la matrice; E01 riguarda la granularità della tracciabilità, non una lacuna della spiegazione.

## 6. Contenuto da verificare

- Fonti granulari e neutrali per chiave-valore, wide-column e grafo, come indicato in E01.
- Dialetto SQL, livelli di isolamento e comportamento specifico del DBMS eventualmente nominato dal singolo bando.

Non sono presenti riferimenti normativi nel capitolo; non occorre una verifica normativa.

## 7. Suggerimenti facoltativi (non errori)

- Valutare un piccolo diagramma entità-relazione del caso `Pratica`–`Ufficio`–`Soggetto`.
- Aggiungere nel laboratorio finale una query volutamente errata con join cartesiana da diagnosticare.
- Inserire nel glossario le opposizioni schema/istanza, chiave/vincolo/indice, `WHERE`/`HAVING`, relazionale/documentale.

## 8. Priorità degli interventi

1. Integrare e verificare le fonti NoSQL secondo E01.
2. Consolidare il glossario secondo E02.
3. Controllare il master KDP secondo E03.

## 9. Giudizio di pubblicabilità

Pubblicabile dopo intervento medio.

Motivazione: il capitolo supera il test dello studente, è strutturalmente completo e non presenta errori gravi aperti. E01 è circoscritto, ma riguarda la tracciabilità specialistica di un nucleo centrale e va chiuso prima della pubblicazione; E02 ed E03 sono rifiniture di collana.

## 10. Limiti di questa revisione

La revisione riguarda il Markdown, la matrice, il piano e le note wiki collegate. Non è stato ispezionato un PDF impaginato. Le fonti consolidate sono state valutate per pertinenza e coerenza editoriale; in questa fase non sono state eseguite le query su tutti i DBMS potenzialmente indicati dai bandi. La conformità a un dialetto o prodotto specifico resta verificabile soltanto rispetto al singolo bando.
