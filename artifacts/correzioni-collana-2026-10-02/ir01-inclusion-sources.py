from pathlib import Path
import shutil,hashlib,re
A=Path('artifacts/correzioni-collana-2026-10-02');R=Path('wiki/raw/correzioni-collana-2026-10-02')
paths=['dlgs66-art7-current.html','dl170-art1-current.html','l104-art15-current.html','mim-dsa-lineeguida.pdf']
for name in paths:
 if not (R/name).exists(): shutil.copyfile(A/name,R/name)
p=Path('wiki/sources/inclusione-scolastica-disabilita-dsa-dlgs-66-2017-legge-170-2010.md');t=p.read_text(encoding='utf8')
t=t.replace('Per le funzioni puntuali dei gruppi di lavoro, la documentazione individuale e i provvedimenti applicativi e\' necessaria review umana.','Le funzioni e le scadenze sono integrate dal riscontro normativo del 3 ottobre 2026 riportato sotto; le applicazioni a casi individuali restano di competenza dei soggetti previsti.')
t+='''
## Riscontro normativo del 3 ottobre 2026: PEI, GLO e PDP

Letti integralmente art. 7 D.Lgs. 66/2017, art. 1 D.L. 170/2026 e art. 15 L. 104/1992 consolidati; letti §§ 3 e 3.1, pagine 6–8, delle Linee guida DSA del 2011 e artt. 4–6 D.M. 5669/2011. Non confondere i termini previgenti dei modelli PEI con quelli della legge sopravvenuta.

- Il PEI è elaborato e approvato dal GLO; considera accertamento, profilo di funzionamento, barriere e facilitatori e definisce obiettivi, sostegni, verifiche, valutazione e raccordo degli interventi. Il GLO comprende team/consiglio di classe, famiglia, figure professionali pertinenti con supporto multidisciplinare; è assicurata la partecipazione attiva dello studente secondo autodeterminazione. Il GLI opera invece a livello d'istituto e supporta Piano per l'inclusione e attuazione dei PEI.
- Dal 1° ottobre 2026, D.L. 30 settembre 2026 n. 170, art. 1: nuova iscrizione o certificazione → provvisorio entro giugno, definitivo entro il 15 ottobre; già inseriti nel supporto e nella stessa scuola → definitivo entro giugno, aggiornamenti nelle prime due settimane di ottobre, successive modifiche per nuove condizioni di funzionamento. Non attribuire retroattivamente adempimenti a giugno 2026: il decreto entra in vigore in ottobre e il regime applicativo va seguito negli atti della procedura concreta.
- Il PEI definisce motivatamente le ore di sostegno alla classe. Nel passaggio d'anno si valuta prioritariamente il mantenimento, salva assegnazione dell'organico e motivati aggiornamenti; non è automatismo né blocco assoluto delle modifiche. Restano verifiche periodiche e aggiornamenti nei passaggi di grado/condizioni rilevanti.
- Art. 15, comma 11-bis: possibile approvazione anche in assenza di una componente regolarmente convocata quando la mancata partecipazione impedirebbe il rispetto dei termini, fermo art. 7, comma 2, lett. b). Non autorizza a omettere la convocazione o escludere la famiglia.
- Al 3 ottobre 2026 si tratta di decreto-legge vigente non ancora convertito: la verifica della conversione è necessaria per edizioni successive.
- DSA: individualizzazione adatta percorsi per competenze comuni; personalizzazione valorizza bisogni e potenzialità. Nel quadro DSA gli strumenti compensativi facilitano la prestazione deficitaria e le dispense evitano prestazioni non essenziali; non costituiscono da sole un percorso a obiettivi ridotti. Il PDP formalizza attività, strumenti, dispense e verifiche, con raccordo familiare, entro il primo trimestre secondo le Linee guida. Non trasferire automaticamente termini o disciplina del PEI al PDP.

Fonti primarie: https://www.gazzettaufficiale.it/eli/id/2026/09/30/26G00190/sg ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2017-04-13;66~art7!vig= ; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1992-02-05;104~art15!vig= ; https://www.istruzione.it/esame_di_stato/Primo_Ciclo/normativa/allegati/prot5669_11.pdf ; https://www.mim.gov.it/documents/20182/198444/Linee%2Bguida%2Bper%2Bil%2Bdiritto%2Ballo%2Bstudio%2Bdegli%2Balunni%2Be%2Bdegli%2Bstudenti%2Bcon%2Bdisturbi%2Bspecifici%2Bdi%2Bapprendimento/663faecd-cd6a-4fe0-84f8-6e716b45b37e . Modelli e linee guida PEI: D.I. 182/2020, corretto dal D.I. 153/2023, repertorio USR https://www.istruzioneer.gov.it/2023/09/15/decreto-interministeriale-1-8-2023-153-pei/ .

Copie acquisite immutabili:
'''
for name in paths:t+=f'- `raw/correzioni-collana-2026-10-02/{name}`; SHA-256 {hashlib.sha256((R/name).read_bytes()).hexdigest()}.\n'
t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
p=Path('wiki/sources/programmi-concorsi-docenti-dm-205-206-2023.md');t=p.read_text(encoding='utf8');t+='''
## Integrazione disciplinare e progettuale del 3 ottobre 2026

La precedente sintesi del programma non copriva le teorie promesse. Il capitolo 11 viene integrato con un nucleo selezionato: comportamentismo/rinforzo; cognitivismo, attenzione e memoria; costruzione attiva, Piaget e adattamento; mediazione sociale e zona di sviluppo prossimale; scaffolding; autoefficacia e metacognizione. Sono modelli interpretativi, non etichette diagnostiche o età rigide da applicare a una classe.

Riscontri istituzionali e bibliografici selettivi: INDIRE, ricostruzione del rapporto tra teorie dell'apprendimento e tecnologie (https://www.indire.it/content/index.php?action=read&id=1175&navig=t); materiali universitari di Paola Nicolini su Piaget, p. 5 per assimilazione/accomodamento (https://docenti.unimc.it/paola.nicolini/teaching/2024/31101/files/Piaget.pdf); esperienza documentata INDIRE «Parole in gioco», per mediazione nella zona prossimale (https://repository.indire.it/repository_cms/working/export/6659/progettazione-intervento-didattico.html); Wood, Bruner e Ross, *The role of tutoring in problem solving*, 1976, 17:89–100, DOI 10.1111/j.1469-7610.1976.tb00381.x (record editore verificato, non dichiarata lettura integrale); Stanford, sintesi della ricerca di Bandura del 1977 sull'autoefficacia (https://longevity.stanford.edu/self-efficacy-toward-a-unifying-theory-of-behavior-change/).

Consolidamento: assimilazione usa uno schema disponibile, accomodamento lo modifica; la zona prossimale distingue prestazione autonoma e assistita; scaffolding è sostegno graduato da ridurre; autoefficacia è convinzione di riuscire in un compito, distinta dalla competenza effettiva. Rinforzo aumenta la probabilità di una risposta; il segno positivo/negativo riguarda aggiunta/rimozione, non valore morale. Le applicazioni e i casi sono elaborazione didattica originale e non risultati sperimentali attribuiti agli autori.

Per la prova docente valgono i D.M. 205/206 e la procedura specifica, non la trasposizione del DPR 487. Il capitolo 13 offre una lezione originale completa su frazioni equivalenti con contesto e durata assunti, materiali cartacei, verifica e rubrica. Non pretende di sostituire il programma disciplinare di ogni classe di concorso.
''';t=re.sub(r'^updated_at:.*$','updated_at: 2026-10-03',t,flags=re.M);p.write_text(t,encoding='utf8')
print('Fonti inclusione e pedagogia consolidate prima del testo')
