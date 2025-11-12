---
title: repository
---

# KEDA (Kubernetes-based Event Driven Autoscaling)

KEDA 是一个基于 Kubernetes 的事件驱动自动扩缩容组件，为在 Kubernetes 中运行的任何容器提供事件驱动的扩缩容能力。

## 项目概述

KEDA 是一个云原生计算基金会（CNCF）的毕业项目，专注于为 Kubernetes 工作负载提供细粒度的自动扩缩容（包括从零扩容和缩容到零）。它作为 Kubernetes Metrics Server 运行，允许用户使用专门的 Kubernetes 自定义资源定义来定义自动扩缩容规则。

## 核心特性

- **事件驱动扩缩容**：基于各种事件源进行智能扩缩容
- **从零到零扩缩容**：支持将工作负载缩容到零，并在有事件时自动扩容
- **原生 Kubernetes 集成**：与 Horizontal Pod Autoscaler 等 Kubernetes 组件原生集成
- **多云和边缘支持**：可在云端和边缘环境中运行
- **无外部依赖**：独立运行，不需要额外的外部服务
- **丰富的扩展器支持**：支持 50+ 种内置扩展器

## 主要功能

### 扩展器（Scalers）

KEDA 支持多种事件源作为扩展器，包括但不限于：

- 消息队列：RabbitMQ、Kafka、Azure Service Bus、AWS SQS
- 数据库：PostgreSQL、MySQL、Redis
- 云服务：Azure Functions、AWS Lambda、Google Cloud Functions
- 监控和日志：Prometheus、Elasticsearch
- 自定义扩展器：支持构建自定义扩展器

### 部署方式

支持多种部署方式：

- Helm Chart
- Operator Hub
- YAML 清单文件
- Kustomize

## 使用场景

1. **事件驱动应用**：基于消息队列长度自动扩缩容
2. **批处理作业**：根据待处理任务数量动态调整
3. **API 服务**：基于请求量或队列深度自动扩缩容
4. **数据处理管道**：根据数据流入量调整处理能力
5. **无服务器架构**：实现真正的无服务器体验

## 快速开始

### 部署 KEDA

使用 Helm 部署：

```bash
helm repo add kedacore https://kedacore.github.io/charts
helm install keda kedacore/keda --namespace keda --create-namespace
```

### 基本配置示例

创建 ScaledObject：

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: my-scaled-object
spec:
  scaleTargetRef:
    name: my-deployment
  pollingInterval: 30
  cooldownPeriod: 300
  minReplicaCount: 0
  maxReplicaCount: 10
  triggers:
    - type: rabbitmq
      metadata:
        host: rabbitmq.default.svc.cluster.local
        queueName: myqueue
```

## 社区和支持

- **GitHub**: https://github.com/kedacore/keda
- **官方网站**: https://keda.sh
- **Slack**: #KEDA 频道在 Kubernetes Slack
- **文档**: 完整的官方文档和示例
- **贡献者**: 450+ 贡献者，9.6k+ GitHub stars

## 项目状态

- **CNCF 状态**: 毕业项目
- **许可证**: Apache-2.0
- **主要语言**: Go (99.2%)
- **活跃度**: 持续活跃开发，定期发布新版本

## 相关资源

- [KEDA 官方文档](https://keda.sh/docs/)
- [示例项目集合](https://github.com/kedacore/samples)
- [社区指南](https://keda.sh/community/)
- [支持政策](https://keda.sh/support/)

KEDA 为 Kubernetes 生态系统提供了强大而灵活的事件驱动自动扩缩容能力，是构建现代化云原生应用的重要工具。
