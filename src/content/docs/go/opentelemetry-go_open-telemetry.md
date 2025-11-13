---
title: Opentelemetry Go
---

# OpenTelemetry-Go

## 功能

OpenTelemetry-Go 是 OpenTelemetry 的 Go 语言实现。它提供了一套 API 来直接测量软件的性能和行为，并将这些数据发送到可观测性平台。

- **分布式跟踪 (Traces)**: 稳定，支持捕获和传播分布式跟踪信息。
- **指标 (Metrics)**: 稳定，支持收集和导出指标数据。
- **日志 (Logs)**: Beta 阶段，支持日志收集。

## 用法

### 入门

访问 [opentelemetry.io](https://opentelemetry.io/docs/languages/go/getting-started/) 获取入门指南。

### 仪器化 (Instrumentation)

要开始从应用捕获分布式跟踪和指标事件，需要仪器化应用。最简单的方式是使用仪器化库。查看 [官方支持的仪器化库](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/instrumentation)。

如果需要扩展或直接构建仪器化，使用 [Go otel](https://pkg.go.dev/go.opentelemetry.io/otel) 包。查看 [示例](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/main/examples)。

### 导出 (Export)

配置导出管道将遥测数据发送到可观测性平台。

支持的导出器：

- **OTLP**: 支持日志、指标、跟踪。
- **Prometheus**: 支持指标。
- **stdout**: 支持日志、指标、跟踪。
- **Zipkin**: 支持跟踪。

### 兼容性

支持 Go 1.24 和 1.25 等版本。支持多种操作系统和架构。

### 贡献

查看 [贡献文档](https://github.com/open-telemetry/opentelemetry-go/blob/main/CONTRIBUTING.md)。
