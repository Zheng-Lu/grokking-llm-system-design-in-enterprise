# Knowledge Retrieval Systems

Knowledge retrieval systems are the default enterprise LLM pattern because most useful answers depend on current, permissioned, and organization-specific information. The hard part is not "adding a vector database." It is building retrieval that stays grounded, authorized, and measurable.

## In this section

- [Retrieval Foundations](../foundations/retrieval-foundations.md) explains the retrieval stack, hybrid search, permissions, citations, and freshness.
- [Design RAG System](rag-system.md) covers the broad enterprise knowledge assistant archetype.
- [Design a Domain-Specific Q&A Bot](domain-specific-q-and-a-bot.md) narrows the problem to a high-precision assistant for one corpus or business domain.
- [Design a NotebookLM-Style Research Workspace](notebooklm.md) covers notebook-centric retrieval over a bounded source set.
- [Microsoft Ask Learn](microsoft-ask-learn.md) is a starter case study placed inside the retrieval section because that is where readers will look for it.

## Section lens

Retrieval chapters should make four things explicit:

- What knowledge can enter the answer path
- How permissions and freshness are enforced
- How retrieval quality is measured separately from answer quality
- How users can see the evidence behind an answer
