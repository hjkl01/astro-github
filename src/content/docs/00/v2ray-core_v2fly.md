
---
title: v2ray-core
---


# v2ray-core（v2fly}

> GitHub 项目地址: https://github.com/v2fly/v2ray-core

## 主要特性

- **多协议支持**：兼容 VMess、VLess、Shadowsocks、Trojan、Socks 等协议，满足不同网络空间隐藏需求。
- **灵活路由**：提供基于域名、IP、端口的路由规则，支持中间人代理、策略路由和全局代理。
- **插件体系**：支持动态插件，支持 TLS、GRPC、HTTP/2、QUIC 等多种传输层协议。
- **边缘网络与反向代理**：支持多链路连接、节点负载均衡与容错，可实现多节点代理跳转。
- **跨平台**：支持 Linux、Windows、macOS、iOS、Android、ARM 等多平台，统一配置文件。

## 核心功能

1. **传输层加密**  
   - TLS、TLS（TLS 1.3）、Websocket、HTTP/2、QUIC、GRPC 等多种保密传输方式。

2. **链路隧道**  
   - 支持 `vmess`, `vless`, `socks`, `shadowsocks` 等隧道协议，保证数据传输高效且匿名。

3. **策略路由**  
   - 根据 `outbounds` 与 `routing` 的结合，精细化管理流量走向。  
   - 支持 `direct`, `block`, `blackhole`, `shunt` 等策略。

4. **插件与自定义**  
   - `handler`、`mux`、`dispatcher` 等插件系统，可自行扩展。  
   - 提供 `speedtest`、`健康检查` 等工具。

5. **监控与管理**  
   - HTTP API、Prometheus 指标、可视化 `dashboard`。  
   - 支持远程重启、动态更新配置。

## 用法示例

1. **安装**  
   ```bash
   # 使用官方 Docker 镜像
   docker pull v2fly/v2ray-core:latest
   docker run -d --name v2ray \
     -v /etc/v2ray:/etc/v2ray \
     -p 1080:1080 -p 80:80 v2fly/v2ray-core
   ```

2. **配置文件（toml）**  
   ```toml
   [inbounds]
     [[inbounds]]
     port = 1080
     protocol = "socks"
     listen = "0.0.0.0"

   [outbounds]
     [[outbounds]]
     protocol = "vmess"
     settings = {
       address = "server.example.com",
       port = 443,
       uuid = "YOUR_UUID",
       alterId = 64,
       network = "ws",
       ws_settings = {
         path = "/websocket",
         headers = { Host = "example.com" }
       }
     }

   [routing]
     routers = [
       { domain = ["geosite:cn"], outbounds = "direct", type = "field" }
     ]
   ```

3. **启动 & 验证**  
   - 在客户端使用 SOCKS5 代理指向 `127.0.0.1:1080`。  
   - 访问 `https://example.com`，验证是否走正确的隧道。

## 文档与示例

- 官方文档: https://www.v2fly.org/
- 示例配置: https://github.com/v2fly/v2ray-core/tree/master/geoip

---

> **提示**：将配置文件放在 `/etc/v2ray/config.json` 或 `/etc/v2ray/config.toml`，然后重启服务即可生效。 全部功能可通过 `v2ctl` 命令行工具进一步管理。