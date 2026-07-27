# Agent Memory Scenarios

## 2026-05-27T21:45:00.000Z - global

- conversation_id: conv-20260527214500-always-on-memory
- route: codex-user-preference
- l0: l0/conv-20260527214500-always-on-memory.md
- atoms:
  - mem-20260527214500-always-on-memory | preference | Nel contesto ConcorsoBook OS la memoria locale deve restare sempre attiva per ricordare cio' che e' stato detto e migliorare progressivamente gli output.

## 2026-05-27T21:55:00.000Z - global

- conversation_id: conv-20260527215500-shared-provider-memory
- route: codex-user-preference
- l0: l0/conv-20260527215500-shared-provider-memory.md
- atoms:
  - mem-20260527215500-shared-provider-memory | instruction | La memoria persistente del progetto deve essere condivisa da tutti gli agenti e provider usati: Codex/GPT, Claude, Kimi, OpenAI API, Hermes e locale.

## 2026-05-28T00:50:00.000Z - global

- conversation_id: conv-20260528005000-ruflo-stop-hook-patch
- route: codex-system-maintenance
- l0: l0/conv-20260528005000-ruflo-stop-hook-patch.md
- atoms:
  - mem-20260528005000-ruflo-stop-hook-patch | system-fix | L'avviso ricorrente Stop hook failed era causato dallo Stop hook di Claude/Ruflo ruflo-core 0.2.0 che chiamava npx claude-flow@alpha; il file hooks.json globale e' stato patchato per wrappare quei comandi con cmd /c e fallback exit 0 tramite node.

## 2026-05-27T23:13:08.944Z - global

- conversation_id: conv-20260527231308-1pogjhn
- route: codex/resolve-skill-and-mcp-warnings
- l0: l0/conv-20260527231308-1pogjhn.md
- atoms:
  - mem-20260527231308-116gwtz | project_fact | Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS.
  - mem-20260527231308-10gu8jz | result | Esito codex/resolve-skill-and-mcp-warnings: Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS. -> Corretti 17 SKILL.md con frontmatter YAML valido, description presente e sotto 1024 caratteri; rigenerata autenticazione OAuth del MCP Supabase con codex mcp logout/login.

## 2026-05-28T11:43:54.020Z - global

- conversation_id: conv-20260528114354-1rtulm9
- route: codex/resolve-heygen-skill-cache-warnings
- l0: l0/conv-20260528114354-1rtulm9.md
- atoms:
  - mem-20260528114354-1hznga7 | result | Esito codex/resolve-heygen-skill-cache-warnings: Gli avvisi continuano a uscire per HeyGen 719ed655: heygen-avatar e heygen-video hanno description oltre 1024 caratteri. -> Corretti i due SKILL.md HeyGen nel cache 719ed655 e le due copie sorgente temporanee in .codex/.tmp/plugins/plugins/heygen; validazione finale: 4 copie controllate, tutte valide.

## 2026-05-28T15:48:49.069Z - global

- conversation_id: conv-20260528154849-4kjfkk
- route: codex/adapt-book-layout-from-docx
- l0: l0/conv-20260528154849-4kjfkk.md
- atoms:
  - mem-20260528154849-1cefyks | project_fact | Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini.
  - mem-20260528154849-l23wje | result | Esito codex/adapt-book-layout-from-docx: Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini. -> Aggiornata la preview editoriale a 16,8 x 24 cm con Playfair Display, Montserrat, palette Navy/Bordeaux/Muted Gold, barra BANDO e callout box; mantenuto colore pagina esistente e margini ottimizzati.

## 2026-05-28T16:05:00.000Z - global

- conversation_id: conv-20260528160500-dashboard-next-cache
- route: codex/fix-dashboard-next-cache
- l0: l0/conv-20260528160500-dashboard-next-cache.md
- atoms:
  - mem-20260528160500-dashboard-next-cache | system-fix | Errore dashboard Cannot find module './331.js' risolto fermando il processo Next su porta 3000, eliminando solo la cache generata .next e riavviando npm run dev su 127.0.0.1:3000; verificati / e /api/book-studio/assets/file con HTTP 200 e screenshot artifacts/dashboard-check.png.

## 2026-05-28T17:55:00.000Z - global

- conversation_id: conv-20260528175500-ch12-logic-corpus
- route: codex/ingest-chapter-12-logic-corpus
- l0: l0/conv-20260528175500-ch12-logic-corpus.md
- atoms:
  - mem-20260528175500-ch12-logic-corpus | result | Preparato il knowledge pack per il capitolo 12 Logica, comprensione del testo e ragionamento: scaricati 19 PDF leciti in wiki/raw/chapter-12-logica-comprensione-ragionamento, creati 5 source notes, 4 topic pages, aggiornati index/log e portato il capitolo a status knowledge-ready preservando le note pregresse.

## 2026-05-28T20:25:00.000+02:00 - global

- conversation_id: conv-20260528202500-ch12-editorial-draft
- route: codex/write-chapter-12-editorial-draft
- l0: l0/conv-20260528202500-ch12-editorial-draft.md
- atoms:
  - mem-20260528202500-ch12-editorial-draft | result | Scritto il Testo editoriale professionale del capitolo 12 Logica, comprensione del testo e ragionamento: capitolo in status revised_draft/editorial-revision, con mappa BANDO, metodi per logica, comprensione, ragionamento critico e numerico, diario errori, domanda commissario, mini-esercizio e mini-simulazione originale da 25 quesiti.

## 2026-05-28T20:38:00.000+02:00 - global

- conversation_id: conv-20260528203800-editorial-proofread-chapters
- route: codex/editorial-proofread-chapters
- l0: l0/conv-20260528203800-editorial-proofread-chapters.md
- atoms:
  - mem-20260528203800-editorial-proofread-chapters | result | Revisione editoriale capillare dei capitoli scritti del Metodo BANDO: audit da Introduzione a Capitolo 12, rimozione di sezioni interne dal Capitolo 12, pulizia di link wiki visibili, correzione di accenti/sintassi/titoli e microcorrezioni nel Capitolo 9 Contratti pubblici; git diff --check e test preview libro passati.

## 2026-05-28T23:05:00.000+02:00 - global

- conversation_id: conv-20260528230500-front-matter-pages
- route: codex/front-matter-pages
- l0: l0/conv-20260528230500-front-matter-pages.md
- atoms:
  - mem-20260528230500-front-matter-pages | result | Integrate servizi digitali con QR, frontespizio, copyright/colophon, sommario, premessa e indice generato in Book Studio.

## 2026-05-28T23:56:00.000+02:00 - global

- conversation_id: conv-20260528235600-editorial-frontmatter-index-polish
- route: codex/editorial-frontmatter-index-polish
- l0: l0/conv-20260528235600-editorial-frontmatter-index-polish.md
- atoms:
  - mem-20260528235600-editorial-frontmatter-index-polish | result | Revisione editoriale front matter/capitoli scritti, rimozione note interne, correzione accenti e nuovo layout indice compatto verificato in dashboard.

## 2026-05-29T00:26:00.000+02:00 - global

- conversation_id: conv-20260529002600-index-editorial-toc-layout
- route: codex/index-editorial-toc-layout
- l0: l0/conv-20260529002600-index-editorial-toc-layout.md
- atoms:
  - mem-20260529002600-index-editorial-toc-layout | result | Indice trasformato in sommario tipografico con parti, capitoli, sottocapitoli numerati, puntini guida e numeri pagina stimati.

## 2026-05-29T13:35:00.000+02:00 - global

- conversation_id: conv-20260529133500-ch09-editorial-images
- route: codex/illustrate-chapter-09-contracts
- l0: l0\conv-20260529133500-ch09-editorial-images.md
- atoms:
  - mem-20260529133500-ch09-editorial-images | result | Capitolo 9 Contratti pubblici essenziali illustrato con 6 figure professionali SVG+PNG: mappa generale, ciclo fabbisogno-esecuzione, procedure/concorrenza, documenti-offerte-stipula, ecosistema digitale BDNCP/PCP/FVOE/CIG, sintesi portale-controlli-responsabilita; preview Playwright verificata con 6 immagini caricate e nessuna sovrapposizione footer.

## 2026-05-29T13:45:00.000+02:00 - global

- conversation_id: conv-20260529134500-ch12-quiz-layout
- route: codex/ch12-quiz-layout
- l0: l0\conv-20260529134500-ch12-quiz-layout.md
- atoms:
  - mem-20260529134500-ch12-quiz-layout | result | Capitolo 12 riorganizzato nella parte esercizi/quesiti: schede tabellari a blocchi tematici, quesito prima delle risposte, soluzioni ragionate separate.

## 2026-05-29T18:22:13.032Z - global

- conversation_id: conv-20260529182213-djvsvf
- route: codex/chapter09-image-audit
- l0: l0/conv-20260529182213-djvsvf.md
- atoms:
  - mem-20260529182213-16onnkx | workflow | Effettua un controllo capillare sulle immagini inserite all'interno del capitolo 9, perchÃ© i testi di alcune escono dai margini e non sono ottimizzate.
  - mem-20260529182213-jo8qr4 | result | Esito codex/chapter09-image-audit: Effettua un controllo capillare sulle immagini inserite all'interno del capitolo 9, perchÃ© i testi di alcune escono dai margini e non sono ottimizzate. -> Rifiniti i master SVG/PNG del capitolo 9, in particolare figura 9.3 con barre e nota ampliate; aggiunto audit Playwright dei bounding box testuali negli SVG e controllo di impaginazione A4 per tutte le sei immagini.

## 2026-05-30T12:18:00+02:00 - manual-writer

- conversation_id: conv-20260530121800-ch13-16-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530121800-ch13-16-editorial-draft.md
- atoms:
  - mem-20260530121800-ch13-16-editorial-draft | result | Sviluppati i capitoli 13-16 della Parte III del Metodo BANDO: consolidata conoscenza su metodo di studio, prova a quiz, scritto teorico-pratico, risposta concorsuale e orale; creati 3 source notes, 5 topic pages, aggiornati index/log e scritti i quattro capitoli in status revised_draft.

## 2026-05-30T11:54:30.382Z - global

- conversation_id: conv-20260530115430-jt5ntw
- route: codex/chapter10-editorial-images
- l0: l0/conv-20260530115430-jt5ntw.md
- atoms:
  - mem-20260530115430-2t6ohh | workflow | Passa all'analisi del capitolo 10 e quindi alle immagini necessarie alla loro elaborazione e all'inserimento professionale e capillare, come fatto con il capitolo precedente.
  - mem-20260530115430-p61xax | result | Esito codex/chapter10-editorial-images: Passa all'analisi del capitolo 10 e quindi alle immagini necessarie alla loro elaborazione e all'inserimento professionale e capillare, come fatto con il capitolo precedente. -> Capitolo 10 Informatica, PA digitale e competenze digitali illustrato con 7 figure professionali SVG+PNG: mappa generale, hardware/software/dati, file-Office-dati, Internet/reti/protocolli, sicurezza PA, ecosistema PA...

## 2026-05-30T16:25:00+02:00 - manual-writer

- conversation_id: conv-20260530162500-ch17-18-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530162500-ch17-18-editorial-draft.md
- atoms:
  - mem-20260530162500-ch17-18-editorial-draft | result | Sviluppati i capitoli 17-18 della Parte III del Metodo BANDO: consolidata conoscenza su casi pratici, problem solving amministrativo, quesiti situazionali, competenze trasversali PA, soft skills, etica pubblica e orientamento al cittadino; creati 3 source notes, 7 topic pages, aggiornati index/log e scritti i due capitoli in status revised_draft.

## 2026-05-30T19:25:00+02:00 - manual-writer

- conversation_id: conv-20260530192500-ch19-20-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530192500-ch19-20-editorial-draft.md
- atoms:
  - mem-20260530192500-ch19-20-editorial-draft | result | Sviluppati i capitoli 19-20 della Parte IV del Metodo BANDO: consolidata conoscenza su famiglie concorsuali, mappe profilo, nucleo comune, moduli profilo e bandi rappresentativi; creati 3 source notes, 10 topic pages, aggiornati index/log e scritti i due capitoli in status revised_draft.

## 2026-05-30T17:44:02.585Z - il-metodo-bando

- conversation_id: conv-20260530174402-5ghawm
- route: codex/chapter11-editorial-images
- l0: l0/conv-20260530174402-5ghawm.md
- atoms:
  - mem-20260530174402-1ro8bhv | workflow | Procedi per il capitolo undici come fatto per il capitolo precedente: analisi, immagini necessarie, elaborazione, inserimento professionale e controllo capillare.
  - mem-20260530174402-8g8sec | result | Esito codex/chapter11-editorial-images: Procedi per il capitolo undici come fatto per il capitolo precedente: analisi, immagini necessarie, elaborazione, inserimento professionale e controllo capillare. -> Capitolo 11 Inglese concorsuale essenziale illustrato con 7 figure professionali SVG+PNG: mappa generale, metodo cloze, tempi verbali e segnali, ausiliari/modali, preposizioni-lessico-false friends, reading-email-oral...

## 2026-06-01T14:10:52.386Z - il-metodo-bando

- conversation_id: conv-20260601141052-1w6925h
- route: codex/chapter12-editorial-images
- l0: l0/conv-20260601141052-1w6925h.md
- atoms:
  - mem-20260601141052-odwaqo | workflow | Individua ora le immagini necessarie nel capitolo 12, cosi come gli altri capitoli, genera e inseriscile in maniera professionale e perfetta all'interno del capitolo.
  - mem-20260601141052-1yedyr1 | result | Esito codex/chapter12-editorial-images: Individua ora le immagini necessarie nel capitolo 12, cosi come gli altri capitoli, genera e inseriscile in maniera professionale e perfetta all'interno del capitolo. -> Capitolo 12 Logica, comprensione del testo e ragionamento illustrato con 7 figure professionali SVG+PNG: mappa generale, classificazione dei quesiti, parole logiche, vincoli/serie/pattern, testo e argomento, ragioname...

## 2026-06-05T08:01:44.528Z - manual-writer

- conversation_id: conv-20260605080144-680if7
- route: codex/manual-editorial-flow
- l0: l0/conv-20260605080144-680if7.md
- atoms:
  - mem-20260605080144-af54xy | workflow | Procedi alla scrittura professionale del prossimo capitolo, trova le fonti necessarie a coprire la conoscenza completa e poi procedi.
  - mem-20260605080144-z4j30f | result | Esito codex/manual-editorial-flow: Procedi alla scrittura professionale del prossimo capitolo, trova le fonti necessarie a coprire la conoscenza completa e poi procedi. -> Sviluppato il Capitolo 25 extra del Metodo BANDO, Aggiornare il metodo dopo il libro: salvate raw copies di fonti ufficiali inPA, Gazzetta Ufficiale, Normattiva, DFP/Syllabus, SNA, ANAC, AgID e Garante; creata source ...

## 2026-06-05T15:27:39.658Z - manual-writer

- conversation_id: conv-20260605152739-17xivma
- route: chapter-26-capitale-studio
- l0: l0/conv-20260605152739-17xivma.md
- atoms:
  - mem-20260605152739-15ygvyn | workflow | Ora procediamo con il prossimo capitolo del libro Il Metodo BANDO.
  - mem-20260605152739-ccczzi | result | Esito chapter-26-capitale-studio: Ora procediamo con il prossimo capitolo del libro Il Metodo BANDO. -> Creato il Capitolo 26 extra: Trasformare ogni concorso in capitale di studio.

## 2026-06-05T15:34:38.408Z - manual-writer

- conversation_id: conv-20260605153438-1vwq3p1
- route: chapter-26-source-verification
- l0: l0/conv-20260605153438-1vwq3p1.md
- atoms:
  - mem-20260605153438-gv0of7 | workflow | Per il prossimo capitolo trova le fonti necessarie e procedi con scrittura professionale.
  - mem-20260605153438-1w8a4yh | result | Esito chapter-26-source-verification: Per il prossimo capitolo trova le fonti necessarie e procedi con scrittura professionale. -> Per il Capitolo 26 sono state aggiunte alla source note fonti scientifiche web verificate su active recall, practice testing e spaced practice.

## 2026-06-07T16:41:24+02:00 - manual-writer

- conversation_id: conv-20260607164124-ch27-concorsi-paralleli
- route: chapter-27-concorsi-paralleli
- l0: l0/conv-20260607164124-ch27-concorsi-paralleli.md
- atoms:
  - mem-20260607164124-ch27-workflow | workflow | ok procedi con la scrittura professionale del prossimo capitolo
  - mem-20260607164124-ch27-result | result | Creato il Capitolo 27 extra del Metodo BANDO: Gestire concorsi paralleli senza disperdersi.

## 2026-06-07T18:27:10+02:00 - manual-writer

- conversation_id: conv-20260607182710-ch28-strumenti-digitali
- route: chapter-28-strumenti-digitali
- l0: l0/conv-20260607182710-ch28-strumenti-digitali.md
- atoms:
  - mem-20260607182710-ch28-workflow | workflow | prossimo capitolo scrittura professionale proci / procedio
  - mem-20260607182710-ch28-result | result | Creato il Capitolo 28 extra del Metodo BANDO: Usare il digitale senza perdere il metodo.

## 2026-06-07T18:35:58+02:00 - manual-writer

- conversation_id: conv-20260607183558-ch29-sostenibilita
- route: chapter-29-sostenibilita
- l0: l0/conv-20260607183558-ch29-sostenibilita.md
- atoms:
  - mem-20260607183558-ch29-workflow | workflow | prossimo capitolo procedi
  - mem-20260607183558-ch29-result | result | Creato il Capitolo 29 extra del Metodo BANDO: Reggere la preparazione: energia, ansia e continuita.

