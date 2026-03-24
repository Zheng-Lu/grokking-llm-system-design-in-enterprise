# Design a NotebookLM-Style Research Workspace

A NotebookLM-style system is a retrieval workspace centered on a bounded set of user-selected sources. It is less about searching a global enterprise corpus and more about helping a reader explore, synthesize, and reason over the materials inside one notebook.

## Problem framing

The system must let a user assemble a working set of sources, ask grounded questions about them, generate notes or summaries, and keep the answer path tied to notebook-specific evidence.

## Functional requirements

- create notebooks or workspaces with explicit source collections
- ingest documents, notes, transcripts, or links into a workspace
- answer questions only from the notebook's source set
- generate citations, outlines, summaries, or notes linked to evidence
- preserve notebook state across sessions

## Non-functional requirements

- workspace isolation so one notebook does not leak into another
- interactive latency while handling multi-document synthesis
- support for heterogeneous document formats
- traceability from note or answer back to source passages
- manageable storage and reindex costs as notebooks accumulate

## High-level architecture

- notebook service that owns workspace metadata
- source ingestion and parsing pipeline
- per-workspace or logically partitioned retrieval index
- synthesis layer for notes, answers, and cross-document summaries
- citation and provenance renderer

## Core components

- workspace metadata store
- source parser and chunker
- retrieval service scoped to notebook boundaries
- prompt/context builder for question answering and note generation
- note artifact store
- trace and feedback pipeline

## Data flow / request flow

1. A user creates a notebook and attaches a set of sources.
2. The system parses, chunks, and indexes those sources with notebook-specific metadata.
3. A question or note request triggers retrieval only within that notebook's source set.
4. The model synthesizes an answer, outline, or note with citations back to notebook evidence.
5. The generated artifact and its provenance are stored for later review or editing.

## Scaling and reliability

- partition storage and retrieval by workspace to preserve isolation and manage growth
- support incremental reindexing when a notebook changes instead of rebuilding everything
- cache stable parsing artifacts more aggressively than answer results
- keep provenance durable so notebooks remain trustworthy over time

## Trade-offs

- notebook-scoped retrieval improves relevance but reduces reuse across notebooks
- richer note generation helps usability but increases the chance of unsupported synthesis
- per-workspace indexing improves isolation but can increase operational overhead
- long-context summarization reduces retrieval hops but can hide which sources really mattered

## Failure modes

- answers that accidentally mix notebook content with unrelated global context
- broken provenance links that weaken user trust
- source parsing failures that silently exclude important evidence
- notebooks becoming too large for the intended interactive experience

## Security / safety / governance

- keep workspace access aligned to notebook ownership and sharing rules
- track which sources were visible when a note or answer was generated
- prevent notebook imports from bypassing enterprise content controls
- make retention rules explicit for uploaded or attached documents

## Interview discussion points

- Would you use one global index or notebook-scoped indexes?
- How do you preserve provenance for generated notes?
- When is long-context inference enough, and when do you still need retrieval?
- How would you debug a user complaint that a notebook answer used the wrong source?
