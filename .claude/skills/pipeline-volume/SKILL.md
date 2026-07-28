---
name: pipeline-volume
description: Use when running the ConcorsoBook OS editorial pipeline on a volume — executing the 25-prompt protocol chapter by chapter without pasting prompts by hand. Drives the loop next → work → gate → complete through the npm CLI, which owns state, order and gates.
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
