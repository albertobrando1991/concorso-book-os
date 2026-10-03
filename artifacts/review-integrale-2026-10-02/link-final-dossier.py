from pathlib import Path
import json

base=Path('artifacts/review-integrale-2026-10-02')
result=json.loads((base/'final-verification.json').read_text(encoding='utf8'))
visual=json.loads((base/'visual-verification.json').read_text(encoding='utf8'))
assert result['textReviewComplete'] and result['chapters']==326 and not result['problems'] and visual['complete']
assert Path('wiki/reviews/audit-integrale-2026-10-02/README.md').exists()

index=Path('wiki/index.md')
content=index.read_text(encoding='utf8')
old='- [[reviews/audit-prepubblicazione-collana-2026-10-02]] — primo rapporto: 12 rilievi, proposte non applicate, revisione integrale ancora aperta.\n- [[reviews/registro-audit-collana-2026-10-02]] — registro dei 326 capitoli/appendici cartacei, con controlli eseguiti e verifiche residue.'
new=f'''- [[reviews/audit-integrale-2026-10-02/README]] — revisione diagnostica conclusa: 12 volumi, 326 capitoli/appendici letti integralmente; panorama dei 12 PDF e controllo delle figure. Correzioni da applicare; collana non pronta alla pubblicazione.
- [[reviews/audit-integrale-2026-10-02/registro-interventi]] — {result['actions']} voci operative con posizione, gravità e proposta; disponibile anche il CSV nella stessa cartella.
- [[reviews/audit-prepubblicazione-collana-2026-10-02]] — primo rapporto, conservato come storico e superato dal dossier integrale.
- [[reviews/registro-audit-collana-2026-10-02]] — registro preliminare storico; per lo stato conclusivo usare il dossier integrale.'''
if old in content:
    index.write_text(content.replace(old,new,1),encoding='utf8')
else:
    assert '[[reviews/audit-integrale-2026-10-02/README]]' in content, 'Index context changed'

for name in ['audit-prepubblicazione-collana-2026-10-02.md','registro-audit-collana-2026-10-02.md']:
    p=Path('wiki/reviews')/name
    text=p.read_text(encoding='utf8')
    marker='**Aggiornamento conclusivo del 2 ottobre 2026:**'
    if marker not in text:
        text=text.replace('status: in_progress','status: historical_superseded',1)
        start=text.index('\n# ')
        end=text.index('\n',start+1)
        text=text[:end]+f'\n\n{marker} il presente documento conserva la ricognizione iniziale. La lettura integrale dei 326 capitoli/appendici cartacei è stata successivamente completata: consultare il [dossier conclusivo](audit-integrale-2026-10-02/README.md) e il [registro degli interventi](audit-integrale-2026-10-02/registro-interventi.md). Le limitazioni e gli stati aperti riportati sotto descrivono il primo giro, non lo stato finale della revisione. Correzioni ancora da applicare.\n'+text[end:]
        p.write_text(text,encoding='utf8')

log=Path('wiki/log.md')
event=' | audit_integrale_collana_concluso | '
if event not in log.read_text(encoding='utf8'):
    with log.open('a',encoding='utf8') as out:
        out.write(f'\n- 2026-10-02{event}VOL-01/VOL-12 | Revisione diagnostica conclusa: 326/326 capitoli e appendici cartacei letti con quiz/casi; {result["actions"]} voci di intervento ({result["contentActions"]} testo, {result["pdfAndExportActions"]} PDF/figure/export). Panorama di 4861 pagine su 12 candidati, dettagli mirati e 308 immagini originali; verificati checksum. Fonti ufficiali controllate selettivamente, nessuna certificazione universale dei claim. Dossier e registro MD/CSV in reviews/audit-integrale-2026-10-02/. I precedenti report parziali sono storici. Nessuna correzione ai manoscritti, PDF o pipeline applicata da questo audit; preservate integrazioni di altri incarichi. Tutti i volumi richiedono interventi prima della pubblicazione. Ricettario digitale separato escluso; limiti e priorità espliciti.\n')
print('Dossier linked; historical reports marked; append-only event recorded')
