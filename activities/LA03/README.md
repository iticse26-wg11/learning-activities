---
id: LA03
title: "Unplugged Language Model Simulation"
keywords: ["Language modeling", "n-grams", "token sampling", "training data", "randomness"]
related_ilos: [MM01, EPR02, CS02]
prerequisite_ilos: []
type: "In-class, small groups, unplugged"
setting: ["In-class"]
grouping: ["Small groups"]
mode: Unplugged
duration: "45 minutes"
assessment: "No"
assessed: false
scale: "Two or more small groups, scalable for large classes"
expanded_version: "expanded.md"
---
<!-- Imported from the WG11 report, sections/60-design-activities.tex (Overleaf commit fb8ec81 2026-09-12) by scripts/import-from-report.py. The report is the source of truth: edit it there and re-run the import; hand edits here are overwritten. -->

# Unplugged Language Model Simulation

**Related ILOs** (at the end of the course, students should be able to …)
- [MM01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM01.md): explain how GenAI models generate output using a simplified "next-word prediction" process, recognising that real systems predict tokens and use contextual information from prompts and prior text to determine their responses.
- [EPR02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR02.md): identify data sources used to train GenAI models and describe how training data quality, consent, and representation shape GenAI model behaviors.
- [CS02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS02.md): explain operational GenAI concepts (e.g., tokens, context windows, probability distributions, and non-determinism) and use these concepts to interpret system behavior, output variability, and prompt sensitivity.

**Type:** In-class, small groups, unplugged · **Duration:** 45 minutes · **Scale:** Two or more small groups, scalable for large classes

> Expanded version: [expanded.md](expanded.md)

## Description

To investigate the process by which transformer-based language models produce text, student groups run a small ‘unplugged’ simulation using paper, pencil, and a 6-sided die. Each student group is given a different ‘training dataset’ consisting of approximately one page of text on the same topic (sourced from different internet text genres, representing common training sources for large language models). Using this data, students complete a few rows of a provided n-gram table based on the training dataset. Finally, students run multiple iterations of sampling from the n-gram table using a 6-sided die to provide randomness in next token selections. While all groups are given the same prompt, the differences in training data and randomness will result in significant differences in output. After comparing outputs, students relate specific parts of the simulation to key LLM concepts and discuss how differences in training data lead to differences in outputs.

## Keywords

Language modeling, n-grams, token sampling, training data, randomness

## Prerequisites

- Understanding of basic language model terminology (input, training data, prompt, output)

## Resources

- Pre-printed training dataset n-gram tables, one six-sided die for each group (can replace with random number generator)

## Assessment

No
