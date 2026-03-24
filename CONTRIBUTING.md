# Contributing

Thanks for contributing to **Grokking LLM System Design**.

The project is intentionally simple: Markdown content, MkDocs Material for presentation, GitHub Actions for validation and deployment, and a lightweight review process focused on clarity and evidence.

## Working principles

- keep prose concise, technical, and evidence-driven
- keep changes small and reviewable
- prefer Markdown and Mermaid over custom frontend work
- separate sourced fact from editorial inference
- update `mkdocs.yml` and the relevant section `index.md` pages when navigation should change

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
- place new chapters in the section folder they logically belong to

Examples:

- `docs/knowledge-retrieval-systems/internal-chatgpt.md`
- `docs/inference-platform-infra/llm-gateway-proxy.md`
- `docs/model-lifecycle/llm-fine-tuning-system.md`

## Structure a case study

Handbook chapters should follow the system design structure in `docs/contributing/chapter-template.md`:

1. problem framing
2. functional requirements
3. non-functional requirements
4. high-level architecture
5. core components
6. data flow or request flow
7. scaling and reliability
8. trade-offs
9. failure modes
10. security, safety, and governance
11. interview discussion points

Case studies should use the same chapter frame, then add a one-line summary and explicit sources.

Keep the distinction between sourced facts and editorial inference explicit.

When adding a new case study, place it in the section where readers would expect to find that system archetype.

When adding any new chapter, update the relevant section landing page such as `docs/inference-platform-infra/index.md` or `docs/knowledge-retrieval-systems/index.md`.

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
