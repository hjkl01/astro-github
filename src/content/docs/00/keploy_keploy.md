---
title: Keploy
---

# Keploy

## 项目简介

Keploy 是一个开发者友好的 API、集成和端到端 (E2E) 测试代理工具。它能够从用户流量中自动生成测试和数据模拟 (mocks/stubs)，比传统的单元测试更快。

## 主要功能

- **无代码更改**：只需运行应用即可自动捕获真实的 API 调用并转换为测试和模拟。
- **记录和重放复杂流程**：捕获分布式 API 流程作为测试和模拟，支持重放以节省时间。
- **完整基础设施虚拟化**：不仅模拟 HTTP 端点，还支持数据库 (Postgres, MySQL, MongoDB)、流/队列 (Kafka, RabbitMQ) 等。
- **组合测试覆盖率**：计算语句、分支和业务用例覆盖率，提供统一的覆盖率报告。
- **AI 扩展 API 覆盖率**：使用 AI 基于现有记录和 Swagger/OpenAPI Schema 生成边界值、缺失字段等测试用例。
- **CI/CD 集成**：支持在本地 CLI、CI 管道 (Jenkins, Github Actions) 或 Kubernetes 集群中运行测试。
- **多用途模拟**：生成的模拟可作为服务器测试使用。
- **报告**：统一的 API、集成、单元和 E2E 覆盖率报告，直接在 CI 或 PR 中查看。
- **开发者控制台**：友好的控制台用于查看、管理和调试记录的测试和模拟。
- **时间冻结**：确定性地重放测试，通过冻结系统时间。
- **模拟注册表**：集中式注册表用于管理、复用和版本化模拟。

## 用法

### 1. 安装 Keploy Agent

```bash
curl --silent -O -L https://keploy.io/install.sh && source install.sh
```

### 2. 记录测试用例

启动应用以将真实的 API 调用转换为测试和模拟。

```bash
keploy record -c "CMD_TO_RUN_APP"
```

例如，对于 Python 应用：

```bash
keploy record -c "python main.py"
```

### 3. 运行测试

在没有外部依赖的情况下离线运行测试。

```bash
keploy test -c "CMD_TO_RUN_APP" --delay 10
```

## 支持的语言和框架

Keploy 使用 eBPF 在网络层捕获流量，因此适用于任何语言、框架或运行时，无需 SDK。

支持的语言包括：Go, Java, Node.js, Python, Rust, C#, C/C++, TypeScript, Scala, Kotlin, Swift, Dart, PHP, Ruby, Elixir, .NET, gRPC, GraphQL, HTTP/REST, Kafka, RabbitMQ, PostgreSQL, MySQL, MongoDB, Redis 等。

## 资源

- [官方网站](https://keploy.io)
- [文档](https://keploy.io/docs/)
- [Slack 社区](https://join.slack.com/t/keploy/shared_invite/zt-357qqm9b5-PbZRVu3Yt2rJIa6ofrwWNg)
- [贡献指南](https://keploy.io/docs/keploy-explained/contribution-guide/)
- [博客](https://keploy.io/blog/)
