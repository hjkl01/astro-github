---
title: ADK-Go
---

# ADK-Go

## 项目简介

ADK-Go 是 Google 开发的开源 Go 工具包，用于构建、评估和部署复杂的 AI 代理。它采用代码优先的方法，提供灵活性和控制力，适用于从简单任务到复杂系统的代理工作流。虽然针对 Gemini 进行了优化，但它是模型无关的、部署无关的，并与其他框架兼容。

这个 Go 版本的 ADK 非常适合构建云原生代理应用程序，利用 Go 在并发和性能方面的优势。

## 主要功能

- **原生 Go 风格**：设计上感觉自然，并充分利用 Go 的强大功能。
- **丰富的工具生态**：使用预构建工具、自定义函数或集成现有工具，为代理提供多样化的能力。
- **代码优先开发**：直接在 Go 中定义代理逻辑、工具和编排，以实现终极灵活性、可测试性和版本控制。
- **模块化多代理系统**：通过组合多个专门代理来设计可扩展应用程序。
- **任意部署**：轻松容器化并部署代理，对云原生环境（如 Google Cloud Run）提供强大支持。

## 安装

要将 ADK Go 添加到您的项目中，请运行：

```bash
go get google.golang.org/adk
```

## 用法

ADK-Go 允许开发者使用 Go 代码定义代理的行为、工具和交互。以下是一个基本示例（基于项目示例）：

1. 定义代理：使用 ADK 的 API 创建代理实例，配置模型和工具。
2. 添加工具：集成自定义函数或预构建工具，如搜索、计算等。
3. 运行代理：启动代理以处理任务或对话。
4. 部署：将代理打包为容器，并在云环境中运行。

详细用法请参考 [官方文档](https://google.github.io/adk-docs/) 和 [示例代码](https://github.com/google/adk-go/tree/main/examples)。

## 相关链接

- [官方文档](https://google.github.io/adk-docs/)
- [示例代码](https://github.com/google/adk-go/tree/main/examples)
- [Python ADK](https://github.com/google/adk-python)
- [Java ADK](https://github.com/google/adk-java)
- [ADK Web](https://github.com/google/adk-web)