## 2026-06-07T16:47:52.612Z - il-metodo-bando

- conversation_id: conv-20260607164752-1qgdro8
- route: codex/chapter14-editorial-images
- l0: l0/conv-20260607164752-1qgdro8.md
- atoms:
  - mem-20260607164752-1mkkbkx | workflow | crea le immagini ora e inseriscile in maniera professionale e precisa nel capitolo come in quelli precedenti
  - mem-20260607164752-1d6liod | result | Esito codex/chapter14-editorial-images: crea le immagini ora e inseriscile in maniera professionale e precisa nel capitolo come in quelli precedenti -> Capitolo 14 La prova a quiz illustrato con 7 figure professionali SVG+PNG: mappa operativa, albero banca dati, scheda tecnica, metodo banca dati in quattro passaggi, routine tre giri, anatomia distrattore, punteggio-d...

## 2026-06-07T18:56:29+02:00 - manual-writer

- conversation_id: conv-20260607185629-ch30-dopo-prova
- route: chapter-30-dopo-prova
- l0: l0/conv-20260607185629-ch30-dopo-prova.md
- atoms:
  - mem-20260607185629-ch30-workflow | workflow | prosismo capitolo procedi
  - mem-20260607185629-ch30-result | result | Creato il Capitolo 30 extra del Metodo BANDO: Dopo la prova: esiti, graduatoria e prossima mossa.

## 2026-06-07T19:11:17+02:00 - manual-writer

- conversation_id: conv-20260607191117-ch31-presa-servizio
- route: chapter-31-presa-servizio
- l0: l0/conv-20260607191117-ch31-presa-servizio.md
- atoms:
  - mem-20260607191117-ch31-workflow | workflow | procedi prossimo capitolo
  - mem-20260607191117-ch31-result | result | Creato il Capitolo 31 extra del Metodo BANDO: Prendere servizio nella PA: dal concorso al ruolo.

## 2026-06-07T17:24:48.977Z - il-metodo-bando

- conversation_id: conv-20260607172448-19sliqz
- route: codex/chapter15-editorial-images
- l0: l0/conv-20260607172448-19sliqz.md
- atoms:
  - mem-20260607172448-1hkpblu | workflow | procedi ora con il capitolo successivo stesso procedimento
  - mem-20260607172448-16jwdar | result | Esito codex/chapter15-editorial-images: procedi ora con il capitolo successivo stesso procedimento -> Capitolo 15 La prova scritta e teorico-pratica illustrato con 7 figure professionali SVG+PNG: mappa operativa dello scritto, formati prova, lettura traccia, schema risposta concorsuale, risposte 10/20/30 righe, caso t...

## 2026-06-07T19:28:12+02:00 - manual-writer

- conversation_id: conv-20260607192812-ch32-sistema-bando-personale
- route: chapter-32-sistema-bando-personale
- l0: l0/conv-20260607192812-ch32-sistema-bando-personale.md
- atoms:
  - mem-20260607192812-ch32-workflow | workflow | ora prossimo capitolo
  - mem-20260607192812-ch32-result | result | Creato il Capitolo 32 extra del Metodo BANDO: Il tuo sistema BANDO personale.

## 2026-06-07T17:49:41.913Z - il-metodo-bando

- conversation_id: conv-20260607174941-12bhj9c
- route: codex/chapter16-editorial-images
- l0: l0/conv-20260607174941-12bhj9c.md
- atoms:
  - mem-20260607174941-pom8u0 | workflow | ora procedi con lo stesso procedimento al prossimo capitolo
  - mem-20260607174941-1svq46j | result | Esito codex/chapter16-editorial-images: ora procedi con lo stesso procedimento al prossimo capitolo -> Capitolo 16 La prova orale illustrato con 7 figure professionali SVG+PNG: mappa operativa prova orale, scheda orale bando, struttura universale risposta orale, risposta in due minuti, collegamenti e domande incrociate...

## 2026-06-07T19:55:28+02:00 - manual-writer

- conversation_id: conv-20260607195528-ch33-materiali-studio
- route: chapter-33-materiali-studio
- l0: l0/conv-20260607195528-ch33-materiali-studio.md
- atoms:
  - mem-20260607195528-ch33-workflow | workflow | prossimo capitolo procedi
  - mem-20260607195528-ch33-result | result | Creato il Capitolo 33 extra del Metodo BANDO: Manuali, corsi e banche dati: scegliere senza disperdersi.

## 2026-06-07T18:09:47.448Z - il-metodo-bando

- conversation_id: conv-20260607180947-oro3xo
- route: codex/chapter17-editorial-images
- l0: l0/conv-20260607180947-oro3xo.md
- atoms:
  - mem-20260607180947-ttbc2v | result | Esito codex/chapter17-editorial-images: prossimo capitolo procedi -> Capitolo 17 Casi pratici e problem solving amministrativo illustrato con 7 figure professionali SVG+PNG: mappa BANDO del caso pratico, caso come fascicolo amministrativo ridotto, griglia in otto domande, schema di ris...

## 2026-06-08T13:55:00+02:00 - il-metodo-bando

- conversation_id: conv-20260608135500-ch18-situazionali-images
- route: codex/chapter18-editorial-images
- l0: l0/conv-20260608135500-ch18-situazionali-images.md
- atoms:
  - mem-20260608135500-ch18-workflow | workflow | procedi con il capitolo successivo, identificazione delle immagini da inserire, generazione dell'immagine e inserimento professionale preciso come nei precedenti capitoli
  - mem-20260608135500-ch18-result | result | Capitolo 18 Quesiti situazionali e soft skills illustrato con 7 figure professionali SVG+PNG.

## 2026-06-08T17:50:37.572Z - manual-writer

- conversation_id: conv-20260608175037-z2bh7
- route: codex/ch34-simulazioni-concorsuali
- l0: l0/conv-20260608175037-z2bh7.md
- atoms:
  - mem-20260608175037-skunz5 | result | Esito codex/ch34-simulazioni-concorsuali: prossimo capitolo -> Creato il Capitolo 34 extra del Metodo BANDO: Simulazioni concorsuali: dalla preparazione alla prova.

## 2026-06-08T19:55:00+02:00 - il-metodo-bando

- conversation_id: conv-20260608195500-ch19-famiglie-images
- route: codex/chapter19-editorial-images
- l0: l0/conv-20260608195500-ch19-famiglie-images.md
- atoms:
  - mem-20260608195500-ch19-workflow | workflow | prossimo capitolo
  - mem-20260608195500-ch19-result | result | Capitolo 19 Le famiglie dei concorsi pubblici illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T08:49:36.381Z - manual-writer

- conversation_id: conv-20260609084936-13sgo5y
- route: codex/ch35-schede-operative
- l0: l0/conv-20260609084936-13sgo5y.md
- atoms:
  - mem-20260609084936-1mafs34 | workflow | procedi con il prossimo capitolo; vai
  - mem-20260609084936-1txg0nu | result | Esito codex/ch35-schede-operative: procedi con il prossimo capitolo; vai -> Creato il Capitolo 35 extra del Metodo BANDO: Schede operative: trasformare studio ed errori in risposte.

## 2026-06-09T10:52:01.4580719+02:00 - il-metodo-bando

- conversation_id: conv-20260609105201-ch20-mappe-profilo-images
- route: codex/chapter20-editorial-images
- l0: l0/conv-20260609105201-ch20-mappe-profilo-images.md
- atoms:
  - mem-20260609105201-ch20-workflow | workflow | procedi ocn il prossimo capitolo
  - mem-20260609105201-ch20-result | result | Capitolo 20 Mappe profilo: cosa resta comune e cosa cambia illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T11:12:55.6026857+02:00 - il-metodo-bando

- conversation_id: conv-20260609111255-ch21-moduli-integrativi-images
- route: codex/chapter21-editorial-images
- l0: l0/conv-20260609111255-ch21-moduli-integrativi-images.md
- atoms:
  - mem-20260609111255-ch21-workflow | workflow | prossimo capitolo procedi
  - mem-20260609111255-ch21-result | result | Capitolo 21 Come scegliere i moduli integrativi illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T09:16:20.262Z - manual-writer

- conversation_id: conv-20260609091620-1fj2bn6
- route: codex/ch36-taglio-priorita-studio
- l0: l0/conv-20260609091620-1fj2bn6.md
- atoms:
  - mem-20260609091620-rcxmrz | result | Esito codex/ch36-taglio-priorita-studio: ok procedi -> Creato il Capitolo 36 extra del Metodo BANDO: Tagliare senza perdere punti: priorita e studio ad alta resa.

## 2026-06-09T13:15:22.7557043+02:00 - il-metodo-bando

- conversation_id: conv-20260609131522-ch22-piano-30-60-90-images
- route: codex/chapter22-editorial-images
- l0: l0/conv-20260609131522-ch22-piano-30-60-90-images.md
- atoms:
  - mem-20260609131522-ch22-workflow | workflow | prossimo capitolo
  - mem-20260609131522-ch22-result | result | Capitolo 22 Piano 30/60/90 giorni illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T12:14:58.066Z - manual-writer

- conversation_id: conv-20260609121458-ee2e5b
- route: codex/ch37-strategia-punteggio-prova
- l0: l0/conv-20260609121458-ee2e5b.md
- atoms:
  - mem-20260609121458-174e3oi | workflow | procedi con prossimo capitolo
  - mem-20260609121458-rrz2bq | result | Esito codex/ch37-strategia-punteggio-prova: procedi con prossimo capitolo -> Creato il Capitolo 37 extra del Metodo BANDO: Strategia di punteggio: soglie, tempo e rischio nella prova.

## 2026-06-09T14:30:14.3644559+02:00 - il-metodo-bando

- conversation_id: conv-20260609143014-ch23-diario-errori-images
- route: codex/chapter23-editorial-images
- l0: l0/conv-20260609143014-ch23-diario-errori-images.md
- atoms:
  - mem-20260609143014-ch23-workflow | workflow | procedi con prossimo capitolo
  - mem-20260609143014-ch23-result | result | Capitolo 23 Il diario degli errori illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T16:27:53.3228734+02:00 - il-metodo-bando

- conversation_id: conv-20260609162753-ch24-checklist-operative-images
- route: codex/chapter24-editorial-images
- l0: l0/conv-20260609162753-ch24-checklist-operative-images.md
- atoms:
  - mem-20260609162753-ch24-workflow | workflow | prossimo capitolo
  - mem-20260609162753-ch24-result | result | Capitolo 24 Checklist operative illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T14:34:32.936Z - manual-writer

- conversation_id: conv-20260609143432-18e3sgb
- route: codex/ch38-giorno-prova
- l0: l0/conv-20260609143432-18e3sgb.md
- atoms:
  - mem-20260609143432-7fxhpv | result | Esito codex/ch38-giorno-prova: prossimo capitolo -> Creato il Capitolo 38 extra del Metodo BANDO: Il giorno della prova: routine, logistica e lucidita operativa.

## 2026-06-09T17:20:17.556Z - manual-writer

- conversation_id: conv-20260609172017-gp8h7e
- route: codex/ch39-intervallo-prove
- l0: l0/conv-20260609172017-gp8h7e.md
- atoms:
  - mem-20260609172017-mran3o | result | Esito codex/ch39-intervallo-prove: PROSSIMO CAPITOLO -> Creato il Capitolo 39 extra del Metodo BANDO: Tra una prova e l'altra: ripianificare senza ricominciare.

## 2026-06-09T19:22:06.0253752+02:00 - il-metodo-bando

- conversation_id: conv-20260609192206-ch25-aggiornare-metodo-images
- route: codex/chapter25-editorial-images
- l0: l0/conv-20260609192206-ch25-aggiornare-metodo-images.md
- atoms:
  - mem-20260609192206-ch25-workflow | workflow | PROSSIMO CAPITOLO
  - mem-20260609192206-ch25-result | result | Capitolo 25 Aggiornare il metodo dopo il libro illustrato con 7 figure professionali SVG+PNG.

## 2026-06-10T14:55:42.1454789+02:00 - il-metodo-bando

- conversation_id: conv-20260610145542-ch26-capitale-studio-images
- route: codex/chapter26-editorial-images
- l0: l0/conv-20260610145542-ch26-capitale-studio-images.md
- atoms:
  - mem-20260610145542-ch26-workflow | workflow | Con il prossimo capitolo
  - mem-20260610145542-ch26-result | result | Capitolo 26 Trasformare ogni concorso in capitale di studio illustrato con 7 figure professionali SVG+PNG.

## 2026-06-10T13:59:33.529Z - manual-writer

- conversation_id: conv-20260610135933-6gooud
- route: codex/ch40-ripasso-finale
- l0: l0/conv-20260610135933-6gooud.md
- atoms:
  - mem-20260610135933-3beybi | workflow | Procedi con il prossimo capitolo.
  - mem-20260610135933-1fmy0em | result | Esito codex/ch40-ripasso-finale: Procedi con il prossimo capitolo. -> Creato il Capitolo 40 extra del Metodo BANDO: Ripasso finale: consolidare senza saturarsi.

## 2026-06-10T16:09:31.8187103+02:00 - il-metodo-bando

- conversation_id: conv-20260610160931-ch27-concorsi-paralleli-images
- route: codex/chapter27-editorial-images
- l0: l0/conv-20260610160931-ch27-concorsi-paralleli-images.md
- atoms:
  - mem-20260610160931-ch27-workflow | workflow | procedi prossimo capitolo
  - mem-20260610160931-ch27-result | result | Capitolo 27 Gestire concorsi paralleli senza disperdersi illustrato con 7 figure professionali SVG+PNG.

## 2026-06-12T09:49:51.749Z - manual-writer

- conversation_id: conv-20260612094951-11lznqr
- route: codex/ch41-caso-completo-bando
- l0: l0/conv-20260612094951-11lznqr.md
- atoms:
  - mem-20260612094951-1uys01 | result | Esito codex/ch41-caso-completo-bando: procedi con il prossimo capitolo -> Creato il Capitolo 41 extra del Metodo BANDO: Caso completo BANDO: dal bando alla prova.

## 2026-06-12T09:52:16.281Z - il-metodo-bando

- conversation_id: conv-20260612095216-178ykdn
- route: codex/chapter28-editorial-images
- l0: l0/conv-20260612095216-178ykdn.md
- atoms:
  - mem-20260612095216-10lti1a | result | Esito codex/chapter28-editorial-images: prossimo capitolo -> Capitolo 28 Usare il digitale senza perdere il metodo illustrato con 7 figure professionali SVG+PNG: mappa BANDO del digitale, regola 1-3-5, cartella minima, AI assistente non fonte, protocollo AI sicuro, digitale/car...

## 2026-06-14T15:58:53.214Z - il-metodo-bando

- conversation_id: conv-20260614155853-1i503yy
- route: codex/chapter29-editorial-images
- l0: l0/conv-20260614155853-1i503yy.md
- atoms:
  - mem-20260614155853-1ro7szv | result | Esito codex/chapter29-editorial-images: prossimo capitolo procedi -> Capitolo 29 Reggere la preparazione: energia, ansia e continuita illustrato con 7 figure professionali SVG+PNG: mappa BANDO della sostenibilita, scala energia, minimo efficace, recupero senza distruggere il piano, ans...

## 2026-06-14T16:10:39.089Z - manual-writer

- conversation_id: conv-20260614161039-ks2ki6
- route: codex/ch42-banca-dati-ufficiale
- l0: l0/conv-20260614161039-ks2ki6.md
- atoms:
  - mem-20260614161039-1oxwfiu | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 41.
  - mem-20260614161039-oh5sy5 | result | Esito codex/ch42-banca-dati-ufficiale: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 41. -> Creato Capitolo 42: Banca dati ufficiale: studiarla senza memorizzare male.

## 2026-06-14T19:20:58.045Z - manual-writer

- conversation_id: conv-20260614192058-1berl6p
- route: codex/chapter30-editorial-images
- l0: l0/conv-20260614192058-1berl6p.md
- atoms:
  - mem-20260614192058-9yngr9 | result | Esito codex/chapter30-editorial-images: prossimo capitolo procedi -> Capitolo 30 Dopo la prova: esiti, graduatoria e prossima mossa illustrato con 7 figure professionali SVG+PNG in chapter-30: mappa BANDO, prime 24 ore, tre livelli di esito, cartella dopo-prova, graduatoria/accesso att...

## 2026-06-14T20:10:22.327Z - manual-writer

- conversation_id: conv-20260614201022-dunwve
- route: codex/ch43-risposta-sintetica
- l0: l0/conv-20260614201022-dunwve.md
- atoms:
  - mem-20260614201022-i3vvv9 | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 42.
  - mem-20260614201022-156g8ur | result | Esito codex/ch43-risposta-sintetica: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 42. -> Creato Capitolo 43: Risposta sintetica: scrivere poco, dire tutto.

## 2026-06-15T12:21:37.773Z - manual-writer

- conversation_id: conv-20260615122137-1qlf0fh
- route: codex/ch44-confrontare-istituti-simili
- l0: l0/conv-20260615122137-1qlf0fh.md
- atoms:
  - mem-20260615122137-kih0gv | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 43.
  - mem-20260615122137-191m2pm | result | Esito codex/ch44-confrontare-istituti-simili: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 43. -> Creato Capitolo 44: Confrontare istituti simili: differenze che fanno punti.

## 2026-06-15T12:21:46.420Z - manual-writer

