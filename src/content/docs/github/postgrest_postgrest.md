
---
title: postgrest
---

# PostgREST 项目

## 项目地址
[https://github.com/postgrest/postgrest](https://github.com/postgrest/postgrest)

## 主要特性
PostgREST 是一个开源工具，用于将 PostgreSQL 数据库自动转换为符合 RESTful 标准的 Web API。它的主要特性包括：
- **自动 API 生成**：无需编写额外代码，即可基于数据库 schema 自动生成完整的 REST API，支持 CRUD 操作（创建、读取、更新、删除）。
- **安全性**：内置基于角色的访问控制 (RBAC)，支持 JWT 令牌认证，并可集成 PostgreSQL 的行级安全 (RLS) 策略，确保数据访问的安全性。
- **高性能**：直接利用 PostgreSQL 的查询优化器，支持分页、过滤、排序和聚合等高级查询功能，响应速度快。
- **标准符合**：完全遵守 HTTP/REST 规范，支持 JSON、CSV 等数据格式，并处理事务和并发。
- **轻量级**：单二进制文件部署，无需额外的服务器框架，易于扩展和集成。

## 主要功能
- **资源操作**：通过 HTTP 方法（如 GET、POST、PUT、DELETE）直接操作数据库表或视图，例如 GET /table 获取数据，POST /table 插入记录。
- **查询过滤**：支持 URL 参数进行复杂查询，如过滤（eq、gt、ilike）、排序（order）、分页（limit、offset）和关联（embed 外键关系）。
- **认证与授权**：使用 JWT 或 API 密钥进行身份验证，并通过数据库权限控制访问。
- **事务支持**：自动处理数据库事务，确保数据一致性；支持批量操作和存储过程调用。
- **扩展性**：可自定义端点、处理文件上传，并与 PostgREST 的 OpenAPI 规范集成生成文档。

## 用法
1. **安装**：从 GitHub Releases 下载二进制文件，或使用 Docker 镜像 `postgrest/postgrest`。例如：
   ```
   docker run --name postgrest -p 3000:3000 \
     -e PGRST_DB_URI="postgres://user:pass@localhost/dbname" \
     -e PGRST_DB_SCHEMA="public" \
     -e PGRST_DB_ANON_ROLE="web_anon" \
     postgrest/postgrest
   ```

2. **配置**：创建配置文件 `postgrest.conf`，指定数据库连接、schema、角色等参数：
   ```
   db-uri = "postgres://user:pass@localhost/dbname"
   db-schema = "public"
   db-anon-role = "web_anon"
   server-host = "0.0.0.0"
   server-port = 3000
   jwt-secret = "your-secret-key"
   ```

3. **运行**：执行 `./postgrest postgrest.conf` 启动服务器。API 端点即为 `http://localhost:3000/`，如 GET /users 获取 users 表数据。

4. **示例查询**：
   - 获取所有用户：`GET /users`
   - 过滤用户：`GET /users?age=gt.18&name=ilike.*john*`
   - 插入数据：`POST /users` with JSON body `{"name": "John", "age": 30}`

更多详情请参考项目文档。