---
title: aisuite
---

# aisuite

## 功能介绍

aisuite 是一个简单的、统一的接口，用于与多个生成式 AI 提供商进行交互。它提供了一个类似于 OpenAI 的接口，支持聊天补全和音频转录，使开发者能够轻松地与最受欢迎的 AI 提供商合作并比较结果。作为 Python 客户端库的薄包装器，它允许开发者无缝切换和测试不同的提供商，而无需更改代码。

支持的主要提供商包括：Anthropic、AWS、Azure、Cerebras、Cohere、Google、Groq、HuggingFace、Ollama、Mistral、OpenAI、Sambanova、Watsonx 等。

aisuite 通过 HTTP 端点或 SDK 调用提供商，以最大化稳定性。

### 主要功能

- **聊天补全**：统一的聊天接口，支持多个提供商。
- **音频转录**：支持语音到文本的转录功能。
- **工具调用**：提供工具/函数调用的抽象，支持手动和自动处理。
- **提供商切换**：无需更改代码即可切换提供商。

## 安装

### 基础安装

```bash
pip install aisuite
```

### 安装特定提供商

```bash
pip install 'aisuite[anthropic]'
```

### 安装所有提供商

```bash
pip install 'aisuite[all]'
```

## 设置

需要为使用的提供商设置 API 密钥。可以作为环境变量设置，或传递给 aisuite Client 构造函数。

### 设置 API 密钥

```bash
export OPENAI_API_KEY="your-openai-api-key"
export ANTHROPIC_API_KEY="your-anthropic-api-key"
```

## 用法

### 聊天补全

```python
import aisuite as ai

client = ai.Client()

models = ["openai:gpt-4o", "anthropic:claude-3-5-sonnet-20240620"]

messages = [
    {"role": "system", "content": "Respond in Pirate English."},
    {"role": "user", "content": "Tell me a joke."},
]

for model in models:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.75
    )
    print(response.choices[0].message.content)
```

模型名称格式为 `<provider>:<model-name>`。aisuite 会根据提供商值调用相应的提供商。

### 工具调用

#### 手动工具处理

```python
def will_it_rain(location: str, time_of_day: str):
    """Check if it will rain in a location at a given time today.

    Args:
        location (str): Name of the city
        time_of_day (str): Time of the day in HH:MM format.
    """
    return "YES"

tools = [{
    "type": "function",
    "function": {
        "name": "will_it_rain",
        "description": "Check if it will rain in a location at a given time today",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "Name of the city"
                },
                "time_of_day": {
                    "type": "string",
                    "description": "Time of the day in HH:MM format."
                }
            },
            "required": ["location", "time_of_day"]
        }
    }
}]

response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    tools=tools
)
```

#### 自动工具执行

```python
client = ai.Client()
messages = [{
    "role": "user",
    "content": "I live in San Francisco. Can you check for weather and plan an outdoor picnic for me at 2pm?"
}]

# 自动工具执行
response = client.chat.completions.create(
    model="openai:gpt-4o",
    messages=messages,
    tools=[will_it_rain],
    max_turns=2  # 最大工具调用轮数
)
print(response.choices[0].message.content)
```

### 音频转录

```python
import aisuite as ai

client = ai.Client()

# 转录音频文件
result = client.audio.transcriptions.create(
    model="openai:whisper-1",
    file="meeting.mp3"
)
print(result.text)

# 切换提供商
result = client.audio.transcriptions.create(
    model="deepgram:nova-2",
    file="meeting.mp3"
)
print(result.text)
```

支持的提供商包括 OpenAI、Deepgram、Google、Hugging Face 等。

## 许可证

aisuite 基于 MIT 许可证发布。
