
---
title: templates
---


# Cloudflare Templates

**项目地址**: <https://github.com/cloudflare/templates>

---

## 主要特性

- **多平台支持**  
  - Cloudflare Workers  
  - Cloudflare Pages  
  - Cloudflare Pages + Functions  
  - Cloudflare Pages + Functions + Edge  
- **示例丰富**  
  - 简单的 “Hello World”  
  - API 路由示例  
  - 静态站点与动态 API 结合  
  - 基于 Edge KV 的缓存示例  
  - 跨域资源共享 (CORS) 处理  
- **开箱即用**  
  - 已经配置好 `wrangler.toml`、`next.config.js` 等配置文件  
  - 支持 TypeScript 与 JavaScript 两种语言  
- **易于扩展**  
  - 目录结构清晰，便于自定义业务逻辑  
  - 通过 `wrangler dev` 本地调试与 `wrangler publish` 一键部署  

---

## 功能概览

| 功能 | 说明 |
|------|------|
| **Worker 模板** | 适用于需要快速启动 Cloudflare Worker 的项目，包含基本的请求处理与响应示例。 |
| **Pages 模板** | 支持纯静态站点与 Next.js SPA，配合 Cloudflare Pages 自动构建与部署。 |
| **Pages + Functions** | 结合 Cloudflare Pages 的静态资源与 Workers 的 API，适合需要 API 与前端同在一个域名下的项目。 |
| **Pages + Edge KV** | 在 Pages 项目中直接使用 Edge KV 进行缓存与数据存储，示例展示了如何读取与写入 KV。 |
| **CORS 示例** | 通过 Worker 实现跨域资源共享，演示如何配置 `Access-Control-Allow-Origin` 等头信息。 |

---

## 用法

### 1. 克隆仓库

```bash
git clone https://github.com/cloudflare/templates.git
cd templates
```

### 2. 选择模板

模板目录结构如下：

```
templates/
├─ cookie/
├─ hello/
├─ kv/
├─ pages/
├─ pages-functions/
├─ pages-functions-kv/
├─ pages-nextjs/
└─ ...
```

- 进入对应目录，例如 `pages-nextjs`：

```bash
cd pages-nextjs
```

### 3. 安装依赖

```bash
# 若为 Node.js 项目
npm install
# 或者
yarn install
```

### 4. 本地开发

- **Worker**：  
  ```bash
  wrangler dev
  ```
- **Pages / Next.js**：  
  ```bash
  npm run dev
  # 或者
  yarn dev
  ```

### 5. 部署

- **Worker**：  
  ```bash
  wrangler publish
  ```
- **Pages / Next.js**：  
  ```bash
  wrangler pages publish
  # 或者使用 Cloudflare Pages UI 直接连接 GitHub
  ```

### 6. 自定义

- 修改 `wrangler.toml` 或 `next.config.js`，根据业务需求调整配置。  
- 在 `src/` 或 `pages/` 目录下添加自定义业务逻辑。  
- 如需使用 Edge KV，先在 Cloudflare 控制台创建 KV 命名空间，然后在 `wrangler.toml` 中绑定。

---

## 参考文档

- [Cloudflare Workers 官方文档](https://developers.cloudflare.com/workers/)
- [Cloudflare Pages 官方文档](https://developers.cloudflare.com/pages/)
- [wrangler CLI 使用指南](https://developers.cloudflare.com/workers/cli-wrangler)

---

> 以上内容为快速上手 Cloudflare Templates 的核心信息，更多细节请参阅仓库内的 README 与官方文档。
