
---
title: go-redis
---

# go-redis（Redis Go 客户端）

> **项目地址**: <https://github.com/redis/go-redis>

## 主要特性

| 特性 | 说明 |
|------|------|
| **兼容性** | 支持 Redis 5/6/7 版本，兼容 `redis-cli` 所有命令 |
| **多种连接模式** | 单实例、集群（Cluster）、哨兵（Sentinel） |
| **连接池** | 自动连接复用，支持最大连接数、最小闲置连接、超时等配置 |
| **事务 & 管道** | 支持 `TxPipelined`、`Pipelined`、`TxPipeline` 等 |
| **Lua 脚本** | `Script` 结构体，支持脚本缓存、自动重试 |
| **发布/订阅** | `PubSub`、`Subscribe`、`Unsubscribe` 等 |
| **监控 & 日志** | 通过 `redis.Options` 的 `OnConnect`、`OnSlowLog` 等钩子 |
| **上下文** | 所有操作均支持 `context.Context`，可控制超时、取消 |
| **可插拔** | 自定义连接器、重连策略、TLS 等 |

## 安装

```bash
go get github.com/redis/go-redis/v9
```

> 使用 v9 作为最新主线版本，若需要旧版请改为 `v8`。

## 快速开始

### 单实例

```go
package main

import (
    "context"
    "fmt"
    "github.com/redis/go-redis/v9"
)

func main() {
    ctx := context.Background()

    rdb := redis.NewClient(&redis.Options{
        Addr:     "localhost:6379",
        Password: "", // no password
        DB:       0,  // default DB
        // 其他可选配置
        PoolSize:     10,
        MinIdleConns: 2,
        MaxRetries:   3,
    })

    // Ping
    if err := rdb.Ping(ctx).Err(); err != nil {
        panic(err)
    }

    // Set / Get
    if err := rdb.Set(ctx, "hello", "world", 0).Err(); err != nil {
        panic(err)
    }
    val, err := rdb.Get(ctx, "hello").Result()
    if err != nil {
        panic(err)
    }
    fmt.Println("hello:", val) // 输出: hello: world
}
```

### 集群

```go
cluster := redis.NewClusterClient(&redis.ClusterOptions{
    Addrs: []string{
        "localhost:7000",
        "localhost:7001",
        "localhost:7002",
    },
    // 其他配置同上
})

ctx := context.Background()
if err := cluster.Ping(ctx).Err(); err != nil {
    panic(err)
}
```

### 哨兵

```go
sentinel := redis.NewFailoverClient(&redis.FailoverOptions{
    MasterName:    "mymaster",
    SentinelAddrs: []string{"localhost:26379", "localhost:26380"},
    Password:      "",
})
```

## 关键 API

| 组别 | 方法 | 说明 |
|-----|------|------|
| **基本操作** | `Get`, `Set`, `Del`, `Incr`, `Decr`, `Exists`, `Keys`, `MGet`, `MSet` | 常用键值操作 |
| **事务** | `TxPipelined(ctx, func(tx *redis.Tx) error)`, `TxPipeline()` | 事务并行执行 |
| **管道** | `Pipelined(ctx, func(pipe redis.Pipeliner) error)`, `Pipeline()` | 批量执行 |
| **脚本** | `ScriptRun(ctx, script, keys, args...)` | Lua 脚本执行 |
| **订阅** | `Subscribe(ctx, channels...)`, `Unsubscribe(...)`, `PSubscribe(...)` | 发布/订阅 |
| **管道 & 事务混合** | `TxPipelined` | 先开启事务，再使用管道 |
| **Cluster** | `ClusterSlots`, `ClusterNodes` | 集群信息查询 |
| **监控** | `OnConnect`, `OnSlowLog` | 连接与慢查询钩子 |

## 示例：事务 + 管道

```go
err := rdb.TxPipelined(ctx, func(tx *redis.Tx) error {
    tx.Set(ctx, "foo", "bar", 0)
    tx.Incr(ctx, "counter")
    return nil
})
if err != nil {
    fmt.Println("事务执行失败:", err)
}
```

## 示例：Lua 脚本缓存

```go
script := redis.NewScript(`
    local val = redis.call('GET', KEYS[1])
    if val == false then
        return nil
    else
        return tonumber(val) + tonumber(ARGV[1])
    end
`)

newVal, err := script.Run(ctx, rdb, []string{"counter"}, 5).Int()
if err != nil {
    fmt.Println("脚本执行错误:", err)
}
fmt.Println("新值:", newVal)
```

## 常见配置说明

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `Addr` | `localhost:6379` | Redis 服务器地址 |
| `Password` | `""` | 密码 |
| `DB` | `0` | 数据库编号 |
| `PoolSize` | `10 * runtime.NumCPU()` | 连接池最大大小 |
| `MinIdleConns` | `0` | 最小闲置连接数 |
| `MaxRetries` | `3` | 失败重试次数 |
| `DialTimeout` | `5 * time.Second` | 连接超时 |
| `ReadTimeout` | `3 * time.Second` | 读超时 |
| `WriteTimeout` | `3 * time.Second` | 写超时 |
| `IdleTimeout` | `5 * time.Minute` | 空闲连接关闭时间 |
| `TLSConfig` | `nil` | TLS 配置 |

## 结语

go-redis 是一款功能齐全、性能优秀、使用简洁的 Redis Go 客户端，适用于从单节点到大规模集群的各种场景。其丰富的 API 与细粒度的配置选项，让开发者可以灵活地控制连接、事务、脚本、订阅等行为，满足高并发与低延迟的需求。  

> 如需进一步了解，请访问官方文档或参考源代码中的示例。