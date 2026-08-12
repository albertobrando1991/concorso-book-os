---
id: source-basi-dati-sql-nosql-qualita-fonti-tecniche
type: source
title: "Basi dati, SQL, NoSQL e qualità — fonti tecniche primarie"
status: processed
domain: "informatica specialistica"
topics: ["basi dati", "sql", "nosql", "qualità dati"]
entities: ["PostgreSQL", "MongoDB", "MIT OpenCourseWare", "Commissione europea"]
source_refs: []
book_refs: ["m-tr01-ict-trasformazione-digitale"]
confidence: 0.9
updated_at: 2026-07-29
created_at: 2026-07-29
review_required: true
canonical: true
tags: ["source", "vol-08", "database", "sql", "nosql", "qualita-dati"]
source_type: official_documentation_and_university_materials
source_url: "https://www.postgresql.org/docs/current/tutorial.html"
source_date: 2026-07-29
authority_level: alta
---

# Basi dati, SQL, NoSQL e qualità — fonti tecniche primarie

## Uso

Nota consolidata per il capitolo 4 di VOL-08. Sostiene modello relazionale, vincoli, SQL, transazioni, indici, privilegi, modellazione documentale e qualità del dato. Gli esempi del capitolo adottano SQL semplice e dichiarano lo schema; i comportamenti specifici di prodotto non sono presentati come universali.

## Fonti ufficiali e universitarie

- **PostgreSQL Tutorial**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/tutorial.html>. Introduce concetti relazionali, creazione e interrogazione di tabelle, join, aggregazioni, aggiornamenti, eliminazioni, chiavi esterne e transazioni.
- **Data Definition**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/ddl.html>. Documenta tabelle, valori predefiniti, vincoli `CHECK`, `NOT NULL`, `UNIQUE`, chiavi primarie, chiavi esterne, privilegi e sicurezza delle righe.
- **Indexes**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/indexes.html>. Spiega che gli indici possono accelerare il reperimento di righe, ma introducono costi aggiuntivi e vanno usati con criterio.
- **Transaction Isolation**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/transaction-iso.html>. Descrive i livelli di isolamento e gli effetti della concorrenza sulle viste dei dati.
- **Transactions and Identifiers**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/transaction-id.html>. Conferma l’apertura esplicita delle transazioni e la chiusura con `COMMIT` o `ROLLBACK`.
- **Privileges**, PostgreSQL Global Development Group, documentazione corrente consultata il 29 luglio 2026: <https://www.postgresql.org/docs/current/ddl-priv.html>. Documenta proprietà degli oggetti, ruoli e privilegi quali `SELECT`, `INSERT`, `UPDATE` e `DELETE`.
- **Relational Database Design: Database Design Principles**, MIT OpenCourseWare, consultato il 29 luglio 2026: <https://ocw.mit.edu/courses/11-208-introduction-to-computers-in-public-management-ii-january-iap-2002/f61e098641cd8231afd226e8658026a3_lect52.pdf>. Materiale universitario su modello entità-relazione, passaggio al progetto relazionale e normalizzazione.
- **Data Modeling in MongoDB**, MongoDB Database Manual, consultato il 29 luglio 2026: <https://www.mongodb.com/docs/manual/data-modeling/>. Documenta il modello a documenti, la flessibilità dello schema, embedding, riferimenti e progettazione guidata dai pattern di accesso.
- **Embedded Data in Your MongoDB Schema**, MongoDB Database Manual, consultato il 29 luglio 2026: <https://www.mongodb.com/docs/manual/data-modeling/embedding/>. Descrive vantaggi e compromessi dell’incorporamento di dati correlati in un documento.
- **Recommendation 13 — Fit for purpose data quality design approach**, Interoperable Europe Portal, Commissione europea, consultata il 29 luglio 2026: <https://interoperable-europe.ec.europa.eu/collection/elise-european-location-interoperability-solutions-e-government/solution/eulf-blueprint/recommendation-13>. Richiama, fra le dimensioni della qualità, tempestività, accuratezza, completezza, integrità, coerenza e conformità alle specifiche, secondo un criterio adeguato allo scopo.

## Decisioni editoriali

- Usare il modello relazionale come nucleo principale, distinguendo modello concettuale, schema logico e istanza.
- Presentare 1NF, 2NF e 3NF attraverso anomalie e dipendenze, senza trasformare il capitolo in un corso formale di teoria relazionale.
- Spiegare le query su uno schema dichiarato; non usare sintassi avanzata non portabile.
- Trattare ACID e isolamento a livello concettuale, segnalando che i dettagli dipendono dal DBMS.
- Non equiparare indice, chiave e vincolo: possono essere collegati nell’implementazione, ma hanno funzioni concettuali differenti.
- Presentare NoSQL come insieme di famiglie. Il modello documentale è documentato direttamente; chiave-valore, wide-column e grafo restano classificazioni introduttive da sottoporre a review specialistica.
- Descrivere la qualità come adeguatezza allo scopo tradotta in dimensioni, regole, metriche e azioni correttive.
- Limitare la sicurezza a ruoli, privilegi, accesso minimo, audit e raccordi; IAM e incident response appartengono ai capitoli 8 e 9.

## Limiti e review

- Le forme normali sono esposte a livello didattico: dipendenze multivalore, BCNF e normalizzazioni superiori restano fuori perimetro.
- Le query e i comportamenti relativi a `NULL`, join e isolamento devono essere verificati sul DBMS eventualmente richiesto dal bando.
- MongoDB è una fonte primaria per il modello documentale, non una fonte neutrale per valutare tutte le famiglie NoSQL.
- Le dimensioni di qualità vanno adattate allo scopo e al dataset; non esiste una soglia universale.
- Schema, query, esercizi e soluzioni richiedono revisione manuale di un database specialist.

## Collegamenti

- [[topics/database-e-sql]]
- [[topics/informatica]]
- [[books/il-metodo-bando/chapters/informatica-pa-digitale-competenze-digitali]]
- [[books/moduli/m-tr01-ict-trasformazione-digitale/chapters/04-basi-dati-sql-nosql-qualita-dato]]
