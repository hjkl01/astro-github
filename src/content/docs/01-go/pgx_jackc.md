
---
title: pgx
---

# pgx

**项目地址**: https://github.com/jackc/pgx

## 主要特性
- **纯 Go 实现**：无依赖 C 库，适合云原生部署。
- **高性能二进制协议**：使用 PostgreSQL 的二进制协议，减少序列化开销。
- **连接池（pgxpool）**：自动管理连接，支持并发、高可用。
- **事务与批处理**：`Tx`、`Batch` 支持原子操作与批量执行。
- **COPY 与 COPY FROM**：高效批量导入/导出数据。
- **自定义类型映射**：灵活注册自定义 Go 类型与 PostgreSQL 类型。
- **Context 支持**：通过 `context.Context` 进行查询超时与取消。
- **多版本兼容**：支持 PostgreSQL 9.6+，并提供 v4 与 v5 版本。

## 功能概览
| 功能 | 说明 |
|------|------|
| `pgx.Connect` | 单连接方式，适合轻量级应用 |
| `pgxpool.Connect` | 连接池，适合高并发 |
| `Conn.Query`, `Conn.Exec` | 标准 SQL 执行 |
| `Conn.QueryRow` | 单行查询 |
| `Conn.CopyFrom` | 大量数据写入 |
| `Conn.CopyTo` | 大量数据读取 |
| `Tx` | 事务管理 |
| `Batch` | 批量查询/执行 |
| `CopyFromRows` | 通过 `[]pgx.CopyFromSource` 写入 |
| `pgxpool.Config` | 连接池配置 |
| `pgx.ConnConfig` | 单连接配置 |
| `pgx.TypeMapper` | 类型映射与解析 |

## 用法示例

```go
package main

import (
    "context"
    "fmt"
    "github.com/jackc/pgx/v5"
    "github.com/jackc/pgx/v5/pgxpool"
)

func main() {
    ctx := context.Background()

    // 1. 连接池方式
    pool, err := pgxpool.New(ctx, "postgres://user:pass@localhost:5432/dbname")
    if err != nil {
        panic(err)
    }
    defer pool.Close()

    // 2. 执行查询
    var count int
    err = pool.QueryRow(ctx, "SELECT COUNT(*) FROM users").Scan(&count)
    if err != nil {
        panic(err)
    }
    fmt.Println("用户数量:", count)

    // 3. 事务
    tx, err := pool.Begin(ctx)
    if err != nil {
        panic(err)
    }
    defer tx.Rollback(ctx)

    _, err = tx.Exec(ctx, "INSERT INTO users(name) VALUES ($1)", "Alice")
    if err != nil {
        panic(err)
    }
    tx.Commit(ctx)

    // 4. COPY FROM 示例
    rows := [][]interface{}{
        {"Bob", 30},
        {"Carol", 25},
    }
    _, err = pool.CopyFrom(ctx,
        pgx.Identifier{"users"},
        []string{"name", "age"},
        pgx.CopyFromRows(rows),
    )
    if err != nil {
        panic(err)
    }
}
```

> 以上示例演示了连接池创建、单行查询、事务操作以及 COPY FROM 批量写入。  
> 更多高级用法请参阅官方文档与源码示例。