---
title: sea-orm
---

# SeaORM

SeaORM 是一个强大的 Rust ORM，用于构建 Web 服务。它是一个异步和动态的 ORM，支持过滤、分页和嵌套查询，帮助加速构建 REST、GraphQL 和 gRPC API。

## 功能特性

### 功能丰富

SeaORM 是一个功能齐全的 ORM，具有过滤、分页和嵌套查询功能，用于加速构建 REST、GraphQL 和 gRPC API。

### 生产就绪

SeaORM 已生产就绪，每周下载量超过 250k，被全球初创企业和企业广泛信任。

### 支持的数据库

- MySQL
- PostgreSQL
- SQLite
- MariaDB

### 实体格式

SeaORM 支持表达式的实体格式，可以从现有数据库生成实体文件。

### 智能实体加载器

实体加载器智能地使用 join 处理 1-1 关系，使用数据加载器处理 1-N 关系，消除 N+1 问题。

### Schema First 或 Entity First

SeaORM 提供强大的迁移系统，让您轻松创建表、修改模式和种子数据。SeaORM 2.0 还提供一流的 Entity First 工作流。

### 原始 SQL 支持

SeaORM 提供便捷的支持来编写复杂的原始 SQL 查询。

## 基本用法

### 安装

在 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
sea-orm = { version = "1", features = ["sqlx-postgres", "runtime-tokio-rustls", "macros"] }
```

### 定义实体

使用宏定义实体：

```rust
use sea_orm::entity::prelude::*;

#[derive(Clone, Debug, PartialEq, Eq, DeriveEntityModel)]
#[sea_orm(table_name = "cake")]
pub struct Model {
    #[sea_orm(primary_key)]
    pub id: i32,
    pub name: String,
}

#[derive(Copy, Clone, Debug, EnumIter, DeriveRelation)]
pub enum Relation {
    #[sea_orm(has_many = "super::filling::Entity")]
    Filling,
}

impl Related<super::filling::Entity> for Entity {
    fn to() -> RelationDef {
        Relation::Filling.def()
    }
}

impl ActiveModelBehavior for ActiveModel {}
```

### 连接数据库

```rust
use sea_orm::{Database, DatabaseConnection};

let db: DatabaseConnection = Database::connect("postgres://user:password@localhost/myapp").await?;
```

### 查询

```rust
// 查找所有模型
let cakes: Vec<cake::Model> = Cake::find().all(&db).await?;

// 查找和过滤
let chocolate: Vec<cake::Model> = Cake::find()
    .filter(Cake::COLUMN.name.contains("chocolate"))
    .all(&db)
    .await?;
```

### 插入

```rust
let apple = fruit::ActiveModel {
    name: Set("Apple".to_owned()),
    ..Default::default()
};

// 插入一个
let apple = apple.insert(&db).await?;
```

### 更新

```rust
let mut pear: fruit::ActiveModel = pear.into();
pear.name = Set("Sweet pear".to_owned());
let pear: fruit::Model = pear.update(&db).await?;
```

### 删除

```rust
let orange: fruit::Model = orange.unwrap();
orange.delete(&db).await?;
```

## 高级用法

### 嵌套查询

```rust
#[derive(DerivePartialModel)]
#[sea_orm(entity = "cake::Entity")]
struct CakeWithFruit {
    id: i32,
    name: String,
    #[sea_orm(nested)]
    fruit: Option<fruit::Model>,
}

let cakes: Vec<CakeWithFruit> = Cake::find()
    .left_join(fruit::Entity)
    .into_partial_model()
    .all(&db)
    .await?;
```

### 原始 SQL

```rust
let user: Option<user::Model> = user::Entity::find()
    .from_raw_sql(raw_sql!(
        Sqlite,
        r#"SELECT "id", "name" FROM "user"
           WHERE "name" LIKE {user.name}
           AND "id" in ({..ids})"#
    ))
    .one(&db)
    .await?;
```

## 集成

### Seaography

Seaography 是为 SeaORM 构建的 GraphQL 框架，允许您快速构建 GraphQL 解析器。

### SeaORM Pro

SeaORM Pro 是一个管理面板解决方案，让您快速轻松地为应用程序启动管理面板。

## 文档和示例

- [官方文档](https://www.sea-ql.org/SeaORM)
- [示例](https://github.com/SeaQL/sea-orm/tree/master/examples)
