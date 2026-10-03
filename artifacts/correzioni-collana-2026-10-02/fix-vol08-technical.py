from pathlib import Path
import re,json
B=Path('wiki/books/moduli/m-tr01-ict-trasformazione-digitale');A=Path('artifacts/correzioni-collana-2026-10-02')
def path(n):return next((B/'chapters').glob(f'{n:02}-*.md'))
def patch(n,fn):
 p=path(n);s=p.read_text(encoding='utf8');p.write_text(fn(s),encoding='utf8')
def addbefore(s,marker,content):
 assert marker in s,marker
 return s.replace(marker,content.strip()+'\n\n'+marker,1)
for p in (B/'chapters').glob('*.md'):
 s=p.read_text(encoding='utf8');fm,body=s.split('---',2)[1:];fm=re.sub(r'(?m)^review_required:.*$','review_required: true',fm);fm=re.sub(r'(?m)^draft_stage:.*$','draft_stage: revision-in-progress',fm);fm=re.sub(r'(?m)^status:.*$','status: revised_draft',fm);fm=re.sub(r'(?m)^updated_at:.*$','updated_at: 2026-10-03',fm)
 fm=fm.replace('source_refs: [','source_refs: ["sources/ict-rettifiche-specialistiche-2026-10-03", ',1).replace('topics: [','topics: ["ict-rettifiche-specialistiche-2026", ',1)
 body=re.sub(r'\n## Apparato di verifica dei nuclei\n.*?(?=\n## )','\n',body,flags=re.S)
 p.write_text('---'+fm+'---'+body,encoding='utf8')
patch(2,lambda s:s.replace("Per gli interi con segno, i sistemi moderni usano comunemente una rappresentazione che rende efficienti somma e sottrazione. Ai fini concorsuali è più importante comprenderne l'effetto: una sequenza di bit ha valore solo entro un formato dichiarato. Interpretare come senza segno un campo progettato con segno può produrre un risultato completamente diverso.","Gli interi con segno sono comunemente rappresentati in **complemento a due**. Con n bit l’intervallo è da −2^(n−1) a 2^(n−1)−1; senza segno è da 0 a 2^n−1. Su otto bit, +5 è `00000101`: invertendo i bit e aggiungendo uno si ottiene −5, `11111011`. La stessa sequenza letta senza segno vale 251. Il formato decide il significato. La somma 127+1 non è rappresentabile su otto bit con segno: nell’aritmetica modulare i bit diventano `10000000`, cioè −128, ma il comportamento concreto del linguaggio (errore, wraparound o altro) va distinto dal calcolo sui bit.").replace('segno, grandezza e precisione significativa','segno, esponente e significando').replace('Il modello consente di rappresentare numeri molto grandi e molto piccoli, ma non tutti i reali.', 'Per un numero binario normalizzato il modello è (−1)^s × 1.f × 2^e: 1,5 = 1,1₂ × 2^0. Esponente e significando hanno un numero finito di bit; valori subnormali, zeri e valori speciali seguono regole proprie del formato. Il modello consente di rappresentare numeri molto grandi e molto piccoli, ma non tutti i reali.'))
def alg(s):
 s=s.replace('La **complessità spaziale** descrive la crescita della memoria aggiuntiva.', 'La **complessità spaziale totale** comprende input e memoria usata dall’algoritmo; lo **spazio ausiliario** esclude l’input. In questi esercizi, quando si valuta memoria aggiuntiva, si dichiara espressamente lo spazio ausiliario.')
 s=s.replace("l'etichetta dice che il lavoro dominante cresce linearmente", "il solo limite O(n) non dice che il lavoro cresca esattamente in modo lineare: anche un costo costante è O(n). Per un ordine stretto si usa Theta(n), con limite superiore e inferiore dello stesso ordine")
 s=s.replace("La complessità spaziale considera la memoria aggiuntiva rispetto all'input.", "Lo spazio ausiliario considera la memoria aggiuntiva rispetto all’input. Una scansione di un array di n elementi con un solo contatore usa Theta(n) spazio totale e Theta(1) ausiliario.")
 s=s.replace('Se `n` raddoppia, un algoritmo lineare', 'Nel modello T(n)=a·n, a>0, o T(n)=a·n², considerando il termine dominante, se `n` raddoppia, un algoritmo lineare')
 s=re.sub(r'(?m)^.*materiali didattici universitari.*$', '- Pat Morin, *Open Data Structures*, edizione Python, § 1.3 e capitoli sulle strutture: notazione asintotica, ricerca e organizzazione dei dati.',s)
 s=s.replace('Un algoritmo O(n²)', 'Un algoritmo con termine dominante a·n² (a positivo)')
 return s
