
---
title: signoz
---

# SigNoz 项目

**GitHub 项目地址:** [https://github.com/SigNoz/signoz](https://github.com/SigNoz/signoz)

## 主要特性

SigNoz 是一个开源的可观测性平台，专为监控和调试分布式系统而设计。它集成了指标（Metrics）、追踪（Traces）和日志（Logs）的收集与分析功能，支持 OpenTelemetry 标准，提供高效的 APM（Application Performance Monitoring）体验。主要特性包括：

- **全栈可观测性**：支持指标、追踪和日志的统一视图，帮助开发者快速识别性能瓶颈和错误根因。
- **OpenTelemetry 原生支持**：无缝集成 OpenTelemetry SDK 和 Collector，无需额外代理或修改代码。
- **高效存储与查询**：使用 ClickHouse 作为后端数据库，提供高性能的时序数据存储和查询，支持 PB-level 数据规模。
- **实时警报与仪表盘**：内置警报系统和自定义仪表盘，支持 Slack、PagerDuty 等通知渠道。
- **异常检测**：自动检测异常事件和根因分析，减少手动排查时间。
- **云原生部署**：支持 Kubernetes、Docker 等部署方式，适用于云环境和本地开发。
- **开源与社区驱动**：完全开源（Apache 2.0 许可），活跃社区贡献，提供企业级功能如 SSO 和 RBAC。

## 功能

SigNoz 的核心功能聚焦于现代应用的监控和调试：

- **指标监控**：收集 CPU、内存、网络等系统指标，以及自定义业务指标，支持 Prometheus 兼容的查询语言。
- **分布式追踪**：可视化服务间调用链路，分析延迟和错误，支持服务地图（Service Map）和火焰图（Flame Graphs）。
- **日志管理**：集中式日志聚合、搜索和过滤，支持结构化日志和全文搜索。
- **APM 功能**：应用性能监控，包括响应时间、吞吐量、错误率等指标，提供端到端追踪。
- **基础设施监控**：监控主机、容器和 Kubernetes 集群的健康状态。
- **安全与合规**：数据加密、访问控制，支持自托管以确保数据隐私。

## 用法

### 安装与部署

1. **前提条件**：确保系统安装 Docker 和 Docker Compose（推荐版本 1.29+）。对于 Kubernetes 部署，需要 kubectl 和 Helm。

2. **快速启动（使用 Docker）**：
   - 克隆仓库：`git clone https://github.com/SigNoz/signoz.git && cd signoz`
   - 启动服务：`docker-compose up -d`
   - 服务将运行在 `http://localhost:3301`（UI 界面）。

3. **Kubernetes 部署**：
   - 添加 Helm 仓库：`helm repo add signoz https://charts.signoz.io`
   - 安装：`helm install my-signoz signoz/signoz -n platform --create-namespace`
   - 通过 LoadBalancer 或 Ingress 访问 UI。

4. **自定义配置**：
   - 编辑 `docker-compose.yaml` 或 Helm values.yaml 来配置持久化存储、端口等。
   - 对于生产环境，推荐使用外部 ClickHouse 集群和对象存储（如 S3）。

### 使用步骤

1. **访问 UI**：打开浏览器访问 SigNoz 仪表盘，默认无密码（生产环境需配置认证）。

2. **集成应用**：
   - **使用 OpenTelemetry**：在你的应用中集成 OpenTelemetry SDK（支持 Java、Python、Node.js 等语言）。
     - 示例（Python）：安装 `opentelemetry-sdk`，配置 exporter 指向 SigNoz Collector（默认端口 4317/4318）。
   - **手动仪器化**：为关键代码添加追踪 span 和指标。

3. **监控与分析**：
   - **仪表盘**：创建自定义面板，查询指标如 `http_server_duration`。
   - **追踪**：在 Traces 页面搜索特定请求，查看调用链。
   - **日志**：使用 Logs 页面过滤和聚合日志条目。
   - **警报**：在 Alerts 部分设置阈值规则，例如 CPU 使用率 > 80% 时通知。

4. **扩展与维护**：
   - 更新：拉取最新代码并重启 Docker Compose。
   - 故障排除：检查日志 `docker-compose logs` 或 Kubernetes pod 日志。
   - 文档：参考官方文档 [https://signoz.io/docs](https://signoz.io/docs) 获取高级用法，如自定义 Collector 配置。

SigNoz 适用于 DevOps、SRE 和开发者团队，帮助提升系统可靠性和调试效率。