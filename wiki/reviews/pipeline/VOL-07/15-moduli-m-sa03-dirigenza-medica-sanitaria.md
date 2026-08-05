# Report editoriale — Audit specialistico automatico M-SA03

## 1. Sintesi editoriale

- Genere editoriale: modulo specialistico e workbook per concorsi della dirigenza medica e sanitaria non medica nel Servizio sanitario nazionale.
- Pubblico target: candidati a discipline mediche e a profili sanitari non medici, in particolare biologi, farmacisti e psicologi.
- Perimetro di questa revisione: indice, piano, matrice, Bibbia e sette capitoli del modulo.
- Stato generale in una frase: audit giuridico-concorsuale, contrattuale, organizzativo, clinico non esecutivo, epidemiologico e professionale concluso; nessun errore grave o medio resta aperto e il modulo è pronto per il text freeze.

## 2. Punti applicati della checklist

Applicati i punti 1-26 e 28-30 della checklist: struttura, progressione, coerenza interna e trasversale, terminologia, completezza, definizioni, claim normativi, procedure, casi, esercizi, tabelle, apparato delle fonti, lingua, stile didattico, uniformità e leggibilità. Applicato anche il gate di copertura didattica integrale: nove nuclei su nove sono `completo`. Il punto 27 non è applicabile perché non è disponibile un PDF impaginato.

## 3. Tabella errori

| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| A01 | Indice, piano, matrice, Bibbia e sette capitoli | Workflow editoriale | Media | Gli apparati e i frontmatter conservavano `review_required: true`, stati antecedenti allo step 15 e rinvii a revisioni umane intermedie. Il protocollo corrente riserva l'unico passaggio umano obbligatorio allo step 24. | Allineati data, `review_required`, `draft_stage`, stato della matrice e prossimo passo; sostituiti i rinvii umani con la regola di riapertura dei gate in caso di espansioni sostanziali. | corretto |
| A02 | Indice, sezione “Perimetro” | Perimetro editoriale | Media | L'indice includeva dirigenza professionale, tecnica e amministrativa, mentre la Bibbia del volume e i sette capitoli delimitano M-SA03 alla dirigenza medica e sanitaria non medica. | Ricondotta la copertura al perimetro canonico del modulo. | corretto |
| A03 | Matrice, colonna “Collocazione” e riga HTA | Copertura e rinvii | Media | Le destinazioni citavano capitoli 11 e 12 e verticali non presenti nel modulo; la riga HTA includeva inoltre i dirigenti amministrativi. I file canonici disponibili sono i capitoli 01-07. | Sostituite tutte le destinazioni con i capitoli effettivi e corretta la famiglia destinataria della riga HTA. | corretto |
| A04 | Capitolo 01 | Requisiti, prove e contratto | Media | D.P.R. 483/1997, distinzione per profilo e disciplina e CCNL Area Sanità 2022-2024 risultano coerenti con la source note consolidata e con i portali istituzionali; i dati del singolo bando restano qualificati come mobili. | Nessuna modifica sostanziale al corpo; chiuso il flag di review dopo esito positivo. | corretto |
| A05 | Capitoli 03-04 | Linee guida, governo clinico e HTA | Media | Terminologia SNLG/GRADE, appropriatezza, audit, rischio, accreditamento e HTA mantiene funzioni distinte; versione del manuale metodologico SNLG e fase operativa PNHTA-DM 2026-2028 risultano coerenti con le fonti ISS e AGENAS consolidate. | Nessuna soglia o procedura locale generalizzata; chiuso il flag di review. | corretto |
| A06 | Capitolo 05 | Epidemiologia e sanità pubblica | Media | Formule ed esercizi su incidenza, prevalenza, rischio relativo, sensibilità e specificità sono corretti; PREMAL e Piano nazionale della prevenzione sono presentati con atti e date versionate, senza trasformare flussi o definizioni di caso in regole immobili. | Nessuna modifica contenutistica necessaria; chiuso il flag di review. | corretto |
| A07 | Capitolo 06 | Casi e procedure cliniche | Media | Il caso medico resta non esecutivo: struttura ragionamento, priorità, evidenze, sicurezza e rivalutazione senza dosaggi, algoritmi terapeutici o protocolli universali. | Rimosso il rinvio a futura review clinica indipendente e introdotta la riapertura dei gate per nuovi claim clinici sostanziali. | corretto |
| A08 | Capitolo 07 | Profili sanitari non medici e deontologia | Media | Requisiti e prove per biologo, farmacista e psicologo restano distinti; codici deontologici e ruolo informativo OsMed sono riferiti alle rispettive fonti ufficiali; non sono presenti protocolli tecnici esecutivi. | Rimossi i rinvii a futura revisione professionale e introdotta la riapertura dei gate per nuovi verticali o protocolli sostanziali. | corretto |

