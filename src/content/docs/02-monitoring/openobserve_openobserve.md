
---
title: openobserve
---

# OpenObserve 项目

## 项目地址
[GitHub 项目地址](https://github.com/openobserve/openobserve)

## 主要特性
OpenObserve 是一个开源的分布式日志和指标监控系统，专为高性能、可扩展性和成本效益而设计。它采用 100% Rust 语言开发，提供云原生架构，支持快速查询和分析大规模数据。主要特性包括：
- **高性能查询**：支持 SQL-like 查询语言，查询速度可达数百万日志/秒。
- **低资源消耗**：存储成本低至 0.02 美元/GB/月，CPU 和内存使用率极低。
- **多数据源支持**：集成日志、指标、追踪和配置文件，支持 Kubernetes、Docker 等环境。
- **实时监控**：内置仪表盘、告警和通知功能，支持 Prometheus、Grafana 等工具集成。
- **分布式架构**：支持水平扩展，可部署在单节点或多节点集群中。
- **开源与社区驱动**：Apache 2.0 许可，易于自托管或云部署。

## 主要功能
- **数据摄取**：通过 HTTP API、Kafka、Fluentd 等方式实时摄取日志和指标，支持自动解析 JSON、文本等格式。
- **存储与索引**：使用 Parquet 格式存储数据，提供全文搜索和聚合功能，支持时间序列数据优化。
- **查询与分析**：内置查询引擎，支持过滤、聚合、时间范围查询，并生成可视化图表。
- **监控仪表盘**：自定义仪表盘，实时显示系统指标、日志流和警报。
- **告警系统**：基于规则的告警，支持 Slack、Email、Webhook 等通知渠道。
- **安全与访问控制**：角色-based 访问控制（RBAC），支持 TLS 加密和审计日志。
- **扩展性**：集成 OpenTelemetry，支持 AI/ML 增强的异常检测（实验性）。

## 用法
### 安装
1. **Docker 部署**（推荐快速启动）：
   ```
   docker run -d \
     -p 5080:5080 \
     -v /path/to/data:/data \
     --name openobserve \
     public.ecr.aws/openobserve/openobserve:latest
   ```
   访问 `http://localhost:5080` 以进入 Web UI。

2. **Kubernetes 部署**：
   使用 Helm Chart：
   ```
   helm repo add openobserve https://openobserve.github.io/helm-charts/
   helm install openobserve openobserve/openobserve
   ```

3. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/openobserve/openobserve`
   - 安装 Rust：`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
   - 构建：`cargo build --release`
   - 运行：`./target/release/openobserve`

### 基本用法
1. **数据摄取**：
   - 使用 API 发送日志：`curl -X POST http://localhost:5080/api/default/default/_json -H "Authorization: Basic <token>" -d '{"message": "Hello World"}'`
   - 配置 Fluent Bit 或 Logstash 将日志流向 OpenObserve。

2. **查询数据**：
   - 在 Web UI 中，使用 SQL 查询如：`SELECT * FROM default WHERE level = 'error' LIMIT 10`
   - 支持聚合：`SELECT COUNT(*) FROM default GROUP BY service`

3. **创建仪表盘和告警**：
   - 在 UI 中添加新仪表盘，拖拽图表组件。
   - 设置告警规则：选择指标、阈值和通知方式。

4. **扩展部署**：
   - 对于生产环境，配置多节点集群，使用 S3 或 MinIO 作为对象存储。
   - 参考官方文档：[docs.openobserve.ai](https://docs.openobserve.ai) 以获取详细配置。

更多细节请参考 GitHub 仓库的 README 和文档。