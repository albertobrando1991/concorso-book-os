from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl01-comuni-unioni/chapters')
def replace(s,old,new):
 assert old in s,old[:90]
 return s.replace(old,new)
def paragraph(s,start,new):
 return re.sub(re.escape(start)+r'[^\n]*',lambda m:new,s,count=1)
p=next(base.glob('09-*.md'));s=p.read_text(encoding='utf8')
s=replace(s,'La disciplina collega il bilancio a un orizzonte pluriennale.','Il bilancio di previsione copre un orizzonte almeno triennale.')
s=paragraph(s,'Per le scadenze bisogna distinguere', '''Il calendario seguente riporta i termini ordinari. Un differimento previsto per un determinato esercizio va verificato nella fonte che lo dispone; non modifica per sempre la regola del TUEL.

| Documento o verifica | Organo e adempimento | Termine ordinario |
| --- | --- | --- |
| DUP | La Giunta presenta al Consiglio, per le conseguenti deliberazioni | 31 luglio, in vista del ciclo successivo |
| Nota di aggiornamento al DUP | La Giunta presenta al Consiglio con lo schema del bilancio | 15 novembre |
| Bilancio di previsione | Approvazione del Consiglio | 31 dicembre dell'anno precedente |
| PEG | Adozione della Giunta | Entro 20 giorni dall'approvazione del bilancio |
| Assestamento generale | Verifica generale del Consiglio | 31 luglio dell'esercizio in corso |
| Salvaguardia degli equilibri | Verifica e, se necessarie, misure del Consiglio | Almeno una volta entro il 31 luglio, oltre alle verifiche previste dal regolamento |
| Rendiconto | Approvazione del Consiglio | 30 aprile dell'anno successivo |

Per il bilancio 2027–2029, il percorso ordinario parte dal DUP presentato entro luglio 2026 e arriva al bilancio approvato entro dicembre 2026. Il rendiconto della gestione 2027 si approva entro aprile 2028. L'esempio separa l'anno di preparazione, quello di gestione e quello della dimostrazione dei risultati; non presume proroghe.''')
s=replace(s,'Il PEG risponde quindi a tre domande:', 'Per i Comuni con popolazione inferiore a 5.000 abitanti l’applicazione dei commi 1 e 2 dell’art. 169 è facoltativa: la facoltà riguarda il PEG, non l’obbligo di assicurare una gestione organizzata, responsabilità definite e copertura delle spese. Il PEG risponde quindi a tre domande:')
s=replace(s,'La disciplina introdotta nel 2022 collega','Istituito dall’art. 6 del d.l. 80/2021, il Piano collega')
s=paragraph(s,'Le amministrazioni con più di cinquanta', '''Per le amministrazioni con meno di 50 dipendenti il DM 132/2022 prevede modalità semplificate: la semplificazione non equivale a esonero dal Piano. Il caso di esattamente 50 dipendenti richiede attenzione: il DPR 81/2022 usa «non più di cinquanta», mentre il DM 132/2022 usa «meno di cinquanta». Il quadro operativo del PNA 2022 ANAC distingue almeno 50 dipendenti, regime ordinario, e meno di 50, regime semplificato. Una risposta che colloca 50 in nessuna delle due fasce lascia irrisolta la domanda. Restano da applicare le indicazioni specifiche per la tipologia di ente e i contenuti effettivamente richiesti.''')
p.write_text(s,encoding='utf8')
p=next(base.glob('10-*.md'));s=p.read_text(encoding='utf8')
s=paragraph(s,'Calcoli improvvisati indeboliscono', '''### Due calcoli con presupposti dichiarati

**FPV.** Un contributo di 100.000 euro è già accertato e incassato nel 2026. Il contratto di lavori è perfezionato: 40.000 euro di prestazioni sono esigibili nel 2026 e 60.000 nel 2027. Assumendo soddisfatte le condizioni del principio contabile applicato, il FPV di spesa al termine del 2026 è 60.000 euro: conserva il collegamento tra finanziamento e spesa futura. L'importo non diventa avanzo libero solo perché si trova ancora in tesoreria. Se manca l'obbligazione perfezionata, occorre esaminare le specifiche condizioni del principio applicato: non si costituisce il FPV per il solo desiderio di spendere l'anno dopo.

**FCDE.** Le previsioni di entrate soggette al fondo sono 100.000 euro. Si assume che il rapporto medio di riscossione, calcolato correttamente sulla serie storica e secondo le regole applicabili, sia il 70%. La quota non riscossa è il 30%: nell'esempio l'accantonamento è 100.000 × 30% = 30.000 euro. Non si inventa una percentuale prudenziale: si selezionano le entrate soggette al fondo, si applica il metodo previsto dall'allegato 4/2 al d.lgs. 118/2011 e si documentano dati e calcolo. Il credito rimane iscritto finché ne sussistono i presupposti; il fondo limita la capacità di spendere contando su incassi incerti.

### Chi approva una variazione

| Fattispecie | Competenza e controllo |
| --- | --- |
| Regola generale delle variazioni di bilancio | Consiglio, art. 175, comma 2, TUEL |
| Variazioni attribuite espressamente all'esecutivo | Giunta, nei casi del comma 5-bis; per esempio, variazioni di cassa nei limiti previsti |
| Variazioni gestionali attribuite ai responsabili | Responsabili, nei casi e con le modalità del comma 5-quater e del regolamento contabile; non qualsiasi spostamento discrezionale |
| Variazione urgente di competenza consiliare | Giunta con urgenza motivata; ratifica consiliare entro 60 giorni e comunque entro il 31 dicembre |

Se la ratifica manca o è parziale, il Consiglio regola i rapporti eventualmente sorti nei successivi 30 giorni, sempre entro il 31 dicembre. Una variazione urgente adottata il 20 dicembre non consente di attendere febbraio: il limite di fine esercizio prevale. Non occorre invece ratificare come urgente una variazione che appartiene già alla competenza propria della Giunta.''')
s=paragraph(s,'Il risultato di amministrazione sintetizza', '''Il risultato di amministrazione si determina al rendiconto con la formula:

**Fondo cassa al 31 dicembre + residui attivi − residui passivi − fondo pluriennale vincolato di spesa = risultato di amministrazione.**

Il risultato si scompone poi in quote accantonate, vincolate, destinate agli investimenti e parte disponibile. Il FPV, già sottratto nella prima formula, non va sottratto una seconda volta.

**Esempio, valori in migliaia di euro.** Cassa 200, residui attivi 120, residui passivi 90 e FPV 60 producono: 200 + 120 − 90 − 60 = **170**. Se le quote accantonate sono 80, quelle vincolate 50 e quelle destinate agli investimenti 20, la parte disponibile è 170 − 80 − 50 − 20 = **20**. La cassa di 200 non misura quindi le risorse libere. Se gli accantonamenti necessari salgono a 110, a parità degli altri dati la parte disponibile diventa **−10**: emerge un disavanzo da affrontare secondo l'art. 188 TUEL, benché il risultato complessivo sia ancora positivo. L'esempio mostra perché omettere il FCDE o altri accantonamenti altera la valutazione dell'equilibrio.''')
s=replace(s,'La composizione monocratica o collegiale dipende dalla disciplina applicabile; ai fini concorsuali conta soprattutto riconoscere la funzione.', 'Per i Comuni con meno di 15.000 abitanti opera un revisore unico; da 15.000 abitanti opera un collegio di tre componenti, secondo l’art. 234 TUEL. Questa soglia non va trasferita automaticamente alle Unioni, per le quali esistono disposizioni specifiche. L’incarico dura tre anni; non può essere svolto più di due volte nello stesso ente, anche se i mandati non sono consecutivi. La nomina segue le regole speciali di selezione e le incompatibilità: non è una scelta fiduciaria del responsabile finanziario.')
s=replace(s,'Tra i compiti ricorrenti figurano i pareri sugli strumenti finanziari e sugli atti individuati dalla legge, le verifiche di cassa, la vigilanza sulla regolarità contabile e finanziaria, l’esame degli equilibri e la relazione sul rendiconto.', 'L’art. 239 TUEL prevede, fra l’altro, pareri sul bilancio, sulle variazioni per le quali il parere è richiesto, sul riconoscimento dei debiti fuori bilancio e sulle proposte di regolamento di contabilità, economato e applicazione dei tributi locali. Comprende vigilanza sulla gestione e relazione sul rendiconto. Le verifiche ordinarie di cassa e della gestione del tesoriere e degli altri agenti contabili hanno cadenza trimestrale, ai sensi dell’art. 223; vanno distinte dalle verifiche straordinarie.')
anchor='## N-FL01-10-04'
idx=s.index(anchor)
s=s[:idx]+'''### Esercizio provvisorio e gestione provvisoria

Se il bilancio non è approvato all'inizio dell'anno, non si applica automaticamente una proroga illimitata. L'esercizio provvisorio è autorizzato dalla legge o dal decreto che differisce il termine nei casi previsti. L'art. 163 TUEL consente la gestione entro i limiti delle previsioni del secondo esercizio dell'ultimo bilancio approvato. Per le spese ammesse opera, per ciascun programma, il limite mensile dei dodicesimi, considerando anche quelli non utilizzati nei mesi precedenti e depurando la base dagli impegni già assunti e dal FPV secondo la norma.

Sono sottratte al frazionamento le spese tassativamente regolate dalla legge, quelle non suscettibili di pagamento frazionato e quelle continuative necessarie a mantenere il livello dei servizi esistenti, impegnate a seguito della scadenza dei relativi contratti. L'eccezione va motivata sulla fattispecie: chiamare una spesa «utile» non basta. In mancanza dell'autorizzazione all'esercizio provvisorio, la gestione provvisoria ammette soltanto le operazioni nei limiti più restrittivi del comma 2, tra cui obbligazioni già assunte e operazioni necessarie a evitare danni patrimoniali certi e gravi.

### Debiti fuori bilancio: riconoscere non significa sanare tutto

Il Consiglio può riconoscere i debiti nelle categorie dell'art. 194 TUEL: sentenze esecutive; copertura dei disavanzi di consorzi, aziende speciali e istituzioni nei limiti prescritti; ricapitalizzazione delle società di capitali costituite per servizi pubblici locali nei limiti civilistici o di norme speciali; procedure espropriative o occupazioni d'urgenza per opere di pubblica utilità; acquisizioni di beni e servizi effettuate violando le regole di impegno, limitatamente all'utilità e all'arricchimento accertati nell'esercizio di funzioni e servizi dell'ente.

Il provvedimento deve individuare categoria, titolo, quantificazione e copertura, con istruttoria e parere dell'organo di revisione. Non è sufficiente constatare che è arrivata una fattura. Per esempio, una fornitura ordinata irregolarmente costa 8.000 euro, ma l'istruttoria dimostra utilità e arricchimento per l'ente soltanto per 6.000: la lettera e) non consente di riconoscere automaticamente tutti gli 8.000. Per la parte non riconoscibile rileva il rapporto previsto dall'art. 191, comma 4, con chi ha consentito la fornitura, nei suoi presupposti; eventuali responsabilità richiedono accertamento separato.

### Riequilibrio e dissesto

Il riequilibrio finanziario pluriennale dell'art. 243-bis affronta squilibri strutturali che possono provocare dissesto quando le misure ordinarie non bastano, attraverso un piano sottoposto a istruttoria e controllo. Non è una dilazione informale dei debiti. Il dissesto dell'art. 244 ricorre quando l'ente non riesce a garantire funzioni e servizi indispensabili oppure non può far fronte a debiti liquidi ed esigibili con gli strumenti previsti dagli artt. 193 e 194. Alla deliberazione consiliare seguono la gestione della massa pregressa affidata all'organo straordinario di liquidazione e il risanamento della gestione dell'ente secondo le rispettive competenze. Il piano di riequilibrio non consente di ignorare i presupposti che rendono necessaria la dichiarazione di dissesto.

'''+s[idx:]
s=replace(s,'### Caso ragionato — Dalla manutenzione al rendiconto','''### Quiz 8 — Risultato disponibile

Cassa 200, residui attivi 120, residui passivi 90, FPV 60; quote accantonate 80, vincolate 50 e destinate agli investimenti 20. Tutti gli importi sono in migliaia. Qual è la parte disponibile?

A. 200.
B. 170.
C. 80.
D. 20.

**Risposta corretta: D.** Prima si determina il risultato: 200 + 120 − 90 − 60 = 170. Poi si sottraggono 80 + 50 + 20: restano 20. A indica la cassa; B ignora la scomposizione; C non deriva dalla formula completa. Il FPV non va sottratto due volte.

### Quiz 9 — Ratifica urgente

La Giunta adotta il 20 dicembre una variazione urgente di competenza consiliare. Quale limite vale per la ratifica?

A. Il 31 dicembre dello stesso anno.
B. Sempre 60 giorni, anche oltre la fine dell'anno.
C. Il termine del rendiconto successivo.
D. Nessun termine, se il revisore è favorevole.

**Risposta corretta: A.** I 60 giorni sono limitati dal 31 dicembre. Il parere non sostituisce la ratifica e il rendiconto non sana la sua omissione. L'esempio presuppone una variazione adottabile in dicembre secondo la disciplina dell'art. 175: l'urgenza non rimuove i limiti oggettivi della variazione.

### Caso ragionato — Dalla manutenzione al rendiconto''')
s=replace(s,'in particolare l’art. 183 (impegno di spesa).','in particolare gli artt. 163, 175, 183, 186–188, 191, 193–194, 223, 227, 234–239, 243-bis e 244.')
p.write_text(s,encoding='utf8')
source='vol-02-contabilita-piao-verifica-2026-10-03';topic='vol-02-contabilita-piao-casi'
for n in (9,10):
 p=next(base.glob(f'{n:02d}-*.md'));s=p.read_text(encoding='utf8')
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M)
 s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M)
 for key,refs in [('source_refs',[f'sources/{source}.md']),('last_compiled_from',[f'wiki/sources/{source}.md',f'wiki/topics/{topic}.md'])]:
  for ref in refs:s=re.sub(rf'^({key}: \[)(.*)(\])$',lambda m:m[1]+m[2]+(', '+json.dumps(ref) if ref not in m[2] else '')+m[3],s,flags=re.M)
 p.write_text(s,encoding='utf8')
p=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');d=json.loads(p.read_text(encoding='utf8'))
for fid,ns,change,evidence in [('V02-12',[9],'PIAO istituito nel2021; caso50dipendenti e regime ANAC; PEG facoltativo sotto5000 e calendario ordinario.','Confronto DPR81/DM132/PNA2022, distinzione termini ordinari/proroghe e presentazione/approvazione.'),('V02-13',[9,10],'Calendario, FPV/FCDE numerici, formula risultato/scomposizione, variazioni e ratifica, revisori, esercizio provvisorio, debiti e crisi.','Risolti170totale/20disponibile e variante−10; quiz ratifica31dicembre; cinque categorie194 e caso8mila/6mila.')]:
 d['changes'][fid]={'files':[str(next(base.glob(f'{n:02d}-*.md'))).replace('\\','/') for n in ns],'change':change,'evidence':evidence,'status':'applicato'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
