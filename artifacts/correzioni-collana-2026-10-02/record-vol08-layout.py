from pathlib import Path
import shutil,json
A=Path(__file__).parent;P=Path('wiki/reviews/pipeline/VOL-08');label='vol-08-release-20261003';v=json.loads((A/(label+'-verification.json')).read_text());vis=json.loads((A/'VOL-08-production-visual.json').read_text())
for step,name in [('19','19-impaginazione-kdp.md'),('20','20-audit-pagina-per-pagina.md')]:
 p=P/name;archive=A/f'VOL-08-step{step}-before-production.md'
 if not archive.exists():shutil.copy2(p,archive)
 p.write_text(f'''# VOL-08 — Step{step}, prova corrente del3ottobre2026

PDF244pagine, SHA256`{v['sha256']}`. Formato481,92×691,92pt, colonna singola, corpo Garamond10,99pt effettivi, indice/tabelle9,49–9,50pt, codice Consolas9,49pt. Margini speculari e numerazione conservati. Zero overflow DOM, zero testo oltre la pagina, font incorporati, nessun asset mancante. Conteggio DOM=PDF.

Indice:13capitoli e82nuclei confrontati direttamente con le pagine PDF, zero discrepanze. Nessuna eliminazione di contenuti per ottenere il riflusso. Tabelle dense proiettate in gruppi collegati. Pseudocodice44, SQL66, timeline163–164, apertura222, diario237 echiusura244 esaminati ingranditi, oltre all’indice6.

Copertura: tutte16tavole contatto delle244pagine,8ingrandimenti. Le miniature controllano geometria, ritmo e salti; non equivalgono a lettura di ogni parola alla piena risoluzione. Metriche per ogni pagina e registro esatto in artifacts/correzioni-collana-2026-10-02/{label}-proof-audit/metrics.json e VOL-08-production-visual.json.

Le difformità storiche P08-01–05 sono risolte nella prova: indice leggibile, timeline senza spezzature patologiche, diario compilabile, gerarchia dei titoli distinta, avvertenza integrata nella chiusura. Nessun nuovo difetto locale bloccante osservato. Promessa digitale e dati editoriali comuni restano aperti: questa verifica non dà il via libera alla pubblicazione, né certifica KDP o stampa fisica.
''',encoding='utf8')
print('Recorded actual evidence19/20; CLI completion remains sequential.')
