# Application Patterns

LLM applications are the user-facing layer of the stack: assistants, copilots, shopping guides, workflow helpers, and domain-specific operators. This layer is where technical quality meets user trust.

## What defines an application chapter

An application chapter should explain:

- who the user is and what job they need to get done
- which lower-level systems the product depends on
- what remains deterministic and what is model-driven
- how the interface exposes evidence, uncertainty, and escalation

## Shared architecture concerns

Most vertical applications combine:

1. interaction model and UX state
2. context assembly or retrieval
3. model or model-router invocation
4. safety and policy controls
5. feedback, analytics, and quality review

## Typical application mistakes

- treating every task as if it belongs in one generic chat box
- hiding the difference between grounded answers and open-ended generation
- shipping without explicit fallback behavior when the model is wrong
- optimizing surface polish before the control layer is ready

## How to read the next chapters

Use the vertical application chapters as synthesis exercises. Each one should make clear which patterns come from platform infra, retrieval, agents, or model lifecycle rather than presenting the final product as if it were a single feature.
