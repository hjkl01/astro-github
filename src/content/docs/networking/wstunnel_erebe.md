---
title: wstunnel
---

## 项目简介

wstunnel 是一个开源工具，用于通过 WebSocket 或 HTTP2 协议隧道所有网络流量，从而绕过防火墙和深度包检测 (DPI)。它支持静态二进制文件，便于部署，无需额外依赖。

## 主要功能

- **隧道类型**：支持 TCP、UDP、Unix 套接字和 Stdio 的静态转发和反向隧道。
- **动态隧道**：提供 Socks5、HTTP 代理和透明代理功能。
- **安全特性**：支持 TLS/mTLS 证书认证，证书自动重载；支持 IPv6。
- **传输协议**：使用 WebSocket（性能更佳）或 HTTP2 作为传输层。
- **其他特性**：支持代理协议、自定义 HTTP 头、DNS 解析器、连接池等。
- **平台支持**：提供静态二进制文件，支持 Linux、macOS、Windows 等平台。

## 使用方法

### 服务器端

启动 wstunnel 服务器：

```bash
wstunnel server wss://[::]:8080
```

这将在端口 8080 上启动 WebSocket 服务器，支持 TLS。

### 客户端

创建 SOCKS5 代理隧道：

```bash
wstunnel client -L socks5://127.0.0.1:8888 wss://server:8080
```

这将在本地端口 8888 创建 SOCKS5 代理，通过服务器隧道流量。

### 示例用法

- **绕过企业代理**：使用 HTTP 代理连接到服务器，然后隧道 SSH 流量。
- **WireGuard 隧道**：通过 wstunnel 隐藏 WireGuard 流量。
- **反向隧道**：从服务器访问本地服务。
- **透明代理**：在 Linux 上无缝代理任何程序。

更多详细示例和选项请参考项目的 GitHub README。
