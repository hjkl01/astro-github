---
title: ingress-nginx
---


# ingress-nginx（Kubernetes Ingress NGINX 控制器）

- **项目地址**: https://github.com/kubernetes/ingress-nginx  

## 项目简介
Ingress-NGINX 是为 Kubernetes 集群提供的开源 Ingress 控制器，基于 NGINX 容器实现 HTTP 与 HTTPS 流量路由、负载均衡、TLS 终止以及多种扩展功能。

## 主要特性
| 特性 | 说明 |
|------|------|
| **高性能 HTTP/HTTPS 负载均衡** | 利用 NGINX 高效的事件驱动模型，支持数千 TCP/UDP 连接。 |
| **多实例部署与弹性扩容** | 支持水平扩容，内部使用 ConfigMap 共享配置，实现无缝滚动更新。 |
| **TLS 终止与加密** | 支持 Kubernetes Secret 存储证书，自动生成 TLS 配置。 |
| **自定义 NGINX 配置** | 通过 ConfigMap 或 Annotation 可以插入自定义配置片段。 |
| **灵活路由** | 支持主机、路径、正则表达式、注解等多种路由规则。 |
| **动态修订** | 监听 Ingress、ConfigMap、Secret 资源变更，动态重载配置。 |
| **安全功能** | 支持 IP 白名单/黑名单、X-Forwarded-For 保护、HTTP Basic Auth 等。 |
| **监控与日志** | 集成 Prometheus 指标、可自定义日志格式，支持访问日志与错误日志。 |
| **CORS & 负载均衡策略** | 可配置权重、Least Connections、Session Affinity 等负载算法。 |

## 功能亮点
* **ConfigMap 配置**：全球统一的 `nginx-configuration`、`tcp-configuration`、`udp-configuration`。
* **命名空间隔离**：Ingress 控制器默认仅监控 `default` 之外可通过 `--default-namespace` 指定。
* **外部服务连接**：支持升多种外部通道（如 Cloud Load Balancer）与内部 Service 透明连接。
* **WebSocket 与 gRPC**：自动识别并保持长连接，支持 gRPC 协议升级。

## 用法示例

### 1. 安装

```bash
# Helm 安装（推荐）
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx --create-namespace \
  --set controller.publishService.enabled=true
```

### 2. 创建 Ingress 资源

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  tls:
  - hosts:
    - example.com
    secretName: tls-secret
  rules:
  - host: example.com
    http:
      paths:
      - path: /app
        pathType: Prefix
        backend:
          service:
            name: my-service
                         number: 80
```

### 3. 动态配置修改

```bash
# 修改 ConfigMap
kubectl edit configmap nginx-configuration -n ingress-nginx
# 例如: 启用 gzip
#   gzip on;
```

### 4. 监控

```bash
# 启用 Prometheus 指标
helm upgrade ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --set controller.metrics.enabled=true
```

---
以上即为 **Ingress‑NGINX** 项目的核心特性、功能与基本使用流程。