
---
title: linera-protocol
---


# Linera Protocol

项目地址: https://github.com/linera-io/linera-protocol

## 主要特性

| 特性 | 说明 |
|------|------|
| **高吞吐量 & 可扩展性** | 采用分片（sharding）与并行事务执行，单节点吞吐可达数万 TPS，支持水平扩容。 |
| **低延迟** | 线程化执行模型将确认时间压缩至毫秒级，满足即时交互需求。 |
| **跨链互操作** | 内置跨链消息通道（Cross‑Chain Messaging Protocol，CCMP），支持不同链资产与协议之间的安全交互。 |
| **安全性** | 所有状态变更都通过可验证的状态快照保证，采用 Rust、安全编译、加密哈希与零知识证明等技术。 |
| **准确定义的账户与资产** | 支持可编程资产类型（Native Assets, Fungible Tokens, Non‑Fungible Tokens）与细粒度权限控制。 |
| **内置治理** | 通过链上投票与决策，支持协议升级、参数调整等治理操作。 |
| **易于开发** | 提供完整的 Rust SDK，示例合约与工具链，支持快速原型与生产部署。 |

## 主要功能

1. **核心网络**  
   - 节点互联、共识算法（如 Tendermint 或 Raft）实现一致性。  
   - 生成与验证区块，维护全局账本。

2. **交易 & 合约执行**  
   - 跨合约调用、状态更新、事件日志。  
   - 支持多合约组合（Contract Composition）与升级。

3. **资产与账户管理**  
   - 原生资产系统与 ERC‑20/EIP‑721 风格的代币。  
   - 多重签名、时间锁、额度限制等高级权限。

4. **跨链消息**  
   - 通过消息编解码实现链间数据共享。  
   - 支持跨链资产桥接、去中心化交易所等应用。

5. **工具与 SDK**  
   - `linera-cli`：节点与合约部署、交互工具。  
   - `linera-sdk`：Rust SDK，包含合约开发框架与测试工具。  
   - `linera-macro`：提供合约属性宏，简化代码结构。

## 快速使用方法

1. **环境准备**  
   ```bash
   # 安装 Rust（推荐使用 rustup）
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   rustup toolchain install nightly
   ```

2. **克隆仓库**  
   ```bash
   git clone https://github.com/linera-io/linera-protocol.git
   cd linera-protocol
   ```

3. **编译项目**  
   ```bash
   cargo build --release
   # 生成可执行文件位于 target/release/
   ```

4. **运行单节点网络（示例）**  
   ```bash
   # 启动一个本地链（默认配置）
   ./target/release/linera-runner
   ```

5. **部署示例合约**  
   ```bash
   # 编译示例合约
   cargo build --manifest-path examples/token/Cargo.toml

   # 部署
   ./target/release/linera-detach client upload examples/token/target/wasm32-unknown-unknown/release/token.wasm
   ```

6. **与合约交互**  
   ```bash
   # 调用合约方法
   ./target/release/linera-detach client call <contract-id> "mint" '{"address":"player1","amount":100}'
   ```

7. **运行单元测试**  
   ```bash
   cargo test
   ```

8. **文档与示例**  
   - `doc/` 目录下包含协议规范与设计文档。  
   - `examples/` 提供多种合约示例（Token、Marketplace、Voting 等）。  

## 进一步学习

- 阅读 `doc/protocol.md` 了解协议细节。  
- 查看 `examples/` 下的代码，快速上手合约开发。  
- 参与社区讨论：[Linera Discord](https://discord.com/invite/linera) 或 [GitHub Discussions](https://github.com/linera-io/linera-protocol/discussions)。

> 以上步骤基于官方 README 与开发者指南，实际使用时请结合最新代码版本与官方文档进行调整。