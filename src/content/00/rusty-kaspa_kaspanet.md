---
title: rusty-kaspa
---

# rusty-kaspa

## 项目简介

`rusty-kaspa` 是 Kaspa 区块链的全节点参考实现及其相关库，使用 Rust 编程语言开发。该项目作为 Golang 节点的替代品，是 Kaspa 网络推荐的节点软件，旨在提供高性能、可扩展性和安全性，同时保持去中心化。

项目包括多个组件：

- **kaspad**: 全节点实现
- **WASM SDK**: 用于 Web 和 Node.js 的 WebAssembly 构建
- **CLI 和钱包**: 命令行接口和终端钱包
- **模拟框架 (Simpa)**: 用于网络模拟和基准测试
- **其他库**: 共识、加密、数据库等

## 主要功能

- **高性能共识**: 实现 Kaspa 的 GHOSTDAG 协议，支持高块率（10 BPS）。
- **RPC 支持**: 提供 wRPC 子系统，支持 JSON 和 Borsh 协议。
- **WASM 兼容**: 允许在浏览器和 Node.js 中运行。
- **钱包集成**: 支持 UTXO 索引和钱包功能。
- **多平台构建**: 支持 Linux、Windows、Mac OS 和 Docker。
- **测试和基准**: 包括单元测试、集成测试和性能基准。

## 安装和构建

### 系统要求

- Rust 工具链（通过 rustup 安装）
- Protobuf 编译器
- Clang 工具链（用于 RocksDB 和 WASM）
- wasm-pack（用于 WASM 构建）

### 构建步骤

1. 克隆仓库：

   ```bash
   git clone https://github.com/kaspanet/rusty-kaspa
   cd rusty-kaspa
   ```

2. 安装依赖（以 Linux 为例）：

   ```bash
   sudo apt install curl git build-essential libssl-dev pkg-config protobuf-compiler libprotobuf-dev clang-format clang-tidy clang-tools clang clangd libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-dev libllvm-ocaml-dev libomp-dev libomp5 lld lldb llvm-dev llvm-runtime llvm python3-clang
   ```

3. 安装 Rust 和 WASM 工具：

   ```bash
   rustup update
   cargo install wasm-pack
   rustup target add wasm32-unknown-unknown
   ```

4. 构建项目：
   ```bash
   cargo build --release
   ```

### Docker 构建

使用提供的 Dockerfile 或多架构构建脚本：

```bash
docker build -f docker/Dockerfile.kaspad -t kaspad:latest .
# 或多架构构建
./build-docker-multi-arch.sh --tag kaspad:latest --artifact kaspad
```

## 使用方法

### 运行节点

- **主网节点**：

  ```bash
  cargo run --release --bin kaspad
  # 启用 UTXO 索引（用于钱包）
  cargo run --release --bin kaspad -- --utxoindex
  ```

- **测试网节点**：

  ```bash
  cargo run --release --bin kaspad -- --testnet
  ```

- **开发网节点**：
  ```bash
  cargo run --bin kaspad -- --devnet --enable-unsynced-mining --rpclisten=127.0.0.1 --rpclisten-borsh=127.0.0.1 --utxoindex
  ```

### 启用 RPC

- JSON 协议：

  ```bash
  cargo run --release --bin kaspad -- --rpclisten-json=default
  ```

- Borsh 协议：
  ```bash
  cargo run --release --bin kaspad -- --rpclisten-borsh=default
  ```

### CLI 和钱包

运行 CLI：

```bash
cd cli
cargo run --release
```

运行本地 Web 钱包：

```bash
cd wallet/wasm/web
basic-http-server
# 访问 http://localhost:4000
```

### 构建 WASM SDK

```bash
./build-release  # 完整发布包
./build-web      # Web 发布构建
./build-nodejs   # Node.js 发布构建
```

### 测试和基准

- 运行测试：

  ```bash
  cargo test --release
  ```

- 运行基准：

  ```bash
  cargo bench
  ```

- 运行模拟：
  ```bash
  cargo run --release --bin simpa -- -t=200 -d=2 -b=8 -n=1000
  ```

## 更多信息

- [GitHub 仓库](https://github.com/kaspanet/rusty-kaspa)
- [文档](https://kaspa.aspectron.org/docs/)
- [发布版本](https://github.com/kaspanet/rusty-kaspa/releases)
