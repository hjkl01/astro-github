---
title: FerretDB
---

# FerretDB 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/FerretDB/FerretDB)

## 主要特性
FerretDB 是一个开源的 MongoDB 兼容数据库替代方案，它使用 PostgreSQL 作为后端存储引擎。主要特性包括：
- **MongoDB 协议兼容**：完全支持 MongoDB 的 Wire Protocol，允许现有 MongoDB 驱动、工具和应用程序无缝迁移。
- **开源与免费**：采用 Apache 2.0 许可，无需付费，支持社区贡献和自定义扩展。
- **高性能与可扩展**：基于 PostgreSQL 的可靠性和 ACID 事务支持，适用于高负载场景。
- **多语言支持**：提供 Go、C++ 等语言实现的后端选项，便于集成。
- **安全与合规**：内置认证、授权和加密功能，符合企业级安全标准。

## 主要功能
FerretDB 的核心功能聚焦于提供 MongoDB-like 的数据库服务：
- **CRUD 操作**：支持创建、读取、更新和删除文档，兼容 MongoDB 的查询语言（例如 find、insert、update、delete）。
- **聚合管道**：实现 MongoDB 的聚合框架，用于数据处理、过滤和转换。
- **索引与查询优化**：利用 PostgreSQL 的索引机制，支持高效的全文搜索和排序。
- **副本集与分片**：通过配置支持高可用性和水平扩展。
- **集成工具**：兼容 MongoDB Compass、mongosh 等工具，以及各种 ORM 框架（如 Mongoose）。

## 用法
### 安装
1. **使用 Docker（推荐快速启动）**：
   ```
   docker run --rm -p 27017:27017 -e FDB_POSTGRESQL_URL="postgres://postgres:password@localhost:5432" ferretdb/ferretdb
   ```
   这将启动 FerretDB 服务，监听 27017 端口，并连接到 PostgreSQL 实例。

2. **从源代码构建**：
   - 克隆仓库：`git clone https://github.com/FerretDB/FerretDB.git`
   - 安装依赖：确保有 Go 1.20+ 和 PostgreSQL。
   - 构建：`make build`
   - 运行：`./bin/ferretdb -config config.yaml`

### 基本用法
1. **连接数据库**：
   使用 MongoDB 客户端连接 `mongodb://127.0.0.1:27017`。

2. **创建数据库和集合**：
   在客户端（如 mongosh）中执行：
   ```
   use mydb
   db.mycollection.insertOne({ name: "example", value: 123 })
   ```

3. **查询数据**：
   ```
   db.mycollection.find({ value: { $gt: 100 } })
   ```

4. **配置 PostgreSQL 后端**：
   编辑配置文件指定 PostgreSQL URL，例如：
   ```
   postgresql_url: "postgres://user:pass@host:port/dbname"
   ```

更多详细用法请参考官方文档：https://docs.ferretdb.io/