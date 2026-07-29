# Report editoriale — VOL-08, capitolo 4

## 1. Sintesi editoriale

- Genere editoriale: manuale-workbook specialistico per concorsi pubblici.
- Pubblico target: candidati a profili di funzionario ICT, database e Data/AI nella PA.
- Perimetro di questa revisione: capitolo 4, matrice di copertura M-TR01, piano di completamento, rinvio al VOL-01, capitoli di raccordo e fonti consolidate.
- Stato generale in una frase: capitolo autonomo, ben strutturato e didatticamente completo, da sottoporre a validazione tecnica circoscritta prima della pubblicazione.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30: coerenza con indice e struttura; progressione; gerarchia; autonomia del capitolo; rapporto con i capitoli adiacenti; terminologia; completezza e accuratezza delle spiegazioni; errori concettuali o fattuali; esempi, query, tabelle e apparato delle fonti; sintassi; chiarezza; tono; stile didattico; ripetizioni; contraddizioni; grammatica; ortografia; punteggiatura; refusi; uniformità grafica; layout Markdown; leggibilità e qualità complessiva.

Il punto 27, impaginazione, non è applicabile: non è disponibile un PDF o un file impaginato da ispezionare pagina per pagina.

È stato applicato anche il gate di copertura didattica integrale. Il nucleo «Basi dati» sviluppa modello e schema, chiavi e vincoli, normalizzazione, SQL, transazioni, indici, famiglie NoSQL, qualità e sicurezza del dato. Gli esempi applicano concetti già spiegati. Il rinvio al VOL-01, capitolo 10, § 7, è preciso e limitato ai prerequisiti.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Normalizzazione e anomalie | Accuratezza contenutistica | Media | Le definizioni operative di 2NF e 3NF sono adatte al livello concorsuale, ma omettono parte del formalismo sulle dipendenze funzionali e sui prerequisiti delle forme normali. | Far validare la formulazione da un docente di basi dati; se il campione dei bandi richiede formalismo, aggiungere dipendenza funzionale, determinante e prerequisito della forma precedente con un esempio controllato. | Da verificare |
| E02 | NoSQL: famiglie e criteri di scelta | Apparato delle fonti | Media | La source note documenta direttamente il modello documentale, mentre chiave-valore, wide-column e grafo sono classificazioni introduttive non ancora collegate a una fonte primaria neutrale e puntuale. | Integrare la source note con documentazione primaria o materiale universitario per ciascuna famiglia; mantenere la review specialistica aperta. | Da verificare |
| E03 | Transazioni e concorrenza | Accuratezza contenutistica | Media | ACID e isolamento sono esposti correttamente a livello concettuale, ma i comportamenti concreti dipendono dal DBMS e dal livello di isolamento; il capitolo non esemplifica un’anomalia concorrente. | Verificare il blocco sul DBMS richiesto dal bando e valutare un esempio breve di lettura o aggiornamento concorrente, senza trasformare la sezione in documentazione di prodotto. | Proposto |
| E04 | SQL per interrogare e modificare | Portabilità degli esempi | Media | Le query usano un sottoinsieme semplice, ma portabilità di identificatori, `LIKE`, gestione di `NULL` e comportamento delle funzioni aggregate deve essere verificata sul dialetto eventualmente nominato dal bando. | Eseguire le query su almeno un DBMS di riferimento e aggiungere note di dialetto solo quando un bando richiede un prodotto specifico. | Da verificare |
| E05 | Terminologia tecnica | Coerenza terminologica | Lieve | Il capitolo usa coppie equivalenti come relazione/tabella, tupla/riga e attributo/colonna; sono spiegate correttamente, ma devono confluire nel glossario finale con una forma principale. | Registrare nel glossario le equivalenze e usare «tabella, riga, colonna» negli esercizi operativi, conservando i termini teorici nella spiegazione del modello. | Proposto |
| E06 | Checklist finale e blocchi SQL | Layout | Lieve | Caselle Unicode, righe di codice e tabelle sono leggibili nel Markdown, ma la resa dipende dal font e dalla larghezza utile del formato KDP. | Verificare nel PDF allineamento, ritorni a capo e incorporazione dei glifi; spezzare eventuali tabelle che eccedono la gabbia. | Proposto |

