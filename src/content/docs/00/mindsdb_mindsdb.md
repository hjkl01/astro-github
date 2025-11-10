---
title: mindsdb
---

# MindsDB

## 功能

MindsDB 是一个开源的联邦查询引擎，专为 AI 设计。它允许人类、AI、代理和应用程序从大规模数据源中获取高度准确的答案。核心哲学是“连接、统一、响应”：

- **连接数据**：支持连接到数百个企业数据源，包括数据库、数据仓库和 SaaS 应用程序。
- **统一数据**：使用 MindsDB SQL 创建知识库和视图来索引和组织结构化和非结构化数据，实现无 ETL 的统一。
- **响应数据**：通过内置代理和 MCP（Model Context Protocol）与数据交互，进行问答。

MindsDB 还内置 MCP 服务器，使 MCP 应用程序能够连接、统一和响应大规模联邦数据。

## 用法

### 安装 MindsDB Server

推荐使用 Docker Desktop 快速启动：

```bash
# 使用 Docker Desktop
# 按照文档安装 Docker Desktop，然后运行：
docker run -p 47334:47334 mindsdb/mindsdb
```

或者使用 Docker：

```bash
docker run -p 47334:47334 mindsdb/mindsdb
```

### 基本用法

1. **连接数据源**：在 MindsDB 中连接到你的数据库或数据源。

   ```sql
   CREATE DATABASE my_db
   WITH ENGINE = 'postgres',
   PARAMETERS = {
     "host": "your-host",
     "port": 5432,
     "database": "your-db",
     "user": "your-user",
     "password": "your-password"
   };
   ```

2. **创建知识库或视图**：统一数据。

   ```sql
   CREATE VIEW my_view AS
   SELECT * FROM my_db.table1
   UNION
   SELECT * FROM another_source.table2;
   ```

3. **配置代理**：创建代理来回答问题。

   ```sql
   CREATE AGENT my_agent
   USING
     model = 'openai/gpt-4',
     knowledge_base = 'my_kb';
   ```

4. **查询**：使用 SQL 或通过 MCP 与数据交互。
   ```sql
   SELECT * FROM my_agent
   WHERE question = 'What is the sales trend?';
   ```

更多详细信息，请参考 [官方文档](https://docs.mindsdb.com)。
