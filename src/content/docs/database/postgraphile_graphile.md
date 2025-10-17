
---
title: postgraphile
---

# PostGraphile 项目

## 项目地址
[https://github.com/graphile/postgraphile](https://github.com/graphile/postgraphile)

## 主要特性
PostGraphile 是一个快速、强大的、扩展性的工具，用于从 PostgreSQL 数据库自动生成实时 GraphQL API。它专注于性能和简单性，支持以下核心特性：
- **自动生成 GraphQL Schema**：基于 PostgreSQL 数据库模式（schema）自动推断并生成完整的 GraphQL 类型、查询、变更和订阅，而无需编写额外的代码。
- **实时订阅支持**：集成 PostgreSQL 的 LISTEN/NOTIFY 机制，提供实时数据更新，通过 GraphQL Subscriptions 实现。
- **高度可扩展**：支持插件系统，用户可以自定义插件来扩展功能，如添加认证、授权、自定义字段或集成第三方服务。
- **性能优化**：内置连接池管理、查询优化和缓存机制，确保高并发场景下的高效运行。
- **类型安全**：生成的 GraphQL Schema 与 PostgreSQL 的数据类型紧密对应，支持输入验证和错误处理。
- **无代码生成**：零配置启动，适合快速原型开发，同时支持高级自定义以适应复杂需求。

## 主要功能
- **查询和变更操作**：自动生成 CRUD（创建、读取、更新、删除）操作，支持复杂查询如过滤、分页、排序和关联关系。
- **权限控制**：基于 PostgreSQL 的行级安全（RLS）和角色系统，实现细粒度访问控制。
- **智能关系处理**：自动检测并处理数据库中的一对多、多对多关系，支持嵌套查询。
- **批处理和事务支持**：允许批量变更操作，并确保数据一致性。
- **监控和调试**：内置日志、指标收集和 GraphQL  playground，用于开发和生产环境调试。
- **多租户支持**：通过插件或配置支持多数据库 schema 或多租户隔离。

## 用法
### 安装
使用 npm 或 yarn 安装：
```
npm install postgraphile
```
或全局安装 CLI 工具：
```
npm install -g postgraphile
```

### 基本启动
通过 CLI 快速启动服务器：
```
postgraphile -c postgres://username:password@localhost:5432/database
```
这将连接到指定的 PostgreSQL 数据库，并暴露 GraphQL API 于默认端口 5000（http://localhost:5000/graphql）。

### Node.js 集成
在 Node.js 应用中集成：
```javascript
const postgraphile = require('postgraphile');
const express = require('express');
const app = express();

app.use(postgraphile('postgres://username:password@localhost:5432/database', 'public', {
  graphiql: true,  // 启用 GraphiQL 接口
  enhanceGraphiql: true,  // 增强 GraphiQL 体验
}));

app.listen(5000, () => {
  console.log('Server running on http://localhost:5000/graphql');
});
```

### 高级配置
- **插件使用**：例如添加 JWT 认证插件：
  ```
  npm install postgraphile-plugin-connection-filter
  ```
  在配置中启用：
  ```javascript
  postgraphile(dbUrl, 'public', {
    appendPlugins: [require('postgraphile-plugin-connection-filter').default],
  });
  ```
- **自定义选项**：通过选项对象配置，如忽略某些表、添加自定义查询或设置 CORS。
- **生产部署**：结合 PM2 或 Docker 部署，支持环境变量配置数据库连接。

更多细节请参考官方文档：https://www.graphile.org/postgraphile/