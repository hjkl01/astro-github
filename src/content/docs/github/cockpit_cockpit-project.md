
---
title: cockpit
---

# Cockpit 项目

**项目地址:** [https://github.com/cockpit-project/cockpit](https://github.com/cockpit-project/cockpit)

## 主要特性
Cockpit 是一个现代化的服务器管理工具，提供基于 Web 的图形界面，用于管理和监控 Linux 系统。它支持多服务器管理、实时监控和自动化任务，具有以下核心特性：
- **实时系统监控**：显示 CPU、内存、磁盘、网络等资源使用情况，支持图表可视化。
- **多服务器支持**：可同时连接和管理多个服务器，通过 Fabric 技术实现无缝操作。
- **模块化设计**：内置模块包括用户账户管理、软件更新、日志查看、存储配置、网络设置、虚拟机管理（集成 libvirt）等。
- **安全性**：使用 WebSocket 协议，支持 HTTPS 加密，集成 PAM 认证，无需额外代理。
- **轻量级**：资源占用低，适合生产环境服务器。
- **开源免费**：基于 GPLv3 许可，支持多种 Linux 发行版（如 RHEL、Fedora、Ubuntu）。

## 主要功能
Cockpit 提供全面的系统管理功能，包括但不限于：
- **系统信息与性能**：查看主机信息、进程列表、资源利用率，支持警报通知。
- **账户与安全**：管理用户、组、防火墙（firewalld）和 SELinux 配置。
- **软件管理**：安装、更新和移除软件包，支持 DNF/YUM 或 APT。
- **存储与网络**：配置磁盘分区、LVM、iSCSI，以及网络接口和路由。
- **服务与日志**：启动/停止 systemd 服务，浏览和过滤系统日志（journalctl）。
- **虚拟化**：创建、启动、停止和管理 KVM/QEMU 虚拟机。
- **终端集成**：内置 Web 终端，支持 SSH 连接远程服务器。
- **扩展性**：通过插件系统添加自定义功能，如 Kubernetes 或 Podman 集成。

## 用法
### 安装
1. 在支持的 Linux 发行版上安装 Cockpit 包：
   - Fedora/RHEL/CentOS：`sudo dnf install cockpit` 或 `sudo yum install cockpit`。
   - Ubuntu/Debian：`sudo apt install cockpit`。
2. 启用并启动服务：`sudo systemctl enable --now cockpit.socket`。
3. 对于额外功能，安装特定包，如 `sudo dnf install cockpit-machines`（虚拟机管理）或 `sudo dnf install cockpit-podman`（容器管理）。

### 访问与使用
1. **浏览器访问**：在服务器主机或远程机器的浏览器中打开 `https://<服务器IP>:9090`（默认端口 9090）。首次访问需接受自签名证书。
2. **登录**：使用系统用户凭证登录（支持 PAM 认证）。推荐使用有 sudo 权限的用户。
3. **界面导航**：
   - 左侧菜单选择模块，如 “System” 查看概述、“Networking” 配置网络。
   - 使用搜索栏快速查找功能。
   - 添加服务器：点击 “Add server” 输入主机名/IP 和凭证，实现多机管理。
4. **示例操作**：
   - 更新软件：转到 “Software” 模块，点击 “Updates” 检查并应用更新。
   - 管理虚拟机：安装 cockpit-machines 后，转到 “Virtual Machines” 创建新 VM。
   - 监控日志：转到 “Logs” 过滤错误日志。
5. **高级用法**：
   - 通过 API 或 WebSocket 集成自定义脚本。
   - 配置 HTTPS：使用 Let's Encrypt 或自定义证书替换默认自签名证书。
   - 故障排除：检查 `/var/log/cockpit/` 日志，或使用 `cockpit-bridge` 调试。

Cockpit 适合系统管理员快速诊断和配置服务器，无需命令行操作。更多详情参考官方文档。