---
title: Tracing
---

# tracing_tokio-rs

## 项目简介

tracing 是 Tokio 项目维护的一个用于 Rust 程序的结构化、事件驱动诊断信息的框架。它允许开发者收集和记录应用程序的跟踪数据，如日志、性能指标等，而不依赖于 Tokio 运行时。

## 主要功能

- **结构化日志记录**：提供宏来创建事件和跨度（spans），支持字段和元数据。
- **跨度管理**：允许嵌套跨度来跟踪代码执行的层次结构。
- **异步支持**：特别适合异步 Rust 代码，支持 `async fn` 的自动仪器化。
- **兼容性**：与 `log` crate 兼容，可以消费 log 库发出的消息。
- **可扩展性**：通过 Subscriber 接口支持自定义收集器，如日志输出、文件写入、远程发送等。

## 用法

### 在应用程序中使用

应用程序需要使用一个兼容 `tracing` 的 `Subscriber` 来收集跟踪数据。`tracing-subscriber` 提供了默认的日志 Subscriber。

1. 添加依赖：

```toml
[dependencies]
tracing = "0.1"
tracing-subscriber = "0.3"
```

2. 初始化 Subscriber 并记录事件：

```rust
use tracing::{info, Level};
use tracing_subscriber;

fn main() {
    // 安装全局 Subscriber，根据 RUST_LOG 环境变量配置
    tracing_subscriber::fmt::init();

    let number_of_yaks = 3;
    // 创建一个新事件
    info!(number_of_yaks, "preparing to shave yaks");

    let number_shaved = shave_all(number_of_yaks);
    info!(
        all_yaks_shaved = number_shaved == number_of_yaks,
        "yak shaving completed."
    );
}
```

### 在库中使用

库应仅依赖 `tracing` crate，使用宏来收集信息，而不安装 Subscriber。

```rust
use tracing::{debug, error, info, span, warn, Level};

// 使用 #[tracing::instrument] 属性自动创建和进入跨度
#[tracing::instrument]
pub fn shave(yak: usize) -> Result<(), Box<dyn std::error::Error + 'static>> {
    debug!(excitement = "yay!", "hello! I'm gonna shave a yak.");
    if yak == 3 {
        warn!("could not locate yak!");
        return Err(std::io::Error::new(std::io::ErrorKind::Other, "shaving yak failed!").into());
    } else {
        debug!("yak shaved successfully");
    }
    Ok(())
}

pub fn shave_all(yaks: usize) -> usize {
    // 创建一个新跨度
    let span = span!(Level::TRACE, "shaving_yaks", yaks);
    let _enter = span.enter();

    info!("shaving yaks");

    let mut yaks_shaved = 0;
    for yak in 1..=yaks {
        let res = shave(yak);
        debug!(yak, shaved = res.is_ok());

        if let Err(ref error) = res {
            error!(yak, error = error.as_ref(), "failed to shave yak!");
        } else {
            yaks_shaved += 1;
        }
    }

    yaks_shaved
}
```

### 在异步代码中使用

对于 `async fn`，推荐使用 `#[instrument]` 属性：

```rust
use tracing::{info, instrument};
use tokio::{io::AsyncWriteExt, net::TcpStream};
use std::io;

#[instrument]
async fn write(stream: &mut TcpStream) -> io::Result<usize> {
    let result = stream.write(b"hello world\n").await;
    info!("wrote to stream; success={:?}", result.is_ok());
    result
}
```

对于一般的 Future，可以使用 `Future::instrument`：

```rust
use tracing::Instrument;

let my_future = async {
    // ...
};

my_future
    .instrument(tracing::info_span!("my_future"))
    .await
```

## 相关生态

tracing 有丰富的生态系统，包括：

- `tracing-subscriber`：Subscriber 实现和工具。
- `tracing-appender`：输出工具，如文件追加器。
- `tracing-futures`：Future 仪器化工具。
- `tracing-attributes`：过程宏属性。
- 以及许多第三方集成，如与 Actix、Axum、Sentry 等框架的集成。

更多信息请访问 [tracing.rs](https://tracing.rs)。
