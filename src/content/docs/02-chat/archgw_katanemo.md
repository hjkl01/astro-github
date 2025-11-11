---
title: Archgw
---

# ArchGW

Arch is a models-native proxy server designed to handle the essential plumbing work in AI agent development. It provides agent routing, guardrails, observability, and unified access to various LLMs like OpenAI, Anthropic, and Ollama, enabling faster and more reliable agent building and scaling.

## Key Features

- **Agent Routing**: Fast (<100ms) routing and hand-off between agents using purpose-built LLMs.
- **LLM Routing**: Supports three strategies - model-based, alias-based, and preference-aligned routing for unified access to multiple LLM providers.
- **Guardrails**: Centrally configured safety measures to prevent harmful outcomes and ensure secure interactions.
- **Tools Integration**: Automatically clarifies prompts and converts them to API calls for common agentic scenarios.
- **Observability**: W3C-compatible tracing, metrics, and logging that integrates with popular monitoring tools.
- **Built on Envoy**: Leverages Envoy Proxy's proven HTTP management and scalability features.

## Usage

### Installation

Install the ArchGW CLI using pip:

```bash
pip install archgw==0.3.18
```

### LLM Router Configuration

Create a configuration file (e.g., `arch_config.yaml`) for routing to LLMs:

```yaml
version: v0.1.0

listeners:
  egress_traffic:
    address: 0.0.0.0
    port: 12000
    message_format: openai
    timeout: 30s

llm_providers:
  - model: openai/gpt-4o
    access_key: $OPENAI_API_KEY
    default: true

  - model: anthropic/claude-3-5-sonnet-20241022
    access_key: $ANTHROPIC_API_KEY
```

Start the gateway:

```bash
archgw up arch_config.yaml
```

### Agentic App Configuration

For building agentic applications, configure prompts, guards, and endpoints:

```yaml
version: v0.1.0

listeners:
  ingress_traffic:
    address: 0.0.0.0
    port: 10000
    message_format: openai
    timeout: 30s

llm_providers:
  - access_key: $OPENAI_API_KEY
    model: openai/gpt-4o

system_prompt: |
  You are a helpful assistant.

prompt_targets:
  - name: currency_exchange
    description: Get currency exchange rate from USD
    parameters:
      - name: currency_symbol
        description: the currency for conversion
        required: true
        type: str
        in_path: true
    endpoint:
      name: frankfurter_api
      path: /v1/latest?base=USD&symbols={currency_symbol}

endpoints:
  frankfurter_api:
    endpoint: api.frankfurter.dev:443
    protocol: https
```

Interact using OpenAI-compatible API:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:10000/v1", api_key="test")
response = client.chat.completions.create(
    model="none",
    messages=[{"role": "user", "content": "what is exchange rate for gbp"}]
)
```

For more details, visit the [official documentation](https://docs.archgw.com).
