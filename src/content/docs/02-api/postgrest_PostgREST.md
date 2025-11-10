---
title: postgrest
---

# PostgREST 项目概述

## 项目地址
[https://github.com/PostgREST/postgrest](https://github.com/PostgREST/postgrest)

## 主要特性
PostgREST 是一个开源工具，用于将 PostgreSQL 数据库直接暴露为 RESTful API。它基于 Haskell 语言开发，具有以下核心特性：
- **自动生成 REST API**：无需编写额外代码，即可从数据库 schema 自动生成完整的 CRUD（创建、读取、更新、删除）端点。
- **高性能**：利用 PostgreSQL 的强大查询能力，支持高效的实时数据处理和复杂查询。
- **安全性**：集成 PostgreSQL 的行级安全（RLS）策略，确保数据访问控制。
- **实时支持**：通过 PostgreSQL 的通知机制，提供 WebSocket 支持，实现实时数据更新。
- **类型安全**：API 响应严格遵循数据库 schema，支持 JSON 和其他格式。
- **轻量级**：无需额外的数据库层，直接连接 PostgreSQL，减少架构复杂性。

## 主要功能
PostgREST 的功能主要围绕 REST API 的实现，包括：
- **资源端点**：为数据库表和视图自动创建 GET、POST、PUT、PATCH、DELETE 等 HTTP 方法，支持分页、过滤、排序和联接查询。
- **查询优化**：支持嵌入式资源（embeds）、过滤器（filters，如 eq、gt、ilike）和聚合函数。
- **认证与授权**：支持 JWT、API 密钥等多种认证方式，与 PostgreSQL 的权限系统无缝集成。
- **批量操作**：允许批量插入、更新和删除操作，提高效率。
- **媒体类型处理**：支持 multipart/form-data 用于文件上传，以及自定义媒体类型。
- **扩展性**：可通过 PostgreSQL 扩展（如 PostGIS）增强地理空间查询等功能。

## 用法
### 安装
1. 确保已安装 PostgreSQL（版本 9.4 或更高）。
2. 通过 Stack（推荐）或 Docker 安装 PostgREST：
   - 使用 Stack：`stack install postgrest`。
   - 使用 Docker：`docker run --name postgrest -p 3000:3000 postgrest/postgrest`。

### 配置
1. 创建一个配置文件（例如 `openresty.conf` 或直接通过命令行参数）：
   ```
   db-uri = "postgres://user:pass@localhost/dbname"
   db-schema = "public"
   db-anon-role = "web_anon"
   server-host = "0.0.0.0"
   server-port = 3000
   jwt-secret = "your-secret-key"
   ```
   - `db-uri`：数据库连接字符串。
   - `db-anon-role`：匿名访问角色（需在 PostgreSQL 中预先创建）。

2. 在 PostgreSQL 中设置行级安全：
   ```sql
   ALTER TABLE your_table ENABLE ROW LEVEL SECURITY;
   CREATE POLICY "policy_name" ON your_table FOR ALL USING (auth_user() = user_id);
   ```

### 运行
启动服务器：
```
postgrest openresty.conf
```
API 将在 `http://localhost:3000` 上可用。例如：
- 获取所有用户：`GET /users`
- 过滤用户：`GET /users?age=gt.18`
- 创建用户：`POST /users` with JSON body。

### 示例用法
假设有一个 `users` 表，API 调用：
- `GET /users?id=eq.1`：获取 ID 为 1 的用户。
- `POST /users`：body `{"name": "Alice", "age": 30}` 创建新用户。
- 支持 OData-like 语法进行复杂查询，如联接：`GET /users?select=name,posts(title)`。

更多细节请参考官方文档：https://postgrest.org/en/stable/。