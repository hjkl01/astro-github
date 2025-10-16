
---
title: hypertrace
---

# Hypertrace 项目

**GitHub 项目地址:** [https://github.com/hypertrace/hypertrace](https://github.com/hypertrace/hypertrace)

## 主要特性
Hypertrace 是一个开源的分布式追踪和可观测性平台，专为现代微服务架构设计。它基于 OpenTelemetry 标准，提供高性能的追踪、指标和日志收集能力。主要特性包括：
- **端到端追踪**：支持分布式系统中的请求追踪，自动捕获服务间调用链路。
- **多协议支持**：兼容 Jaeger、Zipkin 和 OpenTelemetry 等标准协议，便于集成现有系统。
- **可扩展架构**：使用微服务设计，支持 Kubernetes 等容器化环境部署。
- **数据聚合与分析**：内置聚合引擎，能处理海量追踪数据，并提供可视化仪表板。
- **插件系统**：支持自定义插件扩展追踪范围，如数据库、HTTP 等。

## 主要功能
- **追踪收集**：通过代理或 SDK 自动注入追踪上下文，支持多种编程语言（如 Java、Go、Node.js）。
- **存储与查询**：集成 Elasticsearch 或其他后端存储，支持高效查询和搜索追踪数据。
- **警报与监控**：提供实时警报功能，监控系统性能瓶颈和错误率。
- **集成生态**：无缝集成 Prometheus、Grafana 等工具，实现全面可观测性。
- **安全与合规**：支持数据加密和访问控制，确保追踪数据的隐私保护。

## 用法
1. **安装与部署**：
   - 克隆仓库：`git clone https://github.com/hypertrace/hypertrace.git`。
   - 使用 Docker Compose 快速启动：运行 `docker-compose up` 以部署核心服务（包括代理、收集器和 UI）。
   - 对于生产环境，推荐在 Kubernetes 上部署，使用 Helm 图表：`helm install hypertrace ./charts/hypertrace`。

2. **配置追踪**：
   - 在应用中集成 SDK，例如在 Java 项目中添加依赖并初始化追踪器：
     ```java
     import io.opentelemetry.api.OpenTelemetry;
     // 配置并启动追踪
     OpenTelemetry openTelemetry = ...; // 通过 Hypertrace 配置
     ```
   - 配置代理：编辑 `hypertrace-agent.yaml` 文件，指定服务名称和采样率。

3. **使用 UI**：
   - 访问本地 UI（默认端口 8080）：查看追踪列表、时间线图和依赖图。
   - 查询追踪：使用搜索功能过滤服务、操作或标签。

4. **高级用法**：
   - 自定义插件：实现接口添加新追踪类型，并构建部署。
   - 扩展存储：修改配置连接外部数据库，如 `elasticsearch.hosts: ["localhost:9200"]`。
   - 测试：运行单元测试 `mvn test` 或集成测试以验证部署。

更多详情请参考仓库的 README 和文档。