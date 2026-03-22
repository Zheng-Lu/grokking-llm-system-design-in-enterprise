# AGENTS.md

## Project purpose

This repository is an open-source technical book called **Grokking LLM System Design in Enterprise**. It documents reusable system design patterns and public case studies for enterprise LLM applications, RAG systems, AI agents, AI infrastructure, and LLMOps.

## Repository conventions

- Treat `Grokking LLM System Design in Enterprise` as the canonical project name across docs, metadata, and contributor messaging.
- Keep the architecture static, Markdown-first, and GitHub Pages friendly.
- Prefer MkDocs Material features over custom frontend code.
- Favor small, reviewable changes over broad rewrites.
- Do not add backend services, databases, authentication, or analytics unless explicitly requested.

## File and folder expectations

- Put reader-facing site content in `docs/`.
- Keep contributor and community documents at the repository root.
- Place editable diagram sources in `docs/assets/diagrams/`.
- Place exported images in `docs/assets/images/`.
- Keep utility scripts in `scripts/` and make them dependency-light.

## Writing rules

- Keep prose concise, technical, and evidence-driven.
- Lead with the system design problem, then explain architecture and trade-offs.
- Separate facts from inference when summarizing public case studies.
- Prefer short sections, bullets, tables, and diagrams over long narrative blocks.
- Use lowercase kebab-case for filenames.

## Navigation updates

- When adding a new documentation page, update `mkdocs.yml` in the same change.
- If a new chapter changes how readers browse the book, update any relevant hub pages such as `docs/index.md`, `docs/roadmap.md`, or `docs/case-studies/_index.md`.
- Keep nav labels concise and consistent with the file contents.

## Change management

- Avoid unnecessary complexity, plugin churn, and theme customization.
- Prefer Markdown and Mermaid over custom HTML, JavaScript, or image-heavy diagrams.
- Never silently delete user content.
- If a section must be restructured, preserve intent and move content deliberately.
- Keep diagrams source-controlled and editable.

## New chapter checklist

When adding a new chapter:

1. Create the Markdown file in the appropriate `docs/` section.
2. Follow `docs/contributing/chapter-template.md` if it is a case study.
3. Add the page to `mkdocs.yml`.
4. Update related catalog or taxonomy pages if discoverability would otherwise regress.
5. Run `python scripts/check_links.py` and `uv run mkdocs build --strict`.
