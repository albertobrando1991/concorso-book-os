from pathlib import Path
import json,hashlib,re
A=Path(__file__).parent
def read(name): return json.loads((A/name).read_text(encoding='utf8'))
def save(name,data): (A/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
pdf=A/'vol-01-native-release-20261003-proof.pdf'; sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
m=read('VOL-01-native-release-pdf-map.json'); comp=read('VOL-01-native-release-render-comparison.json'); ix={r['page']:r for r in comp['pages']}
direct=[378,380,404,405,406,408,409,410,412,415,489,490,553,554]
rows=[]
for p in m['selectedPages']:
 old=ix[p]['matchesReviewedPage']; assert old or p in direct,p
 rows.append({'page':p,'visualReviewed':True,'method':'direct-view' if p in direct else 'exact-render-match','previousReviewedPage':old})
for r in m['native']+m['protected']: r['visualReview']=True
save('VOL-01-native-release-pdf-map.json',m)
save('VOL-01-native-release-visual-ledger.json',{'pdf':str(pdf),'sha256':sha,'pages':687,'selectedPages':rows,'extraDirectPages':direct,'previousReview':'VOL-01-native-final-pdf-visual-ledger.json','comparison':'VOL-01-native-release-render-comparison.json','limitations':'178 pagine mirate coprono tutti gli apparati; 169 risultano identiche alle pagine già esaminate, escluse le sole fasce dei piè di pagina; 9 sono state viste nuovamente. Ulteriori 5 pagine sono state viste direttamente. Non è una rilettura integrale delle 687 pagine.'})
old=read('VOL-01-native-final-pdf-visual-ledger.json'); old[27]['review']='Apparati leggibili. Rilevata separazione fra esempio orale e risposta a pagina 404; corretta e rivista nella prova release, pagina 405.'; save('VOL-01-native-final-pdf-visual-ledger.json',old)
mp={r['id']:r for r in m['native']}; ledger=read('VOL-01-native-ledger.json')
for r in ledger:
 r.update(pdfReview='complete',pdfPages=mp[r['id']]['pages'],proofSHA256=sha,proof=str(pdf),currentChapterSHA256=hashlib.sha256(Path(r['chapter']).read_bytes()).hexdigest(),pdfReviewEvidence='VOL-01-native-release-visual-ledger.json')
save('VOL-01-native-ledger.json',ledger)
hist=read('VOL-01-native-layout-findings.json'); resolved=[]
for r in hist['findings']:
 resolved.append({'ids':r['ids'],'previousPage':r['page'],'currentPages':mp[r['ids'][0]]['pages'],'status':'verified-resolved'})
save('VOL-01-native-layout-resolutions.json',{'pdf':str(pdf),'sha256':sha,'schemaFindings':resolved,'otherRaccordi':[{'previousPage':a,'currentPage':b,'status':'verified-resolved'} for a,b in [(394,405),(462,475),(476,489),(492,506),(537,553)]],'extraCorrections':{'worksheet19':471,'percentages20':490,'uppercaseQuestions':[468,547]}})
freeze=read('M-PA01-freeze.json'); f=freeze['controlledNativePrintCorrections']; f.update(description='133 schemi nativi verificati semanticamente e nella prova release; 19 immagini protette invariate. Tutti i 25 raccordi segnalati risolti. Revisione degli apparati conclusa, nessuna pubblicabilità complessiva dichiarata.',proof=str(pdf),proofSHA256=sha,visualEvidence='VOL-01-native-release-visual-ledger.json');save('M-PA01-freeze.json',freeze)
p=Path('wiki/reviews/correzioni-collana-2026-10-02/VOL-01-schemi-nativi.md'); s=p.read_text(encoding='utf8')
s=re.sub(r'Sono state esaminate 194 pagine.*?motore di impaginazione\.', 'La prova release conta 687 pagine. La verifica copre tutti i 133 schemi e le 19 figure: 177 pagine della prova intermedia sono state esaminate visivamente; nella release 169 pagine sono identiche a quelle già viste e nove pagine cambiate sono state riesaminate, per 178 pagine mirate. Altre cinque pagine sono state viste per i raccordi. Tutti i 20 schemi con apertura separata e i cinque raccordi aggiuntivi sono corretti.',s)
lines=[]
for line in s.splitlines():
 match=re.match(r'\| (F\d{3}) \|',line)
 if match:
  r=mp[match.group(1)]; cells=line.split('|'); cells[-3]=' PDF release 687 pagine, pp. '+', '.join(map(str,r['pages']))+'; evidenza nel registro visivo. ';cells[-2]=' Applicato e verificato. ';line='|'.join(cells)
 lines.append(line)
s='\n'.join(lines)+'\n'
s=s[:s.index('## 8. Priorità degli interventi')]+'''## 8. Verifica dei raccordi

Tutti i 20 raccordi degli schemi e i cinque raccordi aggiuntivi sono risolti; il dettaglio conserva posizione precedente e posizione attuale in `VOL-01-native-layout-resolutions.json`. Titolo e primo contenuto sono sulla stessa pagina in 133 schemi su 133. L’esempio orale è unito alla risposta a pagina 405; la mappa modello a pagina 475; la distribuzione del tempo a pagina 489; la matrice di decisione a pagina 506; la Checklist 1 a pagina 553. Il mini-esercizio del capitolo 19 è completo a pagina 471. Il rinvio alle percentuali è corretto a pagina 490; le due domande iniziano con «Perché» alle pagine 468 e 547.

Il renderer mantiene insieme titolo, brevi introduzioni e primo apparato, quando il gruppo entra nella pagina. I gruppi troppo alti restano divisibili. Passano 127 test pertinenti e il typecheck. La prova conta 687 pagine sia nel DOM sia nel PDF, senza overflow o testo fuori pagina; corpo circa 11 pt, tabelle circa 9,5 pt. Le prove precedenti e i rilievi storici sono conservati.

## 9. Giudizio di pubblicabilità

La revisione degli apparati è conclusa: 133 sostituzioni applicate e verificate, 19 immagini protette invariate. Questo esito riguarda lo step 18 e non sostituisce revisione complessiva, preflight, preparazione del pacchetto e conferma finale. Non si dichiara la pubblicabilità del volume e non si esegue il gate 24.

## 10. Limiti

La revisione semantica riguarda gli apparati e il loro contesto. Non è una nuova certificazione normativa dell’intero volume né una rilettura integrale delle 687 pagine. La copertura della release è documentata in `VOL-01-native-release-visual-ledger.json`: 169 pagine con rendering esattamente uguale alle pagine già viste, escluse le fasce inferiori dei piè di pagina, nove pagine cambiate viste direttamente e cinque ulteriori dettagli. La mappa include tutte le 133 sostituzioni e tutte le 19 immagini. Il confronto dei pixel è una verifica di equivalenza della pagina, non una modifica degli asset. La prova a schermo non sostituisce una prova fisica.
'''
p.write_text(s,encoding='utf8')
p=Path('wiki/reviews/pipeline/VOL-01/18-il-metodo-bando.md'); s=p.read_text(encoding='utf8'); s+='''
## Chiusura della revisione degli apparati — 3 ottobre 2026

La prova `artifacts/correzioni-collana-2026-10-02/vol-01-native-release-20261003-proof.pdf` conta 687 pagine, con DOM e PDF coerenti, zero overflow e zero testo fuori pagina. Tutti i 133 schemi sono leggibili e hanno titolo e primo contenuto sulla stessa pagina; le 19 immagini protette conservano hash e riferimenti. Risolti i 20 raccordi segnalati e i cinque aggiuntivi. Verificati anche mini-esercizio, rinvio alle percentuali e maiuscole delle domande.

Il registro [Schemi nativi](../../correzioni-collana-2026-10-02/VOL-01-schemi-nativi.md) contiene le dieci sezioni della revisione e le 133 righe asset → problema → correzione → verifica → esito. La copertura visiva della release comprende 178 pagine degli apparati: 169 equivalenti per confronto esatto del rendering a pagine già viste e nove riesaminate direttamente, oltre a cinque pagine aggiuntive. Le 177 pagine della prova intermedia sono state viste in 45 tavole. Il registro distingue i due metodi senza dichiarare una lettura integrale del PDF. Le evidenze sono `VOL-01-native-release-visual-ledger.json`, `VOL-01-native-layout-resolutions.json`, `VOL-01-native-release-chain-audit.json` e `VOL-01-native-verifica.json`.

La seconda passata conferma uniformità e precisione degli apparati. I 127 test del renderer pertinenti e il typecheck passano. Revisione degli apparati conclusa; resta il percorso successivo della pipeline, senza gate 24 e senza pubblicabilità complessiva dichiarata.
''';p.write_text(s,encoding='utf8')
p=A/'renderer-chain-checkpoint.md';s=p.read_text(encoding='utf8').replace('126 test','127 test').replace('sette test','otto test');s=s[:s.index('La prova `')]+'''La prova release `vol-01-native-release-20261003-proof.pdf` conta 687 pagine sia nel DOM sia nel PDF: zero overflow e testo fuori pagina. Tutti i 133 schemi iniziano con titolo e primo contenuto nella stessa pagina; i 20 raccordi segnalati e i cinque aggiuntivi sono risolti. Il registro visivo distingue confronto esatto del rendering e ispezione diretta. Le prove precedenti restano immutate. Nessun gate 24 eseguito.
''';p.write_text(s,encoding='utf8')
print(json.dumps({'sha256':sha,'schemas':len(ledger),'releaseApparatusPages':len(rows),'identical':sum(r['method']=='exact-render-match' for r in rows)}))
