
---
title: solana
---


# Solana (Solana Labs)

- **仓库地址**: [https://github.com/solana-labs/solana](https://github.com/solana-labs/solana)

## 项目概述
Solana 是一个高性能的区块链项目，旨在提供可扩展、去中心化且低延迟的基础设施。它通过引入“Proof of History (PoH)”作为时间辅助层，并与传统的权益证明（Proof of Stake, PoS）相结合，破解了传统区块链扩展性瓶颈。

## 主要特性
- **超高吞吐量**：≈ 65,000 TPS（每秒交易数），可通过分片与并行处理进一步提升。
- **低交易延迟**：约 400 毫秒最终确认时间。
- **可扩展性**：支持多核、异步执行，利用Rust生态提升并发计算。
- **安全性**：多层加密、PoS + PoH 设计抵御51%攻击。
- **跨链互操作**：支持跨链桥接与原子交换。

## 核心组件
| 组件 | 说明 |
|------|------|
| `solana-program-lib` | 用于写智能合约（程序）的 Rust 库，提供 BPF/Anchor 框架。 |
| `solana-cli` | 与本地区块链交互的命令行工具，支持账户管理、交易提交、查看状态等。 |
| `solana-validator` | 参与共识的验证节点，实现 PoS + PoH 计算。 |
| `solana-test-validator` | 本地测试链，可在 CI/CD 或本地开发环境快速部署。 |

## 常见用法

### 1. 安装 Solana CLI
```bash
sh -c "$(curl -sSfL https://release.solana.com/v1.18.19/install)"
```

### 2. 创建钱包
```bash
solana-keygen new -o ~/.config/solana/devnet.json
solana config set --keypair ~/.config/solana/devnet.json
```

### 3. 在 Devnet 领取测试 SOL
```bash
solana airdrop 2
solana balance
```

### 4. 编译 & 部署智能合约（Rust 版本）
```bash
cargo build-sbf --manifest-path path/to/Cargo.toml
solana program deploy target/deploy/your_program.so
```

### 5. 发送交易
```bash
solana transfer <recipient_pubkey> 1 --allow-unfunded-recipient
```

### 6. 通过 Anchor 框架
```bash
anchor init my_solana_app
anchor build
anchor deploy
```

## 文档与社区
- 官方文档: https://docs.solana.com/
- 开发者社区: Discord、Telegram、Twitter
- 贡献指南: https://github.com/solana-labs/solana/blob/master/CONTRIBUTING.md
