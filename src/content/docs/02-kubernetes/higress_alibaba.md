---
title: higress
---


# Higress（阿里巴巴开源 API Gateway）

- **项目地址**  
  <https://github.com/alibaba/higress>

## 项目概述
Higress 是基于 Envoy、Open Policy Agent（OPA）和 Kubernetes 的高性能 API Gateway 与服务网格平台。它融合了 API 网关的功能与服务网格的可观测性、流量管理能力，支持多租户、插件化扩展，并兼容 Kubernetes 原生生态。

## 主要特性

| 特色 | 描述 |
|------|------|
| **API Gateway** | 提供速率限制、熔断、重试、流量镜像、负载均衡等常用网关功能。 |
| **服务网格** | 通过 Envoy Sidecar 实现细粒度流量控制、链路追踪（OpenTelemetry）、服务发现与健康检查。 |
| **动态配置** | 通过 Kubernetes CRD（`Gateway`, `Route`, `ServiceEntry` 等）实现零停机配置。 |
| **多租户 & 安全** | 支持命名空间隔离、基于 OPA 的自定义策略（RBAC、ACL、API Key、JWT 等）。 |
| **可观测性** | 集成 Prometheus、Grafana、Jaeger、Zipkin，自动生成监控与追踪数据。 |
| **插件化扩展** | 通过 `Extension` CRD 或自定义 Envoy 插件实现功能扩展（如自定义鉴权、日志、计费等）。 |
| **Kubernetes 原生** | 完全基于 CRD 与 Helm，支持 CRD 版本管理、滚动升级与回滚。 |
| **多协议支持** | HTTP/1.1, HTTP/2, gRPC, WebSocket，甚至 TCP/UDP 的访问控制与流量管理。 |
| **高可用与弹性** | 支持水平扩容、自动故障恢复、蓝绿/灰度发布。 |

## 核心组件

- **Higress Core**：负责配置解析、策略校验、动态 Envoy 配置生成。
- **Gateway CRD**：定义入口网关、监听器、TLS 证书等。
- **Route CRD**：路由规则、重写、镜像、限流等。
- **ServiceEntry CRD**：外部服务声明与流量出口。
- **Extension CRD**：自定义插件/鉴权逻辑。
- **Kubernetes Operator**：监听 CRD 变更并同步到 Envoy。

## 安装与使用

1. **安装 Helm 仓库**

   ```bash
   helm repo add higress https://alibaba.github.io/higress-helm
   helm repo update
   ```

2. **部署 Higress Operator**

   ```bash
   helm install higress higress/higress-operator \
     --namespace higress-system \
     --create-namespace
   ```

3. **创建 Gateway 与 Route**

   ```yaml
   apiVersion: networking.higress.io/v1alpha1
   kind: Gateway
   metadata:
     name: example-gateway
   spec:
     listeners:
     - protocol: HTTP
       port: 80
       routes:
       - name: example-route
         route:
           - destination:
               host: my-service
               port: 80
   ```

4. **开启插件（如 JWT 鉴权）**

   ```yaml
   apiVersion: networking.higress.io/v1alpha1
   kind: Extension
   metadata:
     name: jwt-auth
   spec:
     type: authentication
     config:
       jwt:
         issuer: "example.com"
         jwks_uri: "https://example.com/.well-known/jwks.json"
   ```

5. **监控与追踪**

   - Prometheus: `http://<higress-prometheus-service>/metrics`
   - Grafana: 默认 dashboard 可通过 `kubectl port-forward` 访问
   - Jaeger/Zipkin: 访问相应服务端口即可查看链路

## 常用命令

| 命令 | 用途 |
|------|------|
| `kubectl get gateways` | 查看已部署的网关 |
| `kubectl describe routes <name>` | 查看路由配置详情 |
| `kubectl logs -l app=higress-operator` | 查看 Operator 日志 |
| `helm upgrade higress higress/higress-operator` | 升级 Operator |

## 贡献与社区

- 项目主页: <https://github.com/alibaba/higress>
- 文档: <https://higress.io/docs>
- 讨论: 通过 Issues、Pull Requests 与社区交流

> 以上内容仅为快速入门概览，详细使用请参阅官方文档及示例配置。
