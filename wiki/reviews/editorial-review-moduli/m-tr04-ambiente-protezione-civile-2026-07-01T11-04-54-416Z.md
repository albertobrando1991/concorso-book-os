---
id: review-editorial-moduli/m-tr04-ambiente-protezione-civile-1782903894416
type: review
title: "Revisione editoriale - moduli/m-tr04-ambiente-protezione-civile"
status: completed
issue_type: editorial_review
severity: high
affected_pages: []
created_at: 2026-07-01T11:04:54.416Z
updated_at: 2026-07-01T11:04:54.416Z
review_required: false
canonical: true
tags: [revisione-editoriale, pubblicabilita]
---

# Report editoriale — M-TR04 - Ambiente e protezione civile

## 1. Sintesi editoriale
- Genere editoriale: modulo specialistico/workbook per concorsi pubblici.
- Pubblico target: candidato che usa Il Metodo BANDO e deve adattarlo ad ambiente, rifiuti, territorio e protezione civile.
- Perimetro di questa revisione: intero libro/modulo M-TR04, sulla base dei file disponibili.
- Stato generale in una frase: il modulo è ancora uno scaffold interno, non un testo editoriale pubblicabile.

## 2. Punti applicati della checklist
1. Applicato — indice non coerente: indicizza un piano interno come capitolo.
2. Applicato — struttura incompleta: manca il libro effettivo.
3. Applicato — progressione non valutabile nel merito perché non ci sono capitoli.
4. Applicato — gerarchia presente ma non ancora editoriale.
5. Applicato — giudizio finale negativo.
6. Applicato — il piano è coerente come nota di lavoro.
7. Applicato — non valutabile tra capitoli: esiste un solo file.
8. Applicato — terminologia generale coerente.
9. Applicato — spiegazioni assenti come testo didattico.
10. Applicato con limite — definizioni non presenti.
11. Applicato con limite — nessun errore concettuale verificabile, ma contenuto assente.
12. Applicato con limite — norme non presenti né verificabili.
13. Applicato — esempi assenti.
14. Applicato — richiami generici presenti, apparato operativo assente.
15. Applicato con limite — apparato normativo non consolidato.
16. Applicato — sintassi semplice.
17. Applicato — chiaro come piano, non come capitolo.
18. Applicato — tono interno, non pubblicabile.
19. Applicato — stile didattico non ancora sviluppato.
20. Applicato — nessuna ripetizione rilevante.
21. Applicato — nessuna contraddizione locale.
22. Applicato — grammatica sostanzialmente corretta.
23. Applicato — presenti accenti mancanti.
24. Applicato — punteggiatura accettabile.
25. Applicato — refusi lievi.
26. Applicato — uniformità grafica accettabile nel file.
27. Non applicabile — nessun PDF/impaginato disponibile.
28. Applicato con limite — layout editoriale del modulo assente.
29. Applicato con limite — leggibilità buona, ma testo troppo breve e interno.
30. Applicato — qualità complessiva non pubblicabile.

