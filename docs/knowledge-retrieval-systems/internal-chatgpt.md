# Design an Internal ChatGPT

An internal ChatGPT is the broad enterprise knowledge assistant archetype: one interface that helps employees ask policy, product, process, and documentation questions while respecting permissions and maintaining user trust.

## Problem framing

The system must answer questions across multiple internal corpora without pretending that all knowledge is equally visible, current, or reliable.

## Functional requirements

- conversational interface for follow-up questions and multi-turn context
- grounded answers over internal documentation, policies, and process content
- citations or evidence links for trust and review
- identity-aware access to corpora and snippets
- feedback capture for bad answers, missing context, or stale content

## Non-functional requirements

- interactive latency that fits daily employee workflows
- high trust through clear evidence and consistent access control
- observability across retrieval, answer generation, and user feedback
- freshness handling for changing documentation and policy content
- controlled blast radius when prompts or models change

## High-level architecture

- chat or search UI
- identity and authorization service
- retrieval layer over indexed enterprise content
- LLM gateway for routing, policy, and tracing
- answer renderer with citations, confidence signals, and feedback capture

## Core components

- ingestion and indexing pipeline for enterprise content
- hybrid retriever plus optional reranker
- conversation state or session context manager
- permission resolution and filtering layer
- answer synthesis layer
- evaluation and observability pipeline

## Data flow / request flow

1. A user submits a question with identity and session context.
2. The system resolves which corpora and snippets the user may access.
3. Retrieval gathers grounded evidence using lexical, semantic, and metadata signals.
4. The answer layer synthesizes a response from permitted evidence and attaches citations.
5. Feedback, traces, and low-confidence signals flow into the evaluation system.

## Scaling and reliability

- isolate slow ingestion from the online retrieval path
- keep session state lightweight so serving remains mostly stateless
- separate retrieval failures from generation failures in traces and dashboards
- use rollbacks and eval gates when prompt, ranking, or model changes ship

## Trade-offs

- one broad assistant improves discoverability but can blur task boundaries
- richer context improves quality but increases latency and cost
- stricter permission checks improve safety but complicate caching and ranking
- concise answers feel fast but may hide the evidence users need to trust the result

## Failure modes

- broad answers that look plausible but are weakly grounded
- hidden permission leaks through citations, logs, or cached retrieval results
- stale content outranking current guidance
- user trust erosion when the system does not expose uncertainty clearly

## Security / safety / governance

- align retrieval access with source-system permissions
- classify sensitive corpora before they reach prompts
- keep a traceable path from answer to evidence to prompt/model version
- require explicit review for prompt, ranking, or policy changes that affect many users

## Interview discussion points

- Where should permission checks happen in the retrieval flow?
- When is hybrid retrieval necessary?
- How would you measure retrieval quality separately from answer quality?
- What should the system do when it cannot ground an answer confidently?
