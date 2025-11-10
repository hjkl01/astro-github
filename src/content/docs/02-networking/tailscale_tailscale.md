---
title: tailscale
---

# Tailscale

Tailscale 是基于 WireGuard 的即时、零配置 VPN 链接工具，能够让设备快速建立安全的私网互联。

## 主要特性
- **零配置、即插即用**：通过安装客户端、使用单一身份凭证即可自动完成网络配置，无需手动路由或防火墙规则。
- **多平台支持**：Windows、macOS、Linux、Android、iOS、FreeBSD 等，甚至容器和裸金属服务器都能无缝接入。
- **SSO 认证**：支持 Google、Microsoft 365、Okta、GitHub、SAML 等身份提供者，统一管理访问权与授权，满足企业级安全需求。
- **ACL（访问控制列表）**：通过 `tailscale.json` 文件定义细粒度访问规则，控制哪些节点间能互通、哪些端口可开放。
- **内置 SSH 与 HTTP/HTTPS 隧道**：无需额外工具即可通过 Tailscale 内网地址使用 `ssh host` 或访问服务。
- **出口节点（Exit Node）**：任何一台设备可作为 NAT Traversal 的出口，内部网络可安全访问 Internet 或公共 IP。
- **设备管理与监控**：Web UI 提供设备状态、流量统计、日志观测，并支持自动化脚本管理。
- **高性能 WireGuard**：底层采用 WireGuard 协议，提供低延迟、高吞吐量的加密隧道。
- **一次性启动器**：单次 `tailscale up` 即可完成连接与身份验证，后续自动保持连接。

## 功能概览
| 功能 | 命令示例 | 说明 |
|---|---|---|
| 安装 | `sudo apt install tailscale` | 安装客户端 |
| 启动 | `sudo tailscale up` | 连接网络，需凭证登录 |
| 查看状态 | `tailscale status` | 列出已加入的节点 |
| 心跳检查 | `tailscale ping <node>` | 诊断测距 |
| 共享服务 | `tailscale serve example.com:80` | 让外部访问本机服务 |
| 远程交互 | `ssh user@<node>` | 通过 VPN 连接 |
| 退出节点 | `sudo tailscale up --exit-node <node>` | 将此节点设为出口 |
| ACL 配置 | 编辑 `tailscale.json` <br> `tailscale up` | 重新加载 ACL 规则 |
| 预授权凭证 | `tailscale up --authkey key_abcdef` | 通过一次性密钥快速加入 |

## 使用方式
1. **在每台设备安装**  
   ```bash
   # Debian/Ubuntu
   curl -fsSL https://tailscale.com/install.sh | sh
   ```

2. **首次登录**  
   ```bash
   sudo tailscale up
   # 浏览器弹窗，使用 Google/Microsoft/OIDC 或令牌登录
   ```

3. **查看网络**  
   ```bash
   tailscale status
   # 可获得内网 IP 及设备列表
   ```

4. **为全局访问设置出口节点**  
   ```bash
   sudo tailscale up --exit-node <node-id>
   ```

5. **定义 ACL**  
   ```json
   {
     "ACLs": [
       {"Action": "accept", "Ports": ["*"], "Users": ["*"]}  // 简单示例
     ],
     "TagOwners": {
       "tag:admin": ["user@example.com"]
     }
   }
   ```
   保存后重启：
   ```bash
   sudo tailscale up
   ```

6. **利用 Tailscale 内部服务**  
   ```bash
   # 在机 B 上运行服务
   tailscale serve my.site.com:8080

   # 在机 A 上访问
   curl http://my.site.com
   ```

7. **SSH 访问**  
   ```bash
   ssh alice@bob  # 通过 Tailscale 内网直接 SSH
   ```

## 项目地址
[https://github.com/tailscale/tailscale](https://github.com/tailscale/tailscale)