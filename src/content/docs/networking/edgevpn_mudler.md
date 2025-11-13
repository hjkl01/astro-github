---
title: edgevpn
---

# EdgeVPN

EdgeVPN 是一个完全去中心化的、不可变的、静态编译的P2P VPN和反向代理，使用libp2p构建私有去中心化网络，通过共享密钥访问。

## 功能

- **创建VPN**：在P2P对等点之间建立安全VPN
  - 自动为节点分配IP
  - 嵌入小型DNS服务器解析内部/外部IP
  - 创建信任区域防止令牌泄露时网络访问
- **作为反向代理**：分享TCP服务，如ngrok，但通过P2P网络暴露TCP服务而无需建立VPN连接
- **发送文件via P2P**：在节点之间发送文件而无需建立VPN连接
- **作为库使用**：在Golang代码中轻松插入分布式P2P账本

## 用法

EdgeVPN 通过生成令牌（或配置文件）在不同机器、主机或对等点之间共享，以访问去中心化安全网络。每个令牌都是唯一的，标识网络，无需中央服务器设置或指定主机IP。

### 生成配置

生成新配置文件：

```bash
edgevpn -g > config.yaml
```

或生成便携令牌：

```bash
EDGEVPNTOKEN=$(edgevpn -g -b)
```

### 作为VPN

启动VPN，只需运行 `edgevpn` 无参数。

多主机示例：

```bash
# 节点A
EDGEVPNTOKEN=.. edgevpn --address 10.1.0.11/24
# 节点B
EDGEVPNTOKEN=.. edgevpn --address 10.1.0.12/24
```

`--address` 是每个节点的虚拟唯一IP，节点将从VPN中可达。您可以自由分配IP给网络节点，可以用 `IFACE`（或 `--interface`）覆盖默认 `edgevpn0` 接口。

注意：节点间建立连接可能需要时间。至少等待5分钟，取决于主机背后的网络。

### 安装

从[发布页面](https://github.com/mudler/edgevpn/releases)下载预编译的静态发布。您可以将其安装到系统中或直接运行。

## 示例用例

### 去中心化k3s测试集群

1. 生成EdgeVPN配置：`edgevpn -g > vpn.yaml`
2. 启动VPN：
   - 节点A：`sudo IFACE=edgevpn0 ADDRESS=10.1.0.3/24 EDGEVPNCONFIG=vpn.yml edgevpn`
   - 节点B：`sudo IFACE=edgevpn0 ADDRESS=10.1.0.4/24 EDGEVPNCONFIG=vpn.yml edgevpn`
3. 启动k3s：
   - 节点A：`k3s server --flannel-iface=edgevpn0`
   - 节点B：`K3S_URL=https://10.1.0.3:6443 K3S_TOKEN=xx k3s agent --flannel-iface=edgevpn0 --node-ip 10.1.0.4`

## 警告

这不是生产就绪的软件，未经过完整安全审计。请勿用于敏感流量或生产环境。主要用于开发和实验。

更多信息请查看[文档](https://mudler.github.io/edgevpn)。
