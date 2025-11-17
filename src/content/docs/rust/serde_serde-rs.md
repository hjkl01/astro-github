---
title: serde
---

# Serde

Serde 是一个用于 Rust 的高效且通用的序列化和反序列化框架。它允许你将 Rust 数据结构转换为各种格式（如 JSON、YAML 等），并从这些格式中恢复数据。

## 功能

- **高效序列化**：Serde 提供了高性能的序列化和反序列化功能，支持多种数据格式。
- **通用性**：通过 trait 系统，可以轻松扩展到新的数据格式。
- **自动派生**：使用 `#[derive(Serialize, Deserialize)]` 宏，可以自动为结构体和枚举生成序列化代码。
- **零拷贝**：在可能的情况下，Serde 支持零拷贝反序列化。
- **自定义格式**：支持自定义序列化器和反序列化器。

## 用法

### 1. 添加依赖

在你的 `Cargo.toml` 文件中添加以下依赖：

```toml
[dependencies]
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```

### 2. 定义数据结构

使用 `#[derive(Serialize, Deserialize)]` 为你的结构体或枚举添加序列化支持：

```rust
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
struct Point {
    x: i32,
    y: i32,
}
```

### 3. 序列化

将数据结构转换为字符串（例如 JSON）：

```rust
let point = Point { x: 1, y: 2 };
let serialized = serde_json::to_string(&point).unwrap();
println!("serialized = {}", serialized); // 输出: {"x":1,"y":2}
```

### 4. 反序列化

从字符串恢复数据结构：

```rust
let deserialized: Point = serde_json::from_str(&serialized).unwrap();
println!("deserialized = {:?}", deserialized); // 输出: Point { x: 1, y: 2 }
```

### 支持的数据格式

Serde 支持多种数据格式，包括但不限于：

- JSON (serde_json)
- YAML (serde_yaml)
- TOML (serde_toml)
- CBOR (serde_cbor)
- MessagePack (serde_msgpack)

更多信息请参考 [Serde 官网](https://serde.rs/)。
