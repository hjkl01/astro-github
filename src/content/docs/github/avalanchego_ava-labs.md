---
title: avalanchego
---


# Avalanchego – Ava Labs 官方区块链节点实现

> 项目地址: [https://github.com/ava-labs/avalanchego](https://github.com/ava-labs/avalanchego)

## 项目概述
Avalanchego 是 Ava Labs 为 Avalanche 网络提供的官方 Go 语言实现，充当高性能、可扩展的全节点（full node）和轻节点（light node）客户端。它实现了 Avalanche 的共识协议、协议层（P-Chain、C-Chain、X-Chain）以及跨链功能。

## 主要特性
- **完整节点实现**：支持全节点验证、交易打包、状态同步及共识参与。
- **轻节点支持**：可通过 RPC 访问链状态，减少本地存储和资源占用。
- **协议层**：实现 P-Chain（治理与资产管理）、C-Chain（以太坊虚拟机）与 X-Chain（平台资产）三大链。
- **高级共识**：采用 Avalanche Consensus、Snowman 等高级 DAG 共识协议。
- **插件化架构**：可扩展的插件接口，可插入自定义交易、共识或网络功能。
- **多语言绑定**：Go 内核可通过 RPC 或 gRPC 与其他语言（JavaScript、Python、Rust 等）交互。
- **高性能**：针对 AVAX 交易量拆分、缓存、BFT 等做了多项性能优化。
- **安全性**：提供多种安全选项，包括 QC 存档、网络隔离、节点安全配置。

## 关键功能
| 功能 | 描述 |
|------|------|
| 节点同步 | 与网络中其他节点同步区块、事务、状态变更。 |
| 共识参与 | 通过雪崩共识（Snowball/Snowman）参与区块验证与挖矿。 |
| RPC 接口 | 以 JSON-RPC / gRPC 提供完整的链查询、交易发送、账户管理 API。 |
| 本持久化 | 通过 BadgerDB 或 LevelDB 存储区块、索引、存档。 |
| 跨链交易 | 支持 AVAX、ERC20 资产跨链（⛓）支付与流通。 |
| 节点管理 | 通过 CLI 或主题配置（`config.yaml`）管理节点参数。 |
| 监控与日志 | 集成 Prometheus、Telegraf、Elasticsearch 等监控工具。 |
| 插件机制 | 可自定义插件用于验证、共识、网络层。 |
| 升级系统 | 热更新、回滚、版本管理功能。## 快速上手

### 1. 克隆仓库
```bash
git clone https://github.com/ava-labs/avalanchego.git
cd avalanchego
```

### 2. 编译
```bash
make build
```

### 3. 配置
编辑 `config.yaml`（示例位于 `config/example_config.yaml`），配置 RPC 接口、网络监听、共识参数等。

### 4. 启动节点
```bash
./build/bin/avalanchego -configPath=./config.yaml
```

### 5. 与节点交互
- **CLI**  
  ```bash
  ./build/bin/avalanche-cli --configFile config.yaml
  ```
- **RPC**  
  访问 `http://localhost:9650/ext/bc/C/rpc` 或 `http://localhost:9650/ext/bc/X/rpc` 通过 JSON-RPC 调用。

### 6. 发送交易
```bash
# 账号：0x...
# 链 ID：X
./build/bin/avalanche-cli --rpcURL http://localhost:9650/ext/bc/X/rpc \
    --avalancheWallet <wallet-key> \
    --txType 12 \
    --to 0xRecipient <address> \
    --amount 10
```

> 参考官方 SDK 文档以获取更多语言绑定与高级功能。

## 部署与扩展

- **云部署**：使用 Docker Compose / Kubernetes 配置。
- **节点监控**：集成 Prometheus，通过 `prometheus.yaml` 监控指标。
- **扩容**：水平扩展轻节点，垂直扩展全节点可通过会话分区提升吞吐率。
- **安全**：使用 TLS 加密 RPC、网络分层、访问控制、防伪码等。

## 参考链接

- 官方文档: [https://docs.avax.network](https://docs.avax.network)
- 代码仓库: [https://github.com/ava-labs/avalanchego](https://github.com/ava-labs/avalanchego)
- 开发者社区: [Discord](https://discord.com/channels/1009076934912068378), [Forum](https://forum.avax.network)

--- 
*此 Markdown 文档已准备好，可直接保存为 `src/content/docs/00/avalanchego_ava-labs.md`。*
