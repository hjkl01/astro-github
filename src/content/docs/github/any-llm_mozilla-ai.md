---
title: any-llm
---

# any-llm

**Communicate with any LLM provider using a single, unified interface.** Switch between OpenAI, Anthropic, Mistral, Ollama, and more without changing your code.

## Features

- **Simple, unified interface**: Single function for all providers, switch models with just a string change
- **Developer friendly**: Full type hints for better IDE support and clear, actionable error messages
- **Leverages official provider SDKs**: Ensures maximum compatibility
- **Framework-agnostic**: Can be used across different projects and use cases
- **Flexible deployment**: Direct connections for simplicity, or optional any-llm-gateway for production budget and access control
- **Optional Gateway**: FastAPI-based proxy server for budget management, API key management, usage analytics, and multi-tenant support

## Installation

### Requirements

- Python 3.11 or newer
- API keys for whichever LLM providers you want to use

### Basic Installation

Install support for specific providers:

```bash
pip install 'any-llm-sdk[openai]'           # Just OpenAI
pip install 'any-llm-sdk[mistral,ollama]'   # Multiple providers
pip install 'any-llm-sdk[all]'              # All supported providers
```

### Setting Up API Keys

Set environment variables for your chosen providers:

```bash
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"
export MISTRAL_API_KEY="your-key-here"
# ... etc
```

Alternatively, pass API keys directly in your code.

## Usage

### Direct API Functions (Recommended for Bootstrapping and Experimentation)

```python
from any_llm import completion
import os

# Make sure you have the appropriate environment variable set
assert os.environ.get('MISTRAL_API_KEY')

response = completion(
    model="mistral-small-latest",
    provider="mistral",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

**Alternative syntax:** Use combined `provider:model` format:

```python
response = completion(
    model="mistral:mistral-small-latest",  # <provider_id>:<model_id>
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### AnyLLM Class (Recommended for Production)

For applications that need to reuse providers, perform multiple operations, or require more control:

```python
from any_llm import AnyLLM

llm = AnyLLM.create("mistral", api_key="your-mistral-api-key")

response = llm.completion(
    model="mistral-small-latest",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Responses API

For providers that implement the OpenAI-style Responses API:

```python
from any_llm import responses

result = responses(
    model="gpt-4o-mini",
    provider="openai",
    input_data=[
        {"role": "user", "content": [
            {"type": "text", "text": "Summarize this in one sentence."}
        ]}
    ],
)

# Non-streaming returns an OpenAI-compatible Responses object alias
print(result.output_text)
```

## Any-LLM Gateway

any-llm-gateway is an optional FastAPI-based proxy server that adds enterprise-grade features:

- **Budget Management**: Enforce spending limits with automatic resets
- **API Key Management**: Issue, revoke, and monitor virtual API keys
- **Usage Analytics**: Track every request with full token counts, costs, and metadata
- **Multi-tenant Support**: Manage access and budgets across users and teams

### Quick Start

```bash
docker run \
  -e GATEWAY_MASTER_KEY="your-secure-master-key" \
  -e OPENAI_API_KEY="your-api-key" \
  -p 8000:8000 \
  ghcr.io/mozilla-ai/any-llm/gateway:latest
```

## Supported Providers

See the [official documentation](https://mozilla-ai.github.io/any-llm/providers/) for the full list of supported LLM providers.

## Documentation

- [Full Documentation](https://mozilla-ai.github.io/any-llm/)
- [Cookbook Examples](https://mozilla-ai.github.io/any-llm/cookbook/)

## License

Apache License 2.0
