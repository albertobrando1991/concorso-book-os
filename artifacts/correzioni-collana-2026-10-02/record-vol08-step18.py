from pathlib import Path
import shutil
A=Path(__file__).parent;p=Path('wiki/reviews/pipeline/VOL-08/18-moduli-m-tr01-ict-trasformazione-digitale.md');archive=A/'VOL-08-step18-before-production.md'
if not archive.exists():shutil.copy2(p,archive)
p.write_text('''# VOL-08 — Step18, verifica corrente del 3 ottobre2026

| Asset | Problema | Correzione | Verifica nel Book Studio e PDF | Esito |
|---|---|---|---|---|
| Immagini raster | Nessuna immagine nei13capitoli né nel PDF244pagine | Nessuna grafica decorativa aggiunta | Inventario PDF zero immagini, zero missingImages | N/D motivato |
| Timeline procurement | Parole spezzate e intestazioni ripetute nella prova storica | Proiezione delle colonne in tabelle collegate | pp.163–164 viste ingrandite; celle leggibili e fasi continue | Verificato |
| Diario compilabile | Otto colonne troppo strette | Tre gruppi di campi collegati4/4/2, righe vuote con spazio | p.237 vista ingrandita; etichette chiare e righe compilabili | Verificato |
| Pseudocodice e SQL | Corpo dei blocchi ridotto nella prova storica | Consolas9,49pt effettivi in export | pp.44/66 viste ingrandite; indentazione e operatori integri | Verificato |

Seconda passata: tutte16tavole contatto e otto zoom del registro VOL-08-production-visual.json. Zero overflow DOM e testo fuori pagina. Le quattro colonne del diario identificano campi brevi; mantengono spazio leggibile nella prova, senza ridurre il carattere. Il giudizio resta sulla prova digitale locale; nessuna stampa fisica o validazione dei servizi digitali.
''',encoding='utf8')
print(p)
