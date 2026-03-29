# Design an LLM Fine-tuning System

Fine-tuning is not only a training job. In practice it is a lifecycle system for dataset curation, experiment tracking, evaluation, model registration, promotion, and rollback.

## Problem framing

The system must let a team improve model behavior for a specific task or domain while keeping data lineage, evaluation quality, and deployment risk under control.

## Functional requirements

- Ingest and version training and validation datasets
- Define fine-tuning jobs with explicit base model, configuration, and owner
- Track experiment metadata and produced artifacts
- Evaluate candidate models before promotion
- Register promoted models for downstream serving systems

## Non-functional requirements

- Reproducibility across runs and environments
- Lineage from model artifact back to data, config, and code
- Controlled cost for training and repeated experimentation
- Secure handling of proprietary or sensitive training data
- Rollback when a promoted model regresses in production

## High-level architecture

- Dataset registry and preparation pipeline
- Training job orchestrator
- Experiment tracker
- Evaluation harness
- Model registry and promotion workflow
- Deployment hooks into serving infrastructure

## Core components

- Data ingestion and labeling pipeline
- Feature or example validation checks
- Training runner and compute scheduler
- Artifact store for checkpoints and logs
- Automated and human evaluation workflow
- Registry with staged promotion states

## Data flow / request flow

1. Data is collected, cleaned, and versioned into training and validation sets.
2. A fine-tuning job is launched against a specific base model and configuration.
3. Training outputs checkpoints, logs, and metrics into the experiment tracker.
4. Candidate models run through offline evaluations and task-specific review.
5. Approved models are registered and promoted to serving environments with rollback metadata.

## Scaling and reliability

- Validate datasets before expensive training runs begin
- Cache reusable preprocessing steps and artifact metadata
- Keep experiment and registry metadata durable enough for audit and rollback
- Separate exploratory experimentation from production promotion workflows
- Connect production traces back to future training data curation

## Trade-offs

- Custom fine-tuning improves task fit but increases lifecycle complexity
- Larger datasets may improve generalization but increase labeling and review cost
- Strict promotion gates improve safety but slow iteration
- Provider-managed fine-tuning reduces operational toil but may reduce control and transparency

## Failure modes

- Weak dataset curation that teaches the wrong behavior
- Evaluation sets too small or too narrow for production reality
- Unclear lineage between a deployed model and the data that created it
- No rollback discipline when a promoted model regresses

## Security / safety / governance

- Control who can access training data, artifacts, and model promotion workflows
- Classify and redact sensitive data before training
- Require explicit sign-off for promotions into production
- Retain enough lineage to investigate incidents or bias complaints later

## Interview discussion points

- What belongs in the dataset registry versus the experiment tracker?
- How would you decide whether fine-tuning is justified at all?
- What evaluations should gate promotion?
- How do you connect production failures back to future training data?
