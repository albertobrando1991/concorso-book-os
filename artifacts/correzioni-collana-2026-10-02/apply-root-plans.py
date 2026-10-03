import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)

s='sistema-adattabile';t=u.read(s)
t=u.replace(t,'### Cosa tagliare nel piano 30 giorni','''### Giorni 29–30 - Chiusura del piano

Quattro settimane coprono 28 giorni. Nei due giorni residui completa il ripasso degli errori selezionati, controlla sede, orario e documenti e svolgi soltanto richiami brevi. Evita una simulazione estenuante la sera precedente. Se la prova cade prima, adatta i blocchi alle date effettive.

### Cosa tagliare nel piano 30 giorni''')
t=u.replace(t,'Il piano da 60 giorni è il più comune.','Il piano da 60 giorni offre più spazio per alternare studio e verifica.')
t=u.replace(t,'### Mese 1 - Fondazione','### Giorni 1–30 - Fondazione')
t=u.replace(t,'### Mese 2 - Moduli e applicazione','### Giorni 31–60 - Moduli e applicazione')
t=u.replace(t,'### Mese 3 - Prova e stabilizzazione','### Giorni 61–90 - Prova e stabilizzazione')
t=u.replace(t,'## Settimana tipo','''## Dai giorni alle righe del calendario

Le settimane sono blocchi di sette giorni; le fasi sopra indicano il lavoro prevalente, mantenendo ripasso e prove anche durante lo studio di nuovi argomenti. Nell’Appendice D compila le righe settimanali e il blocco finale secondo questa corrispondenza:

| Piano | Settimane complete | Blocco finale |
|---|---|---|
| 15 giorni | 2: giorni 1–14 | giorno 15 |
| 30 giorni | 4: giorni 1–28 | giorni 29–30 |
| 60 giorni | 8: giorni 1–56 | giorni 57–60 |
| 90 giorni | 12: giorni 1–84 | giorni 85–90 |

I giorni finali non si aggiungono alle fasi già descritte: ne sono la parte conclusiva. Per esempio, nel piano di 60 giorni il giorno 56 è nella settimana 8 e nella fase di rifinitura; i giorni 57–60 completano la stessa fase nel blocco residuo.

## Settimana tipo''')
u.save(s,t,['V01-41'])
s='appendice-d-piano-studio-personale';t=u.read(s)
t=u.replace(t,'Usa tutte le 12 righe se hai 90 giorni. Se hai 60 giorni usa le prime 8. Se hai 30 giorni usa le prime 4. Se hai 15 giorni usa solo le prime 2 e lavora per blocchi.', 'Compila 12 settimane e 6 giorni residui per il piano di 90 giorni; 8 settimane e 4 giorni per 60; 4 settimane e 2 giorni per 30; 2 settimane e un giorno per 15. Una settimana comprende sette giorni: assegna le date reali, inclusi riposi e impegni personali. Usa la griglia finale per il periodo che resta dopo le settimane complete.')
t=u.replace(t,'La colonna “Decisione” è obbligatoria.', '''### Giorni residui e chiusura

Compila solo le righe necessarie: 6, 4, 2 oppure 1, secondo il piano. Riporta i giorni 85–90, 57–60, 29–30 oppure 15 e le rispettive date.

| Giorno e data | Ripasso prioritario | Output breve | Verifica e logistica |
|---|---|---|---|
| 1: ____ | | | |
| 2: ____ | | | |
| 3: ____ | | | |
| 4: ____ | | | |
| 5: ____ | | | |
| 6: ____ | | | |

La colonna “Decisione” è obbligatoria.''')
u.save(s,t,['V01-41'])
s='conclusione';t=u.read(s)
t=u.replace(t,'## Le cinque promesse mantenute','## Verifica le cinque competenze')
t=u.replace(t,'L’introduzione elencava cinque cose che questo libro ti avrebbe insegnato a fare. Ora puoi verificarle una per una, non come definizioni, ma come azioni che sai già compiere.', 'L’introduzione indicava cinque competenze da allenare. Verificale con un bando reale: riesci a ricostruire requisiti e prove, classificare le materie, motivare le priorità, analizzare gli errori e svolgere un esercizio nel formato richiesto?')
start=t.index('Sai leggere un bando senza perderti');end=t.index('\n\n## Il capitale',start)
t=t[:start]+'''Il Bando Decoder aiuta a controllare requisiti, prove e allegati, ma non garantisce una lettura senza errori: confronta ogni campo con il documento ufficiale e chiarisci i dubbi prima della scadenza. La mappa delle aree distingue contenuti comuni e specialistici; il diario collega gli errori al ripasso; le simulazioni verificano se la preparazione regge nelle condizioni della prova.

Se una competenza resta fragile, torna alla spiegazione e all’esercizio corrispondenti. Può essere necessario cambiare esempio, approfondire una materia o chiedere un chiarimento. Il risultato dipende anche dal tempo disponibile, dai prerequisiti e dalle caratteristiche della selezione: un’incertezza non è una colpa del candidato.''' +t[end:]
start=t.index('Chi non costruisce capitale');end=t.index('\n\n## Che cosa fare',start)
t=t[:start]+'''Quando due bandi condividono materie, puoi riutilizzare spiegazioni, schemi e verifiche già svolte. La parte comune va misurata confrontando i programmi effettivi: non esiste una percentuale valida per tutti i concorsi. Aggiorna le norme, controlla il livello di approfondimento e prova a rispondere a quesiti nuovi prima di considerare una materia consolidata.''' +t[end:]
u.save(s,t,['V01-40','V01-44'])
s='scegliere-moduli-integrativi';t=u.read(s)
t=u.replace(t,'anche quando l’80% delle materie è già la stessa', 'anche quando una parte delle materie è già stata studiata')
t=u.replace(t,'Il cliente — e tu come candidato — deve capirla in pochi secondi.', 'Confronta il programma del bando con gli indici dei volumi prima di scegliere il percorso.')
t=u.replace(t,'non sull’ansia o sull’upsell', 'sulla presenza di contenuti ulteriori effettivamente richiesti')
t=u.replace(t,'Per il lettore la mappa commerciale e questa:', 'La mappa dei volumi è questa:')
t=u.replace(t,'La roadmap editoriale prevede uscita progressiva per famiglie (MVP su M-FL01, M-IR01, M-FC03, M-SA02, poi espansione). Se un modulo non è ancora disponibile, usa il criterio di questo capitolo per costruire un percorso provvisorio con fonti ufficiali e scheda modulo personale.', 'Verifica nel catalogo aggiornato la disponibilità del volume e l’edizione. Se manca un approfondimento richiesto dal bando, inseriscilo nella scheda del percorso e scegli una fonte di studio adeguata: il solo titolo della famiglia non dimostra che l’argomento sia coperto.')
t=u.replace(t,'— non ricomprare o restudiare l’80% sovrapposto.', 'senza ripetere inutilmente le parti che hai già appreso, dopo averne verificato attualità e profondità.')
u.save(s,t,['V01-40'])

