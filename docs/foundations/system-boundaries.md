# System Boundaries

Most weak LLM system designs start by confusing the model with the system. In practice, the interesting design work lives in the layers around the model: context assembly, policy checks, routing, tool boundaries, feedback capture, and rollback.

## What belongs inside the boundary

For this book, an LLM system usually includes:

- the user or upstream interface
- context assembly and retrieval
- model invocation and provider routing
- post-processing and action handling
- policy, approval, and safety controls
- tracing, evaluation, and operational ownership

If a proposal only describes prompts and models, the system boundary is too small.

## Questions to answer early

- Is the primary job retrieval, generation, planning, action execution, or a mix?
- Which steps must remain deterministic?
- What data enters prompts, and under which identity?
- Which outputs are advisory, and which can trigger real actions?
- Where does the team observe regressions before users do?

## A useful decomposition

Most production systems can be understood as four planes:

1. interface plane: where users or services interact with the system
2. reasoning plane: retrieval, planning, ranking, and model calls
3. control plane: policy, evaluation, approvals, and configuration
4. operations plane: tracing, incident response, rollbacks, and ownership

This decomposition is more useful than asking whether a system is "just chat" or "an agent."

## Common boundary mistakes

- hiding retrieval and permission logic inside application code
- letting tool-use decisions bypass the policy layer
- treating evaluations as an afterthought instead of a release gate
- assuming one generic assistant can own every workflow equally well

## Reading consequence

The rest of the book groups chapters by system archetype, but the same boundary questions apply in every section. Readers should keep returning to them when a design starts to look simpler on paper than it would be in production.
