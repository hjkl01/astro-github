
---
title: grpc-go
---

## grpc-go

> 项目地址: https://github.com/grpc/grpc-go

### 主要特性

- Go 原生实现的 gRPC 框架，兼容官方 gRPC 协议
- 基于 HTTP/2，支持流式传输与连接复用
- 自动生成 Go 代码：`protoc --go_out=. --go-grpc_out=.`
- 支持 Unary 与 Stream RPC
- 可插拔拦截器、负载均衡、负载隔离
- 统一的错误码体系，兼容 gRPC 官方错误码
- 认证支持 TLS、mTLS、JWT、OAuth 等多种方式
- 丰富的 Metadata 与 Trailing Metadata 用法
- 轻量、易用的客户端与服务器 API

### 功能

- **Server** 与 **Client** 基本用法
- `proto` 文件定义、代码生成
- 双向流、服务器流、客户端流
- 拦截器 (`UnaryInterceptor`, `StreamInterceptor`)
- 负载均衡（RoundRobin、logic、层级）
- KeepAlive、心跳、超时控制
- Metadata 的传递
- 大文件与分块下载/上传

### 用法示例

```bash
# 安装依赖
go get google.golang.org/grpc

# 编写 proto
# greeter.proto
syntax = "proto3";

package greet;
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}
message HelloRequest { string name = 1; }
message HelloReply { string message = 1; }

# 生成 gRPC 代码
protoc --go_out=. --go-grpc_out=. greeter.proto

# 服务器实现（部分）
import (
  "google.golang.org/grpc"
  "net"
  greetpb "path/to/generated/package"
)

type server struct{ greetpb.UnimplementedGreeterServer }

func (s *server) SayHello(ctx context.Context, in *greetpb.HelloRequest) (*greetpb.HelloReply, error) {
  return &greetpb.HelloReply{Message: "Hello " + in.Name}, nil
}

func main() {
  lis, _ := net.Listen("tcp", ":50051")
  grpcServer := grpc.NewServer()
  greetpb.RegisterGreeterServer(grpcServer, &server{})
  grpcServer.Serve(lis)
}

# 客户端调用（部分）
conn, _ := grpc.Dial("localhost:50051", grpc.WithInsecure())
client := greetpb.NewGreeterClient(conn)
resp, _ := client.SayHello(context.Background(), &greetpb.HelloRequest{Name: "world"})
fmt.Println(resp.Message)
```

---