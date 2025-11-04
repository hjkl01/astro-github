
---
title: gpt4free
---


# gpt4free by xtekky

> **GitHub 项目地址**: [https://github.com/xtekky/gpt4free](https://github.com/xtekky/gpt4free)

---

## 主要特性

- **无付费门槛**：提供对 OpenAI GPT 系列模型的免费访问方式，无需使用 API Key。
- **多模型支持**：支持 GPT‑3.5、GPT‑4 等多种模型，兼容多种语言。
- **多渠道接入**：支持直接 HTTP 接口、Python SDK、命令行工具等多种调用方式。
- **代理与缓存**：内置代理支持、请求缓存机制，提升请求效率与稳定性。
- **自动轮询**：自动切换可用节点，减少请求失败率。

## 核心功能

| 功能 | 描述 |
|------|------|
| **HTTP API** | 通过 `POST /v1/chat/completions` 接口获取模型回复，兼容 OpenAI 官方格式。 |
| **Python SDK** | `pip install gpt4free`，直接在 Python 代码中调用 `gpt4free.chat()`。 |
| **命令行工具** | `gpt4free-cli` 可在终端交互式使用 GPT 模型。 |
| **代理设置** | 支持自定义 HTTP/HTTPS 代理，解决网络访问限制。 |
| **缓存机制** | 本地缓存最近请求结果，减少重复调用。 |

## 用法示例

### 1. 使用 HTTP API

```bash
curl -X POST "http://localhost:5000/v1/chat/completions" \
     -H "Content-Type: application/json" \
     -d '{
           "model": "gpt-3.5-turbo",
           "messages": [
             {"role": "user", "content": "Hello!"}
           ]
         }'
```

### 2. 使用 Python SDK

```python
from gpt4free import GPT4Free

client = GPT4Free()
response = client.chat(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tell me a joke."}]
)
print(response.choices[0].message.content)
```

### 3. 使用命令行工具

```bash
gpt4free-cli "What is the capital of France?"
```

## 快速启动

1. 克隆仓库  
   `git clone https://github.com/xtekky/gpt4free.git`

2. 安装依赖  
   `pip install -r requirements.txt`

3. 启动服务器  
   `python app.py`

4. 访问 `http://localhost:5000/v1/chat/completions` 进行调用。

---

> **提示**：项目默认使用公共节点，若遇到访问受限，可在 `config.yaml` 配置自定义代理或节点列表。