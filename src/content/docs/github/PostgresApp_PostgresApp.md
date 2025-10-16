
---
title: PostgresApp
---

# PostgresApp 项目

## 项目地址
[https://github.com/PostgresApp/PostgresApp](https://github.com/PostgresApp/PostgresApp)

## 主要特性
PostgresApp 是一个简单易用的 macOS 应用程序，用于在 Mac 上安装、运行和管理 PostgreSQL 数据库服务器。它无需复杂的命令行操作或第三方依赖，直接通过图形界面管理，支持多版本 PostgreSQL 共存。核心特性包括：
- **一键安装**：快速下载并安装最新或指定版本的 PostgreSQL，无需 Homebrew 或其他工具。
- **图形化管理**：提供直观的界面来启动、停止服务器，查看日志，以及管理数据库集群。
- **多版本支持**：可以同时运行多个 PostgreSQL 版本（如 9.x 到 16.x），便于开发和测试。
- **内置工具**：集成 psql 命令行工具、pgAdmin 等，支持导入/导出数据、备份和恢复。
- **轻量级**：应用程序体积小，资源占用低，适合开发者个人使用。
- **安全性**：默认配置安全的数据库设置，支持 SSL 和认证机制。
- **跨平台兼容**：专为 macOS 设计，支持 Intel 和 Apple Silicon（M1/M2）架构。

## 主要功能
- **服务器管理**：启动/停止 PostgreSQL 服务器，监控状态和性能。
- **数据库操作**：创建、删除数据库；管理用户和角色；执行 SQL 查询。
- **数据导入/导出**：支持 SQL 转储、CSV 文件导入，以及 pg_dump/pg_restore 工具。
- **配置自定义**：编辑 postgresql.conf 和 pg_hba.conf 文件，调整内存、连接等参数。
- **日志查看**：实时查看错误日志和查询日志，便于调试。
- **扩展支持**：轻松安装 PostgreSQL 扩展，如 PostGIS（地理信息系统）或 pg_trgm（全文搜索）。
- **集成开发**：与 IDE（如 VS Code、IntelliJ）无缝集成，支持远程连接模拟。

## 用法
1. **下载与安装**：
   - 从 GitHub Releases 页面下载最新 .dmg 文件。
   - 双击安装包，将 Postgres.app 拖到 Applications 文件夹。
   - 首次运行时，选择 PostgreSQL 版本并安装（约 100-200MB）。

2. **启动服务器**：
   - 打开 Postgres.app，从菜单栏图标选择“Start Servers for Version X.Y”。
   - 服务器默认监听 localhost:5432，支持超级用户 postgres（密码为空，可自定义）。

3. **创建数据库**：
   - 在应用界面点击“Open psql”或使用内置浏览器创建新数据库。
   - 示例命令（在 Terminal 中）：`createdb mydb`（需先连接 psql）。

4. **连接数据库**：
   - 使用 psql：`psql -U postgres -d mydb`。
   - 或通过外部工具如 DBeaver、TablePlus 连接（主机：localhost，端口：5432）。

5. **停止与卸载**：
   - 从菜单栏停止服务器。
   - 要卸载，删除 Applications 中的 Postgres.app，并移除 ~/Library/Application Support/Postgres 目录。

更多细节请参考项目 README 和官方文档。