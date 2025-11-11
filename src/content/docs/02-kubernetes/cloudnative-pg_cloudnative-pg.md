---
title: cloudnative-pg
---

# CloudNativePG

CloudNativePG (CNPG) 是一个开源平台，专为在 Kubernetes 环境中无缝管理 PostgreSQL 数据库而设计。它涵盖了整个操作生命周期，从初始部署到持续维护，通过其核心组件 CloudNativePG operator 实现。

## 功能

- **Kubernetes 原生管理**：直接与 Kubernetes API 集成，PostgreSQL 集群状态可在 `Cluster` 资源中查看。
- **自动化操作**：自动处理故障转移、扩展副本、滚动更新和服务更新，无需外部高可用工具。
- **高可用性**：支持主备集群管理，确保数据库的连续性和可靠性。
- **备份与恢复**：提供备份、计划备份和恢复功能，支持灾难恢复。
- **监控与扩展**：集成 Prometheus 导出器，支持扩展资源如 `Backup`、`Database`、`Pooler` 等。
- **不可变容器**：遵循不可变基础设施模型，确保更新安全可靠。

## 用法

1. **安装 Operator**：
   - 使用 Helm 或 kubectl 安装 CloudNativePG operator 到 Kubernetes 集群。
   - 示例命令：
     ```
     kubectl apply -f https://raw.githubusercontent.com/cloudnative-pg/cloudnative-pg/main/releases/cnpg-1.27.1.yaml
     ```

2. **部署 PostgreSQL 集群**：
   - 创建 `Cluster` 自定义资源 (CR) 来定义 PostgreSQL 集群。
   - 示例 YAML：
     ```yaml
     apiVersion: postgresql.cnpg.io/v1
     kind: Cluster
     metadata:
       name: my-postgres-cluster
     spec:
       instances: 3
       imageName: ghcr.io/cloudnative-pg/postgresql:16
       storage:
         size: 1Gi
     ```
   - 应用到集群：`kubectl apply -f cluster.yaml`

3. **管理集群**：
   - 使用 `kubectl` 查看状态：`kubectl get clusters`
   - 扩展副本：编辑 `spec.instances` 并重新应用。
   - 备份：创建 `Backup` 或 `ScheduledBackup` 资源。

4. **监控**：
   - 集成 Prometheus 和 Grafana 进行监控。
   - 查看日志：`kubectl logs -f deployment/cnpg-controller-manager`

更多详细信息，请参考 [官方文档](https://cloudnative-pg.io/documentation/current/)。
