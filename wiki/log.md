# ConcorsoBook OS Log

- 2026-05-09T00:00:00.000Z | bootstrap | vault structure created | status=completed
- 2026-05-09T00:05:00.000Z | ingest | Legge 241/1990 - procedimento amministrativo | source=sources/legge-241-1990-procedimento-amministrativo.md | topics=procedimento amministrativo, diritto amministrativo | impacted=manuale-concorso-funzionari-enti-locali
- 2026-05-09T00:10:00.000Z | ingest | D.lgs. 267/2000 - enti locali | source=sources/dlgs-267-2000-enti-locali.md | topics=enti locali, pubblico impiego | impacted=manuale-concorso-funzionari-enti-locali
- 2026-05-09T00:15:00.000Z | ingest | ANAC - trasparenza e anticorruzione | source=sources/anac-trasparenza-e-anticorruzione.md | topics=anticorruzione e trasparenza, procedimento amministrativo | impacted=manuale-concorso-funzionari-enti-locali
- 2026-05-09T00:20:00.000Z | book_compile | manuale-concorso-funzionari-enti-locali | chapters=2
- 2026-05-09T00:25:00.000Z | lint | issues=3 | report=reviews/quality-review-2026-05-09.md
- 2026-05-09T01:00:00.000Z | ingest | Metodo BANDO - progetto editoriale | source=sources/metodo-bando-progetto-editoriale.md | topics=metodo bando, anatomia del bando, bando decoder, moduli profilo, piano 30 60 90 giorni, diario errori | impacted=il-metodo-bando
- 2026-05-09T01:05:00.000Z | book_compile | il-metodo-bando | chapters=4 | source_of_truth=sources/metodo-bando-progetto-editoriale.md
- 2026-05-10T00:00:00.000Z | ingest | Manuale di diritto amministrativo | source=sources/manuale-diritto-amministrativo-lopilato.md | topics=diritto amministrativo, fonti del diritto, organizzazione pubblica, principio di legalità | impacted=il-metodo-bando
- 2026-05-10T00:00:00.000Z | ingest | Responsabilità dirigenziale, performance e governo del rischio | source=sources/responsabilita-dirigenziale-legalita-organizzativa-performance-rischio.md | topics=responsabilità dirigenziale, performance amministrativa, governo del rischio, contratti pubblici, PNRR | impacted=il-metodo-bando
- 2026-05-10T11:45:00+02:00 | book_structure_update | Il Metodo BANDO | source=sources/struttura-madre-il-metodo-bando.md | chapters=25 | appendices=6 | status=structure-ready
- 2026-05-10T12:20:00+02:00 | ingest_metadata_only | Diritto costituzionale - manuale Bin/Pitruzzella | source=sources/diritto-costituzionale-bin-pitruzzella.md | raw=local_uncommitted_due_rights_review | impacted=books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato.md
- 2026-05-10T12:25:00+02:00 | ingest | Costituzione della Repubblica Italiana - testo vigente | source=sources/costituzione-repubblica-italiana-testo-vigente.md | topics=diritto costituzionale, ordinamento dello stato, fonti del diritto | impacted=books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato.md
- 2026-05-10T12:35:00+02:00 | rights_confirmed_process | Diritto costituzionale - manuale Bin/Pitruzzella | source=sources/diritto-costituzionale-bin-pitruzzella.md | raw=wiki/raw/manuals/diritto-costituzionale-bin-pitruzzella-authorized.pdf | policy=summaries_no_long_verbatim | impacted=books/il-metodo-bando/chapters/costituzione-e-ordinamento-dello-stato.md
- 2026-05-10T12:59:21+02:00 | editorial_design_system | Il Metodo BANDO | design=books/il-metodo-bando/design-system-editoriale.md | source=sources/book-layout-typography-standards.md | format=17x24cm | fonts=source-serif-4/source-sans-3 | dashboard_preview=updated
- 2026-05-10T13:16:00+02:00 | manual_writer_correction | Il Metodo BANDO | fixed=books/il-metodo-bando/chapters/introduzione.md,books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md | policy=write_actual_chapters_from_wiki_brain | web_research=review_only_until_consolidated

- 2026-05-10T11:10:49.244Z | manual_writer | books/il-metodo-bando/chapters/introduzione.md | mode=integrate | target_heading=Testo editoriale | knowledge=6
- 2026-05-10T11:11:22.156Z | manual_writer | books/il-metodo-bando/chapters/il-nuovo-candidato-pubblico.md | mode=integrate | target_heading=Testo editoriale | knowledge=5
- 2026-05-10T13:46:00+02:00 | dashboard_formatting_fix | Book Studio | format=A4_paginated | text=justified | pagination=anti_orphan_headings | screenshot=artifacts/dashboard-screenshot.png | verification=typecheck,test,build,screenshot
- 2026-05-10T14:22:00+02:00 | dashboard_pagination_optimization | Book Studio | pagination=measured_rendered_a4_blocks | tables=compact_manual_layout | headings=no_orphans | screenshot=artifacts/dashboard-screenshot.png | verification=typecheck,test,build,screenshot
