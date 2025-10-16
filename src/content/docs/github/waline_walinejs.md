
---
title: waline
---

# Waline 项目

## 项目地址
[GitHub 项目地址](https://github.com/walinejs/waline)

## 主要特性
Waline 是一个现代化的、非托管的评论系统，专为静态网站设计。它具有以下核心特性：
- **轻量级与高效**：基于 Node.js 构建，支持快速部署和低资源消耗。
- **自托管**：用户可以完全控制数据，无需依赖第三方服务，确保隐私和安全性。
- **多平台支持**：兼容多种静态站点生成器，如 Next.js、Hugo、Jekyll 等。
- **国际化支持**：内置多语言支持，包括简体中文、英文等。
- **用户友好**：提供登录、点赞、回复、嵌套评论等功能，支持 Markdown 渲染。
- **扩展性强**：集成 TeX 数学公式、表情包、图片上传等高级功能。
- **SEO 友好**：评论数据可作为 JSON-LD 结构化数据，提升搜索引擎优化。

## 主要功能
Waline 提供丰富的功能模块，包括：
- **评论管理**：支持实时评论、嵌套回复、@提及用户和通知机制。
- **用户认证**：集成 OAuth 登录（如 GitHub、Google），或匿名评论模式。
- **内容渲染**：自动解析 Markdown，支持代码高亮、LaTeX 公式和自定义表情。
- **数据统计**：内置访客计数、评论统计和页面浏览量追踪。
- **管理员面板**：Web 界面用于管理评论、用户和站点配置。
- **API 接口**：RESTful API 允许自定义集成和扩展。
- **搜索与过滤**：支持评论搜索、审核和垃圾评论过滤。

## 用法指南
### 1. 安装与部署
- **前提**：Node.js ≥ 14.0.0，MySQL/PostgreSQL/MongoDB 等数据库（推荐 Vercel 或自建服务器部署）。
- **快速启动**：
  1. 克隆仓库：`git clone https://github.com/walinejs/waline.git`
  2. 安装依赖：`cd waline && npm install`
  3. 配置环境：复制 `.env.example` 为 `.env`，编辑数据库连接和站点 URL。
  4. 运行开发模式：`npm run dev`
  5. 构建生产环境：`npm run build` 并启动服务器 `npm start`。

### 2. 集成到网站
- **JS SDK 集成**（客户端）：
  ```html
  <div id="waline"></div>
  <script type="module">
    import { init } from 'https://unpkg.com/@waline/client@v2/dist/waline.js';
    init({
      el: '#waline',
      serverURL: 'https://your-waline-server.com',
      path: window.location.pathname,
    });
  </script>
  ```
- **服务器端配置**：在 Waline 管理面板设置站点、启用插件（如腾讯云 OSS 上传）。

### 3. 高级用法
- **自定义主题**：修改 CSS 或使用主题变量调整外观。
- **插件扩展**：安装社区插件，如点击分析或邮件通知。
- **迁移数据**：支持从 Disqus 或其他系统导入评论。
- **文档参考**：详见 [官方文档](https://waline.js.org/)，包括 API 参考和故障排除。

Waline 适合博客、文档站点等场景，提供简单易用的评论解决方案。