from pathlib import Path
import json
s='vol-04-spese-verifica-2026-10-03'
for f in ['wiki/topics/giustizia-e-upp.md','wiki/entities/ministero-della-giustizia.md','wiki/sources/cancelleria-spese-casellario-unep-m-fc04.md']:
 p=Path(f);t=p.read_text('utf-8')
 if s not in t:t+=f'\n\n## Spese di giustizia — aggiornamento del 3 ottobre 2026\n\n[[sources/{s}]] consolida soglia13.659,64 euro e computo familiare distinto civile/penale; competenze, termini e regimi di spesa; CU minimo43 e Corte137/2026; recupero civile248c3-bis. La scheda centrale19agosto conferma SPEdiGIUS dal1luglio2026, superando la precedente qualificazione solo locale. Capitolo09: [[books/moduli/m-fc04-giustizia/chapters/09-spese-giustizia-patrocinio-recupero]].\n'
 p.write_text(t,'utf-8')
p=Path('wiki/index.md');t=p.read_text('utf-8')
if s not in t:p.write_text(t+f'\n- [[sources/{s}]] — spese, patrocinio, CU, liquidazioni e SPEdiGIUS.\n','utf-8')
with Path('wiki/log.md').open('a',encoding='utf-8') as f:f.write('\n\n## 2026-10-03 — Fonti spese VOL04\n\nConsolidati TUSG, decreto reddituale2025, circolare24aprile2025 e Corte137/2026; CU minimo non annullato, patrocinio e recupero distinti per rito. Verificato avvio nazionale SPEdiGIUS nella scheda ministeriale19agosto2026.\n')
print('Consolidato wiki spese')
