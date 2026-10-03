from pathlib import Path
import importlib.util,re,json,hashlib
s=importlib.util.spec_from_file_location('u',Path(__file__).with_name('root-utils.py'));u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
u.BASE=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/chapters');u.REF='sources/vol-09-bandi-specialistici-verificati-2026-10-03.md'
slug='01-quattro-profili-ciclo-integrato';t=u.read(slug)
t=u.replace(t,'## N-TR02-01-02 · Il ciclo dal fabbisogno alla chiusura','''### Tre riscontri nei bandi, tre livelli di lavoro

Il bando 2026 per l’Ufficio Gare di **Ca’ Foscari** richiede a un funzionario di seguire documenti di gara, procedure, strumenti Consip e PAD, esecuzione e tempi. Il bando **Bologna, rif. 5163 del 2025**, colloca invece nell’Area Collaboratori attività operative di acquisto, atti e piattaforme nazionali e regionali. Entrambi confermano l’utilità dei capitoli sul procurement digitale, ma non attribuiscono lo stesso livello di autonomia al personale.

Il concorso 2026 della **CUC dell’Unione Le Terre del Sole** riguarda uno specialista tecnico-giuridico del ciclo contrattuale. Il testo rettificato del 10 luglio sostituisce la procedura per titoli ed esami con prove scritta teorico-pratica e orale: studiare il solo avviso iniziale porterebbe a preparare una selezione diversa.

Questi esempi giustificano esercizi su atti, scelte e controlli; non dimostrano che ogni concorso contenga tutte le materie del volume. La funzione di RUP richiede i presupposti e la nomina previsti dal Codice: il nome del posto non la conferisce automaticamente. Il profilo PNRR/project management è documentato, fra gli altri, dall’avviso MIT 2026 per program management degli investimenti, con monitoraggio, ReGiS e coordinamento.

Per confrontare il tuo bando, annota **attività**, **materie**, **tipo di prova** e **rettifiche**. Poi scegli un output corrispondente nel capitolo 14. I testi richiamati sono pubblicati su inPA e nelle sezioni concorsi dei rispettivi enti; date e identificativi permettono di distinguerli da procedure simili.

## N-TR02-01-02 · Il ciclo dal fabbisogno alla chiusura''')
u.save(slug,t,['V09-38'],u.REF);u.record()
corpus=Path('wiki/sources/bandi-rappresentativi-m-tr02-appalti-pnrr-2025-2026.md');c=corpus.read_text(encoding='utf8')
c+='''
## Integrazione verificata del 3 ottobre 2026

[[sources/vol-09-bandi-specialistici-verificati-2026-10-03]] acquisisce tre PDF ufficiali aggiuntivi (CUC Le Terre del Sole, Ca’ Foscari Ufficio Gare, Bologna acquisti). Risolve la lacuna del campione specialistico e digitale segnalata sopra; le righe iniziali non acquisite restano storicamente tali. Il campione utilizzabile passa da tre a sei procedure, senza valore statistico nazionale. La preparazione M-TR02 è sostenuta da programmi e mansioni effettivi, non dalla sola denominazione del posto. Le sezioni precedenti descrivono il checkpoint del 29 luglio e non lo stato corrente delle nuove acquisizioni.
''';corpus.write_text(c,encoding='utf8')
u.REF='sources/vol-09-laboratorio-soluzioni-verificate-2026-10-03.md'
slug='14-laboratorio-atti-casi-simulazioni';t=u.read(slug)
anchor='### Riferimenti e uso degli strumenti nel volume'
t=u.replace(t,anchor,'''### Kit cartaceo: trovare e riutilizzare gli strumenti

I modelli sono collocati accanto alla teoria e ai casi che ne spiegano l’uso. La tavola seguente consente di ritrovarli senza un’appendice separata o un servizio digitale.

| Strumento cercato | Destinazione nel volume |
|---|---|
| Ruoli, qualificazione e responsabilità | Capitolo 2, matrice RACI e livelli di qualificazione |
| Valore, soglie e percorso di affidamento | Capitoli 3 e 5, tavole e caso Alfa; simulazioni 1–3 di questo capitolo |
| Accesso e rimedi | Capitolo 9, timeline; simulazione 6 di questo capitolo |
| Consip, MePA, accordi quadro, SDA e ASP | Capitolo 7, confronto degli strumenti e albero di scelta |
| PNRR, ReGiS e chiusura | Capitolo 10, scheda di avanzamento e scadenze; simulazione 7 |
| Spesa e antifrode | Capitolo 11, calcolo ammissibilità e cofinanziamento; simulazione 8 |
| DNSH e CAM | Capitolo 12, casi notebook e arredi; simulazione 9 |
| Charter, WBS, Gantt, registri e report | Capitolo 13, rete svolta e registri; simulazione 10 |
| Atti e controlli | Simulazioni 1–6 e schede compilabili seguenti |

### Scheda di decisione per affidamento diretto

Usala dopo aver verificato che la procedura sia ammissibile. Non è un provvedimento già adottato né un modello valido per qualsiasi ente. Nella simulazione 2 compila i campi con i dati disponibili e indica espressamente quelli da acquisire; non inventare un numero di CIG, un impegno contabile o un esito di controllo.

**Ente e soggetto competente:** __________

**Oggetto e prestazioni richieste:** __________

**Fabbisogno e interesse pubblico:** __________

**Valore netto, opzioni e metodo di calcolo:** __________

**Procedura, norma e strumento utilizzato:** __________

**Contraente e ragioni della scelta:** __________

**Esperienze idonee, requisiti generali e speciali richiesti:** __________

**Controlli svolti, documenti ed esiti:** __________+
**Risorse, impegno e riferimenti contabili:** __________

**CIG, eventuale CUP, tracciabilità e adempimenti digitali:** __________

**Termini, condizioni, controllo della prestazione e forma del contratto:** __________

**Dispositivo proposto e allegati:** __________

La revisione finale controlla soprattutto la coerenza fra oggetto, valore, procedura e motivazione. Le formule «visto» e «considerato» non sostituiscono i fatti. Una decisione ben ordinata può essere comunque errata se esclude le opzioni dal valore o richiama una deroga non applicabile.

### Verbale e registro delle modifiche

Per il verbale della simulazione 5 usa questa sequenza: **contratto e oggetto** __________; **data e presenti** __________; **prestazione attesa** __________; **attività e prove svolte** __________; **risultato osservato** __________; **difformità rispetto alla clausola** __________; **osservazioni dell’esecutore** __________; **azione richiesta e verifica successiva** __________; **effetti proposti, soggetto competente e allegati** __________.

Il verbale documenta l’accertamento. Non va confuso con un’autorizzazione a modificare il contratto o con una decisione sulla penale già adottata. Se il completamento avviene dopo, si redige un documento successivo collegato al primo, senza sostituire il verbale originario con una versione che faccia scomparire il ritardo.

Per una modifica tieni una scheda autonoma: **richiesta e data** __________; **richiedente** __________; **causa e documenti** __________; **effetto su oggetto, prezzo, durata e prestazioni** __________; **fattispecie dell’articolo 120 proposta** __________; **limiti e calcoli** __________; **effetti su finanziamento e DNSH/CAM** __________; **decisione competente** __________; **atti contrattuali e pubblicità** __________; **nuova versione approvata** __________. Se manca la decisione, la scheda resta una proposta: il fornitore non è autorizzato dal solo aggiornamento del Gantt.

### Registro degli aggiornamenti per lo studio

Quando cambia una norma, annota: **data di verifica** __________; **atto e articolo** __________; **fonte ufficiale** __________; **decorrenza e transitorio** __________; **regola precedente** __________; **regola attuale** __________; **capitoli ed esercizi coinvolti** __________; **riprova eseguita** __________. Un comunicato, una proposta e una norma efficace non sono intercambiabili. Il campo sul transitorio impedisce di applicare automaticamente la nuova disciplina a una procedura che resta soggetta a quella precedente.

'''+anchor)
# Repair a literal stray patch escape before writing.
t=t.replace('__________\\+','__________\n')
u.save(slug,t,['V09-37'],u.REF)
p=Path('wiki/books/moduli/m-tr02-appalti-pnrr-fondi-ue/planning/01-indice-analitico-vol-09.md');m=p.read_text(encoding='utf8')
start=m.index('## Appendici');end=m.index('## Percorsi di studio',start)
m=m[:start]+'''## Strumenti distribuiti nei capitoli

Revisione del 3 ottobre 2026: le appendici A–E non sono unità editoriali separate. I nuclei necessari sono presenti nel corpo; il kit cartaceo del capitolo 14 fornisce la mappa e schede effettivamente compilabili. Questa sezione sostituisce la precedente promessa di 4.500 parole di appendici autonome, evitando rinvii a unità inesistenti.

| Famiglia di strumenti | Destinazione effettiva |
| --- | --- |
| Tavole del Codice: ruoli, valore, soglie e rimedi | cap. 2, 3, 5, 9; cap. 14 simulazioni 1–6 |
| MePA e Consip: scelta dello strumento e percorsi operativi | cap. 7; cap. 14 simulazione 2 |
| PNRR, ReGiS, DNSH e antifrode | cap. 10–12; cap. 14 simulazioni 7–9 |
| Project management: charter, WBS, Gantt, RACI, registri e report | cap. 2 e 13; cap. 14 simulazione 10 |
| Atti, controlli e aggiornamenti | cap. 14, Kit cartaceo, Scheda di decisione, Verbale e registro modifiche, Registro aggiornamenti |

'''+m[end:]
m=m.replace('inclusi front matter e appendici','inclusi front matter e strumenti').replace('; appendici A, B, E.','; kit cartaceo del capitolo 14.').replace('; appendici B, E.','; kit cartaceo del capitolo 14.').replace('; appendici C, D, E.','; kit cartaceo del capitolo 14.').replace('; appendici C, D.','; kit cartaceo del capitolo 14.')
p.write_text(m,encoding='utf8');u.changes['V09-37'].append(p.as_posix());u.record()
raw=Path('wiki/raw/correzioni-collana-2026-10-02')
names=['unive-gare-2026.pdf','unibo-acquisti-5163-2025.pdf','terre-sole-cuc-rettificato-2026.pdf']
Path('artifacts/correzioni-collana-2026-10-02/vol09-bandi-manifest.json').write_text(json.dumps([{'file':(raw/n).as_posix(),'bytes':(raw/n).stat().st_size,'sha256':hashlib.sha256((raw/n).read_bytes()).hexdigest()} for n in names],indent=2),encoding='utf8')
