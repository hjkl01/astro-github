
---
title: gateway-api
---


# Kubernetes Gateway API

**GitHub 地址**: [https://github.com/kubernetes-sigs/gateway-api](https://github.com/kubernetes-sigs/gateway-api)

---

## 项目简介
Gateway API 是一种开源规范，提供了一套以资源为中心的、可扩展的网络代理控制模型，用于在 Kubernetes 上实现高级路由、负载均衡、TLS、授权等功能。其目标是取代传统的 Ingress 资源，让流量管理更具可组合性、可扩展性和可观察性。

---

## 主要特性

| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | `Gateway` 资源 | 统一定义负载均衡器、入口点与 TLS 终止点，支持实例化 NetBI 等多种代理实现。 |
| 2 | `HTTPRoute` / `GRPCRoute` | 抽象化 HTTP/1.x、HTTPS、gRPC 路由逻辑，支持基于请求路径、主机、方法等多维度匹配。 |
| 3 | 细粒度访问控制 | `GatewayClass`、`HTTPRouteGroup`、`Permission` 等资源，提供对路由创建与访问的细粒度授权。 |
| 4 | 可观测性融合 | 与 Prometheus、OpenTelemetry 兼容，支持流量数据导出、日志与 tracing。 |
| 5 | 可扩展性 | 通过 CRD 模式，允许插件化 Gateway 实现，支持多种后端代理（Envoy、NGINX、Traefik 等）。 |
| 6 | 版本管理 | 支持多版本（β1、α2 等）共存，逐步平滑迁移。 |
| 7 | 高可用 & 软硬件隔离 | 通过 `GatewayClass` 指定后端实现、节点选择器、优先级等，提升 HA 与资源隔离。 |

---

## 核心资源

- **GatewayClass**  
  - 定义可用的负载均衡器类型与配置范围。
- **Gateway**  
  - 实例化一个 Gateway 对象，绑定到某个 `GatewayClass`，配置监听器（如 HTTP/HTTPS）、TLS 与负载均衡器信息。
- **HTTPRoute / GRPCRoute**  
  - 定义跨 Gateway 的路由规则，支持 `Match HTTP`、`Header`、`Query`、`BackendRef` 等。
- **ReferenceGrant**  
  - 允许跨命名空间的对 `Gateway`、`Route` 的引用权限控制。
  
---

## 使用方法

1. **安装规范**
   ```bash
   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/latest/download/gateway-api.yaml
   ```
   或使用 Custom Resource Definition (CRD) 版本。

2. **创建 GatewayClass**
   ```yaml
   apiVersion: gateway.networking.k8s.io/v1beta1
   kind: GatewayClass
   metadata:
     name: example-gateway
   spec:
     controllerName: gateway-controller.kubernetes.io/istio
   ```

3. **创建 Gateway**
   ```yaml
   apiVersion: gateway.networking.k8s.io/v1beta1
   kind: Gateway
   metadata:
     name: example-gateway
   spec:
     gatewayClassName: example-gateway
     listeners:
     - protocol: HTTP
       port: 80
       hostname: "*"
   ```

4. **创建 HTTPRoute**
   ```yaml
   apiVersion: gateway.networking.k8s.io/v1beta1
   kind: HTTPRoute
   metadata:
     name: example-route
   spec:
     parentRefs:
     - name: example-gateway
     hostnames:
     - "example.com"
     rules:
     - matches:
       - path:
           type: PathPrefix
           value: /app
       backendRefs:
       - name: my-application
         port: 8080
   ```

5. **验证**
   ```bash
   kubectl get gateways,httproutes
   ```

---

## 典型场景

| 场景 | 说明 |
|------|------|
| 多个 Ingress 合并 | 用 Gateway 统一管理多租户、不同协议的流量。 |
| gRPC 与 HTTP 混合 | `GRPCRoute` 与 `HTTPRoute` 并存，细粒度路由。 |
| 本地服务导出 | 通过 `BackendRef` 将 ClusterIP/Service 暴露给 Gateway。 |
| 动态 TLS 终止 | `TLS` 监听器与 `Certificate` 资源结合，实现 HTTPS。 |

---

## 贡献与支持

- 订阅官方 Issue Tracker 与 Discussions。
- 参与 CRD 规范社区讨论，提交 PR。
- 官方文档与示例在 repo 的 `docs/` 与 `examples/` 目录。

---

**关键词**: Kubernetes, Gateway API, Ingress, CRD, IngressClass, HTTPRoute, GRPCRoute, GatewayClass, ReferenceGrant, 负载均衡, TLS, 观察性, 高可用
