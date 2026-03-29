# Design RAG System

A RAG system is the broad enterprise knowledge assistant archetype: one system that answers questions over changing, permissioned, organization-specific content while keeping responses grounded in retrieved evidence.

## Problem framing

The system must answer questions across multiple corpora without pretending that all knowledge is equally visible, current, or reliable.

## Functional requirements

- Support question answering and optional multi-turn follow-up
- Grounded answers over internal documentation, policies, and process content
- Citations or evidence links for trust and review
- Identity-aware access to corpora and snippets
- Feedback capture for bad answers, missing context, or stale content

## Non-functional requirements

- Interactive latency that fits real user workflows
- High trust through clear evidence and consistent access control
- Observability across retrieval, answer generation, and user feedback
- Freshness handling for changing documentation and policy content
- Controlled blast radius when prompts or models change

## High-level architecture

- Chat, search, or API interface
- Identity and authorization service
- Retrieval layer over indexed enterprise content
- LLM gateway for routing, policy, and tracing
- Answer renderer with citations, confidence signals, and feedback capture

## Core components

- Ingestion and indexing pipeline for enterprise content
- Hybrid retriever plus optional reranker
- Conversation state or session context manager
- Permission resolution and filtering layer
- Answer synthesis layer
- Evaluation and observability pipeline

## Data flow / request flow

1. A user submits a question with identity and session context.
2. The system resolves which corpora and snippets the user may access.
3. Retrieval gathers grounded evidence using lexical, semantic, and metadata signals.
4. The answer layer synthesizes a response from permitted evidence and attaches citations.
5. Feedback, traces, and low-confidence signals flow into the evaluation system.

## Scaling and reliability

- Isolate slow ingestion from the online retrieval path
- Keep session state lightweight so serving remains mostly stateless
- Separate retrieval failures from generation failures in traces and dashboards
- Use rollbacks and eval gates when prompt, ranking, or model changes ship

## Trade-offs

- One broad assistant improves discoverability but can blur task boundaries
- Richer context improves quality but increases latency and cost
- Stricter permission checks improve safety but complicate caching and ranking
- Concise answers feel fast but may hide the evidence users need to trust the result

## Failure modes

- Broad answers that look plausible but are weakly grounded
- Hidden permission leaks through citations, logs, or cached retrieval results
- Stale content outranking current guidance
- User trust erosion when the system does not expose uncertainty clearly

## Security / safety / governance

- Align retrieval access with source-system permissions
- Classify sensitive corpora before they reach prompts
- Keep a traceable path from answer to evidence to prompt/model version
- Require explicit review for prompt, ranking, or policy changes that affect many users

## Interview discussion points

- Where should permission checks happen in the retrieval flow?
- When is hybrid retrieval necessary?
- How would you measure retrieval quality separately from answer quality?
- What should the system do when it cannot ground an answer confidently?
