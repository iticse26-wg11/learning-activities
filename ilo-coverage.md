# ILO coverage

Which learning activities address which intended learning outcomes. Generated from the `related_ilos` field of each activity's frontmatter; ILO ids come from [`../intended-learning-outcomes/ilos.yaml`](../intended-learning-outcomes/ilos.yaml).

**Summary:** all 32 ILOs are covered; each ILO is currently addressed by exactly one activity. No activity is unmapped.

## ILO → activities

| ILO | Activities |
|-----|------------|
| H01 | [LA01](activities/01-ai-history-timeline.md) |
| H02 | [LA01](activities/01-ai-history-timeline.md) |
| MM01 | [LA07](activities/07-unplugged-llm-simulation.md) |
| MM02 | [LA15](activities/15-ai-model-pipeline.md) |
| MM03 | [LA09](activities/09-ai-alignment-lab.md) |
| MM04 | [LA13](activities/13-ai-use-case-analysis-and-evaluation.md) |
| MM05 | [LA10](activities/10-ai-pre-post-mindmap.md) |
| MM06 | [LA13](activities/13-ai-use-case-analysis-and-evaluation.md) |
| MM07 | [LA05](activities/05-designing-an-explainable-ai-system.md) |
| MM08 | [LA06](activities/06-llm-output-checking-inductive-explainability-pipeline.md) |
| EPR01 | [LA08](activities/08-anatomy-of-another-ai-system.md) |
| EPR02 | [LA07](activities/07-unplugged-llm-simulation.md) |
| EPR03 | [LA15](activities/15-ai-model-pipeline.md) |
| EPR04 | [LA03](activities/03-basic-llm-output-evaluation-and-fact-checking.md) |
| EPR05 | [LA09](activities/09-ai-alignment-lab.md) |
| EPR06 | [LA06](activities/06-llm-output-checking-inductive-explainability-pipeline.md) |
| EPR07 | [LA02](activities/02-content-detection-limitations.md) |
| EPR08 | [LA12](activities/12-personal-ai-use-reflection.md) |
| EPR09 | [LA08](activities/08-anatomy-of-another-ai-system.md) |
| EPR10 | [LA11](activities/11-ai-evaluation-frameworks-and-policies.md) |
| EPR11 | [LA04](activities/04-ai-application-project.md) |
| EPR12 | [LA11](activities/11-ai-evaluation-frameworks-and-policies.md) |
| EPR13 | [LA04](activities/04-ai-application-project.md) |
| EPR14 | [LA04](activities/04-ai-application-project.md) |
| CS01 | [LA14](activities/14-application-of-ai-to-specific-problem.md) |
| CS02 | [LA07](activities/07-unplugged-llm-simulation.md) |
| CS03 | [LA14](activities/14-application-of-ai-to-specific-problem.md) |
| CS04a | [LA13](activities/13-ai-use-case-analysis-and-evaluation.md) |
| CS04b | [LA13](activities/13-ai-use-case-analysis-and-evaluation.md) |
| CS05 | [LA14](activities/14-application-of-ai-to-specific-problem.md) |
| CS06 | [LA14](activities/14-application-of-ai-to-specific-problem.md) |
| CS07 | [LA04](activities/04-ai-application-project.md) |

## Activity → ILOs

| Activity | Related ILOs | Prerequisite ILOs |
|----------|--------------|-------------------|
| LA01 AI History Timeline | H01, H02 | — |
| LA02 Content Detection Limitations | EPR07 | — |
| LA03 Basic LLM Output Evaluation and Fact Checking | EPR04 | — |
| LA04 AI Application Project | EPR11, EPR13, EPR14, CS07 | — |
| LA05 Designing an Explainable AI System | MM07 | — |
| LA06 LLM Output-Checking: Inductive Explainability Pipeline | MM08, EPR06 | — |
| LA07 Unplugged LLM Simulation | MM01, EPR02, CS02 | — |
| LA08 Anatomy of (Another) AI System | EPR01, EPR09 | — |
| LA09 AI Alignment Lab | MM03, EPR05 | (LA07 recommended) |
| LA10 AI Pre/Post Mindmap | MM05 | — |
| LA11 AI Evaluation Frameworks + Policies | EPR10, EPR12 | — |
| LA12 Personal AI Use Reflection | EPR08 | — |
| LA13 AI Use Case Analysis and Evaluation | MM04, MM06, CS04a, CS04b | MM01, MM02, EPR05, CS02 |
| LA14 Application of AI to Specific Problem | CS01, CS03, CS05, CS06 | CS01, CS02, CS03 |
| LA15 AI Model Pipeline | MM02, EPR03 | (CS02 familiarity) |

## Observations

- Every ILO has exactly one activity, so there is no redundancy but also no choice: dropping any activity leaves its ILOs uncovered.
- Activities that carry the most ILOs: LA04 and LA14 (4 each), LA13 (4, counting CS04a/b), LA07 (3).
- Implied sequencing from prerequisites: LA07 → LA09; (LA07, LA15) → LA13; LA14 assumes CS01–CS03 (partly covered by LA14 itself and LA07).
