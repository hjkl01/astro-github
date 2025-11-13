---
title: Agno
---

# Agno

Agno 是一个多代理框架、运行时和控制平面，专为速度、隐私和规模而构建。它提供丰富的工具来构建：

- **代理**：具有记忆、知识、会话管理的高级功能，如人类干预、护栏、动态上下文管理和一流的 MCP 支持。
- **多代理团队**：在团队领导下自主运行，维护共享状态和上下文。适用于超出单个代理范围的用例。
- **基于步骤的工作流**：用于受控、确定性执行。步骤可以是代理、团队或常规 Python 函数，按顺序、并行、循环、分支或条件运行。

Agno 还提供一个现成的 FastAPI 应用（称为 AgentOS），用于在生产中服务代理、团队和工作流。无状态、水平可扩展，专为规模而设计，为构建 AI 产品提供重大优势。

## 功能特性

### 核心智能

- **模型无关**：与任何模型提供商合作，使用您喜欢的 LLM。
- **类型安全**：通过 `input_schema` 和 `output_schema` 强制结构化 I/O，实现可预测、可组合的行为。
- **动态上下文工程**：动态将变量、状态和检索数据注入上下文。完美适用于依赖驱动的代理。

### 记忆、知识和持久性

- **持久存储**：为代理、团队和工作流提供数据库，以持久化会话历史、状态和消息。
- **用户记忆**：内置记忆系统，允许代理跨会话回忆用户特定上下文。
- **代理 RAG**：连接到 20+ 向量存储（在 Agno 中称为 **Knowledge**），开箱即用混合搜索 + 重排序。
- **文化（集体记忆）**：跨代理和时间共享知识。

### 执行和控制

- **人类干预**：原生支持确认、手动覆盖和外部工具执行。
- **护栏**：内置验证、安全和提示保护的安全措施。
- **代理生命周期钩子**：预和后钩子，用于验证或转换输入和输出。
- **MCP 集成**：一流支持模型上下文协议 (MCP)，将代理与外部系统连接。
- **工具包**：100+ 内置工具包，包含数千个工具，适用于数据、代码、网络和企业 API。

### 运行时和评估

- **运行时**：基于 FastAPI 的预构建运行时，具有 SSE 兼容端点，从第一天起就准备好生产。
- **控制平面 (UI)**：集成界面，用于实时可视化、监控和调试代理活动。
- **原生多模态**：代理可以处理和生成文本、图像、音频、视频和文件。
- **评估**：衡量代理的准确性、性能和可靠性。

### 安全和隐私

- **隐私设计**：完全在您的云中运行。UI 直接从浏览器连接到您的 AgentOS，从不发送数据到外部。
- **数据治理**：您的数据安全地存在于您的代理数据库中，无外部数据共享或供应商锁定。
- **访问控制**：基于角色的访问 (RBAC) 和每代理权限，以保护敏感上下文和工具。

## 用法

### 快速入门

如果您是 Agno 新手，请按照我们的 [快速入门](https://docs.agno.com/introduction/quickstart) 构建您的第一个代理，并使用 AgentOS UI 与其聊天。

之后，查看 [示例库](https://docs.agno.com/examples/introduction) 并使用 Agno 构建真实世界应用。

### 示例

以下是一个代理的示例，它连接到 MCP 服务器，在数据库中管理对话状态，使用 FastAPI 应用服务，您可以使用 [AgentOS UI](https://os.agno.com) 与其聊天。

```python
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

# ********** 创建代理 **********
agno_agent = Agent(
    name="Agno Agent",
    model=Claude(id="claude-sonnet-4-5"),
    # 为代理添加数据库
    db=SqliteDb(db_file="agno.db"),
    # 为代理添加 Agno MCP 服务器
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # 将之前的会话历史添加到上下文
    add_history_to_context=True,
    markdown=True,
)

# ********** 创建 AgentOS **********
agent_os = AgentOS(agents=[agno_agent])
# 获取 AgentOS 的 FastAPI 应用
app = agent_os.get_app()

# ********** 运行 AgentOS **********
if __name__ == "__main__":
    agent_os.serve(app="agno_agent:app", reload=True)
```

### AgentOS - 多代理系统的生产运行时

构建代理很容易，运行它们很难，这就是 AgentOS 的用武之地。AgentOS 是用于在生产中服务多代理系统的高性能运行时。主要功能包括：

1. **预构建 FastAPI 应用**：AgentOS 附带一个现成的 FastAPI 应用，用于编排代理、团队和工作流。这为您构建 AI 产品提供了重大优势。
2. **集成控制平面**：[AgentOS UI](https://os.agno.com) 直接连接到您的运行时，让您实时测试、监控和管理系统，提供无与伦比的控制。
3. **隐私设计**：AgentOS 完全在您的云中运行，确保完全数据隐私。从不发送数据离开您的系统。非常适合注重安全的企業。

### 性能

Agno 默认保证一流性能。我们对性能的痴迷是必要的，因为即使简单的 AI 工作流也可以产生数百个代理，并且许多任务是长期运行的——无状态、水平可扩展性是成功的关键。

Agno 在三个维度优化性能：

1. **代理性能**：优化静态操作（实例化、内存占用）和运行时操作（工具调用、内存更新、历史管理）。
2. **系统性能**：AgentOS API 默认异步，具有最小内存占用。系统无状态且水平可扩展，专注于防止内存泄漏。它在知识摄取期间处理并行和批量嵌入生成、在后台任务中收集指标等。
3. **代理可靠性和准确性**：通过评估监控，我们稍后会探讨。

### 代理性能

让我们测量实例化代理和代理内存占用的时间。这里是数字（最后测量于 2025 年 10 月，在 Apple M4 MacBook Pro 上）：

- **代理实例化**：平均 ~3μs
- **内存占用**：平均 ~6.6KiB

我们将展示 Agno 代理实例化比 Langgraph 快 **529 倍**，比 PydanticAI 快 **57 倍**，比 CrewAI 快 **70 倍**。Agno 代理也比 Langgraph 使用低 **24 倍** 内存，比 PydanticAI 低 **4 倍**，比 CrewAI 低 **10 倍**。

## 文档和社区

- 文档：[docs.agno.com](https://docs.agno.com)
- Cookbook：[Cookbook](https://github.com/agno-agi/agno/tree/main/cookbook)
- 社区论坛：[community.agno.com](https://community.agno.com/)
- Discord：[discord](https://discord.gg/4MtYHHrgA8)
