---
title: metrics-server
---

# Kubernetes Metrics Server

## 功能

Metrics Server 是 Kubernetes 内置自动缩放管道的可扩展、高效的容器资源指标源。它从 Kubelets 收集资源指标，并通过 Metrics API 在 Kubernetes apiserver 中公开它们，用于 Horizontal Pod Autoscaler 和 Vertical Pod Autoscaler。也支持 `kubectl top`，便于调试自动缩放管道。

**注意**：Metrics Server 仅用于自动缩放目的。请勿用于转发指标到监控解决方案或作为监控指标源。在这种情况下，请直接从 Kubelet `/metrics/resource` 端点收集指标。

Metrics Server 提供：

- 单次部署，适用于大多数集群（见[要求](#要求)）
- 快速自动缩放，每 15 秒收集指标
- 资源效率，每个节点使用 1 毫核 CPU 和 2 MB 内存
- 可扩展支持高达 5,000 节点集群

### 用例

- CPU/内存基于的水平自动缩放（了解更多关于[水平自动缩放](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)）
- 自动调整/建议容器所需的资源（了解更多关于[垂直自动缩放](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler/)）

**不要使用** Metrics Server 当您需要：

- 非 Kubernetes 集群
- 准确的资源使用指标源
- 基于 CPU/内存以外的其他资源的水平自动缩放

对于不支持的用例，请查看完整的监控解决方案，如 [Prometheus](https://github.com/prometheus/prometheus)。

## 要求

Metrics Server 对集群和网络配置有特定要求。这些要求不是所有集群分发的默认设置。请在使用 Metrics Server 之前确保您的集群分发支持这些要求：

- kube-apiserver 必须[启用聚合层](https://kubernetes.io/docs/tasks/access-kubernetes-api/configure-aggregation-layer/)。
- 节点必须启用 Webhook [认证和授权](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-authn-authz/)。
- Kubelet 证书需要由集群证书颁发机构签名（或通过传递 `--kubelet-insecure-tls` 到 Metrics Server 来禁用证书验证）
- 容器运行时必须实现[容器指标 RPC](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/cri-container-stats.md)（或有 [cAdvisor](https://github.com/google/cadvisor) 支持）
- 网络应支持以下通信：
  - 控制平面到 Metrics Server。控制平面节点需要到达 Metrics Server 的 pod IP 和端口 10250（或节点 IP 和自定义端口如果启用了 `hostNetwork`）。阅读更多关于[控制平面到节点通信](https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/#control-plane-to-node)。
  - Metrics Server 到所有节点上的 Kubelet。Metrics Server 需要到达节点地址和 Kubelet 端口。地址和端口在 Kubelet 中配置，并作为 Node 对象的一部分发布。地址在 `.status.addresses` 中，端口在 `.status.daemonEndpoints.kubeletEndpoint.port` 字段（默认 10250）。Metrics Server 将基于 `kubelet-preferred-address-types` 命令行标志提供的列表选择第一个节点地址（清单中默认 `InternalIP,ExternalIP,Hostname`）。

## 安装

Metrics Server 可以直接从 YAML 清单或通过官方 [Helm 图表](https://artifacthub.io/packages/helm/metrics-server/metrics-server)安装。要从 _components.yaml_ 清单安装最新的 Metrics Server 版本，请运行以下命令。

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

以前版本的安装说明可以在 [Metrics Server 版本](https://github.com/kubernetes-sigs/metrics-server/releases)中找到。

### 兼容性矩阵

| Metrics Server | Metrics API group/version | Supported Kubernetes version |
| -------------- | ------------------------- | ---------------------------- |
| 0.8.x          | `metrics.k8s.io/v1beta1`  | 1.31+                        |
| 0.7.x          | `metrics.k8s.io/v1beta1`  | 1.27+                        |
| 0.6.x          | `metrics.k8s.io/v1beta1`  | 1.25+                        |
| 0.5.x          | `metrics.k8s.io/v1beta1`  | \*1.8+                       |
| 0.4.x          | `metrics.k8s.io/v1beta1`  | \*1.8+                       |
| 0.3.x          | `metrics.k8s.io/v1beta1`  | 1.8-1.21                     |

\*Kubernetes 版本低于 v1.16 需要传递 `--authorization-always-allow-paths=/livez,/readyz` 命令行标志

### 高可用性

Metrics Server 可以直接从 YAML 清单或通过官方 [Helm 图表](https://artifacthub.io/packages/helm/metrics-server/metrics-server)以高可用性模式安装，通过设置 `replicas` 值大于 `1`。要从 _high-availability.yaml_ 清单安装最新的 Metrics Server 版本以高可用性模式，请运行以下命令。

对于 Kubernetes v1.21+：

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability-1.21+.yaml
```

对于 Kubernetes v1.19-1.21：

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/high-availability.yaml
```

**注意**：此配置**需要**至少有 2 个节点的集群，Metrics Server 可以调度到这些节点上。

此外，为了最大化此高可用性配置的效率，**推荐**向 kube-apiserver 添加 `--enable-aggregator-routing=true` CLI 标志，以便发送到 Metrics Server 的请求在 2 个实例之间负载均衡。

### Helm 图表

[Helm 图表](https://artifacthub.io/packages/helm/metrics-server/metrics-server)作为此仓库中的附加组件维护，并发布到 `gh-pages` 分支支持的图表仓库。对于每个 Metrics Server 版本，都会发布新版本的图表，如果需要，也可以独立发布。`master` 分支上的图表不应直接引用，因为它可能包含自上次发布以来的修改；要查看图表代码，请使用图表发布标签。

## 安全上下文

Metrics Server 需要 `CAP_NET_BIND_SERVICE` 能力，以便作为非 root 用户绑定到特权端口。如果您在启用 [PSS](https://kubernetes.io/docs/concepts/security/pod-security-standards/) 或其他机制限制 pod 能力的环境中运行 Metrics Server，请确保允许 Metrics Server 使用此能力。即使您使用 `--secure-port` 标志将 Metrics Server 绑定到的端口更改为非特权端口，这也适用。

## 缩放

从 v0.5.0 开始，Metrics Server 带有默认资源请求，应保证大多数集群配置（高达 100 个节点）的良好性能：

- 100m 核 CPU
- 200MiB 内存

Metrics Server 资源使用取决于多个独立维度，创建一个[可扩展性信封](https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md)。默认 Metrics Server 配置应在不超过以下列出的任何阈值的集群中工作：

| Quantity               | Namespace threshold | Cluster threshold |
| ---------------------- | ------------------- | ----------------- |
| #Nodes                 | n/a                 | 100               |
| #Pods per node         | 70                  | 70                |
| #Deployments with HPAs | 100                 | 100               |

资源可以根据集群中的节点数量按比例调整。对于超过 100 个节点的集群，另外分配：

- 每个节点 1m 核
- 每个节点 2MiB 内存

您可以使用相同的方法降低资源请求，但有一个边界，这可能影响其他可扩展性维度，如每个节点的最大 pod 数量。

### 配置

根据您的集群设置，您可能还需要更改传递给 Metrics Server 容器的标志。最有用的标志：

- `--kubelet-preferred-address-types` - 确定连接到特定节点时使用的节点地址类型的优先级（默认 \[Hostname,InternalDNS,InternalIP,ExternalDNS,ExternalIP\]）
- `--kubelet-insecure-tls` - 不要验证 Kubelets 提供的服务证书的 CA。仅用于测试目的。
- `--requestheader-client-ca-file` - 指定用于验证传入请求上客户端证书的根证书包。
- `--node-selector` - 可以根据标签完成从指定节点抓取指标

您可以通过运行以下命令获取 Metrics Server 配置标志的完整列表：

```
docker run --rm registry.k8s.io/metrics-server/metrics-server:v0.8.0 --help
```

## 设计

Metrics Server 是 [Kubernetes 监控架构](https://github.com/kubernetes/design-proposals-archive/blob/main/instrumentation/monitoring_architecture.md)中描述的核心指标管道中的组件。

有关更多信息，请参见：

- [Metrics API 设计](https://github.com/kubernetes/design-proposals-archive/blob/main/instrumentation/resource-metrics-api.md)
- [Metrics Server 设计](https://github.com/kubernetes/design-proposals-archive/blob/main/instrumentation/metrics-server.md)

## 有问题？

在发布问题之前，首先查看[常见问题解答](/kubernetes-sigs/metrics-server/blob/master/FAQ.md)和[已知问题](/kubernetes-sigs/metrics-server/blob/master/KNOWN_ISSUES.md)。

## 社区、讨论、贡献和支持

了解如何参与 Kubernetes 社区在[社区页面](http://kubernetes.io/community/)。

您可以在以下位置联系此项目的维护者：

- [Slack 频道](https://kubernetes.slack.com/messages/sig-instrumentation)
- [邮件列表](https://groups.google.com/forum/#!forum/kubernetes-sig-instrumentation)

此项目由 [SIG Instrumentation](https://github.com/kubernetes/community/tree/master/sig-instrumentation)维护。

### 行为准则

参与 Kubernetes 社区受 [Kubernetes 行为准则](/kubernetes-sigs/metrics-server/blob/master/code-of-conduct.md)约束。
