---
title: dgraph
---

# Dgraph 项目

## 项目地址
[https://github.com/dgraph-io/dgraph](https://github.com/dgraph-io/dgraph)

## 主要特性
Dgraph 是一个开源的分布式图数据库，专为处理大规模数据和复杂查询而设计。它采用图数据库模型，支持属性图和 RDF 数据存储，具有高性能、可扩展性和 ACID 事务保证。主要特性包括：
- **分布式架构**：支持水平扩展，可运行在多个节点上，实现高可用性和容错。
- **GraphQL 支持**：内置 GraphQL API，支持实时查询和变更数据。
- **高性能查询**：使用自定义的查询语言 DQL（Dgraph Query Language），优化了图遍历和复杂关系查询。
- **全文搜索**：集成全文索引，支持模糊搜索和过滤。
- **安全性**：提供认证、授权和加密功能，确保数据安全。
- **多语言支持**：官方客户端支持 Go、Java、Python 等语言。

## 主要功能
Dgraph 的核心功能聚焦于图数据管理和查询：
- **数据建模**：支持 schema 定义，包括节点、边、索引和类型，支持多租户隔离。
- **查询与更新**：通过 DQL 或 GraphQL 执行查询，支持聚合、排序、分页和变量绑定。更新操作包括添加、删除和条件变更。
- **事务处理**：提供线性化读写事务，确保数据一致性。
- **备份与恢复**：内置增量备份工具，支持云存储集成。
- **监控与运维**：集成 Prometheus 和 Grafana，用于性能监控和集群管理。
- **集成扩展**：可与 Kafka、Elasticsearch 等工具结合，实现数据流处理和混合搜索。

## 用法
### 安装
1. **二进制安装**：从 GitHub Releases 下载预编译二进制文件，解压后运行 `dgraph alpha`（Alpha 节点）和 `dgraph zero`（Zero 节点）启动集群。
2. **Docker 安装**：使用官方 Docker 镜像：
   ```
   docker run -d -p 8080:8080 -p 9080:9080 -p 8000:8000 dgraph/standalone:latest
   ```
   这将启动单节点模式，访问 http://localhost:8000 进入 Ratel UI。

### 基本用法
1. **启动集群**：
   - 运行 Zero：`dgraph zero --wal=zwal`
   - 运行 Alpha：`dgraph alpha --zero=localhost:5080`

2. **定义 Schema**：
   使用 HTTP POST 到 `/admin/schema` 端点，例如：
   ```
   curl -X POST localhost:8080/admin/schema -d 'name: string @index(exact) .'
   ```

3. **插入数据**（使用 Mutation）：
   ```
   curl -X POST localhost:8080/mutate?commitNow=true -d $'{"set": [{"uid": "_:a", "name": "Alice"}]}' -H "Content-Type: application/json"
   ```

4. **查询数据**（使用 DQL）：
   ```
   curl -X POST localhost:8080/query -d $'
   {
     q(func: has(name)) {
       name
     }
   }' -H "Content-Type: application/json"
   ```

5. **GraphQL 模式**：在 Ratel UI 或通过 API 配置 GraphQL schema，然后使用标准 GraphQL 查询。

详细文档和示例请参考项目仓库的 README 和 docs 目录。