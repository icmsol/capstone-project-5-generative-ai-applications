# Phase 6 Controlled-Generation Review

## Status

**PASS**

## Evaluation design

The validation-selected dropout 0.10 model was evaluated with three fixed clause-number prompts and three decoding strategies. Every combination used the same random seed and generated 360 continuation characters. The outputs were assessed using repetition, diversity, cross-prompt similarity, FAR-style markers, and a documented five-point human-review rubric.

## Quantitative comparison

| Setting | Average 4-Gram Repetition | Average Cross-Prompt Similarity | Average Unique Characters | Average Sentence Terminals |
|---|---:|---:|---:|---:|
| Greedy | 0.6312 | 0.7685 | 39.3 | 1.0 |
| Conservative top-k | 0.3249 | 0.0731 | 39.0 | 2.3 |
| Exploratory top-k | 0.1839 | 0.0741 | 40.7 | 2.3 |

## Findings

### Greedy decoding

Greedy decoding produced recognizable contract-language vocabulary and formatting but showed severe repetition and mode collapse. Different clause-number prompts produced substantially similar generic continuations, often repeating “the Contractor shall” without developing a coherent obligation.

### Conservative top-k sampling

Conservative top-k sampling produced the best balance among the tested settings. It reduced repetitive sequences while retaining paragraph markers, contractual roles, modal verbs, and FAR-like structure. Nevertheless, it invented or distorted clause titles, prescription references, dates, terminology, and legal relationships.

### Exploratory top-k sampling

Exploratory sampling produced the lowest four-gram repetition and the greatest diversity. This apparent improvement came with malformed words, broken syntax, inconsistent paragraph structure, and reduced semantic coherence.

## Selection and limitations

`conservative_top_k` is selected only as the most useful setting for continued research and demonstration. It is not approved for operational, procurement, contractual, or legal use. Every setting generated authoritative-sounding content that could be mistaken for valid FAR language even when the text was fabricated or internally inconsistent.

## Conclusion

The model learned recognizable surface conventions from the FAR corpus but did not acquire dependable legal reasoning, factual grounding, or clause-level semantic fidelity. Quantitative language-model performance therefore does not establish that generated text is accurate, enforceable, or appropriate for acquisition decisions.
