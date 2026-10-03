from pathlib import Path
import json
A=Path(__file__).parent;W='wiki/reviews/correzioni-collana-2026-10-02';p=A/'registro-evidence-handoffs.json'
assert not p.exists(),'Do not overwrite coordinator handoffs'
d={'readyToMerge':False,'note':'Bozza: attesa evidenze finali del coordinatore per01/04 e handoff degli altri agenti. Nessuna approvazione alla pubblicazione.','volumes':{},'overrides':{}}
for n in range(1,13):
 v=f'VOL-{n:02}';ready=n in [2,3,8,9,10,11]
 d['volumes'][v]={'textReport':f'{W}/{v}.md','pdfReport':f'{W}/PDF-{v}.md','textVerified':ready,'pdfVerified':ready,'finalEvidenceApproved':ready,'productionStatus':'verificato-nella-copertura-dichiarata' if ready else 'attesa-handoff','note':'Dipendenze digitali/editoriali comuni aperte; non equivale a signoff.'}
d['volumes']['VOL-09']['chapterRoot']='wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
print(p)
