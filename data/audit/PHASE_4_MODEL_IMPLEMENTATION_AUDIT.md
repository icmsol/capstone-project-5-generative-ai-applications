# Phase 4 Transformer Implementation and Smoke-Test Audit

## Purpose

Phase 4 implements a compact decoder-style causal Transformer directly in PyTorch and validates the architecture before full model training. The tests confirm tensor compatibility, causal masking, padding-aware loss, finite gradient flow, short-run optimization, validation improvement, and exact checkpoint restoration.

## Architecture

| Attribute | Value |
|---|---:|
| Vocabulary size | 96 |
| Context length | 256 |
| Model dimension | 128 |
| Attention heads | 4 |
| Transformer layers | 4 |
| Feed-forward dimension | 512 |
| Dropout | 0.10 |
| Trainable parameters | 838,400 |
| Parameter memory | 3.35 MB |
| Activation | GELU |
| Normalization | Pre-layer normalization |
| Output-weight tying | Enabled |

## Forward-Pass Validation

| Test | Result |
|---|---|
| Input tensor shape | `(4, 256)` |
| Target tensor shape | `(4, 256)` |
| Logits tensor shape | `(4, 256, 96)` |
| Initial loss | 4.573635 |
| Causal attention mask | PASS |
| Padding-aware loss | PASS |
| Finite logits and loss | PASS |

The initial loss is consistent with an untrained model predicting across 96 vocabulary entries.

## Causal-Invariance Test

The second half of a full-length input sequence was altered while the first half remained unchanged.

| Measure | Value |
|---|---:|
| Changed suffix start position | 128 |
| Maximum earlier-position difference | 0.0000000000 |
| Maximum permitted suffix difference | 0.2911112309 |
| Future-to-past information leakage | None |
| Result | PASS |

## Gradient and Fixed-Batch Optimization Test

| Measure | Value |
|---|---:|
| Nonzero gradient tensors | 52 |
| All gradients finite | True |
| Initial gradient norm | 3.757951 |
| Optimization steps | 25 |
| Initial fixed-batch loss | 4.614851 |
| Final fixed-batch loss | 3.128065 |
| Loss reduction | 1.486786 |
| Loss reduction percentage | 32.22% |
| Result | PASS |

## Reusable Training-Loop and Validation Test

| Measure | Value |
|---|---:|
| Batch size | 16 |
| Training batches | 50 |
| First training-batch loss | 4.625175 |
| Final training-batch loss | 3.051215 |
| Minimum training-batch loss | 2.944910 |
| Validation loss before | 4.611577 |
| Validation loss after | 2.940165 |
| Validation loss reduction | 1.671412 |
| Validation perplexity before | 100.643 |
| Validation perplexity after | 18.919 |
| Result | PASS |

## Checkpoint Round Trip

| Measure | Value |
|---|---:|
| Checkpoint size | 10.13 MB |
| SHA-256 | `c4f6bc991ae859eb4565058e15703e27adf7e9286c6ab2a89800ef86971bbc4d` |
| Restored prediction maximum difference | 0.0000000000 |
| Exact restoration | PASS |

The Phase 4 binary checkpoint is treated as a temporary smoke-validation artifact. The final selected-model checkpoint will be created and preserved during Phase 5.

## Phase 4 Conclusion

The custom causal Transformer is structurally valid and ready for full training. The implementation prevents future-token leakage, ignores padding targets during loss calculation, produces finite nonzero gradients, improves both training and validation loss, and restores predictions exactly from a saved checkpoint. Phase 5 may proceed using the validated architecture and reusable training/evaluation functions.
