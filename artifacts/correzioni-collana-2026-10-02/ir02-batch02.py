from pathlib import Path
import re,json
A=Path('artifacts/correzioni-collana-2026-10-02');p=Path('wiki/books/moduli/m-ir02-universita-afam/chapters/11-afam-ordinamento-amministrazione.md');t=p.read_text()
t=t.replace('## Bozza agente\n`n`n## Apertura editoriale\n\n','')
t=t.replace('Questa posizione intermedia, ma autonoma, genera spesso confusione.','Questa collocazione nella formazione terziaria, parallela a quella universitaria e dotata di un proprio ordinamento, genera talvolta confusione.')
blocks={1:'''Il settore comprende istituzioni statali e istituzioni non statali autorizzate o accreditate al rilascio dei titoli secondo la disciplina pertinente: non ogni scuola privata di musica appartiene automaticamente al sistema AFAM. Conservatori, accademie e altre istituzioni riconosciute vanno identificati attraverso l’ordinamento e i provvedimenti ministeriali. La natura non statale non impedisce di per sé il rilascio di un titolo riconosciuto, ma il riconoscimento non trasforma automaticamente l’ente in amministrazione pubblica. Per un concorso si verifica quindi sia l’istituzione sia il regime del posto.
''',3:'''L’art. 4 del D.P.R. 132/2003 individua otto organi necessari: presidente, direttore, consiglio di amministrazione, consiglio accademico, collegio dei revisori, nucleo di valutazione, collegio dei professori e consulta degli studenti. La presenza di una consulta rende riconoscibile il contributo studentesco; il controllo contabile e la valutazione della qualità restano funzioni distinte.

| Soggetto | Funzione essenziale | Errore da evitare |
| --- | --- | --- |
| Presidente | Rappresentanza e presidenza del CdA nel quadro regolamentare | Considerarlo il responsabile unico della didattica |
| Direttore | Andamento didattico, scientifico e artistico; convoca e presiede il consiglio accademico | Assimilarlo al direttore generale universitario |
| Consiglio accademico | Indirizzi delle attività didattiche, scientifiche, artistiche e di ricerca | Confonderne il piano di indirizzo con il bilancio approvato |
| Consiglio di amministrazione | Programmazione economica, bilancio, variazioni e consuntivo | Attribuirgli ogni valutazione didattica individuale |
| Revisori e nucleo di valutazione | Rispettivamente controllo contabile e valutazione delle attività | Trattarli come uffici che eseguono la gestione |

Il CdA ordinario è composto da cinque membri: presidente, direttore, un docente designato dal consiglio accademico, uno studente designato dalla consulta e un esperto nominato dal Ministro. Nei casi previsti può essere integrato da un massimo di due componenti. Il direttore amministrativo partecipa con voto consultivo. La delibera sul bilancio si colloca nelle competenze del CdA, mentre le linee di sviluppo didattico e artistico provengono dal consiglio accademico.

**Caso risolto.** La proposta di un nuovo laboratorio comprende un programma artistico e l’acquisto di attrezzature. La prima componente va raccordata alla programmazione accademica; la seconda richiede disponibilità, atti gestionali e competenze economiche. Una mail del docente proponente non sostituisce né l’approvazione pertinente né la procedura di acquisto. La segreteria separa i documenti, controlla l’iter e informa gli organi competenti.''',4:'''Il **credito formativo accademico (CFA)** misura ordinariamente 25 ore di impegno dello studente; sono possibili variazioni ministeriali entro il 20% per singole scuole. Il carico medio annuo è 60 CFA a tempo pieno e, nel testo vigente dell’art. 6, 36 a tempo parziale. Ore di lezione, esercitazione, laboratorio e studio individuale non coincidono: il credito riguarda l’impegno complessivo.

Il D.P.R. 212/2005, artt. 3 e 8, distingue:

- diploma accademico di primo livello: almeno 180 CFA;
- diploma accademico di secondo livello: almeno 120 CFA;
- secondo livello a ciclo unico: almeno 300 CFA, nel relativo ordinamento;
- diploma di perfezionamento o master: almeno 60 CFA;
- diploma accademico di specializzazione e diploma accademico di dottorato di ricerca, con disciplina propria. Quest’ultimo è equiparato al dottorato universitario.

Si tratta dei parametri del regolamento, da coordinare con i decreti dei percorsi: non ogni istituzione può attivare qualsiasi titolo soltanto perché compare nell’elenco. Il regolamento prevede anche la possibilità di modificare i crediti di secondo livello nei casi e con gli atti ministeriali indicati. Il riconoscimento dei crediti in ingresso compete all’istituzione che accoglie lo studente secondo criteri predeterminati, non al solo operatore che registra la domanda.

**Calcolo.** Un’attività da 8 CFA corrisponde ordinariamente a 200 ore complessive. Se il piano applicabile destina 100 ore alle attività guidate, le restanti 100 appartengono alle altre componenti del carico: non sono ulteriori 200 ore. Il numero di crediti non esprime un voto e non attesta da solo l’equivalenza del contenuto con un corso universitario.''',5:'''Il caso amministrativo di questo nucleo assume una **istituzione AFAM statale**. I principi e gli istituti propri dell’amministrazione pubblica si applicano nel loro perimetro: la presenza nel sistema AFAM di soggetti non statali richiede di verificare il regime pertinente, senza attribuire indistintamente a tutti natura pubblica o ogni obbligo del pubblico impiego.
'''}
for k,block in blocks.items():
 h=re.search(rf'^### N-IR02-11-{k:02}[^\n]*\n',t,re.M);assert h;t=t[:h.end()]+'\n'+block.strip()+'\n\n'+t[h.end():]
t=t.replace("Il candidato deve usare un linguaggio prudente. Non deve inventare elenchi analitici di corsi, titoli, crediti o procedure se non sono richiesti dal bando o se non sono presenti tra le fonti di studio disponibili. Deve però saper dire che il D.P.R. n. 212/2005 disciplina gli ordinamenti didattici e che tale disciplina si integra con gli atti adottati dalle singole istituzioni.","Il quadro di titoli e crediti appena esposto permette di leggere gli atti dell’istituzione. Per ammissione, articolazione dei corsi e riconoscimenti si applicano poi i decreti e i regolamenti pertinenti, senza inventare requisiti o trasferire quelli di un altro percorso.")
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
batch={}
for fid,change,evidence in [('V06-13','Corretta la collocazione terziaria AFAM; distinte istituzioni statali e non statali, limitato il caso amministrativo al settore statale, integrati organi/CFA/titoli e calcolo risolto.','DPR132 artt.4/6/7 e DPR212 artt.3/6/8 consolidati; calcolo8×25=200.'),('V06-14','Rimossi Bozza agente, escape letterali e apertura duplicata.','Controllo del testo: una sola apertura editoriale.')]:batch[fid]={'change':change,'files':[str(p).replace('\\','/'),'wiki/sources/fonti-ufficiali-m-ir02-universita-afam-2026-07-24.md'],'evidence':evidence,'status':'applicato'}
(A/'VOL-06-batch06.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf8');print('AFAM corretto')
