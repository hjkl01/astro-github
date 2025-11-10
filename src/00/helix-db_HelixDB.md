# HelixDB

HelixDB 是一个用 Rust 从头构建的开源图向量数据库。它提供了一个统一的平台，用于构建 AI 应用程序的所有组件，无需单独的应用程序数据库、向量数据库、图数据库或应用层来管理多个存储位置。

## 主要功能

- **图向量数据模型**：主要操作图 + 向量数据模型，但也支持 KV、文档和关系数据。
- **内置 MCP 工具**：允许代理发现数据并遍历图，而非生成人类可读查询。
- **内置嵌入**：无需预先嵌入数据，使用 `Embed` 函数向量化文本。
- **RAG 工具**：内置向量搜索、关键词搜索和图遍历，用于支持任何类型的 RAG 应用程序。
- **默认安全**：私有化默认，只能通过编译的 HelixQL 查询访问数据。
- **超低延迟**：使用 Rust 构建，并以 LMDB 作为存储引擎，提供极低延迟。
- **类型安全查询**：HelixQL 100% 类型安全，确保查询在生产环境中执行。

## 使用方法

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

打开新创建的 `.hx` 文件，开始编写模式和查询。有关编写查询的更多信息，请参阅[文档](https://docs.helix-db.com/documentation/hql/hql)。

示例：

```
N::User {
   INDEX name: String,
   age: U32
}

QUERY getUser(user_name: String) =>
   user <- N<User>({name: user_name})
   RETURN user
```

### （可选）检查查询编译

```bash
helix check
```

### 部署查询到 API 端点

```bash
helix push dev
```

### 使用 SDK 调用

使用 [TypeScript SDK](https://github.com/HelixDB/helix-ts) 或 [Python SDK](https://github.com/HelixDB/helix-py) 调用。

TypeScript 示例：

```typescript
import HelixDB from 'helix-ts';

// 创建新的 HelixDB 客户端
// 默认端口为 6969
const client = new HelixDB();

// 查询数据库
await client.query('addUser', {
  name: 'John',
  age: 20,
});

// 获取创建的用户
const user = await client.query('getUser', {
  user_name: 'John',
});

console.log(user);
```

## 许可证

HelixDB 根据 AGPL（Affero General Public License）许可证授权。

## 商业支持

HelixDB 作为托管服务提供给选定用户。如果您有兴趣使用 Helix 的托管服务或需要企业支持，请[联系](mailto:founders@helix-db.com)我们以获取更多信息和部署选项。
