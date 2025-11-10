---
title: Quiche
---

# quiche

## 功能介绍

quiche 是 Cloudflare 开发的 QUIC 传输协议和 HTTP/3 的 Rust 实现。它提供了一个低级 API，用于处理 QUIC 数据包和维护连接状态。应用程序负责处理 I/O（例如套接字）和支持定时器的事件循环。

### 主要特性

- **QUIC 协议支持**：实现 IETF 标准的 QUIC 传输协议。
- **HTTP/3 支持**：提供 HTTP/3 模块，用于在 QUIC 上发送和接收 HTTP 请求和响应。
- **低级 API**：允许精细控制连接和数据流。
- **跨平台**：支持多种平台，包括 Android、iOS 和 Docker。
- **C/C++ 绑定**：提供 C API，便于集成到其他语言。

### 使用场景

- Cloudflare 的边缘网络 HTTP/3 支持。
- Android 的 DNS over HTTP/3。
- curl 的 HTTP/3 集成。

## 用法

### 构建

需要 Rust 1.83 或更高版本。克隆仓库并构建：

```bash
git clone --recursive https://github.com/cloudflare/quiche
cd quiche
cargo build --examples
```

运行测试：

```bash
cargo test
```

### 基本使用

1. **配置连接**：创建 `Config` 对象，设置协议版本、ALPN 等。

```rust
let mut config = quiche::Config::new(quiche::PROTOCOL_VERSION)?;
config.set_application_protos(&[b"example-proto"]);
```

2. **建立连接**：
   - 客户端：`quiche::connect(Some(&server_name), &scid, local, peer, &mut config)?`
   - 服务端：`quiche::accept(&scid, None, local, peer, &mut config)?`

3. **处理数据包**：
   - 接收：`conn.recv(&mut buf[..read], recv_info)`
   - 发送：`conn.send(&mut out)`

4. **流数据**：
   - 发送：`conn.stream_send(0, b"hello", true)?`
   - 接收：遍历 `conn.readable()` 并调用 `conn.stream_recv(stream_id, &mut buf)`

### HTTP/3

使用 `quiche::h3` 模块进行 HTTP 请求和响应处理。

### 命令行工具

- 客户端：`cargo run --bin quiche-client -- https://example.com/`
- 服务端：`cargo run --bin quiche-server -- --cert cert.crt --key cert.key`

更多详情请参考 [官方文档](https://docs.quic.tech/quiche/)。
