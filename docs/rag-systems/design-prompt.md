# Design Prompt: RAG System

This prompt narrows the focus to retrieval quality, grounding, and data operations.

## Prompt

Design a retrieval-augmented question answering system for enterprise documentation that serves both exact technical lookups and broader conceptual questions.

## System sketch

```mermaid
flowchart LR
  A[Source systems] --> B[Ingestion and normalization]
  B --> C[Indexing and metadata]
  D[User query] --> E[Query understanding]
  E --> F[Retriever and reranker]
  C --> F
  F --> G[Grounded generation]
  G --> H[Answer with citations]
  H --> I[Feedback and evals]
```

## What a strong answer should cover

=== "Candidate view"
    Focus on:

    - chunking and metadata strategy
    - lexical plus semantic retrieval when query patterns demand it
    - permission-aware filtering
    - citation-grounded generation
    - retrieval and answer quality metrics
    - freshness and reindexing strategy

=== "Reviewer view"
    Strong candidates usually separate:

    - ingestion failures from retrieval failures
    - retrieval failures from generation failures
    - latency optimizations from quality optimizations

## Trade-offs worth calling out

- smaller chunks improve precision but can lose context
- larger chunks preserve meaning but hurt recall and latency
- query-time permission checks improve freshness but add complexity
- hybrid retrieval improves coverage but increases tuning overhead

## Red flags

- "vector DB" presented as the whole design
- no discussion of document updates or deletions
- no evaluation plan beyond user thumbs up or down
- no answer citations
