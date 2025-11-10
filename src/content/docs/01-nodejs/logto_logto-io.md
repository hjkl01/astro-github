---
title: logto
---

# Logto 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/logto-io/logto)

## 主要特性
Logto 是一个开源的身份验证和授权服务，旨在为现代应用程序提供简单、安全的身份管理解决方案。其核心特性包括：
- **开源且自托管**：完全开源，支持自托管部署，避免依赖第三方服务，确保数据隐私。
- **现代身份协议支持**：兼容 OIDC（OpenID Connect）、OAuth 2.0 和 SAML 等标准协议，便于集成各种应用。
- **多租户架构**：支持多租户模式，适合 SaaS 应用，每个租户可独立管理用户和权限。
- **密码less 认证**：支持无密码登录方式，如多因素认证（MFA）、社交登录（Google、GitHub 等）和一次性密码（OTP）。
- **角色与权限管理**：细粒度的 RBAC（基于角色的访问控制）和 ABAC（基于属性的访问控制），简化权限配置。
- **可扩展性**：模块化设计，支持自定义插件和钩子，易于扩展功能。
- **开发者友好**：提供 SDK 支持多种语言（如 JavaScript、Python 等），并有详细的 API 文档和控制台界面。

## 主要功能
Logto 的功能聚焦于身份验证、用户管理和安全控制，主要包括：
- **用户注册与登录**：支持电子邮件、手机号或社交账户注册，提供安全的登录流程。
- **会话管理**：处理用户会话、令牌颁发和刷新，确保安全注销和会话过期。
- **组织与团队管理**：内置组织结构，支持团队协作和权限分级。
- **审计日志**：记录所有认证事件，便于安全审计和合规。
- **集成工具**：内置控制台用于配置应用、用户和策略，支持 Web、移动和 API 集成。
- **安全特性**：防范常见攻击，如 CSRF、XSS，并支持 JWT 令牌签名。

## 用法指南
### 1. 安装与部署
- **前提条件**：Node.js（v16+）、Docker（可选，用于容器化部署）和数据库（如 PostgreSQL）。
- **快速启动**：
  1. 克隆仓库：`git clone https://github.com/logto-io/logto.git`
  2. 安装依赖：`cd logto && yarn install`
  3. 配置环境：复制 `.env.example` 为 `.env`，设置数据库连接等参数。
  4. 运行开发模式：`yarn dev`（启动控制台和 API 服务）。
- **生产部署**：使用 Docker Compose 或 Kubernetes 部署，支持云平台如 AWS、Azure。

### 2. 配置与使用
- **访问控制台**：部署后，访问 `http://localhost:3001`（默认端口），使用 admin 账户登录（初始凭证在文档中）。
- **创建应用**：在控制台中添加应用，选择协议（如 OIDC），配置重定向 URI。
- **集成到应用**：
  - 使用 Logto SDK：例如，在 JavaScript 项目中安装 `@logto/node`，初始化客户端：
    ```javascript
    import { LogtoClient } from '@logto/node';
    const client = new LogtoClient({
      endpoint: 'https://your-logto-endpoint',
      appId: 'your-app-id',
      appSecret: 'your-app-secret',
    });
    // 发起登录
    await client.signIn('https://your-app/callback');
    ```
  - 处理回调：验证令牌并获取用户信息。
- **用户管理**：通过控制台或 API 创建用户、分配角色。
- **高级用法**：自定义登录页面、使用钩子扩展行为，或集成 MFA。

更多详情请参考项目文档：[Logto 文档](https://docs.logto.io)。