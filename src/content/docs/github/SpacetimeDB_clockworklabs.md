
---
title: SpacetimeDB
---

```markdown
# SpacetimeDB (Clockwork Labs)

**仓库地址**:  
<https://github.com/clockworklabs/SpacetimeDB>

## 主要特性

| 功能 | 描述 |
|------|------|
| 时间旅行查询 | 支持对任意历史版本的数据进行查询，便于审计与回溯。 |
| 增量计算 | 采用增量算法，仅计算变化部分，显著提升实时分析性能。 |
| SQL 接口 | 内置 ANSI‑SQL 子集，直接使用 `SELECT/INSERT/UPDATE/DELETE` 语句。 |
| 事件驱动存储 | 内建事件流引擎，支持 OCC、CQRS、Event Sourcing 等模式。 |
| 零写延迟 | Append‑only 结构，写入立即可见，低延迟并发。 |
| 可扩展性 | 支持多节点 Raft 复制，水平扩容。 |
| 安全 | RBAC 与 TLS 加密传输。 |

## 核心功能

- **表与索引**：声明式表定义，自动生成 B‑Tree/Merkle 索引。  
- **事务**：ACID 事务，MVCC 多版本并发控制。  
- **视图 & Materialized**：查询视图与自动刷新。  
- **触发器**：支持 Rust / SQL 脚本触发。  
- **时间维度**：按时间分区，`WHERE ts >= ... AND ts < ...` 高效。  
- **备份/恢复**：增量快照，节点间同步恢复。  

## 快速上手

```bash
# 1. 安装命令行工具
cargo install spacetimedb-cli

# 2. 启动数据库
spacetimedb run --data ./data

# 3. 使用 SQL 客户端连接（默认端口 5432）
psql spacetimedb://localhost:5432/mydb?user=spacetime

# 4. 示例：创建表、插入数据、时间旅行查询
CREATE TABLE events (
    id BIGINT PRIMARY KEY,
    ts TIMESTAMP,
    payload JSONB
);

INSERT INTO events VALUES (123, '2025-10-28T12:00:00Z', '{"value": 42}');

SELECT * FROM events AT (TIMESTAMP '2025-10-27T12:00:00Z');
```

## 开发与贡献

- **代码结构**：`src/`（核心引擎）、`sql/`（解析器）、`tests/`（集成测试）。  
- **编译**：Rust 1.75+，`cargo build`。  
- **贡献指南**：详见 `CONTRIBUTING.md`。  

## 参考文档

- 官方文档: <https://clockworklabs.github.io/SpacetimeDB>  
- 社区讨论: GitHub Discussions / Discord  

---  
**注**：以上为项目核心特性与使用示例，功能实现细节请参考仓库源码与官方文档。
