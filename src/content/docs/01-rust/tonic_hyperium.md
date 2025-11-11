---
title: tonic
---

# tonic

## 简介

`tonic` 是 Rust 语言中一个原生的 gRPC 客户端和服务器实现，支持 async/await。它专注于高性能、互操作性和灵活性，是基于 `hyper` 和 `tokio` 构建的，用于生产系统的核心构建块。

## 功能

- **双向流式传输**：支持 gRPC 的双向流式 RPC。
- **高性能异步 I/O**：基于 Tokio 的异步运行时，提供高效的网络 I/O。
- **互操作性**：与 gRPC 规范完全兼容，支持与其他语言的 gRPC 服务交互。
- **TLS 支持**：基于 `rustls` 的 TLS 加密。
- **负载均衡**：内置负载均衡功能。
- **自定义元数据**：支持自定义请求和响应元数据。
- **认证**：支持各种认证机制。
- **健康检查**：实现标准的 gRPC 健康检查服务。

## 用法

### 依赖

在 `Cargo.toml` 中添加：

```toml
[dependencies]
tonic = "0.14"
prost = "0.13"

[build-dependencies]
tonic-build = "0.14"
```

### 定义服务

使用 Protocol Buffers 定义服务，例如 `hello.proto`：

```protobuf
syntax = "proto3";

package hello;

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

### 生成代码

在 `build.rs` 中：

```rust
fn main() -> Result<(), Box<dyn std::error::Error>> {
    tonic_build::compile_protos("proto/hello.proto")?;
    Ok(())
}
```

### 实现服务器

```rust
use tonic::{transport::Server, Request, Response, Status};

pub mod hello {
    tonic::include_proto!("hello");
}

use hello::{greeter_server::{Greeter, GreeterServer}, HelloRequest, HelloReply};

#[derive(Default)]
pub struct MyGreeter {}

#[tonic::async_trait]
impl Greeter for MyGreeter {
    async fn say_hello(
        &self,
        request: Request<HelloRequest>,
    ) -> Result<Response<HelloReply>, Status> {
        let reply = HelloReply {
            message: format!("Hello {}!", request.into_inner().name),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    let greeter = MyGreeter::default();

    Server::builder()
        .add_service(GreeterServer::new(greeter))
        .serve(addr)
        .await?;

    Ok(())
}
```

### 实现客户端

```rust
use hello::{greeter_client::GreeterClient, HelloRequest};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = GreeterClient::connect("http://[::1]:50051").await?;

    let request = tonic::Request::new(HelloRequest {
        name: "Tonic".into(),
    });

    let response = client.say_hello(request).await?;

    println!("RESPONSE={:?}", response);

    Ok(())
}
```

更多示例请参考 [官方文档](https://docs.rs/tonic) 和 [GitHub 示例](https://github.com/hyperium/tonic/tree/master/examples)。