## 3. Tabella errori
| ID | Posizione | Categoria | Gravita | Descrizione | Correzione proposta | Stato |
|----|-----------|-----------|---------|-------------|----------------------|-------|
| E01 | Intero modulo | 5. Idoneità finale alla pubblicazione | Grave | Il modulo non contiene capitoli editoriali: il solo testo disponibile è un piano di lavoro con “Da sviluppare...” | Sviluppare i capitoli effettivi del modulo prima della revisione finale. Il piano non deve essere considerato contenuto pubblicabile. | Aperto |
| E02 | `chapters/00-piano-editoriale.md`; `index.md`, Capitoli di lavoro | 1. Indice coerente con struttura reale | Grave | Il piano editoriale interno è collocato e indicizzato come capitolo. La memoria operativa del progetto indica che per i moduli specialistici il piano deve stare in `planning/`, non in `chapters/`. | Spostare il file in `planning/00-piano-editoriale.md`, rimuoverlo dai capitoli pubblicabili e creare capitoli reali in `chapters/`. | Proposto |
| E03 | Struttura modulo | 1. Indice / 27-28. Impaginazione e layout | Grave | Mancano front matter e indice del modulo secondo la regola operativa dei moduli specialistici. | Creare `front-matter/` con FM1 servizi digitali, FM2 frontespizio, FM3 copyright/note, FM4 sommario, FM5 premessa, FM6 indice; usare indice `chapters-only`. | Aperto |
| E04 | `index.md`, Fonti da consolidare; capitolo, Fonti da consolidare | 12. Errori normativi o contenutistici / 15. Apparato normativo | Grave | Le fonti settoriali sono dichiarate “da consolidare”; per ambiente, rifiuti, territorio e protezione civile questo blocca la pubblicazione. | Consolidare bandi rappresentativi, fonti ufficiali di settore, topic/entity pages e source notes prima della scrittura. | Da verificare |
| E05 | Frontmatter del capitolo | 30. Qualità editoriale complessiva | Grave | Il metadata dichiara `status: structure`, `draft_stage: structure-ready`, `review_required: true`, `confidence: 0.55`: è uno stato preparatorio, non finale. | Aggiornare lo stato solo dopo scrittura, revisione contenutistica e review umana delle parti normative. | Aperto |
| E06 | Struttura prevista | 9. Completezza delle spiegazioni | Media | La struttura è corretta come scaletta, ma troppo generica per un modulo specialistico: non distingue profili, prove, enti, rischi e macroaree operative. | Trasformare i 9 punti in capitoli con perimetro, output didattici, casi guidati e riferimenti specifici. | Aperto |
| E07 | Obiettivo / Perimetro | 17. Chiarezza espositiva | Media | “Ambiente, rifiuti, territorio, protezione civile e funzioni tecniche collegate” è un campo molto ampio e non delimita cosa resta fuori. | Inserire un paragrafo “Dentro/fuori dal modulo” con confini editoriali e limiti di copertura. | Proposto |
| E08 | Collegamenti obbligatori | 14. Note, richiami, tabelle, box e schemi | Media | I collegamenti sono solo generali; mancano richiami a fonti, topic o entity pages specifiche del modulo. | Dopo il consolidamento, aggiungere link a topic/entity/source notes specifiche per ambiente, rifiuti, territorio e protezione civile. | Da verificare |
| E09 | Lettore; Fonti da consolidare | 23. Ortografia | Lieve | Mancano accenti: “priorita”, “gia”. | Correggere in “priorità” e “già”. | Proposto |
| E10 | Titolo/H1 del piano | 4. Titoli e gerarchia | Lieve | Il titolo contiene codice modulo e funzione interna; va bene per un file di planning, non per un capitolo visibile. | Se resta piano interno: mantenere. Se diventa capitolo: rinominare con titolo editoriale rivolto al lettore. | Proposto |

## 4. Osservazioni per capitolo
### Capitolo 0 — Piano editoriale - M-TR04 Ambiente e protezione civile
- Punti di forza: obiettivo, lettore, struttura prevista e collegamenti obbligatori sono chiari; il testo rispetta l’idea dei moduli come estensione del Metodo BANDO.
- Criticità: non è un capitolo per il lettore, ma una nota di lavoro; manca testo didattico, mancano fonti consolidate, mancano front matter e capitoli effettivi.

## 5. Coerenza globale
- Terminologia: sostanzialmente coerente; da uniformare solo gli accenti e la resa dei titoli interni.
- Struttura vs indice: incoerente; l’indice del modulo presenta il piano editoriale come capitolo pubblicabile.
- Promesse dell’introduzione mantenute: no; non esiste ancora una premessa editoriale pubblicabile e il testo promette uno sviluppo futuro non presente.

## 6. Contenuto da verificare
- Bandi rappresentativi recenti per profili ambiente, territorio, rifiuti, protezione civile e funzioni tecniche collegate.
- Normativa ufficiale di settore, da consolidare in source notes prima della scrittura.
- Topic/entity pages specifiche del wiki: da collegare e verificare.
- Review umana richiesta per ogni parte normativa o settoriale prima della pubblicazione.

## 7. Suggerimenti facoltativi (non errori)
- Separare “casi guidati”, “quiz” e “risposte sintetiche” in tre output distinti, se il modulo deve avere forte valore operativo.
- Aggiungere una mini-mappa iniziale dei profili tipici solo dopo avere consolidato bandi reali.
- Prevedere una checklist finale compilabile in stile workbook, coerente con il Metodo BANDO.

## 8. Priorità degli interventi
1. Risolvere E01, E02, E03: separare planning, front matter e capitoli pubblicabili.
2. Risolvere E04: consolidare fonti, topic/entity pages e review normativa.
3. Risolvere E05-E08: trasformare la scaletta in capitoli didattici completi.
4. Solo dopo intervenire su E09-E10. Correggere i refusi prima della struttura sarebbe uno spreco di tempo editoriale.

## 9. Giudizio di pubblicabilità
Non pubblicabile allo stato attuale

Motivazione: la tabella contiene errori gravi strutturali e contenutistici, in particolare E01, E02, E03 ed E04. Il materiale disponibile è un piano editoriale interno, non un modulo completo destinato al lettore.

## 10. Limiti di questa revisione
La revisione ha valutato i file disponibili nel modulo: `index.md` e `chapters/00-piano-editoriale.md`. Non è stato possibile valutare capitoli editoriali, PDF impaginato, apparato normativo o accuratezza settoriale perché non sono ancora presenti nel modulo.