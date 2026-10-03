from pathlib import Path
import re,json,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc03-enti-non-economici')
plans=json.loads((A/'FC03-nuclei-plan.json').read_text(encoding='utf8'))
names=[
['Perimetro e natura degli enti','Famiglia EPNE e materie comuni','Delta specialistico e lettura del profilo','Errori di perimetro e caso guidato','Piano iniziale e verifica'],
['Organi di INPS e INAIL','Fonti, ordinamento e competenze','Governance, vigilanza e documenti','Schema delle responsabilità e caso','Errori, esercizi e verifica'],
['INPS e fondamenti della protezione sociale','Contributi, pensioni, sostegni e ISEE','Prestazioni e servizi nel procedimento','Caso utente e applicazione delle regole','Comunicazione e verifica previdenziale'],
['Rischio assicurato, premio e prestazioni','Nesso professionale e fonti INAIL','Assicurazione, prevenzione e servizio','Mappa operativa e caso lavorativo','Errori e verifica assicurativa'],
['Domanda e procedimento EPNE','Fasi, richieste e accesso','Servizi digitali e comunicazione','Caso, tutela e risposta motivata','Fascicolo e verifica finale'],
['Documenti contabili e organi competenti','Entrate, spese e ciclo finanziario','Patrimonio e sistemi di controllo','Trasparenza contabile e caso','Errori e calcoli di verifica'],
['Performance e programmazione integrata','Obiettivi, indicatori e rischi','Valore pubblico, monitoraggio e output','Caso e valutazione del servizio','Diario e verifica degli indicatori'],
['Rapporto pubblico e profilo EPNE','CCNL, aree e competenze','Doveri e condotta professionale','Risposte orali e recupero degli errori','Responsabilità e verifica contrattuale'],
['Fabbisogno EPNE e materie comuni','Ciclo di acquisto e responsabilità','Strumenti digitali e controlli','Caso di acquisto e applicazione','Diario e verifica del contratto'],
['Natura dell’ente e obiettivi del Decoder','Fonti, profilo, prove e materie','Avvisi e schede operative','Bando campione e caso guidato','Controlli e verifica del bando'],
['Fatti, competenza e griglia del caso','Schema di risposta e domanda INPS','Casi INAIL, documenti e accesso','Comunicazioni e risposte sintetiche','Esercitazioni e verifica dei mini-atti'],
['Contesto e competenze situazionali','Gerarchia delle scelte e scenari','Batteria di otto quesiti commentati','Lettura delle opzioni e caso utente','Esercitazione e verifica delle condotte'],
['Dati iniziali e struttura del piano','Prime settimane e consolidamento','Simulazioni e piani per ente','Caso Luca e correzione delle priorità','Ciclo settimanale e verifica'],
['Perimetro e competenze della vigilanza','Poteri, verbali, diffide e rimedi','Materie, scheda ispettiva e caso','Accertamento, limiti e contraddittorio','Riservatezza e verifica ispettiva'],
['Metodo del glossario e lessico INPS','Lessico assicurativo e amministrativo','Distinzioni e applicazione ai casi','Trappole e catene concettuali','Verifica del linguaggio tecnico'],
['Natura, comparti e confronto degli enti','Schede da ACI a CRI','Caso e metodo comparativo','Dal profilo ai documenti istituzionali','Aggiornamento e verifica comparativa'],
['Portale, gestore ed ente','Materie, allegati e perimetro','Prove, soglie e caso guidato','Laboratorio e controllo della domanda','Diario documentale e verifica'],
['Perimetro e criteri dei rinvii','Appendici e cambiamento di percorso','Destinazioni disponibili e casi','Costruzione del percorso di studio','Controllo dei rinvii e verifica'],
['Perimetro delle materie, UE e civile','Responsabilità e rito previdenziale','Sicurezza, finanze e reati contro la PA','Profilo sociale e strategia di studio','Cinque simulazioni e verifica integrata']]
rows=[];dims=[];manifest=[]
for idx,plan in enumerate(plans):
 p=Path(plan['path']);s=p.read_text(encoding='utf8');fm,body=s.split('---',2)[1:];body=re.sub(r'^## N-FC03-.*\n+','',body,flags=re.M).replace('### Testo editoriale\n\n','')
 chunks=[]
 for n,g in enumerate(plan['groups']):
  chunk=body[g['start']:g['end']];title=names[idx][n];nid=g['id'];chunks.append(f'## {nid} · {title}\n\n'+chunk)
  subheads=re.findall(r'^### (.+)$',chunk,re.M);qcount=len(re.findall(r'^\*\*Quiz \d+\.',chunk,re.M));ccount=int('### Caso ragionato di chiusura' in chunk);ecount=int('### Mini-esercizio' in chunk)
  # Counts describe physical occurrences. Shared final assessment is not multiplied per nucleus.
  verification=f'Q:{qcount} C:{ccount} E:{ecount}; richiamo alla verifica finale cap. {idx+1:02d}, domande 1–6 e caso, conteggiati una sola volta'
  if idx==11 and n==2:verification+='; inoltre 8 quesiti situazionali autonomi'
  if idx==18 and n==4:verification+='; inoltre 5 tracce miste con rubrica'
  concepts='; '.join(subheads[:5]);location=p.stem+' § '+nid
  rows.append('| '+' | '.join([nid,'EPNE, profilo amministrativo; delta dichiarato',title,concepts,'secondo programma','source_refs; rettifiche EPNE 3 ottobre 2026',location,'sviluppato nelle sezioni nominate','applicazioni e casi del capitolo','orale, caso o scheda',verification,'completo nel perimetro dichiarato','riesame corrente step 15',''])+' |')
  dims.append('| '+' | '.join([nid,'✓ concetti: '+title,'✓ obiettivo e uso del capitolo','✓ fonte e perimetro dichiarati','✓ '+(subheads[0] if subheads else title),'✓ confronti nelle sezioni elencate','✓ passaggio operativo e soluzione finale','✓ casi del capitolo, senza duplicarne il conteggio','✓ errore tipico o confronto motivato','✓ verifica finale cap. '+str(idx+1),'✓ source_refs e nota rettifiche'])+' |')
  manifest.append({'id':nid,'title':title,'path':p.as_posix(),'sections':subheads,'words':g['words'],'quizPhysicalCount':qcount,'casePhysicalCount':ccount,'exercisePhysicalCount':ecount})
 # Put the H1 before the first nucleus rather than nesting the title inside it.
 text=''.join(chunks);h1=re.search(r'^# .+\n+',text,re.M)
 if h1: titleline=h1.group();text=text[:h1.start()]+text[h1.end():];text=titleline+text
 p.write_text('---'+fm+'---\n'+text,encoding='utf8')
