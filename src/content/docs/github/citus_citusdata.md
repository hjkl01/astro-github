
---
title: citus
---

# Citus 项目概述

## 项目地址
[GitHub 项目地址](https://github.com/citusdata/citus)

## 主要特性
Citus 是一个开源的 PostgreSQL 扩展，将 PostgreSQL 扩展为分布式数据库。它支持水平扩展（sharding），允许将数据分布到多个节点上，从而处理大规模数据集和查询。主要特性包括：
- **分布式查询处理**：将 SQL 查询分布到多个 PostgreSQL 节点上执行，支持复杂查询如 JOIN、聚合和窗口函数。
- **水平分片（Sharding）**：根据分片键自动将表分布到多个工作节点，提高性能和可扩展性。
- **多租户支持**：适合 SaaS 应用，按租户 ID 分片数据，实现隔离和高效查询。
- **实时分析**：结合 PostgreSQL 的 OLTP 和 OLAP 能力，支持实时数据摄取和分析。
- **高可用性**：集成 PostgreSQL 的复制和故障转移机制，支持分布式事务和一致性。
- **与 PostgreSQL 兼容**：无缝集成现有 PostgreSQL 工具和扩展，如 PostGIS、TimescaleDB 等。

## 主要功能
- **数据分发**：使用分片键（如用户 ID 或时间戳）将数据分布到集群中的节点。
- **查询路由**：协调节点自动路由查询到相关分片，支持跨分片 JOIN 和子查询。
- **扩展管理**：通过 Citus 协调器节点管理集群，自动处理负载均衡和节点添加/移除。
- **列式存储**：可选集成列式存储以优化分析查询性能。
- **集成工具**：支持 pgAdmin、psql 等工具，以及与 Kafka、Spark 等生态系统的集成。

## 用法
1. **安装**：
   - 在 Ubuntu/Debian 上：使用包管理器安装 Citus 扩展，例如 `apt install postgresql-15-citus-11.2`（版本需匹配 PostgreSQL）。
   - 源码安装：克隆仓库，编译并安装扩展。

2. **设置集群**：
   - 初始化 PostgreSQL 实例作为协调器节点。
   - 在协调器上启用扩展：`CREATE EXTENSION citus;`
   - 添加工作节点：使用 `SELECT citus_add_node('hostname', port);` 注册节点。
   - 创建分布式表：`SELECT create_distributed_table('table_name', 'shard_key');`

3. **使用示例**：
   - 插入数据：标准 SQL INSERT 会自动分发到节点。
   - 查询：执行 SELECT、UPDATE 等查询，Citus 会优化路由。
   - 监控：使用 `SELECT * FROM citus_shards;` 查看分片状态。

更多细节请参考官方文档：https://docs.citusdata.com/en/stable/