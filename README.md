# Research Paper Writing Skills

An evidence-grounded paper-writing skill for ML, CV, NLP, and adjacent research. It is adapted from Prof. Peng Sida's public research-writing notes and packaged for Codex, Claude Code, and Gemini.

## What changed in v2

- Adds explicit `intake`, `outline`, `draft`, `revise`, `audit`, and `review` modes.
- Requires a research story and claim-evidenceevidence matrix before persuasive drafting.
- Adds citation-integrity, reproducibility, venue-adaptation, and reviewer-checklist references.
- Replaces novelty-inflation advice with evidence-bound contribution writing.
- Adds a local validator for required files and internal reference links.

## Package

```text
research-paper-writing/
  SKILL.md
  agents/openai.yaml
  references/
    abstract.md
    claim-evidence-matrix.md
    citation-integrity.md
    conclusion.md
    experiments.md
    introduction.md
    method.md
    paper-review.md
    related-work.md
    reproducibility.md
    reviewer-checklist.md
    venue-adaptation.md
    workflow.md
```

## Install

From the repository root, copy `research-paper-writing/` into the relevant skills directory.

```bash
# Codex
mkdir -p "$CODEX_HOME/skills"
cp -R research-paper-writing "$CODEX_HOME/skills/"

# Claude Code
mkdir -p "$HOME/.claude/skills"
cp -R research-paper-writing "$HOME/.claude/skills/"

# Gemini
mkdir -p "$HOME/.gemini/skills"
cp -R research-paper-writing "$HOME/.gemini/skills/"
```

Use it explicitly:

```text
Use $research-paper-writing to audit the claim-evidence matrix and revise my Introduction.
```

## Attribution and comparison sources

See [SOURCES.md](./SOURCES.md) for the original Peng Sida notes and the open research-skill repositories consulted during the v2 redesign.

## License

MIT. See [LICENSE](./LICENSE).

