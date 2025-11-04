
---
title: risingwave
---


# RisingWave – 一个高速实时 OLAP 数据平台

**项目地址**: <https://github.com/risingwavelabs/risingwave>

## 一、项目简介
RisingWave 是面向 SaaS 和企业内部应用的实时 OLAP 数据实验室级系统，结合了流式处理、批处理、SQL 完整性与低时延，构建为无服务器、弹性可扩展的数据湖接入层。核心目标是让业务团队能够通过标准 SQL 近乎零延迟地访问海量实时事务数据，支持即时查询、分析和报表。

## 二、主要特性
| 特性 | 说明 |
|------|------|
| **流式 + 批处理一体** | 支持 `INSERT`, `SELECT`, `CREATE STREAM` 等 SQL 语句，通过 Flink 核心实现流式处理与批量查询无缝融合。 |
| **高并发低延迟** | 内存计算 + 列式存储 + 高效索引，单条查询延迟低至数百毫秒，吞吐量可达千万行每秒。 |
| **原生 PostgreSQL 兼容** | 提供完全相同的客户端/驱动接口，业务代码无需改动即可访问 RisingWave。 |
| **弹性伸缩** | 支持水平扩容，节点动态加入/剔除，数据自动重分区。 |
| **可观测性** | 支持系统监控、查询执行计划、诊断工具（`SHOW STATS`, `EXPLAIN` 等）。 |
| **安全与多租户** | IAM/RBAC、资源隔离，支持多租户安全模型。 |
| **多协议上传/下载** | 支持对象存储（S3/MinIO）、文件系统、Kafka、Message Queue 等多源接入与输出。 |
| **高可靠性** | 持久化 WAL 与投影函数，节点崩溃后可通过 WAL 回放恢复。 |

## 三、核心功能
- **实时 OLAP**：Federated View、Window函数、聚合、CTE、相对增量查询。  
- **弹性查询**：支持批量查询、窗口查询和近实时查询，返回半实时结果。  
- **链接多源**：通过 `CREATE TABLE` 连接各种外部数据源（Kafka、RabbitMQ、HTTP、S3等）。  
- **物化视图**：自动维护物化视图，提升重复查询性能。  
- **分区与压缩**：列式压缩 + 动态分区，提高存储密度与查询效率。  
- **CI/CD 集成**：支持 Operator、Helm Chart，易于在 Kubernetes 中部署。  

## 四、快速上手

```bash
# 1. 拉取源码
git clone https://github.com/risingwavelabs/risingwave.git
cd risingwave

# 2. 本地构建（需 Docker）
make docker-build

# 3. 启动单机 Demo
make start-single-node

# 4. 进入 PostgreSQL 客户端
psql -h 127.0.0.1 -p 4566 -U root
```

```sql
-- 创建外部 Kafka 表
CREATE TABLE my_table (
    id INT,
    value STRING
) WITH (
    "connector" = 'kafka',
    "topic" = 'my_topic',
    "properties.bootstrap.servers" = 'localhost:9092',
    "format" = 'json'
);

-- 实时查询
SELECT * FROM my_table LIMIT 10;
```

## 五、部署与运维

- **Kubernetes**：使用官方 Helm Chart (`helm install risingwave risingwave/risingwave --namespace risingwave -f values.yaml`)。
- **升级**：拉取新版本 `git pull`，执行 `make operator-upgrade` 或 `helm upgrade`。
- **日志与监控**：Prometheus 支持，Grafana 面板可直接导入。

## 六、常见问题排查

```bash
# 查看节点状态
risingwave_ctl status

# 查看 WAL 状态
risingwave_ctl wal-status

# 重建索引
risingwave_ctl rebuild-indexes
```

> 详细文档请参阅项目 Wiki 或官方文档。

---

> 以上内容已保存至 `src/content/docs/00/risingwave_risingwavelabs.md`。