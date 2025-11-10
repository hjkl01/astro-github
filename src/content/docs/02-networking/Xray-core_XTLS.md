---
title: Xray-core
---

# Xray-core (XTLS)

**GitHub 地址**: [https://github.com/XTLS/Xray-core](https://github.com/XTLS/Xray-core)

## 主要特性

- **跨平台**：支持 Windows、macOS、Linux、FreeBSD、Android、iOS、OpenBSD、NetBSD、Solaris 等多种操作系统。
- **模块化设计**：核心组件与插件分离，易于扩展与维护。
- **多协议支持**：
  - VMess、VLESS、Trojan、Socks、Shadowsocks、HTTP、HTTPS、SNI、WebSocket、gRPC、Quic 等流量代理协议。
  - 支持多种加密方式（AES-256-GCM、CHACHA20-poly1305 等）。
- **安全性能**：内置多重安全机制，支持 TLS、TLS+XTLS、TLS+QUIC、TLS+WebSocket 等。
- **高性能**：使用 Go 语言实现，充分利用多核 CPU、异步 IO，支持高并发连接。
- **配置灵活**：通过 JSON 配置文件完成链路构建，支持多路由、负载均衡、流量控制、访问控制等。
- **插件系统**：可插拔的插件（如 DNS、HTTP 代理、TLS 终端、验证插件）可在链路中随意插入。
- **监控与日志**：提供对接 Prometheus、Grafana、OpenTelemetry 等监控系统，支持详细日志输出。

## 功能概览

| 功能 | 描述 |
|------|------|
| **链路构建** | 通过 `inbounds` / `outbounds` / `routers` / `domains` 等模块构建完整代理链路。 |
| **路由策略** | 根据域名、IP、协议、流量等多维度进行路由决策，支持 `balancer`、`detour`、`direct` 等方式。 |
| **多协议混淆** | 支持多协议混淆与链路混合，增强抗干扰能力。 |
| **TLS/XTLS 加密** | 支持 TLS、XTLS、QUIC 等加密协议，提供更高安全性与性能。 |
| **插件功能** | 通过插件实现 DNS 解析、HTTP 代理、TLS 终端、用户鉴权、流量限制等。 |
| **监控与统计** | 内置统计接口，可生成流量报表、连接数、延迟等指标。 |
| **CLI 工具** | 命令行启动、配置验证、日志查看、进程管理等工具。 |

## 用法示例

1. **克隆仓库**

   ```bash
   git clone https://github.com/XTLS/Xray-core.git
   cd Xray-core
   ```

2. **编译（可选）**

   ```bash
   go build -o xray
   ```

   或直接使用预编译二进制文件。

3. **创建配置文件（config.json）**

   ```json
   {
     "log": {
       "loglevel": "info"
     },
     "inbounds": [
       {
         "port": 1080,
         "protocol": "socks",
         "settings": {
           "auth": "noauth",
           "udp": true
         }
       }
     ],
     "outbounds": [
       {
         "protocol": "vmess",
         "settings": {
           "vnext": [
             {
               "address": "example.com",
               "port": 443,
               "users": [
                 {
                   "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                   "alterId": 64,
                   "security": "auto"
                 }
               ]
             }
           ]
         },
         "streamSettings": {
           "network": "ws",
           "wsSettings": {
             "path": "/path"
           }
         }
       }
     ]
   }
   ```

4. **启动 Xray**

   ```bash
   ./xray run -config config.json
   ```

5. **验证连接**

   - 配置系统代理为 `socks5://127.0.0.1:1080`，访问外部网站即可验证代理功能。

6. **日志与监控**

   - 日志文件默认位于当前目录下 `log` 文件夹。
   - 通过配置 `metrics` 开启 Prometheus 接口。

## 进一步阅读

- 官方文档: <https://xtls.github.io/>
- 配置示例和插件列表: <https://github.com/XTLS/Xray-core/blob/master/README.md>
- 贡献指南: <https://github.com/XTLS/Xray-core/blob/master/CONTRIBUTING.md>