---
title: Helix Db
---

# HelixDB

HelixDB 是一个用 Rust 从头构建的开源图向量数据库。它提供了一个统一的平台来构建 AI 应用，消除了对应用数据、向量、图和应用层的单独数据库的需求。

## 主要特性

- **图向量数据模型**：主要操作图 + 向量数据，但也支持 KV、文档和关系数据。
- **内置 MCP 工具**：允许代理发现数据并遍历图。
- **内置嵌入**：使用 `Embed` 函数对文本进行向量化，无需预处理。
- **RAG 工具**：包括向量搜索、关键词搜索和图遍历，用于 RAG 应用。
- **默认安全**：默认私有，仅通过编译的 HelixQL 查询访问。
- **超低延迟**：用 Rust 构建，使用 LMDB 存储引擎。
- **类型安全查询**：HelixQL 是 100% 类型安全的。

## 入门指南

### 安装 Helix CLI

```bash
curl -sSL "https://install.helix-db.com" | bash
```

### 初始化项目

```bash
mkdir <path-to-project> && cd <path-to-project>
helix init
```

### 编写查询

编辑生成的 `.hx` 文件来定义您的模式和查询。例如：

```sql
N::User {
   INDEX name: String,
   age: U32
}

QUERY getUser(user_name: String) =>
   user <- N<User>({name: user_name})
   RETURN user
```

### 检查和部署

```bash
helix check  # 可选：验证查询编译
helix push dev  # 部署到 API 端点
```

### 使用 SDK

安装并使用 TypeScript 或 Python SDK 与您的部署查询交互。

**TypeScript 示例：**

```typescript
import HelixDB from 'helix-ts';

const client = new HelixDB();

await client.query('addUser', {
  name: 'John',
  age: 20,
});

const user = await client.query('getUser', {
  user_name: 'John',
});

console.log(user);
```

更多详情，请访问 [官方文档](https://docs.helix-db.com)。
