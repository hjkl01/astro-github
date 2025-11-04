
---
title: mihomo
---


# Mihomo

项目地址: https://github.com/MetaCubeX/mihomo

## 主要特性

- **轻量级跨平台**：基于 Go 开发，运行无外部依赖；支持 Windows、Linux、macOS、FreeBSD 等操作系统。
- **兼容 V2Ray**：与 V2Ray 核心保持高度兼容，可直接使用 v2ray 生成的路由、VMess/VLESS 等配置。
- **多协议支持**：VMess、VLESS、Trojan、Shadowsocks、Socks5 等主流代理协议均已支持。
- **灵活传输层**：支持 TCP、TLS、WebSocket、gRPC、HTTP1、HTTP2、QUIC、mKCP 等多种传输协议与加密方式。
- **高性能路由**：实现负载均衡、GeoIP/ASN 路由、域名白名单/黑名单等高级路由功能；支持分级代理与链路组合。
- **流量监控与限速**：可实时监控流量，支持按 IP/域名/协议/协议版本等维度进行速率限制与流量计费。
- **安全与隐私**：支持 AES-256-GCM、ChaCha20-Poly1305、none 等加密方式；可启用 DNS-over-HTTPS、透明代理与 UDP 代理。
- **多用户管理**：单机多用户访问，支持自定义用户密钥与访问控制。
- **易于部署**：提供预编译二进制包、Go 模块安装、Docker 镜像等多种安装方式；支持 systemd、init.d 等常见服务管理。

## 功能说明

| 功能 | 说明 |
|------|------|
| **代理协议** | VMess、VLESS、Trojan、Shadowsocks、Socks5 等 |
| **传输层** | TCP、TLS、WebSocket、mKCP、Quic、HTTP1/2、gRPC |
| **加密方式** | AES-GCM、ChaCha20-Poly1305、none |
| **配置文件** | 使用 YAML 语法，支持完整自定义 |
| **路由器** | 基于域名、IP、ASN、境外/内网、路径等信息实现精细路由 |
| **监控** | 提供 RESTful API，支持流量实时统计、节点状态监测 |
| **限速** | 按用户、IP、协议、端口等多维度设置限速策略 |
| **管理面板** | 默认在 8080 端口提供 Web UI 与配置 API |
| **日志** | 支持自定义日志级别、输出格式、远程接收（如 ES、Grafana） |

## 用法

### 1. 安装

- **使用 Go 安装（推荐）**

```bash
# 需要已安装 Go 环境
go install github.com/MetaCubeX/mihomo@latest
```

- **下载预编译二进制包**

```bash
wget https://github.com/MetaCubeX/mihomo/releases/download/vX.Y.Z/mihomo_linux_amd64.tar.gz
tar -xzf mihomo_linux_amd64.tar.gz
sudo mv mihomo /usr/local/bin/
```

> 省略 `X.Y.Z` 具体版本号，实际使用时请替换为最新发布版本。

### 2. 创建配置示例 `config.yaml`（仅包含最小必需字段，实际配置可根据需求扩展）：

```yaml
log:
  level: info
  encoding: console

# 处理进来的连接
inbounds:
  - port: 1080
    protocol: socks
    listen: 0.0.0.0
    auth: noauth

# 发送请求的出口
outbounds:
  - protocol: vmess
    settings:
      vnext:
        - address: example.com
          port: 443
          users:
            - id: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
              alterId: 0
              security: auto
    streamSettings:
      network: ws
      security: tls
```

> 详细字段说明请查阅官方 README 或内部文档。

### 3. 启动

```bash
mihomo -config ./config.yaml
```

> 或者直接使用 `mihomo` 在路径已存放配置文件的目录下运行。

### 4. systemd 服务示例

```ini
# /etc/systemd/system/mihomo.service
[Unit]
=Mihomo Proxy Service
After=network.target

[Service]
ExecStart=/usr/local/bin/mihomo -config /etc/mihomo/config.yaml
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

然后：

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now mihomo
```

### 5. 访问管理面板

默认监听 8080 端口，浏览器访问：

```
http://localhost:8080
```

> 可通过 API `/api/config` 查询或更新配置；具体路由与使用示例可参考官方文档。

---

> 如需进一步定制与高级使用，请阅读项目 README 与内置示例配置，或参考官方 Wiki。祝使用愉快！