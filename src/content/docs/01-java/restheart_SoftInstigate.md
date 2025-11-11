---
title: restheart
---

# RESTHeart 项目概述

## 项目地址

[GitHub 项目地址](https://github.com/SoftInstigate/restheart)

## 主要特性

RESTHeart 是一个开源的、轻量级的 REST API 服务器，专为 MongoDB 设计。它将 MongoDB 数据库转换为符合 HATEOAS 原则的 RESTful API，支持现代 Web 开发需求。主要特性包括：

- **RESTful 接口**：提供完整的 CRUD 操作，支持 JSON 和 HAL 格式的响应。
- **安全性**：内置 JWT 认证、OAuth 2.0 支持，以及细粒度的访问控制（RBAC）。
- **插件架构**：可扩展性强，支持自定义拦截器、预处理器和安全插件。
- **高性能**：基于 Undertow NIO 服务器，使用 Java 21 虚拟线程，轻量级且异步非阻塞，支持高并发。
- **数据格式支持**：原生支持 JSON、BSON，以及 HAL（Hypertext Application Language）以实现超媒体链接。
- **监控与日志**：集成 Prometheus 监控、详细的访问日志和审计功能。
- **多协议支持**：兼容 WebSocket 和 SSE（Server-Sent Events）用于实时数据推送。

## 主要功能

RESTHeart 的核心功能是将 MongoDB 的 NoSQL 数据库暴露为 REST API，简化后端开发。主要功能包括：

- **资源管理**：支持数据库、集合、文档和查询资源的 REST 操作（GET、POST、PUT、DELETE、PATCH）。
- **查询与聚合**：集成 MongoDB 的查询语言，支持复杂查询、聚合管道和全文搜索。
- **文件服务**：内置 GridFS 支持，用于处理大文件上传和下载。
- **Schema 验证**：可选的 JSON Schema 验证，确保数据一致性。
- **批量操作**：支持批量插入、更新和删除操作，提高效率。
- **国际化与缓存**：支持多语言响应和 ETag-based 缓存机制。
- **集成工具**：易于与 Spring Boot、Node.js 等框架集成。

## 用法

### 安装与启动

1. **前提条件**：需要安装 MongoDB（版本 3.6+）和 Java 8+。
2. **下载**：从 GitHub Releases 下载最新 JAR 文件，或使用 Docker 镜像 `docker pull softinstigate/restheart`。
3. **配置**：编辑 `restheart.yml` 文件，配置 MongoDB 连接、端口（默认 8080）和安全设置。
4. **启动**：运行 `java -jar restheart-<version>.jar` 或使用 Docker：`docker run -it -p 8080:8080 softinstigate/restheart`。
5. **验证**：访问 `http://localhost:8080/`，RESTHeart 会自动创建默认数据库和集合。

### 基本用法示例

- **REST API**：
  - 创建集合：`POST /mycollection`（Body: JSON 数据）。
  - 查询文档：`GET /mycollection` 或 `GET /mycollection?filter={"name":"value"}`。
  - 分页和排序：`GET /mycollection?pagesize=10&page=1&sort={"name":1}`。
- **GraphQL API**：创建 GraphQL 应用定义，查询如 `{ people(filter: "{'age': {'$gt': 30}}") { _id name age } }`。
- **WebSocket**：连接 `ws://localhost:8080/ws/mycollection` 监听实时变更。
- **认证**：使用 JWT Token 在 Header 中添加 `Authorization: Bearer <token>`。
- **自定义插件**：实现 Java 接口并在配置文件中注册，支持 JavaScript 和 Python 插件。

详细文档和 API 示例请参考项目 Wiki。RESTHeart 适合构建微服务、API 网关或快速原型开发。
