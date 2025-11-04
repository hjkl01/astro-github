
---
title: goose
---

# Goose – pressly/goose

项目地址: <https://github.com/pressly/goose>

## 1. 概述

`goose` 是一个用 Go 语言编写的数据库移框架，专门用于管理 SQL/Go 迁移脚本，支持多种数据库（PostgreSQL、MySQL、SQLite 等）。它的主要目标是简化数据库版本控制，保证迁移过程的可重复、可追溯与可回滚。

## 2. 主要特性

| 特性 | 说明 |
|------|------|
| **文件驱动** | 迁移脚本既可以写成独立的 SQL 文件 (*.sql)，也可以写成 Go 程序 (*.go)。|
| **版本控制** | 通过 migration ID（如 `001_create_users_table.sql`）记录迁移顺序，避免重复执行。|
| **事务安全** | 所有迁移执行在事务中（若数据库支持），错误自动回滚。|
| **多数据库支持** | 内置 PostgreSQL、MySQL、SQLite、SQL Server、CockroachDB 等数据库驱动。|
| **在线迁移** | 通过 Go 包直接在应用中调用，无需外部 CLI。|
| **回滚 & 前滚** | `goose down` 可撤销最近一次迁移；`goose up-to` 可在任意版本之间迁移。|
| **可插拔外部脚本** | 可通过 `--eval` 执行外部命令或脚本进行特殊任务。|
| **代码生成** | `goose create` 自动生成迁移文件骨架。|

## 3. 安装

```bash
# Go 模块
go get github.com/pressly/goose/v3

# CLI
go install github.com/pressly/goose/v3/cmd/goose@latest
```

## 4. 基本用法

### 4.1 准备迁移文件

1. **创建迁移**  
   ```bash
   goose create create_users_table sql
   ```
   生成文件名类似 `20230916123456_create_users_table.sql`。

2. **编辑文件**  
   在文件中写入 SQL 或 Go 代码。例如：

   ```sql
   -- +migrate Up
   CREATE TABLE users (
       id      BIGSERIAL PRIMARY KEY,
       name    TEXT NOT NULL,
       email   TEXT NOT NULL UNIQUE
   );
   --

   -- +migrate Down
   DROP TABLE users;
   ```

### 4.2 迁移数据库

```bash
# 指定数据库连接字符串
goose -dir migrations postgres "postgres://user:password@localhost:5432/dbname?sslmode=disable" up
```

- `-dir`：迁移文件目录。  
- `up`：执行所有未执行的迁移。  
- `down`：回滚最近一次迁移。  
- `status`：查看迁移执行状态。  
- `up-to 20190101010101`：迁移到指定版本。

### 4.3 在 Go 代码中使用

```go
import "github.com/pressly/goose/v3"

func migrate(db *sql.DB) error {
    // 迁移到最新版本
    return goose.Up(db, "migrations")
}
```

## 5. 迁移文件约定

| 文件名格式 | 示例 | 说明 |
|------------|------|------|
| `YYYYMMDDHHMMSS_description.sql` | `20230916123456_create_users_table.sql` | SQL 迁移 |
| `YYYYMMDDHHMMSS_description.go` | `20230916123456_create_users_table.go` | Go 迁移 |

迁移文件中支持两段代码块：
- `-- +migrate Up` 与 `-- +migrate Down`（SQL）或 `// +goose Up` 与 `// +goose Down`（Go）。

## 6. 常用命令

| 命令 | 用途 |
|------|------|
| `goose create <name> sql|go` | 创建迁移文件 |
| `goose up` | 执行所有未执行的迁移 |
| `goose down` | 回滚最近一次迁移 |
| `goose status` | 查看迁移状态 |
| `goose up-to <version>` | 迁移到指定版本 |
| `goose reset` | 回滚所有迁移并重新执行 |

## 7. 进阶使用

- **自定义 SQL**：在迁移脚本中使用 `-- +migrate Up`／`Down` 插件来执行不同环境下的 SQL。  
- **代码迁移**：在 Go 文件中实现 `func Up(db *sql.DB) error` 和 `func Down(db *sql.DB) error`，可执行复杂事务逻辑。  
- **外部脚本**：通过 `--eval` 选项执行 shell 脚本或 Python 脚本以处理文件系统等非数据库任务。  

## 8. 注意事项

1. 迁移文件必须保持不可变，对已部署的迁移文件不应再进行修改。  
2. 保证所有迁移在事务中执行，若数据库不支持事务则回滚不可用。  
3. 在生产环境前请先在测试数据库上充分验证迁移顺序与回滚逻辑。

--- 

**文件路径**: `src/content/docs/00/goose_pressly.md`  
（请按需保存以上 Markdown 内容。）