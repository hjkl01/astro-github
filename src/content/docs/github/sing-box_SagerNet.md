
---
title: sing-box
---


# Sing-Box (SagerNet)

> GitHub 项目地址: <https://github.com/SagerNet/sing-box>

## 项目简介
Sing-Box 是一个高性能、跨平台的网络代理工具，旨在替代传统的 V2Ray、Trojan 等代理方案。它支持多种协议（如 VLESS、VMess、Trojan、Shadowsocks 等），并提供了可插拔的插件机制，方便用户自定义功能。

## 主要特性
- **高性能**：基于 Go 语言实现，充分利用多核 CPU，支持高并发连接。
- **多协议支持**：VLESS、VMess、Trojan、Shadowsocks、Socks5、HTTP 等。
- **插件化**：可动态加载插件（如 DNS、TLS、负载均衡等）。
- **跨平台**：支持 Windows、Linux、macOS、Android、iOS 等系统。
- **配置灵活**：采用 JSON/YAML 配置文件，支持命令行参数覆盖。
- **安全可靠**：支持 TLS 1.3、QUIC、TLS 1.2 等加密协议，防止流量被识别。

## 功能列表
| 功能 | 说明 |
|------|------|
| **代理服务** | 提供多协议代理节点，支持多用户配置。 |
| **负载均衡** | 通过插件实现 round-robin、least-connections 等策略。 |
| **DNS 加速** | 内置 DNS 缓存和多源 DNS 查询。 |
| **流量加密** | 支持 TLS 1.3、QUIC、TLS 1.2，防止流量被深度检测。 |
| **分流** | 根据域名、IP、路径等规则进行分流。 |
| **多平台客户端** | 内置 CLI 与 GUI 客户端，支持移动端。 |
| **监控与日志** | 提供详细日志与统计接口，支持 Prometheus。 |

## 用法

### 1. 安装

```bash
# 以 Linux 为例
wget https://github.com/SagerNet/sing-box/releases/latest/download/sing-box-linux-amd64
chmod +x sing-box-linux-amd64
sudo mv sing-box-linux-amd64 /usr/local/bin/sing-box
```

### 2. 基础配置

在 `config.json`（或 `config.yaml`）中配置代理节点：

```json
{
  "log": {
    "level": "info"
  },
  "inbounds": [
    {
      "port": 1080,
      "protocol": "socks",
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "server.example.com",
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
      }
    }
  ]
}
```

### 3. 启动

```bash
sing-box run -config ./config.json
```

### 4. 进阶使用

- **插件**：在 `plugins` 目录下放置插件，配置文件中通过 `plugins` 节点加载。
- **命令行参数**：`sing-box -h` 查看所有可用参数。
- **日志**：通过 `log.level` 控制日志级别；日志文件可通过 `log.file` 指定。

> 详细使用说明请参阅官方文档：<https://sing-box.sagernet.org/>

---

> 以上为 Sing-Box 项目核心信息与使用示例，供快速上手与参考。