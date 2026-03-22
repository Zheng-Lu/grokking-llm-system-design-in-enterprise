# Grokking LLM System Design in Enterprise

Open case studies on enterprise LLMs, RAG, agents, AI infra, and LLMOps.

This repository hosts a concise, contributor-friendly, open-source book on how real teams design, operate, and govern LLM systems in enterprise settings. The focus is practical system design: architecture choices, trade-offs, failure modes, evaluation loops, security boundaries, and reusable patterns that show up across serious production deployments.

## Why this project exists

There is plenty of LLM content that is either too shallow, too vendor-specific, or too focused on demos. This project aims to be different:

- grounded in public case studies and technical write-ups
- optimized for readers who want reusable design patterns, not hype
- structured to work both as a book and as interview prep
- easy for outside contributors to extend with Markdown-first workflows

## Screenshot

Add a homepage screenshot here after the first published GitHub Pages deploy.

Suggested path: `docs/assets/images/site-homepage.png`

## Quickstart

```bash
uv sync
python scripts/check_links.py
uv run mkdocs serve
```

Then open the local preview URL printed by MkDocs, usually `http://127.0.0.1:8000`.

## Local development

1. Install Python 3.11 or newer.
2. Install `uv`.
3. Install dependencies with `uv sync`.
4. Run `python scripts/check_links.py` to catch broken local Markdown links.
5. Run `uv run mkdocs serve` for live reload while editing.
6. Run `uv run mkdocs build --strict` before opening a pull request.

Fallback (if you do not want `uv`):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m mkdocs serve
```

## Deployment

The repository includes GitHub Actions for:

- validating builds on pull requests and pushes
- deploying the static MkDocs site to GitHub Pages

The deployment workflow is configured for `main` and `master` so it works during repo bootstrap. Once the canonical default branch is set, you can narrow the trigger if you want.

## Contribution invitation

Contributions are welcome across:

- new case studies backed by public sources
- taxonomy and pattern chapters
- diagrams that clarify architecture or trade-offs
- editorial improvements that reduce ambiguity or verbosity

Start with [CONTRIBUTING.md](CONTRIBUTING.md), then review the docs style guidance in [docs/contributing/style-guide.md](docs/contributing/style-guide.md) and the chapter structure in [docs/contributing/chapter-template.md](docs/contributing/chapter-template.md).

## Roadmap summary

- MVP: establish the site, editorial rules, taxonomy pages, reusable patterns, and a few sample chapters
- Near term: add high-quality case studies from major enterprise deployments and tighten the interview track
- Long term: turn the repository into a dependable reference for enterprise LLM system design

See [docs/roadmap.md](docs/roadmap.md) for the detailed roadmap.

## License

This repository uses Apache-2.0 in v1 to keep licensing simple for both content and repo tooling. If the project later benefits from separate content and code licenses, that can be introduced explicitly in a future revision.

## Community

Use GitHub Issues for concrete bugs, content proposals, and feature requests. Use GitHub Discussions for broader questions, editorial ideas, and roadmap conversation once Discussions is enabled on the repository.