patch(3,alg)
def db(s):
 s=s.replace('id_ufficio FK → Ufficio.id_ufficio','id_ufficio NOT NULL FK → Ufficio.id_ufficio',1).replace('Assegnazione(id_pratica, id_dipendente, nome_dipendente, ruolo, nome_ufficio)','Assegnazione(id_pratica, id_dipendente, nome_dipendente, ruolo, id_ufficio, nome_ufficio)')
 return addbefore(s,'## N-TR01-04-05', '''### Livelli di isolamento e anomalie

Una **lettura sporca** usa un dato non ancora confermato da un’altra transazione. Una **lettura non ripetibile** trova cambiato un valore già letto, dopo il commit altrui. Un **phantom** cambia l’insieme delle righe che soddisfano una query. Un’anomalia di serializzazione produce un risultato incompatibile con qualsiasi esecuzione seriale delle transazioni concluse.

| Livello SQL | Garanzie minime rispetto alle letture | Serializzazione |
| --- | --- | --- |
| Read Uncommitted | Può consentire tutte e tre le anomalie | Non garantita |
| Read Committed | Esclude letture sporche | Non garantita |
| Repeatable Read | Esclude sporche e non ripetibili; phantom ammessi dal minimo SQL | Non garantita |
| Serializable | Esclude tutte e tre | Equivalenza a un ordine seriale |

PostgreSQL 18 implementa Read Uncommitted come Read Committed; il suo Repeatable Read usa snapshot e impedisce anche i phantom. Può comunque richiedere retry, e non equivale a Serializable. A quest’ultimo livello l’applicazione deve saper ripetere l’intera transazione abortita per un conflitto di serializzazione, senza duplicare effetti esterni.

**Sequenza svolta.** Saldo iniziale 100. T1, in Read Committed, legge 100. T2 aggiorna a 80 e fa commit. T1 legge di nuovo e ottiene 80: lettura non ripetibile, senza lettura sporca. In Repeatable Read di PostgreSQL, con snapshot già fissato dalla prima lettura, T1 continua a vedere 100. Se invece T2 avesse solo aggiornato senza commit, la lettura di 80 da T1 sarebbe sporca, esclusa già da Read Committed. Non confondere la stabilità delle letture con la correttezza di una regola che coinvolge più righe e transazioni.''')
patch(4,db)
patch(5,lambda s:s.replace('Una workstation invia una richiesta web a un server in un’altra rete.', 'Una workstation invia una richiesta HTTP/1.1 non cifrata a un server in un’altra rete; l’esempio isola l’incapsulamento TCP/IP.').replace('Lo switch inoltra il frame nella rete locale; il router instrada il pacchetto IP verso una rete diversa.', 'Lo switch inoltra il frame nella rete locale; il router instrada il pacchetto IP verso una rete diversa. HTTP/2 usa anch’esso TCP; HTTP/3 usa QUIC su UDP, perciò questa sequenza non si applica indistintamente a tutte le versioni.'))
def api(s):
 s=s.replace('| regressione | funzioni già valide dopo una modifica | suite rieseguita su nuova release |','\nLa regressione è una finalità trasversale, eseguibile a più livelli: riesamina comportamenti già validi dopo una modifica.')
 s=s.replace('**Soluzione:** definire operazione, carico, indicatore, valore obiettivo e finestra di misurazione. Senza questi elementi, «veloce» non produce un criterio di accettazione.', '**Soluzione svolta, valori ipotetici:** su ambiente di collaudo dichiarato, con 100 utenti concorrenti e un milione di pratiche, il 95° percentile delle risposte valide di `GET /v1/pratiche/{id}` deve essere al massimo 800 ms durante 30 minuti a carico stabile; errori inferiori allo 0,5%. Il test genera quel carico, conserva latenza per richiesta ed errori e verifica entrambe le soglie. Non scarta le richieste fallite per migliorare artificialmente il percentile. Questi valori sono requisiti dell’esercizio, non soglie imposte alla PA.')
 return addbefore(s,'### Errori e descrizione formale', '''### Un contratto HTTP concreto

REST combina separazione client/server, richieste senza dipendere da sessione applicativa sul server, cache dichiarata, interfaccia uniforme e sistema a livelli; il code-on-demand è opzionale. L’interfaccia uniforme comprende identificazione delle risorse, manipolazione mediante rappresentazioni, messaggi autoesplicativi e collegamenti che guidano le transizioni. Usare JSON non basta a soddisfare questi vincoli. Il contratto ridotto seguente illustra una API HTTP orientata a risorse, senza pretendere di dimostrare da solo un’intera architettura REST.

Il fruitore autenticato chiede `GET /v1/pratiche/42`, con `Accept: application/json` e un token autorizzato alla lettura. Il servizio verifica anche che il soggetto possa consultare **quella** pratica: conoscere 42 non autorizza l’accesso.

```json
{"id":42,"stato":"IN_ISTRUTTORIA","versione":3,
 "links":{"self":"/v1/pratiche/42"}}
```

| Esito | Codice | Contratto |
| --- | --- | --- |
| Lettura autorizzata | 200 | Oggetto con id intero positivo, stato enumerato, versione intera |
| Credenziali mancanti/non valide | 401 | Richiesta di autenticazione secondo lo schema |
| Identità valida, permesso assente | 403 | Accesso negato; nessun dato della pratica |
| Identificativo malformato | 400 | Errore di validazione, senza stack trace |
| Risorsa assente | 404 | Esito di assenza secondo la politica di visibilità |
| Dipendenza temporaneamente indisponibile | 503 | Errore temporaneo; retry limitato secondo contratto |

Esempio di errore: `{"codice":"ACCESSO_NEGATO","requestId":"r-17"}`. Il campo di correlazione è registrato senza token o dati superflui. Il test confronta 200 per il soggetto assegnatario e 403 per un altro soggetto autenticato. Una politica che maschera l’esistenza con 404 va dichiarata e testata in modo uniforme. Rinominare `stato` rompe i fruitori: `/v2` o una migrazione concordata conserva la compatibilità. La risposta non contiene campi sanitari o fiscali non necessari. Per aggiornamenti concorrenti si definisce separatamente il controllo della versione, evitando che una lettura precedente autorizzi a sovrascrivere modifiche successive.''')
patch(6,api)
def cyber(s):
 marker='STRIDE è una tassonomia possibile: spoofing, tampering, repudiation, information disclosure, denial of service ed elevation of privilege. Non è l’unico metodo e non deve diventare un elenco scollegato dal sistema.'
 s=s.replace(marker,marker+'''\n\n| Categoria e significato | Minaccia al portale PA | Controllo motivato |
| --- | --- | --- |
| Spoofing: impersonificazione | Accesso come istruttore con credenziali sottratte | MFA e recupero account controllato |
| Tampering: alterazione | Modifica non autorizzata dell’importo | Autorizzazione e controlli di integrità |
| Repudiation: disconoscimento | Operazione negata da chi l’ha compiuta | Audit trail integro con identità e tempo |
| Information disclosure: divulgazione | Fascicolo visibile a un altro utente | Autorizzazione per oggetto e minimizzazione |
| Denial of service: indisponibilità | Richieste saturano il servizio | Limiti proporzionati e capacità/resilienza |
| Elevation of privilege: aumento dei privilegi | Utente ordinario diventa amministratore | Separazione ruoli e controllo dei privilegi |
''')
 return s.replace("**Risposta corretta: risposta aperta.** Lo scenario deve separare minaccia, vulnerabilità, evento e impatto; l'esercizio sui controlli deve motivare come ciascuna misura riduce probabilità o conseguenze.",'''**Soluzione 6.** Asset: fascicoli del portale. Minaccia: un attore tenta di leggere pratiche altrui. Vulnerabilità: l’API controlla il login ma non l’assegnazione della pratica. Evento: l’attore cambia l’identificativo e ottiene un fascicolo non autorizzato. Impatto: divulgazione di dati e danno alle persone; il rischio combina probabilità dello sfruttamento e conseguenze, senza attribuire un punteggio privo di scala.

**Soluzione 7.** Preventivo: autorizzazione per oggetto sul server, con test fra due utenti distinti. Detective: alert su sequenze anomale di richieste, da validare senza registrare il contenuto dei fascicoli. Compensativo, mentre si corregge il difetto: sospendere l’endpoint esposto e gestire le richieste tramite canale autenticato e operatore autorizzato, preservando un servizio minimo. La misura temporanea ha responsabile, termine e prova di chiusura; un semplice banner non compensa l’assenza di autorizzazione.''')
patch(8,cyber)
for n in [10,11,12]:
 def method(s):
  s=re.sub(r'(?m)^- \*\*B — [^:]+:\*\*.*$', '- **B — Bando:** individua profilo, programma e formato della prova; ricava il caso d’uso richiesto.',s)
  s=re.sub(r'(?m)^- \*\*A — Attori:\*\*.*$', '- **A — Aree:** collega le materie tecniche alle responsabilità dei soggetti coinvolti.',s)
  s=s.replace('**N — Nodi:**','**N — Nuclei:**')
  s=re.sub(r'(?m)^- \*\*D — Documenti:\*\*.*$', '- **D — Diario:** registra errori, motivazioni e correzioni; conserva i documenti utili a ricostruire il ragionamento.',s)
  return s.replace('usare interno','uso interno')
 patch(n,method)
patch(9,lambda s:s.replace('nel ignorare','nell’ignorare'))
print('Correzioni tecniche e apparati applicati; normativa e laboratorio in corso.')
