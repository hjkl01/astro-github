
---
title: usql
---

# uSQL 项目

## 项目地址
[https://github.com/xo/usql](https://github.com/xo/usql)

## 主要特性
uSQL 是一个通用的命令行 SQL 工具，支持多种数据库系统。它允许用户使用统一的接口连接和查询各种 SQL 数据库，而无需为每个数据库安装单独的客户端。主要特性包括：
- **多数据库支持**：兼容 PostgreSQL、MySQL、Oracle、SQL Server、SQLite、DB2、Sybase、Teradata 等多种数据库。
- **统一语法**：使用标准的 SQL 语法执行查询，支持跨数据库的命令行交互。
- **驱动集成**：内置 Go 语言的数据库驱动，简化安装和使用。
- **命令行友好**：提供类似于 `psql` 或 `mysql` 的交互式 shell，支持历史记录、自动补全和输出格式化。
- **跨平台**：支持 Linux、macOS 和 Windows 系统。
- **轻量级**：无需复杂配置，即插即用。

## 主要功能
- **连接数据库**：通过 DSN（Data Source Name）字符串连接到目标数据库。
- **执行 SQL 查询**：支持 SELECT、INSERT、UPDATE、DELETE 等标准 SQL 操作。
- **元数据查询**：内置命令如 `\dt`（列出表）、`\d`（描述表结构）等，类似于 PostgreSQL 的 psql。
- **输出格式**：支持表格、CSV、TSV 等多种输出格式，便于数据导出。
- **脚本执行**：可以从文件读取 SQL 脚本批量执行。
- **错误处理**：提供详细的错误信息和诊断工具。

## 用法
### 安装
1. 通过 Go 安装（推荐）：
   ```
   go install github.com/xo/usql@latest
   ```
2. 或从 GitHub Releases 下载预编译二进制文件，并确保添加到 PATH。

### 基本用法
1. **连接数据库**：
   - 直接在命令行指定 DSN：
     ```
     usql "postgres://user:pass@localhost/dbname?sslmode=disable"
     ```
   - 交互模式：运行 `usql` 进入 shell，然后使用 `\c DSN` 连接。

2. **执行查询**：
   - 在交互 shell 中输入 SQL：
     ```
     SELECT * FROM users LIMIT 10;
     ```
   - 命令行一次性执行：
     ```
     usql "mysql://user:pass@localhost/db" -c "SELECT * FROM users;"
     ```

3. **常用命令**（在 shell 中）：
   - `\h`：显示帮助。
   - `\l`：列出数据库。
   - `\dt`：列出表。
   - `\q`：退出。
   - `\o filename`：输出到文件（例如 CSV）。

4. **高级选项**：
   - 指定输出格式：`usql -f csv DSN`。
   - 执行 SQL 文件：`usql DSN < script.sql`。
   - 更多细节请参考项目 README：https://github.com/xo/usql/blob/master/README.md。