- conversation_id: conv-20260615122146-11zuqpx
- route: codex/chapter31-editorial-images
- l0: l0/conv-20260615122146-11zuqpx.md
- atoms:
  - mem-20260615122146-1u3cwzr | result | Esito codex/chapter31-editorial-images: prossimo capitolo procedi -> Capitolo 31 Prendere servizio nella PA: dal concorso al ruolo illustrato con 7 figure professionali SVG+PNG in chapter-31: mappa BANDO della presa di servizio, sequenza dal concorso al ruolo, cartella di ingresso, qua...

## 2026-06-16T20:13:12.023Z - manual-writer

- conversation_id: conv-20260616201312-1vz86jl
- route: codex/ch45-collegare-materie
- l0: l0/conv-20260616201312-1vz86jl.md
- atoms:
  - mem-20260616201312-1tsmgby | result | Esito codex/ch45-collegare-materie: PROSSIMO CAPITOLO PROCEDI -> Creato Capitolo 45 del Metodo BANDO: Collegare le materie: dal programma alla risposta integrata.

## 2026-06-16T23:11:39.534Z - manual-writer

- conversation_id: conv-20260616231139-1ch2u9j
- route: codex/chapter32-editorial-images
- l0: l0/conv-20260616231139-1ch2u9j.md
- atoms:
  - mem-20260616231139-1qls1lf | result | Esito codex/chapter32-editorial-images: PROSSIMO CAPITOLO PROCEDI -> Capitolo 32 Il tuo sistema BANDO personale illustrato con 7 figure professionali SVG+PNG in chapter-32: mappa BANDO del sistema personale, cinque pagine vive, protocollo 15/30/60, cruscotto BANDO personale, mantieni-a...

## 2026-06-17T14:39:25.856Z - manual-writer

- conversation_id: conv-20260617143925-hzqp8m
- route: codex/chapter33-editorial-images
- l0: l0/conv-20260617143925-hzqp8m.md
- atoms:
  - mem-20260617143925-1sx4qq | result | Esito codex/chapter33-editorial-images: PROSSIMO CAPITOLO PROCEDI -> Capitolo 33 Manuali, corsi e banche dati: scegliere senza disperdersi illustrato con 7 figure professionali SVG+PNG in chapter-33: mappa BANDO dei materiali, prima bando poi materiale, pila minima, scorecard materiali...

## 2026-06-17T14:41:23.180Z - manual-writer

- conversation_id: conv-20260617144123-g8t0g1
- route: codex/ch46-domande-impreviste
- l0: l0/conv-20260617144123-g8t0g1.md
- atoms:
  - mem-20260617144123-1rzoyf9 | result | Esito codex/ch46-domande-impreviste: PROSSIMO CAPITOLO PROCEDI -> Creato Capitolo 46 del Metodo BANDO: Domande impreviste: rispondere senza inventare.

## 2026-06-20T03:33:16.240Z - manual-writer

- conversation_id: conv-20260620033316-payn4r
- route: codex/ch47-revisione-finale
- l0: l0/conv-20260620033316-payn4r.md
- atoms:
  - mem-20260620033316-1oeucbw | result | Esito codex/ch47-revisione-finale: prossimo capitolo -> Creato Capitolo 47 del Metodo BANDO: Revisione finale: controllare prima di consegnare.

## 2026-06-27T19:04:42+02:00 - manual-writer

- conversation_id: conv-20260627190442-ricettario-digitale
- route: codex/editorial-architecture-ricettario-digitale
- l0: l0/conv-20260627190442-ricettario-digitale.md
- atoms:
  - mem-20260627190442-ricettario-digitale | instruction | Per Il Metodo BANDO, i capitoli 1-24 restano nel volume principale senza riduzione strutturale; i capitoli 25-47 gia scritti vanno trattati come Ricettario operativo digitale, moduli R1-R23 collegati al libro e non come corpo cartaceo principale.

## 2026-06-27T19:56:28+02:00 - manual-writer

- conversation_id: conv-20260627195628-moduli-specialistici
- route: codex/editorial-architecture-moduli-specialistici
- l0: l0/conv-20260627195628-moduli-specialistici.md
- atoms:
  - mem-20260627195628-moduli-specialistici | instruction | Per Il Metodo BANDO, i moduli specialistici vivono in wiki/books/moduli/<module-id>/ come libri di lavoro separati: 6 famiglie e 25 moduli canonici, con book_id uguale allo slug cartella, index.md e capitoli in chapters/.

## 2026-06-29T12:48:07.887Z - manual-writer

- conversation_id: conv-20260629124807-1d0ax5h
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629124807-1d0ax5h.md
- atoms:
  - mem-20260629124807-pg6ite | workflow | instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti e struttura Metodo BANDO, riscrivi solo i passaggi necessari.
  - mem-20260629124807-1uojduy | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti ... -> Revisione humanizer completata su books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md.

## 2026-06-29T15:08:07.606Z - manual-writer

- conversation_id: conv-20260629150807-1282rhq
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629150807-1282rhq.md
- atoms:
  - mem-20260629150807-hyeogg | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/il-metodo-bando/chapters/anatomia-del-bando.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti e struttu... -> Revisione humanizer completata su books/il-metodo-bando/chapters/anatomia-del-bando.md.

## 2026-06-29T15:12:24.544Z - manual-writer

- conversation_id: conv-20260629151224-1qwkjb3
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629151224-1qwkjb3.md
- atoms:
  - mem-20260629151224-12xtpfh | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri-funzioni-centrali.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva signi... -> Revisione humanizer completata su books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri-funzioni-centrali.md.

## 2026-06-29T15:21:36.094Z - manual-writer

- conversation_id: conv-20260629152136-v2ve0a
- route: ManualWriterAgent.writeChapter
- l0: l0/conv-20260629152136-v2ve0a.md
- atoms:
  - mem-20260629152136-1cg7i7s | workflow | instruction=Scrivi il capitolo effettivo , non un riepilogo tecnico.
  - mem-20260629152136-195qkxl | instruction | Usa prima il cervello wiki: struttura madre, nota capitolo, source notes, topic pages, entity pages e design system; scarica altre fonti necessarie per la copertura totale della conoscenza e procedi poi alla scrittura professionale del capitolo completo
  - mem-20260629152136-6r2rui | result | Esito ManualWriterAgent.writeChapter: chapterPath=books/moduli/m-fc01-ministeri/chapters/02-anatomia-bando-ministeriale-ripam.md mode=integrate instruction=Scrivi il capitolo effettivo , non un riepilogo tecnico. -> Manual Writer completato su books/moduli/m-fc01-ministeri/chapters/02-anatomia-bando-ministeriale-ripam.md.

## 2026-07-01T11:04:54.420Z - editorial-reviewer

- conversation_id: conv-20260701110454-1epn91o
- route: EditorialReviewerAgent.runReview
- l0: l0/conv-20260701110454-1epn91o.md
- atoms:
  - mem-20260701110454-kr0dhf | result | Esito EditorialReviewerAgent.runReview: bookId=moduli/m-tr04-ambiente-protezione-civile scope=full aspect=full -> Revisione editoriale completata su moduli/m-tr04-ambiente-protezione-civile.
## 2026-07-02T16:37:06.612Z - manual-writer

- conversation_id: conv-20260702163706-1t4oml3
- route: ManualWriterAgent.writeChapter
- l0: l0/conv-20260702163706-1t4oml3.md
- atoms:
  - mem-20260702163706-1pr3th0 | workflow | PRODEGUI CON IL SECONDO CAPITOLO DEL LIBRO
  - mem-20260702163706-1izkerd | result | Esito ManualWriterAgent.writeChapter: PRODEGUI CON IL SECONDO CAPITOLO DEL LIBRO -> M-FC02 capitolo 2 Bando Decoder fiscale completato in professional draft: trasformata la scheda source-ready in capitolo workbook da 444 righe con apertura editoriale, mappa BANDO, regole di compilazione, pagine opera...

## 2026-07-02T17:24:56.314Z - manual-writer

- conversation_id: conv-20260702172456-1es68u
- route: codex/editorial-images/mfc02-chapter02
- l0: l0/conv-20260702172456-1es68u.md
- atoms:
  - mem-20260702172456-xesxf9 | workflow | Integra immagini editoriali coerenti nel capitolo 2 M-FC02 Bando Decoder fiscale, con layout senza sovrapposizioni.
  - mem-20260702172456-jajyrm | result | Esito codex/editorial-images/mfc02-chapter02: Integra immagini editoriali coerenti nel capitolo 2 M-FC02 Bando Decoder fiscale, con layout senza sovrapposizioni. -> Creati 5 asset SVG/PNG 1600x900 in stile libro base per il capitolo 2 M-FC02, inseriti nel markdown e verificati nel Book Studio.

## 2026-07-02T17:26:18.733Z - manual-writer

- conversation_id: conv-20260702172618-1am96gi
- route: codex/editorial-images/mfc02-chapter02-correction
- l0: l0/conv-20260702172618-1am96gi.md
- atoms:
  - mem-20260702172618-86ux49 | workflow | Correggi dettaglio memoria intervento immagini M-FC02 capitolo 2.
  - mem-20260702172618-1a63obw | result | Esito codex/editorial-images/mfc02-chapter02-correction: Correggi dettaglio memoria intervento immagini M-FC02 capitolo 2. -> Correzione dettaglio: nel Book Studio il valore finale effettivo di PAGE_MEASURE_GUARD_SPACE per la paginazione misurata e 180.

## 2026-07-02T17:42:54.296Z - manual-writer

- conversation_id: conv-20260702174254-2ptyt9
- route: codex/manual-writer/mfc02-chapter03
- l0: l0/conv-20260702174254-2ptyt9.md
- atoms:
  - mem-20260702174254-iq6giv | instruction | Redigere il terzo capitolo del modulo M-FC02 con stile accademico/manualistico, fonti consolidate e struttura dei capitoli esistenti.
  - mem-20260702174254-14g79zt | result | Esito codex/manual-writer/mfc02-chapter03: Redigere il terzo capitolo del modulo M-FC02 con stile accademico/manualistico, fonti consolidate e struttura dei capitoli esistenti. -> M-FC02 capitolo 3 completato in professional draft: ordinamento e organizzazione di Agenzia delle Entrate, ADM e Agenzia delle entrate-Riscossione; D.Lgs.

## 2026-07-03T15:37:48.293Z - concorso-book-os

- conversation_id: conv-20260703153748-oyh59l
- route: codex/dashboard-catalog-restructure
- l0: l0/conv-20260703153748-oyh59l.md
- atoms:
  - mem-20260703153748-pv65mj | workflow | Analizzare il DOCX Idea di business e vendita libri Capitale Personale e ristrutturare dashboard e lista testi in funzione della nuova struttura dei volumi.
  - mem-20260703153748-1g54jxj | result | Esito codex/dashboard-catalog-restructure: Analizzare il DOCX Idea di business e vendita libri Capitale Personale e ristrutturare dashboard e lista testi in funzione della nuova struttura dei volumi. -> Dashboard ristrutturata intorno al catalogo commerciale a 12 volumi.

## 2026-07-10T22:13:34.957Z - catalog-dashboard

- conversation_id: conv-20260710221334-8fk3vl
- route: catalog-volume-scope-correction
- l0: l0/conv-20260710221334-8fk3vl.md
- atoms:
  - mem-20260710221334-zq2w8j | workflow | Nel catalogo dashboard, il Volume 1 Il Metodo BANDO non deve essere toccato.
  - mem-20260710221334-1xcl483 | result | Esito catalog-volume-scope-correction: Nel catalogo dashboard, il Volume 1 Il Metodo BANDO non deve essere toccato. -> Correzione applicata: VOL-01 resta il libro base originale; l'aggregazione editoriale resta limitata ai volumi specialistici VOL-02-VOL-12.

## 2026-07-14T15:57:55.466Z - il-metodo-bando

- conversation_id: conv-20260714155755-1ueyp44
- route: codex/manual-writer
- l0: l0/conv-20260714155755-1ueyp44.md
- atoms:
  - mem-20260714155755-1pwxyid | workflow | Completa le sezioni mancanti di VOL-01 e analizza le modifiche al layout dei capitoli.
  - mem-20260714155755-1hbj0xm | result | Esito codex/manual-writer: Completa le sezioni mancanti di VOL-01 e analizza le modifiche al layout dei capitoli. -> Completate B-PA04 con un quadro essenziale sui reati contro la PA nel capitolo 6 e B-PA11 con il laboratorio di redazione atti nel capitolo 15.

## 2026-07-14T16:06:49.823Z - catalog-governance

- conversation_id: conv-20260714160649-lfigmj
- route: Codex.volume-coverage-v4
- l0: l0/conv-20260714160649-lfigmj.md
- atoms:
  - mem-20260714160649-18ljyby | project_fact | Rendere logica_volumi_copertura_concorsobook_v4.md la base vincolante per sviluppo dei volumi, prossimi passi e revisioni.
  - mem-20260714160649-18qc8ta | result | Esito Codex.volume-coverage-v4: Rendere logica_volumi_copertura_concorsobook_v4.md la base vincolante per sviluppo dei volumi, prossimi passi e revisioni. -> Ingestita la fonte v4 e applicata a architettura, AGENTS, Manual Writer e Revisore Editoriale.

## 2026-07-14T16:58:08.462Z - vol01-editorial-review

- conversation_id: conv-20260714165808-w505d2
- route: Codex.fullVolumeReview
- l0: l0/conv-20260714165808-w505d2.md
- atoms:
  - mem-20260714165808-1lx9tc2 | instruction | Analizzare integralmente VOL-01, usare le skill writer e revisore, verificare le 11 aree B-PA, correggere grammatica e impaginazione professionale, usare come struttura canonica il file VOL-01 del 14 luglio 2026 e conservare tutte le immagini esistenti.
  - mem-20260714165808-1ke3qis | result | Esito Codex.fullVolumeReview: Analizzare integralmente VOL-01, usare le skill writer e revisore, verificare le 11 aree B-PA, correggere grammatica e impaginazione professionale, usare come struttura canonica il file VOL-01 del 14 luglio 2026 e con... -> Revisione completa eseguita.

## 2026-07-15T19:02:10.448Z - editorial-layout

- conversation_id: conv-20260715190210-13qj2ug
- route: Codex.volume01LayoutOptimization
- l0: l0/conv-20260715190210-13qj2ug.md
- atoms:
  - mem-20260715190210-1b65r83 | result | Esito Codex.volume01LayoutOptimization: Le pagine del Volume 1 non sono ottimizzate: c'e troppo spazio vuoto tra le pagine. -> Ottimizzata la paginazione A4 del VOL-01 Il Metodo BANDO.

## 2026-07-16T16:51:02.569Z - editorial-layout

- conversation_id: conv-20260716165102-18b2mx0
- route: Codex.bookStudioPreviewRegressionFix
- l0: l0/conv-20260716165102-18b2mx0.md
- atoms:
  - mem-20260716165102-16yuo3g | project_fact | Sistema l'anteprima del libro: e cambiata, le immagini sono sotto e non e ottimizzata come prima.
  - mem-20260716165102-vdvg0c | result | Esito Codex.bookStudioPreviewRegressionFix: Sistema l'anteprima del libro: e cambiata, le immagini sono sotto e non e ottimizzata come prima. -> Individuata una sovrapposizione tra il pannello Asset libro e la preview A4 causata dalla griglia desktop a due colonne con controlli sticky.
## 2026-07-08T20:12:00+02:00 - manual-writer

- conversation_id: conv-20260708201200-mfc03-ch12-quesiti-situazionali
- route: codex/mfc03-ch12-quesiti-situazionali
- l0: l0/conv-20260708201200-mfc03-ch12-quesiti-situazionali.md
- atoms:
  - mem-20260708201200-mfc03-ch12-quesiti-situazionali | result | M-FC03 capitolo 12 Quesiti situazionali EPNE redatto come professional-draft; test frontmatter/markdown/book-preview 12/12 passati.

## 2026-07-08T20:20:00+02:00 - manual-writer

- conversation_id: conv-20260708202000-mfc03-ch13-piano-30-60-90
- route: codex/mfc03-ch13-piano-30-60-90
- l0: l0/conv-20260708202000-mfc03-ch13-piano-30-60-90.md
- atoms:
  - mem-20260708202000-mfc03-ch13-piano-30-60-90 | result | M-FC03 capitolo 13 Piano 30/60/90 redatto come professional-draft/revised_draft.

## 2026-07-08T20:20:00+02:00 - manual-writer

- conversation_id: conv-20260708202000-mfc03-ch13-frontmatter-cleanup
- route: codex/mfc03-ch13-frontmatter-cleanup
- l0: l0/conv-20260708202000-mfc03-ch13-frontmatter-cleanup.md
- atoms:
  - mem-20260708202000-mfc03-ch13-frontmatter-cleanup | result | Capitolo 13 M-FC03 ripulito da metadati visibili, accenti e punteggiatura corretti, book-preview test 7/7.

## 2026-07-08T21:55:00+02:00 - manual-writer

- conversation_id: conv-20260708215500-mfc03-appendice-b-glossario
- route: codex/mfc03-appendice-b-glossario
- l0: l0/conv-20260708215500-mfc03-appendice-b-glossario.md
- atoms:
  - mem-20260708215500-mfc03-appendice-b-glossario | result | Appendice B M-FC03 redatta come glossario operativo INPS/INAIL; book-preview test 7/7.

