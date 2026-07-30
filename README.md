# Capstone Project 5 — Generative AI Applications

## Transformer-Based Generation of Public-Sector Contract Language

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/icmsol/capstone-project-5-generative-ai-applications/blob/main/generative_model.ipynb)

This project develops and evaluates a small custom character-level causal Transformer in PyTorch using official Federal Acquisition Regulation (FAR) Subpart 52.2 provisions and clauses. The purpose is to study generative-model behavior, controlled model selection, decoding tradeoffs, reproducibility, and responsible-use risks in a public-sector procurement context.

The generated text is experimental. It is not legally valid contract language and is not approved for legal, procurement, compliance, or operational use.

## Project Objectives

The project was designed to:

1. Acquire and validate an authoritative public-sector contract-language corpus.
2. Preserve complete clauses during training, validation, and test partitioning.
3. Build a causal Transformer directly in PyTorch rather than relying on a pretrained language model.
4. Conduct a controlled model comparison in which dropout is the only changed architectural setting.
5. Select the final model using validation performance without examining the held-out test partition.
6. Evaluate the selected model quantitatively on untouched test data.
7. Compare deterministic and stochastic decoding strategies under controlled prompts and random seeds.
8. Document limitations, hallucination risks, and required responsible-use controls.

## Dataset

The frozen project corpus was derived from the official Acquisition.gov FAR publication associated with Federal Acquisition Circular 2026-01. The source is publicly available, non-synthetic, appropriate for academic use, and was not reused from any earlier capstone project.

After source-boundary validation and removal of material belonging to Subpart 52.3, the final dataset contained:

| Measure | Value |
|---|---:|
| Complete FAR provisions and clauses | 610 |
| Record-text characters | 2,207,308 |
| Model-corpus characters | 2,214,359 |
| Record-text word-like tokens | 342,400 |
| Model-corpus word-like tokens | 343,620 |
| Unique word-like tokens | 8,513 |
| Empty records | 0 |
| Duplicate clause numbers | 0 |
| Duplicate text records | 0 |
| Subpart 52.3 spillover records | 0 |

The model corpus prepends each complete record with its clause number so that clause identifiers remain part of the learned character sequence.

## Data Partitioning and Preprocessing

Records were divided at the complete-clause level to prevent the same clause from appearing in more than one partition.

| Partition | Records | Sequence windows |
|---|---:|---:|
| Training | 488 | 11,489 |
| Validation | 61 | 1,408 |
| Held-out test | 61 | 1,444 |

Additional preprocessing settings:

- Split ratio: 80% training, 10% validation, and 10% test
- Character vocabulary: constructed from the training partition only
- Vocabulary size: 96 symbols
- Context length: 256 characters
- Window stride: 128 characters
- Maximum windows per record: 64
- Padding token index: 0
- Unknown token index: 1
- Random seed: 42

The held-out test partition was not used for architecture selection, hyperparameter comparison, checkpoint selection, or early stopping.

## Model Architecture

The project implements a decoder-only causal Transformer using PyTorch.

| Component | Configuration |
|---|---:|
| Vocabulary size | 96 |
| Context length | 256 |
| Embedding dimension | 128 |
| Attention heads | 4 |
| Transformer layers | 4 |
| Feed-forward dimension | 512 |
| Trainable parameters | 838,400 |
| Optimization objective | Next-character cross-entropy |
| Optimizer | AdamW |
| Learning rate | 0.0003 |
| Weight decay | 0.01 |
| Maximum epochs | 15 |

Causal attention masking prevents each position from accessing future target characters.

## Controlled Dropout Experiment

Two models were trained under the same data partitions, architecture, optimizer settings, random seed, batch sizes, epoch limit, and evaluation process. Dropout was the only controlled difference.

| Model | Dropout | Best epoch | Validation loss | Validation perplexity | Runtime | Peak GPU memory |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 0.10 | 15 | 1.125494 | 3.082 | 133.07 sec | 0.587 GB |
| Experimental | 0.30 | 15 | 1.582670 | 4.868 | 137.61 sec | 0.594 GB |

