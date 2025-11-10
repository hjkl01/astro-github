---
title: Stacks Core
---

# Stacks Core

## 项目简介

Stacks Core 是 Stacks 区块链的参考实现，使用 Rust 语言编写。Stacks 是一个 layer-2 区块链，它利用比特币作为基础层的安全性，并通过 Clarity 编程语言启用去中心化应用（dApps）和可预测的智能合约。Stacks 通过 Proof of Transfer (PoX) 挖矿机制与比特币区块链锚定，无需修改比特币即可实现智能合约和 dApps。

## 主要功能

- **Layer-2 区块链**：在比特币之上构建，提供智能合约和 dApps 支持。
- **Clarity 语言**：一种可预测的智能合约语言，避免了传统智能合约的漏洞。
- **Proof of Transfer (PoX)**：挖矿机制，直接与比特币的安全性绑定。
- **去中心化应用支持**：允许开发者构建和部署 dApps。
- **比特币集成**：利用比特币的去中心化和安全性。

## 用法

### 构建项目

1. **安装 Rust**：

   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   source $HOME/.cargo/env
   rustup component add rustfmt
   rustup update
   ```

2. **克隆仓库**：

   ```bash
   git clone --depth=1 https://github.com/stacks-network/stacks-core.git
   cd stacks-core
   ```

3. **构建项目**：
   ```bash
   # 完全优化的发布构建
   cargo build --release
   # 更快但优化较少的构建（如果 RAM < 16 GB）
   cargo build --profile release-lite
   ```

### 测试

- 运行测试：

  ```bash
  cargo test testnet -- --test-threads=1
  ```

- 使用 nextest 运行所有单元测试：
  ```bash
  cargo nextest run
  ```

### 运行测试网

```bash
cargo run --bin stacks-node -- start --config ./sample/conf/testnet-follower-conf.toml
```

更多测试网文档请参考 [docs/testnet.md](https://github.com/stacks-network/stacks-core/blob/master/docs/testnet.md) 和 [Stacks 文档](https://docs.stacks.co/docs/nodes-and-miners/miner-testnet)。

## 进一步阅读

- [Stacks 官网](https://stacks.co)
- [Stacks 文档](https://docs.stacks.co/)
- [Stacks Improvement Proposals (SIPs)](https://github.com/stacks-network/stacks-core/blob/master/docs/SIPS.md)
- [挖矿文档](https://github.com/stacks-network/stacks-core/blob/master/docs/mining.md)
- [性能分析](https://github.com/stacks-network/stacks-core/blob/master/docs/profiling.md)
- [RPC 端点](https://github.com/stacks-network/stacks-core/blob/master/docs/rpc-endpoints.md)
- [事件分发器](https://github.com/stacks-network/stacks-core/blob/master/docs/event-dispatcher.md)

## 许可证

该项目采用 GPL-3.0 许可证。
