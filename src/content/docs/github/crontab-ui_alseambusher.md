
---
title: crontab-ui
---

# Crontab-UI 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/alseambusher/crontab-ui)

## 主要特性
Crontab-UI 是一个基于 Web 的 cron 任务管理工具，主要特性包括：
- **可视化界面**：提供直观的 Web 界面来管理和监控 cron 任务，无需命令行操作。
- **任务调度**：支持标准 cron 表达式定义任务，支持分钟、小时、日、月、周等时间周期。
- **实时监控**：实时显示任务执行状态、日志输出和错误信息，便于调试。
- **用户友好**：内置 cron 表达式生成器，帮助用户轻松创建复杂调度规则。
- **轻量级**：基于 Node.js 开发，资源占用低，支持 Docker 部署。

## 主要功能
- **任务管理**：添加、编辑、删除 cron 任务，支持批量操作。
- **执行日志**：记录每个任务的执行历史、输出结果和运行时长。
- **权限控制**：支持多用户登录和任务权限分配（需配置）。
- **API 支持**：提供 RESTful API 接口，可集成到其他系统中。
- **通知集成**：可选集成邮件或 Slack 等通知服务，报告任务失败。
- **备份与恢复**：自动备份任务配置，支持一键恢复。

## 用法
1. **安装**：
   - 通过 npm 安装：`npm install -g crontab-ui`。
   - 或使用 Docker：`docker run -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock alseambusher/crontab-ui`。

2. **启动**：
   - 命令行启动：`crontab-ui`。
   - 默认访问地址：`http://localhost:8000`，初始用户名/密码为 `admin/admin`。

3. **使用步骤**：
   - 登录 Web 界面。
   - 点击“添加任务”，输入命令（如 `echo "Hello" >> /tmp/log.txt`）和 cron 表达式（如 `* * * * *` 表示每分钟执行）。
   - 保存后，任务将自动调度执行。
   - 在“任务列表”查看状态，在“日志”查看输出。
   - 编辑或删除任务时，系统会自动更新 crontab 文件。

注意：项目基于 Node.js 和 Express 框架，确保系统已安装 cron 服务。更多详情请参考 GitHub 仓库的 README。