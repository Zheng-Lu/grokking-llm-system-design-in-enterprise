# Control Surfaces

Security, safety, governance, and evaluation are not side topics. They are the control surfaces that turn a model-backed workflow into an operable system.

## The core control surfaces

- identity and authorization
- data classification and prompt boundaries
- model, prompt, and policy versioning
- tracing, logging, and audit review
- evaluations and release gates
- approval workflows for high-risk actions

## Why these surfaces matter

Without clear control points, teams accumulate the same failure pattern:

- multiple applications reach providers directly
- prompt and policy changes have no review trail
- retrieval and tool permissions drift from user permissions
- incidents are visible only as anecdotal user complaints

This makes the system hard to trust even if the user experience looks polished.

## Design questions each chapter should surface

- Which component enforces identity and authorization?
- Which changes require review before release?
- What traces exist for debugging low-quality or unsafe behavior?
- How are prompt injection, tool misuse, or data exfiltration contained?
- Who owns the rollback path when the model, prompt, or retrieval stack regresses?

## A practical stance

Good control surfaces should make safe iteration easier, not only slower. If the architecture centralizes policy but hides failure detail, or adds governance but no operational visibility, the design is incomplete.

## Where these surfaces appear in the book

- platform chapters emphasize tracing, routing, and policy enforcement
- retrieval chapters emphasize permissions, freshness, and grounded answers
- agent chapters emphasize tool boundaries, approvals, and action auditability
- model lifecycle chapters emphasize dataset lineage, evaluation, and release control
