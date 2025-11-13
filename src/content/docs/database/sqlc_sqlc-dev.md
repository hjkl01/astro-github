---
title: sqlc
---

# sqlc 项目简介

## 主要功能

sqlc 是一个 SQL 编译器，能够从 SQL 查询生成类型安全的、符合语言习惯的代码。它的工作流程如下：

1. 编写 SQL 查询。
2. 运行 sqlc 生成包含类型安全接口的代码。
3. 在应用程序中调用生成的代码。

## 主要特性

- **类型安全**：生成的代码提供类型安全的接口，避免运行时错误。
- **多语言支持**：支持生成 Go、Kotlin、Python、TypeScript 等语言的代码，还可通过插件扩展更多语言。
- **数据库兼容**：支持 PostgreSQL、MySQL 和 SQLite。
- **零依赖**：sqlc 本身是一个单二进制文件，无需额外依赖。
- **云服务集成**：可与 sqlc Cloud 集成，用于查询验证、模式变更检查和洞察分析。
- **查询注解**：支持在 SQL 查询中使用注解（如 `:one`、`:many`、`:exec`）来指定返回类型。
- **配置灵活**：通过 `sqlc.yaml` 或 `sqlc.json` 配置文件自定义生成选项。

## 使用说明

### 安装

- **macOS**：`brew install sqlc`
- **Ubuntu**：`sudo snap install sqlc`
- **Go 安装**（需要 Go 1.21+）：`go install github.com/sqlc-dev/sqlc/cmd/sqlc@latest`
- **Docker**：`docker pull sqlc/sqlc`，运行时使用 `docker run --rm -v $(pwd):/src -w /src sqlc/sqlc generate`
- **下载**：从 [downloads.sqlc.dev](https://downloads.sqlc.dev/) 获取预编译二进制文件。

### 基本使用步骤

1. **初始化项目**：创建一个新目录，初始化 Go 模块（或其他语言项目）。
2. **创建配置文件**：在目录中创建 `sqlc.yaml`，示例配置：
   ```yaml
   version: '2'
   sql:
     - engine: 'postgresql' # 或 "mysql"、"sqlite"
       queries: 'query.sql'
       schema: 'schema.sql'
       gen:
         go: # 或其他语言，如 kotlin、python
           package: 'tutorial'
           out: 'tutorial'
           sql_package: 'pgx/v5'
   ```
3. **编写数据库模式**：创建 `schema.sql` 文件，定义表结构，例如：
   ```sql
   CREATE TABLE authors (
     id   BIGSERIAL PRIMARY KEY,
     name text      NOT NULL,
     bio  text
   );
   ```
4. **编写查询**：创建 `query.sql` 文件，使用注解编写查询，例如：

   ```sql
   -- name: GetAuthor :one
   SELECT * FROM authors WHERE id = $1 LIMIT 1;

   -- name: ListAuthors :many
   SELECT * FROM authors ORDER BY name;

   -- name: CreateAuthor :one
   INSERT INTO authors (name, bio) VALUES ($1, $2) RETURNING *;

   -- name: UpdateAuthor :exec
   UPDATE authors SET name = $2, bio = $3 WHERE id = $1;

   -- name: DeleteAuthor :exec
   DELETE FROM authors WHERE id = $1;
   ```

5. **生成代码**：运行 `sqlc generate`，这将在指定输出目录生成代码文件。
6. **使用生成的代码**：在应用程序中导入生成的包，使用提供的接口执行查询。例如，在 Go 中：
   ```go
   queries := tutorial.New(conn)
   authors, err := queries.ListAuthors(ctx)
   ```
7. **可选：云验证**：注册 sqlc Cloud 账户，设置项目 ID 和认证令牌，使用 `sqlc push` 上传查询，`sqlc verify` 验证模式变更。

更多详细信息请参考 [官方文档](https://docs.sqlc.dev) 或 [交互式示例](https://play.sqlc.dev/)。