s='anatomia-del-bando';t=u.read(s);a=t.index('## Classificare le materie:');b=t.index('\n![Schema per classificare',a)
t=t[:a]+'''## Classificare le materie: programma, prova, peso e priorità

Tieni separati quattro campi. La presenza nel programma è un dato del bando; la priorità dipende anche dalla tua preparazione. Una materia richiesta rimane da preparare anche se le assegni meno tempo.

| Campo | Che cosa annotare | Esempio |
|---|---|---|
| Prevista dal bando | Sì, no oppure ambito da chiarire, con il punto del programma | Inglese espressamente richiesto |
| Fase della prova | Preselettiva, scritto, orale, pratica; anche più fasi | Accertamento all’orale |
| Peso e soglia | Punti, numero di quesiti se noto, idoneità o soglia autonoma | Idoneità obbligatoria |
| Priorità personale | Alta, media o bassa, motivata da peso e lacune | Alta perché la comprensione è fragile |

“Solo orale” si usa soltanto se risulta dal bando. “Killer” è un’etichetta di lavoro per una materia che espone a un rischio rilevante, non una categoria giuridica né la prova che eliminerà molti candidati. “Probabile” indica un’ipotesi da verificare, non autorizza ad aggiungere materie estranee al programma. Una materia breve o senza punteggio può essere decisiva se prevede una soglia di idoneità.''' +t[b:]
t=u.replace(t,'| Materie obbligatorie | |\n| Materie probabili | |\n| Materie accessorie | |\n| Materie killer | |\n| Materie solo orali | |','| Materie previste, con riferimento al programma | |\n| Fase per ciascuna materia | |\n| Peso e soglie per materia | |\n| Priorità personali e motivo | |\n| Ambiti da chiarire su fonte ufficiale | |')
t=u.replace(t,'A questo punto classifica le materie: diritto amministrativo ed enti locali sono obbligatorie; trasparenza e anticorruzione possono diventare killer; informatica e inglese richiedono blocchi brevi ma costanti.', 'Tutte le materie elencate sono richieste. Per ciascuna registra in quale prova compare e con quale peso o soglia. Poi assegna la priorità personale: amministrativo ed enti locali possono richiedere più ore, mentre informatica e inglese richiedono esercizi costanti. La durata dei blocchi dipende dalla diagnosi iniziale, non da una presunta facoltatività.')
t=u.replace(t,'La decisione non è “studiare tutto”. La decisione è partire', 'Il programma va coperto; la decisione riguarda l’ordine di lavoro. Conviene partire')
t=u.replace(t,'| Quali sono le tre materie obbligatorie? | |','| Quali materie sono richieste e quali tre hanno ora priorità maggiore? | |')
u.save(s,t,['V01-01'])
s='appendice-c-template-bando-decoder';t=u.read(s);a=t.index('Classifica le materie. Non limitarti a copiarle.');b=t.index('### Nuclei immediati',a)
t=t[:a]+'''Separa programma, fase, peso e priorità. Compila una scheda per ciascuna materia richiesta; copia le righe se necessario.

| Campo | Materia 1 | Materia 2 |
|---|---|---|
| Nome della materia | | |
| Prevista: punto del bando/programma | | |
| Fase: preselettiva/scritto/orale/pratica | | |
| Peso e soglia, oppure non indicati | | |
| Priorità personale: alta/media/bassa | | |
| Motivo e prima azione | | |

“Solo orale” richiede un’indicazione del bando. Una priorità bassa non elimina la materia dal programma. Se il peso non è specificato, scrivi “non indicato”: non inventare percentuali.

''' +t[b:]
t=u.replace(t,'- Classificare tutte le materie come “obbligatorie”.','- Assegnare a tutte le materie la stessa priorità senza valutarne peso e difficoltà: possono invece essere tutte obbligatorie se previste dal programma.')
u.save(s,t,['V01-01'])

