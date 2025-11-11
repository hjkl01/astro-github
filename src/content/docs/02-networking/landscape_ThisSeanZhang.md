---
title: landscape
---

# Landscape

Landscape 是一个基于 Rust / eBPF / AF_PACKET 的 Web 工具，帮助您轻松地将您喜欢的 Linux 发行版配置为路由器。

## 核心功能

- **流量分流控制**：支持 SIP-CIDR、MAC、DIP、域名、地理位置匹配规则
- **eBPF 路由**：高效的网络包处理
- **独立 DNS 配置**：为每个流量流提供独立的 DNS 配置和缓存，防止 DNS 污染和泄漏
- **Docker 容器流量导入**：将流量导入到 Docker 容器中
- **地理位置管理**：管理多个地理位置源

## 其他功能

- **IP 配置**：静态 IP、DHCP 客户端、PPPoE、DHCP 服务器、IPv6 支持
- **流量控制模块**：使用 IP/MAC 标记流量，每个流量流可有自己的 DNS 设置
- **DNS**：支持 DoH、DoT、DoQ 上游，域名特定上游 DNS，DNS 劫持，地理站点文件支持
- **NAT (eBPF)**：基本 NAT 支持，静态映射/端口转发
- **指标**：报告连接统计（字节/包），显示活跃连接
- **Docker**：基本 Docker 容器管理和运行时
- **Wi-Fi**：启用/禁用 Wi-Fi，使用 hostapd 创建 AP
- **存储**：使用数据库而非文件配置，导出配置为 TOML

## 使用方法

### 系统要求

- 支持的 Linux 内核：6.9 或更高版本
- （可选）Docker

### 手动启动

1. 创建配置目录：

   ```
   mkdir -p /root/.landscape-router
   ```

2. 从 [Releases](https://github.com/ThisSeanZhang/landscape/releases) 下载 **static.zip** 并解压到 `/root/.landscape-router/static`

3. 如果您有桌面环境和浏览器，可以跳过此步骤。否则，参考 [配置文档](https://landscape.whileaway.dev/config/) 创建 `landscape_init.toml`

4. 从 [Releases](https://github.com/ThisSeanZhang/landscape/releases) 下载发布二进制文件，然后以 root 身份运行：

   ```
   ./landscape-webserver
   ```

   默认端口：**6300**，默认用户名：**root**，默认密码：**root**。使用 `./landscape-webserver --help` 查看其他选项。

5. 确认一切正常后，可以将其设置为 systemd 服务。创建 `/etc/systemd/system/landscape-router.service`：

   ```
   [Unit]
   Description=Landscape Router

   [Service]
   ExecStart=/root/landscape-webserver  # 请相应修改此路径
   Restart=always
   User=root
   LimitMEMLOCK=infinity

   [Install]
   WantedBy=multi-user.target
   ```

### Armbian 集成

参考 [Armbian 集成指南](https://landscape.whileaway.dev/compilation/armbian.html)

## 构建说明

参考 [构建文档](https://landscape.whileaway.dev/compilation/) 或 [交叉编译指南](https://landscape.whileaway.dev/compilation/cross.html)

## 许可证

- `landscape-ebpf`：GNU GPL v2.0
- 其他部分：GNU GPL v3.0
