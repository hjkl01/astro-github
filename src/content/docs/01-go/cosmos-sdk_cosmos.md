---
title: cosmos-sdk
---

# Cosmos SDK

> 项目地址: <https://github.com/cosmos/cosmos-sdk>

Cosmos SDK 是一个模块化、开源的区块链 SDK，用于构建安全的、高性能的 Layer 1 链，具有完全的可定制性，被 200 多个生产链使用。开发者可以使用 Cosmos SDK 轻松快速地启动自定义区块链，这些区块链可以原生互操作。

Cosmos SDK 专为构建安全的、主权应用程序特定区块链而定制。使用 Cosmos SDK 构建的开发者可以使用涵盖标准区块链功能的预定义模块，或为特定用例创建自定义模块。这种可组合架构实现了强大的定制。SDK 为权限、治理、状态管理、账户抽象、代币化过程、应用程序逻辑等提供了抽象。

Cosmos SDK 区块链通过与 [Inter-Blockchain Communication Protocol (IBC)](https://github.com/cosmos/ibc-go) 的原生集成开箱即用地获得互操作性。Ibc-go 在 Cosmos SDK 中作为 Go 模块实现。

虽然 Cosmos SDK 与任何共识引擎即插即用，但我们推荐使用 [CometBFT](https://github.com/cometbft/cometbft) 作为快速、久经考验、高吞吐量、可配置的 BFT 状态机。CometBFT 是作为 Cosmos Stack 的一部分开发的，其发布与 SDK 一起更新。

**警告**：Cosmos SDK 大部分已稳定，但我们仍在进行一些破坏性更改。

## 快速开始

要从高层视角学习 Cosmos SDK 的工作原理，请参阅 Cosmos SDK [高层介绍](https://docs.cosmos.network/main/intro/overview)。

如果您想快速入门并学习如何在 Cosmos SDK 上构建，请访问 [Cosmos SDK 教程](https://tutorials.cosmos.network)。您也可以 fork 教程的仓库来开始构建自己的 Cosmos SDK 应用程序。

注意：我们建议始终使用最新的维护 [Go 版本](https://go.dev/dl/) 来构建 Cosmos SDK 应用程序。

## 模块

Cosmos SDK 维护了一套可以包含在区块链应用程序中的模块。有关模块的更多信息，请参阅我们的 [介绍文档](./x/README.md)。

## 模块

Cosmos SDK 维护了一套可以包含在区块链应用程序中的模块。有关模块的更多信息，请参阅我们的 [介绍文档](/cosmos/cosmos-sdk/blob/main/x/README.md)。

## 维护者

[Cosmos Labs](https://cosmoslabs.io/) 维护堆栈的核心组件：Cosmos SDK、CometBFT、IBC、Cosmos EVM 以及各种开发者工具和框架。详细的维护政策可以在 [这里](https://github.com/cosmos/security/blob/main/POLICY.md) 找到。除了开发和维护 Cosmos Stack，Cosmos Labs 为区块链解决方案提供咨询和工程服务。[联系 Cosmos Labs](https://www.cosmoslabs.io/contact)。

Cosmos Labs 是 [Interchain Foundation](https://interchain.io/) 的全资子公司，Interchain Foundation 是瑞士非营利组织，负责财务管理、资助公共产品并支持 Cosmos 的治理。

Cosmos Stack 由强大的开源贡献者社区支持。

## 历史

Cosmos SDK 于 2019 年首次发布，使用 SDK 的第一个生产区块链是 [Cosmos Hub](https://hub.cosmos.network/main)。今天，Cosmos SDK 是一个流行的、久经考验的开源框架，被数百个链使用。

Cosmos Hub 仍然接收最新的 Cosmos SDK 版本。Cosmos Hub 应用程序 `gaia` 有自己的 [cosmos/gaia 仓库](https://github.com/cosmos/gaia)。

## 开发者社区和支持

这个仓库的问题列表仅用于错误报告和功能请求。我们在 Discord、Telegram 和 Slack 上有活跃、乐于助人的社区。

**| 需要帮助？ | 支持与社区：[Discord](https://discord.com/invite/interchain) - [Telegram](https://t.me/CosmosOG) - [与专家交谈](https://cosmos.network/interest-form) - [加入 #Cosmos-tech Slack 频道](https://forms.gle/A8jawLgB8zuL1FN36) |**

## 文档和资源

**查看 Cosmos SDK 文档：[https://docs.cosmos.network/](https://docs.cosmos.network/)**

### Cosmos Stack 库

- [CometBFT](https://github.com/cometbft/cometbft) - 高性能、10k+ TPS 可配置 BFT 共识引擎。
- [Inter-Blockchain Communication Protocol (IBC)](https://github.com/cosmos/ibc-go/) - 一种区块链互操作协议，允许区块链传输以字节编码的任何类型数据。
- [Cosmos EVM](https://github.com/cosmos/evm) - Cosmos SDK 链的原生 EVM 层。

## 歧义消除

这个 Cosmos SDK 项目与 [React-Cosmos](https://github.com/react-cosmos/react-cosmos) 项目无关（目前）。非常感谢 Evan Coury 和 Ovidiu (@skidding) 为这个 GitHub 组织名称。根据我们的协议，这个歧义消除通知将保留在这里。

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

## Cosmos Stack 库

- [CometBFT](https://github.com/cometbft/cometbft) - 高性能、10k+ TPS 可配置 BFT 共识引擎。
- [Inter-Blockchain Communication Protocol (IBC)](https://github.com/cosmos/ibc-go/) - 一种区块链互操作协议，允许区块链传输以字节编码的任何类型数据。
- [Cosmos EVM](https://github.com/cosmos/evm) - Cosmos SDK 链的原生 EVM 层。

## 歧义消除

这个 Cosmos SDK 项目与 [React-Cosmos](https://github.com/react-cosmos/react-cosmos) 项目无关（目前）。非常感谢 Evan Coury 和 Ovidiu (@skidding) 为这个 GitHub 组织名称。根据我们的协议，这个歧义消除通知将保留在这里。

## 快速链接

- 官方文档: <https://docs.cosmos.network>
- IBC 规范: <https://github.com/cosmos/ibc>
- 示例链(Tendermint + Gaia): <https://github.com/cosmos/gaia>
- 开发者社区: <httpsforum.cosmos.network>
