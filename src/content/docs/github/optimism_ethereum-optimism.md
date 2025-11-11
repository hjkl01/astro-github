---
title: optimism
---

# Optimism

## 功能介绍

Optimism 是 Ethereum 的 Layer 2 扩展解决方案，旨在通过 OP Stack 实现 Ethereum 的可扩展性。OP Stack 是一个去中心化的软件栈，由 Optimism Collective 维护，用于构建可扩展的区块链，如 OP Mainnet 和 Base。它遵循 "impact=profit" 原则，鼓励积极贡献者获得相应回报。

主要功能包括：

- **Layer 2 Rollup**：通过 Optimistic Rollup 技术降低交易费用，提高吞吐量。
- **去中心化治理**：支持社区驱动的治理和经济模型。
- **开源组件**：提供完整的 OP Stack 组件，如 op-node、op-batcher、op-proposer 等，用于构建自定义区块链。
- **跨链互操作性**：支持链间消息传递和数据可用性。
- **故障证明**：使用 Cannon（MIPS 指令模拟器）进行链上故障证明。

## 用法

### 构建在 OP Mainnet 上

- 参考 [Optimism 文档](https://docs.optimism.io) 进行开发。
- 使用 OP Stack 合约和工具与 OP Mainnet 交互。

### 构建自己的 OP Stack 区块链

1. 克隆仓库：`git clone https://github.com/ethereum-optimism/optimism.git`
2. 安装依赖：根据 [CONTRIBUTING.md](https://github.com/ethereum-optimism/optimism/blob/develop/CONTRIBUTING.md) 设置开发环境。
3. 使用 op-deployer 部署合约：运行 `op-deployer` 工具部署和升级 OP Stack 智能合约。
4. 配置节点：使用 op-node 运行共识层客户端，op-batcher 提交批次到 L1。
5. 测试：使用 op-e2e 或 op-devstack 进行端到端测试。

### 开发和贡献

- 查看 [OP Stack Guide](https://docs.optimism.io/stack/getting-started) 了解详细规范。
- 参与社区讨论：[Discord](https://discord.gg/optimism) 或 [Governance Forum](https://gov.optimism.io/)。
- 贡献代码：提交 PR 到 develop 分支，遵循 [CONTRIBUTING.md](https://github.com/ethereum-optimism/optimism/blob/develop/CONTRIBUTING.md)。

更多信息请访问 [optimism.io](https://optimism.io)。
