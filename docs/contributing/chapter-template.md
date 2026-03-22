# Chapter Template

!!! note "How to use this template"
    Copy this structure when creating a new case study. Replace prompts with sourced content. If a section depends on inference, label it clearly instead of presenting it as fact.

## 1. One-line summary

State the core design lesson in one sentence.

Example prompt:

`[Company/system]` shows how to build `[system type]` under `[enterprise constraint]` by combining `[key design moves]`.

## 2. Problem

Describe the real problem the system needed to solve.

Cover:

- users
- jobs to be done
- enterprise constraints
- why the problem mattered enough to justify the system

## 3. Why naive solutions fail

Explain what breaks with the obvious approach.

Typical failure modes:

- hallucinated answers
- bad retrieval quality
- stale knowledge
- permission leaks
- latency spikes
- cost blowups
- weak evaluation

## 4. Architecture

Describe the end-to-end flow:

- ingestion
- indexing or memory
- retrieval or planning
- model invocation
- tool use
- guardrails
- feedback loops

Add a diagram if the architecture cannot be understood quickly from text alone.

## 5. Key design choices

List the highest-leverage decisions.

Examples:

- why a gateway exists
- why hybrid retrieval was chosen
- where authorization is enforced
- why a human approval step remains in the loop

## 6. Trade-offs

Document what the architecture gains and what it gives up.

Good trade-off sections mention:

- quality versus latency
- precision versus recall
- flexibility versus control
- autonomy versus reliability
- centralization versus team-level speed

## 7. Reusable patterns

Name the patterns other teams can adopt.

Each pattern should be stated independently from the company-specific details.

## 8. Failure modes

List the ways the system can still fail in practice.

Examples:

- permission drift
- retrieval overfetch
- evaluator blind spots
- prompt regressions
- broken tool contracts
- weak human escalation paths

## 9. Interview version

Compress the case into a system design interview prompt:

- what the interviewer asks
- what components a strong answer should cover
- what weak answers usually miss

## 10. Sources

List the sources that support the chapter.

Recommended format:

- source title
- source type
- what claim or section it supports

