---
promptId: escher_ganger_template
name: Escher Ganger Template
description: Generate a Escher ganger following the right formatting for Necromunda
author: Noureddine
tags:
  - ideas
  - writing
version: 0.0.1
chain.maxTokens: 4000
chain.type: map_reduce
splitter.chunkSize: 1000
splitter.chunkOverlap: 200
max_tokens: 4000
temperature: 0.6
---


```handlebars
{{read "7-gangs/1-gang-lists/house-escher/equipment-list.md"}}
```

prompt:
Generate a ganger for House Orlock.  The following format (but not content) must be followed:

---
type: ganger
name: ganger_name
faction: ganger_faction
subtype: ganger_subtype
movement: 4
weapon-skill: 4
ballistic-skill: 4
strength: 3
toughness: 3
wounds: 1
init: 4
attacks: 1
leadership: 7
cool: 7
willpower: 7
intelligence: 7
---

# Ganger Name


## Ganger Details


## Ganger Equipment


## Ganger Skills

