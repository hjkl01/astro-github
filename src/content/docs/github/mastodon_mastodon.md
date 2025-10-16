
---
title: mastodon
---

# Mastodon 项目

## 项目地址
[GitHub 项目地址](https://github.com/mastodon/mastodon)

## 主要特性
Mastodon 是一个开源的、去中心化的社交网络平台，基于 ActivityPub 协议构建。它允许用户在独立的服务器（称为“实例”）上运行和互动，形成一个联邦化的网络。核心特性包括：
- **去中心化与联邦化**：用户可以选择加入不同的 Mastodon 实例，这些实例之间可以互通，形成一个分布式社区，避免单一平台的控制。
- **隐私与控制**：用户拥有数据所有权，支持自定义隐私设置、内容警告和屏蔽功能。
- **开源与可扩展**：使用 Ruby on Rails 开发，支持插件和主题自定义，社区驱动开发。
- **多媒体支持**：内置图片、视频、GIF 和投票功能，支持最大 4 个附件。
- **实时互动**：通过 WebSocket 实现实时通知、时间线更新和聊天。
- **无广告**：纯净的用户体验，不依赖广告盈利。

## 主要功能
- **时间线与发布**：用户可以发布“嘶吼”（toots，类似于推文），支持文本、表情符号和多媒体。时间线包括首页、本地和联邦视图。
- **关注与互动**：关注用户、点赞、转发、回复和收藏。支持列表和收藏夹组织内容。
- **搜索与发现**：搜索用户、标签和内容，支持高级过滤。
- **管理工具**：管理员可以管理实例用户、 moderation 和备份。用户端有报告和屏蔽功能。
- **集成与 API**：提供 REST API 和 GraphQL，支持第三方客户端和自动化工具。
- **移动友好**：响应式设计，支持 PWA（渐进式 Web 应用），可作为移动 App 使用。

## 用法
### 安装与部署（针对服务器管理员）
1. **前提条件**：需要 Ruby 2.7+、Node.js 14+、PostgreSQL 9.5+、Redis 和 FFmpeg 等依赖。推荐使用 Ubuntu/Debian 系统。
2. **克隆仓库**：`git clone https://github.com/mastodon/mastodon.git`。
3. **安装依赖**：运行 `bundle install`（Ruby 包）和 `yarn install`（Node 包）。
4. **配置**：复制 `.env.production` 示例文件，编辑数据库、SMTP 和 Redis 设置。生成密钥：`rails secret` 和 `rails db:setup`。
5. **构建与启动**：`rails assets:precompile`、`rails db:migrate` 和 `rails server`。使用 Docker 或 systemd 服务生产部署。
6. **详细指南**：参考官方文档 [https://docs.joinmastodon.org/admin/install/](https://docs.joinmastodon.org/admin/install/)。

### 用户使用（针对普通用户）
1. **注册**：访问 Mastodon 实例（如 [mastodon.social](https://mastodon.social)），创建账户。每个实例有自己的规则和社区。
2. **发布内容**：在首页点击“发布”按钮，输入文本（最多 500 字符），添加媒体或标签（如 #开源），选择可见性（公开、仅关注者、仅提及或私密）。
3. **互动**：浏览时间线，点击用户关注；使用心形图标点赞、转发图标分享。
4. **探索**：使用搜索栏查找内容，或通过 Mastodon 的联邦搜索发现其他实例的用户。
5. **移动端**：添加实例到浏览器书签，或使用官方/第三方 App（如 Tusky for Android、Mastodon for iOS）。
6. **迁移账户**：支持从一个实例迁移到另一个，保留关注者和帖子。

更多详情请查看官方文档 [https://docs.joinmastodon.org/](https://docs.joinmastodon.org/)。