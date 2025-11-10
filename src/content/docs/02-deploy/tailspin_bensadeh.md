---
title: tailspin
---


# Tailspin (ben‑sadeh)

> **GitHub 地址**: <https://github.com/bensadeh/tailspin>

## 项目简介
Tailspin 是一个用 Rust 编写的灵活高效的 **流式转发/缓冲** 库。它可以把输入流（文件、网络、标准输入等）按块或行处理，并能与多种异步/同步环境无缝集成。该项目适用于日志分析、实时数据管道和 CLI 工具等场景。

## 主要特性

| 序号 | 特性 | 说明 |
|------|------|------|
| 1 | **零成本抽象** | 通过 Rust 的标准 Iterator、async-stream 等接口，做到不引入额外运行时开销。 |
| 2 | **多种缓冲策略** | 支持行缓冲 (`lines()`)、块缓冲 (`chunks()`)、自定义缓冲大小。 |
| 3 | **同步与异步兼容** | 同步迭代器 `Iterator` 和异步迭代器 `Stream` 两种实现，任选其一。 |
| 4 | **跨平台** | 纯 Rust 实现，无 C 绑定，支持 Linux、macOS、Windows。 |
| 5 | **可配置延迟** | 通过 `sleep`、`delay` 或自定义 `Future` 对数据流进行节流，适配网络 I/O。 |
| 6 | **CLI 模式** | `tailspin <文件名>` 能快速查看文件尾部数据，类似 `tail -f`。 |

## 主 API

```rust
use tailspin::{TailSpin, TailSpinOptions};

/// 同步从文件读取首 10 行
let options = TailSpinOptions::new().lines(10);
for line in TailSpin::from_file("log.txt", options).iter() {
    println!("{}", line);
}

/// 异步读取流并限速
use futures::{stream::StreamExt, executor::block_on};
use std::time::Duration;

let async_source = async {
    let mut tail = TailSpin::from_reader(reader, TailSpinOptions::default().chunks(1024));
    while let Some(chunk) = tail.next().await {
        process(chunk).await;
        futures_timer::Delay::new(Duration::from_millis(50)).await; // 节流
    }
};
block_on(async_source);
```

### `TailSpinOptions`

| 方法 | 作用 |
|------|------|
| `lines(n)` | 读取固定行数 |
| `chunks(size)` | 读取固定字节数 |
| `delay(dur)` | 每次读取间隔时间 |
| `prefetch(n)` | 预取缓冲条数 |
| `encoding(Enc)` | 指定文本编码（default UTF‑8） |

### `TailSpin::from_file` / `from_reader`

- `from_file(path, options)` 读取文件路径。
- `from_reader(reader, options)` 读取任意 `Read + Seek`。

### `skip(n)`

对于同步迭代器可以跳过前 `n` 行/块；异步版本同理。

## 用法示例

### 安装

```bash
cargo add tailspin
```

### 在 Rust 项目中使用

```rust
use tailspin::TailSpin;

fn main() {
    tail = TailSpin::from_file("data.txt", Default::default());
    for entry in tail {
        println!("{}", String::from_utf8_lossy(&entry));
    }
}
```

### CLI

```bash
# 查看文件前 5 行
tailspin --lines 5 data.txt

# 持续跟踪文件末尾（类似 tail -f）
tailspin --follow data.log
```

### 集成至流式数据管道

```rust
use futures::{stream::TryStreamExt, executor::block_on};
use tailspin::TailSpin;

let source = async {
    let mut tail = TailSpin::from_stream(url_stream, Default::default());
    while let Some(data) = tail.try_next().await? {
        // 处理每一个 চ​块或者行
        process_packet(data).await?;
    }
    Ok::<(), Box<dyn std::error::Error>>(())
};
block_on(source).expect("failed");
```

## 贡献

本项目采用 MIT 许可证。欢迎 Issue、Pull Request 与社区一起扩展功能。

---
*以上内容基于对 `bensadeh/tailspin` 仓库的公开信息整理。若版本更新，功能列表与示例请以仓库最新 README 为准。*
