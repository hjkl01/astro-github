---
title: gofr
---

# GoFr

GoFr 是一个用于加速微服务开发的 Go 框架，提供内置的数据库和可观测性支持。

## 功能

- **简单 API 语法**：提供直观的 API 定义方式。
- **默认 REST 标准**：遵循 RESTful 设计原则。
- **配置管理**：内置配置处理。
- **可观测性**：支持日志、跟踪和指标收集。
- **认证中间件**：内置认证支持和自定义中间件。
- **gRPC 支持**：原生支持 gRPC 服务。
- **HTTP 服务**：带断路器支持的 HTTP 通信。
- **Pub/Sub**：发布-订阅模式支持。
- **健康检查**：对所有数据源进行健康监控。
- **数据库迁移**：简化数据库模式更新。
- **Cron Jobs**：定时任务支持。
- **动态日志级别**：无需重启更改日志级别。
- **Swagger 渲染**：自动生成 API 文档。
- **抽象文件系统**：统一的文件操作接口。
- **Websockets**：实时通信支持。

## 用法

### 安装

```bash
go get -u gofr.dev/pkg/gofr
```

### 基本示例

```go
package main

import "gofr.dev/pkg/gofr"

func main() {
    app := gofr.New()

    app.GET("/greet", func(ctx *gofr.Context) (any, error) {
        return "Hello World!", nil
    })

    app.Run() // 监听 localhost:8000
}
```

运行应用：

```bash
go run main.go
```

访问 `http://localhost:8000/greet` 查看结果。

更多示例请参考 [GoFr 示例目录](https://github.com/gofr-dev/gofr/tree/development/examples)。
