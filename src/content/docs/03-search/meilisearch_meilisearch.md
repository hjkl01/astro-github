---
title: meilisearch
---

# Meilisearch 项目

**项目地址：** [https://github.com/meilisearch/meilisearch?tab=readme-ov-file](https://github.com/meilisearch/meilisearch?tab=readme-ov-file)

## 主要特性

Meilisearch 是一个开源的、易于使用的全文搜索引擎，旨在提供快速、相关的搜索体验。它采用 Rust 语言开发，具有以下核心特性：

- **混合搜索**：结合语义搜索和全文搜索的最佳优势，以获得最相关的结果。
- **即时搜索**：在不到 50 毫秒内查找和显示结果，提供直观的体验。
- **拼写容错**：即使查询包含拼写错误和拼写错误，也能获得相关匹配。
- **过滤和分面搜索**：使用自定义过滤器增强用户搜索体验，并用几行代码构建分面搜索界面。
- **排序**：根据价格、日期或其他用户需要的任何内容，在查询时动态排序结果。
- **同义词支持**：配置同义词以在搜索结果中包含更多相关内容。
- **地理搜索**：基于地理数据过滤和排序文档。
- **广泛的语言支持**：搜索任何语言的数据集，对中文、日文、希伯来语和使用拉丁字母的语言进行优化支持。
- **安全管理**：使用允许细粒度权限处理的 API 密钥控制哪些用户可以访问哪些数据。
- **多租户**：为任意数量的应用程序租户个性化搜索结果。
- **高度可定制**：根据您的具体需求定制 Meilisearch，或使用开箱即用的无忧预设。
- **RESTful API**：使用我们的插件和 SDK 将 Meilisearch 集成到您的技术栈中。
- **AI 就绪**：开箱即用地与 langchain 和模型上下文协议配合使用。
- **易于安装、部署和维护**：简单设置、集成、操作和扩展。

## 主要功能

Meilisearch 的功能聚焦于构建高效的搜索系统，主要包括：

- **索引管理**：创建、更新和删除索引，支持批量导入 JSON、CSV 等格式的数据。
- **搜索查询**：支持全文搜索、过滤、排序、分面搜索和地理位置搜索。
- **文档处理**：自动提取和索引文档中的字段，支持嵌套对象和数组。
- **任务管理**：异步处理任务队列，提供任务状态监控和错误处理。
- **配置选项**：可自定义搜索参数，如排名规则、停用词和同义词列表。
- **监控与分析**：内置健康检查、指标收集和日志记录，便于运维和调试。

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
import { MeiliSearch } from 'meilisearch';

const client = new MeiliSearch({ host: 'http://localhost:7700' });

// 创建索引
await client.createIndex('movies');

// 添加文档
const documents = [{ id: 1, title: '电影标题', description: '电影描述' }];
await client.index('movies').addDocuments(documents);
```

### 3. 执行搜索

```javascript
// 搜索查询
const searchResults = await client.index('movies').search('电影标题', {
  limit: 10, // 限制结果数
  filter: 'rating > 8', // 过滤条件
});
console.log(searchResults.hits);
```

### 4. 高级用法

- **过滤和排序**：在查询中添加 `filter` 和 `sort` 参数。
- **更新配置**：通过 API 修改索引设置，如 `client.index('movies').updateSettings({ rankingRules: ['words', 'typo'] })`。
- **监控任务**：使用 `client.getTask(taskUid)` 检查异步任务状态。

更多细节请参考官方文档：https://docs.meilisearch.com/。Meilisearch 适合构建电商搜索、博客站或任何需要快速搜索的应用。
