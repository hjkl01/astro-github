
---
title: cosmos-sdk
---

以下是你可以直接复制到 **src/content/docs/00/cosmos-sdk_cosmos.md** 的 Markdown 文档内容：

```markdown
# Cosmos SDK

> 项目地址: <https://github.com/cosmos/cosmos-sdk>

Cosmos SDK 是一套用 Go 语言编写的模块化区块链开发框架，帮助开发者快速构建自定义区块链。它提供了开箱即用的核心组件、标准化的治理、权限、交易处理与模块化开发能力，使得链与链之间可互操作、可通过 IBC（Inter‑Blockchain Communication）协议互联。

## 主要特性

| 特性 | 说明 |
|------|------|
| **模块化设计** | 每个功能（如账户、治理、交易、验证等）被拆解成独立模块，用户可按需复用或自定义模块。 |
| **Cosmos Hub & IBC** | 通过 IBC 轻松实现跨链资产转移与跨链协议调用，实现链与链之间的互操作。 |
| **可扩展治理** | 支持提案投票、锁仓投票、代币持有授权等治理机制，适合 DAO 或去中心化自治组织。 |
| **生态友好** | 与 Tendermint 共识、Protobuf/GRPC、REST、WebSocket 等 RPC 接口辅以行业标准，易于集成。 |
| **安全的交易 & 通用 SDK** | 内置交易签名、验证、序列化、广播，并支持多签、租赁等高级功能。 |
| **开发与调试工具** | 提供 `cosmos-sdk` CLI、`testnet` 快速启动脚本、`simapp` 模拟应用快速验证功能。 |
| **多链互操作** | 通过 `cosmos-sdk` 的 `ModuleAccount`、`Bank` 等核心模块实现资产托管与转账。 |

## 核心功能

1. **链初始化与运行**  
   - 使用 `gaia` 或自定义链配置启动 Tendermint 共识节点。  
   - `app.py` 通过 `NewApp` 注册核心模块，生成 `App` 对象。

2. **交易处理**  
   - 交易包含 `Msgs`，每个 Msg 进入相应模块进行验证与执行。  
   - 支持多签、递延交易、单元测试。

3. **账户 & 权限**  
   - 采用 `sdk.AccAddress` 与 `sdk.Coins`，提供余额查询、代币发放。  
   - `module` 模块账号（ModuleAccount）用于托管各类系统资金。  

4. **治理与提案**  
   - 提案类型包括升级、修改、社区增发、抵押资产等。  
   - 票权与投票机制通过 `staking` 与 `governance` 模块实现。

5. **跨链功能**  
   - IBC 协议支持：轻量级通道建立、跨链转账、事件同步。  
   - 可与 Cosmos Hub、Stargate、Juno 等链互通。

## 用法示例

### 1. 创建自定义链

```bash
# 生成链文件
git clone https://github.com/cosmos/cosmos-sdk
cd cosmos-sdk
make install

# 初始化链
myapp init myhome --chain-id mychain

# 生成 genesis 账户
myapp add-genesis-account $(stake addr) 1000000uatom

# 配置交易
myapp tx bank send $(stake addr) $(stake addr) 10uatom --keyring-backend test --chain-id mychain
```

### 2. 开发自定义模块

```go
// modules/myapp/keeper/keeper.go
type Keeper struct {
    storeKey storetypes.StoreKey
    cdc      codec.Codec
}

func NewKeeper(cdc codec.Codec, key storetypes.StoreKey) Keeper {
    return Keeper{storeKey: key, cdc: cdc}
}
```

随后在 `app.go` 中注册：

```go
app.MyAppKeeper = NewKeeper(appCodec, keys[types.StoreKey])
```

### 3. 启动测试网络

```bash
# 在同一目录下启动多个节点
myapp start --keyring-backend test
```

## 快速链接

- 官方文档: <https://docs.cosmos.network>
- IBC 规范: <https://github.com/cosmos/ibc>
- 示例链(Tendermint + Gaia): <https://github.com/cosmos/gaia>
- 开发者社区: <httpsforum.cosmos.network>
