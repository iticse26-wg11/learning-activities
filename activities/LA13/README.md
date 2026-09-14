---
id: LA13
title: "Application of AI to a Specific Problem: Problem Decomposition, Model Selection, Output Evaluation"
keywords: ["Problem decomposition", "model selection", "human oversight", "data privacy", "task allocation"]
related_ilos: [CS01, CS03, CS05, CS06]
prerequisite_ilos: [CS02]
type: "In-class, pre-sessional, individual or small group, digital"
setting: ["In-class", "Pre-sessional"]
grouping: ["Individual", "Small groups"]
mode: Digital
duration: "3 hours of in-class activities (Suggestion: implement phase 1 in the same class session (2 hours) and phase 2 in the following one (1 hour)."
assessment: "Formative assessment based on group artifact submissions and individual work"
assessed: true
scale: "Two or more small groups, scalable to large classes"
expanded_version: null
---
<!-- Imported from the WG11 report, sections/60-design-activities.tex (Overleaf commit bf239f6 2026-09-14) by scripts/import-from-report.py. The report is the source of truth: edit it there and re-run the import; hand edits here are overwritten. -->

# Application of AI to a Specific Problem: Problem Decomposition, Model Selection, Output Evaluation

**Related ILOs** (at the end of the course, students should be able to …)
- [CS01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS01.md): distinguish between different types of GenAI systems (e.g., web-based chatbots, coding assistants, local vs cloud-hosted models) and apply this knowledge to select an appropriate system for a given context.
- [CS03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS03.md): compare open-source and proprietary GenAI models and identify their main advantages and disadvantages for a given context, for example in terms of data privacy.
- [CS05](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS05.md): deconstruct (decompose) problems and determine appropriate subtasks to be undertaken by humans or GenAI systems.
- [CS06](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS06.md): distinguish between different levels of human oversight and automation in GenAI-supported development workflows (e.g., AI-assisted, agentic, or highly automated workflows) and select an appropriate workflow for a given scenario.

**Prerequisite ILOs** (assumed before this activity)
- [CS02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS02.md): explain operational GenAI concepts (e.g., tokens, context windows, probability distributions, and non-determinism) and use these concepts to interpret system behavior, output variability, and prompt sensitivity.

**Type:** In-class, pre-sessional, individual or small group, digital · **Duration:** 3 hours of in-class activities (Suggestion: implement phase 1 in the same class session (2 hours) and phase 2 in the following one (1 hour). · **Scale:** Two or more small groups, scalable to large classes

## Description

This multi-task activity covers several design and implementation decisions. The activity has two phases: a) tasks 1-3 and b) tasks 4-5.

*Task 1: In-class individual reflection (suggested time: 45 minutes, but instructor can adjust according to the complexity of the assigned task/scenario)*. Students individually use at least two different GenAI systems (e.g., a local, small model vs. a large, proprietary model) with the same prompt related to the assigned scenario, such as generating an outline for a university course management system. They compare the outputs and document differences in quality, accuracy, usefulness, and, where relevant, considerations such as data privacy, deployment model, and whether the systems are open-source or proprietary.

*Task 2: In-class small group discussion (45 minutes).* Students work in small groups on the same scenario, focusing on its technical and system-related aspects. They identify the system’s main requirements, share and discuss their pre-sessional findings, and compare GenAI systems that could support the design and implementation tasks. They use their task 1 observations to inform their discussion of which GenAI systems may be most suitable for different design and implementation tasks. Students then justify their preferred GenAI system or systems and break the scenario into manageable subtasks, such as designing a database schema or system architecture. Instructors can provide a template for summarizing the outcome of the activity, for example, including the prompt used, GenAI tool comparison criteria and results, and identified subtasks.

*Task 3: Full class discussion (30 minutes).* Instructors moderate a discussion where each group presents the main outcomes of the activity. After reflecting, the class agrees on a shared list of subtasks to consider in the second phase of the activity (tasks 4–5).

*Task 4: In-class small group discussion (30 minutes); groups can be the same as in task 2, or instructors can decide to mix.* For each subtask identified in task 3, groups decide whether it should be completed by humans, supported by GenAI, led by GenAI with human review, or largely automated. Using a template provided by the instructors (e.g., a table to be completed for each subtask), students report their decisions.

*Task 5: Full class discussion (30 minutes)* Students present and discuss their decisions, focusing on task allocation, appropriate level of human oversight, and data privacy aspects. Instructors propose reflection questions, such as: "How much can we delegate to AI?", "What are the most critical subtasks?", "Do you see risks related to data privacy?"

## Keywords

Problem decomposition, model selection, human oversight, data privacy, task allocation

## Prerequisites

- Learning objectives [CS01](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS01.md), [CS02](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS02.md), [CS03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/CS03.md), practical knowledge of GenAI models, prompting, and tools

## Resources

- Scenario description and reflection questions, support documentation for model and tool selection, access to at least two LLMs

## Assessment

Formative assessment based on group artifact submissions and individual work