s='appendice-f-matrice-materie-profili';t=u.read(s)
t=u.replace(t,'Indica una probabilità operativa.', 'Suggerisce un ambito di confronto, senza attribuire probabilità statistiche.')
t=u.replace(t,'| ALTA | Materia molto probabile o ad alta resa |', '| ALTA | Priorità di studio orientativa elevata, da confermare |')
t=u.replace(t,'Lettura: se una colonna è CORE o ALTA, non puoi trattarla come ripasso casuale. Se è MEDIA o VERIF, devi leggere il bando prima di assegnare tempo. Se è MIN, basta spesso un raccordo essenziale.', 'Le sigle orientano lo studio, ma non sostituiscono i quattro campi del Bando Decoder: materia prevista, fase, peso/soglia e priorità personale. Anche con MIN, MEDIA o NO, una materia espressamente richiesta va preparata al livello indicato; con CORE o ALTA non si presume che compaia in ogni selezione.')
t=u.replace(t,'sarà ha già preparato', 'Sara ha già preparato')
note='''Questa selezione comprende 13 mappe operative; le 15 famiglie del Capitolo 19 hanno un perimetro più ampio. Per i profili culturali, archivistici e bibliotecari usa il VOL-06, percorso M-IR04, confrontando il programma con l’indice specialistico. Per dirigenza, carriere speciali e corpi uniformati usa l’inquadramento del Capitolo 19, sezione “Famiglia 15 - Dirigenza, carriere speciali e corpi uniformati”, e costruisci la scheda sul programma specifico: i volumi qui elencati non promettono la copertura di tutte quelle carriere. Le indicazioni di frequenza sono orientamenti qualitativi, non percentuali ricavate da un campione rappresentativo.

'''
t=u.replace(t,'## Regole di lettura',note+'## Regole di lettura')
u.save(s,t,['V01-01','V01-39','V01-48'])
s='mappe-profilo-cosa-resta-comune-cosa-cambia';t=u.read(s)
t=u.replace(t,'## Obiettivo del capitolo',note+'## Obiettivo del capitolo')
u.save(s,t,['V01-39'])

for topic in ['piano-studio-personale','metodo-di-studio','logica-copertura-volumi-concorsobook']:
 p=Path('wiki/topics')/(topic+'.md')
 with p.open('a',encoding='utf8') as out:out.write('\n\n## Calendari e perimetro del 3 ottobre 2026\n\n[[sources/vol-01-esempi-logica-inglese-metodo-2026-10-02]] documenta i giorni residui dei piani, le quattro dimensioni della classificazione delle materie e la selezione di 13 mappe sulle 15 famiglie. Corrette promesse non documentate; controllo PDF ancora aperto.\n')
u.record()
