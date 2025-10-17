
---
title: nezha
---

# Nezha 项目

## 项目地址
[GitHub 项目地址](https://github.com/naiba/nezha)

## 主要特性
Nezha 是一个开源的服务器监控代理和仪表盘项目，专为 VPS 和服务器管理设计。它采用轻量级架构，支持多服务器监控，提供实时数据可视化。核心特性包括：
- **实时监控**：监控 CPU、内存、磁盘、网络流量、进程等系统资源。
- **多代理支持**：通过代理端部署在多个服务器上，实现集中管理。
- **仪表盘界面**：简洁的 Web 界面，支持主题切换和自定义配置。
- **通知功能**：集成推送通知（如 Telegram、Discord），在资源阈值异常时警报。
- **安全性**：支持 HTTPS、基本认证和 IP 白名单。
- **跨平台**：兼容 Linux、Windows 和 macOS，支持 Docker 部署。
- **开源免费**：基于 Go 语言开发，MIT 许可，社区活跃。

## 主要功能
- **系统监控**：实时显示服务器负载、温度、硬盘使用率等指标，支持历史数据图表。
- **进程管理**：监控特定进程（如 Nginx、MySQL），并提供重启或停止功能。
- **网络统计**：追踪带宽使用、连接数和 IP 流量。
- **自定义警报**：设置阈值（如 CPU > 80%）触发通知。
- **API 接口**：提供 RESTful API，便于集成到其他工具。
- **数据持久化**：使用 SQLite 存储数据，支持备份和恢复。

## 用法
### 1. 部署仪表盘（Dashboard）
- **要求**：Go 1.18+ 或 Docker。
- **从源代码部署**：
  1. 克隆仓库：`git clone https://github.com/naiba/nezha.git`
  2. 进入目录：`cd nezha`
  3. 构建：`go build -o nezha-dashboard ./dashboard`
  4. 配置：编辑 `config.yaml` 文件，设置端口、数据库路径等。
  5. 运行：`./nezha-dashboard`
- **Docker 部署**：
  ```
  docker run -d --name nezha-dashboard -p 80:80 -v /path/to/config:/etc/nezha naiba/nezha-dashboard
  ```
- 访问：浏览器打开 `http://your-server-ip:port`，默认用户名/密码为 `admin/admin`（首次登录后修改）。

### 2. 部署代理（Agent）
- 在每个需要监控的服务器上部署代理端。
- **从源代码部署**：
  1. 克隆仓库并构建：`go build -o nezha-agent ./agent`
  2. 配置：编辑 `config.yaml`，设置 Dashboard 地址、认证令牌（从 Dashboard 获取）。
  3. 运行：`./nezha-agent`
- **Docker 部署**：
  ```
  docker run -d --name nezha-agent -v /path/to/config:/etc/nezha naiba/nezha-agent
  ```
- 在 Dashboard 中添加代理：输入代理 ID 和令牌，即可看到监控数据。

### 3. 配置和使用
- **添加服务器**：在 Dashboard 的“代理”页面生成令牌，配置到 Agent。
- **设置警报**：在“设置”中定义通知渠道和阈值。
- **查看数据**：仪表盘首页显示所有服务器的实时状态，支持排序和过滤。
- **更新**：定期拉取最新代码并重新构建。

更多详情请参考项目 README 和 Wiki。