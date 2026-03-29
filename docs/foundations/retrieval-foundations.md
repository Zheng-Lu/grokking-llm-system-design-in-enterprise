# Retrieval Foundations

Retrieval-augmented generation is the dominant pattern for enterprise knowledge use because raw model memory is rarely enough. The design work is in corpus shaping, permissions, ranking, freshness, and evidence presentation.

## The retrieval stack

A practical enterprise retrieval stack usually includes:

- Ingestion and normalization
- Chunking and metadata design
- Dense and or sparse retrieval indexes
- Reranking or rank fusion
- Permission-aware filtering
- Grounded answer synthesis with citations

## Design choices that matter

### Chunking and metadata

Chunk size, overlap, and metadata design determine whether the system retrieves coherent evidence or noisy fragments.

### Hybrid retrieval

Dense retrieval handles paraphrase well. Sparse retrieval handles exact strings, acronyms, and identifiers well. Most technical corpora benefit from both.

### Permission-aware retrieval

Authorization must happen before or during retrieval, not only after answer generation. Otherwise sensitive chunks can leak into candidate sets, logs, or citations.

### Freshness and deletion

Indexes must reflect document updates, deletions, and permission changes quickly enough that users do not lose trust.

### Evidence and evaluation

Good systems separate retrieval metrics from generation metrics and show users the evidence behind answers.

## Common enterprise failure modes

- Chunks too small to preserve meaning
- Chunks too large to retrieve precisely
- Exact-match queries that fail under pure dense retrieval
- Stale ACL snapshots or identity-unaware caches
- Answer evaluations that hide retrieval regressions

## How the rest of this section uses these ideas

- [Design RAG System](../knowledge-retrieval-systems/rag-system.md) broadens the retrieval problem across many corpora and user roles.
- [Domain-Specific Q&A Bot](../knowledge-retrieval-systems/domain-specific-q-and-a-bot.md) narrows the domain but raises the precision bar.
- [NotebookLM-Style Research Workspace](../knowledge-retrieval-systems/notebooklm.md) adds per-workspace sources and citation-heavy synthesis.
