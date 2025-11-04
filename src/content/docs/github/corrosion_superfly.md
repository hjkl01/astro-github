
---
title: corrosion
---


# Corrosion (superfly/corrosion)

**项目地址**: <https://github.com/superfly/corrosion>

## 主要特性

- **纯 Rust 实现**：利用 Rust 的内存安全和高性能优势实现 Ethereum 协议栈。
- **完整节点功能**：支持全节点、轻节点，具备区块同步、交易验证、状态存储等。
- **高性能网络**：基于 libp2p 的 P2P 网络通信，支持多路复用与加密。
- **JSON‑RPC / WebSocket 接口**：内置 HTTP/WS 服务器，兼容官方 API。
- **模块化设计**：核心模块（网络、共识、存储、交易）可单独使用或集成到其他项目。
- **可扩展插件系统**：通过 Cargo feature 轻松启用或禁用功能，例如 `rpc`, `cli`, `bench` 等。
- **完整测试与文档**：提供单元/集成测试，文档生成与示例代码。

## 主要功能

| 功能 | 描述 |
|------|------|
| 区块同步 | 通过 P2P 拉取区块，支持 GHOST、Clique 等共识算法。 |
| 交易执行 | 以太坊虚拟机（EVM）实现，支持 ERC‑20、ERC‑721 等合约。 |
| 状态存储 | 使用 RocksDB/LMDB 存储账户余额、合约代码等。 |
| JSON‑RPC | 提供 `eth_blockNumber`, `eth_getBalance`, `eth_sendTransaction` 等接口。 |
| CLI 工具 | `corrosion-cli` 用于快速启动节点、查询状态、加载合约。 |
| 性能测试 | `bench` 功能提供基准测试，测评吞吐量与延迟。 |

## 快速上手

### 安装

```bash
cargo install --git https://github.com/superfly/corrosion
```

### 运行全节点

```bash
corrosion --config config/fullnode.toml
```

### 运行轻节点

```bash
corrosion --config config/lightnode.toml
```

### 使用 JSON‑RPC

```bash
curl -X POST -H "Content-Type: application/json" \
     --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
     http://127.0.0.1:8545
```

### 在项目中使用

```rust
use corrosion::{Client, Config};

#[tokio::main]
async fn main() {
    let config = Config::from_file("config/fullnode.toml").unwrap();
    let client = Client::new(config).await.unwrap();
    let block_number = client.eth_block_number().await.unwrap();
    println!("Latest block: {}", block_number);
}
```

## 贡献

- Fork → Create feature branch → Push → Pull Request
- 详细文档请查看 `README.md` 与 `docs/` 目录。

## 许可

MIT License – 参见 `LICENSE` 文件。
