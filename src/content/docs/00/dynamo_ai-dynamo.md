
---
title: dynamo
---


# Dynamo - AI 助手框架

**项目地址**: [https://github.com/ai-dynamo/dynamo](https://github.com/ai-dynamo/dynamo)

## 📌 简介
Dynamo 是一个面向开发者的 AI 助手框架，旨在减少与大型语言模型（如 OpenAI GPT 系列、Claude、Gemini 等）交互的重复工作。它通过模块化、可插拔的设计，让你能在自己的项目中快速集成文本理解、摘要、代码生成、数据清洗、问答等功能。

---

## 🚀 主要特性

| # | 功能 | 说明 |
|---|------|------|
| 1 | **通用接口** | 统一的 `AIEngine.exec()` 接口，支持多家模型提供商（OpenAI、Anthropic、Google Gemini、Azure OpenAI 等）。 |
| 2 | **插件化 Prompt** | 通过 `Prompt` 类实现多种 Prompt 模型，支持可插拔、层级组合与变量替换。 |
| 3 | **任务模板** | 提供一系列内置任务：`文本摘要`、`文本检索`、`代码分析`、`JSON 结构化` 等。你可直接实例化或自定义。 |
| 4 | **多轮对话** | 内置 `Conversation` 对象，支持会话上下文管理、知识库注入与记忆。 |
| 5 | **管道化工作流** | 支持将多个 AITask 叠加成一个 Pipeline，自动处理数据流、错误回退与日志。 |
| 6 | **可视化调试** | 配置 `debug=True` 可打印 Prompt、返回结果、使用时长、调用链路。 |
| 7 | **离线缓存** | 内置缓存机制减少重复请求，支持自定义缓冲区大小与过期策略。 |
| 8 | **轻量级依赖** | 仅依赖 `httpx`、`pydantic`、`tiktoken`（可选），无额外消耗。 |
| 9 | **跨平台** | 纯 Python 代码，支持 Windows / Linux / macOS；可部署为 Lambda/Cloud Functions。 |

---

## 📦 安装

```bash
# PyPI
pip install dynamo-ai

# 或直接从 GitHub
pip install git+https://github.com/ai-dynamo/dynamo.git
```

---

## 📄 基本使用

### 1️⃣ 初始化 AI 引擎

```python
from dynamo import AIEngine

# 使用 OpenAI GPT-4
engine = AIEngine(
    model="gpt-4o-mini",
    api_key="YOUR_OPENAI_KEY",
    provider="openai",
    temperature=0.7
)

# 使用 Anthropic Claude
# engine = AIEngine(
#     model="claude-3-5-sonnet",
#     api_key="YOUR_CLAUDE_KEY",
#     provider="anthropic",
#     temperature=0.6
# )
```

### 2️⃣ 简单文本摘要

```python
summary = engine.exec(
    prompt="请将以下文章摘要为三句话：\n文章内容：<article>",
    variables={"article": "......"}  # 传入文章文本
)

print(summary)
```

### 3️⃣ 代码分析与生成

```python
from dynamo.tasks import CodeAnalysis

analysis = engine.exec(
    prompt=CodeAnalysis.description,  # 内置Prompt模板
    variables={"code": "def foo(): ..."}
)

print(analysis)  # 返回分析文本或 JSON
```

### 4️⃣ 创建工作流 Pipeline

```python
from dynamo import Pipeline, TextSummary, CodeGeneration

pipeline = Pipeline(
    [TextSummary("gpt-4o-mini"), CodeGeneration("gpt-4o-mini")]
)

result = pipeline.run(
    article_text="......",
    function_name="process_data"
)
print(result)
```

### 5️⃣ 调试与日志

```python
engine.debug = True  # 打开调试模式
```

---

## 📚 进阶用法

### 自定义 Prompt

```python
from dynamo.prompts import Prompt

my_prompt = Prompt(
    template="请回答以下问题：\n{{question}}\n答案：",
    name="custom_qna"
)

engine.register_prompt(my_prompt)
response = engine.exec(prompt="custom_qna", variables={"question": "Python 里什么是装饰器？"})
```

### 仓储知识库

```python
from dynamo.engines import KnowledgeBase

kb = KnowledgeBase(
    storagesqlite",
    db_path="~/.dynamo/kb.sqlite"
)

kb.add_entry("decorator", "装饰器是一个返回值为加工后函数的函数。")
engine.set_kb(kb)

```

### 自定义错误回退

```python
def fallback(result, error):
    return f"调用失败：{error}，请稍后重试。"

pipeline = Pipeline([...])
pipeline.on_error(fallback)
```

---

## 📑 常见问题

| 问题 | 解决方案 |
|------|----------|
| 如何切换模型？ | 在 `AIEngine` 初始化时修改 `model` 与 `provider` 参数。 |
| 参数太长导致 token 超限？ | 使用 `max_tokens` 限制返回长度，或先做预剪裁。 |
| 如何加速 API 调用？ | 开启缓存 (`engine.cache=True`) 或使用多线程/多进程。 |
| 如何在 Docker 部署？ | 暴露 `OPENAI_API_KEY` 与其他秘钥，直接 `docker run` 即可。 |

---

## 🎉 贡献 & 文档

- Issues / PRs: 欢迎提交改进建议与 bug 修复。  
- 文档：`docs/` 目录下有更详细的 API 说明与案例。  
- 示例：`examples/` 中包含完整的 demo。

---

*© 2024 AI Dynamo 项目，遵循 Apache-2.0 协议。祝开发愉快 🚀*

