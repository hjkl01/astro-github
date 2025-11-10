---
title: sqlx
---

# SQLx (launchbadge)

项目地址: <https://github.com/launchbadge/sqlx>

## 主要特性

- **编译时查询校验**  
  通过 `query!`, `query_as!`, `fetch!` 等宏，在编译阶段就能检查 SQL 语法、字段与 Rust 结构体的一致性，降低运行时错误。

- **异步/阻塞双模式**  
  原生支持 `async/await`，同时提供同步 API，满足不同场景需求。

- **多数据库支持**  
  兼容 PostgreSQL、MySQL、SQLite 等主流关系型数据库，单个 crate 即可跨数据库使用。

- **Connection Pool（连接池）**  
  内置强大且可配置的连接池，支持最大连接数、连接生命周期等参数。

- **事务与批处理**  
  支持手动事务和自动回滚；提供 `query` 批量执行、`transaction` 事务链式调用。

- **灵活错误处理**  
  所有查询返回 `Result<T, sqlx::Error>`，标准化错误类型，便于统一处理。

- **高性能 & 低耦合**  
  采用零成本抽象，避免反射与运行时类型检查，保持高吞吐量。

## 快速开始

### Cargo 依赖

```toml
[dependencies]
sqlx = { version = "0.8", features = ["postgres", "runtime-tokio-rt", "macros"] }
tokio = { version = "1", features = ["full"] }
```

> 根据需要开启对应数据库功能，例如 `mysql`, `sqlite` 等。

### 简单示例（PostgreSQL）

```rust
use sqlx::postgres::PgPoolOptions;
use sqlx::Result;

#[tokio::main]
async fn main() -> Result<()> {
    // 创建连接池
    let pool = PgPoolOptions::new()
        .max_connections(5)
        .connect("postgres://user:password@localhost/dbname")
        .await?;

    // 简单查询
    let count: (i64,) = sqlx::query_as("SELECT COUNT(*) FROM users")
        .fetch_one(&pool)
        .await?;

    println!("用户总数: {}", count.0);

    // 参数化查询，编译时校验
    let user: (i32, String) = sqlx::query_as!(UserRecord, "SELECT id, name FROM users WHERE id = $1", 42)
        .fetch_one(&pool)
        .await?;

    println!("id: {}, name: {}", user.0, user.1);

    Ok(())
}

struct UserRecord {
    id: i32,
    name: String,
}
```

### 动态查询

```rust
use sqlx::Executor;

async fn find_user_by_name(pool: &sqlx::PgPool, name: &str) -> Result<Vec<User>> {
    let recs = sqlx::query_as!(
        User,
        "SELECT id, name FROM users WHERE name = $1",
        name
    )
    .fetch_all(pool)
    .await?;

    Ok(recs)
}

struct User {
    id: i32,
    name: String,
}
```

## 高级功能

- **简化结构体映射**  
  `#[derive(sqlx::FromRow)]` 自动实现行到结构体的转换，减少冗余代码。

- **连接池指标**  
  `sqlx::postgres::PgPool` 提供 `acquire_timeout`, `max_lifetime` 等细粒度调控。

- **缓存与预编译**  
  `QueryBuilder` 支持构造可重用的动态语句，配合 `query_builder!` 宏可提高性能。

- **多模式查询**  
  运行时可以指定不同数据库的查询实现，切换母语数据库实现更灵活。

## 文档与社区

- 官方文档: <https://docs.rs/sqlx/>
- GitHub Issues: <https://github.com/launchbadge/sqlx/issues>
- Discord 讨论组: https://discord.com/invite/sqlx

---