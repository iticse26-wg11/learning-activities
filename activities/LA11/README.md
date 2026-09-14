---
id: LA11
title: "Content Detection Limitations"
keywords: ["Output evaluation", "hallucination detection", "adversarial prompting", "evaluation criteria", "scope compliance"]
related_ilos: [EPR07]
prerequisite_ilos: []
type: "In-class, small groups, digital"
setting: ["In-class"]
grouping: ["Small groups"]
mode: Digital
duration: "60-90 minutes"
assessment: "No"
assessed: false
scale: "Two or more small groups"
expanded_version: "expanded.md"
---
<!-- Imported from the WG11 report, sections/60-design-activities.tex (Overleaf commit bf239f6 2026-09-14) by scripts/import-from-report.py. The report is the source of truth: edit it there and re-run the import; hand edits here are overwritten. -->

# Content Detection Limitations

**Related ILOs** (at the end of the course, students should be able to …)
- [EPR07](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR07.md): identify tools and procedures for evaluating and verifying model outputs, and apply these to assess AI-generated content.

**Type:** In-class, small groups, digital · **Duration:** 60-90 minutes · **Scale:** Two or more small groups

> Expanded version: [expanded.md](expanded.md)

## Description

This activity helps students evaluate and verify AI model outputs, identify content generation limitations, and apply systematic procedures to detect errors or hallucinations. This activity consists of two parts. Part 1 defines the evaluation procedure (e.g., a checklist to verify the GenAI system's output), and part 2 applies these procedures to assess AI-generated content.

*Phase 1.* To start this activity, the entire class is given one scenario to develop an evaluation procedure. An example scenario the instructor could provide to students is: *Imagine your group has been tasked with building an AI chatbot to answer visitor questions at a zoo. To keep visitors safe and informed, the AI has one job and strict rules. The AI must answer visitor questions accurately using only the official Zoo Fact Book. The strict rules are that the AI chatbot must not make up facts (hallucinate), give off-topic advice, or encourage dangerous behavior.*

Next, students are divided into groups, and each group writes a checklist or procedure to verify the AI system's output based on the given scenario. Using the AI zoo chatbot example above, the checklist should include tests evaluating if the AI system stayed inside the boundaries (e.g., the zoo factbook for the examples above) or if the AI system hallucinated.

The students are provided with guidance on developing the evaluation procedure. This should include test questions or prompts for the AI system, together with clear criteria for judging the responses, preferably using binary “Pass/Fail” results where appropriate. The questions should test accuracy, scope, and safety, including cases that are answerable from the provided knowledge base as well as questions that are off-topic, unsafe, based on false premises, or cannot be answered from the available information.

Next, groups are encouraged to test their evaluation procedures and modify the evaluation criteria where relevant.

*Phase 2* For the second phase of the activity, each group swaps its evaluation procedure with another group. Using the swapped procedure, groups test the same GenAI system and scenario and evaluate the outputs it produces. They are also encouraged to use adversarial approaches, such as edge cases, trick questions, or deceptive prompts, to test whether the system can be pushed beyond the boundaries defined in the original scenario.

The entire class is regrouped to discuss their experience of evaluating model output, with the lecturer providing clear guidance on best practice and tools.

## Keywords

Output evaluation, hallucination detection, adversarial prompting, evaluation criteria, scope compliance

## Prerequisites

- Defined scenario, initial GenAI prompt/custom GPT and knowledge base (e.g., Zoo Fact Book)

## Resources

- Flipcharts, computers, pens

## Assessment

No