Non sono emersi errori oggettivi gravi, contraddizioni interne, riferimenti normativi da correggere, rinvii generici o nuclei soltanto nominati. Non sono state applicate correzioni dirette al capitolo in questa fase.

## 4. Osservazioni per capitolo

### Capitolo 4 — Basi dati, SQL/NoSQL e qualità del dato

- Punti di forza: uso coerente di un solo caso guida; progressione dai requisiti allo schema e poi alle query; distinzione efficace fra chiave, vincolo e indice; normalizzazione collegata alle anomalie; query spiegate e non soltanto mostrate; confronto SQL/NoSQL prudente; qualità tradotta in dimensioni e controlli; raccordi chiari con cybersecurity e data governance.
- Criticità: alcune semplificazioni richiedono sign-off specialistico; la copertura delle famiglie NoSQL è più ampia della granularità attuale delle fonti; la portabilità degli esempi SQL va controllata rispetto ai prodotti effettivamente richiesti.

## 5. Coerenza globale

- Terminologia: coerente nel capitolo. Le equivalenze teoriche e operative indicate in E05 richiedono soltanto consolidamento nel glossario.
- Struttura vs indice: coerente. L’indice promette modellazione, query, transazioni e controlli; il capitolo sviluppa tali contenuti e aggiunge gli elementi previsti dalla specifica.
- Promesse dell’introduzione mantenute: sì. Ogni competenza dichiarata dispone di spiegazione, esempio o esercizio.
- Confini: rispettati. API e interoperabilità sono rinviate al capitolo 6; rischio, IAM e logging ai capitoli 8-9; governance, metadati e open data al capitolo 10.
- Rinvio al VOL-01: preciso, verificabile e limitato alle nozioni introduttive del capitolo 10, § 7.
- Copertura v4: completa per la riga assegnata al capitolo 4. Non è necessario declassare la matrice.

## 6. Contenuto da verificare

- Formalizzazione di 2NF e 3NF rispetto alla profondità richiesta dai bandi.
- Fonti granulari e neutrali per chiave-valore, wide-column e grafo.
- Comportamento concreto di transazioni e isolamento sul DBMS eventualmente richiesto.
- Portabilità delle query e dei comportamenti relativi a identificatori, `NULL`, `LIKE` e aggregazioni.
- Adeguatezza delle dimensioni di qualità rispetto al raccordo con il capitolo 10.

Non sono presenti riferimenti normativi nel capitolo; non occorre una verifica normativa.

## 7. Suggerimenti facoltativi (non errori)

- Valutare un piccolo diagramma entità-relazione del caso `Pratica`–`Ufficio`–`Soggetto`.
- Aggiungere nel laboratorio finale una query volutamente errata con join cartesiana da diagnosticare.
- Inserire nel glossario le opposizioni schema/istanza, chiave/vincolo/indice, `WHERE`/`HAVING`, relazionale/documentale.

## 8. Priorità degli interventi

1. Eseguire la review specialistica indicata in E01 ed E03.
2. Integrare le fonti NoSQL secondo E02.
3. Verificare gli esempi SQL sui dialetti rilevanti come indicato in E04.
4. Consolidare il glossario secondo E05.
5. Controllare il master KDP secondo E06.

## 9. Giudizio di pubblicabilità

Pubblicabile dopo intervento medio.

Motivazione: il capitolo è strutturalmente completo e non presenta errori gravi aperti. Le verifiche E01-E04 sono circoscritte, ma riguardano accuratezza specialistica, tracciabilità e portabilità di contenuti centrali; vanno chiuse prima della pubblicazione.

## 10. Limiti di questa revisione

La revisione riguarda il Markdown, la matrice, il piano e le note wiki collegate. Non è stato ispezionato un PDF impaginato. Le fonti ufficiali consolidate sono state valutate per pertinenza, ma non è stata eseguita una revisione umana firmata da un DBA, un docente di basi dati, uno specialista NoSQL o un data quality specialist. Non sono state eseguite le query su tutti i DBMS potenzialmente indicati dai bandi.
