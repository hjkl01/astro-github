# tonic_hyperium

## 项目简介

`tonic` 是一个原生的 gRPC 客户端和服务器实现，支持 async/await。它专注于高性能、互操作性和灵活性，是用 Rust 编写生产系统的基础构建块。

## 主要功能

- **双向流式传输**：支持 gRPC 的双向流式 RPC。
- **高性能异步 I/O**：基于 Tokio 栈，提供高效的异步操作。
- **互操作性**：与 gRPC 规范完全兼容。
- **TLS 支持**：使用 rustls 提供 TLS 加密。
- **负载均衡**：内置负载均衡功能。
- **自定义元数据**：支持自定义 gRPC 元数据。
- **认证**：支持各种认证机制。
- **健康检查**：实现标准的 gRPC 健康检查服务。

## 用法

### 快速开始

1. **安装依赖**：在 `Cargo.toml` 中添加 `tonic` 和相关依赖。

   ```toml
   [dependencies]
   tonic = "0.14"
   prost = "0.13"
   ```

2. **定义服务**：使用 Protocol Buffers 定义 gRPC 服务。

3. **生成代码**：使用 `tonic-build` 从 `.proto` 文件生成 Rust 代码。

   ```rust
   tonic_build::compile_protos("proto/echo.proto")?;
   ```

4. **实现服务器**：

   ```rust
   use tonic::{transport::Server, Request, Response, Status};

   // 实现生成的 trait
   #[tonic::async_trait]
   impl Echo for MyEcho {
       async fn echo(&self, request: Request<EchoRequest>) -> Result<Response<EchoResponse>, Status> {
           // 处理请求
       }
   }

   #[tokio::main]
   async fn main() -> Result<(), Box<dyn std::error::Error>> {
       let addr = "[::1]:50051".parse()?;
       let echo = MyEcho::default();

       Server::builder()
           .add_service(EchoServer::new(echo))
           .serve(addr)
           .await?;

       Ok(())
   }
   ```

5. **实现客户端**：

   ```rust
   use tonic::transport::Channel;

   #[tokio::main]
   async fn main() -> Result<(), Box<dyn std::error::Error>> {
       let channel = Channel::from_static("http://[::1]:50051").connect().await?;
       let mut client = EchoClient::new(channel);

       let request = tonic::Request::new(EchoRequest { message: "hello".into() });
       let response = client.echo(request).await?;

       println!("RESPONSE={:?}", response);

       Ok(())
   }
   ```

### 教程和示例

- **Hello World 教程**：基本示例，适合初学者。
- **Route Guide 教程**：完整示例，展示所有功能。
- **示例代码**：在 `examples/` 目录中查看更多示例，包括 TLS、负载均衡和双向流式传输。

## 项目结构

- `tonic`：通用 gRPC 和 HTTP/2 客户端/服务器实现。
- `tonic-build`：基于 prost 的服务代码生成。
- `tonic-types`：gRPC 工具类型，包括知名类型支持。
- `tonic-health`：标准 gRPC 健康检查服务实现。
- `tonic-reflection`：gRPC 反射实现。
- `examples`：展示各种功能的示例。
- `interop`：互操作性测试。

## 许可证

MIT License
