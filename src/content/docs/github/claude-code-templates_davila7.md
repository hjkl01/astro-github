---
title: claude-code-templates
---

# claude-code-templates

这是一个用于配置和监控 Anthropic Claude Code 的 CLI 工具，提供现成的 AI 代理、自定义命令、设置、钩子、外部集成（MCPs）和项目模板，以增强开发工作流程。

## 功能特性

- **🤖 AI 代理**：针对特定领域的 AI 专家，如安全审计员、React 性能优化器、数据库架构师
- **⚡ 自定义命令**：斜杠命令，如 `/generate-tests`、`/optimize-bundle`、`/check-security`
- **🔌 MCPs**：外部服务集成，如 GitHub、PostgreSQL、Stripe、AWS、OpenAI
- **⚙️ 设置**：Claude Code 配置，如超时、内存设置、输出样式
- **🪝 钩子**：自动化触发器，如预提交验证、完成后的操作
- **🎨 技能**：可重用的能力，具有渐进式披露，如 PDF 处理、Excel 自动化、自定义工作流程

## 额外工具

- **📊 Claude Code Analytics**：实时监控 AI 驱动的开发会话，包括实时状态检测和性能指标
- **💬 Conversation Monitor**：移动优化界面，实时查看 Claude 响应，支持安全远程访问
- **🔍 Health Check**：全面诊断，确保 Claude Code 安装优化
- **🔌 Plugin Dashboard**：从统一界面查看市场、已安装插件和管理权限

## 安装和使用

### 快速安装

```bash
# 安装完整开发栈
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# 交互式浏览和安装
npx claude-code-templates@latest

# 安装特定组件
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

### 工具使用

```bash
# Claude Code Analytics
npx claude-code-templates@latest --analytics

# 本地访问 Conversation Monitor
npx claude-code-templates@latest --chats

# 通过 Cloudflare Tunnel 安全远程访问
npx claude-code-templates@latest --chats --tunnel

# Health Check
npx claude-code-templates@latest --health-check

# Plugin Dashboard
npx claude-code-templates@latest --plugins
```

## 文档和资源

- **🌐 浏览模板**：[aitmpl.com](https://aitmpl.com)
- **📚 文档**：[docs.aitmpl.com](https://docs.aitmpl.com)
- **💬 社区**：[GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
- **🐛 问题**：[GitHub Issues](https://github.com/davila7/claude-code-templates/issues)

## 许可证

本项目采用 MIT 许可证。
