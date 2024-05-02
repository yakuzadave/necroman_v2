---
promptId: getChildren
name: Get Childreb
description: uses langchain chain to summarize large chunk of text from childreb
author: Noureddine
tags:
  - writing
version: 0.0.1
mode: insert
chain.type: map_reduce
splitter.chunkSize: 1000
splitter.chunkOverlap: 100
max_tokens: 4000
temperature: 0
chain.maxTokens: 4000
---


```handlebars
{{#script}}
	const linked = await run("necromundaGenTemplates/getChildren", {tg_selection: this.tg_selection});
	const getSum = await run("default/summarizeLarge", {tg_selection: linked});
	return linked;
{{/script}}
```