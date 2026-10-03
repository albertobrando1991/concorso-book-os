from pathlib import Path
import re,json,hashlib,shutil
A=Path('artifacts/correzioni-collana-2026-10-02');p=next(Path('wiki/books/moduli/m-fc04-giustizia/chapters').glob('10-*.md'));t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest();b=A/'before-text/VOL-04/first'/p.name
if not b.exists():shutil.copyfile(p,b)
t=t.replace('| Soggetto | Persona o ente a cui il dato si riferisce |','| Soggetto | Persona fisica cui si riferiscono le iscrizioni; per gli enti opera la distinta anagrafe delle sanzioni dipendenti da reato. |')
t=t.replace('Il suo oggetto riguarda procedimenti penali in corso a carico di un soggetto, con esclusioni e limiti previsti dal Testo unico.','Il suo oggetto riguarda provvedimenti relativi a soggetti che hanno assunto la **qualità di imputato**, secondo gli artt. 2 e 6 del D.P.R. 313/2002, con esclusioni e limiti di menzionabilità. Non è un elenco indiscriminato delle indagini in corso.')
at=t.index('### Anagrafe delle sanzioni')
t=t[:at]+'''### Dall'iscrizione della notizia di reato alla pendenza certificabile

L'**art. 335 c.p.p.** riguarda l'iscrizione della notizia di reato e del nome della persona cui il reato è attribuito; l'interessato ha in questa fase la posizione di indagato. L'**art. 60 c.p.p.** collega invece la qualità di imputato agli atti che formulano l'imputazione: per esempio, la richiesta di rinvio a giudizio o il decreto di citazione diretta. Neppure il solo avviso di conclusione delle indagini dell'art. 415-bis trasforma automaticamente l'indagato in imputato.

| Documento o evento | Posizione da riconoscere | Conseguenza per il servizio |
|---|---|---|
| Iscrizione nominativa ex art. 335 | Indagato. | Non basta per affermare un carico pendente certificabile come imputato. |
| Avviso ex art. 415-bis | Conclusione delle indagini con garanzie difensive. | Non sostituire il certificato dei carichi pendenti alla distinta comunicazione ex art. 335. |
| Richiesta di rinvio a giudizio | Assunzione della qualità di imputato. | Rileva per le iscrizioni dei carichi pendenti secondo artt. 6 e 27 TUC. |
| Condanna irrevocabile | Procedimento definito per il relativo capo. | Rileva l'iscrizione nel casellario secondo l'art. 3; non si qualifica ancora quel medesimo capo come pendente. |

La comunicazione delle iscrizioni prevista dall'art. 335 segue presupposti, segreto e limiti propri, illustrati nel capitolo 7. Un certificato dei carichi pendenti senza iscrizioni non dimostra quindi, da solo, l'assenza di qualsiasi indagine. Il contenuto dipende anche dall'ufficio che lo rilascia e dalle esclusioni dell'art. 27.

I certificati hanno **validità di sei mesi dal rilascio**, secondo le indicazioni ministeriali. Il dato attesta la situazione certificata: non impedisce che in seguito intervengano nuovi provvedimenti. Per la visura, priva di efficacia certificativa, non si deve parlare di certificato alternativo valido per sei mesi.

''' +t[at:]
at=t.index('### Pubbliche amministrazioni, decertificazione')
t=t[:at]+'''### Il certificato del datore per attività con minori: un obbligo delimitato

L'**art. 25-bis del D.P.R. 313/2002** stabilisce che il soggetto che intende impiegare una persona al lavoro per attività comportanti **contatti diretti e regolari con minori deve richiedere** il certificato pertinente. Non è una semplice facoltà di controllo. La richiesta compete al datore per lo specifico rapporto, e non va sostituita automaticamente da un generico certificato ottenuto dal candidato per uso personale.

La verifica riguarda le condanne per i reati degli artt. 600-bis, 600-ter, 600-quater, 600-quinquies e 609-undecies c.p., oltre alle pertinenti sanzioni interdittive. Non è il potere di acquisire senza limiti ogni informazione penale o ogni carico pendente.

Le FAQ ministeriali precisano che l'obbligo si riferisce all'instaurazione di un rapporto contrattuale con prestazioni corrispettive; può riguardare anche un professionista quando il contratto realizza tale rapporto. Un'associazione che assume un educatore non è esclusa soltanto perché opera nel volontariato. Le collaborazioni volontarie estranee a un rapporto di lavoro non sono invece automaticamente equiparate alle assunzioni ai fini di questo obbligo.

| Situazione | Applicazione |
|---|---|
| Nuova assunzione di educatore con attività quotidiana con minori | Il datore deve richiedere il certificato ex art. 25-bis. |
| Attività amministrativa senza contatti diretti e regolari con minori | Il solo nome dell'organizzazione non integra il presupposto: verificare la mansione concreta. |
| Nuovo contratto dopo la scadenza del precedente | Le FAQ ministeriali ricondicono anche questo caso al sorgere dell'obbligo. |
| Decorso di sei mesi durante il medesimo rapporto | La validità semestrale del documento non crea un obbligo generale di nuova richiesta ogni sei mesi. |

Nell'attesa del certificato **già richiesto**, le FAQ ammettono una dichiarazione sostitutiva di certificazione per il datore pubblico o di atto di notorietà per quello privato. È una gestione dell'attesa, non l'eliminazione definitiva del controllo. Prima dell'avvio del rapporto si qualifica la mansione e si adempie all'obbligo di richiesta.

''' +t[at:]
t=t.replace('Dal 1 gennaio 2012, nei rapporti con pubbliche amministrazioni e gestori di pubblici servizi, i certificati sono necessari solo nei rapporti tra privati; nei rapporti con PA e gestori pubblici si usano dichiarazioni sostitutive e acquisizione d\'ufficio nei limiti previsti.',"Dal 1° gennaio 2012, nei rapporti con pubbliche amministrazioni e gestori di pubblici servizi opera il regime di dichiarazioni sostitutive e acquisizione d'ufficio nei limiti previsti. Il certificato consegnato dal privato conserva il proprio ambito nei rapporti tra privati e negli altri casi espressamente disciplinati.")
t=t.replace('utilizzando canali istituzionali e, per il casellario, il sistema CERPA.',"utilizzando i canali istituzionali autorizzati secondo l'art. 39 del Testo unico.")
at=t.index('### Uffici',t.index('### Pubbliche amministrazioni'))
t=t[:at]+'''### Accessi PA: PDND, convenzioni e QuiCasellario

Il vigente **art. 39** prevede la consultazione per le PA e i gestori di pubblici servizi mediante accreditamento alla **Piattaforma Digitale Nazionale Dati (PDND)**; nelle more dell'accreditamento, operano apposite convenzioni. La disposizione non prova che qualsiasi amministrazione possa già interrogare qualsiasi dato: occorrono legittimazione, servizio disponibile, accreditamento o accordo e selezione delle informazioni pertinenti.

CERPA è una denominazione presente nei servizi e nelle istruzioni pregresse per le PA, ma non va insegnata come unico canale immutabile. **QuiCasellario** permette servizi fondati su accordi diretti con gli uffici. Per esempio, la Procura di Pescara indica l'attivazione di tali accordi e il superamento locale di MASSIVE CERPA, richiamando una circolare del 5 febbraio 2026. Questo esempio dimostra l'evoluzione dei canali; non autorizza a trasferire recapiti o modalità della sede a tutte le procure.

Il controllo resta identico: quale procedimento amministrativo giustifica la richiesta, quali reati o informazioni rilevano, chi è abilitato e quale traccia deve restare. L'interoperabilità evita al cittadino di fare da corriere del certificato, ma non amplia da sola il potere di conoscere dati penali.

''' +t[at:]
at=t.index('### Archivi, conservazione')
t=t[:at]+'''### Iscritto, menzionato, eliminato: tre esiti diversi

L'art. 3 elenca i provvedimenti da iscrivere. Accanto alle condanne definitive vi sono, tra gli altri, provvedimenti sulle misure alternative, riabilitazione, messa alla prova e amministrazione di sostegno. Il certificato richiesto dall'interessato segue invece le esclusioni dell'art. 24: non è la stampa integrale della banca dati.

| Esempio | Iscrizione e certificato dell'interessato |
|---|---|
| Condanna con beneficio di non menzione non revocato | L'iscrizione esiste; la condanna non è menzionata nel certificato ex art. 24. |
| Sospensione con messa alla prova ed estinzione per esito positivo | Provvedimenti previsti dall'art. 3, esclusi dal certificato dell'interessato dall'art. 24. |
| Riabilitazione non revocata | Incide sulla menzionabilità secondo art. 24; non significa cancellazione arbitraria di ogni dato. |
| Condanna revocata a seguito di revisione | L'art. 5 prevede l'eliminazione dell'iscrizione relativa al provvedimento revocato. Occorre il titolo che la giustifica. |

**Non menzionare** significa escludere un'iscrizione da un determinato prodotto certificativo; **eliminare** significa intervenire sull'iscrizione quando ricorrono i presupposti del Testo unico. La visura consente all'interessato di conoscere le iscrizioni senza efficacia certificativa e non deve essere usata per aggirare le regole del certificato destinato a terzi.

L'art. 5 detta anche termini e condizioni specifici. Per esempio, le condanne del giudice di pace a pena pecuniaria sono eliminate dopo cinque anni dall'esecuzione della sanzione, purché nel periodo non sia commesso un ulteriore reato; per una pena diversa il termine è dieci anni. Non basta contare gli anni dalla data della sentenza. Per i minori, la regola dell'eliminazione al diciottesimo anno presenta eccezioni: perdono giudiziale al ventunesimo anno e provvedimenti di condanna a pena detentiva, anche condizionalmente sospesa. Una formula «a diciotto anni si cancella tutto» sarebbe errata.

### Contestazione del dato e giudice competente

L'operatore verifica il documento e attiva il percorso competente; non cancella una condanna valida per assecondare una richiesta orale. Se sorge una questione su iscrizioni o certificati, l'**art. 40** attribuisce la decisione al tribunale monocratico del luogo di nascita della persona, con le forme dell'art. 666 c.p.p.; per nati all'estero o luogo di nascita non accertato in Italia è competente il Tribunale di Roma. Per le anagrafi delle sanzioni e delle pendenze degli enti decide il Tribunale di Roma.

Questo rimedio non va confuso con l'ufficio che ha materialmente rilasciato la copia. Un certificato ottenuto in una città diversa dalla nascita non sposta, da solo, la competenza prevista per la controversia sull'iscrizione.

''' +t[at:]
t=t.replace('Al cut-off istituzionale del volume, le pagine del Ministero indicano','Nelle pagine ministeriali consultate il 3 ottobre 2026, il Ministero indica')
t=t.replace('nel sistema CERPA','nei canali autorizzati ex art. 39').replace('canale CERPA','canale autorizzato').replace('norma, contratto e limiti sul trattamento dei dati','la previsione normativa applicabile e i limiti sul trattamento dei dati; una clausola contrattuale non è da sola sufficiente')
t=t.replace('In prova non conviene ricordare una cifra. Conviene ricordare il flusso.','Il flusso va studiato insieme alle regole sostanziali richieste dal bando; una domanda sugli importi richiede la tabella ufficiale vigente, non una cifra ricordata senza data.')
at=t.index('### Da sapere in 5 righe')
t=t[:at]+'''### Dossier svolto: quattro richieste, quattro risposte

**Caso fittizio, 8 ottobre 2026.** R1: Luca, residente a Bologna, produce un avviso ex art. 415-bis e chiede se sia già imputato. R2: un'associazione sta assumendo un educatore che lavorerà ogni giorno con minori. R3: un ministero chiede al candidato di portare il certificato del casellario per controllare un requisito ordinario autocertificabile. R4: Sara, nata a Firenze, ritira a Bologna un certificato e contesta una condanna che ritiene non più menzionabile; non risulta agli atti un provvedimento di eliminazione.

| Richiesta | Risposta modello |
|---|---|
| R1 | L'avviso415-bis non basta ad assumere la qualità di imputato. Verificare gli atti dell'art.60; distinguere carichi pendenti e comunicazione335. |
| R2 | Obbligo del datore ex25-bis per il nuovo rapporto con contatti diretti e regolari. La forma associativa non esclude l'obbligo. |
| R3 | Per il requisito indicato opera dichiarazione sostitutiva e controllo/acquisizione d'ufficio; individuare il canale autorizzato della PA. |
| R4 | Verificare tipo di certificato e regola di menzionabilità senza cancellare informalmente. Per la questione ex40 è competente il tribunale monocratico di Firenze, non Bologna per il solo luogo di rilascio. |

**Valutazione, 12 punti.** Tre punti per richiesta: regola pertinente, conseguenza corretta, limite o controllo necessario. Risposte come «è tutto online», «lo decide la privacy» o «basta chiedere il certificato» non spiegano l'esito e non ottengono i tre punti.

''' +t[at:]
i=t.index('### Quiz commentato');j=t.index('### Checklist di ripasso',i)
t=t[:i]+'''### Quiz commentati

1. **È stato notificato soltanto l'avviso ex art. 415-bis. Quale conclusione è corretta?**
   - A. Il destinatario è già condannato.
   - B. Il destinatario è sempre imputato dal giorno dell'iscrizione ex335.
   - C. L'avviso, da solo, non attribuisce la qualità di imputato.
   - D. Il certificato dei carichi pendenti contiene necessariamente tutte le indagini.
   **Risposta corretta: C.** La qualità di imputato segue gli atti dell'art.60, distinti dall'iscrizione della notizia e dall'avviso di conclusione indagini.

2. **Una condanna con non menzione non revocata non compare nel certificato dell'interessato. Che cosa significa?**
   - A. L'iscrizione può esistere, ma è esclusa da quel certificato.
   - B. La sentenza non è mai esistita.
   - C. La condanna è stata necessariamente eliminata dal sistema.
   - D. La visura assume efficacia certificativa verso il datore.
   **Risposta corretta: A.** Art.24 e art.5 regolano operazioni differenti: menzionabilità ed eliminazione.

3. **Un'associazione assume un educatore per contatti quotidiani con minori. Quale regola si applica?**
   - A. La forma associativa esclude l'art.25-bis.
   - B. Basta qualsiasi certificato personale del candidato.
   - C. Il certificato è una facoltà rimessa alla curiosità del datore.
   - D. Il datore deve richiedere il certificato pertinente per il nuovo rapporto.
   **Risposta corretta: D.** Rilevano rapporto lavorativo e contatti diretti e regolari, non il solo nome dell'organizzazione.

4. **La validità semestrale del certificato ex art.25-bis impone una nuova richiesta ogni sei mesi durante lo stesso rapporto?**
   - A. Sì, per ogni dipendente senza eccezioni.
   - B. No: le FAQ distinguono la validità del certificato dal sorgere dell'obbligo all'assunzione.
   - C. Sì, ma solo se il datore è un'associazione.
   - D. No, perché il certificato vale indefinitamente.
   **Risposta corretta: B.** Il nuovo contratto dopo la scadenza è distinto dal semplice decorso di sei mesi nel rapporto in corso.

5. **Una PA legge che l'art.39 prevede l'accesso mediante PDND. Che cosa può concludere?**
   - A. Tutti i dipendenti possono consultare liberamente l'intera banca dati.
   - B. Il cittadino deve sempre stampare un certificato.
   - C. Servono titolo, finalità, servizio e accreditamento o accordo secondo il regime applicabile.
   - D. Un avviso di una Procura vale automaticamente per ogni ufficio nazionale.
   **Risposta corretta: C.** Interoperabilità e legittimazione al trattamento sono piani distinti; la norma non prova l'attivazione universale.

6. **Una persona nata in Italia contesta un'iscrizione; il certificato è stato ritirato altrove. Quale criterio segue l'art.40?**
   - A. Tribunale monocratico del luogo di nascita, con le forme dell'art.666 c.p.p.
   - B. Sempre il luogo di ritiro.
   - C. Sempre la residenza attuale.
   - D. La cancelleria decide definitivamente senza rimedio giudiziario.
   **Risposta corretta: A.** Il luogo del rilascio non modifica da solo la competenza; per nati all'estero o luogo non accertato opera Roma.

''' +t[j:]
# Keep printed prose spaced, including new legal references.
t=re.sub(r'(art\.|ex|avviso|comunicazione)(\d)',r'\1 \2',t)
s='sources/vol-04-casellario-verifica-2026-10-03.md';t=t.replace('source_refs: [','source_refs: [\n  "'+s+'",',1).replace('last_compiled_from: [','last_compiled_from: [\n  "wiki/'+s+'",',1)
t=re.sub(r'updated_at: .*','updated_at: 2026-10-03',t,count=1).replace('review_required: false','review_required: true',1).replace('status: reviewed','status: revised_draft',1).replace('draft_stage: reviewed','draft_stage: editorial-revision',1)
p.write_text(t,'utf-8');result={'file':p.as_posix(),'before':before,'after':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(t.split()),'quizKeys':re.findall(r'Risposta corretta: ([A-D])',t),'source':s,'textApplied':True,'pdfVerified':False};(A/'VOL-04-casellario-delta.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf-8');print(json.dumps(result,ensure_ascii=False))
