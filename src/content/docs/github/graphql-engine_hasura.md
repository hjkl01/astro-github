
---
title: graphql-engine
---

# Hasura GraphQL Engine 项目

## 项目地址
[https://github.com/hasura/graphql-engine](https://github.com/hasura/graphql-engine)

## 主要特性
Hasura GraphQL Engine 是一个开源的即时 GraphQL API 引擎，主要用于快速将数据库转换为 GraphQL API。它支持多种数据库后端，包括 PostgreSQL、SQL Server、MySQL 等，并提供实时订阅、细粒度访问控制和事件触发等高级功能。核心特性包括：
- **即时 API 生成**：无需编写代码，即可从现有数据库 schema 自动生成 GraphQL 查询、变异（mutation）和订阅 API。
- **实时订阅**：支持 GraphQL 订阅，实现数据库变化的实时推送，使用 WebSocket 协议。
- **权限管理**：基于角色的访问控制（RBAC），允许定义复杂的权限规则，支持行级安全（RLS）。
- **事件触发**：集成 Webhook 和事件处理器，支持数据库事件触发外部服务。
- **多租户支持**：内置多租户架构，适合 SaaS 应用。
- **可扩展性**：支持自定义业务逻辑通过 Actions 和 Remote Schemas 集成外部 GraphQL 服务。
- **高性能**：基于 Haskell 构建，优化了查询执行和缓存机制。
- **开源与社区驱动**：Apache 2.0 许可，活跃社区，提供云托管版本（Hasura Cloud）。

## 主要功能
- **数据库集成**：连接到关系型数据库，自动暴露 GraphQL 接口，支持 SQL 查询优化和跟踪。
- **GraphQL API**：提供完整的 GraphQL 服务器，支持 introspection、查询验证和批处理。
- **实时数据同步**：通过订阅机制，实现客户端与服务器的实时数据更新。
- **安全性**：集成 JWT 认证、CORS 支持和 SQL 注入防护。
- **监控与调试**：内置查询分析、日志和性能指标，支持 Prometheus 集成。
- **迁移与版本控制**：支持数据库迁移工具（如 Hasura Metadata API），便于团队协作。
- **扩展功能**：允许添加自定义 resolver、聚合函数和第三方集成（如 Kafka、Stripe）。

## 用法
1. **安装与部署**：
   - 使用 Docker 快速启动：`docker run -p 8080:8080 hasura/graphql-engine:latest`。
   - 或通过 Helm 在 Kubernetes 上部署，支持 Hasura Cloud 托管。

2. **配置数据库**：
   - 启动后，访问 Hasura 控制台（默认 http://localhost:8080/console）。
   - 在控制台中添加数据库连接字符串（如 PostgreSQL 的 `postgres://user:pass@host:port/db`）。

3. **生成 API**：
   - 跟踪数据库 schema：控制台中选择 "Track" 所有表、视图和函数，即自动生成 GraphQL API。
   - 示例查询：使用 GraphiQL 接口测试，如 `{ users { id name } }`。

4. **设置权限**：
   - 在控制台的 "Permissions" 标签下，为每个角色定义查询/插入/更新/删除规则，使用 session 变量（如 JWT claims）。

5. **启用订阅**：
   - 跟踪表后，订阅自动可用。示例：`subscription { user(id: "1") { name } }`。

6. **高级用法**：
   - **Actions**：定义自定义变异，集成外部 API（如 REST endpoints）。
   - **Remote Schemas**：合并外部 GraphQL 服务到 Hasura 的 schema 中。
   - **事件**：配置数据库触发器，发送 Webhook 到外部服务。
   - 客户端集成：使用 Apollo Client 或 Relay 等库连接 GraphQL endpoint。

项目文档详见 GitHub 仓库的 README 和官方文档（https://hasura.io/learn/），适合后端开发者快速构建可扩展的 GraphQL 服务。