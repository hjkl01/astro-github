---
title: rogue
---

# Rogue - AI Agent Evaluator

Rogue 是一个强大的工具，旨在评估 AI agents 的性能、合规性和可靠性。它使用动态的 `EvaluatorAgent` 与您的 agent 进行对抗，使用各种协议对其进行一系列场景测试，以确保其行为完全符合预期。

## 功能特性

- **动态场景生成**：从您的高级业务上下文自动创建全面的测试套件。
- **实时评估监控**：在实时聊天界面中观察评估器与您的 agent 之间的交互。
- **全面报告**：生成详细的评估摘要，包括通过/失败率、关键发现和建议。
- **多方面测试**：原生支持政策合规测试，具有灵活的框架，可扩展到其他领域，如提示注入或安全。
- **广泛模型支持**：兼容来自 OpenAI、Google (Gemini) 和 Anthropic 等提供商的各种模型。
- **用户友好界面**：简单的分步 Gradio UI 指导您完成配置、执行和报告。

## 架构

Rogue 采用客户端-服务器架构：

- **Rogue Server**：包含核心评估逻辑。
- **客户端接口**：多个接口连接到服务器：
  - **TUI (Terminal UI)**：使用 Go 和 Bubble Tea 构建的现代终端界面。
  - **Web UI**：基于 Gradio 的 Web 界面。
  - **CLI**：用于自动化评估和 CI/CD 的命令行界面。

这种架构允许灵活的部署和使用模式，其中服务器可以独立运行，多个客户端可以同时连接。

## 支持的协议和传输

Rogue 可以使用各种协议和传输与您的 agent 通信：

### A2A

Rogue 支持 Google 的 A2A 协议，通过以下传输：

1. HTTP

要使用 A2A 将您的 agent 与 Rogue 集成：

1. 使用任何框架构建您的 agent。
2. 通过 A2A 兼容的 HTTP 服务器公开您的 agent。
3. Rogue 将使用标准化的 A2A 协议与您的 agent 通信。

### MCP

Rogue 支持 Model Context Protocol (MCP)，通过以下传输：

1. SSE (Server-Sent Events)
2. STREAMABLE_HTTP

要使用 MCP 将您的 agent 与 Rogue 集成：

1. 使用任何框架构建您的 agent。
2. 使用名为 `send_message` 的工具将您的 agent 包装在 MCP 服务器中。
3. Rogue 将调用此工具与您的 agent 通信和评估。

## 快速开始

### 先决条件

