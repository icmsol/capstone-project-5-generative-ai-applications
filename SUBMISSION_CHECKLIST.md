# Submission Checklist

This checklist reflects the current repository status following completion of Phases 1–6 and the final notebook and README cleanup. Items remain unchecked only where final report creation, full-environment capture, or final reproducibility validation is still required.

## Notebook

- [ ] `generative_model.ipynb` runs top to bottom without errors during the final reproducibility validation
- [x] Dataset source and preprocessing provenance are documented
- [x] Full Transformer architecture is implemented
- [x] Training logic, loss, optimizer, and diagnostics are shown
- [x] Multiple generated samples are displayed
- [ ] Qualitative strengths and failure cases cite specific output IDs in the final reviewer-facing narrative
- [x] Four-to-six-sentence notebook summary is included

## Report

- [ ] `reports/Generative_AI_Analysis_Report.pdf` is included
- [ ] `reports/module_summary.pdf` duplicate is included
- [ ] Overview
- [ ] Dataset or Prompt Description
- [ ] Model Design and Training Approach
- [ ] Output Evaluation and Interpretation
- [ ] Ethical Considerations and Responsible Use
- [ ] Limitations and Future Improvements
- [ ] References
- [ ] At least two credible sources are included, including one scholarly source
- [ ] At least one concrete generated failure case is discussed

## Reproducibility

- [x] Fixed source snapshot is retained
- [x] Source checksum is recorded
- [x] Processed dataset and extraction script are included
- [x] Fixed random seeds are recorded in the executed notebook
- [x] Final checkpoint and configuration are retained
- [ ] Full `requirements.txt` is generated with `pip freeze > requirements.txt`
- [x] Public GitHub accessibility is verified

## Current Closeout Status

| Area | Status |
|---|---|
| Phases 1–6 | Complete |
| Notebook structure and completion narrative | Complete |
| README | Complete |
| Final analysis report | Pending |
| Duplicate `module_summary.pdf` | Pending |
| Full `requirements.txt` | Pending |
| Final top-to-bottom reproducibility validation | Pending |
| Final strict rubric review | Pending |

## Final Filename Standard

The canonical report filename for submission will be:

```text
reports/Generative_AI_Analysis_Report.pdf
```

An identical duplicate will also be retained as:

```text
reports/module_summary.pdf
```

The README must use the same canonical report filename before final submission.