The dropout 0.10 model was selected because it achieved:

- 28.89% lower validation loss
- 36.69% lower validation perplexity
- Similar training time and resource usage

The selected inference checkpoint is stored at:

```text
checkpoints/phase5/selected_model_inference.pt
```

## Held-Out Test Results

The selected model was evaluated on the test partition only after model selection was complete.

| Metric | Result |
|---|---:|
| Test records | 61 |
| Test sequence windows | 1,444 |
| Valid target tokens | 354,877 |
| Unknown target tokens | 15 |
| Unknown target rate | 0.0042% |
| Validation loss | 1.125494 |
| Held-out test loss | 1.141745 |
| Validation-to-test loss increase | 0.016252 |
| Held-out test perplexity | 3.132 |
| Held-out token accuracy | 66.47% |

The small difference between validation and test loss indicates that the validation-selected checkpoint transferred consistently to the untouched partition. These metrics measure next-character prediction performance and do not establish legal correctness, factual accuracy, or operational reliability.

## Controlled Generation Experiment

The selected model generated nine controlled samples using three FAR-style prompts and three decoding settings. All experiments used random seed 42 and generated 360 characters per output.

### Decoding Settings

| Setting | Temperature | Top-k | Main observed behavior |
|---|---:|---:|---|
| Greedy | 1.00 | 1 | Highly repetitive and weakly differentiated |
| Conservative top-k | 0.70 | 10 | Best balance of structure and diversity |
| Exploratory top-k | 1.00 | 25 | More diverse but more corrupted and unstable |

### Generation-Quality Comparison

| Setting | Four-gram repetition | Pairwise similarity | Average unique characters | Human-review average |
|---|---:|---:|---:|---:|
| Greedy | 0.631186 | 0.768519 | 39.33 | 1.2 / 4 |
| Conservative top-k | 0.324930 | 0.073148 | 39.00 | 2.2 / 4 |
| Exploratory top-k | 0.183940 | 0.074074 | 40.67 | 1.8 / 4 |

Conservative top-k sampling was the strongest research-oriented setting, but it still fabricated or distorted clause titles, citations, dates, requirements, and obligations. It was therefore not approved for legal or operational use.

## Key Findings

1. Lower dropout produced materially better validation performance for this dataset and architecture.
2. Held-out test performance remained close to validation performance.
3. Greedy decoding produced mode collapse and extensive repetitive language.
4. Conservative top-k sampling improved structural variety but continued to generate authoritative-sounding hallucinations.
5. Exploratory sampling reduced repetition but increased lexical and syntactic corruption.
6. Character-level predictive accuracy did not translate into legally reliable contract drafting.
7. Responsible-use controls are essential when generated language resembles authoritative public-sector source material.

## Responsible Use

This project is limited to reproducible research, education, and demonstration.

Generated outputs must not be:

- Inserted directly into solicitations, contracts, amendments, policies, legal opinions, compliance decisions, or procurement records
- Treated as current or authoritative FAR language
- Used to make autonomous procurement, legal, regulatory, financial, or compliance decisions
- Published without qualified human review
- Generated from confidential, procurement-sensitive, personally identifiable, or otherwise restricted information

Any citation, title, date, obligation, threshold, definition, or legal requirement produced by the model must be checked against the current official source and reviewed by a qualified professional.

## Reproducibility

The repository preserves:

- Frozen processed datasets and split assignments
- Character-vocabulary mapping
- Sequence-window metadata
- Project configuration
- Training histories and comparison results
- Selected compact inference checkpoint
- Held-out test metrics
- Controlled generated outputs
- Quantitative and qualitative generation reviews
- Figures
- SHA-256 artifact hashes
- Machine-readable and human-readable completion audits

Primary audit files include:

