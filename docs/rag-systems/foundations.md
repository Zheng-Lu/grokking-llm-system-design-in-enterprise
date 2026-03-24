# RAG Foundations

Retrieval-augmented generation is the default pattern for enterprise knowledge use because raw model memory is rarely enough. The real system design work is not "adding a vector database." It is making retrieval reliable under real document, identity, and freshness constraints.

## The enterprise RAG problem

Enterprise knowledge is:

- scattered across systems
- permissioned unevenly
- updated continuously
- inconsistent in format and quality

A good RAG system has to decide what to ingest, how to normalize it, how to segment it, how to retrieve it, and how to keep answers grounded without leaking data.

## Core components

- ingestion and normalization
- chunking and metadata design
- embeddings or sparse indexes
- retrieval and ranking
- authorization-aware filtering
- answer synthesis with citations or evidence

## Design questions that matter

- Should permission checks happen at index time, query time, or both?
- How much document structure should survive chunking?
- Is pure vector retrieval good enough for the query mix?
- How will freshness and deletion propagate through the index?
- What metrics distinguish retrieval failure from generation failure?

## Common enterprise failure modes

- chunks that are too small to preserve meaning
- chunks that are too large to retrieve precisely
- retrieval quality degrading for exact-match or acronym-heavy queries
- access control enforced only after retrieval
- no offline evaluation set for search quality changes

## Strong chapters on RAG should explain

- the retrieval stack
- where permissions are enforced
- how citations or evidence are surfaced
- how quality is measured over time
