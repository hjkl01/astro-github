---
title: aisuite
---

# aisuite

## 项目简介

aisuite 是一个简单、统一的接口，用于与多个生成式 AI 提供商交互。它允许开发者通过标准化的接口轻松与各种大型语言模型 (LLM) 进行交互和比较。

项目地址: [andrewyng/aisuite](https://github.com/andrewyng/aisuite)

## 主要特性

- **统一接口**: 为多个 AI 提供商提供一致的 API 接口
- **易于使用**: 简单的初始化和调用方式
- **多提供商支持**: 支持 OpenAI、Anthropic、Google、Cerebras 等多个 AI 提供商
- **工具调用**: 支持函数调用和工具集成
- **灵活配置**: 支持自定义 API 密钥和端点配置

## 安装

```bash
pip install aisuite
```

## 基本使用

### 初始化客户端

```python
import aisuite as ai

client = ai.Client()
```

### 简单的聊天完成

```python
messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    temperature=0.75
)

print(response.choices[0].message.content)
```

### 多提供商比较

```python
models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(f"{model}: {response.choices[0].message.content}")
```

### 工具调用

```python
def get_current_temperature(location: str, unit: str):
    return {"temperature": 72}

tools = [{
    "type": "function",
    "function": {
        "name": "get_current_temperature",
        "description": "Get the current temperature for a specific location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state"},
                "unit": {"type": "string", "enum": ["Celsius", "Fahrenheit"]}
            },
            "required": ["location", "unit"]
        }
    }
}]

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    tools=tools
)
```

### 配置环境变量

```bash
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

### 简化查询函数

```python
def ask(message, sys_message="You are a helpful agent.", model="groq:llama-3.2-3b-preview"):
    client = ai.Client()
    messages = [
        {"role": "system", "content": sys_message},
        {"role": "user", "content": message}
    ]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content

# 使用
answer = ask("What is the capital of Japan?")
print(answer)
```

## 支持的提供商

- OpenAI (GPT 系列)
- Anthropic (Claude 系列)
- Google (Gemini)
- Groq
- Cerebras
- DeepSeek
- Fireworks
- Hugging Face
- Mistral
- Nebius
- Ollama
- SambaNova
- Together AI
- Watsonx
- XAI (Grok)

## 文档和资源

- [GitHub 仓库](https://github.com/andrewyng/aisuite)
- [README](https://github.com/andrewyng/aisuite/blob/main/README.md)
- [示例代码](https://github.com/andrewyng/aisuite/tree/main/examples)
