
---
title: operating-system
---


# Home Assistant Operating System

**项目地址**：<https://github.com/home-assistant/operating-system>

## 简介
Home Assistant Operating System（简称 HassOS）是 Home Assistant 官方提供的全栈、轻量级操作系统，专门为 Home Assistant 的运行环境设计。它基于 Linux，包含 Docker、Supervisor、Home Assistant Core 等组件，能够在多种硬件平台（如 Raspberry Pi、Intel NUC、虚拟机等）上以一键方式部署。

## 主要特性
- **一键安装**：支持多种硬件架构（armhf、arm64、amd64）通过官方映像文件快速安装。
- **自带 Docker & Supervisor**：内置 Docker 引擎与 Home Assistant Supervisor，简化容器管理与插件安装。
- **固件更新**：Supervisor 自动检测并安全升级系统、核心与插件，支持 OTA 更新。
- **安全性**：使用官方安全更新，支持 SELinux/AppArmor 等安全策略。
- **网络集成**：内置 MQTT、NTP、DHCP、DNS 等网络服务，方便与网络设备交互。
- **多平台支持**：可在 Raspberry Pi、Intel NUC、VirtualBox、VMware、QEMU、Docker 容器等多种环境中运行。

## 功能概览
| 功能 | 说明 |
|------|------|
| **Home Assistant Core** | 核心业务逻辑，负责自动化、界面与集成。 |
| **Supervisor** | 管理 Home Assistant Core 与插件，提供 Web UI、日志、更新等。 |
| **Add-ons** | 通过 Supervisor 安装社区插件（如 Mosquitto、InfluxDB 等）。 |
| **Docker** | 通过 Supervisor 运行容器化服务，支持自定义镜像。 |
| **OTA 更新** | 自动检测并更新系统、核心与插件，保持安全与功能更新。 |
| **日志与监控** | 集成日志收集、系统监控与告警，支持 Grafana、Prometheus 等。 |

## 用法

### 1. 下载映像
1. 访问项目 Releases 页面，下载对应硬件架构的 `.img.xz` 镜像文件（如 `hassos_rpi_64.img.xz`）。  
2. 解压后得到 `hassos.img`。

### 2. 写入 SD 卡或磁盘
- **Raspberry Pi**  
  ```bash
  sudo dd if=hassos.img of=/dev/sdX bs=4M status=progress && sync
  ```
- **Intel NUC / 其他 x86**  
  使用磁盘工具将镜像写入硬盘，或直接通过 USB 启动。

### 3. 启动与初始设置
1. 将 SD 卡/硬盘插入设备，连接电源。  
2. 通过浏览器访问 `http://homeassistant.local:8123`（或使用设备 IP）。  
3. 按照向导完成 Home Assistant 配置，创建管理员账户。

### 4. 通过 Supervisor 管理
- **安装 Add-on**：在 Supervisor UI → Add-on Store → 选择插件 → Install → Start。  
- **更新系统**：Supervisor UI → System → Update，或使用 `hassio homeassistant update` CLI。  
- **备份/恢复**：Supervisor UI → Snapshots → Create / Restore。

### 5. 高级使用
- **自定义 Docker Compose**：在 `docker/` 目录可放置自定义 `docker-compose.yaml`，Supervisor 会读取。  
- **SSH 访问**：启用 SSH Add-on，使用 `ssh root@<IP>` 登录。  
- **远程访问**：通过 Home Assistant Cloud 或配置 `ssl` 与 `api_password` 实现安全远程管理。

## 结语
Home Assistant Operating System 为智能家居爱好者提供了一站式、可维护的运行环境。其一键安装、自动更新和丰富的插件生态，使得从新手到专业用户都能轻松上手并扩展功能。  

**项目地址**：<https://github.com/home-assistant/operating-system>
