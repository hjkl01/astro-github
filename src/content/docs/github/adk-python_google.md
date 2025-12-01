---
title: adk-python
---

# ADK-Python

ADK-Python 是 Google 开发的开源、代码优先的 Python 工具包，用于构建、评估和部署复杂的 AI 代理，具有灵活性和控制力。它将软件开发原则应用于 AI 代理创建，简化了从简单任务到复杂系统的代理工作流的构建、部署和编排。虽然针对 Gemini 进行了优化，但它是模型无关的、部署无关的，并与其他框架兼容。

## 主要功能

- **丰富的工具生态系统**：利用预构建工具、自定义函数、OpenAPI 规范、MCP 工具或集成现有工具，为代理提供多样化能力，并与 Google 生态系统紧密集成。
- **代码优先开发**：直接在 Python 中定义代理逻辑、工具和编排，以实现终极灵活性、可测试性和版本控制。
- **代理配置**：无需代码即可构建代理。查看[代理配置](https://google.github.io/adk-docs/agents/config/)功能。
- **工具确认**：一个[工具确认流程(HITL)](https://google.github.io/adk-docs/tools/confirmation/)，可以保护工具执行并提供显式确认和自定义输入。
- **模块化多代理系统**：通过将多个专门代理组合成灵活的层次结构来设计可扩展应用程序。
- **部署任意位置**：轻松容器化并在 Cloud Run 上部署代理，或使用 Vertex AI Agent Engine 无缝扩展。

## 用法

### 安装

#### 稳定版本（推荐）

使用 `pip` 安装最新稳定版本：

```bash
pip install google-adk
```

发布节奏约为每两周一次。

#### 开发版本

如果需要访问尚未包含在官方 PyPI 发布中的更改，可以直接从主分支安装：

```bash
pip install git+https://github.com/google/adk-python.git@main
```

注意：开发版本直接从最新代码提交构建。虽然它包含最新的修复和新功能，但也可能包含实验性更改或稳定版本中不存在的错误。主要用于测试即将到来的更改或在正式发布前访问关键修复。

### 定义单个代理

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",  # 或您首选的 Gemini 模型
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)
```

### 定义多代理系统

定义一个多代理系统，包括协调器代理、问候代理和任务执行代理。然后 ADK 引擎和模型将指导代理协同工作以完成任务。

```python
from google.adk.agents import LlmAgent, BaseAgent

# 定义单个代理
greeter = LlmAgent(name="greeter", model="gemini-2.5-flash", ...)
task_executor = LlmAgent(name="task_executor", model="gemini-2.5-flash", ...)

# 创建父代理并通过 sub_agents 分配子代理
coordinator = LlmAgent(
    name="Coordinator",
    model="gemini-2.5-flash",
    description="I coordinate greetings and tasks.",
    sub_agents=[  # 在此处分配 sub_agents
        greeter,
        task_executor
    ]
)
```

### 评估代理

```bash
adk eval \
    samples_for_testing/hello_world \
    samples_for_testing/hello_world/hello_world_eval_set_001.evalset.json
```

更多详细信息，请查看[官方文档](https://google.github.io/adk-docs/)。
