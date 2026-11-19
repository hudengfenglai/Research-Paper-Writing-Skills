# Method writing guide

The Method section should let a technically trained reader reconstruct what was done and why each design choice exists.

## Before prose

List the modules and answer for each:

- What are the input and output?
- What problem or assumption motivates the module?
- What is the forward process, in execution order?
- What consequence should be visible in the experiments?
- What assumptions or trade-offs limit the module?

## Subsection pattern

1. Motivation tied to a concrete challenge
2. Representation, architecture, or algorithm definition
3. Forward process from input to output
4. Objective, optimization, or inference details
5. Technical consequence and boundary

Place hyperparameters, normalization, coordinate conventions, stopping rules, and implementation details close enough to reproduce the method. Keep ablation interpretation in Experiments.

## Method clarity checks

- Define every symbol at first use.
- Separate intuition from the formal operation.
- Use one name for one concept.
- Explain why a module is needed before claiming its advantage.
- Do not imply a causal mechanism that the experiments do not isolate.

