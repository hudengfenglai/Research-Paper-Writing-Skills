# Writing workflow

This workflow keeps persuasive writing downstream of research evidence. It is designed for a human-in-the-loop session and can be stopped at any gate.

## Intake card

```text
Mode:
Target venue and audience:
Paper status:
Available artifacts:
One-sentence contribution:
Primary claim:
Supporting claims:
Known limitations:
Output needed now:
Open decisions:
```

## Gates

### Gate A �� scope

Pass when the task, audience, output format, and available artifacts are explicit. If a missing item could change the scientific interpretation, stop and ask one focused question.

### Gate B �� story

Pass when `problem �� gap �� insight �� method �� evidence �� boundary` can be written without placeholders except those explicitly marked `MISSING`.

### Gate C �� claims

Pass when every major claim has an evidence type, source anchor, status, and allowed wording in the claim�Cevidence matrix.

### Gate D �� draft

Pass when every paragraph has one role and every section transition is justified by the story.

### Gate E �� audit

Pass when citation identity, claim strength, reproducibility details, and venue constraints have been checked. Unresolved items remain visible in the output.

## Recommended artifact set

```text
paper-work/
  intake.md
  story-card.md
  claim-evidence-matrix.md
  citation-ledger.md
  draft.md
  review-report.md
```

Use another directory layout when the user's project already has one. Do not create duplicate project memory files without a reason.

