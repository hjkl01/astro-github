---
title: chartdb
---

# ChartDB

[GitHub 项目地址](https://github.com/chartdb/chartdb)

## 项目简介

ChartDB 是一个开源的数据库图表编辑器，允许您通过单个查询来可视化和设计数据库。它无需安装、无需数据库密码即可使用。提供即时数据库模式导入、AI 驱动的导出以及交互式编辑功能。

## 状态

ChartDB 目前处于公开 Beta 阶段。关注此仓库以获取更新通知。

## 它做什么

- **即时模式导入**
  运行单个查询即可将数据库模式作为 JSON 即时检索。这使得可视化数据库模式变得非常快速，无论是用于文档、团队讨论还是更好地理解数据。

- **AI 驱动导出以便轻松迁移**
  我们的 AI 驱动导出功能允许您以目标数据库的方言生成 DDL 脚本。无论是从 MySQL 迁移到 PostgreSQL，还是从 SQLite 迁移到 MariaDB，ChartDB 都简化了流程，并提供了针对目标数据库定制的脚本。

- **交互式编辑**
  使用我们的直观编辑器微调数据库模式。轻松进行调整或注释，以更好地可视化复杂结构。

## 主要特性

- **即时模式导入**：运行单个查询即可将数据库模式作为 JSON 即时检索。这使得可视化数据库模式变得非常快速，无论是用于文档、团队讨论还是更好地理解数据。
- **AI 驱动导出**：我们的 AI 驱动导出功能允许您以目标数据库的方言生成 DDL 脚本。无论是从 MySQL 迁移到 PostgreSQL，还是从 SQLite 迁移到 MariaDB，ChartDB 都简化了流程，并提供了针对目标数据库定制的脚本。
- **交互式编辑**：使用我们的直观编辑器微调数据库模式。轻松进行调整或注释，以更好地可视化复杂结构。

## 支持的数据库

- ✅ PostgreSQL（包括 Supabase、Timescale）
- ✅ MySQL
- ✅ SQL Server
- ✅ MariaDB
- ✅ SQLite（包括 Cloudflare D1）
- ✅ CockroachDB
- ✅ ClickHouse

## 快速使用

### 安装

```bash
npm install
npm run dev
```

### 构建

```bash
npm install
npm run build
```

或使用 AI 功能：

```bash
npm install
VITE_OPENAI_API_KEY=<YOUR_OPEN_AI_KEY> npm run build
```

### 使用 Docker 运行

```bash
docker run -e OPENAI_API_KEY=<YOUR_OPEN_AI_KEY> -p 8080:80 ghcr.io/chartdb/chartdb:latest
```

### 本地构建和运行

```bash
docker build -t chartdb .
docker run -e OPENAI_API_KEY=<YOUR_OPEN_AI_KEY> -p 8080:80 chartdb
```

### 使用自定义推理服务器

```bash
# 构建
docker build \
  --build-arg VITE_OPENAI_API_ENDPOINT=<YOUR_ENDPOINT> \
  --build-arg VITE_LLM_MODEL_NAME=<YOUR_MODEL_NAME> \
  -t chartdb .

# 运行
docker run \
  -e OPENAI_API_ENDPOINT=<YOUR_ENDPOINT> \
  -e LLM_MODEL_NAME=<YOUR_MODEL_NAME> \
  -p 8080:80 chartdb
```

> **隐私说明**：ChartDB 包含隐私友好的分析，使用 Fathom Analytics。您可以通过添加 `-e DISABLE_ANALYTICS=true` 到运行命令或构建时使用 `--build-arg VITE_DISABLE_ANALYTICS=true` 来禁用它。

> **注意**：您必须配置选项 1（OpenAI API 密钥）或选项 2（自定义端点和模型名称）才能使 AI 功能正常工作。请勿混合使用这两个选项。

在浏览器中打开 `http://localhost:8080`。

本地 vLLM 服务器的示例配置：

```
VITE_OPENAI_API_ENDPOINT=http://localhost:8000/v1
VITE_LLM_MODEL_NAME=Qwen/Qwen2.5-32B-Instruct-AWQ
```

## 在网站上试用

1. 访问 [ChartDB.io](https://chartdb.io?ref=github_readme_2)
2. 点击“转到应用”
3. 选择您使用的数据库。
4. 获取魔法查询并在数据库中运行。
5. 将结果 JSON 集复制并粘贴到 ChartDB 中。
6. 享受查看和编辑！

## 💚 社区与支持

- [Discord](https://discord.gg/QeFwyWSKwC)（与社区和 ChartDB 团队进行实时讨论）
- [GitHub Issues](https://github.com/chartdb/chartdb/issues)（任何使用 ChartDB 时遇到的错误和错误）
- [Twitter](https://x.com/intent/follow?screen_name=jonathanfishner)（快速获取新闻）

## 贡献

我们欢迎社区贡献，大小皆宜，并在这里指导您沿着这条路走下去。随时在 [ChartDB Community Discord](https://discord.gg/QeFwyWSKwC) 中给我们留言。

有关如何贡献的更多信息，请参阅我们的 [贡献指南](/CONTRIBUTING.md)。

此项目以 [贡献者行为准则](/CODE_OF_CONDUCT.md) 的名义发布。通过参与此项目，您同意遵守其条款。

感谢您帮助使 ChartDB 对每个人都更好 :heart:.

## 许可证

ChartDB 根据 [GNU Affero General Public License v3.0](LICENSE) 获得许可

```

```
