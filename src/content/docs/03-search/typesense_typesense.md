---
title: typesense
---

# Typesense 项目

## 项目地址

[https://github.com/typesense/typesense](https://github.com/typesense/typesense)

## 主要特性

Typesense 是一个现代、开源的搜索引擎，专为快速搜索体验设计。它类似于 Elasticsearch，但更注重简单性和速度。主要特性包括：

- **拼写容错**：优雅地处理拼写错误，开箱即用。
- **简单而令人愉悦**：设置、集成、操作和扩展简单。
- **⚡ 极快**：用 C++ 构建。从头精心架构，用于低延迟（<50ms）即时搜索。
- **可调排名**：轻松调整搜索结果以达到完美。
- **排序**：在查询时根据特定字段动态排序结果（有助于“按价格排序（升序）”等功能）。
- **分面和过滤**：深入挖掘并细化结果。
- **分组和去重**：将相似结果分组在一起以显示更多多样性。
- **联合搜索**：在单个 HTTP 请求中跨多个集合（索引）搜索。
- **地理搜索**：围绕纬度/经度搜索和排序，或在边界框内搜索。
- **向量搜索**：在 Typesense 中索引机器学习模型的嵌入，并进行最近邻搜索。可用于构建相似性搜索、语义搜索、视觉搜索、推荐等。
- **语义/混合搜索**：使用内置模型如 S-BERT、E-5 等从 Typesense 内自动生成嵌入，或使用 OpenAI、PaLM API 等，用于查询和索引数据。这允许您将 JSON 数据发送到 Typesense 并构建开箱即用的语义搜索 + 关键字搜索体验。
- **对话搜索（内置 RAG）**：向 Typesense 发送问题，并根据您在 Typesense 中索引的数据获得完整句子的响应。想想 ChatGPT，但基于您自己的数据。
- **自然语言搜索**：LLM 驱动的意图检测和查询理解，将任何自由形式的自然语言短语转换为结构化过滤器、排序和查询。
- **图像搜索**：使用内容的文本描述搜索图像，或使用 CLIP 模型执行相似性搜索。
- **语音搜索**：通过语音录音捕获和发送查询 - Typesense 将转录（通过 Whisper 模型）并提供搜索结果。
- **作用域 API 密钥**：生成仅允许访问某些记录的 API 密钥，用于多租户应用程序。
- **JOIN**：通过公共引用字段连接一个或多个集合，并在查询时加入它们。这允许您优雅地建模 SQL 式的关系。
- **同义词**：将单词定义为彼此的等价物，因此搜索单词也将返回为同义词定义的结果。
- **策展和商品化**：将特定记录提升到搜索结果的固定位置，以突出显示它们。
- **基于 Raft 的集群**：设置高度可用的分布式集群。
- **无缝版本升级**：随着新版本的 Typesense 发布，升级就像更换二进制文件并重新启动一样简单。
- **无运行时依赖**：Typesense 是一个您可以在本地或生产中用单个命令运行的单个轻量级二进制文件。

## 主要功能

- **文档索引**：支持实时索引 JSON 文档，支持 schema 定义字段类型（如字符串、整数、地理位置等）。
- **搜索查询**：支持全文搜索、过滤、排序、突出显示和分页。查询语言类似于 SQL，但更简洁。
- **集合管理**：创建和管理文档集合（collections），每个集合可有自定义 schema。
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
