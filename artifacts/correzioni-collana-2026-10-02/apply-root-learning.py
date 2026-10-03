from pathlib import Path
import re,json,hashlib

root=Path('wiki/books/il-metodo-bando/chapters')
source='sources/vol-01-esempi-logica-inglese-metodo-2026-10-02.md'
changed={}
def edit(slug,ids,replacements):
    p=root/(slug+'.md'); t=p.read_text(encoding='utf8')
    for old,new in replacements:
        if old not in t: raise ValueError(f'Missing anchor {slug}: {old[:80]}')
        t=t.replace(old,new,1)
    t=re.sub(r'^updated_at:.*$', 'updated_at: 2026-10-02',t,flags=re.M)
    t=re.sub(r'^review_required:.*$', 'review_required: true',t,flags=re.M)
    t=re.sub(r'^draft_stage:.*$', 'draft_stage: editorial-review',t,flags=re.M)
    for key in ['source_refs','last_compiled_from']:
        line=next((l for l in t.splitlines() if l.startswith(key+':')),None)
        if line and source not in line:t=t.replace(line,line[:-1]+', "'+source+'"]',1)
    p.write_text(t,encoding='utf8')
    for id in ids:changed[id]=str(p).replace('\\','/')

edit('inglese-concorsuale-essenziale',['V01-30','V01-31','V01-32'],[
('Per i profili generalisti, la preparazione efficace si colloca di solito tra A2, B1 e B2 operativo.', 'Questo capitolo offre una base di ripasso: non equivale a un corso completo né al conseguimento di un livello QCER. Se il bando richiede B1 o B2, occorre allenare tutte le abilità richieste con materiali graduati di quel livello.'),
('Copri le domande statisticamente più probabili.', 'Costruisci le basi per affrontare completamenti e comprensione.'),
('I dati ricorrenti sulle banche di domande mostrano una gerarchia netta. Il candidato deve partire dai formati più richiesti, non dagli argomenti che preferisce.', 'La tabella propone un ordine didattico di ripasso, non una stima statistica della frequenza nei concorsi. Adattalo alle prove ufficiali disponibili e al programma del tuo bando.'),
('I tempi verbali sono il secondo blocco più richiesto.', 'I tempi verbali sono un blocco centrale del ripasso.'),
('| it | it | its | its |', '| it | it | its | di norma non usato da solo; vedi `its own` |'),
('### Relativi', 'Il possessivo `its` accompagna normalmente un nome: `The office changed its address`. Non costruire `This address is its` sul modello di `This document is mine`. Esiste l’uso con `own`, per esempio `The system has rules of its own`. Non confondere `its` con `it’s`, contrazione di `it is` o `it has`.\n\n### Relativi'),
('open / opens / is open', 'open / opens / opening'),
('| 9 | Do you have ___ questions? | some / any / much |', '| 9 | Do you have ___ questions? | many / much / a |'),
('| 10 | If you submit the form late, it ___ rejected. | is / will be / was |', '| 10 | If you submit the form late tomorrow, it ___ rejected. | will / will be / will being |'),
('Soluzioni: 1 `opens`; 2 `sent`; 3 `bring`; 4 `will be`; 5 `since`; 6 `much`; 7 `who`; 8 `by`; 9 `any`; 10 `will be`.', '''**Soluzioni commentate**

1. `opens`: abitudine, present simple alla terza persona singolare. `Opening` da solo non costituisce il predicato.
2. `sent`: `yesterday` colloca l’azione in un passato concluso.
3. `bring`: dopo `must` occorre la forma base senza `to`.
4. `will be`: futuro passivo, `will be published`.
5. `since`: indica il punto iniziale; `for` introdurrebbe una durata.
6. `much`: `time` è qui non numerabile; `many` e `few` richiedono un plurale numerabile.
7. `who`: pronome relativo riferito alla persona che ha risposto.
8. `by`: `by email` indica il mezzo di comunicazione.
9. `many`: `questions` è plurale numerabile; `much` non è adatto, `a` richiede un singolare.
10. `will be`: la conseguenza futura è espressa al passivo. `Will rejected` e `will being rejected` sono costruzioni errate.'''),
('Per il candidato medio, la soglia più utile è questa: devi capire un breve testo d’ufficio, riconoscere la frase grammaticalmente corretta e rispondere con frasi semplici. È meglio una frase lineare e corretta che una frase ambiziosa piena di errori.', 'Il primo traguardo di questo capitolo è capire un breve testo d’ufficio, riconoscere una frase corretta e formulare risposte semplici. È una base da confrontare con la prova richiesta: B2 comprende anche testi complessi, argomentazione e interazione sufficientemente fluida. Il livello non si ricava dal numero di regole memorizzate.'),
('### Present perfect', '''Per formare il passato, molti verbi regolari aggiungono `-ed`: `work → worked`. I verbi irregolari hanno una forma propria: `send → sent`, `go → went`, `write → wrote`. Nelle domande e nelle negazioni con `did` il verbo torna alla forma base: `Did she send the form?`, `She did not send the form`. Con `be` si usano invece `was/were`: `Was the office open?`, `The offices were not open`.

**Controllo rapido:** trasforma `They submitted the documents yesterday` in domanda e negazione. Soluzioni: `Did they submit the documents yesterday?` e `They did not submit the documents yesterday`. L’errore da evitare è `did submitted`.

### Present perfect'''),
('## 10. Numeri, date e ordinali', '''### Comparativi e superlativi

Il comparativo confronta due termini; il superlativo colloca un elemento rispetto a un gruppo. Gli aggettivi brevi usano spesso `-er/-est`: `fast → faster → the fastest`. Quelli più lunghi usano normalmente `more/the most`: `accurate → more accurate → the most accurate`. Sono irregolari `good → better → the best` e `bad → worse → the worst`. Il secondo termine è introdotto da `than`: `This form is shorter than the previous one`.

Per l’uguaglianza usa `as ... as`: `This office is as busy as the other one`. Per una quantità minore, `fewer` accompagna nomi plurali numerabili e `less` quantità non numerabili: `fewer errors`, `less time`.

**Esercizio:** completa `The new procedure is ___ (simple) than the old one` e `This is the ___ (good) solution`. Soluzioni: `simpler`, perché confronta due procedure; `best`, perché seleziona la soluzione migliore nel gruppo. Non usare `more simpler` o `the most best`.

## 10. Numeri, date e ordinali''')])

