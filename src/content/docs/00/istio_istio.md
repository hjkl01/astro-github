
---
title: istio
---

# Istio

项目地址: <https://github.com/istio/istio>

## 主要特性
- **服务网格（Service Mesh）**：为微服务架构提供统一的网络层，支持可观测性、流量管理与安全策略。
- **流量管理**：细粒度路由、流量镜像、故障注入、重试、超时、熔断等。
- **安全**：基于 mTLS 的双向认证、细粒度访问控制、证书生命周期管理。
- **可观测性**：分布式追踪、指标收集、日志聚合、可视化仪表板。
- **策略与治理**：基于 RBAC、OPA、Istio Policy 的动态策略与限流。
- **多集群与多云**：支持跨集群服务发现与流量控制，兼容 Kubernetes、VM、裸机等。

## 核心功能
| 功能 | 说明 |
|------|------|
| **Ingress/Egress Gateway** | 统一入口/出口流量入口，支持 TLS 终止、虚拟服务、授权策略。 |
| **VirtualService / DestinationRule** | 定义路由规则、超时、重试、熔断，以及后端服务的策略。 |
| **ServiceEntry** | 允许将非集群外部服务纳入网格，支持自定义流量管理与安全。 |
| **AuthorizationPolicy** | 基于 JWT、OPA 或自定义规则实现细粒度访问控制。 |
| **Mixer（已废弃）** | 通过插件实现可插拔的计量、限流与策略，已在 V1.5+ 被注入替代。 |
| **Pilot** | 动态配置推送与服务发现，支持多种服务发现后端。 |
| **Citadel** | 证书签发与密钥管理，自动化 mTLS。 |
| **Mixer / Envoy** | Envoy 代理拦截流量，执行混合策略与可观测性收集。 |

## 快速开始
```bash
# 安装 Istioctl
curl -L https://istio.io/downloadIstio | sh -
cd istio-<version>
export PATH=$PWD/bin:$PATH

# 安装 Istio 基础组件
istioctl install --set profile=demo -y

# 测试环境
kubectl get svc -n istio-system

# 部署示例应用
kubectl label namespace default istio-injection=enabled
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
```

1. **启用 sidecar 自动注入**：在命名空间加标签 `istio-injection=enabled`，Pod 将自动注入 Envoy sidecar。
2. **配置流量路由**：通过 `VirtualService` 与 `DestinationRule` 定义请求路由与策略。
3. **开启安全**：默认使用 mTLS，可通过 `MeshPolicy` 或 `AuthorizationPolicy` 细化安全策略。
4. **监控与可观测**：Istio 默认集成 Prometheus、Grafana、Kiali；可自定义 Dashboards。

> 详细文档请参考官方文档: <https://istio.io/latest/docs/>