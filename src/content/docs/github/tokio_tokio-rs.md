
---
title: tokio
---


# Tokio
**项目地址**：[https://github.com/tokio-rs/tokio](https://github.com/tokio-rs/tokio)

## 主要特性
- **Async运行时**：高效的多线程（或单线程）任务调度器，支持非阻塞 I/O。
- **I/O 框架**：异步网络、文件、管道等 I/O API。
- **时间与计时器**：定时器、间隔、闹钟等。
- **同步原语**：`Mutex`, `RwLock`, `Semaphore`, `Barrier` 等。
- **通道（Channels）**：`mpsc`, `broadcast`, `watch`。
- **Process & Signal 处理**：异步进程管理与信号监听。
- **特性模块**：`full`, `net`, `time`, `sync`, `io-util`, `rt-multi-thread`, `rt-core` 等按需启用。

## 核心功能
| 类别 | 功能 | 代码示例 |
|------|------|---------|
| 任务调度 | 创建、等待并发任务 | `tokio::spawn(async { /* ... */ });` |
| I/O | TCP/UDP 连接 | `TcpStream::connect("127.0.0.1:8080").await?;` |
| 时间 | 延迟与周期操作 | `tokio::time::sleep(Duration::from_secs(1)).await;` |
| 通道 | 发送与接收 | `let (tx, mut rx) = mpsc::channel(32);` |
| 同步 | 互斥锁 | `let lock = Mutex::new(0);` |
| 进程 | async Fork & Exec | `Command::new("sleep").arg("1").spawn().await?;` |

## 快速使用
1. **添加依赖**  
   `Cargo.toml`  
   ```toml
   [dependencies]
   tokio = { version = "1", features = ["full"] }
   ```

2. **初始化运行时**  
   ```rust
   #[tokio::main]
   async fn main() -> Result<(), Box<dyn std::error::Error>> {
       // ejemplo...
       Ok(())
   }
   ```

3. **异步任务示例**  
   ```rust
   #[tokio::main]
   async fn main() {
       let handle = tokio::spawn(async {
           println!("Hello from async task!");
       });

       handle.await.unwrap(); // 等待任务完成
   }
   ```

4. **异步网络示例（Echo 服务器）**  
   ```rust
   use tokio::net::TcpListener;
   use tokio::io::{AsyncReadExt, AsyncWriteExt};

   #[tokio::main]
   async fn main() -> std::io::Result<()> {
       let listener = TcpListener::bind("127.0.0.1:8080").await?;
       loop {
           let (mut socket, _) = listener.accept().await?;
           tokio::spawn(async move {
               let mut buf = [0u8; 1024];
               loop {
                   let n = match socket.read(&mut buf).await {
                       Ok(n) if n == 0 => return, // 连接关闭
                       Ok(n) => n,
                       Err(_) => return,
                   };
                   if socket.write_all(&buf[..n]).await.is_err() { break; }
               }
           });
       }
   }
   ```

5. **错误处理**  
   通过 `?` 传播，并可使用 `tokio::try_join!` 等宏同时等待任务。

## 文档与资源
- 官方文档: https://docs.rs/tokio/
- 示例与教程: https://tokio.rs/docs
- 社区与讨论: GitHub Issues, Discord

此 Markdown 文件已包含在 `src/content/docs/00/tokio_tokio-rs.md` 路径下，可直接使用或进一步扩充。