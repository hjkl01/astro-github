---
title: Kimi-K2
---

## 项目介绍

Kimi-K2 是 Moonshot AI 团队开发的先进混合专家（Mixture-of-Experts, MoE）大型语言模型系列。该模型拥有 1 万亿总参数和 320 亿激活参数，专为前沿知识、推理和编码任务优化，同时具备强大的代理智能能力。

## 主要功能

- **大规模训练**：在 15.5T tokens 上预训练 1T 参数 MoE 模型，无训练不稳定性。
- **MuonClip 优化器**：应用 Muon 优化器于前所未有的规模，并开发新技术解决扩展过程中的不稳定性。
- **代理智能**：专门设计用于工具使用、推理和自主问题解决。

## 模型变体

- **Kimi-K2-Base**：基础模型，适合研究者和开发者进行完全控制的微调和自定义解决方案。
- **Kimi-K2-Instruct**：后训练模型，最适合即插即用的一般用途聊天和代理体验，无需长思考。

## 部署方式

可以通过 Moonshot AI 平台 API 访问 Kimi-K2，提供与 OpenAI/Anthropic 兼容的 API。模型检查点以 block-fp8 格式存储，可在 Hugging Face 上获取。

推荐的推理引擎包括：

- vLLM
- SGLang
- KTransformers
- TensorRT-LLM

## 使用方法

### 聊天完成

设置本地推理服务后，通过聊天端点进行交互：

```python
def simple_chat(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": [{"type": "text", "text": "Please give a brief self-introduction."}]},
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=False,
        temperature=0.6,
        max_tokens=256
    )
    print(response.choices[0].message.content)
```

推荐温度设置为 0.6。

### 工具调用

Kimi-K2-Instruct 具备强大的工具调用能力。以下是调用天气工具的示例：

```python
# 工具实现
def get_weather(city: str) -> dict:
    return {"weather": "Sunny"}

# 工具模式定义
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retrieve current weather information. Call this when the user asks about the weather.",
        "parameters": {
            "type": "object",
            "required": ["city"],
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            }
        }
    }
}]

# 工具映射
tool_map = {
    "get_weather": get_weather
}

def tool_call_with_client(client: OpenAI, model_name: str):
    messages = [
        {"role": "system", "content": "You are Kimi, an AI assistant created by Moonshot AI."},
        {"role": "user", "content": "What's the weather like in Beijing today? Use the tool to check."}
    ]
    finish_reason = None
    while finish_reason is None or finish_reason == "tool_calls":
        completion = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=0.6,
            tools=tools,
            tool_choice="auto"
        )
        choice = completion.choices[0]
        finish_reason = choice.finish_reason
        if finish_reason == "tool_calls":
            messages.append(choice.message)
            for tool_call in choice.message.tool_calls:
                tool_call_name = tool_call.function.name
                tool_call_arguments = json.loads(tool_call.function.arguments)
                tool_function = tool_map[tool_call_name]
                tool_result = tool_function(**tool_call_arguments)
                print("tool_result:", tool_result)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_call_name,
                    "content": json.dumps(tool_result)
                })
    print("-" * 100)
    print(choice.message.content)
```
