# Design an AI-Based Shopping Chatbot

A shopping chatbot is a vertical application that mixes product discovery, retrieval over catalog data, recommendation logic, and transactional safety boundaries. It is a good example of why user-facing polish is not enough without clean system structure underneath.

## Problem framing

The system must help users discover products, compare options, and answer shopping questions without confusing grounded catalog facts with speculative generation.

## Functional requirements

- Answer product questions using catalog and policy data
- Support conversational product discovery and narrowing
- Explain or compare options using grounded attributes
- Hand off to deterministic checkout or cart flows instead of improvising transactional logic
- Capture feedback on bad recommendations or unsupported answers

## Non-functional requirements

- Low interactive latency
- High accuracy for price, inventory, and policy-sensitive claims
- Support for rapid catalog updates
- Traceability for recommendation and merchandising decisions
- Clear separation between advice, promotion, and transactional actions

## High-level architecture

- Chat or shopping assistant interface
- Product catalog retrieval layer
- Recommendation and ranking service
- LLM gateway for generation and summarization
- Deterministic commerce services for cart, checkout, and account actions
- Feedback and experimentation pipeline

## Core components

- Catalog ingestion and indexing pipeline
- Attribute-aware retrieval and ranking
- Prompt/context builder that pulls grounded product facts
- Policy checks for pricing, promotions, and unsupported claims
- Transactional service adapters
- Quality and experiment monitoring

## Data flow / request flow

1. A shopper asks a product question or describes intent.
2. Retrieval and ranking gather relevant products, attributes, reviews, or policy snippets.
3. The model generates a grounded response or comparison from those facts.
4. If the user wants to take action, the system hands off to deterministic commerce APIs.
5. Feedback and conversion signals feed ranking, prompt, and policy tuning.

## Scaling and reliability

- Keep catalog freshness independent from model rollout cadence
- Separate recommendation ranking failures from generation failures
- Protect commerce APIs from chat-driven request spikes
- Degrade to search or filtered catalog views when generation is unavailable

## Trade-offs

- Richer conversational help improves discovery but can blur into unsupported sales claims
- Tightly grounded answers improve trust but may feel less flexible
- One assistant simplifies the experience but can overload one interface with very different jobs
- Aggressive personalization may improve conversion but increase privacy and governance burden

## Failure modes

- Hallucinated product claims or compatibility guidance
- Stale pricing or inventory in the answer path
- Recommendations that optimize engagement over user fit
- Chat flows that attempt to improvise transactional steps instead of handing off cleanly

## Security / safety / governance

- Keep transactional actions deterministic and explicitly authorized
- Enforce policy around pricing, regulated products, and promotional claims
- Scope personalization and customer data use to the allowed privacy boundary
- Retain enough traces to investigate unsafe or misleading recommendations

## Interview discussion points

- Which parts of the flow should remain deterministic?
- How would you separate catalog retrieval from recommendation logic?
- What signals tell you the chatbot is useful rather than merely engaging?
- Where do safety and policy checks need to sit in the request path?
