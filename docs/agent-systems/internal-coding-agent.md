# Design an Internal Coding Agent

This chapter intentionally merges two commonly duplicated prompts: "design a coding assistant AI agent for internal users" and "design an internal coding agent." In practice they are the same system archetype with different autonomy settings, tool scopes, and review policies.

## Problem framing

The system must help internal engineers understand repositories, propose code changes, run bounded tooling, and escalate risky actions without turning repository access into an ungoverned autonomous workflow.

## Functional requirements

- Answer codebase questions using repository and documentation context
- Search files, symbols, and change history
- Propose edits, patches, or implementation plans
- Run bounded tools such as tests, linters, or static analysis when allowed
- Support approval checkpoints before risky writes or external actions

## Non-functional requirements

- High traceability for prompts, context, tool calls, and code changes
- Strong least-privilege boundaries for repository and runtime access
- Predictable failure handling so agents do not loop or spam tools
- Support for multiple repos, branches, and developer roles
- Latency low enough for interactive use, even if some actions remain asynchronous

## High-level architecture

- Chat or IDE integration surface
- Repository context service for search, symbols, and history
- Planning and execution orchestrator
- Sandboxed tool runner
- Policy engine for approvals, secrets, and repo permissions
- Trace and evaluation pipeline

## Core components

- Repository indexer and context retriever
- Planner or orchestrator
- Tool registry with stable contracts
- Sandbox execution environment
- Diff generation and review handoff
- Policy, audit, and trace pipeline

## Data flow / request flow

1. A user asks for analysis, code changes, or task execution.
2. The system retrieves repository context, ownership signals, and relevant docs.
3. The planner proposes a workflow and chooses bounded tools.
4. Tool outputs are validated, summarized, and fed back into the next step.
5. Proposed diffs, test results, and trace metadata are shown to the user for review or approval.

## Scaling and reliability

- Keep repository indexing and retrieval separate from live execution
- Bound loops, retries, and tool budgets so the system cannot thrash
- Use deterministic wrappers around risky tools where possible
- Preserve execution traces so regressions can be replayed and reviewed
- Separate read-only assistance from write-capable agent modes

## Trade-offs

- More autonomy reduces manual toil but raises review and safety requirements
- Richer repository context improves quality but can increase latency and prompt size
- Direct tool execution improves usefulness but expands the attack surface
- One general coding agent is simpler to discover but harder to tune across very different workflows

## Failure modes

- Context retrieval misses the files that actually matter
- Tool outputs are accepted without schema or sanity checks
- The agent loops on the same failing action
- Repository writes happen without enough human review or ownership awareness

## Security / safety / governance

- Keep repository, secret, and runtime access scoped to the user and task
- Require explicit approval for writes, external network actions, or privileged commands
- Store enough audit detail to reconstruct why a change was proposed or applied
- Defend against prompt injection from repository content and tool output

## Interview discussion points

- Where do you separate assistant mode from higher-autonomy agent mode?
- Which tools can the agent call directly, and which require approval?
- How would you sandbox execution?
- What traces would you need to debug a bad code change proposal?
