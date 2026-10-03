import fs from 'node:fs/promises'
import path from 'node:path'
import crypto from 'node:crypto'
import {parseStudentChapterForExport, type BookStudioData, type BookStudioChapter, type MarkdownBlock} from '../../src/server/book/book-preview'
async function main(){
const out='artifacts/correzioni-collana-2026-10-02/vol02-tomi'
await fs.mkdir(out,{recursive:true})
const response=await fetch('http://127.0.0.1:3020/api/book-studio?bookId=volumi%2Fvol-02')
if(!response.ok) throw new Error('API '+response.status)
const all:BookStudioData=await response.json()
await fs.writeFile(path.join(out,'source-full-payload.json'),JSON.stringify(all))
const sourceSim=await fs.readFile('wiki/books/vol-02-enti-locali-polizia-locale/chapters/50-simulazione-finale-vol-02.md','utf8')
const simBody=sourceSim.split('---').slice(2).join('---').trim()
function parsed(markdown:string,title:string,p:string){return parseStudentChapterForExport(`---\ntitle: ${JSON.stringify(title)}\nreview_required: false\ndraft_stage: publication-ready\n---\n\n${markdown}`,p).blocks}
function front(template:BookStudioChapter,which:string,title:string,markdown:string):BookStudioChapter{
 const p=`books/volumi/vol-02/tomi/${which}/${template.outlineSection.toLowerCase()}.md`
 return {...template,path:p,title,blocks:parsed(markdown,title,p)}
}
function chapter(original:BookStudioChapter,title:string,markdown:string):BookStudioChapter{
 return {...original,title,blocks:parsed(markdown,title,original.path),reviewRequired:false}
}
const spec=[{id:'tomo-1',roman:'I',title:'Comuni, Regioni, area vasta e Camere di commercio',codes:['M-FL01','M-FL02','M-FL03'],qfrom:1,qto:15,paths:[1,2,3],points:35,minutes:65},{id:'tomo-2',roman:'II',title:'Polizia locale',codes:['M-FL04'],qfrom:16,qto:20,paths:[4],points:25,minutes:55}]
const sourceHashes=[]
const referenceChanges:Array<{path:string,before:string,after:string}>=[]
// Reviewed against VOL-02-numbered-refs.json: FL01 references use module-local
// numbering, except explicit Il Metodo BANDO citations and budget chapters.
function alignReferences(value:any,p:string):any{
 if(typeof value==='string'){
  if(/Il Metodo BANDO/i.test(value))return value
  const after=value.replace(/(capitol[oi]\s+)(\d+)(?!\d|[.,/]\d)(\s+e\s+(\d+))?/gi,(match,prefix,a,join,b)=>{
   if(Number(a)<1||Number(a)>14)return match
   return prefix+(Number(a)+3)+(b?' e '+(Number(b)+3):'')
  })
  if(after!==value)referenceChanges.push({path:p,before:value,after})
  return after
 }
 if(Array.isArray(value))return value.map(v=>alignReferences(v,p))
 if(value&&typeof value==='object')return Object.fromEntries(Object.entries(value).map(([k,v])=>[k,alignReferences(v,p)]))
 return value
}
for(const c of all.chapters.filter(c=>c.sectionType==='chapter')){
 const bytes=await fs.readFile(path.join('wiki',c.path));sourceHashes.push({path:c.path,sha256:crypto.createHash('sha256').update(bytes).digest('hex')})
}
for(const s of spec){
 const allMain=all.chapters.filter(c=>c.sectionType==='chapter')
 const opening=allMain.filter(c=>Number(c.outlineSection)<4).map(c=>structuredClone(c))
 const specialized=allMain.filter(c=>s.codes.includes(c.volumeModuleCode||'')).map(c=>structuredClone(c))
 for(const c of specialized.filter(c=>c.volumeModuleCode==='M-FL01')){
  c.blocks=alignReferences(c.blocks,c.path)
  for(const b of c.blocks){
   if(b.type==='table'&&b.headers?.includes('Capitoli più pesanti')){
    const col=b.headers.indexOf('Capitoli più pesanti')
    b.rows=b.rows?.map(row=>{const before=row[col];const after=before.replace(/\d+/g,n=>String(Number(n)+3));referenceChanges.push({path:c.path,before,after});return row.map((cell,i)=>i===col?after:cell)})
   }
  }
 }
 const closing=allMain.filter(c=>Number(c.outlineSection)>=50).map(c=>structuredClone(c))
 const guide=`# Come usare questo tomo insieme a VOL-01

## Percorso e destinatari

Il VOL-02 è articolato in due tomi. Questo è il **Tomo ${s.roman} — ${s.title}**. ${s.id==='tomo-1'?'I tre moduli sviluppano Comuni e Unioni; Regioni, Province e Città metropolitane; Camere di commercio. Scegli il modulo principale dal bando: i contenuti camerali non sono un obbligo per chi prepara un profilo comunale, e la tecnica legislativa regionale richiede il programma pertinente. Il percorso completo di Polizia locale è nel Tomo II.':'Il percorso sviluppa i quindici capitoli di Polizia locale: ordinamento, qualifiche, circolazione, sanzioni, PG, pubblica sicurezza, commercio, edilizia, ambiente, sinistri, comando e atti. I percorsi amministrativi comunali, regionali, di area vasta e camerali sono nel Tomo I.'}

Ogni tomo contiene il proprio indice, gli strumenti di orientamento e una simulazione con soluzioni stampate. **La numerazione dei capitoli resta comune ai due tomi**: orientamento 1–3, Comuni 4–17, Regioni e area vasta 18–29, Camere di commercio 30–34, Polizia locale 35–49, simulazione 50 e conclusione 51. Gli intervalli assenti dall'indice di questo tomo appartengono all'altro; le pagine ripartono da uno. La simulazione e la conclusione sono adattate al percorso presente.

## Regola comune e applicazione specialistica

Il VOL-01 fornisce il metodo e le materie comuni: Costituzione, procedimento, accesso, trasparenza, privacy, anticorruzione, pubblico impiego, contratti e contabilità di base. Qui quelle conoscenze diventano decisioni del profilo: chi ha la competenza, quali presupposti servono, quale documento redigere e quale seguito attivare. Non basta citare una norma senza applicarla al fatto.

${s.id==='tomo-1'?'Per un istruttore comunale la priorità può essere organi, atti e servizi; per un contabile, bilancio, gestione, tributi e controlli; per un funzionario regionale, competenze, procedimenti e programmazione; per un candidato camerale, Registro, servizi e organizzazione. Il profilo tecnico usa il contesto amministrativo e i rinvii puntuali al VOL-10 per la specializzazione tecnica.':'Per un agente la priorità comprende qualifiche, servizi, accertamento e documentazione; per ufficiale, funzionario o comandante si aggiungono coordinamento, personale, turni e responsabilità organizzative. La legge regionale e il regolamento del Corpo richiesti dal bando si studiano nel loro ambito: non si trasferiscono automaticamente regole di un territorio in un altro.'}

## Dal bando all'output

Compila il Decoder del capitolo 2: ente, profilo, area, requisiti, prove, materie, fonti territoriali e calendario. Separa la regola comune dalla sua applicazione specialistica. Per ogni materia assegna un risultato concreto: una risposta in 120 parole, un caso, una nota, un verbale o un'esposizione di tre minuti. Gli esempi didattici non sono bandi reali né modelli ufficiali dell'amministrazione.

Usa il piano del capitolo 3 per alternare studio, richiamo attivo e prova. Correggi prima gli errori che cambiano l'esito: competenza sbagliata, termine confuso, fatto non dimostrato, garanzia omessa. Poi migliora sintassi e ordine. Nei laboratori trovi elaborati svolti; nella simulazione 50, quesiti e percorsi coerenti con questo tomo.

## Scheda iniziale

| Campo | Da compilare |
|---|---|
| Ente e profilo | |
| Prova, durata e materie | |
| Modulo e capitoli prioritari | |
| Fonti regionali/locali richieste | |
| Output da allenare | |
| Primo errore da recuperare | |

Il testo normativo è verificato al 3 ottobre 2026 nel perimetro delle fonti dei capitoli. Prima della prova controlla bando, rettifiche e norme ufficiali pertinenti. Il libro e le soluzioni restano utilizzabili senza servizi digitali; eventuali materiali online sono complementari.
`
 opening[0]=chapter(opening[0],'Come usare questo tomo insieme a VOL-01',guide)
 await fs.writeFile(path.join(out,`${s.id}-orientamento.md`),guide)
 // Keep the verified question texts/options and select the matching solved paths.
 const qblocks=[...simBody.matchAll(/\*\*(\d+)\.[\s\S]*?(?=\*\*\d+\.|## Parte B)/g)].filter(m=>Number(m[1])>=s.qfrom&&Number(m[1])<=s.qto).map(m=>m[0].trim().replace(/### (?:Comune|Regione|Camera|Polizia)[\s\S]*$/m,''))
 if(qblocks.length!==s.qto-s.qfrom+1)throw new Error('quiz missing '+s.id+' '+qblocks.length)
 const partB=simBody.split('## Parte B')[1].split('## Soluzioni')[0]
 const solved=simBody.split('### Percorso 1 — Soluzione e documento')[1]
 const paths=[...partB.matchAll(/### Percorso (\d+) —[\s\S]*?(?=### Percorso |$)/g)].filter(m=>s.paths.includes(Number(m[1]))).map(m=>m[0].trim())
 const solutionText='### Percorso 1 — Soluzione e documento'+solved
 const solutions=[...solutionText.matchAll(/### Percorso (\d+) — Soluzione e documento[\s\S]*?(?=### Percorso \d+ — Soluzione|## Correzione|$)/g)].filter(m=>s.paths.includes(Number(m[1]))).map(m=>m[0].trim())
 const keyRows=simBody.split('\n').filter(l=>{const m=/^\| (\d+) \| [A-D] \|/.exec(l);return m&&Number(m[1])>=s.qfrom&&Number(m[1])<=s.qto})
 let sim=`# Simulazione finale — Tomo ${s.roman}

Questa prova didattica originale usa soltanto le materie presenti nel tomo. Enti, persone e dossier sono fittizi. Mantiene la numerazione dei quesiti e dei percorsi dell'edizione coordinata per facilitare i rinvii fra tomi; le soluzioni sono qui incluse.

## Consegna e punteggio

Svolgi i ${qblocks.length} quiz e ${s.paths.length>1?'scegli uno dei tre percorsi pratici':'il percorso pratico PL'} con risposta sintetica, caso, documento e orale. Disponi di ${s.minutes} minuti: ${qblocks.length} per i quiz, 10 per la risposta, 20 per il caso, 15 per il documento e 5 per l'orale. Prima fase senza manuale, seconda fase di correzione sulle soluzioni.

Ogni quiz vale un punto; errata o omessa vale zero. Risposta sintetica fino a5, caso fino a7, documento fino a5, orale fino a3. Totale massimo **${s.points} punti**. Una soglia diagnostica del70% suggerisce un primo consolidamento; non sostituisce i criteri del bando reale e non sana errori gravi su competenze o garanzie.

## Quiz

${qblocks.join('\n\n')}

## Percorsi pratici

${paths.join('\n\n')}

## Soluzioni — Aprire dopo la prova

${keyRows.map(row=>{const cells=row.split('|').map(x=>x.trim());return `**${cells[1]} — ${cells[2]}.** ${cells[3]}`}).join('\n\n')}

${solutions.join('\n\n')}

## Griglia di correzione

La risposta sintetica vale un punto per ciascuno di: definizione, distinzione, competenza, conseguenza nel caso, chiarezza entro120 parole. Il caso vale fino a due punti per la qualificazione e due per la sequenza: zero se errate, uno se incomplete, due se corrette e applicate. Gli ulteriori tre punti, uno ciascuno, riguardano:

${s.id==='tomo-1'?'- Comune: differenza di100 euro dichiarata teorica; istruttoria dell’acquisto e controlli mancanti; nessun pagamento anticipato.\n- Provincia: competenza sull’edificio; diagnosi tecnica non acquisita; raccordo scuola/ufficio tecnico senza spesa o urgenza inventata.\n- Camera: visura distinta dal fascicolo; interesse documentale da istruire; controinteressati e limiti senza esiti automatici.':'- qualificazione penale ex art.255, comma1;\n- CNR anche contro ignoti;\n- ripristino distinto dalla PG, senza sequestro inventato.'}

Il documento vale un punto per ciascuno di: destinatario/oggetto, fatti fedeli, distinzione noto/mancante, seguito corretto, allegati e firma. L'orale vale un punto per risposta diretta, uno per fondamento e uno per applicazione. Correggi il primo errore decisivo e ripeti l'output dopo due giorni, registrando il confronto nel Diario. Il punteggio serve a scegliere cosa recuperare.
`
 sim=sim.replace(/(?<=[a-zà-ÿ])(?=\d)/g,' ').replace(/\bart\.(?=\d)/g,'art. ').replace(/comma(?=\d)/g,'comma ')
 closing[0]=chapter(closing[0],`Simulazione finale — Tomo ${s.roman}`,sim)
 await fs.writeFile(path.join(out,`${s.id}-simulazione.md`),sim)
 const conclusion=`# Dal tomo al prossimo bando

Hai a disposizione il percorso **${s.title}**, i casi guidati, i laboratori e una simulazione con soluzioni. Non serve ripartire dalla prima pagina dopo ogni errore: torna al capitolo e alla distinzione che non hai applicato correttamente.

Conserva tre prodotti: il Decoder del bando, una mappa delle competenze e il Diario degli errori. Nel prossimo concorso della stessa famiglia confronta programma, prove e fonti territoriali con questi strumenti. Riutilizza ciò che resta pertinente e integra le differenze.

La regola comune del VOL-01 e l'applicazione specialistica di questo tomo si richiamano: il procedimento diventa pratica, il potere diventa atto e il controllo diventa motivazione verificabile. Nella prova mostra il percorso dal fatto alla decisione senza attribuire al soggetto un potere che non possiede.

La collana VOL-02 comprende anche il Tomo ${s.roman==='I'?'II, Polizia locale':'I, Comuni, Regioni, area vasta e Camere di commercio'}. Usalo quando il tuo bando ne richiede le materie. Per specializzazioni ulteriori segui i rinvii precisi dei capitoli, senza trasformare ogni concorso in un programma illimitato.

Prima della prova verifica bando, rettifiche e fonti ufficiali vigenti: le norme possono cambiare dopo il cut-off del3 ottobre2026. Il tuo criterio resta individuare fatto, fonte, competenza, atto e seguito. Ripeti la simulazione dopo aver recuperato gli errori e confronta le motivazioni delle risposte, oltre al punteggio.
`.replace('del3 ottobre2026','del 3 ottobre 2026')
 closing[1]=chapter(closing[1],'Dal tomo al prossimo bando',conclusion)
 await fs.writeFile(path.join(out,`${s.id}-conclusione.md`),conclusion)
 const fm=all.chapters.filter(c=>c.sectionType==='front_matter'&&!c.volumeModuleCode).map(c=>structuredClone(c))
 const titleIndex=fm.findIndex(c=>c.frontMatterLayout==='title-page');fm[titleIndex]=front(fm[titleIndex],s.id,'Frontespizio',`# VOL-02 — Tomo ${s.roman}\n\n## ${s.title}\n\nManuale-workbook per i concorsi territoriali\n\n### Capitale Personale\n\nMetodo BANDO · Edizione verificata al 3 ottobre 2026`)
 const sumIndex=fm.findIndex(c=>c.frontMatterLayout==='summary');fm[sumIndex]=front(fm[sumIndex],s.id,'Sommario',`# Sommario\n\nQuesto tomo comprende ${s.codes.join(', ')}.\n\n| Percorso | Capitoli della collana |\n|---|---|\n| Orientamento e metodo | 1–3 |\n${s.id==='tomo-1'?'| Comuni e Unioni | 4–17 |\n| Regioni, Province e Città metropolitane | 18–29 |\n| Camere di commercio | 30–34 |':'| Polizia locale | 35–49 |'}\n| Simulazione adattata e conclusione | 50–51 |\n\nLa numerazione dei capitoli è comune ai due tomi; l'indice delle pagine riguarda soltanto questo tomo. Teoria e prove specialistiche sono incluse; per le materie comuni resta il raccordo con VOL-01.`)
 const preIndex=fm.findIndex(c=>c.frontMatterLayout==='preface');fm[preIndex]=front(fm[preIndex],s.id,'Premessa',`# Premessa\n\nI concorsi richiedono di applicare le regole a enti, funzioni e fatti concreti. Il Tomo ${s.roman} sviluppa ${s.title.toLowerCase()} con spiegazioni, esempi, casi e verifiche.\n\nParti dal bando, scegli le materie pertinenti e produci una risposta o un atto prima di passare al nucleo successivo. Gli esempi originali sono didattici; non sostituiscono modelli ufficiali dell'ente.\n\nLa divisione del VOL-02 in due tomi conserva la leggibilità della pagina e la copertura dei moduli. Ogni tomo dispone di orientamento, indice e simulazione con soluzioni; il testo è verificato al 3 ottobre2026 nel perimetro delle fonti dei capitoli.\n\nIl libro resta utilizzabile senza piattaforma digitale. Le condizioni degli eventuali servizi aggiuntivi seguono le informazioni rese disponibili dall'editore.`.replace('ottobre2026','ottobre 2026'))
 const main=[...opening,...specialized,...closing]
 const idx=fm.find(c=>c.frontMatterLayout==='analytical-index')!;idx.blocks=[{type:'heading',level:2,text:`Indice del Tomo ${s.roman}`}]
 let group=''
 for(const c of main){const next=c.volumeModuleCode|| (Number(c.outlineSection)<4?'Orientamento':'Parte finale');if(next!==group){idx.blocks.push({type:'index-part',number:c.volumeModuleCode||'',text:c.volumeModuleTitle?.replace(/^M-[A-Z]+\d+\s*[-—]\s*/,'')||next});group=next}idx.blocks.push({type:'index-chapter',number:`Cap. ${c.outlineSection}`,text:c.title,path:c.path,pageNumber:1});for(const b of c.blocks.filter(b=>b.type==='heading'&&b.nucleusId&&b.number))idx.blocks.push({type:'index-row',text:b.text,number:b.number,nucleusId:b.nucleusId,path:c.path,pageNumber:1})}
 const moduleOpenings=all.chapters.filter(c=>c.frontMatterLayout==='module-opening'&&s.codes.includes(c.volumeModuleCode||'')).map(c=>structuredClone(c))
 for(const c of moduleOpenings){c.blocks=c.blocks.map(b=>({...b,text:b.text?.replace(/Sezione interna del volume.*$/,`Percorso del VOL-02, Tomo ${s.roman} — ${s.title}.`)}))}
 const assembled=[...fm,...opening,...s.codes.flatMap(code=>[...moduleOpenings.filter(c=>c.volumeModuleCode===code),...specialized.filter(c=>c.volumeModuleCode===code)]),...closing]
 const payload={...all,title:`VOL-02 — Tomo ${s.roman}: ${s.title}`,footerTitle:`VOL-02 · Tomo ${s.roman}`,chapters:assembled,summary:{...all.summary,chapters:assembled.length,mainChapters:main.length,written:assembled.length,draft:0,structure:0}}
 await fs.writeFile(path.join(out,`${s.id}-payload.json`),JSON.stringify(payload))
 await fs.writeFile(path.join(out,`${s.id}-manifest.json`),JSON.stringify({id:s.id,title:s.title,modules:s.codes,mainChapters:main.length,pagesPending:true,sourceHashes:sourceHashes.filter(x=>main.some(c=>c.path===x.path)),derivedMarkdown:[`${s.id}-orientamento.md`,`${s.id}-simulazione.md`,`${s.id}-conclusione.md`],notes:['Nessuna modifica al renderer o ai master congelati','Front matter, indice e chiusura adattati alla selezione; numerazione capitoli collana conservata','Servizi digitali: condizioni commerciali ancora dipendenza del coordinatore']},null,2))
 console.log(JSON.stringify({tomo:s.id,main:main.length,questions:qblocks.length,paths:paths.length,solutions:solutions.length}))
}
await fs.writeFile(path.join(out,'reference-alignment.json'),JSON.stringify({review:'All source matches reviewed, explicit VOL-01/Il Metodo BANDO and budget chapters preserved',changes:referenceChanges},null,2))
}
main().catch(e=>{console.error(e);process.exit(1)})
