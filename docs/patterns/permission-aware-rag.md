# Permission-Aware RAG

Permission-aware RAG keeps retrieval aligned with the reader's actual access rights. In enterprise settings, this is often the difference between a usable assistant and a security incident.

## When to use it

Use this pattern when:

- documents inherit permissions from source systems
- different users should see different slices of the same corpus
- retrieval results may contain sensitive snippets even before answer generation

## Reference flow

1. ingest documents with stable identity metadata
2. preserve source-level permission context
3. resolve the user's identity at query time
4. filter or pre-scope retrieval candidates using authorization data
5. generate an answer only from permitted evidence

## Why naive RAG fails

If permissioning is checked only after retrieval or only in the UI layer, the system can still:

- retrieve unauthorized chunks
- leak sensitive snippets in citations or logs
- pollute reranking with documents the user should never have seen

## Key design choices

- whether access control is materialized into the index or joined at query time
- whether document-level permissions are enough or chunk-level permissions are needed
- how permission changes propagate into indexes and caches

## Trade-offs

- stricter enforcement can increase query latency
- index-time materialization can simplify reads but complicate updates
- query-time joins preserve freshness but increase operational complexity

## Failure modes

- stale ACL snapshots
- overbroad group membership expansion
- missing service-account boundaries during ingestion
- caches that ignore identity

