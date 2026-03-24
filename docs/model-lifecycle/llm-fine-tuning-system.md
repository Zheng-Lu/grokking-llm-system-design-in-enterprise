# Design an LLM Fine-tuning System

Fine-tuning is not only a training job. In practice it is a lifecycle system for dataset curation, experiment tracking, evaluation, model registration, promotion, and rollback.

## Problem framing

The system must let a team improve model behavior for a specific task or domain while keeping data lineage, evaluation quality, and deployment risk under control.

## Functional requirements

- ingest and version training and validation datasets
- define fine-tuning jobs with explicit base model, configuration, and owner
- track experiment metadata and produced artifacts
- evaluate candidate models before promotion
- register promoted models for downstream serving systems

## Non-functional requirements

- reproducibility across runs and environments
- lineage from model artifact back to data, config, and code
- controlled cost for training and repeated experimentation
- secure handling of proprietary or sensitive training data
- rollback when a promoted model regresses in production

## High-level architecture

- dataset registry and preparation pipeline
- training job orchestrator
- experiment tracker
- evaluation harness
- model registry and promotion workflow
- deployment hooks into serving infrastructure

## Core components

- data ingestion and labeling pipeline
- feature or example validation checks
- training runner and compute scheduler
- artifact store for checkpoints and logs
- automated and human evaluation workflow
- registry with staged promotion states

## Data flow / request flow

1. Data is collected, cleaned, and versioned into training and validation sets.
2. A fine-tuning job is launched against a specific base model and configuration.
3. Training outputs checkpoints, logs, and metrics into the experiment tracker.
4. Candidate models run through offline evaluations and task-specific review.
5. Approved models are registered and promoted to serving environments with rollback metadata.

## Scaling and reliability

- validate datasets before expensive training runs begin
- cache reusable preprocessing steps and artifact metadata
- keep experiment and registry metadata durable enough for audit and rollback
- separate exploratory experimentation from production promotion workflows
- connect production traces back to future training data curation

## Trade-offs

- custom fine-tuning improves task fit but increases lifecycle complexity
- larger datasets may improve generalization but increase labeling and review cost
- strict promotion gates improve safety but slow iteration
- provider-managed fine-tuning reduces operational toil but may reduce control and transparency

## Failure modes

- weak dataset curation that teaches the wrong behavior
- evaluation sets too small or too narrow for production reality
- unclear lineage between a deployed model and the data that created it
- no rollback discipline when a promoted model regresses

## Security / safety / governance

- control who can access training data, artifacts, and model promotion workflows
- classify and redact sensitive data before training
- require explicit sign-off for promotions into production
- retain enough lineage to investigate incidents or bias complaints later

## Interview discussion points

- What belongs in the dataset registry versus the experiment tracker?
- How would you decide whether fine-tuning is justified at all?
- What evaluations should gate promotion?
- How do you connect production failures back to future training data?
