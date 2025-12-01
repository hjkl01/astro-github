---
title: aichat
---

# aichat

aichat 是一个全功能的 LLM CLI 工具，提供 Shell 助手、Chat-REPL、RAG、AI 工具和代理功能，支持 OpenAI、Claude、Gemini、Ollama、Groq 等多个提供商。

## 功能

- **多提供商支持**：统一接口集成 20+ LLM 提供商，包括 OpenAI、Claude、Gemini、Ollama 等。
- **CMD 模式**：强大的命令行功能。
- **REPL 模式**：交互式 Chat-REPL，支持自动补全、多行输入、历史搜索等。
- **Shell 助手**：将自然语言描述转换为精确的 shell 命令，适应操作系统和 shell 环境。
- **多形式输入**：支持 stdin、本地文件/目录、远程 URL 等输入形式。
- **角色**：自定义角色以调整 LLM 行为，提高效率。
- **会话**：维护上下文感知的对话，确保连续性。
- **宏**：将一系列 REPL 命令组合成自定义宏。
- **RAG**：将外部文档集成到对话中，提供更准确的响应。
- **函数调用**：连接外部工具和数据源，包括 AI 工具和代理。
- **本地服务器**：内置轻量级 HTTP 服务器，提供 API 和 Web 界面（如 Playground 和 Arena）。
- **自定义主题**：支持暗色和亮色主题，高亮响应文本和代码块。

## 用法

### 安装

- Rust 开发者：`cargo install aichat`
- Homebrew/Linuxbrew 用户：`brew install aichat`
- Pacman 用户：`pacman -S aichat`
- Windows Scoop 用户：`scoop install aichat`
- Android Termux 用户：`pkg install aichat`

或从 [GitHub Releases](https://github.com/sigoden/aichat/releases) 下载预构建二进制文件。

### 基本用法

- CMD 模式：`aichat "hello"`
- REPL 模式：`aichat`（进入交互式模式）
- Shell 助手：`aichat --execute "list files in current directory"`
- 文件输入：`aichat -f file.txt "summarize this"`
- 会话：`aichat --session session_name`
- 服务器模式：`aichat --serve`（启动本地服务器，提供 API 和 Web UI）

### 配置

首次运行时会创建配置文件。支持环境变量和 YAML 配置。详见 [配置指南](https://github.com/sigoden/aichat/wiki/Configuration-Guide)。

### 更多文档

- [Chat-REPL 指南](https://github.com/sigoden/aichat/wiki/Chat-REPL-Guide)
- [命令行指南](https://github.com/sigoden/aichat/wiki/Command-Line-Guide)
- [角色指南](https://github.com/sigoden/aichat/wiki/Role-Guide)
- [RAG 指南](https://github.com/sigoden/aichat/wiki/RAG-Guide)
- [FAQ](https://github.com/sigoden/aichat/wiki/FAQ)
