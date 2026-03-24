# Design an AI-Based Shopping Chatbot

A shopping chatbot is a vertical application that mixes product discovery, retrieval over catalog data, recommendation logic, and transactional safety boundaries. It is a good example of why user-facing polish is not enough without clean system structure underneath.

## Problem framing

The system must help users discover products, compare options, and answer shopping questions without confusing grounded catalog facts with speculative generation.

## Functional requirements

- answer product questions using catalog and policy data
- support conversational product discovery and narrowing
- explain or compare options using grounded attributes
- hand off to deterministic checkout or cart flows instead of improvising transactional logic
- capture feedback on bad recommendations or unsupported answers

## Non-functional requirements

- low interactive latency
- high accuracy for price, inventory, and policy-sensitive claims
- support for rapid catalog updates
- traceability for recommendation and merchandising decisions
- clear separation between advice, promotion, and transactional actions

## High-level architecture

- chat or shopping assistant interface
- product catalog retrieval layer
- recommendation and ranking service
- LLM gateway for generation and summarization
- deterministic commerce services for cart, checkout, and account actions
- feedback and experimentation pipeline

## Core components

- catalog ingestion and indexing pipeline
- attribute-aware retrieval and ranking
- prompt/context builder that pulls grounded product facts
- policy checks for pricing, promotions, and unsupported claims
- transactional service adapters
- quality and experiment monitoring

## Data flow / request flow

1. A shopper asks a product question or describes intent.
2. Retrieval and ranking gather relevant products, attributes, reviews, or policy snippets.
3. The model generates a grounded response or comparison from those facts.
4. If the user wants to take action, the system hands off to deterministic commerce APIs.
5. Feedback and conversion signals feed ranking, prompt, and policy tuning.

## Scaling and reliability

- keep catalog freshness independent from model rollout cadence
- separate recommendation ranking failures from generation failures
- protect commerce APIs from chat-driven request spikes
- degrade to search or filtered catalog views when generation is unavailable

## Trade-offs

- richer conversational help improves discovery but can blur into unsupported sales claims
- tightly grounded answers improve trust but may feel less flexible
- one assistant simplifies the experience but can overload one interface with very different jobs
- aggressive personalization may improve conversion but increase privacy and governance burden

## Failure modes

- hallucinated product claims or compatibility guidance
- stale pricing or inventory in the answer path
- recommendations that optimize engagement over user fit
- chat flows that attempt to improvise transactional steps instead of handing off cleanly

## Security / safety / governance

- keep transactional actions deterministic and explicitly authorized
- enforce policy around pricing, regulated products, and promotional claims
- scope personalization and customer data use to the allowed privacy boundary
- retain enough traces to investigate unsafe or misleading recommendations

## Interview discussion points

- Which parts of the flow should remain deterministic?
- How would you separate catalog retrieval from recommendation logic?
- What signals tell you the chatbot is useful rather than merely engaging?
- Where do safety and policy checks need to sit in the request path?
