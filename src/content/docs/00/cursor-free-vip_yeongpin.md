
---
title: cursor-free-vip
---


# cursor‑free‑vip

- **仓库地址**：<https://github.com/yeongpin/cursor-free-vip>

## 项目简介
`cursor-free-vip` 是一个轻量级的命令行工具，旨在方便地在 Linux 系统上为服务绑定和管理虚拟 IP（VIP）。它通过直接操作 `ip` 命令、发送 ARP 通告以及保持后台守护进程，保证 VIP 在集群节点之间平滑切换，适用于需要零停机时间的高可用部署。

## 主要特性

| 功能 | 说明 |
|------|------|
| **快速添加/删除 VIP** | 只需几条命令即可把指定 IP 绑定到任意网络接口，或清除绑定。 |
| **ARP 广播与显式声明** | 操作完成后自动发送ARP请求，确保局域网内其它主机及时更新路由。 |
| **自定义配置文件** | 支持 YAML/JSON 配置，集中管理多项 VIP 方案，适合自动化流程。 |
| **健康检查** | 可检测指定端口/服务是否可达，确保 VIP 只绑定到健康节点。 |
| **跨平台（Linux）** | 基于 Bash / Go 的实现，兼容主流发行版。 |
| **日志与调试** | 提供详细日志，支持 `-v/--verbose` 级别。 |

## 安装方式

- **Bash 脚本**（最简方式，直接下载并 chmod）  
  ```bash
  wget https://raw.githubusercontent.com/yeongpin/cursor-free-vip/master/cursor-free-vip.sh
  chmod +x cursor-free-vip.sh
  sudo mv cursor-free-vip.sh /usr/local/bin/cursor-free-vip
  ```

- **Go 编译**（源代码编译）  
  ```bash
  git clone https://github.com/yeongpin/cursor-free-vip.git
  cd cursor-free-vip
  go build -o cursor-free-vip
  sudo mv cursor-free-vip /usr/local/bin/
  ```

## 用法示例

### 1. 立即绑定 VIP

```bash
# 添加 VIP 10.0.0.100 到 eth0
sudo cursor-free-vip add 10.0.0.100 --interface eth0

# 从 eth0 上移除 VIP
sudo cursor-free-vip del 10.0.0.100
```

### 2. 使用配置文件批量操作

`vip.yaml`

```yaml
interfaces:
  - name: eth0
    vip: 10.0.0.100
    netmask: 255.255.255.0
    ttl: 64
  - name: eth1
    vip: 10.0.0.101
    netmask: 255.255.255.0
```

```bash
# 添加配置文件中所有 VIP
sudo cursor-free-vip --config vip.yaml add
# 删除配置文件中所有 VIP
sudo cursor-free-vip --config vip.yaml del
```

### 3. 集成到系统服务

在 `systemd` 的 `ExecStart` 中调用 `cursor-free-vip`，并在相应的 `ExecStop` 清理 VIP，确保服务重启后 VIP 自动恢复。

```
[Unit]
Description=VIP Manager
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/cursor-free-vip --config /etc/cursor-free/vip.yaml add
ExecStop=/usr/local/bin/cursor-free-vip --config /etc/cursor-free/vip.yaml del
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 把 VIP 绑定后不可访问 | 检查 `iptables` 或 `firewalld` 是否阻止了 VIP 的流量。 |
| ARP 升级不及时 | 通过 `sudo arp -n` 查看 ARP 表，必要时手动 `sudo arp -d <IP>` 再重试。 |
| Linux 发行版报错“command not found” | 确认已把脚本或编译产物放到 `$PATH`，并给出可执行权限。 |

> **提示**：此工具仅在 Linux 环境中得到验证，若需在其他操作系统上使用，请自行评估兼容性。

---

> 你可以在项目前往 **Issues** 或 **Pull Requests** 贡献代码，也欢迎提交你在使用过程中遇到的问题。祝你使用愉快！
