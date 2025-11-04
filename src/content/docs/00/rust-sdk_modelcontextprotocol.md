
---
title: rust-sdk
---


# Rust SDK (ModelContextProtocol)

- **仓库地址**：<https://github.com/modelcontextprotocol/rust-sdk>

## 主要特性

| 特色 | 说明 |
|------|------|
| **数据模型定义** | 通过 `#[derive(ProtocolJson, ProtocolModel)]` 等宏，可快速生成序列化/反序列化实现。 |
| **上下文管理** | `ModelContext` 提供 CRUD、查询、变更追踪等操作，兼容异步调用。 |
| **变更记录** | `ModelModifier` 记录对模型的增删改操作，可批量提交。 |
| **事务支持** | `ModelTransaction` 用于原子性执行一组变更，支持回滚。 |
| **跨语言兼容** | 内建的 JSON 传输层使得 SDK 可与 Java、Python 等语言互操作。 |
| **可插拔存储后端** | 默认使用 Rust 标准库自带 `HashMap`，也可通过实现 `Store` trait 换用数据库或网络存储。 |
| **类型安全** | Rust 的强类型系统保证模型字段匹配与安全执行。 |

## 功能概览

```rust
use modelcontext_protocol::{
    ModelContext, ModelModifier, Identifier,
    protocols::{user::UserModel, order::OrderModel},
};

#[tokio::main]
async fn main() {
    // 初始化上下文
    let mut ctx = ModelContext::new();

    // 创建模型实例
    let user = UserModel {
        id: Identifier::new(),
        name: "Alice".to_string(),
        email: "alice@example.com".to_string(),
    };

    // 应用增改
    let mut modifier = ModelModifier::new();
    modifier.add(user);
    ctx.apply(modifier).await.unwrap();

    // 查询
    let users = ctx.query::<UserModel>().await;
    println!("{:?}", users);
}
```

## 用法指南

1. **安装依赖**  
   ```toml
   [dependencies]
   modelcontext_protocol = "0.1"
   tokio = { version = "1", features = ["full"] }
   ```

2. **定义业务模型**  
   ```rust
   use modelcontext_protocol::{ProtocolModel, ProtocolJson};

   #[derive(ProtocolModel, ProtocolJson)]
   struct UserModel {
       id: Identifier,
       name: String,
       email: String,
   }
   ```

3. **创建并操作上下文**  
   - `ModelContext::new()`：创建一个空上下文。  
   - `ModelModifier::add()` / `remove()` / `update()`：构造变更。  
   - `ctx.apply(modifier)`：提交变更。  
   - `ctx.query::<T>()`：查询指定类型的所有实例。  

4. **事务与回滚**  
   ```rust
   let mut transaction = ctx.transaction();
   transaction.add(user);
   transaction.commit().await?;
   // 如出现错误
   transaction.rollback().await?;
   ```

5. **自定义存储后端**  
   ```rust
   use modelcontext_protocol::{Store, InMemoryStore};

   struct MyDbStore;
   impl Store for MyDbStore { /* ... */ }

   let store = MyDbStore::new();
   let mut ctx = ModelContext::new_with_store(Box::new(store));
   ```

6. **多语言交互**  
   - SDK 自带 `ProtocolJson`，仅需将 JSON 传输给后端实现即可实现与其他语言的协同。

> 进一步细节请参阅项目 README 与 API 文档。  
