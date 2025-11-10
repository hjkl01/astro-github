---
title: gatsby
---


# Gatsby - 一个基于 React 的静态站点生成器

**GitHub 地址**: https://github.com/gatsbyjs/gatsby

## 项目概述
Gatsby 是一个开源的、基于 React 的静态站生成器（Static Site Generator，SSG）。它利用 GraphQL 做为数据层，支持多来源（Markdown、CMS、数据库等）的内容聚合，并通过 Webpack 和 Babel 进行构建。Gatsby 的目标是让构建高性能、可扩展、易维护的现代网站变得简单。

## 主要特性

| 特性 | 说明 |
|------|------|
| **静态优先** | 在构建阶段把页面预渲染为静态 HTML，几乎无需服务器渲染，提升首屏加载速度。 |
| **React + Hooks** | 采用 React 生态，可使用所有官方组件、第三方库及 React Hooks。 |
| **GraphQL 数据层** | 统一查询接口，支持多来源数据，查询转换为组件 props。 |
| **插件系统** | 海量官方与社区插件可快速集成 Markdown、CMS（Contentful、DatoCMS）、SEO、PWA、图片优化等功能。 |
| **构建与部署** | 与 Netlify、Vercel、Firebase 等静态托管平台无缝集成，支持 CI/CD。 |
| **图片优化** | `gatsby-image` 自动生成多分辨率图像、懒加载、Blur-up 占位，提升性能。 |
| **代码拆分 & 按需加载** | 每页仅加载所需的 JS，进一步缩小 bundle。 |
| **Progressive Web App (PWA)** | 支持 Service Worker、缓存策略、离线体验。 |
| **SEO 友好** | 服务器渲染、meta 自动注入、结构化数据支持。 |
| **易用的页面路由** | 基于文件系统的路由，`src/pages` 或 `src/templates` 自动生成。 |
| **TypeScript 支持** | 完整类型支持，配合 `gatsby-plugin-typescript`。 |
| **可视化构建状态** | 自动化构建进度监控与错误追踪。 |

## 典型功能

| 功能 | 示例 |
|------|------|
| **Markdown 博客** | 通过 `gatsby-transformer-remark` 读取 Markdown，使用 GraphQL 查询内容，渲染为 `src/templates/blog-page.js`。 |
| **Headless CMS** | 通过 `gatsby-source-contentful` 或 `gatsby-source-prismic` 拉取内容，随时更新。 |
| **多语言站点** | 利用 `gatsby-plugin-i18n` 或 `gatsby-plugin-intl` 实现翻译。 |
| **电商解决方案** | 与 Prismic、DatoCMS 或自建 REST API 集成，展示产品列表。 |
| **图像优化** | `gatsby-plugin-image` + `gatsby-plugin-sharp` 自动生成 WebP、懒加载。 |
| **离线博客** | `gatsby-plugin-offline` 与 Service Worker 配合，实现离线阅读。 |
| **分析与监控** | `gatsby-plugin-analytics` 集成 Google Analytics、Segment。 |
| **自定义搜索** | 通过 `search-with-react` 或自建 Algolia 结合 `gatsby-plugin-algolia`。 |

## 快速开始

```bash
# 1. 安装 Node.js (>= 14)

# 2. 创建 Gatsby 项目
npx gatsby new my-gatsby-site https://github.com/gatsbyjs/gatsby-starter-blog

# 3. 进入项目目录
cd my-gatsby-site

# 4. 启动开发服务器
gatsby develop
# 或者
npm run develop

# 5. 打开浏览器访问 http://localhost:8000
```

### 常用 CLI 命令

| 命令 | 作用 |
|------|------|
| `gatsby develop` | 启动本地开发服务器，热重载。 |
| `gatsby build` | 打包生成 `public/` 目录。 |
| `gatsby serve` | 本地预览已构建产物。 |
| `gatsby clean` | 删除 `.cache/` 与 `public/`，重建。 |

## 部署示例（Netlify）

1. 在 Netlify 里创建新站点，连接 GitHub 仓库。
2. 设置构建命令为 `gatsby build`，发布目录为 `public/`。
3. Netlify 自动触发 CI/CD。

Netlify 还支持即时预览、header 配置、环境变量等。

## 生态与社区

- 官方插件列表: https://github.com/gatsbyjs/gatsby/tree/master/packages/gatsby-plugins
- 贡献者9000+ 开发者
- 讨论区: https://github.com/gatsbyjs/gatsby/discussions
- 视觉化: GraphiQL Playground (`http://localhost:8000/___graphql`)

## 进一步学习

- **官方文档**: https://www.gatsbyjs.com/docs/
- **教程**: https://www.gatsbyjs.com/docs/tutorial/
- **视频课程**: YouTube 上多位讲师分享完整项目实战

> 通过以上功能与特性，Gatsby 成为构建现代化网站、博客、文档站点、企业官网、PWA 等项目的一站式解决方案。祝你在使用过程中愉快 🚀

