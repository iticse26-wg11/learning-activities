# Learning Activities

Learning activities for **generative AI literacy for computing students in higher education**, developed by ITiCSE 2026 Working Group 11. Each activity is mapped to the working group's [intended learning outcomes](https://github.com/iticse26-wg11/intended-learning-outcomes) (ILOs).

## Contents

| Path | What it is |
|------|------------|
| [`activities/`](activities/) | One directory per activity, named by its id (`activities/LA01/README.md`), with YAML frontmatter (id, keywords, related ILOs, type, duration, assessment, scale) followed by the full description, prerequisites, resources and assessment. Expanded versions (`expanded.md`) and figures live alongside. |
| [`scripts/import-from-report.py`](scripts/import-from-report.py) | Imports every activity from the working-group report (the source of truth); `--check` reports drift. |
| [`scripts/build-index.py`](scripts/build-index.py) | Regenerates the tables below and `ilo-coverage.md` from the frontmatter; `--check` validates ids. |
| [`ilo-coverage.md`](ilo-coverage.md) | Matrix of which activities address which ILOs (generated). |
| [`TEMPLATE.md`](TEMPLATE.md) | Template for adding a new activity. |

## Activities

<!-- BEGIN GENERATED -->
15 activities. IDs (`LA01`–`LA15`) follow the presentation order of the working-group report and are permanent: never renumbered or reused. ILO ids link to their stable pages in [`intended-learning-outcomes`](https://github.com/iticse26-wg11/intended-learning-outcomes).

| ID | Activity | Related ILOs | Type | Duration |
|----|----------|--------------|------|----------|
| LA01 | [AI Mindmap](activities/LA01/README.md) | [MM05](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM05.md) | In-class, individual and small groups | 50 minutes |
| LA02 | [AI History Timeline](activities/LA02/README.md) | [H01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/H01.md), [H02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/H02.md) | In-class, small groups, unplugged | 45 minutes |
| LA03 | [Unplugged Language Model Simulation](activities/LA03/README.md) | [MM01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM01.md), [EPR02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR02.md), [CS02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS02.md) | In-class, small groups, unplugged | 45 minutes |
| LA04 | [Anatomy of (Another) AI System](activities/LA04/README.md) | [EPR01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR01.md), [EPR09](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR09.md) | In-class, small groups, offline | 60 minutes |
| LA05 | [AI Model Pipeline](activities/LA05/README.md) | [MM02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM02.md), [EPR03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR03.md) | In-class, individual and small groups, unplugged | 45 minutes |
| LA06 | [LLM Output Evaluation and Fact-Checking](activities/LA06/README.md) | [EPR04](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR04.md) | In-class, individual, digital | 60 minutes |
| LA07 | [Inductive LLM Explainability Pipeline](activities/LA07/README.md) | [MM08](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM08.md), [EPR06](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR06.md) | In-class, small groups, digital | 1 hour |
| LA08 | [Designing an Explainable AI System](activities/LA08/README.md) | [MM07](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM07.md) | In-class, small groups, unplugged | 80-120 minutes |
| LA09 | [AI Alignment Lab](activities/LA09/README.md) | [MM03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM03.md), [EPR05](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR05.md) | In-class, individual or small groups, digital | 2 hours (including individual investigation and reflection outside of class) |
| LA10 | [AI Use Case Analysis and Evaluation](activities/LA10/README.md) | [MM04](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM04.md), [MM06](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM06.md), [CS04a](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS04a.md), [CS04b](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS04b.md) | In-class, individual or small groups, digital | 75 minutes total. 20 minutes for individual work on one use case + 20 minutes for within-group sharing + 30 minutes for the final discussion, perhaps between groups |
| LA11 | [Content Detection Limitations](activities/LA11/README.md) | [EPR07](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR07.md) | In-class, small groups, digital | 60-90 minutes |
| LA12 | [AI Evaluation Frameworks and Policies](activities/LA12/README.md) | [EPR10](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR10.md), [EPR12](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR12.md) | In-class, small groups, unplugged | 90 minutes (45 + 45 for the two phases) |
| LA13 | [Application of AI to a Specific Problem: Problem Decomposition, Model Selection, Output Evaluation](activities/LA13/README.md) | [CS01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS01.md), [CS03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS03.md), [CS05](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS05.md), [CS06](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS06.md) | In-class, pre-sessional, individual or small group, digital | 3 hours of in-class activities (Suggestion: implement phase 1 in the same class session (2 hours) and phase 2 in the following one (1 hour). |
| LA14 | [Personal AI Use Reflection](activities/LA14/README.md) | [EPR08](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR08.md) | In-class, pre-sessional, individual or small group, digital | 45 minutes |
| LA15 | [AI Application Project](activities/LA15/README.md) | [EPR11](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR11.md), [EPR13](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR13.md), [EPR14](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR14.md), [CS07](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS07.md) | In-class, individual or small group, digital | 2 hours |

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

### With an assessment component

| Activity | Assessment |
|----------|------------|
| [LA04](activities/LA04/README.md) Anatomy of (Another) AI System | Formative assessment evaluating depth and specificity of group’s research, and group’s ability to connect findings to each other and earlier class discussions/readings |
| [LA05](activities/LA05/README.md) AI Model Pipeline | Formative assessment based on reflections and observations |
| [LA12](activities/LA12/README.md) AI Evaluation Frameworks and Policies | Each group submits its completed evaluation grid, including its definitions and its evaluation using the AI policy. |
| [LA13](activities/LA13/README.md) Application of AI to a Specific Problem: Problem Decomposition, Model Selection, Output Evaluation | Formative assessment based on group artifact submissions and individual work |

### With pre-sessional work

LA13, LA14

### With an expanded version

- [LA02](activities/LA02/README.md) AI History Timeline: [expanded.md](activities/LA02/expanded.md)
- [LA03](activities/LA03/README.md) Unplugged Language Model Simulation: [expanded.md](activities/LA03/expanded.md)
- [LA08](activities/LA08/README.md) Designing an Explainable AI System: [expanded.md](activities/LA08/expanded.md)
- [LA14](activities/LA14/README.md) Personal AI Use Reflection: [expanded.md](activities/LA14/expanded.md)
<!-- END GENERATED -->

## Source of truth and syncing

The activity texts are **maintained in the working-group report** (Overleaf, `sections/60-design-activities.tex`) and imported here; the report is the gold standard and this repository is its stable, linkable mirror. Do not hand-edit `activities/<ID>/README.md`: the next import overwrites it. To sync after the report changes:

```sh
git -C ../report pull                     # the Overleaf clone, checked out next to this repo
scripts/import-from-report.py             # rewrites activities/<ID>/README.md from the report
scripts/build-index.py                    # refreshes the tables above and ilo-coverage.md
scripts/import-from-report.py --check && scripts/build-index.py --check
```

Each imported README carries a comment naming the Overleaf commit it came from. The importer prints a warning for anything it strips or cannot convert (editorial `\hl{}` notes, unknown LaTeX commands, text left after an activity box), so extend `scripts/import-from-report.py` when the report grows a new construct.

Only two frontmatter keys are owned by this repository and survive an import: `expanded_version` and `status`. Everything else, including `prerequisite_ilos` (ILO ids found in the report's *Prerequisites* text) and `assessed` (false when *Assessment* is "No"), is derived from the report.

**Expanded versions.** The report's appendices hold the expanded versions of four activities; they are ported by hand into `activities/<ID>/expanded.md` (LA02, LA03, LA08, LA14), each stamped with the Overleaf state it came from, with figures under `activities/<ID>/figures/`. Materials that are not in the report (worksheets, notebooks, templates) can go in `activities/<ID>/materials/`.

## Identifiers and links

- **Ids are permanent.** `LA01`–`LA15` follow the presentation order of the working-group report. An id is never renumbered or reused; a new activity takes the next free number, a retired one keeps its id and gains `status: retired` in its frontmatter.
- **Links use only the id.** The stable URL for an activity is  
  `https://github.com/iticse26-wg11/learning-activities/blob/main/activities/<ID>/README.md`  
  (e.g. [LA03](activities/LA03/README.md)). Titles may change; paths do not.
- Old-to-new id mapping from the 2026-09-10 renumbering (source-document order → report order), in case anyone holds old references: LA01←LA10, LA02←LA01, LA03←LA07, LA04←LA08, LA05←LA15, LA06←LA03, LA07←LA06, LA08←LA05, LA09←LA09, LA10←LA13, LA11←LA02, LA12←LA11, LA13←LA14, LA14←LA12, LA15←LA04.

## Activity format

Each `activities/<ID>/README.md` has YAML frontmatter followed by the report's description and box fields as Markdown sections (Description, Keywords, Prerequisites, Resources, Assessment, and References when the report cites something):

```yaml
---
id: LA##
title: "…"
keywords: ["…"]
related_ilos: [ … ]        # ILO ids from ../intended-learning-outcomes/ilos.yaml
prerequisite_ilos: [ … ]   # ILO ids named in the report's Prerequisites field
type: "…"                  # the report's "Type of activity" string
setting: [ In-class | In-lab | Pre-sessional ]   # derived from type
grouping: [ Individual | Small groups ]          # derived from type
mode: Unplugged | Digital | Offline | null       # derived from type
duration: "…"
assessment: "…"
assessed: true | false     # derived from assessment
scale: "…"
expanded_version: "expanded.md" | url | null     # repo-owned
status: retired            # repo-owned, optional
---
```

`setting`, `grouping` and `mode` are a structured split of the free-text "Type of activity" field, to allow filtering; `type` preserves the original.

## History

- 2026-09-12: content re-imported from the report (post-focus-group revisions by the activity authors) with `scripts/import-from-report.py`; the four report appendices ported as `expanded.md`.
- 2026-09-10: renumbered to report order, id-only paths, generated index and ILO links.
- 2026-08: first extraction from `wg11-activities.pdf` (*Final Set of Activities (To Review) #2*).
