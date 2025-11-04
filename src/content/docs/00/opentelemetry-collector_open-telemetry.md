
---
title: opentelemetry-collector
---


# OpenTelemetry Collector

**项目地址**: https://github.com/open-telemetry/opentelemetry-collector

## 概述
OpenTelemetry Collector 是一个跨语言、可扩展的可观测性数据收集与处理组件，专为实现统一的指标、日志和追踪收集、转换、处理、导出而设计。它可以部署在边缘、服务网格或本地/云基础设施中，帮助团队高效采集、聚合并导出多种格式的数据。

## 主要特性
- **多协议支持**：同时支持 OTLP、Jaeger、Zipkin、Prometheus、OpenCensus、StatsD 等协议的接收（Receiver）和导出（Exporter）。
- **丰富的数据处理 Pipeline**：支持：
  - **Batch**：批量化处理、延迟规整。
  - **Resampling**：数据重采样、下采样。
  - **Reshaping**：数据扁平化/汇总。
  - **Sampler**：采样策略，例如概率采样、父子采样。
  - **Metrics Cadence**：指标周期控制。
  - **Logs Processor**：日志过滤、转换等。
- **插件化架构**：所有 Receiver、Processor、Exporter 及 Extension 都可作为插件独立构建或更新。可使用 Golang 模块直接下载或通过 Docker 镜像。
- **扩展与自定义**：支持：
  - **service.yaml**：通过配置文件声明 Pipeline 组成与参数。
  - **Telemetry**：Collector 本身的指标、日志、追踪导出。
  - **Extension**：如 health_check、zpages、prometheus、kubernetes∕OTLP等。
- **多环境兼容**：
  - **单二进制**：可在容器 (Docker)、Kubernetes、裸机或云环境中直接运行。
  - **Helm Chart**：即插即用的 Helm Chart。
  - **GitOps**：支持自定义 OCI 镜像、Containerd、Buildpacks 等。
- **安全与认证**：支持 TLS、JWT、OAuth  等认证/加密方式。
- **运行时 API 与 Debug**：提供zPages、Prometheus Exporter、Health Check 等交互式调试工具。

## 典型功能
1. **统一数据收集**  
   把来自多种语言 SDK 的 OTLP 收集并统一导出到 Prometheus、Jaeger、Grafana Cloud 等后端。
   
2. **边缘聚合**  
   在边缘节点部署 Collector，通过 batch、resampling、filter 预处理后再送往云端，减少网络与后端存储开销。

3. **管道细粒度控制**  
   在 Pipeline 中按数据类型（trace/metric/log）依次配置和执行 Processor，可实现精准的数据净化与路由。

4. **性能调优**  
   通过 `batch` 处理延迟控制、排队大小、IO 预分配等方式根据业务需求细调 Collector 性能。

5. **安全整体**  
   使用 `tls`、`http2`、`jwt` 等方式保证数据链路安全，减少对后端的暴露。

## 用法示例

### 1. 快速启动

```bash
docker run --name otel-collector \
  -p 4317:4317 -p 4318:4318 -p 55679:55679 \
  otel/opentelemetry-collector:latest
```

- `4317`：OTLP (gRPC) Receiver
- `4318`：OTLP (HTTP) Receiver
- `55679`：zPages 交互页面

### 2. 自定义配置

保存以下内容为 `collector_config.yaml`：

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

exporters:
  logging:
    loglevel: debug
  otlp:
    endpoint: "otel-collector:4317"

processors:
  batch:

service:
  pipelines:
    traces      receivers: [otlp]
      processors: [batch]
      exporters: [logging, otlp]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging, otlp]
```

然后启动：

```bash
docker run --name otel-collector \
  -v $(pwd)/collector_config.yaml:/etc/otel-collector-config.yaml \
  -p 4317:4317 -p 4318:4318 -p 55679:55679 \
  -e OTEL_COLLECTOR_CONFIG=/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector:latest
```

### 3. Helm 下载

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm repo update
helm install otel-collector open-telemetry/opentelemetry-collector --namespace otel
```

可根据 `values.yaml` 定制 channels、processors、exporters 等。

## 进一步学习

- 官方文档: https://opentelemetry.io/docs/collector/
- 组件参考: https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/
- Helm Chart: https://github.com/open-telemetry/opentelemetry-helm-charts

---
```

> 说明：将上述内容保存为 `src/content/docs/00/opentelemetry-collector_open-telemetry.md`。