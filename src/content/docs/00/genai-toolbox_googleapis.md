---
title: Genai Toolbox
---

# genai-toolbox

## 功能介绍

MCP Toolbox for Databases 是一个开源的 MCP 服务器，专为数据库设计。它简化了生成式 AI 工具的开发，使代理能够安全、高效地访问数据库数据。该工具处理连接池、认证和可观察性等复杂性，提供以下核心功能：

- **简化开发**：只需几行代码即可将工具集成到代理中，支持在多个代理或框架间复用工具，并轻松部署新版本。
- **性能优化**：内置最佳实践，如连接池和认证，提升数据访问效率。
- **增强安全性**：集成认证机制，确保数据访问的安全性。
- **端到端可观察性**：提供开箱即用的指标和追踪，支持 OpenTelemetry。
- **AI 数据库助手**：通过 MCP 将 IDE 连接到数据库，让 AI 助手成为真正的共同开发者，支持自然语言查询、管理数据库和生成上下文感知代码。

该工具支持多种数据库类型，包括 PostgreSQL、MySQL、BigQuery 等，并提供预构建工具和自定义工具选项。

## 用法

### 安装

支持多种安装方式：

- **二进制**：从 [releases 页面](https://github.com/googleapis/genai-toolbox/releases) 下载对应平台的二进制文件。
- **容器**：使用 Docker 拉取镜像 `us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:$VERSION`。
- **Homebrew**：运行 `brew install mcp-toolbox`。
- **源码编译**：确保安装 Go，然后运行 `go install github.com/googleapis/genai-toolbox@v0.19.1`。
- **Gemini CLI 扩展**：运行 `gemini extensions install https://github.com/gemini-cli-extensions/mcp-toolbox`。

### 运行服务器

1. 配置 `tools.yaml` 文件，定义数据源、工具和工具集。
2. 启动服务器：
   - 二进制：`./toolbox --tools-file "tools.yaml"`
   - 容器：`docker run -p 5000:5000 -v $(pwd)/tools.yaml:/app/tools.yaml us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:$VERSION --tools-file "/app/tools.yaml"`
   - Homebrew：`toolbox --tools-file "tools.yaml"`

服务器默认启用动态重载，可通过 `--disable-reload` 禁用。

### 集成到应用

使用官方 SDK 将工具加载到应用中：

- **Python**：支持 Core、LangChain、LlamaIndex 等框架。安装 `pip install toolbox-core`，然后使用 `ToolboxClient` 加载工具集。
- **JavaScript/TypeScript**：支持 Core、LangChain、Genkit 等。安装 `npm install @toolbox-sdk/core`，使用 `ToolboxClient` 加载工具。
- **Go**：支持 Core、LangChain Go、Genkit、Go GenAI、OpenAI Go、ADK Go 等。安装 `go get github.com/googleapis/mcp-toolbox-sdk-go`，使用 `core.NewToolboxClient` 加载工具。

### 配置

通过 `tools.yaml` 配置：

- **Sources**：定义数据源，如 PostgreSQL 连接。
- **Tools**：定义工具，包括类型、数据源、参数和 SQL 语句。
- **Toolsets**：分组工具，便于按代理或应用加载。

### 与 Gemini CLI 扩展一起使用

安装扩展后，可使用自然语言与数据源交互。支持预构建工具（如 AlloyDB、BigQuery、Cloud SQL 等）和自定义工具。

更多详情请参考 [官方文档](https://googleapis.github.io/genai-toolbox/)。
