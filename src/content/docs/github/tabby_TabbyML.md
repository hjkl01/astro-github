---
title: tabby
---

# Tabby

Tabby 是一个自托管的 AI 编码助手，提供开源且本地部署的 GitHub Copilot 替代方案。它具有以下主要特点：

- **自包含**：无需数据库管理系统或云服务，完全本地运行。
- **易集成**：提供 OpenAPI 接口，便于与现有基础设施（如云 IDE）集成。
- **硬件支持**：支持消费级 GPU。

## 主要功能

- **代码补全**：基于 AI 的智能代码补全，支持多种编程语言。
- **聊天界面**：内置聊天功能，可与 AI 助手对话，获取编码建议。
- **Answer Engine**：知识引擎，可集成团队内部数据，提供精准答案。
- **多模型支持**：支持多种后端聊天模型，如 Qwen2、CodeLlama 等。
- **集成工具**：支持 GitHub、GitLab 等代码仓库集成，提供上下文感知。

## 安装和使用

### 快速启动（1 分钟内）

使用 Docker 运行 Tabby 服务：

```bash
docker run -it \
  --gpus all -p 8080:8080 -v $HOME/.tabby:/data \
  tabbyml/tabby \
  serve --model StarCoder-1B --device cuda --chat-model Qwen2-1.5B-Instruct
```

这将在本地启动 Tabby 服务，端口 8080 可访问 Web 界面。

### IDE 扩展

Tabby 支持多种编辑器扩展：

- **VS Code**：安装 Tabby 扩展，支持内联补全和侧边栏聊天。
- **Vim/Neovim**：通过插件集成。
- **IntelliJ IDEA**：JetBrains 插件市场下载。

更多配置和选项请参考 [官方文档](https://tabby.tabbyml.com/docs/)。

## 社区和贡献

Tabby 是开源项目，欢迎贡献代码。访问 [GitHub 仓库](https://github.com/TabbyML/tabby) 获取源码和参与开发。
