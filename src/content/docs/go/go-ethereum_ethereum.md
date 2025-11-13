---
title: go-ethereum
---

# go-ethereum

## 项目简介

go-ethereum 是 Ethereum 协议的 Go 语言实现，也称为 Geth。它是 Ethereum 区块链的官方客户端之一，提供完整的节点功能，支持主网、测试网和私有网络。

## 主要功能

- **全节点支持**：运行完整的 Ethereum 节点，包括主网、测试网（如 Holesky）和私有网络。
- **挖矿**：支持 PoW 挖矿（在 Ethereum 2.0 合并后主要用于测试）。
- **智能合约**：部署和执行智能合约。
- **钱包管理**：创建和管理 Ethereum 账户。
- **RPC 接口**：提供 HTTP、WebSocket 和 IPC 接口，用于与节点交互。
- **开发工具**：包括 EVM 调试器、ABI 生成器等。

## 主要可执行文件

- **geth**：主 Ethereum CLI 客户端，用于运行节点和交互。
- **clef**：独立的签名工具，可作为 geth 的后端签名器。
- **devp2p**：网络层工具，用于与节点交互。
- **abigen**：从 Ethereum 合约 ABI 生成 Go 代码。
- **evm**：EVM 调试工具。
- **rlpdump**：RLP 数据解码工具。

## 安装和构建

### 环境要求

- Go 1.23 或更高版本
- C 编译器

### 构建步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/ethereum/go-ethereum.git
   cd go-ethereum
   ```

2. 构建 geth：

   ```bash
   make geth
   ```

3. 或构建所有工具：
   ```bash
   make all
   ```

## 使用方法

### 运行主网全节点

```bash
geth console
```

这将启动 snap sync 模式，并打开 JavaScript 控制台。

### 运行测试网节点（Holesky）

```bash
geth --holesky console
```

### 配置选项

- `--syncmode`：同步模式（full, snap, light）
- `--http`：启用 HTTP-RPC
- `--http.addr`：HTTP 监听地址（默认 localhost）
- `--http.port`：HTTP 端口（默认 8545）
- `--ws`：启用 WebSocket-RPC
- `--ipcdisable`：禁用 IPC

### Docker 快速启动

```bash
docker run -d --name ethereum-node -v /path/to/data:/root \
           -p 8545:8545 -p 30303:30303 \
           ethereum/client-go
```

### 私有网络

设置私有网络需要配置 genesis 文件和网络参数。推荐使用 Dev Mode 或 Kurtosis 进行测试。

## API 接口

geth 支持 JSON-RPC API，包括标准 Ethereum API 和 geth 特定 API。可通过 HTTP、WebSocket 或 IPC 访问。

## 贡献

欢迎贡献代码。请遵循 Go 格式化指南，确保代码有文档，并针对 master 分支提交 PR。

## 许可证

- 库代码：LGPL-3.0
- 二进制文件：GPL-3.0

## 更多信息

- 官方网站：[geth.ethereum.org](https://geth.ethereum.org)
- 文档：[geth.ethereum.org/docs](https://geth.ethereum.org/docs)
- Discord：[discord.gg/nthXNEv](https://discord.gg/nthXNEv)
