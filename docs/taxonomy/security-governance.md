# Security and Governance

Security and governance are not bolt-on controls for enterprise LLM systems. They shape the architecture from the start because the system handles data, automation, and probabilistic behavior at the same time.

## Core control surfaces

- identity and authorization
- data classification
- secret and credential handling
- content filtering and policy enforcement
- logging and audit trails
- approval workflows for high-risk actions

## Security questions every chapter should surface

- What data can enter prompts?
- What retrieval paths exist, and who can use them?
- Which tools can take external action?
- How is prompt injection handled?
- What logs are kept, and who can inspect them?

## Governance questions

- Who owns prompt and policy changes?
- What review is required before a model or workflow change ships?
- Which actions require human sign-off?
- How are incidents investigated and remediated?

## Common weak points

- permission checks that happen too late
- tool access broader than user access
- no policy layer between apps and providers
- missing audit detail for sensitive workflows
- no clear owner for evaluation regressions

## A practical stance

Good governance should make dangerous changes harder and safe iteration easier. If the process only slows teams down without improving control or visibility, the design is incomplete.

