
---
title: aws-sdk-go-v2
---


# AWS SDK for Go v2

**仓库地址**: [https://github.com/aws/aws-sdk-go-v2](https://github.com/aws/aws-sdk-go-v2)

## 项目概述
AWS SDK for Go v2 是 AWS 官方提供的 Go 语言 SDK，支持 Go 1.18+，提供对 AWS 各类服务的完整、类型安全、易用的客户端。相比 v1，v2 在性能、配置、错误处理、重试机制、分页、插件体系等方面做了显著改进。

## 主要特性
- **现代化设计**  
  - 采用 `context.Context` 统一支持超时、取消等控制。  
  - 所有 API 采用类型安全、结构化的请求/响应对象，无需手动解析 JSON/XML。  
- **高性能**  
  - 内置高效连接池与 HTTP Client，支持自定义 Transport。  
  - 支持 HTTP/2、TLS 1.3 等现代协议。  
- **灵活配置**  
  - 支持多种凭证提供方式：环境变量、共享凭证文件、EC2 实例角色、STS 角色假设等。  
  - 支持自定义 Region、Endpoint、Retry、Retryer、Logger 等。  
- **插件化架构**  
  - 通过 `smithy-go` 的插件机制，轻松添加自定义拦截器、日志、监控等功能。  
- **分页与重试**  
  - 自动处理分页（`paginators`），一次调用即可获取完整结果。  
  - 内置可配置的重试策略（指数退避、最大重试次数、错误排除等）。  
- **多语言互操作**  
  - 与 AWS Service Client 的 Go SDK 版本保持一致，支持跨语言调用。  

## 常用功能

| 功能 | 说明 | 示例 |
|------|------|------|
| 核心客户端 | 创建并使用 AWS 服务客户端 | `svc := s3.NewFromConfig(cfg)` |
| 认证 | 加载凭证 | `cfg, err := config.LoadDefaultConfig(ctx)` |
| 分页 | 自动遍历结果 | `paginator := s3.NewListObjectsV2Paginator(svc, &s3.ListObjectsV2Input{Bucket: aws.String("my-bucket")})` |
| 重试 | 自定义重试策略 | `cfg, _ := config.LoadDefaultConfig(ctx, config.WithRetryer(customRetryer))` |
| 插件 | 添加自定义拦截器 | `svc.AddMiddleware(myMiddleware)` |
| 生成代码 | 使用 Smithy 生成 SDK | `smithy-go generate` |

## 快速上手

```go
package main

import (
    "context"
    "fmt"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
    ctx := context.Background()
    // 加载默认配置（凭证、Region 等）
    cfg, err := config.LoadDefaultConfig(ctx)
    if err != nil {
        panic("configuration error, " + err.Error())
    }

    // 创建 S3 客户端
    svc := s3.NewFromConfig(cfg)

    // 列出桶中对象
    paginator := s3.NewListObjectsV2Paginator(svc, &s3.ListObjectsV2Input{Bucket: aws.String("my-bucket")})
    for paginator.HasMorePages() {
        output, err := paginator.NextPage(ctx)
        if err != nil {
            panic(err)
        }
        for _, obj := range output.Contents {
            fmt.Println(*obj.Key)
        }
    }
}
```

## 文档与资源
- 官方文档: https://docs.aws.amazon.com/sdk-for-go/api/
- 代码示例: https://github.com/aws/aws-sdk-go-v2/tree/main/private/examples
- 贡献指南: https://github.com/aws/aws-sdk-go-v2/blob/main/CONTRIBUTING.md

## 许可证
MIT License
```