- `uvx` - 如果未安装，请按照 [uv 安装指南](https://docs.astral.sh/uv/getting-started/installation/) 操作。
- Python 3.10+
- LLM 提供商的 API 密钥（例如 OpenAI、Google、Anthropic）。

### 安装

#### 选项 1：快速安装（推荐）

使用我们的自动化安装脚本快速启动：

```bash
# TUI
uvx rogue-ai

# Web UI
uvx rogue-ai ui

# CLI / CI/CD
uvx rogue-ai cli
```

#### 选项 2：手动安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/qualifire-dev/rogue.git
   cd rogue
   ```

2. 安装依赖：
   如果使用 uv：

   ```bash
   uv sync
   ```

   或使用 pip：

   ```bash
   pip install -e .
   ```

3. 可选：设置环境变量。在根目录创建 `.env` 文件并添加您的 API 密钥。Rogue 使用 `LiteLLM`，因此您可以为各种提供商设置密钥。
   ```
   OPENAI_API_KEY="sk-..."
   ANTHROPIC_API_KEY="sk-..."
   GOOGLE_API_KEY="..."
   ```

### 运行 Rogue

Rogue 采用客户端-服务器架构，其中核心评估逻辑在后端服务器中运行，各种客户端连接到它以获取不同接口。

#### 默认行为

运行 `uvx rogue-ai` 时，如果未指定模式，它将：

1. 在后台启动 Rogue 服务器。
2. 启动 TUI（终端用户界面）客户端。

```bash
uvx rogue-ai
```

#### 可用模式

- **默认（服务器 + TUI）**：`uvx rogue-ai` - 在后台启动服务器 + TUI 客户端。
- **服务器**：`uvx rogue-ai server` - 仅运行后端服务器。
- **TUI**：`uvx rogue-ai tui` - 仅运行 TUI 客户端（需要服务器运行）。
- **Web UI**：`uvx rogue-ai ui` - 仅运行 Gradio Web 界面客户端（需要服务器运行）。
- **CLI**：`uvx rogue-ai cli` - 运行非交互式命令行评估（需要服务器运行，非常适合 CI/CD）。

#### 模式参数

##### 服务器模式

```bash
uvx rogue-ai server [OPTIONS]
```

选项：

- `--host HOST` - 运行服务器的主机（默认：127.0.0.1 或 HOST 环境变量）。
- `--port PORT` - 运行服务器的端口（默认：8000 或 PORT 环境变量）。
- `--debug` - 启用调试日志。

##### TUI 模式

```bash
uvx rogue-ai tui [OPTIONS]
```

##### Web UI 模式

```bash
uvx rogue-ai ui [OPTIONS]
```

选项：

- `--rogue-server-url URL` - Rogue 服务器 URL（默认：http://localhost:8000）。
- `--port PORT` - 运行 UI 的端口。
- `--workdir WORKDIR` - 工作目录（默认：./.rogue）。
- `--debug` - 启用调试日志。

##### CLI 模式

```bash
uvx rogue-ai cli [OPTIONS]
```

选项：

- `--config-file FILE` - 配置文件的路径。
- `--rogue-server-url URL` - Rogue 服务器 URL（默认：http://localhost:8000）。
- `--evaluated-agent-url URL` - 要评估的 agent 的 URL。
- `--evaluated-agent-auth-type TYPE` - 认证方法（no_auth, api_key, bearer_token, basic）。
- `--evaluated-agent-credentials CREDS` - agent 的凭据。
- `--input-scenarios-file FILE` - 场景文件的路径（默认：/scenarios.json）。
- `--output-report-file FILE` - 输出报告文件的路径。
- `--judge-llm MODEL` - 用于评估和报告生成的模型。
- `--judge-llm-api-key KEY` - LLM 提供商的 API 密钥。
- `--business-context TEXT` - 业务上下文描述。
- `--business-context-file FILE` - 业务上下文文件的路径。
- `--deep-test-mode` - 启用深度测试模式。
- `--workdir WORKDIR` - 工作目录（默认：./.rogue）。
- `--debug` - 启用调试日志。

## 示例：测试 T-Shirt Store Agent

此仓库包含一个简单的示例 agent，用于销售 T 恤。您可以使用它来查看 Rogue 的实际运行。

### 选项 1：一体化（推荐）

使用 `--example` 标志，这是尝试 Rogue 与示例 agent 的最简单方法，它会自动启动 Rogue 和示例 agent：

```bash
uvx rogue-ai --example=tshirt_store
```

这将：

- 在 http://localhost:10001 上启动 T-Shirt Store agent。
- 启动 Rogue 的 TUI 界面。
- 退出时自动清理。

您可以自定义主机和端口：

```bash
uvx rogue-ai --example=tshirt_store --example-host localhost --example-port 10001
```

### 选项 2：手动设置

如果您更喜欢单独运行示例 agent：

1. 安装示例依赖：
   如果使用 uv：

   ```bash
   uv sync --group examples
   ```

   或使用 pip：

   ```bash
   pip install -e .[examples]
   ```

2. 在单独的终端中启动示例 agent 服务器：
   如果使用 uv：

   ```bash
   uv run python -m examples.tshirt_store_agent
   ```

   或使用脚本命令：

   ```bash
   uv run rogue-ai-example-tshirt
   ```

   或如果已安装：

   ```bash
   uvx rogue-ai-example-tshirt
   ```

   这将在 http://localhost:10001 上启动 agent。

3. 在 UI 中配置 Rogue 以指向示例 agent：
   - **Agent URL**：http://localhost:10001
   - **认证**：no-auth

4. 启动评估并观看 Rogue 测试 T-Shirt agent 的策略！

您可以使用 TUI（`uvx rogue-ai`）或 Web UI（`uvx rogue-ai ui`）模式。

## 如何工作

Rogue 的工作流程设计为简单直观，完全通过其 Web 界面管理。

1. **配置**：您提供要测试的 agent 的端点和认证详情，并选择 Rogue 用于其服务（场景生成、判断）的 LLM。
2. **生成场景**：您输入“业务上下文”或您的 agent 应该做什么的高级描述。Rogue 的 `LLM Service` 使用此上下文生成相关测试场景的列表。您可以审查和编辑这些场景。
3. **运行和评估**：您启动评估。`Scenario Evaluation Service` 启动 `EvaluatorAgent`，它为每个场景开始与您的 agent 的对话。您可以实时观看此对话发生。
4. **查看报告**：一旦所有场景完成，`LLM Service` 分析结果并生成 Markdown 格式的报告，为您提供 agent 性能的清晰摘要。

## 贡献

欢迎贡献！如果您想贡献，请遵循以下步骤：

1. Fork 仓库。
2. 创建新分支（`git checkout -b feature/your-feature-name`）。
3. 进行更改并提交（`git commit -m 'Add some feature'`）。
4. 推送到分支（`git push origin feature/your-feature-name`）。
5. 打开拉取请求。

请确保相应地更新测试。

## 许可证

此项目根据许可证授权 - 请参阅 [LICENSE](https://github.com/qualifire-dev/rogue/blob/main/LICENSE.md) 文件以获取详情。这意味着您可以免费使用此软件，但不允许托管和销售此软件。

如果您对许可证和此项目的商业使用有任何疑问，请发送邮件至 `admin@qualifire.ai`。
