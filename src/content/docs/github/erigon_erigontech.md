---
title: erigon
---


# Erigon（erigontech/erigon）

> 项目地址：🔗 [https://github.com/erigontech/erigon](https://github.com/erigontech/erigon)

## 主要特性

- **高性能、低资源**  
  - 使用 Go 语言实现，采用多核并行处理，显著降低 CPU 与内存占用。  
  - 通过批量写入磁盘和共享内存，I/O 成本大幅下降。

- **多同步模式**  
  - **FastSync**：快速同步最新区块，适用于需要快速获得网络状态的用户。  
  - **ArchiveSync**：完整存档所有历史状态，支持历史查询。  
  - **Light**：仅存储最近共识关键数据，适合轻节点部署。  
  - **Pruned**（可选）: 只保留必要的状态快照，极大减少磁盘占用。

- **兼容 Geth API**  
  - 兼容标准的 `eth_*`, `net_*`, `web3_*` RPC 接口，现有 dApp 与工具无需修改即可使用。

- **快速状态回滚与重放**  
  - 自动化的 `reboot` 与 `fast reorg` 支持链上分叉的快速处理。

- **强大的调试工具**  
  - `erigon-cli`、`debug.rpc`, `ethstats` 等工具，可对节点状态、网络、性能进行实时监控与排错。

- **高可扩展性**  
  - 支持多实例并行同步，适合大规模节点部署与托管服务。

- **安全与合规**  
  - 采用最新的安全审计版代码，保持与主网同步的安全性与合规性。

## 功能概览

| 模块 | 说明 |
|------|------|
| `datasource` | 分层数据存储（leveldb/badger） |
| `backend` | 区块与交易查询接口 |
| `sync` | 区块同步协议（Eth, BDVT） |
| `eth` | Geth 兼容 RPC 与 JSON‑RPC 服务器 |
| `debug` | 调试与监控接口 |
| `utils` | 日志、加密、并发工具 |

## 用法

### 1. 预编译二进制下载

```bash
# 直接从 GitHub Release 页面下载对应平台预编译包
# 例如 macOS 64 位
wget https://github.com/erigontech/erigon/releases/download/v{{version}}/erigon_macos_amd64.tar.gz
tar -xzf erigon_macos_amd64.tar.gz
cd erigon
```

### 2. 源码编译（Go 1.22+）

```bash
git clone https://github.com/erigontech/erigon.git
cd erigon
git checkout v{{version}}
make
# 可直接执行 erigon
./build/erigon
```

#### 编译基本命令

- 编译完整二进制：`make erigon`  
- 只编译 RPC 服务器：`make rpc`  
- 编译并行构建：`make -j`  

### 3. 启动节点

```bash
./build/erigon --http --http.addr 0.0.0.0 --http.port 8545 --http.api eth,net,web3,debug
```

#### 快速 Sync

```bash
./build/erigon --sync-mode fast
```

#### Archive Sync

```bash
./build/erigon --sync-mode full
```

#### 仅做轻节点

```bash
./build/erigon --light
```

### 4. RPC 调用示例

```bash
curl -X POST http://127.0.0.1:8545 -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
```

### 5. 监控与调试

- **Ethstats**: `./build/erigon --ethstats privateKey@npmAddress`  
- **debug.geth**: `./build/erigon --debug.rpc`  
- 查看节点状态: `./build/erigon --metrics`

### 6. 部署与运维

- 创建 system‑d 服务文件：  
  ```ini
  [Unit]
  Description=Erigon Ethereum node
  After=network.target

  [Service]
  ExecStart=/path/to/aws/erigon --http
  Restart=on-failure
  User=erigon

  [Install]
  WantedBy=multi-user.target
  ```
- 使用 `docker`：  
  ```docker
  docker run -d -p 8545:8545 -p 30303:30303 \
    erigontech/erigon:v{{version}} \
    --http --http.addr 0.0.0.0 --http.port 8545
  ```

## 参考文档

- 官方文档: <https://docs.erigon.tech/>  
- 快速上手指南: <https://github.com/erigontech/erigon#quick-start>  
- 代码结构: <https://github.com/erigontech/erigon/blob/master/README.md>

---
> 项目地址: [https://github.com/erigontech/erigon](https://github.com/erigontech/erigon)
