# Integrazione visiva M-FC05 — Specifica di progetto

## Obiettivo

Integrare il solo modulo **M-FC05 — Authority indipendenti**, composto dai capitoli 1–15, con un sistema di infografiche editoriali didattiche. Il lavoro non riguarda il libro base né gli altri volumi; questi ultimi sono riferimenti vincolanti di stile, non oggetti di modifica.

## Perimetro e decisione

- Capitoli interessati: `wiki/books/moduli/m-fc05-authority-indipendenti/chapters/01-...md` fino a `15-...md`.
- Stato rilevato: il modulo non contiene asset grafici incorporati; perciò ogni capitolo richiede una nuova copertura visiva.
- Riferimenti visivi: `wiki/books/il-metodo-bando/assets/` e `wiki/books/moduli/m-fc02-agenzie-fiscali/assets/`.
- Approccio selezionato: **cinque infografiche per capitolo**, come nel Volume 2, realizzate e inserite in sequenza capitolo per capitolo. Il totale previsto è 75 soggetti grafici, ciascuno disponibile in SVG editabile e PNG di compatibilità.
- Esclusioni: fotografie stock, immagini decorative, icone prive di funzione, screenshot non indispensabili, modifiche al testo sostanziale dei capitoli.

## Linguaggio visivo vincolante

Ogni visual sarà un’infografica orizzontale `1600 × 1000 px`, con fondo Off-White `#F8FAFC`, card bianche con bordo `#CBD5E1`, angoli arrotondati e linee non inferiori a 2,5 px. Il testo interno userà Arial o un fallback sans-serif compatibile; titolo 43 px, sottotitolo 22 px, etichette 23–25 px, corpo 18–20 px.

La palette riprende il libro base e M-FC02:

- Navy `#10233F` / Ink `#0F172A` per titoli, struttura e flussi;
- Bordeaux `#7A2430` per casi, rischi, errori e rimedi;
- Muted Gold `#D4AF37` per nuclei, snodi e accenti;
- Green `#2F7D5A` per esiti, controlli e output;
- Teal `#1F6F78` per dati, strumenti e cooperazione;
- campiture tenui blu, bordeaux, oro, verde e teal per distinguere i nodi senza ridurre la leggibilità in stampa.

Ogni SVG avrà `title`, `desc`, `role="img"` e zone con testo contenuto in card. L’asset non conterrà testo sovrapposto al corpo della pagina: sarà inserito fra blocchi autonomi di Markdown, con alt text descrittivo e didascalia in corsivo.

## Architettura di ogni capitolo

Ogni capitolo riceve cinque visual con funzioni ricorrenti, adattate alla materia:

1. **Mappa BANDO**: dal programma di concorso alla risposta o all’output richiesto.
2. **Architettura concettuale**: soggetti, fonti, interessi e poteri oppure categorie da distinguere.
3. **Flusso procedimentale**: sequenza di regolazione, vigilanza, istruttoria, decisione e controllo, quando pertinente.
4. **Confronto o griglia decisionale**: differenze da non confondere, criteri, dati o rimedi.
5. **Sintesi pre-epilogativa**: mappa di ripasso che collega teoria, caso, errore tipico e output di prova.

Le cinque funzioni non implicano una rigida ripetizione: nel capitolo 15 la griglia di correzione e il piano di allenamento sostituiranno il flusso procedimentale; nei capitoli sulle singole authority, il confronto renderà visibili mandato, poteri, destinatari e tutela.

## Piano editoriale dei soggetti

| Capitolo | Cinque soggetti grafici previsti |
|---|---|
| 1. Le authority viste dal candidato | Mappa BANDO; panorama authority-settore-potere; percorso G/E/P; Decoder del bando; sintesi fonte-interesse-potere-procedimento-controllo. |
| 2. Indipendenza, governance, accountability e personale | garanzie di indipendenza; governance e responsabilità; ciclo di accountability; personale e incompatibilità; mappa dei controlli. |
| 3. Regolazione europea multilivello e reti | livelli UE-nazionale; reti delle authority; cooperazione e casi transfrontalieri; fonti e competenze; sintesi del coordinamento. |
| 4. Ciclo regolatorio, consultazione, AIR e VIR | Mappa BANDO; ciclo regolatorio; consultazione; AIR-VIR; sintesi evidenze-decisione-valutazione. |
| 5. Vigilanza, istruttoria, ispezioni, dati e prova | architettura della vigilanza; istruttoria; ispezione; qualità del dato e prova; garanzie e contraddittorio. |
| 6. Sanzioni, impegni, rimedi e controllo giurisdizionale | mappa dei poteri; procedimento sanzionatorio; impegni e rimedi; tutela e giudice; criteri di proporzionalità. |
| 7. Economia industriale, regolazione, econometria e contabilità regolatoria | mercato e fallimento; strumenti regolatori; dati ed evidenze; contabilità regolatoria; catena incentivo-qualità-tariffa. |
| 8. AGCM | mappa dell’Autorità; concorrenza-consumatore; istruttoria; pratiche scorrette e rimedi; sintesi caso-output. |
| 9. ARERA | mappa dell’Autorità; filiere e servizi; tariffa e qualità; dati e tutela utenti; sintesi regolatoria. |
| 10. AGCOM | mappa dell’Autorità; comunicazioni-media-piattaforme; utenti e garanzie; regolazione e vigilanza; sintesi dei poteri. |
| 11. CONSOB | mappa dell’Autorità; mercati-emittenti-intermediari; tutela investitore; vigilanza e sanzioni; sintesi della trasparenza. |
| 12. Banca d’Italia e IVASS | riparto di vigilanza; prudenziale-condotta; governance e rischi; banca-assicurazione; sintesi tutela-stabilità. |
| 13. Garante privacy | mappa GDPR-Garante; ciclo del trattamento; procedimento e misure; cooperazione europea; sintesi accountability. |
| 14. ANAC | prevenzione e integrità; PNA-RPCT; vigilanza; whistleblowing; sintesi rischio-segnalazione-rimedio. |
| 15. Laboratorio delle prove authority | percorso d’esame; rubriche di correzione; simulazioni G/E/P; diario degli errori; piano 30/60/90 giorni. |

## Inserimento e impaginazione

Per ogni capitolo gli asset saranno salvati in `assets/chapter-XX/` con nomi numerati `01-...`–`05-...`. Il Markdown userà il PNG come fallback in anteprima, preceduto da una breve frase di raccordo e seguito da una didascalia. Ogni inserimento sarà collocato dopo il blocco che introduce il concetto e prima del relativo caso, esercizio o epilogo; non sarà mai inserito fra titolo e primo paragrafo né dentro una tabella o un blockquote.

La verifica controllerà: proporzione coerente, alt text, didascalia, assenza di clipping e sovrapposizione, leggibilità dei testi, correttezza dei link e coerenza cromatica. Le immagini già eventualmente presenti saranno mantenute se superano gli stessi controlli; non verranno sostituite solo per uniformità estetica.

## Sequenza di esecuzione e criteri di accettazione

Si procede dal Capitolo 1 al Capitolo 15. Per ogni capitolo: audit del contenuto, creazione di SVG e PNG, inserimento Markdown, ispezione visiva e controllo dei riferimenti; quindi si passa al capitolo successivo. Un capitolo è concluso soltanto quando dispone di cinque asset correttamente collegati e nessuna immagine è decorativa, illeggibile o fuori gabbia.

Al termine saranno prodotti: i 75 asset, i riferimenti nei 15 capitoli e un breve registro di audit in `wiki/reviews/` con decisioni di mantenimento/creazione e verifiche di layout.
