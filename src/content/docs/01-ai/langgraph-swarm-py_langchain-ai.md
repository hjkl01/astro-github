---
title: langgraph-swarm-py
---

# LangGraph Swarm Py

## 项目简介

LangGraph Swarm Py 是一个 Python 库，用于使用 [LangGraph](https://github.com/langchain-ai/langgraph) 创建 swarm-style 多代理系统。Swarm 是一种多代理架构，其中代理根据其专业化动态地将控制权移交给彼此。系统会记住最后一个活跃的代理，确保在后续交互中从该代理继续对话。

## 功能特性

- **多代理协作**：允许专门化的代理协同工作，并相互传递上下文。
- **可定制的手动工具**：内置工具用于代理之间的通信。
- **基于 LangGraph**：支持流式处理、短期和长期记忆、人机交互等功能。

注意：此库已更新以支持 LangChain 1.0，但尚未与新的 `langchain.agents` 中的代理进行测试。目前仅支持预构建的 `langgraph.prebuilt.create_react_agent`。

## 安装

```bash
pip install langgraph-swarm
```

## 快速开始

首先安装必要的依赖：

```bash
pip install langgraph-swarm langchain-openai
```

设置环境变量：

```bash
export OPENAI_API_KEY=<your_api_key>
```

示例代码：

```python
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_swarm import create_handoff_tool, create_swarm

model = ChatOpenAI(model="gpt-4o")

def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

alice = create_react_agent(
    model,
    [add, create_handoff_tool(agent_name="Bob")],
    prompt="You are Alice, an addition expert.",
    name="Alice",
)

bob = create_react_agent(
    model,
    [create_handoff_tool(agent_name="Alice", description="Transfer to Alice, she can help with math")],
    prompt="You are Bob, you speak like a pirate.",
    name="Bob",
)

checkpointer = InMemorySaver()
workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice"
)
app = workflow.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "1"}}
turn_1 = app.invoke(
    {"messages": [{"role": "user", "content": "i'd like to speak to Bob"}]},
    config,
)
print(turn_1)
turn_2 = app.invoke(
    {"messages": [{"role": "user", "content": "what's 5 + 7?"}]},
    config,
)
print(turn_2)
```

## 记忆功能

您可以为 swarm 多代理系统添加短期和长期记忆。由于 `create_swarm()` 返回一个需要在使用前编译的 `StateGraph` 实例，您可以直接将 checkpointer 或 store 实例传递给 `.compile()` 方法：

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

# 短期记忆
checkpointer = InMemorySaver()
# 长期记忆
store = InMemoryStore()

model = ...
alice = ...
bob = ...

workflow = create_swarm(
    [alice, bob],
    default_active_agent="Alice"
)

# 使用 checkpointer/store 编译
app = workflow.compile(
    checkpointer=checkpointer,
    store=store
)
```

重要提示：添加短期记忆对于在多个交互中保持对话状态至关重要。没有它，swarm 会“忘记”最后一个活跃的代理并丢失对话历史。如果计划在多轮对话中使用，请务必使用 checkpointer 编译 swarm，例如 `workflow.compile(checkpointer=checkpointer)`。

## 自定义

您可以通过更改手动工具实现或代理实现来自定义多代理 swarm。

### 自定义手动工具

默认情况下，swarm 中的代理使用由预构建的 `create_handoff_tool` 创建的手动工具。您也可以创建自己的自定义手动工具。例如：

```python
from typing import Annotated
from langchain_core.tools import tool, BaseTool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langgraph.types import Command
from langgraph.prebuilt import InjectedState

def create_custom_handoff_tool(*, agent_name: str, name: str | None, description: str | None) -> BaseTool:
    @tool(name, description=description)
    def handoff_to_agent(
        task_description: Annotated[str, "Detailed description of what the next agent should do, including all of the relevant context."],
        state: Annotated[dict, InjectedState],
        tool_call_id: Annotated[str, InjectedToolCallId],
    ):
        tool_message = ToolMessage(
            content=f"Successfully transferred to {agent_name}",
            name=name,
            tool_call_id=tool_call_id,
        )
        messages = state["messages"]
        return Command(
            goto=agent_name,
            graph=Command.PARENT,
            update={
                "messages": messages + [tool_message],
                "active_agent": agent_name,
                "task_description": task_description,
            },
        )
    return handoff_to_agent
```

### 自定义代理实现

默认情况下，各个代理通过共享的 `messages` 键进行通信，这意味着所有代理的消息将合并到一个共享的消息列表中。如果您不想暴露代理的内部消息历史，可以自定义代理：

1. 使用自定义状态模式，其中消息使用不同的键，例如 `alice_messages`。
2. 编写一个包装器，将父图状态转换为子代理状态并返回。

然后，您可以手动创建 swarm：

```python
from typing_extensions import TypedDict, Annotated
from langchain_core.messages import AnyMessage
from langgraph.graph import StateGraph, add_messages
from langgraph_swarm import SwarmState

class AliceState(TypedDict):
    alice_messages: Annotated[list[AnyMessage], add_messages]

alice = (
    StateGraph(AliceState)
    .add_node("model", ...)
    .add_node("tools", ...)
    .add_edge(...)
    ...
    .compile()
)

def call_alice(state: SwarmState):
    response = alice.invoke({"alice_messages": state["messages"]})
    return {"messages": response["alice_messages"]}

def call_bob(state: SwarmState):
    ...

from langgraph_swarm import add_active_agent_router

workflow = (
    StateGraph(SwarmState)
    .add_node("Alice", call_alice, destinations=("Bob",))
    .add_node("Bob", call_bob, destinations=("Alice",))
)
workflow = add_active_agent_router(
    builder=workflow,
    route_to=["Alice", "Bob"],
    default_active_agent="Alice",
)

app = workflow.compile()
```

## 许可证

MIT License

## 链接

- [GitHub 仓库](https://github.com/langchain-ai/langgraph-swarm-py)
- [LangGraph 多代理概念](https://langchain-ai.github.io/langgraph/concepts/multi_agent/)
