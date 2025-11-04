
---
title: kit
---


# SvelteKit 项目简介

- **项目地址**：<https://github.com/sveltejs/kit>

## 核心特性

| 特性 | 说明 |
|------|------|
| **文件系统路由** | 通过 `src/routes` 目录自动生成路由，支持布局层与布局文件（`+layout.svelte`）以及路由层级。 |
| **端到端渲染** | 支持 SSR、CSR、Svelte 组件化，构建时可选择性渲染。 |
| **模块化数据请求** | `+page.server.ts`/`+page.ts` 中可直接编写服务器端 or 客户端的数据获取逻辑。 |
| **预加载（Loaders）** | `load()` 函数支持在页面渲染前预取数据，返回嵌套子组件共享的数据。 |
| **API 路由** | 在 `src/routes/api` 下创建 `+.ts` 或 `+.js` 文件即可生成 /api/* 的 RESTful 接口。 |
| **静态站点生成（SSG）** | 通过 `adapter-static` 把 SvelteKit 迁移为预渲染站点。 |
| **适配器生态** | `adapter-node`、`adapter-vercel`、`adapter-cloudflare` 等，支持多处部署。 |
| **中间件（Middleware）** | 通过 `src/hooks.server.ts` 或 `src/middleware.ts` 编写请求拦截、身份验证等逻辑。 |
| **全局状态管理** | 可与 Svelte 的 `stores` 结合，也能方便集成 Redux、Zustand 等第三方库。 |
| **集成 TypeScript** | 默认 TypeScript 支持，配置简单。 |
| **ESLint、Prettier 与 Husky** | 开箱即用的 lint / 代码格式化与 git 钩子。 |
| **热重载（HMR）** | 开发时修改页面即可即时刷新。 |
| **SSR 与 CSR 混合** | 可针对不同页面选择渲染方式。 |
| **i18n 与 SEO** | 通过自定义 `head()` 函数与 `lang` 目录支持多语言与 SEO 优化。 |

## 安装与启动

```bash
# 1. 创建项目
npm create svelte@latest my-sveltekit-app
cd my-sveltekit-app

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run dev
```

> `npm run dev` 生成的应用可在 <http://localhost:5173> 访问。

## 目录结构

```
my-sveltekit-app/
├─ src/
│  ├─ routes/          # 路由文件夹，+page.svelte、+layout.svelte 等
│  ├─ lib/             # 共享组件与逻辑
│  ├─ hooks.server.ts  # 服务端钩子
│  ├─ app.html         # 页头模板
│  └─ routes/api/      # API 路由
├─ static/              # 静态文件
├─ svelte.config.js     # SvelteKit 配置
├─ package.json
└─ vite.config.js      # Vite 配置
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动开发服务器（热重载） |
| `npm run build` | 生成生产构建文件 |
| `npm run preview` | 本地预览构建产物 |
| `npm run format` | 代码格式化（Prettier） |
| `npm run lint` | 代码检查（ESLint） |

## 发布与部署

1. 选择合适的 Adapter（例如 `adapter-node`、`adapter-vercel` 等）。  
2. 在 `svelte.config.js` 配置对应 Adapter。  
3. 运行 `npm run build` 生成输出文件。  
4. 将 `build` 目录部署到服务器或对应云平台。

---

**总结**  
SvelteKit 是一个全栈框架，结合了 Svelte 的高效组件化与现代化的 web 开发特性，支持路由、SSR、API、静态站点生成、插件生态，一站式满足 SPA、SSR、静态站点与后端服务的集成开发需求。