---
id: source-vol-04-digitale-verifica-2026-10-03
type: source
title: "VOL-04 — Depositi telematici: verifica del 3 ottobre 2026"
status: consolidated
domain: concorsi pubblici italiani
topics: [giustizia digitale, processo civile telematico, processo penale telematico]
entities: [Ministero della giustizia, Codice di procedura civile, Codice di procedura penale]
source_refs: ["sources/vol-04-processo-civile-verifica-2026-10-03.md", "sources/vol-04-processo-penale-verifica-2026-10-03.md"]
book_refs: [m-fc04-giustizia, vol-04-giustizia-upp]
source_type: normativa-e-documentazione-istituzionale
source_url: https://pst.giustizia.it/PST/it/paginadettaglio.page?contentId=ACC3429
source_date: 2026-10-03
authority_level: primaria
confidence: 0.98
created_at: 2026-10-03
updated_at: 2026-10-03
review_required: false
canonical: true
tags: [source, vol-04, correzioni-collana]
---

# Depositi telematici — fonti e controllo temporale

Raw immutabili in `wiki/raw/correzioni-vol04-2026-10-03`; estratti e manifest `norme-vol04/manifest-digitale*.json`. I precedenti raw `wiki/raw/m-fc04-giustizia/dm-114-2026-processo-penale-telematico.html` e analoghi sono schede GU, non testo degli articoli: non bastano alla verifica. Acquisiti separatamente art. 1 D.M. 114 e art. 3 D.M. 217 vigente. Letti integralmente gli articoli indicati sotto; per il PDF di 28 pagine letti artt. 7, 15–17 e 19 e le due rettifiche, non attestata lettura integrale di tutti gli altri articoli.

## PCT: aggiornamento della regola temporale

L'art. 196-sexies disp. att. c.p.c. rinvia alla conferma del completamento della trasmissione secondo la disciplina anche regolamentare: tempestività entro fine giorno, art. 155 commi 4–5, più trasmissioni per superamento dimensioni. Il vigente art. 13 D.M. 44/2011, modificato dal D.M. 217/2023, rinvia alle specifiche per la conferma della trasmissione.