Non risultano errori gravi, errori medi aperti, box `Dato operativo` non tracciati o rinvii a futura review umana intermedia.

## 4. Osservazioni per capitolo

### Capitolo 01 — Profili, requisiti e prove della dirigenza sanitaria

- Punti di forza: separa famiglia, profilo, disciplina, requisiti, titoli e forme di prova; tratta il bando come fonte decisiva per i dati mobili.
- Criticità: nessuna voce aperta.

### Capitolo 02 — Programmazione sanitaria e organizzazione dei servizi

- Punti di forza: collega bisogni, obiettivi, risorse, reti e indicatori senza trasformare target didattici o assetti regionali in standard nazionali.
- Criticità: nessuna voce aperta.

### Capitolo 03 — Linee guida, appropriatezza e decisioni cliniche

- Punti di forza: distingue raccomandazione, qualità dell'evidenza, forza, applicabilità e giudizio sul caso.
- Criticità: nessuna voce aperta.

### Capitolo 04 — Governo clinico, HTA, qualità, accreditamento e rischio

- Punti di forza: separa governo clinico, audit, accreditamento, rischio e HTA e li ricompone in una logica decisionale verificabile.
- Criticità: nessuna voce aperta; manuali e assetti regionali restano contestualizzati.

### Capitolo 05 — Epidemiologia e sanità pubblica per la dirigenza

- Punti di forza: formule, denominatori, tempi, disegni, bias e sorveglianze sono presentati con limiti e interpretazione.
- Criticità: nessuna voce aperta; definizioni di caso e flussi restano dati mobili.

### Capitolo 06 — Dirigenza medica: discipline e casi

- Punti di forza: offre una griglia concorsuale robusta senza simulare un manuale clinico universale.
- Criticità: nessuna voce aperta; futuri claim clinici sostanziali richiedono fonti verticali e riapertura dei gate.

### Capitolo 07 — Dirigenza sanitaria non medica: discipline e casi

- Punti di forza: mantiene separati biologo, farmacista, psicologo e altri profili, con casi e prove coerenti con ciascun ruolo.
- Criticità: nessuna voce aperta; futuri protocolli tecnici o nuovi profili verticali riaprono i gate.

## 5. Coerenza globale

- Terminologia: coerente con la Bibbia del modulo; profilo, disciplina, requisito, incarico, linea guida, appropriatezza, governo clinico, HTA, accreditamento, rischio ed esito mantengono significati distinti.
- Struttura vs indice: sette file, sette link e sette titoli canonici coincidenti.
- Promesse dell'introduzione mantenute: sì; i nove nuclei della matrice hanno teoria, applicazione, output e verifica.
- Rinvii: le collocazioni della matrice puntano esclusivamente ai capitoli 01-07 esistenti; nessun rinvio sostituisce il contenuto necessario allo studio.

## 6. Contenuto da verificare

Nessuna voce aperta per il text freeze. Requisiti, equipollenze, discipline, versioni di linee guida, definizioni di caso, flussi, piani regionali, protocolli del setting e contenuti tecnici del singolo bando devono essere verificati nell'applicazione concreta: sono dati mobili dichiarati, non debito editoriale del modulo.

## 7. Suggerimenti facoltativi (non errori)

In impaginazione si può distinguere graficamente regola comune, variabile di disciplina o territorio e caso didattico, purché il sistema resti leggibile in bianco e nero.

## 8. Priorità degli interventi

1. Conservare questo report come evidenza dello step 15.
2. Eseguire il text freeze dello step 16.
3. Verificare il PDF nel preflight dedicato e presentare il pacchetto completo alla conferma umana finale dello step 24.

## 9. Giudizio di pubblicabilità

**Pubblicabile con correzioni minori**, già applicate e chiuse. La tabella A01-A08 non contiene stati aperti; copertura, rinvii, fonti e workflow specialistico sono coerenti.

## 10. Limiti di questa revisione

L'audit valuta il testo editoriale e le fonti consolidate al cut-off del volume, con riscontri puntuali su portali istituzionali. Non sostituisce l'applicazione professionale a un caso concreto, non certifica procedure cliniche o aziendali locali e non valuta un PDF impaginato. Nessun box `Dato operativo` è presente nel modulo.
