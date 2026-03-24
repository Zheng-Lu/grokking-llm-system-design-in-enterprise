# Design a Domain-Specific Q&A Bot

A domain-specific Q&A bot serves one corpus or business domain with a narrower user intent space than a general internal assistant. The smaller scope usually raises the precision bar instead of making the problem trivial.

## Problem framing

The system must answer high-value questions in one domain, such as legal policy, product support, medical reference, or internal engineering docs, where errors are costly and readers expect precise grounding.

## Functional requirements

- answer questions over a clearly bounded corpus
- support exact lookups as well as conceptual questions
- attach citations to the relevant source passages
- collect feedback on missing or incorrect answers
- expose enough metadata for reviewers to inspect retrieval quality

## Non-functional requirements

- high precision on the domain's critical queries
- strong freshness guarantees if the corpus changes frequently
- explainability for reviewers and subject-matter experts
- support for domain-specific terminology, acronyms, and identifiers
- predictable latency for interactive use

## High-level architecture

- ingestion pipeline tuned to the domain corpus
- retrieval stack with lexical and semantic search
- reranking tuned to domain-specific relevance
- grounded answer generation with citation rendering
- evaluation pipeline with domain-focused golden sets

## Core components

- corpus normalizer and metadata extractor
- hybrid retriever
- optional domain-specific query understanding
- answer synthesis layer
- domain review workflow for difficult or high-risk queries
- evaluation harness with representative query sets

## Data flow / request flow

1. Source content is normalized, chunked, and indexed with useful domain metadata.
2. A user query is analyzed for exact identifiers, concepts, and filters.
3. Retrieval combines lexical and semantic signals, then reranks candidates.
4. The model answers only from retrieved evidence and returns citations.
5. Feedback and reviewer corrections feed future eval sets and ranking adjustments.

## Scaling and reliability

- keep domain metadata rich enough that retrieval can use filters before ranking
- build golden queries for exact-match and acronym-heavy lookups
- separate ingestion freshness issues from ranking issues in diagnostics
- preserve source version information so content changes are auditable

## Trade-offs

- narrow scope improves precision but limits reuse across teams
- domain-specific ranking improves quality but increases maintenance
- stronger review workflows improve trust but slow iteration
- answer synthesis improves readability but introduces another failure layer beyond retrieval

## Failure modes

- lexical edge cases missed by overly semantic retrieval
- domain synonyms or acronyms that degrade recall
- stale content remaining in the index after source changes
- reviewers relying on answer quality alone instead of inspecting retrieval coverage

## Security / safety / governance

- reflect the domain's review and approval rules in the release process
- keep source citations visible for subject-matter review
- classify high-risk content paths before they can enter prompts
- make escalation paths explicit when the system should defer to a human expert

## Interview discussion points

- How would you tune for both exact lookups and conceptual queries?
- What data would you need to debug a retrieval failure?
- When should a human reviewer stay in the loop?
- How would you measure freshness and citation quality?
