---
title: jupyter-ai
---

# Jupyter AI

## 简介

Jupyter AI 是 JupyterLab 的一个生成式 AI 扩展，它将生成式 AI 与 Jupyter 笔记本连接起来，提供用户友好且强大的方式在笔记本中探索生成式 AI 模型，并提高在 JupyterLab 和 Jupyter Notebook 中的生产力。

## 功能

- **%%ai 魔法命令**：将 Jupyter 笔记本变成可重现的生成式 AI 游乐场。该命令可在任何运行 IPython 内核的地方工作（JupyterLab、Jupyter Notebook、Google Colab、Kaggle、VSCode 等）。
- **原生聊天 UI**：在 JupyterLab 中提供原生聊天界面，使您能够与生成式 AI 作为对话助手一起工作。
- **支持多种模型提供商**：包括 AI21、Anthropic、AWS、Cohere、Gemini、Hugging Face、MistralAI、NVIDIA 和 OpenAI。
- **本地模型支持**：通过 GPT4All 和 Ollama，支持在消费级机器上轻松且私密地使用生成式 AI 模型。

## 用法

### 安装

推荐使用 pip 快速安装（包括 %%ai 魔法和 JupyterLab 扩展）：

```bash
pip install jupyter-ai[all]
```

然后重启 JupyterLab。

如果只想安装 %%ai 魔法（不使用 JupyterLab）：

```bash
pip install jupyter-ai-magics[all]
```

### 设置模型提供商

1. 从模型提供商平台获取必要的凭据（如 API 密钥）。
2. 在笔记本的代码单元中设置凭据，或使用环境变量。

例如，使用 getpass 设置 API 密钥：

```python
import getpass
import os

key = getpass.getpass('Enter your PROVIDER API key: ')
os.environ['PROVIDER_API_KEY'] = key
```

### 使用 %%ai 魔法

首先加载扩展：

```python
%load_ext jupyter_ai_magics
```

然后使用 %%ai 魔法指定模型和自然语言提示：

```python
%%ai model_name
Your prompt here
```

例如：

```python
%%ai openai-chat:gpt-3.5-turbo
Explain the concept of machine learning in simple terms.
```

### 使用 JupyterLab 扩展

安装后，JupyterLab 中会自动激活聊天界面。您可以在聊天中与 AI 对话，询问问题或请求帮助。

## 要求

- Python 3.9 - 3.12
- JupyterLab 4 或 Notebook 7
- 至少一个模型提供商的访问权限

更多详细信息，请参考 [官方文档](https://jupyter-ai.readthedocs.io/en/latest/)。
