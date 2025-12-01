---
title: claude-task-master
---

# Claude Task Master 功能和使用总结

## 功能

Claude Task Master 是一个专为 AI 驱动开发设计的任务管理系统，能够无缝集成任何 AI 聊天工具。它提供以下核心功能：

- **任务管理**：解析产品需求文档 (PRD)，自动生成和管理开发任务，支持任务状态跟踪、依赖关系和标签管理。
- **AI 集成**：支持多种 AI 模型（如 Claude、OpenAI、Google Gemini 等），用于任务规划、代码生成和研究。
- **研究功能**：集成研究模型，帮助获取最新技术信息和最佳实践。
- **项目初始化**：自动设置项目结构，生成模板和配置文件。
- **多编辑器支持**：兼容 Cursor、VS Code、Windsurf 等，支持 MCP (Model Control Protocol) 协议。
- **命令行工具**：提供 CLI 界面，支持任务列表、状态更新、研究查询等操作。

## 使用

### 安装和配置

1. **MCP 安装（推荐）**：
   - 在编辑器配置文件中添加 `task-master-ai` 服务器。
   - 配置 API 密钥（如 ANTHROPIC_API_KEY、OPENAI_API_KEY 等）。
   - 重启编辑器并启用 MCP。

2. **CLI 安装**：
   ```bash
   npm install -g task-master-ai
   task-master init
   ```

### 基本使用

- **初始化项目**：在 AI 聊天中说 "Initialize taskmaster-ai in my project" 或运行 `task-master init`。
- **解析需求**：创建 PRD 文件，然后说 "Can you parse my PRD at scripts/prd.txt?"。
- **任务操作**：
  - 查看任务：`task-master list` 或 "What's the next task I should work on?"
  - 实现任务：`task-master show 1` 或 "Can you help me implement task 3?"
  - 研究信息：`task-master research "latest best practices for JWT authentication"`
- **模型配置**：在聊天中指定主模型、研究模型和备用模型。

### 工具优化

通过设置 `TASK_MASTER_TOOLS` 环境变量优化工具加载：

- `core`：7 个核心工具（~5000 tokens）
- `standard`：15 个标准工具（~10000 tokens）
- `all`：36 个全部工具（~21000 tokens，默认）

支持 Claude Code 无需 API 密钥使用本地 Claude 实例。
