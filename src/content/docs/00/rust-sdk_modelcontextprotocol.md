---
title: Rust Sdk
---

# rust-sdk

## 功能介绍

rust-sdk 是 Model Context Protocol (MCP) 的官方 Rust SDK 实现，使用 tokio 异步运行时。该项目提供了构建 MCP 客户端和服务器的核心功能，支持通过 JSON-RPC 2.0 协议进行通信。

主要组件包括：

- **rmcp**: 核心 crate，提供 RMCP 协议实现
- **rmcp-macros**: 过程宏 crate，用于生成 RMCP 工具实现

## 用法

### 导入 crate

在 `Cargo.toml` 中添加依赖：

```toml
rmcp = { version = "0.8.0", features = ["server"] }
# 或者使用开发版本
rmcp = { git = "https://github.com/modelcontextprotocol/rust-sdk", branch = "main" }
```

### 第三方依赖

基本依赖：

- [tokio](https://github.com/tokio-rs/tokio) (必需)
- [serde](https://github.com/serde-rs/serde) (必需)

### 构建客户端

```rust
use rmcp::{ServiceExt, transport::{TokioChildProcess, ConfigureCommandExt}};
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = ().serve(TokioChildProcess::new(Command::new("npx").configure(|cmd| {
        cmd.arg("-y").arg("@modelcontextprotocol/server-everything");
    }))?).await?;
    Ok(())
}
```

### 构建服务器

1. 构建传输层：

```rust
use tokio::io::{stdin, stdout};
let transport = (stdin(), stdout());
```

2. 构建服务：

```rust
let service = common::counter::Counter::new();
```

3. 启动服务器：

```rust
let server = service.serve(transport).await?;
```

4. 与服务器交互：

```rust
// 请求
let roots = server.list_roots().await?;

// 发送通知
server.notify_cancelled(...).await?;
```

5. 等待服务关闭：

```rust
let quit_reason = server.waiting().await?;
// 或者取消
let quit_reason = server.cancel().await?;
```

更多示例请参考 [examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples) 目录。

## OAuth 支持

详情请参考 [OAuth 支持文档](https://github.com/modelcontextprotocol/rust-sdk/blob/main/docs/OAUTH_SUPPORT.md)。

## 相关资源

- [MCP 规范](https://spec.modelcontextprotocol.io/specification/2024-11-05/)
- [Schema](https://github.com/modelcontextprotocol/specification/blob/main/schema/2024-11-05/schema.ts)
