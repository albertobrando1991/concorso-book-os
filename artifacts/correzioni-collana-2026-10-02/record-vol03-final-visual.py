from pathlib import Path
import json
A=Path(__file__).parent
R=A/'vol03-proof'
v=json.loads((R/'verification.json').read_text(encoding='utf8'))
pages=[6,174,194,258,301,322,340,376,388,410,468,476,477,478,489,506,507,534,535,536,792,793]
contacts=[f'contact-{n:03}-{min(n+15,813):03}.png' for n in range(1,814,16)]
assert all((R/'vol-03-current-proof-audit'/p).exists() for p in contacts)
assert all((R/f'final-page-{p:03}.png').exists() for p in pages)
data={'volume':'VOL-03','date':'2026-10-03','pdfSha256':v['pdfSha256'],'pages':813,'allContactSheetsViewed':True,'contactSheets':contacts,'fullResolutionPagesViewed':pages,'method':'All 813 pages visually examined through 51 contact sheets, then 22 selected pages examined enlarged. Technical geometry and index checks cover every page.','limitations':['Contact sheets do not establish full-size reading of all body text.','No physical print proof, KDP upload or final publication signoff.','Digital-service and publisher-data dependencies remain open.']}
(R/'visual-review.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
p=A/'package-vol03.py';t=p.read_text(encoding='utf8')
fixes={'e31.5':'e 31.5','VOL08, VOL09, VOL05':'VOL-08, VOL-09, VOL-05','Gate14/15/16':'Gate 14/15/16','step24':'step 24','Step21':'Step 21','step21':'step 21','signoff24':'signoff 24',';22,23,24':'; 22, 23, 24','pagina1':'pagina 1','fino a828':'fino a 828','candidato{v[\'pages\']}p':'candidato di {v[\'pages\']} pagine','invece776':'invece 776','dei50master':'dei 50 master','indice194/194':'indice 194/194','formato6,69':'formato 6,69',',70 schemi':', 70 schemi',',194 rimandi':', 194 rimandi','le51 tavole':'le 51 tavole','uploadKDP':'upload KDP','i50master':'i 50 master','i113 allineamenti':'i 113 allineamenti',',126 etichette':', 126 etichette','e4 trasformazioni':'e 4 trasformazioni','su127.0.0.1':'su 127.0.0.1','le 57 correzioni sostanziali del 3 ottobre':'le correzioni testuali registrate il 3 ottobre','VOL02 il 3 ottobre':'VOL-02 il 3 ottobre'}
for old,new in fixes.items():t=t.replace(old,new)
p.write_text(t,encoding='utf8')
print(json.dumps({'contactsViewed':len(contacts),'enlargedPagesViewed':len(pages),'sha256':v['pdfSha256']}))
