---
id: LA09
title: "AI Alignment Lab"
keywords: ["AI alignment", "AI jailbreaks", "model safety", "misuse prevention", "Python lab"]
related_ilos: [MM03, EPR05]
prerequisite_ilos: []
type: "In-class, individual or small groups, digital"
setting: ["In-class"]
grouping: ["Individual", "Small groups"]
mode: Digital
duration: "2 hours (including individual investigation and reflection outside of class)"
assessment: "No"
assessed: false
scale: "Individual assignment, or one or more small groups"
expanded_version: null
---
<!-- Imported from the WG11 report, sections/60-design-activities.tex (Overleaf commit bf239f6 2026-09-14) by scripts/import-from-report.py. The report is the source of truth: edit it there and re-run the import; hand edits here are overwritten. -->

# AI Alignment Lab

**Related ILOs** (at the end of the course, students should be able to …)
- [MM03](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/MM03.md): evaluate technical, ethical and practical limitations of GenAI systems (e.g., hallucinations, computational cost, context window, lack of true understanding, biases, …).
- [EPR05](https://github.com/iticse26-wg11/intended-learning-outcomes/blob/main/ilos/EPR05.md): recognize limitations of GenAI model outputs, including hallucination, misinformation, privacy leakage, harmful content, in the context of societal impacts.

**Type:** In-class, individual or small groups, digital · **Duration:** 2 hours (including individual investigation and reflection outside of class) · **Scale:** Individual assignment, or one or more small groups

## Description

The AI alignment lab [(Weichert, 2026)](https://dl.acm.org/doi/10.1145/3803401.3811967) is an exploratory, hands-on Python notebook in which students are challenged to jailbreak and then align a small-scale open-source large language model. Through the lab, students discover gaps and difficulties in AI alignment by circumventing basic alignment behavior, like the avoidance of offensive language in LLM outputs. Students then change roles to consider what it takes to (robustly) align AI models in the face of myriad forms of misuse, building an understanding of AI alignment as a multifaceted challenge requiring both technical approaches and collaborative governance of AI applications. The lab also provides an opportunity for students to identify how particular limitations in generative AI model outputs result from particular mechanisms in these models (e.g., inherent output stochasticity) or stages in a larger AI pipeline (e.g., failure to accurately summarize information retrieved through retrieval-augmented generation).

## Keywords

AI alignment, AI jailbreaks, model safety, misuse prevention, Python lab

## Prerequisites

- Conceptual understanding of the LLM text generation process (e.g., after “Unplugged Language Model Simulation” activity), introductory-level Python ability, access to hosted Python notebook runtime (e.g., Google Colab) and `transformers` Python module

## Resources

- Python notebook lab file ([link](https://colab.research.google.com/drive/1Ohl5zZ58EXg3pfuh2omPJArixupYExa3)) (with a Python notebook application like Google Colab with sufficient memory to download the 7B-parameter LLM)

## Assessment

No

## References

- Weichert, James (2026). *Exploring the AI Principles-to-Practices Gap with an Interactive AI Alignment Lab*. Proceedings of the 31st ACM Conference on Innovation and Technology in Computer Science Education V. 2. <https://dl.acm.org/doi/10.1145/3803401.3811967>
