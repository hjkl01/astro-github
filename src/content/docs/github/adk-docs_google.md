---
title: repository
---

# Agent Development Kit (ADK)

Agent Development Kit (ADK) 是一个开源的、代码优先的工具包，用于构建、评估和部署具有灵活性和控制能力的复杂 AI 代理。

## 项目概述

ADK 是一个灵活且模块化的框架，专门用于**开发和部署 AI 代理**。虽然针对 Gemini 和 Google 生态系统进行了优化，但 ADK 是**模型无关的**、**部署无关的**，并且构建时考虑了**与其他框架的兼容性**。ADK 的设计目标是让代理开发更像软件开发，使开发者更容易创建、部署和编排从简单任务到复杂工作流的代理架构。

## 主要特性

- **丰富的工具生态系统**：利用预构建工具、自定义函数、OpenAPI 规范或集成现有工具，为代理提供多样化能力，所有这些都紧密集成 Google 生态系统

- **代码优先开发**：直接在 Python 和 Java 中定义代理逻辑、工具和编排，实现终极的灵活性、可测试性和版本控制

- **模块化多代理系统**：通过将多个专业代理组合成灵活的层次结构来设计可扩展的应用程序

- **跟踪和监控**：内置代理可观察性，用于调试和优化工作流

- **随处部署**：轻松容器化并在 Cloud Run 或 GKE 上部署代理，或使用 Vertex AI Agent Engine 无缝扩展

## 支持的语言

ADK 支持多种编程语言：

- **Python** - 使用 pip 安装 `google-adk`
- **Java** - 使用 Maven Central 中的 `com.google.adk:google-adk`
- **Go** - 提供完整的 Go 语言支持

## 快速开始

### Python 安装

```bash
pip install google-adk
```

### Java 安装

```xml
<dependency>
    <groupId>com.google.adk</groupId>
    <artifactId>google-adk</artifactId>
    <version>最新版本</version>
</dependency>
```

## 核心功能

### 1. 代理开发

- 定义代理行为和逻辑
- 集成各种工具和 API
- 支持复杂的工作流编排

### 2. 工具集成

- 预构建的工具库
- 自定义函数支持
- OpenAPI 规范集成
- Google 生态系统深度集成

### 3. 多代理系统

- 代理层次结构
- 专业化代理组合
- 可扩展架构设计

### 4. 部署选项

- Cloud Run 部署
- Google Kubernetes Engine (GKE)
- Vertex AI Agent Engine
- 容器化部署

## 文档和资源

- **[官方文档](https://google.github.io/adk-docs)** - 完整的构建、评估和部署代理指南
- **[Python 入门](https://google.github.io/adk-docs/get-started/python/)** - Python 快速开始指南
- **[Java 入门](https://google.github.io/adk-docs/get-started/java/)** - Java 快速开始指南
- **[Go 入门](https://google.github.io/adk-docs/get-started/go/)** - Go 快速开始指南

## 许可证

本项目采用 Apache 2.0 许可证 - 详见 [LICENSE](https://github.com/google/adk-docs/blob/main/LICENSE) 文件。

## 贡献

我们欢迎社区贡献！无论是错误报告、功能请求、文档改进还是代码贡献，请查看我们的[贡献指南](https://github.com/google/adk-docs/blob/main/CONTRIBUTING.md)开始参与。

---

_祝您代理开发愉快！_
