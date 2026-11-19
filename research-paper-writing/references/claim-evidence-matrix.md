# Claim�Cevidence matrix

Use one row per claim. Split a compound claim when different parts need different evidence.

| ID | Claim | Type | Evidence required | Source anchor | Status | Allowed wording | Gap or next action |
|---|---|---|---|---|---|---|---|
| C1 | ... | method / empirical / theoretical / interpretive | ... | table, figure, equation, log, citation | VERIFIED / INFERRED / DRAFT / MISSING | ... | ... |

## Evidence types

- **Method:** equation, algorithm, architecture, or implementation artifact that directly defines what was done.
- **Empirical:** result table, figure, test output, or statistical analysis produced by the stated protocol.
- **Theoretical:** proposition, proof, derivation, or cited result whose assumptions match the paper.
- **Interpretive:** explanation that follows from verified results and is stated with appropriate uncertainty.
- **Scope:** task, data, or deployment boundary that limits how far the claim can be generalized.

## Wording policy

- `VERIFIED` permits a direct statement whose scope matches the evidence.
- `INFERRED` permits cautious interpretation and must identify the inference.
- `DRAFT` is planning text and must not appear as a final result.
- `MISSING` cannot appear as a conclusion. Add evidence, weaken the claim, or remove it.

## Minimum checks

1. A headline claim has at least one direct evidence anchor.
2. A comparison claim names the baseline, dataset, metric, and protocol.
3. A causal claim has a comparison or design that can distinguish the proposed cause.
4. A generalization claim names the tested distribution and the boundary of extrapolation.
5. A limitation is recorded when the evidence does not cover an obvious alternative explanation.

