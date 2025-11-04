
---
title: deepagents
---

# DeepAgents – LangChain AI

> GitHub 项目地址: https://github.com/langchain-ai/deepagents

## 概述
DeepAgents 是 LangChain AI 生态系下的开源框架，专为构建多智能体（Agent）驱动的 LLM 场景而设计。它整合了规划、决策、记忆、工具调用等关键能力，让开发者可以快速搭建复杂、可靠且可扩展的智能代理系统。

## 核心特性

| 特性 | 说明 |
|---|---|
| **多智能体协同** | 支持 Agent 之间的沟通与分工，适用于需要多角色分工的大规模任务 |
| **任务规划** | 内置子进程“Planning Agent”，能将大任务拆分为可执行子任务并生成行动计划 |
| **执行和工具调用** | 提供统一的工具执行接口，可调用外部 API、数据库、文件操作等 |
| **记忆与上下文管理** | 集成 LangChain 的记忆组件，支持临时、全局、上下文特定记忆 |
| **自定义工具与插件** | 开发者可快速编写自定义工具，按需注入到 Agent 生态中 |
| **可视化与监控** | 提供 UI 监控 Agent 行为与决策过程，支持调试与分析 |

## 功能概述

1. **Agent 组件**：`DeepAgent` 基类，可在子类中实现 `generate()`、`plan()`、`act()` 等方法，实现自定义行为。
2. **工具类**：`DeepTool` 基类，支持 `run()`、`describe()`，所有工具可通过 `ToolRegistry` 注册。
3. **执行框架**：`DeepExecutor` 负责解析计划，查找可用工具并执行，支持同步与异步模式。
4. **记忆层**：`MemoryStore` 与 `MemoryManager`，提供简单键值存储、向量检索与时间维度管理。
5. **配置与运行**：使用 YAML 或 JSON 定义 agent、工具与任务配置，`DeepRunner` 负责加载、初始化与执行流程。

## 快速使用

```bash
# 1. 克隆仓库
git clone https://github.com/langchain-ai/deepagents.git && cd deepagents

# 2. 安装依赖
pip install -e ".[dev]"

# 3. 设置环境变量（示例）
export OPENAI_API_KEY="your_api_key"

# 4. 运行示例脚本
python examples/simple_agent.py
```

### 示例：构建一个基于天气查询的 Agent

```python
from deepagents import DeepAgent, DeepTool, DeepRunner

# 定义天气工具
class WeatherTool(DeepTool):
    name = "weather_query"
    description = "查询当前天气信息"

    def run(self, location: str) -> str:
        # 调用第三方天气 API
        return f"{location} 的天气是晴朗"

# 定义 Agent
class WeatherAgent(DeepAgent):
    def plan(self, task: str):
        # 简单规划：直接调用天气工具
        return [(self.tools["weather_query"], ["上海"])]

# 注册工具与 Agent
runner = DeepRunner()
runner.register_tool(WeatherTool)
runner.register_agent(WeatherAgent)

# 执行
runner.run("查询上海天气")
```

## 文档与学习

- 官方文档: <https://deepagents.langchain.ai/docs/>
- 示例代码: `examples/` 目录
- 插件/工具开发文档: `docs/extensions/`

--- 

> 以上内容可直接保存为  
> `src/content/docs/00/deepagents_langchain-ai.md`
祝你使用愉快！