
---
title: opentelemetry-collector-contrib
---

# OpenTelemetry Collector Contrib

**项目地址**  
<https://github.com/open-telemetry/opentelemetry-collector-contrib>

## 简介  
OpenTelemetry Collector Contrib 是 OpenTelemetry 生态系统中提供的可扩展收集器插件库。它补充了核心 Collector，提供了大量预构建的 **receiver**、**processor**、**exporter** 等组件，支持多种数据源与后端系统。通过插件化设计，用户可灵活组合、扩展功能，快速构建符合业务需求的监控链路。

---

## 主要特性

| 类别 | 说明 |
|------|------|
| **Receiver** | 支持从 Kafka、Graphite、Prometheus、OTLP、JMX、OTel Collector、Sockets、Datadog、StatsD、AWS XRay 等多种协议与数据源采集数据。 |
| **Processor** | 提供日志/指标/追踪的过滤、处理、合并、转换、重命名、异常过滤、防作弊等功能；可与 OTEL SDK 两相结合处理。 |
| **Exporter** | 能将数据导出到 200+ 后端：Jaeger、Zipkin、OTLP、Prometheus Pushgateway、AWS CloudWatch、Datadog、Azure Monitor、Google Cloud Trace/Monitoring、Elastic APM、Honeycomb、NewRelic、OTel Collector、OTel Collector via gRPC/HTTP、Slack、Kafka、File、Cassandra、BigQuery、InfluxDB、Network Metrics 等。 |
| **Extensions** | 提供身份验证、健康检查、配置热更新、权限控制、TLS、Kafka 等扩展。 |
| **插件化** | 通过 `otelcol-contrib` CLI 可动态加载/卸载插件，支持插件格式化与版本控制。 |
| **可观测性** | 集成 OPK 监控与日志，支持内部状态和指标的导出。 |
| **社区活动** | 定期更新、RFC 评审、Bug 跟踪、Pull Request 协作，以保持与 OpenTelemetry 规范同步。 |

---

## 典型用法

### 1. 安装

> 用官方镜像：
```bash
docker pull otel/opentelemetry-collector-contrib:latest
```
> 或自行构建：
```bash
go install go.opentelemetry.io/collector/cmd/bundle@latest
bundle build
```

### 2. 配置文件示例

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

processors:
 batch:

exporters:
  jaeger:
    endpoint: jaeger:14250

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [jaeger]
```

> 只需按需修改 `receivers`/`processors`/`exporters`，即可构成任意数据流。

## 开发与自定义组件

1. **写自定义 Receiver/Processor/Exporter**  
   - 继承 `otelcol/receiver/receiver`, `processor/processor`, `exporter/exporter` 接口。  
   - 使用 `componentmain` 生成 main，可与 `otelcol-contrib` 一起构建。  
2. **上传插件**  
   - 编译为共享库，放置到 `plugins/`.  
   - 在配置文件中使用 `name: <plugin_name>` 引用即可。

---

## 资源

- 官方文档: <https://opentelemetry.io/docs/collector/contrib/>  
- 代码仓库: <https://github.com/open-telemetry/opentelemetry-collector-contrib>  
- 社区讨论: Slack #otel-collector, GitHub Issues  

---