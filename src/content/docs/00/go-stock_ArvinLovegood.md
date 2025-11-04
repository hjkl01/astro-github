
---
title: go-stock
---


# go-stock

项目地址: https://github.com/ArvinLovegood/go-stock

## 主要特性

- 多源股票数据：支持从 `pangu`、`tencent`、`jd` 等多家接口获取行情、K线、分时、个股基本面数据。  
- 统一接口：所有数据接口统一归纳到 `api.Stock` 结构体，调用方式一致，易于切换数据源。  
- 缓存机制：默认使用内存缓存，避免频繁网络请求，支持自定义缓存时长。  
- 可扩展：新数据源只需实现 `Provider` 接口，即可无缝集成。

## 关键功能

| 功能 | 说明 | 关键函数 |
|------|------|----------|
| 获取日K线 | 返回指定股票代码的日K线列表 | `DailyKLine(code string, start, end time.Time) ([]KLine, error)` |
| 获取分时行情 | 按分钟粒度获取实时行情 | `MinuteChart(code string, period int) ([]Minute, error)` |
| 股票基本面 | 获取个股的财务数据、行业估值等 | `BasicInfo(code string) (*Company, error)` |
| 股票列表查询 | 根据关键字搜索股票 | `Search(keyword string) ([]Stock, error)` |
| 订阅推送 | 通过 WebSocket 或 SSE 接收实时涨跌 | `Subscribe(code string, ch chan Quote)` |
| 数据转换 | K线、分时等数据统一格式，可转为 CSV / JSON | `ToCSV(data []KLine) string` |

## 快速上手

```go
package main

import (
    "fmt"
    "time"

    "github.com/ArvinLovegood/go-stock"
)

func main() {
    // 设定数据源，例如 “tencent” (可选值：pangu, jd, tencent)
    provider := stock.NewProvider("tencent")

    // 1. 获取日K线
    start := time.Date(2023, 1, 1, 0, 0, 0, 0, time.UTC)
    end   := time.Date(2023, 12, 31, 0, 0, 0, 0, time.UTC)
    klines, err := provider.DailyKLine("600519", start, end)
    if err != nil {
        panic(err)
    }
    fmt.Printf("K线数量: %d\n", len(klines))

    // 2. 获取分时行情
    minutes, err := provider.MinuteChart("600519", 5) // 5 分钟一档
    if err != nil {
        panic(err)
    }
    fmt.Printf("分时档数: %d\n", len(minutes))

    // 3. 获取基本面
    info, err := provider.BasicInfo("600519")
    if err != nil {
        panic(err)
    }
    fmt.Printf("公司名称: %s, 行业: %s\n", info.Name, info.Industry)
}
```

## 配置缓存

```go
// 设置全局缓存时间为 30 分钟
stock.SetCacheTTL(time.Minute * 30)
```

## 文档与资源

- API 文档：https://pkg.go.dev/github.com/ArvinLovegood/go-stock  
- 示例代码请参见 `example/` 目录  
- 统一数据结构见 `model/` 目录  

---  

> 项目地址: https://github.com/ArvinLovegood/go-stock
