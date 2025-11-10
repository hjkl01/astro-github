---
title: typesense
---

# Typesense 项目

## 项目地址
[https://github.com/typesense/typesense](https://github.com/typesense/typesense)

## 主要特性
Typesense 是一个现代、开源的搜索引擎，专为快速搜索体验设计。它类似于 Elasticsearch，但更注重简单性和速度。主要特性包括：
- **高性能搜索**：使用 SIMD 指令和内存映射文件，实现毫秒级搜索响应，支持数百万文档。
- **类型安全的搜索**：内置支持 JSON 数据结构，提供精确的类型匹配，避免 Elasticsearch 的动态类型问题。
- **智能搜索功能**：包括拼写纠正、自动完成、同义词支持、多语言分词和 faceting（分面搜索）。
- **易于部署**：单二进制文件，支持 Docker 和 Kubernetes，零配置即可运行。
- **分布式架构**：支持多节点集群，实现高可用性和水平扩展。
- **RESTful API**：简单易用的 HTTP API，便于集成到各种应用中。
- **开源与免费**：Apache 2.0 许可，完全开源，无需付费即可使用核心功能。

## 主要功能
- **文档索引**：支持实时索引 JSON 文档，支持 schema 定义字段类型（如字符串、整数、地理位置等）。
- **搜索查询**：支持全文搜索、过滤、排序、突出显示和分页。查询语言类似于 SQL，但更简洁。
- **集合管理**：创建和管理文档集合（collections），每个集合可有自定义 schema。
- **高级功能**：地理位置搜索、向量搜索（用于 AI 嵌入）、图像搜索集成，以及监控和健康检查 API。
- **客户端支持**：官方 SDK 支持 JavaScript、Python、Ruby、Go 等语言，便于应用集成。

## 用法
### 安装与启动
1. **下载二进制文件**：从 GitHub Releases 下载适合你的平台的二进制文件。
2. **运行服务器**：
   ```
   ./typesense-server --data-dir=/tmp/typesense-data --api-key=xyz --listen-port=8108
   ```
   - `--data-dir`：指定数据存储目录。
   - `--api-key`：设置 API 密钥（生产环境必需）。
   - 支持配置文件方式启动。

3. **使用 Docker**：
   ```
   docker run -d -p 8108:8108 -v /tmp/typesense-data:/data typesense/typesense:0.25.2 --data-dir /data --api-key=xyz --listen-port=8108
   ```

### 基本用法示例
1. **创建集合**（使用 curl）：
   ```
   curl -H "X-TYPESENSE-API-KEY: xyz" -X POST "localhost:8108/collections" \
   -d '{
     "name": "companies",
     "fields": [
       {"name": "company_name", "type": "string"},
       {"name": "num_employees", "type": "int32"}
     ]
   }'
   ```

2. **索引文档**：
   ```
   curl -H "X-TYPESENSE-API-KEY: xyz" -X POST "localhost:8108/collections/companies/documents" \
   -H "Content-Type: application/json" \
   -d '[
     {"id": "1", "company_name": "Typesense", "num_employees": 5}
   ]'
   ```

3. **执行搜索**：
   ```
   curl -H "X-TYPESENSE-API-KEY: xyz" "localhost:8108/collections/companies/documents/search?q=type&query_by=company_name"
   ```

更多用法详见官方文档：https://typesense.org/docs/。建议从快速启动指南开始，逐步集成到你的应用中。