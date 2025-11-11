---
title: claudecode.nvim
---

# claudecode.nvim

> Description from GitHub: 🧩 Claude Code Neovim IDE Extension

## 主要特性

- 🚀 **纯 Lua，零依赖** — 完全使用 `vim.loop` 和 Neovim 内置构建
- 🔌 **100% 协议兼容** — 与官方扩展相同的 WebSocket MCP 实现
- 🎓 **完全记录协议** — 学习如何构建自己的集成（参见 PROTOCOL.md）
- 🏆 **第一个上市** — 在 Anthropic 发布 Neovim 支持之前击败他们
- 🤖 **使用 AI 构建** — 使用 Claude 逆向工程 Claude 自己的协议

## 工作原理

此插件创建 WebSocket 服务器，Claude Code CLI 连接到该服务器，实现与官方 VS Code 扩展相同的协议。当您启动 Claude 时，它会自动检测 Neovim 并获得对您编辑器的完全访问权限。

协议使用 WebSocket 变体的 MCP（模型上下文协议），该协议：

1. 在随机端口上创建 WebSocket 服务器
2. 将连接信息写入 `~/.claude/ide/[port].lock`（或 `$CLAUDE_CONFIG_DIR/ide/[port].lock` 如果设置了 `CLAUDE_CONFIG_DIR`）
3. 设置告诉 Claude 在哪里连接的环境变量
4. 实现 Claude 可以调用的 MCP 工具

📖 **[阅读完整的逆向工程故事 →](/coder/claudecode.nvim/blob/main/STORY.md)** 🔧 **[完整的协议文档 →](/coder/claudecode.nvim/blob/main/PROTOCOL.md)**
