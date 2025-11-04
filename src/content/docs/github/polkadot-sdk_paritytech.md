
---
title: polkadot-sdk
---


# ParityTech Polkadot SDK

**项目地址**：<https://github.com/paritytech/polkadot-sdk>

## 主要特性

| 类别 | 特点 |
|------|------|
| **模块化** | 采用 Substrate 框架，治理、资产、权益、共识等组件可自由组合 |
| **Wasm Runtime** | 所有链运行在 WebAssembly 上，支持快速迭代与安全性 |
| **跨链互操作** | 原生支持 Parachain、XPUB、XRPL 等跨链协议 |
| **智能合约** | 兼容 Ink! & EVM，支持 Rust & Solidity 开发 |
| **治理机制** | 内置提案、投票、延期、质押等民主决策流程 |
| **本地开发工具** | `substrate` CLI、`polkadot-js`、`cargo`、`docker`、`docker-compose` 等 |

## 主要功能

1. **区块链节点**  
   - 运行完整节点 (`polkadot`, `node-template`)
   - 轻量客户端 (`light-client`)

2. **链开发**  
   - 通过 `node-template` 快速打通链代码（Runtime, Genesis Config, ParaBridge, etc.）
   - 插件化治理、资产、staking（Rust)
   - 通过 Ink! 书写智能合约，编译为 Wasm

3. **工具链**  
   - `cargo-substrate`：编译、测试、部署
   - `pallets`：预制模块
   - `polkadot-js-api`/`polkadot-api`：JS/TS 前端 SDK
   - `mocha` + `chai`：链端测试
   - `docker` + `docker-compose`：快速部署测试网

4. **多链生态**  
   - `relay-chain` + `parachain` 组合（XCM, XCMP）
   - 通过 `bridge` 连接以太坊、Cosmos 等链

## 用法示例

### 开发与构建

```bash
# 克隆仓库
git clone https://github.com/paritytech/polkadot-sdk.git
cd polkadot-sdk

# 安装 Rust+Substrate
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update

# 编译 node-template (示例链)
cargo build --release -p node-template
```

### 运行本地节点

```bash
./target/release/node-template --dev  # 开发模式
```

### 使用 `polkadot-js` API

```js
import { ApiPromise, WsProvider } from '@polkadot/api';

async function main() {
  const provider = new WsProvider('ws://127.0.0.1:9944');
  const api = await ApiPromise.create({ provider });

  // 查询链信息
  const bestHash = await api.rpc.chain.getBlockHash();
  console.log('Best block hash:', bestHash.toHex());
}

main();
```

### 部署 Ink! 合约

```bash
# 编译合约
cd contracts/contract1
cargo contract build

# 部署签名钱包
./scripts/deploy.sh contract1.wasm 0.1
```

### 启动 Parachain

```bash
# 运行 Parachain VM
docker pull paritytech/polkadot-parachain
docker run --rm -it paritytech/polkadot-parachain --chain dev
```

### 测试与 CI

```bash
# 单元测试
cargo test

# 集成测试
cargo test --lib -- --nocapture
```

---

> **提示**：详细使用可查看 `README.md`、`examples/` 目录和官方文档  
> *Polkadot SDK* 兼容最新的 Substrate 1.x，兼具可扩展性与安全性，适用于 PDN、资产发行、去中心化治理等多种场景。