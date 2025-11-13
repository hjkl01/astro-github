---
title: arangodb
---

# ArangoDB 项目

## 项目地址
[https://github.com/arangodb/arangodb](https://github.com/arangodb/arangodb)

## 主要特性
ArangoDB 是一个开源的多模型数据库，支持图、文档和键值存储模型。它结合了 NoSQL 的灵活性和关系数据库的强大查询能力。主要特性包括：
- **多模型支持**：无缝集成文档、图和键值数据模型，无需多个数据库系统。
- **ACID 事务**：支持分布式事务，确保数据一致性和完整性。
- **AQL 查询语言**：ArangoDB 查询语言（AQL）是一种声明式语言，支持复杂查询、JOIN 操作和图遍历。
- **高性能和可扩展性**：支持水平扩展，通过分片和复制实现高可用性。
- **Foxx 服务**：内置微服务框架，允许在数据库中直接运行 JavaScript 服务。
- **集成工具**：提供 Web 界面（arangodb）、驱动程序（支持多种编程语言）和 API 接口。
- **开源与社区**：采用 Apache 2.0 许可，社区活跃，支持企业版扩展功能如集群管理和备份。

## 主要功能
- **数据存储与检索**：存储 JSON 文档，支持键值对和图边/顶点结构。功能包括索引（哈希、全文、地理空间）、聚合和过滤。
- **图数据库功能**：内置图算法，如最短路径、社区检测和 PageRank，支持复杂网络分析。
- **查询与分析**：AQL 支持子查询、排序、分组和聚合，适用于 OLTP 和 OLAP 场景。
- **安全与管理**：用户认证、角色-based 访问控制（RBAC）、审计日志和备份/恢复工具。
- **集成与扩展**：支持 RESTful API、GraphQL 和多种客户端库（Java、Python、Node.js 等）。Foxx 允许自定义后端服务。
- **部署选项**：单节点、集群模式，支持 Docker、Kubernetes 和云部署。

## 用法
1. **安装**：
   - 下载二进制文件或使用包管理器（如 apt、yum）。
   - Docker 示例：`docker run -p 8529:8529 arangodb/arangodb`。
   - 启动服务器：运行 `arangod` 命令，默认端口 8529。

2. **基本操作**：
   - 通过 Web 界面访问 `http://localhost:8529`，创建数据库和集合。
   - 使用 AQL 查询示例：在 Web 界面或客户端执行：
     ```
     FOR u IN users
       FILTER u.age > 25
       RETURN u.name
     ```
     这将返回年龄大于 25 的用户姓名。

3. **图数据用法**：
   - 创建图：`db._createGraph("social", ["users", "friends"]);`（users 为顶点集合，friends 为边集合）。
   - 查询图：`FOR v, e IN 1..2 OUTBOUND 'users/123' GRAPH 'social' RETURN v;`（遍历朋友关系）。

4. **编程集成**：
   - Python 示例（使用 pyArango 库）：
     ```python
     from pyArango.connection import Connection
     conn = Connection(arangoURL="http://localhost:8529", username="root", password="password")
     db = conn["mydb"]
     aql = db.AQLQuery("FOR doc IN %%s RETURN doc", "collection", batchSize=1000)
     for row in aql.result:
         print(row)
     ```
   - 更多驱动程序见官方文档。

5. **高级用法**：
   - 部署集群：配置代理节点和数据节点，使用 `arangodb` 工具管理。
   - 开发 Foxx 服务：使用 `@arangodb/foxx` CLI 创建和部署服务。
   - 参考官方文档：https://docs.arangodb.com/ 以获取详细教程和 API 参考。