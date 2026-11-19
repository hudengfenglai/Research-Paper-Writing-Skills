---
name: research-paper-writing
description: Evidence-grounded writing and review workflow for ML, CV, NLP, and adjacent research papers. Use when turning research artifacts into a paper story, drafting or revising Abstract, Introduction, Related Work, Method, Experiments, or Conclusion, auditing citations and claims, planning missing experiments, or preparing a venue submission.
version: 2.0.0
license: MIT
---

# Research Paper Writing

Use this skill to make a research paper easier to understand, verify, and review. It is adapted from Prof. Peng Sida's public research-writing notes and supplemented with evidence-first practices from established open research-skill projects.

## Non-negotiable rules

1. **Evidence before prose.** Inspect the supplied paper, code, tables, figures, logs, and citations before making a factual claim.
2. **Keep the truth boundary visible.** Mark statements as `VERIFIED`, `INFERRED`, `DRAFT`, or `MISSING`. Never turn an inference into a result or a hypothesis into a conclusion.
3. **Never invent citations, numbers, experiments, reviewer feedback, or implementation details.** If a citation cannot be verified, use `[CITATION NEEDED]` and record what must be checked.
4. **Explain genuine novelty precisely.** Do not inflate a simple pipeline, hide a baseline component, or replace a weak result with stronger wording.
5. **Make claims falsifiable.** Every major claim must map to a result, a method derivation, a citation, or an explicitly stated limitation.
6. **Preserve user facts and notation.** Ask only when a missing decision would change the paper's scientific meaning. Otherwise state the assumption and continue.

## Route the request

| Request | Mode | Primary output |
|---|---|---|
| Topic, notes, code, or results are not yet organized | `intake` | Research story card and missing-artifact list |
| Need a paper architecture or section plan | `outline` | Section outline, figure plan, and claim-evidenceevidence matrix |
| Need new prose | `draft` | Draft text with paragraph roles and evidence anchors |
| Need to improve existing prose | `revise` | Revised text plus change rationale and fact changes |
| Need to check a paper before submission | `audit` | Citation, claim, reproducibility, and venue audits |
| Need a skeptical assessment | `review` | Prioritized findings, evidence anchors, and minimum fixes |

If the request does not specify a mode, infer one from the task and state it in the first line of the response.

## Workflow and gates

### 1. Intake

Create a compact intake card before drafting:

- Task, audience, target venue, and format constraints
- Available artifacts and their paths
- Proposed contribution in one sentence
- Known results, baselines, metrics, and limitations
- Output requested in this turn

If the proposed contribution or the evidence is unclear, produce the card and a focused missing-information list before writing persuasive prose.

### 2. Research story

Build `problem -> gap -> insight -> method -> evidence -> boundary`.

The story must answer three questions:

- **What:** What new result, method, analysis, or understanding is contributed?
- **Why:** Which evidence distinguishes the claim from plausible alternatives?
- **So what:** Why does the result matter to the intended research community?

Reduce the paper to one primary contribution and at most three supporting claims. Split claims that require different evidence.

### 3. Claim-evidenceevidence matrix

Before drafting Abstract or Introduction, create a matrix using `references/claim-evidence-matrix.md`. Each claim receives an evidence type, source anchor, status, and allowed wording. A claim without evidence is either downgraded to a hypothesis or moved to the open-issues list.

### 4. Section drafting

Load only the relevant guide from `references/`:

- `abstract.md`
- `introduction.md`
- `related-work.md`
- `method.md`
- `experiments.md`
- `conclusion.md`

Draft from the matrix, then run reverse outlining. Each paragraph needs one job, a clear topic sentence, and a visible relation to the paragraph before it.

### 5. Verification passes

Run the following passes in order:

1. **Fact pass:** numbers, settings, dataset names, baselines, and citations match the supplied artifacts.
2. **Claim pass:** Abstract and Introduction contain no claim stronger than the matrix allows.
3. **Reproduction pass:** another researcher could identify data, code, configuration, seeds, metrics, and evaluation protocol.
4. **Reader pass:** terms are defined, notation is stable, and figures/tables can be interpreted from their captions.
5. **Reviewer pass:** use `references/reviewer-checklist.md` and `references/paper-review.md`.

### 6. Output

Return the requested text together with:

1. Assumptions and missing artifacts
2. A compact outline or paragraph-role map
3. Revised or drafted content
4. Claim-evidenceevidence matrix changes
5. Unresolved risks and the smallest next action for each risk

For `review` mode, report findings by severity: `blocking`, `major`, `minor`, or `polish`. Attach an evidence anchor or explain why an anchor is unavailable.

## Section routing notes

- **Abstract:** task, concrete challenge, contribution or insight, evidence, and boundary. Include a number only when its source and comparison are verified.
- **Introduction:** lead readers from the problem to the exact gap and then to the tested solution. Describe the actual mechanism and the reason it addresses the gap.
- **Related Work:** group by technical idea or assumption. Compare mechanisms and limitations rather than listing papers one by one.
- **Method:** for every module, state motivation, input/output, forward process, assumptions, and technical consequence. Separate final design from ablations.
- **Experiments:** introduce each experiment with the claim it tests, the protocol, the expected signal, the result, and the interpretation. Report uncertainty and failure cases when relevant.
- **Conclusion:** restate the supported contribution, strongest evidence, scope boundary, and a concrete next direction.

## Citation and source discipline

Use `references/citation-integrity.md` whenever adding or changing citations. Search first, verify bibliographic identity, inspect the source for the attributed claim, and keep a citation ledger. Do not use a search snippet as evidence for a technical statement.

## Revision discipline

When revising existing text, preserve all scientific facts unless the user requests a factual change. Distinguish wording edits from changes to claims, numbers, scope, or interpretation. Flag every factual change explicitly.

