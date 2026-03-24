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

- latency, throughput, and cost expectations
- reliability and rollback expectations
- observability, auditability, and compliance constraints
- multi-tenant or permission boundaries if relevant

### 4. High-level architecture

Describe the end-to-end system shape. A diagram is useful if the flow is not obvious from text alone.

### 5. Core components

List the major services, stores, pipelines, and control points. Keep the components distinct enough that a reader could sketch the system quickly.

### 6. Data flow or request flow

Explain the path through the system step by step:

- ingestion or input capture
- retrieval, planning, or routing
- model invocation
- post-processing, policy checks, or action execution
- logging, feedback, and evaluation loops

### 7. Scaling and reliability

Surface the engineering mechanics that keep the system useful under load:

- batching, caching, sharding, or backpressure
- retries, idempotency, and dead-letter handling
- fallbacks, rollbacks, and operational ownership

### 8. Trade-offs

Document what the design gains and what it gives up. Good trade-off sections usually cover:

- latency versus quality
- flexibility versus control
- centralization versus team autonomy
- precision versus recall
- autonomy versus reliability

### 9. Failure modes

List the ways the system can still fail in practice:

- stale or incorrect context
- missing permissions or overbroad access
- weak tool contracts
- evaluator blind spots
- hidden operator toil

### 10. Security, safety, and governance

Make the control layer explicit:

- identity and authorization
- prompt or tool safety boundaries
- audit and incident review
- who approves high-risk changes or actions

### 11. Interview discussion points

Compress the chapter into an interview-friendly version:

- what the interviewer asks
- what a strong answer should cover
- what weak answers usually miss

## Case study addendum

If the chapter is based on a public system, add:

### One-line summary

State the core design lesson in one sentence.

### Sources

List the sources that support the chapter. Recommended format:

- source title
- source type
- what claim or section it supports
