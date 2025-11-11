---
title: Claudable
---

# Claudable

## 项目简介

Claudable 是一个开源的 Web 构建器，利用本地 CLI 代理（如 Claude Code、Cursor CLI 等）来轻松构建和部署产品。它结合了 Claude Code 的高级 AI 代理能力和 Lovable 的简单直观的应用构建体验。

## 主要功能

- **强大的代理性能**：利用 Claude Code 和 Cursor CLI Agent 的全部能力
- **自然语言转代码**：只需描述您想要构建的应用，Claudable 就会生成生产就绪的 Next.js 代码
- **即时预览**：通过热重载即时查看更改
- **零设置，即时启动**：无需复杂的沙箱、无需 API 密钥、无需数据库配置 - 立即开始构建
- **美观 UI**：使用 Tailwind CSS 和 shadcn/ui 生成美观的用户界面
- **部署到 Vercel**：一键将应用发布到生产环境，无需配置
- **GitHub 集成**：自动版本控制和持续部署设置
- **Supabase 数据库**：连接生产就绪的 PostgreSQL 数据库，认证功能已准备就绪
- **桌面应用**：作为 Electron 桌面应用程序提供，支持 Mac、Windows 和 Linux

## 支持的 AI 编码代理

Claudable 支持多种 AI 编码代理：

- **Claude Code**（推荐）：Anthropic 的高级 AI 编码代理
- **Codex CLI**：OpenAI 的强大编码代理
- **Cursor CLI**：强大的多模型 AI 代理
- **Qwen Code**：阿里巴巴的开源编码 CLI
- **Z.AI GLM-4.6**：智谱 AI 的编码代理

## 技术栈

- **前端**：Next.js、React、Tailwind CSS、shadcn/ui
- **数据库**：Supabase（PostgreSQL）
- **部署**：Vercel
- **桌面应用**：Electron

## 安装和使用

### 前置要求

- Node.js 18+
- Claude Code 或 Cursor CLI（已登录）
- Git

### 快速开始

1. 克隆仓库：

   ```bash
   git clone https://github.com/opactorai/Claudable.git
   cd Claudable
   ```

2. 安装依赖：

   ```bash
   npm install
   ```

3. 启动开发服务器：
   ```bash
   npm run dev
   ```

应用将在 http://localhost:3000 可用。

### 桌面应用

- 开发模式：`npm run dev:desktop`
- 构建桌面应用：`npm run build:desktop`
- 为特定平台打包：`npm run package:mac`、`npm run package:win`、`npm run package:linux`

## 使用指南

1. **连接 Claude Code**：将您的 Claude Code CLI 链接到 Claudable 以启用 AI 协助
2. **描述您的项目**：使用自然语言描述您想要构建的内容
3. **AI 生成**：观看 AI 生成您的项目结构和代码
4. **实时预览**：通过热重载功能即时查看更改
5. **部署**：使用 Vercel 集成推送到生产环境

## 集成设置

### GitHub

- 获取令牌：GitHub Personal Access Tokens → 生成新令牌（经典）→ 选择 `repo` 范围
- 连接：设置 → 服务集成 → GitHub → 输入令牌 → 创建或连接仓库

### Vercel

- 获取令牌：Vercel Account Settings → 创建令牌
- 连接：设置 → 服务集成 → Vercel → 输入令牌 → 创建新项目进行部署

### Supabase

- 获取凭据：Supabase Dashboard → 您的项目 → 设置 → API
- Project URL：`https://xxxxx.supabase.co`
- Anon Key：客户端公钥
- Service Role Key：服务端密钥

## 许可证

MIT License
