
---
title: shiori
---

# Shiori 项目

## 项目地址
[GitHub 项目地址](https://github.com/go-shiori/shiori)

## 主要特性
Shiori 是一个基于 Go 语言开发的简单书签管理工具（Bookmark Manager），它允许用户保存、组织和检索网页书签。核心特性包括：
- **书签存储与检索**：支持通过标题、标签、内容等关键词快速搜索书签，支持全文搜索功能。
- **网页内容提取**：自动提取网页的主要内容，移除广告和无关元素，便于阅读和存档。
- **标签与组织**：为书签添加标签，支持多标签分类和管理。
- **离线访问**：保存网页的 HTML 快照，支持离线阅读。
- **API 支持**：提供 RESTful API，便于与其他工具集成或扩展。
- **多平台支持**：可作为 Web 应用运行，支持 Docker 部署，适用于服务器或本地环境。
- **简单轻量**：无复杂依赖，易于安装和维护，支持 SQLite 或 PostgreSQL 作为后端数据库。

## 主要功能
- **添加书签**：通过 URL 输入添加新书签，工具会自动抓取并提取页面内容。
- **管理书签**：编辑、删除、归档书签，支持批量操作。
- **搜索与过滤**：高级搜索功能，包括按日期、标签或内容过滤。
- **导出/导入**：支持导出书签为 HTML、JSON 等格式，便于迁移或备份。
- **用户认证**：基本用户登录系统，支持多用户管理。
- **移动友好**：响应式 Web 界面，适用于桌面和移动设备。

## 用法
1. **安装**：
   - 下载预编译二进制文件，或使用 Go 构建：`go install github.com/go-shiori/shiori/cmd/shiori@latest`。
   - 支持 Docker：`docker run --rm -p 8080:8080 ghcr.io/go-shiori/shiori:latest`。

2. **运行**：
   - 命令行启动：`shiori server`（默认监听 8080 端口，使用 SQLite 数据库）。
   - 指定数据库：`shiori server --db-type postgres --db-url "postgres://user:pass@localhost/dbname"`。

3. **使用 Web 界面**：
   - 浏览器访问 `http://localhost:8080`。
   - 首次使用需创建账户。
   - 添加书签：点击 "Add Bookmark"，输入 URL 并添加标签。
   - 搜索：使用搜索栏输入关键词，浏览结果。
   - 管理：通过书签列表编辑或删除。

更多详情请参考项目 README。