---
title: questdb
---

# QuestDB 项目

**GitHub 项目地址:** [https://github.com/questdb/questdb](https://github.com/questdb/questdb)

## 主要特性

QuestDB 是一个开源的时间序列数据库，专为高性能数据摄入、查询和分析而设计。它采用 SQL 标准，支持实时数据流处理和大规模时间序列数据管理。主要特性包括：

- **高性能摄入**：支持每秒数百万行数据的导入，使用 SIMD 优化和零拷贝机制，确保低延迟数据摄入。
- **SQL 查询语言**：完全兼容 SQL，支持时间序列特定的函数，如 ASOF JOIN、SAMPLE BY 和时间分区查询。
- **列式存储**：基于列式存储引擎，优化了时间序列数据的压缩和查询速度，支持分区和索引。
- **实时流处理**：集成 ILP（Influx Line Protocol）和 PostgreSQL 协议，支持实时数据流和 WebSocket 订阅。
- **可扩展性**：无外部依赖，支持水平扩展和分布式部署，适用于云环境如 Kubernetes。
- **开源与免费**：采用 Apache 2.0 许可，完全开源，提供企业版高级功能。

## 主要功能

QuestDB 针对时间序列工作负载（如金融、IoT、监控和 DevOps）提供以下核心功能：

- **数据摄入**：通过 REST API、ILP、PostgreSQL 线协议或 CSV/Parquet 文件批量导入数据。支持自动分区和时间戳索引。
- **查询与分析**：执行复杂 SQL 查询，包括聚合、连接和时间窗口操作。内置可视化工具 Web Console，支持 Grafana 集成。
- **数据管理**：自动数据分区、TTL（生存时间）策略和数据保留规则。支持 WAL（预写日志）以确保数据持久性。
- **集成与生态**：兼容 Grafana、Prometheus 和 Telegraf 等工具；提供 JDBC/ODBC 驱动和 Python/Java 客户端库。
- **监控与安全**：内置 Prometheus 指标暴露、角色-based 访问控制（RBAC）和 TLS 加密。
- **部署选项**：支持单节点、集群模式和 Docker/Kubernetes 部署。

## 用法指南

### 安装
1. **下载二进制文件**：从 GitHub Releases 下载最新版本的 QuestDB（适用于 Linux、macOS 或 Windows）。
2. **Docker 部署**：
   ```
   docker run -p 9000:9000 -p 9009:9009 questdb/questdb
   ```
   - 端口 9000：Web Console（浏览器访问 http://localhost:9000）。
   - 端口 9009：ILP 摄入端口。
3. **Kubernetes**：使用 Helm Chart 部署，支持高可用集群。

### 基本用法
1. **启动服务器**：运行 `./questdb.sh start`（Linux/macOS）或 `questdb.exe start`（Windows）。
2. **数据摄入示例**（使用 ILP 协议，通过 curl）：
   ```
   curl -F data='trades,symbol=AAPL,side=buy price=150.5,amount=100 1640995200000000000' "http://localhost:9009/exec"
   ```
   这将插入一条带有时间戳的交易记录。
3. **SQL 查询示例**（在 Web Console 或客户端）：
   ```sql
   -- 创建表
   CREATE TABLE trades (
       timestamp TIMESTAMP,
       symbol SYMBOL,
       price DOUBLE,
       amount LONG
   ) TIMESTAMP(timestamp) PARTITION BY DAY;

   -- 查询最近一天的平均价格
   SELECT avg(price) FROM trades SAMPLE BY 1h WHERE timestamp > dateadd('d', -1, now());
   ```
4. **客户端集成**：
   - Python：使用 `questdb` 库连接并执行查询。
     ```python
     from questdb.ingress import Sender
     sender = Sender('localhost', 9009)
     sender.row('trades', timestamp='2023-01-01', symbol='AAPL', price=150.5, amount=100)
     sender.flush()
     ```
   - Java：通过 JDBC 驱动连接 `jdbc:postgresql://localhost:8812/qdb`。

### 高级用法
- **配置**：编辑 `server.conf` 文件自定义存储路径、端口和性能参数。
- **监控**：访问 `/metrics` 端点集成 Prometheus，或使用内置的系统查询如 `SHOW TABLES`。
- **扩展**：对于生产环境，启用集群模式以实现数据复制和高可用。

更多细节请参考官方文档：https://questdb.io/docs/。