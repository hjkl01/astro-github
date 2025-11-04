
---
title: LMCache
---


# LMCache

[GitHub项目地址](https://github.com/LMCache/LMCache)

## 项目概览
LMCache 是一款用 Go 语言实现的轻量级高性能内存缓存库。它支持多种淘汰策略、线程安全访问，并提供了丰富的统计与监控接口，适用于对读写吞吐和低延迟有严格要求的业务场景。

## 主要特性
| 特性 | 说明 |
|------|------|
| **高并发** | 内部采用分段锁（sharding）实现无锁读 + 有锁写，单核读写竞争极低。 |
| **多种淘汰策略** | `LRU`、`MRU`、`LFU`、`ARC`、`SLRU`、`Random` 等，支持在实例创建时任选。 |
| **容量与TTL** | 可设定最大容量（条目数或字节数），支持单条缓存项的自定义过期时间（TTL）。 |
| **线程安全** | 所有公共接口均为并发安全，内部使用读写互斥或无锁访问。 |
| **序列化/反序列化** | 对任意 `interface{}` 类型值自动使用 gob/JSON；可自定义序列化函数。 |
| **批量操作** | 支持 `GetMulti`、`SetMulti`、`DeleteMulti` 等一次性多项处理。 |
| **扩展插槽** | 插件化的 `Hook`、`Evict`、`Clean` 机制，方便在淘汰/清理时执行自定义逻辑。 |
| **监控统计** | 提供命中率、使用率、容量等指标；可通过 `Prometheus` 导出。 |
| **轻量部署** | 仅依赖 Go 标准库（+可选 `encoding/gob`），不需要任何外部依赖或 C 组件。 |

## 使用方式

```go
package main

import (
    "fmt"
    "time"

    "github.com/LMCache/LMCache"
)

func main() {
    // 创建一个容量为 1000 条目，默认 LRU 淘汰策略的缓存
    cache, err := lmcache.New(
        lmcache.WithSizeLimit(1000),
        lmcache.WithEvictionPolicy(lmcache.LRUEviction), // 可选：MRUEviction, LiuEviction 等
    )
    if err != nil {
        panic(err)
    }

    // 设置缓存项，可指定 TTL（可选）
    err = cache.Set("user:123", map[string]string{
        "name":  "张三",
        "email": "zhangsan@example.com",
    }, 5*time.Minute) // 5 分钟后过期
    if err != nil {
        fmt.Println("Set error:", err)
    }

    // 获取缓存项
    var userInfo map[string]string
    if ok, err := cache.Get("user:123", &userInfo); err == nil && ok {
        fmt.Println("user info:", userInfo)
    }

    // 批量获取
    keys := []string{"user:123", "user:456", "user:789"}
    results, err := cache.GetMulti(keys)
    if err != nil {
        fmt.Println("GetMulti error:", err)
    } else {
        fmt.Println("GetMulti results:", results)
    }

    // 删除缓存项
    err = cache.Delete("user:123")
    if err != nil {
        fmt.Println("Delete error:", err)
    }

    // 统计信息
    stats := cache.Stats()
    fmt.Printf("cache hits: %d, misses: %d, current size: %d\n",
        stats.Hits, stats.Misses, stats.CurrentSize)

    // 自定义回调（可选）
    cache.OnEvict(func(key string, value interface{}) {
        fmt.Printf("Evicted key=%s, value=%v\n", key, value)
    })
}
```

### API 简览

| 方法 | 作用 |
|------|------|
| `New(opts ...Option)` | 创建缓存实例 |
| `Set(key string, value interface{}, ttl time.Duration)` | 设置单键 |
| `Get(key string, dst interface{}) (bool, error)` | 读取单键 |
| `GetMulti(keys []string)` | 批量读取 |
| `SetMulti(items map[string]Item)` | 批量写入 |
| `Delete(key string)` | 删除单键 |
| `Clear()` | 清空缓存 |
| `Stats()` | 获取统计信息 (`Hits`, `Misses`, `CurrentSize`) |
| `OnEvict(fn func(key string, value interface{}))` | 设置淘汰回调 |
| `About()` | 打印缓存配置信息 |

> 详情可查看源码内注释或官方文档。

## 结语
LMCache 以其轻量、灵活与高性能被设计为内存层级缓存的理想选择。无论是 Web 后端、微服务还是命令行工具，都可以直接利用它提升数据访问速度与系统吞吐率。若有更高级需求（如持久化、分布式共享），可在此基础上做进一步封装或结合分布式缓存方案。

``` 
