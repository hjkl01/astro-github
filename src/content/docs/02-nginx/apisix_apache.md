---
title: apisix
---

# APISIX

> **GitHub 项目地址**  
> https://github.com/apache/apisix

## 简介
Apache APISIX 是一款轻量、高性能、可插拔的云原生 API 网关。它基于 Nginx/Stream Server 与 Lua 开发，支持动态配置、流量控制、边缘缓存、服务治理等功能，面向微服务架构、服务网格与边缘计算场景。

## 主要特性

| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | **动态配置** | 通过 etcd、nacos、Redis 等分布式键值存储实时更新路由、插件配置，无需重启。 |
| 2 | **插件体系** | 内置 60+ 插件（如限流、鉴权、负载均衡、监控），支持自定义 Lua 插件。 |
| 3 | **高性能** | 采用 **Stream 级别** Nginx + LuaJIT，wrk 测试可达数十万 QPS。 |
| 4 | **多协议支持** | HTTP、HTTPS、TCP、UDP、TLS、SNI 等；支持 mTLS、HTTPS+重写等。 |
| 5 | **边缘缓存** | 支持基于 response code, TTL, 缓存 key 的边缘缓存。 |
| 6 | **请求流量控制** | 弹性限速、漏桶、令牌桶、漏桶、漏帧；支持熔断、降级。 |
| 7 | **服务治理** | 自动健康检查、权重调度、会话保持、负载均衡（round robin, random, weighted, IP hash）。 |
| 8 | **双向 TLS (mTLS)** | 支持双向 TLS 认证与身份授权。 |
| 9 | **多租户/无状态** | 通过 namespace 隔离多租户，无状态部署，易于水平扩容。 |
| 10 | **监控与日志** | 集成 OpenTelemetry、Prometheus、Grafana；支持访问日志、错误日志。 |
| 11 | **CLI & UI** | `apisix-admin` 提供 CLI，`apisix-dashboard` 提供 Web 控制台，实现一键管理。 |
| 12 | **服务网格集成** | 支持与 Istio, Linkerd 等服务网格互操作；可作为网关插件。 |
| 13 | **无缝容灾** | 对 etcd/PostgreSQL 进行多副本，高可用。在集群中可实现主/备切换。 |
| 14 | **云原生特性** | 支持 DaemonSet、Deployment、StatefulSet，配合 Helm 打包与 Helm Chart。 |
| 15 | **安全与身份** | JWT、Basic Auth、WAF、IPS、Proxy、IP 黑白名单等安全插件。 |

## 核心功能

| 功能 | 细节 |
|------|------|
| API 路由 | RESTful 或 prefix 路由；可配置多级路由，支持 URI 和 Host 组合匹配。 |
| 插件链 | 预定义插件链顺序；支持自定义插件加入链。 |
| 负载均衡 | Round Robin, Random, Weighted Round Robin, Topology, Weighted IP Hash 等。 |
| 控制台 | `grafana`、`kibana` 集成。 |
| 日志 | 对 Kubernetes Audit, EnvoyLog 等日志归档。 |
| 重试 | 通过插件支持重试、错误处理策略。 |
| 监控 | 指标导出接口，支持用户自定义指标。 |

## 快速上手

> 下面示例基于 Docker + etcd，演示安装、配置路由、启用限流插件。

### 1. 启动等组件

```bash
# 当前工作目录下执行
docker-compose -f docker-compose.yml up -d

# 等待 etcd/redis/nacos 启动完成
```

### 2. 安装 APISIX

```bash
# 拉取镜像或编译
docker pull apache/apisix:latest
```

### 3. 配置 API 路由

```bash
curl -X POST http://127.0.0.1:9080/apisix/admin/routes/1 \
  -d '{
        "uri": "/hello",
        "host": "example.com",
        "upstream": {
          "type": "roundrobin",
          "nodes": {"127.0.0.1:8001": 1}
        }
      }'
```

### 4. 添加限流插件

```bash
curl -X PATCH http://127.0.0.1:9080/apisix/admin/routes/1 \
  -H "Content-Type: application/json" \
  -d '{
        "plugins": {
          "limit-conn": {"conn": 50},
          "limit-count": {"count": 100, "time_window": 60}
        }
      }'
```

### 5. 验证

```bash
curl -H "Host: example.com" http://127.0.0.1/hello
```

### 6. 查看监控

```bash
# Prometheus 监控端点
http://127.0.0.1:9091/metrics
```

## 代码目录结构概览

```
apisix/
├─ api/        # 管理 API
├─ conf/       # 默认配置文件
├─ core/       # 核心功能实现
├─ plugins/    # 插件 ui/         # Web 控制台
├─ docs/       # 文档
└─ etcd/       # etcd 配置与资源
```

## 社区与支持

- **邮件列表**：apisix-dev@apache.org
- **钉钉/Slack**：Apache APISIX 官方讨论组
- **官网**：https://apisix.apache.org
- **技术博客**：httpsapisix.apache.org/blog

以上即为 Apache APISIX 的核心特性、功能与基本使用方法。祝你使用愉快！