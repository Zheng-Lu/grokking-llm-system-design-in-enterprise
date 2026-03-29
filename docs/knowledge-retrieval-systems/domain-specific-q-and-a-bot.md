# Design a Domain-Specific Q&A Bot

A domain-specific Q&A bot serves one corpus or business domain with a narrower user intent space than a general internal assistant. The smaller scope usually raises the precision bar instead of making the problem trivial.

## Problem framing

The system must answer high-value questions in one domain, such as legal policy, product support, medical reference, or internal engineering docs, where errors are costly and readers expect precise grounding.

## Functional requirements

- Answer questions over a clearly bounded corpus
- Support exact lookups as well as conceptual questions
- Attach citations to the relevant source passages
- Collect feedback on missing or incorrect answers
- Expose enough metadata for reviewers to inspect retrieval quality

## Non-functional requirements

- High precision on the domain's critical queries
- Strong freshness guarantees if the corpus changes frequently
- Explainability for reviewers and subject-matter experts
- Support for domain-specific terminology, acronyms, and identifiers
- Predictable latency for interactive use

## High-level architecture

- Ingestion pipeline tuned to the domain corpus
- Retrieval stack with lexical and semantic search
- Reranking tuned to domain-specific relevance
- Grounded answer generation with citation rendering
- Evaluation pipeline with domain-focused golden sets

## Core components

- Corpus normalizer and metadata extractor
- Hybrid retriever
- Optional domain-specific query understanding
- Answer synthesis layer
- Domain review workflow for difficult or high-risk queries
- Evaluation harness with representative query sets

## Data flow / request flow

1. Source content is normalized, chunked, and indexed with useful domain metadata.
2. A user query is analyzed for exact identifiers, concepts, and filters.
3. Retrieval combines lexical and semantic signals, then reranks candidates.
4. The model answers only from retrieved evidence and returns citations.
5. Feedback and reviewer corrections feed future eval sets and ranking adjustments.

## Scaling and reliability

- Keep domain metadata rich enough that retrieval can use filters before ranking
- Build golden queries for exact-match and acronym-heavy lookups
- Separate ingestion freshness issues from ranking issues in diagnostics
- Preserve source version information so content changes are auditable

## Trade-offs

- Narrow scope improves precision but limits reuse across teams
- Domain-specific ranking improves quality but increases maintenance
- Stronger review workflows improve trust but slow iteration
- Answer synthesis improves readability but introduces another failure layer beyond retrieval

## Failure modes

- Lexical edge cases missed by overly semantic retrieval
- Domain synonyms or acronyms that degrade recall
- Stale content remaining in the index after source changes
- Reviewers relying on answer quality alone instead of inspecting retrieval coverage

## Security / safety / governance

- Reflect the domain's review and approval rules in the release process
- Keep source citations visible for subject-matter review
- Classify high-risk content paths before they can enter prompts
- Make escalation paths explicit when the system should defer to a human expert

## Interview discussion points

- How would you tune for both exact lookups and conceptual queries?
- What data would you need to debug a retrieval failure?
- When should a human reviewer stay in the loop?
- How would you measure freshness and citation quality?
