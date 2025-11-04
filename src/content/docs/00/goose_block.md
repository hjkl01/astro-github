
---
title: goose
---


# Goose

> GitHub 地址: <https://github.com/block/goose>

---

## 概述

Goose 是一个专为 Go 语言打造的轻量级区链工具库，提供完整的 **RPC 通信**、**交易签名**、**区块查询**以及 **事件监听** 等功能。凭借易用的 API，开发者可以快速在 Golang 项目中集成区块链交互，支持主流以太坊兼容链（Geth、OpenEthereum、GoChain 等）。

---

## 主要特性

| 特性 | 描述 |
|------|------|
| **RPC 客户端** | 简化 JSON‑RPC 网络调用，自动处理`Request ID`、错误与重试。 |
| **交易构造 & 签名** | 提供 `TxBuilder` 工具，支持链下生成 RLP 编码交易，并通过私钥签名。 |
| **账户与余额查询** | `GetBalance`、`GetNonce`、`GetAddress` 等接口，支持多链取值。 |
| **区块 & 交易查询** | `BlockByNumber`、`TxByHash` 等，支持同步与异步查询。 |
| **事件监听** | 基于 `SubscribeFilterLogs` 的实时监听，支持多主题过滤。 |
| **CLI 工具** | `goose-cli`：快速生成私钥、查询余额、发送交易、查看区块等。 |
| **链兼容** | 通过配置文件即可切换不同链（主网、测试网）。 |
| **扩展性** | 采用插件化设计，易于添加自定义 RPC 方法与事件处理。 |

---

## 安装方式

```bash
go get github.com/block/goose@latest
```

如果想使用 CLI 工具：

```bash
go install github.com/block/goose/cmd/goose-cli@latest
```

---

## 示例代码

```go
package main

import (
    "context"
    "fmt"
    "github.com/block/goose"
)

func main() {
    // 1. 创建 RPC 客户端
    client, err := goose.NewClient("https://goerli.infura.io/v3/YOUR_PROJECT_ID")
    if err != nil {
        panic(err)
    }

    // 2. 查询主账号余额
    addr := "0xYourAddressHere"
    balance, err := client.GetBalance(context.Background(), addr)
    if err != nil {
        panic(err)
    }
    fmt.Printf("Balance: %s wei\n", balance.String())

    // 3. 构造并发送交易
    txBuilder := goose.NewTxBuilder().
        To("0xDestinationAddress").
        Value(goose.NewWei("1_000_000_000_000_000_000")). // 1 ETH
        Nonce(7) // 从 client.GetNonce 获取
    signedTx, err := txBuilder.Sign("YOUR_PRIVATE_KEY")
    if err != nil {
        panic(err)
    }

    txHash, err := client.SendRawTransaction(context.Background(), signedTx)
    if err != nil {
        panic(err)
    }
    fmt.Printf("Transaction sent, hash: %s\n", txHash.Hex())
}
```

---

## CLI 用法

```bash
# 查看帮助
goose-cli help

# 显示地址余额
goose-cli balance 0xYourAddress

# 发送交易
goose-cli send \
    --to 0xRecipient \
    --value 1.0 \
    --from 0xYourAddress \
    --key YOUR_PRIVATE_KEY

# 监听事件
goose-cli listen --topic 0xTopicHash --from-block 2000000
```

---

## 开发要点

1. **配置文件**  
   存在 `goose.yaml` 用于指定 RPC URL、网络ID、默认账户等。  
2. **自动重试**  
   所有 RPC 调用均支持可配置的重试次数与间隔。  
3. **日志**  
   采用 `zap`，支持 `debug`、`info`、`error` 等级。  

---

## 贡献

欢迎提交 PR 或 issue。  
> 代码规范请遵循项目 README 与 `.golangci.yml` 配置。  

---

祝编码愉快 🚀

```

保存该内容至 `src/content/docs/00/goose_block.md`.