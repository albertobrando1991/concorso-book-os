import fs from 'node:fs';
const base='wiki/reviews/audit-integrale-2026-10-02/';
const observations:any={
'VOL-08':[
'Orientamento utile; il rapporto con i diversi profili va sostenuto da percorsi e prove più differenziati.',
'Le nozioni di base sono coerenti, ma diversi concetti specialistici sono solo accennati e richiedono esempi applicati.',
'Pseudocodice ed esercizi elementari risultano coerenti. Ampliare le spiegazioni degli algoritmi e delle strutture richiamate dal programma.',
'Query e casi SQL controllati; completare le distinzioni su transazioni, anomalie e livelli di isolamento.',
'I calcoli di subnetting verificati sono corretti. Precisare le versioni dei protocolli e sviluppare i livelli e i servizi richiesti dal profilo.',
'Il metodo di analisi è utile; occorrono requisiti, test e artefatti compilati che dimostrino l’applicazione.',
'Il quadro del cloud pubblico deve includere classificazione e qualificazione dei servizi, con fonti e date identificabili.',
'Approccio al rischio coerente; rendere più concrete le tecniche, le metriche e le verifiche dei controlli.',
'Ampliare obblighi NIS2, gestione degli incidenti e distinzione fra identità, autenticazione e autorizzazione con casi operativi.',
'Correggere la definizione dei dati aperti e la rimappatura di BANDO; rafforzare qualità, governance e interoperabilità.',
'Completare categorie e ruoli dell’AI Act, disciplina italiana della PA e calendario applicativo; aggiungere formule e casi per le metriche.',
'Integrare valutazione comparativa e riuso del software, obblighi di acquisto ICT e misure del servizio; correggere la rappresentazione del ruolo del DPO.',
'I quiz verificati risultano coerenti. Il laboratorio richiede soluzioni complete e prove SQL, algoritmiche, di rete e metriche, oltre alle scalette di metodo.'
],
'VOL-09':[
'La lettura dei profili è utile, ma la tabella del ciclo è spezzata e la distinzione fra fasi contabili richiede correzione.',
'Completare qualificazione, RUP, responsabili di fase e DEC; la matrice delle responsabilità deve dichiarare il modello organizzativo assunto.',
'Sviluppare programmazione, calcolo del valore e lotti con regole e dati sufficienti a risolvere un caso.',
'Integrare requisiti, criteri di aggiudicazione e soccorso istruttorio; fornire documenti di gara effettivamente compilati.',
'Il capitolo deve insegnare le soglie e le procedure vigenti, con rotazione, eccezioni e controlli; la sola cautela sui dati mobili non prepara la prova.',
'Completare il flusso digitale e correggere il titolo inserito nel quiz. Collegare piattaforme e banche dati agli adempimenti e ai tempi.',
'Correggere l’ambito MePA Lavori e sviluppare obblighi di acquisto, accordi quadro, SDAPA e ASP.',
'La parte sull’esecuzione richiede regole operative su modifiche, subappalto, revisione prezzi, anticipazione e verifica finale.',
'Ampliare accesso digitale, standstill e tutela; ricomporre titoli, tabelle e quiz interrotti.',
'Integrare struttura giuridica e calendario del PNRR, insieme al ciclo operativo di monitoraggio in ReGiS.',
'Sviluppare tracciabilità, ammissibilità della spesa, conflitto di interessi e controlli con casi e documentazione concreta.',
'Precisare DNSH e obblighi CAM, applicando un criterio reale; il titolo di sezione non deve dividere le opzioni del quiz.',
'Rimuovere i codici provvisori e fornire WBS, cronoprogramma e calcoli risolti; distinguere dipendenze obbligatorie da scelte organizzative.',
'Il laboratorio deve contenere atti e soluzioni verificabili, oltre alle indicazioni di metodo; riallineare diario e piani di studio promessi dalla matrice.'
]};
function clean(t:string){
 return t.split(/(`[^`]*`|https?:\/\/[^\s)]+|\]\([^)]*\))/g).map((s,i)=>{
  if(i%2)return s;
  return s.replace(/([a-zàèéìòù])([A-Z]{2,})/g,'$1 $2').replace(/([a-zàèéìòù])(?=\d)/g,'$1 ').replace(/(\d)(?=[a-zàèéìòù])/g,'$1 ').replace(/(UE|CCNL|CDU|CAD|VOL|FC)(?=\d)/g,'$1 ').replace(/\b(artt?\.|cap\.|r\.|d\.lgs\.)(?=\d)/gi,'$1 ').replace(/([a-zàèéìòù]),(?=\S)/g,'$1, ').replace(/([a-zàèéìòù0-9])\(/g,'$1 (').replace(/\)(?=[A-Za-zàèéìòù])/g,') ').replace(/letterab\b/g,'lettera b').replace(/m-fc 03-fonti/g,'m-fc03-fonti').replace(/soprattuttoFC 03/g,'soprattutto FC03').replace(/firma definitiva delCCNL/g,'firma definitiva del CCNL').replace(/intraUE/g,'intra-UE').replace(/legge90/g,'legge 90').replace(/ISO27001/g,'ISO 27001').replace(/allegatoIII/g,'allegato III').replace(/III2dicembre/g,'III, 2 dicembre');
 }).join('');
}
for(const vol of ['VOL-03','VOL-08','VOL-09','VOL-11']){
 const p=base+vol+'.md';let t=fs.readFileSync(p,'utf8');
 if(observations[vol]){
  const l=JSON.parse(fs.readFileSync('artifacts/review-integrale-2026-10-02/'+vol+'-ledger.json','utf8'));
  const block='## 4. Osservazioni per capitolo\n\nTutti i capitoli sono stati letti integralmente, con controllo di quiz, commenti e casi. Le note analitiche di lettura restano nel ledger.\n\n'+observations[vol].map((x:string,i:number)=>`- **Capitolo ${i+1} — ${l.chapters[i].title}**: ${x}`).join('\n')+'\n\n';
  t=t.replace(/## 4\.[\s\S]*?(?=## 5\.)/,block);
 }
 t=t.split('\n').map(line=>{
  if(line.startsWith('| m-'))return line;
  if(/^\| V\d/.test(line)){
   const parts=line.split('|');
   if(vol==='VOL-09'&&parts.length===8){parts.splice(3,0,' Contenuto e didattica ');}
   return parts.map((p,i)=>i>=3?clean(p):p).join('|');
  }
  return clean(line);
 }).join('\n');
 if(vol==='VOL-09')t=t.replace('| ID | Posizione | Gravità | Descrizione ed estratto | Correzione proposta | Stato |\n|---|---|---|---|---|---|','| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n|---|---|---|---|---|---|---|');
 t=t.replace(/allegato III2 dicembre/g,'allegato III dal 2 dicembre').replace(/\]\(([^)]*)\)/g,(_,url)=>']('+url.replace(/\s+/g,'')+')');
 fs.writeFileSync(p,t);
 console.log(vol,'leggibilità aggiornata');
}
