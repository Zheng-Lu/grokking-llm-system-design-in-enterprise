# About

## Vision

**Grokking LLM System Design in Enterprise** is an open-source book for readers who want system design guidance that survives contact with production.

The project aims to document how enterprise LLM systems are actually shaped by constraints that are easy to ignore in toy examples:

- fragmented knowledge sources
- data sensitivity and access control
- latency and cost budgets
- evaluation ambiguity
- operational ownership
- governance and audit requirements

## Scope

The book focuses on public, reusable lessons in:

- enterprise assistants and copilots
- retrieval-augmented systems
- agent architectures and orchestration
- AI platform and infra patterns
- evaluation, observability, and release management
- security, risk, and governance controls

Each chapter should help readers answer not only _what_ a system looked like, but _why_ the design was chosen and what would likely break first.

## Editorial model

The repository combines three layers:

1. **Taxonomy pages** define the problem space.
2. **Pattern pages** describe reusable architecture moves.
3. **Case studies** connect public examples to concrete design decisions.

The interview track then compresses the same ideas into answerable system design prompts.

## What is out of scope

The project is not trying to be:

- a benchmark leaderboard
- a product comparison site
- a prompt library
- a research survey of every new model release

When a topic changes too quickly to stay useful, the book should prefer stable design principles over short-lived implementation detail.[^stability]

## Source philosophy

Public case studies are rarely complete. That is fine. Good chapters can still be valuable if they clearly separate:

- sourced facts
- reasoned inference
- open questions

That distinction is a core editorial rule, not a footnote.

[^stability]: Enterprise readers usually need architectures and trade-offs that remain useful after individual model versions change.

