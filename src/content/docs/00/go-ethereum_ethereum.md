
---
title: go-ethereum
---

以下是对 GitHub 项目 **go-ethereum**（简称 Geth）的中文描述，已按要求以 Markdown 格式整理。  
> **文件路径**：`src/content/docs/00/go-ethereum_ethereum.md`

```markdown
# go-ethereum (Geth)

**GitHub 地址**：<https://github.com/ethereum/go-ethereum>

## 主要特性
- 官方以太坊客户端，使用 Go 语言实现，兼容多平台（Windows、Linux、macOS）。
- 完整的以太坊节点实现：同步链、共识机制（PoW/PoS）、网络层、存储层、执行层。
- 提供强大的 **JSON‑RPC** 与 **WebSocket** 接口，支持远程调用与实时事件订阅。
- 内置 **Geth Console**（REPL）和 **Command‑Line Interface (CLI)**，方便交互式开发与运维。
- 支持 **账户管理**（Keystore、HD 钱包）、**私钥加密**、**交易签名** 与 **广播**。
- 集成 **EIP‑1559**、**EIP‑155** 等以太坊改进提案，兼容主网与测试网。
- 支持 **智能合约** 的部署、调用与调试，结合 `evm` 虚拟机实现。
- 提供 **轻节点**（Light Client）与 **完整节点**（Full Node）两种模式。
- 支持 **跨链桥接** 与 **侧链**（如 Optimism、Arbitrum）的兼容层。

## 功能概览
| 功能 | 说明 |
|------|------|
| **节点同步** | 与以太坊主网/测试网同步区块链，支持快照与全量同步。 |
| **交易池** | 管理未确认交易，支持 fee、nonce、gas 计算。 |
| **RPC API** | `eth`, `net`, `web3`, `personal`, `debug`, `admin` 等接口。 |
| **CLI 工具** | `geth init`, `geth --datadir`, `geth console`, `geth account new` 等。 |
| **智能合约** | `evm`, `solc`, `truffle` 等集成，支持 Solidity 合约部署与调用。 |
| **身份验证** | 使用 Keystore、Mnemonic、Hardware Wallet（Ledger, Trezor）等。 |
| **网络层** | P2P（libp2p）支持多路复用、加密、路由。 |
| **监控** | 通过 `metrics` 导出 Prometheus 指标，支持 Grafana 可视化。 |

## 使用方法

1. **获取源码**  
   ```bash
   git clone https://github.com/ethereum/go-ethereum.git
   cd go-ethereum
   ```

2. **安装依赖**  
   ```bash
   go mod download
   ```

3. **编译**  
   ```bash
   make geth
   # 或者直接使用 go build
   go build -o geth ./cmd/geth
   ```

4. **初始化节点**  
   ```bash
   ./geth init <genesis.json>
   ```

5. **启动完整节点**  
   ```bash
   ./geth --datadir ./data --http --http.api "eth,net,web3,personal,admin,debug"
   ```

6. **使用 Geth Console**  
   ```bash
   ./geth console
   ```

7. **部署与调用智能合约**  
   - 编译合约：`solc --bin --abi MyContract.sol -o build/`
   - 部署：`eth.sendTransaction({to: "", data: "0x...", value: 0})`
   - 调用：`eth.call({to: contractAddress, data: "0x..."})`

8. **RPC 调试示例**  
   ```bash
   curl -X POST --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' http://localhost:8545
   ```

9. **轻节点模式**（仅同步状态）  
   ```bash
   ./geth --syncmode "light"
   ```

10. **监控与日志**  
    - 通过 `--metrics` 启用 Prometheus 指标。  
    - 日志等级可通过 `--verbosity` 调整（0-6）。

> **提示**：为避免与已有节点冲突，建议使用不同的 `--datadir` 或 `--port`。

---  

> 以上内容为对 **go-ethereum** 项目的核心特性、功能以及常用使用方法的简明概述。  
> 如需更深入的使用细节，请参考官方文档和源码注释。