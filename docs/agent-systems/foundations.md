# Agent Foundations

An agent is useful when the system needs to reason over multiple steps, use tools, manage state, or adapt its plan based on intermediate results. In enterprise settings, the hard part is not making an agent act. It is making it act within safe, observable, and governable boundaries.

## When agentic design is justified

Agents are most useful when:

- the task requires decomposition
- the system must choose among tools dynamically
- intermediate failures should change the next step
- the user benefits from supervised autonomy rather than one-shot answers

If the workflow is stable, deterministic, and high risk, a conventional orchestrated system may be better.

## Key building blocks

- planning or task decomposition
- tool registry and contract definitions
- memory or state handling
- policy checks and approval gates
- execution traces and debugging support

## Enterprise-specific concerns

- who owns the tools the agent can call
- which actions require human approval
- how retries and loops are bounded
- how prompt injection or malicious tool outputs are contained
- how failures are attributed across model, tool, and orchestration layers

## Common mistakes

- using multiple agents where one orchestrator would do
- allowing tool calls without stable schemas
- hiding execution traces from operators
- equating autonomy with product quality

## A useful mental model

Treat agents as controlled workflow systems with probabilistic planning, not as magic autonomous employees.
