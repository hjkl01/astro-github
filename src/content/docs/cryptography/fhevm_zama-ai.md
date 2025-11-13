---
title: fhevm
---

# FHEVM 项目概述

**GitHub 地址**  
[https://github.com/zama-ai/fhevm](https://github.com/zama-ai/fhevm)

## 项目简介

FHEVM 是 Zama Confidential Blockchain Protocol 的核心框架。它通过集成全同态加密 (FHE) 与区块链应用程序，实现 EVM 兼容的保密智能合约。FHEVM 确保端到端加密事务和状态，同时保持可组合性和链上数据可用性。

## 主要特性

- **隐私设计**：在以太坊上构建具有完全隐私和机密性的去中心化应用，使用 FHE。
- **Solidity 集成**：像任何标准 Solidity 合约一样编写 FHEVM 合约。兼容现有工具链——如 Hardhat 和 Foundry（即将推出）。
- **可编程隐私**：精确定义哪些数据被加密，并直接在智能合约中编写访问控制逻辑。
- **高精度加密整数**：整数高达 256 位精度。
- **全运算符范围**：所有典型运算符都可用：`+`、`-`、`*`、`/`、`<`、`>`、`==`、三元-if、布尔运算……连续 FHE 操作不受限制。
- **安全性**：底层 FHE 加密方案是量子抗性的。解密由密钥管理系统管理，使用多方计算 (MPC)，即使某些方被妥协或行为不端也能确保安全性。
- **FHE 计算的象征执行**：所有 FHE 操作在主机链上象征执行，大大减少执行时间。实际加密数据计算异步卸载到我们的协处理器，允许更快、更高效和可扩展的处理。

## 核心功能

- **保密转移**：保持余额和金额私有，而不使用混币器。
- **代币化**：在链上交换代币和 RWA，而不让其他人看到金额。
- **盲拍卖**：竞标物品而不透露金额或获胜者。
- **链上游戏**：保持移动、选择、卡牌或物品隐藏，直到准备揭示。
- **保密投票**：防止贿赂和敲诈，通过保持投票私有。
- **加密 DID**：在链上存储身份并生成证明，而不泄露 ZK。

## 快速上手

1. 安装依赖：`npm install -g fhevm-cli fhevm-compiler`
2. 编译 Solidity 合约：`fhevm-compiler --input HelloWorld.sol --output HelloWorld.fvm`
3. 生成密钥对：`fhevm-cli keygen --output keypair.json`
4. 合约部署：`fhevm-cli deploy HelloWorld.fvm --keypair keypair.json --rpc https://fhevm.example.com`
5. 调用合约：`fhevm-cli call <contract_address> hello --args "world" --keypair keypair.json`

## 五、文档与社区

- 官方文档: [https://fhevm.zama.ai/docs](https://fhevm.zama.ai/docs)
- 开发者指南: `docs/` 目录
- 社区讨论: Discord / GitHub Discussions

---

> 通过 FHEVM，开发者可以在不泄露数据的前提下，构建可扩展且安全的智能合约生态。

```
> 以上内容请保存为 `src/content/docs/00/fhevm_zama-ai.md`。
```
