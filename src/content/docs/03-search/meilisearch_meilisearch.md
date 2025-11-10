---
title: meilisearch
---

# Meilisearch 项目

**项目地址：** [https://github.com/meilisearch/meilisearch?tab=readme-ov-file](https://github.com/meilisearch/meilisearch?tab=readme-ov-file)

## 主要特性
Meilisearch 是一个开源的、易于使用的全文搜索引擎，旨在提供快速、相关的搜索体验。它采用 Rust 语言开发，具有以下核心特性：
- **即时搜索**：支持毫秒级响应时间，即使在大型数据集上也能实现实时搜索。
- **类型化搜索**：内置对文档字段的类型化支持（如文本、数字、日期），无需额外配置即可处理复杂查询。
- **自动补全**：提供搜索建议和自动补全功能，提升用户搜索效率。
- **多语言支持**：支持多种语言的搜索，包括中文、日文等，支持分词和同义词处理。
- **高性能和可扩展性**：单实例即可处理数百万文档，支持分布式部署以扩展规模。
- **安全与隐私**：内置 API 密钥认证和数据加密，确保搜索数据的安全性。
- **易于集成**：轻量级设计，支持多种编程语言的 SDK（如 JavaScript、Python、Java 等）。

## 主要功能
Meilisearch 的功能聚焦于构建高效的搜索系统，主要包括：
- **索引管理**：创建、更新和删除索引，支持批量导入 JSON、CSV 等格式的数据。
- **搜索查询**：支持全文搜索、过滤、排序、分面搜索和地理位置搜索。
- **文档处理**：自动提取和索引文档中的字段，支持嵌套对象和数组。
- **任务管理**：异步处理任务队列，提供任务状态监控和错误处理。
- **配置选项**：可自定义搜索参数，如排名规则、停用词和同义词列表。
- **监控与分析**：内置健康检查、指标收集和日志记录，便于运维和调试。
- **实验性功能**：如向量搜索（实验中），支持 AI 和语义搜索扩展。

## 用法
Meilisearch 的用法简单，通过 HTTP API 或官方 SDK 操作。以下是基本步骤：

### 1. 安装和启动
- 下载二进制文件或使用 Docker：
  ```
  docker run -p 7700:7700 getmeili/meilisearch:latest
  ```
- 启动后，访问 `http://localhost:7700` 确认服务运行。

### 2. 创建索引和添加文档
使用 curl 或 SDK 示例（以 JavaScript SDK 为例）：
```javascript
import { MeiliSearch } from 'meilisearch'

const client = new MeiliSearch({ host: 'http://localhost:7700' })

// 创建索引
await client.createIndex('movies')

// 添加文档
const documents = [
  { id: 1, title: '电影标题', description: '电影描述' }
]
await client.index('movies').addDocuments(documents)
```

### 3. 执行搜索
```javascript
// 搜索查询
const searchResults = await client.index('movies').search('电影标题', {
  limit: 10,  // 限制结果数
  filter: 'rating > 8'  // 过滤条件
})
console.log(searchResults.hits)
```

### 4. 高级用法
- **过滤和排序**：在查询中添加 `filter` 和 `sort` 参数。
- **更新配置**：通过 API 修改索引设置，如 `client.index('movies').updateSettings({ rankingRules: ['words', 'typo'] })`。
- **监控任务**：使用 `client.getTask(taskUid)` 检查异步任务状态。

更多细节请参考官方文档：https://docs.meilisearch.com/。Meilisearch 适合构建电商搜索、博客站或任何需要快速搜索的应用。