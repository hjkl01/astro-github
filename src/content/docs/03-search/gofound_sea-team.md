
---
title: gofound
---

# GoFound 项目

**GitHub 项目地址**: [https://github.com/sea-team/gofound](https://github.com/sea-team/gofound)

## 主要特性
GoFound 是一个基于 Go 语言实现的开源搜索引擎框架，专注于高性能全文搜索和分布式索引。它具有以下核心特性：
- **高性能索引和搜索**：支持倒排索引（Inverted Index），查询速度快，支持实时索引更新。
- **分布式架构**：可扩展到多节点集群，支持负载均衡和故障转移。
- **多种数据源支持**：兼容 JSON、CSV 等格式数据导入，易于集成各种数据源。
- **高级查询功能**：支持布尔查询、短语查询、模糊匹配、范围查询和聚合函数。
- **轻量级部署**：无外部依赖，单二进制文件运行，便于部署在各种环境中。
- **RESTful API**：提供 HTTP 接口，便于与其他系统集成。
- **监控与管理**：内置仪表盘和日志系统，支持性能监控。

## 主要功能
- **数据索引**：通过 API 或命令行工具批量导入数据，建立高效的搜索索引。
- **全文搜索**：支持自然语言查询、关键词高亮和分页结果。
- **数据管理**：包括索引创建、删除、更新和优化功能。
- **集群管理**：支持主从复制和分片，提高搜索的可靠性和扩展性。
- **扩展插件**：可自定义分析器、过滤器和存储后端（如内存或磁盘）。

## 用法
### 安装
1. 从 GitHub 仓库克隆项目：`git clone https://github.com/sea-team/gofound.git`
2. 进入目录并构建：`cd gofound && go build`
3. 运行服务器：`./gofound`（默认监听 8080 端口）

### 基本用法
- **创建索引**：使用 POST 请求到 `/index/create` 端点，指定索引名称和字段映射。
  示例（使用 curl）：
  ```
  curl -X POST http://localhost:8080/index/create -d '{"name": "myindex", "fields": {"title": "text", "content": "text"}}'
  ```
- **添加数据**：POST 到 `/index/myindex/add` 上传 JSON 数据。
  示例：
  ```
  curl -X POST http://localhost:8080/index/myindex/add -d '{"id": 1, "title": "示例标题", "content": "示例内容"}'
  ```
- **搜索**：GET 到 `/search/myindex` 执行查询。
  示例：
  ```
  curl "http://localhost:8080/search/myindex?q=示例"
  ```
- **集群部署**：配置 `config.yaml` 文件中的节点列表，启动多个实例实现分布式搜索。

更多详细用法请参考项目仓库的 README 和文档。