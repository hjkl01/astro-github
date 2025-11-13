---
title: pingora
---


# Pingora

> 项目主页: [https://github.com/cloudflare/pingora](https://github.com/cloudflare/pingora)

## 简介  
Pingora 是 Cloudflare 开发的高性能、可编程 Web 代理服务器，采用 **Rust** 编写，目标是提供可扩展且低延迟的 HTTP/2、HTTP/3 代理服务。它可作为 CDN、负载均衡器或应用程序前置代理使用，并通过插件/DSL 让用户自由扩展功能。

## 主要特性  

| 特性 | 简述 |
|------|------|
| **多协议支持** | 同时支持 HTTP/1.1、HTTP/2、HTTP/3（QUIC） |
| **插件化可编程** | 通过其自定义 DSL (Pingora DSL) 或 Rust 编写插件，定制路由、TLS 处理、重定向、缓存等行为 |
| **高并发性能** | 采用 event-driven 的异步 I/O 模型，内置连接池与异步太使资源复用 |
| **可插拔 TLS** | 支持托管 & 任意 TLS（ECDHE, AES-GCM 等），可与 Cloudflare CA 集成 |
| **HTTP/3 负载均衡** | 通过 QUIC 进行多路径请求，提升网络鲁棒性 |
| **日志与指标** | 与 OpenTelemetry/Prometheus 兼容，提供丰富调试信息 |
| **简易部署** | 支持 container、k8s、systemd，官方 docker 镜像可直接使用 |

## 核心功能  

1. **连接代理** – 接收客户端请求后，按规则转发到上游服务器，并返回响应。  
2. **动态路由** – 通过配置文件或插件动态决定目标主机、路径、协议。  
3. **负载均衡** – 支持轮询、最小连接数、权重等多种算法。  
4. **缓存** – 可配置 FIN-to-cache，基于请求 URI、headers 进行智能缓存。  
5. **安全** – TLS 终止、HSTS、Origin Shield、Rate Limiting 等。  
6. **重写与重定向** – 通过 DSL 重写请求/响应。  
7. **请求摘要** – 支持 hostname 或 certificate 自定义摘要交换。  
8. **插件 API** – 提供对 HTTP 事件的钩子，允许自定义业务逻辑。  

## 用法示例  

```bash
# 克隆仓库
git clone https://github.com/cloudflare/pingora.git
cd pingora

# 使用官方 Docker 镜像
docker run -d --name pingora \
  -p 80:80 -p 443:443 \
  cloudflare/pingora

# 启动后访问 http://localhost/
```

### 配置示例 (`./conf/pingora.conf`)

```toml
[http]
  listen = "0.0.0.0:80"

[https]
  listen = "0.0.0.0:443"
  cert = "/etc/ssl/certs/server.crt"
  key  = "/etc/ssl/private/server.key"

[[routes]]
  pattern = "/api/*"
  dest = "http://backend-service:8000"
  weight = 1

[[routes]]
  pattern = "/"
  dest = "http://frontend-service:3000"
  weight = 1
```

> 插件与 DSL 示例请参见官方文档:  
> https://github.com/cloudflare/pingora/blob/main/docs/DSL.md  
> https://github.com/cloudflare/pingora/blob/main/docs/plugins.md  

## 安装与运行 (Rust)

```bash
# 克隆
git clone https://github.com/cloudflare/pingora.git
cd pingora

# 安装依赖
cargo build --release

# 运行
./target/release/pingora -c conf/pingora.conf
```

## 结语

Pingora 通过其插件化架构让开发者可以在 Cloudflare 高性能基础上实现自定义业务逻辑，适用于 CDN、代理、负载均衡和安全层等多种场景。更多详细信息请阅读其官方仓库与文档。  
```
