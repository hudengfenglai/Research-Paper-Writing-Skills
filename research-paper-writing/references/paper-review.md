# Paper review

Review the manuscript as a skeptical but fair reader. The aim is to expose evidence gaps and unclear reasoning, not to manufacture objections.

## Review order

1. Reconstruct the paper's one-sentence contribution.
2. Extract the primary and supporting claims.
3. Locate the evidence anchor for each claim.
4. Check whether the method and protocol can distinguish the claimed explanation from alternatives.
5. Check scope, limitations, citations, and reproducibility.
6. Prioritize fixes by effect on scientific validity.

## Review report

```text
Summary:
Primary contribution as understood:

Findings:
- [blocking|major|minor|polish] Finding
  Evidence anchor:
  Why it matters:
  Smallest fix:

Claims that are currently supported:
Claims that must be weakened or tested:
Missing artifacts or experiments:
Questions for the authors:
```

## High-risk findings

- A headline claim has no direct evidence anchor.
- A comparison omits the baseline, protocol, or metric direction.
- A causal explanation is inferred from a non-isolating ablation.
- A citation does not support the statement attributed to it.
- Results cannot be reproduced from the stated data, code, configuration, and evaluation procedure.
- The conclusion exceeds the tested task, distribution, or deployment setting.

State plainly when a concern is resolved by existing evidence. Do not recommend speculative machinery or unrelated experiments.

