# AIBrix

## Overview

AIBrix is an open-source project under the vLLM organization that provides cost-efficient and pluggable infrastructure components for deploying, managing, and scaling large language model (LLM) inference in a cloud-native environment. It is designed specifically for enterprise needs, offering building blocks to construct scalable GenAI inference systems.

## Key Features

- **High-Density LoRA Management**: Supports lightweight, low-rank adaptations of models for efficient fine-tuning.
- **LLM Gateway and Routing**: Manages and directs traffic across multiple models and replicas.
- **LLM App-Tailored Autoscaler**: Dynamically scales inference resources based on real-time demand.
- **Unified AI Runtime**: A sidecar for metric standardization, model downloading, and management.
- **Distributed Inference**: Scalable architecture for handling large workloads across multiple nodes.
- **Distributed KV Cache**: Enables high-capacity, cross-engine KV reuse.
- **Cost-efficient Heterogeneous Serving**: Supports mixed GPU inference to reduce costs while maintaining SLO guarantees.
- **GPU Hardware Failure Detection**: Proactive detection of GPU hardware issues.

## Architecture

AIBrix features a modular architecture optimized for Kubernetes, including components for gateway, autoscaling, runtime, and observability. It integrates with vLLM for efficient LLM serving.

## Usage

AIBrix is deployed using Kubernetes manifests. For local testing or development:

1. Clone the repository: `git clone https://github.com/vllm-project/aibrix.git`
2. Install dependencies: `kubectl apply -k config/dependency --server-side`
3. Install components: `kubectl apply -k config/default`

For stable releases, apply the provided YAML files from the releases page (e.g., for v0.4.0).

Detailed installation, configuration, and usage instructions are available in the [official documentation](https://aibrix.readthedocs.io/latest/).

## License

Apache 2.0 License. Contributions are welcome via the [contributing guidelines](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md). Support and discussions on the [Slack channel](https://vllm-dev.slack.com/archives/C08EQ883CSV) or [GitHub issues](https://github.com/vllm-project/aibrix/issues).
