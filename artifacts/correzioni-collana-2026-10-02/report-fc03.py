from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');B=Path('wiki/books/moduli/m-fc03-enti-non-economici');R=Path('wiki/reviews/pipeline/VOL-03')
applied={2:'FC03/08: CCNL definitivo del 6 agosto 2026, successione dei contratti e ferie dal 2027.',14:'Appendice F: abrogazione art. 323, distinzione dei reati vigenti e art. 314-bis.',15:'Tutti i 19 capitoli: 114 domande specifiche e 19 casi originali, con soluzioni separate e ragionate.',16:'FC03/03: art. 38, previdenza/assistenza, contribuzione, automaticità, pensioni, NASpI, invalidità, ISEE/DSU e calcoli.',17:'FC03/04: rischio assicurato, causa e occasione di lavoro, in itinere, malattie tabellate/non, premi, prestazioni, danno biologico e limiti automaticità.',18:'Appendice A: competenze, accesso, verbali, due diffide, conciliazione, recuperi, tutele e aggiornamento 2024.',19:'FC03/02: Presidente, CdA, CIV, DG, Collegio dei sindaci e vigilanza ministeriale.',20:'FC03/06: DPR 97/2003, d.lgs. 91/2011, regolamenti, documenti preventivi/consuntivi, competenze e calcoli.',21:'Appendice F: responsabilità e patologie civilistiche, rito lavoro/previdenza, ATP, obblighi 81/2008 e finanze con casi.',22:'Appendice B: definizioni sostanziali di premio e danno biologico, soglie e rinvio al caso INAIL.',23:'Appendice B: INAIL nel sistema previdenziale; automaticità distinta dall’assenza di istruttoria.',24:'Capitoli 01/10/12 e appendice C: CRI privata dal 2016; comparto Istruzione e Ricerca degli EPR anche amministrativi.',25:'Tutti i capitoli: 95 nuclei ricollocati a confini semantici, titoli specifici e matrice riconciliata senza moltiplicare i quiz.',26:'Appendice E: destinazioni esistenti per volume/capitolo/sezione, copertura e limiti espliciti; rinvio ispettivo e procurement ridimensionati.',41:'FC03/11: acquisizione d’ufficio, caso residenza e caso P-18 con documento, data e canale autosufficienti.',42:'FC03/12: canale telefonico autorizzato e verificato, astensione nei casi dovuti.',49:'FC03/12: otto situazionali con alternative plausibili, chiavi A/B/C/D bilanciate e commenti coerenti.',51:'FC03/13: articolo duplicato e accento corretti; origine dei dieci scenari esplicitata.',53:'Corpo dei 19 capitoli: rimossi riferimenti staff, fonti nominate per il lettore; perimetro sociale esplicitamente definito.',55:'Appendice F: cinque tracce complete, soluzioni applicate, tempi e rubrica 10 punti.',56:'Appendice C: CONI nel confronto operativo finale.',57:'Appendice D: recupero documentato e archivio degli errori, cancellazione dei soli duplicati.'}
# Make the legal rule tested by question 08/4 explicit in the teaching text.
p=next((B/'chapters').glob('08-*.md'));s=p.read_text(encoding='utf8');head='### 4. Doveri e codice di comportamento'
s=s.replace(head,head+'''\n\nPer un ordine ritenuto manifestamente illegittimo, il dipendente formula rimostranza spiegandone le ragioni; se l'ordine è rinnovato per iscritto, segue la disciplina contrattuale. Non deve comunque eseguirlo se vietato dalla legge penale o costituente illecito amministrativo: è il limite dell'articolo 42, comma 3, lettera h, del CCNL 2019–2021, da coordinare con i rinnovi. La rimostranza non coincide con un rifiuto immotivato; il rinnovo scritto non sana un illecito. Nei conflitti di interesse si aggiungono segnalazione e astensione quando dovute, anche nell'istruttoria.\n''',1);p.write_text(s,encoding='utf8')
audit={}
for line in Path('wiki/reviews/audit-integrale-2026-10-02/VOL-03.md').read_text(encoding='utf8').splitlines():
 if re.match(r'\| V03-\d{3} \|',line):
  c=[x.strip() for x in line.strip('|').split('|')];audit[int(c[0][-3:])]=c
table='| ID | Posizione | Categoria | Gravità | Descrizione | Correzione proposta | Stato |\n| --- | --- | --- | --- | --- | --- | --- |\n'
for n,desc in sorted(applied.items()):
 c=audit[n];table+='| '+c[0]+' | '+c[1]+' | '+c[2]+' | '+c[3]+' | '+c[4]+' | '+desc+' | Applicato; riesame del testo corrente |\n'
