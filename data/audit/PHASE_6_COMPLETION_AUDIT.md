# Phase 6 Completion Audit

## Status

**PASS**

## Held-out evaluation

- Selected model: `baseline_dropout_0.10`
- Test records: 61
- Test windows: 1,444
- Persisted windows validated: 1,444
- Valid target tokens: 354,877
- Validation cross-entropy loss: 1.125494
- Test cross-entropy loss: 1.141745
- Test perplexity: 3.132
- Test token accuracy: 66.47%
- Test-minus-validation loss: +0.016252
- Unknown-target rate: 0.0042%
- Test partition role: final evaluation only

## Controlled generation

- Prompts: 3
- Decoding settings: 3
- Generated outputs: 9
- Continuation characters per output: 360
- Fixed seed: 42
- Recommended research setting: `conservative_top_k`
- Approved for operational, procurement, contractual, compliance, or legal use: **No**

## Observed behavior

| Setting | Average 4-Gram Repetition | Primary Failure |
|---|---:|---|
| Greedy | 0.6312 | Repetition and mode collapse |
| Conservative top-k | 0.3249 | Authoritative-sounding hallucination |
| Exploratory top-k | 0.1839 | Lexical and syntactic corruption |

## Conclusion

The selected Transformer generalized consistently from validation to the held-out test partition, but its generated outputs did not demonstrate dependable factual grounding, legal reasoning, or clause-level semantic fidelity. Conservative top-k decoding provided the most useful balance for research demonstration, while every tested setting produced fabricated, corrupted, or unsupported contract language. The model is therefore restricted to controlled research and educational use with mandatory human verification against authoritative sources.

## Final closeout readiness

**PASS**