## M-FC03 - Appendice A vigilanza ispettiva INPS-INAIL
- Data: 2026-07-08
- Quando si redigono appendici M-FC03 su sottoprofili ispettivi, mantenere la funzione di orientamento al bando: non trasformare l'appendice in manuale autonomo di lavoro/sicurezza.
- Distinguere sempre INPS, INAIL e INL; citare numeri di posti o prove solo dopo verifica su avviso e allegati ufficiali.
- Struttura efficace: apertura, obiettivo, Mappa BANDO, perimetri, materie da attivare, scheda compilabile, caso guidato, domanda da commissario, domanda-trappola, errore tipico, mini-esercizio, checklist, riferimenti e note di review.

## M-FC03 - Appendice C schede rapide enti
- Data: 2026-07-08
- Appendice C deve restare strumento di orientamento ente-specifico: schede rapide, Bando Decoder, confini e rinvii, non manuale autonomo su ogni ente.
- Per CONI usare fonte ufficiale riacquisita il 2026-07-08; per CRI mantenere cautela sulla natura giuridica e verificare sempre il singolo bando.
- Per ENEA, ASI e ISTAT separare profili amministrativi da ricerca, tecnologi, profili scientifici o statistici avanzati.
## 2026-07-08T22:10:00+02:00 - manual-writer

- conversation_id: conv-20260708221000-mfc03-appendice-d-errori-bandi
- route: codex/mfc03-appendice-d-errori-bandi
- l0: l0/conv-20260708221000-mfc03-appendice-d-errori-bandi.md
- atoms:
  - mem-20260708221000-mfc03-appendice-d-errori-bandi | result | Appendice D M-FC03 redatta sugli errori tipici nei bandi EPNE; book-preview test 7/7.

## M-FC03 - Appendice D errori tipici nei bandi EPNE
- Data: 2026-07-08
- L'appendice deve funzionare come strumento di prevenzione degli errori di lettura del bando, non come repertorio astratto di irregolaritÃ  amministrative.
- Mantenere sempre la distinzione tra portale di pubblicazione, gestore della procedura ed ente destinatario del profilo.
- Per contenuti instabili, come prove, soglie, calendari, rettifiche e allegati, richiamare la verifica dell'avviso ufficiale piÃ¹ aggiornato.
## M-FC03 - Appendice E rinvii ragionati
- Data: 2026-07-08
- Appendice E deve funzionare come routing del bando: M-FC03 resta principale per profili amministrativi/giuridici/economici/contabili/servizi/vigilanza non tecnica; ricerca, ICT puro, appalti-PNRR specialistici, agenzie fiscali e authority vanno rinviati ai moduli corretti.
- Non presentare i rinvii come perdita del lavoro svolto: libro base e parti M-FC03 restano capitale di studio, ma il modulo principale cambia se profilo e prove lo richiedono.


## Integrazione da origin/main del 17 luglio 2026

# Agent Memory Scenarios

## 2026-05-27T21:45:00.000Z - global

- conversation_id: conv-20260527214500-always-on-memory
- route: codex-user-preference
- l0: l0/conv-20260527214500-always-on-memory.md
- atoms:
  - mem-20260527214500-always-on-memory | preference | Nel contesto ConcorsoBook OS la memoria locale deve restare sempre attiva per ricordare cio' che e' stato detto e migliorare progressivamente gli output.

## 2026-05-27T21:55:00.000Z - global

- conversation_id: conv-20260527215500-shared-provider-memory
- route: codex-user-preference
- l0: l0/conv-20260527215500-shared-provider-memory.md
- atoms:
  - mem-20260527215500-shared-provider-memory | instruction | La memoria persistente del progetto deve essere condivisa da tutti gli agenti e provider usati: Codex/GPT, Claude, Kimi, OpenAI API, Hermes e locale.

## 2026-05-28T00:50:00.000Z - global

- conversation_id: conv-20260528005000-ruflo-stop-hook-patch
- route: codex-system-maintenance
- l0: l0/conv-20260528005000-ruflo-stop-hook-patch.md
- atoms:
  - mem-20260528005000-ruflo-stop-hook-patch | system-fix | L'avviso ricorrente Stop hook failed era causato dallo Stop hook di Claude/Ruflo ruflo-core 0.2.0 che chiamava npx claude-flow@alpha; il file hooks.json globale e' stato patchato per wrappare quei comandi con cmd /c e fallback exit 0 tramite node.

## 2026-05-27T23:13:08.944Z - global

- conversation_id: conv-20260527231308-1pogjhn
- route: codex/resolve-skill-and-mcp-warnings
- l0: l0/conv-20260527231308-1pogjhn.md
- atoms:
  - mem-20260527231308-116gwtz | project_fact | Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS.
  - mem-20260527231308-10gu8jz | result | Esito codex/resolve-skill-and-mcp-warnings: Risolvi tutti gli avvisi di caricamento skill e MCP Supabase nel contesto ConcorsoBook OS. -> Corretti 17 SKILL.md con frontmatter YAML valido, description presente e sotto 1024 caratteri; rigenerata autenticazione OAuth del MCP Supabase con codex mcp logout/login.

## 2026-05-28T11:43:54.020Z - global

- conversation_id: conv-20260528114354-1rtulm9
- route: codex/resolve-heygen-skill-cache-warnings
- l0: l0/conv-20260528114354-1rtulm9.md
- atoms:
  - mem-20260528114354-1hznga7 | result | Esito codex/resolve-heygen-skill-cache-warnings: Gli avvisi continuano a uscire per HeyGen 719ed655: heygen-avatar e heygen-video hanno description oltre 1024 caratteri. -> Corretti i due SKILL.md HeyGen nel cache 719ed655 e le due copie sorgente temporanee in .codex/.tmp/plugins/plugins/heygen; validazione finale: 4 copie controllate, tutte valide.

## 2026-05-28T15:48:49.069Z - global

- conversation_id: conv-20260528154849-4kjfkk
- route: codex/adapt-book-layout-from-docx
- l0: l0/conv-20260528154849-4kjfkk.md
- atoms:
  - mem-20260528154849-1cefyks | project_fact | Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini.
  - mem-20260528154849-l23wje | result | Esito codex/adapt-book-layout-from-docx: Adatta layout del libro e delle pagine alla proposta_layout_editoriale_metodo_bando.docx, mantenendo il colore pagina attuale e l'ottimizzazione dei margini. -> Aggiornata la preview editoriale a 16,8 x 24 cm con Playfair Display, Montserrat, palette Navy/Bordeaux/Muted Gold, barra BANDO e callout box; mantenuto colore pagina esistente e margini ottimizzati.

## 2026-05-28T16:05:00.000Z - global

- conversation_id: conv-20260528160500-dashboard-next-cache
- route: codex/fix-dashboard-next-cache
- l0: l0/conv-20260528160500-dashboard-next-cache.md
- atoms:
  - mem-20260528160500-dashboard-next-cache | system-fix | Errore dashboard Cannot find module './331.js' risolto fermando il processo Next su porta 3000, eliminando solo la cache generata .next e riavviando npm run dev su 127.0.0.1:3000; verificati / e /api/book-studio/assets/file con HTTP 200 e screenshot artifacts/dashboard-check.png.

## 2026-05-28T17:55:00.000Z - global

- conversation_id: conv-20260528175500-ch12-logic-corpus
- route: codex/ingest-chapter-12-logic-corpus
- l0: l0/conv-20260528175500-ch12-logic-corpus.md
- atoms:
  - mem-20260528175500-ch12-logic-corpus | result | Preparato il knowledge pack per il capitolo 12 Logica, comprensione del testo e ragionamento: scaricati 19 PDF leciti in wiki/raw/chapter-12-logica-comprensione-ragionamento, creati 5 source notes, 4 topic pages, aggiornati index/log e portato il capitolo a status knowledge-ready preservando le note pregresse.

## 2026-05-28T20:25:00.000+02:00 - global

- conversation_id: conv-20260528202500-ch12-editorial-draft
- route: codex/write-chapter-12-editorial-draft
- l0: l0/conv-20260528202500-ch12-editorial-draft.md
- atoms:
  - mem-20260528202500-ch12-editorial-draft | result | Scritto il Testo editoriale professionale del capitolo 12 Logica, comprensione del testo e ragionamento: capitolo in status revised_draft/editorial-revision, con mappa BANDO, metodi per logica, comprensione, ragionamento critico e numerico, diario errori, domanda commissario, mini-esercizio e mini-simulazione originale da 25 quesiti.

## 2026-05-28T20:38:00.000+02:00 - global

- conversation_id: conv-20260528203800-editorial-proofread-chapters
- route: codex/editorial-proofread-chapters
- l0: l0/conv-20260528203800-editorial-proofread-chapters.md
- atoms:
  - mem-20260528203800-editorial-proofread-chapters | result | Revisione editoriale capillare dei capitoli scritti del Metodo BANDO: audit da Introduzione a Capitolo 12, rimozione di sezioni interne dal Capitolo 12, pulizia di link wiki visibili, correzione di accenti/sintassi/titoli e microcorrezioni nel Capitolo 9 Contratti pubblici; git diff --check e test preview libro passati.

## 2026-05-28T23:05:00.000+02:00 - global

- conversation_id: conv-20260528230500-front-matter-pages
- route: codex/front-matter-pages
- l0: l0/conv-20260528230500-front-matter-pages.md
- atoms:
  - mem-20260528230500-front-matter-pages | result | Integrate servizi digitali con QR, frontespizio, copyright/colophon, sommario, premessa e indice generato in Book Studio.

## 2026-05-28T23:56:00.000+02:00 - global

- conversation_id: conv-20260528235600-editorial-frontmatter-index-polish
- route: codex/editorial-frontmatter-index-polish
- l0: l0/conv-20260528235600-editorial-frontmatter-index-polish.md
- atoms:
  - mem-20260528235600-editorial-frontmatter-index-polish | result | Revisione editoriale front matter/capitoli scritti, rimozione note interne, correzione accenti e nuovo layout indice compatto verificato in dashboard.

## 2026-05-29T00:26:00.000+02:00 - global

- conversation_id: conv-20260529002600-index-editorial-toc-layout
- route: codex/index-editorial-toc-layout
- l0: l0/conv-20260529002600-index-editorial-toc-layout.md
- atoms:
  - mem-20260529002600-index-editorial-toc-layout | result | Indice trasformato in sommario tipografico con parti, capitoli, sottocapitoli numerati, puntini guida e numeri pagina stimati.

## 2026-05-29T13:35:00.000+02:00 - global

- conversation_id: conv-20260529133500-ch09-editorial-images
- route: codex/illustrate-chapter-09-contracts
- l0: l0\conv-20260529133500-ch09-editorial-images.md
- atoms:
  - mem-20260529133500-ch09-editorial-images | result | Capitolo 9 Contratti pubblici essenziali illustrato con 6 figure professionali SVG+PNG: mappa generale, ciclo fabbisogno-esecuzione, procedure/concorrenza, documenti-offerte-stipula, ecosistema digitale BDNCP/PCP/FVOE/CIG, sintesi portale-controlli-responsabilita; preview Playwright verificata con 6 immagini caricate e nessuna sovrapposizione footer.

## 2026-05-29T13:45:00.000+02:00 - global

- conversation_id: conv-20260529134500-ch12-quiz-layout
- route: codex/ch12-quiz-layout
- l0: l0\conv-20260529134500-ch12-quiz-layout.md
- atoms:
  - mem-20260529134500-ch12-quiz-layout | result | Capitolo 12 riorganizzato nella parte esercizi/quesiti: schede tabellari a blocchi tematici, quesito prima delle risposte, soluzioni ragionate separate.

## 2026-05-29T18:22:13.032Z - global

- conversation_id: conv-20260529182213-djvsvf
- route: codex/chapter09-image-audit
- l0: l0/conv-20260529182213-djvsvf.md
- atoms:
  - mem-20260529182213-16onnkx | workflow | Effettua un controllo capillare sulle immagini inserite all'interno del capitolo 9, perché i testi di alcune escono dai margini e non sono ottimizzate.
  - mem-20260529182213-jo8qr4 | result | Esito codex/chapter09-image-audit: Effettua un controllo capillare sulle immagini inserite all'interno del capitolo 9, perché i testi di alcune escono dai margini e non sono ottimizzate. -> Rifiniti i master SVG/PNG del capitolo 9, in particolare figura 9.3 con barre e nota ampliate; aggiunto audit Playwright dei bounding box testuali negli SVG e controllo di impaginazione A4 per tutte le sei immagini.

## 2026-05-30T12:18:00+02:00 - manual-writer

- conversation_id: conv-20260530121800-ch13-16-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530121800-ch13-16-editorial-draft.md
- atoms:
  - mem-20260530121800-ch13-16-editorial-draft | result | Sviluppati i capitoli 13-16 della Parte III del Metodo BANDO: consolidata conoscenza su metodo di studio, prova a quiz, scritto teorico-pratico, risposta concorsuale e orale; creati 3 source notes, 5 topic pages, aggiornati index/log e scritti i quattro capitoli in status revised_draft.

## 2026-05-30T11:54:30.382Z - global

- conversation_id: conv-20260530115430-jt5ntw
- route: codex/chapter10-editorial-images
- l0: l0/conv-20260530115430-jt5ntw.md
- atoms:
  - mem-20260530115430-2t6ohh | workflow | Passa all'analisi del capitolo 10 e quindi alle immagini necessarie alla loro elaborazione e all'inserimento professionale e capillare, come fatto con il capitolo precedente.
  - mem-20260530115430-p61xax | result | Esito codex/chapter10-editorial-images: Passa all'analisi del capitolo 10 e quindi alle immagini necessarie alla loro elaborazione e all'inserimento professionale e capillare, come fatto con il capitolo precedente. -> Capitolo 10 Informatica, PA digitale e competenze digitali illustrato con 7 figure professionali SVG+PNG: mappa generale, hardware/software/dati, file-Office-dati, Internet/reti/protocolli, sicurezza PA, ecosistema PA...

## 2026-05-30T16:25:00+02:00 - manual-writer

- conversation_id: conv-20260530162500-ch17-18-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530162500-ch17-18-editorial-draft.md
- atoms:
  - mem-20260530162500-ch17-18-editorial-draft | result | Sviluppati i capitoli 17-18 della Parte III del Metodo BANDO: consolidata conoscenza su casi pratici, problem solving amministrativo, quesiti situazionali, competenze trasversali PA, soft skills, etica pubblica e orientamento al cittadino; creati 3 source notes, 7 topic pages, aggiornati index/log e scritti i due capitoli in status revised_draft.

## 2026-05-30T19:25:00+02:00 - manual-writer

- conversation_id: conv-20260530192500-ch19-20-editorial-draft
- route: codex/manual-editorial-flow
- l0: l0/conv-20260530192500-ch19-20-editorial-draft.md
- atoms:
  - mem-20260530192500-ch19-20-editorial-draft | result | Sviluppati i capitoli 19-20 della Parte IV del Metodo BANDO: consolidata conoscenza su famiglie concorsuali, mappe profilo, nucleo comune, moduli profilo e bandi rappresentativi; creati 3 source notes, 10 topic pages, aggiornati index/log e scritti i due capitoli in status revised_draft.

## 2026-05-30T17:44:02.585Z - il-metodo-bando

- conversation_id: conv-20260530174402-5ghawm
- route: codex/chapter11-editorial-images
- l0: l0/conv-20260530174402-5ghawm.md
- atoms:
  - mem-20260530174402-1ro8bhv | workflow | Procedi per il capitolo undici come fatto per il capitolo precedente: analisi, immagini necessarie, elaborazione, inserimento professionale e controllo capillare.
  - mem-20260530174402-8g8sec | result | Esito codex/chapter11-editorial-images: Procedi per il capitolo undici come fatto per il capitolo precedente: analisi, immagini necessarie, elaborazione, inserimento professionale e controllo capillare. -> Capitolo 11 Inglese concorsuale essenziale illustrato con 7 figure professionali SVG+PNG: mappa generale, metodo cloze, tempi verbali e segnali, ausiliari/modali, preposizioni-lessico-false friends, reading-email-oral...

## 2026-06-01T14:10:52.386Z - il-metodo-bando

- conversation_id: conv-20260601141052-1w6925h
- route: codex/chapter12-editorial-images
- l0: l0/conv-20260601141052-1w6925h.md
- atoms:
  - mem-20260601141052-odwaqo | workflow | Individua ora le immagini necessarie nel capitolo 12, cosi come gli altri capitoli, genera e inseriscile in maniera professionale e perfetta all'interno del capitolo.
  - mem-20260601141052-1yedyr1 | result | Esito codex/chapter12-editorial-images: Individua ora le immagini necessarie nel capitolo 12, cosi come gli altri capitoli, genera e inseriscile in maniera professionale e perfetta all'interno del capitolo. -> Capitolo 12 Logica, comprensione del testo e ragionamento illustrato con 7 figure professionali SVG+PNG: mappa generale, classificazione dei quesiti, parole logiche, vincoli/serie/pattern, testo e argomento, ragioname...

## 2026-06-05T08:01:44.528Z - manual-writer

- conversation_id: conv-20260605080144-680if7
- route: codex/manual-editorial-flow
- l0: l0/conv-20260605080144-680if7.md
- atoms:
  - mem-20260605080144-af54xy | workflow | Procedi alla scrittura professionale del prossimo capitolo, trova le fonti necessarie a coprire la conoscenza completa e poi procedi.
  - mem-20260605080144-z4j30f | result | Esito codex/manual-editorial-flow: Procedi alla scrittura professionale del prossimo capitolo, trova le fonti necessarie a coprire la conoscenza completa e poi procedi. -> Sviluppato il Capitolo 25 extra del Metodo BANDO, Aggiornare il metodo dopo il libro: salvate raw copies di fonti ufficiali inPA, Gazzetta Ufficiale, Normattiva, DFP/Syllabus, SNA, ANAC, AgID e Garante; creata source ...

