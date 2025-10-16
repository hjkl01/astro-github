
---
title: gofound
---

# GoFound 项目介绍

**GitHub 项目地址:** [https://github.com/newpanjing/gofound](https://github.com/newpanjing/gofound)

## 主要特性
GoFound 是一个用 Go 语言编写的开源搜索引擎框架，专注于高性能和分布式搜索能力。其核心特性包括：
- **高效索引和搜索**：支持倒排索引（Inverted Index），实现快速全文搜索和精确匹配。
- **分布式架构**：支持集群部署，可水平扩展节点，实现高可用性和负载均衡。
- **多种数据源支持**：兼容 JSON、XML 等格式的数据导入，并支持实时索引更新。
- **RESTful API 接口**：提供简洁的 HTTP API，便于集成到 Web 应用中。
- **轻量级设计**：无外部依赖，易于部署和维护，适用于中小型搜索引擎场景。
- **插件扩展**：允许自定义分词器和查询处理器，支持中文分词（如集成 Jieba）。

## 主要功能
- **数据索引**：通过 API 或命令行工具批量导入数据，建立搜索索引。
- **搜索查询**：支持布尔查询、短语搜索、范围查询和排序等高级搜索功能。
- **数据管理**：提供索引的创建、删除、更新和监控接口。
- **性能优化**：内置缓存机制和并发处理，提升查询速度。
- **监控与日志**：集成 Prometheus 支持的 metrics，以及详细的日志输出用于调试。

## 用法
### 1. 安装
- 克隆仓库：`git clone https://github.com/newpanjing/gofound.git`
- 进入目录：`cd gofound`
- 构建：`go build -o gofound`
- 运行：`./gofound`（默认监听 8080 端口）

### 2. 基本配置
编辑 `config.yaml` 文件设置节点地址、数据路径等参数。例如：
```yaml
server:
  port: 8080
data:
  path: ./data
cluster:
  nodes: ["localhost:8080"]
```

### 3. 数据索引
- 创建索引：`curl -X PUT "localhost:8080/indexes/myindex" -d '{"analyzer": "standard"}'`
- 添加文档：`curl -X POST "localhost:8080/indexes/myindex/docs" -d '{"id":1,"title":"示例文档","content":"GoFound 是一个搜索引擎"}'`

### 4. 搜索查询
- 基本搜索：`curl -X GET "localhost:8080/indexes/myindex/search?q=GoFound"`
- 高级查询：支持 JSON 参数，如 `{"query": {"match": {"title": "搜索引擎"}}}`

### 5. 集群部署
- 在多台机器上运行节点，并通过 `cluster.nodes` 配置连接。
- 使用内置的 Raft 协议实现数据同步和主从选举。

更多细节请参考项目 README 和 API 文档。项目适用于构建自定义搜索引擎，如企业内部搜索或内容推荐系统。