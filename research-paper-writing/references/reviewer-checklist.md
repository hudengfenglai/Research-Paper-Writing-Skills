# Reviewer checklist

Classify each item as `pass`, `needs revision`, or `needs new evidence`. Record an anchor for every non-trivial finding.

## Contribution and scope

- [ ] The primary contribution is one sentence and is technically precise.
- [ ] Novelty is compared with the closest prior mechanisms, assumptions, and results.
- [ ] The paper does not claim more generality than the tested setting supports.
- [ ] Limitations are concrete and connected to the task goal.

## Writing and organization

- [ ] The abstract states task, challenge, contribution, evidence, and boundary.
- [ ] The introduction exposes the exact gap before presenting the solution.
- [ ] Each paragraph has one message and a topic sentence.
- [ ] Terms, symbols, and method names remain stable.
- [ ] Related Work is organized by ideas rather than a paper-by-paper list.

## Method and evidence

- [ ] Inputs, outputs, assumptions, and forward steps are reproducible.
- [ ] Every key module has a reason for existing and a verifiable consequence.
- [ ] Each main experiment names the claim it tests.
- [ ] Baselines, splits, metrics, tuning, seeds, and compute are fair and documented.
- [ ] Ablations isolate the claimed design choices.
- [ ] Failure cases and alternative explanations are reported where relevant.

## Integrity and presentation

- [ ] Every citation is verified and supports the attributed statement.
- [ ] Every headline number has an artifact anchor.
- [ ] Statistical uncertainty and test assumptions are stated where needed.
- [ ] Captions are self-contained and tables use consistent notation and precision.
- [ ] Official venue requirements have been checked against the current call for papers.

## Final triage

- `blocking`: a claim is false, unsupported, or impossible to reproduce.
- `major`: a missing experiment or explanation changes the paper's evaluation.
- `minor`: a localized clarity, notation, or presentation issue.
- `polish`: wording or formatting improvement with no scientific consequence.

