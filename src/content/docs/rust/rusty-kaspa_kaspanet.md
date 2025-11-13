---
title: rusty-kaspa
---

# rusty-kaspa

## 项目简介

Rusty Kaspa 是 Kaspa 区块链的 Rust 实现版本，是 Kaspa 全节点的 Rust 替代方案。它作为 Golang 节点的直接替代品，是 Kaspa 网络推荐的软件。

## 主要功能

- **全节点实现**：提供完整的 Kaspa 区块链节点功能
- **UTXO 索引**：支持 UTXO 索引，用于钱包功能
- **多网络支持**：支持主网和测试网
- **RPC 接口**：提供 wRPC JSON 和 Borsh 协议接口
- **WASM SDK**：支持 WebAssembly，用于浏览器和 Node.js 环境
- **钱包功能**：包含命令行钱包和 Web 钱包
- **挖矿支持**：支持 CPU 挖矿
- **网络模拟**：包含 Simpa 网络模拟框架

## 安装和构建

### 系统要求

- Rust 工具链
- Protobuf 编译器
- LLVM/Clang 工具链
- wasm-pack（用于 WASM 构建）

### Linux 安装

```bash
sudo apt install curl git build-essential libssl-dev pkg-config
sudo apt install protobuf-compiler libprotobuf-dev
sudo apt-get install clang-format clang-tidy clang-tools clang clangd libc++-dev libc++1 libc++abi-dev libc++abi1 libclang-dev libclang1 liblldb-dev libllvm-ocaml-dev libomp-dev libomp5 lld lldb llvm-dev llvm-runtime llvm python3-clang
cargo install wasm-pack
rustup target add wasm32-unknown-unknown
git clone https://github.com/kaspanet/rusty-kaspa
cd rusty-kaspa
```

### macOS 安装

```bash
brew install protobuf
brew install llvm
export PATH="/opt/homebrew/opt/llvm/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"
export AR=/opt/homebrew/opt/llvm/bin/llvm-ar
cargo install wasm-pack
rustup target add wasm32-unknown-unknown
git clone https://github.com/kaspanet/rusty-kaspa
cd rusty-kaspa
```

### Windows 安装

```bash
cargo install wasm-pack
rustup target add wasm32-unknown-unknown
git clone https://github.com/kaspanet/rusty-kaspa
cd rusty-kaspa
```

## 使用方法

### 运行主网节点

```bash
cargo run --release --bin kaspad
```

启用 UTXO 索引（钱包功能需要）：

```bash
cargo run --release --bin kaspad -- --utxoindex
```

### 运行测试网节点

```bash
cargo run --release --bin kaspad -- --testnet
```

### 使用配置文件

创建 `config.toml` 文件：

```toml
testnet = true
utxoindex = false
disable-upnp = true
perf-metrics = true
appdir = "some-dir"
netsuffix = 11
addpeer = ["10.0.0.1", "1.2.3.4"]
```

运行节点：

```bash
cargo run --release --bin kaspad -- --configfile /path/to/configfile.toml
```

### 运行命令行钱包

```bash
cd cli
cargo run --release
```

### 运行 Web 钱包

```bash
cd wallet/wasm/web
cargo install basic-http-server
basic-http-server
```

然后在浏览器中访问 `http://localhost:4000`

### WASM SDK 使用

构建 WASM 组件：

```bash
./build-release
./build-web
./build-nodejs
```

Node.js 示例：

```bash
cd wasm
./build-release
cd examples
npm install
node init
node nodejs/javascript/general/rpc.js
```

### 运行测试

```bash
cargo test --release
```

### 性能基准测试

```bash
cargo bench
```

### 网络模拟

```bash
cargo run --release --bin simpa -- -t=200 -d=2 -b=8 -n=1000
```

## 高级配置

### RPC 接口配置

启用 JSON RPC：

```bash
--rpclisten-json = <interface:port>
```

启用 Borsh RPC：

```bash
--rpclisten-borsh = <interface:port>
```

### 性能和日志配置

启用性能指标：

```bash
--perf-metrics --loglevel=info,kaspad_lib::daemon=debug,kaspa_mining::monitor=debug
```

调整缓存大小：

```bash
--ram-scale=3.0
```

### 挖矿

测试网 CPU 挖矿：

```bash
kaspa-miner --testnet --mining-address <your-address> -p 16210 -t 1
```

## 开发和贡献

项目使用 Rust 编写，支持多种平台。贡献者可以参与代码审查、测试和功能开发。

更多详细信息请参考 [GitHub 仓库](https://github.com/kaspanet/rusty-kaspa)。