edit('logica-comprensione-ragionamento',['V01-33'],[
('| O A o B | uno solo dei due | ammettere entrambi |','| O A o B, ma non entrambi | esattamente uno dei due | ammettere entrambi |'),
('Una condizione **sufficiente** basta a produrre un effetto. Una condizione **necessaria** deve esserci, ma da sola non basta.', 'Una condizione **sufficiente** basta, secondo la premessa, a garantire la conseguenza. Una condizione **necessaria** deve esserci, ma non è necessariamente sufficiente: può anche esserlo, se una seconda premessa lo stabilisce. Per esempio, per un numero intero, essere divisibile per 2 è condizione necessaria e sufficiente per essere pari.'),
('Nel linguaggio dei quiz, “solo se” è una sirena.', 'Gli esempi della tabella sono premesse astratte del quesito, non regole giuridiche complete sull’ammissione o sull’assunzione. In una procedura reale possono occorrere altri requisiti.\n\nLa parola “o”, da sola, nella logica proposizionale ammette che siano veri entrambi i termini. Anche la ripetizione italiana “o ... o ...” va interpretata nel contesto: l’esclusione è certa se il testo precisa “uno solo”, “alternativamente” oppure “ma non entrambi”. Se sono richiesti documento A o documento B e non è vietato presentarli entrambi, la disgiunzione è inclusiva.\n\nNel linguaggio dei quiz, “solo se” è una sirena.')])

