---
title: Temporal
---

# Temporal

## 项目简介

Temporal 是一个持久执行平台，使开发者能够构建可扩展的应用，而不牺牲生产力或可靠性。Temporal 服务器以弹性方式执行称为 Workflows 的应用逻辑单元，自动处理间歇性故障，并重试失败的操作。

Temporal 起源于 Uber 的 Cadence 项目，是一个成熟的技术，由 Temporal Technologies 开发。

## 主要功能

- **Workflow 执行**：以持久和可靠的方式执行工作流，支持长时间运行的任务。
- **故障处理**：自动处理间歇性故障，重试失败的操作，确保应用可靠性。
- **可扩展性**：支持构建大规模分布式应用。
- **多语言支持**：提供 SDK 支持多种编程语言，如 Go、Java 等。
- **时间旅行调试**：允许回放和调试工作流执行历史。
- **Web UI**：提供可视化界面查看和管理工作流。

## 用法

### 安装和启动服务器

1. 使用 Homebrew 安装 Temporal CLI：

   ```
   brew install temporal
   ```

2. 启动开发服务器：
   ```
   temporal server start-dev
   ```

### 运行示例

1. 克隆示例仓库（以 Go 为例）：

   ```
   git clone https://github.com/temporalio/samples-go.git
   cd samples-go
   ```

2. 运行示例工作流。

### 使用 CLI

使用 Temporal CLI 与服务器交互：

- 列出命名空间：

  ```
  temporal operator namespace list
  ```

- 列出工作流：
  ```
  temporal workflow list
  ```

### 使用 Web UI

打开浏览器访问 [http://localhost:8233](http://localhost:8233) 查看和管理工作流。

### 开发工作流

要实现 Workflows、Activities 和 Workers，请参考 [Temporal 文档](https://docs.temporal.io/dev-guide/) 并使用相应的 SDK。

## 贡献

欢迎贡献！请查看 [贡献指南](https://github.com/temporalio/temporal/blob/main/CONTRIBUTING.md)。

## 许可证

MIT License