## 2026-06-05T15:27:39.658Z - manual-writer

- conversation_id: conv-20260605152739-17xivma
- route: chapter-26-capitale-studio
- l0: l0/conv-20260605152739-17xivma.md
- atoms:
  - mem-20260605152739-15ygvyn | workflow | Ora procediamo con il prossimo capitolo del libro Il Metodo BANDO.
  - mem-20260605152739-ccczzi | result | Esito chapter-26-capitale-studio: Ora procediamo con il prossimo capitolo del libro Il Metodo BANDO. -> Creato il Capitolo 26 extra: Trasformare ogni concorso in capitale di studio.

## 2026-06-05T15:34:38.408Z - manual-writer

- conversation_id: conv-20260605153438-1vwq3p1
- route: chapter-26-source-verification
- l0: l0/conv-20260605153438-1vwq3p1.md
- atoms:
  - mem-20260605153438-gv0of7 | workflow | Per il prossimo capitolo trova le fonti necessarie e procedi con scrittura professionale.
  - mem-20260605153438-1w8a4yh | result | Esito chapter-26-source-verification: Per il prossimo capitolo trova le fonti necessarie e procedi con scrittura professionale. -> Per il Capitolo 26 sono state aggiunte alla source note fonti scientifiche web verificate su active recall, practice testing e spaced practice.

## 2026-06-07T16:41:24+02:00 - manual-writer

- conversation_id: conv-20260607164124-ch27-concorsi-paralleli
- route: chapter-27-concorsi-paralleli
- l0: l0/conv-20260607164124-ch27-concorsi-paralleli.md
- atoms:
  - mem-20260607164124-ch27-workflow | workflow | ok procedi con la scrittura professionale del prossimo capitolo
  - mem-20260607164124-ch27-result | result | Creato il Capitolo 27 extra del Metodo BANDO: Gestire concorsi paralleli senza disperdersi.

## 2026-06-07T18:27:10+02:00 - manual-writer

- conversation_id: conv-20260607182710-ch28-strumenti-digitali
- route: chapter-28-strumenti-digitali
- l0: l0/conv-20260607182710-ch28-strumenti-digitali.md
- atoms:
  - mem-20260607182710-ch28-workflow | workflow | prossimo capitolo scrittura professionale proci / procedio
  - mem-20260607182710-ch28-result | result | Creato il Capitolo 28 extra del Metodo BANDO: Usare il digitale senza perdere il metodo.

## 2026-06-07T18:35:58+02:00 - manual-writer

- conversation_id: conv-20260607183558-ch29-sostenibilita
- route: chapter-29-sostenibilita
- l0: l0/conv-20260607183558-ch29-sostenibilita.md
- atoms:
  - mem-20260607183558-ch29-workflow | workflow | prossimo capitolo procedi
  - mem-20260607183558-ch29-result | result | Creato il Capitolo 29 extra del Metodo BANDO: Reggere la preparazione: energia, ansia e continuita.

## 2026-06-07T16:47:52.612Z - il-metodo-bando

- conversation_id: conv-20260607164752-1qgdro8
- route: codex/chapter14-editorial-images
- l0: l0/conv-20260607164752-1qgdro8.md
- atoms:
  - mem-20260607164752-1mkkbkx | workflow | crea le immagini ora e inseriscile in maniera professionale e precisa nel capitolo come in quelli precedenti
  - mem-20260607164752-1d6liod | result | Esito codex/chapter14-editorial-images: crea le immagini ora e inseriscile in maniera professionale e precisa nel capitolo come in quelli precedenti -> Capitolo 14 La prova a quiz illustrato con 7 figure professionali SVG+PNG: mappa operativa, albero banca dati, scheda tecnica, metodo banca dati in quattro passaggi, routine tre giri, anatomia distrattore, punteggio-d...

## 2026-06-07T18:56:29+02:00 - manual-writer

- conversation_id: conv-20260607185629-ch30-dopo-prova
- route: chapter-30-dopo-prova
- l0: l0/conv-20260607185629-ch30-dopo-prova.md
- atoms:
  - mem-20260607185629-ch30-workflow | workflow | prosismo capitolo procedi
  - mem-20260607185629-ch30-result | result | Creato il Capitolo 30 extra del Metodo BANDO: Dopo la prova: esiti, graduatoria e prossima mossa.

## 2026-06-07T19:11:17+02:00 - manual-writer

- conversation_id: conv-20260607191117-ch31-presa-servizio
- route: chapter-31-presa-servizio
- l0: l0/conv-20260607191117-ch31-presa-servizio.md
- atoms:
  - mem-20260607191117-ch31-workflow | workflow | procedi prossimo capitolo
  - mem-20260607191117-ch31-result | result | Creato il Capitolo 31 extra del Metodo BANDO: Prendere servizio nella PA: dal concorso al ruolo.

## 2026-06-07T17:24:48.977Z - il-metodo-bando

- conversation_id: conv-20260607172448-19sliqz
- route: codex/chapter15-editorial-images
- l0: l0/conv-20260607172448-19sliqz.md
- atoms:
  - mem-20260607172448-1hkpblu | workflow | procedi ora con il capitolo successivo stesso procedimento
  - mem-20260607172448-16jwdar | result | Esito codex/chapter15-editorial-images: procedi ora con il capitolo successivo stesso procedimento -> Capitolo 15 La prova scritta e teorico-pratica illustrato con 7 figure professionali SVG+PNG: mappa operativa dello scritto, formati prova, lettura traccia, schema risposta concorsuale, risposte 10/20/30 righe, caso t...

## 2026-06-07T19:28:12+02:00 - manual-writer

- conversation_id: conv-20260607192812-ch32-sistema-bando-personale
- route: chapter-32-sistema-bando-personale
- l0: l0/conv-20260607192812-ch32-sistema-bando-personale.md
- atoms:
  - mem-20260607192812-ch32-workflow | workflow | ora prossimo capitolo
  - mem-20260607192812-ch32-result | result | Creato il Capitolo 32 extra del Metodo BANDO: Il tuo sistema BANDO personale.

## 2026-06-07T17:49:41.913Z - il-metodo-bando

- conversation_id: conv-20260607174941-12bhj9c
- route: codex/chapter16-editorial-images
- l0: l0/conv-20260607174941-12bhj9c.md
- atoms:
  - mem-20260607174941-pom8u0 | workflow | ora procedi con lo stesso procedimento al prossimo capitolo
  - mem-20260607174941-1svq46j | result | Esito codex/chapter16-editorial-images: ora procedi con lo stesso procedimento al prossimo capitolo -> Capitolo 16 La prova orale illustrato con 7 figure professionali SVG+PNG: mappa operativa prova orale, scheda orale bando, struttura universale risposta orale, risposta in due minuti, collegamenti e domande incrociate...

## 2026-06-07T19:55:28+02:00 - manual-writer

- conversation_id: conv-20260607195528-ch33-materiali-studio
- route: chapter-33-materiali-studio
- l0: l0/conv-20260607195528-ch33-materiali-studio.md
- atoms:
  - mem-20260607195528-ch33-workflow | workflow | prossimo capitolo procedi
  - mem-20260607195528-ch33-result | result | Creato il Capitolo 33 extra del Metodo BANDO: Manuali, corsi e banche dati: scegliere senza disperdersi.

## 2026-06-07T18:09:47.448Z - il-metodo-bando

- conversation_id: conv-20260607180947-oro3xo
- route: codex/chapter17-editorial-images
- l0: l0/conv-20260607180947-oro3xo.md
- atoms:
  - mem-20260607180947-ttbc2v | result | Esito codex/chapter17-editorial-images: prossimo capitolo procedi -> Capitolo 17 Casi pratici e problem solving amministrativo illustrato con 7 figure professionali SVG+PNG: mappa BANDO del caso pratico, caso come fascicolo amministrativo ridotto, griglia in otto domande, schema di ris...

## 2026-06-08T13:55:00+02:00 - il-metodo-bando

- conversation_id: conv-20260608135500-ch18-situazionali-images
- route: codex/chapter18-editorial-images
- l0: l0/conv-20260608135500-ch18-situazionali-images.md
- atoms:
  - mem-20260608135500-ch18-workflow | workflow | procedi con il capitolo successivo, identificazione delle immagini da inserire, generazione dell'immagine e inserimento professionale preciso come nei precedenti capitoli
  - mem-20260608135500-ch18-result | result | Capitolo 18 Quesiti situazionali e soft skills illustrato con 7 figure professionali SVG+PNG.

## 2026-06-08T17:50:37.572Z - manual-writer

- conversation_id: conv-20260608175037-z2bh7
- route: codex/ch34-simulazioni-concorsuali
- l0: l0/conv-20260608175037-z2bh7.md
- atoms:
  - mem-20260608175037-skunz5 | result | Esito codex/ch34-simulazioni-concorsuali: prossimo capitolo -> Creato il Capitolo 34 extra del Metodo BANDO: Simulazioni concorsuali: dalla preparazione alla prova.

## 2026-06-08T19:55:00+02:00 - il-metodo-bando

- conversation_id: conv-20260608195500-ch19-famiglie-images
- route: codex/chapter19-editorial-images
- l0: l0/conv-20260608195500-ch19-famiglie-images.md
- atoms:
  - mem-20260608195500-ch19-workflow | workflow | prossimo capitolo
  - mem-20260608195500-ch19-result | result | Capitolo 19 Le famiglie dei concorsi pubblici illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T08:49:36.381Z - manual-writer

- conversation_id: conv-20260609084936-13sgo5y
- route: codex/ch35-schede-operative
- l0: l0/conv-20260609084936-13sgo5y.md
- atoms:
  - mem-20260609084936-1mafs34 | workflow | procedi con il prossimo capitolo; vai
  - mem-20260609084936-1txg0nu | result | Esito codex/ch35-schede-operative: procedi con il prossimo capitolo; vai -> Creato il Capitolo 35 extra del Metodo BANDO: Schede operative: trasformare studio ed errori in risposte.

## 2026-06-09T10:52:01.4580719+02:00 - il-metodo-bando

- conversation_id: conv-20260609105201-ch20-mappe-profilo-images
- route: codex/chapter20-editorial-images
- l0: l0/conv-20260609105201-ch20-mappe-profilo-images.md
- atoms:
  - mem-20260609105201-ch20-workflow | workflow | procedi ocn il prossimo capitolo
  - mem-20260609105201-ch20-result | result | Capitolo 20 Mappe profilo: cosa resta comune e cosa cambia illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T11:12:55.6026857+02:00 - il-metodo-bando

- conversation_id: conv-20260609111255-ch21-moduli-integrativi-images
- route: codex/chapter21-editorial-images
- l0: l0/conv-20260609111255-ch21-moduli-integrativi-images.md
- atoms:
  - mem-20260609111255-ch21-workflow | workflow | prossimo capitolo procedi
  - mem-20260609111255-ch21-result | result | Capitolo 21 Come scegliere i moduli integrativi illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T09:16:20.262Z - manual-writer

- conversation_id: conv-20260609091620-1fj2bn6
- route: codex/ch36-taglio-priorita-studio
- l0: l0/conv-20260609091620-1fj2bn6.md
- atoms:
  - mem-20260609091620-rcxmrz | result | Esito codex/ch36-taglio-priorita-studio: ok procedi -> Creato il Capitolo 36 extra del Metodo BANDO: Tagliare senza perdere punti: priorita e studio ad alta resa.

## 2026-06-09T13:15:22.7557043+02:00 - il-metodo-bando

- conversation_id: conv-20260609131522-ch22-piano-30-60-90-images
- route: codex/chapter22-editorial-images
- l0: l0/conv-20260609131522-ch22-piano-30-60-90-images.md
- atoms:
  - mem-20260609131522-ch22-workflow | workflow | prossimo capitolo
  - mem-20260609131522-ch22-result | result | Capitolo 22 Piano 30/60/90 giorni illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T12:14:58.066Z - manual-writer

- conversation_id: conv-20260609121458-ee2e5b
- route: codex/ch37-strategia-punteggio-prova
- l0: l0/conv-20260609121458-ee2e5b.md
- atoms:
  - mem-20260609121458-174e3oi | workflow | procedi con prossimo capitolo
  - mem-20260609121458-rrz2bq | result | Esito codex/ch37-strategia-punteggio-prova: procedi con prossimo capitolo -> Creato il Capitolo 37 extra del Metodo BANDO: Strategia di punteggio: soglie, tempo e rischio nella prova.

## 2026-06-09T14:30:14.3644559+02:00 - il-metodo-bando

- conversation_id: conv-20260609143014-ch23-diario-errori-images
- route: codex/chapter23-editorial-images
- l0: l0/conv-20260609143014-ch23-diario-errori-images.md
- atoms:
  - mem-20260609143014-ch23-workflow | workflow | procedi con prossimo capitolo
  - mem-20260609143014-ch23-result | result | Capitolo 23 Il diario degli errori illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T16:27:53.3228734+02:00 - il-metodo-bando

- conversation_id: conv-20260609162753-ch24-checklist-operative-images
- route: codex/chapter24-editorial-images
- l0: l0/conv-20260609162753-ch24-checklist-operative-images.md
- atoms:
  - mem-20260609162753-ch24-workflow | workflow | prossimo capitolo
  - mem-20260609162753-ch24-result | result | Capitolo 24 Checklist operative illustrato con 7 figure professionali SVG+PNG.

## 2026-06-09T14:34:32.936Z - manual-writer

- conversation_id: conv-20260609143432-18e3sgb
- route: codex/ch38-giorno-prova
- l0: l0/conv-20260609143432-18e3sgb.md
- atoms:
  - mem-20260609143432-7fxhpv | result | Esito codex/ch38-giorno-prova: prossimo capitolo -> Creato il Capitolo 38 extra del Metodo BANDO: Il giorno della prova: routine, logistica e lucidita operativa.

## 2026-06-09T17:20:17.556Z - manual-writer

- conversation_id: conv-20260609172017-gp8h7e
- route: codex/ch39-intervallo-prove
- l0: l0/conv-20260609172017-gp8h7e.md
- atoms:
  - mem-20260609172017-mran3o | result | Esito codex/ch39-intervallo-prove: PROSSIMO CAPITOLO -> Creato il Capitolo 39 extra del Metodo BANDO: Tra una prova e l'altra: ripianificare senza ricominciare.

## 2026-06-09T19:22:06.0253752+02:00 - il-metodo-bando

- conversation_id: conv-20260609192206-ch25-aggiornare-metodo-images
- route: codex/chapter25-editorial-images
- l0: l0/conv-20260609192206-ch25-aggiornare-metodo-images.md
- atoms:
  - mem-20260609192206-ch25-workflow | workflow | PROSSIMO CAPITOLO
  - mem-20260609192206-ch25-result | result | Capitolo 25 Aggiornare il metodo dopo il libro illustrato con 7 figure professionali SVG+PNG.

## 2026-06-10T14:55:42.1454789+02:00 - il-metodo-bando

- conversation_id: conv-20260610145542-ch26-capitale-studio-images
- route: codex/chapter26-editorial-images
- l0: l0/conv-20260610145542-ch26-capitale-studio-images.md
- atoms:
  - mem-20260610145542-ch26-workflow | workflow | Con il prossimo capitolo
  - mem-20260610145542-ch26-result | result | Capitolo 26 Trasformare ogni concorso in capitale di studio illustrato con 7 figure professionali SVG+PNG.

## 2026-06-10T13:59:33.529Z - manual-writer

- conversation_id: conv-20260610135933-6gooud
- route: codex/ch40-ripasso-finale
- l0: l0/conv-20260610135933-6gooud.md
- atoms:
  - mem-20260610135933-3beybi | workflow | Procedi con il prossimo capitolo.
  - mem-20260610135933-1fmy0em | result | Esito codex/ch40-ripasso-finale: Procedi con il prossimo capitolo. -> Creato il Capitolo 40 extra del Metodo BANDO: Ripasso finale: consolidare senza saturarsi.

## 2026-06-10T16:09:31.8187103+02:00 - il-metodo-bando

- conversation_id: conv-20260610160931-ch27-concorsi-paralleli-images
- route: codex/chapter27-editorial-images
- l0: l0/conv-20260610160931-ch27-concorsi-paralleli-images.md
- atoms:
  - mem-20260610160931-ch27-workflow | workflow | procedi prossimo capitolo
  - mem-20260610160931-ch27-result | result | Capitolo 27 Gestire concorsi paralleli senza disperdersi illustrato con 7 figure professionali SVG+PNG.

## 2026-06-12T09:49:51.749Z - manual-writer

- conversation_id: conv-20260612094951-11lznqr
- route: codex/ch41-caso-completo-bando
- l0: l0/conv-20260612094951-11lznqr.md
- atoms:
  - mem-20260612094951-1uys01 | result | Esito codex/ch41-caso-completo-bando: procedi con il prossimo capitolo -> Creato il Capitolo 41 extra del Metodo BANDO: Caso completo BANDO: dal bando alla prova.

## 2026-06-12T09:52:16.281Z - il-metodo-bando

- conversation_id: conv-20260612095216-178ykdn
- route: codex/chapter28-editorial-images
- l0: l0/conv-20260612095216-178ykdn.md
- atoms:
  - mem-20260612095216-10lti1a | result | Esito codex/chapter28-editorial-images: prossimo capitolo -> Capitolo 28 Usare il digitale senza perdere il metodo illustrato con 7 figure professionali SVG+PNG: mappa BANDO del digitale, regola 1-3-5, cartella minima, AI assistente non fonte, protocollo AI sicuro, digitale/car...

