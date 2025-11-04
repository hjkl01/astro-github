
---
title: chartdb
---


# ChartDB

[GitHub 项目地址](https://github.com/chartdb/chartdb)

## 项目简介
ChartDB 是一个用 Go 语言实现、轻量化的时序数据库，专为存储与查询图表数据而设计。它提供高速写入、压缩存储、灵活查询以及多语言 SDK 与 CLI。

## 主要特性
- **高速写入**：内存缓存 + 定期刷盘，写入延迟低。  
- **高效查询**：支持时间范围 + 标签过滤。  
- **数据压缩**：使用 Gorilla 压缩算法，节省磁盘。  
- **多语言 SDK**：Go、Python、CLI 工具。  
- **灵活存储**：单文件或分区存储。  
- **插件化**：可自定义存储后端与查询插件。

## 快速使用

### 1. 安装
```bash
go get github.com/chartdb/chartdb
```

### 2. 初始化数据库
```go
import "github.com/chartdb/chartdb"

db, err := chartdb.Open("./data")
if err != nil { log.Fatal(err) }
defer db.Close()
```

### 3. 写入数据
```go
points := []chartdb.Point{
    {Timestamp: time.Now(), Value: 100.5, Labels: map[string]string{"host":"server1"}},
    {Timestamp: time.Now().Add(time.Minute), Value: 101.2, Labels: map[string]string{"host":"server1"}},
}
err = db.Write("cpu_usage", points)
```

### 4. 查询数据
```go
query := chartdb.Query{
    Start:  time.Now().Add(-time.Hour),
    End:    time.Now(),
    Labels: map[string]string{"host":"server1"},
}
results, err := db.Query("cpu_usage", query)
for _, p := range results {
    fmt.Printf("%s: %.2f\n", p.Timestamp, p.Value)
}
```

### 5. CLI 与 HTTP API
```bash
# 启动服务
chartdb-cli serve --data-dir ./data

# 通过 HTTP 写入
curl -X POST http://localhost:8080/write \
     -H 'Content-Type: application/json' \
     -d '{"series":"cpu_usage","points":[{"timestamp":1633072800,"value":100.5,"labels":{"host":"server1"}}]}'
```

## 贡献与许可证
- 贡献请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。  
- 许可证：MIT
```
