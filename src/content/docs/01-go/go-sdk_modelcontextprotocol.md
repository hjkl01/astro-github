
---
title: go-sdk
---


# ModelContextProtocol Go SDK

- 项目地址：<https://github.com/modelcontextprotocol/go-sdk>

## 简介

`go-sdk` 是 ModelContextProtocol 的 Go 语言实现，旨在帮助开发者轻松地将业务数据、日志与上下文信息发送到 ModelContextProtocol 平台。该 SDK 通过提供高层封装的客户端 API，简化了数据校验、序列化、签名、重试等常见任务，让你专注于业务逻辑。

## 主要特性

- **易用的客户端**：只需几行代码即可完成数据上传。
- **自动签名与校验**：使用项目密钥对请求进行 HMAC‑SHA256 签名，保障数据完整性和安全性。
- **重试机制**：内置指数退避策略，自动重试网络错误与 5xx 状态码。
- **异步批量发送**：支持将多条数据聚合后一次性发送，减少网络开销。
- **丰富的错误处理**：统一返回错误结构，方便开发者捕获与定位问题。
- **可配置化**：支持自定义超时、重试次数、日志级别等。

## 快速开始

### 1. 安装

```bash
go get github.com/modelcontextprotocol/go-sdk@latest
```

### 2. 初始化客户端

```go
package main

import (
	"log"

	"github.com/modelcontextprotocol/go-sdk/pkg/sdk"
)

func main() {
	cfg := sdk.NewConfig(
		"YOUR_PROJECT_ID",
		"YOUR_API_KEY",
		sdk.WithEndpoint("https://api.modelcontextprotocol.com"), // 可, 默认值
		sdk.WithTimeout(30),                                      // 传输超时秒
		sdk.WithRetry(3),                                          // 重试次数
	)

	client, err := sdk.NewClient(cfg)
	if err != nil {
		log.Fatalf("创建客户端失败: %v", err)
	}
	defer client.Close()

	// 发送单条数据
	if err := client.Send(context.Background(), map[string]interface{}{
		"user_id":   12345,
		"action":    "click",
		"timestamp": time.Now().Unix(),
	}); err != nil {
		log.Printf("发送失败: %v", err)
	}
}
```

### 3. 异步批量发送

```go
batch := &sdk.Batch{
    Events: []map[string]interface{}{
        {"user_id": 1, "action": "view"},
        {"user_id": 2, "action": "purchase"},
    },
}
err := client.SendBatch(context.Background(), batch)
if err != nil {
    // handle error
}
```

## API 概览

| 包 | 功能 | 说明 |
|----|------|------|
| `sdk/config.go` | 账户与连接配置 | 传递项目 ID、API Key、endpoint、超时、重试配置 |
| `sdk/client.go` | 主要客户端 | `NewClient`, `Send`, `SendBatch`, `Close` |
| `sdk/transport.go` | HTTP 传输层 | 自动签名、重试、日志 |
| `sdk/models.go` | 数据模型 | `Event`, `Batch`, `Response` 等 |
| `sdk/errors.go` | 错误定义 | 包含 `ErrUnauthorized`, `ErrRequestFailed` 等 |

## 配置参数

- `ProjectID`（必填）：ModelContextProtocol 项目 ID。  
- `APIKey`（必填）：用于签名请求的密钥。  
- `Endpoint`（可选）：API 接口地址，默认 `https://api.modelcontextprotocol.com`。  
- `Timeout`（可选）：HTTP 超时时间，单位秒。  
- `Retry`（可选）：失败时重试次数。  
- `LogLevel`（可选）：日志级别，支持 `debug`, `info`, `warn`, `error`。

## 贡献

欢迎 Issue 与 Pull Request。开发流程请参考 `CONTRIBUTING.md`。

## 许可证

MIT 开源协议，详见 `LICENSE`。
