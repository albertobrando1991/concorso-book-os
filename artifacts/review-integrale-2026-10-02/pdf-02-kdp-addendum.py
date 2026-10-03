import pathlib,json
R=pathlib.Path(__file__).resolve().parents[2]
A=R/'artifacts/review-integrale-2026-10-02'
p=R/'wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-02.md'
s=p.read_text(encoding='utf8')
row='| P02-10 | Candidato rebuild: 867 pagine, circa 6,69 × 9,61 pollici; precedente: 830 pagine | Specifiche di produzione KDP | Grave | Entrambi superano il massimo KDP di 828 pagine per questa gabbia in bianco e nero su carta bianca e a colori Premium; gli altri supporti previsti hanno massimi inferiori (crema 776, pastalegno 812, colore standard 600). Verifica ufficiale del 2 ottobre 2026: [KDP, tabella gabbie](https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6). Il rebuild supera il limite di 39 pagine già prima dell’eventuale arrotondamento a numero pari. | Decidere una configurazione editoriale e produttiva supportata, valutando una suddivisione organica del volume; preservare copertura e leggibilità, poi rigenerare interni e copertina e verificare il conteggio finale nel Previewer. Nessuna compressione automatica del corpo o taglio dei contenuti per rientrare nel limite. | Aperto |\n'
s=s.replace('\nIl candidato precedente', '\n'+row+'\nIl candidato precedente')
p.write_text(s,encoding='utf8')
lp=A/'VOL-02-ledger.json'; l=json.loads(lp.read_text(encoding='utf8'));l['pdfReview']['findingIds'].append('P02-10');l['pdfReview']['productionCheck']={'claim':'867 e 830 pagine eccedono massimo 828 KDP per gabbia 6.69x9.61, nero su bianco o colori Premium','url':'https://kdp.amazon.com/it_IT/help/topic/GVBQ3CMEQW3W2VL6','checkedAt':'2026-10-02','measuredInches':[6.693333095974392,9.60999976264106]};lp.write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
rows=json.loads((A/'figures-VOL-02/manifest.json').read_text(encoding='utf8'))
for x in rows:x.update(visuallyInspected=True,inspection='Each of all ten original PNGs viewed individually at original 1600x900 resolution, plus three overview sheets',report='wiki/reviews/audit-integrale-2026-10-02/PDF-VOL-02.md',limitations=['No physical print proof; print-size readability checked selectively in PDF'])
(A/'figures-VOL-02/visual-review.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('P02-10 and 10 visual-review records saved')
