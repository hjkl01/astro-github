
---
title: tailscale
---

# Tailscale 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/tailscale/tailscale)

## 主要特性
Tailscale 是一个基于 WireGuard 协议的零配置 VPN 解决方案，主要特性包括：
- **零配置连接**：无需手动配置防火墙或端口转发，通过 Tailscale 的协调服务器自动建立安全的点对点连接。
- **端到端加密**：使用 WireGuard 提供高效、安全的加密隧道，支持多平台设备间的无缝连接。
- **访问控制**：基于 ACL（访问控制列表）的细粒度权限管理，支持用户和设备级别的策略。
- **跨平台支持**：兼容 Windows、macOS、Linux、iOS、Android 等多种操作系统，以及 Docker 和 Kubernetes 等容器环境。
- **MagicDNS**：内置 DNS 服务，允许使用简单的主机名访问设备，而非 IP 地址。
- **子网路由**：支持访问本地子网，而无需在每个设备上安装 Tailscale。
- **开源与自托管**：核心代码开源，用户可选择自托管 Headscale 服务器以避免依赖 Tailscale 的云服务。

## 主要功能
Tailscale 的核心功能聚焦于简化网络连接和安全访问：
- **设备间直接连接**：自动发现并连接网络中的设备，形成一个安全的虚拟网络（tailnet）。
- **远程访问**：允许从任何位置安全访问家庭或企业网络中的资源，如服务器、NAS 或打印机。
- **协作与共享**：支持团队协作，通过共享节点或出口节点实现共享访问。
- **监控与日志**：提供 Web 界面查看网络拓扑、连接状态和日志，支持 API 集成。
- **集成扩展**：与第三方工具如 Terraform、Puppet 等集成，便于自动化部署。

## 用法
### 安装
1. 访问 [Tailscale 官网](https://tailscale.com/download) 下载适用于你的操作系统的安装包。
2. 对于 Linux，可使用包管理器安装，例如：
   ```
   curl -fsSL https://tailscale.com/install.sh | sh
   ```

### 基本用法
1. **注册与登录**：
   - 运行 `tailscale up` 命令，或通过 Web 界面登录 Tailscale 账户（支持 Google、Microsoft 等身份提供商）。
   - 首次连接会生成一个认证链接，打开浏览器授权设备加入 tailnet。

2. **连接设备**：
   - 安装后，运行 `tailscale up` 启用 VPN。
   - 使用 `tailscale status` 查看连接的设备列表。
   - 通过主机名（如 `device.tailnet.ts.net`）或 IP 直接访问其他设备。

3. **高级配置**：
   - 编辑 ACL 文件（JSON 格式）管理访问权限，并在 Tailscale 控制台应用。
   - 启用子网路由：`tailscale up --advertise-routes=192.168.1.0/24`。
   - 退出节点：`tailscale up --exit-node=example-node` 用于将流量路由到指定设备。

4. **管理**：
   - 使用 Tailscale Admin Console（https://login.tailscale.com/admin）监控和管理整个网络。
   - 对于自托管，部署 Headscale 服务器并配置客户端指向自定义控制服务器。

Tailscale 适用于个人远程访问、团队协作或企业网络安全，入门简单，扩展性强。