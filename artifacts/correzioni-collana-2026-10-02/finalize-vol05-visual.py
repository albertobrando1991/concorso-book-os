from pathlib import Path
import json,shutil,hashlib
A=Path(__file__).parent;R=A/'vol05-proof';W=Path('wiki/reviews/pipeline/VOL-05')
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf8')
v=load(R/'verification.json');prior=load(R/'visual-before-balance.json');cmp=load(R/'balance-comparison.json')
assert cmp['currentPDFSHA256']==v['pdfSha256'] and len(cmp['pixelIdenticalPagesAt72DPI'])==232
for n in cmp['changedPages']:shutil.copy2(R/'details'/f'balanced-{n:03}.png',R/'details'/f'page-{n:03}.png')
visual={'pdfSha256':v['pdfSha256'],'pages':239,'allFinalPagesVisuallyCovered':True,'allContactSheetsViewed':False,'baseReview':{'pdfSha256':prior['pdfSha256'],'allContactSheetsViewed':True,'contactSheets':prior['contactSheets'],'detailPages':prior['fullResolutionPagesViewed']},'finalDeltaPagesViewed':cmp['changedPages'],'pixelIdenticalPagesAt72DPI':cmp['pixelIdenticalPagesAt72DPI'],'fullResolutionPagesViewed':sorted(set(prior['fullResolutionPagesViewed']+cmp['changedPages'])),'method':'15 contact sheets of the prior candidate, 50 detailed pages; final delta checked at full page for all 7 changed pages; 232 remaining pages pixel-identical at 72 dpi. Final contacts regenerated and included, not claimed separately reread.','observations':['Page 35 reflowed; nucleus 2.4 now shares page with preceding content.','Closing pages 39 and 220 have white space after evaluation/references or case conclusion.','Tables continue with repeated headers; no rows omitted.','Native schemes readable at 9.5 pt.','Front matter digital promise and publisher data remain unverified.'],'limitations':['No full-size rereading of all body text in PDF.','No physical print, KDP upload or final signoff.']}
save(R/'visual-review.json',visual)
rows=[]
for p in range(1,240):
 issue='Nessuna anomalia geometrica rilevata';severity='—';correction='Nessuna';status='Contatto e misure; dettaglio ove elencato'
 if p in [1,2,3,4]:issue='Front matter commerciale comune';severity='grave';correction='Verificare promessa digitale, dati editoriali e testo di collana';status='Aperto; coordinamento comune'
 if p==35:issue='Bianco eccessivo per titoli consecutivi';severity='medio';correction='Sottotitolo breve incorporato nel capoverso, senza perdita di testo';status='Risolto; dettaglio finale'
 if p in [39,220]:issue='Bianco finale di capitolo';severity='lieve';correction='Chiusura conservata, senza comprimere caratteri o contenuti';status='Valutato; non pagina vuota'
 if p in [23,39,53,67,81,96,113,129,144,159,173,190,204,219]:
  issue+='; link esterni';correction+='; sintassi Markdown sostituita da nome e dominio nella proiezione';status+='; riferimenti completi nel manifest'
 rows.append({'page':p,'issue':issue,'element':'Impaginato','severity':severity,'correction':correction,'status':status})
save(R/'page-review.json',rows)
table='| Pagina | Tipo di problema | Elemento | Gravità | Correzione | Esito |\n|---|---|---|---|---|---|\n'+''.join('| '+' | '.join(str(r[k]) for k in ['page','issue','element','severity','correction','status'])+' |\n' for r in rows)
text='# VOL-05 — Audit pagina per pagina, 3 ottobre 2026\n\n239 pagine, SHA-256 '+v['pdfSha256']+'. Copertura: tutte le 15 tavole della prova precedente e 50 dettagli; dopo l’ultimo riflusso, 232 pagine sono identiche pixel per pixel a 72 dpi e tutte le 7 cambiate sono state riesaminate ingrandite. In totale 53 pagine distinte hanno riscontro di dettaglio corrente. È una verifica dell’impaginato, non una nuova lettura integrale del testo minuto.\n\nIndice 90/90, schemi 75/75, font incorporati, zero overflow DOM, zero testo fuori pagina, zero asset mancanti e zero HTML letterale. Il PDF mantiene i dati editoriali comuni da verificare: questo impedisce il signoff del volume, non viene nascosto dal controllo geometrico.\n\n'+table+'\nGate page-fill non automatizzato: la verifica manuale è documentata; nessun verde automatico simulato. Non chiudere 21–24 prima di risolvere le dipendenze comuni.\n'
(W/'20-vol-05.md').write_text(text,encoding='utf8')
p=W/'19-vol-05.md';s=p.read_text(encoding='utf8');s=s.replace('Restano bianchi ampi a pagina 35 e nella chiusura 220, senza perdita o titolo isolato.','Riequilibrata pagina 35; restano spazi finali nelle chiusure 39 e 220, senza perdita o titolo isolato.');import re;s=re.sub(r'PDF SHA-256: [0-9a-f]{64}', 'PDF SHA-256: '+v['pdfSha256'],s);p.write_text(s,encoding='utf8')
p=W/'18-moduli-m-fc05-authority-indipendenti.md';s=p.read_text(encoding='utf8');s=re.sub(r'SHA-256 [0-9a-f]{64}', 'SHA-256 '+v['pdfSha256'],s);s+='\nUltimo delta di riflusso: 232 pagine pixel-identiche, sette riesaminate a dettaglio. La copertura finale è documentata in visual-review.json; 53 pagine distinte di dettaglio.\n';p.write_text(s,encoding='utf8')
print('Visual final:',len(visual['fullResolutionPagesViewed']),'details, 239 pages covered.')