## 2026-06-14T15:58:53.214Z - il-metodo-bando

- conversation_id: conv-20260614155853-1i503yy
- route: codex/chapter29-editorial-images
- l0: l0/conv-20260614155853-1i503yy.md
- atoms:
  - mem-20260614155853-1ro7szv | result | Esito codex/chapter29-editorial-images: prossimo capitolo procedi -> Capitolo 29 Reggere la preparazione: energia, ansia e continuita illustrato con 7 figure professionali SVG+PNG: mappa BANDO della sostenibilita, scala energia, minimo efficace, recupero senza distruggere il piano, ans...

## 2026-06-14T16:10:39.089Z - manual-writer

- conversation_id: conv-20260614161039-ks2ki6
- route: codex/ch42-banca-dati-ufficiale
- l0: l0/conv-20260614161039-ks2ki6.md
- atoms:
  - mem-20260614161039-1oxwfiu | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 41.
  - mem-20260614161039-oh5sy5 | result | Esito codex/ch42-banca-dati-ufficiale: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 41. -> Creato Capitolo 42: Banca dati ufficiale: studiarla senza memorizzare male.

## 2026-06-14T19:20:58.045Z - manual-writer

- conversation_id: conv-20260614192058-1berl6p
- route: codex/chapter30-editorial-images
- l0: l0/conv-20260614192058-1berl6p.md
- atoms:
  - mem-20260614192058-9yngr9 | result | Esito codex/chapter30-editorial-images: prossimo capitolo procedi -> Capitolo 30 Dopo la prova: esiti, graduatoria e prossima mossa illustrato con 7 figure professionali SVG+PNG in chapter-30: mappa BANDO, prime 24 ore, tre livelli di esito, cartella dopo-prova, graduatoria/accesso att...

## 2026-06-14T20:10:22.327Z - manual-writer

- conversation_id: conv-20260614201022-dunwve
- route: codex/ch43-risposta-sintetica
- l0: l0/conv-20260614201022-dunwve.md
- atoms:
  - mem-20260614201022-i3vvv9 | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 42.
  - mem-20260614201022-156g8ur | result | Esito codex/ch43-risposta-sintetica: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 42. -> Creato Capitolo 43: Risposta sintetica: scrivere poco, dire tutto.

## 2026-06-15T12:21:37.773Z - manual-writer

- conversation_id: conv-20260615122137-1qlf0fh
- route: codex/ch44-confrontare-istituti-simili
- l0: l0/conv-20260615122137-1qlf0fh.md
- atoms:
  - mem-20260615122137-kih0gv | workflow | Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 43.
  - mem-20260615122137-191m2pm | result | Esito codex/ch44-confrontare-istituti-simili: Procedi con il prossimo capitolo professionale del Metodo BANDO dopo il Capitolo 43. -> Creato Capitolo 44: Confrontare istituti simili: differenze che fanno punti.

## 2026-06-15T12:21:46.420Z - manual-writer

- conversation_id: conv-20260615122146-11zuqpx
- route: codex/chapter31-editorial-images
- l0: l0/conv-20260615122146-11zuqpx.md
- atoms:
  - mem-20260615122146-1u3cwzr | result | Esito codex/chapter31-editorial-images: prossimo capitolo procedi -> Capitolo 31 Prendere servizio nella PA: dal concorso al ruolo illustrato con 7 figure professionali SVG+PNG in chapter-31: mappa BANDO della presa di servizio, sequenza dal concorso al ruolo, cartella di ingresso, qua...

## 2026-06-16T20:13:12.023Z - manual-writer

- conversation_id: conv-20260616201312-1vz86jl
- route: codex/ch45-collegare-materie
- l0: l0/conv-20260616201312-1vz86jl.md
- atoms:
  - mem-20260616201312-1tsmgby | result | Esito codex/ch45-collegare-materie: PROSSIMO CAPITOLO PROCEDI -> Creato Capitolo 45 del Metodo BANDO: Collegare le materie: dal programma alla risposta integrata.

## 2026-06-16T23:11:39.534Z - manual-writer

- conversation_id: conv-20260616231139-1ch2u9j
- route: codex/chapter32-editorial-images
- l0: l0/conv-20260616231139-1ch2u9j.md
- atoms:
  - mem-20260616231139-1qls1lf | result | Esito codex/chapter32-editorial-images: PROSSIMO CAPITOLO PROCEDI -> Capitolo 32 Il tuo sistema BANDO personale illustrato con 7 figure professionali SVG+PNG in chapter-32: mappa BANDO del sistema personale, cinque pagine vive, protocollo 15/30/60, cruscotto BANDO personale, mantieni-a...

## 2026-06-17T14:39:25.856Z - manual-writer

- conversation_id: conv-20260617143925-hzqp8m
- route: codex/chapter33-editorial-images
- l0: l0/conv-20260617143925-hzqp8m.md
- atoms:
  - mem-20260617143925-1sx4qq | result | Esito codex/chapter33-editorial-images: PROSSIMO CAPITOLO PROCEDI -> Capitolo 33 Manuali, corsi e banche dati: scegliere senza disperdersi illustrato con 7 figure professionali SVG+PNG in chapter-33: mappa BANDO dei materiali, prima bando poi materiale, pila minima, scorecard materiali...

## 2026-06-17T14:41:23.180Z - manual-writer

- conversation_id: conv-20260617144123-g8t0g1
- route: codex/ch46-domande-impreviste
- l0: l0/conv-20260617144123-g8t0g1.md
- atoms:
  - mem-20260617144123-1rzoyf9 | result | Esito codex/ch46-domande-impreviste: PROSSIMO CAPITOLO PROCEDI -> Creato Capitolo 46 del Metodo BANDO: Domande impreviste: rispondere senza inventare.

## 2026-06-20T03:33:16.240Z - manual-writer

- conversation_id: conv-20260620033316-payn4r
- route: codex/ch47-revisione-finale
- l0: l0/conv-20260620033316-payn4r.md
- atoms:
  - mem-20260620033316-1oeucbw | result | Esito codex/ch47-revisione-finale: prossimo capitolo -> Creato Capitolo 47 del Metodo BANDO: Revisione finale: controllare prima di consegnare.

## 2026-06-27T19:04:42+02:00 - manual-writer

- conversation_id: conv-20260627190442-ricettario-digitale
- route: codex/editorial-architecture-ricettario-digitale
- l0: l0/conv-20260627190442-ricettario-digitale.md
- atoms:
  - mem-20260627190442-ricettario-digitale | instruction | Per Il Metodo BANDO, i capitoli 1-24 restano nel volume principale senza riduzione strutturale; i capitoli 25-47 gia scritti vanno trattati come Ricettario operativo digitale, moduli R1-R23 collegati al libro e non come corpo cartaceo principale.

## 2026-06-27T19:56:28+02:00 - manual-writer

- conversation_id: conv-20260627195628-moduli-specialistici
- route: codex/editorial-architecture-moduli-specialistici
- l0: l0/conv-20260627195628-moduli-specialistici.md
- atoms:
  - mem-20260627195628-moduli-specialistici | instruction | Per Il Metodo BANDO, i moduli specialistici vivono in wiki/books/moduli/<module-id>/ come libri di lavoro separati: 6 famiglie e 25 moduli canonici, con book_id uguale allo slug cartella, index.md e capitoli in chapters/.

## 2026-06-29T12:48:07.887Z - manual-writer

- conversation_id: conv-20260629124807-1d0ax5h
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629124807-1d0ax5h.md
- atoms:
  - mem-20260629124807-pg6ite | workflow | instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti e struttura Metodo BANDO, riscrivi solo i passaggi necessari.
  - mem-20260629124807-1uojduy | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti ... -> Revisione humanizer completata su books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md.

## 2026-06-29T15:08:07.606Z - manual-writer

- conversation_id: conv-20260629150807-1282rhq
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629150807-1282rhq.md
- atoms:
  - mem-20260629150807-hyeogg | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/il-metodo-bando/chapters/anatomia-del-bando.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva significato, riferimenti e struttu... -> Revisione humanizer completata su books/il-metodo-bando/chapters/anatomia-del-bando.md.

## 2026-06-29T15:12:24.544Z - manual-writer

- conversation_id: conv-20260629151224-1qwkjb3
- route: ManualWriterAgent.reviseChapter
- l0: l0/conv-20260629151224-1qwkjb3.md
- atoms:
  - mem-20260629151224-12xtpfh | result | Esito ManualWriterAgent.reviseChapter: chapterPath=books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri-funzioni-centrali.md mode=humanizer_revision instruction=Applica la skill humanizer al capitolo: rimuovi segnali di scrittura AI, conserva signi... -> Revisione humanizer completata su books/moduli/m-fc01-ministeri/chapters/01-lavorare-ministeri-funzioni-centrali.md.

## 2026-06-29T15:21:36.094Z - manual-writer

- conversation_id: conv-20260629152136-v2ve0a
- route: ManualWriterAgent.writeChapter
- l0: l0/conv-20260629152136-v2ve0a.md
- atoms:
  - mem-20260629152136-1cg7i7s | workflow | instruction=Scrivi il capitolo effettivo , non un riepilogo tecnico.
  - mem-20260629152136-195qkxl | instruction | Usa prima il cervello wiki: struttura madre, nota capitolo, source notes, topic pages, entity pages e design system; scarica altre fonti necessarie per la copertura totale della conoscenza e procedi poi alla scrittura professionale del capitolo completo
  - mem-20260629152136-6r2rui | result | Esito ManualWriterAgent.writeChapter: chapterPath=books/moduli/m-fc01-ministeri/chapters/02-anatomia-bando-ministeriale-ripam.md mode=integrate instruction=Scrivi il capitolo effettivo , non un riepilogo tecnico. -> Manual Writer completato su books/moduli/m-fc01-ministeri/chapters/02-anatomia-bando-ministeriale-ripam.md.

## 2026-07-01T11:04:54.420Z - editorial-reviewer

- conversation_id: conv-20260701110454-1epn91o
- route: EditorialReviewerAgent.runReview
- l0: l0/conv-20260701110454-1epn91o.md
- atoms:
  - mem-20260701110454-kr0dhf | result | Esito EditorialReviewerAgent.runReview: bookId=moduli/m-tr04-ambiente-protezione-civile scope=full aspect=full -> Revisione editoriale completata su moduli/m-tr04-ambiente-protezione-civile.
## 2026-07-02T16:37:06.612Z - manual-writer

- conversation_id: conv-20260702163706-1t4oml3
- route: ManualWriterAgent.writeChapter
- l0: l0/conv-20260702163706-1t4oml3.md
- atoms:
  - mem-20260702163706-1pr3th0 | workflow | PRODEGUI CON IL SECONDO CAPITOLO DEL LIBRO
  - mem-20260702163706-1izkerd | result | Esito ManualWriterAgent.writeChapter: PRODEGUI CON IL SECONDO CAPITOLO DEL LIBRO -> M-FC02 capitolo 2 Bando Decoder fiscale completato in professional draft: trasformata la scheda source-ready in capitolo workbook da 444 righe con apertura editoriale, mappa BANDO, regole di compilazione, pagine opera...

## 2026-07-02T17:24:56.314Z - manual-writer

- conversation_id: conv-20260702172456-1es68u
- route: codex/editorial-images/mfc02-chapter02
- l0: l0/conv-20260702172456-1es68u.md
- atoms:
  - mem-20260702172456-xesxf9 | workflow | Integra immagini editoriali coerenti nel capitolo 2 M-FC02 Bando Decoder fiscale, con layout senza sovrapposizioni.
  - mem-20260702172456-jajyrm | result | Esito codex/editorial-images/mfc02-chapter02: Integra immagini editoriali coerenti nel capitolo 2 M-FC02 Bando Decoder fiscale, con layout senza sovrapposizioni. -> Creati 5 asset SVG/PNG 1600x900 in stile libro base per il capitolo 2 M-FC02, inseriti nel markdown e verificati nel Book Studio.

## 2026-07-02T17:26:18.733Z - manual-writer

- conversation_id: conv-20260702172618-1am96gi
- route: codex/editorial-images/mfc02-chapter02-correction
- l0: l0/conv-20260702172618-1am96gi.md
- atoms:
  - mem-20260702172618-86ux49 | workflow | Correggi dettaglio memoria intervento immagini M-FC02 capitolo 2.
  - mem-20260702172618-1a63obw | result | Esito codex/editorial-images/mfc02-chapter02-correction: Correggi dettaglio memoria intervento immagini M-FC02 capitolo 2. -> Correzione dettaglio: nel Book Studio il valore finale effettivo di PAGE_MEASURE_GUARD_SPACE per la paginazione misurata e 180.

## 2026-07-02T17:42:54.296Z - manual-writer

- conversation_id: conv-20260702174254-2ptyt9
- route: codex/manual-writer/mfc02-chapter03
- l0: l0/conv-20260702174254-2ptyt9.md
- atoms:
  - mem-20260702174254-iq6giv | instruction | Redigere il terzo capitolo del modulo M-FC02 con stile accademico/manualistico, fonti consolidate e struttura dei capitoli esistenti.
  - mem-20260702174254-14g79zt | result | Esito codex/manual-writer/mfc02-chapter03: Redigere il terzo capitolo del modulo M-FC02 con stile accademico/manualistico, fonti consolidate e struttura dei capitoli esistenti. -> M-FC02 capitolo 3 completato in professional draft: ordinamento e organizzazione di Agenzia delle Entrate, ADM e Agenzia delle entrate-Riscossione; D.Lgs.

## 2026-07-03T15:37:48.293Z - concorso-book-os

- conversation_id: conv-20260703153748-oyh59l
- route: codex/dashboard-catalog-restructure
- l0: l0/conv-20260703153748-oyh59l.md
- atoms:
  - mem-20260703153748-pv65mj | workflow | Analizzare il DOCX Idea di business e vendita libri Capitale Personale e ristrutturare dashboard e lista testi in funzione della nuova struttura dei volumi.
  - mem-20260703153748-1g54jxj | result | Esito codex/dashboard-catalog-restructure: Analizzare il DOCX Idea di business e vendita libri Capitale Personale e ristrutturare dashboard e lista testi in funzione della nuova struttura dei volumi. -> Dashboard ristrutturata intorno al catalogo commerciale a 12 volumi.

## 2026-07-10T22:13:34.957Z - catalog-dashboard

- conversation_id: conv-20260710221334-8fk3vl
- route: catalog-volume-scope-correction
- l0: l0/conv-20260710221334-8fk3vl.md
- atoms:
  - mem-20260710221334-zq2w8j | workflow | Nel catalogo dashboard, il Volume 1 Il Metodo BANDO non deve essere toccato.
  - mem-20260710221334-1xcl483 | result | Esito catalog-volume-scope-correction: Nel catalogo dashboard, il Volume 1 Il Metodo BANDO non deve essere toccato. -> Correzione applicata: VOL-01 resta il libro base originale; l'aggregazione editoriale resta limitata ai volumi specialistici VOL-02-VOL-12.

## 2026-07-14T15:57:55.466Z - il-metodo-bando

- conversation_id: conv-20260714155755-1ueyp44
- route: codex/manual-writer
- l0: l0/conv-20260714155755-1ueyp44.md
- atoms:
  - mem-20260714155755-1pwxyid | workflow | Completa le sezioni mancanti di VOL-01 e analizza le modifiche al layout dei capitoli.
  - mem-20260714155755-1hbj0xm | result | Esito codex/manual-writer: Completa le sezioni mancanti di VOL-01 e analizza le modifiche al layout dei capitoli. -> Completate B-PA04 con un quadro essenziale sui reati contro la PA nel capitolo 6 e B-PA11 con il laboratorio di redazione atti nel capitolo 15.

## 2026-07-14T16:06:49.823Z - catalog-governance

- conversation_id: conv-20260714160649-lfigmj
- route: Codex.volume-coverage-v4
- l0: l0/conv-20260714160649-lfigmj.md
- atoms:
  - mem-20260714160649-18ljyby | project_fact | Rendere logica_volumi_copertura_concorsobook_v4.md la base vincolante per sviluppo dei volumi, prossimi passi e revisioni.
  - mem-20260714160649-18qc8ta | result | Esito Codex.volume-coverage-v4: Rendere logica_volumi_copertura_concorsobook_v4.md la base vincolante per sviluppo dei volumi, prossimi passi e revisioni. -> Ingestita la fonte v4 e applicata a architettura, AGENTS, Manual Writer e Revisore Editoriale.

## 2026-07-14T16:58:08.462Z - vol01-editorial-review

- conversation_id: conv-20260714165808-w505d2
- route: Codex.fullVolumeReview
- l0: l0/conv-20260714165808-w505d2.md
- atoms:
  - mem-20260714165808-1lx9tc2 | instruction | Analizzare integralmente VOL-01, usare le skill writer e revisore, verificare le 11 aree B-PA, correggere grammatica e impaginazione professionale, usare come struttura canonica il file VOL-01 del 14 luglio 2026 e conservare tutte le immagini esistenti.
  - mem-20260714165808-1ke3qis | result | Esito Codex.fullVolumeReview: Analizzare integralmente VOL-01, usare le skill writer e revisore, verificare le 11 aree B-PA, correggere grammatica e impaginazione professionale, usare come struttura canonica il file VOL-01 del 14 luglio 2026 e con... -> Revisione completa eseguita.

