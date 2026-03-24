# Hybrid Retrieval

Hybrid retrieval combines dense semantic search with sparse or keyword-driven retrieval. It is one of the most common enterprise upgrades after teams discover that pure vector search is not robust enough.

## When it helps

Hybrid retrieval is useful when the corpus includes:

- product names and exact identifiers
- acronyms and specialized jargon
- mixed structured and unstructured content
- queries that alternate between semantic intent and exact lookup

## Typical architecture

- dense index for semantic similarity
- sparse or lexical index for exact-match recall
- rank fusion or reranking stage
- optional metadata filters before final selection

## Why it works

Dense retrieval is good at paraphrase and semantic similarity. Sparse retrieval is good at exact strings, abbreviations, and rare terms. Hybrid systems improve recall by letting each method cover the other's blind spots.

## Trade-offs

- more infrastructure to operate
- more tuning surfaces
- more evaluation work to understand why ranking changed

## Failure modes

- unstable rank fusion logic
- weak query analysis that routes everything the same way
- evaluation that measures answer quality but not retrieval contribution
