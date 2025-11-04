
---
title: opentelemetry-go
---


# OpenTelemetry Go

**GitHub 项目地址**: https://github.com/open-telemetry/opentelemetry-go

## 项目简介
OpenTelemetry Go 是一个基于 OpenTelemetry 规范的 Go 语言实现，提供了统一的追踪、指标和日志收集、处理和导出功能。它集成了 SDK、API、自动化采样、导出器以及多种语言间的互操作性。

## 主要特性
- **统一 API**：`go.opentelemetry.io/otel` 包提供标准化的 `Tracer`, `Meter`, `Logger` 等接口。
- **SDK**：实现了 `otel/sdk` 子包，支持自定义配置、采样、批处理、导出等。
- **自动化采样**：支持 `TraceIDRatioBased`, `ParentBased`, `AlwaysOn`, `AlwaysOff` 等采样策略。
- **导出器**：
  - OTLP (gRPC/HTTP)
  - Jaeger
  - Zipkin
  - Prometheus
  - Console
  - File
  - 自定义导出。
- **自动化仪表**：自动化采集 HTTP, gRPC, MySQL, PostgreSQL, Redis 等常用组件的指标和追踪。
- **跨语言互操作**：通过共享的 `OTLP` 协议，支持多语言协作。
- **扩展性**：支持自定义 `SpanProcessor`, `BatchSpanProcessor`, `MetricExporter` 等。
- **资源检测**：自动检测主机、容器、Kubernetes 等环境信息。

## 核心模块
| 模块 | 说明 |
|------|------|
| `api` | 追踪、指标、日志的公共接口。 |
| `sdk` | 具体实现，包括 `trace`, `metric`, `log`。 |
| `exporters` | 各类导出器实现。 |
| `instrumentation` | 自动化采集库。 |
| `propagation` | 传输上下文的实现。 |
| `trace` | Span, Tracer 相关实现。 |
| `metric` | Metric, Meter 等实现。 |
| `log` | 日志相关实现。 |

## 快速上手

```go
package main

import (
    "context"
    "log"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/resource"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
    "go.opentelemetry.io/otel/attribute"
    "go.opentelemetry.io/otel/trace"
)

func main() {
    // 创建 OTLP 导出器
    exporter, err := otlptracegrpc.New(context.Background())
    if err != nil {
        log.Fatalf("failed to create exporter: %v", err)
    }

    // 创建 TraceProvider
    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(exporter),
        sdktrace.WithResource(resource.NewSchemaless(
            attribute.String("service.name", "my-service"),
        )),
    )
    otel.SetTracerProvider(tp)

    // 创建 Tracer
    tracer := otel.Tracer("example.com/trace")
    ctx, span := tracer.Start(context.Background(), "main")
    defer span.End()

    // 业务逻辑
    doWork(ctx)

    // 关闭资源
    if err := tp.Shutdown(context.Background()); err != nil {
        log.Fatalf("Error shutting down tracer provider: %v", err)
    }
}

func doWork(ctx context.Context) {
    // 业务代码
}
```

## 文档与社区
- 官方文档: https://opentelemetry.io/docs/instrumentation/go/
- 贡献指南: https://github.com/open-telemetry/opentelemetry-go/blob/main/CONTRIBUTING.md
- GitHub Issues: https://github.com/open-telemetry/opentelemetry-go/issues

---

> 以上内容已保存至 `src/content/docs/00/opentelemetry-go_open-telemetry.md`。