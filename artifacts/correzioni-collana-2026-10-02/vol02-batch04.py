from pathlib import Path
import re,json
base=Path('wiki/books/moduli/m-fl01-comuni-unioni/chapters')
def rep(s,a,b):
 assert a in s,a[:70]
 return s.replace(a,b)
p=next(base.glob('11-*.md'));s=p.read_text(encoding='utf8')
a=s.index('| Profilo | IMU | TARI |');b=s.index('### Altri tributi',a)
s=s[:a]+'''| Elemento | IMU | TARI |
| --- | --- | --- |
| Presupposto | Possesso di fabbricati, aree fabbricabili e terreni, secondo le definizioni di legge | Possesso o detenzione di locali e aree scoperte suscettibili di produrre rifiuti urbani |
| Soggetti | Proprietario o titolare di usufrutto, uso, abitazione, enfiteusi o superficie; regole specifiche per concessionario demaniale e locatario finanziario | Possessore o detentore; in caso di detenzione temporanea non superiore a sei mesi nello stesso anno solare, il possessore a titolo di proprietà o diritto reale indicato dalla legge |
| Grandezza rilevante | Valore imponibile: per i fabbricati iscritti, rendita rivalutata e moltiplicatore di categoria; per le aree, valore venale; per i terreni, reddito dominicale rivalutato e moltiplicatore | Superficie imponibile, durata e categoria di utenza; per le utenze domestiche rileva anche il numero degli occupanti secondo la disciplina applicabile |
| Esclusioni e riduzioni | Abitazione principale ordinaria esclusa, salvo A/1, A/8, A/9; altre esenzioni o riduzioni richiedono i presupposti di legge | Escluse aree scoperte pertinenziali/accessorie non operative e parti comuni condominiali non detenute in esclusiva; riduzioni legali e regolamentari da distinguere |
| Atto locale | Regolamento e aliquote nei limiti statali, con pubblicazione prescritta | Regolamento, piano economico-finanziario e tariffe secondo legge e regolazione ARERA |

L'abitazione principale IMU richiede che il possessore vi abbia **residenza anagrafica e dimora abituale**. Dopo la sentenza costituzionale 209/2022 non si impone che vi risieda e dimori anche tutto il nucleo familiare. Non basta tuttavia spostare formalmente la residenza: la dimora deve essere effettiva. «Prima casa» nelle imposte sull'acquisto e «abitazione principale» IMU sono nozioni diverse. Le pertinenze ammesse sono C/2, C/6 e C/7, al massimo una per categoria. Tra le altre fattispecie da conoscere vi sono la riduzione del 50% della base per immobili di interesse storico o artistico e per fabbricati inagibili/inabitabili e non utilizzati alle condizioni richieste; esenzioni per determinati terreni agricoli e immobili di enti non commerciali hanno presupposti specifici, non derivano dal solo nome del proprietario.

**Calcolo IMU didattico.** Un appartamento A/2, diverso dall'abitazione principale, ha rendita catastale di 500 euro. Il proprietario lo possiede al 100% per tutto l'anno; non ricorrono agevolazioni. La base è 500 × 1,05 × 160 = **84.000 euro**. Assumendo per il solo esercizio un'aliquota dell'1%, l'imposta annua è **840 euro**. L'1% non è un'aliquota nazionale da memorizzare: nella pratica si applica quella vigente e pubblicata per il Comune e l'anno. Anche il moltiplicatore160 dipende dalla categoria scelta. Il normale inquilino non diventa soggetto IMU per il solo contratto di locazione, mentre può essere tenuto alla TARI.

Per la TARI la base non è il valore catastale dell'immobile. Nel regime ordinario si parte dalla superficie calpestabile secondo le regole vigenti, distinguendo utenze domestiche e non domestiche e applicando quote fisse e variabili. Una famiglia non calcola quindi la tassa moltiplicando la rendita per l'aliquota IMU. Non usare personalmente il cassonetto non elimina da solo il presupposto. Le riduzioni per mancato o gravemente irregolare servizio e per zone non servite seguono le condizioni legali; agevolazioni sociali e ulteriori riduzioni richiedono la disciplina pertinente. La tariffa corrispettiva prevista nei sistemi di misurazione puntuale, quando istituita nei presupposti del comma668, va distinta dalla TARI tributaria.

**Caso soggettivo.** Un alloggio è concesso in locazione per l'intero anno: di regola il proprietario resta soggetto IMU e il conduttore è soggetto TARI. Se la detenzione è temporanea per quattro mesi nello stesso anno solare, la TARI ricade sul possessore qualificato ai sensi del comma643. Il diverso esito dipende dalla durata e dal titolo, non dalla residenza anagrafica da sola.

'''+s[b:]
anchor='### Caso ragionato — Credito TARI non riscosso'
s=rep(s,anchor,'''### Caso datato — Decadenza e prescrizione

Il Comune controlla nell'ottobre2026 una TARI2025 dichiarata correttamente ma non versata alla scadenza del 30settembre2025. Per esercitare il calcolo si assumono assenti proroghe e sospensioni speciali.

**Accertamento.** Il comma161 dell'art.1 della legge296/2006 richiede la notifica dell'avviso motivato entro il 31dicembre del quinto anno successivo a quello in cui il versamento è stato o doveva essere effettuato: il termine ordinario del caso è **31dicembre2030**. Il calcolo non parte dal giorno in cui l'ufficio scopre l'omissione. Se si contestasse invece una dichiarazione autonomamente dovuta nel2026 e omessa, il riferimento sarebbe quell'adempimento e il termine ordinario diventerebbe **31dicembre2031**. La data futura è il risultato della regola attuale, da ricontrollare se intervengono nuove disposizioni.

**Riscossione.** La prescrizione riguarda il diritto di credito e la sua mancata attivazione: per tributi periodici come IMU e TARI il termine è, in via ordinaria, quinquennale. Vanno ricostruiti decorrenza, valide notifiche, atti interruttivi, sospensioni e contenzioso; il 31dicembre del quinto anno non è una formula universale della prescrizione. Una mera annotazione interna non interrompe il termine verso il debitore. La mancata impugnazione dell'avviso non trasforma automaticamente il credito in un credito con prescrizione decennale: il giudicato segue la distinta regola dell'art.2953 codice civile.

**Esito operativo.** Nell'ottobre2026 l'ufficio non può dichiarare decaduta la pretesa solo perché è trascorso un anno dal pagamento omesso. Deve predisporre l'atto previsto, documentare la notifica e alimentare lo scadenzario. Un sollecito non rimedia a un accertamento notificato quando il relativo potere è già decaduto. Prima di recuperare una posizione risalente, lo scadenzario deve dunque contenere due verifiche separate: tempestività dell'accertamento e prescrizione del credito.

### Caso ragionato — Credito TARI non riscosso''')
s=rep(s,'- Legge 27 dicembre 2013, n. 147, disciplina TARI,','- Legge 27 dicembre 2006, n. 296, art. 1, commi 161 e seguenti, per accertamento locale; codice civile, artt. 2948 e 2953, per prescrizione e giudicato.\n- Legge 27 dicembre 2013, n. 147, art. 1, commi 641–668, disciplina TARI,')
p.write_text(s,encoding='utf8')
p=next(base.glob('12-*.md'));s=p.read_text(encoding='utf8')
s=rep(s,'beni, servizi e lavori di manutenzione da operatori abilitati','beni, servizi e lavori, sia di costruzione sia di manutenzione, da operatori abilitati')
s=rep(s,'La nomina, i requisiti e i compiti si leggono','Il RUP è nominato nel primo atto di avvio dell’intervento pubblico: non si attende la scelta dell’affidatario. La nomina, i requisiti e i compiti si leggono')
s=rep(s,'All’esame conviene distinguere il contenuto giuridico, la decisione di contrarre, dal veicolo amministrativo con cui il Comune lo formalizza.', '''Il raccordo comunale è l'art.192 TUEL: la determinazione del responsabile del procedimento di spesa indica fine, oggetto, forma e clausole essenziali del contratto, modalità di scelta del contraente e ragioni della scelta. L'art.17 del Codice e l'art.192 si coordinano: non impongono due atti duplicati se un unico provvedimento contiene tutti gli elementi richiesti. Nell'affidamento diretto la decisione può individuare anche contraente, importo, ragioni e requisiti secondo l'art.17, comma2.

Per esempio, nella fornitura di materiali di consumo per la biblioteca: fine è garantire il servizio, oggetto sono quantità e caratteristiche richieste, forma è lo scambio elettronico ammesso dall'art.18, clausole sono consegna, prezzo e verifica; la modalità è l'affidamento consentito dall'importo, con motivazione sull'operatore e sulla congruità. «Acquisto sul MePA» indica lo strumento digitale, non esaurisce la motivazione né identifica da solo la procedura.''')
s=rep(s,'Controlla contratto esistente, programmazione, stanziamento e imputazione. Individua il RUP e distingue i compiti del servizio finanziario.','Con il primo atto di avvio si nomina il RUP. L’ufficio controlla contratto esistente, programmazione, stanziamento e imputazione e distingue i compiti del servizio finanziario.')
p.write_text(s,encoding='utf8')
p=next(base.glob('14-*.md'));s=p.read_text(encoding='utf8')
s=rep(s,'bando normativo applicabile','quadro normativo applicabile')
s=rep(s,'Capitolo 10 su bilancio','Capitolo 9 su programmazione e bilancio')
s=rep(s,'- 12-16: livello buono, passare a simulazione mista;\n- oltre 16: mantenimento e orale.','- 12-14: livello buono, passare a simulazione mista;\n- 15-16: consolidamento e prova orale.')
s=s.replace('RUP o del responsabile del progetto secondo il caso','RUP, già nominato nel primo atto di avvio dell’intervento').replace('RUP o responsabile del progetto secondo l’organizzazione','il RUP fin dal primo atto di avvio dell’intervento')
s=rep(s,'3. competenza del responsabile;\n4. copertura nel bilancio;\n5. scelta della procedura o dello strumento di affidamento;\n6. individuazione del RUP, già nominato nel primo atto di avvio dell’intervento;','3. competenza del responsabile e nomina del RUP nel primo atto di avvio;\n4. copertura nel bilancio;\n5. scelta della procedura o dello strumento di affidamento;\n6. verifica dei requisiti e della motivazione della scelta;')
p.write_text(s,encoding='utf8')
source='vol-02-tributi-procurement-verifica-2026-10-03';topic='vol-02-tributi-atti-comunali-applicazioni'
for n in (11,12,14):
 p=next(base.glob(f'{n:02d}-*.md'));s=p.read_text(encoding='utf8')
 s=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',s,flags=re.M);s=re.sub(r'^review_required:.*$','review_required: true',s,flags=re.M)
 for key,refs in [('source_refs',[f'sources/{source}.md']),('last_compiled_from',[f'wiki/sources/{source}.md',f'wiki/topics/{topic}.md'])]:
  for ref in refs:s=re.sub(rf'^({key}: \[)(.*)(\])$',lambda m:m[1]+m[2]+(', '+json.dumps(ref) if ref not in m[2] else '')+m[3],s,flags=re.M)
 p.write_text(s,encoding='utf8')
p=Path('artifacts/correzioni-collana-2026-10-02/VOL-02-changes.json');d=json.loads(p.read_text(encoding='utf8'))
for fid,ns,change,evidence in [('V02-14',[11],'Schede IMU/TARI su presupposti, soggetti, base, esclusioni/riduzioni; caso datato e distinzione decadenza/prescrizione.','Calcolo840su84mila con aliquota ipotetica; locazione4mesi vs12; termini2030/2031 distinti per adempimento.'),('V02-15',[12],'MePA costruzione/manutenzione, art192TUEL coordinato con17/18Codice e caso concreto.','Consip2022 e pagina mercato; controllo finalità/oggetto/forma/clausole/modalità/motivazione.'),('V02-19',[14],'Fasce0–16, rinvio programmazione09, quadro normativo e RUP nel primo atto.','Otto criteri0–2: fasce0–6,7–11,12–14,15–16 coprono dominio senza sovrapposizioni.')]:
 d['changes'][fid]={'files':[str(next(base.glob(f'{n:02d}-*.md'))).replace('\\','/') for n in ns],'change':change,'evidence':evidence,'status':'applicato'}
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
