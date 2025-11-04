
---
title: traefik
---


# Traefik

**项目地址:** https://github.com/traefik/traefik

## 主要特性

- **动态配置**：支持多种后端配置源（Docker、Kubernetes、Consul、Etcd、ZooKeeper 等），可根据变化自动更新路由。
- **反向代理与负载均衡**：自动发现服务实例，进行轮询、加权或最少连接负载分发。
- **HTTPS 自动化**：集成 Let's Encrypt，自动生成并续期 TLS 证书，支持 HTTP → HTTPS 自动跳转。
- **路由与中间件**：通过 `Router` 定义路径、主机、方法、正则等规则；通过 `Middleware` 添加重写、速率限制、限流、IP 白名单、重定向等功能。
- **运行状态监控**：内置健康检查、请求追踪、日志收集，支持 Prometheus、Datadog、Grafana 等监控系统。
- **Web Dashboard**：一键可视化，查看路由表、TLS 证书和监控数据。
- **多协议**：支持 HTTP/1.x、HTTP/2、WebSocket、TCP、UDP 等协议。
- **插件扩展**：自定义插件机制，可使用 Go、Lua、JavaScript、Python 编写插件。
- **高可用与无状态**：可以部署多实例，使用 Etcd 或 Consul 等进行集群状态同步。

## 常见用法

### 1. Docker 快速启动

```bash
docker run -d \
  -p 80:80 -p 443:443 \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v $(pwd)/traefik.yml:/etc/traefik/traefik.yml \
  traefik:v3.2
```

#### `traefik.yml` 简单示例

```yaml
entryPoints:
  web:
    address: ":80"
  websecure:
    address: ":443"

providers:
  docker:
    exposedByDefault: false

certificatesResolvers:
  http:
    acme:
      email: your@email.com
      storage: acme.json
      httpChallenge:
        entryPoint: web
```

### 2. 基 Docker Compose

```yaml
services:
  reverse-proxy:
    image: traefik:v3.2
    command:
      - "--providers.docker=true"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.http.acme.email=example@example.com"
      - "--certificatesresolvers.http.acme.storage=acme.json"
      - "--certificatesresolvers.http.acme.httpchallenge=true"
      - "--certificatesresolvers.http.acme.httpchallenge.entrypoint=web"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./acme.json:/acme.json"
      - "./traefik.yml:/traefik.yml"
```

### 3. 配置路由（Docker 标签）

```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.myapp.rule=Host(`example.com`)"
  - "traefik.http.routers.myapp.entrypoints=websecure"
  - "traefik.http.routers.myapp.tls.certresolver=http"
```

## 文档与社区

- 官方文档: https://doc.traefik.io/traefik/
- 贡献指南: https://github.com/traefik/traefik/blob/main/CONTRIBUTING.md
- 社区讨论: https://github.com/traefik/traefik/discussions
