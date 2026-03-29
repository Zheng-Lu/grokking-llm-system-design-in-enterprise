# Chapter Template

!!! note "How to use this template"
    Use this structure for new handbook chapters. If the page is also a case study, keep the same architecture but add explicit sources and clearly label any inference.

## Standard system design chapter

### 1. Problem framing

- What is the system trying to do?
- Who are the users or upstream teams?
- Why is this problem worth solving as a system, not a prompt demo?

### 2. Functional requirements

- What the system must do for readers or users
- What interfaces or workflows it must support
- What outputs, actions, or feedback loops it must produce

### 3. Non-functional requirements

- Latency, throughput, and cost expectations
- Reliability and rollback expectations
- Observability, auditability, and compliance constraints
- Multi-tenant or permission boundaries if relevant

### 4. High-level architecture

Describe the end-to-end system shape. A diagram is useful if the flow is not obvious from text alone.

### 5. Core components

List the major services, stores, pipelines, and control points. Keep the components distinct enough that a reader could sketch the system quickly.

### 6. Data flow or request flow

Explain the path through the system step by step:

- Ingestion or input capture
- Retrieval, planning, or routing
- Model invocation
- Post-processing, policy checks, or action execution
- Logging, feedback, and evaluation loops

### 7. Scaling and reliability

Surface the engineering mechanics that keep the system useful under load:

- Batching, caching, sharding, or backpressure
- Retries, idempotency, and dead-letter handling
- Fallbacks, rollbacks, and operational ownership

### 8. Trade-offs

Document what the design gains and what it gives up. Good trade-off sections usually cover:

- Latency versus quality
- Flexibility versus control
- Centralization versus team autonomy
- Precision versus recall
- Autonomy versus reliability

### 9. Failure modes

List the ways the system can still fail in practice:

- Stale or incorrect context
- Missing permissions or overbroad access
- Weak tool contracts
- Evaluator blind spots
- Hidden operator toil

### 10. Security, safety, and governance

Make the control layer explicit:

- Identity and authorization
- Prompt or tool safety boundaries
- Audit and incident review
- Who approves high-risk changes or actions

### 11. Interview discussion points

Compress the chapter into an interview-friendly version:

- What the interviewer asks
- What a strong answer should cover
- What weak answers usually miss

## Case study addendum

If the chapter is based on a public system, add:

### One-line summary

State the core design lesson in one sentence.

### Sources

List the sources that support the chapter. Recommended format:

- Source title
- Source type
- What claim or section it supports
