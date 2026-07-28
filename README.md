# Capstone Project 5 - Generative AI Applications

## Project title
**Transformer-Based Generation of Public-Sector Contract Language: An ICM Contract Knowledge-Reuse and Risk Demonstrator**

## Objective
This project implements a small custom PyTorch causal Transformer that learns character-level patterns from authentic Federal Acquisition Regulation provisions and clauses. The model generates short controlled continuations for evaluation of coherence, variability, repetition, memorization, hallucination, and responsible-use risks.

The generated text is an academic demonstration only. It is not legal advice, is not authoritative FAR language, and must not be inserted into a solicitation or contract without validation against an official source and qualified human review.

## Dataset
The dataset is a frozen FAC 2026-01 snapshot of FAR Subpart 52.2, effective March 13, 2026. The processed corpus contains 610 usable provisions and clauses after excluding reserved headings and the scope-only section. See `data/DATASET_SOURCE.md` and `data/audit/PHASE_1_DATASET_AUDIT.md`.

## Planned model
- Custom character-level causal Transformer in PyTorch
- Clause-level train/validation/test split before sequence chunking
- Baseline and one controlled comparison
- Temperature and top-k generation evaluation
- Qualitative failure analysis plus lightweight repetition, diversity, and source-overlap diagnostics

## Repository status
- Phase 0: complete
- Phase 1: complete - dataset decision **GO**
- Phase 2: repository skeleton prepared; GitHub and Colab setup pending

## Required submission files
- `generative_model.ipynb`
- `Generative_AI_Analysis_Report.pdf`
- `module_summary.pdf`
- `requirements.txt`
- Dataset or clearly documented source
