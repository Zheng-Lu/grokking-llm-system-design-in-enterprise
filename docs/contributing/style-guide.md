# Style Guide

## Core principles

Write for readers who want technical signal fast.

Every chapter should be:

- Concise
- Structured
- Technically precise
- Evidence-driven
- Useful to someone designing a similar system

## Tone

- Prefer direct statements over hype.
- Use plain technical language.
- Avoid marketing adjectives unless you are quoting a source.
- Keep sentences short when the concept is already complex.

## Structure

A good chapter usually moves in this order:

1. define the problem and requirements
2. show the architecture and request flow
3. explain the components and operating constraints
4. make trade-offs and failure modes explicit
5. close with governance and interview discussion points if useful

Do not bury the design problem under long company background sections.

## Evidence and sourcing

- Prefer primary sources when possible.
- Attribute claims that are company-specific, quantitative, or operationally important.
- If you infer a design choice from public material, label it as inference.
- If you are not sure, leave an open question instead of overstating confidence.

## Writing rules

- One section should solve one reader question.
- Prefer bullets and short tables when they improve scanability.
- Use diagrams to clarify structure, not to decorate pages.
- Keep headings short and specific.
- Define acronyms the first time they matter.

## Enterprise framing

Enterprise chapters should explicitly consider:

- Data boundaries
- Identity and authorization
- Latency and cost
- Observability
- Evaluation
- Operational ownership

If those concerns are absent, the chapter is probably still too close to a demo mindset.

## Examples and diagrams

- Keep examples small and representative.
- Prefer Mermaid for simple architecture or sequence diagrams.
- If a richer diagram is necessary, commit the editable source in `docs/assets/diagrams/`.

## Editing discipline

- Trim repetition aggressively.
- Remove filler before adding explanation.
- Rewrite vague claims into concrete system design statements.
- If a paragraph has no design consequence, it probably does not belong.
