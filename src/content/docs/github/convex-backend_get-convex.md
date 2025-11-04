
---
title: convex-backend
---


# Convex Backend (get-convex/convex-backend)

项目地址: https://github.com/get-convex/convex-backend  
文件路径: `src/content/docs/00/convex-backend_get-convex.md`

---

## 👋 简介

**Convex Backend** 是一个基于 [Convex](https://convex.dev) 的示例后端项目，用来展示如何利用 Convex 的现代数据平台快速构建 Serverless 应用。它集成了身份认证、实时数据库操作、事务处理、REST/GraphQL 接口以及自动部署等功能，为快速迭代和原型开发提供了一站式解决方案。

---

## ⚙️ 核心特性

| 特性 | 说明 |
|------|------|
| **无服务器架构** | 代码自动按需扩展，无需维护传统服务器。 |
| **Convex 数据模型** | 灵活的声明式模式，支持事务、索引与权限控制。 |
| **身份认证** | 支持 JWT、Google Sign‑In、GitHub OAuth 等账号方式。 |
| **实时订阅** | 通过 `watch` API 实时推送数据变化，适合聊天、协同编辑等场景。 |
| **自动化部署** | 一键推送到 Convex Cloud，支持 CI/CD 集成。 |
| **事务与并发控制** | Convex 内置乐观并发策略，避免因冲突导致的数据不一致。 |
| **安全 ACL** | 通过 `convex auth` 配置资源访问策略。 |
| **日志与监控** | 集成 Convex Metrics 与 Tracing，帮助排查性能瓶颈。 |
| **类型安全** | TypeScript + Convex Client 库，减少运行时错误。 |

---

## 📦 主要目录结构

```
├─ src/
│   ├─ db/          # Convex 数据模型与 API
│   │   ├─ objects.ts  # 数据表定义
│   │   └─ index.ts    # 聚合所有 API 操作
│   ├─ auth/        # 身份验证相关逻辑
│   └─ utils/       # 工具函数
├─ convex/          # Convex 配置文件
├─ .env.example     # 环境变量示例
└─ README.md
```

---

## 🚀 快速开始

### 1️⃣ 克隆仓库

```bash
git clone https://github.com/get-convex/convex-backend.git
cd convex-backend
```

### 2️⃣ 安装依赖

```bash
# 推荐使用 pnpm
pnpm install
```

### 3️⃣ 配置环境

1. 复制 `.env.example` 为 `.env` 并填写凭证。  
   需在 Convex 控制台创建项目后获得 `PROJECT_ID` 与 `API_SECRET`。

```env
# .env
CONVEX_PROJECT_ID=xxxxxxxxxxxx
CONVEX_API_SECRET=xxxxxxxxxxxx
AUTH_SECRET=super-secret-phrase
PORT=5173
```

> ⚠️ **安全提示**：不要将 `.env` 直接提交到公共仓库。

### 4️⃣ 运行本地开发服务器

```bash
pnpm dev
```

访问 `http://localhost:5173` 即可看到 Convex 后台控制台。

### 5️⃣ 部署到 Convex Cloud

```bash
# 登录 Convex
convex login

# 推送代码
convex publish
```

部署完成后，你将获得一个唯一的部署 URL。

---

## 🛠️ 主要 API 说明

```ts
// src/db/index.ts
export const createPost = async ({ content, authorId }) => { ... }
export const getPosts = async () => { ... }
export const deletePost = async ({ postId }) => { ... }
export const subscribePosts = async (onChange) => { ... }
```

- **createPost**：创建新的帖子的服务器函数。  
- **getPosts**：读取所有帖子的查询函数。  
- **deletePost**：删除指定帖子。  
- **subscribePosts**：实时订阅帖子列表变化（客户端使用 `convex.subscribe`）。

---

## 📚 文档与学习资源

- **Convex 官方文档**：<https://docs.convex.dev>  
- **示例项目**：> [Convex Starter](https://github.com/convex-io/convex-example)  
- **关于 Auth**：<https://docs.convex.dev/auth>  

---

## 📎 联系与支持

- Issue 跟踪：<https://github.com/get-convex/convex-backend/issues>  
- 贡献指南：<https://github.com/get-convex/convex-backend/blob/main/CONTRIBUTING.md>

祝你使用愉快， 🚀
