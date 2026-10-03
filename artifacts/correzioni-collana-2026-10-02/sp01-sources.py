from pathlib import Path
import re,shutil,hashlib,json
S=Path('wiki/sources'); A=Path('wiki/reviews/correzioni-collana-2026-10-02/archive'); A.mkdir(exist_ok=True)
names=['bandi-rappresentativi-m-sp01-forze-polizia-2026','prove-efficienza-fisica-accertamenti-forze-di-polizia-m-sp01','ordinamento-forze-di-polizia-quadro-normativo-m-sp01']
for name in names:
 p=S/(name+'.md'); backup=A/('pre-correzioni-'+name+'.md'); assert not backup.exists(); shutil.copyfile(p,backup)
p=S/(names[0]+'.md'); t=p.read_text(encoding='utf-8')
t=t.replace('massimo **29 anni non compiuti** per civili e bilinguisti; **28 non compiuti** per VFP; elevabile fino a 3 anni per servizio militare prestato','18 compiuti e **26 non compiuti** per civili e bilinguisti; **25 non compiuti** per VFP; elevazione pari al servizio militare effettivo, non superiore a tre anni (art. 2, p. 8)')
t=re.sub(r'> \*\*Rilievo di fact-checking\.\*\* Numerose fonti secondarie[^\n]+','> **Rettifica del 3 ottobre 2026.** La precedente nota aveva scambiato i massimi comprensivi di elevazione con le soglie ordinarie. La lettura visiva dell’originale, art. 2 a p. 8, conferma 26/25 anni non compiuti, non 29/28 come soglie generali.',t)
t=t.replace('666 aperti · 167 riservati al ruolo dei sovrintendenti con titolo di studio prescritto · 167 riservati a personale della Polizia di Stato con almeno 3 anni di anzianità di effettivo servizio','167 riservati ai sovrintendenti e 167 al personale PS con almeno tre anni di effettivo servizio; ulteriori riserve dell’art. 2 (3 bilinguisti, 50 superstiti, 20 ufficiali con ferma biennale conclusa senza demerito, 10 diplomati Centro studi Fermo). Non chiamare 666 posti tutti liberi da riserve')
t=t.replace('non superiore a 24 anni per i civili, fino a 26 per i volontari','civili: non superato il giorno del 24° compleanno, domanda possibile dai 17 anni con consenso; VFP: non superiore a 25 anni compiuti. Art. 2, p. 4; formule non intercambiabili')
t=t.replace('prova scritta · prove di efficienza fisica · accertamenti sanitari e psico-attitudinali · valutazione titoli · colloquio','prova scritta di selezione · efficienza fisica · accertamenti psicofisici · accertamenti attitudinali · valutazione titoli (art. 6). Nessuna prova orale autonoma')
t=t.replace('entro le 23.59 del 7 aprile 2026, esclusivamente tramite inPA','entro le 23.59 del 7 aprile 2026; invio nell’area concorsi di carabinieri.it, con SPID o CIE. inPA pubblica il bando e reindirizza (artt. 3–4)')
t=t.replace('compiuti 17 anni, non compiuti 26 alla scadenza','civili: 17 compiuti e non superato il giorno del 26° compleanno; elevazione al giorno del 28° per il servizio militare qualificato dall’art. 2; personale dell’Arma indicato dalla norma: non superato il giorno del 30°')
t=t.replace('preselezione scritta · prova scritta di **componimento di italiano** · prove di efficienza fisica · accertamenti psico-fisici e attitudinali · prova orale','prova preliminare · prova scritta di italiano a **60 quesiti a risposta multipla**, non componimento (allegato C, p. 28) · efficienza fisica · accertamenti psicofisici e attitudinali · orale · facoltative lingua e informatica; titoli per graduatoria')
t=t.replace('la partecipazione al concorso per i posti del contingente di mare **non è ammessa per più di due volte**','la partecipazione per i soli posti riservati ai motoristi navali descritti al comma 3 (otto posti nella specializzazione tecnico di macchine) **non è ammessa per più di due volte**')
t=t.replace('da 17 a 26 anni non compiuti alla scadenza; fino a 35 per militari già in servizio nel Corpo','civili: 17 compiuti e non superato il giorno del 26° compleanno alla scadenza; categorie militari del Corpo elencate all’art. 2: non superato il giorno del 35° (non beneficio indistinto per tutti i militari)')
t=t.replace('tecnico dei sistemi di comunicazione e rilevamento','tecnico dei sistemi di comunicazione e scoperta')
t=re.sub(r'> \*\*Rilievo di fact-checking\.\*\* Le fonti secondarie[^\n]+','> **Riscontro del 3 ottobre 2026.** L’art. 12, comma 3, p. 17 del bando definisce espressamente la prova come composizione italiana della durata di sei ore. Il dato è ufficiale e utilizzabile come esempio datato.',t)
t=t.replace('Il capitolo deve insegnare **come verificarli**, non riportarli.','Il capitolo insegna come verificarli e può riportare esempi datati con esatta procedura, categoria e fonte, senza trasformarli in regole permanenti.')
t+='''

## Riscontro sugli originali del 3 ottobre 2026

PS 4.400: PDF ufficiale locale, pp. 7–9 lette visivamente; art. 1 quote, art. 2 età, diploma conseguibile entro la prima prova scritta e speciale titolo per VFP in servizio/congedati al 31 dicembre 2020. La pagina PS oggi nega accesso: la verifica è sull’originale conservato, non sul sommario web.

PS 1.000: originale completo di 24 pagine acquisito da https://portale.inpa.gov.it/api/media/ad7af019-8205-4f49-9b33-6cdf5099733a e conservato in `wiki/raw/correzioni-collana-2026-10-02/ps1000-bando-2026-completo.pdf`. Lette visivamente pp. 7–10 e 13–15. Art. 3: 28 anni non compiuti, elevazione effettivo servizio militare sino a tre; nessun limite per personale PS con tre anni di servizio alla data del bando; 33 per appartenenti ai ruoli civili dell’Interno. Diploma conseguibile entro la prima prova, non generalizzare questa eccezione. Art. 4: annullare e rinviare la domanda modificata entro termine. Art. 8: scritto su penale, procedura penale, costituzionale; orale aggiunge amministrativo/pubblica sicurezza, civile (persone, famiglia, diritti reali, obbligazioni, tutela), inglese con traduzione e conversazione, informatica anche pratica. Art. 9: banca di 5.000 (2.000 penale, 2.000 procedura, 1.000 costituzionale), quesiti a cinque opzioni, scritto di 100 quesiti, tempo e criteri commissione. Art. 10: primi 4.000 con almeno 18/30 più pari merito all’ultimo; non basta 18/30 per tutti. Art. 7 consente riorganizzare ordine degli accertamenti anche dopo l’orale. Non usare ordine come immutabile.

CC 3.081: letti artt. 2–6, pp. 4–7: le rettifiche sopra prevalgono sul precedente sommario. Titolo: diploma entro a.s. 2025/26, speciale scuola secondaria di primo grado per militari già in servizio o congedati al 31 dicembre 2020. Ricevuta PDF va salvata; art. 4 consente annullare e reinviare entro termine.

CC 898: letti artt. 2, 6, 9–10 e allegato C p. 28. Prova scritta di italiano: 60 quesiti; soglia 18/30. Non è un tema. Prova preliminare comprende anche lingua scelta e comprensione: banca non comprende tutte queste componenti. Età secondo formule letterali sopra. Le facoltative non trasformano il concorso in un terzo percorso ufficiali.

GdF 983: letti artt. 1–2, 12–14, pp. 5–6, 17–19. Composizione sei ore, minimo 10/20. Ordinario: obbligatorie salto in alto, 1.000 m, piegamenti; facoltativa scelta in domanda fra 100 m e 25 m nuoto. Mare: obbligatorie salto, 1.000 m, nuoto25; facoltativa100 m o piegamenti. Un obbligatorio insufficiente esclude; facoltativo insufficiente non toglie idoneità. Punti fisici1–12 convertiti in maggiorazione0,05–0,40 secondo fasce dell’art.14, non aggiunti tal quali. Certificato agonistico valido per atletica o altro sport tabellaB DM18 febbraio1982 da specialista abilitato. Usare questo esempio ispettivo e il relativo allegato4, non quello69ufficiali.

Tracciabilità: [[topics/m-sp01-forze-ordine-percorsi-prove]]; [[entities/ministero-interno]]. Le letture sono mirate ai claim citati, non attestano una nuova lettura integrale di ogni allegato né un censimento di tutti gli avvisi successivi.
'''
t=t.replace('checked_at: 2026-08-13','checked_at: 2026-10-03').replace('updated_at: 2026-08-13T00:00:00+02:00','updated_at: 2026-10-03T00:00:00+02:00')
p.write_text(t,encoding='utf-8')
raw=Path('wiki/raw/correzioni-collana-2026-10-02/ps1000-bando-2026-completo.pdf'); assert not raw.exists(); shutil.copyfile('artifacts/correzioni-collana-2026-10-02/ps1000-complete.pdf',raw)
p=S/(names[2]+'.md'); t=p.read_text(encoding='utf-8'); start=t.index('**Il principio generale, comune'); end=t.index('**Da tenere fuori',start)
t=t[:start]+'''L’art. 26 della legge 53/1989 rinvia alle qualità morali e di condotta richieste per l’accesso alla magistratura ordinaria. Questo requisito deve essere coordinato con le autonome cause ostative contenute negli ordinamenti e nel bando. Non significa che ogni causa di esclusione sia stata abolita o trasformata in valutazione discrezionale.

La Corte costituzionale, sentenza 40/2024, ha eliminato dall’art. 6, comma 1, lettera i), del D.Lgs. 199/1995 la sola previsione della guida in stato di ebbrezza costituente reato quale causa automatica di esclusione dal reclutamento GdF. Resta l’esame individuale della condotta; la decisione non assicura l’ammissione e non riguarda indistintamente altri illeciti, sostanze o accertamenti. Il dispositivo e i paragrafi 3.3–5 sono stati riscontrati il 3 ottobre 2026 sulla pagina ufficiale https://www.cortecostituzionale.it/scheda-pronuncia/2024/40. La precedente frase «un fatto pregresso non produce mai un’esclusione automatica» era eccessiva ed è ritirata.

''' +t[end:]
t=t.replace('resta la fonte per l\'idoneità **psichica e attitudinale**. Non lo è più per la statura.','continua a disciplinare, nel proprio ambito Polizia di Stato, anche gli altri requisiti fisici e sanitari oltre a quelli psichici e attitudinali. Il superamento dei limiti di statura non abroga l’intero regolamento e non ne estende l’ambito ad Arma o GdF.')
p.write_text(t,encoding='utf-8')
p=S/(names[1]+'.md'); t=p.read_text(encoding='utf-8'); t=t.replace("Quest'ultimo resta rilevante per l'idoneità psichica e attitudinale.","Quest’ultimo conserva anche altri requisiti fisici e sanitari della Polizia di Stato; non si applica indistintamente ad Arma e Guardia di finanza.")
t=t.replace('è a costo zero: chi non se la sente rinuncia senza penalità','non comporta perdita dell’idoneità già raggiunta se non superato secondo il bando applicabile; prepararlo richiede comunque tempo e carico fisico')
t+='''

## Rettifica di ambito del 3 ottobre 2026

Le tabelle storiche sopra non sono parametri universali dei corpi. Prima di usarle occorre associare il documento tecnico alla specifica procedura, ruolo, sesso e versione. Per il capitolo 04 si adotta come esempio completo nel perimetro il bando **983 allievi marescialli GdF 2026**, art.14 e allegato4, non il bando69ufficiali escluso dal modulo. Struttura, bonus e certificato sono consolidati nella sezione di riscontro di [[sources/bandi-rappresentativi-m-sp01-forze-polizia-2026]]. Evitare prescrizioni di allenamento o deduzioni personali di idoneità sanitaria. La condotta segue la sintesi rettificata della sentenza40/2024 nella fonte ordinamentale: non esiste una generale eliminazione delle cause ostative.
'''
p.write_text(t,encoding='utf-8')
print('Consolidate 3 fonti SP01; originale PS1000 completo acquisito')
