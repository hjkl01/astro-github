---
title: prest
---

# PREST 项目

## 项目地址
[GitHub 项目地址](https://github.com/prest/prest)

## 主要特性
PREST（PostgreSQL RESTful API）是一个开源工具，用于将 PostgreSQL 数据库直接暴露为 RESTful API。它具有以下主要特性：
- **自动生成 API**：无需编写代码，即可基于数据库 schema 自动创建 RESTful 端点，支持 CRUD 操作（创建、读取、更新、删除）。
- **安全性**：内置 JWT 认证、角色-based 访问控制（RBAC），并支持数据库级别的权限管理。
- **高性能**：使用 Go 语言开发，支持并发处理和连接池优化，适用于高负载场景。
- **可扩展性**：允许自定义钩子（hooks）、中间件和扩展，支持 GraphQL 查询（通过插件）。
- **易集成**：兼容 OpenAPI 规范，可生成 Swagger 文档，便于前端或移动应用集成。
- **轻量级**：无外部依赖，易于部署，支持 Docker 和 Kubernetes。

## 主要功能
- **RESTful 接口**：提供 GET、POST、PUT、DELETE 等 HTTP 方法，直接操作数据库表、视图和存储过程。
- **认证与授权**：支持 JWT token、OAuth 和基本认证；可配置数据库角色来限制访问。
- **查询优化**：内置 SQL 注入防护、参数化查询；支持分页、排序和过滤。
- **监控与日志**：集成 Prometheus 指标、详细的请求日志，便于调试和性能监控。
- **自定义路由**：允许定义自定义端点和处理逻辑，通过配置文件或代码扩展。
- **数据导出**：支持 JSON、CSV 等格式导出查询结果。

## 用法
1. **安装**：
   - 通过 Go 安装：`go install github.com/prest/prest/cmd/prest@latest`。
   - 使用 Docker：`docker run --rm -p 3000:3000 prest/prest:latest`。

2. **配置**：
   - 创建配置文件 `prest.toml` 或使用环境变量设置数据库连接（如 `DB_CONNECTION_STRING=postgres://user:pass@localhost/db`）。
   - 示例配置：
     ```
     [prest]
     port = 3000
     jwt_secret = "your-secret-key"
     [database]
     host = "localhost"
     port = 5432
     user = "postgres"
     password = "password"
     dbname = "mydb"
     ```

3. **运行**：
   - 命令行启动：`prest start`。
   - API 端点自动生成，例如：`GET /schema/table` 查询表数据；`POST /schema/table` 插入数据。
   - 认证示例：使用 `/auth` 端点获取 JWT token，然后在请求头中携带 `Authorization: Bearer <token>`。

4. **高级用法**：
   - 自定义钩子：在配置文件中添加预/后处理脚本（如 Lua 或 Go 函数）。
   - 生成文档：访问 `/swagger` 端点查看 OpenAPI 文档。
   - 扩展：通过插件系统添加 GraphQL 支持或自定义中间件。

更多详情请参考项目 README。