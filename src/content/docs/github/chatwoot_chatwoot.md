
---
title: chatwoot
---

# Chatwoot 项目

## 项目地址
[GitHub 项目地址](https://github.com/chatwoot/chatwoot)

## 主要特性
Chatwoot 是一个开源的客户支持平台，旨在帮助团队通过多种渠道（如网站聊天、电子邮件、社交媒体等）高效管理客户互动。它采用现代化的 Ruby on Rails 框架构建，支持自托管部署，具有高度的可扩展性和自定义性。主要特性包括：
- **多渠道支持**：集成网站实时聊天、Facebook Messenger、Twitter、WhatsApp、电子邮件、SMS 等多种通信渠道，实现统一的管理界面。
- **实时协作**：团队成员可以实时查看和协作处理对话，支持共享对话、@提及和内部备注。
- **自动化功能**：内置聊天机器人支持、自动回复规则、对话路由和标签系统，帮助自动化常见查询。
- **报告与分析**：提供对话统计、代理绩效报告、CSAT（客户满意度）调查等分析工具，帮助优化支持流程。
- **安全与合规**：支持数据加密、GDPR 合规、角色-based 访问控制（RBAC），确保客户数据安全。
- **移动端支持**：提供 iOS 和 Android 移动应用，允许代理随时随地响应客户。
- **集成扩展**：易于与其他工具集成，如 Slack、Zendesk、Intercom 等，通过 API 和 Webhooks 实现无缝连接。
- **开源与社区驱动**：免费开源（MIT 许可），活跃社区贡献，支持自定义插件和主题。

## 主要功能
- **对话管理**：集中式仪表板显示所有客户对话，支持搜索、过滤和归档。
- **代理工具**：每个代理有个性化仪表板，包括分配对话、响应模板和快捷回复。
- **客户档案**：自动构建客户历史记录，包括过去互动、标签和自定义属性。
- **知识库集成**：内置或外部知识库支持，帮助代理快速查找答案。
- **AI 增强**：可选集成 AI 工具，如自动分类对话或生成回复草稿。
- **自定义工作流**：通过规则引擎设置触发器，例如基于关键词路由对话到特定代理。

## 用法
1. **安装与部署**：
   - **前提条件**：需要 Ruby 2.7+、Node.js 14+、PostgreSQL 12+ 和 Redis。推荐使用 Docker 进行简单部署。
   - **从 GitHub 克隆**：`git clone https://github.com/chatwoot/chatwoot.git`，然后运行 `bundle install` 和 `yarn install`。
   - **Docker 部署**：使用官方 Docker Compose 文件，一键启动：`docker-compose up -d`。详细指南见 [官方文档](https://www.chatwoot.com/docs/self-hosted/deployment/docker)。
   - **云部署**：支持 Heroku、DigitalOcean 等平台，或使用 Chatwoot 的托管服务。

2. **配置**：
   - 编辑 `config/settings.yml` 文件设置数据库、邮件服务器和渠道集成。
   - 运行数据库迁移：`rails db:migrate` 和 `rails db:seed`。
   - 通过 Web 界面（localhost:3000）创建管理员账户并配置渠道（如添加 Facebook App ID）。

3. **日常使用**：
   - **添加网站小部件**：生成 JavaScript 代码嵌入网站，实现实时聊天。
   - **设置渠道**：在仪表板中连接社交媒体账户或电子邮件 inbox。
   - **管理团队**：邀请代理，分配角色和权限。
   - **处理对话**：登录代理仪表板，响应消息、使用模板或转移对话。
   - **监控与优化**：查看报告仪表板，调整规则以提高效率。

更多详细用法和 API 文档，请参考官方文档：https://www.chatwoot.com/docs。