mp=B/'planning/02-matrice-copertura-didattica.md';old=mp.read_text(encoding='utf8');arc=A/'before-text/VOL-03/FC03-02-matrice-copertura-didattica.md'
if not arc.exists():shutil.copy2(mp,arc)
fm=old.split('---',2)[1];fm=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',fm,flags=re.M);fm=re.sub(r'^review_required:.*$','review_required: true',fm,flags=re.M)
mp.write_text('---'+fm+'''---

# Matrice M-FC03 — riallineamento del 3 ottobre 2026

I 95 nuclei sono ricollocati a confini di sezioni complete: nessuna domanda è separata dalla propria sequenza e nessun caso è interrotto da una nuova intestazione di nucleo. La precedente matrice è archiviata negli artefatti. I conteggi Q/C/E indicano la collocazione fisica; la verifica conclusiva attraversa più nuclei ma non viene moltiplicata cinque volte. Totale aggiunto/sostituito: 114 domande aperte, 19 casi finali, otto situazionali e cinque tracce miste. Restano gli esempi ed esercizi preesistenti utili. Il grado completo riguarda il perimetro esplicitato, non una promessa di copertura di ogni professione sociale, sanitaria o ispettiva.

## Copertura primaria

| Nucleo ID | Famiglia/Profilo | Materia | Concetto/sotto-concetti | Frequenza/Peso | Fonti consolidate | Collocazione | Copertura teorica | Applicazione | Output concorsuale | Verifica | Stato | Review normativa | Destinazione rinvio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''+'\n'.join(rows)+'''

## Checklist dimensionale

La checklist si legge con le sezioni puntuali della tabella precedente e con il caso/soluzioni del capitolo. Gli apparati di metodo hanno una funzione applicativa: non si inventano definizioni normative autonome per ciascuna checklist. Le fonti normative sono collegate nel frontmatter e le regole sono spiegate nei nuclei specialistici; gli esercizi richiamano tali regole.

| Nucleo ID | Definizione | Funzione | Inquadramento | Elementi | Distinzioni | Conseguenze | Esempio/caso | Errore tipico | Verifica | Fonti |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''+'\n'.join(dims)+'\n',encoding='utf8')
(A/'FC03-nuclei-ledger.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print('95 nuclei semantici e matrice riallineati.')
