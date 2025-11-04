
---
title: nexa-sdk
---


# Nexa SDK（NexaAI）文档

**项目地址**: https://github.com/NexaAI/nexa-sdk

---

## 主要特性

- **多语言支持**：SDK 提供 Python 与 JavaScript 两套语言实现，方便不同项目使用。
- **简洁的 API 封装**：对 Nexa AI 的核心接口（Chat、Completion、Embedding 等）做了统一封装，调用方式一致。
- **异步与同步兼容**：Python 版支持同步和 `async/await` 异步调用；JavaScript 版原生支持 Promise。
- **流式输出**：支持实时流式回答，适合聊天机器人、实时翻译等场景。
- **错误处理与重试**：内置错误分类与自动重试机制，减少网络波动导致的请求失败。
- **可配置的超时与重试次数**：用户可通过参数自定义请求超时时间及最大重试次数。

---

## 功能概览

| 功能 | 说明 |
|------|------|
| `Chat` | 发送聊天对话，返回模型回复。 |
| `Completion` | 生成文本补全，支持多轮上下文。 |
| `Embedding` | 生成文本向量，适用于检索、聚类等。 |
| `Stream` | 对 `Chat`/`Completion` 结果进行流式输出。 |
| `Batch` | 批量请求同类接口，提升效率。 |
| `Config` | 设置全局配置（API Key、Endpoint、超时、重试等）。 |

---

## 快速上手

### 1. 安装

**Python**

```bash
pip install nexasdk
```

**JavaScript**

```bash
npm install nexasdk
# 或
yarn add nexasdk
```

### 2. 配置 API Key

**Python**

```python
from nexasdk import NexaClient

client = NexaClient(api_key="YOUR_API_KEY")
```

**JavaScript**

```js
const { NexaClient } = require('nexasdk');

const client = new NexaClient({ apiKey: 'YOUR_API_KEY' });
```

### 3. 发送聊天请求

**Python**

```python
response = client.chat(
    model="nexa-base",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "今天天气怎么样？"}
    ]
)
print(response["choices"][0]["message"]["content"])
```

**JavaScript**

```js
const response = await client.chat({
    model: 'nexa-base',
    messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: '今天天气怎么样？' }
    ]
});
console.log(response.choices[0].message.content);
```

### 4. 流式输出

**Python**

```python
for chunk in client.chat_stream(
        model="nexa-base",
        messages=[{"role": "user", "content": "写一段 Python 代码示例"}]
    ):
    print(chunk["delta"]["content"], end='', flush=True)
```

**JavaScript**

```js
for await (const chunk of client.chatStream({
    model: 'nexa-base',
    messages: [{ role: 'user', content: '写一段 Python 代码示例' }]
})) {
    process.stdout.write(chunk.delta.content);
}
```

### 5. 生成文本向量

**Python**

```python
embedding = client.embedding(
    model="nexa-embed",
    input="这是一段需要向量化的文本"
)
print(embedding["data"][0]["embedding"])
```

**JavaScript**

```js
const embedding = await client.embedding({
    model: 'nexa-embed',
    input: '这是一段需要向量化的文本'
});
console.log(embedding.data[0].embedding);
```

---

## 进阶配置

```python
# Python
client = NexaClient(
    api_key="YOUR_API_KEY",
    endpoint="https://api.nexa.ai/v1",
    timeout=30,          # 秒
    retry_max=3          # 最大重试次数
)
```

```js
// JavaScript
const client = new NexaClient({
    apiKey: 'YOUR_API_KEY',
    endpoint: 'https://api.nexa.ai/v1',
    timeout: 30000,      // 毫秒
    retryMax: 3
});
```

---

## 常见问题

- **API Key 无效**：请确认在 Nexa AI 控制台已生成并复制正确的 API Key。
- **网络超时**：可通过 `timeout` 参数增大超时时间，或检查本地网络代理设置。
- **流式输出卡住**：确认服务器支持 HTTP/2 或已经开启对应配置。

--- 

> 以上内容仅为快速入门示例，更多高级用法请参阅官方文档与 API 参考。