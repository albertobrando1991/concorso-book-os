---
name: pipeline-volume
description: Use when executing or resuming the ConcorsoBook OS 25-step editorial pipeline for a volume, module, or chapter.
---

# Pipeline di volume

Il corpo canonico di questa skill è `.agents/skills/pipeline-volume/SKILL.md`, condiviso con Codex e con gli altri agenti. **Leggilo prima di procedere**: questo file è solo il puntatore che rende la skill invocabile da Claude Code.

In sintesi, il ciclo è:

```
npm run pipeline -- status VOL-03
npm run pipeline -- next VOL-03
# esegui il prompt scritto in artifacts/pipeline/<VOL>/<step>/<target>/prompt.md
npm run pipeline -- complete VOL-03 --step 09 --module M-FC02 --chapter 01
```

Nessun gate va saltato. Il run-state in `pipeline/<VOL>/run-state.json` non si modifica a mano.

Il corpo canonico definisce anche il formato 2 a nuclei, le soglie esposte dal contratto di `next` e il gate composito dello step 10. Un warning `retrofit-dovuto` non equivale a un gate verde; ogni blocker deve essere corretto prima di chiudere lo step.
