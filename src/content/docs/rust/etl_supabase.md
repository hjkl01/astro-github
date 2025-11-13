---
title: etl
---

# ETL by Supabase

## 项目简介

ETL 是 Supabase 开发的 Rust 框架，用于构建高性能、实时的 Postgres 数据复制应用程序。它基于 Postgres 逻辑复制，提供干净、Rust 原生的 API，用于将更改流式传输到自定义目的地。

## 主要功能

- **实时复制**：实时流式传输更改到自定义目的地。
- **高性能**：可配置批处理和并行性以最大化吞吐量。
- **容错**：内置强大的错误处理和重试逻辑。
- **可扩展**：实现自定义目的地和状态/模式存储。
- **Rust 原生**：类型化和符合人体工程学的 Rust API。

## 要求

- **PostgreSQL 版本**：官方支持并测试 PostgreSQL 14、15、16 和 17。
- **推荐**：PostgreSQL 15+ 以访问高级发布功能，包括列级过滤、行级过滤（使用 WHERE 子句）和 `FOR ALL TABLES IN SCHEMA` 语法。

有关详细配置说明，请参阅 [配置 Postgres 文档](https://supabase.github.io/etl/how-to/configure-postgres/)。

## 快速开始

通过 Git 安装（在准备 crates.io 发布时）：

```toml
[dependencies]
etl = { git = "https://github.com/supabase/etl" }
```

使用内存目的地的快速示例：

```rust
use etl::{
    config::{BatchConfig, PgConnectionConfig, PipelineConfig, TlsConfig},
    destination::memory::MemoryDestination,
    pipeline::Pipeline,
    store::both::memory::MemoryStore,
};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let pg = PgConnectionConfig {
        host: "localhost".into(),
        port: 5432,
        name: "mydb".into(),
        username: "postgres".into(),
        password: Some("password".into()),
        tls: TlsConfig { enabled: false, trusted_root_certs: String::new() },
    };

    let store = MemoryStore::new();
    let destination = MemoryDestination::new();

    let config = PipelineConfig {
        id: 1,
        publication_name: "my_publication".into(),
        pg_connection: pg,
        batch: BatchConfig { max_size: 1000, max_fill_ms: 5000 },
        table_error_retry_delay_ms: 10_000,
        table_error_retry_max_attempts: 5,
        max_table_sync_workers: 4,
    };

    let mut pipeline = Pipeline::new(config, store, destination);
    pipeline.start().await?;
    // pipeline.wait().await?; // 可选：阻塞直到完成

    Ok(())
}
```

有关教程和更深入的指导，请参阅 [文档](https://supabase.github.io/etl) 或查看 [示例](https://github.com/supabase/etl/tree/main/etl-examples)。

## 目的地

ETL 设计为可扩展。您可以实现自己的目的地将数据发送到任何您喜欢的地方，但它附带了一些内置目的地：

- BigQuery

开箱即用的目的地在 `etl-destinations` crate 中可用：

```toml
[dependencies]
etl = { git = "https://github.com/supabase/etl" }
etl-destinations = { git = "https://github.com/supabase/etl", features = ["bigquery"] }
```

## 许可证

Apache-2.0。详见 `LICENSE`。

---

由 [Supabase](https://supabase.com) 团队用 ❤️ 制作
