---
title: pgweb
---

# pgweb 项目

**GitHub 项目地址:** [https://github.com/sosedoff/pgweb](https://github.com/sosedoff/pgweb)

## 主要特性
pgweb 是一个基于 Web 的 PostgreSQL 数据库浏览器和编辑器，主要特性包括：
- **浏览器界面**：提供直观的 Web 界面，允许用户通过浏览器访问和操作 PostgreSQL 数据库，无需安装额外的桌面客户端。
- **数据库连接**：支持通过连接字符串或环境变量快速连接到 PostgreSQL 服务器，支持 SSL 和自定义端口。
- **查询执行**：内置 SQL 编辑器，支持运行单个查询或多语句脚本，实时显示结果集。
- **数据管理**：可以浏览表结构、查看和编辑数据、导出结果为 CSV 或 JSON 格式。
- **轻量级部署**：Go 语言编写，单二进制文件，可作为 Web 服务器运行，支持 Docker 部署，便于在各种环境中使用。
- **安全性**：支持基本认证和会话管理，适用于开发和测试环境。
- **跨平台**：兼容 Windows、macOS 和 Linux，支持嵌入式模式作为库使用。

## 主要功能
- **连接管理**：通过 Web 表单输入数据库连接细节（如主机、端口、用户名、密码），或使用 DSN（Data Source Name）格式连接。
- **表浏览器**：列出所有数据库、模式和表，支持搜索和过滤，查看表元数据（如列、索引、约束）。
- **SQL 编辑器**：语法高亮、自动补全（基本支持），执行查询后显示结果，包括行数统计和错误信息。
- **数据编辑**：支持直接在界面中编辑表数据、插入新行或删除记录（需谨慎使用）。
- **导出与导入**：结果集可导出为文件，支持简单的 CSV 导入。
- **监控**：显示服务器状态、连接信息和基本性能指标。
- **API 支持**：可作为 RESTful API 服务器，提供查询端点。

## 用法
1. **下载与安装**：
   - 从 GitHub Releases 下载适用于你的平台的二进制文件（例如 pgweb_v0.x.x_linux_amd64.tar.gz）。
   - 解压后运行 `./pgweb` 启动服务器，默认监听 8080 端口。

2. **运行服务器**：
   - 基本启动：`./pgweb`（需设置环境变量 `DATABASE_URL` 如 `postgres://user:pass@localhost:5432/dbname`）。
   - 指定端口：`./pgweb --bind 0.0.0.0:8081`。
   - 使用认证：`./pgweb --user admin --pass secret`。

3. **Docker 部署**：
   - 拉取镜像：`docker pull sosedoff/pgweb`。
   - 运行：`docker run -p 8080:8080 -e "DATABASE_URL=postgres://user:pass@host:5432/db" sosedoff/pgweb`。

4. **Web 界面使用**：
   - 打开浏览器访问 `http://localhost:8080`。
   - 输入连接信息连接数据库。
   - 选择数据库，浏览表或输入 SQL 查询执行。
   - 编辑数据时，确认操作以避免意外修改。

注意：pgweb 适合开发和测试，不推荐用于生产环境的高并发访问。更多细节请参考项目 README。