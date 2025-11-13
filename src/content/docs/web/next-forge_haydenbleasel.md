---
title: next-forge
---

# Next Forge 项目

## 项目地址

[GitHub 项目地址](https://github.com/vercel/next-forge)

## 主要特性

Next Forge 是一个生产级的 Turborepo 模板，用于 Next.js 应用。它提供了一个全面的起点，用于构建 SaaS 应用，具有最小的配置要求。主要特性包括：

### 应用

- **Web**：使用 Tailwind CSS 和 TWBlocks 构建的营销网站
- **App**：具有认证和数据库集成的主应用
- **API**：具有健康检查和监控的 RESTful API
- **Docs**：由 Mintlify 驱动的文档网站
- **Email**：使用 React Email 的电子邮件模板
- **Storybook**：组件开发环境

### 包

- **认证**：由 Clerk 提供支持
- **数据库**：具有迁移的类型安全 ORM
- **设计系统**：具有暗模式的综合组件库
- **支付**：通过 Stripe 的订阅管理
- **电子邮件**：通过 Resend 的交易电子邮件
- **分析**：Web (Google Analytics) 和产品 (Posthog)
- **可观测性**：错误跟踪 (Sentry)、日志和正常运行时间监控 (BetterStack)
- **安全**：应用安全 (Arcjet)、速率限制和安全头
- **CMS**：博客和文档的类型安全内容管理
- **SEO**：元数据管理、站点地图和 JSON-LD
- **AI**：AI 集成工具
- **Webhooks**：入站和出站 webhook 处理
- **协作**：具有头像和实时光标的实时功能
- **功能标志**：功能标志管理
- **Cron**：计划作业管理
- **存储**：文件上传和管理
- **国际化**：多语言支持
- **通知**：应用内通知系统

## 主要功能

- **组件库**：预置 UI 组件，包括按钮、表单、模态框等，支持主题自定义。
- **路由管理**：使用 Next.js App Router 或 Pages Router，实现动态路由和嵌套布局。
- **数据获取**：集成 SWR 或 React Query，实现高效的数据缓存和实时更新。
- **构建工具**：支持 TypeScript、ESLint 和 Prettier，确保代码质量和类型安全。
- **部署友好**：一键部署到 Vercel 或其他平台，包含环境变量管理和 CI/CD 集成。

## 用法

### 先决条件

- Node.js 20+
- pnpm (或 npm/yarn/bun)
- Stripe CLI 用于本地 webhook 测试

### 安装

创建新的 next-forge 项目：

```
npx next-forge@latest init
```

### 设置

1. 配置环境变量
2. 设置所需的服务账户 (Clerk, Stripe, Resend 等)
3. 运行开发服务器

详细设置说明，请阅读 [文档](https://www.next-forge.com/docs)。

更多细节请参考 GitHub 仓库的 README 和 [文档](https://www.next-forge.com/docs)。
