from pathlib import Path
import shutil, re
A=Path('artifacts/correzioni-collana-2026-10-02')
R=Path('wiki/reviews/pipeline/VOL-04');R.mkdir(exist_ok=True)
audit=Path('wiki/reviews/audit-integrale-2026-10-02/VOL-04.md').read_text('utf-8')
(R/'13-moduli-m-fc04-giustizia.md').write_text(audit+'\n\n## Presa in carico del 3 ottobre 2026\n\nRevisione trasversale integrale già eseguita sui 17 originali inventariati. Il presente report ne conserva i 29 rilievi per la fase di correzione. Indice, premessa, matrice e piano riletti: la matrice storica sovrastima la completezza e la dichiarazione di preflight del modulo non è valida per questa revisione. Prossimo passo: correzioni, fonti consolidate e audit specialistico; nessuna pubblicabilità dichiarata.\n','utf-8')
p=Path('wiki/books/moduli/m-fc04-giustizia/planning/03-bibbia-modulo.md')
if not p.exists():p.write_text('''---
type: editorial_plan
title: "Bibbia di revisione — Giustizia e Ufficio per il processo"
updated_at: 2026-10-03
review_required: true
canonical: false
---

# Bibbia di revisione — VOL-04

## Progressione e perimetro

Capitoli 1–3: profili, amministrazione, uffici e competenze. Capitoli 4–5: struttura UPP e prodotti del lavoro AUPP. Capitoli 6–7: regole processuali civili e penali necessarie ai servizi. Capitoli 8–12: cancelleria, spese, casellario, UNEP e telematico. Capitoli 13–14: minorile, comunità e penitenziario. Capitoli 15–17: applicazioni complete, conclusione e fonti.

Materie comuni nel volume Il Metodo BANDO con rinvio preciso; diritto processuale specialistico spiegato qui, senza rinvii al base per contenuti che il base non sviluppa. Magistratura e professioni legali rinviate al relativo percorso di Carriere speciali. Pedagogia e servizio sociale non sostituite dall'ordinamento penitenziario.

## Distinzioni vincolanti

- Funzione giudiziaria comprende funzione giudicante e requirente; la decisione giurisdizionale è del giudice.
- UPP è struttura; AUPP è una figura del personale. La Procura ordinaria ha segreteria del PM, non un UPP ordinario derivato dall'art. 1 D.Lgs. 151/2022.
- Magistrato dirigente e dirigente amministrativo hanno competenze distinte e programmazione coordinata ex D.Lgs. 240/2006.
- DGSIA nelle fonti storiche; assetto corrente del DIT da aggiornare con le quattro direzioni attuali.
- Copia conforme e titolo esecutivo non ripropongono la formula esecutiva abolita.
- Dati relativi a condanne e reati distinti dalle categorie particolari di dati.
- Regola nazionale, disposizione transitoria, istruzione tecnica e prassi locale sempre distinte.

## Prove e apparati

Rielaborare gli 84 quiz su regole insegnate, con distrattori plausibili e chiavi distribuite. Inserire fascicolo fittizio lavorato e sei simulazioni con dati, svolgimenti e rubriche verificabili. Conservare strumenti compilabili dopo l'esempio risolto.

## Controllo delle dipendenze

Correzione normativa → source note → topic/entity → capitolo → quiz → indice e matrice. Il report immutabile del 2 ottobre resta intatto. Il registro delle correzioni distingue applicato, verificato nel testo e verificato nel PDF. Il volume resta non pubblicabile fino a chiusura dei 29 rilievi testuali e dei rilievi di produzione.
''','utf-8')
for p in [Path('wiki/books/moduli/m-fc04-giustizia/index.md'),Path('wiki/books/vol-04-giustizia-upp/planning/02-matrice-copertura-didattica.md')]:
 backup=A/'before-text/VOL-04/reopening'/p.name;backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():shutil.copyfile(p,backup)
 t=p.read_text('utf-8').replace('review_required: false','review_required: true')
 t=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-03',t,flags=re.M)
 t+='\n\n## Rettifica di stato — 3 ottobre 2026\n\nLe attestazioni di completezza e preflight sopra riportate descrivono il ciclo storico. La revisione integrale del 2 ottobre ha identificato 29 rilievi testuali e ulteriori problemi PDF: stato corrente **in correzione, non pubblicabile**. Le righe della matrice saranno riconciliate sull’effettivo testo corretto, con prove specifiche.\n'
 p.write_text(t,'utf-8')
print('Report 13 e bibbia creati; stato storico qualificato')
