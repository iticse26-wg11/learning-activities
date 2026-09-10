# Learning Activities

Learning activities for **generative AI literacy for computing students in higher education**, developed by ITiCSE 2026 Working Group 11. Each activity is mapped to the working group's [intended learning outcomes](../intended-learning-outcomes/) (ILOs).

## Contents

| Path | What it is |
|------|------------|
| [`activities/`](activities/) | One directory per activity, named by its id (`activities/LA01/README.md`), with YAML frontmatter (id, keywords, related ILOs, type, duration, assessment, scale) followed by the full description, prerequisites, resources and assessment. Figures and expanded materials live alongside (`activities/LA08/figures/`). |
| [`scripts/build-index.py`](scripts/build-index.py) | Regenerates the tables below and `ilo-coverage.md` from the frontmatter; `--check` validates ids. |
| [`ilo-coverage.md`](ilo-coverage.md) | Matrix of which activities address which ILOs (generated). |
| [`TEMPLATE.md`](TEMPLATE.md) | Template for adding a new activity. |

## Activities

<!-- BEGIN GENERATED -->
15 activities. IDs (`LA01`–`LA15`) follow the presentation order of the working-group report and are permanent: never renumbered or reused.

| ID | Activity | Related ILOs | Type | Duration |
|----|----------|--------------|------|----------|
| LA01 | [AI Mindmap](activities/LA01/README.md) | MM05 | In-class, Individual and Small groups | ~25 minutes for the first session + ~25 minutes for the second session |
| LA02 | [AI History Timeline](activities/LA02/README.md) | H01, H02 | In-class, Small groups, Unplugged | 45 minutes |
| LA03 | [Unplugged Language Model Simulation](activities/LA03/README.md) | MM01, EPR02, CS02 | In-class, Small groups, Unplugged | 45 minutes |
| LA04 | [Anatomy of (Another) AI System](activities/LA04/README.md) | EPR01, EPR09 | In-class, Small groups, Offline | 1 hour |
| LA05 | [AI Model Pipeline](activities/LA05/README.md) | MM02, EPR03 | In-class, Individual and Small-group, Unplugged | 45 minutes |
| LA06 | [LLM Output Evaluation and Fact-Checking](activities/LA06/README.md) | EPR04 | In-lab, Individual, Digital | 60 minutes |
| LA07 | [Inductive LLM Explainability Pipeline](activities/LA07/README.md) | MM08, EPR06 | In-class, Small groups, Digital | 60 minutes |
| LA08 | [Designing an Explainable AI System](activities/LA08/README.md) | MM07 | In-class, Small groups, Unplugged | 60–90 minutes |
| LA09 | [AI Alignment Lab](activities/LA09/README.md) | MM03, EPR05 | In-class, Individual or Small groups, Digital | 2 hours (including individual investigation and reflection outside of class) |
| LA10 | [AI Use Case Analysis and Evaluation](activities/LA10/README.md) | MM04, MM06, CS04a, CS04b | In-class, Individual and Small groups, Digital | 20 minutes per use case + 30 minutes for the final discussion |
| LA11 | [Content Detection Limitations](activities/LA11/README.md) | EPR07 | In-class, Small groups, Digital | 60–90 minutes |
| LA12 | [AI Evaluation Frameworks and Policies](activities/LA12/README.md) | EPR10, EPR12 | In-class, Small groups, Unplugged | 90 minutes (45 + 45 for the two parts) |
| LA13 | [Application of AI to Specific Problem: Problem Decomposition, Model Selection, Output Evaluation](activities/LA13/README.md) | CS01, CS03, CS05, CS06 | In-class, Pre-sessional, Individual and Small group, Digital | 60 minutes pre-sessional activity; 90–120 minutes in-classroom activities |
| LA14 | [Personal AI Use Reflection](activities/LA14/README.md) | EPR08 | In-class, Pre-sessional work, Individual and Small groups, Digital | ~20 min at home + ~15–20 min in-class group discussion |
| LA15 | [AI Application Project](activities/LA15/README.md) | EPR11, EPR13, EPR14, CS07 | In-lab, Individual or Small groups, Digital | 2 hours |

### By ILO area

