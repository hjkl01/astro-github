---
title: Archgw
---

# ArchGW

ArchGW 是一个模型原生的代理服务器，旨在处理 AI 代理开发中的基本管道工作。它提供代理路由、护栏、可观测性和对各种 LLM（如 OpenAI、Anthropic 和 Ollama）的统一访问，从而实现更快、更可靠的代理构建和扩展。

## 主要功能

- **代理路由**：使用专用构建的 LLM 进行快速（<100ms）代理路由和交接。
- **LLM 路由**：支持三种策略 - 基于模型的路由、别名路由和偏好对齐路由，以统一访问多个 LLM 提供商。
- **护栏**：集中配置的安全措施，以防止有害结果并确保安全交互。
- **工具集成**：自动澄清提示并将其转换为常见代理场景的 API 调用。
- **可观测性**：与流行监控工具集成的 W3C 兼容跟踪、指标和日志记录。
- **基于 Envoy 构建**：利用 Envoy Proxy 经过验证的 HTTP 管理和可扩展性功能。

## 用法

### 安装

使用 pip 安装 ArchGW CLI：

```bash
pip install archgw==0.3.18
```

### LLM 路由器配置

创建配置文件（例如 `arch_config.yaml`）以路由到 LLM：

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

启动网关：

```bash
archgw up arch_config.yaml
```

### 代理应用配置

对于构建代理应用，配置提示、护栏和端点：

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

使用 OpenAI 兼容 API 进行交互：

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:10000/v1", api_key="test")
response = client.chat.completions.create(
    model="none",
    messages=[{"role": "user", "content": "what is exchange rate for gbp"}]
)
```

有关更多详细信息，请访问[官方文档](https://docs.archgw.com)。
