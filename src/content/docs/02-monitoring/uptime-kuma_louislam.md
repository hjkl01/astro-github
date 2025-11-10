---
title: uptime-kuma
---

# Uptime Kuma 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/louislam/uptime-kuma)

## 主要特性
Uptime Kuma 是一个免费开源的自托管监控工具，用于跟踪网站、服务器、API 和其他服务的可用性和响应时间。主要特性包括：
- **多协议支持**：监控 HTTP(s)、TCP、Ping、DNS 记录等多种协议，支持自定义端口和路径。
- **通知集成**：内置多种通知方式，如 Telegram、Discord、Slack、Email、Pushover 等，支持 webhook 自定义通知。
- **仪表板和可视化**：提供现代化的 Web 界面，支持仪表板自定义、图表显示 uptime 历史数据、响应时间统计和维护模式。
- **多站点监控**：可以同时监控多个站点，支持分组管理、标签和证书到期提醒。
- **易于部署**：支持 Docker、Node.js 一键安装，轻量级设计，资源占用低。
- **高级功能**：心跳监控（Heartbeat）、代理支持、地理位置监控、SLA 计算，以及开源社区贡献的扩展。

## 功能
- **状态监控**：实时检查服务是否在线，记录 downtime 和 uptime 百分比。
- **警报系统**：当服务中断时立即发送通知，支持阈值设置（如响应时间超过阈值）。
- **历史数据**：存储监控日志，支持导出数据、设置数据保留期。
- **用户管理**：支持多用户登录、权限控制（仅限开源版需手动配置）。
- **移动友好**：响应式设计，适用于手机和桌面端访问。
- **扩展性**：通过插件或 API 集成其他工具，如 Prometheus 或 Grafana。

## 用法
1. **安装**：
   - **Docker 方式**（推荐）：运行命令 `docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:1`。访问 `http://你的IP:3001`。
   - **Node.js 方式**：克隆仓库 `git clone https://github.com/louislam/uptime-kuma.git`，安装依赖 `npm run setup`，启动 `npm run start-server`。
   - 详细安装指南见项目 README。

2. **基本使用**：
   - 打开 Web 界面，登录（默认无密码，首次使用设置）。
   - 点击“添加新监视器”，选择类型（如 HTTP），输入 URL 或 IP，设置检查间隔（默认 60 秒）。
   - 配置通知：在“设置 > 通知”中添加服务（如 Telegram Bot），然后在监视器中启用通知。
   - 查看仪表板：监控列表显示状态、响应时间和历史图表；支持拖拽排序和分组。

3. **高级用法**：
   - **心跳监控**：服务端发送心跳到 Uptime Kuma，避免单向检查失败。
   - **维护模式**：临时禁用监控以避免误报。
   - **API 集成**：使用 REST API 添加/删除监视器，支持自动化脚本。
   - 更新：Docker 拉取最新镜像；Node.js 运行 `git pull` 后重启。

Uptime Kuma 适合个人开发者、运维团队用于简单可靠的监控，无需复杂配置。