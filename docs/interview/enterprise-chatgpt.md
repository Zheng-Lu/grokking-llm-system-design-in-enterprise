# Enterprise ChatGPT

This interview prompt tests whether a candidate can design a general internal assistant without collapsing into hand-wavy "just call an API" answers.

## Prompt

Design an internal enterprise assistant that helps employees answer policy, product, and process questions, while respecting permissions and keeping an audit trail.

## What a strong answer should cover

=== "Candidate view"
    A strong solution should discuss:

    - identity-aware retrieval or knowledge access
    - an LLM gateway or platform layer
    - conversation context management
    - citations and user trust signals
    - logging, evaluation, and feedback loops
    - escalation paths for ambiguous or high-risk requests

=== "Reviewer view"
    A strong candidate usually:

    - clarifies the highest-value use cases first
    - distinguishes grounded answers from open-ended generation
    - places authorization before or during retrieval
    - adds observability and release controls instead of focusing only on prompts
    - explains what should remain deterministic

## Target architecture

- UI layer for search, chat, and feedback
- identity service for user context and authorization
- retrieval service over indexed enterprise knowledge
- LLM gateway for routing, policy, and tracing
- evaluation pipeline that turns failures into test cases

## Common misses

- no distinction between public and sensitive corpora
- no citation strategy
- no rollback plan for prompt or model changes
- no operator view into low-quality answers

## Good follow-up questions

- How would you handle permission changes?
- When would you use hybrid retrieval?
- What metrics would block a release?
- Which actions, if any, require human approval?

