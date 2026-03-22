---
hide:
  - toc
---

<div class="home-hero" markdown>

<div class="book-metadata">
<span>Open-source book</span>
<span>Enterprise LLM systems</span>
<span>Markdown-first</span>
</div>

# Grokking LLM System Design in Enterprise

_Open case studies on enterprise LLMs, RAG, agents, AI infra, and LLMOps._

This project turns public engineering material into a practical book about how serious teams build LLM systems under enterprise constraints: messy data, permission boundaries, reliability requirements, evaluation pressure, cost limits, and governance overhead.

[Read the vision](about.md){ .md-button .md-button--primary }
[Browse the roadmap](roadmap.md){ .md-button }
[Contribute a chapter](contributing/chapter-template.md){ .md-button }

</div>

## What the book covers

<div class="grid cards" markdown>

- :material-application-braces-outline: **LLM applications**

  System design for copilots, internal assistants, workflow automation, and task-specific interfaces.

- :material-database-search-outline: **Retrieval-augmented generation**

  Chunking, indexing, retrieval quality, freshness, permission filters, and grounding strategies.

- :material-robot-outline: **AI agents**

  Tool use, planning, orchestration, escalation, and where agentic systems break in production.

- :material-server-outline: **AI infrastructure**

  Gateways, model routing, latency controls, caching, observability, and cost-aware serving.

- :material-chart-timeline-variant: **LLMOps and evals**

  Trace capture, offline and online evaluation, release gates, and feedback loops for iteration.

- :material-shield-check-outline: **Security and governance**

  Data boundaries, access control, prompt injection defense, auditability, and policy enforcement.

</div>

## Why this project exists

Most LLM material falls into one of three weak buckets:

- demo-driven content with little operational realism
- vendor content that hides hard trade-offs
- fragmented notes that never become reusable design knowledge

This book exists to compress public lessons into clear chapters that answer the same questions repeatedly:

- What problem was the system actually solving?
- Why did naive approaches fail?
- Which architectural choices mattered?
- What were the trade-offs, failure modes, and reusable patterns?

## Who this is for

- engineers designing enterprise LLM systems
- staff and principal engineers reviewing architecture choices
- AI platform teams building internal abstractions
- interview candidates preparing for modern AI system design rounds
- contributors who want to turn scattered public material into durable technical writing

!!! note "Editorial stance"
    The project is intentionally technical and concise. It favors architecture, trade-offs, and operational reality over product marketing language.

## How to contribute

Start with the contributor materials:

- [Style guide](contributing/style-guide.md)
- [Chapter template](contributing/chapter-template.md)
- [Review process](contributing/review-process.md)

Practical contribution paths:

1. Propose a new case study backed by public sources.
2. Improve an existing taxonomy or pattern chapter.
3. Add a diagram that clarifies a design trade-off.
4. Tighten wording where content is correct but too verbose.

