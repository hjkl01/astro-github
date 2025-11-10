---
title: tempo
---

# Grafana Tempo

**GitHub 项目地址**：<https://github.com/grafana/tempo>

## 主要特性

- **分布式追踪**：支持 Jaeger、OpenTelemetry 等协议，聚合、存储和可视化分布式系统的请求链路。  
- **可水平扩展的存储**：兼容多种后端（CDynamoDB、S3、GCS 等），可横向扩展至数百 TB。  
- **低成本压缩**：采用高效压缩与分区存储，避免冗余索引，降低磁盘与网络成本。  
- **无缝集成**：与 Grafana、Prometheus、Kubernetes、Kong 等监控栈原生集成。  
- **多租户 & 安全**：支持 IAM、RBAC、VPC、TLS/MTLS，保障数据隔离与访问控制。

## 核心功能

1. **采集与采样**  
   - 通过 OpenTelemetry Collector、Prometheus、Jaeger Collector/Agent 等采集器接入。  
   - 支持无代理采样与侧信道采样。

2. **存储层**  
   - 支持多种后端：Cassandra、DynamoDB、S3、GCS、Local FS。  
   - 自动分段、压缩与分区，支持运行时切换后端。

3. **查询与分析**  
   - HTTP API 兼容 OpenTelemetry Trace API。  
   - 与 Grafana Trace Explorer 集成，实现链路、服务依赖、错误率等可视化。

4. **数据迁移 & 兼容**  
   - 支持从 Zipkin、OpenTelemetry、Jaeger 等多种格式导入。  
   - 与 Tempo‑s3、Tempo‑aggregation 等工具兼容。

5. **运维与监控**  
   - 提供健康检查、Prometheus 原生指标。  
   - Grafana Dashboards 可查看节点状态、查询延迟、存储使用等。

## 快速使用

```bash
# Docker Compose 快速启动
docker compose -f docker-compose.yaml up -d
```

> 详细说明可参考官方文档: <https://github.com/grafana/tempo#documentations>