edit('metodo-di-studio-per-concorsi',['V01-34'],[
('Una distribuzione utile è questa:', 'Un esempio di distribuzione su 60 ore complessive è questo:'),
('| Fase | Quota indicativa | Obiettivo |','| Fase | Quota e ore | Obiettivo |'),
('| Setup | 10-15% |','| Setup | 10% · 6 ore |'),
('| Apprendimento base | 40-45% |','| Apprendimento base | 40% · 24 ore |'),
('| Consolidamento | 25-30% |','| Consolidamento | 30% · 18 ore |'),
('| Rifinitura | 15-20% |','| Rifinitura | 20% · 12 ore |'),
('Queste percentuali non sono una legge. Servono a evitare due errori:', 'Le quote sommano al 100% e le ore a 60. Sono un esempio da adattare: se aumenti una fase, riduci le altre mantenendo invariato il totale. Le attività possono alternarsi durante le settimane; la tabella non impone di rinviare ogni quiz alla fine della lettura. Serve a evitare due errori:')])

edit('diario-degli-errori',['V01-42'],[
('| Memoria | Sapevi il tema ma non ricordavi dato, sequenza o definizione |','| Conoscenza/recupero | Non avevi studiato il punto, oppure lo avevi studiato ma non lo ricordavi; annota quale dei due casi ricorre |'),
('La categoria decide il rimedio.', 'La categoria decide il rimedio. All’interno di conoscenza/recupero distingui **lacuna** (il concetto non era stato appreso: serve studiarlo con un esempio) e **mancato recupero** (lo sapevi ma non lo richiami: servono domande a distanza e ripasso). Una flashcard non sostituisce la prima comprensione.'),
('Marta fa 50 quiz di diritto amministrativo. Ne sbaglia 14.', 'Marta affronta 50 quiz di diritto amministrativo: 36 risposte corrette, 12 errate e 2 omesse.'),
('Marta non deve “studiare tutto di più”. Deve correggere i pattern.', 'Le cinque voci descrivono 14 quesiti problematici, dei quali 12 sbagliati e 2 non risposti. Con +1 per risposta corretta, −0,25 per errore e 0 per omissione, il punteggio è 36 − (12 × 0,25) = **33 punti su 50**. Le corrette sono il 72% dei quesiti complessivi (36/50) e il 75% delle risposte date (36/48).\n\nMarta non deve “studiare tutto di più”. Deve correggere i pattern. I dettagli isolati restano nel programma: li riprenderà dopo le lacune ricorrenti, senza considerarli esclusi.'),
('Le soglie sono segnali di lavoro, non voti assoluti:', 'Per confrontare settimane diverse, mantieni lo stesso denominatore e batterie simili per argomento, difficoltà, tempo e penalità; registra separatamente le omissioni. Un aumento su quiz già memorizzati non dimostra da solo un miglioramento su quesiti nuovi. Le soglie sono segnali di lavoro, non voti assoluti:')])

