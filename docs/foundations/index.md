# Foundations of LLM System Design

This section covers the design lenses that apply across the rest of the book. The goal is not to repeat generic AI advice. It is to make the cross-cutting decisions visible before readers dive into specific system archetypes.

## In this section

- [System Boundaries](system-boundaries.md) explains where an LLM system starts and ends, and why most design mistakes come from drawing that boundary badly.
- [Control Surfaces](control-surfaces.md) makes the operational layer explicit: identity, policy, tracing, evaluation, and change control.
- [Retrieval Foundations](retrieval-foundations.md) covers the retrieval stack, hybrid search, permissions, and grounded answers.
- [Agent Foundations](agent-foundations.md) defines when agentic architecture is justified and where it fails.

## Why start here

The same failure patterns reappear across platform infra, retrieval systems, agents, and vertical applications:

- The model is treated as the system instead of one component
- Control paths are added after launch instead of designed up front
- Reliability and governance are discussed only after the feature shape is fixed

These chapters give the rest of the book a shared vocabulary.