**Non applicare automaticamente la vecchia regola della seconda PEC.** [Specifiche 7 agosto 2024](https://pst.giustizia.it/PST/it/paginadettaglio.page?contentId=ACC3429), efficaci dal 30 settembre 2024, art. 17 comma 11: in caso di accettazione dell'atto, anche dopo intervento di cancelleria, effetto dal momento della ricevuta di accettazione del gestore PEC **del depositante**, ossia prima PEC/RdA. RdAC è invece consegna alla casella destinataria. Il buon fine rimane necessario; la sola prima PEC non sana una busta FATAL rifiutata. L’ipotesi iniziale di correzione centrata sulla sola RdAC è stata aggiornata dopo il confronto con le specifiche e la rassegna della Cassazione. L’audit storico rimane immutato.

Conferma interpretativa primaria: [Cassazione, Rassegna tematica aggiornata al 30 giugno 2025](https://www.cortedicassazione.it/resources/cms/documents/Rassegna_tematica_aggiornata_al_30_giugno_2025.pdf), pagine stampate 109–110 (PDF 112–113), §5: distingue espressamente disciplina previgente della seconda PEC e nuovo momento della prima PEC condizionato al buon fine. È relazione di studio, non sentenza che sostituisca il testo normativo. La ricerca ha restituito commenti alla n. 23286/2026 sulla seconda PEC ma senza testo primario né individuazione del regime temporale della fattispecie: non usati per sovrascrivere la norma attuale o come fonte del capitolo.

Art. 17 commi 8–11: WARN non bloccante (esempi della fonte: procura mancante, certificato firma non valido, mittente non firmatario); ERROR richiede intervento cancelleria per consentire accettazione; FATAL non gestibile, es. impossibilità decifrare o elementi essenziali mancanti, comunicazione PEC di rifiuto. Non assimilare ogni firma mancante a FATAL. Accettazione automatica salvo anomalie/casi che richiedono operatori. [Circolare 19 settembre 2024](https://pst.giustizia.it/PST/resources/cms/documents/m_dg.DOG07.19092024.0034552.U_20240916_Comunicazione_Dip._su_accetta.pdf), lette 8 pagine: attivazione dal 30 settembre per tipologie enumerate; quattro messaggi conservati, quarto specifica automatico/manuale. WARN/ERROR esclusi dalla prima implementazione automatica, non significa rifiuto automatico del deposito. Non generalizzare la lista di rilascio 2024 a ogni successiva versione dei sistemi.

Art. 15: atto principale PDF/PDF-A testuale, selezionabile, non scansione, senza elementi attivi/password, firma digitale o qualificata e dati XML civili firmati; eccezione scansione penale degli atti formati personalmente secondo requisiti specifici. Allegati art. 16 hanno formati ulteriori e firma quando prevista dalla legge, non tutti firmati indiscriminatamente. Rettifica 16 settembre 2024: art. 17 comma 4 limite 60 MB riferito ad **Atto.enc**, non intera busta MIME. Art. 19 comma 15 PDP 60 MB/file, 600 MB/deposito. Non confondere limiti né limite del gestore PEC con norma processuale.

## PPT e calendario vigente

Art. 111-bis c.p.p.: regola telematica coordinata al transitorio; esclusi documenti non acquisibili in copia per natura/esigenze; parti e persona offesa possono depositare personalmente anche non telematicamente. Art. 172 comma 6-bis già acquisito nella verifica penale: termine sino ore 24, accettazione dal sistema entro termine. Art. 13-bis D.M. 44: ricevuta del portale, non quattro PEC civili. Art. 19 specifiche: ricevuta PDF con identificativo anno/numero, dati, data/ora invio rilevati dai sistemi ministeriali; stati inviato/in transito/accettato/in verifica/rifiutato/errore tecnico. **Rettifica 30 ottobre 2024**: per denuncia/querela/istanza di procedimento accoglimento = ricevimento nel ReGeWEB, non automatica iscrizione del procedimento. Il richiamo numerico alla lettera nella rettifica non coincide con numerazione materiale del PDF, ma la frase sostituita è univoca.

[Art. 3 D.M. 217/2023 vigente](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto:2023-12-29;217~art3!vig=), letto integralmente. Regola 1 gennaio 2025 per Procura ordinaria/EPPO/GIP/tribunale/PG avocazione. Deroghe commi 2–3 cessate 31 dicembre 2025, 3-ter cessata 31 marzo 2026; comma 3-bis intercettazioni soggetti interni fino 31 dicembre 2026. Non scrivere che queste deroghe sono tutte ancora aperte.

[D.M. 114/2026 art. 1](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.versione=1&art.idGruppo=0&art.flagTipoArticolo=0&art.codiceRedazionale=26G00134&art.idArticolo=1&art.idSottoArticolo=1&art.idSottoArticolo1=10&art.dataPubblicazioneGazzetta=2026-06-30&art.progressivo=0) vigente dal 30 giugno: comma 5 appello/PG 1 luglio 2027, Cassazione/PG/GdP 1 gennaio 2028, con esclusioni specifiche; minorile 1 gennaio 2029, tribunale sorveglianza 1 gennaio 2030. Comma 5-bis impugnazioni GdP 1 gennaio 2028, sezione appello minori 1 gennaio 2029, libro X esecuzione 1 luglio 2029; libri IV titolo I capo VIII (riparazione ingiusta detenzione), IX titoli III-bis/IV (rescissione/revisione), XI, prevenzione/MAE/consegna 1 luglio 2030. Comma 6 facoltativo esterni appello sino 30 giugno 2027 e Cassazione/GdP sino 31 dicembre 2027; comma 7 ulteriori attivazioni previo provvedimento funzionalità pubblicato PST. Comma 9 PEC difensori ex87-bis D.Lgs150 nei casi ammessi anche nontelematico, non alternativa universale al PDP obbligatorio.

## Malfunzionamenti e registri

196-quater civile: capo ufficio autorizza nontelematico per urgenza + certificazione ministeriale indisponibilità pubblicata PST. Giudice può ordinare singoli originali/copie cartacei necessari a decidere con ragione specifica. 175-bis penale: certificazione centrale oppure malfunzionamento locale accertato/attestato dal dirigente, comunicazioni con intervallo; durante malfunzionamento modalità nontelematiche; restituzione nel termine richiede prova caso fortuito/forza maggiore dell'impossibilità anche della via sostitutiva, non proroga automatica.

Spec. art. 7 e scheda PST ReGIndE: Registro generale degli indirizzi elettronici, Ministero, dati/PEC dei soggetti abilitati esterni, non elenco universale dei cittadini. Scheda vecchia contiene richiami CEC-PAC/modalità autenticazione non assunti attuali; per categorie base usato art. 7 del 2024. CAD6-bis INI-PEC imprese/professionisti e ulteriori registri professionali previsti;6-ter IPA ora include **società a controllo pubblico** oltre PA/gestori, non usare nome abbreviato come elenco esaustivo;6-quater INAD persone fisiche/professionisti/altri enti privati non obbligatiINI-PEC. Registro PP.AA. del Ministero distinto da IPA, non equivalenza automatica per notificazioni; elenco concretamente utilizzabile dipende dalla disciplina processuale.

## Impatto

Capitolo12: quattro ricevute spiegate, nuovo dies temporale, tre anomalie, automatismo, limiti dimensionali, calendarioPPT operativo, tre dossier con orari/esiti e soluzione12punti; sei quiz quattro alternative. Apparato17 aggiornato. [[topics/giustizia-e-upp]] e [[entities/ministero-della-giustizia]].
