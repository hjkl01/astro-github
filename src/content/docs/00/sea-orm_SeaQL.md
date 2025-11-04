
---
title: sea-orm
---

# SeaORM (SeaQL)

**项目地址**  
<https://github.com/SeaQL/sea-orm>

## 概述  
SeaORM 是 Rust 生态中一个基于异步 I/O 的 ORM 框架，旨在提供类型安全、可组合且性能优异的数据库交互方式。它支持多种主流数据库（PostgreSQL、MySQL、SQLite、MSSQL 等），并提供迁移、查询构建、事务管理等完整功能。

## 主要特性  

| 特性 | 说明 |
|------|------|
| **异步原生** | 采用 async/await，使用 `tokio` / `async-std` 运行时，适合高并发的 Web/CLI 应用 |
| **类型安全** | 通过 Rust 的类型系统，编译期检查表结构、字段类型，减少运行时错误 |
| **查询构建器** | 支持链式 DSL 与原生 SQL 两种写法，查询语句在编译期就能被验证 |
| **迁移工具** | `sea-orm-cli` 提供 `migrate` 命令，支持版本化迁移、自动生成迁移脚本 |
| **事务支持** | 事务可在单个查询或多查询块中使用，支持嵌套事务 |
| **连接池** | 内置 `bb8` / `sqlx` 连接池，自动管理连接、扩容、回收 |
| **多数据库** | 通过统一的驱动接口，支持 PostgreSQL、MySQL、SQLite、MSSQL，甚至自定义数据库 |
| **自动代码生成** | `sea-orm-cli generate` 可以根据数据库模式生成模型代码，减少手工编写 |
| **可插拔** | 可通过自定义 `EntityTrait`、`Filter` 等实现业务扩展 |

## 安装

```bash
# Cargo.toml
[dependencies]
sea-orm = { version = "0.12", features = ["sqlx-postgres", "runtime-tokio-rustls"] }

# 如果需要使用 CLI
cargo install sea-orm-cli
```

## 基本用法

### 1. 定义模型

```rust
use sea_orm::entity::prelude::*;

#[derive(Clone, Debug, PartialEq, DeriveEntityModel)]
#[sea_orm(table_name = "user")]
pub struct Model {
    #[sea_orm(primary_key)]
    pub id: i32,
    pub username: String,
    pub email: String,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {}

impl ActiveModelBehavior for ActiveModel {}
```

### 2. 创建数据库连接

```rust
use sea_orm::{Database, DatabaseConnection};

pub async fn init_db() -> DatabaseConnection {
    let db = Database::connect("postgres://user:pwd@localhost:5432/dbname")
        .await
        .expect("Cannot connect to database");
    db
}
```

### 3. CRUD 示例

```rust
use sea_orm::entity::ActiveModelTrait;
use sea_orm::prelude::*;

#[tokio::main]
async fn main() {
    let db = init_db().await;

    // Create
    let new_user = user::ActiveModel {
        username: Set("alice".into()),
        email: Set("alice@example.com".into()),
        ..Default::default()
    };
    let inserted = user::Entity::insert(new_user)
        .exec(&db)
        .await
        .expect("Insert failed");

    // Read
    let users = user::Entity::find()
        .filter(user::Column::Username.eq("alice"))
        .all(&db)
        .await
        .expect("Select failed");

    // Update
    let mut user: user::ActiveModel = users[0].clone().into();
    user.email = Set("alice_new@example.com".into());
    user.update(&db).await.expect("Update failed");

    // Delete
    user.delete(&db).await.expect("Delete failed");
}
```

### 4. 事务

```rust
let txn = db.begin().await.expect("Begin txn");
let _ = user::Entity::insert(new_user).exec(&txn).await?;
txn.commit().await.expect("Commit txn");
```

## 迁移

```bash
# 初始化迁移目录
sea-orm-cli migrate init

# 创建新迁移
sea-orm-cli migrate generate add_user_table

# 编写迁移脚本（在 migrations/xxxx_add_user_table.rs）
# 运行迁移
sea-orm-cli migrate up
```

## CLI 工具

```bash
# 生成模型代码
sea-orm-cli generate

# 查看帮助
sea-orm-cli --help
```

## 参考

- 官方文档: <https://www.sea-ql.org/SeaORM/docs/>
- GitHub 仓库: <https://github.com/SeaQL/sea-orm>

--- 

> 以上内容已保存为 **src/content/docs/00/sea-orm_SeaQL.md**。请根据项目需求自行调整或扩充。