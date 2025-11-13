---
title: autoscaler
---

# Kubernetes Autoscaler

## 项目简介

Kubernetes Autoscaler 是 Kubernetes 社区维护的一个仓库，包含多个自动缩放相关的组件，用于优化 Kubernetes 集群的资源利用率和性能。

## 主要功能

### Cluster Autoscaler

- 自动调整 Kubernetes 集群的大小，确保所有 Pod 都有地方运行，同时避免不必要的节点。
- 支持多个公有云提供商。

### Vertical Pod Autoscaler (VPA)

- 一组组件，自动调整运行在 Kubernetes 集群中的 Pod 所请求的 CPU 和内存量。
- 当前状态：beta。

### Addon Resizer

- Vertical Pod Autoscaler 的简化版本，根据 Kubernetes 集群中的节点数量修改部署的资源请求。
- 当前状态：beta。

此外，还提供了 Cluster Autoscaler 和 Vertical Pod Autoscaler 的 Helm Chart，用于简化部署。

## 用法

### 获取代码

1. 在 GitHub 上 Fork 该仓库：https://github.com/kubernetes/autoscaler
2. 将代码检出到 `k8s.io` 的子目录中：

```shell
mkdir -p $GOPATH/src/k8s.io
cd $GOPATH/src/k8s.io
git clone https://github.com/$YOUR_GITHUB_USERNAME/autoscaler.git
cd autoscaler
```

### 部署

- 使用提供的 Helm Chart 部署 Cluster Autoscaler 或 Vertical Pod Autoscaler。
- 参考各组件的文档进行配置和部署。

### 联系和支持

- 加入 Kubernetes Slack 的 #sig-autoscaling 频道讨论。
- 参加每周会议，详情请见 [Kubernetes Community Repo](https://github.com/kubernetes/community/blob/master/sig-autoscaling/README.md)。

更多详细信息，请参考官方文档和 GitHub 仓库。
