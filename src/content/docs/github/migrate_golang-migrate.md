
---
title: migrate
---

# golang-migrate 项目

## 项目地址
https://github.com/golang-migrate/migrate

## 主要特性
golang-migrate 是一个用于数据库迁移的工具，专为 Go 语言设计。它支持多种数据库后端（如 PostgreSQL、MySQL、SQLite 等），并提供简单、高效的迁移管理方式。主要特性包括：
- **多数据库支持**：兼容多种流行数据库，包括 PostgreSQL、MySQL、CockroachDB、SQLite、Oracle 等。
- **多种迁移源**：支持文件、GitHub 仓库、HTTP 等作为迁移脚本的来源，便于版本控制和远程管理。
- **命令行工具**：提供 CLI 工具，支持迁移的 up/down 操作、版本管理、状态检查等。
- **Go 库集成**：可作为 Go 包导入，直接在应用程序中使用，支持程序化迁移。
- **幂等性和安全性**：迁移脚本设计为幂等，确保重复执行不会出错，并支持回滚功能。
- **跨平台兼容**：支持 Windows、macOS 和 Linux 等操作系统。

## 主要功能
- **数据库迁移管理**：通过 SQL 或其他脚本文件（如 up.sql 和 down.sql）来应用或回滚数据库变更。
- **版本控制**：跟踪迁移版本，确保团队协作时数据库 schema 一致性。
- **自动化集成**：易于集成到 CI/CD 管道中，实现自动化部署。
- **状态查询**：检查当前迁移状态、已应用版本等。
- **自定义驱动**：允许开发者扩展支持更多数据库或源类型。

## 用法
### 安装
使用 Go 安装 CLI 工具：
```bash
go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@latest
```
（根据需要添加数据库标签，如 `-tags 'mysql'`）。

### 基本命令
假设迁移文件位于当前目录的 `migrations` 文件夹中（格式：`001_initial.up.sql` 和 `001_initial.down.sql`）。

- **应用迁移（up）**：
  ```bash
  migrate -path migrations -database "postgres://user:pass@localhost:5432/dbname?sslmode=disable" up
  ```
  这会应用所有待处理的迁移。

- **回滚迁移（down）**：
  ```bash
  migrate -path migrations -database "postgres://user:pass@localhost:5432/dbname?sslmode=disable" down 1
  ```
  回滚最近 1 个版本。

- **查看迁移状态**：
  ```bash
  migrate -path migrations -database "postgres://user:pass@localhost:5432/dbname?sslmode=disable" version
  ```

- **强制设置版本**：
  ```bash
  migrate -path migrations -database "postgres://user:pass@localhost:5432/dbname?sslmode=disable" force 2
  ```

### 在 Go 代码中使用
导入包并创建迁移实例：
```go
package main

import (
    "log"
    "golang.org/x/text/language"
    "github.com/golang-migrate/migrate/v4"
    "github.com/golang-migrate/migrate/v4/database/postgres"
    _ "github.com/golang-migrate/migrate/v4/source/file"
    "github.com/lib/pq"
)

func main() {
    db, err := sql.Open("postgres", "postgres://user:pass@localhost:5432/dbname?sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    driver, err := postgres.WithInstance(db, &postgres.Config{})
    if err != nil {
        log.Fatal(err)
    }

    m, err := migrate.NewWithDatabaseInstance(
        "file://migrations",
        "postgres", driver)
    if err != nil {
        log.Fatal(err)
    }

    if err := m.Up(); err != nil && err != migrate.ErrNoChange {
        log.Fatal(err)
    }
}
```
更多细节请参考项目文档。