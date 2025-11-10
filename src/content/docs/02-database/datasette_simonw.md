---
title: datasette
---

# Datasette 项目

## 项目地址
[GitHub 项目地址](https://github.com/simonw/datasette)

## 主要特性
Datasette 是一个开源工具，用于将 SQLite 数据库文件即时转换为可浏览和查询的 Web 接口。它支持快速部署数据应用，无需编写复杂代码。主要特性包括：
- **即时 Web 接口**：上传 SQLite 文件，即可生成交互式网页，支持 SQL 查询和数据浏览。
- **数据发布**：轻松将数据作为 API 发布，支持 JSON、CSV 等格式导出。
- **插件生态**：丰富的插件系统，可扩展功能，如数据可视化、认证和搜索。
- **元数据支持**：添加描述、标签和自定义视图，提升数据可读性。
- **跨平台兼容**：支持 SQLite 的所有特性，包括空间数据（Spatialite）和全文搜索（FTS）。
- **部署灵活**：可作为命令行工具、Docker 容器或云服务运行，支持 Vercel、Heroku 等平台。

## 主要功能
- **数据浏览**：通过网页表格查看数据库表，支持分页、排序和过滤。
- **SQL 查询**：内置查询编辑器，执行自定义 SQL 并显示结果。
- **API 端点**：每个表和查询自动生成 RESTful API，支持参数化查询。
- **数据导入/导出**：从 CSV、JSON 等导入数据，或导出为多种格式。
- **自定义界面**：使用模板和 JavaScript 插件自定义页面外观和交互。
- **协作与分享**：生成可分享的链接，支持嵌入式视图和嵌入式组件。
- **安全与访问控制**：通过插件实现用户认证和权限管理。

## 用法
1. **安装**：
   - 使用 pip 安装：`pip install datasette`
   - 或通过 Docker：`docker run -p 8001:8001 -v $PWD:/data simonw/datasette`

2. **运行**：
   - 基本命令：`datasette mydatabase.db`（替换为你的 SQLite 文件路径）
   - 这将启动本地服务器，默认在 http://localhost:8001 访问。
   - 添加元数据：`datasette mydatabase.db --metadata metadata.yml`

3. **使用示例**：
   - 访问网页：打开浏览器，浏览表、执行查询。
   - API 调用：如 `http://localhost:8001/mydatabase/table.json` 获取 JSON 数据。
   - 发布到云：使用 `datasette publish vercel mydatabase.db` 部署到 Vercel。
   - 插件安装：`pip install datasette-插件名`，然后在元数据中启用。

更多详情请参考项目文档。