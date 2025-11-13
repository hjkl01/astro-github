---
title: grpc-gateway_grpc-ecosystem
---

## 功能介绍

grpc-gateway 是一个 Google protocol buffers 编译器 protoc 的插件。它读取 protobuf 服务定义，并生成一个反向代理服务器，将 RESTful HTTP API 转换为 gRPC 调用。根据服务定义中的 `google.api.http` 注解生成服务器。

这允许您同时提供 gRPC 和 RESTful 风格的 API。

## 主要特性

- 生成 JSON API 处理程序
- 支持请求体、路径参数和查询字符串中的方法参数
- 支持枚举字段在路径参数中
- 将流式 API 映射到换行符分隔的 JSON 流
- 可选生成 OpenAPI (Swagger) v2 定义
- 支持通过 HTTP `Grpc-Timeout` 头设置 gRPC 超时
- 部分支持 gRPC API 配置文件作为注解的替代方案
- 自动将 PATCH 请求转换为带字段掩码的 gRPC 请求

## 安装

### 从源码编译

使用 Go Modules 管理依赖：

```bash
go install \
    github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway \
    github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2 \
    google.golang.org/protobuf/cmd/protoc-gen-go \
    google.golang.org/grpc/cmd/protoc-gen-go-grpc
```

确保 `$GOBIN` 在 `$PATH` 中。

### 下载二进制文件

从 [GitHub releases 页面](https://github.com/grpc-ecosystem/grpc-gateway/releases/latest) 下载预编译的二进制文件。

## 使用方法

### 1. 定义 gRPC 服务

使用 protocol buffers 定义服务：

```protobuf
syntax = "proto3";
package your.service.v1;
option go_package = "github.com/yourorg/yourprotos/gen/go/your/service/v1";

import "google/api/annotations.proto";

message StringMessage {
  string value = 1;
}

service YourService {
  rpc Echo(StringMessage) returns (StringMessage) {
    option (google.api.http) = {
      post: "/v1/example/echo"
      body: "*"
    };
  }
}
```

### 2. 生成 gRPC stubs

使用 buf 或 protoc 生成 stubs。

### 3. 实现 gRPC 服务

按常规方式实现服务。

### 4. 生成反向代理

使用 `protoc-gen-grpc-gateway` 生成反向代理代码。

### 5. 编写 HTTP 反向代理服务器入口点

```go
package main

import (
  "context"
  "flag"
  "net/http"

  "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
  "google.golang.org/grpc"
  "google.golang.org/grpc/credentials/insecure"

  gw "github.com/yourorg/yourrepo/proto/gen/go/your/service/v1/your_service"
)

var (
  grpcServerEndpoint = flag.String("grpc-server-endpoint", "localhost:9090", "gRPC server endpoint")
)

func run() error {
  ctx := context.Background()
  ctx, cancel := context.WithCancel(ctx)
  defer cancel()

  mux := runtime.NewServeMux()
  opts := []grpc.DialOption{grpc.WithTransportCredentials(insecure.NewCredentials())}
  err := gw.RegisterYourServiceHandlerFromEndpoint(ctx, mux, *grpcServerEndpoint, opts)
  if err != nil {
    return err
  }

  return http.ListenAndServe(":8081", mux)
}

func main() {
  flag.Parse()

  if err := run(); err != nil {
    panic(err)
  }
}
```

### 6. (可选) 生成 OpenAPI 定义

使用 `protoc-gen-openapiv2` 生成 Swagger 文件。

更多详细信息请参考官方文档：https://grpc-ecosystem.github.io/grpc-gateway/
