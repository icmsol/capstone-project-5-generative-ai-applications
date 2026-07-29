# Phase 3 Preprocessing and Sequence Audit

## Clause-Level Split

| Partition | Records | Percentage | Characters | Word-Like Tokens | Families Represented |
|---|---:|---:|---:|---:|---:|
| Train | 488 | 80.0% | 1,740,590 | 269,982 | 43 |
| Validation | 61 | 10.0% | 219,276 | 34,337 | 32 |
| Test | 61 | 10.0% | 247,442 | 38,081 | 31 |

The split was performed at the complete-clause level before sequence-window construction. Record overlap between all partition pairs is zero. The test partition is held out from model selection.

## Character Vocabulary

- Vocabulary source: training partition only
- Training characters: 94
- Special tokens: 2 (`<PAD>` and `<UNK>`)
- Total vocabulary size: 96
- Validation-only characters: ["\u2018"]
- Test-only characters: ["\u00ae", "\u274f"]
- Families absent from training: 202, 239

Rare validation or test characters not observed in training are mapped to `<UNK>`. Building the vocabulary from training data only prevents information from held-out records from influencing preprocessing.

## Sequence Construction

| Partition | Windows | Records Represented | Padded Windows | Average Valid Tokens | Maximum Windows per Record |
|---|---:|---:|---:|---:|---:|
| Train | 11,489 | 488 | 924 | 245.3 | 64 |
| Validation | 1,408 | 61 | 119 | 245.1 | 64 |
| Test | 1,444 | 61 | 114 | 245.8 | 64 |

- Context length: 256 characters
- Sequence stride: 128 characters
- Maximum windows per record: 64
- Cross-clause sequence windows: prohibited
- Padding loss policy: padding targets will be ignored by the cross-entropy loss
- Long-clause control: evenly spaced windows are retained across the full clause when the cap is reached

## Phase 3 Conclusion

The corrected FAR corpus has been divided into reproducible, leakage-controlled train, validation, and held-out test partitions. The character vocabulary was derived exclusively from training records. The sequence pipeline retains coverage across every source record while limiting the influence of unusually long clauses. The artifacts are ready for Transformer implementation and smoke testing.
