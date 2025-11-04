
---
title: netbird
---

**文件路径:** `src/content/docs/00/netbird_netbirdio.md`

```markdown
# NetBird（netbirdio/netbird）

NetBird 是一个现代化、零配置的 VPN 与网络管理平台，基于 WireGuard/自研协议实现安全、自动化、可扩展的多宿主网络。它提供轻量级代理、动态路由、身份鉴权、网络防火墙等核心功能，支持跨云、跨网络的私有 VPC 构建与管理。

## 主要特性

| 特性 | 说明 |
|------|------|
| **零配置** | 只需安装客户端或服务器，自动发现并建立加密隧道，无需手动分配 IP 或配置防火墙。 |
| **多宿主网络** | 支持多台物理/云服务器互联，形成统一的虚拟网络，类似于 VPC。 |
| **自动身份鉴权** | 内置 KMS/PKI 体系，提供身份凭证签发、签名验证，实现无密钥管理的安全接入。 |
| **分布式路由** | 使用 BGP/DPOT 或自研路由协议，支持多路径、可编程路由；可创建子网、网段隔离，支持 NAT。 |
| **网络防火墙与 ACL** | 提供基于身份、IP、子网的细粒度访问控制；支持实时状态同步与策略下发。 |
| **系统级 VPN** | 通过 `netbirdctl` 可开启整个系统的网络透明隧道，所有进程流量统一走 VPN。 |
| **多协议融合** | 根据信号质量可切换 UDP、TCP、WebSocket、Tor 等多种传输；支持多种平台（Linux、macOS、Windows、docker、k8s）。 |
| **云对象模型** | 通过 Web UI / REST API 管理节点、规则、网络；支持自动化脚本与 CI/CD 集成。 |

## 核心功能

1. **客户端 & 服务器组件**  
   * `netbird` 客户端：部署在终端设备或服务器上，负责建立隧道并注册到控制面。  
   * `netbird` 服务器（Control Plane）：管理节点注册、路由表、访问策略，实现统一管理。

2. **自动化安全模型**  
   * 每个节点在启动时生成或从 KMS 获取 ECC 密钥/证书。  
   * 通过 `netbirdctl` 生成安全凭证，并使用 TLS 证书签名通信。

3. **多宿主虚拟网络**  
   * 动态分配 IPV4、IPV6 子网。  
   * 通过 `netbird.yaml` 在 Kubernetes 中配置网络策略。  
   * 内置多路径选择与冗余保证带宽与可靠性。

4. **可编程防火墙**  
   * 支持基于 `Identity`, `IP`, `CIDR` 的访问控制。  
   * 规则可实时下发，支持灵活的分层安全策略。  

5. **易用命令行与 Web UI**  
   * `netbirdctl`：启动/停止、查看连接、管理节点。  
   * Web UI：集中监控节点状态、流量统计与策略管理。  

## 快速上手

```bash
# 安装客户端 (以 Linux 为例)
sudo apt-get update
sudo apt-get install netbird

# 启动客户端并加入网关
netbirdctl enroll http://<gateway-address> # 或者使用 Kiosk URL

# 查看连接状态
netbirdctl status
```

### 在 Kubernetes 中使用

```yaml
# netbird.yaml
netbird:
  host: "10.123.45.678:20000"
  token: "<node-token>"
```

```bash
kubectl apply -f netbird.yaml
```

## 参考文档

* 官方主页: https://netbird.io  
* GitHub 项目: https://github.com/netbirdio/netbird  
* 文档仓库: https://github.com/netbirdio/docs  
* 快速安装指引: https://docs.netbird.io/docs/installation  
* API 参考: https://docs.netbird.io/api  
``` 

> 以上内容为项目主要特性与使用方式，适合作为项目文档的简要摘要。 

``` 
