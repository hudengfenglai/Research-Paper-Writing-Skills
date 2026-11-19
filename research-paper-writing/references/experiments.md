# Experiments writing guide

Experiments should test claims rather than decorate a method description.

## Experiment card

```text
Claim tested:
Why this protocol can test it:
Datasets and splits:
Baselines and tuning:
Metrics and direction:
Seeds and uncertainty:
Expected signal:
Observed result:
Interpretation:
Failure cases or alternative explanations:
Artifact anchors:
```

## Core package

- Main comparison against strong and relevant baselines
- Ablation that isolates every central design choice
- Robustness, generalization, efficiency, or qualitative analysis matched to the claims
- Reproducibility details and uncertainty reporting

Use the smallest experiment that can distinguish competing explanations. A gain over a weak or poorly tuned baseline does not support a superiority claim. An ablation shows sensitivity to a design choice, but it does not automatically prove the proposed causal explanation.

## Figures and tables

- Captions state the setting, metric direction, and notation without requiring the body text.
- Tables use consistent precision and units, and group results by one message.
- Report variance or intervals when run-to-run variation matters.
- Show meaningful failure cases when they define the method's boundary.

