# Review Process

## Review goals

Reviews should improve:

- Technical clarity
- Structural coherence
- Source quality
- Usefulness for future readers

The target is not maximal prose polish. It is a chapter that is accurate, readable, and worth reusing.

## What reviewers check

### 1. Scope and fit

- Is the topic clearly in scope for enterprise LLM system design?
- Does the change improve the book rather than adding noise?

### 2. Structure

- Does the page follow the expected section order?
- Is the problem statement clear before architecture detail starts?

### 3. Technical quality

- Are important trade-offs explicit?
- Are enterprise constraints acknowledged?
- Are failure modes concrete rather than generic?

### 4. Evidence

- Are factual claims sourced?
- Are inferred claims marked as inference?
- Are open questions left visible instead of implied away?

### 5. Maintainability

- Is the change small enough to review?
- Does it avoid needless customization or plugin sprawl?
- Was `mkdocs.yml` updated if navigation changed?

## Suggested reviewer workflow

1. Read the chapter once for structure.
2. Read it again for technical correctness and evidence.
3. Check whether the chapter teaches reusable patterns.
4. Ask for narrowing if the change tries to cover too much at once.

## Approval standard

A chapter is ready when a reviewer can answer "yes" to these questions:

- Would a system designer learn something reusable from this page?
- Can a future contributor maintain or extend it without guessing the structure?
- Are the strongest claims supported well enough for an open-source technical book?

