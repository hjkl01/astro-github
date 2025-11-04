
---
title: reth
---


# Reth – 以太坊客户端与工具集

**项目地址**：<https://github.com/paradigmxyz/reth>

Reth 是一个完全用 Rust 编写的以太坊客户端，目标是提供更高性能、内存占用更低、易于扩展的以太坊实现。它同时包含与以太坊兼容的工具链，帮助开发者快速构建和调试区块链应用。

## 主要特性

- **高性能**  
  - 用 Rust写，利用零成本抽象实现低延迟和高吞吐量。  
  - 支持 **内存优势** 的块缓存和快速状态同步。
- **模块化架构**  
  - 分离数据库、网络、共识、执行以及 API 层，易于单元化测试和定制。  
  - 通过插件方式可以替换不同的网络或共识实现。
- **兼容以太坊**  
  - 遵循以太坊 2.0 及 EIPs，兼容现有合约与工具。  
  - 支持 `GETH` 兼容的 RPC 接口（JSON‑RPC、WebSocket、GraphQL）。
- **可扩展与可维护**  
  - 采用现代 Rust 生态（`tokio`、`serde`、`tonic` 等），便于维护。  
  - 提供丰富的 CLI 工具，可在单机或多节点集群部署。
- **状态同步与共识优化**  
  - 支持快速同步（Fast Sync）与完整同步（Full Sync）。  
  - 与 Beacon、Clique 等共识算法集成，用于 PoS / PoW 网络。
- **工具链支持**  
  - 内置 `reth-node`、`reth-cli`、`reth-client` 等可直接启动网络节点。  
  - `reth-analyzer` 用于链状态、交易统计与性能分析。

## 主要功能

| 功能 | 描述 |
|------|------|
| 逻辑节点（`reth-node`） | 启动完整以太坊节点，支持 JSON‑RPC、WebSocket、EVM 调试接口。 |
| 区块同步 | 包含 **Fast Sync**、**Full Sync** 两种模式，支持离线预同步。 |
| 数据库 & 存储 | 使用 RocksDB 或 Postgres，提供状态、事务、日志的持久化。 |
| EVM 解释器 | 兼容以太坊虚拟机，支持 Solidity、Vyper 合约部署与执行。 |
| RPC / GraphQL 接口 | 快速访问链状态、账户余额、交易详情等。 |
| CLI 工具 | `reth-cli` 提供节点管理、配置、日志、诊断、统计。 |
| 测试与模拟 | 通过 `reth-test-utils` 能够在节点环境中模拟多种链条状态。 |

## 快速入门

```bash
# 克隆仓库
git clone https://github.com/paradigmxyz/reth.git
cd reth

# 编译
cargo build --release

# 启动测试网络（以本地区块链模式）
./target/releaseth-node --dev

# 访问 RPC 接口
# 默认端口：8545
curl -X POST http://localhost:8545 -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

### 通过 Docker 启动

```bash
docker pull paradigmxyz/reth:latest
docker run --rm -p 8545:8545 paradigmxyz/reth:latest --dev
```

### 配置文件

Reth 使用 `reth.toml` 进行配置，默认生成在 `$HOME/.config/reth/`。可自行修改节点选项、网络参数、日志级别等。

---

> **提示**：详细使用与开发文档请参阅官方文档及代码注释。常用命令和参数列表可通过 `reth-cli --help` 获得。