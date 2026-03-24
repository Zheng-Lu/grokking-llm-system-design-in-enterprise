# Inference and Platform Infra

This section covers the serving and control layer underneath most LLM applications. It is where teams turn model access into a shared platform with latency targets, quotas, routing policy, traceability, and release discipline.

## In this section

- [Platform Foundations](../foundations/platform-foundations.md) defines the shared infra layer and the main design tensions it introduces.
- [Design an Offline Batch Inference Service](offline-batch-inference-service.md) covers asynchronous, throughput-oriented model processing.
- [Design an Online Inference Service](online-inference-service.md) covers low-latency serving for user-facing or synchronous workloads.
- [Design an LLM Gateway / Proxy](llm-gateway-proxy.md) focuses on routing, policy enforcement, and platform control at the model boundary.
- [Design an Evaluation & Observability System for LLM Applications](evaluation-observability-system.md) covers tracing, datasets, release gates, and regression detection.

## Section lens

If the model is the engine, this section is the transmission, brakes, and dashboard.