## 2026-07-15T19:02:10.448Z - editorial-layout

- conversation_id: conv-20260715190210-13qj2ug
- route: Codex.volume01LayoutOptimization
- l0: l0/conv-20260715190210-13qj2ug.md
- atoms:
  - mem-20260715190210-1b65r83 | result | Esito Codex.volume01LayoutOptimization: Le pagine del Volume 1 non sono ottimizzate: c'e troppo spazio vuoto tra le pagine. -> Ottimizzata la paginazione A4 del VOL-01 Il Metodo BANDO.

## 2026-07-16T16:51:02.569Z - editorial-layout

- conversation_id: conv-20260716165102-18b2mx0
- route: Codex.bookStudioPreviewRegressionFix
- l0: l0/conv-20260716165102-18b2mx0.md
- atoms:
  - mem-20260716165102-16yuo3g | project_fact | Sistema l'anteprima del libro: e cambiata, le immagini sono sotto e non e ottimizzata come prima.
  - mem-20260716165102-vdvg0c | result | Esito Codex.bookStudioPreviewRegressionFix: Sistema l'anteprima del libro: e cambiata, le immagini sono sotto e non e ottimizzata come prima. -> Individuata una sovrapposizione tra il pannello Asset libro e la preview A4 causata dalla griglia desktop a due colonne con controlli sticky.

## 2026-07-16T17:50:48.140Z - editorial-layout

- conversation_id: conv-20260716175048-14p2j85
- route: Codex.canonicalTypographySystem
- l0: l0/conv-20260716175048-14p2j85.md
- atoms:
  - mem-20260716175048-savrbb | result | Esito Codex.canonicalTypographySystem: Applicare a tutti i libri, esistenti e futuri, questa struttura: H1/H2/H3 Arial Bold 18-20/14/12 pt; corpo Garamond Regular 11 pt con interlinea 1,15-1,20; tabelle, quiz, schemi e box Arial 9,5-10 pt. -> Standard canonico applicato al renderer condiviso, al Manual Writer, al Revisore Editoriale e alla documentazione di collana.

## 2026-07-17T14:24:23.074Z - global

- conversation_id: conv-20260717142423-9pa203
- route: codex/dashboard-open
- l0: l0/conv-20260717142423-9pa203.md
- atoms:
  - mem-20260717142423-1r6zl25 | result | Esito codex/dashboard-open: apri dashboard -> Dashboard ConcorsoBook ripristinata sulla porta 3000: fermata l'istanza Next bloccata, rimossa esclusivamente la cache generata .next, riavviato il launcher ufficiale, verificati homepage e CSS con HTTP 200 e aperto i...

## 2026-07-17T14:35:53.605Z - global

- conversation_id: conv-20260717143553-1cfo53p
- route: codex/git-delivery
- l0: l0/conv-20260717143553-1cfo53p.md
- atoms:
  - mem-20260717143553-gu8wy8 | result | Esito codex/git-delivery: fai commit e push del progetto attuale -> Preparata la consegna su main dell'aggiornamento tipografico canonico Arial/Garamond.

## 2026-07-21T10:30:44.862Z - vol01-editorial-review

- conversation_id: conv-20260721103044-14ay82y
- route: codex.professional-review
- l0: l0/conv-20260721103044-14ay82y.md
- atoms:
  - mem-20260721103044-c6a3gf | result | Esito codex.professional-review: Effettuare la revisione professionale del VOL-01 con matrice didattica obbligatoria, audit retroattivo, integrazione editoriale e gate finale; nessun completo con concetti solo nominati, rinvii generici o review norma... -> Creata la matrice VOL-01 con 17 nuclei: 2 completi e 15 parziali.

## 2026-07-21T11:08:10.978Z - manual-writer

- conversation_id: conv-20260721110810-1sqoqx4
- route: vol01-p0-content-integration
- l0: l0/conv-20260721110810-1sqoqx4.md
- atoms:
  - mem-20260721110810-1sj6tti | result | Esito vol01-p0-content-integration: Procedere con le competenze editoriali per modificare e implementare il Volume 1 secondo la matrice obbligatoria e il gate di copertura didattica integrale. -> Integrati nei capitoli 11, 17, 23 e 24 dieci mini-reading con spiegazione, dieci casi pratici, un cruscotto cartaceo settimanale e dodici checklist.

## 2026-07-21T11:21:36.956Z - manual-writer

- conversation_id: conv-20260721112136-adr3zc
- route: vol01-p1-surface-structure
- l0: l0/conv-20260721112136-adr3zc.md
- atoms:
  - mem-20260721112136-t0xprf | result | Esito vol01-p1-surface-structure: Procedere con il secondo blocco della revisione professionale del Volume 1. -> Risolti E08 ed E13: le sezioni Note di review sono escluse dalla preview pubblica con test di regressione e le heading Sanità amministrativa sono uniformate.

## 2026-07-21T11:36:02.046Z - editorial-reviewer

- conversation_id: conv-20260721113602-1cz9436
- route: vol-01-intervento-p2
- l0: l0/conv-20260721113602-1cz9436.md
- atoms:
  - mem-20260721113602-1xejkc | instruction | Procedere con la revisione professionale del VOL-01 usando matrice didattica, audit retroattivo, integrazione editoriale e gate finale, preservando il lavoro e usando rinvii solo quando il contenuto completo esiste davvero altrove.
  - mem-20260721113602-1d3kmd4 | result | Esito vol-01-intervento-p2: Procedere con la revisione professionale del VOL-01 usando matrice didattica, audit retroattivo, integrazione editoriale e gate finale, preservando il lavoro e usando rinvii solo quando il contenuto completo esiste da... -> Intervento P2 completato: il Capitolo 9 e la source note canonica sono riallineati al D.Lgs.

## 2026-07-21T11:49:43.026Z - editorial-reviewer

- conversation_id: conv-20260721114943-9gtjny
- route: vol-01-intervento-p3
- l0: l0/conv-20260721114943-9gtjny.md
- atoms:
  - mem-20260721114943-7p0ao9 | result | Esito vol-01-intervento-p3: M-TR01 e M-TR02 saranno scritti a breve: mantenerli aperti e procedere con il passo successivo della revisione professionale del Volume 1. -> Completato l'intervento P3 sul Capitolo 9, Contratti pubblici essenziali.

## 2026-07-21T12:08:32.882Z - editorial-reviewer

- conversation_id: conv-20260721120832-x833iz
- route: vol-01-intervento-p4
- l0: l0/conv-20260721120832-x833iz.md
- atoms:
  - mem-20260721120832-7619i7 | result | Esito vol-01-intervento-p4: Prossimo passo nella revisione professionale del Volume 1, mantenendo M-TR01 e M-TR02 aperti finche non saranno scritti. -> Completato l'intervento P4 sul raccordo B-PA07 fra Capitolo 7 e Capitolo 10.

## 2026-07-21T12:22:05.022Z - editorial-reviewer

- conversation_id: conv-20260721122205-qgmkwh
- route: vol-01-intervento-p5
- l0: l0/conv-20260721122205-qgmkwh.md
- atoms:
  - mem-20260721122205-wocr9o | result | Esito vol-01-intervento-p5: Prossimo passo nella revisione professionale del Volume 1. -> Completato l'intervento P5 sul nucleo B-PA01 del Capitolo 4.

## 2026-07-21T13:57:06.919Z - editorial-reviewer

- conversation_id: conv-20260721135706-iuija9
- route: vol-01-intervento-p6
- l0: l0/conv-20260721135706-iuija9.md
- atoms:
  - mem-20260721135706-qa6u8k | result | Esito vol-01-intervento-p6: Procedere con il prossimo passo della revisione professionale del Volume 1. -> Completato l'intervento P6 sul nucleo B-PA02 del Capitolo 5.

## 2026-07-21T14:15:22.100Z - editorial-reviewer

- conversation_id: conv-20260721141522-105euax
- route: vol-01-intervento-p7
- l0: l0/conv-20260721141522-105euax.md
- atoms:
  - mem-20260721141522-1yxvlvx | result | Esito vol-01-intervento-p7: Procedere con il prossimo passo della revisione professionale del Volume 1. -> Completato P7 B-PA03 Capitolo 6: fonti D.Lgs.

## 2026-07-21T14:26:22.870Z - editorial-reviewer

- conversation_id: conv-20260721142622-8lixn
- route: vol-01-intervento-p8
- l0: l0/conv-20260721142622-8lixn.md
- atoms:
  - mem-20260721142622-19omj44 | result | Esito vol-01-intervento-p8: Procedere con il prossimo passo della revisione professionale del Volume 1. -> P8 B-PA04: consolidate distinzioni tra reato, illecito disciplinare e responsabilita contabile; aggiunta mappa delle fattispecie e report.

## 2026-07-21T15:03:07.156Z - manual-writer

- conversation_id: conv-20260721150307-qke7qs
- route: codex/p9-capitolo-8-tracciabilita
- l0: l0/conv-20260721150307-qke7qs.md
- atoms:
  - mem-20260721150307-h0t58v | workflow | Il Capitolo 8 contiene gia controlli, parificazione, agenti contabili e responsabilita erariale; il prossimo intervento deve essere mirato a tracciabilita normativa e mappa di studio, senza duplicare contenuti.
  - mem-20260721150307-1axikhx | workflow | Proseguo con P9: il Capitolo 8 e confermato completo sul piano didattico di base; applica fonti, riferimenti normativi e matrice, senza duplicazioni.
  - mem-20260721150307-1yo55ka | result | Esito codex/p9-capitolo-8-tracciabilita: Il Capitolo 8 contiene gia controlli, parificazione, agenti contabili e responsabilita erariale; il prossimo intervento deve essere mirato a tracciabilita normativa e mappa di studio, senza duplicare contenuti. -> P9 applicato al Capitolo 8: aggiunte solo traccia normativa, matrice fonte-nucleo-output e checkpoint; aggiornato B-PA05 a completo con review giuridica umana ancora obbligatoria.

## 2026-07-23T08:24:51.501Z - editorial-reviewer

- conversation_id: conv-20260723082451-ki8kz4
- route: vol-01-intervento-p10
- l0: l0/conv-20260723082451-ki8kz4.md
- atoms:
  - mem-20260723082451-1cxr7t6 | workflow | continua la revisione professionale del volume 1 in base alla nuova matrice, da dove ci siamo fermati anche dopo il lavoro di Claude
  - mem-20260723082451-1myqto7 | result | Esito vol-01-intervento-p10: continua la revisione professionale del volume 1 in base alla nuova matrice, da dove ci siamo fermati anche dopo il lavoro di Claude -> Verificato e formalizzato P10 sui Capitoli 12, 14 e 18: i collegamenti interni già inseriti sono coerenti, B-PA10 resta completo nella matrice; aperta la sola verifica psicometrica/metodologica umana.

## 2026-07-23T08:29:35.152Z - editorial-reviewer

- conversation_id: conv-20260723082935-ob1n7n
- route: vol-01-intervento-p11
- l0: l0/conv-20260723082935-ob1n7n.md
- atoms:
  - mem-20260723082935-1tbaou6 | result | Esito vol-01-intervento-p11: prossimo passo -> P11 ha verificato l'apparato di riferimenti dei Capitoli 4-10 e ha chiuso E11 come rilievo superato.

## 2026-07-23T08:35:13.566Z - editorial-reviewer

- conversation_id: conv-20260723083513-1g7jre6
- route: vol-01-intervento-p12
- l0: l0/conv-20260723083513-1g7jre6.md
- atoms:
  - mem-20260723083513-1v24f7h | result | Esito vol-01-intervento-p12: prossimo passo -> P12 ha normalizzato il workflow del cartaceo principale: 31 file sono ora in editorial-review, con review_required invariato.

## 2026-07-23T08:37:23.056Z - editorial-reviewer

- conversation_id: conv-20260723083723-uopb1x
- route: vol-01-intervento-p13
- l0: l0/conv-20260723083723-uopb1x.md
- atoms:
  - mem-20260723083723-1il7t92 | result | Esito vol-01-intervento-p13: prossimo passo -> P13 ha controllato il Capitolo 11: dieci mini-reading con domanda, risposta e spiegazione sono presenti.

## 2026-07-23T08:39:37.089Z - editorial-reviewer

- conversation_id: conv-20260723083937-rpxesw
- route: vol-01-intervento-p14
- l0: l0/conv-20260723083937-rpxesw.md
- atoms:
  - mem-20260723083937-j4ulwl | result | Esito vol-01-intervento-p14: prossimo passo -> P14 ha verificato i Capitoli 15 e 17: sono presenti dieci casi completi con scenario, lettura, risposta modello ed errore da evitare.

## 2026-07-23T08:46:25.153Z - editorial-reviewer

- conversation_id: conv-20260723084625-3az0yu
- route: vol-01-intervento-p15
- l0: l0/conv-20260723084625-3az0yu.md
- atoms:
  - mem-20260723084625-13id8wj | result | Esito vol-01-intervento-p15: prossimo passo -> P15 ha verificato i Capitoli 13 e 16, chiudendo l'audit editoriale del blocco prove.

## 2026-07-23T08:48:18.522Z - editorial-reviewer

- conversation_id: conv-20260723084818-19wntuz
- route: vol-01-intervento-p16
- l0: l0/conv-20260723084818-19wntuz.md
- atoms:
  - mem-20260723084818-1mzfddi | result | Esito vol-01-intervento-p16: prosimo passo -> P16 ha verificato i Capitoli 19-22, confermando la logica core/modulo/prova e i piani 15/30/60/90 giorni.

## 2026-07-23T08:55:04.182Z - editorial-reviewer

- conversation_id: conv-20260723085504-18gd7zq
- route: vol-01-intervento-p17
- l0: l0/conv-20260723085504-18gd7zq.md
- atoms:
  - mem-20260723085504-p6vn6x | result | Esito vol-01-intervento-p17: prossimo passo -> P17 ha verificato diario, cruscotto e dodici checklist.

## 2026-07-23T08:57:14.538Z - editorial-reviewer

- conversation_id: conv-20260723085714-1dwdv7e
- route: vol-01-intervento-p18
- l0: l0/conv-20260723085714-1dwdv7e.md
- atoms:
  - mem-20260723085714-4hc1is | result | Esito vol-01-intervento-p18: prossimo passo -> P18 ha rieseguito il gate: VOL-01 ha 4 nuclei completi, 13 parziali, nessun nucleo solo nominato o mancante.

## 2026-07-23T09:19:03.552Z - editorial-reviewer

- conversation_id: conv-20260723091903-1lmzvyv
- route: wiki/reviews/review-vol-01-intervento-p19-preview-a4-2026-07-23.md
- l0: l0/conv-20260723091903-1lmzvyv.md
- atoms:
  - mem-20260723091903-c3ybel | result | Esito wiki/reviews/review-vol-01-intervento-p19-preview-a4-2026-07-23.md: Prossimo passo: continuare la revisione professionale di VOL-01 con la preview A4. -> P19 completata: la preview A4 runtime del Book Studio ha prodotto 349 pagine; il controllo DOM ha rilevato 0 overflow oltre 8 px e massimo 0 px.

## 2026-07-23T09:25:44.695Z - editorial-reviewer

- conversation_id: conv-20260723092544-y7m6al
- route: wiki/reviews/review-vol-01-intervento-p20-prova-stampa-2026-07-23.md
- l0: l0/conv-20260723092544-y7m6al.md
- atoms:
  - mem-20260723092544-19st2ne | result | Esito wiki/reviews/review-vol-01-intervento-p20-prova-stampa-2026-07-23.md: Prossimo passo. -> P20 completata: il Book Studio ha una preview A4 runtime ma non espone export PDF, stampa o endpoint di generazione PDF.

## 2026-07-23T09:31:20.634Z - editorial-reviewer

- conversation_id: conv-20260723093120-n33fve
- route: wiki/reviews/review-vol-01-intervento-p21-costituzionale-2026-07-23.md
- l0: l0/conv-20260723093120-n33fve.md
- atoms:
  - mem-20260723093120-jqh9oo | result | Esito wiki/reviews/review-vol-01-intervento-p21-costituzionale-2026-07-23.md: Procediamo in ordine a completarli. -> P21 ha chiuso B-PA01 a completo sul piano della copertura didattica e della verifica documentale: fonte Senato, Normattiva e Corte costituzionale ricontrollate il 23 luglio 2026.

## 2026-07-23T09:32:52.562Z - editorial-reviewer

- conversation_id: conv-20260723093252-xi8vas
- route: wiki/reviews/review-vol-01-intervento-p22-amministrativo-2026-07-23.md
- l0: l0/conv-20260723093252-xi8vas.md
- atoms:
  - mem-20260723093252-14eye2y | result | Esito wiki/reviews/review-vol-01-intervento-p22-amministrativo-2026-07-23.md: Procediamo in ordine a completarli. -> P21 e P22 completati in sequenza.

## 2026-07-23T09:35:28.086Z - editorial-reviewer

- conversation_id: conv-20260723093528-1ioks7a
- route: wiki/reviews/review-vol-01-intervento-p23-pubblico-impiego-2026-07-23.md
- l0: l0/conv-20260723093528-1ioks7a.md
- atoms:
  - mem-20260723093528-1vc565g | result | Esito wiki/reviews/review-vol-01-intervento-p23-pubblico-impiego-2026-07-23.md: Procedi. -> P23 ha chiuso B-PA03 a completo per copertura didattica e verifica documentale: D.Lgs.

## 2026-07-23T09:48:51.417Z - editorial-reviewer