text='''# M-FC03 — Correzioni integrali, step 14, 3 ottobre 2026

## 1. Sintesi editoriale

Applicati i 22 rilievi del modulo: integrate teoria previdenziale e assicurativa, governance, contabilità, vigilanza e materie INAIL; aggiornato il CCNL; sostituite le verifiche ripetute. I 19 capitoli mantengono contenuti ed esempi legittimi. I 95 nuclei iniziano su sezioni complete e la matrice non attribuisce più sei quiz identici a ciascuna riga.

## 2. Metodo e copertura

Baseline: lettura integrale documentata nell'audit VOL-03. La correzione riprende tutti i 19 file e i 22 ID, con riesame dei blocchi modificati, dei 114 nuovi quesiti aperti, dei 19 casi finali, degli otto situazionali e delle cinque tracce miste. Le soluzioni sono dopo la prova. Questo rapporto non attribuisce una nuova lettura integrale a tutte le fonti storiche né sostituisce il controllo del PDF candidato.

## 3. Registro per ID

'''+table+'''
## 4. Fonti ed evidenze

Nuova nota `epne-previdenza-assicurazione-rettifiche-2026-10-03.md` e topic collegato, con URL ufficiali INPS, INAIL, INL, ARAN, Normattiva, Gazzetta Ufficiale, Senato e CRI. Tre PDF acquisiti con hash: CCNQ 2025–2027, circolare INL 6/2020, preventivo INPS 2026. I documenti sono letti per i passaggi pertinenti; le tavole economiche del preventivo non sono oggetto di audit integrale. Rettifiche delle tre note storiche collegate, conservate per tracciabilità; testo definitivo CCNL già consolidato nella fonte ARAN condivisa.

## 5. Coerenza e autonomia

La previdenza comprende anche l'assicurazione INAIL; automaticità e istruttoria sono compatibili. CRI non è presentata come EPNE ordinario e gli enti di ricerca non diventano Funzioni Centrali per le mansioni amministrative. Vigilanza, servizio sociale e procurement riportano il limite del percorso e le integrazioni necessarie; le destinazioni della collana hanno volume, capitolo e sezione esistenti. Il caso P-18 identifica i dati didattici senza trasformarli in termini generali dell'ente.

## 6. Verifiche

I 19 gate di copertura e densità sono passati senza blocchi né warning dopo il riallineamento semantico. Zero destinazioni o ancore irrisolte nel corpo; cinque destinazioni esterne al modulo censite nell'artefatto dedicato. Verificati calcoli ISEE, durata NASpI, cassa/residui, tassi di errore e costo medio; otto situazionali con due chiavi per ciascuna lettera, senza commenti rimappati per errore. Le sei domande aperte finali per capitolo hanno risposte specifiche e non richiedono una falsa distribuzione di lettere.

## 7. Suggerimenti facoltativi

Nessun suggerimento opzionale è assunto come correzione obbligatoria. Eventuali accorpamenti di schede saranno valutati soltanto sull'export, senza rimuovere contenuto teorico o soluzioni.

## 8. Priorità

Riesame specialistico 15, freeze 16 con manifest e controlli manuali quando il gate non è implementato; quindi figura, PDF candidato e preflight di volume. Le verifiche di testo non anticipano l'esito degli ultimi passaggi.

## 9. Giudizio

I 22 rilievi risultano corretti nel manoscritto corrente, con copertura circoscritta alle promesse esplicite. Il modulo non è ancora dichiarato pubblicabile: occorrono i controlli sull'esportazione aggiornata e il completamento della pipeline del volume.

## 10. Limiti

Norme e dati verificati al 3 ottobre 2026 per i claim pertinenti; esempi numerici e calendari didattici identificati come tali. Nessuna promessa di esaustività rispetto a ogni bando ispettivo o professione sociale. Nessuna approvazione delle figure preesistenti o delle pagine PDF non ancora rigenerate dopo questi interventi.
'''
p=R/'14-moduli-m-fc03-enti-non-economici.md';archive=A/'before-text/VOL-03'/p.name
if p.exists() and not archive.exists():shutil.copy2(p,archive)
p.write_text(text,encoding='utf8')
# Persist corrected IDs and sources for the volume register.
(A/'FC03-applied.json').write_text(json.dumps(applied,ensure_ascii=False,indent=2),encoding='utf8')
reg=A/'update-vol03-register.py';s=reg.read_text(encoding='utf8');needle="for line in audit.read_text(encoding='utf-8').splitlines():"
s=s.replace(needle,"applied.update({int(k):v for k,v in json.loads((root/'artifacts/correzioni-collana-2026-10-02/FC03-applied.json').read_text(encoding='utf8')).items()})\n"+needle)
reg.write_text(s,encoding='utf8')
print('Rapporto 14 con 22 ID e registro predisposti.')
