from pathlib import Path
import re,shutil
p=Path('wiki/books/moduli/m-sp01-forze-ordine/chapters/08-piano-30-60-90-doppio-binario.md');t=p.read_text(encoding='utf-8');a=Path('wiki/reviews/correzioni-collana-2026-10-02/archive/pre-correzioni-sp01-08.md');assert not a.exists();shutil.copyfile(p,a)
t=t.replace("Significa costruire un piano che tenga insieme due binari diversi: da un lato lo studio delle conoscenze richieste dal bando, dall'altro la preparazione progressiva alle fasi eliminatorie, selettive e valutative che possono seguire la prova iniziale.","Significa integrare studio, accertamenti e adempimenti. In questo modulo «doppio binario» indica sempre accesso base e accesso ispettivo, non studio teorico e preparazione fisica.")
t=t.replace('Ogni numero inserito nel piano deve derivare dal bando o dagli avvisi ufficiali.','I dati della prova derivano dal bando; ore, ritmi e obiettivi di allenamento sono scelte personali, da distinguere dalle prescrizioni ufficiali.')
t=t.replace('Il binario ispettivo richiede quiz, scrittura ed esposizione.','Il binario ispettivo richiede gli output del proprio bando: non tutti i concorsi prevedono un elaborato.')
t=t.replace('Se il candidato allena solo una di queste tre prestazioni, il piano ispettivo resta incompleto.','Il candidato allena le prestazioni effettivamente previste: per esempio, italiano a quiz nei Carabinieri 898 del 2026 e composizione nella GdF 983. Non aggiunge un tema obbligatorio soltanto perché il percorso è ispettivo.')
t=t.replace('nel usare','nell’usare').replace('Regole editoriali ConcorsoBook sulla distinzione tra volume base, moduli specialistici e preparazione per famiglia concorsuale.','')
pos=t.index('## N-SP01-13-03')
t=t[:pos]+'''### Variante numerica: 5.000 quesiti e 33 giorni

Il bando PS 1.000 vice ispettori 2026, art. 9, indica una banca di 5.000 quesiti: 2.000 di penale, 2.000 di procedura penale e 1.000 di costituzionale. Per rendere controllabile il carico, considera **uno scenario didattico di 33 giorni utili**. Non è un tempo di preparazione garantito dal bando.

| Giorni | Compito | Quantità e verifica |
| --- | --- | --- |
| 1–20 | Primo passaggio | 240 quesiti nuovi al giorno: 4.800 |
| 21 | Completamento | 200 nuovi: copertura totale 5.000 |
| 22–28 | Ripasso selettivo | 200 ritorni al giorno: 1.400 verifiche su errori, dubbi e campione di risposte sicure |
| 29–31 | Simulazioni | Una prova di 100 quesiti al giorno, secondo tempo e correzione ufficiali, poi analisi |
| 32–33 | Consolidamento e documenti | Errori residui, istruzioni, logistica; nessun nuovo archivio indiscriminato |

Per i primi venti giorni la proporzione della banca permette 96 quesiti di penale, 96 di procedura e 48 di costituzionale al giorno. Il giorno21 completa rispettivamente80,80e40. Sono quantità di pianificazione, non pesi automaticamente applicabili alla prova effettiva.

Il carico va provato prima di accettarlo. A una media effettiva di45secondi per quesito,240richiedono180minuti; aggiungendo45minuti di correzione e15di aggiornamento del diario si arriva a quattro ore. Se il candidato dispone di due ore, quel piano non è fattibile senza modifiche. Occorre stimare il ritmo reale, anticipare la teoria prima della banca o ridurre altre attività disponibili; non basta dividere5.000per33e dichiarare risolto il problema. Un ritmo iniziale troppo lento segnala una lacuna da affrontare, non una colpa personale.

Il secondo giro non copre automaticamente tutti i5.000quesiti:1.400ritorni sono una selezione. Se le domande ancora incerte sono2.000, il piano deve cambiare. Al controllo delgiorno21scrivi il numero reale dei dubbi e il tempo necessario; conserva un margine per malattia o imprevisti. La copertura misura ciò che hai visto; la padronanza richiede una risposta motivata a distanza.

''' +t[pos:]
pos=t.index('## Caso guidato\n')
t=t[:pos]+'''## Tre piani completi: 30, 60 oppure 90 giorni

Le tre durate sono alternative. I nuclei precedenti spiegano la progressione lunga; se mancano30giorni devi completare un ciclo entro30, non svolgere soltanto il primo terzo di quello da90. Gli esempi assumono una disponibilità media di due ore al giorno per studio e gestione documentale:60,120oppure180ore complessive. Le eventuali attività fisiche concordate con professionisti hanno un calendario separato e devono essere compatibili con il tempo reale disponibile.

| Durata | Diagnosi e programma | Copertura e recupero | Simulazioni e correzioni | Ripasso finale e documenti |
| --- | --- | --- | --- | --- |
| 30 giorni, 60 ore | Giorni1–4,8ore | Giorni5–18,28ore | Giorni19–26,16ore | Giorni27–30,8ore |
| 60 giorni, 120 ore | Giorni1–7,14ore | Giorni8–35,56ore | Giorni36–50,30ore | Giorni51–60,20ore |
| 90 giorni, 180 ore | Giorni1–10,20ore | Giorni11–55,90ore | Giorni56–75,40ore | Giorni76–90,30ore |

**Percorso base.** Nella fase di copertura distribuisci una settimana tipo di14ore in6di teoria ed esercizi sui nuclei deboli,4di quiz,2di correzione e ripasso,1di simulazione parziale e1di documenti e avvisi. Nella fase finale sposta due ore dalla lettura alla simulazione corretta. L’obiettivo non è un numero astratto di pagine: ogni area del programma deve comparire nel diario e negli esercizi.

**Percorso ispettivo.** Sulle stesse14ore usa5per teoria,3per il formato scritto richiesto,2per esposizione orale se prevista,3per correzione e ripasso e1per adempimenti. Per GdF una composizione completa di sei ore sostituisce, nella settimana scelta, più blocchi brevi: non può stare dentro un blocco da tre ore. Per CC898le tre ore sullo scritto sono dedicate all’italiano a quesiti. Per PSviceispettori la banca giuridica modifica le priorità secondo lo scenario precedente.

**Checkpoint a30giorni.** Il giorno4deve esistere un elenco completo delle aree e una misura iniziale; il giorno18nessuna area resta invisibile; il giorno26confronti almeno tre prove corrette o, per l’elaborato, tre produzioni con revisione. Se la copertura è bassa, redistribuisci il tempo rimanente e documenta le lacune: non segnare completo ciò che non hai studiato.

**Checkpoint a60giorni.** Al giorno7classifica gli errori; al35ripeti a distanza un campione per ogni area; al50controlla stabilità e tempo in almeno tre prove comparabili. Mantieni una quota di recupero nelle ore di correzione: un ritardo non deve cancellare automaticamente la revisione.

**Checkpoint a90giorni.** Al giorno10valida il programma; al55misura copertura e debolezze residue; al75scegli gli interventi finali sulla base delle simulazioni. Gli ultimi15giorni non autorizzano ad abbandonare un’intera materia prevista: riduci attività ripetitive già stabili e cura le lacune decisive. Il controllo di domanda, titoli e certificati segue le proprie scadenze fin dal giorno iniziale, non viene rimandato all’ultima fase.

''' +t[pos:]
# Tabella breve senza HTML letterale.
start=t.index('| Elemento | Dati essenziali | Verifica o azione |');end=t.index('Dopo aver compilato la griglia',start)
t=t[:start]+'''| Campo | Piano personale |
| --- | --- |
| Durata scelta e ore effettivamente disponibili | __________________________ |
| Base o ispettivo; formato scritto | __________________________ |
| Primo checkpoint e risultato misurabile | __________________________ |
| Recupero settimanale riservato | __________________________ |
| Ultime simulazioni e correzioni | __________________________ |
| Adempimento più vicino e ricevuta necessaria | __________________________ |

''' +t[end:]
comments=["Il bando stabilisce prove e vincoli; A parte dal materiale senza verificarne pertinenza, C importa disponibilità altrui, D misura quantità senza collegarla alla prova.","La forma della prova può richiedere produzioni diverse. A e D introducono esclusioni assolute smentite dagli esempi; B cancella la preparazione culturale.","La copertura deve lasciare traccia degli errori e del concetto. A perde la diagnosi, B memorizza una posizione instabile, D ignora il materiale ufficiale pertinente.","Più prove comparabili mostrano oscillazioni, tempi e errori ricorrenti. Pagine, strumenti e sensazioni delle altre opzioni non misurano quella stabilità.","Il piano organizza tempi e adempimenti senza formulare prescrizioni sanitarie. A attribuisce al manuale una competenza impropria, C confonde prestazione e teoria, D rinvia troppo tardi.","Nuovi materiali senza un problema identificato sottraggono tempo alla correzione. A e B sono attività pertinenti; D è ragionevole solo se motivato e senza cancellare obblighi del programma."]
part=t.index('## ▣ Verifica 08.A'); pre=t[:part];tail=t[part:]; i=[0]
def com(m):
 v=m.group(0)+'\n'+comments[i[0]]+'\n';i[0]+=1;return v
tail=re.sub(r'\*\*Risposta corretta: [A-D]\.\*\*',com,tail);assert i[0]==6;t=pre+tail
# Spazi nelle integrazioni numeriche.
t=re.sub(r'(?<=[A-Za-zÀ-ÿ])(\d)',r' \1',t);t=re.sub(r'(\d)(?=[A-Za-zÀ-ÿ])',r'\1 ',t)
# Non alterare i codici ID: ripristino SP 01.
t=t.replace('SP 01','SP01').replace('VOL- 01','VOL-01')
p.write_text(t,encoding='utf-8');print('SP01/08: tre durate, carico reale, sei commenti')
