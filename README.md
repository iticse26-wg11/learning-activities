# Learning Activities

Learning activities for **generative AI literacy for computing students in higher education**, developed by ITiCSE 2026 Working Group 11. Each activity is mapped to the working group's [intended learning outcomes](../intended-learning-outcomes/) (ILOs).

## Contents

| Path | What it is |
|------|------------|
| [`activities/`](activities/) | One markdown file per activity (`NN-slug.md`), each with YAML frontmatter (id, keywords, related ILOs, type, duration, assessment, scale) followed by the full description, prerequisites, resources and assessment. |
| [`activities/figures/`](activities/figures/) | Figures referenced by activities. |
| [`ilo-coverage.md`](ilo-coverage.md) | Matrix of which activities address which ILOs. |
| [`TEMPLATE.md`](TEMPLATE.md) | Template for adding a new activity. |

## Activities

15 activities. IDs (`LA01`–`LA15`) follow the order in the source document.

| ID | Activity | Related ILOs | Type | Duration |
|----|----------|--------------|------|----------|
| LA01 | [AI History Timeline](activities/01-ai-history-timeline.md) | H01, H02 | In-class, Small groups, Unplugged | 45 minutes |
| LA02 | [Content Detection Limitations](activities/02-content-detection-limitations.md) | EPR07 | In-class, Small groups, Digital | 60–90 minutes |
| LA03 | [Basic LLM Output Evaluation and Fact Checking](activities/03-basic-llm-output-evaluation-and-fact-checking.md) | EPR04 | In-lab, Individual, Digital | 60 minutes |
| LA04 | [AI Application Project](activities/04-ai-application-project.md) | EPR11, EPR13, EPR14, CS07 | In-lab, Individual or Small groups, Digital | 2 hours |
| LA05 | [Designing an Explainable AI System](activities/05-designing-an-explainable-ai-system.md) | MM07 | In-class, Small groups, Unplugged | 60–90 minutes |
| LA06 | [LLM Output-Checking: Inductive Explainability Pipeline](activities/06-llm-output-checking-inductive-explainability-pipeline.md) | MM08, EPR06 | In-class, Small groups, Digital | 60 minutes |
| LA07 | [Unplugged LLM Simulation](activities/07-unplugged-llm-simulation.md) | MM01, EPR02, CS02 | In-class, Small groups, Unplugged | 45 minutes |
| LA08 | [Anatomy of (Another) AI System](activities/08-anatomy-of-another-ai-system.md) | EPR01, EPR09 | In-class, Small groups, Offline | 1 hour |
| LA09 | [AI Alignment Lab](activities/09-ai-alignment-lab.md) | MM03, EPR05 | In-class, Individual or Small groups, Digital | 2 hours (including individual investigation and reflection outside of class) |
| LA10 | [AI Pre/Post Mindmap](activities/10-ai-pre-post-mindmap.md) | MM05 | In-class, Individual and Small groups | ~25 minutes for the first session + ~25 minutes for the second session |
| LA11 | [AI Evaluation Frameworks + Policies](activities/11-ai-evaluation-frameworks-and-policies.md) | EPR10, EPR12 | In-class, Small groups, Unplugged | 90 minutes (45 + 45 for the two parts) |
| LA12 | [Personal AI Use Reflection](activities/12-personal-ai-use-reflection.md) | EPR08 | In-class, Pre-sessional work, Individual and Small groups, Digital | ~20 min at home + ~15–20 min in-class group discussion |
| LA13 | [AI Use Case Analysis and Evaluation](activities/13-ai-use-case-analysis-and-evaluation.md) | MM04, MM06, CS04a, CS04b | In-class, Individual and Small groups, Digital | 20 minutes per use case + 30 minutes for the final discussion |
| LA14 | [Application of AI to Specific Problem](activities/14-application-of-ai-to-specific-problem.md) | CS01, CS03, CS05, CS06 | In-class, Pre-sessional, Individual and Small group, Digital | 60 minutes pre-sessional activity; 90–120 minutes in-classroom activities |
| LA15 | [AI Model Pipeline](activities/15-ai-model-pipeline.md) | MM02, EPR03 | In-class, Individual and Small-group, Unplugged | 45 minutes |

### By ILO area

| Area | Activities |
|------|------------|
| History (H) | LA01 |
| Mental Models (MM) | LA05, LA06, LA07, LA09, LA10, LA13, LA15 |
| Ethics, Policy and Regulations (EPR) | LA02, LA03, LA04, LA06, LA07, LA08, LA09, LA11, LA12, LA15 |
| Computer Science (CS) | LA04, LA07, LA13, LA14 |

### By mode

| Mode | Activities |
|------|------------|
| Unplugged | LA01, LA05, LA07, LA11, LA15 |
| Digital | LA02, LA03, LA04, LA06, LA09, LA12, LA13, LA14 |
| Offline | LA08 |
| Not specified (paper or digital) | LA10 |

### With an assessment component

LA08 (formative), LA11 (evaluation grid submitted), LA14 (formative, artifacts), LA15 (formative, reflections). LA07 optionally extends into a coding exercise.

### With pre-sessional work

LA12, LA14. LA10 spans two sessions (start and end of course).

## Activity format

Each activity file follows the structure of the source document:

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

- **Activity IDs (`LA01`–`LA15`) are not in the source** — they were assigned here for cross-referencing.
- **Missing expanded-version links.** LA05 (*Designing an Explainable AI System*), LA07 (*Unplugged LLM Simulation*) and LA12 (*Personal AI Use Reflection*) have an "Expanded version is here:" placeholder with no link. Only LA01 has a working link (a Google Doc).
- **LA05 figure** — the example decision tree on p.5 is reproduced as a Mermaid diagram and kept as a PNG in `activities/figures/`.
- **LA10 has no mode** (Unplugged/Digital) in its "Type of activity"; the description allows paper or a tool such as Miro.
- **LA13 duration** read "30 minutes ai use for the final discussion" in the source; rendered as "30 minutes for the final discussion".
- **LA13 and LA14 list ILOs as prerequisites** (MM01, MM02, EPR05, CS02 and CS01, CS02, CS03 respectively); these are recorded in `prerequisite_ilos`.
- **LA06** — "provides examples.link to examples of such system/frameworks/models" tidied to "provides examples of (or links to) such systems/frameworks/models".
- **LA12** — a garbled sentence about the whole-class discussion was tidied ("Once the group discussions finish, the whole class discusses: common patterns are collected, …").
- **Assessment field** is inconsistent in the source (mostly "No"; LA08/LA14/LA15 "Formative"; LA11 requires a submitted grid).
- The source's "Type of activity" vocabulary is inconsistent ("In-class"/"In-lab", "Small groups"/"Small group"/"Small-group", "Unplugged"/"Offline"); the structured `setting`/`grouping`/`mode` fields normalise these while `type` keeps the original.