| Area | Activities |
|------|------------|
| History (H) | LA02 |
| Mental Models (MM) | LA01, LA03, LA05, LA07, LA08, LA09, LA10 |
| Ethics, Policy and Regulations (EPR) | LA03, LA04, LA05, LA06, LA07, LA09, LA11, LA12, LA14, LA15 |
| Computer Science (CS) | LA03, LA10, LA13, LA15 |

### By mode

| Mode | Activities |
|------|------------|
| Unplugged | LA02, LA03, LA05, LA08, LA12 |
| Digital | LA06, LA07, LA09, LA10, LA11, LA13, LA14, LA15 |
| Offline | LA04 |
| Not specified (paper or digital) | LA01 |
<!-- END GENERATED -->

### With an assessment component

LA04 (formative), LA12 (evaluation grid submitted), LA13 (formative, artifacts), LA05 (formative, reflections). LA03 optionally extends into a coding exercise.

### With pre-sessional work

LA14, LA13. LA01 spans two sessions (start and end of course).

## Identifiers and links

- **Ids are permanent.** `LA01`–`LA15` follow the presentation order of the working-group report. An id is never renumbered or reused; a new activity takes the next free number, a retired one keeps its id and gains `status: retired` in its frontmatter.
- **Links use only the id.** The stable URL for an activity is  
  `https://github.com/iticse26-wg11/learning-activities/blob/main/activities/<ID>/README.md`  
  (e.g. [LA03](activities/LA03/README.md)). Titles may change; paths do not.
- After editing frontmatter run `scripts/build-index.py` to refresh this README and `ilo-coverage.md`.

## Activity format

Each `activities/<ID>/README.md` follows the structure of the source document:

```yaml
---
id: LA##
title: …
keywords: [ … ]
related_ilos: [ … ]        # ILO ids from ../intended-learning-outcomes/ilos.yaml
prerequisite_ilos: [ … ]   # optional: ILOs assumed before the activity
type: "…"                  # original "Type of activity" string from the source
setting: [ In-class | In-lab | Pre-sessional ]
grouping: [ Individual | Small groups ]
mode: Unplugged | Digital | Offline | null
duration: "…"
assessment: "…"
scale: "…"
expanded_version: url | null
---
```

`setting`, `grouping` and `mode` are a structured split of the source's free-text "Type of activity" field, to allow filtering; `type` preserves the original.

## Source and extraction notes

Extracted from `wg11-activities.pdf` (*Final Set of Activities (To Review) #2*, 14 pages). Descriptions are reproduced faithfully; only light copy-editing was applied (punctuation, spacing, obvious typos, and converting run-on task lists into bullets/bold labels). Items to note:

- **Activity IDs (`LA01`–`LA15`) are not in the source** — they were assigned here for cross-referencing and follow the order of the working-group report (renumbered 2026-09-10 from the source-document order). Titles follow the report where it differs from the source.
- **Missing expanded-version links.** LA08 (*Designing an Explainable AI System*), LA03 (*Unplugged LLM Simulation*) and LA14 (*Personal AI Use Reflection*) have an "Expanded version is here:" placeholder with no link. Only LA02 has a working link (a Google Doc).
- **LA08 figure** — the example decision tree on p.5 is reproduced as a Mermaid diagram and kept as a PNG in `activities/LA08/figures/`.
- **LA01 has no mode** (Unplugged/Digital) in its "Type of activity"; the description allows paper or a tool such as Miro.
- **LA10 duration** read "30 minutes ai use for the final discussion" in the source; rendered as "30 minutes for the final discussion".
- **LA10 and LA13 list ILOs as prerequisites** (MM01, MM02, EPR05, CS02 and CS01, CS02, CS03 respectively); these are recorded in `prerequisite_ilos`.
- **LA07** — "provides examples.link to examples of such system/frameworks/models" tidied to "provides examples of (or links to) such systems/frameworks/models".
- **LA14** — a garbled sentence about the whole-class discussion was tidied ("Once the group discussions finish, the whole class discusses: common patterns are collected, …").
- **Assessment field** is inconsistent in the source (mostly "No"; LA04/LA13/LA05 "Formative"; LA12 requires a submitted grid).
- The source's "Type of activity" vocabulary is inconsistent ("In-class"/"In-lab", "Small groups"/"Small group"/"Small-group", "Unplugged"/"Offline"); the structured `setting`/`grouping`/`mode` fields normalise these while `type` keeps the original.
