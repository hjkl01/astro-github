
---
title: overleaf
---


# Overleaf（开源版）

> 项目地址: https://github.com/overleaf/overleaf

## 主要特性
- **实时协作**：多人可同时编辑同一 LaTeX 文档，编辑过程即时同步。
- **版本控制**：内置 Git 集成，支持提交、分支、合并和回滚。
- **即时预览**：支持 PDF、DVI、PS 等多种输出格式的实时渲染。
- **丰富的模板库**：提供多种学术、会议、期刊模板，快速启动项目。
- **插件与扩展**：支持 MathJax、ChemJax、Citeproc 等插件，满足高阶排版需求。
- **可扩展架构**：后端基于 Node.js + Express，前端使用 React，易于自定义插件。

## 功能概览
| 功能 | 说明 |
|------|------|
| **项目管理** | 创建、删除、共享项目，设置访问权限。 |
| **文件浏览** | 树形文件结构，支持上传、下载、重命名、删除。 |
| **编辑器** | 支持语法高亮、自动补全、行号、折叠、搜索。 |
| **编译系统** | 支持多种 TeX 发行版（TeX Live、MiKTeX 等），可配置编译选项。 |
| **协作** | 通过 WebSocket 实时同步编辑内容，显示其他协作者光标。 |
| **导出** | PDF、HTML、LaTeX 源文件、BibTeX 等格式导出。 |
| **Git 集成** | 自动推送到远程仓库，支持 pull、push、merge。 |
| **用户管理** | 单点登录（SSO）、OAuth、LDAP、SAML 等认证方式。 |

## 快速上手

### 1. 环境准备
```bash
# 需要 Node.js 18+、Docker、Docker Compose
```

### 2. 克隆仓库
```bash
git clone https://github.com/overleaf/overleaf.git
cd overleaf
```

### 3. 配置环境变量
复制示例文件并根据需求修改：
```bash
cp .env.example .env
```
常见变量：
- `OVERLEAF_DOMAIN` – 站点域名
- `MONGO_URI` – MongoDB 连接字符串
- `REDIS_URL` – Redis 连接字符串
- `SMTP_*` – 邮件服务配置

### 4. 启动服务
```bash
# 使用 Docker Compose 一键启动
docker-compose up -d
```
或直接 Node 方式：
```bash
npm install
npm run start:dev
```

### 5. 访问
浏览器打开 `http://localhost:3000`，使用 GitHub / Google / 电子邮件等方式注册或登录。

### 6. 创建项目
- 登录后点击 “New Project”。
- 选择模板或空白项目。
- 在左侧文件树中添加 `.tex` 文件，右侧编辑器实时预览。

### 7. Git 操作
```bash
# 在项目根目录
git init
git remote add origin <your-repo-url>
git add .
git commit -m "initial commit"
git push -u origin master
```
在 Overleaf UI 中可直接 “Push to Git” 或 “Pull from Git”。

### 8. 自定义插件
在 `packages/server/src/plugins` 目录下编写插件，重新编译后即可使用。

## 贡献与社区
- Issues & Pull Requests：欢迎提交 bug 报告和功能改进。
- 官方文档：查看 `docs/` 目录。
- 社区支持：Slack/Discord 频道、GitHub Discussions。

---

> 以上内容为 Overleaf 开源版的核心功能与使用概览，更多细节请参考官方 README 与文档。
