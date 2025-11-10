---
title: gotosocial
---

# GoToSocial 项目概述

## 项目地址
[https://github.com/superseriousbusiness/gotosocial](https://github.com/superseriousbusiness/gotosocial)

## 主要特性
GoToSocial 是一个开源的、轻量级的 ActivityPub 服务器实现，专注于联邦社交网络协议。它是 Mastodon 等平台的兼容替代品，但设计更注重效率和隐私。主要特性包括：
- **ActivityPub 兼容**：支持 Fediverse 生态，与 Mastodon、Pleroma 等平台无缝交互，实现跨服务器的帖子、关注和互动。
- **轻量级部署**：资源消耗低，适合个人或小型社区运行，支持 Docker 和二进制安装，无需复杂数据库。
- **隐私优先**：强调用户数据控制，提供端到端加密选项和最小化数据收集。
- **联邦功能**：支持帖子发布、时间线、通知、媒体附件和轮廓自定义。
- **可扩展性**：模块化架构，便于开发者扩展插件或自定义行为。
- **开源许可**：采用 AGPL-3.0 许可，社区驱动开发。

## 主要功能
- **用户管理**：注册、登录、账户设置，包括用户名、头像、简介和隐私设置。
- **内容发布**：创建文本帖子、分享链接、上传图片/视频，支持标签、提及和内容警告。
- **社交互动**：关注/取关用户、点赞、转发、回复，形成动态时间线和通知系统。
- **联邦通信**：自动处理与其他服务器的互动，如接收远程帖子或同步账户状态。
- **管理工具**：管理员面板用于服务器配置、用户审核和内容审核。
- **API 支持**：提供 RESTful API，兼容 Mastodon API，允许第三方客户端连接。

## 用法
### 安装
1. **前提条件**：确保系统有 Go 1.19+ 或使用 Docker。需要 PostgreSQL 或 SQLite 数据库。
2. **Docker 方式**（推荐新手）：
   ```
   docker run -d -p 8080:8080 -v $HOME/gts:/var/lib/gotosocial superseriousbusiness/gotosocial:latest
   ```
   编辑 `config.yaml` 文件配置数据库、主机名等。
3. **二进制安装**：
   - 下载预编译二进制：从 GitHub Releases 获取。
   - 运行 `./gotosocial server` 启动服务器。
   - 配置：使用 `gotosocial admin account create` 创建管理员账户。

### 基本使用
1. **启动服务器**：运行后，访问 `https://your-domain.com` 注册账户。
2. **发布内容**：登录后，点击“撰写”按钮创建帖子，支持 Markdown 格式和附件。
3. **联邦互动**：搜索 `@username@other-server.com` 关注远程用户，帖子将自动联邦。
4. **客户端集成**：使用 Mastodon 兼容客户端如 Tusky 或 Elk，通过 API 连接。
5. **管理**：管理员登录 `/admin` 面板，监控活动和配置设置（如速率限制、主题）。

更多细节参考官方文档：https://docs.gotosocial.org。