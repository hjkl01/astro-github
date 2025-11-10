---
title: netbird
---

# NetBird

## 项目简介

NetBird 是一个开源的网络安全平台，将配置-free 的点对点私有网络与集中式访问控制系统结合在一起，使创建组织或家庭的安全私有网络变得简单。

## 主要功能

- **连接**：基于 WireGuard 的覆盖网络，自动通过加密隧道连接您的机器，无需打开端口、复杂的防火墙规则、VPN 网关等。
- **安全**：通过应用粒度访问策略实现安全远程访问，同时允许从单一位置直观管理它们。在任何基础设施上通用工作。
- **SSO & MFA 支持**：支持单点登录和多因素认证。
- **管理 Web UI**：提供管理员 Web 界面。
- **Public API**：提供公共 API 接口。
- **自动化**：支持自动化网络配置。
- **多平台支持**：Linux、Mac、Windows、Android、iOS、OpenWRT、Docker 等。
- **其他特性**：
  - 内核 WireGuard
  - 点对点连接
  - 自动对等发现和配置
  - 访问控制 - 组和规则
  - 设置密钥用于批量网络配置
  - 连接中继回退
  - IdP 集成
  - 活动日志记录
  - 自托管快速启动脚本
  - 路由到外部网络
  - 私有 DNS
  - 设备姿态检查
  - IdP 组与 JWT 同步
  - NAT 穿越与 BPF
  - 多用户支持
  - 点对点加密
  - 量子抵抗与 Rosenpass
  - 定期重新认证
  - 无服务器

## 使用方法

### 使用 NetBird Cloud 快速开始

1. 在 [https://app.netbird.io/install](https://app.netbird.io/install) 下载并安装 NetBird。
2. 按照步骤使用 Google、Microsoft、GitHub 或您的电子邮件地址注册。
3. 检查 NetBird [管理 UI](https://app.netbird.io/)。
4. 添加更多机器。

### 自托管 NetBird 快速开始

**基础设施要求：**

- 至少 1CPU 和 2GB 内存的 Linux VM。
- VM 应在 TCP 端口 80 和 443 以及 UDP 端口 3478、49152-65535 上公开访问。
- 指向 VM 的公共域名。

**软件要求：**

- VM 上安装 Docker 和 docker-compose 插件，或 Docker 和版本 2 或更高的 docker-compose。
- 安装 jq（在大多数发行版中可用，通过 `sudo apt install jq` 或 `sudo yum install jq` 安装）。
- 安装 curl（在大多数发行版中可用，通过 `sudo apt install curl` 或 `sudo yum install curl` 安装）。

**步骤：**

1. 下载并运行安装脚本：

   ```bash
   export NETBIRD_DOMAIN=netbird.example.com; curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started-with-zitadel.sh | bash
   ```

2. 完成后，您可以通过 `docker-compose` 管理资源。

## 内部架构

- 网络中的每台机器运行 NetBird Agent（或客户端），管理 WireGuard。
- 每个代理连接到管理服务，保存网络状态、管理对等 IP，并将网络更新分发给代理（对等）。
- NetBird 代理使用 pion/ice 库实现的 WebRTC ICE 来发现连接候选者，以在机器之间建立点对点连接。
- 使用 STUN 服务器帮助发现连接候选者。
- 代理通过信号服务协商连接，传递带有候选者的 p2p 加密消息。
- 有时 NAT 穿越由于严格 NAT（例如移动运营商级 NAT）而不成功，无法建立 p2p 连接。此时系统回退到中继服务器 TURN，并通过 TURN 服务器建立安全的 WireGuard 隧道。

Coturn 是 NetBird 设置中成功用于 STUN 和 TURN 的工具。

## 许可证

此仓库根据 BSD-3-Clause 许可证授权，适用于仓库的所有部分，除了 management/、signal/ 和 relay/ 目录。这些目录根据 GNU Affero General Public License version 3.0 (AGPLv3) 授权。请参阅每个目录内的相应 LICENSE 文件。

WireGuard 和 WireGuard 标志是 Jason A. Donenfeld 的注册商标。
