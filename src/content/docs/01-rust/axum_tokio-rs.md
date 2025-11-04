
---
title: axum
---


# Axum（tokio-rs/axum）

[GitHub 项目地址](https://github.com/tokio-rs/axum)

## 项目简介
Axum 是基于 Tokio 的 async/await Web 框架，目标是提供高性能、类型安全、可组合的 HTTP 服务器。

## 主要特性
- **类型安全**：Rust 的类型系统保证运行时错误最小化  
- **可组合**：路由、Extractor、Middleware 等组件可自由组合  
- **基于 Tower**：共享 Tower 的 Service 抽象，支持链式中间件、限流、超时、重试等  
- **高性能**：利用 Tokio 的事件循环和多线程调度，适合大并发场景  
- **易用**：简洁 API + 丰富示例，快速上手并且易于扩展

## 核心功能
| 功能 | 说明 |
|------|------|
| 路由 | 支持路径参数、查询参数、正则路径匹配等 |
| Extractors | `Path`, `Query`, `Json`, `Form`, `State` 等内置 Extractor，亦可自定义 Extractor |
| 中间件 | 通过 `tower_http` 或自定义 Service 实现日志、鉴权、错误处理等 |
| 静态文件 | `ServeDir`, `ServeFile` 快速提供静态资源 |
| WebSocket | `WebSocketUpgrade` 与 Tokio 的异步 I/O 整合 |
| OpenAPI | 与 `utoipa` 等结合可自动生成 API 规范 |
| 集成数据库 | 与 `sqlx`, `sea-orm`, `diesel` 等无缝对接 |

## 快速开始

```bash
cargo add axum
cargo add tower-http
cargo add tokio --features full
```

```rust
// src/main.rs
use axum::{
    routing::{get, post},
    Router, Json,
};
use serde::{Serialize};

#[derive(Serialize)]
struct Greeting {
    message: String,
}

async fn hello() -> Json<Greeting> {
    Json(Greeting {
        message: "Hello, Axum!".to_string(),
    })
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/", get(hello))
        .route("/echo", post(echo));

    axum::Server::bind(&"0.0.0.0:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}

async fn echo(Json(body): Json<serde_json::Value>) -> Json<serde_json::Value> {
    Json(body)
}
```

### 运行

```bash
cargo run
```

访问 <http://localhost:3000> 查看 "Hello, Axum!"。

## 目录结构示例

```
my_axum_app/
├─ Cargo.toml
├─ src/
│  ├─ main.rs
│  └─ ...
```

## 参考资料
- 官方文档: https://docs.rs/axum
- GitHub 仓库: https://github.com/tokio-rs/axum
