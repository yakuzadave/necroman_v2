---
promptId: ganger_template
name: Ganger Template
description: Generate a Orlock ganger following the right formatting for Necromunda
author: Noureddine
tags:
  - ideas
  - writing
version: 0.0.1
---
content:
{{context}}
{{read "7-gangs/1-gang-lists/house-orlock/house-orlock.md"}}
{{read "7-gangs/1-gang-lists/house-orlock/equipment-list.md"}}
{{#each mentions.linked}} {{this.results}} {{/each}}
prompt:
Generate a ganger for House Orlock.  The following format (but not content) must be followed:

```
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
```



