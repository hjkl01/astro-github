
---
title: rust
---


# Rust（rust-lang/rust）

**项目地址**: https://github.com/rust-lang/rust

## 主要特性

- **内存安全** – 通过所有权、借用与生命周期机制，消除空指针、悬挂指针和数据竞争。
- **零成本抽象** – 高层抽象（如迭代器、闭包）在编译期被展开为等价于手写循环的代码。
- **并发友好** – 轻量级线程(`std::thread`)与无锁并发原语(`Mutex`, `RwLock`, `Atomic*`)。
- **跨平台** – 支持 Windows、macOS、Linux 及多种嵌入式系统。
- **包管理与构建工具** – `cargo` 为一站式依赖解析、构建、测试、发布。
- **工具链生态** – `rustc`（编译器）、`rustfmt`（代码格式化）、`clippy`（代码审查）、`rust-analyzer`（IDE 语言服务器）等。

## 核心功能

| 功能 | 说明 |
|------|------|
| **编译器 (`rustc`)** | 将 `.rs` 源码编译为机器码或 WebAssembly。 |
| **包管理 (`cargo`)** | 依赖管理、构建、测试、文档生成、发布到 `crates.io`。 |
| **标准库 (`std`)** | 包含集合、I/O、网络、线程、同步、时间、字符串等常用功能。 |
| **宏系统** | 递归宏、属性宏、过程宏，实现代码生成与编译时检查。 |
| **错误处理** | `Result<T, E>` 与 `?` 操作符，鼓励显式错误处理。 |
| **泛型与特征（Traits）** | 静态多态，支持泛型函数、结构体与特征实现。 |
| **异步编程** | `async`/`await` 与 `Future`，配合 `tokio`、`async-std` 等运行时。 |

## 基本用法

```bash
# 安装 Rust 工具链
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 创建新项目
cargo new hello_world
cd hello_world

# 编译并运行
cargo run

# 生成文档
cargo doc --open

# 运行测试
cargo test
```

### 代码示例

```rust
// hello_world/src/main.rs
fn main() {
    println!("Hello, world!");
}
```

### 错误处理示例

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_file(path: &str) -> Result<String, io::Error> {
    let mut file = File::open(path)?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    Ok(contents)
}
```

### 泛型与 trait 示例

```rust
fn longest<T: std::fmt::Debug>(x: T, y: T) -> T {
    // 这里的逻辑可以根据需要实现
    x
}
```

### 异步编程示例

```rust
use tokio::net::TcpStream;

#[tokio::main]
async fn main() {
    let stream = TcpStream::connect("127.0.0.1:8080").await.unwrap();
    // 处理流
}
```

## 文档与社区

- 官方文档: https://doc.rust-lang.org/
- 生态库: https://crates.io/
- Rust 社区: https://users.rust-lang.org/
- 相关博客与教程: https://www.rust-lang.org/learn

--- 

> 以上内容为简要概述，欲深入了解请参考官方文档与源码。