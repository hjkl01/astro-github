
---
title: google-cloud-go
---

# Google Cloud Go Client Library

GitHub 地址: <https://github.com/googleapis/google-cloud-go>

## 项目概述
`google-cloud-go` 是 Google 官方维护的 Go 语言 Google Cloud Platform (GCP) 客户端库集合，提供对 GCP 各大服务（Compute Engine、Cloud Storage、BigQuery、Pub/Sub、Firestore 等）的统一且 idiomatic 的访问方式。库采用标准 Go 代码风格，支持自动化版本管理、依赖式更新以及向后兼容。

## 主要特性
- **完整的服务覆盖**：涵盖 GCP 近百种服务的客户端 SDK。  
- **简洁的 API**：使用 Go 的 idiomatic 风格与标准库一致，易于阅读与使用。  
- **自动化版本控制**：通过 `go.mod` 与 `google.golang.org/api` 版本同步，保持与 GCP API 更新同步。  
- **统一的身份验证**：内置 OAuth2、Service Account、Compute Engine、App Engine 等多种凭证方式。  
- **灵活的配置**：支持自定义 `ClientOptions`、`transport`、`retry` 等。  
- **测试友好**：每个客户端都提供内置的 `Mock` 或 `IntegrationTest` 方便单元与集成测试。  
- **多语言互操作**：与官方的 Java、Python、Node.js 等语言客户端保持接口一致。  

## 关键功能
| 服务 | 功能概览 |
|------|----------|
| Cloud Storage | 桶与对象 CRUD、批量操作、签名 URL |
| Pub/Sub | 发布/订阅、事务、流式消费 |
| BigQuery | 查询、作业管理、表读写 |
| Compute Engine | 实例、磁盘、网络等资源管理 |
| Firestore | 文档读写、事务、查询 |
| Cloud Spanner | 数据库管理、事务、批量读写 |
| Cloud Functions | 触发器与部署管理 |
| Cloud IAM | 权限与角色管理 |
| Cloud Logging, Monitoring, Trace, Error Reporting | 日志、指标、链路追踪、错误报告 |

## 快速入门
```bash
# 安装
go get google.golang.org/cloud

# 示例：上传文件到 Cloud Storage
package main

import (
    "context"
    "cloud.google.com/go/storage"
    "os"
)

func main() {
    ctx := context.Background()
    client, err := storage.NewClient(ctx)
    if err != nil {
        panic(err)
    }
    defer client.Close()

    bucket := client.Bucket("my-bucket")
    obj := bucket.Object("hello.txt")
    w := obj.NewWriter(ctx)
    _, err = w.Write([]byte("Hello, World!"))
    if err != nil {
        panic(err)
    }
    if err := w.Close(); err != nil {
        panic(err)
    }
}
```

## 依赖与构建
```bash
# 使用 go.mod
go mod init example.com/myapp
go get cloud.google.com/go
```

## 贡献
- Fork 本仓库  
- 创建 issue 或 PR  
- 参考 [CONTRIBUTING.md](https://github.com/googleapis/google-cloud-go/blob/main/CONTRIBUTING.md)  

## 许可证
Apache 2.0 – 详见 [LICENSE](https://github.com/googleapis/google-cloud-go/blob/main/LICENSE)  

--- 

> 以上内容可直接保存为 `src/content/docs/00/google-cloud-go_googleapis.md`。