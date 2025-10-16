
---
title: cockroach
---

# CockroachDB 项目

## 项目地址
[GitHub 项目地址](https://github.com/cockroachdb/cockroach)

## 主要特性
CockroachDB 是一个开源的分布式 SQL 数据库，设计灵感来源于 Google 的 Spanner 和 F1 系统。它具有以下主要特性：
- **分布式架构**：支持水平扩展，通过多节点集群实现高可用性和容错能力，即使在节点故障时也能保持数据一致性。
- **SQL 兼容性**：完全兼容 PostgreSQL 的 SQL 语法和驱动程序，便于从传统数据库迁移。
- **强一致性**：采用 Raft 共识算法，确保事务的 ACID 属性，支持全局分布式事务。
- **高可用性和弹性**：自动数据复制、故障转移和自我修复，支持地理分布式部署。
- **可扩展性**：线性扩展读写性能，支持 PB 级数据存储，无单点瓶颈。
- **多租户支持**：内置多租户隔离，适合云原生环境。

## 主要功能
CockroachDB 提供了一系列核心功能，适用于构建可靠的分布式应用：
- **分布式事务**：支持跨节点的事务处理，确保数据一致性。
- **自动分片和复制**：数据自动分片（sharding）和多副本复制，提高性能和耐久性。
- **备份与恢复**：企业级备份工具，支持增量备份和点-in-time 恢复。
- **变更数据捕获 (CDC)**：实时捕获数据变更，集成 Kafka 等流式系统。
- **安全与合规**：角色-based 访问控制 (RBAC)、加密传输和存储，符合 GDPR 等标准。
- **监控与运维**：内置内置的 Prometheus 指标、SQL 调试和集群管理工具。

## 用法
### 安装
1. **下载二进制文件**：从 GitHub Releases 下载适合平台的 cockroach 包。
2. **单节点启动**（开发模式）：
   ```
   cockroach start-single-node --insecure --listen-addr=localhost
   ```
3. **多节点集群**（生产模式）：
   - 初始化集群：`cockroach start --certs-dir=certs --listen-addr=localhost`
   - 加入节点：使用 `--join` 标志连接现有节点。
   - 启用安全：使用证书配置 TLS。

### 基本用法
1. **启动 SQL 客户端**：
   ```
   cockroach sql --insecure --host=localhost
   ```
2. **创建数据库和表**：
   ```sql
   CREATE DATABASE bank;
   USE bank;
   CREATE TABLE accounts (id INT PRIMARY KEY, balance INT);
   INSERT INTO accounts VALUES (1, 1000);
   ```
3. **执行查询**：支持标准 SQL 操作，如 SELECT、UPDATE、JOIN 等。
4. **监控集群**：访问内置 Web UI（默认端口 8080）查看节点状态、查询性能。
5. **集成应用**：使用 PostgreSQL 驱动连接，例如在 Go/Python 中：
   - Go: `import "github.com/cockroachdb/cockroach-go/v2/driver"`
   - Python: 使用 `psycopg2` 库。

更多详细用法请参考官方文档：https://www.cockroachlabs.com/docs