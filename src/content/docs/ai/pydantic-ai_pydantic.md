---
title: pydantic-ai
---

# Pydantic AI

## 功能介绍

Pydantic AI 是一个 Python 代理框架，旨在帮助开发者快速、自信且轻松地构建生产级别的生成式 AI 应用程序和工作流。它由 Pydantic 团队构建，基于 Pydantic Validation 和现代 Python 特性，如类型提示。

### 主要特性

- **模型无关性**：支持几乎所有模型和提供商，包括 OpenAI、Anthropic、Gemini、DeepSeek、Grok 等。
- **无缝可观测性**：与 Pydantic Logfire 紧密集成，提供实时调试、评估性能监控、行为追踪和成本追踪。
- **完全类型安全**：设计为提供 IDE 或 AI 编码代理尽可能多的上下文，用于自动补全和类型检查。
- **强大的评估**：允许系统地测试和评估构建的代理系统性能，并通过 Pydantic Logfire 监控性能。
- **MCP、A2A 和 UI**：集成模型上下文协议、代理到代理和各种 UI 事件流标准。
- **人工干预工具批准**：轻松标记某些工具调用需要批准。
- **持久执行**：构建持久代理，能够在瞬时 API 失败和应用程序错误或重启中保留进度。
- **流式输出**：提供连续流式结构化输出，具有即时验证。
- **图支持**：使用类型提示定义图，用于复杂应用程序。

## 用法示例

### Hello World 示例

```python
from pydantic_ai import Agent

# 定义一个简单的代理，包括使用的模型
agent = Agent(
    'anthropic:claude-sonnet-4-0',
    instructions='Be concise, reply with one sentence.',
)

# 同步运行代理
result = agent.run_sync('Where does "hello world" come from?')
print(result.output)
# 输出: The first known use of "hello, world" was in a 1974 textbook about the C programming language.
```

### 工具和依赖注入示例

```python
from dataclasses import dataclass
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

@dataclass
class SupportDependencies:
    customer_id: int
    db: DatabaseConn

class SupportOutput(BaseModel):
    support_advice: str = Field(description='Advice returned to the customer')
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description='Risk level of query', ge=0, le=10)

support_agent = Agent(
    'openai:gpt-5',
    deps_type=SupportDependencies,
    output_type=SupportOutput,
    instructions='You are a support agent in our bank, give the customer support and judge the risk level of their query.',
)

@support_agent.tool
async def customer_balance(ctx: RunContext[SupportDependencies], include_pending: bool) -> float:
    """Returns the customer's current account balance."""
    balance = await ctx.deps.db.customer_balance(
        id=ctx.deps.customer_id,
        include_pending=include_pending,
    )
    return balance

# 异步运行代理
async def main():
    deps = SupportDependencies(customer_id=123, db=DatabaseConn())
    result = await support_agent.run('What is my balance?', deps=deps)
    print(result.output)
```

更多详细信息请参考 [官方文档](https://ai.pydantic.dev/)。
