---
title: adk-web_google
---

# Google ADK Web - Agent 开发套件 Web 界面

## 项目简介

Google ADK Web（Agent Development Kit Web）是 Google Agent Development Kit 的内置开发者用户界面，旨在简化 AI 代理的开发和调试过程。该项目提供了一个直观的 Web UI，与 ADK 框架深度集成，让开发者能够更轻松地创建、部署和编排代理架构。

## 核心特性

- **内置开发者 UI**：与 Agent Development Kit 无缝集成的 Web 界面
- **简化开发流程**：让代理开发更像传统软件开发
- **模型无关**：虽然针对 Gemini 和 Google 生态系统进行了优化，但支持多种模型
- **部署无关**：灵活的部署选项
- **框架兼容**：与其他框架保持兼容性
- **可视化调试**：提供直观的调试和监控界面

## 技术栈

- **TypeScript** (76.4%) - 主要开发语言
- **SCSS** (12.1%) - 样式处理
- **HTML** (11.0%) - 页面结构
- **JavaScript** (0.5%) - 辅助脚本
- **Angular** - 前端框架

## 系统要求

在运行 ADK Web 之前，需要安装以下组件：

- **npm** - Node.js 包管理器
- **Node.js** - JavaScript 运行时环境
- **Angular CLI** - Angular 命令行工具
- **google-adk (Python)** - Python 版本的 ADK
- **google-adk (Java)** - Java 版本的 ADK

## 安装和运行

### 1. 克隆项目

```bash
git clone https://github.com/google/adk-web/
cd adk-web
```

### 2. 安装依赖

```bash
sudo npm install
```

### 3. 启动 Web 界面

```bash
npm run serve --backend=http://localhost:8000
```

### 4. 启动 API 服务器

在另一个终端中运行：

```bash
adk api_server --allow_origins=http://localhost:4200 --host=0.0.0.0
```

### 5. 访问界面

打开浏览器访问 `http://localhost:4200` 即可开始开发。

## 项目状态

- **GitHub Stars**: 535
- **Forks**: 146
- **Contributors**: 15
- **Issues**: 75 个开放问题
- **Pull Requests**: 43 个待合并请求
- **许可证**: Apache-2.0

## 重要链接

- **官方文档**: https://google.github.io/adk-docs/
- **示例代码**: https://github.com/google/adk-samples
- **Python 版本**: https://github.com/google/adk-python
- **Java 版本**: https://github.com/google/adk-java/
- **Reddit 社区**: r/agentdevelopmentkit

## 贡献指南

项目欢迎社区贡献，包括：

- 错误报告
- 功能请求
- 文档改进
- 代码贡献

### 测试要求

为了保持与上游代码的兼容性，测试代码需要遵循特定规则：

- 必须在 `TestBed.configureTestingModule()` 之前调用 `./src/app/testing/utils.ts` 中的 `initTestBed()`

## 许可证

本项目采用 Apache 2.0 许可证，详情请查看 [LICENSE](https://github.com/google/adk-web/blob/main/LICENSE) 文件。

## 预览状态

该功能目前处于预发布阶段，受 Google Cloud 服务条款中的"预发布产品条款"约束。预发布功能按"原样"提供，可能支持有限。

## 总结

Google ADK Web 是一个强大的开发者工具，为 AI 代理开发提供了直观的 Web 界面。通过简化开发流程和提供可视化调试工具，它让开发者能够更专注于代理逻辑的实现，而不是底层的技术细节。无论是简单的任务还是复杂的工作流，ADK Web 都能提供相应的支持，是 AI 代理开发者的理想选择。
