
---
title: OpenGFW
---


# OpenGFW（apernet/OpenGFW）

[GitHub](https://github.com/apernet/OpenGFW)

## 项目简介
OpenGFW 是一个用于突破中国大陆网络防火墙（Great Firewall）的开源工具。它通过在本地提供一个 HTTP/HTTPS/WS/SOCKS5 代理，将请求转发到可突破防火墙的远程节点，实现安全、稳定的网络访问。

## 主要特性
- **多协议代理**：支持 HTTP、HTTPS、WebSocket、SOCKS5 等协议。  
- **自动切换节点**：内置节点池，支持健康检查与负载均衡。  
- **DNS 解析**：支持 DNS over HTTPS（DoH）/DNS over TLS，避免 DNS 泄露。  
- **简易配置**：提供 YAML/JSON 配置文件，支持命令行参数优先级。  
- **日志与监控**：详细的访问日志、错误日志，支持 Prometheus exporter。  
- **可扩展插件**：支持自定义插件、插件化日志、插件化策略。

## 功能模块
- **客户端（Client）**  
  - 启动本地代理服务器。  
  - 读取配置文件或命令行参数。  
  - 透明代理或手动代理。  
- **服务端（Server）**  
  - 监听公网 IP，提供突破 GFW 的转发功能。  
  - 支持多种传输协议与加密方式。  
- **管理接口**  
  - HTTP API 用于动态添加/删除节点、查询状态。  
  - Web UI（可选）查看实时流量、节点状态。

## 快速使用

### 1. 安装

```bash
# 直接下载
wget https://github.com/apernet/OpenGFW/releases/latest/download/ogfw-linux-amd64.tar.gz
tar -xzvf ogfw-linux-amd64.tar.gz
cd ogfw

# 或使用 Go 直接构建
go build -o ogfw ./cmd/ogfw
```

### 2. 配置文件示例（`config.yaml`）

```yaml
# 本地代理
proxy:
  listen: 127.0.0.1:1080
  type: socks5

# 远程服务器
remote:
  address: your.remote.server:443
  protocol: ws
  tls:
    insecure: false
    ca_file: /path/to/ca.crt

# DNS
dns:
  server: https://dns1.opendns.com/dns-query

# 日志
log:
  level: info
  file: ogfw.log
```

### 3. 启动客户端

```bash
./ogfw -c config.yaml
```

设置系统或浏览器代理为 `127.0.0.1:1080` 即可。

### 4. 启动服务器（示例）

```bash
./ogfw -s -c server.yaml
```

`server.yaml` 与 `client.yaml` 结构相同，只是 `proxy` 部分可以省略，服务器只需要 `remote` 配置。

## 进阶使用

- **动态节点管理**  
  通过 `GET /status` 接口获取节点健康状态；通过 `POST /nodes` 添加新节点。

- **TLS/QUIC 加密**  
  在 `remote.tls` 配置中设置 `quic: true`，即可使用 QUIC 传输。

- **插件**  
  在 `plugins` 目录放置 Go 插件，程序启动时自动加载。

## 贡献与支持

- 代码托管在 GitHub 上，欢迎 Issue 与 Pull Request。  
- 文档与示例已包含在仓库中。  
- 若遇到问题，请先查看 Issues，或在 Discussions 讨论。

---

**项目地址**  
[https://github.com/apernet/OpenGFW](https://github.com/apernet/OpenGFW)