edit('la-prova-a-quiz',['V01-35'],[
('Solo alla fine la banca dati diventa simulazione.', 'Dopo le prime basi, affianca allo studio della banca dati simulazioni progressive; rendile complete nella fase di consolidamento.'),
('In prova non devi affrontare tutte le domande nello stesso modo. Usa tre giri.', 'Se il sistema consente di tornare alle domande precedenti, puoi organizzare la prova in tre giri. Se ogni risposta è definitiva o l’ordine è vincolato, applica invece un limite di tempo a ogni quesito e decidi prima di proseguire.'),
('Segna la domanda e torna dopo. Il salto è utile solo se esiste un secondo giro.', '''Segna la domanda e torna dopo, se la procedura lo consente. Il salto è utile solo se esiste un secondo giro.

### Penalità: calcolare il valore atteso

Il **valore atteso** è il punteggio medio teorico di una scelta ripetuta in condizioni comparabili. Non garantisce il risultato della singola risposta. Indica con **G** il premio per una risposta corretta, con **P** la penalità sottratta per un errore e con **p** la probabilità di rispondere correttamente. Se l’omissione vale zero:

**E = p × G − (1 − p) × P**

Rispondere ha valore atteso positivo quando **p > P / (G + P)**. La formula assume G positivo e P non negativo. Se il bando assegna un punteggio anche all’omissione, confronta E con quel punteggio, anziché con zero.

**Esempio svolto.** Un quiz assegna +1 per la risposta corretta, −0,25 per quella errata e 0 per l’omissione. La soglia è 0,25/1,25 = **20%**. Con quattro alternative davvero equiprobabili, p = 25%: E = 0,25 × 1 − 0,75 × 0,25 = **+0,0625 punti**. La sola presenza di una penalità, quindi, non rende sempre conveniente omettere.

Se la penalità sale a −0,50, lasciando invariati premio e omissione, la soglia diventa 0,50/1,50 = **33,33…%**. Con quattro alternative E = 0,25 − 0,375 = **−0,125**; con due alternative equiprobabili rimaste dopo un’esclusione fondata, E = 0,50 − 0,25 = **+0,25**.

La scelta concreta richiede altri due controlli. Primo: l’eliminazione di un’opzione deve avere una ragione; sentirsi sicuri non rende esatta la stima di p. Secondo: spendere due minuti per un piccolo guadagno atteso può sottrarre tempo a una risposta che sai risolvere. Inoltre massimizzare il punteggio medio e massimizzare la probabilità di superare una soglia non sono sempre lo stesso obiettivo. Se hai già un punteggio certo pari alla soglia, un’ultima risposta rischiosa potrebbe farti scendere sotto: il valore atteso positivo, da solo, non decide la strategia.

### Verifica del calcolo

**1. Con +1, −0,50 e omissione 0, restano tre alternative equiprobabili. Quanto vale E?**

A. +0,50. B. 0. C. −0,50. D. +1.

**Soluzione: B.** Un terzo di probabilità di guadagnare 1 e due terzi di perdere 0,50 danno 1/3 − 1/3 = 0. Non hai un vantaggio medio sul punteggio dell’omissione; il tempo e l’obiettivo di soglia restano rilevanti.

**2. Un valore atteso positivo assicura punti sul singolo quesito?**

A. Sì, se le opzioni sono quattro. B. Sì, se hai eliminato un distrattore. C. No: descrive una media teorica, mentre una risposta può essere errata. D. No, perché le penalità annullano sempre il premio.

**Soluzione: C.** La risposta singola produce il premio o la penalità previsti; non produce il valore medio E. La D è falsa: il bilancio dipende dalle probabilità e dai valori assegnati.

**Caso rapido.** Su cinque quesiti con +1/−0,25/0 ottieni tre corrette, un errore e un’omissione. Punteggio: 3 − 0,25 = **2,75**. Rispondere all’ultimo quesito con p stimata pari a 50% darebbe un incremento medio di 0,50 − 0,125 = **0,375**, ma gli esiti effettivi sarebbero 3,75 oppure 2,50. Distingui sempre punteggio realizzato, previsione media e obiettivo da raggiungere.''')])

for topic in ['inglese-concorsuale','logica-concorsuale','metodo-di-studio','diario-errori','prova-a-quiz']:
    p=Path('wiki/topics')/(topic+'.md')
    with p.open('a',encoding='utf8') as out:out.write('\n\n## Correzioni didattiche del 2 ottobre 2026\n\n[[sources/vol-01-esempi-logica-inglese-metodo-2026-10-02]] consolida le correzioni di quiz e possessivi, limiti QCER, condizioni logiche, distribuzione delle ore, punteggio del caso Marta e valore atteso. Applicazione nei rispettivi capitoli del VOL-01; verifica indipendente e grafica ancora aperta.\n')
reg=Path('artifacts/correzioni-collana-2026-10-02/registro-applicazione.json')
rows=json.loads(reg.read_text(encoding='utf8'))
for row in rows:
    if row['id'] in changed:
        row['status']='applicato-da-verificare'
        row['changedFiles']=[changed[row['id']],'wiki/'+source]
        row['verification']=['Correzione testuale applicata; fonti e calcoli consolidati; controllo indipendente e coerenza figure/PDF da completare']
        row['sourceSha256']=hashlib.sha256(Path(changed[row['id']]).read_bytes()).hexdigest()
reg.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
assert 36+12+2==50 and 36-12*.25==33 and sum([10,40,30,20])==100
assert .25-.75*.25==.0625 and .25-.75*.5==-.125 and .5-.5*.5==.25
print('Applicati e verificati aritmeticamente: '+', '.join(changed))
