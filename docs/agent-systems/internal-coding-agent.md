# Design an Internal Coding Agent

This chapter intentionally merges two commonly duplicated prompts: "design a coding assistant AI agent for internal users" and "design an internal coding agent." In practice they are the same system archetype with different autonomy settings, tool scopes, and review policies.

## Problem framing

The system must help internal engineers understand repositories, propose code changes, run bounded tooling, and escalate risky actions without turning repository access into an ungoverned autonomous workflow.

## Functional requirements

- answer codebase questions using repository and documentation context
- search files, symbols, and change history
- propose edits, patches, or implementation plans
- run bounded tools such as tests, linters, or static analysis when allowed
- support approval checkpoints before risky writes or external actions

## Non-functional requirements

- high traceability for prompts, context, tool calls, and code changes
- strong least-privilege boundaries for repository and runtime access
- predictable failure handling so agents do not loop or spam tools
- support for multiple repos, branches, and developer roles
- latency low enough for interactive use, even if some actions remain asynchronous

## High-level architecture

- chat or IDE integration surface
- repository context service for search, symbols, and history
- planning and execution orchestrator
- sandboxed tool runner
- policy engine for approvals, secrets, and repo permissions
- trace and evaluation pipeline

## Core components

- repository indexer and context retriever
- planner or orchestrator
- tool registry with stable contracts
- sandbox execution environment
- diff generation and review handoff
- policy, audit, and trace pipeline

## Data flow / request flow

1. A user asks for analysis, code changes, or task execution.
2. The system retrieves repository context, ownership signals, and relevant docs.
3. The planner proposes a workflow and chooses bounded tools.
4. Tool outputs are validated, summarized, and fed back into the next step.
5. Proposed diffs, test results, and trace metadata are shown to the user for review or approval.

## Scaling and reliability

- keep repository indexing and retrieval separate from live execution
- bound loops, retries, and tool budgets so the system cannot thrash
- use deterministic wrappers around risky tools where possible
- preserve execution traces so regressions can be replayed and reviewed
- separate read-only assistance from write-capable agent modes

## Trade-offs

- more autonomy reduces manual toil but raises review and safety requirements
- richer repository context improves quality but can increase latency and prompt size
- direct tool execution improves usefulness but expands the attack surface
- one general coding agent is simpler to discover but harder to tune across very different workflows

## Failure modes

- context retrieval misses the files that actually matter
- tool outputs are accepted without schema or sanity checks
- the agent loops on the same failing action
- repository writes happen without enough human review or ownership awareness

## Security / safety / governance

- keep repository, secret, and runtime access scoped to the user and task
- require explicit approval for writes, external network actions, or privileged commands
- store enough audit detail to reconstruct why a change was proposed or applied
- defend against prompt injection from repository content and tool output

## Interview discussion points

- Where do you separate assistant mode from higher-autonomy agent mode?
- Which tools can the agent call directly, and which require approval?
- How would you sandbox execution?
- What traces would you need to debug a bad code change proposal?
