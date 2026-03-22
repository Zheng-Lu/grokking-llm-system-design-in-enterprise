# Contributing

Thanks for contributing to **Grokking LLM System Design in Enterprise**.

The project is intentionally simple: Markdown content, MkDocs Material for presentation, GitHub Actions for validation and deployment, and a lightweight review process focused on clarity and evidence.

## Local setup

```bash
uv sync
```

## Run the docs site locally

```bash
python scripts/check_links.py
uv run mkdocs serve
```

For a CI-equivalent build:

```bash
uv run mkdocs build --strict
```

## Propose a new chapter

Use one of these paths:

- open a GitHub issue with the `case study request` template
- open a draft pull request with a starter outline
- discuss the idea in GitHub Discussions once enabled

Before writing a full chapter, make sure the topic has:

- clear enterprise relevance
- reusable design lessons
- public sources that can support factual claims

## File naming

- use lowercase kebab-case
- keep filenames short and descriptive
- group related pages under the existing section folders

Examples:

- `docs/case-studies/microsoft-ask-learn.md`
- `docs/patterns/permission-aware-rag.md`
- `docs/taxonomy/llmops-evals.md`

## Structure a case study

Case studies should follow the chapter template in `docs/contributing/chapter-template.md`:

1. one-line summary
2. problem
3. why naive solutions fail
4. architecture
5. key design choices
6. trade-offs
7. reusable patterns
8. failure modes
9. interview version
10. sources

Keep the distinction between sourced facts and editorial inference explicit.

## Submit diagrams

Prefer diagrams that are easy to review and edit:

- Mermaid for simple architecture and sequence diagrams
- editable source files in `docs/assets/diagrams/`
- exported SVG or PNG assets in `docs/assets/images/` only when needed

When you submit a diagram:

- keep the source under version control
- keep labels short and technically precise
- ensure the diagram still reads well on mobile and narrow viewports
- reference the diagram from the relevant chapter instead of leaving orphaned assets

## Pull request expectations

Before opening or updating a PR:

- run `python scripts/check_links.py`
- run `uv run mkdocs build --strict`
- update `mkdocs.yml` if you added or renamed docs pages
- keep changes small enough for reviewers to reason about quickly

## Dependency notes

`uv` is the default path and `uv.lock` is committed for reproducible installs. `requirements.txt` remains as a simple fallback for contributors who prefer `pip`.
