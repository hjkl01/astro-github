---
title: kong
---


# Kong

**GitHub 地址**：<https://github.com/Kong/kong>

## 主要特性

- **API Gateway**：统一入口，支持 HTTP/HTTPS、gRPC、WebSocket 等协议。
- **插件化架构**：可插拔插件实现认证、限流、日志、监控等功能。
- **高可用与弹性**：支持多实例部署、服务发现、负载均衡、故障转移。
- **声明式配置**：使用 YAML/JSON 文件一次性配置路由、插件、服务等，适合 GitOps。
- **多环境支持**：内置数据库（PostgreSQL/MySQL）或无数据库模式，支持 Docker、Kubernetes、VM 等多种部署方式。

## 关键功能

| 功能 | 说明 |
|------|------|
| **路由与转发** | 根据请求路径、方法、Header 等规则将流量路由到后端服务。 |
| **身份认证** | 支持 JWT、OAuth 2.0、Basic Auth、Key Auth 等多种认证方式。 |
| **限流与配额** | 按 IP、API Key、用户等粒度进行请求限流、配额控制。 |
| **插件管理** | 通过 Lua 编写自定义插件或使用官方插件集合。 |
| **监控与日志** | 集成 Prometheus、Datadog、OpenTelemetry 等监控系统；支持日志采集、请求追踪。 |
| **安全加固** | TLS/TLS 终止、HSTS、CORS、请求体大小限制等安全功能。 |
| **服务发现** | 支持 Consul、ETCD、Kubernetes Service 等后端服务发现机制。 |
| **多租户** | 通过命名空间或 Consumer 进行多租户隔离。 |

## 快速使用

### 1. Docker 方式

```bash
docker run -d --name kong \
  -e "KONG_DATABASE=off" \
  -e "KONG_DECLARATIVE_CONFIG=/kong.yml" \
  -v $(pwd)/kong.yml:/kong.yml \
  kong:latest
```

### 2. Kubernetes 方式

```bash
helm repo add kong https://charts.konghq.com
helm repo update
helm install kong kong/kong --set ingressController.installCRDs=false
```

### 3. 声明式配置（kong.yml 示例）

```yaml
_format_version: "1.1"
services:
- name: example-service
  url: http://httpbin.org
  routes:
  - name: example-route
    paths:
    - /example
plugins:
- name: key-auth
  config:
    key_names: [ "apikey" ]
```

### 4. 添加插件（Lua 示例）

```lua
-- plugins/hello.lua
local plugin = {}

function plugin.execute(conf)
  kong.response.set_header("X-Hello", "World")
end

return plugin
```

> 将插件放在 `plugins` 目录并在 `kong.conf` 中启用。

## 进一步阅读

- 官方文档：<https://docs.konghq.com/>
- 插件开发指南：<https://docs.konghq.com/plugin-development/>
- GitHub 仓库：<https://github.com/Kong/kong>