- conversation_id: conv-20260723094851-1lgjba8
- route: wiki/reviews/review-vol-01-intervento-p24-reati-pa-2026-07-23.md
- l0: l0/conv-20260723094851-1lgjba8.md
- atoms:
  - mem-20260723094851-zxgal6 | result | Esito wiki/reviews/review-vol-01-intervento-p24-reati-pa-2026-07-23.md: Prossimo passo. -> P24 ha chiuso B-PA04 a completo per copertura didattica e verifica documentale: art.

## 2026-07-23T09:53:44.151Z - editorial-reviewer

- conversation_id: conv-20260723095344-1kjir9z
- route: wiki/reviews/review-vol-01-intervento-p25-contratti-2026-07-23.md
- l0: l0/conv-20260723095344-1kjir9z.md
- atoms:
  - mem-20260723095344-mgzi1z | result | Esito wiki/reviews/review-vol-01-intervento-p25-contratti-2026-07-23.md: Procedi. -> P25 ha chiuso B-PA06 a completo per copertura didattica e verifica documentale: D.Lgs.

## 2026-07-23T10:23:15.626Z - editorial-reviewer

- conversation_id: conv-20260723102315-x38pcw
- route: wiki/reviews/review-vol-01-intervento-p26-privacy-digitale-2026-07-23.md
- l0: l0/conv-20260723102315-x38pcw.md
- atoms:
  - mem-20260723102315-zlhsts | result | Esito wiki/reviews/review-vol-01-intervento-p26-privacy-digitale-2026-07-23.md: Prossimo passo. -> P26 ha chiuso B-PA07 a completo per copertura didattica e verifica documentale: CAD, GDPR e Piano Triennale AgID 2026 ricontrollati.

## 2026-07-23T11:57:43.253Z - editorial-reviewer

- conversation_id: conv-20260723115743-1mb7bcz
- route: wiki/reviews/review-vol-01-intervento-p27-inglese-2026-07-23.md
- l0: l0/conv-20260723115743-1mb7bcz.md
- atoms:
  - mem-20260723115743-1tovrut | result | Esito wiki/reviews/review-vol-01-intervento-p27-inglese-2026-07-23.md: Procedi. -> P27 ha chiuso B-PA08: verificati dieci mini-reading con testo, domanda, risposta e spiegazione e dieci chiavi grammaticali.

## 2026-07-23T12:52:57.263Z - editorial-reviewer

- conversation_id: conv-20260723125257-uc36nn
- route: wiki/reviews/review-vol-01-intervento-p28-informatica-2026-07-23.md
- l0: l0/conv-20260723125257-uc36nn.md
- atoms:
  - mem-20260723125257-4vfjsf | result | Esito wiki/reviews/review-vol-01-intervento-p28-informatica-2026-07-23.md: PROSSIMO PASSO? -> P28 ha chiuso B-PA09: verificati core operativo, caso guidato, otto domande da commissario, quattro mini-esercizi e checklist.

## 2026-07-23T13:01:12.129Z - editorial-reviewer

- conversation_id: conv-20260723130112-1suisc7
- route: wiki/reviews/review-vol-01-intervento-p29-atti-casi-2026-07-23.md
- l0: l0/conv-20260723130112-1suisc7.md
- atoms:
  - mem-20260723130112-17oc2md | result | Esito wiki/reviews/review-vol-01-intervento-p29-atti-casi-2026-07-23.md: procedi -> P29 ha chiuso B-PA11: verificati dieci casi completi, atto guidato, checklist, mini-simulazione e quadro delle prove teorico-pratiche.

## 2026-07-23T13:10:08.615Z - editorial-reviewer

- conversation_id: conv-20260723131008-5lfhfj
- route: wiki/reviews/review-vol-01-intervento-p30-prove-2026-07-23.md
- l0: l0/conv-20260723131008-5lfhfj.md
- atoms:
  - mem-20260723131008-1leyzuf | result | Esito wiki/reviews/review-vol-01-intervento-p30-prove-2026-07-23.md: procedi -> P30 ha chiuso V01-PROVE: verificati Capitoli 13-16, sequenza BANDO, schede, simulazioni, esercizi e diari.

## 2026-07-23T17:41:48.401Z - editorial-reviewer

- conversation_id: conv-20260723174148-18jlys
- route: wiki/reviews/review-vol-01-intervento-p31-profili-2026-07-23.md
- l0: l0/conv-20260723174148-18jlys.md
- atoms:
  - mem-20260723174148-h1a6uy | result | Esito wiki/reviews/review-vol-01-intervento-p31-profili-2026-07-23.md: procedi -> P31 ha chiuso V01-PROFILI: verificati core/delta, mappe, moduli e piani 15/30/60/90.

## 2026-07-23T17:56:08.016Z - editorial-reviewer

- conversation_id: conv-20260723175608-s0ggek
- route: wiki/reviews/review-vol-01-intervento-p32-kit-2026-07-23.md
- l0: l0/conv-20260723175608-s0ggek.md
- atoms:
  - mem-20260723175608-17wx1lb | result | Esito wiki/reviews/review-vol-01-intervento-p32-kit-2026-07-23.md: procedi -> P32 ha chiuso V01-KIT: verificati diario con sei categorie e cruscotto, piu dodici checklist autonome.

## 2026-07-23T18:26:06.568Z - editorial-reviewer

- conversation_id: conv-20260723182606-p52p7h
- route: manual-p33-vol01-appendici
- l0: l0/conv-20260723182606-p52p7h.md
- atoms:
  - mem-20260723182606-188tvtt | result | Esito manual-p33-vol01-appendici: Procedi con la revisione del volume 1. -> P33 ha chiuso V01-APP: 144 voci di glossario, 100 parole, Decoder di 9 pagine, piano di 12 pagine, tre durate orali e 13 profili.

## 2026-07-23T18:35:46.778Z - editorial-reviewer

- conversation_id: conv-20260723183546-ub6nam
- route: humanizer-vol01-h1
- l0: l0/conv-20260723183546-ub6nam.md
- atoms:
  - mem-20260723183546-1ep4dhr | workflow | Effettuare la revisione Humanizer su ogni capitolo del Volume 1 e applicare le correzioni necessarie.
  - mem-20260723183546-dgmhrq | result | Esito humanizer-vol01-h1: Effettuare la revisione Humanizer su ogni capitolo del Volume 1 e applicare le correzioni necessarie. -> H1 ha umanizzato introduzione e Capitoli 1-3: rimosse negazioni formulaiche, enfasi generiche e segnali metatestuali, preservando fonti, struttura e strumenti workbook.

## 2026-07-23T18:48:03.991Z - editorial-reviewer

- conversation_id: conv-20260723184803-1gol61z
- route: humanizer-vol01-h2
- l0: l0/conv-20260723184803-1gol61z.md
- atoms:
  - mem-20260723184803-hzm1p8 | result | Esito humanizer-vol01-h2: Procedi. -> H2 ha umanizzato i Capitoli 4-6: Costituzione, diritto amministrativo e pubblico impiego.

## 2026-07-23T18:50:09.913Z - editorial-reviewer

- conversation_id: conv-20260723185009-12eznim
- route: humanizer-vol01-h3
- l0: l0/conv-20260723185009-12eznim.md
- atoms:
  - mem-20260723185009-1g5v5g2 | result | Esito humanizer-vol01-h3: Procedi. -> H3 ha umanizzato i Capitoli 7-9: trasparenza/anticorruzione/privacy, contabilita pubblica e contratti pubblici.

## 2026-07-24T07:39:55.617Z - editorial-reviewer

- conversation_id: conv-20260724073955-128k9id
- route: humanizer-vol01-h4
- l0: l0/conv-20260724073955-128k9id.md
- atoms:
  - mem-20260724073955-1ly7yk | result | Esito humanizer-vol01-h4: Procedi. -> H4 ha umanizzato i Capitoli 10-12: informatica/PA digitale, inglese e logica.

## 2026-07-24T07:41:53.587Z - editorial-reviewer

- conversation_id: conv-20260724074153-1kv27e7
- route: humanizer-vol01-h5
- l0: l0/conv-20260724074153-1kv27e7.md
- atoms:
  - mem-20260724074153-db9dn4 | result | Esito humanizer-vol01-h5: Procedi. -> H5 ha umanizzato i Capitoli 13-15: metodo di studio, quiz e prova scritta teorico-pratica.

## 2026-07-24T08:03:51.298Z - editorial-reviewer

- conversation_id: conv-20260724080351-17w17mt
- route: humanizer-vol01-h6
- l0: l0/conv-20260724080351-17w17mt.md
- atoms:
  - mem-20260724080351-3r8kvt | result | Esito humanizer-vol01-h6: Procedi. -> H6 ha umanizzato i Capitoli 16-18: orale, casi pratici e quesiti situazionali.

## 2026-07-24T08:06:03.362Z - editorial-reviewer

- conversation_id: conv-20260724080603-1m7ktl7
- route: humanizer-vol01-h7
- l0: l0/conv-20260724080603-1m7ktl7.md
- atoms:
  - mem-20260724080603-53m760 | result | Esito humanizer-vol01-h7: Procedi. -> H7 ha umanizzato i Capitoli 19-21: famiglie concorsuali, mappe profilo e moduli integrativi.

## 2026-07-24T08:09:40.520Z - editorial-reviewer

- conversation_id: conv-20260724080940-1il3gmo
- route: humanizer-vol01-h8
- l0: l0/conv-20260724080940-1il3gmo.md
- atoms:
  - mem-20260724080940-164qidb | result | Esito humanizer-vol01-h8: Procedi. -> H8 ha umanizzato i Capitoli 22-24: piano 30/60/90, diario degli errori e checklist.

## 2026-07-24T08:19:08.965Z - editorial-reviewer

- conversation_id: conv-20260724081908-1j1bpiz
- route: humanizer-vol01-h9-final
- l0: l0/conv-20260724081908-1j1bpiz.md
- atoms:
  - mem-20260724081908-zb7ilj | result | Esito humanizer-vol01-h9-final: Procedi. -> H9 ha completato la revisione Humanizer del Volume 1 cartaceo: Introduzione, capitoli 1-24 e Appendici A-F, per 31 file.

## 2026-07-24T14:15:37.495Z - editorial-reviewer

- conversation_id: conv-20260724141537-4sw2fm
- route: ricettario-digitale-h1
- l0: l0/conv-20260724141537-4sw2fm.md
- atoms:
  - mem-20260724141537-xdiyma | result | Esito ricettario-digitale-h1: Procedi. -> Avviato il primo blocco del Ricettario digitale: R1-R5, capitoli 25-29.

## 2026-07-24T14:25:18.372Z - editorial-reviewer

- conversation_id: conv-20260724142518-1j9pwao
- route: ricettario-digitale-h2
- l0: l0/conv-20260724142518-1j9pwao.md
- atoms:
  - mem-20260724142518-4ovvt8 | result | Esito ricettario-digitale-h2: Procedi. -> Revisione micro-editoriale e Humanizer applicata ai moduli R6-R10 del Ricettario digitale, capitoli 30-34.

## 2026-07-24T14:31:48.826Z - editorial-reviewer

- conversation_id: conv-20260724143148-cyi81n
- route: ricettario-digitale-h3
- l0: l0/conv-20260724143148-cyi81n.md
- atoms:
  - mem-20260724143148-14j19dp | result | Esito ricettario-digitale-h3: Procedi. -> Revisione micro-editoriale e Humanizer applicata ai moduli R11-R15 del Ricettario digitale, capitoli 35-39.

## 2026-07-24T14:58:17.688Z - editorial-reviewer

- conversation_id: conv-20260724145817-qirewl
- route: ricettario-digitale-final
- l0: l0/conv-20260724145817-qirewl.md
- atoms:
  - mem-20260724145817-19jg7n | result | Esito ricettario-digitale-final: Completa. -> Completata la revisione editoriale e Humanizer del Ricettario operativo digitale: 23 moduli, R1-R23, capitoli 25-47.

## 2026-07-24T17:06:19.238Z - concorso-book

- conversation_id: conv-20260724170619-473ga
- route: codex/kdp-print-profile
- l0: l0/conv-20260724170619-473ga.md
- atoms:
  - mem-20260724170619-1qhvvbc | project_fact | Vorrei impostare il libro con tutti i parametri previsti per la stampa con Amazon.
  - mem-20260724170619-h8qhdq | result | Esito codex/kdp-print-profile: Vorrei impostare il libro con tutti i parametri previsti per la stampa con Amazon. -> Impostato il profilo di stampa Amazon KDP per Il Metodo BANDO: paperback A4 210 x 297 mm, bianco e nero su carta bianca, senza abbondanza, margini di sicurezza 18 mm sopra/sotto e 16 mm sui lati.

## 2026-07-24T17:22:00.168Z - concorso-book

- conversation_id: conv-20260724172200-99qela
- route: codex/kdp-format-conversion
- l0: l0/conv-20260724172200-99qela.md
- atoms:
  - mem-20260724172200-1rbnci4 | instruction | Adattiamo tutti i volumi al formato professionale 17 x 24 circa per Amazon KDP in maniera precisa.
  - mem-20260724172200-v0ylt4 | result | Esito codex/kdp-format-conversion: Adattiamo tutti i volumi al formato professionale 17 x 24 circa per Amazon KDP in maniera precisa. -> Tutto il Book Studio e le istruzioni editoriali usano ora il paperback KDP 6,69 x 9,61 in (16,99 x 24,41 cm), bianco e nero su carta bianca senza bleed, con margini speculari e gutter da 23 mm compatibile con tutti i ...

## 2026-07-24T18:37:15.849Z - concorso-book

- conversation_id: conv-20260724183715-x8ht71
- route: codex/kdp-layout-audit
- l0: l0/conv-20260724183715-x8ht71.md
- atoms:
  - mem-20260724183715-1cqjnjg | instruction | Procedi con il controllo di riflusso del Volume 1 nel formato KDP.
  - mem-20260724183715-1wm2j1f | result | Esito codex/kdp-layout-audit: Procedi con il controllo di riflusso del Volume 1 nel formato KDP. -> Audit visuale KDP eseguito sul Volume 1: 554 pagine, nessun overflow.

## 2026-07-25T11:16:42.791Z - concorso-book

- conversation_id: conv-20260725111642-15ottoq
- route: codex/volume1-print-master
- l0: l0/conv-20260725111642-15ottoq.md
- atoms:
  - mem-20260725111642-1af28fv | result | Esito codex/volume1-print-master: Il Volume 1 deve mantenere immagini, testo giustificato, pagine allineate e tipografia professionale coerente. -> Master corretto: immagini senza compattazione selettiva, Garamond 11 pt per il corpo giustificato, gerarchia Arial per titoli e strumenti, margini speculari KDP 20/13 mm e controllo automatico di immagini e overflow.

## 2026-07-25T14:18:29.635Z - concorso-book

- conversation_id: conv-20260725141829-1h2gv8
- route: codex/volume1-layout-balance
- l0: l0/conv-20260725141829-1h2gv8.md
- atoms:
  - mem-20260725141829-1yzxeeb | result | Esito codex/volume1-layout-balance: Procedi con il bilanciamento professionale delle pagine del Volume 1 mantenendo immagini, giustificazione e coerenza tipografica. -> Corretto il doppio accantonamento del margine inferiore nel budget di paginazione.

## 2026-07-25T14:59:56.382Z - concorso-book

- conversation_id: conv-20260725145956-1lpsf9l
- route: codex/dashboard-essential-performance
- l0: l0/conv-20260725145956-1lpsf9l.md
- atoms:
  - mem-20260725145956-yzalpc | workflow | Alleggerire molto la dashboard sulle funzioni essenziali per praticità e velocità di esecuzione.
  - mem-20260725145956-a7dw5x | result | Esito codex/dashboard-essential-performance: Alleggerire molto la dashboard sulle funzioni essenziali per praticità e velocità di esecuzione. -> Dashboard essenziale implementata con selezione testo, Studio, Writer e Revisione.

## 2026-07-25T15:08:09.350Z - concorso-book

- conversation_id: conv-20260725150809-m7r0we
- route: codex/github-team-sync
- l0: l0/conv-20260725150809-m7r0we.md
- atoms:
  - mem-20260725150809-1djo0lm | result | Esito codex/github-team-sync: Portare tutte le modifiche su GitHub preservando eventuali modifiche dello staff non ancora scaricate localmente. -> Prima del commit e del push è stato eseguito fetch di origin/main e verificata l'assenza di divergenze remote.

## 2026-07-25T16:47:36.445Z - book:il-metodo-bando:ricettario

- conversation_id: conv-20260725164736-yisggn
- route: manual-image-integration
- l0: l0/conv-20260725164736-yisggn.md
- atoms:
  - mem-20260725164736-12k8ltn | result | Esito manual-image-integration: Integra immagini professionali coerenti nel Ricettario digitale. -> Audit conclusivo: capitoli 34-47 con 7 riferimenti Markdown e 7 PNG ciascuno; 98 nuove immagini in totale, palette avorio-blu notte-bordeaux-oro e iconografia non testuale.

## 2026-07-26T17:02:16.955Z - book:il-metodo-bando:ricettario

- conversation_id: conv-20260726170216-1teh099
- route: ricettario-layout-audit
- l0: l0/conv-20260726170216-1teh099.md
- atoms:
  - mem-20260726170216-1u9e4fx | result | Esito ricettario-layout-audit: R22 ha immagini consecutive e alcuni esercizi sono formattati male; controlla tutto il Ricettario. -> Corretti R15-R23: immagini redistribuite nelle sezioni didattiche.
