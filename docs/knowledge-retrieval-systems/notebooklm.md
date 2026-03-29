# Design a NotebookLM-Style Research Workspace

A NotebookLM-style system is a retrieval workspace centered on a bounded set of user-selected sources. It is less about searching a global enterprise corpus and more about helping a reader explore, synthesize, and reason over the materials inside one notebook.

## Problem framing

The system must let a user assemble a working set of sources, ask grounded questions about them, generate notes or summaries, and keep the answer path tied to notebook-specific evidence.

## Functional requirements

- Create notebooks or workspaces with explicit source collections
- Ingest documents, notes, transcripts, or links into a workspace
- Answer questions only from the notebook's source set
- Generate citations, outlines, summaries, or notes linked to evidence
- Preserve notebook state across sessions

## Non-functional requirements

- Workspace isolation so one notebook does not leak into another
- Interactive latency while handling multi-document synthesis
- Support for heterogeneous document formats
- Traceability from note or answer back to source passages
- Manageable storage and reindex costs as notebooks accumulate

## High-level architecture

- Notebook service that owns workspace metadata
- Source ingestion and parsing pipeline
- Per-workspace or logically partitioned retrieval index
- Synthesis layer for notes, answers, and cross-document summaries
- Citation and provenance renderer

## Core components

- Workspace metadata store
- Source parser and chunker
- Retrieval service scoped to notebook boundaries
- Prompt/context builder for question answering and note generation
- Note artifact store
- Trace and feedback pipeline

## Data flow / request flow

1. A user creates a notebook and attaches a set of sources.
2. The system parses, chunks, and indexes those sources with notebook-specific metadata.
3. A question or note request triggers retrieval only within that notebook's source set.
4. The model synthesizes an answer, outline, or note with citations back to notebook evidence.
5. The generated artifact and its provenance are stored for later review or editing.

## Scaling and reliability

- Partition storage and retrieval by workspace to preserve isolation and manage growth
- Support incremental reindexing when a notebook changes instead of rebuilding everything
- Cache stable parsing artifacts more aggressively than answer results
- Keep provenance durable so notebooks remain trustworthy over time

## Trade-offs

- Notebook-scoped retrieval improves relevance but reduces reuse across notebooks
- Richer note generation helps usability but increases the chance of unsupported synthesis
- Per-workspace indexing improves isolation but can increase operational overhead
- Long-context summarization reduces retrieval hops but can hide which sources really mattered

## Failure modes

- Answers that accidentally mix notebook content with unrelated global context
- Broken provenance links that weaken user trust
- Source parsing failures that silently exclude important evidence
- Notebooks becoming too large for the intended interactive experience

## Security / safety / governance

- Keep workspace access aligned to notebook ownership and sharing rules
- Track which sources were visible when a note or answer was generated
- Prevent notebook imports from bypassing enterprise content controls
- Make retention rules explicit for uploaded or attached documents

## Interview discussion points

- Would you use one global index or notebook-scoped indexes?
- How do you preserve provenance for generated notes?
- When is long-context inference enough, and when do you still need retrieval?
- How would you debug a user complaint that a notebook answer used the wrong source?
