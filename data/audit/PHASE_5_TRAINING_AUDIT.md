# Phase 5 Training and Model-Selection Audit

## Status

**PASS**

## Controlled experiments

- Baseline experiment: `baseline_dropout_0.10`
- Comparison experiment: `experimental_dropout_0.30`
- Only controlled difference: dropout
- Maximum epochs per run: 15
- Selection metric: validation cross-entropy loss
- Held-out test partition used during training or selection: **No**

## Selected model

- Selected experiment: `baseline_dropout_0.10`
- Selected dropout: 0.10
- Best epoch: 15
- Best validation loss: 1.125494
- Best validation perplexity: 3.082
- Validation-loss advantage: 28.89%
- Perplexity advantage: 36.69%

## Checkpoint validation

- Compact checkpoint: `checkpoints/phase5/selected_model_inference.pt`
- Maximum restored-logit difference: 0.000000000000
- Restoration validation: **PASS**
- Phase 6 readiness: **PASS**

## Interpretation

The dropout 0.10 model outperformed the dropout 0.30 model throughout the controlled training budget. The higher-dropout configuration reduced learning efficiency and produced a substantially higher validation loss and perplexity. The baseline checkpoint was therefore selected using validation evidence only, while the held-out test partition remained untouched.
