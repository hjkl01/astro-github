
---
title: tikv
---


# TiKV

> 项目地址: <https://github.com/tikv/tikv>

TiKV 是一个**高性能、可水平扩缩的分布式事务型键值存储**，兼容 TiDB 的二层存储引擎。它以 Rust 开发，提供 ACID 事务、强一致性以及海量数据水平扩容能力。

## 主要特性

| 特性 | 说明 |
|------|------|
| **事务型键值存储** | 实现了 TSO (Timestamp Oracle) + PAXOS/Raft 的两阶段提交，实现 2PC + 3PC 的 ACID 事务。 |
| **Raft 共识** | 每个 Region 内使用 Raft 保证顺序一致性和高可用，支持动态 Region 迁移与副本调度。 |
| **水平扩展** | 通过拆分 Region（default 128 MiB）实现数据分片，自动平衡负载。 |
| **快照隔离** | 采用 MVCC，支持多版本并发读写，提供 Snapshot Isolation。 |
| **多实例读写分离** | 通过 Placement Driver (PD) 实现节点发现与拓扑管理，兼容多租户。 |
| **高可用与弹性** | 支持抢占式 leader、故障转移、手动与自动恢复。 |
| **兼容 TiDB** | 作为 TiDB 的后端存储，支持 SQL 层、索引、事务等功能。 |
| **扩展插件机制** | 可驱动编辑器、CLI、开发者工具（DAG、Shell 等）。 |
| **跨语言 SDK** | 提供 Java/Golang/Rust/Go SDK 供外部应用直接读写。 |

## 主要功能

| 模块 | 作用 |
|------|------|
| **storage** | KV 存储层，交互层对外提供 API。 |
| **coprocessor** | 负责执行 Region 内的事务、索引查询等。 |
| **pd** | Placement Driver，负责拓扑管理、调度与心跳。 |
| **api** | 基于 gRPC 的 RPC 接口。 |
| **copr** | Coprocessor 处理器，基于 RocksDB 进行数据持久化。 |
| **raftstore** | Raft 运行时，用 Rust 维护 Peer 生命周期。 |
| **test** | 集成测试与性能基准测试脚本。 |

## 用法

### 1. 安装与启动

```bash
git clone https://github.com/tikv/tikv.git
cd tikv
make

# 启动 PD（单节点）
./pd-server --data-dir=./data/pd

# 启动 TiKV （单节点）
./tikv-server --pd=127.0.0.1:2379 --data-dir=./data/tikv
```

> **提示：** 在生产环境中，PD 与 TiKV 节点均需以集群方式配置，使用 `config.toml` 管理网络及副本策略。

### 2. 通过 TiDB 访问

1. 安装 TiDB，配置 `tikv` 作为后端。
2. 通过 `mysql` 客户端连接 TiDB，执行 SQL。

```bash
mysql -h 127.0.0.1 -P 4000 -u root
```

### 3. 直接使用 KV API

```rust
use tikv_client::{RawClient, Transaction};

let client = RawClient::new("127.0.0.1:20160");

client.put(b"key1", b"value1").unwrap();

let val = client.get(b"key1").unwrap();
println!("GET key1 = {:?}", val);

// 事务示例
let txn = client.begin().unwrap();
txn.put(b"tx_key", b"tx_value").unwrap();
txn.commit().unwrap();
```

> 同样可以使用 Java、Go、Python 等 SDK（官方请参阅 `go/getting-started.md`）。

### 4. 监控与管理

- **PD Dashboard**：访问 `http://<pd_host>:2379/status` 查看集群拓扑与 Region 分布。
- **TiKV API**：如 `http://<tikv_host>:20180/api/servers` 获取节点信息。
- **Prometheus**：在配置信息中开启 Exporter，收集指标。

### 5. 进行测试与基准

```bash
# 单元测试
make test

# 基准测试
./tools/benchmarks/run_benchmarks.sh
```

## 文档与社区

- 官方文档: <https://tikv.org/docs/>
- Contributing Guide: <https://github.com/tikv/tikv/blob/master/CONTRIBUTING.md>
- 邮件列表 / Slack: <https://github.com/tikv/tikv/discussions>

> TiKV 的生态正快速发展，社区对新的存储引擎特性如事后回滚、进制 log、云原生部署等持续贡献。

--- 

文件: `src/content/docs/00/tikv_tikv.md`
