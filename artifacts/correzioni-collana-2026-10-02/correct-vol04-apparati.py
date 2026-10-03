from pathlib import Path
import re,json,hashlib
B=Path('wiki/books/moduli/m-fc04-giustizia/chapters');A=Path('artifacts/correzioni-collana-2026-10-02')
sources=['organizzazione-upp','processo-civile','processo-penale','cancelleria','spese','casellario','unep','digitale','minorile-penitenziario']
refs=[f'sources/vol-04-{s}-verifica-2026-10-03.md' for s in sources]
for ref in refs: assert (Path('wiki')/ref).exists(),ref
rows=[]
for n in [15,16,17]:
 p=next(B.glob(f'{n:02}-*'));t=p.read_text('utf-8');before=hashlib.sha256(p.read_bytes()).hexdigest()
 fm,body=t.split('---',2)[1:]
 fm=fm.replace('status: reviewed','status: revised_draft').replace('draft_stage: reviewed','draft_stage: editorial-revision').replace('review_required: false','review_required: true').replace('updated_at: 2026-08-18T12:00:00+02:00','updated_at: 2026-10-03T12:00:00+02:00')
 fm=re.sub(r'source_refs: \[.*?\]', 'source_refs: '+json.dumps(refs,ensure_ascii=False),fm,flags=re.S)
 if n==15:
  body=body.replace('| Distingue dichiarazioni','| Distingui dichiarazioni')
  start=body.index('## Appendice E —');end=body.index('## Strumento 1',start)
  body=body[:start]+'''## Appendice E — Orientamento verso Magistratura, Avvocatura e Notariato

Il VOL-04 riguarda profili amministrativi, UPP e servizi della giustizia. Per orientarsi alle selezioni giuridiche specialistiche, il riferimento della collana è **VOL-12, Carriere speciali premium**, parte **Magistratura, Avvocatura e Notariato**: sezioni «Mappa delle tre professioni e scelta del binario», «Magistratura ordinaria: accesso, prove e ordinamento» e «Metodo per tema, atto e prova teorico-pratica».

Quel percorso insegna a distinguere accesso, prove e organizzazione della preparazione. Non sostituisce lo studio istituzionale completo delle materie o una preparazione specialistica ai temi. La conoscenza amministrativa di un fascicolo non coincide con la capacità richiesta al concorso in magistratura.

Per le basi comuni, usa **VOL-01, Il Metodo BANDO**: «Costituzione e ordinamento dello Stato» per organi e funzioni, «Diritto amministrativo essenziale» per attività amministrativa, «PA digitale, CAD e gestione documentale» per documenti e servizi digitali; cerca questi titoli nell'indice. Per la pratica di questo volume, torna invece ai capitoli 5–14 e alle simulazioni seguenti: il rinvio al base non sostituisce le regole processuali insegnate qui.

''' +body[end:]
  start=body.index('| Data | Materia |');end=body.index('Classifica come',start)
  body=body[:start]+'''Compila una scheda per ogni errore: la disposizione verticale lascia spazio a una regola completa.

| Campo | Annotazione |
|---|---|
| Data e materia | … |
| Domanda o caso | … |
| Tipo | Nozione / lettura / metodo / distrazione |
| Causa concreta | … |
| Regola corretta e riferimento | … |
| Azione di recupero | Rileggere / schematizzare / rifare |
| Nuova verifica | Data, esito e dubbio residuo |

''' +body[end:]
  start=body.index('## Strumento 4');end=body.index('## Strumento 5',start)
  root=(A/'VOL-04-simulazioni-uffici.md').read_text('utf-8')
  other=(A/'VOL-04-simulazioni-minorile-penitenziario.md').read_text('utf-8')
  other=other[other.index('## Simulazione minorile'):].replace('## Simulazione minorile','## Simulazione 5 — Minorile').replace('## Simulazione penitenziaria','## Simulazione 6 — Penitenziario')
  body=body[:start]+'''## Strumento 4 — Laboratorio finale per profilo

Le sei simulazioni contengono documenti fittizi, consegne, soluzioni e rubriche. Scegli quelle pertinenti al tuo bando. Lavora prima senza consultare la soluzione; correggi poi elemento per elemento. La prova civile e quella penale allenano anche il supporto UPP; le altre coprono cancelleria, UNEP, servizi minorili e penitenziari.

'''+root+'\n\n'+other+'\n\n'+body[end:]
 if n==16:
  body=body.replace('Torna alla matrice profilo-materia-output','Torna alla griglia «Profilo-materia-output» del capitolo 15')
  body=body.replace('Scegli una simulazione, svolgila senza consultare il testo, correggila con la griglia e aggiorna il diario degli errori.','Scegli nel capitolo 15 la simulazione del tuo profilo: scheda UPP civile, segreteria penale, cancelleria, UNEP, minorile o penitenziario. Svolgila nel tempo indicato, correggila con la soluzione e la rubrica, quindi aggiorna il diario degli errori. Usa i casi svolti nei capitoli 5–14 per recuperare le singole difficoltà.')
  body+='\n\nLe competenze qui esercitate riguardano il perimetro dichiarato dal volume. Se il bando richiede discipline pedagogiche, sociali o giuridiche ulteriori, inseriscile nel piano con materiali specifici: la riuscita nelle sei simulazioni non certifica la copertura di ogni possibile programma.\n'
 if n==17:
  body='''

# Fonti e riferimenti essenziali

Il volume è aggiornato al **3 ottobre 2026**. I riferimenti seguenti collegano i capitoli alle disposizioni e ai servizi ufficiali. Per i testi normativi usa la versione vigente alla data rilevante; per un caso storico controlla anche il testo allora applicabile. I collegamenti sono strumenti di verifica, mentre regole, esempi e soluzioni necessarie alle attività del volume sono spiegati nei capitoli.

## Organizzazione, ordinamento e UPP — capitoli 1–5

- R.D. 30 gennaio 1941, n. 12, ordinamento giudiziario, in particolare artt. 42, 48, 56, 65, 70 e 73, con disposizioni transitorie.
- D.Lgs. 25 luglio 2006, n. 240, artt. 1–4: capo dell'ufficio, dirigente amministrativo, risorse e programma annuale.
- D.Lgs. 10 ottobre 2022, n. 151, artt. 1–9: struttura, progetti, composizione e compiti degli UPP.
- D.L. 12 giugno 2026, n. 100, convertito senza modificazioni dalla L. 7 agosto 2026, n. 145: [legge di conversione, GU 8 agosto 2026](https://www.gazzettaufficiale.it/eli/id/2026/08/08/26G00164/SG).
- D.L. 7 agosto 2026, n. 144, art. 7: ulteriore intervento sui compiti del personale. Alla data di aggiornamento il procedimento di conversione richiede ancora monitoraggio: controllare la pubblicazione finale, non soltanto una votazione parlamentare.
- Ministero della giustizia, [articolazione degli uffici](https://www.giustizia.it/giustizia/page/it/articolazione_degli_uffici) e [dipartimenti](https://www.giustizia.it/giustizia/page/it/dipartimenti): organigramma da distinguere dalle denominazioni storiche ancora presenti negli atti tecnici.

## Procedura civile, penale e cancelleria — capitoli 5–8

- Codice di procedura civile, R.D. 28 ottobre 1940, n. 1443: artt. 132–135, 155, 163-bis, 165–167, 171-bis e 171-ter, 183, 281-decies e seguenti, 325–327, 409 e seguenti. [Testo vigente su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1940-10-28;1443).
- Disposizioni di attuazione del c.p.c., R.D. 18 dicembre 1941, n. 1368: art. 76 per la consultazione e artt. 196-quater e seguenti per il digitale.
- L. 7 ottobre 1969, n. 742, artt. 1 e 3, sospensione feriale e relative esclusioni, da coordinare con il tipo di procedimento.
- Codice di procedura penale, D.P.R. 22 settembre 1988, n. 447: artt. 60–61, 116, 172, 335 e seguenti, 405–415-bis, 425, 431, 438 e seguenti, 444, 459, 533, 544, 548, 550, 554-ter, 585, 648, 650, 655–656, 665–666. [Testo vigente su Normattiva](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1988-09-22;447).
- D.Lgs. 10 ottobre 2022, nn. 149, 150 e 151, e correttivi successivi: sono atti di riforma, da leggere attraverso le disposizioni vigenti che modificano.

## Spese, patrocinio, casellario e UNEP — capitoli 9–11

- D.P.R. 30 maggio 2002, n. 115: contributo unificato, artt. 9–16; anticipazioni art. 30; domanda di liquidazione e decadenze art. 71; patrocinio artt. 74–79, 91–99, 107, 112, 124–136; liquidazione e opposizione artt. 165, 168, 170 e 199; recupero artt. 208, 227-bis, 227-ter e 248. [Testo unico vigente](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2002-05-30;115).
- Decreto 22 aprile 2025, adeguamento del limite reddituale per il patrocinio, [GU n. 159 dell'11 luglio 2025](https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.codiceRedazionale=25A03904&atto.dataPubblicazioneGazzetta=2025-07-11&tipoSerie=serie_generale&tipoVigenza=originario).
- D.Lgs. 1° settembre 2011, n. 150, art. 15, opposizione alle liquidazioni. Corte costituzionale n. 106/2016 per il termine dell'opposizione; n. 137/2026 sul contributo minimo e accesso alla giustizia.
- Ministero, [circolare 24 aprile 2025 sul contributo minimo e patrocinio](https://www.giustizia.it/giustizia/page/it/provvedimento_ministeriale_selezionato?contentId=SDC1454004); [servizi per liquidazione e SPEdiGIUS](https://www.giustizia.it/giustizia/page/it/come_fare_per_liquidazioni_spese_giustizia?tab=f).
- D.P.R. 14 novembre 2002, n. 313: iscrizioni ed eliminazione artt. 3 e 5; certificati artt. 24, 25-bis e 27; acquisizioni, controversie e visura artt. 39–42. [Testo unico vigente](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2002-11-14;313).
- Ministero, [certificato del datore di lavoro: domande frequenti](https://www.giustizia.it/giustizia/it/mg_3_3_7.page?tab=f) e [carichi pendenti](https://www.giustizia.it/giustizia/it/mg_3_3_3.page?tab=w).
- D.P.R. 15 dicembre 1959, n. 1229, ordinamento UNEP, artt. 106–107; c.p.c. artt. 137–148, 474–482, 492 e 492-bis, 497, 513–518, 543, 555–557, 608, 615 e 617; codice civile artt. 1206–1210 sull'offerta e mora del creditore.
- [Corte costituzionale n. 3/2010](https://www.cortecostituzionale.it/scheda-pronuncia/2010/3): perfezionamento della notificazione ex art. 140 c.p.c. per il destinatario.

## Giustizia digitale e dati — capitoli 8 e 12

- D.M. 21 febbraio 2011, n. 44, artt. 13 e 13-bis, nel testo vigente; art. 196-sexies disp. att. c.p.c.; artt. 111-bis, 172 comma 6-bis e 175-bis c.p.p.
- [Specifiche tecniche del 7 agosto 2024 e rettifiche del 16 settembre e 30 ottobre 2024](https://pst.giustizia.it/PST/it/paginadettaglio.page?contentId=ACC3429): artt. 7, 15–17 e 19. Per il PCT, l'art. 17 comma 11 va letto nel regime attuale, senza trasferirvi automaticamente la regola previgente della seconda PEC.
- [Circolari sull'accettazione automatica](https://pst.giustizia.it/PST/it/paginadettaglio.page?contentId=ACC3517), con indicazioni distinte per civile, penale e Cassazione.
- D.M. 29 dicembre 2023, n. 217, art. 3, modificato dai D.M. 206/2024, 206/2025 e [114/2026](https://www.gazzettaufficiale.it/eli/id/2026/06/30/26G00134/sg): calendario transitorio dei depositi penali.
- Corte di cassazione, [Rassegna tematica aggiornata al 30 giugno 2025](https://www.cortedicassazione.it/resources/cms/documents/Rassegna_tematica_aggiornata_al_30_giugno_2025.pdf), pagine stampate 109–110: relazione di studio sul deposito, distinta da una decisione giurisdizionale.
- D.Lgs. 7 marzo 2005, n. 82, artt. 6-bis, 6-ter e 6-quater: INI-PEC, IPA e INAD; [PST Giustizia](https://pst.giustizia.it) per servizi, ReGIndE e attestazioni di malfunzionamento.
- Regolamento (UE) 2016/679, artt. 9 e 10; D.Lgs. 196/2003, art. 2-octies; D.Lgs. 18 maggio 2018, n. 51, per i trattamenti delle autorità competenti con finalità penali previste. Non estendere indiscriminatamente il medesimo regime a ogni trattamento dell'ufficio.

## Minorile, comunità e penitenziario — capitoli 13–14

- Codice penale artt. 97–98 e 168-bis e seguenti; c.p.p. artt. 464-bis e seguenti: età, imputabilità e prova adulta.
- D.P.R. 22 settembre 1988, n. 448, in particolare artt. 9, 28 e 29; D.Lgs. 28 luglio 1989, n. 272: processo e servizi minorili. Coordinare le disposizioni con Corte costituzionale nn. 125/1995, 203/2025 e 110/2026 nei punti trattati.
- D.Lgs. 2 ottobre 2018, n. 121, artt. 2–8: esecuzione minorile e misure penali di comunità.
- D.Lgs. 10 ottobre 2022, n. 150, artt. 42–58: definizioni, accesso, consenso, garanzie, programmi ed esiti della giustizia riparativa.
- L. 26 luglio 1975, n. 354, artt. 4-bis, 13–15, 21, 30-ter, 35-bis e 35-ter, 47 e seguenti, 54, 59–61 e 69; D.P.R. 30 giugno 2000, n. 230, in particolare artt. 27 e 29, da coordinare con la legge successiva; art. 656 c.p.p. e Corte costituzionale n. 41/2018 sulla sospensione dell'ordine di esecuzione.
- Corte costituzionale [n. 99/2019](https://www.cortecostituzionale.it/scheda-pronuncia/2019/99), [n. 253/2019](https://www.cortecostituzionale.it/scheda-pronuncia/2019/253), [n. 10/2024](https://www.cortecostituzionale.it/scheda-pronuncia/2024/10): rispettivamente salute psichica, permessi e reati ostativi, affettività; gli effetti vanno coordinati alle norme vigenti, come spiegato nel capitolo 14.
- Corte EDU, *Torreggiani e altri c. Italia*, 8 gennaio 2013, ricorso n. 43517/09 e altri: [testo della sentenza, traduzione italiana del Ministero su HUDOC](https://hudoc.echr.coe.int/app/conversion/pdf/?filename=001-116248.pdf&id=001-116248&library=ECHR). Il [comunicato stampa coevo](https://hudoc.echr.coe.int/app/conversion/pdf?filename=Chamber+judgment+Torreggiani+and+Others+v.+Italy+08.01.2013.pdf&id=003-4212710-5000451&library=ECHR) è un documento distinto e non sostituisce la pronuncia.

## Controllo prima della prova

Confronta bando, testo vigente e data del caso. Per organigrammi e servizi consulta il Ministero; per i depositi anche il PST; per prassi locali il sito dell'ufficio. Registra disposizione, data e modifica rilevante nel diario degli errori. Un avviso locale non vale automaticamente in ogni ufficio e una disciplina con efficacia futura non è già applicabile oggi.
'''
 t='---'+fm+'---'+body;p.write_text(t,'utf-8');rows.append(dict(chapter=n,path=p.as_posix(),before=before,after=hashlib.sha256(p.read_bytes()).hexdigest(),words=len(t.split())))
(A/'VOL-04-apparati-delta.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),'utf-8');print(rows)
