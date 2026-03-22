# LLMOps and Evals

LLMOps is the practice of turning prompt and model changes into an engineering discipline. Evaluation is the core of that discipline because teams cannot improve what they cannot reliably measure.

## What belongs here

- dataset and prompt versioning
- trace capture
- offline evaluations
- online experimentation
- release criteria
- rollback and incident response

## Why this is hard

Enterprise LLM systems often fail in ways that look subjective until the team forces structure onto them:

- answers are technically plausible but unhelpful
- retrieval is correct but not complete
- latency is acceptable on average but bad for important users
- evaluator coverage misses the real regression

## The eval stack

A practical eval stack usually has:

1. traced production or staging examples
2. curated task datasets
3. automated checks for stable failure modes
4. human review for ambiguous quality questions
5. release gates tied to both quality and operational metrics

## Common traps

- evaluating generation quality without measuring retrieval quality
- overfitting to a tiny golden set
- relying on one aggregate score
- shipping model changes without a rollback plan

## What good chapters should reveal

- what the team measured
- how they closed the loop from failure to dataset
- which metrics were trusted for release decisions

