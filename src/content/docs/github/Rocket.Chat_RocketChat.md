
---
title: Rocket.Chat
---

# Rocket.Chat 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/RocketChat/Rocket.Chat)

## 主要特性
Rocket.Chat 是一个开源的团队协作和通信平台，类似于 Slack 或 Microsoft Teams。它提供了一个安全的、可自托管的聊天解决方案，支持实时消息、视频通话和文件共享。主要特性包括：
- **实时聊天**：支持一对一、私聊、群组聊天和频道讨论。
- **多媒体支持**：集成视频/音频通话、屏幕共享、文件上传和表情包。
- **安全性**：端到端加密、两因素认证（2FA）、角色-based 访问控制（RBAC）和数据导出功能，确保合规（如 GDPR、HIPAA）。
- **集成与扩展**：支持与 GitHub、Jira、Zapier 等工具集成；内置 API 和插件系统，便于自定义。
- **移动与桌面支持**：跨平台应用（iOS、Android、Web、桌面客户端），支持推送通知。
- **企业级功能**：如 Omnichannel 支持（客服系统）、LDAP/Active Directory 集成和白标定制。
- **开源与社区驱动**：基于 Node.js 和 React 构建，MIT 许可，活跃社区贡献。

## 主要功能
- **消息管理**：发送文本、图片、视频；支持消息编辑、删除、搜索和线程回复。
- **用户与组织管理**：用户邀请、角色分配、部门结构和访客访问。
- **通知与协作**：@提及、在线状态、任务提醒和集成机器人（bots）。
- **分析与报告**：内置仪表盘，监控用户活动和聊天统计。
- **部署选项**：支持 Docker、Kubernetes 和云部署（如 AWS、Azure）。

## 用法
1. **安装与部署**：
   - 克隆仓库：`git clone https://github.com/RocketChat/Rocket.Chat.git`。
   - 使用 Docker 快速启动：运行 `docker run -p 3000:3000 rocketchat/rocket.chat`（需配置 MongoDB）。
   - 详细安装指南见 [官方文档](https://docs.rocket.chat/)，支持 Ubuntu、CentOS 等系统。

2. **基本使用**：
   - 访问 Web 界面（默认 http://localhost:3000），注册管理员账户。
   - 创建频道：点击 "+" 创建公共/私有频道，邀请成员。
   - 发送消息：选择频道输入文本，支持 Markdown 格式化。
   - 集成应用：通过设置 > 集成 添加外部服务。
   - 移动端：从 App Store/Google Play 下载 Rocket.Chat 应用，登录服务器 URL。

3. **高级用法**：
   - 自定义主题：编辑 `settings.json` 配置 UI 和功能。
   - 开发扩展：使用 JavaScript SDK 构建自定义应用或机器人。
   - 自托管管理：通过 MongoDB 备份数据，使用 Nginx 反向代理优化性能。

项目适合企业、社区或个人用于构建私有聊天系统，社区版免费，企业版提供额外支持。