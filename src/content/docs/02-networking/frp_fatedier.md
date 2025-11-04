
---
title: frp
---


---
title: "Frp（fatedier/frp）项目概述"
author: "ChatGPT"
date: 2025-10-30
path: src/content/docs/00/frp_fatedier.md
---

# Frp（fatedier/frp）简介

Frp（Fast Reverse Proxy）是一款高性能、轻量级的反向代理应用。它支持多种协议（TCP/UDP/HTTP/HTTPS/WebSocket），可以把内网服务暴露到公网上，常用于：

- 内网穿透
- 隧道代理
- 防火墙突破
- 远程办公

---

## 主要特性

| 功能 | 说明 |
| ---- | ---- |
| **高性能** | 内置多路复用、低延迟、低内存使用 |
| **多协议支持** | TCP、UDP、HTTP、HTTPS、WebSocket、HTTP 隧道 |
| **安全** | 支持 TLS 加密、基于 token 的鉴权、路径、域名白名单 |
| **灵活配置** | 支持配置文件 + 命令行参数，支持多实例 |
| **动态路由** | 支持按路径、域名、IP 自动转发 |
| **负载均衡** | 支持 round‑robin 与 least‑conn |
| **监控与日志** | 内置 web 管理界面，支持 Prometheus、Grafana 监控 |
| **高可用** | 支持 failover、热更新、分布式部署 |
| **易于集成** | 通过 Docker/Kubernetes 原生镜像，二进制可直接执行 |

---

## 核心组件

| 组件 | 作用 |
| ---- | ---- |
| **frps** | 服务器端，负责接收来自客户端的隧道连接，转发给对应的目标服务 |
| **frpc** | 客户端/跳板机，建立对 frps 的连接，并根据配置向内网服务开启通道 |
| **frpcd** | 为 frpc 提供统一管理，支持多账号多通道 |
| **frpctl** | 命令行工具，集成 frps 与 frpc 的管理操作 |
| **frp-web** | Web UI 界面（可选），提供实时监控与管理功能 |

---

## 示例用法

### 1. 服务器端（frps）配置

```yaml
# frps.ini
[common]
bind_port = 7000
vhost_http_port = 8080
vhost_https_port = 8443
# token 可选，用于验证客户端身份
auth_token = "mypassword"
```

启动 `frps`：

```bash
./frps -c ./frps.ini
```

### 2. 客户端（frpc）配置

```yaml
# frpc.ini
[common]
server_addr = x.x.x.x          # frps 服务器公网 IP
server_port = 7000
auth_token = "mypassword"

# TCP 隧道：暴露本地 8080 端口到公网
[web]
type = tcp
local_ip = 127.0.0.1
local_port = 8080
custom_domains = www.example.com
```

启动 `frpc`：

```bash
./frpc -c ./frpc.ini
```

> **移植技巧**  
> 通过 Docker 部署可方便开启：

```bash
docker run -d --name frps \
  -p 7000:7000 -p 8080:8080 -p 8443:8443 \
  -v ~/frps.ini:/etc/frp/frps.ini \
  fatedier/frps

docker run -d --name frpc \
  -p 0:0 -v ~/frpc.ini:/etc/frp/frpc.ini \
  fatedier/frpc
```

### 3. HTTP/HTTPS 隧道

在 `frps.ini` 开启 vhost:

```ini
vhost_http_port = 80
vhost_https_port = 443
```

客户端配置：

```ini
[http]
type = http
local_port = 80
custom_domains = www.example.com
```

Frp 会自动为 `www.example.com` 指配 HTTP/HTTPS 隧道。

### 4. 监控

```bash
./frps -c frps.ini
# 默认开启 Prometheus metrics at http://<server_ip>:7000/metrics
```

集成 Grafana 或 Prometheus 后即可实时查看连接数、带宽等指标。

---

## 常见命令

| 命令 | 说明 |
| ---- | ---- |
| `frps -c frps.ini` | 启动服务器端 |
| `frpc -c frpc.ini` | 启动客户端 |
| `frpctl` | 统一管理 frps/frpc（列出状态、重启、停止） |

---

## 项目地址

- **GitHub**：<https://github.com/fatedier/frp>

该仓库包含：

- `docs/`：官方文档与示例
- `conf/`：示例配置
- `Dockerfile`：供应官方镜像

---

**结语**

Frp 以其轻量、高性能与多协议的特性，成为构建内网穿透、远程办公、云端代理的首选工具。通过灵活的配置与简单的部署方式，可满足从个人开发到企业级部署的多种场景。