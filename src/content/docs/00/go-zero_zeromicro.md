
---
title: go-zero
---


# go-zero —— 高性能、易用的微服务框架

**项目地址**: https://github.com/zeromicro/go-zero

---

## 1. 项目简介

go-zero 是一个基于 Go 语言的微服务框架，主打 **高性能**、**易用**、**可扩展**。采用零配置（zero configuration）理念，提供丰富的工具链与 SDK，支持 gRPC、HTTP、Redis、Kafka、MySQL、SQL Server、PostgreSQL 等多种技术栈。

---

## 2. 主要特性

| 特性 | 描述 |
|------|------|
| **零配置** | 项目通过 `zncfg` 或 `go-zero` CLI 自动生成配置文件与代码 |
| **支持多协议** | 同时支持 HTTP、gRPC，且能做双向桥接 |
| **高效的服务治理** | 内置服务注册、发现（Consul、Nacos、etcd）、负载均衡、熔断、限流 |
| **可插拔中间件** | 全链路追踪（OpenTracing、OpenTelemetry）、日志、监控、鉴权 |
| **声明式数据访问** | `sqlx` 与 `gen` 代码生成器，实现 ORM 与手写 SQL 的统一 |
| **异步任务** | 集成 Kafka、RabbitMQ，支持任务调度（cron、delay） |
| **服务化开发** | 自动生成 API 文档（Swagger）、Req/Res 模式、请求校验、错误统一处理 |
| **可扩展插件** | 通过插件体系可在不改代码的情况下扩展如插件化配置、插件化鉴权 |

---

## 3. 功能亮点

- **快速启动**：`goctl api new`, `goctl api serve` 一键生成 REST API；`goctl rpc new`, `goctl rpc serve` 一键生成 gRPC 服务。  
- **自动化代码生成**：`goctl biz new` 生成业务逻辑层，`goctl api query`/`goctl api _add` 自动生成查询/增删改代码。  
- **全链路监控**：内置 Prometheus、Zipkin，支持自定义监控与日志。  
- **安全鉴权**：JWT/MD5/自定义中间件一键集成。  
- **分布式事务**：可结合 TCC、SAGA 或基于 RocketMQ 的唯一事务。  
- **快捷部署**：支持 Dockerfile、Kubernetes manifests、Helm Chart，配合 `helm chart` 生成一键发布。

---

## 4. 快速入门

### 4.1 安装 CLI（goctl）

```bash
# macOS / Linux
curl -sL https://install.goharbor.io/goctl | bash

# Windows
powershell -c "iwr https://install.goharbor.io/goctl | iex"
```

### 4.2 创建一个 HTTP API

```bash
# 1. 新建 API 项目
goctl api new blog_api

# 2. 进入目录
cd blog_api

# 3. 生成 API 代码
goctl api go

# 4. 运行
go run main.go
```

访问 `http://localhost:8888/api/v1/hello?name=world` 将返回 `{"msg":"Hello world!"}`。

### 4.3 创建一个 gRPC 服务

```bash
# 1. 新建 RPC 项目
goctl rpc new blog_rpc

cd blog_rpc
goctl rpc go

go run main.go
```

调用 gRPC client：

```go
conn, _ := grpc.Dial("localhost:8888", grpc.WithInsecure())
client := pb.NewBlogServiceClient(conn)
resp, _ := client.GetArticle(context.Background(), &pb.GetArticleRequest{Id: 1})
```

---

## 5. 进阶使用

### 5.1 服务治理

```bash
# Consul 注册
export SERVICE_REGISTRY=consul
export SERVICE_REGISTRY_ADDRESS="http://127.0.0.1:8500"
```

go-zero 会自动将服务注册到 Consul，并通过 Consul 进行服务发现。

### 5.2 使用插件化钩子

```go
import (
    "github.com/zeromicro/go-zero/core/hook/goroutine"
)

func main() {
    p := goroutine.NewGoroutineHook()
    // 在这里添加自定义跨进程、错误处理等逻辑
}
```

---

## 6. 运行与调试

| 环境 | 指令 |
|------|------|
| **Docker** | `docker build -t blog_api . && docker run -p 8888:8888 blog_api` |
| **Kubernetes** | `kubectl apply -f deploy`（查看 `deploy/` 目录） |
| **本地单元测试** | `go test ./...` |
| **覆盖率** | `go test -cover ./...` |

---

## 7. 贡献

```
git clone https://github.com/zeromicro/go-zero.git
cd go-zero
make install
make test
```

请遵循项目的 [CONTRIBUTING](https://github.com/zeromicro/go-zero/blob/master/CONTRIBUTING.md) 文档。

---

## 8. 常见问题

- **为什么 `goctl` 生成的代码比较多？**  
  go-zero 追求**规范**和**安全**，代码量虽大但分层清晰，易于维护。

- **如何迁移到 Kubernetes？**  
  `goctl deploy microcluster` 可自动生成 n 个 Kubernetes YAML 文件。

- **支持多语言？**  
  go-zero 仅支持 Go；若需要多语言，目前官方并无计划。

---

**项目地址**: https://github.com/zeromicro/go-zero

