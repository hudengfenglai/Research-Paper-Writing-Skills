# Reproducibility and statistical reporting

Use this guide when drafting Method, Experiments, or an audit report.

## Minimum experiment record

- Dataset version, split, preprocessing, and exclusion rules
- Baseline implementation and tuning protocol
- Model, optimizer, schedule, batch size, stopping rule, and selected hyperparameters
- Random seeds and number of independent runs
- Hardware, software versions, and relevant compute budget
- Metrics, direction of improvement, aggregation rule, and evaluation script
- Exact artifact path for each reported number or figure

## Uncertainty

Report variation across runs when randomness can affect the conclusion. State whether an interval is a standard deviation, standard error, confidence interval, bootstrap interval, or another quantity. Do not call a difference significant without a stated test and its assumptions.

## Result interpretation

For every experiment, write:

1. **Claim tested**
2. **Protocol**
3. **Expected signal**
4. **Observed result**
5. **Interpretation**
6. **Alternative explanations and limits**

Ablations identify which design choices matter. They do not by themselves establish a causal explanation unless the comparison isolates the relevant factor.

