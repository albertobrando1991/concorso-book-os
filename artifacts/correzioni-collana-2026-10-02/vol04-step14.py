from pathlib import Path
import json,re,hashlib
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc04-giustizia');R=Path('wiki/reviews/pipeline/VOL-04')
text=(R/'13-moduli-m-fc04-giustizia.md').read_text('utf-8').replace('Revisione trasversale dopo le correzioni','Applicazione e riesame delle correzioni')
by=[[1],[2,12],[2,3],[4,17],[4],[5,15],[6],[7],[7],[8],[8],[9],[9],[10],[10],[11],[11],[12],[12],[13],[13],[14],[14],[14],[15],[17],list(range(1,15)),[5,10,11,12,13,14,15],[15,16]]
rows=json.loads((A/'VOL-04-ledger.json').read_text('utf-8'))['findings'];mapping='\n\n### Registro per file ed evidenza\n\n| ID | File modificato | Correzione | Fonte/evidenza | Stato finale |\n|---|---|---|---|---|\n'
for i,row in enumerate(rows):
 paths=[next((B/'chapters').glob(f'{n:02}-*.md')).as_posix() for n in by[i]]
 mapping+='| '+row['id']+' | '+'; '.join(paths)+' | '+row['evidence']+' | Frontmatter dei file, nove source notes 2026-10-03; delta tematici e VOL-04-text-verifica.json | Corretto e verificato |\n'
text=text.replace('## 4. Osservazioni per capitolo',mapping+'\n## 4. Osservazioni per capitolo')
text=text.replace('## 7. Migliorie opzionali','### Riesame dei passaggi sostanziali\n\nRipetuto il controllo di copertura su nuove regole, casi, quiz e apparati. La passata Humanizer conserva il tono manualistico: rimossi rinvii generici, sostituite consegne astratte con dati e decisioni, ridotte formule promozionali e affermazioni assolute prive di bando. La micro-revisione controlla sintassi, nomi degli istituti, autorità, date e concordanza tra risposta e spiegazione. Nessuna opinione o esperienza personale inventata. I suggerimenti facoltativi non sono trattati come obblighi.\n\n## 7. Migliorie opzionali')
(R/'14-moduli-m-fc04-giustizia.md').write_text(text,'utf-8')
# Document actual read scope without changing raw originals.
N=A/'norme-vol04';p=N/'manifest-digitale-norme.json';d=json.loads(p.read_text('utf-8'))
for row in d:row.update(readComplete=True,readScope='Articolo indicato, testo vigente estratto e identificato; non intero atto normativo.')
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
p=N/'manifest-digitale.json';d=json.loads(p.read_text('utf-8'))
for row in d:
 n=row['name'];scope={'pct-specifiche2024.pdf':'Artt. 7, 15–17 e 19; non lettura integrale delle 28 pagine.','cassazione-rassegna-tematica2025.pdf':'Sezione deposito civile, pagine stampate 109–110 (PDF 112–113); non intera rassegna.','pct-reginde.html':'Descrizione del registro e soggetti abilitati; dettagli storici CEC-PAC non assunti come procedura corrente.'}.get(n,'Testo del documento/articolo acquisito letto integralmente.')
 row.update(readComplete=n not in {'pct-specifiche2024.pdf','cassazione-rassegna-tematica2025.pdf','pct-reginde.html'},readScope=scope)
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),'utf-8')
print('Report14 e ambiti di lettura registrati.')
