---
title: autogen
---


# Microsoft AutoGen

> GitHub 地址: [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen)

## 主要特性

- **多代理交互**：支持多智能体（Agent）之间的协作与对话，自动管理代理角色、目标与对话状态。
- **动态任务分配**：根据对话上下文自动分配任务给合适的代理，保持任务链的连贯性。
- **可扩展插件体系**：通过插件（Plugin）机制集成外部工具、数据库或自定义 API，提升代理能力。
- **安全与审计**：内置安全审计框架，监控代理行为，防止不安全输出。
- **高可配置性**：提供丰富的配置选项（如代理模型、温度、最大 token 长度等），可按需调优。

## 核心功能

| 功能 | 描述 |
|------|------|
| **Agent** | 创建并管理代理，定义其角色、知识库、策略与目标。 |
| **Conversation** | 记录多轮对话，管理上下文与状态，支持回滚与重试。 |
| **Planner** | 基于任务步骤生成计划，支持子任务拆分与优先级调度。 |
| **Tool** | 调用外部工具（如搜索、数据库查询、API 调用），并将结果返回给代理。 |
| **Scheduler** | 控制代理执行顺序，支持并行与串行执行。 |
| **Safety** | 监控生成内容，提供过滤、提示与审计日志。 |

## 使用示例

```python
from autogen import ConversableAgent, AssistantAgent, OpenAI, ChatOpenAI

# 创建代理
assistant = AssistantAgent(
    name="assistant",
    llm=ChatOpenAI(model="gpt-4o-mini"),
    system_message="你是一个专业的技术支持助手。"
)

# 与用户对话
assistant.send("你好，我有一个问题。")
assistant.send("你能帮我解决吗？")

# 读取回复
response = assistant.receive()
print(response)
```

> 更多示例可参见 `examples/` 目录。

## 快速开始

1. 克隆仓库  
   ```bash
   git clone https://github.com/microsoft/autogen.git
   cd autogen
   ```

2. 安装依赖  
   ```bash
   pip install -e .
   ```

3. 运行示例  
   ```bash
   python examples/simple_chat.py
   ```

> 详细文档请查看项目的 `docs/` 目录和 `README.md`。

--- 

> **提示**：若要使用 Azure OpenAI，可在 `autogen/config.py` 中配置相关字段。  
> 详细配置请参阅官方文档。