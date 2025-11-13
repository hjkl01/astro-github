---
title: repository
---

# Google ADK Python

Google ADK (Agent Development Kit) 是一个开源的、代码优先的 Python 工具包，用于构建、评估和部署复杂的 AI 代理，提供灵活性和控制力。

## 项目概述

ADK 是一个灵活且模块化的框架，将软件开发原理应用于 AI 代理创建。它旨在简化代理工作流的构建、部署和编排，从简单任务到复杂系统。虽然针对 Gemini 进行了优化，但 ADK 是模型无关、部署无关的，并且与其他框架兼容。

## 核心特性

### 🛠️ 丰富的工具生态系统

- 利用预构建工具、自定义函数、OpenAPI 规范、MCP 工具或集成现有工具
- 为代理提供多样化能力，与 Google 生态系统紧密集成

### 💻 代码优先开发

- 直接在 Python 中定义代理逻辑、工具和编排
- 提供终极的灵活性、可测试性和版本控制

### ⚙️ 代理配置

- 无需代码即可构建代理，支持 Agent Config 功能

### ✅ 工具确认

- 提供工具确认流程 (HITL)，可以用明确确认和自定义输入来保护工具执行

### 🔄 模块化多代理系统

- 通过将多个专业代理组合成灵活的层次结构来设计可扩展应用程序

### 🚀 随处部署

- 轻松容器化并在 Cloud Run 上部署代理，或使用 Vertex AI Agent Engine 无缝扩展

## 安装方式

### 稳定版本（推荐）

```bash
pip install google-adk
```

### 开发版本

```bash
pip install git+https://github.com/google/adk-python.git@main
```

## 使用示例

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
    sub_agents=[  # 在这里分配 sub_agents
        greeter,
        task_executor
    ]
)
```

## 开发工具

### 内置开发 UI

提供内置开发 UI，帮助您测试、评估、调试和展示代理。

### 代理评估

```bash
adk eval \
    samples_for_testing/hello_world \
    samples_for_testing/hello_world/hello_world_eval_set_001.evalset.json
```

## 最新功能

- **自定义服务注册**：添加服务注册表，提供注册自定义服务实现的通用方法
- **回退功能**：添加将会话回退到之前调用之前的能力
- **新代码执行器**：引入新的 AgentEngineSandboxCodeExecutor 类，支持使用 Vertex AI 代码执行沙盒 API 执行代理生成的代码

## 相关资源

- **[官方文档](https://google.github.io/adk-docs/)**
- **[示例代码](https://github.com/google/adk-samples)**
- **[Java ADK](https://github.com/google/adk-java)**
- **[Go ADK](https://github.com/google/adk-go)**
- **[ADK Web](https://github.com/google/adk-web)**

## 社区支持

- 拥有活跃的社区贡献和讨论
- 提供 [adk-python-community](https://github.com/google/adk-python-community) 仓库，包含社区贡献的工具、第三方服务集成和部署脚本
- 定期举办社区会议和活动

## 许可证

本项目采用 Apache 2.0 许可证。

---

_Happy Agent Building!_
