---
title: agent-starter-pack
---

# agent-starter-pack

## 项目简介

agent-starter-pack 是 Google Cloud Platform 提供的一个生产就绪的生成式 AI 代理模板集合。它旨在加速开发，通过提供全面的生产就绪解决方案，解决构建和部署 GenAI 代理中的常见挑战，包括部署与运营、评估、定制和可观测性。

## 主要功能

- **预构建代理模板**：提供多种代理模板，如 ReAct、RAG、多代理系统和实时 API 支持。
- **评估与测试**：集成 Vertex AI 评估和交互式游乐场，用于测试代理性能。
- **生产基础设施**：支持监控、可观测性和 CI/CD 自动化，部署到 Cloud Run 或 Agent Engine。
- **定制与扩展**：允许根据需求扩展和定制模板。
- **Gemini CLI 集成**：与 Gemini CLI 结合，提供终端中的指导和代码示例。

## 使用方法

### 安装

使用 `uv`（推荐）：

```bash
uvx agent-starter-pack create my-awesome-agent
```

或使用 `pip`：

```bash
# 创建并激活 Python 虚拟环境
python -m venv .venv && source .venv/bin/activate

# 安装 agent-starter-pack
pip install --upgrade agent-starter-pack

# 创建新代理项目
agent-starter-pack create my-awesome-agent
```

### 增强现有代理

如果已有代理项目，在项目根目录运行：

```bash
uvx agent-starter-pack enhance
```

### 部署

项目提供完整的 CI/CD 管道，支持 Google Cloud Build 和 GitHub Actions。一键设置生产环境。

## 文档与资源

- [官方文档](https://googlecloudplatform.github.io/agent-starter-pack/)
- [快速开始指南](https://googlecloudplatform.github.io/agent-starter-pack/guide/getting-started)
- [部署指南](https://googlecloudplatform.github.io/agent-starter-pack/guide/deployment)

## 社区展示

查看使用 agent-starter-pack 构建的精彩项目：[社区展示](https://googlecloudplatform.github.io/agent-starter-pack/guide/community-showcase)。
