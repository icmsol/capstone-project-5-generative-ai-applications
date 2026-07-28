# Phase 1 Dataset Sufficiency Audit

## Decision
**GO - the dataset is suitable for the approved Project 5 generative task.**

## Results

| Audit measure | Result |
|---|---:|
| Detected section headings, 52.200-52.253-1 | 746 |
| Reserved headings excluded | 135 |
| Scope-only records excluded | 1 |
| Usable provisions/clauses | 610 |
| Empty usable records | 0 |
| Exact duplicate usable records | 0 |
| Clean corpus characters | 2,214,901 |
| Case-folded word tokens | 343,705 |
| Unique case-folded word tokens | 8,519 |
| Character vocabulary | 97 |
| Median words per record | 291.5 |
| Minimum / maximum words | 41 / 8,553 |
| Clause families represented | 45 |
| Records containing underscore fill-ins | 178 |
| Records containing bracket-style fill-ins | 112 |

## Model recommendation
Use a **character-level causal Transformer** and split by complete clause/provision records before sequence chunking. This avoids external tokenizer dependencies, prevents out-of-vocabulary failures, keeps the output layer small, and is practical for a Colab T4. The model will generate short continuations for controlled prompts; it will not attempt to draft complete or legally usable clauses.

## Principal dataset risks
1. Clause lengths are highly skewed, so long clauses could dominate the training stream unless sampling is controlled.
2. Fill-in fields, dates, thresholds, and cross-references may be reproduced incorrectly or hallucinated.
3. The corpus represents federal acquisition language rather than all state and local public-sector contracting practices.
4. The frozen FAC snapshot can become outdated after later regulatory changes.
5. A model may memorize recurring boilerplate; source-overlap checks are therefore required.

## Phase 2/3 controls
- Preserve a fixed source snapshot and checksum.
- Split at the clause level before creating fixed-length sequences.
- Apply maximum contribution or balanced sampling controls for unusually long records.
- Retain fill-in markers but normalize them consistently.
- Save prompt, sampling, seed, and checkpoint information for every final output.
- Evaluate source overlap and prohibit operational/legal use.