```text
data/audit/file_manifest.json
data/audit/PHASE_6_GENERATION_REVIEW.md
data/audit/phase6_completion_audit.json
data/audit/PHASE_6_COMPLETION_AUDIT.md
```

## Repository Structure

```text
capstone-project-5-generative-ai-applications/
├── checkpoints/
│   └── phase5/
│       └── selected_model_inference.pt
├── config/
│   └── project_config.json
├── data/
│   ├── audit/
│   ├── processed/
│   └── raw/
├── figures/
│   ├── phase3_clause_length_distribution.png
│   ├── phase3_sequence_windows_by_split.png
│   ├── phase4_training_smoke_loss.png
│   ├── phase5_validation_loss_comparison.png
│   └── phase6_decoding_tradeoff.png
├── outputs/
│   ├── phase5_training/
│   ├── phase6_evaluation/
│   └── phase6_generation/
├── reports/
│   ├── Generative_AI_Analysis_Report.pdf
│   └── module_summary.pdf
├── src/
├── generative_model.ipynb
├── requirements.txt
├── requirements_minimal.txt
├── SUBMISSION_CHECKLIST.md
└── README.md
```

## Running the Project

### Google Colab

The preferred review environment is Google Colab.

1. Open `generative_model.ipynb` using the Colab badge at the top of this README.
2. Use a T4 GPU for complete retraining.
3. Run notebook cells in order.
4. Do not use the held-out test partition for model selection or experimentation.
5. Review all generated outputs under the responsible-use restrictions documented in the notebook.

The committed notebook already contains the completed project outputs. Retraining is not required to review the submitted analysis and results.

### Local Environment

```bash
git clone https://github.com/icmsol/capstone-project-5-generative-ai-applications.git
cd capstone-project-5-generative-ai-applications

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook generative_model.ipynb
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

A CUDA-capable environment is recommended for training. CPU execution is sufficient for documentation review and lightweight artifact inspection. The full `requirements.txt` is the rubric-compliance environment snapshot generated from the working Colab runtime; `requirements_minimal.txt` is retained only as a concise convenience list of the principal project libraries.

## Primary Deliverables

- Executed modeling notebook: `generative_model.ipynb`
- Selected inference checkpoint: `checkpoints/phase5/selected_model_inference.pt`
- Project configuration: `config/project_config.json`
- Held-out test metrics: `outputs/phase6_evaluation/selected_model_test_metrics.json`
- Controlled generation outputs: `outputs/phase6_generation/controlled_generations.json`
- Generation-quality review: `outputs/phase6_evaluation/generation_quality_review.json`
- Decoding comparison figure: `figures/phase6_decoding_tradeoff.png`
- Submission verification: `SUBMISSION_CHECKLIST.md`
- Final analysis report: `reports/Generative_AI_Analysis_Report.pdf`
- Required duplicate report: `reports/module_summary.pdf`

## Final Reports

The final reviewer-facing analysis is stored in the `reports` directory:

```text
reports/Generative_AI_Analysis_Report.pdf
reports/module_summary.pdf
```

The two PDF files are identical. `Generative_AI_Analysis_Report.pdf` is the canonical report filename, and `module_summary.pdf` is the required duplicate for submission compatibility.

## Limitations

- The model is character-level and has limited semantic understanding.
- The dataset represents a frozen FAR source and may not reflect later regulatory changes.
- Evaluation focuses on next-character prediction and selected surface-level generation measures.
- Human-review scores are based on a small controlled sample.
- Generated language can resemble authoritative source material while being inaccurate.
- The project does not provide legal advice or a deployable contract-authoring system.

## Conclusion

The project demonstrates an end-to-end, reproducible generative-model workflow using public-sector contract language. The controlled experiment supports selection of the dropout 0.10 configuration, and the held-out evaluation shows consistent predictive performance. The generation analysis also demonstrates that plausible structure and low token-level loss are not sufficient for legal reliability. The resulting model is therefore appropriate only for research and demonstration under strict human oversight.
