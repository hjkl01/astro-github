---
title: ydb
---

# YDB 项目

**GitHub 项目地址：** [https://github.com/ydb-platform/ydb](https://github.com/ydb-platform/ydb)

## 主要特性
YDB（Yandex Database）是一个分布式 SQL 数据库系统，由 Yandex 开发，旨在提供高性能、高可用性和可扩展性。它支持 ACID 事务、分布式存储和多租户隔离。主要特性包括：
- **分布式架构**：支持水平扩展，可处理 PB 级数据和数百万 QPS 的查询负载。
- **多 API 支持**：兼容 SQL（基于 YQL）、Table API（键值存储）和脚本化查询。
- **高可用性**：内置复制、故障转移和自动分片，确保数据耐久性和系统稳定性。
- **强一致性**：提供分布式事务支持，适用于金融、游戏和大数据分析等场景。
- **开源与云原生**：完全开源，支持自托管或云部署，集成 Kubernetes 等现代基础设施。

## 主要功能
YDB 的核心功能聚焦于分布式数据管理和查询处理：
- **数据存储**：支持结构化数据（表）、半结构化数据（JSON）和时间序列数据。
- **查询引擎**：YQL 查询语言（类似于 SQL），结合优化器和执行引擎，实现高效查询。
- **事务管理**：支持读写事务、快照隔离和乐观并发控制。
- **监控与运维**：内置监控工具、备份/恢复机制，以及与 Prometheus/Grafana 的集成。
- **扩展性**：模块化设计，便于自定义存储后端（如本地磁盘或对象存储）。

## 用法
YDB 的用法主要通过命令行工具、客户端库或集成 API 进行部署和操作。以下是基本步骤：

### 1. 安装与部署
- **前提**：需要 Go 1.20+ 或 Docker。克隆仓库：`git clone https://github.com/ydb-platform/ydb.git`。
- **构建**：运行 `make` 命令编译二进制文件，或使用 Docker 镜像 `docker pull ydbplatform/ydb`。
- **单节点部署**（测试用）：启动服务器 `ydb -s`。
- **集群部署**：使用 Helm Chart 在 Kubernetes 上部署，或手动配置多节点集群（需设置域和租户）。

### 2. 连接与查询
- **客户端工具**：使用 `ydb` CLI 工具连接数据库，例如：
  ```
  ydb database create --endpoint=grpcs://ydb.example.com:2135 mydb
  ydb table query execute --database=/mydb --endpoint=grpcs://ydb.example.com:2135 "SELECT * FROM mytable;"
  ```
- **编程集成**：支持多种语言 SDK（如 Go、Python、Java）。示例（Python）：
  ```python
  from ydb import Driver, SessionPool, Session
  driver = Driver(endpoint='grpcs://ydb.example.com:2135', database='/mydb', credentials={...})
  pool = SessionPool(driver)
  with pool.checkout() as session:
      session.execute('CREATE TABLE mytable (id Uint64, name Utf8, PRIMARY KEY (id));')
  ```
- **高级用法**：创建租户 `ydb tenant create`，管理表 `ydb table create`，执行脚本化查询或批量导入数据。

更多细节请参考仓库的 [文档](https://ydb.tech/docs/) 和示例代码。