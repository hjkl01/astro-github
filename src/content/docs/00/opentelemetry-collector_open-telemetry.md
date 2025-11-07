# OpenTelemetry Collector

## 项目简介

OpenTelemetry Collector 是 OpenTelemetry 项目的一部分，提供了一个 vendor-agnostic 的实现，用于接收、处理和导出遥测数据。它支持 traces、metrics 和 logs，并消除了运行多个 agents/collectors 的需要，以支持开源遥测数据格式（如 Jaeger、Prometheus 等）到多个开源或商业后端。

## 主要功能

- **统一处理**：单一代码库，可部署为 agent 或 collector，支持 traces、metrics 和 logs。
- **可扩展性**：通过 receivers、processors 和 exporters 组件实现定制化。
- **高性能**：在各种负载和配置下稳定且高性能。
- **可观测性**：作为可观测服务的典范。
- **易用性**：合理的默认配置，支持流行协议，开箱即用。

## 使用方法

### 安装

1. 从 [GitHub Releases](https://github.com/open-telemetry/opentelemetry-collector/releases) 下载最新版本的二进制文件。
2. 或者使用 Docker 镜像：
   ```bash
   docker pull otel/opentelemetry-collector
   ```

### 配置

使用 YAML 配置文件定义 pipelines。示例配置：

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  logging:
    loglevel: debug

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
```

### 运行

1. 保存配置为 `config.yaml`。
2. 运行 collector：
   ```bash
   ./otelcol --config-file=config.yaml
   ```
3. 或者使用 Docker：
   ```bash
   docker run -v $(pwd)/config.yaml:/etc/otelcol/config.yaml otel/opentelemetry-collector
   ```

### 监控

Collector 支持内部遥测，可用于监控其自身性能。更多详情请参考 [官方文档](https://opentelemetry.io/docs/collector/internal-telemetry/)。

## 社区与贡献

- **社区**：在 [CNCF Slack](https://cloud-native.slack.com/archives/C01N6P7KR6W) 的 #otel-collector 频道参与讨论。
- **贡献**：请参考 [Contributing Guide](https://github.com/open-telemetry/opentelemetry-collector/blob/main/CONTRIBUTING.md)。

## 许可证

Apache-2.0 License
