# Citation integrity

## Source hierarchy

Prefer, in order:

1. The paper's official version, DOI landing page, or publisher record
2. The authors' project page or institutional repository
3. arXiv or another recognized preprint server
4. Bibliographic indexes such as Semantic Scholar, OpenAlex, or Crossref
5. Search results only as leads, never as final evidence

## Verification procedure

For every new citation:

1. Search with title, author, and topic terms.
2. Confirm that the title, authors, year, venue, and DOI or stable URL agree across a reliable record.
3. Read the source passage that supports the attributed statement.
4. Retrieve BibTeX from the verified record, never from memory.
5. Record the query, source URL, verification date, and claim supported in `citation-ledger.md`.

If a paper cannot be verified, use a visible placeholder:

```latex
\cite{PLACEHOLDER_verify_author_year} % verify before submission
```

## Citation ledger

```text
Key:
Claim supported:
Bibliographic identity:
Verified sources:
Source passage or page:
Verification date:
Status: VERIFIED / NEEDS_REVIEW / REJECTED
```

## Claim attribution

A citation proves what the cited source says. It does not prove that the current paper's method works. Keep prior-work claims, current-paper results, and interpretations in separate sentences when their evidence differs.

