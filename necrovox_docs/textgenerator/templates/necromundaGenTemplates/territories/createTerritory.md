---
promptId: createTerritory
name: Create Territory
description: Generate a Territory following the right formatting for Necromunda
author: Katharsis
tags: []
version: 0.0.1
---
{{#each headings}}
# HEADER: {{@key}} 
{{this}} 
{{/each}}

{{read "Necromunda_Docs/8-campaigns/dominion-campaign/5-dominion-campaign-territories.md"}}
{{#each mentions.linked}} {{this.results}} {{/each}}

{{metadata}}
prompt:  Using the context above, expand the following in the context of a Necromunda territory:

{{selection}}
prompt:
Generate a Necromunda territory using the following rules and context.  The following format (but not content) must be followed:

# Location Details

## Description


## Special Rules


## Boons


## Income


## Dice Rolls



## Linked Territories


