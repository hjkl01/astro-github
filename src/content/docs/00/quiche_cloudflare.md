
---
title: quiche
---


# Cloudflare Quiche

> **项目地址**：<https://github.com/cloudflare/quiche>

## 1. 项目简介

Quiche 是 Cloudflare 开发的一套用 Rust 编写的 QUIC（Quick UDP Internet Connections）协议栈，提供了完整的 QUIC 服务器与客户端实现，并支持 HTTP/3。它兼容 Rust 的生态系统，利用 Rust 的安全性与高性能特点，适合构建需要低延迟、高吞吐量网络服务的项目。

## 2. 主要特性

| 特性 | 说明 |
|------|------|
| **纯 Rust 实现** | 代码不依赖任何 C/C++ 绑定，易于维护与安全审计 |
| **完整 QUIC 协议栈** | 支持 IETF QUIC 规范的所有核心功能：多路复用、流层、拥塞控制、加密 |
| **HTTP/3 支持** | 内置 HTTP/3 处理器，能够快速构建 HTTP/3 服务器/客户端 |
| **TLS 1.3 集成** | 使用 Rustls / OpenSSL 进行 TLS 握手，支持 0-RTT |
| **可扩展性** | 可通过特性标志编译不同功能（例如仅 QUIC、仅 HTTP/3 等） |
| **性能优异** | 采用零拷贝、异步 I/O（async-std / tokio）实现，适合高并发场景 |
| **跨平台** | 支持 Linux、macOS、Windows 等主流操作系统 |

## 3. 安装与编译

```bash
# 克隆仓库
git clone https://github.com/cloudflare/quiche.git
cd quiche

# 安装 Rust 工具链（如果尚未安装）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# 编译库（默认启用所有特性）
cargo build --release
```

如果想更轻量，只编译 QUIC 核心：

```bash
cargo build --release --features quic
```

## 4. 基本使用示例

### 4.1 服务器端

```rust
use quiche::{Connection, Config};
use std::net::UdpSocket;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 服务器配置
    let mut config = Config::new(quiche::PROTOCOL_VERSION)?;
    config.set_application_protos(b"\x05h3-29")?; // HTTP/3
    config.set_max_idle_timeout(5000);
    config.set_initial_max_data(10_000_000);
    config.set_initial_max_stream_data_bidi_local(1_000_000);
    config.set_initial_max_streams_bidi(100);
    config.set_initial_max_streams_uni(0);
    config.set_enable_early_data(true);

    // 生成服务器私钥
    let cert = std::fs::read("cert.pem")?;
    let key = std::fs::read("key.pem")?;
    config.load_cert_chain(&cert)?;
    config.load_priv_key(&key)?;

    // UDP 监听
    let socket = UdpSocket::bind("0.0.0.0:4433")?;
    let mut buf = [0; 1350];

    loop {
        let (len, src) = socket.recv_from(&mut buf)?;
        let mut conn = Connection::accept(&src, &mut config)?;
        conn.recv(&buf[..len])?;

        // 处理数据...
        // 发送响应
        let data = b"Hello, QUIC!";
        conn.send(data)?;
        socket.send_to(conn.send_data(), &src)?;
    }
}
```

### 4.2 客户端

```rust
use quiche::{Config, Connection, Error};
use std::net::UdpSocket;

fn main() -> Result<(), Error> {
    let mut config = Config::new(quiche::PROTOCOL_VERSION)?;
    config.set_application_protos(b"\x05h3-29")?;
    config.set_max_idle_timeout(5000);
    config.set_initial_max_data(10_000_000);
    config.set_initial_max_stream_data_bidi_local(1_000_000);
    config.set_initial_max_streams_bidi(100);
    config.set_initial_max_streams_uni(0);

    // 服务器地址
    let dst = "127.0.0.1:4433".parse().unwrap();
    let src = "0.0.0.0:0".parse().unwrap();
    let socket = UdpSocket::bind(src)?;
    socket.connect(dst)?;

    // 发起连接
    let mut conn = Connection::connect(&dst, "example.com", &mut config)?;
    socket.send_to(conn.send_data(), &dst)?;

    // 发送请求
    conn.stream_send(0, b"GET / HTTP/3\r\n\r\n", true)?;
    socket.send_to(conn.send_data(), &dst)?;

    // 接收响应
    let mut buf = [0; 1350];
    loop {
        let len = socket.recv(&mut buf)?;
        conn.recv(&buf[..len])?;
        if conn.is_closed() { break; }
    }

    Ok(())
}
```

## 5. 常用命令行工具

- `quiche-h3`：HTTP/3 客户端工具，支持 GET/POST 请求。
- `quiche-server`：示例服务器，可通过 `--cert`、`--key` 指定 TLS 证书。

```bash
# 安装
cargo install quiche

# 运行示例服务器
quiche-server --cert cert.pem --key key.pem
```

## 6. 文档与资源

- 官方文档：<https://docs.rs/quiche/>
- 示例代码：<https://github.com/cloudflare/quiche/tree/master/examples>
- 贡献指南：<https://github.com/cloudflare/quiche/blob/main/CONTRIBUTING.md>

---

> 以上内容已整理为 Markdown，保存路径为 `src/content/docs/00/quiche_cloudflare.md`。