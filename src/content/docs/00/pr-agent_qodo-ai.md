---
title: Pr Agent
---

# pr-agent

## 功能

PR-Agent 是一个由 AI 驱动的工具，用于自动化拉取请求（Pull Request）的分析、反馈、建议等。它是第一个用于 PR 的 AI 助手，由 Qodo 团队构建并开源。

主要功能包括：

- 自动分析 PR 的代码变更
- 提供智能反馈和改进建议
- 生成 PR 描述和总结
- 代码审查和质量检查
- 支持多种命令如 /review, /describe, /improve 等

这是一个开源的 legacy 版本，Qodo 提供了更先进的付费版本。

## 用法

PR-Agent 可以作为 GitHub Action 或 CLI 工具使用。

### 安装

通过 pip 安装：

```bash
pip install pr-agent
```

### 配置

需要配置 OpenAI API key 和 GitHub token：

```bash
export OPENAI_API_KEY=your_key
export GITHUB_TOKEN=your_token
```

### GitHub Action 使用

在 `.github/workflows/pr-agent.yml` 中添加：

```yaml
name: PR Agent
on:
  pull_request:
    types: [opened, reopened, synchronize]

jobs:
  pr_agent:
    runs-on: ubuntu-latest
    steps:
      - uses: qodo-ai/pr-agent@latest
        with:
          command: /review
```

### CLI 使用

```bash
pr-agent --pr_url https://github.com/owner/repo/pull/123 --command /review
```

更多用法请参考官方文档。
